"""@file
@brief End to end test of the lecture script: real Chromium, real network.

It runs only inside the Docker container (see tests/e2e/run_e2e.sh), never on the host desktop.
"""

import re
import subprocess
import sys

## @brief Seconds the script may take before the test fails.
SCRIPT_TIMEOUT_SECONDS: int = 120

## @brief The article count is in the millions; the active editors count is not.
MINIMUM_ARTICLE_COUNT: int = 1_000_000

## @brief One line with a thousands-separated number, for example `7,123,456`.
ARTICLE_COUNT_LINE_PATTERN: str = r"^\d{1,3}(,\d{3})+\n$"


def test_interaction_prints_article_count_when_run_headless() -> None:
    """@brief The script exits with 0 and prints the article count as one line."""
    result = subprocess.run(
        [sys.executable, "-m", "scraping_wiki.interaction", "--headless"],
        capture_output=True,
        text=True,
        timeout=SCRIPT_TIMEOUT_SECONDS,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert re.fullmatch(ARTICLE_COUNT_LINE_PATTERN, result.stdout), repr(result.stdout)
    assert int(result.stdout.strip().replace(",", "")) >= MINIMUM_ARTICLE_COUNT, result.stdout
