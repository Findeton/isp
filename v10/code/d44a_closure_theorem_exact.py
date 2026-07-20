#!/usr/bin/env python3
"""
d44a_closure_theorem_exact.py — v10 D44a (successor 1): the renewal-
pumping closure theorem. Pin: note-d44a-renewal-pumping-closure-
theorem.md (strict). Parents: d43b TERMINAL (#344/#345; six-state
intrinsic chain decided on the window; ingredients receipt-gated NC3
+ MG6); the d42a admission layer exec'd from the committed d42b3
receipt (__file__-anchored, the d43b pattern).

THE DELIVERED OBJECT: sigma(h) = the pin §2 bounded local-state
abstraction — per-actor non-superseded holdings pattern + the live-
proposal structure (payload triples with component/conflict-edge
data) + the superseded marks restricted to bases still carrying
holdings or live proposals — modulo base renaming (canonical form =
minimum over base bijections of the post-renaming-sorted
serialization; genesis and renewal bases identified by the
renaming). CG1 and CG2 hold EXACTLY (zero exceptions on all 34,375,
and — round-1 extension — on the full 145,408-history depth-7
family, out-of-sample). BFS on sigma-space from sigma([]) TERMINATES
at 36 states with the frontier exhausted — the depth-free closure —
and the 36 realize exactly the cache's sigma values, with ZERO new
sigma-states at depth 7.

TWO PIN CLAUSES ARE PROVABLY UNSATISFIABLE AS WRITTEN and are
delivered as gated obstructions + the repaired route (forward
corrections for the note's §6; pre-registered failure-mode
discipline: nothing weakened silently, every replacement clause is a
mechanical gate):
 (A1) CG3's "reachable set == 6 / induced partition == the committed
  six blockwise" cannot hold for ANY CG1-sound sigma: the committed
  intrinsic partition MERGES menu-distinct states (witness, gated in
  CG3b: [pA0,pB0] and [pA0,pB0,selfA,pA(vA,0)] are BOTH intrinsic
  class 2, yet their renamed menus differ entrywise — the two self-
  arbs share one base token in the first and use two tokens in the
  second). Bisimilarity is coarser than menu-identity: CG1 + "==6"
  are jointly contradictory. The repaired CG3: closure at 36 (gated)
  + the EXACT probabilistic-bisimulation quotient of the 36-state
  chain has SIX classes, blockwise EQUAL to the committed intrinsic
  partition, with induced transfer == T_REF. This is NOT the pin §4
  reversal mode: no seventh intrinsic state exists — the fine states
  merge under the gated exact quotient, and the closure theorem's
  conclusion (six states at every VERIFIED depth, transfer T, Perron
  package) is delivered THROUGH the quotient (CG5 runs on it; the
  all-depth quantifier is CONDITIONAL on the named structural
  menu-factorization lemma — round-1 F1/R2, note §7).
 (A2) CG4's "length <= 3" normal form is false as written: 17 of the
  36 sigma-states have NO realization below length 4 (divergence
  needs two arbs + two proposals; gated census), and the reduction
  cannot cross the diverged sector because that sector contains no
  clean-slate renewal points at d42a scope (no deliveries — exactly
  the pin §5 scope note). Delivered instead: the reduction (pad
  deletion + renewal truncation via MG6-style base back-substitution)
  is gated VALID on all 34,375 (sigma-preserving, idempotent, zero
  mechanism failures), its length spectrum is anchored (max 6), the
  irreducible witness is exhibited, and the window-realization the
  pin §4 proof sketch actually needs holds at quotient level: every
  history's intrinsic class is realized at length <= 3.

Banner: EXACT Fractions throughout; deterministic (all canonical
forms are post-renaming-sorted plain-tuple serializations — no raw
frozenset reprs); exit 1 on any gate failure.
"""
import os
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import permutations

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
vname = ns['vname']
View = ns['View']
event_poset = ns['event_poset']
AB = ('A', 'B')

print("[d44a — the renewal-pumping closure theorem]")
print("  banner: EXACT; d42a layer from the committed d42b3 receipt")
print("  (__file__-anchored); ONE depth-6 enumeration re-anchored;")
print("  sigma = the pin-2 local-state abstraction modulo base")
print("  renaming (canonical form: min over base bijections of the")
print("  post-renaming-sorted serialization); CG1/CG2 exact on the")
print("  full cache; CG3 = depth-free BFS closure (36 states) + the")
print("  gated obstruction (no CG1-sound sigma induces exactly six)")
print("  + the exact bisimulation quotient == the committed six;")
print("  CG4 = the reduction gated + the <=3 clause's obstruction")
print("  exhibited + quotient-window realization; CG5 = the Perron")
print("  package on the quotient transfer; CG6 = negative controls.")
print("  Deviations A1/A2 are forward corrections, printed above and")
print("  gated below — no clause was silently weakened.")
print("  Round-1 amendments (frozen review d44a-round1, note §7):")
print("  the depth-7 out-of-sample extension gated in-receipt (CG7a-")
print("  CG7e, all 145,408 depth-7 histories); the COMMITTED per-")
print("  candidate quotient operator gated (CG3f, round-1 F2); BFS")
print("  frontier exhaustion gated (CG3a, round-1 F4); CG4 relabeled")
print("  as the mechanism exhibit off the assembly route (round-1")
print("  F5); the verdict rescoped to EVERY VERIFIED DEPTH with the")
print("  structural menu-factorization lemma as the NAMED RESIDUAL")
print("  (round-1 F1, route R2).")

# ---- SG0: one enumeration, census re-anchored ----------------------
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
check("SG0 the enumeration anchor: cumulative depth-0..6 family "
      "sizes equal the referee-verified census (pin CG1's re-anchor)",
      cum == [1, 7, 39, 215, 1191, 6471, 34375],
      f"sizes = {cum}")

def cands_of(hk):
    if hk not in CACHE: CACHE[hk] = candidates_for(list(hk), AB)
    return CACHE[hk]

# ========== SECTION A — sigma: the local-state abstraction ==========
# Derived from the committed View machinery only (holdings / live /
# superseded / components / edges); no admission logic reinvented.
SG_VIOL = {'alive': 0, 'nonsup': 0, 'liveX': 0, 'cmp': 0}

def own_alive(h, a):
    """a's own-view alive holdings: the committed View on a's chain
    past (the d42b3 own-view pattern: append a noop, take its
    past-cone). The d42a invariant (gated in SG2): a SINGLETON."""
    acts2 = list(h) + [('n', a)]
    pred = event_poset(acts2)
    vw = View(acts2, pred, pred[len(acts2) - 1])
    alive = {b for b in vw.holdings(a) if b not in vw.superseded}
    if len(alive) != 1:
        SG_VIOL['alive'] += 1
    return sorted(alive, key=repr)[0]

