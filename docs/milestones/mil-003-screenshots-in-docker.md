# MIL-003 Screenshots in Docker

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review | pending |

---

## Purpose

Decide whether the browser run works end to end and the lecture steps are documented visually, without ever driving the host desktop.

## Deliverable

`Dockerfile` and `.dockerignore`, the end to end (e2e) run and screenshot capture under `tests/e2e/`, the lecture step scripts, and seven PNG (Portable Network Graphics) screenshots in `docs/screenshots/` (one per lecture step), with the run log and exit code.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The container run exits 0 and its log shows the article count printed by `interaction.py` | Met | Not met |
| 2 | `docs/screenshots/` has one PNG for each of the 7 lecture steps, named `step-1-...` to `step-7-...` | Met | Not met |
| 3 | `.dockerignore` excludes `.env` and `.venv`, and the image contains no `.env` | Met | Not met |
| 4 | No browser or GUI was started on the host; results were read from the shared results folder | Met | Not met |
| 5 | The default `python -m pytest` run does not collect the e2e tests | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The e2e run executes `interaction.py` |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3 and 4; success criteria 2 and 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-30

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Dockerfile and .dockerignore | Image with Python 3.13, Chromium and its driver from the distribution packages, running as a non-root user and installing the project. `.dockerignore` keeps `.env`, `.venv` and `.git` out of the build context. | No | |
| 2 | Add lecture step scripts | One script per lecture step (create the file, import Selenium, initialise the Chrome driver, navigate with `get()`, identify the element, `find_element` and print, and the hint at future interactions) so each step's code can be shown and run. | No | |
| 3 | Add e2e run and screenshot capture | `tests/e2e/` code that runs `interaction.py` against the live Wikipedia main page and writes one PNG for each of the 7 lecture steps (code views for steps 1 to 3, page views for steps 4 to 7 with the target element highlighted, the printed count for step 6) plus a log and an exit code file into a results folder. Environment: Docker container (headless Chromium), never the host desktop. | No | |
| 4 | Run the e2e in Docker and keep the screenshots | Build the image, run it with the results folder mounted, read the log and exit code, and copy the 7 screenshots to `docs/screenshots/`. Environment: Docker container. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-interaction-script.md
