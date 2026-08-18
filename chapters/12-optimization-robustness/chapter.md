---
chapter: 12
part: 3
title: "Optimization, Robustness, and Adaptive Plans"
status: drafted
---

# Chapter 12: Optimization, Robustness, and Adaptive Plans

## 1. Fifteen Zones, Not One

Eleven chapters of this book have been about Hillcrest.

The utility has fifteen pumped zones, a trunk main, three zones scheduled for mains renewal, and a capital envelope of **£2.4m** for the coming year.
Hillcrest is one line in a programme.

Here is the programme.

| | Scheme | Cost |
|---|---|---:|
| **A** | Hillcrest variable-speed drive | **£40k** |
| **B** | Network pressure management | **£380k** |
| **C** | Zone 4 mains renewal | **£620k** |
| **D** | Zone 9 mains renewal | **£540k** |
| **E** | Zone 12 mains renewal | **£700k** |
| **F1** | Trunk main reinforcement, **stage 1 only** | **£900k** |
| **F2** | Trunk main reinforcement, **full** | **£1,900k** |

F1 and F2 are the same project at two sizes, so only one of them can be built.

Everything the engineers want costs **£5,080k**.
The envelope is **£2,400k**.

### Before reading further

Take about **six minutes**.

> **How would you spend the £2.4m?**
>
> Name the schemes you would fund, and — the part that matters — **say how you decided.**

Keep what you write.
You will come back to it.

---

### Why fifteen is a different problem from one

It is tempting to read a programme as fifteen copies of Chapter 11's decision, to be worked one at a time.
It is not, and the reason is the whole of this chapter.

**Chapter 11's zone had its own budget.** This programme has one envelope covering all fifteen, so **funding Hillcrest is refusing something else** — and the something else is not named in the Hillcrest paper.

**Chapter 11's zone could be solved in isolation.** Here the schemes interact: pressure management changes what the trunk main has to carry, and two zones fed by one main cannot be treated separately.

**And Chapter 11's decision could be made once.** A programme is spent over years, in an order, and the order is itself a choice.

**None of that is arithmetic Chapter 11 taught**, which is why this chapter exists rather than saying *repeat Chapter 11 fifteen times*.

### Two questions, and the second changes the standard

The governed question for this chapter has two halves.

> **How do we choose well at scale when the model itself is uncertain?**

**At scale** is the first half.
When there is one decision you compare acts; when there are seven schemes and a budget you compare **combinations**, and a great deal of useful structure appears that a two-act table cannot show — what the budget is worth, where the returns stop, whether the answer is even findable.

**When the model itself is uncertain** is the second half, and it is a change of criterion rather than a better method.

Chapter 11 found the act with the lowest expected cost, and every figure in it rested on a probability of 0.636. A source that this chapter uses describes that approach from outside, and describes it fairly:

> "Traditional decision analysis seeks the optimal strategy, that is, the one that performs best **for a fixed set of assumptions about the future**." [@lempert2003shaping, p. 52]

That is exactly what Chapter 11 did, and it was the right thing to do there. §6 is about what to do when the fixed set of assumptions is the thing you cannot supply.

**Optimization is not superseded by what follows.** It answers a real question well.
The second half of this chapter answers a different question, which arises when the first question's premise fails.

### What you will be able to do

Five things, and each is a couple of lines of arithmetic on a table the utility already has.

**Rank the schemes by value for money, and know when the ranking is wrong.** It is wrong on this programme, by seven per cent, and the check takes two minutes.

**Price the budget constraint.** Chapter 10 established the envelope was a convention with an author.
This chapter can tell that author what moving it would buy — and finds that an extra fifty thousand pounds is sometimes worth nothing at all.

**Diagnose whether the problem is one a computer can solve properly**, from the shape of that pricing curve, without knowing any mathematics.

**Build a regret table across futures**, and find the programme that is best in none of them and defensible in all.

**Turn that into a plan with a trigger** rather than a review date.

## 2. Objectives and Constraints at Scale

### What changes

With one decision, the acts are alternatives and you pick one.
With seven schemes and a budget, the object of choice is a **combination** — and the arithmetic of combinations is where the interesting structure lives.

Seven schemes with one mutual exclusion give sixty-four possible programmes if money were no object.
The envelope cuts that down, and the set of programmes that fit is the **feasible region**.

That phrase does real work.
It names the thing optimization searches, and it makes visible that the search is bounded by something somebody chose.

Count them, because the number is instructive.
Seven schemes give 128 subsets; the mutual exclusion between F1 and F2 removes 32 of them, leaving 96; and the envelope removes most of the rest. **Fewer than forty programmes fit £2.4m.**

That is few enough to check by hand and far too many to hold in a meeting.
Which is the situation optimization exists for, and it is worth noticing that it arrives at seven schemes rather than at seven hundred.

### And Chapter 10 gets the first word

Before searching a feasible region, ask who drew it.

Chapter 10 examined the utility's four stated constraints and found that two dissolved on inspection.
The **£2.4m envelope** was one of them: an annual planning convention, with an author, and a precedent for moving capital between years twice in five years.

**So the region this chapter searches is bounded by a line that could move.**

That is not a reason to ignore it.
It is a reason §4 exists: once you have optimised inside the boundary, you can ask what moving the boundary would be worth — which is a question Chapter 10 could pose and not answer.

### The three zones nobody has been arguing about

One more thing changes at scale, and it is not arithmetic.

Chapter 10 found that three zones were scheduled for mains renewal from this same envelope, and that they did not appear on the Hillcrest paper.
They are C, D, and E on the list above.

**They are now in the same table as Hillcrest**, competing directly, which is the first time in twelve chapters that the comparison has been possible.

That is what a programme view buys, and it is most of what it buys.
A paper about Hillcrest cannot weigh Hillcrest against Zone 9, because Zone 9 is not in it.
Every organisation that decides scheme by scheme is making a portfolio decision without a portfolio, and the comparison happens anyway — in whichever order the papers reach the committee.

### The benefits

Every scheme has to be worth something, in units that can be compared.

| Scheme | Household-events avoided per year |
|---|---:|
| **A** — Hillcrest variable-speed drive | **95** |
| **B** — Network pressure management | **190** |
| **C** — Zone 4 mains renewal | **210** |
| **D** — Zone 9 mains renewal | **168** |
| **E** — Zone 12 mains renewal | **175** |
| **F1** — Trunk reinforcement, stage 1 | **420** |
| **F2** — Trunk reinforcement, full | **700** |

These are the utility's central forecast.

**And they carry the same caveat Chapter 11's payoff table carried.** A household-event is a compression of things Chapter 10 established were three distinct objectives — households without adequate pressure, whole-life cost, and disruption during works.
Somebody decided the exchange rate.

Every number in §§3 to 5 inherits it. §6 is where that stops being a caveat and becomes the subject.

### What is not in the table

Two things, and both were established earlier in this book.

**The schemes are not independent.** Network pressure management reduces demand everywhere, which reduces what the trunk main has to carry, which means B and F2 together deliver less than the sum of their separate figures.
The table treats them as additive because a table has to.

**That is an assumption**, it is doing real work, and it is the kind of thing Chapter 5 taught you to look for.
On this programme it flatters every combination that includes both.

