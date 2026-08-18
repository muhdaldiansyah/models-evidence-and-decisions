# Decision 0025: Validation Architecture

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

The first record written after the drafting phase closed, and the first that is not about a chapter.

Written in the form of a decision because it proposes a new top-level directory, which `0002` reserves for demonstrated need and `../README.md`'s Governance section reserves for a decision record. `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`validation/` and the sixteen new `freeze-gates.md` trackers are built on this record and inherit its provisional status.

**Clause 4 records a discontinuity in the book's own instruments that was not decided anywhere.** It is referred to the author rather than resolved here.

## Context

`../README.md` states that the drafting phase is complete and validation has not begun. That was accurate and it understated the problem.

Before this record, the validation apparatus consisted of five files, all in `../chapters/01-decisions-questions/`: `freeze-gates.md`, `sme-review-water-anchor.md`, `pilot-protocol.md`, `pilot-data-capture.md`, and `validation-handoff.md`. **Sixteen chapters had nothing.** A willing SME or pilot reader arriving today could have worked on Chapter 1 and on no other chapter in the book.

Two further facts were established while writing this record and are load-bearing for it.

**A full-book pilot is 126 hours per reader.** 100 learning hours of manuscript across 503 pages, plus 13.1 hours of cold-transfer production, doubled to 26.2 by the delayed parallel-form retest every chapter specifies. That is roughly three weeks of full-time work for one participant, before any facilitation, and it is not a design that can be recruited for.

**The book changes its own assessment instrument at Chapter 12** and no record says so. See clause 4.

## Decision

### 1. A `validation/` directory, and what goes in it

**1.1** Validation material that is **the same for every chapter** lives once, in `../validation/`. Validation material that is **specific to one chapter** lives in that chapter's directory.

**1.2** Book-level, in `../validation/`:

| File | What it is |
|---|---|
| `README.md` | the architecture, and the order things happen in |
| `gate-status.md` | one row per chapter; **the single place a gate's status is true** |
| `pilot-protocol.md` | one protocol, parameterised by chapter |
| `pilot-data-capture.md` | one capture template, parameterised by chapter |
| `sme-review-water-anchor.md` | the cumulative anchor packet, Chapters 1–15 and 17 |
| `sme-review-unfamiliar-cases.md` | Chapter 16's two problems and Chapter 17's Case 2 |

**1.3** Chapter-level: `freeze-gates.md`, one per chapter, seventeen in total. It records that chapter's authored state, what evidence each gate needs, and what is chapter-specific about it.

**1.4** **Chapter 1's five files are not moved.** They are the worked instance the book-level files generalise from, they are referenced by `../decisions/0008` and by Chapter 1's own gates, and moving them would break links for no gain. `../validation/README.md` records that Chapter 1's copies are the originals.

### 2. Why the SME packets are book-level and cumulative

**2.1** The anchor appears in sixteen chapters. **Sixteen per-chapter SME packets would ask one reviewer to read the same operating story sixteen times** to reach the part that is new.

**2.2** The material for a cumulative packet already existed and was not consolidated: **each chapter's `case-data.md` ends with a publication gate naming exactly what its own extension needs reviewed.** Twelve were written during drafting; the convention lapsed after Chapter 12 and the five missing ones were written before this record.

**2.3** `../validation/sme-review-water-anchor.md` is therefore an assembly, not new authorship. It carries Chapter 1's frozen facts once, then one section per chapter stating **what that chapter adds and what the reviewer is being asked about it.**

**2.4** **Two reviewer domains, not one.** Chapter 15 needs a regulatory or price-control reviewer in addition to the water reviewer, and Chapter 16 needs a social-housing reviewer and a fundraising reviewer for cases that are not the anchor at all. Chapter 17 inherits both.

### 3. The pilot is sampled, not exhaustive

**3.1** 126 hours per reader makes a whole-book pilot undesignable. **The pilot samples four chapters**, chosen so that a failure in any of them would be a failure of something the whole book relies on:

| Chapter | Why this one |
|---|---|
| **1** | the entry point, the only chapter with prepared materials, and the source of the preserved artifact Chapter 16 compares against |
| **8** | the largest chapter in the book at 40 pages and 8 hours; if the page-and-hour budget is wrong anywhere it is wrong here first |
| **12** | where the assessment instrument changes; a failure here is a failure across six chapters |
| **16** | the only chapter that tests routing across the whole book, and the only one whose exit task depends on an artifact preserved fifteen chapters earlier |

