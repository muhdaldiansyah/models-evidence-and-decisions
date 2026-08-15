# Decision 0003: Citation and Source-Note System

## Status

Accepted (2026-08-15)

## Decision

- One global `references.bib` is the canonical bibliographic store. There are no per-chapter bibliographies; per-chapter reference lists, if ever wanted, are a build-time rendering.
- Citation keys are human-readable: `authoryearkeyword`, lowercase (e.g. `box1976science`). A key becomes stable once used in manuscript prose.
- Manuscript citations use Pandoc syntax: `[@key]`, `[@key, p. 12]`. Locators appear in manuscript citations for source-specific claims.
- Source notes (when reading begins) live at `sources/<citekey>.md`; the source note and the bibliography entry share the same key.
- Source-note files distinguish quoted material (blockquotes with page locators) from author interpretation (plain text).
- No standalone claim database by default. Load-bearing claims are managed through inline citations, explicit `TODO-cite` markers, and chapter research dossiers (`notes.md`).

## Why

One identifier threads bibliography entry ↔ source note ↔ inline citation, making provenance a filename lookup rather than a database query.
Pandoc syntax plus BibTeX keeps every candidate publication toolchain (Pandoc, Quarto, LaTeX, Typst, mdBook) open.
Readable keys let humans and AI sanity-check citations in passing.

## Rejected alternatives

- Per-chapter bibliographies (publication-time dedupe nightmare).
- Opaque numeric keys (hide citation errors).
- A standalone claim ledger/database (maintenance cost exceeds value for a 500-page book; its benefits are preserved by cite-or-TODO-cite plus chapter dossiers).

## Reopen only if

- The Phase-4 toolchain cannot consume this format, or key collisions become unmanageable.
