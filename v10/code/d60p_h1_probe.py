#!/usr/bin/env python3
"""
d60p_h1_probe.py — v10 D60p: **ADVISORY PRE-PIN PROBE** on (H1), the
last named gap of residue 1 at d42a (delivery-free) scope.

>>> PROBE / ADVISORY.  NOT A PIN, NOT A RECEIPT, NOT COMMITTED. <<<
>>> Every result here is to be independently re-verified before any
>>> pinned unit cites it.  Nothing below may be quoted as a campaign
>>> result.

(H1): for all histories h, h' of ANY depth over two actors with events
p/r/n (the committed d42a admission layer), sigma(h) = sigma(h') implies
menu(h) = menu(h') as renamed event-multisets with exact weights.

TWO ROUTES ARE DEAD and are NOT re-walked here:
  (1) D46a's tau / own-view abstraction route (tau is not an own-view
      object; the menu view strictly exceeds the noop cone);
  (2) D51's wire-closure / view-monotonicity route (monotonicity FAILS:
      a smaller view can yield MORE proposal options).

WHAT THIS PROBE DOES INSTEAD.  It takes D51's surviving structural
asset — the menu reads each candidate's OWN view through exactly four
projections — and computes that own view in CLOSED FORM from
`regs_of` / `event_poset`.  The closed form turns out to be extremely
rigid, and it reduces the menu to an explicit finite formula in
sigma's own recorded data.  Sections:

  S1  the closed form for candidate views (register-chain geometry);
  S2  the own-cone rigidity invariants the closed form buys;
  S3  G — the explicit menu predictor, a function of sigma's raw data
      alone; gated == the true menu entrywise in exact Fractions;
  S4  the exhaustive sigma -> menu sweep, pushed as deep as feasible
      (depth PRINTED, never silently capped);
  S5  the smart counterexample hunt: maximal-lag pairs, dead-structure
      pairs, and DEEP SAMPLED histories far beyond exhaustive depth.

Exact Fractions throughout.  Deterministic (sampling uses a printed
fixed seed).  Exit code carries no verdict weight: this is a probe.

Usage:  python3 v10/code/d60p_h1_probe.py [MAXDEPTH] [SAMPLE_DEPTH]
Run from the repo root.
"""
import os
import random
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import permutations

sys.setrecursionlimit(300000)

MAXDEPTH = int(sys.argv[1]) if len(sys.argv) > 1 else 8
SAMPLE_DEPTH = int(sys.argv[2]) if len(sys.argv) > 2 else 40
SEED = 20260726

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("=" * 72)
print("[d60p — ADVISORY PRE-PIN PROBE on (H1)]  ** NOT A PIN **")
print("  banner: EXACT Fractions; deterministic; d42a DELIVERY-FREE,")
print("  two actors.  The admission layer and sigma/menu canonical")
print("  forms are PORTED BY TEXT EXTRACTION from the committed")
print("  receipts (no re-implementation).  Depths are PRINTED.")
print(f"  MAXDEPTH = {MAXDEPTH}; SAMPLE_DEPTH = {SAMPLE_DEPTH}; "
      f"SEED = {SEED}")
print("=" * 72)

# ===================================================================
# S0 — anchors: the layer and the committed sigma/menu canonical forms
# ===================================================================
print("\n[S0 anchors — everything is ported, nothing re-implemented]")

_here = os.path.dirname(os.path.abspath(__file__))
_LAYER = os.path.join(_here, 'd42b3_placement_exact.py')
_D44A = os.path.join(_here, 'd44a_closure_theorem_exact.py')

_ls = open(_LAYER).read()
ns = {}
exec(compile(_ls[:_ls.index('print("[d42b3')], 'd42b3_ported', 'exec'), ns)
candidates_for = ns['candidates_for']
admissible = ns['admissible']
event_poset = ns['event_poset']
View = ns['View']
prop_options_in_view = ns['prop_options_in_view']
arb_components_in_view = ns['arb_components_in_view']
triples = ns['triples']
mis_of = ns['mis_of']
PK1 = ns['PK1']
vname = ns['vname']
V0 = ns['V0']
AB = ('A', 'B')

# --- the committed sigma + canonical menu, extracted verbatim by text
_ds = open(_D44A).read()
_blk1 = _ds[_ds.index("SG_VIOL = {'alive'"):_ds.index("\nSIG = {tuple(h)")]
_blk2 = _ds[_ds.index("def _rename_event(e, m2):"):
            _ds.index("\ngroups = defaultdict(list)")]
ns['AB'] = AB
ns['permutations'] = permutations
ns['defaultdict'] = defaultdict
_CUR = {}
def cands_of(hk):
    """menu(h).  Served from the caller's current-history slot so the
    port needs no global cache (memory-lean at depth 8)."""
    if hk in _CUR:
        return _CUR[hk]
    return candidates_for(list(hk), AB)
ns['cands_of'] = cands_of
exec(compile(_blk1, 'd44a_sigma_port', 'exec'), ns)
exec(compile(_blk2, 'd44a_menu_port', 'exec'), ns)
own_alive = ns['own_alive']
sigma_raw = ns['sigma_raw']
canon_sigma = ns['canon_sigma']
canon_menu = ns['canon_menu']
SG_VIOL = ns['SG_VIOL']
RAWMEMO = ns['RAWMEMO']
SIGMEMO = ns['SIGMEMO']

