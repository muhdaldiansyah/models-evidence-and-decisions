---
chapter: 6
part: 2
title: "Probability, Prediction, and Simulation"
status: specified
pages_target: 34
hours_target: 7
---

# Chapter 6: Probability, Prediction, and Simulation

> **Provisional.** Built on `../../decisions/0013-chapter6-probability-terminology-and-notation.md`, which is **PROPOSED and not author-adjudicated**. The eight Chapter 6 entries in `../../canon/terminology.md`, and the updated `calibration` entry, are provisional for the same reason. **Decision 0013 clause 2 breaks the book's five-chapter no-notation policy** and deserves separate attention. Title, central question, core competence, and the page and hour targets are **not** provisional — they are governed by `README.md` and `../../decisions/0001`.

## Central question

How is uncertainty represented, updated, and scored?

## Core competence

Use conditioning, Bayes, expectation, base rates, simulation, probabilistic prediction, and calibration to reason coherently under uncertainty.

## Role in the book

Chapter 6 opens Part II. Chapter 5 closed Part I by observing that nearly every unresolved item was now a question about evidence: how likely is it that the tank starts lower than assumed, what would the pump test actually tell us, how much would one hot afternoon move belief about Mechanism A.

Part I supplied no way to answer any of them beyond *it might* and *it might not*.

Chapter 6's unique job:

> Teach readers to hold uncertainty as a stated quantity conditional on stated information, to update it coherently when evidence arrives, and to be scored on the result.

The chapter must accomplish five things.

1. Establish that a probability is not a property of an event but of an event given stated information — which dissolves the one-off-event objection and makes conditioning the central concept.
2. Give the reader an update procedure they can execute by hand, on two hypotheses, and know what the answer means.
3. Establish what people demonstrably do with base rates, so the arithmetic has a reason to exist.
4. Make probabilistic claims accountable: what a scoring rule is for, why a good one cannot be gamed, and why a single forecast cannot be scored.
5. Frame simulation as computing the consequences of assumptions, not as producing evidence.

**Chapter 6 is the first chapter that teaches a technique rather than a habit of mind.** Part I taught ways of looking. This chapter has mathematics attached, and the reader is assumed comfortable with algebra and unwilling to be handed a statistics course. That tension is why this is the longest chapter in the book.

## Hard prerequisites

- Chapters 1–5. The anchor is Chapter 5's list of open items and is not restated from scratch.
- Arithmetic, ratios, and percentages. Ability to multiply two numbers.
- Willingness to write a number down and be wrong about it later.
- No prior probability or statistics. No calculus.
- No domain expertise. All case facts are supplied.

## Soft dependencies / spiral links

| Spiral element | Treatment in Chapter 6 | Later development |
|---|---|---|
| Uncertainty | Represented as a stated conditional quantity | Chapters 8, 11, 12 |
| Conditioning | Central concept; explicitly not intervening | Chapter 7 |
| Base rates | Used, and the tendency to abandon them documented | Chapters 8, 9 |
| Expectation | A summary of a distribution | Chapter 11 |
| Calibration | Forecast sense, reopening Chapter 3's collision | Chapter 17 |
| Simulation | Computing consequences of assumptions | Chapters 8, 12, 14 |

## Established concepts to cover

### Conditioning and updating

- A probability is stated conditional on information. Mathematics, taught by demonstration.
- Conditioning changes what is taken as given; it is not filtering.
- `P(A | B)` and `P(B | A)` are different quantities.
- Bayes in odds form: prior odds × ratio = posterior odds.
- Conditioning is not intervening (`pearl2009causal`).

### Base rates

- Representativeness: "probabilities are evaluated by the degree to which A is representative of B" (`tversky1974judgment` p. 1124).
- Base-rate frequency has "no effect on representativeness but should have a major effect on probability" (p. 1124).
- The engineers-and-lawyers result: "In a sharp violation of Bayes' rule, the subjects in the two conditions produced essentially the same probability judgments" (p. 1124).
- **The qualification that matters:** "people respond differently when given no evidence and when given worthless evidence. When no specific evidence is given, prior probabilities are properly utilized; when worthless evidence is given, prior probabilities are ignored" (p. 1125).
- Insensitivity to sample size; conservatism — "The underestimation of the impact of evidence has been observed repeatedly" (p. 1125).
- The heuristics "are quite useful, but sometimes they lead to severe and systematic errors" (p. 1124).

### Scoring

