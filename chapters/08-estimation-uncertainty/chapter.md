---
chapter: 8
part: 2
title: "Estimation, Uncertainty, and Model Checking"
status: drafted
---

# Chapter 8: Estimation, Uncertainty, and Model Checking

## 1. The Number You Were Told Not to Trust

Two chapters ago, this book did something it had not done before: it used a number it had already told you was made up.

Chapter 6 needed a spread on the utility's daily demand in order to run a simulation. It supplied **±0.6 ML**, and said this about it:

> *The spread is supplied and is not derived from anything. That is the point of the demonstration: running the projection ten thousand times will produce a stable answer about a spread nobody has justified.*

Then it ran the projection, got a breach probability of about **77%**, and told you that the stability of that figure was about the arithmetic rather than about the world.

**This chapter goes and gets the records.**

The utility has forecast-versus-actual demand for twenty-four past heat events, sitting in a system nobody has interrogated for this purpose. By the end of §4 the ±0.6 will have been replaced by something earned, and the 77% will have moved — in a direction that should surprise you, for a reason worth understanding.

Notice what kind of repair that is. Nobody has to collect anything, commission anything, or wait. The records exist, they have existed for twelve years, and the reason nobody ran the calculation is that **nobody was assigned to be uncertain about the spread.** The forecast had a number, the simulation needed a spread, and a plausible one was supplied at the moment it was needed by whoever was writing that section.

### Before reading further

Take about **six minutes**.

> **Where should the ±0.6 have come from? And once you had the records, what exactly would you do with them?**

Write a few sentences. Be specific — not "look at historical data" but what you would compute and what you would report.

Keep what you write. You will come back to it.

---

### Where this sits

Chapter 7 borrowed a four-step sequence: Define, Assume, Identify, Estimate. It worked the first three and handed the fourth here.

**This is step 4, and Chapter 7's verdict still stands.** The pump-upgrade question was found *not identified*, and nothing in this chapter revisits it. A good estimation procedure cannot repair a bad identification — Chapter 7 said so, from a source, and this chapter does not quietly walk it back by estimating the thing anyway.

What Chapter 8 estimates is a quantity that **is** identified and that the utility has been using without checking for years.

### A promise this chapter does not keep

Chapter 6 told you something about notation, and it needs correcting rather than quietly dropping.

> *If something in this chapter seems to want a symbol that is not on that list, it belongs to Chapter 8.*

**The material belongs here. The symbols do not.**

Everything in the next thirty-eight pages is done on the utility's actual numbers — averages, differences, divisions, and an interval written as two numbers. The symbols Chapter 6 deferred are needed for **deriving** estimators and interval formulas, and this chapter derives none. What it teaches instead is what a derived number means, what it is conditional on, and how routinely that gets thrown away.

So the book's notation stays where Chapters 6 and 7 left it: the conditioning bar, odds, `do(·)`, and arrows. Where the machinery genuinely requires more, this chapter says where it lives rather than gesturing at it.

### And a warning about what this chapter takes away

Chapters 1 to 7 mostly added things. This one mostly removes them.

By the end you will find it harder to write *the effect is 1.8*, harder to report an interval without a paragraph attached, and much harder to write *significant* in a sentence you expect somebody to act on. Several habits that currently make your reports look competent will stop being available.

**That is the point, and it is not nihilism.** What replaces them is more useful and only slightly longer: a number, what it is conditional on, what would change it, and what has been checked in a way that could have failed. Every organisation that reads analysis has been trained to accept the shorter form, and the shorter form is where most of the damage happens.

## 2. Estimand, Estimator, Estimate

Chapter 1 told you these were three different things. Chapter 7 gave the first one its formal treatment. This section does the other two, and the reason to spend five pages on three definitions is that **every failure in this chapter is a confusion between two of them**.

### Three words, three jobs

**Estimand.** What you want to know. Chapter 7's subject: a target quantity with its attributes filled in — treatment, comparison, population, variable, window, summary.

**Estimator.** The procedure you apply to data to produce a number. *Take the twenty-four errors and average them* is an estimator. So is *take the median*. So is *fit a line and read off the slope*.

**Estimate.** The number that procedure produced on the data you actually have. **+1.8 ML** is an estimate.

Here is why the separation earns its space.

| The confusion | What it produces |
|---|---|
| The **estimate** treated as the **estimand** | "The bias is 1.8 ML" — a number reported as the thing itself |
| The **estimator** treated as the **estimand** | The question quietly becomes whatever the method computes |
| The **estimand** treated as the **estimator** | A target defined by what is convenient to calculate |
| The **estimator's properties** attributed to the **estimate** | "This is an unbiased estimate" — a category error, below |

The second is the most common in organisations and the least visible. Somebody asks what the average forecast error is; the analyst averages what is in the system; and the estimand silently becomes *the mean error among events that were logged in the current system*, which is a different quantity from *the mean error the utility's forecasting process produces*.

Chapter 4 taught you to ask how records come to exist. This is where that question meets a number.

### Which procedure, and does it matter?

The utility's 24 errors could be summarised several ways, and the choice is an estimator choice.

**The mean.** Add the 24 errors, divide by 24. Sensitive to a single extreme event.

**The median.** The middle value. Insensitive to extremes, and answering a slightly different question about the typical error rather than the average one.

**A trimmed mean.** Drop the largest and smallest few, average the rest. A compromise, and a choice about how many to drop.

**A fitted trend.** Model the error as changing over time and read off where it is now. A different estimand again, because it is about the current error rather than the average across twelve years.

Notice what happened at the fourth. The estimator changed and **the estimand changed with it**, without anybody announcing a new question. That is the third row of the table above, and it is the route by which a target quantity gets chosen by what is convenient to compute.

**The discipline is to write the estimand down first and then pick a procedure for it**, which is Chapter 7's *define before design* arriving one step later in the pipeline. If you find yourself justifying a target by saying it is what the method produces, the two have swapped places.

### Three properties, and whose they are

Textbook treatments give an estimator many properties. Three are worth your attention.

**Bias.** Whether the procedure, applied over and over to fresh data from the same process, centres on the estimand.

**Variance.** How much the procedure's output moves between such applications.

**Consistency.** Whether the procedure converges on the estimand as the amount of data grows without limit.

**All three are properties of the procedure.** Not of your number.

### The category error

> *This is an unbiased estimate.*

Strictly, there is no such thing.

Unbiasedness is a property of the **estimator** — a statement about where the procedure centres across repeated application. Your estimate is one number, produced once, on the data you happen to have. One number is neither biased nor unbiased. It is simply what came out, and it can be far from the estimand even when the procedure that produced it is unbiased in every sense a statistician would recognise.

This is not fussiness about wording. The sentence licenses a reader to treat the number as trustworthy, and the licence comes from grammar rather than from evidence. Nothing about *this* number has been established.

**Chapter 3 taught you the same structure in a different vocabulary.** A calibrated instrument is not a correct reading. Calibration is a property of the device, established against a reference; any particular reading still carries random error, and a well-calibrated sensor can hand you a number that is well off.

Same shape. A good procedure does not make a given output good.

### A shape you have now met three times

Chapter 6: **calibration** is a property of a forecaster across a record. One forecast cannot be scored, because a single outcome is consistent with any probability strictly between 0 and 1.

Chapter 7: **balance** is a property of a randomization procedure across hypothetical replications. Reading it off a single trial is a category error, and four published sources were caught doing it.

Chapter 8: **bias, variance, and consistency** are properties of an estimator across repeated application. Attributing them to one estimate is the same error again.

Three chapters, three fields, one structure: **a property defined over an ensemble, routinely read off a single instance.** By the third occurrence it is worth converting into a reflex — when told that something *is* unbiased, calibrated, balanced, or reliable, ask what the ensemble is and whether you are looking at one member of it.

### The estimate that is not about anything

One consequence of the three-way separation is a diagnosis you can make quickly and that most reports invite.

If a number has no stated estimand, it is not an answer to anything. It is the output of a procedure.

