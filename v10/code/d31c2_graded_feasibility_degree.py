#!/usr/bin/env python3
"""
d31c2_graded_feasibility_degree.py — v10 O3: the D31C OPEN-family exact
search (simple-graph degree, distance-degree = family (ii), motif,
component-size). Pin: note-d32-dimension-map.md §7(4) (committed
pre-run) + the d31c2 appendix in note-d31 (class-map conventions,
committed pre-run). Stdlib only; exact rationals (Fractions);
Fourier-Motzkin for the positivity decision. RECONNAISSANCE ONLY: the
horizon is the D28-seed reachable set with u <= 5 unsealed registers
(<= 3 births); NO unbounded-existence claim without an extension
theorem (stated in D6).

Conventions (pinned):
- STATE = the simple graph (registers, edges) + the seal set {R}.
  Births add a leaf on an unsealed register; interacts change NO state
  (the circuit gains a gate; the simple graph does not — the d31c C1
  bookkeeping). Opportunities at a state: one birth per unsealed
  register; one interact per ORDERED pair of distinct unsealed
  registers (complete-graph interacts, classed by graph distance —
  the D31C family-(i) convention).
- KERNEL = normalized stationary class-graded: P(op|W) = w_{cls(op|W)}
  / Z(W), Z(W) = the sum of w over all opportunities at W; w > 0.
- INDEPENDENCE (the D31A state-level convention): two ops are
  independent at W iff both are available at W, each remains available
  after the other, and both orders reach the SAME state. Overlapping
  supports are allowed — the kernel's path measure lives on STATE
  paths, not circuits.
- Path-covariance on an independent pair:
  w(o1|W) * w(o2|W+o1) * Z(W+o2) = w(o2|W) * w(o1|W+o2) * Z(W+o1).
- degree(v) = neighbor count in the simple graph, SEALED NEIGHBORS
  INCLUDED (graph-intrinsic); d_cover(y,x) = graph distance (paths
  through any node, sealed included), capped at 2; common-neighbor
  count capped at 1; DCAP = 5 — exact on the class-collection domain
  (guarded to u <= 5 per round-1 m2; the cap WOULD bind at deg-6
  u = 6 successors, which are excluded from the class set).
Round-1 repairs applied (reviews/d31c2-o3-round1-hostile-review.md):
the component-size verdict scoped to UNBOUNDED GROWTH with the
horizon-EXISTS witness receipt-verified (D5b); minimal single-row
certificates + disjoint-only robustness gated (in D2/D3); the
class-invariance half of L1's premise gated (D1); limits re-scoped
to the EXISTS side (D6).
Gates D1-D6; exit 1 on any failure.
"""
from fractions import Fraction as F
from itertools import permutations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

DCAP = 5

# ---- states ----------------------------------------------------------------
# state = (n, frozenset of frozenset({a,b})); node 0 = R (sealed); seed:
# R-A, A-B with A = 1, B = 2. Unsealed = 1..n-1; u = n-1.
SEED = (3, frozenset({frozenset({0, 1}), frozenset({1, 2})}))

def births(state):
    n, E = state
    outs = []
    for y in range(1, n):
        E2 = set(E); E2.add(frozenset({y, n}))
        outs.append((y, (n + 1, frozenset(E2))))
    return outs

def canon(state):
    n, E = state
    best = None
    for perm in permutations(range(1, n)):
        m = {0: 0}
        for i, p in enumerate(perm, start=1): m[i] = p
        E2 = tuple(sorted(tuple(sorted((m[a], m[b]))) for ab in E
                          for a, b in [tuple(ab)]))
        if best is None or E2 < best: best = E2
    return (n, best)

def enumerate_states(max_u=5):
    """All reachable states with u <= max_u, deduped up to isomorphism
    (R fixed). Returns dict canon -> representative state."""
    reps = {canon(SEED): SEED}
    frontier = [SEED]
    while frontier:
        nxt = []
        for st in frontier:
            if st[0] - 1 >= max_u: continue
            for _, st2 in births(st):
                c = canon(st2)
                if c not in reps:
                    reps[c] = st2; nxt.append(st2)
        frontier = nxt
    return reps

