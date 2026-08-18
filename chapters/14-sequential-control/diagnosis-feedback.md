# Chapter 14 — Diagnosis Feedback

**Open this only after you have written all five diagnoses.**

Four of these statements contain a defect. **One is true of this case and false as a general claim**, which is a different kind of problem and the one worth finding.

Nothing here is scored.

---

## 1. "P1 has worked for nine years, so it is a reasonable rule."

**The defect.** Nine years of use is evidence that the rule is **survivable**, not that it is good — and the two feel identical from inside.

The utility's record says how P1 behaved in nine particular summers. It says nothing whatever about how P2 or P4 would have behaved, because neither was ever in force.

> "Purely evaluative feedback indicates how good the action taken was, but not whether it was the best or the worst action possible." [@sutton2018reinforcement, p. 25]

**What it stops you concluding.** Anything comparative — which is the only kind of conclusion that matters when you are choosing a rule. And it stops you noticing that P1 is beaten on all four measures by a rule differing from it in a single clause.

**The repair.** Never assess a rule on its own record. **Write down at least one alternative and run both against the same histories**, which on this case took an afternoon and produced a result nine years of operation could not.

**And a caution about the repair.** Having found that P1 is dominated, the temptation is to conclude that somebody was careless. **P1 was a reasonable rule to write.** It watches the right quantity, acts in proportion, and stands down. What nobody did was ask *compared to what?* — and nobody's job description contained it.

---

## 2. "We can't tell leakage from base demand, so we need more data."

**The defect.** More data of the kind the utility collects will not help, and the reason is in the model rather than in the data.

Base demand and leakage enter the model only through their sum. Any increase in one is exactly cancelled by a decrease in the other, and the predictions do not move. **The three splits fit exactly equally well, not approximately equally well**, and another decade of records would produce the same exact tie.

**This is structural non-identifiability**, and it is what the source means by parameters whose changes "can be fully compensated by altering other parameters" [@wieland2021identifiability, p. 61].

**What it stops you concluding.** That the question is answerable by the means proposed. Worse, it converts an unanswerable question into a funded project, which will run for years and end where it began.

**The repair, and it has two branches** [@wieland2021identifiability, p. 64].

**Measure differently.** Not more of the same — differently. Something that observes one of the two on its own. The night-flow meter works because at 03:00 base demand is near zero, so the sum has one term in it.

**Or model less.** Drop the distinction, report a combined figure, and **write down that you have done so**. This is what the utility already did in 2014 without recording it, and Chapter 4 is a chapter about what that cost.

**The check that distinguishes them takes ten minutes.** Write down the model. Write down what is measured. Look for parameters appearing only in combination. Ask what measurement would break the combination.

---

## 3. "P4 is better than P1 on every measure, so the utility should switch to P4."

**This is the one that is true of this case and wrong as a general claim.**

It is true that P4 beats P1 on all four tabulated measures across all five summers. Nothing in the sentence is false about the case.

**The defect is that it treats four measures over five summers as though it were the answer**, and three things are missing.

**P2 also beats P1**, and P2 beats P4 on the measure the utility's service standard is written in — days below the critical level. The sentence quietly picks a winner from a two-way tie that the arithmetic does not break.

**The four measures were chosen.** Nothing counts operator workload, and P4 requires two figures to be right where P1 requires one — and Chapter 4 established that one of P4's two, the demand figure, is a residual.

**The five summers were chosen.** A sixth, with a two-week heatwave, might rank them differently, and nobody has said how likely any of the five is.

**What it stops you concluding.** Nothing, in this case — the recommendation may well be right. **What it stops you doing is stating the conditions**, and a recommendation whose conditions are unstated cannot be revisited when they change.

**The repair.** Say what the recommendation is conditional on: these measures, these histories, and a judgment about the day-below-standard against the spill. Then say who made that judgment.

---

## 4. "We should run P4 next summer and see how it does."

**The defect.** Most summers will not tell you anything, and the sentence assumes every summer is a trial.

On the mild summer **all four rules produce identical results**. Between P2 and P4 — the two rules actually in contention — **two of the five summers are identical**. A year of running P4 has roughly a three-in-five chance of being informative about the comparison, and the utility gets one year per year.

**What it stops you concluding.** It leads an organisation to expect an answer next autumn, and to draw one whether or not the summer discriminated. A mild summer under P4 will read as *P4 was fine*, which is true and empty.

**The repair.** **Say in advance what would count as an informative summer**, and say what you will conclude if the summer is not one. On this case: a summer in which demand exceeds 115 for at least two days and storage falls below 200, because outside those conditions P2 and P4 issue the same orders.

**And note what running a rule cannot do.** The utility cannot repeat a summer, cannot choose which kind it gets, and cannot run two rules side by side on one reservoir. Simulation does some of the work the trials cannot — and Chapter 13's warning applies: a convincing simulation of a wrong system teaches its wrongness efficiently.

---

## 5. "The reservoir is under control — we have a documented operating rule and daily monitoring."

**The defect.** `control` names an activity, not an achievement, and the sentence uses it as though it were a verdict.

> "In this book, we define control to be the use of algorithms and feedback in engineered systems." [@astrom2008feedback, p. 3]

The loop is **sensing, computation, actuation** [@astrom2008feedback, p. 4]. A system with a controller on it is under control in that sense whether the controller is any good or not.

**Now look at the utility in those three terms.**

**Sensing.** Its instruments cannot distinguish the two states its rule most needs to distinguish, and cannot separate two parameters its capital programme turns on.

**Computation.** Its rule was never compared with an alternative and is dominated by one that differs in a single clause.

**Actuation.** Its production changes take two days to arrive, which Chapter 13 showed is most of why the rule fails.

**Failing at all three, and under control the whole time.**

**What it stops you concluding.** That anything needs attention. It is the most comfortable sentence in the list and it will pass every review, because everything in it is true.

**The repair.** When somebody says a process is under control, ask the three questions separately. **Can we see the state? Is the rule the best of the ones we compared? Does the action arrive in time?** Each has an answer, and "we have a documented rule and daily monitoring" is not one of them.

---

## What the five have in common

**Three of them are true.**

P1 has worked for nine years. P4 is better than P1 on every tabulated measure. The reservoir has a documented rule and daily monitoring. Not one would fail a fact-check.

**And the fourth is a reasonable-sounding response that funds the wrong project**, while the fifth is a reasonable-sounding plan that will produce a confident answer from an uninformative year.

**The shape is the same throughout.** Each sentence answers a question that was not asked. *Has this rule survived?* instead of *is it the best rule we have compared?* *Can we collect more?* instead of *would more of this help?* *Is there a loop?* instead of *does the loop work?*

**And the repairs are all the same move**: name the question the sentence is actually answering, then ask the one you meant.
