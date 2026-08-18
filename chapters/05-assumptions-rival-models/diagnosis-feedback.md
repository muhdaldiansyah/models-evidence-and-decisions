# Chapter 5 — Diagnosis Feedback

Open this file only **after** you have written your diagnosis of all five defects in §6, and after you have placed the four situations.

Your wording will differ; what matters is whether you found the same fault.

## 1. "The data may be incomplete; the assumptions may not hold; the model is a simplification; further research is recommended."

**Defect.** Criticism has been replaced by doubt. Not one item carries anything that would settle it, and every sentence would apply, unchanged, to any analysis in any field.

**What it costs.** The reader finishes it knowing the author is aware that analyses can be wrong, and knowing nothing about whether this one is. It is unfalsifiable, so it cannot be acted on, argued with, or checked off.

**Repair.** Replace each item with a specific claim about *this* analysis, paired with the observation that would settle it. If an item cannot be made specific enough to be wrong, delete it — it was never a criticism.

**Note.** This paragraph is not lazy. It is usually written by someone who has genuinely thought about the problem and has no format for saying so. The format is the thing this chapter supplies.

## 2. "We documented all model assumptions in Appendix C."

**Defect.** Naming an assumption is being treated as handling it.

**What it costs.** An eleven-item appendix with nothing attached to any item establishes that the author was aware, not that any assumption holds. It also creates a specific hazard: it *looks* like the criticism has been done, so nobody does it.

**Repair.** Every entry gets a second half — what would show this false — and a label saying whether that observation is available now, obtainable with effort, or not obtainable. The three deserve different responses, and an appendix that does not distinguish them is hiding its own to-do list.

**Note.** The template from Jacob and Monod is the correct shape: *our conclusions might be invalid if (i), (ii), or (iii); here is what would eliminate each.* Note the second clause. Most appendices contain only the first.

## 3. "The model reproduces last year's observed storage within 3%, confirming its validity."

**Defect.** Fit is being treated as validation.

**What it costs.** Fitting past data is weak evidence against structural error, because a wrong model with adjustable parts will often fit. It is particularly weak here: the model was built from last year's data, so reproducing it is close to guaranteed and could not have come out the other way — which by §3's test means it establishes nothing.

Worse, this is the one check the analysis reports, so it will carry the whole weight of the reader's confidence.

**Repair.** Ask what the model predicts that it was *not* built to reproduce, and check that. Then say what the fit does and does not establish: the arithmetic is verified; whether it is the right model is a separate question.

**Note.** The verification/validation pair is the cleanest correction here. The 3% figure is a verification result being reported as a validation result.

## 4. "Criticism and robustness: we varied each input parameter by ±20% and the conclusion was unchanged in all cases."

**Defect.** Sensitivity analysis is being offered as criticism.

**What it costs.** Varying inputs explores uncertainty *inside* a formulation and therefore cannot see the formulation. A structurally wrong model produces a stable sensitivity analysis, and the stability gets reported as confidence — which is worse than reporting nothing.

Everything Part I found would have survived this exercise. Varying the Hillcrest demand figure by ±20% would not have revealed that it was a subtraction residual. Varying the monitoring-point pressure would not have revealed that it was measured in the wrong place.

**Repair.** Sensitivity analysis is a real and valuable technique, and it belongs to Chapter 8. Keep it, label it as what it is, and add a criticism section that asks whether the formulation itself could be wrong.

**Note.** This is the most sophisticated-looking way to skip this chapter, which is why it is the hardest of the five to catch. If you marked it as adequate criticism, that is worth sitting with.

## 5. "All models are wrong, so this cannot be settled definitively."

**Defect.** A true general remark is being used to terminate a specific question.

**What it costs.** The reviewer asked whether the pump is really the constraint. That question **can** be settled — Chapter 2 named the observation, and it takes a technician, an afternoon, and a portable gauge. The response converts an answerable question into an unanswerable one and closes it.

**Repair.** Separate the two claims. Yes, the model is wrong in some respects; that was never in doubt. The question is whether it is wrong **in a way that matters for this use, at this risk** — and for this particular objection, here is the observation that would settle it and here is what it costs.

**Note.** The remark's usual source runs the opposite way. Recognising the limits of a model is offered there as a reason to expand boundaries and take responsibility, not as grounds for abandoning judgment. Used as an off-switch, it is the exact inversion of its point.

## The four placements

| Situation | Placement |
|---|---|
| The Hillcrest figure stays positive when Hillcrest consumption is zero | **Chapter 5** — the formulation is wrong |
| The 0.62 figure is a two-week study from three years ago and may be off | **Chapter 8** — uncertainty in a quantity |
| Mechanism A and Mechanism B are both still alive | **Chapter 5** — structural uncertainty |
| Varying friction loss between 4 and 8 metres to see what changes | **Chapter 8** — sensitivity within a formulation |

The first and third concern whether the model is right. The second and fourth concern how uncertain an answer is, given the model.

**The fourth is the trap**, and it is the same trap as defect 4 above. If you placed it in Chapter 5, you are in good company — it is systematic, quantitative, and produces output that looks exactly like criticism.

The test that separates them: **could this exercise tell me my model has the wrong structure?** Sensitivity analysis cannot, by construction. It holds the structure fixed and moves the numbers inside it.

## After you have compared

Do not simply correct your answers.

Pick the defect you got most wrong and write two sentences on **why it read as diligence**. Four of these five appear in real reports written by careful people, and all four are what carefulness looks like when nobody has been told what criticism requires.
