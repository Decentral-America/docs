#!/usr/bin/env python3
"""Fail if any built HTML page references a local file that is not in the build.

Usage: check_static_refs.py <html build dir>

Checks every relative `src=` / `href=` in every *.html file under the build
directory (external URLs, mailto:, javascript:, data: and pure #anchors are
skipped). This catches assets that an extension links into every page head but
never ships, such as the old thebelab-helper.js / thebelab.css 404s.
"""
from __future__ import annotations

import pathlib
import re
import sys
from urllib.parse import unquote, urlsplit

ATTR = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""")
SKIP_PREFIXES = ("http://", "https://", "//", "mailto:", "javascript:", "data:", "#", "tel:")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    root = pathlib.Path(sys.argv[1]).resolve()
    missing: set[tuple[str, str]] = set()
    # _static/ holds theme template fragments (e.g. webpack-macros.html), not pages.
    pages = sorted(p for p in root.rglob("*.html") if "_static" not in p.relative_to(root).parts)
    for page in pages:
        for ref in ATTR.findall(page.read_text(encoding="utf-8", errors="replace")):
            if ref.startswith(SKIP_PREFIXES):
                continue
            path = unquote(urlsplit(ref).path)
            if not path:
                continue
            target = (root / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
            target = target.resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                missing.add((str(page.relative_to(root)), ref))
    for page, ref in sorted(missing):
        print(f"FAIL {page}: {ref} not found in the build")
    print(f"{len(pages)} page(s) checked, {len(missing)} missing local reference(s)")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
