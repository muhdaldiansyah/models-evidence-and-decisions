#!/usr/bin/env python3
"""Generate front-matter/term-index.md from canon/terminology.md.

The index points at chapters; it does not define terms. See decisions/0026 clause 3.
Run via `make index`. Do not edit the output by hand.
"""
import re, sys, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANON = os.path.join(ROOT, 'canon', 'terminology.md')
OUT = os.path.join(ROOT, 'front-matter', 'term-index.md')

SLUGS = {}
for d in sorted(os.listdir(os.path.join(ROOT, 'chapters'))):
    if re.match(r'^\d\d-', d):
        SLUGS[int(d[:2])] = d

def field(body, name):
    m = re.search(r'^- ' + name + r':\s*(.+)$', body, re.M)
    return m.group(1).strip() if m else ''

def trim(s, n=110):
    s = re.sub(r'`([^`]+)`', r'`\1`', s)
    s = re.split(r'(?<=[a-z])\s*;\s*', s)[0]
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '…'

text = open(CANON).read()
entries = []
for m in re.finditer(r'^## (.+?)$(.*?)(?=^## |\Z)', text, re.M | re.S):
    term, body = m.group(1).strip(), m.group(2)
    if term in ('term', 'Index') or term.startswith('Chapter '):
        continue
    ci = re.search(r'Introduced in:.*?Chapter\s*(\d+)', body, re.S)
    entries.append(dict(
        term=term,
        chapter=int(ci.group(1)) if ci else None,
        origin=trim(field(body, 'Field/origin'), 70),
        distinct=trim(field(body, 'Distinct from')),
        todo='Definition status: TODO' in body,
    ))

by_ch = collections.defaultdict(list)
for e in entries:
    by_ch[e['chapter']].append(e)

anchor = lambda t: re.sub(r'[^a-z0-9 -]', '', t.lower()).replace(' ', '-')

L = []
w = L.append
w("# Term Index\n")
w("**Generated from `../canon/terminology.md` by `../tools/make-term-index.py`. Do not edit by hand — run `make index`.**\n")
w(f"{len(entries)} controlled terms across seventeen chapters.\n")
w("**This is an index, not a glossary.** It tells you where a term is introduced and what the book keeps it apart from.")
w("It does not define the terms, because the book defines them in the place where they do work, and a definition lifted out of that place would be a different claim.\n")
w("Terms are listed by the chapter that introduces them. A term you meet in Chapter 12 may have been introduced in Chapter 3.\n")

w("## The six collisions\n")
w("The book works across fields that borrowed one another's words without coordinating.")
w("Where one word carries two established meanings, the book **announces the collision and keeps both senses** rather than inventing a third word to avoid it.\n")
w("**If a term below is giving you trouble, look here first.**\n")
w("| Word | Sense one | Sense two | Announced |")
w("|---|---|---|---|")
w("| `validation` | in measurement, assessing whether evidence supports an interpretation | in computational modelling, checking a model against the world | Chapter 3, taken up in Chapter 5 |")
w("| `consistency` | an estimator property — converging on the target as evidence grows | the third identification condition, about observed outcomes under treatment received | Chapter 8 |")
w("| `significance` | a threshold verdict on a P value | substantive importance | Chapter 8 |")
w("| `sensitivity analysis` | varying inputs inside a formulation | robustness of a decision across futures | Chapter 8, with the decision sense at Chapter 12 |")
w("| `robustness` / `stability` | in dynamics, whether a system returns after disturbance | in decision-making, whether a choice survives across futures | Chapter 13 |")
w("| **`identifiable`** — four senses | `statistical identifiability` and `causal identification` (Chapter 7) | `structural identifiability` and `practical identifiability` (Chapter 14) | Chapter 14 |")
w("")
w("**No chapter may add a fifth sense of `identifiable`.** That is a standing instruction proposed at [Decision 0021](../decisions/0021-chapter14-sequential-control-terminology-and-boundary.md) clause 7.3.\n")
w("Two further notes. `equilibrium` means one thing in Chapter 13's dynamics and another in Chapter 15's strategic setting; the registry flagged it from Chapter 1. And `shadow price` collides with a cost-benefit sense the book does not use — noted at Chapter 12 and not adopted.\n")

w("## Terms by chapter\n")
for ch in sorted(k for k in by_ch if k):
    slug = SLUGS.get(ch)
    w(f"### Chapter {ch} — [{len(by_ch[ch])} terms](../chapters/{slug}/chapter.md)\n")
    w("| Term | Kept distinct from | Field |")
    w("|---|---|---|")
    for e in sorted(by_ch[ch], key=lambda x: x['term']):
        flag = ' **[open]**' if e['todo'] else ''
        w(f"| [`{e['term']}`](../canon/terminology.md#{anchor(e['term'])}){flag} | {e['distinct'] or '—'} | {e['origin'] or '—'} |")
    w("")

todo = [e for e in entries if e['todo']]
if todo:
    w("## Terms marked open\n")
    for e in todo:
        w(f"- **`{e['term']}`** — assigned to Chapter {e['chapter']}, which is drafted and did not define it. There is no later chapter to close it in. See [Decision 0020](../decisions/0020-chapter13-dynamics-terminology-and-boundary.md) clause 12.4.")
    w("")

w("## Status\n")
w("Every terminology block from Chapter 2 onward is **provisional**, pending adjudication of the decision record that proposes it.")
w("`../canon/terminology.md` records which record governs which block, and `../README.md` lists them.\n")

open(OUT, 'w').write('\n'.join(L) + '\n')
print(f"{OUT}: {len(entries)} terms, {len(by_ch)-(1 if None in by_ch else 0)} chapters, {len(todo)} open")
