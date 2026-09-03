# AGENTS.md — DecentralChain Docs

Technical orientation for anyone (human or AI agent) contributing to this repo. Read this before touching content, `conf.py`, or the build pipeline — several things here are non-obvious and have already caused real bugs.

## What this is

The Sphinx + MyST documentation site for DecentralChain (DCC), a blockchain protocol forked from Waves. Published at `docs.decentralchain.io` via GitHub Pages. Built in **2 branches** (`main`, `dev`) × **11 languages**, so every content change gets multiplied across that matrix.

## Stack

- **Sphinx 9** + **MyST** (write `.rst` or `.md`, both are first-class — `source_suffix = ['.rst', '.md']`)
- **pydata-sphinx-theme** for HTML rendering
- **sphinx-intl** + gettext `.po` files for translation (11 locales in `docs/locales/`)
- Content lives in `docs/`, config in `docs/conf.py`, pinned deps in `docs/requirements.txt`

Do not propose migrating this to Docusaurus/MkDocs/Starlight. It was evaluated in depth (see git log around Sept 2026 for the research) — this content is table-and-cross-reference-dense (300+ `csv-table` directives, 700+ `:ref:` cross-references that Sphinx validates at build time), which Markdown-first tools handle worse, not better. Sphinx is the right tool here.

