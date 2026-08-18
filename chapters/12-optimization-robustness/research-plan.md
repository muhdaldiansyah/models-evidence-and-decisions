# Chapter 12 Bounded Research Plan

Status: working control. Governs the four `research-0N-*.md` dossiers.

Bounded in the same sense as Chapters 2–11.

## Standing rules, carried forward

> **Every locator must come from reading the document directly.**
>
> **Quote only prose that survives text extraction cleanly.**
>
> **Cite the version whose pagination you can see.**

## The source position, and a deliberate contrast with Chapter 11

Chapter 11 could not source risk attitude, and `../../decisions/0018` clause 4.4 recorded that it declined to formalize rather than teach unsourced — the closest the book has come to a fifth instance of the disposition on notice.

**This chapter set out to avoid repeating that**, and three sources were obtained in full:

- **`boyd2004convex`** — Boyd and Vandenberghe, *Convex Optimization*, the authors' freely distributed PDF, carrying published pagination. Covers convexity, local versus global optima, solver handoff, and the shadow-price interpretation of constraints.
- **`lempert2003shaping`** — Lempert, Popper and Bankes, *Shaping the Next One Hundred Years*, RAND MR-1626, free from RAND, carrying printed pagination. Covers scenario ensembles, robustness, regret via Savage, and adaptive strategies.
- **`epa2010economic`** — the EPA's *Guidelines for Preparing Economic Analyses*, whose glossary supplies marginal benefit, marginal cost, and opportunity cost.

**Every item in the governed core competence is covered.** `readiness-audit.md` §1 maps them.

## Cluster R01 — Objectives, constraints, and margins

### Questions

1. What is the structure of an optimization problem, in terms the book already has?
2. What is a margin, defined authoritatively?
3. What is the stopping rule that marginal reasoning is supposed to supply?

### Sources

`epa2010economic` glossary, printed pp. xiii–xiv; `bradley2016structured` p. 8 as read for Chapter 10.

### Stop condition

Stop when marginal benefit, marginal cost, and opportunity cost are recorded verbatim, and when the efficiency condition is recorded as the source states it.

### Deliverable

`research-01-objectives-constraints-margins.md`.

## Cluster R02 — Shadow prices and convexity

### Questions

1. What does a constraint's shadow price mean?
2. Why does convexity matter, and what fails without it?
3. What does the literature say about handing a problem to a solver?

### Sources

`boyd2004convex` printed pp. 7–9, 241, 250–252.

### Stop condition

Stop when the shadow-price interpretation is recorded, when the local-versus-global consequence is recorded with the source's own warning about not knowing how far off you are, and when the recognition-is-the-hard-part claim is recorded.

**Do not proceed into duality theory, KKT conditions, or any algorithm.** The governed word is "intuition".

### Deliverable

`research-02-shadow-prices-and-convexity.md`.

## Cluster R03 — Deep uncertainty

### Questions

1. What is the contrast between optimality and robustness, stated by a source?
2. What is a scenario ensemble for?
3. What is regret, and what are its documented pathologies?

### Sources

`lempert2003shaping` printed pp. 39–40, 45–53.

### Stop condition

Stop when the optimality/robustness contrast is quoted, when robustness is defined including the many-value-systems clause, and when Savage's pathologies are recorded from the source's own footnote.

### Deliverable

`research-03-deep-uncertainty.md`.

## Cluster R04 — Adaptive plans, and the chapter's own examples

### Questions

1. What makes a strategy adaptive, and why is adaptivity a route to robustness?
2. Is there a named structure for an adaptive plan?
3. What must the anchor supply, and does every figure compute?

### Sources

`lempert2003shaping` printed pp. 57–58.

### Stop condition

Stop when the adaptivity/robustness link is recorded, when the shaping/hedging/signposts structure is recorded with its attribution, and when **every figure in the anchor has been computed and checked** — the optimum at the envelope, the divisible and indivisible shadow prices, the three futures' optima, the full regret table, and the minimax portfolio.

### Deliverable

`research-04-adaptive-plans-and-examples.md`.

## What this plan does not attempt

- **Any algorithm.** No simplex, no interior-point, no gradient methods.
- **Duality theory, Lagrange multipliers as machinery, KKT conditions.** The shadow-price *intuition* only.
- **Any formulation notation.** No objective functions written as expressions, no constraint inequalities.
- **Integer programming as a technique.** Lumpiness appears as a property of the anchor, not as a solution method.
- **Real options valuation.** `lempert2003shaping` p. 58 names it; the chapter does not teach it.
- **Robust optimization as a mathematical programme.** The decision-analytic sense only.
- **Lempert's software, the XLRM framework, or the Wonderland scenario generator.** Method-specific.
- **Dynamic programming and sequential control.** Chapter 14.
- **Feedback and system response.** Chapter 13.
- **Monitoring in operation.** Chapter 17.

## Known unobtainable or declined

- **Savage (1950)**, cited within `lempert2003shaping` p. 53 for minimax regret and its pathologies. Not obtained; used **as reported**.
- **Dewar's Assumption-Based Planning (1993, 2001)**, cited within `lempert2003shaping` p. 58 for the shaping/hedging/signposts structure. Not obtained; used **as reported**.
- **Rosenhead (1989)**, **Gupta and Rosenhead (1972)**, **Walters (1986)**, **Trigeorgis (1996)**, all cited within `lempert2003shaping`. None obtained.
- **The shadow-price-of-capital sense** in `epa2010economic` §6.2.4 was **not read**; the book uses only the optimization sense and says so.
- Silberzahn, Wasserstein and Lazar, Holland, Rubin, Keeney (1996 full text), Ellsberg, Howard, and the paginated transportability paper all remain unobtained.
