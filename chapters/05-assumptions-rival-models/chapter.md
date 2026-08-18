---
chapter: 5
part: 1
title: "Assumptions, Adequacy, and Rival Models"
status: drafted
---

# Chapter 5: Assumptions, Adequacy, and Rival Models

## 1. What Would Have Shown It

Four chapters, four failures, and one thing in common.

**Chapter 1.** The dashboard read **10.8 ML** and the tank held **9.9**. What would have shown it: an independent check using a different observation path. Somebody made that one.

**Chapter 2.** The single-tank representation said the town had nine days of margin. It could not express who lost service first, and Hillcrest had about sixteen hours. What would have shown it: dividing the zone's storage by the zone's draw. Nobody did.

**Chapter 3.** The monitoring point read **25 metres** of head at the evening peak and the top of the zone read **3**. What would have shown it: one person with a portable gauge, on one hot evening, at the top of the hill. Nobody did.

**Chapter 4.** The Hillcrest demand figure was a subtraction residual containing leakage in other zones, water the utility used itself, and the amount by which two meters elsewhere read low. What would have shown it: asking where the number came from. Nobody did.

Each was found by a different chapter's machinery. Representation caught the second, measurement the third, provenance the fourth.

And in each case there was something specific that would have revealed the problem — cheap, obvious in hindsight, and never done, because nobody had a way of going looking.

### Before reading further: what would have to be true?

Take about **seven minutes**.

Part I ends with a conclusion about Hillcrest: it is the zone at risk, it has roughly sixteen to twenty hours of endurance without its pump, and the utility's response options are conservation, production increase, and restriction.

Write a list: **what would have to be true for that to be right?**

Be as specific as you can. Do not write "the data would have to be accurate."

Keep the list. You will come back to it.

---

This chapter introduces no new case.

Every other chapter in Part I added something — a representation, a construct, a dataset. This one turns entirely on what is already in front of you, because its subject is not another way analyses go wrong. It is what to do about the four you have already met.

> How could this formulation fail its purpose, and what would show it?

The second half of that question is what makes the chapter more than a list of things to fear. Anyone can produce doubts. The skill is producing a doubt with an observation attached — something that could come back and settle it.

### Why this is the hardest of the five

Each of the previous four chapters taught something with a natural shape: a representation gets built, a number gets interrogated, a dataset gets traced. You know when you have done it, because there is an artifact.

Criticism has no natural shape and no natural end.

You can always think of another thing that might be wrong. There is no point at which the list is complete, no signal that you have done enough, and no artifact that announces itself as finished. Which produces the two failure modes this chapter has to defeat, and they are opposites.

**The first is doing none of it.** Criticism that has no stopping rule is criticism nobody starts, because starting means opening something that cannot be closed before the deadline. So it gets replaced with a limitations paragraph, written last, in five minutes.

**The second is doing an unbounded amount of it** — endlessly qualifying, endlessly caveating, and never producing a usable answer. This looks like rigour and functions as paralysis.

Both failures come from the same missing piece: nothing tells you how much is enough.

So this chapter starts there, in §2, before any technique. The techniques are useless without a stopping rule, and the stopping rule turns out to be the same shape as everything else in Part I.

## 2. Adequate for What, at What Risk

### The question with no answer

Start with the question a colleague will actually ask you.

> Is this analysis any good?

By now you should distrust the shape of that. Chapter 1 said adequacy is relative to a stated use. Chapter 3 said validity belongs to an interpretation. Chapter 4 said trustworthiness attaches to a quantity, not a dataset.

The pattern holds here too, and this is where the word from Chapter 1 finally gets its full form.

A model or an analysis is not adequate in itself. It is **adequate for a stated use, at a stated accuracy, for a stated quantity.**

The reliability literature says this precisely. Validation is treated as meaningful "for specified quantities of interest" and in relation to "the accuracy required for an intended use" [@nrc2012reliability, Summary p. 3].

Read that last phrase twice: *the accuracy required for an intended use*. Accuracy has no threshold of its own. The threshold arrives with the use.

### Adequacy is not accuracy

These are routinely merged, and separating them is the most useful thing in this section.

Regulatory guidance on computational models draws the line explicitly, distinguishing **quantifiable model accuracy** from the broader judgment of whether the **total credibility evidence is sufficient** for the context of use, given model risk [@fda2023credibility, §VI.D p. 33].

Three things there, not one:

- how accurate the model is — a quantity you might measure;
- whether the evidence you have assembled is enough — a judgment;
- what governs that judgment — the use, and what is at stake.

A model can be accurate and inadequate: precise about the wrong quantity, or precise with no evidence that it applies here. A model can also be rough and adequate, if the stakes are low and the roughness cannot change the decision.

### Work it on Part I

The analysis you have been building is adequate for a specific thing.

**Adequate for:** deciding whether to request voluntary conservation during a seven-day heatwave, at day-level resolution, for total system storage.

That is not a small achievement. For that question it used the right quantity, at a defensible grain, from records good enough for the purpose.

**Not adequate for:**

- deciding which zone to restrict first — Chapter 2 established this;
- reporting service performance — Chapter 3 established this;
- anything requiring a trustworthy Hillcrest demand figure — Chapter 4 established this;
- sizing a pump or planning capital works, which nobody in Part I attempted.

Notice that "not adequate" is doing no work as a general verdict. Four different inadequacies, four different reasons, one artifact.

### What governs how much criticism is enough

