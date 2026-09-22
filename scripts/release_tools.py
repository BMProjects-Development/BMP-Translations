#!/usr/bin/env python3
"""Validate, build, plan, and describe BMP Translations releases.

The script intentionally uses only Python's standard library so it can run both
locally and on a clean GitHub-hosted runner without installing dependencies.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import zipfile
from collections import defaultdict
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "release-config.json"
VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z.-]+))?(?:\+([0-9A-Za-z.-]+))?$")
MC_RE = re.compile(r"^\d+\.\d+(?:\.\d+)?$")
MARKER_RE = re.compile(r"^\s*release\s+(all|gh|cf|mr)(?:\s+(.+?))?\s*$", re.IGNORECASE)
ZERO_SHA_RE = re.compile(r"^0+$")
IGNORED_SOURCE_NAMES = {"README.md", "VERSION", "mods.json"}


class ReleaseError(RuntimeError):
    pass


def run_git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        raise ReleaseError(f"git {' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout


def load_config() -> dict[str, Any]:
    try:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReleaseError(f"Cannot read {CONFIG_PATH.relative_to(ROOT)}: {exc}") from exc

    required = {"project_name", "curseforge_project_id", "modrinth_project_id", "packs"}
    missing = sorted(required - config.keys())
    if missing:
        raise ReleaseError(f"release-config.json is missing: {', '.join(missing)}")
    if not isinstance(config["packs"], dict) or not config["packs"]:
        raise ReleaseError("release-config.json must define at least one pack")
    return config


def pack_dir(minecraft: str) -> Path:
    return ROOT / "packs" / minecraft


def read_version(minecraft: str) -> str:
    path = pack_dir(minecraft) / "VERSION"
    try:
        version = path.read_text(encoding="utf-8-sig").strip()
    except OSError as exc:
        raise ReleaseError(f"Cannot read {path.relative_to(ROOT)}: {exc}") from exc
    if not VERSION_RE.fullmatch(version):
        raise ReleaseError(f"{path.relative_to(ROOT)} must contain a SemVer value such as 1.2.3")
    return version


def strip_json_comments(text: str) -> str:
    """Remove // and /* */ comments without touching quoted strings."""
    output: list[str] = []
    index = 0
    in_string = False
    escaped = False
    while index < len(text):
        char = text[index]
        next_char = text[index + 1] if index + 1 < len(text) else ""
        if in_string:
            output.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            index += 1
            continue
        if char == '"':
            in_string = True
            output.append(char)
            index += 1
            continue
        if char == "/" and next_char == "/":
            index += 2
            while index < len(text) and text[index] not in "\r\n":
                index += 1
            continue
        if char == "/" and next_char == "*":
            index += 2
            while index + 1 < len(text) and text[index : index + 2] != "*/":
                index += 1
            index += 2
            continue
        output.append(char)
        index += 1
    return "".join(output)


def load_json_relaxed(text: str, source: str) -> Any:
    try:
        return json.loads(text.lstrip("\ufeff"))
    except json.JSONDecodeError:
        without_comments = strip_json_comments(text.lstrip("\ufeff"))
        without_trailing_commas = re.sub(r",\s*([}\]])", r"\1", without_comments)
        try:
            return json.loads(without_trailing_commas)
        except json.JSONDecodeError as exc:
            raise ReleaseError(f"Invalid JSON in {source}: {exc}") from exc


