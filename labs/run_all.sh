#!/usr/bin/env bash
# Runs every lab and fails if any assertion fails. Creates a venv with numpy on first run.
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
  .venv/bin/pip install -q numpy
fi
status=0
for f in lab*.py; do
  echo "=== $f"
  if .venv/bin/python "$f"; then echo "PASS $f"; else echo "FAIL $f"; status=1; fi
done
exit $status
