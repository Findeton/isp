#!/usr/bin/env python3
"""
d43b_state_chain_exact.py — v10 D43b (N2): residue 1 via the
intrinsic state chain. Pin: note-d43b + its §5 round-1 amendments.
EXACT Fractions throughout; the d42a layer exec'd from the committed
d42b3 receipt (__file__-anchored — round-1 F-B8 repair).

ROUND-1 REBUILT REVISION (reviews/d43bc-round1-hostile-review.md,
R-B1..R-B4, adopted at LOG #339). The first build substituted the
boundary-marked truncation quotient for the pinned intrinsic map and
delivered its horizon growth (17/23/29) as the Martin datum; that
computation is retained below as the gated NEGATIVE CONTROL (the
horizon-stratification exhibit). The delivered object is now the
referee's UNIFORM-LOOKAHEAD INTRINSIC partition: P_0 = menu shape;
P_{t+1} = one probabilistic-bisimulation refinement; NO boundary
marker — a history's P_t class depends only on its t-step subtree,
horizon-uniform. It stabilizes at SIX states at lookahead t = 2 on
every window computable from the depth-6 cache (referee depth-7 run:
still six), the exact 6 x 6 transfer is well-defined, and MG3-MG5
execute exactly: lambda = 2, unique dominant class {2,4,5},
f = (4,4,3,7,3,3)/3 unique up to scale, root = renewal state,
mass-transport exact. Every gate below is mechanical (round-1 F-B3
repaired: no check(True) anywhere; every delivered count is an
anchored expectation that can fail). Exit 1 on breakage.
"""
import os
import sys
from fractions import Fraction as Fr

sys.setrecursionlimit(400000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

_here = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(_here, 'd42b3_placement_exact.py')).read()
ns = {}
exec(_src[:_src.index('print("[d42b3')], ns)
V0 = ns['V0']
candidates_for = ns['candidates_for']
canon = ns['canon']
vname = ns['vname']
View = ns['View']
event_poset = ns['event_poset']
AB = ('A', 'B')

print("[d43b — residue 1 via the intrinsic state chain (round-1 "
      "rebuilt)]")
print("  banner: EXACT; d42a layer from the committed d42b3 receipt")
print("  (__file__-anchored); ONE depth-6 enumeration; the delivered")
print("  object = the uniform-lookahead INTRINSIC partition (round-1")
print("  R-B1); the boundary-marked truncation runs retained as the")
print("  gated NEGATIVE CONTROL (horizon stratification); all gates")
print("  mechanical (R-B3); scope: closure on the computed window,")
print("  the renewal-pumping closure theorem = the named successor")
print("  (note §5 A3); no infinite-volume claim beyond it (pin §4).")

# ---- one enumeration (R-B4: the depth-6 family contains 4/5) -------
FAM = [[]]
CACHE = {}
frontier = [[]]
while frontier:
    h = frontier.pop()
    CACHE[tuple(h)] = candidates_for(h, AB)
    if len(h) >= 6: continue
    for e, q in CACHE[tuple(h)]:
        FAM.append(h + [e]); frontier.append(h + [e])
cum = [sum(1 for h in FAM if len(h) <= k) for k in range(7)]
check("MG0 the enumeration anchor: cumulative family sizes at depths "
      "0-6 equal the referee-verified census",
      cum == [1, 7, 39, 215, 1191, 6471, 34375],
      f"sizes = {cum}")

def menu_shape(cands):
    d = {}
    for e, q in cands:
        d[(e[0], q)] = d.get((e[0], q), 0) + 1
    return tuple(sorted(d.items(), key=repr))

# =============== SECTION A — the intrinsic object ===================
def relabel(d):
    relab = {}
    for k in sorted(d, key=repr):
        relab.setdefault(d[k], len(relab))
    return {k: relab[d[k]] for k in d}

P = {0: relabel({tuple(h): menu_shape(CACHE[tuple(h)]) for h in FAM})}
for t in range(5):
    nxt = {}
    for h in FAM:
        if len(h) > 5 - t: continue
        k = tuple(h)
        succ = tuple(sorted((str(q), P[t][tuple(h + [e])])
                            for e, q in CACHE[k]))
        nxt[k] = (P[t][k], succ)
    P[t + 1] = relabel(nxt)

