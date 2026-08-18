---
chapter: 12
part: 3
title: "Optimization, Robustness, and Adaptive Plans"
status: specified
pages_target: 36
hours_target: 7
---

# Chapter 12: Optimization, Robustness, and Adaptive Plans

> **Provisional.** Built on `../../decisions/0019-chapter12-optimization-terminology-and-boundary.md`, which is **PROPOSED and not author-adjudicated**. The ten Chapter 12 entries in `../../canon/terminology.md`, the `robustness` entry it closes, and the specialised `constraint` entry are provisional for the same reason. **Decision 0019 clause 1 records that, unlike Chapter 11, nothing in this chapter is taught unsourced.** Title, central question, core competence, and the page and hour targets are **not** provisional — they are governed by `README.md` and `../../decisions/0001`.

## Central question

How do we choose well at scale when the model itself is uncertain?

## Core competence

Formulate objectives and constraints, reason marginally, understand shadow-price and convexity intuition, and use scenarios, robustness, regret, adaptive plans, and computational solver handoff appropriately.

## Role in the book

Chapter 12 closes Part III, and it is the chapter where the anchor finally scales.

Everything from Chapter 1 to Chapter 11 concerned one zone and, latterly, one choice. The governed central question says **at scale**, and the object of choice becomes a portfolio drawn from seven candidate schemes against a fixed envelope.

**And the second half of the question is the pivot.** Chapter 11 optimised against a probability of 0.636 and everything followed from it. This chapter asks what to do when the model itself is in doubt, and takes its answer from a source that states the replacement directly: traditional decision analysis "seeks the optimal strategy, that is, the one that performs best for **a fixed set of assumptions about the future**" [@lempert2003shaping, p. 52].

**Five chapters and one book-level decision defer here**, and `robustness` has been reserved for this chapter since Chapter 5.

## Hard prerequisites

- **Chapter 10** — `constraint`, and the practice of asking who set each one.
- **Chapter 11** — expected value as a rule; the critical value; the three responses when the answer turns, of which this chapter treats two.
- **Chapter 1** — the £2.4m envelope's origin, and feasibility named.

## Soft dependencies / spiral links

- **Chapter 5** — `robustness` reserved here by Decision 0012 clause 5.4; the robust-theorem habit.
- **Chapter 8** — position relative to a threshold decides direction.
- **Chapter 9** — sources that disagree, and acting anyway.

## Established concepts to cover

1. Programme scale: the object of choice is a combination [@bradley2016structured, p. 8 for the process placement].
2. Marginal benefit, marginal cost, opportunity cost [@epa2010economic, pp. xiii–xiv].
3. The efficiency condition, **and its failure on indivisible investments**.
4. Shadow prices, with locality and asymmetry [@boyd2004convex, pp. 241, 251–252].
5. Convexity through its consequence [@boyd2004convex, pp. 8–9].
6. Solver handoff: recognising is the hard part [@boyd2004convex, p. 8].
7. Scenario ensembles as challenge sets, with the diversity requirement [@lempert2003shaping, p. 52].
8. Robustness replacing optimality [@lempert2003shaping, p. 52].
9. The many-value-systems clause, repairing Chapter 11's single currency [@lempert2003shaping, pp. 52–53].
10. Regret, **with Savage's four pathologies** [@lempert2003shaping, p. 53, n. 13].
11. Adaptive strategies as a route to robustness [@lempert2003shaping, pp. 40, 57].
12. Shaping / hedging / signposts, as reported [@lempert2003shaping, p. 58].
13. Naming the futures implicitly classed as unimportant [@lempert2003shaping, p. 57].

## Terminology to introduce or stabilize

Ten new, one closed, one specialised. See `../../canon/terminology.md`, Chapter 12 block, and `../../decisions/0019` §7.

### Notation

**None is added.** A programme table and a regret table. No formulation, no algorithm, no diagram. The governed word "intuition" is read as controlling.

## Interfaces with other chapters

