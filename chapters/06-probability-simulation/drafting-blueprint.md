# Chapter 6 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0013-chapter6-probability-terminology-and-notation.md`.

## 1. Drafting objective

34 pages / 7 learning hours that leave the reader able to state a probability with its conditioning information, update it by hand on two hypotheses, and accept being scored.

The chapter must **defeat** twelve named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | How Likely Is It? | 2 | 0.30 |
| 2 | A Probability Is Conditional on Something | 5 | 1.00 |
| 3 | Moving Between Positions: The Odds Update | 6 | 1.25 |
| 4 | Base Rates and Worthless Evidence | 5 | 1.00 |
| 5 | Expectation, and What It Is Not | 3 | 0.60 |
| 6 | Being Scored | 6 | 1.20 |
| 7 | Simulation: Consequences of Assumptions | 4 | 0.85 |
| 8 | Cold-Start Practice and Retrieval | 3 | 0.80 |

Roughly 360 words per page. This is the longest chapter in the book; do not rebalance without recording the reason.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **Notation: `P(A | B)` and odds as `3 : 1`. Nothing else.** No summation, integration, calculus, distributions as functions, random variables as symbols, expectation operators, or the Bayes formula with its denominator.
- Citations: `tversky1974judgment` only to p. 1125; `gneiting2007scoring` only to p. 360.
- **Every probability the chapter states carries its conditioning information.** The chapter models the discipline it teaches, and a lapse is a defect.

### Register discipline

This chapter has mathematics in it and the reader has been promised none. Two failure modes.

**Apologising for it.** Hedging about "a little arithmetic" makes it seem worse than it is. State the exception, give the reason, proceed.

**Letting it expand.** Every additional symbol makes the next one easier to justify. The permitted list is short and closed; if the manuscript wants something outside it, that material belongs to Chapter 8.

## 4. Reader-facing sequence

Per `../../decisions/0008`. No new case; the anchor is Chapter 5's open items.

Self-explanation pauses: exactly three — §2 (conditioning), §4 (the detail that moves nothing), §6 (the always-45% forecaster).

## 5. Section 1 — How Likely Is It?

**Beats.**

1. Recall Chapter 5's closing observation: nearly every open item is now a question about evidence, and Part I gave no way to answer any of them.
2. List three, one line each — the tank starting level, the pump test, Mechanism A versus B.
3. Restate Mechanism A and B in two sentences each, for a reader who has not just reread Chapter 2.
4. **Opening task, about six minutes.** How likely is Mechanism A? Write a number and the reasoning behind it. Preserve unscored.
5. Close by noting that most readers will have written a number and very few will have written what it is conditional on — which is the chapter's subject.

**Do not** introduce conditioning, priors, or notation here.

## 6. Section 2 — A Probability Is Conditional on Something

**Beats.**

1. The claim: a probability is not a property of an event but of an event **given stated information**.
2. Work it on Mechanism A. The pipe either is or is not the constraint; the number describes your evidential position, not the pipe.
3. **Defeat the one-off objection immediately**, because a reader who holds it will not engage with the rest. Collapse 12 and 1 defeated here.
4. Name the frequency / degree-of-belief distinction, say the book does not adjudicate it, and say why the conditioning framing makes both usable. One paragraph, no more.
5. **Announce the notation exception.** Five chapters without notation; here is one bar and one colon; here is why — the asymmetry between `P(A | B)` and `P(B | A)` is the chapter's central distinction and prose obscures it.
6. Introduce `P(A | B)` and read it aloud in words.
7. **Conditioning is not filtering.** Two reasons: filtering has nothing to restrict for a unique event, and it hides the direction. Collapse 3 defeated here.
8. **The inversion.** `P(A | B)` and `P(B | A)` worked on the anchor with different numbers. Collapse 4 defeated here — this is the chapter's most consequential single error.
9. **Self-explanation pause 1.** Why does "conditioning is filtering" fail for Mechanism A?
10. **Reader task.** Rewrite the §1 opening probability with its conditioning information.

