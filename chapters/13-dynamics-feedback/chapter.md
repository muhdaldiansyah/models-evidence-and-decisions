---
chapter: 13
part: 4
title: "Dynamics, Feedback, and Stability"
status: drafted
---

# Chapter 13: Dynamics, Feedback, and Stability

## 1. The Reservoir Does Not Hold Still

Chapter 12 ended by naming what it had assumed.

Through twelve chapters, the network sat there and the utility acted on it.
The demand forecast might be wrong, the mechanism might be either of two, the future might be one of three — but in all of it the system was a thing to be analysed, and the analysis was a thing done to it.

**That is not what a water network does.**

It carries water forward from one day to the next.
It responds to what the utility does, on a schedule the utility does not choose.
And the responses come back round and change what the utility sees, which changes what it does next.

Part IV is about that, and this chapter is the simplest version: **what happens when the effect of an action feeds back into its own cause.**

### Before reading further

Here is the utility's reservoir over a seven-day heatwave.

Storage at the start of day 1 is **220 ML**.
Production runs at the standing level of **100 ML/day** throughout, because nobody has ordered a change.
Demand, in ML/day, is:

| Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Demand | 118 | 124 | 128 | 126 | 120 | 112 | 104 |

**Allow about eight minutes and write three things down.**

**What is the storage at the end of each day?**

**On which day is storage at its lowest?**

**On which day should the utility have started to worry, and why that day?**

Do this before reading on.
It matters more here than in any previous chapter that you produce an answer rather than recognise one, and §3 will say why.

This is a version of an instrument that has been administered to several hundred graduate students at a well-known business school.
Their results are in §3.
Nothing more about them until then.

### Why this one is worth doing properly

Every chapter of this book has opened by asking for something before teaching it, and the reason has always been the same: you cannot compare your answer to the chapter's if you never wrote one down.

**This chapter's opening task is different in one respect.** In the earlier chapters, the thing being tested was whether you had a concept — a target quantity, an objective, a payoff table.
If you had not met the concept, of course you did not use it, and the comparison was gentle.

**Here the task requires nothing you have not had since primary school.** It is addition and subtraction on seven numbers.
There is no concept to be missing.

**Which is why the results are worth having**, and why §3 will spend two pages on them rather than a paragraph.

### What this chapter is for

Chapter 1 taught you to ask a set of questions and deliberately withheld the words for the answers.

*What carries over from one period to the next?*
*What adds to it, and what removes from it?*
*What is delayed?*
*Does what you do change what you will later see?*

You have been asking those questions for twelve chapters without a vocabulary.
This chapter supplies it, and then shows you what the vocabulary buys.

### What you will be able to do

Run a quantity forward through a table of flows and say where it turns, which is not where most people put it.

Distinguish the two kinds of delay, add them, and work out whether a correction can arrive in time.

Tell an **equilibrium** from a **stability** — a system sitting still from a system that would come back if you knocked it.

Say why a rule that looks careful produced an overshoot, without concluding that anybody was careless.

And name the thing that happens when an intervention is defeated by the system's response to the intervention itself.

## 2. What Carries Forward

Chapter 2 introduced **state** as *what must be carried forward to answer the question*, and then refused to go further.

This is further.

### Stocks and flows

A **stock** is a quantity that accumulates.
A **flow** is a rate that adds to it or takes away from it.

The distinction is old and it is everywhere, which is the first reason to learn it once rather than four times.

> "Stocks and the flows that alter them (the concepts of prevalence and incidence in epidemiology) are fundamental in disciplines from accounting to zoology: a population is increased by births and decreased by mortality; the burden of mercury in a child's body is increased by ingestion and decreased by excretion." [@sterman2006evidence, p. 508]

Prevalence and incidence.
Balance and cash flow.
Population and births.
Four vocabularies, one distinction — and an analyst who has learned it in one of them has learned it in all four.

### Flows come in pairs

Notice the grammar of the source's examples.

*Increased by births and decreased by mortality.*
*Increased by ingestion and decreased by excretion.*

**Every stock has at least one inflow and at least one outflow, and a stock with only its inflow named has not been analysed.**

This sounds trivial and is not.
The commonest way to get a stock wrong is to attend to the flow somebody is arguing about and forget the other one — to track production and not demand, admissions and not discharges, hiring and not attrition.

**Chapter 4 already caught the book doing a version of this.** The utility's demand figure was never measured; it was production minus metered consumption, a subtraction residual containing about a third of things that were neither Hillcrest nor demand.
That was a flow reconstructed from other flows, and the reconstruction absorbed everything nobody had named.

### And a stock is not any quantity that changes

This is the mistake the vocabulary invites, and it is worth stopping on.

`decisions/0007` guards it with a specific case, and the case is a good one.
The temperature inside a refrigerated warehouse changes over time.
It rises when the door is opened and falls when the plant runs.
**It is not a stock.**

Temperature is not accumulating anything.
There is no quantity of temperature flowing in and out; the temperature is a *state* of the air, and what accumulates is heat.
You can model the warehouse with heat as the stock and temperature as its indicator, and that model will be right — but calling temperature itself a stock will produce nonsense the moment you try to name its flows.

**The test is not "does it change over time".** Almost everything changes over time.

**The test is: is this quantity the running total of something?**
If you can name what flows in and what flows out, and the quantity is their accumulated difference, it is a stock.
If you cannot, it is a variable, and it may well be an important one.

### Why the pairing is the hard part

There is a reason flows are easy to name badly, and it is worth seeing before the case arrives.

**Organisations are built around flows and report stocks as an afterthought.** A treatment works has a production target.
A hospital ward has an admissions rate.
A charity has a fundraising figure.
Somebody owns each of those numbers, is measured on it, and reports it monthly.

**The stock usually belongs to nobody.** Reservoir storage is a consequence of two departments' work and the responsibility of neither.
So it appears in the pack as a level, without a trend, and nobody has to explain it.

