---
chapter: 7
part: 2
title: "Targets, Identification, and Causal Claims"
status: drafted
---

# Chapter 7: Targets, Identification, and Causal Claims

## 1. The Question the 91% Cannot Answer

Chapter 6 ended with a number the utility had never had before.

After one hot afternoon with the duty pump running at elevated output, and a recovery of more than 8 metres of head at the top of the zone, belief moved from roughly two-to-one to about **91%** for Mechanism A — the pump's capacity, rather than the feeder main, being what starves Hillcrest.

That number is correct. It carries its conditioning information. It was computed with one multiplication and could be checked by anybody.

And the next sentence in the briefing note is this:

> **Replacing the pump will stop the pressure drops at Hillcrest.**

### Look at the gap

The 91% is about **which mechanism operates**.

The sentence is about **what happens if you act**.

Those are not the same claim, and nothing in Chapter 6's arithmetic gets you from the first to the second. You could be 99% sure the pump is the binding constraint today and still be wrong about what replacing it would do — because replacing it changes the system, and a belief about the current system is not a prediction about the changed one.

Chapter 6 stated this once, in a single paragraph, and promised the argument here.

This is the argument.

### Before reading further: answer the question

Take about **six minutes**.

> **Does the 91% support the sentence? If not, what else would you need?**

Write a few sentences. Be specific about what is missing rather than saying the evidence is weak.

Keep what you write. You will come back to it at the end of the chapter, and the comparison is the point.

---

### What this chapter does

There is a four-step sequence that a widely cited overview describes as what "should be part of every exercise in causal inference" [@pearl2009causal, p. 122]:

> 1. **Define**: Express the target quantity Q as a function Q(M) that can be computed from any model M.
> 2. **Assume**: Formulate causal assumptions using ordinary scientific language and represent their structural part in graphical form.
> 3. **Identify**: Determine if the target quantity is identifiable.
> 4. **Estimate**: Estimate the target quantity if it is identifiable, or approximate it, if it is not.

This chapter is steps 1 to 3. Chapter 8 is step 4.

The structure is not this book's invention, and it is worth saying so, because the temptation to invent a memorable four-step device is strong and the discipline of using established structure where established structure exists is one this book has committed to.

It is also the chapter where six earlier chapters come due.

Chapter 1 told you that association alone is not enough to establish what an action would do, and said the formal treatment was here. Chapter 2 drew two mechanisms for the same association and handed the resolution here. Chapter 3 distinguished whether a measurement means what you think from whether an effect has been established, and put the second here. Chapter 4 named selection as a threat to be dealt with here. Chapter 5 asked you to record your assumptions and left the hardest category of assumption for this chapter to name. Chapter 6 said conditioning is not intervening and stopped.

**Six debts, one chapter.** That is why it is the longest in the book.

### And a warning about what the chapter delivers

Most chapters end by giving you a better answer.

This one frequently ends by establishing that **the question cannot be answered with the evidence available, and would not be answered by more of it.**

That sounds like failure and is not. A verdict of *not answerable with this* tells you to stop paying for more of the same, tells you exactly which assumption the whole argument is resting on, and tells you what a different kind of evidence would have to look like. The four-step sequence above builds it in: step 4 says to approximate the quantity if it is not identifiable, not to abandon the exercise.

It is also, in a great many real analyses, the true answer. A chapter that could not deliver it would be teaching you to always find something.

## 2. Define: What Quantity Are You Asking About?

Step 1 is **Define**, and the source is emphatic about the order: the approach "insists on defining the target quantity, in our case 'causal effect,' before specifying the process of treatment selection, and without making functional form or distributional assumptions" [@pearl2009causal, p. 122].

**Define before design.** Before you consider what data to collect, what comparison to run, or what method to use.

Most readers will feel this step has already been done. The utility asked a clear question in a short sentence: will replacing the pump stop the pressure drops? What is there to define?

This section is six pages long because the answer is: nearly everything.

### One field's answer

Clinical trials are the setting where vagueness about the target became expensive enough to force a fix, because a regulator has to decide whether a drug works and cannot accept a question that shifts after the results arrive.

The resulting guidance sets out attributes that "are used to construct the estimand, defining the treatment effect of interest" [@fda2021estimands, p. 9].

There are five.

**Treatment.** "The treatment condition of interest and, as appropriate, the alternative treatment condition to which comparison will be made" [@fda2021estimands, p. 9]. Not just what you do — what you are comparing it against.

**Population.** "The population of patients targeted by the clinical question" [@fda2021estimands, p. 9]. Which units the answer is about.

**Variable.** "The variable (or endpoint) to be obtained for each patient that is used to address the clinical question" [@fda2021estimands, p. 9]. What gets measured, on each unit.

**Events in between.** Things that happen after treatment starts and change what the measurement means. The guidance calls these intercurrent events and gives named strategies for handling them [@fda2021estimands, p. 10].

**A summary.** "Finally, a population-level summary for the variable should be specified, providing a basis for comparison between treatment conditions" [@fda2021estimands, p. 10]. A mean, a proportion, a risk difference — some rule for turning many units into one number.

**This list is authoritative for its own context and only for its own context.** It is regulatory guidance about drugs, written in the vocabulary of patients and treatments, and this book does not present it as a universal cross-disciplinary definition. What it offers a reader outside clinical trials is the **shape** of the answer, and generalising a shape is a pedagogical move rather than a finding.

The guidance also supplies a warning that generalises without any help: a definition must identify "an effect because of treatment and not because of potential confounders such as differences in duration of observation or patient characteristics" [@fda2021estimands, p. 10].

### Five attributes, five blanks

Now run them at the utility's sentence.

> *Replacing the pump will stop the pressure drops at Hillcrest.*

| Attribute | What the sentence says | What is missing |
|---|---|---|
| Treatment | "replacing the pump" | Which of four things the utility could do — and compared with **what**? Doing nothing? Deferring a year? Relining the main instead? |
| Population | nothing | Hillcrest only? All pumped zones? Hillcrest during heat events, or year-round? |
| Variable | "stop the pressure drops" | Complaints? Metres of head at the top of the zone? Hours below a threshold? These do not move together. |
| Events in between | nothing | A conservation request. The mains renewal programme. A hotter summer. Any of them changes what the measurement means. |
| Summary | nothing | Mean complaints per heat event? Probability of any breach? Worst hour? |

**Five attributes, five blanks.**

And the sentence did not look vague. It looked like an ordinary, competent, actionable claim of the sort that appears in briefing notes every day. That is precisely why the step gets skipped: nothing about the sentence announces that it is underspecified.

### Why the step gets skipped

It is worth being honest about the mechanism, because *be more precise* is advice everybody has received and nobody follows.

**Everyone in the room fills the blanks, silently and differently.** The operations engineer reads "replacing the pump" as the like-for-like replacement in the capital plan. The finance lead reads it as the cheapest option that closes the complaint. The board member who asked the question is thinking about last summer. All three believe they are discussing one claim.

Nothing surfaces the disagreement, because a shared sentence feels like a shared question. The analysis then answers whichever version the analyst filled in, and the finding is reported against the sentence rather than against the version — so the room hears three different results and no one notices.

**And the blanks get filled by the data.** This is the more damaging route. An analyst who has not defined the target quantity in advance will define it, without deciding to, from whatever the records happen to support. The population becomes the zones with complete records. The variable becomes the field that was logged. The comparison becomes whatever the register distinguishes.

That is a target quantity chosen by the filing conventions of the last twelve years, and it will be reported as an answer to the board's question.

**A filled-in target quantity is therefore a contract**, not a formality. It says what will be answered, before anybody knows how it comes out, and it is the one document that stops the question drifting toward the answer.

### The same sentence, two different questions

Fill the blanks two ways and you get two claims that are both faithful to the original and are not the same claim.

**Version one.**

