import tempfile
import unittest
from pathlib import Path

from check_links import find_broken_links


class CheckLinksTests(unittest.TestCase):
    def test_finds_missing_local_markdown_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            content_dir = root / "content"
            content_dir.mkdir()
            page = content_dir / "guide.md"
            page.write_text("See [missing](./missing.md).", encoding="utf-8")

            broken_links = find_broken_links([page])

            self.assertEqual(len(broken_links), 1)
            self.assertEqual(broken_links[0][0], page)
            self.assertEqual(broken_links[0][1], "./missing.md")

    def test_ignores_external_and_pelican_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            content_dir = root / "content"
            content_dir.mkdir()
            page = content_dir / "guide.md"
            page.write_text(
                "See [Docs](https://example.com), [Local]({filename}/general/outline.md), and [Anchor](#section).",
                encoding="utf-8",
            )

            broken_links = find_broken_links([page])

            self.assertEqual(broken_links, [])


if __name__ == "__main__":
    unittest.main()
