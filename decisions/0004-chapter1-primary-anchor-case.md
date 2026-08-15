# Decision 0004: Chapter 1 Primary Anchor Case

## Status

Accepted (2026-08-15)

## Decision

Chapter 1 uses a **municipal water-supply shortage during a heatwave** as its primary worked anchor case.

The former hospital-pharmacy stockout case is retired as the Chapter 1 anchor and carries no recurrence obligation.

The anchor is a synthetic small-municipal-utility decision situation: during a hot, dry week, usable stored water may fall below a minimum operating reserve specified by the case within seven days. The decision-maker must consider actions such as changing pumping, issuing a conservation request or restriction, gathering more information, or combining actions.

This decision governs the Chapter 1 anchor wherever older working material still names the hospital-pharmacy case. Such references are stale and must be synchronized before Chapter 1 drafting is treated as stable.

## Why

The water-supply case is a better Chapter 1 teaching anchor because it can carry the complete reasoning loop while requiring less hidden specialist knowledge.

- Storage, inflow, demand, and pumping form an intuitive stock-flow situation.
- Physical stored water can be distinguished cleanly from sensor, telemetry, and dashboard records.
- Demand forecasting can be separated from claims about the effect of conservation or pumping changes.
- Consequences and trade-offs are consequential without requiring clinical knowledge.
- Time, delay, repeated decisions, feedback, and monitoring arise naturally.
- Residents, businesses, and operators can respond after alerts, requests, restrictions, or operating changes, making adaptation visible.
- The case can support later recurrence across representation, observation, prediction, causal reasoning, decisions, dynamics, control, strategic response, and monitoring without forcing recurrence.

## Required Chapter 1 revision behavior

The worked example must still show at least two materially different backward revisions:

1. **Measurement/observation revision:** dashboard storage and a verified physical level diverge because telemetry is delayed or a level sensor is miscalibrated.
2. **Responsive-system revision:** a conservation action changes water-use behavior enough that a forecast assuming unchanged demand is no longer adequate.

The number two remains a worked-example design requirement, not a general rule for competent reasoning.

## Case constraints

- All numerical data are synthetic unless provenance and permissions are explicit.
- Every utility-specific operating fact needed for reasoning must be supplied in the case.
- Claims about water-utility operations, metering, pumping or treatment constraints, reserve practice, or demand response require authoritative sourcing or domain review.
- The simple mathematical preview may use a storage balance; detailed representation belongs to Chapter 2 and formal dynamics to Chapter 13.

## Architecture preserved

This decision does not change the Chapter 1 title, central question, core competence, six-section structure, 24-page / 4-hour budget, pendulum contrast, student-assessment contrast, exercise progression, transfer target, or the book architecture.

## Reopen only if

- Pilot readers require hidden water-engineering knowledge despite all necessary case facts being supplied.
- Domain review shows that a realistic version cannot remain simple enough for Chapter 1.
- Another anchor demonstrably carries the same cross-book reasoning functions with materially lower cognitive or sourcing burden.

Ordinary prose or case-detail revision is not a reopening condition.
