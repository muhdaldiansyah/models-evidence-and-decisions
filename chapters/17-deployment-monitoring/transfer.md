# Chapter 17 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0024`.

**These are the last exercises in the book.**

## Transfer target

Per `spec.md`:

> Given a deployed rule with stated thresholds, a baseline period, an operating period, a set of monitored indicators that all look acceptable, and one quantity nobody reports, assess whether each threshold is a trigger or a timer, say what the monitoring can and cannot see, diagnose which stage the failure entered through, and state a revision trigger in both directions.

## The changed task shape

**Every previous form in this book gave the reader a problem to work. These give the reader something already running.**

The reader does not choose an approach, build an estimate, select a portfolio, or route a problem. **They are handed a rule that has been in force for four years, a monitoring pack that looks fine, and a question about whether anything is wrong.**

**And the first produce item is arithmetic on data the organisation already held**, which is the chapter's most portable result and the thing nobody in either case did.

## Form design

Both forms supply the same nine things, in the same order:

1. **A deployed rule with two threshold limbs joined by "or"**, quoted in full, with an owner and a frequency.
2. **Seven baseline years for each watched figure**, given before the operating years so that the reader can compute what nobody computed.
3. **One limb whose threshold sits outside the baseline range** — a trigger.
4. **One limb whose threshold sits inside it** — a timer.
5. **Four operating years** in which the trigger limb is exceeded twice non-consecutively and never fires, and the timer limb fires once.
6. **A board minute recording that nothing was done.**
7. **Three monitored indicators, one of which has improved.**
8. **Two numbers collected by different teams whose ratio nobody reports.**
9. **One further fact about how the model was built**, stated last and in one paragraph, which is where the failure entered.

| | Form A | Form B |
|---|---|---|
| Domain | Water company leakage programme | School trust attendance plan |
| Trigger limb | overnight-flow rise, threshold 6% | persistent absence, threshold +4 points |
| Trigger limb, in baseline standard deviations | **3.07** | **2.40** |
| Times reached in seven baseline years | **0** | **0** |
| Timer limb | burst events, threshold 3 per quarter | safeguarding referrals, threshold 12 |
| Timer limb, in baseline standard deviations | **1.21** | **1.28** |
| Times exceeded in seven baseline years | **1** | **1** |
| Expected firings over a 15-year horizon from baseline variation | **2.1** | **2.1** |
| The value that fired, against baseline maximum | 4 against 4 | 14 against 13 |
| Improved indicator | pressure against target | contacted within five days |
| Unreported ratio | urgent repairs / pipe-failure reports | flagged pupils / attendance orders |
| Ratio change | **+19.9%** | **+26.2%** |
| Where the failure entered | Chapter 4 — a demand model built on two pandemic years | Chapter 4 — a label that is a head of year's referral, on two pandemic years |
| Re-specification cost | £420,000 | £95,000 |

Every figure was computed and checked before the forms were written.

### The structure is the chapter's, deliberately

**Both forms have the same skeleton as Case 1 and the same failure as Case 2.** That is unusual for this book, whose forms normally vary the structure to prevent pattern-matching.

**Here the repetition is the point.** The chapter's claim is that the trigger-or-timer check is four lines of arithmetic applicable to any threshold anybody proposes to act on, and a form that disguised the structure would test recall of a disguise rather than the check.

**What varies is what makes each limb a timer.** Form A's burst threshold is low because burst counts are small integers with a long tail; Form B's referral threshold is low because referral counts vary with staffing and reporting practice as much as with need. **The arithmetic is the same and the reason is not**, and item 2 asks for both.

### The improved indicator is the trap

**In both forms one monitored indicator has improved**, and in both it improved *because of* the thing that is wrong.

Form A: pressure against target improved because the controller is holding pressure tightly — which is what it does, and which is also why night flow is rising.

Form B: contact within five days improved because more pupils are flagged and the caseworkers are contacting the easy ones first.

**A reader who reports "one indicator improved, so at least something is working" has read the pack the way the board read it.**

