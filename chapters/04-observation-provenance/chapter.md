---
chapter: 4
part: 1
title: "Observation Processes and Data Provenance"
status: drafted
---

# Chapter 4: Observation Processes and Data Provenance

## 1. The Number That Was Never Measured

Chapter 3 ended by handing you something.

Hillcrest has no zone meter. The figure you have been calling **Hillcrest demand — 0.9 ML per day** — was produced like this:

| | Value | Where the number comes from |
|---|---:|---|
| Town total | **9.0 ML** | Meter at the treatment works outlet |
| Lowfield | **5.4 ML** | Zone meter, installed 1998 |
| Millbrook | **2.7 ML** | Zone meter, installed 2004 |
| **Hillcrest** | **0.9 ML** | **None. Computed as 9.0 − 5.4 − 2.7** |

Before going further, notice what is *not* wrong here.

The subtraction is correct. The treatment works meter is correct. Both zone meters are correct and recently serviced. Nobody has falsified anything, nobody has been careless, and there is no arithmetic error anywhere in this table.

And you have used that 0.9 twice.

In Chapter 2 you divided **0.6 ML** of Hillcrest tank storage by it and got about sixteen hours of endurance with no pump — the number that carried the whole aggregation lesson. In Chapter 3 it sat in your role table while you interrogated the word *adequate* at some length and never once asked where the 0.9 came from.

### Before reading further: what is it a measurement of?

Take about **seven minutes**.

The figure is whatever is left after subtracting two metered zones from a metered total.

Write a list: **everything that could be in that leftover.** Do not stop at the obvious answer. For each item, say whether it is water that Hillcrest customers actually used.

Keep the list. You will come back to it.

---

Whatever you wrote, the exercise has a shape worth naming.

Every technique from the last two chapters examines something that is **in front of you**. Chapter 2 asked what belongs in your representation and at what grain. Chapter 3 asked what a number stands for and how well.

Both are inspections. Both took the dataset as given.

Neither can ask why *these* are the numbers you have.

> Why did these records, and not others, come to exist in this form?

That question cannot be answered by looking harder at the data, and this chapter is about why — and about what to do instead.

### This is the ordinary case, not the exotic one

It would be comfortable to treat the Hillcrest figure as an unusually bad dataset — a cautionary tale about one utility's record-keeping.

It is not unusual. It is close to universal.

Almost every dataset you will ever be handed was produced by somebody solving a different problem. Hospital coding records exist to bill insurers. Police incident records exist to dispatch officers and to survive a court. Sensor logs exist because an engineer wanted an alarm. Web analytics exist to sell advertising. Census records exist because a legislature required a count for a purpose written into a statute.

In every one of those cases the records are competent, maintained, and fit for what they were built for — and the question you are bringing to them is not the question they were built for.

The interesting consequence is that the resulting distortions are not random. They are shaped by the original purpose, which means they are **predictable in advance**, if you know what the purpose was.

That is what makes this a skill rather than a warning. You are not being asked to be suspicious of data in general. You are being asked to find out what a dataset was for, and to work out what that purpose would have made invisible.

## 2. Two Processes

### There are two of them

Here is the claim this chapter rests on.

**Your dataset is the output of two processes, not one.**

There is the process you are trying to understand — water moving through a network, patients arriving at a hospital, potholes forming in a road. And there is a completely separate process that decided which facts about it got written down.

Most analytical training attends closely to the first and treats the second as plumbing. The second has its own actors, its own purposes, its own budget constraints, and its own failure modes. It is a system, and it deserves to be described as one.

### The separation is not a metaphor

It is easy to hear "two processes" as a helpful way of talking. It is more than that: the separation appears in the statistical literature as a distinct variable.

In an analysis of what makes large datasets mislead, the error in a sample average is decomposed using "the correlation between X_j and the response/recording indicator R_j" [@meng2018paradox, p. 685].

Read that slowly, because it repays it. For each unit *j* there are two quantities:

- **X_j** — the value out in the world;
- **R_j** — whether that unit made it into your dataset.

Two variables per unit, produced by two different processes. And the thing that determines how badly your data misleads you is the **correlation between them**.

That is the whole chapter in one line, and it gives us the term.

### The observation process

The **observation process** is the process that decides which things get written down.

It is not measurement. Chapter 3 was about measurement, and Chapter 3's question — does this number mean what I think? — assumes a number is there. The observation process is what determines whether there is a number at all.

And here is the idea to carry out of this section:

> **Being recorded is something that happens to a unit, and it can depend on the unit's value.**

Say that back to yourself with an example. A pothole gets into the council's database if somebody reports it. A hospital records a wait if the patient reaches the desk. A meter reading exists if somebody installed a meter.

In each case, whether the thing is recorded depends on something — and that something is often related to the very quantity you are trying to estimate.

### The utility's two processes

Write the two side by side for the water case. It takes four lines each and it is the most useful four minutes in this chapter.

**The process being modelled.** Water is treated and enters the network. It flows under pressure through mains to three zones. Customers draw it. Some escapes through leaks. Some is used by the utility for flushing and by the fire service for hydrants.

**The observation process.** In 1998 a capital-planning decision put a zone meter in Lowfield. In 2004 another put one in Millbrook. A meter registers flow past a point and reports it to a billing system. Technicians read meters, and when one fails somebody decides what to write in the gap. A monthly return goes to the regulator on a form the regulator designed.

Now look at the second list and ask what it is *for*.

**The meters exist to bill customers.** Not to model the network. Not to understand drought behaviour. Not to answer any question you have asked in the last three chapters.

