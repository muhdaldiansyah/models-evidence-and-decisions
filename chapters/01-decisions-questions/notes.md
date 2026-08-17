# Chapter 1 Research Notes

Status: accumulated research dossier, superseded in part. Each bounded task below records its own adjudication date and disposition, but the file as a whole has not been consolidated — `freeze-gates.md` lists that consolidation as non-blocking housekeeping.

This file is evidence for decisions, not a statement of them. Where it appears to conflict with a governed artifact, the governed artifact wins: the adjudicated outcomes live in `../../decisions/` (0004–0008), `../../canon/`, and `spec.md`. Do not cite this file as authority.

## Bounded task: intended use, context of use, and adequacy for use

Status: author approved for implementation on 2026-08-15.

This note records the adjudicated result of the first bounded Chapter 1 terminology-research task.
It does not reopen the Chapter 1 architecture, research `target` versus `estimand`, or perform the Chapter 5 verification/validation terminology review.

## Adjudicated principle

Overall adequacy cannot be judged without a stated use.
Some properties, such as internal consistency, dimensional correctness, or numerical correctness, may be assessed independently, but whether a model or analysis is adequate depends on what it will be used for.

## Chapter 1 terminology decisions

- `intended use` is required Chapter 1 vocabulary.
- In modeling and simulation, `intended use` is established terminology.
- Applying `intended use` to analyses, estimates, forecasts, and recommendations is this book's pedagogical synthesis; it is not presented as one universal formal definition across disciplines.
- Use `relevant application context` in ordinary language.
- Formal `context of use (COU)` is established but field-specific in computational-model credibility practice; it is an optional Chapter 1 preview, not memorization material, and its formal home is Chapter 5.
- Use reader-facing wording such as `adequate for the stated intended use` or `adequate for this use`.
- The Chapter 1 use of `adequacy` is disciplined reader-facing language, not one universal standardized adequacy framework.
- Accuracy, validity, validation, applicability, credibility, adequacy, and fitness for purpose are not synonyms.
- Do not adopt `purpose-relative adequacy`.
- Preserve the Chapter 1 versus Chapter 5 boundary: verification, validation, formal COU, applicability, credibility, model risk, validation domains, and framework-specific adequacy assessment remain later material.

## Verified sources promoted for Chapter 1

### `nasa2024models`

National Aeronautics and Space Administration. 2024. *NASA-STD-7009B: Standard for Models and Simulations*. Version B.

Role in Chapter 1:
- establishes `intended use` in modeling and simulation;
- connects intended use to model scope, expected results, decisions informed, and use-specific acceptance criteria.

Verified locators:
- §3, definition of `Intended Use`;
- §4.1;
- §4.1.1.1 [M&S 40];
- §4.1.1.5 [M&S 43];
- file pp. 20–21.

### `nrc2012reliability`

National Research Council. 2012. *Assessing the Reliability of Complex Models: Mathematical and Statistical Foundations of Verification, Validation, and Uncertainty Quantification*. Washington, DC: The National Academies Press.

Role in Chapter 1:
- supports the proposition that required validation accuracy and VVUQ effort depend on the intended application and eventual decision use;
- supports avoiding an abstract, global judgment of model quality detached from the relevant quantity and application.

Verified locators:
- Summary, printed pp. 1–4, especially p. 3;
- Chapter 6, §§6.1–6.2, printed pp. 86–87.

### `fda2023credibility`

U.S. Food and Drug Administration. 2023. *Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions: Guidance for Industry and Food and Drug Administration Staff*.

Role in Chapter 1:
- supports the optional field-specific preview of `context of use (COU)`;
- supports preserving distinctions among accuracy, applicability, credibility, and adequacy;
- supports the intuition that consequences and model influence affect how much credibility evidence is warranted.

Verified locators:
- §IV, Definitions, printed pp. 8–9;
- comparison with ASME V&V 40, printed p. 13;
- §VI.D, `Adequacy Assessment`, printed p. 33.