def adj(state):
    n, E = state
    A = {v: set() for v in range(n)}
    for ab in E:
        a, b = tuple(ab); A[a].add(b); A[b].add(a)
    return A

def deg(state, v): return len(adj(state)[v])

def dist(state, y, x):
    A = adj(state)
    seen = {y: 0}; q = [y]
    while q:
        v = q.pop(0)
        if v == x: return seen[v]
        for w2 in A[v]:
            if w2 not in seen:
                seen[w2] = seen[v] + 1; q.append(w2)
    return 10**6

def common_nbrs(state, y, x):
    A = adj(state)
    return len(A[y] & A[x])

def connected(state):
    A = adj(state); n = state[0]
    seen = {0}; q = [0]
    while q:
        v = q.pop(0)
        for w2 in A[v]:
            if w2 not in seen: seen.add(w2); q.append(w2)
    return len(seen) == n

# ---- class maps (the four OPEN families) -----------------------------------
def cls_DEG(state, op):
    if op[0] == 'b': return ('b', min(deg(state, op[1]), DCAP))
    _, y, x = op
    return ('i', min(deg(state, y), DCAP), min(deg(state, x), DCAP))

def cls_DDEG(state, op):
    if op[0] == 'b': return ('b',)
    _, y, x = op
    return ('i', min(dist(state, y, x), 2), min(deg(state, x), DCAP))

def cls_MOTIF(state, op):
    if op[0] == 'b': return ('b',)
    _, y, x = op
    return ('i', min(dist(state, y, x), 2), min(common_nbrs(state, y, x), 1))

def cls_COMP(state, op):
    s = state[0]        # component size = register count (all states connected)
    return ('b', s) if op[0] == 'b' else ('i', s)

def opportunities(state):
    n, _ = state
    ops = [('b', y) for y in range(1, n)]
    ops += [('i', y, x) for y in range(1, n) for x in range(1, n) if x != y]
    return ops

def census(state, cls):
    c = {}
    for op in opportunities(state):
        k = cls(state, op); c[k] = c.get(k, 0) + 1
    return c

def delta_census(state, y, cls):
    """census(state + b_y) - census(state) as a dict class -> int."""
    st2 = None
    for yy, s2 in births(state):
        if yy == y: st2 = s2; break
    c1, c2 = census(state, cls), census(st2, cls)
    d = {}
    for k in set(c1) | set(c2):
        v = c2.get(k, 0) - c1.get(k, 0)
        if v: d[k] = v
    return d, st2

# ---- exact linear algebra + Fourier-Motzkin --------------------------------
def rref(rows, nvar):
    rows = [r[:] for r in rows if any(x != 0 for x in r)]
    piv = []
    r = 0
    for c in range(nvar):
        p = None
        for i in range(r, len(rows)):
            if rows[i][c] != 0: p = i; break
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        piv.append(c); r += 1
        if r == len(rows): break
    return [row for row in rows if any(x != 0 for x in row)], piv

