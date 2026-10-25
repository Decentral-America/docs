#!/usr/bin/env python3
"""Compile every Ride sample under docs/_samples/ride/ with a node's compiler.

Each `*.ride` file is sent to `POST /utils/script/compileCode` on the node given
by `--node` (default: the public Testnet node). The node compiles it with the
standard library version the file's `STDLIB_VERSION` directive names and
reports its complexity, so this catches syntax errors, type errors and scripts
that exceed a complexity limit. It does not deploy or broadcast anything.

Needs network access to the node, so it is not part of the PR checks in
docs_checks.yml (those reach nothing but npm). Run it locally after changing a
sample:

    python3 docs/scripts/check_ride_samples.py
    python3 docs/scripts/check_ride_samples.py --node http://127.0.0.1:6869

Exit status 0 when every sample compiles, 1 otherwise.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.error
import urllib.request

SAMPLES = pathlib.Path(__file__).resolve().parents[1] / "_samples" / "ride"
DEFAULT_NODE = "https://testnet-node.decentralchain.io"


def compile_code(node: str, source: str) -> dict:
    req = urllib.request.Request(
        f"{node.rstrip('/')}/utils/script/compileCode",
        data=source.encode("utf-8"),
        headers={"Content-Type": "text/plain", "Accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            return json.load(res)
    except urllib.error.HTTPError as err:
        # The node answers a compile error with HTTP 400 and {"error": ..., "message": ...}
        return json.load(err)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--node", default=DEFAULT_NODE, help=f"node REST API base URL (default: {DEFAULT_NODE})")
    args = parser.parse_args()

    files = sorted(SAMPLES.glob("*.ride"))
    if not files:
        print(f"FAIL no Ride samples found in {SAMPLES}")
        return 1
    failures = 0
    for path in files:
        rel = path.relative_to(SAMPLES.parents[1])
        result = compile_code(args.node, path.read_text(encoding="utf-8"))
        if "script" not in result:
            failures += 1
            print(f"FAIL {rel}: {result.get('message', result)}")
            continue
        details = f"complexity {result.get('complexity')}, verifier complexity {result.get('verifierComplexity')}"
        if result.get("callableComplexities"):
            details += f", callables {result['callableComplexities']}"
        print(f"ok   {rel}: {details}, extra fee {result.get('extraFee')}")
    print(f"{len(files)} Ride sample(s) compiled against {args.node}, {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