def validate_pack(minecraft: str) -> list[str]:
    config = load_config()
    if minecraft not in config["packs"]:
        raise ReleaseError(f"Unknown Minecraft version: {minecraft}")

    directory = pack_dir(minecraft)
    if not directory.is_dir():
        raise ReleaseError(f"Missing directory: {directory.relative_to(ROOT)}")
    version = read_version(minecraft)

    required_paths = [directory / "pack.mcmeta", directory / "pack.png", directory / "assets"]
    for path in required_paths:
        if not path.exists():
            raise ReleaseError(f"Missing required pack path: {path.relative_to(ROOT)}")

    mcmeta_path = directory / "pack.mcmeta"
    mcmeta = load_json_relaxed(mcmeta_path.read_text(encoding="utf-8-sig"), str(mcmeta_path.relative_to(ROOT)))
    pack_meta = mcmeta.get("pack") if isinstance(mcmeta, dict) else None
    if not isinstance(pack_meta, dict) or not isinstance(pack_meta.get("pack_format"), int):
        raise ReleaseError(f"{mcmeta_path.relative_to(ROOT)} must contain an integer pack.pack_format")
    if not isinstance(pack_meta.get("description"), (str, dict, list)):
        raise ReleaseError(f"{mcmeta_path.relative_to(ROOT)} must contain pack.description")

    warnings: list[str] = []
    seen_casefolded: dict[str, str] = {}
    json_count = 0
    for path in sorted(directory.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(directory).as_posix()
        folded = relative.casefold()
        if folded in seen_casefolded and seen_casefolded[folded] != relative:
            raise ReleaseError(f"Case-conflicting paths: {seen_casefolded[folded]} and {relative}")
        seen_casefolded[folded] = relative
        if path.suffix.casefold() == ".zip":
            raise ReleaseError(f"Nested ZIP is not allowed in pack sources: {path.relative_to(ROOT)}")
        if path.suffix.casefold() == ".json":
            json_count += 1
            load_json_relaxed(path.read_text(encoding="utf-8-sig"), str(path.relative_to(ROOT)))

    if json_count == 0:
        warnings.append(f"{minecraft}: no JSON files found")
    print(f"Validated Minecraft {minecraft} v{version}: {json_count} JSON files")
    return warnings


def source_files(minecraft: str) -> list[Path]:
    directory = pack_dir(minecraft)
    files: list[Path] = []
    for path in directory.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(directory)
        if len(relative.parts) == 1 and relative.name in IGNORED_SOURCE_NAMES:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(directory).as_posix())


def build_pack(minecraft: str, output_dir: Path) -> Path:
    validate_pack(minecraft)
    version = read_version(minecraft)
    directory = pack_dir(minecraft)
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"BMP_Translations_{minecraft}_v{version}.zip"

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in source_files(minecraft):
            relative = path.relative_to(directory).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    print(f"Built {archive.relative_to(ROOT)}")
    return archive


def semver_key(version: str) -> tuple[int, int, int, str, str]:
    match = VERSION_RE.fullmatch(version)
    if not match:
        return (-1, -1, -1, "", "")
    major, minor, patch, prerelease, build = match.groups()
    return int(major), int(minor), int(patch), prerelease or "~", build or ""


def compare_semver(left: str, right: str) -> int:
    """Return -1, 0, or 1 using SemVer precedence (build metadata ignored)."""
    left_match = VERSION_RE.fullmatch(left)
    right_match = VERSION_RE.fullmatch(right)
    if not left_match or not right_match:
        raise ReleaseError(f"Cannot compare invalid versions: {left!r}, {right!r}")
    left_parts = left_match.groups()
    right_parts = right_match.groups()
    left_core = tuple(map(int, left_parts[:3]))
    right_core = tuple(map(int, right_parts[:3]))
    if left_core != right_core:
        return (left_core > right_core) - (left_core < right_core)

    left_pre = left_parts[3]
    right_pre = right_parts[3]
    if left_pre is None or right_pre is None:
        if left_pre is None and right_pre is None:
            return 0
        return 1 if left_pre is None else -1

    left_ids = left_pre.split(".")
    right_ids = right_pre.split(".")
    for left_id, right_id in zip(left_ids, right_ids):
        if left_id == right_id:
            continue
        left_numeric = left_id.isdigit()
        right_numeric = right_id.isdigit()
        if left_numeric and right_numeric:
            return (int(left_id) > int(right_id)) - (int(left_id) < int(right_id))
        if left_numeric != right_numeric:
            return -1 if left_numeric else 1
        return (left_id > right_id) - (left_id < right_id)
    return (len(left_ids) > len(right_ids)) - (len(left_ids) < len(right_ids))


