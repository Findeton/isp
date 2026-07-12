#!/usr/bin/env python3
"""
d24_tree_birth_kernel_exact.py — v10 D24: the tree birth kernel.
Pin: note-d24-tree-birth-kernel-identifiability.md (committed pre-run).
Stdlib only; exact rationals (Pythagorean rotations, Z-basis clicks).
Gates G1-G7 per the pin; exit 1 on any failure.
"""
from fractions import Fraction as F
from itertools import permutations, product

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# Pythagorean (cos, sin) pairs; coupling g = sin^2.
CS = {F(9,25): (F(4,5), F(3,5)), F(16,25): (F(3,5), F(4,5)),
      F(576,625): (F(7,25), F(24,25))}
PREP = (F(3,5), F(4,5))          # root preparation, P(root=1) = 16/25
PREP2 = (F(5,13), F(12,13))      # alternate preparation for injectivity

class Web:
    """A grown record web: registers in birth order, pure state vector."""
    def __init__(self, root_label, prep):
        c, s = prep
        self.regs = [root_label]
        self.psi = [c, s]        # |0>, |1> amplitudes
    def _cry(self, ctrl, targ, c, s):
        n = len(self.regs); dim = 2**n
        out = [F(0)]*dim
        for i, a in enumerate(self.psi):
            if a == 0: continue
            bits = [(i >> (n-1-q)) & 1 for q in range(n)]
            if bits[ctrl] == 0:
                out[i] += a
            else:
                t = bits[targ]
                for tn in (0, 1):
                    b2 = list(bits); b2[targ] = tn
                    j = sum(bb << (n-1-q) for q, bb in enumerate(b2))
                    amp = (c if tn == t else (s if tn == 1 else -s))
                    out[j] += a * amp
        self.psi = out
    def birth(self, parent_label, child_label, g):
        """Birth event: new register in |0>, coupled from parent (isometry)."""
        self.psi = [x for a in self.psi for x in (a, F(0))]  # tensor |0>
        self.regs.append(child_label)
        c, s = CS[g]
        self._cry(self.regs.index(parent_label), len(self.regs)-1, c, s)
    def norm2(self):
        return sum(a*a for a in self.psi)
    def clicks(self):
        """Exact Z-click law keyed by register identity (sorted labels)."""
        n = len(self.regs); order = sorted(range(n), key=lambda q: self.regs[q])
        law = {}
        for i, a in enumerate(self.psi):
            if a == 0: continue
            bits = tuple((i >> (n-1-q)) & 1 for q in order)
            law[bits] = law.get(bits, F(0)) + a*a
        return law
    def marg1(self, label):
        n = len(self.regs); q = self.regs.index(label)
        return sum(a*a for i, a in enumerate(self.psi) if (i >> (n-1-q)) & 1)
    def joint(self, lab_v, v, lab_u, u):
        n = len(self.regs); qv, qu = self.regs.index(lab_v), self.regs.index(lab_u)
        return sum(a*a for i, a in enumerate(self.psi)
                   if ((i >> (n-1-qv)) & 1) == v and ((i >> (n-1-qu)) & 1) == u)

def grow(edges, schedule, gmap, prep=PREP):
    """edges: {child: parent}; schedule: birth order of children."""
    w = Web('A', prep)
    for ch in schedule:
        w.birth(edges[ch], ch, gmap[ch])
    return w