Here is the question this section exists to answer, because "criticize your model" is useless advice without it.

**How much is enough depends on what happens if you are wrong.**

The same guidance conditions sufficiency on the context of use *given model risk* [@fda2023credibility, §VI.D p. 33]. The reliability literature connects the nature and allocation of verification, validation, and uncertainty work to how results will be used in an eventual application and decision [@nrc2012reliability, ch. 6, §§6.1–6.2, pp. 86–87].

So there is no fixed standard, and looking for one is a category error.

For the utility: if the analysis is wrong, a pressure zone falls below its operating threshold during a hot evening, and households at the top of the zone see low pressure until the tank refills overnight.

That is a genuine service consequence. It is a service consequence — not an irreversible one, not a safety event, and recoverable by the following morning.

Which bounds the criticism this analysis deserves. More than a routine monthly report. Considerably less than a decision that cannot be undone.

Being explicit about that is not a way of excusing shallow work. It is what stops criticism becoming infinite — and criticism that has no stopping rule does not get done at all.

### And the pattern completes

You have now met the same structural move in every chapter of Part I.

| Chapter | What is not self-standing | What it is relative to |
|---|---|---|
| 1 | whether an answer is adequate | the stated intended use |
| 2 | what belongs in a representation | the purpose |
| 3 | whether a measurement is valid | the interpretation placed on the scores |
| 4 | whether a dataset is trustworthy | the quantity being estimated |
| 5 | **how much criticism is enough** | **what happens if you are wrong** |

Each row is independently established, in a different literature, by people who were not coordinating.

That they share a shape is this book's observation, not a finding — and it is offered as a working habit rather than a theory. When something is presented as a property of an object, check whether it is a property of a relation between that object and a purpose.

### Two questions, not one

One distinction before leaving this section, because it costs a sentence and prevents a common confusion.

> **Verification:** did I do the thing right?
> **Validation:** did I do the right thing?

The engineering literature separates these carefully, along with uncertainty quantification and the broader credibility judgment, and warns against merging them [@asme2025credibility, slides 5–7].

The reason to hold them apart is that they fail independently. A flawless computation of the wrong model is wrong. A correct model computed badly is also wrong. Checking one tells you nothing about the other.

Chapter 2's endurance arithmetic was verified — `0.6 ÷ 0.9` is correct. Chapter 4 showed it was not validated: the 0.9 was not a demand.

**A note about the word `validation`.** Chapter 3 refused to use it, because measurement validation and computational-model validation are different practices that share a word, and merging them causes real confusion.

This chapter is where the second sense properly belongs, so the word becomes available — and the rule has changed, which you are owed an explanation for rather than being expected not to notice. When this chapter says *validation*, it means the model sense: did we build the right model for this use. Chapter 3's sense, assessing evidence for an interpretation of scores, is a different activity and this chapter does not use the word for it.

**One limit on all of this.** The frameworks quoted above are written for computational modelling and simulation in regulated engineering and medical-device settings, with apparatus — credibility factors, evidence tables, submission requirements — that presupposes an institutional context most readers do not work in. What transfers is the structure of the judgment. The machinery does not, and this book does not teach it.

### Writing it down

An adequacy statement is a short artifact and almost nobody produces one, which is why analyses circulate with no attached account of what they are for.

Four lines will do.

> **Built for:** deciding whether to request voluntary conservation during a seven-day heatwave.
> **At:** day-level resolution, for total system storage.
> **Not built for:** deciding which zone to restrict; reporting service performance; anything requiring a trustworthy Hillcrest demand figure; sizing plant.
> **If wrong:** a zone falls below its operating threshold on a hot evening and recovers overnight.

Put that at the top of the analysis rather than the bottom.

The third line is the one that does the most work, and it is the one people leave out because it feels like advertising weakness. It is the opposite. A reader who knows what an analysis is not for cannot misuse it, and every one of Part I's failures involved a number being used for something it was never built for — the dashboard reading, the aggregate, the monitoring point, the residual.

The fourth line is what makes the rest of this chapter finite.

### Task: state the adequacy

In two or three sentences, for the Part I analysis:

1. What is it adequate for — use, accuracy, quantity?
2. What happens if it is wrong?
3. Given that, does it deserve more criticism than it has had?

Question 3 has an answer, and the rest of the chapter is what to do about it.

## 3. Four Cheap Checks

This is the most useful section in the chapter, and it is worth saying why before starting.

The four checks below need no data you do not already have. They take minutes. Between them, run on the analysis you have just spent four chapters building, they will catch two of the four things Part I found — one of them in about sixty seconds.

**A note on sources.** None of these four is cited to anything in this book's bibliography. They are craft practices, taught by demonstration in every quantitative field and defined formally in none of the sources consulted here. So each is demonstrated rather than asserted, on numbers you can check yourself. If the demonstration works, that is the argument.

### Check one: do the units survive?

The cheapest check there is.

Chapter 2 computed the Hillcrest tank's endurance without its pump:

`0.6 ML ÷ 0.9 ML per day = 0.67`

Megalitres divided by megalitres-per-day gives **days**. So 0.67 days, about sixteen hours.

That looks like bookkeeping, and it catches a specific and common error: a quotient reported as "0.67" with no unit attached, into which a reader supplies whatever unit they were expecting.

It also catches something subtler. Storage and demand are both measured in megalitres, which makes them look comparable. They are not the same kind of thing — one is a quantity, the other a rate — and only their ratio means anything. A dimensional check is what stops you subtracting them.

