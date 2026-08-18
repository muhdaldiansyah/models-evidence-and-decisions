# Chapter 8 — Diagnosis Feedback

Open this file only **after** you have written your diagnosis of all five statements in §7.

Your wording will differ; what matters is whether you found the same fault.

## 1. "The 95% interval is 0.84 to 2.76, so we're 95% sure the true value is in there."

**Defect.** A property of the procedure is being read off one of its outputs.

**What it costs.** The response in the source is short: "No! A reported confidence interval is a range between two numbers" [@greenland2016misinterpretations, p. 343]. The 95% describes how often intervals built this way would cover the estimand, across repeated construction. Your interval either contains it or does not, and nothing about the pair `0.84, 2.76` carries a probability.

The practical cost is that the sentence licenses a decision-maker to treat the range as a settled bracket on the answer, when it is a bracket on the effect of sampling under a model — and §4 enumerated five things outside it, at least one of which is larger than the interval is wide.

**Repair.** State what the procedure does: intervals constructed this way cover the estimand about 95 times in 100, *if the model holds*. Then state what the model assumes, and say what is outside it.

**Note.** Third time in three chapters. Calibration is a property of a forecaster over a record (Chapter 6); balance is a property of randomization over replications (Chapter 7); coverage is a property of an interval procedure over repeated construction. Same error, three fields.

## 2. "We widened the interval to be conservative."

**Defect.** Widening is being treated as the cautious direction, unconditionally.

**What it costs.** It is not a direction at all until you know where the threshold sits.

On the anchor, widening the spread from 0.92 to 2.4 moved the breach probability from **77% down to 62%** — because the breach threshold of 64.2 ML sits *below* the central forecast of 64.9, so spreading the distribution moved mass to the safe side. The analyst who widened "to be conservative" reported a **more reassuring** number and believed they had been careful.

Worse, on this case widening alone was further from the honest answer than doing nothing. The honest figure was **85%**, and it required correcting the offset as well.

**Repair.** Before adjusting a spread, ask where the centre sits relative to any threshold in the decision. Then correct the centre and the spread together, and report both one-sided results so the reader can see which correction did the work.

**Note.** The two corrections are Chapter 3's precision and trueness, arriving on a forecasting process instead of an instrument. *Uncertainty* makes people think of spread; an offset in the centre is a bias and does not feel like uncertainty at all, which is why the wrong one gets fixed.

## 3. "P was 0.31, so there's no bias in the forecasts."

**Defect.** A verdict of "not significant" is being reported as an established absence.

**What it costs.** Unless the estimate is exactly zero, some difference is present in the data, and it is a mistake to report "no evidence" on the strength of a large value — you have to look at the estimate to see which values are most compatible with what you saw [@greenland2016misinterpretations, p. 341, paraphrased]. Here the estimate is `+1.1` on fourteen events, which is entirely consistent with a bias worth acting on.

And the guideline is explicit: "It is simply false to claim that statistically nonsignificant results support a test hypothesis, because the same results may be even more compatible with alternative hypotheses" [@greenland2016misinterpretations, p. 347].

The specific cost here is operational. On the anchor, three of four defensible analyses crossed the threshold and the fourth produced `+1.1`. All four agreed the forecasts run low. The sentence above converts that agreement into an absence, and the utility plans on the strength of it.

**Repair.** Report the estimate and its interval. If a verdict is demanded, say what the estimate is and what range is compatible with the record, and let the decision-maker weigh it against what a bias of that size would cost.

**Note.** Chapter 5 established that absence of a failed check is not evidence of adequacy. This is the same claim with an arithmetic verdict attached, which makes it much harder to resist.

## 4. "We tried several specifications and are reporting the cleanest."

**Defect.** An assumption of the calculation has been violated, and the sentence reports it as diligence.

**What it costs.** This is not a matter of research etiquette. The assumptions a computed number rests on "include assumptions about the conduct of the analysis, for example that intermediate analysis results were not used to determine which analyses would be presented" [@greenland2016misinterpretations, p. 339].

So the reported number is no longer a compatibility summary. One of the assumptions it is conditional on is false, in exactly the way the independence assumption could be false — and the number carries no sign of it. The ASA's principle 4 says the same institutionally: "Proper inference requires full reporting and transparency" [@asa2016pvalue].

**Repair.** Report all the specifications, in a table, with a sentence saying which you would use and why. If they agree, that is a stronger result than any single one. If they disagree, that is a finding.

**Note.** The honest version of this sentence is rarer and more damaging: *we ran one specification*. The analyst who tried several at least knows the alternatives exist. The one who ran the first thing that occurred to them exercised the same flexibility with nothing to disclose.

## 5. "The model fits the last five years to within 2%, so it's been checked."

**Defect.** Reproducing the fitting data is being reported as a check.

**What it costs.** The check could not have failed. The model was built from those five years; reproducing them is close to guaranteed, and Chapter 5 established that a check which could not have come out otherwise establishes nothing.

The 2% figure establishes that the arithmetic runs — verification — and it is being presented as evidence that the model is right, which is validation. Chapter 5 named that pair for exactly this.

The specific damage is that it is the **only** check reported, so it carries the whole weight of a reader's confidence, and it is the most precise-sounding number in the document.

**Repair.** Ask what the model predicts that it was not built to reproduce, and check that. Hold out the most recent period, fit on the rest, and look at where the held-out cases fall — as a record, not a single case. Then report both: the fit figure as verification, and the held-out performance as the check.

**Note.** Apply the three criteria. **Cheap:** yes. **Consequential:** if it failed, yes. **Falsifiable:** no. Two out of three is why it survives in the documentation — it is easy, it sounds serious, and it cannot embarrass anybody.
