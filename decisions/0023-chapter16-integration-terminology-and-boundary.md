# Decision 0023: Chapter 16 Integration Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §9 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

**Three clauses need author attention.**

- **Clause 4** records that this chapter's research base is the smallest since Chapter 1, deliberately, and proposes that the manuscript say so to the reader.
- **Clause 6** applies the bounded pagination exception proposed at `0022` clause 8 **for a second time**, and makes the dependency explicit.
- **Clause 7** records that the chapter's central empirical warrant is an author's retrospective commentary rather than the study it describes.

Evidence base: `../chapters/16-integration-full-loop/research-01-how-people-triage.md`, `research-02-how-well-it-replicates.md`, `research-03-transfer-and-what-may-be-claimed.md`, `research-04-cases-revisions-and-exercises.md`.

## Decision

Chapter 16's organizing claim is:

> The competence this book was written to build is not the fifteen bodies of machinery. It is deciding which of them a problem needs, recording what you judged not material and why, and going back when the work tells you to.

### 1. This chapter adds no machinery, and that is its subject

**1.1** Chapters 2 to 15 each introduced a body of reasoning. **Chapter 16 introduces none.**

**1.2** **Every move in the chapter is traceable to a chapter the reader has read**, and the manuscript carries a routing table showing which.

**1.3** No new notation. **Five of the last six chapters have added none**, and this one has no candidate.

### 2. Triage, and the negative finding

**2.1** `../chapters/01-decisions-questions/spec.md` L582 names "Mechanically applying every stage to every problem" as one of the book's major category errors, with the remedy assigned here: "Require relevance justification and allow explicit 'not material here' findings."

**2.2** **The chapter's central instrument is a routing record** with a reason column, and **the reasons on the negative rows are the interesting part.**

**2.3** **A "not material" finding without a reason is indistinguishable from an omission**, and the manuscript says so.

**2.4** The chapter's two problems are chosen for contrast: **eleven of fourteen chapters material** on the substantial one, **four of fifteen** on the thin one. **The manuscript states that the first is unusual and the second is the common shape.**

### 3. The governed AI requirement, and how it is met

**3.1** `README.md`'s Chapter 16 block requires "at least one substantial automated or AI system case", with the standing that "AI is an application and stress test, not a separate intellectual foundation of the book."

**3.2** **The requirement is met by Problem A**, an automated repairs-triage tool.

**3.3** **No AI-specific machinery is taught and no AI or machine-learning source is cited.** `research-plan.md` records this as a deliberate consequence of the governed block rather than an oversight, so that the absence of such a source does not read as a gap.

**3.4** **Held-out accuracy appears in the case as something the system's builders reported**, not as a technique the chapter teaches.

**3.5** The case is a **stress test**: it is chosen because it puts pressure on the book's existing chapters, and it does — eleven of them are material.

### 4. A smaller research base, stated rather than disguised

**4.1 This clause needs author attention.**

**4.2** Chapters 7 to 15 each rested on three or four load-bearing sources. **Chapter 16 rests on two**, plus two already in the bibliography used at their existing depth.

**4.3** **This is proposed as correct rather than as a shortfall.** The chapter's authority comes from the book's own fifteen chapters. What it needs from outside is a warrant for one empirical claim and a check on how well that claim has held up, and two sources supply both.

**4.4** **The manuscript says so to the reader**, in one paragraph, rather than leaving a reader who counts citations to wonder.

**4.5** If the author disagrees, the honest response is to commission more research rather than to cite more sources for claims the chapter does not make.

### 5. The Chapter 1 baseline comparison stays unscored

**5.1** `../chapters/01-decisions-questions/spec.md` L492 records that the Chapter 1 exit artifact "is retained and repeated after Chapter 5 and in Chapter 16 to measure improvement in cold-start reasoning."

**5.2** **It is the only longitudinal instrument in this book**, and it is a within-reader comparison rather than a claim about readers.

**5.3** **It stays unscored.** Chapter 1's spec records the exit task as "diagnostic rather than a major book transfer gate" with "no validated numerical cut score". **Introducing a score fifteen chapters later would change retrospectively what the preserved artifact was**, and would invalidate the comparison it was preserved for.

**5.4** **No claim of transfer is made anywhere in the chapter.** `research-03` records that neither transfer source has been read in full and that no pilot data exists for any form in this book.

### 6. The pagination exception, applied a second time

**6.1 This clause needs author attention.**

**6.2** `0022` clause 8 proposed a **bounded** exception to the standing rule adopted in Chapter 9 — cite the version whose pagination you can see — allowing a source with no printed page numbers to be cited by numbered section.

**6.3** **`masonsingh2016categorization` is the second application.** It carries no printed page numbers and is cited by named section — Abstract, Introduction, Conclusions.

**6.4 The dependency is explicit: if the author declines `0022` clause 8, this application falls with it**, and Chapter 16 reverts to paraphrase without locators for that source.

**6.5** **`chi1993classic` is not an application of the exception.** It is one page, so the document is the locator, and nothing is lost.