## Local build

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -W -b html docs/ /tmp/out   # -W = warnings fail the build, matches CI
python3 -m http.server 8000 --directory /tmp/out
```

To test a specific version/language combo (affects the version-switcher and language-selector in the rendered navbar):

```bash
export current_version=dev      # or "main"
export current_language=es      # or any dir name under docs/locales/
sphinx-build -b html docs/ /tmp/out -D language="${current_language}"
```

Also run the link checker before opening a PR — it won't block CI (see below) but tells you if you just broke something external:

```bash
sphinx-build -b linkcheck docs/ /tmp/linkcheck-out
```

## The build/deploy pipeline

`docs/buildDocs.sh` is the actual build engine. It:
1. Loops over every remote branch except `HEAD`/`gh-pages` (currently `main`, `dev`)
2. For each branch, checks it out, then loops over `en` + every dir under `docs/locales/`
3. Runs `sphinx-build` once per (branch, language) pair → 22 builds total right now
4. `rsync`s every build's output into one shared `docroot`, producing the final `/{language}/{version}/` URL layout
5. Emits the docroot path as a `GITHUB_OUTPUT` for the workflow to pick up

`.github/workflows/github_pages_workflow.yml` calls that script, then publishes via `actions/upload-pages-artifact` + `actions/deploy-pages` (the current GitHub-native standard — do not swap back to a hand-rolled `git push --force` to `gh-pages`, that was the old pattern and it's what let the site go dark for months, since the workflow's only trigger was manual `workflow_dispatch`). It now also triggers on every push to `main`.

**Known real gap, evaluated and intentionally not solved this way**: `sphinx-polyversion` looks like the obvious tool to replace the branch loop, but it has *zero* locale support and assumes `/{version}/` as the outer layout, the opposite of this site's `/{language}/{version}/` — adopting it would need 11 separate invocations and custom fan-out code, i.e. worse than the current bash loop. Don't reach for it without solving that mismatch first.

**Requires**: repo Settings → Pages → Source = "GitHub Actions" (not "Deploy from a branch"). If that ever gets reset, the deploy job will fail even though the build succeeds.

## PR checks

`.github/workflows/pr_check_workflow.yml` runs two jobs on every PR to `main`/`dev`:
- `build_check`: `sphinx-build -W` — **blocks merge** on any warning (broken `:ref:`, bad directive, etc.)
- `link_check`: `sphinx-build -b linkcheck` — **does not block merge** (`continue-on-error: true`), because external links go stale independent of any PR and shouldn't hold up unrelated work. Check its output anyway; it catches real rot.

## Content conventions

- **Cross-references**: use `:ref:` (RST) or the MyST equivalent, not raw links, for anything pointing at another page in this site. `autosectionlabel_prefix_document = True` means every heading gets an implicit label `path/to/doc:Heading Text` — reference it that way. This is what makes `-W` catch broken internal links; don't defeat it by hardlinking to `.html` paths.
- **Tables with rich content** (links, math, multi-line explanations per cell): use `.. csv-table::` sourcing a `.csv` file under `docs/_static/**/tables/`, not a plain Markdown table. Markdown tables cannot hold multi-paragraph cell content or survive a `|` inside inline math — this was confirmed by direct testing, not assumption. Look at `docs/_static/02_decentralchain/tables/003_JSON-Representation.csv` for the pattern (cells contain `:ref:` and `:math:` inline).
- **Math**: `:math:` role / `$...$` renders via MathJax, works fine inline including inside table cells.
- **Admonitions**: MyST `{note}` / `{warning}` colon-fence syntax in `.md` files, or `.. note::` / `.. warning::` in `.rst`.
- Don't add content assuming `jupyter_sphinx`, `matplotlib.sphinxext.plot_directive`, `ablog`, or `numpydoc` — they're enabled in `conf.py` but **zero files use them**. If you have a real reason to use one, fine, but don't treat their presence in `extensions` as evidence they're load-bearing; they're dead config.

## Theming & styling

This is the part someone focusing on visual design/branding needs most. Everything below is verified against **pydata-sphinx-theme 0.21.0 specifically** (the version pinned in `docs/requirements.txt`) — theme internals have genuinely changed between versions (e.g. `footer_items` → `footer_start`, see the git history around Sept 2026), so don't trust older blog posts or a different project's `conf.py` as gospel.

### Where things live

- `docs/conf.py` — `html_theme_options` dict controls layout/navbar/logo/switcher config. `html_context` controls default color mode and feeds the custom version/language data.
- `docs/_static/custom.css` — the site's own CSS overrides, loaded via `html_css_files = ["custom.css"]`
- `docs/_static/logo.png` / `logo-dark.png` — light/dark logo variants
- `docs/_templates/language-selector.html` — the one custom navbar template (see below)

### The CSS variable system — use it, don't fight it

The theme exposes everything as CSS custom properties prefixed `--pst-*`, defined once per color mode. **Never hardcode a hex color in `custom.css`** — it will look right in light mode and wrong (or invisible) in dark mode, because the theme has no `prefers-color-scheme` fallback for your own rules; it only reacts to its own variables.

The semantic color variables that matter most for branding:

- `--pst-color-primary` / `--pst-color-secondary` — the two brand hooks. Links (`--pst-color-link`, `--pst-color-link-hover`) are literally *aliased* to these, so retheming links is just retheming these two.
- `--pst-color-accent` — a third accent color (pink by default in the base theme)
- `--pst-color-background` / `--pst-color-on-background` — page background / text on it
- `--pst-color-surface` / `--pst-color-on-surface` — card/panel-like surfaces and their text
- `--pst-color-border` / `--pst-color-border-muted`
- `--pst-color-text-base` / `--pst-color-text-muted` / `--pst-color-heading`

There is **no single "brand color" master switch** — override `--pst-color-primary`, `--pst-color-secondary`, and optionally `--pst-color-accent`, and links/buttons/badges cascade from those automatically.

### Light/dark overrides — the pattern that actually works

The theme selects mode via an **attribute on `<html>`**, not a media query:

```css
html[data-theme="light"] { --pst-color-primary: #your-light-value; }
html[data-theme="dark"]  { --pst-color-primary: #your-dark-value; }
```

Both blocks are required for any color override. Writing it under bare `html { }` works for non-color variables (font sizes, spacing) but **loses to the theme's own `html[data-theme=...]` rules for colors** — a same-selector-specificity trap, easy to get bitten by.

This project's own `docs/_static/custom.css` has a live example of getting this wrong, worth fixing first before adding anything new: `.sd-card-header` sets `color: #150458 !important` (a dark purple) in the light-mode block, then the dark-mode override block (`html[data-theme=dark] .sd-card .sd-card-header`) correctly swaps `background-color` to `var(--pst-color-background)` but **copies the same `color: #150458 !important` unchanged** — dark purple text on a dark background, unreadable. Separately, `.custom-button` and its `a`/`p` children are hardcoded `background-color: #DCDCDC` / `color: #484848` with **no dark-mode override at all**. Both are exactly the "one mode only" trap described above, not a hypothetical — they're in production right now.

Also relevant: color-variable theming in pydata-sphinx-theme 0.21 is explicitly flagged upstream as a **beta feature with no backward-compatibility guarantee** — pin the theme version deliberately (already done here) and re-check this section on any future theme bump.

### sphinx-design (`.sd-card`, grids, buttons) — don't theme it separately

This site uses sphinx-design for the homepage cards/grid (`docs/conf.py` extension `sphinx_design`). The theme already maps every `--sd-color-*` variable sphinx-design uses onto the matching `--pst-color-*` variable, per mode, specifically so that **overriding `--pst-color-primary` etc. also re-themes cards/badges/buttons automatically** — that mapping is the intended override point. Do not write separate `--sd-color-*` dark-mode rules; redefine the `--pst-*` variables instead and let it cascade.

One real gotcha inherited from sphinx-design itself: its own stylesheet uses `!important` liberally. Any custom `.sd-card`/`.sd-tab-set`/`.sd-dropdown` override in `custom.css` will likely need `!important` too and a selector at least as specific as `.bd-content .sd-card` to actually win.

### Logo / branding config

```python
html_theme_options = {
    "logo": {
        "image_light": "...",       # optional — falls back to html_logo
        "image_dark": "logo-dark.png",
        "alt_text": "DecentralChain",
        "link": "...",              # optional — docname or external URL
        "text": "...",              # optional — text beside/instead of image
    },
}
```

`image_dark`/`image_light` are current, correct keys for 0.21.0 (not deprecated). The deprecated key to avoid is top-level `logo_link` — use `logo["link"]` instead. Note this repo's `conf.py` sets `html_logo = "_static/logo.png"` (path prefixed with `_static/`) but `logo["image_dark"] = "logo-dark.png"` (bare filename, no prefix) — inconsistent style, but verified to still resolve correctly at build time, so it's a style nit to clean up, not an active bug.

**Dark-mode image washout**: the theme applies `filter: brightness(0.8) contrast(1.2)` plus a white background to any `<img>` in the main content area when in dark mode, unless the image has class `only-dark`, `only-light`, or `dark-light`. Any diagram/screenshot embedded in the docs body (not the navbar logo, which is handled separately by `image_dark`) that looks washed out or has a jarring white box around it in dark mode needs one of those classes applied.

### Layout — navbar/sidebar/footer slots

These are named "slots" you assign component lists to in `html_theme_options`. Current 0.21.0 defaults, useful as a reference for what's customized here vs. stock:

```
navbar_start            = navbar-logo
navbar_center           = navbar-nav              (this repo: version-switcher, navbar-nav)
navbar_end              = theme-switcher, navbar-icon-links
navbar_persistent       = (empty)                 (this repo: language-selector, search-button)
primary_sidebar_end     = sidebar-ethical-ads
secondary_sidebar_items = page-toc, edit-this-page, sourcelink
footer_start            = copyright, sphinx-version   (this repo: copyright only)
footer_center           = (empty)
footer_end              = theme-version
```

Note `footer_start`/`footer_center`/`footer_end` (the page footer) got renamed from a single `footer_items` list at some point before 0.21 — but `article_footer_items` and `content_footer_items` (per-page footer slots, different from the site footer) **kept** the old `_items` naming. Easy to mix these up; check which footer you actually mean.

Custom entries in any of these lists (like this repo's `language-selector`) resolve to a Jinja2 template file of the same name (`.html` optional) in `templates_path` (`docs/_templates/`). See `docs/_templates/language-selector.html` for the working pattern — it's plain Jinja reading `html_context`, no special wrapper markup required unless you want it to visually match a built-in dropdown's styling.

### Fonts / typography

`--pst-font-family-base`, `--pst-font-family-heading`, `--pst-font-family-monospace`, and the `--pst-font-size-h1` … `-h6` / `--pst-font-size-base` scale are all overridable the same way (these aren't color variables, so a single `html { }` block is fine — no dark/light split needed for typography).

### Common pitfalls, specific to this repo

1. **Hardcoded colors with no dark-mode pair** — see the `custom.css` bug above. Grep for `background-color:` / `color:` with literal hex/named values before adding new rules; prefer `var(--pst-color-*)`.
2. **Testing only in one color mode.** Always toggle the theme switcher (top-right, built-in) or force it via `html_context = {"default_mode": "dark"}` locally before calling a style change done.
3. **Forgetting sphinx-design's `!important`.** A card override that "does nothing" is almost always this.
4. **Confusing the two footer slot systems** (`footer_start/center/end` vs `article_footer_items`/`content_footer_items`).
5. **Deprecated key names**: `pygment_light_style`/`pygment_dark_style` (missing the `s` — current is `pygments_light_style`/`pygments_dark_style`) and top-level `logo_link`.

## Version/language switcher

Both live in the navbar, both are populated from `html_context` built in `conf.py` (around the "SETUP THE RTD LOWER-LEFT" section — the name is stale, it now drives a proper navbar dropdown, not an RTD-style sidebar):
- **Version switcher**: native pydata-sphinx-theme feature, config'd via `html_theme_options["switcher"]`, data comes from `docs/_static/switcher.json`. Add a branch → add an entry there too, or it won't show up as a switch target (it'll still build fine, just won't be selectable).
- **Language switcher**: pydata-sphinx-theme has **no native language switcher** (confirmed via their own open issue #2212) — `docs/_templates/language-selector.html` + `docs/_static/language_select.js` are custom, hand-rolled to fill that gap. Don't delete them thinking they're vestigial; they're the only reason the language dropdown exists.
- Both read from `html_context['versions']` / `html_context['languages']`, which are computed once per build from `git branches` and `os.scandir('locales')`. Do not hardcode `'en'` into that list — it's already picked up from `docs/locales/en/` (a real gettext catalog dir), a duplicate entry bug already happened once from exactly that mistake.

## Adding a new language

1. Generate the `.po` catalog via `sphinx-intl` (see `docs/locales/` for existing structure — each language is `LC_MESSAGES/*.po` + compiled `.mo`)
2. Translate the `.po` files (GitLocalize integration handles this for maintained languages — see `docs/06_contributing.md`)
3. Nothing else — `buildDocs.sh`'s locale loop and the language-selector template both discover new `docs/locales/*` dirs automatically

## Adding a new version/branch

1. Create the branch normally
2. Add an entry to `docs/_static/switcher.json` (`version`, `url`, optional `name`/`preferred`) — this is the one manual step, everything else in the pipeline discovers branches automatically via `git for-each-ref`

## Things that look like bugs but aren't

- `matcher.decentralchain.io` linkcheck failure (SSL cert mismatch) and `data-service.decentralchain.io` (404): both are the *correct* documented endpoints per `../DecentralChain/docs/UPSTREAM.md`'s network table. They're live infra failures on services this repo doesn't control — don't "fix" by changing the URL, that would make the docs wrong to work around someone else's outage.
- GitHub anchor links like `...#readme` or `...#some-heading` sometimes get flagged broken by `linkcheck` — GitHub renders those anchors client-side via JS, which a static-HTML link checker can't see. Verify manually (`curl -sI <url>` plus check the target heading exists) before "fixing" a false positive.
- Redirects (`master` → `main`, `developers.google.com/protocol-buffers` → `protobuf.dev`) show as `redirect` not `broken` in linkcheck output — worth fixing for cleanliness but not urgent; they still resolve.

## Spanish translation

Currently ~49% complete and has real content-accuracy issues (some translated `:ref:` targets drifted from the actual English section names, e.g. a translated target reading `02_token(activo)` when the real doc is `02_token(asset)`). This is a known, accepted state — not a build blocker, not something to silently "fix" by guessing corrections. If you're doing translation work, coordinate on this specifically.