- Propriety: the forecaster "is encouraged to quote his or her true belief" (`gneiting2007scoring` p. 359).
- "Intuitively appealing but improper" rules are a real hazard (pp. 359–360).
- Calibration is "a joint property of the forecasts and the events or values that materialize"; sharpness is "a property of the forecasts only" (p. 359).
- The goal is "to maximize the sharpness of the predictive distributions subject to calibration" (p. 359).
- The idea dates at least to Brier (1950), **as reported at** p. 360.

## Terminology to introduce or stabilize

Eight terms registered provisionally; `calibration` updated in place.

| Term | Treatment | Distinction or caution |
|---|---|---|
| probability | Required | Of an event **given information**; never stated without its conditioning |
| conditional probability | Required | Not filtering; `P(A\|B)` ≠ `P(B\|A)`; not intervening |
| prior | Required | Often set from a base rate; not an arbitrary starting point |
| posterior | Required | Via odds form; a posterior without its ratio hides whether evidence did work |
| base rate | Required | Neglect is **conditional**, triggered by worthless-looking evidence |
| expectation | Required, as a summary | **Not** what will happen; not a decision rule |
| sharpness | Required | Property of forecasts alone; the objective, subject to calibration |
| scoring rule | Concept depth | Propriety; a single forecast cannot be scored |
| calibration | Forecast sense; **collision reopened** | Joint property of forecasts and outcomes |

**Not used:** `likelihood` (Chapter 8 owns the estimation sense), `random variable`, `density`, `variance`, `confidence`, `significance`.

### Notation

**Permitted:** `P(A | B)`; odds as `3 : 1`; arithmetic.
**Not permitted:** summation, integration, calculus; distributions as functions; random variables as symbols; expectation operators; the Bayes formula with its denominator.

The exception is **announced to the reader** with its reason.

## Interfaces with other chapters

| Chapter | Interface established here | Boundary Chapter 6 must respect |
|---|---|---|
| Ch. 3 | `calibration` collision reopened, once | Do not adopt the word silently |
| Ch. 5 | Chapter 5 named the discriminating observation; Chapter 6 says how far it moves belief | Do not reteach criticism |
| Ch. 7 | **Conditioning is not intervening**, stated once | Do not define estimands, identifiability, or causal identification |
| Ch. 8 | Uncertainty represented and updated | Do not teach likelihood, regression, intervals, or UQ |
| Ch. 9 | — | Do not teach transportability |
| Ch. 11 | Expectation as a summary; a ratio near 1 means an observation moves nothing | Do not teach expected utility, risk attitude, or value of information |
| Ch. 12 | — | Do not teach robustness formalism |
| Ch. 14 | Updating once, by hand | Do not teach sequential updating, filtering, or observability |
| Ch. 17 | Scoring a forecast after the fact | Do not teach monitoring design |

## Scope boundary

### Core

- State a probability together with the information it is conditional on, and refuse the unqualified form.
- Recognize that a unique event can carry a probability, and say why the objection fails.
- Distinguish `P(A | B)` from `P(B | A)` and identify the inversion error in someone else's reasoning.
- Set a prior from a base rate where one is available, and say what population it came from.
- Express prior belief as odds.
- Compute a ratio from two stated likelihoods and apply the odds update by hand.
- Recognize that a ratio near 1 means the observation moves nothing.
- Recognize the pattern in which worthless-looking evidence displaces a base rate.
- Read an expectation as a summary and not as a prediction of what will happen.
- Assess a record of past probabilistic statements for calibration.
- Distinguish calibration from sharpness and explain why calibration alone is not the goal.
- Explain why a single forecast cannot be scored, and why an unscored forecast is unfalsifiable.
- Describe what a simulation computes and what it does not.
- State what more simulation runs improve and what they leave untouched.

### Deferred to later chapters

- Estimands, identifiability, causal identification, intervention, counterfactuals: Chapter 7.
- Likelihood, estimation, regression, intervals, uncertainty quantification, model checking: Chapter 8.
- Evidence synthesis, external validity, transportability: Chapter 9.
- Expected utility, risk attitude, decision trees, value of information: Chapter 11.
- Robustness, regret, scenarios, adaptive plans: Chapter 12.
- Sequential updating, filtering, observability, control: Chapter 14.
- Monitoring design, drift detection: Chapter 17.

### Deferred to depth curriculum

- Foundations and interpretations of probability; measure theory.
- Bayesian computation: MCMC, conjugacy, hierarchical models.
- Which scoring rules are proper, and the mathematics of propriety.
- The continuous ranked probability score and multivariate scores.
- Variance reduction, importance sampling, quasi-Monte Carlo.
- The heuristics-and-biases literature beyond the results cited, and the debiasing literature.

## Section architecture

No new case. The anchor is Chapter 5's list of open items, worked probabilistically.

