# MIL-005 Wiki in three languages

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review | [b344b6e] |

---

## Purpose

Decide whether the wiki explains what each lecture step taught, with its screenshot, in English, Danish and Bahasa Malaysia, and is ready to publish.

## Deliverable

`docs/wiki/` with the same page set in English (`Page.md`), Danish (`Page-da.md`) and Bahasa Malaysia (`Page-ms.md`), the screenshots, `_Sidebar.md`, and the publish workflow.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every English page has a `-da` and a `-ms` page, and each page starts with the language line | Met | Not met |
| 2 | The lecture steps page has all 7 steps, each with its screenshot and a "what we gained" paragraph, in all three languages | Met | Not met |
| 3 | Code blocks, commands, file names and IDs stay in English in all languages | Met | Not met |
| 4 | `_Sidebar.md` lists every language and every page | Met | Not met |
| 5 | `.gitea/workflows/publish-wiki.yml` is installed from the framework template | Met | Not met |
| 6 | `framework/scripts/check-languages.sh` passes | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | The wiki links to the README instructions and reuses the screenshots |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 5; success criteria 3 and 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-02

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki pages | Pages Home, Lecture-Steps (each of the 7 steps with its screenshot and what we gained), Setup-and-Run and Docker-Testing, following `framework/process/wiki.md`. English is the authoritative text. | No | |
| 2 | Translate the wiki to Danish | The same page set as `Page-da.md`, page by page, with the language line; code, commands and file names stay in English. | No | |
| 3 | Translate the wiki to Bahasa Malaysia | The same page set as `Page-ms.md`, page by page, with the language line; code, commands and file names stay in English. | No | |
| 4 | Add sidebar, screenshots and publish workflow | `_Sidebar.md` listing all languages and pages; screenshots reachable from the pages; `.gitea/workflows/publish-wiki.yml` copied from the framework template. The wiki secret and runner are the host's setup and are reported, not created. | No | |
| 5 | Check the wiki | Run `check-languages.sh` and a link check of the pages and images. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-004]: ./mil-004-readme-and-api-docs.md
[b344b6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/commit/b344b6e2cba397e23714c73a45ad4155bb1e00e0