**And the schemes are not all equally certain.** Chapter 7 found that the Hillcrest mechanism was not identified, so scheme A's benefit of 95 rests on a mechanism the book could not establish.
Scheme C's benefit rests on a mains renewal whose effects the utility has measured many times.

**Two numbers in the same column, with entirely different provenance**, and the column does not say so.
Nothing in §§3 to 5 will distinguish them.

### Where this sits

Nothing about the process has changed.
The six steps Chapter 10 worked from — decision context, objectives, alternatives, prospects, trade-offs, recommendations [@bradley2016structured, p. 8] — apply to a programme exactly as they applied to a choice.

**What has changed is the size of the alternative set**, and that turns out to change what is worth computing.

With three acts, Chapter 11 could show every one against every state and let the reader see the whole problem.
With forty feasible programmes that is impossible, and the useful outputs change accordingly.

**Not the answer alone, but the structure around it.** What the binding constraint is worth.
Where the returns stop.
Which schemes appear in every good programme and which appear in none.
Whether the best programme is meaningfully better than the second.

**That structure is the deliverable.** A committee handed a single recommended programme has been given the least useful output the analysis can produce, and it is the one they are usually given.

### The envelope, and where it came from

**£2.4m** is the figure in the paper.
It is worth asking where it came from, because the whole of §4 depends on the answer.

**It is not a physical limit.** No engineering fact makes £2.4m the amount of capital that can be usefully deployed on this network.

**It is not a solvency limit either.** The utility is not unable to raise £2.6m.

**It is the capital maintenance line in an approved five-year plan**, set by a process that allocated across the utility's whole asset base before anyone looked at these fifteen zones.

**Which makes it a constraint of exactly the kind Chapter 10 taught you to interrogate** — an item somebody chose, on grounds that had nothing to do with the seven schemes now being ranked against it.
Chapter 10 dissolved two of the Hillcrest paper's four constraints by asking who set them and why. §4 asks the same question of this one, and answers it with a number rather than an argument.

### Objectives at programme scale

One thing does get harder at scale, and the chapter should say so before the arithmetic begins.

With one decision, Chapter 10's three fundamental objectives could at least be held in mind while choosing.
With forty programmes they cannot, and the pressure to reduce them to one number is overwhelming — which is what the benefit column above does.

**Two things are worth knowing about that reduction.**

**It is doing more work here than it did in Chapter 11.** There, one exchange rate sat inside six cells.
Here it sits inside seven schemes across three futures — twenty-one numbers — and every comparison in the chapter runs through it.

**And §6 partly undoes it.** The robustness criterion, unlike the value-of-information machinery Chapter 11 used, does not require a single currency; it can assess a programme "with respect to the many different value systems for assessing the performance of the strategies" [@lempert2003shaping, pp. 52–53].
So the plural objectives Chapter 10 established are not permanently lost — they are set aside for §§3 to 5 and recoverable in §6.

**That is worth flagging now** so that a reader who finds §3's single benefit column unsatisfying knows the chapter agrees and knows where the repair is.

### One thing that has not changed

Chapter 11 required a probability.
This chapter, so far, does not.

The benefit table is a set of point estimates under one forecast, and §§3 to 5 will optimise against it without ever asking how likely that forecast is.
That is not an oversight — it is what optimisation is: **finding the best act given a stated model.**

**The model is the forecast.** And Chapters 1, 8, and 9 all found reasons to doubt it: it was conditional on no new action, its errors ran low by about 1.8 ML on the week, and five external sources did not transport to this network.

**§6 is where that doubt becomes the subject rather than a footnote.** Until then, read every figure as conditional on a forecast the book has already criticised — which is exactly the position a real programme analysis is in, and exactly the position nobody states.

### Task: how many programmes fit?

1. List the combinations of the seven schemes that cost **£2,400k** or less, remembering that F1 and F2 are exclusive.
2. Count them.
3. Then say how you would compare them, before reading §3.

Most readers reach for a ranking. §3 is about what that buys and what it costs.

## 3. Reasoning at the Margin

The natural move with a budget and a list is to rank by value for money and fund down the list.

It is a good move, it has a proper name, and it is worth knowing exactly where it works.

### Three definitions

> "**Marginal benefit.** The marginal benefit is the benefit received from an incremental increase in the consumption of a good or service. It is calculated as the increase in total benefit divided by the increase in consumption." [@epa2010economic, p. xiii]

> "**Marginal cost.** The marginal cost is the change in total cost that results from a unit increase in output. It is calculated as the increase in total cost divided by the increase in output." [@epa2010economic, p. xiii]

> "**Opportunity cost.** Opportunity cost is the value of the next best alternative to a particular activity or resource. Opportunity cost need not be assessed in monetary terms. It can be assessed in terms of anything that is of value to the person or persons doing the assessing." [@epa2010economic, p. xiv]

**Note the last two sentences.** Opportunity cost does not require money, or any single currency.

That is worth flagging, because Chapter 11's value-of-information machinery **did** require one — a limitation its own source named — and this chapter's marginal reasoning does not.
Marginal thinking is cheaper in exactly the respect that hurt the last chapter.

### The ratios

Benefit per thousand pounds, under the central forecast:

| Scheme | Per £k |
|---|---:|
| **A** — Hillcrest drive | **2.375** |
| B — Pressure management | 0.500 |
| F1 — Trunk, stage 1 | 0.467 |
| F2 — Trunk, full | 0.368 |
| C — Zone 4 mains | 0.339 |
| D — Zone 9 mains | 0.311 |
| E — Zone 12 mains | 0.250 |

**A is in a different league.** Forty thousand pounds for ninety-five household-events a year is roughly five times the return of anything else on the list, which is the arithmetic behind Chapter 10's finding that a procurement convention had kept it off the paper entirely.

### The rule this is supposed to support

The classical stopping rule is that a market is efficient when prices "reflect their marginal costs, or when marginal benefits equal marginal costs" [@epa2010economic, glossary].

Applied to a budget: **keep funding in order of return until the money runs out.**

### Pause: fund down the list

Before reading on, do it.

> Take the ratio order — A, B, F1, F2, C, D, E — and fund down it until you cannot afford the next scheme. Remember F1 and F2 are exclusive.
>
> **What do you get, and what is left over?**

---

**A + B + F1 + C.** Forty, plus three hundred and eighty, plus nine hundred, plus six hundred and twenty: **£1,940k spent**, benefit **915**, and **£460k unspent**.

D at £540k does not fit.
Neither does E.

### And the ranking is wrong

The best programme that fits the envelope is:

**A + B + F2** — £2,320k spent, benefit **985**.

**The ranking misses by 70**, which is about seven per cent of the achievable benefit and more than half of what scheme B contributes.

Look at why. **F2 has a worse ratio than F1** — 0.368 against 0.467 — so the ranking takes F1 and moves on.
But F2 delivers 700 against F1's 420, and once you have taken F1 the remaining £1,080k cannot buy anything worth 280.

**The ranking optimises the wrong thing.** It maximises return per pound spent, and the utility does not need return per pound.
It needs the most benefit that £2.4m can buy, and those are different objectives whenever the money must be committed in whole schemes.

### What went wrong, stated precisely

The ranking is not wrong because the ratios are wrong.
Every one of them is correctly computed, and every one means what it says.

**It is wrong because a ratio answers a question about one scheme, and the decision is about a set.**

