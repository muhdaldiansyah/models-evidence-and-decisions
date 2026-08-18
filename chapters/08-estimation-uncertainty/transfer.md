# Chapter 8 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0015-chapter8-estimation-terminology-and-notation.md`.

## Transfer target

Per `spec.md`:

> Given an estimate with an interval, a record permitting several defensible analyses, and a threshold verdict, say what the number is conditional on, produce at least two alternative analyses and their answers, explain what the dichotomy destroyed, and propose a check that could have failed.

## The changed task shape

Chapter 7 asked for a **verdict**. Chapter 8 asks the reader to **rewrite somebody else's summary**.

That is deliberately the most concrete output the book has asked for. The chapter's failure mode is a reader who agrees with everything and writes the same report next week, because criticising a threshold is easy and producing the replacement is not. Item 7 requires the replacement.

The forms therefore hand over a written summary containing four distinct defects, in the register such summaries are actually written in, and ask for a better one.

## Form design

Both forms supply the same five things, in the same order:

1. **A written summary** containing a point estimate, an interval, a non-significance verdict with an inference drawn from it, and a fit-to-fitting-data model check.
2. **A headline analysis whose interval barely straddles zero** — `−0.04` in Form A, `−0.15` in Form B.
3. **Three further defensible analyses**, each supplied with its own estimate and standard error, all of which cross the conventional threshold.
4. **A stated contaminant** in the headline analysis that the alternatives remove.
5. **A model whose only check was against the data it was fitted to.**

| | Form A | Form B |
|---|---|---|
| Domain | Electricity distribution | Charity fundraising |
| Units | 30 substations | 40 campaigns |
| Headline estimate | **+3.1** failures per substation-year | **+1.9** percentage points |
| Headline interval | `−0.04` to `+6.24` | `−0.15` to `+3.95` |
| Alternatives | +4.2 (n=26), +3.8 (n=19), +3.5 (weighted) | +2.8 (n=35), +2.4 (n=22), +2.2 (weighted) |
| Verdicts | 1 not crossing, 3 crossing | 1 not crossing, 3 crossing |
| Contaminant | 4 refurbishments | 5 national-appeal overlaps |
| Records change | inconsistent logging at 11 sites | CRM migration |
| Size heterogeneity | 2–11 transformers | 4k–200k letters |
| Fit figure | 4% | 5% |

Units, magnitudes, and counts differ so that a reader working both forms cannot carry an answer across. Every structural feature is matched.

### The design's central inversion

In the chapter's anchor, the analysis that failed to cross the threshold was a **careful subset** — the post-SCADA events — and it was arguably the most defensible of the four.

**In both transfer forms the inversion is reversed.** The analysis that fails to cross is the **headline, least careful** one: all units, contaminant included. Three more careful analyses all cross.

This is deliberate. A reader who learned "the subset that fails to cross is usually the good one" would have learned a pattern rather than a principle. The forms require the principle: **look at the estimates, not the verdicts, and ask which analysis handled the known contaminant.**

### Deliberate difficulty features

**The interval straddles zero by a hair.** `−0.04` and `−0.15`. A reader who reports "the interval includes zero" without noticing how narrowly has reproduced the ritual in a different vocabulary.

**Every alternative is supplied with its arithmetic.** The forms do not test whether a reader can compute a standard error; they test whether a reader looks at four estimates and sees that they agree. Computation is not the difficulty and should not be the obstacle.

**Item 6 asks for a check that could have failed.** The most common response will be to re-propose a fit check in different words, and the rubric scores that 1 rather than 2.

**Item 7 requires production, not criticism.** Four short paragraphs replacing the summary.

**Neither form asks for a recommendation.** Whether to reverse the loading regime, or keep the letter format, needs consequences. Chapter 11.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors.

Electricity distribution and charity fundraising are both new.

**One judgment recorded.** Form A concerns equipment failure in an electricity network, which is adjacent to the water utility's asset questions in Chapters 5 and 7. The resemblance is at the level of "infrastructure asset with failures" and no quantity, mechanism, or question is shared — the water case's asset questions were about identification, and this is about what an estimate and its interval mean. Flagged rather than left for a reader to notice.

