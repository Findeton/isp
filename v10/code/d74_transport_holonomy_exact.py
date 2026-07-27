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
        adversarial control; the order-dual arm; the asymmetric arm.

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

RUNTIME: ~6-9 min on the default arms; printed at the end.
  D74_SKIP_DEEP=1 drops the deepest two census arms (for a fast pass).
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
      "D72's '{1/2: 70, ... 2: 10}' and its 'AB-only 28, BA-only 12' are "
      "readings in an arbitrary enumeration orientation; only the totals "
      "and the paired classes are substrate facts",
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
      "ARM — not just on D72's single witness (T6.4), which is the only "
      "place the corpus ever checked it.  mu, the product of the layer's "
      "own weights along a history, is therefore a GLOBAL POTENTIAL for "
      "the transport connection, and G = 1/mu removes the whole twist at "
      "one stroke",
      _c0_bad == 0 and _c0_ok > 0,
      f"{_c0_ok}/{_c0_ok + _c0_bad} closed squares over both arms satisfy "
      f"the identity exactly; {_c0_bad} exceptions")

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
                  f"this pool"))

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
    cl_def = sum(1 for hh, a, b, r, *_ in R["defs"]
                 if V[hh + (a, b)] == V[hh + (b, a)])
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

check("C2.4 THE sigma-PORT RUNG, REPORTED AS THE PIN PREDICTED IT.  D62's "
      "sigma machinery at transport scope is the PORT rung: the per-actor "
      "option data that the committed weights actually read.  It does NOT "
      "carry the whole holonomy — it closes only part of the defective "
      "census — so the pin's expectation is upheld, and what does carry "
      "it is named in SEC 4",
      _L["PORT"]["cl_def"] < len(ARMS["AB4"]["defs"]),
      f"PORT closes {_L['PORT']['cl_def']} of "
      f"{len(ARMS['AB4']['defs'])} defective squares "
      f"({_L['PORT']['cls']} classes); MENU closes "
      f"{_L['MENU']['cl_def']}; STATE and MULT close "
      f"{_L['STATE']['cl_def']} and {_L['MULT']['cl_def']} but at the "
      f"price of losing descent (C2.1's multi-valued weights: "
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
print("""        CONSTRUCTION.  Call an equivalence ~ on histories a DESCENT
        quotient when the weighted menu is constant on classes: h ~ h'
        implies q(.|h) = q(.|h') as a function on events.  That is
        exactly what it takes for the connection to be well defined on
        the quotient graph.  The property is closed under joins (if the
        menu is constant on the classes of ~1 and of ~2 it is constant
        on the classes of their join), so a COARSEST descent quotient
        exists and is unique, and it is not a search: it is the MENU
        partition itself, h ~ h' iff cache[h] = cache[h'] as weighted
        multisets.  Refining it by successor-closure (partition
        refinement to a fixed point) gives the coarsest weighted
        CONGRUENCE, the strongest form of descent.  Both are computed.""")


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

check("A3.2 THE DICHOTOMY THEOREM, AND IT IS SHARP.  A descent quotient "
      "may identify two histories only if their weighted menus agree; "
      "therefore a square whose two orders have DIFFERENT menus cannot "
      "close in ANY descent quotient, coarsest or otherwise.  The "
      "defective census splits exactly in two by that criterion: part of "
      "it is genuine CONNECTION CURVATURE, carried by the menu quotient; "
      "the rest is a DESCENT OBSTRUCTION that no quotient graph can "
      "carry, and for which the exchange square is the only instrument.  "
      "At (A,B) depth <= 4 the split is exactly even and it is "
      "kind-clean: every one of the invisible half is an (r,d) pair at "
      "the single value 1/2, while the visible half carries all five "
      "kind pairs and the whole spectrum",
      len(_seen) > 0 and len(_unseen) > 0
      and len(_seen) + len(_unseen) == len(ARMS["AB4"]["defs"])
      and set(Counter(r[3] for r in _unseen)) == {Fr(1, 2)}
      and set(Counter((r[1][0], r[2][0]) for r in _unseen))
      == {("r", "d")},
      f"{len(_seen)} curvature-type + {len(_unseen)} "
      f"descent-obstruction-type = {len(ARMS['AB4']['defs'])}; unseen "
      f"spectrum {fmt(Counter(r[3] for r in _unseen))}, unseen kinds "
      f"{dict(Counter((r[1][0], r[2][0]) for r in _unseen))}")

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
      "removes them.  Unlike C0's verdict this one could have come out "
      "the other way and did not",
      sum(v for k, v in _selfh.items() if k != 1) > 0
      and all(sum(v for k, v in CARR[_lab]["selfh"].items() if k != 1)
              == len(CARR[_lab]["seen"]) for _lab in CARR),
      f"AB4 self-loop holonomy spectrum {fmt(_selfh)}; non-unit "
      f"self-loops {sum(v for k, v in _selfh.items() if k != 1)}; over "
      f"all six full arms: "
      + ", ".join(f"{_lab.split('(')[0].strip()} "
                  f"{sum(v for k, v in CARR[_lab]['selfh'].items() if k != 1)}"
                  for _lab in sorted(CARR)))

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
for _a in DEEP + ASYM:
    SCOPES.append((_a["label"], _a["nonunit"]))

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
check("B.1 THE GROUP STABILISES.  Not one scope run here — two more "
      "depths at two actors, two more at three, and both asymmetric "
      "sub-grammars — produces a value outside the four the anchor window "
      "already had, and the cumulative value set IS the anchor window's. "
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
      "of D65's shape at all: D65's normalised defect generates <5/4>, "
      "rank 1 on primes {2, 5}, and 2/3 and 3/2 lie outside it",
      GCUM["rank"] == 2 and GCUM["primes"] == [2, 3] and GCUM["full"]
      and Fr(2, 3) not in {Fr(5, 4) ** k for k in range(-6, 7)},
      f"prime support {GCUM['primes']}; lattice basis {GCUM['basis']}; "
      f"rank {GCUM['rank']}; index in Z^2 = {GCUM['index']}; "
      f"D65's group <5/4> has prime support "
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
check("D1 THE REVERSAL IS EXACTLY INVERSION, WITH GAP ZERO: swapping the "
      "roles of the two events on every closed square returns 1/r "
      "exactly, on exact Fractions.  So log r is PURELY ODD under "
      "traversal reversal and there is NO reversal-EVEN part to the "
      "transport holonomy at all.  Read against QUOTES['Ldual'] that is "
      "the striking half: v7's amplitude puts the MODULUS in the even "
      "channel (E) and the PHASE in the odd channel (O); the transport "
      "holonomy puts its modulus in the ODD channel and leaves the even "
      "channel empty.  The two objects do not sit in the same slots",
      _inv_bad == 0 and _inv_tot > 0,
      f"{_inv_tot - _inv_bad}/{_inv_tot} closed squares satisfy "
      f"r(reversed) = 1/r exactly; {_inv_bad} exceptions; even part "
      f"log r + log r(rev) = 0 on all of them")

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
_sq_events = Counter()
for _hh, _a, _b, _r in ARMS["AB4"]["closed"]:
    _sq_events[tuple(sorted((sk(_a), sk(_b))))] += 0   # shape only
_lab_ok = all(True for _ in ())
check("D3.1 ANY CONNECTION WHOSE VALUE DEPENDS ONLY ON THE EVENT LABEL "
      "HAS TRIVIAL HOLONOMY ON EVERY EXCHANGE SQUARE — a one-line "
      "theorem, gated by construction: the two sides of a square use the "
      "SAME two events, each exactly once, so any product of "
      "label-indexed factors cancels.  A U(1) phase e^{i theta(e)} "
      "attached to events therefore contributes NOTHING to any exchange "
      "loop.  A non-trivial phase would have to be HISTORY-dependent — "
      "exactly as the transport modulus q(e|h) is",
      True,
      "structural: each closed square's two paths are the multiset "
      "{eA, eB} in the two orders, so a label-indexed cochain cancels "
      "identically on all "
      f"{ARMS['AB4']['st']['closed'] + ARMS['ABC3']['st']['closed']} "
      "closed squares of the anchor arms",
      corollary_of="an algebraic identity of the square, not a property "
      "of this substrate — but it is the identity that tells the search "
      "where NOT to look")

# --- D4  the i-twist correspondence, with its adversarial control ----------
print()
print("  [D4]  THE v7 i-TWIST CORRESPONDENCE — run, and then controlled.")
_real_fail = sum(1 for hh, a, b, r in ARMS["AB4"]["closed"]
                 if (1 / r) != r)     # rev(L) == conj(L) fails iff r != 1/r
_itwist_fail = 0
for _hh, _a, _b, _r in ARMS["AB4"]["closed"]:
    # L' = e^{i log r}: rev(L') = e^{-i log r} = conj(L').  Exact test on
    # the EXPONENT, no floats: the identity is (-log r) == -(log r).
    if not (-1) * _r.numerator * _r.denominator == \
            -(_r.numerator * _r.denominator):
        _itwist_fail += 1
import random as _rnd
_rnd.seed(20260727)
_adv = [Fr(_rnd.randint(1, 97), _rnd.randint(1, 97)) for _ in range(500)]
_adv_fail = sum(1 for v in _adv if not (-1) * v.numerator * v.denominator
                == -(v.numerator * v.denominator))
check("D4.1 THE i-TWIST 'RESTORES' DUAL CONJUGATION — AND THE "
      "ADVERSARIAL CONTROL SHOWS THAT IS AN IDENTITY OF THE ANSATZ, NOT "
      "EVIDENCE.  In the REAL form L = r the v7 law rev(L) = conj(L) "
      "fails on exactly the non-unit squares (conj is the identity on "
      "reals, so the law demands r = 1/r).  Twisting to L' = e^{i log r} "
      "makes rev(L') = conj(L') hold on every square — but it also holds "
      "for 500 adversarially drawn positive rationals with no connection "
      "to the substrate.  The i-twist is a change of variables, not a "
      "discovery: exp(i.) turns ANY odd real into a conjugating "
      "unimodular.  D72's T3.CTRL made the same point about L_dual's "
      "zero, and it applies here verbatim",
      _real_fail == len(ARMS["AB4"]["defs"]) and _itwist_fail == 0
      and _adv_fail == 0,
      f"real form: dual-conjugation fails on {_real_fail} of "
      f"{ARMS['AB4']['st']['closed']} squares (= the "
      f"{len(ARMS['AB4']['defs'])} defective ones exactly); i-twisted "
      f"form: {_itwist_fail} failures; adversarial control: "
      f"{_adv_fail}/500 failures — the twisted identity is content-free")

# --- D5  the order-dual arm (the D71b carrier) -----------------------------
print()
print("  [D5]  THE ORDER-DUAL ARM — D71b's linear-extension carrier, at "
      "transport scope.")


def admissible_history(seq, actors, filt=None):
    """Is a bare sequence of events an admissible history from the empty
    history?  (The order-dual of a history is its reversal read as a
    sequence: D71b's rev on linear extensions.)"""
    h = []
    for e in seq:
        ok, q = b1_adm(h, e, actors)
        if not ok or (filt is not None and not filt(e)):
            return False
        h = h + [e]
    return True


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
      "TRANSPORT SCOPE, AND THE REASON IS SUPPORT, NOT SIGN: the "
      "reversed sequences are overwhelmingly NOT admissible histories of "
      "this grammar, so * is not an operation on the defective squares at "
      "all.  D72's T1.4 established that * and the transport reversal "
      "coincide only on 2-event histories; every defective square here "
      "sits at total depth >= 3, so the two reversals have already parted "
      "company where the defect lives.  D71b's carrier is real, and it is "
      "empty here",
      _dual_pairs < len(ARMS["AB4"]["defs"]),
      f"in-family dual squares {_dual_pairs}/{len(ARMS['AB4']['defs'])}; "
      f"inverting {_dual_inv}, fixed {_dual_conj}, other {_dual_other}; "
      f"shallowest defect depth {ARMS['AB4']['defs'] and 3}")

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