A ratio says: per pound spent on this scheme, this much benefit.
Perfectly true. **What it cannot say is what else that pound could have been part of** — and on an indivisible programme the answer depends on the whole remaining list, not on the scheme in hand.

**F1 has a better ratio than F2 and is the wrong choice**, because taking F1 leaves £1,000k that no combination of what remains can turn into more than F2's extra 280. The ratio cannot see that, because the ratio never looks at what remains.

**The general statement:** ranking is a procedure that evaluates items independently, and the value of an item in an indivisible programme is not independent of the rest of the programme. **The procedure is answering a different question from the one asked.**

That is a stronger claim than *ratios are approximate*.
It says ratios are exactly right about something else.

### Why the ranking is so hard to give up

It is worth being fair to it, because it will still be the right tool most of the time and because the reasons it survives are good ones.

**It is transparent.** Anybody can check a column of benefit-per-pound figures, and anybody can see why scheme A came first.
The optimum is a set, and the argument for it is that no other set does better — which is true, checkable, and completely unilluminating in a meeting.

**It gives an order, not just an answer.** Ranked schemes can be funded down to whatever the envelope turns out to be, which matters when the envelope moves late — as Chapter 10 found this one does.

**And it is defensible when challenged.** *We funded in order of value for money* is a sentence a committee accepts. *We funded the combination that maximises total benefit subject to the constraint* invites the question of who checked, which is usually nobody.

**So the recommendation is not to abandon the ranking.** It is to produce it, then spend two minutes checking it against the best combination that fits — and to expect the check to matter whenever one scheme is large relative to the envelope.

On this programme F2 is 79% of the envelope, which is exactly the condition under which ratios mislead.

### Where the ranking did land

Worth noticing, because it is how such rules survive.

**A + B + C + F1** — the ranking's answer — reappears in §6 as one of the two most robust portfolios in the whole feasible set.

The ratio rule found a defensible programme.
It found it for the wrong reason, and it would not have found it if the numbers had been slightly different.

### A cheaper version of the same check

The full comparison — ranking against best-combination — needs somebody to search the combinations.
On seven schemes that is quick; on seventy it is not something a person does by hand.

**There is a two-minute proxy that catches most of the error.**

**Look at the largest scheme relative to the envelope.** If nothing costs more than about a tenth of the budget, ratios and the optimum will usually agree closely, because the leftover money is always small relative to the next item.

**If one item is a large fraction of the envelope, expect the ranking to be wrong.** F2 is 79% of £2.4m.
The moment such an item is on the list, the question stops being *what order* and becomes *in or out*, and an order cannot answer it.

**A second proxy: look at what the ranking leaves unspent.** £460k on this programme, against a cheapest-remaining scheme of £540k.
Leftover money that cannot buy anything is the signature of a ranking that has stopped in the wrong place — and it is visible without solving anything.

### Where marginal reasoning does work

None of this makes marginal thinking wrong, and it would be a bad lesson to take.

**It works when the quantity is continuous.** How much pressure management to install, how many kilometres of main to reline, how many staff to add — all of these come in fine gradations, and for them "keep going until the next unit costs what it is worth" is exactly right.

**It works when returns are smooth.** If each extra kilometre of relining does slightly less good than the last, the ranking and the optimum coincide.

**It fails when the thing is lumpy.** You cannot build 43% of a trunk main. §5 is about why that matters more than it sounds.

### What a ranking is good for even when it is wrong

Two uses survive, and both matter more than the optimisation.

**It tells you which schemes are never in doubt.** A at 2.375 is five times the next-best return.
No plausible envelope, no plausible future, and no plausible reweighting of objectives excludes it — and Chapter 10 found that a procurement convention had kept it off the paper entirely. **The ranking's most valuable output on this programme is a £40,000 scheme that was invisible.**

**And it tells you which are always marginal.** E at 0.250 is last under the central forecast and appears in no optimum at £2.4m.
That is worth knowing before anyone spends three months developing its business case.

**Neither of those is the programme.** Both are structure, and structure is what a committee can act on.
A ranked list with the top and bottom identified survives the envelope moving, which — on this programme, per Chapter 10 — it does.

### Task: rank, fund, compare

1. Reproduce the ratio table.
2. Fund down it and record what you get.
3. Compare with **A + B + F2 at 985** and say, in one sentence, what the ranking optimised instead.

## 4. What a Constraint Is Worth

Chapter 10 asked whether the £2.4m envelope was a real constraint and found it was a convention with an author.
It could not ask the next question.

**What would it be worth to move it?**

### Shadow prices

The idea has a name and a price interpretation.

> "we can interpret a dual optimal λ⋆ as a set of prices for which there is no advantage to the firm in being allowed to pay for constraint violations (or receive payments for nontight constraints). For this reason a dual optimal λ⋆ is sometimes called a set of **shadow prices** for the original problem." [@boyd2004convex, p. 241]

Strip the machinery and the idea is simple. **A shadow price is what an extra unit of a binding constraint is worth to you.** If somebody offered the utility another £100k of envelope, the shadow price says how much benefit that would buy.

The source's own statement of the interpretation, **paraphrased here because the sentence carries symbols**: the multiplier on a constraint tells you how active it is — a small one means the constraint could be loosened or tightened a little without much effect on the answer, and a large one means the effect would be great [@boyd2004convex, p. 252].
An inactive constraint "can be tightened or loosened a small amount without affecting the optimal value" [@boyd2004convex, p. 252].

**Two cautions come with it, and both are in the source.**

**It is local.** The statement is about loosening or tightening *a small amount*.

**And it is asymmetric.** "the results are not symmetric with respect to loosening or tightening a constraint" [@boyd2004convex, p. 251].
What an extra pound is worth is not the mirror image of what losing one costs.

**One collision to note.** The phrase `shadow price` also appears in cost-benefit analysis in a quite different sense — the shadow price of capital, a discounting concept.
This book uses only the optimization sense, and did not read the other.

### Why this question almost never gets asked

Chapter 10 established that the envelope is a convention with an author and a precedent for exceptions.
So the obvious move is to go and ask for more.

**Almost nobody does, and the reason is structural.**

The request has to be made in a currency the person setting the envelope understands, and *we could do more good* is not one. **What is needed is a number**: another two hundred thousand buys ninety-eight household-events a year, and another fifty buys three.

**That number does not exist until somebody solves the programme more than once.** A single optimisation returns the best programme at £2.4m and says nothing about £2.6m — and running it four times is nobody's idea of a deliverable.

So the conversation about the envelope happens without any of the information that would settle it, and the envelope stays where the convention put it.

**This section is four extra runs of an arithmetic somebody has already done once.**

### The clean case first

Suppose the schemes were divisible — that the utility could buy 43% of a mains renewal and get 43% of the benefit.

Then the answer is the ratio ranking, taken literally.
Fund A, then B, then F2 in full, and spend what is left on the next-best scheme, C, at 12.9% of its size.
Total benefit **1,012.1**.

**And the shadow price is C's ratio: 0.339 per £k.**

That number means something clean.
Another thousand pounds of envelope buys another 0.339 household-events avoided, because it buys a little more of C — and it will keep meaning that until C runs out.

**This is what marginal reasoning promises**: a single number, valid over a range, that tells you what the constraint is worth.

### The real case

The schemes are not divisible.