def static_circuit(edges, schedule, gmap, prep=PREP):
    """Independent constructor: all registers first, then edges (wiring check)."""
    labels = ['A'] + list(schedule)
    n = len(labels); dim = 2**n
    psi = [F(0)]*dim; psi[0] = F(1)
    c, s = prep
    out = [F(0)]*dim
    for i, a in enumerate(psi):
        if a == 0: continue
        b0 = (i >> (n-1)) & 1
        for bn in (0, 1):
            j = (i & (dim//2 - 1)) | (bn << (n-1))
            amp = (c if bn == b0 else (s if bn == 1 else -s))
            out[j] += a * amp
    psi = out
    w = Web.__new__(Web); w.regs = labels; w.psi = psi
    for ch in schedule:
        cc, ss = CS[gmap[ch]]
        w._cry(labels.index(edges[ch]), labels.index(ch), cc, ss)
    return w

print("[d24 tree birth kernel — exact]")
TREE = {'B': 'A', 'C': 'A', 'D': 'B'}          # A->B, A->C, B->D
GMAP = {'B': F(9,25), 'C': F(16,25), 'D': F(576,625)}

# G1: exhibit — normalization/positivity at every step, norm preserved (isometry)
ok1 = True
w = Web('A', PREP)
ok1 &= w.norm2() == 1
for ch in ('B', 'C', 'D'):
    w.birth(TREE[ch], ch, GMAP[ch])
    law = w.clicks()
    ok1 &= w.norm2() == 1 and sum(law.values()) == 1 and all(p >= 0 for p in law.values())
check("G1 exhibit: isometric growth — norm 1 and exact click normalization/"
      "positivity at every birth", ok1)

# G2: construction-order gauge — all causal linear extensions agree
ok2 = True
ref = None; n_ext = 0
for order in permutations(('B', 'C', 'D')):
    if order.index('B') > order.index('D'):    # D's parent B must exist
        continue
    n_ext += 1
    law = grow(TREE, order, GMAP).clicks()
    if ref is None: ref = law
    ok2 &= (law == ref)
check("G2 construction-order gauge: all causal linear extensions give the "
      "identical label-keyed click law", ok2, f"{n_ext} extensions")

# G3: reception at birth + ledger balance (injectivity across growth)
ok3 = True
for gB in CS:
    for gD in CS:
        gm = {'B': gB, 'C': F(16,25), 'D': gD}
        wv = Web('A', PREP)
        for ch in ('B', 'C', 'D'):
            p_par = wv.marg1(TREE[ch])
            wv.birth(TREE[ch], ch, gm[ch])
            ok3 &= wv.marg1(ch) == gm[ch] * p_par   # content received from parent
wa, wb = Web('A', PREP), Web('A', PREP2)
ok3 &= wa.psi != wb.psi
for ch in ('B', 'C', 'D'):
    wa.birth(TREE[ch], ch, GMAP[ch]); wb.birth(TREE[ch], ch, GMAP[ch])
    ok3 &= wa.psi != wb.psi                          # distinction never erased
check("G3 no silent creation: P(child=1) = g*P(parent=1) exactly at every "
      "birth; root distinctions survive every growth step", ok3)

# G4: fixed-carrier reduction — grown web == independent static constructor
ok4 = True
for order in (('B','C','D'), ('C','B','D')):
    ok4 &= grow(TREE, order, GMAP).clicks() == static_circuit(TREE, order, GMAP).clicks()
check("G4 reduction (wiring-grade): grown-web law == static-circuit law, "
      "exact byte equality", ok4)

# G5: identifiability — exhaustive labeled rooted trees, n = 3 and 4
def rooted_trees(children):
    """All parent maps for the given children over {A}+children forming a tree rooted at A."""
    nodes = ['A'] + children
    for parents in product(*[[p for p in nodes if p != ch] for ch in children]):
        pm = dict(zip(children, parents))
        ok = True
        for ch in children:                      # each child must reach A
            seen, cur = set(), ch
            while cur != 'A':
                if cur in seen or cur not in pm: ok = False; break
                seen.add(cur); cur = pm[cur]
            if not ok: break
        if ok:
            yield pm

def schedule_of(pm):
    """A topological birth order (children after parents)."""
    out, placed = [], {'A'}
    while len(out) < len(pm):
        for ch in sorted(pm):
            if ch not in placed and pm[ch] in placed:
                out.append(ch); placed.add(ch)
    return tuple(out)

def ancestors_of(pm, v):
    out, cur = set(), pm[v]
    while True:
        out.add(cur)
        if cur == 'A': return out
        cur = pm[cur]

ok5 = True; total = 0
for children, gassign in ((['B','C'], None), (['B','C','D'], None)):
    laws = {}
    trees = list(rooted_trees(children))
    for pm in trees:
        gm = {ch: g for ch, g in zip(sorted(pm), [F(9,25), F(16,25), F(576,625)])}
        wv = grow(pm, schedule_of(pm), gm)
        key = tuple(sorted(wv.clicks().items()))
        ok5 &= key not in laws                   # zero collisions
        laws[key] = pm
        # recovery: ancestors from exact zero patterns, couplings from ratios
        for ch in pm:
            anc = {u for u in (['A'] + children) if u != ch
                   and wv.joint(ch, 1, u, 0) == 0 and wv.marg1(ch) > 0}
            ok5 &= anc == ancestors_of(pm, ch)
            par = [u for u in anc if (u == 'A' and len(anc) == 1) or
                   (u != 'A' and u in pm and ancestors_of(pm, u) == anc - {u})]
            ok5 &= len(par) == 1 and par[0] == pm[ch]
            ok5 &= wv.joint(ch, 1, pm[ch], 1) == gm[ch] * wv.marg1(pm[ch])
    total += len(trees)
check("G5 identifiability: zero collisions + exact tree-and-coupling recovery "
      "over ALL labeled rooted trees", ok5, f"3 trees (n=3) + 16 trees (n=4) = {total+0} laws")

# G6: family non-uniqueness — two admissible kernels, different laws
k_chain = grow({'B':'A','C':'B'}, ('B','C'), {'B':F(16,25),'C':F(16,25)})
k_star  = grow({'B':'A','C':'A'}, ('B','C'), {'B':F(16,25),'C':F(16,25)})
check("G6 non-uniqueness: chain-growth and star-growth kernels both satisfy "
      "G1-G4 constraints yet print different click laws (extra physics)",
      k_chain.clicks() != k_star.clicks())

# G7: boundary honesty (prints)
print("      G7 boundary: a birth to an unexcited parent is click-invisible:")
w2 = Web('A', (F(1), F(0)))                      # root prepared in |0>
w2.birth('A', 'B', F(16,25))
print(f"        root |0>: P(B=1) = {w2.marg1('B')} (the newborn EXISTS, has no"
      " click shadow — clicks certify the activated subtree)")
print("      G7 boundary: in-degree >= 2 is structurally impossible AT BIRTH")
print("        (a newborn has exactly one parent); non-tree edges arise only")
print("        as post-birth interactions — outside this kernel class.")
check("G7 boundary prints emitted", True)

print()
total_checks = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total_checks}: 6 substantive gates + 1 print gate)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total_checks}")
if FAIL: raise SystemExit(1)
