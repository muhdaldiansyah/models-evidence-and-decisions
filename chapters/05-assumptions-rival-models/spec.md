---
chapter: 5
part: 1
title: "Assumptions, Adequacy, and Rival Models"
status: specified
pages_target: 27
hours_target: 5
---

# Chapter 5: Assumptions, Adequacy, and Rival Models

> **Provisional.** Built on `../../decisions/0012-chapter5-criticism-terminology-and-boundary.md`, which is **PROPOSED and not author-adjudicated**. The five Chapter 5 entries in `../../canon/terminology.md`, and the updated `adequacy` and `validation` entries, are provisional for the same reason. Title, central question, core competence, and the page and hour targets are **not** provisional — they are governed by `README.md` and `../../decisions/0001`.

## Central question

How could this formulation fail its purpose, and what would show it?

## Core competence

Criticize models using assumption records, dimensional reasoning, limiting and extreme-condition checks, Fermi estimation and bounding, rival models, structural uncertainty, and predicted failure modes.

## Role in the book

Chapter 5 closes Part I. Chapters 1–4 each taught a way an analysis can go wrong. None taught how to go looking.

Chapter 4 ended by naming what they had in common: every failure found in Part I had a specific observation that would have revealed it, and in every case nobody had made it.

Chapter 5's unique job:

> Turn four chapters of accumulated failure modes into a method: predict, specifically, how this formulation would fail its purpose, and name the observation that would show it.

The chapter must accomplish five things.

1. Establish what governs how much criticism is enough — and that it is not a fixed standard.
2. Give the reader four checks cheap enough to run on anything, and show them catching things on the book's own case.
3. Supply a method for organising criticism around alternatives and exclusions, sourced.
4. Handle honestly the common case where the discriminating observation cannot be obtained.
5. Prevent the chapter's characteristic failure, which is a list of generic worries presented as criticism.

**Chapter 5 introduces no new case.** Every other Part I chapter added something; this one turns on what is already there. That is what makes it the closing chapter rather than a fifth topic.

The five-chapter pattern — adequacy relative to use, content relative to purpose, validity relative to interpretation, trustworthiness relative to the quantity, criticism relative to the stakes — is **the book's own observation** and must be labelled as such per `../../canon/pedagogy.md`. Each row is independently established; the pattern is not.

## Hard prerequisites

- Chapters 1–4 in full. The chapter criticizes the analysis they jointly produced and is unreadable without it.
- Arithmetic, division, and willingness to estimate roughly.
- No probability, no statistics, no notation.
- No domain expertise. All case facts are supplied.

## Soft dependencies / spiral links

| Spiral element | Treatment in Chapter 5 | Later development |
|---|---|---|
| Adequacy | Developed from Chapter 1's placeholder into its full form | Chapters 11, 12, 16–17 |
| Rival models | Instruments of criticism; leaving both alive is legitimate | Chapters 7, 12 |
| Structural uncertainty | Recognized and named, never quantified | Chapter 8 |
| The discriminating observation | Named; not valued | Chapter 11 |
| Robust conclusions across representations | Noted as a criticism technique | Chapter 12 |
| Predicted failure modes | Predicted before deployment | Chapter 17 |

## Established concepts to cover

### Adequacy and sufficiency

- Adequacy is not accuracy: `fda2023credibility` §VI.D p. 33 distinguishes quantifiable model accuracy from whether total credibility evidence is sufficient for the context of use, **given model risk**.
- Validation is meaningful "for specified quantities of interest" and relative to "the accuracy required for an intended use" (`nrc2012reliability` Summary p. 3).
- The nature and allocation of VVUQ activity is connected to how results will be used in an eventual application and decision (`nrc2012reliability` ch. 6 §§6.1–6.2, pp. 86–87).

### Verification and validation

- `asme2025credibility` slides 5–7 distinguishes numerical verification, model validation, uncertainty quantification, and broader credibility assessment.
- `fda2023credibility` §IV pp. 8–9 defines context of use, credibility, and applicability; p. 13 compares with ASME V&V 40.

### The criticism method

- Strong inference: "1) Devising alternative hypotheses; 2) Devising a crucial experiment … each of which will, as nearly as possible, exclude one or more of the hypotheses; 3) Carrying out the experiment so as to get a clean result" (`platt1964strong` p. 347).
- "Any conclusion that is not an exclusion is insecure and must be rechecked" (`platt1964strong` p. 347).
- The tree metaphor and the "conditional inductive tree" attributed to Bacon (`platt1964strong` p. 347).
- Why it does not happen: "in between, we do busywork. We become 'method-oriented' rather than 'problem-oriented'" (`platt1964strong` p. 348).
- The artifact template, from Jacob and Monod: "Our conclusions … might be invalid if … (i) … (ii) … or (iii)…. We shall describe experiments which eliminate these alternatives" (`platt1964strong` p. 348).

