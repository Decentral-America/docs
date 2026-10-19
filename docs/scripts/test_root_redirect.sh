#!/bin/bash
# Test for write_root_redirect.sh: the docroot index.html must send visitors to
# /en/main/, whatever language the build loop in buildDocs.sh happened to finish on.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
docroot="$(mktemp -d)"
trap 'rm -rf "${docroot}"' EXIT

# Simulate the leftover loop variable that caused the bug.
export current_language=pt
"${here}/write_root_redirect.sh" "${docroot}"

grep -q "content=\"0; url='/en/main/'\"" "${docroot}/index.html" \
  || { echo "FAIL: meta refresh does not target /en/main/"; cat "${docroot}/index.html"; exit 1; }
grep -q 'href="/en/main/"' "${docroot}/index.html" \
  || { echo "FAIL: fallback link does not target /en/main/"; exit 1; }
if grep -q '/pt/' "${docroot}/index.html"; then
  echo "FAIL: redirect leaks the build loop's last language"; exit 1
fi
echo "PASS: root redirect targets /en/main/"
