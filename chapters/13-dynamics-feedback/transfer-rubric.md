# Chapter 13 — Cold-Transfer Rubric

**Do not open this before your response is complete.**

This is a review instrument, not a mark scheme. Nothing here is scored and nothing is recorded.
Read only the section for the form you worked.

Both forms have a single structure: a stock that bottoms out four days after the shock peaks, a written rule that cannot fire in time, and a repair that works and costs more.

---

## Form A — the platelet store

### 1. Stock and flows

**The stock is platelet units held.**
**The inflow is deliveries from the blood service. The outflow is units transfused.**

**The hospital controls deliveries and does not control transfusions.**

Answers that name usage as something the hospital "manages" have missed the asymmetry, and the asymmetry is why the rest of the form is hard. If you could set usage you would not need a rule.

### 2. The trajectory

| Day | Used | Net | Stock |
|---|---:|---:|---:|
| 1 | 38 | −8 | 92 |
| 2 | 42 | −12 | 80 |
| 3 | **46** | −16 | 64 |
| 4 | 44 | −14 | 50 |
| 5 | 40 | −10 | **40** |
| 6 | 36 | −6 | 34 |
| 7 | 33 | −3 | **31** |
| 8–12 | 30 | 0 | 31 |

**Usage peaks on day 3. The store bottoms out on day 7, at 31 units. Four days apart.**

Total drawdown 69 units, which is the sum of the seven net flows.

**If you put the minimum on day 3 or day 4**, you made the error this chapter is about: you gave the stock the shape of the flow. From day 4 the deficit shrinks every day — 14, 10, 6, 3 — and the store falls every day, because a shrinking deficit is still a deficit.

### 3. The critical crossing

**Day 5, at 40 units.**

**Two days after usage peaked and began falling.**

The hospital cancels elective lists while the emergency is receding, and there is no moment at which anything visibly happens — the store passes 45 in the ordinary course of falling by ten, the same as the day before.

**Stocks cross thresholds quietly.** A strong answer says so.

### 4. Why doing nothing does not recover

**The store stays at 31 units. Indefinitely.**

Deliveries are 30 and usage is 30. The flows are balanced, so nothing changes, and the store sits 14 units below the level at which the hospital cancels surgery — with nothing visibly wrong and no alarm.

**Balanced flows hold a stock where it is. They do not restore it.**

To get back to 100, somebody has to order a surplus and keep ordering it. At 5 extra units a day it takes 14 days.

**This is the item readers most often hedge on.** If you wrote that the store "would presumably recover over time", check the arithmetic: name the surplus that would do it, and you will find you have to invent one.

### 5. The delays, and what they cost

**Verification delay: 2 days.** The store changes before the operator sees it.
**Resupply delay: 2 days.** The order changes before the store feels it.
**Sum: 4 days**, against a shock that lasted 7.

**With both delays at zero, the written rule holds the minimum at 50 units on day 4** and never breaches the critical level.

Work it: on day 5 the operator would see the day-4 figure of 50, fire the rule, order 44 plus 12, and have 56 units arrive that day.

**So the delay is what cost the protection, and the trigger variable is not the underlying problem.** That is the most important thing on this page, and it is why item 7's repair should be understood as a workaround rather than a fix.

An answer that reports the two delays without adding them has not done the item. **Four days is the number that matters**, because it is what you compare against the length of the disturbance.

### 6. Why the rule fires too late

| Day | Sees | Rule | Order | Delivered | Stock |
|---|---:|---|---:|---:|---:|
| 4 | 80 | between | — | 30 | 50 |
| 5 | 64 | between | — | 30 | 40 |
| 6 | **50** | **fires** | 56 | 30 | 34 |
| 7 | 40 | fires | 52 | 30 | **31** |
| 8 | 34 | fires | 48 | **56** | 57 |
| 9 | 31 | fires | 45 | 52 | 79 |
| 10 | 57 | between | — | 48 | 97 |
| 11 | 79 | between | — | 45 | 112 |
| 12 | 97 | stand down | 30 | 45 | **120** (7 lost) |
| 13 | 112 | stand down | 30 | 45 | **120** (15 lost) |
| 14 | 120 | stand down | 30 | 30 | 120 |

