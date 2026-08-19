# Term Index

**Generated from `../canon/terminology.md` by `../tools/make-term-index.py`. Do not edit by hand — run `make index`.**

163 controlled terms across seventeen chapters.

**This is an index, not a glossary.** It tells you where a term is introduced and what the book keeps it apart from.
It does not define the terms, because the book defines them in the place where they do work, and a definition lifted out of that place would be a different claim.

Terms are listed by the chapter that introduces them. A term you meet in Chapter 12 may have been introduced in Chapter 3.

## The six collisions

The book works across fields that borrowed one another's words without coordinating.
Where one word carries two established meanings, the book **announces the collision and keeps both senses** rather than inventing a third word to avoid it.

**If a term below is giving you trouble, look here first.**

| Word | Sense one | Sense two | Announced |
|---|---|---|---|
| `validation` | in measurement, assessing whether evidence supports an interpretation | in computational modelling, checking a model against the world | Chapter 3, taken up in Chapter 5 |
| `consistency` | an estimator property — converging on the target as evidence grows | the third identification condition, about observed outcomes under treatment received | Chapter 8 |
| `significance` | a threshold verdict on a P value | substantive importance | Chapter 8 |
| `sensitivity analysis` | varying inputs inside a formulation | robustness of a decision across futures | Chapter 8, with the decision sense at Chapter 12 |
| `robustness` / `stability` | in dynamics, whether a system returns after disturbance | in decision-making, whether a choice survives across futures | Chapter 13 |
| **`identifiable`** — four senses | `statistical identifiability` and `causal identification` (Chapter 7) | `structural identifiability` and `practical identifiability` (Chapter 14) | Chapter 14 |

**No chapter may add a fifth sense of `identifiable`.** That is a standing instruction proposed at [Decision 0021](../decisions/0021-chapter14-sequential-control-terminology-and-boundary.md) clause 7.3.

Two further notes. `equilibrium` means one thing in Chapter 13's dynamics and another in Chapter 15's strategic setting; the registry flagged it from Chapter 1. And `shadow price` collides with a cost-benefit sense the book does not use — noted at Chapter 12 and not adopted.

## Terms by chapter

