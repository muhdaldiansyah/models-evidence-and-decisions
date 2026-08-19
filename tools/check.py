#!/usr/bin/env python3
"""Repository verification suite.

Codifies the checks that were run by hand at every chapter boundary during
drafting. Exits non-zero on any failure. See decisions/0026 clause 4.3.
"""
import re, os, sys, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
fails, known_hit, known_clear = [], [], []

# Divergences that are surfaced, adjudicated by nobody yet, and owned by the author.
# A known item reports as KNOWN and does not fail the suite. A NEW divergence does.
# If a known item stops applying, the suite says so — the exception should then be deleted.
KNOWN = {
    'Ch1 core competence':
        "README and chapters/01-decisions-questions/spec.md state it differently; "
        "an architectural change requiring author sign-off. See README Current State.",
}

def check(name, ok, detail=''):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  — ' + detail) if detail else ''}")
    if not ok:
        fails.append(name)

MD = [f for f in glob.glob('**/*.md', recursive=True) if not f.startswith('.')]
read = lambda f: open(f, encoding='utf-8').read()

print("\nBibliography and sources")
keys = set(re.findall(r'@\w+\{([^,]+),', read('references.bib')))
notes_ = {os.path.basename(f)[:-3] for f in glob.glob('sources/*.md')} - {'README'}
check('every citation key has a source note', keys == notes_,
      f'{len(keys)} keys, {len(notes_)} notes' + ('' if keys == notes_ else f' · diff {sorted(keys ^ notes_)}'))

PLACEHOLDER = {'citekey', 'key'}
bad = {(f, k) for f in MD for k in re.findall(r'\[@([a-zA-Z0-9_]+)', read(f))
       if k not in keys and k not in PLACEHOLDER}
check('every cited key resolves', not bad, f'{len(bad)} unresolved' if bad else '')

print("\nCitation locators against what was read")
def pages_read(text):
    s = set()
    for m in re.finditer(r'(?i)(?:read (?:directly )?(?:at|to)|read at|pp?\.)\s*([0-9,\s–\-and]+)', text):
        for part in re.split(r'[,;]| and ', m.group(1)):
            part = part.strip()
            r = re.match(r'^(\d+)\s*[–-]\s*(\d+)$', part)
            if r:
                s.update(range(int(r.group(1)), int(r.group(2)) + 1))
            elif re.match(r'^\d+$', part):
                s.add(int(part))
    return s
NOTE = {os.path.basename(f)[:-3]: pages_read(read(f)) for f in glob.glob('sources/*.md')}
out = []
for f in glob.glob('chapters/*/chapter.md'):
    for m in re.finditer(r'\[@([a-zA-Z0-9_]+),\s*([^\]]+)\]', read(f)):
        for pm in re.finditer(r'pp?\.\s*(\d+)(?:\s*[–-]\s*(\d+))?', m.group(2)):
            a = int(pm.group(1)); b = int(pm.group(2)) if pm.group(2) else a
            out += [(m.group(1), p) for p in range(a, b + 1) if p not in NOTE.get(m.group(1), set())]
check('no locator falls outside its source note', not out, f'{sorted(set(out))[:5]}' if out else '')

print("\nLinks")
broken = [(f, l) for f in MD for l in re.findall(r'\]\(([^)#][^)]*)\)', read(f))
          if not l.startswith(('http', 'mailto'))
          and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), l.split('#')[0])))]
check('every relative link resolves', not broken, f'{broken[:3]}' if broken else '')

print("\nCanon")
c = read('canon/terminology.md')
ents = [h for h in re.findall(r'^## (.+)$', c, re.M) if h not in ('term', 'Index') and not h.startswith('Chapter ')]
idx = c.split('## Index', 1)[1].split('\n## ', 1)[0] if '## Index' in c else ''
lnk = set(re.findall(r'\[([^\]]+)\]\(#[^)]+\)', idx))
check('registry and index agree', set(ents) == lnk, f'{len(ents)} entries')
todo = c.count('Definition status: TODO') - 1
check('open definitions are the expected one', todo == 1, f'{todo} open — expected 1 (`utility`)')

homes = {}
for m in re.finditer(r'^## (.+?)$(.*?)(?=^## |\Z)', c, re.M | re.S):
    t = m.group(1).strip()
    if t in ('term', 'Index') or t.startswith('Chapter '):
        continue
    ci = re.search(r'Introduced in:.*?Chapter\s*(\d+)', m.group(2), re.S)
    if ci:
        homes[t] = int(ci.group(1))
MS = {int(re.search(r'chapters/(\d+)', f).group(1)): read(f) for f in glob.glob('chapters/*/chapter.md')}
early = []
for t, home in homes.items():
    pat = re.compile('`' + re.escape(t) + '`')
    for n in MS:
        if n < home and pat.search(MS[n]):
            seg = next((L for L in MS[n].split('\n') if pat.search(L)), '')
            if not re.search(r'reserved|Chapter \d+ uses|warning', seg, re.I):
                early.append((t, home, n))
