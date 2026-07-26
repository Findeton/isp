#!/usr/bin/env python3
"""
d51_menu_visibility_exact.py — v10 D51: (H1) via MENU-VISIBILITY.
Pin: note-d51-h1-menu-visibility-pin.md (STRICT, LOG #423, committed
before this file existed).

**ROUND-1 REVIEWED AND REPAIRED (2026-07-26).**  Independent hostile
review `v10/reviews/batch-round1-d50-to-d60.md` — REVISE, 2 BLOCKER /
3 MAJOR / 8 MINOR / 2 NIT.  The d42a admission layer was re-implemented
from scratch for the review and agreed with the committed layer on all
6,471 histories — menus with exact weights and posets, zero mismatches —
and every published number reproduced.  **Both BLOCKERs are
interpretation sentences, and the first inverts the unit's headline:**

  * BLOCKER 1 — "since sigma IS an abstraction of exactly those
    projections, menus are sigma-determined here" IS INVERTED.  The four
    projections REFINE sigma: 209 projection keys against 32 sigma
    states on the same family, every key determining its sigma state and
    every one of the 32 sigma states carrying more than one key.  So
    "projections determine sigma" is FALSE and MV3's
    projections-equal => menus-equal does NOT establish
    sigma-equal => menus-equal.  **(H1) IS NOT REDUCED IN THE CLAIMED
    DIRECTION**, and the committed `sigma` — never loaded by the first
    draft — is loaded here and the comparison made.  MV4's (H2) claim
    falls the same way, and d44a already had BOTH results verbatim, two
    depths deeper.
  * BLOCKER 2 — MV2's stated MECHANISM cannot happen.  An actor's own
    live proposals are ALWAYS in its own noop cone (`regs_of` of a
    propose by `a` is `{a}`), so the "own-proposal exclusion" clause is
    operative in neither fibre element.  **The real mechanism is MISSED
    SUPERSESSION**: a lagged view does not know its base has been
    superseded.  Witnesses for both fibre elements are printed.
  * MAJOR 1 — the reduction reads a FIFTH thing: `view.pred`, through
    `incomparable()` -> `edges()` -> `mis_of` (admissibility) and `PK1`
    (the weight).  It is inert at this scope, but by a theorem the first
    draft never stated, and that theorem is (H0)'s fourth clause.
    "[STRUCTURAL, exact]" becomes "exact GIVEN (H0)", declared.
  * MAJOR 2 — MV1's headline surprise is FORCED by `regs_of`: a propose
    candidate's view IS its actor's noop cone, so "p candidates lag too"
    is the idle lag recounted.  And pin §5 dies on its own premise in
    thousands of exhibited cases — a cleaner refutation than the claimed
    one.
  * MAJOR 3 — MV2's preamble asserted the negation of the gate above it
    and licensed testing only the idle 2-bit pair; the `'r'` branch is
    tested here.
  * MINOR 1 — the depth-5 cap is lifted: MV3/MV4 now run to depth 7,
    which is what the pin asked for.
  * MINOR 2/3 — MV5 now implements the PINNED mutant (opponent-authored
    drop) alongside the committed protocol and an exhaustive one, and
    gates the pin's "> 0", not an invented 50% bar.
  * MINOR 4 — dead variables removed; the MV1 witness is PRINTED.
  * MINOR 5 — the theorem-passes are labelled as such.
  * MINOR 6 — `sigma` is loaded from the committed d44a source, as the
    pin promised.
  * MINOR 7 — MV1/MV2 no longer gate the author's negative findings.
  * MINOR 8 — "MV3 is the menu-level form of MV1+MV2" is withdrawn.
  * NIT 1 — result note written (`note-d51-h1-menu-visibility-result.md`).
  * NIT 2 — MV0's census is a complete trichotomy; stated.

THE STRUCTURAL READING (pin §2), read from the committed layer:
`admissible(acts, e)` builds `View(acts+[e], pred, pred[j])` — the
CANDIDATE EVENT'S OWN CAUSAL PAST — and the menu reads that view through
FOUR PROJECTIONS: holdings(a), superseded, live/props, components(), plus
the FIFTH read MAJOR 1 names.  What (H1) needs is a statement about
SIGMA; what this receipt establishes is a statement about the
projections, which are strictly finer.

The refuted route (D46a: tau as an own-view object) is NOT re-walked.

Exit 1 ONLY on anchor breakage or mutant misbehaviour.  Every
substantive outcome — including MV-FAIL, which would refute (H1) — is an
exit-0 deliverable.

Run from the repo root: python3 v10/code/d51_menu_visibility_exact.py
"""
import ast
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import permutations

sys.setrecursionlimit(300000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D51 — (H1) via MENU-VISIBILITY, ROUND-1 REPAIRED]")
print("  banner: the admission layer's view is the CANDIDATE's own causal")
print("  past, and the menu reads it through four projections PLUS a")
print("  fifth read (view.pred, MAJOR 1).  **Round 1 inverted the")
print("  headline: those projections REFINE sigma (209 keys vs 32 sigma")
print("  states), so equal-projections => equal-menus does NOT give")
print("  equal-sigma => equal-menus.**  D46a's refuted own-view route is")
print("  NOT re-walked.  Depths are PRINTED and now run to 7.  Scope:")
print("  d42a, DELIVERY-FREE, two actors (D44b's boundary).")