### `asme2025credibility`

ASME Task Group on VVUQ Concepts in Engineering Education. 2025. *Introduction to VVUQ, Part 1: Simulation Credibility Assessment*. Version 1.

Role in Chapter 1:
- supports the distinction between aspects of numerical verification and broader model validation/credibility judgments;
- supports the optional COU preview and the relevance of intended-use requirements.

Verified locators:
- slides 5–7, especially printed slides 6–7.

## Verified sources not promoted in this bounded implementation

These sources were sufficiently inspected during research but are not needed for the Chapter 1 claims being implemented now.
They remain recorded here rather than being added to `references.bib` or receiving source-note files.

- **Epstein 2008, “Why Model?”** — verified support for plural modeling purposes; not needed for the implemented Chapter 1 terminology claims.
- **ASME 2025, Part 3: Validation** — verified background on intended-use and validation domains and broader model-adequacy considerations; retained for the Chapter 5 handoff rather than promoted now.
- **ISO 9000:2026** — verified primarily as evidence that validation vocabulary differs across traditions; Chapter 1 does not need to make that formal comparison.
- **Commission Implementing Regulation (EU) 2022/1426** — verified primarily as evidence of field-specific technical use of `fit for purpose`; Chapter 1 does not need that example.

## Partially verified authoritative sources

The following authoritative sources were not inspected in full and must not be treated as verified support for exact definitions or clauses:

- **ASME VVUQ 1-2022** — official description inspected; full standard clauses not inspected.
- **ASME V&V 40-2018** — official description inspected; selected terminology was available indirectly through FDA; full standard not inspected.

These remain source leads for the later Chapter 5 terminology review.

## Source leads — full relevant content not inspected

The following works remain explicit source leads and are not promoted:

- Howard, Ronald A. 1988. “Decision Analysis: Practice and Promise.”
- Robinson, Stewart. 2008. “Conceptual modelling for simulation Part I: definition and requirements.”
- Sargent, Robert G. 2013. “Verification and validation of simulation models.”
- Oberkampf, William L., and Christopher J. Roy. 2010. *Verification and Validation in Scientific Computing*.

Promising metadata, abstracts, front matter, or limited previews were inspected, but the full relevant content was not.

## Chapter 5 handoff

Do not execute this handoff as part of Chapter 1 implementation.
Chapter 5 should later verify and adjudicate:

- the complete ASME VVUQ 1-2022 standard;
- the complete ASME V&V 40-2018 standard;
- Oberkampf and Roy;
- Sargent;
- computational versus systems-engineering validation terminology;
- formal COU;
- applicability and credibility;
- validation domains and intended-use domains;
- model risk and consequence-sensitive credibility requirements;
- framework-specific adequacy concepts.

## Implementation boundary

This research result changes terminology control and a small number of Chapter 1 specification statements only.
It does not change the chapter title, central question, core competence, section structure, page or hour budget, worked cases, exercise architecture, transfer target, or the book architecture.

## Bounded task: target and answer specification

Status: author approved for implementation on 2026-08-15.

This note records the adjudicated result of the second bounded Chapter 1 terminology-research task.
It does not reopen the Research 01 decisions on `intended use`, `context of use`, or `adequacy`, perform the later claim-type adjudication, or conduct Chapter 3, Chapter 7, Chapter 9, Chapter 10, or Chapter 11 formal terminology research.

## Adjudicated target principle

`Target` is required Chapter 1 organizing vocabulary, but its book-wide Chapter 1 meaning is a pedagogical synthesis rather than one universal cross-disciplinary technical definition.
At Chapter 1 depth, `target` is the informal organizing word for what an inquiry is trying to determine about a focal entity, unit, population, or system.
Qualify the word whenever possible so that the following noun carries the substantive meaning, for example target quantity, event, state, outcome, comparison, population, or system.

A minimally usable target specification states:

