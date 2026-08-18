# Models, Evidence, and Decisions

**An Integrated Course in Reasoning Under Uncertainty**

The book teaches technically literate professionals and advanced students to reason about unfamiliar consequential problems: working out what is actually being asked, what the available records can and cannot support, what a decision requires beyond evidence, and what to revise when action changes the system being acted on.

The intended reader is comfortable with algebra and willing to use light computation or simulation, but does not need prior specialist training in statistics, economics, operations research, causal inference, control theory, or decision analysis.

The book is not intended to replace specialist textbooks. Its differentiated purpose is to teach:

1. formulation before technique;
2. the interfaces between established disciplines;
3. reasoning from models and evidence to decisions and action;
4. dynamic and strategic consequences of action;
5. monitoring, criticism, and revision after deployment;
6. transfer to unfamiliar problems.

It is an integrated pedagogical architecture built from established concepts — not a proposed new discipline or unified formal theory — and it preserves the disciplinary distinctions it draws on rather than collapsing them for elegance (see [Intellectual Principle](#intellectual-principle)). A separate depth curriculum may later provide deeper technical study of specialist machinery.

## Start Here

**To read the book.** **Part I is complete** — five chapters, written to be read in order:

> **[Chapter 1 — Decisions, Questions, and a First Complete Pass](chapters/01-decisions-questions/chapter.md)** — six sections, about four learning hours including exercises.
>
> **[Chapter 2 — Representation, Mechanisms, and Scale](chapters/02-representation-mechanisms/chapter.md)** — seven sections, about six learning hours.
>
> **[Chapter 3 — Measurement and Operationalization](chapters/03-measurement-operationalization/chapter.md)** — seven sections, about five learning hours.
>
> **[Chapter 4 — Observation Processes and Data Provenance](chapters/04-observation-provenance/chapter.md)** — seven sections, about five learning hours.
>
> **[Chapter 5 — Assumptions, Adequacy, and Rival Models](chapters/05-assumptions-rival-models/chapter.md)** — seven sections, about five learning hours.

All five work one case: a small municipal water utility during a seven-day heatwave.

Chapter 1 frames the decision and discovers that the storage reading it depends on may be wrong. Chapter 2 asks what belongs inside a representation of that utility, and finds that the picture which answered Chapter 1's question cannot express who loses service first. Chapter 3 opens a phrase Chapter 2 deliberately left standing — *adequate or not* — and shows the utility's records calling a zone adequately served because of where an instrument happened to be installed. Chapter 4 turns on a figure the reader has been using since Chapter 2 and shows that it was never measured at all: it is a subtraction residual, arithmetically correct, containing about a third of things that are neither Hillcrest nor demand.

Chapter 5 introduces nothing and criticizes what the other four built. Its centrepiece is a division nobody performed for four chapters — two numbers already on the page, which turn out to imply about five times a plausible household's water use, and whose reconciliation reveals an option the entire analysis had no way to express.

Read each manuscript in order rather than skimming. All three open by asking you to produce something unaided — a first-pass analysis, a representation, a definition — before any of the chapter's vocabulary arrives, and later exercises compare against what you wrote. Skipping that opening costs you the comparison.

Each drafted chapter carries the same four exercise files beside its manuscript — `transfer-form-a.md` and `transfer-form-b.md` (parallel unfamiliar-domain cases), `transfer-rubric.md` (scoring; open it only after you have written your own analysis), and `diagnosis-feedback.md` (the discussion for the diagnosis exercise). The chapter links each one at the moment it is needed. The transfer exercises and their delayed retests only work on material you have not seen, so let the manuscript decide when you open them. Everything else in a chapter directory is authoring and validation scaffolding; some of it discusses the exercises' answers, so if you intend to do the exercises, stay out of it until you have finished the delayed retest.

**To work on the project.** Authority runs `README.md → decisions/ → canon/ → chapter spec.md → working files`; the operating contract is [CLAUDE.md](CLAUDE.md).

- [`decisions/`](decisions/) — settled decisions and their reopening conditions, indexed by scope: three book-level, five governing Chapter 1, and four proposed for Chapters 2–5.
- [`canon/`](canon/) — controlled terminology and registered pedagogical syntheses.
- [`chapters/`](chapters/) — one directory per chapter; `spec.md` is each chapter's contract.
- [`references.bib`](references.bib) and [`sources/`](sources/) — one global bibliography; one note per source, named by citation key.

Chapter 1's directory, still the most developed, shows the kinds of file a chapter accumulates. Chapters 2 and 3 carry the same kinds, minus the validation instruments and with their research split across separate dossiers rather than a single notes file.

- **Manuscript** — `chapter.md`. The chapter itself; the only file a reader opens directly.
- **Exercise materials** — `transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, `diagnosis-feedback.md`. Linked from the manuscript at the moment they are needed.
- **Chapter contract** — `spec.md`. Governed scope, section architecture, and design targets.
- **Authoring controls** — `anchor.md`, `case-data.md`, `decision-framing.md`, `dynamics-response.md`, `learning-sequence.md`, `transfer.md`. Frozen case facts and boundary rules implementing Decisions 0004–0008.
- **Validation instruments** — `freeze-gates.md`, `sme-review-water-anchor.md`, `pilot-protocol.md`, `pilot-data-capture.md`, `validation-handoff.md`. The evidence trail from drafted toward frozen.
- **Research and drafting** — `drafting-blueprint.md`, plus `notes.md` in Chapter 1 and `readiness-audit.md`, `research-plan.md`, and numbered `research-0N-*.md` dossiers in Chapters 2 and 3.

## Current State

Last reviewed 2026-08-18.

- The 5-part, 17-chapter architecture is frozen for drafting ([Decision 0001](decisions/0001-book-architecture-freeze.md)).
- **Chapter 1 is fully drafted** and awaiting external validation: before it can be frozen, its water-utility anchor case needs a human subject-matter-expert review and its exercise design needs reader-pilot data ([freeze gates](chapters/01-decisions-questions/freeze-gates.md); gates 1–3 open).
- **Part I is fully drafted.** Chapters 2–5 rest on specifications and terminology blocks that remain **provisional**: Decisions [0009](decisions/0009-chapter2-representation-terminology-and-boundary.md), [0010](decisions/0010-chapter3-measurement-terminology-and-boundary.md), [0011](decisions/0011-chapter4-observation-process-terminology-and-boundary.md), and [0012](decisions/0012-chapter5-criticism-terminology-and-boundary.md) propose those chapters' controlled vocabulary, scope boundaries, and example architecture, and none has been author-adjudicated.
- Chapters 6–17 exist as skeleton specs: governed title, central question, core competence, and page and hour targets, with content architecture still open.

| Part | Ch. | Chapter and central question | Status |
|---|---:|---|---|
| I | 1 | **[Decisions, Questions, and a First Complete Pass](chapters/01-decisions-questions/chapter.md)**<br>What is being asked, for what use, and what would count as an adequate answer? | **Drafted** — [in validation](chapters/01-decisions-questions/freeze-gates.md) |
| I | 2 | **[Representation, Mechanisms, and Scale](chapters/02-representation-mechanisms/chapter.md)**<br>What is inside the model, at what grain, and how do parts produce behavior? | **Drafted** — [decision pending](decisions/0009-chapter2-representation-terminology-and-boundary.md) |
| I | 3 | **[Measurement and Operationalization](chapters/03-measurement-operationalization/chapter.md)**<br>What do the numbers stand for, and how well? | **Drafted** — [decision pending](decisions/0010-chapter3-measurement-terminology-and-boundary.md) |
| I | 4 | **[Observation Processes and Data Provenance](chapters/04-observation-provenance/chapter.md)**<br>Why did these records, and not others, come to exist in this form? | **Drafted** — [decision pending](decisions/0011-chapter4-observation-process-terminology-and-boundary.md) |
| I | 5 | **[Assumptions, Adequacy, and Rival Models](chapters/05-assumptions-rival-models/chapter.md)**<br>How could this formulation fail its purpose, and what would show it? | **Drafted** — [decision pending](decisions/0012-chapter5-criticism-terminology-and-boundary.md) |
| II | 6 | **[Probability, Prediction, and Simulation](chapters/06-probability-simulation/spec.md)**<br>How is uncertainty represented, updated, and scored? | Spec skeleton |
| II | 7 | **[Targets, Identification, and Causal Claims](chapters/07-targets-identification/spec.md)**<br>Could ideal evidence establish the target, and under what assumptions? | Spec skeleton |
| II | 8 | **[Estimation, Uncertainty, and Model Checking](chapters/08-estimation-uncertainty/spec.md)**<br>What does finite evidence say, with what reliability? | Spec skeleton |
| II | 9 | **[Combining and Transporting Evidence](chapters/09-evidence-synthesis/spec.md)**<br>What do many imperfect sources jointly support — here? | Spec skeleton |
| III | 10 | **[Values, Objectives, and Alternatives](chapters/10-values-alternatives/spec.md)**<br>What matters, to whom, and what options exist beyond those offered? | Spec skeleton |
| III | 11 | **[Decisions Under Uncertainty and Value of Information](chapters/11-decisions-voi/spec.md)**<br>Which act is defensible, and would more evidence change it? | Spec skeleton |
| III | 12 | **[Optimization, Robustness, and Adaptive Plans](chapters/12-optimization-robustness/spec.md)**<br>How do we choose well at scale when the model itself is uncertain? | Spec skeleton |
| IV | 13 | **[Dynamics, Feedback, and Stability](chapters/13-dynamics-feedback/spec.md)**<br>How does the system evolve once acted upon? | Spec skeleton |
| IV | 14 | **[Sequential Decisions, Information, and Control](chapters/14-sequential-control/spec.md)**<br>How should choices be made through time as information arrives? | Spec skeleton |
| IV | 15 | **[Strategic Interaction, Incentives, and Endogenous Response](chapters/15-strategic-interaction/spec.md)**<br>What changes when the system contains other modelers? | Spec skeleton |
| V | 16 | **[Integration: The Full Loop on Unfamiliar Problems](chapters/16-integration-full-loop/spec.md)**<br>Which machinery does this problem need, and how do the pieces connect? | Spec skeleton |
| V | 17 | **[Deployment, Monitoring, and Revision](chapters/17-deployment-monitoring/spec.md)**<br>Is the deployed reasoning still working — and if not, which stage failed? | Spec skeleton |

Stages: **spec skeleton** (governed title, question, competence, and targets only) → **in research** (bounded pre-drafting research) → **drafting** → **drafted — in validation** (manuscript complete; external evidence pending) → **frozen**. Update a chapter's row, and the date above, in the same commit that moves the chapter across a stage boundary.

Chapter names link to the manuscript where one exists, otherwise to that chapter's `spec.md`. This table restates governed titles and central questions for orientation; the per-chapter blocks below remain the full architectural record.

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

The architecture should only be reopened for a genuine structural reason; the reopening conditions are recorded in [Decision 0001](decisions/0001-book-architecture-freeze.md).

Ordinary drafting difficulties should lead to chapter revision, not immediate architecture redesign.

## Governance

- `README.md` is the architectural source of truth for the book: parts, chapters, sequence, and freeze status. Chapter titles, central questions, and core competences must remain synchronized between this file and each chapter's `spec.md`; conflicts are surfaced, not silently resolved.
- The operating contract — authority order, intellectual rules, source discipline, writing conventions — is [CLAUDE.md](CLAUDE.md).
- Architectural change goes through a decision record in [`decisions/`](decisions/), never through silent edits here; each record carries its own reopening conditions.
- The manuscript must conform to [`canon/`](canon/): introducing or varying a term requires an entry in the terminology registry, and pedagogical syntheses must be labeled as such rather than presented as established theory.
- Repository structure and the citation system are settled by [Decision 0002](decisions/0002-repository-architecture.md) and [Decision 0003](decisions/0003-citation-and-source-note-system.md); new top-level systems require demonstrated need.
