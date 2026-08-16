# Chapter 1 Validation Handoff

Status: operational handoff for external SME review and learner pilot. This file does not change Chapter 1 claims, architecture, or scoring policy.

Use this document to launch the two evidence-producing activities that remain before Chapter 1 can be considered for freeze:

1. human drinking-water utility / engineering SME review;
2. timed reader + cold-transfer + delayed-retest pilot.

The detailed governing artifacts remain:

- `sme-review-water-anchor.md`;
- `pilot-protocol.md`;
- `pilot-data-capture.md`;
- `transfer-form-a.md`;
- `transfer-form-b.md`;
- `transfer-rubric.md`.

## A. Human SME handoff

### A1. Reviewer profile

Prefer a reviewer with practical experience in at least one of:

- drinking-water utility operations;
- storage/tank instrumentation or telemetry;
- treatment and pumping operations;
- drought/emergency operations;
- municipal water-system engineering.

The reviewer does not need to endorse the synthetic numbers as typical or recommended values.

### A2. Materials to send

Send, in this order:

1. `sme-review-water-anchor.md`;
2. `anchor.md`;
3. `case-data.md`;
4. `chapter.md`, with primary attention to Section 4.

Do not lead with the research history or the book-wide architecture unless the reviewer asks for it. The review question is narrow: whether the operating story and wording are plausible, natural, and free of unsafe or universal implications.

### A3. Suggested outreach message

> I am preparing an introductory reasoning chapter built around a deliberately synthetic municipal drinking-water case. I am not asking you to judge whether the numerical values are typical industry values. I would like you to review the operating story and wording for plausibility, natural utility/engineering language, hidden assumptions, and any accidental unsafe or universal implication. The attached review packet contains five focused questions and the exact case boundaries. Please mark the result as PASS, PASS WITH WORDING CHANGES, or REVISE MECHANISM, and note any sentence that should be changed before publication.

### A4. Requested reviewer output

Ask the SME to return:

- disposition: `PASS`, `PASS WITH WORDING CHANGES`, or `REVISE MECHANISM`;
- answers to the five questions in `sme-review-water-anchor.md`;
- sentence-level wording changes where possible;
- any hidden operational assumption that materially affects plausibility;
- any unsafe implication or wording that resembles universal guidance;
- confidence/limits of the reviewer's own expertise where relevant.

### A5. Author adjudication rule

Do not apply SME comments automatically.

For each comment record:

1. reviewer observation;
2. whether it concerns plausibility, safety, wording, or preference;
3. author interpretation;
4. decision: accept / modify / decline / investigate;
5. files affected;
6. whether the change touches a frozen synthetic fact or only wording.

A request to change a synthetic value merely because another value is more common is not automatically a defect. A comment that exposes an impossible mechanism, unsafe implication, or misleading operational relationship is materially different and may require reopening the case fact.

## B. Pilot launch

### B1. Freeze the pilot version

Before the first participant starts, record the exact Chapter 1 commit SHA in every participant data sheet.

Do not silently edit the manuscript between participants in the same comparison wave unless a defect makes the task unusable. If an emergency fix is required, end the current wave or record the version break explicitly.

### B2. Participant assignment

For an organized pilot, assign approximately balanced form orders:

- `A→B`: warehouse first, housing after delay;
- `B→A`: housing first, warehouse after delay.

Do not preview the delayed form.

Record prior familiarity with both transfer domains before the first transfer task.

### B3. Session 1 facilitator run sheet

Before start:

- create a participant copy of `pilot-data-capture.md`;
- record participant ID/pseudonym and assigned form order;
- record exact chapter commit SHA;
- keep `transfer-rubric.md`, `diagnosis-feedback.md`, and the delayed transfer form unavailable until their designated point;
- instruct the reader not to search external domain information.

During the session:

1. start total timing;
2. preserve the approximately 5-minute opening attempt;
3. record section-completion timestamps and meaningful interruptions;
4. preserve each of the three self-explanation responses before the explanation is read;
5. preserve planted-failure diagnosis before feedback is opened;
6. expose only the assigned first transfer form;
7. preserve the one-page transfer response before rubric access;
8. record eight rubric dimensions separately after production;
9. preserve post-task self-explanation;
10. capture retrieval from memory before the reader checks the chapter map;
11. complete the short reader debrief;
12. calculate, with appropriate caution, total time and active-production/retrieval share.

### B4. Session 1 contamination check

At session end verify:

- delayed form was not previewed;
- rubric was not visible during production;
- worked water solution was not consulted during cold transfer;
- no external domain lookup occurred, or any occurrence is recorded;
- original responses were preserved before revisions;
- interruptions were recorded rather than counted as instructional time.

### B5. Delayed retest scheduling

Schedule Session 2 for **7–14 days** after Session 1.

Record the exact planned date and actual elapsed days. The interval is a pilot parameter, not a universal spacing claim.

Before Session 2, do not ask the participant to reread Chapter 1.

### B6. Session 2 facilitator run sheet

1. confirm the second form was not previewed;
2. do not display the Chapter 1 map, rubric, first response, or feedback before production;
3. give the previously unseen form;
4. preserve the one-page response;
5. record completion time;
6. expose the same rubric only after production;
7. record all eight dimensions and major category errors;
8. preserve the post-task explanation;
9. record any spontaneous reconstruction of Chapter 1 relationships;
10. complete a short delayed-task debrief.

## C. Minimum evidence packet after one coherent pilot wave

Do not summarize only average totals.

The author adjudication packet should contain:

- exact manuscript commit used;
- participant/form-order table;
- total and section-level timing patterns;
- opening-attempt observations;
- self-explanation codes for all three pauses;
- recurring planted-failure omissions;
- transfer completion times;
- eight dimension-level patterns for first and delayed forms;
- major category errors;
- domain-familiarity notes;
- form/order differences;
- active-production/retrieval share;
- reader comments about ambiguity, repetition, hidden knowledge, and premature answer reveal;
- actual delay in days;
- a distinction between observed evidence and author interpretation.

## D. Stop conditions

Pause the pilot wave and repair the instrument/manuscript if a defect prevents meaningful interpretation, for example:

- a link reveals the unused transfer form or rubric early;
- supplied facts are contradictory;
- a task cannot be completed without unsupplied specialist knowledge;
- instructions direct different participants to materially different outputs;
- a file/version mismatch changes the task mid-wave;
- an SME identifies a potentially unsafe operating implication that is also present in the participant-facing manuscript.

Minor stylistic preferences should normally be recorded and adjudicated after the wave rather than changed participant by participant.

## E. What counts as progress from here

Chapter 1 should not accumulate additional internal artifacts merely to appear unfinished work is continuing.

Meaningful next evidence is one of:

- returned human SME review;
- completed Session 1 reader/transfer data;
- completed delayed retest data;
- author adjudication based on those data;
- final synchronization and freeze audit.

Until one of those exists, the current chapter remains a complete authored draft with external validation gates open.