---
chapter: 1
part: 1
title: "Decisions, Questions, and a First Complete Pass"
status: specified
pages_target: 24
hours_target: 4
---

# Chapter 1: Decisions, Questions, and a First Complete Pass

## Central question

What is being asked, for what use, and what would count as an adequate answer?

## Core competence

Frame the decision situation, state the intended use, specify the target of the inquiry in qualified terms, distinguish relevant claim types and environment properties at intuitive depth, and perform one informal pass through the complete reasoning process.

## Role in the book

This chapter is the book's orientation, initial diagnostic, and first production experience.
Its unique job is to change the reader's default response to an unfamiliar consequential problem from immediate technique selection to explicit problem framing and disciplined routing.

The chapter must accomplish five things.

1. Establish that a topic, a question, a claim, and a decision situation are not the same object.
2. Make intended use, decision relevance, target, context, time horizon, stakeholders, consequences of error, and provisional adequacy criteria explicit before technical analysis begins.
3. Give the reader a layered way to distinguish positive from normative questions, associational or predictive claims from interventional or counterfactual claims, and non-adaptive environments from environments containing adaptive or strategic agents.
4. Let the reader experience one complete but deliberately informal pass through formulation, evidence, choice, action, monitoring, criticism, and revision before later chapters decompose the required machinery.
5. Teach routing and iteration: not every problem needs every method, and discoveries made late in the analysis can force revision of an earlier target, representation, measurement, observation process, assumption, objective, or action.

The chapter is not a compressed survey of the remaining sixteen chapters.
It should create questions that later chapters answer, not front-load their terminology or techniques.
The reader should leave with a usable first-pass analysis of a new problem and a map of what must be learned next, while remaining appropriately aware of how much has not yet been established.

The Reasoning Loop introduced here is explicitly the book's pedagogical synthesis, as registered in `../../canon/pedagogy.md`.
It is a navigation device assembled from established distinctions, not a new formal theory, universal ontology, mandatory checklist, or one-directional workflow.

## Hard prerequisites

- Ordinary algebra, ratios, units, and the ability to interpret a simple table or graph.
- Ability to read a short real-world case and write a brief justification for a choice.
- Willingness to state assumptions and uncertainty without immediately resolving them.
- No prior probability, statistics, causal inference, economics, decision theory, optimization, control, game theory, or programming is required.
- No domain expertise in the worked cases is required; all case-specific facts needed for the reasoning task must be supplied in the chapter.

## Soft dependencies / spiral links

Chapter 1 introduces questions and distinctions at intuitive depth that later chapters formalize or operationalize.

| Spiral element | Treatment in Chapter 1 | Later development |
|---|---|---|
| Intended use and adequacy for the stated use | State who will use an answer, for what judgment or action, and what would count as good enough | Chapters 2–5, 10–12, 16–17 |
| Target and context | State who or what the answer concerns and what about it is being sought; add population, application context, horizon, comparison, or resolution when material | Chapters 3, 7, 9–11 |
| Representation | Ask what must be represented and whether another representation would answer a different question | Chapters 2 and 5 |
| Measurement and observation | Distinguish the target from recorded traces and ask how the records arose | Chapters 3, 4, and 8 |
| Uncertainty | Locate major unknowns qualitatively and ask which ones could change the conclusion | Chapters 6, 8, 11–14 |
| Claim type and identification | Distinguish what is being described, predicted, changed, or compared counterfactually; ask whether the available evidence could answer it | Chapters 6 and 7 |
| Evidence strength and transfer | Ask what finite evidence supports and whether it applies in the relevant application context | Chapters 8 and 9 |
| Values, alternatives, and decision relevance | Separate what evidence says from what should be done; identify who bears consequences and whether the option set is adequate | Chapters 10 and 11 |
| Constraints, robustness, and tractability | Ask whether a proposed action is feasible and whether its conclusion survives plausible changes | Chapter 12 |
| State, time, and feedback | Screen for accumulation, delay, feedback, and repeated decisions | Chapters 2, 13, and 14 |
| Strategic or adaptive response | Ask whether people or institutions will respond to the model, intervention, rule, or metric | Chapter 15 |
| Criticism, monitoring, and revision | Predict possible failure, identify what would be monitored, and show backward movement through the reasoning process | Chapters 5, 8, 16, and 17 |

The intended-use statement and first-pass analysis produced in this chapter should be revisited after Part I, after Part III, and in Chapters 16–17.
Those returns provide evidence of learning and expose whether later technical knowledge actually improves formulation.

## Established concepts to cover

### Problem and decision framing

- Decision situation or decision context: who faces what judgment or action, under what conditions.
- Intended use for a model or simulation, extended by this book as a pedagogical synthesis to an analysis, estimate, forecast, or recommendation.
- Relevant application context in ordinary language; formal `context of use (COU)` is an optional field-specific preview whose formal treatment belongs to Chapter 5.
- Decision-maker, affected stakeholders, candidate actions or alternatives, consequences, constraints, time horizon, and consequences of error.
- Assessment of whether a model or analysis is adequate for the stated intended use and relevant application context; Chapter 1 uses this as disciplined reader-facing language rather than a universal standardized adequacy framework.
- Overall adequacy cannot be judged without a stated use. Some properties, such as internal consistency, dimensional correctness, or numerical correctness, may be assessed independently, but whether a model or analysis is adequate depends on what it will be used for.
- Distinction among a broad topic, a practical concern, a research or analytical question, a claim, and a decision.
- `Target` is Chapter 1's informal organizing word for what an inquiry is trying to determine about a focal entity, unit, population, or system; the book-wide use is a pedagogical synthesis, not one universal disciplinary technical definition.
- Qualify the target whenever possible using the substantive object actually sought, such as a quantity, event, state, outcome, relationship, comparison, population, or system.
- A minimally usable target specification states who or what the answer concerns and what about it is being sought, then adds context, horizon, resolution or aggregation, comparator, population, required answer form, or threshold only when changing that qualifier would materially change the question.
- Keep intended use, target, relevant application context, and adequacy for the stated intended use distinct.
- Distinguish the sought target from what is measured or recorded; formal construct, measure, operationalization, proxy, validity, and reliability treatment belongs to Chapter 3.
- Preview that later statistical and causal work may require a precisely defined target of estimation. Do not require the term `estimand` in Chapter 1; formal treatment belongs to Chapter 7.

