# Chapter 3 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0010-chapter3-measurement-terminology-and-boundary.md`.

## 1. Drafting objective

26 pages / 5 learning hours that leave the reader unable to write a number into a representation without asking what it stands for and how well.

The chapter must **defeat** twelve named collapses (`spec.md`, "Failure modes"), each by putting the reader somewhere the collapse produces a visibly wrong answer.

## 2. Fixed architecture and budget

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | The Number and the Thing | 2 | 0.25 |
| 2 | From Construct to Score | 5 | 0.90 |
| 3 | What "Valid" Is a Property Of | 5 | 0.95 |
| 4 | Reliable, Precise, and Wrong | 5 | 0.90 |
| 5 | Proxies, Units, and the Cost of Standing In | 3 | 0.55 |
| 6 | The Utility's Pressure Problem | 3 | 0.60 |
| 7 | Cold-Start Practice and Retrieval | 3 | 0.85 |

Roughly 360 words per page. Do not rebalance without recording the reason.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- Pressure is given in **metres of head** throughout, so all arithmetic is subtraction.
- No statistical notation, no formulas beyond arithmetic.
- Citations use Pandoc syntax with locators: `[@key, p. 531]`, `[@key, §2.14]`.
- Never write that an instrument "is valid". See `spec.md` terminology table.
- When the book generalises beyond a source, say so in the sentence that does it.

### Register discipline

This chapter tells the reader that a familiar word — *adequate*, *accurate*, *reliable* — was hiding a decision. The prose must not itself use those words loosely, or the chapter refutes itself on the page.

## 4. Reader-facing sequence

Per `../../decisions/0008`. Chapter 3 follows Chapter 2's structural choice: the anchor is developed incrementally through §2–§5 and consolidated in §6, so the reader builds the case rather than reading it.

Self-explanation pauses: exactly three — §2 (construct versus working definition), §3 (what validity is predicated of), §4 (precise but wrong).

## 5. Section 1 — The Number and the Thing

**Purpose.** Produce an unscaffolded baseline and open the gap.

**Beats.**

1. Recall Chapter 2's role table row in one sentence: zone pressure, what customers experience, observed, **adequate or not**.
2. Point at the phrase. Note that the drought plan uses the same word and never defines it.
3. State the chapter's question: what does a number stand for, and how well?
4. **Opening task, about six minutes.** Define "adequate service pressure" precisely enough that two people measuring independently would get the same answer. Preserve unscored.
5. Close by observing that the reader has just made at least three choices — where, when, and how much — and that most requirements make none of them.

**Do not** introduce construct, working definition, validity, or any Chapter 3 vocabulary here.

## 6. Section 2 — From Construct to Score

**Purpose.** Install the ladder and show that rung 2 is where the argument lives.

**Beats.**

1. Introduce the four rungs: **construct → working definition → measure → score**.
2. Name the source's terms once, attributed: background concept, systematized concept, indicator, scores for cases [@adcock2001validity, p. 530]. Then stop using them.
3. State that `measurement` covers the interaction among the middle levels [@adcock2001validity, p. 530] — arguing about what "adequate" ultimately means is conceptual dispute, not measurement.
4. Work the utility's own definition: **at least 20 metres of head at the fixed monitoring point.** Show it decided *where*, *when*, and *how much*.
5. Reveal how it was chosen — the monitoring point already had an instrument. Not negligence; the normal condition.
6. **The arithmetic.** Tank surface **96 m**; monitoring point **62 m**; highest property **84 m**. Static: 34 m versus 12 m. At peak with 6 m friction and 3 m tank drop: 25 m versus 3 m. One system, two verdicts.
7. **Self-explanation pause 1.** Both numbers are correct. What exactly did the working definition decide?
8. `operationalization` named: working definition → measure. Not "turning a vague idea into a number", which skips a rung.
9. **Choosing a measure does not define the construct** [@adcock2001validity, p. 532]. Interpretations of scores are falsifiable claims; a stipulation cannot be falsified. Collapse 7 defeated here.
10. The ladder revises upward [@adcock2001validity, p. 530]; Kaplan's paradox, resolved "by a process of approximation" [@adcock2001validity, p. 532].
11. Signpost `measurand` once [@jcgm2012vim, §2.3]: metrology's term for the quantity intended to be measured, with the same gap arrived at independently — and note the vocabularies do not translate.
12. **Reader task.** Ladder placement on six supplied statements; then produce a second operationalization and compute its disagreement with the first.

