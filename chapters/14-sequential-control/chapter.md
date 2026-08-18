---
chapter: 14
part: 4
title: "Sequential Decisions, Information, and Control"
status: drafted
---

# Chapter 14: Sequential Decisions, Information, and Control

## 1. The Thing You Are Choosing Is a Rule

Chapter 13 ended on a question it could not answer.

The utility had a written operating rule.
It fired on day 6, delivered on day 8, did not move the trough by a single megalitre, and spilled thirty of treated water.
And the rule was not stupid — it had a numeric trigger, a proportional response, and a stand-down condition, which is more than most operating instructions have.

**So what rule should it have had?**

### Before reading further

Here is the rule, in the utility's own words.

> When the most recent verified storage figure is below 150 ML, set production to the most recent verified demand plus 20 ML/day. When the most recent verified storage figure is above 210 ML, return production to the standing level of 100 ML/day.

You know from Chapter 13 that storage readings are two days old and production changes take two days to arrive.

**Allow about ten minutes and write two things down.**

**Write a better rule.** State it precisely enough that somebody who was not in this conversation could apply it on a Tuesday morning without asking you anything.

**Then say how you would know it was better.**

Do this before reading on.
The second half is the harder half and most readers skip it.

### What has changed

Thirteen chapters have asked you to produce an analysis, an estimate, or a choice.

Chapter 1 asked for a first pass.
Chapter 8 asked for a number and an interval.
Chapter 11 asked for a recommendation.
Chapter 12 asked for a portfolio and a plan.

**This chapter asks for a rule**, and a rule is a different kind of object.

A choice is made once and can be defended by the circumstances of the day.
A rule will be applied by somebody else, on a day you cannot foresee, to a situation you did not imagine — which is why it has to be written in a way that survives your absence.

**Chapter 12 already set the standard without naming it.** Its signposts needed an observable quantity, a threshold with a number, an owner, and a frequency.
That is what a rule needs, and for the same reason: so that it fires without anyone having to reopen the argument.

Look at what you wrote.
If it says *increase production when storage is getting low*, it is not yet a rule.
It has no number, so two people applying it in good faith will do different things.

### Why a rule is harder to write than a decision

There is a specific difficulty here that is worth naming before you compare what you wrote with §2.

**A decision can be defended by its circumstances.** *We increased production because storage was at 92 and the forecast was bad* is an account that a reasonable person can assess, and if the circumstances were unusual, the decision can be unusual too.

**A rule has to be defended in advance, for circumstances nobody has seen.** It will fire in a summer you did not imagine, applied by an operator who has not read your reasoning, and the only thing standing between the rule and a bad outcome is what you wrote.

**Which means a rule has to be worse than you would be**, in the cases you would have handled well by hand — and the compensation is that it is better than the person who will actually be on duty, at three in the morning, in their ninth consecutive shift.

**That trade is the reason organisations have rules at all**, and it is the reason a rule that cannot be applied without asking its author is not doing its job.

### And the second half

*How would you know it was better?*

This is where most answers stop, and it is where this chapter mostly lives.

You cannot answer it from the summer Chapter 13 described, because that summer is one summer, and a rule is not a thing that happens once. **A rule is a thing that happens every year, and the years are not alike.**

### What you will be able to do

State a decision rule precisely enough for somebody else to apply, and recognise when a rule has not been stated.

Compare rules across several histories rather than one, and notice that some histories cannot tell two rules apart.

Say which states your instruments cannot distinguish — and understand that this is not the same as saying nobody has measured something.

Say which of your model's parameters cannot be told apart from each other, and know that this is answerable **before you collect any data at all**.

Tell a problem more data would fix from one it would not.

And say what it costs to find out whether a different rule would have been better, which is not nothing.

## 2. Policies, and Why One Summer Cannot Rank Them

The word for what you wrote in §1 is **policy**.

> "Formally, a policy is a mapping from states to probabilities of selecting each possible action." [@sutton2018reinforcement, p. 58]

Strip the formality and it says something simple.

**A plan says what to do on Monday, Tuesday, and Wednesday.
A policy says what to do given what you see.**

That is why one policy produces different actions in different years.
The utility's rule did nothing at all in a mild summer and ordered 202 megalitres of extra production in a hot one, and it was the same rule both times.

### Four rules

Here are four, including the utility's own.
Each is stated so that somebody who was not in the room could apply it.

**P0 — do nothing.** Hold production at the standing 100 ML/day.

**P1 — stock-keyed.** *The utility's actual rule.* When verified storage is below 150, set production to verified demand plus 20. When it is above 210, return to standing.

**P2 — flow-keyed.** *Chapter 13's repair.* When verified demand exceeds 115, set production to that demand plus 20; otherwise standing.

**P4 — both.** Act only when verified demand exceeds 115 **and** verified storage is below 200; otherwise standing.

### Five summers

One summer cannot rank four rules, so here are five: the heatwave from Chapter 13, a mild year, a long moderate spell, a year with two separate peaks, and a false alarm that looked like the start of a heatwave and was not.

Each cell reads **minimum storage / days below the critical level of 120 / spill / extra production**, in megalitres.

