# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review | [b344b6e] |

---

## Purpose

Name the people affected by the project so that owners and reviewers in the other documents cite stakeholder IDs. The method is the power/interest grid and FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus design, implementation, interface and physical constraints). The project is a course assignment, so the analysis is short ([BC-001]).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, tested and documented lecture solution with screenshots and a three-language wiki |
| S02 | Udemy coursists | Course participants who share code and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no heavy runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, does the work and accepts every milestone.
- **Keep Informed (S02):** cannot change the project but depend on its quality and clarity; they get the README and the wiki.
- **Monitor (S03):** casual visitors; they get the repository description, topics and README.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The script opens Wikipedia and prints the article count as in the lecture | Functionality |
| CN-002 | S01 | Browser runs never take over the desktop | Supportability |
| CN-003 | S01 | Each lecture step has a screenshot and the wiki explains what was learned, in three languages | Functionality |
| CN-004 | S02 | Code is readable and runs from the README steps; uses the assignment's names (`interaction.py`) | Usability |
| CN-005 | S02 | Setup with a local `.venv` and tests with pytest works first time | Supportability |
| CN-006 | S03 | Clear repository description, topics and README | Usability |
| CN-007 | S03 | No runtime dependencies beyond what the lecture needs | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat | Per milestone | Pull request and summary | MIL-001 to MIL-005 |
| S02 | README and wiki | At release | Run instructions, screenshots, explanations | MIL-004, MIL-005 |
| S03 | Repository page | At release | Description, topics, README | MIL-001, MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies; the lecture needs Selenium | S03, S01 | Selenium is the only runtime dependency; pytest stays a `dev` extra; the README says why |
| S02 wants it to run on their machine; GUI runs must not take S01's desktop | S02, S01 | `python -m scraping_wiki.interaction` runs locally for S02; S01's own runs and the screenshots use Docker |

## Traceability Analysis

### Stakeholder to Actor / Use Case

| Stakeholder | Actor | Use case |
| --- | --- | --- |
| S01, S02 | Course participant | Run the script and read the article count (a plain task; no use case document for this size) |

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objective 1 in [BC-001] |
| S01 | CN-002 | Objective 3 in [BC-001] |
| S01 | CN-003 | Objectives 4 and 5 in [BC-001] |
| S02 | CN-004, CN-005 | Objectives 2 and 6 in [BC-001] |
| S03 | CN-006, CN-007 | Objective 7 and the runtime dependency criterion in [BC-001] |

## Sign-Off

Accepted by `AI as stand-in for S01`, after a Go review (RC-002).

---

[BC-001]: ./business-case.md
[b344b6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/commit/b344b6e2cba397e23714c73a45ad4155bb1e00e0
