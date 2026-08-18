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

## Chapters 2–10 — proposed, not yet adjudicated

| # | Decision | Settles |
|---:|---|---|
| [0009](0009-chapter2-representation-terminology-and-boundary.md) | Chapter 2 Representation Terminology and Boundary | Purpose-relative representation; `mechanism` phenomenon-indexed and hedged; abstraction as omission versus idealization as asserted falsehood; representational aggregation demonstrated rather than cited; `state` as what must be carried forward. **PROPOSED.** |
| [0010](0010-chapter3-measurement-terminology-and-boundary.md) | Chapter 3 Measurement Terminology and Boundary | The `construct → working definition → measure → score` ladder; validity as a property of an interpretation for a use, never of an instrument; the accuracy/trueness/precision separation; the Chapter 3 / Chapter 4 line. **PROPOSED.** |
| [0011](0011-chapter4-observation-process-terminology-and-boundary.md) | Chapter 4 Observation-Process Terminology and Boundary | The dataset as the output of two processes; the five-stage enumeration as the book's own device; more records do not fix a selection problem; missingness as a question rather than a taxonomy; absence as the invisible case; the Chapter 4 / Chapter 15 line. **PROPOSED.** |
| [0012](0012-chapter5-criticism-terminology-and-boundary.md) | Chapter 5 Criticism Terminology and Boundary | Adequacy for a use, accuracy, and quantity; how much criticism is enough is governed by what happens if you are wrong; verification versus validation, reopening Chapter 3's declined word; strong inference plus a fourth step that is the book's own; four cheap checks taught by demonstration; the Chapter 5 / Chapter 8 line. **PROPOSED.** |
| [0013](0013-chapter6-probability-terminology-and-notation.md) | Chapter 6 Probability Terminology and Notation | A probability as conditional on stated information rather than a property of an event; the frequency/degree-of-belief argument named and not adjudicated; **a bounded notation exception** — the conditioning bar and odds, and nothing else — announced to the reader, breaking a five-chapter policy; `calibration` reopened for the forecast sense Chapter 3 declined; calibration as constraint and sharpness as objective; expectation stopped short of decision rules; the Chapter 6 / Chapter 7 and Chapter 11 lines. **PROPOSED.** |
| [0014](0014-chapter7-identification-terminology-and-notation.md) | Chapter 7 Identification Terminology and Notation | The four-step spine taken from the source rather than invented; target quantity before design; identification defined compatibly from two traditions and taught as relative to assumptions; **a second bounded notation exception** — `do(·)` inside the conditioning bar and inline arrows — extending Decision 0013's; exchangeability, positivity, and consistency with the source's own "heroic"; `consistency` reopened against the estimator sense Chapter 8 needs; what randomization buys and does not; not-identified as a reportable result; the Chapter 7 / Chapter 8 line in the source's own terms. **PROPOSED.** |
| [0015](0015-chapter8-estimation-terminology-and-notation.md) | Chapter 8 Estimation Terminology and Notation | Eight named topics reorganised as consequences of one sourced claim — that a computed number tests an entire model, including how the analysis was conducted; **the notation exception declined**, departing from a promise Chapter 6 made to the reader; `estimator` and `estimate` closed from TODO with their properties held to the procedure; `consistency` reopened against Chapter 7's causal sense; `confidence` declined in the book's own prose in favour of `interval estimate`; analytic flexibility placed inside the model rather than beside it; the threshold dichotomy taught as a hazard with the discipline's own six principles. **PROPOSED.** |
| [0016](0016-chapter9-synthesis-terminology-and-boundary.md) | Chapter 9 Synthesis Terminology and Boundary | Synthesis and transport treated as one question, with the same-question check ordered before any weighting; **no synthesis method taught**, on the strength of the governed core competence's "at an appropriate conceptual level"; `external validity` registered as a hazard and `transportability` preferred; support factors as what decides whether a result carries; `target population` closed from its Chapter 1 stub; **clause 6 records a fourth instance of the demonstrate-because-unsourced disposition and refers it to the author rather than invoking precedent.** **PROPOSED.** |
| [0017](0017-chapter10-values-terminology-and-boundary.md) | Chapter 10 Values Terminology and Boundary | Values before objectives before alternatives, with an option set treated as an unstated claim about what matters; the two-part objective test and the why-is-this-important test; stakeholders as those affected rather than those consulted; constraints sorted by who set them; alternatives derived rather than brainstormed; `objective` and `metric` closed from TODO. **Clause 1 records that `keeney1996valuefocused` could not be obtained in full and that the framework is used as reported at `bradley2016structured`, honouring a prohibition standing since Chapter 1.** **Clause 5 resolves a conflict between Decision 0006 and README.md over where trade-offs live.** **PROPOSED.** |

Records 0001–0008 are **Accepted**. Records 0009–0017 are **PROPOSED and not author-adjudicated**; the chapter specifications, terminology entries, and manuscripts built on them inherit that status.

**The notation question now spans three records and must be adjudicated in order.** 0013 clause 2 opens a bounded exception to a policy the book held from Chapter 1 through Chapter 5; 0014 clause 2 extends it; 0015 clause 2 **declines** to extend further and thereby departs from a promise Chapter 6 made to the reader in its own text. Ruling on any of them without the earlier ones would be incoherent.

All three are announced to readers in their manuscripts, which means a refusal is not a silent edit: Chapter 6 §§2–4, Chapter 7 §3, and Chapter 8 §1 each contain prose that would have to be rewritten rather than adjusted.

**0015 clause 2 is the unusual one.** It is the only clause in the set that keeps a chapter's material while refusing its symbols, and it is the only one that resolves a commitment made in already-drafted prose rather than proposing something new.

**One cross-cutting item.** Decisions 0009 (clause 6.3), 0011 (clause 4.4), and 0012 (clause 4.2) each adopt the same disposition: teach a practice by demonstration because no source was obtained for it. `chapters/05-assumptions-rival-models/research-03-cheap-checks.md` §2 records this as a pattern rather than three coincidences and recommends treating it as a standing book-level question. If a fifth chapter reaches for the disposition, research should be reopened rather than precedent invoked.

Chapter 6 teaches conditioning, the odds update, expectation, and Monte Carlo mechanics by demonstration, and is **not** an instance. `chapters/06-probability-simulation/research-04-simulation-examples-exercises.md` §1 states the distinction rather than assuming it: mathematics is legitimately taught by working it, whereas the pattern on notice is a *practice* taught by demonstration because a source proved hard to obtain. The count therefore stands at three for Chapter 6.

**Chapter 9 is the fourth instance, and it is the one the standing instruction was written for.** [Decision 0016](0016-chapter9-synthesis-terminology-and-boundary.md) clause 6 teaches that agreement among dependent evidence sources is cheap, with no source behind it, and the manuscript says so in its own text rather than only in the dossier. Clause 6.4 keeps the treatment to about one page **pending author adjudication of whether book-level research should now be reopened**, and exists to make that decision unavoidable rather than to pre-empt it.

**A second cross-cutting item, opened by 0017.** Clause 5 of that record resolves a conflict between [0006](0006-chapter1-decision-framing-boundary.md) — which assigns "trade-off structure" to Chapter 10 — and `../README.md`, which assigns trade-offs and value of information to Chapter 11. The resolution follows the authority order in `../CLAUDE.md` and favours `README.md`. **If the author accepts it, 0006's wording needs amending to match; that amendment has not been made**, and until it is, two accepted-or-proposed records disagree in writing.

Each record carries its own status, date, and reopening conditions; this index is navigation only and does not restate them.