**6.6** **One source was obtained and declined to keep the exception bounded.** The author's accepted manuscript of `schwartz2011contrasting` is readable and was not used, because the bibliography entry gives published page numbers the manuscript does not carry, and citing it by section would let a reader expect locators in a document the book has not read. **That is a stricter position than the exception requires, taken deliberately.**

### 7. The central warrant is a commentary, not the study

**7.1 This clause needs author attention.**

**7.2** The chapter's claim about how people categorise unfamiliar problems comes from Chi, Feltovich and Glaser (1981). **That paper could not be obtained**, after three documented routes.

**7.3** What was obtained is [@chi1993classic], the first author's one-page retrospective, which reproduces the 1981 abstract verbatim.

**7.4** **This is the second time a chapter has rested a central claim on something other than the primary source**, after Chapter 14's `structural identifiability`, and the two are different: there the substitute was a peer-reviewed review by other authors; here it is the original author's own commentary, quoting her own abstract. **Neither is what the book prefers.**

**7.5** **The author's own hedges travel with the finding**, quoted: "however one characterizes 'deep'", and "we continue to elaborate on the characterization".

**7.6** **The citation count is not used as corroboration.** The commentary records 375 citations; Chapter 9 established that agreement among dependent sources is cheap, and the manuscript does not treat the number as evidence.

### 8. The replication is given equal standing

**8.1** [@masonsingh2016categorization] found "a much wider distribution of expertise among introductory students" and states that "it is not appropriate to call all introductory students novices as in the Chi study."

**8.2** **It also records what the classic study consisted of: eight introductory students.** Chapter 8 gave the reader everything needed to react to that, and the manuscript lets them.

**8.3** **What the replication changes is the population claim, not the distinction.** Surface and structure remain two bases for sorting.

**8.4 And this is better for the chapter than the tidy version.** The chapter is not telling readers they are novices. It is giving them a second basis for sorting and fifteen categories — and **whether they already sort that way is what Chapter 1's preserved baseline lets each reader check for themselves.**

**8.5** **Neither source may be used without the other**, and both source notes say so.

### 9. Two backward revisions, worked

**9.1** `../chapters/01-decisions-questions/spec.md` L582 names "Treating the teaching order as a real-world waterfall" as a major category error, with the remedy assigned to Chapters 16 and 17: "Worked demonstration of two distinct backward revisions."

**9.2** **Both are placed in Chapter 16**, both are evidence-triggered, and **they are distinct in kind**.

**9.3 Revision 1** is triggered at the identification stage and returns to Chapters 1 and 3: the tool predicts a scheduler's code, not a need. **A revision about what the target was.**

**9.4 Revision 2** is triggered at the strategic stage and returns to Chapter 8: the data arriving now comes from a process that was changing while it was measured. **A revision about an answer going stale.**

**9.5** **Neither is criticism in Chapter 5's sense**, and the manuscript holds the distinction: Chapter 5 criticised what four chapters had built; these are the ordinary consequence of finding at stage seven something that changes stage two.

### 10. Vocabulary

**10.1** Introduced here: `triage`, `materiality`, `backward revision`, `surface feature`, `deep structure`, `routing record`.

**10.2** **Four of the six are the book's own controlled terms**, which is appropriate for a chapter that adds no machinery.

**10.3** **No collision requiring announcement.** The first chapter since Chapter 5 with none.

**10.4** The registry's one remaining `TODO` — `utility`, belonging to the drafted Chapter 11 — is untouched.

### 11. What Chapter 16 does not do

- Introduce any machinery, notation, or technique.
- Teach anything about artificial intelligence, machine learning, or model evaluation.
- Rework the water anchor, which is referred to and not reopened.
- Score the Chapter 1 baseline comparison.
- Claim that this book produces transfer.
- Claim that the reader has acquired triage competence by reading.
- Present the surface/structure finding as settled, or as a fact about readers.
- Use a citation count as evidence.
- Treat backward revision as criticism.
- Treat monitoring or revision after deployment — Chapter 17.

## Sources promoted

`chi1993classic` and `masonsingh2016categorization` are new to `references.bib`. `butler2010transfer` and `schwartz2011contrasting` are **used at their existing Chapter 1 depth with their existing cautions**, after failed attempts to upgrade both.

## Known gaps carried forward

1. **Chi, Feltovich and Glaser (1981) not obtained** — clause 7. The chapter's principal gap.
2. **`masonsingh2016categorization` cited by section**, under an unadjudicated exception — clause 6.
3. **`butler2010transfer` and `schwartz2011contrasting` remain abstract-verified**, after failed upgrades; the Schwartz accepted manuscript was obtained and declined.
4. **No source supports the AI case's substance**, by architecture — clause 3.3.
5. **No pilot data exists for any transfer form in this book**, including this chapter's.
6. **The research base is the smallest since Chapter 1** — clause 4.
7. Both cases are synthetic, as every case in this book has been.
8. **The water anchor is not the case**, for the first time since Chapter 1, and Gate 1 remains open regardless.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields. It meets a content requirement the Chapter 16 block states and records how.
