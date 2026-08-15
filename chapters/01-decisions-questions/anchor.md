# Chapter 1 Primary Anchor Case

Status: governed by `../../decisions/0004-chapter1-primary-anchor-case.md`

## Municipal water-supply shortage during a heatwave

The primary worked case is a synthetic but operationally realistic decision for a small municipal water utility facing a hot, dry week in which usable stored water may fall below a minimum operating reserve specified in the case within seven days.

The reader does not need water-engineering expertise. Every operational fact needed to reason about the case must be supplied explicitly.

## Decision situation

The decision-maker must decide whether to change pumping, issue a conservation request or restriction, gather additional information, combine actions, or retain current operation.

The decision must remain distinct from the informational targets used to support it.

Possible analytical targets include:

- forecast demand over the relevant horizon;
- determine whether usable stored water will fall below the specified reserve;
- verify the current physical storage level rather than relying only on a dashboard value;
- estimate how a conservation action or pumping change would affect shortage risk;
- compare candidate actions and the consequences they create.

## Why this case carries the Chapter 1 loop

- **Purpose and target:** demand forecasting, storage verification, operational decision support, and intervention evaluation are different inquiries.
- **Representation:** stored water alone may omit inflow, pumping or treatment limits, leakage, distribution demand, and timing.
- **Measurement and observation:** physical storage can differ from dashboard readings because of calibration error, telemetry delay, aggregation, or missing readings.
- **Evidence:** historical weather and demand can support prediction without by themselves identifying the effect of a new conservation or pumping policy.
- **Values and choice:** continuity of service, operating and energy cost, burden on households and businesses, equity, reserve margin, and restrictions on nonessential use create competing consequences.
- **Dynamics:** storage, inflow, demand, pumping, leakage, and repeated operating decisions evolve through time.
- **Adaptive response:** residents, businesses, and operators may change behavior after alerts, conservation requests, restrictions, or operating targets are deployed.
- **Monitoring and revision:** verified level checks, telemetry discrepancies, pressure or demand patterns, and decision outcomes can send the analysis back to measurement, representation, evidence, or objectives.

## Required backward revisions

The worked case must visibly demonstrate at least these two different revision modes:

1. dashboard storage and a verified physical level diverge because telemetry is delayed or a level sensor is miscalibrated;
2. a conservation action changes water-use behavior enough that a forecast assuming unchanged demand is no longer adequate.

These two revisions are a worked-example design requirement, not a universal rule.

## Source discipline

All case numbers should be synthetic unless provenance and permissions are explicit. Water-utility operating claims must be checked against authoritative water-utility, water-resources, metering, and infrastructure sources or domain review. Any pumping limit, treatment capacity, reserve threshold, sensor characteristic, or response assumption used by the reader must be supplied in the case rather than assumed as background knowledge.

## Recurrence

Possible later homes include Chapters 2, 4, 6–7, 11–15, and 17. Recurrence is optional and should occur only when a later chapter adds a genuinely new operation.

The former hospital-pharmacy case is retired as the Chapter 1 anchor and has no recurrence obligation.
