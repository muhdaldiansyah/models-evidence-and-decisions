# Chapter 11 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0018-chapter11-decision-terminology-and-boundary.md`.

## 1. Drafting objective

33 pages / 7 learning hours that leave the reader able to lay a decision out, choose defensibly, find where the answer turns, and decline a study whose result could not change the act.

The chapter must **defeat** thirteen named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | Seven Alternatives and No Way to Choose | 2 | 0.35 |
| 2 | Laying the Decision Out | 5 | 1.05 |
| 3 | Expected Value, and Whether to Use It | 6 | 1.30 |
| 4 | Does the Answer Turn on Anything? | 5 | 1.05 |
| 5 | What Would It Be Worth to Know? | 7 | 1.50 |
| 6 | When the Analysis Is Not Worth It | 5 | 1.05 |
| 7 | Cold-Start Practice and Retrieval | 3 | 0.70 |

Roughly 360 words per page — about **11,900 words**.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- **No formula anywhere.** Every figure is arithmetic on the table.
- A decision table; one inline text tree in §5 only.
- Rhodes et al. and Møller and Fiedler cited **as reported at** `colyvan2016voi`.
- Ellsberg not named.
- **The negative result is not softened.**

### Register discipline

Three failure modes specific to this chapter.

**Sounding like decision analysis.** The reader was promised no specialist training. Every idea lands on the anchor's numbers and no formula appears.

**Sounding triumphant about the negative result.** The £2,300 is not a gotcha. Chapter 6's work was correct, the test genuinely is informative, and the finding is that informative and valuable are different — which is interesting, not clever.

**Sounding like the machinery settles things.** §6 exists because it does not. The single-currency step, the monetisation, and the narrowing are all value judgments the arithmetic hides.

## 4. Reader-facing sequence

Per `../../decisions/0008`. No new case; the anchor is Chapter 10's alternatives with Chapter 6's probabilities.

Self-explanation pauses: exactly three — §3 (which act would a risk-averse committee choose), §4 (where does the answer turn), §5 (what is the test worth).

## 5. Section 1 — Seven Alternatives and No Way to Choose

**Beats.**

1. Where the book stands: seven alternatives, three objectives, four conflicts, and no way to choose among them.
2. **Opening task, about six minutes.** Which would you choose, and how? Preserve unscored.
3. Name what this chapter is: the last three steps of the six-step process [@bradley2016structured, p. 8].
4. **Announce the second question early.** *Which act is defensible* and *would more evidence change it* are the governed central question's two halves, and the second is the one that closes the book's longest thread.
5. Say plainly that the answer to the second will be no, and that the machinery for showing it is one afternoon's arithmetic.

## 6. Section 2 — Laying the Decision Out

**Beats.**

1. Acts, states, consequences.
2. **The states are Chapter 2's mechanisms.** No new uncertainty is invented, and the chapter says so.
3. **The narrowing**, with the criterion stated and the four dropped alternatives named.
4. Say that the narrowing is a choice, and that Chapter 10 spent five pages establishing why.
5. **The payoff table.**
6. **The monetisation is a value judgment**, and the single-currency limitation is quoted [@colyvan2016voi, p. 305].
7. Note that no source read for this book teaches the layout, and that the presentation is the book's own of standard material.
8. Note the iteration warning: a table that produces an uncomfortable answer sends you back to Chapter 10, not forward.
9. **Reader task.** Build a table for a decision of your own.

## 7. Section 3 — Expected Value, and Whether to Use It

**Beats.**

1. Compute all three expected costs at the prior: **173.6**, **319.1**, **216.0**.
2. Best act: **A**.
3. **Now the instruction from canon, discharged.** Chapter 6 refused to slide from an expected value to a decision and told this chapter to make the move deliberately. Make it: using expected value is a choice, and it is called risk neutrality.
4. **Self-explanation pause 1.** Act C costs 216 whatever happens. Which act would a risk-averse committee choose, and what does it cost them?
5. The answer: C, at **£42,400** more in expectation, and the spread removed entirely. Neither choice is an error.
6. **Risk attitude, named and demonstrated.** Say plainly that no source was obtained for a formal treatment, that the chapter therefore shows what the table displays and stops, and that utility functions and certainty equivalents are depth curriculum.
7. **The positive case for expected value**: it is the only rule that uses all the numbers and all the probabilities, and it is what makes §5 computable.
8. Note that a source applying it records "decision theory recommends indifference" at equal expected monetary value [@colyvan2016voi, p. 303] — the recommendation follows from the rule.
9. **Decision quality**, briefly: a good decision and a good outcome are different things, and the second does not grade the first.
10. **Reader task.** Compute the three; then say what using them assumes.

