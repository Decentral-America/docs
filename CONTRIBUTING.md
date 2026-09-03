# Contributing to DecentralChain Docs

Thanks for helping improve the docs. This file covers how to get set up and submit a change. For the deeper technical reference (build pipeline, content conventions, gotchas), see [AGENTS.md](AGENTS.md) — worth a skim before any non-trivial change.

## Quick start

```bash
git clone https://github.com/Decentral-America/docs.git
cd docs
python3 -m venv .venv && source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs/ /tmp/out
python3 -m http.server 8000 --directory /tmp/out
```

Open `http://localhost:8000` and check your change rendered correctly.

## Making a change

1. Branch off `dev` (not `main` — `dev` is the integration branch; `main` is what deploys live)
2. Edit the relevant `.rst` or `.md` file under `docs/`
3. Build locally with `sphinx-build -W -b html docs/ /tmp/out` — the `-W` flag turns warnings into errors, matching what CI enforces. Fix anything it flags before opening a PR.
4. Open a pull request against `dev`

Every PR runs two automated checks: a strict build (blocks merge on warnings — broken cross-references, bad directives) and a link check (informational only, won't block merge, but worth a look).

## Style notes

- Prefer `:ref:` / MyST cross-reference syntax over hardcoded links when pointing at another page in this site — it gets validated at build time, a raw link doesn't.
- For tables with links, math, or multi-part explanations inside cells, use a `.. csv-table::` sourcing a `.csv` file (see existing examples under `docs/_static/**/tables/`) rather than a plain Markdown table — Markdown tables can't hold that kind of content cleanly.
- Keep line-by-line diffs focused; this repo builds in 2 branches × 11 languages, so a change to shared structure (headings, `conf.py`, templates) has a wide blast radius — double-check before renaming a heading that other pages `:ref:` into.

## Translations

Translation contributions go through [GitLocalize](https://gitlocalize.com/repo/8397), not directly as PRs editing `.po` files by hand. See the badges on this repo's README for current coverage per language.

## Reporting issues

If the bug is in the docs content itself, open an issue here. If it's in the SDK, node, wallet, or another DCC repo, file it there instead — see [docs/06_contributing.md](docs/06_contributing.md) (also rendered on the live site) for the full list of repos and where each kind of issue belongs.
