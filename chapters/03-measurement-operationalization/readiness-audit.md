# Chapter 3 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 3: **Measurement and Operationalization**

**Process note.** Chapter 2's audit was written before its research. This one was written alongside it, in a single working session. That is a departure from the sequence in `../02-representation-mechanisms/research-plan.md` §9 and is recorded rather than concealed: the boundaries and collapses below were identified first and then checked against sources, but the two were not separated in time. Where a finding came from the sources rather than from prior analysis, it is marked.

Current architecture from `README.md` and `spec.md`:

- central question: **What do the numbers stand for, and how well?**
- core competence: **Connect constructs to observables through operationalization, units, proxies, validity, reliability distinctions, and measurement error.**
- target: 26 pages / 5 serious learning hours.

## 1. Readiness verdict

**Drafting-ready after adjudication.**

Unlike Chapter 2 at the equivalent stage, Chapter 3 has an unusually strong starting position:

- `jcgm2012vim` is already in the bibliography, already verified, and its Chapter 1 source note **explicitly reserves formal measurement terminology for Chapter 3**;
- `canon/terminology.md` already registers `construct`, `measure`, `proxy`, `target`, `target population`, `estimand`, `estimator`, `estimate`, and `metric` — the collision set is already mapped;
- Chapter 1 already planted a measurement failure in its anchor case: a dashboard reading of **10.8 ML** against a verified **9.9 ML**;
- Chapter 2 closes by handing this chapter its question explicitly.

What remains is adjudication, not discovery.

## 2. Unique-job hypothesis

> Teach readers to interrogate the link between a quantity in their representation and the number attached to it — what the number stands for, by what procedure it was produced, and how well it supports the interpretation being placed on it.

Chapter 2 decided *which quantities belong in the representation*. Chapter 3 asks whether the numbers attached to those quantities mean what the reader assumes.

The reader who finishes Chapter 3 should be unable to write "Hillcrest demand: 0.9 ML/day" without asking what "Hillcrest demand" was defined to be, what procedure produced 0.9, and what would have to be true for that number to support the decision it is being used for.

## 3. Neighbouring-chapter boundaries

### Chapter 1 — target and intended use

Chapter 1 owns intended use, target, and the record-is-not-the-target distinction at intuitive depth. Chapter 3 formalizes the second of these. It must not reteach decision framing.

### Chapter 2 — representation

Chapter 2 owns what is inside the representation, at what grain, and the roles quantities play. Chapter 3 takes a representation as given and asks about the numbers.

The boundary is clean and worth stating in the manuscript: Chapter 2 asked *should Hillcrest demand be in the model, and at what grain?* Chapter 3 asks *what does the number 0.9 stand for, and how well?*

### Chapter 4 — observation processes and provenance

**This is the hardest boundary in the chapter and the one most likely to be violated.**

Proposed split, to be adjudicated:

- **Chapter 3** — given that a record exists, does the number in it mean what we think? This is the construct → indicator → score link.
- **Chapter 4** — why does *this* record exist rather than another, and in this form? This is sampling, selection, missingness, censoring, reporting, and institutional production.

Worked test of the split: a pressure sensor that reads 0.15 bar high is Chapter 3. A pressure sensor that exists only at the pump station and nowhere in the zone is Chapter 4.

The test is not perfectly sharp — where an instrument is placed is both a measurement-procedure choice and a fact about which records come to exist. The manuscript must state the split explicitly and accept that some cases sit on the line.

### Chapter 5 — assumptions and adequacy

Chapter 5 owns systematic criticism, verification, validation, and adequacy frameworks. Chapter 3 may say a measurement is inadequate for a stated interpretation; it must not import the full credibility apparatus.

Note a genuine terminology hazard: `validation` in the measurement sense (assessing evidence for an interpretation of scores) and `validation` in the computational-model sense (`asme2025credibility`, `fda2023credibility`) are different practices sharing a word.

### Chapter 7 — estimands and identification

Chapter 7 owns the formal target of estimation. Chapter 3 may say that a measured quantity is not automatically the quantity a later analysis will target, and must not define estimands.

### Chapter 8 — estimation and measurement-error models

Chapter 8 owns uncertainty quantification and measurement-error mathematics — attenuation, errors-in-variables, correction methods. Chapter 3 stops at recognizing that error exists, has kinds, and has consequences.

### Chapter 9 — transport and generalizability

`adcock2001validity` p. 530 introduces **contextual specificity**: a measure valid in one context may be invalid in another. This is genuinely Chapter 3 material, and it is adjacent to Chapter 9's external validity. Chapter 3 owns *this instrument, this context*; Chapter 9 owns moving evidence between populations and settings.

