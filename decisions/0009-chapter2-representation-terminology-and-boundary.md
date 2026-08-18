# Decision 0009: Chapter 2 Representation Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

This record is written in the form of a decision so that its consequences are inspectable, but it has **not** been adjudicated by the author. `research-plan.md` §11 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced for review rather than silently applied.

Everything downstream of this record — `spec.md`, the drafting blueprint, the manuscript, and the provisional `canon/terminology.md` entries — is built on it and inherits its provisional status. Rejecting a clause here invalidates the corresponding downstream text, which is why each clause is numbered.

Evidence base: `research-01-models-representations-boundaries.md`, `research-02-mechanism-causal-boundary.md`, `research-03-abstraction-aggregation-scale.md`, `research-04-entities-variables-state.md`.

## Decision

Chapter 2 teaches **purpose-relative representation** at introductory but productive depth. Its organizing claim is:

> What belongs inside a representation, at what grain, is settled by the stated purpose — not by the system, and not by how much is known.

This claim is **established content**, not pedagogical synthesis. It is asserted independently by an engineering textbook (`astrom2008feedback` p. 27), a working scientist's methodological argument (`levins1966strategy` pp. 421–422), and an agency standard (`nasa2024models` §4.1.1.1).

### 1. Model, representation, and target system

**1.1** Chapter 2 uses `model` and `representation` interchangeably for the constructed object, preferring `representation` because it foregrounds selection and purpose. **No distinction between them is manufactured.** Inventing one would violate the intellectual rule against coining umbrella terminology for elegance.

**1.2** The thing represented is the **target system**. This is established terminology (`frigg2025models` §1) and was already reserved by Chapter 1's spec with the note that "The target system is not its model; detailed boundary work belongs to Chapter 2."

**1.3** Chapter 2 must state explicitly that its `target system` is *not* a renaming of Chapter 1's `target`. Chapter 1's `target` is what the answer is about. The target system is the part of the world under representation. They frequently coincide and are not the same concept.

**1.4** Rejected: `focal system`. Not established terminology; coining it would breach the same rule as 1.1.

### 2. Boundary

**2.1** Chapter 2 teaches boundary choice **by worked example and by warning**, not by criterion. R01 found no sourced general procedure for boundary selection.

**2.2** Four boundary claims are supportable and may be taught:

- the cut is governed by purpose and is provisional (`sterman2006evidence`);
- narrowing can hide delayed and distal consequences (`sterman2006evidence`);
- widening enables new questions rather than merely adding work (`astrom2008feedback` p. 29);
- where the cut falls can change the internal description, not only its size (`astrom2008feedback` p. 33).

**2.3** Chapter 2 must **not** present a general boundary-selection procedure as sourced. If a future draft wants one, R01 reopens for the system-dynamics and experimental-frame literature.

### 3. Mechanism

**3.1** `mechanism` is **required controlled vocabulary, always phenomenon-indexed, always epistemically hedged.** The chapter's governed title and core competence name mechanisms, so the term cannot be optional; its established definitions carry a responsible-for-the-phenomenon commitment the reader cannot yet discharge, so it cannot be unhedged.

**3.2** The reader-facing definition is the **minimal** formulation, not the 2000 formulation:

> A mechanism for a phenomenon is a set of parts whose activities and interactions are organized so as to be responsible for that phenomenon.

`craver2026mechanisms` §2, after Glennan (2017) and Glennan & Illari (2017a).

**3.3** Rejected as reader-facing: the `machamer2000mechanisms` p. 3 formulation. It requires **regularity**, which most of this book's cases fail, and its authors confine themselves to molecular biology and neurobiology (p. 2). It remains cited for entities/activities/organization and for the schema–sketch material.

**3.4** Chapter 2 may say a mechanism is **proposed**, **represented**, or **could produce** the phenomenon. It may not say a mechanism is **established**, or that X **causes** Y. Causal identification is Chapter 7.