**And the outflow is worse.** Production is a decision and demand is a fact; the utility employs people to hit the first and nobody to forecast the second.
Chapter 4 found that the demand figure was not even measured — it was what remained after subtracting.

**So the predictable failure is asymmetric.** When an organisation gets a stock wrong, it is almost always because it was watching the flow it controls and not the flow it does not.

### The case's stock

**The stock is usable stored water**, measured in megalitres, and you have known it since Chapter 1 — it is the reading Chapter 1 discovered might be wrong.

**The inflow is treated production.**

**The outflow is demand**, which includes leakage, and which Chapter 4 showed was never measured directly.

That is the whole system for the next four sections.
One stock, two flows, and a set of dates.

The reservoir holds **260 ML** at capacity.
The utility's operating target is **220 ML**.
Below **120 ML** the utility breaches its own service standard, and that figure is called the critical level.

### What the word buys you

It is fair to ask what naming any of this achieves, given that the reader could already add and subtract.

**Three things, and the third is the one that matters.**

**It tells you what to look for.** Faced with an unfamiliar situation, *what is the stock here* is a question with an answer, and finding it usually locates the problem.

**It tells you what question to ask next.** Once you have a stock you need both its flows, and asking for the one nobody tracks is often the whole of the analysis.

**And it tells you which reasoning is available.** A stock has properties a flow does not: it has history, it cannot jump, and it can only be changed by changing a flow and waiting.
Every one of those is a constraint on what any intervention can do, and none of them is visible if you have not identified the stock.

**That last point is why this chapter comes before Chapter 14 rather than after it.** You cannot sensibly design a rule for changing something until you know what kind of thing it is.

### A word named and not used

The set of all the states a system could be in is called its **state space**.

Chapter 2 promised the term would not be named until here, and here it is.
It will not be used again in this book.
It is named because you will meet it, and because you should know that when somebody says *state space* they mean the set of possibilities and not a technique.

### Where the stocks are in this book

It is worth noticing how much of the book has been about stocks without saying so.

**Chapter 1's storage reading** is a stock, and the chapter's whole difficulty was that the reading might not match it.

**Chapter 4's demand figure** is a flow, reconstructed by subtracting one flow from another, and the reconstruction is why it contained a third of things that were neither Hillcrest nor demand.

**Chapter 7's sixty-eight-year-old main** is neither.
It is a piece of the system's structure — the thing that determines what the flows do.

**Chapter 12's capital envelope** is a stock, drawn down by scheme commitments, and one of the reasons the ranking failed is that indivisible commitments draw it down in lumps.

**None of those chapters needed the word.** Each did its job without it.
But the vocabulary makes visible something they had in common, and what they had in common is that in every case the difficulty lay in the relationship between a level and the rates that move it.

### Task: name the parts

Before §3, write down:

- the stock in the Hillcrest pressure problem from Chapter 7;
- both of its flows;
- one quantity in the water case that varies over time and is **not** a stock, with the reason.

Two minutes.
The answers are not printed; §8 returns to them.

## 3. Accumulation, and Why It Is Hard

Here is the trajectory.

| Day | Demand | Net flow | Storage at end of day |
|---|---:|---:|---:|
| 1 | 118 | −18 | **202** |
| 2 | 124 | −24 | **178** |
| 3 | **128** | −28 | **150** |
| 4 | 126 | −26 | **124** |
| 5 | 120 | −20 | **104** |
| 6 | 112 | −12 | **92** |
| 7 | 104 | −4 | **88** |

Compare it with what you wrote.

### Four facts

**Peak demand is day 3.**

**Minimum storage is day 7.**

**They are four days apart.**

And the fourth, which is the operational one: **storage crosses the critical level of 120 ML on day 5** — two days after demand peaked and started coming down.

The utility breached its own service standard while the weather was improving.

### Pause: why is storage still falling?

Look at the net flow column from day 4 onward.

**−26, −20, −12, −4.**

The deficit shrinks every single day.
Demand is falling, the gap is closing, and by day 7 the utility is only four megalitres short.

**And storage falls every single day, from 124 to 88.**

Why?

Write a sentence before reading on.

### The answer, and the principle

Storage falls on day 7 because on day 7 the utility used more water than it made.

That is all.
A shrinking deficit is still a deficit, and a stock falls whenever its net flow is negative, however small.

The general principle is the one sentence in this chapter worth memorising:

> "stocks integrate (accumulate) their net inflows. A stock rises even as its net inflow falls, as long as the net inflow is positive: the national debt rises even as the deficit falls—debt falls only when the government runs a surplus; the number of people living with HIV continues to rise even as incidence falls—prevalence falls only when infection falls below mortality." [@sterman2006evidence, p. 508]

Debt and deficit.
Prevalence and incidence.
Storage and net flow.

**The stock turns when the flow crosses zero, not when the flow peaks.**

### The error has a name and a shape

The source names it in the sentence before:

> "Most people assume that system inputs and outputs are correlated (e.g., the higher the federal budget deficit, the greater the national debt will be)." [@sterman2006evidence, p. 508]

On this case, that assumption produces a specific and predictable wrong answer.

**If you think storage should look like demand, you turn storage upward on day 4**, because that is when demand peaks and starts to fall.

The actual trough is three days later.

Go back to what you wrote in §1.
If your minimum was day 4, you made the error the source names, on the case the book gave you, having been warned by Chapter 1 to look for exactly this.

That is not a remark about you.
It is the finding.

### One more thing the trajectory shows

Look again at where the critical level is crossed.

**Day 5, at 104 ML.**

Demand peaked on day 3 and has been falling for two days.
Anybody watching the weather is relaxing.
Anybody watching demand is reporting good news.
And the reservoir goes through the floor.

**This is the accumulation point in its operationally nastiest form.** The variable everybody is watching turned two days ago, and the variable that triggers a breach has not turned yet — it will not turn for another two days, and it will not recover at all.

