# Chapter 4 Bounded Research Plan

Status: working research control. No manuscript drafting and no chapter-boundary decision is implied by this file.

Chapter 4: **Observation Processes and Data Provenance**

**Process note.** As recorded in `readiness-audit.md`, this plan was written alongside its research rather than strictly before it. Stop conditions are stated as applied, not as predicted.

## 1. Research objective

Produce only the conceptual evidence needed to adjudicate Chapter 4's unique job, terminology, scope boundaries, and example architecture.

Do **not** attempt a literature review of survey methodology, missing-data theory, selection models, causal inference, or data provenance standards.

The research ends when the author can decide:

- how to name and describe the observation process as distinct from the modelled process;
- what to teach about why dataset size does not protect against selection;
- how much missingness and censoring vocabulary a core reader needs;
- where the Chapter 4 / Chapter 15 line falls, in a form a reader can apply;
- which anchor and transfer cases carry a five-hour competence.

## 2. Source hierarchy

Priority:

1. peer-reviewed statistical work establishing what dataset composition does to inference;
2. survey-methodology sources for nonresponse and coverage, where they correct a common belief;
3. primary sources for missingness where the conditions for ignoring it are at issue;
4. official statistical-agency standards for established terminology;
5. review sources only where they efficiently map competing vocabulary.

**Special caution for this chapter.** Much of the relevant literature is written for probability surveys. Chapter 4 must also serve readers whose records are administrative, operational, or incidental — meters, logs, tickets, filings — where no sampling design ever existed. No survey-methodology source may be cited as though its framework covered those cases automatically.

## 3. Dossier format

As `../02-representation-mechanisms/research-plan.md` §3.

## 4. R01 — Two processes: the world and the record

### Questions

1. What is the defensible way to name and separate the process being modelled from the process that produced the records?
2. What is a record, and what does describing its provenance involve?
3. What does the separation buy the reader that Chapters 2 and 3 have not already bought?
4. At what points can the record-producing process intervene between the world and the dataset?

### Deliverable

`research-01-two-processes.md`

### Stop condition

Stop when the separation can be stated in one reader-facing sentence and the intervention points can be enumerated. Do not research provenance standards, lineage formalisms, or data-management frameworks.

## 5. R02 — Selection, coverage, and why size does not save you

### Questions

1. What determines how badly a non-representative dataset misleads?
2. Does collecting more records reduce that error?
3. Is a high coverage rate or response rate evidence that a dataset is trustworthy?
4. Is a dataset biased as a whole, or per quantity estimated?
5. What can be said at core depth without importing the mathematics?

### Deliverable

`research-02-selection-and-size.md`

### Stop condition

Stop when the chapter's central counterintuitive claim can be stated and sourced, and when the response-rate correction can be stated and sourced. Do not research weighting, calibration, post-stratification, or selection models — Chapter 8.

## 6. R03 — Missingness, censoring, and absence

### Questions

1. Under what conditions may the process causing missing data be ignored?
2. How much of the standard missingness vocabulary does a core reader need?
3. What distinguishes a censored observation from a missing one?
4. What does it mean that something is absent from a dataset entirely — not missing, but never eligible to appear?
5. Which of these can be detected from the dataset itself, and which cannot?

### Deliverable

`research-03-missingness-censoring-absence.md`

### Stop condition

Stop when the reader can be told what question to ask about a gap and why the answer matters. Do not research imputation, likelihood methods, or survival analysis.

## 7. R04 — Examples, exercises, and the Chapter 15 boundary

R04 begins only after R01–R03 are adjudicated.

### Questions

1. Which case has a record set whose **composition** produces a wrong answer while every value in it is correct?
2. Can the case expose selection, missingness, censoring, reporting, and institutional purpose without specialist knowledge?
3. Should the water case recur, given Chapter 3 has already handed it over?
4. What worked contrast best exposes the Chapter 4 / Chapter 15 line?
5. What cold-transfer task tests provenance reasoning rather than domain expertise?

### Deliverable

`research-04-examples-exercises.md`

## 8. Sequencing

R01 → R02 → R03 → author adjudication → R04 → fill `spec.md` → drafting blueprint.

R02 is placed second because its result is the chapter's most counterintuitive and shapes how much of R03 is needed.

## 9. Evidence discipline

For every candidate source: verify metadata before promoting a key; create or update `sources/<key>.md` when actually read; record exact support and cautions; do not cite beyond the inspected passage.

**Where a source is verified only at abstract level, that must be stated in the source note, no internal locator may be cited, and the reliance must be recorded as a gap to close before freeze.**

## 10. Author-adjudication gates

After R01–R03: reader-facing name for the observation process; the size/selection claim and how quantitatively it is given; missingness vocabulary depth; the Chapter 15 line in applicable form; core versus deferred scope.

After R04: anchor, contrasts, exercise sequence, cold-transfer target, and section architecture within 28 pages / 5 hours.

## 11. No-write boundary during bounded research

During each conceptual research cluster, do not modify `spec.md`, `canon/`, `decisions/`, or manuscript files. Research dossiers may be added as working evidence. Governed artifacts change only after explicit author adjudication.
