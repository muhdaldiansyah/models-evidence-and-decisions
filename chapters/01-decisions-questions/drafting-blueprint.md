# Chapter 1 Detailed Drafting Blueprint

Status: drafting-ready authoring control.

Governed by:

- `spec.md`;
- Decisions 0004–0008;
- `anchor.md`;
- `case-data.md`;
- `decision-framing.md`;
- `dynamics-response.md`;
- `learning-sequence.md`;
- `transfer.md`.

This file does not change the Chapter 1 architecture. It converts the governed specification into a section-by-section writing plan.

## 1. Drafting objective

Write the first complete manuscript of:

**Chapter 1 — Decisions, Questions, and a First Complete Pass**

Central question:

> What is being asked, for what use, and what would count as an adequate answer?

Core competence:

> Frame the decision situation, state the intended use, specify the target of the inquiry in qualified terms, distinguish relevant claim types and environment properties at intuitive depth, and perform one informal pass through the complete reasoning process.

The chapter should leave the reader able to produce a defensible first pass on an unfamiliar consequential problem without pretending that the first pass is a completed analysis.

## 2. Fixed architecture and drafting budget

| Section | Title | Pages | Learning time | Rough prose target | Primary job |
|---:|---|---:|---:|---:|---|
| 1 | A Good Answer to the Wrong Question | 2 | 0.25 h | 650–800 words | Break technique-first reflex; preserve unsupported baseline |
| 2 | Intended Use and the Decision Situation | 4 | 0.50 h | 1,300–1,500 words | Separate use, target, decision, authority, alternatives, consequences |
| 3 | What Kind of Question Is This? | 4 | 0.55 h | 1,300–1,500 words | Layer positive/normative, claim form, and environment screens |
| 4 | A First Complete Pass: Preventing a Town Water Shortage | 8 | 1.00 h | 2,800–3,200 words | Show one complete expert performance with two backward revisions |
| 5 | When the First Formulation Fails | 3 | 0.30 h | 950–1,150 words | Distinguish adjustment from reframing; teach rival formulations and routing |
| 6 | Cold-Start Practice and Retrieval | 3 | 1.40 h | 750–950 words plus exercises | Remove scaffolds; diagnose, transfer, retrieve, schedule delayed retest |
| **Total** |  | **24** | **4.00 h** | **~7,750–9,100 words plus tables/exercises** |  |

The prose targets are drafting guides, not governed architecture. Page/time budgets remain authoritative.

## 3. Voice and exposition rules

The chapter should sound like an expert reasoning alongside the reader, not like a glossary or standards manual.

Use:

- ordinary language first;
- technical labels only after the underlying distinction is visible;
- short tables when comparison is more useful than prose;
- equations only when they clarify a distinction;
- explicit statements of what has **not** been established;
- backward references when later evidence changes earlier reasoning.

Avoid:

- acronym-heavy frameworks;
- long lists of later-chapter terminology;
- “the data say we should…” phrasing;
- presenting the Reasoning Loop as a waterfall;
- implying that every problem uses every screen;
- implying the synthetic water numbers are industry norms;
- implying that one recommendation is uniquely correct.

## 4. Reader-facing pedagogical sequence

Across the six sections, implement:

`attempt → complete worked example → self-explain → structural contrast → fade → diagnose → independently produce → retrieve → delayed retest`

The sequence is an authoring synthesis, not a reader-facing named framework.

The learner should encounter decreasing support:

1. unsupported opening attempt;
2. guided distinctions;
3. complete worked case;
4. principle-focused pauses;
5. compact structural contrasts;
6. faded reasoning prompts;
7. planted-failure repair;
8. independent transfer with no checklist/rubric visible;
9. retrieval from memory;
10. delayed parallel-form retest.

## 5. Section 1 — A Good Answer to the Wrong Question

### Purpose

Create the chapter's central failure mode before introducing terminology:

> A technically competent answer can be useless if it answers the wrong question.