> Among **heat events at Hillcrest**, the difference in **mean low-pressure complaints per event** between a world where the utility **installs a variable-speed drive on the existing duty pump** and a world where it **does nothing**, over the **three years following installation**, with any **conservation request** left in place as it would occur.

**Version two.**

> Among **all fifteen pumped zones**, the difference in **mean hours per year below the pressure threshold** between a world where each zone **receives a higher-capacity duty pump** and a world where each **keeps its current pump**, over the **first year**, **excluding** any zone that receives mains renewal in the same period.

Different treatment. Different population. Different variable. Different window. Different handling of what happens in between.

**These can have opposite signs.** Under Mechanism B, where friction loss along an old main is what limits pressure at the top of the zone, pushing more water through the same main could make things worse — so Version two's higher-capacity pump could increase hours below threshold in exactly the zones Version one's variable-speed drive helps.

And a third version is available that is not about pumps at all:

> Among **heat events at Hillcrest**, the difference in **mean low-pressure complaints per event** between a world where the utility **relines the feeder main** and a world where it **replaces the duty pump**, over the **three years following**, with everything else as it would occur.

That one has no *do nothing* arm. Its comparison is between two actions the utility could take with the same money, which is frequently the comparison a decision actually faces and almost never the comparison an analysis reports.

**The comparison is an attribute, not a detail.** *Does the upgrade work* and *is the upgrade the best use of the budget* are different questions with different answers, and only the first survives being asked without a named alternative.

One English sentence. Two target quantities. Possibly two different signs.

**That is the argument for step 1**, and it is not about rigour or neatness. An analysis that answers Version two and reports it as an answer to the original sentence has not been imprecise. It has answered a different question and said nothing about it.

Notice also what the two versions did to the rest of the work. Version one is about one zone over three years and could plausibly be studied by watching Hillcrest. Version two is about fifteen zones over one year and would need the whole network's records. **Defining the target quantity did not just clarify the question — it determined which evidence is even relevant**, which is why the source insists the step comes before any of that gets chosen.

### Three words, kept apart

The book has now used three terms for closely related things, and they need separating before the chapter goes further.

**`target`** is Chapter 1's informal word for what an inquiry is trying to determine. It stays informal, and the noun that follows it carries the meaning.

**`target quantity`** is the thing defined at step 1 — framework-neutral, presupposing no population, no treatment, and no statistical model. This is the chapter's general term.

**`estimand`** is a target quantity with its attributes filled in. Version one and Version two above are estimands; the original sentence was not.

Two further words belong to Chapter 8 and must not be confused with these. An **estimator** is the procedure you use to get a number. An **estimate** is the number it produces. Chapter 1 already told you these are three different things; this chapter is where the first of the three gets its formal treatment, and Chapter 8 is where the other two do.

### A second field, arriving at almost the same list

There is a device from causal inference that does the same work by a different route.

For any causal effect, imagine the randomized experiment that would measure it. Write out that experiment's protocol. The components to specify are "eligibility criteria, interventions (or treatment strategies), outcome, follow-up, causal contrast, and statistical analysis" [@hernan2019whatif, p. 37].

That is the **target trial**, and §6 is about using it. Here it is worth setting the two lists side by side.

| Estimand attributes | Target trial protocol |
|---|---|
| Treatment | interventions / treatment strategies |
| Population | eligibility criteria |
| Variable | outcome |
| Events in between | follow-up |
| Summary | causal contrast |
| — | statistical analysis |

**This table is the book's own alignment.** Neither source draws it, and the correspondence is close rather than exact.

What the convergence licenses saying: a regulator and a methods textbook, working in overlapping but distinct traditions with different pressures on them, arrived at roughly the same set of things you must write down before you have asked a question. That is some evidence that the set is about the problem rather than about either field's habits.

What it does not license: claiming the lists are the same list, that either is complete, or that the rows map exactly. *Follow-up* and *events in between* overlap and are not the same idea, and one list has a sixth row the other has no counterpart for.

That sixth row is worth a sentence. *Statistical analysis* appears on the target-trial protocol and has no counterpart among the estimand attributes, and the omission is deliberate on both sides: the attributes define **what** is being estimated, and the analysis is **how**. Chapter 1 separated those and Chapter 8 owns the second. A protocol includes both because it is a plan for conducting something; a target quantity includes only the first because it is a statement of what the question is.

If you take one habit from this section, take that separation. **The question is not allowed to depend on the method**, and an analysis whose target quantity shifted when the method changed has told you something about the analyst rather than about the world.

### Task: fill the five

Take the utility's sentence.

> *Replacing the pump will stop the pressure drops at Hillcrest.*

1. Fill all five attributes. Commit to specific choices; do not write "to be determined".
2. Then mark the choices somebody could reasonably disagree with, and say what they would choose instead.

The second part is the harder one and the more useful. A filled-in target quantity is not a neutral restatement of the question — it embeds judgments about what matters, and writing them down is what makes them arguable rather than invisible.

## 3. Three Different Questions About the Same Pipe

Step 2 is **Assume**, and before you can state an assumption you need to know what kind of claim you are making. This section is about a distinction that decides which assumptions you will need.

### A line you can apply

There is a criterion sharp enough to use on a real sentence:

> "An associational concept is any relationship that can be defined in terms of a joint distribution of observed variables, and a causal concept is any relationship that cannot be defined from the distribution alone." [@pearl2009causal, p. 99]

In plainer form: **could you write this down using nothing but what you observe?** If yes, it is associational. If no, it is causal, and it will need something from outside the data.

The same section lists both sides. Associational: "correlation, regression, dependence, conditional independence, likelihood, collapsibility, propensity score, risk ratio, odds ratio, marginalization, conditionalization, 'controlling for'" [@pearl2009causal, pp. 99–100]. Causal: "randomization, influence, effect, confounding, 'holding constant,' disturbance, spurious correlation, faithfulness/stability, instrumental variables, intervention, explanation, attribution" [@pearl2009causal, p. 100].

**Two entries on the second list should stop you.**

`confounding` is a causal concept, not a statistical one. So is `randomization`. A great deal of applied practice treats both as things you handle with a procedure — run this adjustment, apply this design — and both sit on the side of the line where a procedure alone cannot reach.

§4 returns to confounding, because the consequence is severe.

### The three questions

Take one situation — Hillcrest, the duty pump, twelve years of network records — and ask three things that sound similar and are not.

**Association.** *Among the zones that had pump upgrades, what happened to complaints?*

This is a question about the records. Everything needed to answer it is in the distribution of what was observed. It is arithmetic on a table, and §5 does it.

**Intervention.** *If we upgrade Hillcrest's pump, what happens to complaints?*

This is a question about a world that does not exist yet. No amount of staring at what happened to other zones answers it directly, because those zones were not upgraded by you, for your reasons, in Hillcrest's condition.

**Counterfactual.** *Hillcrest was not upgraded, and complaints rose. Would they have risen if it had been?*

This is a question about a world that never existed, concerning a case whose actual outcome you already know. It is the hardest of the three.

### The notation, announced

The book went five chapters with no notation at all. Chapter 6 took one bounded exception — the conditioning bar, and odds — and said why: the difference between *the probability of A given B* and *the probability of B given A* is invisible in spoken English and obvious with a bar.

This chapter takes a second bounded exception, and the reason is the same kind of reason, stated by the source:

> "any mathematical approach to causal analysis must acquire new notation for expressing causal relations – probability calculus is insufficient." [@pearl2009causal, p. 100]

The problem is that these two sentences look identical:

> The probability that pressure recovers, given that the pump was replaced.
>
> The probability that pressure recovers, if we replace the pump.

*Given that* and *if we* — three words apart, spoken almost interchangeably, and they are the association question and the intervention question respectively.

So, from here:

> **`P(pressure recovers | the pump was replaced)`** — observing. Among cases where the pump happened to be replaced, how often did pressure recover?
>
> **`P(pressure recovers | do(replace the pump))`** — intervening. If we impose the replacement, how often does pressure recover?

And, for structure, arrows written inline:

> `heat → demand → pressure at the top of the zone`

That is the complete list. No potential-outcome sub- or superscripts, no rules for manipulating `do(·)`, no formal diagram conventions, no blocking or path vocabulary as machinery.

**A note on the choice.** There are two established notations for this and both are in wide use. `do(·)` is used here because it is the smaller change — it puts one marker inside a bar the reader already reads fluently, rather than introducing a new object with its own indexing conventions. **That is a pedagogical judgment about this book's readers, not a claim that one framework is better than the other.** §4 comes back to the two traditions.

### The rule that governs everything after this

Here is the sentence the rest of the chapter depends on:

> "one cannot substantiate causal claims from associations alone, even at the population level—behind every causal conclusion there must lie some causal assumption that is not testable in observational studies." [@pearl2009causal, p. 99]

The same article calls it a golden rule and restates it: "behind any causal conclusion there must be some causal assumption, untested in observational studies" [@pearl2009causal, p. 100].

Read the qualifier. **Even at the population level.** This is not a claim about small samples or noisy measurement. If you had the entire population, measured perfectly, forever, you would still need the assumption.

The reason is stated in one line:

> "There is nothing in the joint distribution of symptoms and diseases to tell us that curing the former would or would not cure the latter." [@pearl2009causal, p. 99]

A distribution describes how things vary together under the conditions that produced it. It contains no information about how it would look under different conditions, because — as the same page puts it — the laws of probability do not dictate how one property of a distribution changes when another is modified.

**So every causal claim you have ever read rests on an assumption that its data could not test.** The good ones say what it is.

### Pause: which question is the board asking?

Before reading on, write two or three sentences.

> The utility's board has been told the pump is 91% likely to be the constraint, and complaints at Hillcrest rose again last summer. **Which of the three questions is the board actually asking?**

---

Most boards ask the third.

Not *what should we expect if we act*, which is the intervention question, but *was last summer's failure caused by not having acted* — which is counterfactual, about a case whose outcome is known, and which carries an implicit question about whose fault it was.

That question is the hardest of the three and frequently has no answer available. The overview records that "attributional queries are generally not identifiable in nonparametric models" [@pearl2009causal, p. 121] — which, unpacked, means that even with unlimited data and a correct model of the structure, questions of the form *did this particular thing cause that particular outcome* often cannot be pinned to a single answer.

**The most commonly asked causal question is the one least likely to be answerable.** Recognising which question is on the table is therefore not pedantry; it is the difference between an analysis that could succeed and one that could not.

Why the third is harder than the second is worth one paragraph, because it is not obvious.

The intervention question asks about an average over cases like Hillcrest. You can get at an average without knowing anything about any particular case. The counterfactual question asks about **this** zone, **this** summer, whose actual outcome is fixed and known — and the thing you would need is what that same zone would have done under the other action, at the same moment, with everything else the same. There is no second Hillcrest and no second summer. The two branches are not two observations; they are one observation and one thing that did not happen.

So a rival explanation for last summer cannot be ruled out by collecting more summers. More summers speak to the average.

**The practical move is to redirect the question.** When a board asks whether last summer was caused by inaction, the answerable neighbour is usually the intervention question: what should we expect if we act now. It is not the same question, and saying so is part of the answer rather than an evasion of it — but it is a question that has a route to an answer, and the original frequently is not.

### And a warning aimed at what you just learned

Chapter 6 spent twelve thousand words making you good at prediction — stating probabilities, updating them, being scored on them.

A model that predicts Hillcrest's pressure drops accurately is **not thereby a guide to what happens if you act on any of its inputs.** A predictive relationship may capture association without any causal interpretation, and a variable that predicts well is not automatically a lever you can pull [@shmueli2010predict].

The Hillcrest example makes it concrete. Complaint volume predicts pressure drops very well — complaints go up when pressure goes down. Nothing follows about what happens if you act on complaints.

That example is deliberately silly. The serious versions are not, because the predictor is usually something that looks like a cause: staffing levels, maintenance frequency, a leading indicator on a dashboard. **A dashboard is built for prediction and gets read for intervention**, and nothing on the screen marks the transition.

### Where the slide happens

The three questions are easy to keep apart when they are lined up like that. They are not easy to keep apart in a sentence.

> *Zones with more frequent valve maintenance have fewer main breaks, so increasing maintenance frequency will reduce breaks.*

The first clause is association. It is a statement about the records and could be checked this afternoon.

The second clause is intervention. It is a statement about a world in which somebody changes the maintenance schedule.

**The word carrying the whole weight is *so*.** Everything before it is a fact about a table. Everything after it is a claim about a system under change. And *so* asserts, without argument, that the assumption connecting them holds.

That is what §3's demarcation line is for. Run it on the second clause: could *increasing maintenance frequency will reduce breaks* be written down using only the distribution of what has been observed? It could not. The clause is about a distribution that has never existed.

**Look for the word.** *So*, *therefore*, *which means*, *implying that*, *hence* — in a great many analyses the entire causal claim lives inside one of them, and the assumption it rests on is nowhere on the page.

### Task: write all three

Here is a claim from a different part of the utility's operation.

> *Zones with more frequent valve maintenance have fewer main breaks, so increasing maintenance frequency will reduce breaks.*

1. Write the **association** question this claim's evidence actually answers.
2. Write the **intervention** question the claim makes.
3. Write a **counterfactual** question somebody might ask after a break happens.
4. Say which one the sentence slides between, and where in the sentence the slide happens.

## 4. Identification: Could Any Amount of This Evidence Settle It?

This is the chapter's central section and its central question.

You have a defined target quantity from §2. You know from §3 that a causal claim about it needs an assumption the data cannot test. Step 3 asks: **given assumptions you are willing to make, would the evidence available pin your quantity to a single answer?**

Notice what the question does not mention. It does not mention your dataset, your sample size, or your method. **Identification is settled before any data arrives.**

### The definition, from two traditions

Causal inference has two large traditions that disagree publicly about a great deal. They define this concept compatibly, which is worth knowing.

From the structural tradition, a quantity is identifiable given a set of assumptions if any two models satisfying those assumptions that agree on the observable distribution also agree on the quantity. The author's own restatement:

> "In words, the details of M1 and M2 do not matter; what matters is that the assumptions in A (e.g., those encoded in the diagram) would constrain the variability of those details in such a way that equality of P's would entail equality of Q's." [@pearl2009causal, p. 109]

From the potential-outcome tradition:

> "We say that an average causal effect is (non parametrically) identifiable under a particular set of assumptions if these assumptions imply that the distribution of the observed data is compatible with a single value of the effect measure. Conversely, we say that an average causal effect is nonidentifiable under the assumptions when the distribution of the observed data is compatible with several values of the effect measure." [@hernan2019whatif, p. 27]

Different vocabularies, same content. **Fix the assumptions; ask whether everything you could ever observe pins the answer to one value.** One value, identified. Several values, not.

That the two agree is worth stating because a reader who later meets the framework argument — and it is a real argument, conducted in print by serious people — should know that it is not an argument about what identification means. **This book does not adjudicate that argument**, on the same grounds Chapter 6 declined the argument about what probability fundamentally is: the chapter's work can be done from either side.

### The form to carry

Here is the same idea in the book's own words, which is a formulation of a sourced idea rather than a quotation of one:

> **If two different states of the world would produce exactly the same data — however much of it you collected — and they give different answers to your question, then no amount of that data can settle your question.**

Two things follow immediately, and both are worth more than the definition.

