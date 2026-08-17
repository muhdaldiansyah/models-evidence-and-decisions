# Research 04 — Entities, Variables, States, and Structural Representation

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision. Written under the no-write boundary in `research-plan.md` §12.

Cluster R04 of `research-plan.md` §7. Researched 2026-08-18, before R03 per the recommended sequencing in §9.

Sources inspected: `astrom2008feedback` (page-verified this pass), `machamer2000mechanisms`, `craver2026mechanisms`.

## 1. Q1 — Entities, attributes/variables, parameters, state variables

### Entities

`machamer2000mechanisms` p. 3: "Entities are the things that engage in activities." Terse, usable, and it defines entities by their role rather than by their substance — which is what a general book needs, since Chapter 2's entities will be reservoirs, households, vehicles, and agencies rather than molecules.

`craver2026mechanisms` §2 uses "entities (or parts)", confirming `part` as an acceptable plain-language equivalent.

### Variables

`astrom2008feedback` uses `variable` throughout without a formal definition — it is treated as understood. p. 34 distinguishes three roles by symbol: the **state** vector `x`, the **control/input** vector `u`, and the **measured signal** `y`.

The useful finding is that the control tradition classifies variables **by role in the representation**, not by type: the same physical quantity can be a state in one model, an input in another, and an output in a third. This is a representation choice, and it is exactly Chapter 2's subject matter.

### Parameters

**Evidence gap.** No source inspected in this pass gives a definition of `parameter` that Chapter 2 could cite.

What was found is oblique but pedagogically valuable: the Chapter 2 epigraph of `astrom2008feedback` p. 27 records Dyson's report of Fermi's objection, and von Neumann's "with four parameters I can fit an elephant, and with five I can make him wiggle his trunk." That warrants a warning about parameters; it does not define them.

The readiness audit already flagged `parameter` as "only if needed this early." R04's recommendation is to **not** introduce it as controlled vocabulary in Chapter 2 on current evidence.

### State variables

Two page-verified formulations from the same book, and the difference between them is instructive:

- p. 28: "The state of a dynamical system is a collection of variables that completely characterizes the motion of a system **for the purpose of predicting future motion**."
- p. 34: "The state of a system is a collection of variables that summarize the past of a system **for the purpose of predicting the future**."

Both embed purpose in the definition. This is the single most important finding of R04: **the canonical control-theory definition of `state` is itself purpose-relative.** Chapter 2's central thesis is not being imported into control theory; it is already there.

p. 34 continues: "For a physical system the state is composed of the variables required to account for storage of mass, momentum and energy. A key issue in modeling is to decide how accurately this storage has to be represented."

Two further things follow. State is about **what is stored / carried forward**. And its grain is a **decision**.

## 2. Q2 — Which meaning of `state` is compatible with Chapters 13–14

The one above, unmodified.

The compatibility test is whether Chapter 2's introduction would have to be retracted or corrected in Chapter 13. Using `astrom2008feedback`'s own definition, it would not — Chapter 13 simply adds the machinery (evolution laws, state space, order, stability) that Chapter 2 withholds.

The handoff sentence is available verbatim from the source. Chapter 2 can say: the state is what you must carry forward to answer the question; Chapter 13 supplies the laws by which it moves.

### The failure mode to prevent

The readiness audit's high-risk collapse #5 is "State = any variable." The sourced definition prevents it precisely: a variable belongs to the state only if it is needed to summarize the past **for predicting the future**. A variable you can recompute from others, or that does not bear on what comes next, is not a state variable.

This gives Chapter 2 a real, checkable test rather than a slogan.

## 3. Q3 — Static snapshot without evolution laws

**Yes, and the source supplies the phrase.**

`astrom2008feedback` p. 28, of the spring–mass system: "The position q and velocity q̇ represent the **instantaneous state** of the system." And p. 28: the set of all possible states is called the state space.

So the tradition itself separates:

- a **state** — the values right now, a snapshot;
- the **state space** — the set of possible snapshots;
- the **dynamics** — the rule taking one snapshot to the next.

Chapter 2 may teach the first, name the second in passing if useful, and hand the third to Chapter 13.