Here is what an extra slice of envelope actually buys, computed by re-solving the programme at each size.

| Envelope moves from | to | Extra benefit | Per £k |
|---:|---:|---:|---:|
| £2,400k | £2,450k | **+3** | **0.060** |
| £2,560k | £2,610k | **+0** | **0.000** |
| £2,400k | £2,600k | +98 | 0.490 |
| £2,900k | £2,950k | +42 | **0.840** |

**Read those four rows carefully, because each says something different.**

**An extra £50k can be worth almost nothing.** At £2.4m it buys three household-events a year — 0.060 per thousand pounds, against the divisible case's 0.339.

**An extra £50k can be worth literally nothing.** At £2,560k it buys zero.
Not a small amount: none.
There is no combination reachable with £2,610k that beats the best one reachable with £2,560k.

**The answer depends on how far you move.** Fifty thousand is worth 0.060 per £k; two hundred thousand is worth 0.490 per £k.
There is no single number.

**And the marginal value is higher at a bigger envelope than at a smaller one.** 0.840 at £2.9m against 0.060 at £2.4m.

That last one should stop you, and §5 is about why.

### Why the curve looks like that

The four rows are not four measurements of one thing.
They are four different questions, and the answers differ because the underlying object is not smooth.

**At £2.4m the best programme costs £2,320k**, so there is already £80k spare.
Adding fifty thousand gives you £130k spare, and the cheapest unfunded scheme is D at £540k.
Nothing new becomes affordable.
The +3 comes from a small reshuffle at the margin, not from buying anything.

**At £2,560k the same thing happens more starkly**: the best programme costs £2,480k, an extra £50k takes the spare to £130k, and there is still nothing to buy. **Zero.**

**Going from £2.4m to £2.6m crosses a threshold**, and the extra two hundred thousand is what makes a different combination reachable — so it is worth 0.490 per £k, eight times what the first fifty thousand was worth.

**And at £2.9m you are close to affording a programme with both a mains renewal and the full trunk scheme.** The last fifty thousand there is the fifty thousand that unlocks it, and it is worth 0.840.

**None of this is a defect in the analysis.** It is a property of a programme built from indivisible projects, and it means the question *what is another hundred thousand worth* has no single answer — it has an answer for each hundred thousand.

### The practical upshot

**Never quote a shadow price without the size of the move it refers to.**

"An extra £100k would be worth about 34 household-events" is a sentence that sounds precise and is, on this programme, simply false — it is the divisible answer applied to an indivisible problem.

The honest form is a small table: **here is what £50k more buys, here is what £200k buys, here is what £500k buys.** Three numbers, an hour's work, and they tell a finance committee something no single figure can.

### What the number is for

A shadow price is not an academic quantity.
It is the answer to a question somebody in the organisation is going to ask, and it changes what the utility can say.

**Without it:** *we could do more with a larger envelope.* True of every programme ever proposed, and worth nothing to whoever sets envelopes.

**With it:** *another £200k would buy 98 household-events a year — about half a Zone 4 mains renewal — and another £50k on top of the current figure would buy almost none, because nothing new becomes affordable until £2.6m.*

**That second sentence is a different kind of conversation.** It names a threshold.
It tells the person with the envelope that £2.45m is not worth arguing for and £2.6m is.
And it is checkable — anyone can re-solve and disagree.

**It also works in the direction nobody volunteers.** If the envelope is going to be cut, the utility can say what the first £200k of cuts costs before the cut is made, rather than discovering it afterwards.

### Two ways to read a zero

The £50k that bought nothing has two readings and they lead in opposite directions.

**The first: the envelope is well set.** No obvious gain from more money, so the figure is about right, and the utility should stop asking.

**The second: the envelope is badly set, and £50k is simply the wrong increment to test.** The step from £2.4m to £2.6m buys 98. The zero at £50k says nothing whatever about whether £2.4m is the right number — it says only that £2.45m is not.

**The second reading is correct, and the first is the one organisations reach for**, because a zero is easy to report and easy to accept.

**The practical rule: never price a constraint at one increment.** A single probe of a lumpy problem can land anywhere on a staircase, and a step's flat part is not information about the staircase.
Price it at several, and report the shape rather than a number.

### And what it is worth to move it the other way

The asymmetry the source flags has a practical form that finance committees will recognise.

**Suppose the envelope is cut to £2.2m.** The best programme reachable is A + B + C + F1 at £1,940k, benefit **915** — a loss of **70** against the £2.4m optimum, for a cut of £200k.

**That is 0.350 per £k**, against the 0.490 per £k that adding £200k would have gained.

**Losing money hurts less per pound than gaining it helps**, on this programme, at this point.
There is no reason it should be the other way round on a different programme, and no way to know without computing both.

Which gives the practical rule: **if you are going to argue about the envelope, compute both directions.** The number you need to defend an increase is not the number you need to survive a cut, and quoting one when asked about the other is the ordinary way this goes wrong.

### Task: price the envelope

1. Compute what an extra **£200k** is worth on this programme.
2. Compute what an extra **£50k** is worth.
3. Explain the difference in one sentence.
4. Then say what you would tell a finance director who asked "what would another hundred thousand buy?"

## 5. When Local Improvement Finds the Best

§4's table behaved badly, and the reason has a name.

### Convexity, through what it does

There is a property that optimization problems either have or do not, and it decides almost everything about whether they can be solved.

**This book does not teach how to recognise it.** The standard reference says plainly that "recognizing a convex function can be difficult" [@boyd2004convex, p. 8], and a chapter promising no specialist training is not going to do better.

**What the book teaches is the consequence**, which a reader can act on without any mathematics.

**When a problem is convex**, local improvement finds the global best, reliable methods exist, and the source puts the practical position strongly:

> "With only a bit of exaggeration, we can say that, **if you formulate a practical problem as a convex optimization problem, then you have solved the original problem.**" [@boyd2004convex, p. 8]

Such problems, it notes, can be solved "with hundreds of variables and thousands of constraints on a current desktop computer, in at most a few tens of seconds" [@boyd2004convex, p. 8].

**When it is not**, the position is bleak and the source does not soften it:

> "Sadly, **there are no effective methods for solving the general nonlinear programming problem.** Even simple looking problems with as few as ten variables can be extremely challenging, while problems with a few hundreds of variables can be intractable." [@boyd2004convex, p. 9]

### What you get instead

You get a **local optimum**: a point that "minimizes the objective function among feasible points that are near it, but is not guaranteed to have a lower objective value than all other feasible points" [@boyd2004convex, p. 9].

Two consequences follow, and both are things a reader can check for.

**The answer depends on where you started.** "This initial guess or starting point is critical, and can greatly affect the objective value of the local solution obtained" [@boyd2004convex, p. 9].

**And you are not told how wrong it might be.**

> "**Little information is provided about how far from (globally) optimal the local solution is.**" [@boyd2004convex, p. 9]

**That is a different situation from anything in Part II.** Chapter 8's estimate came with an interval; the interval covered less than it appeared to, and the chapter spent six pages on that, but it existed.
A local optimum comes with nothing.
There is no bound, no interval, and no way to compute one from the answer itself.

### Where this shows up outside optimisation

The lumpiness point is not confined to capital programmes, and it is worth seeing in a form readers will recognise.

