# Research 01 — Two Processes: The World and the Record

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision. Written under the no-write boundary in `research-plan.md` §11.

Cluster R01 of `research-plan.md` §4. Research conducted 2026-08-18.

Sources inspected: `meng2018paradox` (pp. 685–687), `censusndtargetpopulation`, `davern2013nonresponse`.

## 1. Q1 — Naming and separating the two processes

### The unexpectedly strong finding

The separation Chapter 4 needs is not a conceptual framing this book has to invent. It appears as a formal object in the statistical literature, and it appears there as a **separate variable**.

`meng2018paradox` p. 685 decomposes the difference between a sample average and a population average into three terms. The first is:

> "a *data quality* measure, ρ_{R,X}, the correlation between X_j and the **response/recording indicator** R_j"

Read that carefully. For every unit *j* there are two quantities:

- **X_j** — the value in the world;
- **R_j** — whether that unit made it into your dataset.

Two variables, one per unit, from two different processes. And the thing that determines how badly your dataset misleads you is the **correlation between them**.

This is the two-process separation stated as mathematics, and it hands Chapter 4 the point that being recorded is itself something that happens to a unit, and can depend on the unit's value.

### Implication for naming

The literature's own word for R_j is the **recording indicator** or **response indicator**. That suggests the reader-facing term for the process generating it: the **recording process**, or — retaining the book's governed chapter title — the **observation process**.

The governed title uses *observation process*, so that term is fixed. What R01 recommends is that the manuscript introduce it concretely as *the process that decides which things get recorded*, rather than abstractly.

## 2. Q2 — What a record is, and what provenance involves

No inspected source defines `record` or `provenance` as terms of art. Recorded as a gap.

What the sources supply instead is a set of **decision points**, which is more useful at this depth than a definition.

`censusndtargetpopulation` §1.1 supplies the first: **eligibility**. The standard uses `target population` for the units about which inference is intended, and distinguishes target-population membership from the status of a sampled unit. So before anything is measured, something decides which units are even candidates for appearing.

`davern2013nonresponse` supplies the second: units that were candidates and did not respond.

`meng2018paradox` supplies the third and most general: whatever the mechanism, its effect is summarized by R_j.

### Recommended reader-facing treatment

Teach `provenance` as **the history of how a record came to exist** — who produced it, for what purpose, under what requirement — and note explicitly that this is not a metadata field. Do not treat it as controlled technical vocabulary, since no inspected source establishes one.

## 3. Q3 — What the separation buys, beyond Chapters 2 and 3

This matters, because a reader who has done Chapters 2 and 3 may reasonably think the ground is covered.

| Chapter | Question | What it cannot catch |
|---|---|---|
| 2 | What belongs in the representation? | A quantity correctly represented, whose records were produced by a process that skipped part of the system |
| 3 | Does this number mean what I think? | A number that means exactly what you think, for the units it covers |
| 4 | Why are these the records I have? | — |

The distinguishing case is the one Chapter 3 hands over: a demand figure that is arithmetically correct, produced by a defensible procedure, meaning precisely what it says — and existing only because certain meters were installed and others were not.

Chapters 2 and 3 examine what is in front of you. Chapter 4 asks what determined **what is in front of you**, which no amount of scrutiny of the present data can answer.

## 4. Q4 — Where the recording process can intervene

Consolidating the decision points the sources support, plus the ones the anchor case makes visible:

| Stage | The question | Sourced? |
|---|---|---|
| Eligibility | Which units could appear at all? | Yes — `censusndtargetpopulation` §1.1 |
| Coverage | Which eligible units were reachable by the instrument or frame? | Partly — implied by `meng2018paradox`'s N versus n |
| Response / capture | Which reachable units actually produced a record? | Yes — `davern2013nonresponse`; `meng2018paradox` R_j |
| Retention | Which captured records were kept? | No source |
| Reporting | Which retained records were passed on, and in what form? | No source |

**Three of five stages are unsourced.** Chapter 4 may teach all five, because they are observable features of the anchor case that a reader can verify on the page — but the manuscript must not imply that a cited framework establishes the five-stage list. It is the book's own enumeration.

## 5. Cautions — claims the manuscript must NOT make

1. Do not present the five-stage list as a sourced framework. Two stages are sourced; the enumeration is the book's own.
2. Do not present `provenance` as established technical vocabulary. No inspected source defines it.
3. Do not import Meng's identity as notation. Chapter 4 takes the *existence* of a recording indicator, not the algebra.
4. Do not describe R_j as "the observation process". R_j is an **indicator per unit** — whether that unit was recorded. The process is what generates it.
5. Do not imply that survey-methodology framing covers administrative or operational records automatically. Much of this literature assumes a sampling design that meters, logs, and filings never had.
6. Do not use `censusndtargetpopulation` beyond eligibility and target-population membership; its Chapter 1 note already limits it.

## 6. Verdict on the stop condition

`research-plan.md` §4 requires the separation stated in one reader-facing sentence, and the intervention points enumerated.

**Met.** Proposed sentence:

> Your dataset is the output of two processes, not one: the process you are trying to understand, and the separate process that decided which of its facts got written down.

Intervention points enumerated in §4, with sourcing status marked.

## 7. Unresolved author decisions

1. Is `observation process` used throughout, or is `recording process` clearer for administrative and operational records?
2. Is `provenance` reader-facing vocabulary, or is the idea carried by "where did this record come from"?
3. Are all five stages taught, given three are unsourced?
4. Is `record` registered, or left as an ordinary word?
5. Does the reader meet the idea that being recorded can **depend on the value** — the heart of ρ_{R,X} — early, or is it saved for the selection section?

Decision 5 is the consequential one. It is the chapter's key idea, and introducing it early risks the reader treating everything afterwards as a special case of it.