That sounds harsh until you try to use such a number. Somebody reports that forecast error is 1.8. You want to know whether it applies to the coming week — which needs the population attribute. Whether it would survive a conservation request — which needs the window and the treatment of intervening events. Whether it is about the process or about the logged events — which needs the estimand. **None of those is answerable, so the number cannot be used for anything except being quoted**, which is what happens to it.

Chapter 6 made the same diagnosis of a probability with no conditioning information, and Chapter 7 of a causal claim with no comparison. Three chapters, three quantities, one failure: a number offered as though it stood alone.

### One word announced, one word declined

Two vocabulary problems, and they need different handling.

**`consistency` collides with Chapter 7.**

There, it was the third identifiability condition: the observed outcome under the treatment received equals the counterfactual outcome under that treatment, which requires the intervention to be well defined. That is a condition about what a causal claim needs.

Here, it is an estimator property: the procedure converges on the estimand as data accumulates.

**These have nothing in common beyond the word.** This book will use both, as it uses both senses of `calibration` and both traditions' `validation`. Say which you mean, every time, in your own writing.

That is the fourth such collision the book has had to announce. The book keeps meeting them because it works across fields that borrowed one another's words without coordinating, and the alternative — inventing new words to avoid the clashes — would leave you unable to read anything.

**`confidence` is worse, and this book declines it.**

The technical term does not mean what the ordinary word promises, and the problem is documented. One of this chapter's sources notes that the statistical usages of "significance" and "confidence" are "at odds with other authors and with ordinary English definitions" [@greenland2016misinterpretations, p. 339].

So this book writes **`interval estimate`**. You will meet `confidence interval` everywhere else, which is why it is named here once, and §4 explains exactly what it is and is not.

Chapter 3 took the same position on `validation` — declined the word, said why, and told you what you would encounter elsewhere.

### Why this section is five pages

Because the alternative wording is available and worse.

A report that says *the forecast bias is 1.8 ML* has collapsed all three into one. It reads as a fact about the utility's forecasting. It is in fact a number produced by one procedure, applied to one set of records, chosen for one target quantity, and each of those three choices was made by somebody who could have chosen otherwise.

**Keeping the three apart is what makes the report arguable.** A colleague who disagrees can now say which one they disagree with — that the estimand should have excluded conservation events, or that the median would have been a better procedure, or that they accept both and think the number is what it is. Those are three different conversations and the collapsed sentence permits none of them.

That is the same service Chapter 6 got from writing conditioning information into a probability, and Chapter 7 from writing a target quantity's five attributes. The book keeps making the same move because it keeps working.

### Task: label three statements

Label each as an estimand, an estimator, or an estimate — and where a statement confuses two, say which.

1. *"The mean forecast error across all logged heat events, in ML over the seven-day window."*
2. *"Take every logged event, subtract forecast from actual, and average."*
3. *"The forecasts are biased low by 1.8 ML."*

Statement 3 is the interesting one, and what is wrong with it is not the number.

## 3. Everything You Compute Is Conditional on a Model

This is the section the rest of the chapter is a consequence of.

### The claim

Here is a paragraph from a paper on how statistical results are misread. It is about P values, which §5 deals with, but the claim is general and it is the organising idea of this chapter.

> "This definition embodies a crucial point lost in traditional definitions: In logical terms, the P value tests all the assumptions about how the data were generated (the entire model), not just the targeted hypothesis it is supposed to test (such as a null hypothesis). Furthermore, these assumptions include far more than what are traditionally presented as modeling or probability assumptions—they include assumptions about the conduct of the analysis, for example that intermediate analysis results were not used to determine which analyses would be presented." [@greenland2016misinterpretations, p. 339]

Three claims, and each does work.

**A computed result is about the entire model**, not the one thing you had in mind.

**The model contains more than the statistical assumptions** anybody writes down in a methods section.

**It includes how you conducted the analysis** — specifically, that you did not look at intermediate results and then decide what to present.

### The third claim reorganises the subject

Analytic flexibility — the fact that the same records support many defensible analyses with different answers — is usually filed under research ethics. Something about integrity, adjacent to the statistics, to be handled by norms and disclosure.

**The source puts it inside the model.**

That the analysis was not steered by intermediate results is an assumption **on the same footing as** the assumption that observations are independent, or that the measurement process was stable. Violating it invalidates the computed number in exactly the same way and for exactly the same reason.

This is why §6 of this chapter is not an appendix about good practice. It is the same subject as §3.

It also changes what a methods section is for. Most methods sections describe the procedure: which records, which exclusions, which calculation. Almost none describe **how the procedure came to be the one reported** — how many alternatives were considered, in what order, and whether any results were seen along the way.

By the claim above, that second description is part of the model. Leaving it out is not a stylistic omission; it is leaving out an assumption the number depends on.

### The model contains the analyst

That sentence sounds like a slogan and it is a literal reading of the quotation.

Consider two analysts, working the same 24 records with the same procedure, and arriving at the same **+1.8**.

The first wrote down the procedure on Monday, ran it on Tuesday, and reported the result.

The second ran it four ways over a fortnight, saw that three gave one verdict and one gave another, and reported the version that matched what the operations director had said in a meeting.

**The two numbers are identical and they do not mean the same thing.** The first is a compatibility summary under a model whose assumptions hold. The second is a compatibility summary under a model with one assumption false, and there is nothing in the number, the record, or the arithmetic that distinguishes them.

The only thing that could distinguish them is a description of the process, which is why principle 4 of the statement in §5 says what it says and why the guideline in §7 asks for exactly that.

### The anchor's number, and what it assumes

The utility has forecast-versus-actual seven-day demand for **24 past heat events**. Forecast error is `actual − forecast`, in ML.

The mean error is **+1.8 ML**. The forecasts run low.

Now list what that number is conditional on. Not the statistical assumptions — the others.

- That the 24 logged events are the relevant ones. Some heat events were presumably not logged as such, and the threshold for calling something a heat event has not been checked.
- That "actual demand" means the same thing across twelve years, through a SCADA replacement and at least one metering change.
- That the forecast recorded against each event is the forecast that was current when the decision was made, rather than a later revision.
- That events with a conservation request in force belong in the same average as events without one — which Chapter 1 gives a specific reason to doubt, since the forecast is conditional on no new action.
- That nobody, at any point, looked at the running average and decided how far back to go.

**Five assumptions, and not one of them is statistical.** Every one of them can make the +1.8 the wrong number, and none would be caught by any calculation performed on the 24 records.

That last clause is the one to sit with. There is no diagnostic you can run on the twenty-four rows that reveals a changed definition of "heat event", because the rows do not record what the definition was. A calculation cannot see an assumption that never entered the data.

**Which is why the check that matters most is usually a conversation.** Somebody in operations knows when the SCADA changed. Somebody in the forecasting team knows whether the recorded forecast is the original or a revision. Neither of them is normally asked, because the analysis feels like a data problem and they are not data people.

Chapter 4's discipline was to ask how the records came to exist. Chapter 8's is to ask that question of a **number** rather than of a dataset, and the answer is nearly always upstream of anything you can compute.

### When the number surprises you

Suppose the mean error had come back at +9 ML rather than +1.8 — an enormous, implausible figure. What would you have learned?

The source is precise about this:

> "It is true that the smaller the P value, the more unusual the data would be if every single assumption were correct; but a very small P value does not tell us which assumption is incorrect." [@greenland2016misinterpretations, p. 339]

**You would have learned that something is wrong, and not what.**

Maybe the forecasts really are terrible. Maybe two events were double-counted. Maybe the units changed. Maybe a decimal moved. The surprising number flags the whole model and points at nothing inside it.

Chapter 5 established exactly this structure: a failed check tells you a formulation is inadequate somewhere and does not tell you where. Chapter 8's version is sharper only because the number arrives looking precise, so the temptation to attribute the failure to the one assumption you were thinking about is much stronger.

### And when it does not surprise you

