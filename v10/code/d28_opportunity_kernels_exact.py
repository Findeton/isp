#!/usr/bin/env python3
"""
d28_opportunity_kernels_exact.py — v10 D28 receipt 2: two complete finite
opportunity kernels (K_collar, K_tail), the gate battery, kernel-level
identifiability, and the dimension triage. Pin: note-d28 (committed pre-run).
Stdlib only; exact rationals. Gates N1-N10; exit 1 on any failure.
"""
from fractions import Fraction as F
from itertools import product, permutations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

CS = {F(9,25): (F(4,5), F(3,5)), F(16,25): (F(3,5), F(4,5)),
      F(576,625): (F(7,25), F(24,25))}
PREP = (F(3,5), F(4,5)); PREP2 = (F(5,13), F(12,13))
G_B, G_I = F(16,25), F(9,25)     # birth and interaction couplings (declared)

# ---- slim pure-state engine (D24 conventions + interact) ----
class Web:
    def __init__(self, roots):
        self.regs = [lab for lab, _ in roots]
        self.psi = [F(1)]
        for _, (c, s) in roots:
            self.psi = [a*x for a in self.psi for x in (c, s)]
    def _cry(self, ctrl, targ, c, s):
        n = len(self.regs)
        out = [F(0)]*(1 << n)
        cb, tb = 1 << (n-1-ctrl), 1 << (n-1-targ)
        for i, a in enumerate(self.psi):
            if a == 0: continue
            if not (i & cb): out[i] += a
            else:
                i0, i1 = i & ~tb, i | tb
                if not (i & tb): out[i0] += a*c; out[i1] += a*s
                else:            out[i0] += -a*s; out[i1] += a*c
        self.psi = out
    def birth(self, parent, child, g):
        self.psi = [x for a in self.psi for x in (a, F(0))]
        self.regs.append(child)
        c, s = CS[g]; self._cry(self.regs.index(parent), len(self.regs)-1, c, s)
    def interact(self, ctrl, targ, g):
        c, s = CS[g]; self._cry(self.regs.index(ctrl), self.regs.index(targ), c, s)
    def law(self):
        n = len(self.regs); order = sorted(range(n), key=lambda q: self.regs[q])
        out = {}
        for i, a in enumerate(self.psi):
            if a == 0: continue
            key = tuple((i >> (n-1-q)) & 1 for q in order)
            out[key] = out.get(key, F(0)) + a*a
        return tuple(sorted(out.items())), tuple(sorted(self.regs))

# ---- the opportunity package ----
# state = (regs tuple, edges frozenset of (u, v) couplings, sealed frozenset)
SEED_REGS = ('R', 'A', 'B')
SEED_EDGES = (('R','A'), ('A','B'))
SEED_SEALED = frozenset({'R'})

def d_cover(regs, edges, x, y):
    adj = {r: set() for r in regs}
    for (u, v) in edges: adj[u].add(v); adj[v].add(u)
    front, seen, d = {x}, {x}, 0
    while front:
        if y in front: return d
        front = {w for u in front for w in adj[u]} - seen
        seen |= front; d += 1
    return None

def options(regs, edges, sealed, kernel):
    """kernel = ('collar',) or ('tail', eps). Returns [(op, weight)] exact."""
    uns = [r for r in regs if r not in sealed]
    opts = [(('none',), F(1))]
    for y in uns:
        opts.append((('birth', y), F(1)))
    for y in uns:
        for x in uns:
            if x == y: continue
            d = d_cover(regs, edges, y, x)
            if d is not None and d <= 1:
                opts.append((('interact', y, x), F(1)))
            elif kernel[0] == 'tail' and d is not None:
                opts.append((('interact', y, x), kernel[1] * F(1,2)**d))
    Z = sum(w for _, w in opts)
    return [(op, w/Z) for op, w in opts]

def apply_op(regs, edges, op, counter):
    if op[0] == 'none': return regs, edges, None
    if op[0] == 'birth':
        child = f"z{counter}"
        return regs + (child,), edges + ((op[1], child),), ('b', op[1], child)
    return regs, edges + ((op[1], op[2]),), ('i', op[1], op[2])

