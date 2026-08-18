# Chapter 5 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0012-chapter5-criticism-terminology-and-boundary.md`.

## 1. Drafting objective

27 pages / 5 learning hours that leave the reader able to hand someone a written criticism in which every item names what would settle it, and at least one item could reverse the recommendation.

The chapter must **defeat** twelve named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | What Would Have Shown It | 2 | 0.25 |
| 2 | Adequate for What, at What Risk | 4 | 0.75 |
| 3 | Four Cheap Checks | 6 | 1.10 |
| 4 | Alternatives and Exclusions | 5 | 0.95 |
| 5 | When You Cannot Find Out | 4 | 0.70 |
| 6 | Criticizing Part I | 3 | 0.65 |
| 7 | Cold-Start Practice and Retrieval | 3 | 0.60 |

Roughly 360 words per page. Do not rebalance without recording the reason.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **No notation. No formulas beyond arithmetic.**
- Citations use Pandoc syntax with locators. `platt1964strong` may be cited **only to p. 348**. The three credibility sources may be cited only at their inspected extents.
- When the book generalises beyond a source, say so in the sentence that does it.

### Register discipline

This chapter criticizes four chapters the reader has just worked through, and it is easy to make that read as though the earlier chapters were sloppy. **They were not.** Every step in Part I was correct given what was available. The chapter's point is that correct steps are not enough, not that the steps were wrong. If a paragraph reads as an exposé of the book's own earlier work, rewrite it.

Equally: the chapter must not be a lecture about intellectual humility. Humility is not the skill. Naming what would settle a question is.

## 4. Reader-facing sequence

Per `../../decisions/0008`. No new case; the anchor is the accumulated Part I analysis.

Self-explanation pauses: exactly three — §3 (what makes a check worth doing), §3 (the nursery), §5 (the no-experiment case).

## 5. Section 1 — What Would Have Shown It

**Purpose.** Land the handoff and produce an unscaffolded baseline.

**Beats.**

1. Recall Chapter 4's closing observation: every failure in Part I had a specific observation that would have revealed it, and nobody made it.
2. List the four, one line each — the biased transmitter, the aggregate that could not express *who*, the sensor measuring the wrong place, the residual that was never measured.
3. Note that each was found by a different chapter's machinery, and that nobody had a way to go looking.
4. **Opening task, about seven minutes.** What would have to be true for Part I's conclusion about Hillcrest to be right? List it. Preserve unscored.
5. Close on the chapter's question, and state plainly that Chapter 5 introduces no new case — it turns on what is already there.

**Do not** introduce adequacy, verification, or any Chapter 5 vocabulary here.

## 6. Section 2 — Adequate for What, at What Risk

**Beats.**

1. Open on the unqualified question: *is this analysis any good?* By now the reader should distrust the form.
2. `adequacy` developed from Chapter 1's placeholder: adequate **for a stated use, at a stated accuracy, for a stated quantity**.
3. Sourced: validation is meaningful "for specified quantities of interest" and relative to "the accuracy required for an intended use" [@nrc2012reliability, Summary p. 3].
4. **Adequacy is not accuracy** [@fda2023credibility, §VI.D p. 33] — quantifiable accuracy is one thing; whether the total evidence is sufficient for the context of use, given model risk, is another. Collapse 5 defeated here.
5. Work it on the anchor: what Part I's analysis is adequate for, and the four things it is not.
6. **What governs how much criticism is enough: what happens if you are wrong.** [@fda2023credibility, §VI.D p. 33; @nrc2012reliability, ch. 6 §§6.1–6.2, pp. 86–87]. Collapse 12 defeated here.
7. Work the consequence for the anchor: a zone below threshold on a hot evening. A service consequence, not a safety event. State what that bounds.
8. **Verification and validation** [@asme2025credibility, slides 5–7]: *did I do the thing right* versus *did I do the right thing*. Collapse 3 defeated here.
9. **Reopen the Chapter 3 collision explicitly.** Chapter 3 declined `validation` because measurement validation and model validation are different practices. Chapter 5 is where the second belongs; say so, say why the word is now available, and move on. Once only.
10. Note that these frameworks are written for regulated computational simulation and that what transfers is the structure of the judgment, not the apparatus.
11. **Reader task.** State what the analysis is adequate for and what would change the answer.

## 7. Section 3 — Four Cheap Checks

**Purpose.** The chapter's most useful section and its best argument.

**Beats.**

1. Frame: four checks, none needing data you do not have, all runnable in minutes.
2. State the sourcing honestly, once: none of the four is cited to a source in this book, and each is demonstrated instead so the reader can verify it.
3. **Dimensional.** `0.6 ML ÷ 0.9 ML/day = 0.67 days`. What it catches: a quotient without units. Note Chapter 3's deliberate choice of metres of head.
4. **Limiting case.** Set Hillcrest consumption to zero; the residual stays positive. **This flags Chapter 4's entire finding in a minute.** Say so plainly, and say what it does not do — it raised the alarm; Chapter 4's investigation produced the explanation. Clause 4.4 and 4.5 of the decision record.
5. **Extreme condition.** Set demand to zero; storage rises without bound. No spill term, against a stated **1.2 ML** tank and **14.0 ML** system. Harmless for the question asked, wrong for any refill question.
6. **Self-explanation pause 1.** What makes a check worth running? Answer before reading on. The answer is that it could have come out the other way — the Chapter 3 lesson recurring. Collapse 6 defeated here.
7. **Order of magnitude — the centrepiece.** Reader produces the arithmetic: **340** properties (Ch 3), **0.62 ML/day** (Ch 4), `620,000 ÷ 340 = 1,824 L per property per day` against a bounding `150 × 2.5 = 375`. **About five times too high.**
8. Ask the reader to generate the three candidate explanations before revealing any.
9. **Reveal the nursery**: one connection, **0.40 ML/day**, leaving `0.22 ÷ 339 ≈ 649 L/day` for the rest — plausible for large-plot properties in a heatwave.
10. **Self-explanation pause 2.** The nursery is about **65%** of Hillcrest's consumption. Four chapters never saw it. Why not?
11. **The payoff.** The nursery is one account, on a contract, whose irrigation is schedulable. That is an alternative Part I never produced. Tie to Chapter 2 — a representation can only contain the alternatives it can express — and to Chapter 4 — the billing system knew.
12. Close: the cheapest check in the book found the option the expensive machinery missed. That is an argument for running them **first**, not for skipping the machinery.