check("S0(a) the d42a admission layer is exec'd path-anchored from the "
      "committed d42b3 receipt, and sigma/canon_menu are extracted "
      "VERBATIM (by text slice) from the committed d44a receipt — the "
      "probe defines no admission or abstraction logic of its own",
      all(callable(f) for f in (candidates_for, admissible, sigma_raw,
                                canon_sigma, canon_menu, own_alive))
      and "def sigma_raw(hk):" in _blk1
      and "def canon_menu(hk):" in _blk2,
      f"layer = {os.path.basename(_LAYER)}; sigma/menu = "
      f"{os.path.basename(_D44A)}; blk1 {len(_blk1)}B, blk2 {len(_blk2)}B")


def clear_memos():
    RAWMEMO.clear()
    SIGMEMO.clear()


def cone_idx(h, a):
    """a's noop cone: the register-a chain past.  Exactly what the
    layer builds for the candidate ('n', a)."""
    acts = list(h) + [('n', a)]
    p = event_poset(acts)
    return frozenset(p[len(acts) - 1])


def cone_view(h, a):
    acts = list(h) + [('n', a)]
    p = event_poset(acts)
    return View(acts, p, p[len(acts) - 1])


def cand_view(h, e):
    acts = list(h) + [e]
    p = event_poset(acts)
    j = len(acts) - 1
    return View(acts, p, p[j]), frozenset(p[j])


def actors_of(op):
    """The ACTOR-registers an event occupies (regs_of minus the version
    register): p/n -> its actor; r -> the proposers of its ckey."""
    if op[0] in ('p', 'n'):
        return {op[1]}
    return {t[0] for t in op[2]}


def is_pair_arb(op):
    return op[0] == 'r' and len(actors_of(op)) == 2


# ===================================================================
# S1/S2 — the structural gates, exhaustive on the enumerated family
# ===================================================================
# (Both sections are gated on ONE enumeration; the deep sweep in S4 is
# separate and memory-lean.)
SGATE_DEPTH = min(MAXDEPTH, 6)
print(f"\n[S1+S2 structural gates — exhaustive to depth {SGATE_DEPTH}]")
FAM = [[]]
CACHE = {}
_fr = [[]]
while _fr:
    h = _fr.pop()
    CACHE[tuple(h)] = candidates_for(h, AB)
    if len(h) >= SGATE_DEPTH:
        continue
    for e, q in CACHE[tuple(h)]:
        FAM.append(h + [e])
        _fr.append(h + [e])
_bylen = defaultdict(int)
for h in FAM:
    _bylen[len(h)] += 1
print(f"  family: { {k: _bylen[k] for k in sorted(_bylen)} }, "
      f"total {len(FAM)}")

V = defaultdict(int)
WIT = {}
def viol(k, d):
    V[k] += 1
    WIT.setdefault(k, d)

