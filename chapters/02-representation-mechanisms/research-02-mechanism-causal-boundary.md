# Research 02 — Mechanism and the Causal-Language Boundary

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision. Written under the no-write boundary in `research-plan.md` §12.

Cluster R02 of `research-plan.md` §5. Research conducted 2026-08-18.

Sources inspected: `machamer2000mechanisms` (primary, page-verified), `craver2026mechanisms` (reference survey), `pearl2009causal` (existing, Chapter 1).

## 1. Q1 — How `mechanism` is used across fields

### The 2000 formulation

`machamer2000mechanisms` p. 3 is the canonical statement:

> "Mechanisms are entities and activities organized such that they are productive of regular changes from start or set-up to finish or termination conditions."

with p. 3: "Activities are the producers of change. Entities are the things that engage in activities," and "The organization of these entities and activities determines the ways in which they produce the phenomenon."

Three components, all of which Chapter 2 wants anyway: **entities, activities, organization.**

### The scope caveat, from the same paper

`machamer2000mechanisms` p. 2 is unusually explicit about its own limits. The authors "confine our attention to mechanisms in molecular biology and neurobiology," say they "do not claim that all scientists look for mechanisms or that all explanations are descriptions of mechanisms," and leave cognitive and social application "as an open question."

This is a real constraint on a general-purpose book. Chapter 2's examples will not be molecular biology.

### The later consensus formulation

`craver2026mechanisms` §2 records the "minimal mechanism" characterization:

> "A mechanism for a phenomenon consists of entities (or parts) whose activities and interactions are organized so as to be responsible for the phenomenon."

attributed to Glennan (2017) and Glennan & Illari (2017a). Per §2 the formulation deliberately **drops the regularity requirement** (to admit one-off mechanisms) and **drops function language** (to admit mechanisms serving no end).

That matters for this book. A drought response, a housing allocation, a market reacting to a published forecast — none is reliably "regular" in MDC's sense. The minimal formulation travels; the 2000 formulation does not, by its own admission.

### Engineering usage

No engineering source in this pass defines `mechanism` as a term of art. `astrom2008feedback` speaks of subsystems, interconnection, and interfaces (p. 32) without invoking mechanism vocabulary. This is itself a finding: **`mechanism` is philosophy-of-science and life-science vocabulary, not universal modelling vocabulary.**

## 2. Q2 — The minimal common idea Chapter 2 can safely use

Stripping to what both formulations share:

> parts, what those parts do, and how they are arranged — such that the arrangement is responsible for the behaviour of interest.

Chapter 2 can use exactly that. It is common to both, it does not require regularity, it does not require biology, and it does not require function.

**What it does require, and what Chapter 2 must not skip:** the arrangement must be *responsible for* the phenomenon. That is a claim about the world, not a property of the diagram. See §3.

## 3. Q3 — Represented mechanism vs identified causal effect

This is the cluster's central question, and the sources answer it cleanly.

### Phenomenon-relativity comes first

`craver2026mechanisms` §2.1.1: "All mechanisms are mechanisms *of* some phenomenon, a consequential truism first articulated by Kauffman (1971 [1976])." §5.1: "mechanisms are defined only relative to the phenomenon they cause, underlie, or otherwise explain," and (paraphrase) mechanism boundaries are fixed by relevance to the phenomenon, so different phenomena yield different decompositions of the same system.

This is the mechanism-side twin of R01's purpose-relativity, and it is the single most useful thing found in this cluster. **You cannot draw "the mechanism of" a system. You can only draw the mechanism of a specified phenomenon.** Change the phenomenon and the correct decomposition changes.

### The gap between drawing and establishing

`machamer2000mechanisms` p. 18 names the object Chapter 2 actually needs:

> "A sketch is an abstraction for which bottom out entities and activities cannot (yet) be supplied or which contains gaps in its stages. The productive continuity from one stage to the next has missing pieces, black boxes, which we do not yet know how to fill in. A sketch thus serves to indicate what further work needs to be done in order to have a mechanism schema."

and p. 3: "A missing arrow, namely, the inability to specify an activity, leaves an explanatory gap in the productive continuity of the mechanism."

`craver2026mechanisms` §3.3 (paraphrase) supplies the complementary pair: a **how-possibly** model describes an organization that *could* produce the phenomenon; a **how-actually** model describes one that *actually* produces it.

### What supplies the evidence

`machamer2000mechanisms` p. 17 is explicit, and it is the authors' own account, not an outside criticism:

> "While the mechanism is operating, the experimenter may intervene to alter some part of the mechanism and observe the changes in a termination condition or what the mechanism does. Changes produced by such interventions can provide evidence for the hypothesized schema."

