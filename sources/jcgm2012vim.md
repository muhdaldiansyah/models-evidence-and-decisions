# `jcgm2012vim`

## Bibliographic record

Joint Committee for Guides in Metrology. 2012. *International Vocabulary of Metrology — Basic and General Concepts and Associated Terms (VIM)*, 3rd edition. 2008 version with minor corrections. JCGM 200:2012.

DOI: 10.59161/JCGM200-2012

Official interactive text: https://jcgm.bipm.org/vim/en/

## Verification status

Verified against the relevant official VIM entries and BIPM metadata during Chapter 1 Research 02: Target and Answer Specification.

## Locators and direct support

- §2.3, `measurand`.
- Note 1 and Note 3 to §2.3.
- §2.34, `target measurement uncertainty`.

The VIM defines the measurand as the quantity intended to be measured, indicates that its specification includes the kind of quantity and relevant state or carrier conditions, and warns that the quantity actually measured can differ from the intended measurand.
It also treats target measurement uncertainty as selected on the basis of intended use.

## Chapter 1 use

Direct support for the structural distinction between the thing an inquiry seeks and the variable or quantity actually measured or recorded.
The field-specific term `measurand` is not required Chapter 1 vocabulary; formal measurement terminology remains Chapter 3 material.

## Role in Chapter 3

This is Chapter 3's metrology-side source. It supplies standards-backed definitions that defeat two of the chapter's target collapses outright: precision is not accuracy, and error is not only noise.

Chapter 1 deferred `measurand` and formal measurement vocabulary to Chapter 3. That deferral is now taken up.

### Verified locators added during Chapter 3 research (2026-08-18)

Entries consulted through the official interactive VIM at `https://jcgm.bipm.org/vim/en/`.

- **§2.13, `measurement accuracy`** — "closeness of agreement between a measured quantity value and a true quantity value of a measurand". Note 1: measurement accuracy **is not a quantity and is not given a numerical quantity value**; a measurement is said to be more accurate when it offers a smaller measurement error. Note 2: the term should not be used for measurement trueness, nor for measurement precision, although it relates to both.
- **§2.14, `measurement trueness`** — "closeness of agreement between the average of an infinite number of replicate measured quantity values and a reference quantity value". Trueness **is not a quantity** and is not expressed numerically; ISO 5725 supplies measures of closeness of agreement. Trueness is **inversely related to systematic measurement error** but is **not related to random measurement error**. "Measurement accuracy" should not be used for trueness.
- **§2.15, `measurement precision`** — "closeness of agreement between indications or measured quantity values obtained by replicate measurements on the same or similar objects under specified conditions". Precision **is** expressed numerically, by measures of imprecision such as standard deviation, variance, or coefficient of variation. Specified conditions may be repeatability, intermediate precision, or reproducibility conditions (ISO 5725-1:1994). The entry cautions that "measurement precision" is sometimes **erroneously** used to mean measurement accuracy.
- **§2.16, `measurement error`** — "measured quantity value minus a reference quantity value". Note 1 distinguishes the case where a single reference value exists (through calibration against a standard of negligible uncertainty, or a conventional value), making the error known, from the case where the measurand is taken to have a unique true value, making the error unknown. Note 2: measurement error **should not be confused with production error or mistake**. Systematic measurement error (§2.17), measurement bias (§2.18), and random measurement error (§2.19) are separate entries.
- **§2.3, `measurand`** and **§2.34, `target measurement uncertainty`** — as recorded above for Chapter 1.

## Author synthesis / caution

Do not use `measurand` as a general synonym for the book's Chapter 1 `target`.
The Chapter 1 umbrella use of `target` is pedagogical synthesis precisely because other disciplines have their own more specific terms.

### Chapter 3 cautions

- **The VIM is a metrology vocabulary.** Its definitions are stated for physical measurement with reference standards and traceability. Chapter 3 also treats constructs that have no reference standard — service adequacy, need, capability — and there the VIM's `true quantity value` and `reference quantity value` have no straightforward counterpart. Where the chapter pairs this source with `adcock2001validity`, it must not imply that metrology and social-science measurement share one vocabulary. They share a structure; they do not share a standard.
- Do not present `accuracy` as something that can be reported as a number. Note 1 to §2.13 is explicit that it cannot.
- Do not teach measurement uncertainty evaluation, the GUM framework, coverage intervals, or traceability chains. Uncertainty quantification is Chapter 8; adequacy criticism is Chapter 5.
- Do not use §2.16 to imply that error is always knowable. Its Note 1 makes knowability conditional on a reference value existing.
- The VIM's own usage notes record that several of these terms are widely misused in practice. Chapter 3 may say the misuse is common; it may not attribute a claim about how common to this source.
