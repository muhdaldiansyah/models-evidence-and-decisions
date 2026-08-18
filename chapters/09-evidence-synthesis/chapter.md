---
chapter: 9
part: 2
title: "Combining and Transporting Evidence"
status: drafted
---

# Chapter 9: Combining and Transporting Evidence

## 1. Five Reports and One Decision

The utility is out of chapters to hide behind.

Chapter 7 examined whether its own records could establish what a pump upgrade would do at Hillcrest and returned a verdict of **not identified** — no zone resembling Hillcrest had ever been upgraded, and no amount of the same record would change that. Chapter 8 estimated a different quantity, carefully, and said what it was conditional on.

Neither answered the question the asset committee is going to ask in March.

So the utility does what organisations do when their own evidence runs out. It goes and finds more.

### What came back

Five things now sit on the same desk, all bearing on what a duty-pump upgrade does to low-pressure complaints during heat events.

| | Source | Size | Estimate |
|---|---|---:|---:|
| **A** | The utility's own upgrade record | 15 zones | **−2.4** |
| **B** | A neighbouring utility's before-and-after study | 40 zones | **−3.1** |
| **C** | An industry benchmarking dataset | 1,400 zones | **−0.6** |
| **D** | The pump manufacturer's rig test | 6 rigs | **−4.8** |
| **E** | An expert panel of five engineers | — | **−1.5** |

Negative means fewer complaints per heat event. The five estimates run from **−0.6 to −4.8**, a factor of eight.

Nobody is lying. Each of the five was produced competently by people who would defend it.

And the committee's question is simple enough to write in one line: **should we upgrade the pump at Hillcrest before next summer?** The five reports were commissioned to answer it.

### Before reading further

Take about **six minutes**.

> **Which of the five would you trust? And how would you combine them into a number the committee can use?**

Write a few sentences. Commit to something specific — a rule, or a choice, or a reason for excluding one.

Keep what you write. You will come back to it.

---

### The word that makes this hard

This chapter's question is: **what do many imperfect sources jointly support — here?**

Most of the effort a reader will expect goes into the clause before the dash. Five numbers, how do you put them together, what is the right weighting.

**The word after the dash is the harder half.**

Every one of the five sources is about somewhere else. Forty zones in a neighbouring network. Fourteen hundred zones across the industry. Six test rigs in a factory. Fifteen zones of the utility's own, none of which resembles Hillcrest in the respect Chapter 7 identified.

A number synthesised from all five is a statement about the places they came from. Hillcrest is not one of those places, and §5 is about what it would take to get from there to here.

This chapter is also the last of Part II. After it, the book stops asking what the evidence supports and starts asking what the decision-maker wants.

### Why this is not a small problem

It would be reasonable to think of this as tidying up — the analysis is done, several people have done versions of it, somebody now has to put the versions together.

**It is the situation almost every real decision is actually in.**

Nobody deciding anything consequential has one clean study. They have an internal analysis, a vendor's claim, a benchmark, something from a trade body, and a room full of people with opinions. The single-source situation the last three chapters treated is the exception, taught first because it is simpler, and the five-source situation is the ordinary one.

And the failures are different in kind. Chapters 7 and 8 were about ways a single analysis can mislead. This chapter is about failures that only exist when there is more than one source — which means that a reader who applies Chapters 7 and 8 five times over, perfectly, still walks into them.

## 2. Are They About the Same Thing?

There is a question that comes before any weighting, and skipping it is how five reports become one meaningless average.

**What is each of these numbers a number about?**

### The test you already have

Chapter 7 gave you the apparatus without calling it this. A quantity is specified when you can state its treatment and comparison, its population, its variable, the events in between, and the summary rule.

Run those attributes down each source.

| | Treatment | Population | Variable |
|---|---|---|---|
| **A** | four different actions recorded as one | 6 upgraded zones of 15, chosen as the worst | complaints per heat event |
| **B** | duty-pump upgrade | 40 zones, all on flat ground | complaints per heat event |
| **C** | "pump upgrade", member-defined | 1,400 zones, voluntary participation | complaints, **no enforced definition** |
| **D** | a specified pump swap | 6 test rigs | pressure recovery on a rig |
| **E** | unspecified | unspecified | complaints per heat event |

Two things fall out immediately, and neither requires any arithmetic.

**Source D is about a different quantity.** A test rig has no feeder main. Mechanism B — friction loss along an old, undersized main — cannot occur in it. So D measures what a pump does, which is a real and useful thing, and it is not what happens in a zone.

**Source C's variable is not defined.** Member utilities report "complaints" against no enforced definition. Some count calls; some count distinct properties; some count only complaints that survived triage. Fourteen hundred zones of an unspecified quantity is fourteen hundred zones of something.

And **source A carries Chapter 7's problem forward** unchanged: four different actions are recorded as *pump upgrade*, so its −2.4 is an average over a mixture nobody recorded.

**Three of the five are not about the utility's question, and this was determined before any weighting rule was chosen.**

### Why this step gets skipped

Five numbers in a table are an invitation. They are the same kind of thing, in the same units, pointing the same direction, and the natural next act is to combine them.

**The question of whether they are about one quantity has to be imported from outside the table**, and nothing in the presentation prompts it.

Worse, the sources arrive having each done their own §2. Every one of them defined its quantity carefully, for its own purposes, and said so somewhere in a methods section nobody reads. The neighbouring utility was not careless about terrain; terrain was simply not a variable in a study where every zone was flat. The manufacturer was not hiding that a rig has no feeder main; a rig test is *for* isolating the pump.