### Layered question and environment triage

- Begin with the ordinary-language contrast between what is, was, or would happen and what should count as better, acceptable, important, or preferable, or what should be done.
- Introduce `positive` and `normative` only after that contrast; apply the labels to components or subquestions rather than forcing an entire problem into one mutually exclusive category.
- A positive component concerns what is, was, or would happen under specified conditions. Positive is broader than descriptive: predictive, interventional, and counterfactual questions can also be positive when they ask what would happen.
- A normative component concerns what should matter, what should count as better or acceptable, or what should be done; do not reduce normative reasoning to mere opinion.
- Descriptive and associational questions.
- Predictive questions about unknown or future outcomes.
- Interventional questions about what would happen under an action.
- Counterfactual questions about what would have happened under a different action or condition.
- Explanatory aims and mechanism claims, without treating explanation as a mutually exclusive question category.
- Non-adaptive physical or natural processes versus settings containing adaptive or strategic agents.
- Static or one-shot settings versus problems involving time, accumulation, feedback, repeated choice, or learning.

These distinctions form layered prompts, not one exhaustive and mutually exclusive taxonomy.
The positive/normative layer is orthogonal to the claim-type layer: description, association, prediction, intervention effects, and counterfactual comparisons may all be positive when they ask what is or would happen.
A single decision problem may contain a predictive subproblem, an interventional claim, normative trade-offs, dynamic feedback, and strategic response simultaneously.

### First-pass relationships among models, evidence, and decisions

- Target system versus model of the target system.
- Target quantity or outcome versus what is measured or recorded.
- Process being modeled versus process producing the observed records.
- Model implication versus observation.
- Ideal evidence question versus finite-evidence question, introduced without the formal terminology of identification and estimation.
- Evidence or model claims about consequences versus the evaluative premises used to judge those consequences.
- Recommendation as a decision conclusion that may depend on both consequence claims and evaluative or decision premises; do not present a recommendation as if it followed from evidence alone.
- Supplied alternatives versus the need to search for or construct alternatives.
- One-shot action versus policy or contingent action through time.
- Prediction before deployment versus behavior after deployment changes incentives or information.
- Parameter or input adjustment versus revision of the question, target, boundary, representation, observation process, structural assumption, or objective, introduced only as an intuitive distinction.

### Metacognitive and procedural competence

- Prediction before explanation: require the reader to commit to an initial framing before seeing the worked analysis.
- Assumption surfacing and rival initial formulations.
- Qualitative sensitivity: which answer would change if a key assumption changed.
- Decision relevance of information: whether learning something could change the action, introduced without formal value-of-information calculations.
- Specialist handoff: recognizing when an answer requires machinery not yet learned or expertise outside the book.
- Iteration and recorded revision rather than silent replacement of earlier reasoning.

## Terminology to introduce or stabilize

The terminology burden must remain low.
Terms listed as previews may be used in ordinary language but must not receive their formal treatment here.
Any term requiring book-wide control must be flagged for canon review before drafting and added and verified before the chapter is declared stable or frozen.

| Term | Treatment in Chapter 1 | Distinction or caution |
|---|---|---|
| intended use | Required vocabulary; introduce and use throughout | Established in modeling and simulation; this book's extension to analyses, estimates, forecasts, and recommendations is explicitly a pedagogical synthesis; must name the use of the answer, not merely the topic being studied |
| context of use (COU) | Optional field-specific preview only | Established in computational M&S VVUQ / model credibility; readers need not memorize it; formal treatment belongs to Chapter 5; do not treat it as a universal synonym for intended use |
| decision situation / decision context | Introduce at practical depth | Includes decision-maker, stakeholders, alternatives, consequences, constraints, information, and horizon; not every analytical question immediately implies a decision |
| target | Required informal organizing vocabulary; qualify whenever possible | Book-wide sense is pedagogical synthesis, not one universal technical definition; distinguish from construct, measure, proxy, estimand, estimator, estimate, response variable, decision, objective, and metric |
| target quantity | Use when the sought object is literally a quantity | Ordinary qualifying phrase; not a synonym for estimand and not suitable for every inquiry |
| target population | Introduce intuitively when inference or generalization concerns a population | Established qualified term; distinct from observed sample and data-collection setting; formal development later |
| target system | Introduce at orientation depth when the inquiry concerns a system | The target system is not its model; detailed boundary work belongs to Chapter 2 |
| estimand | Concept preview only; term not required | A later formal target of estimation; exact disciplinary definitions vary; formal home Chapter 7 |
| estimator | Do not formally introduce | Method or rule for estimation; Chapter 8 |
| estimate | Ordinary language only if unavoidable; formal stabilization later | Numerical result, distinct from estimand and estimator; Chapter 8 |
| question of interest / quantity of interest | Optional field-specific examples only | Use only when accurately reporting a framework that uses them; do not make either the Chapter 1 umbrella |
| relevant application context | Use in ordinary language | Settled in Research 01; do not replace it with a new formal `target context` term |
| adequacy | Use reader-facing wording such as `adequate for the stated intended use` | Disciplined Chapter 1 language, not one universal standardized adequacy framework; distinct from literal truth, empirical fit alone, accuracy, verification, validation, applicability, credibility, and formal model checking |
| positive | Required vocabulary after an ordinary-language contrast | Established paired terminology in economics; use mainly for components or subquestions; not synonymous with descriptive, factual, objective, certain, favorable, or universally value-free |
| normative | Required vocabulary after an ordinary-language contrast | Established paired terminology in economics with broader discipline-specific uses; concerns what should matter or be done; not synonymous with mere opinion and not a universal synonym for `prescriptive` |
| association / associational claim | Introduce at intuitive depth | Association does not by itself establish the consequence of intervention |
| prediction | Preview only | Formal probabilistic prediction and calibration begin in Chapter 6; prediction is not synonymous with explanation or intervention |
| intervention | Preview only | Formal causal treatment begins in Chapter 7 |
| counterfactual | Preview only | Formal causal treatment begins in Chapter 7; do not use as a loose synonym for any hypothetical scenario |
| alternative | Introduce as a possible action or course of action | Alternative generation and value-focused thinking belong to Chapter 10 |
| consequence | Introduce at practical depth | Evidence may inform consequences, but values are needed to evaluate them |
| adaptive agent / strategic agent | Preview as an environment property | Formal strategic interaction, equilibrium, and incentives belong to Chapter 15 |
| Reasoning Loop | Introduce explicitly as pedagogical synthesis | It is a revisable navigation structure, not an established formal theory or mandatory waterfall |