### Opening scene

Begin immediately with the fictional water utility.

Reveal only:

- a seven-day hot, dry period;
- dashboard usable storage: **10.8 ML**;
- case-specific reserve: **4.5 ML**;
- current treated-water input: **8.4 ML/day**;
- the seven-day demand forecast;
- Utility Director as immediate decision-maker;
- broad possibilities: continue, verify, change production, ask customers to conserve, or combine actions.

Do **not** yet reveal:

- the 9.9 ML independent measurement;
- sensor bias;
- the 8.8 ML temporary production option details;
- the six-hour delay;
- the $2,000/day cost;
- authority split for mandatory restrictions;
- the post-conservation 8.6 ML observation.

### Opening learner task

Approximate pilot parameter: **five minutes**.

Prompt the reader to write:

- what should be modeled or calculated;
- what evidence should be checked;
- what action they would advise now;
- one assumption they are making.

No checklist and no rubric.

Tell the reader to keep the response.

Do not score or correct it line by line yet.

### Expository turn

Show that competent analysts could immediately pursue different tasks:

- forecast demand;
- verify current storage;
- calculate reserve crossing;
- estimate effect of more production;
- estimate effect of conservation;
- choose among actions.

Ask:

> Which of these is the question?

Answer:

> That depends on what the answer will be used for and what decision or judgment is actually at issue.

### First conceptual distinction

Introduce only:

- topic;
- practical concern;
- analytical question;
- claim;
- decision situation.

Do not yet define the full Reasoning Loop.

### Section close

Reader takeaway:

> Before choosing a method, make sure the answer being produced is the answer someone needs.

Forward pointer:

> The next task is to state the use, target, and decision precisely enough that two competent analysts are not silently solving different problems.

### Citation/source slots

Reader-facing citations may be light here.

Load-bearing author controls already exist for intended use and adequacy. Do not add new water-domain citations to synthetic numbers.

## 6. Section 2 — Intended Use and the Decision Situation

### Purpose

Turn the opening concern into a usable problem statement.

### Beat 1 — Intended use

Ask:

> What will the answer be used for?

Possible uses in the same water setting:

- decide whether to change operation now;
- decide whether to collect better information first;
- communicate shortage risk;
- evaluate a conservation action after the event.

Emphasize that “study water demand” is not an intended-use statement.

### Beat 2 — Target

Ask:

> What exactly are we trying to determine, and about whom or what?

Use minimally different water targets:

- physical usable storage now;
- whether storage will fall below 4.5 ML within seven days;
- seven-day demand;
- consequence of changing production;
- consequence of issuing a conservation request.

Introduce `target` as the book's informal organizing word.

Use the same-question test:

> Would two competent analysts know they are answering the same substantive question?

Only add qualifiers when changing them would materially change the question.

### Beat 3 — Record is not target

Use the dashboard:

- target: physical usable storage;
- record: dashboard value;
- observation process: remote level transmitter / telemetry.

Do not reveal the measurement failure yet.

The point is conceptual:

> A record can be evidence about the target without being the target itself.

### Beat 4 — Decision-maker and authority

Reveal the fictional authority structure:

Utility Director can:

- order independent verification;
- increase production up to 8.8 ML/day;
- issue voluntary conservation request;
- increase monitoring.

Mandatory restriction requires City Manager approval and cannot take effect sooner than six hours after request.

Teach:

> A desirable action is not necessarily an action this decision-maker can choose directly.

Distinguish:

- analysis;
- recommendation;
- decision.

Use a compact three-line contrast.

### Beat 5 — Alternatives

Start with:

- do nothing / continue;
- pump more.

Then explicitly widen:

- verify first;
- voluntary conservation;
- combine actions;
- contingent escalation.

State that supplied options can be artificially narrow.

Chapter 1 requires noticing at least one plausible missing or combined alternative when the option set is narrow.

Do not teach systematic value-focused alternative generation.

