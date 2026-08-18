# Chapter 7 — Diagnosis Feedback

Open this file only **after** you have written your diagnosis of all five statements in §7.

Your wording will differ; what matters is whether you found the same fault.

## 1. "We controlled for every variable in the dataset, so the estimate is unbiased."

**Defect.** Adjustment is being treated as a data-processing choice rather than a causal claim.

Which variables to adjust for is a question about causal structure. Answering it by taking everything available is answering it with the filing conventions of whoever built the dataset.

**What it costs.** Two things, and the second is worse.

The obvious cost is that the confounders you needed may not be in the dataset at all, and adjusting for everything present does nothing about anything absent.

The less obvious one is that adjusting for more can make the answer **worse**. The practice "of conditioning on as many pre-treatment measurements as possible should be approached with great caution; some covariates … may actually increase bias if included in the analysis" [@pearl2009causal, p. 117]. Adjusting for the wrong variable can open a spurious route that was closed.

And the sentence forecloses the conversation. It sounds like the maximum available diligence, so nobody asks what was assumed.

**Repair.** State the causal claim the adjustment set embodies: these variables, because they plausibly affect both the treatment and the outcome; not those, for stated reasons. Then say what would have to be true for the set to suffice, and who would know.

**Note.** The person saying this is usually being careful, not lazy. They have done more work than someone who adjusted for nothing. The problem is that the extra work was done in the wrong currency — more covariates instead of a stated structure.

## 2. "It was a randomized trial, so the two groups were balanced."

**Defect.** A property that holds in expectation over hypothetical replications is being read off a single trial.

**What it costs.** The claim is not available. In your one trial, "there is nothing in randomization that limits" the size of the imbalance [@deaton2016rct, p. 9], and by chance it can over-represent an important cause. What randomization gives you is an unbiased estimate and a sound way to compute the error — "therein lies its virtue, not that it yields precise estimates through balance" [@deaton2016rct, p. 10].

This is not a subtlety that only pedants notice. A jointly issued World Bank and Inter-American Development Bank manual states that a randomized impact estimate "constitutes the true impact of the program, since we have eliminated all observed and unobserved factors that might otherwise plausibly explain the difference in outcomes", quoted at [@deaton2016rct, p. 10] — and the diagnosis is that it "confuses actual balance in any single trial with balance in expectation over many (hypothetical) trials" [@deaton2016rct, p. 11].

**Repair.** Say what the design licenses: an unbiased estimate of the effect in this trial's sample, with a computable error. Report the error. Then, separately, say whether the trial's target quantity is the one you were asked about.

**Note.** You met this shape in Chapter 6. Calibration is a property of a forecaster across a record; scoring one forecast is a category error. Balance is a property of a procedure across replications; reading it off one trial is the same error. Two fields, one mistake.

## 3. "We have twelve years of records on fifteen zones, so we can settle this."

**Defect.** Quantity of evidence is being offered against a problem that quantity does not touch.

**What it costs.** Every identification problem in the case survives the twelfth year exactly as it survived the first. The upgraded zones were still the worst-complaining ones. Old-main zones still received no upgrades. The register still recorded four different actions as one. The mains renewal programme still ran alongside.

More records make the numbers steadier. They make an unidentified quantity **more precisely** unidentified, and — the part that does the damage — everything visible in the output improves while nothing that matters does.

The general statement is that "sensitivity to prior causal assumptions … remains substantial regardless of sample size" [@pearl2009causal, p. 101], in contrast to statistical assumptions whose influence shrinks as data accumulates.

**Repair.** Ask which term the extra data enters. If the answer is *the one that was already small*, the collection is not worth commissioning. Then ask what would help instead: how the treated cases were selected, whether the missing kind of case exists anywhere, whether a mechanism argument is available, whether one comparison could be arranged deliberately.

**Note.** Fourth appearance of one shape. More measurements improve precision, not trueness (Chapter 3). More records shrink sampling variability, not the data-quality term (Chapter 4). More runs shrink Monte Carlo error, not model error (Chapter 6). More records do not touch causal assumptions. The first three were this book's observation; this one is the source's.

## 4. "The model predicts pressure drops with 94% accuracy, so we know what causes them."

**Defect.** Predictive performance is being read as causal knowledge.

**What it costs.** A predictive relationship may capture association with no causal interpretation, and a variable that predicts well is not automatically a lever [@shmueli2010predict]. A model can predict Hillcrest's pressure drops beautifully from complaint volume, which is a consequence of the drops rather than a cause of them, and acting on complaints would do nothing.

The specific damage is that the 94% is genuinely impressive and genuinely irrelevant to the question. It will carry the room, because everyone can see it is a good number and nobody can see what it is a good number **for**.

**Repair.** Say what the model licenses — prediction of the outcome under conditions like those it was fitted on — and say explicitly that it licenses nothing about what happens if any input is changed. If a causal claim is needed, that is a different question requiring assumptions the model's accuracy has no bearing on.

**Note.** This one is aimed at Chapter 6, which spent twelve thousand words making you good at prediction. Being good at prediction is worth having and is not this chapter's currency. The hazard is structural: **a dashboard is built for prediction and gets read for intervention**, and nothing on the screen marks the transition.

## 5. "The effect isn't identified, so there's nothing we can say."

**Defect.** A finding is being treated as a dead end.

**What it costs.** More than the other four together, because it is the response of somebody who has understood the chapter and drawn the wrong conclusion from it.

Non-identification is informative. It says the question as posed cannot be answered by this kind of evidence; it says which assumption the whole argument turns on; and it usually says what different evidence would look like. The four-step sequence includes it: estimate the quantity if identifiable, "or approximate it, if it is not" [@pearl2009causal, p. 122].

And the practical cost is that the decision still gets made. Declining to report anything does not pause the capital programme. It means the decision proceeds on somebody's unexamined intuition, with the one person who understood the problem having said nothing.

**Repair.** Write the three-part verdict. What is not identified, stated as a target quantity. Which assumption would change it. What you would go and get.

**Note.** Notice that such a verdict is **disagreeable** in the useful sense: an engineer can dispute the allocation rule, or produce a comparison case you did not know about. Those are productive arguments about checkable facts. A number with an interval invites no such conversation, because the only thing available to argue about is the number.
