---
chapter: 1
part: 1
title: "Decisions, Questions, and a First Complete Pass"
status: drafted
---

# Chapter 1: Decisions, Questions, and a First Complete Pass

## 1. A Good Answer to the Wrong Question

At 08:00 on Monday, a fictional small municipal water utility is entering a seven-day hot, dry period.
Its usable finished-water storage capacity is **14.0 megaliters (ML)**, and the operations dashboard reports **10.8 ML** currently in storage.
The utility's drought plan uses **4.5 ML** as an event-specific operating-reserve threshold — a planning rule supplied by this fictional case, not an industry standard.
Falling below the reserve would not mean that taps immediately run dry; it would mean that the operating margin the plan treats as acceptable is gone, and that the situation must be reconsidered or escalated.
Current treated-water input is **8.4 ML per day**.

The utility's no-new-action demand forecast — expected demand if no new conservation action is introduced — is:

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

The immediate decision-maker is the Utility Director.
Broadly, the director could continue current operation, gather more information, increase treated-water production, ask customers to conserve water, combine several actions, or seek stronger action through another authority.

You have enough information to start doing something.
That is the point.

### Before reading further: make a first pass

Take about **five minutes**.
Without looking for a named method or checklist, write a short response to four questions:

1. What should be modeled, calculated, or otherwise determined?
2. What evidence would you want to check first?
3. What action would you advise now?
4. What is one important assumption you are making?

Keep what you write.
Do not polish it after the fact.

This response is not a graded test.
It is a baseline.
Later in the chapter you will compare it with a more explicit first-pass analysis and with an unfamiliar problem.

The temptation is to start with technique.
You might sum the seven-day demand forecast, project the storage balance, fit a demand model, inspect recent weather-demand data, or compare operating scenarios.
Any of those could be technically competent.

But competent work can still answer the wrong question.

Consider several analyses that an expert might reasonably begin in this same situation:

- forecast demand over the next seven days;
- verify the current physical storage level;
- calculate whether the reserve will be crossed under current operation;
- estimate the consequence of increasing treated-water production;
- estimate the consequence of issuing a conservation request;
- compare combinations of actions and recommend what the director should do.

These are not interchangeable tasks.
They differ in what must be determined, what evidence would count, what assumptions matter, and what kind of conclusion is justified.

A highly accurate demand forecast could still be a poor answer if the urgent problem is that the current storage record is unreliable.
A precise estimate of storage could still be insufficient if the actual question is what a conservation action would do.
A strong estimate of action consequences could still fail to determine what should be chosen if the relevant costs, burdens, obligations, and authority are left implicit.

So before asking, "Which model should we use?" or "Which method is best?", ask a more basic question:

> **What is being asked, for what use, and what would count as an adequate answer?**

That question is the organizing problem of this chapter.

It does not mean that every real problem begins with a perfectly stated decision.
Sometimes the immediate task is a scientific judgment, an estimate, a diagnosis, a forecast, or an authorization request.
Nor does it mean that all analysis must wait until every value and stakeholder is formally catalogued.
A first pass is supposed to be fast enough to use.

The discipline is narrower: do not let the available data, familiar technique, or first wording of the problem silently decide what question you answer.

The same topic can contain several legitimate questions.
The job is to make the relevant one explicit enough that two competent analysts are not doing different work while believing they agree.

We therefore begin not with a model class, but with the **intended use** of the answer and the **decision situation** in which it will matter.

## 2. Intended Use and the Decision Situation

"Water shortage" is a topic.
"Will demand exceed supply?" is an analytical question.
"Should the utility change operations this morning?" is a decision.
Those objects are related, but they are not interchangeable.

The first discipline is simple:

> **State what the answer will be used for before deciding what answer to produce.**

In the water case, the immediate intended use is to support the Utility Director's operating decision during a seven-day heatwave.
That is more informative than saying that the purpose is to "understand demand" or "analyze storage."
It tells us who needs the answer, when it will be used, and what kind of consequence an inadequate answer could have.

Here an inadequate answer can fail in two directions.
**False reassurance** treats the situation as safe while usable storage is actually heading below the reserve.
**False alarm** imposes cost and public burden that the real situation did not require.
The two failures fall on different people, which is one more reason the analysis cannot be judged apart from its use.

Engineering model-credibility and verification-and-validation frameworks are built around stated intended uses because a model's adequacy cannot be judged apart from the application the model must support [@nasa2024models; @nrc2012reliability].
Chapter 1 extends that discipline beyond formal models — a pedagogical extension, not a claim those standards make themselves: an estimate, forecast, comparison, or recommendation should also be judged against what someone intends to do with it.

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

Conversely, the same target can serve different intended uses.
An estimate of current physical storage could be used to decide whether to change operations now, to investigate a sensor discrepancy, or to prepare a monthly operating report.
The target may be similar while the required timeliness, accuracy, evidence, and consequences of error differ.

A useful test is:

> Would two competent analysts, given this target statement, know that they are trying to answer the same substantive question?

If not, the target needs another material qualifier.
Perhaps the population, system, horizon, comparison, aggregation, or required answer form is missing.
But qualification should solve ambiguity, not become a ritual.
"Usable storage in the utility's main finished-water facility at 08:00 Monday" is useful if the immediate state matters.
Adding irrelevant descriptors does not make the target more scientific.