### Beat 6 — Consequences and stakeholders

List only material consequences:

- reserve crossing;
- service margin;
- operating cost;
- burden on households/businesses;
- burden of restrictions;
- timing;
- future flexibility.

Stakeholders:

- households;
- businesses;
- essential services;
- utility staff;
- municipal budget/governance.

### Beat 7 — Adequate for the stated intended use

Ask:

> What would count as a good enough answer for this decision?

Examples:

- current storage must be accurate enough that a threshold-sensitive decision is not based on a biased record;
- forecast horizon must match the seven-day decision;
- an intervention recommendation requires more than association.

Keep adequacy provisional and use-relative.

### Active micro-contrast

Same target, different intended use:

- physical storage to decide immediate pumping;
- physical storage to produce a monthly performance report.

Different targets, one intended use:

- current physical storage;
- future reserve breach;
both may inform the same operational decision.

### Section output

A compact reader-generated frame:

- intended use;
- immediate decision;
- decision-maker / authority;
- qualified target(s);
- key alternatives;
- material consequences;
- affected stakeholders.

### Section close

Transition:

> Once the use and target are explicit, the next mistake is asking for the wrong kind of claim.

## 7. Section 3 — What Kind of Question Is This?

### Purpose

Teach layered question triage without presenting one flat taxonomy.

### Layer 1 — What is/would happen versus what should matter/be done

Start in ordinary language.

Positive component:

> What is, was, or would happen under specified conditions?

Normative component:

> What should matter, count as better or acceptable, or be done?

Then introduce `positive` and `normative`.

Use water contrast:

- “Will storage fall below 4.5 ML?” → positive.
- “How burdensome would a restriction be?” → positive consequence inquiry.
- “How much burden is acceptable to reduce shortage risk?” → normative.
- “Should the director issue a voluntary request?” → recommendation containing both positive and normative premises.

Do not call normative reasoning “mere opinion.”

### Layer 2 — Claim form

Use the same water setting.

Association:

> Across historical hot-weather days, is higher temperature associated with higher demand?

Prediction:

> Given the current information, will usable storage fall below reserve within seven days?

Intervention:

> Would issuing a conservation request reduce seven-day shortage risk compared with no request?

Counterfactual:

> If reserve was crossed yesterday, would it have been avoided had the request been issued three days earlier?

Decision:

> What should the utility do now?

Emphasize:

- forms may overlap;
- association does not by itself establish intervention effect;
- prediction does not automatically identify a causal lever;
- counterfactual is not every hypothetical.

### Layer 3 — Environment properties

Ask:

- does time matter?
- what carries over?
- what is delayed?
- what feeds back?
- will the decision be revisited?
- will people or organizations respond?

Keep `feedback` intuitive.

Do not teach:

- stocks/flows as required terms;
- positive/negative feedback;
- stability;
- control;
- equilibrium;
- game theory.

### Structural contrasts

#### Pendulum

Use three purposes:

- estimate local gravitational acceleration;
- predict short-horizon angular position;
- design a durable clock.

Purpose changes representation and adequacy even when the target system is the same.

Use pendulum also to establish:

> dynamic does not imply adaptive or strategic.

#### Student assessment

Keep compact:

- rank applicants;
- diagnose prerequisite skills;
- select next instructional activity.

Preview:

- target versus observed response;
- proxy/measurement concerns;
- value stakes;
- behavior can change when the score becomes consequential.

Do not teach psychometrics here.

### Self-explanation pause 1

Prompt:

> A historical relationship predicts shortage well. Why does that not by itself tell us whether changing one predictor will prevent shortage?

Require principle, not paraphrase.

### Section close

Give a short reusable sequence in ordinary language, not an acronym:

> What is being asked? What kind of answer would satisfy it? Does time or response change the problem?

Transition:

> Now perform the whole first pass once, with the details arriving in the order a real analysis often encounters them.

## 8. Section 4 — A First Complete Pass: Preventing a Town Water Shortage