tables = {c: [len({P[t][tuple(h)] for h in FAM if len(h) <= c})
              for t in range(0, 7 - c)] for c in (2, 3, 4)}
print(f"  intrinsic |P_t| tables: cutoff-2 {tables[2]}, cutoff-3 "
      f"{tables[3]}, cutoff-4 {tables[4]}")
check("MG2a the INTRINSIC partition stabilizes at SIX states at "
      "lookahead t = 2: the |P_t| tables on the len<=2/3/4 windows "
      "equal the referee anchors — the depth-4/5/6 family agreement "
      "(referee depth-7 run: P_3 == P_2 on len<=4, still six — "
      "cited, not rerun here)",
      tables == {2: [4, 4, 5, 5, 5], 3: [4, 5, 6, 6], 4: [4, 5, 6]},
      "anchors [4,4,5,5,5] / [4,5,6,6] / [4,5,6]")

def part_of(Pm, hs):
    b = {}
    for h in hs:
        b.setdefault(Pm[tuple(h)], set()).add(tuple(h))
    return frozenset(frozenset(v) for v in b.values())
agree = {}
for t in range(5):
    W = [h for h in FAM if len(h) <= 5 - t]
    agree[t] = (part_of(P[t], W) == part_of(P[t + 1], W))
check("MG2b stabilization is AT t = 2, blockwise, on every window "
      "computable from the cache: P_t vs P_{t+1} DIFFER at t = 0, 1 "
      "and AGREE at t = 2, 3, 4 (three consecutive agreements coded "
      "— round-1 F-B5 repaired)",
      agree == {0: False, 1: False, 2: True, 3: True, 4: True},
      f"agreements per t = {agree}")

