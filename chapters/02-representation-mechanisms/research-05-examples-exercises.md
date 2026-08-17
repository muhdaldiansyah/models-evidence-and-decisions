# Research 05 — Example and Exercise Architecture

Status: bounded design dossier. Proposals for author adjudication; **not** author decisions.

Cluster R05 of `research-plan.md` §8. Written after the provisional adjudication recorded in `decisions/0009-chapter2-representation-terminology-and-boundary.md`, whose vocabulary it uses throughout. As §8 anticipates, this dossier is mostly design comparison rather than new conceptual literature research.

## 1. Q1–Q2 — Anchor case selection

### The requirement

`readiness-audit.md` §7 requires an anchor that "permit[s] several defensible representations of the **same focal system** at different boundaries or grain, with visible consequences for what can be answered," exposing boundary, entities and variables, mechanism, state, aggregation or scale, and alternative representations — while avoiding a case whose real difficulty is measurement validity, provenance, causal identification, optimization, or formal control.

### Candidates considered

| Candidate | Strength | Fatal or serious weakness |
|---|---|---|
| Building thermal model | Thermal mass is literally storage → clean `state`; zone averaging → clean aggregation failure | Pulls hard toward Chapter 13 dynamics; reads as an engineering exercise |
| Bus route with bunching | Vivid, intuitive, genuine proposable mechanism | Bunching **is** a feedback phenomenon; anchoring on it preempts Chapter 13 |
| School-district assignment | Excellent aggregation and organizational scale | Weak on `state` and on mechanism |
| Hospital emergency department | Rich representations | Its real difficulty is queueing — Chapter 12 |
| **Chapter 1 water utility, extended to the distribution network** | See below | Requires new synthetic facts, which inherit Chapter 1's open SME gate |

### Recommendation: recur the Chapter 1 water utility, at the network

`readiness-audit.md` §7 names this option explicitly — recurrence is permitted "only if Chapter 2 adds a genuinely new operation (for example, comparing storage-only, treatment-and-demand, and network-level representations)."

The new operation is available and it is the chapter's thesis in miniature:

> Chapter 1 represented the utility as **one tank** with an inflow and one demand number. That representation was **adequate** for Chapter 1's question — will usable storage breach the operating reserve within seven days? It is **inadequate** for a different question — if we must restrict, who loses service first?

The same representation, adequate for one purpose and inadequate for another. That is precisely the structure of the verified Levins passage (`levins1966strategy` p. 422): Haldane, Fisher and Wright's constant-environment assumption was legitimate for their question and is not legitimate for today's. Chapter 2's anchor and its strongest source teach the identical lesson.

### What the extended anchor exposes

| Chapter 2 element | How the anchor exposes it |
|---|---|
| Boundary | Are the pipes inside? the pumps? the customers' behaviour? the neighbouring utility's interconnection? |
| Entities and roles | Tanks, pump stations, pressure zones, customer classes — and which are carried forward, acted on, or observed |
| State | Stored volume per zone: what must be carried forward to answer what comes next |
| Mechanism | Elevation + pumping + demand → pressure at a node: drawable, **proposed**, not established |
| Abstraction vs idealization | Omitting pipe friction (silence) versus assuming instantaneous, lossless transfer (assertion of falsehood) |
| Aggregation | One demand number hides that the hilltop zone fails while total storage is still adequate — **arithmetically demonstrable on the page** |
| Grain and scale | Single tank / three pressure zones / node-level |
| Alternative representations | Storage-only, treatment-and-demand, and network — each answering a different question |

The aggregation row is the one that discharges Decision 0009 clause 6.3, which requires the failure to be demonstrated rather than cited. A reader who can add can verify it.

### Cost of the recommendation, stated plainly

Chapter 2 needs **new synthetic facts** — pressure zones, elevations, per-zone demand — that Chapter 1's frozen `case-data.md` does not contain. Consequences:

1. Chapter 2 requires its own governed case-data file.
2. Those facts inherit Chapter 1's **open SME gate**. The Chapter 1 freeze tracker records Gate 1 as OPEN; Chapter 2's extension cannot be more validated than the case it extends.
3. If SME review forces a mechanism change to the Chapter 1 anchor, Chapter 2's extension may need revision too.

This coupling is a real risk and is recorded rather than hidden. The alternative — a fresh anchor — costs the reader a second domain and forfeits the adequate-then-inadequate demonstration, which no fresh case can provide.

## 2. Q4 — Short contrasts

Each contrast isolates **one** representation choice. None is allowed to carry two.

### C1 — Pendulum: same object, two purposes

Deliberate recurrence from Chapter 1, which used the pendulum to show that intended use changes adequacy. Chapter 2 performs a **new operation** on it: showing what changes *inside* the representation.

- To answer *how long is one swing*: length and gravity. Air resistance omitted.
- To answer *why does it eventually stop*: air resistance and pivot friction are now the whole point.

Same object, two entity sets, both correct. Cheapest possible demonstration that content follows purpose. Cost: two sentences.

### C2 — Aggregation, verifiable in three lines

A contrast in which an average is adequate for one decision and hides the deciding fact for another. Must be arithmetic the reader can check without a calculator, per Decision 0009 clause 6.3.

