# Chapter 7 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0014-chapter7-identification-terminology-and-notation.md`.

## Transfer target

Per `spec.md`:

> Given a claim that an action caused an outcome, a supplied observational record, and a supplied structural fact about how the action was allocated, state the target quantity, name the identifying assumption the claim requires, find the condition that fails and say why it is structural rather than a sample-size problem, and write the target trial that would answer the question.

## The changed task shape

Chapter 6 asked the reader to **produce** numbers. Chapter 7 asks them to produce a **verdict**, which is a third thing.

Chapters 4 and 5 asked for criticism, and a reader can criticize by listing worries. Chapter 6 asked for computation, and a reader can compute without understanding. Chapter 7's output is neither: it is a written judgment about what a body of evidence could and could not establish, ending in a form that names an assumption and says what would change it.

That is harder to fake in both directions. A reader who lists worries without naming a condition scores badly. A reader who computes all three comparisons correctly and reports the third as the answer scores badly too — **and that is the trap the forms are built around.**

## Form design

Both forms supply exactly the same five things, in the same order:

1. **A vague causal claim** in one sentence, of the kind that appears in real reports, with all five estimand attributes missing.
2. **Four numbers** — treated and untreated, before and after — supporting three contradictory comparisons, the first of which points the **wrong way**.
3. **An allocation rule** that breaks exchangeability, and that is defensible operational practice rather than a blunder.
4. **A concurrent change** across all units, visible as the control group's small movement.
5. **A structural constraint** that makes positivity fail exactly for the units the decision-maker cares about most.
6. **Multiple versions of the intervention**, unrecorded, at least one of which plausibly behaves differently from the others.

| | Form A | Form B |
|---|---|---|
| Domain | Manufacturing safety | City transport |
| Units | 20 production lines | 18 bus corridors |
| Treated / untreated | 8 / 12 | 7 / 11 |
| Before, treated / untreated | 5.4 / 2.1 | 34.5 / 21.8 |
| After, treated / untreated | 3.6 / 1.8 | 30.2 / 21.0 |
| Cross-section, after | **+1.8** | **+9.2** |
| Before and after, treated | **−1.8** | **−4.3** |
| Difference in differences | **−1.5** | **−3.5** |
| Allocation rule | the eight worst | the seven slowest |
| Concurrent change | company-wide glove standard | city-wide signal retiming |
| Positivity constraint | fixed machine bed required | 9.5 m carriageway required |
| Versions of the intervention | 3 | 4 |

The units, magnitudes, and counts differ so that a reader working both forms cannot carry an answer across. Every structural feature is matched.

### Deliberate difficulty features

**The cross-section has the wrong sign in both forms.** Not merely imprecise — backwards. A reader who reports it has not made a small error.

**Difference in differences is the trap.** It is the answer most likely to be produced by a capable reader, it is the best of the three, and it is still not safe. The rubric awards full marks only to a response that names its assumption and connects it to the allocation rule.

**The positivity failure hits the units the decision-maker cares about most.** In both forms, the constrained units are the worst ones — the four adjustable-bed lines with the highest injury rates, the four historic streets that are the slowest. This is deliberate: it makes the failure consequential rather than a technicality.

**Item 6 asks the more-data question directly**, because the wrong answer is the one readers give when left to find it themselves.

**Neither form asks for a recommendation.** The verdict names what is unestablished and what would change it. Whether to fund the programme needs consequences, and Chapter 11 has them.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting.

Manufacturing safety and city bus corridors are both new.

**One judgment recorded.** Form B is a city transport case, and Chapter 4's Form A used a city's pothole repair records. Both are municipal, and there the resemblance ends: the pothole case is about how records come to exist, this one about how an intervention was allocated; they share no quantity, actor, or question. Flagged here rather than left for a reader to notice.

**One deliberate near-miss.** Form A concerns workplace injuries, which is a domain where real harm is at stake. The form takes no position on machine guarding, presents no value as typical, and asks only about what a record can establish. This is judged non-sensitive in the sense `spec.md` uses, but the judgment is recorded rather than assumed.