Chapter 3 used this deliberately. Pressure was given in metres of head throughout, precisely because that made every calculation a subtraction and every elevation difference visible.

### Check two: what does it say at zero?

Take a quantity in your model and set it to zero. Then ask what the model says.

Set **Hillcrest customer consumption to zero.**

The Hillcrest figure — town total minus the two metered zones — does not go to zero.

From Chapter 4's decomposition, what remains is leakage elsewhere in the network (**0.08 ML/day**), unbilled operational use (**0.06**), meter under-registration in the metered zones (**0.04**), and leakage inside the Hillcrest zone itself (**0.10**), which is not customer consumption either.

A quantity labelled *Hillcrest demand* that stays positive when Hillcrest customers use nothing **is not a demand.**

Stop and notice what just happened.

That is Chapter 4's central finding. The whole of Chapter 4 — the two-process separation, the five stages, the institutional-purpose analysis, the interviews — arrived at a conclusion that one limiting case flags in about a minute, using arithmetic already on the page.

**This is not an argument that Chapter 4 was unnecessary.** The check raised an alarm; it produced no explanation. It cannot tell you *why* the figure behaves that way, that it is a subtraction residual, what is in it, or what to do. Chapter 4's investigation produced all of that.

It is an argument for running the cheap checks **first**, so that the expensive machinery is spent on problems that survived them.

### Check three: what does it do when pushed?

Different from the limiting case, and it catches different things. Instead of setting something to zero, push it to an extreme the model was never asked about.

Set demand to zero and let treated-water input run at **8.4 ML per day**.

The storage representation from Chapters 1 and 2 says storage rises. And rises. And keeps rising, past the Hillcrest tank's stated **1.2 ML** capacity, past the system's **14.0 ML**, without limit.

There is no spill in the model. No overflow, no ceiling, nothing.

Real tanks overflow. The representation has no term for it, because every question Part I asked ran storage *downward* — and for those questions the omission was invisible and harmless.

It would not be harmless for a question about refill, about recovery after the drought breaks, or about what happens when a conservation request works better than expected. The moment anyone asks one of those, the model gives an answer, and the answer is nonsense.

That is the characteristic value of the extreme-condition check: it finds the questions your model will answer confidently and wrongly.

### Pause: what makes a check worth running?

Before reading on, write two or three sentences.

> You have just run three checks. Two found something and one did not. What makes a check worth running at all?

The tempting answer is "it might find something", which is true and not useful, because it is true of everything.

The answer is that **a check is worth running when it could have come out the other way.**

The dimensional check on `0.6 ÷ 0.9` could have failed — the units could have failed to reduce to days. It did not, and that is information.

You have met this before. Chapter 3 said an interpretation that could never have been contradicted has not been supported, only unchallenged. Chapter 4 said the surviving records are exactly the subset the process kept.

The same idea, arriving for the third time: **a test that could not have failed establishes nothing**, however diligent it looks. This is why running more checks does not straightforwardly mean more confidence, and why a long checklist of things that were never in doubt is a way of feeling careful rather than being careful.

### Check four: is the number the right size?

The last check is the one that repays the most, and it needs two numbers you already have from two different chapters.

From Chapter 3: Hillcrest has **340 connected properties.**

From Chapter 4: Hillcrest customer consumption is **0.62 ML per day**, measured by a temporary insertion meter fitted to the feeder main for two weeks.

Nobody has ever divided them.

### Task: divide them

Do this before reading on. Two lines.

1. What is 0.62 ML per day, per property?
2. Roughly how much water does one household use in a day? Build it from people and litres — do not look it up.

---

`620,000 litres ÷ 340 properties = 1,824 litres per property per day`

For a bound: the case supplies a regional planning figure of about **150 litres per person per day**, and an average household of about **2.5 people**.

`150 × 2.5 = 375 litres per household per day`

`1,824 ÷ 375 ≈ 4.9`

**About five times too high.**

One division and one estimate. No instruments, no interviews, no elevation survey, no provenance work.

### What the check establishes, and what it does not

It establishes that the numbers are **mutually inconsistent**. It does not say which is wrong, and treating it as though it did is the main way this check gets misused.

Three candidates, all alive:

- the property count is wrong;
- the 0.62 figure is wrong;
- **Hillcrest properties are not households.**

Generate all three before accepting any. A reader who jumps to "the measurement must be wrong" has done the check and skipped the thinking.

### The nursery

The case supplies the third.

One of the 340 Hillcrest connections is a **commercial horticultural nursery**. It draws about **0.40 ML per day** on irrigation days, which through a hot summer is most days.

Take it out:

`0.62 − 0.40 = 0.22 ML per day` across the remaining **339** properties

`220,000 ÷ 339 ≈ 649 litres per property per day`

Still high against the 375 bound, and now plausible: Hillcrest is large-plot hillside properties with gardens, and summer garden watering is a large share of their use.

The arithmetic reconciles.

### Pause: why did nobody see it?

Before reading on:

> The nursery is about **65%** of Hillcrest's customer consumption. Four chapters of analysis never revealed it. Why not?

Work back through them.

Chapter 1 had one town-wide demand number — no zones, so certainly no customers. Chapter 2 disaggregated to three zones and stopped there, because zones were what the question needed. Chapter 3 asked what *adequate pressure* meant, which is a question about a threshold, not about who uses the water. Chapter 4 asked where the numbers came from and found the residual, which is a question about records.

