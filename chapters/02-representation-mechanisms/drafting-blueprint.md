# Chapter 2 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0009-chapter2-representation-terminology-and-boundary.md`.

## 1. Drafting objective

Produce 29 pages / 6 learning hours that leave the reader able to build two defensible representations of an unfamiliar system and say what each can and cannot answer.

The chapter must **defeat** twelve named collapses (`spec.md`, "Failure modes"), not merely avoid them. Defeating a collapse means the reader meets a case where the collapse would produce a visibly wrong answer.

## 2. Fixed architecture and budget

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | The Same System, Two Questions | 2 | 0.30 |
| 2 | Boundary: What the Question Puts Inside | 5 | 1.00 |
| 3 | Parts, Roles, and What Must Be Carried Forward | 5 | 1.00 |
| 4 | Mechanism: What Would Have to Be True | 4 | 0.80 |
| 5 | Leaving Out, Making Up, and Lumping Together | 6 | 1.15 |
| 6 | Three Representations of One Utility | 4 | 0.85 |
| 7 | Cold-Start Practice and Retrieval | 3 | 0.90 |

Do not rebalance without recording the reason. Page counts are drafting targets at roughly 360 words per page.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and for the first appearance of a controlled term.
- No notation. No symbols standing for quantities. Numbers appear as numbers with units.
- Every diagram must be describable in prose and reproducible by hand in under two minutes. Diagrams are specified in words; no figure files are produced at this stage.
- Citations use Pandoc syntax with locators: `[@key, p. 34]`, `[@key, §2.1.1]`.
- Never write "the mechanism is" or "X causes Y". See `spec.md` terminology table.
- When the book generalises beyond a source, say so in the sentence that does it.

### Register discipline

The chapter argues that a simpler representation is often better. The prose must not therefore become breezy. Precision about *why* a simplification is defensible is the chapter's subject; imprecise prose would contradict the content.

## 4. Reader-facing sequence

Per `../../decisions/0008`: initial attempt → worked development → prompted self-explanation → fading → error diagnosis → cold transfer → retrieval → delayed retest.

Chapter 2 differs from Chapter 1 in one structural way, deliberately: the worked case is developed **incrementally across §2–§5** and consolidated in §6, rather than delivered whole in one section. The reader therefore builds the anchor rather than reading it.

Self-explanation pauses: exactly three, at §2 (boundary choice), §4 (epistemic status of a drawn mechanism), §5 (the aggregation failure).

## 5. Section 1 — The Same System, Two Questions

**Purpose.** Produce an unscaffolded baseline and create the chapter's central puzzle.

**Beats.**

1. Recall the Chapter 1 utility in four sentences. Supply the verified **9.9 ML**, the **4.5 ML** reserve, **8.4 ML/day** input, **9.0 ML** day-1 demand. Do not re-derive Chapter 1's analysis.
2. State that Chapter 1's representation was one tank, one inflow, one demand number — and that it answered its question correctly.
3. Pose the second question: *if supply must be restricted, who loses service first?*
4. **Opening task, about eight minutes.** Ask the reader to sketch what a representation would need to contain to answer the second question, and to name one thing Chapter 1's representation cannot tell them. Preserve unscored.
5. Close by naming the chapter's claim: what goes inside is settled by the question, and this is established practice, not a stance of this book.

**Do not** define representation, boundary, or state in this section. The reader must feel the gap before it is named.

## 6. Section 2 — Boundary

**Purpose.** The reader draws and defends an analytical cut.

**Beats.**

