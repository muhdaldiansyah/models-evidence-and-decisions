---
chapter: 6
part: 2
title: "Probability, Prediction, and Simulation"
status: drafted
---

# Chapter 6: Probability, Prediction, and Simulation

## 1. How Likely Is It?

Chapter 5 ended by pointing at a list.

Almost every unresolved item in Part I had turned into a question about evidence, and Part I had supplied no way to answer any of them:

- **Does the Hillcrest tank typically start a shortage at around 0.6 ML?** The logs would settle it in an afternoon. Nobody has looked.
- **What would the pump test actually tell us?** Chapter 2 named the test. Chapter 5 confirmed it was obtainable and had not been done. Neither could say what it would establish.
- **Is Mechanism A or Mechanism B operating?** Open since Chapter 2. Still open.

Part I could say *it might be* and *it might not*. That is the whole of what it had.

That is not a failure of Part I. It is what Part I was for.

Each of its five chapters handed you a discipline, and none of them was about weighing evidence.
Chapter 1 asked what question a decision actually needs answered.
Chapter 2 asked what belongs in a representation and what may be left out.
Chapter 3 asked whether the numbers mean what the label on them says.
Chapter 4 asked how the records came to exist and what that does to the quantity you want.
Chapter 5 asked how a formulation could fail and what would show it.

Every one of those is a question about **whether something is fit to use**.
Not one of them is a question about **how far a piece of evidence should move you**.

So Part I could establish that the pump test was the right test, that it was obtainable, and that nobody had run it — and then stop, with no way to say whether running it would settle anything.
That last step is what this chapter supplies, and it turns out to require exactly one multiplication.

### The two mechanisms, briefly

You met these in Chapter 2 and it has been three chapters. Both explain why Hillcrest loses pressure before the other zones.

**Mechanism A — pump capacity.** Hot weather raises demand. Hillcrest's water arrives only through the duty pump, which has a fixed capacity of **1.1 ML per day**. When the zone's draw exceeds what the pump can replace, the hilltop tank falls, and pressure falls with it.

**Mechanism B — the feeder main.** Hillcrest's feeder main is the oldest in the system. Water moving through a pipe loses pressure along the way, and the loss grows sharply with flow. On a hot afternoon the loss along an old, undersized main could drop pressure at the top of the zone while the tank is still comfortably full.

Both are drawable from supplied facts. Both would produce what is observed. They point at different repairs — a pump or a pipe — and at very different costs.

And nothing in the record so far distinguishes them.
That is worth pausing on, because it is the ordinary situation rather than a contrived one.
The complaints, the timing, the weather, the zone's history: every one of those facts sits comfortably with either mechanism, which is precisely why the question has stayed open for four chapters.

### Before reading further: write a number

Take about **six minutes**.

> **How likely is it that Mechanism A is the one operating?**

Write a number. A percentage, or odds, or "about two in three" — whatever form comes naturally.

Then write, in a sentence or two, the reasoning behind it.

Do this before reading on, and do it even if the request feels unreasonable — especially then.
Many capable readers will want to refuse on the grounds that there is not enough information to justify a number.
That instinct is the subject of §2 and it deserves a real answer rather than a brush-off, but the answer will land much harder if you have first felt the discomfort yourself.

Keep both the number and the reasoning.
You will come back to them in §2, and again at the very end of the chapter, and the comparison is more useful than any mark could be.

---

Most readers write a number.

Very few write down what the number is **conditional on** — what they are taking as known, what evidence they are using, and what the number would have been without it.

That omission is the subject of this chapter, and it is not a matter of neatness. It is the difference between a probability that means something and a probability that cannot be checked, argued with, updated, or scored.

## 2. A Probability Is Conditional on Something

### The claim

Here is the sentence this chapter is built on.

> **A probability is not a property of an event. It is a property of an event given stated information.**

Work it on the anchor.

Either the pump is the constraint at Hillcrest or the feeder main is. One of those is the case, out in the world, in the pipes, right now. It does not fluctuate, it does not depend on who is asking, and it has been settled since long before anybody wrote a report about it.

So when you wrote "about 60% for Mechanism A" six minutes ago, what were you describing?

Not the pipe. The pipe is not 60% anything.

You were describing **your evidential position** — what the information available to you supports. Somebody with the pump test results in hand would write a different number about the same unchanged pipe. Not because the pipe changed, but because they know more.

If that sounds familiar, it should.

Chapter 1 established that an answer is not adequate on its own but adequate for a stated use.
Chapter 3 established that a measurement is not valid on its own but valid for an interpretation.
Chapter 4 established that a dataset is not trustworthy on its own but trustworthy for a particular quantity.
Chapter 5 established that criticism is not sufficient on its own but sufficient relative to what happens if you are wrong.

Chapter 6 adds the sixth: **a probability is not high or low on its own; it is high or low given stated information.**

Five chapters have now taught the same structural lesson in five vocabularies, and this is the point at which it stops being a coincidence and starts being the thing the book is about.
The pattern is not a discovery about the world.
It is a discipline: whenever a quantity is offered as though it stood alone, the useful question is *relative to what*, and there is always an answer, and the answer is frequently the whole argument.

### Which dissolves an objection you may be holding

A great many capable people refuse to use probability on this kind of problem, and their reason is worth taking seriously rather than talking around.

> *You can't put a probability on a one-off event. Either the pump is the constraint or it isn't. There's no long run to average over. There's one Hillcrest.*

Every part of that is true, and the conclusion does not follow.

The objection assumes probability is a property of the event — that saying "60%" claims the world is 60% one way, and that this needs a sequence of trials to make sense of. On that reading the objection is correct.

But that is not what the number is doing. It describes what your information supports. And you certainly do have information: a network history, two candidate mechanisms, some physics, and a pipe of known age. There is no long run of Hillcrests, and there does not need to be, because the number was never a claim about a long run.

The test of whether this is a real quantity or a comfortable noise is whether it can be **wrong** in a way that shows. It can, and §6 is about exactly that.

### One distinction, named and set aside

There is a long-running argument about what probability fundamentally *is* — a limiting frequency in a sequence of trials, or a degree of belief that satisfies certain coherence requirements. It has occupied serious people for a century and is not settled.

**This book does not adjudicate it**, and does not need to.

Both readings are useful and the book uses both. A fair coin has a long-run frequency, and if you are asked about coins you should certainly use it. Mechanism A has no long run, and there the number describes an evidential position.

What unifies them is the framing above: in both cases the number is conditional on stated information. Where a relevant long-run frequency exists, it is usually the best thing to condition on. Where none exists, you condition on what you have and say what that is.

If you want the argument itself, it is in the philosophy of probability and it is genuinely interesting. It is not needed to do any of the work in this chapter.

### A note about notation

This book has gone five chapters without any.

That was deliberate, and it worked: representation, measurement, provenance, and criticism are all subjects where symbols would have added ceremony and subtracted clarity.

