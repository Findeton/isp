#!/usr/bin/env python3
"""
d46a_h1_lemma_exact.py — v10 D46a: the H1 structural lemma, route
R-A (own-view determination). Pin: note-d46a-h1-structural-lemma.md
(strict). Parents: D44a TERMINAL #368 (the closure theorem,
all-depth CONDITIONAL on H1; note-d44a §7-§8); D44b TERMINAL #374
(scope boundary: DELIVERY-FREE d42a scope only). The d42a admission
layer is exec'd from the committed d42b3 receipt (__file__-anchored,
the d43b/d44a pattern); the sigma construction is the d44a port,
verbatim.

THE DELIVERED OBJECT: per-actor own-view abstractions tau_A, tau_B —
the sigma construction applied to actor a's MENU-VIEW sub-history
(the union of the past cone of a's next-event vantage ('n', a),
which is also the cone the layer builds for every p-candidate, and
the past cones of a's admissible r-candidates — exactly the views
prop_options_in_view and arb_components_in_view actually run on;
the union is downward-closed, hence itself a committed-layer
history) — and the JOINT (sigma, tau_A, tau_B) transition system:
its BFS CLOSES at 36 joint states with the frontier exhausted, and
the projection onto sigma is INJECTIVE — tau_A and tau_B are
CONSTANT on sigma within the closed system. THIS IS THE MECHANICAL
CORE OF H1: the own-view lag (the D44a W2 witness) is
sigma-INVISIBLE at the abstraction level, and the per-actor menu is
gated a FUNCTION of tau_a on the entire depth-7 family (LG2, zero
exceptions; the structural claim made mechanical: the layer's
per-actor menu recomputed from the menu-view sub-history ALONE
equals the full computation, 436,316 comparisons, zero exceptions).
The R-B counterexample horn did NOT fire; had it fired, the pair
would be the delivered object at exit 0 (pin §3-§4 discipline).

H2'S STATUS (LG3, DECLARED): the joint transition is deterministic
keyed by (sigma, renamed e) ALONE (160 cache keys + 16 depth-6->7
keys = 176, zero conflicts) — so on the closed system H2 needs no
separate closure: sigma-injectivity makes the joint BFS and the
sigma BFS the SAME 36-state/176-edge object, and H2 is subsumed by
the same joint-closure conditional that powers LG1.

WHAT REMAINS FOR THE PIN-§5 PROOF NOTE (the author writes it; the
receipt only gates the mechanical parts): (i) cone-locality as a
THEOREM — the committed admissible() builds its View from the
candidate's past cone only, so a downward-closed sub-history
containing that cone reproduces the candidate and its weight
verbatim (LG2a is this claim's exhaustive depth-7 census); (ii) the
abstract-update law — joint-transition determinism at ALL depths
(LG1a/LG3 verify it exhaustively through depth 7; the note must
argue the sigma/tau raw-data update under one event is a function
of the abstract state and the renamed event). Given (i)+(ii), the
closed injective joint system delivers H1 and H2 at every depth and
the D44a §8 assembly closes residue 1 outright at d42a scope.

Banner: EXACT Fractions; deterministic (every canonical form is a
post-renaming-sorted plain-tuple serialization; witness prints go
through a sorted event printer — no raw frozenset reprs); exit 1 on
gate failure only; delivered outcomes exit 0.

GREEN-UNREVIEWED — the hostile round is deferred per the D46
program pin (token budget); this receipt must not be cited as
review-hardened until its round converts (paper-32's round precedes
it).
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

print("[d46a — the H1 structural lemma: route R-A]")
print("  banner: GREEN-UNREVIEWED — the hostile round is deferred")
print("  per the D46 program pin (token budget); this receipt must")
print("  not be cited as review-hardened until its round converts")
print("  (paper-32's round precedes it).")
print("  EXACT; d42a layer from the committed d42b3 receipt")
print("  (__file__-anchored); sigma = the committed d44a")
print("  construction, ported verbatim; tau_a = sigma applied to")
print("  a's menu-view sub-history (defined at [DEF] below); LG1 =")
print("  the joint (sigma, tau_A, tau_B) BFS closure + the")
print("  injectivity verdict (H1's mechanical core); LG2 = menu")
print("  factorization through tau on the full depth-7 family +")
print("  the own-view recomputation gate; LG3 = H2's status,")
print("  declared; LG4 = negative controls; LG5 = allow-list")
print("  purity walk (#362 form). Delivered-outcome discipline:")
print("  an R-B counterexample (non-injective projection) would be")
print("  a RESULT at exit 0, not a failure; exit 1 is reserved for")
print("  gate breakage.")

# ---- LG0: the enumeration + the D44a anchors, re-anchored ----------
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
check("LG0a the enumeration anchor: cumulative depth-0..6 family "
      "sizes equal the referee-verified census (the D44a SG0 "
      "re-anchor); the depth-7 extension (27,904 parents, 145,408 "
      "children, 179,783 total histories) is re-anchored in the "
      "depth-7 section below (LG1d)",
      cum == [1, 7, 39, 215, 1191, 6471, 34375],
      f"sizes = {cum}")

def cands_of(hk):
    if hk not in CACHE: CACHE[hk] = candidates_for(list(hk), AB)
    return CACHE[hk]

# ---- sigma: the committed d44a local-state abstraction, verbatim ---
SG_VIOL = {'alive': 0, 'nonsup': 0, 'liveX': 0, 'cmp': 0}

def own_alive(h, a):
    """a's own-view alive holdings: the committed View on a's chain
    past (the d42b3 own-view pattern: append a noop, take its
    past-cone). The d42a invariant (gated in LG0c): a SINGLETON."""
    acts2 = list(h) + [('n', a)]
    pred = event_poset(acts2)
    vw = View(acts2, pred, pred[len(acts2) - 1])
    alive = {b for b in vw.holdings(a) if b not in vw.superseded}
    if len(alive) != 1:
        SG_VIOL['alive'] += 1
    return sorted(alive, key=repr)[0]

RAWMEMO = {}
def sigma_raw(hk):
    """The d44a pin-2 data, raw base names as placeholders (hold /
    live / comps / refs / sup) — the committed construction."""
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
check("LG0b sigma re-anchored on the entire cache: 36 distinct "
      "values, distinct-value growth over the len<=2/3/4/5/6 "
      "windows = the D44a SG1 anchor [11, 19, 28, 32, 36]",
      NSIG == 36 and wins == [11, 19, 28, 32, 36],
      f"windows = {wins}")
check("LG0c the d42a view invariants sigma and tau rely on (the "
      "D44a SG2 gate re-run family-wide, 34,375 histories): "
      "own-view alive holding a SINGLETON; full-view non-superseded "
      "holdings inside it; live proposals on the proposer's "
      "own-view base; conflicting live pairs poset-incomparable",
      all(v == 0 for v in SG_VIOL.values()),
      f"violations = {SG_VIOL}")

# ---- [DEF] tau_a: the sigma construction on a's menu-view ----------
print("  [DEF] tau_a(h) = canon_sigma of a's MENU-VIEW sub-history:")
print("  the union of (i) the past cone of a's next-event vantage")
print("  ('n', a) — the exact view admissible() builds for a's n-")
print("  and p-candidates (regs {a}: both cones coincide), on which")
print("  prop_options_in_view and the noop's arb_components_in_view")
print("  run — and (ii) the past cones of a's ADMISSIBLE r-")
print("  candidates — the exact views arb_components_in_view runs")
print("  on for arbitration (the r-event's registers span the co-")
print("  proposers' chains, so these cones carry the join-visible")
print("  opponent past). The union of past cones is downward-")
print("  closed; the committed layer is cone-local, so the sub-")
print("  history (original order) is itself a layer history and")
print("  every menu input of actor a is computed inside it. tau is")
print("  the SAME canonical base renaming as sigma (LG0b's port).")

MVMEMO = {}
def sub_of(hk, a):
    """a's menu-view sub-history at h (index-ordered)."""
    if (hk, a) in MVMEMO: return MVMEMO[(hk, a)]
    h = list(hk)
    acts2 = h + [('n', a)]
    pred = event_poset(acts2)
    idxs = set(pred[len(acts2) - 1])
    for e, q in cands_of(hk):
        if e[1] == a and e[0] == 'r':
            acts3 = h + [e]
            pred3 = event_poset(acts3)
            idxs |= set(pred3[len(acts3) - 1])
    sub = tuple(h[i] for i in sorted(idxs))
    MVMEMO[(hk, a)] = sub
    return sub

