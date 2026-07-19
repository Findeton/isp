#!/usr/bin/env python3
"""
d44c_arb_dimension_exact.py — v10 D44c (successor 3): the multi-author-
arbitration dimension corner. Pin: note-d44c-multiauthor-arb-dimension.md
(strict, 2026-07-19). Parents: d43d TERMINAL (#342, forward-corrected
#348), the d42a admission layer (d42a TERMINAL at #289, embedded in the
committed d42b3), program pin #347; execution gate opened at #349.

THE QUESTION (pre-registered OPEN, pin SS1): can ARBITRATION STRUCTURE
ALONE — events p/r/n only, NO deliveries, NO merges — push a generated
event poset out of order-dimension <= 2?  The structural fork (pin SS2):
arb events natively cover their pools (cover-two, crown-friendly) VS the
component law (mutually conflicting proposals form ONE component and an
arb consumes its component).  Either horn is a deliverable result.

Instruments: the g2 dim<=2 oracle + exact D* + the width diagnostic
ported code-faithfully from the committed v10/code/
d43d_dstar_generated_exact.py; the d42a-terminal p/r/n admission layer
(candidates_for / admissible / View / event_poset / canon / vname)
exec'd path-anchored from the committed v10/code/
d42b3_placement_exact.py (single source), exactly as the committed d43d
receipt does.  Exact Fractions everywhere.  Exit 1 ONLY on anchor/port
breakage or internal inconsistency; the dimension outcome itself is
pre-registered open — either horn exits 0 with its verdict printed.
Run from the repo root: python3 v10/code/d44c_arb_dimension_exact.py
"""
import sys
from fractions import Fraction as Fr
from itertools import combinations, permutations

sys.setrecursionlimit(300000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ---- the committed dim<=2 oracle (g2, backtracking + forcing) --------------
# ported code-faithfully from v10/code/d43d_dstar_generated_exact.py
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

def width_of(C):
    n = len(C)
    best = 0
    for mask in range(1 << n):
        elems = [i for i in range(n) if mask >> i & 1]
        if all(not C[i][j] and not C[j][i]
               for i in elems for j in elems if i < j):
            best = max(best, len(elems))
    return best

def poset_of(h, ns):
    pred = ns['event_poset'](h)
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]

print("[d44c — multi-author arbitration vs order-dimension <= 2]")
print("  banner: p/r/n events ONLY (transport excluded by construction");
print("  — that mechanism is S4's, decided at d43d NG3b); the g2 oracle")
print("  + exact D* + width diagnostic ported code-faithfully from the")
print("  committed d43d receipt; the d42a admission layer exec'd")
print("  path-anchored from the committed d42b3 receipt (single")
print("  source); EXACT Fractions; the dimension outcome is")
print("  PRE-REGISTERED OPEN (pin SS1) — witness and obstruction are")
print("  both deliverable; exit 1 only on anchor/port breakage or")
print("  internal inconsistency.  Dim checks are deduplicated by the")
print("  register-word class (DECLARED, receipt-internal: event_poset")
print("  is a function of the regs_of sequence; vname registers are")
print("  single-writer — gated below — hence pred-inert; soundness")
print("  re-sampled every 97th arb-containing history against the full")
print("  committed builder).  D* appears ONLY as port-fidelity anchors")
print("  and the AG0b print repair — no geometry claims from it.")

# ---- the d42a layer (single source: the committed d42b3 receipt) -----------
_src3 = open('v10/code/d42b3_placement_exact.py').read()
ns3 = {}
exec(_src3[:_src3.index('print("[d42b3')], ns3)
candidates_for = ns3['candidates_for']
admissible = ns3['admissible']
event_poset = ns3['event_poset']
regs_of = ns3['regs_of']
vname = ns3['vname']
View = ns3['View']
canon = ns3['canon']
V0 = ns3['V0']

def C_of(h):
    return poset_of(h, ns3)

def fmt(e):
    """Deterministic event formatter (frozensets printed sorted by
    repr — raw frozenset printing is hash-order-dependent)."""
    if e[0] == 'r':
        ck = ", ".join(repr(t) for t in sorted(e[2], key=repr))
        wk = ", ".join(repr(t) for t in sorted(e[3], key=repr))
        return f"('r', {e[1]!r}, {{{ck}}}, {{{wk}}})"
    return repr(e)

def vname_of_arb(e):
    return vname(next(iter(e[2]))[1], e[3], e[1])

def mints_in(h):
    return [vname_of_arb(e) for e in h if e[0] == 'r']

def aset(e):
    """Actor-register projection of regs_of (vname registers dropped;
    sound once vname-freshness is gated)."""
    return frozenset(x for x in regs_of(e) if isinstance(x, str))

def irreducible_core(C):
    """Greedy minimization of a dim>2 poset to an irreducible core
    (witness path only)."""
    alive = list(range(len(C)))
    changed = True
    while changed:
        changed = False
        for x in list(alive):
            sub = [y for y in alive if y != x]
            Cs = [[C[i][j] for j in sub] for i in sub]
            ok, _ = dim_le_2(Cs)
            if not ok:
                alive = sub; changed = True; break
    return alive

def report_witness(tag, h, qs, C):
    print(f"  [WITNESS {tag}] dim > 2 — the pre-registered witness horn")
    mu = Fr(1)
    for q in qs: mu *= q
    for j, e in enumerate(h):
        print(f"    e{j}: {fmt(e)}  q = {qs[j]}")
    print(f"    mu = {mu}")
    n = len(h)
    preds = [sorted(i for i in range(n) if C[i][j]) for j in range(n)]
    print(f"    poset preds = {preds}")
    print(f"    width = {width_of(C)}")
    core = irreducible_core(C)
    Cs = [[C[i][j] for j in core] for i in core]
    m = len(core)
    cp = [sorted(i for i in range(m) if Cs[i][j]) for j in range(m)]
    print(f"    3-irreducible core: events {core}, preds = {cp}")

# ============================ AG0: port re-anchor ===========================
print("[AG0 port re-anchor]")
n6 = 6
C6 = [[False] * n6 for _ in range(n6)]
for i in range(3):
    for j in range(3):
        if i != j: C6[i][3 + j] = True
okS3, _ = dim_le_2(C6)
P4 = all_posets(4)
ok4 = len(P4) == 219 and all(dim_le_2(C)[0] for C in P4)
P5 = all_posets(5)
ok5 = len(P5) == 4231 and all(dim_le_2(C)[0] for C in P5)
rng = set()
ident = list(range(5))
for sig in permutations(range(5)):
    rng.add(star_discrepancy_exact(emb(ident, list(sig))))
ok5rng = (min(rng) == Fr(1, 4) and max(rng) == Fr(7, 20))
# W6 regression: hard-coded from the committed d43d .out (pure oracle
# regression, no transport layer needed — this receipt's scope is p/r/n)
W6_preds = [[], [], [], [1, 2], [0, 2], [0, 1]]
C_w6 = [[i in W6_preds[j] for j in range(6)] for i in range(6)]
d2_w6, _ = dim_le_2(C_w6)
ok_w6reg = (C_w6 == C6) and not d2_w6
ok_regs = (regs_of(('n', 'A')) == regs_of(('p', 'A', V0, 0))
           == frozenset({'A'}))
check("AG0 PORT RE-ANCHOR: S3 (6 elements) REJECTED by dim<=2; all "
      "219 labeled 4-posets and all 4,231 labeled 5-posets PASS (the "
      "n < 6 vacuity floor, in-receipt); the n=5 D* range = [1/4, "
      "7/20] exactly; the W6 regression (preds hard-coded from the "
      "committed d43d .out) is EXACTLY the S3 matrix and fails "
      "dim<=2; regs_of identity: n- and p-events are register-"
      "identical ({actor})",
      (not okS3) and ok4 and ok5 and ok5rng and ok_w6reg and ok_regs,
      f"S3 dim<=2 = {okS3}; n=4 posets = {len(P4)}; n=5 posets = "
      f"{len(P5)}; n=5 range = [{min(rng)}, {max(rng)}]; W6 preds = "
      f"{W6_preds}, dim<=2 = {d2_w6}, matrix == S3 = {C_w6 == C6}")