## 7. Section 3 — The Odds Update

**Beats.**

1. Frame the question Chapter 5 could not answer: not *what would show it* but *how far would it move me*.
2. Odds, in two sentences. `3 : 1` means three ways for one against.
3. **The prior**, from the utility's register: **7** pump-limited, **4** main-related, in pumped zones — odds **7 : 4**, about **1.75 : 1**. State the population every time.
4. Note that this is a base rate, and forward-reference §4.
5. **The two likelihoods** [case data]: recovery greater than 8 m expected with probability **0.85** under A, **0.15** under B. **Say plainly that these are supplied**, and that where such numbers come from is the hardest step in real work.
6. **The ratio**: 0.85 ÷ 0.15 ≈ **5.7**. Read it in words — the observation is about six times more expected under A than under B.
7. **The update**: `1.75 × 5.7 ≈ 9.9 : 1`, about **91%** for A.
8. **The other branch**: no recovery gives 0.15 ÷ 0.85 ≈ **0.18**, so `1.75 × 0.18 ≈ 0.31 : 1`, i.e. **3.2 : 1** for B, about **76%**.
9. **The payoff.** One afternoon moves 2:1 to either 10:1 or 1:3. Decisive in both directions, which is what makes it worth doing — and Chapter 5 could name the test but not say this.
10. **The contrast that follows free:** a ratio near 1 moves nothing. Forward to §4 and to Chapter 11 for whether an informative observation is worth its cost. Do not develop.
11. **Conditioning is not intervening**, once. Updating belief about which mechanism operates establishes nothing about what would happen if you changed the pump. Chapter 7. One paragraph.
12. **Reader task.** Both branches by hand.

## 8. Section 4 — Base Rates and Worthless Evidence

**Beats.**

1. The question: why bother with the prior at all, when you have evidence?
2. `base rate` named, with the population requirement.
3. **The experimental result** [@tversky1974judgment, p. 1124]: engineers and lawyers, 70/30 versus 30/70, and "In a sharp violation of Bayes' rule, the subjects in the two conditions produced essentially the same probability judgments."
4. **The qualification that matters** [@tversky1974judgment, p. 1125], quoted: priors are used correctly when no other information is given, and ignored when worthless information is. Collapse 5 defeated here.
5. Draw the consequence: the trigger is being handed something that *looks* like information.
6. **The anchor instance.** The caller says it has been getting worse since the hot spell began. Compute: **0.80 ÷ 0.75 ≈ 1.07**, posterior `1.75 × 1.07 ≈ 1.87`. Essentially unchanged.
7. **Self-explanation pause 2.** The caller's report is true and relevant to the situation. Why did it move nothing?
8. The answer: it is uninformative **for discriminating between these two mechanisms**, which is a different claim from being worthless. Hot weather strains both.
9. **The other direction** [@tversky1974judgment, p. 1125]: insensitivity to sample size, and conservatism — "The underestimation of the impact of evidence has been observed repeatedly."
10. The tension: worthless evidence displaces priors, genuine evidence is under-weighted. Intuition fails in both directions, which is the argument for the arithmetic.
11. **The heuristics are useful** [@tversky1974judgment, p. 1124]. State this; do not present intuition as broken.
12. State the limit: nothing here says these tendencies can be trained away, and this book claims only that doing the arithmetic is a way of not relying on the intuition.

## 9. Section 5 — Expectation, and What It Is Not

**Beats.**

1. `expectation` as a **summary of a distribution**.
2. Work one on the anchor — expected end-of-week storage under the supplied demand spread.
3. **It is not what will happen**, and may be a value the quantity cannot take. Collapse 11 defeated here.
4. It is not the most likely outcome, and it is not the median.
5. **The Chapter 11 boundary, firmly.** *The expected value is X* to *therefore act as if X* smuggles in risk neutrality. That move is legitimate, it has a name, and it belongs to Chapter 11 where it can be made deliberately.
6. Short section. Do not expand it into decision theory.