def tau(hk, a):
    return canon_sigma(sub_of(hk, a))

TAU = {}
for h in FAM:
    hk = tuple(h)
    TAU[hk] = (tau(hk, 'A'), tau(hk, 'B'))
n_subs = len(set(MVMEMO.values()))
n_tauA = len({TAU[tuple(h)][0] for h in FAM})
n_tauB = len({TAU[tuple(h)][1] for h in FAM})
check("TG1 tau computed on the ENTIRE cache: 10,169 distinct "
      "menu-view sub-histories across 34,375 histories x 2 actors, "
      "and tau takes exactly EIGHT values per actor — the own-view "
      "abstraction is radically coarser than sigma (36) yet menus "
      "factor through it per-actor (LG2)",
      len(TAU) == 34375 and n_subs == 10169
      and n_tauA == 8 and n_tauB == 8,
      f"distinct sub-histories = {n_subs}; |tau_A| = {n_tauA}; "
      f"|tau_B| = {n_tauB}")

# ---- the d44a canonical-renaming machinery (verbatim port) ---------
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
    """Bases the menu mentions beyond sigma's refs (the d44a rule:
    the canonical renaming extends over them deterministically)."""
    ex = set()
    for e, q in menu:
        if e[0] == 'p' and e[2] not in m:
            ex.add(e[2])
        elif e[0] == 'r':
            for t in tuple(e[2]) + tuple(e[3]):
                if t[1] not in m: ex.add(t[1])
    return sorted(ex, key=repr)