Zone meters went where zone meters would pay for themselves. That is a completely defensible way to run a water utility, and it means the geography of your data is the geography of revenue.

Hillcrest is ten per cent of demand. It never justified the capital.

### Records exist because something made them exist

A **record** exists because something caused it to exist, and that cause is not the phenomenon the record describes.

The history of how a record came to exist — who produced it, for what purpose, under what requirement — is its **provenance**.

Provenance in this sense is not a metadata field. It is not the "source" column in a spreadsheet or a line in a data dictionary. It is a causal story about how a row got onto your screen, and most of it is not written down anywhere, because the people who made those decisions were solving a different problem and did not imagine you.

The Lowfield meter's provenance includes a capital-planning meeting in 1998. That meeting is why you have a number for Lowfield and not for Hillcrest, and it is not in any dataset.

### What records are usually for

You will rarely be told the purpose outright. But datasets come from a small number of recurring institutional motives, and recognising which one you are looking at tells you a great deal before you have read a single row.

**Billing and payment.** Records exist to charge somebody. They are complete and accurate for whatever is charged for, and blind to whatever is not. The utility's meters are this case. A hospital's coding records are this case. So is almost every commercial transaction dataset in existence.

**Compliance and reporting.** Records exist because an external body requires a return. They are shaped by the return form, in the form's categories, at the form's frequency — and anything the form does not ask for is not there, however important it is.

**Operations.** Records exist so somebody can do their job today. They are excellent for the operational question and often discarded once it is answered, because nobody's job depended on keeping them.

**Dispute and liability.** Records exist so that a future argument can be settled. They are unusually detailed about whatever is contested and thin about everything else, and they may be created only when trouble is anticipated.

**Research.** Records exist to answer a question — sometimes even yours. These are rare, and the ones you are handed are almost never these.

Now the practical use of that list. Once you know which motive produced a dataset, the blind spots are largely predictable.

A billing dataset is blind to anything unbilled. A compliance dataset is blind to anything off the form. An operational dataset is blind to history. A liability dataset is blind to the uncontested.

You can often guess a dataset's blind spot from its purpose before you have looked at it — and then go and check whether you were right.

### The observation process has a history

One more property, easy to miss because datasets present themselves as flat.

The observation process is not fixed. It was different in the past, and the record of the past was made by that different process.

The utility's data begins in 1998, when Lowfield got its meter. From 1998 to 2004 there was no Millbrook figure, so the residual then contained Millbrook **and** Hillcrest **and** everything else. In 2004 the composition of that residual changed overnight — not because anything about the town changed, but because a meter was installed.

A long time series produced by a changing observation process is not a long series of comparable observations. It is several short series stacked end to end, with the joins invisible.

Whenever you are handed history, ask when the recording process last changed. The answer is often in a procurement record, a software migration, or a regulation, and almost never in the data.

### Pause: why did the last two chapters miss it?

Before reading on, write two or three sentences.

> Chapter 2 built a representation containing Hillcrest demand. Chapter 3 interrogated the numbers in that representation at length. Neither noticed that the Hillcrest figure was a subtraction residual. Why not?

The answer is not that those chapters were careless.

Chapter 2's tools ask what should be in the model. *Hillcrest demand* should absolutely be in the model — Chapter 2 got that right. Chapter 3's tools ask what a number stands for and whether it is measured well. And every number in the subtraction **is** measured well.

Both chapters examine the objects in front of you. The residual passes both examinations, because the problem is not in any object. The problem is in the **set** — in which objects exist and which do not — and a set has no property you can inspect by looking at its members.

That is why this chapter needs a different method, which §5 will name.

### Task: write the two processes

For the water utility, write two short paragraphs.

1. **The process being modelled.** What actually happens to water.
2. **The observation process.** What actually happens to records — who creates them, when, why, and what they are for.

Then answer one question in a sentence: **what were these records made for?**

If your second paragraph is shorter than your first, you have found the asymmetry this chapter exists to correct.

### Why the second process is invisible

That asymmetry is not a personal failing, and it is worth understanding, because knowing why something is hard to see is most of the work of seeing it.

**The data arrives without its history.** A file has columns and rows. It does not have a column for *why this row exists*. Everything about the observation process was stripped off at the moment the data was written, and what remains is the output with the production erased.

**The observation process is somebody else's job.** The person who installed the meter, the technician who filled the gap, the administrator who set the retention policy — none of them is in the room when the analysis happens, and none of them thought of themselves as producing data. They thought of themselves as billing customers, covering a shift, controlling storage costs.

**It looks like infrastructure.** Plumbing is not where you look for the interesting question. The modelling feels like the intellectual work and the data feels like the input to it, so attention flows to the model.

**And nothing goes wrong visibly.** A representation that omits something leaves a question you cannot answer. A number that means the wrong thing can sometimes be caught by checking it. A dataset selected by a process unrelated to your purpose returns an answer — a plausible one, in the right units, with a comfortable interval around it.

That last point is the whole difficulty. The other three chapters' failures announce themselves eventually. This one does not announce itself at all.

## 3. Where the Recording Process Intervenes

Knowing there is a second process is not much use without knowing where to look at it.

This section gives you five places. They are ordered, roughly, by how early they act — and the earlier one acts, the harder it is to see afterwards.

**One honesty note first.** Two of these five are established concepts with sources behind them. The other three are ordinary features of record-keeping that you can verify directly on this case. The **five-stage list is this book's own device**, not a framework you will find in the literature. It is offered because it gives you somewhere to look, and you should treat it as a checklist someone made up rather than a law.