Design constraint: the aggregate must be **genuinely fine** for the first purpose. If the average is simply wrong, the contrast teaches "averages are bad" rather than "adequacy is purpose-relative."

### C3 — A drawable mechanism that establishes nothing

Non-technical and non-numeric. Proposed shape: customers who use a loyalty app spend more. The reader can draw a mechanism — app → reminders → more visits → more spend — and can equally draw its reverse: frequent spenders are the ones who bother to install the app.

Both are drawable. Neither is established. This is the cleanest available demonstration of Decision 0009 clause 3.4, and it hands off to Chapter 7 without teaching any of Chapter 7's machinery.

### Contrasts deliberately not used

`readiness-audit.md` §7 warns against examples chosen for visual appeal. Rejected: predator–prey (pulls to dynamics), traffic (pulls to feedback), epidemic models (pulls to Chapter 6 and to causal identification).

## 3. Q3 — Recurrence policy

Recur: the water utility (new operation — network), the pendulum (new operation — entity set).

Do **not** recur: the student-assessment contrast from Chapter 1. Its interest is measurement validity, which is Chapter 3. Reusing it here would invite exactly the boundary violation the readiness audit warns about.

## 4. Q5 — Cold-transfer forms

### Design constraints inherited

From `decisions/0005` and `chapters/01-decisions-questions/transfer.md`, the Chapter 1 pattern is two parallel forms — one mainly physical, one institutional — requesting the same core outputs, scored on the same dimensions, with all domain facts supplied.

Chapter 2 should keep that pattern and must **avoid every Chapter 1 domain**: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment. A reader doing both chapters' transfer tasks must not meet a repeated domain.

### Proposed forms

**Form A — regional blood supply** (physical / logistical).
Units have shelf life, so something accumulates and expires — a natural `state`. Blood types are heterogeneous, so total units can be adequate while one type is short: the aggregation failure is vivid and checkable. Boundary questions are real: donors, testing laboratory, transport, hospitals. A mechanism is drawable — donation, testing, storage, issue — and is not thereby established.

**Form B — a city rental-assistance programme** (institutional).
Applications accumulate as a backlog, which is the `state`. Total budget can be adequate while need concentrates in one district — the same aggregation structure as Form A, in institutional clothing, which is what makes the forms parallel rather than merely different. Boundary: are landlords inside the representation? Mechanism: application, review, award, payment.

### Why these two are parallel

Both require: two representations for two stated purposes; an explicit boundary with one defended inclusion and one defended exclusion; identification of what must be carried forward; one drawn mechanism with its epistemic status stated; one aggregation that would hide something decision-relevant.

The **structural** demands are identical. Only the surface domain differs. That is what makes them usable as parallel forms and delayed retest, per `decisions/0005`.

### The Chapter 2 transfer target

Chapter 1's transfer target is a first-pass analysis. Chapter 2's is different and must not be confused with it:

> Given an unfamiliar system and **two different stated purposes**, construct two defensible representations, state what each includes and excludes and why, and identify one simplification that is acceptable under the first purpose and unacceptable under the second.

The last clause is the discriminating one. A reader who produces two representations but cannot name a simplification whose verdict *flips* between purposes has not demonstrated the chapter's competence — they have merely produced two drawings.

## 5. Exercise progression

Following the scaffold governed by `decisions/0008`, which is book-wide rather than Chapter-1-specific:

1. **Opening attempt** — represent the utility for a stated purpose, unscaffolded, before any Chapter 2 vocabulary.
2. **Worked comparison** — the three water representations, fully worked, with reasoning transitions exposed.
3. **Self-explanation pauses** — placed at boundary choice, at the aggregation failure, and at the mechanism's epistemic status.
4. **Faded case** — the pendulum and the loyalty-app contrasts, with prompts reduced.
5. **Error diagnosis** — a supplied representation containing planted defects (see below).
6. **Cold transfer** — Form A or Form B.
7. **Retrieval** — reconstruct the representation checklist from memory.
8. **Delayed retest** — the other form.

### Planted defects for the diagnosis task

Each maps to one high-risk collapse from `readiness-audit.md` §5:

| Planted defect | Collapse it targets |
|---|---|
| A representation defended as "more realistic" with no purpose stated | detail = realism = adequacy |
| A drawn mechanism whose caption says the effect is established | mechanism = causal effect |
| An aggregate that hides a decision-relevant difference | aggregation harmless |
| A boundary drawn at a physical edge rather than an analytical one | boundary = physical edge |
| A quantity called `state` that is recomputable from others | state = any variable |

Five defects, five collapses, all diagnosable without domain expertise.

## 6. Open design questions for the author

1. Accept the water-network recurrence, given that it couples Chapter 2 to Chapter 1's open SME gate?
2. Are three self-explanation pauses right for a 6-hour chapter, when Chapter 1 uses three for 4 hours?
3. Should the loyalty-app contrast be replaced by a case with no commercial framing?
4. Do the transfer forms need their own SME check, or are blood supply and rental assistance simple enough at supplied-facts depth?
5. Should the pendulum recur at all, or has Chapter 1 exhausted it?

Question 1 is the one that should be settled first; everything else in the chapter's example architecture depends on it.