### The record is not automatically the thing we care about

The dashboard displays **10.8 ML**.
It is tempting to write:

> Current storage = 10.8 ML.

That sentence silently turns a record into the target.

A more careful first pass distinguishes at least three things:

- the **target**: current physical usable storage;
- the **record**: 10.8 ML displayed on the dashboard;
- the **observation process**: a remote level transmitter and telemetry system that produced the record.

At this point we have no reason to declare the dashboard wrong.
We also have no reason to erase the distinction.
A measurement or administrative record can be excellent evidence about a target without being identical to the target itself.

That separation will become much more important in Chapters 3 and 4.
For now, it prevents a common framing error: answering a question about what was recorded when the decision depends on what is physically or substantively true.

### Name the decision—and who can make it

Now make the decision situation explicit.

The **decision-maker** is the person, group, or institution with authority or responsibility for the immediate decision.
Here it is the Utility Director.

The case supplies a fictional authority structure.
The director may:

- order an independent verification of the storage level;
- increase treated-water production up to a permitted temporary limit of **8.8 ML/day**;
- issue a voluntary conservation request;
- increase monitoring and review frequency.

The director may **not** directly impose a mandatory water-use restriction.
That requires City Manager approval.

This matters because an action is not a genuine alternative for a decision-maker merely because an analyst can imagine it.
If another actor controls the action, the relevant alternative may be to **request**, **negotiate**, **escalate**, or **seek authorization**.

It also keeps three objects separate:

| Object | What it does |
|---|---|
| Analysis | Describes, predicts, estimates, or otherwise characterizes relevant facts and consequences |
| Recommendation | Advises what should be chosen given stated or assumed evaluative premises |
| Decision | Selects, authorizes, or commits to an action by the relevant decision-maker |

Evidence can change an analysis.
An analyst can issue a recommendation.
Neither event is automatically the decision itself.
Practical decision processes similarly distinguish facts, values, alternatives, predicted consequences, uncertainty, and the actual choice [@nasem2026decisionmaking].

### Do not accept the first option set as complete

Suppose the problem is initially phrased as:

> Should we pump more or do nothing?

That is already a decision question, but the alternatives are suspiciously narrow.

The Utility Director could also verify the current state before acting, issue a voluntary conservation request, combine production and conservation, increase monitoring, stage actions over time, or prepare an escalation request if a later trigger is crossed.

An **alternative** is a candidate course of action that can actually be chosen, authorized, requested, negotiated, or otherwise pursued.
Good decision framing does not assume that the first alternatives supplied by the problem statement exhaust the possibilities.
Value-focused decision analysis makes active creation of alternatives an explicit part of better decision making [@keeney1996valuefocused].

Chapter 1 does not require a formal alternative-generation method.
It asks for something simpler:

> If the supplied option set is materially narrow, can you name at least one plausible missing, combined, contingent, information-gathering, staged, or escalation alternative?

That question is often enough to prevent a false binary from controlling the rest of the analysis.

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

Evidence can help estimate these consequences.
But evidence does not by itself tell us how much each consequence should matter.

For example, a calculation may support the claim that higher production increases projected storage.
It cannot, by itself, determine whether the additional operating cost is worth paying, how precautionary the utility should be, or what public burden is acceptable.
Those judgments require values, obligations, requirements, constraints, or other evaluative premises.

This is why "the data say we should increase production" is usually too compressed.
The data may support beliefs about what higher production would do.
A recommendation requires an additional bridge from consequences to what should be chosen.

### What would count as adequate?

A final framing question is:

> **What would count as a good enough answer for this intended use?**

There is no useful notion of overall adequacy that ignores use.
A model or analysis that is adequate for a rough screening task may be inadequate for a threshold-sensitive operational decision.
At the same time, some properties—such as arithmetic consistency or dimensional correctness—can be criticized regardless of use.
The point is not that "anything is acceptable if the purpose says so."
The point is that the required evidence, precision, timeliness, and scope depend on what the answer must support [@nasa2024models; @fda2023credibility].

For this utility, provisional adequacy questions include:

- Is the current storage estimate reliable enough when less than 1 ML could change the action?
- Does the forecast cover the same seven-day horizon as the decision?
- Does evidence about historical demand support the specific claim being made?
- If an intervention is recommended, do we have evidence relevant to its consequences rather than only predictive association?
- Have material consequences and feasible alternatives been represented well enough for this decision?

These criteria are provisional.
Later evidence can force us to revise them along with the analysis.

### A compact first frame

Before choosing a technical method, we can now state the problem more clearly:

- **Intended use:** support the Utility Director's immediate operating decision during the seven-day heatwave.
- **Decision:** choose or authorize actions within the director's authority and decide whether escalation is needed.
- **Decision-maker:** Utility Director; City Manager controls mandatory-restriction authorization.
- **Targets:** current physical usable storage, risk of falling below the 4.5 ML case reserve, and material consequences of candidate actions.
- **Alternatives:** continue, verify, increase production, request voluntary conservation, combine and stage actions, monitor, and escalate when warranted.
- **Consequences:** service margin, operating cost, public burden, timing, and future flexibility.
- **Stakeholders:** households, businesses, essential services, utility staff, and municipal governance.