### Rival models and limits

- Robust theorems across differently simplified models; "our truth is the intersection of independent lies" (`levins1966strategy` p. 423).
- "All models are wrong" paired with expanding boundaries and taking responsibility, not with abdication (`sterman2002models` p. 505).

## Terminology to introduce or stabilize

Five terms registered provisionally under the Chapter 5 block; `adequacy` and `validation` updated in place.

| Term | Treatment | Distinction or caution |
|---|---|---|
| verification | Required | *Did I do the thing right?* Paired with validation, never merged |
| validation | Required, computational-model sense | Chapter 3 declined it; **Chapter 5 must reopen the collision explicitly** |
| adequacy | Developed, not re-registered | For a stated use, at a stated accuracy, for a stated quantity; **not accuracy** |
| assumption record | Required | Naming an assumption does not handle it; each entry needs what would show it false |
| rival model | Required | An instrument of criticism; leaving both alive is legitimate |
| structural uncertainty | Recognition depth | Not parameter uncertainty; **collides with `structural identifiability`** (Ch 14) |
| failure mode | Required | A specific predicted failure paired with what would show it; predicting is not preventing |

**Ordinary careful language:** credibility, model risk, dimensional check, limiting case, extreme-condition check, order-of-magnitude estimate, bound.

**No notation. No formulas beyond arithmetic.**

## Interfaces with other chapters

| Chapter | Interface established here | Boundary Chapter 5 must respect |
|---|---|---|
| Ch. 1–4 | Criticizes the artifact they produced | Reteaches none of them |
| Ch. 6 | Bounding without probability | No distributions, intervals, or probabilistic language |
| Ch. 7 | Rivals may be left alive | Do not teach identification or how to resolve them |
| Ch. 8 | **Could this be the wrong model?** versus **given this model, how uncertain?** | Do not teach UQ, propagation, or sensitivity methods |
| Ch. 9 | — | Do not teach transportability |
| Ch. 11 | The discriminating observation is **named** | Do not teach whether it is **worth acquiring** |
| Ch. 12 | A conclusion surviving across representations is more trustworthy | Do not teach robustness formalism, regret, or adaptive plans |
| Ch. 17 | Failure modes predicted before deployment | Do not teach monitoring design or drift detection |

## Scope boundary

### Core

- State what a model is adequate *for* — use, accuracy, quantity — and refuse the unqualified form.
- Explain what governs how much criticism is enough, and act on it.
- Distinguish verification from validation and say which a given check addresses.
- Run a dimensional check and say what it caught or ruled out.
- Run a limiting case and an extreme-condition check on a model and state what the model implies that cannot be right.
- Produce an order-of-magnitude estimate and compare it against a figure in use.
- Write an assumption record whose entries each carry what would show the assumption false.
- Generate at least two rival explanations for a finding.
- For each rival, name the observation that would exclude it.
- State plainly when the discriminating observation cannot be obtained, and what the conclusion therefore rests on.
- Distinguish structural uncertainty from uncertainty about a number.
- Recognize that sensitivity analysis cannot see the formulation.
- Judge whether a criticism could have changed the recommendation, and discard it if not.
- Criticize a completed analysis produced by someone else.

### Deferred to later chapters

- Probability, distributions, intervals, calibration: Chapter 6.
- Estimands, identifiability, causal identification, resolving between rivals: Chapter 7.
- Uncertainty quantification, propagation, sensitivity methods, measurement-error models: Chapter 8.
- External validity, generalizability, transportability: Chapter 9.
- Values, objectives, trade-offs: Chapter 10.
- Value of information, whether an observation is worth acquiring: Chapter 11.
- Robustness formalism, regret, scenarios, adaptive plans: Chapter 12.
- Monitoring design, drift and tampering detection, revision triggers: Chapter 17.

### Deferred to depth curriculum

- Verification and validation procedures, credibility factors, and regulatory submission frameworks.
- Formal uncertainty quantification and model-form uncertainty methods.
- Dimensional-analysis theory and the Buckingham Pi theorem.
- Asymptotic and limiting analysis.
- Falsificationism, severe-testing frameworks, and the debate over strong inference.
- Model selection, model averaging, and information criteria.
- Failure modes and effects analysis and reliability engineering practice.

## Section architecture

