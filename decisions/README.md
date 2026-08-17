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

All eight are **Accepted**. Each record carries its own status, date, and reopening conditions; this index is navigation only and does not restate them.