### Purpose

Show one complete expert performance under the five book parts.

This is the chapter's longest section and primary worked example.

The reader must see reasoning transitions, not just a final answer.

### 4.1 Frame and Formulate

Restate the intended use:

> Support the Utility Director's immediate operating decision for the seven-day heatwave.

State:

- immediate decision;
- authority;
- current informational targets;
- seven-day horizon;
- provisional boundary;
- key alternatives;
- reserve threshold as fictional case rule.

Use the simple no-action balance with dashboard start:

`10.8 + 58.8 - 64.9 = 4.7 ML`

Interpret:

> Marginally above reserve, if the dashboard is an adequate representation of current physical storage and if the no-new-action forecast remains applicable.

Surface assumptions explicitly.

Rival formulation:

> Is this mainly a forecasting problem, or first a current-state verification problem?

### Self-explanation pause 2

Ask:

> If the decision changes when starting storage changes by less than 1 ML, what evidence should be questioned before adding a more elaborate forecast model?

Then continue.

### 4.2 Learn from Evidence

Reveal:

- independent check exists;
- takes 25 minutes;
- result: 9.9 ML;
- remote transmitter is biased high.

Calculate:

`9.9 + 58.8 - 64.9 = 3.8 ML`

### Backward Revision 1

Explicitly return to earlier reasoning.

Show:

- target unchanged;
- observation changed;
- current-state belief changed;
- decision urgency changed;
- some prior “forecasting sophistication” would have been beside the point if starting state was wrong.

Label the revision:

**measurement / observation revision**.

Do not call it “the sensor is bad therefore SCADA is unreliable.”

### Evidence limits

Explain what historical demand records can support:

- prediction under comparable conditions.

Explain what they do not alone establish:

- effect of a new conservation request;
- effect of production change.

Keep identification language informal.

### 4.3 Choose

Reveal:

- temporary production: 8.8 ML/day;
- six-hour delay;
- $2,000/day incremental cost;
- voluntary request authority;
- mandatory restriction authority split.

Calculate central production-increase scenario:

`9.9 + 61.5 - 64.9 = 6.5 ML`

Then stress demand:

`9.9 + 61.5 - 67.7 = 3.7 ML`

Interpret:

- production helps;
- not robust to supplied high-demand stress;
- decision remains consequential.

Compare alternatives:

- verify only;
- increase production only;
- conservation only;
- production + conservation;
- staged combination + monitoring;
- request stronger authority if trigger is crossed.

Make evidence-versus-choice bridge explicit.

Example positive consequence claim:

> Higher production increases projected storage under the supplied balance.

Example evaluative premise:

> Paying the incremental cost is acceptable to gain operating margin during the heatwave.

Example recommendation:

> Use a staged combination if those premises are accepted.

Example decision:

> The Utility Director authorizes the permitted actions.

### 4.4 Act in Responsive Systems

Ask:

- what carries over? usable stored water;
- what adds/removes? treated-water input and demand;
- what is delayed? production increase and level verification;
- what feeds back? observations influence actions; actions influence future storage/demand; new observations influence next action;
- will we decide again? yes.

Do not require stock-flow vocabulary.

Reveal that the no-action forecast was explicitly conditioned on no new conservation intervention.

Worked staged action may now include:

- verified state;
- production increase;
- voluntary conservation request;
- enhanced monitoring.

### 4.5 Integrate and Revise

After 24 hours reveal:

- forecast Day 1 demand: 9.0 ML;
- observed demand: 8.6 ML;
- several large users report reducing nonessential use after the request.

Do **not** estimate `0.4 ML` as the causal effect.

### Backward Revision 2

Return to the forecast formulation.

State:

> The no-new-action forecast is no longer the correct forecast for a system in which a conservation action has been deployed and behavior has changed.

Revise:

- forecast assumptions;
- monitoring plan;
- perhaps representation of demand response;
- next decision.

Label:

**structural/process revision**.

