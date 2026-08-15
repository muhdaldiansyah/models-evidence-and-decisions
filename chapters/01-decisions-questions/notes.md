# Chapter 1 Research Notes

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