### Eligibility — what could ever have appeared?

Before anything is measured, something decides which units are even candidates.

In official statistics this is settled explicitly. The `target population` is the set of units about which inference is intended, and membership in it is distinguished from the status of any particular sampled unit [@censusndtargetpopulation, §1.1].

For the utility, the eligibility rule is almost comically simple and nobody ever wrote it as a rule:

> **A connection is metered if it has a billing account.**

Which means firefighting draw is not eligible. Neither is the utility's own operational use — mains flushing, tank cleaning. Neither are standpipes. None of these has an account, so none has a meter, so none has a record.

Water leaves the network through a hydrant and **nothing anywhere registers that it did.**

### Coverage — which eligible units were reached?

Being eligible is not being reached.

Zone meters went into Lowfield in **1998** and Millbrook in **2004**. Both decisions were made on revenue: those zones had enough billed consumption to justify the capital.

Hillcrest, at ten per cent of demand, did not.

So the coverage of your zone-level data was determined by two capital-planning decisions, twenty-six and twenty years ago, made by people optimising something entirely reasonable and entirely unrelated to your question.

### Capture — which reached units produced a record?

An instrument that exists still has to work, and somebody has to decide what happens when it does not.

The Millbrook zone meter failed for **11 days** last year. The gap was filled by carrying forward the previous week's average.

That is a reasonable rule. It is consistently applied and it is documented. Hold on to it; §5 will show what it did.

Capture is also where the survey-methodology literature lives — nonresponse, refusals, unreachable households. Most readers of this book will not be running surveys, and it matters that the same stage exists whether or not anyone designed a sample. A meter that fails and a household that declines are the same stage of the same kind of process.

### Retention — which captured records were kept?

Data that existed is not data that exists.

The utility logs readings every **15 minutes**. It keeps them for **90 days**. After that they are aggregated to daily totals and the fine-grained data is discarded, because storage costs money and nobody had a reason to keep it.

Now recall Chapter 3. The whole Hillcrest pressure problem appeared **at the evening peak** and would have been invisible in daily figures.

For anything more than ninety days old, the evening peak is not merely hard to see. It is gone. No analysis, however careful, will recover it.

### Reporting — what was passed on, and in what shape?

The last stage is the one most likely to be the only one you ever see, because for most datasets you are not the first recipient.

The utility's monthly regulatory return reports **non-revenue water** as a single line: leakage, unbilled operational use, and metering error, combined.

Combined by the time it leaves the utility. If you are the regulator, or a researcher using the regulator's published data, those three things arrived pre-summed and there is no operation you can perform that separates them again.

### The five stages, away from water

The stages are only useful if you can run them on something that is not a utility. Here they are as questions, with what each typically looks like elsewhere.

| Stage | The question to ask | What it looks like elsewhere |
|---|---|---|
| **Eligibility** | What could never have appeared here at all? | People without an address, in a dataset keyed to addresses. Transactions below a reporting threshold. Incidents that do not meet a definition of "incident". |
| **Coverage** | Among things that could appear, which were reached? | Sensors installed in some buildings. A survey frame drawn from landline numbers. A app-based reporting channel used by some people and not others. |
| **Capture** | What happened when the instrument or the person did not deliver? | Nonresponse. A sensor outage. A form field left blank. A shift that got too busy to log. |
| **Retention** | What has been deleted, and after how long? | Logs rotated weekly. Records purged under a retention policy. A system migration that carried forward only summary data. |
| **Reporting** | What was combined, rounded, or reshaped before it reached me? | Monthly totals. Suppressed small cells. Categories mapped to a funder's taxonomy. Percentages published without denominators. |

Two things about this table are worth noticing.

**The stages get harder to see as you go up.** Reporting is usually documented somewhere, because somebody had to build it. Retention is usually a policy you can ask about. Capture is sometimes flagged in the data. Coverage requires knowing what was not covered. And eligibility is a rule that may never have been written down, because to the people applying it, it was not a rule — it was just how things obviously worked.

**The stages compose.** A unit that survives eligibility can still be missed at coverage, and one that survives coverage can still fail at capture. Your dataset is what got through all five, and each stage had its own reasons for filtering.

### Two kinds of aggregation, kept apart

Chapter 2 warned that this word does double duty, and here is the second half of the split.

**Representational aggregation** is a modelling choice you make, before any data exist, about treating distinguishable things as one. Chapter 2's single town-wide demand number was that.

**Reporting aggregation** is done *to the records*, by somebody else, usually before you see them.

The difference is what you can do about it. Representational aggregation you can undo this afternoon by choosing differently. Reporting aggregation you cannot undo at all — the components were combined and discarded, and no amount of care with what remains will separate them.

### Selection is not one event

Notice what has happened across the five stages.

At eligibility, firefighting draw was excluded. At coverage, Hillcrest was excluded. At capture, eleven days went missing. At retention, ninety-day-old detail was discarded. At reporting, three quantities were merged.

**Selection operated at every one of them.** It is not a thing that happens once, in a sampling step, to datasets that have a sampling design. A dataset assembled with no design at all — meters, logs, tickets, filings — has been selected five times over by the time it reaches you.

That is why "we didn't sample, we have everything" is not the reassurance it sounds like.

### When you cannot find out

The honest difficulty with everything above is that you frequently cannot answer these questions. The dataset arrived as a file. The person who built it left. The system was replaced. Nobody knows why the threshold is £500.