The other direction says considerably less.

> "Conversely, a large P value indicates only that the data are not unusual under the model, but does not imply that the model or any aspect of it (such as the test hypothesis) is correct." [@greenland2016misinterpretations, p. 339]

An unsurprising result means nothing you were checking has visibly broken. It does not mean the model is right. Chapter 5's test applies unchanged: a check that could not have failed establishes nothing, and a check that simply did not fail establishes only that.

### Eight subjects, one claim

The description of this chapter in the book's architecture names eight things: likelihood, estimation, regression, uncertainty quantification, predictive evaluation, measurement-error reasoning, analytic-flexibility awareness, and model checking.

Forty pages divided eight ways would be a survey, and a survey would teach you nothing you could use.

They are not eight subjects. They are consequences of one claim.

**Estimation** — the estimate is conditional on the model.
**Uncertainty quantification** — the interval is conditional on the same model, and covers only part of it.
**Analytic flexibility** — the conduct of the analysis is one of the model's assumptions.
**Model checking** — checking the assumptions you were not interested in.
**Predictive evaluation** — checking them against data they were not fitted to.
**Measurement-error reasoning** — one of the assumptions, and usually unstated.
**Likelihood** — the machinery that ties data to a model; you need to know it exists and that this book does not teach it.
**Regression** — a model, and therefore a set of assumptions under discussion, not a technique this chapter teaches.

Two of those deserve a sentence more, because they are the two most likely to be expected and not delivered.

**Likelihood** is the machinery that connects a body of data to a model — a way of asking how well a given set of assumptions accounts for what was observed, which is then used to pick among candidate settings. Chapter 6 deliberately avoided the word because the ratio it taught would have been called a likelihood ratio, and Chapter 6 did not want the estimation sense arriving early. It arrives here as a named thing you should know exists. Working with it requires the notation §1 declined, and it is depth curriculum.

**Regression** is not a technique in this chapter. It is an example of a model, and everything §3 says applies to it exactly: a regression coefficient is a number conditional on an entire specification — which variables were included, what functional form was assumed, which observations were kept, and how the specification came to be the one reported. The last of those is the one nobody writes down, and by the claim at the top of this section it is inside the model with the rest.

Everything after this section is one of those eight, worked on the anchor.

### A note on what "the model" means here

The word has been doing heavy work and it is broader than a reader coming from Chapter 2 may expect.

Chapter 2 used `representation` for what is inside a model of a system — the entities, the mechanisms, the grain. That is part of what is meant here and it is not the whole.

**The model, in this chapter's sense, is everything that had to be true for the number to mean what it is being taken to mean.** The representation. The assumptions about how the data were generated. The assumptions about what the recorded fields mean. And, per the quotation above, the assumptions about how the analysis was conducted.

Written out, the model behind `+1.8` includes propositions like *the recorded forecast is the one that was current*, *heat events were identified the same way throughout*, and *the person computing this did not choose the window after seeing the answer*. None of those is a modelling assumption in Chapter 2's sense, and every one of them is load-bearing.

### The assumption nobody writes down about the numbers themselves

There is one more assumption inside every calculation in this chapter, and it has been invisible because Chapters 3 and 4 dealt with it so thoroughly that it feels handled.

**That the recorded numbers are the quantities they are labelled as.**

Chapter 3 established that a measurement has trueness and precision, that a calibrated instrument still hands you readings with error, and that adding decimal places to a biased reading produces a more finely specified wrong answer. Chapter 4 established that one of the utility's demand figures was never measured at all — it is a subtraction residual containing leakage in other zones and water the utility used itself.

**Every "actual demand" in the 24-event record inherits both.**

So the `+1.8` is a difference between a forecast and a quantity that is itself a construction. Some part of the offset could be a forecasting bias; some part could be the residual's composition changing over twelve years; and nothing in the record separates them.

This is not a reason to discard the number. It is a reason the number cannot be reported as *the forecasting process runs low by 1.8 ML* without a clause attached, and it is one more item for §4's enumeration.

### Task: five non-statistical assumptions

The mean forecast error is **+1.8 ML** across 24 events.

Write down **five assumptions that number depends on which are not statistical assumptions** — not independence, not normality, not sample size. Assumptions about how the records came to exist, what the fields mean, and how the analysis was conducted.

Then mark which of the five you could check with the records the utility already holds, and which would require asking somebody.

Most readers find the second list longer than the first. That is the ordinary situation and it is not a reason to stop; it is a reason to make the phone call before publishing the number.

## 4. How Uncertain, and About What?

You have an estimate: **+1.8 ML**. The obvious next question is how far off it might be.

### The interval

The spread of the 24 errors is **2.4 ML**.

A standard rule turns that into a statement about how much the *average* would move if you drew another 24 events from the same process. Divide the spread by the square root of the count:

`2.4 ÷ √24 = 0.49 ML`

That is the **standard error** — a summary of how much the estimate would move between repeated applications of the same procedure to fresh data. Note what it is a property of: the procedure and the sample size. Not the number.

Two features of that division are worth noticing, because both get misused.

**It shrinks with the square root of the count, not with the count.** Quadrupling the record halves the standard error. Getting the 0.49 down to 0.25 needs ninety-six events rather than forty-eight, and to 0.12 needs three hundred and eighty-four. There are diminishing returns built into the arithmetic, and a data-collection proposal that does not account for them is promising more than it can deliver.

**It says nothing about whether 2.4 is the right spread.** The formula takes the observed spread as given. If the 24 events came from two different processes — and §7 shows they did — then 2.4 is a mixture of two spreads and a difference in centres, and dividing it by the square root of 24 produces a tidy number about a quantity that does not exist.

Take roughly two standard errors either side and you get an **interval estimate**:

**+0.84 to +2.76 ML**

### What it covers

Exactly one thing: **how much the average of 24 errors would move if you drew another 24 events from the same process.**

That is `sampling variability`, and it is worth having. It tells you that +1.8 is not pinned down to the decimal, and that a claim of "the bias is 1.8" overstates what 24 events support.

### What it does not cover

Everything Part I found.

**Chapter 1's conditionality.** The demand forecast is conditional on no new conservation request. Three of the 24 events had one in force. Their errors are in the average, and the interval says nothing about it.

**Chapter 4's residual.** One zone's demand figure was never measured; it is a subtraction residual containing leakage elsewhere and water the utility used itself. Every "actual" in the record inherits that.

**Chapter 5's missing spill term.** The storage model that turns demand into a breach probability grows water without limit under low demand. The interval on the demand error is silent about it.

**Which events were logged.** Twenty-four is the count of events somebody recorded as heat events. Chapter 4's whole subject.

**And the SCADA replacement**, which changed what "actual demand" was measured by, partway through.

**The interval is a statement about sampling. It looks like a statement about the answer.** That gap is the section's subject, and it is why the enumeration above is worth writing out in a real report rather than leaving to a reader's imagination.

And the enumeration is not a hedging exercise. Each item on it is a **specific, checkable, potentially fixable** thing:

| What the interval omits | What could be done about it |
|---|---|
| Three events had a conservation request in force | exclude them, and report both ways |
| One zone's demand is a subtraction residual | ask what share of the total it is |
| The storage model has no spill term | add one; it is an afternoon's work |
| Only logged events are counted | ask how events came to be logged |
| The SCADA changed partway | split the record and look — §7 does |

**Compare that with "there is additional uncertainty not captured by the interval."** The sentence is true, appears in a great many reports, commits to nothing, and could not be acted on by anybody. The list can be worked through in a week.

Chapter 5 made this distinction its central discipline: criticism that names what would settle it, against doubt that applies to any analysis in any field. The enumeration above is criticism. The hedging sentence is doubt.

Chapter 4 supplied the general form of the point: for a dataset with a defect, what matters is a term whose expression **does not contain the number of records you collected at all** [@meng2018paradox, p. 687]. The interval shrinks as records accumulate. The other terms do not.

### And what a reported interval is not

