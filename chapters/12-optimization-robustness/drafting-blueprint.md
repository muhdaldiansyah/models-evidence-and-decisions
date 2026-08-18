# Chapter 12 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0019-chapter12-optimization-terminology-and-boundary.md`.

## 1. Drafting objective

36 pages / 7 learning hours that leave the reader able to lay out a programme decision under a binding budget, read what the constraint is worth, notice when the marginal rule breaks, and choose a portfolio that is best in no future and acceptable in all of them.

The chapter must **defeat** thirteen named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | Fifteen Zones, Not One | 2 | 0.35 |
| 2 | Objectives and Constraints at Scale | 5 | 0.95 |
| 3 | Reasoning at the Margin | 5 | 0.95 |
| 4 | What a Constraint Is Worth | 5 | 0.95 |
| 5 | When Local Improvement Finds the Best | 5 | 1.00 |
| 6 | When the Model Itself Is Uncertain | 7 | 1.40 |
| 7 | Adaptive Plans | 4 | 0.80 |
| 8 | Cold-Start Practice and Retrieval | 3 | 0.60 |

Roughly 360 words per page — about **13,000 words**.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- **No formulation, algorithm, or diagram.** Two tables.
- The `boyd2004convex` p. 252 sentence is **paraphrased**, not quoted.
- Savage and Dewar cited **as reported at** `lempert2003shaping`.
- Minimax regret is **not** the right rule; its pathologies are carried.
- The staging premium is stated as an assumption.

### Register discipline

Three failure modes specific to this chapter.

**Sounding like an operations-research course.** The reader was promised no specialist training. Every idea lands on the seven schemes and no expression appears.

**Sounding as though robustness supersedes optimization.** It does not. Optimization answers a real question well; robustness answers a different one when the first question's premise fails. §6 must say this rather than implying a progression.

**Sounding as though the chapter has a recommendation.** It has a table with 580 and 590 in it, and the honest reading is that the two are indistinguishable.

## 4. Reader-facing sequence

Per `../../decisions/0008`. No new case; the anchor is the capital programme.

Self-explanation pauses: exactly three — §3 (fund down the ranking and see what happens), §5 (why did an extra £50k buy nothing), §6 (which portfolio would you defend to the board).

## 5. Section 1 — Fifteen Zones, Not One

**Beats.**

1. Where the book stands: eleven chapters on one zone, and the utility has fifteen.
2. Seven schemes, £5,080k of ambition, £2,400k of envelope.
3. **Opening task, about six minutes.** How would you spend it? Preserve unscored.
4. Name the two halves of the governed question: *choose well at scale*, and *when the model itself is uncertain*.
5. Say plainly that the second half replaces the standard used in Chapter 11, and that this is a change of criterion rather than a better method.

## 6. Section 2 — Objectives and Constraints at Scale

**Beats.**

1. What changes at scale: the object of choice is a **combination**, not an alternative.
2. The seven schemes, with costs. Total against envelope.
3. **`feasible region`** at concept depth: the combinations that fit.
4. **Chapter 10's discipline applies first.** The envelope is a convention with an author and a precedent for exceptions — so the feasible region is drawn around a constraint that could move, and §4 prices the move.
5. The benefits table under the central forecast, and where those numbers came from — a monetisation, as in Chapter 11, with the same caveat.
6. Note that the process placement is unchanged [@bradley2016structured, p. 8]: this is the same steps applied to a programme.
7. **Reader task.** Which combinations fit, and how many are there?

## 7. Section 3 — Reasoning at the Margin

**Beats.**

1. The natural move: rank by benefit per pound.
2. The three definitions, quoted [@epa2010economic, pp. xiii–xiv].
3. **Opportunity cost "need not be assessed in monetary terms"** — and note that this is cheaper than Chapter 11's machinery, which required a single currency.
4. The ratio table. A at **2.375** dominates everything.
5. The classical stopping rule, quoted from the source's efficiency condition.
6. **Self-explanation pause 1.** Fund down the ranking until the money runs out. What do you get, and what is left?
7. Work it: the ranking funds **A, B, F1, C** — £1,940 spent, benefit **915**, and **£460k left over**. The true optimum is **A + B + F2** at **985**, spending £2,320.
8. **The ranking is not the rule.** It misses by **70**, and it misses because F2 has a worse ratio than F1 yet belongs in the answer — ratios ignore that the envelope must be filled with whole schemes.
9. **And note where the ranking landed.** A + B + C + F1 reappears in §6 as the near-tied robust portfolio. The ratio rule found a defensible answer for the wrong reason, which is worth saying because it is how such rules survive.
10. State plainly where marginal reasoning does work: continuous quantities, divisible spend, smooth returns.
11. **Reader task.** Rank; fund down the list; compare with the optimum.

## 8. Section 4 — What a Constraint Is Worth

**Beats.**

1. Chapter 10 asked whether the envelope was real and found it soft. **This section asks what moving it is worth**, which Chapter 10 could not.
2. `shadow price`, from [@boyd2004convex, p. 241], quoted.
3. The paraphrased sensitivity statement [@boyd2004convex, p. 252], marked as paraphrase.
4. **The divisible case first**, because it is the clean one: if schemes could be bought fractionally, the shadow price is C's ratio, **0.339 per £k**, single-valued and meaningful.
5. **Then the real case.** The table of envelope moves: 0.060, 0.000, 0.490, 0.840.
6. **An extra £50k is worth nothing** at one point on the curve.
7. Locality and asymmetry, from [@boyd2004convex, p. 251].
8. **The practical upshot**: never quote a shadow price without the size of the move it refers to.
9. Name the collision: `shadow price` has a distinct discounting sense in cost-benefit analysis, which this book does not use and did not read.
10. **Reader task.** Price an extra £200k; then an extra £50k; explain the difference.

