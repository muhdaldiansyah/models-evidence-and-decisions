# Research 03 — Missingness, Censoring, and Absence

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision.

Cluster R03 of `research-plan.md` §6. Research conducted 2026-08-18.

Sources inspected: `rubin1976missing` (**published abstract only** — see that source note), `censusndtargetpopulation`, `meng2018paradox`.

## 1. Q1 — When the missingness process may be ignored

### What is verified

`rubin1976missing`, published summary, verbatim:

> "When making sampling distribution inferences about the parameter of the data, θ, it is appropriate to ignore the process that causes missing data if the missing data are 'missing at random' and the observed data are 'observed at random' … When making direct-likelihood or Bayesian inferences about θ, it is appropriate to ignore the process that causes missing data if the missing data are missing at random and the parameter of the missing data process is 'distinct' from θ. These conditions are the weakest general conditions under which ignoring the process that causes missing data always leads to correct inferences."

### What Chapter 4 takes from it

One claim, and it is the right one:

> Whether you may ignore the process that caused data to be missing **depends on why they are missing**, and the conditions under which you may ignore it are the *weakest general conditions* under which doing so always works — which is to say, they are conditions, not a default.

A reader who absorbs only that has what Chapter 4 needs. Deleting rows with gaps, or filling them with a column mean, is not a neutral tidying step; it is an assumption about the recording process, made silently.

### The attribution hazard

**The summary uses "missing at random" and "observed at random". It does not contain MCAR, MAR, MNAR as a three-way scheme.** That vocabulary was consolidated later in the literature.

Chapter 4 must therefore either teach the question in plain language, or introduce the three-way scheme without attributing it to this source. Attributing MCAR/MNAR to a 1976 paper whose abstract does not use the terms would be exactly the kind of error this book's source discipline exists to prevent.

**Second hazard.** Only the abstract was verified. No internal locator may be cited, and the reliance is recorded as a gap to close before freeze.

## 2. Q2 — How much vocabulary a core reader needs

Recommendation: **the question, not the taxonomy.**

The reader should be able to ask, of any gap:

> Is whatever caused this value to be absent related to what the value would have been?

Three plain-language cases follow, and they can be taught without importing the acronyms:

- absent for reasons having nothing to do with the value;
- absent for reasons related to something else you *did* record;
- absent for reasons related to **the value itself** — the dangerous one, because nothing in the dataset reveals it.

The third case is the one worth the reader's memory. A meter that fails more often under high flow produces gaps that are systematically the high-flow periods, and no inspection of the surviving readings shows this.

## 3. Q3 — Censoring versus missingness

**Recorded gap: no inspected source defines censoring.**

The distinction Chapter 4 wants is standard and this book cannot currently cite it:

- a **missing** observation carries no information about its value;
- a **censored** observation carries partial information — you know it lies beyond a bound, because the recording process stopped there.

A logger that saturates at its maximum does not lose the reading; it tells you the value was at least the maximum. Treating that as missing throws away real information; treating it as the maximum understates the value. Both are wrong in known directions.

**Disposition.** Chapter 4 may teach this by worked demonstration on the anchor, where the reader can see both errors arithmetically, and must not present a citation for the distinction. This mirrors the disposition adopted for representational aggregation in `decisions/0009` clause 6.3.

## 4. Q4 — Absence, and why it is the worst case

Distinct from missingness, and more consequential.

`censusndtargetpopulation` §1.1 supplies the sourced half: the standard uses `target population` for the units about which inference is intended, and distinguishes target-population membership from the status of a sampled unit. Something decides which units are candidates for appearing **before** any measurement happens.

A unit that was never eligible does not appear as a gap. It produces no row, no null, no flag. There is nothing in the dataset to notice.

`meng2018paradox` supplies the reason this matters more than it looks: p. 685's ρ_{R,X} is the correlation between the value and *whether the unit was recorded*. Absence is R_j = 0, and if absence is related to the value, the data-quality term is non-zero however complete the dataset appears.

### The asymmetry Chapter 4 should build on

| Kind of gap | Visible in the dataset? | Detectable from the dataset alone? |
|---|---|---|
| Missing value in an existing record | Yes — a null, a blank, a flag | Its *pattern* is visible; its *cause* is not |
| Censored observation | Sometimes — often disguised as a value | Only if the bound is documented |
| Unit never eligible or never captured | **No** | **No** |

The bottom row is why Chapter 4 exists. Everything a reader can do by staring at their data harder addresses the top two rows. The third requires going outside the dataset and asking who made it and what they were required to record.

## 5. Q5 — What can be detected from the data alone

Consolidated answer, and the chapter's practical takeaway:

- **Patterns of missing values**: yes, from the data.
- **Why those values are missing**: no, not from the data.
- **Censoring**: only if the bound is documented, or a suspicious pile-up at a limit is noticed.
- **Units that never entered**: never from the data. Only from the provenance.

This is why Chapter 4's method is not a data-inspection method. It is an interview with whoever built the dataset.

## 6. Cautions — claims the manuscript must NOT make

1. Do not attribute MCAR / MAR / MNAR to `rubin1976missing`. The verified summary does not use that scheme.
2. Do not cite any internal locator in `rubin1976missing`. Only the abstract was verified.
3. Do not present a citation for the censoring/missingness distinction. None was obtained.
4. Do not teach imputation, deletion rules, weighting, or selection models. Chapter 8.
5. Do not teach survival analysis or time-to-event methods.
6. Do not say a pattern of missingness reveals its cause. It does not.
7. Do not use `censusndtargetpopulation` beyond eligibility and target-population membership.
8. Do not imply that a dataset with no nulls has no gaps. That is the chapter's central irony and must be stated the other way round.

## 7. Verdict on the stop condition

`research-plan.md` §6 requires that the reader be tellable what question to ask about a gap and why the answer matters.

**Met.** The question:

> Is whatever caused this to be absent related to what it would have been?

And the reason it matters: if yes, no amount of care with the records you have will repair it, and if the absence is at the eligibility or capture stage, nothing in the dataset will even tell you it happened.

## 8. Unresolved author decisions

1. Is the three-way missingness scheme named, given it cannot be attributed to the verified source?
2. Is `censoring` taught, given it cannot be cited?
3. Is the visible/detectable table given to the reader, or is it authoring scaffolding?
4. How hard does the chapter press the claim that Chapter 4's method is an interview rather than an analysis?
5. Is `rubin1976missing` cited at all in the manuscript, given it is abstract-verified — or is the claim carried in the book's own voice with the source noted only in `spec.md`?

Decision 5 is a source-discipline judgement. Citing an abstract-verified source in manuscript prose is defensible if the citation carries only what the abstract states, and it is the first time this book has done so.
