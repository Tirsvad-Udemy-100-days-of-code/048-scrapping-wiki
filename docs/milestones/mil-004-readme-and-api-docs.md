# MIL-004 README and API docs

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review | pending |

---

## Purpose

Decide whether a newcomer can set up, run and test the project from the README alone, and see each lecture step as a screenshot.

## Deliverable

`README.md` built from the framework template, with the screenshots of the 7 lecture steps, and a verified Doxygen build.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `README.md` follows `framework/templates/README-template.md` and `check-readme.sh` passes | Met | Not met |
| 2 | README shows how to create and use a local `.venv` and runs `python -m pip install --upgrade pip` | Met | Not met |
| 3 | README shows how to run the project, run the tests and run the Docker end to end run | Met | Not met |
| 4 | README shows the 7 lecture step screenshots and the images exist | Met | Not met |
| 5 | The README steps work on a fresh `.venv` (commands executed and passing) | Met | Not met |
| 6 | `doxygen Doxyfile` builds without warnings | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | The README uses its screenshots and the Docker run |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 2, 4 and 6; success criterion 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-31

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write README.md from the template | Fill every section of the framework README template: overview, requirements (Python 3.13 or newer, Docker, optional Doxygen), the screenshots of the 7 lecture steps, license and links, and the appendix of project documents. | No | |
| 2 | Document .venv, pip upgrade, run and tests | Setup steps for Windows and Linux/macOS: create `.venv`, activate it, `python -m pip install --upgrade pip`, `pip install -e ".[dev]"`; the run command, `python -m pytest`, and the Docker command for the end to end run. | No | |
| 3 | Verify the README steps and the Doxygen build | Execute the README commands in a fresh `.venv`, run `doxygen Doxyfile`, run `check-readme.sh`, and fix whatever fails. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-screenshots-in-docker.md