def positive_solution(eqs, nvar):
    """Decide: does {A w = 0, w > 0 componentwise} have a solution?
    Exact: RREF -> express pivots in free vars -> Fourier-Motzkin on the
    strict inequalities. Returns (feasible, witness_or_certificate)."""
    R, piv = rref(eqs, nvar)
    free = [c for c in range(nvar) if c not in piv]
    # w_j > 0 as inequalities over the free vars: w_pivot = -sum coeff*free
    ineqs = []   # each: (coeffs over free vars, meaning sum > 0)
    for j in range(nvar):
        if j in piv:
            row = R[piv.index(j)]
            co = [-row[f] for f in free]
        else:
            co = [F(1) if f == j else F(0) for f in free]
        ineqs.append(co)
    # Fourier-Motzkin eliminate free vars one at a time (strict > 0)
    def fm(ineqs, k):
        pos = [q for q in ineqs if q[k] > 0]
        neg = [q for q in ineqs if q[k] < 0]
        zer = [q for q in ineqs if q[k] == 0]
        out = [q[:k] + q[k+1:] for q in zer]
        for p in pos:
            for m in neg:
                comb = [p[k] * m[i] - m[k] * p[i] for i in range(len(p))]
                out.append(comb[:k] + comb[k+1:])
        return out
    nf = len(free)
    if nf == 0:
        # homogeneous RREF with full pivot rank: the only solution is w = 0,
        # which is not componentwise positive
        return False, "full rank: only the zero solution (no free variables)"
    if any(all(c == 0 for c in q) for q in ineqs):
        return False, "a variable is forced to 0 (empty positivity row)"
    cur = [q[:] for q in ineqs]
    for _ in range(nf):
        cur = fm(cur, 0)
        if any(all(c == 0 for c in q) for q in cur):
            return False, "FM derived 0 > 0 (contradiction certificate)"
    # feasible: construct a witness by back-substitution grid search
    for grid in _witness_grids(nf):
        vals = [F(g) for g in grid]
        w = [None] * nvar
        okv = True
        for j in range(nvar):
            if j in piv:
                row = R[piv.index(j)]
                w[j] = -sum(row[f] * vals[i] for i, f in enumerate(free))
            else:
                w[j] = vals[free.index(j)]
            if w[j] <= 0: okv = False; break
        if okv: return True, w
    # round-1 n3: this (True, None) fallback makes a genuinely feasible
    # family print a FAILED gate (no witness found) — fail-safe direction
    return True, None

def _witness_grids(nf):
    from itertools import product as prod
    if nf <= 3:
        cands = [F(1), F(1, 2), F(2), F(1, 4), F(4), F(1, 8), F(8),
                 F(1, 16), F(16), F(1, 32), F(32)]
    elif nf <= 6:
        cands = [F(1), F(1, 4), F(4), F(1, 16), F(16)]
    else:
        cands = [F(1), F(1, 8), F(8)]
    return prod(cands, repeat=nf)

# ---- the covariance system builder (interact-inert families) ---------------
def build_system(reps, cls):
    """Returns (classes, eq_rows, merges, exhibits).
    Layer 1 (linear): for every state with u >= 3 and every birth y, a
    disjoint interact exists (gated in D1), forcing Z(W+b_y) = Z(W):
    the delta-census row = 0. The u = 2 seed joins after Layer-2 merging
    (its bi pairs are all overlapping).
    Layer 2 (bilinear -> merge): at u >= 3, an overlapping bi pair
    (b_y, i_ab with y in {a,b}) gives w(c')Z(W) = w(c)Z(W+b_y); with
    Layer 1 forcing the Z's equal, w(c') = w(c): classes MERGE."""
    classes = set()
    for st in reps.values():
        for op in opportunities(st): classes.add(cls(st, op))
        for y, st2 in births(st):
            if st2[0] - 1 > 5: continue   # round-1 m2: no phantom u=6 classes
            for op in opportunities(st2): classes.add(cls(st2, op))
    classes = sorted(classes)
    idx = {c: i for i, c in enumerate(classes)}
    parent = list(range(len(classes)))
    def find(i):
        while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
        return i
    def union(i, j):
        ri, rj = find(i), find(j)
        if ri != rj: parent[max(ri, rj)] = min(ri, rj)
    merges = []
    for st in reps.values():
        u = st[0] - 1
        if u < 3: continue
        for y, st2 in births(st):
            if st2[0] - 1 > 5: continue
            for op in opportunities(st):
                if op[0] != 'i': continue
                if y not in (op[1], op[2]): continue
                c, c2 = cls(st, op), cls(st2, op)
                if c != c2:
                    if find(idx[c]) != find(idx[c2]):
                        merges.append((c, c2))
                    union(idx[c], idx[c2])
    groups = {}
    for i, c in enumerate(classes): groups.setdefault(find(i), []).append(c)
    rep_of = {}
    for g in groups.values():
        for c in g: rep_of[c] = g[0]
    merged = sorted(set(rep_of.values()))
    midx = {c: i for i, c in enumerate(merged)}
    rows, exhibits = [], []
    seed_rows_skipped = 0
    for st in reps.values():
        u = st[0] - 1
        for y, st2 in births(st):
            if st2[0] - 1 > 5: continue
            if u == 2:
                # the u = 2 seed has NO disjoint interact: its bi pairs are
                # all overlapping (bilinear). The Z-equality row is implied
                # ONLY if every class this birth reclassifies is already
                # merged (then w(c') = w(c) linearizes the equation); else
                # the seed equation stays unresolved and is SKIPPED (sound:
                # we only add implied equations; count disclosed).
                implied = True
                for op in opportunities(st):
                    if op[0] != 'i': continue
                    if y not in (op[1], op[2]): continue
                    c, c2 = cls(st, op), cls(st2, op)
                    if c != c2 and rep_of[c] != rep_of[c2]:
                        implied = False; break
                if not implied:
                    seed_rows_skipped += 1; continue
            d, _ = delta_census(st, y, cls)
            row = [F(0)] * len(merged)
            for k, v in d.items(): row[midx[rep_of[k]]] += v
            if any(x != 0 for x in row):
                rows.append(row)
                exhibits.append((st, y, {rep_of[k]: v for k, v in d.items()}))
    return merged, rows, merges, exhibits, rep_of, seed_rows_skipped