**Every source is fit for its own purpose and none was built for yours**, which is why the check has to be done by the person combining rather than by the people who produced them.

### The general problem has a name

This situation is not peculiar to water utilities, and it has been given a name and a framing.

> "we address the problem of data fusion—piecing together multiple datasets collected under heterogeneous conditions (i.e., different populations, regimes, and sampling methods) to obtain valid answers to queries of interest." [@bareinboim2016fusion, p. 7345]

**Three kinds of heterogeneity, named on the page.** Different populations. Different regimes. Different sampling methods.

Not different noise levels. Not different sample sizes. Different **circumstances of production** — which is Chapter 4's subject, asked of five sources at once.

### Design is part of what a dataset is

The same page offers a phrase worth carrying:

> "One unique feature of the SCM framework, essential in big data applications, is the ability to encode mathematically the method by which data are acquired, often referred to generically as the 'design.' This sensibility to design, which we can label proverbially as **'not all data are created equal'**" [@bareinboim2016fusion, p. 7345]

The book has been walking toward that sentence for five chapters. Chapter 3 asked what the numbers stand for. Chapter 4 asked why these records and not others came to exist. Chapter 7 asked how treatment was allocated. Chapter 8 asked how the analysis was conducted.

Every one of those is a question about **how the data came to be**, and the answer is not context surrounding the dataset. It is part of the dataset, and a source that arrives without it has arrived incomplete.

### Only one of the three failures is new

The same page separates three problems that ordinary practice runs together:

> "The problems represented in these archetypal examples are known as confounding bias (Fig. 1, tasks 1 and 2), sample selection bias (Fig. 1, task 3), and transportability bias (Fig. 1, task 4)." [@bareinboim2016fusion, p. 7345]

Map them onto what you already have.

**Confounding bias** is Chapter 7. Source A has it, by its own allocation rule.

**Sample selection bias** is Chapter 4, and Chapter 7's positivity. Source C has it: participation in the benchmarking scheme is voluntary, so the fourteen hundred zones are the zones of utilities that chose to join and chose to report.

**Transportability bias** is new, and it is §5.

**Two of the three failures you can already diagnose**, which is why this chapter is twenty-eight pages rather than forty.

It is also worth noticing that the three are not degrees of the same problem. Confounding is about what happened inside a study. Selection is about who got into it. Transport is about whether its answer reaches you. **A source can be flawless on the first two and useless to you on the third**, which is why §5 exists as its own section rather than as a caveat at the end of §3.

### Population, and three words that are not synonyms

One attribute in the table deserves more than a column, because it is where most of the trouble lives and because the vocabulary is slippery.

**The target population** is whom the decision is about. For the utility: Hillcrest, during heat events, next summer.

**The study population** is whom a source actually observed. For source B: forty flat-ground zones in a neighbouring network.

**The source population** is whom that study's sampling drew from — the pool the study population came out of. For source C: utilities that joined a voluntary benchmarking scheme, and within them the zones those utilities chose to report.

These three come apart routinely and the words get used interchangeably, which hides the gaps. A source can be perfectly representative of its source population, which is itself a self-selected slice of the industry, which does not contain your zone.

The formal literature is direct about the consequence:

> "Because participation cannot be mandated, we cannot guarantee that the study population would be the same as the population of interest." [@bareinboim2016fusion, p. 7350]

**Whenever a report says "the population", ask which of the three it means.** In the utility's five sources the answer differs every time, and not one of the five says so on its front page.

### A note on where the test came from

The attribute-by-attribute comparison above is **this book's own extension** of Chapter 7's material, not something either source states. What the sources supply is that heterogeneity in populations, regimes, and sampling methods is the general problem. Turning that into a checklist you can run against five reports on a desk is the book's move, and it is labelled here so that a reader can weigh it as such.

### What to do with a source that is about something else

A reader who has just eliminated three of five sources may conclude the exercise has gone badly. It has not, and §5 explains why, but the shape of the answer belongs here.

**A source that does not answer your question can still supply a piece of an argument that does.**

Source D — six rigs, no feeder main — cannot tell you what happens at Hillcrest. It can tell you, cleanly and under controlled conditions, exactly what a given pump delivers at a given duty point. That is one of the two terms you need if you want to reason from hydraulics rather than from records, and it is the only source in the room that supplies it without contamination.

Source C — fourteen hundred zones, undefined variable — cannot supply an effect estimate. It can supply something else nobody has asked it for: **a membership list.** If a hilltop zone with a sixty-year-old main has ever been upgraded anywhere in the country, that list is where to look.

**Sources are not admitted or rejected. They are asked what they can answer**, and the answer is frequently not the question they were commissioned for.

### Task: which are about your question?

For each of the five sources:

1. Write what quantity it is an estimate of, in one sentence with a population and a comparison.
2. Mark whether that quantity is the one the utility needs.
3. For any you mark no, say whether the source is **useless**, or **useful for something else**.

Question 3 is the one that matters. The answer for source D is emphatically the second, and §5 explains what it is useful for.

## 3. Combining Is Not Averaging

Suppose §2 has been done and you have decided which sources bear on your question. Now the weighting.

### First, the case for combining

It would be easy to read this chapter as an argument against putting sources together. It is not, and the source that supplies its framing says so first:

> "The availability of multiple heterogeneous datasets presents new opportunities to big data analysts, because the knowledge that can be acquired from combined data would not be possible from any individual source alone." [@bareinboim2016fusion, p. 7345]

**Knowledge that no individual source could give you.** That is a strong claim and the paper means it: sources that each fail to answer a question can jointly answer it, when what each contributes is understood.

And then the second sentence, which is this section:

> "However, the biases that emerge in heterogeneous environments require new analytical tools." [@bareinboim2016fusion, p. 7345]

Both halves. Combining is more powerful than any single source **and** introduces failures no single source has.

### Four rules, four answers

Take the five estimates and apply four rules that a competent person would defend.

**Simple average of all five.**

`(−2.4 − 3.1 − 0.6 − 4.8 − 1.5) ÷ 5 = ` **−2.48**

**Median of all five.** Order them: −4.8, −3.1, −2.4, −1.5, −0.6. The middle is **−2.40**. Robust to the extremes, which is the usual argument for it.

**Weight by sample size.** The rule that feels most principled, because bigger studies carry more information.

`(15 × −2.4 + 40 × −3.1 + 1400 × −0.6 + 6 × −4.8) ÷ 1461 = −1028.8 ÷ 1461 = ` **−0.70**

**Drop the source with the known defect and average the rest.**

`(−2.4 − 3.1 − 4.8) ÷ 3 = ` **−3.43**

| Rule | Result |
|---|---:|
| Simple average | **−2.48** |
| Median | **−2.40** |
| Weight by size | **−0.70** |
| Drop C, average the rest | **−3.43** |

**A range of −0.70 to −3.43, a factor of nearly five, with no arithmetic error anywhere.**

Notice that nothing above is a mistake. Each rule answers a reasonable question.

The **simple average** treats the five as five independent opinions of equal standing. That is defensible when you have no basis for ranking them and no reason to think any is contaminated.

The **median** is the same idea, made robust to one source being wildly off. It is what you use when you suspect an outlier and do not know which.

**Size weighting** treats each source as a bundle of observations and pools them, which is what you would do if the five were samples from one population differing only in how many you drew.

**Dropping a source** treats quality as a gate rather than a weight — in or out, no partial credit.

**Four different beliefs about what the five sources are**, none of them silly, producing four answers spanning a factor of five. And in a report, only one of them will appear.

### Pause: which would you have used?

Before reading on, write two or three sentences.

> **Which of the four rules would you have reached for? And what does it assume?**

---

Most readers reach for size weighting, and it is worth seeing what it did.

| Source | n | Share of the weight |
|---|---:|---:|
| A | 15 | 1.0% |
| B | 40 | 2.7% |
| **C** | **1,400** | **95.8%** |
| D | 6 | 0.4% |

**Source C received 95.8% of the weight.** It is the source whose variable has no enforced definition and whose participation is voluntary.

The size-weighted answer of −0.70 is, to a good approximation, source C's answer with three decorations attached.

### Size is not worth

That is not a fluke of these numbers. There is a published claim about it:

> "When combining data sources for population inferences, those relatively tiny but higher quality ones should be given far more weights than suggested by their sizes." [@meng2018paradox, p. 685]

**Far more weight than their sizes suggest.** Not "size is one factor among several" — a claim about direction and magnitude.

The same source records how large the discrepancy can be. In an analysis of 2016 US election survey data, a data defect correlation of about −0.005 — a number small enough to look like nothing — implied that a self-reported sample of about **2,300,000** people had "the same mean squared error as the corresponding sample proportion from a genuine simple random sample of size n ≈ 400" [@meng2018paradox, p. 685].

**Two point three million, worth four hundred.** About 5,750 to one.

Four cautions come with that figure and all four bind here.

**This is not an argument that big datasets are bad.** The claim is conditional on data quality not being accounted for; a large dataset whose defect correlation is near zero is excellent.

**The figure belongs to that specific dataset and that specific question.** It is an empirical estimate, not a general exchange rate.

**The −0.005 is a correlation between being recorded and the value recorded.** It is not a bias, a rate, or a percentage.

**And the mathematics behind it is not taught here.** Chapter 4 declined it, Chapter 8 declined it, and this chapter declines it a third time. What transfers is the direction of the correction.

The usable form, which is this book's phrasing:

> **Sample size measures how much of a source you have. It does not measure how much it is worth.**

### And the sources may not be five sources

Here is a problem that no arithmetic will reveal.

Ask three questions about the five reports and the answers are these.

**The neighbouring utility (B) is a member of the benchmarking scheme (C).** Its forty zones are inside the fourteen hundred. Averaging B and C counts those forty twice.

**Two of the five panel members (E) served on the working group that wrote the benchmarking scheme's complaint definition.** Their judgment was formed on the same conventions that produced C.

**The manufacturer's rig protocol (D) was written against that same definition.**

So the five sources share data, share a measurement convention, and share people.

**Agreement among dependent sources is cheap.** If four of the five agree, that may be four independent confirmations or it may be one convention reported four times, and the five numbers look identical either way.

**A note on this passage.** No source in this book's bibliography supports it. It follows directly from what dependence means, and the book states it as its own reasoning rather than attributing it. That is the fourth time this book has taught something with no source behind it, and the governing decision record for this chapter refers the pattern to the author rather than treating three previous instances as permission.

What can be said with confidence is narrower and still useful: **the three facts above are answerable by three emails**, and nobody sent them.

There is a further reason dependence is hard to see, and it is worth one paragraph.

