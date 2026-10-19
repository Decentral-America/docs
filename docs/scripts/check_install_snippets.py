#!/usr/bin/env python3
"""Install and import every documented `npm install` snippet, exactly as written.

For each Markdown page under docs/ (locales, _build and _samples excluded):
  * every `npm install ...` line inside a ```bash / ```sh / ```shell fence is run
    verbatim in a fresh ESM project (package.json with "type": "module");
  * every `@decentralchain/*` package on that line must then load with a
    dynamic `import()` on the current Node.js;
  * every `import { a, b } from '@decentralchain/x'` / `import X from '...'`
    statement in a ts/typescript/js/javascript fence on the same page must name
    exports that the installed package really has.

A fence is skipped when the line directly above it is the MyST comment
`% snippet-check: skip` (used only for packages that are not published yet).

Exit status 0 when every snippet passes, 1 otherwise.
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import tempfile

DOCS = pathlib.Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {"locales", "_build", "_samples", "node_modules"}
FENCE_OPEN = re.compile(r"^```\s*(\{[^}]*\}|[A-Za-z]*)\s*$")
SKIP_MARKER = "% snippet-check: skip"
SHELL_LANGS = {"bash", "sh", "shell", "console"}
CODE_LANGS = {"ts", "typescript", "js", "javascript"}
IMPORT_RE = re.compile(
    r"^import\s+(?:(?P<default>[A-Za-z_$][\w$]*)\s*,?\s*)?(?:\{(?P<named>[^}]*)\})?\s*from\s*['\"](?P<pkg>@decentralchain/[^'\"]+)['\"]",
    re.MULTILINE,
)


def package_name(spec: str) -> str:
    """'@scope/name@1.2.3' -> '@scope/name'; '@scope/name' -> '@scope/name'."""
    if spec.startswith("@"):
        at = spec.find("@", 1)
        return spec if at == -1 else spec[:at]
    return spec.split("@", 1)[0]


def fences(text: str):
    """Yield (lang, body, skipped) for every fenced block in a Markdown page."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i])
        if not m:
            i += 1
            continue
        lang = m.group(1).lower()
        prev = next((l.strip() for l in reversed(lines[:i]) if l.strip()), "")
        skipped = prev == SKIP_MARKER
        j = i + 1
        while j < len(lines) and not lines[j].startswith("```"):
            j += 1
        yield lang, "\n".join(lines[i + 1 : j]), skipped
        i = j + 1


def run(cmd: list[str], cwd: pathlib.Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def exports_of(pkg: str, cwd: pathlib.Path) -> tuple[set[str] | None, str]:
    probe = (
        f"const m = await import({json.dumps(pkg)});"
        "console.log(JSON.stringify(Object.keys(m)));"
    )
    res = run(["node", "--input-type=module", "-e", probe], cwd)
    if res.returncode != 0:
        lines = res.stderr.strip().splitlines() or ["(no stderr)"]
        return None, next((l for l in lines if re.match(r"\s*\w*Error\b", l)), lines[-1])
    return set(json.loads(res.stdout.strip().splitlines()[-1])), ""


def main() -> int:
    failures: list[str] = []
    checked = 0
    with tempfile.TemporaryDirectory(prefix="docs-snippets-") as tmp:
        tmp_root = pathlib.Path(tmp)
        for page in sorted(DOCS.rglob("*.md")):
            if EXCLUDED_DIRS & set(page.relative_to(DOCS).parts):
                continue
            rel = page.relative_to(DOCS.parent)
            installed: dict[str, pathlib.Path] = {}
            code_blocks: list[str] = []
            for lang, body, skipped in fences(page.read_text(encoding="utf-8")):
                if skipped:
                    continue
                if lang in CODE_LANGS:
                    code_blocks.append(body)
                    continue
                if lang not in SHELL_LANGS:
                    continue
                for line in body.splitlines():
                    tokens = line.strip().split()
                    if tokens[:2] != ["npm", "install"]:
                        continue
                    checked += 1
                    work = tmp_root / f"s{checked}"
                    work.mkdir()
                    (work / "package.json").write_text('{"private": true, "type": "module"}\n')
                    res = run(tokens + ["--no-audit", "--no-fund"], work)
                    if res.returncode != 0:
                        failures.append(f"{rel}: `{line.strip()}` failed to install: {res.stderr.strip()[-300:]}")
                        continue
                    for spec in tokens[2:]:
                        if spec.startswith("-") or not spec.startswith("@decentralchain/"):
                            continue
                        name = package_name(spec)
                        keys, err = exports_of(name, work)
                        if keys is None:
                            failures.append(f"{rel}: `{line.strip()}` installs but `import('{name}')` fails: {err}")
                        else:
                            installed[name] = work
                            print(f"ok   {rel}: import('{name}') after `{line.strip()}`")
            for block in code_blocks:
                for m in IMPORT_RE.finditer(block):
                    pkg = m.group("pkg")
                    if pkg not in installed:
                        failures.append(f"{rel}: imports {pkg} but no passing `npm install` for it on this page")
                        continue
                    keys, err = exports_of(pkg, installed[pkg])
                    assert keys is not None, err
                    wanted = []
                    if m.group("default"):
                        wanted.append("default")
                    if m.group("named"):
                        wanted += [n.split(" as ")[0].strip() for n in m.group("named").split(",") if n.strip()]
                    missing = [w for w in wanted if w not in keys]
                    if missing:
                        failures.append(f"{rel}: `import ... from '{pkg}'` names missing exports {missing}")
                    else:
                        print(f"ok   {rel}: {pkg} exports {wanted}")
    if checked == 0:
        failures.append("no `npm install` snippets found -- the parser is broken")
    for f in failures:
        print(f"FAIL {f}")
    print(f"{checked} install snippet(s) checked, {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