**Note also what the crossing does not look like.** There is no discontinuity, no alarm, no day on which something visibly happens.
Storage passes 120 in the ordinary course of falling by twenty megalitres, the same as it fell the day before and the day after.

**Stocks cross thresholds quietly.** That is a property of accumulation and not a failing of anybody's instrumentation, and it is why thresholds on stocks need forecasting rather than monitoring.

### Now the measurement

Two researchers built a set of short tasks to test how well people reason about stocks, flows, delays, and feedback, and administered them to graduate students at MIT's business school [@boothsweeney2000bathtub].

The simplest task showed a graph of an inflow and an outflow over time and asked for the stock.

**Mean score: 0.77.**

A second, slightly harder version of the same task: **0.48.**

A version dressed as a manufacturing problem: **0.41.**

The authors' own summary:

> "Table 2 summarizes overall performance. In general, performance is poor." [@boothsweeney2000bathtub, p. 264]

**And the failures cluster on exactly the two ideas §3 has been about.** On the simplest task, the criterion that the slope of the stock is the net rate scored **0.66**, and the criterion that the quantity added to the stock over an interval is the area under the net rate scored **0.63** [@boothsweeney2000bathtub, p. 265].

The named misconception, from the discussion:

> "Many subjects appear to believe that the stock trajectory should have the same qualitative shape as the net rate." [@boothsweeney2000bathtub, p. 278]

That is the day-4 answer, written down by researchers six years before this book's case existed.

### The two obvious objections, answered by the authors

**They had not studied it.**

> "These concepts are the most basic and intuitive features of accumulation. Further, they are the fundamental concepts of calculus, a subject all MIT students are required to have." [@boothsweeney2000bathtub, p. 265]

**They made arithmetic slips.**

> "It is possible that their poor performance arose from numerical errors in the required computations, but the arithmetic required is modest and examination of the responses suggests conceptual confusion, not arithmetical error." [@boothsweeney2000bathtub, p. 265]

And in the discussion:

> "The errors are highly systematic and indicate violations of basic principles, not merely calculation errors." [@boothsweeney2000bathtub, p. 278]

### What kind of claim this is

This is the only place in this book where a chapter's claim that its material is difficult rests on a measurement rather than on the author's assertion, and it is worth being exact about what the measurement supports.

**The subjects were graduate students at one business school**, described in the paper as typical of that school's student body [@boothsweeney2000bathtub, p. 264].
Nothing about the general population follows.

**It was a convenience sample**, and demographic reporting was voluntary.

**It was published in 2000.**

**And the book uses the study's measurements and none of its threshold verdicts.**
The paper reports several demographic comparisons using the language of statistical significance, including one it calls "only marginally significant".
Chapter 8 spent six pages on why a threshold verdict throws away almost everything a number contains, and that discipline does not stop applying when the source is one the book likes.
The figures used above — 0.77, 0.48, 0.41, 0.66, 0.63 — are measurements.
The verdicts are not used, and the marginal comparison is not used at all.

What the study supports is narrow and sufficient: **on tasks of this kind, capable and numerate people get systematically wrong answers, and the wrong answers have the shape §3 predicted.**

### What this changes about reading a report

The accumulation point has an immediate practical consequence, and it is worth extracting before §4.

**A falling rate and a falling level are different news, and organisations report them interchangeably.**

*Demand is coming down.* True on day 4, and the reservoir was still emptying.

*The deficit has nearly closed.* True on day 7, and the reservoir was at its lowest point of the year.

*We are through the worst of it.* Ambiguous, and the ambiguity is doing the work — through the worst of the **weather**, certainly; nowhere near through the worst of the **storage**.

**None of those sentences is a lie.** Each describes a real quantity moving in a real direction, and each would survive a fact-check.
What they do not say is which quantity, and the difference between the flow and the stock is four days and 62 megalitres.

**A useful habit follows.** Whenever somebody reports an improvement, ask whether the thing improving is the level or the rate.
If it is the rate, ask where the level is.
The answer is frequently that nobody has looked.

### And doing nothing does not recover

One more line of the trajectory, which is the part people find hardest to believe.

From day 8 the heatwave is over.
Demand returns to **100 ML/day**, production is at **100 ML/day**, and the two are equal.

**Storage stays at 88 ML.**

Not on day 8, and not on day 30.
The flows have re-balanced and the stock has not refilled, because balanced flows hold a stock where it is — they do not restore it.

The utility is 32 ML below its own critical level, indefinitely, with production exactly matching demand and nothing visibly wrong.

> "Stocks and flows (accumulations) and long time delays often mean doing and undoing have fundamentally different time constants" [@sterman2006evidence, p. 507]

Drawing the reservoir down took seven days of ordinary summer weather.
Filling it back up requires a surplus that nobody has ordered, for as long as it takes.

### And a note on what the reader was and was not told

The §1 task gave you demand and production and asked for storage.

**It did not tell you there was a critical level.** So the third question — when should the utility have worried — had no defensible answer available, and if you found that question unfair, you were right.

**That was deliberate, and it is the second lesson of this section.** A trajectory alone does not tell you when to act.
It tells you what happened.
To know when to worry you need a threshold, and the threshold is a decision somebody made — Chapter 10's material, arriving in a dynamic setting.

**The utility's 120 ML critical level is not a physical fact about the reservoir.** It is the level below which the utility judged it could no longer guarantee its service standard, and a different utility, or the same one after a bad summer, would set it somewhere else.

So the honest answer to the third question is: *on day 5, given a critical level of 120 — and I cannot answer this without being told the level.*

### Task: work the recovery

At a surplus of **4 ML/day**, how many days does it take to get from 88 ML back to the 220 ML target?

Write the number down.
It is arithmetic, and the size of it is the point.

## 4. Two Delays, and Their Sum

The utility is not passive.
It has an operating instruction for exactly this situation, and it has had it for nine years.