1. who or what the answer concerns; and
2. what about it is being sought, such as a quantity, event, state, outcome, relationship, comparison, or consequence.

Add conditions, relevant application context, horizon, resolution or aggregation, comparison or reference condition, target population, required answer form, or a threshold only when omission could materially change the meaning of the question.
Do not teach those qualifiers as a universal checklist.

The Chapter 1 diagnostic heuristic is the book-specific **same-question test**: ask whether omitting or changing a qualifier could cause two competent analysts to answer materially different questions while both believing they had answered the prompt.
This heuristic is pedagogical synthesis, not an established disciplinary rule.

## Relationship to Research 01

Keep four questions distinct:

- `intended use`: What will the answer be used for?
- `target`: What is the inquiry trying to determine, and about whom or what?
- `relevant application context`: Under what relevant conditions does that target apply?
- `adequacy for the stated intended use`: Is the resulting answer good enough for the use?

A target can remain the same while intended use changes, and intended use can remain the same while the target changes.
Target specification alone does not establish adequacy.

## Terminology decisions

- `target` is required informal Chapter 1 vocabulary and should be qualified whenever possible.
- The book-wide Chapter 1 sense of `target` is pedagogical synthesis because disciplinary uses differ materially.
- `target quantity` is useful ordinary qualifying language when the sought object is literally a quantity; it is not a synonym for `estimand`.
- `target population` is an established qualified term for population-based questions and is distinct from the observed sample and the data-collection setting.
- `estimand` is a concept preview only in Chapter 1; the term is not required. Formal treatment belongs to Chapter 7.
- `estimator` and `estimate` remain Chapter 8 terms and must remain distinct from `estimand`.
- `question of interest`, `quantity of interest`, `measurand`, `endpoint`, `response variable`, `prediction target`, `label`, and optimization terminology remain field-specific and do not become Chapter 1 umbrella vocabulary.
- Do not introduce `answer target` or formalize `target context` as new controlled vocabulary.
- Preserve all existing distinctions among target, construct, measure, operationalization, proxy, estimand, estimator, estimate, decision, objective, and metric.
- Preserve the settled distinctions among statistical identifiability, causal identification, and structural identifiability.

## Verified sources promoted for Research 02

### `fda2021estimands`

U.S. Department of Health and Human Services, Food and Drug Administration, Center for Drug Evaluation and Research, and Center for Biologics Evaluation and Research. 2021. *E9(R1) Statistical Principles for Clinical Trials: Addendum: Estimands and Sensitivity Analysis in Clinical Trials. Guidance for Industry.*

Role in Chapter 1:
- supports separating a target of estimation from the method of estimation and from the numerical result;
- supports keeping estimand, estimator, and estimate distinct;
- supports the Chapter 1 preview that a later target of estimation may require more structure than naming an endpoint.

Verified locators:
- §I, printed p. 1;
- §II A.2, printed p. 4;
- §III A.3, printed p. 5;
- §III.C A.3.3, printed pp. 9–10;
- Glossary, printed p. 19.

Caution: the ICH treatment-effect definition is authoritative for its clinical-trial context and is not adopted as the book's universal formal definition of `estimand`.

### `jcgm2012vim`

Joint Committee for Guides in Metrology. 2012. *International Vocabulary of Metrology — Basic and General Concepts and Associated Terms (VIM)*, 3rd edition. JCGM 200:2012.

Role in Chapter 1:
- supports distinguishing the quantity intended to be measured from the quantity actually measured;
- supports the structural point that the sought object is not automatically identical to the available recorded variable.

Verified locators:
- §2.3, `measurand`;
- Note 1 and Note 3 to §2.3;
- §2.34, `target measurement uncertainty`.

Caution: `measurand` remains field-specific measurement terminology and is not a synonym for the book's Chapter 1 `target`.

### `censusndtargetpopulation`

U.S. Census Bureau. *Appendix D3-A: Requirements for Calculating and Reporting Response Rates: Demographic Surveys and Decennial Censuses.* Census Bureau Statistical Quality Standards appendix.

