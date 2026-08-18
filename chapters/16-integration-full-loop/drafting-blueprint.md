# Chapter 16 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0023`, three of whose clauses need author attention.

## 1. Drafting objective

26 pages / 6 learning hours that leave the reader able to route an unfamiliar problem, defend the negatives, and revise a completed stage when a later one undermines it.

The chapter must **defeat** twelve named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Words |
|---|---|---:|
| 1 | Fifteen Chapters and a Problem Nobody Has Framed | 1,080 |
| 2 | Triage | 1,440 |
| 3 | A Tool That Scores Repairs | 1,440 |
| 4 | Working It: What Turned Out to Matter | 1,800 |
| 5 | Two Times It Sent Us Backwards | 1,440 |
| 6 | A Problem That Needs Four Chapters | 1,080 |
| 7 | What Is Still Unresolved | 360 |
| 8 | Cold-Start Practice and Retrieval | 720 |

About **9,360 words**. The shortest chapter since Chapter 9, and appropriate: this chapter has no machinery to explain.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the cases.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **No new notation.** The sixth chapter in seven to add none.
- **No quotation may contain a comparison symbol.**
- **`masonsingh2016categorization` is cited by named section, never by page.**
- **`chi1993classic` is cited without a locator**, because it is one page.
- Every figure the chapter reports appears in `case-data.md`.

### Register discipline

Five failure modes specific to this chapter.

**Sounding like a summary.** The temptation in a final-integration chapter is to recapitulate fifteen chapters. **The chapter must not.** Every reference to an earlier chapter should be a *use*, not a reminder, and if a sentence would still make sense with the chapter number removed, it is a reminder.

**Sounding like a method.** Triage is a habit with a written output, not a procedure with steps. A numbered method would reintroduce the waterfall the chapter exists to defeat.

**Sounding congratulatory.** The reader has finished fifteen chapters and the chapter must not tell them what they can now do. **`../../decisions/0023` clause 5.4 forbids any claim of transfer**, and the honest position is that the book has given them a procedure and a baseline to check themselves against.

**Sounding like an AI chapter.** Problem A is a stress test. Every finding traces to an existing chapter, and the manuscript carries the table proving it.

**Overreading a thin source.** The chapter's central empirical claim comes from a one-page commentary on an unobtainable paper about eight students. **Every hedge the author wrote travels with it**, and §2 must not read as though the finding were settled.

## 4. Reader-facing sequence

Per `../../decisions/0008`. Three pauses: §2 (route it yourself), §4 (which number would you check?), §6 (how many chapters?).

## 5. Section 1 — Fifteen Chapters and a Problem Nobody Has Framed

**Beats.**

1. Pick up Chapter 15's closing question directly.
2. Say what has changed: fifteen chapters supplied machinery, and nobody has yet had to choose.
3. **Say plainly what this chapter does not do**: it adds nothing. Say why that makes it the hardest chapter to write and possibly the most useful.
4. **The water case leaves.** Say so, and say why: a chapter about unfamiliar problems cannot be taught on the most familiar one. It will be referred to and not reworked.
5. **Opening task, about fifteen minutes.** Give Problem A's situation from `case-data.md` §§1–5 — everything except the routing record and the revisions. Ask: **which parts of this book does this need, and which does it not?** Ask for reasons on both. **Preserve unscored.**
6. Note that the answer is in §3 and §4 and that the reader should not skip forward.

## 6. Section 2 — Triage

**Beats.**

1. Name the activity. **`triage`**, and its distinctness from doing a bit of everything.
2. **The finding**, from [@chi1993classic] — the abstract quoted, with the provenance stated in the same breath: this is the author's own retrospective, the paper could not be obtained.
3. Chi's account: novices sorted problems that looked alike; experts did not; novices sorted by the concrete objects.
4. **`surface feature`** and **`deep structure`**, defined.
5. **The hedge, quoted** — "however one characterizes 'deep'" and "we continue to elaborate".
6. **Now the replication.** Eight students [@masonsingh2016categorization, Introduction]. The replicating authors' refusal to run statistics on that sample. The wider distribution. And "it is not appropriate to call all introductory students novices".
7. **What survives and what does not.** The distinction survives; the population claim does not. **And say why this is better for the reader** than the tidy version: the chapter is not telling them they are novices, and Chapter 1's preserved baseline lets each reader check for themselves.
8. **The citation count, and the refusal to use it.** 375 citations is influence, and Chapter 9 established that agreement among dependent sources is cheap.
9. **In this book the deep structures are the fifteen chapters.** State that this application is the book's own.
10. **`materiality`** and the negative finding. `../01-decisions-questions/spec.md`'s category error quoted.
11. **`routing record`.** One row per stage, a judgment, and a reason — **including on the negative rows, which are the interesting part.**
12. **Self-explanation pause 1.** Go back to your §1 answer and mark which rows have reasons.

## 7. Section 3 — A Tool That Scores Repairs

**Beats.**