This is not yet a complete analysis.
It is a disciplined statement of what the analysis is for and what it must connect.

The next framing hazard is subtler: asking for the wrong **kind of claim**.

## 3. What Kind of Question Is This?

Two questions can mention the same system and the same outcome while asking for different kinds of answers.

Consider four questions about the water utility:

1. Is hotter weather associated with higher water demand?
2. Will usable storage fall below 4.5 ML during the next seven days?
3. Would a voluntary conservation request reduce shortage risk compared with no request?
4. Should the Utility Director issue the request?

The same records may be relevant to all four.
They do not support the same claim automatically.

A useful first pass therefore screens the question in layers.
The layers are neither an exhaustive taxonomy nor mutually exclusive boxes.
Their job is to expose what kind of evidence and reasoning the answer will require.

### First layer: what would happen, and what should matter?

Begin before technical labels.
Ask whether a component concerns:

- **what is, was, or would happen under specified conditions**, or
- **what should matter, count as acceptable or preferable, or be done**.

The first kind is often called **positive** and the second **normative**; the what-is / what-ought distinction has a long history in economics [@keynes1891scope].

Positive does not mean "certain," "objective," or "merely descriptive."
A forecast is positive when it asks what will happen.
An intervention or counterfactual question can also be positive when it asks what would happen under a specified change.

Normative does not mean "unsupported opinion."
Practical judgments about what should count as preferable may be constrained by law, professional obligation, policy, ethical reasoning, institutional purpose, or stated values.
Structured decision work likewise separates facts and consequence estimates from values and objectives used to evaluate them [@bradley2016structured].

In the water case:

- "Will storage fall below 4.5 ML?" is positive.
- "How much additional operating cost would higher production create?" is also positive.
- "How much burden is acceptable to reduce shortage risk?" introduces a normative premise.
- "Should the director issue a conservation request?" connects positive beliefs about consequences to normative or institutional premises about what should be preferred.

A consequential problem often contains both layers.
The point is to notice where evidence about what would happen ends and evaluation of those consequences begins.

### Second layer: what kind of claim is being asked for?

Within the positive part of a problem, several claim forms may appear.

**Association** asks whether variables or events are related under observed or specified conditions.

> On historically hot days, was higher temperature associated with higher demand?

That relationship may be useful, but by itself it does not establish what would happen if we changed a predictor or introduced a policy.

**Prediction** asks about an unknown, new, or future observable given the information currently available.

> Given the current storage record, weather forecast, and demand history, will usable storage fall below reserve during the next seven days?

A useful predictor need not be a lever that would change the outcome if we intervened on it [@shmueli2010predict].

**Intervention** asks what would happen under an action or changed condition.

> Would issuing a voluntary conservation request reduce shortage risk compared with not issuing one?

Association alone is not enough to establish that intervention effect; causal conclusions require additional assumptions or design information [@pearl2009causal].
Formal causal identification belongs to Chapter 7.

**Counterfactual** asks about an alternative outcome under a changed action or condition while retaining relevant factual or background information.

> Suppose the utility crossed its reserve yesterday. Would that crossing have been avoided if a conservation request had been issued three days earlier?

This is not just any hypothetical story.
It compares the factual situation with an alternative course under a specified change.

These forms can overlap.
A decision analysis may require a demand prediction, an intervention estimate for a conservation action, and a counterfactual assessment of an earlier missed action.
The mistake is to force the whole problem into one label or to assume that evidence adequate for one claim automatically supports the others.

### Same outcome, different question

| Question | What is being asked? | What would not be enough by itself? |
|---|---|---|
| Are hotter days associated with higher demand? | Association | A causal conclusion about changing demand |
| What will demand be tomorrow? | Prediction | Evidence that a predictor is a causal lever |
| What would a conservation request do to demand? | Intervention consequence | Historical association alone |
| What would demand have been without yesterday's request? | Counterfactual comparison | An unrelated hypothetical scenario |
| What should the utility do? | Recommendation / decision support | Consequence evidence without evaluative premises |

### Third layer: what kind of environment are we acting in?

Even when the claim type is clear, the environment can change what must be represented.

Ask:

> **What changes through time? What carries over? What is delayed? What feeds back? Will we decide again? Who or what may respond to our action, rule, model, metric, or prediction—and could that response change the process we thought we were analyzing?**

These are screening questions, not a new formal framework.

A problem is **dynamic** when relevant states or conditions evolve through time.
Dynamics do not require strategic behavior.
A simple pendulum changes through time, yet it does not adapt because it anticipates our model.

At the introductory depth used here, **feedback** occurs when effects of a process or action return through the system and influence later behavior, outcomes, information, or actions.
Chapter 1 does not classify feedback as positive or negative or analyze stability; those topics belong later.

Repeated choice is yet another distinct property: a decision can be revisited as state or information changes even when nothing in the system is strategic.

People and institutions may also **adapt** or respond **strategically**.
Adaptation is broader: behavior changes after conditions, information, experience, or intervention change.
Strategic response is narrower: behavior changes partly because a rule, incentive, metric, prediction, policy, or anticipated action of others makes some response more advantageous.
The presence of people does not automatically make a problem strategic.

### Two short contrasts