## What a strong Form A answer should notice

- **The four estimates: `+3.1`, `+3.5`, `+3.8`, `+4.2`.** All positive, all the same order. The estimates agree.
- **The headline is the only verdict that does not cross**, at about 2.02 standard errors against a threshold of roughly 2.
- **The interval's lower limit is `−0.04`.** A reader who quotes "the interval includes zero" without noting that it does so by four hundredths has missed the item.
- **The four refurbishments are a stated contaminant** that the headline analysis includes and one alternative removes — which makes the reported analysis the least careful of the four.
- **Eleven sites with inconsistent logging** is a Chapter 4 problem about which records exist, and it is not in the interval.
- **Each substation contributes one number regardless of size**, so the headline estimand is per-substation, not per-transformer — and the report never says which it means.
- **The 4% fit figure could not have failed.**

## What a strong Form B answer should notice

- **The four estimates: `+1.9`, `+2.2`, `+2.4`, `+2.8`.**
- **The headline is at about 1.88 standard errors**, and the interval's lower limit is `−0.15`.
- **The five national-appeal overlaps are a stated contaminant**, and the fundraising team has already said it depresses response — so excluding them is not a post-hoc rescue but a documented reason.
- **The CRM migration changed what a "response attributed to a campaign" means**, which is a measurement question and is not in the interval.
- **Campaigns range from four thousand to two hundred thousand letters**, so an unweighted mean over campaigns is a different estimand from a response-rate change over letters — and the trustees almost certainly want the second.
- **A reader may object that response rate is the wrong variable**, since the charity cares about money raised. That is an item-1 observation about the estimand and should be credited.
- **The 5% fit figure could not have failed.**

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Supplied facts | 4 | 4 | ✓ |
| Produce items | 7 | 7 | ✓ |
| Alternatives supplied | 3 | 3 | ✓ |
| Verdict pattern | 1 not / 3 crossing | 1 not / 3 crossing | ✓ |
| Headline is the non-crossing one | ✓ | ✓ | ✓ |
| Interval straddles zero narrowly | −0.04 | −0.15 | ✓ |
| Headline standard errors from zero | 2.02 | 1.88 | ✓ close |
| Stated contaminant in headline | ✓ | ✓ | ✓ |
| Records-change confound | ✓ | ✓ | ✓ |
| Size heterogeneity | ✓ | ✓ | ✓ |
| Fit-only model check | 4% | 5% | ✓ |
| Rewrite required | ✓ | ✓ | ✓ |
| Word count | comparable | comparable | ✓ |

Arithmetic for both forms was computed and checked before the forms were written; the values in `transfer-rubric.md` are the checked values, and the threshold verdicts were checked against the appropriate critical values rather than assumed from the intervals.

## Rubric-to-item mapping

Recorded here so it can be checked, as `../07-targets-identification/transfer.md` began doing after the Chapter 6 mismatch.

| Rubric dimension | Produce item |
|---|---|
| Estimand stated | 1 |
| Estimator not confused with estimate | 1, 7 |
| What the interval covers | 2 |
| The non-significance sentence | 3 |
| Four analyses | 4 |
| What the dichotomy did | 5 |
| A check that could have failed | 6 |

**Item 7 is scored across all seven dimensions** rather than having its own, because a rewritten summary either carries the chapter's disciplines or does not.

## Pilot notes

Untested. Four things a pilot should measure.

**Time.** 50 minutes for seven items including a rewrite. This is the third consecutive transfer at that target and none has been timed.

**Whether readers notice the interval straddles zero narrowly.** If most report "includes zero" flatly, the forms have reproduced the ritual and the intervals should be widened so the point cannot be made by arithmetic alone.

**Whether item 6 produces fit checks in disguise.** Expected to be common. If it is near-universal, §7 of the chapter needs a second worked example rather than the form needing a change.

**Whether item 7 is producible in the time available.** It is the chapter's most distinctive output and readers have seen one worked example, in §4. If rewrites come back as bullet lists of complaints, the example was insufficient.
