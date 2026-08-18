# Chapter 3 Bounded Research Plan

Status: working research control. No manuscript drafting and no chapter-boundary decision is implied by this file.

Chapter 3: **Measurement and Operationalization**

**Process note.** As recorded in `readiness-audit.md`, this plan was written alongside its research rather than strictly before it. The stop conditions below are therefore stated as they were applied, not as predictions.

## 1. Research objective

Produce only the conceptual evidence needed to adjudicate Chapter 3's unique job, terminology, scope boundaries, and example architecture.

Do **not** attempt a literature review of psychometrics, metrology, measurement theory, or the philosophy of measurement.

The research ends when the author can decide:

- what the ladder from concept to number is, and what each step commits the reader to;
- what `validity` is a property of;
- how the metrology vocabulary (accuracy, trueness, precision, error) relates to the social-science vocabulary (validity, reliability, bias);
- where the Chapter 3 / Chapter 4 line falls, in a form a reader can apply;
- which anchor and transfer cases can carry a five-hour competence.

## 2. Source hierarchy

Chapter 3 has an unusual requirement: it must serve readers who measure physical quantities against traceable standards **and** readers who measure constructs for which no standard exists. Sourcing must reflect both, and must not silently merge them.

Priority:

1. authoritative metrology standards and vocabularies for physical measurement terms;
2. peer-reviewed cross-disciplinary methodology for concept-to-indicator reasoning;
3. primary psychometric sources where validity theory is genuinely at issue;
4. high-quality reviews only where they efficiently map competing terminology;
5. pedagogical sources only if Chapter 3 introduces a learning-design claim not covered by the book-wide pedagogy.

Avoid textbook summaries as load-bearing definitional evidence, and avoid any source that presents one field's measurement vocabulary as universal.

## 3. Dossier format

As `../02-representation-mechanisms/research-plan.md` §3: precise question; candidate definitions from sources; where sources agree; where terminology is field-specific or contested; implications for Chapter 3; explicit cautions; candidate citation keys; unresolved author decisions.

A dossier is evidence for adjudication, not the author's decision.

## 4. R01 — Constructs, operationalization, indicators, scores

### Questions

1. What is the defensible sequence from a concept to a number, and what does each step commit the reader to?
2. What is the difference between the loose everyday meaning of a concept and the specific formulation a particular analysis adopts?
3. What does `operationalization` name, precisely?
4. Is choosing a measurement procedure the same as defining the concept?
5. Does the sequence run one way, or does it revise upward?

### Deliverable

`research-01-constructs-operationalization.md`

### Stop condition

Stop when the reader-facing ladder can be stated and each rung named without inventing terminology. Do not continue into measurement theory, representational theory of measurement, or scale-type formalism.

## 5. R02 — Validity: what it is a property of

### Questions

1. Is validity a property of an instrument, of scores, of an interpretation, or of a use?
2. What follows for the reader from that answer?
3. What is contextual specificity and how far does it extend?
4. How should the proliferation of validity adjectives be handled at core depth?
5. Where is the boundary to Chapter 5's model validation and Chapter 9's external validity?

### Deliverable

`research-02-validity.md`

### Stop condition

Stop when a reader-facing sentence stating what validity is predicated of can be written and defended from a verified locator. Do not research validity taxonomies, argument-based validation frameworks, or consequential validity debates beyond stating the boundary.

## 6. R03 — Reliability, error, accuracy, trueness, precision

### Questions

1. What do the metrology standards define these terms to mean, exactly?
2. Which of them are quantities that can be reported numerically, and which are not?
3. How does the metrology vocabulary relate to systematic/random error and reliability as used outside metrology?
4. What does and does not improve with more measurements?
5. Which of these terms does a core reader actually need?

### Deliverable

`research-03-reliability-error-precision.md`

### Stop condition

Stop when the controlled vocabulary can be chosen and the "precise but wrong" demonstration can be sourced. Do not research uncertainty evaluation, the GUM framework, coverage intervals, traceability chains, or ISO 5725 statistics.

## 7. R04 — Examples, exercises, and the Chapter 4 boundary

R04 begins only after R01–R03 are adjudicated enough that examples will not smuggle in unstable terminology.

### Questions

1. Which construct can be operationalized several defensible ways that **disagree**, with the disagreement mattering to a decision?
2. Can the case show precise-but-wrong, reliable-but-invalid, and proxy substitution without requiring specialist knowledge?
3. Should the water case recur, and if so on what new operation?
4. What worked contrast best exposes the Chapter 3 / Chapter 4 line?
5. What cold-transfer task tests measurement reasoning rather than domain expertise or arithmetic?

### Deliverable

`research-04-examples-exercises.md`

## 8. Sequencing

R01 → R02 → R03 → author adjudication → R04 → fill `spec.md` → drafting blueprint.

R02 depends on R01 because "validity of what?" cannot be answered before the ladder exists. R03 is largely independent and could be done first, but is placed after R02 so that the metrology vocabulary is introduced against an already-settled account of what measurement is for.

## 9. Evidence discipline

For every candidate source: verify metadata before promoting a key; create or update `sources/<key>.md` when the source is actually read; record exact support and cautions; distinguish established terminology from the book's synthesis; do not cite beyond the inspected passage.

Existing sources may be reused only where they directly support a Chapter 3 claim. `jcgm2012vim` qualifies, and its Chapter 1 note already reserves formal measurement terminology for this chapter.

**Special caution for this chapter.** Metrology and social-science measurement share a structure but not a standard. No source may be cited as if its vocabulary were universal, and any sentence that pairs the two traditions must make the pairing visible.

## 10. Author-adjudication gates

After R01–R03, produce decisions on: the reader-facing ladder and its rung names; what validity is predicated of; the accuracy/trueness/precision set; the Chapter 3 / Chapter 4 line in applicable form; core versus deferred scope.

After R04: anchor, contrasts, exercise sequence, cold-transfer target, and section architecture within 26 pages / 5 hours.

## 11. No-write boundary during bounded research

During each conceptual research cluster, do not modify `spec.md`, `canon/`, `decisions/`, or manuscript files. Research dossiers may be added as working evidence. Governed artifacts change only after explicit author adjudication.
