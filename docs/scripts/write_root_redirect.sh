#!/bin/bash
# Write the GitHub Pages docroot index.html that redirects to the default docs
# language and version. Usage: write_root_redirect.sh <docroot>
# The target is fixed on purpose: it must never depend on build-loop variables.
set -euo pipefail
docroot="${1:?usage: write_root_redirect.sh <docroot>}"
readonly DEFAULT_PATH="/en/main/"
cat > "${docroot}/index.html" <<HTML
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="utf-8" />
      <title>DecentralChain Documentation</title>
      <link rel="canonical" href="https://docs.decentralchain.io${DEFAULT_PATH}" />
      <meta http-equiv="refresh" content="0; url='${DEFAULT_PATH}'" />
   </head>
   <body>
      <p>Please wait while you're redirected to our <a href="${DEFAULT_PATH}">documentation</a>.</p>
   </body>
</html>
HTML
