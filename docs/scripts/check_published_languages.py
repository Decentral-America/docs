#!/usr/bin/env python3
"""Check one built language of the site against docs/locales/PUBLISHED.

On every page of <html_dir> (the build of <language>):
- the navbar language switcher lists exactly the published languages, English
  first, a `partial` one labelled `<code> (partial)`, each linking to
  /<code>/<version>/ for one shared version, with <language> selected;
- the partial-translation banner is present if <language> is `partial`, and
  absent otherwise.

Usage: check_published_languages.py <html_dir> <language>
Exit status 0 when every check passes, 1 otherwise.
"""
from __future__ import annotations

import html.parser
import pathlib
import re
import sys

from published_locales import published_locales

LOCALES = pathlib.Path(__file__).resolve().parents[1] / "locales"
BANNER_CLASS = "partial-translation-notice"
URL = re.compile(r"^/(?P<lang>[^/]+)/(?P<version>.+)/$")


class Page(html.parser.HTMLParser):
    """Collect each language switcher's options and whether the banner is present.

    The theme renders the switcher twice per page (navbar and mobile sidebar).
    """

    def __init__(self):
        super().__init__()
        self.switchers: list[list[tuple[str, str, bool]]] = []  # [(url, label, selected)] per <select>
        self.banner = False
        self._in_selector = False
        self._option: list | None = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if BANNER_CLASS in (attrs.get("class") or "").split():
            self.banner = True
        if tag == "select" and attrs.get("id") == "language-selector":
            self._in_selector = True
            self.switchers.append([])
        elif tag == "option" and self._in_selector:
            self._option = [attrs.get("value", ""), "", "selected" in attrs]

    def handle_data(self, data):
        if self._option is not None:
            self._option[1] += data

    def handle_endtag(self, tag):
        if tag == "option" and self._option is not None:
            url, label, selected = self._option
            self.switchers[-1].append((url, label.strip(), selected))
            self._option = None
        elif tag == "select":
            self._in_selector = False


def problems(page: Page, language: str, published: list[tuple[str, bool]]) -> list[str]:
    found = []
    want = [(code, f"{code} (partial)" if partial else code) for code, partial in published]
    want_selected = [label for code, label in want if code == language]
    for options in page.switchers:
        got = []
        versions = set()
        for url, label, _ in options:
            m = URL.match(url)
            got.append((m["lang"] if m else url, label))
            versions.add(m["version"] if m else None)
        if got != want:
            found.append(f"switcher lists {got}, want {want}")
        if len(versions) > 1 or None in versions:
            found.append(f"switcher links to more than one version or a malformed URL: {[u for u, _, _ in options]}")
        selected = [label for _, label, sel in options if sel]
        if selected != want_selected:
            found.append(f"switcher selects {selected}, want {want_selected}")
    partial = dict(published).get(language, False)
    if page.banner != partial:
        found.append("partial-translation banner " + ("missing" if partial else "shown on a complete language"))
    return found


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(f"usage: {argv[0]} <html_dir> <language>", file=sys.stderr)
        return 2
    html_dir, language = pathlib.Path(argv[1]), argv[2]
    published = published_locales(LOCALES)
    if language not in dict(published):
        print(f"FAIL: '{language}' is not a published language ({' '.join(dict(published))})")
        return 1

    checked, failed = 0, 0
    for path in sorted(html_dir.rglob("*.html")):
        page = Page()
        page.feed(path.read_text(errors="replace"))
        if not page.switchers:
            continue  # not a themed page (e.g. a raw HTML asset)
        checked += 1
        for problem in problems(page, language, published):
            failed += 1
            if failed <= 20:
                print(f"FAIL: {path.relative_to(html_dir)}: {problem}")
    if checked == 0:
        print(f"FAIL: no page in {html_dir} has a language switcher")
        return 1
    if failed:
        print(f"{failed} problem(s) on {checked} page(s)")
        return 1
    print(f"PASS: {checked} '{language}' page(s) match docs/locales/PUBLISHED")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
