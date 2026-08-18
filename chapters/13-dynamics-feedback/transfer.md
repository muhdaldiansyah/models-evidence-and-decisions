# Chapter 13 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0020`, which rests on **Accepted** `../../decisions/0007`.

## Transfer target

Per `spec.md`:

> Given a stock with named inflows and outflows, a table of flows over time, two delays of different kinds, and a written trigger rule, produce the stock trajectory, identify the minimum and when it occurs, show why the rule fires too late, price what the delay cost, propose a rule keyed to a different variable, and say what that repair costs.

## The changed task shape

Chapters 10 to 12 asked for a **decision**. Chapter 13 asks for a **trajectory** and then for a **diagnosis of a rule**.

That is a genuinely different demand, and it is the first time the book has asked for one. Every earlier transfer could be answered by reasoning about a static object — a table, a set of sources, a portfolio. These forms cannot be answered without running something forward.

**And unlike every earlier form, the arithmetic is trivial and the reasoning is not.** Seventeen rows of addition and subtraction, no formula, no probability. A reader who finds these forms easy has probably not done them.

## Form design

Both forms supply the same nine things, in the same order:

1. **A stock the organisation holds**, with a stated capacity and a stated critical level.
2. **Two named flows**, one controlled and one not.
3. **A seven-day shock** in the uncontrolled flow, followed by a return to baseline.
4. **A verification delay of two days** on the stock reading.
5. **A resupply delay of two days** on the controlled flow.
6. **A written operating rule keyed to the stock**, with a trigger and a stand-down.
7. **A capacity limit**, so that overshoot costs something real.
8. **An alternative rule keyed to the uncontrolled flow**, supplied in the produce items rather than in the setup.
9. **Eight produce items.**

| | Form A | Form B |
|---|---|---|
| Domain | Hospital platelet inventory | District heating fuel store |
| Stock | platelet units | wood pellets, tonnes |
| Inflow / outflow | deliveries / transfusions | deliveries / burn |
| Capacity | **120 units** | **780 t** |
| Critical level | **45 units** | **250 t** |
| Starting stock | **100** | **700** |
| Baseline flow | **30/day** | **180 t/day** |
| Peak of the shock | day 3 | day 3 |
| Minimum stock, unaided | **31 on day 7** | **190 on day 7** |
| Critical level crossed | **day 5** | **day 5** |
| Total drawdown | **69** | **510** |
| Stock rule fires | day 6 | day 6 |
| First extra arrives | **day 8** | **day 8** |
| Stock rule: minimum | **31 (unchanged)** | **190 (unchanged)** |
| Stock rule: extra ordered / lost | **111 / 22** | **636 / 46** |
| Flow rule: minimum | **50 on day 4** | **322 on day 4** |
| Flow rule: extra ordered / lost | **120 / 31** | **656 / 66** |
| Flow rule costs more, by a factor of | **1.41** | **1.43** |

All figures computed by simulating the stated rules before the forms were written.

### The four structural features, and why each is there

**The shock peaks on day 3 and the stock bottoms on day 7.** Four days apart in both forms, as in the chapter. A reader who has absorbed §3 finds day 7; a reader who has not finds day 3.

**Doing nothing leaves the stock permanently below the critical level.** In both forms the flows re-balance at baseline and the stock stays where the shock left it — 31 units against a critical 45, 190 tonnes against a critical 250. This is the fact readers most often refuse to believe, and it is the one that most directly transfers.

**The written rule fires on day 6 and delivers on day 8 — one day after the trough.** Not late by a margin that could be tuned away: raising Form A's trigger from 55 to 70 buys one day, moves the minimum from 31 to 34, and costs 13 more wasted units.

**The capacity limit makes overshoot cost something.** Without it, over-ordering is invisible; with it, the reader can put a number on the delay.

### What is held constant, and what is not

