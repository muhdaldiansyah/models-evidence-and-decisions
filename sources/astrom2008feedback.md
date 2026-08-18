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

## Role in Chapter 13

**Extended 2026-08-18 during Chapter 13 research.** The first-edition PDF (version 2.10b) was read at printed pp. 1–4, 17–24, and 98–104, extending the pp. 27–34 reading recorded for Chapter 2. Printed page equals PDF page minus 12, calibrated against the p. 27 sentence already verified.

**The second edition was obtained and declined.** Its electronic text paginates by chapter — `5-1`, `5-2` — and renumbers the chapters, so *Dynamic Behavior* is Chapter 5 there and Chapter 4 here. Under the standing rule adopted in Chapter 9, the book cites the version whose pagination it can see, and that is the first edition named in `references.bib`.

This is Chapter 13's source for feedback, equilibrium, stability, and oscillation.

### Verified locators

- p. 1: "A dynamical system is a system whose behavior changes over time, often in response to external stimulation or forcing. The term feedback refers to a situation in which two (or more) dynamical systems are connected together such that each system influences the other and their dynamics are thus strongly coupled."
- p. 1, **the chapter's spine candidate**: "Simple causal reasoning about a feedback system is difficult because the first system influences the second and the second system influences the first, leading to a circular argument. This makes reasoning based on cause and effect tricky, and it is necessary to analyze the system as a whole. A consequence of this is that the behavior of feedback systems is often counterintuitive, and it is therefore necessary to resort to formal methods to understand them."
- p. 2: "A system is said to be a closed loop system if the systems are interconnected in a cycle... If we break the interconnection, we refer to the configuration as an open loop system"
- p. 3: "feedback can make a system resilient toward external influences... More generally, feedback allows a system to be insensitive both to external disturbances and to variations in its individual elements."
- p. 3, immediately following: "Feedback has potential disadvantages as well. It can create dynamic instabilities in a system, causing oscillations or even runaway behavior. Another drawback, especially in engineering systems, is that feedback can introduce unwanted sensor noise into the system, requiring careful filtering of signals."
- p. 17: "The principle of feedback is simple: base correcting actions on the difference between desired and actual performance."
- p. 17, on the key use: "One of the key uses of feedback is to provide robustness to uncertainty."
- p. 21: "While feedback has many advantages, it also has some drawbacks. Chief among these is the possibility of instability if the system is not designed properly."
- p. 22: "Feedback is reactive: there must be an error before corrective actions are taken." And on feedforward's condition: "Since feedforward attempts to match two signals, it requires good process models; otherwise the corrections may have the wrong size or may be badly timed."
- p. 22: "In a system with positive feedback, the increase in some variable or signal leads to a situation in which that quantity is further increased through its dynamics. This has a destabilizing effect and is usually accompanied by a saturation that limits the growth of the quantity."
- p. 23, on-off control: "It typically results in a system where the controlled variables oscillate, which is often acceptable if the oscillation is sufficiently small."
- p. 24, **the oscillation mechanism**: "The reason why on-off control often gives rise to oscillations is that the system overreacts since a small change in the error makes the actuated variable change over the full range."
- p. 100, equilibrium: "An equilibrium point of a dynamical system represents a stationary condition for the dynamics." And: "Equilibrium points are one of the most important features of a dynamical system since they define the states corresponding to constant operating conditions. A dynamical system can have zero, one or more equilibrium points."
- p. 100, the inverted pendulum as the worked example, whose equilibria alternate between pointing up and hanging down.
- p. 101, limit cycles: "Nonlinear systems can exhibit rich behavior. Apart from equilibria they can also exhibit stationary periodic solutions." And: "The figure shows that the solutions in the phase plane converge to a circular trajectory. In the time domain this corresponds to an oscillatory solution. Mathematically the circle is called a limit cycle."
- p. 102, **the definition of stability**: "The stability of a solution determines whether or not solutions nearby the solution remain close, get closer or move further away."
- p. 102: "If a solution is stable in this sense and the trajectories do not converge, we say that the solution is neutrally stable."
- p. 102, **the equilibrium-versus-stability hinge**: "An important special case is when the solution [is] an equilibrium solution. Instead of saying that the solution is stable, we simply say that the equilibrium point is stable."
- p. 104: "An asymptotically stable equilibrium point is called a sink or sometimes an attractor. An unstable equilibrium point can be either a source, if all trajectories lead away from the equilibrium point, or a saddle, if some trajectories lead to the equilibrium point and others move away."

### Chapter 13 cautions

- **The formal definitions of stable, asymptotically stable, and unstable at pp. 102–103 contain symbols, quantifiers, and arrows that mangle under text extraction and would carry comparison symbols into a quotation.** Under the standing rules adopted in Chapters 7 and 8, they are **paraphrased and not quoted**. The prose sentences listed above are quotable and are the only ones quoted.
- **Chapter 14 owns control, and the line runs through p. 24.** The oscillation mechanism on that page is a fact about correction rules and is used; the proportional, integral, and PID material that follows on the same page and the next is not taught.
- **Limit cycles are named and not developed.** `../decisions/0007` defers phase portraits and the planar machinery, and pp. 98–99 were read without being taught.
- **`positive feedback` collides with the book's `positive` / `normative` pair**, which is why `../decisions/0007` banned it from Chapter 1. Chapter 13 prefers `reinforcing` and `balancing`, names the positive/negative pair once as the terms in circulation, and gives the reason.
- **The saturation clause at p. 22 matters.** Reinforcing feedback is "usually accompanied by a saturation that limits the growth of the quantity", so a reinforcing loop is not a prediction of unbounded growth.
- **§4.4 (Lyapunov analysis) and §4.5 (parametric and nonlocal behaviour) are unread**, deliberately, and no claim is made about them.
