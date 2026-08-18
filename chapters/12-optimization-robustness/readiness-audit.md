# Chapter 12 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 12: **Optimization, Robustness, and Adaptive Plans** — the last chapter of Part III.

**Process note.** As in Chapters 3–11, this audit was written alongside its research. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **How do we choose well at scale when the model itself is uncertain?**
- core competence: **Formulate objectives and constraints, reason marginally, understand shadow-price and convexity intuition, and use scenarios, robustness, regret, adaptive plans, and computational solver handoff appropriately.**
- target: 36 pages / 7 serious learning hours.

## 1. Readiness verdict

**Drafting-ready after adjudication, and better sourced than the previous chapter.**

**Chapter 11 ended on a near-miss.** No source was obtained for risk attitude, and `../../decisions/0018` clause 4.4 recorded that the chapter declined to formalize rather than teach unsourced. That was the closest the book has come to a fifth instance of the disposition under notice.

**Chapter 12 does not repeat it.** Three sources were obtained in full, and between them they cover every item in the governed core competence:

| Competence item | Source |
|---|---|
| objectives and constraints | `bradley2016structured` (already read), plus the anchor |
| reason marginally | `epa2010economic`, glossary p. xiii |
| shadow-price intuition | `boyd2004convex` pp. 241, 250–252 |
| convexity intuition | `boyd2004convex` pp. 7–9 |
| computational solver handoff | `boyd2004convex` p. 8 |
| scenarios | `lempert2003shaping` pp. 45–52 |
| robustness | `lempert2003shaping` pp. 52–53 |
| regret | `lempert2003shaping` p. 53, reporting Savage |
| adaptive plans | `lempert2003shaping` pp. 57–58 |

**Nothing in this chapter is taught unsourced.**

## 2. Unique-job hypothesis

> Teach readers that optimization answers *what is best given this model*, that the answer has structure worth reading — margins, constraint values, whether local improvement suffices — and that when the model itself is in doubt, *best* stops being the right target.

The reader who finishes Chapter 12 should be able to lay out a programme decision under a budget, read what the budget constraint is worth, recognise when the lumpiness of real investments breaks the marginal rule, build a regret table across futures, and choose a portfolio that is best in no future and acceptable in all of them.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `01/chapter.md` L883 | "optimization and feasibility → Chapter 12" | §§2–5 |
| `05/chapter.md` L519 | "Formal treatment of robustness — how to construct it, how to trade it against performance, what to do when conclusions do not survive — is Chapter 12, and `robustness` is reserved there" | §6 |
| `08/chapter.md` L916 | "choosing an action that performs acceptably across a range of assumptions rather than optimally under one" | §6 |
| `09` decision 0016 | choosing an action robust to source disagreement | §6 |
| `11/chapter.md` L487, L972 | "Chapter 11 optimises. Chapter 12 hedges" — and sequences of decisions | §§6–7 |
| `decisions/0006` L69 | "Chapter 12 owns formal optimization constraints, feasible regions, robustness, regret, scenarios, and adaptive plans" | the whole chapter |
| `canon` | `robustness` at `Definition status: TODO` since Chapter 1 | §6 |

**Five chapters and one book-level decision defer here**, and `robustness` has been explicitly reserved since Chapter 5.

## 4. Neighbouring-chapter boundaries

### Chapter 11 — what precedes

Chapter 11 needed a probability and got one. Its §4 showed the answer survived any defensible range around it, and named three responses if it had not: get information, hedge, or stage the decision. **It treated only the first and routed the other two here.**

### Chapter 13 — dynamics

Part IV opens after this chapter. `astrom2008feedback` is already in the bibliography for it. Chapter 12 treats plans that adapt to information; Chapter 13 treats systems that respond to action. **The line is worth stating**: an adaptive plan changes because you learn, a feedback system changes because you acted.

### Chapter 14 — sequential control

Formal sequential decision machinery — dynamic programming, control policies — is Chapter 14's. Chapter 12 treats staging at concept depth.

### Chapter 17 — monitoring

Signposts are observations that trigger a plan change. **Chapter 12 designs them; Chapter 17 operates them.**

