# Chapter 16 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0023`.

## Transfer target

Per `spec.md`:

> Given two unfamiliar problems — one an automated system, one a small decision — produce a routing record for each with a reason on every row including the negatives, work the material stages far enough to reach a finding, identify at least one fact that changes the routing once noticed, and say what remains unresolved.

## The changed task shape

**Every previous form in this book told the reader what kind of problem they had.** Chapter 8's forms were estimation problems. Chapter 12's were portfolio problems. Chapter 14's were policy-comparison problems. The reader's job was to apply the chapter.

**These forms tell the reader nothing.** They supply a situation and ask which of fifteen chapters it needs.

**And each form contains two problems**, deliberately different in size, so that the discrimination is tested twice within one sitting: **one automated system that touches most of the book, and one small decision that touches four or five chapters.**

**A reader who produces two routing records of similar length has failed the form**, and that is the single most informative outcome a pilot could produce.

## Form design

Both forms supply the same nine things, in the same order:

1. **A repeated automated decision** replacing a human judgment.
2. **A training set with a visible artefact year** whose cause is not the quantity of interest.
3. **A label that is a human decision rather than the thing it is named after.**
4. **Two accuracy figures**, one against the label and one against an independent assessment, roughly 25 points apart.
5. **A rising share** over six quarters since deployment.
6. **An independent indicator that does not move.**
7. **A payment, incentive, or reporting structure** that gives somebody a reason to prefer the direction of drift.
8. **A second, thin problem** with a seven- or six-year series containing a confounded natural experiment.
9. **Nine produce items**, of which three concern the negatives, the ordering, and the unresolved.

| | Form A | Form B |
|---|---|---|
| System | rail delay attribution | helpline call triage |
| Label | the clerk's attribution | the supervisor's escalation |
| Artefact year | 2020, **39% below** 2019 | 2020, **32% above** 2019 |
| Accuracy against label / independent | **88% / 64%** | **86% / 59%** |
| Rising share, six quarters | 41.2% → **49.8%** | 8.4% → **15.6%** |
| Independent indicator | track faults, **+1.1%** | safeguarding referrals, **+2.5%** |
| Money at stake | **£5,428,000** in compensation | **£40,660** in call cost |
| Who benefits from the drift | the **train operators**; the system is owned by the party paying | the **charity**, against a funder's reported measure |
| Thin problem | signage repaint, 6 years, 2 confounded | newsletter send day, 7 years, 2 confounded |
| Thin problem's difference | **−78 complaints, −18.6%** | **+1.46 points, +7.3%** |
| Test available at low cost | no — the repaint is the intervention | **yes** — a free split test |

Every figure was computed and checked before the forms were written.

### The artefact years run in opposite directions

**Form A's 2020 is 39% below trend; Form B's is 32% above.**

Rail delay incidents collapsed when the trains stopped running. Helpline calls rose when people were confined at home.

**A reader who has learned "2020 means a dip" gets Form B wrong.** The competence is asking why a year is unusual, not remembering which way the pandemic went.

### The incentive structures are deliberately asymmetric

**Form A's system is procured and maintained by the party that pays the compensation**, and the drift is against that party's interest. That is the harder case: the obvious strategic story runs backwards, and a reader who reaches for Chapter 15 automatically has to work out who actually benefits — which is the train operators, who did not build the system.

**Form B's drift is toward a measure the funder introduced**, which is Chapter 15's ordinary shape.

**So one form rewards the reflex and one punishes it**, and the rubric says which.

### The thin problems differ in one important way

**Form B's has a free test available.** Splitting the mailing list costs nothing but a fortnight, which makes Chapter 11's row almost trivial and Chapter 7's row a clean negative.

**Form A's does not.** The repaint *is* the intervention; there is no cheap experiment, and the two confounded years are all the evidence there will be. **Chapter 7 is therefore closer to material in Form A than in Form B**, and a reader who marks it "not material" in both without noticing the difference has pattern-matched.

**This is the only deliberate non-parallelism in the pair**, and it is there because the chapter's §6 makes a point about Chapter 7 that a reader could over-generalise.

### Deliberate difficulty features

**Item 2 asks for fifteen rows twice.** Thirty rows is a lot of writing, and that is the point: the discipline is producing the negatives, and a form that asked for the positives only would test nothing.

**Item 3 asks what the difference between the counts tells them.** The expected wrong answer is that Problem 1 was analysed more thoroughly.

**Item 4 asks why they started where they did.** A reader who started at Chapter 1 because it is Chapter 1 has not understood §4 of the chapter.

**Item 5 asks for a fact that changes the routing once noticed.** In both forms the label's identity is the intended answer, and it is stated once, in a subordinate clause, exactly where such facts live.

**Item 6 asks for a recorded revision in five parts**, including whether the previous answer was reasonable. Answers that describe the revision as a correction have missed the chapter.

**Item 9 asks them to sort the unresolved into two kinds.** This is the hardest item on the page and it is not required for a good answer.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors, electricity distribution, charity fundraising, hospital estates, banking risk, higher education, food manufacturing, rail infrastructure, retail loss prevention, port and harbour infrastructure, health system diagnostic capacity, hospital platelet inventory, district heating, grid reserve procurement, county winter road service, policing, further education, local-authority housing repairs.

**Two judgments recorded, and one is a genuine repeat.**