No new case. The anchor is the accumulated water-utility analysis from Chapters 1–4.

| Section | Working title | Pages | Learning hours | Primary output |
|---|---|---:|---:|---|
| 1 | What Would Have Shown It | 2 | 0.25 | An unscaffolded list of what would have to be true for Part I's conclusion to hold |
| 2 | Adequate for What, at What Risk | 4 | 0.75 | A statement of what the analysis is adequate for, and what governs how much checking it deserves |
| 3 | Four Cheap Checks | 6 | 1.10 | Four checks run on the book's own analysis, with what each caught |
| 4 | Alternatives and Exclusions | 5 | 0.95 | An assumption record whose entries each carry a discriminating observation |
| 5 | When You Cannot Find Out | 4 | 0.70 | A statement of what a conclusion rests on when the discriminating observation is unavailable |
| 6 | Criticizing Part I | 3 | 0.65 | A written criticism of the accumulated analysis, with one item capable of reversing it |
| 7 | Cold-Start Practice and Retrieval | 3 | 0.60 | An independently produced criticism of an unfamiliar completed analysis |
| **Total** |  | **27** | **5.00** |  |

### Drafting constraints

- No new case and no new domain. Familiarity is the point.
- At least half of active learning time is prediction, production, explanation, diagnosis, or retrieval, per `../../decisions/0008`.
- Three self-explanation pauses: at what makes a check worth doing (§3), at the nursery (§3), at the no-experiment case (§5).
- **Every criticism the chapter models must name what would settle it.** A worry with no discriminating observation attached is the failure the chapter exists to prevent.
- The `validation` collision from Chapter 3 is reopened explicitly, once.
- No notation.

## Examples / recurring cases

### The anchor: Part I's own analysis

The chapter criticizes what Chapters 1–4 produced.

**The centrepiece is an order-of-magnitude check.** Two numbers the reader already holds from two different chapters — **340** connected Hillcrest properties (Ch 3) and **0.62 ML/day** Hillcrest consumption (Ch 4) — give `620,000 ÷ 340 = 1,824 L per property per day`, roughly **five times** a plausible household figure of about 375 L/day.

The resolution is supplied: a **commercial horticultural nursery** drawing about **0.40 ML/day**, leaving `0.22 ML ÷ 339 ≈ 649 L/property/day`, which is plausible for large-plot hillside properties in a heatwave.

**The payoff is not the catch.** The nursery is one customer, on a commercial contract, whose irrigation is schedulable — an alternative that four chapters of analysis never produced, because every representation aggregated Hillcrest into one demand number. It closes the loop on Chapter 2's finding that a representation can only contain the alternatives it can express.

**Other checks demonstrated on the same analysis:**

- **Limiting case:** set Hillcrest consumption to zero and the residual stays positive — which flags Chapter 4's entire finding in one minute, without provenance work.
- **Extreme condition:** set demand to zero and storage grows without bound; the model has no spill term, and the Hillcrest tank has a stated **1.2 ML** capacity.
- **Dimensional:** ML ÷ ML/day gives days; a quotient reported without units invites the reader to supply the wrong ones.

**New synthetic facts required** — the nursery, its draw, and household bounding figures — extending four prior case-data files. All of it **inherits Chapter 1's open SME gate, now four chapters deep.**

### Deliberately not used

Any new domain. Any case requiring the reader to learn something before criticizing it.

## Exercise architecture

1. **Opening attempt (§1).** What would have to be true for Part I's conclusion about Hillcrest to hold? Preserved unscored.
2. **Adequate for what (§2).** State what the analysis is adequate for and what would change the answer.
3. **Run the four checks (§3).** The reader produces the arithmetic, including the 1,824 figure.
4. **Assumption record (§4).** Each entry paired with what would show it false.
5. **Rivals and exclusions (§4).** Two rival explanations, each with a discriminating observation.
6. **Planted-defect diagnosis (§6).** Five defects.
7. **Chapter 8 placement (§6).** Four supplied situations, one of which is a sensitivity analysis offered as criticism.
8. **Cold transfer (§7).** One assigned parallel form.
9. **Retrieval and delayed retest (§7).**

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| A review of six generic caveats with no discriminating observation | criticism = skepticism |
| "We listed our assumptions, so they are handled" | naming an assumption handles it |
| "The model reproduces last year's data well, so it is validated" | fit validates the model |
| A sensitivity analysis offered as the criticism section | sensitivity analysis = criticism |
| "All models are wrong, so this objection cannot be settled" | the maxim as abdication |

### Rubric dimensions