| Summer | P0 | P1 | P2 | P4 |
|---|---|---|---|---|
| Heatwave | 88 / 14 / 0 / 0 | 88 / 3 / 30 / 202 | **124** / 0 / 44 / 216 | 104 / 1 / **6** / 178 |
| **Mild** | 190 / 0 / 0 / 0 | 190 / 0 / 0 / 0 | 190 / 0 / 0 / 0 | 190 / 0 / 0 / 0 |
| Long moderate | 66 / 13 / 0 / 0 | 106 / 2 / 28 / 222 | 130 / 0 / 0 / 148 | 130 / 0 / 0 / 148 |
| Double peak | 80 / 13 / 0 / 0 | 84 / 3 / 38 / 218 | **148** / 0 / 66 / 246 | 132 / 0 / **28** / 208 |
| False alarm | 192 / 0 / 0 / 0 | 192 / 0 / 0 / 0 | 192 / 0 / **18** / 86 | 192 / 0 / **0** / 0 |

And the totals:

| Rule | Worst minimum | Days below critical | Total spill | Total extra production |
|---|---:|---:|---:|---:|
| P0 do nothing | 66 | 40 | 0 | 0 |
| P1 stock-keyed | 84 | 8 | 96 | 642 |
| **P2 flow-keyed** | **124** | **0** | 128 | 696 |
| **P4 both** | 104 | 1 | **34** | 534 |

### Pause: which would you keep?

Look at the totals and pick one.

Then write down what your choice says about what you are willing to pay, and in what currency.

Two minutes, before reading on.

### One thing the table cannot do

Before the findings, note what the five rows are and are not.

**They are five histories, not five samples from a distribution.** Nothing here says how likely a heatwave is, and Chapter 12 established why: on this network there is no defensible probability over summers, and inventing one converts a stated ignorance into a number people will quote.

**So the totals row is a sum, not an expectation.** It weights every summer equally because it has no grounds to weight them otherwise, and that is a choice, stated here rather than buried.

**A reader who wants an expected value will have to supply the weights**, and the moment they do, the ranking becomes a function of their weights rather than of the rules.

### The first finding, and it is blunt

**P1 is dominated by P4.**

Higher worst minimum — 104 against 84.
Fewer days below the critical level — 1 against 8.
Less spill — 34 against 96.
Less extra production — 534 against 642.

**Better on every measure.** Not a trade-off, not a matter of preference, not a question of what the utility values.
Simply worse, on all four counts, for nine years.

### And the utility was not being foolish

This is the strongest thing this book has said about the utility, and it needs immediate qualification.

**P1 was a reasonable rule to write.** It watches the thing that matters — storage.
It acts in proportion.
It stands down.
Somebody thought about it.

**What nobody did was compare it with anything.**

A rule that has never been compared with an alternative is not a rule anybody chose.
It is a rule somebody wrote, which is a different act, and the utility has been treating the first as if it were the second for nine years.

**The comparison in this section took an afternoon.** The data existed.
The alternative rules are obvious once you write down what the instruments show.
The only thing that was missing was somebody asking *compared to what?* — which is the question this book has been asking since Chapter 1, arriving at last at the utility's own procedures.

### The second finding

**P4 differs from P1 in exactly one respect: what it watches.**

Same two-day verification delay.
Same two-day production delay.
Same response size — verified demand plus twenty.
Same stand-down structure.

P1 watches the stock.
P4 watches the stock **and** the flow.

**One extra condition in one sentence, and every one of the four measures improves.**

### The third finding, which is not a finding

P2 and P4 do not dominate each other.

**P2 never breaches the critical level, and spills 128 megalitres across five summers.**

**P4 breaches it on one day, and spills 34.**

So the question is whether one day below the utility's service standard is worth ninety-four megalitres of treated water, and **nothing in this table answers it**.

That is a question about what the utility values, and Chapter 10 is where questions of that shape go.
The arithmetic has taken the decision as far as arithmetic goes, and the remaining step is a judgment that somebody has to make and defend.

**The chapter will not settle it**, and a chapter that did would be teaching you that these problems have right answers.

### What it would take to change the first finding

Domination is a strong claim, so it is worth saying what would overturn it.

**A summer on which P1 beats P4.** There is no such summer among the five, and there is a structural reason: P4 acts whenever P1 would act *and* the demand signal agrees, so P4 acts earlier in every year where the demand signal moves first — which is every year in this set.

**A measure on which P1 wins.** Four are tabulated.
A fifth — say, the number of separate production changes an operator has to make — might favour P1, which is quieter.
Nobody has counted them, and if operator workload matters, somebody should.

**Or a cost the table does not carry.** P4 requires the demand figure to be available and trusted, and Chapter 4 established that the demand figure is a residual. **P1 needs one instrument to be right; P4 needs two.** That is a real difference and the table does not show it.

**None of these rescues nine years of not asking.** But a reader who takes "dominated" as the end of the discussion has stopped one step early, and this book's whole method is to take that step.

### Why nine years of experience could not have told them

There is a reason the utility's operating record, however long, could not have produced this table.

> "The most important feature distinguishing reinforcement learning from other types of learning is that it uses training information that evaluates the actions taken rather than instructs by giving correct actions." [@sutton2018reinforcement, p. 25]

> "Purely evaluative feedback indicates how good the action taken was, but not whether it was the best or the worst action possible. Purely instructive feedback, on the other hand, indicates the correct action to take, independently of the action actually taken." [@sutton2018reinforcement, p. 25]

**The utility's nine years are evaluative.** They say how P1 did.
They contain nothing whatever about how P2 or P4 would have done, because P2 and P4 were never run.

**And this book has been working with evaluative feedback throughout without the word.** Chapter 6 scored forecasts against outcomes.
Chapter 8 found four defensible analyses that agreed in direction and disagreed in verdict.
In both cases the record said how well something did and not what would have done better.

