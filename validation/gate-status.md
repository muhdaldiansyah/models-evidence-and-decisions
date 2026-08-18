# Gate Status

Status: **provisional.** Built on [Decision 0025](../decisions/0025-validation-architecture.md), **PROPOSED and not author-adjudicated**.

**This file is the single authority for gate status.** A chapter's `freeze-gates.md` describes its gates; it does not assert whether one is closed. If the two ever disagree, this file is right.

Last reviewed 2026-08-18.

## Summary

**119 gates. None closed.** Seventeen chapters times seven gates, and no reviewer or reader has been approached for any of them at any point.

| | count |
|---|---:|
| gates closed | **0** |
| gates open — evidence actively sought | 25 |
| gates blocked behind an open gate | 16 |
| gates not sampled — evidence not scheduled | 78 |
| chapters with any prepared reviewer material | 17 (as of Decision 0025) |
| chapters with returned evidence | **0** |

## Per chapter

`Gate 1` is SME review. `Gates 2–3` are the timed reader session and the delayed parallel-form retest. `Gates 4–7` — pilot adjudication, manuscript synchronisation, chapter audit, freeze — are strictly sequential and blocked behind them.

| Ch | Chapter | pp / h | transfer | rubric | Gate 1 | Gates 2–3 | Gates 4–7 | pilot |
|---:|---|---|---|---|---|---|---|---|
| 1 | [Decisions, Questions, and a First Comp](../chapters/01-decisions-questions/freeze-gates.md) | 24 / 4 | 30–40 min | scored | OPEN | OPEN | BLOCKED | SAMPLED |
| 2 | [Representation, Mechanisms, and Scale](../chapters/02-representation-mechanisms/freeze-gates.md) | 29 / 6 | 40 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 3 | [Measurement and Operationalization](../chapters/03-measurement-operationalization/freeze-gates.md) | 26 / 5 | 40 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 4 | [Observation Processes and Data Provena](../chapters/04-observation-provenance/freeze-gates.md) | 28 / 5 | 40 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 5 | [Assumptions, Adequacy, and Rival Model](../chapters/05-assumptions-rival-models/freeze-gates.md) | 27 / 5 | 40 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 6 | [Probability, Prediction, and Simulatio](../chapters/06-probability-simulation/freeze-gates.md) | 34 / 7 | 45 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 7 | [Targets, Identification, and Causal Cl](../chapters/07-targets-identification/freeze-gates.md) | 38 / 8 | 50 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 8 | [Estimation, Uncertainty, and Model Che](../chapters/08-estimation-uncertainty/freeze-gates.md) | 40 / 8 | 50 min | scored | OPEN | OPEN | BLOCKED | SAMPLED |
| 9 | [Combining and Transporting Evidence](../chapters/09-evidence-synthesis/freeze-gates.md) | 28 / 5 | 45 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 10 | [Values, Objectives, and Alternatives](../chapters/10-values-alternatives/freeze-gates.md) | 30 / 5 | 45 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 11 | [Decisions Under Uncertainty and Value ](../chapters/11-decisions-voi/freeze-gates.md) | 33 / 7 | 50 min | scored | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 12 | [Optimization, Robustness, and Adaptive](../chapters/12-optimization-robustness/freeze-gates.md) | 36 / 7 | 50 min | **unscored** | OPEN | OPEN | BLOCKED | SAMPLED |
| 13 | [Dynamics, Feedback, and Stability](../chapters/13-dynamics-feedback/freeze-gates.md) | 28 / 5 | 45 min | **unscored** | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 14 | [Sequential Decisions, Information, and](../chapters/14-sequential-control/freeze-gates.md) | 28 / 6 | 50 min | **unscored** | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 15 | [Strategic Interaction, Incentives, and](../chapters/15-strategic-interaction/freeze-gates.md) | 30 / 6 | 50 min | **unscored** | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |
| 16 | [Integration: The Full Loop on Unfamili](../chapters/16-integration-full-loop/freeze-gates.md) | 26 / 6 | 60 min | **unscored** | OPEN (own) | OPEN | BLOCKED | SAMPLED |
| 17 | [Deployment, Monitoring, and Revision](../chapters/17-deployment-monitoring/freeze-gates.md) | 18 / 5 | 50 min | **unscored** | OPEN | NOT SAMPLED | NOT SAMPLED | NOT SAMPLED |

**Gate 1 reviewer domains.** Chapters 1–15 and 17 (Case 1) share one water-utility reviewer through [sme-review-water-anchor.md](sme-review-water-anchor.md); Chapter 15 additionally needs a regulatory reviewer; Chapter 16 and Chapter 17 (Case 2) need housing and fundraising reviewers through [sme-review-unfamiliar-cases.md](sme-review-unfamiliar-cases.md).

**Inheritance.** Chapters 2–15 and 17 cannot close Gate 1 ahead of Chapter 1, because their cases extend Chapter 1's operating story. Each chapter's `case-data.md` records this in its own publication gate. **Chapter 16 is the only chapter that does not inherit it.**

## How to update this file

Change a cell only when evidence has been received **and** adjudicated, and record the adjudication in the chapter's own files in the same commit. Move the date at the top in that commit too.

Do not mark a gate closed because the material was prepared. Preparation is what Decision 0025 did; it closed nothing.