**3.2** That is 126 pages and roughly 25 learning hours plus about 3.5 hours of transfer production — **about 30 hours per reader**, which is recruitable.

**3.3** **The other thirteen chapters get their gates opened and left open.** `gate-status.md` records them as `NOT SAMPLED` rather than `OPEN`, so that the difference between *no evidence yet* and *not scheduled for evidence* stays visible.

**3.4** Sampling is a design choice, and it is the kind of bounded coverage `../decisions/0002` says must be stated rather than implied. **If the four sampled chapters pass, that is evidence about four chapters.**

### 4. The rubric instrument changes at Chapter 12, and no record says so

**4.1** Chapters 1–11 supply a **scored** rubric: dimensions marked 0, 1, 2, with the standing caution that there is no validated aggregate cut score.

**4.2** Chapters 12–17 supply an **unscored review instrument**: "This is a review instrument, not a mark scheme. Nothing here is scored and nothing is recorded."

**4.3** **No decision record proposes this change, and Chapter 12's own `spec.md` still carries a seven-item "Rubric dimensions" section** as though the dimensions were to be scored. The change happened in the artifacts and not in the governance.

**4.4** It may well be right. `../decisions/0023` clause 5 gives a strong argument for the unscored direction — that scoring an artifact retrospectively changes what it was preserved for — and that argument was made about Chapter 1's baseline comparison, not about rubrics generally.

**4.5** **The consequence for validation is concrete.** Chapter 1's Gate 2 requires "eight rubric dimensions recorded after production." For Chapters 12–17 there are no dimensions to record, by design. `pilot-protocol.md` therefore specifies **two capture modes**, and `gate-status.md` records which mode each chapter is in.

**4.6** **This is referred to the author.** Either the book has one assessment instrument or it deliberately has two, and whichever is true should be written down. This record does not choose.

### 5. What a gate is, and what closes it

**5.1** The seven-gate sequence in `../chapters/01-decisions-questions/freeze-gates.md` is adopted for every chapter unchanged: SME → timed reader → delayed retest → pilot adjudication → manuscript synchronisation → chapter audit → freeze.

**5.2** **Gates are evidence conditions, not tasks.** A gate closes when evidence exists and has been adjudicated, never because work was done.

**5.3** **No chapter's gate can close ahead of the evidence it inherits.** Chapters 2–15 and 17 inherit Chapter 1's Gate 1; their case-data files already say so. A chapter cannot be more validated than the case it extends.

**5.4** `gate-status.md` is the single authority for gate status. A chapter's `freeze-gates.md` describes its gates; it does not independently assert that one is closed.

### 6. What this record does not do

- Schedule anything, or claim any reviewer or reader has been approached.
- Assert that any gate has closed. **All 119 gates in the book are open or not sampled.**
- Change any chapter's content, budget, exercises, or governed fields.
- Create a build system, a CI configuration, or an exercise bank.
- Resolve the rubric discontinuity — clause 4.
- Resolve the Chapter 1 core-competence divergence, the two orphaned routings, or any of the sixteen open chapter records.
- Claim that passing these gates would establish that the book teaches transfer. `../chapters/17-deployment-monitoring/chapter.md` §8 states the book's position on that and this record does not soften it.

## Known gaps carried forward

1. **No reviewer and no reader has been approached**, for any chapter, at any point.
2. **The four-chapter sample is an author judgment**, not a power calculation, and no power calculation is possible without pilot variance.
3. **The rubric discontinuity is unresolved** — clause 4.
4. **Chapter 16's and 17's non-water cases need two reviewer domains this project has no route to**, and no route has been attempted.
5. **The 126-hour figure assumes the stated budgets are right**, which is one of the things a pilot exists to test.

## Reopen if

- A pilot wave produces evidence that the four-chapter sample missed something structural.
- The author resolves clause 4 in a way that changes what Gate 2 must capture.
- The validation apparatus obstructs revision rather than supporting it, which is `../decisions/0002`'s standing test for any structure in this repository.

## No architecture change to the book

This record proposes no change to `../README.md`'s parts, chapters, sequence, or governed fields. It adds a directory and a per-chapter tracker, and it does not touch the manuscript.
