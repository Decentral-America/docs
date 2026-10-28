#!/usr/bin/env python3
"""Fail if a published docs page is a stub: shorter than MIN_LINES lines.

Usage: check_page_length.py

Counts the lines of every .md and .rst page under docs/, except section index
pages (index.md / index.rst), translations (locales/) and anything Sphinx does
not publish (folders and files whose name starts with "_", such as _samples/
and _terminology.md). A page under MIN_LINES lines fails unless it is listed in
short_pages_allowlist.txt next to this script, one path per line relative to
docs/, each with a "# reason". An allowlisted page that has grown past the
minimum, or no longer exists, is reported so the entry can be removed; the
second one fails, because the allowlist must not name pages that are gone.
"""
from __future__ import annotations

import pathlib
import sys

MIN_LINES = 60
DOCS = pathlib.Path(__file__).resolve().parents[1]
ALLOWLIST = pathlib.Path(__file__).with_name("short_pages_allowlist.txt")


def published_pages() -> list[pathlib.Path]:
    pages = []
    for path in sorted(DOCS.rglob("*")):
        rel = path.relative_to(DOCS)
        if path.suffix not in (".md", ".rst") or path.stem == "index":
            continue
        if rel.parts[0] == "locales" or any(part.startswith(("_", ".")) for part in rel.parts):
            continue
        pages.append(path)
    return pages


def read_allowlist() -> dict[str, str]:
    entries = {}
    for number, raw in enumerate(ALLOWLIST.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        path, _, reason = line.partition("#")
        if not reason.strip():
            print(f"FAIL {ALLOWLIST.name}:{number}: {path.strip()} has no '# reason'")
            entries[path.strip()] = ""
            continue
        entries[path.strip()] = reason.strip()
    return entries


def main() -> int:
    allowlist = read_allowlist()
    failures = sum(1 for reason in allowlist.values() if not reason)
    pages = published_pages()
    for page in pages:
        rel = page.relative_to(DOCS).as_posix()
        lines = len(page.read_text(encoding="utf-8").splitlines())
        if lines >= MIN_LINES:
            if rel in allowlist:
                print(f"note {rel}: {lines} lines, no longer short; remove it from {ALLOWLIST.name}")
            continue
        if rel not in allowlist:
            print(f"FAIL {rel}: {lines} lines, under {MIN_LINES}; expand it or add it to {ALLOWLIST.name} with a reason")
            failures += 1
    known = {page.relative_to(DOCS).as_posix() for page in pages}
    for rel in sorted(set(allowlist) - known):
        print(f"FAIL {ALLOWLIST.name}: {rel} is not a published page")
        failures += 1
    print(f"{len(pages)} page(s) checked, {len(allowlist)} allowlisted, {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