RAWMEMO = {}
def sigma_raw(hk):
    """The pin-2 data, with raw base names as placeholders:
    - hold: per actor the full-view NON-SUPERSEDED holding
      (singleton-or-empty at d42a scope, gated; None = empty);
    - live: the live-proposal triples (proposer, base, payload bit);
    - comps: the conflict components of the live proposals with
      their edge structure (committed components()/edges());
    - refs: the referenced bases = held or live-carrying (bullet 3:
      dead structure carrying nothing is dropped);
    - sup: the full-view superseded set (marks are taken on refs)."""
    if hk in RAWMEMO: return RAWMEMO[hk]
    h = list(hk)
    pred = event_poset(h)
    fv = View(h, pred, set(range(len(h))))
    sup = fv.superseded
    X = {a: own_alive(h, a) for a in AB}
    hold = {}
    for a in AB:
        if not (fv.holdings(a) - sup <= {X[a]}):
            SG_VIOL['nonsup'] += 1
        hold[a] = X[a] if X[a] not in sup else None
    live = tuple(sorted(((op[1], op[2], op[3])
                         for op in fv.live.values()), key=repr))
    for t in live:
        if t[1] not in (X['A'], X['B']):
            SG_VIOL['liveX'] += 1
    li = sorted(fv.live.items())
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            (i1, o1), (i2, o2) = li[i], li[j]
            if (o1[2] == o2[2] and o1[3] != o2[3]
                    and not fv.incomparable(i1, i2)):
                SG_VIOL['cmp'] += 1
    comps = []
    for base, idxs in fv.components():
        mem = tuple(sorted((fv.props[i][1], fv.props[i][3])
                           for i in idxs))
        E = tuple(sorted(tuple(sorted(((fv.props[i][1],
                                        fv.props[i][3]),
                                       (fv.props[k][1],
                                        fv.props[k][3]))))
                         for (i, k) in fv.edges(set(idxs))))
        comps.append((base, mem, E))
    refs = sorted({b for b in (hold['A'], hold['B']) if b is not None}
                  | {t[1] for t in live}, key=repr)
    RAWMEMO[hk] = (hold, tuple(live), tuple(comps), tuple(refs), sup)
    return RAWMEMO[hk]

def ser(hold, live, comps, refs, sup, m):
    """One serialization under the base renaming m — every listed
    part is sorted AFTER renaming (order-independence)."""
    return repr((tuple((a, m.get(hold[a])) for a in AB),
                 tuple(sorted(((t[0], m[t[1]], t[2]) for t in live),
                              key=repr)),
                 tuple(sorted(((m[c[0]], c[1], c[2]) for c in comps),
                              key=repr)),
                 tuple(sorted((m[b], b in sup) for b in refs))))

SIGMEMO = {}
def canon_sigma(hk):
    """sigma(h): minimum serialization over all base bijections
    refs -> {0..k-1} (k <= 2 at d42a scope)."""
    if hk in SIGMEMO: return SIGMEMO[hk]
    hold, live, comps, refs, sup = sigma_raw(hk)
    best = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        s = ser(hold, live, comps, refs, sup, m)
        if best is None or s < best: best = s
    SIGMEMO[hk] = best
    return best

SIG = {tuple(h): canon_sigma(tuple(h)) for h in FAM}
NSIG = len(set(SIG.values()))
wins = [len({SIG[tuple(h)] for h in FAM if len(h) <= c})
        for c in (2, 3, 4, 5, 6)]
check("SG1 sigma is computed on the ENTIRE cache; distinct-value "
      "growth over the len<=2/3/4/5/6 windows is the anchored "
      "[11, 19, 28, 32, 36] — 36 values total, finite by "
      "construction on every window",
      NSIG == 36 and wins == [11, 19, 28, 32, 36],
      f"windows = {wins}")
check("SG2 the d42a view invariants sigma relies on, gated family-"
      "wide (34,375 histories): every actor's own-view alive holding "
      "is a SINGLETON; full-view non-superseded holdings lie inside "
      "it; every live proposal sits on its proposer's own-view "
      "base; conflicting live pairs (same base, opposite payload) "
      "are always poset-incomparable",
      all(v == 0 for v in SG_VIOL.values()),
      f"violations = {SG_VIOL}")

# renaming-invariance: the MG6 substitution pair, all 215
tA = ('A', V0, 0)
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
pA0 = ('p', 'A', V0, 0)
pB0 = ('p', 'B', V0, 0)
pB1 = ('p', 'B', V0, 1)
tB = ('B', V0, 1)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
PAIR = ('r', 'A', frozenset({tA, tB}), frozenset({tA}))
H3 = (pA0, pB1, PAIR)
ren_bad = ren_n = 0
for h in FAM:
    if len(h) > 3: continue
    ren_n += 1
    h2 = H3 + tuple(_sub_e(e, V1) for e in h)
    if canon_sigma(h2) != SIG[tuple(h)]: ren_bad += 1
check("SG3 base-renaming invariance, gated on the MG6 isomorphism "
      "pair: for all 215 root-tree members h, sigma(H3 + sub_v0->v1 "
      "(h)) == sigma(h) — histories differing only by base identity "
      "get EQUAL sigma (and root == renewal point in sigma-space, "
      "the h = [] instance)",
      ren_n == 215 and ren_bad == 0
      and canon_sigma(H3) == SIG[()],
      f"pairs = {ren_n}, mismatches = {ren_bad}; sigma(H3) == "
      f"sigma([]) = {canon_sigma(H3) == SIG[()]}")

# ===== SECTION B — the committed intrinsic partition, re-derived ====
# Ported verbatim from the committed d43b receipt (P_0 = menu shape;
# P_{t+1} = one probabilistic-bisimulation refinement; horizon-
# uniform), with its anchors re-gated: this is the object CG3's
# quotient must equal.
def menu_shape(c):
    d = {}
    for e, q in c:
        d[(e[0], q)] = d.get((e[0], q), 0) + 1
    return tuple(sorted(d.items(), key=repr))

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

REPS6 = [(), (pA0,), (pA0, pB0), (pA0, pB1), (pA0, SELFA),
         (pA0, pB0, SELFA)]
