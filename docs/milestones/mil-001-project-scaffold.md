# MIL-001 Project scaffold

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review | [b344b6e] |

---

## Purpose

Decide whether the repository is ready for code: layout, tooling and configuration exist, a fresh clone can create a local virtual environment, and the repository is described on the git host.

## Deliverable

`pyproject.toml`, Python `.gitignore`, `src/scraping_wiki/` and `tests/` skeletons, `Doxyfile`, repository description and topics on the git host, `origin` pointing at the repository named by the Product Owner.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` requires Python 3.13 or newer; the only runtime dependency is `selenium`; `pytest` is a `dev` extra | Met | Not met |
| 2 | `.gitignore` is the Python one and also covers `.env`, `.venv` and `docs/doxygen/` | Met | Not met |
| 3 | Folders `src/`, `tests/` and `docs/` exist | Met | Not met |
| 4 | `doxygen Doxyfile` runs without error | Met | Not met |
| 5 | Repository description and at least 5 topics are set on the git host (API response checked) | Met | Not met |
| 6 | `.env` is not tracked by git | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 2, 6 and 7; success criteria 6 and 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-28

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Project configuration: name `scraping-wiki`, Python 3.13 or newer, `selenium` as the only runtime dependency, `dev` extra with pytest, setuptools `src` layout and pytest settings (`testpaths`, `pythonpath`). | No | |
| 2 | Add Python .gitignore and folder layout | Python `.gitignore` that also ignores `.env`, `.venv`, `docs/doxygen/` and the e2e results folder; create `src/scraping_wiki/` and `tests/`. | No | |
| 3 | Add Doxyfile | Doxygen configuration reading `src/` and writing to `docs/doxygen/`, so Doxygen comments in the source build into API documentation. | No | |
| 4 | Set repository description and topics | On the git host, set the description and topics (selenium, web-scraping, python, udemy, 100-days-of-code, wikipedia) through its API (application programming interface) with the token from `.env`, which is personal tooling and never part of the project. Check that `origin` is the repository the Product Owner named and correct it if not. | No | |
| 5 | Start the AI prompt log | Create `docs/ai-prompts/session-NNN/prompts.md` and check the repository's visibility through the host's API; when it is public, add `/docs/ai-prompts/` to `.gitignore` ([ai-prompt-log.md](../../framework/process/ai-prompt-log.md)). | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[b344b6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/commit/b344b6e2cba397e23714c73a45ad4155bb1e00e0