## 7. Section 3 — What "Valid" Is a Property Of

**Purpose.** The chapter's central correction.

**Beats.**

1. Open on the malformed question: *is the monitoring-point sensor valid?*
2. The definition [@adcock2001validity, p. 530]: valid measurement is achieved when scores meaningfully capture the ideas in the corresponding concept.
3. Sharpened [@adcock2001validity, p. 531]: validity holds of the **conjunction** of indicator, scores, and concept. Collapse 2 defeated here.
4. "Scores are never examined in isolation" [@adcock2001validity, p. 531].
5. Therefore the answerable question is *are these scores interpretable as this construct, for this use?*
6. **Self-explanation pause 2.** If validity is not a property of the sensor, what would it even mean to buy a "validated" sensor?
7. Interpretations are falsifiable claims requiring evidence; "Validity assessment is the search for this evidence" [@adcock2001validity, p. 532] — credited there to Messick 1989, and to be attributed as reported.
8. **Reader task.** Write what would have to be true for the scores to support "Hillcrest is adequately served", and name one observation that would count against it.
9. **Contextual specificity** [@adcock2001validity, p. 530]. A 20 m threshold defensible in flat Lowfield may not be in Hillcrest. Collapse 12 defeated here. State the Chapter 9 boundary in the same paragraph.
10. The 37 adjectives [@adcock2001validity, p. 530]. One validity, several kinds of evidence — never a taxonomy.
11. **Name the `validation` collision, once.** Measurement validation versus computational-model validation [@asme2025credibility; @fda2023credibility]. Then say Chapter 3 will say *assessing the evidence for an interpretation* instead, and move on.
12. Boundary to causal inference in one sentence, quoting [@adcock2001validity, p. 529].
13. **The three-chapter echo**, stated once and labelled as the book's own observation: adequacy relative to use, content relative to purpose, validity relative to interpretation.

## 8. Section 4 — Reliable, Precise, and Wrong

**Purpose.** The two confusions that cost most in practice.

**Beats.**

1. **Reliability** [@adcock2001validity, p. 531]: random error is inconsistency on repetition, conventionally a reliability problem; systematic error is bias.
2. **C1 contrast — reliable and wrong.** Two sentences. Collapse 3 defeated here.
3. The relation between reliability and validity is contested [@adcock2001validity, p. 532]. Show both accounts; resolve neither. The practical lesson survives either.
4. The metrology trio, from the standard. **Precision** [@jcgm2012vim, §2.15]: agreement among replicates, expressed numerically. **Trueness** [@jcgm2012vim, §2.14]: closeness of the average of infinitely many replicates to a reference value; not a quantity. **Accuracy** [@jcgm2012vim, §2.13]: not a quantity, and not to be used for either alone.
5. **The asymmetry.** Precision is the one you can put a number on — so the quotable figure is not the one you care about. Collapse 5 defeated here.
6. The pump-station sensor: resolution **0.01 bar**, repeatability **±0.02 bar**, offset **0.15 bar high**, about **1.5 m** of head. Precise, and wrong. Collapse 4 and 9 defeated here.
7. **Self-explanation pause 3.** You have 200 readings from this sensor, all within 0.02 bar of each other. What have you learned, and what have you not?
8. **More measurements improve precision and do nothing for trueness** — from [@jcgm2012vim, §2.14], since trueness concerns the average of infinitely many replicates and is unrelated to random error.
9. **The offset demonstration**, on the book's own facts: dashboard **10.8 ML**, verified **9.9 ML**, a 0.9 ML gap in one direction. No number of dashboard readings would have found it. Collapse 6 defeated here.
10. `measurement error` [@jcgm2012vim, §2.16]: measured value minus a reference value; knowable only where a reference exists; **not** to be confused with a mistake.
11. **The no-reference problem.** Stored volume has a reference value. *Adequate pressure* does not — its threshold is chosen. Where the construct is chosen, there is nothing to subtract from, and error language must be used with care. This is structural, not a footnote.
12. `calibration` at recognition depth: it finds an offset; it does not establish you measured the right thing. Collapse 11 defeated here.