check('no term used before its chapter without a reservation notice', not early, f'{early[:3]}' if early else '')

print("\nChapters")
want = ['spec.md', 'chapter.md', 'case-data.md', 'drafting-blueprint.md', 'transfer.md',
        'transfer-form-a.md', 'transfer-form-b.md', 'transfer-rubric.md', 'diagnosis-feedback.md',
        'freeze-gates.md']
missing = [(d, w) for d in sorted(glob.glob('chapters/*/')) for w in want if not os.path.exists(d + w)]
check('every chapter has its core files', not missing, f'{missing[:3]}' if missing else '')
check('seventeen chapters', len(glob.glob('chapters/*/chapter.md')) == 17,
      f"{len(glob.glob('chapters/*/chapter.md'))} manuscripts")

gates = [d for d in sorted(glob.glob('chapters/*/')) if not os.path.exists(d + 'freeze-gates.md')]
check('every chapter has a gate tracker', not gates)

pauses = {int(re.search(r'chapters/(\d+)', f).group(1)): len(re.findall(r'(?im)^#{3,4} .*pause', read(f)))
          for f in glob.glob('chapters/*/chapter.md')}
odd = {k: v for k, v in pauses.items() if v != 3}
check('every chapter has exactly three pauses', not odd, f'{odd}' if odd else '')

print("\nREADME and spec synchronisation")
R = read('README.md')
blocks = {}
for m in re.finditer(r'^### Chapter (\d+): (.+?)$(.*?)(?=^### Chapter |\Z)', R, re.M | re.S):
    cq = re.search(r'\*\*Central question\.\*\*\s*(.+?)\s*$', m.group(3), re.M)
    cc = re.search(r'\*\*Core competence\.\*\*\s*(.+?)\s*$', m.group(3), re.M)
    blocks[int(m.group(1))] = (m.group(2).strip(),
                               cq.group(1).strip() if cq else None,
                               cc.group(1).strip() if cc else None)
def sec(t, h):
    m = re.search(r'^## ' + h + r'\s*\n+(.+?)(?=\n\s*\n|\n## )', t, re.M | re.S)
    return ' '.join(m.group(1).split()) if m else None
div = []
for f in sorted(glob.glob('chapters/*/spec.md')):
    t = read(f)
    n = int(re.search(r'^chapter:\s*(\d+)', t, re.M).group(1))
    ti = re.search(r'^title:\s*"(.+)"', t, re.M).group(1).strip()
    for label, a, b in (('title', blocks.get(n, (None,)*3)[0], ti),
                        ('central question', blocks.get(n, (None,)*3)[1], sec(t, 'Central question')),
                        ('core competence', blocks.get(n, (None,)*3)[2], sec(t, 'Core competence'))):
        if a != b:
            div.append(f'Ch{n} {label}')
new_div = [d for d in div if d not in KNOWN]
known_hit.extend(d for d in div if d in KNOWN)
known_clear.extend(k for k in KNOWN if k not in div)
check('no NEW governed-field divergence (51 fields)', not new_div, ' · '.join(new_div) if new_div else
      f'{len(div)} known divergence(s) held open')

print("\nGate status")
gs = read('validation/gate-status.md')
cnt = collections.Counter()
for line in gs.split('| Ch | Chapter')[1].split('\n'):
    cells = [x.strip() for x in line.split('|')]
    if len(cells) < 10 or not cells[1].isdigit():
        continue
    cnt[cells[6]] += 1; cnt[cells[7]] += 2; cnt[cells[8]] += 4
check('gate arithmetic sums to 119', sum(cnt.values()) == 119, f'{sum(cnt.values())}')
check('no gate is closed', 'CLOSED' not in gs, 'a closed gate needs adjudicated evidence')

print("\nFront matter")
for f in ['front-matter/preface.md', 'front-matter/how-to-use-this-book.md', 'front-matter/term-index.md']:
    check(f'{os.path.basename(f)} exists', os.path.exists(f))
if os.path.exists('front-matter/term-index.md'):
    ti = read('front-matter/term-index.md')
    m = re.search(r'(\d+) controlled terms', ti)
    cur = bool(m) and int(m.group(1)) == len(ents)
    check('term index is current with the registry', cur,
          '' if cur else f'index {m.group(1) if m else "?"} vs registry {len(ents)} — run `make index`')

if known_hit:
    print("\nKnown open items — surfaced, not failures")
    for k in known_hit:
        print(f"  KNOWN {k}\n        {KNOWN[k]}")
if known_clear:
    print("\nKnown items that no longer apply — delete them from KNOWN in tools/check.py")
    for k in known_clear:
        print(f"  CLEAR {k}")

print()
if fails:
    print(f"FAILED: {len(fails)} check(s) — {', '.join(fails)}\n")
    sys.exit(1)
print("All checks passed.\n")