Role in Chapter 1:
- supports `target population` as an established qualified term;
- supports distinguishing the population about which estimates or inference are intended from sampled units and the observed sample.

Verified locator:
- §1.1, `Eligibility Status`, especially the target-population definition and sample-unit eligibility discussion.

The inspected page did not state a publication year, so the bibliography does not invent one.

## Existing promoted sources reused for Research 02

### `nrc2012reliability`

Research 02 reuses the already-promoted National Research Council source for the direct point that quantities of interest must be specified for VVUQ questions to be well posed and that relevant quantities depend on application and decision.

Additional Research 02 locators inspected:
- Summary, printed pp. 2–4;
- Chapter 2, §2.1, printed pp. 19–20;
- Chapter 5, §5.1 and related validation discussion;
- Appendix A Glossary, printed pp. 116–118, especially `quantity of interest` on p. 117.

### `fda2023credibility`

Research 02 reuses the already-promoted FDA computational-model guidance for its field-specific distinction between `question of interest` and `quantity of interest` and for keeping the model context of use separate from the substantive question.

Additional Research 02 locators inspected:
- Definitions, printed p. 10;
- §VI.A.(1), `Question of Interest`, printed p. 15;
- §VI.A.(2), `Context of Use`, beginning printed p. 16.

These terms remain optional field-specific examples, not the Chapter 1 umbrella vocabulary.

## Verified contextual sources not promoted

The following sources were inspected and useful as cross-disciplinary checks but are not needed as repository-level support for the implemented Chapter 1 claims, so Decision 0003 does not justify promoting them now:

- NIST/SEMATECH *e-Handbook of Statistical Methods* — contextual support for response/dependent-variable and parameter language in statistical modeling.
- scikit-learn glossary — contextual support that supervised machine learning commonly uses `target`, `y`, outcome, response, ground truth, or label for closely related roles.
- Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed. — contextual support for defining the series and horizon of a forecast rather than relying on a generic target term.
- Boyd and Vandenberghe, *Convex Optimization* — contextual support that optimization uses an objective function rather than a generic inquiry target.
- Society of Decision Professionals, `Decision Quality` — contextual support for distinguishing framing, information, alternatives, values, reasoning, and action in decision work.

These remain contextual evidence in the Research 02 dossier and are not added to `references.bib` or `sources/` by this implementation.

## Partially verified source

- Hernán, Miguel A., and James M. Robins. 2016. “Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available.” *American Journal of Epidemiology* 183(8):758–764. DOI 10.1093/aje/kwv254.

Publisher metadata and abstract were verified, but the relevant full text was not directly inspected to the standard required for a load-bearing source note.
Do not promote or cite it as verified support from this task.

## Source leads — full relevant content not inspected

- Howard, Ronald A. 1988. “Decision Analysis: Practice and Promise.”
- Hernán, Miguel A., and James M. Robins. 2020. *Causal Inference: What If.*

These remain source leads only and are not promoted.

## Chapter boundaries and later handoffs

### Chapter 2

Own detailed system/model boundaries, representation, abstraction, scale, and the formal question of what belongs inside a representation.
Chapter 1 may name a target system but does not teach the representation machinery.

### Chapter 3

Own construct, measure, operationalization, proxy, validity, reliability, and formal measurement-error distinctions.
Later work may decide whether `measurand` is useful in the book's measurement treatment.
Chapter 1 only insists that the sought target is not automatically identical to what was measured or recorded.

### Chapter 7

Own formal targets and estimands, statistical identifiability, causal identification, intervention and counterfactual target specification, causal graphs, and identification strategies.
The broader book-wide formal definition of `estimand` remains provisional pending that research.

### Chapter 8

Own estimators, estimates, likelihood, regression, uncertainty quantification, predictive evaluation, and statistical model checking.

### Chapter 9