raw6 = [P[2][r] for r in REPS6]
n6 = len({P[2][tuple(h)] for h in FAM if len(h) <= 4})
check("SB1 the committed intrinsic partition re-derived (d43b MG2a/"
      "MG2c port): |P_2| == 6 on len<=4 and the six shortest "
      "representatives (0 quiescent/shared; 1 one live; 2 two non-"
      "conflicting live; 3 the conflict pair; 4 diverged quiescent; "
      "5 diverged + one live) land in six distinct classes",
      n6 == 6 and len(set(raw6)) == 6,
      f"|P_2 on len<=4| = {n6}; reps distinct = "
      f"{len(set(raw6)) == 6}")
repmap = {r: i for i, r in enumerate(raw6)}
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
check("SB2 the committed transfer re-derived (d43b MG2d port): "
      "well-defined per class on all 215 len<=3 members and equal "
      "to T_REF, row sums (2, 2, 2, 5/2, 2, 2)",
      ok_wd and n_members == 215 and rows == T_REF
      and [sum(rows[i].values()) for i in range(6)]
      == [Fr(2), Fr(2), Fr(2), Fr(5, 2), Fr(2), Fr(2)],
      f"members = {n_members}; well-defined = {ok_wd}; rows == "
      f"T_REF = {rows == T_REF}")
splits = defaultdict(set)
onto1 = defaultdict(set)
for h in FAM:
    if len(h) > 4: continue
    splits[CLS[tuple(h)]].add(SIG[tuple(h)])
    onto1[SIG[tuple(h)]].add(CLS[tuple(h)])
check("SB3 sigma REFINES the committed partition on the window "
      "(every sigma-block lies inside one intrinsic class) with the "
      "anchored split census {0:1, 1:4, 2:10, 3:2, 4:3, 5:8} on "
      "len<=4 — the intrinsic classes 1/2/4/5 each merge several "
      "menu-distinct or label-distinct sigma-states, class 0 (root/"
      "renewal) and the payload-mirrored classes 3 stay near-fine",
      all(len(v) == 1 for v in onto1.values())
      and {c: len(v) for c, v in sorted(splits.items())}
      == {0: 1, 1: 4, 2: 10, 3: 2, 4: 3, 5: 8},
      f"splits = { {c: len(v) for c, v in sorted(splits.items())} }; "
      f"mixed sigma-blocks = "
      f"{sum(1 for v in onto1.values() if len(v) > 1)}")

# ================= SECTION C — CG1 and CG2, exact ===================
def _rename_event(e, m2):
    """Event under a base renaming, rebuilt with sorted plain tuples
    (never a raw frozenset repr)."""
    if e[0] == 'p':
        return ('p', e[1], m2[e[2]], e[3])
    if e[0] == 'r':
        return ('r', e[1],
                tuple(sorted((t[0], m2[t[1]], t[2]) for t in e[2])),
                tuple(sorted((t[0], m2[t[1]], t[2]) for t in e[3])))
    return e

def _menu_extras(menu, m):
    """Bases the menu mentions beyond sigma's refs: the admission
    layer shows actors their own-view proposables, which can be
    full-view-dead structure sigma has dropped (bullet 3); the
    canonical menu extends the sigma renaming over them
    deterministically (minimum serialization over extensions)."""
    ex = set()
    for e, q in menu:
        if e[0] == 'p' and e[2] not in m:
            ex.add(e[2])
        elif e[0] == 'r':
            for t in tuple(e[2]) + tuple(e[3]):
                if t[1] not in m: ex.add(t[1])
    return sorted(ex, key=repr)

def canon_menu(hk):
    """The menu of h as an event-multiset with exact weights, under
    the SAME canonical renaming as sigma(h) (extended over menu-only
    bases; all remaining freedom minimized deterministically)."""
    hold, live, comps, refs, sup = sigma_raw(hk)
    menu = cands_of(hk)
    sbest = canon_sigma(hk)
    mbest = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        if ser(hold, live, comps, refs, sup, m) != sbest: continue
        extras = _menu_extras(menu, m)
        for eperm in permutations(range(len(extras))):
            m2 = dict(m)
            for i in range(len(extras)):
                m2[extras[i]] = 100 + eperm[i]
            rows = tuple(sorted((repr(_rename_event(e, m2)), str(q))
                                for e, q in menu))
            s1 = repr(rows)
            if mbest is None or s1 < mbest: mbest = s1
    return mbest

groups = defaultdict(list)
for h in FAM:
    groups[SIG[tuple(h)]].append(tuple(h))
cg1_bad = []
cg1_hist = 0
CLASS_MENU = {}
for sg in sorted(groups):
    menus = set()
    for hk in groups[sg]:
        menus.add(canon_menu(hk))
        cg1_hist += 1
    if len(menus) > 1:
        cg1_bad.append((sg, sorted(groups[sg], key=len)[:2]))
    CLASS_MENU[sg] = min(menus)
if cg1_bad:
    print("  [CG1 SPLITTING PAIR]", cg1_bad[0])
check("CG1 MENU FACTORIZATION, exhaustive on the entire cache: "
      "menu(h) as an event-multiset-up-to-renaming with exact "
      "Fraction weights is a FUNCTION of sigma(h) — all 34,375 "
      "histories in all 36 sigma-classes, entrywise, ZERO exceptions",
      cg1_hist == 34375 and len(groups) == 36 and not cg1_bad,
      f"histories = {cg1_hist}; sigma-classes = {len(groups)}; "
      f"violating classes = {len(cg1_bad)}")

def canon_pair(hk, e):
    """(sigma(h), e) jointly canonical: e renamed under the sigma-
    minimizing bijections (extended over e's extra bases),
    minimized. The CG2 key."""
    hold, live, comps, refs, sup = sigma_raw(hk)
    sbest = canon_sigma(hk)
    ebest = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        if ser(hold, live, comps, refs, sup, m) != sbest: continue
        extras = _menu_extras([(e, None)], m)
        for eperm in permutations(range(len(extras))):
            m2 = dict(m)
            for i in range(len(extras)):
                m2[extras[i]] = 100 + eperm[i]
            s1 = repr(_rename_event(e, m2))
            if ebest is None or s1 < ebest: ebest = s1
    return (sbest, ebest)

TRANS = {}
cg2_bad = []
cg2_n = 0
for h in FAM:
    if len(h) >= 6: continue
    hk = tuple(h)
    for e, q in CACHE[hk]:
        cg2_n += 1
        key = canon_pair(hk, e)
        tgt = SIG[hk + (e,)]
        if key in TRANS:
            if TRANS[key] != tgt:
                cg2_bad.append((hk, e))
        else:
            TRANS[key] = tgt
