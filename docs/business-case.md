# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review | [b344b6e] |

---

## Executive Summary

The Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" has a lecture on web scraping with Selenium: create `interaction.py`, start a Chrome driver, open the Wikipedia main page and print the article count found with a CSS (Cascading Style Sheets) selector. This project delivers that lecture as a small, tested and documented Python 3.13+ program. Every lecture step has a screenshot in the README and in a wiki written in English, Danish and Bahasa Malaysia that explains what was learned.

## Methodological and Standards Foundation

The SQA and QC framework in `framework/` (plan first, then code, every step reviewed), ISO/IEC 25010:2023 for quality characteristics, and the Python conventions of the `coding-conventions` skill.

## Problem Statement

A lecture exercise is usually one untested script that only runs on the author's machine. Course participants who compare solutions (S02) and visitors who browse for ideas (S03) get no setup instructions, no tests and no explanation of what each step teaches. A browser-driven script also cannot be tested on the author's desktop without taking over the mouse and keyboard.

## Business Opportunity

A finished reference solution for the lecture that others can run and compare against, and a template for the later Selenium lectures (clicking links, typing into fields).

## Objectives

1. Provide `interaction.py` that starts a Chrome driver, opens `https://en.wikipedia.org/wiki/Main_Page` with `get()`, finds the anchor inside the `articlecount` div with `find_element` and a CSS selector, and prints its text.
2. Keep constants (URL, selector) in `constants.py` and document the source with Doxygen comments and a `Doxyfile`.
3. Cover the logic with pytest tests that need no browser, and run the browser end to end only in an isolated Docker container.
4. Provide a screenshot for each lecture step, shown in the README and in the wiki.
5. Provide a wiki in English, Danish and Bahasa Malaysia that explains what each lecture step taught.
6. Provide a README from the framework template with instructions to create and use a local `.venv`, upgrade pip, run the project and run its tests.
7. Set the description and topics on the git host repository.

## Scope

### In Scope

Python package under `src/`, tests under `tests/`, documentation under `docs/` (screenshots, wiki, Doxygen), `pyproject.toml`, `Doxyfile`, Python `.gitignore`, Dockerfile for the screenshot and end-to-end run, README, wiki in three languages, repository description and topics.

### Out of Scope

Clicking links and typing into search fields (later lectures), other websites, a graphical or web interface of our own, packaging for PyPI, testing the GUI on the host desktop, reading or testing the `.env` file.

## Expected Benefits

### Tangible Benefits

A working, tested lecture solution; reproducible setup from a clean `.venv`; screenshots and a trilingual wiki that others can follow.

### Intangible Benefits

Practice with the plan-first process on a browser-automation task and with isolated GUI testing.

## Strategic Alignment

Supports completing the Python Pro Bootcamp with reviewed, portfolio-quality projects, and makes the repository useful to other course participants.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Unit tests pass without a browser | All tests pass | `python -m pytest` in the `.venv` |
| 2 | End to end run prints the article count | A number is printed, exit code 0 | Docker container run, log file |
| 3 | Screenshot per lecture step | 7 lecture steps, 7 screenshots | Files in `docs/screenshots/` |
| 4 | Wiki languages | 3 languages, same page set | `framework/scripts/check-languages.sh` |
| 5 | Setup is reproducible | README steps work on a clean `.venv` | Manual run of the README |
| 6 | Runtime dependencies | Exactly one: `selenium` | `pyproject.toml` |
| 7 | Repository metadata | Description and at least 5 topics set | Git host API (application programming interface) response |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Wikipedia changes the page and the selector `#articlecount a` stops matching | End to end run and screenshots fail | Selector lives in `constants.py`; the end to end run is the check; the README names the date it was verified |
| Chrome driver cannot be fetched in the container | No screenshots | Dockerfile installs Chromium and its driver from the distribution packages |
| Token in `.env` leaks | Account compromise | `.env` stays git-ignored, is used only by personal tooling and is never read, tested or imported by the project |
| Running Selenium on the host desktop takes the user's mouse and keyboard | Interrupted work | GUI runs only in Docker, as `framework/process/gui-testing.md` requires |
| Translations drift from the English text | Inconsistent wiki | English is authoritative; same page set in all languages; `check-languages.sh` |

## Assumptions

- Python 3.13 or newer, Docker and (optionally) Doxygen are installed on the Product Owner's machine.
- The Product Owner (S01) is the reviewer; in autonomous mode the AI acts as S01's stand-in and records it in the review.
- The git host is reachable and the `.env` token may create repository metadata and issues.
- Wikipedia is reachable from the Docker container.

## Constraints

- Python 3.13 or newer, `venv`, `pytest`, folders `src/`, `tests/`, `docs/`, constants in `constants.py`, Doxygen comments and a `Doxyfile`.
- Runtime dependencies only where needed: `selenium` is the one the lecture requires.
- Product Owner language English, domain IT; wiki in English, Danish and Bahasa Malaysia.
- No GUI or browser test on the host desktop.

## Cost–Benefit Assessment

Qualitative, by decision: this is an unpaid course assignment with no revenue or budget, so no ROI can be calculated; the cost is the time of S01 and the AI.

| Costs | Benefits |
| --- | --- |
| A few hours of the Product Owner's time and the AI's work; Docker image build time | A finished, documented lecture solution that others can run and learn from |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; accepts each milestone |
| S02 | Course participants; need readable, runnable code with the assignment's names and run instructions |
| S03 | Repository viewers; need a clear description, topics and README and no extra runtime dependencies |

## Recommendation

Proceed — the scope is small, the cost is low and it completes the lecture with a reusable, documented result.

---

[SA-001]: ./stakeholder-analysis.md
[b344b6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/commit/b344b6e2cba397e23714c73a45ad4155bb1e00e0