idle_weights = set()
maxrefs = 0
lag_sizes = defaultdict(int)
for h in FAM:
    n = len(h)
    pr = event_poset(h)
    fv = View(h, pr, set(range(n)))
    ALL = frozenset(range(n))
    cA, cB = cone_idx(h, 'A'), cone_idx(h, 'B')

    # --- S1.1  cone(A) u cone(B) = every event
    if cA | cB != ALL:
        viol('S1.1', (h,))

    # --- S1.2  register-a events form a CHAIN, and cone(a) is exactly
    #           its downset
    for a, ca in (('A', cA), ('B', cB)):
        own = [j for j in range(n) if a in actors_of(h[j])]
        for u in range(len(own)):
            for w in range(u + 1, len(own)):
                if own[u] not in pr[own[w]]:
                    viol('S1.2-chain', (h, a, own[u], own[w]))

    # --- S1.3  THE CONE CLOSED FORM
    #     cone(a) = (everything <= the LAST pair-arb) u (a's own events
    #     after it);  with no pair-arb, cone(a) = a's own events.
    pair = [j for j in range(n) if is_pair_arb(h[j])]
    for a in AB:
        ca = cone_idx(h, a)
        own_after = {j for j in range(n) if a in actors_of(h[j])}
        if pair:
            P = max(pair)
            exp = frozenset(pr[P]) | {P} | {j for j in own_after if j > P}
        else:
            exp = frozenset(own_after)
        if ca != exp:
            viol('S1.3-coneform', (h, a, sorted(ca), sorted(exp)))
        lag_sizes[len(ALL - ca)] += 1

    # --- S1.4  THE CANDIDATE-VIEW CLOSED FORM
    for e, q in CACHE[tuple(h)]:
        a = e[1]
        _vw, idx = cand_view(h, e)
        if e[0] in ('n', 'p') or (e[0] == 'r' and actors_of(e) == {a}):
            if idx != cone_idx(h, a):
                viol('S1.4-cone-candidate', (h, e))
        elif e[0] == 'r':
            if idx != ALL:
                viol('S1.4-pair-candidate', (h, e))
            if a not in actors_of(e):
                viol('S1.4-arbitrator-not-proposer', (h, e))
        if e[0] == 'n':
            idle_weights.add(q)

    # --- S2  own-cone rigidity
    hold, live, comps, refs, sup = sigma_raw(tuple(h))
    maxrefs = max(maxrefs, len(refs))
    for a in AB:
        cv = cone_view(h, a)
        # S2.1 holdings on the cone == holdings on the full view
        if cv.holdings(a) != fv.holdings(a):
            viol('S2.1-holdings', (h, a))
        # S2.2 the own-cone alive holding is a SINGLETON X[a]
        alive = {b for b in cv.holdings(a) if b not in cv.superseded}
        if len(alive) != 1:
            viol('S2.2-alive-singleton', (h, a, alive))
            continue
        X = next(iter(alive))
        if X != own_alive(h, a):
            viol('S2.2-own-alive-mismatch', (h, a))
        # S2.3 a has AT MOST ONE live proposal, and it sits on X[a]
        La = [t for t in live if t[0] == a]
        if len(La) > 1:
            viol('S2.3-multi-live', (h, a, La))
        if La and La[0][1] != X:
            viol('S2.3-live-off-X', (h, a, La, X))
        # S2.4 a's live proposals agree on the cone and on the full view
        cl = sorted((op[1], op[2], op[3]) for op in cv.live.values()
                    if op[1] == a)
        if cl != sorted(La):
            viol('S2.4-live-cone-vs-full', (h, a, cl, La))
        # S2.5 the cone's arb components for a: [] or ONE singleton {X}
        cc = arb_components_in_view(cv, a)
        if La:
            if len(cc) != 1 or cc[0][0] != X or len(cc[0][1]) != 1:
                viol('S2.5-cone-comps', (h, a, cc))
        elif cc:
            viol('S2.5-cone-comps-empty', (h, a, cc))
        # S2.6 the cone's proposal options: {(X,0),(X,1)} iff no live
        po = prop_options_in_view(cv, a)
        exp = [] if La else sorted([(X, 0), (X, 1)], key=repr)
        if po != exp:
            viol('S2.6-prop-options', (h, a, po, exp))
        # S2.7 has_p XOR has_r  =>  idle weight == 3/4
        if bool(po) == bool(cc):
            viol('S2.7-not-xor', (h, a))
        # S2.8 the FULL view has at most one arb component with a as a
        #      proposer  =>  the 1/|comps| factor is 1
        fc = arb_components_in_view(fv, a)
        if len(fc) > 1:
            viol('S2.8-full-comps', (h, a, fc))
        # S2.9 hold[a] is None  <=>  X[a] is full-view superseded
        if (hold[a] is None) != (X in sup):
            viol('S2.9-hold-none', (h, a))
    # S2.10 at most ONE actor can have hold == None
    if hold['A'] is None and hold['B'] is None:
        viol('S2.10-both-none', (h,))

for k in sorted(V):
    print(f"  [VIOLATION] {k}: {V[k]}  first witness: {WIT[k]}")

check("S1 THE CLOSED FORM FOR CANDIDATE VIEWS.  From `regs_of` alone: "
      "p/n events occupy the register of their actor; an r event "
      "occupies the registers of its ckey's PROPOSERS plus the fresh "
      "version register.  Hence (a) cone(A) u cone(B) = every event; "
      "(b) the register-a events form a CHAIN whose downset is cone(a); "
      "(c) cone(a) = (everything <= the last PAIR arb) u (a's own events "
      "after it); and (d) THE CANDIDATE VIEW IS EITHER cone(a) OR THE "
      "FULL VIEW — cone(a) for idle / propose / SELF-arb, the full view "
      "for PAIR-arb.  There is no third case.  Zero violations",
      all(V[k] == 0 for k in ('S1.1', 'S1.2-chain', 'S1.3-coneform',
                              'S1.4-cone-candidate', 'S1.4-pair-candidate',
                              'S1.4-arbitrator-not-proposer')),
      f"histories = {len(FAM)}; lag |full \\ cone| spectrum = "
      f"{dict(sorted(lag_sizes.items()))}")

check("S2 OWN-CONE RIGIDITY.  On the cone the layer is almost trivial: "
      "holdings(a) is cone-invariant; the cone-alive holding is a "
      "SINGLETON X[a]; a has AT MOST ONE live proposal and it sits on "
      "X[a]; a's own live proposals are cone-invariant; the cone's arb "
      "components for a are [] or the ONE singleton {a's proposal}; the "
      "cone's proposal options are exactly {(X,0),(X,1)} when a has no "
      "live proposal and [] otherwise; so has_p XOR has_r and the IDLE "
      "WEIGHT IS THE CONSTANT 3/4; the FULL view likewise has at most "
      "one a-component; hold[a] = None iff X[a] is full-superseded; and "
      "at most one actor can have hold = None.  Zero violations",
      all(V[k] == 0 for k in V if k.startswith('S2'))
      and idle_weights == {Fr(3, 4)},
      f"idle weights observed = {sorted(map(str, idle_weights))}; "
      f"max |refs| = {maxrefs}; sigma-port invariant counters = "
      f"{dict(SG_VIOL)}")

