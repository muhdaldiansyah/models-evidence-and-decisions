# Chapter 7 — Cold-Transfer Rubric

Status: reader-delivery copy. Governed by `spec.md` (Rubric dimensions) and `transfer.md`.

**Do not read this before your response is complete.** It contains the answers.

Score each dimension 0, 1, or 2. Both forms use the same rubric.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Target quantity stated | Not attempted | A quantity named | Treatment, **comparison**, population, variable, window, and summary all present |
| Intervention specified | Treated as one thing | Noticed that it covers several | Named which options could differ **and in which direction** |
| Comparisons computed | Fewer than three | Three computed | Three computed **and** each paired with what it assumes |
| Exchangeability | Not addressed | "Selection bias" asserted | The allocation rule used to explain **why the cross-section has the sign it has** |
| Positivity | Missed | Noticed the constrained cases | Named as structural, **and** the more-data question answered correctly with a reason |
| Target trial | Not written | Written | Written, infeasibility explained specifically, **and used to name the assumption** |
| Verdict | Absent, or "more research needed" | Says the claim is unproven | Names what is unestablished, which assumption would change it, and what to go and get |

## The arithmetic

### Form A — guarding retrofit

| Comparison | Arithmetic | Result |
|---|---|---:|
| Cross-section, after | `3.6 − 1.8` | **+1.8** — retrofit looks **worse** |
| Before and after, retrofitted | `3.6 − 5.4` | **−1.8** |
| Difference in differences | `(3.6 − 5.4) − (1.8 − 2.1)` | **−1.5** |

### Form B — bus lanes

| Comparison | Arithmetic | Result |
|---|---|---:|
| Cross-section, after | `30.2 − 21.0` | **+9.2** — lanes look **worse** |
| Before and after, with lanes | `30.2 − 34.5` | **−4.3** |
| Difference in differences | `(30.2 − 34.5) − (21.0 − 21.8)` | **−3.5** |

**A response that produced only one of the three has missed the point of item 2**, whichever one it produced.

## What a strong answer says

### On the cross-section

The treated units were selected for being the worst. They started far behind — 5.4 against 2.1 in Form A, 34.5 against 21.8 in Form B — and improving without fully closing that gap leaves them still behind afterwards.

So the cross-sectional comparison **has to** come out positive whenever a programme is targeted at the worst cases and does not completely fix them. It is not evidence that the treatment harms; it is arithmetic about where the two groups started.

**A strong answer also notes that targeting the worst cases is not a mistake.** It is ordinary, defensible resource allocation. The organisation did nothing wrong; its allocation rule simply destroys the assumption the naive comparison needs.

### On the concurrent change

The untreated group moved without receiving anything — by 0.3 in Form A, 0.8 in Form B. That is the visible trace of the glove standard, or the signal retiming.

So the whole of the treated group's improvement cannot be attributed to the treatment.

### On difference in differences

**Full marks require noticing that this one is not safe either**, and saying why.

It assumes the treated units would have moved like the untreated ones had nothing been done to them. They were selected for being extreme, and units observed at their worst tend to be less bad next time regardless of what anybody does. Some unknown share of the improvement is that, and nothing in the four numbers separates it.

The difference-in-differences comparison is the best of the three because its assumption can be **named**. That is not the same as being right, and a response that presented it as the answer has been caught by the trap the form is built around.

### On the constrained cases — the item most often missed

Form A: the four adjustable-bed lines cannot take the standard retrofit, so none was ever retrofitted.
Form B: the four historic streets are too narrow for a lane, so none ever got one.

In both, the units the decision-maker most cares about have **zero** probability of having been treated in this record. Not few — zero.

**And the answer to the more-data question is no.** The failure is structural: those units do not get treated *because of what they are*, so more years and more units drawn from the same world contain more instances of the same exclusion. The missing comparison never accumulates.

A response that said "the sample is too small" has diagnosed the wrong problem.

### On the multiple versions

Form A: two-hand controls can be defeated when cycle time is tight, so option 3 may perform quite differently from a fixed barrier.
Form B: a bus-and-taxi lane on a busy corridor can carry enough taxis that buses queue in it, so option 3 may be close to no lane at all.

The consequence is that the treated group is not a group that received one treatment. It received an unrecorded mixture, and the computed effect is an average over that mixture whose composition nobody knows — and which will not match whatever the remaining units are given.

### On the target trial

Randomly assign units to treatment or not; follow for the programme period; compare the outcome.

Infeasible for reasons the response should state specifically: the number of units is small; you cannot withhold a safety retrofit, or a street improvement subject to public consultation, from those who need it; and the units are not interchangeable in what they carry.

**And the payoff.** Writing it names the assumption the observational analysis is being asked to carry — that treatment was assigned as though at random — which the supplied allocation rule flatly contradicts.

## Three answers that look right and are not

**"The difference-in-differences estimate shows the programme worked."** The most common full-marks-looking answer. It is defensible only under an assumption that the allocation rule gives specific reason to doubt.

**"The sample is too small to draw conclusions."** Wrong diagnosis. Every problem in the form survives any sample size. Saying this means the identification and estimation questions have been merged.

**"Correlation does not imply causation."** True, and it earns nothing. The work is naming which condition fails, why, and what would change it.

## A note on tone

Two dimensions — positivity, and using the target trial rather than merely writing it — are the ones this chapter exists to install, and they are the ones most often scored 0 by readers who handled everything else well.

## Post-task self-explanation

Write two or three sentences, before the delayed retest.

> Of the problems you found, which one would still be there if the organisation had ten times the data, and how would you explain that to somebody who wanted to commission more?

If your answer is "all of them", you have the chapter.