Contrast with a simple parameter update.

### Self-explanation pause 3

Ask:

> What exactly has changed here: our estimate of an unchanged process, or the process generating future demand?

Then explain.

### Repeated decision

Use the cadence:

- initial decision;
- review after verification;
- review after 24 hours;
- escalation if updated projection again falls below 4.5 ML.

No dynamic programming or control formalism.

### End-of-section synthesis

Present one compact first-pass record, perhaps a table:

| Element | Current first-pass statement |
|---|---|
| Intended use | Immediate seven-day operating decision |
| Decision-maker | Utility Director |
| Target(s) | Current physical storage; reserve breach; consequences of actions |
| Evidence | Dashboard + independent verification + demand history |
| Key limit | Historical patterns do not isolate intervention effect |
| Alternatives | Continue, verify, raise production, conserve, combine, escalate |
| Values | Service margin, burden, cost, continuity |
| Dynamics | Accumulation, delays, repeated review |
| Response | Conservation changes demand process |
| Revision triggers | Sensor discrepancy; post-action demand |
| Routing | Ch2–15 as relevant |

Do not present this as a mandatory universal checklist.

### Section close

Say explicitly:

> The point was not to finish water-utility analysis in eight pages. The point was to experience a complete first pass that reveals what later expertise is needed.

## 9. Section 5 — When the First Formulation Fails

### Purpose

Teach that “update the number” and “change the problem formulation” are different operations.

### Beat 1 — Adjustment versus revision

Use a compact contrast table.

Adjustment within formulation:

- update weather forecast;
- update demand estimate;
- update current storage when same measurement model remains trusted.

Formulation revision:

- change target;
- change horizon;
- change comparison;
- change boundary;
- separate physical state from record;
- add behavioral response;
- revise decision authority;
- introduce a new alternative;
- revise evaluative premises.

### Beat 2 — Two water rivals

Rival A:

> Forecast shortage under current operation.

Rival B:

> Decide whether to verify state before acting.

Ask what evidence or decision condition makes each more appropriate.

Show that a problem can change from one rival to another as evidence arrives.

### Beat 3 — Pendulum

Return briefly to the three uses.

Do not repeat Section 3.
Use it only to make the revision principle vivid:

> same object, different purpose → different model adequacy.

### Beat 4 — Student-assessment faded micro-case

Use student assessment as the **faded case** because it is already in the approved example portfolio and does not contaminate the two cold-transfer forms.

Supply all necessary facts.

Give only partial prompts:

- The same 20-item assessment is proposed for ranking applicants and diagnosing prerequisite skills.
- A single total score is available.
- No external psychometrics knowledge is required.

Ask the reader to complete:

- intended use;
- target;
- one record-versus-target concern;
- one consequence of using the same analysis for both purposes;
- one likely revision trigger.

Do not provide the full Chapter 1 checklist.

After response, give a short expert comparison.

### Beat 5 — Specialist handoff

Give examples of correct routing:

- measurement validity → Ch3;
- observation process → Ch4;
- causal identification → Ch7;
- value/objective structure → Ch10;
- formal decision under uncertainty → Ch11;
- dynamics/control → Ch13–14;
- incentives/gaming → Ch15.

The skill is recognizing the need, not using the later machinery early.

### Section close

> A strong first pass is valuable partly because it tells you when the first pass is no longer enough.

## 10. Section 6 — Cold-Start Practice and Retrieval

### Purpose

Remove scaffolds and obtain evidence of independent first-pass competence.

This section is activity-heavy; prose must stay lean.

### Activity 1 — Planted-failure diagnosis

Present a concise faulty analysis containing at least six of:

- topic substituted for intended use;
- dashboard record treated as physical target;
- material target qualifier omitted;
- association/predictive performance treated as intervention evidence;
- recommendation without consequences/values/alternatives;
- recommendation treated as identical to decision;
- supplied option set treated as complete;
- action authority ignored;
- deployment assumed not to change behavior;
- Reasoning Loop treated as mandatory waterfall.

