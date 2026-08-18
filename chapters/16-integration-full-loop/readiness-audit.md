# Chapter 16 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 16: **Integration: The Full Loop on Unfamiliar Problems** — the first chapter of Part V.

**Process note.** As in Chapters 3–15, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **Which machinery does this problem need, and how do the pieces connect?**
- core competence: **Triage unfamiliar problems and execute the relevant reasoning process across formulation, evidence, decision, dynamics, and strategy without mechanically forcing every problem through every chapter.**
- target: 26 pages / 6 serious learning hours.
- **`README.md` adds a content requirement no other chapter block carries**: "This chapter should eventually contain full-loop cases, including at least one substantial automated or AI system case. AI is an application and stress test, not a separate intellectual foundation of the book."

## 1. Readiness verdict

**Drafting-ready after adjudication**, and it is a different kind of chapter from the fourteen before it.

Five observations.

**This chapter adds no machinery, and that is its subject.** Chapters 2–15 each introduced a body of reasoning. Chapter 16 introduces none. Its intellectual content is the fifteen chapters already written, and its competence is knowing which of them a problem needs.

**Its research is therefore legitimately lighter, and the audit says so rather than padding it.** What Chapter 16 needs from outside the book is a warrant for one empirical claim — that people sort problems by surface features until they know enough to sort by structure — and a caution that the claim is less tidy than it is usually presented. Two sources cover that. Chapters 2–15 needed three or four each because they were teaching something; this one is not.

**The governed block imposes a content requirement.** At least one substantial automated or AI system case, with the standing that AI is an application and a stress test rather than a foundation. That is a specification, and the chapter must meet it.

**Two structural promises from Chapter 1 come due here**, and both are unusual.

`../01-decisions-questions/spec.md` L492: the Chapter 1 exit artifact "is retained and repeated after Chapter 5 and in Chapter 16 to measure improvement in cold-start reasoning." **The reader's first unaided attempt, preserved for fifteen chapters, is compared here.**

And L582 names, among the book's major category errors, "**Mechanically applying every stage to every problem**", with the remedy assigned to Chapter 16: "Require relevance justification and allow explicit 'not material here' findings."

**The book's own teaching order is a hazard this chapter has to defuse.** `../01-decisions-questions/spec.md` L582 also names "Treating the teaching order as a real-world waterfall", with the remedy assigned to Chapters 16 and 17: "Worked demonstration of two distinct backward revisions."

## 2. Unique-job hypothesis

> Teach readers to decide which of fifteen chapters a problem needs, to record what they judged **not** material and why, and to go back when the work tells them to.

The reader who finishes Chapter 16 should be able to take a problem nobody has framed, produce a routing decision with reasons on both sides, work the relevant parts in an order the problem dictates rather than the order the book taught, revise a completed stage when a later stage undermines it, and say what remains unresolved.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `01/spec.md` L189 | "Chapter 1 is heavily scaffolded; Chapter 16 requires **independent triage and repeated backward revision**" | §§2, 5 |
| `01/spec.md` L492 | the exit artifact "is retained and repeated... in Chapter 16 to measure improvement in cold-start reasoning" | §8 |
| `01/spec.md` L582 | "Mechanically applying every stage to every problem... Require relevance justification and allow explicit 'not material here' findings" | §§2, 4 |
| `01/spec.md` L582 | "Treating the teaching order as a real-world waterfall... Worked demonstration of two distinct backward revisions" | §5 |
| `02/spec.md` L152 | "Chapter 2 is heavily scaffolded; **independent triage is Chapter 16**" | §2 |
| `15/chapter.md` L1025 | "Chapter 16 puts an unfamiliar problem in front of you and asks the question this book has been building toward: which of the fifteen chapters does this need?" | the whole chapter |
| `README.md` Ch16 block | "at least one substantial automated or AI system case" | §§3–6 |

**Only six chapters defer here explicitly, which is fewer than Chapters 7, 9, 14, or 15.** That is not a shortfall: every chapter defers here implicitly, because every chapter's machinery is a candidate for the triage.

## 4. Neighbouring-chapter boundaries

### Chapter 1 — the same task, without the scaffolding

Chapter 1 walked the reader through a complete pass with the stages named and the order given. **Chapter 16 gives neither.** The comparison between the two attempts is the measurement Chapter 1 set up, and it is the only longitudinal instrument in the book.