At no point did any chapter's machinery ask **how big should this number be?**

And the billing system knew perfectly well. The nursery is a large commercial account; somebody sends it an invoice every quarter. Nothing that reached the analysis carried that fact, which is Chapter 4's institutional-purpose finding arriving one more time.

### The part that actually matters

The catch is not the payoff.

**The nursery is one customer, on a commercial contract, whose irrigation is schedulable.**

Sixty-five per cent of a zone's consumption belongs to a single account that could — possibly, subject to the contract and to asking — shift its watering by twelve hours, off the evening peak that Chapter 3 showed was when the top of the zone falls to three metres of head.

That is an **option**. It is cheap, fast, reversible, and specific, and it involves one phone call rather than a town-wide conservation request.

Part I never produced it. Not because anyone reasoned badly, but because Chapter 2's lesson holds: a representation can only contain the alternatives it can express, and every representation in Part I aggregated Hillcrest into one demand number. There was no nursery in the model for anyone to think about.

Whether the nursery *can* be rescheduled is a separate question, and nothing here says it can. It is an option to investigate, which is more than the analysis had before.

### The four checks, away from water

They are only useful if you can run them on something that is not a utility. Here they are as questions, with what each typically finds elsewhere.

| Check | The question | What it catches, in general |
|---|---|---|
| **Dimensional** | Do the units survive the arithmetic, and are the quantities the same kind of thing? | Rates added to totals. Percentages of different denominators averaged together. A ratio reported without saying of what to what. Currency compared across years with no deflation. |
| **Limiting case** | What does this say when a quantity goes to zero, or to one, or to everything? | A "rate" that stays positive when the numerator is zero. A share that does not sum to one. A cost model with fixed costs hidden inside a per-unit figure. |
| **Extreme condition** | What does it do when pushed far past normal operation? | Capacities exceeded silently. Negative queues, negative inventory, negative populations. Growth without limit. Probabilities above one. |
| **Order of magnitude** | Is this the right *size*? Divide something by something and bound it independently. | Per-person, per-day, per-unit figures that are wildly off. Totals that imply impossible throughput. Effects larger than the thing they act on. |

Two things are worth noticing about that table.

**Every one of them is a division or a substitution.** None requires new data, software, or expertise. That is what "cheap" means here, and it is why there is no defensible reason not to run them.

**They fail in different directions.** The dimensional check catches a category error, the limiting case catches a structural one, the extreme condition catches a missing constraint, and the order-of-magnitude check catches a wrong number. Running one is not running the others.

### The one they will not catch

Honesty requires the other half.

None of these four would have found Chapter 3's pressure problem.

The monitoring point read 25 metres of head. The top of the zone read 3. Both numbers were correct, dimensionally clean, well-behaved at limits and extremes, and entirely the right size. Nothing about the arithmetic was wrong.

What was wrong was that *adequate* had been defined at a place where the problem was not — which is a question about what the number means, not about how it behaves. Only Chapter 3's machinery finds that.

So the cheap checks are a filter, not a substitute. They are worth running first because they are nearly free and they catch a real share of problems. They are not worth trusting as a clean bill of health, and a model that passes all four can still be measuring the wrong thing in the wrong place.

### What this section argues

Four checks. Minutes each. Between them they flagged Chapter 4's central finding, exposed a model that grows water without limit, and produced an option that four chapters of careful work missed.

The conclusion is not that the careful work was wasted. Chapter 4 explained the residual; the limiting case only noticed it. Chapter 3 explained the pressure problem; no cheap check would have.

The conclusion is about **order**. Run the cheap checks first, on everything, before the expensive machinery — because they cost almost nothing, and because what survives them is where the expensive machinery should go.

## 4. Alternatives and Exclusions

You now have a set of criticisms and no way to tell a real one from a worry.

That is a genuine problem and it is the reason most criticism is worthless. *The data might be biased. The assumptions may not hold. More research is needed.* Every sentence there is true, applies to every analysis ever written, costs nothing to produce, and cannot be wrong.

This section is about the difference.

### The method

There is an established one, it is short, and it comes from a 1964 argument about why some fields move faster than others.

> "Strong inference consists of applying the following steps to every problem in science, formally and explicitly and regularly: 1) Devising alternative hypotheses; 2) Devising a crucial experiment (or several of them), with alternative possible outcomes, each of which will, as nearly as possible, exclude one or more of the hypotheses; 3) Carrying out the experiment so as to get a clean result; 1′) Recycling the procedure, making subhypotheses or sequential hypotheses to refine the possibilities that remain; and so on." [@platt1964strong, p. 347]

Three steps and a loop. Notice what each does.

**Step 1 is rival models**, and it comes first rather than last. Most criticism starts by attacking the conclusion in hand; this starts by asking what else could be true.

**Step 2 is this chapter's question in operational form.** *What would show it?* becomes: what observation has alternative possible outcomes, at least one of which excludes something?

**Step 3 is the one nobody does.**

The same source describes the structure as a tree: "At the first fork, we choose—or in this case, 'nature' or the experimental outcome chooses—to go to the right branch or the left; at the next fork, to go left or right; and so on" [@platt1964strong, p. 347]. The image is old — it is credited there to Bacon, as a "conditional inductive tree".

### The line worth memorizing

From the same page:

> "Any conclusion that is not an exclusion is insecure and must be rechecked." [@platt1964strong, p. 347]

Nine words, and they are the chapter's thesis.