Before the instruction, though, two facts about what the utility can see and do.

### The verification delay

Reservoir storage is telemetered continuously.
It is also read manually, and the utility does not act on the telemetered figure until it has been reconciled against the manual reading — a procedure adopted after Chapter 1's discovery that the reading could be wrong.

Reconciliation takes two days.

**The most recent storage figure any operator can act on is two days old.**

This is an **information delay**: the system changes before the decision-maker observes it.

### The production delay

A change to production ordered today does not arrive today.
The treatment works ramps, then the water travels.

Two days.

This is an **action delay**, or a physical delay: the decision is taken before the system feels it.

### They add

Chapter 1 asked you to look for both kinds and did not say what to do with them.

Here is what to do with them: **add them.**

Two days of not knowing, plus two days of not yet arriving, is **four days of loop delay** — four days between the reservoir being in a state and the utility's response to that state reaching the reservoir.

The heatwave lasted seven.

### The rule

> When the most recent verified storage figure is below 150 ML, set production to the most recent verified demand plus 20 ML/day. When the most recent verified storage figure is above 210 ML, return production to the standing level of 100 ML/day.

Read it before reading on.

It is a sensible rule.
It has a trigger, a response proportional to the situation, and a stand-down condition.
It is more specific than most operating instructions you will meet, and it is exactly the kind of thing Chapter 12 said an adaptive plan needs.

### What the rule does

| Day | Demand | Storage seen | Order | Production | Net | Storage |
|---|---:|---:|---:|---:|---:|---:|
| 3 | 128 | 202 | none | 100 | −28 | 150 |
| 4 | 126 | 178 | none | 100 | −26 | 124 |
| 5 | 120 | 150 | none | 100 | −20 | 104 |
| 6 | 112 | **124** | **146** | 100 | −12 | 92 |
| 7 | 104 | 104 | 140 | 100 | −4 | **88** |
| 8 | 100 | 92 | 132 | **146** | +46 | 134 |
| 9 | 100 | 88 | 124 | 140 | +40 | 174 |
| 10 | 100 | 134 | 120 | 132 | +32 | 206 |
| 11 | 100 | 174 | none | 124 | +24 | 230 |
| 12 | 100 | 206 | none | 120 | +20 | 250 |
| 13 | 100 | 230 | 100 | 120 | +20 | **260** |
| 14 | 100 | 260 | 100 | 120 | +20 | **260** |

Storage reaches capacity on day 13.
**Ten megalitres go over the weir on day 13 and twenty on day 14** — thirty megalitres of treated water, abstracted, pumped, and treated, then spilled.

And the minimum storage is **88 ML on day 7**, which is exactly what it was when the utility did nothing at all.

### Pause: when should the order have been placed?

The first extra water arrives on day 8.
The trough is day 7.

Work out when the order would have had to be placed for the water to arrive by day 6, and then work out whether the rule could have placed it then.

Two minutes.

### The answer, and it is worse than late

To have water arriving on day 6, the order must be placed on day 4.

On day 4 the utility is looking at the day-2 storage figure, which is **178 ML** — well above the 150 trigger.

On day 5 it sees day 3: **150 ML**.
Not below 150.

On day 6 it sees day 4: **124 ML**.
The rule fires.

**So the rule is not merely slow.
It cannot fire in time, and no adjustment of the trigger fixes it cheaply.**

Set the trigger at 180 rather than 150 and it does help: the rule fires on day 4, the water arrives on day 6, and the lowest storage rises from **88 ML to 104 ML**.

**Which is still below the critical level of 120.**

And the spill rises from **30 ML to 70 ML**, because a rule that fires two days earlier keeps ordering for two days longer.
It will also fire in ordinary summers, when storage dips to 175 in a dry August and nothing is wrong.

**Retuning buys something, it does not buy enough, and it is not free.**
The problem is not the number.
The problem is that **storage is the wrong variable to watch**, because by the time a stock has fallen far enough to alarm you, the flows that drew it down have been running for days.

### The general form of the failure

It is worth lifting this off the reservoir, because the arithmetic generalises and the situation is common.

**Three quantities.** How long the loop takes — observation plus action.
How long the disturbance lasts.
And how long the stock can absorb the disturbance before something breaks.

**On this case: four days, seven days, and four days.** Storage started at 220 and the critical level is 120, so at the early deficit rate the buffer was gone in about four days.

**When the loop delay is comparable to the buffer, a stock-keyed rule cannot protect the buffer.** The trigger has to wait for the stock to move, the stock only moves as fast as the flows push it, and by the time it has moved far enough to be alarming, the response is a full loop delay away.

**And when the loop delay is comparable to the disturbance, the response arrives during the recovery.** That is where the overshoot comes from — not from the size of the response but from its timing.

**Both conditions hold here**, which is why the rule both fails to protect and overshoots.
Those look like two failures and they are one.

### The overshoot

**202 megalitres of extra production. Thirty of them spilled.**

And the mechanism is not carelessness:

> "As a result, decision makers often continue to intervene to correct apparent discrepancies between the desired and actual state of the system even after sufficient corrective actions have been taken to restore equilibrium. The result is overshoot and oscillation: stop-and-go traffic, drunkenness, and high-tech boom and bust cycles." [@sterman2006evidence, p. 508]

Read the middle of that sentence again.
**Even after sufficient corrective actions have been taken.**

On day 9 the utility orders more water.
Enough water has already been ordered.
The utility cannot know this, because what it can see is the day-7 figure of 88 ML, and 88 ML is genuinely alarming.
It is ordering against a reservoir that no longer exists.

**Overshoot is what a correct rule does when it is applied through a delay**, and a chapter that let you read it as impatience would have taught you the wrong thing.

### Worse before better

There is a second consequence of delay, and it is nastier because it corrupts evidence rather than outcomes.

