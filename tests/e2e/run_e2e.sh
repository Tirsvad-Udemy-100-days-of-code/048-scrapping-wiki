#!/usr/bin/env bash
# End to end run, inside the Docker container: run the e2e test, then capture the
# screenshots of the seven lecture steps. Results are files in the folder given as $1:
#   e2e.log        the combined output
#   exit-code.txt  0 when both parts passed
#   screenshots/   one PNG per lecture step
set -uo pipefail

results="${1:-/results}"
mkdir -p "$results/screenshots"
status=0

{
  python -m pytest tests/e2e -p no:cacheprovider --override-ini="addopts=" -q || status=$?
  python tests/e2e/capture_screenshots.py "$results/screenshots" || status=$?
} >"$results/e2e.log" 2>&1

cat "$results/e2e.log"
echo "$status" >"$results/exit-code.txt"
exit "$status"
