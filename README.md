# Models, Evidence, and Decisions

**An Integrated Course in Reasoning Under Uncertainty**

## Status

Architecture baseline established.

Detailed chapter architecture and manuscript development will follow. The book architecture should be treated as stable enough to begin chapter design, but not as immune to empirical revision.

## Purpose

The book is designed for technically literate professionals and advanced students who want to reason better about unfamiliar consequential problems. The intended reader is comfortable with algebra and willing to use light computation or simulation, but does not need prior specialist training in statistics, economics, operations research, causal inference, control theory, or decision analysis.

The book is not intended to replace specialist textbooks. Its differentiated purpose is to teach:

1. formulation before technique;
2. the interfaces between established disciplines;
3. reasoning from models and evidence to decisions and action;
4. dynamic and strategic consequences of action;
5. monitoring, criticism, and revision after deployment;
6. transfer to unfamiliar problems.

A separate depth curriculum may later provide deeper technical study of specialist machinery.

## Intellectual Principle

The project does not claim to invent a new scientific discipline or unified formal theory. It is an integrated pedagogical architecture built from established concepts and terminology in fields including:

- scientific modeling;
- measurement science;
- probability;
- statistics;
- causal inference;
- econometrics;
- decision analysis;
- operations research;
- systems analysis;
- system dynamics;
- control theory;
- game theory;
- robust decision-making;
- machine learning evaluation.

Established disciplinary distinctions must be preserved. For example:

- statistical identifiability;
- causal identification;
- structural identifiability;

must remain distinct concepts.

Likewise, the book must not casually collapse:

- construct;
- measure;
- proxy;
- target;
- estimand;
- estimator;
- estimate;
- prediction;
- intervention;
- utility;
- objective;
- metric;
- robustness;
- stability;
- equilibrium;
- observability.

Pedagogical syntheses are allowed, but must be identified as pedagogical syntheses rather than presented as established formal theories.

## Book Architecture

The current architecture contains **5 parts** and **17 chapters**, at approximately:

- 500 body pages;
- 100 serious learning hours.

The intellectual progression is:

```text
Frame and Formulate
        ↓
Learn from Evidence
        ↓
Choose
        ↓
Act in Responsive Systems
        ↓
Integrate and Revise
        ↺
```

The sequence is a teaching order, not a claim that real reasoning is a one-directional pipeline. In practice, later evidence, decisions, deployment outcomes, and failures may require returning to any earlier stage.

## Part I: Frame and Formulate

### Chapter 1: Decisions, Questions, and a First Complete Pass

**Central question.** What is being asked, for what use, and what would count as an adequate answer?

**Core competence.** Frame the decision situation, identify intended use and target, distinguish relevant claim types and environment properties, and perform one informal pass through the complete reasoning process.

### Chapter 2: Representation, Mechanisms, and Scale

**Central question.** What is inside the model, at what grain, and how do parts produce behavior?

**Core competence.** Construct purpose-relative representations using boundaries, entities, variables, states, mechanisms, abstraction, aggregation, scale, and alternative representations.

### Chapter 3: Measurement and Operationalization

**Central question.** What do the numbers stand for, and how well?

**Core competence.** Connect constructs to observables through operationalization, units, proxies, validity, reliability distinctions, and measurement error.

### Chapter 4: Observation Processes and Data Provenance

**Central question.** Why did these records, and not others, come to exist in this form?

**Core competence.** Describe the observation process separately from the process being modeled, including sampling, selection, missingness, censoring, aggregation, reporting, institutional incentives, and possible manipulation.

### Chapter 5: Assumptions, Adequacy, and Rival Models

**Central question.** How could this formulation fail its purpose, and what would show it?

**Core competence.** Criticize models using assumption records, dimensional reasoning, limiting and extreme-condition checks, Fermi estimation and bounding, rival models, structural uncertainty, and predicted failure modes.

## Part II: Learn from Evidence

### Chapter 6: Probability, Prediction, and Simulation

**Central question.** How is uncertainty represented, updated, and scored?

**Core competence.** Use conditioning, Bayes, expectation, base rates, simulation, probabilistic prediction, and calibration to reason coherently under uncertainty.

### Chapter 7: Targets, Identification, and Causal Claims

**Central question.** Could ideal evidence establish the target, and under what assumptions?

**Core competence.** Define targets and estimands, distinguish statistical identifiability from causal identification, distinguish prediction from intervention and counterfactual claims, and understand experiments and observational designs as strategies for identification.

Structural identifiability is deferred to the dynamic-systems part of the book.

### Chapter 8: Estimation, Uncertainty, and Model Checking

**Central question.** What does finite evidence say, with what reliability?

**Core competence.** Use likelihood, estimation, regression, uncertainty quantification, predictive evaluation, measurement-error reasoning, analytic-flexibility awareness, and model checking without reducing evidence to threshold rituals.

### Chapter 9: Combining and Transporting Evidence

**Central question.** What do many imperfect sources jointly support — here?

**Core competence.** Reason about heterogeneous and dependent evidence, replication, evidence synthesis, expert judgment, external validity, generalizability, target populations, and transportability at an appropriate conceptual level.

## Part III: Choose

### Chapter 10: Values, Objectives, and Alternatives

**Central question.** What matters, to whom, and what options exist beyond those offered?

**Core competence.** Structure values and consequences, distinguish values from measurable objectives and metrics, identify stakeholders and constraints, and generate alternatives instead of accepting a fixed option set.

### Chapter 11: Decisions Under Uncertainty and Value of Information

**Central question.** Which act is defensible, and would more evidence change it?

**Core competence.** Use decision trees, expected utility, risk attitudes, sensitivity analysis, value of information, decision-quality reasoning, ambiguity awareness, and recognition of when further analysis itself is not worthwhile.