def canon_pair(hk, e):
    """(sigma(h), e) jointly canonical — the d44a CG2 key."""
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

def pr_e(e):
    """Deterministic event printer (sorted plain tuples; no raw
    frozenset reprs — seed-independent output)."""
    if e[0] == 'r':
        return ('r', e[1], tuple(sorted(e[2], key=repr)),
                tuple(sorted(e[3], key=repr)))
    return e

# ---- LG1a: joint-transition determinism on the cache ---------------
# The precondition that licenses the representative-based joint BFS
# (the CG2-for-the-joint-abstraction gate; same epistemic level as
# d44a's CG2 -> CG3a licensing).
def J(hk):
    return (canon_sigma(hk), tau(hk, 'A'), tau(hk, 'B'))

JT = {}
ST = {}
jt_bad = []
st_bad = []
n_tr = 0
for h in FAM:
    if len(h) >= 6: continue
    hk = tuple(h)
    jh = (SIG[hk],) + TAU[hk]
    for e, q in CACHE[hk]:
        n_tr += 1
        sb, eb = canon_pair(hk, e)
        tgt = (SIG[hk + (e,)],) + TAU[hk + (e,)]
        k1 = (jh, eb)
        if k1 in JT:
            if JT[k1] != tgt: jt_bad.append((hk, e))
        else:
            JT[k1] = tgt
        k2 = (sb, eb)
        if k2 in ST:
            if ST[k2] != tgt: st_bad.append((hk, e))
        else:
            ST[k2] = tgt
check("LG1a JOINT-TRANSITION DETERMINISM, exhaustive on the cache: "
      "the successor joint state (sigma, tau_A, tau_B)(h + [e]) is "
      "a function of (joint state of h, e-up-to-renaming) — all "
      "34,374 cached transitions, 160 distinct abstract keys "
      "(EXACTLY the D44a CG2 key count: the joint keys do not "
      "outnumber the sigma keys), ZERO exceptions — the "
      "representative-based joint BFS below is licensed at "
      "cache-verified level",
      n_tr == 34374 and len(JT) == 160 and not jt_bad,
      f"transitions = {n_tr}; joint keys = {len(JT)}; violations = "
      f"{len(jt_bad)}")

# ---- LG1b: the joint BFS closure (the depth-free step) -------------
JROOT = J(())
JREP = {JROOT: ()}
bq = [JROOT]
n_exp = 0
n_edge = 0
while bq:
    s = bq.pop(0)
    r = JREP[s]
    n_exp += 1
    for e, q in cands_of(r):
        n_edge += 1
        s2 = J(r + (e,))
        if s2 not in JREP:
            JREP[s2] = r + (e,)
            bq.append(s2)
rep_spec = defaultdict(int)
for r in JREP.values():
    rep_spec[len(r)] += 1
check("LG1b THE JOINT BFS CLOSES: BFS on (sigma, tau_A, tau_B)-"
      "space from the root joint state, one representative per "
      "state (licensed by LG1a), TERMINATES WITH THE FRONTIER "
      "EXHAUSTED — every reachable representative EXPANDED (no "
      "budget stop); the closed set has exactly 36 joint states, "
      "176 traversed edges, and the representative-length spectrum "
      "{0:1, 1:4, 2:6, 3:8, 4:9, 5:4, 6:4} — ALL identical to the "
      "D44a sigma-BFS anchors (CG3a): adjoining tau to sigma "
      "creates NO new abstract states",
      len(JREP) == 36 and n_exp == 36 and not bq
      and n_edge == 176
      and dict(rep_spec) == {0: 1, 1: 4, 2: 6, 3: 8, 4: 9, 5: 4,
                             6: 4},
      f"states = {len(JREP)}; expanded = {n_exp}; edges = "
      f"{n_edge}; rep-length spectrum = "
      f"{dict(sorted(rep_spec.items()))}")

