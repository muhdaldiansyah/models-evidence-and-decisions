# Chapter 2 Readiness Audit

Status: pre-research working control; not a final chapter decision.

Chapter 2: **Representation, Mechanisms, and Scale**

Current architecture from `README.md` and `spec.md`:

- central question: **What is inside the model, at what grain, and how do parts produce behavior?**
- core competence: **Construct purpose-relative representations using boundaries, entities, variables, states, mechanisms, abstraction, aggregation, scale, and alternative representations.**
- target: 29 pages / 6 serious learning hours.

## 1. Readiness verdict

**Not drafting-ready.**

The live `spec.md` contains the chapter title, central question, core competence, page target, and learning-time target, but its role, prerequisites, interfaces, scope boundary, section architecture, examples, exercise architecture, transfer target, evidence plan, failure modes, and open questions remain unresolved.

Do not create `chapter.md` until the conceptual boundary and core terminology have been researched and adjudicated.

## 2. Unique-job hypothesis to test

The likely unique job of Chapter 2 is:

> Teach readers how to build and compare purpose-relative representations of a focal system before asking whether the resulting quantities are well measured, whether the resulting records are representative, or whether the representation is adequate under stronger criticism.

A successful Chapter 2 reader should be able to decide what belongs inside a representation, at what grain, with which entities, variables, states, relations or mechanisms, and which simplifications or aggregations are defensible for the stated use.

This is a **working hypothesis**, not yet a governed definition.

## 3. Neighboring-chapter boundaries already implied by the architecture

### Chapter 1 — formulation before representation

Chapter 1 owns intended use, practical decision framing, informal targets, claim-type triage, environment screening, and the first complete reasoning pass.

Chapter 2 should begin after the reader can state what the analysis is for. It should not reteach decision framing as its main content.

### Chapter 3 — measurement and operationalization

Chapter 3 owns constructs, observables, operationalization, units, proxies, validity, reliability distinctions, and measurement error.

Chapter 2 may distinguish a modeled quantity or state from its observation, but should not become a measurement-validity chapter.

### Chapter 4 — observation processes and provenance

Chapter 4 owns why particular records came to exist: sampling, selection, missingness, censoring, aggregation in the data-production process, reporting, institutional incentives, and manipulation.

Chapter 2 may teach **representational aggregation** or coarse-graining, but must distinguish that from aggregation introduced by the observation or reporting process.

### Chapter 5 — assumptions, adequacy, and rival models

Chapter 5 owns systematic criticism: assumption records, dimensional and limiting checks, Fermi bounds, rival models as criticism, structural uncertainty, and predicted failure modes.

Chapter 2 should teach that multiple representations are possible and purpose-relative. It should not absorb Chapter 5's full criticism toolkit.

### Chapter 7 — causal identification

Chapter 7 owns formal targets/estimands and causal identification.

Chapter 2 may discuss mechanisms as parts and relations through which represented behavior is produced, but must not imply that drawing or narrating a mechanism establishes a causal effect or causal identification.

### Chapters 13–14 — dynamics and control

Chapter 13 owns formal dynamics, accumulation, stock/flow language, feedback, equilibrium/stability, oscillation, overshoot, and policy resistance. Chapter 14 owns sequential decision/control, observability, and structural identifiability.

Chapter 2 can introduce `state` and time-dependent representation at foundational depth only if the boundary is explicit: a state variable may be represented without yet teaching the formal machinery of dynamical systems or control.

### Chapter 9 — transport and target populations

Chapter 9 owns external validity, generalizability, target populations, and transportability.

Chapter 2 may discuss spatial, organizational, or population scale as part of representation, but should not become a chapter about transporting evidence between populations or settings.

## 4. Terminology readiness gap

The current terminology registry does not yet stabilize the Chapter 2 core vocabulary. Before drafting, research and adjudicate at least:

- model;
- representation;
- system boundary / model boundary;
- entity;
- variable;
- parameter (only if needed this early);
- state / state variable;
- mechanism;
- abstraction;
- idealization (decision needed: core term or optional contrast);
- aggregation;
- scale / level / grain / resolution;
- alternative representation.

Avoid treating common words as harmless. Several have field-specific meanings that can collide later with statistics, causal inference, dynamical systems, philosophy of science, or engineering modeling.

## 5. High-risk conceptual collapses to prevent

