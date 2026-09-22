import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "release_tools.py"
SPEC = importlib.util.spec_from_file_location("release_tools", SCRIPT)
release_tools = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(release_tools)


class ReleaseToolsTests(unittest.TestCase):
    def test_comment_stripping_preserves_urls_and_comment_like_text(self):
        source = r'''{
          // a comment
          "url": "https://example.com/a//b",
          "marker": "/* text */",
          /* another comment */
          "value": 1,
        }'''
        parsed = release_tools.load_json_relaxed(source, "test.json")
        self.assertEqual(parsed["url"], "https://example.com/a//b")
        self.assertEqual(parsed["marker"], "/* text */")
        self.assertEqual(parsed["value"], 1)

    def test_all_marker_selects_every_platform(self):
        platforms, packs = release_tools.parse_markers(
            "Update translations\n\nrelease all", {"1.20.1", "1.21.1"}
        )
        self.assertEqual(platforms, {"gh", "cf", "mr"})
        self.assertEqual(packs, set())

    def test_explicit_retry_marker_selects_pack(self):
        platforms, packs = release_tools.parse_markers(
            "release cf 1.21.1", {"1.20.1", "1.21.1"}
        )
        self.assertEqual(platforms, {"cf"})
        self.assertEqual(packs, {"1.21.1"})

    def test_marker_must_occupy_a_complete_line(self):
        parsed = release_tools.parse_markers(
            "Do not release all of the files", {"1.21.1"}
        )
        self.assertIsNone(parsed)

    def test_versions_are_semver(self):
        self.assertIsNotNone(release_tools.VERSION_RE.fullmatch("1.2.3"))
        self.assertIsNone(release_tools.VERSION_RE.fullmatch("1.2"))

    def test_semver_comparison(self):
        self.assertGreater(release_tools.compare_semver("1.2.0", "1.1.9"), 0)
        self.assertGreater(release_tools.compare_semver("1.2.0", "1.2.0-rc.1"), 0)
        self.assertLess(release_tools.compare_semver("1.2.0-rc.1", "1.2.0"), 0)
        self.assertEqual(release_tools.compare_semver("1.2.0+build.2", "1.2.0+build.1"), 0)

    def test_minecraft_versions_are_sorted_numerically(self):
        versions = ["1.9.4", "1.21.1", "1.20.1", "1.16.5"]
        versions.sort(key=release_tools.minecraft_version_key)
        self.assertEqual(versions, ["1.9.4", "1.16.5", "1.20.1", "1.21.1"])

    def test_plan_marks_highest_selected_minecraft_as_github_latest(self):
        config = {
            "project_name": "BMP",
            "curseforge_project_id": "cf",
            "modrinth_project_id": "mr",
            "packs": {
                "1.20.1": {"game_versions": ["1.20.1"]},
                "1.21.1": {"game_versions": ["1.21.1"]},
            },
        }
        with (
            mock.patch.object(release_tools, "load_config", return_value=config),
            mock.patch.object(release_tools, "normalize_before", return_value="before"),
            mock.patch.object(release_tools, "run_git", return_value="parent"),
            mock.patch.object(release_tools, "changed_version_packs", return_value=set()),
            mock.patch.object(release_tools, "validate_pack", return_value=[]),
            mock.patch.object(release_tools, "read_version", return_value="1.0.0"),
        ):
            plan = release_tools.create_plan(
                "before", "head", "release gh 1.20.1 1.21.1"
            )

        entries = json.loads(plan["matrix"])["include"]
        latest = [entry["minecraft"] for entry in entries if entry["github_latest"]]
        self.assertEqual(latest, ["1.21.1"])

    def test_changelog_is_english_then_russian(self):
        minecraft = "1.21.1"
        base_file = f"packs/{minecraft}/assets/ae2/lang/ru_ru.json"
        head_file = base_file
        temporary_root = SCRIPT.parents[1] / ".release"
        temporary_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as temporary:
            output = Path(temporary) / "CHANGELOG.md"
            with (
                mock.patch.object(release_tools, "load_config", return_value={"project_name": "BMP", "packs": {minecraft: {}}}),
                mock.patch.object(release_tools, "read_version", return_value="1.2.3"),
                mock.patch.object(release_tools, "changelog_base", return_value="base"),
                mock.patch.object(release_tools, "tree_files", side_effect=[{base_file}, {head_file}]),
                mock.patch.object(release_tools, "changed_paths", return_value={head_file}),
                mock.patch.object(release_tools, "load_mod_names", return_value={"ae2": "Applied Energistics 2"}),
                mock.patch.object(
                    release_tools,
                    "git_file",
                    side_effect=['{"old": "a"}', '{"old": "b", "new": "c"}'],
                ),
            ):
                release_tools.generate_changelog(minecraft, "head", output)
            changelog = output.read_text(encoding="utf-8")
            self.assertLess(changelog.index("## English"), changelog.index("## Русский"))
            self.assertIn("1 key added", changelog)
            self.assertIn("1 key updated", changelog)
            self.assertIn("добавлен 1 ключ", changelog)

    def test_generated_mod_catalog_maps_namespaces_to_full_names(self):
        minecraft = "1.21.1"
        catalog = {
            "minecraft": minecraft,
            "mods": [
                {
                    "name": "Applied Energistics 2",
                    "namespaces": ["ae2", "ae2guide"],
                    "resolved": True,
                }
            ],
        }
        with (
            mock.patch.object(release_tools, "pack_dir", return_value=SCRIPT.parents[1] / "virtual-pack"),
            mock.patch.object(Path, "exists", return_value=True),
            mock.patch.object(Path, "read_text", return_value=json.dumps(catalog)),
        ):
            names = release_tools.load_mod_names(minecraft)
        self.assertEqual(names["ae2"], "Applied Energistics 2")
        self.assertEqual(names["ae2guide"], "Applied Energistics 2")


if __name__ == "__main__":
    unittest.main()