This chapter takes one small, closed exception, and it is worth saying why rather than slipping it past you.

The chapter's central distinction is between two things that sound almost identical in English — *the probability of A given B* and *the probability of B given A*. Said aloud, they are seven words apart and easy to conflate. Written with a bar, they are visibly different objects. That visibility is the whole reason for the exception.

So, from here:

> **`P(A | B)`** — read as *the probability of A, given B*.

And odds written as **`3 : 1`**, which §3 needs.

That is the complete list. No summation signs, no integrals, no distributions written as functions, no random variables as letters, and no Bayes formula with a denominator in it. If something in this chapter seems to want a symbol that is not on that list, it belongs to Chapter 8.

### Conditioning is not filtering

Here is the account most people carry, usually without having examined it.

*To find `P(A | B)`, take all the cases, throw away the ones where B does not hold, and see how often A holds in what remains.*

As arithmetic on a table, that is correct. As an account of the concept it fails, in two ways that matter.

**It has nothing to filter.** There is no collection of Hillcrests to throw cases out of. If conditioning is filtering, then conditioning on a unique event is not merely difficult but meaningless — which brings back the objection §2 just disposed of.

**It hides the direction.** This is the serious one. Filtering makes `P(A | B)` and `P(B | A)` look like the same operation done on the same table, and it offers no reason to expect them to differ. A reader who thinks in filters has no natural defence against confusing the two.

**A better account:** conditioning changes **what you are taking as given**.

That is a statement about your position, not about a subset of rows. It works for the coin and for Hillcrest. And it makes the direction obvious, because taking A as given and asking about B is plainly not the same act as taking B as given and asking about A.

### The inversion

This is the most consequential single error in the chapter, so it gets worked properly.

Take two statements about the anchor. The case supplies the numbers.

> `P(the pump test shows recovery | Mechanism A operates) = 0.85`

Under Mechanism A, running the pump harder should relieve the zone, so recovery is expected. That is a claim about what the test would do **if A were true**.

> `P(Mechanism A operates | the pump test shows recovery) = ?`

That is a completely different question. It asks what you should believe about the pipe **after seeing the test come out that way**.

They are not equal, and they are not close. The second depends on something the first does not contain at all: **how likely A was before the test.** If Mechanism A were vanishingly rare in networks like this one, a positive test would still leave it unlikely, however expected the test result is under A.

The first number is 0.85. The second, as §3 computes, is about 0.91 — and it is 0.91 only because the prior happened to favour A slightly. Change the prior and the second number moves while the first sits still.

**Reading the two aloud is not enough to keep them apart.** That is what the bar is for.

The asymmetry is easier to feel away from the case, on a pair where the answer is obvious.

> Most people who have influenza have a fever.
> Most people who have a fever have influenza.

The first is nearly true. The second is plainly false — fevers have many causes and influenza is only one of them. Yet the two sentences differ by moving four words, and in a meeting, spoken quickly, they sound like a restatement.

What separates them is the same thing that separates the two Hillcrest statements: **how common the condition was to begin with.** The first sentence does not depend on it. The second is almost entirely determined by it.

Which means the error has a signature. Whenever somebody moves from *this evidence is very expected under my hypothesis* to *my hypothesis is very probable*, they have silently dropped the prior, and the size of the mistake is exactly the size of the prior they dropped.

Whenever you meet a probability in someone else's work, it is worth one deliberate second: *given* which, about which? The number of professional arguments that turn out to rest on the two being swapped is not small, and they are hard to spot precisely because both parties are usually being sincere.

### Pause: why does filtering fail here?

Before reading on, write two or three sentences.

> Conditioning is often explained as filtering a dataset. Why does that explanation fail for Mechanism A?

If your answer is that there is no dataset, you have the first half.

The second half is the one worth having. Filtering describes an operation on cases; conditioning describes a **position you are reasoning from**. Those coincide when you happen to have many cases, which is why the filtering account survives for so long — it is right about the arithmetic in the situations where arithmetic is easy, and silent everywhere else.

### Task: restate your number

Find what you wrote in §1.

Rewrite it in this form:

> `P(Mechanism A | ______ ) = ______`

Fill the blank with everything you were actually taking as given. The zone's behaviour. The age of the main. What you know about pumps. Whatever it was.

Two things usually happen.

The blank is harder to fill than the number was — which tells you the number was doing less work than it appeared to.

And filling it changes the number, because writing down what you were conditioning on reveals that some of it was thinner than it felt.

## 3. Moving Between Positions: The Odds Update

Chapter 5 taught you to name the observation that would settle a question. It could not tell you **how far that observation would move you**, and without that, "we should run the test" is a preference rather than an argument.

This section supplies the arithmetic. It is one multiplication.

### Odds, in two sentences

Odds are a way of writing a probability as a comparison rather than a share.

**`3 : 1`** means three ways for and one against.
Four possibilities altogether, three of which are the thing, so a probability of `3/4`.

Going the other way, divide the probability by what is left over.
A probability of `0.6` gives `0.6 ÷ 0.4 = 1.5`, so **`1.5 : 1`**.

A few conversions, to make the two forms interchangeable in your head:

| Probability | Odds |
|---:|---:|
| 0.50 | 1 : 1 |
| 0.64 | about 1.75 : 1 |
| 0.75 | 3 : 1 |
| 0.90 | 9 : 1 |
| 0.91 | about 10 : 1 |

Two features are worth noticing now, because both matter later.

**Odds have no ceiling.** Probability is trapped between 0 and 1, so the difference between 0.90 and 0.99 looks small on the page. In odds it is the difference between 9 : 1 and 99 : 1 — a factor of eleven. Odds keep the strength of a belief visible at the extremes, where probability compresses it.

**Odds below 1 : 1 mean the other side is ahead.** Odds of `0.31 : 1` for A is the same statement as odds of about `3.2 : 1` for B. You will meet exactly that number in a moment, and it is not a different kind of result — just the same comparison read from the other end.

That is all the odds you need. They are used here because the update is a multiplication in odds and a mess in probabilities.

### The prior

Before the test, what should you believe?

The utility keeps a register of low-pressure investigations across its network. Restricted to **pumped zones** — which is the relevant population, since unpumped zones cannot have a pump problem — it records:

| Outcome of investigation | Count |
|---|---:|
| Pump-capacity limited | **7** |
| Main-related | **4** |
| **Total** | **11** |

So, conditional on the register and on nothing else:

> `P(Mechanism A | the register alone)` corresponds to odds of **7 : 4**, about **1.75 : 1**.

As a probability, `7/11 ≈ 0.64`.

**State the population every time you use this.** It is investigations in *pumped zones*, from a register covering eighteen years and three different network configurations. That is a real reference class and an imperfect one, and pretending otherwise would be exactly the kind of unstated conditioning §2 was about.

Three things about that reference class deserve saying out loud, because each of them would be invisible in the bare figure 7 : 4.

