import importlib.util
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


if __name__ == "__main__":
    unittest.main()
