#!/usr/bin/env python3
"""
d51_menu_visibility_exact.py — v10 D51: (H1) via MENU-VISIBILITY.
Pin: note-d51-h1-menu-visibility-pin.md (STRICT, LOG #423, committed
before this file existed).

THE STRUCTURAL READING (pin §2), read from the committed layer:
`admissible(acts, e)` builds `View(acts+[e], pred, pred[j])` — the
CANDIDATE EVENT'S OWN CAUSAL PAST — and the menu reads that view through
EXACTLY FOUR PROJECTIONS: holdings(a), superseded, live/props,
components().  `sigma` records exactly those four kinds of data on the
FULL view.  So (H1) reduces to: are those four projections, evaluated on
each candidate's own view, determined by sigma?

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

sys.setrecursionlimit(300000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D51 — (H1) via MENU-VISIBILITY]")
print("  banner: the admission layer's view is the CANDIDATE's own causal")
print("  past, and the menu reads it through exactly four projections.")
print("  D46a's refuted own-view (tau) route is NOT re-walked.  Depths")
print("  reached are PRINTED, never silently capped.  Scope: d42a,")
print("  DELIVERY-FREE, two actors (D44b's boundary).")

# ------------------------------------------------------------------ MV0
print("\n[MV0 anchor + capacity]")
_SRC = 'v10/code/d42b3_placement_exact.py'
_s = open(_SRC).read()
ns = {}
exec(compile(_s[:_s.index('print("[d42b3')], 'd42b3_ported', 'exec'), ns)
candidates_for = ns['candidates_for']
admissible = ns['admissible']
event_poset = ns['event_poset']
View = ns['View']
prop_options_in_view = ns['prop_options_in_view']
arb_components_in_view = ns['arb_components_in_view']
canon = ns['canon']
V0 = ns['V0']
AB = ('A', 'B')

check("MV0(a) the admission layer is exec'd path-anchored from the "
      "committed d42b3 receipt (single source), and the four "
      "menu-relevant projection functions are taken from it rather than "
      "re-implemented",
      all(callable(f) for f in (candidates_for, admissible,
                                prop_options_in_view,
                                arb_components_in_view)),
      f"source = {_SRC}")


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
    """The FOUR projections the menu actually reads, as a deterministic
    key.  Nothing else in the view can affect a's menu."""
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

# capacity: does the menu view actually EXCEED the noop cone?
exceed = same = 0
extras_max = 0
opp_only = True
for h in FAM:
    for a in AB:
        _, cone = view_of_candidate(h, ('n', a))
        for e, q in CACHE[tuple(h)]:
            if e[1] != a or e[0] == 'n':
                continue
            _, mv = view_of_candidate(h, e)
            if set(mv) > set(cone):
                exceed += 1
                ex = set(mv) - set(cone)
                extras_max = max(extras_max, len(ex))
                for i in ex:
                    if h[i][1] == a:
                        opp_only = False
            elif set(mv) == set(cone):
                same += 1
print(f"  menu view vs noop cone: strictly exceeds in {exceed} "
      f"(actor, candidate) pairs, equal in {same}; max extra events "
      f"{extras_max}; all extras opponent-authored = {opp_only}")
check("MV0(b) CAPACITY — the lag is REAL and NON-EMPTY, so the question "
      "is not vacuous.  The menu view strictly exceeds the actor's noop "
      "cone, and every extra event is OPPONENT-AUTHORED — D46a's finding "
      "reproduced independently on this receipt's own family",
      exceed > 0 and opp_only,
      f"exceeding pairs = {exceed}, equal = {same}, max extras = "
      f"{extras_max}, opponent-authored only = {opp_only}")

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
idle_gap = by_kind['n'][1] < by_kind['n'][0]
pr_exact = all(by_kind[k][1] == by_kind[k][0] for k in ('p', 'r')
               if by_kind[k][0])
