# RC-010 Code review of MIL-002 (src and tests)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Claude (AI) | AI as stand-in for S01 | Initial version: Go | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case functions, variables and modules; UPPER_SNAKE constants. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | create_driver, open_main_page, read_article_count state their purpose; no abbreviations or one-letter names. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff format and ruff check (E, F, I, B, UP) are clean; no noqa suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function, test and fake is annotated, including -> None; mypy --strict is clean. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No except clause; main uses try/finally so the driver is always quit; errors propagate (tested). |
| 6 | No mutable default arguments and no shadowed builtins | Pass | The only default is the immutable `headless: bool = False`; no builtins are shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | The browser is closed with try/finally and driver.quit(); kept close to the lecture instead of a with block (judgement). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Modules and all public functions have Doxygen @brief/@param/@return; doxygen Doxyfile builds with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | print is the program's console output, which the lecture asks for, not logging; no secrets are handled (judgement). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No classes and no Design Class Diagram; the test fakes are not production classes (judgement; passes by absence). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 9 unit tests named for behaviour with a fake driver; no browser, network or order dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict is clean; the six type: ignore comments mark fakes standing in for WebDriver; no Any. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | selenium>=4.20 is the only runtime dependency, dev tools are pytest, ruff, mypy; lower bounds rather than exact pins. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | URL, selector, Chrome options and env names are defined once in constants.py; tests import them. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | interaction imports constants and selenium; constants imports nothing; no cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each module and function has one reason to change; no type tests. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Flat package by decision: ADR-0001 records why no layer packages exist; tests/unit now, tests/e2e in MIL-003. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English, snake_case, no spaces. |

## Overall Verdict

Go — Every Mandatory criterion of the checklist passes; no Fail. Stand-in review as `AI as stand-in for S01`, not independent: S01 can challenge it in the end-of-run summary. Verified: pytest 9 passed, ruff, mypy strict and doxygen clean.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[MIL-002]: ../../milestones/mil-002-interaction-script.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