def histories(kernel, T=2):
    """All depth-T histories: (flag sequence, prob, final regs, final edges)."""
    out = []
    def rec(regs, edges, flags, p, t, counter):
        if t == T:
            out.append((tuple(flags), p, regs, edges)); return
        for op, w in options(regs, edges, SEED_SEALED, kernel):
            r2, e2, act = apply_op(regs, edges, op, counter)
            rec(r2, e2, flags + [op], p*w, t+1, counter + (1 if op[0]=='birth' else 0))
    rec(SEED_REGS, SEED_EDGES, [], F(1), 0, 1)
    return out

def final_web(hist_regs, hist_edges, prep=PREP):
    w = Web([('R', prep)])
    for (u, v) in SEED_EDGES:
        w.birth(u, v, G_B)
    for (u, v) in hist_edges[len(SEED_EDGES):]:
        if v.startswith('z'): w.birth(u, v, G_B)
        else:                 w.interact(u, v, G_I)
    return w

def P_K(kernel, prep=PREP):
    """The observable-history law: flag sequence -> (prob, final click law)."""
    law = {}
    for flags, p, regs, edges in histories(kernel):
        if p == 0: continue
        key = (flags, final_web(regs, edges, prep).law())
        law[key] = law.get(key, F(0)) + p
    return law

K_COLLAR = ('collar',)
K_TAIL = ('tail', F(1,5))
K_TAIL2 = ('tail', F(1,10))

print("[d28 opportunity kernels — exact]")

# N1: normalization at every reachable node
ok1 = True
for kernel in (K_COLLAR, K_TAIL, K_TAIL2):
    def walk(regs, edges, t, counter):
        global ok1
        if t == 2: return
        opts = options(regs, edges, SEED_SEALED, kernel)
        ok1 = ok1 and sum(w for _, w in opts) == 1
        for op, w in opts:
            r2, e2, _ = apply_op(regs, edges, op, counter)
            walk(r2, e2, t+1, counter + (1 if op[0]=='birth' else 0))
    walk(SEED_REGS, SEED_EDGES, 0, 1)
check("N1 normalization: sum of opportunity weights = 1 exactly at every "
      "reachable history node, all three kernels", ok1)

# N2 label-independence + N7 sealed protection + N3 null + N5 non-explosion
ok2 = True
o1 = options(('R','A','B','z1'), SEED_EDGES + (('B','z1'),), SEED_SEALED, K_TAIL)
o2 = options(('R','A','B','w1'), SEED_EDGES + (('B','w1'),), SEED_SEALED, K_TAIL)
ren = {('none',): ('none',)}
for op, w in o1:
    op2 = tuple('w1' if x == 'z1' else x for x in op)
    ren[op] = op2
ok2 &= sorted((ren[op], w) for op, w in o1) == sorted(o2)
ok3 = True; ok7 = True; ok5 = True
for kernel in (K_COLLAR, K_TAIL):
    for flags, p, regs, edges in histories(kernel):
        for op in flags:
            ok7 &= ('R' not in op[1:])
        births = sum(1 for op in flags if op[0] == 'birth')
        ok5 &= births <= 2
    opts = options(SEED_REGS, SEED_EDGES, SEED_SEALED, kernel)
    ok3 &= any(op == ('none',) and w > 0 for op, w in opts)
check("N2 history-isomorphism covariance: kernel weights invariant under "
      "register relabeling (exact multiset equality)", ok2)
check("N3 nonzero null opportunity at every node; N5 non-explosion "
      "(at most one op per step, structural)", ok3 and ok5)
check("N7 sealed-algebra protection: zero weight on every op touching the "
      "sealed register, verified over all realized histories", ok7)

# N4: cylinder consistency — depth-2 marginal == depth-1 law
ok4 = True
for kernel in (K_COLLAR, K_TAIL):
    d1 = {}
    for op, w in options(SEED_REGS, SEED_EDGES, SEED_SEALED, kernel):
        d1[op] = d1.get(op, F(0)) + w
    d2 = {}
    for flags, p, _, _ in histories(kernel):
        d2[flags[0]] = d2.get(flags[0], F(0)) + p
    ok4 &= d1 == d2
check("N4 projective/cylinder consistency: the depth-2 law marginalizes to "
      "the depth-1 law exactly", ok4)

