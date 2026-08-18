# Pilot Protocol

Status: **provisional.** Built on [Decision 0025](../decisions/0025-validation-architecture.md), **PROPOSED and not author-adjudicated**.

One protocol for any chapter. Chapter-specific values are read from that chapter's own files at run time rather than restated here, so that this file cannot drift away from the manuscript.

**For Chapter 1, use [`../chapters/01-decisions-questions/pilot-protocol.md`](../chapters/01-decisions-questions/pilot-protocol.md) instead.** It is more detailed, it is what Chapter 1's gates are written against, and it is the instance this file generalises from.

## 1. What the pilot is for

To find out whether the chapter can be worked as designed: whether the budget is approximately right, whether the exercises can be completed without the answers leaking, and whether readers systematically misread anything.

**It is not a transfer study.** No arrangement in this directory can establish that the book produces durable far transfer, and no output of it may be reported as though it had.

## 2. Before the session — parameters to read

For chapter *N*, read these from the chapter's own directory and write them on the run sheet:

| Parameter | Where it is |
|---|---|
| page and hour budget | `spec.md` frontmatter, `pages_target` and `hours_target` |
| number of sections | `chapter.md`, the `## N.` headings |
| the three self-explanation pauses | `chapter.md`, the `### Pause` headings — **every chapter has exactly three** |
| opening task and its time allowance | `chapter.md` §1 |
| planted-defect diagnosis task | `chapter.md`, usually the penultimate section |
| transfer form time allowance | `transfer-form-a.md`, stated in its opening line |
| which form is assigned | `transfer.md` |
| **rubric mode** | `transfer-rubric.md` — see §6 |

Ranges across the book, for planning: **18–40 pages, 4–8 learning hours, 6–8 sections, exactly 3 pauses, 30–60 minutes of transfer production.**

## 3. Freezing the version

Record the **exact commit hash** of the manuscript the participant reads. A pilot run against an unrecorded version establishes nothing, because a later edit cannot then be distinguished from a reader effect.

## 4. Form-order assignment

Each chapter has two parallel cold-transfer forms. Assign **A first and B at retest** for odd-numbered participants, **B first and A at retest** for even-numbered ones.

The forms are **selected for pilot, not established as equivalent**. Any comparison between a Form A result and a Form B result is confounded with form until enough participants exist to separate them, and no such number of participants exists yet.

**The second form must remain unseen until the retest.** If a participant opens it early, record the contamination and treat the retest as void rather than discarding the participant.

## 5. Session 1

### 5.1 Start conditions

Chapter unread. No prior exposure to the case. Rubric, worked solutions, diagnosis feedback, and the unassigned form all unavailable — on paper or on screen.

### 5.2 The opening attempt

Every chapter opens with an unaided task before it has taught anything. Administer it at the chapter's stated allowance, and **preserve the response verbatim and unscored**.

This artifact is used twice: once at the end of the chapter, and — for Chapter 1's — once again at Chapter 16. `../decisions/0023` clause 5 records that it must stay unscored, because scoring it later would change retrospectively what was preserved.

### 5.3 Reading

Time each section separately. Record navigation behaviour: re-reading, skipping, going back to the case data, consulting an earlier chapter.

**Do not intervene.** A reader who is stuck is data.

### 5.4 The three pauses

At each self-explanation pause, capture the response before the chapter's own answer is read. Then record whether the reader's answer changed after reading it, and how.

The three pauses are the chapter's main instrument for whether the reasoning landed. **A pause that every reader answers correctly on first attempt is not necessarily working** — it may be too easy to be diagnostic, and that is a finding.

### 5.5 The planted-defect diagnosis task

Every chapter plants five defects in a supplied piece of work. Capture the reader's diagnosis **before** the feedback file is opened.

Record, per defect: found, not found, or **mis-diagnosed** — the third being the interesting case, and the one that says something about the chapter rather than about the reader.

### 5.6 Cold-transfer production

Assigned form only, at its stated allowance, from that page alone. No chapter, no case, no rubric, no other form.

Record actual completion time against the allowance. **Preserve the original response before any revision.**

### 5.7 After production — the rubric

Only now is the rubric opened. See §6 for what to record, which depends on the chapter.

### 5.8 Retrieval from memory

Chapter closed. The reader reconstructs the chapter's structure from memory. Record what is recovered, what is missing, and what is recalled in the wrong relation to something else.

### 5.9 Debrief

Where they got stuck, what felt like busywork, what they would have wanted earlier, and whether anything read as condescending or as unreasonably hard.

## 6. Two rubric modes — read this before recording anything

**The book has two assessment instruments**, and which one a chapter uses changes what can be recorded. [Decision 0025](../decisions/0025-validation-architecture.md) clause 4 records that this discontinuity is undecided.

### Mode S — scored (Chapters 1–11)

The rubric supplies dimensions marked **0, 1, 2**. Record the dimension-level marks.

**Do not total them.** Every scored rubric in the book states that there is no validated aggregate cut score, and producing one in a pilot would manufacture the number the chapters refuse to supply.

Record **major category errors** separately from dimension marks. Each scored rubric lists its own.

### Mode U — unscored (Chapters 12–17)

The rubric states that nothing is scored and nothing is recorded. **Honour that at the level of the instrument and record observations instead.**

For each element the rubric discusses, record one of: **present**, **absent**, **present but wrong**, or **not attempted** — and a verbatim fragment of the reader's own text as evidence. No marks, no scale, no total.

If a reader asks how they did, the answer is the rubric's own: it is a review instrument, not a mark scheme.

### Consequence for comparison

**Mode S and Mode U results cannot be compared with each other.** A pilot that samples Chapters 1, 8, 12, and 16 produces two S results and two U results, and the difference between them is an instrument difference before it is anything else.

## 7. Session 2 — the delayed retest

Between **7 and 14 days** after Session 1. The reader does not reread the chapter beforehand, and the unassigned form is opened for the first time.

Same procedure as §5.6–5.7. Preserve the delayed response before any revision, and record the actual delay in days — not the intended one.

## 8. What the pilot may and may not support

**May support** author decisions about: whether the hour budget is roughly right; whether the opening task earns its place; whether all three pauses are distinct in value; whether the transfer allowance is feasible; whether a rubric element is repeatedly weak; whether a planted defect is undetectable or mis-stated; whether a form is harder than its parallel.

**Does not by itself establish**: that the chapter teaches transfer; that the two forms are equivalent; that the budgets generalise beyond these participants; that a weak dimension reflects the reader rather than the chapter; or that a chapter is ready to freeze.

## 9. Revision triggers

Treat as a signal worth acting on, not as proof:

- reading time **more than 50% over** the stated budget for two or more participants;
- a pause that no participant can answer, or that every participant answers without thinking;
- a planted defect that no participant finds, **or one that participants find for the wrong reason** — the second being worse;
- a transfer form that cannot be completed in its allowance by anyone;
- the same rubric element weak across participants **and** forms;
- any participant reporting that they answered from the water case rather than from the transfer domain.

## 10. After each wave

For each material finding, separate: **observed evidence**, **interpretation**, **author decision**, **scope of change**, **follow-up evidence needed**. Interpretation is not evidence, and a decision recorded without its evidence is not adjudication.

Then update [gate-status.md](gate-status.md) — and nothing else — for gate status.
