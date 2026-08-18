# Chapter 14 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0021`.

## Transfer target

Per `spec.md`:

> Given a repeated decision with a written rule, several histories over which to compare rules, two states the instruments cannot distinguish, and two model parameters that enter only as a sum, evaluate the rules across all histories, identify which comparisons the histories cannot settle, say which failure is structural and which is practical, and decide whether to buy the instrument that would fix both.

## The changed task shape

Chapter 13's forms asked the reader to **compute a trajectory**. Chapter 14's ask the reader to **interpret a table somebody else computed, and then ask the questions the table cannot answer.**

That inversion is deliberate and it is the point of the pair.

**The arithmetic in these forms is trivial** — four columns of five numbers, added and minimised. It takes six minutes. **Everything else takes forty**, and every one of the remaining items is a question about what the numbers cannot settle: which comparisons the histories do not discriminate, which states the instruments cannot separate, which parameters cannot be told apart, and what an instrument is worth when no probability is available.

**A reader who spends the session computing has misread the forms**, and that is a measurable outcome a pilot should look for.

## Form design

Both forms supply the same nine things, in the same order:

1. **A repeated decision**, made on a fixed cycle by an organisation.
2. **A written rule in force for eleven years**, quoted.
3. **Three alternative rules**, one minimal, one keyed to a different variable, one conjunctive.
4. **Five histories**, pre-computed against four measures.
5. **One history on which all four rules are identical.**
6. **A second history on which the two live candidates are identical.**
7. **A list of exactly what the organisation records.**
8. **A fitted model with two parameters entering only in combination**, and three splits that fit equally well.
9. **One instrument that resolves both failures**, priced against a decision already stated.

| | Form A | Form B |
|---|---|---|
| Domain | Regional electricity grid operation | County winter road service |
| Decision | daily reserve procurement | nightly gritting |
| Rule in force | margin-keyed, 11 years | depot-sensor-keyed, 11 years |
| Dominated rule | **R1, by R3** | **G1, by G3** |
| Live candidates | R2 and R3 | G2 and G3 |
| Histories carrying no information about that choice | **2 of 5** | **2 of 5** |
| Two states, one signature | high demand vs undelivered declared availability | no ice vs ice nobody drove on |
| Two parameters, one combination | baseline + embedded generation shortfall = **31,400 MW** | base exposure − residual salt protection = **46** |
| Instrument | per-unit telemetry, **£240,000** | surface-state sensors, **£96,000** |
| Decision it informs | **£5,100,000** | **£2,100,000** |
| Instrument as a share | **4.7%** | **4.6%** |

All figures were checked for internal consistency before the forms were written: every totals row, every dominance claim, and every identical-history claim was verified by computation.

### The four structural features, and why each is there

**The eleven-year-old rule** is there so that the dominated result lands on something that has survived a long time. A rule adopted last year being beaten is unremarkable; a rule that has been in force for eleven years being beaten on every measure is the finding.

**The identical history** is what makes item 3 answerable. Without a row where every rule agrees, the exploration point has to be asserted, and the chapter's own case shows that asserting it does not work.

**The two states with one signature** are chosen so that the wrong response actively makes things worse — reserve procured against a generator that cannot deliver does not help, and salt spread on a road nobody drives does not appear in the incident record either way.

**The parameters entering only in combination** are chosen so that the affected decision is the organisation's largest, which is what makes item 7 bite.

### What is deliberately not parallel

**Form A's parameters enter as a sum; Form B's enter as a difference.** Both are structural non-identifiability and neither is fixed by more of the same data, but a reader who has learned "look for two things added together" will have to generalise slightly to see Form B's.

**Form A's measures point in different directions** — a higher margin is better, fewer hours below standard is better. **Form B's ice-hours are lower-is-better**, which the form states explicitly. Readers who compute a "worst" by taking a minimum in Form B will get it backwards, and the rubric names that.

### Deliberate difficulty features

**Item 1 is easy and is not the point.** It exists so that the reader has handled the numbers before item 2 asks them to reason about them.

**Item 2 asks for the diagnosis and then immediately guards against the wrong one.** *Being careful to distinguish it from writing a bad rule* is in the prompt because the expected failure is to conclude that the organisation was incompetent. The failure is not writing a bad rule; it is never comparing.

**Item 5 says "say precisely what follows for every rule in the table."** The expected shortfall is to identify the ambiguity and stop. What follows is that all four rules fire on a signal whose cause they cannot determine, and that in one of the two causes the response is useless or harmful.

**Item 6 says "explain your answer in terms of the model rather than in terms of the data."** This is the item that tests whether the reader has understood that structural non-identifiability is diagnosable before collection. An answer reasoning about sample sizes has missed it.

**Item 8 ends with "if you cannot compute what it is worth, say why not."** The prompt invites the reader to notice the absence of a probability. Readers who invent one and compute an expected value have done something the chapter explicitly declines to do — and it is worth measuring how many do.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors, electricity distribution, charity fundraising, hospital estates, banking risk, higher education, food manufacturing, rail infrastructure, retail loss prevention, port and harbour infrastructure, health system diagnostic capacity, hospital platelet inventory, district heating.

County winter road service is new.

