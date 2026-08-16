---
chapter: 1
part: 1
title: "Decisions, Questions, and a First Complete Pass"
status: draft
---

# Chapter 1: Decisions, Questions, and a First Complete Pass

<!-- Drafting order follows drafting-blueprint.md. Sections 2 and 4 are drafted; Sections 1, 3, 5, and 6 will be written around the worked-example spine, then this comment will be removed during integration. -->

## 2. Intended Use and the Decision Situation

A problem becomes easier to analyze once we stop treating its topic as its question.

“Water shortage” is a topic. “Will demand exceed supply?” is an analytical question. “Should the utility change operations this morning?” is a decision. Those objects are related, but they are not interchangeable.

The first discipline is therefore simple:

> **State what the answer will be used for before deciding what answer to produce.**

In the water case, the immediate intended use is to support the Utility Director’s operating decision during a seven-day heatwave. That is more informative than saying that the purpose is to “understand demand” or “analyze storage.” It tells us who needs the answer, when it will be used, and what kind of consequence an inadequate answer could have.

Model-credibility and verification/validation frameworks use intended use or closely related use statements because adequacy cannot be separated from the application a model is meant to support [@nasa2024models; @nrc2012reliability]. Chapter 1 extends that discipline beyond formal models: an estimate, forecast, comparison, or recommendation should also be judged against what someone intends to do with it.

### Intended use is not the target

Once the use is clear, ask a second question:

> **What exactly are we trying to determine, and about whom or what?**

This book uses **target** as an informal organizing word for that answer.

For the same utility, several targets are possible:

- the current physical quantity of usable stored water;
- whether usable storage will fall below 4.5 ML within seven days;
- customer demand over the next seven days if no new conservation action is introduced;
- the consequence of increasing treated-water production;
- the consequence of issuing a voluntary conservation request.

These targets can support the same decision, but they are not the same target.

Conversely, the same target can serve different intended uses. An estimate of current physical storage could be used to decide whether to change operations now, to investigate a sensor discrepancy, or to prepare a monthly operating report. The target may be similar while the required timeliness, accuracy, evidence, and consequences of error differ.

A useful test is:

> Would two competent analysts, given this target statement, know that they are trying to answer the same substantive question?

If not, the target needs another material qualifier. Perhaps the population, system, horizon, comparison, aggregation, or required answer form is missing. But qualification should solve ambiguity, not become a ritual. “Usable storage in the utility’s main finished-water facility at 08:00 Monday” is useful if the immediate state matters. Adding ten irrelevant descriptors does not make the target more scientific.

### The record is not automatically the thing we care about

The dashboard displays **10.8 ML**. It is tempting to write:

> Current storage = 10.8 ML.

That sentence silently turns a record into the target.

A more careful first pass distinguishes at least three things:

- the **target**: current physical usable storage;
- the **record**: 10.8 ML displayed on the dashboard;
- the **observation process**: a remote level transmitter and telemetry system that produced the record.

At this point we have no reason to declare the dashboard wrong. We also have no reason to erase the distinction. A measurement or administrative record can be excellent evidence about a target without being identical to the target itself.

That separation will become much more important in Chapters 3 and 4. For now, it prevents a common framing error: answering a question about what was recorded when the decision depends on what is physically or substantively true.

### Name the decision—and who can make it

Now make the decision situation explicit.

The **decision-maker** is the person, group, or institution with authority or responsibility for the immediate decision. Here it is the Utility Director.

The case supplies a fictional authority structure. The director may:

- order an independent level verification;
- increase treated-water production up to 8.8 ML/day;
- issue a voluntary conservation request;
- increase monitoring and review frequency.

The director may **not** directly impose a mandatory water-use restriction. That requires City Manager approval.

This matters because an action is not a genuine alternative for a decision-maker merely because an analyst can imagine it. If another actor controls the action, the relevant alternative may be to **request**, **negotiate**, **escalate**, or **seek authorization**.

It also keeps three objects separate:

| Object | What it does |
|---|---|
| Analysis | Describes, predicts, estimates, or otherwise characterizes relevant facts and consequences |
| Recommendation | Advises what should be chosen given stated or assumed evaluative premises |
| Decision | Selects, authorizes, or commits to an action by the relevant decision-maker |

Evidence can change an analysis. An analyst can issue a recommendation. Neither event is automatically the decision itself. Practical decision processes similarly distinguish facts, values, alternatives, predicted consequences, uncertainty, and the actual choice [@nasem2026decisionmaking].