A pendulum used to estimate local gravitational acceleration, predict short-horizon angular position, or design a durable clock is the same physical system under different intended uses.
The representation and adequacy requirements can change, but the example remains dynamic without being adaptive or strategic.

Now consider a 20-item student assessment used to rank applicants, diagnose prerequisite skills, or choose the next instructional activity.
The observed responses are the same kind of record, but the intended use and target differ.
If the score becomes consequential, students or institutions may also change behavior in response to the rule.

The contrast is structural:

- the pendulum shows **dynamic does not imply strategic**;
- the assessment shows that **measurement and decision use can change the environment in which later data are produced**.

### Pause: a predictor is not automatically a lever

Suppose historical data show that a particular variable predicts shortage very well.

Why does that not, by itself, tell us that changing that variable will prevent shortage?

Commit to an explanation before continuing.

A strong answer distinguishes prediction from intervention.
The first asks whether the variable helps forecast an outcome; the second asks what would happen if an action changed something in the system.

### A compact screen

A first pass can now ask three layers without pretending they form a complete ontology:

1. **Positive or normative:** are we asking what is or would happen, what should matter or be done, or both?
2. **Claim form:** is the relevant component associational, predictive, interventional, counterfactual, or some combination?
3. **Environment:** do time, accumulation, delay, feedback, repeated choice, adaptation, or strategic response materially change the analysis?

The purpose is not to reward labeling.
It is to make the next question sharper:

> **What evidence and reasoning would actually be capable of answering this claim in this environment?**

We can now perform the whole first pass once, with the details arriving in the order an analyst might actually encounter them.

## 4. A First Complete Pass: Preventing a Town Water Shortage

A first pass is not a shortcut to the final answer.
It is a disciplined way to discover what the problem actually requires before the analysis becomes expensive, formal, or difficult to reverse.

We will use a five-part navigation through the case:

**Frame and formulate → Learn from evidence → Choose → Act in responsive systems → Integrate and revise**

This is a book-specific navigation device, not a formal scientific theory or a mandatory waterfall.
Later evidence can send us backward to an earlier question, target, observation process, representation, alternative, or decision.

Return to the fictional utility.
The numbers are synthetic.
They are designed to make the reasoning visible; they are not industry averages or regulatory standards.
The case is also deliberately simplified: a real event of this kind would involve engineering, regulatory, and communication detail that this chapter intentionally leaves outside its boundary, and the points where professional expertise would be required are flagged as they arise.

At 08:00 Monday, the dashboard reports **10.8 ML**.
The case reserve is **4.5 ML**.
Current treated-water input is **8.4 ML/day**.
Seven-day forecast demand totals **64.9 ML**.

### Frame and formulate

The intended use is to **support the Utility Director's operating decision during the seven-day heatwave**.

Relevant informational targets include current physical storage, whether storage will cross the case reserve, and the consequences of candidate actions.
None is identical to the decision itself.

The first provisional boundary can stay simple.
Include usable stored water, treated-water input, customer demand, the observation process that produces the dashboard value, available actions, and any customer response that could materially change demand.
We do not need a hydraulic network model, treatment-chemistry model, or full municipal governance model merely because those systems exist.

Use the simplest relevant balance:

`ending storage = starting storage + treated-water input - demand`

At current operation, seven-day treated-water input is:

`8.4 × 7 = 58.8 ML`

Using the dashboard value as the starting state:

`10.8 + 58.8 - 64.9 = 4.7 ML`

The result is just above the 4.5 ML reserve.

That is a **conditional** answer:

> If the dashboard value adequately represents current physical storage, if the seven-day demand forecast is adequate for this use, and if operating conditions remain as represented, ending storage is projected to be about 4.7 ML.

The important feature of 4.7 ML is not its numerical precision.
It is its **decision sensitivity**.
The projection sits only 0.2 ML above the case reserve.
A modest error in starting storage or demand could reverse the reserve-crossing conclusion.
That tells the analyst what to ask next: which uncertain input can be checked soon enough, and accurately enough, to change the immediate action?

The calculation has not established that 10.8 ML is the physical storage level.
It has not established how demand would change after a conservation action.
It has not chosen among actions.
The next step should therefore be driven by decision relevance, not by a reflex to make the forecast more elaborate.

A rival formulation becomes important: **Is the urgent problem mainly forecasting future demand, or is it first verifying the current state?**

### Pause: what evidence should be questioned first?

Suppose the operational decision can change when starting storage moves by less than 1 ML.
Before adding a more elaborate forecast model, what evidence would you inspect first, and why?

Commit to an answer before continuing.

### Learn from evidence

The utility can obtain an independent local **tank-level check derived from a pressure measurement**.
It uses a different observation path from the remote level transmitter that feeds the dashboard, and a field technician can complete it in about **25 minutes**.
The measured tank level converts to usable volume through the utility's own tank geometry and calibration; the case supplies that conversion, and the reader is not asked to perform it.
This is not a claim that an arbitrary pressure reading somewhere in a distribution system reveals storage volume.
It is a supplied second way of observing the same physical state.

Why is that check worth considering?
Not because "more data" are automatically better.
The check has three properties that make it decision-relevant here:

- the starting storage value is influential enough to change the reserve-crossing conclusion;
- the independent check uses a different observation path from the dashboard;
- it can arrive in 25 minutes, while the operational decision still has time to change.