> "Characterized by trade-offs. Time delays in feedback channels mean the long-run response of a system to an intervention is often different from its short-run response. Low-leverage policies often generate transitory improvement before the problem grows worse, whereas high-leverage policies often cause worse-before-better behavior." [@sterman2006evidence, p. 507]

On day 8 the utility's storage is 134 and rising.
On day 7 it was 88.
Whoever ordered the increase looks right.

But the increase that arrives on day 8 was ordered on day 6, and the one that arrives on day 12 was ordered on day 10, and by then the situation had reversed.
**The evidence available at the moment of each decision pointed the wrong way**, and it pointed the wrong way because of the delay rather than because anyone misread it.

A policy that gets worse before it gets better is indistinguishable, at the moment you must judge it, from a policy that is simply failing.

### Task: shorten one delay

Suppose the verification delay were one day instead of two, and everything else unchanged.

Work out which day the rule fires, which day the water arrives, and whether the trough moves.

## 5. Closing the Loop

The word for what §4 described is **feedback**, and it has a technical meaning that Chapter 1 deliberately withheld.

> "A dynamical system is a system whose behavior changes over time, often in response to external stimulation or forcing. The term feedback refers to a situation in which two (or more) dynamical systems are connected together such that each system influences the other and their dynamics are thus strongly coupled." [@astrom2008feedback, p. 1]

Two systems, each influencing the other.
The reservoir influences the utility's decisions; the utility's decisions influence the reservoir.

### The sentence this chapter exists for

Immediately after that definition, the same page says this:

> "Simple causal reasoning about a feedback system is difficult because the first system influences the second and the second system influences the first, leading to a circular argument. This makes reasoning based on cause and effect tricky, and it is necessary to analyze the system as a whole. A consequence of this is that the behavior of feedback systems is often counterintuitive, and it is therefore necessary to resort to formal methods to understand them." [@astrom2008feedback, p. 1]

**Chapter 7 spent thirty-eight pages on what it takes to establish that A causes B.**

It taught you to define a target quantity, state the assumptions under which evidence could identify it, check exchangeability and positivity, and refuse the causal sentence when the assumptions failed.
It was careful, it was hard-won, and it ended by refusing to say that replacing the pump would fix Hillcrest.

This sentence says something different and more disquieting.
Where feedback is present, the question *does A cause B* is not merely hard to answer.
**It is the wrong shape**, because A causes B and B causes A, and asking which one came first is asking about a circle.

**Chapter 7 is not retracted, and the book will not say it again.**
Its machinery is correct for the questions it addressed, and most questions are of that kind.
But you now know a class of question where the machinery does not straightforwardly apply, and knowing that is worth more than another technique.

### Open and closed

> "A system is said to be a closed loop system if the systems are interconnected in a cycle... If we break the interconnection, we refer to the configuration as an open loop system" [@astrom2008feedback, p. 2]

**Parts I, II, and III of this book were open loop.**

Chapter 4 asked why these records exist and not others — a question about a fixed process.
Chapter 7 asked what would identify an effect — in a world that does not react to being studied.
Chapter 12 chose a portfolio — against futures that do not depend on the choice.

None of that was wrong.
Most of it was necessary.
But naming the configuration is what lets you notice that you have been assuming it.

### Reinforcing and balancing

Loops come in two kinds and the standard names are a problem.

The engineering terms are `positive feedback` and `negative feedback`, and they are what you will meet everywhere.
**This book does not use them**, for a reason that is about this book rather than about engineering: `positive` has been a controlled term here since Chapter 1, paired with `normative`, and a reader meeting *positive feedback* three chapters after *positive claims* has been handed an ambiguity for nothing.

The system dynamics tradition supplies the alternative in the same breath:

> "Like organisms, social systems contain intricate networks of feedback processes, both self-reinforcing (positive) and self-correcting (negative) loops." [@sterman2006evidence, p. 507]

This book writes **reinforcing** and **balancing**.

A **reinforcing** loop amplifies: more of something produces more of it.

> "In a system with positive feedback, the increase in some variable or signal leads to a situation in which that quantity is further increased through its dynamics. This has a destabilizing effect and is usually accompanied by a saturation that limits the growth of the quantity." [@astrom2008feedback, p. 22]

**Note the last clause**, because it is the half people drop.
A reinforcing loop is not a prediction of unbounded growth.
Something always stops it — a physical limit, a resource, a saturation — and the interesting question is usually *what stops this* rather than *how fast does it grow*.

A **balancing** loop corrects: a discrepancy produces action that reduces the discrepancy.

### Balancing does not mean stabilising

This is where §4 comes back.

The utility's operating rule is a balancing loop.
Storage falls, the rule notices, production rises, storage recovers.
Every arrow points the right way.

**And it overshot by thirty megalitres.**

A balancing loop reduces the discrepancy it *sees*, and what it sees is four days old.
Correcting toward a target you observed four days ago is not the same activity as correcting toward the target, and the difference is the whole of this chapter.

**Balancing is a description of the loop's sign, not a promise about its behaviour.**

### What feedback buys and what it costs

One page of the source states both halves, which is unusual and worth quoting whole.

> "feedback can make a system resilient toward external influences... More generally, feedback allows a system to be insensitive both to external disturbances and to variations in its individual elements." [@astrom2008feedback, p. 3]

And immediately afterwards:

> "Feedback has potential disadvantages as well. It can create dynamic instabilities in a system, causing oscillations or even runaway behavior. Another drawback, especially in engineering systems, is that feedback can introduce unwanted sensor noise into the system, requiring careful filtering of signals." [@astrom2008feedback, p. 3]

You have seen this shape six times now.

More data improved one thing and not another in Chapter 4.
More sources improved coverage and not agreement in Chapter 9.
More scrutiny improved criticism and not credibility in Chapter 3.
The pattern has been that a property which buys you one thing costs you another, and the book has each time had to construct the second half itself.

**Here the source supplies both halves on one page**, unprompted, as a matter of course — which is a sign that the field learned this lesson early and at some cost.