# ---- LG1c: THE INJECTIVITY VERDICT (H1's mechanical core) ----------
sig_proj = [s[0] for s in JREP]
inj = (len(set(sig_proj)) == len(JREP))
per_sig = defaultdict(set)
for h in FAM:
    per_sig[SIG[tuple(h)]].add(TAU[tuple(h)])
n_nonconst = sum(1 for v in per_sig.values() if len(v) > 1)
jcache = {(SIG[tuple(h)],) + TAU[tuple(h)] for h in FAM}
if inj:
    check("LG1c THE PROJECTION IS INJECTIVE — H1'S MECHANICAL CORE "
          "HOLDS: within the closed joint system tau_A and tau_B "
          "are CONSTANT on sigma (the 36 joint states project onto "
          "36 distinct sigma values == the cache-realized 36); "
          "directly on the cache, all 36 sigma classes over 34,375 "
          "histories carry ONE (tau_A, tau_B) pair each, ZERO "
          "exceptions, and the cache-realized joint values are "
          "EXACTLY the closed set — the own-view lag (D44a W2) is "
          "sigma-invisible at the abstraction level: what an actor "
          "has not witnessed is FORCED by what sigma records",
          inj and set(sig_proj) == set(SIG.values())
          and len(per_sig) == 36 and n_nonconst == 0
          and jcache == set(JREP),
          f"joint states = {len(JREP)}; distinct sigma projections "
          f"= {len(set(sig_proj))}; cache sigma classes with "
          f"non-constant tau = {n_nonconst}; cache joint values == "
          f"closed set = {jcache == set(JREP)}")
else:
    # THE R-B HORN — a DELIVERED OUTCOME (exit 0 per the pin):
    coll = defaultdict(list)
    for s in JREP:
        coll[s[0]].append(s)
    pair = sorted((v for v in coll.values() if len(v) > 1),
                  key=repr)[0][:2]
    h1r, h2r = JREP[pair[0]], JREP[pair[1]]
    print("  [R-B HORN] sigma-equal, tau-different joint states:")
    print(f"    rep1 = {tuple(pr_e(e) for e in h1r)}")
    print(f"    rep2 = {tuple(pr_e(e) for e in h2r)}")
    menus_eq = (sorted((repr(pr_e(e)), str(q))
                       for e, q in cands_of(h1r))
                == sorted((repr(pr_e(e)), str(q))
                          for e, q in cands_of(h2r)))
    check("LG1c' R-B COUNTEREXAMPLE DELIVERED: the pair is exact "
          "(sigma equal, tau different); menu comparison printed — "
          "menu-different means H1 is FALSE and the D44a "
          "conditional stands; menu-equal means the lag is real "
          "but menu-invisible at joint-closure level",
          pair[0][0] == pair[1][0] and pair[0] != pair[1],
          f"raw menus equal = {menus_eq}")

# ---- LG2a: the structural claim made mechanical (cache) ------------
# The layer's per-actor menu computation consumes ONLY menu-view
# data: recompute a's menu by running the COMMITTED candidates_for
# on the menu-view sub-history ALONE and compare to the full
# computation — exact equality, raw events and exact weights
# (base names are preserved by the sub-history, so no renaming is
# involved; the comparison is seed-independent because both sides
# serialize identical values within one process).
SUBCAND = {}
def subcands(subk):
    if subk not in SUBCAND:
        SUBCAND[subk] = candidates_for(list(subk), AB)
    return SUBCAND[subk]

n_cmp = 0
struct_bad = []
for h in FAM:
    hk = tuple(h)
    for a in AB:
        sub = MVMEMO[(hk, a)]
        ma = sorted((repr(e), q) for e, q in CACHE[hk]
                    if e[1] == a)
        ms = sorted((repr(e), q) for e, q in subcands(sub)
                    if e[1] == a)
        n_cmp += 1
        if ma != ms: struct_bad.append((hk, a))
check("LG2a OWN-VIEW SUFFICIENCY, exhaustive on the cache: for "
      "every history and every actor, the committed layer run on "
      "the menu-view sub-history ALONE reproduces actor a's full "
      "menu — candidates AND exact weights, entrywise — 68,750 "
      "comparisons (34,375 x 2), ZERO exceptions: the per-actor "
      "menu computation consumes only own-view data (the "
      "structural-arm claim of pin §3 R-A, made mechanical)",
      n_cmp == 68750 and not struct_bad,
      f"comparisons = {n_cmp}; violations = {len(struct_bad)}")

