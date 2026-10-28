#!/bin/bash
# Translation checks, run by pr_check_workflow.yml (`translations`) and by the
# deploy workflow before it uploads the site:
#   1. every target locale has a catalog for every section, every catalog
#      passes `msgfmt --check`, and no translation breaks the English markup;
#   2. the coverage per locale, on a copy of the catalogs updated against the
#      current English (also written to the job summary in CI);
#   3. the publish rule: a locale in docs/locales/PUBLISHED is either at
#      least 80% translated or marked `partial`.
# Usage: check_translations.sh <work dir>. Needs the docs requirements and
# GNU gettext (msgfmt). See docs/scripts/translations.py.
set -euo pipefail
work="${1:?usage: check_translations.sh <work dir>}"
mkdir -p "${work}"
work="$(cd "${work}" && pwd)"
cd "$(dirname "$0")/.."   # docs/

python3 -m sphinx -q -b gettext . "${work}/gettext"
python3 scripts/translations.py check locales "${work}/gettext"

rm -rf "${work}/locales"
cp -R locales "${work}/locales"
python3 -m sphinx_intl update -p "${work}/gettext" -d "${work}/locales" -w -1 \
  $(find locales -mindepth 1 -maxdepth 1 -type d ! -name en -exec basename {} \; | sed 's/^/-l /') > /dev/null
python3 scripts/translations.py coverage "${work}/locales" --markdown | tee -a "${GITHUB_STEP_SUMMARY:-/dev/null}"
python3 scripts/translations.py publish "${work}/locales"