Information that arrives after the decision is irreversible, or that cannot move the action, would be much less useful for this immediate purpose.
Chapter 11 will later formalize questions about the value of information; here the qualitative screen is enough.

At 08:25 the independent check indicates **9.9 ML** of usable storage.
A follow-up inspection finds that the remote transmitter feeding the dashboard is reading high because of calibration drift.

Recompute:

`9.9 + 58.8 - 64.9 = 3.8 ML`

The before/after comparison is compact:

| Item | Initial pass | After independent verification | What changed? |
|---|---:|---:|---|
| Evidence about current storage | Dashboard: 10.8 ML | Independent check: 9.9 ML | Current-state evidence |
| Seven-day demand forecast | 64.9 ML | 64.9 ML | Nothing |
| Operating reserve | 4.5 ML | 4.5 ML | Nothing |
| Projected ending storage | 4.7 ML | 3.8 ML | Consequence of revised state belief |
| Reserve-crossing conclusion | Slightly above | Below | Decision relevance changes |

The target did not change.
The seven-day demand forecast did not change.
The reserve did not change.
What changed was our evidence about the current physical state, and that change was sufficient to alter the practical conclusion.

**Backward revision 1 — a measurement/observation revision.**

We move backward because the dashboard record was not the target itself.
The target was physical usable storage.
The record was evidence about that target, produced by an observation process.
Once that process failed in a decision-relevant way, the current-state belief—and therefore the urgency of the decision—had to change.

The lesson is not that remote monitoring is inherently unreliable or that every decision needs an independent check.
It is narrower: **when a decision is sensitive to a recorded value, the provenance and adequacy of that record can matter more than another layer of downstream modeling.**

Now consider the demand evidence.
Historical hot-weather demand records can be useful for prediction.
But predictive usefulness does not automatically tell us what would happen if we intervene.
An observed association alone does not establish the effect of an action [@shmueli2010predict; @pearl2009causal].

Suppose past voluntary conservation requests were often followed by lower observed demand.
Those episodes occurred under different weather and operating conditions and sometimes alongside other utility actions.
The historical pattern may be informative, but by itself it does not isolate the effect of the request.

So the evidence is uneven.
We now have strong case-specific reason to revise current storage.
We have a forecast for demand under a no-new-action condition.
We have weaker evidence about the causal effect of a new conservation request.
A first pass should expose that asymmetry rather than compress it into one confidence statement.

Before choosing, ask what remains uncertain **and which uncertainties matter to the next action**.
We still do not know the exact conservation effect, future forecast error, or whether the higher-production action will be sufficient under a hotter-than-expected demand path.
Those are reasons to compare alternatives and preserve monitoring, not reasons to pretend no decision can be made yet.

### Choose: consequences, alternatives, and authority

Return to the supplied action facts and quantify their consequences.

The Utility Director may authorize a temporary increase in treated-water input from **8.4 to 8.8 ML/day**.
For this fictional event, 8.8 ML/day is already supplied as the **permitted temporary operating limit** within the utility's treatment, source, water-quality, and pumping constraints; production above it is unavailable during this event.
The case is not suggesting that a director can raise drinking-water output independently of such constraints.
The case also stipulates a **six-hour production ramp-up** before the higher output becomes available — a synthetic case fact, not a typical industry response time — at an incremental cost of **$2,000 per 24 hours**.

The director may also issue a voluntary conservation request and increase monitoring.
A mandatory restriction requires City Manager approval and cannot take effect sooner than six hours after a request for authorization — a governance delay supplied by the case, separate from the production ramp-up.

The alternatives differ not only in expected effect but also in timing, burden, reversibility, and authority:

| Alternative | Authority / timing | Material consequence to consider |
|---|---|---|
| Continue current operation | Immediate | Avoids added cost and burden but leaves little margin under revised state |
| Increase production | Director; effect after 6 h ramp-up | Adds storage margin at $2,000 per 24 h |
| Voluntary conservation request | Director; behavioral effect uncertain | May reduce demand with public inconvenience but uncertain causal effect |
| Request mandatory restriction | City Manager approval; at least 6 h | Potentially stronger burden and response; not directly selectable by director |
| Staged combination + monitoring | Director can begin several components now | Preserves ability to revise as new evidence arrives |

Because the higher output arrives only after the case-stipulated six-hour ramp-up, seven-day treated-water input becomes:

`8.4 × 0.25 + 8.8 × 6.75 = 61.5 ML`

Using the verified 9.9 ML starting level:

`9.9 + 61.5 - 64.9 = 6.5 ML`

Under the central no-new-action demand forecast, higher production restores substantial margin above 4.5 ML.

Now stress demand by **+0.4 ML/day** throughout the seven-day horizon.
This is a supplied planning stress, not a statistical prediction interval.

`64.9 + (0.4 × 7) = 67.7 ML`

Then:

`9.9 + 61.5 - 67.7 = 3.7 ML`

Higher production helps, but it does not make the conclusion insensitive to demand assumptions.
The central calculation and the stress calculation support different statements: one says the action creates margin under the central forecast; the other says that margin is not robust to the supplied high-demand stress.

The evidence-choice boundary is now visible.
The calculation supports a positive consequence claim:

> Under the supplied central demand forecast, increasing production raises projected ending storage from 3.8 ML to 6.5 ML.

The calculation alone cannot tell us whether the additional **$2,000 per day** is worth paying, how much inconvenience from conservation is acceptable, how much operating margin should be preferred, or when the burden of a mandatory restriction is justified.
Evidence informs expected consequences; it does not by itself determine how those consequences should be valued [@nasem2026decisionmaking].

Make the evaluative bridge explicit.
For this worked recommendation, suppose the decision-maker accepts these case premises:

- a projected breach of the 4.5 ML operating reserve is materially undesirable;
- paying the supplied short-horizon production cost is acceptable when it buys meaningful operating margin;
- a voluntary request is less burdensome than a mandatory restriction and is acceptable when margin is thin, even though its exact effect is uncertain;
- stronger restrictions should remain contingent on updated evidence rather than being imposed solely because they are available.

These premises are not empirical findings hidden in the data.
They state how consequences are being judged for this decision.
A different legitimate set of premises could support a different recommendation.

Given those premises, a defensible first-pass recommendation is staged:

- verify the physical state;
- increase production within the director's authority;
- issue a voluntary conservation request;
- monitor storage, demand, and production status;
- retain escalation as a contingent alternative if the updated projection again crosses the case reserve.

That recommendation is not the decision.
The decision occurs when the Utility Director authorizes permitted actions and, if needed, requests authorization from the City Manager for actions outside that authority.

The staged form also matters.
It avoids treating the seven-day horizon as one irreversible commitment.
The director can act on what is sufficiently supported now while preserving the ability to revise when better evidence arrives.

### Act in a responsive system

The balance is simple, but the decision is not static.

Usable storage carries over from one period to the next.
Treated-water input adds to it.
Customer demand removes from it.
The higher-production action is delayed by the six-hour ramp-up.
The independent verification takes 25 minutes.
The director will reconsider the decision after new information arrives.

There is also feedback in the ordinary systems sense used here: observations influence actions; actions change future storage or demand; resulting observations influence later actions.
Formal stock-flow diagrams, feedback-loop analysis, stability, and control belong later.

This matters especially for conservation.

The original demand forecast was explicitly a **no-new-action forecast**.
It described expected demand if no new conservation request or restriction were introduced.
Once a conservation request is deployed, that condition is no longer automatically true.

Suppose the director chooses the staged combination: verified state, temporary production increase, voluntary conservation request, and enhanced monitoring.

Twenty-four hours later, observed demand is **8.6 ML**, compared with the pre-action forecast of **9.0 ML** for that period.
Several monitored large users report that they reduced nonessential use in response to the request.

It would be tempting to say that the conservation request "saved 0.4 ML."
That conclusion is not warranted.
The difference between one forecast and one observed value does not identify the causal effect of the request.
Weather, ordinary forecast error, other operating changes, and other factors could contribute.

But something important **has** been established for the framing of the next decision: the system after deployment is no longer adequately represented as a system in which no new conservation action occurred.

Predictions used to support decisions can influence the outcomes they are intended to predict when people respond to them [@perdomo2020performative].
Chapter 1 uses a broader version of that warning as a pedagogical synthesis: a deployed rule, metric, model, or policy can also become part of a responsive environment.
More generally, feedback, delays, omitted responses, and narrow boundaries can make learning from interventions difficult [@sterman2006evidence].

### Backward revision 2: the process has changed

Return to the earlier forecast formulation.

The first demand forecast answered:

> What demand should we expect over the next seven days if no new conservation action is introduced?

After the utility introduces a conservation request and users respond, that is no longer the right forecast question for the next review.

This is not merely "replace 9.0 with 8.6 and continue."
The analyst should reconsider the forecast assumptions, monitoring plan, and perhaps the representation of demand response.
The action has changed the process that produces future demand.

**This second revision is a structural/process revision, not a numerical parameter update.**

Contrast the two revisions.
In Revision 1, the target process did not change; our observation of the current state was wrong.
In Revision 2, the decision itself helped change the process we were trying to forecast.

What did not change is equally important.
The intended use is still to support the utility's short-horizon operating decision, the physical reserve remains a case constraint, and the director's authority has not changed.
Revision should be targeted to the part of the formulation that failed, not used as an excuse to rebuild everything.

### Pause: estimate update or process revision?

What exactly changed after the conservation request: our estimate of an unchanged demand process, or the demand process relevant to the next decision?

Commit to an answer before continuing.

A strong answer can acknowledge both uncertainty and structure.
We do not yet know the causal effect precisely.
But we do know that a forecast explicitly conditioned on no new conservation action cannot simply be carried forward as though the intervention never occurred.

### Integrate, monitor, and decide again

The decision unfolds through repeated reviews rather than one irreversible choice for the full seven days.

A simple cadence is enough:

1. **08:00 Monday:** frame the decision and initial evidence.
2. **About 08:25:** review after independent storage verification.
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
| Routing | Representation/measurement; probability/causal evidence; values/decision; dynamics/strategy as needed |

This table is a record of this case, not a mandatory universal checklist.
A simpler problem may screen out several issues as immaterial.
A harder problem may require much more detail.

