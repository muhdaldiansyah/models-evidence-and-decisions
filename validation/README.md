# Validation

Status: **provisional.** Built on [Decision 0025](../decisions/0025-validation-architecture.md), which is **PROPOSED and not author-adjudicated**.

This directory holds the validation apparatus for the whole book. The manuscript is drafted; **nothing in it has been validated**, and this directory exists to make that condition workable rather than to soften it.

## What is here

| File | What it is | Who uses it |
|---|---|---|
| [gate-status.md](gate-status.md) | one row per chapter — **the single place a gate's status is true** | author |
| [pilot-protocol.md](pilot-protocol.md) | how a reader session is run, parameterised by chapter | facilitator |
| [pilot-data-capture.md](pilot-data-capture.md) | what gets written down, and in what form | facilitator |
| [sme-review-water-anchor.md](sme-review-water-anchor.md) | the cumulative water-anchor packet, Chapters 1–15 and 17 | water-utility reviewer |
| [sme-review-unfamiliar-cases.md](sme-review-unfamiliar-cases.md) | Chapter 16's two problems and Chapter 17's Case 2 | housing and fundraising reviewers |

Each chapter also has its own `freeze-gates.md`, which describes that chapter's seven gates and what is specific about them. **It does not assert status.** Status lives in `gate-status.md` and nowhere else.

## Chapter 1's files are the originals

`../chapters/01-decisions-questions/` holds `sme-review-water-anchor.md`, `pilot-protocol.md`, `pilot-data-capture.md`, and `validation-handoff.md`, written while Chapter 1 was being drafted. They are **not superseded and not moved**. The book-level files here generalise from them, cite them, and are the ones to use for any chapter other than Chapter 1.

Where the two disagree about Chapter 1, **Chapter 1's own copies win**, because `../decisions/0008` and Chapter 1's gates are written against them.

## The order things happen in

```text
SME review            ─┐
                       ├─→  pilot adjudication  →  manuscript sync  →  chapter audit  →  freeze
timed reader + retest ─┘
```

Gates 1 and 2–3 are independent of each other and can run in either order or at once. Gates 4–7 are strictly sequential and each is blocked by the one before.

**Gates are evidence conditions.** A gate closes when evidence exists and has been adjudicated. Doing the work does not close a gate; being unable to find a reviewer does not close one either.

## Two facts that shape everything here

**A full-book pilot is about 126 hours per reader** — 100 learning hours across 503 pages, plus 26.2 hours of cold-transfer production once the delayed parallel-form retest is counted. That is not recruitable, so **the pilot samples four chapters**: 1, 8, 12, and 16. The reasons are in [Decision 0025](../decisions/0025-validation-architecture.md) clause 3. The other thirteen are marked `NOT SAMPLED` rather than `OPEN`, so that *no evidence yet* stays distinguishable from *not scheduled for evidence*.

**The book changes its own assessment instrument at Chapter 12.** Chapters 1–11 score rubric dimensions 0–2; Chapters 12–17 supply an unscored review instrument that explicitly records nothing. No decision proposes the change. `pilot-protocol.md` therefore has two capture modes and `gate-status.md` records which mode a chapter is in. The question of whether the book means to have two instruments is [Decision 0025](../decisions/0025-validation-architecture.md) clause 4, and it is open.

## What passing all of this would and would not establish

It would establish that the cases are operationally plausible, that the budgets are approximately right, that the exercises can be completed as designed, and that readers do not systematically misread the material.

It would **not** establish that the book produces durable far transfer. `../chapters/17-deployment-monitoring/chapter.md` §8 says so to the reader on the book's last page, and nothing in this directory changes that.