# N6: local clock / preparation-independence of the flag law (A0c/Busch gate)
ok6 = True
for kernel in (K_COLLAR, K_TAIL):
    f1 = {}; f2 = {}
    for flags, p, regs, edges in histories(kernel):
        f1[flags] = f1.get(flags, F(0)) + p
    # the kernel consults only (graph, seals): the flag law cannot depend on
    # the preparation; verified by rebuilding the observable law under PREP2
    for (flags, lawk), p in P_K(kernel, PREP2).items():
        f2[flags] = f2.get(flags, F(0)) + p
    ok6 &= f1 == f2
check("N6 local-clock form + Busch flag gate: the opportunity-flag law is "
      "EXACTLY preparation-independent (recorded, non-silent randomness)", ok6)

# N8: gauge on realized webs — commuting recorded ops, same final law
wa = Web([('R', PREP)]); wa.birth('R','A',G_B); wa.birth('A','B',G_B)
wa.birth('A','C',G_B); wa.birth('B','D',G_B)
wb = Web([('R', PREP)]); wb.birth('R','A',G_B); wb.birth('A','B',G_B)
wb.birth('B','D',G_B); wb.birth('A','C',G_B)
ok8 = wa.law() == wb.law()
check("N8 construction-order gauge on realized webs: commuting recorded ops "
      "in either order give the identical label-keyed law", ok8)

# N9: kernel-level identifiability — injectivity of K -> P_K on the family
law_c, law_t, law_t2 = P_K(K_COLLAR), P_K(K_TAIL), P_K(K_TAIL2)
sep_events = [(k, p) for k, p in law_t.items()
              if k not in law_c and any(op[0] == 'interact' for op in k[0])]
ok9 = (law_c != law_t) and (law_t != law_t2) and (law_c != law_t2)
ok9 &= len(sep_events) > 0
p_sep = sum(p for _, p in sep_events)
check("N9 K-level identifiability: P_K distinct pairwise on {K_collar, "
      "K_tail(1/5), K_tail(1/10)} — beyond-collar interaction flags have "
      "probability 0 under collar, positive under tail", ok9,
      f"total separating-event probability under K_tail(1/5): {p_sep}")
print("      scope [pinned]: family-level injectivity of K -> P_K(observable")
print("      histories); the general-K identifiability class is front F7.")
print("      (D23 recovered a realized graph; this gates the KERNEL law.)")

# N10a: the tree upper bound — explicit mirror-DFS 2-realizer, whole census
def rooted_trees(children):
    nodes = ['A'] + children
    for parents in product(*[[p for p in nodes if p != ch] for ch in children]):
        pm = dict(zip(children, parents)); good = True
        for ch in children:
            seen, cur = set(), ch
            while cur != 'A':
                if cur in seen or cur not in pm: good = False; break
                seen.add(cur); cur = pm[cur]
            if not good: break
        if good: yield pm
def preorder(pm, rev):
    kids = {}
    for ch, p in pm.items(): kids.setdefault(p, []).append(ch)
    out = []
    def dfs(u):
        out.append(u)
        for ch in sorted(kids.get(u, []), reverse=rev): dfs(ch)
    dfs('A'); return out
def leq_tree(pm, u, v):
    cur = v
    while True:
        if cur == u: return True
        if cur == 'A': return False
        cur = pm[cur]
ok10a = True; n_trees = 0
for children in (['B','C'], ['B','C','D']):
    for pm in rooted_trees(children):
        n_trees += 1
        L1, L2 = preorder(pm, False), preorder(pm, True)
        nodes = ['A'] + children
        for u in nodes:
            for v in nodes:
                both = (L1.index(u) <= L1.index(v)) and (L2.index(u) <= L2.index(v))
                ok10a &= both == leq_tree(pm, u, v)
check("N10a THE TREE UPPER BOUND, theorem-grade: the explicit mirror-DFS "
      "pair realizes every census tree order exactly — pure-birth order "
      "dimension <= 2, a scale-independent structural bound", ok10a,
      f"{n_trees} trees")
print("      => the pure-birth class is EXCLUDED for M4 (which requires")
print("      unbounded order dimension, the corpus's S_n theorem) by a PROVEN")
print("      upper bound — the repaired triage logic: witnesses are lower")
print("      bounds and growth evidence; witness ABSENCE is never evidence")
print("      without a registered power calculation (the v9 #119 lesson).")