if cg2_bad:
    print("  [CG2 SPLITTING PAIR]", cg2_bad[0])
check("CG2 TRANSITION DETERMINISM, exhaustive on the cache: "
      "sigma(h + [e]) is a function of (sigma(h), e-up-to-renaming) "
      "— all 34,374 cached transitions, 160 distinct abstract "
      "transition keys, ZERO exceptions",
      cg2_n == 34374 and len(TRANS) == 160 and not cg2_bad,
      f"transitions = {cg2_n}; keys = {len(TRANS)}; violations = "
      f"{len(cg2_bad)}")

# ====== SECTION D — CG3: the depth-free closure + the quotient ======
SROOT = SIG[()]
REP = {SROOT: ()}
bfs_q = [SROOT]
n_expanded = 0
n_bfs_edges = 0
while bfs_q:
    s = bfs_q.pop(0)
    hk = REP[s]
    n_expanded += 1
    for e, q in cands_of(hk):
        n_bfs_edges += 1
        s2 = canon_sigma(hk + (e,))
        if s2 not in REP:
            REP[s2] = hk + (e,)
            bfs_q.append(s2)
maxrep = max(len(r) for r in REP.values())
rep_spec = defaultdict(int)
for r in REP.values():
    rep_spec[len(r)] += 1
check("CG3a THE DEPTH-FREE CLOSURE: BFS on sigma-space from "
      "sigma([]) using one representative per class (licensed by "
      "CG2) TERMINATES WITH THE FRONTIER EXHAUSTED — every one of "
      "the 36 reachable representatives was EXPANDED (round-1 F4: "
      "a capped/budget-stopped BFS cannot pass this gate silently); "
      "the reachable set has exactly 36 states, the representative-"
      "length spectrum is anchored {0:1, 1:4, 2:6, 3:8, 4:9, 5:4, "
      "6:4} (max 6 — the minimal ABSTRACT realization lengths, a "
      "property of the chain, not a cap), the TRAVERSED-EDGE count "
      "== 176 (delta D1: previously print-only — a depth-cap mutant "
      "passed with 160; now gated, the deficit of 16 being exactly "
      "the depth-6->7 keys), and the set coincides EXACTLY with the "
      "sigma values realized on the cache",
      len(REP) == 36 and maxrep == 6
      and n_expanded == 36 and not bfs_q
      and n_bfs_edges == 176
      and dict(rep_spec) == {0: 1, 1: 4, 2: 6, 3: 8, 4: 9, 5: 4,
                             6: 4}
      and set(REP) == set(SIG.values()),
      f"reachable = {len(REP)}; expanded = {n_expanded}; traversed "
      f"edges = {n_bfs_edges}; rep-length spectrum = "
      f"{dict(sorted(rep_spec.items()))}; reachable == "
      f"cache-realized = {set(REP) == set(SIG.values())}")

W1 = (pA0, pB0)
W2 = (pA0, pB0, SELFA, ('p', 'A', V1, 0))
check("CG3b THE OBSTRUCTION, gated (deviation A1's forcing "
      "witness): [pA0,pB0] and [pA0,pB0,selfA,pA(v1,0)] lie in the "
      "SAME committed intrinsic class (2: two non-conflicting live) "
      "but have DIFFERENT canonical menus — the two self-arbs share "
      "one base token in the first (shared slate) and use two "
      "tokens in the second (diverged slate). Hence NO sigma can "
      "satisfy CG1 (equal sigma => identical renamed menus) AND "
      "induce exactly the committed six blockwise: bisimilarity is "
      "strictly coarser than menu-identity on this family, and the "
      "pinned CG3 equality clause is unsatisfiable as written",
      CLS[W1] == 2 and CLS[W2] == 2
      and canon_menu(W1) != canon_menu(W2)
      and SIG[W1] != SIG[W2],
      f"CLS = ({CLS[W1]}, {CLS[W2]}); canonical menus equal = "
      f"{canon_menu(W1) == canon_menu(W2)}; sigma equal = "
      f"{SIG[W1] == SIG[W2]}")

# the exact probabilistic-bisimulation quotient of the 36-state chain
WROW = {}
for s, r in REP.items():
    row = defaultdict(Fr)
    for e, q in cands_of(r):
        row[canon_sigma(r + (e,))] += q
    WROW[s] = dict(row)
shape36 = {s: repr(tuple(sorted((e[0], str(q))
                                for e, q in cands_of(r))))
           for s, r in REP.items()}
QPART = relabel(shape36)
qtraj = [len(set(QPART.values()))]
while True:
    nxt = {}
    for s in REP:
        acc = defaultdict(Fr)
        for s2, q in WROW[s].items():
            acc[QPART[s2]] += q
        nxt[s] = (QPART[s],
                  tuple(sorted((c, str(q)) for c, q in acc.items())))
    nxt = relabel(nxt)
    qtraj.append(len(set(nxt.values())))
    stable = (len(set(nxt.values())) == len(set(QPART.values())))
    QPART = nxt
    if stable: break
check("CG3c the EXACT bisimulation quotient of the closed 36-state "
      "chain (P_0 = menu shape, refined by exact successor-class "
      "weight vectors AGGREGATED PER CLASS to stability — round-1 "
      "F2 correction: this is NOT the committed partition's "
      "operator, which refines by PER-CANDIDATE (weight, successor-"
      "class) multisets; the committed operator is gated separately "
      "in CG3f and lands identical blocks): trajectory 4-5-6-6, "
      "SIX classes",
      qtraj == [4, 5, 6, 6] and len(set(QPART.values())) == 6,
      f"trajectory = {qtraj}")

def blocks(assign):
    b = defaultdict(set)
    for k, v in assign.items():
        b[v].add(k)
    return frozenset(frozenset(x) for x in b.values())
q_on_cache = {tuple(h): QPART[SIG[tuple(h)]]
              for h in FAM if len(h) <= 4}
cls_on_cache = {tuple(h): CLS[tuple(h)] for h in FAM if len(h) <= 4}
check("CG3d the induced partition on the cached histories EQUALS "
      "the committed intrinsic partition BLOCKWISE (len<=4, all "
      "1,191 histories): quotient-of-sigma blocks == the committed "
      "six blocks",
      blocks(q_on_cache) == blocks(cls_on_cache),
      f"blockwise equal = "
      f"{blocks(q_on_cache) == blocks(cls_on_cache)}")

