# Chapter 8 Freeze Gates

Status: **live validation tracker.** Built on [Decision 0025](../../decisions/0025-validation-architecture.md), **PROPOSED and not author-adjudicated**.

**This file describes this chapter's gates. It does not assert their status.** Status is held in [`../../validation/gate-status.md`](../../validation/gate-status.md), and if the two ever disagree that file is right.

## Authored state

| | |
|---|---|
| Chapter | **Estimation, Uncertainty, and Model Checking** |
| Manuscript | complete — 8 sections, 13,944 words |
| Budget | 40 pages / 8 learning hours |
| Self-explanation pauses | 3 |
| Planted-defect diagnosis task | yes — 5 defects |
| Parallel cold-transfer forms | A and B, 50 minutes |
| Rubric mode | **S — scored dimensions (0/1/2)** |
| Terminology block | provisional, pending [Decision 0015](../../decisions/0015-chapter8-estimation-terminology-and-notation.md) |
| Pilot sample | **SAMPLED** |

The chapter is **authored**, not validated. No reviewer and no reader has seen it.

## What is specific about this chapter

**The largest chapter in the book — 40 pages, 8 learning hours — and one of the four sampled.** If the page-and-hour budget is wrong anywhere it is wrong here first, which is why it is in the sample. The chapter also quotes a source that cannot be quoted with comparison symbols, so any wording change from review must preserve that constraint.

**This chapter inherits Chapter 1's open Gate 1**, and its `case-data.md` publication gate records the accumulation. It cannot be more validated than the case it extends.

## Gate 1 — subject-matter review

**Evidence needed.** A domain reviewer has read this chapter's `case-data.md` and answered the questions in its publication gate, with a disposition of `PASS`, `PASS WITH WORDING CHANGES`, or `REVISE MECHANISM`.

**Packet.** [`../../validation/sme-review-water-anchor.md`](../../validation/sme-review-water-anchor.md)

**Closes when** the author has adjudicated every material comment, accepted changes are synchronised through `case-data.md` and the manuscript, and unresolved concerns are either repaired or recorded as blocking.

## Gates 2 and 3 — timed reader, and delayed parallel-form retest

**Status in the sample: OPEN.**

**Evidence needed.** A session run under [`../../validation/pilot-protocol.md`](../../validation/pilot-protocol.md), captured with [`../../validation/pilot-data-capture.md`](../../validation/pilot-data-capture.md), against a recorded commit hash: timing per section, the preserved opening attempt, all three pauses, the five-defect diagnosis before feedback, one cold-transfer form produced without the rubric visible, rubric observations in **mode S**, retrieval from memory, and a debrief. Then the other form at 7–14 days, unseen until then.

**Neither gate requires a validated total score.** The scored rubric states that there is no validated aggregate cut score, and the pilot may not manufacture one.

## Gates 4 to 7 — adjudication, synchronisation, audit, freeze

**Status: BLOCKED BY GATES 1 AND 2–3.**

4. **Pilot adjudication.** Per material finding: observed evidence, interpretation, author decision, scope of change, follow-up evidence needed.
5. **Manuscript synchronisation.** Accepted SME wording and pilot-driven changes applied; governed case facts and reader-facing prose kept consistent; transfer links, rubric concealment, and delayed-form concealment reverified.
6. **Chapter audit.** The 40-page / 8-hour architecture holds unless evidence justifies reopening it; all 8 sections still serve their governed jobs; central question and core competence intact; reveal order coherent; citation keys resolve and source-note cautions are respected; no exercise exposes an answer, rubric, or parallel form before production.
7. **Freeze decision.** `FREEZE` · `FREEZE WITH DEFERRED NON-BLOCKING ITEMS` · `REVISE AND RE-PILOT` · `REOPEN GOVERNED DECISION`.

**Gate 7 additionally requires that [Decision 0015](../../decisions/0015-chapter8-estimation-terminology-and-notation.md) has been adjudicated.** This chapter's terminology and scope are provisional until it is, and a chapter cannot freeze on a provisional boundary.

## Next evidence needed

A returned SME review, or a pilot participant. This chapter is in the four-chapter sample, so both are in scope.

Without external evidence, further tuning of this chapter would be speculative rather than evidence-driven.