## What a strong Form A answer should notice

- **The three comparisons: `+1.8`, `−1.8`, `−1.5`.** All three, or item 2 was not answered.
- **The cross-section is guaranteed positive.** Starting at 5.4 against 2.1, a fall of 1.8 cannot close a gap of 3.3. This is arithmetic about starting points, not evidence of harm.
- **The glove standard is visible as the control group's 0.3.**
- **Two-hand controls can be defeated**, so option 3 may behave quite differently from a fixed barrier — and the eight lines are an unrecorded mixture of three treatments.
- **The four adjustable-bed lines have zero probability of retrofit**, and they are the lines with the highest injury rates among the twelve.
- **More lines and more years do not fix it**, because adjustable-bed lines cannot take the retrofit at all. A strong answer says this in terms of *why those units are excluded*, not in terms of sample size.
- **The target trial cannot be run** because you cannot withhold a safety retrofit from a line that needs one — and saying so names the assumption.

## What a strong Form B answer should notice

- **The three comparisons: `+9.2`, `−4.3`, `−3.5`.**
- **The cross-section is guaranteed positive.** 34.5 against 21.8 is a gap of 12.7; a fall of 4.3 does not close it.
- **Signal retiming is visible as the control group's 0.8**, and a strong answer notes that this is a *large* share of the raw improvement relative to Form A's — 0.8 of 4.3 against 0.3 of 1.8, which are similar fractions and worth noticing as the same structure.
- **A bus-and-taxi lane on a busy corridor may be close to no lane at all**, so the seven corridors are an unrecorded mixture of four treatments.
- **The four historic streets have zero probability of a lane**, and they are the slowest of the eleven.
- **More corridors and more years do not fix it**, because a 7-metre street cannot take a 9.5-metre-minimum lane in any year.
- **A reader may object that journey time is the wrong outcome** — that a bus lane's purpose includes reliability and passenger numbers, not only mean time. That is correct, it is an item-1 observation about the variable attribute, and it should be credited.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Supplied facts | 4 | 4 | ✓ |
| Produce items | 7 | 7 | ✓ |
| Cross-section sign | positive | positive | ✓ |
| DiD available and unsafe | ✓ | ✓ | ✓ |
| Control-group movement as fraction of treated | 0.3 / 1.8 = 17% | 0.8 / 4.3 = 19% | ✓ |
| Versions of intervention | 3 | 4 | ✓ close |
| Constrained units are the worst | ✓ | ✓ | ✓ |
| More-data question asked explicitly | ✓ | ✓ | ✓ |
| Verdict required | ✓ | ✓ | ✓ |
| Word count | comparable | comparable | ✓ |

Arithmetic for both forms was computed and checked before the forms were written; the values in `transfer-rubric.md` are the checked values.

## Carried forward from Chapter 6

`../06-probability-simulation/transfer.md` records an unresolved item: `spec.md` there listed eight rubric dimensions of which one was not exercised by either form.

**Chapter 7 does not repeat it.** Its seven rubric dimensions each correspond to a numbered Produce item, and the correspondence is listed here so it can be checked:

| Rubric dimension | Produce item |
|---|---|
| Target quantity stated | 1 |
| Intervention specified | 5 |
| Comparisons computed | 2 |
| Exchangeability | 3, 4 |
| Positivity | 6 |
| Target trial | 7 |
| Verdict | the closing paragraph |

## Pilot notes

Untested. Four things a pilot should measure.

**Time.** 50 minutes is a guess, and it is the longest transfer in the book for the longest chapter in the book. Seven produce items plus a verdict may not fit.

**Whether readers report the difference in differences as the answer.** If most do, the chapter's §5 did not land, and the fix is in §5 rather than in the form.

**Whether the positivity item is found without item 6's prompt.** Item 6 currently points at fact 4 directly. A harder variant would not, and a pilot should establish whether the unprompted version is reachable or merely frustrating.

**Whether the verdict format is producible.** It is the chapter's most distinctive output and readers have seen exactly one worked example. If verdicts come back as "more research needed", the example was insufficient and §4 needs a second one.