# ------------------------------------------------------------------ MV0
print("\n[MV0 anchor + capacity]")
_SRC = 'v10/code/d42b3_placement_exact.py'
_D44A = 'v10/code/d44a_closure_theorem_exact.py'
_s = open(_SRC).read()
ns = {}
exec(compile(_s[:_s.index('print("[d42b3')], 'd42b3_ported', 'exec'), ns)
candidates_for = ns['candidates_for']
admissible = ns['admissible']
event_poset = ns['event_poset']
View = ns['View']
prop_options_in_view = ns['prop_options_in_view']
arb_components_in_view = ns['arb_components_in_view']
edge_triples_of = ns['edge_triples_of']
triples = ns['triples']
mis_of = ns['mis_of']
PK1 = ns['PK1']
regs_of = ns['regs_of']
AB = ('A', 'B')

# ROUND-1 MINOR 6 / BLOCKER 1: sigma and the canonical renamed menu,
# extracted VERBATIM by text slice from the committed d44a receipt — the
# pin promised this and the committed receipt never did it, which is the
# omission that made BLOCKER 1 possible.
_ds = open(_D44A).read()
_blk1 = _ds[_ds.index("SG_VIOL = {'alive'"):_ds.index("\nSIG = {tuple(h)")]
_blk2 = _ds[_ds.index("def _rename_event(e, m2):"):
            _ds.index("\ngroups = defaultdict(list)")]
ns['AB'] = AB
ns['permutations'] = permutations
ns['defaultdict'] = defaultdict
_CUR = {}
def cands_of(hk):
    if hk in _CUR:
        return _CUR[hk]
    return candidates_for(list(hk), AB)
ns['cands_of'] = cands_of
exec(compile(_blk1, 'd44a_sigma_port', 'exec'), ns)
exec(compile(_blk2, 'd44a_menu_port', 'exec'), ns)
canon_sigma = ns['canon_sigma']
canon_menu = ns['canon_menu']
SG_VIOL = ns['SG_VIOL']

check("MV0(a) [ANCHOR / SMOKE TEST, labelled per round-1 MINOR 5] the "
      "admission layer is exec'd path-anchored from the committed d42b3 "
      "receipt (single source) and **the committed sigma and canonical "
      "renamed menu are extracted VERBATIM by text slice from the "
      "committed d44a receipt** — the pin §4 MV0 promise the first draft "
      "dropped, and the omission that let BLOCKER 1 through.  This gate "
      "checks LOADING only; it is a callable() test and nothing more",
      all(callable(f) for f in (candidates_for, admissible,
                                prop_options_in_view,
                                arb_components_in_view, canon_sigma,
                                canon_menu))
      and "def sigma_raw(hk):" in _blk1
      and "def canon_menu(hk):" in _blk2,
      f"layer = {_SRC}; sigma/menu = {_D44A} ({len(_blk1)}B, "
      f"{len(_blk2)}B)")


def dk(o):
    """Deterministic key (D49's A4 lesson: raw frozenset reprs are
    hash-order dependent and produced spurious mismatches)."""
    if isinstance(o, frozenset):
        return ('fs', tuple(sorted((dk(x) for x in o), key=repr)))
    if isinstance(o, (tuple, list)):
        return tuple(dk(x) for x in o)
    return o


def view_of_candidate(acts, e):
    """Exactly what admissible() builds."""
    acts2 = list(acts) + [e]
    j = len(acts2) - 1
    pred = event_poset(acts2)
    return View(acts2, pred, pred[j]), pred[j]


def full_view(acts):
    pred = event_poset(list(acts))
    return View(list(acts), pred, set(range(len(acts))))


def projections(view, a):
    """The FOUR projections named in the pin.  ROUND-1 MAJOR 1: this is
    NOT everything the menu reads — `view.pred` is read through
    incomparable() -> edges() -> mis_of/PK1.  That fifth read is inert at
    this scope, but only by (H0)'s fourth clause; see MV7."""
    hold = tuple(sorted((dk(b) for b in view.holdings(a)), key=repr))
    sup = tuple(sorted((dk(b) for b in view.superseded), key=repr))
    live = tuple(sorted((dk((op[1], op[2], op[3]))
                         for op in view.live.values()), key=repr))
    craw = []
    for base, comp in view.components():
        mem = tuple(sorted(((view.props[i][1], view.props[i][2],
                             view.props[i][3]) for i in comp), key=repr))
        craw.append(dk((base, mem)))
    comps = tuple(sorted(craw, key=repr))
    return (hold, sup, live, comps)


# enumerate the family
CAP = 5
FAM = [[]]
frontier = [[]]
CACHE = {}
while frontier:
    h = frontier.pop()
    CACHE[tuple(h)] = candidates_for(h, AB)
    if len(h) >= CAP:
        continue
    for e, q in CACHE[tuple(h)]:
        FAM.append(h + [e])
        frontier.append(h + [e])
BYLEN = defaultdict(list)
for h in FAM:
    BYLEN[len(h)].append(tuple(h))
print(f"  family enumerated to depth {CAP}: "
      f"{ {L: len(BYLEN[L]) for L in sorted(BYLEN)} }, total {len(FAM)}")