Own target population versus source or study population, generalizability, transportability, external validity, and any later adjudication of `target context` terminology.
Chapter 1 uses `relevant application context` in ordinary language rather than formalizing `target context`.

### Chapters 10–11

Chapter 10 owns values, objectives, metrics, constraints, and alternative generation.
Chapter 11 owns formal decisions under uncertainty, sensitivity, value of information, and later treatment of decision thresholds.
A decision or recommendation must remain distinct from the informational targets that support it.

## Open questions retained for later work

- What general statistical definition of `estimand` should the book adopt in Chapter 7 beyond the verified ICH clinical-trial usage?
- How should Chapter 7 and Chapter 9 distinguish target population, study/source population, and transport/generalization concepts?
- Should `target context` ever become a formal later term, or should the book continue using more specific transportability vocabulary plus ordinary `relevant application context`?
- When is a decision threshold part of the substantive question and when is it an adequacy or decision criterion? This boundary belongs to later decision-analysis work.
- Does the Chapter 1 same-question test reliably help learners add material qualifiers without turning target specification into a checklist? This requires pedagogical testing, not more terminology invention.

## Research 02 implementation boundary

This implementation changes target-related terminology control, source provenance, and narrowly scoped Chapter 1 specification wording only.
It does not change the chapter title, central question, six-section architecture, 24-page / 4-hour budget, hospital anchor, pendulum or student-assessment contrasts, exercise progression, transfer intent, or the book architecture.
It does not perform the later claim-type, measurement, estimand, identification, transportability, value, or decision-theory research tasks.

## Bounded task: positive and normative questions

Status: author approved for implementation on 2026-08-15.

This note records the adjudicated result of the third bounded Chapter 1 terminology-research task.
It does not reopen Research 01 (`intended use`, `context of use`, `adequacy`) or Research 02 (`target` and answer specification), and it does not perform the later full association/prediction/intervention/counterfactual adjudication or formal Chapter 10–11 value and decision-theory work.

## Adjudicated positive/normative principle

Chapter 1 should begin in ordinary language with the distinction between:

- what is, was, or would happen; and
- what should count as better, acceptable, important, or preferable, or what should be done.

It should then introduce `positive` and `normative` as established but discipline-sensitive labels.
The labels apply to components or subquestions, not to mutually exclusive classes of entire problems.

A positive component asks what is, was, or would happen under specified conditions.
Positive inquiry is broader than description: predictive, interventional, and counterfactual questions can also be positive when they ask what would happen.

A normative component asks what should matter, what should count as better or acceptable, or what should be done.
Normative reasoning is not synonymous with unsupported opinion.

A recommendation may depend on evidence or models about consequences plus evaluative or decision premises about how those consequences should be judged.
Chapter 1 should make that bridge explicit rather than presenting a recommendation as if it followed from evidence alone.

## Terminology decisions

- `positive` and `normative` are required Chapter 1 vocabulary after an ordinary-language contrast.
- Use them primarily for components or subquestions rather than for exclusive whole-problem classification.
- Do not teach `positive = descriptive`; positive questions may also be predictive, interventional, or counterfactual.
- Do not teach `positive = fact`, `positive = objective`, or `positive = value-free`.
- Do not teach `normative = subjective opinion`.
- Do not require `prescriptive` in Chapter 1 and do not use it as a synonym for `normative`; decision theory may use the term more specifically later.
- Keep predicted consequences distinct from their evaluation.
- When a recommendation is made, expose the material evaluative premise, objective, obligation, constraint, or commitment required to move from consequence claims to action.
- Formal ethics, value structuring, objectives, preference representation, utility, trade-off elicitation, and decision rules remain later material.

## Verified sources promoted for Research 03

### `keynes1891scope`

John Neville Keynes. 1891. *The Scope and Method of Political Economy*. London: Macmillan and Co.

Role in Chapter 1:
- establishes paired `positive` and `normative` terminology in the economics tradition;
- supports the introductory distinction between what is and criteria concerning what ought to be.

