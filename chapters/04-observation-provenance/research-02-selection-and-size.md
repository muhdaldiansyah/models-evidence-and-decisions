# Research 02 — Selection, Coverage, and Why Size Does Not Save You

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision.

Cluster R02 of `research-plan.md` §5. Research conducted 2026-08-18.

Sources inspected: `meng2018paradox` (pp. 685–687), `davern2013nonresponse`.

## 1. Q1–Q2 — What determines the error, and whether more data reduces it

### The decomposition

`meng2018paradox` p. 685 gives the difference between a sample average and a population average as the **product of three terms**:

1. **data quality** — ρ_{R,X}, the correlation between the value and whether the unit was recorded;
2. **data quantity** — √((N−n)/n), where N is the population size;
3. **problem difficulty** — σ_X, the standard deviation of the quantity.

Three factors, multiplied. That structure alone carries most of what Chapter 4 needs, because a product is zero only if a factor is zero — and no amount of increasing one factor compensates for another.

### The counterintuitive result

`meng2018paradox` p. 685, insight (I): probabilistic sampling "ensures high data quality by controlling ρ_{R,X} at the level of N^{−1/2}".

Insight (II) states what happens when that control is lost: "When we lose this control, the impact of N is no longer canceled by ρ_{R,X}, leading to a *Law of Large Populations* (LLP), that is, our estimation error, relative to the benchmarking rate 1/√n, increases with √N".

Read plainly: in a designed random sample, the recording process is arranged so that whether a unit is recorded is unrelated to its value, and the population size drops out. Without that arrangement, **the error scales with the size of the population you are drawing from.**

p. 687 restates the practical consequence as a proposed shift in what analysts attend to:

> from `Standard Error ∝ σ/√n`
> to `Relative Bias ∝ ρ√N`

The first falls as you collect more. The second does not contain *n* at all.

### The empirical anchor

`meng2018paradox` p. 685: CCES estimates for the 2016 US presidential election "suggest a ρ_{R,X} ≈ −0.005 for self-reporting to vote for Donald Trump. Because of LLP, this seemingly minuscule data defect correlation implies that the simple sample proportion of the self-reported voting preference for Trump from 1% of the US eligible voters, that is, n ≈ 2,300,000, has the same mean squared error as the corresponding sample proportion from a genuine simple random sample of size n ≈ 400, a 99.98% reduction of sample size (and hence our confidence)."

**2.3 million records worth 400.** A correlation of one two-hundredth destroyed 99.98% of the effective sample.

### The paradox

`meng2018paradox` p. 686: "without taking data quality into account, population inferences with Big Data are subject to a *Big Data Paradox*: the more the data, the surer we fool ourselves."

And the observed pattern that motivates it, same page: "on average, the larger the state's voter populations, the further away the actual Trump vote shares from the usual 95% confidence intervals based on the sample proportions."

Not merely wrong. **Confidently wrong, and more confidently wrong where the population was larger.**

### The structural parallel worth noting

Chapter 3 established, from metrology, that more measurements improve precision and do nothing for trueness.

Chapter 4 establishes, from statistics, that more records shrink the sampling-variability term and do nothing for the data-quality term.

Both chapters teach the same shape: **there is a quantity that effort reduces, and a quantity that effort does not touch, and the second usually decides the answer.** Each is independently established in its own field; the observation that they rhyme is the book's own.

## 2. Q3 — Is a high coverage or response rate reassuring?

**No, and this is a separate, independently sourced correction.**

`davern2013nonresponse`: "Response rates lack validity in that there is not even a moderate correlation with nonresponse bias."

The article reports (paraphrase, to be re-checked before quoting) a case in which a less aggressive protocol producing roughly 40% fewer responses "would not have produced one statistically different result", and draws on Groves (2006) for evidence of substantial variation in bias across estimates within a single survey at a single response rate.

**Note what this does and does not say.** It does not say nonresponse is harmless. It says the response rate — the number everyone reports — is a poor indicator of how much damage nonresponse did.

That is consistent with `meng2018paradox`: what matters is ρ_{R,X}, the *relationship* between being recorded and the value. A response rate reports only how many were recorded, and says nothing about who.

## 3. Q4 — Is a dataset biased as a whole?

**No.** `davern2013nonresponse`: nonresponse bias "is an estimate level measure and it cannot be easily summarized by a survey level proxy measure."

Bias attaches to a **quantity being estimated**, not to a dataset. The same records can support one quantity well and another badly, because the recording process may be unrelated to one variable and strongly related to another.

This is directly consistent with ρ_{R,X} carrying an *X* subscript: the data-quality term is defined per variable.

**Implication for Chapter 4.** The reader must be taught to ask "is this dataset trustworthy **for this quantity**?", and to reject the unqualified form of the question — which is the same move Chapter 3 made about validity, and Chapter 1 about adequacy.

## 4. Q5 — What can be said at core depth without the mathematics

Recommended, all sourced:

- Being recorded is something that happens to a unit, and it can depend on the unit's value.
- Whether that dependence exists matters more than how many records you have.
- A designed random sample is valuable precisely because it *arranges* for that dependence to be absent.
- Without that arrangement, more records do not help, and error grows with the size of the population.
- A high coverage or response rate is not evidence that the dependence is absent.
- Trustworthiness is per quantity, not per dataset.

**Not recommended at core depth:** the identity, the derivation, the data defect index, ρ as a computed number, or any formula.

The 2016 figure — 2.3 million behaving like 400 — should be given, because it is memorable, empirical, and exactly quotable. It must be attributed to that specific dataset and question.

## 5. Cautions — claims the manuscript must NOT make

1. Do not say "big data is bad". The paradox is conditional on *not taking data quality into account* (`meng2018paradox` p. 686).
2. Do not present the 400-equivalent as a general property of large datasets. It is one empirical estimate for one question in one study.
3. Do not describe ρ ≈ −0.005 as a bias, a rate, or a percentage. It is a correlation.
4. Do not write the identity or use the notation.
5. Do not say response rates do not matter. They are a poor *indicator of bias*, which is different.
6. Do not cite Groves (2006); it was not read, and is reported here via `davern2013nonresponse`.
7. Do not extend survey-methodology findings to administrative records as though automatic. Meng's framing explicitly covers non-probabilistic data; Davern's does not.
8. Do not import weighting, calibration, or post-stratification as remedies. Chapter 8.

## 6. Verdict on the stop condition

`research-plan.md` §5 requires the central counterintuitive claim and the response-rate correction both stated and sourced.

**Met on both.**

> More records do not fix a selection problem. Where being recorded is related to the value, the error grows with the size of the population you drew from, not shrinks with the number you collected.

> A high response or coverage rate is not evidence that a dataset is trustworthy, because it counts how many were recorded and says nothing about who.

## 7. Unresolved author decisions

1. Is the Meng result given with its numbers (2.3 million ≈ 400) or qualitatively?
2. Is `data defect correlation` named, or is the idea carried as "whether being recorded is related to the value"?
3. Is the three-factor structure shown as three factors, without notation, or not shown at all?
4. Is the parallel with Chapter 3's trueness lesson made explicit?
5. Does the chapter use the 2016 election, which is politically loaded, or is a neutral illustration substituted with the source cited for the principle?

Decision 5 needs care. The election example is the source's own and is the most memorable thing in the chapter; it is also the kind of example that can distract a reader into arguing about politics instead of about recording processes.