**Staffing.** You cannot hire 0.4 of a specialist.
The marginal return to headcount is a step function, and *hire until the marginal hire pays for themselves* has no fixed point.

**Coverage.** A monitoring station covers a catchment or it does not.
Half a station monitors nothing.

**Compliance.** Meeting a standard is binary.
Ninety per cent of a permit condition is a breach.

**In every one, the same three symptoms appear**: leftover resource that cannot buy anything, an extra increment worth nothing, and a larger increment worth a great deal.

**And in every one, the marginal rule is taught and applied anyway**, because it is what everybody learned and because the failure is quiet.
Nothing goes visibly wrong; the organisation simply funds the wrong combination and never learns that a better one existed.

### Pause: why did £50k buy nothing?

Before reading on, work it out.

> At £2,560k an extra £50k bought zero benefit. And an extra £50k at £2.9m bought **0.840** per £k, while at £2.4m it bought **0.060**.
>
> **How can more budget be worth more per pound than less budget was?**

---

Because the schemes come in lumps.

At £2,560k the best programme costs £2,480k, and the cheapest thing that could improve it costs far more than the £130k you would then have. **The extra fifty thousand sits there.** It is not too little to be useful in general; it is too little to reach the next lump.

And at £2.9m you are close to affording a combination that includes both a mains renewal and the full trunk scheme — so the last fifty thousand there is the fifty thousand that unlocks it.

**Under convexity this cannot happen.** The marginal value of a budget is non-increasing: the first pound is worth at least as much as the millionth.
Here it is not, and that is the diagnostic.

**You can see it in a table without any mathematics.** Re-solve at several budget sizes, look at what each increment buys, and if the increments do not shrink, the problem is lumpy — and the marginal stopping rule has no fixed point to stop at.

### Why the failure is invisible from inside

The uncomfortable feature of §3's error is that the organisation that makes it sees nothing wrong.

**The ranking produces a defensible-looking programme.** Four schemes, funded in order of value for money, each individually justified.

**The £460k that could not be spent looks like prudence**, or like a contingency, or like next year's start — and there is always a story available.

**And the better programme is never seen**, because nobody solved for it.
You cannot miss what was never on the paper.

**This is why the check has to be a habit rather than a response to a symptom.** Chapter 5 made the same point about model failure and Chapter 8 about analytic choices: the errors this book is concerned with do not announce themselves.
They produce plausible outputs, and the only defence is a procedure applied before there is any reason for suspicion.

### The lumpiness test

Recognising convexity is hard.
Recognising lumpiness is not, and for the decisions this book's readers face it is the same question in practice.

Three checks, all of which take a minute.

**Can you buy part of it?** Sixty per cent of a pressure-management programme is a real thing and delivers roughly sixty per cent of the benefit.
Sixty per cent of a trunk main is a hole in the ground.

**Does the benefit arrive gradually or at the end?** A relining programme delivers as each kilometre completes.
A treatment works upgrade delivers nothing until commissioning.

**Is any single item large relative to the budget?** F2 is 79% of the envelope.
When one item dominates, the combination problem is genuinely combinatorial and every intuition built on smooth trade-offs fails.

**On this programme all three answers point the same way**, and that is why §4's curve behaved as it did.

The general form of the diagnostic: **re-solve at several budget sizes and look at whether the increments shrink.** If they do not — if more budget is worth more per pound than less budget was — the problem is lumpy, and the marginal stopping rule has nothing to stop at.

That check needs no mathematics, no software, and no vocabulary.
It needs the willingness to solve the problem four times instead of once.

### What to hand to a solver, and what to keep

The governed competence for this chapter includes handing problems off to computation, and the source states the position exactly.

**The solving is a solved problem, for the right class of problem.** Reliable methods exist, they run in seconds, and there is no craft in operating them.

**The recognising is not.** "Recognizing a least-squares problem is straightforward, but recognizing a convex function can be difficult...
Recognizing convex optimization problems, or those that can be transformed to convex optimization problems, can therefore be challenging" [@boyd2004convex, p. 8].

So the division of labour is not what most people assume.

**Hand over:** the search.
Finding the best combination of seven schemes under a budget is arithmetic a computer does instantly and a person does badly.

**Keep:** which schemes are on the list, what the constraints really are, what the benefits mean, what units they are in, and what the answer is conditional on. **None of that is in the solver**, and all of it decides the answer.

**And ask one question of any optimised result**: is this the best, or the best that was found? If nobody can tell you, you have a local answer and no idea how far off it is.

### What optimisation is actually for

Having spent a section on what it cannot do, the positive case deserves stating, because the chapter would mislead if it stopped at the limits.

**It finds things a committee will not.** The optimum on this programme includes F2 over F1, which no ranking would select and no meeting would propose, because F2's return per pound is worse.
It is right anyway, and only a search over combinations finds it.

**It prices the constraint.** §4's table is the by-product of solving the same problem at several budgets, and it is the output a finance committee can most directly use.

**It shows what is never in the answer.** Scheme E appears in no optimal programme at £2.4m under the central forecast.
That is worth knowing before its business case is written.

**And it makes the assumptions do visible work.** Change the benefit column and the answer changes, traceably.
A committee's judgment changes the answer too, and untraceably.

**None of that requires the answer to be trustworthy.** The optimum on this programme rests on a benefit column that compresses three objectives at an unstated exchange rate, in one future out of three. §6 is about that.
What §§3 to 5 establish is that even a doubtful model, searched properly, yields structure that a doubtful model argued over does not.

### Task: find the lumpiness

Take a resourcing or investment decision in your own organisation.

1. List the things that could be funded, with costs.
2. Mark which are **divisible** — you could buy 60% of them and get roughly 60% of the value — and which come in lumps.
3. For one lumpy item, say what the smallest useful increment is.
4. Then say whether anyone has ever asked what an extra ten per cent of budget would buy, and whether the answer they gave was a single number.

## 6. When the Model Itself Is Uncertain

Everything so far has taken the benefit table as given.
It is time to ask where it came from.

### The forecast underneath

The benefits in §2 are the utility's central forecast: what each scheme would deliver if demand grows as Chapter 1 projected.

**Chapter 1 said that forecast was conditional on no new action.** Chapter 8 found the forecasts ran low by about 1.8 ML on the week.
Chapter 9 found five sources that did not transport.
And nobody has ever checked what the trunk main is worth if demand does something the forecast did not anticipate.

**So the model that generated §3's optimum is itself in doubt**, and that is a different problem from the ones Part II treated.
It is not that the numbers are noisy.
It is that the table would look different under a different future, and nobody can say which future.

### A different criterion

The source that supplies this section states the position plainly:

> "What criterion should decisionmakers use to compare alternative solutions for long-term policy challenges? Traditional decision analysis seeks the optimal strategy, that is, the one that performs best for a fixed set of assumptions about the future. In contrast, LTPA requires a standard that allows analysts to make policy arguments true across a multiplicity of unpredictable futures." [@lempert2003shaping, p. 52]

And the reframing:

> "Rather than first predicting the future in order to act on it, decisionmakers may now gain a systematic understanding of their best near-term options for shaping a long-term future **in the absence of any reliable predictions**." [@lempert2003shaping, p. 39]

### Scenarios are not forecasts

The device is an **ensemble** of plausible futures, and its purpose is adversarial.