**Identification is settled before data collection.** It is a property of the question, the assumptions, and the *kind* of evidence — not of any particular dataset. You can determine it on a whiteboard, in an hour, before anybody is commissioned to gather anything. Most organisations determine it afterwards, if at all, which is how large data-collection budgets get spent on questions that were never answerable.

**Identification is always relative to assumptions.** There is no such thing as identified full stop. The potential-outcome source puts it exactly:

> "To identify the causal effect in observational studies, we need an assumption external to the data, an identifying assumption." [@hernan2019whatif, p. 27]

**External to the data.** Not derived from it, not checkable against it, not weakened by having less of it or strengthened by having more.

### The sixth time this book has said something of this shape

Chapter 1: an answer is not adequate on its own, but adequate for a stated use.

Chapter 3: a measurement is not valid on its own, but valid for an interpretation.

Chapter 4: a dataset is not trustworthy on its own, but trustworthy for a particular quantity.

Chapter 5: criticism is not sufficient on its own, but sufficient relative to what happens if you are wrong.

Chapter 6: a probability is not high or low on its own, but relative to stated information.

Chapter 7: **a causal quantity is not identified on its own, but identified relative to stated assumptions.**

Six chapters, six vocabularies, one structure. The useful question, when a property is offered as though it stood alone, is always *relative to what* — and the answer is frequently the entire argument.

### Pause: build two worlds

Before reading on. This one takes longer than the others; give it ten minutes and write properly.

> The utility has twelve years of records covering fifteen pumped zones: complaints, upgrades, weather, main ages, everything it collects.
>
> **Describe two states of the world that would produce those same records and that give different answers to "will upgrading Hillcrest's pump reduce complaints?"**
>
> Do not describe measurement error or missing data. Describe two ways the world could actually be.

---

Here is one pair.

**World one.** The duty pump's capacity is what limits refill at Hillcrest. Upgrades were given to the worst-complaining zones, which were the worst because of pump limits, and complaints fell after upgrade because the limit was relieved. Upgrading Hillcrest reduces complaints substantially.

**World two.** Friction loss along old feeder mains is what limits pressure at the top of every affected zone. Upgrades were given to the worst-complaining zones, and complaints fell after upgrade because the separate mains renewal programme reached those zones in the same period. Upgrading Hillcrest's pump does nothing, and a higher-capacity pump makes it slightly worse by increasing flow through a 68-year-old main.

**Both worlds produce the same twelve years of records.** Complaints higher in upgraded zones before, lower after, and the same weather. Nothing in the records distinguishes them, and nothing in another twelve years of the same records would either, because the two worlds are not distinguished by *how much* of that data you have.

**They give opposite answers to the utility's question.**

That is what non-identification looks like. Not a wide interval, not a weak result, not a caveat — two coherent stories, one body of evidence, opposite conclusions.

### Which of the three senses

The word `identification` is used in at least three ways and this book always qualifies it.

**Statistical identifiability** asks whether a model's parameters are pinned down by the distribution that model implies. Two parameter settings that imply exactly the same distribution cannot be told apart by any amount of data. This is an old idea in statistics, and the causal literature had to define its own version precisely because the classical notion — has a unique solution — does not carry over to causal quantities [@pearl2009causal, p. 109].

**Causal identification** asks whether a causal quantity is pinned down by the observable distribution **together with causal assumptions**. This is what the rest of this chapter means.

The difference matters in a specific way. Statistical identifiability can fail because a model is over-parameterised, and the repair is to change the model. Causal identification can fail **when every parameter is estimated perfectly**, and the repair is not available in the data at all.

**Structural identifiability** asks whether a dynamic system's parameters can be recovered from its input-output behaviour — whether, watching what a system does in response to what you feed it, you could work out what is inside. It belongs to Chapter 14 with the rest of the dynamic-systems material, and this book names it here only so that the three-way distinction is on the record. Nothing further about it is taught in this chapter.

### Confounding is not a statistical problem

Now the consequence that most often lands badly.

`confounding` sits on the causal side of §3's demarcation line, and the argument for why is short enough to follow completely.

Suppose confounding could be defined associationally — some pattern in the observed distribution that identifies a variable as a confounder. Then you could find confounders in observational data, adjust for them, and obtain an unbiased causal estimate. You would have produced a causal conclusion with no causal assumption, which contradicts §3's golden rule. So no such definition can be right; the source says exactly that: "Hence the definition must be false" [@pearl2009causal, p. 100].

The consequence is blunt:

> "confounding bias cannot be detected or corrected by statistical methods alone; one must make some judgmental assumptions regarding causal relationships in the problem before an adjustment (e.g., by stratification) can safely correct for confounding bias." [@pearl2009causal, p. 100]

**Cannot be detected.** There is no test you can run on a dataset that tells you whether it is confounded. There is no diagnostic, no statistic, no plot.

The practical form: when somebody says *we checked for confounding*, the useful question is what causal assumption they used to do it, because they cannot have done it without one.

### Not identified is a result

The chapter has now spent several pages on what evidence cannot do, and a reader is entitled to ask what they are supposed to do with a verdict of *not identified*.

**Report it, in a specific form.** The four-step sequence builds it in: step 4 says to "Estimate the target quantity if it is identifiable, or approximate it, if it is not" [@pearl2009causal, p. 122]. Non-identification changes what you do next; it does not end the exercise.

A useful verdict has three parts.

**What is not identified**, stated as a target quantity rather than a topic. Not "the pump question" but *the difference in mean complaints per heat event at Hillcrest between installing a variable-speed drive and doing nothing*.

**Which assumption would change it.** Naming the assumption converts an argument about conclusions into an argument about a premise, which is a much more productive argument and one a domain expert can join.

**What would have to be collected, or arranged, instead.** Sometimes a different design. Sometimes a fact nobody has looked up. Sometimes nothing, and saying so honestly is worth more than a number.

Written out for the anchor, it looks like this:

> **Not identified.** The difference in mean low-pressure complaints per heat event at Hillcrest between installing a variable-speed drive and doing nothing cannot be determined from the network's twelve-year record.
>
> **The assumption that would change it:** that whether a zone received a pump upgrade was unrelated to how bad its complaints were going to be. The programme allocated upgrades to the six worst-complaining zones, so this assumption is false as stated.
>
> **What would change the answer:** a comparison case — one zone with a feeder main over sixty years old that received a pump upgrade. None exists in this record. Failing that, an argument from hydraulics rather than from records, which is a question for the network engineers rather than for the analysts.

Three short paragraphs, no arithmetic, and it took an afternoon.

**A verdict in that form is more useful than most estimates.** It tells a decision-maker what they are actually betting on, which is the thing an estimate with a confidence interval conspicuously fails to tell them.

It also has a property worth noticing: **somebody can disagree with it.** An engineer can say the allocation rule was looser than the analyst thought, or that a comparable zone exists in a predecessor utility's records. Those are productive disagreements about checkable facts. A number with an interval invites no such conversation, because the only available disagreement is about the number.

### Task: two worlds, written out

Take the maintenance claim from §3's task.

> *Zones with more frequent valve maintenance have fewer main breaks, so increasing maintenance frequency will reduce breaks.*

1. Describe **two states of the world** that produce the same maintenance-and-breaks records and imply different answers about what increasing maintenance would do.
2. Name **one assumption** that, if you were willing to make it, would rule out your second world.
3. Say whether that assumption could be checked against the utility's records, and if not, who would have to be asked.

Question 3 is the one that changes practice. The answer is almost always *an engineer who knows how the maintenance schedule was set*, and that person is rarely in the room when the analysis is done.

## 5. Three Conditions, and How the Anchor Fails Them

§4 said identification is relative to assumptions. This section names the assumptions.

There is a standard set of three, and they come with an unusual framing: they are the conditions under which an observational study can be treated as though it were a randomized experiment. The strategy behind them is stated plainly:

> "We analyze our data as if treatment had been randomly assigned conditional on measured covariates –though we often know this is at best an approximation." [@hernan2019whatif, p. 26]