### Feedback is reactive, and the alternative is what this book has been doing

> "Feedback is reactive: there must be an error before corrective actions are taken." [@astrom2008feedback, p. 22]

There is another way to act, and it has a name.
Measure the disturbance before it hits the system, and correct for it in advance — **feedforward**.

**That is what this book has been doing for twelve chapters.**
Forecasting demand and building capacity to meet it is feedforward.
So is Chapter 12's programme, and so is every plan made from a model rather than from an error.

The source states its condition in one sentence:

> "Since feedforward attempts to match two signals, it requires good process models; otherwise the corrections may have the wrong size or may be badly timed." [@astrom2008feedback, p. 22]

**Wrong size or badly timed.**
Chapters 5, 7, and 8 were about the first.
This chapter is about the second.

### The flow-keyed rule

If storage is the wrong variable to watch, watch the flow.

*When the most recent verified demand exceeds 115 ML/day, set production to that demand plus 20; otherwise return to standing.*

Demand rises on day 1, so the rule fires on day 3 and water arrives on day 5.

| | Do nothing | Stock-triggered | Flow-triggered |
|---|---:|---:|---:|
| Minimum storage | 88 (day 7) | 88 (day 7) | **124** (day 4) |
| Days below the critical level | permanently | days 5–7 | **none** |
| Extra production | 0 | 202 ML | 216 ML |
| Spilled | 0 | 30 ML | **44 ML** |
| Storage at day 18 | **88 ML** | 260 ML | 260 ML |

**The critical level is never breached.**

**And the spill rises from 30 to 44** — about half as much again, because a rule that fires on the first sign of demand fires harder and earlier than one that waits for evidence in the stock.

**Neither rule dominates.**
The stock rule wastes less and does not protect.
The flow rule protects and wastes more.

There is no version of this problem in which watching the right variable is free, and a chapter that ended with *watch flows, not stocks* would have taught you a slogan.

### Task: find the loops

In the water case as it now stands, name one reinforcing loop and one balancing loop.

For each, say what would stop it.

## 6. Equilibrium Is Not Stability

Two words that ordinary speech treats as near-synonyms, and that this chapter has to prise apart.

### Equilibrium

> "An equilibrium point of a dynamical system represents a stationary condition for the dynamics." [@astrom2008feedback, p. 100]

> "Equilibrium points are one of the most important features of a dynamical system since they define the states corresponding to constant operating conditions. A dynamical system can have zero, one or more equilibrium points." [@astrom2008feedback, p. 100]

**Zero, one, or more.**

That phrase does more work than it looks like doing.
A reader who thinks of equilibrium as a destination — the place a system settles — has quietly assumed there is one.
There may be none, and there may be several, and which one you are near is then a fact about your situation rather than about the system.

### Pause: is 88 an equilibrium?

From day 8, production is 100 and demand is 100.
Storage is 88 ML and stays there.

**Is that an equilibrium?**

**Is it a good one?**

Answer both before reading on.

### Yes, and no

It is an equilibrium in the exact sense of the definition.
The flows are balanced, nothing is changing, the condition is stationary.

**And it is 32 megalitres below the level at which the utility breaches its own service standard.**

This is the point of the section, and it is worth stating flatly: **equilibrium says nothing whatever about whether you want to be there.** It is a description of the arithmetic, not an endorsement.

An organisation that reports *the system has stabilised* has told you that things have stopped changing.
It has not told you that things are all right, and the two statements are routinely confused — often by people who are relieved.

### Stability

> "The stability of a solution determines whether or not solutions nearby the solution remain close, get closer or move further away." [@astrom2008feedback, p. 102]

Notice what the sentence is about.
It is not about the point.
It is about **the solutions near the point** — about what happens if you are not exactly there, which you never are.

And that is the distinction:

> "An important special case is when the solution [is] an equilibrium solution. Instead of saying that the solution is stable, we simply say that the equilibrium point is stable." [@astrom2008feedback, p. 102]

**Equilibrium is a property of a point: nothing changes if you are exactly there.**

**Stability is a property of the neighbourhood: what happens when you are knocked off it.**

A system can sit at an equilibrium it will never return to.

### Three grades

The source gives formal definitions with quantifiers and inequalities.
They are stated here in words, and the paraphrase is deliberate — the symbols do not survive being lifted out of the page cleanly, and this book does not quote what it cannot reproduce faithfully.

**Unstable.** Start near the point, and you do not stay near it.
The inverted pendulum balanced upright is the standing example: it is genuinely an equilibrium, and the smallest disturbance ends it.

**Neutrally stable.** Start near, stay near, and do not converge.

> "If a solution is stable in this sense and the trajectories do not converge, we say that the solution is neutrally stable." [@astrom2008feedback, p. 102]

A frictionless pendulum swinging: knock it and it swings differently forever, but it never runs away and it never settles.

**Asymptotically stable.** Start near, stay near, *and* come back.
Nearby trajectories converge on the point over time.
A real pendulum, with friction, hanging down.

**The middle grade is the one people do not have a word for**, and it is the one that catches them. *Stable* in ordinary speech means asymptotically stable — it will come back.
The weaker property, staying nearby without returning, is genuinely different and genuinely common.

The named cases, in one sentence, so you recognise them elsewhere: an asymptotically stable point is called a **sink** or **attractor**, an unstable one from which everything departs a **source**, and one where some trajectories arrive and others leave a **saddle** [@astrom2008feedback, p. 104].

### The pendulum, which the book and the source both use

`decisions/0007` fixed the pendulum as this book's standing example of a system that is dynamic without containing anybody who wants anything.

It turns out to be the source's worked example too, at p. 100, chosen for the same reason: it has an equilibrium pointing up and an equilibrium hanging down, and the difference between them is entirely a difference of stability.

The convergence is a coincidence and is worth one sentence, because it is a small piece of evidence that the example is well chosen rather than merely convenient.

