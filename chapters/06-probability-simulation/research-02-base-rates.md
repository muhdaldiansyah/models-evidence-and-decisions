# Research 02 — Base Rates, and What People Do with Evidence

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision.

Cluster R02 of `research-plan.md` §5. Research conducted 2026-08-18.

Source: `tversky1974judgment` (primary, pp. 1124–1125 read).

## 1. Q1–Q2 — What is documented, and whether neglect is universal

### The basic finding

`tversky1974judgment` p. 1124 identifies representativeness as a heuristic by which "probabilities are evaluated by the degree to which A is representative of B, that is, by the degree to which A resembles B."

And the consequence: "One of the factors that have no effect on representativeness but should have a major effect on probability is the prior probability, or base-rate frequency, of the outcomes."

The experiment: subjects assessed whether a described individual was an engineer or a lawyer, drawn from a group described as either 70 engineers and 30 lawyers, or 30 engineers and 70 lawyers. "In a sharp violation of Bayes' rule, the subjects in the two conditions produced essentially the same probability judgments" (p. 1124).

### The finding that actually matters

Base-rate neglect is **not** universal, and the qualification is more useful than the headline.

`tversky1974judgment` p. 1125: "The subjects used prior probabilities correctly when they had no other information."

And then, with a description supplied that "was intended to convey no information relevant to the question", subjects answered .5 regardless of whether the stated proportion was .7 or .3.

The authors state the conclusion directly, and this is the sentence Chapter 6 should quote:

> "Evidently, people respond differently when given no evidence and when given worthless evidence. When no specific evidence is given, prior probabilities are properly utilized; when worthless evidence is given, prior probabilities are ignored." [p. 1125]

### Why this framing is better for the book

The generic claim — *people neglect base rates* — is folk-wisdom shaped and easy to nod at without changing anything.

The precise claim is actionable and unsettling. The trigger for abandoning the base rate is **being handed something that looks like information**. Which means the danger is not ignorance; it is a plausible-sounding briefing, a vivid anecdote, a detailed case description.

For this book's readers, that lands close to home. A representation, a measurement, a dataset, and a criticism are all things that look like information. Part I spent five chapters showing that each can be uninformative about the question at hand while appearing substantial.

## 2. Q3 — Evidence strength versus sample size

Two further results on the same page, both usable.

**Insensitivity to sample size.** The two-hospitals problem — a large hospital and a small one, which recorded more days on which over 60% of babies were boys. Of the respondents, "21" chose the larger, "21" the smaller, and "53" said about the same (p. 1125). The correct answer follows because "a large sample is less likely to stray from 50 percent."

**Conservatism.** The urn problem, where "the correct posterior odds are 8 to 1 for the 4:1 sample and 16 to 1 for the 12:8 sample, assuming equal prior probabilities. However, most people feel that the first sample provides much stronger evidence" (p. 1125). The authors note: "The underestimation of the impact of evidence has been observed repeatedly in problems of this type. It has been labeled 'conservatism.'"

### The tension worth showing the reader

Put those two next to base-rate neglect and something odd appears.

People **abandon** priors when handed worthless evidence, and simultaneously **underweight** genuinely informative evidence.

Both directions, in the same subjects, on adjacent pages. Which means the practical lesson is not "trust your priors more" or "update harder" — it is that intuition does not track evidential weight reliably in either direction, and that arithmetic is worth doing precisely because the intuition is not merely noisy but systematically wrong in ways that depend on presentation.

That is a strong argument for the odds form recommended in R01: it makes evidential weight a number rather than a feeling.

## 3. Q4 — What the chapter may claim about correction

**Very little, and the limits must be stated.**

The inspected pages document tendencies. Nothing in them says the tendencies can be trained away, and a substantial later literature disputes how far they can be. **That literature was not read** and must not be characterized.

What the chapter may say: doing the arithmetic explicitly is a way of not relying on the intuition. That is a claim about a procedure, not about debiasing.

`tversky1974judgment` p. 1124 also supplies a caution the chapter must respect: the heuristics "are quite useful, but sometimes they lead to severe and systematic errors." A chapter that presented intuition as merely broken would misreport the source and would be poor teaching besides — the reader uses these heuristics constantly and correctly.

## 4. Cautions — claims the manuscript must NOT make

1. Do not state base-rate neglect as universal. p. 1125 conditions it explicitly.
2. Do not present the heuristics as defects. p. 1124 calls them useful.
3. Do not claim these tendencies can be trained away. Not supported, and disputed in literature not read.
4. Do not cite beyond p. 1125. Availability and anchoring are on uninspected pages.
5. Do not reverse the author order. The article prints Tversky then Kahneman.
6. Do not use this source for anything about decisions. It concerns judgments of probability; Chapter 11 owns decisions.
7. Do not present laboratory results with student subjects as directly establishing what professional analysts do. The extension is the book's own and should be made in the sentence that makes it.

## 5. Verdict on the stop condition

`research-plan.md` §5 requires the empirical claims about human judgment sourced and bounded.

**Met.** Three claims, all sourced to pp. 1124–1125: base rates are used when nothing else is offered and abandoned when worthless evidence is; sample size is under-weighted; evidential impact is under-estimated. Bounds are recorded in §4.

## 6. Unresolved author decisions

1. Is the "worthless evidence" sentence quoted, or paraphrased?
2. Is the two-directional tension in §2 shown to the reader, or is it too much for one chapter?
3. Is the base-rate material placed before the Bayes arithmetic, as motivation, or after, as a caution?
4. Does the chapter connect base-rate neglect to Part I — that a representation, a measurement, a dataset, and a criticism all look like information?

Decision 4 is attractive and slightly risky: it is the sharpest connection available, and it invites a reader to conclude that Part I was about nothing, which is the opposite of the point.