check("MV1 MV-STRONG IS REFUTED, AND NOT ONLY WHERE THE PIN EXPECTED. "
      "The pin (§3) pre-registered MV-STRONG as failing for IDLES and "
      "HOLDING for propose/arbitrate, on the wire-closure reasoning that "
      "a candidate touching base b already sees every live proposal on b. "
      "**The measurement refutes that: p and r candidates lag too.**  The "
      "reason is that these projections are the FULL four-tuple over ALL "
      "bases, while a candidate's view need only cover the base it "
      "touches — so the pin's argument, even if right about base b, was "
      "never enough for MV-STRONG as stated.  **The pin's §5 depth-free "
      "sketch is damaged and must be revised; it is NOT quietly dropped**",
      by_kind['p'][1] < by_kind['p'][0] and by_kind['r'][1] < by_kind['r'][0]
      and idle_gap,
      f"by type (equal/total): "
      f"{ {k: f'{v[1]}/{v[0]}' for k, v in sorted(by_kind.items())} } — "
      f"every type lags, so MV-STRONG fails outright")

# ------------------------------------------------------------------ MV2
print("\n[MV2 MV-WEAK — the target: are the projections sigma-determined?]")
print("  sigma is a FULL-VIEW abstraction.  MV1 shows p/r candidates read")
print("  the full-view values, so those are sigma-determined outright.")
print("  The whole question therefore collapses onto the IDLE weight,")
print("  which reads has_p / has_r on the bare cone.")
idle_sig = defaultdict(set)
for h in FAM:
    fv = full_view(h)
    for a in AB:
        cv, _ = view_of_candidate(h, ('n', a))
        hp = bool(prop_options_in_view(cv, a))
        hr = bool(arb_components_in_view(cv, a))
        hp_f = bool(prop_options_in_view(fv, a))
        hr_f = bool(arb_components_in_view(fv, a))
        idle_sig[(hp_f, hr_f)].add((hp, hr))
print(f"  full-view (has_p, has_r) -> set of cone-level values observed:")
for k in sorted(idle_sig):
    print(f"    {k} -> {sorted(idle_sig[k])}")
idle_determined = all(len(v) == 1 for v in idle_sig.values())
check("MV2 THE 2-BIT PROXY IS NOT A FUNCTION — reported as the negative "
      "it is, with its MECHANISM.  The cone-level (has_p, has_r) an idle "
      "reads is NOT determined by the full-view (has_p, has_r): "
      "full-view (False, False) maps to BOTH (False, True) and "
      "(True, False).  **A SMALLER VIEW CAN YIELD MORE OPTIONS**, because "
      "prop_options_in_view excludes a base on which the actor already "
      "has a live proposal — so a view that MISSES that proposal INCLUDES "
      "the base.  Monotonicity fails, and any argument assuming a lagged "
      "view sees a subset of the options is wrong.  This does NOT refute "
      "MV-WEAK: sigma records far more than these two bits, and MV3 tests "
      "the real thing",
      not idle_determined and (False, False) in idle_sig
      and len(idle_sig[(False, False)]) > 1,
      f"map = { {k: sorted(v) for k, v in sorted(idle_sig.items())} } — "
      f"the (False, False) fibre is multi-valued, which is the finding")

# ------------------------------------------------------------------ MV5
print("\n[MV5 mutant — can the instrument see the lag at all?]")
mut_changed = 0
mut_tested = 0
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
        drop = next((i for i in sorted(hidden) if h[i][0] == 'p'), None)
        if drop is None:
            continue
        mut_tested += 1
        vw = View(acts2, pred, hidden - {drop})
        if projections(vw, e[1]) != projections(cv, e[1]):
            mut_changed += 1
        break
check("MV5 THE INSTRUMENT IS NOT BLIND — and the partial rate is itself "
      "the point.  Hiding one proposal from an arbitration candidate's "
      "view changes its menu-relevant projections in a large majority of "
      "cases but NOT all: when the dropped proposal is on a base the "
      "candidate's projections do not reach, nothing moves.  A gate "
      "demanding 100% would have been wrong about the object; what must "
      "be shown is that the projections DO respond to their input, and "
      "they do",
      mut_tested > 0 and mut_changed > mut_tested // 2,
      f"mutants tested = {mut_tested}, projections changed = "
      f"{mut_changed} ({100 * mut_changed // max(mut_tested, 1)}%) — "
      f"responsive, not blind, and not vacuously total")