Q2C = {}
for h in FAM:
    if len(h) > 4: continue
    Q2C.setdefault(QPART[SIG[tuple(h)]], set()).add(CLS[tuple(h)])
Q2C = {k: next(iter(v)) for k, v in Q2C.items()}
TQ = {}
tq_ok = True
for s in REP:
    c = Q2C[QPART[s]]
    row = defaultdict(Fr)
    for s2, q in WROW[s].items():
        row[Q2C[QPART[s2]]] += q
    row = dict(row)
    if c in TQ:
        tq_ok &= (TQ[c] == row)
    else:
        TQ[c] = row
check("CG3e the INDUCED TRANSFER equals T_REF: quotient-class "
      "successor rows are constant across all 36 abstract states "
      "(the bisimulation property, re-gated at abstract level) and "
      "equal the committed matrix entrywise in Fractions",
      tq_ok and TQ == T_REF,
      f"abstract rows well-defined = {tq_ok}; TQ == T_REF = "
      f"{TQ == T_REF}")

# round-1 F2: the COMMITTED per-candidate refinement operator, run
# on the same 36-state chain (the d43b operator ported in §B refines
# by the multiset of (weight, successor-class) PER CANDIDATE, not by
# per-class aggregates; the theorem needs THIS operator's fixed
# point).
PC = relabel(shape36)
pctraj = [len(set(PC.values()))]
while True:
    nxt = {}
    for s, r in REP.items():
        succ = tuple(sorted((str(q), PC[canon_sigma(r + (e,))])
                            for e, q in cands_of(r)))
        nxt[s] = (PC[s], succ)
    nxt = relabel(nxt)
    pctraj.append(len(set(nxt.values())))
    pc_stable = (len(set(nxt.values())) == len(set(PC.values())))
    PC = nxt
    if pc_stable: break
check("CG3f [round-1 F2] the COMMITTED PER-CANDIDATE operator on "
      "the abstract chain: refining the 36 states by per-candidate "
      "(weight, successor-class) MULTISETS — the actual operator of "
      "the committed intrinsic partition (d43b port, §B), finer-or-"
      "equal per step than CG3c's aggregation — has trajectory "
      "4-5-6-6 and lands on blocks IDENTICAL to CG3c's QPART: the "
      "two operators' fixed points coincide on this chain, closing "
      "the operator-identification gap",
      pctraj == [4, 5, 6, 6] and len(set(PC.values())) == 6
      and blocks(PC) == blocks(QPART),
      f"trajectory = {pctraj}; blocks == QPART = "
      f"{blocks(PC) == blocks(QPART)}")

# ===== SECTION D2 — CG7: the depth-7 out-of-sample extension ========
# Round-1 F1, route R2: the enumeration extended ONE LEVEL past the
# committed cache (every child of every depth-6 history), and every
# load-bearing gate re-run there. The committed depth-6 gates above
# are untouched; this block is strictly additional evidence that the
# closure holds OUT-OF-SAMPLE — it does not discharge the all-depth
# quantifier (the structural lemma remains the named residual).
D7 = []
for h in FAM:
    if len(h) != 6: continue
    hk = tuple(h)
    for e, q in CACHE[hk]:
        D7.append(hk + (e,))
n_d6 = sum(1 for h in FAM if len(h) == 6)
SIG7 = {}
d7_new_states = set()
for hk in D7:
    s7 = canon_sigma(hk)
    SIG7[hk] = s7
    if s7 not in REP:
        d7_new_states.add(s7)
check("CG7a DEPTH-7 CLOSURE, out-of-sample: all 145,408 depth-7 "
      "histories (children of the 27,904 depth-6 cache members — "
      "the referee-sweep census, re-anchored) have sigma INSIDE the "
      "closed 36 — ZERO new sigma-states one full level beyond the "
      "committed cache",
      len(D7) == 145408 and n_d6 == 27904
      and len(SIG7) == 145408 and not d7_new_states,
      f"depth-7 histories = {len(D7)}; depth-6 parents = {n_d6}; "
      f"new sigma-states = {len(d7_new_states)}")

cg7_menu_bad = 0
for hk in D7:
    if canon_menu(hk) != CLASS_MENU[SIG7[hk]]:
        cg7_menu_bad += 1
check("CG7b MENU FACTORIZATION AT DEPTH 7 (CG1 extended): every "
      "depth-7 canonical menu equals its sigma-class's canonical "
      "menu from the depth-6 pass — 145,408 menus, ZERO exceptions "
      "(the own-view-lag subtlety holds one level out-of-sample)",
      cg7_menu_bad == 0,
      f"violations = {cg7_menu_bad}")

NEW_T = {}
cg7_tr_bad = 0
n_tr7 = 0
for hk in D7:
    h6, e = hk[:-1], hk[-1]
    n_tr7 += 1
    key = canon_pair(h6, e)
    tgt = SIG7[hk]
    if key in TRANS:
        if TRANS[key] != tgt: cg7_tr_bad += 1
    elif key in NEW_T:
        if NEW_T[key] != tgt: cg7_tr_bad += 1
    else:
        NEW_T[key] = tgt
check("CG7c TRANSITION DETERMINISM AT 6->7 (CG2 extended): all "
      "145,408 depth-6->7 transitions are deterministic in "
      "(sigma, e-up-to-renaming); 16 NEW abstract keys appear "
      "beyond the cached 160 (176 total — the committed CG2 did "
      "NOT cover this level; the referee count, re-anchored), each "
      "consistent across all its instances, and ZERO mismatches "
      "against the cached keys",
      n_tr7 == 145408 and cg7_tr_bad == 0
      and len(NEW_T) == 16 and len(TRANS) + len(NEW_T) == 176,
      f"transitions = {n_tr7}; violations = {cg7_tr_bad}; new keys "
      f"= {len(NEW_T)}; total keys = {len(TRANS) + len(NEW_T)}")

wit_count = defaultdict(int)
for h in FAM:
    wit_count[SIG[tuple(h)]] += 1
for hk in D7:
    wit_count[SIG7[hk]] += 1
min_wit = min(wit_count.values())
check("CG7d WITNESS MULTIPLICITY: on the extended (depth <= 7) "
      "family every one of the 36 sigma-states has at least TWO "
      "realizing witnesses — no state (in particular none of the "
      "four minlen-6 states) rests on a single history",
      len(wit_count) == 36 and min_wit >= 2,
      f"states = {len(wit_count)}; min witnesses = {min_wit}")

