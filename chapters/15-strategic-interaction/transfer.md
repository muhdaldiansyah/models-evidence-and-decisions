# Chapter 15 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0022`, four of whose clauses need author attention.

## Transfer target

Per `spec.md`:

> Given a metric with a documentable date of consequence, a before-and-after series in which the metric moves and the underlying quantity does not, and a legal documented mechanism, apply the discriminator, name which Goodhart mechanisms are present, quantify the broken planning relationship as a forecast error, describe the two-party structure and identify the equilibrium, and say why the obvious remedies do not work.

## The changed task shape

Chapters 13 and 14 asked the reader to compute a trajectory and then to interpret a table. **Chapter 15 asks the reader to explain a table that has already been interpreted — wrongly — by the organisation that produced it.**

Both forms open with a series that has a published, official reading: the measure improved. That reading is what the funding body recorded, what the annual report said, and what a competent analyst who looked only at the metric column would conclude.

**The task is to arrive at a different reading and to say what would establish it.** Every item after the first is about the second half.

## Form design

Both forms supply the same nine things, in the same order:

1. **A repeated official measurement** with an established recording process.
2. **A documented commencement date** at which consequences attached, sourced to a published framework.
3. **A seven-year series with two columns** — the metric, and an independent indicator of the goal behind it.
4. **Three flat pre-period years**, so the discontinuity is unambiguous.
5. **Two facts that close off the innocent explanations** — the volume input was flat, and resources fell.
6. **A lawful, documented mechanism**, stated in enough detail to be assessed.
7. **A planning relationship fitted before the date**, with the fitted value given.
8. **A large decision the metric is being used to justify**, and an instrument priced against it.
9. **Nine produce items**, of which one asks about people who appear in no column.

| | Form A | Form B |
|---|---|---|
| Domain | County police force | Further-education college |
| Metric | cases recorded as cleared | learners recorded as completing |
| Goal indicator | convictions at court | employment or further study at six months |
| Date | 2019, published funding framework | 2019, published funding rules |
| Mechanism | disposal-code guidance reissued | census date moved; withdrawal processing tightened |
| Metric change, first year | **+26.4%** | **+23.0%** |
| Goal indicator, first year | **−0.3%** | **−0.4%** |
| Metric change by 2022 | **+44.2%** | **+35.9%** |
| Goal indicator by 2022 | **−1.6%** | **−1.7%** |
| Fitted ratio | 0.50 | 0.85 |
| 2022 forecast / actual | 2,230 / 1,520 | 2,516 / 1,810 |
| Forecast error | **47% above actual** | **39% above actual** |
| Instrument / decision | £210,000 / £4,600,000 | £140,000 / £3,100,000 |
| Instrument as a share | **4.6%** | **4.5%** |
| Invisible group | victims of cases closed by out-of-court disposal | learners who withdrew before the census date |

Every figure was computed and checked before the forms were written.

### The direction is deliberately reversed

**In the chapter, the broken relationship makes the forecast too low** — the utility forecast 439 complaints and got 930.

**In both forms it makes the forecast too high** — the force forecasts 2,230 convictions and gets 1,520; the college forecasts 2,516 destinations and gets 1,810.

**A reader who pattern-matched on "the forecast will be an underestimate" gets both forms wrong.** The direction depends on which side of the ratio the metric sits, and it is not a property of the phenomenon.

### The four structural features, and why each is there

**Three flat pre-period years** make the discontinuity unarguable, so that item 2 tests whether the reader looks for a date rather than whether they can see a step.

**The flat volume input and the falling resources** close off the two explanations a reader will reach for first — more crime reported, or more staff hired. Without them, item 1 has an innocent answer.

**The mechanism is given rather than hidden.** This is unlike the chapter, where §1 withholds it. **The forms give it because item 3 is the point**: the reader has to say that three of the four mechanisms would operate even if the mechanism described had not happened, and they cannot do that unless they know what it was.

**And the invisible group in item 9 is the hardest item on the page.** It is not required for a good answer. It tests whether a reader who has learned to ask what a record leaves out — Chapter 4's competence — still asks it when the chapter is about something else.

### Deliberate difficulty features

**Item 1 asks for three sentences.** Readers who write a page have not committed to a reading.

**Item 2 asks what the finding does *and does not* establish.** The discriminator fails safely in one direction only, and this is where that is tested.

**Item 3 describes the four mechanisms without naming them**, so that a reader who memorised four labels cannot pattern-match, and a reader who understood them can still answer.

**Item 5 asks for the stable outcome without using the word equilibrium**, and asks whether it is better or worse than before — which is the chapter's central result and the one most likely to be missed.

**Item 6 supplies three remedies that all sound sensible.** The expected failure is to endorse one.

**Item 7 ends with the invitation to say why no value can be computed**, as Chapter 14's did. Readers who invent a probability and compute an expected value have skipped Chapter 12.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors, electricity distribution, charity fundraising, hospital estates, banking risk, higher education, food manufacturing, rail infrastructure, retail loss prevention, port and harbour infrastructure, health system diagnostic capacity, hospital platelet inventory, district heating, grid reserve procurement, county winter road service.

Policing and further education are both new.

**Two judgments recorded.**

