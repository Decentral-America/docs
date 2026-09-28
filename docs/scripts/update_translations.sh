#!/bin/bash
# Regenerate translation catalogs after English content changes (WP6 in
# PLAN-docs-expansion.md). Run this from a checkout whose path has no
# spaces — building with a space in the path corrupts the `#:` location
# comments Sphinx writes into the .pot/.po files (verified while adding
# this script: an out-of-tree/spaced build path produced comments like
# `#: ../../../../../Users/name/My Docs/docs/01_introduction.md:1`
# instead of the correct `#: ../../01_introduction.md:1`).
#
# This only touches the .pot/.po catalogs — it never edits committed
# English content, and it never overwrites an existing translated
# msgstr; sphinx-intl update only adds new msgids and marks removed
# ones obsolete. Review the diff (it will touch every language under
# docs/locales/) before committing, and let Gitlocalize's own sync
# reconcile with in-flight translator work rather than force-pushing
# over it.
set -euo pipefail
cd "$(dirname "$0")/.."   # docs/

python3 -m sphinx -b gettext . _build/gettext
python3 -m sphinx_intl update -p _build/gettext -d locales \
  $(find locales -mindepth 1 -maxdepth 1 -type d ! -name en -exec basename {} \; | sed 's/^/-l /')

echo "Done. Review with: git status docs/locales && git diff docs/locales"