The first pass has not completed a professional water-utility analysis.
It has done something more basic and more transferable: it has exposed what must be learned next.
The observation problem routes toward Chapters 3–4; forecast uncertainty and intervention evidence toward Chapters 6–8; values and choice toward Chapters 10–11; and repeated, responsive behavior toward Chapters 13–15.
The first pass is successful partly because it tells us where specialist machinery is now warranted.

The first revision said: **our record of the current state was wrong enough to change the decision.**

The second said: **our action changed the process, so the old forecast question was no longer adequate.**

Those failures require different repairs.
Section 5 turns that distinction into a more general habit.

## 5. When the First Formulation Fails

A first formulation is provisional by design.
If later evidence can never send us backward, either the problem is unusually simple or we have made the reasoning process too rigid.

The important distinction is between **updating an answer inside the same formulation** and **changing the formulation itself**.

A new weather forecast or newer trusted storage reading may change numbers while leaving the target, comparison, boundary, authority, alternatives, and intended use intact.
Other discoveries are different.
If the dashboard record is not an adequate representation of physical storage, the observation problem must be reconsidered.
If conservation changes the process generating future demand, a no-new-action forecast is no longer the right forecast.
If the proposed action belongs to another authority, the decision situation itself has been misstated.

| Adjustment within a formulation | Revision of the formulation |
|---|---|
| update weather or demand inputs | change the target, comparison, or horizon |
| replace an old trusted reading with a newer trusted reading | separate a record from the substantive target |
| refine a parameter while the model's role is unchanged | add an omitted behavioral response or revise the boundary |
| recompute consequences under the same alternatives | revise authority, alternatives, or evaluative premises |

The size of the numerical change does not decide which column applies.
A small discrepancy can force major reframing if it exposes the wrong target or observation process; a large update can remain ordinary adjustment if the formulation still fits the use.

### Rival formulations are useful before failure is obvious

Consider two ways to formulate the water problem.

**Formulation A**

> Forecast whether usable storage will fall below reserve under current operation.

**Formulation B**

> Decide whether the current physical state should be verified before committing to an operating action.

Neither is absurd.
If the dashboard is well verified and forecast uncertainty dominates, Formulation A may deserve priority.
If less than 1 ML of starting-state error can change the action and an independent check arrives in 25 minutes, Formulation B becomes more important.

The point is not to generate rivals for sport.
It is to keep a plausible alternative formulation available when the current framing depends heavily on an assumption that could fail.

Ask:

> **What observation, consequence, or decision condition would make me wish I had formulated this problem differently?**

That turns a hidden assumption into a possible revision trigger.

### The same object can need a different model

Return briefly to the pendulum.
The same physical object can be used to estimate local gravity, predict short-horizon position, or regulate a durable clock.
Intended use changes what the representation must preserve and what counts as adequate.
The object did not change; the question did.

That is why model criticism should not demand that every representation contain every feature of reality.
The better question is whether an omitted feature could matter for the stated use.
Chapters 2 and 5 develop that judgment more carefully.

### A faded case: one test, two uses

A school has a **20-item mathematics assessment** and one total score for each student.
Administrators propose using it to:

1. rank applicants for a limited advanced program;
2. diagnose which prerequisite skills current students need to review.

No psychometrics knowledge is required.
Before reading further, write a short response:

- State the intended use and a plausible target for each use.
- Name one reason the total score might not be identical to the target of interest.
- Give one consequence of treating the same analysis as automatically adequate for both uses.
- Give one observation that would make you revise the formulation.

Do not reconstruct the full Chapter 1 screen.
Use only what is needed.

A defensible comparison notices that the same **record** can support different inquiries.
Ranking may concern relative standing under a selection purpose; diagnosis concerns which skills require attention.
A total score may be relevant to both without carrying the same information for both.
Evidence that students with the same total score miss very different items would be enough to challenge a formulation that treats the total as an adequate answer to both questions.

If the score becomes consequential, another revision may eventually be needed because students or institutions may respond to the rule itself.
Chapter 1 only screens for that possibility.

### Different failures require different repairs

The examples suggest several reasons to go backward: intended-use failure, target failure, observation failure, evidence failure, alternative or authority failure, evaluation failure, and response failure.
These labels are reminders, not a checklist.
The practical point is that the repair must match the failure: if the record is wrong, more forecast data may not help; if an intervention effect is not established, polishing predictive accuracy does not answer the causal question; if authority is misstated, a more precise calculation does not make an infeasible action feasible; and if action changes behavior, a model fitted to the pre-action environment may need more than a parameter update.

### Know when to hand the problem forward

A strong first pass often ends by identifying the kind of expertise needed next.
Common routes can be grouped:

- **representation, measurement, and records** → Chapters 2–4;
- **assumptions, uncertainty, prediction, and inference** → Chapters 5–9;
- **values, alternatives, and choice** → Chapters 10–11;
- **optimization and feasibility** → Chapter 12;
- **dynamics, sequential decisions, feedback, and information** → Chapters 13–14;
- **incentives, gaming, and strategic response** → Chapter 15.

Routing is not an admission that the first pass failed.
It is one of the outputs of a successful first pass.

The purpose of Chapter 1 is not to solve every specialist problem before it appears.
It is to recognize what kind of problem has appeared, what the current reasoning can support, and when continuing with the same formulation would create false confidence.