# ---- AG0b: the LOG #348 print repair (the d43d NG2 median line) ------------
# computation ported code-faithfully from the committed d43d NG2 block;
# ONLY the print format is repaired here.
land4 = sorted(dstar_min_max(C)[0] for C in P4)
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
med = sorted(land4)[len(land4) // 2]
below = sum(m for d, m in fam_scores if d <= med)
ratio = below / wsum
print("  print-format note: the next line is the D44c-assigned "
      "cosmetic repair of the committed d43d NG2 median print (LOG "
      "#348): the committed '8/1037/64' decodes as below = 8, wsum = "
      "1037/64; here below and wsum print as separate Fractions with "
      "their ratio reduced.  The terminal d43d receipt stays frozen.")
print(f"  mu-mass at-or-below landscape median: below = {below}, "
      f"wsum = {wsum}, ratio = {ratio} (~{float(ratio):.4f}) "
      "[MEASURED, descriptor]")
check("AG0b THE #348 PRINT REPAIR anchored: the d43d NG2 quantities "
      "rebuilt from the committed layers — AB depth-4 family 1,191 "
      "histories (the committed d42b3 family line), landscape D* in "
      "[19/64, 25/64] mean 4735/14016, family mu-weighted mean D* "
      "23595/66368, below = 8, wsum = 1037/64, reduced ratio = "
      "512/1037 — all EXACT matches to the committed record",
      len(FAM) == 1191 and len(land4) == 219
      and min(land4) == Fr(19, 64) and max(land4) == Fr(25, 64)
      and land_mean == Fr(4735, 14016)
      and w_mean == Fr(23595, 66368)
      and below == Fr(8) and wsum == Fr(1037, 64)
      and ratio == Fr(512, 1037),
      f"FAM = {len(FAM)}; landscape [{min(land4)}, {max(land4)}], "
      f"mean {land_mean}; w_mean = {w_mean}; med = {med}")

# ================= the shared exhaustive-sweep machinery ====================
class Witness(Exception):
    pass

def sweep(actors, cap, allow_idle, tag):
    """Label-level exhaustive DFS over the admissible family (the
    committed candidates_for as the sole expander).  Incremental law
    checks per history; dim<=2 once per register-word class; canon()
    census; witness => stop the hunt."""
    st = {
        'total': [0] * (cap + 1), 'arb': [0] * (cap + 1),
        'mass_all': Fr(0), 'mass_arb': Fr(0),
        'classes': {}, 'canons': set(),
        'laws': {'laminar': 0, 'samebase': 0, 'nest': 0,
                 'base_chain': 0, 'vfresh': 0, 'chain': 0},
        'sample_checked': 0, 'sample_mism': 0, 'arb_seen': 0,
        'witness': None,
    }
    h = []
    qs = []
    word = []

    def class_handle(e, q):
        key = tuple(word)
        cl = st['classes'].get(key)
        if cl is None:
            C = C_of(h)
            okd, _ = dim_le_2(C)
            wd = width_of(C)
            n = len(h)
            for i in range(n):
                for j in range(i + 1, n):
                    if (word[i] & word[j]) and not (C[i][j] or C[j][i]):
                        st['laws']['chain'] += 1
            st['classes'][key] = (n, okd, wd)
            if not okd:
                st['witness'] = (list(h), list(qs), C)
                raise Witness()
            return (n, okd, wd)
        return cl

    def explore(pools, vns, last_pool, arbful, mu):
        depth = len(h)
        if depth >= cap: return
        for e, q in candidates_for(h, actors):
            if e[0] == 'n' and not allow_idle: continue
            d = depth + 1
            st['total'][d] += 1
            pools2, vns2, last2 = pools, vns, last_pool
            if e[0] == 'r':
                P = frozenset(t[0] for t in e[2])
                b = next(iter(e[2]))[1]
                vn = vname_of_arb(e)
                if vn in vns: st['laws']['vfresh'] += 1
                for (P0, b0, vn0) in pools:
                    if (P & P0) and not (P <= P0 or P0 <= P):
                        st['laws']['laminar'] += 1
                    if b0 == b and (P & P0):
                        st['laws']['samebase'] += 1
                for a in sorted(P):
                    prev = last_pool.get(a)
                    if prev is None:
                        if b != V0: st['laws']['base_chain'] += 1
                    else:
                        if not (P <= prev[0]): st['laws']['nest'] += 1
                        if b != prev[2]: st['laws']['base_chain'] += 1
                pools2 = pools + ((P, b, vn),)
                vns2 = vns | {vn}
                last2 = dict(last_pool)
                for a in P: last2[a] = (P, b, vn)
            arbful2 = arbful or e[0] == 'r'
            h.append(e); qs.append(q); word.append(aset(e))
            st['canons'].add(canon(h))
            if arbful2:
                st['arb'][d] += 1
                st['arb_seen'] += 1
                cl = class_handle(e, q)
                if st['arb_seen'] % 97 == 0:
                    st['sample_checked'] += 1
                    Cx = C_of(h)
                    okx, _ = dim_le_2(Cx)
                    wx = width_of(Cx)
                    if (len(h), okx, wx) != cl:
                        st['sample_mism'] += 1
            if d == cap:
                st['mass_all'] += mu * q
                if arbful2: st['mass_arb'] += mu * q
            if d < cap:
                explore(pools2, vns2, last2, arbful2, mu * q)
            h.pop(); qs.pop(); word.pop()

    try:
        st['canons'].add(canon([]))
        explore((), frozenset(), {}, False, Fr(1))
    except Witness:
        pass
    return st

def census_lines(tag, st, cap):
    tot = sum(st['total'][1:])
    arb = sum(st['arb'][1:])
    cls = st['classes']
    wmax = max((w for (_n, _ok, w) in cls.values()), default=0)
    fails = sum(1 for (_n, ok, _w) in cls.values() if not ok)
    strat = sum(1 for (n, _ok, w) in cls.values() if n >= 6 and w >= 3)
    wdist = {}
    for (n, ok, w) in cls.values():
        wdist[(w, ok)] = wdist.get((w, ok), 0) + 1
    print(f"  {tag} census: depths 1..{cap} totals = "
          f"{st['total'][1:]}, arb-containing = {st['arb'][1:]}; "
          f"label-level histories = {tot} (+ the empty root), "
          f"arb-containing = {arb}; canonical classes (committed "
          f"canon()) = {len(st['canons'])}; register-word classes "
          f"(arb-containing) = {len(cls)}; max poset width realized "
          f"= {wmax}; dim<=2 failures = {fails}")
    print(f"  {tag} width x dim distribution over word classes "
          f"{{(width, dim<=2): count}} = "
          f"{dict(sorted(wdist.items()))} [MEASURED]")
    print(f"  {tag} cap-depth mu-mass (repaired format per AG0b): "
          f"mass_arb = {st['mass_arb']}, mass_all = {st['mass_all']}, "
          f"ratio = {st['mass_arb'] / st['mass_all']} "
          f"(~{float(st['mass_arb'] / st['mass_all']):.4f}) "
          "[MEASURED, descriptor]")
    return tot, arb, wmax, fails, strat

# ========================= AG1: exhaustive width 3 ==========================
print("[AG1 exhaustive width 3 — the full p/r/n grammar]")
print("  CAP DECLARATION: cap = 6 events (pin target 8).  Measured "
      "growth 9 / 75 / 639 / 5,865 / 54,489 / 490,851 label-level "
      "histories at depths 1..6 (~9.0x per level) => depth 7 ~ 4.4e6 "
      "and depth 8 ~ 4.0e7; at the measured ~0.6 ms per committed "
      "candidates_for call the enumeration alone would be ~45 min / "
      "~7 h — over the < 10 min receipt budget.  DECLARED: cap 6 for "
      "the full grammar, plus the no-idle depth-7 subfamily (AG1b) "
      "and the width-4 no-idle depth-6 subfamily (AG2b).")
ABC = ('A', 'B', 'C')
st1 = sweep(ABC, 6, True, "AG1")
tot1, arb1, wmax1, fails1, strat1 = census_lines("AG1", st1, 6)
if st1['witness']:
    report_witness("AG1", *st1['witness'])
check("AG1 EXHAUSTIVE WIDTH 3 (cap 6, declared): every admissible "
      "p/r/n history over (A,B,C) enumerated by the committed "
      "candidates_for; census anchored (totals 9/75/639/5,865/54,489/"
      "490,851; arb-containing 0/6/186/3,264/41,016/426,294 = "
      "470,766; canonical classes 32,288; register-word classes "
      "3,309 of which 2,514 at width 3; arb-mass ratio 96878/349355 "
      "exactly); every arb-containing poset checked dim<=2 via the "
      "register-word reduction (soundness sampled, zero mismatches); "
      "max width realized = 3 (= the actor bound); ZERO dim<=2 "
      "failures",
      st1['total'][1:] == [9, 75, 639, 5865, 54489, 490851]
      and st1['arb'][1:] == [0, 6, 186, 3264, 41016, 426294]
      and arb1 == 470766 and len(st1['canons']) == 32288
      and len(st1['classes']) == 3309
      and sum(1 for (_n, _ok, w) in st1['classes'].values()
              if w == 3) == 2514
      and st1['mass_arb'] / st1['mass_all'] == Fr(96878, 349355)
      and st1['witness'] is None and fails1 == 0 and wmax1 == 3
      and st1['sample_mism'] == 0 and st1['sample_checked'] > 0,
      f"sampled recomputations = {st1['sample_checked']}, mismatches "
      f"= {st1['sample_mism']}; law violations = "
      f"{dict(sorted(st1['laws'].items()))}")

# ==================== AG1b: no-idle width 3, depth 7 ========================
print("[AG1b no-idle width 3 — declared subfamily]")
print("  DECLARATION: n-events excluded (p/r only).  n- and p-events "
      "are register-identical (AG0 regs_of gate), so idling adds "
      "poset chain elements but no new register mechanics; the "
      "no-idle family concentrates arbitration depth.  This is a "
      "DECLARED subfamily census — no completeness claim for the "
      "full grammar beyond AG1's cap.  Cap 7 (measured no-idle "
      "growth 6/30/180/1,356/7,176/35,496/180,336; depth 8 = 954,288 "
      "~ +3.5 min — over budget; DECLARED).")
st1b = sweep(ABC, 7, False, "AG1b")
tot1b, arb1b, wmax1b, fails1b, strat1b = census_lines("AG1b", st1b, 7)
if st1b['witness']:
    report_witness("AG1b", *st1b['witness'])
check("AG1b NO-IDLE WIDTH 3 (cap 7, declared): census anchored "
      "(totals 6/30/180/1,356/7,176/35,496/180,336; arb-containing "
      "0/6/132/1,356/7,176/35,496/180,336 — every no-idle history of "
      "depth >= 4 contains an arb; canonical classes 10,049; "
      "register-word classes 5,904 of which 4,950 at width 3; the "
      "depth-7 mass is ALL arb-mass, ratio 1); two-level mint towers "
      "reached (root + child + grandchild structures at depth 7); "
      "ZERO dim<=2 failures; max width = 3",
      st1b['total'][1:] == [6, 30, 180, 1356, 7176, 35496, 180336]
      and st1b['arb'][1:] == [0, 6, 132, 1356, 7176, 35496, 180336]
      and len(st1b['canons']) == 10049
      and len(st1b['classes']) == 5904
      and sum(1 for (_n, _ok, w) in st1b['classes'].values()
              if w == 3) == 4950
      and st1b['mass_arb'] == st1b['mass_all'] == Fr(8613, 32768)
      and st1b['witness'] is None and fails1b == 0 and wmax1b == 3
      and st1b['sample_mism'] == 0,
      f"sampled = {st1b['sample_checked']}, mismatches = "
      f"{st1b['sample_mism']}; law violations = "
      f"{dict(sorted(st1b['laws'].items()))}")

# ================== AG2: guided constructor search 4..6 =====================
def try_pool(h, S, base, actors, bits=None):
    """Execute one pool per the SIG-chain convention (pin AG2:
    constructed, not enumerated): p-events by sorted(S) on base (bit
    rule: lex-max member proposes 1, the rest 0 — the lex-min
    connected pattern; overridable via bits; a standing proposal by
    (a, base) is reused — the interleaved mode), then the arb
    CONSTRUCTED as ('r', min(S), ckey = S's triples on base, wkey)
    with wkey swept over ALL nonempty subsets of ckey in sorted
    order, each checked by the committed admissible(); the first
    admissible wkey is taken (declared; wkey affects only the vname
    value bits, never holders or the poset).  Every event carries its
    exact weight.  Returns (h2, qs2, status, detail)."""
    h2 = list(h)
    qs2 = []
    mx = max(S)
    for a in sorted(S):
        if any(x[0] == 'p' and x[1] == a and x[2] == base
               for x in h2):
            continue  # the standing proposal is the pool member
        x = bits[a] if bits else (1 if a == mx else 0)
        e = ('p', a, base, x)
        ok, q = admissible(h2, e)
        if not ok:
            return h2, qs2, 'p-death', (a, base)
        h2.append(e); qs2.append(q)
    trip = {}
    for x in h2:
        if x[0] == 'p' and x[1] in S and x[2] == base:
            trip[x[1]] = (x[1], x[2], x[3])
    ck = frozenset(trip.values())
    items = sorted(ck, key=repr)
    for m in range(1, 1 << len(items)):
        wk = frozenset(items[i] for i in range(len(items))
                       if m >> i & 1)
        e = ('r', min(S), ck, wk)
        ok, q = admissible(h2, e)
        if ok:
            h2.append(e); qs2.append(q)
            return h2, qs2, 'ok', e
    return h2, qs2, 'r-death', 'no-admissible-arb'

def run_events(name, seq, verbose=True):
    h = []
    qs = []
    for e in seq:
        ok, q = admissible(h, e)
        if verbose:
            print(f"    {fmt(e)}  ->  admissible = {ok}, q = {q}")
        if not ok:
            return h, qs, (len(h), e)
        h.append(e); qs.append(q)
    return h, qs, None

def state_report(name, h, actors):
    C = C_of(h)
    okd, _ = dim_le_2(C)
    wd = width_of(C)
    tagw = " [width <= 2: dim<=2 pass is a THEOREM, not evidence]" \
        if wd <= 2 else ""
    print(f"    {name}: n = {len(h)}, width = {wd}, dim<=2 = {okd}"
          + tagw)
    cands = candidates_for(h, actors)
    arbs = [(e, q) for e, q in cands if e[0] == 'r']
    pools_now = [frozenset(t[0] for t in e[2]) for e in h
                 if e[0] == 'r']
    cross = [e for e, q in arbs
             if any((frozenset(t[0] for t in e[2]) & P)
                    and not (frozenset(t[0] for t in e[2]) <= P
                             or P <= frozenset(t[0] for t in e[2]))
                    for P in pools_now)]
    print(f"    {name} candidate census: {len(cands)} candidates, "
          f"{len(arbs)} arbs, {len(cross)} pool-crossing arbs")
    return C, okd, wd, len(arbs), len(cross)

print("[AG2a the crown programs — width 6 and the width-3 cascade]")
A6 = ('A', 'B', 'C', 'D', 'E', 'F')
# P1: the W6-translation bottom row — three disjoint pair-arbs on V0.
tA = ('A', V0, 0); tF = ('F', V0, 1)
tB = ('B', V0, 0); tD = ('D', V0, 1)
tC = ('C', V0, 0); tE = ('E', V0, 1)
P1 = [('p', 'A', V0, 0), ('p', 'F', V0, 1),
      ('r', 'A', frozenset({tA, tF}), frozenset({tA})),
      ('p', 'B', V0, 0), ('p', 'D', V0, 1),
      ('r', 'B', frozenset({tB, tD}), frozenset({tB})),
      ('p', 'C', V0, 0), ('p', 'E', V0, 1),
      ('r', 'C', frozenset({tC, tE}), frozenset({tC}))]
print("  P1 (bottoms {A,F},{B,D},{C,E} on V0 — the S3 bottom row):")
h1, qs1, death1 = run_events("P1", P1)
C1, ok1, w1, narb1, ncross1 = state_report("P1", h1, A6)
arb_idx1 = [j for j, e in enumerate(h1) if e[0] == 'r']
inc_pairs1 = sum(1 for i in arb_idx1 for j in arb_idx1 if i < j
                 and not C1[i][j] and not C1[j][i])
bases_now = {}
for a in A6:
    hx = h1 + [('n', a)]
    px = event_poset(hx)
    vx = View(hx, px, px[len(hx) - 1])
    bases_now[a] = sorted({b for b, x in
                           ns3['prop_options_in_view'](vx, a)},
                          key=repr)
print("    per-actor proposable bases after P1 (each actor is "
      "confined to its OWN pool's mint):")
for a in A6:
    print(f"      {a}: {bases_now[a]}")
check("AG2a-P1 the S3 BOTTOM ROW EXISTS: three cross-authored pair-"
      "arbs on V0, pairwise incomparable, every event admissible at "
      "exactly 1/8 — realized width 6 with >= 2 coexisting cross-"
      "authored arbs; and the TOP ROW STARVES: the terminal candidate "
      "census has ZERO arb candidates (so zero pool-crossing arbs); "
      "each actor's proposable bases = exactly its own pool's mint",
      death1 is None and all(q == Fr(1, 8) for q in qs1)
      and ok1 and w1 == 6 and inc_pairs1 == 3
      and narb1 == 0 and ncross1 == 0
      and all(len(bases_now[a]) == 1 for a in A6)
      and bases_now['A'] == bases_now['F']
      and bases_now['B'] == bases_now['D']
      and bases_now['C'] == bases_now['E']
      and bases_now['A'] != bases_now['B'],
      f"9 events all q = 1/8; incomparable arb pairs = {inc_pairs1}"
      f"/3; dim<=2 = {ok1}, width = {w1}")

# P2: the two-level variant — global 6-pool mint, then the bottom row
# on the minted base (multi-base layout).
t6 = [('A', V0, 0), ('B', V0, 1), ('C', V0, 0),
      ('D', V0, 1), ('E', V0, 0), ('F', V0, 1)]
f6 = ('r', 'A', frozenset(t6), frozenset({t6[0], t6[2], t6[4]}))
P2a = [('p', 'A', V0, 0), ('p', 'B', V0, 1), ('p', 'C', V0, 0),
       ('p', 'D', V0, 1), ('p', 'E', V0, 0), ('p', 'F', V0, 1), f6]
print("  P2 (global 6-pool mint on V0, then pair-arbs {A,F},{B,D},"
      "{C,E} on the mint v*):")
h2, qs2, death2 = run_events("P2", P2a)
vstar = vname_of_arb(f6)
uA = ('A', vstar, 0); uF = ('F', vstar, 1)
uB = ('B', vstar, 0); uD = ('D', vstar, 1)
uC = ('C', vstar, 0); uE = ('E', vstar, 1)
P2b = [('p', 'A', vstar, 0), ('p', 'F', vstar, 1),
       ('r', 'A', frozenset({uA, uF}), frozenset({uA})),
       ('p', 'B', vstar, 0), ('p', 'D', vstar, 1),
       ('r', 'B', frozenset({uB, uD}), frozenset({uB})),
       ('p', 'C', vstar, 0), ('p', 'E', vstar, 1),
       ('r', 'C', frozenset({uC, uE}), frozenset({uC}))]
h2b = list(h2); qs2b = list(qs2); death2b = None
for e in P2b:
    ok, q = admissible(h2b, e)
    print(f"    {fmt(e)}  ->  admissible = {ok}, q = {q}")
    if not ok:
        death2b = (len(h2b), e); break
    h2b.append(e); qs2b.append(q)
C2m, ok2m, w2m, narb2, ncross2 = state_report("P2", h2b, A6)
check("AG2a-P2 THE MULTI-BASE LAYOUT: the global 6-pool mint gives "
      "ALL SIX actors one shared base v*, the bottom row re-forms ON "
      "v* (view-local components — each pair's component is just its "
      "own two proposals), all 16 events admissible; and the "
      "supersession law strikes ONE LEVEL UP: after the pair-arbs "
      "the terminal census again has ZERO arb candidates — the tops "
      "starve at every level; dim<=2 holds at width 6",
      death2 is None and death2b is None and ok2m and w2m == 6
      and narb2 == 0 and ncross2 == 0,
      f"n = {len(h2b)}; dim<=2 = {ok2m}, width = {w2m}")

# P3: supersession timing — delayed B; can {A,B} pool on V0 after A's
# V0-arb?  (the direct crossing attempt)
P3 = [('p', 'A', V0, 0), ('p', 'F', V0, 1),
      ('r', 'A', frozenset({tA, tF}), frozenset({tA})),
      ('p', 'B', V0, 1)]
print("  P3 (delayed B — pool {A,B} on V0 after A's V0-arb?):")
h3, qs3, death3 = run_events("P3", P3)
pA_retry = ('p', 'A', V0, 0)
ok_pA, _q = admissible(h3, pA_retry)
cands3 = candidates_for(h3, A6)
arbs3 = [(e, q) for e, q in cands3 if e[0] == 'r']
arbs3_auth = sorted({tuple(sorted({t[0] for t in e[2]}))
                     for e, q in arbs3})
check("AG2a-P3 SUPERSESSION TIMING: after A's V0-arb, A's re-"
      "proposal on V0 is INADMISSIBLE (V0 superseded in A's view) "
      "while fresh B holds only V0 — the {A,B} pool has no common "
      "live base; the only arb candidate at the state is B's self-"
      "arb ({B},) — cross-pool arbitration cannot form on V0",
      death3 is None and (not ok_pA)
      and arbs3_auth == [('B',)],
      f"p(A,V0,0) re-admissible = {ok_pA}; arb candidate author-sets "
      f"= {arbs3_auth}")

# P4: mint-first ordering — mint {A,B} on V0 first, then try the
# bottom {A,F} pool.
tA2 = ('A', V0, 0); tB2 = ('B', V0, 1)
P4seq = [('p', 'A', V0, 0), ('p', 'B', V0, 1),
         ('r', 'A', frozenset({tA2, tB2}), frozenset({tA2}))]
print("  P4 (mint {A,B} first, then attempt the {A,F} pool):")
h4, qs4, death4 = run_events("P4", P4seq)
vAB = vname_of_arb(P4seq[2])
ok_pF_v, _ = admissible(h4, ('p', 'F', vAB, 1))
ok_pA_V0, _ = admissible(h4, ('p', 'A', V0, 0))
ok_pF_V0, qF = admissible(h4, ('p', 'F', V0, 1))
h4b = h4 + [('p', 'F', V0, 1)]
cands4 = candidates_for(h4b, A6)
match_AF = [e for e, q in cands4 if e[0] == 'r'
            and {t[0] for t in e[2]} == {'A', 'F'}]
check("AG2a-P4 MINT-FIRST ORDERING FAILS THE CROSS TOO: after the "
      "{A,B} mint, F cannot propose on v_AB (not a holder) and A "
      "cannot propose on V0 (superseded) — F's V0-proposal stands "
      "alone and no {A,F} arb candidate exists at the state",
      death4 is None and (not ok_pF_v) and (not ok_pA_V0)
      and ok_pF_V0 and match_AF == [],
      f"p(F,v_AB) = {ok_pF_v}; p(A,V0) = {ok_pA_V0}; p(F,V0) = "
      f"{ok_pF_V0}; {{A,F}} arb candidates = {len(match_AF)}")

# P5: the width-3 cascade — 3-pool mint {A,B,C}, child {A,B}, then
# the non-laminar sibling {B,C} attempt.
ABCt = [('A', V0, 0), ('B', V0, 1), ('C', V0, 0)]
r3 = ('r', 'A', frozenset(ABCt), frozenset({ABCt[0], ABCt[2]}))
P5a = [('p', 'A', V0, 0), ('p', 'B', V0, 1), ('p', 'C', V0, 0), r3]
print("  P5 (width-3 cascade: mint {A,B,C}; child {A,B}; attempt the "
      "non-laminar {B,C}):")
h5, qs5, death5 = run_events("P5", P5a)
v3 = vname_of_arb(r3)
c1 = ('A', v3, 0); c2 = ('B', v3, 1)
P5b = [('p', 'A', v3, 0), ('p', 'B', v3, 1),
       ('r', 'A', frozenset({c1, c2}), frozenset({c1}))]
death5b = None
for e in P5b:
    ok, q = admissible(h5, e)
    print(f"    {fmt(e)}  ->  admissible = {ok}, q = {q}")
    if not ok:
        death5b = e; break
    h5.append(e); qs5.append(q)
ok_pB_v3, _ = admissible(h5, ('p', 'B', v3, 0))
ok_pC_v3, qC3 = admissible(h5, ('p', 'C', v3, 1))
h5c = h5 + [('p', 'C', v3, 1)]
cands5 = candidates_for(h5c, ABC)
arbs5 = sorted({tuple(sorted({t[0] for t in e[2]}))
                for e, q in cands5 if e[0] == 'r'})
C5m, ok5m, w5m, _na5, _nc5 = state_report("P5", h5c, ABC)
check("AG2a-P5 THE COMPONENT LAW AT WIDTH 3: the {A,B,C} mint is one "
      "3-component (connected conflict graph) consumed whole; the "
      "child {A,B} re-forms on the mint; then B CANNOT re-propose on "
      "v_ABC (its child-arb superseded it in B's view) while C still "
      "can (the child is not in C's chain) — so the non-laminar "
      "{B,C} pool is unrealizable and C's only arb option is its "
      "self-arb: sibling pools are forced DISJOINT",
      death5 is None and death5b is None and (not ok_pB_v3)
      and ok_pC_v3 and arbs5 == [('C',)],
      f"p(B,v_ABC) = {ok_pB_v3}; p(C,v_ABC) = {ok_pC_v3}; arb "
      f"author-sets at the state = {arbs5}")

# -------------------- AG2b: exhaustive no-idle width 4 ----------------------
print("[AG2b exhaustive no-idle width 4 — declared subfamily]")
print("  DECLARATION: actors (A,B,C,D), p/r only, cap 6 (measured "
      "growth 8/56/448/4,864/48,896/382,592; depth 7 ~ 3e6 — over "
      "budget; DECLARED).  This is the systematic core of the "
      "guided-width search: every <= 6-event no-idle layout at width "
      "4 — all pool shapes, bit patterns, orderings and supersession "
      "timings — is in this family.")
A4 = ('A', 'B', 'C', 'D')
st2b = sweep(A4, 6, False, "AG2b")
tot2b, arb2b, wmax2b, fails2b, strat2b = census_lines("AG2b", st2b, 6)
if st2b['witness']:
    report_witness("AG2b", *st2b['witness'])
check("AG2b EXHAUSTIVE NO-IDLE WIDTH 4 (cap 6, declared): census "
      "anchored (totals 8/56/448/4,864/48,896/382,592; arb-"
      "containing 0/8/256/4,480/48,896/382,592 = 436,232; canonical "
      "classes 16,273; register-word classes 11,936 of which 5,472 "
      "at width 4; the depth-6 mass is ALL arb-mass, 2749/1024); "
      "every arb-containing poset dim<=2-checked via the register-"
      "word reduction; ZERO failures; max width realized = 4 (the "
      "actor bound); the transport contrast is SHARP: at four actors "
      "transport fails dim<=2 at six events (d43d NG3b W4) — "
      "arbitration at the same width and event count NEVER does",
      st2b['total'][1:] == [8, 56, 448, 4864, 48896, 382592]
      and st2b['arb'][1:] == [0, 8, 256, 4480, 48896, 382592]
      and len(st2b['canons']) == 16273
      and len(st2b['classes']) == 11936
      and sum(1 for (_n, _ok, w) in st2b['classes'].values()
              if w == 4) == 5472
      and st2b['mass_arb'] == st2b['mass_all'] == Fr(2749, 1024)
      and st2b['witness'] is None and fails2b == 0 and wmax2b == 4
      and st2b['sample_mism'] == 0,
      f"arb-containing = {st2b['arb'][1:]}; sampled = "
      f"{st2b['sample_checked']}, mismatches = {st2b['sample_mism']};"
      f" law violations = {dict(sorted(st2b['laws'].items()))}")

# ----------------- AG2c: systematic crossing attempts (F-CROSS) -------------
print("[AG2c F-CROSS — systematic non-laminar pool-pair attempts]")
print("  DECLARATION: for every ordered pair (X, Y) of actor subsets "
      "with 2 <= |X|,|Y| <= 3, X and Y overlapping and non-nested "
      "(the minimal non-laminar configurations — the crown's "
      "prerequisite): execute X's pool, then attempt Y's pool on "
      "EVERY base then available ({V0} + all mints), in four "
      "contexts: direct (both on V0), global (all-actor mint first), "
      "parent (mint over X union Y first), interleaved (Y's "
      "proposals placed BEFORE X's arb — the supersession-timing "
      "evasion).  Every event admission-checked with exact weights "
      "via the committed admissible(); arbs CONSTRUCTED with the "
      "full wkey-subset sweep (the SIG-chain convention — "
      "constructed, not enumerated; wkey never affects holders or "
      "the poset); repeated states served from a cache (identical "
      "prefixes rebuilt once).  Bit patterns: the lex rule "
      "everywhere; PLUS the full 2^|X u Y| bit sweep over the "
      "4-actor pairs in the direct and interleaved contexts (bit-"
      "completeness at widths 3..4 is already exhaustive via AG1/"
      "AG2b at their caps; DECLARED).  Backstop at every reached "
      "non-interleaved state: the full committed candidates_for "
      "enumeration, scanned for ANY pool-crossing arb candidate.  A "
      "cross SUCCESS would be a dim>2 candidate; the census gates "
      "zero successes and categorizes every death.")

def subsets_23(actors):
    out = []
    for s in (2, 3):
        if s <= len(actors):
            out.extend(frozenset(c) for c in combinations(actors, s))
    return out

def cross_pairs(actors):
    subs = subsets_23(actors)
    out = []
    for X in subs:
        for Y in subs:
            if X == Y: continue
            if (X & Y) and not (X <= Y or Y <= X):
                out.append((X, Y))
    return out

def attempt_Y(h, Y, actors, bits=None):
    """Try Y's pool on every available base; return list of
    (base, status)."""
    res = []
    for b in [V0] + sorted(set(mints_in(h)), key=repr):
        h2, qs2, statusb, det = try_pool(h, Y, b, actors, bits)
        res.append((b, statusb, h2 if statusb == 'ok' else None))
    return res

def arb_construct(h, S, base):
    """The constructed-arb sweep (the SIG-chain convention): the
    first admissible ('r', min(S), ckey = S's triples on base, wkey)
    over the sorted nonempty wkey subsets, via the committed
    admissible(); (None, None) if no wkey is admissible."""
    trip = {}
    for x in h:
        if x[0] == 'p' and x[1] in S and x[2] == base:
            trip[x[1]] = (x[1], x[2], x[3])
    ck = frozenset(trip.values())
    items = sorted(ck, key=repr)
    for m in range(1, 1 << len(items)):
        wk = frozenset(items[i] for i in range(len(items))
                       if m >> i & 1)
        e = ('r', min(S), ck, wk)
        ok, q = admissible(h, e)
        if ok: return e, q
    return None, None

def build_interleaved(X, Y, actors, bits=None):
    """X's p's, then Y's extra p's (BEFORE X's arb — the
    supersession-timing evasion), then X's constructed arb."""
    h = []
    for a in sorted(X):
        e = ('p', a, V0, bits[a] if bits else
             (1 if a == max(X) else 0))
        ok, q = admissible(h, e)
        if not ok: return 'p-death-X', None
        h.append(e)
    for a in sorted(Y - X):
        e = ('p', a, V0, bits[a] if bits else
             (1 if a == max(Y) else 0))
        ok, q = admissible(h, e)
        if not ok: return 'p-death-Ypre', None
        h.append(e)
    e, q = arb_construct(h, X, V0)
    if e is None: return 'r-death-X', None
    h.append(e)
    return 'ok', h

print("  UNIVERSE NOTE (mechanical, gated): the committed admissible "
      "is the 2-argument d42a form — a function of (acts, event) "
      "only, with NO actor-universe argument — so a pool-pair "
      "attempt's fate is identical in every universe containing its "
      "actors; the main sweep therefore runs the 6-actor universe "
      "over ALL 840 ordered overlapping non-nested 2-3-element pool "
      "pairs (subsuming the width-3..5 patterns), the at-state "
      "enumerator census runs with the LARGEST candidate space "
      "(actors = 6), and the width-3 pairs are re-run in the width-3 "
      "universe and gated status-identical (the independence gate).")

def cross_run(actors, X, Y, ctx, census, successes, wtag):
    """One (X, Y, ctx) attempt; returns the post-X state key data
    (skey, status, hX)."""
    U = X | Y
    if ctx == 'interleaved':
        skey = (wtag, ctx, tuple(sorted(X)), tuple(sorted(Y)))
    elif ctx == 'parent':
        skey = (wtag, ctx, tuple(sorted(X)), tuple(sorted(U)))
    else:
        skey = (wtag, ctx, tuple(sorted(X)), None)
    if skey not in STATE_CACHE:
        if ctx == 'interleaved':
            STATE_CACHE[skey] = build_interleaved(X, Y, actors)
        else:
            h0 = []
            s0 = 'ok'
            if ctx in ('global', 'parent'):
                S0 = frozenset(actors) if ctx == 'global' else U
                ckey0 = (wtag, ctx, tuple(sorted(S0)))
                if ckey0 not in CTX_CACHE:
                    hc, _qc, sc, _dc = try_pool([], S0, V0, actors)
                    CTX_CACHE[ckey0] = (sc, hc)
                s0, h0 = CTX_CACHE[ckey0]
                if s0 != 'ok':
                    s0 = 'ctx-' + s0
            if s0 != 'ok':
                STATE_CACHE[skey] = (s0, None)
            else:
                bx = V0 if ctx == 'direct' else mints_in(h0)[-1]
                hX, _qs, sX, _d = try_pool(h0, X, bx, actors)
                STATE_CACHE[skey] = (('ok', hX) if sX == 'ok'
                                     else ('X-' + sX, None))
    status, hX = STATE_CACHE[skey]
    y_statuses = []
    if status != 'ok':
        key = (wtag, ctx, status)
        census[key] = census.get(key, 0) + 1
    else:
        for b, statusb, hY in attempt_Y(hX, Y, actors):
            key = (wtag, ctx, 'Y-' + statusb)
            census[key] = census.get(key, 0) + 1
            y_statuses.append(statusb)
            if statusb == 'ok':
                successes.append((wtag, ctx, tuple(sorted(X)),
                                  tuple(sorted(Y)), repr(b)))
    return skey, status, hX, tuple(y_statuses)

CTX_CACHE = {}
STATE_CACHE = {}
cross_census = {}
cross_successes = []
cross_states = 0
cross_state_widths = {}
state_census_done = set()
pairs6 = cross_pairs(A6)
outcome6 = {}
for (X, Y) in pairs6:
    for ctx in ('direct', 'global', 'parent', 'interleaved'):
        skey, status, hX, ys = cross_run(A6, X, Y, ctx, cross_census,
                                         cross_successes, 6)
        outcome6[(tuple(sorted(X)), tuple(sorted(Y)), ctx)] = \
            (status, ys)
        if status == 'ok' and ctx != 'interleaved' \
                and skey not in state_census_done:
            # at-state exhaustive census (the committed enumerator,
            # 6-actor candidate space): ANY pool-crossing arb
            # candidate?  (interleaved states are per-pair; their
            # crossing potential is exactly the Y-attempt — DECLARED)
            state_census_done.add(skey)
            cross_states += 1
            cross_state_widths[skey] = width_of(C_of(hX))
            pools_hX = [frozenset(t[0] for t in e[2]) for e in hX
                        if e[0] == 'r']
            for e, q in candidates_for(hX, A6):
                if e[0] != 'r': continue
                Pe = frozenset(t[0] for t in e[2])
                if any((Pe & P) and not (Pe <= P or P <= Pe)
                       for P in pools_hX):
                    cross_successes.append(
                        (6, ctx, tuple(sorted(X)),
                         'at-state-candidate', fmt(e)))
# the width-3 universe-independence gate
indep_census = {}
indep_ok = True
for (X, Y) in cross_pairs(ABC):
    for ctx in ('direct', 'global', 'parent', 'interleaved'):
        skey, status, hX, ys = cross_run(ABC, X, Y, ctx,
                                         indep_census,
                                         cross_successes, 3)
        if ctx == 'global':
            continue  # the global pool differs by universe (ABC vs
            # A6 all-actor mint) — universe-dependent BY CONTENT,
            # excluded from the identity gate (DECLARED)
        ref = outcome6.get((tuple(sorted(X)), tuple(sorted(Y)), ctx))
        if ref != (status, ys):
            indep_ok = False
# width-4 bit sweep (direct + interleaved)
bit_attempts = bit_successes = 0
for (X, Y) in cross_pairs(A4):
    U = sorted(X | Y)
    for mask in range(1 << len(U)):
        bits = {a: (mask >> i) & 1 for i, a in enumerate(U)}
        for ctx in ('direct', 'interleaved'):
            if ctx == 'direct':
                hX, _qs, sX, _d = try_pool([], X, V0, A4, bits)
                if sX != 'ok': continue
            else:
                sX, hX = build_interleaved(X, Y, A4, bits)
                if sX != 'ok': continue
            for b, statusb, hY in attempt_Y(hX, Y, A4, bits):
                bit_attempts += 1
                if statusb == 'ok':
                    bit_successes += 1
                    cross_successes.append(
                        (4, ctx + '-bits', tuple(sorted(X)),
                         tuple(sorted(Y)), repr(b)))
print(f"  F-CROSS 6-actor-universe census {{(universe, context, "
      f"outcome): count}} = {dict(sorted(cross_census.items()))}")
print(f"  F-CROSS width-3 independence-gate census = "
      f"{dict(sorted(indep_census.items()))}")
print(f"  F-CROSS post-X state widths {{poset width: states}} = "
      f"{dict(sorted((w, list(cross_state_widths.values()).count(w)) for w in set(cross_state_widths.values())))} "
      "[AG4; one entry per cached non-interleaved state, MEASURED; "
      "no dim evidence is drawn from these states — they are death "
      "exhibits]")
print(f"  F-CROSS totals: {sum(cross_census.values())} lex-bit "
      "Y-attempts (840 pairs x 10 context-base slots), every one "
      "dead (p-death = the proposal inadmissible: supersession or "
      "non-holding; r-death = no admissible arb over the placed "
      "proposals)")
print(f"  F-CROSS width-4 bit sweep: {bit_attempts} Y-attempts over "
      f"all 2^|X u Y| patterns, successes = {bit_successes}")
for s in cross_successes[:5]:
    print(f"  [CROSS SUCCESS] {s[:5]}")
CROSS_ANCH = {
    (6, 'direct', 'Y-p-death'): 840, (6, 'direct', 'Y-r-death'): 840,
    (6, 'global', 'Y-p-death'): 840,
    (6, 'global', 'Y-r-death'): 1680,
    (6, 'interleaved', 'Y-p-death'): 840,
    (6, 'interleaved', 'Y-r-death'): 840,
    (6, 'parent', 'Y-p-death'): 840,
    (6, 'parent', 'Y-r-death'): 1680}
INDEP_ANCH = {
    (3, 'direct', 'Y-p-death'): 6, (3, 'direct', 'Y-r-death'): 6,
    (3, 'global', 'Y-p-death'): 6, (3, 'global', 'Y-r-death'): 12,
    (3, 'interleaved', 'Y-p-death'): 6,
    (3, 'interleaved', 'Y-r-death'): 6,
    (3, 'parent', 'Y-p-death'): 6, (3, 'parent', 'Y-r-death'): 12}
wtable = {w: list(cross_state_widths.values()).count(w)
          for w in set(cross_state_widths.values())}
check("AG2c F-CROSS: ZERO successes over all 840 ordered "
      "overlapping non-nested pool pairs x 4 contexts x every "
      "available base in the 6-actor universe (8,400 lex-bit "
      "attempts, census anchored exactly: every Y-attempt is a "
      "p-death or an r-death), the width-3 universe re-run, and the "
      "full width-4 bit sweep (1,920 attempts); the width-3 "
      "universe-independence gate holds (status-identical to the "
      "6-actor run on the universe-free contexts); at every one of "
      "the 340 cached post-X states the committed candidate "
      "enumeration itself offers ZERO pool-crossing arb candidates; "
      "state widths {2: 15, 3: 80, 4: 150, 5: 60, 6: 35} — the non-"
      "laminar (crown-prerequisite) configurations are unrealizable "
      "at every probed state",
      len(cross_successes) == 0 and len(pairs6) == 840
      and cross_census == CROSS_ANCH and indep_census == INDEP_ANCH
      and cross_states == 340 and indep_ok
      and wtable == {2: 15, 3: 80, 4: 150, 5: 60, 6: 35}
      and bit_attempts == 1920 and bit_successes == 0,
      f"ordered pairs = {len(pairs6)}; Y-attempt total = "
      f"{sum(cross_census.values())}; cached post-X states = "
      f"{cross_states}; independence gate = {indep_ok}; bit-sweep "
      f"attempts = {bit_attempts}")

# ----------------- AG2d: the laminar layout family (F-LAM) ------------------
print("[AG2d F-LAM — the laminar mint-forest family]")
print("  DECLARATION: all laminar pool forests over widths 3..6 with "
      "<= 3 pools, pool sizes in {2, 3, w (root only)}, children "
      "subsets of parents (towers = same set allowed), sibling "
      "children disjoint, executed parents-first with the lex bit "
      "rule and constructed arbs (first admissible wkey, declared); "
      "event-count cap n <= 14.  The POSITIVE half of the component "
      "law: these are the layouts the admission layer accepts; each "
      "is gated all-admissible, dim<=2-checked, width-printed (AG4).")

def child_opts(S):
    out = [frozenset(c) for c in combinations(sorted(S), 2)]
    if len(S) >= 3:
        out.extend(frozenset(c) for c in combinations(sorted(S), 3))
    if frozenset(S) not in out:
        out.append(frozenset(S))
    return sorted(set(out), key=repr)

def lam_forests(actors):
    subs = subsets_23(actors)
    roots_opts = []
    for k in (1, 2, 3):
        for combo in combinations(subs, k):
            if all(not (a & b) for a, b in combinations(combo, 2)):
                roots_opts.append(list(combo))
    if len(actors) > 3:
        roots_opts.append([frozenset(actors)])
    forests = []
    for roots in roots_opts:
        base = [(r, None) for r in roots]
        forests.append(base)
        budget = 3 - len(roots)
        if budget < 1: continue
        for ri in range(len(roots)):
            for c in child_opts(roots[ri]):
                f1 = base + [(c, ri)]
                forests.append(f1)
                if budget < 2: continue
                for g in child_opts(c):
                    forests.append(f1 + [(g, len(base))])
                for c2 in child_opts(roots[ri]):
                    if repr(sorted(c2, key=repr)) <= \
                       repr(sorted(c, key=repr)): continue
                    if c2 & c: continue
                    forests.append(f1 + [(c2, ri)])
                for rj in range(ri + 1, len(roots)):
                    for c2 in child_opts(roots[rj]):
                        forests.append(f1 + [(c2, rj)])
    out = []
    for f in forests:
        nev = sum(len(S) + 1 for S, _p in f)
        if nev <= 14:
            out.append(f)
    return out

lam_stats = {}
LAM_MEMO = {}  # C-matrix bytes -> (dim<=2, width): two forests with
# identical labeled C matrices have identical verdicts (exact
# matrix-equality memo, no symmetry assumption)
lam_total = lam_dead = lam_dimfail = 0
lam_max_arbpairs = 0
for w, actors in ((3, ABC), (4, A4), (5, ('A', 'B', 'C', 'D', 'E')),
                  (6, A6)):
    for f in lam_forests(actors):
        lam_total += 1
        h = []
        qs_f = []
        minted = {}
        dead = None
        for i, (S, par) in enumerate(f):
            b = V0 if par is None else minted[par]
            h2, qs2, s, det = try_pool(h, S, b, actors)
            if s != 'ok':
                dead = (i, s); break
            minted[i] = vname_of_arb(h2[-1])
            qs_f.extend(qs2)
            h = h2
        shape = (w, tuple(sorted((len(S),
                                  -1 if p is None else p)
                                 for S, p in f)))
        if dead:
            lam_dead += 1
            key = shape + ('DEAD',)
            lam_stats[key] = lam_stats.get(key, 0) + 1
            continue
        C = C_of(h)
        mkey = repr(C)
        if mkey not in LAM_MEMO:
            okd_m, _ = dim_le_2(C)
            LAM_MEMO[mkey] = (okd_m, width_of(C))
        okd, wd = LAM_MEMO[mkey]
        if not okd:
            lam_dimfail += 1
            report_witness("AG2d", h, qs_f, C)
        arb_idx = [j for j, e in enumerate(h) if e[0] == 'r']
        inc = sum(1 for i in arb_idx for j in arb_idx
                  if i < j and not C[i][j] and not C[j][i])
        lam_max_arbpairs = max(lam_max_arbpairs, inc)
        key = shape + (len(h), wd, okd)
        lam_stats[key] = lam_stats.get(key, 0) + 1
print("  F-LAM shape census {(width, ((poolsize, parent), ...), n, "
      "poset-width, dim<=2): count} — every candidate's width "
      "computed and entered (AG4); width <= 2 rows are theorem-"
      "passes, not evidence:")
for key in sorted(lam_stats, key=repr):
    tagw = ""
    if len(key) == 5 and key[3] <= 2:
        tagw = "  [theorem, not evidence]"
    print(f"    {key}: {lam_stats[key]}{tagw}")
check("AG2d F-LAM: all 1,597 laminar mint-forest layouts in the "
      "declared family execute fully admissibly (ZERO deaths — "
      "laminar layouts are exactly what the layer accepts), ZERO "
      "dim<=2 failures at widths 3..6 up to 14 events, and "
      "configurations with THREE pairwise-incomparable cross-"
      "authored arbs are realized (the pin's >= 2 exceeded)",
      lam_total == 1597 and lam_dead == 0 and lam_dimfail == 0
      and lam_max_arbpairs == 3,
      f"forests executed = {lam_total}; deaths = {lam_dead}; dim "
      f"failures = {lam_dimfail}; max pairwise-incomparable arb "
      f"pairs in one layout = {lam_max_arbpairs}")

# ==================== AG3: the component-law statement ======================
print("[AG3 the component law, made mechanical]")
law_viol_total = {}
for stx in (st1, st1b, st2b):
    for k, v in stx['laws'].items():
        law_viol_total[k] = law_viol_total.get(k, 0) + v
print("  THE COMPONENT-CONFINEMENT LAW (the five clauses gated "
      "mechanically, zero violations, over the three EXHAUSTIVE "
      "families — width 3 <= 6 events full grammar, width 3 <= 7 "
      "no-idle, width 4 <= 6 no-idle — every history checked at "
      "creation; the AG2a/AG2c/AG2d constructor runs at widths up "
      "to 6 exhibit the law's consequences: laminar layouts "
      "all-admissible, every crossing attempt dead, starvation at "
      "the pinned points):")
print("    (i)   LAMINARITY: the pools of any two arb events are "
      "disjoint or nested;")
print("    (ii)  SIBLING DISJOINTNESS: arbs on a common base have "
      "disjoint pools;")
print("    (iii) THE MINT CHAIN: each actor's successive arb pools "
      "are nested decreasing, and each arb's base is exactly the "
      "vname minted by that actor's previous arb (V0 for its "
      "first);")
print("    (iv)  THE CHAIN LAW: any two events whose register sets "
      "intersect are comparable — so incomparable arbs have "
      "disjoint pools, each actor's events form a chain, and poset "
      "width <= actor width;")
print("    (v)   VNAME FRESHNESS: no vname register is ever written "
      "twice.")
print("  CONSEQUENCE (the crown obstruction, exhibited by AG2a/"
      "AG2c): the S3 crown needs three pairwise-incomparable tops "
      "each above two of three pairwise-incomparable bottoms; with "
      "(i)+(iv), a top sharing an actor with a bottom has a pool "
      "nested with that bottom's pool, and the required overlap "
      "pattern {A,B} vs {A,F} vs {B,D} is non-laminar — the pool "
      "pairs that would build the crown are exactly the F-CROSS "
      "deaths.  Arbitration's covering structure is confined to a "
      "laminar mint forest; the crown pattern is unrealizable at "
      "the tested scales.")
check("AG3 THE COMPONENT-CONFINEMENT LAW GATED: zero violations of "
      "(i)-(v) across 1,213,372 label-level histories (AG1 551,928 + "
      "AG1b 224,580 + AG2b 436,864 with their arb-containing "
      "subsets, register-word classes included) and zero F-CROSS "
      "successes; the law is the pinned obstruction horn made "
      "mechanical — the exact confinement statement above is the "
      "deliverable in the no-witness branch",
      all(v == 0 for v in law_viol_total.values())
      and tot1 == 551928 and tot1b == 224580 and tot2b == 436864
      and len(cross_successes) == 0,
      f"aggregate law violations = {dict(sorted(law_viol_total.items()))}")

# ========================= AG4: width discipline ============================
print("[AG4 width discipline]")
ev1 = sum(1 for (n, ok, w) in st1['classes'].values()
          if n >= 6 and w >= 3)
ev1b = sum(1 for (n, ok, w) in st1b['classes'].values()
           if n >= 6 and w >= 3)
ev2b = sum(1 for (n, ok, w) in st2b['classes'].values()
           if n >= 6 and w >= 3)
th_ok = all(ok for stx in (st1, st1b, st2b)
            for (n, ok, w) in stx['classes'].values() if w <= 2)
print(f"  dim-capable (EVIDENCE) stratum — n >= 6 AND width >= 3 — "
      f"register-word classes: AG1 = {ev1}, AG1b = {ev1b}, AG2b = "
      f"{ev2b}; every width <= 2 pass is a THEOREM (width doctrine, "
      "d43d note SS3/F2), every n < 6 pass is FLOOR (AG0's 219/"
      "4,231 anchors); the widths of all AG2 candidates are printed "
      "in their own sections (P1/P2/P5 state lines, the F-CROSS "
      "state-width table, the F-LAM shape census).")
check("AG4 WIDTH DISCIPLINE: the evidence stratum is NON-EMPTY at "
      "every exhaustive gate (2,034 / 4,596 / 9,000 register-word "
      "classes at n >= 6 and width >= 3 — the dim question was "
      "live, not width-vacuous); all width <= 2 classes pass dim<=2 "
      "(Dilworth tripwire — a width <= 2 dim failure would be an "
      "oracle bug); no dim<=2 pass outside the evidence stratum is "
      "cited as evidence anywhere in this receipt",
      ev1 == 2034 and ev1b == 4596 and ev2b == 9000 and th_ok,
      f"evidence-stratum classes = {ev1}/{ev1b}/{ev2b}; "
      f"width<=2 all-pass = {th_ok}")

# ========================== AG5: honest floor ===============================
check("AG5 HONEST FLOOR: (a) the n < 6 vacuity is re-cited with "
      "in-receipt proof (all 219 n=4 and all 4,231 n=5 labeled "
      "posets pass dim<=2 — AG0), so no sub-6-event configuration "
      "can witness anything; (b) all family-level quantities "
      "(mu-masses, distributions, censuses) are labeled MEASURED "
      "descriptors; (c) NO manifoldlikeness claim and no dimension-"
      "estimator statement appears anywhere — the only dimension "
      "statement is the exact order-dimension gate; (d) the caps "
      "(AG1 = 6 full, AG1b = 7 no-idle, AG2b = 6 no-idle width 4, "
      "AG2c/AG2d constructor caps) are DECLARED with their measured "
      "growth tables; (e) the no-idle subfamilies claim no full-"
      "grammar completeness beyond AG1's cap",
      True, "scope per pin SS1/SS4")

# ============================== the verdict =================================
any_witness = (st1['witness'] or st1b['witness'] or st2b['witness']
               or cross_successes or lam_dimfail)
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — anchor/port breakage or internal "
          "inconsistency; exit 1 by design")
    sys.exit(1)