This is normal, and it does not license giving up. Three things remain available.

**Reason from purpose.** Even with nobody to ask, you can usually establish what the records were *for* — from the field names, from what is measured precisely versus roughly, from what has a mandatory field and what does not. A dataset with meticulous timestamps and vague categories was built for sequencing, not classification. A dataset that records amounts to the penny and dates to the month was built for accounting. Purpose is legible in structure.

**Look for the seams.** Changes in the observation process usually leave marks: a field that starts being populated in a particular month, a distribution that shifts abruptly at a date with no plausible worldly cause, a category that appears once and never again. These are not anomalies to clean. They are the observation process's fingerprints.

**Write down what you do not know.** An explicit list of unanswered provenance questions is a real deliverable. It tells a reader which conclusions are exposed, it tells your future self where to look when something turns out wrong, and it is honest in a way that a silent analysis is not.

What is not available is treating unknown provenance as though it were harmless provenance. "We could not determine how these records were selected" and "these records were selected in a way unrelated to our question" are very different sentences, and only the first one is ever justified by an absence of information.

### Task: walk the five stages

For the water utility, fill this in.

| Stage | What it decided | Who decided it, and what were they optimising? |
|---|---|---|
| Eligibility | | |
| Coverage | | |
| Capture | | |
| Retention | | |
| Reporting | | |

The third column matters most. In every row the answer is a real person or committee solving a real problem — and in no row were they solving yours.

## 4. Why More Records Do Not Help

Here is the reasonable objection.

The utility has eleven years of these records. Millions of readings, taken every fifteen minutes, across two decades of operation. Surely a dataset that large has something going for it?

This section is about why the answer is no, and it is the least intuitive thing in the chapter.

### Three things multiplied

There is a result in the statistical literature that decomposes the gap between what your data says and what is actually true into **three factors, multiplied together** [@meng2018paradox, p. 685].

In words, they are:

1. **how strongly being recorded is related to the value** — the data-quality term;
2. **how much of the population you have** — the data-quantity term;
3. **how variable the quantity is** — the problem-difficulty term.

The important word is *multiplied*. A product is small only if one of its factors is small. Making one factor better does not compensate for another being bad — it multiplies a better number by an unchanged bad one.

Collecting more records improves the second factor. It does nothing whatever to the first.

### What a random sample actually buys you

This reframes something most people half-remember from a statistics course.

The value of a properly designed random sample is not that it is a clever way to save effort. It is that random selection **arranges for the first factor to be near zero**. Probabilistic sampling "ensures high data quality by controlling ρ_{R,X} at the level of N^{−1/2}" [@meng2018paradox, p. 685] — that is, it holds the relationship between being recorded and the value down to a level that shrinks as the population grows.

Randomisation is not a sampling convenience. It is a **method of controlling the data-quality term**, and it is the only one that works by construction.

Now the consequence of not having it. When that control is absent, "our estimation error, relative to the benchmarking rate 1/√n, increases with √N" [@meng2018paradox, p. 685] — where N is the size of the population you are drawing from.

Read that again. The error grows with the size of the **population**, not shrinking with the size of your **dataset**.

The same source puts the practical shift plainly: analysts are used to attending to a standard error that falls as you collect more; what matters for a dataset with a defect is a relative bias whose expression **does not contain the number of records you collected at all** [@meng2018paradox, p. 687].

More is not in the formula.

### Two point three million records worth four hundred

The paper gives an empirical case, and the numbers are what make it stick.

Analysing the 2016 US presidential election using a large survey, the estimated correlation between recording and value — for self-reported intention to vote for one candidate — was about **−0.005** [@meng2018paradox, p. 685].

Half of one per cent, in correlation. Trivially small by any conventional standard.

The consequence: a sample covering **1% of US eligible voters, about 2,300,000 people**, carried "the same mean squared error as the corresponding sample proportion from a genuine simple random sample of size n ≈ 400, a 99.98% reduction of sample size (and hence our confidence)" [@meng2018paradox, p. 685].

**2.3 million records behaving like 400.**

Not because the data was fabricated, not because the respondents lied more than usual, and not because the analysis was wrong. Because whether someone appeared in the dataset was very slightly related to how they intended to vote, and slight was enough.

Three cautions, because this figure travels badly.

It is one empirical estimate, for one question, in one study. It is not a general law about large datasets. The −0.005 is a **correlation**, not a bias and not a percentage. And a large dataset with that correlation near zero is excellent — nothing here says size is bad.

### The paradox

What makes this worse than ordinary error is what happens to confidence.

The paper reports that in that election, "on average, the larger the state's voter populations, the further away the actual Trump vote shares from the usual 95% confidence intervals based on the sample proportions" [@meng2018paradox, p. 686].

Bigger populations, wronger answers, **narrower intervals**. The estimate drifted further from the truth while the reported uncertainty around it shrank.

Hence the name:

> "without taking data quality into account, population inferences with Big Data are subject to a *Big Data Paradox*: the more the data, the surer we fool ourselves." [@meng2018paradox, p. 686]

Keep the conditional clause. The claim is not that big data is bad. It is that *without accounting for data quality*, more of it buys you confidence rather than accuracy — and confidence is the more dangerous purchase.

### Pause: what would eleven more years fix?

Before reading on:

> The utility has eleven years of these records. Suppose it had twenty-two. Which of the problems from §3 would be improved?

Work down the list. Eligibility: firefighting draw is still not metered. Coverage: Hillcrest still has no zone meter. Capture: more failed days, filled the same way. Retention: still ninety days. Reporting: still one combined line.