A strong first pass is therefore valuable partly because it can tell you:

> **This is no longer the problem I thought I was solving.**

The final section removes most of the scaffolding.

## 6. Cold-Start Practice and Retrieval

The worked case is over.
The scaffolding now has to disappear.

The goal is not to prove that four hours of instruction have produced durable expertise.
It is to obtain initial evidence about whether you can reconstruct the reasoning without being led through every step.

You will diagnose a flawed analysis, attempt one unfamiliar case without the checklist or rubric in view, inspect feedback only after production, compare your work with the opening baseline, retrieve the navigation from memory, and reserve the second unfamiliar form for a delayed retest.

### Activity 1 — Diagnose and repair a flawed analysis

Read the following deliberately poor response to the water case.

> The problem is a water shortage, so the main task is to forecast demand. The dashboard says current storage is 10.8 ML, so that is the current physical storage level. Historical hot-weather records predict high demand, and previous conservation requests were followed by lower demand, so issuing a conservation request will reduce demand in this event. The available choices are to pump more or impose a mandatory restriction. Because reserve crossing is dangerous, the data show that the Utility Director should impose the restriction, and that recommendation is the decision. There is no need to discuss values or stakeholders because the safer option is obvious. Once the action is chosen, the remaining stages can be completed in order; the forecast does not need to be reconsidered after deployment.

Identify at least **six consequential failures**.
For each one, write:

1. **Diagnosis:** What is wrong?
2. **Consequence:** What claim, decision, or adequacy judgment becomes unreliable because of it?
3. **Repair:** What should be changed?

Then answer:

> Which failure should be repaired first, and why?

Do not score yourself by the number of labels you can name.
Several errors interact.
The important skill is recognizing which repair changes the rest of the reasoning.

**Stop here until you have completed the diagnosis.**
Then open [`diagnosis-feedback.md`](diagnosis-feedback.md) and compare your reasoning before continuing.

### Activity 2 — Cold transfer without the checklist

Now work on one unfamiliar case.

The parallel forms are delivered separately:

- [**Form A — Refrigerated warehouse cooling risk**](transfer-form-a.md)
- [**Form B — Emergency temporary-housing allocation after a flood**](transfer-form-b.md)

For self-study, choose the domain that is **less familiar** from the titles alone.
Open only that form.
**Do not preview the other form.**
It is reserved for the delayed retest.

Do not consult the Chapter 1 map, worked water solution, or scoring rubric until you have finished a one-page first-pass analysis.
The current pilot target is **30–40 minutes**; that is an operational design target, not a universal standard.

State only assumptions that are needed.
Do not invent missing domain facts; if an important fact is absent, identify it and explain whether learning it could change the decision.
The selected form supplies the domain facts needed for the reasoning task.

**Finish the one-page analysis before opening the rubric.**
Then use [`transfer-rubric.md`](transfer-rubric.md) for dimension-level feedback and the post-task self-explanation prompt.

### Return to your five-minute opening attempt

Retrieve the response you wrote at the beginning of the chapter.
Do not ask whether the later answer simply contains more terminology.
Ask whether the structure changed.

Compare the two responses:

1. Did you state the intended use more clearly?
2. Did you separate the target from its records or proxies?
3. Did you separate consequence claims from the recommendation or decision?
4. Did you identify a reason the analysis might have to move backward?

Then answer the stronger question:

> **What did you fail to represent at the beginning that you now consider decision-relevant?**

Write one sentence naming the most important change in your default framing.

### Retrieve the navigation from memory

Close or cover the chapter map.
From memory, reconstruct the five-part navigation used in the worked case and add arrows showing at least two ways later evidence can send reasoning backward.

Also reconstruct these relationships in your own words:

- intended use versus target;
- evidence versus claim type;
- consequence claims versus evaluative premises;
- action versus feedback or response;
- monitoring versus revision and routing.

Only after you have finished should you compare your reconstruction with the chapter's navigation:

**Frame and formulate → Learn from evidence → Choose → Act in responsive systems → Integrate and revise**

The arrows are not one-way.
A measurement problem can send you back to the target or observation process.
Deployment can change the process and send you back to the forecast, representation, evidence requirements, alternatives, or decision.

Repair what you omitted.
Then choose one omission and explain why it mattered in the water case.

### Delayed retest

Do not use or preview the second transfer form immediately.

For self-study, schedule the form you did **not** use today for approximately **7–14 days** from now.
The interval is a pilot window, not a universal spacing optimum.

At the retest:

- do not reread Chapter 1 first;
- do not display the checklist or rubric while producing the response;
- open the previously unseen parallel form;
- use the same one-page first-pass task;
- consult the same eight rubric dimensions only after production;
- compare dimension-level performance with the first transfer attempt.

The purpose is not to prove far transfer from one delayed exercise.
It is to test whether the reasoning structure can be produced again after the immediate scaffolding and narrative details have faded.

A successful Chapter 1 outcome is modest but important:

> **You can begin an unfamiliar consequential problem by making the use, target, claim, evidence limits, alternatives, consequences, environment, and revision conditions explicit—without pretending that this first pass is the finished analysis.**

The rest of the book develops the machinery needed to answer the questions this first pass has learned to ask.