def verify_covariance(reps, cls, wmap):
    """Direct check: every independent 2-op pair at every horizon state,
    both orders, exact normalized products equal. Returns (ok, bad, npairs)."""
    def Z(st):
        return sum(wmap[cls(st, op)] for op in opportunities(st))
    def step(st, op):
        if op[0] == 'b':
            for y, s2 in births(st):
                if y == op[1]: return s2
        return st
    npairs = 0
    for st in reps.values():
        if st[0] - 1 >= 5: continue
        ops = opportunities(st)
        for i1 in range(len(ops)):
            for i2 in range(i1 + 1, len(ops)):
                o1, o2 = ops[i1], ops[i2]
                s1, s2 = step(st, o1), step(st, o2)
                if canon(step(s1, o2)) != canon(step(s2, o1)): continue
                npairs += 1
                lhs = (wmap[cls(st, o1)] / Z(st)) * (wmap[cls(s1, o2)] / Z(s1))
                rhs = (wmap[cls(st, o2)] / Z(st)) * (wmap[cls(s2, o1)] / Z(s2))
                if lhs != rhs: return False, (st, o1, o2), npairs
    return True, None, npairs

def raw_nonneg_row(reps, cls):
    """Round-1 m1: the ROBUSTNESS probe — in RAW (unmerged) classes, using
    only u >= 3 births (each justified by a DISJOINT interact, the
    strictest circuit-friendly independence reading), find a single
    all-nonnegative delta row with a positive entry: one such row alone
    contradicts Z(W+b) = Z(W) for positive weights, with NO merges and NO
    overlap convention consumed. Deeper horizons contain these rows —
    the negative verdicts extend a fortiori."""
    for st in sorted(reps.values(), key=lambda s: (s[0], canon(s))):
        u = st[0] - 1
        if u < 3: continue
        for y, st2 in births(st):
            if st2[0] - 1 > 5: continue
            d, _ = delta_census(st, y, cls)
            if d and all(v >= 0 for v in d.values()) \
                 and any(v > 0 for v in d.values()):
                return st, y, d
    return None

print("[d31c2 O3 — the open-family exact search (degree / distance-degree /")
print("      motif / component-size); normalized stationary class-graded")
print("      kernels; horizon u <= 5 from the D28 seed; exact rationals]")

