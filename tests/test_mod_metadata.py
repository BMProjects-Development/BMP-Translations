import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "mod_metadata.py"
SPEC = importlib.util.spec_from_file_location("mod_metadata", SCRIPT)
mod_metadata = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mod_metadata)


class ModMetadataTests(unittest.TestCase):
    def test_short_acronym_does_not_create_false_partial_match(self):
        score = mod_metadata.similarity(
            "ae2importexportcard",
            "AllTheCompressed",
            "https://www.curseforge.com/minecraft/mc-mods/allthecompressed",
        )
        self.assertLess(score, 0.78)

    def test_meaningful_acronym_is_supported(self):
        self.assertEqual(mod_metadata.similarity("bhc", "Baubley Heart Canisters"), 1.0)

    def test_legacy_link_is_assigned_to_matching_namespace_only(self):
        records = [
            {"name": "AE2 Import Export Card", "namespaces": ["ae2importexportcard"], "resolved": True},
            {"name": "AllTheCompressed", "namespaces": ["allthecompressed"], "resolved": True},
        ]
        links = [
            {
                "name": "AllTheCompressed",
                "curseforge": "https://www.curseforge.com/minecraft/mc-mods/allthecompressed",
            }
        ]
        mod_metadata.overlay_legacy(records, links)
        self.assertNotIn("curseforge", records[0])
        self.assertEqual(records[1]["curseforge"], links[0]["curseforge"])

    def test_platform_links_omit_missing_platform(self):
        entry = {"name": "Example", "modrinth": "https://modrinth.com/mod/example"}
        rendered = mod_metadata.mod_line(entry)
        self.assertIn("Modrinth", rendered)
        self.assertNotIn("CurseForge", rendered)

    def test_sync_includes_year_based_pack_and_preserves_reviewed_catalog(self):
        temporary_root = SCRIPT.parents[1] / ".release"
        temporary_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as temporary:
            root = Path(temporary)
            config = {"packs": {
                "1.21.1": {"game_versions": ["1.21.1"]},
                "26": {"game_versions": ["26.1", "26.3"]},
            }}
            (root / "release-config.json").write_text(json.dumps(config), encoding="utf-8")
            (root / "README.md").write_text(
                mod_metadata.ROOT_BEGIN + "\n" + mod_metadata.ROOT_END + "\n", encoding="utf-8"
            )
            platform = root / "docs" / "platform"
            platform.mkdir(parents=True)
            for name in ("MODRINTH_INTRO_EN.md", "MODRINTH_INTRO_RU.md", "MODRINTH_FOOTER.md"):
                (platform / name).write_text("Description template", encoding="utf-8")
            for minecraft in config["packs"]:
                pack = root / "packs" / minecraft
                (pack / "assets" / "echoes").mkdir(parents=True)
                (pack / "mods.json").write_text(json.dumps({"minecraft": minecraft, "mods": [{
                    "name": "Timeless Echoes", "namespaces": ["echoes"], "resolved": True,
                    "curseforge": "https://www.curseforge.com/minecraft/mc-mods/timeless-echoes",
                }]}), encoding="utf-8")
            with (
                mock.patch.object(mod_metadata, "ROOT", root),
                mock.patch.object(mod_metadata, "CONFIG_PATH", root / "release-config.json"),
                mock.patch.object(mod_metadata, "modrinth_exact", return_value={
                    "echoes": {"title": "Unrelated Mod", "slug": "echoes"},
                }),
            ):
                mod_metadata.sync(discover=True, rebuild=False)
            record, = json.loads((root / "packs/26/mods.json").read_text(encoding="utf-8"))["mods"]
            self.assertEqual(record["name"], "Timeless Echoes")
            self.assertNotIn("modrinth", record)
            for language in ("EN", "RU"):
                text = (root / f"packs/26/README_{language}.md").read_text(encoding="utf-8")
                self.assertIn("Minecraft 26", text)
                self.assertIn("Timeless Echoes", text)
            readme = (root / "README.md").read_text(encoding="utf-8")
            self.assertLess(readme.index("Minecraft 26:"), readme.index("Minecraft 1.21.1:"))
            description = (platform / "MODRINTH_DESCRIPTION.md").read_text(encoding="utf-8")
            self.assertLess(description.index("### Minecraft 26"), description.index("### Minecraft 1.21.1"))


if __name__ == "__main__":
    unittest.main()