Twenty-two years of records produced by the same process is twenty-two years of the same five decisions.

The dataset would be twice as large and not one of its defects would be smaller.

### Complete is not representative

A related reassurance that fails the same way.

The utility meters **100% of its billed connections**. Not a sample — all of them. Surely that settles it?

It does not, because the question was never whether you have all the units you are recording. It is whether being recorded is related to the value. The same source notes that the "bigness" of a dataset for population inference should be judged by **relative** size — what fraction of the population you have — rather than absolute size [@meng2018paradox, p. 685].

And the utility does not have 100% of the water. It has 100% of the *billed connections*, which is a different population, chosen by the billing system.

Complete coverage of the wrong population is complete coverage of the wrong population, however many rows it has.

### The rate that tells you nothing

The same mistake has a specific and very common form: reading a response rate as a measure of bias.

It is not one. In survey research, "response rates lack validity in that there is not even a moderate correlation with nonresponse bias" [@davern2013nonresponse].

That result deserves care in both directions.

It does **not** mean nonresponse is harmless. It means the number everyone reports — the percentage who responded — is a poor guide to how much damage the nonresponse did. A low rate is a reason to investigate, not a measurement of the harm. A high rate is not a clean bill of health.

Which makes sense given everything above: a rate counts **how many** were recorded and says nothing about **who**.

### A dataset is not trustworthy or untrustworthy

One more, and it changes how you should talk about your data.

Nonresponse bias "is an estimate level measure and it cannot be easily summarized by a survey level proxy measure" [@davern2013nonresponse].

Bias attaches to a **quantity you are estimating**, not to a dataset. The same records can be excellent for one question and disastrous for another, because the recording process may be unrelated to one variable and strongly related to another.

The utility's meter records are perfectly good for billing. They are perfectly good for total treated output. They are bad for Hillcrest demand, and they are bad for evening peaks older than ninety days.

Same records. The question "is this data any good?" has no answer until you say **good for what** — which by now should be a familiar move. Chapter 1 said adequacy is relative to a stated use. Chapter 3 said validity is relative to an interpretation. Chapter 4 says trustworthiness is relative to the quantity being estimated.

### The same shape as Chapter 3

One last thing before leaving this section, because you have met this structure before and the repetition is not accidental.

Chapter 3 established, from metrology, that **more measurements improve precision and do nothing for trueness**.

Chapter 4 establishes, from statistics, that **more records shrink the sampling-variability term and do nothing for the data-quality term.**

Two different fields, two different vocabularies, one shape: there is a quantity that effort reduces, and a quantity that effort does not touch, and the second is usually the one that decides your answer.

Each of those results is independently established in its own literature. The observation that they rhyme is this book's, and it is offered as a habit rather than a theory: when you are told that more of something will fix a problem, ask which term it enters.

### So what does help?

Having spent a section saying what does not work, it is only fair to indicate what does — while noting that the methods themselves are Chapters 7 and 8, and this is a signpost rather than a treatment.

**Change the recording process, not the record count.** The utility's real option is a Hillcrest zone meter. Nothing in its archive substitutes for one, and a modest amount of the right data beats an enormous amount of the wrong data — the same source notes that when combining sources, "relatively tiny but higher quality ones should be given far more weights than suggested by their sizes" [@meng2018paradox, p. 685].

**Get a second, differently-produced view.** This is the same move that caught the storage discrepancy in Chapter 1 and the pressure problem in Chapter 3. A temporary insertion meter on the Hillcrest main for two weeks is worth more than a decade of subtraction, because it does not share the subtraction's assumptions.

**Find out how being recorded relates to your quantity.** You usually cannot measure that relationship, but you can often reason about its direction. If meters were installed where revenue was high, and you are estimating something correlated with revenue, you know which way you are wrong before you compute anything.

**Bound what you cannot fix.** If you cannot separate the components of the residual, you can sometimes bracket them. A leakage figure from a night-flow study, an operational-use estimate from work orders — none of it precise, all of it enough to say how large the contamination could plausibly be.

**And say so.** The most valuable output of a provenance analysis is often not a corrected number. It is a sentence in the report saying what this figure includes, what it cannot include, and which decisions it should not be used for.

## 5. Gaps, Bounds, and What Is Not There

Something is not in your data. There are three quite different reasons for that, they call for different responses, and only one of the three is visible.

### Missing: the value should be there and is not

The familiar case. A row exists, a column exists, and the cell is empty.

The temptation is to treat this as a tidying problem — drop the rows, or fill them with a column average, and get on with the analysis.

Both moves are assumptions about the observation process, made silently.