The conditions, as the source gives them:

> 1. the values of treatment under comparison correspond to well-defined interventions that, in turn, correspond to the versions of treatment in the data
> 2. the conditional probability of receiving every value of treatment, though not decided by the investigators, depends only on measured covariates
> 3. the probability of receiving every value of treatment conditional on [the covariates] is greater than zero, i.e., positive
>
> [@hernan2019whatif, p. 26]

Their names, on the same page: condition 1 is **consistency**, condition 2 is **exchangeability**, condition 3 is **positivity**. Collectively they are "identifiability conditions or assumptions".

### Before the list becomes a checklist

It will be tempting to treat the three as boxes to tick, and the source heads that off:

> "We will see that these conditions are often heroic, which explains why causal inferences from observational studies are viewed with suspicion." [@hernan2019whatif, p. 26]

**Heroic** is their word, not this book's softening or sharpening of it.

And the thesis of the whole apparatus, from the same page:

> "Causal inference from observational data requires two elements: data and identifiability conditions." [@hernan2019whatif, p. 26]

**Two elements.** Not data plus a good method. Not data plus enough of it. Data plus assumptions that the data cannot supply.

### The utility's record

Here is what the utility has, and it is a genuinely good record by the standards of most organisations.

Fifteen pumped zones. A capital programme over twelve years upgraded the duty pump in six of them. Mean low-pressure complaints per heat event, before the programme and after:

| | Zones | Before | After |
|---|---:|---:|---:|
| Upgraded | **6** | **6.8** | **4.1** |
| Not upgraded | **9** | **2.9** | **2.6** |

Four numbers. Now watch how many answers they support.

**Compare the two groups after the programme.**

`4.1 − 2.6 = ` **+1.5**

Upgraded zones have *more* complaints than un-upgraded ones. Read straight, this says pump upgrades make things worse.

**Compare the upgraded zones before and after.**

`4.1 − 6.8 = ` **−2.7**

A fall of nearly three complaints per event. Read straight, this says upgrades help a great deal.

**Compare the changes.**

`(4.1 − 6.8) − (2.6 − 2.9) = −2.7 − (−0.3) = ` **−2.4**

The upgraded zones fell by 2.7; the others fell by 0.3; the difference is 2.4. Read straight, this says upgrades help, and controls for whatever made everything fall.

**Three comparisons, three answers, and the first has the opposite sign from the other two.** All three are arithmetically correct. Every one of them appears in real briefing notes, usually without the other two.

Nothing in the table tells you which to believe, because what separates them is not in the table.

### Exchangeability, and why the first comparison is backwards

**Exchangeability** is the assumption that the treated and untreated are interchangeable in the relevant respect — that, as the source puts it for the randomized case, "the treated, had they remained untreated, would have experienced the same average outcome as the untreated did, and vice versa" [@hernan2019whatif, p. 27].

Now the fact the table does not contain.

**The six zones chosen for upgrade were the six worst-complaining zones at the time the programme was funded.**

Allocation was made on past values of the outcome itself. Of course the upgraded zones still have more complaints afterwards: they started at 6.8 against 2.9, and a fall of 2.7 does not close a gap of 3.9.

The cross-sectional comparison is not merely biased. It is **guaranteed to point the wrong way** whenever a programme is targeted at the worst cases and does not completely fix them.

**And targeting the worst cases is not a mistake.** It is how most capital programmes, maintenance schedules, inspection regimes, and interventions of every kind allocate scarce resources, and it is usually the right thing to do operationally. The utility did nothing wrong. Its allocation rule simply happens to destroy the assumption that a naive comparison needs — which is why the assumption has to be checked rather than assumed, and why *how were these cases selected* is the first question to ask of any before-and-after table.

### Why the second comparison fails too

The before-and-after within upgraded zones has a different problem: something else changed over the same twelve years.

A separate mains renewal programme ran across the network. Its trace is visible in the table — the nine un-upgraded zones fell by **0.3** without receiving any pump work at all.

So part of the 2.7 fall in upgraded zones is not the pumps. Some of it is whatever moved the other nine.

### And why the third is not safe either

This is where most analyses stop, because the third comparison looks like it has fixed the problem. It subtracted off the general trend. What is left over should be the pump effect.

**It requires an assumption, and the assumption is doubtful here for a specific reason.**

The difference-in-differences comparison assumes the upgraded zones would have moved like the un-upgraded ones — falling by about 0.3 — had nothing been done to them. That is a real, nameable assumption, which already makes it better than the other two.

But the six zones were selected for being extreme. Zones observed at their worst tend to be less bad next time regardless of what anybody does, partly because part of what made them worst was transient. Some unknown share of the 2.7 fall is that, and **nothing in the four numbers separates it from the pump effect.**

**So all three comparisons rest on assumptions, and none of the assumptions is in the table.** The third is the best of them because its assumption can at least be named, argued about, and sometimes checked against other periods. That is a real advantage and it is not the same as being right.

A chapter that walked you to the third comparison and stopped would have taught you to trust a number for the wrong reason — which is precisely the habit Chapter 5 exists to prevent.

### Positivity, and the fact that settles it

The third condition is the one that finishes the utility's question, and it is the one most likely to be missed.

> "we must ensure that there is a probability greater than zero–a positive probability–of being assigned to each of the treatment levels. This is the positivity condition." [@hernan2019whatif, p. 30]

For an observational record, the question is whether every kind of unit you want to reason about actually appears under both treatment values.

Now the fact.

**Hillcrest's feeder main is 68 years old. None of the six upgraded zones has a main older than 40.**

Two of the nine un-upgraded zones have mains over 60, Hillcrest among them. So in this record, for zones like Hillcrest, the probability of having received a pump upgrade is **zero**.

Not small. Not imprecisely estimated. Zero.

There is no zone in twelve years of records that both resembles Hillcrest in the respect that matters and received the treatment. The comparison the utility wants to make has no cases on one side.

And the intuition for why this is fatal is straightforward: with no upgraded old-main zones, the data contain nothing with which to work out what would have happened to an old-main zone had it been upgraded [@hernan2019whatif, p. 31].

**None of the three comparisons shows any sign of this.** The numbers `+1.5`, `−2.7`, and `−2.4` are all computable, all stable, and all silent about the fact that they were computed over zones unlike the one the question is about.

### Pause: would fifty more zones help?

Before reading on, write two or three sentences.

> Suppose the utility merged with a neighbouring one and acquired fifty more pumped zones with fifteen years of comparable records. **Does the positivity problem go away?**

---

**No — and the reason is the whole point of the section.**

The failure is not that there are too few old-main zones. It is that old-main zones **do not get pump upgrades**, and they do not get them for a reason: an old main is the thing you replace instead. Fifty more zones drawn from the same world contain fifty more instances of the same policy.

More data of a kind that never contained the comparison you need does not eventually contain it.

You met this in Chapter 4, in a different vocabulary. Roads with no residential frontage generated no rows in the pothole register, and no amount of the register revealed the gap, because the missing cases produce nothing to notice. Positivity failure is the same shape: **a hole with no edges.**

What *would* help is different in kind. Upgrade one old-main zone deliberately and watch. Find another utility that did. Or work from physics rather than records — which is what Chapter 2's mechanism reasoning was for.

### Consistency, and a word that means something else

The first condition is the one that sounds trivial and is not.

**Consistency**, in this sense, means the outcome you observed under the treatment actually received is the outcome that would have obtained under that treatment. The source anticipates the reader's reaction:

> "The apparent simplicity of the consistency condition is deceptive." [@hernan2019whatif, p. 31]

The difficulty is upstream of the arithmetic. To say what would have happened under a treatment, the treatment has to be specified precisely enough to have **one** effect rather than several. Where several different actions all count as the treatment and could differ in their effects, the causal effect "will be ill-defined" [@hernan2019whatif, p. 33].