Do not require `estimand` or formally introduce `estimator`, `utility`, `objective function`, `identification`, `structural identifiability`, `observability`, `equilibrium`, or `robust optimization` in this chapter.
Do not introduce `prescriptive` as a synonym for `normative`; later decision theory may use it in a more specialized sense.
Where the first complete pass needs their underlying questions, use ordinary language and point to the later chapter that owns the formal term.

## Interfaces with other chapters

| Later chapter | Interface established here | Boundary that Chapter 1 must respect |
|---|---|---|
| Ch. 2: Representation, Mechanisms, and Scale | Purpose constrains boundaries, abstraction, variables, mechanisms, state, and scale | Do not teach the detailed representation taxonomy or state sufficiency tests here |
| Ch. 3: Measurement and Operationalization | The target is not automatically what a number records; objectives and metrics may be proxies | Do not teach validity, reliability, latent-variable models, or measurement-error mathematics here |
| Ch. 4: Observation Processes and Data Provenance | Ask why these records, rather than others, came to exist in this form | Do not inventory sampling, selection, missingness, censoring, aggregation, and reporting mechanisms in depth here |
| Ch. 5: Assumptions, Adequacy, and Rival Models | State assumptions, anticipate failure, and acknowledge alternative formulations | Do not teach the full assumption record, dimensional and limiting checks, Fermi bounds, verification/validation, formal context of use, applicability, credibility, or rival-model criticism here |
| Ch. 6: Probability, Prediction, and Simulation | Recognize uncertainty and predictive questions | Do not introduce probability rules, Bayes, expectation, simulation methods, scoring, or calibration here |
| Ch. 7: Targets, Identification, and Causal Claims | Preview that some inquiries require a more precisely defined target of estimation; separate association, prediction, intervention, and counterfactual questions at intuitive depth | Do not formally define estimands, statistical identifiability, causal identification, causal graphs, or identification strategies here |
| Ch. 8: Estimation, Uncertainty, and Model Checking | Ask what finite evidence says and how uncertain the answer remains | Do not teach estimators, estimates, likelihood, intervals, regression, or formal model checking here |
| Ch. 9: Combining and Transporting Evidence | Qualify the relevant population and application context and ask whether evidence travels | Do not teach synthesis methods, dependence among sources, external-validity analysis, generalizability, or transportability formalism here |
| Ch. 10: Values, Objectives, and Alternatives | Identify stakeholders, consequences, and whether the available option set is artificially narrow | Do not formalize utility, objectives, trade-offs, metrics, or alternative-generation methods here |
| Ch. 11: Decisions Under Uncertainty and Value of Information | Separate beliefs about consequences from choice and ask whether more information could change the decision | Do not calculate expected utility or value of information here |
| Ch. 12: Optimization, Robustness, and Adaptive Plans | Recognize constraints, feasibility, model uncertainty, and brittleness | Do not formulate or solve optimization models here |
| Ch. 13: Dynamics, Feedback, and Stability | Screen for time, accumulation, delay, feedback, and policy resistance | Do not teach stocks and flows, stability, oscillation, or formal dynamics here |
| Ch. 14: Sequential Decisions, Information, and Control | Recognize that a policy may be more appropriate than a one-shot action and that actions can change future information | Do not teach control, observability, structural identifiability, exploration, filtering, or dynamic programming here |
| Ch. 15: Strategic Interaction, Incentives, and Endogenous Response | Ask whether agents will respond to the model, policy, evidence, or metric | Do not teach equilibrium, games, principal-agent models, Goodhart taxonomies, or mechanism design here |
| Ch. 16: Integration: The Full Loop on Unfamiliar Problems | Establish the baseline whole-loop attempt and initial routing habit | Chapter 1 is heavily scaffolded; Chapter 16 requires independent triage and repeated backward revision |
| Ch. 17: Deployment, Monitoring, and Revision | Ask what will be monitored, what would trigger revision, and where failure might have entered | Do not teach control-chart reasoning, drift diagnosis, monitoring design, or governance procedures here |

## Scope boundary

### Core

The chapter must teach the reader to do the following at an introductory but productive level.