**The restriction to pumped zones is a judgment.** Unpumped zones cannot have a pump problem, so including them would drag the ratio toward the main and mean nothing. That reasoning is sound, and it is still a choice somebody made. Widen the class and the prior moves; narrow it to zones with feeder mains of Hillcrest's vintage and it moves again, probably by more. Nobody has computed those alternatives here, and the manuscript is not going to pretend they would come out the same.

**Eleven investigations is not many.** The prior is built on a count small enough that one reclassified case shifts it noticeably: 8 : 3 instead of 7 : 4 would take you from 1.75 to about 2.7. Chapter 4's discipline applies directly — this is a record with a provenance, and how an investigation came to be filed as *pump-limited* rather than *main-related* is a question nobody in this chapter has asked.

**Eighteen years and three configurations is a real span.** The network that produced the early entries is not the network Hillcrest sits in now. Whether those entries belong in the same population is exactly the kind of question Chapter 2 taught you to ask about what a representation includes, and the honest answer is that they are in the register because the register goes back that far.

None of this makes 7 : 4 unusable. It makes it a stated starting point with known weaknesses rather than a fact, which is the most any prior ever is, and the reason the arithmetic below always carries its conditioning along with it.

This number is a **base rate**, and §4 is about what people do with them.

### The two likelihoods

Now the test. Run the duty pump at elevated output through one hot afternoon and record pressure at the top of the zone. The threshold of interest is a recovery of more than **8 metres of head**.

The case supplies what to expect under each mechanism:

| | Recovery > 8 m | No recovery |
|---|---:|---:|
| If Mechanism A operates | **0.85** | 0.15 |
| If Mechanism B operates | **0.15** | 0.85 |

**These numbers were handed to you, and that matters.**

In real work, getting them is the hardest step in the entire procedure. They come from engineering judgment, from the register, from hydraulic reasoning about the specific main, and from somebody being willing to commit to a figure. A textbook that supplies them and moves on has quietly skipped the difficult part.

This one supplies them and says so. When you meet this in your own work, expect the numbers to be argued about, and expect the argument to be more informative than the arithmetic that follows.

### The ratio

Compare the two numbers in the first column.

`0.85 ÷ 0.15 ≈ 5.7`

Read that in words: **a recovery is about six times more expected if Mechanism A is operating than if Mechanism B is.**

That single number is the answer to Chapter 5's unanswerable question. It is how much the observation is worth.

### The update

Prior odds, times the ratio, gives posterior odds.

`1.75 × 5.7 ≈ 9.9`

So if the test shows recovery:

> `P(Mechanism A | register, and recovery > 8 m)` corresponds to odds of about **9.9 : 1**, or about **91%**.

From roughly two-to-one to roughly ten-to-one, on one afternoon's work.

### Why multiplying is the right thing to do

The step above is easy to perform and easy to distrust. Here is the same calculation without any rule at all, so you can see where the multiplication comes from.

Take the register at face value: of eleven investigations, **7** turned out pump-limited and **4** main-related.

Now ask what the test would have done in each of those eleven cases.

Of the **7** pump-limited ones, the supplied likelihood says about 85% would have shown recovery: `7 × 0.85 = 5.95`.

Of the **4** main-related ones, about 15% would have shown recovery anyway: `4 × 0.15 = 0.60`.

So among cases that show recovery, the pump-limited ones outnumber the main-related ones **5.95 to 0.60**, which is about **9.9 : 1** — the same answer, reached by counting rather than by applying anything.

As a probability: `5.95 ÷ (5.95 + 0.60) ≈ 0.91`.

Run the other branch the same way. Of the 7 pump-limited cases, `7 × 0.15 = 1.05` would show no recovery; of the 4 main-related, `4 × 0.85 = 3.40` would. That is **3.40 to 1.05**, about **3.2 : 1 for Mechanism B**, or `3.40 ÷ 4.45 ≈ 0.76`.

Notice what the multiplication is doing. Each side of the prior gets scaled by how well it explains what you saw. The side that explains it better survives the scaling in greater numbers, and the ratio between the survivors is your new belief. That is the entire content of the operation.

This is also why the prior cannot be dropped. The 5.95 came from the 7 as much as from the 0.85. Take away the register and there is nothing to scale.

### And the other branch

A test is only worth running if you know what you would conclude either way, so do the other one.

If the pump runs harder and pressure does **not** recover, the relevant numbers are the second column: `0.15` under A, `0.85` under B.

`0.15 ÷ 0.85 ≈ 0.18`

`1.75 × 0.18 ≈ 0.31`

Odds of `0.31 : 1` for A is the same as odds of about **3.2 : 1 for B**, or about **76%** for the feeder main.

### Why this is the point of the whole section

Put the two branches side by side.

| Result | Belief afterwards |
|---|---|
| Recovery > 8 m | about **91%** Mechanism A |
| No recovery | about **76%** Mechanism B |

You start at roughly 64% for A. After one afternoon you are at either 91% for A or 76% for B.

**The test is decisive in both directions.** That is what makes it worth doing, and it is a thing you can now say with a number rather than an intuition. Chapter 5 could tell you the test existed and was obtainable. It could not tell you this.

Note what would happen with a weaker test. If the two likelihoods were `0.55` and `0.45`, the ratio would be about `1.2`, and the update would take you from 1.75 to about 2.1 — from 64% to 68%. A day's work for four percentage points.

**A ratio near 1 means the observation moves nothing**, however interesting or expensive or scientific it sounds. That is worth knowing before you commission the work rather than after.

And a test can be decisive in one direction and useless in the other, which is a trap worth seeing once.

Imagine a different test — the numbers here are invented for the illustration and are not the case's — where a positive result is expected with probability `0.99` under A and `0.90` under B.

Positive result: `0.99 ÷ 0.90 = 1.1`. Your odds go from 1.75 to about 1.9. Nothing happened.

Negative result: `0.01 ÷ 0.10 = 0.1`. Your odds go from 1.75 to about `0.18 : 1`, which is roughly **5.7 : 1 for B**. A great deal happened.

That test is worth running, but only for the chance of the negative. If it comes back positive you have learned essentially nothing and spent the afternoon anyway — and if you had not worked both branches beforehand, you would very likely have reported the positive as confirmation.

**Work both branches before you commission anything.** Not to be thorough, but because the branch that would have told you nothing is the one you are most likely to get and least likely to recognise.

Whether an observation that *does* move belief is worth what it costs is a further question with real machinery behind it, and it is Chapter 11's.

### One thing this is not

A caution that has to be stated once, clearly, because the temptation is strong.

You have just updated your belief about which mechanism operates. You have **not** established what would happen if you changed the pump.

Those are different claims.
Conditioning on an observation tells you what to believe given that the world produced it.
It does not tell you what the world would do if you reached in and altered something; association alone does not establish an intervention effect, and causal conclusions require causal assumptions or design information that association by itself does not supply [@pearl2009causal].

The distinction survives the arithmetic being correct.
Every number in this section could be exactly right, and the conclusion *therefore replace the pump* would still be a further claim resting on further assumptions.