def exact_release_tag(minecraft: str, version: str) -> str:
    return f"mc{minecraft}-v{version}"


def latest_release_tag(minecraft: str, head: str, exclude: str | None = None) -> str | None:
    pattern = f"mc{minecraft}-v*"
    candidates: list[tuple[tuple[int, int, int, str, str], str]] = []
    for tag in run_git("tag", "--merged", head, "--list", pattern).splitlines():
        if tag == exclude:
            continue
        prefix = f"mc{minecraft}-v"
        version = tag[len(prefix) :]
        if VERSION_RE.fullmatch(version):
            candidates.append((semver_key(version), tag))
    return max(candidates, default=((), None))[1]


def first_source_commit(minecraft: str, head: str) -> str | None:
    path = f"packs/{minecraft}/pack.mcmeta"
    commits = run_git("log", "--diff-filter=A", "--format=%H", "--reverse", head, "--", path).splitlines()
    return commits[0] if commits else None


def changelog_base(minecraft: str, head: str, version: str | None = None) -> str:
    current_tag = exact_release_tag(minecraft, version) if version else None
    tag = latest_release_tag(minecraft, head, exclude=current_tag)
    if tag:
        return tag
    first_commit = first_source_commit(minecraft, head)
    if first_commit:
        return first_commit
    parent = run_git("rev-parse", f"{head}^").strip()
    return parent


