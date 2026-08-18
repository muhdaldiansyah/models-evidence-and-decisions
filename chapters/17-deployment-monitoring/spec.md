---
chapter: 17
part: 5
title: "Deployment, Monitoring, and Revision"
status: drafted
pages_target: 18
hours_target: 5
---

# Chapter 17: Deployment, Monitoring, and Revision

**Provisional.** Built on proposed `../../decisions/0024-chapter17-deployment-terminology-and-boundary.md` and inheriting its status. **Three of that record's clauses need author attention**, and one of them concerns how the book ends.

## Central question

Is the deployed reasoning still working — and if not, which stage failed?

*Governed by `README.md`. Not amendable here.*

## Core competence

Design monitoring, distinguish signal from ordinary variation, recognize drift and tampering, diagnose failure by stage, define revision triggers, and return deliberately to earlier parts of the reasoning process.

*Governed by `README.md`. Not amendable here.*

**The Chapter 17 block also carries the only permissive clause in the book's architecture**: "Concept-level monitoring machinery may include common-cause versus special-cause variation and control-chart reasoning where appropriate." **The chapter takes the distinction and declines the technique**; `../../decisions/0024` clause 2 records the choice and the reason.

## Role in the book

**This is the last chapter.**

**Its unique job:**

> Teach readers that monitoring catches failures which show up in outputs and is constitutionally incapable of catching failures in what the thing was built to represent — and that knowing which is which is a diagnosis, made by stage, before anything has gone visibly wrong.

**Fourteen chapters defer here**, more than to any other chapter in the book, and two of those deferrals are requirements rather than topics: `canon/terminology.md` assigns the operation of Chapter 12's signposts here, and Chapter 16 hands over its own case by name.

**And the book ends here.** §8 is the book's final section.

## Hard prerequisites

All sixteen preceding chapters. Specifically: Chapter 8's habit about thresholds, Chapter 12's adaptive plan, Chapter 13's overshoot mechanism, Chapter 15's ratio finding, and Chapter 16's routing and backward revision.

## Soft dependencies / spiral links

- Chapter 1's `intended use`, of which `permissible use` is the deployment-time counterpart.
- Chapter 3's `validity`, Chapter 9's `transportability`, Chapter 14's `observability` — the relation-not-property shape, here for the fourth time.
- Chapter 5's model checking, which the canon already records as the same activity earlier.
- Chapter 6's calibration, reused as a monitoring instrument.

## Established concepts to cover

Deployment as a repeated act. Permissible use. Signal against ordinary variation, and the threshold that is a timer. Drift, and why detecting it is not diagnosing it. Tampering. Revision triggers, in two directions. Diagnosis by stage. Retirement.

## Terminology to introduce or stabilize

**Introduced:** `monitoring`, `ordinary variation`, `signal`, `drift`, `tampering`, `revision trigger`, `permissible use`, `retirement`.

**Six of the eight are the book's own or extend its own.**

**No collision requiring announcement** — the second chapter in a row with none.

**Two flags.** `ordinary variation` rests on a primary source that could not be obtained. **`tampering` is named in the governed core competence and has no source at all** — `../../decisions/0024` clause 6.

**And `utility` does not close.** It remains the registry's one `TODO`, assigned to the drafted Chapter 11, and **there is no later chapter to close it in.**

## Interfaces with other chapters

| Chapter | Interface |
|---|---|
| 1 | supplies `intended use`; `permissible use` is its deployment-time counterpart |
| 5 | supplies model checking, which the canon records as the same activity earlier |
| 6 | supplies calibration, reused as a standing instrument |
| 8 | supplies the habit this chapter applies to Chapter 12's thresholds |
| 12 | supplies the signposts this chapter operates and criticises |
| 13 | supplies the mechanism `tampering` names |
| 15 | supplies the unreported-ratio finding, which repeats here |
| 16 | routes forward from a problem; this chapter routes backward from a symptom |

## Scope boundary

### Core

Deployment as a repeated assessment against permissible use. Signal against ordinary variation, with the threshold-as-timer result. Drift, tampering, and revision triggers in two directions. Diagnosis by stage, and which stages monitoring cannot see. Retirement.

### Deferred to the depth curriculum

Control charts, control limits, run rules, chart types, sampling plans. Drift-detection methods: distribution-shift tests, change-point detection, CUSUM, sequential analysis. Governance and assurance frameworks. Reliability engineering, condition monitoring, maintenance scheduling. Machine-learning monitoring.

### Not deferred anywhere

**Nothing.** This is the last chapter, and what it does not cover is not covered.

