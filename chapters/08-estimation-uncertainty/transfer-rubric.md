# Chapter 8 — Cold-Transfer Rubric

Status: reader-delivery copy. Governed by `spec.md` (Rubric dimensions) and `transfer.md`.

**Do not read this before your response is complete.** It contains the answers.

Score each dimension 0, 1, or 2. Both forms use the same rubric.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Estimand stated | Not attempted | A quantity named | Population, comparison, and window all present, with the report's silences marked |
| Estimator not confused with estimate | The number treated as the thing | Noticed a procedure was chosen | Named a specific alternative procedure and what it would change |
| What the interval covers | Not addressed | Says it is uncertainty | States it covers sampling variability **and** lists four things it does not |
| The non-significance sentence | Accepted, or merely called wrong | Called wrong | Called wrong **with the reason** — the estimate is positive and the interval barely straddles zero |
| Four analyses | Fewer than four worked | Four worked | Four worked **and** the estimates set against the verdicts |
| What the dichotomy did | Not addressed | Notes disagreement | Notes the estimates **agree**, and identifies the most defensible analysis |
| A check that could have failed | None proposed, or fit re-proposed | A check proposed | A check proposed **with what result would have embarrassed the model** |

## The arithmetic

### Form A — transformer failures

| Analysis | n | Estimate | Standard error | Roughly how many standard errors? | Crosses? |
|---|---:|---:|---:|---:|---|
| All substations | 30 | **+3.1** | 1.53 | 2.02 | **no** |
| Excluding 4 refurbished | 26 | **+4.2** | 1.57 | 2.68 | yes |
| Complete records only | 19 | **+3.8** | 1.74 | 2.18 | yes |
| Weighted by transformer count | 30 | **+3.5** | 1.50 | 2.34 | yes |

### Form B — donation response

| Analysis | n | Estimate | Standard error | Roughly how many standard errors? | Crosses? |
|---|---:|---:|---:|---:|---|
| All campaigns | 40 | **+1.9** | 1.01 | 1.88 | **no** |
| Excluding 5 appeal overlaps | 35 | **+2.8** | 1.03 | 2.72 | yes |
| Since the migration | 22 | **+2.4** | 1.07 | 2.25 | yes |
| Weighted by size | 40 | **+2.2** | 1.00 | 2.21 | yes |

**The headline analysis is the only one that fails to cross**, and it is the one the report leads with.

## What a strong answer says

### On the estimand

The report never says what population the number is about. Is it *these thirty substations*, or *substations of this type in general*? Is it the mean change per substation, or per transformer? Over what window — the four years, or the state at the end of them?

**A response that noticed the number has no stated population has done the hardest part of item 1.**

### On the interval

It covers how much the average would move if you drew another 30 substations (or 40 campaigns) from the same process.

It does **not** cover: the four refurbishments; the eleven incomplete logging records; that each unit contributes one number regardless of size; the CRM migration or the logging inconsistency changing what the field means; which units came to be in the record at all; and everything about whether the failure or response model behind the 4% or 5% figure is any good.

Four is the required minimum; the record supports more.

### On the non-significance sentence

Three things are wrong with it, and the third is the one that earns full marks.

**"Not significant" does not mean "no evidence".** The estimate is `+3.1` (or `+1.9`), which is not zero. Unless the estimate is exactly the null value, some change is present in the data.

**The interval barely straddles zero.** `−0.04` in Form A; `−0.15` in Form B. The verdict turns on a hair, and the sentence reports it as a settled absence.

**And "so there is no evidence" is an inference from a verdict, not from a number.** The number available — a positive estimate whose interval runs to +6.24 or +3.95 — is entirely consistent with a substantial increase. The verdict discarded it.

### On what the dichotomy did

The four estimates are **+3.1, +3.5, +3.8, +4.2** (Form A) or **+1.9, +2.2, +2.4, +2.8** (Form B).

**They agree.** All positive, all the same order of magnitude, all pointing the same way. Any of them would support the same operational concern.

The four verdicts do not agree, and the disagreement is produced entirely by sample size and by which units were included — not by anything about the world.

**And the arguably most defensible analysis is one of the three that crosses.** Excluding the refurbished substations, or the campaigns that overlapped a national appeal, removes a known and stated contaminant. The headline analysis — the one reported — is the one that includes it.

So the reported verdict is not merely unlucky. It is the verdict produced by the least careful of the four available analyses.

### On the model check

The 4% (or 5%) figure is the model reproducing the data it was fitted to. That could not have come out much otherwise, so it establishes that the arithmetic runs and nothing about whether the model is right.

Acceptable checks that could have failed:

- **Split the record** — before and after the refurbishments, or the migration — and see whether the halves agree.
- **Hold out the most recent units**, fit on the rest, and see where the held-out ones fall.
- **Rerun with one defensible choice changed** and see whether the answer swings.
- **Push an input to a limit** and see whether the model does something impossible.

**Full marks require saying what result would have embarrassed the model.** A check with no failing outcome is not a check.

## Three answers that look right and are not

**"The sample is too small to conclude anything."** Wrong diagnosis. Three of the four analyses cross the threshold on samples of the same order; the problem is not size, it is that a continuous estimate was converted into a verdict.

**"They should have preregistered the analysis."** Nobody could have preregistered a decision about the CRM migration or the logging inconsistency without already knowing about them. Preregistration closes one route and not this one.

**"The 95% interval means we're 95% sure the change is between those values."** The interval is a range between two numbers. The 95% is a property of the procedure across repeated construction.

## A note on tone

Two dimensions — listing what the interval does not cover, and proposing a check that could have failed — are the ones this chapter exists to install, and they are the ones most often scored 0 by readers who handled the arithmetic perfectly.

## Post-task self-explanation

Write two or three sentences, before the delayed retest.

> The report's headline analysis was the only one that failed to cross the threshold, and it was also the least careful of the four. **Was that a coincidence?**

There is no single right answer. A response that notices the question is worth asking, and says what would settle it, has the chapter.