**The rule fires on day 6 and the first extra units arrive on day 8 — one day after the trough.**

**The minimum is 31 units, exactly what it was with no rule at all.**

**And the reason is not the trigger value.** Actual stock first falls below 55 on day 4. The operator sees that on day 6. Units arrive on day 8 at the earliest.

**Raising the trigger does not buy much and is not free.** At 70 the rule fires on day 5 and delivers on day 7 — the minimum improves from 31 to 34, still well below the critical level of 45 — and the waste rises from 22 units to 35. At 80 nothing further changes, because the store does not pass 80 any earlier than it passes 70.

**By the time a stock has fallen far enough to alarm you, the flows that drew it down have been running for days.** That is the finding, and it is a property of stocks rather than of this hospital.

**Extra ordered: 111 units. Lost to a full store: 22.**

**Do not credit** an answer that blames the consultant's leave or the duty operator's authority. The rule is a written object that could have been analysed in an afternoon by anyone who added the two delays together.

**Note also**, without treating it as an error: the stand-down condition fires on day 3, because the day-1 figure of 92 is above 85 — and does nothing, because the order is already at the standing level. Readers who spot this and say it is harmless have read the rule properly.

### 7. The flow-keyed repair, and its price

A rule that works: *when the most recent verified usage exceeds 36 units a day, set the order to that usage plus 12; otherwise return to the standing 30.*

Usage rises on day 1, so the rule fires on day 3 and units arrive on day 5.

| | Do nothing | Written rule | Usage-keyed rule |
|---|---:|---:|---:|
| Minimum stock | 31 (day 7) | 31 (day 7) | **50 (day 4)** |
| Days below the critical level | permanently | 5–7 | **none** |
| Extra units ordered | 0 | 111 | 120 |
| Units lost to a full store | 0 | **22** | **31** |

**The repair costs about 40 per cent more in wasted units**, because a rule that fires on the first sign of demand fires earlier and harder than one that waits for evidence in the stock.

**And these are units with a five-day shelf life**, so a lost unit is destroyed rather than delayed. Hold on to that when you meet Form B.

**An answer that proposes the repair and stops has done half the item.** The chapter's position, and this rubric's, is that neither rule dominates.

**Also credit** an answer noting that the usage-keyed rule with delays achieves exactly what the stock-keyed rule achieves without them — minimum 50 on day 4 in both cases. Watching the flow is a way of buying back the four days, not a way of removing them.

### 8. What the form does not supply

**The cost of breaching the critical level.**

Without it, the comparison in item 7 cannot be made. One rule wastes 22 units and cancels elective lists for three days; the other wastes 31 and cancels none. Which is better depends entirely on what a cancelled list costs relative to a wasted unit, and the form does not say.

**Also creditable**, as second answers: how long a wasted unit's shelf life would have allowed it to be held; whether the blood service could have been asked to hold stock on the hospital's behalf; whether the shock was foreseeable from the collision itself.

**Not creditable:** the demand table, the delays, and the capacity are all supplied. An answer naming those has misread the form.

---

## Form B — the pellet silo

### 1. Stock and flows

**The stock is pellets in the silo. The inflow is deliveries; the outflow is the burn.**

**The network controls deliveries and does not control the burn**, which is set by the weather and by 4,000 households.

### 2. The trajectory

| Day | Burned | Net | Silo |
|---|---:|---:|---:|
| 1 | 240 | −60 | 640 |
| 2 | 270 | −90 | 550 |
| 3 | **300** | −120 | 430 |
| 4 | 288 | −108 | 322 |
| 5 | 258 | −78 | **244** |
| 6 | 216 | −36 | 208 |
| 7 | 198 | −18 | **190** |
| 8–12 | 180 | 0 | 190 |

**The burn peaks on day 3. The silo bottoms out on day 7, at 190 t. Four days apart.**

Total drawdown 510 t, the sum of the seven net flows.

### 3. The critical crossing

**Day 5, at 244 t. Two days after the burn peaked.**

The backup gas boiler comes on — at four times the fuel cost — while the cold snap is easing.

### 4. Why doing nothing does not recover