### Do not accept the first option set as complete

Suppose the problem is initially phrased as:

> Should we pump more or do nothing?

That is already a decision question, but the alternatives are suspiciously narrow.

The Utility Director could also verify the current state before acting, issue a voluntary conservation request, combine production and conservation, increase monitoring, stage actions over time, or prepare an escalation request if a later trigger is crossed.

An **alternative** is a candidate course of action that can actually be chosen, authorized, requested, negotiated, or otherwise pursued. Good decision framing does not assume that the first alternatives supplied by the problem statement exhaust the possibilities. Value-focused decision analysis makes active creation of alternatives an explicit part of better decision making [@keeney1996valuefocused].

Chapter 1 does not require a formal alternative-generation method. It asks for something simpler:

> If the supplied option set is materially narrow, can you name at least one plausible missing, combined, contingent, information-gathering, staged, or escalation alternative?

That one question is often enough to prevent a false binary from controlling the rest of the analysis.

### Consequences are not values

Alternatives matter because they can produce different **consequences**.

In the water case, relevant consequences may include:

- crossing or avoiding the case-specific operating reserve;
- maintaining service margin;
- additional operating cost;
- burden on households and businesses;
- burden from voluntary or mandatory restrictions;
- the time required for information or action to arrive;
- preserving or losing future options.

The affected stakeholders include households, local businesses, essential community services, utility staff, and the municipal budget or governing authority.

Evidence can help estimate these consequences. But evidence does not by itself tell us how much each consequence should matter.

For example, a calculation may support the claim that higher production increases projected storage. It cannot, by itself, determine whether an extra $2,000 per day is worth paying, how precautionary the utility should be, or what public burden is acceptable. Those judgments require values, obligations, requirements, constraints, or other evaluative premises.

This is why “the data say we should increase production” is usually too compressed. The data may support beliefs about what higher production would do. A recommendation requires an additional bridge from consequences to what should be chosen.

### What would count as adequate?

A final framing question is:

> **What would count as a good enough answer for this intended use?**

There is no useful notion of overall adequacy that ignores use. A model or analysis that is adequate for a rough screening task may be inadequate for a threshold-sensitive operational decision. At the same time, some properties—such as arithmetic consistency or dimensional correctness—can be criticized regardless of use. The point is not that “anything is acceptable if the purpose says so.” The point is that the required evidence, precision, timeliness, and scope depend on what the answer must support [@nasa2024models; @fda2023credibility].

For this utility, provisional adequacy questions include:

- Is the current storage estimate reliable enough when less than 1 ML could change the action?
- Does the forecast cover the same seven-day horizon as the decision?
- Does evidence about historical demand support the specific claim being made?
- If an intervention is recommended, do we have evidence relevant to its consequences rather than only predictive association?
- Have material consequences and feasible alternatives been represented well enough for this decision?

These criteria are provisional. Later evidence can force us to revise them along with the analysis.

### A compact first frame

Before choosing a technical method, we can now state the problem more clearly:

- **Intended use:** support the Utility Director’s immediate operating decision during the seven-day heatwave.
- **Decision:** choose or authorize actions within the director’s authority and decide whether escalation is needed.
- **Decision-maker:** Utility Director; City Manager controls mandatory-restriction authorization.
- **Targets:** current physical usable storage, risk of falling below the 4.5 ML case reserve, and material consequences of candidate actions.
- **Alternatives:** continue, verify, increase production, request voluntary conservation, combine and stage actions, monitor, and escalate when warranted.
- **Consequences:** service margin, operating cost, public burden, timing, and future flexibility.
- **Stakeholders:** households, businesses, essential services, utility staff, and municipal governance.

This is not yet a complete analysis. It is a disciplined statement of what the analysis is for and what it must connect.

The next mistake to avoid is asking for the wrong **kind of claim**. A forecast, an intervention effect, a counterfactual comparison, and a recommendation can mention the same outcome while requiring different evidence and reasoning.

## 4. A First Complete Pass: Preventing a Town Water Shortage

A first pass is not a shortcut to the final answer. It is a disciplined way to discover what the problem actually requires before the analysis becomes expensive, formal, or difficult to reverse.

Consider a fictional small municipal water utility entering a seven-day hot, dry period. The numbers in this case are synthetic. They are designed to make the reasoning visible; they are not industry averages or regulatory standards.