- Convert a broad concern or topic into an explicit intended-use statement and a qualified target.
- Specify the target well enough that another competent analyst can tell what answer is sought: normally who or what the answer concerns and what quantity, event, state, outcome, relationship, comparison, or consequence is at issue.
- Add conditions, horizon, resolution or aggregation, comparison or reference condition, target population, required answer form, or threshold only when omission could materially change the meaning of the question.
- Keep the target distinct from the observed or recorded variable, proxy, decision, objective, and adequacy criterion.
- Screen the claim type only far enough to determine whether the target requires description, prediction, comparison under intervention, counterfactual comparison, or decision support; formal treatment remains later.
- Identify the person or institution using the answer, the judgment or action at stake, affected stakeholders, and consequences of major errors.
- State provisional adequacy criteria for the stated intended use without pretending they are already measured or optimized.
- Distinguish positive and normative components of a problem using ordinary language first, then stabilize the formal labels.
- Treat positive inquiry as broader than description and keep the positive/normative layer separate from the later claim-type layer.
- When a recommendation is made, identify the material evaluative or decision premise needed to move from consequence claims to action.
- Distinguish descriptive or associational, predictive, interventional, and counterfactual claims at intuitive depth.
- Recognize that explanatory aims and mechanism claims can accompany several claim types.
- Screen for dynamics, repeated decisions, feedback, adaptive behavior, strategic response, and the possibility that model deployment changes the target process.
- Distinguish the target system, model, measured or recorded data, evidence claim, value judgment, and action at a first-pass level.
- Generate at least two plausible formulations or interpretations when the prompt is materially ambiguous.
- Perform one informal pass through all five parts of the book using a single consequential case.
- Revise an earlier target, representation, assumption, evidence claim, value judgment, or action when later information warrants revision.
- Identify what is currently unknown, what evidence would be decision-relevant, what could make the analysis inadequate, and which later chapter or specialist method is needed next.
- Produce a concise first-pass analysis on an unfamiliar case without mechanically forcing every stage onto it.

### Deferred to later chapters

- Detailed system and model boundaries, endogenous/exogenous treatment, abstraction, idealization, aggregation, scale, entities, quantities, states, mechanisms, relations, units, and alternative representations: Chapter 2.
- Constructs, operationalization, proxies, validity, reliability, and formal measurement error: Chapter 3.
- Sampling, selection, missingness, censoring, aggregation, reporting, institutional production of records, and adversarial corruption: Chapter 4.
- Assumption records, dimensional and extreme-condition checks, Fermi estimation and bounding, verification, validation, structural uncertainty, rival models, and model criticism: Chapter 5.
- Probability, conditioning, Bayes, expectation, simulation, probabilistic prediction, and calibration: Chapter 6.
- Formal targets and estimands, statistical identifiability, causal identification, causal graphs, identification strategies, experiments, observational designs, intervention, and counterfactual formalism: Chapter 7.
- Estimators, estimates, likelihood, regression, uncertainty quantification, predictive evaluation, and statistical model checking: Chapter 8.
- Evidence synthesis, expert judgment, dependence, replication, target-population refinement, external validity, generalizability, and transportability: Chapter 9.
- Value structuring, objectives, measurable proxies, metrics, trade-offs, utility, constraints, and systematic alternative generation: Chapter 10.
- Formal decisions under uncertainty, expected utility, decision trees, sensitivity analysis, ambiguity, and value of information: Chapter 11.
- Optimization, computational tractability, robustness, regret, scenarios, and adaptive plans: Chapter 12.
- Stocks and flows, delay, feedback, equilibrium, stability, oscillation, and policy resistance: Chapter 13.
- Policies, sequential information, control, observability, structural identifiability, and exploration versus exploitation: Chapter 14.
- Strategic dependence, incentives, equilibrium, commitment, information asymmetry, principal-agent reasoning, metric gaming, and endogenous response: Chapter 15.
- Independent integration on unfamiliar cases and post-deployment monitoring and revision: Chapters 16 and 17.

### Deferred to depth curriculum

- Formal problem-structuring-method practice, including facilitated soft-systems, cognitive-mapping, and group decision-conferencing methods.
- Comprehensive requirements engineering, stakeholder analysis, and systems-engineering lifecycle standards.
- Formal logic and philosophical semantics of explanation, action, modality, and counterfactuals.
- Axiomatic decision theory and detailed normative foundations.
- Formal causal hierarchies, do-calculus, potential-outcome derivations, and specialist identification strategies.
- Full measurement theory, psychometrics, econometrics, optimization algorithms, control design, reinforcement learning, game theory, and mechanism design.
- Domain-specific safety cases, model-risk regulation, validation standards, and governance frameworks.

## Section architecture

The chapter uses one consequential anchor case, two short contrasts, and a final unfamiliar production task.
The expanded Reasoning Loop may appear as a reference figure, but the worked narrative should group it into the book's five parts so that the reader is not asked to memorize seventeen stages.

| Section | Working title | Pages | Learning hours | Primary output |
|---|---|---:|---:|---|
| 1 | A Good Answer to the Wrong Question | 2 | 0.25 | An initial prediction that exposes the reader's default framing |
| 2 | Intended Use and the Decision Situation | 4 | 0.50 | A precise intended-use statement for the anchor case |
| 3 | What Kind of Question Is This? | 4 | 0.55 | A layered classification of the problem's positive/normative, claim, time, and agent properties |
| 4 | A First Complete Pass: Preventing a Hospital Stockout | 8 | 1.00 | A worked pass through formulation, evidence, choice, responsive action, monitoring, and revision |
| 5 | When the First Formulation Fails | 3 | 0.30 | Rival formulations, contrasting backward revisions, and a justified handoff to later machinery |
| 6 | Cold-Start Practice and Retrieval | 3 | 1.40 | An independently produced first-pass analysis and self-diagnosis |
| **Total** |  | **24** | **4.00** |  |

### Section 1: A Good Answer to the Wrong Question

- Open with an underspecified but consequential prompt such as “reduce hospital stockouts.”
- Require the reader to predict what should be modeled, what data should be collected, and what action should be taken before receiving further guidance.
- Show that several technically competent analyses could answer different questions: predicting stockout, reconciling inventory, evaluating a replenishment policy, or deciding which items deserve intervention.
- Establish the chapter's governing failure: technically solving a question that was never the relevant question.
- Do not begin with a glossary or the full Reasoning Loop diagram.

### Section 2: Intended Use and the Decision Situation