### Deliberate difficulty features

**Item 1 asks for the baseline before item 2 asks what it means.** The arithmetic is trivial and it is the item most likely to be skipped, because the thresholds are stated and computing a baseline feels like work already done by somebody else.

**Item 3 asks what can *and cannot* be concluded from the firing.** The expected answer names the referral; the strong answer notes that the firing value equals or barely exceeds the baseline maximum.

**Item 4 asks whether the non-firing limb is a fault or an accepted cost.** In both forms it is the second — the two-consecutive-years condition was written deliberately — and a reader who calls it a bug has not asked what it was for.

**Item 6 asks for a failure that would leave all three indicators acceptable.** This is the chapter's central claim inverted into a construction task.

**Item 8 asks for the distance between symptom and entry.** Both forms put the entry at Chapter 4 and the symptom several stages later.

**Item 9 asks for a trigger in two directions.** The model-side condition is the one readers omit, and it is the one that would have caught both forms' actual failure.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors, electricity distribution, charity fundraising, hospital estates, banking risk, higher education, food manufacturing, rail infrastructure, retail loss prevention, port and harbour infrastructure, health system diagnostic capacity, hospital platelet inventory, district heating, grid reserve procurement, county winter road service, policing, further education, local-authority housing repairs, rail delay attribution, helpline call triage.

**Two judgments recorded, and the first is the most significant repeat in the book.**

**Form A is a water company.** The book's anchor is a water utility, and this is the only transfer form in seventeen chapters set in the same industry as the anchor.

**It is deliberate and it is defensible on three grounds.** The anchor's work finished in this chapter's Case 1 and will not be reworked. **The form shares no quantity, no actor, and no question with it**: the anchor is a fifteen-zone municipal supplier with a heatwave, a reservoir, and a capital programme, and this is a regional company with 62 metered areas, an automated pressure controller, and a leakage target. And **the chapter's subject makes an industry repeat cheap** — nothing in the form requires the reader to reason about water, only about a threshold and a monitoring pack.

**If a pilot finds the adjacency confusing, Form A should move to gas distribution**, which is the nearest unused network industry.

**Form B concerns school attendance**, and Chapter 1's contrast used **student assessment** and an earlier exclusion lists **higher education**. Neither overlaps: this form is about a trust-level administrative rule and a monitoring pack, describes no pupil, and takes no position on any attendance practice. **Every routing in it sends a pupil to more support rather than less.**

**Neither domain is sensitive** in the sense `spec.md` uses.

## What a strong Form A answer should notice

- **Overnight-flow baseline: mean 3.23, standard deviation 0.90, maximum 4.6.** The six per cent threshold sits **3.07 standard deviations** above the mean and was never reached in seven years. **A trigger.**
- **Burst baseline: mean 1.57, standard deviation 1.18, maximum 4.** The threshold of three is **1.21 standard deviations** above the mean and was exceeded once in seven years — **2.1 expected firings over fifteen years from ordinary variation alone. A timer.**
- **The 2025 value of four equals the baseline maximum.** It is the sort of year the company has already had.
- **The flow limb was exceeded in 2024 and 2026 and never in consecutive years**, so it never fired. **That is the cost the two-consecutive-years condition was written to buy** — protection against acting on a single bad year — and it is a cost, not a bug.
- **The rule says "or" and the minute records no referral.** The most likely reading is that the two limbs were reported together and the disjunction was read as a conjunction.
- **The three monthly indicators cover coverage, process, and outcome, and all three are reasonable.** None can see a demand model built on pandemic data, because a controller working correctly against a wrong target produces exactly these readings.
- **Pressure against target improved because the controller is holding pressure tightly**, which is also why night flow is rising.
- **The ratio is 6.79 in 2022 and 8.14 in 2024 — up 19.9%.** Urgent repairs are rising much faster than independent pipe-failure reports.
- **The failure entered at Chapter 4**: a demand model built on five years of which two were pandemic years, in areas where non-household consumption fell by a third. **The symptom appears at Chapter 13** — night flow rising against a controller that keeps meeting its target.
- **The model-side revision trigger** is the one to name: *if the demand model is more than three years old, or if any year in its training window is later identified as atypical, the target is re-derived.*