## 8. Section 4 — Does the Answer Turn on Anything?

**Beats.**

1. The prior of 0.636 came from eleven investigations over eighteen years and three network configurations. **It is not a precise number.**
2. `ambiguity`: not knowing the probability exactly is different from knowing it.
3. **The source's two-interval example** [@colyvan2016voi, p. 302], both cases, quoted.
4. The point: what matters is **whether the interval straddles the value at which the best act changes**.
5. **Self-explanation pause 2.** At what value of p does the utility's best act change?
6. Work it: A beats C when `p > 34/120 = ` **0.283**.
7. The prior is **0.636**. Even a generous range around it stays above 0.283.
8. **So the decision is insensitive to the prior across any plausible range** — which is Colyvan's first coin example on the anchor.
9. **Sensitivity analysis, for the third time in this book.** Chapter 5 named and refused it; Chapter 8 used it as a model check; here it asks the decision question. One technique, three jobs.
10. And what it is not: varying every input by a fixed percentage answers a question nobody asked.
11. **Reader task.** Find the critical value for your own table.

## 9. Section 5 — What Would It Be Worth to Know?

**Beats.**

1. Frame with the source's own opening assumption [@colyvan2016voi, p. 302], quoted — and note that the assumption "lies behind, and motivates" a great deal of work, including ten chapters of this book.
2. **The broken toe** [@colyvan2016voi, p. 303], quoted, with its qualification.
3. **The ninth relativity instance**: value of information is relative to a decision.
4. **Self-explanation pause 3.** Before computing: what do you think the pump test is worth?
5. **The inline tree**, the only one in the book: test-then-act against act-now.
6. The branch arithmetic. Recovery → A at **141.0**; no recovery → C at **216.0**.
7. `0.596 × 141.0 + 0.404 × 216.0 = ` **171.3**, against **173.6** without.
8. **The test is worth £2,300, and costs £8,000.**
9. Sit with it: this is the observation Chapter 2 named, Chapter 5 confirmed obtainable, and Chapter 6 called decisive in both directions. **All of that was correct.**
10. Explain why: the act changes on only one branch, and by only £5,700 — which is §4's finding from the other direction.
11. **The ceiling** [@colyvan2016voi, p. 303]. Compute EVPI: **£12,400**.
12. **Teach it as a screening rule**: one line of arithmetic disposes of every study proposal before any of them is costed.
13. **Reader task.** Compute both; then price the cheapest study that could pay for itself.

## 10. Section 6 — When the Analysis Is Not Worth It

**Beats.**

1. The governed core competence asks for this, so the chapter turns on itself.
2. **The analysis costs something** [@colyvan2016voi, p. 308 n. 16], quoted.
3. Which is why the **ceiling** is the version to run first: it is arithmetic on a table you already have.
4. **The four limitations** [@colyvan2016voi, pp. 305–306], each worked on the anchor: framing; the single currency; budgets not fungible; value arriving later.
5. **Three kinds of information gathering** [@colyvan2016voi, p. 306], quoted, with the warning about category (3).
6. Say where most organisational collection sits, and that the machinery cannot price it and should not be used to bless it.
7. **And the honest defence of category (1)**, from the same page.
8. Carry Chapter 10's scope limit: simple decisions need no formal method [@bradley2016structured, p. 7].
9. Close on what the book's evidence arc has established: not that evidence is worthless, but that **what matters is prior to which evidence is worth having** — which is Chapter 10's finding arriving with arithmetic behind it.
10. **Planted-defect diagnosis task.** Five defects per `spec.md`. Feedback linked only after production.

## 11. Section 7 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 answer. Compare, do not score.
2. **Cold transfer.** Both forms listed, one assigned.
3. **Retrieval from memory** — the procedure, ten steps.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly.
7. **What this chapter did not give you.**
8. Close: Chapter 12 asks what to do when you decline to state the probabilities at all.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production.

## 12. What the draft may not do

- Write any formula.
- Teach utility functions, certainty equivalents, or risk premiums.
- Name Ellsberg or describe those experiments.
- Cite Rhodes et al. or Møller and Fiedler directly.
- Enter game theory.
- Present the monetisation as a measurement.
- Present expected value as the right rule.
- Present risk aversion as an error.
- Soften the negative result.
- Suggest that a low value of information means the mechanism question is uninteresting.
- Recommend an act for the utility.
- Present synthetic case values as typical, standard, or recommended.