### Why the middle grade matters operationally

Neutral stability sounds like an edge case for mathematicians.
It is not, and it has a specific organisational signature.

**A neutrally stable system absorbs a shock and keeps the change.** Knock it and it does not run away, so nothing alarms; it also does not return, so the shock is permanent.

**The utility's reservoir is close to this.** Draw it down by 132 megalitres and the flows will happily balance at the new level.
Nothing breaks, nothing oscillates, no alarm sounds — the system simply operates from then on with a third less water in it than it had.

**This is why *nothing went wrong* is such poor evidence.** In an asymptotically stable system it means the system recovered.
In a neutrally stable one it means the system kept the damage and stopped reacting.

**The diagnostic question is the same one either way**: not *did anything break* but *did it come back*.
Those come apart precisely when it matters.

### The collision: robustness and stability

Chapter 12 made **robustness** a controlled term in this book.
This chapter has made **stability** one.

In ordinary speech they are near-synonyms, and both mean roughly *it holds up*.
They are different concepts and the book uses them differently, so here is the distinction, stated once.

**Robustness is a property of a choice, across a set of futures somebody wrote down.** Chapter 12's portfolio was robust because its worst regret across three named futures was smaller than the alternatives'.
Change the set of futures and the answer changes.

**Stability is a property of a system, near an operating point.** It says what happens to nearby trajectories, and it does not require anybody to have written anything down.

**A robust choice can sit inside an unstable system**, and Chapter 12's programme does.

**And a stable system can be a bad thing to be stable at.** The utility's do-nothing equilibrium at 88 ML is asymptotically stable — knock the flows and they return — and it is below the critical level.

This is the fifth time this book has had to announce a collision, after `validation`, `consistency`, `significance`, and `sensitivity analysis`.
Each time the cause is the same: a word that ordinary usage treats as one thing turns out to name two, and the disciplines that named them were not talking to each other.

### Oscillation

The last behaviour in the core competence, and it has a mechanism.

> "The reason why on-off control often gives rise to oscillations is that the system overreacts since a small change in the error makes the actuated variable change over the full range." [@astrom2008feedback, p. 24]

**Overreaction is not an emotional description.** It means the response is large relative to the discrepancy that triggered it — a thermostat that goes from full heat to nothing when the temperature crosses a line, or a rule that adds 46 ML/day of production because the reservoir is 26 ML low.

Combine that with a four-day delay and you have the utility's trajectory: hard correction, delayed arrival, overshoot, hard correction the other way.

A system that settles into a sustained periodic swing with nothing driving it from outside is said to have a **limit cycle** [@astrom2008feedback, p. 101].
The term is named here and not developed; establishing that a particular system has one requires machinery this book does not teach.

**What you should take is narrower and more useful.** When you see something oscillating, ask two questions: how big is the response relative to the discrepancy, and how long is the loop delay.
Those two account for most of it.

## 7. Policy Resistance

The last idea in the chapter is the one that names what it feels like from inside.

> "policy resistance, the tendency for interventions to be defeated by the response of the system to the intervention itself." [@sterman2002models, p. 504]

**Read the definition carefully, because it does not say what people hear.**

It does not say the system is perverse.
It does not say the intervention was bad, or that somebody failed to think.

It says the response defeats the intervention — and a system that responds is doing what a system does.

### There are no side effects

> "But there are no side effects—just effects. Those we expected or that prove beneficial we call the main effects and claim credit." [@sterman2006evidence, p. 505]

Chapter 2 quoted a different sentence, from a different paper by the same author, to make a point about boundaries: a side effect is an effect that fell outside the line somebody drew.

Here the point is about responsibility.
The category *side effect* exists to sort effects by whether we anticipated them, and then to treat the unanticipated ones as though they belonged to somebody else.

### Two examples, from the source

> "Forest fire suppression causes greater tree density and fuel accumulation, leading to larger, hotter, and more dangerous fires, often consuming trees that previously survived smaller fires unharmed." [@sterman2006evidence, p. 506]

**This one is §3 arriving in a different domain.** Suppressing fires does not remove fuel; it accumulates it.
The stock rises while the flow that would have drained it is held at zero, and the accumulated stock is what eventually burns.

> "Flood control efforts, such as levee and dam construction, have led to more severe floods by preventing the natural dissipation of excess water in flood plains. The cost of flood damage has increased as flood plains were populated in the belief they were safe." [@sterman2006evidence, p. 506]

**And this one is §5.** The intervention changed what people did — they built where they had not built — and the change in behaviour is where the damage went.

Both are the source's examples and not the book's, and neither is offered as evidence about fire policy or flood policy.
They are offered because the mechanisms are legible.

### The book's own instance

Chapter 7 established that the Hillcrest feeder main is sixty-eight years old.
Chapter 12 established that pressure management changes leakage.

Put those together with an intervention nobody in this book has yet proposed: **raise the pressure at the Hillcrest inlet** so that households at the top of the zone get adequate service.

It works, and here is what it costs.

| Step | Delivered to Hillcrest | Extra leakage | Total extra draw | Share delivered |
|---|---:|---:|---:|---:|
| First pressure increase | **3.0** | **4.0** | **7.0** | **43%** |
| Second increase | **2.0** | **6.0** | **8.0** | **25%** |
| Both | **5.0** | **10.0** | **15.0** | **33%** |

All figures in ML/day.

**Two thirds of the water drawn to fix Hillcrest never reaches Hillcrest.**

And the loop closes: the leaked water lowers pressure downstream, which is the observation that prompts the next increase, which leaks more.

**The second increase delivers less than the first and leaks more.** A third would deliver less again.
There is a pressure at which an increment delivers nothing at all — every additional litre pushed in leaves through the main's defects — and the utility would reach it by following a rule that had been working.

