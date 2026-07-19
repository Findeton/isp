#!/usr/bin/env python3
"""
d43d_dstar_generated_exact.py — v10 D43d (N4): the canonical-D*
two-clock instrument on the generated families. Pin: note-d43d
(4a6bb9c). Algorithms ported code-faithfully from the committed v8
receipts (g2/i1/i2 per the extraction record); the d42 layers exec'd
from the committed d42b3/d42b1 receipts (single source). Exact
Fractions for D* (rank coordinates are rationals; the star sweep is
exact). Exit 1 on anchor/port breakage; the NG3 dimension outcome is
PRE-REGISTERED as open (either answer is a result).
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations

sys.setrecursionlimit(300000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ---- the committed dim<=2 oracle (g2, backtracking + forcing) --------------
def is_comparability(nodes, edges):
    adj = set()
    for a, b in edges:
        adj.add((a, b)); adj.add((b, a))
    direction = {}
    def force(a, b):
        changed = []
        stack = [(a, b)]
        while stack:
            x, y = stack.pop()
            key = frozenset((x, y))
            if key in direction:
                if direction[key] != (x, y):
                    for k in changed: del direction[k]
                    return None
                continue
            direction[key] = (x, y)
            changed.append(key)
            for z in nodes:
                if z == x or z == y: continue
                kz = frozenset((y, z))
                if kz in direction and direction[kz] == (y, z):
                    if (x, z) in adj: stack.append((x, z))
                    else:
                        for k in changed: del direction[k]
                        return None
                kz2 = frozenset((z, x))
                if kz2 in direction and direction[kz2] == (z, x):
                    if (z, y) in adj: stack.append((z, y))
                    else:
                        for k in changed: del direction[k]
                        return None
        return changed
    edge_list = [frozenset(e) for e in edges]
    def bt(ei):
        while ei < len(edge_list) and edge_list[ei] in direction:
            ei += 1
        if ei == len(edge_list): return True
        a, b = tuple(edge_list[ei])
        for (x, y) in ((a, b), (b, a)):
            ch = force(x, y)
            if ch is not None:
                if bt(ei + 1): return True
                for k in ch: del direction[k]
        return False
    ok = bt(0)
    return ok, dict(direction)

def topo_rank(n, less):
    indeg = [0] * n
    for i in range(n):
        for j in range(n):
            if less[i][j]: indeg[j] += 1
    order = []
    avail = sorted(i for i in range(n) if indeg[i] == 0)
    while avail:
        x = avail.pop(0)
        order.append(x)
        for j in range(n):
            if less[x][j]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    avail.append(j); avail.sort()
    if len(order) != n: return None
    rank = [0] * n
    for r, x in enumerate(order): rank[x] = r
    return rank

def dim_le_2(C, want_realizer=False):
    n = len(C)
    incomp = [(i, j) for i in range(n) for j in range(i + 1, n)
              if not C[i][j] and not C[j][i]]
    ok, orient = is_comparability(list(range(n)), incomp)
    if not ok: return False, None
    F = [[False] * n for _ in range(n)]
    for key, (x, y) in orient.items():
        F[x][y] = True
    L1 = [[C[i][j] or F[i][j] for j in range(n)] for i in range(n)]
    L2 = [[C[i][j] or F[j][i] for j in range(n)] for i in range(n)]
    r1, r2 = topo_rank(n, L1), topo_rank(n, L2)
    if r1 is None or r2 is None: return False, None
    return True, (r1, r2)

def all_orientation_ranks(C, cap=64):
    """Enumerate ALL transitive orientations (committed
    count_orientations pattern), returning the rank pairs; capped."""
    n = len(C)
    incomp = [frozenset((i, j)) for i in range(n)
              for j in range(i + 1, n)
              if not C[i][j] and not C[j][i]]
    adj = set()
    for e in incomp:
        a, b = tuple(e)
        adj.add((a, b)); adj.add((b, a))
    results = []
    direction = {}
    def force(a, b):
        changed = []
        stack = [(a, b)]
        while stack:
            x, y = stack.pop()
            key = frozenset((x, y))
            if key in direction:
                if direction[key] != (x, y):
                    for k in changed: del direction[k]
                    return None
                continue
            direction[key] = (x, y)
            changed.append(key)
            for z in range(n):
                if z == x or z == y: continue
                if direction.get(frozenset((y, z))) == (y, z):
                    if (x, z) in adj: stack.append((x, z))
                    else:
                        for k in changed: del direction[k]
                        return None
                if direction.get(frozenset((z, x))) == (z, x):
                    if (z, y) in adj: stack.append((z, y))
                    else:
                        for k in changed: del direction[k]
                        return None
        return changed
    def bt(ei):
        if len(results) >= cap: return
        while ei < len(incomp) and incomp[ei] in direction:
            ei += 1
        if ei == len(incomp):
            F = [[False] * n for _ in range(n)]
            for key, (x, y) in direction.items():
                F[x][y] = True
            L1 = [[C[i][j] or F[i][j] for j in range(n)]
                  for i in range(n)]
            L2 = [[C[i][j] or F[j][i] for j in range(n)]
                  for i in range(n)]
            r1, r2 = topo_rank(n, L1), topo_rank(n, L2)
            if r1 is not None and r2 is not None:
                results.append((r1, r2))
            return
        a, b = tuple(incomp[ei])
        for (x, y) in ((a, b), (b, a)):
            ch = force(x, y)
            if ch is not None:
                bt(ei + 1)
                for k in ch: del direction[k]
    bt(0)
    return results

def star_discrepancy_exact(pts):
    """Exact anchored-box discrepancy, both closure sides; pts are
    (Fraction, Fraction) pairs."""
    N = len(pts)
    us = sorted({p[0] for p in pts} | {Fr(1)})
    vs = sorted({p[1] for p in pts} | {Fr(1)})
    best = Fr(0)
    for a in us:
        open_v = sorted(p[1] for p in pts if p[0] < a)
        clos_v = sorted(p[1] for p in pts if p[0] <= a)
        for b in vs:
            for sv in (open_v, clos_v):
                lo = sum(1 for v in sv if v < b)
                hi = sum(1 for v in sv if v <= b)
                for cnt in (lo, hi):
                    d = abs(Fr(cnt, N) - a * b)
                    if d > best: best = d
    return best

def emb(r1, r2):
    n = len(r1)
    return [(Fr(2 * r1[i] + 1, 2 * n), Fr(2 * r2[i] + 1, 2 * n))
            for i in range(n)]

def dstar_min_max(C, cap=64):
    ranks = all_orientation_ranks(C, cap)
    vals = [star_discrepancy_exact(emb(r1, r2)) for r1, r2 in ranks]
    return (min(vals), max(vals), len(ranks)) if vals else (None, None, 0)

print("[d43d — canonical D* on the generated families]")
print("  banner: g2/i1/i2 algorithms extraction-ported; EXACT")
print("  Fraction D*; the d42 layers exec'd from committed receipts;")
print("  NO manifoldlikeness verdicts at n <= 5 (pin §1); the NG3")
print("  chain dimension outcome is PRE-REGISTERED open; statistical")
print("  layer nan-DISCLOSED (zero qualifying pairs at these n).")

# ---- NG1: port fidelity -----------------------------------------------------
# S3: minimal a0,a1,a2; maximal b0,b1,b2; ai < bj iff i != j
n6 = 6
C6 = [[False] * n6 for _ in range(n6)]
for i in range(3):
    for j in range(3):
        if i != j: C6[i][3 + j] = True
okS3, _ = dim_le_2(C6)

def all_posets(n):
    """All labeled strict partial orders on n elements (transitively
    closed relations)."""
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    out = []
    for mask in range(1 << len(pairs)):
        C = [[False] * n for _ in range(n)]
        for b, (i, j) in enumerate(pairs):
            if mask >> b & 1: C[i][j] = True
        ok = True
        for i in range(n):
            if not ok: break
            for j in range(n):
                if C[i][j] and C[j][i]: ok = False; break
                if not C[i][j]: continue
                for k in range(n):
                    if C[j][k] and not C[i][k]: ok = False; break
        if ok: out.append(C)
    return out

P4 = all_posets(4)
ok4 = len(P4) == 219 and all(dim_le_2(C)[0] for C in P4)
rng = set()
ident = list(range(5))
for sig in permutations(range(5)):
    rng.add(star_discrepancy_exact(emb(ident, list(sig))))
ok5rng = (min(rng) == Fr(1, 4) and max(rng) == Fr(7, 20))
check("NG1 PORT FIDELITY: S3 (6 elements) REJECTED by dim<=2; all "
      "219 labeled 4-posets PASS; the full 120-permutation n=5 D* "
      "range = [1/4, 7/20] exactly (the extraction's committed "
      "anchors)",
      (not okS3) and ok4 and ok5rng,
      f"S3 dim<=2 = {okS3}; n=4 posets = {len(P4)}; n=5 range = "
      f"[{min(rng)}, {max(rng)}]")

# ---- the d42 layers ---------------------------------------------------------
_src3 = open('v10/code/d42b3_placement_exact.py').read()
ns3 = {}
exec(_src3[:_src3.index('print("[d42b3')], ns3)
_src1 = open('v10/code/d42b1_transport_exact.py').read()
ns1 = {}
exec(_src1[:_src1.index('print("[d42b1')], ns1)

def poset_of(h, ns):
    pred = ns['event_poset'](h)
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]

# ---- NG2: the n=4 landscape + the d42a family sweep ------------------------
land4 = sorted(dstar_min_max(C)[0] for C in P4)
V0 = ns3['V0']
AB = ('A', 'B')
FAM = [[]]
frontier = [[]]
CACHE = {}
while frontier:
    h = frontier.pop()
    CACHE[tuple(h)] = ns3['candidates_for'](h, AB)
    if len(h) >= 4: continue
    for e, q in CACHE[tuple(h)]:
        FAM.append(h + [e]); frontier.append(h + [e])
recs = [(h, ns3['mu_of'](h)) for h in FAM if len(h) == 4]
wsum = sum(m for _, m in recs)
fam_scores = []
for h, m in recs:
    dmin, dmax, cnt = dstar_min_max(poset_of(h, ns3))
    fam_scores.append((dmin, m))
w_mean = sum(d * m for d, m in fam_scores) / wsum
land_mean = sum(land4) / len(land4)
below = sum(m for d, m in fam_scores
            if sum(1 for x in land4 if x <= d) <= len(land4) // 2)
check("NG2 the exact n=4 landscape (219 posets, min-over-"
      "orientations D*) + the d42a depth-4 family sweep "
      "(mu-weighted; descriptors ONLY per pin §1)",
      len(land4) == 219 and len(recs) > 0 and wsum > 0,
      f"landscape D* in [{min(land4)}, {max(land4)}], mean "
      f"{land_mean} (~{float(land_mean):.4f}); family mu-weighted "
      f"mean D* = {w_mean} (~{float(w_mean):.4f}); mu-mass at-or-"
      f"below landscape median = {below}/{wsum} [MEASURED, "
      "descriptor]")

# ---- NG3: the chain suite (the verdict-capable gate) -----------------------
vname = ns1['vname']; mname = ns1['mname']; value_of = ns1['value_of']
pA0 = ('p', 'A', V0, 0)
pC1 = ('p', 'C', V0, 1)
tA, tC = ('A', V0, 0), ('C', V0, 1)
rA = ('r', 'A', frozenset({tA}), frozenset({tA}))
rC = ('r', 'C', frozenset({tC}), frozenset({tC}))
v1 = vname(V0, frozenset({tA}), 'A')
vC = vname(V0, frozenset({tC}), 'C')
dA = ('d', 'A', 'B', v1)
dC = ('d', 'C', 'B', vC)
PK = tuple(sorted((v1, vC), key=repr))
mB = ('m', 'B', PK, v1)
vm = mname(PK, value_of(v1), 'B')
SIG_FM = [pA0, pC1, rA, rC, dA, dC, mB, ('p', 'B', vm, 1)]
pB1v0 = ('p', 'B', V0, 1)
SIG_KR = [pA0, rA, pB1v0, dA]
tB_ = ('B', V0, 1)
h5 = [pA0, ('p', 'B', V0, 1), ('d', 'B', 'C', V0),
      ('d', 'C', 'A', V0), ('r', 'B', frozenset({tB_}),
                            frozenset({tB_}))]
tAv1 = ('A', v1, 1)
h11 = SIG_FM[:6] + [('p', 'B', v1, 0), ('p', 'A', v1, 1),
                    ('d', 'A', 'C', v1), ('d', 'C', 'B', vC),
                    ('r', 'A', frozenset({tAv1}), frozenset({tAv1}))]
h12 = h11 + [('p', 'B', vC, 0)]
pD0 = ('p', 'D', V0, 0)
tD0 = ('D', V0, 0)
rD0 = ('r', 'D', frozenset({tD0}), frozenset({tD0}))
vD0 = vname(V0, frozenset({tD0}), 'D')
CH = [pA0, pC1, pD0, rA, rC, rD0, dA, dC, mB, ('d', 'D', 'B', vD0)]
chains = [("SIG_KR", SIG_KR), ("h5", h5), ("SIG_FM", SIG_FM),
          ("CH", CH), ("h11", h11), ("h12", h12)]
rows = []
ok3 = True
for name, h in chains:
    C = poset_of(h, ns1)
    ok2d, ranks = dim_le_2(C)
    if not ok2d:
        rows.append(f"{name}(n={len(h)}): DIM>2 — REJECTED")
        continue
    dmin, dmax, cnt = dstar_min_max(C, cap=64)
    r1, r2 = ranks
    # parity invariance (the relabeling lemma check)
    dsw = star_discrepancy_exact(emb(r2, r1))
    dcan = star_discrepancy_exact(emb(r1, r2))
    ok3 &= (dsw == dcan)
    rows.append(f"{name}(n={len(h)}): 2D, D* in [{dmin}, {dmax}] "
                f"over {cnt} orientations; canonical {dcan} "
                f"(~{float(dcan):.4f}); two-clock (b, chi) = ranks "
                "delivered")
n_rej = sum(1 for r in rows if "REJECTED" in r)
check("NG3 THE CHAIN SUITE (pre-registered open): dim<=2 verdict "
      "per constructed transport chain; parity invariance exact on "
      "every 2D chain",
      len(rows) == 6 and ok3,
      " | ".join(rows))
print(f"  NG3 outcome: {n_rej}/6 chains REJECTED (dim > 2) — "
      + ("TRANSPORT GENERATES DIMENSION at chain scale"
         if n_rej else "every constructed chain is a TWO-CLOCK "
         "configuration (paper 13 universality holds at chain "
         "scale)"))

check("NG4 disclosures: statistical layer nan (zero qualifying "
      "pairs at n <= 12 with exp_k >= 10 unverified here — the "
      "layer is NOT RUN, per the pin's nan-disclosure convention); "
      "no manifoldlikeness verdict anywhere in this receipt",
      True, "scope per pin §1")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — port/anchor breakage; exit 1")
    sys.exit(1)
print("[VERDICT] d43d delivered: port-faithful D* instrument; the "
      "n<=4 family = descriptors only (floor-dominated, disclosed); "
      f"the chain-scale dimension question ANSWERED: {n_rej}/6 "
      "rejections — see NG3.")
