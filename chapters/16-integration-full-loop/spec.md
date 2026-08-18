---
chapter: 16
part: 5
title: "Integration: The Full Loop on Unfamiliar Problems"
status: drafted
pages_target: 26
hours_target: 6
---

# Chapter 16: Integration: The Full Loop on Unfamiliar Problems

**Provisional.** Built on proposed `../../decisions/0023-chapter16-integration-terminology-and-boundary.md` and inheriting its status. **Three of that record's clauses need author attention.**

## Central question

Which machinery does this problem need, and how do the pieces connect?

*Governed by `README.md`. Not amendable here.*

## Core competence

Triage unfamiliar problems and execute the relevant reasoning process across formulation, evidence, decision, dynamics, and strategy without mechanically forcing every problem through every chapter.

*Governed by `README.md`. Not amendable here.*

**The Chapter 16 block also carries a content requirement no other chapter block carries**: "This chapter should eventually contain full-loop cases, including at least one substantial automated or AI system case. AI is an application and stress test, not a separate intellectual foundation of the book." **Met by Problem A**; see `../../decisions/0023` clause 3.

## Role in the book

Chapter 16 opens Part V and is the first chapter since Chapter 1 that adds no machinery.

**Its unique job:**

> Teach readers to decide which of fifteen chapters a problem needs, to record what they judged **not** material and why, and to go back when the work tells them to.

It discharges four promises Chapter 1 made about itself, of which two are structural: the preserved baseline artifact is compared here, and the "worked demonstration of two distinct backward revisions" is placed here.

## Hard prerequisites

All fifteen preceding chapters. **This is the only chapter in the book of which that is true**, and it is why the chapter sits where it does.

## Soft dependencies / spiral links

- Chapter 1's exit artifact, preserved unscored since the first chapter.
- Chapter 5's model criticism, from which backward revision must be distinguished.
- Chapter 8's discipline about small samples, applied here to one of the chapter's own sources.
- Chapter 9's finding that agreement among dependent sources is cheap, applied here to a citation count.

## Established concepts to cover

Triage. Materiality, and the negative finding. Surface features against deep structure. The routing record. Backward revision, in two kinds. The book's fifteen chapters as a set of categories to sort into.

## Terminology to introduce or stabilize

**Introduced:** `triage`, `materiality`, `backward revision`, `surface feature`, `deep structure`, `routing record`.

**Four of the six are the book's own controlled terms.**

**No collision requiring announcement** — the first chapter since Chapter 5 with none.

**Two entries carry flags**: `surface feature` and `deep structure` rest on a finding whose primary paper could not be obtained. `../../decisions/0023` clause 7.

## Interfaces with other chapters

| Chapter | Interface |
|---|---|
| 1 | supplies the preserved baseline and four promises; Chapter 16 is the same task without scaffolding |
| 5 | supplies criticism, from which backward revision is distinguished |
| 8 | supplies the discipline applied here to a source with eight subjects |
| 9 | supplies the dependence finding applied here to a citation count |
| All 2–15 | supply the categories the triage sorts into |
| 17 | owns whether a deployed thing is still working |

## Scope boundary

### Core

Triage of two unfamiliar problems, with reasons on the negative rows. Two worked backward revisions, distinct in kind. The surface/structure distinction, with its replication. The Chapter 1 baseline comparison, unscored.

### Deferred to Chapter 17

Monitoring design, drift diagnosis, revision after deployment, governance.

### Deferred to depth curriculum

**Nothing**, because nothing in this chapter is new. What it defers is what every earlier chapter deferred.

### Not taught at all

Anything about artificial intelligence, machine learning, or model evaluation as subjects. Per `README.md`, AI here is an application and a stress test.