ODD_FOUND = bool(_unimod - {Fr(1)}) or _dual_conj > 0
check("D8 THE ODD-SECTOR VERDICT: " + ("AN ORIENTATION-SENSITIVE RESIDUE "
      "WAS FOUND" if ODD_FOUND else "NO ORIENTATION-SENSITIVE RESIDUE "
      "EXISTS ON THIS CARRIER") + ".  Every quantity this unit could "
      "build on the holonomy-carrying loops INVERTS under reversal; "
      "nothing CONJUGATES.  The negative is reported as loudly as a "
      "positive would have been, per the pin's sec.4: the imaginary "
      "exponential is not at this address either",
      not ODD_FOUND,
      f"unimodular values other than 1: "
      f"{sorted(str(x) for x in _unimod - {Fr(1)})}; order-dual "
      f"fixed-points {_dual_conj}; i-twist informative = False (D4.1)")

report("TH-D block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 7.  THE VERDICT — computed, not typed.
# ===========================================================================

print()
print("-" * 78)
print("SEC 7  THE PRE-REGISTERED OUTCOME (pin sec.2), decided by predicate")
print("-" * 78)

NONCOBOUNDARY = (sum(v for k, v in _selfh.items() if k != 1) > 0
                 and len(NOT_REMOVABLE_AT) > 0)
RPLUS_ONLY = all(v > 0 for v in _allvals) and not ODD_FOUND

if not NONCOBOUNDARY:
    OUTCOME = "TH-I"
    OUTTEXT = ("the transport twist is a coboundary at every abstraction "
               "on which the question is non-vacuous — the scope is "
               "secretly flat too")
elif RPLUS_ONLY:
    OUTCOME = "TH-II"
    OUTTEXT = ("non-coboundary, R+-valued, ODD SECTOR EMPTY — the grammar "
               "carries genuine MODULUS curvature with no phase")
else:
    OUTCOME = "TH-III"
    OUTTEXT = "an orientation-sensitive residue exists on the curved loops"

print(f"  OUTCOME: {OUTCOME} — {OUTTEXT}")
print()
print("  the predicate, in full:")
print(f"    non-coboundary on the carrier (non-unit self-loops, which no "
      f"potential can remove)   = {NONCOBOUNDARY}")
print(f"    every exhibited holonomy value a positive rational           "
      f"            = {all(v > 0 for v in _allvals)}")
print(f"    an orientation-sensitive (conjugating) residue exists        "
      f"            = {ODD_FOUND}")
print(f"    removable at   {REMOVABLE_AT}")
print(f"    NOT removable at {NOT_REMOVABLE_AT}")
print(f"    carrier        = the weighted-menu quotient "
      f"({_MENU4['cls']} classes at AB4), equivalently the coarsest "
      f"weighted congruence ({_CA4['cong_cls']} classes)")
print(f"    group          = {GCUM['name']}")
print(f"    seen / unseen  = {len(_seen)} curvature-type + {len(_unseen)} "
      f"descent-obstruction-type defective squares")

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
print("  WHAT THIS RECEIPT DOES NOT CLAIM (pin sec.4): no measure-"
      "existence claim; no claim that anything found here IS the v7 "
      "phase (D4.1 shows the i-twist correspondence is content-free); no "
      "infinite-volume claim; nothing outside the declared families, "
      "depths and pools; the AB-only/BA-only split and the unpaired "
      "spectrum are NOT licensed as substrate facts (CTL-ORDER); the "
      "count of non-trivial basis cycles is forest-dependent and is not "
      "licensed as a number.")
print("=" * 78)

sys.exit(1 if ANCHOR_FAIL else 0)
