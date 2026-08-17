# Source Note: astrom2008feedback

## Citation

Karl J. Åström and Richard M. Murray. 2008. *Feedback Systems: An Introduction for Scientists and Engineers*. Princeton University Press.

## Verification

Verified against the official Caltech author/textbook site and its citation-information page.

Verified metadata:
- authors: Karl J. Åström and Richard M. Murray;
- title: *Feedback Systems: An Introduction for Scientists and Engineers*;
- publisher: Princeton University Press;
- year: 2008.

**Upgraded 2026-08-18 during Chapter 2 research.** The first-edition text was subsequently inspected page by page, so the Chapter 2 locators below are verified against printed pages rather than against the publisher's summary. Chapter 1's use of this source is unchanged.

The official Chapter 1 summary defines feedback through interconnected dynamical systems whose behavior influences one another. It also describes the sensing–computation–actuation loop in engineered control, notes that feedback can provide robustness and shape dynamics, and warns that feedback can also introduce instability, sensor-noise coupling, and additional system complexity.

## Role in Chapter 1

This source supports a controlled systems meaning of `feedback` distinct from ordinary evaluative comments or reviewer feedback.

At Chapter 1 depth, the book uses the introductory idea that consequences of a process or action can return through the system and influence later behavior, outcomes, information, or actions.

The source also supports deferring formal feedback-control analysis: stability, controller design, state feedback, output feedback, and observability are later topics.

## Role in Chapter 2

This is Chapter 2's engineering-side source for purpose-relative representation and for the controlled meaning of `state`.

- supports the claim that which model is right depends on the question being asked, stated by an engineering textbook rather than by philosophy of science;
- supports the existence of **multiple models of one system at different fidelities**, chosen by use;
- supplies the canonical control-theory definition of `state`, which is itself purpose-qualified;
- supports the point that grain is a decision — how accurately storage must be represented is chosen, not discovered;
- supports the point that where a boundary is drawn changes the internal description, because states can disappear when components are connected.

### Verified locators (first edition, printed pages)

- Ch. 2 opening, printed p. 27: "A model is a precise representation of a system's dynamics used to answer questions via analysis and simulation. The model we choose depends on the questions we wish to answer, and so there may be multiple models for a single dynamical system, with different levels of fidelity depending on the phenomena of interest."
- §2.1, printed p. 27: "A model is a mathematical representation of a physical, biological or information system. Models allow us to reason about a system and make predictions about how a system will behave."
- Ch. 2 epigraph, printed p. 27: Dyson's report of Fermi's objection, and von Neumann's "with four parameters I can fit an elephant, and with five I can make him wiggle his trunk" — usable as an established anecdote that added parameters are not added credibility.
- §2.1 "The Heritage of Mechanics", printed p. 28: "The state of a dynamical system is a collection of variables that completely characterizes the motion of a system for the purpose of predicting future motion." The set of all possible states is called the state space.
- §2.1, printed p. 28: for the spring–mass system, "The position q and velocity q̇ represent the instantaneous state of the system."
- §2.1, printed p. 29: "Adding the input makes the model richer and allows new questions to be posed."
- §2.1, printed p. 32: "Because of these different uses of models, it is common to use a hierarchy of models having different complexity and fidelity"; "other uses of models may require more complexity and more accuracy."
- §2.1 "Multidomain Modeling", printed p. 32: multidomain systems are modelled by "partitioning a system into smaller subsystems", with interface behaviour described where subsystems are interconnected.
- §2.1, printed p. 33: "states may disappear when components are connected. This implies that the internal description of a component may change when it is connected to other components." Two capacitors in parallel are given as the illustration.
- §2.2, printed p. 34: "The state of a system is a collection of variables that summarize the past of a system for the purpose of predicting the future. For a physical system the state is composed of the variables required to account for storage of mass, momentum and energy. A key issue in modeling is to decide how accurately this storage has to be represented."

## Cautions

- Chapter 1 does not teach open-loop/closed-loop mathematics, feedback-controller design, PID control, or stability analysis.
- Do not introduce `positive feedback` or `negative feedback` in Chapter 1; those are technical systems terms and would also create avoidable ambiguity with the book's positive/normative terminology.
- Formal dynamical feedback belongs primarily to Chapter 13; engineered sensing/control specialization belongs to Chapter 14.

### Chapter 2 cautions

- The book's `state` is introduced at Chapter 2 as *what must be carried forward to answer the question*. Åström and Murray's definition is stated for **dynamical** systems and is tied to predicting future motion; Chapter 2 must not silently widen it into "any variable."
- Do not import state-space notation, order of a system, phase portraits, linearity, LTI form, reachability, or observability into Chapter 2. Those are Chapters 13–14 and the depth curriculum.
- The printed p. 27 sentence is the strongest available warrant for purpose-relative model choice, but it is stated about **dynamical systems models for analysis and simulation**. Chapter 2 applies it more broadly; that widening is the book's own pedagogical synthesis.
- The p. 33 point about disappearing states is a compositional-modelling observation, not a general claim that boundaries always change internal descriptions. Use it as an illustration, not a law.
