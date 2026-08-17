# Research 01 — Models, Representations, Boundaries, and Purpose

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision and not a change to any governed artifact. Written under the no-write boundary in `research-plan.md` §12.

Cluster R01 of `research-plan.md` §4. Research conducted 2026-08-18.

## 0. Scope actually covered

Five questions were posed. Four are answered with verified primary or authoritative sources. One — boundary choice — is **partially answered**, and the gap is recorded in §7 rather than papered over.

Sources inspected for this cluster: `frigg2025models`, `astrom2008feedback` (newly verified at page level), `weisberg2007idealization`, `sterman2006evidence` (existing), `nasa2024models` (existing).

## 1. Q1 — The focal system / model / representation distinction

### What the sources say

`frigg2025models` §1: "Many scientific models are representational models: they represent a selected part or aspect of the world, which is the model's target system."

Two things are doing work in that sentence and both matter for Chapter 2:

1. **`target system` is the established term** for the part of the world a model is about. It is not a coinage.
2. The model represents a **selected** part or aspect. Selection is built into the definition, not added later as a concession.

`frigg2025models` §2.4 supplies the model/description separation: "the Newtonian model of the solar system consists of orbiting spheres, but it makes no sense to say this about its description." A model, a description of a model, and the system modelled are three things.

`astrom2008feedback` p. 27 gives the engineering-side formulation: "A model is a mathematical representation of a physical, biological or information system."

### Where sources agree

Both traditions treat a model as *of* something, and as selective. Neither treats a model as a copy.

### Where terminology is field-specific

- Philosophy of science says **target system**.
- Engineering and control say **system** or **plant**, and use **model** for the representation.
- Chapter 1 already uses **target** in the book's own qualified sense (`canon/terminology.md`, `target`), and already registers **target system** with the note that "The target system is not its model; detailed boundary work belongs to Chapter 2" (`chapters/01-decisions-questions/spec.md`).

There is therefore a live collision risk: Chapter 1's `target` means *what the answer is about*; R01's `target system` means *the part of the world being represented*. These are close but not identical, and Chapter 1 has already made `target` load-bearing.

### Implication for Chapter 2

Chapter 2 needs a term for the thing being represented that does **not** silently re-open Chapter 1's `target`. The candidate registered in Chapter 1's spec is `target system`. An alternative is `focal system`, which is not established terminology and would violate the intellectual rule against coining umbrella terms.

**Recommendation to the author (not a decision):** keep `target system`, and state explicitly in Chapter 2 that it names the part of the world under representation, which may be narrower or wider than Chapter 1's `target`.

## 2. Q2 — Traditions that treat model adequacy or construction as purpose-relative

This is the best-evidenced question in the cluster. Three independent traditions say it.

### Engineering / control

`astrom2008feedback` p. 27: "A model is a precise representation of a system's dynamics used to answer questions via analysis and simulation. **The model we choose depends on the questions we wish to answer**, and so there may be multiple models for a single dynamical system, with different levels of fidelity depending on the phenomena of interest."

p. 32: "Because of these different uses of models, it is common to use a hierarchy of models having different complexity and fidelity."

### Model credibility standards

`nasa2024models` §3 establishes `intended use` as the expected purpose and application of a model; §4.1.1.1 [M&S 40] requires the documented intended use to state **what is represented**; §4.1.1.5 [M&S 43] ties acceptance criteria to whether the model satisfies its intended use.

This is the strongest institutional form of the claim: a standards body requires that what is inside the representation be justified against a stated use.

### Philosophy of science

`weisberg2007idealization` supplies the goal-relative frame: "There is no single purpose for idealization and hence there is not a single set of rules that theorists ought to follow when idealizing," and introduces *representational ideals* as the goals governing the practice.

### Where sources agree

All three say the same structural thing in different vocabularies: **adequacy is relative to use, not absolute.** Chapter 1 already established this for analyses (`canon/terminology.md`, `adequacy`). R01 confirms it holds for representations specifically.

### Caution

`frigg2025models` does **not** theorise representation as purpose-relative (recorded as a negative finding in that source note). Chapter 2 must not cite the SEP entry for this claim.

## 3. Q3 — Boundary choice (partially answered)

### What was found

`sterman2006evidence` supports the negative case: narrow model boundaries can hide delayed and distal consequences, and interventions can trigger responses that undermine intended outcomes. The existing source note records that Chapter 1 already uses this as "the first boundary is purpose-governed and provisional."

`astrom2008feedback` supplies two mechanical facts about boundaries:

- p. 32: multidomain systems are modelled by "partitioning a system into smaller subsystems," with interface behaviour described where subsystems interconnect;
- p. 33: "states may disappear when components are connected. This implies that the internal description of a component may change when it is connected to other components."

The second is unexpectedly useful. It is a concrete, verifiable case in which **where you cut changes what is inside**, not merely how much is inside.

`astrom2008feedback` p. 29 supplies the converse: "Adding the input makes the model richer and allows new questions to be posed." Widening a boundary is not merely more work; it changes the question set the model can answer.

### What was not found

No source in this cluster supplies a **general theory of boundary selection** — criteria, procedures, or a taxonomy of boundary errors. Sterman gives a warning; Åström and Murray give mechanics.

