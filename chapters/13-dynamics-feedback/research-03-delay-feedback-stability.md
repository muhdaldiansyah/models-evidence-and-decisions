# Research 03: Delay, Feedback, Equilibrium, and Stability

Cluster 3 of four. Every locator below was taken from reading the document directly.

**Edition note.** `astrom2008feedback` is the 2008 first edition. The first-edition PDF (version 2.10b) was used; printed page equals PDF page minus 12, calibrated against the p. 27 sentence verified during Chapter 2 research. The second edition was obtained and **declined**: its electronic text paginates by chapter and renumbers the chapters, so its locators are not the bibliography entry's. Standing rule 3.

## 1. Delay

`sterman2006evidence` p. 508 is the chapter's source for delay, and it does four jobs in one paragraph.

> "Time delays in feedback processes are common and particularly troublesome. Most obviously, delays slow the accumulation of evidence. More problematic, the short- and long-run impacts of our policies are often different (smoking gives immediate pleasure, while lung cancer develops over decades). Delays also create instability and fluctuations that confound our ability to learn."

Then the mechanism, which is the paragraph the chapter is built around:

> "Driving a car, drinking alcohol, and building a new semiconductor plant all involve time delays between the initiation of a control action (accelerating/braking, deciding to 'have another,' the decision to build) and its effects on the state of the system. As a result, decision makers often continue to intervene to correct apparent discrepancies between the desired and actual state of the system even after sufficient corrective actions have been taken to restore equilibrium. The result is overshoot and oscillation: stop-and-go traffic, drunkenness, and high-tech boom and bust cycles."

**Three things the chapter must draw out.**

**The rule being followed is not stupid.** *Correct the discrepancy between desired and actual* is the same rule `astrom2008feedback` p. 17 calls the principle of feedback. The overshoot comes from applying a correct rule through a delay.

**The overshoot is not a failure of discipline.** The corrections continue "even after sufficient corrective actions have been taken" — that is, after the problem is already solved and before anyone can see that it is.

**Three examples of very different kinds.** A physical control task, a physiological one, and a capital-investment one. The book adds a fourth: a reservoir.

Also `sterman2006evidence` p. 507:

> "Characterized by trade-offs. Time delays in feedback channels mean the long-run response of a system to an intervention is often different from its short-run response. Low-leverage policies often generate transitory improvement before the problem grows worse, whereas high-leverage policies often cause worse-before-better behavior."

**"Worse-before-better" is exactly the shape a decision-maker cannot distinguish from a failing policy**, and the chapter should say so.

## 2. Feedback — the definition

`astrom2008feedback` p. 1:

> "A dynamical system is a system whose behavior changes over time, often in response to external stimulation or forcing. The term feedback refers to a situation in which two (or more) dynamical systems are connected together such that each system influences the other and their dynamics are thus strongly coupled."

And the consequence, which is the strongest sentence available for the chapter's relationship to Part II:

> "Simple causal reasoning about a feedback system is difficult because the first system influences the second and the second system influences the first, leading to a circular argument. This makes reasoning based on cause and effect tricky, and it is necessary to analyze the system as a whole. A consequence of this is that the behavior of feedback systems is often counterintuitive, and it is therefore necessary to resort to formal methods to understand them."

**This is a candidate chapter spine.** Chapter 7 spent thirty-eight pages on what it takes to establish that A causes B. This sentence says that where feedback is present, the question is not merely hard to answer — it is the wrong shape.

`astrom2008feedback` p. 2, on the two configurations:

> "A system is said to be a closed loop system if the systems are interconnected in a cycle... If we break the interconnection, we refer to the configuration as an open loop system"

## 3. Feedback — what it gives and what it costs

`astrom2008feedback` p. 3:

> "Feedback has many interesting properties that can be exploited in designing systems. As in the case of glucose regulation or the flyball governor, feedback can make a system resilient toward external influences. It can also be used to create linear behavior out of nonlinear components, a common approach in electronics. More generally, feedback allows a system to be insensitive both to external disturbances and to variations in its individual elements."

Immediately followed, on the same page, by:

> "Feedback has potential disadvantages as well. It can create dynamic instabilities in a system, causing oscillations or even runaway behavior. Another drawback, especially in engineering systems, is that feedback can introduce unwanted sensor noise into the system, requiring careful filtering of signals."

**Two paragraphs, one page, opposite directions.** This is a new instance of a shape the book has now seen six times — the property that buys you one thing costs you another — and here the source states both halves itself.

The principle, `astrom2008feedback` p. 17:

> "The principle of feedback is simple: base correcting actions on the difference between desired and actual performance."

And the drawback restated at p. 21:

> "While feedback has many advantages, it also has some drawbacks. Chief among these is the possibility of instability if the system is not designed properly."

## 4. Reinforcing and balancing

`astrom2008feedback` p. 22:

> "In a system with positive feedback, the increase in some variable or signal leads to a situation in which that quantity is further increased through its dynamics. This has a destabilizing effect and is usually accompanied by a saturation that limits the growth of the quantity."

`sterman2006evidence` p. 507 names the same pair in the other tradition's words:

> "Like organisms, social systems contain intricate networks of feedback processes, both self-reinforcing (positive) and self-correcting (negative) loops. However, studies show that people think in short, causal chains, tend to assume each effect has a single cause, and often cease their search for explanations when the first sufficient cause is found."

