# Decision 0010: Chapter 3 Measurement Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `research-plan.md` §10 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 3 entries in `canon/terminology.md` are built on this record and inherit its provisional status. Clauses are numbered so that rejecting one identifies the downstream text it invalidates.

Evidence base: `research-01-constructs-operationalization.md`, `research-02-validity.md`, `research-03-reliability-error-precision.md`, `research-04-examples-exercises.md`.

## Decision

Chapter 3 teaches the reader to interrogate the link between a quantity in a representation and the number attached to it. Its organizing claim is:

> A measurement is valid when the scores it produces can meaningfully be interpreted as the construct you set out to measure — so validity belongs to the interpretation, not to the instrument.

This is **established content**, traceable to `adcock2001validity` p. 531, not pedagogical synthesis.

### 1. The ladder

**1.1** Chapter 3 teaches a four-rung ladder, reader-facing:

> **construct → working definition → measure → score**

**1.2** The rungs correspond to `adcock2001validity` p. 530's four levels. The source's own terms — *background concept*, *systematized concept*, *indicator*, *scores for cases* — are named **once**, attributed, and then not used as working vocabulary.

**1.3** Rationale for departing from the source's names. `construct`, `measure`, and `proxy` are **already registered** in `canon/terminology.md` as TODO entries marked "Introduced in: Chapter 3"; filling them is completion, not collision. *Systematized concept* is a political-science coinage; `working definition` is plain English carrying the same content and correctly signalling revisability. No new umbrella term is coined.

**1.4** The three moves are named: **conceptualization** (construct → working definition), **operationalization** (working definition → measure), and **scoring** (measure → score). Only `operationalization` is controlled vocabulary; the chapter's governed title names it.

**1.5** The ladder must be taught as **revisable upward**, not as a one-pass procedure. `adcock2001validity` p. 530 shows three upward tasks; p. 532 quotes Kaplan's paradox, resolved "by a process of approximation".

**1.6** Choosing a measure does **not** define the construct. Interpretations of scores are falsifiable claims requiring evidence (`adcock2001validity` p. 532). A stipulation cannot be falsified; a claim can. The historical operationist position may be mentioned as having existed; it may **not** be characterized, since it was not researched.

### 2. Validity

**2.1** Validity is a property of the **interpretation of scores in relation to a construct, for a use** — never of an instrument. `adcock2001validity` p. 531: the focus of validation "is on the conjunction of these components".

**2.2** The reader is taught **one validity and several kinds of evidence for it**, never a taxonomy of validities. `adcock2001validity` p. 530 reports 37 adjectives attached to the word and resolves them as "types of evidence for validity", not "multiple independent types of validity".

**2.3** "Is this measure valid?" is taught as a **malformed question**. The answerable form is "are these scores interpretable as this construct, for this use?"

**2.4** **Contextual specificity** is taught: a measure valid in one context may be invalid in another (`adcock2001validity` p. 530). It is **not** extended into transportability, which is Chapter 9.

**2.5** `validation` is **not** used as reader-facing Chapter 3 vocabulary. It collides with computational-model validation (`asme2025credibility`, `fda2023credibility`), which Chapter 5 owns. Chapter 3 says *assessing the evidence for an interpretation*. The collision is named once, explicitly, so a reader arriving at Chapter 5 does not merge them.

**2.6** The three-chapter structural echo — adequacy relative to use (Ch 1), content relative to purpose (Ch 2), validity relative to interpretation (Ch 3) — is made **explicit**, once, at the end of the validity section. Each instance is independently established; the observation that they share a shape is the book's own and is labelled as such.

### 3. Reliability, error, and the metrology trio

**3.1** Controlled: `precision`, `trueness`, `measurement error`, `systematic error`, `random error`, `reliability`, `accuracy`.

**3.2** `accuracy` is taught as the **combination** of trueness and precision, not as a third independent property. VIM §2.13 Note 2 forbids using it for either alone while stating it relates to both.

**3.3** The chapter states plainly that **accuracy and trueness are not numbers**. VIM §2.13 Note 1 and §2.14 are explicit. Precision is the reportable one — and the chapter draws the consequence: *the quotable figure is not the one you care about*.

**3.4** **More measurements improve precision and do nothing for trueness.** Derived from VIM §2.14 (trueness is closeness of the average of infinitely many replicates to a reference value; inversely related to systematic error, unrelated to random error) and §2.15.

**3.5** The demonstration uses the book's own Chapter 1 facts: dashboard **10.8 ML** against verified **9.9 ML**. A 0.9 ML systematic offset that no number of dashboard readings would have revealed.

