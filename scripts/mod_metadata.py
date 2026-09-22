#!/usr/bin/env python3
"""Discover translated mods and generate repository/platform descriptions."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "release-config.json"
USER_AGENT = "BMProjects-Development/BMP-Translations (github.com/BMProjects-Development/BMP-Translations)"
ROOT_BEGIN = "<!-- BEGIN GENERATED TRANSLATED MODS -->"
ROOT_END = "<!-- END GENERATED TRANSLATED MODS -->"
MARKDOWN_LINK_RE = re.compile(r"\[([^\n]*?)\]\((https?://[^)]+)\)")


class MetadataError(RuntimeError):
    pass


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def minecraft_key(value: str) -> tuple[int, ...]:
    return tuple(map(int, value.split(".")))


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def acronym(value: str) -> str:
    ignored = {"a", "an", "and", "for", "of", "the", "to"}
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", value)
    words = re.findall(r"[a-z0-9]+", value.casefold())
    return "".join(word[0] for word in words if word not in ignored)


def humanize(namespace: str) -> str:
    replacements = {
        "ae2": "AE2", "api": "API", "ftb": "FTB", "jei": "JEI",
        "me": "ME", "nbt": "NBT", "rftools": "RFTools", "xp": "XP",
    }
    words = re.split(r"[_-]+", namespace)
    return " ".join(replacements.get(word.casefold(), word[:1].upper() + word[1:]) for word in words)


def similarity(namespace: str, name: str, url: str = "") -> float:
    namespace_key = normalize(namespace)
    values = [normalize(name), acronym(name)]
    if url:
        values.append(normalize(urllib.parse.urlparse(url).path.rstrip("/").split("/")[-1]))
    scores = []
    for value in values:
        if not value:
            continue
        if namespace_key == value:
            scores.append(1.0)
        elif min(len(namespace_key), len(value)) >= 4 and (namespace_key in value or value in namespace_key):
            scores.append(0.86)
        else:
            scores.append(SequenceMatcher(None, namespace_key, value).ratio())
    return max(scores, default=0.0)


def request_json(url: str, retries: int = 3) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            if exc.code == 429 and attempt + 1 < retries:
                time.sleep(float(exc.headers.get("Retry-After", "2")))
                continue
            raise MetadataError(f"HTTP {exc.code} while requesting {url}") from exc
        except urllib.error.URLError as exc:
            if attempt + 1 == retries:
                raise MetadataError(f"Cannot request {url}: {exc}") from exc
            time.sleep(attempt + 1)
    return None


def modrinth_exact(namespaces: Iterable[str]) -> dict[str, dict[str, Any]]:
    values = sorted(set(namespaces))
    result: dict[str, dict[str, Any]] = {}
    for offset in range(0, len(values), 80):
        chunk = values[offset : offset + 80]
        query = urllib.parse.urlencode({"ids": json.dumps(chunk, separators=(",", ":"))})
        projects = request_json(f"https://api.modrinth.com/v2/projects?{query}") or []
        for project in projects:
            slug = project.get("slug")
            if isinstance(slug, str):
                result[normalize(slug)] = project
    return result


def modrinth_search(namespace: str, minecraft_versions: set[str]) -> dict[str, Any] | None:
    query = urllib.parse.urlencode({
        "query": namespace,
        "facets": json.dumps([["project_type:mod"]], separators=(",", ":")),
        "limit": "5",
    })
    response = request_json(f"https://api.modrinth.com/v2/search?{query}") or {}
    candidates = []
    for project in response.get("hits", []):
        versions = set(project.get("versions") or [])
        if minecraft_versions and versions and not minecraft_versions.intersection(versions):
            continue
        score = max(
            similarity(namespace, str(project.get("title", ""))),
            similarity(namespace, str(project.get("slug", ""))),
        )
        candidates.append((score, project))
    candidates.sort(key=lambda item: item[0], reverse=True)
    if not candidates or candidates[0][0] < 0.88:
        return None
    if len(candidates) > 1 and candidates[0][0] - candidates[1][0] < 0.08:
        return None
    return candidates[0][1]


def legacy_links(readme: Path) -> list[dict[str, str]]:
    if readme.is_file():
        text = readme.read_text(encoding="utf-8-sig")
    else:
        relative = readme.relative_to(ROOT).as_posix()
        result = subprocess.run(
            ["git", "show", f"HEAD:{relative}"], cwd=ROOT, text=True,
            encoding="utf-8", errors="replace", stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, check=False,
        )
        text = result.stdout if result.returncode == 0 else ""
    entries = []
    for name, url in MARKDOWN_LINK_RE.findall(text):
        host = urllib.parse.urlparse(url).netloc.casefold()
        platform = "curseforge" if "curseforge.com" in host else "modrinth" if "modrinth.com" in host else ""
        if platform:
            entries.append({"name": name.strip("[] "), platform: url})
    return entries


def load_catalog(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("mods"), list):
        raise MetadataError(f"{path.relative_to(ROOT)} must contain a mods array")
    return [entry for entry in raw["mods"] if isinstance(entry, dict)]


def project_record(namespace: str, project: dict[str, Any] | None) -> dict[str, Any]:
    if project:
        title = str(project.get("title") or humanize(namespace))
        slug = str(project.get("slug") or "")
        return {
            "name": title,
            "namespaces": [namespace],
            "modrinth": f"https://modrinth.com/mod/{slug}",
            "resolved": True,
        }
    return {"name": humanize(namespace), "namespaces": [namespace], "resolved": False}


def overlay_legacy(records: list[dict[str, Any]], links: list[dict[str, str]]) -> None:
    unused = set(range(len(links)))
    for record in records:
        namespace = record["namespaces"][0]
        scored = []
        for index in unused:
            entry = links[index]
            score = max(
                similarity(namespace, entry["name"], entry.get("curseforge", "") or entry.get("modrinth", "")),
                SequenceMatcher(None, normalize(record["name"]), normalize(entry["name"])).ratio(),
            )
            scored.append((score, index, entry))
        if not scored:
            continue
        score, index, entry = max(scored, key=lambda item: item[0])
        if score < 0.90:
            continue
        record["name"] = entry["name"]
        for platform in ("curseforge", "modrinth"):
            if entry.get(platform):
                record[platform] = entry[platform]
        record["resolved"] = True
        unused.remove(index)


def merge_same_projects(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[tuple[str, str, str], dict[str, Any]] = {}
    for record in records:
        key = (normalize(str(record.get("name", ""))), str(record.get("curseforge", "")), str(record.get("modrinth", "")))
        if key not in merged:
            merged[key] = dict(record)
            merged[key]["namespaces"] = list(record.get("namespaces", []))
        else:
            merged[key]["namespaces"].extend(record.get("namespaces", []))
            merged[key]["resolved"] = bool(merged[key].get("resolved")) and bool(record.get("resolved"))
    for record in merged.values():
        record["namespaces"] = sorted(set(record["namespaces"]))
    return sorted(merged.values(), key=lambda entry: str(entry["name"]).casefold())


def project_description_names(project_id: str, versions: set[str]) -> dict[str, list[dict[str, str]]]:
    project = request_json(f"https://api.modrinth.com/v2/project/{urllib.parse.quote(project_id)}") or {}
    result = {version: [] for version in versions}
    current = ""
    for raw_line in str(project.get("body", "")).splitlines():
        line = raw_line.strip()
        heading = line.lstrip("# ").strip()
        if heading in versions:
            current = heading
            continue
        if current and line.startswith("- "):
            name = re.sub(r"\s*[—-]\s*\[[^]]+\]\([^)]+\).*$", "", line[2:]).strip()
            if name:
                result[current].append({"name": name})
    return result


def update_catalog(
    minecraft: str,
    discover: bool,
    exact: dict[str, dict[str, Any]],
    rebuild: bool,
    known_names: list[dict[str, str]],
) -> list[dict[str, Any]]:
    config = load_config()
    directory = ROOT / "packs" / minecraft
    namespaces = sorted(path.name for path in (directory / "assets").iterdir() if path.is_dir())
    path = directory / "mods.json"
    previous = [] if rebuild else load_catalog(path)
    previous_by_namespace = {
        namespace: entry for entry in previous for namespace in entry.get("namespaces", []) if isinstance(namespace, str)
    }
    links = legacy_links(directory / "README.md") + known_names
    game_versions = set(config["packs"][minecraft]["game_versions"])
    records = []
    unknown = []
    for namespace in namespaces:
        if namespace in previous_by_namespace:
            record = dict(previous_by_namespace[namespace])
            record["namespaces"] = [namespace]
        else:
            project = exact.get(normalize(namespace)) if discover else None
            record = project_record(namespace, project)
            if not project:
                unknown.append(record)
        records.append(record)

    overlay_legacy(records, links)
    if discover:
        for record in unknown:
            if record.get("resolved"):
                continue
            namespace = record["namespaces"][0]
            project = modrinth_search(namespace, game_versions)
            if project:
                record.update(project_record(namespace, project))

    records = merge_same_projects(records)
    payload = {"minecraft": minecraft, "mods": records}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    unresolved = sum(not bool(entry.get("resolved")) for entry in records)
    print(f"Minecraft {minecraft}: {len(records)} mod entries, {unresolved} require metadata review")
    return records


def platform_links(entry: dict[str, Any]) -> str:
    links = []
    if entry.get("curseforge"):
        links.append(f"[CurseForge]({entry['curseforge']})")
    if entry.get("modrinth"):
        links.append(f"[Modrinth]({entry['modrinth']})")
    return " · ".join(links)


def mod_line(entry: dict[str, Any]) -> str:
    links = platform_links(entry)
    return f"- {entry['name']} — {links}" if links else f"- {entry['name']}"


def write_pack_readmes(minecraft: str, records: list[dict[str, Any]]) -> None:
    directory = ROOT / "packs" / minecraft
    lines = "\n".join(mod_line(entry) for entry in records)
    english = (
        f"# Translated mods for Minecraft {minecraft}\n\n"
        f"BMP Translations currently contains translations for {len(records)} mods and add-ons on Minecraft {minecraft}.\n\n"
        "The list is generated from the resource-pack sources. A platform link is shown only when the project was found there.\n\n"
        f"{lines}\n"
    )
    russian = (
        f"# Переведённые моды для Minecraft {minecraft}\n\n"
        f"BMP Translations содержит переводы для {len(records)} модов и дополнений на Minecraft {minecraft}.\n\n"
        "Список создаётся автоматически из исходников ресурспака. Ссылка на площадку отображается только тогда, когда проект на ней найден.\n\n"
        f"{lines}\n"
    )
    (directory / "README_EN.md").write_text(english, encoding="utf-8")
    (directory / "README_RU.md").write_text(russian, encoding="utf-8")


def write_root_readme(versions: list[str]) -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    lines = ["## Translated mods | Переведённые моды", ""]
    for minecraft in sorted(versions, key=minecraft_key, reverse=True):
        lines.append(f"- Minecraft {minecraft}: [English](packs/{minecraft}/README_EN.md) · [Русский](packs/{minecraft}/README_RU.md)")
    block = ROOT_BEGIN + "\n" + "\n".join(lines) + "\n" + ROOT_END
    if ROOT_BEGIN in text and ROOT_END in text:
        text = re.sub(re.escape(ROOT_BEGIN) + r".*?" + re.escape(ROOT_END), block, text, flags=re.DOTALL)
    else:
        anchor = "\n## Repository structure"
        text = text.replace(anchor, f"\n\n{block}\n{anchor}") if anchor in text else text.rstrip() + f"\n\n{block}\n"
    path.write_text(text, encoding="utf-8")


def read_template(name: str) -> str:
    return (ROOT / "docs" / "platform" / name).read_text(encoding="utf-8").strip()


def description_section(title: str, versions: list[str], catalogs: dict[str, list[dict[str, Any]]], count_word: str) -> str:
    output = [f"## {title}", ""]
    for minecraft in sorted(versions, key=minecraft_key, reverse=True):
        records = catalogs[minecraft]
        output.extend([
            f"### Minecraft {minecraft}", "", "<details>",
            f"<summary>{len(records)} {count_word}</summary>", "",
            *(mod_line(entry) for entry in records), "", "</details>", "",
        ])
    return "\n".join(output).rstrip()


def write_modrinth_description(versions: list[str], catalogs: dict[str, list[dict[str, Any]]]) -> None:
    output = "\n\n".join([
        "# BMP Translations",
        "## English\n\n" + read_template("MODRINTH_INTRO_EN.md"),
        "## Русский\n\n" + read_template("MODRINTH_INTRO_RU.md"),
        description_section(
            "Translated mods | Переведённые моды",
            versions,
            catalogs,
            "mods and add-ons | модов и дополнений",
        ),
        read_template("MODRINTH_FOOTER.md"),
    ])
    (ROOT / "docs" / "platform" / "MODRINTH_DESCRIPTION.md").write_text(output + "\n", encoding="utf-8")


def sync(discover: bool, rebuild: bool) -> None:
    config = load_config()
    versions = list(config["packs"])
    namespaces = {
        path.name for minecraft in versions
        for path in (ROOT / "packs" / minecraft / "assets").iterdir() if path.is_dir()
    }
    exact = modrinth_exact(namespaces) if discover else {}
    known_names = (
        project_description_names(config["modrinth_project_id"], set(versions))
        if discover and rebuild
        else {version: [] for version in versions}
    )
    catalogs = {}
    for minecraft in versions:
        catalogs[minecraft] = update_catalog(
            minecraft, discover, exact, rebuild, known_names.get(minecraft, [])
        )
        write_pack_readmes(minecraft, catalogs[minecraft])
        (ROOT / "packs" / minecraft / "README.md").unlink(missing_ok=True)
    write_root_readme(versions)
    write_modrinth_description(versions, catalogs)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["sync"])
    parser.add_argument("--discover", action="store_true", help="query Modrinth for new namespaces")
    parser.add_argument("--rebuild", action="store_true", help="recreate catalogs instead of preserving entries")
    return parser


def main() -> int:
    try:
        args = build_parser().parse_args()
        sync(args.discover, args.rebuild)
    except (MetadataError, OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