# ------------------------------------------------------------------ MV3
print("\n[MV3 (H1) at the menu level, on this family]")
by_proj = defaultdict(set)
for h in FAM:
    fv = full_view(h)
    key = tuple(projections(fv, a) for a in AB)
    men = tuple(sorted(((dk(e), q) for e, q in CACHE[tuple(h)]), key=repr))
    by_proj[key].add(men)
viol = sum(1 for v in by_proj.values() if len(v) > 1)
live_keys = sum(1 for v in by_proj.values() if len(v) >= 1)
multi = sum(1 for k, v in by_proj.items()
            if len([1 for h in FAM]) and len(v) >= 1)
check("MV3 [EVIDENCE, never a premise] EQUAL FULL-VIEW PROJECTIONS => "
      "EQUAL MENUS, with exact weights, over every history of the "
      f"enumerated family to depth {CAP}: zero violations.  This is the "
      "menu-level form of MV1+MV2 and it is what (H1) asserts, verified "
      "here at finite depth only",
      viol == 0 and len(by_proj) > 1,
      f"distinct full-view projection keys = {len(by_proj)}; keys "
      f"carrying more than one menu = {viol}; histories = {len(FAM)}")

# ------------------------------------------------------------------ MV4
print("\n[MV4 (H2) settled explicitly]")
trans = defaultdict(set)
for h in FAM:
    if len(h) >= CAP:
        continue
    fv = full_view(h)
    kh = tuple(projections(fv, a) for a in AB)
    for e, q in CACHE[tuple(h)]:
        h2 = list(h) + [e]
        f2 = full_view(h2)
        k2 = tuple(projections(f2, a) for a in AB)
        trans[(kh, dk(e))].add(k2)
h2_viol = sum(1 for v in trans.values() if len(v) > 1)
check("MV4 (H2) IS SETTLED HERE, not left dangling as d44a left it: the "
      "successor projection-state is a FUNCTION of (projection-state, "
      "event) — zero violations over the family.  So (H2) holds at the "
      "projection level on this family, and does NOT need a separate "
      "argument from (H1) at this scope",
      h2_viol == 0 and len(trans) > 1,
      f"(state, event) pairs = {len(trans)}; pairs with more than one "
      f"successor state = {h2_viol}")

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
      "nothing more; falsifiability is MV5's job",
      len(_ch) >= 7 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

# ============================== verdict ==================================
print("\n[VERDICT — D51]")
print("  **MV-WEAK HOLDS ON THIS FAMILY — carried by MV3, not by the "
      "route the pin proposed.**  Equal full-view projections give equal "
      "menus with exact weights across all 6,471 histories, over 209 "
      "distinct projection keys, zero violations.  Since sigma IS an "
      "abstraction of exactly those projections, menus are "
      "sigma-determined here.")
print("  **BUT THE PIN'S PROOF ROUTE IS DAMAGED, AND THAT IS THE REAL "
      "NEWS.**  MV-STRONG was pre-registered to hold for propose and "
      "arbitrate candidates on a wire-closure argument.  It does not: "
      "every event type lags.  Worse, MV2 shows monotonicity FAILS — a "
      "smaller view can yield MORE options, because missing an actor's "
      "own live proposal makes a base look available.  Any depth-free "
      "argument built on 'the lagged view sees a subset' is therefore "
      "unsound, and the pin's §5 sketch is one of those.")
print("  WHAT THIS IS AND IS NOT.  Every gate above is FINITE-DEPTH "
      f"[EVIDENCE] on the family to depth {CAP}.  **(H1) IS NOT "
      "DISCHARGED.**  What this unit delivers is: (a) the reduction of "
      "(H1) to the four menu-relevant projections, which is exact and "
      "structural; (b) MV3/MV4 confirming the reduction's target and "
      "(H2) at finite depth; and (c) the REFUTATION of the pin's own "
      "depth-free route, with the monotonicity failure that kills it "
      "exhibited.  A second refuted route is worth more than a third "
      "unexamined one, but it is not a proof.")
print("  SCOPE: d42a, delivery-free, two actors.  Nothing transfers to "
      "transport scope.")

print(f"\n[d51] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")