## 9. Section 5 — Proxies, Units, and the Cost of Standing In

**Beats.**

1. `proxy`: a measure of something else, accepted because the construct cannot be measured directly or affordably.
2. The anchor's proxy: tank level for customer pressure. Cheap, continuous, already instrumented.
3. **When it works and when it breaks.** It tracks pressure when the tank is the binding constraint; it fails when friction loss is — Chapter 2's Mechanism B. At peak, the 6 m friction loss exceeds the 3 m tank drop, so the proxy is least informative exactly when the answer matters. Collapse 8 defeated here.
4. **The failure is structured, not random** — which is why more readings do not repair it. Contrast explicitly with random error from §4.
5. **Units.** Metres of head, bar, psi. Say what a unit choice makes comparable and what it hides. Keep short; no cited framework exists and none is claimed.
6. **C2 contrast — one construct, two thresholds.** The neighbouring utility's **95%** against the utility's **91%**: different threshold, time, and location. Comparable in appearance only. Say plainly that the neighbour is not misreporting.
7. Close: a score without its working definition is not a weak number, it is an uninterpretable one.

## 10. Section 6 — The Utility's Pressure Problem

**Purpose.** Consolidation. Fading begins.

**Beats.**

1. The four operationalizations side by side against one decision: whether to report Hillcrest as adequately served.
2. A table giving each one's verdict, and what each is good for.
3. State the consequence: the utility's plan records Hillcrest as adequate because of where an instrument happened to be.
4. Tie back to Chapter 2's finding that a plan can only contain triggers its representation can express — and add Chapter 3's: a plan can only contain thresholds its measures can evaluate.
5. **Planted-defect diagnosis task.** Five defects per `spec.md`. Diagnosis, consequence, repair. Feedback linked only after production.
6. **Boundary placement task.** Four supplied items on the Chapter 3 / Chapter 4 line. The fourth is unresolved and must be given as such.

## 11. Section 7 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 opening definition. Compare, do not score. Name the two or three patterns most first definitions show.
2. **Cold transfer.** Link exactly one assigned form. State plainly that the other must not be opened.
3. **Retrieval from memory** before checking: the measurement checklist.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form, per the `../../decisions/0008` pilot window.
6. If the transfer went badly — a short diagnostic of specific missing moves, as in Chapter 2 §7.
7. Close: Chapter 4 asks why these records exist and not others.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production. The delayed form is never linked in §7.

## 12. Citation discipline

Every section carries at least one verified locator. `adcock2001validity` may be cited only to **p. 532**; later pages were not inspected. The falsifiable-claims formulation must be attributed as reported from Messick 1989, which was not read.

## 13. What the draft may not do

- Say an instrument is valid.
- Report accuracy or trueness as a number.
- Teach a taxonomy of validities.
- Merge measurement validation with model validation.
- Resolve the reliability/validity disagreement.
- Teach sampling, missingness, or why records exist — Chapter 4.
- Teach uncertainty quantification or error models — Chapter 8.
- Characterize operationism.
- Present synthetic case values as typical, standard, or recommended.
- Imply any health or safety consequence of low pressure.