The system-dynamics literature (Forrester's endogenous point of view; Sterman's *Business Dynamics* model boundary chart) and the modelling-and-simulation literature (Zeigler's experimental frame) are the obvious places to look, and both were identified but **not obtained in verifiable full text** in this pass.

### Implication for Chapter 2

Chapter 2 can teach boundary choice honestly at introductory depth on current evidence: purpose governs the cut; the cut is provisional; widening enables new questions; narrowing can hide consequences; where you cut can change the internal description.

Chapter 2 cannot, on current evidence, present a **sourced general procedure** for boundary selection. If the chapter wants one, R01 must be reopened for the system-dynamics and experimental-frame sources.

## 4. Q4 — Why omitting detail can be appropriate rather than defective

### What the sources say

`frigg2025models` §1 records the abstraction-as-silence analysis attributed to Jones (2005) and Godfrey-Smith (2009): "while an abstraction remains silent about certain features … it does not say anything false."

This is the key move. Omission is not error, because silence is not assertion. A representation that leaves something out has not thereby said something untrue about it.

`frigg2025models` §1 also records Aristotelian idealization as "stripping away, in our imagination, all properties from a concrete object that we believe are not relevant to the problem" — note *relevant to the problem*, i.e. purpose again.

`astrom2008feedback` p. 34 makes the positive case operationally: "A key issue in modeling is to decide how accurately this storage has to be represented." Grain is a decision to be made, not a defect to be minimised.

The Chapter 2 epigraph candidate at `astrom2008feedback` p. 27 — Fermi's objection about arbitrary parameters, and von Neumann's "with four parameters I can fit an elephant, and with five I can make him wiggle his trunk" — gives the reverse lesson from an impeccable source: added parameters are not added credibility.

### Where sources agree

Omission is legitimate when the omitted feature does not bear on the question. All three formulations route the justification through purpose.

### Caution

None of these sources says omission is *always* fine. The claim Chapter 2 may make is conditional: omission is defensible **relative to a stated use**, and the same omission can be fatal under a different use. Chapter 5 owns the systematic criticism of whether a given omission was in fact acceptable.

## 5. Q5 — Multiple models of the same system

Three traditions, again independently.

- `astrom2008feedback` p. 27: "there may be multiple models for a single dynamical system, with different levels of fidelity depending on the phenomena of interest"; p. 32: "a hierarchy of models having different complexity and fidelity."
- `weisberg2007idealization`, §"Multiple Models Idealization": MMI "is the practice of building multiple related but incompatible models, each of which makes distinct claims about the nature and causal structure giving rise to a phenomenon," and "differs from both Galilean and minimalist idealization in not expecting a single best model to be generated."
- `frigg2025models` §5.1, the "incompatible-models argument": "scientists often successfully use several incompatible models of *one and the same* target system for predictive purposes."

### Where sources agree

That multiple, even mutually incompatible, models of one system can be simultaneously useful is asserted by an engineering textbook, a philosophy-of-science paper, and a reference survey. This is about as well-supported as a Chapter 2 claim can be.

### Implication

Chapter 2's anti-"one true model" lesson is **established**, not a pedagogical synthesis. It may be taught as established content, with citation.

Note the strength difference: Åström and Murray describe a *hierarchy* selected by use (compatible models at different fidelity). Weisberg and Frigg–Hartmann describe *incompatible* models. Chapter 2 should teach the weaker, better-behaved version — different representations for different uses — and may mention that the sciences also tolerate outright incompatible models, without making that the reader's takeaway.

## 6. Cautions — claims the Chapter 2 manuscript must NOT make

1. Do not cite `frigg2025models` for purpose-relativity or for boundaries. It addresses neither.
2. Do not present `target system` as this book's coinage. It is established.
3. Do not say the sources show omission is generally harmless. They show it is defensible relative to a use.
4. Do not present a general boundary-selection procedure as sourced. It is not, on current evidence.
5. Do not attribute the abstraction-as-silence analysis to Frigg and Hartmann or to Weisberg. Both report it from Jones (2005); Frigg and Hartmann also cite Godfrey-Smith (2009).
6. Do not let the incompatible-models literature become a licence for the reader to build inconsistent representations casually. The sources describe a mature scientific practice, not a beginner's method.
7. Do not import model credibility, verification, or validation machinery from `nasa2024models`. Chapter 5 owns adequacy criticism; Chapter 2 uses only the intended-use-governs-content point.

## 7. Gaps and what would close them

| Gap | Effect on Chapter 2 | What would close it |
|---|---|---|
| No sourced boundary-selection theory | Chapter 2 teaches boundary reasoning by example and warning rather than by criterion | Verified text of Sterman *Business Dynamics* ch. 3 (model boundary chart, endogenous point of view), or Zeigler's experimental frame |
| `weisberg2007idealization` read in preprint | Locators are section headings, not printed pages | Published *Journal of Philosophy* 104(12):639–659 |
| Jones 2005 not read directly | The omission/distortion distinction rests on two secondary reports | Jones, "Idealization and Abstraction: A Framework," *Idealization XII* (Rodopi, 2005), 173–217 |

None of these blocks adjudication. The first blocks only one optional chapter move.

## 8. Candidate citation keys

Already in `references.bib` and verified: `astrom2008feedback` (upgraded to page-level this pass), `sterman2006evidence`, `nasa2024models`.

Added this pass: `frigg2025models`, `weisberg2007idealization`.

Not yet obtained: a boundary-theory source; Jones 2005.

## 9. Unresolved author decisions raised by R01

1. Adopt `target system` for the thing represented, or a different term, given Chapter 1's prior claim on `target`?
2. Is `representation` controlled vocabulary distinct from `model`, or are they used interchangeably at Chapter 2 depth?
3. Does Chapter 2 teach boundary choice by criterion (requires reopening R01 for sources) or by worked example and warning (supportable now)?
4. Does the reader meet the incompatible-models point at all, or only the different-representations-for-different-uses point?

These go to author adjudication under `research-plan.md` §11. R01 does not settle them.