**3.6** `bias` is taught as the social-science name for systematic error (`adcock2001validity` p. 531). Both words are given; neither is presented as the correct one.

**3.7** The disagreement about how reliability relates to validity (`adcock2001validity` p. 532) is **shown, not resolved**. The practical lesson — reliable does not mean valid — survives either account.

**3.8** Not taught: measurement uncertainty evaluation, the GUM framework, coverage intervals, traceability chains, ISO 5725 repeatability and reproducibility conditions. Chapters 5 and 8, and the depth curriculum.

**3.9** `calibration` is taught at recognition depth only — enough to explain how a systematic offset is found, and enough to say that calibrating against a standard does not establish that the quantity measured is the quantity wanted.

### 4. The two traditions

**4.1** Chapter 3 must serve readers measuring physical quantities against reference standards **and** readers measuring constructs for which no standard exists. It must not present either as the general case.

**4.2** Where a reference standard exists, the metrology vocabulary applies cleanly. Where the construct is chosen, "error" language is used with visible care, because there is nothing to subtract from. `jcgm2012vim` §2.16 Note 1 makes error's knowability conditional on a reference value existing.

**4.3** The anchor case must contain **both kinds in one system**: stored volume has a reference value; adequate service pressure does not. This is a structural requirement on the chapter, not a caution to be footnoted.

**4.4** No source may be cited as if its vocabulary were universal. Any sentence pairing metrology with social-science measurement must make the pairing visible.

### 5. The Chapter 4 boundary

**5.1** The reader-facing test:

> **Chapter 3:** the number is here — does it mean what I think?
> **Chapter 4:** why is this number here, and not another?

**5.2** Worked pairs are supplied: a sensor reading 0.15 bar high is Chapter 3; sensors existing only at pump stations is Chapter 4.

**5.3** At least one supplied item **sits on the line** — a monitoring point sited where a technician could park is both a procedure choice and a fact about which records exist. It is given to the reader **unresolved**, as a placement exercise. A boundary a reader can place cases against is worth more than one they are told about.

### 6. Vocabulary decisions

**6.1** `measure` is the controlled term for the procedure. `indicator` is named once as the equivalent term in the literature (`adcock2001validity` p. 530: indicators are "also routinely called measures").

**6.2** `measurand` is **signposted, not reader-facing**. It is the metrology term for the quantity intended to be measured (`jcgm2012vim` §2.3) and does not translate cleanly to a working definition, which need not be quantitative.

**6.3** `score` is registered and used.

**6.4** `proxy` is registered: a measure of something else, accepted because the construct itself cannot be measured directly, with the substitution's cost stated. A proxy's failure mode is **structured, not random** — it fails in the specific circumstances where the substitution breaks.

**6.5** Not introduced: `metric` (registered to Chapter 10), scale types and permissible-statistics theory, `repeatability`, `reproducibility`, `measurement uncertainty`.

### 7. What Chapter 3 does not do

- Not representation (Chapter 2) — it takes a representation as given.
- Not provenance, sampling, selection, or missingness (Chapter 4).
- Not adequacy frameworks, verification, or model validation (Chapter 5).
- Not estimands or identification (Chapter 7).
- Not measurement-error models, attenuation, or uncertainty quantification (Chapter 8).
- Not transportability or external validity (Chapter 9).
- Not metrics as objectives (Chapter 10).
- Not gaming, Goodhart-type failure, or manipulation (Chapter 15).

## Sources promoted

New and verified: `adcock2001validity`.

Reused, verified as directly supporting a Chapter 3 claim: `jcgm2012vim` (upgraded this pass with §§2.13–2.16), `censusndtargetpopulation`, `nasa2024models`, `asme2025credibility` and `fda2023credibility` (named only for the `validation` collision).

## Known gaps carried forward

1. **Messick (1989) not read.** The falsifiable-claims formulation at `adcock2001validity` p. 532 is credited to it and must be attributed as reported.
2. ~~**`adcock2001validity` read to p. 532 only.**~~ **Closed 2026-08-18.** Pages **537–539** were read, covering the treatment of validation types. Clause 2.2's "one validity, several kinds of evidence" is now directly supported rather than inferred: p. 538 calls the three-way grouping "a heuristic device" for grouping **procedures**, and p. 537 records near-universal consensus that content and criterion evidence are types of evidence for construct validity. Pages **533–536 and 540–546 remain uninspected and may not be cited.**
3. **Operationism not researched.** May be mentioned as having existed; may not be characterized.
4. **No source obtained for scale types or units theory.** Units are taught as ordinary careful practice, not from a cited framework.

## No architecture change

Title, central question, core competence, 26-page and 5-hour targets are unchanged and remain governed by `README.md` and `decisions/0001`.