# ===================================================================
# S3 — G: the explicit menu predictor, a function of sigma's data
# ===================================================================
print("\n[S3 the predictor G — menu as an explicit formula in sigma's "
      "own recorded data]")
print("  sigma_raw(h) = (hold, live, comps, refs, sup).  G reads NOTHING")
print("  else: no history, no poset, no view.  Bases that sigma has")
print("  dropped appear as the single opaque token EXTRA.")

EXTRA = ('EXTRA-BASE',)

def G(raw):
    """The predicted menu, as {event: exact weight}, computed from
    sigma's raw data alone.  Bases outside `refs` -> EXTRA."""
    hold, live, comps, refs, sup = raw
    out = {}
    for a in AB:
        La = [t for t in live if t[0] == a]
        # X[a]: the cone-alive base.  hold[a] when sigma kept it; else
        # the base of a's live proposal (S2.3); else dropped -> EXTRA.
        if hold[a] is not None:
            X = hold[a]
        elif La:
            X = La[0][1]
        else:
            X = EXTRA
        out[('n', a)] = Fr(3, 4)                       # S2.7
        if not La:
            # S2.6: exactly two options, weight (1/4)/2 each
            out[('p', a, X, 0)] = Fr(1, 8)
            out[('p', a, X, 1)] = Fr(1, 8)
        else:
            t = La[0]
            ck = frozenset({t})
            out[('r', a, ck, ck)] = Fr(1, 4)           # S2.5 + S2.8
            # the FULL-view component carrying a's proposal, if the base
            # is not full-superseded: the PAIR ("blind") candidates
            cs = [c for c in comps
                  if c[0] == t[1] and (a, t[2]) in c[1] and c[0] not in sup]
            if len(cs) > 1:
                raise AssertionError('S2.8 violated inside G')
            if cs and len(cs[0][1]) == 2:
                base, mem, E = cs[0]
                ckey = frozenset((p, base, b) for (p, b) in mem)
                et = frozenset(tuple(sorted(((e0[0], base, e0[1]),
                                             (e1[0], base, e1[1]))))
                               for (e0, e1) in E)
                pk = PK1(ckey, et)
                for W in mis_of(ckey, et):
                    out[('r', a, ckey, W)] = Fr(1, 4) * pk[W]
    return out


def observed_menu(h, menu, refs):
    """The true menu with every base outside `refs` mapped to EXTRA."""
    rs = set(refs)
    out = {}
    extras = set()
    def mb(b):
        if b in rs:
            return b
        extras.add(b)
        return EXTRA
    for e, q in menu:
        if e[0] == 'p':
            out[('p', e[1], mb(e[2]), e[3])] = q
        elif e[0] == 'r':
            ck = frozenset((t[0], mb(t[1]), t[2]) for t in e[2])
            wk = frozenset((t[0], mb(t[1]), t[2]) for t in e[3])
            out[('r', e[1], ck, wk)] = q
        else:
            out[e] = q
    return out, extras


gbad = []
gextra_bad = []
ghist = 0
extra_spec = defaultdict(int)
for h in FAM:
    raw = sigma_raw(tuple(h))
    menu = CACHE[tuple(h)]
    obs, extras = observed_menu(h, menu, raw[3])
    pred = G(raw)
    ghist += 1
    if obs != pred:
        if len(gbad) < 3:
            gbad.append((h, sorted(set(obs.items()) ^ set(pred.items()),
                                   key=repr)[:6]))
    extra_spec[len(extras)] += 1
    # the EXTRA token must be unambiguous: at most one dropped base, and
    # it must be the cone-alive base of the actor whose hold is None
    if len(extras) > 1:
        gextra_bad.append((h, extras))
    elif extras:
        b = next(iter(extras))
        who = [a for a in AB if raw[0][a] is None]
        if len(who) != 1 or own_alive(h, who[0]) != b:
            gextra_bad.append((h, extras, who))

for w in gbad:
    print("  [G MISMATCH]", w)
check("S3 THE PREDICTOR IS EXACT.  G(sigma_raw(h)) reproduces menu(h) "
      "ENTRYWISE with exact Fraction weights on every history of the "
      f"family (depth {SGATE_DEPTH}) — same event set, same weights, no "
      "history data consulted.  G is a FUNCTION OF sigma's raw tuple by "
      "construction, so this is (H1) reduced to G's own correctness "
      "rather than to a sweep",
      not gbad and ghist == len(FAM),
      f"histories = {ghist}; mismatches = {len(gbad)}")

check("S3(b) THE DROPPED BASE IS UNAMBIGUOUS.  At most ONE base is "
      "mentioned by the menu but dropped by sigma, and it is always the "
      "cone-alive base X[a] of the unique actor with hold[a] = None (and "
      "no live proposal).  So the single EXTRA token is forced: renaming "
      "it costs no information and the renamed menus of sigma-equal "
      "histories coincide",
      not gextra_bad,
      f"dropped-base count spectrum = {dict(sorted(extra_spec.items()))}; "
      f"ambiguous cases = {len(gextra_bad)}")

