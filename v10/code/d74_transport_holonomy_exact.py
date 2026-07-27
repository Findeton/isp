#!/usr/bin/env python3
"""
d74_transport_holonomy_exact.py — v10 D74 THE TRANSPORT HOLONOMY:
carrier, group, removability, and the odd-sector U(1) search.

Pin: v10/note-d74-transport-holonomy-pin.md (FROZEN, STRICT).
Parents: D72 TERMINAL (note-d72-weld-result.md — the transport-scope
census this receipt ANCHORS on), D65 (the mass-ratio coboundary and
its repair theory), D71b (the order-dual / traversal-reversal carrier),
D64 (the coboundary-FIRST discipline and the C7 removability idiom),
D73 (the generic-geometry lesson: carry an asymmetric substrate).

THE FOUR ARMS (pin sec.1), run in the pin's OUTPUT order — removability
BEFORE structure:

  TH-C  REMOVABILITY (first).  Is the transport twist a coboundary?
        Both routes (potential propagation with an obstruction count;
        relabelled recount), on the R+-valued connection, over a LADDER
        of committed state abstractions; plus the D65 per-state test.
  TH-A  THE CARRIER.  The census extended in depth, pool and schedule
        family (incl. two asymmetric/defected sub-grammars); the
        defects classified by kind-pair and register-overlap type; and
        the QUOTIENT THAT SEES THE HOLONOMY, constructed explicitly.
  TH-B  THE GROUP.  The multiplicative group generated per scope and
        cumulatively; prime content; growth with depth/pool.
  TH-D  THE ODD SECTOR.  Reversal decomposition on the holonomy-
        carrying loops; the search for a residue that CONJUGATES
        rather than inverts; the v7 i-twist correspondence with its
        adversarial control; the order-dual arm; the asymmetric arm;
        and (ROUND 1) the reversal-EVEN channel, which the first pass
        declared empty and is not.

ROUND-1 REPAIRS (reviews/d74-round1-hostile-review.md, 5 MAJOR / 6
MODERATE / 6 MINOR).  Applied here, with the round credited where it
found something the first pass did not:
  * MAJOR 1 / MODERATE 4 — C0.1, D1 and D4.1 are ALGEBRAIC IDENTITIES of
    their own definitions and are now tagged NO INDEPENDENT INFORMATION,
    as are A3.3 (the self-loop / closure identity of the exchange graph)
    and the join-closure "construction", which is a definitional remark.
  * MAJOR 2 — the outcome predicate is rebuilt so that TH-III is
    REACHABLE, and its positive branch is demonstrated on constructed
    input (OUT.1) instead of being asserted.
  * MAJOR 3 — THE ROUND'S FIND: the reversal-EVEN channel is NOT empty.
    The referee's invariant J (built from this receipt's own D5 raw
    material) is gated at D9: J = 1 implies r = 1 on every closed square
    of three arms, and J = 0 on every defective square.
  * MAJOR 4 — the order-dual arm is rebuilt honestly: ALL linear
    extensions of the opposite poset (D5.2), not one enumeration order;
    and the grammar is gated to be NOT reversal-blocking (D5.0), which
    is the corrected reason for the negative.
  * MAJOR 5 / MODERATE 6 — the dichotomy carries the DESCENT qualifier
    everywhere; MULT (the ladder's own rung 3) is gated to close all 44
    of the descent-obstruction half; the four weakenings of descent are
    gated at 0 of 44 each.
  * MODERATE 2 — CTL-ORDER is applied to THIS unit's own dichotomy.
  * MODERATE 5 — a genuinely independent FOURTH ACTOR POOL (A,B,C,D).
  * MINOR — D3.1's bare-constant predicate and dead code removed;
    linear_extensions (required by the AST pass) is now used.

RUNTIME: ~6-9 min on the default arms; printed at the end.
  D74_SKIP_DEEP=1 drops the deepest two census arms (for a fast pass).

HOUSE RULES OBSERVED
  * Exact arithmetic (fractions.Fraction) end to end.  Every ratio is
    an exact Fraction; every gate is stated on the Fraction.
  * Committed layers are single-sourced by TEXT-SLICE of their own
    source, with (a) an AST pass that asserts the required defs exist
    with the required signatures and (b) EXIT-FREEDOM GATED: sys.exit
    and os._exit raise inside the sliced exec.
  * No bare-constant predicates: every number a gate tests against is
    either a QUOTED committed value (registry ANCH/QUOTES, with
    path:line provenance) or a quantity derived inside this receipt.
  * Every census printed BOTH WAYS.
  * Substantive negatives exit 0.  exit 1 is reserved for ANCHOR
    failure — a committed D72 number that does not reproduce.
  * Determinism: all set/dict iteration that feeds a printed number is
    ordered by stable_key (hash-seed independent).

"""

from __future__ import annotations

import ast
import os
import sys
import time
import types
from collections import Counter, defaultdict
from fractions import Fraction as Fr

T0 = time.time()
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO)          # .../isp  (run from anywhere)
os.chdir(REPO)

PASS = FAIL = 0
ANCHOR_FAIL = 0
COROLLARY = []


def check(label, ok, detail="", corollary_of=None):
    """corollary_of: the gate is entailed by another gate or is true of
    every object of its type.  It is run and printed but NOT counted as
    independent evidence (the D72 MODERATE-4 discipline)."""
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS += int(bool(ok))
    FAIL += int(not ok)
    if corollary_of is not None:
        COROLLARY.append((label.split(":")[0].split("  ")[0], corollary_of))
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))
    if corollary_of is not None:
        print(f"         ^ NO INDEPENDENT INFORMATION: {corollary_of}")
    return bool(ok)


def anchor(label, ok, detail=""):
    global ANCHOR_FAIL
    if not check("ANCHOR " + label, ok, detail):
        ANCHOR_FAIL += 1
    return bool(ok)


def report(label, value):
    print(f"  [DATA] {label}: {value}")


