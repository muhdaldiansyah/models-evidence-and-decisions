# Research 03 — Thresholds

Cluster R03 of `research-plan.md`. Closed.

Sources read directly: `asa2016pvalue`; `greenland2016misinterpretations` printed pp. 339–341, 343–344, 346–348.

The governed core competence requires this chapter to teach its material "without reducing evidence to threshold rituals". That phrase is in `README.md` and is not negotiable, so the chapter has to say what the ritual is and what is wrong with it.

## 1. The professional body's position

The American Statistical Association released a statement on 7 March 2016. The document obtained and read is the **ASA's own press release**, which prints the six principles in full.

> 1. P-values can indicate how incompatible the data are with a specified statistical model.
> 2. P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone.
> 3. Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold.
> 4. Proper inference requires full reporting and transparency.
> 5. A p-value, or statistical significance, does not measure the size of an effect or the importance of a result.
> 6. By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis.
>
> [@asa2016pvalue]

**Principle 4 is the one this chapter's spine needs.** *Proper inference requires full reporting and transparency* is the same claim as `greenland2016misinterpretations` p. 339's inclusion of analytic conduct among the model's assumptions, arriving from the professional body rather than from a methods paper.

The release also carries a quotation from the ASA's executive director:

> "The p-value was never intended to be a substitute for scientific reasoning… Well-reasoned statistical arguments contain much more than the value of a single number and whether that number exceeds an arbitrary threshold." [@asa2016pvalue]

And, from the ASA president at the time, an account of the mechanism:

> "Over time it appears the p-value has become a gatekeeper for whether work is publishable, at least in some fields… This apparent editorial bias leads to the 'file-drawer effect,' in which research with statistically significant outcomes are much more likely to get published, while other work that might well be just as important scientifically is never seen in print." [@asa2016pvalue]

**What the chapter may not do with this source.** The release states that the statement "has short paragraphs elaborating on each principle" — those paragraphs are in the American Statistician article, which was **not obtained**. The manuscript cites the six principles and the two quotations, and characterises nothing else.

## 2. What a P value is

The source's definition, given in prose that survives extraction:

> "The P value is then the probability that the chosen test statistic would have been at least as large as its observed value if every model assumption were correct, including the test hypothesis." [@greenland2016misinterpretations, p. 339]

And the framing the authors prefer over "significance level": a P value is "a statistical summary of the compatibility between the observed data and what we would predict or expect to see if we knew the entire statistical model … were correct" [@greenland2016misinterpretations, p. 339].

**Compatibility.** That word is the chapter's handle, and it is the source's own.

## 3. The dichotomy, named

> "Too often, however, the P value is degraded into a dichotomy in which results are declared 'statistically significant' if P falls on or below a cut-off (usually 0.05) and declared 'nonsignificant' otherwise." [@greenland2016misinterpretations, p. 339]

The same page notes that "the term 'significance level' invites confusion of the cut-off with the P value itself".

And the paper's closing judgment, which is as strong as methodological writing gets:

> "we join others in singling out the degradation of P values into ''significant'' and ''nonsignificant'' as an especially pernicious statistical practice" [@greenland2016misinterpretations, p. 348]

**"Especially pernicious statistical practice"** is the phrase to quote, and it is the last substantive sentence of the paper.

## 4. Four misinterpretations the chapter needs

The paper lists 25. The chapter uses four, chosen because each has a direct analogue in something the book has already taught.

**Misinterpretation 1** — the P value as the probability the hypothesis is true. The correction, quoted: "The P value assumes the test hypothesis is true—it is not a hypothesis probability and may be far from any reasonable probability for the test hypothesis" [@greenland2016misinterpretations, p. 340].

*Book analogue:* Chapter 6's inversion. `P(A | B)` and `P(B | A)` again, in a new setting, and the chapter should say so.

**The chance-alone version**, p. 340: "to claim that the null P value is the probability that chance alone produced the observed association is completely backwards: The P value is a probability computed assuming chance was operating alone."

**Misinterpretations 3 and 4** — that a small P value means the hypothesis is false, and a large one means it is true. Both refused. Paraphrased rather than quoted because the source's wording carries comparison symbols that do not survive extraction: a small value flags the data as unusual if *every* assumption held, and may be small because some assumption other than the hypothesis failed; a large value indicates only that the data are not unusual under the model [@greenland2016misinterpretations, p. 341].

