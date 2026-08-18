# Chapter 9 — Diagnosis Feedback

Open this file only **after** you have written your diagnosis of all five statements in §6.

Your wording will differ; what matters is whether you found the same fault.

## 1. "We pooled all five studies, giving us 1,461 observations."

**Defect.** Sample sizes are being added across sources that measure different quantities.

**What it costs.** The 1,461 is arithmetic on numbers that do not describe one thing. Fifteen zones with an unallocated treatment mixture, forty flat-ground zones, fourteen hundred zones of an undefined variable, and six rigs with no feeder main are not 1,461 observations of anything.

And the sentence does specific damage, because a large *n* is the strongest reassurance signal in analytic writing. A reader who sees 1,461 stops asking what the sources are and starts asking what the confidence interval is.

**Repair.** Report each source with its own quantity and size, and say which are about the question. If a combined figure is wanted, produce several rules and show the spread — the number that matters is how far apart they land, not how many rows went in.

**Note.** This is the §2 failure with arithmetic attached. Whether the sources are about one quantity is prior to how many of them there are, and the pooled *n* buries the question under a big number.

## 2. "Four of the five agree, so the finding is robust."

**Defect.** Agreement is being counted without checking whether the sources could have disagreed.

**What it costs.** Two of the utility's five share a measurement convention: the neighbouring utility is a member of the benchmarking scheme, so its forty zones are inside the fourteen hundred. Two of the five panel members wrote that scheme's complaint definition. The manufacturer's protocol was written against the same definition.

So four apparent confirmations may be one convention reported four times, **and the five numbers look identical either way.**

The error runs in the reassuring direction, which is what makes it dangerous. Dependence makes sources agree more than independent ones would, so it raises confidence exactly where confidence is least warranted.

**Repair.** Before counting agreement, ask what the sources share: data, people, definitions, software, training, funding. Three emails answered all three questions for the utility, and nobody sent them.

**Note.** This book found no source for the claim in this passage, and says so in §3. It follows from what dependence means, and it is the weakest-supported material in Part II — which is stated rather than hidden.

## 3. "It has been replicated three times, so it will hold here."

**Defect.** Replication is being treated as establishing transport.

**What it costs.** "Without further understanding and analysis, even successful replication tells us little either for or against simple generalization or to support for the conclusion that the next will work in the same way" [@deaton2016rct, p. 27].

Three replications in settings unlike yours are three confirmations that the effect is real **in that kind of setting**. Whether it holds in yours depends on whether your setting has the conditions the effect needs, and no number of repetitions elsewhere speaks to that.

Russell's chicken had the longest replication record in the barn.

**Repair.** Ask what the three settings had in common, and whether your setting has it. If the three differ from one another in a respect your setting shares, that is worth much more than the count.

**Note.** The count is doing rhetorical work here that it cannot support. *Three times* sounds like accumulating certainty; what would actually accumulate is understanding of which conditions the effect requires, and that comes from replications that **differ** rather than from replications that match.

## 4. "The trial was internally valid, so the effect is real and applies."

**Defect.** Two claims have been welded together by the word *and*.

**What it costs.** The first half may be entirely correct. The second does not follow: "establishing causality does nothing in and of itself to guarantee generalizability" [@deaton2016rct, p. 28].

An internally valid trial establishes an effect **in the population it studied, under the conditions it ran in**. Whether that effect operates elsewhere depends on support factors — the conditions a cause needs in order to work — and those "are just the kind of factors that are likely to be differently distributed in different populations" [@deaton2016rct, p. 29].

The specific cost is that the sentence is usually said by the most careful person in the room, having done the hardest part properly, and the room defers to them.

**Repair.** Separate the claims. *The effect is established for those units under those conditions.* Then, separately: *whether it operates here depends on ___, and here is whether we have it.*

**Note.** Chapter 7's work is not wasted by this. An unidentified effect cannot be transported either — there is nothing established to carry. Identification is a prerequisite for transport, not a substitute for it, and it is the second step that gets skipped because the first was so much work.

## 5. "There's no evidence it works differently here, so we'll assume it transfers."

**Defect.** Transport is being made the default, and the burden of proof reversed.

**What it costs.** More than the other four, because it is the sentence that gets an organisation to spend money.

Absence of evidence that a setting differs is not evidence that it does not — which is Chapter 5's point about checks that could not have failed, and Chapter 8's about non-significance. Nobody looked for the difference, so of course there is no evidence of one.

And in the utility's case the evidence was **available and unexamined**: terrain is on a contour map, and feeder-main age is in the asset register. Both facts were held by the utility while the five sources were being assembled, and neither was used to select them.

**Repair.** Invert the question. Not *is there evidence this setting is different*, but *what does this effect need in order to operate, and does this setting have it?* The second is answerable; the first invites a shrug.

**Note.** The default matters more than any individual judgment, because it decides what happens when nobody has time to check — which is most of the time. An organisation whose default is *assume it transfers* will be wrong in exactly the cases where the target setting is unusual, which are exactly the cases somebody escalated because the target setting is unusual.