1. `representation` and `target system` introduced. State explicitly that `target system` is not a renaming of Chapter 1's `target`.
2. The boundary as an analytical cut, not a physical edge. Collapse 3 defeated here.
3. Purpose-relativity, cited from three traditions [@astrom2008feedback, p. 27; @nasa2024models, §4.1.1.1; @levins1966strategy, pp. 421–422]. Present as established, not as this book's stance.
4. Levins's brute-force passage [@levins1966strategy, p. 421] — three reasons a faithful one-to-one model fails. Lead with **uninterpretable**, not with cost. Collapse 2 defeated here.
5. Three boundary questions on the anchor: are customer responses inside? is the emergency interconnection inside? is the pump's power supply inside? Work the second in full — including it creates an alternative that otherwise cannot exist.
6. Widening enables new questions [@astrom2008feedback, p. 29]; the cut can change the internal description [@astrom2008feedback, p. 33].
7. Narrow boundaries hide distal consequences [@sterman2006evidence].
8. **Self-explanation pause 1.** Why is the boundary a decision rather than a discovery? Answer before reading on.
9. **Reader task.** One defended inclusion, one defended exclusion, for a stated purpose. Then: which of the two changes under the other purpose?

## 7. Section 3 — Parts, Roles, and State

**Purpose.** Populate the boundary and identify what must be carried forward.

**Beats.**

1. Parts and what they do [@machamer2000mechanisms, p. 3]. Entities defined by role, not substance.
2. The **role table** as the chapter's standing artifact: part / what it does / role (carried forward, acted on from outside, observed) / grain.
3. Roles are assigned within a representation, not read off the world. The same quantity takes different roles in different representations.
4. `state` introduced with the purpose-qualified definition [@astrom2008feedback, p. 34]. Quote it.
5. **The state test.** A quantity recomputable from others, or irrelevant to what comes next, is not state. Collapse 5 defeated here.
6. Work the three non-examples from `case-data.md`: forecast temperature, pump flow rate, and — the instructive one — **total system storage**, which was the state in Chapter 1 and is not state here.
7. Grain as a decision [@astrom2008feedback, p. 34]. Zone-level versus property-level for this purpose.
8. Explicit handoff: Chapter 13 supplies the laws by which state moves; Chapter 2 stops at what must be carried.
9. **Reader task.** Complete the role table; apply the state test to two candidates, one of which fails.

## 8. Section 4 — Mechanism

**Purpose.** Draw a mechanism and know exactly what drawing it established.

**Beats.**

1. Minimal formulation [@craver2026mechanisms, §2]. Parts, activities and interactions, organization, responsible for the phenomenon.
2. Phenomenon-relativity [@craver2026mechanisms, §2.1.1, §5.1]. You cannot draw *the* mechanism of a system, only the mechanism of a stated phenomenon. Collapse 10 held off here.
3. State the generalisation explicitly: sources say *phenomenon*; this book extends to *stated purpose*; that extension is the book's pedagogical synthesis.
4. Name the phenomenon for the anchor: *Hillcrest loses pressure first.*
5. Draw **Mechanism A** (pump capacity) in prose and diagram.
6. Draw **Mechanism B** (old undersized feeder main). Both from supplied facts. Both could produce it.
7. **The four-sign check** [@machamer2000mechanisms, pp. 3, 18; @craver2026mechanisms, §3.3]: an arrow with no nameable activity; a black box; could-produce not does-produce; no intervention has tested it.
8. Intervention is the evidence, not the diagram [@machamer2000mechanisms, p. 17]. Association alone is insufficient [@pearl2009causal]. Collapse 4 defeated here.
9. The loyalty-app contrast: two mechanisms drawable in opposite directions for one association. Non-numeric, two paragraphs.
10. **Self-explanation pause 2.** What would have to happen before you could write "the pump is the reason"? Answer before reading on.
11. Handoff to Chapter 7 in one sentence. Do not teach identification.

## 9. Section 5 — Leaving Out, Making Up, Lumping Together

**Purpose.** The heaviest conceptual section. Three distinctions, each with a reader task.

**Beats.**