- Develop the anchor case from topic to practical concern, analytical question, claim, and decision.
- Separate intended use (`what will the answer be used for?`) from target (`what exactly is the inquiry trying to determine, and about whom or what?`).
- Require a minimally qualified target, then add context, horizon, aggregation, comparator, or answer form only when those details change the substantive question.
- Specify decision-maker, affected stakeholders, possible actions, information available at decision time, consequences of false reassurance and false alarm, and provisional adequacy criteria.
- Use the same target under two different intended uses and two different targets under one intended use to demonstrate that intended use and target are related but not identical.
- Preserve `adequate for the stated intended use` as a separate judgment rather than treating it as part of target specification.
- Introduce `adequate for the stated intended use` as disciplined reader-facing language, not as a universal standardized adequacy framework.
- Make clear that overall adequacy depends on use even though some properties, including aspects of numerical verification, may be assessed independently.
- If `context of use (COU)` is mentioned, label it as field-specific, do not require memorization, and route formal treatment to Chapter 5.
- Do not imply that intended use can excuse incoherence, bias, or avoidable harm.
- End with a reusable short prompt, not a named proprietary framework or acronym.

### Section 3: What Kind of Question Is This?

- Present question classification as layered inquiry rather than a flat menu of mutually exclusive types.
- Begin with ordinary language: ask whether the component concerns what is or would happen, what should matter or be done, or both.
- Then introduce `positive` and `normative`, applying them to components or subquestions rather than entire problems.
- Make clear that positive is broader than descriptive and that normative is not a synonym for unsupported opinion.
- Then distinguish description or association, prediction, intervention, and counterfactual comparison.
- Then screen for time, feedback, repeated action, and adaptive or strategic response.
- Use minimally different questions about the same case to show why the required evidence and machinery change.
- Use claim-type screening only to expose target differences: a predicted outcome, an intervention comparison, and a counterfactual comparison may mention the same outcome variable while asking for different objects.
- Keep the layers orthogonal: a prediction, intervention-effect question, or counterfactual comparison may still be positive because it asks what would happen.
- Do not introduce formal estimand or identification terminology here.
- Include one example in which an accurate prediction does not establish the effect of acting on the predicted factor.
- Include one example in which evidence supports a consequence estimate but cannot by itself determine what should be valued.

### Section 4: A First Complete Pass: Preventing a Hospital Stockout

The pass should be informal, concrete, and organized under the five book parts.

1. **Frame and Formulate:** intended use; a target event, quantity, or other sought object distinguished from recorded inventory; the relevant item, location or system, horizon, and material conditions; provisional boundary; important assumptions; and a rival formulation. If the task is a replenishment decision, state that decision separately from the prediction or consequence targets that inform it.
2. **Learn from Evidence:** uncertainty, how records came to exist, what historical patterns can predict, what they cannot establish about an intervention, finite-evidence limits, and whether evidence applies to the relevant item and hospital context.
3. **Choose:** distinguish positive claims about consequences from the normative evaluation of those consequences; identify affected stakeholders, alternatives beyond “order or do nothing,” constraints, and whether additional information such as a physical count could change the decision.
4. **Act in Responsive Systems:** order pipeline, time delay, repeated decisions, feedback, supplier and staff response, and the possibility that a metric or alert changes recording or ordering behavior.
5. **Integrate and Revise:** deployment, monitoring, discrepancy detection, diagnosis by stage, and deliberate return to an earlier formulation choice.

The worked case must visibly loop backward at least twice so that readers encounter two materially different forms of revision.
The number is a worked-example design requirement, not a general rule for competent reasoning; outside the example, revision occurs whenever later information warrants it.
One backward move should be triggered by discovering that recorded stock and physical stock diverge because of unit conversion or delayed posting.
Another should be triggered by deployment changing staff, supplier, or ordering behavior.

Each stage should end with a forward pointer explaining which later chapter supplies the missing machinery.
The narrative must also show that some stages can be screened out as immaterial in simpler problems.

### Section 5: When the First Formulation Fails

- Contrast adjustment within an accepted formulation with revision of the question, target, representation, observation process, structural assumption, value model, or action.
- Treat a change in target quantity, event, population, comparison, horizon, or aggregation as a formulation revision rather than a parameter adjustment.
- Show at least two rival initial formulations of the anchor problem and what evidence or decision requirement would favor each.
- Use the pendulum as a short contrasting case: estimating gravitational acceleration, predicting angular position, and designing a clock do not merely require different methods; they seek different targets or decisions in the same physical system.
- Identify warning signs requiring a specialist rather than improvised use of advanced terminology.
- Make clear that `adequate for the stated intended use` is provisional and must be monitored after action.

### Section 6: Cold-Start Practice and Retrieval

- Diagnose a planted formulation that begins with a technique, treats a recorded variable or available label as the target, conflates prediction with intervention, and recommends an action without stating values or alternatives.
- Require the learner to repair an underspecified target by adding only the qualifiers that materially change the question rather than completing a fixed checklist.
- Give a faded case with prompts reduced relative to the worked example.
- Require an unfamiliar-domain first-pass analysis completed before consulting the rubric.
- Require a short self-explanation of the most consequential revision made after checking the answer.
- End with retrieval from memory: the reader reconstructs the five-part navigation map and its backward links without copying the diagram.
- Schedule a 7–14 day retest on a different domain; the retest result becomes baseline evidence for the Part I transfer gate.

### Drafting constraints

- Use the five-part map before exposing the expanded chapter-by-chapter loop.
- Do not present the layered triage as a named new framework, hierarchy, or acronym.
- Treat the same-question test for material target qualifiers as book-specific pedagogical synthesis, not as an established disciplinary rule.
- Keep formal notation minimal; a simple inventory balance may be used only when it clarifies the distinction between physical and recorded quantities.
- Do not define later specialist terms merely to mention them.
- Every preview must either support the anchor decision or be removed.
- At least half of the chapter's active-learning time must require prediction, production, self-explanation, error diagnosis, or retrieval rather than rereading.
- The prose must explicitly state where the worked case is simplified and where domain expertise would be required in practice.

## Examples / recurring cases

### Primary anchor: hospital pharmacy stockout decision