1. Adequacy stated for a use, an accuracy, and a quantity.
2. Verification and validation distinguished correctly.
3. A cheap check run and its result stated, including what it ruled out.
4. An order-of-magnitude comparison produced with arithmetic.
5. Assumption record entries each carry what would show them false.
6. At least two rival explanations generated.
7. A discriminating observation named for each rival, or its unavailability stated.
8. At least one criticism capable of reversing the recommendation.

Dimension 8 is discriminating. Criticism that could not change the decision is decoration.

## Transfer target

> Given a completed analysis and its recommendation, produce a written criticism that names at least one order-of-magnitude or dimensional problem, one behaviour the formulation implies at a limit or extreme that cannot be right, one load-bearing assumption the analysis does not state, and one rival explanation that would reverse the recommendation — and for each, name the observation that would settle it, or say that none is available.

### Parallel forms

The task shape differs deliberately from Chapters 1–4: the reader is a **reviewer, not an analyst**. A four-chapter analysis cannot be built in forty minutes, so one is supplied.

- **Form A — closing one of four recycling depots** (physical/operational).
- **Form B — moving clinic appointment reminders from post to SMS** (institutional).

Each supplies a completed, plausible, competently written one-page analysis containing exactly four defects — one order-of-magnitude error, one limit or extreme failure, one unstated load-bearing assumption, and one unconsidered rival explanation **of the reversing kind**.

Every prior transfer and contrast domain is excluded.

Chapter 5 must not claim durable far transfer.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| Adequacy is not accuracy; sufficiency depends on model risk | `fda2023credibility` §VI.D p. 33 |
| Validation is per quantity of interest and per required accuracy | `nrc2012reliability` Summary p. 3 |
| VVUQ activity is allocated by how results will be used | `nrc2012reliability` ch. 6 §§6.1–6.2 pp. 86–87 |
| Verification, validation, UQ, and credibility are distinct | `asme2025credibility` slides 5–7 |
| Context of use, credibility, applicability defined | `fda2023credibility` §IV pp. 8–9, p. 13 |
| The three-step method; the tree | `platt1964strong` p. 347 |
| "Any conclusion that is not an exclusion is insecure" | `platt1964strong` p. 347 |
| Why criticism does not happen — busywork, method-oriented | `platt1964strong` p. 348 |
| The Jacob–Monod artifact template | `platt1964strong` p. 348 |
| Robust theorems across differently simplified models | `levins1966strategy` p. 423 |
| "All models are wrong" paired with responsibility | `sterman2002models` p. 505 |

### Known gaps constraining the manuscript

1. **All four cheap checks are unsourced** and taught by demonstration. **Third chapter to reach this disposition**; `research-03-cheap-checks.md` §2 recommends escalating it to a book-level question.
2. **`platt1964strong` read to p. 348 only.** No citation beyond it.
3. **The debating literature on strong inference was not read** and must not be characterized.
4. **Step 4 of the method — say what your conclusion rests on when you cannot find out — is the book's own** and has no source.
5. Inspected extents of the three credibility sources are narrow and may not be exceeded.

### Evidence needed before prose is stable

- SME review of the nursery extension, coupled to Chapter 1's open Gate 1.
- SME or ethical check on Form B, which concerns clinic non-attendance.
- Timed reader pilot against the 5-hour target.

## Failure modes this chapter should prevent

1. Criticism is skepticism.
2. Naming an assumption handles it.
3. Verification is validation.
4. Fitting the data validates the model.
5. Adequate means accurate.
6. More checks mean more confidence.
7. Rival models are options to choose between.
8. "All models are wrong" means no model can be judged.
9. Structural uncertainty is parameter uncertainty.
10. A predicted failure mode is a prevented one.
11. Sensitivity analysis is criticism.
12. Criticism has a fixed standard.

## Open questions

### Before drafting

1. Does the author accept Decision 0012 as proposed, and if not, which clauses change?
2. Accept the fifth recurrence of the water case — here as the object of criticism rather than a case to build?
3. Does the chapter admit that a one-minute limiting check would have flagged Chapter 4's finding?
4. Is the five-chapter pattern table shown to the reader, or left for them to assemble?
5. Is the reviewer-not-analyst transfer shape accepted?
6. Should the nursery have been planted earlier, or is discovering it here the point?

### Before declaring Chapter 5 verified or frozen

7. Is the demonstrate-don't-cite disposition escalated to a book-level question, given this is its third use?
8. Has `platt1964strong` been read past p. 348?
9. Has the nursery extension passed SME review?
10. Has Form B had an ethical check?
11. Does the 27-page / 5-hour budget survive a timed reader pilot?