**The trade-off is reproduced at the chapter's own magnitude.** The water case's flow-keyed rule spilled 1.47 times what the stock-keyed rule spilled; Form A's costs 1.41 times as much and Form B's 1.43. That is deliberate — a reader who found the chapter's margin small should not find the forms' margin conveniently larger.

**What changes between the forms is what the waste *is*.** Form A's overshoot destroys a perishable clinical product with a short shelf life. Form B's is turned away at a gate and rescheduled — a wasted haulage movement, not a destroyed good.

**The mechanism is identical and the consequence is not**, and that is the transfer this pair is designed to test. A reader who reports both as "waste" without noticing that one is recoverable has carried the arithmetic across and not the judgment.

**Both forms end with the same honest position as the chapter**: neither rule dominates, and choosing between them requires knowing what the critical level costs to breach — which neither form supplies, deliberately.

### Deliberate difficulty features

**The arithmetic invites the wrong answer.** In both forms the flow's peak is unmistakable and the stock's trough is not. Item 2 is where the day-3 error appears if it is going to.

**The rule looks careful.** It has a numeric trigger, a proportional response, and a stand-down condition — everything Chapter 12 asked of a signpost. A reader who assesses it on its face will approve it.

**The stand-down condition is a no-op on days 3 and 4 in Form A**, because the store starts above the stand-down threshold and the order is already at the standing level. Readers who report this as an error have misread the rule; readers who notice and say it is harmless have read it properly.

**Item 5 asks for the cost of the delay, which requires two runs.** A reader who answers from one run cannot have priced anything, and this is the item that separates a worked answer from a described one.

**Item 7 asks what the flow-keyed rule costs, and the answer is "about 40 per cent more".** The expected failure is proposing the repair and stopping. The second expected failure is reporting Form B's turned-away tonnes as though they were destroyed.

**Item 8 asks what neither form supplies.** The answer is the cost of breaching the critical level, without which the two rules cannot be compared at all.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors, electricity distribution, charity fundraising, hospital estates, banking risk, higher education, food manufacturing, rail infrastructure, retail loss prevention, port and harbour infrastructure, health system diagnostic capacity.

District heating is new.

**One judgment recorded, and it is a close call.** Chapter 6's Form B concerned a **regional blood supply**, and Form A here concerns a hospital's platelet store. They are adjacent and the adjacency is deliberate rather than accidental: platelets are the clearest small-stock, short-shelf-life, delayed-resupply system in ordinary institutional life, and no substitute was as clean. **The questions do not overlap** — Chapter 6's form asked for a calibrated forecast and a score; this one asks for a trajectory and a rule diagnosis. Neither shares a quantity, an actor, or a decision with the other. **Flagged rather than left for a reader to notice**, and if a pilot finds the adjacency confusing, Form A should be moved to a domain with no blood in it at all.

**Neither domain is sensitive** in the sense `spec.md` uses. Form A concerns inventory management for a product whose supply is well understood; the form takes no position on transfusion practice and every clinical decision in it is somebody else's. Form B is municipal heating logistics.

## What a strong Form A answer should notice

- **The stock is platelet units; the inflow is deliveries and the outflow is transfusions.** Deliveries are controlled, transfusions are not.
- **Peak usage is day 3. Minimum stock is day 7. Four days apart.**
- **The critical level of 45 is crossed on day 5** — two days after usage peaked and began falling.
- **Doing nothing leaves the store at 31 units permanently**, 14 below the critical level, with deliveries exactly matching usage.
- **The rule fires on day 6** — seeing the day-4 figure of 50 — **and the first extra units arrive on day 8**, one day after the trough.
- **No adjustment of the trigger fixes it cheaply.** Raising it to 70 fires the rule on day 5 and delivers on day 7 — the minimum improves from 31 to 34, still below the critical level of 45, and the waste rises from 22 units to 35.
- **The stock rule orders 111 extra units and loses 22** to a full store.
- **The flow-keyed rule holds the minimum at 50 and never breaches the critical level** — and orders 120 extra and loses 31, about 40 per cent more waste.
- **Neither rule dominates**, and the comparison cannot be made without knowing what a breach costs.
- **The two delays add to four days**, against a shock that lasted seven.