1. Problem A stated in full, from `case-data.md` §§1–5.
2. **The board minute records the 84% and not the 61%.** Note it and move on; §4 returns to it.
3. **The routing record**, from `case-data.md` §6, as a table.
4. **Eleven of fourteen material**, and immediately: **this is unusual**, and it is why this case was chosen.
5. **The three negatives, with their reasons**, given more space than the positives. Chapter 6, Chapter 9, Chapter 12 — and why each is genuinely not material rather than merely unexamined.
6. **Say what the routing record is not**: a plan, an order, or a commitment.
7. **And say what the governed architecture says about AI here** — an application and a stress test — with the observation that every row of the table names an ordinary chapter.

## 8. Section 4 — Working It: What Turned Out to Matter

**Beats.**

1. Work the material stages in **the order the problem dictates**, not the book's, and say so.
2. **Chapter 4 first**, not Chapter 1: the 2020 volume, and what the labels are.
3. **Chapter 3**: what a score of 70 stands for.
4. **Chapter 8**: the 84% and the 61%, as two numbers about different things.
5. **Self-explanation pause 2.** Given emergencies up 22% and statutory referrals up 3.1%, which number would you check next?
6. **Chapter 5**: the rival explanation.
7. **Chapter 13**: the emergency queue as a stock against fixed capacity.
8. **Chapter 15**: the payment differential, and the rising share.
9. **Chapter 10 and 11**, briskly: whose objective, and whether a larger re-inspection is worth commissioning.
10. **Chapter 14**: this is a policy, and the state it needs is not observable.
11. **Do not resolve the case.** §7 says what is unresolved, and a tidy ending would teach the wrong thing.

## 9. Section 5 — Two Times It Sent Us Backwards

**Beats.**

1. **`backward revision`**, defined, and immediately distinguished from Chapter 5's criticism.
2. **Revision 1**: trigger, what it revised, and that both earlier answers were reasonable.
3. **Name its kind**: a revision about what the target was.
4. **Revision 2**: trigger, what it revised, and that the interval was not wrong but was about a period.
5. **Name its kind**: a revision about an answer having gone stale.
6. **The two are different**, and the manuscript says how.
7. **Quote Chapter 1's own spec** on the waterfall category error, and note that this is the demonstration it asked for.
8. **And the discipline**: revision is evidence-triggered. A revision performed because the method says to revise is not one.

## 10. Section 6 — A Problem That Needs Four Chapters

**Beats.**

1. Problem B stated, from `case-data.md` §§8–9.
2. **Self-explanation pause 3.** How many of the fifteen does this need? Write a number before reading on.
3. **Four**, and the routing record from `case-data.md` §10.
4. **Chapter 4's row** — why the two November years exist — and that this is the whole finding.
5. **Chapter 8's row**: two observations against a spread of 0.34.
6. **Chapter 11's row**: £4,800 against £11,800.
7. **Chapter 7's negative row, given its own paragraph.** Not material *because* a randomised split test is available — the easy case Chapter 7 identified.
8. **Four of fifteen and the analysis is complete.** This is the common shape, and Problem A is not.
9. **Reader task.** Name a stage you would add to Problem B and say what evidence would justify it.

## 11. Section 7 — What Is Still Unresolved

**Beats.**

1. Problem A is not resolved and the chapter does not resolve it.
2. List what is open: whether the tool should be kept, what the re-inspection would show, what the contractor's contract should say.
3. **And say that this is what the end of a real analysis looks like.**
4. **Sort the open items into two kinds**: open because nobody has done the work, and open because they are somebody's decision.
5. **Planted-defect diagnosis task.** Five defects. **One of them routes correctly and stops**, which is the failure a reader of this chapter is most likely to commit. Feedback linked only after production.

## 12. Section 8 — Cold-Start Practice and Retrieval

**Beats.**

1. **The Chapter 1 comparison.** Retrieve the preserved artifact. **Do not score it.** Say why not, quoting Chapter 1's own spec.
2. Three things to look for, none of them a mark.
3. **Cold transfer.** Both forms listed, one assigned.
4. **Retrieval from memory** — the procedure, five steps.
5. Rubric linked **after** production only.
6. **Delayed retest** on the other form.
7. Short diagnostic if the transfer went badly.
8. **What this chapter did not give you** — and here it is short, because the chapter gave no machinery.
9. **What the book cannot claim.** No transfer claim, no pilot data, and the sentence every chapter has carried.
10. Close: Chapter 17 asks what happens after the thing is deployed and somebody has to notice it going wrong.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production.

## 13. What the draft may not do

- Introduce any machinery, notation, technique, or vocabulary beyond the six controlled terms.
- Teach anything about artificial intelligence, machine learning, or model evaluation.
- Rework the water anchor.
- Recapitulate earlier chapters. Every cross-reference must be a use.
- Present triage as a numbered method.
- Score the Chapter 1 comparison, or introduce any score.
- Claim that this book produces transfer, or that the reader has acquired anything by reading.
- Present the surface/structure finding as settled, or as a fact about the reader.
- Use the 375-citation figure as corroboration.
- Cite `masonsingh2016categorization` by page, or `chi1993classic` with a locator.
- Claim anything about Chi, Feltovich and Glaser (1981) beyond what the commentary states.
- Resolve Problem A.
- Treat monitoring, drift, or post-deployment revision.