One misinterpretation is worth stating flatly, because nearly everyone holds it.

> *There is a 95% chance the true value lies between 0.84 and 2.76.*

The source's response is short.

> "No! A reported confidence interval is a range between two numbers." [@greenland2016misinterpretations, p. 343]

The 95% is a property of the **procedure** — of how often intervals built this way would cover the estimand, across repeated application. Your interval is two numbers. It either contains the estimand or it does not.

**Third time this chapter, and the third time in three chapters.** Calibration over a record. Balance over replications. Coverage over repeated construction. The property lives in the ensemble; the thing in front of you is one member of it.

### Now repair Chapter 6

Chapter 6 assumed ±0.6 ML per day, independent across seven days. That implies a spread on the weekly total of about **0.92 ML**, centred on the forecast of 64.9.

The record says two things about that.

**The spread is far too small.** The observed spread of weekly errors is **2.4 ML** — about **2.6 times** larger.

**And there is an offset Chapter 6 assumed away entirely.** The mean error is `+1.8`, not zero. A symmetric spread around the forecast is not what the record shows.

Chapter 6's breach condition was that weekly demand exceeds **64.2 ML**. Run it four ways.

| Assumption about weekly demand | Centre | Spread | P(breach) |
|---|---:|---:|---:|
| Chapter 6 as written | 64.9 | 0.92 | **77%** |
| Fix the spread only | 64.9 | 2.4 | **62%** |
| Fix the offset only | 66.7 | 0.92 | **over 99%** |
| Fix both | 66.7 | 2.4 | **85%** |

### Pause: why did the answer go down?

Before reading on, write two or three sentences.

> Widening the spread from 0.92 to 2.4 — admitting far more uncertainty than Chapter 6 assumed — moved the breach probability from **77% down to 62%**.
>
> **Why?**

---

Because the threshold sits **below** the centre.

A breach happens when demand exceeds 64.2. The central forecast is 64.9. The utility is already expected to breach — the central case is on the wrong side of the line.

Spreading the distribution moves mass in both directions. With the threshold below the centre, more of the new mass lands on the safe side than on the unsafe side, so the computed probability falls.

**Admitting more uncertainty made the situation look better.**

That is worth sitting with, because "we widened the interval to be conservative" is something people say, and they say it believing that widening is always the cautious direction. It is not. Whether a wider spread raises or lowers a threshold probability depends entirely on which side of the threshold your centre sits, and nobody checks.

### And correcting one thing was worse than correcting neither

Look at the table again.

Chapter 6's uncorrected answer was **77%**. Correct only the spread and you get **62%** — further from the honest answer than where you started, and wrong in the reassuring direction. Correct only the offset and you get **over 99%** — a near-certainty that overstates the case badly.

The honest figure is **85%**, and it requires both corrections.

**A partial repair is not a partial improvement.** The two errors in Chapter 6's assumption were pushing in opposite directions and partly cancelling. Fixing the one that was easier to notice — the spread, which is what "uncertainty" makes people think of — left the other running unopposed.

And note which of the two an analyst is more likely to fix. Spread is what the word *uncertainty* means to most people. An offset in the centre of a forecast is a bias, which is Chapter 3's subject and does not feel like uncertainty at all.

**Chapter 3 drew exactly this line and the anchor has now walked into it.** Precision is about spread; trueness is about where the centre sits; and more of the first does nothing for the second. Chapter 3 said it of an instrument. Here the same separation applies to a forecasting process, and the analyst repairing "uncertainty" fixed the precision term and left the trueness term running.

Anyone who wants a single sentence to carry out of this section:

> **Widening is not caution, and precision is not trueness.**

### So what should the utility actually report?

Having spent six pages on what a number does not say, the constructive form is worth writing out, because "report it carefully" is not an instruction anybody can follow.

> **About 85%.** That is the probability that end-of-week storage falls below the 4.5 ML reserve, given the Chapter 1 seven-day forecast, the record of 24 past heat events, and the storage model as it stands.
>
> The forecast errors on those 24 events run **low by about 1.8 ML** on the week, with a spread of **2.4 ML**. Both corrections matter and they pull in opposite directions: using the observed spread alone would give 62%, and correcting the offset alone would give over 99%.
>
> The interval around the 1.8 — **0.84 to 2.76** — covers only how much that average would move on another 24 events. It does not cover the fact that three of the 24 had a conservation request in force, that one zone's demand figure is a subtraction residual, that the storage model has no spill term, or that the recording system changed partway through the record. **The last of those is checkable this week and has not been checked.**

Four short paragraphs. It contains a number, what the number is conditional on, what the alternatives would have given, what is not covered, and one item somebody can act on tomorrow.

**Compare it with "about 77%, plus or minus a bit."** That sentence is shorter, was what the utility had, and is wrong in the reassuring direction by eight percentage points for reasons nobody could have recovered from it.

### Fifth time

Chapter 3: more measurements improve precision, not trueness. Chapter 4: more records shrink sampling variability, not the data-quality term. Chapter 6: more runs shrink Monte Carlo error, not model error. Chapter 7: more sample size does not touch sensitivity to causal assumptions.

Chapter 8 adds the fifth in the plainest form yet: **more heat events narrow the interval and do nothing about the five items enumerated earlier in this section.**

The rule stands as Chapter 6 stated it and Chapter 7 sourced it. When told more of something will fix a problem, ask which term it enters.

### One more thing the interval does not do

It does not get wider when the model is wrong.

That sounds obvious stated flatly and it is the source of a great deal of misplaced comfort. An interval computed under a false assumption is not a wide interval; it is a **confidently wrong narrow one**. The arithmetic has no channel through which a broken assumption could widen it, because the assumption is what the arithmetic is conditional on.

So the mental image most people carry — that a badly specified analysis will at least announce itself through large uncertainty — is backwards. §4's own case demonstrates it: Chapter 6's spread was 2.6 times too narrow *and* centred in the wrong place, and the simulation it fed produced a perfectly stable 77% with no sign of distress anywhere.

**Wrongness is silent. Only checking is audible**, which is §7.

### Task: both one-sided corrections

Using Chapter 6's breach threshold of **64.2 ML** and the record's mean error of **+1.8 ML**:

1. Confirm the direction of each of the four rows in the table without recomputing them — reason from where the centre sits relative to the threshold.
2. Suppose the threshold had been **66.0 ML** instead of 64.2. Which way would widening the spread have moved the answer then? Say why in one sentence.
3. Write the sentence you would put in a briefing note to report the 85%, including everything it is conditional on.

Question 2 is the one that installs the habit. The direction is not a property of widening; it is a property of where you are relative to the line.

## 5. The Threshold Ritual

The book's description of this chapter contains a phrase that is a standing instruction: teach this material **without reducing evidence to threshold rituals**.

So the ritual has to be named.

### What a P value is

Start with the quantity itself, because the objection that follows is not to the quantity.

> "The P value is then the probability that the chosen test statistic would have been at least as large as its observed value if every model assumption were correct, including the test hypothesis." [@greenland2016misinterpretations, p. 339]

The same page offers a framing worth carrying: a P value is a statistical summary of the **compatibility** between what you observed and what the entire model predicts you would observe.

**Compatibility.** Not truth, not probability of a hypothesis, not importance. How well the data sit with a whole set of assumptions.

And by §3's spine, that set includes how you conducted the analysis.

The word is doing careful work and it is worth unpacking once. *Compatible* is a relation between two things — these data, and what this model predicts. It is not a property of either alone. A large value means the data sit comfortably with the model; a small one means they do not. Neither statement is about the world; both are about the fit between an observation and a set of assumptions, one of which happens to be the thing you cared about.

**Which is why the quantity cannot bear the weight routinely placed on it.** A relation between data and a model is being asked to answer a question about whether an effect is real, and there is no route from the first to the second that does not pass through every other assumption in the model.

### The discipline's own position

In March 2016 the American Statistical Association released a statement on statistical significance and P values. Its press release prints six principles.

