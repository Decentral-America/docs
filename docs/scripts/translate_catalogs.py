#!/usr/bin/env python3
"""Move messages between the .po catalogs and a translator (a machine translation
engine or a person) as JSON lines, and check each translation before it lands.

  translate_catalogs.py export <locales_dir> <locale> <out.jsonl> [catalog ...]
      Write every message of <locale> that has no translation, or only a fuzzy
      one, as {"catalog": ..., "id": <English>} lines. Limit it to some
      catalogs (by name, e.g. 09_user-guides) to translate a section at a time.

  translate_catalogs.py import <locales_dir> <locale> <in.jsonl>
      Read {"catalog": ..., "id": <English>, "str": <translation>} lines and put
      each translation into its catalog, as a finished (not fuzzy) message. A
      translation is rejected, and written to <in>.rejected.jsonl with the
      reason, when it:
        - changes the markup (translations.markup_problem: roles, :ref:/{ref}
          targets, code literals, link URLs, backticks);
        - drops a name the glossary says is never translated (DecentralChain,
          DCC, Ride, Cubensis Connect, ...), when the English has it, or
          names a third-party project (translations.term_problem);
        - changes the {placeholders} of the message;
        - changes the % directives of a message msgfmt checks as a Python
          format string (its English has a `%`, as in "100% of blocks").

A translated locale still needs a review by a native or fluent speaker before
it is listed in docs/locales/PUBLISHED (see AGENTS.md); importing a
translation only makes it count towards the locale's coverage. Use the
fixed terms in docs/locales/glossary.csv. Afterwards run
`translations.py check` and `sphinx-build -W -D language=<locale>`.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

from babel.messages.catalog import PYTHON_FORMAT
from babel.messages.pofile import read_po, write_po

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from translations import kept_names, markup_problem, term_problem  # noqa: E402

PLACEHOLDER = re.compile(r"\{[^{}\s]*\}")
# Messages that must stay in English. The home page's sphinx-design `button-ref` labels carry
# their reference inside the label, so a translated label drops it and the -W build fails
# with "inconsistent term references".
KEEP_ENGLISH = {"Learn More"}


def catalog_paths(locales_dir: pathlib.Path, locale: str) -> dict[str, pathlib.Path]:
    return {p.stem: p for p in sorted((locales_dir / locale / "LC_MESSAGES").glob("*.po"))}


def export(locales_dir: pathlib.Path, locale: str, out: pathlib.Path, only: list[str]) -> int:
    count = 0
    with out.open("w", encoding="utf-8") as f:
        for name, path in catalog_paths(locales_dir, locale).items():
            if only and name not in only:
                continue
            with path.open("rb") as po:
                catalog = read_po(po)
            for message in catalog:
                if not message.id or isinstance(message.id, tuple):
                    continue
                if (message.string and not message.fuzzy) or message.id in KEEP_ENGLISH:
                    continue
                f.write(json.dumps({"catalog": name, "id": message.id}, ensure_ascii=False) + "\n")
                count += 1
    print(f"exported {count} message(s) to {out}")
    return 0


def problem(msgid: str, msgstr: str, names: list[str]) -> str | None:
    if not msgstr.strip():
        return "empty translation"
    if msgid in KEEP_ENGLISH:
        return "this message stays in English (see KEEP_ENGLISH)"
    found = markup_problem(msgid, msgstr) or term_problem(msgid, msgstr, names)
    if found:
        return found
    if sorted(PLACEHOLDER.findall(msgid)) != sorted(PLACEHOLDER.findall(msgstr)):
        return f"placeholders differ: {PLACEHOLDER.findall(msgid)} vs {PLACEHOLDER.findall(msgstr)}"
    return None


def format_problem(msgid: str, msgstr: str) -> str | None:
    """A message whose English has a `%` (100% of blocks) is a Python format string to
    msgfmt: `msgfmt --check` fails unless the translation keeps the same directives."""
    def directives(text: str) -> list[str]:
        return sorted(m.group(0) for m in PYTHON_FORMAT.finditer(text.replace("%%", "")))

    if directives(msgid) != directives(msgstr) or msgstr.replace("%%", "").count("%") != len(directives(msgstr)):
        return f"changes the % directives msgfmt checks: {directives(msgid)} vs {directives(msgstr)}"
    return None


def import_(locales_dir: pathlib.Path, locale: str, source: pathlib.Path) -> int:
    names = kept_names(locales_dir)
    paths = catalog_paths(locales_dir, locale)
    wanted: dict[str, dict[str, str]] = {}
    rejected = []
    for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        entry = json.loads(line)
        if entry.get("catalog") not in paths:
            rejected.append({**entry, "reason": f"line {number}: no catalog {entry.get('catalog')!r}"})
            continue
        reason = problem(entry["id"], entry.get("str", ""), names)
        if reason:
            rejected.append({**entry, "reason": reason})
            continue
        wanted.setdefault(entry["catalog"], {})[entry["id"]] = entry["str"]
    applied = 0
    for name, translations in wanted.items():
        with paths[name].open("rb") as po:
            catalog = read_po(po)
        for message in catalog:
            if message.id in translations:
                msgstr = translations.pop(message.id)
                reason = format_problem(message.id, msgstr) if message.python_format else None
                if reason:
                    rejected.append({"catalog": name, "id": message.id, "str": msgstr, "reason": reason})
                    continue
                message.string = msgstr
                message.flags.discard("fuzzy")
                applied += 1
        for msgid, msgstr in translations.items():
            rejected.append({"catalog": name, "id": msgid, "str": msgstr, "reason": "no such message in the catalog"})
        with paths[name].open("wb") as po:
            write_po(po, catalog, width=-1, include_previous=True)
    if rejected:
        out = source.with_suffix(".rejected.jsonl")
        out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rejected), encoding="utf-8")
        print(f"rejected {len(rejected)} translation(s), with reasons, in {out}")
    print(f"imported {applied} translation(s) into {locale}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 5 or argv[1] not in {"export", "import"}:
        print(__doc__, file=sys.stderr)
        return 2
    locales_dir, locale, path = pathlib.Path(argv[2]), argv[3], pathlib.Path(argv[4])
    if argv[1] == "export":
        return export(locales_dir, locale, path, argv[5:])
    return import_(locales_dir, locale, path)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