You have arrived here three times now by three routes. Chapter 3: an interpretation that could never have been contradicted has not been supported. Chapter 4: your surviving records are exactly the subset the process kept. §3 of this chapter: a check that could not have failed establishes nothing.

This is the general form. **A conclusion is secure to the extent that something was ruled out in reaching it.**

### Why it does not happen

The paper is unusually good on this, and its diagnosis is not the one you would expect.

> "How many of us write down our alternatives and crucial experiments every day, focusing on the *exclusion* of a hypothesis? We may write out our scientific papers so that it looks as if we had steps 1, 2, and 3 in mind all along. But in between, we do busywork. We become 'method-oriented' rather than 'problem-oriented.'" [@platt1964strong, p. 348]

Not carelessness. **Busywork** — legitimate-looking activity that could not have changed the answer.

That is a far more useful account of how criticism fails, because it explains why diligent people produce none. They are busy. What they are busy with is refining, tidying, extending, and re-running, and none of it was ever going to overturn anything.

Which gives you a test to apply to your own work as well as to other people's: *could what I am doing this afternoon change my conclusion?* If not, it is not criticism, whatever else it may be worth.

### The artifact to produce

Principles are cheap. The same page records what two working scientists actually wrote, and the second is a template you can copy directly.

Jacob and Monod, quoted at [@platt1964strong, p. 348]:

> "Our conclusions … might be invalid if … (i) … (ii) … or (iii)…. We shall describe experiments which eliminate these alternatives."

That sentence is the artifact. Not a limitations paragraph, not a list of caveats — a numbered set of ways the conclusion could be wrong, each followed by what would eliminate it.

The same page also credits Lederberg with giving "a list of nine propositions 'subject to denial,' discussing which ones would be 'most vulnerable to experimental test'". Note the second half: not just what could be denied, but which denial is *reachable*.

### Assumption records, and the correction

The obvious way to start is an **assumption record**: a written list of what the analysis takes for granted.

Chapter 5's competence names it, and it is a real practice. But there is a failure mode attached and it is nearly universal.

**Naming an assumption does not handle it.**

A limitations section listing eleven assumptions, none of which carries anything that would show it false, has not criticized anything. It has demonstrated awareness. The reader finishes it knowing the author thought about these things and knowing nothing about whether any of them holds.

So the rule for this book: **every entry in an assumption record carries what would show it false.** If you cannot write that half, say so explicitly — which is §5's subject, and is itself informative.

### Work it on the anchor

Three assumptions from Part I's analysis, each with the second half attached.

**Assumption:** the Hillcrest tank starts a shortage event at or near **0.6 ML**.
*What would show it false:* the tank level log for the same hour on the preceding ten hot days. Available today, in the utility's own records, unexamined.

**Assumption:** Hillcrest's draw during a shortage is roughly its average daily draw.
*What would show it false:* any hourly profile of the zone. **Not available** — Chapter 4 established that fifteen-minute data is discarded after ninety days, and Chapter 3 established the peak is where the problem lives. This is a real gap, not a hypothetical one.

**Assumption:** the conservation request reduces demand roughly as it did last time.
*What would show it false:* the observed response after the previous request, disaggregated by zone. Partly available — Chapter 1 recorded **8.6 ML** against a **9.0 ML** forecast town-wide, but not by zone, because two zones are metered and one is a residual.

Three entries. One check available now, one impossible, one partial. That distribution is normal, and knowing which is which is most of the value.

### Rival models

**Rival models** in this chapter are **instruments of criticism, not options to choose between.**

That distinction matters because the instinct is to treat two competing explanations as a decision to be made. Here they are a tool: if a conclusion survives both, it is stronger; if it survives only one, you have learned where to look.

**Leaving both alive is a legitimate outcome**, and this book's own case is the demonstration.

Chapter 2 proposed two mechanisms for why Hillcrest loses pressure first. **Mechanism A:** the duty pump's capacity limits refill, so the hilltop tank falls. **Mechanism B:** friction loss along an old, undersized feeder main drops pressure at the top of the zone while the tank is still comfortably full.

Both were drawable from supplied facts. Both would produce the phenomenon. They point at different repairs — a pump or a pipe — and at different costs.

Three chapters later, they are **both still alive.**

Chapter 2 named the discriminating observation at the time: run the duty pump at elevated output through one hot afternoon and record pressure at the top of the zone. If pressure recovers, capacity was the constraint. If it does not, the main is.

Nobody has run it. It is not difficult, not expensive, and not prohibited. It simply was not done, and three chapters of increasingly sophisticated analysis passed over the gap without noticing that the whole question was still open.

### Structural uncertainty

That situation has a name. **Structural uncertainty** is uncertainty about whether the formulation is right — not about the value of a number inside it.

The distinction is worth holding firmly, because the two are constantly confused and they call for entirely different responses.

*Is the friction loss 6 metres or 7?* — uncertainty about a number.
*Is friction loss the mechanism at all?* — structural uncertainty.

You can be extremely confident about every number in a model that has the wrong structure, and the confidence is worth nothing. This is why the next section's placement exercise matters: the standard tool for exploring uncertainty in numbers cannot see structural uncertainty at all.

**One word of warning.** Chapter 14 uses `structural identifiability` for something entirely different — whether a model's structure can in principle be recovered from data. Different concept, shared adjective. Do not carry one into the other.

### Building a rival on purpose

A last technique, and it comes from an argument you met in Chapter 2.

