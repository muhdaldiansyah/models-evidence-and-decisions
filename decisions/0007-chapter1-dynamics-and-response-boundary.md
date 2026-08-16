# Decision 0007: Chapter 1 Dynamics and Response Boundary

## Status

Accepted (2026-08-16)

## Decision

Chapter 1 teaches a dynamic-and-responsive-environment screen at introductory depth. It does not teach formal system dynamics, feedback control, sequential control, or game theory.

The reader should be able to ask, when material:

- what changes through time;
- what carries over from one period to the next;
- what increases or decreases that carried-over quantity or state;
- what important action, physical effect, behavioral response, or observation is delayed;
- whether an action changes something that later changes outcomes, information, or future actions;
- whether the decision will be revisited as state or information changes;
- whether people or organizations will respond to a rule, model, metric, prediction, or intervention;
- whether that response can change the process that generated the evidence or forecast.

These are screening prompts, not a named framework or exhaustive taxonomy.

## System boundary

The first system boundary is purpose-governed and provisional.

Chapter 1 should include only what is material for the stated intended use, target, evidence interpretation, consequences, and decision. It must not teach that a good boundary simply includes everything.

The boundary should be revised when an omitted process, actor, delay, accumulation, observation mechanism, or response materially changes the answer.

Detailed representation, endogenous/exogenous treatment, mechanism, scale, and boundary analysis remain Chapter 2.

## Accumulation

Chapter 1 requires the learner to notice when a quantity or state carries over through time.

Use ordinary prompts such as:

> What carries over? What adds to it? What removes from it?

`stock` and `flow` are not required Chapter 1 vocabulary. Formal stock-flow representation and accumulation analysis remain Chapter 13.

A dynamic variable should not be mechanically labeled a stock; the refrigerated-warehouse temperature case is an explicit guard against that overgeneralization.

## Delay

Delay is a first-class screening issue in Chapter 1.

At intuitive depth distinguish only when useful:

- physical/action delay: an intervention or physical process takes time to affect the system;
- information/observation delay: the underlying state changes before the decision-maker observes or records it.

Formal delay models, time constants, lag operators, transfer functions, and delay differential equations remain later material.

The water-supply anchor should contain at least one material information delay and one material action/physical delay.

## Feedback

`feedback` is controlled introductory vocabulary.

At Chapter 1 depth, feedback means that consequences of a process or action return through the system and influence later behavior, outcomes, information, or actions.

Chapter 1 must not teach:

- positive versus negative feedback;
- reinforcing versus balancing loops;
- loop polarity or dominance;
- feedback-controller design;
- feedback stability.

These belong to Chapters 13–14.

Systems feedback must remain distinct from ordinary evaluative or reviewer feedback.

## Repeated and sequential decisions

Chapter 1 should ask whether a decision is one-shot or will be revisited after state or information changes.

When repeated choice matters, ask qualitatively:

- does today's action change tomorrow's state;
- does today's action change what information will be available;
- does today's action preserve or remove future options;
- what should be monitored before the next decision.

Formal policies, dynamic programming, filtering, exploration/exploitation, control, and observability remain Chapter 14.

## Adaptive and strategic response

Do not collapse adaptive and strategic response.

At Chapter 1 depth:

- an adaptive response is a change in behavior or operating practice after conditions, information, experience, or intervention change;
- a strategic response is a behavior change made partly because a rule, incentive, metric, prediction, policy, or anticipated response of others makes some action more advantageous to the agent.

Not every adaptive response is strategic, and the presence of human actors does not by itself make a system strategic.

Formal payoff functions, best response, games, equilibrium, principal-agent analysis, metric gaming, and mechanism design remain Chapter 15.

## Deployment-induced change

Chapter 1 must include the warning that a model, prediction, metric, rule, or policy can become part of the system after deployment.

If people or organizations respond to it, the future process producing observations may differ from the historical process used to construct or evaluate the analysis.

`performative prediction` is not required Chapter 1 vocabulary, and not every distribution shift should be described as performative.

## Anchor and contrasts

### Water-supply anchor

The anchor should expose:

- accumulation of usable stored water through additions and removals;
- an information delay such as telemetry or verification lag;
- an action/physical delay such as the time required for an operational change to alter storage;
- repeated review during the heatwave;
- conservation action changing demand and therefore the process generating future observations.

The existing backward revision in which conservation changes demand is a structural/process revision, not merely a parameter update.

### Pendulum

The pendulum remains the clean counterexample showing that a system may be dynamic without containing adaptive or strategic agents.

### Refrigerated warehouse

The warehouse transfer form should test dynamic physical reasoning, sensing delay, action delay, and operational feedback without forcing a strategic interpretation.

### Emergency housing

The housing transfer form may test adaptive and, only when the prompt supplies relevant incentives or rule dependence, strategic response.

## Chapter boundaries

Chapter 2 owns formal system boundary and representation work.

Chapter 13 owns stocks and flows, formal delays, feedback loops, equilibrium, stability, oscillation, and policy resistance.

Chapter 14 owns sequential decisions, policies, information/control, observability, structural identifiability, filtering, and exploration/exploitation.

Chapter 15 owns strategic dependence, incentives, equilibrium, principal-agent reasoning, gaming, and endogenous behavioral response.

Chapter 1 only screens for whether these later forms of analysis are needed.

## Sources

The bounded Research 06 evidence layer promotes:

- `sterman2006evidence` for narrow boundaries, delayed/distal consequences, and learning from intervention in complex systems;
- `astrom2008feedback` for the systems/control meaning of feedback and the boundary to formal control and stability analysis;
- `perdomo2020performative` for the warning that predictions used in decisions can influence outcomes and future data-generating environments.

Booth Sweeney and Sterman (2000) remains an optional pedagogical source and is not promoted unless Chapter 1 makes an explicit empirical claim about learner difficulty with stock-flow or delay reasoning.

## No architecture change

This decision does not change the Chapter 1 title, central question, six-section architecture, 24-page / 4-hour budget, water-supply anchor, pendulum or student-assessment contrasts, cold-transfer forms, rubric policy, or macro book architecture.