1. **Abstraction is omission.** Silent, asserts nothing false [@weisberg2007idealization, fn. 14; @frigg2025models, §1]. Attribute to Jones (2005) via both reports; say it is one defensible position, not consensus.
2. **Idealization is asserting something false.**
3. **The asymmetry of defence.** Omission is defended by irrelevance to the question. Distortion must be defended by tolerability of the induced error. The second is harder. This is the section's core.
4. Work both on the anchor: zone-level demand (omission) versus instantaneous lossless transfer (distortion).
5. **Abstraction is not generality** [@machamer2000mechanisms, p. 16]. Quote it. Collapse 11 defeated here. Two dials, not one.
6. The pendulum contrast — two purposes, two entity sets. Two sentences, no more.
7. **Aggregation.** Representational, made before any data exist. State the Chapter 4 boundary in the same paragraph the word first appears. Collapse 6 defeated here.
8. **The aggregation demonstration.** The reader computes: aggregate view (9.9 ML, ~9 days to reserve, nothing urgent) then zone view (0.6 ÷ 0.9 ≈ 16 hours). Present as a task, then the worked answer. Decision 0009 clause 6.3 requires the reader to produce this arithmetic.
9. The targeting demonstration: uniform 10% saves 0.9 ML system-wide but 0.09 ML in Hillcrest. The aggregate representation cannot pose the question.
10. **Self-explanation pause 3.** The aggregate arithmetic was correct. Why did it mislead?
11. Levins's map analogy [@levins1966strategy, p. 423]. On a map you know which features carry meaning; in a model often not. Collapse 7 supported here.
12. Grain, resolution, fidelity, scale as ordinary careful language. Explicitly refuse `level`.

## 10. Section 6 — Three Representations

**Purpose.** Consolidation and comparison. Fading begins.

**Beats.**

1. Lay out three representations of one utility: **storage-only** (Chapter 1), **treatment-and-demand**, **network by zone**.
2. Three purposes: will we breach the reserve in seven days; can we raise output enough and at what cost; who loses service first.
3. A 3×3 adequacy table. Each cell says *what this representation can and cannot answer for this purpose*. Not a scoring matrix.
4. State the flip explicitly: the storage-only representation is adequate for purpose 1 and inadequate for purpose 3, and its arithmetic was never wrong. Collapses 1 and 8 defeated here.
5. Tie to [@levins1966strategy, p. 422]: the same simplification, legitimate for one question and not another. Quote the constant-environment case.
6. **The plan's own representation.** The drought plan has a system-wide reserve and no zone trigger, because a plan can only contain triggers its representation can express. Present as a consequence of representation, never as negligence.
7. Robustness [@levins1966strategy, p. 423]: a conclusion surviving across differently simplified representations is more trustworthy. Quote "our truth is the intersection of independent lies" with its caution.
8. Collapse 12: revising a representation when the purpose changes is correct practice, not a confession.
9. **Planted-defect diagnosis task.** Five defects per `spec.md`. Reader diagnoses, states consequence, repairs. Feedback lives in a separate file and is linked only after production.

## 11. Section 7 — Cold-Start Practice and Retrieval

**Purpose.** Independent production, retrieval, delayed retest.

**Beats.**

1. Return to the §1 opening attempt. Compare against what the reader can now produce. Do not score.
2. **Cold transfer.** Link exactly one assigned form. State plainly that the other form must not be opened.
3. **Retrieval from memory.** Reconstruct the representation checklist before checking it.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form, per the `../../decisions/0008` pilot window.
6. Close: what Chapter 3 asks next — whether the quantities in the representation are well measured.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before the production task. The delayed form is never linked in §7.

## 12. Citation slots

Every section carries at least one verified locator. Sections 2, 4, 5, and 6 carry the load-bearing citations listed in `spec.md`.

`weisberg2007idealization` locators are **preprint section headings**. Any citation of it must survive conversion to printed *Journal of Philosophy* pages before freeze; prefer citing it alongside `frigg2025models` §1, which is stable.

## 13. What the draft may not do

- Introduce notation of any kind.
- Present a general boundary-selection procedure as sourced.
- Cite a source for representational aggregation.
- Teach feedback, equilibrium, stability, or evolution laws.
- Say a mechanism is established.
- Assert durable far transfer.
- Present synthetic case values as typical, standard, or recommended.
