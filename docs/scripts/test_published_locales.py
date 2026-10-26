#!/usr/bin/env python3
"""Tests for published_locales.py, the one list of languages buildDocs.sh builds
and the navbar language switcher links to.

Run: python3 docs/scripts/test_published_locales.py
"""
from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from published_locales import published_locales  # noqa: E402

REPO_LOCALES = HERE.parent / "locales"


class PublishedLocalesTest(unittest.TestCase):

    def locales(self, published: str | None, dirs=("en", "es", "pt")) -> pathlib.Path:
        root = pathlib.Path(self.enterContext(tempfile.TemporaryDirectory()))
        for name in dirs:
            (root / name / "LC_MESSAGES").mkdir(parents=True)
        if published is not None:
            (root / "PUBLISHED").write_text(published)
        return root

    def test_english_first_then_listed_locales_only(self):
        root = self.locales("es partial\n")
        self.assertEqual(published_locales(root), [("en", False), ("es", True)])

    def test_locale_without_flag_is_complete(self):
        root = self.locales("es\n")
        self.assertEqual(published_locales(root), [("en", False), ("es", False)])

    def test_comments_and_blank_lines_are_ignored(self):
        root = self.locales("# Spanish is half done\n\n  es partial  # see ECO-204\n\n")
        self.assertEqual(published_locales(root), [("en", False), ("es", True)])

    def test_nothing_listed_builds_english_only(self):
        root = self.locales("# no translations ready yet\n")
        self.assertEqual(published_locales(root), [("en", False)])

    def test_listing_english_is_rejected(self):
        # English is always built; listing it is how `en` got built twice.
        root = self.locales("en\nes partial\n")
        with self.assertRaisesRegex(ValueError, "en"):
            published_locales(root)

    def test_locale_without_a_catalog_dir_is_rejected(self):
        root = self.locales("es\nfrr\n")
        with self.assertRaisesRegex(ValueError, "frr"):
            published_locales(root)

    def test_duplicate_locale_is_rejected(self):
        root = self.locales("es\nes partial\n")
        with self.assertRaisesRegex(ValueError, "es"):
            published_locales(root)

    def test_unknown_flag_is_rejected(self):
        root = self.locales("es partal\n")
        with self.assertRaisesRegex(ValueError, "partal"):
            published_locales(root)

    def test_missing_published_file_is_rejected(self):
        root = self.locales(None)
        with self.assertRaisesRegex(ValueError, "PUBLISHED"):
            published_locales(root)

    def test_cli_prints_the_build_list_for_buildDocs(self):
        root = self.locales("es partial\n")
        out = subprocess.run(
            [sys.executable, str(HERE / "published_locales.py"), str(root)],
            capture_output=True, text=True, check=True,
        ).stdout
        self.assertEqual(out, "en es\n")

    def test_cli_fails_on_a_bad_file(self):
        root = self.locales("pt\nfrr\n")
        result = subprocess.run(
            [sys.executable, str(HERE / "published_locales.py"), str(root)],
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("frr", result.stderr)

    def test_repo_published_file_is_valid(self):
        codes = [code for code, _ in published_locales(REPO_LOCALES)]
        self.assertEqual(codes.count("en"), 1)
        self.assertEqual(codes[0], "en")


if __name__ == "__main__":
    unittest.main(verbosity=2)