If you want to know whether a conclusion depends on your simplifications, build a differently simplified representation and see whether the conclusion survives. Treat one problem "with several alternative models each with different simplifications but with a common biological assumption. Then, if these models, despite their different assumptions, lead to similar results we have what we can call a robust theorem which is relatively free of the details of the model. Hence our truth is the intersection of independent lies" [@levins1966strategy, p. 423].

Chapter 2 used this to test conclusions across the storage-only and network representations. Here it is a criticism technique: deliberately build the rival, then check.

Formal treatment of robustness — how to construct it, how to trade it against performance, what to do when conclusions do not survive — is Chapter 12, and `robustness` is reserved there. What Chapter 5 takes is the habit.

### Task: an assumption record

For the Part I analysis, write four entries.

Each entry has two parts: **the assumption**, stated specifically enough to be wrong, and **what would show it false.**

Then mark each observation: available now, obtainable with effort, or not obtainable.

If any entry's second half reads "further research", delete the entry and write a real one.

## 5. When You Cannot Find Out

There is a problem with the method in §4, and pretending otherwise would undo the chapter.

**It assumes you can run the experiment.**

Molecular biology can. The 1964 argument is drawn from a field where you devise the crucial test on Monday and have the result by Friday.

A water utility cannot rerun a drought. A city cannot un-resurface a road to see what would have happened. A hospital cannot randomise which patients are reminded by post. Most of the decisions this book is about are made once, in conditions that will not recur, by people who cannot experiment on the system they are responsible for.

So what survives?

### Two of three steps survive

**Devising alternatives survives entirely.** Nothing about generating rival explanations requires an experiment. You can always ask what else could be true.

**Naming what would discriminate survives entirely.** You can always ask what observation would have alternative outcomes, at least one of which excludes something — whether or not that observation is available to you.

**Getting the clean result often does not survive.** Frequently the discriminating observation cannot be made: it is in the past, it is prohibitively expensive, it would require an intervention nobody will authorise, or it concerns a counterfactual that never happened.

### The fourth step

So this book adds one, and it is worth being explicit that it is an addition rather than something the 1964 source licenses.

> **Step 4: if you cannot make the observation, say so — and say what your conclusion is resting on.**

That step is **this book's own**. The strong-inference argument does not discuss it, and extending the method this way is a move made here for readers who work outside experimental settings.

### Why that is a result, not a failure

The instinct is to treat "I cannot find out" as the end of the analysis and to quietly drop the item.

It is the opposite. This sentence —

> *This conclusion rests on something we have not excluded and cannot currently exclude.*

— is a stronger output than a confident recommendation, because it is true, it is specific, and it tells the person receiving it exactly where the weight is being carried.

Compare what usually appears instead: a limitations paragraph mentioning that all models have limitations. That sentence tells nobody anything.

### Pause: has Part I failed?

Before reading on, write two or three sentences.

> Mechanism A and Mechanism B have been open since Chapter 2. Three chapters have passed. Is that a failure of Part I?

The answer has two parts and they pull in opposite directions.

**No**, in the sense that unresolved rivals are a normal and honest state. Part I never claimed to know which mechanism operates, and a book that resolved it by assertion would have taught something false.

**Yes**, in a specific and uncomfortable sense. The discriminating observation for Mechanisms A and B **is obtainable.** Running the duty pump at elevated output through a hot afternoon requires a technician, an afternoon, and a portable gauge. It is not a counterfactual, not prohibited, and not expensive.

So this is not the impossible case at all. It is the case where the observation was named in Chapter 2, was available the whole time, and nobody made it.

**That is the more common failure**, and it is worth separating from genuine impossibility. Most unexcluded alternatives in real work are not unexcludable. They are unexcluded because naming what would settle a question and then arranging to find out are different activities, and organisations are much better at the first.

### The three cases

Sort every unresolved item into one of these, and label it.

**Obtainable and not obtained.** The pump test. The tank level log for the last ten hot days. Say so, plainly, and say what it would cost — because this category is an action list, not a limitation.

**Obtainable in principle, not by you.** An hourly demand profile for Hillcrest requires a zone meter that does not exist. Somebody could install one; you cannot produce the data this week. Name what would have to change.

**Not obtainable.** What Hillcrest's demand *would* have been last August without the conservation request. That is a counterfactual and no amount of effort recovers it.

The three deserve different sentences in your write-up, and collapsing them into "limitations" destroys the distinction that matters most — the first category is a to-do list and the third is a permanent condition of the analysis.

### Writing the sentence

Step 4 asks you to say what the conclusion rests on. That is easy to agree with and surprisingly hard to write, so here is the shape.

A usable version names three things: **what is unexcluded, what would exclude it, and what changes if it turns out the other way.**

> *This recommendation assumes the Hillcrest tank starts a shortage at around 0.6 ML. We have not checked the level logs for previous hot days, which would settle it in an afternoon. If the typical starting level is materially lower, the endurance figure falls and the case for acting earlier strengthens.*

Compare the version that usually gets written:

> *Note: starting tank level is uncertain.*

The second sentence is true, costs nothing, and gives its reader no way to act. The first tells them what to do about it, roughly what it costs, and which direction the answer would move.

**The third clause is the one people omit and the one that matters.** An unexcluded alternative that would not change anything is not worth reporting. An unexcluded alternative that would reverse the recommendation belongs in the first paragraph, not the appendix.

If you cannot say what changes, you have not finished thinking about the item — or it does not belong in the criticism at all.

