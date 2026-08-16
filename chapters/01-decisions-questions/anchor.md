# Chapter 1 Primary Anchor Case

Status: drafting freeze; governed by `../../decisions/0004-chapter1-primary-anchor-case.md`, with decision-framing and dynamics boundaries governed by Decisions 0006 and 0007.

## Municipal water-supply shortage during a heatwave

The primary worked case is a synthetic small municipal utility entering a seven-day hot, dry period in which usable finished-water storage may fall below a case-specific operating reserve.

The reader does not need water-engineering expertise. Every operational, governance, and numerical fact needed for the reasoning task is supplied explicitly. The numerical values are synthetic and are not presented as industry averages or regulatory standards.

A human drinking-water utility / engineering realism review remains required before Chapter 1 is declared verified or frozen for publication. That review does not block first-draft writing.

## Frozen decision situation

At 08:00 on Monday:

- usable finished-water storage capacity is **14.0 ML**;
- the fictional utility's event-specific operating-reserve threshold is **4.5 ML**;
- the dashboard reports **10.8 ML** usable storage;
- normal treated-water input is **8.4 ML/day**;
- a seven-day no-new-action demand forecast totals **64.9 ML**.

The immediate decision-maker is the **Utility Director**.

The director must decide whether to:

- continue current operation;
- obtain an independent storage-level verification;
- increase treated-water production within the supplied temporary operating limit;
- issue a voluntary conservation request;
- combine verification, production increase, conservation, and monitoring;
- request authorization for a mandatory restriction if later evidence warrants escalation.

The decision remains distinct from the informational targets used to support it.

Possible analytical targets include:

- forecast demand over the relevant horizon;
- determine whether usable stored water will fall below the specified reserve;
- verify the current physical storage level rather than relying only on a dashboard value;
- estimate how a conservation action or production change would affect shortage risk;
- compare candidate actions and their material consequences.

## Frozen authority facts

These are fictional institutional rules supplied by the case.

The Utility Director may directly authorize:

- an independent field verification of storage level;
- treated-water production up to **8.8 ML/day**;
- a voluntary public conservation request;
- enhanced monitoring and more frequent review.

The Utility Director may **not** directly authorize a mandatory water-use restriction.

A mandatory restriction requires approval by the **City Manager** under the fictional drought-response plan. If requested, the earliest such restriction could take effect is **six hours after the request**.

The case uses this distinction to teach that an attractive action is not automatically an action the named decision-maker can directly choose.

## Frozen physical and operational facts

### Storage and reserve

- Usable capacity: **14.0 ML**
- Case-specific operating reserve: **4.5 ML**
- Dashboard level at 08:00: **10.8 ML**

The 4.5 ML reserve is a fictional internal rule for the case, not a universal engineering or regulatory threshold.

### Normal and increased production

Normal treated-water input is **8.4 ML/day**.

The director can authorize a temporary increase to **8.8 ML/day**, subject to these supplied case facts:

- the increase has a **six-hour action/physical delay** before the additional production is available;
- once online, 8.8 ML/day can be sustained through the seven-day horizon;
- incremental operating cost is **$2,000 per 24 hours** at the higher output;
- production above 8.8 ML/day is unavailable during this event because of supplied treatment and pumping constraints.

The cost and operating limit are synthetic.

## Frozen no-new-action demand forecast

The forecast represents expected demand **if no new conservation request or restriction is introduced**.

| Day | Forecast high | Forecast demand with no new action |
|---:|---:|---:|
| 1 | 36°C | 9.0 ML |
| 2 | 38°C | 9.3 ML |
| 3 | 40°C | 9.6 ML |
| 4 | 40°C | 9.5 ML |
| 5 | 39°C | 9.4 ML |
| 6 | 37°C | 9.2 ML |
| 7 | 35°C | 8.9 ML |
| **Total** |  | **64.9 ML** |

These are synthetic central forecasts, not calibrated probabilistic intervals.

For qualitative sensitivity, the case may stress demand by **+0.4 ML/day** across the horizon. That value is a supplied planning stress, not a statistical confidence or prediction interval.

