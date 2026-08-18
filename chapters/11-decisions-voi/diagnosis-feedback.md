# Chapter 11 — Diagnosis Feedback

Open this file only **after** you have written your diagnosis of all five statements in §6.

Your wording will differ; what matters is whether you found the same fault.

## 1. "The test moves belief from 64% to 91%, so we should run it."

**Defect.** How informative an observation is, is being read as how valuable it is.

**What it costs.** The two are different quantities and neither can be computed from the other. Chapter 6's ratio of about 5.7 is entirely about the evidence — how much more expected a recovery is under one mechanism than the other. **It contains nothing about the acts, the costs, or the currency.**

On the anchor, the same test with the same ratio and the same prior is worth **£2,300**, because on the branch where it comes back positive the utility does what it was going to do anyway, and on the branch where it does not, the better act wins by only £5,700.

The standing example is a radiograph for a suspected broken toe: "the treatment for a bruised toe or a broken toe is the same: strap it and avoid any activities that hurt the toe. The value of information delivered by the radiographic examination in this decision about treatment is zero" [@colyvan2016voi, p. 303]. **The radiograph works perfectly.**

**Repair.** Ask three questions: what would we do differently, in which cases, and how often do those arise? Then multiply the improvement by the chance of getting that branch. On the anchor it is `0.404 × 5.7`.

**Note.** A ratio near 1 does establish that a test is worthless — Chapter 6 said so and was right. **The implication does not run the other way.** A large ratio establishes nothing about worth.

## 2. "Expected value says Act A, so Act A it is."

**Defect.** A rule is being treated as a result.

**What it costs.** Choosing the act with the lowest expected cost treats a certainty of £173,600 as equivalent to a gamble between £130,000 and £250,000. That equivalence is a statement about how much the utility minds spread, and the name for minding it not at all is risk neutrality.

Act C costs £216,000 whatever happens. A committee that will not accept a £250,000 outcome can take it, paying **£42,400** in expectation to remove the spread. **That is not an error and no evidence can settle it.**

The source shows the same thing from the other side: at equal expected monetary value, "decision theory recommends indifference" [@colyvan2016voi, p. 303] — **because expected monetary value is the rule being applied.**

**Repair.** Report the expected values, name the rule, and — if any act has no spread — report what removing the spread would cost. Then let the decision-maker choose, because the choice is theirs.

**Note.** Chapter 6 refused to make this move and instructed this chapter to make it in the open. The instruction is in the book's terminology registry, which is unusual: it does not defer the topic, it specifies that the deferral must end deliberately.

## 3. "We varied every input by 20% and the answer held, so the analysis is robust."

**Defect.** A fixed percentage has been substituted for the question sensitivity analysis exists to answer.

**What it costs.** Twenty per cent is not a property of anything. It is not the uncertainty in the probability, or in the costs, or in the monetisation, and an answer that survives it has survived nothing in particular.

**The useful output is a critical value.** On the anchor, Act A beats Act C when `p > 0.283`, and belief sits at 0.636 — so the prior would have to be less than half what the register says before the answer changed. That is two lines of arithmetic and it says something.

And the check finds different things than percentage-wiggling does. On the anchor, Act A stops winning at **£82,400** of capital against a £40,000 estimate — so a doubling survives and slightly more does not. **The input everyone was arguing about turned out not to matter; the one nobody questioned nearly flips it.**

**Repair.** For each uncertain input, find the value at which the recommendation changes, and say how far you are from it. Report critical values, not ranges of answers.

**Note.** This book has used the phrase three times for three jobs — refused as criticism in Chapter 5, used as a model check in Chapter 8, and used here to find where the act changes. In none of the three does varying everything by a fixed percentage answer the question.

## 4. "We can't put a number on the probability, so we can't analyse this decision."

**Defect.** Not knowing a probability exactly is being treated as a barrier to analysis.

**What it costs.** It is frequently not a barrier at all, and finding out costs two lines.

The source works it: offered $20 on heads and paying $10 otherwise, with the probability known only to lie between 0.4 and 0.6 — "a simple sensitivity analysis of the decision model here shows that the expected utility of accepting the bet is greater than rejecting it. **No further information is required in deciding whether to accept this bet or not**" [@colyvan2016voi, p. 302].

And the contrast on the same page: with a range of 0.2 to 0.4, which "straddles the critical value of 1/3", the analysis genuinely does not settle it.

**Same ignorance. Opposite conclusions about whether it matters.** What separates them is whether the range reaches the point at which the best act changes.

**Repair.** Find the critical value first. Then ask whether any probability you would defend falls on the other side of it. If none does, the ambiguity is real and irrelevant, and you may proceed.

**Note.** The sentence is usually said by somebody being careful, and it is the more damaging for that. It stops the analysis at exactly the point where two lines of arithmetic would have shown the analysis was not needed — or would have shown precisely which range of belief the decision hangs on, which is the most useful thing anyone could tell the room.

## 5. "The study costs £40,000 and could tell us a lot about the network."

**Defect.** A study is being priced against what it would reveal rather than against what it would change.

**What it costs.** "It depends on what you're going to do with the information" [@colyvan2016voi, p. 304], and telling you a lot about the network is not a decision.

There is a one-line test that disposes of this without any argument about the study's merits. **Compute what perfect knowledge would be worth.** On the anchor that is **£12,400**, so no study of the question can be worth £40,000 — not a better test, not a longer monitoring programme, not a consultant's model. The ceiling does not care what the study is, because it already assumes the study works perfectly.

That calculation is one multiplication and one subtraction on a table you already built, and it should be run before any proposal is costed.

**Repair.** Compute the ceiling. If it is below the cheapest study on offer, stop. If it is above, compute the specific study's value and compare it with its price.

**Note.** The sentence is also frequently category three: information gathered "because it might be useful for some ill-defined or unknown decision down the track" [@colyvan2016voi, p. 306], wearing the clothes of information gathered for a specific decision. The source warns about exactly this slippage, and *it would help us understand the network* is what it sounds like.