### What comes next, and what does not

Naming the discriminating observation is where this chapter stops.

Whether it is **worth acquiring** — what it costs, what it would change, whether the decision would move — is a separate question with its own machinery, and it is Chapter 11's. *We should find out* and *finding out is worth what it costs* are different claims, and merging them is how organisations end up either investigating everything or nothing.

### "All models are wrong" is not a way out

One phrase needs handling, because it is the single most common way criticism gets terminated.

Somebody says the model is wrong. Somebody else says all models are wrong. Everyone nods, and the objection evaporates.

The remark's usual source does not use it that way. In the lecture where it appears as a title, the passage runs the other direction: when we blame outside shocks and unforeseen effects for a policy's failure, "we think we are describing a capricious and unpredictable reality. In fact, we are highlighting the limitations of our mental models" — and the response offered is to "expand the boundaries of our mental models so that we become aware of and take responsibility for the feedbacks created by our decisions" [@sterman2002models, p. 505].

Recognising that a model is wrong is the beginning of the obligation, not its discharge.

The question is never *is this model wrong* — it is, and you knew that in §2. The question is whether it is wrong **in a way that matters for this use, at this risk**, and that question is answerable.

### And prediction is the cheap half

A last correction before the section closes.

A failure mode you have predicted is not a failure mode you have prevented.

Writing "the tank may start lower than assumed" costs a sentence. Checking the ten-day log costs an hour. Installing a Hillcrest zone meter costs a capital case, a procurement, and a year.

Chapter 5 teaches the prediction. It should not leave you with the impression that prediction is the work. It is the part that makes the work findable.

## 6. Criticizing Part I

Assemble it.

### The criticism, in one page

**What it is adequate for.** Deciding whether to request voluntary conservation during a seven-day heatwave, at day-level resolution, for total system storage. If it is wrong, a zone falls below its operating threshold on a hot evening and recovers overnight — a service consequence, recoverable, which bounds how much criticism is warranted.

**What the cheap checks found.**

- *Dimensional:* clean. The endurance arithmetic reduces to days correctly.
- *Limiting case:* the Hillcrest figure stays positive when Hillcrest customers use nothing. It is not a demand.
- *Extreme condition:* the storage model grows water without limit. No spill term. Harmless for every question Part I asked; wrong for any refill question.
- *Order of magnitude:* **1,824 litres per property per day**, about five times a plausible household. Resolved by a nursery at **0.40 ML/day** — roughly 65% of the zone's consumption, invisible to every representation in Part I.

**What remains unexcluded.**

- Mechanism A versus Mechanism B — obtainable, not obtained, open since Chapter 2.
- The starting tank level — obtainable from the utility's own logs, unexamined.
- Hillcrest's hourly profile — not obtainable; the meter does not exist and the fine data is discarded after ninety days.
- The zone-level response to a conservation request — not obtainable; two zones metered, one a residual.

**The one item that could reverse the recommendation.**

The nursery. Part I's option set was conservation, production increase, and restriction — all town-wide or zone-wide instruments aimed at many customers. If roughly two-thirds of Hillcrest's consumption is one schedulable commercial account, the cheapest available action may be a phone call, and the analysis never contained it.

That is what a criticism looks like when it is finished. Specific, checkable, sorted by whether anything can be done, and containing at least one item that changes what you would do.

### What it does not say

Worth noting what is absent from that page, because the absences are deliberate.

**It does not say the analysis is bad.** Every step in Part I was correct given what was available. Chapter 2's `0.6 ÷ 0.9` was right arithmetic on the number it had. Chapter 3's monitoring-point reading was a correct measurement. Chapter 4's residual was a correct subtraction. A criticism that concluded "this work was poor" would be both wrong and useless, because it would give nobody anything to do.

**It does not list everything that could conceivably be wrong.** It lists what could plausibly be wrong *and* would matter *and* has something attached that would settle it. Everything else was either checked or dropped.

**It does not end in a recommendation to do more research.** Three items name a specific observation and say whether it can be obtained. One of those is an afternoon's work with equipment the utility already owns.

**And it does not pretend the open questions are closed.** Mechanism A and Mechanism B are still open, and the criticism says so rather than picking one to look decisive.

That last point is worth sitting with, because it is the hardest to do in front of somebody who wants an answer. *We do not know, here is what would tell us, and here is what it costs* is a complete and professional output. It is not a failure to deliver.

### Task: diagnose five defects

Each item below is a criticism section from a real-looking report. Each contains one defect. Write the defect, what it stops the reader concluding, and a repair.

1. *"Limitations: the data may be incomplete; the assumptions may not hold in all conditions; the model is a simplification; further research is recommended."*
2. *"We documented all model assumptions in Appendix C."*
3. *"The model reproduces last year's observed storage within 3%, confirming its validity."*
4. *"Criticism and robustness: we varied each input parameter by ±20% and the conclusion was unchanged in all cases."*
5. *"One reviewer questioned whether the pump is really the constraint. All models are wrong, so this cannot be settled definitively."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

### Task: place four situations

> **Chapter 5:** could this be the wrong model?
> **Chapter 8:** given this model, how uncertain is the answer?

Place each.

1. The Hillcrest figure stays positive when Hillcrest consumption is zero, so it is not a demand.
2. The 0.62 ML/day figure came from a two-week study three years ago and may be off by some margin.
3. Mechanism A and Mechanism B are both still alive.
4. Varying the friction-loss estimate between 4 and 8 metres to see what changes.

