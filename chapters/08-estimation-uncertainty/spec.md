---
chapter: 8
part: 2
title: "Estimation, Uncertainty, and Model Checking"
status: specified
pages_target: 40
hours_target: 8
---

# Chapter 8: Estimation, Uncertainty, and Model Checking

> **Provisional.** Built on `../../decisions/0015-chapter8-estimation-terminology-and-notation.md`, which is **PROPOSED and not author-adjudicated**. The seven Chapter 8 entries in `../../canon/terminology.md`, and the two it closes from `TODO`, are provisional for the same reason. **Decision 0015 clause 2 declines to extend the notation exception and thereby departs from a promise Chapter 6 made to the reader**; it is the first notation clause in the book that refuses rather than permits. Title, central question, core competence, and the page and hour targets are **not** provisional — they are governed by `README.md` and `../../decisions/0001`.

## Central question

What does finite evidence say, with what reliability?

## Core competence

Use likelihood, estimation, regression, uncertainty quantification, predictive evaluation, measurement-error reasoning, analytic-flexibility awareness, and model checking without reducing evidence to threshold rituals.

## Role in the book

Chapter 8 is step 4 of the four-step spine Chapter 7 borrowed: **Estimate**.

It is also the chapter that has to solve an architectural problem no previous chapter has faced. The governed core competence names **eight** subjects, each with textbooks of its own. Forty pages divided eight ways is a survey, and `README.md`'s Intellectual Principle forbids the book from becoming a tour of specialist machinery.

**The solution is a spine that makes the eight into consequences of one claim**, taken from a source:

> a computed result "tests all the assumptions about how the data were generated (the entire model)", and those assumptions "include assumptions about the conduct of the analysis" [@greenland2016misinterpretations, p. 339].

The mapping is recorded at `research-02-what-a-number-is-conditional-on.md` §5 and is the reason this chapter is one chapter.

## Hard prerequisites

- **Chapter 1** — estimand/estimator/estimate previewed as three things; the forecast conditional on no new action.
- **Chapter 3** — trueness versus precision; resolution is not trueness; a calibrated instrument is not a correct reading.
- **Chapter 4** — the subtraction residual; `meng2018paradox` on the term that does not contain the number of records.
- **Chapter 5** — fitting the data a model was built from could not have failed; sensitivity analysis is not criticism and belongs here.
- **Chapter 6** — the supplied ±0.6 ML spread, flagged in terms as justified by nothing; calibration over a record; the inversion.
- **Chapter 7** — the verdict of *not identified*; a good estimator cannot repair a bad identification.

## Soft dependencies / spiral links

- **Chapter 6 §6** and **Chapter 7 §6** — a property defined over an ensemble, read off a single instance. Chapter 8 is the third appearance.
- **Chapter 3** — measurement uncertainty as a component distinct from sampling variability.

## Established concepts to cover

1. `estimand`, `estimator`, `estimate` — three things, never blurred.
2. Bias, variance, consistency — properties of the **procedure**.
3. The spine: a number is conditional on a whole model [@greenland2016misinterpretations, p. 339].
4. That a small result does not say which assumption failed; a large one says very little.
5. `sampling variability`, and the enumeration of what an interval does **not** cover.
6. That widening an interval is not automatically conservative — demonstrated numerically.
7. The six ASA principles [@asa2016pvalue].
8. A P value as a compatibility summary; four misinterpretations with book analogues.
9. That intervals impose the same dichotomy [@greenland2016misinterpretations, p. 344].
10. `analytic flexibility` as an assumption inside the model.
11. `model checking`; predictive evaluation against data not fitted.

## Terminology to introduce or stabilize

Seven new, two closed from `TODO`. See `../../canon/terminology.md`, Chapter 8 block, and `../../decisions/0015` §8.

### Notation

**None is added.** Permitted: everything Decisions 0013 and 0014 already allow, plus ordinary arithmetic and an interval written as two numbers. **The refusal is stated to the reader**, because Chapter 6 promised the deferred symbols would appear here. Per `../../decisions/0015` clause 2.4.

## Interfaces with other chapters