At 08:00 on Monday, the utility dashboard reports **10.8 megaliters (ML)** of usable finished-water storage. The fictional utility's drought plan uses **4.5 ML** as an event-specific operating-reserve threshold. Current treated-water input is **8.4 ML per day**. A no-new-action demand forecast for the next seven days is:

| Day | Forecast high | Forecast demand |
|---:|---:|---:|
| 1 | 36°C | 9.0 ML |
| 2 | 38°C | 9.3 ML |
| 3 | 40°C | 9.6 ML |
| 4 | 40°C | 9.5 ML |
| 5 | 39°C | 9.4 ML |
| 6 | 37°C | 9.2 ML |
| 7 | 35°C | 8.9 ML |
| **Total** |  | **64.9 ML** |

The immediate decision-maker is the Utility Director. Broadly, the director could continue current operation, gather better information, increase treated-water production, ask customers to conserve water, combine several actions, or seek stronger action through another authority.

That looks like enough information to start calculating. It is. But calculation is only one part of the first pass.

### Frame and formulate

Start with intended use. The purpose here is not simply to "study demand" or "model storage." The immediate use is to **support the Utility Director's operating decision during the seven-day heatwave**.

That intended use immediately creates several different informational targets. We may want to know the current physical storage level. We may want to predict whether usable storage will fall below 4.5 ML during the horizon. We may want to estimate what would happen if treated-water production were increased. We may want to know what would happen if the utility issued a conservation request. None of those questions is identical to the decision itself.

This distinction matters because a decision can depend on several analytical answers at once. A good forecast is not automatically a recommendation, and a recommendation is not the same thing as the decision made by the authorized actor. Decision analysis distinguishes factual beliefs about consequences from the values and judgments needed to choose among them [@nasem2026decisionmaking].

The first provisional boundary can also stay simple. For this pass, include usable stored water, treated-water input, customer demand, the observation process that produces the dashboard value, the available operating actions, and any customer response that could materially change demand. We do not need a hydraulic network model, treatment-chemistry model, or full municipal governance model merely because those systems exist. The boundary is tied to what could change this decision.

Now use the simplest relevant balance:

`ending storage = starting storage + treated-water input - demand`

At current operation, seven-day treated-water input is:

`8.4 × 7 = 58.8 ML`

Using the dashboard value as the starting state gives:

`10.8 + 58.8 - 64.9 = 4.7 ML`

The result is just above the 4.5 ML reserve.

That is not a reassuring answer. It is a **conditional** answer. It says, in effect:

> If the dashboard value is an adequate representation of current physical storage, if the seven-day demand forecast is adequate for this use, and if operating conditions remain as represented, ending storage is projected to be about 4.7 ML.

Notice what this calculation has not established. It has not shown that 10.8 ML is the physical storage level. It has not established how demand would change after a conservation action. It has not chosen among actions. It has not shown that every important consequence has been represented.

A rival formulation now becomes important: **Is the urgent problem mainly forecasting future demand, or is it first verifying the current state?**

### Pause: what evidence should be questioned first?

Suppose the operational decision can change when starting storage moves by less than 1 ML. Before adding a more elaborate forecasting model, what evidence would you inspect first, and why?

Commit to an answer before continuing.

### Learn from evidence

The utility has an independent local pressure-based level check that does not use the same remote level transmitter as the dashboard. A field technician can obtain the check in about **25 minutes**.

At 08:25 the independent check indicates **9.9 ML** of usable storage. A follow-up check finds that the remote transmitter feeding the dashboard is reading high because of calibration drift.

Recompute the same balance:

`9.9 + 58.8 - 64.9 = 3.8 ML`

Nothing about the seven-day demand forecast changed. Nothing about the operating reserve changed. The target did not change. What changed was our evidence about the current physical state. That change is enough to move the projected ending level from slightly above the case reserve to below it.

This is the first backward move in the reasoning process.

**Revision 1: measurement / observation revision.**

We return to an earlier stage because the dashboard record was not the target itself. The target was physical usable storage. The record was evidence about that target, produced by an observation process. Once the observation process failed in a decision-relevant way, the current-state belief—and therefore the urgency of the decision—had to change.

The lesson is not that remote monitoring is inherently unreliable. Nor is it that every decision requires an independent physical check. The lesson is narrower: **when a decision is sensitive to a recorded value, the provenance and adequacy of that record can matter more than another layer of downstream modeling.**

Now consider the demand evidence. Historical hot-weather demand records can be useful for prediction. But predictive usefulness does not automatically tell us what would happen if we intervene. Prediction and causal explanation answer different questions, and an observed association alone does not establish the effect of an action [@shmueli2010predict; @pearl2009causal].