**The fourth is the one to think about.** It feels like criticism — it is systematic, it is quantitative, it produces a chart. And it varies an input *inside* a formulation, so it cannot see the formulation. A model that is structurally wrong will produce a beautifully stable sensitivity analysis, and the stability will be reported as confidence.

Sensitivity analysis is a genuine and valuable technique and it belongs to Chapter 8. It is not criticism, and offering it as the criticism section is the most sophisticated-looking way to skip this chapter entirely.

### Part I ends here

You can now take an unfamiliar consequential problem and: frame what is being asked and for what use; build a representation and say what it can and cannot answer; interrogate what its numbers stand for; trace where those numbers came from and what never entered them; and criticize the whole thing well enough to say what would show it wrong.

That is a complete pass through formulation, and it is the foundation the rest of the book is built on.

What Part I cannot do is tell you what the evidence actually supports.

Every chapter so far has been about getting the question, the picture, the numbers, and the criticism into defensible shape. None of them has said what follows from evidence — how uncertainty behaves, what could be established even in principle, what finite data can support, and how to combine sources that disagree.

That is Part II, and it starts with the machinery for reasoning about what you do not know.

## 7. Cold-Start Practice and Retrieval

### Return to your seven-minute list

Find what you wrote at the start of §1: what would have to be true for Part I's conclusion about Hillcrest to be right.

Read it against §6's criticism. Do not score it.

- Did any entry carry **what would show it false**?
- Did any entry name a number and say roughly how big it should be?
- Did you have anything that could have **changed the recommendation**?

Most first lists are assumptions without discriminating observations — which is exactly the artifact §4 says is not yet criticism. That is the specific thing this chapter adds.

The other common pattern is a list of things that could go wrong in general — data quality, model simplification, unforeseen events — none of which is about this analysis. If yours could be pasted unchanged onto any report in any field, it was not about this one.

### Independent transfer

The task shape changes here, deliberately.

Chapters 1 to 4 asked you to build something. This chapter's skill is criticizing a completed analysis, and you cannot build a four-chapter analysis in forty minutes — so one is supplied.

**You are the reviewer, not the analyst.**

You have been assigned **one** of the forms below. Open only that one.

- [Form A — Closing one of four recycling depots](transfer-form-a.md)
- [Form B — Moving clinic appointment reminders from post to SMS](transfer-form-b.md)

Allow about **40 minutes**.
Every fact you need is supplied. Do not look anything up.

Do not open the other form. You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the method from memory

Before looking back, write down how you would criticize any analysis handed to you.

Aim for the sequence, not the wording.

For reference, after you have tried:

1. What is this adequate **for** — use, accuracy, quantity?
2. What happens if it is wrong? (This decides how much of the rest to do.)
3. Do the units survive the arithmetic?
4. What does it say at zero, and at an extreme?
5. Is each number the right **size**? Divide something by something.
6. What are the alternatives — what else could be true?
7. For each, what observation would exclude it?
8. Which of those observations are available now, obtainable with effort, or not obtainable?
9. Which criticism, if right, would **change the recommendation**?
10. What is this conclusion resting on that nobody has excluded?

Question 9 is the one to keep if you keep only one. A criticism that could not change the decision is decoration, however rigorous it looks.

Question 2 is the one people skip, and skipping it is why criticism either does not happen or never stops.

A caution about the list, in the spirit of the chapter.

Ten questions run mechanically produce ten mechanical answers, and a document that has been through them can look thoroughly criticized while nothing was ever at risk. That is precisely the busywork the method warns about — legitimate-looking activity that could not have changed the conclusion.

The test is the same one §3 gave for checks: **could this have come out the other way?** If you ran all ten and changed nothing, either the analysis was unusually sound or you were not really asking.

There is also a social difficulty worth naming, because it is the reason this skill is rarer than it should be. Most of these questions are uncomfortable to ask about work that is finished, defended, and attached to somebody's reputation — including your own. The techniques in this chapter are easy. Asking them out loud, about an analysis a room has already agreed with, is not.

Nothing in this book makes that easier. What it can do is make the question specific enough that it is about the analysis rather than about the analyst — which is most of what "here is what would settle it" buys you.

### If the transfer went badly

- **You produced general caveats.** Reread §4. Every criticism needs what would settle it; if you cannot write that half, you have a worry.
- **You found defects but none could reverse the recommendation.** You proofread rather than criticized. Ask what would have to be true for the *conclusion* to flip.
- **You never divided anything.** The order-of-magnitude check is the highest-yield move in this chapter and it takes one line.
- **You treated a rival explanation as an alternative to choose between.** They are instruments. Ask what would exclude one, not which you prefer.
- **You wrote that the analysis was poor.** Check whether each step was actually wrong, or correct given what was available. Part I's steps were correct and its conclusion was still incomplete. That combination is the normal one.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Do not reread this chapter immediately beforehand, and do not look at the form you have not done.

### What Chapter 6 asks next

Part I got the formulation into defensible shape.

Almost every open item in §6 is now a question about **evidence**: how likely is it that the tank starts lower than assumed; what would the pump test actually tell us; how much would one hot afternoon's data move our belief about Mechanism A.

Those are questions about uncertainty, and Part I has given you no way to reason about them beyond "it might be" and "it might not".

Chapter 6 supplies the machinery: how uncertainty is represented, how it is updated when evidence arrives, and how a claim about what is likely can be scored rather than merely asserted.
