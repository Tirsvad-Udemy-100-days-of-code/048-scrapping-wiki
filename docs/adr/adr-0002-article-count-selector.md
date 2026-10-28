# ADR-0002 Article count selector

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [ADR-0001], [MIL-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version; accepted after a Go review (RC-011) | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The lecture finds the article count with the CSS selector `#articlecount a`. The end to end run in Docker on 2026-10-28 showed that the Wikipedia main page now has two list items in the `articlecount` div: the first link is the number of active editors (269,023), the second list item holds the article count (7,256,081). `find_element` returns the first match, so the lecture selector now prints the active editors, not the articles. [BC-001] lists this as a risk and says the selector lives in `constants.py`.

Options:

1. Keep the lecture selector `#articlecount a` in the program and document that it prints the active editors.
2. Use a selector for the article link, `#articlecount li:nth-of-type(2) a`, in the program, and keep the lecture selector as a constant that the lecture step scripts and screenshots show.
3. Use `find_elements` and pick by text.

Forces: the program is named for the article count (S02, S01 concern CN-001); S02 compares code with the lecture; the end to end run is the check that notices a page change.

## Decision

The program uses `ARTICLE_COUNT_SELECTOR = "#articlecount li:nth-of-type(2) a"` and `constants.py` also keeps `LECTURE_SELECTOR = "#articlecount a"`, which the lecture step scripts show. The end to end test asserts the printed number is at least one million, so the active editors count cannot pass for the article count.

## Consequences

**Positive:**

- The program prints the article count again and the lecture's selector stays visible for comparison.
- The wiki can teach that a page changes and a selector must be checked against the page.
- The end to end test notices the same defect next time.

**Negative:**

- The program differs from the lecture code in one string.
- The selector depends on the order of the list items and breaks if Wikipedia reorders them.
- The one-million threshold must be revisited if the count ever falls below it (very unlikely).

## Affected Artifacts

- [BC-001] — risk 1 materialised; the mitigation (selector in `constants.py`, end to end run as the check) worked
- [ADR-0001] — the flat layout is unchanged; `constants.py` gains one constant
- [MIL-003] — the screenshots of steps 5 to 7 show both selectors

---

[BC-001]: ../business-case.md
[ADR-0001]: ./adr-0001-flat-package-layout.md
[MIL-003]: ../milestones/mil-003-screenshots-in-docker.md