| Chapter | Line |
|---|---|
| 3 | measurement uncertainty is a different component from sampling variability |
| 4 | the conditions under which ignoring missingness is permitted |
| 5 | sensitivity analysis, promised here, arrives as a model-checking device |
| 6 | the ±0.6 ML spread is repaired here; notation promise answered here |
| 7 | step 4; and estimation cannot repair identification |
| **9** | **combining studies and moving results to new populations** |
| 12 | decision-theoretic robustness |
| 15 | gaming of reported estimates |
| 17 | checking a model after deployment |

## Scope boundary

### Core

- The three-term separation and the estimator properties.
- What a computed number is conditional on.
- What an interval covers and what it does not.
- Thresholds, their misinterpretations, and why intervals do not escape them.
- Analytic flexibility as a model assumption, demonstrated.
- Model checking, including checking against data not fitted.

### Deferred to later chapters

- Pooling, meta-analysis, transport — Chapter 9.
- Decision-theoretic robustness — Chapter 12.
- Gaming — Chapter 15.
- Post-deployment monitoring — Chapter 17.

### Deferred to depth curriculum

- Deriving any estimator or interval.
- Test procedures, distributions, power calculations.
- Likelihood as an object to maximise.
- Regression as a technique.
- Bayesian estimation.
- Multiple-comparison corrections.

## Section architecture

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | The Number You Were Told Not to Trust | 2 | 0.30 |
| 2 | Estimand, Estimator, Estimate | 5 | 1.00 |
| 3 | Everything You Compute Is Conditional on a Model | 6 | 1.20 |
| 4 | How Uncertain, and About What? | 6 | 1.25 |
| 5 | The Threshold Ritual | 6 | 1.25 |
| 6 | Four Defensible Analyses | 5 | 1.05 |
| 7 | Checking the Assumptions You Were Not Interested In | 6 | 1.20 |
| 8 | Cold-Start Practice and Retrieval | 4 | 0.75 |

**40 pages, 8.00 hours.** The largest chapter in the book by pages.

### Drafting constraints

- One sentence per line in manuscript prose.
- **No quotation from `greenland2016misinterpretations` may contain a comparison symbol.** Where the source's point requires one, paraphrase and say so. See `../../sources/greenland2016misinterpretations.md`.
- Matrixx is cited **as reported at** `greenland2016misinterpretations` p. 347, once.
- `asa2016pvalue` is described as the ASA's press release; the article's elaborating paragraphs are never characterised.
- **Every number the chapter reports carries what it is conditional on.**
- The chapter must not present P values as worthless, nor claim the field has agreed a replacement.

## Examples / recurring cases

### The anchor: the eighth recurrence

Chapter 6 supplied a ±0.6 ML spread and said it was justified by nothing. Chapter 8 earns it from 24 heat events.

`case-data.md` freezes: the 24-event forecast record, the interval, the four corrections including the two one-sided ones, the four defensible analyses, and the split-half check.

### Deliberately not used

- Anything Chapter 7 declared not identified. Estimating it would undo the previous chapter.
- Coin flips, urns, or medical trials.
- Any example where the counter-intuitive interval result does not appear.

## Exercise architecture

1. **Opening attempt (§1).** Where should the ±0.6 have come from? Six minutes, unscored.
2. **Three words (§2).** Label three statements as estimand, estimator, or estimate.
3. **What the interval covers (§4).** List what it does not.
4. **The two one-sided corrections (§4).** Compute both; explain the direction.
5. **The threshold (§5).** Four analyses, four verdicts; say what the dichotomy destroyed.
6. **Planted-defect diagnosis (§7).** Five defects.
7. **Cold transfer (§8).** One assigned parallel form.
8. **Retrieval and delayed retest (§8).**

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| "The 95% interval is 0.84 to 2.76, so we're 95% sure the true value is in there" | a reported interval is a probability statement |
| "We widened the interval to be conservative" | wider is safer |
| "P was 0.31, so there's no bias in the forecasts" | non-significant means no effect |
| "We tried several specifications and report the cleanest" | analytic conduct is outside the model |
| "The model fits the last five years to within 2%, so it's checked" | fit is model checking |

### Rubric dimensions

1. Estimand, estimator, and estimate kept apart.
2. An estimator property never attributed to a number.
3. What the interval covers stated, and what it does not.
4. A counter-intuitive direction reasoned about rather than asserted.
5. At least two defensible alternative analyses produced.
6. A threshold verdict refused, with a reason that is not merely contrarian.
7. A model check proposed that could have failed.

