# Chapter 5 Transfer Design

Status: governed design source for the Chapter 5 cold-transfer forms.

**Contains answer commentary for both transfer forms. Do not read this file if you intend to complete the Chapter 5 transfer exercises**; use the reader copies `transfer-form-a.md` and `transfer-form-b.md`, which the manuscript links at the right moment.

Where a reader copy conflicts with this file, this file controls.

## Transfer target

> Given a completed analysis and its recommendation, produce a written criticism that names at least one order-of-magnitude or dimensional problem, one behaviour the formulation implies at a limit or extreme that cannot be right, one load-bearing assumption the analysis does not state, and one rival explanation that would reverse the recommendation — and for each, name the observation that would settle it, or say that none is available.

## The changed task shape

Chapters 1–4 asked the reader to **build** something. Chapter 5's competence is criticizing a completed analysis, and a four-chapter analysis cannot be built in forty minutes.

So the forms supply one. **The reader is the reviewer, not the analyst**, and the manuscript says so explicitly before linking a form.

This is a deliberate departure from the Part I pattern and should be watched in piloting: readers trained by four chapters to produce may attempt to rebuild rather than criticize. The rubric treats rebuilding as a major category error.

## Form design

| | Form A | Form B |
|---|---|---|
| Domain | Council recycling centre closure | Clinic appointment reminders |
| Character | Physical / operational | Institutional |
| Recommendation | Close the Western site | Switch from post to SMS |
| **Size defect** | 90,000 visits/year against a site capacity of ~49,920 | 42,000 letters for 9,500 appointments |
| **Limit defect** | Queue formula returns a **negative** wait when arrivals exceed capacity | Model implies non-attendance reaches **0%** at full coverage |
| **Unstated assumption** | Displaced users travel to Northgate rather than stopping | Non-attendance is caused by forgetting |
| **Reversing rival** | Low tonnage reflects **restricted opening hours**, not low demand | Patients who miss most appointments are **least likely to have a mobile recorded** |

Each form contains exactly four planted defects, one per technique, plus supplied facts that make each findable without domain knowledge.

### Domain exclusions

Every previously used domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records.

## What a strong Form A answer should notice

**The size defect, worked.** Western opens four days a week, eight hours a day: `4 × 52 × 8 = 1,664` hours a year. Two bays at four minutes a visit gives `2 × 15 = 30` visits an hour, so at most `1,664 × 30 = 49,920` visits a year. The analysis claims **90,000** — about **1.8×** the site's physical maximum. Either the visit figure is wrong or the bay or duration figures are.

**The limit defect, and its link to the size defect.** The supplied formula *W = q ÷ (c − q)* gives a **negative** waiting time whenever arrivals exceed capacity. With the claimed 54 visits/hour against 30, it returns −2.25 minutes. A negative wait is not a small error; it is a signal that the formula is being used outside its range. Strong answers connect this to the size defect — they are the same problem seen twice.

**The unstated assumption.** "Displaced users will use Northgate" is asserted in the conclusion and never examined. If some stop recycling or fly-tip instead, the tonnage does not transfer; it disappears, and the environmental case reverses. The form supplies that fly-tipping records exist in a separate system and were not consulted — that is the discriminating observation, and it is **available now**.

**The reversing rival.** Western has the lowest tonnage and the analysis reads this as low demand. But **Western opens four days a week and the others open six.** Low tonnage may reflect restricted availability rather than low need — and the form adds that Western is the only site serving the two largest estates without a river crossing. If demand is suppressed rather than absent, Western is the *wrong* site to close, and closing it displaces the least mobile users furthest.

**Item 5.** The rival is the correct answer. It is the only item that changes which site should close rather than how the case is presented.

## What a strong Form B answer should notice

**The size defect.** `42,000 ÷ 9,500 = 4.4` letters per appointment. Either multiple reminders are sent per appointment — which the analysis never says, and which changes the cost saving — or one of the figures is wrong. The form supplies that some patients attend two hospitals and receive letters from each, which is a partial but insufficient explanation.

**The limit defect.** Non-attendance reaching **0%** at full SMS coverage requires that *every* missed appointment is caused by forgetting. The form supplies the staff survey listing transport, work or caring commitments, illness on the day, and not knowing the appointment had been made — four reasons an SMS does not address. A model whose limit is zero has assumed a single cause.

**The unstated assumption.** "Non-attendance is driven by patients forgetting" is asserted as established and is the load-bearing claim of the whole analysis. The records do not capture why appointments were missed, so the clinic has never had evidence for it. The staff survey is the nearest available observation and points the other way.

**The reversing rival, and the form's hardest item.** Mobile numbers are recorded for **71%** of patients overall but only **44%** of those who missed two or more appointments. SMS therefore reaches the group that misses fewest appointments and misses the group that misses most — so the switch could *increase* non-attendance while appearing to succeed on the covered population.

**Register discipline on that item.** The correct reading is **structural**: the difference is about whether a number is *recorded*, and registration happens at a desk in the main entrance, which is itself a barrier. Nothing in this form supports, and the rubric penalises, any inference about the character, motivation, or reliability of patients who miss appointments. This is Chapter 4's lesson recurring — the data records an interaction with a system, not a property of a person.

**Item 5.** The rival again. It is the only item that could make the recommendation actively harmful rather than merely overstated.

## Parallelism check

Both forms supply: a competently written one-page analysis; a figure that fails a single division; a formula or model with an impossible limit; one load-bearing assumption asserted but never established; one reversing rival readable from two supplied facts; and at least one discriminating observation that is **available now** rather than hypothetical.

Both also reward the same discipline: neither analysis is incompetent, and a response whose finding is that the author was careless has missed the structural problems.

## Ethical note on Form B

Form B concerns clinic non-attendance. It was written so that:

- the reversing rival turns on **whether a phone number was recorded**, not on patients' behaviour or character;
- the registration barrier is supplied as a structural fact;
- the staff survey lists reasons that are circumstantial — transport, caring, illness — rather than attitudinal;
- the clinic and its staff are portrayed as acting reasonably;
- no supplied fact invites an inference about individuals.

**The form has not been reviewed by anyone with clinical or health-services expertise.** `spec.md` records this as an open question. If a reviewer judges the domain unsuitable, the form should be **replaced rather than softened** — a version that avoids the difficulty by making the case less real would not teach the same thing.

## Pilot notes

- Target duration **40 minutes**, a design parameter pending pilot evidence.
- Form order counterbalanced (A→B and B→A), per `../../decisions/0008`.
- Record prior familiarity with local-government operations and with healthcare administration before the first task.
- The delayed form must not be previewed.
- **Watch for readers who rebuild rather than criticize.** Given four chapters of building, this is the most likely failure and the most informative to code.
- Also code whether item 5 is answered at all. Prioritising criticisms is the part most likely to be dropped under time pressure, and it is the part that distinguishes a review from a list.