## 5. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `constraint` | exists from Chapter 10 | specialised: the feasible-region sense |
| `feasible region` | new | the anchor; concept depth |
| `marginal benefit` / `marginal cost` | new | `epa2010economic` p. xiii |
| `shadow price` | new | `boyd2004convex` pp. 241, 252 |
| `convexity` | new | `boyd2004convex` pp. 7–9 |
| `local optimum` | new | `boyd2004convex` p. 9 |
| `scenario` | new | `lempert2003shaping` pp. 45–52 |
| `robustness` | stub, **TODO since Chapter 1**, reserved by Decision 0012 | closed here from `lempert2003shaping` pp. 52–53 |
| `regret` | new | `lempert2003shaping` p. 53, reporting Savage |
| `adaptive plan` | new | `lempert2003shaping` pp. 57–58 |
| `signpost` | new | `lempert2003shaping` p. 58, reporting Dewar |

**One collision must be named.** `shadow price` has a distinct sense in cost-benefit analysis — the shadow price of capital, a discounting concept — which appears in `epa2010economic`'s contents at §6.2.4. **This book uses only the optimization sense** and the canon entry says so. The discounting sense was not read and is not characterised.

**And one near-collision.** `scenario` in Chapter 5 meant a rival formulation; here it means a plausible future in an ensemble. Compatible, and the entry should note it.

## 6. High-risk conceptual collapses to prevent

1. **Optimization gives the right answer.** It gives the best answer *given the model*, which is the chapter's whole pivot.
2. **The optimum is the point of the exercise.** The structure around it — margins, constraint values, how flat the peak is — is usually more useful than the peak.
3. **Spend until marginal benefit equals marginal cost.** The anchor shows this failing on lumpy investments, numerically.
4. **A shadow price is a fixed number.** It is local, and with indivisible schemes it is a step function that is not even monotone.
5. **Local improvement finds the best.** True under convexity, false otherwise, and `boyd2004convex` p. 9 records that with a local method "Little information is provided about how far from (globally) optimal the local solution is."
6. **The hard part is the solver.** `boyd2004convex` p. 8: recognising the structure is the hard part.
7. **Scenarios are forecasts.** They are an ensemble to test against, not predictions.
8. **Robustness means insensitivity.** It means performing acceptably across futures *and across value systems*.
9. **Minimax regret is the right rule.** `lempert2003shaping` p. 53 n. 13 lists Savage's own pathologies, and the chapter must carry them.
10. **An adaptive plan is a vague plan.** It is a plan with named triggers.
11. **Robustness is free.** It costs performance in the future that actually arrives.
12. **More scenarios is better analysis.** Diversity, not count.

## 7. Research clusters

1. **Optimization structure** — objectives, constraints, margins.
2. **Shadow prices and convexity.**
3. **Deep uncertainty** — scenarios, robustness, regret.
4. **Adaptive plans, and the chapter's own examples.**

## 8. Candidate example constraints

The anchor scales up for the first time: from one zone to **the whole capital programme**, which is what the governed phrase "at scale" requires.

Constraints:

- Seven candidate schemes against a **£2.4m** envelope carried from Chapter 10, so the constraint binds.
- One scheme must be **phaseable**, so that §7's adaptive plan has something to stage.
- The envelope's shadow price must be **computable and badly behaved**, so §5's convexity lesson is numerical rather than asserted.
- Three futures in which the optimum genuinely differs.
- **A minimax-regret portfolio that is optimal in no future**, or the robustness section has no lesson.

**Gate 1 remains open and is now twelve chapters deep.**

## 9. Decisions likely required after research

1. **Notation.** A programme table and a regret table. Recommend nothing beyond Chapter 11's permission. Fifth notation decision.
2. **How far into optimization** — recommend intuition only, no formulations, no algorithms, per the governed word "intuition".
3. **Whether the true minimax-regret portfolio or the near-tied alternative is the chapter's headline.** Recommend reporting both, since Savage's own pathologies say the rule does not give a clean ordering.
4. **How much of Lempert's method** — recommend the four principles and none of the software.
5. **The twelfth water-case recurrence, now at programme scale.**

## 10. Drafting gate

Do not draft until:

- `../../decisions/0019` exists in proposed form;
- the eleven canon entries are written, including `robustness`, TODO since Chapter 1 and reserved by Decision 0012;
- `case-data.md` freezes the seven schemes, the three futures, and **every computed figure** — the optimum at the envelope, the divisible and indivisible shadow prices, the regret table, and the minimax portfolio;
- `spec.md` records that nothing in this chapter is taught unsourced, in contrast with Chapter 11.