# ------------------------------------------------- MV0(sigma) BLOCKER 1
print("\n[MV0(sigma) THE COMPARISON THE FIRST DRAFT NEVER MADE — "
      "round-1 BLOCKER 1]")
SIG = {tuple(h): canon_sigma(tuple(h)) for h in FAM}
KEY = {tuple(h): tuple(projections(full_view(h), a) for a in AB)
       for h in FAM}
k2s, s2k = defaultdict(set), defaultdict(set)
for h in FAM:
    hk = tuple(h)
    k2s[KEY[hk]].add(SIG[hk])
    s2k[SIG[hk]].add(KEY[hk])
k_multi = sum(1 for v in k2s.values() if len(v) > 1)
s_multi = sum(1 for v in s2k.values() if len(v) > 1)
print(f"  distinct committed-sigma states on the depth-{CAP} family = "
      f"{len(s2k)}")
print(f"  distinct D51 projection keys                          = "
      f"{len(k2s)}")
print(f"  D51 key determines sigma?   keys with >1 sigma state  = "
      f"{k_multi}    <- {'REFINES sigma' if k_multi == 0 else 'no'}")
print(f"  sigma determines D51 key?   sigma states with >1 key  = "
      f"{s_multi}   <- {'all of them, strictly' if s_multi == len(s2k) else ''}")
check("MV0(sigma) [THE CORRECTION THAT INVERTS THE HEADLINE] **THE FOUR "
      "PROJECTIONS REFINE sigma; THEY ARE NOT AN ABSTRACTION OF IT.**  "
      "The committed VERDICT said 'sigma IS an abstraction of exactly "
      "those projections, [so] menus are sigma-determined here'.  "
      "'sigma is an abstraction of the projections' means "
      "projections => sigma, so MV3's projections-equal => menus-equal "
      "is IMPLIED BY sigma-determination, not the converse.  Measured "
      "here: every projection key determines its sigma state, and EVERY "
      "sigma state carries more than one projection key.  (H1) is NOT "
      "reduced in the claimed direction",
      k_multi == 0 and s_multi == len(s2k) and len(k2s) > len(s2k),
      f"projection keys = {len(k2s)}, sigma states = {len(s2k)}; keys "
      f"with >1 sigma = {k_multi}; sigma states with >1 key = {s_multi} "
      f"of {len(s2k)}; sigma invariants clean = "
      f"{all(v == 0 for v in SG_VIOL.values())}")

# capacity: does the menu view actually EXCEED the noop cone?
exceed = same = less = incomp = 0
extras_max = 0
opp_only = True
by_kind_view = defaultdict(lambda: [0, 0])
p_is_cone = [0, 0]
for h in FAM:
    for a in AB:
        _, cone = view_of_candidate(h, ('n', a))
        for e, q in CACHE[tuple(h)]:
            if e[1] != a or e[0] == 'n':
                continue
            _, mv = view_of_candidate(h, e)
            by_kind_view[e[0]][1] += 1
            if e[0] == 'p':
                p_is_cone[1] += 1
                if set(mv) == set(cone):
                    p_is_cone[0] += 1
            if set(mv) > set(cone):
                exceed += 1
                by_kind_view[e[0]][0] += 1
                ex = set(mv) - set(cone)
                extras_max = max(extras_max, len(ex))
                for i in ex:
                    if h[i][1] == a:
                        opp_only = False
            elif set(mv) == set(cone):
                same += 1
            elif set(mv) < set(cone):
                less += 1
            else:
                incomp += 1
print(f"  menu view vs noop cone: strictly exceeds in {exceed} "
      f"(actor, candidate) pairs, equal in {same}, strictly less in "
      f"{less}, incomparable in {incomp}; max extra events {extras_max}")
print(f"  TRICHOTOMY IS COMPLETE (round-1 NIT 2): {exceed} + {same} + "
      f"{less} + {incomp} = {exceed + same + less + incomp} = "
      f"{ {k: v[1] for k, v in sorted(by_kind_view.items())} } summed")
_own_in_cone = 0
_own_tot = 0
_init_in_regs = 0
for h in FAM:
    for a in AB:
        _, cone = view_of_candidate(h, ('n', a))
        for i in range(len(h)):
            if h[i][1] == a:
                _own_tot += 1
                if i in cone:
                    _own_in_cone += 1
    for e, q in CACHE[tuple(h)]:
        if e[1] in regs_of(e):
            _init_in_regs += 1
check("MV0(b) CAPACITY — the lag is REAL and NON-EMPTY, so the question "
      "is not vacuous.  **ROUND-1 MINOR 5: the 'all extras are "
      "OPPONENT-AUTHORED' clause is a THEOREM-PASS, not a finding** — "
      "every event's initiator lies in its own register set, so every "
      "a-authored event of h is inside a's noop cone as a theorem of "
      "`event_poset`, and an extra can never be a-authored.  It is "
      "labelled here rather than reported as a discovery",
      exceed > 0 and opp_only,
      f"exceeding pairs = {exceed}, equal = {same}, max extras = "
      f"{extras_max}; the theorem behind opp_only: initiator in "
      f"regs_of(e) on {_init_in_regs}/"
      f"{sum(len(CACHE[tuple(h)]) for h in FAM)} menu-offered events, "
      f"a-authored events inside a's cone {_own_in_cone}/{_own_tot}")

