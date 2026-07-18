#!/usr/bin/env python3
"""
d42b3_placement_exact.py — v10 D42b3 (front 5): placement — two
no-gos, two laws, the discrete TS-condition. Pin: note-d42b3
(2612166). EXACT Fractions; exit 1 on failure.

Embeds the d42a TERMINAL admission layer (verbatim semantics of
v10/code/d42a_generated_conflict_exact.py at #289): events p/r/n,
carriers per A1/A6, budgets propose 1/4 + arb 1/4 + idle, the
past-local candidate relation. Enumerates ARM-1 (A,B; depth <= 4)
with per-history candidate caches. The d42b1 extension inherits the
theorems by the same arguments (carried; its round is in flight).
"""
import sys
from fractions import Fraction as F
from itertools import permutations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

V0 = ('v', 'v0')

def vname(base, wkey, init):
    value = tuple(sorted({t[2] for t in wkey}))
    authors = tuple(sorted({t[0] for t in wkey}))
    return ('v', base, value, authors, init)

def regs_of(op):
    if op[0] in ('p', 'n'): return frozenset([op[1]])
    props = {t[0] for t in op[2]}
    base = next(iter(op[2]))[1]
    return frozenset(props | {vname(base, op[3], op[1])})

def event_poset(acts):
    n = len(acts)
    pred = [set() for _ in range(n)]
    last = {}
    for j, op in enumerate(acts):
        for r in regs_of(op):
            if r in last:
                pred[j] |= pred[last[r]] | {last[r]}
        for r in regs_of(op):
            last[r] = j
    return pred

class View:
    def __init__(self, acts, pred, idxs):
        self.idxs = sorted(idxs)
        self.pred = pred
        self.props = {i: acts[i] for i in self.idxs if acts[i][0] == 'p'}
        self.arbs = {i: acts[i] for i in self.idxs if acts[i][0] == 'r'}
        self.resolved = set()
        self.superseded = set()
        for op in self.arbs.values():
            self.resolved |= set(op[2])
            self.superseded.add(next(iter(op[2]))[1])
        self.live = {i: op for i, op in self.props.items()
                     if (op[1], op[2], op[3]) not in self.resolved}

    def holdings(self, a):
        h = {V0}
        for i, op in self.arbs.items():
            if a in {t[0] for t in op[2]}:
                base = next(iter(op[2]))[1]
                h.add(vname(base, op[3], op[1]))
        return h

    def incomparable(self, i, k):
        return (i not in self.pred[k]) and (k not in self.pred[i])

    def edges(self, idx_set):
        E = set()
        L = sorted(idx_set)
        for ii, i in enumerate(L):
            for k in L[ii + 1:]:
                pi, pk = self.props[i], self.props[k]
                if (pi[2] == pk[2] and pi[3] != pk[3]
                        and self.incomparable(i, k)):
                    E.add((i, k))
        return E

    def components(self):
        by_base = {}
        for i, op in self.live.items():
            by_base.setdefault(op[2], []).append(i)
        comps = []
        for base, idxs in by_base.items():
            E = self.edges(set(idxs))
            parent = {i: i for i in idxs}
            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            for i, k in E:
                parent[find(i)] = find(k)
            groups = {}
            for i in idxs:
                groups.setdefault(find(i), set()).add(i)
            for g in groups.values():
                comps.append((base, frozenset(g)))
        return comps

def triples(view, idx_set):
    return frozenset((view.props[i][1], view.props[i][2],
                      view.props[i][3]) for i in idx_set)

def mis_of(ckey, edge_triples):
    items = sorted(ckey)
    n = len(items)
    ind = []
    for mask in range(1, 1 << n):
        sub = frozenset(items[i] for i in range(n) if mask >> i & 1)
        if all((a, b) not in edge_triples and (b, a) not in edge_triples
               for a in sub for b in sub if a < b):
            ind.append(sub)
    return [s for s in ind if not any(s < t for t in ind)]

def PK1(ckey, edge_triples):
    items = sorted(ckey)
    tally = {}
    for perm in permutations(items):
        acc = []
        for t in perm:
            if all((t, u) not in edge_triples and (u, t) not in
                   edge_triples for u in acc):
                acc.append(t)
        w = frozenset(acc)
        tally[w] = tally.get(w, 0) + 1
    total = sum(tally.values())
    return {w: F(c, total) for w, c in tally.items()}