def git_file(ref: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if result.returncode != 0:
        return None
    return result.stdout.decode("utf-8-sig", errors="replace")


def tree_files(ref: str, prefix: str) -> set[str]:
    output = run_git("ls-tree", "-r", "--name-only", ref, "--", prefix, check=False)
    return {line for line in output.splitlines() if line}


def namespace_from_path(path: str, minecraft: str) -> str | None:
    parts = PurePosixPath(path).parts
    expected = ("packs", minecraft, "assets")
    if len(parts) >= 4 and parts[:3] == expected:
        return parts[3]
    return None


def translation_map(text: str | None, source: str) -> dict[str, str]:
    if text is None:
        return {}
    if source.casefold().endswith(".json"):
        parsed = load_json_relaxed(text, source)
        if not isinstance(parsed, dict):
            return {}
        return {str(key): json.dumps(value, ensure_ascii=False, sort_keys=True) for key, value in parsed.items()}
    result: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        result[key.strip()] = value
    return result


def changed_paths(base: str, head: str, minecraft: str) -> set[str]:
    prefix = f"packs/{minecraft}"
    output = run_git("diff", "--name-only", "--find-renames", base, head, "--", prefix)
    return {line for line in output.splitlines() if line}


def load_mod_names(minecraft: str) -> dict[str, str]:
    path = pack_dir(minecraft) / "mods.json"
    if not path.exists():
        return {}
    parsed = load_json_relaxed(path.read_text(encoding="utf-8-sig"), str(path.relative_to(ROOT)))
    if not isinstance(parsed, dict):
        raise ReleaseError(f"{path.relative_to(ROOT)} must contain an object")
    names: dict[str, str] = {}
    for namespace, value in parsed.items():
        if isinstance(value, str):
            names[str(namespace)] = value
        elif isinstance(value, dict) and isinstance(value.get("name"), str):
            names[str(namespace)] = value["name"]
    return names


def describe_namespace(namespace: str, names: dict[str, str]) -> str:
    name = names.get(namespace)
    return f"{name} (`{namespace}`)" if name else f"`{namespace}`"


def english_key_count(count: int, action: str) -> str:
    noun = "key" if count == 1 else "keys"
    return f"{count} {noun} {action}"


def russian_key_count(count: int, singular_action: str, plural_action: str) -> str:
    last_two = count % 100
    last = count % 10
    if last == 1 and last_two != 11:
        noun = "ключ"
        action = singular_action
    elif last in {2, 3, 4} and last_two not in {12, 13, 14}:
        noun = "ключа"
        action = plural_action
    else:
        noun = "ключей"
        action = plural_action
    return f"{action} {count} {noun}"


def generate_changelog(minecraft: str, head: str, output: Path) -> Path:
    config = load_config()
    if minecraft not in config["packs"]:
        raise ReleaseError(f"Unknown Minecraft version: {minecraft}")
    version = read_version(minecraft)
    base = changelog_base(minecraft, head, version)
    prefix = f"packs/{minecraft}/assets/"
    base_files = tree_files(base, prefix)
    head_files = tree_files(head, prefix)
    paths = changed_paths(base, head, minecraft)
    names = load_mod_names(minecraft)

    base_namespaces = {namespace_from_path(path, minecraft) for path in base_files}
    head_namespaces = {namespace_from_path(path, minecraft) for path in head_files}
    base_namespaces.discard(None)
    head_namespaces.discard(None)
    touched = {namespace_from_path(path, minecraft) for path in paths}
    touched.discard(None)

    added = sorted((head_namespaces - base_namespaces) & touched)
    removed = sorted((base_namespaces - head_namespaces) & touched)
    updated = sorted(touched - set(added) - set(removed))

    key_stats: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
    for path in sorted(paths):
        namespace = namespace_from_path(path, minecraft)
        if not namespace or not re.search(r"/lang/.*\.(?:json|lang)$", path, re.IGNORECASE):
            continue
        before = translation_map(git_file(base, path), f"{base}:{path}")
        after = translation_map(git_file(head, path), f"{head}:{path}")
        before_keys = set(before)
        after_keys = set(after)
        key_stats[namespace][0] += len(after_keys - before_keys)
        key_stats[namespace][1] += sum(before[key] != after[key] for key in before_keys & after_keys)
        key_stats[namespace][2] += len(before_keys - after_keys)

    root_changes = sorted(
        PurePosixPath(path).name
        for path in paths
        if path in {f"packs/{minecraft}/pack.mcmeta", f"packs/{minecraft}/pack.png"}
    )

    def english_updated(namespace: str) -> str:
        added_keys, changed_keys, removed_keys = key_stats[namespace]
        details = []
        if added_keys:
            details.append(english_key_count(added_keys, "added"))
        if changed_keys:
            details.append(english_key_count(changed_keys, "updated"))
        if removed_keys:
            details.append(english_key_count(removed_keys, "removed"))
        suffix = f": {', '.join(details)}" if details else ""
        return f"- {describe_namespace(namespace, names)}{suffix}."

    def russian_updated(namespace: str) -> str:
        added_keys, changed_keys, removed_keys = key_stats[namespace]
        details = []
        if added_keys:
            details.append(russian_key_count(added_keys, "добавлен", "добавлено"))
        if changed_keys:
            details.append(russian_key_count(changed_keys, "изменён", "изменено"))
        if removed_keys:
            details.append(russian_key_count(removed_keys, "удалён", "удалено"))
        suffix = f": {', '.join(details)}" if details else ""
        return f"- {describe_namespace(namespace, names)}{suffix}."

    lines = [
        f"# {config['project_name']} {minecraft} — v{version}",
        "",
        "## English",
        "",
    ]
    if not (added or removed or updated or root_changes):
        lines.extend(["Maintenance release with no resource-content changes.", ""])
    else:
        if added:
            lines.extend(["### Added translations", "", *[f"- {describe_namespace(item, names)}." for item in added], ""])
        if updated:
            lines.extend(["### Updated translations", "", *[english_updated(item) for item in updated], ""])
        if removed:
            lines.extend(["### Removed translations", "", *[f"- {describe_namespace(item, names)}." for item in removed], ""])
        if root_changes:
            lines.extend(["### Pack changes", "", *[f"- Updated `{item}`." for item in root_changes], ""])

    lines.extend(["## Русский", ""])
    if not (added or removed or updated or root_changes):
        lines.extend(["Технический выпуск без изменений содержимого ресурспака.", ""])
    else:
        if added:
            lines.extend(["### Добавлены переводы", "", *[f"- {describe_namespace(item, names)}." for item in added], ""])
        if updated:
            lines.extend(["### Обновлены переводы", "", *[russian_updated(item) for item in updated], ""])
        if removed:
            lines.extend(["### Удалены переводы", "", *[f"- {describe_namespace(item, names)}." for item in removed], ""])
        if root_changes:
            lines.extend(["### Изменения ресурспака", "", *[f"- Обновлён `{item}`." for item in root_changes], ""])

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Generated {output.relative_to(ROOT)} from {base}..{head}")
    return output


def normalize_before(before: str, head: str) -> str:
    if not before or ZERO_SHA_RE.fullmatch(before):
        return run_git("rev-parse", f"{head}^").strip()
    return before


def parse_markers(message: str, known_packs: Iterable[str]) -> tuple[set[str], set[str]] | None:
    platforms: set[str] = set()
    explicit_packs: set[str] = set()
    known = set(known_packs)
    found = False
    for line in message.splitlines():
        match = MARKER_RE.fullmatch(line)
        if not match:
            continue
        found = True
        target, raw_packs = match.groups()
        target = target.casefold()
        platforms.update({"gh", "cf", "mr"} if target == "all" else {target})
        if raw_packs:
            requested = {part for part in re.split(r"[\s,]+", raw_packs.strip()) if part}
            invalid = sorted(item for item in requested if item not in known or not MC_RE.fullmatch(item))
            if invalid:
                raise ReleaseError(f"Unknown Minecraft version in release marker: {', '.join(invalid)}")
            explicit_packs.update(requested)
    if not found:
        return None
    return platforms, explicit_packs


def changed_version_packs(before: str, head: str, known_packs: Iterable[str]) -> set[str]:
    output = run_git("diff", "--name-only", before, head, "--", "packs/*/VERSION")
    known = set(known_packs)
    result = set()
    for line in output.splitlines():
        parts = PurePosixPath(line).parts
        if len(parts) == 3 and parts[0] == "packs" and parts[2] == "VERSION" and parts[1] in known:
            result.add(parts[1])
    return result


def write_github_output(values: dict[str, str]) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        for key, value in values.items():
            print(f"{key}={value}")
        return
    with open(output_path, "a", encoding="utf-8") as output:
        for key, value in values.items():
            output.write(f"{key}={value}\n")


def create_plan(before: str, head: str, message: str) -> dict[str, str]:
    config = load_config()
    known_packs = config["packs"].keys()
    parsed = parse_markers(message, known_packs)
    empty_matrix = json.dumps({"include": []}, separators=(",", ":"))
    if parsed is None:
        return {"release": "false", "gh": "false", "cf": "false", "mr": "false", "matrix": empty_matrix}

    platforms, explicit_packs = parsed
    before = normalize_before(before, head)
    head_parent = run_git("rev-parse", f"{head}^", check=False).strip() or before
    bumped_packs = changed_version_packs(head_parent, head, known_packs)
    selected = explicit_packs or bumped_packs
    if not selected:
        raise ReleaseError(
            "A release marker was found, but no pack VERSION changed. "
            "Bump packs/<minecraft>/VERSION or add Minecraft versions to the marker for a retry."
        )

    if not explicit_packs:
        for minecraft in selected:
            previous_version = git_file(head_parent, f"packs/{minecraft}/VERSION")
            if previous_version is not None:
                previous_version = previous_version.strip()
                current_version = read_version(minecraft)
                if not VERSION_RE.fullmatch(previous_version):
                    raise ReleaseError(f"Previous VERSION for Minecraft {minecraft} is invalid: {previous_version!r}")
                if compare_semver(current_version, previous_version) <= 0:
                    raise ReleaseError(
                        f"Minecraft {minecraft} VERSION must increase: {previous_version} -> {current_version}"
                    )
            paths = changed_paths(changelog_base(minecraft, head, read_version(minecraft)), head, minecraft)
            content_paths = {
                path
                for path in paths
                if path
                not in {
                    f"packs/{minecraft}/VERSION",
                    f"packs/{minecraft}/README.md",
                    f"packs/{minecraft}/mods.json",
                }
            }
            if not content_paths:
                raise ReleaseError(f"Minecraft {minecraft} changed VERSION but has no resource-content changes")

    include = []
    for minecraft in sorted(selected, key=lambda value: tuple(map(int, value.split(".")))):
        validate_pack(minecraft)
        version = read_version(minecraft)
        include.append(
            {
                "minecraft": minecraft,
                "version": version,
                "tag": exact_release_tag(minecraft, version),
                "artifact": f"release-mc{minecraft}-v{version}",
                "zip": f"BMP_Translations_{minecraft}_v{version}.zip",
                "changelog": f"CHANGELOG_{minecraft}_v{version}.md",
                "name": f"{config['project_name']} {minecraft} - v{version}",
                "game_versions": config["packs"][minecraft]["game_versions"],
                "retry": bool(explicit_packs),
                "curseforge_project_id": config["curseforge_project_id"],
                "modrinth_project_id": config["modrinth_project_id"],
            }
        )
    return {
        "release": "true",
        "gh": str("gh" in platforms).lower(),
        "cf": str("cf" in platforms).lower(),
        "mr": str("mr" in platforms).lower(),
        "matrix": json.dumps({"include": include}, ensure_ascii=False, separators=(",", ":")),
    }


def command_validate(args: argparse.Namespace) -> None:
    config = load_config()
    versions = args.minecraft or list(config["packs"])
    warnings: list[str] = []
    for minecraft in versions:
        warnings.extend(validate_pack(minecraft))
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)


