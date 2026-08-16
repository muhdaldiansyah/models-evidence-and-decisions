# Chapter 1 Decision-Framing Control

Status: governed by `../../decisions/0006-chapter1-decision-framing-boundary.md`

This file records the Chapter 1 implementation of the decision-framing boundary. It is an authoring-control artifact, not a new reader-facing framework or checklist.

## Core principle

Evidence and models can improve beliefs about what is likely to happen under different alternatives. They do not, by themselves, determine which consequences should matter most or which alternative should be chosen.

A recommendation therefore depends on both:

- consequence claims; and
- evaluative or decision premises.

A recommendation may advise a decision, but it is not the decision itself.

## Minimum Chapter 1 prompts

Use ordinary language. Do not present these prompts as a named framework or acronym.

1. **What decision is actually being made?**
   State the immediate judgment, authorization, or action rather than merely naming the topic or desired outcome.

2. **Who can make or authorize it?**
   Identify the person, group, or institution with responsibility or authority for the immediate choice. If authority is distributed, state the relevant dependency.

3. **What alternatives are genuinely available?**
   Identify salient courses of action and ask whether the initial option set is artificially narrow.

4. **What material consequences differ among alternatives?**
   Identify consequences for relevant stakeholders or the target system. One analytical target need not exhaust the decision-relevant consequences.

5. **What makes those consequences better, worse, acceptable, or unacceptable?**
   Expose the material value, requirement, obligation, or constraint without formalizing value functions or utility.

6. **What evidence bears on those consequences?**
   Identify the evidence or uncertainty most likely to change beliefs about the relative consequences.

7. **What could force the decision frame to be revised?**
   Examples include misunderstood authority, omitted stakeholders, a newly feasible alternative, an invalid measurement, changed behavior after action, or a materially different horizon.

## Alternative-set discipline

The first alternatives stated in a prompt are not assumed complete.

When the option set is materially narrow, require at least one plausible additional candidate, such as:

- a combined action;
- a contingent action;
- an information-gathering action;
- a staged action or delay when feasible;
- a request, negotiation, or escalation when another actor controls the desired action.

This is an introductory anti-framing-error requirement. Systematic alternative-generation methods remain Chapter 10.

## Authority discipline

An attractive action is not automatically an alternative available to the named decision-maker.

If another actor controls the action, represent the relevant move as a request, authorization step, negotiation, escalation, or another actor's decision. Do not silently assume authority.

All worked and transfer cases must supply any authority facts needed for reasoning.

## Consequence discipline

Keep distinct:

- the analytical target;
- the consequences of alternatives; and
- the evaluation of those consequences.

For example, a seven-day minimum water-storage target can inform the water-supply decision, but the decision may also involve energy cost, burden on households and businesses, service continuity, reserve margin, implementation burden, and future flexibility.

## Water-supply anchor application

The anchor must specify which utility or municipal actor owns the immediate operational decision and which actions require separate authorization.

Candidate actions may include, depending on the supplied case facts:

- maintaining current operation;
- verifying physical storage before changing operation;
- changing pumping within stated limits;
- issuing a voluntary conservation request;
- combining verification, pumping changes, and conservation;
- adopting a contingent response triggered by a specified observation;
- requesting authorization for a stronger restriction when required.

The case need not use every alternative. Its purpose is to prevent a false binary such as `pump more` versus `do nothing`.

Evidence may inform current physical storage, demand, source inflow, pumping availability, leakage, likely response to conservation, and the consequences of each action.

The recommendation must also expose the material evaluative premise needed to judge shortage risk, operating cost, burden, equity, service continuity, or other supplied consequences.

The two governed backward revisions remain:

1. verified physical storage disagrees with the dashboard because of telemetry delay or sensor miscalibration;
2. a conservation action changes water-use behavior enough that a forecast assuming unchanged demand is no longer adequate.

If useful in drafting, a third framing example may show that mandatory-restriction authority belongs to another actor. This is a decision-frame revision, not a parameter update.

## Refrigerated-warehouse transfer application

The prompt must supply who controls equipment operation, inspection, backup cooling, relocation of high-risk inventory, and any shutdown decision.

A temperature forecast or risk estimate informs the decision but does not choose the response.

The form should preserve alternatives that can expose false binary framing, including inspection or combined actions when supported by the supplied facts.

## Emergency-housing transfer application

The prompt must state which body has allocation authority and must supply any eligibility or mandatory administrative rules needed for reasoning.

A model that predicts who is likely to remain unhoused does not itself determine how limited vouchers should be allocated.

The form should expose the distinction among observed applicant records, target population, predicted outcomes, allocation alternatives, consequences across groups, and evaluative or institutional premises.

## Chapter boundaries

### Chapter 1

Own practical recognition of decision-maker, authority, alternatives, consequences, stakeholders, evaluative premises, material constraints, evidence relevance, and revision triggers.

### Chapter 10

Own formal value structuring, objectives, measurable attributes or metrics, systematic alternative generation, and trade-off structure.

### Chapter 11

Own formal choice under uncertainty, expected utility, risk attitude, decision trees, formal sensitivity analysis, and value of information.

### Chapters 12 and 15

Chapter 12 owns formal optimization constraints and robustness. Chapter 15 owns strategic response and incentives.

## Spec synchronization note

The current `spec.md` is substantively consistent with this control in most places: it already distinguishes evidence about consequences from evaluative premises, requires attention to missing alternatives, and defers formal value/decision machinery.

Before Chapter 1 is declared stable for drafting, synchronize any wording that could imply that a recommendation and decision are identical. In particular, a recommendation should be described as advice or a decision-support conclusion, not as the decision itself.

No title, central question, section count, page budget, learning-hour budget, anchor, contrast, transfer form, or rubric policy changes are authorized by this file.