| Chapter | Line |
|---|---|
| 5 | `robustness` reserved here by Decision 0012 |
| 10 | `constraint` specialised: not *is it real* but *what is it worth to move* |
| 11 | optimises against a fixed model; this chapter replaces the standard |
| **13** | **systems that respond to action; Part IV opens** |
| 14 | sequential control and dynamic programming |
| 17 | signposts are designed here and operated there |

## Scope boundary

### Core

- Programme-scale choice under a binding constraint.
- Marginal reasoning, and where it fails.
- What a constraint is worth.
- Convexity through its consequence; solver handoff.
- Scenarios, robustness, regret.
- Adaptive plans and signposts.

### Deferred to later chapters

- Feedback and system response — Chapter 13.
- Sequential control, dynamic programming — Chapter 14.
- Operating signposts — Chapter 17.

### Deferred to depth curriculum

- Any algorithm or formulation.
- Duality, KKT conditions, multipliers as machinery.
- Integer programming as a technique.
- Real options valuation; adaptive management.
- Robust optimization as a mathematical programme.
- Lempert's method, software, XLRM, and scenario generator.

## Section architecture

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | Fifteen Zones, Not One | 2 | 0.35 |
| 2 | Objectives and Constraints at Scale | 5 | 0.95 |
| 3 | Reasoning at the Margin | 5 | 0.95 |
| 4 | What a Constraint Is Worth | 5 | 0.95 |
| 5 | When Local Improvement Finds the Best | 5 | 1.00 |
| 6 | When the Model Itself Is Uncertain | 7 | 1.40 |
| 7 | Adaptive Plans | 4 | 0.80 |
| 8 | Cold-Start Practice and Retrieval | 3 | 0.60 |

**36 pages, 7.00 hours.**

### Drafting constraints

- One sentence per line in manuscript prose.
- **No formulation, algorithm, or diagram.**
- The `boyd2004convex` p. 252 sentence is **paraphrased**, not quoted, because it carries symbols.
- Savage and Dewar cited **as reported at** `lempert2003shaping`.
- Minimax regret is **not** presented as the right rule.
- The staging premium is stated as an assumption.

## Examples / recurring cases

### The anchor: the twelfth recurrence, at programme scale

`case-data.md` freezes: seven schemes against the £2.4m envelope; three futures; and **every computed figure** — ratios, the optimum, the divisible and indivisible shadow prices, the three futures' optima, the full regret table, and the minimax portfolio.

### Deliberately not used

- Any case where the envelope does not bind.
- Any case where the robust choice is also an optimum, which would leave §6 with no lesson.
- Any new physical fact about the network.

## Exercise architecture

1. **Opening attempt (§1).** How would you spend £2.4m across seven schemes? Six minutes, unscored.
2. **Ratios (§3).** Rank by benefit per pound; say what the ranking assumes.
3. **The stopping rule (§3).** Apply it; find where it fails.
4. **The envelope (§4).** Compute what an extra £200k is worth. Then an extra £50k.
5. **Futures (§6).** Build the regret table.
6. **The robust choice (§6).** Find it; say what it is optimal in.
7. **Planted-defect diagnosis (§7).** Five defects.
8. **Cold transfer (§8).** One assigned parallel form.
9. **Retrieval and delayed retest (§8).**

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| "We ranked by benefit per pound and funded down the list until the money ran out" | greedy ranking is optimal |
| "The optimiser found the best programme, so that is the programme" | optimality is defined relative to a model |
| "An extra £100k would be worth about £34k of benefit" | shadow prices are fixed and smooth |
| "We tested twenty scenarios, so the plan is robust" | count, not diversity |
| "The plan is adaptive — we will review it annually" | a review date is not a signpost |

### Rubric dimensions

1. The envelope treated as binding, and its origin questioned.
2. Marginal ranking produced **and** its limits stated.
3. A shadow price computed, with its locality noted.
4. Lumpiness identified as breaking the stopping rule.
5. A regret table built across futures.
6. A robust choice identified that is optimal in no future.
7. An adaptive plan with a **named threshold**, not a review date.

## Transfer target

> Given a portfolio decision under a binding budget, several candidate schemes including one that is phaseable, and three futures with different benefits, produce the marginal ranking and say where it fails, compute what the budget constraint is worth, build a regret table, identify a robust portfolio, and turn it into an adaptive plan with named signposts.