**Misinterpretation 6** — that a large null P value shows no effect was observed or that absence of an effect was demonstrated. The source refuses this and gives a specific reason, paraphrased here for the same extraction reason: unless the point estimate equals the null value exactly, some association is present in the data, and one must look at the point estimate to see which effect size is most compatible with it [@greenland2016misinterpretations, p. 341].

*Book analogue:* Chapter 5. Absence of a failed check is not evidence of adequacy.

**Misinterpretation 19** — that a specific reported 95 % interval has a 95 % chance of containing the true value. The correction begins: "No! A reported confidence interval is a range between two numbers" [@greenland2016misinterpretations, p. 343].

*Book analogue:* Chapter 6's calibration and Chapter 7's balance. A property defined over an ensemble of repetitions, read off one instance.

## 5. Two results a reader will not expect

**Overlapping intervals do not mean agreement.** The source gives a worked case: two 95 % intervals, `(1.04, 4.96)` and `(4.16, 19.84)`, overlap, "yet the test of the hypothesis of no difference in effect across studies gives P = 0.03" [@greenland2016misinterpretations, p. 344]. The eyeball test on overlapping intervals is not a test.

**Intervals impose the same dichotomy.** "confidence intervals force the 0.05-level cutoff on the reader … and in this way are as bad as presenting P values as dichotomies" [@greenland2016misinterpretations, p. 344].

That second one closes the escape route completely: reporting an interval and reading whether it covers zero is the same ritual with a longer name.

## 6. What the source recommends

Four guidelines, quoted from [@greenland2016misinterpretations, p. 347]:

> (a) "Correct and careful interpretation of statistical tests demands examining the sizes of effect estimates and confidence limits, as well as precise P values (not just whether P values are above or below 0.05 or some other threshold)."
>
> (b) "Careful interpretation also demands critical examination of the assumptions and conventions used for the statistical analysis—not just the usual statistical assumptions, but also the hidden assumptions about how results were generated and chosen for presentation."
>
> (c) "It is simply false to claim that statistically nonsignificant results support a test hypothesis, because the same results may be even more compatible with alternative hypotheses—even if the power of the test is high for those alternatives."
>
> (f) "Any opinion offered about the probability, likelihood, certainty, or similar property for a hypothesis cannot be derived from statistical methods alone. In particular, significance tests and confidence intervals do not by themselves provide a logically sound basis for concluding an effect is present or absent with certainty or a given probability."

Guideline (b) is principle 4 and the p. 339 spine, for a third time from a third direction.

## 7. The instance a reader cannot dismiss as academic

Guideline (e) records:

> "statistical significance is neither necessary nor sufficient for determining the scientific or practical significance of a set of observations. This view was affirmed unanimously by the U.S. Supreme Court, (Matrixx Initiatives, Inc., et al. v. Siracusano et al. No. 09–1156. Argued January 10, 2011, Decided March 22, 2011)" [@greenland2016misinterpretations, p. 347]

**A unanimous supreme court, in a securities case, on the record.** The chapter should use this once, because a reader inclined to treat the whole argument as academics quarrelling has to account for it.

**Attribution discipline:** the case is cited **as reported at** `greenland2016misinterpretations` p. 347. The judgment itself was not read, and the manuscript claims nothing about its reasoning.

## 8. What the chapter must not do

- Teach any test procedure, distribution, or power calculation.
- Present the ASA statement's elaborating paragraphs, which were not read.
- Claim the field agrees on what to do instead. The source's own conclusion offers guidelines "in the hopes of minimizing harms of current practice" [@greenland2016misinterpretations, p. 347], which is not the language of a settled replacement.
- Present p-values as worthless. Principle 1 says they can indicate incompatibility with a model, and the paper's objection is to the dichotomy, not the quantity.
- Suggest that reporting intervals instead solves it. §5 forecloses that.

## 9. Stop condition

Met. Six principles verbatim; four misinterpretations with locators; the source's closing characterisation; four guidelines; one non-academic instance with its attribution discipline recorded.

Not read: `greenland2016misinterpretations` pp. 345–346 on power, beyond guideline (c)'s reference to it; the American Statistician article behind `asa2016pvalue`.
