# Research 03 — Cheap Checks: Dimensions, Limits, Extremes, and Bounds

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision.

Cluster R03 of `research-plan.md` §6. Research conducted 2026-08-18.

## 1. Q1 and Q3 — Sourcing status, stated bluntly

Chapter 5's governed competence names four cheap checks: **dimensional reasoning**, **limiting and extreme-condition checks**, **Fermi estimation**, and **bounding**.

**None of the four is sourced by anything currently in this bibliography.**

Nothing in `platt1964strong`, the three credibility standards, `levins1966strategy`, `sterman2002models`, or `frigg2025models` defines or licenses any of them. Sources exist for all four in the wider literature — dimensional analysis has a formal foundation, system-dynamics validation has a named extreme-condition test, order-of-magnitude estimation has a substantial pedagogical literature — and **none of it was obtained in this pass.**

So the disposition for all four is: **teach by demonstration, cite nothing.**

## 2. A pattern the author should look at

This is now the third chapter to reach that disposition:

| Chapter | Taught by demonstration, uncited | Recorded in |
|---|---|---|
| 2 | representational aggregation | `decisions/0009` clause 6.3 |
| 4 | censoring versus missingness | `decisions/0011` clause 4.4 |
| 5 | all four cheap checks | this dossier |

Three chapters is a pattern rather than a coincidence, and it is worth the author's attention for two reasons.

**The benign reading**, which R03 believes is largely correct: these are *craft practices*. They are taught in apprenticeship and worked examples rather than defined in citable literature, and a demonstration the reader can verify arithmetically is stronger evidence than a citation they cannot check. This book's own discipline already accepts that — a self-evidencing demonstration needs no source.

**The reading that should worry the author:** the disposition is also what happens when research stops early. It is available whenever a source is hard to obtain, and nothing in the process distinguishes "this is craft" from "I did not look hard enough".

**Recommendation.** Keep the disposition for Chapter 5, and record it as a standing question for the book rather than a per-chapter judgment. If a fourth chapter reaches for it, that is the point to reopen research rather than to invoke precedent.

## 3. Q2 — What each check catches that the others do not

Worked against the book's own accumulated analysis, which is what makes them demonstrable.

### Dimensional check — do the units survive the arithmetic?

Chapter 2 computed `0.6 ÷ 0.9 = 0.67`. Megalitres divided by megalitres-per-day gives days, so 0.67 days, about sixteen hours.

The check is trivial and catches a specific, common error: a quotient reported without units, where the reader supplies the wrong ones. It also catches the case where two quantities that look comparable are not — megalitres of storage and megalitres per day are different kinds of thing, and only their ratio is meaningful.

Chapter 3 already exploited this deliberately by choosing metres of head, which made every pressure calculation a subtraction.

### Limiting case — what does the model say at zero?

Set Hillcrest's customer consumption to zero.

The residual — town total minus two metered zones — **does not go to zero.** Leakage, unbilled operational use, and metering error elsewhere remain.

That is a decisive finding, and notice how it arrives: **the limiting case catches Chapter 4's entire result without any provenance work at all.** A quantity labelled *Hillcrest demand* that stays positive when Hillcrest uses nothing is not a demand.

This is the strongest argument in the chapter for doing cheap checks first. Chapter 4 needed interviews, institutional history, and five stages of analysis. One limiting case would have raised the alarm in a minute.

### Extreme-condition check — what does the model do when pushed?

Set demand to zero and let inflow run.

Chapter 1's and Chapter 2's storage representation says storage grows without bound. There is no overflow, no spill, no tank ceiling in the model — the Hillcrest tank has a stated capacity of **1.2 ML** and nothing in the arithmetic prevents exceeding it.

Real tanks spill. The model has no spill term, which was harmless for the question asked and would be wrong for any question involving refill.

### Order-of-magnitude check — is the number the right size?

The chapter's centrepiece, worked in R04 §2.

## 4. Q4 — Which are worth the chapter's space

All four, and in that order, because the order is roughly cheapest-first and the chapter's argument is that cheapness is the point.

The four together take a page to state and would have caught two of the four chapters' findings.

**The uncomfortable implication should be stated to the reader:** the most expensive analytical work in Part I — Chapter 4's provenance investigation — reached a conclusion that a one-minute limiting check would have flagged. That is not an argument against Chapter 4. It is an argument for doing the cheap checks *first*, so that the expensive work is spent on what survives them.

## 5. Cautions — claims the manuscript must NOT make

1. Do not cite any source for any of the four checks. None was obtained.
2. Do not present the four as an exhaustive or established set. They are four useful checks, not a framework.
3. Do not teach dimensional-analysis theory, asymptotics, or formal bounding.
4. Do not imply that passing all four means a model is adequate. They are cheap filters, not sufficiency.
5. Do not use these checks to relitigate Chapters 2 and 4. The point is that cheap checks would have flagged what expensive work found, not that the expensive work was unnecessary — it produced the explanation, which the checks cannot.
6. Do not present the limiting-case finding as a criticism of the earlier chapters' reasoning. The chapters reasoned correctly from what they had.

## 6. Verdict on the stop condition

`research-plan.md` §6 requires each check's sourcing status settled and the demonstrate-versus-cite disposition explicit.

**Met.** All four: unsourced, taught by demonstration, cite nothing. The pattern across three chapters is recorded in §2 as a standing question for the author.

## 7. Unresolved author decisions

1. Accept the demonstrate-don't-cite disposition for all four, or reopen research for at least dimensional analysis?
2. Is the three-chapter pattern in §2 escalated to a book-level question, or left in this dossier?
3. Is the "cheap checks would have caught Chapter 4's finding" point made to the reader? It is the chapter's most persuasive argument and it is mildly deflating about Part I.
4. Are the checks given in a fixed order, risking checklist behaviour?
