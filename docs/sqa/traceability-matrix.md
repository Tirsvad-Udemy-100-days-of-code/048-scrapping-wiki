# Traceability Matrix: Scraping Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [ADR-0001], [ADR-0002], [RC-001], [RC-002], [RC-003], [RC-004], [RC-005], [RC-006], [RC-007], [RC-008], [RC-009], [RC-010], [RC-011], [RC-012], [RC-013], [RC-014], [RC-015], [RC-016], [RC-017], [RC-018], [RC-019] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the baseline milestone and its review records (autonomous, not independent) | [915cba5] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the re-review records RC-017 to RC-019 of BC-001, PP-001 and MIL-006 for task 6; reviewed in autonomous mode, not independent | [11aeac1] |

---

## Purpose

Tracks backward and forward links between the artifact instances of Scraping Wiki so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-017] (Go, re-review after task 6), [RC-013], [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-018] (Go, re-review after task 6), [RC-014], [RC-003] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | [MIL-003] | [RC-005], [RC-010] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | [MIL-004] | [RC-006], [RC-012] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001], [MIL-003] | [MIL-005] | [RC-007] |
| [MIL-005] | MIL | en | it | [BC-001], [PP-001], [MIL-004] | [MIL-006] | [RC-008] |
| [MIL-006] | MIL | en | education | [BC-001], [PP-001], [MIL-005] | - | [RC-019] (Go, re-review after task 6), [RC-015] |
| [ADR-0001] | ADR | - | - | [BC-001], [MIL-002] | - | [RC-009] |
| [ADR-0002] | ADR | - | - | [BC-001], [MIL-002] | - | [RC-011] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-006] | - | [RC-016], [RC-008] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] (criterion 2), [MIL-003] (criterion 1) | [ADR-0002] | - | Covered |
| CN-002 | [MIL-003] (criterion 4) | - | - | Covered |
| CN-003 | [MIL-003] (criterion 2), [MIL-005] (criteria 1 and 2), [MIL-006] (criterion 3) | - | - | Covered |
| CN-004 | [MIL-002] (criterion 2), [MIL-004] (criterion 1), [MIL-006] (criterion 4, the README check) | [ADR-0001] | - | Covered |
| CN-005 | [MIL-004] (criteria 2 and 3), [MIL-006] (criterion 2) | - | - | Covered |
| CN-006 | [MIL-001] (criterion 5), [MIL-004] (criterion 1), [MIL-006] (criteria 4 and 5) | - | - | Covered |
| CN-007 | [MIL-001] (criterion 1), [MIL-006] (criterion 5, the metadata) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [MIL-005] | Criterion 5 of the accepted milestone names the publish workflow `.gitea/workflows/publish-wiki.yml`, which the repository no longer has (it uses the shared workflows of the git host) | [RC-015] | Open | The accepted milestone is not changed; the Open Issues of [PP-001] record it |

## Coverage Notes

- `-` in Upstream means the instance is foundational, in Downstream that nothing is built on it yet.
- This matrix was created with [MIL-006]; until then the project had no traceability matrix.
- The wiki (`docs/wiki/`) is documentation, not an artifact with an ID or a Language and Domain row; it has its own review record, [RC-016], and was reviewed for its content as part of [RC-008].
- The domain of [BC-001], [PP-001], [MIL-006] and the wiki is `education` since [MIL-006]. The other documents keep the domain `it` they were accepted with; a change of their domain would need a new review of each (see the Open Issues of [PP-001]). The ADRs have no Language and Domain rows.
- [MIL-006] changes no source file; its task 6 changes only the indentation of the test script `tests/e2e/run_e2e.sh`, checked by the shell format check of the Validate workflow. The review records RC-010 and RC-012 review the code of MIL-002 and MIL-003 (listed with their milestone). No view or test-plan artifact exists (the scope excludes them), so the milestones' Go/No-Go criteria are the quality checks.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-scaffold.md
[MIL-002]: ../milestones/mil-002-interaction-script.md
[MIL-003]: ../milestones/mil-003-screenshots-in-docker.md
[MIL-004]: ../milestones/mil-004-readme-and-api-docs.md
[MIL-005]: ../milestones/mil-005-wiki.md
[MIL-006]: ../milestones/mil-006-framework-baseline.md
[ADR-0001]: ../adr/adr-0001-flat-package-layout.md
[ADR-0002]: ../adr/adr-0002-article-count-selector.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-project-scaffold.md
[RC-005]: ./reviews/rc-005-mil-002-interaction-script.md
[RC-006]: ./reviews/rc-006-mil-003-screenshots-in-docker.md
[RC-007]: ./reviews/rc-007-mil-004-readme-and-api-docs.md
[RC-008]: ./reviews/rc-008-mil-005-wiki.md
[RC-009]: ./reviews/rc-009-adr-0001-flat-package-layout.md
[RC-010]: ./reviews/rc-010-code-mil-002.md
[RC-011]: ./reviews/rc-011-adr-0002-article-count-selector.md
[RC-012]: ./reviews/rc-012-code-mil-003.md
[RC-013]: ./reviews/rc-013-business-case-baseline.md
[RC-014]: ./reviews/rc-014-project-plan-baseline.md
[RC-015]: ./reviews/rc-015-milestone-006.md
[RC-016]: ./reviews/rc-016-wiki.md
[915cba5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/commit/915cba58cb9ea86be0193540eb965d78f4862548
[RC-017]: ./reviews/rc-017-business-case-task-6.md
[RC-018]: ./reviews/rc-018-project-plan-task-6.md
[RC-019]: ./reviews/rc-019-milestone-006-task-6.md
[11aeac1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/commit/11aeac167a980ba36378ec10a6d25d4fcbf541a7