Chapter 7 is where that gap gets its proper treatment. For now: conditioning is not intervening, and this chapter never claims otherwise.

### Task: both branches

Using the register odds of **7 : 4** and the supplied likelihoods, work both branches yourself, on paper.

Then answer two questions.

1. Suppose the register had recorded **4** pump-limited and **7** main-related instead. What would the two posteriors be?
2. Suppose the likelihoods were `0.60` and `0.40` rather than `0.85` and `0.15`. Would you still spend the afternoon?

Question 1 shows you how much of the answer came from the prior. Question 2 is the one you will actually face.

## 4. Base Rates and Worthless Evidence

A reasonable objection to §3: why bother with the register at all? You have a test. Run it and read the answer.

This section is about why the prior is not a formality, and about a documented pattern in what people do with it.

### What a base rate is

A **base rate** is how often the outcome occurs in the relevant population.

Seven of eleven investigations in pumped zones were pump-limited. That is a base rate, and it is what set the prior in §3.

**The population is part of the number.** Seven-of-eleven *in pumped zones across eighteen years* is a different claim from seven-of-eleven *of all pressure complaints*, and using one where the other belongs is how base rates go wrong even when nobody neglects them.

### What people actually do

There is a well-known experimental result here, and it is worth having in its original form rather than as folklore.

Subjects were given brief personality descriptions of individuals said to be drawn at random from a group of 100 professionals. Some subjects were told the group was 70 engineers and 30 lawyers; others were told 30 engineers and 70 lawyers. They were asked, for each description, the probability that the person was an engineer.

The proportions should matter enormously. They did not:

> "In a sharp violation of Bayes' rule, the subjects in the two conditions produced essentially the same probability judgments." [@tversky1974judgment, p. 1124]

The explanation offered is **representativeness** — that "probabilities are evaluated by the degree to which A is representative of B, that is, by the degree to which A resembles B" [@tversky1974judgment, p. 1124]. A description that sounds like an engineer gets a high number regardless of how many engineers there were to draw from.

### The part that is usually left out

The result is often reported as *people neglect base rates*, which is easy to agree with and changes nothing.

The actual finding is sharper, and it comes with a condition:

> "Evidently, people respond differently when given no evidence and when given worthless evidence. When no specific evidence is given, prior probabilities are properly utilized; when worthless evidence is given, prior probabilities are ignored." [@tversky1974judgment, p. 1125]

Read that twice.

Given nothing, people use the base rate correctly. The failure is not ignorance and it is not innumeracy.

It is **triggered by receiving something that looks like information.** The experimenters demonstrated it by supplying a description written to be entirely uninformative about the question; subjects answered .5 regardless of whether the stated proportion was .7 or .3.

The description was worthless and it displaced a perfectly good base rate, because it arrived looking like evidence.

That should be uncomfortable for anyone who has spent five chapters learning to build representations, interrogate measurements, trace records, and criticize formulations. Every one of those produces something that looks like information.

And the professional versions of the experimenters' worthless description are not rare or exotic. They are the ordinary furniture of analytic work.

A dashboard that displays a metric prominently, without any indication of whether it distinguishes the options under consideration.
A site visit that produces vivid, accurate, first-hand impressions of a system, none of which bear on the question that prompted the visit.
A stakeholder interview full of true statements about a process, obtained at considerable effort, and consistent with every hypothesis on the table.
A well-built model whose output is detailed and plausible under either of the assumptions being compared.

Each of these arrives with everything the experimental description had: specificity, apparent relevance, and the costliness that makes it feel like it must be worth something. None of them is *false*. That was never the mechanism. The description in the experiment was not false either.

The trigger is being handed something that **looks like information about the question**, and the defence is not scepticism about the source. It is asking what the thing would have looked like if the other hypothesis were true.

### The anchor's version

Back to Hillcrest. The investigation is under way and your prior is `1.75 : 1` for Mechanism A.

Then a detail arrives. The customer who reported the low pressure adds:

> *It has been getting worse since the hot spell began.*

That feels like a clue. It is specific, it is recent, it is first-hand, and it points at heat — which is exactly what the whole problem is about.

Do the arithmetic. The case supplies:

| | Caller reports worsening with the hot spell |
|---|---:|
| If Mechanism A operates | **0.80** |
| If Mechanism B operates | **0.75** |

Ratio: `0.80 ÷ 0.75 ≈ 1.07`.

Update: `1.75 × 1.07 ≈ 1.87`.

From `1.75 : 1` to `1.87 : 1`. From about 64% to about 65%.

**Essentially nothing.**

And the honest report is stronger than that. The `0.80` and the `0.75` are engineering judgment, and no engineer alive could defend the difference between them against `0.78` and `0.77`. A ratio of 1.07 is well inside the width of the judgment that produced it.

So the correct thing to say is not *the report moved belief by one percentage point*. It is **the report moved belief by an amount this analysis cannot distinguish from zero** — which is a different sentence, and the one that should appear in the file.

### Pause: why did it move nothing?

Before reading on, write two or three sentences.

> The caller's report is true, relevant, and about the right system. Why did it barely move the number?

The answer is not that the report is worthless. It is genuinely informative about the *situation* — it tells you the problem is heat-related, which rules out plenty of things.

It is uninformative **for discriminating between these two mechanisms**, which is a different claim entirely.

Hot weather raises demand. Higher demand strains the pump, which is Mechanism A. Higher demand also raises flow through the main, increasing friction loss, which is Mechanism B. The observation is almost equally expected either way, so the ratio is near 1, so it moves nothing.

**Evidence is not informative in general. It is informative about a specific question.** A fact can be important, true, and completely useless for the comparison in front of you — and the ratio is what tells you which.

That reframes what §3's arithmetic is for. It is not mainly a way of computing posteriors. It is a way of finding out, before you spend anything, whether an observation discriminates.

### A check you can run in ten seconds

The full arithmetic needs two likelihoods, and in real work you often have neither.

You can still run the structure of it, and most of the value is in the structure.

When something arrives that feels like a clue, ask one question before you let it change anything:

> **Would I have been surprised to see this if the other explanation were the true one?**

If the answer is no — if the fact sits just as comfortably with the alternative — then whatever you were about to conclude, the fact is not the reason.

Apply it to the caller. Would you have been surprised to hear "it has been getting worse since the hot spell began" if the feeder main were the problem? No. Heat drives demand either way. So the report does not bear on the comparison, and you can know that without knowing 0.80 or 0.75.

The check is deliberately cheap because expensive checks do not get run. It will not give you a posterior. It will reliably tell you when you are about to update on nothing, which is the more common error and the more consequential one.

It is also the same move Chapter 5 asked for in a different vocabulary. A check that could not have come out the other way establishes nothing; a fact that would have appeared under either hypothesis discriminates nothing. One is about the test you designed, the other about the evidence you were handed, and both turn on imagining the world in which you are wrong.

### And the other direction