> 1. "P-values can indicate how incompatible the data are with a specified statistical model."
> 2. "P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone."
> 3. "Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold."
> 4. "Proper inference requires full reporting and transparency."
> 5. "A p-value, or statistical significance, does not measure the size of an effect or the importance of a result."
> 6. "By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis."
>
> [@asa2016pvalue]

**A note on this source.** What was obtained and read is the ASA's own press release, which prints the principles in full. The statement article itself, which contains short paragraphs elaborating on each, could not be obtained, and nothing in this book characterises those paragraphs.

**Principle 4 is the one to notice.** *Proper inference requires full reporting and transparency* is the same claim §3 took from a methods paper — that how the analysis was conducted is part of what makes the number mean anything — arriving from the discipline's own institution.

It is worth reading the six as a group rather than as a list, because of what they are collectively doing.

**One is the only positive claim.** It says what the quantity can do, and it is carefully bounded: indicate incompatibility, with a *specified statistical model*.

**Two, five, and six say what it is not.** Not a hypothesis probability. Not an effect size. Not, by itself, a good measure of evidence.

**Three says what not to do with it.** Not the basis of a conclusion or a decision on its own.

**Four says what else is required**, and is the only one that is about the analyst rather than the statistic.

So five of six are restrictions, and the professional body issuing them is the one whose members compute the quantity. That is not a fringe critique; it is a discipline putting a warning label on its most-used output.

### The ritual

> "Too often, however, the P value is degraded into a dichotomy in which results are declared 'statistically significant' if P falls on or below a cut-off (usually 0.05) and declared 'nonsignificant' otherwise." [@greenland2016misinterpretations, p. 339]

**Degraded into a dichotomy.** A continuous measure of compatibility, computed from data and a model, is replaced by one of two words.

The same paper's closing substantive sentence is as strong as methodological writing gets:

> "we join others in singling out the degradation of P values into ''significant'' and ''nonsignificant'' as an especially pernicious statistical practice" [@greenland2016misinterpretations, p. 348]

### Four misreadings, each one you have met before

The paper lists twenty-five. Four are worth your time, because each is something this book has already taught you in another setting.

**It is not the probability the hypothesis is true.**

> "The P value assumes the test hypothesis is true—it is not a hypothesis probability and may be far from any reasonable probability for the test hypothesis." [@greenland2016misinterpretations, p. 340]

And the related version, on the same page: to claim the P value is the probability that chance alone produced the observed association "is completely backwards: The P value is a probability computed assuming chance was operating alone."

**This is Chapter 6's inversion.** The number is computed *given* the hypothesis; it is being read as a statement *about* the hypothesis. Two chapters ago the vehicle was influenza and fever. Here it is the most cited statistic in science.

**A small value does not mean the hypothesis is false.** The paper's wording carries comparison symbols that this book cannot reproduce reliably, so the point is paraphrased: a small value flags the data as unusual *if every assumption held*, and may be small because some assumption other than the hypothesis failed [@greenland2016misinterpretations, p. 341].

**A large value does not mean there is no effect.** Paraphrased from the same page: unless the point estimate is exactly the null value, some association is present in the data, and it is a mistake to report "no association" or "no evidence" on the strength of a large P value; you have to look at the point estimate to see which effect sizes are most compatible with what you saw.

**This is Chapter 5.** Absence of a failed check is not evidence of adequacy. A check that did not fail establishes only that it did not fail.

**A reported interval is not a probability statement.** Misinterpretation 19, quoted in §4 above: "No! A reported confidence interval is a range between two numbers" [@greenland2016misinterpretations, p. 343].

### The escape route, closed

The reasonable response to all this is to stop reporting P values and report intervals instead. The source anticipates it and refuses it.

Intervals rest on the same model, under the same assumptions, including the same assumption about analytic conduct. The paper notes that the exclusive focus on null hypotheses "obscures the close relationship between P values and confidence intervals, as well as **the weaknesses they share**" [@greenland2016misinterpretations, p. 340].

And reading whether an interval covers zero is the ritual with a longer name:

> "confidence intervals force the 0.05-level cutoff on the reader … and in this way are as bad as presenting P values as dichotomies." [@greenland2016misinterpretations, p. 344]

There is a real advantage to intervals, and it is narrower than the escape route imagines: many authors prefer them "because they allow one to shift focus away from the null hypothesis, toward the full range of effect sizes compatible with the data" [@greenland2016misinterpretations, p. 344]. That is an advantage about **where attention goes**. It is not a claim that the number rests on less.

### And overlapping intervals are not agreement

A related habit, worth killing on sight, is comparing two intervals by eye and concluding they agree if they overlap.

The source gives a worked case. Two 95% intervals, `(1.04, 4.96)` and `(4.16, 19.84)`, overlap — and the test of the hypothesis of no difference between them gives `P = 0.03` [@greenland2016misinterpretations, p. 344].

The eyeball test is not a test. Comparing two things requires a statistic about the comparison, not two statistics about the things.

### One instance that is not academic

It would be easy to read all of this as methodologists quarrelling about conventions.

One guideline records otherwise:

> "statistical significance is neither necessary nor sufficient for determining the scientific or practical significance of a set of observations. This view was affirmed unanimously by the U.S. Supreme Court, (Matrixx Initiatives, Inc., et al. v. Siracusano et al. No. 09–1156. Argued January 10, 2011, Decided March 22, 2011)" [@greenland2016misinterpretations, p. 347]

**A unanimous supreme court, in a securities case, on the record.** The judgment itself was not read for this book and nothing here describes its reasoning — it is reported as the source reports it. But the fact of it is enough to answer a reader who thinks the argument is confined to journals.

### Why the ritual survives

Not because anyone defends it intellectually. The ASA release quotes the mechanism directly:

> "Over time it appears the p-value has become a gatekeeper for whether work is publishable, at least in some fields… This apparent editorial bias leads to the 'file-drawer effect,' in which research with statistically significant outcomes are much more likely to get published, while other work that might well be just as important scientifically is never seen in print." [@asa2016pvalue]

**The mechanism is institutional, not intellectual.** Which matters for what you do about it, because arguments do not fix incentives. In your own organisation the equivalent question is what gets a finding into the pack that goes to the board — and it is usually a threshold nobody has ever written down.

### What to do instead

The source's guidelines, quoted:

> "Correct and careful interpretation of statistical tests demands examining the sizes of effect estimates and confidence limits, as well as precise P values (not just whether P values are above or below 0.05 or some other threshold)." [@greenland2016misinterpretations, p. 347]
>
> "Careful interpretation also demands critical examination of the assumptions and conventions used for the statistical analysis—not just the usual statistical assumptions, but also the hidden assumptions about how results were generated and chosen for presentation." [@greenland2016misinterpretations, p. 347]
>
> "It is simply false to claim that statistically nonsignificant results support a test hypothesis, because the same results may be even more compatible with alternative hypotheses—even if the power of the test is high for those alternatives." [@greenland2016misinterpretations, p. 347]
>
> "Any opinion offered about the probability, likelihood, certainty, or similar property for a hypothesis cannot be derived from statistical methods alone." [@greenland2016misinterpretations, p. 347]

The second of those is §3's spine, for the third time from a third direction.

### What this looks like in an organisation that has never heard of the debate

None of the above requires anybody to be doing science. The ritual has an operational form and you will recognise it.

A dashboard shows a metric in red or green against a target. A monthly pack reports whether a change was "material". A supplier's report says a difference was "within tolerance". A safety review records that a trend was "not statistically significant".

**Every one of those is the same move**: a continuous measure of how things stand, replaced by one of two words, with the number that generated it no longer available to the person deciding.

And the operational versions are frequently worse than the academic ones, because the threshold is usually undocumented. Nobody can tell you why the tolerance is what it is, when it was set, or by whom. It is inherited, and inherited thresholds are the hardest kind to question because there is no author to ask.