## Section architecture

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | Eighteen Months Later | 2 | 0.50 |
| 2 | Deployment Is Not a State | 3 | 0.75 |
| 3 | Signal, or Ordinary Variation | 4 | 1.10 |
| 4 | A Trigger That Was a Timer | 3 | 0.85 |
| 5 | What Monitoring Cannot See | 3 | 0.85 |
| 6 | Diagnosis by Stage | 2 | 0.55 |
| 7 | Retirement | 1 | 0.20 |
| 8 | Cold-Start Practice, and What This Book Has Not Established | 1 | 0.20 |

Eight sections, 18 pages, 5 hours. Roughly 360 words per page — about **6,480 words**. **The shortest chapter in the book.**

Three self-explanation pauses: §3 (is seven a signal?), §4 (what should the committee have done?), §6 (where did it enter?).

## Examples / recurring cases

**Two cases, both inherited, frozen in `case-data.md`.**

**Case 1** operates Chapter 12's signposts for four years. **The water anchor's sixteenth and final appearance**, and the chapter says so.

**Case 2** monitors Chapter 16's repairs tool. No new fact about the tool; only the monitoring arrangements are new.

## Exercise architecture

Per `../../decisions/0008`. Opening task before vocabulary; three pauses; five-defect diagnosis; cold transfer on two parallel forms; retrieval from memory; delayed retest.

**The opening task asks for a monitoring design before the chapter says anything**, given Chapter 12's plan and four years of data. **Preserved unscored.**

## Transfer target

> Given a deployed rule with stated thresholds, a baseline period, an operating period, a set of monitored indicators that all look acceptable, and one quantity nobody reports, assess whether each threshold is a trigger or a timer, say what the monitoring can and cannot see, diagnose which stage the failure entered through, and state a revision trigger in both directions.

### Parallel forms

- **Form A — a water company's leakage-reduction programme and its automated pressure-management controller.**
- **Form B — a school trust's attendance-improvement plan and its automated absence-risk flag.**

Both supply: a deployed rule with two threshold limbs; seven baseline years; four operating years in which one limb fires and one does not; three monitored indicators that look acceptable; one unreported ratio; and a failure whose entry stage is early and whose symptom is late.

Every prior transfer and contrast domain is excluded. Neither domain is sensitive.

Chapter 17 must not claim durable far transfer. **No chapter may, and this is the last chance to say so.**

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| The life cycle has two parts; application includes use and archiving | `nasa2024models` p. 86 |
| Testing determines permissible uses; release records the domain | `nasa2024models` p. 87 |
| **Each application restarts the assessment** | `nasa2024models` p. 87 |
| Rejected, restricted, caveated, or placarded | `nasa2024models` p. 87 |
| The record is re-established on any change to world or model | `nasa2024models` p. 18 |
| A plan for operation, maintenance, and **retirement** | `nasa2024models` p. 39 |
| Reverse-flow loops are possible and expected | `nasa2024models` p. 88 |
| SPC originates with Shewhart | `sumanprajapati2018control` p. 1 |
| It rests on common and special causes of variation | `sumanprajapati2018control` p. 1 |
| Ignored performativity surfaces as distribution shift | `perdomo2020performative` Abstract |
| Retraining reread as an equilibrating dynamic | `perdomo2020performative` §1 |
| Overshoot from correcting after enough correction | `sterman2006evidence` p. 508, via Chapter 13 |
| Calibration and sharpness as a standing instrument | `gneiting2007scoring`, as verified in Chapter 6 |

### Not cited

Shewhart (1931) — **not obtained**. Deming on tampering — **not obtained**. `fda2023credibility`, `asme2025credibility`, `nrc2012reliability` — **not re-read**; Chapter 1's locators stand.

## Failure modes this chapter should prevent

1. Monitoring catches failures.
2. A threshold is a trigger.
3. A signal is a value past a threshold.
4. No alarm means nothing is wrong.
5. Drift and tampering are the same thing.
6. Monitoring is a technical activity rather than an assignment.
7. Post-deployment checking is a new activity.
8. A failure is diagnosed where it was noticed.
9. Every failure could have been caught by better monitoring.
10. A revision trigger is a plan to think again.
11. Deployment is the end of the process.
12. A model in use is a model that was validated for this use.

## Open questions

1. **Decision 0024 is unadjudicated**, as are 0009–0023, and three of its clauses need specific attention.
2. **The chapter declines machinery the architecture permits** — clause 2.
3. **`tampering` is unsourced** and named in governed text — clause 6.
4. **How the book ends** — clause 10.
5. **`utility` remains open in the registry with no later chapter to close it.**
6. **Gate 1 remains open**, fourteen chapters deep, across all sixteen chapters in which the anchor appears.
7. **No pilot data exists for any exercise in this book.**