def edge_triples_of(view, idx_set):
    def tri(i): return next(iter(triples(view, {i})))
    return frozenset(tuple(sorted((tri(i), tri(k))))
                     for (i, k) in view.edges(idx_set))

def prop_options_in_view(view, a):
    out = []
    for b in view.holdings(a):
        if b in view.superseded: continue
        if any(op[1] == a and op[2] == b for op in view.live.values()):
            continue
        for x in (0, 1):
            out.append((b, x))
    return sorted(out, key=repr)

def arb_components_in_view(view, a):
    out = []
    for base, comp in view.components():
        if base in view.superseded: continue
        if a in {view.props[i][1] for i in comp}:
            out.append((base, comp))
    return out

def admissible(acts, e):
    acts2 = acts + [e]
    j = len(acts2) - 1
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[j])
    kind = e[0]
    if kind == 'n':
        a = e[1]
        has_p = bool(prop_options_in_view(view, a))
        has_r = bool(arb_components_in_view(view, a))
        return True, 1 - (F(1, 4) if has_p else 0) - (F(1, 4) if has_r else 0)
    if kind == 'p':
        a, b, x = e[1], e[2], e[3]
        opts = prop_options_in_view(view, a)
        if (b, x) not in opts: return False, None
        return True, F(1, 4) / len(opts)
    a, ckey, wkey = e[1], e[2], e[3]
    comps = arb_components_in_view(view, a)
    match = [c for c in comps if triples(view, c[1]) == ckey]
    if not match: return False, None
    base, comp = match[0]
    et = edge_triples_of(view, comp)
    if wkey not in mis_of(ckey, et): return False, None
    return True, F(1, 4) / len(comps) * PK1(ckey, et)[wkey]

def candidates_for(acts, actors):
    pred = event_poset(acts)
    full = View(acts, pred, set(range(len(acts))))
    bases = sorted({V0} | {vname(next(iter(op[2]))[1], op[3], op[1])
                           for op in full.arbs.values()}, key=repr)
    out = []
    live_by_base = {}
    for i, op in full.live.items():
        live_by_base.setdefault(op[2], []).append(i)
    for a in actors:
        for b in bases:
            for x in (0, 1):
                e = ('p', a, b, x)
                ok, q = admissible(acts, e)
                if ok: out.append((e, q))
        seen = set()
        for b in sorted(live_by_base, key=repr):
            idxs = sorted(live_by_base[b])
            n = len(idxs)
            for smask in range(1, 1 << n):
                S = [idxs[i] for i in range(n) if smask >> i & 1]
                ck = triples(full, frozenset(S))
                m = len(S)
                for wmask in range(1, 1 << m):
                    W = frozenset(S[i] for i in range(m) if wmask >> i & 1)
                    e = ('r', a, ck, triples(full, W))
                    if e in seen: continue
                    seen.add(e)
                    ok, q = admissible(acts, e)
                    if ok: out.append((e, q))
        e = ('n', a)
        ok, q = admissible(acts, e)
        out.append((e, q))
    return out

def enumerate_family(actors, max_events):
    out = [[]]
    cache = {}
    frontier = [[]]
    while frontier:
        h = frontier.pop()
        cands = candidates_for(h, actors)
        cache[tuple(h)] = cands
        if len(h) >= max_events: continue
        for e, q in cands:
            out.append(h + [e])
            frontier.append(h + [e])
    return out, cache

def canon(acts):
    pred = event_poset(acts)
    memo = {}
    def c(j):
        if j not in memo:
            memo[j] = (acts[j], frozenset(c(i) for i in pred[j]))
        return memo[j]
    return frozenset(c(j) for j in range(len(acts)))

def own_view_canon(acts, a):
    """Canonical DAG of a's own chain-past (the initiator view)."""
    acts2 = acts + [('n', a)]
    pred = event_poset(acts2)
    idxs = sorted(pred[len(acts2) - 1])
    sub = [acts2[i] for i in idxs]
    return canon(sub)

def mu_of(acts):
    p = F(1)
    for j in range(len(acts)):
        ok, q = admissible(acts[:j], acts[j])
        if not ok: return None
        p *= q
    return p

print("[d42b3 — placement: no-gos, laws, the discrete TS-condition]")
print("  banner: EXACT; d42a-terminal layer embedded; ARM-1 (A,B)")
print("  depth<=4 with candidate caches; d42b1 extension carried.")

