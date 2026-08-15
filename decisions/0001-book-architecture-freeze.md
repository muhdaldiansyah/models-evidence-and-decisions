# Decision 0001: Book Architecture Freeze

## Status

Accepted (2026-08-15)

## Decision

The book is organized as 5 parts and 17 chapters, exactly as specified in `README.md`. The decisive structural choices:

- 5 parts, 17 chapters, in the README order.
- Formulation (Part I) comes before formal probability and inference (Part II).
- Measurement (Ch. 3) is distinct from observation processes and data provenance (Ch. 4).
- Target/estimand specification precedes identification analysis.
- Identification precedes estimation as the working sequence.
- Evidence synthesis and transport receive a dedicated chapter (Ch. 9).
- System dynamics (Ch. 13) is separated from sequential decision and control (Ch. 14).
- Strategic response (Ch. 15) is separate from non-strategic dynamics.
- AI systems are an integration case (Ch. 16), not a standalone intellectual chapter.
- Integration (Ch. 16) is separated from deployment, monitoring, and revision (Ch. 17).
- Established disciplinary terminology is preserved; distinctions are never casually collapsed.
- This architecture is effectively frozen for drafting.

## Why

The book's differentiation is formulation-before-technique and the interfaces between disciplines.
The sequence mirrors where reasoning errors actually enter: formulation and identification failures precede and dominate estimation failures.
Separating measurement from observation processes, dynamics from control, and strategy from dynamics preserves distinctions the source disciplines treat as fundamental.

## Rejected alternatives

- Technique-first or discipline-by-discipline organization.
- Merging dynamics with sequential control, or strategy with dynamics.
- A standalone AI chapter.
- Treating the reasoning sequence as a formal theory rather than a teaching order.

## Reopen only if

- Evidence that the formulation-first sequence materially harms learning.
- Evidence that identification-before-estimation materially harms competence without reducing identification errors.
- A chapter cannot sustain its promised competence within its scope.
- Drafting reveals a real dependency failure between chapters.
- A genuinely superior competing architecture emerges and eliminates the book's differentiation.

Ordinary drafting difficulty is not a reopening condition.