**The recoverable move is the same in all of them.** Ask for the number the verdict was computed from, and ask what the verdict would have been just either side of the threshold. If a small change in an arbitrary line flips the sentence, the sentence was never carrying the information.

### Two things this chapter is not claiming

**Not that P values are worthless.** Principle 1 says they can indicate incompatibility between data and a model, which is a real service. The objection is to the dichotomy, not the quantity, and the first guideline explicitly asks for precise values to be examined.

**Not that the field has agreed on a replacement.** The paper offers its guidelines "in the hopes of minimizing harms of current practice", which is not the language of a settled alternative. Anyone selling you one is ahead of the evidence.

## 6. Four Defensible Analyses

Nobody in this section does anything wrong. That is the section.

### The choices

The utility has 24 heat events. An analyst is asked for the mean forecast error, and faces choices.

**Should events with a conservation request in force be included?** Chapter 1 established that the demand forecast is conditional on **no new action**. Three of the 24 events had a request in force, so their forecasts were answering a question the situation had already invalidated. There is a strong argument that those three do not belong.

**Should events before the SCADA replacement be included?** The system that records actual demand was replaced partway through the period. Ten of the 24 events predate it. There is a strong argument that "actual demand" does not mean the same thing across the changeover.

**Should longer events count for more?** A ten-day heat event and a four-day one both contribute one error to the average. There is a strong argument for weighting by length.

Each of those is defensible. Two of them are arguably **required** rather than optional.

### Four answers

| Analysis | n | Mean error | Standard error |
|---|---:|---:|---:|
| All events | 24 | **+1.8** | 0.49 |
| Excluding conservation events | 21 | **+2.4** | 0.50 |
| Only events since the new SCADA | 14 | **+1.1** | 0.70 |
| Weighted by event length | 24 | **+2.0** | 0.51 |

Four numbers from one record, and the analyst who produces any of them can defend it in a meeting.

Note also that the two "required" exclusions cannot both be taken without consequence. Excluding conservation events **and** restricting to post-SCADA leaves a handful, and an analyst who did both would be criticised for a tiny sample by the same people who asked for both exclusions.

### And now the ritual

Run each through the conventional threshold.

| Analysis | Crosses the threshold? | The sentence it licenses |
|---|---|---|
| All events | yes | "The forecasts are significantly biased low." |
| Excluding conservation | yes | "The forecasts are significantly biased low." |
| Since the new SCADA | **no** | "No significant evidence of bias." |
| Length-weighted | yes | "The forecasts are significantly biased low." |

**The same 24 records support both conclusions**, depending on a choice nobody wrote down in advance.

### Pause: what did the dichotomy destroy?

Before reading on, write two or three sentences.

> Look at the four estimates: **+1.1, +1.8, +2.0, +2.4**.
>
> Now look at the four verdicts: significant, significant, not significant, significant.
>
> **What has the second row thrown away?**

---

**The four estimates do not disagree.**

They are all positive. They are all between one and two and a half. They all say the forecasts run low, by an amount in the same range, and any one of them would lead to the same operational response.

**The disagreement is manufactured entirely by the dichotomy.**

The post-SCADA analysis has fourteen events instead of twenty-four. A smaller record gives a larger standard error, which pushes the verdict across a line — and the line converts *slightly less precisely estimated* into *no evidence*, which is a different sentence about a different world.

Nothing about the world changed between rows three and one. What changed was the count.

### Which is why analytic conduct is inside the model

§3 quoted a source putting the conduct of the analysis among a computed number's assumptions, alongside independence and the rest. This is what that means in practice.

An analyst who ran all four analyses, saw the four verdicts, and reported the one that suited them has violated an assumption of the calculation as surely as if they had ignored a dependency in the data. The number they report is no longer a compatibility summary, because the assumption that intermediate results were not used to choose what to present is false.

**And the analyst need not be dishonest for this to happen.** The far more common route is that the analyst runs one analysis, gets a verdict, and never learns that three other defensible ones existed. The flexibility is exercised without anyone noticing there was a choice — which is worse, because there is nothing for anybody to disclose.

Think about how the single analysis actually gets chosen.

The analyst opens the record and sees a column flagging conservation requests. If the flag is prominent, they exclude those events; if it is buried in a notes field, they do not. The SCADA changeover is not a column at all — it is something you know if you have worked there five years. Event length is in the data but summing it takes an extra step.

**So the analysis that gets run is the one the data made easiest**, and the choices that were never noticed are indistinguishable, from the outside and from the inside, from choices that were considered and rejected.

That is a more uncomfortable picture than deliberate selection, because there is no moment at which anybody could have behaved better. It is also the reason the remedy below is about **running more analyses** rather than about declaring intentions.

**This book demonstrates the phenomenon on its own case.** There is a well-known study in which many independent teams analysed the same dataset and reached different answers; it could not be obtained for this book, and nothing here describes it. The four analyses above are the utility's, and they make the point without borrowing anyone's authority.

### What preregistration does and does not fix

The obvious remedy is to write the analysis down before seeing the data.

**It does help**, and specifically: it removes the route where a result is chosen after the fact. That is a real category of failure and preregistration closes it.

**It does not fix three things**, and they are visible in this case.

**It cannot anticipate what you did not know.** Nobody could have preregistered a decision about the SCADA changeover without already knowing there had been one and that it mattered. The choice that flips the verdict here is exactly the kind that surfaces during analysis.

**It does not make any of the four choices correct.** A preregistered decision to use all 24 events is still a decision to average across a measurement changeover. Committing in advance to a defect commits you to the defect.

**And it does nothing about the choices nobody sees.** The dominant failure in ordinary practice is not choosing among alternatives; it is running the one analysis that occurred to you.

The more useful discipline is cheaper and less celebrated: **run several defensible analyses and report all of them.** Four rows in a table. If they agree, you have said something robust. If they disagree, you have found something worth understanding, which is the more valuable outcome and the one a single analysis hides.

Two objections arrive immediately and both have answers.

**"It looks indecisive."** It looks like what the evidence supports. And the four rows in the anchor's table are not indecisive at all — they agree in direction and in rough magnitude, which is a *stronger* statement than any one of them. The row that would look indecisive is a single number reported without its alternatives, and it only looks decisive because the alternatives are absent.

**"It gives people something to argue with."** Yes. That is the function. A colleague who prefers the post-SCADA subset can now say so and defend it, which is a conversation about the SCADA changeover — a real thing, knowable by asking. Reporting one number moves the same disagreement underground, where it emerges six months later as distrust of the analysis team.

And the practical form is small. **A table with one row per defensible choice, and a sentence saying which you would use and why.** Not a research programme. An afternoon.

### One more feature of the anchor's four

Look again at which analysis produced the dissenting verdict.

It was the **post-SCADA** one — fourteen events instead of twenty-four. And §7 will show, by a check that takes two subtractions, that the post-SCADA events genuinely differ from the earlier ones: `+1.1` against `+2.78`.

So the analysis that failed to cross the threshold is, on the evidence, arguably **the most defensible of the four** — it is the one that avoided averaging across a measurement changeover.

**The dichotomy therefore punished the best analysis.** Not by being wrong about it, but by converting *fewer events, therefore a wider standard error* into *no evidence of bias*, when the estimate it produced was `+1.1` and every other analysis agreed on the direction.

That is the failure mode in its sharpest form: **the threshold rewards sample size and calls it evidence.** An analyst who wanted a significant result had a straightforward route available — use all 24 events and do not mention the SCADA — and it required no dishonesty at all, only not looking.

### And a word about what this is not

This section is not an accusation, and a reader who takes it as one will draw the wrong conclusion.

Nothing here says analysts are dishonest, or that quantitative work is unreliable, or that a result you cannot reproduce four ways should be discarded. The four analyses in the table are all competent. The person who ran one of them and reported it did the job they were asked to do, in the time they were given, with the data they had.

**What the section says is narrower and more useful: one analysis of a record is one draw from a set of defensible analyses, and you cannot tell from the number which draw you got.**