| Section | Working title | Pages | Learning hours | Primary output |
|---|---|---:|---:|---|
| 1 | How Likely Is It? | 2 | 0.30 | An unscaffolded probability for Mechanism A, with whatever reasoning the reader has |
| 2 | A Probability Is Conditional on Something | 5 | 1.00 | A probability restated with its conditioning information |
| 3 | Moving Between Positions: The Odds Update | 6 | 1.25 | The Mechanism A/B update computed by hand, both ways |
| 4 | Base Rates and Worthless Evidence | 5 | 1.00 | A ratio computed for a detail that turns out to move nothing |
| 5 | Expectation, and What It Is Not | 3 | 0.60 | An expectation computed and correctly described |
| 6 | Being Scored | 6 | 1.20 | A calibration assessment of the utility's forecasting record |
| 7 | Simulation: Consequences of Assumptions | 4 | 0.85 | A statement of what a simulation of the storage projection would and would not settle |
| 8 | Cold-Start Practice and Retrieval | 3 | 0.80 | An independently produced probabilistic analysis |
| **Total** |  | **34** | **7.00** |  |

### Drafting constraints

- No new case. The anchor is Chapter 5's open items.
- At least half of active learning time is prediction, production, explanation, diagnosis, or retrieval, per `../../decisions/0008`.
- Three self-explanation pauses: at conditioning (§2), at the worthless-evidence detail (§4), at the always-45% forecaster (§6).
- **The notation exception is announced in §2** and never exceeded.
- **Every probability the chapter states carries its conditioning information.** The chapter must model the discipline it teaches.
- The `calibration` collision is reopened once, in §6.
- Conditioning-is-not-intervening is stated once, in §3, and not developed.

## Examples / recurring cases

### The anchor: Chapter 5's open items

**Centrepiece — Mechanism A versus Mechanism B**, open since Chapter 2, named unresolved in Chapter 5, with a discriminating observation identified and never made.

- **Prior**, from the utility's own history: of 11 recorded low-pressure investigations in pumped zones, **7** were pump-capacity limited and **4** main-related. Odds **7 : 4**, about **1.75 : 1** for A.
- **The test**: run the duty pump at elevated output through a hot afternoon and record pressure at the top of the zone. Under A, recovery greater than 8 m expected with probability **0.85**; under B, **0.15**.
- **Recovery**: ratio ≈ **5.7**, posterior odds ≈ **9.9 : 1** for A, about **91%**.
- **No recovery**: ratio ≈ **0.18**, posterior ≈ **3.2 : 1** for B, about **76%**.

One afternoon moves belief from roughly 2:1 to either 10:1 or 1:3. That is what makes it worth doing — and the reader can now say so with a number.

**The base-rate demonstration.** A detail arrives: the caller says it has been getting worse since the hot spell began. Consistent with both mechanisms; ratio near 1. This instantiates `tversky1974judgment` p. 1125 on the anchor.

**The calibration demonstration.** The utility's record across 40 past heat-event briefings:

| Said | Times | Breached | Observed |
|---:|---:|---:|---:|
| 90% | 10 | 5 | 50% |
| 70% | 10 | 5 | 50% |
| 50% | 10 | 5 | 50% |
| 30% | 10 | 3 | 30% |

Calibrated at the low end, badly overconfident at the high end. Overall base rate **18/40 = 45%** — so a forecaster saying 45% every time is perfectly calibrated and useless.

**The simulation demonstration.** The seven-day storage projection with a spread on daily demand rather than Chapter 1's point forecast.

**New synthetic facts required**, extending five prior case-data files. All of it **inherits Chapter 1's open SME gate, now five chapters deep.**

### Deliberately not used

Medical-test examples — the standard Bayes vehicle, which would import Chapter 7's identification concerns and Chapter 3's measurement concerns at once.

## Exercise architecture

1. **Opening attempt (§1).** How likely is Mechanism A, and why? Preserved unscored.
2. **Restate with conditioning (§2).** Rewrite the opening probability with its conditioning information.
3. **The update (§3).** Compute both branches by hand.
4. **The ratio that moves nothing (§4).** Compute it and say what follows.
5. **Expectation (§5).** Compute one and describe it correctly.
6. **Calibration assessment (§6).** Complete the observed column and state the pattern.
7. **Planted-defect diagnosis (§7).** Five defects.
8. **Cold transfer (§8).** One assigned parallel form.
9. **Retrieval and delayed retest (§8).**

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| "There is a 70% chance the pump is the cause", with no conditioning stated | a probability is a property of the event |
| "We said 80% and it happened, so the forecast was good" | a single forecast can be scored |
| "The test was positive, so it is probably A" — the inversion | `P(A\|B)` = `P(B\|A)` |
| "We ran 50,000 simulations, so the estimate is reliable" | more runs fix model error |
| "You cannot put a number on a one-off event" | probability requires a frequency |