**Independence is invisible and dependence is invisible.** Five numbers look the same either way. There is no diagnostic you can run, no statistic that flags it, and no property of the table that distinguishes five independent estimates from one convention reported five times. The only way to find out is to ask how each source came to exist and who was involved — which is Chapter 4's question again, and which is answered by people rather than by data.

And the direction of the error is unhelpful. Dependence makes sources **agree more** than independent sources would, so its effect is to increase your confidence exactly when it should not. A room looking at five agreeing numbers feels well informed. The same room looking at five disagreeing numbers feels troubled — and is often better off, because disagreement at least establishes that the sources were free to disagree.

### A rule of thumb that does not work

At this point a reader reasonably wants a shortcut, and there is a popular one: **weight by quality instead of by size.**

It sounds like exactly the correction the previous pages argued for. It does not work, for a reason worth being clear about.

**Quality is not a number you have.** To weight by it you would need to score each source, which means deciding how much a voluntary participation defect costs relative to an undefined variable, relative to an unallocated treatment mixture, relative to a rig with no main. Those are not commensurable, and any scoring scheme you invent will encode your judgment about which defect matters — which is fine, and is a judgment that should be argued about rather than buried in a weight.

There is a second problem. **The defects are not independent of the estimates.** Source C's undefined variable is plausibly *why* its estimate is smallest: if some members count only complaints surviving triage, their counts are lower and less responsive to anything. So a quality weight is not correcting noise; it is deciding how much of a systematic difference to believe.

**Which is why the recommendation below is a table rather than a rule.** Not because weighting by quality is wrong in principle, but because doing it honestly means making the judgments visible, and once they are visible you have a table.

### So what should you do?

Not pick a better rule. There isn't one, and this chapter deliberately teaches none.

**Compute several defensible rules and report the spread.**

That is Chapter 8's discipline arriving in a new setting. There, four defensible analyses of one record produced four estimates, and the honest report was the table rather than the winner. Here, four defensible weightings of five sources produce a range from −0.70 to −3.43, and the honest report is that range together with what each rule assumed.

A committee told "the effect is about −2.5" has been given a number. A committee shown four rules spanning −0.70 to −3.43, with the note that the largest source carries 96% of the weight under one of them, has been given the situation.

**And the spread is the more actionable output.** A single number invites the committee to accept or reject it. A range with its rules attached invites them to ask which rule they believe, which is a question they are actually qualified to answer — they know things about the benchmarking scheme's members that no analyst does.

### And what to say in March

The asset committee will not accept "it depends" and should not have to.

Here is a form that fits on one slide and does not require a single combined number.

> **What the five sources say about upgrading a duty pump: between −0.7 and −3.4 fewer complaints per heat event, depending on how they are weighted.**
>
> The spread is not measurement error. It is the difference between four defensible ways of combining sources that were built for different purposes. Under the rule that weights by sample size — the most common one — the industry benchmark carries 96% of the weight, and it is the source whose complaint definition is not enforced across members.
>
> **Two of the five are about a different quantity.** The manufacturer's rig has no feeder main; the benchmark's variable is undefined.
>
> **And none of the five contains a zone like Hillcrest.** No source has a feeder main older than forty years; Hillcrest's is sixty-eight. §5 covers what would change that.

Four short paragraphs, no synthesis, and a committee reading it knows more than one reading "the effect is about −2.5" — including the one thing that decides the question, which the combined number does not contain.

### Task: four rules and three emails

1. Compute all four rules yourself and check them against the figures above.
2. For each, write the assumption in the form *this rule is right if ___*.
3. Then list the **three emails** you would send to find out whether the five sources are five sources.

## 4. Replication, and What It Does Not Settle

The utility could commission a sixth study.

Suppose it does, and suppose the result comes back at −2.6 — comfortably inside the range, agreeing with the average of the others. What has been bought?

### Successful replication settles less than it looks

> "Without further understanding and analysis, even successful replication tells us little either for or against simple generalization or to support for the conclusion that the next will work in the same way." [@deaton2016rct, p. 27]

That runs hard against intuition. A result found once, then again, then again, feels progressively safer to carry somewhere new.

The claim is that **without an account of why the result holds**, the accumulation says little about whether it holds in a place you have not looked.

### And failure settles less than it looks either

> "Nor do failures of replication make the original result useless." [@deaton2016rct, p. 27]

With the constructive version overleaf:

> "We often learn much from coming to understand why replication failed and can use that knowledge, in looking for how the factors that caused the original result might operate differently in different settings." [@deaton2016rct, p. 28]

**A failed replication is a finding about the difference between two settings.** Which is usually more informative than either result, because a difference points at what matters.

You have met this shape twice. Chapter 5: a failed check tells you a formulation is inadequate and not where. Chapter 7: a verdict of *not identified* tells you which assumption the argument turns on. In all three, the negative result is a direction to look rather than the end of the exercise.

### The chicken

The source gives an illustration, and it is the most useful thing in this section.

> "Bertrand Russell's chicken (Russell (1912)) provides an excellent example of the limitations to straightforward extrapolation from repeated successful replication. The bird infers, on repeated evidence, that when the farmer comes in the morning, he feeds her. The inference serves her well until Christmas morning, when he wrings her neck and serves her for dinner." [@deaton2016rct, p. 28]

Then the diagnosis:

> "Though this chicken did not base her inference on an RCT, had we constructed one for her, we would have obtained the same result that she did. **Her problem was not her methodology**, but rather that she did not understand the social and economic structure that gave rise to the causal relations that she observed." [@deaton2016rct, p. 28]

**Sit with the middle clause.**

Every quality control in this book would have passed. The chicken's record is long. Her observations are accurate. The pattern is real and it replicates every single morning. Her sample size grows daily. There is no confounding — the farmer's arrival really does precede the feeding — no measurement error, no analytic flexibility, no threshold ritual, and no defect an auditor could name.

What she lacks is knowledge of the structure that produced the pattern. It is not in her record, it could not be got from more of her record, and it decides everything.

*Russell (1912) was not obtained for this book. The illustration is used as reported at the page cited, and nothing here describes Russell's own text or purpose.*

### Pause: what would a sixth study buy?

Before reading on, write two or three sentences.

> The utility commissions a sixth study. It comes back at **−2.6**, agreeing with the others.
>
> **What has the utility learned about Hillcrest?**

---

**Almost nothing — unless the sixth study contains a zone like Hillcrest.**

A hilltop zone, with a feeder main past sixty years old, upgraded and observed. If it contains one, it is worth more than the other five combined. If it does not, it is a sixth confirmation of a pattern in places unlike the one the committee is deciding about.

And note that the utility can find this out **before commissioning anything**, by asking one question about the proposed study's population. That question costs an email. The study costs a year.

### What replication is actually good for

Having spent two pages on limits, the positive case deserves stating, because replication is not worthless and the section would mislead if it stopped at the chicken.

**Replication across *different* settings is worth far more than replication across similar ones.** Five studies in five kinds of place, agreeing, tell you something about how widely the effect's support factors are distributed. Five studies in five similar places, agreeing, tell you the effect is real in that kind of place. Both are useful and they are not the same finding, and the count of studies does not distinguish them.

**Replication that fails is where the information is.** Two settings, one effect, one non-effect: something differs, and finding what differs is how support factors get identified in the first place. §5's terrain fact is exactly the kind of thing a failed replication would have surfaced.

**And a replication designed to differ deliberately is worth more than one designed to match.** A study that copies the original's conditions as closely as possible tests whether the original was right. A study that varies one condition on purpose tests whether the effect needs that condition — which is the question you actually have.

The utility's sixth study, if it commissions one, should therefore be chosen for what it varies rather than for how large it is.

**Which reverses the usual procurement instinct entirely.** Asked to fund one more study, an organisation asks how big it can be. The more useful question is which condition it would differ in — and for the utility the answer is obvious, sitting in §5, and would produce a smaller and far more informative study than anything the budget would otherwise buy.

### The sentence that stings

> "So, establishing causality does nothing in and of itself to guarantee generalizability." [@deaton2016rct, p. 28]

The authors go further, naming what a purely local causal finding amounts to: effects "that may have only local applicability, what might be labeled 'anecdotal causality'" — their phrase, aimed at practice in their own field.

**This is uncomfortable after Chapter 7**, and it should be said plainly rather than softened. A reader who has just spent forty pages learning what it takes to establish that an effect is real may reasonably feel they have arrived somewhere.

They have. Identification is not wasted — an unidentified effect cannot be transported either, since there is nothing established to carry. But identification is a **prerequisite** for transport, not a substitute for it, and the second step is the one most analyses skip because the first was so much work.

**A note on this source.** It is an NBER working paper whose cover states that such papers have not been peer-reviewed, and the refereed version could not be obtained for this book. Its strongest claims — including "anecdotal causality" — are its authors' positions in a live argument, reported as theirs.

### What Chapter 7 still buys you

It is worth being precise about what survives, because a reader could take the last few pages as saying that identification does not matter.

**An unidentified effect cannot be transported.** There is nothing established to carry. Chapter 7's verdict on the utility's own record was not superseded by finding four more sources; it was joined by four more sources with their own problems.

**Identification tells you what a result is a result about**, which is the input to every transport question. You cannot ask whether an effect's support factors are present in your setting until you know which effect, of what, compared with what.

**And the two steps fail differently, which is diagnostically useful.** A failure of identification says the study cannot establish its own claim. A failure of transport says the study establishes its claim and the claim is about somewhere else. Those call for different responses — the first for a different design, the second for a different setting or an argument about mechanism.

The order is fixed: identify, then transport. Skipping the first makes the second meaningless; skipping the second makes the first local.

## 5. Will It Work Here?

Now the word after the dash.

### A term you will meet, and should not organise your thinking around

> "Suppose a trial has established a result in a specific setting. If `the same' result holds elsewhere, it is said to have `external validity'. External validity may refer just to the transportability of the causal connection, or go further and require replication of the magnitude of the ATE. Either way, the result holds—everywhere, or widely, or in some specific elsewhere—or it does not." [@deaton2016rct, p. 27]

You will meet that phrase constantly. Here is the objection, from the same page:

> "This binary concept of external validity is often unhelpful because it asks the results of an RCT to satisfy a condition that is neither necessary nor sufficient for a trial to be useful, and so both overstates and understates their value." [@deaton2016rct, p. 27]

**Neither necessary nor sufficient.**

Not necessary: a study can be enormously useful without its result holding anywhere else. Source D — six rigs, no feeder main — will never produce a number that applies to Hillcrest, and it is the only source that isolates what the pump alone does, which is exactly what you need to reason about mechanism.