## Section architecture

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | Fifteen Chapters and a Problem Nobody Has Framed | 3 | 0.70 |
| 2 | Triage | 4 | 0.95 |
| 3 | A Tool That Scores Repairs | 4 | 0.95 |
| 4 | Working It: What Turned Out to Matter | 5 | 1.15 |
| 5 | Two Times It Sent Us Backwards | 4 | 0.95 |
| 6 | A Problem That Needs Four Chapters | 3 | 0.70 |
| 7 | What Is Still Unresolved | 1 | 0.25 |
| 8 | Cold-Start Practice and Retrieval | 2 | 0.35 |

Eight sections, 26 pages, 6 hours. Roughly 360 words per page — about **9,360 words**.

Three self-explanation pauses: §2 (route it yourself), §4 (which number would you check?), §6 (how many chapters?).

## Examples / recurring cases

**Two problems, neither of them the water anchor** — the first chapter since Chapter 1 of which that is true. Frozen in `case-data.md`.

**Problem A**, an automated repairs-triage tool, meets the governed AI requirement and is material to eleven of fourteen chapters.

**Problem B**, an appeal-timing decision, is material to four of fifteen.

**The water case is referred to and not reworked.**

## Exercise architecture

Per `../../decisions/0008`. **The opening task is the Chapter 1 baseline comparison and is not scored** — see `../../decisions/0023` clause 5.

Three pauses; five-defect diagnosis; cold transfer on two parallel forms; retrieval from memory; delayed retest.

## Transfer target

> Given two unfamiliar problems — one an automated system, one a small decision — produce a routing record for each with a reason on every row including the negatives, work the material stages far enough to reach a finding, identify at least one fact that changes the routing once noticed, and say what remains unresolved.

### Parallel forms

- **Form A — a rail operator's automated delay-attribution system, and a station-signage decision.**
- **Form B — a helpline's automated call-triage model, and a newsletter send-day decision.**

**Each form contains two problems**, one automated and one thin, so that both halves of the discrimination are tested twice.

Every prior transfer and contrast domain is excluded. Neither domain is sensitive.

Chapter 16 must not claim durable far transfer. **No chapter may, and this one least of all** — see `../../decisions/0023` clause 5.4.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| Experts abstract principles; novices work from literal surface features | `chi1993classic` |
| Novices sorted problems that looked alike; experts did not | `chi1993classic` |
| The characterisation of "deep" was still being elaborated | `chi1993classic` |
| Replicated across domains, with "deep" acknowledged as unsettled | `chi1993classic` |
| The classic study used eight introductory students | `masonsingh2016categorization` |
| A much wider distribution of expertise among introductory students | `masonsingh2016categorization` |
| It is not appropriate to call all introductory students novices | `masonsingh2016categorization` |

### Used at existing depth

`butler2010transfer` and `schwartz2011contrasting`, both abstract-verified for Chapter 1, with Chapter 1's cautions intact. **No upgrade claimed**, after failed attempts on both.

### Not cited

Chi, Feltovich and Glaser (1981) — **not obtained**. Any AI or machine-learning source — **not sought, by architecture**.

## Failure modes this chapter should prevent

1. Triage means doing a bit of everything.
2. A "not material" finding is a gap.
3. The book's order is the working order.
4. Backward revision means the earlier work was wrong.
5. More chapters applied means a better analysis.
6. Triage can be completed from the problem statement alone.
7. Experts triage correctly because they are careful.
8. Novices are simply wrong.
9. An AI system needs AI-specific machinery.
10. The triage output is a list of chapter numbers.
11. A citation count is corroboration.
12. Reading this book has produced transfer.

## Open questions

1. **Decision 0023 is unadjudicated**, as are 0009–0022, and three of its clauses need specific attention.
2. **The research base is the smallest since Chapter 1** — clause 4 — and the manuscript says so.
3. **The pagination exception is applied a second time** — clause 6 — and falls if `0022` clause 8 is declined.
4. **The central empirical warrant is a commentary, not the study** — clause 7.
5. **No pilot data exists for any transfer form in this book.**
6. **Gate 1 remains open**, fifteen chapters deep, and this chapter does not deepen it — Chapter 16 is the first chapter since Chapter 1 whose case is not the anchor Gate 1 concerns.