# ------------------------------------------------------------------ MV1
print("\n[MV1 MV-STRONG — do the candidate's projections EQUAL the full "
      "view's?]")
by_kind = defaultdict(lambda: [0, 0])
first_diff = None
for h in FAM:
    fv = full_view(h)
    for e, q in CACHE[tuple(h)]:
        a = e[1]
        cv, _ = view_of_candidate(h, e)
        pc, pf = projections(cv, a), projections(fv, a)
        k = e[0]
        by_kind[k][0] += 1
        if pc == pf:
            by_kind[k][1] += 1
        elif first_diff is None:
            first_diff = (list(h), e, pc, pf)
for k in sorted(by_kind):
    t, s = by_kind[k]
    print(f"  event type '{k}': {s}/{t} candidates whose own-view "
          f"projections EQUAL the full view's")
if first_diff is not None:
    print(f"  [WITNESS MV-STRONG-FAILS] (round-1 MINOR 4: the committed "
          f"receipt computed this witness and never printed it)")
    print(f"      h = {first_diff[0]}")
    print(f"      candidate = {first_diff[1]}")
    for nm, pr in (('candidate view', first_diff[2]),
                   ('full view     ', first_diff[3])):
        print(f"      {nm}: holdings={pr[0]} superseded={pr[1]}")
        print(f"      {' ' * len(nm)}  live={pr[2]} comps={pr[3]}")
# ROUND-1 MAJOR 2: the 'p' surprise is FORCED by regs_of
print(f"  ROUND-1 MAJOR 2 — the headline surprise is FORCED: "
      f"regs_of(('p',a,b,x)) = {{a}} = regs_of(('n',a)), so a propose "
      f"candidate's view IS its actor's noop cone in "
      f"{p_is_cone[0]}/{p_is_cone[1]} cases.  'p candidates lag too' is "
      f"the IDLE lag recounted with different multiplicities, not a "
      f"second refutation, and pin §2's 'a propose additionally pulls in "
      f"the wires the event touches' is false.")
print(f"      views strictly exceeding the cone, by kind: "
      f"{ {k: v[0] for k, v in sorted(by_kind_view.items())} }")
# ROUND-1 MAJOR 2: pin §5's own premise fails
prem = defaultdict(lambda: [0, 0])
for h in FAM:
    fv = full_view(h)
    for e, q in CACHE[tuple(h)]:
        if e[0] not in ('p', 'r'):
            continue
        cv, idxs = view_of_candidate(h, e)
        base = e[2] if e[0] == 'p' else next(iter(e[2]))[1]
        want = {i for i, op in fv.live.items() if op[2] == base}
        prem[e[0]][1] += 1
        if want <= set(idxs):
            prem[e[0]][0] += 1
print(f"  ROUND-1 MAJOR 2 — pin §5 dies on its OWN premise ('pred[e] "
      f"contains every live proposal on the base b the candidate "
      f"touches'): proposals are carried on the PROPOSER's register, not "
      f"the base wire, and a propose does not touch wire b at all.")
for k in sorted(prem):
    g, t = prem[k]
    print(f"      '{k}' candidates: {g}/{t}   MISSES {t - g}")
check("MV1 [REPORTING GATE — round-1 MINOR 7: a gate must not assert the "
      "author's own negative] MV-STRONG measured by event type, reported "
      "in whichever direction it landed.  The pin (§3) pre-registered "
      "MV-STRONG as failing for IDLES and HOLDING for propose/arbitrate "
      "on a wire-closure argument.  **The measurement refutes that, and "
      "round 1 shows the refutation is cheaper than claimed: the 'p' "
      "result is FORCED by regs_of, and the pinned §5 premise is false "
      "outright in the exhibited cases above.**  The pin's §5 depth-free "
      "sketch is damaged and is NOT quietly dropped",
      sum(v[0] for v in by_kind.values()) > 0,
      f"by type (equal/total): "
      f"{ {k: f'{v[1]}/{v[0]}' for k, v in sorted(by_kind.items())} }; "
      f"'p' candidate view == its actor's noop cone in "
      f"{p_is_cone[0]}/{p_is_cone[1]}; pin §5 premise misses "
      f"{ {k: prem[k][1] - prem[k][0] for k in sorted(prem)} }")

# ------------------------------------------------------------------ MV2
print("\n[MV2 the 2-bit idle proxy, and its ACTUAL mechanism]")
print("  ROUND-1 MAJOR 3: the committed receipt printed, directly under")
print("  MV1's own output, 'MV1 shows p/r candidates read the full-view")
print("  values, so those are sigma-determined outright' — the NEGATION")
print("  of the gate above it, and the sole justification for testing")
print("  only the idle pair.  The 'r' branch is tested below.")
idle_sig = defaultdict(set)
WIT = {}
for h in FAM:
    fv = full_view(h)
    for a in AB:
        cv, _ = view_of_candidate(h, ('n', a))
        hp = bool(prop_options_in_view(cv, a))
        hr = bool(arb_components_in_view(cv, a))
        hp_f = bool(prop_options_in_view(fv, a))
        hr_f = bool(arb_components_in_view(fv, a))
        idle_sig[(hp_f, hr_f)].add((hp, hr))
        k = ((hp_f, hr_f), (hp, hr))
        if (hp_f, hr_f) != (hp, hr) and (k not in WIT
                                         or len(h) < len(WIT[k][0])):
            WIT[k] = (list(h), a)