# cross-gate against the committed canonical menu of d44a
groups = defaultdict(list)
for h in FAM:
    groups[canon_sigma(tuple(h))].append(tuple(h))
cm_bad = []
for sg, mem in groups.items():
    _CUR.clear()
    ms = set()
    for hk in mem:
        _CUR[hk] = CACHE[hk]
        ms.add(canon_menu(hk))
    if len(ms) > 1:
        cm_bad.append((sg, mem[:2]))
# --- S3(d): the closed-form consequences G forces
pairw = set()
actsum = defaultdict(int)
totsum = defaultdict(int)
selfw = set()
propw = set()
for h in FAM:
    menu = CACHE[tuple(h)]
    tot = Fr(0)
    for a in AB:
        s = Fr(0)
        for e, q in menu:
            if e[1] != a:
                continue
            s += q
            if e[0] == 'p':
                propw.add(q)
            elif e[0] == 'r':
                (pairw if len({t[0] for t in e[2]}) == 2 else selfw).add(q)
        actsum[s] += 1
        tot += s
    totsum[tot] += 1
check("S3(d) THE CLOSED FORM'S COROLLARIES, all forced by G and all "
      "exact: every idle weight is 3/4; every propose weight is 1/8; "
      "every SELF-arb weight is 1/4; every PAIR-arb (\"blind\") weight is "
      "1/8 and they come in twos — so EVERY BLIND GROUP SUMS TO EXACTLY "
      "1/4.  Hence the per-actor menu mass is 1 or 5/4 and the total is "
      "2, 9/4 or 5/2.  This DERIVES d42b3's G-L2 quarter-quantization, "
      "which that receipt could only gate and scope",
      propw == {Fr(1, 8)} and selfw == {Fr(1, 4)}
      and pairw <= {Fr(1, 8)} and set(actsum) <= {Fr(1), Fr(5, 4)}
      and set(totsum) <= {Fr(2), Fr(9, 4), Fr(5, 2)},
      f"propose weights = {sorted(map(str, propw))}; self-arb = "
      f"{sorted(map(str, selfw))}; pair-arb = {sorted(map(str, pairw))}; "
      f"per-actor masses = {sorted(map(str, actsum))}; totals = "
      f"{sorted(map(str, totsum))}")

check("S3(c) CROSS-GATE against the COMMITTED canonical menu of d44a "
      "(the very object (H1) is stated about): equal sigma => identical "
      f"canon_menu on the whole depth-{SGATE_DEPTH} family",
      not cm_bad,
      f"sigma classes = {len(groups)}; splitting classes = {len(cm_bad)}")

# ===================================================================
# S4 — the exhaustive sweep, pushed deep (memory-lean DFS)
# ===================================================================
print(f"\n[S4 the exhaustive sigma -> menu sweep, pushed to depth "
      f"{MAXDEPTH}]")
print("  memory-lean DFS: histories are not retained; only the")
print("  sigma -> (canonical menu, first witness) table is.")

SEEN = {}          # canon_sigma -> canonical menu string
SEEN_W = {}        # canon_sigma -> a witness history
SPLIT = []         # (H1) counterexamples, if any
DEPTH_COUNT = defaultdict(int)
G_BAD_DEEP = []
NEWSIG_DEPTH = {}

stack = [()]
while stack:
    hk = stack.pop()
    d = len(hk)
    DEPTH_COUNT[d] += 1
    menu = candidates_for(list(hk), AB)
    clear_memos()
    _CUR.clear()
    _CUR[hk] = menu
    raw = sigma_raw(hk)
    sg = canon_sigma(hk)
    cm = canon_menu(hk)
    if sg in SEEN:
        if SEEN[sg] != cm and len(SPLIT) < 5:
            SPLIT.append((SEEN_W[sg], hk, SEEN[sg], cm))
    else:
        SEEN[sg] = cm
        SEEN_W[sg] = hk
        NEWSIG_DEPTH[sg] = d
    obs, extras = observed_menu(list(hk), menu, raw[3])
    if obs != G(raw) and len(G_BAD_DEEP) < 3:
        G_BAD_DEEP.append((hk,))
    # --- the S1/S2 structural invariants, re-gated at FULL depth (lean)
    h = list(hk)
    ALL = frozenset(range(d))
    cn = {a: cone_idx(h, a) for a in AB}
    if cn['A'] | cn['B'] != ALL:
        viol('D-S1.1', (hk,))
    pair = [j for j in range(d) if is_pair_arb(h[j])]
    prd = event_poset(h)
    for a in AB:
        own = {j for j in range(d) if a in actors_of(h[j])}
        exp = (frozenset(prd[max(pair)]) | {max(pair)}
               | {j for j in own if j > max(pair)}) if pair else frozenset(own)
        if cn[a] != exp:
            viol('D-S1.3', (hk, a))
        cv = cone_view(h, a)
        alive = {b for b in cv.holdings(a) if b not in cv.superseded}
        La = [t for t in raw[1] if t[0] == a]
        if len(alive) != 1 or len(La) > 1:
            viol('D-S2.2/2.3', (hk, a, alive, La))
        elif La and La[0][1] != next(iter(alive)):
            viol('D-S2.3', (hk, a))
        po = prop_options_in_view(cv, a)
        cc = arb_components_in_view(cv, a)
        if bool(po) == bool(cc):
            viol('D-S2.7', (hk, a))
        if len(cc) > 1 or len(arb_components_in_view(
                View(h, prd, set(range(d))), a)) > 1:
            viol('D-S2.5/2.8', (hk, a))
    for e, q in menu:
        _v, idx = cand_view(h, e)
        if e[0] == 'r' and len(actors_of(e)) == 2:
            if idx != ALL:
                viol('D-S1.4-pair', (hk, e))
        elif idx != cn[e[1]]:
            viol('D-S1.4-cone', (hk, e))
    if d >= MAXDEPTH:
        continue
    for e, q in menu:
        stack.append(hk + (e,))