**3.5** The reader receives the four-sign hypothesis checklist from R02 §4 — an arrow with no nameable activity, a black box, a could-produce rather than does-produce claim, and no intervention having tested it. This is established content.

**3.6** `how-possibly` / `how-actually` and `schema` / `sketch` are **not** required reader vocabulary. The underlying contrasts are taught in plain language. The terms may appear once, attributed, as signposts to the literature.

### 4. Two relativities

**4.1** Chapter 2's organizing relativity is **purpose**.

**4.2** **Phenomenon-relativity** — that a mechanism is always a mechanism *of* something, and its boundaries are fixed by relevance to that phenomenon (`craver2026mechanisms` §2.1.1, §5.1) — is taught as the mechanism-specific case.

**4.3** The generalization from *phenomenon* to *stated purpose* is **the book's own pedagogical synthesis** and must be labelled as such per `canon/pedagogy.md`. The sources say phenomenon; they do not say purpose.

**4.4** The chapter must acknowledge that the two relativities usually coincide but can diverge: two purposes may concern the same phenomenon and still warrant different representations.

### 5. Abstraction, idealization, generality

**5.1** `abstraction` is controlled vocabulary: **leaving a feature out**. An abstraction is silent about what it omits; silence asserts nothing false.

**5.2** `idealization` is a **named contrast only**: **putting in something known to be false**.

**5.3** The distinction is Jones's (2005), reported by `weisberg2007idealization` fn. 14 and by `frigg2025models` §1. It must be presented as **one defensible position, not consensus** — Weisberg himself declines to adopt it, and Aristotelian idealization is omission filed under idealization.

**5.4** The asymmetry is the point and must be taught: an omission is defended by showing the feature does not bear on the question; a distortion must be defended by showing the error it introduces is tolerable for the use. The second is a harder argument.

**5.5** `generality` / `scope` is controlled vocabulary and is taught **explicitly as separate from abstraction**: "Abstraction is an issue of the amount of detail … The generality of a schema is the scope (small or large) of the domain in which it can be instantiated" (`machamer2000mechanisms` p. 16). Simpler and more general are different moves.

**5.6** Galilean / minimalist / multiple-models taxonomy is deferred to the depth curriculum.

### 6. Grain, scale, aggregation

**6.1** Controlled: `abstraction`, `generality`/`scope`, `aggregation`.
Ordinary careful language: `grain`, `resolution`, `fidelity`, `scale`.
**Avoided entirely:** `level` (overloaded past repair at this depth) and `coarse-graining` (physics-specific, unsourced here).

**6.2** `aggregation` in Chapter 2 means **representational aggregation**: treating distinguishable things as one for the purpose at hand. It is explicitly distinguished from aggregation introduced by the observation, recording, or reporting process, which is Chapter 4.

**6.3** No source inspected defines representational aggregation or supplies criteria for it. Chapter 2 therefore teaches aggregation failure **by self-evidencing arithmetic demonstration in its own anchor case**, not by citation. The reader must be able to verify the failure on the page.

**6.4** The ecological-fallacy literature is **not** imported. It concerns inference from aggregate data to individuals, which is Chapters 4 and 9.

**6.5** If spatial, temporal, organizational, and population scale are used as four axes, they are labelled as **the book's own organizing device**. No inspected source supplies that taxonomy.

**6.6** `levins1966strategy` p. 424 must not be cited for `grain` in the Chapter 2 sense. Levins's coarse-/fine-grained distinction concerns environmental heterogeneity relative to an organism.

### 7. Entities, variables, state

**7.1** `entity` / `part` and `variable` are **ordinary careful language**, not registry-controlled. They carry low collision risk with later chapters.

**7.2** `state` **is** reader-facing controlled vocabulary in Chapter 2, defined in the purpose-qualified form taken from `astrom2008feedback` p. 34:

> The state is the collection of things you must carry forward — what summarizes the past well enough to answer what comes next.

