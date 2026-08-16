# Chapter 2 Bounded Research Plan

Status: working research control; no manuscript drafting and no chapter-boundary decision is implied by this file.

Chapter 2: **Representation, Mechanisms, and Scale**

## 1. Research objective

Produce only the conceptual evidence needed to adjudicate Chapter 2's unique job, terminology, scope boundaries, and example architecture.

Do **not** attempt a broad literature review of modeling, philosophy of science, causal explanation, systems science, or multiscale modeling.

The research ends when the author can make explicit decisions about:

- what Chapter 2 means by model/representation;
- how boundary choice is taught;
- what `mechanism` may mean without preempting causal identification;
- how abstraction, aggregation, grain, and scale are distinguished;
- how `state` is introduced without teaching formal dynamics early;
- which concepts are core, deferred, or depth-curriculum material;
- which examples can carry the chapter's six-hour competence.

## 2. Source hierarchy

Prefer primary or canonical sources and authoritative technical standards/texts appropriate to each concept.

Priority:

1. authoritative modeling/engineering/scientific-modeling sources;
2. primary philosophy-of-science sources where terminology such as model, representation, mechanism, abstraction, or idealization is genuinely contested or tradition-specific;
3. authoritative systems/dynamical-systems sources for `state` vocabulary and the Chapter 13 boundary;
4. high-quality review/synthesis sources only where they efficiently map competing terminology;
5. pedagogical sources only if Chapter 2 introduces a learning-design claim not already covered by the book-wide pedagogy.

Avoid using popular summaries as load-bearing definitional evidence.

## 3. Dossier format

Each research cluster should produce one bounded dossier containing:

- precise research question;
- candidate terminology/definitions from sources;
- where sources agree;
- where terminology is field-specific or contested;
- implications for Chapter 2;
- explicit cautions / claims the manuscript must not make;
- candidate citation keys and source-note needs;
- unresolved author decisions.

A dossier is evidence for adjudication, not the final author decision.

## 4. R01 — Models, representations, boundaries, and purpose

### Questions

1. What minimally defensible distinction should the book make among a real/focal system, a model, and a representation?
2. Which established traditions explicitly treat model adequacy or model construction as purpose-relative?
3. How do authoritative sources describe system/model boundary choice?
4. What supports the claim that omitting detail can be appropriate rather than inherently inaccurate?
5. What supports the use of multiple models or representations of the same system for different purposes?

### Deliverable

`research-01-models-representations-boundaries.md`

### Stop condition

Stop when there is enough evidence to write a Chapter 2 terminology decision for:

- focal/target system;
- model;
- representation;
- boundary;
- purpose-relative simplification;
- alternative representation.

Do not continue into full VVUQ/credibility machinery; Chapter 5 owns systematic adequacy criticism.

## 5. R02 — Mechanism and causal-language boundary

### Questions

1. How is `mechanism` used in mechanistic explanation, scientific modeling, and systems/engineering contexts?
2. Which minimal common idea, if any, can Chapter 2 safely use across domains?
3. How should the book distinguish a represented mechanism from evidence that a causal effect is identified?
4. When does a diagram or mechanistic narrative merely hypothesize a process rather than establish it?
5. Which Chapter 2 wording would preserve the later Chapter 7 distinction between mechanistic knowledge and causal identification?

### Deliverable

`research-02-mechanism-causal-boundary.md`

### Stop condition

Stop when the author can decide whether `mechanism` is:

- required controlled vocabulary;
- optional explanatory prose;
- or a term needing explicit qualification.

Do not research do-calculus, potential-outcomes estimands, or detailed causal-identification strategies except where needed to state the boundary.

## 6. R03 — Abstraction, idealization, aggregation, grain, and scale

### Questions

1. How do major modeling traditions distinguish abstraction from idealization, if at all?
2. Does the core chapter need both terms?
3. What does aggregation/coarse-graining mean at representation level?
4. Which terms best express descriptive grain or resolution without collapsing them into spatial scale alone?
5. How do changes in spatial, temporal, organizational, or population scale alter what a model can answer?
6. What failure modes arise when heterogeneous entities/processes are aggregated?

### Deliverable

`research-03-abstraction-aggregation-scale.md`

### Stop condition