## 10. Section 6 — Being Scored

**Beats.**

1. Frame: you have been asked to state numbers. What stops you stating convenient ones?
2. **Propriety** [@gneiting2007scoring, p. 359]: a proper rule is one where your best expected score comes from stating what you actually believe. Honesty is score-maximising by construction.
3. Why this answers the reader's real objection — not *how do I compute a score* but *why commit to a number that can be held against me*.
4. **Improper rules are a hazard** [@gneiting2007scoring, pp. 359–360]: "intuitively appealing but improper". Do not teach which are proper.
5. Reference Brier only as reported [@gneiting2007scoring, p. 360]. Say the 1950 paper was not obtained for this book.
6. **Calibration and sharpness** [@gneiting2007scoring, p. 359], both quoted. Calibration is a **joint property**; sharpness is a property of **the forecasts alone**.
7. **Reopen the Chapter 3 collision explicitly.** Chapter 3 set `calibration` aside for the instrument sense. Here is the other sense, here is why the word is now available. Once. Same handling as Chapter 5 gave `validation`.
8. **The record**, worked: the four bins, the observed column, the pattern — calibrated low, overconfident high.
9. **Self-explanation pause 3.** The overall base rate is **45%**. What would a forecaster who said 45% every time score on calibration, and would you want them?
10. **The answer, and the goal** [@gneiting2007scoring, p. 359]: maximize sharpness subject to calibration. Collapse 7 defeated here.
11. **A single forecast cannot be scored.** One outcome is consistent with any probability strictly between 0 and 1. Collapse 8 defeated here.
12. **Connect to Chapter 5:** an unscored forecast is unfalsifiable in exactly the sense Chapter 5 established. An organisation issuing one probabilistic statement per drought and never revisiting it has built something that cannot be wrong.
13. **Reader task.** Complete the observed column; name the pattern; say what it implies for the next briefing.

## 11. Section 7 — Simulation

**Beats.**

1. What a simulation is: run the calculation many times with different draws, and look at the spread.
2. **What it computes: the consequences of assumptions.** Not evidence about the world. Collapse 9 defeated here.
3. Work it on the seven-day projection with the supplied ±**0.6 ML** spread.
4. Say plainly that the spread is supplied and derived from nothing — which is the demonstration's point.
5. **More runs reduce Monte Carlo error and do nothing about model error.** Collapse 10 defeated here.
6. **Name the shape, third time.** Chapter 3: more measurements improve precision, not trueness. Chapter 4: more records shrink sampling variability, not the data-quality term. Here: more runs shrink Monte Carlo error, not model error. Give the reader the rule — when told more of something will fix a problem, ask which term it enters.
7. Tie to Chapter 5: sensitivity analysis cannot see the formulation, for the same reason.
8. **Planted-defect diagnosis task.** Five defects per `spec.md`. Feedback linked only after production.

## 12. Section 8 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 number. Compare, do not score. Name the common patterns — a number with no conditioning, or no number at all.
2. **Cold transfer.** Link exactly one assigned form.
3. **Retrieval from memory** before checking.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly.
7. Close: Chapter 7 asks what evidence could establish even in principle — and why conditioning, however well done, cannot answer it.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production. The delayed form is never linked in §8.

## 13. What the draft may not do

- Use any notation outside the permitted list.
- Cite `tversky1974judgment` beyond p. 1125 or `gneiting2007scoring` beyond p. 360.
- Cite Brier (1950) directly.
- Use `likelihood` as a technical term.
- Present base-rate neglect as universal, or the heuristics as defects.
- Claim anything about debiasing.
- Teach expected utility, risk attitude, or value of information.
- Teach estimation, intervals, or uncertainty quantification.
- Claim conditioning establishes what would happen under intervention.
- Restate the five-row pattern table from Chapter 5.
- Adopt `calibration` silently.
- State a probability without its conditioning information.
- Present synthetic case values as typical, standard, or recommended.