**7.3** The test this licenses is the chapter's defence against "state = any variable": a quantity belongs to the state only if it is needed to summarize the past *for the question being asked*. A quantity recomputable from others, or irrelevant to what comes next, is not state.

**7.4** The role distinction — carried forward / acted on from outside / observed — is taught **as roles within a representation**, with the explicit point that the same physical quantity can take different roles in different representations of the same system.

**7.5** **No symbolic notation.** No `x`, `u`, `y`, no state-space form, no order, linearity, reachability, or observability. `astrom2008feedback` moves from those symbols to matrix equations within two pages; adopting the notation invites the machinery Chapter 2 must defer.

**7.6** `state space` is **not** named. Withheld to Chapter 13.

**7.7** `parameter` is **not** introduced as controlled vocabulary. No inspected source supports a definition at this depth, and the readiness audit already flagged it as optional.

### 8. Alternative representations

**8.1** Chapter 2 teaches that different representations of one target system serve different uses. This is established, asserted independently by `astrom2008feedback` (pp. 27, 32), `weisberg2007idealization` (multiple-models idealization), and `frigg2025models` (§5.1).

**8.2** The reader is taught the **weaker, better-behaved version** — different representations for different purposes. The stronger claim, that the sciences tolerate mutually *incompatible* models of one system, is mentioned but is not the takeaway.

**8.3** Chapter 2 supplies a **reason** to build more than one: conclusions that survive across representations with different simplifications are more trustworthy than conclusions that do not (`levins1966strategy` p. 423, robust theorems).

**8.4** "Our truth is the intersection of independent lies" may be quoted, attributed, with the caution that it concerns robust theorems across models sharing a common assumption — not general epistemology, and not licence to build arbitrary alternatives.

### 9. What Chapter 2 does not do

Reaffirmed from the readiness audit, and binding on the manuscript:

- not a measurement-validity chapter (Chapter 3);
- not a data-provenance chapter (Chapter 4);
- not the full criticism toolkit — assumption records, dimensional and limiting checks, Fermi bounds, rival-model falsification (Chapter 5);
- not causal identification (Chapter 7);
- not transport or target populations (Chapter 9);
- not formal dynamics, stock-flow, feedback, equilibrium, or stability (Chapter 13);
- not observability, structural identifiability, or control (Chapter 14).

## Sources promoted by this decision

Newly added and verified: `machamer2000mechanisms`, `craver2026mechanisms`, `frigg2025models`, `weisberg2007idealization`, `levins1966strategy`.

Reused from Chapter 1, verified as directly supporting a Chapter 2 claim per `research-plan.md` §10: `astrom2008feedback` (upgraded to page-level verification), `sterman2006evidence`, `nasa2024models`, `pearl2009causal`.

Added 2026-08-18 during the gap-closing pass: `sterman2002models` (pp. 501–507 read). Note that this is a **different article** from `sterman2006evidence`; both are in the bibliography and must not be conflated.

`weisberg2007idealization` was read in **preprint**; before any load-bearing quotation is frozen, the published *Journal of Philosophy* text must be checked and locators converted to printed pages.

## No architecture change

This decision does not change the Chapter 2 title, central question, core competence, 29-page target, 6-hour target, or any part of the book architecture. Those remain governed by `README.md` and `decisions/0001`.

## Known gaps carried forward

1. No sourced boundary-selection procedure (R01 §3, §7). **Partially addressed 2026-08-18** by `sterman2002models`, which supplies a principle — a side effect is an effect outside the boundary drawn — but not criteria. Clause 2.3 is unaffected and stands.
2. No sourced definition of representational aggregation (R03 §3).
3. `weisberg2007idealization` locators are preprint section headings, not printed pages.
4. Jones (2005) not read directly; the omission/distortion distinction rests on two secondary reports.

None blocks drafting. Items 1 and 2 constrain what the manuscript may claim, and clauses 2.3 and 6.3 encode those constraints.