Not sufficient: a result holding elsewhere does not make it useful for your decision. If the industry benchmark's −0.6 holds in every zone in the country, it is still an average over an undefined variable.

**Register the term as a hazard**, the way Chapter 8 registered `statistical significance`: know it when you see it, and do not build on it.

The better question form has its own name.

> transportability "lies at the heart of every scientific investigation because, invariably, experiments performed in one environment are intended to be used elsewhere, where conditions are likely to be different." [@bareinboim2016fusion, p. 7350]

Not *is this result externally valid*, which invites yes or no. **Does this carry to my setting, and under what conditions** — which invites an answer you can go and check.

### What makes a result carry

Here is the idea that turns transport from a caveat into a question you can work.

> "The operation of a cause generally requires the presence of 'support factors', without which a cause that produces the targeted effect in one place, even though it may be present and have the capacity to operate elsewhere, will remain latent and inoperative." [@deaton2016rct, p. 28]

The source's own example, on the same page: a house burns down because a television was left on — "although televisions do not operate in this way without support factors, such as wiring faults, the presence of tinder, and so on."

The television is a real cause. It is also present in millions of houses that do not burn down, because the supporting conditions are absent.

And the consequence for averages is exact:

> "two populations will have the same ATE if and only if they have the same average for the net effect of the support factors necessary for the treatment to work" [@deaton2016rct, p. 29]

Followed by the observation that makes it bite:

> "These are however just the kind of factors that are likely to be differently distributed in different populations" [@deaton2016rct, p. 29]

**So transport is not a statistical adjustment.** There is no correction to apply, because what you need to know is which conditions the cause requires and whether your setting has them. That is subject-matter knowledge, and it is in neither dataset.

### Support factors are not confounders

Two Chapter 7 words sit close to this one and the distinction is worth fixing.

A **confounder** is something that distorts your estimate of an effect — it makes the number you computed wrong for the setting you computed it in. Chapter 7's whole apparatus is about identifying and handling them.

A **support factor** does not distort anything. Your estimate can be perfectly correct for the setting it came from, with every confounder handled and every identification condition met, and still not apply elsewhere because the condition the cause needs is absent there.

**Confounders make an estimate wrong here. Missing support factors make a correct estimate irrelevant there.**

Which is why Chapter 7's work cannot substitute for this chapter's. A flawlessly identified effect is still an effect in the place it was identified.

### The anchor's support factor

Hillcrest is a **hilltop** zone.

Its duty pump does two things at once: it overcomes friction along the feeder main, and it lifts water against static head to the top of the zone. When the pump is the binding constraint at Hillcrest, it is binding partly because of the lift.

**Every one of source B's forty zones is on flat ground.**

There, a pump upgrade relieves friction loss and nothing else. There is no lift to restore, because there is no hill.

So the mechanism by which an upgrade would help at Hillcrest **is absent from every zone in the source that produced the largest, cleanest, most convincing estimate.** B's −3.1 is not wrong. It is an answer about a place where one of the two things the pump does at Hillcrest does not arise.

That is a support factor in the source's exact sense: present in one setting, absent in another, decisive for whether the cause operates.

And it is a fact about terrain. Not a statistical caveat, not a limitation paragraph — a fact the utility could establish by looking at a contour map, and which nobody used when the five sources were assembled.

### Pause: which single fact settles it?

Before reading on, write one or two sentences.

> Across all five sources — 15 zones, 40 zones, 1,400 zones, 6 rigs, and 5 engineers —
>
> **which single fact determines whether any of them speaks to Hillcrest?**

---

**No zone in any of the five sources has a feeder main older than forty years. Hillcrest's is sixty-eight.**

Not a small number of such zones. None.

### And you have seen this before

That sentence is Chapter 7's, word for word.

Chapter 7 found the pump question **not identified**, and the sharpest of its three failures was **positivity**: for zones like Hillcrest, the probability of having received an upgrade in the record was zero, so the data contained no comparable case.

Chapter 9 asks whether a result established in the recorded zones applies to Hillcrest, and the answer is that no recorded zone resembles Hillcrest.

**These are the same fact approached from opposite directions.** Positivity asks whether your record contains cases like the target. Transport asks whether a result from the record applies to the target. When the answer to the first is no, the answer to the second follows, and it does not matter which end you start from.

*This identity is the book's own observation. Neither source draws it, and it is stated once here because it is the clearest available evidence that this book's chapters are one architecture rather than a sequence of topics — a failure diagnosed in Chapter 7 with the vocabulary of identification is rediagnosed in Chapter 9 with the vocabulary of transport, on the same fact about a pipe.*

### The other tradition says it too

The formal literature reaches the same place by a different route, and names the specific threat bluntly:

> "This disparity is indeed a major threat to the validity of randomized trials. Because participation cannot be mandated, we cannot guarantee that the study population would be the same as the population of interest." [@bareinboim2016fusion, p. 7350]

With the mechanism spelled out: study populations "may consist of volunteers, who respond to financial and medical incentives offered by pharmaceutical firms or experimental teams, so the distribution of outcomes in the study may differ substantially from the distribution of outcomes under the policy of interest" [@bareinboim2016fusion, p. 7350].

**Two traditions that disagree about method agree about this**, which is worth noticing. One arrives through support factors and subject-matter structure; the other through formal characterisation of how populations differ. Neither thinks a result travels by default.

### Chapter 3, extended