### Chapter 10 — metrics and objectives

`metric` is already registered in canon with a Chapter 10 home. Chapter 3 may discuss a metric as a measurement; it must not treat metrics as objectives.

### Chapter 15 — gaming

Goodhart-type failures, metric gaming, and manipulation of evidence are Chapter 15. Chapter 3 may note that a measure can be acted upon; it must not teach strategic response.

## 4. Terminology readiness

The collision set is unusually well mapped already. Terms requiring adjudication:

- construct (already registered — Chapter 3 sense must be reconciled);
- measure / indicator (already registered as `measure`; `indicator` is the `adcock2001validity` term);
- operationalization;
- measurand (metrology-specific; reserved from Chapter 1);
- score;
- proxy (already registered);
- validity;
- validation (hazard: collides with model validation);
- reliability;
- measurement error, systematic error / bias, random error;
- accuracy, trueness, precision (VIM-specific, mutually confusable);
- calibration;
- units and scale type.

## 5. High-risk conceptual collapses to prevent

1. **Construct = measure.** The thing cared about and the number produced are different objects.
2. **Validity is a property of the instrument.** *(Confirmed from sources.)* `adcock2001validity` p. 531 locates validity in whether scores "can meaningfully be interpreted in terms of the systematized concept", and p. 530 makes it a property of a conjunction, not a device.
3. **Reliability = validity.** Consistent is not correct. A reliably wrong instrument is reliable.
4. **Precision = accuracy.** *(Confirmed from sources.)* VIM §2.15 Note 4 records this as an outright error, and §2.13 Note 2 forbids the conflation in both directions.
5. **Accuracy is a number you can report.** *(Confirmed from sources.)* VIM §2.13 Note 1: accuracy is not a quantity and is not given a numerical value.
6. **Error = noise.** Systematic error does not average out with more readings.
7. **Operationalization = definition.** Choosing a procedure does not settle what the concept means; treating it as if it did is the operationist mistake.
8. **Proxy = target.** A proxy stands in for something; the substitution has a cost that must be stated.
9. **More decimal places = better measurement.** Resolution is not trueness.
10. **Measurement is passive observation.** Producing a number is an active procedure with choices in it — this is also the Chapter 4 boundary.
11. **Calibration = validation.** Calibrating against a standard does not establish that the quantity measured is the quantity wanted.
12. **A validated instrument is valid everywhere.** *(Confirmed from sources.)* `adcock2001validity` p. 530, contextual specificity.

## 6. Research clusters

Because the source position is strong, four clusters suffice.

- **R01 — Constructs, operationalization, indicators, and scores.** The ladder from concept to number, and what each step commits you to.
- **R02 — Validity: what it is a property of.** Whether validity attaches to instruments or to interpretations for uses; contextual specificity; the terminological proliferation problem.
- **R03 — Reliability, error, accuracy, trueness, precision.** The metrology vocabulary and its relation to the social-science vocabulary; what does and does not average out.
- **R04 — Examples, exercises, and transfer.** Anchor selection and the Chapter 3 → Chapter 4 boundary in worked form.

## 7. Candidate example constraints

A Chapter 3 anchor should contain a quantity that is **genuinely a construct** — not directly readable off an instrument — that can be operationalized in several defensible ways which **disagree**, with the disagreement mattering to a decision.

Avoid an anchor whose real difficulty is sampling or missingness (Chapter 4), estimation (Chapter 8), or objective-setting (Chapter 10).

The water utility remains available and may recur only if Chapter 3 performs a genuinely new operation on it. Chapter 2's role table already recorded zone pressure as "what customers experience — observed — adequate or not". That phrase does substantial unexamined work and is a natural Chapter 3 opening.

## 8. Decisions likely required after research

1. Whether `indicator` or `measure` is the controlled term, given `measure` is already registered.
2. Whether `measurand` is reader-facing or a signposted metrology term.
3. What `validity` is predicated of, in reader-facing wording.
4. Whether `validation` is used at all, given the collision with model validation.
5. Whether accuracy/trueness/precision are all three taught, or only the pair the reader most needs.
6. Where exactly the Chapter 3 / Chapter 4 line falls, in a form a reader can apply.
7. The anchor construct and the transfer forms.

## 9. Drafting gate

Chapter 3 becomes drafting-ready when R01–R04 have dossiers, the terminology decisions are adjudicated, the Chapter 4 boundary is stated in applicable form, and `spec.md` no longer contains load-bearing TODOs.
