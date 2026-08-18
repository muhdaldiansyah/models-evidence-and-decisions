# Research 01 — Adequacy, Credibility, and How Much Criticism Is Enough

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision. Written under the no-write boundary in `research-plan.md` §11.

Cluster R01 of `research-plan.md` §4. Research conducted 2026-08-18.

Sources: `fda2023credibility`, `asme2025credibility`, `nrc2012reliability` — all three verified during Chapter 1 research and **explicitly reserved for this chapter** in their own source notes.

## 1. Q1 — Adequacy is not accuracy

The cleanest statement is in the FDA guidance, and it is worth reading carefully because the distinction is easy to nod at and hard to hold.

`fda2023credibility` §VI.D, "Adequacy Assessment", printed p. 33, distinguishes **quantifiable model accuracy** from the broader judgment of whether the **total credibility evidence is sufficient** for the context of use, **given model risk**.

Three things are separated there:

1. how accurate the model is — a quantity;
2. whether the evidence assembled is sufficient — a judgment;
3. what governs that judgment — the context of use and the risk.

A model can be accurate and inadequate. It can also be less accurate and adequate, if the stakes are low and the evidence is proportionate.

`nrc2012reliability` says the same from the other side. Its Summary, printed p. 3, treats validation as meaningful **for specified quantities of interest** and in relation to the **accuracy required for an intended use**.

Note that phrase: *the accuracy required for an intended use*. Accuracy has no threshold of its own. The threshold arrives with the use.

## 2. Q2 — What governs how much evidence a model needs

**Model risk.**

`fda2023credibility` §VI.D p. 33 makes sufficiency conditional on the context of use **given model risk**. `nrc2012reliability` ch. 6, §§6.1–6.2, printed pp. 86–87, connects the nature and allocation of VVUQ activity to how the results will be used in an eventual application and decision.

So the answer to "how much criticism is enough?" is not a standard. It is a function of what happens if the model is wrong.

### The pattern, for the fifth time

This is the same structural move the book has now met in every chapter of Part I, and Chapter 5 completes the set.

| Chapter | The thing that is not self-standing | What it is relative to |
|---|---|---|
| 1 | whether an answer is adequate | the stated intended use |
| 2 | what belongs in a representation | the purpose |
| 3 | whether a measurement is valid | the interpretation placed on the scores |
| 4 | whether a dataset is trustworthy | the quantity being estimated |
| 5 | **how much criticism is enough** | **what happens if you are wrong** |

Each is independently established in its own literature. That they share a shape is the book's own observation, and by Chapter 5 the reader has seen it five times and should be able to state it themselves.

## 3. Q3 — Verification, validation, credibility

`asme2025credibility`, slides 5–7, distinguishes four things that ordinary usage merges:

- **numerical verification** — whether the computation does what the model specifies;
- **model validation** — whether the model represents reality adequately for the purpose;
- **uncertainty quantification**;
- **broader credibility assessment** — the overall judgment.

The same material relates context of use to whether assumptions, accuracy, uncertainty, VVUQ evidence, and validation conditions are sufficient or relevant for intended-use requirements and risks.

`fda2023credibility` §IV, printed pp. 8–9, defines context of use, credibility, and applicability; printed p. 13 compares the FDA framework with ASME V&V 40 and records terminology provenance and cautions.

### The reader-facing pair

At core depth the reader needs the first two, and needs them as a contrast:

> **Verification:** did I do the thing right?
> **Validation:** did I do the right thing?

Both matter and they fail differently. A perfectly verified computation of the wrong model is wrong. This is Chapter 5's cheapest and most durable distinction.

### A terminology collision that must be handled

Chapter 3 **declined to use `validation`** because measurement validation and computational-model validation are different practices sharing a word (`decisions/0010` clause 2.5), and named the collision once.

Chapter 5 is where the computational-model sense properly belongs, so Chapter 5 **may** use the word — but it must reopen the collision explicitly rather than quietly adopting it, or a reader who took Chapter 3's instruction seriously will be confused about why the rule changed.

## 4. Q4 — What this book may take from regulated-simulation frameworks

**Less than the frameworks contain, and it must say so.**

All three sources are written for computational modelling and simulation in regulated engineering, aerospace, and medical-device settings. Their machinery — credibility factors, evidence tables, submission requirements — presupposes an institutional context most readers do not work in.

What transfers is the **structure of the judgment**: adequacy is not accuracy; sufficiency is relative to use and risk; verification is not validation.

What does not transfer is the apparatus.

The existing source notes already impose this discipline. `fda2023credibility`: "FDA's `adequacy assessment` is a framework-specific construct." `nrc2012reliability`: it "does not define the book's complete adequacy vocabulary."

## 5. Q5 — Connection to the earlier chapters

Beyond the shared shape in §2, one specific inheritance is worth naming.

`nrc2012reliability` p. 3 says validation is meaningful for **specified quantities of interest**. That is Chapter 4's finding in different vocabulary: `davern2013nonresponse` established that bias is "an estimate level measure" attaching to a quantity rather than to a dataset.

Two literatures, arriving independently at the same warning: **the unqualified question is malformed.** Not "is this model valid?" but "valid for which quantity, to what accuracy, for what use, at what risk?"

## 6. Cautions — claims the manuscript must NOT make

1. Do not present any of the three frameworks as governing analysis generally. All three are for regulated computational simulation.
2. Do not teach credibility factors, evidence tables, or submission requirements.
3. Do not present FDA's `adequacy assessment` as a universal definition of adequacy. Its own source note forbids this.
4. Do not say a model is "validated" without saying for what quantity, to what accuracy, and for what use.
5. Do not adopt `validation` silently after Chapter 3 declined it. Reopen the collision explicitly.
6. Do not teach uncertainty quantification. Chapter 8.
7. Do not claim the five-chapter pattern in §2 is established. Each row is; the pattern is the book's own.
8. Do not cite `asme2025credibility` beyond slides 5–7, `fda2023credibility` beyond pp. 8–9, 13, 33, or `nrc2012reliability` beyond Summary pp. 1–4 and ch. 6 pp. 86–87. Those are the inspected extents.

## 7. Verdict on the stop condition

`research-plan.md` §4 requires a sourced reader-facing account of adequacy and of what governs sufficiency.

**Met.** Proposed statements:

> A model is not adequate or inadequate in itself. It is adequate for a stated use, at a stated accuracy, for a stated quantity — and whether the evidence you have assembled is enough depends on what happens if you are wrong.

> Verification asks whether you did the thing right. Validation asks whether you did the right thing.

## 8. Unresolved author decisions

1. Does Chapter 5 use `validation`, reopening the Chapter 3 collision — or keep avoiding it?
2. Is `model risk` controlled vocabulary, or is the idea carried as "what happens if you are wrong"?
3. Is `credibility` introduced, given it is framework-specific?
4. Is the five-chapter pattern table shown to the reader, or left for them to assemble?
5. How much of `context of use` is taken up, given Chapter 1 previewed it as optional and field-specific?

Decision 4 is the interesting one. Showing the table is satisfying and risks the reader treating a hard-won habit as a slogan. Chapter 3 already stated a three-row version once; repeating it with five rows may be one time too many.