row7_bad = 0
len6_states = set()
for h in FAM:
    if len(h) != 6: continue
    hk = tuple(h)
    s6 = SIG[hk]
    len6_states.add(s6)
    row = defaultdict(Fr)
    for e, q in CACHE[hk]:
        row[SIG7[hk + (e,)]] += q
    if dict(row) != WROW[s6]: row7_bad += 1
check("CG7e SIGMA-ROW CONSTANCY (CG3d-class), ALL 36 STATES: every "
      "one of the 27,904 depth-6 histories has an outgoing sigma-"
      "row EQUAL to its state's representative row WROW, and the "
      "len-6 instances cover ALL 36 states — the single-witness "
      "rows of the four minlen-6 states are closed by their full "
      "depth-7 instance sets",
      row7_bad == 0 and len6_states == set(REP),
      f"row violations = {row7_bad}; states covered = "
      f"{len(len6_states)}")

# ==== SECTION E — CG4: the reduction mechanism (exhibit) ============
# Round-1 F5: CG4a/CG4b are INDEPENDENT STRUCTURAL EXHIBITS — the
# reduction mechanism's validity and the A2 obstruction — NOT part
# of the delivered assembly route (the pin's pumping route was
# superseded by the quotient route, §6 A1/A2). Only CG4c's window
# realization enters the delivered proof.
def unsub_v(x, b):
    """MG6's substitution, inverted: the renewal base b (a version
    name) is replaced by the genesis base V0, recursively through
    nested version names."""
    if x == b: return V0
    if isinstance(x, tuple) and len(x) == 5 and x[0] == 'v':
        return ('v', unsub_v(x[1], b), x[2], x[3], x[4])
    return x

def unsub_e(e, b):
    if e[0] == 'p':
        return ('p', e[1], unsub_v(e[2], b), e[3])
    if e[0] == 'r':
        return ('r', e[1],
                frozenset((t[0], unsub_v(t[1], b), t[2])
                          for t in e[2]),
                frozenset((t[0], unsub_v(t[1], b), t[2])
                          for t in e[3]))
    return e

def shared_base(hk):
    h = list(hk)
    pred = event_poset(h)
    fv = View(h, pred, set(range(len(h))))
    return (fv.holdings('A') & fv.holdings('B')) - fv.superseded

RED_FAILS = []
def red(hk):
    """(i) pad deletion; (ii) renewal truncation: whenever a proper
    prefix is a clean slate (sigma == sigma([]); at such points the
    shared non-superseded base is UNIQUE — the MG6 census property,
    re-gated here on every reduction path), cut the prefix and
    substitute the renewal base back to genesis. Each step is gated
    sigma-preserving."""
    g = tuple(e for e in hk if e[0] != 'n')
    if canon_sigma(g) != canon_sigma(hk):
        RED_FAILS.append(('pad', hk)); return g
    while True:
        done = True
        for k in range(len(g), 0, -1):
            if canon_sigma(g[:k]) == SROOT:
                sh = shared_base(g[:k])
                if len(sh) != 1:
                    RED_FAILS.append(('shared', hk, k)); return g
                b = next(iter(sh))
                g2 = tuple(unsub_e(e, b) for e in g[k:])
                if canon_sigma(g2) != canon_sigma(g):
                    RED_FAILS.append(('sub', hk, k)); return g
                g = g2; done = False; break
        if done: return g

REDMEMO = {}
lens_spec = defaultdict(int)
red_ok_sig = red_ok_idem = red_ok_form = True
for h in FAM:
    hk = tuple(h)
    r = red(hk)
    REDMEMO[hk] = r
    lens_spec[len(r)] += 1
    if canon_sigma(r) != SIG[hk]: red_ok_sig = False
    if red(r) != r: red_ok_idem = False
    if any(e[0] == 'n' for e in r): red_ok_form = False
    if any(canon_sigma(r[:k]) == SROOT for k in range(1, len(r))):
        red_ok_form = False
check("CG4a [MECHANISM EXHIBIT — off the assembly route, round-1 "
      "F5] the REDUCTION IS VALID on all 34,375 cached histories: "
      "zero mechanism failures (every clean-slate prefix had a "
      "unique shared non-superseded base; every substitution step "
      "verified sigma-preserving — NC3's identity and MG6's "
      "substitution re-gated on the reduction path); the "
      "representative has the SAME sigma, is noop-free, has no "
      "clean-slate proper prefix left, and the map is idempotent",
      not RED_FAILS and red_ok_sig and red_ok_idem and red_ok_form,
      f"mechanism failures = {len(RED_FAILS)}; sigma preserved = "
      f"{red_ok_sig}; idempotent = {red_ok_idem}; normal form = "
      f"{red_ok_form}")

minlen = {}
for h in FAM:
    s = SIG[tuple(h)]
    minlen[s] = min(minlen.get(s, 99), len(h))
mls = defaultdict(int)
for v in minlen.values():
    mls[v] += 1
SELFB = ('r', 'B', frozenset({tB}), frozenset({tB}))
vB1 = vname(V0, frozenset({tB}), 'B')
WIT4 = (pB1, SELFB, ('p', 'B', vB1, 1), pA0)
n_le3 = sum(v for k, v in lens_spec.items() if k <= 3)
n_gap = sum(1 for h in FAM
            if minlen[SIG[tuple(h)]] <= 3
            and len(REDMEMO[tuple(h)]) > 3)
check("CG4b [MECHANISM EXHIBIT — off the assembly route, round-1 "
      "F5] the PINNED <=3 CLAUSE IS FALSE, exhibited (deviation "
      "A2): the reduced-length spectrum is {0: 3727, 1: 5828, "
      "2: 6708, 3: 7200, 4: 6816, 5: 3328, 6: 768} — 23,463 of "
      "34,375 reach length <= 3, maximum 6 ON THE CACHE (a cache "
      "artifact, NOT a normal-form bound: over the unbounded family "
      "the reduction has unbounded image, since the diverged sector "
      "admits no clean-slate truncation points at d42a scope — "
      "which is exactly why the pumping route cannot power the "
      "all-depth step); SEVENTEEN of the 36 "
      "sigma-states have NO realization below length 4 (shortest-"
      "realization census {0:1, 1:4, 2:6, 3:8, 4:9, 5:4, 6:4}); "
      "the gated witness [pB1, selfB, pB(v1,1), pA0] is length-4, "
      "noop-free, renewal-free (no clean-slate prefix: the diverged "
      "sector has none at d42a scope — no deliveries), and equals "
      "its own reduction; 1,832 further histories sit in "
      "<=3-realizable states yet cannot be carried there by pad+"
      "renewal moves alone (the reduction cannot cross divergence)",
      dict(lens_spec) == {0: 3727, 1: 5828, 2: 6708, 3: 7200,
                          4: 6816, 5: 3328, 6: 768}
      and dict(mls) == {0: 1, 1: 4, 2: 6, 3: 8, 4: 9, 5: 4, 6: 4}
      and sum(1 for v in minlen.values() if v > 3) == 17
      and n_le3 == 23463
      and REDMEMO[WIT4] == WIT4 and len(WIT4) == 4
      and minlen[SIG[WIT4]] == 4
      and n_gap == 1832,
      f"spectrum = {dict(sorted(lens_spec.items()))}; minlen census "
      f"= {dict(sorted(mls.items()))}; witness irreducible = "
      f"{REDMEMO[WIT4] == WIT4}; gap histories = {n_gap}")