The response is not suspicion. It is a habit that costs an afternoon — run the alternatives, put them in a table, and say which you would use. An organisation where that is normal has removed the failure mode entirely, and nobody had to be accused of anything.

### Task: produce a fifth

The four analyses above are not exhaustive.

1. Produce a **fifth defensible analysis** of the same 24 events. Say what it does and why somebody would defend it.
2. Predict whether it would cross the threshold, and say what your prediction rests on.
3. Then answer the question that matters: **would you report your fifth analysis if it agreed with the others, and would you report it if it did not?**

Question 3 is uncomfortable on purpose. Most people answer it differently for the two cases, and the difference is the whole subject of this section.

## 7. Checking the Assumptions You Were Not Interested In

§3 established that a computed number is a statement about an entire model. **Model checking** is the practice of examining the parts of that model you were not thinking about.

### One thing that is not a check

Chapter 5 already established this and it is worth restating because the temptation is strong.

Showing that a model reproduces the data it was built from is not a check. It is close to guaranteed, it could not have come out the other way, and by Chapter 5's own test a check that could not have failed establishes nothing.

**The utility's demand model has never been checked in any other way**, and the sentence in its documentation reads that it "reproduces observed demand to within 3% over the fitting period". That sentence is verification — the arithmetic works — presented as though it were evidence that the model is right.

### A check that took two subtractions

Here is one the utility could have run at any point in twelve years.

The interval in §4 treats the 24 errors as draws from one stable process. Test that assumption by splitting the record at the SCADA changeover.

Fourteen events since the changeover have a mean error of **+1.1 ML**.

The other ten therefore have a mean of:

`(24 × 1.8 − 14 × 1.1) ÷ 10 = (43.2 − 15.4) ÷ 10 = ` **+2.78 ML**

**+1.1 against +2.78.** The two halves of the record differ by more than the whole interval in §4 was wide.

That interval assumed one process. The record contains at least two.

**What this establishes and what it does not.** It establishes that the errors are not exchangeable draws from a single stable process, which is enough to invalidate the interval as stated. It does **not** establish that the SCADA replacement caused the difference — that is a causal claim, Chapter 7's subject, and this record cannot support it. The change could be the recording system, or the weather in the two periods, or the forecasting team, or three things at once.

**The check is two subtractions and a division.** It cost nothing, it could have failed, and it changes what can honestly be reported. That combination — cheap, falsifiable, consequential — is what makes a check worth running, and Chapter 5 gave you the same three criteria for its four cheap checks.

Applied as a filter, those three criteria dispose of most of what passes for checking.

**Cheap.** If a check needs a week, it will not be run under deadline, and a check that is not run is not a check. The most valuable ones in this book have all been arithmetic: a division in Chapter 5, a ratio in Chapter 6, two subtractions here.

**Falsifiable.** There has to be a result that would have embarrassed you. Ask, before running it, what outcome would make you change the report. If there is none, you are producing reassurance.

**Consequential.** The embarrassing result has to matter. A check that could fail and would change nothing if it did is a hobby.

**The utility's 3% fit figure fails the second and passes the other two**, which is precisely why it survives in the documentation: it is cheap, it sounds consequential, and it cannot fail.

### The check that has never been run

The stronger form is to check the model against data it was not fitted to.

Hold back the most recent events. Build the interval from the rest. Then see how the held-out events fall relative to it — and do it as a record rather than as a single case, because a property defined over an ensemble cannot be read off one instance, as this book has now said three times.

**This is Chapter 6's machinery, unchanged.** Chapter 6 assessed a forecaster by grouping forty briefings and comparing what was said against what happened. The same two properties apply: whether the intervals cover at about the rate they claim, which is calibration, and how narrow they are while doing so, which is sharpness. The stated goal there was "to maximize the sharpness of the predictive distributions subject to calibration" [@gneiting2007scoring, p. 359], and nothing about it changes when the object being assessed is an interval rather than a probability.

An interval procedure that covers ninety-five times in a hundred and is four ML wide is doing its job. One that covers ninety-five times in a hundred by being twenty ML wide is technically calibrated and useless — which is Chapter 6's always-45% forecaster, wearing a different hat.

The utility's version, concretely.

Take the fourteen post-SCADA events. Build the interval from the first ten. Then look at where the last four actually fell relative to it. Repeat, moving the cut-off forward: build from eleven, check the twelfth; build from twelve, check the thirteenth.

**Now you have a small record of predictions and outcomes**, which is the only object that can be assessed, because coverage is a property over repeated construction and cannot be read off one interval.

Three or four checks is a thin record and will not settle much — Chapter 6's forty briefings were barely enough. But three is not zero, it accumulates, and every heat event from now on adds a row. **The reason the utility has none is that nobody started**, which was Chapter 6's finding about forecasts and is the same finding about intervals.

And notice what this check can catch that no amount of internal inspection can. If the model is systematically over-confident — intervals too narrow, covering far less often than they claim — that shows up immediately in the held-out record and is invisible in every calculation performed on the fitting data.

### Pause: which of these could have failed?

Before reading on, write two or three sentences.

> Three checks have been mentioned in this section:
>
> 1. the model reproduces observed demand to within 3% over the fitting period;
> 2. the record splits into two halves with different mean errors;
> 3. held-out events fall inside the intervals at about the claimed rate.
>
> **Which of them could have come out the other way, and what does each one therefore establish?**

---

**The first could not.** The model was fitted to that period. Reproducing it was close to guaranteed, and a result that could not have been otherwise carries no information about whether the model is right. It establishes that the arithmetic runs.

**The second could, and did.** The two halves could have come back at +1.7 and +1.9, in which case the exchangeability assumption would have survived a genuine attempt to break it. They came back at +1.1 and +2.78. It establishes that a stated assumption of the interval is false.

**The third could, and has not been run.** It is the strongest of the three because the held-out events had no opportunity to influence the model, and it is the only one that speaks to whether the intervals mean what they claim.

**Rank checks by what they could have shown, not by how impressive they look.** The 3% figure is the most precise-sounding thing in the utility's documentation and the least informative.

### Why checking loses to computing

If the checks are this cheap and this informative, the honest question is why organisations do not run them.

**Nothing asks for them.** A report has a section for results and no section for what was checked. Adding one is a change to a template, and templates are owned by nobody.

**They produce bad news at the worst time.** The split-half check is most useful just before publication and its result is that the interval you have already circulated is wrong. There is no moment at which running it is convenient.

**And a failed check has no natural home.** A finding goes in the results. A confirmed assumption goes nowhere. A *broken* assumption is neither a result nor a caveat, and most report structures have no place to put it, so it becomes a verbal comment in a meeting and evaporates.

**The fix is structural rather than exhortative.** Give the report a section headed *what was checked and what it showed*, with a row per check and a column for what the check could have shown. It is three lines of template and it makes the absence of checking visible, which is the only thing that reliably causes checking.

### Sensitivity analysis, arriving as promised

Chapter 5 said something about sensitivity analysis and deferred it here.

> *Sensitivity analysis is a genuine and valuable technique and it belongs to Chapter 8. It is not criticism, and offering it as the criticism section is the most sophisticated-looking way to skip this chapter entirely.*

Here it is, in its proper place. Vary an input across a range and see how far the answer moves. On the anchor: vary the assumed spread from 0.9 to 2.4 and watch the breach probability move from 77% to 62%; vary the offset from 0 to +1.8 and watch it move to 85%.

**That is exactly what §4 did**, and it is a model check: it tells you which assumptions the answer is sensitive to, which is where checking effort should go.

**And Chapter 5's limit still applies without modification.** Varying inputs inside a formulation cannot see the formulation. No amount of varying the spread reveals that the storage model has no spill term, because the spill term is not an input — it is a missing piece of structure. Sensitivity analysis tells you which of the assumptions you have made matter. It is silent about the ones you have not made and should have.

Robustness in the decision sense — choosing an action that performs acceptably across a range of assumptions rather than optimally under one — is a different subject and belongs to Chapter 12.