# ---- LG2b: menu factorization through tau (cache) ------------------
def canon_menu_actor(subk, a):
    """Actor a's menu at the menu-view sub-history, canonicalized
    under the tau-minimizing renamings (the d44a canon_menu rule,
    restricted to a's rows)."""
    hold, live, comps, refs, sup = sigma_raw(subk)
    menu = [(e, q) for e, q in subcands(subk) if e[1] == a]
    sbest = canon_sigma(subk)
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

CMA = {}
def cma(subk, a):
    if (subk, a) not in CMA:
        CMA[(subk, a)] = canon_menu_actor(subk, a)
    return CMA[(subk, a)]

GROUP = defaultdict(set)
for h in FAM:
    hk = tuple(h)
    for i, a in enumerate(AB):
        GROUP[(a, TAU[hk][i])].add(cma(MVMEMO[(hk, a)], a))
lg2_bad = [k for k, v in sorted(GROUP.items()) if len(v) > 1]
n_cma = len(set().union(*GROUP.values()))
check("LG2b MENU FACTORIZATION THROUGH TAU, exhaustive on the "
      "cache: actor a's menu — as a renamed event-multiset with "
      "exact weights — is a FUNCTION of tau_a(h): all 16 (actor, "
      "tau) classes (8 per actor, TG1) carry ONE canonical "
      "per-actor menu each, ZERO exceptions across 34,375 "
      "histories x 2 actors; with LG1c (sigma determines tau) and "
      "LG2a this is exactly H1's factorization chain sigma -> "
      "(tau_A, tau_B) -> menus at every cached depth",
      len(GROUP) == 16 and not lg2_bad,
      f"(actor, tau) classes = {len(GROUP)}; violating classes = "
      f"{len(lg2_bad)}; distinct canonical per-actor menus = "
      f"{n_cma}")

# ---- LG3a: H2's status on the cache (sigma-keyed determinism) ------
check("LG3a SIGMA-KEYED JOINT DETERMINISM, exhaustive on the "
      "cache: the successor JOINT state is already a function of "
      "(sigma(h), e-up-to-renaming) — the SAME 160 keys as D44a's "
      "CG2, zero conflicts on all 34,374 transitions: the joint "
      "table adds no keys beyond the sigma table (the mechanical "
      "shadow of LG1c's injectivity on transitions)",
      len(ST) == 160 and not st_bad,
      f"sigma-keyed keys = {len(ST)}; violations = {len(st_bad)}")
print("  [LG3 DECLARATION] H2's status, determined: H2 (sigma-"
      "transition determinism at all depths) needs NO separate "
      "closure argument at d42a scope. On the closed system LG1c "
      "makes tau a function of sigma, so the joint transition "
      "system and the sigma transition system are THE SAME "
      "36-state/176-edge object (LG1b == D44a CG3a anchors), and "
      "LG3a/LG3b show the transition table is sigma-keyed with "
      "zero conflicts at every verified depth. H2 is subsumed by "
      "the same joint-closure conditional that powers LG1: the "
      "pin-§5 note discharges H1 and H2 from ONE abstract-update "
      "law (docstring item ii), not two.")

# ---- LG1d/LG2c/LG3b: the depth-7 out-of-sample extension -----------
# One full level past the committed cache (the D44a round-1 F1/R2
# pattern): every child of every depth-6 history, all gates re-run.
D7 = []
for h in FAM:
    if len(h) != 6: continue
    hk = tuple(h)
    for e, q in CACHE[hk]:
        D7.append(hk + (e,))
n_d6 = sum(1 for h in FAM if len(h) == 6)
J7 = {}
d7_new = []
for hk in D7:
    j7 = J(hk)
    J7[hk] = j7
    if j7 not in JREP:
        d7_new.append(hk)
check("LG1d DEPTH-7 JOINT CLOSURE, out-of-sample: all 145,408 "
      "depth-7 histories (children of the 27,904 depth-6 members; "
      "179,783 total histories — the LG0a citation re-anchored) "
      "have their JOINT state (sigma, tau_A, tau_B) INSIDE the "
      "closed 36 — ZERO new joint states one full level beyond the "
      "cache: closure AND injectivity both hold out-of-sample",
      len(D7) == 145408 and n_d6 == 27904
      and 34375 + len(D7) == 179783 and not d7_new,
      f"depth-7 histories = {len(D7)}; parents = {n_d6}; new joint "
      f"states = {len(d7_new)}")