cls_le3 = {CLS[tuple(h)] for h in FAM if len(h) <= 3}
qc_all = {Q2C[QPART[s]] for s in REP}
check("CG4c the WINDOW REALIZATION the pin-4 proof sketch needs, "
      "at quotient level: every one of the 36 sigma-states "
      "projects to an intrinsic class realized at length <= 3 "
      "(all six classes are — the T_REF window), so every cached "
      "history's class is realized on the committed window; with "
      "CG4a's sigma-preserving reduction this is the pumping "
      "content that survives A2",
      cls_le3 == set(range(6)) and qc_all <= cls_le3,
      f"classes realized at len<=3 = {sorted(cls_le3)}; "
      f"quotient classes of the closure = {sorted(qc_all)}")

# ==== SECTION F — CG5: the Perron package on the induced chain ======
# The committed exact algebra (d43b MG3a-MG5), re-run against the
# CG3-induced transfer TQ (not against a re-typed matrix).
T = [[TQ[i].get(j, Fr(0)) for j in range(6)] for i in range(6)]
DOM, TRA = [2, 4, 5], [0, 1, 3]
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
check("CG5a the class structure of the induced transfer: two "
      "nontrivial Tarjan classes — transient {0,1,3} (with the "
      "renewal loop 3 -> 0) and closed dominant {2,4,5}",
      nontrivial == [TRA, DOM]
      and all(T[i][j] == 0 for i in DOM for j in range(6)
              if j not in DOM)
      and any(T[i][j] != 0 for i in TRA for j in DOM),
      f"nontrivial = {nontrivial}")

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
check("CG5b lambda = 2 EXACT on the induced chain: the dominant-"
      "block characteristic polynomial vanishes at 2 (Faddeev-"
      "LeVerrier, Fractions) AND T f = 2 f holds exactly with the "
      "positive f = (4/3, 4/3, 1, 7/3, 1, 1)",
      peval(charpoly(Md), LAM) == 0
      and all(sum(T[i][j] * f[j] for j in range(6)) == LAM * f[i]
              for i in range(6))
      and all(x > 0 for x in f),
      f"charpoly_dom(2) = {peval(charpoly(Md), LAM)}")