The diagram is the hypothesis. **Intervention is the evidence.** The mechanist literature says so itself.

This aligns exactly with `pearl2009causal`, whose existing source note records the Chapter 1 claim that "association alone is insufficient for an intervention-effect conclusion; causal conclusions require additional causal assumptions or design information."

### Where the sources are contested

`craver2026mechanisms` §2.1.3 (paraphrase) records that mechanists disagree among themselves about how causation works inside a mechanism — conserved-quantity, activity-based, counterfactual, and Glennan's lower-level-mechanism accounts all compete. The entry maps positions rather than settling them.

**Chapter 2 must not adjudicate this.** It is not Chapter 2's fight, and it is not Chapter 7's either at the level the book teaches.

## 4. Q4 — When a diagram merely hypothesizes

Consolidated answer, all sourced:

| Sign the drawing is a hypothesis | Source |
|---|---|
| An arrow you cannot name an activity for | `machamer2000mechanisms` p. 3 |
| A black box whose contents you cannot yet supply | `machamer2000mechanisms` p. 18 |
| It shows how the phenomenon *could* be produced, not that it *is* | `craver2026mechanisms` §3.3 |
| No intervention has tested it | `machamer2000mechanisms` p. 17 |

This is a usable reader-facing checklist and it is entirely established content. It requires no pedagogical synthesis.

## 5. Q5 — Wording that preserves the Chapter 7 boundary

Recommended Chapter 2 register (proposal, not decision):

- **permitted:** "a proposed mechanism", "the represented mechanism", "on this representation, X acts on Y", "this is how the effect could be produced";
- **forbidden:** "the mechanism is", "X causes Y", "this shows that", "therefore intervening on X will change Y".

The distinguishing test the reader can apply: *have I drawn what would have to be true, or shown that it is true?*

Chapter 2 owns the first. Chapter 7 owns the second.

## 6. Cautions — claims the manuscript must NOT make

1. Do not attribute the entities-and-activities definition to a general science of modelling. `machamer2000mechanisms` p. 2 restricts itself to molecular biology and neurobiology.
2. Do not impose **regularity** on the reader's mechanisms. The 2000 formulation requires it; the minimal formulation drops it; this book's cases mostly fail it.
3. Do not say mechanistic representation establishes causation. The mechanist literature itself routes evidence through intervention (`machamer2000mechanisms` p. 17).
4. Do not present mechanism-causation as settled (`craver2026mechanisms` §2.1.3).
5. Do not extend phenomenon-relativity to purpose-relativity **as if the source said so**. `craver2026mechanisms` says mechanisms are relative to a *phenomenon*. Chapter 2's move from phenomenon to stated purpose is the **book's own pedagogical synthesis** and must be labelled as such per `canon/pedagogy.md`.
6. Do not use `mechanism` where `structure`, `interaction`, or `dependency` is meant. Mechanism carries a productive-of-change commitment.
7. Do not import how-possibly/how-actually as required reader vocabulary without deciding it is worth the terminology budget (see §8).

## 7. Verdict on the stop condition

`research-plan.md` §5 asks whether `mechanism` is (a) required controlled vocabulary, (b) optional explanatory prose, or (c) a term needing explicit qualification.

**The evidence supports (a) with a mandatory qualification — effectively (a) plus (c).**

Reasoning:

- The chapter's governed title contains "Mechanisms" (`README.md`), and its core competence names mechanisms. The term cannot be optional prose without contradicting the frozen architecture.
- But the term cannot be used unqualified either, because its established definitions carry a *responsible-for-the-phenomenon* commitment the reader has not earned and cannot yet discharge.
- The qualification is available and sourced: mechanisms are always mechanisms *of* a specified phenomenon, and a drawn mechanism is a hypothesis until intervention tests it.

So: **required vocabulary, always phenomenon-indexed, always epistemically hedged.**

## 8. Unresolved author decisions raised by R02

1. Adopt the minimal formulation (parts, activities/interactions, organization, responsible-for-phenomenon) as the reader-facing definition, in preference to MDC's regularity-bearing one?
2. Does `entity` / `activity` / `organization` become controlled vocabulary, or only `mechanism`?
3. Does the reader meet **how-possibly / how-actually** as named terms, or only as the plain-language contrast "could produce" versus "does produce"?
4. Does the reader meet **schema / sketch** as named terms, or only the black-box idea?
5. How is phenomenon-relativity reconciled in prose with R01's purpose-relativity, given that they are different relativities that usually but not always coincide?

Question 5 is the important one and is flagged for adjudication: a purpose can require representing a phenomenon, but two purposes can concern the same phenomenon and still want different representations.