## 9. Section 5 — When Local Improvement Finds the Best

**Beats.**

1. Why §4's curve behaved badly: the schemes are lumpy.
2. `convexity` through its consequence [@boyd2004convex, pp. 8–9] — the book does not teach recognition, and the source says recognition "can be difficult".
3. **Under convexity**: local improvement reaches the global best, reliable solvers exist, and "if you formulate a practical problem as a convex optimization problem, then you have solved the original problem" [@boyd2004convex, p. 8].
4. **Without it**: "there are no effective methods for solving the general nonlinear programming problem" [@boyd2004convex, p. 9].
5. `local optimum`, and the two consequences a reader can act on: the answer depends on where you started, and **"Little information is provided about how far from (globally) optimal the local solution is"** [@boyd2004convex, p. 9].
6. **Self-explanation pause 2.** Why did an extra £50k buy nothing, and why is the marginal value higher at £2.9m than at £2.4m?
7. The answer: under convexity the marginal value of a budget cannot increase with the budget. It does here. **That is the diagnostic**, and it is visible in a table without any mathematics.
8. **Solver handoff** [@boyd2004convex, p. 8]: the solving is a solved problem, the recognising is not.
9. What to hand over and what to keep: hand over the search, keep the formulation, the constraints, and the interpretation.
10. **Reader task.** Find the lumpiness in a decision of your own.

## 10. Section 6 — When the Model Itself Is Uncertain

**Beats.**

1. Everything so far assumed the benefit table. Where did it come from?
2. The pivot, quoted [@lempert2003shaping, p. 52]: optimality is "best for a fixed set of assumptions about the future".
3. The alternative framing [@lempert2003shaping, p. 39]: acting "in the absence of any reliable predictions".
4. **`scenario`** as a challenge set, with the **diversity requirement** [@lempert2003shaping, p. 52]. Not forecasts, and no probabilities attached.
5. The three futures and their benefit tables.
6. The optimum in each future. Note that two agree and one does not.
7. **`regret`**, defined; the regret table built.
8. **Self-explanation pause 3.** Which portfolio would you defend to a board?
9. **The robust choice**: A + C + E + F1 at max regret 580, **optimal in no future**.
10. **`robustness` defined** [@lempert2003shaping, p. 52], with the **many-value-systems clause** [@lempert2003shaping, pp. 52–53] — and the observation that this repairs what Chapter 11 had to break.
11. **Savage's four pathologies** [@lempert2003shaping, p. 53, n. 13], quoted, with the first landing immediately: 580 against 590 is not a difference the inputs support.
12. **Robustness is not free.** A + C + E + F1 gives up 85 in the central forecast and 580 in the high-demand future against what could have been had.
13. **Reader task.** Build the table; find the robust choice; say what it gives up.

## 11. Section 7 — Adaptive Plans

**Beats.**

1. The unspent £460k under A + B + C + F1 is not waste.
2. Adaptivity as the route to robustness [@lempert2003shaping, pp. 40, 57], quoted — and **"in specific ways"** underlined.
3. **Shaping, hedging, signposts** [@lempert2003shaping, p. 58], as reported, with Dewar named and recorded as unobtained.
4. Work the anchor: B shapes, A and C hedge, **F1 instead of F2** is the option.
5. **The signposts**: peak-week demand against the Chapter 1 forecast, and heat events per summer — both already collected, neither with a threshold.
6. **A review date is not a signpost.** The threshold has to be named in advance.
7. **The staging premium**: £1,150k later against £1,000k now, a **£150k** cost of the option — stated as an assumption.
8. The honest limit [@lempert2003shaping, p. 57]: an ideal strategy is rare, and this is "an exercise in juggling difficult trade-offs".
9. **The closing discipline** [@lempert2003shaping, p. 57]: name the futures and values the choice has "implicitly classed as unimportant". Do this for the anchor.
10. **Planted-defect diagnosis task.** Five defects per `spec.md`. Feedback linked only after production.

## 12. Section 8 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 answer. Compare, do not score.
2. **Cold transfer.** Both forms listed, one assigned.
3. **Retrieval from memory** — the procedure, ten steps.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly.
7. **What this chapter did not give you.**
8. Close Part III: three chapters on choosing. Chapter 13 opens Part IV and asks what happens when the system responds to what you did.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use.

## 13. What the draft may not do

- State any formulation, algorithm, or method.
- Teach duality, multipliers, or integer programming.
- Quote the symbol-bearing `boyd2004convex` p. 252 sentence.
- Cite Savage or Dewar directly.
- Present minimax regret as the right rule, or 580 as beating 590.
- Present robustness as superseding optimization.
- Present the staging premium as measured.
- Import Lempert's method or software.
- Treat feedback, sequential control, or monitoring in operation.
- Recommend a portfolio.
- Present synthetic case values as typical, standard, or recommended.