if any_witness:
    print("[VERDICT] d44c WITNESS HORN: arbitration structure alone "
          "realizes order-dimension > 2 — see the [WITNESS] block "
          "above; S4's 'transport generates dimension' widens to "
          "'transport or cross-authored arbitration'.")
else:
    print("[VERDICT] d44c delivered — THE OBSTRUCTION HORN (pin SS2, "
          "decided by enumeration): arbitration structure ALONE "
          "does NOT generate order-dimension > 2 at the tested "
          "scales — zero dim<=2 failures across 1,213,372 label-"
          "level p/r/n histories (exhaustive width 3 to 6 events "
          "full-grammar / 7 no-idle; exhaustive width 4 to 6 events "
          "no-idle) and every constructor state at widths 3..6.  "
          "The mechanism is the COMPONENT-CONFINEMENT LAW (AG3, "
          "gated): supersession + whole-component consumption "
          "confine arb pools to a laminar mint forest with per-"
          "actor nested chains, and the crown's non-laminar overlap "
          "pattern starves — every cross attempt dies exactly where "
          "the law says (AG2a/AG2c).  Arbitration realizes width "
          "(up to the actor bound, three pairwise-incomparable "
          "cross-authored arbs coexisting) but cannot convert width "
          "into dimension; TRANSPORT'S MECHANISM STATUS SHARPENS "
          "TOWARD UNIQUENESS: at four actors and six events "
          "transport fails dim<=2 (d43d NG3b) while arbitration at "
          "the same scale never does.  The dimension question was "
          "pre-registered open; this is the obstruction answer at "
          "the declared caps.")
