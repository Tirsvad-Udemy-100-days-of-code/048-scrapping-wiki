# ADR-0001 Flat package layout

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [MIL-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review (RC-009) | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The Python checklist `QC-PY-001` (criterion 17) expects the layers `domain`, `application`, `infrastructure` and `presentation` under `src/`. The `clean-architecture` skill says a small project may merge `Infrastructure` and `Presentation`, never `Domain`, and that a layer with nothing in it yet is created only when its first file is.

This project is one lecture exercise: about 30 lines that start a Chrome driver, open a page, read one element and print it. It has no business rule, no entity, no storage and no second use case. The stakeholders ask for readable code with the assignment's names (S02, CN-004), and the lecture itself names one file, `interaction.py`.

Options:

1. Full four-layer layout (`domain`, `application`, `infrastructure`, `presentation`) with a port for the driver.
2. A flat package `scraping_wiki` with `constants.py` and `interaction.py`; the Selenium adapter and the console entry point stay together in `interaction.py`.

Forces: readability for S02 and S03, the lecture's file names, the amount of code, and the framework's wish for layers that point inward.

## Decision

Use a flat package `src/scraping_wiki/` with `constants.py` and `interaction.py`, and create no `domain`, `application`, `infrastructure` or `presentation` package until the project has code that belongs in one. `interaction.py` holds the Selenium adapter and the console entry point (the merged infrastructure and presentation layers); there is no domain code.

## Consequences

**Positive:**

- The code matches the lecture and the assignment's names, so S02 can compare it line by line.
- No empty packages and no ports that add indirection without a second implementation.
- Tests use a fake driver without a port, because the functions take a `WebDriver`.

**Negative:**

- Criterion 17 of `QC-PY-001` is met only through this ADR, not by the folder structure.
- Later lectures (clicking links, typing into fields) may need the layers; the structure then has to be refactored and this ADR superseded.
- Selenium types appear in the same module as the console entry point.

## Affected Artifacts

- [BC-001] — keeps the single runtime dependency and the lecture-sized scope
- [MIL-002] — the deliverable `interaction.py` and `constants.py` follow this layout

---

[BC-001]: ../business-case.md
[MIL-002]: ../milestones/mil-002-interaction-script.md
