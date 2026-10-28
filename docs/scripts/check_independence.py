#!/usr/bin/env python3
"""Fail if the docs name a third-party project (PLAN-docs-expansion.md §7).

Usage: check_independence.py

Searches every text file under docs/ (pages, tables, samples, scripts, static
assets; not the translation catalogs, build output or node_modules) for the
forbidden terms, case-insensitively. It also decodes every `base64:` literal
and every base64 run of 16 or more characters inside one, so a term can't
hide in an example value or a compiled script.

A legitimate mention (for example an attribution a license requires) goes in
independence_allowlist.txt next to this script: one `<path>: <exact line>`
per entry, relative to docs/, followed by `  # <reason>`. Each entry must
have a reason, and an entry that no longer matches a line fails, so the
allowlist can't go stale.
"""
from __future__ import annotations

import base64
import binascii
import pathlib
import re
import sys

DOCS = pathlib.Path(__file__).resolve().parents[1]
ALLOWLIST = pathlib.Path(__file__).with_name("independence_allowlist.txt")
FORBIDDEN = re.compile(r"waves|wavelet|@waves/|keeper wallet|wavesplatform", re.IGNORECASE)
EXTENSIONS = {
    ".md", ".rst", ".py", ".svg", ".ts", ".js", ".mjs", ".html", ".css",
    ".java", ".ride", ".csv", ".json", ".yaml", ".yml", ".txt", ".sh", ".conf",
}
SKIP_DIRS = {"locales", "_build", "node_modules", ".run", "target"}
BASE64_LITERAL = re.compile(r"base64:([A-Za-z0-9+/=]{4,})")


def text_files() -> list[pathlib.Path]:
    return sorted(
        p for p in DOCS.rglob("*")
        if p.is_file() and p.suffix in EXTENSIONS and not SKIP_DIRS & set(p.relative_to(DOCS).parts)
        and p != ALLOWLIST
    )


def decoded_hits(line: str) -> list[str]:
    hits = []
    for literal in BASE64_LITERAL.findall(line):
        try:
            data = base64.b64decode(literal + "=" * (-len(literal) % 4))
        except (binascii.Error, ValueError):
            continue
        text = data.decode("latin-1")
        hits += sorted({m.group(0) for m in FORBIDDEN.finditer(text)})
    return hits


def read_allowlist() -> tuple[dict[tuple[str, str], str], int]:
    entries, failures = {}, 0
    for number, raw in enumerate(ALLOWLIST.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        entry, sep, reason = raw.partition("  # ")
        path, colon, line = entry.partition(": ")
        if not sep or not reason.strip() or not colon:
            print(f"FAIL {ALLOWLIST.name}:{number}: expected `<path>: <exact line>  # <reason>`")
            failures += 1
            continue
        entries[(path.strip(), line.strip())] = reason.strip()
    return entries, failures


def main() -> int:
    allowlist, failures = read_allowlist()
    used = set()
    files = text_files()
    for path in files:
        rel = path.relative_to(DOCS).as_posix()
        for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            plain = sorted({m.group(0) for m in FORBIDDEN.finditer(line)})
            hidden = decoded_hits(line)
            if not plain and not hidden:
                continue
            key = (rel, line.strip())
            if key in allowlist:
                used.add(key)
                continue
            failures += 1
            what = ", ".join(plain + [f"{h} (base64-encoded)" for h in hidden])
            print(f"FAIL {rel}:{number}: {what}")
    for path, line in sorted(set(allowlist) - used):
        print(f"FAIL {ALLOWLIST.name}: no line in {path} matches `{line}`; remove the entry")
        failures += 1
    print(f"{len(files)} file(s) checked, {len(allowlist)} allowlisted line(s), {failures} failure(s)")
    if failures:
        print("::error::Forbidden third-party reference found (see docs/_terminology.md)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
