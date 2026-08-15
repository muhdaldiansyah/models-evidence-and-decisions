# CLAUDE.md — Operating Contract

This repository develops the book *Models, Evidence, and Decisions: An Integrated Course in Reasoning Under Uncertainty*.
This file is the operating contract for AI agents and human collaborators.

## Authority order

```text
README.md
↓
decisions/
↓
canon/
↓
chapter spec.md
↓
working files and manuscript
```

- `README.md` controls the book architecture (parts, chapters, sequence, freeze status).
- Decision records in `decisions/` explain why settled decisions exist and when they may be reopened.
- `canon/` controls terminology and the labeling of pedagogical syntheses.
- Each chapter's `spec.md` controls that chapter's scope.
- Lower-level files may not silently contradict higher-level authority. Conflicts are surfaced, not silently resolved.
- Chapter title, central question, and core competence must remain synchronized between `README.md` and the corresponding `spec.md`; README remains authoritative for the book-level architecture.

## Intellectual rules

- Use established terminology where established terminology exists.
- Do not invent umbrella terminology merely for elegance.
- Preserve disciplinary distinctions (see `canon/terminology.md`).
- Pedagogical synthesis must be labeled as pedagogical synthesis (see `canon/pedagogy.md`).
- Specialist machinery intentionally deferred to the depth curriculum must not silently expand into the core book.
- Do not casually reopen architecture; reopening conditions live in `decisions/`.

## Source discipline

- No fabricated citations. No fabricated citation keys. Every citation key must exist in `references.bib`.
- Factual/load-bearing claims eventually require `[@citekey, locator]` or an explicit `<!-- TODO-cite: ... -->` marker.
- Primary-source claims should preferably be verified against the primary source; otherwise cite "as cited in".
- Never convert a TODO-cite into a verified citation without checking the actual source.

## Writing conventions

- Plain Pandoc-compatible Markdown; no tool-specific shortcode or transclusion syntax yet.
- One sentence per line in manuscript prose.
- Relative paths for all internal references.
- Keep Git diffs clean: scoped commit messages (`ch07: ...`, `canon: ...`, `decisions: ...`, `sources: ...`).

## AI behavior

- AI may propose changes; architectural changes must be surfaced for review, never silently applied.
- Canonical files (`README.md`, `decisions/`, `canon/`, frozen `spec.md`) require deliberate human review before change.
- Do not create large new systems or top-level directories without demonstrated need (see `decisions/0002`).
