# Chapter 1 — Section 6 Draft

## 6. Cold-Start Practice and Retrieval

The worked case is over. The scaffolding now has to disappear.

The goal of this section is not to prove that four hours of instruction have produced durable expertise. It is to obtain a first piece of evidence about whether you can reconstruct the reasoning without being led through every step.

You will do four things:

1. diagnose a flawed analysis;
2. produce a first-pass analysis in an unfamiliar domain without the Chapter 1 checklist or rubric in view;
3. compare your response with the diagnostic rubric and explain one important revision;
4. reconstruct the chapter's navigation from memory and schedule a delayed retest.

### Activity 1 — Diagnose and repair a flawed analysis

Read the following deliberately poor response to the water case.

> The problem is a water shortage, so the main task is to forecast demand. The dashboard says current storage is 10.8 ML, so that is the current physical storage level. Historical hot-weather records predict high demand, and previous conservation requests were followed by lower demand, so issuing a conservation request will reduce demand in this event. The available choices are to pump more or impose a mandatory restriction. Because reserve crossing is dangerous, the data show that the Utility Director should impose the restriction, and that recommendation is the decision. There is no need to discuss values or stakeholders because the safer option is obvious. Once the action is chosen, the remaining stages can be completed in order; the forecast does not need to be reconsidered after deployment.

Identify at least **six consequential failures**.

For each one, write:

1. **Diagnosis:** What is wrong?
2. **Consequence:** What claim, decision, or adequacy judgment becomes unreliable because of it?
3. **Repair:** What should be changed?

Then answer one more question:

> Which failure should be repaired first, and why?

Do not score yourself by the number of labels you can name. Several errors interact. The important skill is recognizing which repair changes the rest of the reasoning.

A strong diagnosis should be able to notice failures such as a topic substituted for an intended use, a dashboard record treated as the target state, predictive or associational evidence treated as an intervention effect, a false binary in the alternatives, ignored decision authority, hidden evaluative premises, a recommendation treated as the decision, and a responsive system treated as a passive one-shot problem.

### Activity 2 — Cold transfer without the checklist

Now work on one unfamiliar case.

For self-study, choose the domain that is **less familiar** to you. Do not consult the Chapter 1 map, the worked water solution, or the scoring rubric until you have finished a one-page first-pass analysis.

The current pilot target is **30–40 minutes**. That is an operational design target, not a universal standard.

Your task is to produce a defensible first pass. State only assumptions that are needed. Do not invent missing domain facts; if an important fact is absent, identify it and explain whether learning it could change the decision.

#### Form A — Refrigerated warehouse cooling risk

A regional food distributor operates one refrigerated room containing products that this exercise specifies must remain between **1°C and 5°C** until dispatch tomorrow afternoon. The room normally uses two cooling units. Unit A is operating. Unit B has generated an intermittent fault alarm. Outdoor temperature is expected to remain unusually high for the next **20 hours**.

The control dashboard reports **3.8°C** from the room sensor. A handheld thermometer near the loading door reads **4.6°C**, but that reading is only a spot measurement and may not represent the whole room. Product-core temperatures have not yet been checked. The dashboard reading has risen gradually for the last three hours.

The operations manager must decide within **20 minutes** whether to continue current operation, send a technician to verify Unit B and the sensors, reduce door openings and loading activity, move the most temperature-sensitive product to another room with limited spare capacity, start an available backup cooling unit, or combine actions.

Use only these supplied facts:

- The 1–5°C band is the relevant safe band for this exercise; no external food-safety knowledge is required.
- The backup unit can be started immediately, but its effect under comparable extreme heat is uncertain.
- Historical records show that higher outdoor temperature and frequent door opening are associated with higher room temperature; those records do not by themselves establish the causal effect of starting backup cooling.
- The fixed room sensor was calibrated six months ago. A sensor or telemetry fault is possible but not known.
- A technician can produce an independent sensor check in **25 minutes**.
- Product-core measurements require **15 minutes** and cover only a sample of products.
- Moving product reduces exposure in this room but consumes scarce capacity elsewhere and creates handling cost.
- Reducing loading activity delays some dispatch work.
- Product temperature has thermal inertia: a brief air-temperature excursion does not imply immediate product-core failure, and a normal air reading does not guarantee every product is within range.
- No strategic external actor is assumed. Staff may change door-opening behavior after an instruction, but the setting is otherwise mainly physical.

#### Form B — Emergency temporary-housing allocation after a flood

A local emergency-management office has **80 temporary-housing vouchers** available for the next two weeks after a flood. It has received **260 applications**, while field teams estimate that additional displaced households have not yet applied. No external housing law or disaster-program rule is needed; all relevant rules are supplied here.

The office must decide how to allocate the first 80 vouchers and whether to reserve some vouchers while more information is collected.

The administrative file contains household size, current reported sleeping arrangement, neighborhood, whether a dwelling passed a rapid habitability inspection, self-reported health or mobility needs, contactability, and prior program records. Some fields are missing. Applicants with poor internet access are underrepresented in online applications.

A risk score developed after earlier floods predicts which **observed applicants** remained without stable temporary housing for at least seven days. The score has not been evaluated as an allocation rule, and there is no supplied evidence that giving a voucher to a high-score household produces a larger benefit than giving one to another household.

Use only these supplied facts:

- All 260 current applicants satisfy the minimal eligibility rule.
- The office's immediate purpose is to reduce severe short-term housing instability while avoiding systematic exclusion of households poorly represented in the application data.
- Field outreach can identify additional households, but reserving vouchers for that process can delay their final allocation by up to **one day**.
- Some landlords may stop accepting vouchers if administrative delay becomes too long.
- Publishing a simple priority rule may change application behavior and the documentation people submit.
- A voucher helps only if an accepting provider is available; provider availability varies across neighborhoods.
- The historical risk score is predictive, not by itself evidence of the causal effect of receiving a voucher.
- The exercise does not stipulate one ethically correct allocation rule. Material evaluative premises must be made visible rather than hidden inside the score.
- Candidate actions include immediate allocation by a stated rule, reserving a fraction for outreach-discovered households, gathering targeted information before ranking, using categories rather than a single score, or combining these actions.

Stop here until your one-page analysis is complete.

---

### After production: use the rubric

Now score the response you actually produced. Do not rewrite it first.

Score each dimension from **0 to 2**.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Intended use and decision | Missing or merely names a topic | Partly specified | User, action or judgment, and use are explicit |
| Target and context | Missing, unqualified, or conflated with a record or metric | Focal object and sought object are only partly specified | Who or what and what about it are explicit; material qualifiers are present without checklist padding |
| Question and claim type | Major conflation | Labels present but weakly justified | Positive/normative and claim-type layers are separated correctly, and justified overlap is allowed |
| Model, measurement, and records | Treated as identical | One distinction recognized | Target, representation, and recorded traces are separated |
| Evidence limits | Unsupported certainty | Generic uncertainty statement | Specific limit and its consequence for the claim are stated |
| Values and alternatives | Recommendation presented as factual necessity | Some consequences or options identified | Stakeholders, consequences, and a nontrivial option set are visible |
| Dynamics and response | Assumes a passive one-shot world | Time or response noted | Feedback, repeated choice, or adaptation is screened appropriately |
| Revision and routing | No failure condition or next step | Generic caveat | Rival formulation, diagnostic trigger, and justified later machinery are named |

Use the dimensions diagnostically. There is **no validated aggregate cut score** for this task. A total can be recorded for pilot exploration, but the more useful question is which dimension failed and why.

Regardless of any total, treat these as major category errors:

- answering a different decision from the one stated;
- treating a record or metric as identical to the target without justification;
- treating association or predictive performance as sufficient evidence of an intervention effect;
- deriving a recommendation while hiding material value judgments;
- ignoring an explicitly stated adaptive or strategic response;
- mechanically applying every stage even when a stage is irrelevant.

### Explain one revision

After comparing your response with the rubric, answer:

> **What was the most consequential revision you would make, and why?**

Name a change in reasoning, not merely an omitted detail.

Good answers sound like:

- “I treated the observed applicant file as the target population; I would separate them because outreach changes who is represented.”
- “I treated the warehouse sensor reading as the thermal state; I would distinguish the room record, sampled product temperatures, and the decision target.”
- “I used a predictive score as if it identified who benefits most from the intervention; I would separate prediction from the allocation-effect question.”

### Return to your five-minute opening attempt

Now retrieve the response you wrote at the beginning of the chapter.

Do not ask whether the later answer simply contains more terminology. Ask whether the structure changed.

Compare the two responses on four questions:

1. Did you state the intended use more clearly?
2. Did you separate the target from its records or proxies?
3. Did you separate consequence claims from the recommendation or decision?
4. Did you identify a reason the analysis might have to move backward?

Write one sentence naming the most important change in your default framing.

### Retrieve the navigation from memory

Close or cover the chapter map before doing this task.

From memory, reconstruct the five-part navigation structure used in the worked case. Then add arrows showing at least two ways later evidence can send reasoning backward.

Also reconstruct these relationships in your own words:

- intended use versus target;
- evidence versus claim type;
- consequence claims versus evaluative premises;
- action versus feedback or response;
- monitoring versus revision and routing.

Only after you have finished should you compare your reconstruction with the chapter's canonical navigation:

**Frame and formulate → Learn from evidence → Choose → Act in responsive systems → Integrate and revise**

The arrows are not one-way. A measurement problem can send you back to the target or observation process. Deployment can change the process and send you back to the forecast, representation, evidence requirements, alternatives, or decision.

Repair what you omitted. Then choose one omission and explain why it mattered in the water case.

### Delayed retest

Do not use the second transfer form immediately.

For self-study, schedule the form you did **not** use today for approximately **7–14 days** from now. The interval is a pilot window, not a universal spacing optimum.

At the retest:

- do not reread Chapter 1 first;
- do not display the checklist or rubric while producing the response;
- use the same one-page first-pass task;
- consult the same eight rubric dimensions only after production;
- compare dimension-level performance with the first transfer attempt.

The purpose is not to prove far transfer from one delayed exercise. It is to test whether the reasoning structure can be produced again after the immediate scaffolding and narrative details have faded.

A successful Chapter 1 outcome is therefore modest but important:

> **You can begin an unfamiliar consequential problem by making the use, target, claim, evidence limits, alternatives, consequences, environment, and revision conditions explicit—without pretending that this first pass is the finished analysis.**

That is enough to move forward. The rest of the book supplies the machinery needed when the first pass identifies what must be learned, estimated, tested, compared, optimized, monitored, or revised next.