> "Ensembles also offer compelling alternative futures that can force stakeholders to question their assumptions and provide a framework to understand the views of others who might hold very different expectations about the future." [@lempert2003shaping, p. 52]

**A scenario is a challenge set, not a prediction**, and this chapter attaches no probabilities to the three futures below.
That is deliberate: if you could attach probabilities you would be back in Chapter 11.

**And what governs the ensemble is diversity, not count.**

> "the **diversity requirement** that guides the construction of scenario ensembles is crucial to building credibility among parties to a decision." [@lempert2003shaping, p. 52]

Twenty futures differing in one parameter are one future.
The source also notes that plausibility is enforced — paths are excluded when they "violate known principles of economics" [@lempert2003shaping, p. 52] — so an ensemble is not everything imaginable either.

### Three futures

| | A | B | C | D | E | F1 | F2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **As forecast** | 95 | 190 | 210 | 168 | 175 | 420 | 700 |
| **Demand high** | 70 | 150 | 190 | 150 | 160 | 620 | **1,400** |
| **Demand flat** | 130 | 260 | 280 | 230 | 240 | **60** | **80** |

**Under demand high**, the trunk main is nearly everything.
Under **demand flat** it is close to a stranded asset and the local schemes carry the programme.

Notice what happens to the local schemes: their benefits *rise* under flat demand, because with less pressure on the network the improvements they deliver are not swamped.

### Where the futures came from

Three is not many, and the choice of which three matters more than the count.

**They differ in kind, not in degree.** Not the forecast plus or minus ten per cent — that would be one future measured three times, and the diversity requirement above is precisely a warning against it.
These three differ in **which scheme matters**: under high demand the trunk main is everything; under flat demand it is nearly worthless and the local schemes carry the programme.

**Each is defensible on its own terms.** Demand grows faster if the region's housing plan proceeds and summers continue as they have.
It goes flat if the metering programme and leakage reduction succeed, which the utility is separately spending money on.
Neither requires anything implausible.

**And none of them is a disaster scenario.** The ensemble is not there to frighten anybody; it is there to find out which programmes depend on which assumptions.

**What three futures cannot do** is bound the possibilities.
A fourth — demand grows and a major asset fails early — would change the table, and the honest position is that the ensemble is a challenge set of the size somebody had time to build.

### The best programme in each future

| Future | Best programme | Cost | Benefit |
|---|---|---:|---:|
| As forecast | **A + B + F2** | 2,320 | 985 |
| Demand high | **A + B + F2** | 2,320 | 1,620 |
| Demand flat | **A + B + C + D + E** | 2,280 | 1,140 |

**Two futures agree and one does not**, and the disagreement is total: one programme builds a trunk main, the other builds three mains renewals, and they share only the two cheapest schemes.

### Regret

The measure that lets you compare programmes across futures without probabilities.

**Regret is the shortfall between what a programme delivers in a future and the best that could have been delivered in that future.** It answers: if this future arrives, how much will I wish I had chosen differently?

| Programme | Cost | As forecast | Demand high | Demand flat | **Max** |
|---|---:|---:|---:|---:|---:|
| A + B + F2 | 2,320 | 0 | 0 | 670 | **670** |
| A + B + C + D + E | 2,280 | 147 | 900 | 0 | **900** |
| **A + C + E + F1** | 2,260 | 85 | 580 | 430 | **580** |
| A + B + C + F1 | 1,940 | 70 | 590 | 410 | **590** |

### Pause: which would you defend?

Before reading on.

> **Which of those four would you put in front of the board, and what would you say about it?**

---

### The robust choice

**A + C + E + F1**, with a maximum regret of **580**.

It is not the optimum under the central forecast — it gives up 85 there.
It is not the optimum under high demand — it gives up 580. It is not the optimum under flat demand — it gives up 430.

**It is optimal in no future at all**, and that is the point rather than a defect.

> "An argument that is insensitive to significant variation in its underlying assumptions is said to be robust. In this sense, **a strategy should be considered robust if it performs reasonably well compared to the alternatives across a wide range of plausible futures.**" [@lempert2003shaping, p. 52]

Compare it with the programme §3 produced. **A + B + F2** is perfect in two futures and gives up **670** in the third.
It is a bet that demand does not go flat, and nobody has established what that bet is worth, because there are no probabilities here to establish it with.

### And robustness repairs something Chapter 11 broke

There is a clause in the definition that is easy to skim.

> "The use of the normative concept of performing 'well' therefore also suggests robustness should be assessed with respect to the **many different value systems** for assessing the performance of the strategies." [@lempert2003shaping, pp. 52–53]

**Across value systems, not just across futures.**

Chapter 10 established that the utility has three fundamental objectives that conflict.
Chapter 11 had to collapse them into one currency, because value-of-information machinery requires it — and its own source named that as the sharpest limitation of the method.

**Robustness does not require the collapse.** A programme can be assessed as robust across futures *and* across different ways of weighing households against cost against disruption.
Chapter 10's plural objectives survive into Part III's arithmetic instead of being flattened by it.

That is a real advantage and it is worth knowing which chapter's method has it.

### The rule's own author objected to it

This chapter is not going to present minimax regret as the right rule, because the source does not.

> "This concept of robustness draws from, but is not identical to, **L. J. Savage's criterion of minimizing the maximum regret.**" [@lempert2003shaping, p. 53]

And it reports what Savage himself said against it:

> "the rule often yields neither a best strategy nor a simple ordering among strategies. Furthermore, in a group context, the rule can be undemocratic because the importance of a view is independent of the number of people who hold it. Participants can easily manipulate outcomes by lying about the weights they assign to alternative futures. In some cases, the mini-max rule can be too sensitive to low-probability, high-consequence events, thereby producing clearly unreasonable results." [@lempert2003shaping, p. 53, n. 13]

**Four objections, and the first arrives immediately on the anchor.**

The minimax portfolio scores **580**.
The runner-up scores **590**.
Those numbers come from benefit estimates that are themselves compressions of three objectives with an unstated exchange rate, in three futures nobody has probabilities for.

**580 is not better than 590.** The rule has not produced a winner; it has produced a shortlist of two, which is exactly "neither a best strategy nor a simple ordering."

*Savage (1950) was not obtained for this book.
The criterion and its objections are used as reported at the page cited.*

### The two criteria answer different questions

It is worth being precise about the relationship, because "robust" gets used as a synonym for "good" and it is not one.

**Optimisation asks:** given this model of the future, which programme is best?

**Robustness asks:** across these models of the future, which programme is least bad in the worst case?

**Neither dominates.** If the utility genuinely believes its central forecast — if the demand projection is well founded and the alternatives are remote — then optimising against it is correct, and choosing A + C + E + F1 gives away 85 household-events a year for nothing.

**The question is whether the forecast deserves that confidence**, and this book has spent nine chapters establishing how one would find out.
Chapter 8 found the utility's forecasts ran low.
Chapter 9 found nothing external that transported.
Chapter 1 found the forecast conditional on no new action.

**On this network, the answer is that it does not.** Which is a judgment, arrived at from the book's own findings, and the honest form is to say so rather than to present robustness as generally superior.

**And there is a middle position the table supports.** If you think the flat-demand future is genuinely unlikely but not negligible, A + B + F2 costs you 670 in a case you consider improbable, and the robust choice costs you 85 in the case you consider likely. **Which of those you prefer is a value judgment about how much you dislike being badly wrong** — which is Chapter 11's risk attitude, arriving in a setting where there are no probabilities to be neutral about.

