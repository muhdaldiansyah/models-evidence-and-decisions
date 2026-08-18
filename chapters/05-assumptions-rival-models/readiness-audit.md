# Chapter 5 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 5: **Assumptions, Adequacy, and Rival Models**

**Process note.** As in Chapters 3 and 4, this audit was written alongside its research rather than strictly before it. Findings taken from sources are marked.

Current architecture from `README.md` and `spec.md`:

- central question: **How could this formulation fail its purpose, and what would show it?**
- core competence: **Criticize models using assumption records, dimensional reasoning, limiting and extreme-condition checks, Fermi estimation and bounding, rival models, structural uncertainty, and predicted failure modes.**
- target: 27 pages / 5 serious learning hours.

## 1. Readiness verdict

**Drafting-ready after adjudication**, and with the strongest inherited position of any chapter so far.

Three verified credibility sources were **deliberately reserved for this chapter** when they were first read for Chapter 1. Each source note says so explicitly:

- `asme2025credibility`: "defer formal verification, validation, and credibility machinery to Chapter 5";
- `fda2023credibility`: "the full framework belongs in Chapter 5";
- `nrc2012reliability`: supports the use-dependent principle but "does not define the book's complete adequacy vocabulary".

Chapter 4 also hands this chapter its opening move: every failure found in Chapters 1–4 had a specific observation that would have revealed it, and in every case nobody had made it.

## 2. Unique-job hypothesis

> Turn four chapters of accumulated failure modes into a method: predict, specifically, how this formulation would fail its purpose, and name the observation that would show it.

Chapter 5 closes Part I. Chapters 1–4 each taught a way an analysis can go wrong. None taught how to go looking.

A reader who finishes Chapter 5 should be able to hand someone a short written list — *here is what would have to be true, here is what would show it is not, and here is which of those I can actually check* — for an analysis they have just built.

## 3. Neighbouring-chapter boundaries

### Chapters 1–4 — the material being criticized

Chapter 5 does not reteach any of them. It criticizes the artifact they jointly produced. The anchor should therefore be the accumulated water-utility analysis itself, which is the natural culmination of Part I.

### Chapter 6 — probability

Chapter 5 uses bounding and order-of-magnitude reasoning without probability. No distributions, no intervals, no formal uncertainty.

### Chapter 7 — identification

Rival models here are **criticism tools**, not competing causal hypotheses to be identified between. Chapter 2's Mechanism A and Mechanism B remain unresolved and Chapter 5 may say so; it may not teach how to resolve them.

### Chapter 8 — estimation and uncertainty quantification

**The hardest boundary after Chapter 15's.** Sensitivity analysis, uncertainty propagation, and formal UQ are Chapter 8. Chapter 5 owns *structural* criticism — whether the formulation is right — not quantification of uncertainty within a formulation.

Proposed test: Chapter 5 asks *could this be the wrong model?*; Chapter 8 asks *given this model, how uncertain is the answer?*

### Chapter 11 — value of information

Chapter 5 asks what observation would show a failure. Chapter 11 asks whether that observation is worth acquiring. The line is between **naming** the discriminating observation and **valuing** it.

### Chapter 12 — robustness

Chapter 5 may note that a conclusion surviving across representations is more trustworthy (`levins1966strategy`). Formal robustness, regret, and adaptive planning are Chapter 12.

### Chapter 17 — monitoring and revision

Chapter 5 predicts failure modes before deployment. Chapter 17 detects them after. Chapter 5 may say what would be worth watching; it may not teach monitoring design.

## 4. Terminology readiness

Terms requiring adjudication:

- verification and validation (and their collision with Chapter 3's `validation`, already flagged);
- credibility;
- adequacy (already registered from Chapter 1; Chapter 5 was always its development);
- assumption record;
- model risk;
- structural uncertainty (already registered? — check; distinct from parameter uncertainty);
- rival model;
- extreme-condition check; limiting case;
- dimensional check;
- order-of-magnitude estimate / bounding;
- failure mode.

`adequacy` and `context of use` already exist in the registry with Chapter 5 named as their development site.

## 5. High-risk conceptual collapses to prevent

1. **Criticism is skepticism.** Listing worries is not criticism. Criticism produces specific predicted failures, each paired with what would show it.
2. **Naming an assumption handles it.** An assumption record is a starting point, not a discharge.
3. **Verification is validation.** *(Sourced.)* `asme2025credibility` distinguishes numerical verification, model validation, uncertainty quantification, and broader credibility assessment.
4. **Fitting the data validates the model.** Fit is one kind of evidence and a weak one against structural error.
5. **Adequate means accurate.** *(Sourced.)* `fda2023credibility` §VI.D distinguishes quantifiable model accuracy from the broader judgment of whether total credibility evidence is sufficient for the context of use given model risk.
6. **More checks mean more confidence.** Checks that could not have failed add nothing — the Chapter 3 lesson recurring.
7. **Rival models are options to choose between.** They are instruments of criticism; leaving both alive is a legitimate outcome.
8. **"All models are wrong" means no model can be judged.** *(Sourced.)* `sterman2002models` p. 505 pairs the maxim with taking responsibility, not with abdication.
9. **Structural uncertainty is parameter uncertainty.** Being unsure of a number is not being unsure of the form.
10. **A predicted failure mode is a prevented one.** Prediction is the cheap half.
11. **Sensitivity analysis is criticism.** It varies inputs within a formulation and cannot see the formulation.
12. **Criticism has a fixed standard.** *(Sourced.)* How much is enough depends on model risk (`fda2023credibility` §VI.D).

## 6. Research clusters

- **R01 — Adequacy, credibility, and how much criticism is enough.** The reserved credibility standards, finally taken up.
- **R02 — How a formulation fails, and what would show it.** Strong inference; assumption records; the discriminating observation.
- **R03 — Cheap checks: dimensions, limits, extremes, and bounds.** Largely taught by demonstration; sourcing status to be established honestly.
- **R04 — Examples, exercises, and the Chapter 8 boundary.**

## 7. Candidate example constraints

The anchor should be **the reader's own accumulated analysis**, not a new case. Part I's whole point is that four chapters produced one artifact; Chapter 5's job is to criticize it.

A good demonstration should include at least one check that **catches something the previous four chapters missed**, using a technique none of them taught. An order-of-magnitude check on a figure the reader has trusted since Chapter 4 is the obvious candidate.

## 8. Decisions likely required after research

1. Reader-facing treatment of verification versus validation, given Chapter 3 already declined to use `validation`.
2. Whether `model risk` is controlled vocabulary.
3. How much of the credibility-framework apparatus is taught versus signposted.
4. Whether `structural uncertainty` is distinguished from parameter uncertainty here or deferred to Chapter 8.
5. How the strong-inference schema is adapted for cases where no crucial experiment exists.
6. The anchor demonstration and the transfer forms.

## 9. Drafting gate

Chapter 5 becomes drafting-ready when R01–R04 have dossiers, terminology is adjudicated, the Chapter 8 boundary is stated in applicable form, and `spec.md` no longer contains load-bearing TODOs.