The central worked case is a synthetic but operationally realistic decision about whether and how to intervene when a pharmacy item may become physically unavailable within seven days.

The case is selected because it supports every book part without requiring advanced formalism.

- Purpose: prediction, replenishment decision, reconciliation, and policy evaluation can be contrasted.
- Representation: on-hand stock alone may omit the order pipeline, substitution, ward stock, or supplier behavior.
- Measurement and observation: physical stock differs from recorded stock; transactions, timestamps, counts, and product-specific units can distort the record.
- Evidence: historical data can support prediction while remaining insufficient for a causal claim about a new ordering policy.
- Value and choice: stockout harm, waste, cash, urgency, substitution, and staff burden create competing consequences and alternatives.
- Dynamics: demand, receipts, lead times, outstanding orders, and repeated reviews evolve through time.
- Strategic or adaptive response: staff and suppliers may change behavior after alerts, targets, or policies are deployed.
- Monitoring and revision: physical counts, discrepancy patterns, and decision outcomes can send the analysis back to measurement, representation, evidence, or objectives.

The case must use invented or appropriately anonymized data.
Any claims about clinical workflow, inventory practice, or product conversion require authoritative sourcing and domain review.

### Short contrast: simple pendulum

Use the same target system under three purposes: estimate local gravitational acceleration, predict short-horizon position, and design a durable clock.
The contrast demonstrates that purpose changes required representation and adequacy even in a non-strategic physical system.
It also prevents readers from interpreting the book as applicable only to managerial or institutional problems.

### Short contrast: student assessment

Contrast ranking applicants, diagnosing prerequisite skills, and selecting the next instructional activity.
Use the example only to preview target versus observed response, construct or proxy concerns, normative stakes, and adaptive behavior.
Formal measurement, psychometrics, causal claims, and metric gaming remain in later chapters.

### Unfamiliar transfer cases

Prepare at least two parallel cold-transfer forms from domains not used in the worked exposition.
One should involve a mainly physical or engineering system and one an institutional or policy system.
The reader should complete the form from the domain in which they have less prior familiarity.
Each prompt must supply enough domain facts that performance reflects reasoning rather than hidden specialist knowledge.

### Proposed recurrence opportunities

These are candidate later homes, not obligations imposed by the Chapter 1 specification.

- Candidate later homes for hospital inventory include Chapters 2, 4, 6, 11–14, and 17.
- Candidate later homes for student assessment include Chapters 3, 7, 9, 10, and 15.
- Candidate later homes for the pendulum or another physical system include Chapters 2, 5, 6, and 14.
- Recurring-case architecture must be adjudicated book-wide and later recorded in its canonical home under `cases/`.
- Any later appearance should add a genuinely new operation rather than repeat the Chapter 1 narrative with more terminology.

## Exercise architecture

The exercise sequence follows worked-example study, self-explanation, fading, error diagnosis, independent production, and delayed retrieval.

### 1. Opening prediction

Before reading the worked case, the reader responds to the underspecified prompt in five minutes.
The response is preserved and compared with the exit task rather than corrected immediately.

### 2. Dual-use contrast

Given one target system, the reader writes two intended-use statements that require materially different questions, targets, evidence, or actions.
The answer must explain why one unchanged analysis cannot adequately serve both uses.

### 3. Layered question classification

Classify six short questions by:

1. positive, normative, or mixed component;
2. descriptive or associational, predictive, interventional, or counterfactual claim;
3. one-shot or dynamic setting;
4. non-adaptive or adaptive/strategic environment.

Some questions must legitimately receive multiple labels.
The scoring key must reward justified overlap and penalize forced exclusivity.
It must also allow descriptive, predictive, interventional, or counterfactual items to be classified as positive when they ask what is or would happen rather than what should be valued or done.

### 4. Worked-case self-explanation

At three pauses in the hospital case, require the reader to predict:

- which later question will force a boundary or target revision;
- whether the next evidence bears on prediction, intervention, or both;
- which action-relevant uncertainty should be reduced first.

The explanation follows only after the reader commits.

### 5. Planted-failure diagnosis

Present a concise analysis containing at least six faults:

- topic substituted for intended use;
- recorded variable, metric, or available label treated as the target;
- a target qualifier omitted even though its omission materially changes the question;
- association treated as evidence of intervention effect;
- recommendation made without consequences, values, or alternatives;
- deployment assumed not to affect behavior;
- the Reasoning Loop treated as a mandatory waterfall.

The reader identifies, ranks, and revises the faults rather than merely labeling them.

### 6. Cold-transfer production task

Without a chapter checklist in view, the reader produces a one-page first-pass analysis for an unfamiliar case.
The submission must include:

- intended use and decision-maker;
- affected stakeholders and candidate actions;
- qualified target and context;
- layered question classification;
- preliminary distinction among target system, model, and observed records;
- the most important evidence limitation;
- relevant values, consequences, and constraints;
- time, feedback, or adaptive-agent screening;
- one rival formulation;
- one likely revision trigger;
- justified routing to later chapters or specialist expertise.

### Self-scoring rubric

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Intended use and decision | Missing or merely names a topic | Partly specified | User, action or judgment, and use are explicit |
| Target and context | Missing, unqualified, or conflated with a record or metric | Focal object and sought object are only partly specified | Who or what and what about it are explicit; material qualifiers are present without checklist padding |
| Question and claim type | Major conflation | Labels present but weakly justified | Positive/normative and claim-type layers are separated correctly, and justified overlap is allowed |
| Model, measurement, and records | Treated as identical | One distinction recognized | Target, representation, and recorded traces are separated |
| Evidence limits | Unsupported certainty | Generic uncertainty statement | Specific limit and its consequence for the claim are stated |
| Values and alternatives | Recommendation presented as factual necessity | Some consequences or options identified | Stakeholders, consequences, and a nontrivial option set are visible |
| Dynamics and response | Assumes a passive one-shot world | Time or response noted | Feedback, repeated choice, or adaptation is screened appropriately |
| Revision and routing | No failure condition or next step | Generic caveat | Rival formulation, diagnostic trigger, and justified later machinery are named |