Stop when the author can choose controlled vocabulary among:

- abstraction;
- idealization;
- aggregation;
- coarse-graining;
- scale;
- level;
- grain;
- resolution.

Do not expand into formal renormalization, homogenization, multiscale numerical methods, or advanced hierarchical modeling; those are depth-curriculum candidates.

## 7. R04 — Entities, variables, states, and structural representation

### Questions

1. What is the safest introductory distinction among entities/components, attributes/variables, parameters, and state variables?
2. Which meaning of `state` is compatible with later dynamical-systems/control usage?
3. Can Chapter 2 use state/configuration for a static snapshot without teaching evolution laws yet?
4. How should relationships/interactions be represented without implying causal identification?
5. What minimum notation, if any, improves rather than obscures the distinction among entities, variables, states, and mechanisms?

### Deliverable

`research-04-entities-variables-state.md`

### Stop condition

Stop when the Chapter 2–Chapter 13/14 handoff can be stated explicitly and the terminology registry can be updated without later contradiction.

Do not research formal state-space models, observability, controllability, stability, structural identifiability, or dynamic programming beyond boundary-setting needs.

## 8. R05 — Example and exercise architecture

R05 begins only after R01–R04 are adjudicated enough that examples will not smuggle in unstable terminology.

### Questions

1. Which domain can show multiple defensible representations of the same focal system at different boundaries/grain?
2. Can the case expose boundary choice, entities/variables, state/configuration, mechanism, abstraction, aggregation, scale, and alternative representations without requiring hidden specialist knowledge?
3. Should the Chapter 1 water case recur for one worked comparison, or would a new anchor be cleaner?
4. Which short contrasts best isolate one representation choice at a time?
5. What cold-transfer task tests representation construction rather than domain expertise or measurement knowledge?

### Candidate case criteria

A viable primary case should support at least three different representations whose usefulness changes with intended use.

Examples should allow the learner to answer questions such as:

- What should be inside the boundary?
- What can be treated as an entity or aggregate?
- Which variables/states matter for this use?
- What mechanism or interaction is being represented?
- What detail can be omitted?
- What changes when the grain or scale changes?
- What would a different representation make easier or impossible to answer?

### Deliverable

`research-05-examples-exercises.md`

This dossier may be mostly design comparison rather than new conceptual literature research.

## 9. Research sequencing

Recommended order:

1. **R01** — establishes representation/boundary foundation.
2. **R02** — prevents mechanism/causality collapse.
3. **R04** — stabilizes entities/variables/state and later dynamics boundary.
4. **R03** — stabilizes abstraction/aggregation/scale vocabulary once representation primitives are clearer.
5. Author adjudication of R01–R04.
6. **R05** — choose anchor/contrasts/exercises using adjudicated vocabulary.
7. Fill and synchronize `spec.md`.
8. Only then create a detailed drafting blueprint.

R03 and R04 may be researched in the opposite order if source work makes that more efficient, but both must precede final example architecture.

## 10. Evidence discipline

For every candidate source:

- verify metadata before promoting a citation key;
- create/update a matching `sources/<key>.md` note when the source is actually read;
- record exact conceptual support and cautions;
- distinguish established terminology from the book's pedagogical synthesis;
- do not cite a source for claims broader than the inspected passage supports.

Existing Chapter 1 sources may be reused only when they directly support the Chapter 2 claim. Do not reuse a citation merely because it is already in `references.bib`.

## 11. Author-adjudication gates after research

After R01–R04, produce author decisions on:

- Chapter 2's unique job;
- controlled terminology;
- core/deferred scope;
- boundaries to Chapters 3, 4, 5, 7, 9, 13, and 14;
- whether any new pedagogy artifact is needed (default: no).

After R05, decide:

- primary worked case;
- short contrasts;
- exercise sequence;
- cold-transfer target;
- section architecture and time/page allocation.

Only after these decisions should the live `spec.md` be rewritten from TODO skeleton into a drafting-ready specification.

## 12. No-write boundary during bounded research

During each conceptual research cluster, do not modify:

- `spec.md`;
- `canon/terminology.md`;
- `canon/pedagogy.md`;
- `decisions/`;
- manuscript files.

Research dossiers may be added as working evidence. Governed artifacts change only after explicit author adjudication.
