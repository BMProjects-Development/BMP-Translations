import importlib.util
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