Chapter 3 established **contextual specificity**: a measure valid in one context may be invalid in another [@adcock2001validity, p. 530]. It said so and then explicitly declined to push the point further, reserving the extension for this chapter.

Here it is. Chapter 3's claim was about a measure and a context. Chapter 9's is about a finding and a setting.

Different objects, same shape, and a reader who has held the first for six chapters can have the second in a sentence: **nothing is portable on its own; portability is relative to how the two settings differ in the respects that matter.**

That is the sixth or seventh time this book has said something of that form, and by now it should be a reflex rather than a lesson.

### So what would settle it?

The chapter would fail if it stopped here, because *no source applies* is not an answer a committee can use in March.

Four things would help, and none of them is a sixth study of the same kind.

**Find one comparable case anywhere.** A hilltop zone with a main past sixty, upgraded and observed. One is worth more than the fourteen hundred, and the benchmarking scheme's membership list is the place to look.

**Argue from hydraulics instead of records.** Static lift and friction loss are calculable. What a higher-capacity pump does to pressure at the top of a 68-year-old main is a physics question, and Chapter 2's mechanism reasoning was for exactly this. It is available today.

**Use source D for what it is good for.** The rig cannot tell you what happens at Hillcrest. It can tell you precisely what the pump does, which is one of the two terms in the hydraulic argument above. A source that fails to transport can still supply a component of an argument that does.

**Arrange one case deliberately.** Upgrade one old-main hilltop zone, chosen for reasons unrelated to how bad it is, and watch. Chapter 7 made the same recommendation, for the same reason: an arranged comparison is an assumption made true rather than assumed.

**Notice what the first three have in common.** None requires new data collection, and all three were available before the utility spent a year assembling five reports.

### One more thing worth noticing about the five sources

Go back to the table in §1 and read the estimates against what §5 has established.

| Source | Estimate | What its setting has |
|---|---:|---|
| D — rigs | **−4.8** | pump only; no main, no lift |
| B — flat network | **−3.1** | friction loss; no lift |
| A — own network | **−2.4** | mixed, mains up to 40 years |
| E — panel | **−1.5** | judgment, formed on all of the above |
| C — benchmark | **−0.6** | everything, undefined |

**The estimates are ordered by how little of the real system the setting contains.**

The rig, which has neither an old main nor a hill, gives the largest effect. The flat network, which has a main but no hill, gives the next largest. The utility's own record, which has both but no zone like Hillcrest, gives less again.

That ordering may be a coincidence of five synthetic numbers. It may also be exactly what you would expect if a pump upgrade helps most where nothing else is limiting, and less as more constraints are added.

**Nobody can tell which from the table**, and the chapter is not going to pretend otherwise. But the pattern is a hypothesis about support factors, it is checkable against the hydraulics, and it is the kind of thing a reader who has stopped trying to average the five will notice. **The disagreement was the finding.**

### Task: what would have to be true?

Source B is the largest well-conducted study bearing on the utility's question: forty zones, before and after, a clean design.

1. Write, in three sentences, **what would have to be true of Hillcrest for B's −3.1 to apply there.**
2. For each of the three, say whether the utility already knows the answer, could find out this week, or cannot find out at all.
3. Then answer: is B's estimate useless to the utility, or useful for something other than predicting Hillcrest?

## 6. Expert Judgment Is a Source

Source E has been sitting at the bottom of the table, and it deserves two pages rather than a footnote.

### Neither excluded nor privileged

Five engineers, asked what a pump upgrade would do at Hillcrest, produced a median of **−1.5**.

Two reflexes are available and both are wrong.

**Exclude it, because it is only opinion.** But the five engineers know things no dataset in the room contains — how Hillcrest's pumps behave in August, which zones the benchmarking scheme's members actually report, what the manufacturer's rig omits. Judgment is where most of what an organisation knows lives.

**Privilege it, because they are the experts.** But nobody has ever checked whether this panel's estimates come true.

### You already know what to do with it

Chapter 6 spent twelve thousand words on this and it applies without modification.

The panel is a forecaster. Its estimates are forecasts. And **an unscored forecaster cannot be assessed**, because the relevant property is defined over a record and cannot be read off a single statement.

Chapter 6's forty-briefing table showed a pattern no individual briefing contained. The panel has no such table, so nothing about its reliability is available — not that it is unreliable, which would also be a finding, but that the question has no answer.

**The remedy is Chapter 6's remedy.** Write down what was said, when, conditional on what, and — later — what happened. Five fields, one row per estimate. In three years the utility would know whether to weight this panel heavily, and the reason it does not know now is that nobody started.

And do not treat judgment as broken. The research this book cites on heuristics is explicit that they "are quite useful, but sometimes they lead to severe and systematic errors" [@tversky1974judgment, p. 1124].

### Experts are a dependence problem too

One fact from §3 lands here.

**Two of the five panel members served on the working group that wrote the benchmarking scheme's complaint definition.**

So E and C are not independent. The panel's sense of what a typical complaint reduction looks like was formed on conventions those two members helped establish, and which produced source C's numbers.

Five engineers in a room who trained together, read the same guidance, and use the same software defaults are not five independent assessments. They are frequently one assessment with five signatures — and the room will feel like strong agreement.

### Two pages, and why not more

Expert judgment has a literature, with elicitation protocols, aggregation schemes, and methods for weighting experts by past performance. None of it is here.

The reason is the same one that keeps this chapter to twenty-eight pages. **The utility's problem is not that it lacks a method for aggregating five engineers. It is that nobody has ever written down what those engineers said and checked it.** No protocol repairs that, and the repair costs a spreadsheet.