n_cmp7 = 0
struct_bad7 = []
G7 = defaultdict(set)
for hk in D7:
    for i, a in enumerate(AB):
        sub = sub_of(hk, a)
        ma = sorted((repr(e), q) for e, q in CACHE[hk]
                    if e[1] == a)
        ms = sorted((repr(e), q) for e, q in subcands(sub)
                    if e[1] == a)
        n_cmp7 += 1
        if ma != ms: struct_bad7.append((hk, a))
        G7[(a, J7[hk][1 + i])].add(cma(sub, a))
g7_bad = [k for k, v in sorted(G7.items()) if len(v) > 1]
g7_consist = all(G7[k] <= GROUP[k] for k in G7)
n_subs_all = len(set(MVMEMO.values()))
check("LG2c MENU FACTORIZATION AT DEPTH 7 (LG2a + LG2b extended): "
      "own-view sufficiency holds on all 145,408 depth-7 histories "
      "(290,816 further comparisons — 436,316 total with LG2a — "
      "ZERO exceptions), and the (actor, tau) menu classes remain "
      "the SAME 16 with the SAME canonical per-actor menus (no new "
      "tau value, no new menu, zero violations): the own-view-lag "
      "subtlety is menu-invisible one full level out-of-sample; "
      "45,467 distinct menu-view sub-histories in total",
      n_cmp7 == 290816 and not struct_bad7
      and len(G7) == 16 and not g7_bad and g7_consist
      and n_subs_all == 45467,
      f"comparisons = {n_cmp7}; violations = {len(struct_bad7)}; "
      f"classes = {len(G7)}; class-menus inside the cache classes "
      f"= {g7_consist}; distinct sub-histories = {n_subs_all}")

NEW_T = {}
tr7_bad = []
n_tr7 = 0
for hk in D7:
    h6, e = hk[:-1], hk[-1]
    n_tr7 += 1
    k = canon_pair(h6, e)
    tgt = J7[hk]
    if k in ST:
        if ST[k] != tgt: tr7_bad.append((h6, e))
    elif k in NEW_T:
        if NEW_T[k] != tgt: tr7_bad.append((h6, e))
    else:
        NEW_T[k] = tgt
check("LG3b SIGMA-KEYED JOINT DETERMINISM AT 6->7: all 145,408 "
      "depth-6->7 transitions deterministic in (sigma, e-up-to-"
      "renaming) with the JOINT target; 16 NEW abstract keys "
      "beyond the cached 160 (176 total — EXACTLY the D44a CG7c "
      "key census: the joint table again adds no keys), zero "
      "mismatches",
      n_tr7 == 145408 and not tr7_bad
      and len(NEW_T) == 16 and len(ST) + len(NEW_T) == 176,
      f"transitions = {n_tr7}; violations = {len(tr7_bad)}; new "
      f"keys = {len(NEW_T)}; total keys = {len(ST) + len(NEW_T)}")

# ---- LG4: the negative controls (scratch variants, in-receipt) -----
def strip_e(e):
    """Base-blind event skeleton: renaming-invariant (actor names
    and payload bits are never renamed; base identities dropped)."""
    if e[0] == 'p': return ('p', e[1], e[3])
    if e[0] == 'r':
        return ('r', e[1], tuple(sorted((t[0], t[2]) for t in e[2])),
                tuple(sorted((t[0], t[2]) for t in e[3])))
    return e

def menu_bases(menu):
    bs = set()
    for e, q in menu:
        if e[0] == 'p': bs.add(e[2])
        elif e[0] == 'r':
            for t in tuple(e[2]) + tuple(e[3]): bs.add(t[1])
    return bs

def fp_actor(menu, a):
    """Renaming-invariant per-actor menu fingerprint: base-blind
    rows with exact weights + the count of distinct bases the
    actor's rows mention. Fingerprint inequality certifies GENUINE
    menu difference (no canonicalization artifact)."""
    rows = tuple(sorted((repr(strip_e(e)), str(q))
                        for e, q in menu if e[1] == a))
    sub = [(e, q) for e, q in menu if e[1] == a]
    return (rows, len(menu_bases(sub)))

# LG4a: tau variant DROPPING the menu-visible component data (the
# d44a CG6b substitution on the sub-history: live proposals as
# (proposer, base) only — payloads and conflict-edge/component
# structure dropped; at this scope edges are payload-generated, so
# the edge drop and the payload drop are one move, D44a nit N1).
def tau_b(subk):
    hold, live, comps, refs, sup = sigma_raw(subk)
    best = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        s = repr((tuple((a, m.get(hold[a])) for a in AB),
                  tuple(sorted(((t[0], m[t[1]]) for t in live),
                               key=repr)),
                  tuple(sorted((m[b], b in sup) for b in refs))))
        if best is None or s < best: best = s
    return best