### Chapter 1 — [20 terms](../chapters/01-decisions-questions/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`adequacy`](../canon/terminology.md#adequacy) | accuracy | modeling and simulation / VVUQ / engineering evaluation |
| [`alternative`](../canon/terminology.md#alternative) | consequence | decision analysis / ordinary decision practice |
| [`association`](../canon/terminology.md#association) | correlation | statistics / epidemiology / causal inference |
| [`backward revision`](../canon/terminology.md#backward-revision) | model criticism (Chapter 5); iteration | the book's own controlled use |
| [`consequence`](../canon/terminology.md#consequence) | alternative | decision analysis / ordinary decision practice |
| [`context of use`](../canon/terminology.md#context-of-use) | intended use | computational modeling and simulation VVUQ / model credibility |
| [`counterfactual`](../canon/terminology.md#counterfactual) | generic hypothetical scenario | causal inference / philosophy / economics |
| [`decision`](../canon/terminology.md#decision) | analytical question | ordinary language / decision analysis / decision theory |
| [`decision-maker`](../canon/terminology.md#decision-maker) | analyst | decision analysis / decision theory / organizational decision practice |
| [`delay`](../canon/terminology.md#delay) | slowness | system dynamics |
| [`endogenous response`](../canon/terminology.md#endogenous-response) | adaptive response (Chapter 1); policy resistance (Chapter 13); feedback (Chapter 13); distribution shift | economics |
| [`estimand`](../canon/terminology.md#estimand) | target | statistics / causal inference / clinical-trial methodology |
| [`feedback`](../canon/terminology.md#feedback) | ordinary evaluative or reviewer feedback | dynamical systems / control / system dynamics |
| [`intended use`](../canon/terminology.md#intended-use) | purpose | modeling and simulation / engineering M&S |
| [`intervention`](../canon/terminology.md#intervention) | observed exposure | causal inference / experimental science / policy evaluation |
| [`normative`](../canon/terminology.md#normative) | positive | economics for the paired positive/normative distinction |
| [`positive`](../canon/terminology.md#positive) | descriptive | economics for the paired positive/normative distinction |
| [`prediction`](../canon/terminology.md#prediction) | description | statistics / machine learning / forecasting |
| [`target`](../canon/terminology.md#target) | construct | ordinary and interdisciplinary analytic usage with multiple… |
| [`target population`](../canon/terminology.md#target-population) | observed sample | survey statistics / statistics / clinical research |

### Chapter 2 — [9 terms](../chapters/02-representation-mechanisms/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`abstraction`](../canon/terminology.md#abstraction) | idealization | philosophy of science |
| [`aggregation`](../canon/terminology.md#aggregation) | abstraction | modeling practice |
| [`boundary`](../canon/terminology.md#boundary) | a physical edge | system dynamics |
| [`generality`](../canon/terminology.md#generality) | abstraction | mechanistic explanation |
| [`idealization`](../canon/terminology.md#idealization) | abstraction | philosophy of science |
| [`mechanism`](../canon/terminology.md#mechanism) | an identified causal effect | philosophy of science (mechanistic explanation); life sciences |
| [`representation`](../canon/terminology.md#representation) | the target system it represents | philosophy of science |
| [`state`](../canon/terminology.md#state) | any variable | dynamical systems |
| [`target system`](../canon/terminology.md#target-system) | the model or representation of it | philosophy of science (established) |

### Chapter 3 — [15 terms](../chapters/03-measurement-operationalization/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`accuracy`](../canon/terminology.md#accuracy) | trueness alone | metrology (VIM §2.13) |
| [`calibration`](../canon/terminology.md#calibration) | validation | metrology |
| [`construct`](../canon/terminology.md#construct) | measure | measurement science / psychometrics |
| [`measurand`](../canon/terminology.md#measurand) | construct | metrology (VIM §2.3) |
| [`measure`](../canon/terminology.md#measure) | construct | measurement science |
| [`measurement error`](../canon/terminology.md#measurement-error) | mistake | metrology |
| [`operationalization`](../canon/terminology.md#operationalization) | conceptualization | social-science methodology |
| [`precision`](../canon/terminology.md#precision) | accuracy | metrology (VIM §2.15) |
| [`proxy`](../canon/terminology.md#proxy) | construct | measurement / econometrics |
| [`reliability`](../canon/terminology.md#reliability) | validity | social-science methodology / psychometrics |
| [`score`](../canon/terminology.md#score) | construct | social-science methodology / measurement |
| [`trueness`](../canon/terminology.md#trueness) | accuracy | metrology (VIM §2.14) |
| [`validation`](../canon/terminology.md#validation) | validity | two distinct traditions share the word |
| [`validity`](../canon/terminology.md#validity) | reliability | measurement science / social-science methodology / psychometrics |
| [`working definition`](../canon/terminology.md#working-definition) | construct | plain English for what `adcock2001validity` p. 530 calls a… |

### Chapter 4 — [7 terms](../chapters/04-observation-provenance/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`censoring`](../canon/terminology.md#censoring) | missingness | statistics |
| [`coverage`](../canon/terminology.md#coverage) | response rate | survey methodology and official statistics |
| [`missingness`](../canon/terminology.md#missingness) | censoring | statistics |
| [`nonresponse`](../canon/terminology.md#nonresponse) | missingness generally | survey methodology |
| [`observation process`](../canon/terminology.md#observation-process) | the process being modelled | statistics and survey methodology |
| [`record`](../canon/terminology.md#record) | the thing recorded | ordinary and administrative usage |
| [`selection`](../canon/terminology.md#selection) | sampling | statistics |

### Chapter 5 — [6 terms](../chapters/05-assumptions-rival-models/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`assumption record`](../canon/terminology.md#assumption-record) | a list of caveats | modelling practice |
| [`failure mode`](../canon/terminology.md#failure-mode) | a risk | engineering and reliability practice |
| [`rival model`](../canon/terminology.md#rival-model) | alternative representation (Chapter 2, for construction and perspective); competing causal hypotheses to be… | modelling practice |
| [`sensitivity analysis`](../canon/terminology.md#sensitivity-analysis) | criticism (Chapter 5); robustness (Chapter 12); uncertainty quantification | modelling / decision analysis |
| [`structural uncertainty`](../canon/terminology.md#structural-uncertainty) | parameter uncertainty | modelling and simulation |
| [`verification`](../canon/terminology.md#verification) | validation | computational modelling and simulation VVUQ |

### Chapter 6 — [9 terms](../chapters/06-probability-simulation/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`base rate`](../canon/terminology.md#base-rate) | prior | statistics |
| [`conditional probability`](../canon/terminology.md#conditional-probability) | filtering a dataset | mathematics |
| [`expectation`](../canon/terminology.md#expectation) | the most likely outcome | mathematics |
| [`expected value`](../canon/terminology.md#expected-value) | the expectation itself (Chapter 6); the most likely outcome | decision analysis |
| [`posterior`](../canon/terminology.md#posterior) | prior | Bayesian statistics |
| [`prior`](../canon/terminology.md#prior) | base rate (a prior is often *set from* a base rate but need not be); assumption | Bayesian statistics |
| [`probability`](../canon/terminology.md#probability) | frequency alone | mathematics |
| [`scoring rule`](../canon/terminology.md#scoring-rule) | accuracy metric | forecast verification / statistics / decision theory |
| [`sharpness`](../canon/terminology.md#sharpness) | calibration | forecast verification / statistics |

### Chapter 7 — [9 terms](../chapters/07-targets-identification/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`causal identification`](../canon/terminology.md#causal-identification) | statistical identifiability | causal inference / econometrics |
| [`confounding`](../canon/terminology.md#confounding) | correlation | causal inference / epidemiology / statistics |
| [`consistency`](../canon/terminology.md#consistency) | **consistency of an estimator (Chapter 8), which is an unrelated concept sharing the word**; reliability… | causal inference / epidemiology |
| [`exchangeability`](../canon/terminology.md#exchangeability) | positivity | causal inference / epidemiology |
| [`identifying assumption`](../canon/terminology.md#identifying-assumption) | modelling assumption | causal inference / econometrics |
| [`positivity`](../canon/terminology.md#positivity) | exchangeability | causal inference / epidemiology |
| [`statistical identifiability`](../canon/terminology.md#statistical-identifiability) | causal identification | statistics |
| [`target quantity`](../canon/terminology.md#target-quantity) | target (Chapter 1, informal); estimand (the specified form); estimator | causal inference |
| [`target trial`](../canon/terminology.md#target-trial) | an actual experiment | causal inference / epidemiology |

### Chapter 8 — [9 terms](../chapters/08-estimation-uncertainty/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`P value`](../canon/terminology.md#p-value) | the probability a hypothesis is true | statistics |
| [`analytic flexibility`](../canon/terminology.md#analytic-flexibility) | fraud | statistics / research methodology |
| [`estimate`](../canon/terminology.md#estimate) | estimand | statistics |
| [`estimator`](../canon/terminology.md#estimator) | estimand | statistics |
| [`interval estimate`](../canon/terminology.md#interval-estimate) | a range of plausible values in ordinary speech | statistics |
| [`model checking`](../canon/terminology.md#model-checking) | verification (Chapter 5); validation (Chapter 5); criticism (Chapter 5); calibration (Chapters 3 and 6);… | statistics |
| [`sampling variability`](../canon/terminology.md#sampling-variability) | measurement uncertainty (Chapter 3); structural uncertainty (Chapter 5); Monte Carlo error (Chapter 6); the… | statistics |
| [`standard error`](../canon/terminology.md#standard-error) | standard deviation | statistics |
| [`statistical significance`](../canon/terminology.md#statistical-significance) | practical importance | statistics |

### Chapter 9 — [8 terms](../chapters/09-evidence-synthesis/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`dependence`](../canon/terminology.md#dependence) | statistical dependence between variables | the book's own usage in this sense |
| [`evidence synthesis`](../canon/terminology.md#evidence-synthesis) | averaging | research methodology / evidence-based practice |
| [`expert judgment`](../canon/terminology.md#expert-judgment) | opinion | decision analysis / risk analysis |
| [`external validity`](../canon/terminology.md#external-validity) | validity in the measurement sense (Chapter 3); internal validity | research design / social science methodology |
| [`heterogeneity`](../canon/terminology.md#heterogeneity) | sampling variability (Chapter 8); measurement error (Chapter 3); disagreement caused by analytic flexibility… | meta-analysis / statistics / causal inference |
| [`replication`](../canon/terminology.md#replication) | reproduction of an analysis on the same data | research methodology |
| [`support factor`](../canon/terminology.md#support-factor) | confounder (Chapter 7); moderator | philosophy of causation / economics |
| [`transportability`](../canon/terminology.md#transportability) | external validity (the binary framing this book declines); statistical adjustment | causal inference |

### Chapter 10 — [8 terms](../chapters/10-values-alternatives/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`attribute`](../canon/terminology.md#attribute) | objective | decision analysis |
| [`constraint`](../canon/terminology.md#constraint) | objective | decision analysis / optimization |
| [`fundamental objective`](../canon/terminology.md#fundamental-objective) | means objective | decision analysis |
| [`means objective`](../canon/terminology.md#means-objective) | fundamental objective | decision analysis |
| [`metric`](../canon/terminology.md#metric) | objective | management practice / decision analysis |
| [`objective`](../canon/terminology.md#objective) | value | decision analysis |
| [`stakeholder`](../canon/terminology.md#stakeholder) | decision-maker (Chapter 1); expert | decision analysis / public-sector practice |
| [`value`](../canon/terminology.md#value) | objective | decision analysis |

### Chapter 11 — [7 terms](../chapters/11-decisions-voi/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`ambiguity`](../canon/terminology.md#ambiguity) | risk | decision theory |
| [`decision quality`](../canon/terminology.md#decision-quality) | outcome quality | decision analysis |
| [`decision tree`](../canon/terminology.md#decision-tree) | a causal diagram (Chapter 7); an influence diagram | decision analysis |
| [`risk attitude`](../canon/terminology.md#risk-attitude) | risk as a hazard | decision analysis / economics |
| [`utility`](../canon/terminology.md#utility) **[open]** | objective | decision theory |
| [`value of information`](../canon/terminology.md#value-of-information) | how informative an observation is (Chapter 6's ratio); the cost of collection | decision analysis |
| [`value of perfect information`](../canon/terminology.md#value-of-perfect-information) | the value of a particular study | decision analysis |

### Chapter 12 — [11 terms](../chapters/12-optimization-robustness/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`adaptive plan`](../canon/terminology.md#adaptive-plan) | a vague plan | policy analysis |
| [`convexity`](../canon/terminology.md#convexity) | linearity | mathematics / optimization |
| [`feasible region`](../canon/terminology.md#feasible-region) | the option set (Chapter 10); the alternative set | optimization |
| [`local optimum`](../canon/terminology.md#local-optimum) | global optimum | optimization |
| [`marginal benefit`](../canon/terminology.md#marginal-benefit) | total benefit | economics |
| [`marginal cost`](../canon/terminology.md#marginal-cost) | total cost | economics |
| [`regret`](../canon/terminology.md#regret) | loss | decision theory |
| [`robustness`](../canon/terminology.md#robustness) | stability (Chapter 13); reliability (Chapter 3); optimality | decision analysis / policy analysis |
| [`scenario`](../canon/terminology.md#scenario) | forecast | policy analysis / futures studies |
| [`shadow price`](../canon/terminology.md#shadow-price) | market price | optimization |
| [`signpost`](../canon/terminology.md#signpost) | a metric (Chapter 10); a monitoring indicator | policy analysis |

### Chapter 13 — [13 terms](../chapters/13-dynamics-feedback/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`accumulation`](../canon/terminology.md#accumulation) | growth | system dynamics |
| [`balancing feedback`](../canon/terminology.md#balancing-feedback) | reinforcing feedback | system dynamics (`self-correcting`); control theory (`negative… |
| [`closed loop`](../canon/terminology.md#closed-loop) | a repeated decision | control theory |
| [`equilibrium`](../canon/terminology.md#equilibrium) | stability | dynamical systems |
| [`flow`](../canon/terminology.md#flow) | a stock | system dynamics |
| [`open loop`](../canon/terminology.md#open-loop) | a system with no dynamics | control theory |
| [`oscillation`](../canon/terminology.md#oscillation) | noise | dynamical systems |
| [`overshoot`](../canon/terminology.md#overshoot) | overreaction as a character failing | system dynamics |
| [`policy resistance`](../canon/terminology.md#policy-resistance) | a policy failing | system dynamics |
| [`reinforcing feedback`](../canon/terminology.md#reinforcing-feedback) | balancing feedback | system dynamics (`self-reinforcing`); control theory (`positive… |
| [`stability`](../canon/terminology.md#stability) | equilibrium | dynamical systems |
| [`state space`](../canon/terminology.md#state-space) | the state | dynamical systems |
| [`stock`](../canon/terminology.md#stock) | a flow | system dynamics |

### Chapter 14 — [9 terms](../chapters/14-sequential-control/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`control`](../canon/terminology.md#control) | being in control | control theory |
| [`exploitation`](../canon/terminology.md#exploitation) | exploration | reinforcement learning |
| [`exploration`](../canon/terminology.md#exploration) | exploitation | reinforcement learning |
| [`feedback decision`](../canon/terminology.md#feedback-decision) | a decision that is revisited | the book's own term, built from control theory |
| [`information acquisition`](../canon/terminology.md#information-acquisition) | value of information (Chapter 11), which is what it is worth | decision analysis |
| [`observability`](../canon/terminology.md#observability) | structural identifiability | control theory |
| [`policy`](../canon/terminology.md#policy) | a plan | reinforcement learning |
| [`practical identifiability`](../canon/terminology.md#practical-identifiability) | structural identifiability | systems biology |
| [`structural identifiability`](../canon/terminology.md#structural-identifiability) | statistical identifiability (Chapter 7); causal identification (Chapter 7); practical identifiability… | systems and control theory |

### Chapter 15 — [10 terms](../chapters/15-strategic-interaction/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`Goodhart effect`](../canon/terminology.md#goodhart-effect) | metric gaming, which is one of its four mechanisms | economics |
| [`commitment`](../canon/terminology.md#commitment) | a decision (Chapter 11); a plan | game theory |
| [`delegation`](../canon/terminology.md#delegation) | instruction | the book's own controlled use |
| [`incentive`](../canon/terminology.md#incentive) | a motive | economics |
| [`information asymmetry`](../canon/terminology.md#information-asymmetry) | uncertainty | economics |
| [`metric gaming`](../canon/terminology.md#metric-gaming) | fraud | public administration |
| [`performativity`](../canon/terminology.md#performativity) | self-fulfilling prophecy in the loose sense | social science |
| [`principal-agent`](../canon/terminology.md#principal-agent) | employer and employee | economics |
| [`strategic dependence`](../canon/terminology.md#strategic-dependence) | feedback (Chapter 13); policy resistance (Chapter 13); correlation | game theory |
| [`strategic game`](../canon/terminology.md#strategic-game) | a decision problem (Chapter 11); a scenario set (Chapter 12); a metaphor | game theory |

### Chapter 16 — [5 terms](../chapters/16-integration-full-loop/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`deep structure`](../canon/terminology.md#deep-structure) | surface feature | cognitive science |
| [`materiality`](../canon/terminology.md#materiality) | relevance in the loose sense | the book's own controlled use |
| [`routing record`](../canon/terminology.md#routing-record) | a project plan | the book's own controlled use |
| [`surface feature`](../canon/terminology.md#surface-feature) | deep structure | cognitive science |
| [`triage`](../canon/terminology.md#triage) | doing a bit of everything | the book's own controlled use |

### Chapter 17 — [8 terms](../chapters/17-deployment-monitoring/chapter.md)

| Term | Kept distinct from | Field |
|---|---|---|
| [`drift`](../canon/terminology.md#drift) | ordinary variation | statistics |
| [`monitoring`](../canon/terminology.md#monitoring) | model checking (Chapter 5), which the registry already records as the same activity before deployment | the book's own controlled use |
| [`ordinary variation`](../canon/terminology.md#ordinary-variation) | signal | statistical process control |
| [`permissible use`](../canon/terminology.md#permissible-use) | intended use (Chapter 1), which is what it was built for | modelling and simulation standards |
| [`retirement`](../canon/terminology.md#retirement) | replacement | modelling and simulation standards |
| [`revision trigger`](../canon/terminology.md#revision-trigger) | a signpost (Chapter 12), which watches the world only | the book's own controlled use |
| [`signal`](../canon/terminology.md#signal) | a value past a threshold | the book's own controlled use, built on statistical process control |
| [`tampering`](../canon/terminology.md#tampering) | drift | **the book's own controlled use**, built on Chapter 13 |

## Terms marked open

- **`utility`** — assigned to Chapter 11, which is drafted and did not define it. There is no later chapter to close it in. See [Decision 0020](../decisions/0020-chapter13-dynamics-terminology-and-boundary.md) clause 12.4.

## Status

Every terminology block from Chapter 2 onward is **provisional**, pending adjudication of the decision record that proposes it.
`../canon/terminology.md` records which record governs which block, and `../README.md` lists them.