pA0 = ('p', 'A', V0, 0)
pB0 = ('p', 'B', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA, tB = ('A', V0, 0), ('B', V0, 1)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
PAIR = ('r', 'A', frozenset({tA, tB}), frozenset({tA}))
REPS = [[], [pA0], [pA0, pB0], [pA0, pB1], [pA0, SELFA],
        [pA0, pB0, SELFA]]
raw = [P[2][tuple(r)] for r in REPS]
n6 = len({P[2][tuple(h)] for h in FAM if len(h) <= 4})
check("MG2c the SIX states, labeled 0-5 by shortest representatives "
      "(0 quiescent/shared base incl. root+pads+renewals; 1 one live "
      "proposal; 2 two non-conflicting live; 3 THE CONFLICT PAIR "
      "[pA0,pB1]; 4 diverged holdings, quiescent; 5 diverged + one "
      "live proposal): |P_2| = 6 on len<=4 and the six "
      "representatives land in six DISTINCT classes",
      n6 == 6 and len(set(raw)) == 6,
      f"|P_2 on len<=4| = {n6}; representatives distinct = "
      f"{len(set(raw)) == 6}")
repmap = {r: i for i, r in enumerate(raw)}
CLS = {tuple(h): repmap.get(P[2][tuple(h)], -1)
       for h in FAM if len(h) <= 4}

T_REF = {
    0: {0: Fr(3, 2), 1: Fr(1, 2)},
    1: {1: Fr(3, 2), 2: Fr(1, 8), 3: Fr(1, 8), 4: Fr(1, 4)},
    2: {2: Fr(3, 2), 5: Fr(1, 2)},
    3: {0: Fr(1, 2), 3: Fr(3, 2), 5: Fr(1, 2)},
    4: {4: Fr(3, 2), 5: Fr(1, 2)},
    5: {2: Fr(1, 4), 4: Fr(1, 4), 5: Fr(3, 2)},
}
rows = {}
ok_wd = True
n_members = 0
for h in FAM:
    if len(h) > 3: continue
    n_members += 1
    r = CLS[tuple(h)]
    row = {}
    for e, q in CACHE[tuple(h)]:
        c2 = CLS[tuple(h + [e])]
        row[c2] = row.get(c2, Fr(0)) + q
    if r in rows:
        ok_wd &= (rows[r] == row)
    else:
        rows[r] = row
rowsums = [sum(rows.get(i, {}).values()) for i in range(6)]
check("MG2d the EXACT 6 x 6 transfer: WELL-DEFINED per state (every "
      "one of the 215 len<=3 members of a class yields the same "
      "exact row — the probabilistic-bisimulation property, gated) "
      "and equal to the referee matrix; row sums = the per-cut N "
      "(2,2,2,5/2,2,2 — the conflict state carries the 5/4-per-actor "
      "excess)",
      ok_wd and n_members == 215 and rows == T_REF
      and rowsums == [Fr(2), Fr(2), Fr(2), Fr(5, 2), Fr(2), Fr(2)],
      f"members = {n_members}; well-defined = {ok_wd}; rows == "
      f"referee T = {rows == T_REF}; row sums = "
      f"{[str(x) for x in rowsums]}")
T = [[rows.get(i, {}).get(j, Fr(0)) for j in range(6)]
     for i in range(6)]

# ---- MG3: the exact Perron program ---------------------------------
adj = {i: [j for j in range(6) if T[i][j] != 0] for i in range(6)}
index = {}; low = {}; onstack = {}; stack = []; sccs = []
counter = [0]
def strongconnect(v):
    index[v] = low[v] = counter[0]; counter[0] += 1
    stack.append(v); onstack[v] = True
    for w in adj[v]:
        if w not in index:
            strongconnect(w)
            low[v] = min(low[v], low[w])
        elif onstack.get(w):
            low[v] = min(low[v], index[w])
    if low[v] == index[v]:
        comp = []
        while True:
            w = stack.pop(); onstack[w] = False
            comp.append(w)
            if w == v: break
        sccs.append(sorted(comp))
for v in range(6):
    if v not in index: strongconnect(v)
nontrivial = sorted(c for c in sccs
                    if len(c) > 1 or T[c[0]][c[0]] != 0)
DOM, TRA = [2, 4, 5], [0, 1, 3]
closed_dom = all(T[i][j] == 0 for i in DOM for j in range(6)
                 if j not in DOM)
flow_in = any(T[i][j] != 0 for i in TRA for j in DOM)
check("MG3a Tarjan SCC decomposition: exactly two nontrivial "
      "classes — {0,1,3} (the shared/conflict sector, TRANSIENT, "
      "carrying the renewal loop 3 -> 0) and {2,4,5} (the "
      "no-conflict-possible sector, CLOSED at this grammar's scope: "
      "d42a-terminal has no delivery events, so diverged holdings "
      "never re-converge; d42b1 transport = the named successor "
      "scope)",
      nontrivial == [TRA, DOM] and closed_dom and flow_in,
      f"nontrivial classes = {nontrivial}; dominant closed = "
      f"{closed_dom}; transient->dominant flow = {flow_in}")

def charpoly(M):
    n = len(M)
    coeffs = [Fr(1)]
    Mk = [[Fr(1) if i == j else Fr(0) for j in range(n)]
          for i in range(n)]
    for kk in range(1, n + 1):
        Mk = [[sum(M[i][t2] * Mk[t2][j] for t2 in range(n))
               for j in range(n)] for i in range(n)]
        tr = sum(Mk[i][i] for i in range(n))
        c = -tr / kk
        coeffs.append(c)
        for i in range(n): Mk[i][i] += c
    return coeffs
def peval(cs, x):
    v = Fr(0)
    for c in cs: v = v * x + c
    return v
Md = [[T[i][j] for j in DOM] for i in DOM]
Mt = [[T[i][j] for j in TRA] for i in TRA]
LAM = Fr(2)
f = [Fr(4, 3), Fr(4, 3), Fr(1), Fr(7, 3), Fr(1), Fr(1)]
char_ok = (peval(charpoly(Md), LAM) == 0)
eig_ok = all(sum(T[i][j] * f[j] for j in range(6)) == LAM * f[i]
             for i in range(6))
check("MG3b lambda = 2 EXACT: the exact characteristic polynomial "
      "of T restricted to {2,4,5} vanishes at 2 (Faddeev-LeVerrier, "
      "Fractions; u = lambda - 3/2 satisfies u^2 = 1/4 — rational "
      "spectrum, no bisection needed) AND the eigen-identity "
      "T f = 2 f holds EXACTLY on the whole chain with the positive "
      "vector f = (4,4,3,7,3,3)/3",
      char_ok and eig_ok and all(x > 0 for x in f),
      f"charpoly_dom(2) == 0 = {char_ok}; T f == 2 f exact = "
      f"{eig_ok}; f = {[str(x) for x in f]}")

A2 = [[(Fr(2) if i == j else Fr(0)) - Mt[i][j] for j in range(3)]
      for i in range(3)]
aug = [A2[i][:] + [Fr(1) if i == j else Fr(0) for j in range(3)]
       for i in range(3)]
det = Fr(1)
sing = False
for col in range(3):
    piv = next((r2 for r2 in range(col, 3) if aug[r2][col] != 0),
               None)
    if piv is None:
        sing = True; break
    if piv != col:
        aug[col], aug[piv] = aug[piv], aug[col]; det = -det
    det *= aug[col][col]
    pv = aug[col][col]
    aug[col] = [x / pv for x in aug[col]]
    for r2 in range(3):
        if r2 != col and aug[r2][col] != 0:
            fac = aug[r2][col]
            aug[r2] = [a - fac * b2 for a, b2 in zip(aug[r2],
                                                     aug[col])]
inv = [] if sing else [r2[3:] for r2 in aug]
inv_pos = (not sing) and all(x >= 0 for r2 in inv for x in r2)
b = [sum(T[i][j] * f[j] for j in DOM) for i in TRA]
ext = ([sum(inv[i][j] * b[j] for j in range(3)) for i in range(3)]
       if not sing else [])
ext_ok = (ext == [Fr(4, 3), Fr(4, 3), Fr(7, 3)])
check("MG3c dominant-class UNIQUENESS + the forced transient "
      "extension: det(2I - M_transient) = 3/32 > 0 and (2I - "
      "M_transient)^{-1} is entrywise >= 0 [nonnegative matrix with "
      "nonnegative resolvent at s => spectral radius < s — the "
      "M-matrix theorem; the transient radius is 3/2 + (1/32)^(1/3) "
      "~ 1.815], so {2,4,5} is the UNIQUE dominant class; and the "
      "resolvent applied to the cross-flow returns EXACTLY "
      "(4/3, 4/3, 7/3) — the positive 2-harmonic function is unique "
      "up to scale on the whole chain: existence AND uniqueness, "
      "the MG3 decision, delivered",
      (not sing) and det == Fr(3, 32) and inv_pos and ext_ok,
      f"det = {det}; resolvent nonnegative = {inv_pos}; forced "
      f"extension = {[str(x) for x in ext]}")

qp = [[T[i][j] * f[j] / (LAM * f[i]) for j in range(6)]
      for i in range(6)]
norm_ok = all(sum(qp[i]) == 1 for i in range(6))
conf = {j: qp[3][j] for j in range(6) if qp[3][j] != 0}
conf_s = str({k: str(v) for k, v in sorted(conf.items())})
check("MG3d the completed transfer q'(i->j) = T_ij f_j / (2 f_i) is "
      "per-state normalized EXACTLY (all six rows sum to 1 — the "
      "root-free completion exhibited); conflict-state row anchor "
      "{0: 1/7, 3: 3/4, 5: 3/28}",
      norm_ok and conf == {0: Fr(1, 7), 3: Fr(3, 4), 5: Fr(3, 28)},
      f"row sums exact = {norm_ok}; conflict row = " + conf_s)

H3 = [pA0, pB1, PAIR]
mg4_all_t = all(P[t][tuple([])] == P[t][tuple(H3)] for t in range(4))
check("MG4 the ROOT-FREE CERTIFICATE (a real gate — round-1 F-B3 "
      "repaired): the root and the post-arb renewal point H3 = "
      "[pA0, pB1, PAIR] are the SAME intrinsic state (class 0), at "
      "every computable lookahead t = 0..3 — the boundary-frozen "
      "runs split them at every depth (NC3 below): d42b56-S2's "
      "obstruction was the truncation marker's artifact",
      CLS[()] == 0 and CLS[tuple(H3)] == 0 and mg4_all_t,
      f"root class = {CLS[()]}; renewal class = {CLS[tuple(H3)]}; "
      f"P_t equal at all t<=3 = {mg4_all_t}")

pi = {2: Fr(1, 4), 4: Fr(1, 4), 5: Fr(1, 2)}
left_ok = all(sum(pi[i] * T[i][j] for i in DOM) == LAM * pi[j]
              for j in DOM)
stat_ok = all(sum(pi[i] * f[i] * qp[i][j] for i in DOM)
              == pi[j] * f[j] for j in DOM)
check("MG5 the MASS-TRANSPORT identity, EXACT (no residual, no "
      "tolerance — the round-1 approximate-witness design retired): "
      "the left eigenvector pi = (1/4, 1/4, 1/2) on {2,4,5} "
      "satisfies pi T = 2 pi exactly, and the pi.f-weighted law is "
      "invariant under the completed q' exactly [import I1's "
      "unimodularity face at state-chain scope; the rooted-graph "
      "continuum form stays the declared successor]",
      left_ok and stat_ok,
      f"pi T == 2 pi exact = {left_ok}; exact stationarity = "
      f"{stat_ok}")

# ---- MG6: delta D-r1 — ingredient (ii) receipt-carried -------------
V1 = vname(V0, frozenset({tA}), 'A')
def _sub_v(b, tgt):
    return tgt if b == V0 else ('v', _sub_v(b[1], tgt), b[2], b[3],
                                b[4])
def _sub_e(e, tgt):
    if e[0] == 'p':
        return ('p', e[1], _sub_v(e[2], tgt), e[3])
    if e[0] == 'r':
        return ('r', e[1],
                frozenset((t[0], _sub_v(t[1], tgt), t[2])
                          for t in e[2]),
                frozenset((t[0], _sub_v(t[1], tgt), t[2])
                          for t in e[3]))
    return e
ROOT3 = [h for h in FAM if len(h) <= 3]
H3T = {tuple(h[3:]) for h in FAM if tuple(h[:3]) == tuple(H3)}
IMG = {tuple(_sub_e(e, V1) for e in h) for h in ROOT3}
iso_nodes = (len(ROOT3) == 215 and len(IMG) == 215 and IMG == H3T)
iso_menus = all(
    {_sub_e(e, V1): q for e, q in CACHE[tuple(h)]}
    == dict(CACHE[tuple(H3) + tuple(_sub_e(x, V1) for x in h)])
    for h in FAM if len(h) <= 3)
REN = [h for h in FAM if len(h) <= 4 and CLS[tuple(h)] == 0
       and any(e[0] == 'r' for e in h)]
ROOTMENU = CACHE[tuple([])]
ren_ok = True
for h in REN:
    vw = View(h, event_poset(h), set(range(len(h))))
    shared = (vw.holdings('A') & vw.holdings('B')) - vw.superseded
    if len(shared) != 1:
        ren_ok = False; break
    tgt = next(iter(shared))
    if {_sub_e(e, tgt): q for e, q in ROOTMENU} != dict(
            CACHE[tuple(h)]):
        ren_ok = False; break
check("MG6 (delta D-r1) the RENEWAL SUBTREE ISOMORPHISM, "
      "receipt-gated: base substitution v0 -> v1 maps the root tree "
      "ONTO the H3 subtree — 215 == 215 nodes — with menus "
      "event-bijective and q-EQUAL at every node incl. the depth-3 "
      "shell (extends d42b56-S2's one-step bijection two levels); "
      "and ALL clean-slate renewal points at len <= 4 (class 0 "
      "carrying an arb; each with a UNIQUE shared non-superseded "
      "base) have root-identical one-step menus under their own base "
      "substitution — the 144-point census. Closure-theorem "
      "ingredient (ii) joins (i) (NC3) as receipt-carried",
      iso_nodes and iso_menus and len(REN) == 144 and ren_ok,
      f"nodes {len(ROOT3)} == {len(H3T)}, image == subtree = "
      f"{iso_nodes}; q-equal menus all nodes = {iso_menus}; renewal "
      f"census = {len(REN)}; per-point menu identity = {ren_ok}")

# ========= SECTION B — the negative control (the round-1 object) ====
# The first build's boundary-marked truncation quotient (the
# committed d42b56-S3 algorithm at depths 4/5/6), retained with its
# delivered counts as ANCHORED EXPECTATIONS: its growth is HORIZON
# STRATIFICATION, not state birth — exhibited by the pad-shift
# theorem and the 17 -> 6 stratification map, both gated.
def bisim(fam, cache, depth):
    """The truncation algorithm (verbatim semantics): boundary
    (len == depth) marked 'B'; interior refined by (shape, successor
    multiset)."""
    state = {tuple(h): repr(menu_shape(cache[tuple(h)])) for h in fam}
    traj = [len(set(state.values()))]
    while True:
        new = {}
        for h in fam:
            k = tuple(h)
            if len(h) == depth:
                new[k] = (state[k], 'B')
            else:
                succ = tuple(sorted((str(q), state[tuple(h + [e])])
                                    for e, q in cache[k]))
                new[k] = (state[k], succ)
        relab = {}
        for k in sorted(new, key=repr):
            relab.setdefault(new[k], len(relab))
        s2 = {k: relab[new[k]] for k in new}
        traj.append(len(set(s2.values())))
        if len(set(s2.values())) == len(set(state.values())):
            return s2, traj
        state = {k: str(v) for k, v in s2.items()}

S4, traj4 = bisim([h for h in FAM if len(h) <= 4], CACHE, 4)
S5, traj5 = bisim([h for h in FAM if len(h) <= 5], CACHE, 5)
S6, traj6 = bisim(FAM, CACHE, 6)
n4, n5, n6c = (len(set(S4.values())), len(set(S5.values())),
               len(set(S6.values())))
check("MG1 REGRESSION anchor, re-scoped per round-1 F-B1 (a fact "
      "about the TRUNCATION algorithm, NOT the intrinsic anchor — "
      "pin §2's anchor clause was unsatisfiable and is "
      "forward-corrected in note §5 A1): the depth-4 run reproduces "
      "the committed d42b56-S3 17-state partition, trajectory "
      "4-9-14-16-17",
      n4 == 17 and traj4[:5] == [4, 9, 14, 16, 17],
      f"states = {n4}; trajectory = {traj4}")

def induced(S, cutoff):
    part = {}
    for k, v in S.items():
        if len(k) <= cutoff:
            part.setdefault(v, set()).add(k)
    return frozenset(frozenset(x) for x in part.values())
p4_full = induced(S4, 4)
p5_on4 = induced(S5, 4)
p6_on4 = induced(S6, 4)
p6_on5 = induced(S6, 5)
check("NC1 the round-1 delivered counts, now ANCHORED as "
      "expectations (F-B3 repaired — a corrupted datum now fails): "
      "boundary-coarse 17/23/29 at depths 4/5/6; induced-on-4 "
      "by-5 = 19, by-6 = 20; induced-on-5 by-6 = 25 (+6 per depth = "
      "one new stratum per intrinsic class per level — the "
      "stratification arithmetic)",
      (n4, n5, n6c) == (17, 23, 29) and len(p5_on4) == 19
      and len(p6_on4) == 20 and len(p6_on5) == 25,
      f"counts = {(n4, n5, n6c)}; induced-on-4 = "
      f"{(len(p5_on4), len(p6_on4))}; induced-on-5 by-6 = "
      f"{len(p6_on5)}")

def refines(fine, coarse):
    return all(any(fb <= cb for cb in coarse) for fb in fine)
mono = (refines(p6_on4, p5_on4) and refines(p5_on4, p4_full))
check("NC2 refinement monotonicity (can fail on regression) + the "
      "margin diagnosis: by-6 refines by-5 refines run-4, and the "
      "old MG2 criterion's margin-1 comparison DISAGREES (19 != 20) "
      "— the boundary talking, not state birth; the intrinsic "
      "agreements (MG2b) are the true stabilization criterion",
      mono and p5_on4 != p6_on4,
      f"monotone = {mono}; margin-1 agreement = {p5_on4 == p6_on4} "
      "(the round-1 'NO STABILIZATION' datum, now the documented "
      "horizon artifact)")

padbad = padcnt = 0
for h in FAM:
    if len(h) > 5: continue
    base = {e: q for e, q in CACHE[tuple(h)]}
    for a in AB:
        padcnt += 1
        if {e: q for e, q in CACHE[tuple(h + [('n', a)])]} != base:
            padbad += 1
pads = [[('n', 'A')] * k for k in range(5)]
pblocks = [S4[tuple(p)] for p in pads]
pcls = [CLS[tuple(p)] for p in pads]
check("NC3 the PAD-SHIFT THEOREM, gated family-wide (the healing's "
      "first ingredient): appending a noop leaves the candidate "
      "menu IDENTICAL — events and weights — at all 12,942 pad "
      "extensions; the exhibit: [], [n], [nn], [nnn], [nnnn] occupy "
      "FIVE distinct blocks of the committed 17 (and H3 is "
      "co-classed with [nnn]: equal remaining horizon, not equal "
      "structure) yet ONE intrinsic class (0)",
      padcnt == 12942 and padbad == 0 and len(set(pblocks)) == 5
      and pcls == [0, 0, 0, 0, 0]
      and S4[tuple(H3)] == S4[tuple([('n', 'A')] * 3)]
      and CLS[tuple(H3)] == 0,
      f"pad checks = {padcnt}, violations = {padbad}; distinct "
      f"truncation blocks = {len(set(pblocks))}; pad intrinsic "
      f"classes = {pcls}")

proj = {}
for k, v in S4.items():
    proj.setdefault(v, set()).add(CLS[k])
pure = {}
mixed = []
for blk in sorted(proj):
    s = proj[blk]
    if len(s) == 1:
        c = next(iter(s)); pure[c] = pure.get(c, 0) + 1
    else:
        mixed.append(tuple(sorted(s)))
onto = set()
for s in proj.values():
    onto |= s
check("NC4 the HORIZON-STRATIFICATION map, gated: the pad-shift "
      "healing maps the 17 truncation states ONTO the 6 intrinsic "
      "classes — 14 pure blocks (3/3/3/3 horizon strata over "
      "classes 0-3; 1/1 over classes 4-5) plus EXACTLY the three "
      "under-split mixing blocks ({0,4} x2, {1,5} x1: the committed "
      "anchor's genuine merge defects — the 17 is coarser AND finer "
      "than the intrinsic object, which is why pin §2's anchor "
      "clause was unsatisfiable)",
      pure == {0: 3, 1: 3, 2: 3, 3: 3, 4: 1, 5: 1}
      and sorted(mixed) == [(0, 4), (0, 4), (1, 5)]
      and onto == set(range(6)),
      f"pure per class = {dict(sorted(pure.items()))}; mixed = "
      f"{sorted(mixed)}; onto all 6 = {onto == set(range(6))}")

cls5 = {}
for h in FAM:
    if len(h) <= 5:
        cls5.setdefault(canon(h), set()).add(S5[tuple(h)])
cls6 = {}
for h in FAM:
    cls6.setdefault(canon(h), set()).add(S6[tuple(h)])
v5 = sum(1 for s in cls5.values() if len(s) > 1)
v6 = sum(1 for s in cls6.values() if len(s) > 1)
check("NC5 gauge well-definedness RE-GATED at the new depths "
      "(round-1 F-B6, the skipped tripwire): the run-5/run-6 "
      "truncation states are constant on every canonical class "
      "(referee anchor: 5,548 classes at depth 6, 0 violations)",
      v5 == 0 and v6 == 0 and len(cls6) == 5548
      and len(cls5) == 1565,
      f"depth-5: {len(cls5)} classes, {v5} violations; depth-6: "
      f"{len(cls6)} classes, {v6} violations")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — anchor/consistency breakage; exit 1")
    sys.exit(1)
print("[VERDICT] d43b round-1 rebuilt, GREEN: the uniform-lookahead "
      "INTRINSIC chain closes at SIX states at lookahead 2 on every "
      "window computable from the depth-6 cache (referee depth-7 "
      "run concurs); the exact transfer is well-defined with "
      "lambda = 2 EXACT, unique dominant class {2,4,5}, positive "
      "harmonic f = (4,4,3,7,3,3)/3 unique up to scale, root = "
      "renewal state, and the mass-transport identity EXACT — "
      "residue 1's Perron reduction is DECIDED on the computed "
      "window at this grammar's scope, pending the renewal-pumping "
      "closure theorem (BOTH ingredients receipt-gated: the "
      "pad-shift identity in NC3; the renewal subtree isomorphism + "
      "the 144-point census in MG6 — delta D-r1). The old "
      "boundary-marked growth "
      "17/23/29 stands as the gated NEGATIVE CONTROL: horizon "
      "stratification, healed exactly onto the six (NC4). [I1]'s "
      "Martin machinery relocates to the d42b1 transport grammar "
      "(deliveries reopen the absorbing sector).")