### What this chapter is not teaching, and why you should know

The source these definitions come from is a textbook on reinforcement learning, and it formalises all of this as "the optimal control of incompletely-known Markov decision processes" [@sutton2018reinforcement, p. 2].

That formalisation has an apparatus — value functions, dynamic programming, the whole machinery for computing an optimal policy rather than comparing four of them — and **this book does not teach any of it.** The architecture excludes it by name.

The source itself supplies the reason to be careful about the omission:

> "In particular, the distinction between problems and solution methods is very important in reinforcement learning; failing to make this distinction is the source of many confusions." [@sutton2018reinforcement, p. 2]

**This chapter teaches the problem.** When you meet the solution methods later, you will find they answer a question you can already state, which is the right order.

### What the totals table is not

Three cautions before §3, because a table of four rules over five summers invites more confidence than it earns.

**The five summers were chosen.** By whom, on what grounds, and with what left out — the same questions Chapter 12 asked of its three futures, and they do not become easier here.
A sixth summer with a two-week heatwave would change the totals and might change the ranking.

**The four measures were chosen too.** Minimum storage, days below the critical level, spill, extra production.
Nothing here counts operator time, contractor availability, the carbon cost of pumping, or what customers think when the reservoir visibly overflows.
Chapter 10 would have questions about all four.

**And the totals add across summers as though summers were interchangeable.** A day below the critical level in a year with two other bad zones is not the same event as one in a quiet year, and the sum does not know the difference.

**None of this makes the comparison worthless.** It makes it a comparison of four rules against four stated measures over five stated years, which is a great deal more than the utility had, and less than the table's tidiness suggests.

### Task: a fifth rule

Write a fifth rule — anything that could be applied on a Tuesday morning.

Predict its row in the totals table before you work it out: worst minimum, days below critical, spill, extra production.

## 3. What the Instruments Determine

Every rule in §2 fires on a signal.

P1 fires when storage is low.
P2 fires when demand is high.
P4 fires when both.

**A question nobody in §2 asked: what if the signal has two causes?**

### What the utility can see

Four instruments, and this is all of them.

**Reservoir level**, verified, two days old.
**Total production**, daily.
**Metered customer consumption**, quarterly.
**Zone 4 inlet pressure**, continuous.

### Two states, one record

Suppose the daily draw jumps by twelve megalitres.

**It could be hot weather.** People water gardens, fill paddling pools, run showers.

**It could be a burst.** A joint on an old main lets go underground and twelve megalitres a day runs into the subsoil.

These are entirely different situations calling for entirely different actions.

**And they produce the same record.** Total draw rises.
The reservoir falls.
Zone 4 inlet pressure drops.
Quarterly meters will not report for weeks, and when they do, a burst and a hot quarter both show consumption below production.

**There is nothing in the four instruments that separates them.**

### Why nobody noticed

The two states have been in this book since Chapter 2, and no chapter has put them side by side.

**Chapter 2** asked what belongs inside a representation of the network, and put demand in and leakage in, as separate things.

**Chapter 4** found the demand figure was production minus metered consumption — which means, in effect, demand-and-leakage together.

**Chapter 13** watched the utility's rule fire on a demand signal.

**At no point did anyone ask whether the utility could tell which of the two it was looking at**, and the reason is that the question sounds like a data-quality complaint.
It is not.
It is a question about whether the instruments determine the state, and the answer would have been the same on the day the instruments were installed.

### The word for this

> "The problem of observability is one that has many important applications, even outside feedback systems. If a system is observable, then there are no 'hidden' dynamics inside it; we can understand everything that is going on through observation (over time) of the inputs and outputs." [@astrom2008feedback, p. 202]

The source's formal definition is stated with a quantifier, an inequality, and an interval, and this book does not quote formulae it cannot reproduce faithfully. **The paraphrase, and it is a paraphrase**: a system is **observable** if the state at any chosen moment can be determined from the record of its inputs and its measured outputs over an interval.

**Note "over an interval."** Observability is not about what one reading tells you.
A state can be unrecoverable from today's instruments and perfectly recoverable from a fortnight of them, which is why this concept had to wait for Chapter 13's delays.

And the sentence that makes it a decision rather than a theorem:

> "As we shall see, the problem of observability is of significant practical interest because it will determine if a set of sensors is sufficient for controlling a system." [@astrom2008feedback, p. 202]

**Whether a set of sensors is sufficient.** That is a purchasing question, and §6 answers it.

### Unobservable is not unmeasured

This is the distinction to hold on to, because the words invite the wrong one.

**Unmeasured** means nobody wrote it down.
The remedy is to write it down.

**Unobservable** means two different states produce identical records. **No amount of care with the existing instruments separates them**, because there is nothing in the record to separate.
Reading the gauges more often will not help.
Reading them more carefully will not help.
Hiring a better analyst will not help.

The remedy for unobservability is a different instrument, or a different question.

### What this does to every rule in §2

All four rules fire on the same signal, and none of them can tell why the signal appeared.

**On a burst, the response makes things worse.**

Raise production and more water enters the network.
More water in the network means more pressure at the fault.
More pressure at the fault means more water into the subsoil. **The rule that was written to protect storage is now feeding the leak**, and it will keep feeding it until somebody notices the reservoir is not recovering.

That is Chapter 13's policy resistance — an intervention defeated by the system's response to the intervention itself — arriving inside a Chapter 14 rule. **And the reason it can happen is that the rule cannot see which state it is in.**

### A shape the book has met twice before

