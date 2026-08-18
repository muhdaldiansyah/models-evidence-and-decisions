# Decision 0019: Chapter 12 Optimization Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §9 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 12 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**Clause 1 is the one to note.** Unlike Chapter 11, **nothing in this chapter is taught unsourced.**

Evidence base: `../chapters/12-optimization-robustness/research-01-objectives-constraints-margins.md`, `research-02-shadow-prices-and-convexity.md`, `research-03-deep-uncertainty.md`, `research-04-adaptive-plans-and-examples.md`.

## Decision

Chapter 12's organizing claim is:

> Optimization answers *what is best given this model*. Read the structure around the answer — margins, what the constraints are worth, whether local improvement suffices — and then, when the model itself is in doubt, replace *best* with *acceptable across futures*.

### 1. Every competence item is sourced

**1.1** Chapter 11 could not source risk attitude, and `0018` clause 4.4 recorded the resulting near-miss with the disposition on notice at four instances.

**1.2** **This chapter set out to avoid a repeat and succeeded.** Three sources were obtained in full — `boyd2004convex`, `lempert2003shaping`, `epa2010economic` — and every item in the governed core competence maps to one. The mapping is in `readiness-audit.md` §1.

**1.3** **The count of demonstrate-because-unsourced instances stays at four.**

### 2. Notation

**2.1** **Nothing is added.** A programme table and a regret table, both of which are ordinary tables.

**2.2** Not permitted: any formulation, any objective function or constraint written as an expression, any algorithm, any multiplier notation, any feasible-region diagram.

**2.3** The governed core competence says shadow-price and convexity **intuition**. That word is read as controlling, and it is what makes a notation-free treatment possible.

### 3. Optimization structure

**3.1** Marginal benefit, marginal cost, and opportunity cost are taken verbatim from [@epa2010economic, pp. xiii–xiv].

**3.2** The efficiency condition — spend until marginal benefit equals marginal cost — is taught, **and then shown failing on the anchor**, numerically, because the anchor's investments are indivisible.

**3.3** `constraint` is specialised from its Chapter 10 sense. Chapter 10 asked whether a constraint is real; Chapter 12 asks **what it would be worth to move one**, which Chapter 10 could not answer.

### 4. Shadow prices and convexity

**4.1** The shadow-price interpretation is taken from [@boyd2004convex, p. 241], with the locality and asymmetry cautions from pp. 251–252.

**4.2** The p. 252 sentence is **paraphrased, not quoted**, because it carries symbols, per the book's standing extraction rule.

**4.3** Convexity is taught through its **consequence**: under it, local improvement finds the global best; without it, a local answer depends on the starting point and "Little information is provided about how far from (globally) optimal the local solution is" [@boyd2004convex, p. 9].

**4.4** Solver handoff is taught from [@boyd2004convex, p. 8]: for convex problems the solving is reliable and the **recognising** is the difficulty.

**4.5** **The collision is named.** `shadow price` has a distinct sense in cost-benefit analysis — the shadow price of capital — appearing in `epa2010economic`'s contents at §6.2.4. **That section was not read.** The book uses only the optimization sense and says so in canon.

### 5. Deep uncertainty

**5.1** The pivot is quoted [@lempert2003shaping, p. 52]: traditional decision analysis "seeks the optimal strategy, that is, the one that performs best for a fixed set of assumptions about the future."

**5.2** `robustness` is closed from `Definition status: TODO`, where it has sat since Chapter 1 and where `../decisions/0012` clause 5.4 explicitly reserved it.

**5.3** The **many-value-systems clause** [@lempert2003shaping, pp. 52–53] is taught and connected to Chapter 11's single-currency limitation: robustness does not require the collapse that value-of-information machinery does.

**5.4** `scenario` is taught as a **challenge set, not a forecast**, with the diversity requirement [@lempert2003shaping, p. 52].

**5.5** Regret is taught from [@lempert2003shaping, p. 53], **with all four of Savage's own pathologies from footnote 13**. Savage (1950) was not obtained and is cited as reported.

**5.6** **Minimax regret is not presented as the right rule.** The anchor's minimax portfolio and its runner-up differ by 580 against 590, which the inputs cannot support — the first documented pathology arriving on the book's own numbers.

### 6. Adaptive plans

**6.1** The adaptivity/robustness link is taught [@lempert2003shaping, pp. 40, 57].

**6.2** The **shaping / hedging / signposts** structure is taught **as reported at** [@lempert2003shaping, p. 58]. Dewar (1993, 2001) was not obtained.

**6.3** **The staging premium is stated.** The anchor assumes building the trunk main's second stage later costs £150k more than building it now, and the manuscript presents this as an assumption rather than a measurement — because an adaptive plan whose flexibility is free is a way of avoiding a decision.

**6.4** The closing discipline is taken from [@lempert2003shaping, p. 57]: name the futures and values that selecting the strategy has "implicitly classed as unimportant". This is the book's recurring make-the-implicit-explicit move, arriving for the last time in Part III.

### 7. Vocabulary

**7.1** Introduced here: `feasible region`, `marginal benefit`, `marginal cost`, `shadow price`, `convexity`, `local optimum`, `scenario`, `regret`, `adaptive plan`, `signpost`.

**7.2** Closed here, from `Definition status: TODO` since Chapter 1 and reserved by `0012` clause 5.4: `robustness`.

**7.3** Specialised here: `constraint`.

### 8. What Chapter 12 does not do

- Teach any algorithm, formulation, or solution method.
- Teach duality, KKT conditions, or Lagrange multipliers as machinery.
- Teach integer programming; lumpiness is a property of the anchor, not a technique.
- Teach real options valuation or adaptive management, both named at most.
- Import Lempert's method, software, XLRM framework, or scenario generator.
- Present minimax regret as this book's rule.
- Treat feedback or system response — Chapter 13.
- Treat sequential control or dynamic programming — Chapter 14.
- Treat monitoring in operation — Chapter 17; the chapter designs signposts and does not operate them.
- Recommend a portfolio for the utility.

## Sources promoted

`boyd2004convex`, `lempert2003shaping`, and `epa2010economic` are new to `references.bib`, each with a source note recording exactly what was read. `bradley2016structured` is reused as verified.

## Known gaps carried forward

1. **Savage (1950), Dewar (1993, 2001)** cited within `lempert2003shaping`; neither obtained; both used as reported.
2. **`boyd2004convex` read at pp. 7–9, 241, 250–252 only** — a handful of pages of a seven-hundred-page book.
3. **`lempert2003shaping` read at pp. 39–40, 52–53, 57–58 only**; its method chapters unread.
4. **`epa2010economic` read at its glossary only**; the shadow-price-of-capital section unread and uncharacterised.
5. **The staging premium is an assumption**, not a measurement.
6. The **Chapter 12 case is the water anchor's twelfth recurrence**, and Chapter 1's Gate 1 remains open.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields. Chapter 12 closes Part III as the architecture specifies, and Chapter 13 opens Part IV.