The Chapter 1 exit task and its rubric are diagnostic rather than a major book transfer gate.
No validated numerical cut score is assumed at this stage.
Pilot responses will determine whether aggregate scores are interpretable and whether a numerical threshold adds value beyond dimension-level feedback.
The artifact is retained and repeated after Chapter 5 and in Chapter 16 to measure improvement in cold-start reasoning.

Regardless of any future numerical scoring convention, the following constitute major category errors:

- answering a different decision than the one stated;
- treating a metric or record as identical to the target without justification;
- treating association or predictive performance as sufficient evidence of intervention effect;
- deriving a recommendation from evidence while leaving material value judgments hidden;
- ignoring an explicitly stated adaptive or strategic response;
- applying every stage mechanically despite explaining why a stage is irrelevant.

## Transfer target

Given a previously unseen consequential problem and no named method, the reader should be able to produce within 30–40 minutes a defensible first-pass analysis that:

1. identifies who needs what answer and why;
2. states the relevant decision or judgment and a qualified target, adding context or horizon when material;
3. separates positive and normative components;
4. distinguishes the relevant associational, predictive, interventional, or counterfactual claims without forcing exclusivity;
5. asks how target events become observations and what the evidence could fail to establish;
6. identifies affected stakeholders, plausible alternatives, consequences, and constraints;
7. screens for time, feedback, repeated choice, adaptation, and strategic response;
8. states at least one rival formulation and one observable revision trigger;
9. identifies the next chapter-level machinery or specialist expertise required;
10. avoids pretending that the first pass is a completed analysis.

Transfer must be demonstrated on at least one domain outside the reader's training and outside the chapter's worked examples.
The standard is not specialist correctness.
The standard is an explicit, coherent, purpose-governed, revisable formulation with no unresolved major category error.

## Evidence / source plan

### Source discipline

Draft material and secondary source maps may be used as design and source-discovery aids, but they are not citable authorities.
Any terminology, example, or source lead drawn from them must be checked against the original literature before reuse.

No citation key should be created from memory.
Every load-bearing source must be verified, added to `../../references.bib`, and accompanied by a source note under the future `../../sources/` directory before the corresponding prose is treated as supported, in accordance with `../../decisions/0003-citation-and-source-note-system.md`.

### Conceptual source clusters to verify

| Topic or claim family | Candidate primary or canonical sources to inspect | Intended use in Chapter 1 |
|---|---|---|
| Purpose and intended use in mathematical and scientific modeling | Epstein, “Why Model?”; Giordano, Fox, and Horton, *A First Course in Mathematical Modeling*; Box, “Science and Statistics” | Support formulation before technique, selective representation, purpose, criticism, and revision |
| Intended use, conceptual modeling, and adequacy for use | Robinson's work on conceptual modelling for simulation; Sargent on verification and validation of simulation models; Oberkampf and Roy on verification and validation in scientific computing | Stabilize intended use, conceptual model, adequacy, verification/validation boundaries, and the claim that fit alone is insufficient |
| Decision framing and decision analysis | Howard, “Decision Analysis: Practice and Promise”; Keeney, *Value-Focused Thinking*; an appropriate canonical decision-analysis text selected after review | Support decision context, consequences, alternatives, objectives, and separation of evidence from choice while deferring formal decision theory |
| Prediction, explanation, and causal questions | Shmueli, “To Explain or to Predict?”; Hernán and Robins, *Causal Inference: What If*; Pearl, *Causality* or a primary exposition of the association/intervention/counterfactual distinction | Ground the claim distinctions while preventing Chapter 1 from teaching formal causal machinery |
| System boundaries, endogenous explanation, feedback, and adaptive response | Sterman, *Business Dynamics*; appropriate systems-analysis and control sources; Lucas's policy-evaluation critique for later cross-reference | Support screening for boundaries, feedback, deployment effects, and adaptive environments without importing later formalism |
| Model use changing behavior or measurement | Canonical sources later used for Campbell's law, Goodhart-type effects, performativity, and principal-agent reasoning | Support one brief warning and route the reader to Chapter 15; detailed taxonomy remains deferred |
| Learning design | Primary research on worked examples and fading, self-explanation, retrieval practice, contrasting cases, analogical comparison, error diagnosis, and transfer | Justify exercise ordering and delayed retest; these sources may live in a book-level pedagogy dossier rather than appear in reader-facing prose |

### Case-source requirements

- Hospital inventory claims must be checked against authoritative hospital-pharmacy, inventory-control, accounting, and unit-of-measure sources, supplemented by domain-expert review.
- Any statement about medication handling, clinical criticality, or patient consequences requires appropriate clinical or regulatory review.
- Pendulum equations and approximations should be checked against a standard mechanics source, even when treated as elementary.
- Student-assessment examples must be checked against measurement and psychometric sources and must not imply that statistical fit establishes construct validity.
- All numerical case data should be synthetic unless permission, provenance, and privacy conditions are explicit.

### Evidence needed before prose is considered stable

- Verified definitions or usage notes for `intended use`, `target`, `adequacy`, `positive`, `normative`, `association`, `prediction`, `intervention`, and `counterfactual`.
- At least one primary or canonical source supporting each load-bearing distinction.
- A domain review of the hospital case for realism and hidden assumptions.
- A terminology review ensuring Chapter 1 does not preempt the formal meanings assigned in Chapters 6, 7, 10, 11, 14, and 15.
- A learner pilot testing whether the five-part map reduces rather than increases initial cognitive load.

## Failure modes this chapter should prevent

