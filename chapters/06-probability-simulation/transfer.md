# Chapter 6 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0013-chapter6-probability-terminology-and-notation.md`.

## Transfer target

Per `spec.md`:

> Given a situation with two candidate explanations, a stated base rate, and a proposed observation with stated likelihoods, produce a probability with its conditioning information, update it correctly, identify one supplied detail that moves nothing and say why, and assess a short forecasting record for calibration.

## The changed task shape

Chapters 4 and 5 asked the reader to **criticize** something they had been handed. Chapter 6 asks them to **produce** numbers and defend them.

That is a deliberate reversal and it is the harder direction.

A reader who can find the flaw in somebody else's probability has not shown they can state one of their own — and the failure this chapter exists to prevent is the refusal to state one at all, which criticism tasks cannot detect. The forms therefore put the reader in the analyst's seat and require six committed outputs.

It also means the forms cannot be scored on whether the reader noticed something. They are scored on whether the numbers are right and whether the sentences around the numbers carry their conditioning.

## Form design

Both forms supply exactly four things, in the same order:

1. **Two candidate explanations**, both consistent with everything observed, pointing at different and differently priced responses.
2. **A register** the reader must convert into prior odds, with a population that has to be named and a stated imperfection in the record.
3. **One discriminating observation** with two supplied likelihoods, whose ratio is between 3 and 4 and which is decisive in both directions.
4. **One distractor** with a ratio near 1.08 — vivid, true, volunteered by a person, and near-useless for the comparison.

Plus a **36-row forecasting record** with three bins, identical between the forms, showing calibration at the two lower bins and a coin at the top bin.

| | Form A | Form B |
|---|---|---|
| Domain | Light-van fleet maintenance | Social-landlord damp reporting |
| Register | 9 : 6 | 7 : 5 |
| Prior for the first explanation | about 60% | about 58% |
| Discriminating ratio | 4.0 | 3.75 |
| Posterior, positive branch | about 86% | about 84% |
| Posterior, negative branch | about 73% for the second | about 70% for the second |
| Distractor ratio | 1.08 | 1.08 |
| Record | 80/60/40 over 36 | 80/60/40 over 36 |

The registers differ in size (15 versus 12) so that a reader who works both forms cannot carry an answer across, and the priors differ by two points so that no number is reusable. Every structural feature is matched.

### Deliberate difficulty features

**The negative branch flips the winner in both forms.** A reader who works only the positive branch gets a number that is right and an impression that is wrong, because they never see that the same test can hand the case to the other explanation.

**The register is imperfect in both forms**, in a way that is stated and not resolved: two contractor records no longer held (A), three hand-transcribed entries (B). Naming the population is scored; noticing the defect is not required but is the mark of a reader carrying Chapter 4 forward.

**Form B's explanations are a real-change/reporting-change pair**, which is a distinction the reader met in Chapter 4 in a different vocabulary. This is spiral reuse and is intended.

**Neither form asks for a decision.** Item 6 asks whether to run the observation, and a strong answer will say that the numbers make the observation informative while the cost comparison needs something the reader has not been given. Chapter 11 has it.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders.

**One judgment recorded.** Form B is set in social housing, and Chapter 1 used emergency housing while Chapter 2 used city rental assistance. Those cases were about placement capacity and about payments; this one is about building condition and report volume, and shares no quantity, actor, or question with either. The overlap is the sector name only. Flagged here rather than left for a reader to notice.

## What a strong Form A answer should notice

- **The prior is 9 : 6, not 9 : 15.** Odds compare the two explanations; they are not a share of the total. A reader who writes 9 : 15 has confused odds with probability and will get every subsequent number wrong.
- **The ratio is 4, and it is worth saying in words**: a dropout is four times more expected under a loom fault than under a fuel restriction.
- **Both branches, and the flip.** No dropout gives about 73% for Q — the case changes hands. A strong answer states this as the reason the test is worth running.
- **The driver's report moves belief from 60% to 62%**, which is inside the width of the judgment that produced the 0.65 and the 0.60. The strong form of the answer is *not distinguishable from no movement*, not *a two-point movement*.
- **The distinction that carries the marks:** the report is uninformative **for choosing between P and Q**, not worthless. Heat plausibly aggravates both.
- **The record reads 50 / 58 / 42.** The 80% bin delivered a coin. The actionable sentence is about discounting high-confidence statements, not about competence.
- **The always-50% supervisor is perfectly calibrated and useless.** A reader who says only the first half has missed the point of the item.

## What a strong Form B answer should notice

- **The prior is 7 : 5, about 58%** — and the population is *all report types, all blocks*, which is broader than the question being asked. Naming that breadth is the scored move; a reader who notices it is arguably too broad has done more than required.
- **The ratio is 3.75**, and the survey is of homes that have **not reported**. A strong answer sees why that is the informative population: under a reporting change, unreported homes should be much as they were.
- **Both branches, and the flip.** Six or fewer above threshold gives about 70% for S.
- **The cold-snap detail moves 58% to 60%.** Same treatment as Form A's distractor, and the same distinction: it bears on the situation, not on the comparison, because cold weather makes existing damp more visible *and* worsens it.
- **The record reads 50 / 58 / 42**, identical to Form A.
- **A reader may object that R and S are not mutually exclusive** — both could be happening. That is correct, it is a real limitation of a two-hypothesis treatment, and it should be credited. The chapter works two candidates because the arithmetic is a multiplication; it does not claim the world comes in twos.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Number of supplied tables | 4 | 4 | ✓ |
| Register imperfection stated | ✓ | ✓ | ✓ |
| Discriminating ratio | 4.0 | 3.75 | ✓ within band |
| Distractor ratio | 1.083 | 1.077 | ✓ |
| Branch that flips | ✓ | ✓ | ✓ |
| Record structure | identical | identical | ✓ |
| Distractor delivered by a person | driver | housing officer | ✓ |
| Produce items | 6 | 6 | ✓ |
| Word count | comparable | comparable | ✓ |

Arithmetic for both forms was computed and checked before the forms were written; the values in `transfer-rubric.md` are the checked values.

## An unresolved item for the author

`spec.md` lists **eight** rubric dimensions. The eighth of them — *expectation described as a summary, not as a prediction* — is **not exercised by either form**, because the Transfer target sentence in the same spec does not include it and the forms follow the target.

The rubric therefore has seven dimensions, and expectation is assessed only by the in-chapter §5 task.

Two readings are available and this file does not choose between them:

- the Transfer target is right and the rubric-dimension list should drop expectation; or
- the forms should each carry a short expectation item and the target sentence should be extended.

Adding an expectation item would lengthen forms already at a 45-minute target, which is the longest in the book. Recorded for adjudication rather than resolved here.

## Pilot notes

Untested. Three things a pilot should measure.

**Time.** 45 minutes is a guess and the forms ask for six outputs including two branch calculations. Chapter 5's forms asked for five outputs at 40 minutes and were not timed either.

**Whether the odds-versus-share confusion is common.** If most readers write 9 : 15, the forms need a worked odds reminder that the chapter's §3 apparently failed to install, and that is a finding about the chapter rather than about the form.

**Whether item 6 is answerable.** It deliberately asks a question the chapter cannot fully answer. If readers find that frustrating rather than clarifying, the item should say so explicitly instead of leaving them to discover it.
