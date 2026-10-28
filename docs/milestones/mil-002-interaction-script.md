# MIL-002 Interaction script

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review | pending |

---

## Purpose

Decide whether the lecture's code is correct and tested: `interaction.py` starts a Chrome driver, opens the Wikipedia main page, finds the article count with a CSS (Cascading Style Sheets) selector and prints it, and its logic is tested without a browser.

## Deliverable

`src/scraping_wiki/constants.py`, `src/scraping_wiki/interaction.py` (Doxygen comments, runnable with `python -m scraping_wiki.interaction`) and unit tests in `tests/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The URL and the CSS selector are in `constants.py` and nowhere else | Met | Not met |
| 2 | `interaction.py` uses `webdriver.Chrome`, `get()` and `find_element(By.CSS_SELECTOR, ...)` as in the lecture and prints the element text | Met | Not met |
| 3 | `python -m pytest` passes in a fresh `.venv` and starts no browser | Met | Not met |
| 4 | Every public function and constant has a Doxygen comment | Met | Not met |
| 5 | The code review against the Python `qc-programming-*` checklist is a Go | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs `pyproject.toml`, layout and `.venv` setup |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 3; success criterion 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-29

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add constants.py | Constants for the Wikipedia main page URL (`https://en.wikipedia.org/wiki/Main_Page`), the CSS selector `#articlecount a`, and the Chrome options used for a headless run. | No | |
| 2 | Add interaction.py | The lecture's code as small functions with Doxygen comments: create the Chrome driver (`webdriver.Chrome`, optional headless for Docker), open the main page with `get()`, read the article count with `find_element(By.CSS_SELECTOR, ...)` and print it, then quit the driver. Runnable as `python -m scraping_wiki.interaction`. | No | |
| 3 | Add unit tests | pytest tests for the functions using a fake driver so no browser starts: the URL is opened, the selector is used, the text is printed, the driver is always quit. | No | |
| 4 | Review the code | Review `src/` and `tests/` against the Python `qc-programming-*` checklist and write the `RC-*` record before the pull request. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-project-scaffold.md