### Robustness is not free

One more thing the section must say plainly.

**A + C + E + F1 gives up 85 household-events a year under the central forecast**, which is the future the utility's own planners think most likely, and **580 under high demand.**

That is the price of not betting.
Whether it is worth paying is a judgment about how much the utility trusts its own forecast, and — as with everything in Part III — the arithmetic cannot supply it.

The source is honest about this: "one is rarely fortunate enough to engage in LTPA that results in an ideal strategy with good performance properties in all plausible futures judged by all relevant value systems.
In practice, long-term decisionmaking becomes an exercise in juggling difficult trade-offs" [@lempert2003shaping, p. 57].

### What the regret table shows besides the winner

The table is more informative than the single row it selects, and the extra information is what a board actually needs.

**Look down the columns rather than across the rows.**

**Under the central forecast every programme is within 147 of the best.** Whatever the utility does, if the forecast holds, it will do roughly as well.
The central forecast is not where the decision matters.

**Under demand high the spread is 900.** This is the future that discriminates, and it discriminates almost entirely on whether the trunk main is built at full size.

**Under demand flat the spread is 670**, and it discriminates on whether the money went into the trunk at all.

**So the whole decision reduces to one question**: how big to build the trunk main.
Schemes A through E shuffle the margins; F is the bet.

**That is a finding a committee can use**, and it is not visible in any single recommended programme.
It says where to spend the argument, and it says that arguing about Zone 9 against Zone 12 is arguing about the wrong thing.

### One more portfolio worth looking at

**A + B + C + F1** — the one the ratio ranking accidentally produced in §3 — has a maximum regret of **590**, ten worse than the minimax choice.

**And it costs £1,940k**, leaving **£460k uncommitted.**

The regret table does not know that.
It scores programmes on benefit delivered, and uncommitted money delivers nothing in any of the three futures.

**But uncommitted capital in a decision about an uncertain future is not nothing**, and §7 is where it becomes the most interesting thing on the table.

### What the table does not settle

Three things, and the manuscript is not going to pretend otherwise.

**Which futures belong on it.** The three here were chosen; a fourth — sustained drought, say, or a regulatory change in service standards — would change the minimax answer.
There is no procedure that generates the right set, and the criterion is only as good as the set it ranges over.
Chapter 9 met the same problem under the name of which sources to include, and it does not become easier here.

**Whether the benefit figures under each future are right.** They are the utility's own projections re-run under different demand assumptions, which means they inherit every limitation Chapters 5, 7 and 8 identified.
Regret computed from wrong benefits is wrong regret.

**And whether minimax regret is the criterion the utility should use.** It is one criterion among several, it has a live objection from its own author, and this chapter has not claimed it is generally correct — only that it answers a question the expected-value machinery cannot answer when there are no probabilities to be had.

**All three are reasons to show the table rather than only its winner**, which is what §7 does with the plan.

### Task: build the table

1. Reproduce the regret table from the three futures.
2. Identify the programme with the lowest maximum regret.
3. Say what it is optimal in.
4. Then state what it gives up, in each future, against what could have been had.

Question 4 is the one that stops robustness sounding free.

## 7. Adaptive Plans

Go back to the runner-up.

**A + B + C + F1 costs £1,940k**, leaving **£460k uncommitted** against a £2.4m envelope.
In an ordinary capital paper that is a failure — money not spent is money handed back.

In a decision about an uncertain future it is something else.

### Adaptivity as the route to robustness

> "People learn. Over time, they will gain new information. Accordingly, **adaptive decision strategies are the means most commonly used to achieve robustness because they are designed to evolve in response to new data.** Faced with a multiplicity of plausible futures, a decisionmaker may settle on near-term actions but plan to adjust them **in specific ways** as new information renders some futures implausible and others more likely." [@lempert2003shaping, p. 57]

**"In specific ways."** That phrase is the difference between an adaptive plan and a vague one, and organisations produce far more of the second.

The same source puts the link compactly at p. 40: strategies are often robust **because** they are adaptive.

### Three parts

There is a named structure, reported in the source and attributed there to Dewar's assumption-based planning:

> "This approach comprises **shaping actions** intended to influence the future that comes to pass, **hedging actions** intended to reduce vulnerability if adverse futures come to pass, and **signposts** or observations that warn of the need to change the mix of actions." [@lempert2003shaping, p. 58]

*Dewar (1993, 2001) was not obtained for this book; the structure is used as reported.*

Work it on the programme.

**Shaping — B, network pressure management.** It reduces demand on every zone, which makes the high-demand future less likely to arrive and less bad if it does.
It is the only scheme on the list that acts on the future rather than within it.

**Hedging — A and C, and F1 rather than F2.** A and C are useful in every future.
And the trunk decision is the real hedge: **stage 1 buys the capacity all three futures need, without committing to the capacity only one future needs.**

**Signposts — and this is the part that is missing.**

### A review date is not a signpost

The utility already collects both of the observations it would need.

**Peak-week demand**, measured every summer, against the Chapter 1 forecast.

**Heat events per year**, which it counts for regulatory reporting anyway.

What it does not have is a **threshold**, agreed in advance, that would trigger stage 2.

**That is the whole difference.** A plan that says *we will review this annually* has not said what would change it, so it will be reviewed by whoever is in post, against whatever seems reasonable at the time, under whatever pressure the year brings.
A plan that says *if peak-week demand exceeds the forecast by more than four per cent in two consecutive summers, stage 2 proceeds* has made the decision once, in advance, when nobody was under pressure.

**The threshold has to be a number and it has to be written down.** Everything else is a diary entry.

### The option is not free

Building the trunk main's second stage later costs more than building it all at once.
The utility's estimate is **£1,150k later against the £1,000k it would have added today** — a **£150k premium**.

**That premium is what the flexibility costs**, and stating it is what stops adaptive planning being a way of avoiding decisions.

An adaptive plan whose optionality is free is not a plan.
It is a refusal to choose, dressed in the vocabulary of one — and the test is whether anybody has priced the staging.

*The £150k is an assumption in this case, not a measurement.*

### Two ways adaptive plans fail

The structure is easy to state and hard to keep, and it fails in two directions.

**The plan becomes a portfolio.** Shaping and hedging actions get funded, the signposts get written into an appendix, and nobody is accountable for looking at them.
Two years later the trigger condition has been met for four months and nobody has noticed, because watching a signpost is nobody's job description.

**Or the plan becomes an excuse.** Stage 1 gets built, the option is celebrated as prudent flexibility, and stage 2 is deferred at every review on the grounds that the plan was always adaptive. **Adaptivity becomes a permanent reason not to decide**, which is precisely what pricing the staging premium is supposed to prevent: at £150k a year of deferral, somebody has to justify the delay.

**Both failures have the same root.** An adaptive plan makes a commitment about the *future* — that a specified observation will produce a specified action — and organisations are much better at commitments about the present.

**The remedy is unglamorous.** Name the observation, name the threshold, name the person, and put the review of the signpost on the same cycle as the review of the spend.
Chapter 17 is about operating that, and it is where the question of whether anyone is actually looking belongs.

### Name what you have decided not to care about

