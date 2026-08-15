# Chapter 1 Cold-Transfer Forms

Status: selected for pilot; not yet empirically calibrated

These are parallel unfamiliar-domain production forms for Chapter 1. They are design artifacts, not claims of validated measurement. Both forms use the same output requirements and self-scoring rubric in `spec.md`.

## Common instructions

Without consulting the Chapter 1 checklist or rubric, produce a one-page first-pass analysis. State only assumptions that are needed. Do not invent domain facts that the prompt does not provide; instead identify missing information and explain whether it could change the decision.

Your analysis must include:

1. intended use and decision-maker;
2. affected stakeholders and candidate actions;
3. a qualified target and relevant context;
4. layered positive/normative and claim-type classification;
5. a preliminary distinction among target system, model, and observed records;
6. the most important evidence limitation;
7. relevant values, consequences, and constraints;
8. time, feedback, or adaptive-agent screening;
9. one rival formulation;
10. one likely revision trigger;
11. justified routing to later chapters or specialist expertise.

The forms intentionally contain more than one legitimate analytical subquestion. Do not force the whole problem into a single label.

---

## Form A — Refrigerated warehouse cooling risk

### Situation

A regional food distributor operates one refrigerated room containing products that the case specifies must remain between **1°C and 5°C** until dispatch tomorrow afternoon. The room normally uses two cooling units. Unit A is operating. Unit B has generated an intermittent fault alarm. Outdoor temperature is expected to remain unusually high for the next 20 hours.

The control dashboard currently reports **3.8°C** from the room sensor. A handheld thermometer placed near the loading door reads **4.6°C**, but the prompt states that this handheld reading is only a spot measurement and may not represent the entire room. Product-core temperatures have not yet been checked. The last three hours show a gradual rise in the dashboard reading.

The operations manager must decide within 20 minutes whether to continue current operation, send a technician to verify Unit B and the sensors, reduce door openings and loading activity, move the most temperature-sensitive product to another room with limited spare capacity, start an available backup cooling unit that has a stated energy and maintenance cost, or combine actions.

### Supplied facts

- The case treats 1–5°C as the relevant safe operating band; no external food-safety knowledge is required.
- The backup unit can be started immediately, but its effect on room temperature is uncertain because it has not been used in comparable extreme heat.
- Historical records show that higher outdoor temperature and frequent door opening are associated with higher room temperature. They do not by themselves establish the causal effect of starting the backup unit.
- The fixed room sensor was last calibrated six months ago. A sensor or telemetry fault is possible but not known.
- A technician can produce an independent sensor check in 25 minutes. Product-core measurements require 15 minutes and cover only a sample of products.
- Moving product reduces exposure in this room but uses scarce capacity elsewhere and creates handling cost.
- Reducing loading activity delays some dispatch work.
- Product temperature has thermal inertia: a short-lived air-temperature excursion does not imply immediate product-core failure, and a normal air reading does not guarantee every product is within range.
- No strategic external actor is assumed. Staff may change door-opening behavior after an instruction, but the environment is otherwise mainly physical.

### What makes the formulation nontrivial

Possible targets include the true current thermal state, whether product temperature will leave the specified band by dispatch time, the effect of starting backup cooling, and which action should be taken. These are related but not identical questions.

A strong answer should notice that the dashboard value is not identical to the target physical state and that predictive association with outdoor temperature or door openings does not establish the effect of manipulating those variables or starting backup cooling.

### Candidate revision triggers

Examples include an independent sensor check that materially disagrees with the dashboard, product-core measurements that reverse the apparent urgency, or a technician finding that Unit B is operating normally despite the alarm.

---

## Form B — Emergency temporary-housing allocation after a flood

### Situation

A local emergency-management office has **80 temporary-housing vouchers** available for the next two weeks after a flood. The office has received **260 applications**, while field teams estimate that additional displaced households have not yet applied. The prompt states that no external housing law or disaster-program rule is needed; all relevant rules are given here.

The office must decide how to allocate the first 80 vouchers and whether to reserve some vouchers while additional information is collected.

The administrative file contains household size, current reported sleeping arrangement, neighborhood, whether a dwelling has passed a rapid habitability inspection, self-reported health or mobility needs, contactability, and prior program records. Some fields are missing. Applicants with poor internet access are underrepresented in online applications.

A risk score developed after earlier floods predicts which **observed applicants** remained without stable temporary housing for at least seven days. The score has not been evaluated as a rule for allocating vouchers, and the prompt supplies no evidence that giving a voucher to a high-score household produces a larger benefit than giving one to another household.

### Supplied facts

- All 260 current applicants satisfy the minimal eligibility rule stated by the case.
- The office's stated immediate purpose is to reduce severe short-term housing instability while avoiding systematic exclusion of households that are poorly represented in the application data.
- Field outreach can identify additional households, but doing so delays final allocation of any reserved vouchers by up to one day.
- Some landlords may stop accepting vouchers if administrative delay becomes too long.
- Publishing a simple priority rule may change application behavior and the documentation people submit.
- A voucher can help only if an accepting housing provider is available; provider availability varies across neighborhoods.
- The historical risk score is predictive, not evidence by itself of the causal effect of receiving a voucher.
- The case does not stipulate one ethically correct allocation rule. The learner must make material evaluative premises visible rather than hide them inside a score.
- Candidate actions include immediate allocation by a stated rule, reserving a fraction for outreach-discovered households, gathering targeted information before ranking, using categories rather than a single score, or combining these actions.

### What makes the formulation nontrivial

Possible targets include predicting who will remain unstably housed, estimating who can actually use an available voucher, evaluating the consequences of different allocation rules, and deciding what allocation procedure should be used. The target population is not automatically identical to the observed applicant file.

A strong answer should distinguish prediction from intervention, observed applicants from all materially affected households, and positive claims about expected consequences from normative premises about urgency, equity, acceptable error, and procedural burden.

### Candidate revision triggers

Examples include field outreach revealing a large underrepresented group, evidence that voucher acceptance differs sharply by neighborhood, or publication of the rule changing application/documentation behavior enough that the original prediction model no longer applies in the same way.

---

## Parallel-form calibration requirements

Before Chapter 1 is frozen:

- test both forms with representative readers;
- counterbalance which form appears first;
- compare completion time and dimension-level rubric patterns rather than assuming a single aggregate score is meaningful;
- check whether domain familiarity predicts performance after controlling informally for general reasoning competence;
- revise prompt length or supplied facts if one form requires materially more hidden knowledge;
- retain no numerical pass/fail cut score unless pilot evidence supports one.