That matters because one candidate action is a voluntary conservation request. Suppose past requests were often followed by lower observed demand. Those episodes occurred under different weather and operating conditions and sometimes alongside other utility actions. The historical pattern may be informative, but by itself it does not isolate the effect of the request.

So our evidence situation is asymmetric. We have a direct reason to revise our belief about current storage. We have predictive evidence about demand under comparable no-new-action conditions. We have much weaker evidence about exactly how a new conservation request would change demand in this event.

A first pass should expose that asymmetry rather than hide it behind one confidence statement.

### Choose: consequences, alternatives, and authority

The director now has additional supplied facts.

The Utility Director may authorize a temporary increase in treated-water input from **8.4 to 8.8 ML/day**. The additional production takes **six hours** to become available, and operating at the higher rate costs an additional **$2,000 per 24 hours**. Production above 8.8 ML/day is unavailable during this event because of the supplied treatment and pumping constraints.

The director may also issue a **voluntary conservation request** and may increase monitoring. A **mandatory restriction**, however, requires approval by the City Manager and cannot take effect sooner than six hours after a request for authorization.

That authority distinction changes the alternative set. "Impose a mandatory restriction now" is not an action the Utility Director can directly choose. A realistic alternative is instead "request authorization for a mandatory restriction," perhaps conditionally if updated evidence crosses a trigger.

The option set should not be limited to "pump more" versus "do nothing." Plausible alternatives include verification, higher production, voluntary conservation, combinations of those actions, staged decisions, monitoring, and escalation. Generating alternatives is itself part of good decision framing; treating the first supplied option set as complete can make an analysis technically precise but practically poor [@keeney1996valuefocused].

What does the higher-production alternative do under the simple balance?

Because the increase arrives after six hours, seven-day treated-water input becomes:

`8.4 × 0.25 + 8.8 × 6.75 = 61.5 ML`

Using the verified 9.9 ML starting level:

`9.9 + 61.5 - 64.9 = 6.5 ML`

Under the central no-new-action demand forecast, higher production restores substantial margin above 4.5 ML.

But suppose, as a simple qualitative sensitivity check, we stress demand by **+0.4 ML/day** throughout the seven-day horizon. This is not a statistical prediction interval; it is just a supplied planning stress.

Stressed demand is:

`64.9 + (0.4 × 7) = 67.7 ML`

Then:

`9.9 + 61.5 - 67.7 = 3.7 ML`

Higher production helps, but it does not make the conclusion insensitive to demand assumptions.

Now the evidence-choice boundary becomes visible. The calculation supports a positive consequence claim:

> Under the supplied central demand forecast, increasing production raises projected ending storage from 3.8 ML to 6.5 ML.

But the calculation alone cannot tell us whether the additional **$2,000 per day** is worth paying, how much inconvenience from conservation is acceptable, how much operating margin should be preferred, or when the burden of a mandatory restriction is justified. Those are evaluative premises, requirements, or judgments. Evidence informs the expected consequences; it does not by itself determine how those consequences should be valued [@nasem2026decisionmaking].

A defensible first-pass recommendation might therefore be staged:

- verify the physical state;
- increase production within the director's authority;
- issue a voluntary conservation request if the stated evaluative premises support the additional margin relative to its burden;
- monitor storage and demand;
- retain escalation as a contingent alternative if the updated projection again crosses the case reserve.

That recommendation is not the decision. The decision occurs when the Utility Director authorizes the actions within the director's authority and, if needed, requests authorization from the City Manager for actions outside it.

Nor is the staged recommendation uniquely correct. A different decision-maker with different legitimate evaluative premises could prefer a different balance of operating cost, precaution, public burden, and future flexibility. Chapter 10 will treat values and alternatives more systematically, and Chapter 11 will treat formal choice under uncertainty. Here we only need to make the bridge visible.

### Act in a responsive system

So far the balance has looked almost static, but the decision is not.

Usable storage carries over from one period to the next. Treated-water input adds to it. Customer demand removes from it. The higher-production action is delayed by six hours. The independent verification takes 25 minutes. The director will reconsider the decision after new information arrives.

There is also feedback in the ordinary systems sense used here: observations influence actions; actions change future storage or demand; the resulting observations influence later actions. Formal stock-flow diagrams, feedback-loop analysis, stability, and control belong later. For the first pass, the important question is simply whether today's action changes tomorrow's state, information, or behavior.