When an organisation has three years of scored panel estimates and is genuinely stuck on how to combine them, it has a problem worth reading the literature about. Almost none are in that position.

**This is the same judgment the chapter made about synthesis methods**, and it is worth stating once as a general disposition: a method is worth learning when you have the inputs it needs. The utility has none of the inputs that expert-aggregation methods require, and acquiring them is a filing exercise rather than a technical one.

### Task: diagnose five defects

Each statement below contains one defect. Write the defect, what it stops you concluding, and a repair.

1. *"We pooled all five studies, giving us 1,461 observations."*
2. *"Four of the five agree, so the finding is robust."*
3. *"It has been replicated three times, so it will hold here."*
4. *"The trial was internally valid, so the effect is real and applies."*
5. *"There's no evidence it works differently here, so we'll assume it transfers."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

## 7. Cold-Start Practice and Retrieval

### Return to your six-minute answer

Find what you wrote at the start of §1, about which sources you would trust and how you would combine them.

Read it against what you can now produce. Do not score it.

- Did you ask what each source was a number **about**, before weighting anything?
- Did you reach for **size** as the weight?
- Did you say anything about **Hillcrest**, as opposed to about the sources?

Three patterns are common.

Most readers propose a weighting immediately. That is the §2 failure, and it is not carelessness — the five numbers are sitting in a table asking to be combined, and the question of whether they are about one quantity has to be imported from outside.

Many reach for size, which is the rule that hands 96% of the weight to the source with an undefined variable.

Very few write anything about the hilltop. The word after the dash is the half that gets dropped, which is why the central question has it there.

### Independent transfer

Now work an unfamiliar situation, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below. Open only that one.

- [Form A — A hospital trust choosing fall-prevention flooring](transfer-form-a.md)
- [Form B — A bank choosing a fraud-screening rule for a new market](transfer-form-b.md)

Allow about **45 minutes**.
Every fact you need is supplied. Do not look anything up.

Do not open the other form. You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the procedure from memory

Before looking back, write down how you would handle several sources bearing on one decision.

Aim for the sequence, not the wording.

1. What quantity does the **decision** need? Population, comparison, variable, window.
2. For each source: what quantity is **it** about? Same attributes.
3. Which sources are about a different quantity, and are they useless or useful for something else?
4. **How did each source come to exist?** Who is in it, who chose to be, what was recorded.
5. Are these sources **independent**? Shared data, shared people, shared definitions.
6. Compute **more than one** weighting rule. Report the spread.
7. Does any rule hand most of the weight to the **worst** source?
8. What **support factor** does the effect require, and is it present in my setting?
9. Does any source contain a case **like mine**? If none does, say so.
10. What would settle it — one comparable case, an argument from mechanism, or an arranged comparison?

Step 4 is Chapter 4's question, and it is the one that turns a table of numbers back into five human activities.

Step 8 is the one that requires knowing how the thing works, and it is why this cannot be delegated to whoever holds the spreadsheet.

Step 9 is the one nobody asks, and it usually ends the exercise.

### If the transfer went badly

- **You went straight to weighting.** Reread §2. Whether the sources are about one quantity is prior to how much each counts.
- **You used sample size.** Reread §3. It measures how much of a source you have.
- **You treated agreement as confirmation.** Ask what the sources share before counting them as separate.
- **You found no support factor.** Look for something physical or institutional that the effect needs in order to operate, and ask whether the target setting has it.
- **You concluded that nothing can be known.** §5 ends with four things that would settle it, three of which need no new data.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Do not reread this chapter immediately beforehand, and do not look at the form you have not done.

### What this chapter did not give you

**Any method for combining evidence.** No pooling rule, no weighting scheme, no heterogeneity statistic. The chapter's demonstration is that defensible rules disagree, and teaching one would have taught the rule whose failure is the point. The machinery exists and is depth curriculum.

**Any formal apparatus for transport.** There is a literature that characterises formally when a result can be carried between settings, and it needs the graphical machinery Chapter 7 declined.

**A settled treatment of dependence.** §3's passage on shared data, people, and definitions has no source behind it in this book, and says so. It is the weakest-supported material in Part II and is flagged rather than dressed up.

**Any way to elicit or aggregate expert judgment.** §6 said to keep a record. That is a discipline, not a method.

**And no answer for the utility.** Which is honest: after nine chapters, the pump question at Hillcrest is still open, and the chapters have established precisely why, precisely what would close it, and precisely which of those things cost an afternoon.

### What Part III asks next

Part II is over. It asked what the evidence supports, and its last three chapters answered: not more than the assumptions permit, not more precisely than the model allows, and not here unless the conditions match.

Something has been missing from all of it.

Suppose the utility had a clean answer. Suppose it knew that upgrading Hillcrest's pump would cut complaints by 2.4 per heat event, identified, well estimated, and transportable.

**It still would not know what to do**, because it does not yet have any way to say what it wants. Fewer complaints, at what cost? Complaints from whom — and does it matter that Hillcrest is the zone with the most elderly residents? What about the mains renewal programme the money would otherwise fund? What if the upgrade helps on average and makes the worst days worse?

Not one of those is an evidence question. All of them have to be answered before evidence can tell the utility anything about what to do.

**Part III is called Choose**, and Chapter 10 starts where Part II stops: with values, objectives, and the alternatives that were never on the table.
