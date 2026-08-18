# Chapter 12 — Diagnosis Feedback

**Open this only after you have written all five diagnoses.**

Each statement contains one defect. Below is the defect, what it stops you concluding, and a repair.
Nothing here is scored. Where your answer names a different defect that is also present, that is a better outcome than matching this page.

---

## 1. "We ranked the schemes by benefit per pound and funded down the list until the money ran out."

**The defect.** The rule is being applied to indivisible schemes, where it does not find the best affordable set.

Ranking by ratio is correct when items are divisible — when you can buy the last scheme in fractions and the money always runs out mid-item. Every capital scheme in a programme is all-or-nothing, so the money runs out **between** items, and what is left over may be enough to have changed which items you should have taken.

**What it stops you concluding.** Anything about whether this is the best programme. The procedure has produced a defensible-looking answer to a different question: *what order should these be in?* rather than *which set should we fund?*

**In the chapter's programme** the ranking gave A + B + F1 + C, delivering 915 and stranding £460k against a cheapest remaining scheme of £540k, while the best affordable programme delivered 985. The ranking missed by 70 and nothing in its output said so.

**The repair.** Search for the best affordable combination and compare it with the ranking's answer. If they agree, the ranking was safe here and you now know it. If they disagree, you have found what the ranking cost.

**And a two-minute proxy when a full search is impractical:** look at the largest scheme as a fraction of the envelope, and look at what the ranking leaves unspent. A scheme worth a large fraction of the budget, or leftover money that cannot buy anything, means the ranking has almost certainly stopped in the wrong place.

---

## 2. "The optimiser found the best programme, so that is the programme."

**The defect.** The optimiser found the best programme **according to the objective and constraints it was given**, and both were written by somebody.

An optimum is a conditional statement: given this objective function, these constraints, and these benefit estimates, this set maximises. Every one of those inputs is a choice, and the strongest of them is the objective — which typically monetises several incommensurable things into one column so that the arithmetic can run at all.

**What it stops you concluding.** That the programme is right. It is optimal with respect to a formalisation, and the formalisation is where the value judgments went.

**Chapter 10's warning arrives here in a sharper form.** There it was possible to argue about an objective because it was a sentence. Once it is an objective function, arguing about it looks like obstructing the analysis.

**The repair.** State the objective and constraints in plain language alongside the result, and say who set each. Then ask the two questions Chapter 10 supplies: is this an item of value, and is the direction of preference right? An optimum whose objective nobody has read is a computation, not a decision.

**A second repair.** Re-run under one alternative objective. If the answer does not move, the objective was not load-bearing and you can stop worrying about it. If it does, you have found the real decision.

---

## 3. "An extra £100k would be worth about 34 household-events a year."

**The defect.** A single number is being reported as the value of relaxing the constraint, on a problem where the value is a staircase.

The figure 34 is presumably the divisible shadow price — the ratio of the next scheme in the ranking, or the slope of a smoothed curve. On an indivisible programme the actual answer to *what does another £100k buy?* is whatever the best affordable set at £2.5m delivers minus what the best set at £2.4m delivers, and that difference is frequently **zero**, because £100k is not enough to reach the next thing worth having.

**What it stops you concluding.** Whether to ask for more money, and how much. The one number is wrong in both directions: it overstates small increments, which usually buy nothing, and understates large ones, which can buy a great deal.

**In the chapter's programme:** £2.4m to £2.45m bought 3. £2.56m to £2.61m bought nothing. £2.4m to £2.6m bought 98 — and the last figure is the one that would have changed the conversation.

**The repair.** Price the constraint at several increments and report the shape, not a slope. Say where the steps are. A number like *£200k buys 98 and £50k buys almost nothing* names a threshold somebody can act on; *worth 34 per £100k* does not.

**And price it downward too.** The cost of a cut is not the mirror of the gain from an addition, and the cut is the direction nobody volunteers to compute.

---

## 4. "We tested twenty scenarios, so the plan is robust."

**The defect.** The number of scenarios is not the property that matters; what matters is whether they span the ways the plan could fail, and who chose them.

Twenty scenarios generated by varying two demand parameters are twenty points along one axis. A plan that survives all of them has been tested against one kind of surprise. The failure mode that matters is usually the one nobody put on the list — a regulatory change, a workforce constraint, a technology that makes the whole scheme unnecessary — and no amount of resampling the axes you thought of will surface it.

**What it stops you concluding.** That the plan is robust. It supports a narrower claim: the plan survives these twenty, which is worth stating and is not the same thing.

**There is also a second, quieter defect.** "Robust" here is doing the work of "the answer did not change", and Chapter 8's sensitivity analysis made the same move. An answer that does not move under variation you chose may be stable, or the variation may have been too small.

**The repair.** Report the scenario set as a choice with an author, say what kinds of surprise it does and does not represent, and name at least one future that is credible and absent. Then say what the plan does about that one.

**The honest form of the claim** is: *robust across these futures, chosen by these people, on these grounds — and here is one we could not represent.*

---

## 5. "The plan is adaptive — we will review it annually."

**The defect.** A review date is not a signpost. It says when somebody will think, not what would change their mind.

An adaptive plan has three parts: what is committed now, what is deferred, and the observable condition that converts a deferred option into a commitment. The third part needs a quantity somebody already measures, a threshold with a number on it, a named owner, and a frequency. A review has none of them.

**What it stops you concluding.** That the deferred commitment will ever actually be made. Annual reviews reliably conclude that conditions have not changed enough, because "enough" was never defined — and the option that was bought at a premium quietly expires unexercised.

**The repair.** Replace the date with a trigger. *Peak-week demand exceeding the Chapter 1 forecast by more than four per cent in two consecutive summers, taken from a measurement the utility already makes, reviewed each September by the network manager* is a signpost. It can be checked, it can be disagreed with in advance, and it fires without anyone having to reopen the argument.

**A test.** Ask whether somebody who disagrees with the plan could dispute the threshold today. If they could, it is a signpost. If there is nothing to dispute, it is a diary entry.

---

## What the five have in common

Four of them are procedures that produce a plausible output while answering a question nobody asked, and the fifth is a word doing work it has not earned.

**None of them fails loudly.** A ranking produces a fundable programme. An optimiser produces an optimum. A shadow price produces a number. Twenty scenarios produce a chart. An annual review appears in the plan.

That is why every repair on this page is a **procedure applied before there is any reason for suspicion**, rather than a response to a symptom. The symptom is the thing these five do not have.
