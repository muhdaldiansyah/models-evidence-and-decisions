# Decision Records

Settled decisions and the conditions under which they may be reopened. A decision record explains *why* a choice exists, not just what it is; architectural change goes through a record here, never through silent edits to governed files.

Authority runs `README.md → decisions/ → canon/ → chapter spec.md → working files` (see [CLAUDE.md](../CLAUDE.md)).

## Book-level

| # | Decision | Settles |
|---:|---|---|
| [0001](0001-book-architecture-freeze.md) | Book Architecture Freeze | 5 parts, 17 chapters in README order; formulation before inference; measurement distinct from provenance; target before identification. Carries the reopening conditions for the architecture. |
| [0002](0002-repository-architecture.md) | Repository Architecture | Manuscript-centric layout with a thin global knowledge layer; one authoritative home per fact type; no new top-level systems without demonstrated need. |
| [0003](0003-citation-and-source-note-system.md) | Citation and Source-Note System | One global `references.bib`; `authoryearkeyword` keys; Pandoc `[@key, locator]` syntax; one `sources/<key>.md` note per source; no standalone claim database. |

## Chapter 1

| # | Decision | Settles |
|---:|---|---|
| [0004](0004-chapter1-primary-anchor-case.md) | Primary Anchor Case | A synthetic municipal water-supply shortage during a heatwave is the worked anchor; the former hospital-pharmacy case is retired with no recurrence obligation. |
| [0005](0005-chapter1-cold-transfer-forms.md) | Cold-Transfer Forms | Two parallel unfamiliar-domain forms — A (refrigerated warehouse cooling risk, physical) and B (emergency temporary-housing allocation, institutional) — for exit production and delayed retest. |
| [0006](0006-chapter1-decision-framing-boundary.md) | Decision-Framing Boundary | Decision framing at practical depth without formal decision analysis. |
| [0007](0007-chapter1-dynamics-and-response-boundary.md) | Dynamics and Response Boundary | A dynamic-and-responsive-environment screen at introductory depth, short of system dynamics, control, and game theory. |
| [0008](0008-chapter1-pedagogical-scaffold.md) | Pedagogical Scaffold | The authoring sequence from initial attempt through delayed retest, registered as a book-specific pedagogical synthesis rather than a universal instructional algorithm. |

## Chapters 2–4 — proposed, not yet adjudicated

| # | Decision | Settles |
|---:|---|---|
| [0009](0009-chapter2-representation-terminology-and-boundary.md) | Chapter 2 Representation Terminology and Boundary | Purpose-relative representation; `mechanism` phenomenon-indexed and hedged; abstraction as omission versus idealization as asserted falsehood; representational aggregation demonstrated rather than cited; `state` as what must be carried forward. **PROPOSED.** |
| [0010](0010-chapter3-measurement-terminology-and-boundary.md) | Chapter 3 Measurement Terminology and Boundary | The `construct → working definition → measure → score` ladder; validity as a property of an interpretation for a use, never of an instrument; the accuracy/trueness/precision separation; the Chapter 3 / Chapter 4 line. **PROPOSED.** |
| [0011](0011-chapter4-observation-process-terminology-and-boundary.md) | Chapter 4 Observation-Process Terminology and Boundary | The dataset as the output of two processes; the five-stage enumeration as the book's own device; more records do not fix a selection problem; missingness as a question rather than a taxonomy; absence as the invisible case; the Chapter 4 / Chapter 15 line. **PROPOSED.** |

Records 0001–0008 are **Accepted**. Records 0009, 0010, and 0011 are **PROPOSED and not author-adjudicated**; the chapter specifications, terminology entries, and manuscripts built on them inherit that status.

Each record carries its own status, date, and reopening conditions; this index is navigation only and does not restate them.
