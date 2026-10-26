#!/usr/bin/env python3
"""The languages the site publishes: English, then each locale in locales/PUBLISHED.

buildDocs.sh builds exactly this list and conf.py fills the navbar language
switcher from it, so the site never links to a language it did not build.
A catalog dir under locales/ that PUBLISHED does not list is neither built nor
linked: sphinx-intl creates catalogs for every language, translated or not.

PUBLISHED format, one locale per line, `#` starts a comment:

    es partial

`partial` marks an incomplete translation: its switcher entry and a banner on
every page say so. English is always built and must not be listed.

Usage: published_locales.py <locales_dir>  prints the build list, e.g. `en es`.
"""
from __future__ import annotations

import pathlib
import sys

FLAGS = {"partial"}


def published_locales(locales_dir) -> list[tuple[str, bool]]:
    """Return [(code, partial), ...], English first. Raise ValueError on a bad PUBLISHED file."""
    locales_dir = pathlib.Path(locales_dir)
    path = locales_dir / "PUBLISHED"
    if not path.is_file():
        raise ValueError(f"{path} not found: list the translated locales to publish there")

    langs = [("en", False)]
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        words = line.split("#", 1)[0].split()
        if not words:
            continue
        code, flags = words[0], words[1:]
        where = f"{path}:{lineno}"
        if code == "en":
            raise ValueError(f"{where}: 'en' is always built, remove it")
        if not (locales_dir / code).is_dir():
            raise ValueError(f"{where}: no catalog dir for locale '{code}' under {locales_dir}")
        if code in (c for c, _ in langs):
            raise ValueError(f"{where}: locale '{code}' listed twice")
        unknown = set(flags) - FLAGS
        if unknown:
            raise ValueError(f"{where}: unknown flag(s) {', '.join(sorted(unknown))} (allowed: {', '.join(sorted(FLAGS))})")
        langs.append((code, "partial" in flags))
    return langs


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} <locales_dir>", file=sys.stderr)
        return 2
    try:
        langs = published_locales(argv[1])
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    print(" ".join(code for code, _ in langs))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