For each selected error require:

1. diagnosis;
2. consequence;
3. repair.

Ask learner to identify the most consequential first repair.

### Activity 2 — Cold-transfer production

Direct the learner to `transfer.md`.

No checklist.
No worked water solution.
No scoring rubric visible.

Self-study:

- use the less familiar form first.

Form A:
refrigerated warehouse.

Form B:
emergency temporary housing.

Current pilot target:

**30–40 minutes**.

State that the interval is an authoring/pilot target, not a universal standard.

### Activity 3 — Rubric and post-task explanation

After submission, reveal the 8-dimension rubric.

Prioritize dimension-level feedback.

No validated aggregate cut score.

Prompt:

> What was the most consequential reasoning revision you made after checking your answer, and why?

### Activity 4 — Retrieval from memory

Hide the navigation map.

Ask reader to reconstruct:

- five book parts;
- backward links;
- intended use versus target;
- evidence versus claim type;
- consequences versus evaluative premises;
- action versus feedback/response;
- monitoring versus revision/routing.

Then compare and repair.

Do not substitute recognition questions.

### Activity 5 — Delayed retest

Tell reader to schedule the other transfer form for **7–14 days later**.

Label this clearly as the current practical pilot window.

For pilots:

- counterbalance form order;
- record completion time;
- compare dimension-level performance;
- inspect domain-familiarity effects.

### Final before/after comparison

Return to the preserved five-minute opening response.

Ask:

> What did you fail to represent at the beginning that you now consider decision-relevant?

This is the chapter's closing reflective question.

### Final chapter sentence

End with a forward-looking line equivalent to:

> The rest of the book develops the machinery needed to answer the questions this first pass has learned to ask.

Do not end with a long terminology summary.

## 11. Figure and table plan

Keep visuals sparse.

### Required / high-value

1. **Opening demand table** — seven-day forecast.
2. **One simple storage-balance visual or equation** — clarify starting state + input − demand.
3. **Before/after measurement table** — dashboard 10.8 versus verified 9.9 and resulting 4.7 versus 3.8 projection.
4. **Compact first-pass synthesis table** at end of Section 4.
5. **Optional five-part Reasoning Loop map** only after reader has experienced enough of the structure; do not open the chapter with it.

### Avoid

- detailed process-flow diagrams;
- stock-flow diagrams;
- causal DAGs;
- decision trees;
- loop polarity diagrams;
- utility curves;
- optimization graphics.

Those belong later.

## 12. Citation plan

### Reader-facing conceptual citations

Use sparingly where a load-bearing conceptual distinction is introduced.

Potential source families already promoted:

- intended use / adequacy;
- target terminology;
- positive/normative;
- association/prediction/intervention/counterfactual;
- decision framing;
- feedback/deployment;
- pedagogy only if the manuscript explicitly discusses why an exercise is designed a certain way.

### Water-domain citations

The **synthetic numbers require no external citation**.

Do not cite authoritative guidance as if it supplied:

- 4.5 ML reserve;
- 14.0 ML capacity;
- 8.4/8.8 ML/day;
- six-hour delay;
- $2,000/day;
- 25-minute verification;
- 0.4 ML/day stress;
- fictional authority.

If manuscript prose makes general water-utility claims beyond the supplied fictional case, verify and promote the relevant source before treating that prose as stable.

### Pedagogy citations

Prefer keeping most learning-science provenance in author notes rather than interrupting reader-facing prose.

## 13. Exercise-answer architecture

For every exercise, draft answer guidance alongside the question.

### Opening attempt

No model answer immediately.

Later comparison should point out common omissions without declaring one unique response.

### Self-explanation pauses

Answer guidance should identify the principle.

Do not reward keyword matching.

### Faded student-assessment case

Answer guidance should allow multiple defensible formulations if justified.

### Planted failure

Answer key should include:

- error;
- why it matters;
- acceptable repair;
- severity notes.

### Transfer forms

Maintain separate scoring guide using the governed 8 dimensions.

Allow justified “not material here.”

Penalize mechanical application of every stage.

## 14. Drafting order

Do **not** draft Section 1 through Section 6 strictly in reader order.

Recommended authoring order:

1. **Section 4** — complete worked water case;
2. **Section 2** — framing vocabulary extracted from what Section 4 actually needs;
3. **Section 3** — claim/environment distinctions;
4. **Section 1** — opening calibrated to the finished worked case;
5. **Section 5** — revision and faded contrast;
6. **Section 6** — assessment/retrieval tasks;
7. full-chapter integration pass.

Reason:

Section 4 is the load-bearing spine. Drafting it first prevents Sections 1–3 from introducing distinctions that the worked case never uses.

## 15. Section drafting completion gates

### Section 1 complete when

- opening prompt can be attempted without specialist knowledge;
- no later reveal is leaked;
- baseline response can be preserved;
- central wrong-question failure is vivid.

### Section 2 complete when

- intended use, target, decision, recommendation, authority, alternative, consequence are distinct;
- terminology burden remains low;
- reader can state a usable decision frame.

### Section 3 complete when

- positive/normative and claim-form layers remain orthogonal;
- all four claim forms are intuitive;
- dynamics/adaptation screen does not become Ch13–15 formalism.

### Section 4 complete when

- all frozen arithmetic is correct;
- reveal order is respected;
- Revision 1 and Revision 2 are visibly different;
- evidence/choice distinction is explicit;
- final recommendation remains premise-dependent;
- later-chapter routing is visible.

### Section 5 complete when

- adjustment versus reformulation is clear;
- pendulum does not repeat earlier exposition;
- faded student case removes prompts but not facts;
- handoff feels like competence rather than disclaimer.

### Section 6 complete when

- cold transfer occurs without visible checklist/rubric;
- planted failure requires repair;
- retrieval is generative;
- delayed retest instruction is practical;
- no cut score is invented.

## 16. Chapter-level integration checklist

Before declaring first draft complete:

- title unchanged;
- central question unchanged;
- six sections unchanged;
- page target still 24;
- learning time still 4 hours;
- no hidden water-engineering knowledge;
- no synthetic number presented as external fact;
- no recommendation presented as the decision;
- no evidence presented as sufficient for normative choice;
- no prediction/association presented as intervention evidence;
- no formal stock-flow/control/game-theory material;
- no pedagogy parameter presented as universal optimum;
- no cold-transfer answer cues leaked into exposition;
- all later-chapter technical terms either necessary or removed;
- every preview supports a later operation;
- backward revision is visible rather than silently editing earlier prose.

## 17. First-draft artifact plan

The first manuscript should be written as:

`chapters/01-decisions-questions/chapter.md`

Recommended supporting author files remain separate:

- `spec.md` — governed specification;
- `anchor.md` — case narrative and reveal controls;
- `case-data.md` — frozen arithmetic;
- `decision-framing.md` — decision boundary;
- `dynamics-response.md` — systems boundary;
- `learning-sequence.md` — pedagogy control;
- `transfer.md` — parallel forms;
- `drafting-blueprint.md` — this file.

Do not merge these control artifacts into reader-facing prose.

## 18. Remaining blockers before first manuscript writing

After this blueprint is accepted and committed, there is **no conceptual or architectural blocker** to beginning the first manuscript.

The only remaining pre-publication—not pre-drafting—items include:

- human water-utility / engineering SME realism review;
- final exercise answer-key adjudication;
- reader/timed pilots;
- transfer-form comparability pilot;
- citation and terminology audit;
- revision after pilot evidence.

The next action after this blueprint is therefore:

> draft Section 4 first, then Section 2, Section 3, Section 1, Section 5, and Section 6, followed by a chapter integration pass.

DRAFTING BLUEPRINT READY