There is a foundational result on when you may set the missingness process aside. Whether it is appropriate to ignore the process that caused data to be missing **depends on why they are missing**, and the stated conditions are described by that source as the weakest general conditions under which ignoring it always leads to correct inferences [@rubin1976missing]. *(This citation rests on the paper's published summary; the full text has not been consulted for this book.)*

Take the shape of that even if the conditions themselves are Chapter 8's business. Ignoring missingness is permitted **under conditions**. It is not the default, and "the gaps were only two per cent" is not one of the conditions.

So the question to ask about any gap is a single one:

> **Is whatever caused this to be absent related to what the value would have been?**

Three plain-language possibilities:

- absent for reasons having nothing to do with the value — a technician was on holiday;
- absent for reasons related to something else you did record — a whole depot's readings failed, and you know which depot;
- absent for reasons related to **the value itself**.

The third is the dangerous one, because nothing in the surviving data announces it. You cannot find it by studying the rows you have, since the rows you have are precisely the ones the process kept.

There is a standard three-way vocabulary for these cases in the statistical literature. This book does not use it, partly to keep the terminology budget for other things, and partly because the source verified here does not use it either.

What is worth having instead is a sense of how often the third case turns up, because it is easy to assume it is rare and it is not.

Instruments fail under load, which means readings vanish under exactly the conditions that stressed them. People do not respond to surveys when they are busy, ill, or in trouble — which is often what the survey is about. Systems drop transactions at peak volume. Staff skip optional fields when the shift is chaotic, and the chaotic shifts are the interesting ones. Patients who leave without being seen do not generate a discharge record.

In each case the reason for the gap is bound up with the value the gap conceals. And in each case the surviving data looks entirely healthy, because the surviving data is exactly the well-behaved subset.

That is the sense in which missingness is not a data-cleaning problem. Cleaning operates on what is there.

### The utility's gap, worked

The Millbrook zone meter failed for **11 days** last year, and the gap was filled by carrying forward the previous week's average.

Now the fact that matters, which is not in the dataset:

**The meter's failure mode is heat-related.** It faults more often at high ambient temperature. **Nine of the eleven failures fell in the two hottest weeks of the year.**

Follow it through slowly.

Those nine days were filled from a **cooler** week, so the Millbrook figure used was **lower** than the truth.

Millbrook is a subtrahend. `Hillcrest = town total − Lowfield − Millbrook`. A smaller subtrahend leaves a **larger** remainder.

So the Hillcrest figure is **inflated on precisely the hottest days** — the days on which the drought plan is invoked, the days Chapter 1's entire analysis concerned, and the days when Hillcrest's supply actually matters.

Sit with the properties of this failure.

The fill rule was reasonable. It was applied consistently. It was documented. Nobody did anything wrong at any point. And the rule makes the number least trustworthy exactly where it is used most.

The eleven filled days look, in the dataset, like ordinary readings.

### Censored: the value is there and is a boundary

A different thing, often mistaken for the first.

The treatment-works outlet meter registers to a maximum of **10.0 ML per day**. On three days last summer, true output exceeded that maximum. Each was recorded as **10.0**.

Those three records are not missing. They carry real information: output was *at least* 10.0.

That is **censoring** — the recording process stopped at a bound, and the record tells you the value lies beyond it.

Both ways of mishandling it are wrong, and helpfully, both are wrong in known directions.

**Treat them as missing** and you discard genuine information — you knew output was at least 10.0 and you have thrown that away.

**Treat 10.0 as the true value** and you understate the town total on those three days. And since Hillcrest is the town total minus two zones, understating the total **understates the residual** on days of maximum output.

Notice that this pushes the opposite way from the Millbrook gap. Both are systematic, both act on hot days, and they do not cancel in any principled way — you would have to know both magnitudes to say what the net effect is, and you do not.

The hardest thing about censoring is that it does not look like a gap. A row reading 10.0 looks like a measurement. The only ways to catch it are to know the instrument's limits, or to notice an implausible pile-up of values at exactly one number.

That second signal is worth learning to look for, because censoring is common and rarely labelled. A stack of values at a round maximum. Ages recorded as 99. Durations that never exceed the length of a shift. Amounts that stop at a reporting threshold. Satisfaction scores bunched at the top of the scale.

In each case something stopped the recording — an instrument range, a form's options, a policy limit, a scale with no room above it — and the record kept the boundary rather than the value.

The related case runs the other way. Sometimes the recording process does not cap a value but excludes the unit entirely once it passes a limit: claims below a threshold are never filed, incidents shorter than a minute are never logged. Then you do not have a boundary value at all; you have an absence, and you are back in the third case below.

The practical habit is small: whenever a column has a suspiciously popular extreme value, find out whether that is a value or a wall.

*(No source is cited for this distinction. It is standard in the statistical literature and the demonstration above is the argument for it — you can check the direction of each error yourself.)*

### Absent: there was never anything to be missing

The third case, and the one this chapter exists for.

The fire service opens a hydrant. Water leaves the network. Nothing anywhere registers that it did.

There is no meter, because there is no billing account, because the eligibility rule from §3 is *a connection is metered if it has a billing account*.

That water is not missing. **It never had a place to be.**

There is no row. There is no null. There is no flag, no anomaly, no gap in a sequence. There is nothing at all to notice, and every data-quality check ever written will pass.

Compare the three:

| | Visible in the dataset? | Cause detectable from the dataset? |
|---|---|---|
| **Missing** | Yes — a blank, a null, a flag | No. The pattern is visible; the reason is not |
| **Censored** | Often not — it looks like a value | Only if the bound is documented, or a pile-up is noticed |
| **Absent** | **No** | **No** |

### Pause: which could you find by looking?

Before reading on:

> Of the three — the eleven filled Millbrook days, the three censored outlet readings, and the unmetered firefighting draw — which could you discover by inspecting the dataset carefully?

The first, partly. You can see eleven identical carried-forward values if the fill was flagged, and if it was not, you might notice a suspiciously flat stretch. You cannot see **why** those days failed. The heat-related failure mode is a fact about a device, not a fact about the data.

The second, only with luck, and only if you already suspected. Three rows reading 10.00 in a column that otherwise varies is a hint — to someone who knows what the meter's range is.

The third, never. There is no operation on that dataset, however sophisticated, that produces the firefighting draw. It is not hidden. It is not there.

### What follows about method

Which gives Chapter 4 its method, and it is not a data-analysis method.

Everything you can do by studying your data harder addresses the top rows of that table. The bottom row — the one that does the most damage — requires leaving the dataset entirely and asking questions of the people and institutions that produced it.

> **Chapter 4's work is an interview, not an analysis.**

Who built this? What were they required to record? What did they leave out, and why was that reasonable for them? What happens here when an instrument fails? How long do you keep things? What does the form you fill in ask for?

None of those questions has an answer inside the data, and all of them have answers.

### Task: classify three gaps

For each of the three below: say whether it is missing, censored, or absent; say what direction of error results from mishandling it; and say whether you could have detected it from the dataset alone.

1. Eleven days of Millbrook readings, filled by carrying forward.
2. Three outlet readings of exactly 10.0 ML.
3. Water drawn through hydrants by the fire service.

## 6. Reading the Residual

Time to open the number.

### What is actually in the 0.9

A study three years ago fitted a temporary insertion meter to the Hillcrest feeder main for two weeks, and a night-flow study the following year attributed leakage across the network. Operational records supply the rest.

| Component | ML/day | Does it draw the Hillcrest tank? |
|---|---:|---|
| Hillcrest customer consumption | **0.62** | yes |
| Leakage, Hillcrest feeder main and zone | **0.10** | yes |
| Leakage, rest of network | **0.08** | **no** |
| Unbilled operational use — flushing, firefighting, tank cleaning | **0.06** | mostly no |
| Under-registration by the Lowfield and Millbrook meters | **0.04** | **no** |
| **Total** | **0.90** | |

Each component is itself an estimate, and they are not precisely known. But the shape is unmistakable.

**A little under a third of "Hillcrest demand" is not Hillcrest, and is not demand.**

It is leakage in other people's pipes, water the utility used itself, and the amount by which two meters elsewhere read low. The residual absorbed all of it, because a residual absorbs everything that is not one of the things you subtracted.

### Redo Chapter 2's arithmetic

This is the part to work rather than read.

What actually draws down the Hillcrest tank is consumption plus leakage inside the Hillcrest zone:

`0.62 + 0.10 = 0.72 ML per day`

Chapter 2 computed the tank's endurance with no pump as `0.6 ÷ 0.9 = 0.67 days`, about **16 hours**.

The correct figure is:

`0.6 ÷ 0.72 = 0.83 days`, about **20 hours**.

Four hours more than the whole Chapter 2 analysis believed the utility had.

### Two things about that error

**First, the direction.** Chapter 2's figure was *conservative*. It said the utility had less time than it did. Nobody was endangered, no bad decision followed, and precisely because the error was in the comfortable direction, nobody had any reason to look for it.

That comfort was luck. The residual overstated the tank draw because most of its non-Hillcrest components sit outside the zone. If leakage inside Hillcrest grew while leakage elsewhere was repaired — a completely ordinary sequence of events for a utility replacing old mains — the same residual would begin **understating** the draw, and the sixteen-hour figure would become an overestimate of the time available. The error would flip direction with nothing in the data changing.

**Second, and more important: Chapter 2 made no mistake.** `0.6 ÷ 0.9` is correct arithmetic on the number that was available. There is no step in Chapter 2 you could go back and fix. The defect was never in the calculation; it was in what the number was.

### Nobody did anything wrong

It is worth being explicit, because a chapter like this invites a tone it should not have.

Read back through everything that produced this figure. A capital-planning committee put meters where revenue justified them. A technician followed a documented rule for filling a gap. A storage policy discarded fine-grained data after ninety days because storage costs money. A regulator designed a return form with a single line for non-revenue water.

Every one of those decisions is reasonable. Several are obviously correct. None was made by anyone who was thinking about drought analysis, because none of them was about drought analysis.

**The meters exist to bill customers.** That is what they are for, they do it well, and the fact that a billing system produces a poor map of a network is not a failure of the billing system.

Which is the general condition. Almost every dataset you will ever be handed was produced by someone solving a different problem, competently. That is not a scandal to expose. It is the situation, and the only defence is to find out what problem they were solving.

### What the utility should actually do

Worth a moment, because a chapter that only diagnoses is less useful than one that ends somewhere.

The utility's options, roughly in order of value:

**Meter Hillcrest.** The zone has been a residual for twenty-six years and the capital case has changed — it is no longer about billing revenue but about knowing whether a zone can be supplied during a drought. That is a different justification than the one that failed in 1998, and it is a better one.

**Until then, stop calling it demand.** Rename the field. *Hillcrest residual* costs nothing, requires no capital, and prevents every downstream reader from making the mistake this chapter has spent four sections on. A great deal of provenance damage is done by field names that assert more than the data supports.

**Flag the filled days.** The eleven carried-forward Millbrook values should be marked as filled. Whoever fills a gap knows they are filling it; the information is lost only because nobody wrote it down.

**Record the outlet meter's range next to the outlet meter's readings.** Then a value of 10.0 is legible as a possible ceiling rather than as a measurement.

**Keep one week of fifteen-minute data per year.** Not all of it — storage costs are real — but enough that peak behaviour older than ninety days is not entirely gone.

Notice that four of those five cost almost nothing. Provenance failures are expensive to *discover* and often cheap to *prevent*, which is an argument for asking these questions when a dataset is being designed rather than when it is being used.

### Task: diagnose five defects

Each item contains one defect. For each, write the defect, what it stops you concluding, and a repair.

1. A briefing note: "We have meter records for 100% of connections, so the dataset is representative of town water use."
2. An analyst's method section: "Missing readings comprised 2% of rows and were dropped."
3. A data catalogue entry: "Our most reliable source — eleven years of continuous readings."
4. A quality report: "There are no nulls in this table, so the data is clean."
5. A survey summary: "With a 94% response rate, nonresponse bias is negligible."

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

### Task: place four situations

Chapter 15 is about what happens when the people in a system respond to being measured. This chapter is not about that, and the difference is worth being able to see.

> **Chapter 4:** the records were shaped by what the institution needed them for.
> **Chapter 15:** the records changed because people learned they were being used.

Place each of these.

1. Zone meters were installed where billing revenue justified the capital.
2. Fifteen-minute readings are discarded after ninety days to save storage.
3. The regulatory return has one line for non-revenue water, so three quantities arrive combined.
4. After the residual began appearing in monthly management reports, operators started scheduling mains flushing for the day *after* the reading rather than the day before, and the residual fell.

The fourth is Chapter 15, and notice what makes it so: nothing about the network changed. What changed was the recording process, in response to being watched. Everything in this chapter has assumed a recording process that is not reacting to you. That assumption is worth knowing you are making.

## 7. Cold-Start Practice and Retrieval

### Return to your seven-minute list

Find what you wrote at the start of §1: everything that could be in the leftover.

Read it against the decomposition in §6, and do not score it.

- Did you include leakage — and did you distinguish leakage *inside* Hillcrest from leakage elsewhere?
- Did you include water the utility used itself?
- Did you include the possibility that the other meters read low?
- Did you include anything that never had a meter at all?

Most first lists contain Hillcrest consumption and leakage, and stop. The two that are usually missing are the two that require thinking about the recording process rather than about water: metering error somewhere else, and use that no instrument was ever meant to capture.

If your list said "Hillcrest demand, plus maybe some leaks", that is the specific thing this chapter has added.

### Independent transfer

Now work an unfamiliar dataset, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below. Open only that one.

- [Form A — A city's pothole repair records](transfer-form-a.md)
- [Form B — A food bank's client records](transfer-form-b.md)

Allow about **40 minutes**.
Every fact you need is supplied. Do not look anything up.

Do not open the other form. You will work it after a delay, and it tests nothing if you have seen it.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it dimension by dimension.

### Retrieve the questions from memory

Before looking back at the chapter, write down the questions you would ask about any dataset handed to you.

Aim for the sequence, not the wording. Then compare and repair what you missed.

For reference, after you have tried:

1. What process produced these records, as distinct from the process I am asking about?
2. **What were these records made for, and by whom?**
3. What could never have appeared — what was not eligible?
4. Which eligible things were reached, and which were not?
5. What happens here when an instrument fails or a person does not respond?
6. What has been discarded, and after how long?
7. What was combined before it reached me, and can it be separated?
8. Is being recorded related to the quantity I care about?
9. Would more of the same records help? (Almost always: no.)
10. What is absent that would leave no trace?

Question 2 is the one to keep if you keep only one. Almost everything else in this chapter can be reached from a good answer to it.

Question 10 is the one nobody asks unaided.

A caution about the list, in the spirit of the chapter.

These are not questions you answer at your desk. Eight of the ten have answers held by other people — a technician, a systems administrator, whoever designed the return form, whoever signed off the retention policy. The person who can tell you why the meter fails in hot weather is not in your organisation and has never heard of your analysis.

Which makes provenance work slow, social, and unglamorous, and it is why it is usually skipped. A dataset arrives, it opens cleanly, the columns have sensible names, and there is nothing on screen suggesting that a phone call is required.

The absence of a visible problem is not evidence that there is not one. That is the entire content of §5.

### If the transfer went badly

- **You described the process being measured, not the process doing the recording.** The most common outcome. Reread §2 and write the second paragraph first next time.
- **You listed data-quality problems rather than provenance.** Nulls, outliers, and inconsistent formats are properties of the data. Provenance is a story about people. If your answer has no people in it, it is not a provenance analysis.
- **You could not name anything absent.** Ask what the record-keeper had no reason to record. Absence follows from purpose, which is why question 2 comes first.
- **You said more data would help.** Reread §4 and identify which of the five stages more data would change.
- **You treated the institution as negligent.** Look again for the reason each decision was sensible for whoever made it. A provenance analysis that concludes people were careless has usually stopped one question early.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Do not reread this chapter immediately beforehand, and do not look at the form you have not done.

### What Chapter 5 asks next

You can now build a representation, interrogate its numbers, and interrogate where those numbers came from.

Which means you now have four chapters' worth of ways for an analysis to be wrong: the wrong things represented, at the wrong grain, measured by procedures that do not support the interpretation, from records produced by a process that was never aimed at your question.

That is a lot of failure modes and no system for finding them.

Chapter 5 asks the question that organises them: **how could this whole formulation fail its purpose, and what would show it?**

Notice the second half of that question, because it is what makes Chapter 5 more than a longer list of worries.

Everything you have found in this chapter, you found because something specific would have shown it. The insertion meter would have shown the residual's composition. A gauge at the top of the zone would have shown the pressure problem. An independent tank check did show the storage discrepancy.

In each case there was an observation that would have discriminated between "the analysis is fine" and "the analysis is wrong" — and in each case nobody had made it, because nobody had asked what such an observation would be.

That is the habit Chapter 5 builds, and it converts four chapters of accumulated failure modes from a list of things to fear into a list of things to go and check.