TB = {}
GA = defaultdict(dict)
for h in FAM:
    hk = tuple(h)
    for a in AB:
        sub = MVMEMO[(hk, a)]
        if sub not in TB: TB[sub] = tau_b(sub)
        f = fp_actor(CACHE[hk], a)
        d = GA[(a, TB[sub])]
        if f not in d: d[f] = hk
bad_a = {k: v for k, v in sorted(GA.items(), key=repr)
         if len(v) > 1}
ka = sorted(bad_a, key=repr)[0] if bad_a else ('A', '')
wa = sorted(bad_a[ka].values(),
            key=lambda x: (len(x), repr(x)))[:2] if bad_a else []
check("LG4a CONTROL — DROPPING THE COMPONENT/PAYLOAD DATA FROM "
      "TAU BREAKS LG2, loudly: the CG6b-substituted tau variant "
      "(live as (proposer, base) only) merges the 16 (actor, tau) "
      "classes to 10, of which SIX contain histories with "
      "DIFFERENT renaming-invariant per-actor menu fingerprints — "
      "the dropped data is menu-visible (payload bits reappear in "
      "arbitration candidates), so the variant CANNOT factor the "
      "menu; first witness pair printed below",
      len(GA) == 10 and len(bad_a) == 6 and len(wa) == 2
      and fp_actor(CACHE[wa[0]], ka[0])
      != fp_actor(CACHE[wa[1]], ka[0]),
      f"variant classes = {len(GA)}; menu-splitting classes = "
      f"{len(bad_a)}")
if len(wa) == 2:
    print(f"    [LG4a witness, actor {ka[0]}] "
          f"h1 = {tuple(pr_e(e) for e in wa[0])}")
    print(f"    [LG4a witness, actor {ka[0]}] "
          f"h2 = {tuple(pr_e(e) for e in wa[1])}")

# LG4b: sigma coarsening DROPPING the superseded marks AND the
# holdings pattern jointly (pin LG4's second scratch variant) —
# must break LG1's constancy or LG2. It breaks BOTH.
def sigma_c(hk):
    hold, live, comps, refs, sup = sigma_raw(hk)
    lrefs = sorted({t[1] for t in live}, key=repr)
    best = None
    for perm in permutations(range(len(lrefs))):
        m = {lrefs[i]: perm[i] for i in range(len(lrefs))}
        s = repr((tuple(sorted(((t[0], m[t[1]], t[2])
                                for t in live), key=repr)),
                  tuple(sorted(((m[c[0]], c[1], c[2])
                                for c in comps), key=repr))))
        if best is None or s < best: best = s
    return best

GC = defaultdict(dict)
GT = defaultdict(dict)
for h in FAM:
    hk = tuple(h)
    sc = sigma_c(hk)
    menu = CACHE[hk]
    inv = (tuple(sorted((repr(strip_e(e)), str(q))
                        for e, q in menu)),
           len(menu_bases(menu)))
    if inv not in GC[sc]: GC[sc][inv] = hk
    if TAU[hk] not in GT[sc]: GT[sc][TAU[hk]] = hk
bad_c = {k: v for k, v in sorted(GC.items()) if len(v) > 1}
bad_t = {k: v for k, v in sorted(GT.items()) if len(v) > 1}
wc = sorted(sorted(bad_c.items(), key=repr)[0][1].values(),
            key=lambda x: (len(x), repr(x)))[:2] if bad_c else []
wt = sorted(sorted(bad_t.items(), key=repr)[0][1].values(),
            key=lambda x: (len(x), repr(x)))[:2] if bad_t else []
check("LG4b CONTROL — THE SIGMA COARSENING (superseded marks AND "
      "holdings pattern dropped jointly) BREAKS BOTH LG1-CONSTANCY "
      "AND MENU FACTORIZATION, loudly: the coarsened abstraction "
      "has 13 classes on the cache; NINE of them mix distinct "
      "(tau_A, tau_B) pairs (LG1's tau-constancy fails) and FIVE "
      "of them mix histories with different renaming-invariant "
      "full-menu invariants (base-blind rows + distinct-base "
      "count: the root class merges the empty history with "
      "post-renewal states whose menus target TWO bases) — the "
      "dropped data is load-bearing; witnesses printed below",
      len(GC) == 13 and len(bad_t) == 9 and len(bad_c) == 5
      and len(wc) == 2 and len(wt) == 2,
      f"coarse classes = {len(GC)}; tau-mixing = {len(bad_t)}; "
      f"menu-mixing = {len(bad_c)}")
