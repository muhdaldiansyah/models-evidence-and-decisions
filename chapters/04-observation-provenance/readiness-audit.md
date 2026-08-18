# Chapter 4 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 4: **Observation Processes and Data Provenance**

**Process note.** As in Chapter 3, this audit was written alongside its research rather than strictly before it. Recorded rather than concealed; findings taken from sources are marked.

Current architecture from `README.md` and `spec.md`:

- central question: **Why did these records, and not others, come to exist in this form?**
- core competence: **Describe the observation process separately from the process being modeled, including sampling, selection, missingness, censoring, aggregation, reporting, institutional incentives, and possible manipulation.**
- target: 28 pages / 5 serious learning hours.

## 1. Readiness verdict

**Drafting-ready after adjudication.**

Chapter 4 arrives with the strongest handoff of any chapter so far. Chapter 3 closes by naming this chapter's anchor problem outright: Hillcrest has no zone meter, and its **0.9 ML per day** was produced by subtracting the metered zones from the town total. The record exists, it has a number in it, and the number was never measured.

Also already in place:

- `censusndtargetpopulation` is verified and concerns eligibility and response rates — directly Chapter 4 material;
- Chapter 2's `aggregation` entry already reserves observation- and reporting-level aggregation for this chapter;
- Chapter 3's `spec.md` already states the boundary test in reader-applicable form.

## 2. Unique-job hypothesis

> Teach readers to treat the process that produced their records as a **second system**, with its own logic, actors, incentives, and failure modes — separate from the process they are trying to model, and requiring its own description.

Chapter 3 asked whether a number means what you think. Chapter 4 asks a question that survives even a perfect answer to that: given that every number in your dataset is impeccably measured, **why are these the numbers you have?**

A reader who finishes Chapter 4 should be unable to accept a dataset without asking who made it, for what purpose, what they were required to record, and what never entered it at all.

## 3. Neighbouring-chapter boundaries

### Chapter 2 — representational aggregation

Already governed. Chapter 2's `aggregation` entry names the split: representational aggregation is a modelling choice made before any data exist; aggregation introduced by observation, recording, or reporting is Chapter 4's. Chapter 4 must restate the split from its own side.

### Chapter 3 — measurement

The boundary is already stated in `../03-measurement-operationalization/spec.md` and given to readers as a placement exercise:

> **Chapter 3:** the number is here — does it mean what I think?
> **Chapter 4:** why is this number here, and not another?

Chapter 4 should reuse the same test rather than inventing a second one, and should take the deliberately unresolved boundary case with it.

### Chapter 7 — identification

Selection is a threat to causal identification and has a formal treatment there. Chapter 4 owns **recognizing and describing** how records came to exist; Chapter 7 owns what follows for identifying an effect.

### Chapter 8 — methods

Weighting, imputation, missing-data models, selection models, and correction methods are Chapter 8. Chapter 4 must stop at recognizing the problem and naming what would have to be known to address it.

### Chapter 9 — transport

Target populations, external validity, and transportability. Chapter 4 asks whether your records represent the population you are asking about **here**; Chapter 9 asks whether findings travel.

### Chapter 15 — strategic response

**The hardest boundary in this chapter**, because Chapter 4's governed core competence explicitly includes "institutional incentives, and possible manipulation."

Proposed split, to be adjudicated:

- **Chapter 4** — records are produced by people and institutions with reasons, and those reasons shape what gets recorded. *This was recorded because someone had to report it monthly.*
- **Chapter 15** — agents responding to the fact that a measure is being used. *The number changed because people learned it was being watched.*

Chapter 4 is the record-production process **as it is**. Chapter 15 is that process **responding to being used**. Goodhart-type failure, metric gaming, and equilibrium remain Chapter 15.

### Chapter 17 — monitoring

Drift, tampering detection, and revision triggers are Chapter 17. Chapter 4 may note that a recording process can change over time; it must not teach monitoring design.

## 4. Terminology readiness

Terms requiring adjudication:

- observation process (and its relation to the process being modelled);
- provenance;
- record;
- selection, selection effect;
- sampling frame, coverage;
- missingness;
- censoring, truncation;
- nonresponse, response rate;
- reporting;
- administrative data.

`aggregation` is already registered with a Chapter 2 / Chapter 4 split; Chapter 4 completes the second half.

## 5. High-risk conceptual collapses to prevent

1. **The observation process is the process being modelled.** They are two systems, and conflating them is the chapter's root error.
2. **More data is better data.** *(Confirmed from sources.)* `meng2018paradox` p. 686: "without taking data quality into account, population inferences with Big Data are subject to a *Big Data Paradox*: the more the data, the surer we fool ourselves."
3. **Missing means random.** *(Confirmed from sources.)* `rubin1976missing` states conditions under which the missingness process may be ignored, which presupposes that ignoring it is generally not safe.
4. **Response rate measures bias.** *(Confirmed from sources.)* `davern2013nonresponse`: "Response rates lack validity in that there is not even a moderate correlation with nonresponse bias."
5. **A dataset is biased or unbiased as a whole.** *(Confirmed from sources.)* `davern2013nonresponse`: bias "is an estimate level measure and it cannot be easily summarized by a survey level proxy measure."
6. **Complete means representative.** Covering most of a population does not control the correlation between being recorded and the value.
7. **Provenance is documentation.** Provenance is a causal history of how a record came to exist, not a metadata field.
8. **Selection happens once, at sampling.** It happens at every stage: who is eligible, who is reached, who responds, what is retained, what is published.
9. **Censoring is a kind of missingness.** A censored observation carries partial information; a missing one carries none.
10. **Aggregation in records is the same as representational aggregation.** Chapter 2 boundary.
11. **Institutional incentive means fraud.** Ordinary institutional purpose shapes records without anyone behaving badly.
12. **Absence in the record means absence in the world.** The most consequential collapse, and the hardest to see, because there is nothing to look at.

## 6. Research clusters

- **R01 — Two processes: the world and the record.** The core separation, provenance, and what a record is.
- **R02 — Selection, coverage, and why size does not save you.** The `meng2018paradox` material and the response-rate correction.
- **R03 — Missingness, censoring, and absence.** What can and cannot be ignored, and what a gap carries.
- **R04 — Examples, exercises, and the Chapter 15 boundary.**

## 7. Candidate example constraints

A Chapter 4 anchor needs a record set whose **composition** — not whose values — determines a wrong answer, with the composition traceable to identifiable decisions by identifiable actors.

Avoid an anchor whose real difficulty is measurement (Chapter 3), estimation (Chapter 8), or strategic response (Chapter 15).

The water utility is available and Chapter 3 has already handed it over. The subtraction-residual demand figure satisfies the constraint exactly: the number is arithmetically correct and exists only because of which meters were installed.

## 8. Decisions likely required after research

1. What `observation process` is called, reader-facing, and how it is distinguished from the modelled process.
2. Whether `provenance` is controlled vocabulary or an ordinary word.
3. How much of the missingness vocabulary the reader meets, given `rubin1976missing` is verified only at abstract level.
4. Whether `censoring` is taught as distinct from missingness at this depth.
5. Where exactly the Chapter 4 / Chapter 15 line falls, in applicable form.
6. Whether the Meng result is given quantitatively or qualitatively.
7. The anchor and the transfer forms.

## 9. Drafting gate

Chapter 4 becomes drafting-ready when R01–R04 have dossiers, terminology is adjudicated, the Chapter 15 boundary is stated in applicable form, and `spec.md` no longer contains load-bearing TODOs.