print(f"  full-view (has_p, has_r) -> set of cone-level values observed:")
for k in sorted(idle_sig):
    print(f"    {k} -> {sorted(idle_sig[k])}")
print("  [WITNESSES — round-1 BLOCKER 2: the committed receipt printed "
      "NONE, and its stated mechanism is refuted]")
for k in sorted(WIT):
    hh, a = WIT[k]
    print(f"    full {k[0]} -> cone {k[1]}:  actor {a}, h = {hh}")
_own_live_same = [0, 0]
for h in FAM:
    fv = full_view(h)
    for a in AB:
        cv, _ = view_of_candidate(h, ('n', a))
        own_c = {i for i, op in cv.live.items() if op[1] == a}
        own_f = {i for i, op in fv.live.items() if op[1] == a}
        _own_live_same[1] += 1
        if own_c == own_f:
            _own_live_same[0] += 1
opt_eq = opt_more = opt_fewer = 0
for h in FAM:
    fv = full_view(h)
    for a in AB:
        cv, _ = view_of_candidate(h, ('n', a))
        oc = set(prop_options_in_view(cv, a))
        of = set(prop_options_in_view(fv, a))
        if oc == of:
            opt_eq += 1
        elif oc > of:
            opt_more += 1
        elif oc < of:
            opt_fewer += 1
print(f"  THE COMMITTED MECHANISM IS REFUTED: an actor's OWN live "
      f"proposals are identical in the noop cone and the full view in "
      f"{_own_live_same[0]}/{_own_live_same[1]} (actor, history) pairs — "
      f"regs_of(('p',a,b,x)) = {{a}}, so every proposal by a lies on a's "
      f"own register chain.  The 'own-proposal exclusion' clause is "
      f"operative in NEITHER fibre element.")
print(f"  THE ACTUAL MECHANISM IS MISSED SUPERSESSION: a lagged view "
      f"does not know its base has been superseded (witness 1: B "
      f"self-arbitrates, A's empty cone still offers the base), and it "
      f"does not know an opponent's ARB has resolved a proposal it can "
      f"still see (witness 2).")
print(f"  THE CONCLUSION SURVIVES, re-established on OPTION SETS rather "
      f"than the two bits: over {opt_eq + opt_more + opt_fewer} "
      f"(h, actor) pairs the cone's proposal options are equal in "
      f"{opt_eq}, STRICTLY MORE in {opt_more}, strictly fewer in "
      f"{opt_fewer}.  **A SMALLER VIEW CAN YIELD MORE OPTIONS**, so any "
      f"argument assuming a lagged view sees a subset is wrong.")
idle_determined = all(len(v) == 1 for v in idle_sig.values())
check("MV2 [REPORTING GATE — round-1 MINOR 7] THE 2-BIT PROXY IS NOT A "
      "FUNCTION OF THE FULL-VIEW PAIR, reported as the negative it is, "
      "with its MECHANISM **CORRECTED BY ROUND 1** (BLOCKER 2): the "
      "committed text blamed the own-proposal exclusion, which cannot "
      "happen; the obstruction is that a LAGGED VIEW DOES NOT KNOW ITS "
      "BASE HAS BEEN SUPERSEDED — much harder, and precisely what LOG "
      "#432 later hit at transport.  Monotonicity fails in the direction "
      "printed above.  This does NOT refute (H1): sigma records far more "
      "than these two bits",
      len(idle_sig) > 0 and opt_more > 0 and opt_fewer == 0,
      f"map = { {k: sorted(v) for k, v in sorted(idle_sig.items())} }; "
      f"idle-determined = {idle_determined}; option sets: equal "
      f"{opt_eq}, cone strictly more {opt_more}, cone strictly fewer "
      f"{opt_fewer}; own live proposals identical "
      f"{_own_live_same[0]}/{_own_live_same[1]}")

# ------------------------------------------------------- MV2b the 'r' arm
print("\n[MV2b THE 'r' ARM — round-1 MAJOR 3: never tested by the "
      "committed receipt]")
r_sig = defaultdict(set)
for h in FAM:
    fv = full_view(h)
    for e, q in CACHE[tuple(h)]:
        if e[0] != 'r':
            continue
        a = e[1]
        cv, _ = view_of_candidate(h, e)
        kc = (tuple(sorted((dk(triples(cv, c[1])) for c in
                            arb_components_in_view(cv, a)), key=repr)),
              tuple(sorted((dk(edge_triples_of(cv, c[1])) for c in
                            arb_components_in_view(cv, a)), key=repr)))
        kf = (tuple(sorted((dk(triples(fv, c[1])) for c in
                            arb_components_in_view(fv, a)), key=repr)),
              tuple(sorted((dk(edge_triples_of(fv, c[1])) for c in
                            arb_components_in_view(fv, a)), key=repr)))
        r_sig[kf].add(kc)
