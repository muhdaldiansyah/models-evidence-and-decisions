---
chapter: 14
part: 4
title: "Sequential Decisions, Information, and Control"
status: drafted
pages_target: 28
hours_target: 6
---

# Chapter 14: Sequential Decisions, Information, and Control

**Provisional.** Built on proposed `../../decisions/0021-chapter14-sequential-control-terminology-and-boundary.md` and inheriting its status. Its exclusions, however, rest on `README.md` itself, which states them.

## Central question

How should choices be made through time as information arrives?

*Governed by `README.md`. Not amendable here.*

## Core competence

Reason with policies rather than one-shot actions, feedback decisions, observability, structural identifiability, information acquisition, exploration versus exploitation, and control at a foundational conceptual level.

*Governed by `README.md`. Not amendable here.*

**`README.md` also states this chapter's exclusions**, which no other chapter block does: "Formal dynamic programming, filtering, LQR, MPC, POMDP, and reinforcement-learning algorithms belong in the depth curriculum."

## Role in the book

Chapter 13 diagnosed a rule that could not work. Chapter 14 asks what rule the utility should have, and finds that the question changes what counts as an answer.

**Its unique job:**

> Teach readers that in a repeated decision the object of choice is a rule, not an action; that a rule can only use what the instruments reveal; and that what a set of instruments cannot reveal is a question answerable before any data is collected.

The chapter closes the book's longest-standing terminological debt. `observability` and `structural identifiability` have stood in `canon/terminology.md` as `TODO` since Chapter 1, and both close here.

## Hard prerequisites

- Chapter 4's finding that the demand figure is production minus metered consumption.
- Chapter 7's three-way distinction among identifiability senses, and its reservation of the third for here.
- Chapter 8's interval estimate.
- Chapter 11's value of information and its perfect-information ceiling.
- Chapter 12's finding that some settings supply no probabilities.
- Chapter 13's stocks, delays, feedback, and the rule that fired too late.

## Soft dependencies / spiral links

- Chapter 3's `validity` as a property of an interpretation — the same shape as observability.
- Chapter 6's forecast scoring, which was evaluative feedback without the name.
- Chapter 9's `transportability` as a relation — second instance of the same shape.
- Chapter 10's objectives, which is where the chapter's undecided comparison ends up.

## Established concepts to cover

Policies as the object of choice. Comparing rules across histories rather than one. Evaluative versus instructive feedback. Feedback decisions and their feedforward contrast. Observability. Structural identifiability, and its practical counterpart. Information acquisition under Chapter 11's ceiling. Exploration versus exploitation. Control at definitional depth.

## Terminology to introduce or stabilize

**Introduced:** `policy`, `feedback decision`, `practical identifiability`, `information acquisition`, `exploration`, `exploitation`, `control`.

**Closed from `TODO`:** `observability`, `structural identifiability` — both open since Chapter 1.

**Collision announced:** four senses of *identifiable*. The sixth announcement in the book and the first with four senses.

**Flagged for author review:** `practical identifiability` is not named in the governed core competence. Per `../../decisions/0021` clause 6.

## Interfaces with other chapters

| Chapter | Interface |
|---|---|
| 4 | supplies the residual demand figure, re-described here as structural non-identifiability |
| 7 | supplies two identifiability senses; Chapter 14 owes the third and adds a fourth |
| 8 | supplies the interval, re-described here as a practical-identifiability finding |
| 11 | supplies the ceiling; Chapter 14 reuses it and computes no value |
| 12 | supplies the no-probabilities setting |
| 13 | supplies the system's behaviour; Chapter 14 owns the decision-maker's rule |
| 15 | owns rules that agents respond to because they are the rules |
| 17 | owns whether a deployed rule is still working |

## Scope boundary

### Core

A policy as a mapping from what you see to what you do. Comparing four rules across five summers. Evaluative feedback. Observability as a property of a system paired with instruments. Structural non-identifiability, diagnosable before data. Practical identifiability as a property of model and data. Measure more or model less. An instrument screened against Chapter 11's ceiling. Exploration as the only route to information about an untried rule. Control, defined.

### Deferred to later chapters

Rules that change behaviour because they are rules; incentives, gaming, performativity (Chapter 15). Whether a deployed rule is still working (Chapter 17).

### Deferred to depth curriculum

**The six `README.md` names:** dynamic programming, filtering, LQR, MPC, POMDPs, reinforcement-learning algorithms.

**And, additionally:** observers, state estimation, the separation principle, the Kalman filter, the observability rank test, reachability, state feedback, profile likelihood, the Fisher information matrix, any identifiability test, any bandit algorithm, any control law, optimal stopping, Bayesian sequential design.

