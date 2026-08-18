# Chapter 8 Bounded Research Plan

Status: working control. Governs the four `research-0N-*.md` dossiers.

Bounded in the same sense as Chapters 2–7: four clusters, each with a stop condition, each closing before the next opens.

## Standing rules, carried forward

> **Every locator must come from reading the document directly. A fetch summary is a lead, not evidence.**
>
> **Quote only prose that survives text extraction cleanly.**

The first rule dates from the fabricated-quotation incident recorded at `../../sources/sterman2002models.md`. The second was adopted in Chapter 7 when italic math variables were found to drop silently from extracted text.

**The second rule is under more strain in this chapter than in any before it.**

`greenland2016misinterpretations` is a paper about inequalities, and text extraction mangles every one of them. `P ≤ 0.05` extracts as `P B 0.05` or `P £ 0.05`; `P > 0.05` extracts as `P [ 0.05`. A quotation assembled from the extraction would contain characters the source does not print, and in a paper whose entire subject is the difference between *above* and *below* a cut-off, that is not a cosmetic problem.

**Consequence, applied throughout:** no quotation in this chapter contains a comparison symbol. Where the source's point requires one, the manuscript paraphrases with a locator and says it is paraphrasing.

## Cluster R01 — Estimand, estimator, estimate

### Questions

1. What closes the two canon entries that have carried `TODO` since Chapter 1?
2. What properties does an estimator have, and which of them are worth a general reader's attention?
3. Where does `consistency` collide with Chapter 7, and how is the collision handled?

### Sources

`fda2021estimands` (already verified, Chapter 1 and Chapter 7), `../07-targets-identification/research-01-targets-and-estimands.md` for the hierarchy already adopted, `greenland2016misinterpretations` for how estimates and intervals are discussed.

### Stop condition

Stop when the three-term separation is stateable without notation and the collision is documented.

### Deliverable

`research-01-estimand-estimator-estimate.md`.

## Cluster R02 — What a computed number is conditional on

### Questions

1. Is there a published statement that a statistical result tests the whole model rather than the hypothesis of interest?
2. Does any source include the conduct of the analysis among those assumptions?
3. What follows for uncertainty intervals?

### Sources

`greenland2016misinterpretations` printed pp. 339–340, 343–344.

### Stop condition

Stop when the spine claim is recorded verbatim with its locator, and when it is established that the source itself puts analytic conduct inside the model's assumptions rather than treating it as a separate topic.

### Deliverable

`research-02-what-a-number-is-conditional-on.md`.

## Cluster R03 — Thresholds

### Questions

1. What is the authoritative position of the discipline's professional body?
2. What are the documented misinterpretations, in the source's own words?
3. What does the literature recommend instead, and how strongly?
4. Is there a non-academic instance of the point that a general reader would find hard to dismiss?

### Sources

`asa2016pvalue`; `greenland2016misinterpretations` printed pp. 339–341, 343–344, 346–348.

### Stop condition

Stop when the six ASA principles are recorded verbatim, when at least four misinterpretations are recorded with locators, and when the source's own closing characterisation of the dichotomy is recorded.

**Do not proceed into test procedures, distributions, or power calculations.** Recording that power exists and is widely misinterpreted is sufficient.

### Deliverable

`research-03-thresholds.md`.

## Cluster R04 — Uncertainty, checking, and the chapter's own examples

### Questions

1. What does an interval estimate cover, and what does it not?
2. What already exists in the book about uncertainty that is not sampling variability?
3. What must the anchor supply, and does the arithmetic work?

### Sources

`greenland2016misinterpretations` pp. 343–344; `jcgm2012vim` and `meng2018paradox` as already verified in Chapters 3 and 4; `gneiting2007scoring` as already verified in Chapter 6.

### Stop condition

Stop when the anchor's four defensible analyses are specified numerically, when the two one-sided corrections are computed, and when it is confirmed that widening the interval alone moves the answer in the unexpected direction.

### Deliverable

`research-04-uncertainty-checking-examples.md`.

## What this plan does not attempt

- **Deriving any estimator.** No maximum likelihood, no least squares, no method of moments.
- **Any test procedure.** No t-test, no chi-squared, no worked hypothesis test.
- **Distributions as objects.** Named at most.
- **Power calculations.** Recorded as widely misinterpreted; not taught.
- **Bayesian estimation.** Chapter 6 declined the frequency/belief argument; this chapter does not reopen it.
- **Regression as a technique.** It appears as a model whose assumptions are under discussion.
- **Multiple-comparison corrections.** Depth curriculum.
- **The replication-crisis literature as a literature.** The chapter uses two sources and characterises nothing beyond them.
- **Meta-analysis and pooling** — Chapter 9.
- **Decision-theoretic robustness** — Chapter 12.

## Known unobtainable

- **Silberzahn et al. (2018)**, "Many Analysts, One Data Set", the standard demonstration that independent teams analysing the same data reach different answers, could not be retrieved from four sources. **The chapter demonstrates analytic flexibility on its own anchor instead and makes no claim about that study.**
- **Wasserstein and Lazar (2016)**, the American Statistician article itself, could not be retrieved. What was obtained is the ASA's own press release of 7 March 2016, which prints the six principles in full. Cited as the press release; the elaborating paragraphs in the article are **not** characterised.
- **Simmons, Nelson and Simonsohn (2011)** was not sought after the two failures above; the chapter does not need a third source for the same point.
- **Rubin (1976)** remains unobtained, as since Chapter 4.