### Chapter 12: Optimization, Robustness, and Adaptive Plans

**Central question.** How do we choose well at scale when the model itself is uncertain?

**Core competence.** Formulate objectives and constraints, reason marginally, understand shadow-price and convexity intuition, and use scenarios, robustness, regret, adaptive plans, and computational solver handoff appropriately.

## Part IV: Act in Responsive Systems

### Chapter 13: Dynamics, Feedback, and Stability

**Central question.** How does the system evolve once acted upon?

**Core competence.** Reason about state, accumulation, stocks and flows, delay, feedback, equilibrium versus stability, oscillation, overshoot, and policy resistance.

### Chapter 14: Sequential Decisions, Information, and Control

**Central question.** How should choices be made through time as information arrives?

**Core competence.** Reason with policies rather than one-shot actions, feedback decisions, observability, structural identifiability, information acquisition, exploration versus exploitation, and control at a foundational conceptual level.

Formal dynamic programming, filtering, LQR, MPC, POMDP, and reinforcement-learning algorithms belong in the depth curriculum.

### Chapter 15: Strategic Interaction, Incentives, and Endogenous Response

**Central question.** What changes when the system contains other modelers?

**Core competence.** Reason about strategic dependence, incentives, equilibrium as consistency, commitment, information asymmetry, principal-agent relationships, delegation, endogenous response, metric gaming, Goodhart-type failures, Campbell's law, Lucas critique, and manipulation of evidence.

## Part V: Integrate and Revise

### Chapter 16: Integration: The Full Loop on Unfamiliar Problems

**Central question.** Which machinery does this problem need, and how do the pieces connect?

**Core competence.** Triage unfamiliar problems and execute the relevant reasoning process across formulation, evidence, decision, dynamics, and strategy without mechanically forcing every problem through every chapter.

This chapter should eventually contain full-loop cases, including at least one substantial automated or AI system case. AI is an application and stress test, not a separate intellectual foundation of the book.

### Chapter 17: Deployment, Monitoring, and Revision

**Central question.** Is the deployed reasoning still working — and if not, which stage failed?

**Core competence.** Design monitoring, distinguish signal from ordinary variation, recognize drift and tampering, diagnose failure by stage, define revision triggers, and return deliberately to earlier parts of the reasoning process.

Concept-level monitoring machinery may include common-cause versus special-cause variation and control-chart reasoning where appropriate.

## The Reasoning Loop

The book should repeatedly reinforce the following general pattern:

```text
Purpose / Decision
  ↓
Target and Context
  ↓
Representation
  ↓
Measurement
  ↓
Observation Process
  ↓
Assumptions and Adequacy
  ↓
Probability
  ↓
Identification
  ↓
Estimation
  ↓
Evidence Synthesis and Transport
  ↓
Values and Alternatives
  ↓
Decision
  ↓
Optimization / Robust Choice
  ↓
Dynamics
  ↓
Sequential Decision / Control
  ↓
Strategic Response
  ↓
Deployment
  ↓
Monitoring
  ↓
Revision
  ↺
```

This is a pedagogical navigation structure, not a new formal theory, and not a strict one-directional dependency graph. Real reasoning is iterative: a result discovered late in the process may invalidate an earlier representation, measurement, assumption, objective, or evidence claim, and later findings may send the reasoner back to any earlier stage. Targets themselves may be revised after representation, measurement, evidence, or deployment.

## Scope Boundary

The core book should teach readers to:

- recognize which machinery is required;
- understand why it is required;
- execute foundational versions of it;
- interpret its outputs;
- understand major assumptions and failure modes;
- know when deeper specialist methods are needed.

The book should not attempt full technical coverage of:

- measure-theoretic probability;
- advanced statistical asymptotics;
- advanced Bayesian computation;
- full psychometrics;
- formal do-calculus;
- detailed quasi-experimental estimators;
- advanced transportability algorithms;
- mathematical robust optimization;
- LP and KKT algorithms;
- stochastic dynamic programming;
- POMDP algorithms;
- reinforcement-learning algorithms;
- Kalman filtering;
- LQR or MPC;
- formal control design;
- mechanism design;
- equilibrium refinements.

Those belong in the companion depth curriculum.

## Development Principle

Every chapter should eventually distinguish among:

1. **established concepts and terminology;**
2. **pedagogical synthesis used by this book;**
3. **specialist material intentionally deferred.**

The manuscript should favor:

- production over recognition;
- worked examples followed by fading;
- prediction before explanation where pedagogically appropriate;
- self-explanation;
- contrasting cases;
- analogical transfer;
- error diagnosis;
- revision of earlier work;
- cold-transfer assessment.

Reading completion alone is not mastery.

## Current Freeze Status

Treat this architecture as the working baseline for manuscript development. Do not casually restructure parts or chapters during drafting.

The architecture should only be reopened for a genuine structural reason, such as:

- evidence that the formulation-first sequence materially harms learning;
- evidence that identification-before-estimation materially harms competence without reducing identification errors;
- a chapter proving unable to support its promised competence within the available scope;
- a major new competing work eliminating the book's intellectual differentiation.

Ordinary drafting difficulties should lead to chapter revision, not immediate architecture redesign.

## Repository Development Rules

For now:

- `README.md` is the architectural source of truth.
- Do not create manuscript chapter files yet.
- Do not invent content that has not been adjudicated.
- Do not silently change chapter names or order.
- Do not introduce novel academic terminology merely for elegance.
- Keep the repository suitable for a serious long-term book project.

The following will be designed separately, later:

- directory structure;
- chapter Markdown convention;
- citation/reference system;
- source-note system;
- research files;
- exercises;
- figures;
- computational notebooks;
- architecture/version records.

Do not preempt those decisions now.
