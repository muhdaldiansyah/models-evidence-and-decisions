# Decision 0026: Front Matter and Build

## Status

**PROPOSED (2026-08-19) — awaiting author adjudication.**

The second record written after the drafting phase closed, and the second that is not about a chapter.

`front-matter/`, the `Makefile`, and `tools/` are created by this record and inherit its provisional status.

## Context

Seventeen chapters exist and there is no way to read them as a book.

`README.md` serves a reader well and is not a substitute, because it is a **repository** file: it carries governance, freeze status, decision counts, and a Current State section listing sixteen unadjudicated records. A reader does not want that, and a reader who reads it gets the project's condition instead of the book's argument.

Three things were missing, and one of them is not cosmetic.

**The reader is never told how to work a chapter.** Every chapter opens with an unaided task before it teaches anything, contains exactly three self-explanation pauses, plants five defects to be diagnosed before feedback is opened, and supplies two parallel cold-transfer forms with a rubric that must not be seen before production. **A reader who does not know the concealment discipline destroys the instrument on Chapter 1 by opening the rubric early**, and nothing currently warns them. The method is described in `0008`, which is a governance record, and per chapter at the moment of use, which is too late.

**The reader is not told what has not been established until the last page.** `../chapters/17-deployment-monitoring/chapter.md` §8 states that no exercise has pilot data and that the book makes no transfer claim. That is the right place to end and the wrong place to say it first.

**There is no term index.** `../canon/terminology.md` holds 163 entries and is an authoring instrument — `Field/origin`, `Definition status`, provisional-block warnings. The book announces **six terminology collisions**, one of them four ways on *identifiability*, and a reader meeting the fourth sense has nowhere to look.

## Decision

### 1. `front-matter/`, three files

**1.1** A new top-level directory, sibling to `chapters/`, holding reader-facing material that is not a chapter.

| File | What it is |
|---|---|
| `preface.md` | what the book is, who it is for, what it refuses to do, **and what has not been established** |
| `how-to-use-this-book.md` | the working method, the time it costs, and the concealment discipline |
| `term-index.md` | 163 terms, where each is introduced, what it is distinct from, and every announced collision |

**1.2** Front matter is **manuscript prose** and obeys the writing conventions in `../CLAUDE.md`: plain Pandoc Markdown, one sentence per line, relative paths.

**1.3** It is **not** governed by `../README.md`'s chapter architecture, because it is not a chapter. It may not contradict the README, and where the two overlap the README remains authoritative.

### 2. The preface states the book's condition on its first page

**2.1** That no exercise in the book has pilot data; that no chapter has been reviewed by a subject-matter expert; and that **the book makes no claim to produce transfer.**

**2.2** This duplicates Chapter 17 §8 deliberately. The book's own discipline — a claim carries what it is conditional on — applies to the book.

**2.3** **It is not an apology and is not written as one.** A reader who knows what is unestablished can use the book; one who finds out at the end cannot go back.

### 3. The term index is an index, not a dictionary

**3.1** It gives, per term: the chapter that introduces it, what the book keeps it distinct from, and where its definition lives.

**3.2** **It does not define the terms.** The canon entries carry no definition field, by construction — the book teaches terms in context, and a glossary that re-defined 163 of them out of context would compete with the chapters and drift from them.

**3.3** It is **generated** from `../canon/terminology.md` rather than written alongside it, so it cannot disagree with the registry.

**3.4** **The six collisions get their own section**, because they are the thing an index can do that a chapter cannot: show all four senses of *identifiability* on one screen.

### 4. Build

**4.1** `../decisions/0002` already provides for build configuration appearing "on demonstrated need". Seventeen finished chapters with no way to produce one artifact is that need. **No separate record is opened.**

**4.2** A root `Makefile` with `tools/` holding the Pandoc metadata and two scripts. Targets: `check`, `index`, `html`, `epub`, `docx`, `pdf`, `stats`, `clean`.

**4.2a** **`tools/`, not `build/`.** `.gitignore` already reserves `build/` and `_output/` for artifacts, so a script placed in `build/` would never have been committed. `../decisions/0002` names `tools/` among the structures anticipated on demonstrated need; output goes to `_output/`, which was already ignored.

**4.3** **`make check` is the point of this, not the formats.** It runs the verification suite that has been run by hand at every chapter boundary — bibliography and source-note parity, citation keys resolving, internal links, canon index parity, and the chapter inventory. Codifying it is what stops it from being remembered.

**4.4** **`pdf` will not run on the machine this was written on.** No LaTeX engine is installed; the target detects this and says so rather than failing obscurely. `html` (1.4 MB), `epub` (481 KB), and `docx` (484 KB) were built and inspected: seventeen chapters, front matter, term index, table of contents, 391 block quotes, 112 tables.

**4.4a** **Every format depends on `check`.** A repository that fails verification cannot be built into an artifact.

**4.4b** Command-line metadata overrides the YAML block in each chapter file. Without it the book took its title from whichever chapter compiled last, which was Chapter 17.

**4.5** Chapter order is read from the filesystem in numeric order, not from a hand-maintained list, so a build cannot silently omit a chapter.

### 5. What this record does not do

- Change any chapter, its budget, its exercises, or its governed fields.
- Change `../README.md`'s architecture, parts, or sequence.
- Claim the book is ready to publish, or that any format is typeset.
- Add a bibliography renderer, an index, cross-reference numbering, or figures.
- Resolve any open item in `../README.md`'s Current State.

## Known gaps carried forward

1. **No PDF has ever been produced**, and no typesetting decision has been made.
2. **The bibliography is not rendered.** `--citeproc` is not enabled and no CSL style is chosen, so citations appear in the built artifacts as they appear in the source.
3. **The term index is generated**, so a canon edit silently staleness it until `make` is rerun. There is no check that it is current.
4. **The front matter has been read by nobody**, like the rest of the book.

## Reopen if

- A typesetting decision requires the front matter to change shape.
- The term index is found to compete with the chapters rather than point at them.
- `make check` becomes something people route around rather than run.