**Form A uses rail infrastructure, which Chapter 11's Form A also used.** That is the only domain reused anywhere in this book's transfer forms, and it is reused because the delay-attribution regime is the clearest real example of an automated system whose label is a contested human judgment with money attached. **The two forms share no quantity, actor, or question**: Chapter 11's was a maintenance decision under two states with a payoff table; this is a routing task about an attribution system. **Flagged rather than left for a reader to notice**, and if a pilot finds the repeat distracting, Form A should move to a different network industry.

**Form B's helpline is adjacent to Chapter 4's food-bank client records and Chapter 6's social-landlord damp reporting**, both of which involve people in difficulty. This form describes no individual, no call, and no person's circumstances; it is about a routing model, an establishment of nine counsellors, and a grant condition.

**Neither domain is sensitive** in the sense `spec.md` uses. Form B concerns a helpline, and the form takes no position on any clinical or safeguarding practice: every escalation in it goes to a *more* senior person, the independent indicator is a statutory procedure the form does not question, and no claim is made about how such services should operate.

## What a strong Form A answer should notice

- **The decision is not whether the system is accurate.** It is whether the infrastructure owner should keep accepting first attributions from it — and it is the owner's decision, about a system the owner built, against a drift that costs the owner money.
- **The label is the clerk's attribution.** Stated once, in one clause. The system predicts what a clerk would have written, not who caused the delay.
- **88% and 64% are about different things** — agreement with a clerk, and agreement with a joint panel.
- **2020 is 39% below 2019 because the trains stopped**, not because the network got better.
- **Delay minutes to the owner up 21%; track faults up 1.1%.** The independent indicator does not support the attribution shift.
- **Chapter 15's row is the interesting one and it runs backwards.** The party that benefits is the train operators. The party that built and maintains the system is the one paying. **A reader who writes "the system's owner gamed it" has not read who pays.**
- **The signage problem needs about five chapters** — 1, 4, 8, 11, and arguably 7 — and Chapter 4's row is most of it: the two partial-repaint years happened because a contractor had year-end capacity, which is not random.
- **Chapter 7 is closer to material here than in a problem with a cheap test**, because the repaint is the intervention and no experiment is available.
- **£5,428,000 against £186,000** is a useful contrast to state: the two problems are three orders of magnitude apart and the second still needs doing.

## What a strong Form B answer should notice

- **The decision is whether the charity should keep the model's recommendation as the default**, and it is the charity's.
- **The label is the supervisor's escalation decision.**
- **86% and 59%** are agreement with a supervisor and agreement with a clinical review.
- **2020 is 32% above 2019**, and a reader who calls it a dip has pattern-matched on the other form's direction.
- **Senior calls rising, safeguarding referrals flat**, and the funder introduced a "high-risk calls handled" measure in 2023 — **Chapter 15's ordinary shape**, and the money is small (£40,660) while the constraint is not: **nine full-time counsellors is a fixed capacity, which is Chapter 13.**
- **The newsletter problem needs four chapters**, and **Chapter 11's row is nearly trivial** because the split test is free — which makes Chapter 7 a clean negative for the reason §6 of the chapter gives.
- **The strongest available observation** is that Form B's two problems differ in what is scarce: the newsletter decision is limited by evidence, and the triage decision is limited by nine counsellors. **Neither is limited by money**, and a reader who routes both to Chapter 12 has misread both.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Automated system replacing a human judgment | ✓ | ✓ | ✓ |
| Label is a human decision | ✓ | ✓ | ✓ |
| Artefact year | ✓ | ✓ | direction deliberately reversed |
| Two accuracy figures, ~25 points apart | ✓ 24 | ✓ 27 | ✓ |
| Rising share over six quarters | ✓ | ✓ | ✓ |
| Flat independent indicator | ✓ | ✓ | ✓ |
| Incentive structure | ✓ | ✓ | direction deliberately reversed |
| Second thin problem | ✓ | ✓ | ✓ |
| Cheap test available for the thin problem | **no** | **yes** | deliberate |
| Produce items | 9 | 9 | ✓ |
| Word count | comparable | comparable | ✓ |

**Two deliberate non-parallelisms**, both stated above, both there to defeat pattern-matching that the chapter's own examples could otherwise install.

## Rubric-to-item mapping

| Rubric dimension | Produce item |
|---|---|
| The decision, stated as a decision | 1 |
| The routing record, and the negatives | 2 |
| What the two counts mean | 3 |
| Working order, and why | 4 |
| The fact that changes the routing | 5 |
| A recorded backward revision | 6 |
| The thin problem's load-bearing row | 7 |
| The recommendation and its conditions | 8 |
| Unresolved, sorted into two kinds | 9 |

## Pilot notes

Untested. Six things a pilot should measure.

**Whether the two routing records differ in length.** The single most informative outcome. Similar-length records mean the chapter's central discrimination did not land.

**Whether the negatives carry reasons.** Count the rows marked "not material" that have no reason. That number is the chapter's failure rate.

**Whether anyone finds the label clause.** It is stated once, in a subordinate clause. If most readers miss it, the forms are too subtle and the clause should be given its own sentence — though not its own emphasis, because the point is that such facts are buried.

**Whether Form A's Chapter 15 row is worked or assumed.** The incentive runs backwards from the obvious reading, and this is where a reflex shows.

**Whether item 6's revision is described as a correction.** If most answers apologise for the earlier stage, §5 of the chapter needs to be blunter.

**And whether item 9's two kinds are separated.** A low rate is expected. A zero rate across pilots would suggest the distinction needs a paragraph in §7 rather than a produce item.