# D1: enumeration + structural gates
reps = enumerate_states(5)
by_u = {}
for st in reps.values(): by_u.setdefault(st[0] - 1, []).append(st)
ok1 = all(connected(st) for st in reps.values())
disj = True
inv = True
for st in reps.values():
    u = st[0] - 1
    if u < 3: continue
    for y, st2 in births(st):
        found = any(op[0] == 'i' and y not in (op[1], op[2])
                    for op in opportunities(st))
        disj &= found
        if st2[0] - 1 > 5: continue
        # round-1 n1: the load-bearing half of L1's premise — the DISJOINT
        # interact's class is UNCHANGED by the birth (all three
        # elimination-family class maps), gated exhaustively
        for fam in (cls_DEG, cls_DDEG, cls_MOTIF):
            for op in opportunities(st):
                if op[0] == 'i' and y not in (op[1], op[2]):
                    inv &= (fam(st, op) == fam(st2, op))
ok1 &= disj and inv
check("D1 the horizon enumerated (states per u printed; A000081 rooted-tree "
      "counts); ALL states connected (the component-size reduction's "
      "premise); at every u >= 3 state every birth has a DISJOINT interact "
      "AND that interact's class is UNCHANGED by the birth for all three "
      "elimination families — BOTH halves of Layer 1's premise gated "
      "(round-1 n1)", ok1,
      "u->count: " + ", ".join(f"{u}:{len(v)}" for u, v in sorted(by_u.items())))

# D2/D3: the two elimination families
for name, cls, gate in (("DEG (simple-graph degree)", cls_DEG, "D2"),
                        ("DDEG (distance-degree, family ii)", cls_DDEG, "D3")):
    merged, rows, merges, exhibits, rep_of, skipped = build_system(reps, cls)
    feas, wit = positive_solution(rows, len(merged))
    if not feas:
        # find a small certificate: a pair of delta rows whose difference
        # forces a single class to zero (the u-dependence trap)
        cert = None
        for a in range(len(rows)):
            for b in range(len(rows)):
                if a == b: continue
                diff = [x - y for x, y in zip(rows[a], rows[b])]
                nz = [(i, v) for i, v in enumerate(diff) if v != 0]
                if len(nz) == 1:
                    cert = (exhibits[a], exhibits[b], merged[nz[0][0]])
                    break
            if cert: break
        # round-1 m1: the MINIMAL certificate — a single all-nonnegative
        # merged row (one equation alone kills positivity) — and the
        # convention-robustness probe (raw classes, disjoint-only pairs)
        minrow = next(((ex, {k: v for k, v in zip(merged, r) if v != 0})
                       for r, ex in zip(rows, exhibits)
                       if all(x >= 0 for x in r) and any(x > 0 for x in r)),
                      None)
        rawrow = raw_nonneg_row(reps, cls)
        okg = (minrow is not None) and (rawrow is not None)
        detail = (f"{len(merged)} merged classes (from {len(merges)} forced "
                  f"merges), {len(rows)} delta equations "
                  f"({skipped} unresolved seed rows skipped — sound); "
                  f"INFEASIBLE for positive weights: {wit}")
        if cert:
            (stA, yA, _), (stB, yB, _), zc = cert
            detail += (f"; pair certificate: births at u = {stA[0]-1} vs "
                       f"u = {stB[0]-1} webs force merged class {zc} = 0")
        if minrow:
            (stM, yM, _), nzM = minrow
            detail += (f"; MINIMAL single-row kill (u = {stM[0]-1} birth): "
                       f"Delta = {nzM} >= 0 with positive mass — the d31c "
                       f"C2 mechanism post-merge (O2 instance data)")
        if rawrow:
            stR, yR, dR = rawrow
            detail += (f"; RAW disjoint-only single-row kill at u = "
                       f"{stR[0]-1}: {dR} — the verdict needs NO merges and "
                       f"NO overlap convention; deeper horizons contain "
                       f"these rows (a fortiori)")
        check(f"{gate} [{name}] VERDICT: OBSTRUCTION-instance — the merged "
              f"covariance system (Layer 1 Z-invariance + Layer 2 forced "
              f"class-merges) admits NO positive solution on the horizon "
              f"(exact Fourier-Motzkin); minimal + convention-robust "
              f"certificates gated (round-1 m1)", okg, detail)
    else:
        wmap = {c2: (wit[merged.index(rep_of[c2])] if wit else None)
                for c2 in rep_of}
        okv, bad, _ = (verify_covariance(reps, cls, wmap) if wit
                       else (False, None, 0))
        wtxt = ("sample " + ", ".join(f"{c}={v}" for c, v in
                zip(merged, wit)) if wit else "witness search inconclusive")
        check(f"{gate} [{name}] VERDICT: EXISTS-candidate — a positive "
              f"solution of the merged covariance system exists on the "
              f"horizon; direct 2-op covariance verification "
              f"{'PASSED' if okv else 'FAILED/UNAVAILABLE'}",
              bool(wit) and okv, wtxt + f" ({skipped} seed rows skipped)")