| Failure mode | Architectural prevention in Chapter 1 | Later reinforcement |
|---|---|---|
| Treating a topic as a well-formed problem | Topic-to-decision contrast and intended-use production | Chapters 2 and 10 |
| Solving the wrong problem competently | Opening prediction, rival uses, and explicit decision context | Chapters 5 and 16 |
| Choosing a method before defining the target and use | Technique-free first pass and routing requirement | All later chapters |
| Treating the model as the target system | Pendulum and inventory contrasts | Chapters 2 and 5 |
| Treating observed records as neutral facts | Physical versus recorded inventory | Chapters 3 and 4 |
| Confusing target, proxy, metric, objective, and estimand | Qualified informal use of target plus explicit deferral | Chapters 3, 7, and 10 |
| Treating positive evidence as sufficient for a normative recommendation | Require an explicit bridge from consequence claims to material evaluative premises, stakeholders, values, and action | Chapters 10 and 11 |
| Confusing association or prediction with intervention | Layered question exercise and planted failure | Chapters 6 and 7 |
| Assuming an effect or pattern automatically applies in the relevant application context | Require the qualifiers that materially affect application, such as population, system, context, or horizon | Chapter 9 |
| Accepting the supplied option set | Require at least one additional plausible alternative | Chapter 10 |
| Collecting information without asking whether it could change action | Qualitative decision-relevance-of-information prompt | Chapter 11 |
| Treating feasibility or optimization as objective formation | Values and alternatives appear before any optimization preview | Chapters 10–12 |
| Treating uncertainty as one undifferentiated lack of confidence | Ask where uncertainty enters and what conclusion it affects | Chapters 5, 6, 8, and 12 |
| Ignoring time, accumulation, delay, and repeated decisions | Environment screening and dynamic anchor case | Chapters 13 and 14 |
| Ignoring adaptation, incentives, and metric response | Adaptive-agent screen and deployment-induced revision | Chapter 15 |
| Treating the teaching order as a real-world waterfall | Worked demonstration of two distinct backward revisions, while reader revision remains evidence-triggered | Chapters 16 and 17 |
| Mechanically applying every stage to every problem | Require relevance justification and allow explicit “not material here” findings | Chapter 16 |
| Becoming overconfident from possession of terminology | Preview without formal mastery, specialist-handoff prompts, and preserved baseline errors | Throughout the book |

Chapter 1 can only provide initial protection against these failures.
Later chapters must revisit them with stronger concepts, formal tools, and unfamiliar transfer tasks.

## Open questions

The following questions must be resolved during chapter design or pilot testing, but none currently requires changing the chapter title, order, page budget, or core competence.

1. **Anchor-case accessibility:** Is the hospital stockout case understandable without domain knowledge while remaining realistic enough to carry the full loop?
   Default: retain it, supply all necessary facts, use synthetic data, and obtain domain review.
2. **Loop presentation:** Can readers retain the whole-loop idea without being overwhelmed by the expanded sequence?
   Default: teach the five book parts first, show the expanded loop as a reference, and assess reconstruction of relationships rather than memorization of labels.
3. **Target-specification burden:** Do readers learn to add only qualifiers that materially change the question, rather than turning target specification into a fixed checklist?
   Default: teach the two-part minimum plus a same-question test, then pilot whether learners omit material qualifiers or add irrelevant ones.
4. **Positive/normative transfer:** Can readers keep positive inquiry broader than description and avoid collapsing the distinction into fact/opinion or objective/subjective shortcuts?
   Default: begin with ordinary language, then introduce the established terms and test the distinction with prediction, intervention-effect, and recommendation contrasts.
5. **Question-triage load:** Are four claim distinctions too many before probability and causal inference?
   Default: use minimally different concrete questions, require only intuitive discrimination, and defer formal criteria.
6. **Chapter 1 versus Chapter 2 boundary:** How much representation detail is necessary for a meaningful complete pass?
   Default: include one provisional boundary and one target/model/data distinction, but no quantity-role or relation taxonomy.
7. **Chapter 1 versus Chapter 10 boundary:** How much value and alternative work is necessary before formal value structuring?
   Default: name stakeholders, consequences, and at least one missing alternative, but do not introduce utility, objective functions, or formal trade-off methods.
8. **Cold-transfer form:** Which two unfamiliar cases minimize domain-knowledge confounding while remaining consequential?
   Default: pilot one physical or engineering case and one institutional or policy case, then retain parallel forms with comparable scoring difficulty.
9. **Diagnostic interpretation:** Do the rubric dimensions support reliable feedback, and would any aggregate threshold add value?
   Default: use dimension-level feedback and substantive major errors without a cut score until pilot evidence justifies another interpretation.
10. **Time feasibility:** Can a serious self-study reader complete the chapter, embedded predictions, and exit production task within four hours?
    Default: pilot the complete chapter with timed readers; remove exposition before weakening the production task.

### Before drafting

- No unresolved conflict with `README.md`, the decision records, or `canon/`.
- Terminology requiring canon control or source verification has been identified and assigned a clear research action.
- The section, page, and hour budgets still total 24 pages and 4 hours.
- The anchor case, contrasts, scope boundaries, and required backward-revision demonstrations are specified clearly enough to draft.
- The source plan identifies the literature and domain evidence needed for every load-bearing section.
- The exercise progression, transfer task, rubric dimensions, and major category errors are specified without claiming validated measurement.

### Before declaring Chapter 1 verified or frozen

- Load-bearing terminology and sources have been verified and recorded through the repository's bibliography and source-note process.
- The hospital case has passed domain, realism, and privacy review.
- The layered question exercise has an adjudicated answer key allowing justified overlap.
- Two parallel cold-transfer prompts and the self-scoring rubric have been tested with representative readers.
- Timed pilots show whether the full chapter can be completed within four serious learning hours.
- Pilot observation has tested whether the five-part map reduces cognitive load and whether readers avoid treating the Reasoning Loop as a waterfall.
- Evidence has determined whether any aggregate rubric score or cut score is useful; no threshold is required if dimension-level diagnosis is superior.
- Material pilot failures have been corrected before freeze, while ordinary prose improvements remain chapter-level revisions rather than reasons to reopen the book architecture.