**A warning about the word.** `consistency` in Chapter 8 will mean something entirely different — a property of an estimator, that it converges on the quantity being estimated as the sample grows. The two have nothing to do with each other beyond sharing six syllables.

This book will use both, as it uses both senses of `calibration` and both traditions' `validation`. Whenever this book writes `consistency` without qualification in a causal context, it means the condition above; in an estimation context, the estimator property. **Say which you mean, in your own writing, every time.**

### The pump, unspecified

Now apply it.

The utility's register records six zones as having had a *pump upgrade*. Here is what that covers.

| Option | What was done |
|---|---|
| 1 | Like-for-like replacement at the existing **1.1 ML/day** |
| 2 | A higher-capacity duty pump at **1.5 ML/day** |
| 3 | A second pump in parallel |
| 4 | A variable-speed drive on the existing pump |

Four different actions. Different costs, different installation disruption, different failure modes.

**And plausibly different effects, including in sign.**

Under Mechanism B, friction loss along the feeder main grows sharply with flow. Options 2 and 3 both push more water through the main. In a zone whose main is 68 years old and undersized, more flow means more loss, which means **lower** pressure at the top of the zone — the outcome the upgrade was meant to fix.

So `P(complaints fall | do(upgrade the pump))` is not one quantity. It is at least four, and two of them may have opposite signs from the other two.

The register records all four as the same thing.

**This is not a pedantic objection.** It means the six upgraded zones are not six instances of one treatment. They are six instances of some mixture of four treatments, in unknown proportions, and the `−2.4` computed earlier is an average over that mixture — an average whose composition nobody recorded and which will not match whatever Hillcrest ends up receiving.

### Task: three comparisons, three assumptions

Using the four numbers in the table:

1. Compute all three comparisons yourself. Check them against the figures above.
2. For each, write the assumption in one sentence, in the form *this comparison is the answer if ___*.
3. Rank the three by how likely their assumption is to hold here, and say why.
4. Then state, in one sentence, what the positivity fact does to all three at once.

Question 4 is the one worth having. It does not favour one comparison over another — it applies to all of them equally, and it is the reason the ranking in question 3 matters less than it appears to.

## 6. Designs as Strategies for Identification

§5 was about assumptions you have to make. This section is about arranging matters so you do not have to make them.

That is what a design is for, and the source says so in a single sentence:

> "Importantly, in ideal randomized experiments the identifiability conditions hold by design." [@hernan2019whatif, p. 26]

**Hold by design.** Not assumed, not approximated — made true by how the study was set up. That is the whole value proposition of an experiment, and it is why experiments occupy the position they do.

Which makes it worth being precise about what randomization actually delivers, because the usual account is wrong.

### What randomization buys

A critical assessment states it, and the sentence is worth reading twice:

> "This was Fisher's innovation: not that randomization balanced other causes between treatments and controls but that, conditional on our caveat above, randomization provides the basis for calculating the size of the error." [@deaton2016rct, p. 10]

And the summary on the same page:

> "Given the absence of treatment-related post-randomization changes in other causes, randomization yields an unbiased estimate of the ATE in the trial sample as well as a sound method for measuring error of estimation in that sample; therein lies its virtue, not that it yields precise estimates through balance." [@deaton2016rct, p. 10]

Two things, then. An unbiased estimate in the trial sample, and a way to compute how far off it might be.

**Not balance.** The same paper, on the previous page:

> "We do not know the size of this error term, and there is nothing in randomization that limits its size; by chance the randomization in our single trial can over-represent an important excluded cause(s)" [@deaton2016rct, p. 9]

The distinction named:

> "There is often confusion between perfect control, on the one hand (as in a laboratory experiment or perfect matching with no unobservable causes), and control in expectation on the other, which is what randomization contributes." [@deaton2016rct, p. 10]

**Control in expectation.** Across the hypothetical many trials you did not run, the imbalances average out. In the one trial you did run, they do not.

**A note on this source.** It is a working paper whose own cover states that NBER working papers have not been peer-reviewed. The paper is a well-known critique and parts of it are argued against by serious people. Its strongest claim — that randomization "is generally inferior to good control" when you know enough to control well [@deaton2016rct, p. 10] — is **the authors' position in a live debate**, reported here as theirs rather than presented as settled. The narrower points about what randomization does and does not deliver are not controversial; they are standard, and the paper's contribution is documenting how routinely they are misstated.

### A documented overstatement

The paper does not attack a straw man. It quotes published sources, and this one comes from an impact-evaluation manual jointly issued by two development banks:

> "We can be confident that our estimated impact constitutes the true impact of the program, since we have eliminated all observed and unobserved factors that might otherwise plausibly explain the difference in outcomes."
>
> — quoted at [@deaton2016rct, p. 10]

The diagnosis:

> "This statement is false, because it confuses actual balance in any single trial with balance in expectation over many (hypothetical) trials." [@deaton2016rct, p. 11]

And then the detail that makes it useful:

> "Note that the statement contains no reference to sample size; we get the truth by virtue of balance, not from a large number of observations." [@deaton2016rct, p. 11]

**Read that last one against Chapter 6.**

Chapter 6 established that calibration is a property of a forecaster **across a record** — that a single forecast cannot be scored, because one outcome is consistent with any probability between 0 and 1, and that the forty-briefing table showed a pattern no individual row contained.

Balance is a property of a randomization procedure **across hypothetical replications.** Reading it off one trial is the same category error, in a different field, with the same consequence: a claim that sounds like it is about the thing in front of you and is actually about an ensemble you never observed.

Two chapters, two settings, one mistake. Once you have the shape, you will find it in a third place within a month.

### A trial answers the trial's question

Suppose the trial is real, well conducted, and correctly interpreted. It still answers a question defined by its own five attributes: **its** treatment, **its** population, **its** variable, **its** follow-up, **its** summary.

If your question differs on any of them, the trial's answer is evidence about something adjacent to what you asked. Extending a result beyond the trial sample — including to the population the sample was drawn from — "requires further argument" [@deaton2016rct, p. 8].

**That further argument is Chapter 9's subject**, and this chapter goes no further into it than naming that it is required.

The §2 discipline is what makes the mismatch visible. Write both target quantities out with their five attributes, put them side by side, and the differences are on the page instead of in somebody's head.

### And observational evidence is not second-rate

A reader who has come this far could reasonably conclude that only experiments establish anything. The source that supplied the three conditions rejects that, in its own chapter opening:

> "Many scientific studies are not experiments. Much human knowledge is derived from observational studies. Think of evolution, tectonic plates, global warming, or astrophysics. Think of how humans learned that hot coffee may cause burns." [@hernan2019whatif, p. 25]

Not one of those was established by randomizing anything. Continental drift was not tested by assigning continents to conditions.

What distinguishes the strong observational cases is not that they avoided assumptions. It is that their assumptions were stated, were plausible on grounds independent of the data, and had consequences that could be checked in other ways.

Take the coffee. Nobody randomized anybody into hot drinks. The causal claim is secure because the mechanism is understood from physics that was established elsewhere, because the effect is enormous relative to anything else that varies, because the timing is immediate and specific, and because the claim implies things that can be checked independently — that the burn's severity tracks the temperature, that it appears where the liquid landed, that a cold drink does nothing.

**Those four features are what an observational case needs**, and none of them is a statistical procedure. A mechanism from outside the data. An effect large relative to the plausible confounding. A structure in time or space that a rival explanation would have to reproduce. And consequences checkable somewhere else.

Set the utility's record against them and it fails all four. The mechanism is exactly what is in dispute. The effect is small relative to the difference between zones. The timing coincides with another programme. And nothing about the claim implies anything checkable elsewhere.

