#!/usr/bin/env python3
"""Check the TypeScript package table in 04_building-apps/02_client-libraries-and-sdk.md.

Default mode: every row whose **Install** cell is a version is installed as
`@decentralchain/<package>@<version>` in a fresh ESM project and must load with
`import()` on the current Node.js.

`--drift`: additionally compare the `latest` / `next` cells (the leading
version number in each cell) with `npm view @decentralchain/<package> dist-tags`
and fail on any difference, so a publish or dist-tag change forces a docs update.

Exit status 0 when every check passes, 1 otherwise.
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import tempfile

PAGE = pathlib.Path(__file__).resolve().parents[1] / "04_building-apps" / "02_client-libraries-and-sdk.md"
VERSION = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.]+)?")
ROW = re.compile(r"^\|\s*`(?P<pkg>[a-z0-9-]+)`\s*\|(?P<cells>.*)\|\s*$")


def rows(text: str):
    """Yield (package, install, latest, next) from the 5-column TypeScript table."""
    in_table = False
    for line in text.splitlines():
        if line.startswith("| npm package | Install | `latest` | `next` |"):
            in_table = True
            continue
        if in_table and not line.startswith("|"):
            return
        m = ROW.match(line) if in_table else None
        if m:
            cells = [c.strip() for c in m.group("cells").split("|")]
            yield m.group("pkg"), cells[0], cells[1], cells[2]


def leading_version(cell: str) -> str | None:
    m = VERSION.match(cell)
    return m.group(0) if m else None


def main() -> int:
    drift = "--drift" in sys.argv[1:]
    failures: list[str] = []
    table = list(rows(PAGE.read_text(encoding="utf-8")))
    if len(table) < 10:
        failures.append(f"parsed only {len(table)} table rows -- the parser or the table header changed")
    with tempfile.TemporaryDirectory(prefix="docs-sdk-table-") as tmp:
        for pkg, install, latest, nxt in table:
            name = f"@decentralchain/{pkg}"
            version = leading_version(install)
            if version:
                work = pathlib.Path(tmp) / pkg
                work.mkdir()
                (work / "package.json").write_text('{"private": true, "type": "module"}\n')
                res = subprocess.run(["npm", "install", f"{name}@{version}", "--no-audit", "--no-fund"],
                                     cwd=work, capture_output=True, text=True)
                if res.returncode != 0:
                    failures.append(f"{name}@{version}: npm install failed: {res.stderr.strip()[-200:]}")
                else:
                    res = subprocess.run(["node", "--input-type=module", "-e", f"await import({json.dumps(name)})"],
                                         cwd=work, capture_output=True, text=True)
                    if res.returncode != 0:
                        err = next((l for l in res.stderr.splitlines() if re.match(r"\s*\w*Error\b", l)), res.stderr[-200:])
                        failures.append(f"{name}@{version}: import failed: {err}")
                    else:
                        print(f"ok   {name}@{version} installs and imports")
            if drift:
                res = subprocess.run(["npm", "view", name, "dist-tags", "--json"], capture_output=True, text=True)
                tags = json.loads(res.stdout) if res.returncode == 0 and res.stdout.strip() else {}
                for tag, cell in (("latest", latest), ("next", nxt)):
                    documented = leading_version(cell)
                    actual = tags.get(tag)
                    if documented != actual:
                        failures.append(f"{name}: table says {tag}={documented}, npm says {tag}={actual}")
    for f in failures:
        print(f"FAIL {f}")
    print(f"{len(table)} table row(s) checked, {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
