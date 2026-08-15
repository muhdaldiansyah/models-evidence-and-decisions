# Decision 0002: Repository Architecture

## Status

Accepted (2026-08-15)

## Decision

The repository is manuscript-centric with a thin global knowledge layer.

- `chapters/NN-slug/` holds chapter-scoped material: `spec.md` (the contract), and later `notes.md`, `chapter.md`, `exercises.md`, `figures/`.
- Reusable knowledge gets exactly one global home: `references.bib`, `sources/` (one note per source, named by citation key), `canon/` (terminology, pedagogy), `cases/` (recurring cases), `decisions/`.
- The manuscript remains the center of gravity; every other artifact must make it more correct, more checkable, or easier to write.
- No duplication: each fact type has one authoritative home (see `CLAUDE.md` authority order).
- No empty systems: directories and files appear when their first real content exists.
- Mature structures (`computation/`, `tools/`, build configuration, exercise bank, topic notes) appear incrementally on demonstrated need.

This scaffold intentionally creates all 17 chapter `spec.md` skeletons now so the full chapter framework is visible on GitHub; manuscript, research, and exercise files remain deferred until actual work begins.

## Why

Chapter-local working sets keep writing and AI-assisted sessions bounded, while global single-home knowledge prevents source-note duplication, bibliography drift, and terminology/case inconsistency over a multi-year project.

## Rejected alternatives

- Fully chapter-local architecture (per-chapter source notes and bibliographies): duplicates sources across chapters and makes the bibliography unmaintainable at publication.
- Atomic-note / Zettelkasten / claim-database architecture: maximal provenance on paper, but note-gardening and ledger maintenance displace writing, and abandoned ledgers give false confidence.

## Reopen only if

- The two-plane model demonstrably obstructs drafting or provenance in practice.
