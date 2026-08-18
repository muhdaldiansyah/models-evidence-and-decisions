# Chapter 5 Bounded Research Plan

Status: working research control. No manuscript drafting and no chapter-boundary decision is implied by this file.

Chapter 5: **Assumptions, Adequacy, and Rival Models**

**Process note.** As recorded in `readiness-audit.md`, this plan was written alongside its research. Stop conditions are stated as applied.

## 1. Research objective

Produce only the conceptual evidence needed to adjudicate Chapter 5's unique job, terminology, scope boundaries, and example architecture.

Do **not** attempt a literature review of philosophy of science, verification and validation, uncertainty quantification, or model criticism.

The research ends when the author can decide:

- what `adequacy` means when finally developed, and what governs how much criticism is enough;
- how verification, validation, and credibility are distinguished at core depth;
- what method organises criticism, and how it adapts where no decisive observation is available;
- which cheap checks are taught, and whether each is sourced or demonstrated;
- where the Chapter 5 / Chapter 8 line falls;
- which demonstration can criticize the reader's own accumulated analysis.

## 2. Source hierarchy

Chapter 5 is unusual: **its primary sources are already in the bibliography and were deliberately reserved for it.** `asme2025credibility`, `fda2023credibility`, and `nrc2012reliability` each carry a note deferring their full framework to this chapter.

Priority:

1. those three reserved credibility and VVUQ sources, read at greater depth than Chapter 1 required;
2. primary methodological sources for the criticism method itself;
3. existing verified sources that bear directly on rival models and model limits (`levins1966strategy`, `sterman2002models`, `frigg2025models`);
4. new sources only where an established practice would otherwise be taught unsourced.

**Special caution.** The credibility standards are written for computational modelling and simulation in regulated engineering and medical-device settings. This book's readers mostly do not work there. No standard may be presented as though its framework governed analysis generally.

## 3. Dossier format

As `../02-representation-mechanisms/research-plan.md` §3.

## 4. R01 — Adequacy, credibility, and how much criticism is enough

### Questions

1. What do the reserved standards actually say about adequacy, and how does it differ from accuracy?
2. What governs how much evidence a model needs?
3. How are verification, validation, and credibility distinguished?
4. What can this book take from frameworks written for regulated computational simulation?
5. Does the answer connect to the pattern established in Chapters 1–4?

### Deliverable

`research-01-adequacy-and-credibility.md`

### Stop condition

Stop when the reader-facing account of adequacy and of what governs sufficiency can be written and sourced. Do not research VVUQ procedures, credibility-factor tables, or regulatory submission requirements.

## 5. R02 — How a formulation fails, and what would show it

### Questions

1. Is there an established method for organising criticism around alternatives and exclusions?
2. What does that method require, step by step?
3. What is the practice it implies — what artifact does a critic actually produce?
4. How must the method be adapted where no decisive observation can be obtained?
5. What is the boundary to Chapter 7's identification and Chapter 11's value of information?

### Deliverable

`research-02-failure-and-exclusion.md`

### Stop condition

Stop when the method can be stated in reader-facing steps, sourced, with the adaptation clearly marked as the book's own. Do not research falsificationism, severe-testing frameworks, or the later literature debating the method.

## 6. R03 — Cheap checks: dimensions, limits, extremes, and bounds

### Questions

1. Which of dimensional checking, limiting cases, extreme-condition checks, and order-of-magnitude bounding can be sourced, and which must be demonstrated?
2. What does each catch that the others do not?
3. What is the honest sourcing status of each?
4. Which are worth the chapter's space?

### Deliverable

`research-03-cheap-checks.md`

### Stop condition

Stop when each check's sourcing status is settled and the demonstrate-versus-cite disposition is explicit for each. Do not research dimensional-analysis theory, asymptotics, or formal bounding methods.

## 7. R04 — Examples, exercises, and the Chapter 8 boundary

R04 begins only after R01–R03 are adjudicated.

### Questions

1. Can the anchor be the reader's own four-chapter analysis rather than a new case?
2. Is there a check that catches something Chapters 1–4 missed, using a technique none of them taught?
3. What worked contrast best exposes the Chapter 5 / Chapter 8 line?
4. What cold-transfer task tests criticism rather than domain expertise?
5. How is a reader stopped from producing a list of generic worries and calling it criticism?

### Deliverable

`research-04-examples-exercises.md`

## 8. Sequencing

R01 → R02 → R03 → author adjudication → R04 → fill `spec.md` → drafting blueprint.

R01 comes first because "how much criticism is enough" governs how the rest of the chapter is pitched.

## 9. Evidence discipline

For every candidate source: verify metadata before promoting a key; create or update `sources/<key>.md` when actually read; record exact support and cautions; do not cite beyond the inspected passage.

**Standing rule adopted after the Chapter 2 gap-closing pass:** an automated fetch of a PDF once returned four fabricated quotations with fabricated page numbers. **Every locator must come from reading the document directly.** A fetch summary is a lead, not evidence.

## 10. Author-adjudication gates

After R01–R03: the reader-facing account of adequacy; verification/validation treatment given Chapter 3's declined `validation`; the criticism method and its adaptation; per-check sourcing dispositions; the Chapter 8 line.

After R04: anchor demonstration, contrasts, exercise sequence, cold-transfer target, and section architecture within 27 pages / 5 hours.

## 11. No-write boundary during bounded research

During each conceptual research cluster, do not modify `spec.md`, `canon/`, `decisions/`, or manuscript files. Research dossiers may be added as working evidence. Governed artifacts change only after explicit author adjudication.
