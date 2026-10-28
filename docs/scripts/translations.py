#!/usr/bin/env python3
"""Translation catalog tooling: headers, checks, coverage and the publish rule.

Usage, from the repository root:

  translations.py headers  <locales_dir>
      Give every catalog a complete header: Language, Language-Team, the
      locale's Plural-Forms and a UTF-8 charset. Run by update_translations.sh
      after sphinx-intl, so new and old catalogs alike pass `msgfmt --check`.

  translations.py check    <locales_dir> <gettext_dir>
      Fail unless every target locale has a catalog for every section (one
      .pot in <gettext_dir>, from `sphinx-build -b gettext`), every .po
      under <locales_dir> passes `msgfmt --check`, and every translated
      message keeps its English markup: the same roles (`:math:`, `:ref:`...)
      in the same order, the same :ref:/:doc: targets, no space just inside
      a role's backticks. A translation that breaks markup fails the
      `sphinx-build -W` deploy build; mark it fuzzy or fix it.

  translations.py coverage <locales_dir> [--markdown]
      Print the share of messages translated (not fuzzy, not obsolete) per
      target locale. --markdown prints a table for a CI job summary.

  translations.py publish  <locales_dir>
      Apply the publish rule to docs/locales/PUBLISHED: a listed locale must
      be at least PUBLISH_THRESHOLD translated, or be marked `partial`.
      Locales over the threshold that aren't listed are reported: they can be
      published once a reviewer signs them off (ECO-400).

Target locales are the catalog dirs under <locales_dir> except `en`, the
source language. Coverage is only accurate on catalogs that sphinx-intl has
updated against the current English source, so CI runs `coverage` and
`publish` on a freshly updated copy of the catalogs.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

from babel import Locale
from babel.messages.pofile import read_po, write_po

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from published_locales import published_locales  # noqa: E402

PUBLISH_THRESHOLD = 80.0
SOURCE_LOCALE = "en"

ROLE = re.compile(r":([A-Za-z][\w.+-]*):`((?:[^`\\]|\\.)*)`")
REF_TARGET = re.compile(r"<([^<>]+)>\s*$")
LINK_ROLES = {"ref", "doc", "term", "numref"}


def markup(text: str) -> list[tuple[str, str | None]]:
    """The roles in a message, in order: (name, target) for links, (name, None) otherwise."""
    out = []
    for m in ROLE.finditer(text):
        name, body = m.group(1), m.group(2)
        if name in LINK_ROLES:
            target = REF_TARGET.search(body)
            out.append((name, target.group(1) if target else body))
        else:
            out.append((name, None))
    return out


def markup_problem(msgid: str, msgstr: str) -> str | None:
    if markup(msgid) != markup(msgstr):
        return f"roles or link targets differ from the English: {markup(msgid)} vs {markup(msgstr)}"
    for m in ROLE.finditer(msgstr):
        if m.group(2) != m.group(2).strip():
            return f"space just inside the backticks of :{m.group(1)}:`{m.group(2)}`"
    if msgid.count("`") % 2 == 0 and msgstr.count("`") % 2:
        return "unbalanced backticks"
    return None


def locale_dirs(locales_dir: pathlib.Path, include_source: bool = False) -> list[pathlib.Path]:
    return sorted(
        d for d in locales_dir.iterdir()
        if d.is_dir() and (d / "LC_MESSAGES").is_dir() and (include_source or d.name != SOURCE_LOCALE)
    )


def catalogs(locale_dir: pathlib.Path) -> list[pathlib.Path]:
    return sorted((locale_dir / "LC_MESSAGES").glob("*.po"))


def fix_headers(locales_dir: pathlib.Path) -> int:
    changed = 0
    for locale_dir in locale_dirs(locales_dir, include_source=True):
        code = locale_dir.name
        locale = Locale.parse(code)
        for path in catalogs(locale_dir):
            with path.open("rb") as f:
                catalog = read_po(f, locale=code)
            before = path.read_bytes()
            catalog.locale = locale  # also sets Plural-Forms from CLDR
            catalog.language_team = f"{locale.english_name} <https://github.com/Decentral-America/docs>"
            catalog.project = "DecentralChain docs"
            catalog.msgid_bugs_address = "https://github.com/Decentral-America/docs/issues"
            catalog.charset = "utf-8"
            with path.open("wb") as f:
                # width=-1 keeps lines unwrapped, as `sphinx-intl update -w -1` writes them
                write_po(f, catalog, width=-1, include_previous=True)
            if path.read_bytes() != before:
                changed += 1
    print(f"headers: {changed} catalog(s) updated")
    return 0


def check(locales_dir: pathlib.Path, gettext_dir: pathlib.Path) -> int:
    failures = 0
    sections = sorted(p.stem for p in gettext_dir.glob("*.pot"))
    if not sections:
        print(f"FAIL no .pot files in {gettext_dir}: run `sphinx-build -b gettext` first")
        return 1
    for locale_dir in locale_dirs(locales_dir):
        have = {p.stem for p in catalogs(locale_dir)}
        missing = [s for s in sections if s not in have]
        if missing:
            failures += 1
            print(f"FAIL {locale_dir.name}: no catalog for {', '.join(missing)}; run docs/scripts/update_translations.sh")
    checked = 0
    for locale_dir in locale_dirs(locales_dir, include_source=True):
        for path in catalogs(locale_dir):
            checked += 1
            result = subprocess.run(["msgfmt", "--check", "-o", "/dev/null", str(path)], capture_output=True, text=True)
            if result.returncode != 0:
                failures += 1
                errors = [line for line in result.stderr.splitlines() if "warning: header field" not in line]
                print(f"FAIL {path}: msgfmt --check\n  " + "\n  ".join(errors[-5:]))
            with path.open("rb") as f:
                catalog = read_po(f)
            for message in catalog:
                if not message.id or not message.string or message.fuzzy or isinstance(message.id, tuple):
                    continue
                problem = markup_problem(message.id, message.string)
                if problem:
                    failures += 1
                    where = ", ".join(f"{file}:{line}" for file, line in message.locations[:1])
                    print(f"FAIL {path} ({where}): {problem}")
    print(f"{len(sections)} section(s), {len(locale_dirs(locales_dir))} target locale(s), {checked} catalog(s) checked, {failures} failure(s)")
    return 1 if failures else 0


def coverage_of(locale_dir: pathlib.Path) -> tuple[int, int]:
    translated = total = 0
    for path in catalogs(locale_dir):
        with path.open("rb") as f:
            catalog = read_po(f)
        for message in catalog:
            if not message.id:  # the header
                continue
            total += 1
            if message.string and not message.fuzzy and (
                all(message.string) if isinstance(message.string, tuple) else True
            ):
                translated += 1
    return translated, total


def coverage(locales_dir: pathlib.Path, markdown: bool, quiet: bool = False) -> dict[str, float]:
    published = {code: partial for code, partial in published_locales(locales_dir)}
    result = {}
    rows = []
    for locale_dir in locale_dirs(locales_dir):
        translated, total = coverage_of(locale_dir)
        percent = 100.0 * translated / total if total else 0.0
        result[locale_dir.name] = percent
        if locale_dir.name in published:
            status = "published, partial" if published[locale_dir.name] else "published"
        else:
            status = "not published"
        rows.append((locale_dir.name, translated, total, percent, status))
    if quiet:
        return result
    if markdown:
        print("| Locale | Translated | Messages | Coverage | Status |")
        print("|---|---:|---:|---:|---|")
        for code, translated, total, percent, status in rows:
            print(f"| `{code}` | {translated} | {total} | {percent:.1f}% | {status} |")
        print(f"\nA locale is published when it is listed in `docs/locales/PUBLISHED` and is at least {PUBLISH_THRESHOLD:.0f}% translated, or is marked `partial` there.")
    else:
        for code, translated, total, percent, status in rows:
            print(f"{code:4} {percent:5.1f}%  {translated:5}/{total:<5}  {status}")
    return result


def publish(locales_dir: pathlib.Path) -> int:
    percents = coverage(locales_dir, markdown=False, quiet=True)
    failures = 0
    listed = set()
    for code, partial in published_locales(locales_dir)[1:]:
        listed.add(code)
        percent = percents.get(code, 0.0)
        if not partial and percent < PUBLISH_THRESHOLD:
            failures += 1
            print(f"FAIL {code} is listed in PUBLISHED without `partial` but is only {percent:.1f}% translated (needs {PUBLISH_THRESHOLD:.0f}%)")
    for code, percent in percents.items():
        if code not in listed and percent >= PUBLISH_THRESHOLD:
            print(f"note {code} is {percent:.1f}% translated: list it in PUBLISHED once a reviewer has signed it off")
    print(f"publish rule: {len(listed)} listed locale(s), {failures} failure(s)")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if len(argv) < 3 or argv[1] not in {"headers", "check", "coverage", "publish"}:
        print(__doc__, file=sys.stderr)
        return 2
    command, locales_dir = argv[1], pathlib.Path(argv[2])
    if command == "headers":
        return fix_headers(locales_dir)
    if command == "check":
        if len(argv) < 4:
            print(__doc__, file=sys.stderr)
            return 2
        return check(locales_dir, pathlib.Path(argv[3]))
    if command == "coverage":
        coverage(locales_dir, markdown="--markdown" in argv)
        return 0
    return publish(locales_dir)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
