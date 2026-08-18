# Chapter 8 Estimation Case Data

Status: drafting freeze. Extension of the Chapter 1–7 case-data files, all of which remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility.

## What this file adds

Chapter 8 introduces **no new case**. It repairs a defect the book itself flagged in Chapter 6.

`../06-probability-simulation/case-data.md` supplied a spread of ±**0.6 ML** on each day's demand and said, in terms, that the spread "is supplied and is not derived from anything." Chapter 6 used it to compute a breach probability of about **77%** and told the reader the stability of that number was about the arithmetic rather than about the world.

**Chapter 8 goes and gets the records.**

It adds a forecast-error record, four defensible analyses of it, and the corrected probabilities.

## Carried forward

| From | Item |
|---|---|
| Ch 1 | Seven daily forecasts **9.0, 9.3, 9.6, 9.5, 9.4, 9.2, 8.9**, totalling **64.9 ML**; conditional on no new action |
| Ch 1 | Input **8.4 ML/day**; starting storage **9.9 ML**; reserve **4.5 ML** |
| Ch 6 | Breach when weekly demand exceeds **64.2 ML** |
| Ch 6 | Supplied spread ±**0.6 ML/day**, implying a weekly standard deviation of about **0.92 ML** |
| Ch 6 | P(breach) under that spread: about **77%** |
| Ch 7 | The pump-upgrade effect is **not identified**; Chapter 8 does not estimate it |

## The forecast-error record

The utility holds forecast-versus-actual seven-day demand for **24 past heat events**.

Forecast error is `actual − forecast`, in ML across the seven days.

| | Value |
|---|---:|
| Events | **24** |
| Mean error | **+1.8 ML** |
| Standard deviation of errors | **2.4 ML** |
| Standard error of the mean | `2.4 ÷ √24 = ` **0.49 ML** |
| Approximate 95% interval estimate for the mean error | **+0.84 to +2.76 ML** |

Two findings, and the first is the one nobody looked for.

**The forecasts run low.** The mean error is `+1.8`, not zero. Chapter 6's symmetric spread assumed a centred error, and there is none.

**The dispersion is far larger than assumed.** Chapter 6's spread implies about **0.92 ML** on the weekly total; the record says **2.4 ML** — about **2.6 times** larger.

## The four corrections

| Assumption about weekly demand | Mean | SD | P(breach) |
|---|---:|---:|---:|
| Chapter 6 as written | 64.9 | 0.92 | **77%** |
| Fix the spread only | 64.9 | 2.4 | **62%** |
| Fix the offset only | 66.7 | 0.92 | **over 99%** |
| Fix both | 66.7 | 2.4 | **85%** |

**Widening the interval moved the answer down.**

The reason is that the breach threshold of **64.2 ML** sits **below** the central forecast of 64.9. A breach is already the central expectation, so spreading the distribution moves mass across the threshold in the reassuring direction.

**Correcting one thing and not the other was worse than correcting neither**, and the one-sided correction that most analysts would reach for first — a wider interval — is the one that misleads reassuringly.

The honest figure is **85%**, conditional on the Chapter 1 forecast, the 24-event error record, and the storage model as it stands.

## The four defensible analyses

The same 24 records support several analyses. Each would be defended by a competent person.

| Analysis | n | Mean error | SD | Standard error | Crosses the conventional threshold? |
|---|---:|---:|---:|---:|---|
| All events | 24 | **+1.8** | 2.4 | 0.49 | yes |
| Excluding 3 events with a conservation request in force | 21 | **+2.4** | 2.3 | 0.50 | yes |
| Only the 14 events since the new SCADA installation | 14 | **+1.1** | 2.6 | 0.70 | **no** |
| Weighted by event length | 24 | **+2.0** | 2.5 | 0.51 | yes |

Excluding conservation events is arguably **required**, since Chapter 1 established the forecast is conditional on no new action. Restricting to post-SCADA events is arguably required too, since the measurement process changed. Doing both leaves a handful of events.

**Three cross the threshold; one does not.** The same records support "the forecasts are biased low" and "no evidence of bias", depending on a choice nobody wrote down in advance.

**And the four estimates do not disagree**: `+1.1`, `+1.8`, `+2.0`, `+2.4` — all positive, all the same order, all pointing the same way. The disagreement is manufactured entirely by the dichotomy.

## The split-half check

Splitting the 24 events at the SCADA changeover:

| Group | n | Mean error |
|---|---:|---:|
| Since the new SCADA | 14 | **+1.1** |
| Before it | 10 | **+2.78** |

Arithmetic: `(24 × 1.8 − 14 × 1.1) ÷ 10 = (43.2 − 15.4) ÷ 10 = 2.78`.

**The interval in the table above treats all 24 errors as draws from one stable process, and this check says they are not.** The check is two subtractions and a division; nobody had run it.

## Prohibited interpretations

Do not write or imply that:

- any of these values are typical of water utilities, or that 24 events is an adequate record;
- the 85% is correct in any sense beyond being conditional on the stated assumptions;
- any of the four analyses is the right one;
- the split-half result establishes that the SCADA change caused the difference — that is a Chapter 7 claim and this record cannot support it;
- the interval covers anything beyond sampling variability;
- more heat events would repair the Chapter 4 residual, the Chapter 5 missing spill term, or the Chapter 1 conditionality;
- preregistering the analysis would have made any of the four choices correct;
- the pump-upgrade question has become answerable;
- any of this tells the utility what to do.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME should review the 24-event forecast record, the plausibility of a systematic low bias of that size, and the SCADA changeover as a reason to split the record.

**These facts inherit Chapter 1's open Gate 1, now eight chapters deep.** Eight case-data files now extend one anchor whose operating story has never been reviewed by a domain expert. This is a standing risk and remains a book-level decision the author has not yet made.