**The silo stays at 190 t indefinitely**, 60 t below the level at which the gas boiler must run, with deliveries exactly matching the burn.

At 20 t/day of surplus it takes 26 days to get back to 700.

### 5. The delays, and what they cost

**Two days of verification plus two days of haulage is four days**, against a cold snap that lasted seven.

**With both delays at zero, the written rule holds the minimum at 322 t on day 4** and never breaches the critical level. On day 5 the operator would see the day-4 figure of 322, fire the rule, order 288 plus 60, and have 348 t arrive that day — the same protection the burn-keyed rule achieves *with* the delays.

**The delay is what cost the protection.**

### 6. Why the rule fires too late

**The rule fires on day 6, seeing the day-4 figure of 322. The first extra tonnes arrive on day 8 — one day after the trough. The minimum is 190 t, unchanged.**

Actual silo level first falls below 350 on day 4. The operator sees it on day 6. Pellets arrive on day 8 at the earliest.

**Extra delivered: 636 t. Turned away at the gate: 46 t**, on day 13, when the silo is full and the delivery is still running at 258.

### 7. The flow-keyed repair, and its price

*When the most recent verified burn exceeds 230 t a day, set the delivery to that burn plus 40; otherwise return to the standing 180.*

| | Do nothing | Written rule | Burn-keyed rule |
|---|---:|---:|---:|
| Minimum silo | 190 (day 7) | 190 (day 7) | **322 (day 4)** |
| Days below the critical level | permanently | 5–7 | **none** |
| Extra tonnes delivered | 0 | 636 | 656 |
| Tonnes turned away | 0 | **46** | **66** |

**About 40 per cent more waste**, for a repair that never breaches the critical level.

**Your rule will not be this one**, and it does not need to be. What it needs is a trigger on the burn, a stated response, and a stand-down — and then the two figures in the bottom two rows, computed rather than asserted.

**A reader who observes that pellets do not spoil is right and should be credited.** A turned-away delivery is a wasted haulage movement and a scheduling problem, not a destroyed good — the supplier takes it back. That is a real difference from a perishable stock, and it means the *unit* of the overshoot cost is domain-specific even though the mechanism is not. It also means that the 66 t in the table is a softer number than Form A's 31 units, even though 66 is the larger figure — a difference the arithmetic cannot show you and the domain can.

### 8. What the form does not supply

**The cost of running the backup boiler.**

The form says it is four times the fuel cost and does not say for how long or on what volume. Without it, three days of gas cannot be weighed against 20 t of extra haulage and 20 t turned away.

**Also creditable:** whether the supplier charges for turned-away loads; whether the silo could have been filled higher before winter; whether the cold snap was forecast.

---

## The trap in both forms

**The rule looks careful.**

It has a numeric trigger, a response proportional to the observed situation, and a stand-down condition. It is more specific than most operating instructions, and it is exactly what Chapter 12 said a signpost needs.

**And it cannot work**, for a reason that is visible in four days of arithmetic and that nobody did.

If you assessed the rule by reading it rather than by running it, that is the finding. A rule keyed to a stock is a claim that the stock will move far enough, soon enough, to leave room for the response — and that claim is checkable in advance.

## Four answers that look right and are not

**"The minimum is on day 3, when demand peaks."**
The stock turns where the net flow crosses zero, not where it peaks. The trough is four days later.

**"The store recovers once demand returns to normal."**
Balanced flows hold a stock where they find it. Recovery requires a surplus, and nobody ordered one.

**"The trigger was set too low — raise it and the rule works."**
Raise it enough to fire in time and it fires in ordinary weeks too. The problem is the four days, not the number.

**"Watch the flow instead of the stock."**
Correct, and incomplete. It costs about 40 per cent more in waste, and whether that is worth paying depends on a number neither form gives you.

## A note on tone

Both forms describe an organisation whose rule failed while the person who might have overridden it was away.

**That is scenery, not explanation.** The rule would have failed with everybody present, because the loop delay is four days and the shock lasted seven. An answer that locates the failure in the absence has explained a coincidence.

## Post-task self-explanation

Before returning to the chapter, write two sentences on this:

**Which item would you have got wrong if you had read §3 of the chapter and stopped there?**
