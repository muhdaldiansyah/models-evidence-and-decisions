# Chapter 6 — Diagnosis Feedback

Open this file only **after** you have written your diagnosis of all five statements in §7.

Your wording will differ; what matters is whether you found the same fault.

## 1. "There is a 70% chance the pump is the cause."

**Defect.** The number is stated as though it were a property of the pump.

Nothing is said about what it is conditional on — which register, which observations, which assumptions. The sentence reads as a fact about the world, and it is a fact about somebody's evidential position.

**What it costs.** Nobody can disagree with it. To argue about a probability you have to argue about what it was conditioned on, and there is nothing on the page to take hold of. It also cannot be updated, because you cannot tell what has already been counted — if the pump test is run tomorrow, does the 70% already include it?

**Repair.** Write the conditioning in. *Given the register of pumped-zone investigations and no test result, the odds favour the pump about 1.75 : 1, which is about 64%.* Longer, arguable, and updatable.

**Note.** This is the most common defect in the list and the least dramatic. It rarely causes a visible error. It causes an analysis that cannot be checked, which is worse and slower to notice.

## 2. "We said 80% and it happened, so the forecast was good."

**Defect.** A single forecast is being scored.

**What it costs.** The claim is empty. An event called 80% happening is exactly what should occur about four times in five; it is also consistent with 30%, and with 99%. One outcome discriminates almost nothing between any two probabilities strictly between 0 and 1.

The real cost is what the sentence licenses. If a hit proves the forecast was good, a miss proves it was bad, and the forecaster learns to state numbers that survive single outcomes — which means numbers near the middle, which means saying nothing.

**Repair.** Group the statements by what was said and compare each group against how often it happened. That needs a record and time. There is no shortcut, and an organisation that wants its forecasts assessed has to start keeping one before it can have one.

**Note.** The inverse error is just as common and reads as fair-mindedness: *we said 80% and it didn't happen, so we got it wrong.* Also unfounded, from the same missing record.

## 3. "The pump test came back positive, so it is probably Mechanism A."

**Defect.** The inversion.

The supplied 0.85 is how expected a recovery is **if Mechanism A holds**. The sentence treats it as how likely Mechanism A is **given the recovery**. Those are different quantities, and only the first was supplied.

**What it costs.** It depends entirely on the prior, which is exactly the thing the sentence has dropped. Here the prior mildly favours A, so the correct answer is about 91% — higher than 0.85, and the error happens to be in a harmless direction. Change the register to 4 : 7 and the same test result gives about 76%, and the sentence would be badly wrong while sounding identical.

**Repair.** Multiply. Prior odds times the ratio of the two likelihoods. If the prior is not available, say so and say the conclusion is unavailable with it — do not substitute the likelihood for the answer.

**Note.** This is the error §2 spent its length on and it still survives contact with real work, because the mistaken sentence is shorter, sounds like a summary, and is usually said by someone who did the difficult part correctly.

## 4. "We ran 50,000 simulations, so the estimate is reliable."

**Defect.** Run count is being offered as evidence about the world.

**What it costs.** 50,000 runs buys precisely one thing: a stable answer about the assumptions that were fed in. Every question about whether those assumptions are any good survives the run count untouched — the spread that was supplied and never justified, the forecast that was conditional on no new action, the storage model with no spill term.

And the sentence actively obstructs the useful conversation, because it offers a large number as reassurance and the number is about the arithmetic.

**Repair.** Report the run count as what it is — a statement about Monte Carlo error — and report separately what the result is conditional on. Then, if you want to say something about reliability, vary the *structure*: run it with the spill term, with a different spread, with the conservation request in.

**Note.** This is the third appearance of one shape. More measurements improve precision, not trueness (Chapter 3). More records shrink sampling variability, not the data-quality term (Chapter 4). More runs shrink Monte Carlo error, not model error. When told more of something will fix a problem, ask which term it enters.

## 5. "You cannot put a number on a one-off event like this."

**Defect.** Probability is being treated as requiring a frequency.

The premise is right — there is one Hillcrest and no long run to average over. The conclusion does not follow, because the number was never a claim about a long run. It describes what the available information supports.

**What it costs.** More than the other four combined, and it is the only one that sounds like intellectual caution.

Refusing to state a number does not remove the uncertainty. It moves it somewhere it cannot be examined. The decision still gets made, still on somebody's implicit sense of how likely things are, and now nobody can ask what that sense was conditioned on, whether it should move when the test comes back, or whether the people holding it have been right before.

**Repair.** State the number with its conditioning information, and treat the objection as a request to be explicit about what you are conditioning on rather than a reason not to answer.

**Note.** Take the person seriously. They are usually right that the situation is unique and right that a spuriously precise number would be false comfort. The answer is not that they are being unhelpful — it is that the alternative to a stated number is not *no number*, it is an unstated one.