**That is a more informative verdict than *observational data cannot settle it*.** It says which of four things is missing, and two of them — a mechanism argument, and an independently checkable consequence — are available to the utility without collecting anything.

The balancing warning, from the same source, is the other half:

> "The best explanation for an association between treatment and outcome in an observational study is not necessarily a causal effect of the treatment on the outcome." [@hernan2019whatif, p. 26]

**Both sentences at once.** Observational evidence can establish causes, and an observed association is not one.

### The most useful question in the chapter

Here is the device that carries the most weight per word.

> "Therefore 'what randomized experiment are you trying to emulate?' is a key question for causal inference from observational data." [@hernan2019whatif, p. 37]

Every observational analysis is standing in for some experiment. Usually nobody has said which. Writing the protocol out — eligibility, intervention, outcome, follow-up, contrast, analysis — forces the analysis to declare itself, and the source records the payoff: an explicit emulation "prevents investigators from conducting an oversimplified analysis" [@hernan2019whatif, p. 37].

### The utility's target trial

Write it out.

> **Eligibility.** All fifteen pumped zones.
> **Intervention.** Duty-pump upgrade, versus no pump work.
> **Outcome.** Mean low-pressure complaints per heat event.
> **Follow-up.** Three years, or the next six heat events, whichever comes later.
> **Contrast.** Difference in means between arms.
> **Assignment.** At random.

Now read it back, and three things are visible at once.

**There are fifteen zones.** Seven and eight. A trial that size could not distinguish an effect of the size the utility cares about from nothing at all.

**You cannot withhold an upgrade from a zone that needs one.** The zones with the worst pressure are the ones the utility has an obligation to. Randomizing means deliberately not upgrading some of them, which is not a thing a water utility can do.

**Heat events do not arrive on a schedule.** Follow-up cannot be fixed in advance, and the zones would not experience the same weather.

**The trial is infeasible. And writing it was still worth doing.**

Because now the assumption is visible. The observational analysis is being asked to stand in for random assignment, and the protocol says exactly what that means: that whether a zone got an upgrade was unrelated to how bad it was going to be. §5 established that allocation was made *on precisely that basis*.

**The infeasible protocol names the assumption the feasible analysis is carrying.** That is the technique, and it costs ten minutes.

### Controlling for everything is not the answer

The most common response to a confounding worry is to adjust for more variables. It seems obviously safe: more control, less bias.

It is not safe.

> "the prevailing practice of conditioning on as many pre-treatment measurements as possible should be approached with great caution; some covariates (e.g., Z3 in Fig. 3) may actually increase bias if included in the analysis" [@pearl2009causal, p. 117]

**Some covariates increase bias when you include them.** The same page reports that this bias-raising potential has been confirmed by other authors using simulation and parametric analysis.

Which covariates? That question has a real answer, and it is graphical. There is a criterion for selecting sets of factors that are sufficient for adjustment, and the intuition behind it is stateable in prose:

> "The back-door paths in the diagram carry spurious associations from X to Y, while the paths directed along the arrows from X to Y carry causative associations." [@pearl2009causal, p. 114]

Adjusting for the right variables closes the spurious routes. Adjusting for the wrong ones can open routes that were closed.

**This book does not teach the criterion.** Stating it properly requires vocabulary for paths, blocking, and collision nodes that would take a chapter of its own, and it belongs to the depth curriculum. The source itself records that the underlying problem "has baffled epidemiologists and social scientists for decades" [@pearl2009causal, p. 114], which is fair warning that it is not a five-minute topic.

What you should take is narrower and immediately usable: **the list of things to adjust for is a causal claim, not a data-processing choice**, and *we controlled for everything we had* describes an assumption nobody has stated rather than an absence of assumptions.

### And this is where the chapter stops

One more boundary, in the source's own terms.

Deriving what quantity you would need to compute "is merely a first step toward computing quantitative estimates of those effects from finite samples" [@pearl2009causal, p. 117]. The same page separates the two firmly: methods for estimating well "cannot be expected to reduce bias" if the identification step was not satisfied.

**Identification first, estimation second, and a good estimator cannot repair a bad identification.** That is the boundary between this chapter and the next, stated by the source rather than asserted by the book.

### Task: write the target trial

For the maintenance claim you have been working since §3 — *increasing valve maintenance frequency will reduce main breaks*:

1. Write the target trial protocol. All six components.
2. Say why it cannot be run. Give the specific reasons, not "it would be difficult".
3. **Name the assumption** the observational analysis is being asked to carry in its place.
4. Say who in the organisation would know whether that assumption is plausible.

## 7. What More Data Cannot Do

One sentence in this chapter's principal source does more work than any other, and this short section is about it.

### The asymmetry

> "Associational assumptions, even untested, are testable in principle, given sufficiently large sample and sufficiently fine measurements. Causal assumptions, in contrast, cannot be verified even in principle, unless one resorts to experimental control." [@pearl2009causal, p. 101]

**Cannot be verified even in principle.** Not *hard to verify*, not *usually unverified*. There is no observational dataset, of any size, that checks them.

And the consequence for effort:

> "sensitivity to prior causal assumptions, say that treatment does not change gender, remains substantial regardless of sample size." [@pearl2009causal, p. 101]

The contrast in that passage is with statistical assumptions, whose influence shrinks as data accumulates. Causal assumptions do not shrink. Their influence on your answer is the same with twelve years of records as with twelve.

### A shape you have now met four times

| Chapter | More of this improves | And does nothing for |
|---|---|---|
| 3 | measurements | precision — but not **trueness** |
| 4 | records | sampling variability — but not the **data-quality term** |
| 6 | simulation runs | Monte Carlo error — but not **model error** |
| 7 | sample size | associational uncertainty — but not **sensitivity to causal assumptions** |

Chapter 6 gave you the first three and drew the rule from them. It is worth saying what has changed.

**The first three were this book's observation.** Three fields, three vocabularies, and the book noticed that the structure repeated. A reader would have been right to wonder whether the pattern was in the world or in the author's fondness for it.

**The fourth arrives cited.** The passage above is not the book noticing a parallel; it is a source stating the same structure for its own field, in its own words, without any prompting from this book's argument.

The rule, restated:

> **When told that more of something will fix a problem, ask which term it enters.**

There is a reason the pattern keeps appearing, and it is not that the book went looking.

In each case there are two sources of wrongness with different characters. One comes from having a finite amount of something — readings, records, runs, observations — and averaging over more of it makes that source smaller, because that is what averaging does. The other comes from a commitment made before any of the collecting started: where the instrument was installed, which records the process generates, what the model assumes, what the causal structure is.

**Effort scales against the first and slides straight past the second**, and no field has found a way around it, which is why four disciplines with no shared vocabulary all ended up saying the same thing in their own words.

What varies is only how well hidden the second term is. Chapter 3's was visible if you compared against a reference. Chapter 4's was visible if you asked how the records came to exist. Chapter 6's was visible if you changed the model structure and reran. Chapter 7's is the best hidden of the four, and §4's verdict format exists to drag it onto the page.

### On the anchor

Suppose the utility waits and its record doubles. Twenty-four years, thirty zones, complaints logged to the hour.

**What improves.** Every number in §5's table gets steadier. The `−2.4` stops wobbling between recalculations. Seasonal patterns separate from trends. Rare failure modes appear often enough to see.

**What does not move at all.**

The six upgraded zones were still the six worst. Doubling the record doubles the instances of an allocation rule; it does not change what the rule was.

Old-main zones still do not receive pump upgrades, because an old main is the thing you replace instead. The hole has no edges in a longer record either.

*Pump upgrade* still covers four different actions, and if the register never distinguished them, more of the register never will.

And the mains renewal programme still ran at the same time, so the comparison still cannot separate the two.

**Every one of those is an identification problem, and identification does not improve with n.**

Which is why §4 insisted that identification is settled before data collection. It is a whiteboard question, and answering it afterwards means finding out what your budget bought after you have spent it.