**One judgment recorded.** Chapter 11's Form A concerned rail infrastructure and an earlier contrast used **electricity distribution**; Form A here is **electricity transmission and system operation**, which is a different actor, a different asset class, and a different decision — procuring reserve, not maintaining a network. The adjacency is real and is flagged rather than left for a reader to notice. Similarly, Chapter 4's contrast used **city pothole records** and Form B here is a county highways authority; the two share a road and nothing else — one is about how records come to exist, this one is about choosing a nightly rule.

**Neither domain is sensitive** in the sense `spec.md` uses. Form A is commercial system operation. Form B concerns road safety at one remove: every rule in it is a gritting rule, the form takes no position on any authority's winter service policy, and no clinical, legal, or safety recommendation is offered or implied.

## What a strong Form A answer should notice

- **Totals: R0 150 / 30 / 0 / 0; R1 210 / 11 / 660 / 5,050; R2 560 / 0 / 1,050 / 5,800; R3 470 / 1 / 300 / 4,200.**
- **R1 is dominated by R3 on all four measures.**
- **The operator's failure is not writing R1; it is never comparing R1 with anything.** A rule never compared is a rule nobody chose.
- **Two of the five winters — mild and long cold — cannot distinguish R2 from R3.** At one winter a year, and three informative winters in five, settling the choice by running one of them is a decade-scale project.
- **The remaining choice is one hour below the security standard against 750 MWh of unused reserve**, and the table does not price either.
- **The four instruments cannot separate high demand from undelivered declared availability**, because declared availability is a submission rather than a measurement. All four rules therefore fire on a signal whose cause is unknown, and procuring more reserve against a fleet that has over-declared buys capacity that also may not appear.
- **The demand model's baseline and embedded generation shortfall enter only as a sum**, so no quantity of the same data separates them. This is knowable from the model's form.
- **Item 5's problem is fixable by a different instrument; item 6's is not fixable by more data of the same kind.** The alternative to collecting more is to drop the distinction and report the sum, saying so.
- **The instrument costs 4.7% of the decision it informs**, which means it cannot be screened out on cost — and that is not the same as being worth buying. **No expected value can be computed, because no probability over the splits is available.**

## What a strong Form B answer should notice

- **Totals: G0 480 / 30 / 0 / 0; G1 290 / 11 / 33 / 3,920; G2 110 / 0 / 53 / 4,500; G3 130 / 1 / 16 / 3,250.** Worst ice-hours is a **maximum**, because lower is better.
- **G1 is dominated by G3 on all four measures.**
- **Two of the five winters — mild and long frost — cannot distinguish G2 from G3.**
- **The remaining choice is one night above the service threshold against 37 wasted runs and 1,250 tonnes of salt.**
- **The records cannot separate "no ice" from "ice nobody drove on"**, because the authority's outcome measure is incident reports and an untravelled icy road generates none. **The rules are therefore being evaluated against a measure that is partly a measure of traffic.**
- **The ice model's base exposure and residual salt protection enter only through their difference**, so more of the same data will not separate them.
- **The instrument costs 4.6% of the decision it informs.**
- **A reader who observes that the incident-report problem also corrupts the table itself is right and should be credited.** Three of the four measures in the table are recorded quantities, and "ice-affected road-hours" is estimated from a model whose parameters item 6 shows are not separately determinable. The table is less solid than it looks, and saying so is the strongest available answer.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Repeated decision on a fixed cycle | ✓ | ✓ | ✓ |
| Written rule, 11 years | ✓ | ✓ | ✓ |
| Four rules, five histories | ✓ | ✓ | ✓ |
| One history identical across all four | ✓ mild | ✓ mild | ✓ |
| Live candidates identical on two histories | ✓ | ✓ | ✓ |
| Dominated rule | ✓ R1 by R3 | ✓ G1 by G3 | ✓ |
| Two states, one signature | ✓ | ✓ | ✓ |
| Two parameters, one combination | ✓ sum | ✓ difference | deliberately not identical |
| Instrument resolves both | ✓ | ✓ | ✓ |
| Instrument as share of decision | 4.7% | 4.6% | ✓ |
| Produce items | 8 | 8 | ✓ |
| Word count | comparable | comparable | ✓ |

## Rubric-to-item mapping

| Rubric dimension | Produce item |
|---|---|
| Totals computed | 1 |
| Dominance found, and diagnosed correctly | 2 |
| Uninformative histories counted | 3 |
| The undecidable remainder named | 4 |
| Observability | 5 |
| Structural non-identifiability | 6 |
| Structural versus practical | 7 |
| The instrument, and the missing probability | 8 |

**Every dimension has a dedicated item**, as in Chapters 10 to 13.

## Pilot notes

Untested. Five things a pilot should measure.

**Time split.** If readers spend more than fifteen minutes on item 1, the forms read as arithmetic exercises and the framing needs changing.

**Whether item 2's guard works.** If answers say the organisation was incompetent, the prompt's second clause is not doing its job and §2 of the chapter needs to be blunter about P1 having been reasonable to write.

**Whether item 6 is answered from the model or from the data.** This is the single measurement the chapter most wants. An answer reasoning about sample sizes has missed the chapter's most useful check.

**Whether anyone invents a probability at item 8.** The prompt offers an exit. Readers who compute an expected value anyway have reverted to Chapter 11 and skipped Chapter 12, and the rate is worth knowing.

**Whether Form B's readers notice the measure is partly a measure of traffic.** That is the hardest available observation and it is not required for a good answer. If nobody finds it, the form is working as intended; if several do, the chapter's §3 could ask for it directly.