## Section architecture

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | The Thing You Are Choosing Is a Rule | 3 | 0.60 |
| 2 | Policies, and Why One Summer Cannot Rank Them | 5 | 1.05 |
| 3 | What the Instruments Determine | 4 | 0.90 |
| 4 | Two Parameters That Cannot Be Told Apart | 5 | 1.10 |
| 5 | Measure More, or Model Less | 3 | 0.65 |
| 6 | Buying an Instrument | 3 | 0.65 |
| 7 | Exploration, and Why Most Years Teach Nothing | 3 | 0.65 |
| 8 | Cold-Start Practice and Retrieval | 2 | 0.40 |

Eight sections, 28 pages, 6 hours. Roughly 360 words per page — about **10,080 words**.

Three self-explanation pauses: §2 (which rule would you keep?), §4 (what would settle it?), §7 (how many years would you need?).

## Examples / recurring cases

**The water anchor's eleventh recurrence, and the first run across several years.** Frozen in `case-data.md`; every policy figure computed by simulation before drafting.

## Exercise architecture

Per `../../decisions/0008`. Opening task before vocabulary; three pauses; five-defect diagnosis; cold transfer on two parallel forms; retrieval from memory; delayed retest.

**One design constraint is load-bearing.** The opening task asks for a **rule**, stated precisely enough for somebody else to apply. Thirteen chapters have asked for analyses, estimates, and choices; this is the shift, and it must happen before §2 defines a policy.

## Transfer target

> Given a repeated decision with a written rule, several histories over which to compare rules, two states the instruments cannot distinguish, and two model parameters that enter only as a sum, evaluate the rules across all histories, identify which comparisons the histories cannot settle, say which failure is structural and which is practical, and decide whether to buy the instrument that would fix both.

### Parallel forms

- **Form A — a regional grid operator's reserve procurement** (energy).
- **Form B — a livestock veterinary service's antibiotic stewardship** (agriculture and animal health).

Both supply: a repeated decision with a written trigger rule; five histories; at least one history on which all rules are identical; two states with the same instrument signature; two parameters entering only as a sum; and one instrument priced against a decision already on the table.

Every prior transfer and contrast domain is excluded. Neither domain is sensitive.

Chapter 14 must not claim durable far transfer.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| A policy is a mapping from states to action probabilities | `sutton2018reinforcement` p. 58 |
| Problems and solution methods must be kept apart | `sutton2018reinforcement` p. 2 |
| Evaluative versus instructive feedback | `sutton2018reinforcement` p. 25 |
| Exploration and exploitation, defined and traded off | `sutton2018reinforcement` p. 26 |
| The dilemma remains unresolved | `sutton2018reinforcement` p. 3 |
| The theory's guarantees rest on assumptions often violated | `sutton2018reinforcement` p. 27 |
| Observability, paraphrased | `astrom2008feedback` p. 202 |
| No hidden dynamics; sensors sufficient for control | `astrom2008feedback` p. 202 |
| Virtual sensors and sensor fusion | `astrom2008feedback` p. 202 |
| Control, defined; sensing–computation–actuation | `astrom2008feedback` pp. 3–4 |
| Structural versus practical identifiability | `wieland2021identifiability` p. 61 |
| Structural identifiability defined | `wieland2021identifiability` p. 61 |
| Practical identifiability as model **and** data | `wieland2021identifiability` p. 63 |
| Practical nonidentifiability less settled | `wieland2021identifiability` p. 60 |
| Measure more, or model less | `wieland2021identifiability` p. 64 |
| The perfect-information ceiling | `colyvan2016voi`, as verified in Chapter 11 |

### Not cited

Bellman and Åström (1970) — **not obtained**; recorded as the chapter's principal source gap. Villaverde et al. (2016) — obtained, declined for want of visible pagination.

## Failure modes this chapter should prevent

1. A policy is a plan.
2. A rule that worked is a good rule.
3. Observability is about whether an instrument exists.
4. Unobservable means unmeasured.
5. Structural non-identifiability is a data problem.
6. Structural and practical non-identifiability are the same.
7. Any one of the four identifiabilities is any other.
8. More information is always worth buying.
9. Exploration is a luxury.
10. Exploration is free because you learn either way.
11. The theory settles the exploration trade.
12. Control means being in control.
13. A dominated rule means somebody was foolish.

## Open questions

1. **Decision 0021 is unadjudicated**, as are 0009–0020.
2. **`practical identifiability` is not in the governed core competence** — clause 6.
3. **Bellman and Åström (1970) not obtained**; a canon `TODO` is closed from a secondary source for the first time — clause 8.
4. **`utility` remains open in the registry**, assigned to the drafted Chapter 11. It is now the only one.
5. **Gate 1 remains open**, eleven chapters deep.