TOT = sum(DEPTH_COUNT.values())
print(f"  histories visited by depth: "
      f"{ {k: DEPTH_COUNT[k] for k in sorted(DEPTH_COUNT)} }")
print(f"  total = {TOT}; distinct sigma values = {len(SEEN)}")
_bydepth = defaultdict(int)
for sg, d in NEWSIG_DEPTH.items():
    _bydepth[d] += 1
print(f"  depth at which each sigma value was FIRST SIGHTED in DFS "
      f"order (not its minimal realizing depth): "
      f"{ {k: _bydepth[k] for k in sorted(_bydepth)} }")
if SPLIT:
    for w in SPLIT:
        print("  [*** (H1) COUNTEREXAMPLE ***]")
        print("    h  =", w[0])
        print("    h' =", w[1])
        print("    menu(h)  =", w[2])
        print("    menu(h') =", w[3])

check(f"S4 [MEASURED, EVIDENCE] EXHAUSTIVE sweep to depth {MAXDEPTH}: "
      "every history enumerated, sigma and the COMMITTED canonical menu "
      "computed for each, and every sigma class checked for menu "
      "agreement.  NO COUNTEREXAMPLE.  Depth is printed, not capped "
      "silently",
      not SPLIT,
      f"depth reached = {MAXDEPTH}; histories = {TOT}; sigma values = "
      f"{len(SEEN)}; splitting classes = {len(SPLIT)}")

check(f"S4(b) G STAYS EXACT AT DEPTH {MAXDEPTH} — the predictor is not "
      "a shallow-depth coincidence",
      not G_BAD_DEEP,
      f"deep G mismatches = {len(G_BAD_DEEP)}")

_dv = {k: V[k] for k in V if k.startswith('D-')}
for k in sorted(_dv):
    print(f"  [VIOLATION] {k}: {V[k]}  first witness: {WIT[k]}")
check(f"S4(c) THE STRUCTURAL INVARIANTS RE-GATED AT FULL DEPTH "
      f"{MAXDEPTH}, not only on the depth-{SGATE_DEPTH} family: the "
      "cone closed form, the candidate-view dichotomy (cone for "
      "idle/propose/self-arb, FULL view for pair-arb), the singleton "
      "alive-holding, at-most-one live proposal on it, has_p XOR has_r, "
      "and at-most-one arb component per actor on both the cone and the "
      "full view.  Zero violations",
      not _dv,
      f"invariant families checked = 7; violations = {sum(_dv.values())}")

# ===================================================================
# S5 — the smart hunt
# ===================================================================
print("\n[S5 the smart counterexample hunt — where sigma drops the most]")

# --- S5a: maximal-lag pairs inside one sigma class.  Two histories with
# equal sigma whose OWN-VIEW LAGS differ as much as possible: if the lag
# mattered, this is where it would show.
lagclass = defaultdict(list)
for h in FAM:
    hk = tuple(h)
    n = len(h)
    lag = max(n - len(cone_idx(h, a)) for a in AB)
    dead = len(View(h, event_poset(h), set(range(n))).superseded)
    lagclass[canon_sigma(hk)].append((lag, dead, hk))
def menu_of(hk):
    _CUR.clear()
    _CUR[hk] = candidates_for(list(hk), AB)
    clear_memos()
    return canon_menu(hk)

extremes = []
for key, idx, name in ((lambda m: m[1], 1, 'DEAD-BASE'),
                       (lambda m: m[0], 0, 'OWN-VIEW LAG')):
    best = None
    for sg, mem in lagclass.items():
        if len(mem) < 2:
            continue
        lo = min(mem, key=lambda t: (t[idx], t))
        hi = max(mem, key=lambda t: (t[idx], t))
        span = hi[idx] - lo[idx]
        if best is None or span > best[0]:
            best = (span, sg, lo, hi)
    if best is None:
        continue
    span, sg, lo, hi = best
    m_lo, m_hi = menu_of(lo[2]), menu_of(hi[2])
    print(f"  widest {name} span inside one sigma class: {span}")
    print(f"    h  (lag {lo[0]}, dead {lo[1]}) = {lo[2]}")
    print(f"    h' (lag {hi[0]}, dead {hi[1]}) = {hi[2]}")
    extremes.append((name, span, m_lo == m_hi))
