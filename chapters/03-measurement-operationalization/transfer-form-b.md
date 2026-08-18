# Chapter 3 Cold-Transfer Task — Form B

Status: reader-delivery copy. Governed by `spec.md` (Transfer target) and `transfer.md`.

Without consulting the Chapter 3 chapter text, the water case, the checklist, or the rubric, work the situation below and produce the five outputs listed at the end.

Short written answers and simple arithmetic are the expected form. Every fact you need is supplied. Do not look anything up; if something you need is missing, say what it is and whether it would change your answer.

Current pilot target: **40 minutes**. This is a design parameter pending pilot evidence, not a universal standard.

## Form B — Hospital emergency department waiting time

### Situation

A hospital emergency department is deciding two things this quarter.

- **Purpose 1.** Report its waiting-time performance against a regional target.
- **Purpose 2.** Decide whether to fund an additional evening clinician, which requires knowing when during the day patients wait longest and how badly.

### The current arrangement

The regional target requires that **"patients should not wait too long."** The department operates to a written definition:

> Waiting time is the interval from **registration** to **first contact with a clinician**.

Both events produce a timestamp in the department's system, recorded to the second.

### Supplied facts

- Median recorded waiting time last quarter: **42 minutes**.
- Registration happens at a desk inside the entrance. A patient must reach the desk and give their details before a registration timestamp exists.
- A time-and-motion study commissioned last year followed 120 patients from the moment they physically entered the building. It found a median of **19 minutes** between physical arrival and registration.
- The same study found that the arrival-to-registration interval was **longer when the department was busier**, reaching a median of **31 minutes** during the evening period.
- Four other intervals could be recorded, and the system holds timestamps for all of them:
  - arrival at the desk → triage assessment;
  - registration → first clinician contact (the current definition);
  - registration → treatment decision;
  - registration → leaving the department.
- Median registration-to-treatment-decision last quarter: **95 minutes**. Median registration-to-departure: **171 minutes**.
- Patients who leave before reaching the registration desk produce no record of any kind.
- The department's clocks are synchronised nightly to a network time source.
- Triage assessment is performed by a nurse and is not counted as "first contact with a clinician" under the current definition.
- Nothing in the record indicates whether a patient was accompanied, or how they travelled.

### Produce

1. **The ladder.** State the construct, then write a working definition that would serve **Purpose 2**. Say explicitly what your definition decides about **where** the interval starts and ends, **when** it is measured, and **how much** counts as too long.
2. **Disagreement.** Using the supplied figures, show that the department's current working definition and yours give different answers. State the disagreement as numbers.
3. **The interpretation.** Write, in one sentence, what would have to be true for the recorded 42-minute median to support the claim "patients here wait 42 minutes". Then name one observation that would count against it.
4. **The offset.** Identify one systematic offset in the supplied measurements. State why recording more patients under the same definition would not remove it.
5. **The proxy, and the line.** Name what the registration timestamp is standing in for, and one circumstance in this department where the substitution would break worst. Then place each item below on the line between *the number is wrong* and *the wrong numbers exist*:
   - the recorded start is 19 minutes after the patient actually arrived;
   - patients who leave before registering appear nowhere in the data;
   - "waiting time" was defined as registration to first clinician contact;
   - registration is where the timestamp is generated because that is where the desk and the terminal are.

**Stop when your response is complete. Do not open the rubric until then, and do not open Form A at all.**