**One honest caution.** Although a state is a snapshot, *which variables belong in it* is fixed by the prediction requirement. Chapter 2 therefore cannot fully separate "what to record now" from "what happens next" — the question determines the list. This is a feature worth teaching, not a problem to hide: it is why representation cannot be done before the purpose is stated.

## 4. Q4 — Representing relationships without implying causal identification

R02 settled the substance. R04 adds the structural point.

`astrom2008feedback` p. 33 supplies a concrete, verifiable illustration that structure is representational rather than given: "states may disappear when components are connected. This implies that the internal description of a component may change when it is connected to other components." Two capacitors in parallel is the worked case.

p. 32 supplies the constructive counterpart: multidomain models are built by "partitioning a system into smaller subsystems," describing behaviour at the interfaces where they interconnect.

So relationships in Chapter 2 are **interfaces and dependencies among represented parts**, which is a weaker and safer notion than causal structure. Recommended reader-facing verbs: *depends on*, *is computed from*, *feeds*, *constrains*, *acts on* — with the R02 hedging discipline.

Forbidden: *causes*, *determines*, *drives* used as an established finding rather than as a represented relation.

## 5. Q5 — Minimum notation

**Recommendation: no symbolic notation in Chapter 2.**

`astrom2008feedback` p. 34 introduces `x`, `u`, `y`, then immediately `dx/dt = f(x,u)`, `y = h(x,u)`, then matrices `A, B, C, D`, order, linearity, and LTI form within two pages. The notation is a gateway to exactly the machinery Chapter 2 must defer; adopting the symbols invites the equations.

What Chapter 2 needs instead is a **role table** — a plain-language listing of each represented quantity with its role (part / attribute / carried-forward quantity / thing acted on from outside / thing observed) and the grain at which it is represented. That achieves the distinctions the notation achieves, without the slope.

If the author wants a single structural device, a labelled parts-and-arrows figure with the R02 hedging vocabulary is defensible; a state vector is not.

## 6. Cautions — claims the manuscript must NOT make

1. Do not define `state` as "a variable that changes over time." That is false to the source and collapses the concept.
2. Do not present the state as a property of the *system*. It is a property of the **representation, relative to what is to be predicted** — both source formulations say so.
3. Do not introduce `parameter` as controlled vocabulary; no inspected source supports a definition.
4. Do not import `x/u/y`, state-space form, order, linearity, reachability, or observability. Chapters 13–14 and the depth curriculum.
5. Do not generalise p. 33 into "boundaries always change internal descriptions." It is an illustration from compositional modelling, not a law.
6. Do not treat input/state/output as a fixed classification of quantities in the world. It is a role assignment within a representation, and it changes between representations of the same system.
7. Do not use `entity` to mean only physical objects. `machamer2000mechanisms` p. 3 defines entities functionally — the things that engage in activities.

## 7. Verdict on the stop condition

`research-plan.md` §7 requires that the Chapter 2 → Chapter 13/14 handoff be statable explicitly and the terminology registry updatable without later contradiction.

**Met.** The handoff is:

> Chapter 2: which quantities must be carried forward to answer the stated question, and at what grain.
> Chapter 13: the laws by which those quantities evolve, and what their evolution implies about equilibrium, stability, and feedback.
> Chapter 14: what can be inferred about them from observation, and how to act on them through time.

`canon/terminology.md` already registers `observability`, `stability`, `equilibrium`, and `feedback` with Chapter 13/14 homes. Adding `state` at Chapter 2 with the purpose-qualified definition creates no contradiction with any of them.

## 8. Unresolved author decisions raised by R04

1. Is `state` reader-facing controlled vocabulary in Chapter 2, or is the idea taught as "what must be carried forward" with the term introduced only in Chapter 13?
2. Are `entity` and `variable` controlled vocabulary, or ordinary words used carefully?
3. Is the input/state/output **role** distinction taught, given that it is genuinely useful for representation but is also control-theory framing?
4. Is `state space` named, or withheld entirely?
5. Does the chapter adopt the role table as a standing reader artifact — and if so, does it recur in later chapters?

Decision 1 is the consequential one. Naming `state` in Chapter 2 buys precision and a clean Chapter 13 handoff; it also spends terminology budget on a word the reader will meet again in a stricter sense.
