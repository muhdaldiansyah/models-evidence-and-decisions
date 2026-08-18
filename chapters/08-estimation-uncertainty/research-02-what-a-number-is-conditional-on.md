# Research 02 — What a Computed Number Is Conditional On

Cluster R02 of `research-plan.md`. Closed.

Source read directly: `greenland2016misinterpretations` printed pp. 339–340, 343–344.

## 1. The spine

This paragraph is the reason Chapter 8 is one chapter rather than eight, and it should be quoted in full in the manuscript:

> "This definition embodies a crucial point lost in traditional definitions: In logical terms, the P value tests all the assumptions about how the data were generated (the entire model), not just the targeted hypothesis it is supposed to test (such as a null hypothesis). Furthermore, these assumptions include far more than what are traditionally presented as modeling or probability assumptions—they include assumptions about the conduct of the analysis, for example that intermediate analysis results were not used to determine which analyses would be presented." [@greenland2016misinterpretations, p. 339]

Three claims, each doing work.

**A computed result is about the entire model**, not the one hypothesis you had in mind.

**The model includes more than the statistical assumptions** anybody writes in the methods section.

**It includes how the analysis was conducted** — specifically, that you did not look at intermediate results and then choose what to present.

That third claim is the one that reorganises the chapter. Analytic flexibility is not an adjacent topic about research ethics. It is **an assumption inside the model**, on the same footing as the assumption that observations are independent, and violating it invalidates the computed number in exactly the same way.

## 2. What follows when the number comes out small

The same page:

> "It is true that the smaller the P value, the more unusual the data would be if every single assumption were correct; but a very small P value does not tell us which assumption is incorrect. For example, the P value may be very small because the targeted hypothesis is false; but it may instead (or in addition) be very small because the study protocols were violated, or because it was selected for presentation based on its small size." [@greenland2016misinterpretations, p. 339]

**You have found that something is wrong, and not what.**

That is Chapter 5's structure exactly. A failed check tells you a formulation is inadequate somewhere; it does not tell you where. Chapter 8's version is sharper because the number carries an air of precision that a failed sanity check does not.

## 3. And when it comes out large

> "Conversely, a large P value indicates only that the data are not unusual under the model, but does not imply that the model or any aspect of it (such as the test hypothesis) is correct." [@greenland2016misinterpretations, p. 339]

The asymmetry is worth drawing out for the reader. A small number says *something here is off*. A large number says *nothing here is obviously off*. Neither says the hypothesis is true or false, and the second says considerably less than the first.

Chapter 5's test applies without modification: a check that could not have failed establishes nothing, and a check that did not fail establishes only that it did not fail.

## 4. The same conditionality, for intervals

The source treats intervals as relatives of P values rather than as an escape from them:

> "Much distortion arises from basic misunderstanding of what P values and their relatives (such as confidence intervals) do not tell us." [@greenland2016misinterpretations, p. 340]

And it records that focusing only on null hypotheses "obscures the close relationship between P values and confidence intervals, as well as the weaknesses they share" [@greenland2016misinterpretations, p. 340].

**The weaknesses they share.** An interval is computed from the same model, under the same assumptions, including the same assumption about analytic conduct. It is not a more honest object; it is the same object presented as a range.

This closes off the easiest escape route a reader will reach for — *report intervals instead of P values* — before the chapter reaches §5.

The source does say intervals are preferable, but for a specific and narrower reason recorded at [@greenland2016misinterpretations, p. 344]: many authors hold they are superior because they shift focus away from the null hypothesis toward the full range of effect sizes compatible with the data. That is a real advantage about **where attention goes**, not a claim that the number is conditional on less.

## 5. What the chapter takes from this cluster

The organising sentence, in the book's own words and labelled as such:

> **Every number you compute is a statement about a whole set of assumptions, only one of which you were interested in — and the set includes how you conducted the analysis.**

From it, the eight items in the governed core competence become consequences:

| Core-competence item | As a consequence of the spine |
|---|---|
| estimation | the estimate is conditional on the model |
| uncertainty quantification | the interval is conditional on the same model |
| analytic-flexibility awareness | the conduct of the analysis is one of the assumptions |
| model checking | checking the assumptions you were not interested in |
| predictive evaluation | checking them against data they were not fitted to |
| measurement-error reasoning | one of the assumptions, and usually unstated |
| likelihood | the machinery that ties data to a model; concept depth only |
| regression | a model, and therefore a set of assumptions under discussion |

**Eight topics, one claim.** That is the argument for the chapter's architecture and it should be made explicit in `spec.md`.

## 6. Stop condition

Met. The spine is recorded verbatim with locator; the source itself places analytic conduct inside the model's assumptions; the consequences for intervals are recorded, including the source's reason for preferring them.

Not read for this cluster: `greenland2016misinterpretations` pp. 345–346 on power.