## Simple balance used in Chapter 1

The only required arithmetic is:

`ending storage = starting storage + treated-water input - demand`

No differential equations or formal stock-flow notation are required.

Seven-day baseline input is:

`8.4 × 7 = 58.8 ML`

Using the dashboard value:

`10.8 + 58.8 - 64.9 = 4.7 ML`

The dashboard-based first pass therefore projects **4.7 ML**, slightly above the 4.5 ML reserve.

This is intentionally marginal rather than comfortably safe.

## Required backward revision 1 — observation / measurement

An independent local pressure-based level check is available and does not use the same remote level transmitter as the dashboard.

The check:

- takes **25 minutes**;
- indicates **9.9 ML** usable storage;
- is followed by a supplied finding that the remote level transmitter is reading high because of calibration drift.

The reader is not required to diagnose sensor physics.

Using the verified physical level:

`9.9 + 58.8 - 64.9 = 3.8 ML`

The same forecast and operating plan now project **3.8 ML**, below the 4.5 ML reserve.

This revision teaches:

- physical storage is not identical to its dashboard record;
- information gathering can be a genuine action alternative when it can change the decision in time;
- the target did not change, but the belief about the current physical state did.

## Production-increase scenario

With a six-hour delay before the increase takes effect:

`8.4 × 0.25 + 8.8 × 6.75 = 61.5 ML`

Using the verified 9.9 ML start:

`9.9 + 61.5 - 64.9 = 6.5 ML`

So increased production alone projects **6.5 ML** under the central no-new-action forecast.

Under the supplied `+0.4 ML/day` demand stress:

`9.9 + 61.5 - 67.7 = 3.7 ML`

The production increase therefore improves the central projection but does not make the decision trivial under the supplied stress.

## Frozen conservation evidence

The utility may issue a voluntary conservation request asking households and businesses to reduce nonessential water use.

The case supplies these facts:

- past voluntary requests were often followed by lower observed demand;
- those requests occurred under different weather and operating conditions and were sometimes accompanied by other utility actions;
- those historical records do **not** by themselves isolate the causal effect of the request;
- the current demand forecast is explicitly a no-new-action forecast.

Do not assign a universal percentage reduction to conservation.

Do not treat historical association or post-action change as sufficient evidence of an intervention effect.

## Required backward revision 2 — deployment changes the process

A defensible staged action in the worked narrative may combine:

- independent verification;
- temporary production increase;
- voluntary conservation request;
- monitoring;
- escalation if the updated projection again falls below reserve.

After the conservation request is deployed, the case supplies:

- next 24-hour demand is **8.6 ML**, compared with the pre-action forecast of **9.0 ML** for that period;
- several monitored large users report reducing nonessential use in response to the request.

The chapter must **not** infer that 0.4 ML is the causal effect of the request from this single comparison.

The required lesson is:

> The action has become part of the process producing future demand. A forecast explicitly conditioned on no new conservation action is no longer the right forecast for the post-action system.

The model, assumptions, or monitoring plan must therefore be revised.

This is a **structural/process revision**, not merely a numerical parameter update.

## Repeated-decision structure

The decision is not a one-shot commitment for the full heatwave.

Use this supplied cadence:

- **Initial decision:** 08:00–08:30 Monday.
- **First review:** after the 25-minute independent level verification.
- **Second review:** approximately 24 hours after action, using verified storage, actual demand, production status, observed response, and an updated projection.
- **Escalation trigger:** if the updated projection again places usable storage below the **4.5 ML case-specific reserve**, reconsider the action set, including a request to the City Manager for mandatory restriction authority.

No control-policy mathematics is required.

## Consequences and evaluative premises

### Consequences evidence can inform

- projected ending or minimum usable storage;
- risk of crossing the case-specific reserve;
- incremental operating cost;
- timing of information and action;
- observed demand response;
- burdens created by conservation or restriction.

### Stakeholders

At minimum:

- households;
- local businesses;
- essential community services;
- utility operators and staff;
- municipal budget / governing authority.