# D4: MOTIF — birth-inertness of existing interact classes (exhaustive)
inert = True
bad = None
for st in reps.values():
    for y, st2 in births(st):
        if st2[0] - 1 > 5: continue
        for op in opportunities(st):
            if op[0] != 'i': continue
            if cls_MOTIF(st, op) != cls_MOTIF(st2, op):
                inert = False; bad = (st, y, op); break
mass = all(
    sum(v for k, v in delta_census(st, y, cls_MOTIF)[0].items()) > 0
    for st in reps.values() for y, st2 in births(st) if st2[0] - 1 <= 5)
check("D4 [MOTIF (distance x common-neighbor)] VERDICT: OBSTRUCTED by the "
      "C2 MECHANISM — leaf births NEVER reclassify existing interact "
      "classes on this grammar (exhaustive over the horizon: distances and "
      "common-neighbor counts of existing pairs are leaf-birth-invariant), "
      "so the family is birth-inert and multiplicity-insensitive: "
      "Z(W+b) - Z(W+i) = the newborn's strictly positive mass (d31c C2, "
      "verified: every birth strictly enlarges the census)", inert and mass,
      "the open-arm placement of tree-substrate motifs at #139 is hereby "
      "RESOLVED-OBSTRUCTED (they never escaped birth-inertness)")

# D5: COMP — the connectivity reduction (component size == n == u + 1 on
# every reachable state, so the grading is a function of u alone).
# Round-1 M1: the obstruction holds AT UNBOUNDED GROWTH ONLY — at any
# bounded horizon the family is FEASIBLE (D5b exhibits the witness).
comp_is_u = all(connected(st) for st in reps.values())
check("D5 [COMPONENT-SIZE] VERDICT: OBSTRUCTED AT UNBOUNDED GROWTH ONLY "
      "(round-1 M1 scope) — every reachable state is connected (D1), so "
      "component size == register count == u + 1 on the whole grammar: the "
      "grading is u-only == the D31A graph-blind class, and the A-theorem "
      "(birth-positive stationary path-covariant graph-blind => pure birth) "
      "kills interactions AS u GROWS WITHOUT BOUND; at every FINITE horizon "
      "the family is feasible (D5b); disconnected substrates are OUT OF "
      "HORIZON (no op disconnects)", comp_is_u)

# D5b: the horizon-EXISTS witness (round-1 M1 — the pin's dichotomy
# honored: EXISTS-candidate at the horizon + obstructed at unbounded
# growth). The witness is EXACTLY D31A's priced bounded-growth escape:
# c must know the size cap U (c < 1/(U(U-1))) — a size-capped record
# universe, extra physics under the program's unbounded-growth grammar.
C0 = F(1, 40)                       # < 1/(U(U-1)) at U = 5
def w_comp(cl):
    if cl[0] == 'i': return C0
    s = cl[1]
    return (1 - (s - 1) * (s - 2) * C0) / (s - 1)
