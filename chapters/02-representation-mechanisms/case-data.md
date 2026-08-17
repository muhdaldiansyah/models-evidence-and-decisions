# Chapter 2 Water-Network Case Data

Status: drafting freeze. Extension of `../01-decisions-questions/case-data.md`, which remains authoritative for every value it contains.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or empirical values from any real utility.

## Relationship to Chapter 1

Chapter 2 does not change a single Chapter 1 value. It **decomposes** them.

| Chapter 1 aggregate | Chapter 2 decomposition | Check |
|---|---|---|
| Usable storage capacity 14.0 ML | Main reservoir 12.8 ML + Hillcrest tank 1.2 ML | 12.8 + 1.2 = 14.0 |
| Verified usable storage 9.9 ML at 08:25 | Main reservoir 9.3 ML + Hillcrest tank 0.6 ML | 9.3 + 0.6 = 9.9 |
| Day-1 forecast demand 9.0 ML | Lowfield 5.4 + Millbrook 2.7 + Hillcrest 0.9 | 5.4 + 2.7 + 0.9 = 9.0 |

Every Chapter 1 arithmetic check remains valid. This is the point: the same numbers, differently represented.

## Network facts

The town is served in three pressure zones by elevation.

| Zone | Elevation band | Supply path | Share of demand | Day-1 demand |
|---|---|---|---:|---:|
| Lowfield | lowest | gravity from main reservoir | 60% | 5.4 ML |
| Millbrook | middle | gravity from main reservoir | 30% | 2.7 ML |
| Hillcrest | highest | **pumped** from main reservoir to a hilltop tank | 10% | 0.9 ML |

| Item | Frozen value | Authoring role |
|---|---:|---|
| Hillcrest tank usable capacity | 1.2 ML | Zone-level storage limit |
| Hillcrest tank contents at 08:25 | 0.6 ML | Zone-level state |
| Hillcrest pump station | 1 duty pump + 1 standby | Exposes a single represented part |
| Duty pump capacity | 1.1 ML/day | Exceeds zone demand; refills the tank |
| Standby pump availability | case-stipulated: under maintenance, unavailable for 3 days | Makes the failure mode live |
| Emergency interconnection with neighbouring system | 1.5 ML/day maximum | Boundary question |
| Mutual-aid activation time | 12 hours | Boundary question |
| Zone-level reserve in the drought plan | **none exists** | See "The plan's own representation" below |

## The aggregation demonstration

This is the chapter's load-bearing arithmetic. The reader must produce it, not read it.

### Aggregate view — the Chapter 1 representation

Stored 9.9 ML. Day-1 demand 9.0 ML. Input 8.4 ML/day.

`9.9 + 8.4 - 9.0 = 9.3 ML` at the end of day 1.

Net drawdown is 0.6 ML/day. Against the 4.5 ML reserve, that is roughly nine days away. **Nothing about tomorrow looks urgent.**

### Zone view — with the duty pump out of service

Hillcrest holds 0.6 ML and draws 0.9 ML/day. With no pump, nothing refills it.

`0.6 ÷ 0.9 = 0.67 days ≈ 16 hours`

**Hillcrest loses supply in about sixteen hours while total system storage is still above 9 ML.**

### What this shows

The single-tank representation is not *wrong*. Its arithmetic is correct and it answered Chapter 1's question well. It simply **cannot express** the question "who loses service first?", because it contains no zones. Adequacy flipped when the purpose changed.

## The targeting demonstration

A uniform request that every customer reduce use by 10%:

- system-wide saving: `9.0 × 0.10 = 0.9 ML/day`
- saving in Hillcrest: `0.9 × 0.10 = 0.09 ML/day`

Hillcrest's shortfall with no pump is 0.9 ML/day. A 0.09 ML/day saving does not address it.

The aggregate representation cannot even pose the targeting question, because it has one demand number.

## Candidate mechanism for the phenomenon "Hillcrest loses pressure first"

Supplied so that readers draw and hedge a mechanism, **not** so that they conclude one is true.

**Mechanism A — pump capacity.** Hot weather raises demand → zone draw exceeds pump refill rate → hilltop tank depletes → pressure falls.

**Mechanism B — distribution main.** The case supplies that Hillcrest's feeder main is the oldest in the system. Higher flow → larger friction loss along an undersized main → pressure at the top of the zone falls before the tank is empty.

Both are drawable from supplied facts. Both could produce the phenomenon. **Neither is established by being drawn.**

Case-supplied test: running the duty pump at elevated output for one hot afternoon and recording zone pressure would produce evidence bearing on A. The case does **not** supply the result of that test.

## Abstraction and idealization in this case

- **Abstraction (omission):** each zone is represented as one demand quantity. Individual properties, meters, and households are left out. The representation is silent about them; it asserts nothing false about them.
- **Idealization (distortion):** treating transfer from the main reservoir to the Hillcrest tank as instantaneous and lossless. This is known to be false — there is a pump start-up period and friction loss — and it is asserted rather than omitted.

## State in this case

Under the zone representation, the state is the stored volume in **each** tank.

Deliberate non-examples for the state test:

- **today's forecast high temperature** — acted on from outside, not carried forward;
- **current pump flow rate** — recomputable from the pump setting;
- **total system storage** — recomputable by adding the two tank volumes.

The last is the instructive one. Total system storage **was** the state in Chapter 1's representation and is **not** state in the zone representation. Role follows the representation, not the world.

## The plan's own representation

The drought plan supplies a 4.5 ML system-wide operating reserve and **no zone-level trigger**.

That is not an oversight to be scored against the fictional utility. It is what happens when a plan is written against a single-tank representation: the plan can only contain triggers the representation can express.

This is the chapter's strongest illustration that representation choice has consequences beyond analysis. Present it as a consequence of representation, never as negligence.

## Prohibited interpretations

Do not write or imply that:

- any of these values are typical, standard, or recommended;
- three pressure zones, a 10% hilltop demand share, or a single duty pump is a normal configuration;
- 16 hours is a general rule for hilltop tank endurance;
- Mechanism A or Mechanism B is the established cause of anything;
- pressure loss means water is unsafe, or that any specific health consequence follows;
- a real utility may operate without standby capacity, or that leaving a standby pump unavailable for three days is acceptable practice;
- the absence of a zone-level reserve reflects real drought-planning practice;
- an emergency interconnection can be activated without the applicable agreements, permits, and water-quality requirements;
- targeted restriction of one zone is legally or operationally straightforward.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility or distribution-engineering SME should review this network extension for plausibility and accidental unsafe implications, alongside the Chapter 1 anchor. The SME is not asked to validate these synthetic values as industry averages.

**These facts inherit Chapter 1's open Gate 1.** Chapter 2's extension cannot be more validated than the case it extends. If SME review changes the Chapter 1 operating story, this file must be rechecked against it.
