# Chapter 6 — Cold-Transfer Rubric

Status: reader-delivery copy. Governed by `spec.md` (Rubric dimensions) and `transfer.md`.

**Do not read this before your response is complete.** It contains the answers.

Score each dimension 0, 1, or 2. Both forms use the same rubric.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Conditioning stated | Probabilities given bare | Some conditioning mentioned | **Every** probability carries what it is conditional on |
| Prior from a base rate | No prior, or a number with no source | A prior taken from the register | Prior taken from the register **and its population named** |
| Ratio computed | Not computed | The two numbers compared loosely | The division done, and read in words |
| Update, both branches | Neither branch worked | One branch worked | Both branches worked, both stated as probabilities |
| The detail that moves nothing | Treated as evidence, or ignored | Noticed as weak | Ratio computed, and *uninformative for this comparison* distinguished from *worthless* |
| Calibration over the record | Column not completed | Column completed | Column completed **and** the pattern stated as an action |
| Calibration vs sharpness | Not addressed | The always-50% forecaster called well calibrated | Called well calibrated **and** useless, with the reason |

## The arithmetic

Check your numbers against these. Small rounding differences do not matter; a number on the wrong side of the prior does.

### Form A — Unit 14

| Step | Value |
|---|---|
| Prior odds for P | **9 : 6 = 1.5 : 1**, about **60%** |
| Population | Intermittent-stall investigations, **vans of this class and age**, seven years, two records no longer held |
| Ratio, dropout recorded | `0.80 ÷ 0.20 = ` **4.0** |
| Posterior, dropout recorded | `1.5 × 4.0 = ` **6 : 1**, about **86%** for P |
| Ratio, no dropout | `0.20 ÷ 0.80 = ` **0.25** |
| Posterior, no dropout | `1.5 × 0.25 = 0.375 : 1`, i.e. about **2.7 : 1 for Q**, about **73%** |
| Driver's hot-day report | `0.65 ÷ 0.60 ≈ ` **1.08**; `1.5 × 1.08 ≈ 1.63 : 1`, about **62%** — from 60% |
| Record | 80% bin → **50%**; 60% bin → **58%**; 40% bin → **42%**; overall **50%** |

### Form B — Marlow Court

| Step | Value |
|---|---|
| Prior odds for R | **7 : 5 = 1.4 : 1**, about **58%** |
| Population | Investigations into sudden rises in reports, **all report types, all blocks**, nine years, three hand-transcribed |
| Ratio, more than 6 above threshold | `0.75 ÷ 0.20 = ` **3.75** |
| Posterior, more than 6 | `1.4 × 3.75 = ` **5.25 : 1**, about **84%** for R |
| Ratio, 6 or fewer | `0.25 ÷ 0.80 ≈ ` **0.31** |
| Posterior, 6 or fewer | `1.4 × 0.31 ≈ 0.44 : 1`, i.e. about **2.3 : 1 for S**, about **70%** |
| Cold-snap detail | `0.70 ÷ 0.65 ≈ ` **1.08**; `1.4 × 1.08 ≈ 1.51 : 1`, about **60%** — from 58% |
| Record | 80% bin → **50%**; 60% bin → **58%**; 40% bin → **42%**; overall **50%** |

## What a strong answer says about the record

The observed column is **50%, 58%, 42%**, against stated 80%, 60%, 40%.

The 60% and 40% bins are well calibrated. The 80% bin is not: twelve statements of *very likely* delivered a coin.

The actionable sentence is not "these forecasts are poor". It is **discount the high-confidence statements toward the middle and take the moderate ones at face value.**

A forecaster who stated **50%** every time would be perfectly calibrated across this record — the overall rate is 18 of 36 — and would have said nothing about any individual case. Calibration is the constraint you have to satisfy. Being informative while satisfying it is the achievement.

## Three answers that look right and are not

**"The test is 80% accurate, so a dropout means 80% it's the loom."** This is the inversion. 0.80 is how expected the dropout is *if* P holds. What you want is how likely P is *given* the dropout, and that depends on the register as well. The answers differ — 86%, not 80% — and they would differ much more with a different prior.

**"The driver's report is worthless."** It is not. It is uninformative **for choosing between P and Q**, because heat plausibly aggravates both. It may be quite useful for something else. Those are different claims and the ratio only speaks to the first.

**"The supervisor is a poor forecaster."** Two of three bins are well calibrated, which is better than most records. The finding is specific to the top of the scale, and overconfidence there is among the most commonly reported patterns anywhere.

## A note on tone

The purpose is not to catch you out. Two dimensions — conditioning stated, and the detail that moves nothing — are the ones this chapter exists to install, and they are the ones most often scored 0 on a first attempt by readers who got every calculation right.

## Post-task self-explanation

Write two or three sentences, before the delayed retest.

> Which of the two supplied observations changed your belief, and what made the other one different?

If your answer is "one was bigger", reread the ratio. If it is "one bore on the comparison and the other did not", you have the chapter.