## What a strong Form B answer should notice

- **The stock is pellets in the silo; the inflow is deliveries and the outflow is burn.**
- **Peak burn is day 3. Minimum stock is day 7. Four days apart.**
- **The critical level of 250 t is crossed on day 5.**
- **Doing nothing leaves the silo at 190 t permanently**, 60 t below the level at which the backup boiler must run.
- **The rule fires on day 6 and the first extra tonnes arrive on day 8.**
- **The stock rule orders 636 t extra and turns away 46 t.**
- **The flow-keyed rule holds the minimum at 322 t and never breaches** — at 656 t extra and 66 t turned away, about 40 per cent more.
- **A reader may object that pellets do not spoil**, so turned-away deliveries are a scheduling and haulage cost rather than a loss of the goods. That is correct, it is a real difference from Form A, and it should be credited: the *unit* of the overshoot cost is domain-specific even though the mechanism is not.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Stock with two named flows | ✓ | ✓ | ✓ |
| Shock length | 7 days | 7 days | ✓ |
| Peak of shock | day 3 | day 3 | ✓ |
| Trough of stock | day 7 | day 7 | ✓ |
| Critical level crossed | day 5 | day 5 | ✓ |
| Verification delay | 2 days | 2 days | ✓ |
| Resupply delay | 2 days | 2 days | ✓ |
| Do-nothing ends below critical | ✓ by 14 | ✓ by 60 | ✓ |
| Rule fires / delivers | day 6 / day 8 | day 6 / day 8 | ✓ |
| Rule fails to move the minimum | ✓ | ✓ | ✓ |
| Flow rule protects | ✓ | ✓ | ✓ |
| Flow rule costs more | ✓ 1.41× | ✓ 1.43× | ✓ |
| Produce items | 8 | 8 | ✓ |
| Word count | comparable | comparable | ✓ |

**One deliberate non-match, and it is the point of the pair.** Form A's overshoot destroys a perishable product; Form B's is turned away at the gate and rescheduled. The mechanism is identical and the consequence is not, which is a transfer feature rather than a defect — but it means the two forms' overshoot figures are not directly comparable, and the rubric says so.

## Rubric-to-item mapping

| Rubric dimension | Produce item |
|---|---|
| Stock and flows named | 1 |
| The trajectory and its trough | 2 |
| The critical crossing, and when | 3 |
| Why doing nothing does not recover | 4 |
| The delays, added, and what they cost | 5 |
| Why the rule fires too late | 6 |
| The flow-keyed repair, and its price | 7 |
| What the form does not supply | 8 |

**Every dimension has a dedicated item**, as in Chapters 10 to 12.

## Pilot notes

Untested. Five things a pilot should measure.

**Time.** 45 minutes for eight items with seventeen rows of arithmetic. Probably generous, and if it is, the fix is to add a third rule rather than to lengthen the table.

**Whether readers find day 7.** This is the single measurement the chapter most wants. If a large fraction report day 3, §3 did not land and the fix is a second worked accumulation before the transfer, not more prose.

**Whether readers believe the do-nothing result.** Item 4 exists because the permanent shortfall is the most counterintuitive fact in the chapter. If answers hedge — *presumably it would recover eventually* — the fix is in §3, which should show the arithmetic of recovery explicitly.

**Whether the flow-keyed repair is proposed with its price.** If most answers propose it and stop, item 7's wording is too inviting and should ask for the cost first.

**Whether item 8 produces the right absence.** The expected answer is the cost of a breach. Answers naming the demand forecast or the delay lengths have found real absences that the form does in fact supply, and that is a reading failure worth measuring.
