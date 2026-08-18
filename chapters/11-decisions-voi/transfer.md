# Chapter 11 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0018-chapter11-decision-terminology-and-boundary.md`.

## Transfer target

Per `spec.md`:

> Given a decision with two or three acts, two states, a payoff table, a prior, and a proposed study with stated reliability, compute the expected values, find where the best act changes, compute or bound the study's value, and say whether to commission it.

## The changed task shape

Chapter 10 forbade a recommendation. **Chapter 11 requires one**, in four sentences, naming what it is conditional on.

That reversal is deliberate and it is the point of Part III's two chapters read together. Chapter 10 established that recommending before the decision is well-posed is premature. Chapter 11 has posed it, so declining to recommend is now evasion rather than discipline.

## Form design

Both forms supply the same seven things, in the same order:

1. **Two states**, described mechanistically, that the organisation cannot currently distinguish.
2. **A register** giving a prior, small enough that its weakness is visible.
3. **Three acts**, one of which is **dominated** and one of which has **no spread**.
4. **A payoff table** whose cells openly contain a monetisation of several things.
5. **A cheap study** with stated reliability, whose value **exceeds its cost**.
6. **An expensive study**, described as near-certain, whose cost **exceeds the ceiling**.
7. **Eight produce items** plus a four-sentence recommendation.

| | Form A | Form B |
|---|---|---|
| Domain | Rail infrastructure | Retail loss prevention |
| States | rolling contact fatigue / formation defect | organised rings / diffuse abuse |
| Register | 5 : 3, so **0.625** | 9 : 6, so **0.600** |
| Acts | grinding / replacement / restriction | rule / manual team / policy |
| Dominated act | B, by C | B, by C |
| Flat act | C at 2,000 | C at 1,050 |
| Best at prior | **A, 1,662.5** | **A, 908.0** |
| Critical value | **0.400** | **0.403** |
| Cost of choosing the flat act | **337.5** | **142.0** |
| Study 1 reliability | 0.80 / 0.25 | 0.75 / 0.20 |
| Study 1 value / cost | **56.2** / 45 → **run** | **28.3** / 20 → **run** |
| EVPI | **225.0** | **116.0** |
| Study 2 cost | 280 → **refuse on the ceiling** | 150 → **refuse on the ceiling** |

All figures in £ thousands, computed and checked before the forms were written.

### The central inversion

**In the chapter, the study is not worth running. In both forms, the cheap study is.**

This is the same device Chapter 10's forms used, for the same reason. A reader who took away *studies are usually not worth it* has learned a pattern, and both forms punish it immediately.

**And the forms supply the explanation rather than hiding it.** In the chapter the prior sits at 0.636 against a critical value of 0.283 — more than twice it, so the negative branch barely crosses. In both forms the prior sits about half again above the critical value, so the negative branch crosses properly and the study earns its cost.

The rubric awards a mark for saying this unprompted.

### Deliberate difficulty features

**Item 7 forbids computing Study 2's value.** It must be refused on the ceiling alone. A reader who computes it has done unnecessary work and has not understood what the ceiling is for — and the instruction is explicit, so the failure is unambiguous.

**The dominated act is expensive and prominent.** £3.2m of rail replacement and £950k of manual review are the kind of options that dominate a meeting, and both are eliminable without any probability at all.

**The critical value is closer than it looks.** 0.400 against a prior of 0.625 is a comfortable-looking margin that a third of the prior would erase. Readers who report *comfortably above* without quantifying it are half right.

**Item 8 asks for value judgments in the table**, which the forms present as ordinary cost accounting: "a monetised cost of remaining delay minutes, defect rectification, and reputational exposure". Nothing flags it.

**A recommendation is required**, reversing Chapter 10's constraint.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors, electricity distribution, charity fundraising, hospital estates, banking risk, higher education, food manufacturing.

Rail infrastructure and retail loss prevention are both new.