The same source records a second pattern that runs the opposite way, and having both is what makes the lesson usable.

**Sample size is under-weighted.** Asked whether a large hospital or a small one would record more days on which over 60% of babies born were boys, respondents split 21 for the larger, 21 for the smaller, and 53 for "about the same" [@tversky1974judgment, p. 1125]. The correct answer is the small hospital, because "a large sample is less likely to stray from 50 percent."

**Evidential impact is under-estimated.** In an urn problem where "the correct posterior odds are 8 to 1 for the 4:1 sample and 16 to 1 for the 12:8 sample", most people feel the smaller sample is stronger evidence [@tversky1974judgment, p. 1125]. The same page notes: "The underestimation of the impact of evidence has been observed repeatedly in problems of this type. It has been labeled 'conservatism.'"

So put the two findings together.

Worthless evidence **displaces** priors. Genuine evidence is **under-weighted**.

Both directions, in the same subjects, on the same page.

Which means the lesson is not "trust your priors more" or "update harder". It is that intuition does not track evidential weight reliably in either direction, and which way it fails depends on how the evidence is presented rather than on how much it is worth.

**That is the argument for doing the arithmetic.** Not because analysts are careless, but because the feeling of being moved by evidence is a poor guide to being moved by evidence, and a ratio is not.

### What this does not say

Two limits, both important.

**The heuristics are not defects.** The same source is explicit that they "are quite useful, but sometimes they lead to severe and systematic errors" [@tversky1974judgment, p. 1124]. You use representativeness constantly and it usually serves you well. A chapter that told you your intuition was broken would be misreporting the research and giving you nothing usable in its place.

**Nothing here says these tendencies can be trained away.** The results document what people do. Whether awareness fixes it is a separate question with a substantial and contested literature that this book has not read and will not summarise.

What this book claims is narrower and safer: **writing the numbers down is a way of not relying on the intuition.** That is a claim about a procedure, not about your mind.

## 5. Expectation, and What It Is Not

A short section about a word that does more damage than its difficulty warrants.

### What it is

The **expectation** of an uncertain quantity is its probability-weighted average: each possible value, multiplied by how likely it is, all added up.

It is a **summary of a distribution**. One number standing in for a spread.

Work one on the anchor. Starting storage is **9.9 ML**. Input runs at **8.4 ML per day** for seven days, so **58.8 ML** in. Expected demand over the week is **64.9 ML**.

`9.9 + 58.8 − 64.9 = 3.8 ML`

So the expected end-of-week storage is **3.8 ML**, against an operating reserve of **4.5 ML**.

That is a useful number. It compresses seven days of uncertain demand into something a person can hold, and it says the central case lands below the reserve.

One step in that calculation is worth making explicit, because it is doing quiet work.

The case puts a spread of ±**0.6 ML** on *each day's* demand. Seven days of uncertainty went into a single figure of 64.9 ML without any apparent effort. Why?

Because the spread is symmetric — equally likely anywhere in the range, so equally likely above the point forecast as below it — each day's expected demand is just its point forecast. And expectations add. Seven daily expectations sum to the weekly expectation, and the weekly expectation is the same 64.9 ML that Chapter 1 used.

**The spread vanished from the centre and did not vanish from the problem.** It is still there, in full, governing how far the actual week can land from 3.8 ML. The expectation simply does not carry that information, which is what makes it a summary and not a description.

### What it is not

**It is not what will happen.**

The clearest demonstration is the smallest. Roll a fair die: the expectation is `3.5`. The die has no face with 3.5 on it. The expectation is a value the quantity **cannot take**.

Nor is this a curiosity of dice. The expected number of people in a household is a figure like 2.4, and no household contains 2.4 people. The expected number of faults per kilometre of main is a decimal, and no kilometre has a fractional fault. In every case the number is a property of the distribution and not of any instance drawn from it.

Which is largely the fault of the English word. *Expected* suggests anticipation — the thing you should brace for. Nobody rolling a die anticipates 3.5.

This is the same hazard Chapter 3 met with `error`, where the technical term means a deviation from a reference value and the ordinary word means somebody blundered. A biased sensor is not a careless sensor, and an expected value is not a value anybody expects. In both cases the technical term is fixed, the ordinary word is not going away, and the only available defence is knowing that the collision is there.

Storage will end the week at some particular number. It will not end at 3.8 except by coincidence. The 3.8 is the centre of a spread, and the spread is where the decision-relevant information lives.

**It is not the most likely outcome.** For a symmetric spread the two coincide, which is exactly why people stop distinguishing them. For a skewed one they can be far apart — and the quantities analysts care about are frequently skewed, because there is often a floor and no ceiling, or the reverse.

**It is not the median.** Half the outcomes fall on either side of the median. The expectation has no such property.

### And it is not a decision

This is where the real damage is done, and it is done by a slide so smooth that nobody announces it.

> *The expected end-of-week storage is 3.8 ML.*
> *Therefore we should plan as though storage will be 3.8 ML.*

The first sentence is arithmetic. The second is a **decision rule**, and a specific one: it treats a 50-50 chance of 6 ML or 1.6 ML as equivalent to a certainty of 3.8 ML.

For a utility deciding about drought response, those are obviously not equivalent. Running out has consequences that are not the mirror image of having spare.

Acting on the expected value is a legitimate thing to do, it has a name, and there are conditions under which it is exactly right. But it is a **choice**, and the slide above makes it without anyone noticing that a choice occurred.

Chapter 11 is where that choice gets made deliberately — expected utility, risk attitude, and what to do when the consequences of being wrong are not symmetric. Chapter 6 stops at the summary.

In practice the slide rarely appears as two sentences with a *therefore* between them. It appears as a single sentence with the word *expected* quietly deleted.

> *The model projects end-of-week storage at 3.8 ML, against a reserve of 4.5.*

Nothing in that sentence is false, and nobody reading it will supply the missing spread. What they will take away is a shortfall of 0.7 ML — a manageable-sounding gap, close enough to call it tight and move on. The sentence has converted a distribution into a near-miss without anyone deciding to.

The repair is not to add a caveat. It is to report a different quantity altogether — and the task below asks you to name it before this chapter does.

The habit to build now: whenever you see *the expected value is X, so...*, look at what follows the *so*. If it is a decision, something was assumed that has not been stated. And when the *so* has been deleted entirely, as in the sentence above, the assumption is still there — just harder to argue with.

### Task

For the anchor's expected end-of-week storage of **3.8 ML** against a reserve of **4.5 ML**:

1. Write one sentence saying what 3.8 means, without using the words *will be*.
2. What further quantity would you actually want, in order to decide whether to act?

Your answer to 2 is a probability, not an expectation — and §7 is about how to get it.

## 6. Being Scored

You have now been asked to commit to numbers. This section is about what stops those numbers being convenient ones.

### The reader's real objection

It is not *how do I compute a score*. It is this:

> Why would I ever write down a number that can be held against me later?

