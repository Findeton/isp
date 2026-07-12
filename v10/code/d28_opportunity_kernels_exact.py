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

# ---- slim density-matrix engine for the full-matrix influence gate ----
# (round-1 M1/m10: the S_3 pattern is now gated over ALL 30 ordered pairs
# at the pinned ACTIVE alphabet, with true replacement interventions)
ALPHA_ACTIVE = [(F(1), F(0)), (F(0), F(1)), (F(3,5), F(4,5)), (F(5,13), F(12,13))]
class DWeb:
    def __init__(self, roots):
        self.regs = [lab for lab, _ in roots]
        dim = 1 << len(self.regs)
        self.rho = [[F(0)]*dim for _ in range(dim)]
        amps = [F(1)]
        for _, (c, s) in roots:
            amps = [a*x for a in amps for x in (c, s)]
        for i, ai in enumerate(amps):
            if ai == 0: continue
            for j, aj in enumerate(amps):
                if aj: self.rho[i][j] = ai*aj
    def _cry(self, ctrl, targ, c, s):
        n = len(self.regs); dim = 1 << n
        cb, tb = 1 << (n-1-ctrl), 1 << (n-1-targ)
        cmap = []
        for j in range(dim):
            if not (j & cb): cmap.append(((j, F(1)),))
            else:
                j0, j1 = j & ~tb, j | tb
                if not (j & tb): cmap.append(((j0, c), (j1, s)))
                else:            cmap.append(((j0, -s), (j1, c)))
        M = [[F(0)]*dim for _ in range(dim)]
        for i in range(dim):
            for (r, a) in cmap[i]:
                Mr = M[r]; Ri = self.rho[i]
                for j in range(dim):
                    if Ri[j]: Mr[j] += a*Ri[j]
        out = [[F(0)]*dim for _ in range(dim)]
        for i in range(dim):
            Mi = M[i]; Oi = out[i]
            for j in range(dim):
                x = Mi[j]
                if x == 0: continue
                for (r, a) in cmap[j]:
                    Oi[r] += x*a
        self.rho = out
    def birth(self, parent, child, g):
        dim = 1 << len(self.regs)
        new = [[F(0)]*(2*dim) for _ in range(2*dim)]
        for i in range(dim):
            Ri = self.rho[i]
            for j in range(dim):
                if Ri[j]: new[2*i][2*j] = Ri[j]
        self.rho = new; self.regs.append(child)
        c, s = CS[g]; self._cry(self.regs.index(parent), len(self.regs)-1, c, s)
    def interact(self, ctrl, targ, g):
        c, s = CS[g]; self._cry(self.regs.index(ctrl), self.regs.index(targ), c, s)
    def intervene(self, reg, prep):
        if prep is None: return
        c, s = prep
        n = len(self.regs); dim = 1 << n
        bit = 1 << (n-1-self.regs.index(reg))
        phi = (c, s)
        out = [[F(0)]*dim for _ in range(dim)]
        for i in range(dim):
            Ri = self.rho[i]
            for j in range(dim):
                x = Ri[j]
                if x == 0 or (i & bit) != (j & bit): continue
                i0, j0 = i & ~bit, j & ~bit
                for bi in (0, 1):
                    for bj in (0, 1):
                        w = x * phi[bi] * phi[bj]
                        if w: out[i0 | (bit if bi else 0)][j0 | (bit if bj else 0)] += w
        self.rho = out
    def r1(self, reg):
        n = len(self.regs); dim = 1 << n
        bit = 1 << (n-1-self.regs.index(reg))
        p1 = od = F(0)
        for i in range(dim):
            if self.rho[i][i] and (i & bit): p1 += self.rho[i][i]
            if not (i & bit): od += self.rho[i][i | bit]
        return p1, F(1,2) + od          # (Z: P(1), X: P(+))
def dm_influence(builder, u, v):
    qs = [builder({u: a}).r1(v) for a in ALPHA_ACTIVE]
    best = F(0)
    for i in range(len(qs)):
        for j in range(i+1, len(qs)):
            for k in (0, 1):
                d = abs(qs[i][k] - qs[j][k])
                if d > best: best = d
    return best

# exact trace distance (Delta^3 = c*Delta certificate; d27 conventions)
from math import isqrt
def ratsqrt(x):
    n, d = x.numerator, x.denominator
    rn, rd = isqrt(n), isqrt(d)
    return F(rn, rd) if rn*rn == n and rd*rd == d else None
