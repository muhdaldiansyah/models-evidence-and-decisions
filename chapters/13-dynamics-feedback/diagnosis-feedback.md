# Chapter 13 — Diagnosis Feedback

**Open this only after you have written all five diagnoses.**

Each statement below was said about the water case. Four contain a dynamic defect. One does not — it is dynamically correct and wrong for a different reason, and finding that one is the point of including it.

Nothing here is scored.

---

## 1. "Demand peaked on day 3, so storage bottomed out on day 3."

**The defect.** The stock is being given the shape of the flow.

A stock turns when its net flow crosses **zero**, not when the net flow reaches its largest value. On day 3 the utility was short by 28 ML — the largest deficit of the week — and a large deficit empties the reservoir faster than a small one. It does not fill it.

Storage kept falling on days 4, 5, 6, and 7, because on every one of those days the utility used more water than it made.

**The trough is day 7, four days later.**

**What it stops you concluding.** Anything about when the system was in trouble, and therefore anything about when somebody should have acted. It also produces the wrong answer to the operationally important question: the critical level was crossed on day 5, two days after the weather turned.

**The repair.** Find where the net flow crosses zero. On a table, that is the row where the sign changes; on a graph, it is where the net-rate line crosses the axis. It is never where the net rate peaks unless the two happen to coincide.

**This is the error the chapter is named for**, and it is worth knowing that it is not a beginner's error. On the simplest version of this task, the criterion that the slope of the stock is the net rate scored 0.66 among graduate students who had all studied calculus [@boothsweeney2000bathtub, p. 265].

---

## 2. "Production and demand are both back to 100 ML/day, so the reservoir has recovered."

**The defect.** Balanced flows hold a stock where they find it. They do not restore it.

From day 8 the net flow is zero, which means storage stops changing. It stops changing **at 88 ML** — 32 megalitres below the level at which the utility breaches its own service standard.

**What it stops you concluding.** That anything needs doing. This is the most dangerous statement in the list, because everything in it is true and the conclusion is false, and the report that contains it will pass every check.

**The repair.** Distinguish two questions that ordinary language runs together.

*Has the situation stopped deteriorating?* — a question about the flow.

*Is the level acceptable?* — a question about the stock.

The first can be yes while the second is no, and after a drawdown it usually is.

**And then do the arithmetic of recovery**, because it is the part nobody does. Getting from 88 back to 220 needs 132 megalitres of surplus. At 4 ML/day that is 33 days of deliberately over-producing, which nobody has ordered and which will not happen by itself.

> "Stocks and flows (accumulations) and long time delays often mean doing and undoing have fundamentally different time constants" [@sterman2006evidence, p. 507]

Seven days of ordinary summer weather emptied it. Refilling it is a month-long decision that has not been taken.

---

## 3. "The trigger is set at 150 ML. If we'd set it at 180 the rule would have worked."

**The defect.** The problem is the loop delay, and moving the trigger does not remove it.

**Retuning does help, which is what makes this the hardest of the five.** Work it through. Storage first falls below 180 on day 2. The utility sees that on day 4, and the extra water arrives on day 6 — one day before the trough rather than one day after it.

**The lowest storage rises from 88 ML to 104 ML.**

**And 104 is still below the critical level of 120.** The utility still breaches its service standard. The rule still fails to do the job it exists to do.

**The cost of the improvement is not one-sided either.** The spill rises from 30 ML to 70 ML, because a rule that fires two days earlier keeps ordering for two days longer. And a trigger only 40 megalitres below the operating target will fire in ordinary summers, in maintenance drawdowns, and whenever the verification lag catches a low reading — so the utility will over-produce routinely, and the rule will acquire a reputation for crying wolf.

**What it stops you concluding.** That the rule needs redesigning rather than retuning. This statement is the one that keeps an organisation adjusting a parameter for years.

**The repair.** Before tuning a trigger, add the delays and compare the sum with two things: how long the disturbance lasts, and how long the stock's buffer lasts at the disturbance rate. Here that is **four days** against **seven** and against roughly **four**. When the loop delay is comparable to the buffer, no stock-keyed trigger can protect the buffer, and the question becomes what else to watch.

---

## 4. "The system has stabilised."

**The defect.** The word is doing two jobs and the sentence relies on the confusion.

**In its technical sense it is true.** From day 8 the flows are balanced, nothing is changing, and if you perturbed the system slightly it would return. That is an equilibrium, and it is stable.

**In its ordinary sense it is a reassurance**, and the reassurance is unearned. The system has stabilised 32 megalitres below the critical level.

**What it stops you concluding.** That anything is wrong. And it does so while being technically correct, which is what makes it worse than a plain error — there is nothing to fact-check.

**The repair.** Never let *stable* stand alone. **Stable at what?**

> "An equilibrium point of a dynamical system represents a stationary condition for the dynamics." [@astrom2008feedback, p. 100]

A stationary condition. Not a good one, not a safe one, not a recovered one. Whether you want to be at an equilibrium is a separate question from whether you are at one, and this chapter's whole §6 exists because the two get merged.

**There is also a subtler failure available here.** A system can stay near a point without returning to it — neutral stability — which looks exactly like stability until something knocks it and the change turns out to be permanent. *Nothing went wrong* is poor evidence, because in a neutrally stable system it means the system kept the damage and stopped reacting.

---

## 5. "Every megalitre of extra production was wasted — the trough was the same either way."

**This one is dynamically correct**, and that is why it is here.

The minimum storage was 88 ML with the rule and 88 ML without it. The first extra water arrived on day 8, one day after the trough. Every claim of fact in the sentence is true.

**The defect is in the word "wasted", and it is a reasoning failure rather than a dynamic one.**

The extra production did something the sentence does not mention: **it refilled the reservoir.** Without it, storage sits at 88 ML indefinitely. With it, storage reaches capacity by day 13. Of the 202 megalitres produced, 172 went into the reservoir and 30 went over the weir.

**So the honest accounting is 30 megalitres wasted, not 202** — and the 172 were the only thing that undid a drawdown which would otherwise have been permanent.

**What it stops you concluding.** That the rule did anything worth keeping. An organisation that accepts this sentence deletes the rule, and next summer it has no rule at all.

**The repair.** Separate the two things the intervention was doing.

**Protection** — preventing the trough. On this it failed completely, and the reason is the four-day loop delay.

**Recovery** — refilling the stock afterwards. On this it worked, and nothing else would have.

They are different jobs with different timing requirements, and a rule can succeed at one while failing at the other. Judging the rule on one of them and reporting the verdict as though it covered both is the failure here.

---

## What the five have in common

**Four of them are true sentences.**

Demand did peak on day 3. Production and demand are both back to 100. The trigger is set at 150. The system has stabilised. The trough was the same either way.

**Not one of these statements would fail a fact-check**, and every one of them would lead a competent organisation to the wrong action.

That is the shape of the failure this chapter is about. Dynamic errors are rarely errors of fact. They are errors about which quantity a fact is about — the level or the rate, the equilibrium or the neighbourhood, the protection or the recovery — and the vocabulary in §§2 to 6 exists to make those distinctions sayable.

**And the repairs are all the same move.** Ask what quantity is being described, ask whether it is a stock or a flow, and then ask the question about the other one.