aug = [[(Fr(2) if i == j else Fr(0)) - Mt[i][j] for j in range(3)]
       + [Fr(1) if i == j else Fr(0) for j in range(3)]
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
            aug[r2] = [a - fac * b2
                       for a, b2 in zip(aug[r2], aug[col])]
inv = [] if sing else [r2[3:] for r2 in aug]
RES_REF = [[Fr(8, 3), Fr(8, 3), Fr(2, 3)],
           [Fr(2, 3), Fr(8, 3), Fr(2, 3)],
           [Fr(8, 3), Fr(8, 3), Fr(8, 3)]]
b = [sum(T[i][j] * f[j] for j in DOM) for i in TRA]
ext = ([sum(inv[i][j] * b[j] for j in range(3)) for i in range(3)]
       if not sing else [])
check("CG5c dominant-class UNIQUENESS + the forced extension: "
      "det(2I - M_transient) = 3/32; the resolvent equals the "
      "anchored nonnegative matrix ((8/3, 8/3, 2/3), (2/3, 8/3, "
      "2/3), (8/3, 8/3, 8/3)) [M-matrix certificate: transient "
      "radius < 2]; applied to the cross-flow it returns EXACTLY "
      "(4/3, 4/3, 7/3) — existence AND uniqueness up to scale",
      (not sing) and det == Fr(3, 32) and inv == RES_REF
      and ext == [Fr(4, 3), Fr(4, 3), Fr(7, 3)],
      f"det = {det}; resolvent == anchor = {inv == RES_REF}; "
      f"extension = {[str(x) for x in ext]}")

qp = [[T[i][j] * f[j] / (LAM * f[i]) for j in range(6)]
      for i in range(6)]
conf = {j: qp[3][j] for j in range(6) if qp[3][j] != 0}
check("CG5d the completed transfer q'(i->j) = T_ij f_j / (2 f_i) "
      "is per-state normalized EXACTLY on all six rows; conflict-"
      "row anchor {0: 1/7, 3: 3/4, 5: 3/28}; and ROOT-CLASS == "
      "RENEWAL-CLASS IN SIGMA-SPACE: sigma(H3) == sigma([]) at the "
      "fine level (one abstract state, not merely one quotient "
      "class), projecting to intrinsic class 0",
      all(sum(qp[i]) == 1 for i in range(6))
      and conf == {0: Fr(1, 7), 3: Fr(3, 4), 5: Fr(3, 28)}
      and canon_sigma(H3) == SROOT and Q2C[QPART[SROOT]] == 0,
      f"row sums exact = {all(sum(qp[i]) == 1 for i in range(6))}; "
      f"conflict row = { {k: str(v) for k, v in sorted(conf.items())} }; "
      f"sigma(H3) == sigma([]) = {canon_sigma(H3) == SROOT}")

pi = {2: Fr(1, 4), 4: Fr(1, 4), 5: Fr(1, 2)}
check("CG5e the MASS-TRANSPORT identity EXACT on the induced "
      "chain: pi = (1/4, 1/4, 1/2) on {2,4,5} satisfies pi T = "
      "2 pi exactly and the pi.f-weighted law is invariant under "
      "the completed q' exactly — no residual, no tolerance",
      all(sum(pi[i] * T[i][j] for i in DOM) == LAM * pi[j]
          for j in DOM)
      and all(sum(pi[i] * f[i] * qp[i][j] for i in DOM)
              == pi[j] * f[j] for j in DOM),
      "pi T == 2 pi and exact stationarity both hold")

# ============= SECTION G — CG6: the negative controls ===============
def sigma_a(hk):
    """Variant (a): sigma PLUS menu-invisible dead structure — the
    count of ALL superseded bases (the simplest dead-history
    statistic; every renewal cycle increments it)."""
    h = list(hk)
    pred = event_poset(h)
    fv = View(h, pred, set(range(len(h))))
    return (canon_sigma(hk), len(fv.superseded))

va = {sigma_a(tuple(h)) for h in FAM}
repa = {sigma_a(()): ()}
qa = [sigma_a(())]
a_closed = True
while qa:
    s = qa.pop(0)
    hk = repa[s]
    for e, q in cands_of(hk):
        s2 = sigma_a(hk + (e,))
        if s2 not in repa:
            repa[s2] = hk + (e,)
            qa.append(s2)
    if len(repa) > 200:
        a_closed = False
        break
check("CG6a KEEPING MENU-INVISIBLE DEAD STRUCTURE BLOWS UP THE "
      "BFS (the abstraction is not trivially finite-valued): the "
      "dead-keeping variant already takes 67 > 36 values on the "
      "cache alone, and its BFS is STILL OPEN at 201 states under "
      "a 200-state budget — CUT AT BUDGET, not tuned (round-1 N2: "
      "the referee verified non-closure at this budget; each "
      "renewal pumps the dead count — unbounded growth), while the "
      "delivered sigma closes at 36 with the frontier exhausted",
      len(va) == 67 and len(repa) == 201 and not a_closed
      and len(REP) == 36,
      f"cache values = {len(va)}; budget states = {len(repa)}; "
      f"closed = {a_closed}")

def sigma_b(hk):
    """Variant (b): the conflict-edge/component structure dropped —
    live proposals recorded as (proposer, base) only. At d42a scope
    the edges are generated by the payloads (co-based opposite-
    payload live pairs are always incomparable — SG2), so dropping
    the edge structure means dropping the component data with the
    payload distinction that generates it."""
    hold, live, comps, refs, sup = sigma_raw(hk)
    best = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        s = repr((tuple((a, m.get(hold[a])) for a in AB),
                  tuple(sorted(((t[0], m[t[1]]) for t in live),
                               key=repr)),
                  tuple(sorted((m[b], b in sup) for b in refs))))
        if best is None or s < best: best = s
    return best

WB1, WB2 = (pA0, pB0), (pA0, pB1)
NB1 = sum(q for e, q in CACHE[WB1])
NB2 = sum(q for e, q in CACHE[WB2])
check("CG6b DROPPING THE CONFLICT-EDGE STRUCTURE FAILS CG1, "
      "splitting pair exhibited: sigma_b([pA0,pB0]) == "
      "sigma_b([pA0,pB1]) yet their canonical menus differ — the "
      "parallel pair offers two self-arbs only (N = 2) while the "
      "conflict pair adds the four joint arbitrations (N = 5/2); "
      "they are not even intrinsically co-classed (classes 2 vs 3)",
      sigma_b(WB1) == sigma_b(WB2)
      and canon_menu(WB1) != canon_menu(WB2)
      and CLS[WB1] == 2 and CLS[WB2] == 3
      and NB1 == Fr(2) and NB2 == Fr(5, 2),
      f"sigma_b equal = {sigma_b(WB1) == sigma_b(WB2)}; menus "
      f"equal = {canon_menu(WB1) == canon_menu(WB2)}; N = "
      f"{NB1}, {NB2}")

print("  [CG6c] the depth-marked stratification stands as the "
      "committed negative control: d43b NC1/NC4 — the boundary-"
      "marked truncation quotient grows 17/23/29 by horizon "
      "stratification and heals onto the six intrinsic classes "
      "(cited, not rerun).")

# ========================== VERDICT =================================
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — gate breakage; exit 1 by design")
    sys.exit(1)
print("[VERDICT] d44a GREEN — THE CLOSURE THEOREM at d42a scope, "
      "decided at EVERY VERIFIED DEPTH: the pin-2 local-state "
      "abstraction sigma (holdings pattern + live-proposal/conflict "
      "structure + carried superseded marks, modulo base renaming) "
      "determines menus exactly (CG1: 34,375/0 on the cache; CG7b: "
      "145,408/0 at depth 7) and transitions exactly (CG2: "
      "34,374/0, 160 keys; CG7c: 145,408/0 at 6->7, 176 keys "
      "total), and its depth-free BFS CLOSES at 36 states with the "
      "frontier exhausted (CG3a), realized precisely by the depth-6 "
      "cache with ZERO new sigma-states at depth 7 (CG7a). The "
      "pinned six-state landing is impossible for ANY menu-exact "
      "sigma (CG3b's witness: bisimilarity merges menu-distinct "
      "states), and the repaired route lands the decision: the "
      "EXACT bisimulation quotient of the closed chain has SIX "
      "classes under BOTH the aggregated operator (CG3c) and the "
      "COMMITTED per-candidate operator (CG3f — identical blocks), "
      "blockwise equal to the committed intrinsic partition with "
      "transfer T_REF (CG3d-e), and the entire Perron package holds "
      "there: lambda = 2 exact, unique dominant class {2,4,5} (det "
      "3/32, anchored nonnegative resolvent), f = (4,4,3,7,3,3)/3 "
      "with forced extension, root = renewal AS ONE SIGMA-STATE, "
      "pi = (1,1,2)/4 mass transport exact (CG5). THE QUANTIFIER, "
      "honestly (round-1 F1, route R2): residue 1 is decided at "
      "EVERY VERIFIED DEPTH (exhaustive through depth 7 "
      "in-receipt); the depth-free structural lemma (menu "
      "factorization from sigma at all depths — nontrivial because "
      "admissibility runs on own views that lag the full view) is "
      "the NAMED RESIDUAL. IF the lemma holds, CG1/CG2 become "
      "depth-free laws and the pullback argument delivers the "
      "six-state chain, transfer T, and the full Perron package at "
      "ALL depths — stated as the conditional it is. The reduction "
      "machinery is the mechanism exhibit, off the delivered "
      "assembly route (CG4a/b, deviation A2 + round-1 F5); only "
      "CG4c's window realization enters the proof. Controls: "
      "dead-keeping sigma stays open at a 200-state budget (cut at "
      "budget, not tuned), edge-dropping sigma fails CG1 on the "
      "exhibited pair, and the stratification control is cited "
      "(CG6). Residue 1's decided-on-the-window reading UPGRADES "
      "to decided at every verified depth at d42a scope; transport "
      "(deliveries reopening the absorbing sector) remains D44b's "
      "problem.")