def command_build(args: argparse.Namespace) -> None:
    config = load_config()
    versions = list(config["packs"]) if args.all else [args.minecraft]
    output = (ROOT / args.output).resolve()
    for minecraft in versions:
        build_pack(minecraft, output)


def command_changelog(args: argparse.Namespace) -> None:
    generate_changelog(args.minecraft, args.head, (ROOT / args.output).resolve())


def command_plan(args: argparse.Namespace) -> None:
    message = args.message
    if message is None:
        message = run_git("log", "-1", "--format=%B", args.head)
    plan = create_plan(args.before, args.head, message)
    write_github_output(plan)
    print(json.dumps(plan, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="validate one or all resource packs")
    validate.add_argument("--minecraft", action="append", help="Minecraft version; may be repeated")
    validate.set_defaults(func=command_validate)

    build = subparsers.add_parser("build", help="build deterministic release ZIP files")
    build_group = build.add_mutually_exclusive_group(required=True)
    build_group.add_argument("--minecraft", help="Minecraft version")
    build_group.add_argument("--all", action="store_true", help="build every configured pack")
    build.add_argument("--output", default="dist", help="output directory relative to repository root")
    build.set_defaults(func=command_build)

    changelog = subparsers.add_parser("changelog", help="generate an English/Russian changelog")
    changelog.add_argument("--minecraft", required=True, help="Minecraft version")
    changelog.add_argument("--head", default="HEAD", help="release commit")
    changelog.add_argument("--output", required=True, help="output Markdown path")
    changelog.set_defaults(func=command_changelog)

    plan = subparsers.add_parser("plan", help="build a GitHub Actions release matrix")
    plan.add_argument("--before", required=True, help="push before SHA")
    plan.add_argument("--head", default="HEAD", help="push head SHA")
    plan.add_argument("--message", help="override the head commit message")
    plan.set_defaults(func=command_plan)
    return parser


def main() -> int:
    try:
        args = build_parser().parse_args()
        args.func(args)
    except ReleaseError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