### Parallel forms

- **Form A — a port authority's berth and dredging programme** (infrastructure).
- **Form B — a health system's diagnostic capacity programme** (public service).

Both supply: a binding budget; a phaseable large scheme; a scheme whose value collapses in one future; three futures; and a robust portfolio that is optimal in none.

Every prior transfer and contrast domain is excluded. Neither domain is sensitive.

Chapter 12 must not claim durable far transfer.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| Marginal benefit, marginal cost | `epa2010economic` p. xiii |
| Opportunity cost, not requiring money | `epa2010economic` p. xiv |
| Efficiency condition | `epa2010economic` glossary |
| Shadow prices as constraint prices | `boyd2004convex` p. 241 |
| Locality and asymmetry | `boyd2004convex` pp. 251–252 |
| Convex problems are reliably solvable | `boyd2004convex` p. 8 |
| Recognising is the hard part | `boyd2004convex` p. 8 |
| No effective general nonlinear methods | `boyd2004convex` p. 9 |
| Local optima; how far off is unknown | `boyd2004convex` p. 9 |
| Acting without reliable predictions | `lempert2003shaping` p. 39 |
| Robust options across futures and values | `lempert2003shaping` p. 40 |
| Optimality is relative to fixed assumptions | `lempert2003shaping` p. 52 |
| Robustness defined | `lempert2003shaping` p. 52 |
| Many value systems | `lempert2003shaping` pp. 52–53 |
| Scenario ensembles; diversity | `lempert2003shaping` p. 52 |
| Savage's regret and its pathologies, **as reported** | `lempert2003shaping` p. 53, n. 13 |
| Adaptivity as a route to robustness | `lempert2003shaping` pp. 40, 57 |
| Shaping, hedging, signposts, **as reported** | `lempert2003shaping` p. 58 |
| Futures implicitly classed as unimportant | `lempert2003shaping` p. 57 |

### Known gaps constraining the manuscript

1. **Savage (1950) and Dewar (1993, 2001)** cited within `lempert2003shaping`; neither obtained.
2. **`boyd2004convex` read at pp. 7–9, 241, 250–252 only.**
3. **`lempert2003shaping` read at pp. 39–40, 52–53, 57–58 only.**
4. **`epa2010economic` read at its glossary only**; its shadow-price-of-capital section unread.
5. **The staging premium is an assumption**, stated as such.
6. `lempert2003shaping` is twenty-three years old and its computing claims are dated; the book uses its concepts.

### Evidence needed before prose is stable

- SME review of the seven schemes, their costs and benefits, and the three futures, coupled to Chapter 1's open Gate 1, **now twelve chapters deep**.
- Timed reader pilot against the 7-hour target.
- A second opinion on whether the anchor's minimax margin — 580 against 590 — is too fine to carry the section's weight.

## Failure modes this chapter should prevent

1. Optimization gives the right answer.
2. The optimum is the point of the exercise.
3. Spend until marginal benefit equals marginal cost.
4. A shadow price is a fixed number.
5. Local improvement finds the best.
6. The hard part is the solver.
7. Scenarios are forecasts.
8. Robustness means insensitivity to one input.
9. Minimax regret is the right rule.
10. An adaptive plan is a vague plan.
11. Robustness is free.
12. More scenarios is better analysis.
13. Greedy ranking by ratio is optimal.

## Open questions

### Before drafting

1. Does the author accept Decision 0019 as proposed?
2. Is teaching optimization through intuition alone the right reading of the governed core competence?
3. Is the minimax margin of 580 against 590 too fine, and should the case be retuned?
4. **Should the chapter say plainly that Chapter 11's method is the one being replaced?**
5. Accept the twelfth recurrence, now at programme scale?

### Before declaring Chapter 12 verified or frozen

6. Have Savage (1950) or Dewar been obtained?
7. Has a more recent robust-decision source been obtained, given `lempert2003shaping`'s age?
8. Have the seven schemes and three futures passed SME review?
9. Does the 36-page / 7-hour budget survive a timed reader pilot?
