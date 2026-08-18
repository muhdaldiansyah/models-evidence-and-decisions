# Chapter 17 — Diagnosis Feedback

**Open this only after you have written all five diagnoses.**

Four of these statements contain a defect. **One of them correctly identifies a monitoring gap and then proposes a monitoring fix for a failure no monitoring could catch** — which is a different kind of failure, and the one this chapter exists to prevent.

**This is the last of these in the book.**

---

## 1. "Heat events exceeded six, which is what the plan said to watch for, so the trigger fired correctly."

**The defect.** The threshold was never checked against what heat events ordinarily do, so "fired correctly" describes the mechanism and not the finding.

**Seven heat events occurred once in the seven baseline years.** That is a rate of one in seven per year, which over the plan's fifteen-year horizon is **2.1 expected firings from ordinary variation alone.** The 2025 value equals the baseline maximum and sits 1.84 standard deviations above the baseline mean.

**So the limb fired the way a timer fires.** It was going to, eventually, whether or not anything about the climate had changed.

**What it stops you concluding.** Whether anything happened. A firing that carries no information about the world is not a trigger, and treating it as one leads either to acting on nothing or — after a few false firings — to ignoring the limb entirely, which is worse.

**The repair.** Before setting any threshold, get the baseline. **Four lines: mean, spread, maximum, and how often the proposed threshold was crossed.** If the threshold sits inside the range the process already produces, it is a timer, and either the number or the construction has to change.

**And note that the other limb was fine.** Four per cent sat 2.12 standard deviations above its baseline mean and was never reached in seven years. **One limb was well set and one was not**, which is the ordinary condition and the reason to check each rather than to distrust the plan.

---

## 2. "The committee didn't act on a fired trigger. This is a governance failure and needs a stronger escalation process."

**The defect.** It diagnoses the wrong thing and prescribes accordingly.

**What happened is that a two-line rule was misread.** The report presented both limbs together; one had been watched closely for two years and had not fired; and **the disjunction was read as a conjunction.** The rule said *or*.

**A stronger escalation process does not fix that.** Escalation begins after somebody concludes that a trigger has fired, and nobody concluded it.

**And there is a second defect, which is worse.** Given the arithmetic in §3, **not acting was defensible.** Committing £1,150k on a one-in-seven-year value would have been acting on ordinary variation.

**So a governance response would install machinery to make the committee act next time — on exactly the signal it was right not to act on.**

**What it stops you concluding.** That the fault is in how the rule was written and how the report was laid out, both of which are cheap to fix and neither of which is governance.

**The repair.** Three things, none requiring a new process. **State the rule's logic in the report**, not just its result — "either limb triggers on its own" is seven words. **Report each limb separately and end each with a verdict.** And **state what happens next in the report**, not only in the plan.

**A right answer reached by misreading is not a right answer**, and the repair is to make the reading unavailable rather than to make the acting compulsory.

---

## 3. "All three monitored indicators were stable or improving, so the tool was working."

**The defect.** The indicators observe outputs, and the failure was not in the outputs.

**Worse than that: one of them improved because of the failure.** Repairs completed within target went from 94.1% to 95.6%, and it improved because routing more jobs as emergencies gets them attended sooner — which is exactly what that target measures.

**What it stops you concluding.** Anything. This is the reading the housing committee had every month for eighteen months, and it was correct in every particular.

**The repair, and it is not "monitor more things".** Ask what the monitoring **can** see, and list the stages it cannot — which will be the early ones.

**Monitoring observes outputs, so it detects failures that change outputs and is constitutionally incapable of detecting failures in what the thing was built to represent**, because those produce outputs that look right by construction. A tool that reproduces its label will always look accurate against its label.

**And the useful move is available before anything goes wrong.** The visibility table in §5 can be filled in on the day of deployment. **The rows marked "no" are the ones to check by other means**, and checking them is not monitoring — it is going back and asking what the label was.

---

## 4. "We missed the emergency-jobs problem because we weren't monitoring the right things. We should add the ratio to the monthly pack."

**This is the one that is right about the gap and wrong about the fix.**

**The observation is correct.** Emergency jobs divided by statutory hazard referrals went from 6.83 to 8.08 — up 18.3% — and nobody reported it, because one number belongs to the repairs team and the other to environmental health, and **the ratio is nobody's report.** Adding it to the pack is a sensible thing to do.

**And it would not have caught this failure.**

**The ratio is a symptom.** It moved because the tool was routing more jobs as emergencies, which happened because the tool predicts a scheduler's priority code rather than a need. **Watching the ratio would have told the authority, some months earlier, that something was wrong.** It would not have told them what, and it would not have told them where.

**What it stops you concluding.** Where the failure entered. A team that adds the ratio and watches it has an earlier alarm and the same diagnosis problem, and the next question — *why is this ratio moving?* — is answered nine stages upstream by somebody reading what the training label was.

**And it has a further cost.** An earlier alarm invites an earlier intervention, and the available interventions all act on the output: raise the routing threshold, cap emergency volumes, review scheduler codes. **Each would move the ratio without touching the cause**, and the ratio moving back would be read as the problem being solved.

**The repair.** Add the ratio, and **also** write down what it could and could not have told you. **A monitoring improvement is worth making and is not a diagnosis**, and the distinction is the difference between noticing sooner and understanding at all.

---

## 5. "The model was validated before deployment, so what we need now is periodic revalidation on a schedule."

**The defect.** It treats deployment as a state that periodically needs renewing, when the standard this chapter draws on treats it as a repeated act.

> "Each application of the M&S restarts the M&S use/operation with an assessment of permissible uses against the needs of that specific proposed use." [@nasa2024models, p. 87]

**Each application.** Not each quarter.

**Why the difference matters.** A scheduled revalidation asks whether the thing still works. **The per-use check asks whether this use is inside the domain the thing was released for** — and those come apart precisely when a model drifts into applications nobody anticipated, which is the commonest way a validated model becomes a wrong one.

**And a schedule has a specific failure mode.** Between revalidations, the answer is assumed. A model revalidated every two years is a model whose permissible use is unexamined for twenty-three months at a time, and the uses that stray furthest are the ones added most recently.

**What it stops you concluding.** That the question is about *this* use rather than about the model in general.

**The repair.** Keep the schedule if you like — it catches decay that no individual use would reveal — **and add the per-use check**, which costs a sentence: *is what we are about to do inside what this was released for?*

**And when the answer is no, there are three options rather than two.** Refuse the use; permit it; or permit it with restrictions and **placarding** — a label attached to the thing, travelling with it, saying what it is not for. Most organisations have only the first two.

---

## What the five have in common

**Three of them are responses that a competent organisation would make**, and two of those would be approved at the meeting where they were proposed. Stronger escalation. Better monitoring. Scheduled revalidation.

**Each answers a question adjacent to the one that matters.** *Did the threshold get crossed?* rather than *is crossing it informative?* *Did anybody act?* rather than *was the rule readable?* *Are the outputs healthy?* rather than *what could the outputs not show?* *What should we watch?* rather than *what would watching tell us?* *Is it still valid?* rather than *is it valid for this?*

**And the repairs are all the same move**, which is the move this whole book has been about: **ask what the number is a number about, before asking what it says.**