### Chapter 5 — criticism

Chapter 5 criticised what four chapters had built. **Chapter 16's backward revisions are not criticism**; they are the ordinary consequence of finding something at stage seven that changes stage two. The distinction must be held, or the chapter reads as a second Chapter 5.

### Chapter 17 — deployment

Chapter 17 asks whether a deployed thing is still working. **Chapter 16 stops at the point of deployment**, and its AI case must not drift into monitoring design.

### The depth curriculum

Nothing in this chapter is deferred to the depth curriculum, because nothing in this chapter is new. What it defers is the same material every earlier chapter deferred.

## 5. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `triage` | new | the book's own controlled use |
| `materiality` | new | the book's own; the "not material here" finding |
| `backward revision` | new as a controlled term | the book's own; `../../decisions/0008` implies it |
| `surface feature` / `deep structure` | new | `chi1993classic` |
| `routing record` | new | the book's own |

**Five terms, four of which are the book's own.** The lightest terminology load of any chapter after Chapter 1, and appropriate for a chapter that adds no machinery.

**No collision requiring announcement.** The first chapter since Chapter 5 with none.

## 6. High-risk conceptual collapses to prevent

1. **Triage means doing a bit of everything.** It means deciding, with reasons, and recording the negatives.
2. **A "not material" finding is a gap.** It is a finding, and it should be written down with its reason.
3. **The book's order is the working order.** It is a teaching order. Two backward revisions demonstrate the difference.
4. **Backward revision means the earlier work was wrong.** It usually means the earlier work was right about a question that turned out not to be the question.
5. **More chapters applied means a better analysis.** The chapter's second problem needs four.
6. **Triage can be done from the problem statement alone.** Both revisions in the worked case are triggered by things found during the work.
7. **Experts triage correctly because they are careful.** `chi1993classic` says they sort by different features, not more carefully.
8. **Novices are simply wrong.** `masonsingh2016categorization` found a much wider distribution than the classic study, and says calling all beginners novices is not appropriate.
9. **An AI system needs AI-specific machinery.** The governed block says AI is an application and a stress test. The case is worked with the book's existing chapters.
10. **The triage output is a list of chapters.** It is a list of questions with reasons, and the chapter numbers are shorthand.

## 7. Research clusters

1. **How people categorise unfamiliar problems.**
2. **How much of that result survives replication.**
3. **Transfer, and what the book may claim about its own.**
4. **The cases, the two backward revisions, and exercise design.**

## 8. Candidate example constraints

**This is the first chapter since Chapter 1 in which the water anchor is not the case**, and that is deliberate: a chapter about unfamiliar problems cannot be taught on the book's most familiar one.

Constraints:

- **The substantial case must be an automated or AI system**, per the governed block.
- It must **touch most of the book**, because that is what makes it substantial — and the chapter must say plainly that this is unusual.
- **A second, deliberately thin problem is required**, needing four or five chapters, so that the "not material" finding has something to land on.
- The two backward revisions must be **evidence-triggered and distinct in kind** — one about what the target was, one about the data-generating process changing.
- **No new machinery may appear anywhere.** Every move must be traceable to a chapter the reader has read.
- The water case may be **referred to and not reworked**.

**Gate 1 remains open and is now thirteen chapters deep** — and it is worth noting that Chapter 16 is the first chapter whose case is not the anchor Gate 1 is about.

## 9. Decisions likely required after research

1. **Whether the chapter's lighter research base is acceptable**, and whether it should be stated to the reader. Recommend **yes to both**.
2. **How the AI case is scoped** so that it is a stress test rather than a new subject. Recommend: every finding traced to an existing chapter, and a table showing which.
3. **How "not material" findings are recorded.** Recommend a routing record with a reason column, and that the reasons be the interesting part.
4. **Whether the Chapter 1 baseline comparison is scored.** Recommend **no** — it has been unscored since Chapter 1 and changing that now would invalidate the comparison.
5. **How the Chi finding is presented given the replication.** Recommend both, in that order, with the complication given its own paragraph.
6. **Whether any new notation is added.** Recommend **none**; four of the last five chapters added none.

## 10. Drafting gate

Do not draft until:

- `../../decisions/0023` exists in proposed form;
- the terminology block is written;
- `case-data.md` freezes both problems and **every figure is computed and checked**;
- `spec.md` records how the governed AI-case requirement is met and how the two backward revisions are placed.