r_multi = sum(1 for v in r_sig.values() if len(v) > 1)
check("MV2b THE ARBITRATION ARM, TESTED.  An 'r' candidate's view is a "
      "larger object than the idle cone and runs through "
      "arb_components_in_view, mis_of and PK1 — the committed receipt's "
      "collapse onto the idle 2-bit pair left it untested, on a preamble "
      "that contradicted its own MV1 output.  Measured here: the "
      "full-view arbitration data (component member-triples AND the "
      "edge triples the weight is computed from) against the candidate "
      "view's, reported whichever way it lands",
      len(r_sig) > 0,
      f"distinct full-view arb keys = {len(r_sig)}; keys carrying more "
      f"than one candidate-view value = {r_multi} -> "
      + ("the 'r' arm is full-view-determined at this scope"
         if r_multi == 0 else
         "the 'r' arm LAGS too, and the committed preamble was unsound "
         "for it"))

# ------------------------------------------------------------------ MV5
print("\n[MV5 mutant — can the instrument see the lag at all?]")


def mutant_scan(protocol):
    """protocol: 'committed' (first 'r' per history, lowest-indexed
    proposal, no author test — what the receipt actually ran),
    'exhaustive' (every 'r' candidate, same drop rule), or 'pinned' (the
    pin's probe: drop an OPPONENT-authored proposal)."""
    tested = changed = own = 0
    for h in FAM:
        if len(h) < 2:
            continue
        for e, q in CACHE[tuple(h)]:
            if e[0] != 'r':
                continue
            cv, mv = view_of_candidate(h, e)
            if not mv:
                continue
            acts2 = list(h) + [e]
            pred = event_poset(acts2)
            j = len(acts2) - 1
            hidden = set(pred[j])
            if protocol == 'pinned':
                drop = next((i for i in sorted(hidden)
                             if h[i][0] == 'p' and h[i][1] != e[1]), None)
            else:
                drop = next((i for i in sorted(hidden)
                             if h[i][0] == 'p'), None)
            if drop is None:
                continue
            tested += 1
            if h[drop][1] == e[1]:
                own += 1
            vw = View(acts2, pred, hidden - {drop})
            if projections(vw, e[1]) != projections(cv, e[1]):
                changed += 1
            if protocol == 'committed':
                break
    return tested, changed, own


MUT = {p: mutant_scan(p) for p in ('committed', 'exhaustive', 'pinned')}
for p in ('committed', 'exhaustive', 'pinned'):
    t, c, o = MUT[p]
    print(f"  {p:11s}: tested = {t:5d}  changed = {c:5d} "
          f"({100 * c // max(t, 1)}%)  dropped proposal authored by the "
          f"candidate's OWN actor: {o}")
mut_tested, mut_changed, _ = MUT['pinned']
check("MV5 THE INSTRUMENT IS NOT BLIND — **and the mutant is now the "
      "PINNED one** (round-1 MINOR 2: the committed protocol dropped the "
      "LOWEST-INDEXED proposal with no author test and broke after the "
      "first 'r' candidate, so in 82% of cases it hid the candidate's "
      "OWN proposal — the opposite of the pinned probe — and its '63%' "
      "was a sampling artefact quoted three times as if it "
      "characterised the object).  **The gate is the pin's own "
      "'must CHANGE some menu' (> 0)**, not the invented 50% bar that "
      "sat just under an observed 63% (round-1 MINOR 3).  The partial "
      "rate is reported for all three protocols: when the dropped "
      "proposal is on a base the candidate's projections do not reach, "
      "nothing moves",
      mut_tested > 0 and mut_changed > 0,
      f"PINNED mutant: tested = {mut_tested}, changed = {mut_changed} "
      f"({100 * mut_changed // max(mut_tested, 1)}%); committed protocol "
      f"{MUT['committed'][1]}/{MUT['committed'][0]}; exhaustive "
      f"{MUT['exhaustive'][1]}/{MUT['exhaustive'][0]}")

# --------------------------------------------------------- MV3 / MV4
print("\n[MV3 + MV4 at the PROJECTION level, depths 5, 6 and 7 — round-1 "
      "MINOR 1: the committed CAP = 5 was hard-coded against the pin's "
      "explicit instruction to beat d44a's depth 7]")
DEEP = {}
for D in (5, 6, 7):
    fam = [[]]
    fr2 = [[]]
    cache = {}
    while fr2:
        h = fr2.pop()
        cache[tuple(h)] = candidates_for(h, AB)
        if len(h) >= D:
            continue
        for e, q in cache[tuple(h)]:
            fam.append(h + [e])
            fr2.append(h + [e])
    keys = {}
    byproj = defaultdict(set)
    for h in fam:
        hk = tuple(h)
        keys[hk] = tuple(projections(full_view(h), a) for a in AB)
        byproj[keys[hk]].add(tuple(sorted(((dk(e), q)
                                           for e, q in cache[hk]),
                                          key=repr)))
    trans = defaultdict(set)
    for h in fam:
        hk = tuple(h)
        if len(h) >= D:
            continue
        for e, q in cache[hk]:
            trans[(keys[hk], dk(e))].add(keys[hk + (e,)])
    v3 = sum(1 for v in byproj.values() if len(v) > 1)
    v4 = sum(1 for v in trans.values() if len(v) > 1)
    DEEP[D] = (len(fam), len(byproj), v3, len(trans), v4)
    print(f"  depth {D}: histories {len(fam):6d}   MV3 keys {len(byproj):5d} "
          f"violations {v3}   MV4 (state, event) pairs {len(trans):5d} "
          f"violations {v4}")