## 8. Section 4 — Alternatives and Exclusions

**Beats.**

1. Name the problem the section solves: the reader now has criticisms and no way to tell a real one from a worry.
2. **The method** [@platt1964strong, p. 347], quoted: devise alternative hypotheses; devise something with alternative outcomes that would exclude one or more; carry it out; recycle.
3. **The line**, quoted: "Any conclusion that is not an exclusion is insecure and must be rechecked" [@platt1964strong, p. 347]. Connect backwards to Chapter 3 (an interpretation never at risk was never supported) and Chapter 4 (the surviving data is the subset the process kept).
4. Why it does not happen: "we do busywork. We become 'method-oriented' rather than 'problem-oriented'" [@platt1964strong, p. 348]. Collapse 1 defeated here.
5. **`assumption record`**, and the correction: naming an assumption does not handle it. Collapse 2 defeated here.
6. **The template**, from Jacob and Monod [@platt1964strong, p. 348]: *our conclusion might be invalid if (i), (ii), or (iii); here is what would eliminate each.* Give it as the artifact to produce.
7. Work it on the anchor: three assumptions, each with what would show it false.
8. **`rival model`.** Instruments of criticism, not options. Collapse 7 defeated here.
9. Work Chapter 2's Mechanism A and B — still unresolved after three chapters. Name the discriminating observation, which Chapter 2 already named and nobody made.
10. **`structural uncertainty`**, distinguished from being unsure of a number. Flag the `structural identifiability` collision in one clause. Collapse 9 defeated here.
11. Robustness as criticism [@levins1966strategy, p. 423], with the Chapter 12 boundary stated in the same paragraph.
12. **Reader task.** An assumption record, each entry with its discriminating observation.

## 9. Section 5 — When You Cannot Find Out

**Purpose.** The chapter's honesty section, and the book's own contribution.

**Beats.**

1. State the problem: the method assumes you can run the crucial experiment. A utility cannot rerun a drought.
2. What survives — devising alternatives, naming what would discriminate. What does not — getting the clean result.
3. **Step 4, marked as the book's own addition:** if you cannot make the observation, say so, and say what your conclusion is resting on.
4. Insist this is a **result**, not a failure. *This conclusion rests on something we have not excluded and cannot currently exclude* is a stronger output than a confident answer.
5. **Self-explanation pause 3.** Mechanism A and B have been open since Chapter 2. Is that a failure of Part I?
6. Work the anchor's unobtainable cases and its obtainable ones — and note that the pump test *is* obtainable and simply was not done, which is a different problem from impossibility.
7. Name the Chapter 11 boundary: Chapter 5 names the discriminating observation; whether it is worth acquiring is a separate question with its own machinery.
8. **"All models are wrong" and what it is not a licence for** [@sterman2002models, p. 505] — the passage pairs recognising limits with expanding boundaries and taking responsibility. Collapse 8 defeated here.
9. Collapse 10: a predicted failure mode is not a prevented one.

## 10. Section 6 — Criticizing Part I

**Beats.**

1. Assemble the criticism of the whole Part I analysis: what it is adequate for, what the four checks found, what the assumption record contains, what remains unexcluded.
2. State the one item capable of reversing the recommendation — the nursery, which changes the option set.
3. **The five-chapter pattern**, stated once and labelled as the book's own observation.
4. **Planted-defect diagnosis task.** Five defects per `spec.md`.
5. **Chapter 8 placement task.** Four situations, one of which is a sensitivity analysis offered as criticism. Collapse 11 defeated here.
6. Close Part I: the reader can now frame, represent, measure, trace, and criticize. Part II asks what evidence can establish.

## 11. Section 7 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 opening list. Compare, do not score. Name the common patterns.
2. Explain the changed task shape: **you are the reviewer, not the analyst.** A four-chapter analysis cannot be built in forty minutes, so one is supplied.
3. **Cold transfer.** Link exactly one assigned form.
4. **Retrieval from memory** before checking.
5. Rubric linked **after** production only.
6. **Delayed retest** on the other form.
7. Short diagnostic if the transfer went badly.
8. Close: Part I ends; Chapter 6 begins Part II.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production. The delayed form is never linked in §7.

## 12. What the draft may not do

- Cite `platt1964strong` beyond p. 348, or characterize the literature debating it.
- Cite the credibility sources beyond their inspected extents.
- Cite any source for the four cheap checks.
- Present step 4 of the method as anything but the book's own.
- Teach uncertainty quantification, sensitivity methods, identification, value of information, or robustness formalism.
- Imply Chapters 1–4 contained errors.
- Imply any health or safety consequence of low pressure.
- Present the five-chapter pattern as established.
- Present synthetic case values as typical, standard, or recommended.
- Suggest the nursery could certainly be rescheduled. It is an option to investigate.