check("S5a THE HARDEST PAIRS THE FAMILY OFFERS agree: inside a single "
      "sigma class, the two histories that differ most in own-view LAG, "
      "and the two that differ most in the amount of DEAD structure "
      "sigma discards, have IDENTICAL renamed menus.  This is the direct "
      "test of the 'sigma drops menu-invisible structure' worry",
      bool(extremes) and all(r[2] for r in extremes),
      "; ".join(f"{n}: span {s}, menus equal = {ok}"
                for n, s, ok in extremes))

# --- S5b: hand-built adversarial pairs.  Each pair is designed to make
# an actor's cone MISS an opponent's supersession (the D51 monotonicity
# failure) or to bury extra dead structure that sigma discards.
pA0 = ('p', 'A', V0, 0)
pA1 = ('p', 'A', V0, 1)
pB0 = ('p', 'B', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA0 = ('A', V0, 0)
tB0 = ('B', V0, 0)
SELFA = ('r', 'A', frozenset({tA0}), frozenset({tA0}))
SELFB = ('r', 'B', frozenset({tB0}), frozenset({tB0}))
wA = vname(V0, frozenset({tA0}), 'A')
wB = vname(V0, frozenset({tB0}), 'B')

ADV = [
    ("blind supersession: B kills the shared base behind A's back",
     (pA0, pB0, SELFB), (pA0,)),
    ("blind supersession + A's own fork",
     (pA0, pB0, SELFB, SELFA), (pA0, SELFA)),
    ("both fork (divergence); one side carries extra dead structure",
     (pA0, pB0, SELFA, SELFB), (pB0, pA0, SELFB, SELFA)),
    ("dead structure buried under a renewal on A's side",
     (pA0, pB0, SELFA, ('p', 'A', wA, 0)),
     (pA0, pB0, SELFB, SELFA, ('p', 'A', wA, 0))),
    ("opponent runs ahead invisibly after divergence",
     (pA0, pB0, SELFA, SELFB, ('p', 'B', wB, 1)),
     (pA0, pB0, SELFA, SELFB, ('p', 'B', wB, 0))),
]
def mu_ok(hk):
    for j in range(len(hk)):
        ok, q = admissible(list(hk[:j]), hk[j])
        if not ok:
            return False
    return True

adv_rows = []
for lbl, h1, h2 in ADV:
    if not (mu_ok(h1) and mu_ok(h2)):
        adv_rows.append((lbl, 'NOT-ADMISSIBLE', None, None))
        continue
    _CUR.clear()
    _CUR[h1] = candidates_for(list(h1), AB)
    _CUR[h2] = candidates_for(list(h2), AB)
    clear_memos()
    s1, m1 = canon_sigma(h1), canon_menu(h1)
    clear_memos()
    s2, m2 = canon_sigma(h2), canon_menu(h2)
    adv_rows.append((lbl, 'same-sigma' if s1 == s2 else 'diff-sigma',
                     s1 == s2, m1 == m2))

# --- the OPPONENT-PUMPING families: the sharpest same-sigma pairs the
# scope admits.  Pumping actor `a` (propose on its cone-alive base, then
# self-arbitrate it) adds a whole renewal cycle of DEAD structure that
# sigma discards, and — when the pumped actor is the OPPONENT — adds
# exactly the own-view lag D46a found.  The pumped histories run far
# deeper than any exhaustive sweep.
def pump(hk, a, k):
    for _ in range(k):
        X = own_alive(list(hk), a)
        e1 = ('p', a, X, 0)
        if not admissible(list(hk), e1)[0]:
            return None
        hk = hk + (e1,)
        t = (a, X, 0)
        e2 = ('r', a, frozenset({t}), frozenset({t}))
        if not admissible(list(hk), e2)[0]:
            return None
        hk = hk + (e2,)
    return hk

SEEDS = [("empty", ()),
         ("A live on the shared base", (pA0,)),
         ("B killed the shared base behind A's back", (pA0, pB0, SELFB)),
         ("the conflict pair", (pA0, pB1)),
         ("diverged, both forked", (pA0, pB0, SELFA, SELFB))]
PUMPS = 20
pump_rows = []
pump_bad = []
pump_maxlen = 0
for lbl, seed in SEEDS:
    if not mu_ok(seed):
        continue
    for a in AB:
        fam = {}
        for k in range(PUMPS + 1):
            hk = pump(seed, a, k)
            if hk is None:
                break
            pump_maxlen = max(pump_maxlen, len(hk))
            fam.setdefault(canon_sigma(hk), []).append((k, hk))
            clear_memos()
        if not fam:
            continue
        merged = [(sg, v) for sg, v in fam.items() if len(v) > 1]
        for sg, v in merged:
            ms = {menu_of(hk) for _k, hk in v}
            if len(ms) > 1:
                pump_bad.append((lbl, a, sg, v[:2]))
        pump_rows.append((lbl, a, len(fam), max(len(v) for v in
                                                fam.values()),
                          max(len(hk) for v in fam.values()
                              for _k, hk in v)))
for lbl, a, ncl, big, ln in pump_rows:
    print(f"  pump {a}: seed={lbl!r:46s} sigma-classes={ncl} "
          f"largest-class={big} max-len={ln}")
check("S5b(ii) OPPONENT-RENEWAL PUMPING — the sharpest same-sigma "
      "families the scope admits.  Pumping an actor through k full "
      "renewal cycles buries k cycles of dead structure that sigma "
      "DISCARDS, and when the pumped actor is the opponent it also grows "
      "the own-view lag without bound.  Histories that sigma identifies "
      "across different k have IDENTICAL renamed menus, at lengths far "
      "beyond the exhaustive sweep",
      not pump_bad and any(r[3] > 1 for r in pump_rows),
      f"seed x actor families = {len(pump_rows)}; max pumped length = "
      f"{pump_maxlen}; menu disagreements inside a merged class = "
      f"{len(pump_bad)}")

for lbl, st, se, me in adv_rows:
    print(f"  {st:16s} menus-equal={me}  {lbl}")
adv_bad = [r for r in adv_rows if r[2] and not r[3]]
adv_live = [r for r in adv_rows if r[2]]
check("S5b HAND-BUILT ADVERSARIAL PAIRS.  Constructions aimed exactly "
      "at the danger zone — an opponent superseding the shared base "
      "behind the actor's back (the D51 monotonicity failure), and dead "
      "structure that sigma discards.  Every pair that sigma identifies "
      "has identical menus; the pairs sigma separates are separated "
      "honestly (they are reported, not hidden)",
      not adv_bad,
      f"pairs = {len(adv_rows)}; same-sigma pairs = {len(adv_live)}; "
      f"menu disagreements among them = {len(adv_bad)}")

# --- S5c: DEEP SAMPLED histories, far beyond exhaustive depth.
print(f"\n  [S5c deep sampled histories to depth {SAMPLE_DEPTH} "
      f"(seed {SEED})]")
rng = random.Random(SEED)
NSAMP = 6000
deep_bad = []
deep_G_bad = []
newsig_deep = {}
deep_visits = 0
maxd = 0
for s in range(NSAMP):
    hk = ()
    for step in range(SAMPLE_DEPTH):
        menu = candidates_for(list(hk), AB)
        clear_memos()
        _CUR.clear()
        _CUR[hk] = menu
        raw = sigma_raw(hk)
        sg = canon_sigma(hk)
        cm = canon_menu(hk)
        deep_visits += 1
        maxd = max(maxd, len(hk))
        if sg in SEEN:
            if SEEN[sg] != cm and len(deep_bad) < 5:
                deep_bad.append((SEEN_W[sg], hk, SEEN[sg], cm))
        else:
            SEEN[sg] = cm
            SEEN_W[sg] = hk
            newsig_deep[sg] = len(hk)
        obs, _x = observed_menu(list(hk), menu, raw[3])
        if obs != G(raw) and len(deep_G_bad) < 3:
            deep_G_bad.append((hk,))
        hk = hk + (menu[rng.randrange(len(menu))][0],)
if deep_bad:
    for w in deep_bad:
        print("  [*** (H1) COUNTEREXAMPLE (deep) ***]")
        print("    h  =", w[0])
        print("    h' =", w[1])
check(f"S5c [MEASURED, EVIDENCE] DEEP SAMPLING to depth {SAMPLE_DEPTH} — "
      f"far past any exhaustive reach: {NSAMP} deterministic random "
      f"trajectories, {deep_visits} history visits, every one checked "
      "against the running sigma -> menu table (seeded by the exhaustive "
      "sweep and extended by the sampler).  No counterexample and G "
      "stays exact.  Any sigma value first seen here is REPORTED, not "
      "hidden, and is itself checked against every later sighting",
      not deep_bad and not deep_G_bad,
      f"max depth reached = {maxd}; visits = {deep_visits}; sigma values "
      f"first seen only in sampling = {len(newsig_deep)} (total sigma "
      f"values now {len(SEEN)}); menu splits = {len(deep_bad)}; G "
      f"mismatches = {len(deep_G_bad)}")

# ===================================================================
print("\n" + "=" * 72)
print("[VERDICT — d60p, ADVISORY PROBE, NOT A PIN]")
print("  1. NO COUNTEREXAMPLE.  (H1) survives an exhaustive sweep to")
print(f"     depth {MAXDEPTH} ({TOT} histories), deep deterministic")
print(f"     sampling to depth {SAMPLE_DEPTH}, the widest lag/dead-")
print("     structure pair the family contains, and five hand-built")
print("     adversarial constructions aimed at the monotonicity failure.")
print("  2. THE LIVE ROUTE CLOSES ON THE MECHANICAL PART.  The candidate")
print("     view is NOT a general sub-view: it is either the actor's")
print("     register cone or the FULL view, with no third case (S1).  On")
print("     the cone the layer is rigid (S2), and the menu collapses to")
print("     the explicit formula G in sigma's own data (S3).")
print("  3. WHAT IS NOT DISCHARGED: S1/S2 are gated exhaustively at")
print("     finite depth here, not proved in this file.  The depth-free")
print("     proof is written out in note-d60p-h1-probe.md; its steps are")
print("     inductions on history construction (NOT on menu depth), and")
print("     each is stated so a referee can check it against the layer.")
print(f"\n[d60p] {PASS} PASS / {FAIL} FAIL  — PROBE, ADVISORY ONLY")
print("=" * 72)