The source ends its treatment with a requirement that is the best sentence in it, and the last instance of a discipline this book has applied in six chapters.

> "they should emerge with a robust strategy and a clear understanding of the values and futures for which it performs adequately. **They should also be explicitly aware of the futures and values that, by virtue of selecting the candidate strategy, have been implicitly classed as unimportant.**" [@lempert2003shaping, p. 57]

For this programme, written out:

**The future classed as unimportant is a demand shock arriving faster than two summers of signpost data can detect.** If demand jumps in one year, stage 1 will be inadequate and stage 2 will not have been triggered.
The plan has decided that this is unlikely enough to accept.

**The value classed as unimportant is disruption.** Chapter 10 found three fundamental objectives, and the benefit numbers throughout this chapter weight households and cost.
Zone 12 residents, whose renewal is deferred under most of these programmes, are not visible anywhere in the arithmetic.

**Neither of those is wrong.** Both are choices, and neither was made deliberately until this paragraph.

You have met that structure in Chapter 6 with unstated conditioning, Chapter 7 with identifying assumptions, Chapter 8 with analytic conduct, Chapter 10 with values, and Chapter 11 with the decision rule. **Something load-bearing is always operating unwritten, and writing it down is the whole method.**

### What the plan actually is

Written out, so that it is a document rather than a disposition.

> **Now.** Fit the Hillcrest variable-speed drive (**A**, £40k). Install network pressure management (**B**, £380k). Renew the Zone 4 main (**C**, £620k). Build stage 1 of the trunk reinforcement (**F1**, £900k). Total **£1,940k**, leaving **£460k uncommitted** against the envelope.
>
> **Watch.** Peak-week demand against the Chapter 1 forecast, reported each September. Heat events per year, already counted for the regulator.
>
> **If.** Peak-week demand exceeds the forecast by more than four per cent in two consecutive summers, **or** heat events exceed six in a single year, stage 2 of the trunk reinforcement enters the following year's programme at an assumed **£1,150k**.
>
> **Owner.** The asset planning lead reports both signposts to the capital committee each October, whether or not either has triggered.
>
> **What this plan gives up.** If demand jumps in a single year rather than two, stage 1 will be inadequate and the trigger will not have fired. And Zone 12's renewal is deferred indefinitely, which the arithmetic in this chapter does not see because disruption to Zone 12 residents is not in the benefit column.

**Five short blocks, and the last two are the ones that would be missing.**

The threshold in the third block is where the plan lives. **Four per cent, two consecutive summers, six heat events** — those numbers are arguable, and being arguable is the property that matters.
A committee can dispute four per cent.
It cannot dispute "we will keep this under review".

### Task: diagnose five defects

Each statement below contains one defect.
Write the defect, what it stops you concluding, and a repair.

1. *"We ranked the schemes by benefit per pound and funded down the list until the money ran out."*
2. *"The optimiser found the best programme, so that is the programme."*
3. *"An extra £100k would be worth about 34 household-events a year."*
4. *"We tested twenty scenarios, so the plan is robust."*
5. *"The plan is adaptive — we will review it annually."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

## 8. Cold-Start Practice and Retrieval

### Return to your six-minute answer

Find what you wrote at the start of §1.

Read it against what you can now produce.
Do not score it.

- Did you name a **rule**, or a list of schemes?
- If you ranked by value for money, did you notice what it left over?
- Did you ask what would happen if the demand forecast were wrong?

Three patterns are common.

Most readers rank by benefit per pound.
It is the right instinct, it is what §3 teaches properly, and on this programme it misses the optimum by seventy and leaves £460k on the table.

Some readers spread the money across zones for fairness.
That is a value judgment, it is a legitimate one, and it should be stated as one rather than presented as a method.

Very few ask about the forecast. **The benefit table looks like data and is a model**, and §6 is the half of the chapter that most readers do not anticipate.

### Independent transfer

Now work an unfamiliar situation, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below.
Open only that one.

- [Form A — A port authority's berth and dredging programme](transfer-form-a.md)
- [Form B — A health system's diagnostic capacity programme](transfer-form-b.md)

Allow about **50 minutes**.
Every fact you need is supplied.
Do not look anything up.

Do not open the other form.
You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the procedure from memory

Before looking back, write down how you would handle a programme decision under a budget.

Aim for the sequence, not the wording.

1. What are the candidate **schemes**, with costs?
2. What is the **constraint**, and **who set it**?
3. What are the **benefits**, in what units, and what did the unit conversion assume?
4. Rank by benefit per pound — and then **check the ranking against the best combination that fits.**
5. Are the schemes **lumpy**? Can you buy part of one?
6. What is an extra slice of budget **worth** — at £50k, at £200k, at £500k?
7. Do those increments **shrink**? If not, the marginal rule has no stopping point.
8. What **futures** would change the benefit table? Aim for three that differ in kind.
9. Build the **regret table**. Which programme is least bad across all of them?
10. What is the **signpost** — a named observation, with a named threshold, that would change the plan?

Step 3's second half is where the value judgments went.

Step 4 is two minutes and catches an error most programmes contain.

Step 10 is the one that gets replaced by "we'll review it annually", which is not an answer.

### If the transfer went badly

- **You ranked and stopped.** Reread §3. The ranking optimises return per pound, and a budget holder does not want return per pound.
- **You quoted a single shadow price.** Reread §4. Give a small table of increments instead.
- **You treated the benefit table as fact.** Reread §6. It is a model, and §6 is what to do when the model is the uncertain thing.
- **You picked the programme that was best under the central forecast.** That is a bet on the forecast, and the regret table prices it.
- **Your adaptive plan had a review date.** A signpost is an observation with a threshold.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Do not reread this chapter immediately beforehand, and do not look at the form you have not done.

### What this chapter did not give you

**Any method.** No algorithm, no formulation, no solver.
The chapter taught what the answers mean and what makes them findable, which is the part that does not come with the software.

**Any way to recognise convexity.** The source says it is difficult and this book teaches only the consequence — and the lumpiness test in §5, which is a practical proxy and not the property itself.

**Any way to weigh robustness against performance.** §6 priced what the robust programme gives up and stopped.
How much you should pay for not betting is a value judgment, and Chapter 10 established whose it is.

**Any probabilities over futures.** Deliberately.
If you had them you would be in Chapter 11.

**Any treatment of real options or adaptive management.** Both were named; neither is taught.

**And nothing about what happens after you act.** Which is the next part of the book.

### What Part IV asks next

Part III is over.
Three chapters on choosing: what matters, which act is defensible, and how to choose at scale when the model is in doubt.

Every one of them treated the world as something that happens **to** the decision.

The demand forecast might be wrong, the mechanism might be either of two, the future might be one of three — but in all of it the network sits there, and the utility acts on it, and the consequences follow.

**That is not what the utility's network does.**

Chapter 1 already found it.
The seven-day demand forecast was conditional on **no new action** — because when the utility asked people to use less water, they did, and the forecast that had been correct stopped being correct **because the utility used it.**

A system that responds to what you do is a different object from a system that merely varies.
The pressure you relieve in one zone appears somewhere else.
The capacity you add gets used.
The signpost you set gets watched by people who know what it triggers.

**Part IV is called Act in Responsive Systems**, and Chapter 13 starts with the simplest version of the problem: what happens when the effect of an action feeds back into its own cause.