**Form B is adjacent to two earlier domains and neither overlap is substantive.** Chapter 1's contrast used **student assessment** — an individual's marks, not an institution's returns — and an earlier exclusion lists **higher education**, which is a different sector with different funding rules. This form is about a college's recorded completion counts and a funding formula, and shares no actor, quantity, or question with either.

**Form A is the most sensitive domain in the book and is handled accordingly.** Policing invites moral reading in a way that reserve procurement does not. **The form takes no position on any policing practice**, every code it describes is in a national standard, no individual appears, no real force is depicted, and the mechanism described is administrative rather than operational. The rubric's tone note is longer for this form than for any other in the book, for that reason.

## What a strong Form A answer should notice

- **Clearances rose 44% while convictions fell 1.6%**, with recorded crime flat and officer numbers down 4%. Nothing that could produce genuine improvement is present.
- **The date is 2019 and it is in the published funding framework** — not inferred from the data being tested.
- **The pre-period is flat** (3,120 / 3,100 / 3,060) and the step is a single year.
- **The finding establishes that something changed at the date. It does not establish that nothing strategic happened elsewhere**, and a reader who claims it does has over-read the discriminator.
- **Three mechanisms would remain if the force had changed nothing**: regressional, extremal, and — arguably — causal, since the incentive itself is the regulator's action. **Only the adversarial mechanism needs the guidance change.**
- **The forecast is 2,230 against an actual 1,520 — 47% above.** The court liaison team is established for a workload half again the size of the real one, and the consequence falls on that team's budget and on whatever the over-establishment displaced.
- **The two parties are the force and the funding body.** The stable outcome is the funding body scoring clearances and the force recording generously — **and it is no better than 2018 for anybody, with a share of discretionary funding having moved.**
- **Better measure**: acquires consequences too. **More measures**: more surfaces, and the force chooses which to optimise. **Audit the codes**: they are in the national standard and were disclosed, so an audit confirms what was filed.
- **The audit costs 4.6% of the decision it informs**, so it cannot be screened out on cost — which is not the same as being worth buying, and **no expected value can be computed** because nobody will supply a probability over what the sample would show.
- **Item 9: the victims** of cases closed by out-of-court disposal. They appear in the clearance column as a success and in no column at all as people, and neither item 1's reading nor item 4's ratio can see them.

## What a strong Form B answer should notice

- **Completions rose 36% while destinations fell 1.7%**, with enrolments flat and teaching staff down 3%.
- **The date is 2019 and it is in the published funding rules.**
- **The pre-period is flat** (2,180 / 2,150 / 2,205).
- **The mechanism is a definitional change to the cohort**, not to teaching. Nobody learned more.
- **Three mechanisms remain without the census change**, as in Form A.
- **The forecast is 2,516 against an actual 1,810 — 39% above.** The careers service is established for a caseload it does not have.
- **The stable outcome is the funding body scoring completions and the college recording a later cohort** — no better than 2018 for learners, with grant having moved.
- **Item 9: the learners who withdrew before the census date.** They are in no column of the table. **They are also the group most likely to need the careers service**, which makes item 4's error worse than the arithmetic shows — the 0.85 ratio was fitted when they were counted.

**That last observation is the strongest available answer to either form**, and it is not required.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Metric with a dated commencement | ✓ | ✓ | ✓ |
| Independent goal indicator | ✓ | ✓ | ✓ |
| Three flat pre-period years | ✓ | ✓ | ✓ |
| Volume input flat; resources down | ✓ | ✓ | ✓ |
| Lawful, documented mechanism | ✓ | ✓ | ✓ |
| Fitted planning ratio | ✓ 0.50 | ✓ 0.85 | ✓ |
| Forecast error direction | too high | too high | ✓ |
| Forecast error size | 47% | 39% | ✓ |
| Instrument as share of decision | 4.6% | 4.5% | ✓ |
| Invisible group | ✓ | ✓ | ✓ |
| Produce items | 9 | 9 | ✓ |
| Word count | comparable | comparable | ✓ |

**One deliberate asymmetry.** Form B's invisible group is also the group the broken forecast most affects; Form A's is not. **Form B therefore has a deeper bottom**, and the rubric says so rather than pretending the two are equally hard.

## Rubric-to-item mapping

| Rubric dimension | Produce item |
|---|---|
| The reading | 1 |
| The discriminator, and its limits | 2 |
| Four mechanisms, and which need an agent | 3 |
| The broken relationship, quantified | 4 |
| The two-party structure and the stable outcome | 5 |
| Why the remedies fail | 6 |
| The instrument, and the missing probability | 7 |
| What the page omits | 8 |
| Who is in no column | 9 |

## Pilot notes

Untested. Five things a pilot should measure.

**Whether readers reach for fraud.** Both forms state twice that everything was lawful and disclosed. If answers still describe it as cheating, the statement is not doing its work and the fix is in the chapter's §3, not the forms.

**Whether item 3's unnamed mechanisms are recognised.** They are described rather than labelled precisely so that recall is not what is being tested. If readers cannot map the descriptions, the chapter's table is not doing its job.

**Whether the forecast direction is worked or assumed.** The chapter's error runs the other way. An answer stating the error without arithmetic has probably pattern-matched.

**Whether item 5 produces "worse for everybody".** This is the chapter's central result and the easiest to miss, because the metric did improve and somebody did get the money.

**And whether anyone finds item 9.** A low rate is expected and acceptable. A zero rate over several pilots would suggest the chapter should ask for it directly.