### Rubric dimensions

1. Every probability stated with its conditioning information.
2. Prior set from a stated base rate, with its population named.
3. Ratio computed from two stated likelihoods.
4. Update executed correctly, both branches.
5. An observation with a ratio near 1 identified and correctly dismissed.
6. Expectation described as a summary, not as a prediction.
7. Calibration assessed over a record, with the pattern named.
8. Calibration distinguished from sharpness.

## Transfer target

> Given a situation with two candidate explanations, a stated base rate, and a proposed observation with stated likelihoods, produce a probability with its conditioning information, update it correctly, identify one supplied detail that moves nothing and say why, and assess a short forecasting record for calibration.

### Parallel forms

- **Form A — a fleet operator's intermittent vehicle fault** (physical/technical).
- **Form B — a housing team deciding whether a rise in reported damp is real** (institutional).

Both supply: a base rate the reader must use; one observation whose ratio is worth computing; one distractor whose ratio is near 1; and a forecasting record with a visible calibration pattern.

Every prior transfer and contrast domain is excluded. Neither domain is sensitive, which is a change from Chapters 4 and 5.

Chapter 6 must not claim durable far transfer.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| Representativeness; base rates have no effect on it | `tversky1974judgment` p. 1124 |
| The engineers-and-lawyers violation of Bayes | `tversky1974judgment` p. 1124 |
| Priors used with no evidence, abandoned with worthless evidence | `tversky1974judgment` p. 1125 |
| Insensitivity to sample size; conservatism | `tversky1974judgment` p. 1125 |
| Heuristics are useful, not merely defective | `tversky1974judgment` p. 1124 |
| Propriety; honesty is score-maximising | `gneiting2007scoring` p. 359 |
| Intuitively appealing but improper rules | `gneiting2007scoring` pp. 359–360 |
| Calibration joint; sharpness of forecasts alone; the goal | `gneiting2007scoring` p. 359 |
| Brier 1950 provenance, **as reported** | `gneiting2007scoring` p. 360 |
| Conditioning is not intervening | `pearl2009causal` |

### Known gaps constraining the manuscript

1. **Brier (1950) not obtained.** Referenced only as reported at `gneiting2007scoring` p. 360; no direct citation.
2. **`tversky1974judgment` read to p. 1125 only.**
3. **`gneiting2007scoring` read to p. 360 only.**
4. **The debiasing literature was not read** and must not be characterized.
5. The always-state-the-base-rate demonstration and the single-forecast argument are **derived, not sourced**.
6. Conditioning, Bayes, expectation, and Monte Carlo mechanics are **mathematics, taught by demonstration**. `research-04` §1 records that this is **not** an instance of the demonstrate-because-unsourced pattern that `../../decisions/0012` clause 4.3 puts on notice, and states the distinction rather than assuming it.

### Evidence needed before prose is stable

- SME review of the pump-test likelihoods and the investigation history, coupled to Chapter 1's open Gate 1.
- Timed reader pilot against the 7-hour target — the longest in the book and the most likely to overrun.

## Failure modes this chapter should prevent

1. Probability is a frequency and nothing else.
2. A probability is a property of the event.
3. Conditioning is filtering.
4. `P(A | B)` equals `P(B | A)`.
5. Base rates can be ignored once you have evidence.
6. A model that fits well gives good probabilities.
7. Calibration is accuracy.
8. A single forecast can be evaluated.
9. Simulation produces evidence about the world.
10. More simulation runs make the answer better.
11. The expectation is what will happen.
12. A probability for a unique event is meaningless.

## Open questions

### Before drafting

1. Does the author accept Decision 0013 as proposed, and if not, which clauses change?
2. **Accept the bounded notation exception, breaking a five-chapter policy — and is it announced to the reader?**
3. Odds form for Bayes, or the standard formula?
4. Is the five-row pattern table restated here, or assumed from Chapter 5?
5. Are the Mechanism A/B likelihoods supplied, or must the reader elicit them?
6. Accept the sixth recurrence of the water case?

### Before declaring Chapter 6 verified or frozen

7. Has Brier (1950) been obtained, or the reference left explicitly second-hand?
8. Has `tversky1974judgment` been read past p. 1125?
9. Has `gneiting2007scoring` been read past p. 360?
10. Have the pump-test likelihoods passed SME review?
11. Does the 34-page / 7-hour budget survive a timed reader pilot?