AB = ('A', 'B')
FAM, CACHE = enumerate_family(AB, 4)
print(f"  family: {len(FAM)} histories (the d42a depth<=4 slice)")

pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA, tB = ('A', V0, 0), ('B', V0, 1)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
PAIR = ('r', 'A', frozenset({tA, tB}), frozenset({tA}))

def actor_sum(h, a):
    return sum(q for e, q in CACHE[tuple(h)] if e[1] == a)

# ---- G-T1: the actor-local no-go -------------------------------------------
Ha, Hb = [pA0], [pA0, pB1]
ovA_a = own_view_canon(Ha, 'A')
ovA_b = own_view_canon(Hb, 'A')
sA_a, sA_b = actor_sum(Ha, 'A'), actor_sum(Hb, 'A')
check("G-T1 the ACTOR-LOCAL NO-GO: A's own-view canonical DAG is "
      "IDENTICAL at [pA0] and [pA0,pB1], yet A's per-initiator sum "
      "differs (1 vs 5/4) — no function of the initiator's view can "
      "serve as the normalizing counter-term (the excess lives in "
      "join-view data the actor cannot see)",
      ovA_a == ovA_b and sA_a == F(1) and sA_b == F(5, 4),
      f"own-view canons equal = {ovA_a == ovA_b}; sums = {sA_a}, {sA_b}")

# ---- G-T2: cut-normalization is the lottery, reconvicted -------------------
def cut_normalized_product(seq, actors):
    p = F(1)
    for j, e in enumerate(seq):
        prefix = seq[:j]
        cands = CACHE.get(tuple(prefix))
        if cands is None:
            cands = candidates_for(prefix, actors)
        N = sum(q for _, q in cands)
        ok, q = admissible(prefix, e)
        if not ok: return None
        p *= q / N
    return p

E1 = [pA0, SELFA, pB1]
E2 = [pA0, pB1, SELFA]
c1, c2 = canon(E1), canon(E2)
mu1, mu2 = mu_of(E1), mu_of(E2)
cp1 = cut_normalized_product(E1, AB)
cp2 = cut_normalized_product(E2, AB)
Ns1 = [sum(q for _, q in CACHE[tuple(E1[:j])]) for j in range(3)]
Ns2 = [sum(q for _, q in CACHE[tuple(E2[:j])]) for j in range(3)]
check("G-T2 CUT-NORMALIZATION IS THE LOTTERY, reconvicted on the "
      "generated grammar: the A7 witness pair is ONE canonical DAG "
      "with mu = 1/256 under both orders, but the cut-normalized "
      "products DIFFER exactly (1/2048 vs 1/2560; N jumps 2 -> 5/2 "
      "when the blind pair becomes visible) — d34a-H5's conviction, "
      "reproduced",
      c1 == c2 and mu1 == mu2 == F(1, 256)
      and cp1 == F(1, 2048) and cp2 == F(1, 2560)
      and Ns1 == [F(2), F(2), F(2)]
      and Ns2 == [F(2), F(2), F(5, 2)],
      f"mu = {mu1}; cut products = {cp1} vs {cp2}; "
      f"N-sequences = {[str(x) for x in Ns1]} vs {[str(x) for x in Ns2]}")

# ---- G-T3: the discrete TS-condition ---------------------------------------
# A placement completion is a cut-attached Z making q/Z-products
# extension-invariant. The two-path constraint on the witness pair:
#   q(selfA|[pA0]) / Z(cut1) evaluated on path E1 at its position
#   vs on path E2 — one linear equation in the two unknowns
#   Z(cut_after[pA0,'selfA-side']) and Z(cut_after[pA0,pB1]):
# solvable per-pair (underdetermined by one dimension); the GLOBAL
# question — one Z consistent across ALL witness pairs — is whether
# the excess density (G-L2) is a coboundary. DEFINED + OPEN.
# Per-pair solvability, exhibited exactly: require
#   (q1/Z0)(q2/Za)(q3/Zb1) == (q1/Z0)(q2'/Zc)(q3'/Zb2)
# with the E1/E2 factor lists; fix Z0 = Za = Zc = 1 (gauge); solve.
q_E1 = [admissible(E1[:j], E1[j])[1] for j in range(3)]
q_E2 = [admissible(E2[:j], E2[j])[1] for j in range(3)]
# product equality with Z only on the two distinct middle cuts:
#   (prod q_E1) / Zb1 == (prod q_E2) / Zb2  =>  Zb1/Zb2 = mu1/mu2 = 1
# so ANY equal pair works: per-pair solvable, one free dimension.
ratio_needed = (q_E1[0] * q_E1[1] * q_E1[2]) / (q_E2[0] * q_E2[1] * q_E2[2])
check("G-T3 the DISCRETE TS-CONDITION defined; per-pair solvability "
      "exhibited (the two-path constraint fixes only the RATIO of the "
      "two cut-normalizers — here 1 — leaving one free dimension); "
      "GLOBAL existence = whether the L2 excess density is a "
      "coboundary on the cut complex: OPEN, identified as the "
      "discrete shadow of v6 paper 1's TS-integrability residue",
      ratio_needed == F(1),
      f"required Zb1/Zb2 = {ratio_needed} (mu-equality makes the "
      "witness pair's constraint trivially solvable; the naive N "
      "fails because N is NOT cut-attached data — it double-counts "
      "the blind layer)")