**Observability is not a property of the system.** The reservoir is not observable or unobservable in itself.

**Nor is it a property of the instruments.** A pressure gauge is not observable or unobservable.

**It is a property of the pairing.** These instruments, on this system, do or do not determine the state.

Chapter 3 said the same about `validity` — a property of an interpretation, not of a questionnaire.
Chapter 9 said it about `transportability` — a relation between a study and a target, not a badge a study carries.

**Third time.** The book keeps finding that words which sound like properties of things turn out to be relations between things, and the failure is always the same: somebody asks whether the instrument is good, when the question is whether it is good *for this*.

### One term, with a warning attached

The same page offers a phrase worth knowing and worth distrusting:

> "Sensors combined with a mathematical model can also be viewed as a 'virtual sensor' that gives information about variables that are not measured directly." [@astrom2008feedback, p. 202]

The idea is real and useful.
It is also **a model output being treated as a measurement**, and this book spent Chapters 3 and 4 on why that substitution needs watching — a score is not the construct, and a record exists because of a process.

**Use the term.
Do not let it launder a model into an observation.**

### What would have to be true for the rules to be safe

The honest position is not that the rules are wrong.
It is that they rest on an assumption nobody wrote down.

**The assumption is that a rise in draw is a rise in demand.**

On that assumption every rule in §2 is sensible, and P4's totals are as good as the table says.
Off it, the same rules feed a leak.

**Chapter 5 taught you to write assumptions down and ask what would show them false.** Here the assumption is not about a mechanism or a measurement; it is about **which of two worlds you are in**, and the instruments cannot tell you.

**So the assumption is not merely unstated.
It is unfalsifiable with the equipment on site**, which is a stronger condition and a rarer one.

**That is what makes observability worth a section of its own.** Most unstated assumptions can be checked by somebody who thinks to check them.
This one cannot, by anybody, until the utility buys something.

### Task: another blind pair

Name one other pair of states in the water case — not this one — that the utility's four instruments could not tell apart.

## 4. Two Parameters That Cannot Be Told Apart

The utility has a demand model.
It is simple, it fits, and it has a hole in it that no amount of data will fill.

### The model

> daily draw = base demand + heat sensitivity × maximum temperature + background leakage

Fitted to the heatwave week, the utility gets a **heat sensitivity of 2.0 megalitres per degree**, and **base demand plus leakage of 82 megalitres a day**.

Check the fit:

| Maximum temperature (°C) | 18 | 21 | 23 | 22 | 19 | 15 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Model gives | **118** | **124** | **128** | **126** | **120** | **112** | **104** |

Those are the seven demand figures you have been working with since Chapter 13. The model is exact.

### The 82

**Base demand plus leakage of 82.**

Not base demand of 78 and leakage of 4.
Not base demand of 60 and leakage of 22.
Not base demand of 40 and leakage of 42.

**All three fit exactly**, and so does every other pair adding to 82.

| Base demand | Leakage | Sum | Fit |
|---:|---:|---:|---|
| 78 | 4 | 82 | exact |
| 60 | 22 | 82 | exact |
| 40 | 42 | 82 | exact |

### Pause: what would settle it?

Write down what data the utility would need to collect in order to know which split is right.

Be specific.
How many years, how many meters, what measured.

Three minutes, before reading on.

### The answer, and it is not a quantity

**No amount of the data the utility collects will settle it.**

Not ten years.
Not a hundred years.
Not perfect instruments with no measurement error whatsoever.

The two parameters enter the model only through their sum.
Any increase in one is exactly cancelled by a decrease in the other, and the model's output does not move. **There is nothing to observe, because the two candidate worlds produce identical predictions.**

That is not a shortage of data.
It is a property of the model paired with what gets measured, and it would have been true on the day the model was written.

### The word for this

> "A model is structurally identifiable if a unique parameterization exists for any given model output." [@wieland2021identifiability, p. 61]

And the diagnostic, which is the clause to remember: a parameter is structurally non-identifiable when changing it need not alter the model's trajectory, **"because the changes can be fully compensated by altering other parameters"** [@wieland2021identifiability, p. 61].

**Fully compensated.** If two parameters can trade against each other with no visible consequence, they are not separately determinable, and no experiment of the kind you are running will separate them.

### Why this chapter is different from Chapter 8

Chapter 8 took twenty-four events, computed a mean error of **+1.8 ML**, and produced an interval of **+0.84 to +2.76**.
It needed the records.
Without them there was no number and no interval.

**Chapter 14's finding needed no records at all.**

Write down the model.
Write down what is measured.
Look for parameters that appear only in combination.
That is the whole procedure, and you can do it on the back of an envelope before anyone has collected anything.

**This is the most useful thing in the chapter**, because it inverts the usual order.
The normal instinct on meeting an unanswerable question is to go and get more data.
Sometimes the right move is to check first whether more data could possibly help — and that check is cheap, fast, and almost never done.

### The other kind, which Chapter 8 was doing

The source introduces two terms in one sentence, and the pairing is what makes either comprehensible:

> "Concerning identifiability, one distinguishes between structural identifiability dealing with inherently indeterminable parameters because of the model structure itself, and practical identifiability, dealing with insufficiently informative measurements to determine the parameters with adequate precision." [@wieland2021identifiability, p. 61]

**The difference is what more data can fix.**

**Structural** — the model's form makes the parameter indeterminable.
More data does nothing.

**Practical** — the measurements are not informative enough.
More data, or better data, helps.

And the definition of the second:

> "we consider a combination of model and data as practically identifiable if the confidence intervals of all estimated parameters are of finite size" [@wieland2021identifiability, p. 63]

**Note the object: a combination of model and data.** Not a model.
The same relation-not-property shape as §3's observability, for the third time in two sections.

**Chapter 8 was doing practical identifiability without the name.** Its interval was of finite size, so the quantity was practically identifiable — and six pages of that chapter were about how nearly it was not.

**One honest note.** The source itself records that this second sense is less settled than the first: practical nonidentifiability "has not been investigated at the same conceptually clear level" [@wieland2021identifiability, p. 60].
A chapter offering you four crisp terms without saying that one of them is contested would be selling you something.

### How to run the check

The diagnostic in §4 is worth stating as a procedure, because it is short and because almost nobody runs it.

**Write down the model.** Not the code — the model, as an equation or a sentence, with every parameter named.

**Write down what is actually measured.** Not what is in principle measurable.
What is recorded, by whom, at what frequency.

**Look for parameters that appear only in combination.** Two things that only ever occur added together, or only ever multiplied, are not separately determinable from that measurement alone.

**Then ask what would break the combination.** Usually it is a measurement taken under conditions where one of the two is near zero — which is exactly what §6's meter does at three in the morning — or a period in which one of them is known to have changed and the other did not.

**Four steps, ten minutes, no data required.**

**And the reason it is almost never run** is that it does not feel like analysis.
It produces no number and no chart.
It produces a sentence saying that a question you were about to spend two years on cannot be answered by the thing you were about to spend two years doing — which is worth a great deal and looks like nothing.

### Four words, one adjective

The book now has four things called identifiability or identification, and they are different questions.

| Term | The question it asks | Where |
|---|---|---|
| **statistical identifiability** | Can the parameter be determined from the distribution the data come from? | Chapter 7 |
| **causal identification** | Can the causal effect be determined from available data plus stated assumptions? | Chapter 7 |
| **structural identifiability** | Can the model's parameters be determined from its input-output behaviour, in principle? | here |
| **practical identifiability** | Can they be determined from the data actually in hand, with adequate precision? | here |

Chapter 7 registered the first three as a three-way distinction and reserved the third for this chapter. **The fourth is new**, and it is here because the source introduces it in the same breath and because without it you cannot tell a fixable problem from an unfixable one.

**This is the sixth time this book has had to announce that one word names several things** — after `validation`, `consistency`, `significance`, `sensitivity analysis`, and `robustness` against `stability`.
It is the first time with four.

### Two things said plainly about the sources here

**This material comes from systems biology.** Every example in the source is a cell-signalling model.
The book applies the structural-versus-practical distinction across domains, and that widening is the book's own.

**And the term was named somewhere the book could not reach.** `structural identifiability` originates with a 1970 paper by Bellman and Åström, which this book confirmed exists — it is in the bibliography of the control textbook used throughout — and **could not obtain**.
So this chapter closes a definition that has been open since Chapter 1 using a review article rather than the paper that named the thing.
That is weaker than this book prefers, and it is recorded rather than passed over.

### And a decision cannot be made

Chapter 12 costed network pressure management at **£380,000**, delivering 190 household-events a year.

**What that scheme is worth depends on how much of the 82 is leakage.** At 4 megalitres a day there is very little for pressure management to work on.
At 22 there is a great deal.
At 42 the utility has a different business.

**The utility's records cannot say**, and a decade of further record-keeping would not change that.

### Task: another sum

Find a second pair of quantities in this book that were only ever observed added together.

There is at least one, and it is in Chapter 4.

## 5. Measure More, or Model Less

The source that supplied §4's distinction also supplies the response, and the response is a decision with two options.

> "one has two principal options to tailor the model complexity to the information content of the data: (1) measure additional data, corresponding to an increase of the dimension of the observation function g in Equation (2) or (2) reduce the model complexity according to the available data, corresponding to a decrease of the dimension of the parameter space" [@wieland2021identifiability, p. 64]

**Measure more, or model less.**

### Nobody proposes the second

Chapter 10 taught that an option set is a claim about what matters, and that the options nobody writes down are where the interesting alternatives hide.

**Here is a technical warrant for that claim.** When a model has parameters the data cannot separate, there are exactly two responses, and organisations reach for one of them almost every time.

**Measuring more is visible, fundable, and flattering.** It produces a project, a budget line, and somebody to run it.

**Modelling less is none of those things.** It produces a shorter model and an admission.
It is usually cheaper and always faster, and it is very rarely proposed.

### And the utility already did it

Chapter 4 found that the utility's demand figure was never measured.
It is production minus metered consumption — a subtraction residual, arithmetically correct, containing about a third of things that were neither Hillcrest nor demand.

**Read that again with §4's vocabulary.**

The utility had a model with base demand and leakage in it.
It could not separate them.
So it dropped the distinction and reported a single figure covering both.

**That is option (2).** Reduce the model complexity to match the information content of the data.
It is a legitimate response, recommended by the source, and it is what the utility did.

### The asymmetry, and where it comes from

It is worth being precise about why one option gets proposed and the other does not, because the reason is institutional rather than intellectual.

**Measuring more creates a thing.** A meter, a survey, a monitoring programme.
It has a budget line, a supplier, a delivery date, and somebody whose job it becomes.
It can be reported as progress in the quarter it is approved, years before it produces anything.

**Modelling less destroys a thing.** It takes a model with six parameters and returns one with five, and the deliverable is a shorter document and a paragraph admitting that a distinction the organisation has been reporting for a decade was never supported.