## Transfer target

> Given an estimate with an interval, a record permitting several defensible analyses, and a threshold verdict, say what the number is conditional on, produce at least two alternative analyses and their answers, explain what the dichotomy destroyed, and propose a check that could have failed.

### Parallel forms

- **Form A — a grid operator's transformer failure record** (engineering).
- **Form B — a charity's donation-response record** (institutional).

Both supply: a headline estimate with an interval; four defensible analytic choices; a threshold verdict that flips on one of them; and a model whose only check was against the data it was fitted to.

Every prior transfer and contrast domain is excluded. Neither domain is sensitive.

Chapter 8 must not claim durable far transfer.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| A result tests the entire model, including analytic conduct | `greenland2016misinterpretations` p. 339 |
| A P value as a compatibility summary | `greenland2016misinterpretations` p. 339 |
| A small result does not say which assumption failed | `greenland2016misinterpretations` p. 339 |
| The dichotomy, named and condemned | `greenland2016misinterpretations` pp. 339, 348 |
| The P value is not a hypothesis probability | `greenland2016misinterpretations` p. 340 |
| Intervals share the same weaknesses | `greenland2016misinterpretations` p. 340 |
| A reported interval is a range between two numbers | `greenland2016misinterpretations` p. 343 |
| Overlapping intervals; intervals impose the cutoff | `greenland2016misinterpretations` p. 344 |
| Four guidelines | `greenland2016misinterpretations` p. 347 |
| Significance neither necessary nor sufficient; Matrixx **as reported** | `greenland2016misinterpretations` p. 347 |
| The six principles | `asa2016pvalue` |
| The file-drawer mechanism | `asa2016pvalue` |
| The term that does not contain the number of records | `meng2018paradox` p. 687 |
| Calibration and sharpness, reused for checking | `gneiting2007scoring` p. 359 |
| Measurement uncertainty as its own component | `jcgm2012vim` |

### Known gaps constraining the manuscript

1. **Wasserstein and Lazar (2016) not obtained.** Six principles from the ASA press release only.
2. **Silberzahn et al. (2018) not obtained** after four attempts. The chapter demonstrates analytic flexibility on its own anchor and claims nothing about that study.
3. **`greenland2016misinterpretations` read at pp. 337, 339–341, 343–344, 346–348 only.**
4. **Matrixx not read**; reported only.
5. Rubin (1976) still unobtained, as since Chapter 4.
6. The separation of uncertainty into sampling / measurement / structural / model components is **the book's own** assembly across four chapters and is labelled.

### Evidence needed before prose is stable

- SME review of the 24-event forecast record and the SCADA changeover date, coupled to Chapter 1's open Gate 1, **now eight chapters deep**.
- Timed reader pilot against the 8-hour target.
- A second opinion on declining the notation extension, since it reverses a stated promise.

## Failure modes this chapter should prevent

1. The interval covers the uncertainty.
2. A wider interval is more conservative.
3. Significant means real; non-significant means no effect.
4. The P value is the probability the hypothesis is true.
5. The P value tests the hypothesis.
6. Analytic flexibility is a research-ethics topic.
7. Preregistration is the fix.
8. More data fixes it.
9. Fit is model checking.
10. A good estimate rescues a bad identification.
11. More decimal places is more informative.
12. Reporting an interval instead of a P value escapes the ritual.
13. An estimator property belongs to the estimate.

## Open questions

### Before drafting

1. Does the author accept Decision 0015 as proposed, and if not, which clauses change?
2. **Accept the notation refusal, which departs from Chapter 6's stated promise to the reader?**
3. Is declining `confidence` in the book's own prose correct, or over-cautious?
4. How far into regression — recommend "a model whose assumptions are under discussion" and nothing more.
5. Accept the eighth recurrence of the water case?

### Before declaring Chapter 8 verified or frozen

6. Has Wasserstein and Lazar (2016) been obtained?
7. Has Silberzahn et al. (2018) been obtained, or a substitute demonstration sourced?
8. Has `greenland2016misinterpretations` been read past p. 348, and does the power material change anything?
9. Has the 24-event record passed SME review?
10. Does the 40-page / 8-hour budget survive a timed reader pilot?
