# Chapter 1 Dynamics and Response Control

Status: governed by `../../decisions/0007-chapter1-dynamics-and-response-boundary.md`

This is an authoring-control artifact for Chapter 1. It records the maximum permitted introductory treatment of dynamics, feedback, repeated decisions, and responsive environments. It is not a new reader-facing framework or checklist.

## Core screen

Use ordinary language to ask:

> What changes through time? What carries over? What is delayed? What feeds back? Will we decide again? Who or what may respond to our action, rule, model, metric, or prediction—and could that response change the process we thought we were analyzing?

The questions may overlap. Do not force every case into every category.

## Boundary discipline

The first boundary is provisional and tied to intended use, target, evidence interpretation, consequences, and decision.

Do not teach `include everything` as a systems principle.

A boundary should be revised when an omitted process, actor, delay, accumulation, measurement mechanism, or behavioral response becomes material.

Detailed boundary, mechanism, representation, endogenous/exogenous, and scale work remains Chapter 2.

## Accumulation discipline

Chapter 1 should expose accumulation using ordinary prompts:

- What carries over from one time to the next?
- What adds to it?
- What removes from it?
- Can the current level be high while it is declining rapidly?
- Can the current level be low while it is recovering?

Do not require the terms `stock` and `flow`.

Do not label every dynamic variable a stock. In particular, the refrigerated-warehouse example should prevent readers from treating temperature as if it were simply a stored inventory variable.

Formal stock-flow diagrams, balance equations as a general method, and system-dynamics notation remain Chapter 13.

## Delay discipline

When delay matters, distinguish only in ordinary language:

### Action or physical delay

An action or physical process takes time to alter the relevant state or consequence.

### Information or observation delay

The underlying state changes before a measurement, report, or record becomes available to the decision-maker.

Chapter 1 should not teach formal delay categories or mathematics.

## Feedback discipline

Use the controlled systems meaning of `feedback`:

> consequences of a process or action return through the system and influence later behavior, outcomes, information, or actions.

Keep systems feedback distinct from ordinary comments or reviewer feedback.

Do not introduce:

- positive or negative feedback;
- reinforcing or balancing loop terminology;
- loop polarity or dominance;
- feedback stability;
- controller design.

The Chapter 1 positive/normative distinction is unrelated to technical positive/negative-feedback vocabulary, which is deliberately deferred.

## Repeated-decision discipline

Ask whether the decision is one-shot or will be revisited after state or information changes.

If revisited, ask:

- Does today's action change tomorrow's state?
- Does today's action change tomorrow's information?
- Does today's action preserve or remove future options?
- What should be monitored before the next choice?

Do not introduce policy functions, dynamic programming, filtering, control theory, observability, or exploration/exploitation.

## Adaptive and strategic response discipline

At Chapter 1 depth, use ordinary-language distinctions rather than formal agent models.

### Adaptive response

Behavior or operating practice changes after conditions, information, experience, or intervention change.

### Strategic response

Behavior changes partly because a rule, incentive, metric, prediction, policy, or anticipated response of others makes one response more advantageous to the agent.

Do not assume strategy merely because a human or organization is present.

If the strategic/adaptive distinction is not material or not supported by the case facts, simply record that behavior may respond.

Formal strategic interaction belongs to Chapter 15.

## Deployment warning

Chapter 1 should state explicitly:

> A model, prediction, metric, rule, or policy can become part of the system after deployment. If people or organizations respond to it, the process producing future observations may differ from the historical process used to build or evaluate the analysis.

The phenomenon matters more than the label. `Performative prediction` is not required Chapter 1 vocabulary.

Do not call every distribution shift performative.

## Water-supply anchor

The anchor should demonstrate the whole screen without formal systems notation.

### Accumulation

Usable stored water carries over through time and changes through supplied additions and removals.

Reader prompt:

> What makes usable stored water rise or fall over the seven-day horizon?

### Information delay

Use telemetry or verification lag as the principal observation-delay example.

The existing measurement revision remains:

> verified physical storage disagrees with the dashboard because of telemetry delay or sensor miscalibration.

### Action/physical delay

Include at least one case fact in which an operational action does not alter storage or demand immediately.

Possible examples include pumping/treatment lag or delayed behavioral response after conservation messaging. The case should choose one rather than accumulating domain detail.

### Feedback and deployment

A suitable sequence is:

1. storage changes;
2. operators observe or estimate storage;
3. operators change operation or issue a conservation request;
4. the action changes future storage or demand;
5. new observations influence the next decision.

No loop diagram is required.

### Repeated decision

The case should use a simple supplied review cadence, such as reassessment during the seven-day heatwave, rather than implying a single irreversible decision for the entire horizon.

### Structural revision

The governed revision in which conservation changes demand is not merely a parameter update.

Once the conservation action changes water-use behavior, the process generating future demand differs from the process assumed by the pre-action forecast. The target, model, assumptions, or monitoring plan may need revision.

## Pendulum contrast

The pendulum is dynamic but normally non-adaptive and non-strategic.

Use it to block the false inference:

`dynamic = feedback control = adaptive = strategic`.

If an engineered controller is added, route the formal control question to Chapter 14 rather than expanding Chapter 1.

## Student-assessment contrast

Use the student-assessment contrast to show that deployment/use can change behavior.

A score used only descriptively need not induce the same response as a score used for admission, placement, reward, or another consequential decision.

The Chapter 1 question is only:

> Will use of the score change behavior that produces future scores or outcomes?

Formal measurement belongs Chapter 3; causal effects Chapter 7; incentives and gaming Chapter 15.

## Refrigerated-warehouse transfer

The warehouse form should test:

- a changing physical state;
- measurement versus physical state;
- an observation delay;
- an action/thermal response delay;
- operational feedback and repeated monitoring.

Unless the prompt explicitly supplies incentive conflicts, do not require a strategic-agent interpretation.

## Emergency-housing transfer

The housing form may test:

- changing capacity, applications, verified eligibility, or unmet need through time;
- verification or provider-response delays;
- adaptive changes in applicant or provider behavior;
- strategic response only when the prompt supplies a manipulable rule, incentive, or allocation mechanism that makes such reasoning warranted.

The prompt must supply the institutional facts; learners should not need external housing-law knowledge.

## Chapter boundaries

### Chapter 2

Own formal system boundaries, representation, mechanism, state, scale, and endogenous/exogenous choices.

### Chapter 13

Own stocks and flows, formal accumulation, delay models, feedback loops, equilibrium, stability, oscillation, and policy resistance.

### Chapter 14

Own sequential decisions, policies, information/control, observability, structural identifiability, filtering, and exploration/exploitation.

### Chapter 15

Own strategic interaction, incentives, equilibrium, principal-agent reasoning, metric gaming, and endogenous response.

## Terminology boundary

Research 06 adds only `feedback` to the canonical terminology registry.

Do not add merely for Chapter 1:

- stock;
- flow;
- delay;
- adaptive response;
- strategic response;
- responsive environment;
- performative prediction.

These may appear in ordinary or field-specific prose when accurate, but they are not required controlled vocabulary at this stage.

## Source boundary

Load-bearing evidence promoted for this control:

- `sterman2006evidence`;
- `astrom2008feedback`;
- `perdomo2020performative`.

Do not expand the bibliography with every contextual Research 06 source unless a manuscript claim later requires it.

## Spec synchronization note

The current Chapter 1 spec already screens for time, accumulation, delay, feedback, repeated choice, and adaptive/strategic response. Decision 0007 and this control clarify the permitted depth and override any interpretation that would require formal stocks/flows, positive/negative feedback, stability, control, or game-theoretic machinery in Chapter 1.

Before Chapter 1 is declared stable for drafting, synchronize any spec wording that suggests these concepts receive formal treatment rather than introductory screening.

No chapter title, central question, section count, page budget, learning-hour budget, anchor, contrast, transfer form, or rubric policy changes are authorized by this file.