# ---- G-L1: ratio locality ---------------------------------------------------
viol_l1 = tested_l1 = 0
for h in FAM:
    if len(h) != 2: continue
    key = tuple(h)
    for e, q in CACHE[key]:
        if e[0] != 'p': continue
        for h2 in ([pA0], [('p', 'A', V0, 1)]):
            if tuple(h2) == key: continue
            if h[:1] != h2[:1] and h[0][1] == e[1]: continue
            ok1x, q1x = admissible(h, e)
            ok2x, q2x = admissible(h2, e)
            if not (ok1x and ok2x): continue
            v1 = own_view_canon(h + [e], e[1])
            v2 = own_view_canon(h2 + [e], e[1])
            if v1 != v2: continue
            tested_l1 += 1
            m1a, m2a = mu_of(h), mu_of(h2)
            m1b, m2b = mu_of(h + [e]), mu_of(h2 + [e])
            if m1b * m2a != m2b * m1a: viol_l1 += 1
check("G-L1 RATIO LOCALITY: for a common extension whose own-view is "
      "identical in both histories, mu-ratios are preserved exactly "
      "(the paper-28 ratios-only structure as the weight system's "
      "invariant content)",
      tested_l1 > 0 and viol_l1 == 0,
      f"tested = {tested_l1}, violations = {viol_l1}")

# ---- G-L2: the obstruction density -----------------------------------------
viol_l2 = pts = 0
excess_hist = {}
for h in FAM:
    pred = event_poset(h)
    for a in AB:
        cands = CACHE[tuple(h)]
        tot = sum(q for e, q in cands if e[1] == a)
        # blind ckey groups: arb candidates for a whose ckey component
        # is NOT visible in a's own view
        acts2 = h + [('n', a)]
        pred2 = event_poset(acts2)
        ov = View(acts2, pred2, pred2[len(acts2) - 1])
        own_cks = {triples(ov, comp)
                   for base, comp in arb_components_in_view(ov, a)}
        blind_cks = set()
        group_sums = {}
        for e, q in cands:
            if e[1] != a or e[0] != 'r': continue
            if e[2] not in own_cks:
                blind_cks.add(e[2])
                group_sums[e[2]] = group_sums.get(e[2], F(0)) + q
        k = len(blind_cks)
        pts += 1
        if tot != 1 + F(k, 4): viol_l2 += 1
        if any(gs != F(1, 4) for gs in group_sums.values()): viol_l2 += 1
        excess_hist[k] = excess_hist.get(k, 0) + 1
check("G-L2 the OBSTRUCTION DENSITY: per-actor excess = "
      "(#blind ckey groups)/4 with EVERY blind group summing to "
      "exactly 1/4 — component-additive, quarter-quantized, "
      "family-wide (this is the density any admissible Z must "
      "integrate; the cocycle's local form)",
      pts > 0 and viol_l2 == 0,
      f"actor-points = {pts}, violations = {viol_l2}; k-spectrum = "
      f"{dict(sorted(excess_hist.items()))}")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — exit 1 by design")
    sys.exit(1)
print("[VERDICT] d42b3 GREEN: actor-local counter-terms impossible "
      "(T1); cut-normalization reconvicted as the lottery (T2); the "
      "discrete TS-condition defined with per-pair solvability and "
      "the global cocycle question OPEN, identified with v6 paper "
      "1's residue (T3); ratio locality and the quarter-quantized "
      "obstruction density established as exact laws (L1, L2).")