**The terminology decision.** `positive feedback` and `negative feedback` are the established engineering terms and would collide with the book's `positive` / `normative` pair — which is why `decisions/0007` banned them from Chapter 1. Both sources supply an alternative in the same breath: *self-reinforcing* and *self-correcting*. Recommendation is that the book use **reinforcing** and **balancing**, name the positive/negative pair once, and give the reason.

**Note the saturation clause.** Reinforcing feedback is "usually accompanied by a saturation that limits the growth" — so a reinforcing loop is not a prediction of unbounded growth, and the chapter must not let readers take it as one.

## 5. Feedback is reactive; feedforward is not

`astrom2008feedback` p. 22:

> "Feedback is reactive: there must be an error before corrective actions are taken. However, in some circumstances it is possible to measure a disturbance before it enters the system, and this information can then be used to take corrective action before the disturbance has influenced the system."

And the cost:

> "Since feedforward attempts to match two signals, it requires good process models; otherwise the corrections may have the wrong size or may be badly timed."

**A very clean connection to Part I.** Feedforward is what the book has been doing for twelve chapters — acting on a model rather than on an error — and this source states the condition under which it works.

## 6. Equilibrium

`astrom2008feedback` p. 100:

> "An equilibrium point of a dynamical system represents a stationary condition for the dynamics."

> "Equilibrium points are one of the most important features of a dynamical system since they define the states corresponding to constant operating conditions. A dynamical system can have zero, one or more equilibrium points."

**"Zero, one or more" is doing real work.** A reader who thinks equilibrium is a property a system either reaches or fails to reach has not understood that a system can have several, and that which one it is near matters.

Same page, the inverted pendulum, whose equilibria alternate between pointing up and hanging down. **This is the standing counterexample from `decisions/0007` arriving in the source's own text**, which is a convenience the chapter should use and note.

## 7. Stability — the definition, and the three grades

`astrom2008feedback` p. 102:

> "The stability of a solution determines whether or not solutions nearby the solution remain close, get closer or move further away."

The three grades, in the source's words, symbols removed:

**Stable** (in the sense of Lyapunov) — a solution is stable if other solutions that start near it stay close to it. p. 102. And, crucially:

> "Note that this definition does not imply that [the nearby solution] approaches [the reference solution] as time increases but just that it stays nearby."

The bracketed substitutions replace symbols; **the chapter must paraphrase this rather than quote it**, under standing rule 2.

**Neutrally stable** — p. 102: "If a solution is stable in this sense and the trajectories do not converge, we say that the solution is neutrally stable."

**Asymptotically stable** — p. 103, paraphrased: stable in the sense of Lyapunov, and in addition nearby solutions converge to it over time. The source's sentence contains symbols and an arrow and is not quotable.

**Unstable** — p. 103: "A solution x(t; a) is unstable if it is not stable." Contains inline symbols; paraphrase.

The equilibrium-versus-stability hinge, `astrom2008feedback` p. 102:

> "An important special case is when the solution [is] an equilibrium solution. Instead of saying that the solution is stable, we simply say that the equilibrium point is stable."

**This is the distinction the core competence names.** Equilibrium is a property of a *point* — nothing changes if you are exactly there. Stability is a property of the *solutions near* that point — what happens if you are not exactly there, which you never are.

Local versus global, p. 103, paraphrased: a solution is locally stable if it is stable for starting points within some ball around it, and the system is globally stable if this holds for every radius.

Names for the planar cases, p. 104:

> "An asymptotically stable equilibrium point is called a sink or sometimes an attractor. An unstable equilibrium point can be either a source, if all trajectories lead away from the equilibrium point, or a saddle, if some trajectories lead to the equilibrium point and others move away."

## 8. Oscillation

Two mechanisms, from two directions.

**Overreaction through a full-range correction**, `astrom2008feedback` p. 24:

> "The reason why on-off control often gives rise to oscillations is that the system overreacts since a small change in the error makes the actuated variable change over the full range."

And p. 23, on the on-off rule: "It typically results in a system where the controlled variables oscillate, which is often acceptable if the oscillation is sufficiently small."

**Sustained periodic behaviour with no external forcing**, `astrom2008feedback` p. 101:

> "Nonlinear systems can exhibit rich behavior. Apart from equilibria they can also exhibit stationary periodic solutions."

> "The figure shows that the solutions in the phase plane converge to a circular trajectory. In the time domain this corresponds to an oscillatory solution. Mathematically the circle is called a limit cycle."

**The chapter uses the first and names the second.** The on-off mechanism is a fact about correction rules and belongs here; limit cycles require the phase-plane machinery Decision 0007 defers.

**And the Chapter 14 line runs through p. 24.** The same page that supplies the oscillation mechanism goes on to develop proportional, integral, and PID control. The chapter takes the sentence and leaves the controller.

## 9. What was not taken

- §4.4 Lyapunov analysis and §4.5 parametric and nonlocal behaviour — unread, deliberately.
- Phase portraits and vector fields, pp. 98–99 — read, not taught. Decision 0007 defers the machinery.
- PID control, pp. 23–24 — read so the line could be drawn; not taught.
- The congestion-control worked example, p. 104 — read, not used.
- Chapters 5 onward of the source, entirely.