1. **Representation = reality.** A representation selects and organizes features for a purpose; it is not the system itself.
2. **Detail = realism = adequacy.** More detail can be irrelevant or harmful for a stated use.
3. **Boundary = physical edge.** Analytical boundaries can include or exclude processes, actors, time horizons, or scales even when no physical wall exists.
4. **Mechanism = established causal effect.** A mechanistic story or structural relation is not automatically identified causal evidence.
5. **State = any variable.** If the book uses `state`, its Chapter 2 meaning must remain compatible with later dynamical-systems usage.
6. **Aggregation = data summarization only.** Representation can aggregate entities or processes before any data are collected; Chapter 4 later treats aggregation in records and reporting.
7. **Scale = just units.** Spatial, temporal, organizational, population, and descriptive grain may differ even when units are unchanged.
8. **One true model.** Different representations of the same focal system can be useful for different purposes without one being globally correct.
9. **Alternative representation = rival model criticism.** Chapter 2 needs comparison for construction and perspective; Chapter 5 owns stronger falsification/adequacy criticism.
10. **Mechanism = dynamics.** A representation can contain mechanisms or dependency structure without Chapter 2 teaching full feedback/stability/control machinery.

## 6. Research clusters required before spec adjudication

### R01 — Models, representations, boundaries, and purpose

Need source-grounded distinctions for:

- model versus represented system;
- representation as selective/purpose-relative;
- boundary choice;
- why omitted detail can be appropriate rather than defective;
- multiple legitimate representations for different uses.

### R02 — Mechanisms and causal-language boundary

Need a cautious interdisciplinary boundary for:

- mechanism as a way parts/interactions generate behavior;
- mechanistic explanation versus mere association;
- mechanistic representation versus formal causal identification;
- when Chapter 2 may say `mechanism` without preempting Chapter 7.

### R03 — Abstraction, idealization, aggregation, and scale

Need distinctions among:

- abstraction versus idealization;
- aggregation/coarse-graining;
- level/grain/resolution/scale;
- when higher/lower detail changes the question rather than only precision;
- risks of aggregation across heterogeneous entities or mechanisms.

### R04 — Entities, variables, states, and structural representation

Need stable introductory vocabulary for:

- entities/components;
- attributes/variables;
- parameters if needed;
- state/state variable;
- relationships/interactions;
- static representation versus time-evolving state;
- explicit boundary to Chapters 13–14.

### R05 — Chapter-specific pedagogy, examples, and transfer

After R01–R04, adjudicate:

- one primary worked representation case;
- short structural contrasts;
- which existing Chapter 1 cases should recur, if any;
- exercise progression from boundary choice to independent representation;
- a cold-transfer task that tests representation choice rather than hidden domain expertise.

This cluster may reuse the book's established worked-example/fading/retrieval pedagogy; it does not require inventing a new Chapter 2 learning framework.

## 7. Candidate example constraints

Do not select examples solely because they are visually attractive.

A Chapter 2 anchor should permit several defensible representations of the **same focal system** at different boundaries or grain, with visible consequences for what can be answered.

Prefer examples that can expose at least:

- boundary inclusion/exclusion;
- entities and variables;
- mechanism or interaction;
- state or configuration;
- aggregation or scale;
- alternative representations for different intended uses.

Avoid an anchor whose main intellectual difficulty is actually measurement validity, missing-data provenance, causal identification, optimization, or formal feedback/control.

The Chapter 1 water case may recur only if Chapter 2 adds a genuinely new operation (for example, comparing storage-only, treatment-and-demand, and network-level representations). Recurrence is not mandatory.

The pendulum remains a plausible clean contrast because Chapter 1 already established that intended use changes representation adequacy, but Chapter 2 should not rely on it as the only example.

## 8. Decisions likely required after bounded research

At minimum, author adjudication should settle:

1. the reader-facing meaning and Chapter 2 boundary of `model` and `representation`;
2. whether `mechanism` is core controlled vocabulary and exactly what it may claim;
3. whether `abstraction` and `idealization` are both required or one is sufficient at core depth;
4. the preferred controlled vocabulary among `scale`, `level`, `grain`, and `resolution`;
5. the introductory meaning of `state` and its handoff to Chapter 13;
6. the distinction between representational aggregation (Chapter 2) and observed/reporting aggregation (Chapter 4);
7. the primary worked example and transfer task;
8. the section architecture within 29 pages / 6 hours.

## 9. Drafting gate

Chapter 2 becomes drafting-ready only when:

- R01–R04 have bounded research dossiers;
- terminology decisions are adjudicated;
- scope boundaries against Chapters 3, 4, 5, 7, 9, 13, and 14 are explicit;
- a worked-example architecture exists;
- the live `spec.md` is substantially filled and no longer contains load-bearing TODOs;
- an evidence/source plan identifies which conceptual claims require citations;
- exercises and transfer target are specified.

Until then, no `chapter.md` should be created.