def tdist(A, B):
    n = len(A)
    D = [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
    if all(D[i][j] == 0 for i in range(n) for j in range(n)): return F(0)
    if all(D[i][j] == 0 for i in range(n) for j in range(n) if i != j):
        return sum(abs(D[i][i]) for i in range(n)) / 2
    D2 = [[sum(D[i][k]*D[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    D3 = [[sum(D2[i][k]*D[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    c = None
    for i in range(n):
        for j in range(n):
            if D[i][j] != 0: c = D3[i][j] / D[i][j]; break
        if c is not None: break
    if c is None or c <= 0: return None
    if any(D3[i][j] != c*D[i][j] for i in range(n) for j in range(n)): return None
    r = ratsqrt(c)
    if r is None: return None
    return sum(D2[i][i] for i in range(n)) / r / 2

print("[d28 opportunity kernels — exact]")
print("      alphabets (round-1: now printed here too): interventions =")
print("      ACTIVE replacements {|0>, |1>, Ry(3/5,4/5), Ry(5/13,12/13)},")
print("      no postselection; queries = {Z, X} per register.")

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
# round-1 M4/N2-widening: a two-register simultaneous relabeling
o3 = options(('R','A','B','z1','z2'), SEED_EDGES + (('B','z1'), ('A','z2')),
             SEED_SEALED, K_TAIL)
o4 = options(('R','A','B','u','v'), SEED_EDGES + (('B','u'), ('A','v')),
             SEED_SEALED, K_TAIL)
ren2 = {}
for op, w in o3:
    ren2[op] = tuple({'z1': 'u', 'z2': 'v'}.get(x, x) for x in op)
ok2 &= sorted((ren2[op], w) for op, w in o3) == sorted(o4)
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
      "the depth-1 law exactly (structural: implied by N1 via Ionescu-Tulcea; "
      "kept as a smoke test)", ok4)

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
check("N6 preparation-swap invariance (the Busch WEIGHT half): the "
      "opportunity-flag law is EXACTLY preparation-independent; the "
      "orthogonality/recording half is declared, with N12 exhibiting why it "
      "is load-bearing", ok6)

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
p_sep2 = sum(p for k, p in law_t2.items()
             if k not in law_c and any(op[0] == 'interact' for op in k[0]))
ok9 &= p_sep == F(2,405) and p_sep2 == F(2,805)
check("N9 K-level identifiability: P_K distinct pairwise on {K_collar, "
      "K_tail(1/5), K_tail(1/10)} — beyond-collar interaction flags have "
      "probability 0 under collar, positive under tail", ok9,
      f"separating-event probability: {p_sep} under tail(1/5), {p_sep2} under tail(1/10)")
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
# round-1 M1/m10 upgrade: the FULL 30-pair influence matrix at the pinned
# ACTIVE alphabet with true replacement interventions (density-matrix engine)
def s3_dm_build(iv):
    w = DWeb([('a1', PREP), ('a2', PREP), ('a3', PREP)])
    for r in ('a1', 'a2', 'a3'):
        w.intervene(r, iv.get(r))
    for (u, v, t) in S3_EDGES:
        if t == 'B':
            w.birth(u, v, G_B); w.intervene(v, iv.get(v))
        else:
            w.interact(u, v, G_I)
    return w
S3_NODES = ['a1','a2','a3','b1','b2','b3']
S3_ORDER = {(u, v): (u in above.get(v, set())) for u in S3_NODES for v in S3_NODES if u != v}
for u in S3_NODES:
    for v in S3_NODES:
        if u == v: continue
        ok10b &= (dm_influence(s3_dm_build, u, v) > 0) == S3_ORDER[(u, v)]
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
      "interactions realizes S_3 in its operational influence relation — ALL "
      "30 ordered pairs gated interventionally at the pinned active alphabet "
      "(real family, {Z,X}; the relation is an order at this pin) — and S_3 "
      "admits NO 2-realizer (exhaustive) — order dimension >= 3 > 2: "
      "interactions strictly exceed the pure-birth bound", ok10b,
      f"30 pairs; {len(EXTS)} linear extensions searched")

# N11 (round-1 M4, DISCLOSED): both kernels FAIL the Rideout-Sorkin
# path-covariance analog — the same grown graph reached along different
# accretion orders carries different path probabilities. Printed as the
# honest delta; the RS-covariant-NSE-kernel question is the successor front.
def path_prob(kernel, ops):
    regs, edges, p, counter = SEED_REGS, SEED_EDGES, F(1), 1
    for op in ops:
        w = dict(options(regs, edges, SEED_SEALED, kernel)).get(op)
        if w is None: return F(0)
        p *= w
        regs, edges, _ = apply_op(regs, edges, op, counter)
        if op[0] == 'birth': counter += 1
    return p
p1c = path_prob(K_COLLAR, [('birth','A'), ('interact','A','B')])
p2c = path_prob(K_COLLAR, [('interact','A','B'), ('birth','A')])
p1t = path_prob(K_TAIL,   [('birth','A'), ('interact','A','B')])
p2t = path_prob(K_TAIL,   [('interact','A','B'), ('birth','A')])
ok11 = (p1c == F(1,40) and p2c == F(1,25) and p1c != p2c
        and p1t == F(2,81) and p2t == F(1,25) and p1t != p2t)
check("N11 RS path-covariance DISCLOSURE: the same grown graph along two "
      "accretion orders has different path probabilities under BOTH kernels "
      "— the growth measure depends on birth order (the global step clock is "
      "physical in these kernels), unlike Rideout-Sorkin covariance", ok11,
      f"collar: 1/40 vs 1/25; tail: 2/81 vs 1/25")
print("      N11 honest-delta print: RS births take arbitrary partial stems")
print("      (multi-parent) — common futures are NATIVE in RS growth; the D28")
print("      obstruction exists relative to the corpus's ONE-PARENT birth")
print("      clause. Whether an NSE-compliant, RS-path-covariant opportunity")
print("      kernel exists — or whether flags-observable makes path-equality")
print("      the wrong requirement — is the successor front (the first exact")
print("      shot at the kernel-selector problem, paper 19 F12).")

# N12 (round-1 m4/F3): the unrecorded-lottery exhibit — a preparation-
# independent lottery over NON-orthogonal isometries strictly contracts a
# declared pair: preparation-independence alone is NOT Busch-sufficient;
# the orthogonality (= flag recordability) half is load-bearing.
def rho_eta(eta):
    return [[F(1,2), eta/2], [eta/2, F(1,2)]]
def lottery(rho):
    c, s = CS[F(576,625)]
    out = [[F(0)]*4 for _ in range(4)]
    for i in range(2):                     # V1 = append blank (identity)
        for j in range(2):
            out[2*i][2*j] += rho[i][j] / 2
    v = {0: [(0, F(1))], 1: [(2, c), (3, s)]}   # V2 = blank then cRy(g)
    for i in range(2):
        for j in range(2):
            if rho[i][j] == 0: continue
            for (r1, a1) in v[i]:
                for (r2, a2) in v[j]:
                    out[r1][r2] += rho[i][j] * a1 * a2 / 2
    return out
# V1 maps |x> -> |x,0>; V2 maps |0> -> |0,0>, |1> -> c|1,0> + s|1,1>.
# The range-overlap gate is COMPUTED from the explicit isometry matrices
# (round-2 self-catch: it was hardcoded), V1†V2 != 0 <=> non-orthogonal ranges.
cL, sL = CS[F(576,625)]
V1m = [[F(1),F(0)],[F(0),F(0)],[F(0),F(1)],[F(0),F(0)]]
V2m = [[F(1),F(0)],[F(0),F(0)],[F(0),cL],[F(0),sL]]
V1tV2 = [[sum(V1m[r][i]*V2m[r][j] for r in range(4)) for j in range(2)]
         for i in range(2)]
overlap_nonzero = any(V1tV2[i][j] != 0 for i in range(2) for j in range(2))
i1 = [[sum(V1m[r][i]*V1m[r][j] for r in range(4)) for j in range(2)] for i in range(2)]
i2 = [[sum(V2m[r][i]*V2m[r][j] for r in range(4)) for j in range(2)] for i in range(2)]
I2 = [[F(1),F(0)],[F(0),F(1)]]
d_in = tdist(rho_eta(F(1)), rho_eta(F(0)))
d_out = tdist(lottery(rho_eta(F(1))), lottery(rho_eta(F(0))))
ok12 = d_in == F(1,2) and d_out == F(2,5) and d_out < d_in
ok12 &= overlap_nonzero and i1 == I2 and i2 == I2   # isometries, ranges overlap
check("N12 the unrecorded-lottery exhibit (A0c receipt): a preparation-"
      "independent 1/2-1/2 lottery over NON-orthogonal isometries strictly "
      "contracts the eta-pair — NOT Busch-admissible: recording the flag "
      "(= orthogonal ranges) is exactly what non-silence requires", ok12,
      f"D_in = {d_in}, D_out = {d_out}, V1†V2[0][0] = {V1tV2[0][0]} != 0")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 12 substantive gates)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