This is `sterman2002models` p. 504's definition exactly.
The intervention is defeated by the system's response to the intervention itself, and the response is not anybody's decision.
It is what a sixty-eight-year-old pipe does when you raise the pressure in it.

### The cause

> "Policy resistance arises because we do not understand the full range of feedbacks surrounding—and created by—our decisions." [@sterman2006evidence, p. 507]

**Surrounding and created by.**
Some of the loops were there already.
Some of them did not exist until the intervention created them — the flood plains were not populated until the levees made them look safe.

### And the sentence that keeps this honest

There is a bad way to finish a chapter like this one, and it is to leave the reader with a general excuse.

If structure drives behaviour, then nobody is responsible for anything, and every failure was systemic.

The source addresses this directly:

> "Recognizing the power of system structure to shape behavior does not relieve us of personal responsibility for our actions. To the contrary, it enables us to focus our efforts where they have highest leverage—the design of systems in which ordinary people can achieve extraordinary results." [@sterman2006evidence, p. 510]

**The utility's operating rule is a designed object.** Somebody wrote it, somebody approved it, and somebody can change it.
The finding of §4 is not that the utility was unlucky; it is that a rule keyed to a stock cannot fire in time when the loop delay is four days, which is a fact somebody could have worked out in an afternoon and nobody did.

That is a criticism of the rule, made possible by the analysis, and it is the opposite of an excuse.

### Simulation, and its pitfall

Everything in this chapter was produced by running a table forward.
No differential equations, no software, no model beyond a stock, two flows, and a rule.

Chapter 6 used simulation to sample a distribution.
This chapter used it to trace a trajectory.
It is the same machinery answering a different question, and the second use is the one that makes dynamic behaviour visible, because dynamic behaviour is a shape over time and no summary statistic has a shape.

But there is a warning attached, and it is sharper than the usual one:

> "The most insightful model accomplishes nothing if the interface is obscure and the protocol for its use ineffective. The converse is worse: a poor model embedded in a potent interface may teach harmful lessons more effectively than ever before." [@sterman2006evidence, p. 512]

**A convincing simulation of a wrong system teaches its wrongness efficiently.** Everything Chapter 5 said about model criticism applies with more force here, because a trajectory looks like evidence in a way a static estimate does not.

### Task: diagnose five defects

Each statement below contains one defect — except that one of them is dynamically correct and wrong for a different reason.
Write the defect, what it stops you concluding, and a repair.

1. *"Demand peaked on day 3, so storage bottomed out on day 3."*
2. *"Production and demand are both back to 100 ML/day, so the reservoir has recovered."*
3. *"The trigger is set at 150 ML. If we'd set it at 180 the rule would have worked."*
4. *"The system has stabilised."*
5. *"Every megalitre of extra production was wasted — the trough was the same either way."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

## 8. Cold-Start Practice and Retrieval

### Return to your eight-minute answer

Find what you wrote in §1 and compare it with §3's table.

**Do not score it.**

Three patterns are worth looking for.

**Did you turn storage upward on day 4?** That is the error the source names, and about a third of a numerate graduate cohort made a version of it.

**Did you find day 7?** Then check the second question — did you also say the utility should have worried on day 5, when the critical level was crossed, or on day 3, when demand peaked and everything still looked survivable?

**Did you compute the trajectory but not answer the third question?** The arithmetic is the easy part.
Saying *when* somebody should have acted requires knowing about delays, which §1 had not told you about.

### Independent transfer

Now work an unfamiliar situation, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below.
Open only that one.

- [Form A — A hospital's platelet inventory](transfer-form-a.md)
- [Form B — A district heating network's fuel store](transfer-form-b.md)

Allow about **45 minutes**.
Every fact you need is supplied.
Do not look anything up.

Do not open the other form.
You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the procedure from memory

Close the chapter.
From memory, write the eight steps.

1. Name the **stock** — the quantity that is the running total of something.
2. Name **both flows** — what adds to it, what takes from it. If you can only name one, you have not finished.
3. Get the flows over time and **run the stock forward**. The stock turns where the net flow crosses zero, not where it peaks.
4. Name the **information delay** — how old is the most recent figure you can act on?
5. Name the **action delay** — how long between ordering something and the system feeling it?
6. **Add them.** Compare the sum with how long the disturbance lasts.
7. Ask what the response **returns to** — does acting change what you will next observe, and how long until it does?
8. Ask what the system does **at rest**: is there an equilibrium, is it one you want, and would it come back if knocked?

Check against §§2–6. Steps 3 and 6 are the ones people drop.

### If the transfer went badly

If you produced a trajectory shaped like the demand curve, reread §3 and redo the §1 task with different numbers before moving on.
That specific error is the chapter's subject and it does not repair itself by being read about.

If you found the trajectory but missed why the trigger fired late, reread §4's arithmetic — the four days, and what they are four days of.

### Delayed retest

After at least a week, work the other form.

Do not reread this chapter first.
The delay is the test.

### What this chapter did not give you

**Any way to design a rule.** You can now say why a rule fired too late.
Choosing what to do about it — what to watch, how hard to respond, when to stop — is control, and it is Chapter 14's.

**Any mathematics of stability.** You have three grades stated in words and no way to establish which one a given system has.

**Any treatment of systems that contain people who are reasoning about you.** The reservoir does not have interests.
Chapter 15 does.

**Any account of how often this happens.** The mechanisms in this chapter are sourced.
Their frequency in practice is not, and the book has not claimed it.

**And the textbook that systematises this material was not obtained.** Chapter 13 teaches stocks, flows, and delays from a journal article and a test instrument, which is recorded in `../../decisions/0020` as this chapter's largest gap.

### What Part IV asks next

The utility in this chapter made the same decision over and over, using a rule written nine years ago, and the rule could not have worked.

Chapter 14 asks the question this leaves open.
The decision is not made once.
Information arrives between the decisions, and some of what you do changes what information will arrive.
What is the *policy* — not the choice, but the rule for choosing — and how would you know a good one?