This matters especially for conservation.

The original demand forecast was explicitly a **no-new-action forecast**. It described expected demand if no new conservation request or restriction were introduced. Once a conservation request is deployed, that condition is no longer automatically true.

Suppose the director chooses the staged combination: verified state, temporary production increase, voluntary conservation request, and enhanced monitoring.

Twenty-four hours later, observed demand is **8.6 ML**, compared with the pre-action forecast of **9.0 ML** for that period. Several monitored large users report that they reduced nonessential use in response to the request.

It would be tempting to say that the conservation request "saved 0.4 ML." That conclusion is not warranted. The difference between one forecast and one observed value does not identify the causal effect of the request. Weather, ordinary forecast error, other operating changes, and other factors could also contribute.

But something important **has** been established for the framing of the next decision: the system after deployment is no longer adequately represented as a system in which no new conservation action occurred.

Models, rules, predictions, and policies can become part of the process they are used to manage. When people respond to them, the process generating future observations can differ from the historical process used to build the original prediction [@perdomo2020performative]. More generally, feedback, delays, and behavioral response can make learning from interventions difficult if we treat the environment as passive [@sterman2006evidence].

### Backward Revision 2: the process has changed

Return to the earlier forecast formulation.

The first demand forecast answered a clear question:

> What demand should we expect over the next seven days if no new conservation action is introduced?

After the utility introduces a conservation request and users respond, that is no longer the right forecast question for the next review.

This is not merely "replace 9.0 with 8.6 and continue." The analyst should reconsider the forecast assumptions, the monitoring plan, and perhaps the representation of demand response. The action has changed the process that produces future demand.

**Revision 2: structural / process revision.**

Contrast this with the first revision. In Revision 1, the target process did not change; our observation of the current state was wrong. In Revision 2, the decision itself helped change the process we were trying to forecast.

### Pause: estimate update or process revision?

What exactly changed after the conservation request: our estimate of an unchanged demand process, or the demand process relevant to the next decision?

A strong answer can acknowledge both uncertainty and structure. We do not yet know the causal effect precisely. But we do know that a forecast explicitly conditioned on no new conservation action cannot simply be carried forward as though the intervention never occurred.

### Integrate, monitor, and decide again

The decision therefore unfolds through repeated reviews rather than one irreversible choice for the full seven days.

A simple cadence is enough for the first pass:

1. **08:00 Monday:** frame the decision and initial evidence.
2. **About 08:25:** review after the independent storage verification.
3. **After actions are authorized:** monitor whether the production increase is online and how storage and demand evolve.
4. **About 24 hours later:** update the projection using verified storage, actual demand, production status, and the changed behavioral environment.
5. **If the updated projection again falls below 4.5 ML:** reconsider the alternative set, including a request to the City Manager for mandatory-restriction authority.

No dynamic programming or control theory is needed to see the central point: **today's action can change tomorrow's state, tomorrow's evidence, and tomorrow's decision.**

The first-pass record now looks something like this:

| Element | Current first-pass statement |
|---|---|
| Intended use | Support the immediate seven-day operating decision |
| Decision-maker | Utility Director; some escalation requires City Manager |
| Target(s) | Current physical storage; reserve breach; consequences of candidate actions |
| Evidence | Dashboard record, independent verification, demand history, current observations |
| Important evidence limit | Historical patterns and a single post-action observation do not isolate the conservation effect |
| Alternatives | Continue, verify, raise production, request voluntary conservation, combine, monitor, escalate |
| Material consequences | Storage margin, continuity, operating cost, customer burden, timing, future flexibility |
| Dynamics | Storage carries over; action and information are delayed; decision is repeated |
| Response | Conservation action can change the process producing future demand |
| Revision triggers | Measurement discrepancy; post-deployment behavioral response; updated reserve projection |
| Routing | Representation, measurement, evidence, causal, value, decision, dynamics, and strategy machinery in later chapters as needed |

This table is a record of this case, not a mandatory universal checklist. A simpler problem may screen out several of these issues as immaterial. A harder problem may require much more detail.

The point of the exercise was not to complete a professional water-utility analysis in a few pages. The point was to experience one complete pass through a consequential problem and to watch the reasoning move backward twice for different reasons.

The first revision said: **our record of the current state was wrong enough to change the decision.**

The second said: **our action changed the process, so the old forecast question was no longer adequate.**

Those two failures require different repairs. Recognizing that difference is one of the central skills this book will develop.