A vague statement cannot be wrong. "There's a significant risk to Hillcrest" survives any outcome. "About a 70% chance the reserve is breached" does not, and the person who says it has taken on an exposure that the person who says "significant risk" has avoided.

That is a real asymmetry and it is why organisations drift toward vagueness. The answer is not exhortation.

### Propriety

There is a class of scoring rules built so that stating what you actually believe is the score-maximising strategy.

> "The forecaster has no incentive to predict any P ≠ Q and is encouraged to quote his or her true belief". [@gneiting2007scoring, p. 359]

A rule with that property is called **proper**.

Sit with what it means. Under such a rule you cannot improve your expected score by hedging toward the middle to avoid embarrassment, and you cannot improve it by exaggerating toward the extremes to look decisive. Both distortions cost you. **Honesty is optimal by construction**, not by professional virtue.

That is the answer to the objection. A proper scoring rule does not ask you to be brave. It removes the payoff from being anything else.

The stated purpose is exactly this: "the role of scoring rules is to encourage the assessor to make careful assessments and to be honest" [@gneiting2007scoring, p. 359].

### And improper rules are common

This is not a technicality about which rule to prefer.

The same source warns of "the potential issues that result from the use of intuitively appealing but improper scoring rules" [@gneiting2007scoring, pp. 359–360].

**Intuitively appealing but improper** is the phrase to carry. Scoring schemes that organisations invent — count how often the most likely outcome happened; penalise every forecast that turned out wrong; reward confidence — are frequently improper, and an improper rule pays people to distort.

It is worth seeing one distortion concretely, because the abstraction is easy to nod along to and hard to recognise in a meeting.

Suppose a utility scores its briefings by **hit rate**: how often the outcome the briefing called more likely actually occurred. It sounds unimpeachable. It is the scheme most organisations would arrive at unprompted.

Now consider what maximises it. The reserve is breached 45% of the time overall, so *not breached* is the more common outcome. A forecaster who says **not breached** in every single briefing scores 55% and cannot be beaten by anyone who occasionally calls a breach and is occasionally wrong about it. Under this rule, the way to score well is to stop distinguishing between briefings entirely.

Worse, the rule cannot tell 51% apart from 99%. Both round to the same call, so a forecaster gains nothing from expressing how confident they are and loses nothing by concealing it. The scheme has quietly removed probability from the exercise while appearing to measure forecasting skill.

That is what improper looks like from the inside: not a subtle mathematical defect, but a scheme under which the honest, informative forecaster is outscored by somebody who has stopped forecasting.

Which rules are proper, and why, is mathematics this book does not teach. What you need is the awareness that a scoring scheme somebody invented over lunch may be actively rewarding dishonesty, that the reward is often invisible to everyone involved, and that this is a known and studied failure rather than a cynical guess.

The idea of scoring probability forecasts dates at least to Brier in 1950, as reported at [@gneiting2007scoring, p. 360]. That paper was not obtainable for this book, so nothing here describes its contents.

### Calibration

Now the property most people mean when they ask whether a forecaster is any good.

> "Calibration refers to the statistical consistency between the distributional forecasts and the observations, and is a joint property of the forecasts and the events or values that materialize." [@gneiting2007scoring, p. 359]

**A joint property.** You cannot assess it from the forecasts alone; you need what happened. When you say 70% and it happens about 70% of the time, you are calibrated.

**A word that is doing double duty.** Chapter 3 used `calibration` for instruments — comparing a device against a reference standard to find a systematic offset — and explicitly set this second sense aside, warning that it was a different concept sharing the word.

Here is that second sense, and the word is now available.

The two are genuinely different. Chapter 3's calibration applies to a device and is assessed against a standard. This one applies to a forecaster or a forecasting procedure and is assessed against a record of outcomes. Chapter 3's fixes an offset in readings; this one fixes overconfidence or underconfidence in stated probabilities.

They are related only by analogy — both compare what something says against what is so. Do not carry conclusions from one to the other.

### The utility's record

The utility has issued a probabilistic statement in each of 40 past heat-event briefings: the chance that usable storage falls below the operating reserve during the event.

Here is the record, grouped by what was said.

| Stated | Briefings | Reserve breached | Observed |
|---:|---:|---:|---:|
| 90% | 10 | 5 | **50%** |
| 70% | 10 | 5 | **50%** |
| 50% | 10 | 5 | **50%** |
| 30% | 10 | 3 | **30%** |

Read the last column against the first.

At 50% and 30% the utility is well calibrated — it says 50 and gets 50, says 30 and gets 30.

At 70% and 90% it is badly overconfident. Both bins delivered 50%. When these forecasters say they are nearly certain, they are right about half the time.

To see the size of the gap, add what calibration would have required.

| Stated | Briefings | Breached | Observed | Calibration would need |
|---:|---:|---:|---:|---:|
| 90% | 10 | 5 | **50%** | about 9 |
| 70% | 10 | 5 | **50%** | about 7 |
| 50% | 10 | 5 | **50%** | about 5 ✓ |
| 30% | 10 | 3 | **30%** | about 3 ✓ |

The 90% bin is short by four events out of ten. That is not a rounding matter or a small-sample wobble to shrug at; it is the difference between *near-certain* and *a coin*.

**And the pattern is specific and actionable.** It is not "the utility forecasts poorly". It is "the utility's high-confidence statements should be discounted toward the middle, and its moderate ones can be taken at face value." Somebody receiving these briefings could act on that tomorrow, with no cooperation from the forecasters and no change to how the briefings are produced.

It also has a plausible reading, which is worth stating because it stops the finding sounding like an accusation. Overconfidence at the top of the scale is among the most commonly reported patterns in forecasting of all kinds. A forecaster who has decided the situation is serious reaches for 90% as a way of saying *take this seriously*, and the number stops being a probability and becomes an emphasis marker. Nobody is being dishonest. The scale is being used for something other than what it measures.

Two cautions before anyone acts on the table.

**Forty is not many.** Ten briefings per bin means the 90% row rests on ten events. A gap of four is large enough to take seriously and the record is thin enough that the exact size of it should not be quoted to the percentage point.

**The bins are the utility's own stated numbers**, so this is a record of what the utility said, not of the situations it faced. If briefings in the 90% bin were systematically the hardest cases, that would show up here as overconfidence too. Nothing in the record distinguishes those explanations — which is a Chapter 4 point about what a set of records can and cannot support, arriving in a new setting.

And notice that none of it is visible from any single briefing. It took forty.

### Pause: the 45% forecaster

Before reading on.

> Across all 40 briefings, the reserve was breached 18 times — an overall base rate of **45%**.
>
> Suppose a forecaster had simply said "45%" in every single briefing. How would they score on calibration? And would you want them?

They would be **perfectly calibrated**. Say 45%, breach 45% of the time. Better calibrated than the utility, which is overconfident in two of its four bins.

And they would be **completely useless**. They have told you nothing about any particular heatwave. Their forecast for a mild three-day warm spell is identical to their forecast for a record-breaking fortnight.