## What a strong Form B answer should notice

- **Absence baseline: mean +1.10, standard deviation 1.21, maximum +2.9.** The four-point threshold sits **2.40 standard deviations** above the mean and was never reached. **A trigger.**
- **Referral baseline: mean 9.14, standard deviation 2.23, maximum 13.** The threshold of twelve is **1.28 standard deviations** above the mean and was exceeded once in seven years — **2.1 expected firings over fifteen years. A timer.**
- **The 2025 value of fourteen exceeds the baseline maximum by one.** Slightly stronger evidence than Form A's, and still not much.
- **The absence limb behaved as written**, and the two-consecutive-years condition was doing a job.
- **Contact within five days improved because more pupils were flagged**, which is not the same as more pupils being helped.
- **The ratio is 14.42 in 2022 and 18.20 in 2024 — up 26.2%.** More pupils flagged per statutory order sought.
- **The failure entered at Chapter 4**: the model predicts *which pupils a head of year referred*, not which pupils are at risk, and it learned that on two years in which attendance recording changed twice.
- **The strongest available observation** is that safeguarding referrals are a poor independent indicator here, because the flag itself routes pupils to caseworkers who make referrals. **The two numbers are not independent**, which weakens the timer analysis and is worth saying — the baseline was generated by a system that did not contain the flag.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Deployed rule, two limbs joined by "or" | ✓ | ✓ | ✓ |
| Seven baseline years, both figures | ✓ | ✓ | ✓ |
| Trigger limb, standard deviations above mean | 3.07 | 2.40 | ✓ |
| Timer limb, times exceeded in baseline | 1 of 7 | 1 of 7 | ✓ |
| Expected firings over 15 years | 2.1 | 2.1 | ✓ |
| Trigger limb exceeded twice, non-consecutively | ✓ | ✓ | ✓ |
| Board minute recording no action | ✓ | ✓ | ✓ |
| Three indicators, one improved | ✓ | ✓ | ✓ |
| Unreported ratio | ✓ +19.9% | ✓ +26.2% | ✓ |
| Failure enters at Chapter 4 | ✓ | ✓ | ✓ |
| Produce items | 9 | 9 | ✓ |

**One deliberate asymmetry.** Form B's independent indicator is **not independent** — the flag routes pupils toward the people who make referrals. **Form B therefore has a deeper bottom**, and the rubric says so rather than pretending the forms are equally hard.

## Rubric-to-item mapping

| Rubric dimension | Produce item |
|---|---|
| The baseline, computed | 1 |
| Trigger or timer, with arithmetic | 2 |
| What the firing does and does not establish | 3 |
| The non-firing limb as accepted cost | 4 |
| The rule, rewritten | 5 |
| What the indicators cannot see | 6 |
| The unreported ratio | 7 |
| Diagnosis by stage, and the distance | 8 |
| A revision trigger in two directions | 9 |

## Pilot notes

Untested. Six things a pilot should measure, and the last is about the book rather than the form.

**Whether item 1 is actually computed.** If readers assert "the threshold looks low" without the arithmetic, the chapter's most portable result did not transfer.

**Whether both limbs are assessed.** The expected shortcut is to assess the one that fired.

**Whether the improved indicator is caught.** A reader who cites it as reassurance has read the pack as the board read it.

**Whether item 9's model-side condition appears.** This is the item most likely to be half-answered, and it is the one that would have prevented both cases.

**Whether Form B's non-independence is noticed.** A low rate is expected; it is the hardest observation either form allows.

**And whether anyone objects that the forms are too similar to the chapter's own case.** They are, deliberately, and the reasoning is in this document. A pilot that produces that objection has produced a reader who is reading the exercise design as well as the exercise, which for the last exercise in the book is not a bad outcome.