comp_classes = set()
for st in reps.values():
    for op in opportunities(st): comp_classes.add(cls_COMP(st, op))
    for y, st2 in births(st):
        for op in opportunities(st2): comp_classes.add(cls_COMP(st2, op))
wmap_comp = {cl: w_comp(cl) for cl in comp_classes}
pos_ok = all(v > 0 for v in wmap_comp.values())
graded_ok = len({wmap_comp[cl] for cl in comp_classes if cl[0] == 'b'}) > 1
z_ok = all(sum(wmap_comp[cls_COMP(st, op)] for op in opportunities(st)) == 1
           for st in reps.values())
cov_ok, bad_c, npairs = verify_covariance(reps, cls_COMP, wmap_comp)
check("D5b [COMPONENT-SIZE at the HORIZON] EXISTS-candidate — the witness "
      "kernel w_i = c = 1/40, w_b(s) = (1 - (s-1)(s-2)c)/(s-1): positive, "
      "GENUINELY s-graded (w_b varies), Z == 1 identically, and exactly "
      "path-covariant on EVERY independent two-op pair of the horizon "
      "(the same witness class works at any finite cap U with "
      "c < 1/(U(U-1)); only unbounded u forces c = 0 — the D31A escape, "
      "priced: c encodes the cap)", pos_ok and graded_ok and z_ok and cov_ok,
      f"{npairs} independent pairs verified exactly; w_b(3..6) = "
      f"{w_comp(('b',3))}, {w_comp(('b',4))}, {w_comp(('b',5))}, "
      f"{w_comp(('b',6))}")

# D6: the landscape, hardened (round-1 m4: limits scoped to the EXISTS side)
print("      D6 THE LANDSCAPE AFTER O3 [supersedes d31c C5's open arm]:")
print("        multiplicity-insensitive + birth-inert gradings: OBSTRUCTED")
print("          (d31c C2/C3 — d_cover, static-age, component-indicator);")
print("        simple-graph degree: OBSTRUCTED AT THE HORIZON (D2 — and by")
print("          the single-row + raw certificates, at EVERY horizon);")
print("        distance-degree (family ii, the #139 debt O3): OBSTRUCTED AT")
print("          THE HORIZON (D3 — same strength);")
print("        tree-substrate motifs: OBSTRUCTED (D4 — never escaped")
print("          birth-inertness; #139's open-arm clause was FALSE for")
print("          motifs — corrected, see LEDGER #144);")
print("        component-size: OBSTRUCTED AT UNBOUNDED GROWTH ONLY (D5 ->")
print("          D31A); EXISTS at every finite horizon (D5b — the priced")
print("          bounded-growth escape, c encodes the cap);")
print("        none-absorbing: bounded-domain only (d31c C4 / #139 M2);")
print("        K_flat teleological: horizon-dependent (D28b R5).")
print("      SCOPE OF THE LIMITS (round-1 m4): the u <= 5 horizon and the")
print("      two-op closure weaken ONLY exists-side claims — every two-op")
print("      equation is a NECESSARY condition of full path-covariance, so")
print("      the three negative verdicts are closure-depth-independent and")
print("      horizon-monotone (deeper systems contain these rows; MOTIF's")
print("      inertness is a pendant-vertex lemma at all sizes). What is NOT")
print("      decided here: richer gradings (multi-radius degree profiles,")
print("      age-degree products) and the exists side beyond u <= 5. The O7")
print("      fork stands: all of this presumes the covariance quotient is")
print("      physical (accretion order = gauge); if order is recorded")
print("      history, the whole axis re-opens.")
check("D6 the landscape printed with EXISTS-side-scoped limits + the O7 "
      "pointer", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: D1 structural, D2-D5 verdicts, "
      f"D5b the horizon witness, D6 print)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