There is a specific way this goes wrong that is worth naming, because it looks like diligence.

The larger record produces **tighter** numbers. The `−2.4` stops moving between recalculations; if the analysis reports an interval, the interval narrows. Every visible sign of quality improves, and the analysis becomes more confident about a quantity that is no closer to being the one the board asked about.

**Precision and identification move independently, and only one of them is visible in the output.** A stable, tightly bounded answer to an unidentified question looks exactly like a stable, tightly bounded answer to an identified one. Nothing in the number carries the difference — which is why the verdict format in §4 puts the assumption on the page rather than in a footnote.

This is the fourth row's particular sting. The three earlier instances left a visible residue: a biased instrument still reads oddly against a reference, a defective dataset still has a documented provenance, a model error still shows up when you change the structure. **An unstated causal assumption leaves no trace in the output at all.**

### So what does help

If more of the same record does not, the honest question is what does. Four things, in rough order of cost.

**Ask how the treated cases were chosen.** This is one question to one person and it resolves more analyses than any amount of adjustment. It is not a data request; whoever ran the capital programme knows the answer and has never been asked.

**Look for the missing cell.** Not more rows — a *kind* of row that does not exist. An old-main zone that was upgraded. If one exists anywhere, in a predecessor utility or a neighbouring one, it is worth more than another decade of the zones you already have.

**Argue from mechanism instead of records.** Chapter 2's hydraulics can say what a higher-capacity pump does to friction loss along a 68-year-old main. That is an argument from outside the data, which is exactly what §3's golden rule says a causal conclusion requires — and it is available today.

**Arrange the comparison rather than looking for it.** Upgrade one old-main zone deliberately, chosen for reasons unrelated to how bad it is, and watch. One deliberately arranged case can carry more weight than fifteen accumulated ones, because the arrangement is the identifying assumption made true rather than assumed.

**Every one of those is cheaper than another twelve years of records**, and none of them is the thing organisations do when an analysis comes back inconclusive.

### Why this chapter is uncomfortable, honestly

The source names the two things that make this material hard to accept, and the naming is more useful than reassurance:

> "The preceding two requirements: (1) to commence causal analysis with untested, theoretically or judgmentally based assumptions, and (2) to extend the syntax of probability calculus, constitute the two main obstacles to the acceptance of causal analysis among statisticians and among professionals with traditional training in statistics." [@pearl2009causal, p. 101]

**Both apply to you, and one of them applies to this book.**

The first asks a reader trained to be careful about evidence to begin by writing down something the evidence cannot check. That feels like the opposite of rigour and it is not: the assumption is present in every causal analysis ever conducted, and the only choice is whether it is written where somebody can argue with it.

The second is why a book that refused notation for five chapters has now taken two exceptions in two chapters. The distinction between *given that the pump was replaced* and *if we replace the pump* has to be visible on the page. It could not be made visible in prose, which is exactly what the source means by probability calculus being insufficient.

### Task: diagnose five defects

Each statement below contains one defect. Write the defect, what it stops you concluding, and a repair.

1. *"We controlled for every variable in the dataset, so the estimate is unbiased."*
2. *"It was a randomized trial, so the two groups were balanced."*
3. *"We have twelve years of records on fifteen zones, so we can settle this."*
4. *"The model predicts pressure drops with 94% accuracy, so we know what causes them."*
5. *"The effect isn't identified, so there's nothing we can say."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

## 8. Cold-Start Practice and Retrieval

### Return to your six-minute answer

Find what you wrote at the start of §1, about whether the 91% supports the utility's sentence.

Read it against what you can now produce. Do not score it.

- Did you notice that the sentence names **no comparison**?
- Did you distinguish *which mechanism operates* from *what happens if we act*?
- Did you say what would have to be true, or only that more evidence was needed?

Three patterns are common in the opening attempt.

Some readers write that the 91% is fine and the sentence follows — which is the slide the chapter exists to interrupt, and noticing it in your own handwriting is worth more than being told about it.

Some write that the evidence is too weak, and ask for more data. That instinct is honourable and §7 is aimed at it: the problem is not quantity, and more of the same record would not have helped.

Some write that the sentence is vague. That is the strongest of the three opening answers and it is still only §2 — the next question is *vague about what*, and the five attributes are the answer.

### Independent transfer

Now work an unfamiliar situation, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below. Open only that one.

- [Form A — A manufacturer's machine-guarding retrofit](transfer-form-a.md)
- [Form B — A city's bus lane and journey times](transfer-form-b.md)

Allow about **50 minutes**.
Every fact you need is supplied. Do not look anything up.

Do not open the other form. You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the procedure from memory

Before looking back, write down how you would examine a causal claim.

Aim for the sequence, not the wording.

For reference, after you have tried:

1. What exactly is the target quantity? Treatment, **compared with what**, population, variable, window, summary.
2. Is the intervention specified precisely enough to have one effect?
3. Which of the three questions is this — association, intervention, or counterfactual?
4. What randomized experiment would answer it? Write the protocol.
5. Why can that experiment not be run?
6. So what assumption is the available analysis carrying instead?
7. **How were the treated cases selected?**
8. Are there cases like the one I care about on **both** sides?
9. Could two different worlds produce this same record and imply different answers?
10. If it is not identified: which assumption would change that, and who would know?

Step 1 is the one that is skipped, and skipping it is how two different questions get one answer.

Step 7 is the one that finds the problem fastest. In practice it is a single question to a single person, and it resolves more analyses than any amount of adjustment.

Step 8 is the one nobody asks, because a hole with no edges produces nothing to notice.

### If the transfer went badly

- **You critiqued the data rather than the question.** Sample size, missing values, and measurement noise are Chapters 3, 4, and 8. This chapter is about whether the question could be answered by clean, complete data.
- **You said "correlation is not causation" and stopped.** True and useless. The work is naming *which* condition fails and *why it is structural*.
- **You accepted the difference-in-differences.** Check what it assumes about how the treated cases would have moved, then check how they were chosen.
- **You missed a positivity failure.** Ask which kinds of unit never appear on one side. They will not be flagged; there is nothing there to flag.
- **You concluded that nothing can be known.** Reread §4's verdict format. A useful answer names the assumption and says what would change it.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Do not reread this chapter immediately beforehand, and do not look at the form you have not done.

### What this chapter did not give you

**How to estimate anything.** Every number here was supplied or was arithmetic on supplied numbers. Turning an identified quantity into an estimate, with a statement of how far off it might be, is Chapter 8.

**Which covariates to adjust for.** §6 established that this is a causal question with a real answer and that the answer is graphical. The criterion is not taught here.

**Instrumental variables, mediation, and the rest of the apparatus.** When the three conditions fail, other approaches exist with different conditions of their own. They are named nowhere in this chapter except this sentence, deliberately.

**How to extend a result beyond the population it came from.** Chapter 9.

**Whether to act.** Even a fully identified effect does not tell the utility what to do, because that needs consequences and an attitude to risk. Chapter 11.

**Any verdict on the two frameworks.** They were named, their definitions were shown to agree, and the argument between them was left alone.

### What Chapter 8 asks next

You can now say what quantity a causal claim is about, and whether the evidence in front of you could establish it.

Suppose the answer is yes. Suppose the identification step is satisfied — by a design, or by an assumption you are willing to defend and have written down.

You still do not have a number. You have a target quantity that *could* be computed from the right data, and a finite, noisy, incomplete dataset that is not the distribution the identification argument was about.

That gap is the whole of Chapter 8, and the order is not this book's convention. Deriving what to compute "is merely a first step toward computing quantitative estimates of those effects from finite samples" [@pearl2009causal, p. 117].

Chapter 8 takes the second step: how to turn an identified quantity into an estimate, how to say how far off it might be, and how to check whether the model that produced it is any good.