if len(wc) == 2:
    print(f"    [LG4b menu witness] "
          f"h1 = {tuple(pr_e(e) for e in wc[0])}")
    print(f"    [LG4b menu witness] "
          f"h2 = {tuple(pr_e(e) for e in wc[1])}")
if len(wt) == 2:
    print(f"    [LG4b tau witness]  "
          f"h1 = {tuple(pr_e(e) for e in wt[0])}")
    print(f"    [LG4b tau witness]  "
          f"h2 = {tuple(pr_e(e) for e in wt[1])}")

# ---- LG5: purity + self-scan (#362 allow-list form) ----------------
ALLOW = (Fr, int, str, bool, type(None))
CONT = (tuple, list, frozenset, set)
n_leaf = 0
n_impure = 0
def walk(x):
    global n_leaf, n_impure
    if isinstance(x, CONT):
        for y in x: walk(y)
    elif isinstance(x, dict):
        for k2, v2 in x.items():
            walk(k2); walk(v2)
    else:
        n_leaf += 1
        if not isinstance(x, ALLOW): n_impure += 1
for obj in (CACHE, SIG, TAU, JREP, JT, ST, NEW_T, GROUP, G7, CMA):
    walk(obj)
check("LG5a the ALLOW-LIST PURITY WALK (#362 form) over the "
      "delivered objects (the full candidate cache incl. depth 7, "
      "sigma, tau, the closed joint set, all transition tables, "
      "the menu classes): every leaf is Fraction / int / str / "
      "bool / None — floats, Decimals, numpy scalars and every "
      "transient-construction smuggling route rejected "
      "categorically; the leaf census anchored",
      n_leaf == 21088527 and n_impure == 0,
      f"leaves = {n_leaf}; impure = {n_impure}")

_own = open(os.path.abspath(__file__)).read()
_pat = "check(Tr" + "ue"
check("LG5b self-scan: no vacuous gate anywhere in this receipt "
      "(the forbidden always-true check pattern has zero source "
      "occurrences outside this scan's own constructor) and every "
      "check carries a computed predicate",
      _own.count(_pat) == 0,
      f"occurrences = {_own.count(_pat)}")

# ========================== VERDICT =================================
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — gate breakage; exit 1 by design")
    sys.exit(1)
print("[VERDICT] d46a GREEN-UNREVIEWED (the hostile round is "
      "deferred per the D46 program pin; paper-32's round precedes "
      "it) — H1'S MECHANICAL CORE HOLDS, route R-A delivered: "
      "tau_A/tau_B (sigma applied to the menu-view own-view "
      "sub-histories) join sigma in a transition system whose BFS "
      "CLOSES at 36 joint states, frontier exhausted, 176 edges — "
      "IDENTICAL anchors to the D44a sigma closure — and the "
      "projection onto sigma is INJECTIVE: tau is CONSTANT on "
      "sigma (36/36 classes, zero exceptions on all 179,783 "
      "histories through depth 7). The own-view lag (W2) is "
      "sigma-invisible at abstraction level. Menus factor through "
      "tau: the committed layer re-run on the menu-view "
      "sub-history alone reproduces every per-actor menu "
      "entrywise (436,316 comparisons, zero exceptions — "
      "cone-locality made mechanical), and each of the 16 (actor, "
      "tau) classes carries ONE canonical per-actor menu (8 tau "
      "values per actor; zero exceptions at every verified "
      "depth). The R-B counterexample horn did NOT fire. H2's "
      "status DECLARED (LG3): the transition table is sigma-keyed "
      "(160 + 16 = 176 keys, zero conflicts), so H2 is subsumed "
      "by the same joint closure — one abstract-update law powers "
      "both. Controls: the component/payload-dropped tau variant "
      "merges 16 -> 10 classes with 6 menu-splitting (LG4a); the "
      "holdings+superseded-dropped sigma coarsening yields 13 "
      "classes with 9 tau-mixing and 5 menu-mixing (LG4b) — both "
      "fail loudly, the delivered abstractions do not. WHAT THIS "
      "RECEIPT DOES NOT CLAIM: the all-depth quantifier is NOT "
      "discharged mechanically — depth-free H1 now rests on "
      "exactly two structural facts for the pin-§5 proof note: "
      "(i) cone-locality of the layer's per-candidate computation "
      "(LG2a's census, to be written as a code-reading theorem) "
      "and (ii) the abstract-update law (joint-transition "
      "determinism as a law; LG1a/LG3's census). Given (i)+(ii), "
      "sigma -> (tau_A, tau_B) -> menus closes H1 AND H2 at every "
      "depth and the D44a §8 assembly decides residue 1 OUTRIGHT "
      "at d42a scope; transport scope remains D46b's problem.")