### Which is why calibration is not the goal

There is a second property, and the pair is what you actually want.

> "Sharpness refers to the concentration of the predictive distributions and is a property of the forecasts only." [@gneiting2007scoring, p. 359]

**Sharpness** is how far from the middle you are willing to go — how concentrated, how committed. Unlike calibration, it is a property of the forecasts alone, so you can assess it before anything happens.

The always-45% forecaster has perfect calibration and no sharpness whatever.

The goal is stated precisely:

> "the goal of probabilistic forecasting is to maximize the sharpness of the predictive distributions subject to calibration." [@gneiting2007scoring, p. 359]

Calibration is the **constraint**. Sharpness is the **objective**. Not the reverse, and not either alone.

Which gives you a clean way to read a forecasting record. Being right on average is the floor, not the achievement. The achievement is being informative *while* being right on average — and a forecaster who is sharp and badly calibrated is worse than useless, because they are confidently misleading.

### Why one forecast cannot be scored

A consequence that follows directly, and that overturns how most people talk about forecasts.

You said 70%, and the thing happened. Were you right?

**Neither right nor wrong.** A single outcome is consistent with any probability strictly between 0 and 1. Something you called 70% happening is exactly what should occur about seven times in ten; something you called 30% happening is exactly what should occur about three times in ten. One instance of either tells you almost nothing.

This follows from the definition. Calibration is consistency between forecasts and observations **across a record**. One pair is not a record.

And the practical consequence is uncomfortable.

An organisation that issues one probabilistic statement per drought, and never revisits it, has built something that **cannot be wrong**. Not because the statement was carefully hedged, but because there is no accumulation against which it could ever be assessed.

You met that standard in Chapter 5: a check that could not have failed establishes nothing. A forecast nobody scores is the same object. It has the appearance of a commitment and none of the exposure.

**The remedy is not better forecasts. It is a record.**

And the record is a smaller thing than people fear. Five fields, one row per forecast:

- the **date**;
- the **statement** — what event, precisely enough that somebody else could later judge whether it happened;
- the **number**;
- **what you were conditioning on**, in a sentence;
- and, later, **what happened**.

The fourth field is the one that gets dropped, and dropping it is what makes a record uninterpretable two years on. A row reading *12 March, breach, 70%* cannot be learned from, because you no longer know whether the 70% was issued before or after the weather update arrived.

The fifth is the one that requires an actual commitment, because somebody has to go back. A forecast log nobody closes out is a slightly more organised way of not being scored.

Forty rows is enough to see a pattern that no individual row contains. Ten is not nothing. Zero is where most organisations are, including ones with sophisticated modelling functions, and the gap between zero and ten is by far the largest improvement available in this chapter.

### Task: read the record

Using the table above:

1. State the calibration pattern in one sentence a decision-maker could act on.
2. The next briefing says **90%**. What should the recipient do with that number?
3. What would you need in order to tell whether the utility's forecasts have improved since?

Question 3 is the one that changes practice. The answer is another forty rows, and the only way to have them in a year is to start recording now.

## 7. Simulation: Consequences of Assumptions

§5 ended with a question the chapter had not yet answered: you want a probability, not an expectation. This section is about the workhorse for getting one.

### What a simulation does

Run the calculation many times. Each time, draw the uncertain inputs from stated ranges rather than fixing them. Collect the answers and look at the spread.

For the anchor: instead of using the point forecast of **64.9 ML** for the week, put a spread on each day's demand, run the seven-day storage projection a few thousand times, and count how often the end-of-week figure falls below **4.5 ML**.

That count, divided by the number of runs, is the probability §5 asked for. It is a genuinely useful thing that no amount of staring at the arithmetic will produce, because seven uncertain quantities interacting with a threshold is past what anybody can do in their head.

### Doing it

The setup is Chapter 1's, with one change. The seven daily central forecasts are **9.0, 9.3, 9.6, 9.5, 9.4, 9.2, 8.9 ML**. Instead of taking each as given, draw it anywhere within ±**0.6 ML** of that figure, treating every point in the range as equally likely, and draw the seven days independently.

For each draw, run the same projection Chapter 1 ran:

`9.9 + 58.8 − (that week's demand)`

and record whether the result falls below 4.5.

The threshold is worth writing down, because it makes the whole exercise legible: storage ends below the reserve exactly when weekly demand comes in above `9.9 + 58.8 − 4.5 = `**`64.2 ML`**.

That is **0.7 ML below the central forecast of 64.9**. The week does not have to go badly for the reserve to be breached. It has to go slightly better than forecast to avoid it.

Run it and the answer comes out at about **77%**.

Set that against §5's summary. The expectation said 3.8 ML against a reserve of 4.5 — a shortfall of 0.7, the kind of figure a briefing calls *tight*. The probability says the reserve is breached in roughly three weeks out of four. Both describe the same seven days and the same assumptions. Only the second is a quantity anybody can act on.

That is what a simulation is for.

### And what it does not do

> **A simulation computes the consequences of assumptions. It does not produce evidence about the world.**

Everything a simulation tells you was already implied by what you put in. The machine worked out something you could not work out unaided — which is a real service — but it observed nothing.

The case supplies a spread of **±0.6 ML** on each day's demand, treated as equally likely anywhere in that range.

Where did ±0.6 come from?

**Nowhere.** It was supplied, and this chapter's case data says so explicitly. It is not derived from forecast error records, not fitted to anything, and not defended.

Run the projection ten thousand times against that spread and you will get a stable, precise, entirely confident probability — of an assumption nobody has justified.

### More runs

Which brings the section to its point.

**More runs reduce Monte Carlo error. They do nothing about model error.**

Repeat the whole exercise several times at each run count and watch what happens.

| Runs | Answers across repeated runs |
|---:|---|
| 100 | 72% – 80% |
| 1,000 | 76% – 79% |
| 10,000 | 76.7% – 77.9% |
| 1,000,000 | 77.3% |

At a hundred runs the answer is not stable enough to quote. At ten thousand it is stable to about a percentage point. At a million it has effectively stopped moving.

That shrinking spread is **Monte Carlo error** — the wobble that comes from having sampled rather than enumerated. It is a property of how long you ran the machine, it goes away if you run it longer, and it is the only kind of error more runs can touch.

What does not change, at any run count:

- the ±0.6 spread is still unjustified;
- the demand forecast underneath it was conditional on **no new action** (Chapter 1), and a conservation request would break that;
- one of its zone components is a subtraction residual containing leakage in other zones and water the utility used itself (Chapter 4);
- the storage model still has no spill term, so it grows water without limit under low demand (Chapter 5).

The simulation will report all of that with great stability. The stability is about the arithmetic, not about the world.

Which is why the 77% cannot be written down bare. This chapter has asked, since §2, that every probability carry what it is conditional on, and here is the bill for that:

> `P(reserve breached this week | the Chapter 1 no-new-action forecast, the supplied ±0.6 ML spread, and the storage model as it stands)` ≈ **0.77**

Long, and every clause is load-bearing. Drop the first and the number silently assumes nobody issues a conservation request. Drop the second and an unjustified spread has been promoted to a fact. Drop the third and a model that grows water without limit is presented as a description of the reservoir.

A briefing that says *there is a 77% chance of breaching the reserve* has not simplified that sentence. It has deleted the three things a reader would need in order to disagree with it.

**Report the run count too.** It is the one piece of the sentence that is genuinely about the arithmetic rather than the world, and stating it tells the reader which part of the uncertainty you have measured — which, as this section has spent its length arguing, is the smaller part.

### A shape you have now met three times

This should be starting to feel familiar.

| Chapter | More of this improves | And does nothing for |
|---|---|---|
| 3 | measurements | precision — but not **trueness** |
| 4 | records | sampling variability — but not the **data-quality term** |
| 6 | simulation runs | Monte Carlo error — but not **model error** |

Three different fields, three different vocabularies, one structure: there is a quantity that effort reduces, and a quantity that effort does not touch, and the second is usually the one that decides your answer.

By the third instance this is worth converting into a habit rather than a fact:

> **When told that more of something will fix a problem, ask which term it enters.**

Chapter 5's version of the same point was that sensitivity analysis cannot see the formulation, because it varies inputs *inside* a formulation. A simulation has exactly the same limit for exactly the same reason: it explores what your assumptions imply and can never step outside them.

### What simulation is genuinely good for

Having spent the section on limits, the positive case deserves stating, because it is strong.

**Combining several uncertainties.** Seven days of demand, an inflow, a threshold, and possibly a pump failure — the interactions are past hand calculation and simulation handles them without a formula.

**Getting a probability rather than a centre.** §5's expectation of 3.8 ML tells you the middle. A simulation tells you the chance of breaching, which is the decision-relevant quantity.

**Finding out what your assumptions actually imply.** This is the underrated one. People are frequently surprised by what their own stated assumptions produce, and the surprise is informative — it usually means an assumption was less innocent than it looked.

**Testing structure cheaply.** Run it with the spill term and without. Run it with the pump failing on day three. Each run is a question about what the model contains, answered in seconds — which is a Chapter 5 activity conducted by machine.

That last one is the honest reconciliation. Simulation cannot criticize your formulation. It can execute the criticisms you have already thought of, faster than you could by hand.

### Task: diagnose five defects

Each statement below contains one defect. Write the defect, what it stops you concluding, and a repair.

1. *"There is a 70% chance the pump is the cause."*
2. *"We said 80% and it happened, so the forecast was good."*
3. *"The pump test came back positive, so it is probably Mechanism A."*
4. *"We ran 50,000 simulations, so the estimate is reliable."*
5. *"You cannot put a number on a one-off event like this."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

## 8. Cold-Start Practice and Retrieval

### Return to your six-minute number

Find what you wrote at the start of §1.

Read it against what you can now produce. Do not score it.

- Did you write **what the number was conditional on**?
- Did you use a **base rate**, and did you say what population it came from?
- Could you have said **how far a new observation would move it**?

Two patterns are common in the opening attempt.

Some readers write a confident number with no conditioning at all — "about 70%" — which by §2's standard is not yet a probability, because there is no stated position it is a probability from.

Others write no number, on the grounds that there is not enough information. That instinct is honourable and it is the one §2 was aimed at: there is never enough information, the number describes your evidential position rather than the pipe, and refusing to state one does not make the underlying uncertainty go away — it just makes it unexaminable.

### Independent transfer

Now work an unfamiliar situation, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below. Open only that one.

- [Form A — A fleet operator's intermittent vehicle fault](transfer-form-a.md)
- [Form B — A housing team and a rise in reported damp](transfer-form-b.md)

Allow about **45 minutes**.
Every fact you need is supplied. Do not look anything up.

Do not open the other form. You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the procedure from memory

Before looking back, write down how you would update a belief when an observation arrives.

Aim for the sequence, not the wording.

For reference, after you have tried:

1. What are the two candidate explanations?
2. What is my prior, and **what population does it come from**?
3. Write it as odds.
4. How expected is this observation **if the first is true**?
5. How expected is it **if the second is true**?
6. Divide the two. That ratio is what the observation is worth.
7. Multiply the prior odds by the ratio.
8. State the result **with its conditioning information**.
9. Would the other outcome have moved me too? If not, the observation was not worth making.
10. Am I going to record this and check it later?

Step 2 is the one people skip, and skipping it is how a base rate becomes a number from the wrong population.

Step 9 is the one worth having before you commission anything.

Step 10 is the one nobody does, and it is the only one that makes any of the rest checkable.

### If the transfer went badly

- **You stated probabilities with no conditioning.** Reread §2. A number without its conditioning is not yet an answer.
- **You updated on everything.** At least one supplied detail had a ratio near 1. If your posterior moved for every fact you were given, you were not computing ratios.
- **You inverted a conditional.** Check whether you used *how expected the observation is under the hypothesis* or *how likely the hypothesis is given the observation*. They are different numbers and only the first is supplied.
- **You ignored the base rate once the evidence arrived.** That is the documented pattern from §4, and recognising it in your own work is the point of having read it.
- **You could not assess the record.** Group the forecasts by what was said, then compare each group against how often it happened. The pattern is in the grouping, not in any row.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Do not reread this chapter immediately beforehand, and do not look at the form you have not done.

### What this chapter did not give you

Worth being explicit about, so that nothing here is mistaken for more than it is.

**Where likelihoods come from.** The `0.85` and the `0.15` were handed over, and §3 said so at the time. Producing such numbers, defending them, and revising them is the hardest part of the whole procedure and this chapter did not teach it.

**Estimation and intervals.** Every probability here was either supplied or counted. How to estimate a quantity from data, and how to attach an interval to it, is a different subject and a later one.

**Whether an informative observation is worth its cost.** §3 could tell you the pump test moves belief a long way. It could not tell you whether that is worth an afternoon, because that comparison needs consequences and Chapter 11 has them.

**Any claim about fixing your intuition.** §4 documented two failure directions and stopped. Whether knowing about them helps is a question this book has not investigated and will not pronounce on.

**And nothing about intervention.** Which is the next chapter's whole subject.

### What Chapter 7 asks next

You can now hold uncertainty as a stated quantity, move it when evidence arrives, and be scored on the result.

And §3 flagged a limit that this chapter deliberately did not develop.

Updating your belief about which mechanism operates is not the same as establishing what would happen **if you changed the pump**. Conditioning tells you what to believe given that the world produced an observation. It says nothing about what the world would do if you reached in and altered it.

That gap does not close with more data, better priors, or sharper forecasts. No amount of conditioning turns an association into an intervention.

Chapter 7 is about what would have to be true for evidence to establish a causal claim — what the target of such a claim even is, and what designs and assumptions can get you there.
