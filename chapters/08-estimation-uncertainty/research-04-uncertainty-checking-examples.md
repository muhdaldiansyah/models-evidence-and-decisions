# Research 04 — Uncertainty, Checking, and the Chapter's Own Examples

Cluster R04 of `research-plan.md`. Closed.

Sources: `greenland2016misinterpretations` pp. 343–344 read directly; `jcgm2012vim`, `meng2018paradox`, and `gneiting2007scoring` as already verified in Chapters 3, 4, and 6.

## 1. The anchor, and why it is the right one

Chapter 7 ended with **not identified**. Chapter 8 cannot estimate the pump effect without undoing the previous chapter, and must not.

But the book left a defect open two chapters ago, in terms:

> "**The spread is supplied and is not derived from anything.** That is the point of the demonstration: running the projection ten thousand times will produce a stable answer about a spread nobody has justified." — `../06-probability-simulation/case-data.md`

Chapter 6 put ±**0.6 ML** on each day's demand, used it to compute a breach probability of about **77%**, and said plainly that the spread was invented.

**Chapter 8's job is to earn that spread from records.** The chapter repairs a defect the book itself flagged, which is a stronger motivation than a new case and requires no new physical facts.

## 2. The record

The utility has forecast-versus-actual seven-day demand for **24 past heat events**.

Forecast error is defined as `actual − forecast`, in ML over the seven days.

| | Value |
|---|---:|
| Events | **24** |
| Mean error | **+1.8 ML** |
| Standard deviation of errors | **2.4 ML** |

Two findings, and the first is the one nobody looked for.

**The forecasts run low.** Mean error is `+1.8`, not zero. Chapter 6's symmetric spread assumed a centred error and there is no such thing here.

**The dispersion is far larger than assumed.** Chapter 6's ±0.6 ML per day, independent across seven days, implies a standard deviation on the weekly total of about **0.92 ML**. The record says **2.4 ML** — about **2.6 times** larger.

## 3. The interval, and what it covers

Standard error of the mean error: `2.4 ÷ √24 = 0.49 ML`.

An approximate 95% interval estimate for the mean forecast error: **`+0.84` to `+2.76` ML**.

**What that interval covers:** how much the *average* of 24 past errors would move if you drew another 24 events from the same process.

**What it does not cover**, and the list is the whole of Part I:

- that the demand forecast is conditional on **no new action** (Chapter 1), so a conservation request breaks it;
- that one zone's figure is a **subtraction residual** containing leakage elsewhere and the utility's own use (Chapter 4);
- that the storage model has **no spill term** and grows water without limit under low demand (Chapter 5);
- that the 24 events are the ones that were logged, in the configuration the network then had.

`meng2018paradox` p. 687, already verified in Chapter 4, is the sharpest available statement of the general point: what matters for a defective dataset is a term whose expression does not contain the number of records at all.

**The interval is a statement about sampling. It is silent about everything else, and it looks like a statement about the answer.**

## 4. The correction, and the result that surprises

Chapter 6's breach condition: end-of-week storage falls below 4.5 ML exactly when weekly demand exceeds **64.2 ML**.

Four calculations, all run and checked:

| Assumption | Weekly demand | P(breach) |
|---|---|---:|
| Chapter 6 as written — supplied spread, no offset | mean 64.9, sd 0.92 | **77%** |
| Fix the spread only — wider, still centred | mean 64.9, sd 2.4 | **62%** |
| Fix the offset only — shifted, Chapter 6's spread | mean 66.7, sd 0.92 | **over 99%** |
| Fix both | mean 66.7, sd 2.4 | **85%** |

**Widening the interval moved the answer down, from 77% to 62%.**

That is the demonstration this cluster exists to produce, and it refutes a belief most analysts hold without examining it: that admitting more uncertainty is the safe direction.

The reason is visible once stated. The threshold sits **below** the central forecast — the utility is already expected to breach. Spreading the distribution moves mass across the threshold in the safe direction, so a wider interval reports a *lower* chance of trouble.

**Correcting one thing and not the other was worse than correcting neither.** The honest number is 85%, and it requires both corrections; either alone misleads, and one of them misleads in the reassuring direction.

## 5. The four defensible analyses

The same 24 records support several analyses, each of which a competent person would defend.

| Analysis | n | Mean error | SD | Standard error | Crosses the conventional threshold? |
|---|---:|---:|---:|---:|---|
| All events | 24 | **+1.8** | 2.4 | 0.49 | yes |
| Excluding 3 events with a conservation request in force | 21 | **+2.4** | 2.3 | 0.50 | yes |
| Only events since the new SCADA installation | 14 | **+1.1** | 2.6 | 0.70 | **no** |
| Weighted by event length | 24 | **+2.0** | 2.5 | 0.51 | yes |

Every one is defensible. Excluding conservation events is arguably *required*, since Chapter 1 established the forecast is conditional on no new action. Restricting to post-SCADA events is arguably required too, since the measurement process changed. They cannot both be done without dropping to a handful of events.

**Three of the four cross the threshold and one does not.** Under the ritual, the same records support both "the forecasts are biased low" and "no evidence of bias" depending on a choice nobody wrote down in advance.

**And the four estimates do not disagree.** They run `+1.1`, `+1.8`, `+2.0`, `+2.4` — all positive, all the same order, all pointing the same way. The disagreement is manufactured entirely by the dichotomy, which is the source's point at [@greenland2016misinterpretations, p. 348] arriving on the anchor.

This is the chapter's analytic-flexibility demonstration. **`../research-plan.md` records that Silberzahn et al. (2018) could not be obtained**; the chapter demonstrates the phenomenon on its own case and makes no claim about that study.

## 6. Model checking on the anchor

Two checks the chapter can run, both cheap.

**Check the assumption the interval depends on.** The interval treats the 24 errors as exchangeable draws. Split them: the 14 post-SCADA events have mean `+1.1`, the 10 earlier ones have mean `+2.78`. That is a large difference and it says the errors are not draws from one stable process.

Verification: `(24 × 1.8 − 14 × 1.1) ÷ 10 = (43.2 − 15.4) ÷ 10 = 2.78`.

**Check against something the model was not fitted to.** Chapter 5 established that reproducing data a model was built from is weak evidence. The available honest check is to hold out the most recent events, fit on the rest, and see how the interval performs — which is the same discipline Chapter 6 applied to forecasts, and `gneiting2007scoring` p. 359's calibration-and-sharpness framing applies without modification.

**The second check is the one the utility has never done**, and it is the chapter's practical recommendation.

## 7. Prohibitions for the manuscript

- No test procedure, distribution, power calculation, or estimator derivation.
- No claim that any of these values is typical of water utilities.
- No claim that any of the four analyses is the right one.
- No presentation of preregistration as a solution; it is one device with limits.
- No claim about Silberzahn et al. (2018) or about the replication literature as a literature.
- No re-estimation of anything Chapter 7 declared not identified.
- The Supreme Court case is cited **as reported at** `greenland2016misinterpretations` p. 347.
- No recommendation about what the utility should do — Chapter 11.

## 8. Stop condition

Met. The record is specified; the interval and its coverage are stated; the four corrections are computed and the counter-intuitive direction confirmed; four defensible analyses are specified with their threshold verdicts; two model checks are specified and the split-half arithmetic verified.
