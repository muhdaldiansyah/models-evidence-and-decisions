# Decision 0012: Chapter 5 Criticism Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `research-plan.md` §10 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 5 entries in `canon/terminology.md` are built on this record and inherit its provisional status. Clauses are numbered so that rejecting one identifies the downstream text it invalidates.

Evidence base: `research-01-adequacy-and-credibility.md`, `research-02-failure-and-exclusion.md`, `research-03-cheap-checks.md`, `research-04-examples-exercises.md`.

## Decision

Chapter 5 closes Part I by turning four chapters of accumulated failure modes into a method. Its organizing claim is:

> Criticism is not doubt. It is producing specific predicted failures, each paired with the observation that would show it — and how much of it is enough depends on what happens if you are wrong.

### 1. Adequacy, and how much is enough

**1.1** Adequacy is developed here, as Chapter 1's registry entry always anticipated. A model is not adequate in itself: it is adequate **for a stated use, at a stated accuracy, for a stated quantity**.

**1.2** **Adequacy is not accuracy.** `fda2023credibility` §VI.D p. 33 distinguishes quantifiable model accuracy from the broader judgment of whether total credibility evidence is sufficient for the context of use, given model risk. `nrc2012reliability` Summary p. 3 treats validation as meaningful for specified quantities of interest and in relation to the accuracy required for an intended use.

**1.3** **How much criticism is enough is governed by model risk** — what happens if the model is wrong. `fda2023credibility` §VI.D p. 33; `nrc2012reliability` ch. 6 §§6.1–6.2 pp. 86–87.

**1.4** `model risk` is **not** registered as controlled vocabulary. The idea is carried as *what happens if you are wrong*, which is plainer and avoids importing a regulated-industry construct.

**1.5** The five-chapter pattern — adequacy relative to use, content relative to purpose, validity relative to interpretation, trustworthiness relative to the quantity, criticism relative to the stakes — is stated **once**, and is labelled as **the book's own observation**. Each row is independently established; the pattern is not.

### 2. Verification, validation, credibility

**2.1** The reader-facing pair:

> **Verification:** did I do the thing right?
> **Validation:** did I do the right thing?

Sourced from `asme2025credibility` slides 5–7, which distinguishes numerical verification, model validation, uncertainty quantification, and broader credibility assessment.

**2.2** Chapter 5 **does** use `validation`, in the computational-model sense. Chapter 3 declined it (`decisions/0010` clause 2.5) and named the collision once. **Chapter 5 must reopen that collision explicitly** — stating that this is the other sense, and why the word is now available — rather than adopting it silently.

**2.3** `credibility` is **signposted, not taught**. It is framework-specific to regulated computational simulation.

**2.4** The credibility frameworks' apparatus — credibility factors, evidence tables, submission requirements — is **not** taught. What transfers is the structure of the judgment, not the machinery, and the manuscript must say so.

### 3. The criticism method

**3.1** Chapter 5 teaches, in reader-facing form:

1. Write down the alternatives — what else could be true?
2. For each, name the observation that would exclude it.
3. Make the observation, if you can.
4. **If you cannot, say so, and say what your conclusion is resting on.**

**3.2** Steps 1–3 are `platt1964strong` p. 347's strong-inference schema, cited. **Step 4 is the book's own addition** and must be labelled as such per `canon/pedagogy.md`. Platt assumes crucial experiments are available; most of this book's cases cannot run one.

**3.3** The chapter quotes rather than paraphrases: "Any conclusion that is not an exclusion is insecure and must be rechecked" [`platt1964strong` p. 347].

**3.4** The reader's artifact follows the template recorded at `platt1964strong` p. 348 from Jacob and Monod: *our conclusion might be invalid if (i), (ii), or (iii); here is what would eliminate each.*

**3.5** `platt1964strong` is presented as an **influential methodological argument that has been debated**, not as an established result. The debating literature was **not read** and must not be characterized. Its disciplinary polemic is not imported.

**3.6** Chapter 5 explicitly permits **leaving rivals alive**. Mechanism A and Mechanism B from Chapter 2 remain unresolved after three chapters, and the chapter says so. Naming an unobtainable discriminating observation is a result, not a failure.

### 4. Cheap checks

**4.1** Four are taught: **dimensional check, limiting case, extreme-condition check, order-of-magnitude bound.**

**4.2** **None is sourced. All four are taught by demonstration and cite nothing.** No source in this bibliography defines or licenses any of them, and none was obtained.