**Nobody is promoted for the second**, and the first survives scrutiny more comfortably, because *we are gathering better evidence* is unanswerable in a way that *we have stopped claiming to know something* is not.

**But the second is often right**, and it is right precisely when the first is futile — when the non-identifiability is structural, and the additional measurement is of the same kind that already fails to separate the parameters.

**The question that distinguishes them is §4's**, and it takes ten minutes: would the data you propose to collect break the combination, or merely add more of what you already have?

### The difference between doing it and recording it

What the utility did not do was write down that it had done it.

**Option (2) taken deliberately** produces a model with fewer parameters and a note explaining what was collapsed and why.
Anyone reading it later knows that "demand" means demand-plus-leakage-plus-whatever-else, and treats it accordingly.

**Option (2) taken silently** produces a figure called "demand" that people then use as if it meant demand.

Chapter 4 spent a whole chapter on the consequences: a quantity that had been carried through four chapters of analysis, used in a forecast, and cited in a committee paper, none of whose readers knew it was a residual.

**The difference is one sentence in a records manual**, and the difference in what it costs is most of Chapter 4.

### The same choice, in three earlier chapters

Once you have the pair of options, you can see it in places the book did not name it.

**Chapter 5.** The five-times-a-household division revealed a term the analysis had no way to express.
The options were to go and measure the missing quantity, or to stop reporting a figure that silently included it.
The chapter took neither and recorded the gap, which is a third option and an honest one.

**Chapter 9.** Five sources could not be combined without assuming they were about the same quantity.
Measure more would mean commissioning a study in the target setting; model less would mean reporting the range rather than a pooled number.
The chapter recommended the second and did not have this vocabulary for it.

**Chapter 12.** The benefit column compressed three objectives into one, with an exchange rate nobody had stated.
Measure more would mean eliciting the exchange rate; model less would mean reporting three columns and refusing to add them.

**Three chapters, one shape.** In every case an organisation faced a quantity it could not determine, and in every case the visible option was to go and find out.

**Naming the second option is most of what §5 is for**, because an option you cannot name is one you will not propose.

### Task: the missing sentence

Write the sentence the utility should have put in its records manual in 2014, when it started reporting demand as production minus metered consumption.

One sentence.
Under forty words.

## 6. Buying an Instrument

Two problems have now been posed and not solved.

**§3:** hot weather and a burst produce the same record.

**§4:** base demand and leakage cannot be told apart.

**One instrument fixes both.**

### The night-flow meter

A meter at the Zone 4 inlet, reading continuously, with the figure that matters taken at **03:00**.

At three in the morning almost nobody is using water.
No showers, no gardens, no washing machines. **Whatever is flowing into the zone at 03:00 is very largely leakage.**

| | Night flow, ML/day-equivalent |
|---|---:|
| Normal | **4** |
| With a burst of the size that would move the daily figures | **13** |
| Effect of hot weather | **negligible** |

Hot weather does not water a garden at three in the morning. **So the two states of §3 separate cleanly**, and the 82 of §4 splits.

**Installed cost: £18,000.**

### And the utility cannot compute what it is worth

Chapter 11 taught how to value information: put a probability on each state, work out what you would do under each, and compute what knowing would be worth.

**That arithmetic needs a prior**, and there isn't one.

Nobody at the utility will say how likely it is that leakage is 4 rather than 22. Chapter 12 established that this is a real and common condition rather than a failure of nerve — some decisions genuinely arrive with no probabilities attached, and inventing them converts a stated ignorance into a number that will be quoted without its provenance.

**So this chapter computes no value**, and says so rather than manufacturing one.

### What it uses instead

Chapter 11 supplied a second device for exactly this situation: **the perfect-information ceiling**, used as a screening rule.

The meter's information bears on a decision the book has already priced.
Chapter 12 costed network pressure management at **£380,000**.

**The meter costs £18,000. That is 4.7% of the scheme whose value it would inform.**

**What follows from this, and what does not.**

**It follows that the meter cannot be screened out on cost.** Almost any chance of the information changing a £380,000 decision clears a £18,000 bar.

**It does not follow that the meter is worth buying.** A ceiling argument rules things out; it does not rule them in.
Chapter 11 taught precisely this use, and reversing it would undo the chapter's main result — that a perfectly informative test can be worth less than it costs.

**The honest sentence is: this cannot be dismissed on price, and somebody now has to decide.**

### What the ceiling does not cover

One more thing the arithmetic in this section leaves out, because it will bite anybody who runs the same argument in their own organisation.

**£18,000 is the installed cost.
It is not the cost.**

Somebody has to read the meter, or write the thing that reads it.
Somebody has to notice when it drifts, and the utility's load cells drift, which is why the storage figure takes two days to verify in the first place.
Somebody has to decide what a night flow of 9 means when the threshold was set at 8. And a meter that nobody looks at for two years is an £18,000 asset that provides no information at all.

**Every instrument comes with an obligation**, and the obligation outlives the enthusiasm that bought it.

**This is not an argument against the meter.** It is an argument for including the obligation in the price when you compare it against the ceiling — and for asking, before buying, who specifically will be looking at the number, and what they will be authorised to do when it moves.

### Control, defined

One word remains from this chapter's title, and it needs guarding because it is used loosely everywhere.

The source that has carried Chapters 13 and 14 defines it narrowly:

> "In this book, we define control to be the use of algorithms and feedback in engineered systems." [@astrom2008feedback, p. 3]

And gives its structure:

> "A modern controller senses the operation of a system, compares it against the desired behavior, computes corrective actions based on a model of the system's response to external inputs and actuates the system to effect the desired change. This basic feedback loop of sensing, computation and actuation is the central concept in control." [@astrom2008feedback, p. 4]

**Sensing, computation, actuation.**

Look at what this chapter has found about the utility, in those three terms.

**Sensing.** Its instruments cannot distinguish the two states its rule most needs to distinguish, and cannot separate two parameters its capital programme turns on.

**Computation.** Its rule was never compared with an alternative, and is dominated by one that differs in a single clause.

**Actuation.** Its production changes take two days, which Chapter 13 showed is most of why the rule fails.

**All three, and the first is where the trouble starts.**

### A system can be controlled and still do badly

`control` names an activity, not an achievement.

A system with a controller on it is under control in the technical sense whether the controller is any good or not.
The utility has been controlling its reservoir for nine years — sensing, computing, actuating, every day — and doing it badly at all three steps.

**When somebody says a process is under control, they have told you a loop exists.
They have not told you it works.**

### Task: one measurement

Across all fourteen chapters of this book, name the **one** measurement that, if the utility had made it from the beginning, would most have changed the analysis.

Say what it would have changed, and in which chapters.

## 7. Exploration, and Why Most Years Teach Nothing

The utility has run P1 for nine summers.

It has nine years of data on P1 and **zero** on P2, P4, or anything else.

To learn whether P4 is better, somebody has to run P4.

### The words

> "When you select one of these actions, we say that you are exploiting your current knowledge of the values of the actions. If instead you select one of the nongreedy actions, then we say you are exploring, because this enables you to improve your estimate of the nongreedy action's value." [@sutton2018reinforcement, p. 26]

**Exploiting** is doing what you currently believe is best.
**Exploring** is doing something else in order to find out about it.

And the trade:

> "Exploitation is the right thing to do to maximize the expected reward on the one step, but exploration may produce the greater total reward in the long run." [@sutton2018reinforcement, p. 26]

> "Reward is lower in the short run, during exploration, but higher in the long run because after you have discovered the better actions, you can exploit them many times." [@sutton2018reinforcement, p. 26]

Note the word **may**.
It is doing work.

### What nine years of experience actually contains

Before the pause, it is worth being exact about what the utility knows and how it knows it.

**It knows how P1 behaved in nine particular summers.** That is real knowledge and it is not nothing — it includes how the rule interacts with maintenance schedules, how operators actually apply it under pressure, and which of its clauses get quietly ignored.

**It knows nothing about P4**, and it cannot infer anything about P4 from the record, because the record contains no year in which P4 was in force.

**And the two feel the same from inside.** Nine years of successful operation reads as evidence that the rule is good.
It is evidence that the rule is survivable, which is a much weaker claim, and the difference only becomes visible when somebody puts an alternative next to it.

**This is §2's evaluative feedback arriving as an institutional fact rather than a definition.**

### Pause: how many summers?

The utility decides to try P4.

**How many summers would it have to run it before it knew whether P4 was better than P1?**

Write down a number and a reason.
Three minutes.

### The answer is worse than you think

Go back to the table in §2 and look at the **mild** summer.

**All four rules produce identical results.** Minimum 190, no days below critical, no spill, no extra production.
Nothing happens, and nothing is learned.

A full year of operating experience, containing no information whatever about which rule is better.

**And it is not just the mild year.** Between P2 and P4 — the two rules actually in contention — **two of the five summers are identical**.
Mild and long moderate.
Only three of the five discriminate at all.

**So roughly three summers in five carry information about this choice, and the utility gets one summer per year.**

If those five summers are representative, a utility that switched to P4 tomorrow would accumulate about three informative years per five calendar years.
Getting to a confident comparison is a decade-scale project, conducted by an organisation whose staff turn over faster than that.

**That is the real shape of exploration in an institution.** It is not that trying things is expensive.
It is that most trials are uninformative, and the informative ones arrive on the weather's schedule rather than yours.

### And the years are not the utility's to choose

There is a further difficulty that the bandit framing does not capture, and it matters more here than the theory does.

**In a laboratory you choose when to pull a lever.** You can run a thousand trials on a Tuesday.

**The utility gets one summer a year, and does not choose what kind of summer it is.** It cannot decide to have a heatwave in order to test P4. It cannot repeat last August under different conditions.
And it cannot run P1 and P4 side by side, because there is one reservoir.

**So the informative trials arrive at a rate set by the weather**, in an order nobody controls, and each one is a single sample of a summer that will never recur.

**Two consequences worth carrying.**

**Simulation does some of what the trials would do.** The table in §2 was produced by running four rules against five summers on paper, which is exactly what the utility could not do in the world — and Chapter 13's warning applies in full: a convincing simulation of a wrong system teaches its wrongness efficiently.

**And the alternative to exploring is not learning nothing.
It is learning nothing while believing otherwise**, which is where the utility has been for nine years.
It has a great deal of experience, all of it about one rule, and the experience feels like evidence about the choice.

### The dilemma is not solved

It would be comfortable to end this section with a rule for how much to explore.

There isn't one:

> "The exploration–exploitation dilemma has been intensively studied by mathematicians for many decades, yet remains unresolved." [@sutton2018reinforcement, p. 3]

That is the source's own sentence, in a textbook devoted to the subject.

And on the methods that do exist:

> "However, most of these methods make strong assumptions about stationarity and prior knowledge that are either violated or impossible to verify in most applications and in the full reinforcement learning problem that we consider in subsequent chapters. The guarantees of optimality or bounded loss for these methods are of little comfort when the assumptions of their theory do not apply." [@sutton2018reinforcement, p. 27]

**Read that with Chapters 5, 7, and 8 in mind.** A textbook disqualifying its own guarantees, on the grounds that their assumptions are violated or unverifiable, is doing exactly what this book has spent forty pages teaching you to do to other people's results.

### Where this chapter stops

The setting in which the trade has been studied hardest is called the **k-armed bandit** — named, the source explains, by analogy to a slot machine, "except that it has k levers instead of one" [@sutton2018reinforcement, p. 26].

There is a large literature of methods for it. **This chapter teaches none of them**, and the architecture excludes them by name.

The source states its own depth choice in a sentence this book is happy to borrow:

> "In this book we do not worry about balancing exploration and exploitation in a sophisticated way; we worry only about balancing them at all." [@sutton2018reinforcement, p. 27]

**This chapter goes one step further back.** It does not balance them at all.
It establishes that the trade exists, that the utility has never made it, and that most of the years in which it might have been made would not have taught anybody anything.

### Task: diagnose five defects

Each statement below contains one defect — except that one of them is true of this case and false as a general claim, which is a different kind of problem.

Write the defect, what it stops you concluding, and a repair.

1. *"P1 has worked for nine years, so it is a reasonable rule."*
2. *"We can't tell leakage from base demand, so we need more data."*
3. *"P4 is better than P1 on every measure, so the utility should switch to P4."*
4. *"We should run P4 next summer and see how it does."*
5. *"The reservoir is under control — we have a documented operating rule and daily monitoring."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

## 8. Cold-Start Practice and Retrieval

### Return to your ten-minute rule

Find what you wrote in §1.

**Do not score it.** Check three things.

**Does it have a number?** A trigger without a threshold is not a rule, because two people applying it in good faith will do different things.

**Does it say when to stop?** Most first attempts say when to start and not when to stand down, which is how a temporary measure becomes permanent.

**Did you answer the second question at all?** *How would you know it was better* is where the chapter lives, and if you wrote a rule and moved on, that is the finding.

If your answer to the second question was *we would see how it goes*, reread §2 on evaluative feedback.
Seeing how it goes tells you how your rule did.
It says nothing about the rule you did not run.

### Independent transfer

Now work an unfamiliar situation, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below.
Open only that one.

- [Form A — A regional grid operator's reserve procurement](transfer-form-a.md)
- [Form B — A livestock veterinary service's antibiotic stewardship](transfer-form-b.md)

Allow about **50 minutes**.
Every fact you need is supplied.
Do not look anything up.

Do not open the other form.
You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the procedure from memory

Close the chapter.
From memory, write the seven steps.

1. State the decision as a **rule**: a trigger with a number, a response, and a stand-down.
2. Write down **at least one alternative rule**. A rule that has never been compared is not a rule anybody chose.
3. Compare them across **several histories**, not one.
4. Check which histories **cannot tell the rules apart**, and count them.
5. Ask what **states** your instruments cannot distinguish. Two states with one record is unobservability, and no care with existing instruments repairs it.
6. Ask which **parameters** appear only in combination. That is structural non-identifiability, and you can check it before collecting anything.
7. Decide: **measure more, or model less** — and if you model less, write down that you did.

Check against §§2–6. Steps 4 and 7 are the ones people drop.

### If the transfer went badly

If you compared the rules on one history, reread §2's table and note how many rows do not discriminate.

If you proposed collecting more data to fix a structural non-identifiability, reread §4. That is the chapter's most useful single check and the easiest to forget under pressure.

### Delayed retest

After at least a week, work the other form.

Do not reread this chapter first.
The delay is the test.

### What this chapter did not give you

More is missing here than in any other chapter of this book, and the missing pieces have names.

**Any way to compute an optimal policy.** Comparing four rules is not the same as finding the best one. **Dynamic programming** does that, and it is excluded.

**Any way to recover a state you cannot see directly.** You can now ask whether the state is recoverable in principle.
Recovering it is **state estimation** and **filtering** — observers, the Kalman filter — and they are excluded.

**Any test for structural identifiability.** You have a diagnostic you can apply by eye to a small model.
There are algorithms for real ones, and they are not here.

**Any method for the exploration trade.** The **k-armed bandit** literature is large and is excluded.

**Any control law.** **LQR**, **MPC**, and the whole of controller design are excluded.

**And any treatment of partial observability as a formalism.** §3's problem has a formal home — the **POMDP** — and this book stops at the problem.

Those six exclusions are in the book's architecture by name, so you can go and find them. **What you have instead is the ability to state the question each of them answers**, which is the thing that is hard to acquire afterwards.

**One further gap, of a different kind.** The concept in §4 was named in a 1970 paper this book could not obtain, so the definition you have been given comes from a review.
That is recorded in the chapter's decision record rather than smoothed over.

### What Part IV asks next

Every rule in this chapter was applied to a system that did not care what the rule was.

The reservoir does not know its trigger is set at 150. The weather does not read the operating manual.
The burst main is not waiting to see whether the utility notices.

**Chapter 15 removes that assumption.**

When the system contains people who know what the rule is — customers, contractors, regulators, staff whose bonuses depend on the number the rule watches — the rule stops being a way of responding to the system and becomes part of it.
What you measure gets managed.
What you reward gets produced.
And the relationship you estimated before the rule existed may not survive the rule's existence.