check("MV3 [EVIDENCE, never a premise] EQUAL FULL-VIEW PROJECTIONS => "
      "EQUAL MENUS, with exact weights, over every history to depth 7: "
      "zero violations.  **ROUND-1 BLOCKER 1 / MINOR 8: this is NOT the "
      "menu-level form of MV1+MV2** (MV3 reads only FULL views; MV1/MV2 "
      "are about CANDIDATE views, and neither implies the other), and it "
      "does NOT give sigma-determination, because the projections REFINE "
      "sigma (MV0(sigma)).  What it establishes is the PROJECTION "
      "reduction of the MENU function, at finite depth",
      all(DEEP[D][2] == 0 for D in DEEP) and DEEP[7][1] > DEEP[5][1],
      f"(depth, histories, keys, violations) = "
      f"{[(D, DEEP[D][0], DEEP[D][1], DEEP[D][2]) for D in sorted(DEEP)]}")

print("\n[MV3b (H1) AND (H2) WITH THE COMMITTED sigma — what the unit "
      "actually adds over its parent]")
MEN = {tuple(h): canon_menu(tuple(h)) for h in FAM}
h1_by_sig = defaultdict(set)
for h in FAM:
    hk = tuple(h)
    h1_by_sig[SIG[hk]].add(MEN[hk])
h1_viol = sum(1 for v in h1_by_sig.values() if len(v) > 1)
h2_by = defaultdict(set)
for h in FAM:
    hk = tuple(h)
    if len(h) >= CAP:
        continue
    for e, q in CACHE[hk]:
        h2_by[(SIG[hk], dk(e))].add(SIG[hk + (e,)])
h2_viol = sum(1 for v in h2_by.values() if len(v) > 1)
print(f"  (H1) depth<={CAP}, COMMITTED sigma, RENAMED menus with exact "
      f"weights: sigma states = {len(h1_by_sig)}, states carrying >1 "
      f"renamed menu = {h1_viol}")
print(f"  (H2) depth<={CAP}, COMMITTED sigma + event in its raw "
      f"deterministic key (NOT d44a's renamed form — a strictly FINER "
      f"key, so this is WEAKER than d44a's CG2, which is exactly the "
      f"point): keys = {len(h2_by)}, keys with >1 successor sigma = "
      f"{h2_viol}")
check("MV3b [SUBSUMED BY THE PARENT, stated] (H1) and (H2) hold on this "
      "family under the COMMITTED sigma — but these are d44a's results "
      "at a SHALLOWER depth.  d44a's CG1 IS (H1) verbatim (34,375 "
      "histories, 36 sigma-classes, zero exceptions; CG7b extends to "
      "145,408 depth-7 transitions) and CG2 IS (H2) verbatim, so the "
      "committed MV4 label — '(H2) IS SETTLED HERE, not left dangling as "
      "d44a left it' — is FALSE ABOUT d44a's RECEIPT.  What d44a left "
      "open is the LOGICAL question, which its note answers in the "
      "OPPOSITE direction ((H2) is NOT a consequence of (H1)).  D51's "
      "positive content is strictly subsumed by its own parent — and the "
      "(H2) key used here is FINER than d44a's (raw event key, not the "
      "renamed one), so even this is a weaker statement than CG2's",
      h1_viol == 0 and h2_viol == 0 and len(h1_by_sig) == 32,
      f"sigma states = {len(h1_by_sig)}, (H1) violations = {h1_viol}; "
      f"(H2) keys = {len(h2_by)}, violations = {h2_viol}")

check("MV4 [RESTATED BY ROUND 1] the successor PROJECTION state is a "
      "function of (projection state, event) — zero violations to depth "
      "7.  **This is a statement about projections, not about sigma**: "
      "key(h) -> key(h+e) says nothing about sigma(h) -> sigma(h+e), "
      "because sigma(h) does not determine key(h) (MV0(sigma)).  The "
      "committed claim that this SETTLES (H2) is withdrawn; MV3b carries "
      "the sigma-level statement, and it is d44a's, two depths deeper",
      all(DEEP[D][4] == 0 for D in DEEP),
      f"(depth, pairs, violations) = "
      f"{[(D, DEEP[D][3], DEEP[D][4]) for D in sorted(DEEP)]}")

# ------------------------------------------------------------------ MV7
print("\n[MV7 THE FIFTH READ — round-1 MAJOR 1]")
print("  Every View access on the admission-and-enumeration path:")
print("    prop_options_in_view  : holdings(a), superseded, live")
print("    arb_components_in_view: components(), superseded, props")
print("    View.components       : live, edges()")
print("    View.edges            : props, incomparable() -> self.pred")
print("    triples/edge_triples_of ('r'): props, edges() -> self.pred")
print("    candidates_for        : full.arbs, full.live, full.props")
print("  `edge_triples_of` feeds `mis_of` (an ADMISSIBILITY test) and")
print("  `PK1(...)[wkey]` (the WEIGHT).  `components()` records only the")
print("  PARTITION; the edge set inside a component is strictly finer,")
print("  and `projections()` drops it.  The omitted read is where the")
print("  weights live.")
views = 0
same_base_pairs = 0
comparable_pairs = 0
compsizes = defaultdict(int)
edgekeys = defaultdict(set)
for h in FAM:
    vlist = [full_view(h)]
    for e, q in CACHE[tuple(h)]:
        vlist.append(view_of_candidate(h, e)[0])
    for a in AB:
        vlist.append(view_of_candidate(h, ('n', a))[0])
    for vw in vlist:
        views += 1
        li = sorted(vw.live.items())
        for i in range(len(li)):
            for j in range(i + 1, len(li)):
                (i1, o1), (i2, o2) = li[i], li[j]
                if o1[2] != o2[2]:
                    continue
                same_base_pairs += 1
                if not vw.incomparable(i1, i2):
                    comparable_pairs += 1
        for base, comp in vw.components():
            compsizes[len(comp)] += 1
            edgekeys[(dk(base), dk(triples(vw, comp)))].add(
                dk(edge_triples_of(vw, comp)))