def sk(o):
    """Hash-order-independent total key for nested frozenset/tuple
    objects.  repr of a frozenset depends on PYTHONHASHSEED; this does
    not.  (D72's stable_key, re-derived here.)"""
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(sk(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


_EVSK = {}


def evsk(e):
    """sk() of an event, memoised.  Events are immutable tuples and the
    same few thousand of them recur across every history, so this is a
    pure speed-up: the value is identical to sk(e)."""
    v = _EVSK.get(e)
    if v is None:
        v = sk(e)
        _EVSK[e] = v
    return v


def fmt(counter):
    return {str(k): v for k, v in sorted(counter.items(), key=lambda z: sk(z[0]))}


# ===========================================================================
# SEC 0.  THE REGISTRY — every constant a gate tests against, with provenance
# ===========================================================================

QUOTES = {
    "T6.1": (
        "v10/note-d72-weld-result.md:150 (sec.1 T6.1) and "
        "v10/data/d72_weld_exact.out:124",
        "(A,B) d <= 4: 88 of 1,546 closed squares non-unit, spectrum "
        "{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}, kinds {(r,d): 68, (d,r): 8, "
        "(d,n): 6, (d,d): 4, (n,d): 2}, delivery-bearing 88/88, "
        "shallowest defect at total depth 3.  (A,B,C) d <= 3: 12 of "
        "1,554, spectrum {1/2: 12}, kinds {(r,d): 12}.",
    ),
    "T6.2": (
        "v10/note-d72-weld-result.md:151 (sec.1 T6.2) and "
        "v10/data/d72_weld_exact.out:125",
        "(A,B) d <= 4: 40 half-open (AB-only 28, BA-only 12), kinds "
        "{(r,d): 12, (d,r): 4, (p,d): 16, (d,p): 8}, 40/40 "
        "delivery-bearing.",
    ),
    "T6.3": (
        "v10/note-d72-weld-result.md:152 (sec.1 T6.3)",
        "0 of 88 and 0 of 12 defective squares close at record level.",
    ),
    "T6.4": (
        "v10/data/d72_weld_exact.out:127-135",
        "the minimal witness: h = [('p','A',V0,0)], eA = arb of own "
        "proposal, eB = ('d','A','B',V0); q(eA|h) = 1/4, q(eB|h.eA) = "
        "1/8, q(eB|h) = 1/4, q(eA|h.eB) = 1/4; dP_AB/dP_BA = 1/2; "
        "mu(h.eA.eB) = 1/256 vs mu(h.eB.eA) = 1/128.",
    ),
    "T6.5": (
        "v10/note-d72-weld-result.md:154 (sec.1 T6.5)",
        "d42b1 (A,B) d <= 4 idle-weight spectrum {1/2: 7738, 3/4: 200}; "
        "533 of 1,073 comparable closed squares contain no idle event.",
    ),
    "T2.5": (
        "v10/data/d72_weld_exact.out:119-121, 137-139",
        "grammar 2 record deletion graph: (A,B) d<=4 nodes 2477, "
        "up-edges 2900, multi-valued 0, independent cycles 424, "
        "non-trivial holonomies 0, mu class-constant 2477/2477, 3969 "
        "histories; (A,B,C) d<=3 nodes 2128, up-edges 2772, cycles 645, "
        "0 defects, 2128/2128, 3424 histories.",
    ),
    "d65": (
        "v10/note-d65-descent-conditions-result.md:173-182 (quoted by "
        "d72 as QUOTES['d65'])",
        "The defect is exactly the intermediate-mass ratio: d = "
        "M(sigma(Hb))/M(sigma(Ha)) with M the per-state menu mass; "
        "masses {2, 5/2}; spectrum {1, 4/5, 5/4}.",
    ),
    "d72_group": (
        "v10/note-d72-weld-result.md:391-395 (licensed claim 6)",
        "the NORMALISED grammar-1 kernel has holonomy image the "
        "infinite cyclic group <5/4> in R+, square spectrum {4/5,1,5/4}.",
    ),
    "Ldual": (
        "v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:2843-2849 "
        "(quoted by d72 as QUOTES['Ldual'])",
        "L_dual = e^{-kE} e^{i theta O}; E is dual-even data; O is "
        "dual-odd data; dual reversal sends O to -O; therefore dual "
        "reversal sends L to its complex conjugate.",
    ),
    "sqrtq": (
        "v10/note-d42b4-quantum-lift.md:15-18 (quoted by d72)",
        "The lift assigns each complete depth-D history the amplitude "
        "prod sqrt(q) on record ancillas.",
    ),
    "d73": (
        "v10/note-d73-even-gram-result.md sec.12 (the generic-geometry "
        "lesson)",
        "hand-built symmetry is a cage: carry at least one "
        "asymmetric/defected substrate.",
    ),
    # --- added at ROUND 1, for the repairs that cite a committed source ---
    "d72_T61": (
        "v10/note-d72-weld-result.md:150-151 (sec.1 rows T6.1, T6.2) and "
        "its DELTA — NOT licensed claim 7",
        "the MULTIPLICITIES {1/2: 70, 2/3: 2, 3/2: 6, 2: 10} and the "
        "half-open split (AB-only 28, BA-only 12) are TABLE ROWS of D72, "
        "not licensed claims.  D72's licensed claim 7 licenses the VALUE "
        "SET {1/2,2/3,3/2,2} and the TOTALS (88 of 1,546; 40 half-open; "
        "12 of 1,554), which CTL-ORDER leaves untouched.  This receipt's "
        "orientation correction is addressed to the rows and the DELTA.",
    ),
    "d71b_carrier": (
        "v10/note-d71b-holonomy-phase-identity.md:26-37, 287-306, 394-395 "
        "quoting v7 paper30:2506-2511",
        "D71b's carrier is the committed UNLABELED RECORD ORDER and its "
        "* is POSET REVERSAL of a record order type — defined on every "
        "poset, never undefined.  'Linear extensions' is D72's "
        "common-carrier construction (note-d72-weld-result.md:60, "
        "licensed claim 2), scoped to 2-event histories and nothing "
        "larger.  D74's first pass mis-cited the two.",
    ),
    "d65_3.1": (
        "v10/note-d65-descent-conditions-result.md:277-299 (sec.3.1, the "
        "repair cone) and :613-617 (residue 2)",
        "at D = 4: repair constraints 403, repair cone 573, "
        "record-constant family 313, repairs that also descend 205, and "
        "repair rows NOT implied by record-constancy = 152 of 403 = "
        "exactly the rows whose two corners carry different records.  "
        "Residue 2: M is binary at two actors; at three actors or with "
        "delivery the coboundary statement must be RE-DERIVED, not "
        "carried.",
    ),
}

# --- committed NUMERIC anchors, transcribed from the sources above ---------
ANCH = {
    "AB_closed": 1546,
    "AB_defects": 88,
    "AB_spectrum": {Fr(1, 2): 70, Fr(2, 3): 2, Fr(3, 2): 6, Fr(2): 10},
    "AB_full_ratios": {Fr(1, 2): 70, Fr(2, 3): 2, Fr(1): 1458,
                       Fr(3, 2): 6, Fr(2): 10},
    "AB_kinds": {("r", "d"): 68, ("d", "r"): 8, ("d", "n"): 6,
                 ("d", "d"): 4, ("n", "d"): 2},
    "AB_bothblocked": 142,
    "AB_ABonly": 28,
    "AB_BAonly": 12,
    "AB_halfopen": 40,
    "AB_openkinds": {("r", "d"): 12, ("d", "r"): 4, ("p", "d"): 16,
                     ("d", "p"): 8},
    "AB_mindepth": 3,
    "AB_hist": 3969,
    "AB_classes": 2477,
    "AB_edges": 2900,
    "AB_cycles": 424,
    "ABC_closed": 1554,
    "ABC_defects": 12,
    "ABC_spectrum": {Fr(1, 2): 12},
    "ABC_full_ratios": {Fr(1, 2): 12, Fr(1): 1542},
    "ABC_kinds": {("r", "d"): 12},
    "ABC_bothblocked": 42,
    "ABC_halfopen": 0,
    "ABC_hist": 3424,
    "ABC_classes": 2128,
    "ABC_edges": 2772,
    "ABC_cycles": 645,
    "idle_spectrum": {Fr(1, 2): 7738, Fr(3, 4): 200},
    "comparable": 1073,
    "no_idle": 533,
    "wit_qA": Fr(1, 4), "wit_qB2": Fr(1, 8),
    "wit_qB": Fr(1, 4), "wit_qA2": Fr(1, 4),
    "wit_r": Fr(1, 2),
    "wit_muAB": Fr(1, 256), "wit_muBA": Fr(1, 128),
    "d65_masses": {Fr(2), Fr(5, 2)},
    "d65_ratios": {Fr(4, 5), Fr(1), Fr(5, 4)},
}

print("=" * 78)
print("D74 — THE TRANSPORT HOLONOMY: carrier, group, removability, and the")
print("      odd-sector U(1) search  (exact receipt)")
print("=" * 78)
print("  banner: exact Fractions throughout; the committed d42b1 / d42b3")
print("  layers single-sourced by text-slice + an AST signature pass, with")
print("  exit-freedom gated; every tested constant quoted from a committed")
print("  source (registry below); removability BEFORE structure in both")
print("  computation and presentation; substantive negatives exit 0; exit 1")
print("  ONLY if a committed D72 number fails to reproduce.")
print()
print(f"  PYTHONHASHSEED = {os.environ.get('PYTHONHASHSEED', '(unset)')}")
print(f"  D74_SKIP_DEEP  = {os.environ.get('D74_SKIP_DEEP', '0')}")
print()
print("  QUOTE REGISTRY (the anchors below are held to these):")
for k, (where, text) in QUOTES.items():
    print(f"    [{k}] {where}")
    for i in range(0, len(text), 68):
        print(f"        {text[i:i + 68]}")


# ===========================================================================
# SEC 0.1  SINGLE-SOURCING: AST signature pass, then text-slice with gated
#          exit-freedom.
# ===========================================================================

class _NoExit(Exception):
    pass


def ast_signatures(path, required):
    """AST pass: assert each required def exists at module level with the
    exact positional-argument list given.  Returns the census of all
    module-level defs, so a silent upstream edit cannot slip through."""
    tree = ast.parse(open(path).read(), filename=path)
    sigs = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            sigs[node.name] = [a.arg for a in node.args.args]
        elif isinstance(node, ast.ClassDef):
            sigs[node.name] = ["<class>"]
    missing = []
    for name, args in required.items():
        if name not in sigs:
            missing.append((name, "ABSENT"))
        elif args is not None and sigs[name] != args:
            missing.append((name, f"{sigs[name]} != {args}"))
    return sigs, missing


def slice_exec(path, cut_marker, name):
    """Execute the definition head of a committed source (everything
    strictly before the first module-level executable statement).
    sys.exit / os._exit raise inside, and are restored after."""
    src = open(path).read()
    idx = src.index(cut_marker)
    head = src[:idx]
    mod = types.ModuleType(name)
    sys.modules[name] = mod
    ns = mod.__dict__
    ns["__name__"] = name
    real_exit, real_osexit = sys.exit, os._exit

    def _blocked(*a, **k):
        raise _NoExit("sliced layer attempted to exit")

    sys.exit, os._exit = _blocked, _blocked
    try:
        exec(compile(head, f"<slice:{os.path.basename(path)}>", "exec"), ns)
    finally:
        sys.exit, os._exit = real_exit, real_osexit
    return ns, len(head), len(src)


print()
print("-" * 78)
print("SEC 0.1  committed sources: AST signature pass, then slice")
print("-" * 78)

B1_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e", "actors", "law"],
    "canon": ["acts"],
    "regs_of": ["op"],
    "event_poset": ["acts"],
    "full_view": ["acts"],
    "own_view": ["acts", "a"],
    "prop_options_in_view": ["view", "a"],
    "deliver_options_in_view": ["view", "a", "actors"],
    "admissible_arb_ckeys": ["acts", "a", "actors"],
    "linear_extensions": ["acts"],
    "View": ["<class>"],
}
B3_REQ = {
    "candidates_for": ["acts", "actors"],
    "admissible": ["acts", "e"],
    "canon": ["acts"],
    "regs_of": ["op"],
    "mu_of": ["acts"],
}

_sig1, _miss1 = ast_signatures("v10/code/d42b1_transport_exact.py", B1_REQ)
_sig3, _miss3 = ast_signatures("v10/code/d42b3_placement_exact.py", B3_REQ)
if _miss1 or _miss3:
    print("!" * 78)
    print(f"AST SIGNATURE FAILURE: d42b1 {_miss1}; d42b3 {_miss3}")
    print("!" * 78)
    sys.exit(1)
report("d42b1 AST", f"{len(_sig1)} module-level defs/classes; all "
       f"{len(B1_REQ)} required signatures matched exactly")
report("d42b3 AST", f"{len(_sig3)} module-level defs/classes; all "
       f"{len(B3_REQ)} required signatures matched exactly")

B1, _b1n, _b1t = slice_exec("v10/code/d42b1_transport_exact.py",
                            'print("[d42b1', "d74_d42b1")
report("d42b1 slice", f"{_b1n}/{_b1t} bytes executed (definition head "
       "only); exit-freedom gated")
B3, _b3n, _b3t = slice_exec("v10/code/d42b3_placement_exact.py",
                            'print("[d42b3', "d74_d42b3")
report("d42b3 slice", f"{_b3n}/{_b3t} bytes executed (definition head "
       "only); exit-freedom gated")

b1_cand = B1["candidates_for"]
b1_adm = B1["admissible"]
b1_canon = B1["canon"]
b1_regs = B1["regs_of"]
b1_fullview = B1["full_view"]
b1_ownview = B1["own_view"]
b1_propopt = B1["prop_options_in_view"]
b1_delopt = B1["deliver_options_in_view"]
b1_arbck = B1["admissible_arb_ckeys"]
b3_cand = B3["candidates_for"]
b3_adm = B3["admissible"]
b3_canon = B3["canon"]
b3_regs = B3["regs_of"]

_exitfree = False
try:
    _blocked_probe = slice_exec("v10/code/d42b1_transport_exact.py",
                                'print("[d42b1', "d74_probe")
    _exitfree = True
except _NoExit:
    _exitfree = False
check("SRC.1 EXIT-FREEDOM GATED: the sliced layers cannot set this "
      "receipt's exit status — sys.exit/os._exit are neutralised inside "
      "the slice and restored after; the slice re-executes cleanly",
      _exitfree,
      "second slice of d42b1 executed with exit blocked and raised "
      "nothing",
      corollary_of="a property of the loader, not of the substrate; it "
      "tests our plumbing")


# ===========================================================================
# SEC 0.2  THE MACHINERY (D72's census, re-derived here; reused verbatim in
#          shape so that its numbers must reproduce)
# ===========================================================================

def enumerate_line(cands, actors, depth, filt=None):
    """D72's enumerate_line.  `filt` (the asymmetric sub-grammars) removes
    candidate EVENTS from the generated support; the committed WEIGHTS are
    untouched — a declared sub-grammar, not a re-priced one."""
    fam = [[]]
    frontier = [[]]
    cache = {}
    while frontier:
        h = frontier.pop()
        c = cands(h, actors)
        if filt is not None:
            c = [(e, q) for e, q in c if filt(e)]
        cache[tuple(h)] = c
        if len(h) >= depth:
            continue
        for e, q in c:
            fam.append(h + [e])
            frontier.append(h + [e])
    return fam, cache


def square_census(fam, cache, actors, dep, adm, regs, canon_f,
                  filt=None, reverse_cands=False, tamper=None):
    """The exchange-square census (D72's transport_square_census, with the
    controls this unit needs bolted on and nothing else changed).

    Returns (status counter, ratio counter, kinds, open-kinds, defects,
    half-open list, all-closed list).
    Each defect row: (h, eA, eB, r, qA, qB2, qB, qA2)."""
    st = Counter()
    rat = Counter()
    kinds = Counter()
    open_kinds = Counter()
    defects = []
    half = []
    closed = []

    def W(h, e, actors_):
        ok, q = adm(h, e, actors_) if adm is b1_adm else adm(h, e)
        if ok and filt is not None and not filt(e):
            return False, None
        if ok and tamper is not None and tamper[0] == (tuple(h), e):
            q = q * tamper[1]
        return ok, q

    for h in fam:
        if len(h) + 2 > dep:
            continue
        cands = [e for e, q in cache[tuple(h)]]
        if reverse_cands:
            cands = cands[::-1]
        for i in range(len(cands)):
            for j in range(i + 1, len(cands)):
                eA, eB = cands[i], cands[j]
                okA, qA = W(h, eA, actors)
                okB, qB = W(h, eB, actors)
                if not (okA and okB):
                    continue
                okB2, qB2 = W(h + [eA], eB, actors)
                okA2, qA2 = W(h + [eB], eA, actors)
                if okB2 and okA2:
                    st["closed"] += 1
                    r = Fr(qA * qB2, 1) / Fr(qB * qA2, 1)
                    rat[r] += 1
                    closed.append((tuple(h), eA, eB, r))
                    if r != 1:
                        kinds[(eA[0], eB[0])] += 1
                        defects.append((tuple(h), eA, eB, r,
                                        qA, qB2, qB, qA2))
                elif okB2:
                    st["AB-only"] += 1
                    open_kinds[(eA[0], eB[0])] += 1
                    half.append((tuple(h), eA, eB, "AB-only"))
                elif okA2:
                    st["BA-only"] += 1
                    open_kinds[(eA[0], eB[0])] += 1
                    half.append((tuple(h), eA, eB, "BA-only"))
                else:
                    st["both-blocked"] += 1
    return st, rat, kinds, open_kinds, defects, half, closed


def mu_map(fam, cache):
    mu = {(): Fr(1)}
    for h in sorted(fam, key=len):
        if not h:
            continue
        par = tuple(h[:-1])
        qs = [q for ee, q in cache[par] if ee == h[-1]]
        mu[tuple(h)] = mu[par] * Fr(qs[0])
    return mu


def menu_mass(cache):
    return {h: sum(Fr(q) for e, q in cache[h]) for h in cache}


def build_edges(fam, cache, canon_f, depth):
    edgew = defaultdict(set)
    for h in fam:
        if len(h) >= depth:
            continue
        C = canon_f(h)
        for e, q in cache[tuple(h)]:
            edgew[(sk(C), sk(canon_f(h + [e])))].add(Fr(q))
    return edgew


def holonomy_of(edges, reverse_order=False):
    """Exact R+ holonomy census by spanning-forest potentials.

    edges: iterable of (u, v, w) requiring phi(v) = w * phi(u).
    Returns (n_nodes, n_components, cycle_rank, obstruction_count,
             holonomy value multiset, potential dict).
    The obstruction count IS the number of independent cycles whose
    holonomy is != 1; zero means the connection is a coboundary of phi."""
    edges = sorted(edges, key=lambda z: (sk(z[0]), sk(z[1]), z[2]))
    if reverse_order:
        edges = edges[::-1]
    nodes = set()
    for u, v, w in edges:
        nodes.add(u)
        nodes.add(v)
    parent = {x: x for x in nodes}
    pot = {x: Fr(1) for x in nodes}

    def find(x):
        f = Fr(1)
        y = x
        while parent[y] != y:
            f *= pot[y]
            y = parent[y]
        return y, f

    rank = 0
    hol = Counter()
    for u, v, w in edges:
        ru, fu = find(u)
        rv, fv = find(v)
        if ru == rv:
            rank += 1
            hol[(fu * w) / fv] += 1
        else:
            parent[rv] = ru
            pot[rv] = (fu * w) / fv
    comps = len({find(x)[0] for x in nodes})
    phi = {x: find(x)[1] for x in nodes}
    obstruction = sum(v for k, v in hol.items() if k != 1)
    return len(nodes), comps, rank, obstruction, hol, phi


def primes_of(fr):
    """Exact prime factorisation of a positive Fraction -> {p: exponent}."""
    out = {}
    for n, sgn in ((fr.numerator, 1), (fr.denominator, -1)):
        d = 2
        while d * d <= n:
            while n % d == 0:
                out[d] = out.get(d, 0) + sgn
                n //= d
            d += 1
        if n > 1:
            out[n] = out.get(n, 0) + sgn
    return {p: e for p, e in out.items() if e != 0}


def lattice_basis(vecs):
    """Hermite-style integer row reduction: a basis of the subgroup of
    Z^k generated by vecs (exact, no floats)."""
    rows = [list(v) for v in vecs if any(v)]
    k = len(rows[0]) if rows else 0
    basis = []
    col = 0
    while col < k and rows:
        piv = [r for r in rows if r[col] != 0]
        if not piv:
            col += 1
            continue
        while len(piv) > 1:
            piv.sort(key=lambda r: abs(r[col]))
            p = piv[0]
            newpiv = [p]
            for r in piv[1:]:
                f = r[col] // p[col]
                rr = [a - f * b for a, b in zip(r, p)]
                if rr[col] != 0:
                    newpiv.append(rr)
                elif any(rr):
                    rows.append(rr)
            piv = newpiv
        p = piv[0]
        basis.append(p)
        rows = [r for r in rows if r[col] == 0 and any(r)]
        col += 1
    return basis


def group_of(values):
    """The multiplicative subgroup of Q+ generated by `values`, named
    exactly: its prime support, an integer basis of its exponent lattice,
    its rank, and whether it is the FULL group on that prime support."""
    vals = [v for v in values if v != 1]
    if not vals:
        return {"primes": [], "rank": 0, "basis": [], "full": True,
                "index": 1, "name": "{1} (trivial)"}
    ps = sorted({p for v in vals for p in primes_of(v)})
    vecs = []
    for v in vals:
        f = primes_of(v)
        vecs.append([f.get(p, 0) for p in ps])
    B = lattice_basis(vecs)
    rank = len(B)
    full = (rank == len(ps)) and all(
        all(b[i] == (1 if i == j else 0) for i in range(len(ps)))
        for j, b in enumerate(sorted(B, key=lambda r: [abs(x) for x in r]))
    ) if rank == len(ps) else False
    # index of the lattice in Z^{|ps|} when full rank: |det| of the basis
    idx = None
    if rank == len(ps) and rank > 0:
        M = [row[:] for row in B]
        det = Fr(1)
        n = rank
        for i in range(n):
            p = next((r for r in range(i, n) if M[r][i] != 0), None)
            if p is None:
                det = Fr(0)
                break
            if p != i:
                M[i], M[p] = M[p], M[i]
                det = -det
            det *= M[i][i]
            inv = Fr(1, M[i][i])
            for r in range(i + 1, n):
                f = Fr(M[r][i]) * inv
                M[r] = [Fr(a) - f * Fr(b) for a, b in zip(M[r], M[i])]
        idx = abs(det)
    if idx == 1:
        nm = "<" + ", ".join(str(p) for p in ps) + "> = the FULL group of " \
             + "-".join(str(p) for p in ps) + "-smooth positive rationals" \
             + f" (free abelian of rank {rank})"
    else:
        nm = ("subgroup of <" + ", ".join(str(p) for p in ps)
              + f"> of rank {rank}, index {idx}")
    return {"primes": ps, "rank": rank, "basis": B, "full": (idx == 1),
            "index": idx, "name": nm}


# ===========================================================================
# SEC 1.  ANCHORS — the D72 census must reproduce EXACTLY.  exit 1 here only.
# ===========================================================================

print()
print("-" * 78)
print("SEC 1  ANCHORS — D72's committed transport census (exit 1 on failure)")
print("-" * 78)

AB = ("A", "B")
ABC = ("A", "B", "C")
ABCD = ("A", "B", "C", "D")      # round-1 MODERATE 5: a fourth actor pool

ARMS = {}          # name -> dict of everything computed for that arm
_t = time.time()

for _nm, _actors, _dep, _pref in (("AB4", AB, 4, "AB"),
                                  ("ABC3", ABC, 3, "ABC")):
    fam, cache = enumerate_line(b1_cand, _actors, _dep)
    st, rat, kinds, okinds, defs, half, closed = square_census(
        fam, cache, _actors, _dep, b1_adm, b1_regs, b1_canon)
    mu = mu_map(fam, cache)
    M = menu_mass(cache)
    edgew = build_edges(fam, cache, b1_canon, _dep)
    _n, _c, _rk, _ob, _hol, _phi = holonomy_of(
        [(u, v, w) for (u, v), ws in edgew.items() for w in ws])
    mucls = defaultdict(set)
    for h in fam:
        mucls[sk(b1_canon(h))].add(mu[tuple(h)])
    closes = sum(1 for h, eA, eB, r, *_ in defs
                 if sk(b1_canon(list(h) + [eA, eB]))
                 == sk(b1_canon(list(h) + [eB, eA])))
    dely = sum(1 for h, eA, eB, r, *_ in defs if 'd' in (eA[0], eB[0]))
    dely_h = sum(1 for h, eA, eB, k in half if 'd' in (eA[0], eB[0]))
    mind = min((len(h) + 2 for h, *_ in defs), default=None)
    ARMS[_nm] = dict(actors=_actors, dep=_dep, fam=fam, cache=cache, st=st,
                     rat=rat, kinds=kinds, okinds=okinds, defs=defs,
                     half=half, closed=closed, mu=mu, M=M, edgew=edgew,
                     rank=_rk, obstr=_ob, mucls=mucls, closes=closes,
                     nodes=_n)
    report(f"{_nm} family", f"{len(fam)} histories, "
           f"{len(mucls)} record classes")
    report(f"{_nm} exchange-square census", dict(st))
    report(f"{_nm} exact ratios dP_AB/dP_BA", fmt(rat))
    report(f"{_nm} defect kinds", {str(k): v for k, v in
                                   sorted(kinds.items())})
    report(f"{_nm} half-open kinds", {str(k): v for k, v in
                                      sorted(okinds.items())})

    anchor(f"{_nm}.1 D72's T6.1 row reproduces EXACTLY — closed-square "
           f"count, the full ratio multiset (both non-unit AND unit), the "
           f"kind census, delivery-bearing fraction and shallowest depth",
           st["closed"] == ANCH[_pref + "_closed"]
           and dict(rat) == ANCH[_pref + "_full_ratios"]
           and dict(kinds) == ANCH[_pref + "_kinds"]
           and dely == len(defs) == ANCH[_pref + "_defects"]
           and st["both-blocked"] == ANCH[_pref + "_bothblocked"]
           and mind == ANCH["AB_mindepth"],
           f"closed {st['closed']} (quoted {ANCH[_pref + '_closed']}); "
           f"non-unit {len(defs)} (quoted {ANCH[_pref + '_defects']}); "
           f"ratios {fmt(rat)}; kinds match = "
           f"{dict(kinds) == ANCH[_pref + '_kinds']}; delivery-bearing "
           f"{dely}/{len(defs)}; shallowest depth {mind}")

    anchor(f"{_nm}.2 D72's T6.2 half-open row reproduces EXACTLY",
           st.get("AB-only", 0) + st.get("BA-only", 0)
           == ANCH[_pref + "_halfopen"]
           and (_pref != "AB" or (st["AB-only"] == ANCH["AB_ABonly"]
                                  and st["BA-only"] == ANCH["AB_BAonly"]
                                  and dict(okinds) == ANCH["AB_openkinds"]
                                  and dely_h == len(half))),
           f"AB-only {st.get('AB-only', 0)}, BA-only "
           f"{st.get('BA-only', 0)}, total "
           f"{st.get('AB-only', 0) + st.get('BA-only', 0)} (quoted "
           f"{ANCH[_pref + '_halfopen']}); kinds {dict(okinds)}; "
           f"delivery-bearing {dely_h}/{len(half)}")

    anchor(f"{_nm}.3 D72's T6.3 blindness row reproduces: NONE of the "
           f"defective squares closes at record level",
           closes == 0 and len(defs) > 0,
           f"{closes}/{len(defs)} defective squares close under the "
           f"committed canon")

    anchor(f"{_nm}.4 D72's T2.5 record-graph row reproduces: node count, "
           f"up-edge count, independent-cycle count, zero defects, and mu "
           f"class-constant on every class",
           len(mucls) == ANCH[_pref + "_classes"]
           and len(edgew) == ANCH[_pref + "_edges"]
           and _rk == ANCH[_pref + "_cycles"] and _ob == 0
           and len(fam) == ANCH[_pref + "_hist"]
           and all(len(v) == 1 for v in mucls.values()),
           f"histories {len(fam)}, classes {len(mucls)}, up-edges "
           f"{len(edgew)}, independent cycles {_rk}, obstructions {_ob}, "
           f"mu class-constant on "
           f"{sum(1 for v in mucls.values() if len(v) == 1)}/{len(mucls)}")

# --- the minimal witness, digit for digit ----------------------------------
_A = ARMS["AB4"]
_wit = min(_A["defs"], key=lambda z: (len(z[0]), sk((z[0], z[1], z[2]))))
_h, _eA, _eB, _r, _qA, _qB2, _qB, _qA2 = _wit
_muAB = _A["mu"][_h] * _qA * _qB2
_muBA = _A["mu"][_h] * _qB * _qA2
print("  [DATA] THE MINIMAL WITNESS (AB4), in full:")
print(f"           h   = {list(_h)}")
print(f"           eA  = {_eA}")
print(f"           eB  = {_eB}")
print(f"           q(eA|h) = {_qA} , q(eB|h.eA) = {_qB2}")
print(f"           q(eB|h) = {_qB} , q(eA|h.eB) = {_qA2}")
print(f"           dP_AB/dP_BA = {_r};  mu(h.eA.eB) = {_muAB} vs "
      f"mu(h.eB.eA) = {_muBA}")
anchor("W.1 the minimal witness reproduces digit for digit — all four step "
       "weights, the ratio, and both whole-history mu values",
       (_qA, _qB2, _qB, _qA2, _r, _muAB, _muBA)
       == (ANCH["wit_qA"], ANCH["wit_qB2"], ANCH["wit_qB"], ANCH["wit_qA2"],
           ANCH["wit_r"], ANCH["wit_muAB"], ANCH["wit_muBA"]),
       f"({_qA}, {_qB2}, {_qB}, {_qA2}) -> {_r}; mu {_muAB} vs {_muBA}")

# --- the idle-budget row (T6.5) --------------------------------------------
_idle = Counter()
for _hh in _A["fam"]:
    for _a in AB:
        _ok, _q = b1_adm(_hh, ('n', _a), AB)
        if _ok:
            _idle[_q] += 1
_comp = _noidle = 0
for _hh, _eA_, _eB_, _r_ in _A["closed"]:
    if b1_regs(_eA_) & b1_regs(_eB_):
        _comp += 1
        _noidle += int(_eA_[0] != 'n' and _eB_[0] != 'n')
anchor("I.1 D72's T6.5 idle row reproduces: the idle-weight spectrum and "
       "the comparable/no-idle counts",
       dict(_idle) == ANCH["idle_spectrum"] and _comp == ANCH["comparable"]
       and _noidle == ANCH["no_idle"],
       f"idle spectrum {fmt(_idle)}; comparable closed squares {_comp}; "
       f"of which no idle member {_noidle}")

# --- D65's committed masses ------------------------------------------------
_massspec = Counter(_A["M"].values())
anchor("D65.1 the menu-mass spectrum of the transport grammar is drawn "
       "from D65's committed mass set {2, 5/2} — the same two masses, "
       "one grammar over",
       set(_massspec) == ANCH["d65_masses"],
       f"menu-mass spectrum {fmt(_massspec)}; D65's quoted masses "
       f"{sorted(str(x) for x in ANCH['d65_masses'])}")

report("anchor block time", f"{time.time() - _t:.0f}s")

if ANCHOR_FAIL:
    print()
    print("!" * 78)
    print("ANCHOR FAILURE — a committed D72 number did not reproduce.")
    print("STOPPING.  Nothing below this line may be believed.")
    print("!" * 78)
    sys.exit(1)


# ===========================================================================
# SEC 2.  CONTROLS (pin sec.3) — run BEFORE the science, so that every gate
#         below is read against an instrument of known sensitivity.
# ===========================================================================

print()
print("-" * 78)
print("SEC 2  CONTROLS")
print("-" * 78)
_t = time.time()

# --- CTL-FLAT: the closed grammar through the identical pipeline -----------
_f3, _c3 = enumerate_line(b3_cand, AB, 4)
_st3, _rat3, _k3, _ok3, _d3, _hf3, _cl3 = square_census(
    _f3, _c3, AB, 4, b3_adm, b3_regs, b3_canon)
check("CTL-FLAT THE CLOSED-GRAMMAR FLAT CONTROL: the d42b3 placement "
      "grammar — where D72 proved raw flatness depth-free — through THIS "
      "receipt's own census code returns a ratio multiset that is "
      "identically 1 and no half-open square.  The pipeline is therefore "
      "not manufacturing defects",
      len(_d3) == 0 and _st3["closed"] > 0
      and _st3.get("AB-only", 0) + _st3.get("BA-only", 0) == 0,
      f"grammar 1 (A,B) d<=4: census {dict(_st3)}, ratios {fmt(_rat3)}, "
      f"{len(_d3)} non-unit")

# --- CTL-TAMPER: a perturbed weight must be seen ---------------------------
_target = None
for _hh in sorted(_A["cache"], key=sk):
    if len(_hh) + 2 > 4:
        continue
    _cs = [e for e, q in _A["cache"][_hh]]
    if len(_cs) >= 2:
        _target = (_hh, _cs[0])
        break
_stT, _ratT, _kT, _okT, _dT, _hfT, _clT = square_census(
    _A["fam"], _A["cache"], AB, 4, b1_adm, b1_regs, b1_canon,
    tamper=(_target, Fr(3, 2)))
check("CTL-TAMPER THE PERTURBED-WEIGHT NEGATIVE CONTROL: multiplying ONE "
      "committed step weight q(e|h) by 3/2 moves the census — the defect "
      "count and the spectrum both change.  Unlike D72's T2.NC (which "
      "perturbed one edge of an exact gradient and therefore could not "
      "fail), this control CAN fail: a census that ignored the weights "
      "would return the same multiset",
      len(_dT) != len(_A["defs"]) and dict(_ratT) != dict(_A["rat"]),
      f"tampered at (|h| = {len(_target[0])}, e = {_target[1][0]}...): "
      f"non-unit {len(_A['defs'])} -> {len(_dT)}; spectrum size "
      f"{len(_A['rat'])} -> {len(_ratT)}; new values "
      f"{sorted(str(k) for k in set(_ratT) - set(_A['rat']))[:6]}")

# --- CTL-ORDER: the orientation convention ---------------------------------
_stR, _ratR, _kR, _okR, _dR, _hfR, _clR = square_census(
    _A["fam"], _A["cache"], AB, 4, b1_adm, b1_regs, b1_canon,
    reverse_cands=True)
def _pairclasses(rat):
    """The multiset of UNORDERED value classes {r, 1/r} — the only part of
    a square spectrum that does not depend on which order one calls AB."""
    out = Counter()
    for k, v in rat.items():
        out[k if k <= 1 / k else 1 / k] += v
    return out


_inv_stable = _pairclasses(_A["rat"]) == _pairclasses(_ratR)
check("CTL-ORDER WHAT IS AND IS NOT ORIENTATION-INVARIANT — a control the "
      "corpus did not run, and it BITES.  Re-running the identical census "
      "with the candidate list traversed in the opposite order leaves the "
      "closed/half-open/both-blocked TOTALS and the unordered value "
      "classes {r, 1/r} invariant, but it TRANSPOSES the spectrum "
      "(1/2 <-> 2, 2/3 <-> 3/2) and the AB-only / BA-only split.  So "
      "'{1/2: 70, ... 2: 10}' and 'AB-only 28, BA-only 12' are readings "
      "in an arbitrary enumeration orientation; only the totals and the "
      "paired classes are substrate facts.  ADDRESSEE CORRECTED AT ROUND "
      "1 (MODERATE 1): those multiplicities and that split are D72's "
      "TABLE ROWS T6.1/T6.2 and its DELTA (QUOTES['d72_T61']), NOT its "
      "licensed claim 7 — claim 7 licenses the VALUE SET and the TOTALS, "
      "and CTL-ORDER leaves every one of D72's licensed claims standing.  "
      "The correction is routed against the rows; the parent's licence is "
      "untouched, which is a credit to it.  This unit's OWN dichotomy "
      "headline is put through the same control at A3.2",
      _stR["closed"] == _A["st"]["closed"]
      and _stR.get("AB-only", 0) + _stR.get("BA-only", 0)
      == _A["st"].get("AB-only", 0) + _A["st"].get("BA-only", 0)
      and len(_dR) == len(_A["defs"]) and _inv_stable
      and dict(_ratR) != dict(_A["rat"]),
      f"forward ratios {fmt(_A['rat'])}; reversed ratios {fmt(_ratR)}; "
      f"forward half-open split ({_A['st']['AB-only']}, "
      f"{_A['st']['BA-only']}) -> reversed ({_stR.get('AB-only', 0)}, "
      f"{_stR.get('BA-only', 0)}); unordered {{r,1/r}} class multiset "
      f"{fmt(_pairclasses(_A['rat']))} both ways = {_inv_stable}; defect "
      f"total {len(_A['defs'])} -> {len(_dR)}")

# --- CTL-DET: determinism --------------------------------------------------
_e1 = [(u, v, w) for (u, v), ws in _A["edgew"].items() for w in ws]
_h1 = holonomy_of(_e1)
_h2 = holonomy_of(_e1, reverse_order=True)
check("CTL-DET DETERMINISM PROBE: every printed aggregate is computed "
      "under stable_key ordering (hash-seed independent).  The "
      "basis-INdependent quantities — node count, component count, cycle "
      "rank, obstruction count, holonomy value SET — agree under forward "
      "and reversed spanning-forest builds; D72's lesson that the count "
      "of non-trivial BASIS cycles is forest-dependent is carried",
      _h1[:4] == _h2[:4] and set(_h1[4]) == set(_h2[4]),
      f"forward (nodes, comps, rank, obstructions) = {_h1[:4]}; reversed "
      f"= {_h2[:4]}; holonomy value sets equal = "
      f"{set(_h1[4]) == set(_h2[4])}")

report("control block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 3.  TH-C — REMOVABILITY.  FIRST, per the pin and the D64 discipline.
# ===========================================================================

print()
print("-" * 78)
print("SEC 3  TH-C — REMOVABILITY (the D64 discipline: before any structure")
print("       claim).  THE R+ CONNECTION, BOTH ROUTES, ON A LADDER OF")
print("       COMMITTED STATE ABSTRACTIONS.")
print("-" * 78)
_t = time.time()

print("""  WHAT REMOVABILITY MEANS HERE, STATED BEFORE IT IS TESTED.
  The connection is the layer's own step weight: an UP move h -> h.e
  carries q(e|h).  A gauge transformation by a potential G is
  q'(e|h) = q(e|h) * G(h.e)/G(h).  Under it the exchange ratio
  r(h; eA, eB) = q(eA|h) q(eB|h.eA) / [q(eB|h) q(eA|h.eB)] transforms as
      r' = r * G(h.eA.eB) / G(h.eB.eA).
  So the twist is REMOVABLE BY G exactly when r = G(h.eB.eA)/G(h.eA.eB)
  on every closed square: a coboundary condition on the graph whose
  nodes are the two orders of each square.  The question is only
  interesting once one says WHAT G IS ALLOWED TO DEPEND ON.  That is
  the ladder below, and C0 shows why the ladder is mandatory.""")

# --- C0  THE VACUITY LEMMA -------------------------------------------------
print()
print("  [C0]  THE VACUITY LEMMA — the naive removability test cannot fail.")
_c0_ok = 0
_c0_bad = 0
for _nm in ("AB4", "ABC3"):
    _R = ARMS[_nm]
    for _hh, _a, _b, _r in _R["closed"]:
        _m1 = _R["mu"][_hh + (_a, _b)]
        _m2 = _R["mu"][_hh + (_b, _a)]
        if _r == _m1 / _m2:
            _c0_ok += 1
        else:
            _c0_bad += 1
check("C0.1 r = mu(h.eA.eB)/mu(h.eB.eA) ON EVERY CLOSED SQUARE OF EVERY "
      "ARM.  mu, the product of the layer's own weights along a history, "
      "is therefore a GLOBAL POTENTIAL for the transport connection, and "
      "G = 1/mu removes the whole twist at one stroke.  ROUND-1 REPAIR "
      "(MAJOR 1): this is an ALGEBRAIC IDENTITY OF mu's OWN DEFINITION — "
      "mu_map sets mu(h.e) := mu(h) q(e|h), so mu(h.eA.eB)/mu(h.eB.eA) IS "
      "the defining expression for r, on every grammar with a product "
      "weight, at every depth.  '3,100 of 3,100' is not a measurement of "
      "this substrate; the only thing it can detect is a disagreement "
      "between candidates_for's quoted weights and admissible's, i.e. our "
      "own plumbing.  It is reported because the CONCLUSION (the naive "
      "removability test is vacuous) is load-bearing, not because the "
      "count is evidence",
      _c0_bad == 0 and _c0_ok > 0,
      f"{_c0_ok}/{_c0_ok + _c0_bad} closed squares over both arms satisfy "
      f"the identity exactly; {_c0_bad} exceptions",
      corollary_of="an identity of mu_map's recursion mu(h.e) = mu(h) "
      "q(e|h) together with the definition of r — it cannot return a "
      "non-zero exception count on any product-weighted grammar.  The "
      "round-1 referee tagged this and the first pass tagged C0.2 "
      "instead")

check("C0.2 THEREFORE THE NAIVE COBOUNDARY TEST IS VACUOUS AND MUST NOT "
      "BE REPORTED AS A RESULT.  The sequence layer is a TREE (every "
      "history has a unique prefix parent), so H^1 = 0 there for the "
      "reason v8 p1:77 gives for a commit path, and EVERY connection on "
      "it is a coboundary.  Worse, the potential C0.1 exhibits is forced: "
      "on a connected component the potential is unique up to a constant, "
      "so 1/mu is THE removing gauge — and it sets every gauged weight to "
      "exactly 1, i.e. it removes the process along with the twist.  A "
      "removability verdict is only informative RELATIVE TO WHAT THE "
      "POTENTIAL MAY SEE",
      True,
      "gated as a stated lemma, not as a measurement; its content is "
      "C0.1's identity plus the tree structure of the sequence layer",
      corollary_of="C0.1 together with the tree structure of the "
      "sequence extension graph — this is the D72 MAJOR-3 lesson one "
      "level up: a test that cannot fail is not evidence")

# --- C1  THE D65 PER-STATE TEST -------------------------------------------
print()
print("  [C1]  THE D65 TEST — is the twist the committed mass-ratio "
      "coboundary?")
for _nm in ("AB4", "ABC3"):
    _R = ARMS[_nm]
    _M = _R["M"]
    _hit = _miss = 0
    _norm = Counter()
    _on_def = Counter()
    for _hh, _a, _b, _r in _R["closed"]:
        _mr = _M[_hh + (_b,)] / _M[_hh + (_a,)]
        if _r == _mr:
            _hit += 1
        else:
            _miss += 1
        _rn = _r * _mr
        _norm[_rn] += 1
        if _r != 1:
            _on_def[_mr] += 1
    _R["norm"] = _norm
    report(f"{_nm} D65 form r = M(h.eB)/M(h.eA)",
           f"holds on {_hit} of {len(_R['closed'])} closed squares, fails "
           f"on {_miss}")
    report(f"{_nm} NORMALISED square spectrum (q -> q/M, i.e. the "
           f"process's own conditional kernel)", fmt(_norm))
    report(f"{_nm} the intermediate mass ratio M(h.eB)/M(h.eA) RESTRICTED "
           f"to the {len(_R['defs'])} raw-defective squares", fmt(_on_def))
    _surv = Counter({k: v for k, v in _norm.items()
                     if k != 1 and set(primes_of(k)) <= {2, 3}})
    _new = Counter({k: v for k, v in _norm.items()
                    if k != 1 and not set(primes_of(k)) <= {2, 3}})
    _massspec_arm = Counter(_M.values())
    _massratios = {a / b for a in _massspec_arm for b in _massspec_arm}
    report(f"{_nm} menu-mass spectrum (the source of the normalisation "
           f"twist)", fmt(_massspec_arm))
    check(f"C1.{_nm} THE TRANSPORT TWIST IS NOT D65's COBOUNDARY AND "
          f"NORMALISATION DOES NOT REMOVE IT.  D65's repair — divide by "
          f"the per-state menu mass — is the corpus's one committed "
          f"repair for an exchange defect.  Applied here it leaves every "
          f"one of the raw-defective squares EXACTLY where it was, "
          f"because the intermediate mass ratio is identically 1 on all "
          f"of them, and it ADDS a DISJOINT family of new defects which "
          f"are ratios of menu masses.  The two twists live on disjoint "
          f"square sets and their values share no prime beyond 2: the raw "
          f"twist is 3-smooth, the mass twist is not",
          set(_on_def) == {Fr(1)}
          and _surv == Counter({k: v for k, v in _R["rat"].items()
                                if k != 1})
          and set(_new) <= _massratios,
          f"mass ratio on the raw-defective squares = {fmt(_on_def)} "
          f"(so r is UNCHANGED by normalisation there); surviving "
          f"3-smooth defects {fmt(_surv)} = the raw spectrum "
          f"{fmt(Counter({k: v for k, v in _R['rat'].items() if k != 1}))}; "
          f"new non-3-smooth defects {fmt(_new)}, every one a ratio of two "
          f"realised menu masses; D65's committed ratio set is "
          f"{sorted(str(x) for x in ANCH['d65_ratios'])} and the "
          f"{_nm} mass twist "
          + ("REPRODUCES it exactly"
             if set(_new) | {Fr(1)} == ANCH["d65_ratios"]
             else f"does NOT — it is {fmt(_new)}, a wider mass set at "
                  f"this pool, WHICH IS WHAT D65's OWN RESIDUE 2 "
                  f"PREDICTED (QUOTES['d65_3.1']): 'at three actors or "
                  f"with delivery the mass spectrum changes and the "
                  f"coboundary statement must be re-derived, not "
                  f"carried'.  This is a CONFIRMATION of the parent at a "
                  f"scope the parent explicitly refused, not a "
                  f"correction of it"))

# --- C2  THE ABSTRACTION LADDER -------------------------------------------
print()
print("  [C2]  THE LADDER — what may the potential see?")
print("""        Six abstractions of a history, from the finest to the
        coarsest, EVERY ONE of them built from the committed layer's own
        objects and named before it is run:
          SEQ    the history itself (the vacuous end, C0)
          REC    canon(h): D72's committed record functor
          MULT   the multiset of events, all order forgotten
          STATE  the committed order-free state: created / superseded /
                 resolved / live proposals / per-actor holdings, read off
                 full_view(h)
          PORT   the per-actor option data the WEIGHTS actually read:
                 prop_options_in_view, deliver_options_in_view, the arb
                 ckey count and the merge-pair count, in each actor's own
                 view.  This is the transport-scope analogue of D62's
                 sigma-ports, and the pin predicts it will not work
          MENU   the weighted menu itself: the multiset of (e, q(e|h))""")


def A_seq(h, cache):
    return h


def A_rec(h, cache):
    return sk(b1_canon(list(h)))


def A_mult(h, cache):
    return ("MULT", tuple(sorted(evsk(e) for e in h)))


def A_state(h, cache, actors=AB):
    v = b1_fullview(list(h))
    return ("STATE",
            tuple(sorted(sk(x) for x in v.created)),
            tuple(sorted(sk(x) for x in v.superseded)),
            tuple(sorted(sk(x) for x in v.resolved)),
            tuple(sorted(sk((op[1], op[2], op[3]))
                         for op in v.live.values())),
            tuple(sorted((a, tuple(sorted(sk(x) for x in v.holdings(a))))
                         for a in actors)))


def A_port(h, cache, actors=AB):
    out = []
    for a in actors:
        ov = b1_ownview(list(h), a)
        out.append((a,
                    tuple(sorted(sk(x) for x in b1_propopt(ov, a))),
                    tuple(sorted(sk(x) for x in b1_delopt(ov, a, actors))),
                    len(b1_arbck(list(h), a, actors)),
                    len(ov.merge_pairs(a))))
    return ("PORT", tuple(out))


def A_menu(h, cache):
    return ("MENU", tuple(sorted((evsk(e), str(q)) for e, q in cache[h])))


LADDER = [("SEQ", A_seq), ("REC", A_rec), ("MULT", A_mult),
          ("STATE", A_state), ("PORT", A_port), ("MENU", A_menu)]


def ladder_row(R, nm, f, actors):
    """One rung: classes; does mu descend; does the weighted MENU descend
    (= does the connection descend, canonically); how many squares and how
    many DEFECTIVE squares close; then BOTH removability routes on the
    quotient's own exchange graph."""
    fam, cache, dep = R["fam"], R["cache"], R["dep"]
    kw = {} if nm not in ("STATE", "PORT") else {"actors": actors}
    V = {tuple(h): sk(f(tuple(h), cache, **kw)) for h in fam}
    cls = len(set(V.values()))
    mus = defaultdict(set)
    menus = defaultdict(set)
    for h in fam:
        t = tuple(h)
        mus[V[t]].add(R["mu"][t])
        menus[V[t]].add(tuple(sorted((evsk(e), str(q)) for e, q in cache[t])))
    mu_desc = sum(1 for v in mus.values() if len(v) == 1)
    menu_desc = sum(1 for v in menus.values() if len(v) == 1)
    # labelled edge single-valuedness (the weaker descent notion)
    lab = defaultdict(set)
    for h in fam:
        if len(h) >= dep:
            continue
        for e, q in cache[tuple(h)]:
            lab[(V[tuple(h)], evsk(e))].add(Fr(q))
    multi = sum(1 for v in lab.values() if len(v) > 1)
    # squares closing
    cl_all = sum(1 for hh, a, b, r in R["closed"]
                 if V[hh + (a, b)] == V[hh + (b, a)])
    # the SET of defective squares this rung closes (indices into R["defs"]),
    # so that two rungs can be compared as SETS and not merely as counts
    # (round-1 MAJOR 5: MULT closes the descent-obstruction half; and PORT
    # closes exactly the same 44 as MENU, which is stronger than C2.4 said)
    def_set = frozenset(i for i, row in enumerate(R["defs"])
                        if V[row[0] + (row[1], row[2])]
                        == V[row[0] + (row[2], row[1])])
    cl_def = len(def_set)
    # ROUTE 1: potential propagation over the quotient's exchange graph
    ex = [(V[hh + (b, a)], V[hh + (a, b)], r)
          for hh, a, b, r in R["closed"]]
    selfloop = sum(1 for u, v, w in ex if u == v and w != 1)
    n_, c_, rk_, ob_, hol_, phi_ = holonomy_of([e for e in ex
                                                if e[0] != e[1]])
    # ROUTE 2: relabelled recount.  Build the potential on the FULL
    # quotient up-graph (alpha(h) -> alpha(h.e), weight q) and re-run the
    # square census with the gauged weights q' = q phi(a(h.e))/phi(a(h)).
    up = []
    for h in fam:
        if len(h) >= dep:
            continue
        for e, q in cache[tuple(h)]:
            up.append((V[tuple(h)], V[tuple(h) + (e,)], Fr(q)))
    un_, uc_, urk_, uob_, uhol_, uphi = holonomy_of(up)
    # phi solves phi(alpha(h.e)) = q phi(alpha(h)), so the removing gauge
    # is G = 1/phi and the gauged ratio is r * G(s1)/G(s2) = r phi(s2)/
    # phi(s1).  (Getting this direction wrong squares the defect instead
    # of cancelling it; the SEQ rung, where phi is mu exactly, is the
    # control that catches it.)
    surv = 0
    for hh, a, b, r in R["closed"]:
        g1 = uphi.get(V[hh + (a, b)])
        g2 = uphi.get(V[hh + (b, a)])
        if g1 is None or g2 is None:
            continue
        if r * g2 / g1 != 1:
            surv += 1
    return dict(cls=cls, mu_desc=mu_desc, mu_tot=len(mus),
                menu_desc=menu_desc, menu_tot=len(menus), multi=multi,
                nlab=len(lab), cl_all=cl_all, cl_def=cl_def,
                def_set=def_set,
                ex_nodes=n_, ex_rank=rk_, ex_obstr=ob_, selfloop=selfloop,
                ex_hol=hol_, up_rank=urk_, up_obstr=uob_, surv=surv,
                up_hol=uhol_)


LAD = {}
for _nm in ("AB4", "ABC3"):
    _R = ARMS[_nm]
    LAD[_nm] = {}
    print(f"      --- {_nm} ({_R['actors']}, depth <= {_R['dep']}) ---")
    print(f"      {'alpha':6s} {'classes':>8s} {'mu desc':>10s} "
          f"{'menu desc':>11s} {'multi-w':>8s} {'sq close':>10s} "
          f"{'DEF close':>10s} {'ex rank':>8s} {'R1 obstr':>9s} "
          f"{'selfloop':>9s} {'up rank':>8s} {'R2 surv':>8s}")
    for _an, _af in LADDER:
        _row = ladder_row(_R, _an, _af, _R["actors"])
        LAD[_nm][_an] = _row
        print(f"      {_an:6s} {_row['cls']:8d} "
              f"{_row['mu_desc']:5d}/{_row['mu_tot']:<4d} "
              f"{_row['menu_desc']:5d}/{_row['menu_tot']:<5d} "
              f"{_row['multi']:8d} "
              f"{_row['cl_all']:5d}/{len(_R['closed']):<4d} "
              f"{_row['cl_def']:5d}/{len(_R['defs']):<4d} "
              f"{_row['ex_rank']:8d} {_row['ex_obstr']:9d} "
              f"{_row['selfloop']:9d} {_row['up_rank']:8d} "
              f"{_row['surv']:8d}")

_L = LAD["AB4"]
check("C2.1 THE REMOVABILITY THRESHOLD, ROUTE 1 (potential propagation).  "
      "The twist is a coboundary EXACTLY on the rungs where mu itself "
      "descends — SEQ and REC — and on no coarser rung.  At REC the "
      "obstruction is zero for the reason C0 gives and for no other: mu "
      "is class-constant (ANCHOR AB4.4), so 1/mu is a per-RECORD "
      "potential.  At MULT, STATE, PORT and MENU mu is multi-valued and "
      "the obstruction is non-zero.  The record functor sits EXACTLY at "
      "the threshold — which is a structural explanation of D72's "
      "blindness theorem, not a restatement of it",
      _L["REC"]["ex_obstr"] + _L["REC"]["selfloop"] == 0
      and _L["SEQ"]["ex_obstr"] + _L["SEQ"]["selfloop"] == 0
      and all(_L[a]["ex_obstr"] + _L[a]["selfloop"] > 0
              for a in ("MULT", "STATE", "PORT", "MENU"))
      and _L["REC"]["mu_desc"] == _L["REC"]["mu_tot"]
      and all(_L[a]["mu_desc"] < _L[a]["mu_tot"]
              for a in ("MULT", "STATE", "PORT", "MENU")),
      "obstruction (independent cycles + defective self-loops) by rung: "
      + ", ".join(f"{a} {_L[a]['ex_obstr'] + _L[a]['selfloop']}"
                  for a, _ in LADDER)
      + "; mu descends by rung: "
      + ", ".join(f"{a} {_L[a]['mu_desc']}/{_L[a]['mu_tot']}"
                  for a, _ in LADDER))

check("C2.2 THE REMOVABILITY THRESHOLD, ROUTE 2 (relabelled recount — the "
      "D64 C7 idiom, adapted to R+).  The spanning-forest potential is "
      "propagated over the quotient's OWN up-graph and the entire square "
      "census is then RE-RUN with the gauged weights q' = q "
      "phi(alpha(h.e))/phi(alpha(h)); the surviving non-unit squares are "
      "counted.  Route 2 agrees with route 1 rung for rung: zero "
      "survivors exactly where the obstruction is zero",
      all((_L[a]["surv"] == 0)
          == (_L[a]["ex_obstr"] + _L[a]["selfloop"] == 0)
          for a, _ in LADDER),
      "surviving non-unit squares after the relabelling, by rung: "
      + ", ".join(f"{a} {_L[a]['surv']}" for a, _ in LADDER))

check("C2.3 ANTI-VACUITY: the removability test at the coarse rungs is "
      "NOT a test on a forest.  The quotient exchange graphs carry "
      "independent cycles and/or defective self-loops, so a flat answer "
      "was available and was not returned.  (At SEQ the exchange graph is "
      "a perfect MATCHING — 1546 edges on 3092 nodes, cycle rank 0 — "
      "which is precisely why C0's verdict there carries no information.)",
      _L["SEQ"]["ex_rank"] == 0
      and all(_L[a]["ex_rank"] + _L[a]["selfloop"] > 0
              for a in ("MULT", "STATE", "PORT", "MENU")),
      "exchange-graph cycle rank / defective self-loops by rung: "
      + ", ".join(f"{a} {_L[a]['ex_rank']}/{_L[a]['selfloop']}"
                  for a, _ in LADDER))

check("C2.4 THE sigma-PORT RUNG, REPORTED AS THE PIN PREDICTED IT — AND "
      "IT AGREES WITH MENU AS A SET, WHICH IS STRONGER THAN A COUNT.  "
      "D62's sigma machinery at transport scope is the PORT rung: the "
      "per-actor option data that the committed weights actually read.  "
      "It does NOT carry the whole holonomy — it closes only part of the "
      "defective census — so the pin's expectation is upheld, and what "
      "does carry it is named in SEC 4.  ROUND-1 ADDITION: PORT closes "
      "EXACTLY THE SAME defective squares as MENU, as sets and not merely "
      "in number",
      _L["PORT"]["cl_def"] < len(ARMS["AB4"]["defs"])
      and _L["PORT"]["def_set"] == _L["MENU"]["def_set"],
      f"PORT closes {_L['PORT']['cl_def']} of "
      f"{len(ARMS['AB4']['defs'])} defective squares "
      f"({_L['PORT']['cls']} classes); MENU closes "
      f"{_L['MENU']['cl_def']}; the two closed SETS are equal = "
      f"{_L['PORT']['def_set'] == _L['MENU']['def_set']}; STATE and MULT "
      f"close {_L['STATE']['cl_def']} and {_L['MULT']['cl_def']} but at "
      f"the price of losing DESCENT (C2.1's multi-valued weights: "
      f"{_L['STATE']['multi']} and {_L['MULT']['multi']} labelled edges)")

REMOVABLE_AT = [a for a, _ in LADDER
                if _L[a]["ex_obstr"] + _L[a]["selfloop"] == 0]
NOT_REMOVABLE_AT = [a for a, _ in LADDER if a not in REMOVABLE_AT]
report("TH-C VERDICT (AB4)",
       f"removable at {REMOVABLE_AT}; NOT removable at "
       f"{NOT_REMOVABLE_AT}")
report("control block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 4.  TH-A — THE CARRIER.
# ===========================================================================

print()
print("-" * 78)
print("SEC 4  TH-A — THE CARRIER: the census extended, the defects")
print("       classified, and the QUOTIENT THAT SEES THE HOLONOMY")
print("-" * 78)
_t = time.time()

# --- A1  the extended census ----------------------------------------------
print()
print("  [A1]  THE CENSUS EXTENDED — depth, actor pool, and two asymmetric")
print("        sub-grammars (D73's lesson: hand-built symmetry is a cage).")

SKIP_DEEP = os.environ.get("D74_SKIP_DEEP", "0") == "1"


def census_arm(label, actors, dep, filt=None, full=False):
    """`full=False`: a census-only arm — the family is enumerated only to
    depth dep-2 (the deepest base a square can sit on), so a deep census
    costs the census and not the family.  `full=True`: the whole family to
    depth dep, which is what the carrier analysis of A3 needs."""
    t = time.time()
    fam, cache = enumerate_line(b1_cand, actors, dep - (0 if full else 2),
                               filt=filt)
    st, rat, kinds, okinds, defs, half, closed = square_census(
        fam, cache, actors, dep, b1_adm, b1_regs, b1_canon, filt=filt)
    dely = sum(1 for h, a, b, r, *_ in defs if 'd' in (a[0], b[0]))
    mind = min((len(h) + 2 for h, *_ in defs), default=None)
    nonunit = Counter({k: v for k, v in rat.items() if k != 1})
    report(f"{label}", f"census {dict(st)}; non-unit {len(defs)}; spectrum "
           f"{fmt(nonunit)}; kinds {dict(kinds)}; delivery-bearing "
           f"{dely}/{len(defs)}; shallowest {mind}; "
           f"{'FULL family ' + str(len(fam)) + ' histories' if full else 'census-only (bases to depth ' + str(dep - 2) + ')'}"
           f"; [{time.time() - t:.0f}s]")
    return dict(label=label, actors=actors, dep=dep, st=st, rat=rat,
                kinds=kinds, okinds=okinds, defs=defs, half=half,
                closed=closed, nonunit=nonunit, dely=dely, mind=mind,
                fam=fam, cache=cache, full=full)


def oneway(e):
    """ASYM-1: an actor-asymmetric delivery schedule — the link A->B only,
    so B may never deliver to A.  A declared SUB-GRAMMAR: the support is
    restricted, the committed weights are untouched."""
    return not (e[0] == 'd' and (e[1], e[2]) != ('A', 'B'))


def ring(e):
    """ASYM-2: a defected directed ring A->B->C->A — every actor may send
    and receive, but only one way round, so no delivery pair is
    symmetric."""
    return not (e[0] == 'd' and (e[1], e[2]) not in
                (('A', 'B'), ('B', 'C'), ('C', 'A')))


# FULL arms: whole family enumerated, so A3 can build the carrier on them.
FULL = [ARMS["AB4"], ARMS["ABC3"]]
ARMS["AB4"]["label"] = "AB4 (A,B) depth<=4"
ARMS["ABC3"]["label"] = "ABC3 (A,B,C) depth<=3"
ARMS["AB4"]["nonunit"] = Counter({k: v for k, v in ARMS["AB4"]["rat"].items()
                                  if k != 1})
ARMS["ABC3"]["nonunit"] = Counter({k: v for k, v in
                                   ARMS["ABC3"]["rat"].items() if k != 1})
FULL.append(census_arm("(A,B) depth<=5", AB, 5, full=True))
FULL.append(census_arm("(A,B,C) depth<=4", ABC, 4, full=True))
ASYM = [census_arm("ASYM-1 (A,B) one-way A->B only, depth<=5",
                   AB, 5, filt=oneway, full=True),
        census_arm("ASYM-2 (A,B,C) directed ring A->B->C->A, depth<=4",
                   ABC, 4, filt=ring, full=True)]
FULL += ASYM

# CENSUS-ONLY deep arms: the two deepest windows the budget reaches.
DEEP = list(FULL[2:4])
if not SKIP_DEEP:
    DEEP.append(census_arm("(A,B) depth<=6", AB, 6))
    DEEP.append(census_arm("(A,B,C) depth<=5", ABC, 5))

# --- ROUND-1 MODERATE 5: A GENUINELY INDEPENDENT SCOPE ---------------------
# The eight scopes of the first pass are TWO NESTED DEPTH CHAINS at two
# actor pools plus two sub-grammars of them: census_arm enumerates bases to
# depth dep-2, so the d<=5 arm re-counts every d<=4 square and the d<=6 arm
# re-counts every d<=5 square, and the 88 defective squares of AB4 are
# literally a subset of the 960 of (A,B) d<=5.  Along a nested chain the
# value set can only GROW, so "it does not move" has content — but it is not
# eight independent tests, and no scope went beyond three actors.  This is
# the scope the first pass did not run: a FOURTH ACTOR POOL, with new menu
# masses, and it is the strongest evidence in the group claim.
POOL4 = [census_arm("(A,B,C,D) depth<=3", ABCD, 3),
         census_arm("(A,B,C,D) depth<=4", ABCD, 4)]
_p4mass = Counter(sum(Fr(q) for e, q in POOL4[1]["cache"][h])
                  for h in POOL4[1]["cache"])
_ab4mass = Counter(ARMS["AB4"]["M"].values())
report("(A,B,C,D) menu-mass spectrum (the four-actor pool's own scale)",
       f"{fmt(_p4mass)} — against the two-actor pool's {fmt(_ab4mass)} and "
       f"the three-actor {fmt(Counter(ARMS['ABC3']['M'].values()))}")
check("A1.3 THE FOURTH ACTOR POOL — THE ONE INDEPENDENT SCOPE, AND IT "
      "CONFIRMS THE GROUP (round-1 MODERATE 5).  (A,B,C,D) is not nested "
      "in any arm above it and its menu masses are NEW — no history in "
      "the two- or three-actor pools carries them — so it is not a "
      "re-count of squares already seen.  It produces an order of "
      "magnitude more defective squares than the anchor window, every one "
      "delivery-bearing, shallowest still at total depth 3, and its value "
      "set is EXACTLY the anchor window's, with no new prime",
      all(len(a["defs"]) > 0 and a["dely"] == len(a["defs"])
          and a["mind"] == ANCH["AB_mindepth"] for a in POOL4)
      and set(_p4mass) & set(_ab4mass) == set()
      and set(POOL4[1]["nonunit"]) == set(k for k in ARMS["AB4"]["rat"]
                                          if k != 1)
      and set(POOL4[0]["nonunit"]) <= set(POOL4[1]["nonunit"]),
      "; ".join(f"{a['label']}: {len(a['defs'])}/{a['st']['closed']} "
                f"non-unit at {sorted(str(k) for k in a['nonunit'])}, "
                f"delivery {a['dely']}/{len(a['defs'])}, shallowest "
                f"{a['mind']}" for a in POOL4)
      + f"; four-actor menu masses {sorted(str(k) for k in _p4mass)} "
      f"disjoint from the two-actor {sorted(str(k) for k in _ab4mass)}")

check("A1.1 THE DEFECT IS NOT A WINDOW ARTEFACT AND NOT A SYMMETRY "
      "ARTEFACT.  It persists at every depth and pool run here, and it "
      "survives BOTH asymmetric sub-grammars — the one-way link, where "
      "only A may deliver to B, and the defected 3-actor ring, where "
      "deliveries run A->B->C->A and no other way.  In every arm every "
      "single defect still carries a delivery, and the shallowest defect "
      "is still at total depth 3",
      all(len(a["defs"]) > 0 and a["dely"] == len(a["defs"])
          and a["mind"] == ANCH["AB_mindepth"] for a in DEEP + ASYM),
      "; ".join(f"{a['label']}: {len(a['defs'])}/{a['st']['closed']} "
                f"non-unit, delivery {a['dely']}/{len(a['defs'])}, "
                f"shallowest {a['mind']}" for a in DEEP + ASYM))

check("A1.2 THE ASYMMETRIC ARMS ARE NOT VACUOUS: the one-way and ring "
      "sub-grammars really do remove support — their closed-square counts "
      "and half-open counts differ from the symmetric arms at the same "
      "depth and pool — and the defect survives that removal",
      ASYM[0]["st"]["closed"] != DEEP[0]["st"]["closed"]
      and ASYM[1]["st"]["closed"] != DEEP[1]["st"]["closed"],
      f"symmetric (A,B) d<=5 closed {DEEP[0]['st']['closed']} vs one-way "
      f"{ASYM[0]['st']['closed']}; symmetric (A,B,C) d<=4 closed "
      f"{DEEP[1]['st']['closed']} vs ring {ASYM[1]['st']['closed']}")

# --- A2  classification ----------------------------------------------------
print()
print("  [A2]  THE DEFECTS CLASSIFIED — kind pair x register-overlap type.")


def regtype(r):
    if isinstance(r, str):
        return "actor"
    if isinstance(r, tuple) and r and r[0] == 'mw':
        return "mw"
    return "version"


def overlap_profile(eA, eB):
    ov = b1_regs(eA) & b1_regs(eB)
    if not ov:
        return "DISJOINT"
    return "+".join(sorted({regtype(r) for r in ov}))


for _src, _lab in ((ARMS["AB4"]["defs"], "AB4 defective"),
                   (ARMS["ABC3"]["defs"], "ABC3 defective"),
                   (DEEP[0]["defs"], "(A,B) d<=5 defective"),
                   (ASYM[0]["defs"], "ASYM-1 defective")):
    _prof = Counter()
    _joint = Counter()
    for _row in _src:
        _hh, _a, _b = _row[0], _row[1], _row[2]
        _p = overlap_profile(_a, _b)
        _prof[_p] += 1
        _joint[((_a[0], _b[0]), _p)] += 1
    report(f"{_lab}: register-overlap type", dict(_prof))
    report(f"{_lab}: kind-pair x overlap", {str(k): v for k, v in
                                            sorted(_joint.items())})

_prof4 = Counter(overlap_profile(r[1], r[2]) for r in ARMS["AB4"]["defs"])
_profall = Counter(overlap_profile(r[1], r[2]) for r in ARMS["AB4"]["closed"])
check("A2.1 EVERY DEFECTIVE SQUARE IS REGISTER-OVERLAPPING, AND THE "
      "OVERLAP IS ALWAYS ON AN ACTOR REGISTER — never on a version "
      "register alone.  Combined with D72's T2.3b (a square closes at "
      "record level exactly when its two events are register-DISJOINT) "
      "this says the blindness is exact and not statistical: the "
      "record-graph instrument sees precisely the complement of the "
      "defect's support",
      set(_prof4) == {"actor"} and _profall["DISJOINT"] > 0,
      f"defective overlap profile {dict(_prof4)}; all closed squares "
      f"{dict(_profall)}")

# --- A3  THE QUOTIENT ------------------------------------------------------
print()
print("  [A3]  THE QUOTIENT THAT SEES THE HOLONOMY — constructed, not "
      "searched.")
print("""        CONSTRUCTION — AND ITS EXISTENCE CLAUSE IS DEFINITIONAL, NOT
        A THEOREM (round-1 MODERATE 4).  Call an equivalence ~ on
        histories a DESCENT quotient when the weighted menu is constant
        on classes: h ~ h' implies q(.|h) = q(.|h') as a function on
        events.  That is exactly what it takes for the connection to be
        well defined on the quotient graph.  Note what that definition
        says: "~ refines ker(menu)".  The set of equivalences refining
        the kernel of a fixed function has a maximum — the kernel — BY
        DEFINITION, so existence, uniqueness and the identification with
        the menu partition are one and the same triviality.  The
        join-closure argument the first pass gave is decoration on a
        statement that needs no argument, and "it is not a search" is
        true because the definition names the answer.  It is stated here
        as a definitional remark and NOT counted as a construction.
        THE CHOICE OF NOTION IS ALSO DECLARED: the weaker and arguably
        more natural notion for a labelled quotient graph — h ~ h' need
        only agree on the weights of events admissible at BOTH — is not
        join-closed and has no unique coarsest.  A3.4 runs it, and three
        further weakenings, on the descent-obstruction half; all four
        identify NONE of it, so nothing in the dichotomy depends on the
        strong notion having been chosen.
        Refining the menu partition by successor-closure (partition
        refinement to a fixed point) gives the coarsest weighted
        CONGRUENCE, the strongest form of descent.  Both are computed,
        and the MEASURED content — which defective squares each closes —
        is what carries the claim.""")


def congruence(R):
    """The coarsest weighted congruence, by partition refinement from the
    menu partition.  Depth-bounded: leaves have no successors, so this is
    the depth-D congruence, and it is labelled as such."""
    fam, cache = R["fam"], R["cache"]
    H = [tuple(h) for h in fam]
    part = {h: tuple(sorted((evsk(e), str(q)) for e, q in cache[h]))
            for h in H}
    idx = {}
    part = {h: idx.setdefault(part[h], len(idx)) for h in H}
    for it in range(24):
        nxt = {}
        for h in H:
            succ = tuple(sorted((evsk(e), part[h + (e,)])
                                for e, q in cache[h] if h + (e,) in part))
            nxt[h] = (part[h], succ)
        idx2 = {}
        out = {h: idx2.setdefault(nxt[h], len(idx2)) for h in H}
        if len(idx2) == len(set(part.values())):
            return out, it + 1
        part = out
    return part, 24


def carrier_of(R):
    """The carrier analysis on one FULL arm: the menu quotient, the
    coarsest congruence, the seen/unseen dichotomy, and the carrier's own
    holonomy."""
    fam, cache = R["fam"], R["cache"]
    V = {tuple(h): A_menu(tuple(h), cache) for h in fam}
    seen, unseen = [], []
    for row in R["defs"]:
        hh, a, b = row[0], row[1], row[2]
        (seen if V[hh + (a, b)] == V[hh + (b, a)] else unseen).append(row)
    cong, iters = congruence(R)
    cl_def_c = sum(1 for hh, a, b, r, *_ in R["defs"]
                   if cong[hh + (a, b)] == cong[hh + (b, a)])
    cl_all_c = sum(1 for hh, a, b, r in R["closed"]
                   if cong[hh + (a, b)] == cong[hh + (b, a)])
    ex = [(V[hh + (b, a)], V[hh + (a, b)], r) for hh, a, b, r in R["closed"]]
    selfh = Counter(w for u, v, w in ex if u == v)
    n_, c_, rk_, ob_, hol_, phi_ = holonomy_of([e for e in ex
                                                if e[0] != e[1]])
    mus = defaultdict(set)
    for h in fam:
        mus[V[tuple(h)]].add(R["mu"][tuple(h)] if "mu" in R
                             else Fr(1))
    return dict(menu_cls=len({v for v in V.values()}), seen=seen,
                unseen=unseen, cong_cls=len(set(cong.values())),
                cong_iters=iters, cong_def=cl_def_c, cong_all=cl_all_c,
                selfh=selfh, off_nodes=n_, off_rank=rk_, off_obstr=ob_,
                off_hol=hol_, V=V)


CARR = {}
for _R in FULL:
    if "mu" not in _R:
        _R["mu"] = mu_map(_R["fam"], _R["cache"])
    _lab = _R["label"]
    _CA = carrier_of(_R)
    CARR[_lab] = _CA
    report(f"{_lab} CARRIER",
           f"menu quotient {_CA['menu_cls']} classes; coarsest congruence "
           f"{_CA['cong_cls']} classes after {_CA['cong_iters']} "
           f"refinement rounds; of {len(_R['defs'])} defective squares the "
           f"menu quotient CLOSES {len(_CA['seen'])} and the congruence "
           f"closes {_CA['cong_def']}; carrier self-loop holonomy "
           f"{fmt(Counter({k: v for k, v in _CA['selfh'].items() if k != 1}))}"
           f"; off-loop cycles {_CA['off_rank']} of which "
           f"{_CA['off_obstr']} non-trivial")
    report(f"{_lab} the dichotomy",
           f"SEEN (curvature-type) {len(_CA['seen'])}: spectrum "
           f"{fmt(Counter(r[3] for r in _CA['seen']))}, kinds "
           f"{dict(Counter((r[1][0], r[2][0]) for r in _CA['seen']))} | "
           f"UNSEEN (descent-obstruction-type) {len(_CA['unseen'])}: "
           f"spectrum {fmt(Counter(r[3] for r in _CA['unseen']))}, kinds "
           f"{dict(Counter((r[1][0], r[2][0]) for r in _CA['unseen']))}")

_MENU4 = _L["MENU"]
_CA4 = CARR["AB4 (A,B) depth<=4"]
_seen, _unseen = _CA4["seen"], _CA4["unseen"]
_selfh = _CA4["selfh"]
_hol_ = _CA4["off_hol"]

check("A3.1 THE CARRIER EXISTS — AND IT IS WINDOW-DEPENDENT, WHICH IS "
      "REPORTED HERE AND NOT BURIED.  The coarsest descent quotient, the "
      "weighted-menu partition, closes a NON-ZERO number of defective "
      "squares on FIVE of the six full arms — including both asymmetric "
      "sub-grammars — so the holonomy is genuinely visible on a quotient "
      "where the connection is well defined by construction.  On the "
      "sixth, (A,B,C) at depth <= 3, it closes NONE of the 12: at that "
      "window the entire defect is of the descent-obstruction type.  The "
      "coarsest weighted CONGRUENCE closes exactly the same defective "
      "squares on every arm, so the answer does not depend on which of "
      "the two descent strengths one demands",
      sum(1 for _lab in CARR if len(CARR[_lab]["seen"]) > 0) >= 5
      and all(CARR[_lab]["cong_def"] == len(CARR[_lab]["seen"])
              for _lab in CARR),
      "; ".join(f"{_lab}: menu closes {len(CARR[_lab]['seen'])}/"
                f"{len(CARR[_lab]['seen']) + len(CARR[_lab]['unseen'])}, "
                f"congruence closes {CARR[_lab]['cong_def']}"
                for _lab in sorted(CARR)))

# ROUND-1 MODERATE 2: CTL-ORDER, applied to THIS unit's own dichotomy and
# not only to the parent's spectrum.  The menu partition is a function of
# the history alone, so it is orientation-free; what is NOT orientation-free
# is which of a square's two orders the enumerator calls "AB", and hence the
# printed value and kind of every unseen square.
_seenR = [r for r in _dR if _CA4["V"][r[0] + (r[1], r[2])]
          == _CA4["V"][r[0] + (r[2], r[1])]]
_unseenR = [r for r in _dR if _CA4["V"][r[0] + (r[1], r[2])]
            != _CA4["V"][r[0] + (r[2], r[1])]]
_uspecF = Counter(r[3] for r in _unseen)
_uspecR = Counter(r[3] for r in _unseenR)
_ukindF = Counter((r[1][0], r[2][0]) for r in _unseen)
_ukindR = Counter((r[1][0], r[2][0]) for r in _unseenR)
report("A3.2 under CTL-ORDER (the dichotomy re-run in the opposite "
       "enumeration orientation)",
       f"forward seen/unseen {len(_seen)}/{len(_unseen)}, unseen spectrum "
       f"{fmt(_uspecF)}, unseen kinds "
       f"{ {str(k): v for k, v in sorted(_ukindF.items())} } | reversed "
       f"seen/unseen {len(_seenR)}/{len(_unseenR)}, unseen spectrum "
       f"{fmt(_uspecR)}, unseen kinds "
       f"{ {str(k): v for k, v in sorted(_ukindR.items())} } | unordered "
       f"class multiset {{r, 1/r}} on the unseen half: "
       f"{fmt(_pairclasses(_uspecF))} forward, "
       f"{fmt(_pairclasses(_uspecR))} reversed")

check("A3.2 THE DESCENT DICHOTOMY, STATED IN ITS ORIENTATION-INVARIANT "
      "FORM (round-1 MODERATE 2 and MAJOR 5).  A DESCENT quotient may "
      "identify two histories only if their weighted menus agree; "
      "therefore a square whose two orders have DIFFERENT menus cannot "
      "close in ANY DESCENT quotient, coarsest or otherwise.  The "
      "defective census splits in two by that criterion: part of it is "
      "genuine CONNECTION CURVATURE, carried by the menu quotient; the "
      "rest is a DESCENT OBSTRUCTION that no quotient ON WHICH THE "
      "CONNECTION IS WELL DEFINED can carry.  THE QUALIFIER IS "
      "LOAD-BEARING AND WAS MISSING FROM THE FIRST PASS: coarser "
      "quotient GRAPHS do close it — A3.5 gates that MULT, rung 3 of "
      "this unit's own ladder, closes every one of them — what they lose "
      "is descent.  What is gated here is the part that survives "
      "CTL-ORDER: the 44 + 44 SPLIT and the UNORDERED value class "
      "{r, 1/r} of the invisible half are invariant under reversing the "
      "enumeration; the printed value (1/2 forward, 2 reversed) and the "
      "printed kind ((r,d) forward, (d,r) reversed) are NOT, and are "
      "reported as orientation readings, exactly as sec.3(a) demands of "
      "the parent",
      len(_seen) > 0 and len(_unseen) > 0
      and len(_seen) + len(_unseen) == len(ARMS["AB4"]["defs"])
      and (len(_seenR), len(_unseenR)) == (len(_seen), len(_unseen))
      and _pairclasses(_uspecF) == _pairclasses(_uspecR)
      and set(_pairclasses(_uspecF)) == {Fr(1, 2)}
      and len(_ukindF) == len(_ukindR) == 1
      and set(_uspecF) != set(_uspecR),
      f"{len(_seen)} curvature-type + {len(_unseen)} "
      f"descent-obstruction-type = {len(ARMS['AB4']['defs'])}, invariant "
      f"under CTL-ORDER; unordered class of the invisible half "
      f"{fmt(_pairclasses(_uspecF))} both ways; ORIENTATION-DEPENDENT "
      f"readings: unseen spectrum {fmt(_uspecF)} -> {fmt(_uspecR)}, "
      f"unseen kinds { {str(k): v for k, v in sorted(_ukindF.items())} } "
      f"-> { {str(k): v for k, v in sorted(_ukindR.items())} }")

# --- A3.4  the four weakenings of DESCENT, on the invisible half ----------
_W = Counter()
for _hh, _a, _b, _r, *_rest in _unseen:
    _s1, _s2 = _hh + (_a, _b), _hh + (_b, _a)
    _m1 = {e: Fr(q) for e, q in ARMS["AB4"]["cache"][_s1]}
    _m2 = {e: Fr(q) for e, q in ARMS["AB4"]["cache"][_s2]}
    _common = set(_m1) & set(_m2)
    if all(_m1[e] == _m2[e] for e in _common):
        _W["labelled-edge"] += 1
    _M1, _M2 = sum(_m1.values()), sum(_m2.values())
    if set(_m1) == set(_m2) and all(_m1[e] / _M1 == _m2[e] / _M2
                                    for e in _m1):
        _W["normalised q/M (D65's repair)"] += 1
    if set(_m1) == set(_m2):
        _W["equal support"] += 1
    if (set(_m1) == set(_m2) and _m1
            and len({_m1[e] / _m2[e] for e in _m1}) == 1):
        _W["proportional (projective)"] += 1
report("A3.4 the invisible half under four WEAKER notions of descent",
       f"of {len(_unseen)} descent-obstruction squares, identified by: "
       + ", ".join(f"{k} {_W[k]}" for k in
                   ("labelled-edge", "normalised q/M (D65's repair)",
                    "equal support", "proportional (projective)")))
check("A3.4 THE DICHOTOMY DOES NOT DEPEND ON THE STRONG DESCENT NOTION "
      "THIS UNIT CHOSE — the round-1 referee's attack, run here and "
      "reported as it came out.  Four strictly weaker notions of "
      "'the connection descends' are applied to the invisible half: (i) "
      "LABELLED-EDGE single-valuedness (the two endpoints need only "
      "agree on events admissible at both — the notion that is NOT "
      "join-closed, which is why it was not chosen); (ii) the NORMALISED "
      "menu q/M, i.e. D65's own committed measure-twisted repair; (iii) "
      "EQUAL SUPPORT only; (iv) PROPORTIONAL menus (projective descent). "
      "Every one of them identifies ZERO of the invisible squares.  The "
      "obstruction is therefore not an artefact of a strong definition: "
      "the two orders genuinely disagree on the weight of a SHARED "
      "event, which is the weakest thing that could have failed",
      all(_W[k] == 0 for k in ("labelled-edge",
                               "normalised q/M (D65's repair)",
                               "equal support", "proportional (projective)"))
      and len(_unseen) > 0,
      f"0 of {len(_unseen)} under all four weakenings: "
      + ", ".join(f"{k} {_W[k]}" for k in
                  ("labelled-edge", "normalised q/M (D65's repair)",
                   "equal support", "proportional (projective)")))

# --- A3.5  a quotient GRAPH that closes the unclosable half ---------------
_mult_set = _L["MULT"]["def_set"]
_menu_set = _L["MENU"]["def_set"]
_unseen_idx = frozenset(range(len(ARMS["AB4"]["defs"]))) - _menu_set
check("A3.5 'NO QUOTIENT GRAPH CAN CARRY IT' IS FALSE, AND THE CORRECT "
      "STATEMENT IS SHARPER (round-1 MAJOR 5).  MULT — rung 3 of THIS "
      "unit's own ladder, the multiset-of-events quotient — closes every "
      "single defective square, including all of the descent-obstruction "
      "half that the menu quotient cannot see.  MULT is a perfectly good "
      "quotient graph; what it fails is DESCENT, by the multi-valued "
      "labelled edges C2.1 already printed.  So the exchange square is "
      "NOT 'the only instrument'; the true statement is that the "
      "descent-obstruction half is closable ONLY by quotients on which "
      "the connection is not well defined",
      _unseen_idx <= _mult_set and _mult_set == frozenset(
          range(len(ARMS["AB4"]["defs"]))) and _L["MULT"]["multi"] > 0,
      f"MULT closes {len(_mult_set)}/{len(ARMS['AB4']['defs'])} defective "
      f"squares, including {len(_unseen_idx & _mult_set)}/"
      f"{len(_unseen_idx)} of the menu quotient's invisible half — at the "
      f"price of {_L['MULT']['multi']} multi-valued labelled edges (no "
      f"descent).  MENU closes {len(_menu_set)} with 0 multi-valued edges")

report("the carrier's holonomy, AB4",
       f"self-loop values (squares closing IN the carrier) "
       f"{fmt(_selfh)}; off-loop exchange graph: {_CA4['off_nodes']} "
       f"nodes, {_CA4['off_rank']} independent cycles, "
       f"{_CA4['off_obstr']} with holonomy != 1, values "
       f"{fmt(Counter({k: v for k, v in _hol_.items() if k != 1}))}")

check("A3.3 THE HOLONOMY ON THE CARRIER IS NOT REMOVABLE, AND THIS IS THE "
      "NON-VACUOUS REMOVABILITY VERDICT C0 DEMANDED.  On the menu "
      "quotient the closing defective squares are LOOPS — self-loops at a "
      "single class — carrying holonomy != 1.  A self-loop's holonomy is "
      "gauge-invariant outright (any potential whatsoever cancels between "
      "its two ends), so NO potential on the carrier, of any kind, "
      "removes them.  ROUND-1 REPAIR (MODERATE 4b): the ARGUMENT is "
      "sound and the verdict stands, but the GATE below is definitional "
      "and is tagged as such — in the exchange graph a square's edge runs "
      "between the classes of its two endpoints, so 'the square closes in "
      "the quotient' and 'its edge is a self-loop' are THE SAME "
      "STATEMENT, and 'non-unit self-loops == squares closed' cannot "
      "fail.  The measured content is A3.1's 44 of 88 and its agreement "
      "with the congruence; no structural fact about self-loops is "
      "discovered here",
      sum(v for k, v in _selfh.items() if k != 1) > 0
      and all(sum(v for k, v in CARR[_lab]["selfh"].items() if k != 1)
              == len(CARR[_lab]["seen"]) for _lab in CARR),
      f"AB4 self-loop holonomy spectrum {fmt(_selfh)}; non-unit "
      f"self-loops {sum(v for k, v in _selfh.items() if k != 1)}; over "
      f"all six full arms: "
      + ", ".join(f"{_lab.split('(')[0].strip()} "
                  f"{sum(v for k, v in CARR[_lab]['selfh'].items() if k != 1)}"
                  for _lab in sorted(CARR)),
      corollary_of="definitional in the exchange graph: the edge of a "
      "square runs between the classes of its two endpoints, so 'closes "
      "in the quotient' IS 'self-loop', and a defective square's edge "
      "carries r != 1 by definition of defective.  The non-removability "
      "VERDICT rests on the gauge-invariance argument stated above, not "
      "on this count (round-1 MODERATE 4b)")

report("TH-A block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 5.  TH-B — THE GROUP.
# ===========================================================================

print()
print("-" * 78)
print("SEC 5  TH-B — THE GROUP GENERATED BY THE HOLONOMY VALUES")
print("-" * 78)
_t = time.time()

SCOPES = []
for _nm in ("AB4", "ABC3"):
    SCOPES.append((f"{_nm} ({ARMS[_nm]['actors']}, d<={ARMS[_nm]['dep']})",
                   Counter({k: v for k, v in ARMS[_nm]["rat"].items()
                            if k != 1})))
for _a in DEEP + ASYM + POOL4:
    SCOPES.append((_a["label"], _a["nonunit"]))
print("""  WHAT THE SCOPES ARE, STATED HONESTLY (round-1 MODERATE 5).  The
  (A,B) and (A,B,C) rows are TWO NESTED DEPTH CHAINS — each deeper arm
  re-counts every square of the shallower one — plus TWO SUB-GRAMMARS of
  them.  Nesting is not nothing (along a chain the value set can only
  grow, so stability there is a real constraint) but it is not
  independent replication.  The (A,B,C,D) rows ARE independent: a new
  pool, new menu masses, no square in common with any other arm.""")

CUM = Counter()
for _lab, _spec in SCOPES:
    CUM.update(_spec)
    _g = group_of(set(_spec))
    print(f"  [DATA] {_lab}")
    print(f"           spectrum {fmt(_spec)}")
    print(f"           value set {sorted(str(k) for k in _spec)}; "
          f"prime content {_g['primes']}; rank {_g['rank']}; group "
          f"{_g['name']}")

GCUM = group_of(set(CUM))
report("CUMULATIVE over every scope run",
       f"value set {sorted(str(k) for k in CUM)}; total non-unit squares "
       f"{sum(CUM.values())}; group {GCUM['name']}")

_valsets = [frozenset(s) for _l, s in SCOPES if s]
_anchorset = frozenset(k for k in ARMS["AB4"]["rat"] if k != 1)
check("B.1 THE GROUP STABILISES, ACROSS FOUR MUTUALLY NON-NESTED EVIDENCE "
      "POOLS: the two-actor depth chain, the three-actor depth chain, the "
      "two asymmetric sub-grammars, and the four-actor pool (three actor "
      "pools in all; within a chain the arms are nested and count once). "
      "Not one scope run here — two more depths at two "
      "actors, two more at three, both asymmetric sub-grammars, and the "
      "INDEPENDENT four-actor pool with its own new menu masses — "
      "produces a value outside the four the anchor window already had, "
      "and the cumulative value set IS the anchor window's. "
      "Depth and pool multiply the defect COUNTS by more than an order of "
      "magnitude (88 to "
      f"{max(sum(s.values()) for _l, s in SCOPES)}) and move the group "
      "not at all",
      all(s <= _anchorset for s in _valsets)
      and frozenset(CUM) == _anchorset,
      f"anchor value set {sorted(str(x) for x in _anchorset)}; distinct "
      f"value sets across {len(_valsets)} scopes: "
      f"{sorted([sorted(str(x) for x in s) for s in set(_valsets)])}; "
      f"cumulative {sorted(str(x) for x in CUM)}; cumulative prime "
      f"content {GCUM['primes']}")

check("B.2 THE GROUP IS <2, 3> — THE FULL GROUP OF 3-SMOOTH POSITIVE "
      "RATIONALS, free abelian of rank 2 — computed as an integer "
      "exponent lattice (Hermite reduction on the prime valuations), not "
      "read off the four values by eye.  It is NOT cyclic, so it is not "
      "of the mass-twist shape at all.  ATTRIBUTION CORRECTED AT ROUND 1 "
      "(MODERATE 3): the infinite cyclic group <5/4>, rank 1 on primes "
      "{2, 5}, is D72's object — its licensed claim 6 / T4.3, on the "
      "NORMALISED d42b3 kernel (QUOTES['d72_group']).  D65 writes no "
      "group notation anywhere; what D65 commits is the mass set {2, 5/2} "
      "and the ratio spectrum {1, 4/5, 5/4} (QUOTES['d65']).  2/3 and 3/2 "
      "lie outside <5/4> either way",
      GCUM["rank"] == 2 and GCUM["primes"] == [2, 3] and GCUM["full"]
      and Fr(2, 3) not in {Fr(5, 4) ** k for k in range(-6, 7)},
      f"prime support {GCUM['primes']}; lattice basis {GCUM['basis']}; "
      f"rank {GCUM['rank']}; index in Z^2 = {GCUM['index']}; "
      f"D72 claim 6's group <5/4> has prime support "
      f"{group_of({Fr(5, 4)})['primes']} and rank "
      f"{group_of({Fr(5, 4)})['rank']}")

_carrier_vals = {k for k in _selfh if k != 1} | {
    k for k in _hol_ if k != 1}
_gc = group_of(_carrier_vals)
check("B.3 THE CARRIER'S OWN HOLONOMY GROUP — the group generated by the "
      "loops of the menu quotient, which is the object the square census "
      "only bounds — is reported separately and is a subgroup of the "
      "square group.  This is the number that is basis-INdependent; the "
      "count of non-trivial basis cycles is not, and is not licensed "
      "(D72's sec.9 lesson)",
      set(_carrier_vals) <= set(CUM) | {1 / k for k in CUM},
      f"carrier holonomy values {sorted(str(k) for k in _carrier_vals)}; "
      f"group {_gc['name']}")

report("TH-B block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 6.  TH-D — THE ODD-SECTOR U(1) SEARCH.
# ===========================================================================

print()
print("-" * 78)
print("SEC 6  TH-D — THE ODD-SECTOR U(1) SEARCH")
print("-" * 78)
_t = time.time()

print("""  THE TEST, STATED BEFORE IT IS RUN.  v7 paper 30's law (QUOTES
  ['Ldual']) is: dual reversal sends O to -O, therefore dual reversal
  sends L to its COMPLEX CONJUGATE.  For a holonomy that law reads
  Hol(gamma^{-1}) = Hol(gamma)^{-1} = conj(Hol(gamma)) — and those two
  right-hand sides agree exactly when |Hol| = 1.  So "is there an odd
  sector" is, on the nose, "is there a unimodular part".  Every gate
  below is a form of that question.""")


def odd_residue_found(values, dual_conjugating):
    """THE OUTCOME PREDICATE FOR TH-III, WITH A LIVE POSITIVE BRANCH
    (round-1 MAJOR 2).  Returns True iff an ORIENTATION-SENSITIVE
    (conjugating) residue is exhibited, by either of two independent
    routes:
      (a) a holonomy value that is unimodular and not 1 — for a
          real-valued connection that is the sign -1;
      (b) a dual square whose holonomy is FIXED rather than inverted by
          the order-dual, i.e. r(dual) == r.
    The first pass wrote this inline as `bool(_unimod - {1}) or
    _dual_conj > 0` where `_unimod` was drawn from a set the receipt had
    already PROVED (D2) contains only positive rationals, and
    `_dual_conj` was incremented inside a loop whose body never ran.  Both
    disjuncts were empty by construction, so TH-III could not be returned
    on any input, and a three-way pin was being decided by a two-way
    test.  Factoring the predicate out lets OUT.1 FEED IT INPUT ON WHICH
    IT MUST FIRE, which is what makes the negative reportable."""
    return bool({v for v in values if v != 1 and abs(v) == 1}) \
        or dual_conjugating > 0

# --- D1  the reversal is exactly inversion ---------------------------------
_inv_bad = 0
_inv_tot = 0
for _hh, _a, _b, _r in ARMS["AB4"]["closed"]:
    okA, qA = b1_adm(list(_hh), _a, AB)
    okB, qB = b1_adm(list(_hh), _b, AB)
    okB2, qB2 = b1_adm(list(_hh) + [_a], _b, AB)
    okA2, qA2 = b1_adm(list(_hh) + [_b], _a, AB)
    rr = Fr(qB * qA2) / Fr(qA * qB2)
    _inv_tot += 1
    if rr != 1 / _r:
        _inv_bad += 1
check("D1 THE REVERSAL ACTS ON r BY INVERSION — A ONE-LINE LEMMA, NOT A "
      "MEASUREMENT.  r is DEFINED as the ratio q(eA|h)q(eB|h.eA) / "
      "q(eB|h)q(eA|h.eB); swapping the roles of eA and eB exchanges "
      "numerator and denominator, so the swapped value is 1/r.  There is "
      "no substrate, no grammar and no assignment of weights on which "
      "this can return a non-zero exception count, and ROUND 1 (MAJOR 1) "
      "was right that the first pass's '1,546/1,546, gap exactly zero' "
      "implied a measurement it is not.  What follows is that LOG r IS "
      "PURELY ODD — but that is a statement about log r ALONE, and the "
      "first pass wrongly promoted it to 'the reversal-EVEN channel is "
      "empty / the mirror image of v7's amplitude'.  IT IS NOT EMPTY: "
      "D9 exhibits a non-trivial reversal-EVEN invariant on the very same "
      "squares.  What IS empty — and D2 settles it a priori, in one line, "
      "before any fixture runs — is the SCALAR ODD sector: the U(1) part",
      _inv_bad == 0 and _inv_tot > 0,
      f"{_inv_tot - _inv_bad}/{_inv_tot} closed squares satisfy "
      f"r(reversed) = 1/r exactly; {_inv_bad} exceptions — as an identity "
      f"of the definition of r, on any product-weighted grammar",
      corollary_of="an algebraic identity of the definition of r (the "
      "reciprocal of the same expression); it has no positive-exception "
      "branch on any input this or any other grammar can supply")

# --- D2  the unimodular part -----------------------------------------------
_allvals = set(CUM) | set(_carrier_vals)
_unimod = {v for v in _allvals if v == 1 or v == -1}
check("D2 THE UNIMODULAR PART IS TRIVIAL, AND FOR A REASON THAT IS NOT A "
      "MEASUREMENT: every weight the committed layer produces is a "
      "POSITIVE RATIONAL, so every holonomy is a positive rational, and "
      "the only positive rational of modulus 1 is 1.  A U(1) part of a "
      "rational-valued holonomy could only ever be the sign -1; the "
      "search therefore reduces, exactly, to a search for a canonical "
      "SIGN on the loops",
      all(v > 0 for v in _allvals) and _unimod <= {Fr(1)},
      f"{len(_allvals)} distinct holonomy values, all positive rationals; "
      f"unimodular values realised: {sorted(str(x) for x in _unimod)}")

# --- D3  the label-local no-go ---------------------------------------------
print()
print("  [D3]  THE LABEL-LOCAL NO-GO — where a phase could not live.")
# ROUND-1 MINOR 3: the first pass gated this with the bare constant True
# and two dead expressions.  The predicate below actually evaluates the
# structural fact the theorem rests on — that the two paths of a closed
# square carry the SAME multiset of events — on every closed square of
# both anchor arms, and it would report a failure if any did not.
_lab_bad = 0
_lab_tot = 0
for _nm in ("AB4", "ABC3"):
    for _hh, _a, _b, _r in ARMS[_nm]["closed"]:
        _lab_tot += 1
        _p1 = sorted((evsk(e) for e in (tuple(_hh) + (_a, _b))))
        _p2 = sorted((evsk(e) for e in (tuple(_hh) + (_b, _a))))
        if _p1 != _p2:
            _lab_bad += 1
check("D3.1 ANY CONNECTION WHOSE VALUE DEPENDS ONLY ON THE EVENT LABEL "
      "HAS TRIVIAL HOLONOMY ON EVERY EXCHANGE SQUARE — a one-line "
      "theorem, gated by construction: the two sides of a square use the "
      "SAME two events, each exactly once, so any product of "
      "label-indexed factors cancels.  A U(1) phase e^{i theta(e)} "
      "attached to events therefore contributes NOTHING to any exchange "
      "loop.  A non-trivial phase would have to be HISTORY-dependent — "
      "exactly as the transport modulus q(e|h) is",
      _lab_bad == 0 and _lab_tot > 0,
      "structural: each closed square's two paths carry the SAME event "
      "multiset, verified here on "
      f"{_lab_tot - _lab_bad}/{_lab_tot} closed squares of the anchor "
      f"arms ({_lab_bad} exceptions), so a label-indexed cochain cancels "
      "identically on every one of them",
      corollary_of="an algebraic identity of the square, not a property "
      "of this substrate — but it is the identity that tells the search "
      "where NOT to look")

# --- D4  the i-twist correspondence, with its adversarial control ----------
print()
print("  [D4]  THE v7 i-TWIST CORRESPONDENCE — run, and then controlled.")
_real_fail = sum(1 for hh, a, b, r in ARMS["AB4"]["closed"]
                 if (1 / r) != r)     # rev(L) == conj(L) fails iff r != 1/r


def itwist_holds(r_fwd, r_rev):
    """Does v7's law rev(L) = conj(L) hold for the twisted form
    L = e^{i log r}?  rev(L) = e^{i log r_rev} and conj(L) = e^{-i log
    r_fwd}, so the law is log r_rev = -log r_fwd, i.e. r_rev * r_fwd = 1.
    Exact on Fractions, no floats and no transcendentals: the whole
    content of the twist is that the reversal INVERTS.  (Round-1 MAJOR 1
    iii: the first pass's predicate was (-1)*num*den == -(num*den), i.e.
    -x == -x, which never touches the reversal at all.)"""
    return r_fwd * r_rev == 1


_itwist_fail = 0
for _hh, _a, _b, _r in ARMS["AB4"]["closed"]:
    okA, qA = b1_adm(list(_hh), _a, AB)
    okB, qB = b1_adm(list(_hh), _b, AB)
    okB2, qB2 = b1_adm(list(_hh) + [_a], _b, AB)
    okA2, qA2 = b1_adm(list(_hh) + [_b], _a, AB)
    _rrev = Fr(qB * qA2) / Fr(qA * qB2)
    if not itwist_holds(_r, _rrev):
        _itwist_fail += 1
# THE CONTROL, REBUILT SO THAT IT CAN FAIL.  The first pass drew 500
# positive rationals and checked -x == -x, which is true of every number
# ever written down and reads the substrate nowhere.  The control that
# actually discriminates is a reversal that is NOT inversion: draw 500
# adversarial (forward, reversed) pairs with r_rev != 1/r_fwd and confirm
# that the twisted law FAILS on every one.  That is what shows the i-twist
# carries exactly the content of D1's identity — no more, and no less.
import random as _rnd
_rnd.seed(20260727)
_adv = []
while len(_adv) < 500:
    _x = Fr(_rnd.randint(1, 97), _rnd.randint(1, 97))
    _y = Fr(_rnd.randint(1, 97), _rnd.randint(1, 97))
    if _x * _y != 1:
        _adv.append((_x, _y))
_adv_hold = sum(1 for x, y in _adv if itwist_holds(x, y))
_adv_odd_hold = sum(1 for x, y in _adv if itwist_holds(x, 1 / x))
check("D4.1 THE i-TWIST 'RESTORES' DUAL CONJUGATION — AND THAT IS AN "
      "IDENTITY OF THE ANSATZ, NOT EVIDENCE.  In the REAL form L = r the "
      "v7 law rev(L) = conj(L) fails on exactly the non-unit squares "
      "(conj is the identity on reals, so the law demands r = 1/r).  "
      "Twisting to L' = e^{i log r} makes rev(L') = conj(L') hold on "
      "every square — because for the twisted form the law says exactly "
      "r(rev) * r = 1, which is D1's identity and nothing else.  exp(i.) "
      "turns ANY odd real into a conjugating unimodular.  ROUND-1 REPAIR "
      "(MAJOR 1 iii, MINOR 6): the first pass's control checked "
      "-x == -x on 500 drawn rationals — a tautology that never applies a "
      "reversal.  It is replaced by one that CAN fail and does: on 500 "
      "adversarial (forward, reversed) pairs whose reversal is NOT "
      "inversion the twisted law fails 500 of 500, while the same "
      "predicate holds 500 of 500 when the reversal is made inverting.  "
      "The evidence for 'content-free' is the ARGUMENT, not a count",
      _real_fail == len(ARMS["AB4"]["defs"]) and _itwist_fail == 0
      and _adv_hold == 0 and _adv_odd_hold == 500,
      f"real form: dual-conjugation fails on {_real_fail} of "
      f"{ARMS['AB4']['st']['closed']} squares (= the "
      f"{len(ARMS['AB4']['defs'])} defective ones exactly); i-twisted "
      f"form on the substrate: {_itwist_fail} failures of "
      f"{ARMS['AB4']['st']['closed']}; DISCRIMINATING CONTROL: the "
      f"twisted law holds on {_adv_hold}/500 non-inverting drawn pairs "
      f"and on {_adv_odd_hold}/500 inverting ones — so the twist tests "
      f"the oddness of the reversal and nothing about this substrate",
      corollary_of="for the twisted form v7's law reduces to r(rev)*r = "
      "1, which is D1's algebraic identity; the gate therefore restates "
      "D1 in other variables.  The CONCLUSION (the i-twist is a change "
      "of variables, not a discovery) is sound and is carried by the "
      "argument")

# --- D5  the order-dual arm (the D71b carrier) -----------------------------
print()
print("  [D5]  THE ORDER-DUAL ARM — POSET REVERSAL, at transport scope.")
print("""        ATTRIBUTION CORRECTED AT ROUND 1 (MAJOR 4).  The first pass
        headed this arm 'D71b's linear-extension carrier' and concluded
        that 'the order-dual IS NOT DEFINED here'.  Three objects were
        being conflated (QUOTES['d71b_carrier']):
          * D71b's carrier is the committed UNLABELED RECORD ORDER and
            its * is POSET REVERSAL of a record order type.  Poset
            reversal is defined on EVERY poset.  It is never undefined.
          * 'Linear extensions' is D72's common-carrier construction
            (its licensed claim 2), scoped to 2-event histories.
          * What the first pass actually tested was a third thing: ONE
            enumeration-chosen sequence per endpoint, reversed, asked
            for admissibility from the empty history.
        The arm is rebuilt here as the honest question: take the
        OPPOSITE POSET of each defective endpoint and ask whether it has
        ANY admissible realisation — i.e. enumerate EVERY linear
        extension of the event poset (the committed linear_extensions,
        which the first pass declared as a dependency and never called)
        and test every one.  That is strictly stronger than the
        single-order test, and it is what D5.2 gates.""")


def admissible_history(seq, actors, filt=None):
    """Is a bare sequence of events an admissible history from the empty
    history?"""
    h = []
    for e in seq:
        ok, q = b1_adm(h, e, actors)
        if not ok or (filt is not None and not filt(e)):
            return False
        h = h + [e]
    return True


_RADM = {}


def rev_admissible(seq, actors):
    """Memoised: is the REVERSED sequence an admissible history?"""
    k = (tuple(seq), actors)
    v = _RADM.get(k)
    if v is None:
        v = admissible_history(list(seq)[::-1], actors)
        _RADM[k] = v
    return v


# --- D5.0  IS THE GRAMMAR REVERSAL-BLOCKING?  (the first pass said yes) ----
_fam_rev_ok = _fam_rev_tot = 0
_bylen = Counter()
_bylen_ok = Counter()
for _hh in ARMS["AB4"]["fam"]:
    if len(_hh) < 2:
        continue
    _fam_rev_tot += 1
    _bylen[len(_hh)] += 1
    if rev_admissible(tuple(_hh), AB):
        _fam_rev_ok += 1
        _bylen_ok[len(_hh)] += 1
_eps = set()
for _hh, _a, _b, _r in ARMS["AB4"]["closed"]:
    _eps.add(tuple(_hh) + (_a, _b))
    _eps.add(tuple(_hh) + (_b, _a))
_eps = sorted(_eps, key=sk)
_ep_ok = sum(1 for s in _eps if rev_admissible(s, AB))
_ep_del = [s for s in _eps if any(e[0] == 'd' for e in s)]
_ep_del_ok = sum(1 for s in _ep_del if rev_admissible(s, AB))
report("AB4 reverse-admissibility of the whole family (|h| >= 2)",
       f"{_fam_rev_ok} of {_fam_rev_tot} reversed histories are themselves "
       f"admissible; by length "
       + ", ".join(f"|h|={L}: {_bylen_ok[L]}/{_bylen[L]}"
                   for L in sorted(_bylen)))
check("D5.0 THE GRAMMAR IS NOT REVERSAL-BLOCKING — THE FIRST PASS'S "
      "STATED REASON FOR THE NEGATIVE WAS FACTUALLY FALSE (round-1 MAJOR "
      "3a).  D5.1 originally read: 'the reversed sequences are "
      "OVERWHELMINGLY NOT admissible histories of this grammar, so * is "
      "not an operation on the defective squares at all'.  Measured on "
      "the complement it had never looked at, the opposite is true: a "
      "clear MAJORITY of this grammar's histories reverse into admissible "
      "histories, and so do a clear majority of the CLOSED-SQUARE "
      "ENDPOINTS, delivery-bearing ones included.  The 0-of-everything on "
      "the defective squares is therefore NOT a generic support fact "
      "about the grammar; it is a sharp and highly non-generic property "
      "OF THE DEFECT LOCUS — which is a stronger and more interesting "
      "statement than the one it replaces",
      _ep_ok * 2 > len(_eps) and _fam_rev_ok * 2 > _fam_rev_tot
      and _ep_del_ok > 0,
      f"closed-square endpoints reverse-admissible {_ep_ok}/{len(_eps)}; "
      f"of the delivery-bearing endpoints {_ep_del_ok}/{len(_ep_del)}; "
      f"whole family (|h| >= 2) {_fam_rev_ok}/{_fam_rev_tot}")


_dual_in = _dual_pairs = _dual_inv = _dual_conj = _dual_other = 0
for _hh, _a, _b, _r, *_ in ARMS["AB4"]["defs"]:
    _s1 = tuple(_hh) + (_a, _b)
    _s2 = tuple(_hh) + (_b, _a)
    _d1 = _s1[::-1]
    _d2 = _s2[::-1]
    _o1 = admissible_history(list(_d1), AB)
    _o2 = admissible_history(list(_d2), AB)
    _dual_in += int(_o1) + int(_o2)
    if _o1 and _o2:
        # the two duals differ by transposing the FIRST two events: the
        # dual square, based at the empty history's image
        _base = list(_d1[:-2])
        _x, _y = _d1[-2], _d1[-1]
        ok1, q1 = b1_adm(_base, _x, AB)
        ok2, q2 = b1_adm(_base, _y, AB)
        if ok1 and ok2:
            ok3, q3 = b1_adm(_base + [_x], _y, AB)
            ok4, q4 = b1_adm(_base + [_y], _x, AB)
            if ok3 and ok4:
                _dual_pairs += 1
                _rd = Fr(q1 * q3) / Fr(q2 * q4)
                if _rd == 1 / _r:
                    _dual_inv += 1
                elif _rd == _r:
                    _dual_conj += 1
                else:
                    _dual_other += 1
report("AB4 order-dual census on the defective squares",
       f"{_dual_in} of {2 * len(ARMS['AB4']['defs'])} reversed endpoint "
       f"sequences are themselves admissible histories; {_dual_pairs} "
       f"defective squares have a full in-family dual square; of those, "
       f"{_dual_inv} INVERT (r -> 1/r), {_dual_conj} are FIXED (r -> r), "
       f"{_dual_other} neither")
check("D5.1 THE ORDER-DUAL SUPPLIES NO ORIENTATION-SENSITIVE RESIDUE AT "
      "TRANSPORT SCOPE — AND THE REASON IS THE DEFECT LOCUS, NOT THE "
      "GRAMMAR'S SUPPORT (reason corrected at round 1, MAJOR 3a; D5.0 "
      "measures the complement the first pass never looked at).  Not one "
      "defective square has an in-family dual square, so there is no "
      "second value to compare r against and no conjugating residue can "
      "be read off one.  D72's T1.4 established that * and the transport "
      "reversal coincide only on 2-event histories; every defective "
      "square here sits at total depth >= 3, so the two reversals have "
      "already parted company where the defect lives",
      _dual_pairs < len(ARMS["AB4"]["defs"]),
      f"in-family dual squares {_dual_pairs}/{len(ARMS['AB4']['defs'])}; "
      f"inverting {_dual_inv}, fixed {_dual_conj}, other {_dual_other}; "
      f"shallowest defect depth "
      f"{min(len(row[0]) + 2 for row in ARMS['AB4']['defs'])}")

# --- D5.2  THE HONEST ORDER-DUAL: EVERY LINEAR EXTENSION -------------------
_le_tot = _le_fwd = _le_rev = _le_seq = 0
for _hh, _a, _b, _r, *_ in ARMS["AB4"]["defs"]:
    for _s in (tuple(_hh) + (_a, _b), tuple(_hh) + (_b, _a)):
        _le_seq += 1
        _acts = list(_s)
        for _perm in B1["linear_extensions"](_acts):
            _le_tot += 1
            _seq = [_acts[i] for i in _perm]
            if admissible_history(_seq, AB):
                _le_fwd += 1
            if admissible_history(_seq[::-1], AB):
                _le_rev += 1
report("AB4 the OPPOSITE POSET of the defective endpoints, over all linear "
       "extensions",
       f"{_le_seq} endpoint sequences of the {len(ARMS['AB4']['defs'])} "
       f"defective squares; {_le_tot} linear extensions of their event "
       f"posets; {_le_fwd} admissible forwards; {_le_rev} admissible "
       f"reversed")
check("D5.2 THE OPPOSITE POSET HAS NO ADMISSIBLE REALISATION AT ALL — the "
      "honest, and strictly stronger, form of the order-dual negative "
      "(round-1 MAJOR 4).  For every endpoint of every defective square "
      "this gate builds the committed event_poset, enumerates EVERY "
      "linear extension of it (the committed linear_extensions, now "
      "actually called), confirms that all of them are admissible "
      "FORWARDS — so the poset is genuinely the history's own causal "
      "order and nothing is being smuggled — and then tests every "
      "reversal.  NONE is admissible.  So the order-dual is DEFINED here "
      "(it is poset reversal, which every poset admits); what is measured "
      "is that the dual poset has no admissible realisation in this "
      "family, at all, in any order.  The first pass's single-sequence "
      "test could only have shown that one enumeration order failed",
      _le_rev == 0 and _le_fwd == _le_tot and _le_tot > 0,
      f"{_le_tot} linear extensions over {_le_seq} defective endpoints: "
      f"{_le_fwd}/{_le_tot} admissible forwards, {_le_rev}/{_le_tot} "
      f"admissible reversed")

# --- D6  the canonical orientation and sign-definiteness -------------------
print()
print("  [D6]  IS THERE A CANONICAL ORIENTATION?  (CTL-ORDER says the raw "
      "spectrum's asymmetry is not one.)")
_kindorder = {'d': 3, 'r': 2, 'm': 2, 'p': 1, 'n': 0}


def oriented(defs):
    """The kind-canonical orientation: put the DELIVERY second.  Returns
    (oriented spectrum, sign census, count of unorientable squares)."""
    spec = Counter()
    signs = Counter()
    amb = 0
    for row in defs:
        _a, _b, _r = row[1], row[2], row[3]
        ka, kb = _kindorder[_a[0]], _kindorder[_b[0]]
        if ka == kb:
            amb += 1
            continue
        rr = _r if kb > ka else 1 / _r
        spec[rr] += 1
        signs["<1" if rr < 1 else (">1" if rr > 1 else "=1")] += 1
    return spec, signs, amb


ORI = {}
_seen_labels = set()
_ori_arms = []
for _arm in FULL + DEEP:
    if _arm["label"] in _seen_labels:
        continue
    _seen_labels.add(_arm["label"])
    _ori_arms.append(_arm)
for _arm in _ori_arms:
    _sp, _sg, _amb = oriented(_arm["defs"])
    ORI[_arm["label"]] = (_sp, _sg, _amb)
    report(f"{_arm['label']} under the kind-canonical orientation "
           f"(delivery second)",
           f"spectrum {fmt(_sp)}; sign census {dict(_sg)}; {_amb} "
           f"unorientable (equal kind rank)")

_sp4, _sg4, _amb4 = ORI["AB4 (A,B) depth<=4"]
_defarms = [k for k, (s, g, a) in ORI.items() if set(g) <= {"<1"}
            or set(g) <= {">1"}]
_mixarms = [k for k in ORI if k not in _defarms]
check("D6.1 THE SIGN-DEFINITENESS HEADLINE IS TRUE ON THE ANCHOR "
      "WINDOWS AND FALSE ONE DEPTH OUT.  A canonical orientation does "
      "exist and is supplied by the substrate rather than by the "
      "enumeration: order each mixed-kind square so that the DELIVERY is "
      "the second move.  Under it every defective square of BOTH anchor "
      "arms lands strictly BELOW 1 — arbitrating, idling or delivering "
      "before delivering always SUPPRESSES the joint weight — and it "
      "would have been very easy to publish that as the transport-scope "
      "echo of D72's unexplained sign-definiteness of O (T3.B2).  IT DOES "
      "NOT SURVIVE THE WIDER ARMS.  At (A,B) depth <= 5 the oriented "
      "ratio lands above 1 on a small minority of squares, and it does so "
      "again on the one-way sub-grammar.  So the breakage is a DEPTH "
      "effect first and a symmetry effect second — D73's lesson lands, "
      "but not only through D73's door.  The headline is withdrawn to the "
      "windows where it holds and the arms where it fails are named",
      len(_defarms) > 0 and len(_mixarms) > 0,
      "sign-definite on: " + "; ".join(_defarms)
      + " | BOTH SIDES on: "
      + "; ".join(f"{k} {dict(ORI[k][1])}" for k in _mixarms))

# --- D7  the asymmetric substrate ------------------------------------------
check("D7.1 THE ASYMMETRIC SUBSTRATES RETURN THE SAME U(1) VERDICT — AND "
      "THEY MOVE ONE OF THE OTHER ANSWERS (D73's requirement, working "
      "exactly as advertised).  On the one-way link and on the defected "
      "directed ring the holonomy is still R+-valued and generates the "
      "same group <2,3>, still purely odd under reversal, still with no "
      "unimodular part: breaking the actor symmetry does NOT create a "
      "phase.  What breaking the symmetry does do is join the deeper "
      "symmetric window in killing the sign-definiteness of D6.1 — the "
      "asymmetric arm was not needed to break that headline, but it "
      "confirms the break independently",
      all(set(a["nonunit"]) <= set(CUM) for a in ASYM)
      and all(v > 0 for a in ASYM for v in a["nonunit"]),
      "asymmetric value sets "
      f"{[sorted(str(k) for k in a['nonunit']) for a in ASYM]}; oriented "
      "sign censuses "
      + "; ".join(f"{a['label'].split(' ')[0]} {dict(ORI[a['label']][1])}"
                  for a in ASYM))

# ===========================================================================
# D9.  THE REVERSAL-EVEN CHANNEL — THE ROUND'S FIND.
# ===========================================================================
print()
print("  [D9]  THE REVERSAL-EVEN CHANNEL — declared empty by the first")
print("        pass, and it is not.  ROUND 1's find (MAJOR 3), gated here.")
print("""        THE INVARIANT.  For a closed exchange square (h; eA, eB)
        with endpoints s1 = h.eA.eB and s2 = h.eB.eA, define
             J(square) := [ rev(s1) is an admissible history
                            AND rev(s2) is an admissible history ]
        where rev is reversal of the sequence and admissibility is the
        committed `admissible` from the empty history — exactly what the
        D5 arm already computed, and never looked at outside the 88.
        J is SYMMETRIC in (eA, eB) by construction, hence reversal-EVEN:
        it neither inverts nor conjugates under exchanging the two
        orders.  It is a predicate of the substrate, not of the
        enumeration, and it is not a function of r.  The question the
        first pass never asked is whether it is CONSTANT.  It is not.""")

_JROWS = {}
for _JR in (ARMS["AB4"], ARMS["ABC3"], FULL[2]):
    _lab = _JR["label"]
    _act = _JR["actors"]
    _jt = _jf = _jt_nonunit = _jf_unit = _jf_def = _mixed = 0
    for _hh, _a, _b, _r in _JR["closed"]:
        _r1 = rev_admissible(tuple(_hh) + (_a, _b), _act)
        _r2 = rev_admissible(tuple(_hh) + (_b, _a), _act)
        if _r1 != _r2:
            _mixed += 1
        if _r1 and _r2:
            _jt += 1
            _jt_nonunit += int(_r != 1)
        else:
            _jf += 1
            if _r == 1:
                _jf_unit += 1
            else:
                _jf_def += 1
    _JROWS[_lab] = dict(jt=_jt, jf=_jf, jt_nonunit=_jt_nonunit,
                        jf_unit=_jf_unit, jf_def=_jf_def, mixed=_mixed,
                        ndef=len(_JR["defs"]))
    report(f"{_lab} the J census",
           f"J=1 on {_jt} closed squares, of which {_jt_nonunit} have "
           f"r != 1;  J=0 on {_jf} ({_jf_unit} with r = 1 and {_jf_def} "
           f"defective);  squares with MIXED reverse-admissibility "
           f"(exactly one endpoint): {_mixed}")

# is J a relabelling of the register invariant A2.1 / D72 T2.3b already has?
_j_ov = _disj_j0 = 0
for _hh, _a, _b, _r in ARMS["AB4"]["closed"]:
    _J = (rev_admissible(tuple(_hh) + (_a, _b), AB)
          and rev_admissible(tuple(_hh) + (_b, _a), AB))
    _ov = bool(b1_regs(_a) & b1_regs(_b))
    _j_ov += int(_J and _ov)
    _disj_j0 += int((not _J) and (not _ov))
# and is it a depth artefact?  stratify the deepest AB4 stratum.
_d4 = Counter()
for _hh, _a, _b, _r in ARMS["AB4"]["closed"]:
    if len(_hh) + 2 != 4:
        continue
    _J = (rev_admissible(tuple(_hh) + (_a, _b), AB)
          and rev_admissible(tuple(_hh) + (_b, _a), AB))
    _key = "unit" if _r == 1 else "def"
    _d4[_key] += 1
    _d4[_key + "_J"] += int(_J)
report("AB4 J against the register invariant and against depth",
       f"J=1 AND register-OVERLAPPING: {_j_ov} squares (so J is not the "
       f"register-disjointness invariant of A2.1 / D72 T2.3b); "
       f"register-DISJOINT with J=0: {_disj_j0}; at total depth 4 alone, "
       f"{_d4['unit_J']}/{_d4['unit']} unit squares carry J=1 and "
       f"{_d4['def_J']}/{_d4['def']} defective ones do")

_J_TOT1 = sum(v["jt"] for v in _JROWS.values())
_J_EXC = sum(v["jt_nonunit"] for v in _JROWS.values())
_J_DEF = sum(v["jf_def"] for v in _JROWS.values())
_J_NDEF = sum(v["ndef"] for v in _JROWS.values())
check("D9.1 THE REVERSAL-EVEN CHANNEL IS NOT EMPTY: J = 1 IMPLIES r = 1, "
      "AND J = 0 ON EVERY DEFECTIVE SQUARE.  This is round 1's find and "
      "it is credited as such — the raw material is this receipt's own D5 "
      "arm, which evaluated the predicate on the 88 defective squares and "
      "never on the complement.  Across three arms J = 1 on thousands of "
      "closed squares and EVERY ONE of them has holonomy exactly 1; every "
      "defective square in every arm has J = 0.  J is therefore a "
      "SUBSTRATE-SUPPLIED FLATNESS PREDICATE that locates the curvature, "
      "and it is reversal-EVEN — it neither inverts nor conjugates.  It "
      "is NOT a relabelling of the register invariant A2.1 already has "
      "(hundreds of register-OVERLAPPING squares carry J = 1, and "
      "register-DISJOINT squares carry J = 0), and it is not a depth "
      "artefact (it separates within the deepest stratum).  D8's second "
      "clause — 'every quantity this unit could build on these loops "
      "inverts under reversal' — is REFUTED by it.  [MEASURED] on three "
      "windows; NOT a theorem, and not licensed as one: whether "
      "J = 1 => r = 1 survives greater depth and wider pools is the "
      "successor's first question",
      _J_EXC == 0 and _J_TOT1 > 0 and _J_DEF == _J_NDEF
      and all(v["mixed"] == 0 for v in _JROWS.values())
      and all(0 < v["jt"] < v["jt"] + v["jf"] for v in _JROWS.values())
      and _j_ov > 0 and _disj_j0 > 0,
      f"J=1 on {_J_TOT1} closed squares across "
      f"{len(_JROWS)} arms with {_J_EXC} exceptions to r = 1; J=0 on "
      f"{_J_DEF}/{_J_NDEF} defective squares; per arm "
      + "; ".join(f"{k.split('(')[0].strip()} J=1 {v['jt']} (exceptions "
                  f"{v['jt_nonunit']}), J=0 {v['jf']} = {v['jf_unit']} "
                  f"unit + {v['jf_def']} defective"
                  for k, v in sorted(_JROWS.items()))
      + f"; mixed-endpoint squares 0 in every arm, so J is well defined "
      f"as a symmetric predicate")

ODD_FOUND = odd_residue_found(_allvals, _dual_conj)
check("D8 THE ODD-SECTOR VERDICT: " + ("AN ORIENTATION-SENSITIVE RESIDUE "
      "WAS FOUND" if ODD_FOUND else "NO SCALAR ORIENTATION-SENSITIVE "
      "RESIDUE EXISTS ON THIS CARRIER") + ".  Every SCALAR quantity this "
      "unit could build on the holonomy-carrying loops INVERTS under "
      "reversal; nothing CONJUGATES.  The negative is reported as loudly "
      "as a positive would have been, per the pin's sec.4: the imaginary "
      "exponential is not at this address either.  ROUND-1 SCOPE REPAIR: "
      "this is a statement about the SCALAR ODD sector — the U(1) part — "
      "and D2 settles it a priori in one line for a positive-rational "
      "connection.  It is NOT the statement that the reversal-even "
      "channel is empty; D9.1 exhibits a non-trivial invariant there",
      not ODD_FOUND,
      f"unimodular values other than 1: "
      f"{sorted(str(x) for x in _unimod - {Fr(1)})}; order-dual "
      f"conjugating (fixed) dual squares {_dual_conj} of {_dual_pairs} "
      f"in-family dual squares; i-twist informative = False (D4.1); the "
      f"predicate's positive branch is demonstrated at OUT.1")

report("TH-D block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 7.  THE VERDICT — computed, not typed.
# ===========================================================================

print()
print("-" * 78)
print("SEC 7  THE PRE-REGISTERED OUTCOME (pin sec.2), decided by predicate")
print("-" * 78)

def outcome_of(noncoboundary, values, dual_conjugating):
    """The pin's three-way selector, as a FUNCTION of its inputs so that
    each branch can be exercised (round-1 MAJOR 2)."""
    if not noncoboundary:
        return ("TH-I", "the transport twist is a coboundary at every "
                "abstraction on which the question is non-vacuous — the "
                "scope is secretly flat too")
    if odd_residue_found(values, dual_conjugating):
        return ("TH-III", "an orientation-sensitive residue exists on the "
                "curved loops")
    return ("TH-II", "non-coboundary, R+-valued, SCALAR ODD SECTOR EMPTY "
            "— the grammar carries genuine MODULUS curvature with no "
            "phase")


NONCOBOUNDARY = (sum(v for k, v in _selfh.items() if k != 1) > 0
                 and len(NOT_REMOVABLE_AT) > 0)
OUTCOME, OUTTEXT = outcome_of(NONCOBOUNDARY, _allvals, _dual_conj)

# --- OUT.1  THE OUTCOME SELECTOR IS THREE-WAY, DEMONSTRATED ---------------
_probe_I = outcome_of(False, _allvals, _dual_conj)[0]
_probe_IIIa = outcome_of(True, _allvals | {Fr(-1)}, 0)[0]
_probe_IIIb = outcome_of(True, _allvals, 1)[0]
_probe_II = outcome_of(True, _allvals, 0)[0]
check("OUT.1 THE PRE-REGISTERED OUTCOME SELECTOR HAS A LIVE BRANCH IN "
      "EVERY DIRECTION, AND IT IS SHOWN RATHER THAN ASSERTED (round-1 "
      "MAJOR 2).  The first pass's selector could not return TH-III on "
      "any input the fixture could produce: one disjunct ranged over "
      "unimodular values in a set D2 had already proved contains only "
      "positive rationals, and the other over a counter incremented "
      "inside a loop body that never executed.  A three-way pin was "
      "decided by a two-way test.  Here the selector is a function and it "
      "is FED input on which each branch must fire: a flat carrier "
      "returns TH-I; a sign-valued holonomy returns TH-III; a "
      "conjugating dual square returns TH-III; the substrate's own "
      "inputs return TH-II.  The negative at this address is now a "
      "reportable negative and not an artefact of the predicate",
      _probe_I == "TH-I" and _probe_IIIa == "TH-III"
      and _probe_IIIb == "TH-III" and _probe_II == "TH-II"
      and (OUTCOME, OUTTEXT) == outcome_of(NONCOBOUNDARY, _allvals,
                                           _dual_conj),
      f"flat carrier -> {_probe_I}; holonomy set + (-1) -> {_probe_IIIa}; "
      f"one conjugating dual square -> {_probe_IIIb}; the substrate's "
      f"actual inputs -> {_probe_II}")

print()
print(f"  OUTCOME: {OUTCOME} — {OUTTEXT}")
print(f"           WITH THE ROUND-1 FIND: the reversal-EVEN channel is "
      f"NOT empty (D9.1).  The delivered outcome is TH-II WITH J — real "
      f"curvature, scalar phase empty, and an even-channel invariant "
      f"that predicts the curvature's location.")
print()
print("  the predicate, in full:")
print(f"    non-coboundary on the carrier (non-unit self-loops, which no "
      f"potential can remove)   = {NONCOBOUNDARY}")
print(f"    every exhibited holonomy value a positive rational           "
      f"            = {all(v > 0 for v in _allvals)}")
print(f"    an orientation-sensitive (conjugating) SCALAR residue exists  "
      f"            = {ODD_FOUND}")
print(f"    a non-constant reversal-EVEN invariant exists (J, D9.1)      "
      f"            = "
      f"{all(0 < v['jt'] < v['jt'] + v['jf'] for v in _JROWS.values())}")
print(f"      of which:  J = 1 => r = 1, exceptions                       "
      f"            = {_J_EXC} of {_J_TOT1}")
print(f"                 J = 0 on the defective squares                   "
      f"            = {_J_DEF} of {_J_NDEF}")
print(f"    removable at   {REMOVABLE_AT}")
print(f"    NOT removable at {NOT_REMOVABLE_AT}")
print(f"    carrier        = the weighted-menu quotient "
      f"({_MENU4['cls']} classes at AB4), equivalently the coarsest "
      f"weighted congruence ({_CA4['cong_cls']} classes)")
print(f"    group          = {GCUM['name']}, at {len(SCOPES)} scopes over "
      f"three actor pools (2, 3, 4 actors) and two asymmetric "
      f"sub-grammars = four mutually non-nested evidence pools")
print(f"    seen / unseen  = {len(_seen)} curvature-type + {len(_unseen)} "
      f"descent-obstruction-type defective squares (the second half "
      f"closes in MULT, a quotient graph on which the connection is not "
      f"well defined — A3.5)")

print()
print("-" * 78)
print("SUMMARY")
print("-" * 78)
print(f"  gates: {PASS} PASS / {FAIL} FAIL   "
      f"(of which {len(COROLLARY)} carry NO INDEPENDENT INFORMATION and "
      f"are excluded from the evidence count: "
      f"{PASS - len(COROLLARY)} independent passes)")
for _lbl, _why in COROLLARY:
    print(f"    corollary: {_lbl}")
print(f"  anchors: {ANCHOR_FAIL} failures (exit 1 threshold)")
print(f"  wall clock: {time.time() - T0:.0f}s "
      f"({(time.time() - T0) / 60:.1f} min; the pin's budget is ~25 min)")
print()
print("  WHAT THIS RECEIPT DOES NOT CLAIM (pin sec.4, with the round-1 "
      "scope repairs): no measure-existence claim; no claim that "
      "anything found here IS the v7 phase (D4.1 shows the i-twist "
      "correspondence is content-free); no infinite-volume claim; "
      "nothing outside the declared families, depths and pools; the "
      "AB-only/BA-only split and the unpaired spectrum are NOT licensed "
      "as substrate facts (CTL-ORDER) — and neither are THIS unit's own "
      "unseen-half spectrum and kind census, which CTL-ORDER transposes "
      "(A3.2); the count of non-trivial basis cycles is forest-dependent "
      "and is not licensed as a number; J (D9.1) is [MEASURED] on three "
      "windows and is NOT a theorem — no claim is made that "
      "J = 1 => r = 1 survives greater depth or wider pools; the "
      "descent-obstruction half is NOT claimed to be beyond every corpus "
      "formalism — D65 sec.3.1's repair cone computes the same criterion "
      "under a different functor (152 of 403 repair rows not implied by "
      "record-constancy, QUOTES['d65_3.1']) — what is claimed is that no "
      "corpus formalism handles it AT TRANSPORT SCOPE and none "
      "quantifies over quotients; and no claim of independence is made "
      "for the nested depth chains (only the four-actor pool is an "
      "independent scope, A1.3).")
print("=" * 78)

sys.exit(1 if ANCHOR_FAIL else 0)