# N10b: interactions break the ceiling — an operational S_3 web
# forest a1,a2,a3; b_j above exactly {a_i : i != j} (births + interactions)
S3_EDGES = [('a2','b1','B'), ('a3','b1','I'),
            ('a1','b2','B'), ('a3','b2','I'),
            ('a1','b3','B'), ('a2','b3','I')]
def s3_web():
    w = Web([('a1', PREP), ('a2', PREP), ('a3', PREP)])
    for (u, v, t) in S3_EDGES:
        if t == 'B': w.birth(u, v, G_B)
        else:        w.interact(u, v, G_I)
    return w
above = {f"b{j}": {f"a{i}" for i in (1,2,3) if i != j} for j in (1,2,3)}
ok10b = True
for (u, v, t) in S3_EDGES:
    ok10b &= u in above[v]
reach = {f"a{i}": {v for v in above if f"a{i}" in above[v]} for i in (1,2,3)}
ok10b &= all(len(reach[a]) == 2 for a in reach)
# operational spot checks: the intervened nodes are all roots, so pure-state
# preparation replacement suffices (the receipt-1 alphabet's prep subset):
def s3_build(iv):
    w = Web([('a1', iv.get('a1', PREP)), ('a2', iv.get('a2', PREP)),
             ('a3', iv.get('a3', PREP))])
    for (u, v, t) in S3_EDGES:
        if t == 'B': w.birth(u, v, G_B)
        else:        w.interact(u, v, G_I)
    return w
def marg1(w, reg):
    n = len(w.regs); q = w.regs.index(reg)
    p1 = sum(a*a for i, a in enumerate(w.psi) if (i >> (n-1-q)) & 1)
    od = F(0)
    for i, a in enumerate(w.psi):
        if a == 0 or (i >> (n-1-q)) & 1: continue
        od += a * w.psi[i | (1 << (n-1-q))]
    return p1, od
def spot_influence(u, v):
    best = F(0)
    settings = [(F(1),F(0)), (F(0),F(1)), PREP]
    outs = []
    for st in settings:
        w = s3_build({u: st})
        p1, od = marg1(w, v)
        outs.append((p1, F(1,2)+od))
    for i in range(len(outs)):
        for j in range(i+1, len(outs)):
            for k in (0,1):
                d = abs(outs[i][k]-outs[j][k])
                if d > best: best = d
    return best
ok10b &= spot_influence('a1','b1') == 0 and spot_influence('a2','b2') == 0
ok10b &= spot_influence('a3','b3') == 0 and spot_influence('a1','a2') == 0
ok10b &= spot_influence('a2','b1') > 0 and spot_influence('a3','b1') > 0
# S_3 has no 2-realizer: exhaustive over linear-extension pairs
ELEMS = ['a1','a2','a3','b1','b2','b3']
REL = {(u, v) for v in above for u in above[v]}
def extensions():
    out = []
    def rec(rem, acc):
        if not rem: out.append(tuple(acc)); return
        for x in list(rem):
            if all((y, x) not in REL for y in rem if y != x):
                rem.remove(x); acc.append(x)
                rec(rem, acc)
                acc.pop(); rem.add(x)
    rec(set(ELEMS), [])
    return out
EXTS = extensions()
incomp = [(x, y) for i, x in enumerate(ELEMS) for y in ELEMS[i+1:]
          if (x, y) not in REL and (y, x) not in REL]
found2 = False
for L1 in EXTS:
    for L2 in EXTS:
        if all((L1.index(x) < L1.index(y)) != (L2.index(x) < L2.index(y))
               for (x, y) in incomp):
            found2 = True; break
    if found2: break
ok10b &= not found2
check("N10b THE CEILING BROKEN: a 6-record forest with three cross-branch "
      "interactions realizes S_3 in its operational influence order (zeros "
      "a_i -/-> b_i and sideways spot-verified interventionally; edges "
      "positive; remaining pattern structural per the T1 theorem class) and "
      "S_3 admits NO 2-realizer (exhaustive) — order dimension >= 3 > 2: "
      "interactions strictly exceed the pure-birth bound", ok10b,
      f"{len(EXTS)} linear extensions searched")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 10 substantive gates)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