ek_multi = sum(1 for v in edgekeys.values() if len(v) > 1)
print(f"  views inspected = {views}; same-base live-proposal pairs = "
      f"{same_base_pairs}, COMPARABLE ones = {comparable_pairs}")
print(f"  component sizes seen = {dict(sorted(compsizes.items()))}")
print(f"  (base, member-triples) keys = {len(edgekeys)}; keys carrying "
      f"MORE THAN ONE edge set = {ek_multi}")
check("MV7 [DECLARED: EXACT **GIVEN (H0)**, not exact simpliciter] THE "
      "REDUCTION READS A FIFTH THING — `view.pred`, via incomparable() "
      "-> edges() -> mis_of and PK1 — and `projections()` drops it.  At "
      "this scope it is INERT, but by a theorem the committed receipt "
      "never stated, and that theorem is verbatim (H0)'s fourth clause: "
      "same-base live proposals are never comparable, so the edge set "
      "inside a component is determined by its membership.  The "
      "committed sigma records the edge set E EXPLICITLY, so d44a judged "
      "it necessary; D51 drops it without argument.  '[STRUCTURAL, "
      "exact]' must read 'exact GIVEN (H0)'",
      comparable_pairs == 0 and ek_multi == 0 and views > 0,
      f"views {views}; same-base live pairs {same_base_pairs}, "
      f"comparable {comparable_pairs}; (base, members) keys "
      f"{len(edgekeys)}, keys with >1 edge set {ek_multi}")

# ------------------------------------------------------------------ MV6
print("\n[MV6 anti-vacuity]")
_self = ast.parse(open('v10/code/d51_menu_visibility_exact.py').read())
_bound = set()
for _n in ast.walk(_self):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, ast.FunctionDef):
        _bound.add(_n.name)
        for _a in _n.args.args:
            _bound.add(_a.arg)
_ch = [c for c in ast.walk(_self) if isinstance(c, ast.Call)
       and isinstance(c.func, ast.Name) and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)
        or not ({x.id for x in ast.walk(c.args[1])
                 if isinstance(x, ast.Name)} & _bound)]
check("MV6 every check() predicate references a run-bound name and none "
      "is a bare constant.  SCOPE (LOG #403 MA-2): exactly that and "
      "nothing more; falsifiability is MV5's job, and round 1's finding "
      "that MV0(b)'s opponent-only clause is a theorem-pass is the "
      "scan's declared blind spot — it is LABELLED there instead",
      len(_ch) >= 9 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

# ============================== verdict ==================================
print("\n[VERDICT — D51, ROUND-1 REPAIRED]")
print("  **WHAT IS ESTABLISHED.**  EQUAL FULL-VIEW PROJECTIONS GIVE "
      "EQUAL MENUS with exact weights, over every history to depth 7 "
      f"({DEEP[7][0]} histories, {DEEP[7][1]} projection keys, zero "
      "violations) — the PROJECTION reduction of the MENU function, at "
      "finite depth, and GIVEN (H0) for the fifth read (MV7).")
print("  **WHAT IS NOT ESTABLISHED, and was claimed.**  The four "
      f"projections REFINE sigma — {len(k2s)} keys against {len(s2k)} "
      "sigma states, every sigma state carrying more than one key — so "
      "'sigma is an abstraction of exactly those projections' is "
      "BACKWARDS and MV3 does NOT give sigma-equal => menus-equal.  "
      "**(H1) IS NOT REDUCED IN THE CLAIMED DIRECTION.**  The same "
      "inversion voids the committed MV4 reading of (H2).")
print("  **WHAT THE UNIT'S POSITIVE CONTENT ACTUALLY IS.**  (H1) and "
      "(H2) under the committed sigma DO hold here (MV3b) — but they are "
      "d44a's CG1/CG2 at a shallower depth, so D51's positive content is "
      "strictly subsumed by its own parent.  What d44a left open is the "
      "LOGICAL question, and its note answers that in the opposite "
      "direction.")
print("  **THE DURABLE CONTENT IS THE REFUTATIONS.**  MV-STRONG fails "
      "for every event type; the 'p' case is FORCED by regs_of and the "
      "pinned §5 premise is false outright (MAJOR 2).  MONOTONICITY "
      "FAILS — a smaller view yields MORE proposal options — and the "
      "mechanism is MISSED SUPERSESSION, not the own-proposal exclusion "
      "the committed text named (BLOCKER 2, witnesses printed).  Any "
      "depth-free argument built on 'the lagged view sees a subset' is "
      "unsound, and the pin's §5 sketch is one of those.")
print("  SCOPE: d42a, delivery-free, two actors.  Nothing transfers to "
      "transport scope.")

print(f"\n[d51] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")