### A short list of checks worth having

Not exhaustive, and all of them cheap. Each is here because it can fail.

**Split the record.** By time, by site, by whoever collected it. If the halves disagree by more than your interval is wide, the assumption of one process is gone.

**Hold something out.** Fit on part, check on the rest, and keep the results as a record rather than as a single verdict.

**Change one defensible choice and rerun.** §6's four analyses are a model check as much as an integrity exercise: if the answer swings on an arbitrary choice, that is information about the answer.

**Push an input to a limit.** Chapter 5's extreme-condition check. What does the storage model do under zero demand for a week? It grows water without limit, because it has no spill term — which is how Chapter 5 found that in the first place.

**Predict something you have not seen.** The strongest form, and the one that requires waiting.

**Ask somebody who was there.** Not a statistical check, and it catches more than any of the above. The SCADA changeover is not in the data.

**Every one of those has a result that would embarrass the model.** That is the property they were selected for, and it is the only property that matters.

### Measurement error, in one paragraph

One assumption in every model of this chapter has gone unexamined: that the recorded numbers are the quantities they are labelled as.

Chapter 3 established that they are not, in general — that a measurement has trueness and precision, that a calibrated instrument still gives readings with error, and that resolution is not accuracy. Chapter 4 established that one of the utility's demand figures is a subtraction residual that was never measured at all.

**Both of those are inside the model that produced the +1.8**, and neither appears in the interval. Correcting for measurement error, when its size is known, is machinery this book does not teach and routes to the depth curriculum. Knowing that the correction is missing costs nothing and changes what you should write.

### Task: diagnose five defects

Each statement below contains one defect. Write the defect, what it stops you concluding, and a repair.

1. *"The 95% interval is 0.84 to 2.76, so we're 95% sure the true value is in there."*
2. *"We widened the interval to be conservative."*
3. *"P was 0.31, so there's no bias in the forecasts."*
4. *"We tried several specifications and are reporting the cleanest."*
5. *"The model fits the last five years to within 2%, so it's been checked."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

## 8. Cold-Start Practice and Retrieval

### Return to your six-minute answer

Find what you wrote at the start of §1, about where the ±0.6 should have come from.

Read it against what you can now produce. Do not score it.

- Did you say what you would **compute**, or only that you would look at historical data?
- Did you anticipate a **systematic offset**, or only a spread?
- Did you say what your number would be **conditional on**?

Three patterns are common.

Most readers write that they would compute the historical variation. That is right and it is half — the record's biggest surprise was not the size of the spread but the fact that the forecasts were centred in the wrong place, and a reader who thought only about spread would have produced §4's 62% and reported it as a repair.

Some readers write that they would take a wider spread to be safe. §4 was aimed at exactly that instinct, and it moved the answer in the reassuring direction.

Some write that the historical record might not represent the future. That is the strongest opening answer and it is §3's and §7's subject — the next question is *which assumption*, and the record itself can answer some of them.

### Independent transfer

Now work an unfamiliar situation, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below. Open only that one.

- [Form A — A grid operator's transformer failure record](transfer-form-a.md)
- [Form B — A charity's donation-response record](transfer-form-b.md)

Allow about **50 minutes**.
Every fact you need is supplied. Do not look anything up.

Do not open the other form. You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the procedure from memory

Before looking back, write down how you would examine a reported estimate.

Aim for the sequence, not the wording.

1. What is the **estimand** — what quantity is this a number about?
2. What **procedure** produced it, and on which records?
3. What is the estimate **conditional on** that is not a statistical assumption?
4. What does the interval **cover**? Sampling variability, and what else?
5. What does it **not** cover? List it from the record's own history.
6. Is the centre on the safe or unsafe side of any threshold that matters?
7. **How many defensible analyses does this record support?** Produce two more.
8. Do the alternatives disagree in **direction**, or only in whether they cross a line?
9. What check has been run that **could have failed**?
10. What would a check against data the model was not fitted to look like, and has anyone done it?

Step 3 is the one that is skipped, and skipping it is how an interval becomes a statement about the answer.

Step 7 takes twenty minutes and finds more than any amount of scrutiny of the first analysis.

Step 9 is the question that separates checking from reassurance.

### The three sentences worth memorising

Most of this chapter reduces to three claims, and a reader who retains only these has the useful part.

> **An estimate is conditional on a whole model, and the model includes how the analysis was conducted.**

> **An interval covers sampling variability and nothing else, and it does not get wider when the model is wrong.**

> **A threshold verdict discards the number that generated it, and the number is what you needed.**

Each of the three has an operational form, which is what you actually do on a Tuesday.

For the first: **write down what the number is conditional on**, including at least two things that are not statistical assumptions.

For the second: **enumerate what the interval omits**, as a list of specific checkable items rather than a sentence about additional uncertainty.

For the third: **ask for the number behind the verdict**, and ask what the verdict would have been just either side of the line.

### If the transfer went badly

- **You accepted the interval as the uncertainty.** Reread §4. The interval covers sampling variability under a model, and the model is the thing in question.
- **You argued about the threshold verdict.** The verdict is not the problem; having a verdict is. Report the estimates.
- **You produced no alternative analyses.** This is the most common failure and the easiest to fix. Every record supports several; find two.
- **You attributed an estimator property to a number.** "An unbiased estimate" is a category error, and §2 was aimed at it.
- **You proposed a check that could not have failed.** Fit to the fitting period is the usual one. Ask what result would have embarrassed the model.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Do not reread this chapter immediately beforehand, and do not look at the form you have not done.

### What this chapter did not give you

**How to derive anything.** No estimator was derived, no interval formula stated, no standard error computed from first principles. That machinery is real and it is depth curriculum, and this chapter told you where it lives rather than gesturing at it.

**Any test procedure.** No test was performed anywhere in this chapter. The threshold verdicts in §6 were reported as verdicts, not computed for you, because computing them would have taught the ritual while criticising it.

**Regression.** Named once, as a model whose assumptions are the thing under discussion. Not taught.

**Measurement-error correction.** Named as missing, in §7, and not supplied.

**Whether the field has an agreed replacement for the ritual.** It does not, and the source that criticises the ritual most sharply offers guidelines rather than a substitute.

**And nothing about combining evidence.** Which is the next chapter.

### What the book has now finished saying about numbers

Chapter 8 closes Part II's arc on quantities, and it is worth seeing the arc whole, because each chapter added the same kind of clause to a different object.

**Chapter 6:** a probability is not high or low on its own — it is relative to stated information.

**Chapter 7:** a causal quantity is not identified on its own — it is identified relative to stated assumptions.

**Chapter 8:** an estimate is not accurate on its own — it is conditional on an entire model, including how the analysis was conducted.

Three chapters, three objects, one demand: **say what it is relative to.** And Part I made the same demand of adequacy, validity, trustworthiness, and criticism.

That is eight chapters of one discipline in eight vocabularies, and it is now reasonable to state the general form. **Whenever a quantity is offered as though it stood alone, the useful question is *relative to what*.** There is always an answer. The answer is frequently the entire argument. And the person who omitted it usually did so because in their own head the answer was obvious.

### What Chapter 9 asks next

You can now take one body of evidence, produce an estimate, say what it is conditional on, and refuse to reduce it to a verdict.

Two things break that immediately in practice.

**There is rarely one body of evidence.** There is this study and that one, the operator's records and the manufacturer's tests, the pilot and the full rollout. They disagree, they are of different quality, and averaging them is not obviously right — Chapter 5's rival models and Chapter 7's identification conditions both bear on whether two numbers are even about the same quantity.

**And the answer usually has to move.** The estimate came from twenty-four heat events in one network under one configuration. The decision concerns next summer, in a network that has changed. Chapter 7 noted in passing that extending a result beyond the sample it came from "requires further argument" and routed the argument forward.

Chapter 9 is that argument: what it takes to combine evidence from several sources, and what it takes to carry a result to a population it did not come from.