Verified locator:
- printed p. 34.

Caution: the book's cross-disciplinary Chapter 1 transfer is a cautious pedagogical extension, not a claim that Keynes supplies a universal modern taxonomy.

### `bradley2016structured`

Patricia Bradley et al. 2016. *Application of a Structured Decision Process for Informing Watershed Management Options in Guánica Bay, Puerto Rico*. U.S. Environmental Protection Agency. EPA/600/R-15/248.

Role in Chapter 1:
- supports separating facts/evidence, values/objectives, alternatives, consequences, trade-offs, and decision;
- supports the warning that evidence about consequences does not by itself state how those consequences should be valued.

Verified locators:
- Executive Summary, printed p. xiii;
- Chapter 2 formal decision-process discussion beginning printed p. 5;
- EPA Science Inventory publication record for report metadata and 2016 publication year.

Caution: the EPA structured-decision process is not adopted as the book's universal decision framework.

## Verified direct/contextual sources not promoted

The following sources remain in the Research 03 dossier but are not required for the Chapter 1 claims implemented now, so Decision 0003 does not justify adding them to the canonical bibliography in this bounded change:

- David Hume, *A Treatise of Human Nature*, Book III, Part I, Section I — verified direct support for the warning against silently moving from `is` to `ought`; Chapter 1 does not need to teach or name an `is–ought gap`.
- National Academies of Sciences, Engineering, and Medicine, 2026, *Advancing the Art and Science of Decision-Making: A Guide* — verified direct support for a facts/values/evidence/consequences/decision sequence; redundant for the implemented claims once the EPA source is promoted.
- Milton Friedman, 1953, “The Methodology of Positive Economics” — verified contextual support that positive economics includes prediction of consequences; not needed because Chapter 1 can state the broader-than-descriptive point as part of the adjudicated introductory synthesis while Research 04 later formalizes claim types.
- Bell, Raiffa, and Tversky, 1988 — verified from official metadata and substantive chapter summary for the field-specific descriptive/normative/prescriptive distinction; full chapter not inspected, and Chapter 1 only needs the caution not to adopt `prescriptive`.
- Heather Douglas, 2000, “Inductive Risk and Values in Science” — verified contextual caution against equating positive analysis with universally value-free scientific practice; Chapter 1 does not need a philosophy-of-science detour.

## Chapter boundaries and later handoffs

### Research 04 / Chapters 6–7

The later association/prediction/intervention/counterfactual research must preserve the orthogonality established here.
Description, association, prediction, intervention effects, and counterfactual comparisons can all be positive when they ask what is or would happen.
Research 03 does not adjudicate their formal definitions.

### Chapter 10

Own formal value structuring, objectives, stakeholders, alternatives, measurable attributes or metrics, and trade-off structure.
Chapter 1 only exposes material evaluative premises and affected stakeholders at practical depth.

### Chapter 11

Own formal choice under uncertainty, expected utility, risk attitudes, sensitivity analysis, value of information, and decision quality.
Chapter 1 does not calculate a decision rule.

## Open questions retained for pilot or later research

- Does ordinary-language-first instruction prevent readers from misreading `positive` as favorable or `normative` as normal?
- Can readers keep positive inquiry broader than description once prediction/intervention/counterfactual vocabulary is introduced?
- Do learners expose material evaluative premises behind recommendations without turning the task into a values checklist?
- If later decision theory uses `descriptive`, `normative`, and `prescriptive` in a specialized sense, how should that specialization be signposted without destabilizing Chapter 1 usage?

## Research 03 implementation boundary

This implementation changes positive/normative terminology control, source provenance, and narrowly scoped Chapter 1 specification wording only.
It does not change the chapter title, central question, core competence, six-section architecture, 24-page / 4-hour budget, anchor cases, exercise progression, transfer intent, or the book architecture.
It does not perform Research 04 or formal Chapter 10–11 value and decision-theory research.