**4.3** This is the **third** chapter to reach that disposition (`decisions/0009` clause 6.3, `decisions/0011` clause 4.4). `research-03-cheap-checks.md` §2 records it as a pattern and recommends escalating it to a standing book-level question. **If a fourth chapter reaches for the disposition, research should be reopened rather than precedent invoked.**

**4.4** The chapter states plainly that a one-minute limiting check would have flagged Chapter 4's central finding — that a quantity labelled *Hillcrest demand* stays positive when Hillcrest uses nothing. This is mildly deflating about Part I and is the chapter's strongest argument for doing cheap checks first.

**4.5** It also states what the cheap checks **cannot** do: they flagged the problem; they did not produce the explanation. Chapter 4's expensive work did.

### 5. Rival models and structural uncertainty

**5.1** Rival models are **instruments of criticism**, not options to choose between.

**5.2** `structural uncertainty` is registered, and distinguished from parameter uncertainty: being unsure of a number is not being unsure of the form.

**5.3** A collision is named: `structural identifiability` is already registered with a Chapter 14 home. Different concept, shared word.

**5.4** Building a differently-simplified representation and checking whether the conclusion survives is permitted as a criticism technique, citing `levins1966strategy` p. 423 on robust theorems. Formal robustness, regret, and adaptive planning remain Chapter 12, where `robustness` is registered.

**5.5** "All models are wrong" is presented with its other half. `sterman2002models` p. 505 pairs recognising a model's limits with expanding boundaries and taking responsibility — not with abandoning judgment.

### 6. The Chapter 8 boundary

**6.1** The reader-facing test:

> **Chapter 5:** could this be the wrong model?
> **Chapter 8:** given this model, how uncertain is the answer?

**6.2** **Sensitivity analysis is not criticism**, and this is given to the reader as a placement trap. It varies inputs inside a formulation and therefore cannot see the formulation.

**6.3** Not taught: uncertainty quantification, uncertainty propagation, sensitivity methods, formal bounding.

**6.4** Adjacent boundaries stated once each: Chapter 7 owns which rival is true; Chapter 11 owns whether a discriminating observation is worth acquiring; Chapter 17 owns detecting failures after deployment.

### 7. Vocabulary

**7.1** Controlled: `verification`, `validation` (computational-model sense), `assumption record`, `structural uncertainty`, `rival model`, `failure mode`.

**7.2** Ordinary careful language: `credibility`, `model risk`, `dimensional check`, `limiting case`, `extreme-condition check`, `order-of-magnitude estimate`, `bound`.

**7.3** `adequacy` is **not** re-registered. Its Chapter 1 entry names Chapter 5 as its development site; Chapter 5 develops it in prose and the entry is updated rather than duplicated.

**7.4** No notation. No formulas beyond arithmetic.

### 8. What Chapter 5 does not do

- Not representation, measurement, or provenance — it criticizes what those chapters produced.
- Not probability, distributions, or intervals (Chapter 6).
- Not estimands or identification (Chapter 7).
- Not uncertainty quantification or sensitivity methods (Chapter 8).
- Not transportability (Chapter 9).
- Not value of information (Chapter 11).
- Not formal robustness, regret, or adaptive plans (Chapter 12).
- Not monitoring, drift detection, or revision triggers (Chapter 17).

## Sources promoted

New and verified: `platt1964strong` (pp. 347–348 read).

Taken up as reserved: `fda2023credibility`, `asme2025credibility`, `nrc2012reliability` — all three carry Chapter 1 source notes explicitly deferring their framework to this chapter.

Reused: `levins1966strategy` p. 423, `sterman2002models` p. 505.

## Known gaps carried forward

1. **All four cheap checks are unsourced** and taught by demonstration. Third chapter to do so; see clause 4.3.
2. **`platt1964strong` read to p. 348 only.** Pages 349–353 may not be cited.
3. **The debating literature on strong inference was not read** and must not be characterized.
4. **The no-experiment adaptation (step 4) is the book's own** and has no source.
5. Inspected extents of the three credibility sources are narrow — `asme2025credibility` slides 5–7, `fda2023credibility` pp. 8–9, 13, 33, `nrc2012reliability` Summary pp. 1–4 and ch. 6 pp. 86–87 — and may not be exceeded.

## No architecture change

Title, central question, core competence, 27-page and 5-hour targets are unchanged and remain governed by `README.md` and `decisions/0001`.