**One judgment recorded.** Form B concerns fraud, and Chapter 6's Form B concerned a social landlord's damp reports while Chapter 8's concerned donation response. None shares a quantity, actor, or question with this one, which is about choosing among three loss-prevention acts under an unresolved cause. Flagged rather than left for a reader to notice.

**Neither domain is sensitive** in the sense `spec.md` uses. Form A concerns rail safety at one remove — the acts are all safe, and the question is cost — and the form takes no position on rail maintenance practice.

## What a strong Form A answer should notice

- **Act B is dominated by Act C** and needs no probabilities to eliminate.
- **Expected costs 1,662.5 / 3,362.5 / 2,000.0**, best A.
- **Act C is flat at 2,000**, and choosing it costs **337.5** in expectation — reported as a cost, not as an error.
- **Critical value 0.400** against a prior of 0.625: above, but a third of the prior would erase it.
- **Study 1 is worth 56.2 against a cost of 45** — commission it.
- **EVPI is 225.0**, so Study 2 at 280 is refused **without further computation**.
- **The value judgments**: the price of a delay minute, the price of reputational exposure, the five-year horizon.
- **A strong answer notes that the chapter's study was not worth running and this one is**, and says the difference is where the prior sits relative to the critical value.

## What a strong Form B answer should notice

- **Act B is dominated by Act C.**
- **Expected costs 908.0 / 1,680.0 / 1,050.0**, best A.
- **Act C is flat at 1,050**, costing **142.0** in expectation.
- **Critical value 0.403** against a prior of 0.600.
- **Study 1 is worth 28.3 against a cost of 20** — commission it, and note the margin is thin.
- **EVPI is 116.0**, so Study 2 at 150 is refused on the ceiling.
- **The value judgments**: the exchange rate between a pound of fraud loss and a pound of friction imposed on a legitimate customer; the price of lost goodwill; the three-year horizon.
- **A reader may object that the two states are not exclusive** — both could be occurring. That is correct, it is a real limitation of a two-state table, and it should be credited.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| States | 2, mechanistic | 2, mechanistic | ✓ |
| Acts | 3 | 3 | ✓ |
| Dominated act | ✓ B by C | ✓ B by C | ✓ |
| Flat act | ✓ C | ✓ C | ✓ |
| Prior | 0.625 | 0.600 | ✓ |
| Critical value | 0.400 | 0.403 | ✓ |
| Prior ÷ critical value | 1.56 | 1.49 | ✓ |
| Study 1 worth running | ✓ by 11.2 | ✓ by 8.3 | ✓ |
| Study 2 exceeds ceiling | ✓ by 55 | ✓ by 34 | ✓ |
| Produce items | 8 + recommendation | 8 + recommendation | ✓ |
| Word count | comparable | comparable | ✓ |

Arithmetic for both forms was computed and checked before the forms were written; the values in `transfer-rubric.md` are the checked values.

## Rubric-to-item mapping

| Rubric dimension | Produce item |
|---|---|
| Dominance | 1 |
| Expected values | 2 |
| The rule named | 3 |
| Risk | 4 |
| Critical value | 5 |
| Value of Study 1 | 6 |
| The ceiling used | 7 |
| Value judgments named | 8 |

**Every dimension has a dedicated item**, as in Chapter 10 and unlike Chapter 9.

## Pilot notes

Untested. Four things a pilot should measure.

**Time.** 50 minutes for eight items plus a recommendation, with more arithmetic than any previous transfer. This is the most computation the book has asked for and may not fit.

**Whether readers refuse Study 2 on the ceiling alone.** The instruction is explicit. If readers compute it anyway, the ceiling did not land as a screening rule and the fix is in §5 of the chapter.

**Whether the inversion is noticed.** If no reader remarks that the chapter's answer was the opposite, the chapter should say more plainly that the finding is about the decision rather than about tests.

**Whether item 8 produces genuine value judgments.** Expected failure mode is naming the probability as a judgment, which it is not — it is an estimate with a provenance. The judgments are in the currency conversion.
