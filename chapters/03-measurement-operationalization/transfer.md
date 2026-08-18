# Chapter 3 Transfer Design

Status: governed design source for the Chapter 3 cold-transfer forms.

**Contains answer commentary for both transfer forms. Do not read this file if you intend to complete the Chapter 3 transfer exercises**; use the reader copies `transfer-form-a.md` and `transfer-form-b.md`, which the manuscript links at the right moment.

Where a reader copy conflicts with this file, this file controls.

## Transfer target

> Given an unfamiliar construct and a decision it must support, produce a defensible operationalization, state what the resulting scores can and cannot be interpreted as, identify one systematic offset that repetition will not remove, and place one supplied item on the line between "the number is wrong" and "the wrong numbers exist".

## Form design

Two parallel forms, one physical/technical and one institutional, following the pattern governed by `../../decisions/0005`.

| | Form A | Form B |
|---|---|---|
| Domain | Indoor air quality in a school | Hospital emergency department waiting time |
| Character | Physical / technical | Institutional |
| Construct | Air adequate for occupancy | How long patients wait |
| Current working definition | Corridor CO₂ below 1,000 ppm during teaching hours | Registration to first clinician contact |
| The definition's hidden decision | Measures the corridor, which nobody is taught in | Starts the clock after the patient already waited |
| Systematic offset | Sensor reads **80 ppm low**; and the corridor is not a classroom | Recorded start is a median **19 minutes** after physical arrival, **31** in the evening |
| Proxy | CO₂ standing in for ventilation adequacy generally | Registration timestamp standing in for arrival time |
| Proxy failure condition | Pollutants not produced by breathing — solvents, toner, traffic particulates | Exactly when the department is busiest |
| Chapter 4 item | No sensor in any classroom | Patients who leave before registering appear nowhere |
| Mixed boundary item | Sensor sited where the power outlet was | Timestamp generated where the desk and terminal are |

Both demand the same five structural outputs. Only the surface domain differs.

### Domain exclusions

Every earlier transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment (Chapters 1–2), regional blood supply, city rental assistance (Chapter 2).

## What a strong Form A answer should notice

- The construct is air adequate for **occupants**, and the measure is in a space that is occupied only between lessons. The mismatch is the whole case.
- Room 12 at **1,640 ppm** against a corridor reading of **780 ppm** is the disagreement, and it should be stated as numbers rather than described.
- The sensor offset runs the **wrong way for safety**: reading 80 ppm low means true corridor concentration is nearer 860 ppm, so the margin against 1,000 ppm is smaller than it appears. Readers who spot the offset but not its direction have done half the work.
- **Two distinct failures are present and should be separated.** The 80 ppm offset is an instrument problem. The corridor location is an operationalization problem. Conflating them is the most common expected error.
- The proxy point is that CO₂ tracks human-generated pollution. Traffic particulates from the road outside are supplied precisely so that a strong answer can name a circumstance where the substitution breaks.
- Hourly logging cannot see a lesson-length build-up in a closed room.
- "No record is kept of which windows are open" is supplied as an invitation to say what is missing rather than to assume it.
- The mixed boundary item is the power outlet.

## What a strong Form B answer should notice

- The clock starts at registration, so the measure **cannot see the interval it is most needed for**. The recorded 42-minute median plus a 19-minute pre-registration median gives roughly **61 minutes** of actual waiting — and the arithmetic should be produced, not gestured at.
- **The offset is not constant**, and this is the form's hardest and most valuable observation. It rises to **31 minutes** in the evening. So the recorded figures understate evening waits *more* than daytime waits — which is precisely the comparison Purpose 2 depends on. A reader who treats the offset as a uniform 19 minutes has missed the thing that changes the decision.
- Recording more patients under the same definition never removes this. Every patient's clock starts late.
- Registration-to-departure at **171 minutes** versus registration-to-first-contact at **42** shows how much the choice of endpoint moves the number.
- Triage by a nurse not counting as "first clinician contact" is a rung-two decision with real consequences, supplied for readers who look.
- Patients leaving before registration are a **Chapter 4** matter, not Chapter 3: nothing is wrong with the numbers that exist.
- The mixed boundary item is the desk-and-terminal location.
- Synchronised clocks are supplied as a deliberate distractor: the timing infrastructure is excellent, and the measure is still wrong. A reader who concludes the clocks are the problem has confused precision with trueness.

## Parallelism check

Both forms supply: a construct that sounds settled and is not; a current working definition that silently decides where, when, and how much; a systematic offset in a stated direction; a proxy whose failure is structured; one clean Chapter 4 item; and one genuinely mixed boundary item.

Both also supply at least one distractor — the portable meter's reference-gas check in Form A, the synchronised clocks in Form B — so that a reader who reaches for "the instruments are unreliable" finds that they are not.

## Known weakness

Form B's subject matter sits closer to Chapter 4 than Form A's, because waiting-time records are produced by an administrative process. The form is written to keep the required outputs on the Chapter 3 side and gives the provenance item explicitly to Chapter 4, but this is a real asymmetry between the two forms and is recorded as `spec.md` open question 5.

## Pilot notes

- Target duration **40 minutes**, a design parameter pending pilot evidence.
- Form order counterbalanced (A→B and B→A), per `../../decisions/0008`.
- Record prior familiarity with school facilities management and with hospital operations before the first task.
- The delayed form must not be previewed.
- **Neither form has been checked by a subject-matter expert.** One concerns a school and one a hospital. Both use only supplied facts and require no specialist knowledge, but a careless implication about children's air quality or about emergency care would matter more than in the earlier chapters' domains. See `spec.md`, open question 9.