### Evaluative bridge

A worked recommendation should make material premises visible, for example:

- crossing the reserve is undesirable;
- continuity of service and operating margin matter;
- unnecessary operating cost matters;
- unnecessary restrictions and burdens matter;
- a voluntary request is less burdensome than a mandatory restriction;
- additional information is worthwhile when it can arrive soon enough to change action.

These are evaluative or decision premises, not empirical findings extracted from the forecast.

## Recommended worked-case path

The chapter should not imply that a formal optimizer produces the unique correct answer.

A defensible first-pass path is:

1. do not treat the 10.8 ML dashboard record as the physical state without considering provenance;
2. obtain the 25-minute independent verification because the action is sensitive to starting storage;
3. after 9.9 ML is verified, recognize that current operation projects reserve breach under the central forecast;
4. authorize the 8.8 ML/day temporary production increase while noting its delay and cost;
5. issue a voluntary conservation request if the stated evaluative premises support the additional margin relative to the burden;
6. monitor storage and demand rather than treating the pre-action forecast as fixed;
7. recompute after approximately 24 hours;
8. if the updated projection again falls below 4.5 ML, consider escalation, including requesting mandatory-restriction authority.

This is a defensible staged recommendation, not a theorem that it is the unique correct policy.

## Reveal order for the worked example

Do not give every fact at the opening.

### Opening
Reveal:

- seven-day hot, dry period;
- dashboard 10.8 ML;
- reserve 4.5 ML;
- current input 8.4 ML/day;
- forecast table;
- decision-maker and broad candidate actions.

### Intended-use / target stage
Reveal:

- decision authority;
- consequences of false reassurance and false alarm;
- physical-storage target versus dashboard record.

### Evidence / observation stage
Reveal:

- independent check exists;
- it takes 25 minutes;
- verified storage is 9.9 ML;
- remote transmitter is biased high.

This triggers Revision 1.

### Choose stage
Reveal:

- temporary 8.8 ML/day production;
- six-hour delay;
- $2,000/day incremental cost;
- voluntary request is within director authority;
- mandatory restriction requires City Manager approval.

### Responsive-systems stage
Reveal:

- no-action forecast assumed no new conservation intervention;
- post-request demand is 8.6 ML versus 9.0 ML forecast;
- some large users report behavioral response.

This triggers Revision 2.

## Why this case carries the Chapter 1 loop

- **Purpose and target:** forecasting, state verification, intervention evaluation, and decision support remain distinct.
- **Representation:** stored water alone may omit additions, removals, constraints, observation process, timing, and behavioral response.
- **Measurement and observation:** physical storage differs from dashboard records.
- **Evidence:** predictive historical patterns do not by themselves establish intervention effects.
- **Values and choice:** consequences must be evaluated, and recommendation remains distinct from decision.
- **Authority and alternatives:** actions can be combined, staged, or require escalation.
- **Dynamics:** storage carries over through time; the case contains an information delay, a physical/action delay, and repeated review.
- **Adaptive response:** conservation changes behavior and therefore the post-deployment process.
- **Monitoring and revision:** later observations send the analysis backward to measurement, forecast assumptions, representation, or action.

## Source and realism discipline

All numerical values and governance rules in this case are synthetic.

The case design has been checked against authoritative water-utility guidance for the limited plausibility of:

- supply/demand drought response;
- SCADA/telemetry versus independent level evidence;
- conservation requiring forecast revision;
- utility-specific governance and restriction procedures.

These checks support the **type of mechanism**, not the numerical values.

Before Chapter 1 is declared verified or frozen for publication, obtain a human drinking-water utility / engineering review focused on operational wording and hidden assumptions.

The manuscript must not present any synthetic threshold, flow, delay, cost, response, or governance rule as an industry norm.

## Recurrence

Possible later homes include Chapters 2, 4, 6–7, 11–15, and 17.

Recurrence is optional and should occur only when a later chapter adds a genuinely new operation.

The former hospital-pharmacy case is retired as the Chapter 1 anchor and has no recurrence obligation.
