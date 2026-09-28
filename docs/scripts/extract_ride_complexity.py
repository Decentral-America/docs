#!/usr/bin/env python3
"""Extract per-stdlib-version complexity changes for Ride built-ins.

Scans node-scala's `lang` module for the pattern
`NativeFunction("<name>", Map(V.. -> N, ...), ...)` — the direct case
where a Ride function's name is a string literal on the same call as
its complexity map — and prints every function whose complexity map
has an entry at V6 or later (i.e. something changed from the V5
baseline this reference documents elsewhere).

This does not attempt to resolve complexity maps passed indirectly
through a helper (e.g. `bigIntArithmeticOp(OP, NAME, Map(...))`) or
bound only via a `val` a few lines above the map — every row printed
here names a function taken verbatim from a NativeFunction call, never
inferred, so silence on a given function means "not found in the
direct pattern", not "unchanged".

Usage:
    python3 extract_ride_complexity.py <path-to-node-scala>/lang/shared/src/main/scala/com/decentralchain/lang/v1/evaluator/ctx/impl
"""
import re
import sys
from pathlib import Path

PAT = re.compile(r'NativeFunction\(\s*"([^"]+)"\s*,\s*Map\(([^)]*)\)')
VERPAIR = re.compile(r'(V\d)\s*->\s*(\d+)L')


def parse_file(path: Path):
    text = path.read_text(encoding="utf-8")
    out = []
    for m in PAT.finditer(text):
        name, mapbody = m.group(1), m.group(2)
        pairs = VERPAIR.findall(mapbody)
        if not pairs:
            continue
        versions = {v: int(c) for v, c in pairs}
        out.append((name, versions))
    return out


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    root = Path(sys.argv[1])
    rows = []
    for f in sorted(root.rglob("*.scala")):
        rows += parse_file(f)

    changed = [(n, v) for n, v in rows if any(k in v for k in ("V6", "V7", "V8", "V9"))]
    # De-duplicate rows that are byte-for-byte identical (the same
    # NativeFunction definition matched twice is not expected, but two
    # distinct overloads of the same name with the same cost curve are
    # collapsed to one row since they're indistinguishable from this
    # extraction alone).
    seen = set()
    unique = []
    for n, v in changed:
        key = (n, tuple(sorted(v.items())))
        if key not in seen:
            seen.add(key)
            unique.append((n, v))
    unique.sort(key=lambda r: r[0])

    print("| Function | Complexity by version |")
    print("|---|---|")
    for name, versions in unique:
        vs = ", ".join(f"{k}={v}" for k, v in sorted(versions.items()))
        print(f"| `{name}` | {vs} |")


if __name__ == "__main__":
    main()
