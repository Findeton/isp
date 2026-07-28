#!/usr/bin/env python3
"""
ld_reversal_probe_exact.py — v11 LD, THE LAST DOOR: the record-category
reversal probe.

Pin: v11/note-ld-last-door-pin.md (STRICT, binding).  Binding
specification: paper 0 sec.9b (the last door), the catalog [V11-CAT]
sec.4.7 branch (a).  Parents: v10 D74 TERMINAL (the transport holonomy
is R+, group <2,3>, odd sector empty on the tested carrier — the
0-for-5 record), D72 TERMINAL (the transport-scope census this receipt
ANCHORS on), D71b (the order-dual carrier), D73 (carry an asymmetric
substrate).

THE QUESTION.  Every v10 phase search decomposed structures under
reversal ON THE RECORD AS BUILT.  This unit reverses the RECORD
CATEGORY itself: it constructs the formal opposite of the record's
causal order, with the event-kind relabelling that reversal forces, and
asks whether the generated quantities — transport weights, holonomy
values, the Born = K1 arbitration row — transform under record-reversal
by INVERSION in R+ (classical), by CONJUGATION-like pairing (the U(1)
signature), or by NEITHER.

THE FOUR ARMS (pin sec."The unit"):
  LD-A  the reversal functor on the committed transport layer: the
        formal opposite of the record's causal order, with the forced
        event-kind relabelling.  The relabelling table is printed.
        Involutivity is GATED: reversing twice restores the original
        record exactly, on every record of every arm.
  LD-B  the census: for every holonomy-carrying loop of D74's committed
        census (88 non-unit + 40 half-open at (A,B) d<=4; 12 at
        (A,B,C) d<=3, all re-anchored first) and for the Born = K1
        arbitration row, the reversed-record counterpart EXACTLY, each
        pair (v, v_rev) classified INVERSION / INVARIANT / OTHER /
        UNDEFINED, printed BOTH WAYS.
  LD-C  the verdict against the pin's pre-registered outcomes, and —
        where the functor fails to land in the committed grammar — the
        obstruction characterized exactly.
  LD-D  the same census on the defected/asymmetric schedule families
        (D73's lesson), with the MIRROR sub-grammar as the honest
        opposite of a directed schedule.

DECLARED CAPS (printed at the end).  Arms: (A,B) d<=4 and (A,B,C) d<=3
(the two anchor windows), ASYM-1 (A,B) d<=5 one-way A->B, ASYM-2
(A,B,C) d<=4 directed ring A->B->C->A.  The all-linear-extensions
control runs on the anchor arms' holonomy-carrying loops only.  The
non-empty-prefix control runs on the anchor arms against every
admissible prefix of length <= 2.  Transport scope, committed families
only.

SCOPE.  The reversal is FORMAL (category-level).  No claim is made that
reversed records are physically generated; no thermodynamic language is
used anywhere in this receipt.  Weight-system level only.

HOUSE RULES OBSERVED
  * Exact arithmetic (fractions.Fraction) end to end.  No floats
    anywhere except the wall-clock timings.
  * The committed d42b1 layer is single-sourced by TEXT-SLICE of its own
    source, with an AST signature pass and exit-freedom gated.
  * Every number a gate tests against is either a QUOTED committed value
    (registry QUOTES/ANCH, with path:line provenance) or a quantity
    derived inside this receipt.
  * Every census printed BOTH WAYS.
  * Substantive negatives exit 0.  exit 1 is reserved for ANCHOR failure
    — a committed D72/D74 number that does not reproduce.
  * Determinism: all iteration that feeds a printed number is ordered by
    sk() (hash-seed independent), and a determinism probe is run.
  * Runtime printed.
"""

from __future__ import annotations

import ast
import os
import sys
import time
import types
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from itertools import permutations

T0 = time.time()
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO)          # .../isp  (run from anywhere)
os.chdir(REPO)

PASS = FAIL = 0
ANCHOR_FAIL = 0
COROLLARY = []


def check(label, ok, detail="", corollary_of=None):
    """corollary_of: the gate is entailed by another gate or is true of
    every object of its type.  Run and printed but NOT counted as
    independent evidence (the D72 MODERATE-4 discipline, carried)."""
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
    objects (D72's stable_key, re-derived here as D74 re-derives it)."""
    if isinstance(o, (frozenset, set)):
        return ("S", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, (tuple, list)):
        return ("T", tuple(sk(x) for x in o))
    return ("V", type(o).__name__ + "|" + repr(o))


_EVSK = {}


def evsk(e):
    v = _EVSK.get(e)
    if v is None:
        v = sk(e)
        _EVSK[e] = v
    return v


def fmt(counter):
    return {str(k): v for k, v in sorted(counter.items(),
                                         key=lambda z: sk(z[0]))}


def fmtk(counter):
    return {str(k): v for k, v in sorted(counter.items(),
                                         key=lambda z: str(z[0]))}


# ===========================================================================
# SEC 0.  THE REGISTRY — every constant a gate tests against, with provenance
# ===========================================================================

QUOTES = {
    "T6.1": (
        "v10/note-d72-weld-result.md:150 (sec.1 T6.1), quoted verbatim by "
        "v10/code/d74_transport_holonomy_exact.py:163-170 as QUOTES['T6.1']",
        "(A,B) d <= 4: 88 of 1,546 closed squares non-unit, spectrum "
        "{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}, kinds {(r,d): 68, (d,r): 8, "
        "(d,n): 6, (d,d): 4, (n,d): 2}, delivery-bearing 88/88, "
        "shallowest defect at total depth 3.  (A,B,C) d <= 3: 12 of "
        "1,554, spectrum {1/2: 12}, kinds {(r,d): 12}.",
    ),
    "T6.2": (
        "v10/note-d72-weld-result.md:151 (sec.1 T6.2), quoted by "
        "d74 as QUOTES['T6.2']",
        "(A,B) d <= 4: 40 half-open (AB-only 28, BA-only 12), kinds "
        "{(r,d): 12, (d,r): 4, (p,d): 16, (d,p): 8}, 40/40 "
        "delivery-bearing.",
    ),
    "T6.4": (
        "v10/data/d72_weld_exact.out:127-135, quoted by d74 as "
        "QUOTES['T6.4']",
        "the minimal witness: h = [('p','A',V0,0)], eA = arb of own "
        "proposal, eB = ('d','A','B',V0); q(eA|h) = 1/4, q(eB|h.eA) = "
        "1/8, q(eB|h) = 1/4, q(eA|h.eB) = 1/4; dP_AB/dP_BA = 1/2; "
        "mu(h.eA.eB) = 1/256 vs mu(h.eB.eA) = 1/128.",
    ),
    "T2.5": (
        "v10/data/d72_weld_exact.out:119-121, 137-139, quoted by d74 as "
        "QUOTES['T2.5']",
        "(A,B) d<=4: 3969 histories, 2477 record classes, 2900 up-edges; "
        "(A,B,C) d<=3: 3424 histories, 2128 record classes, 2772 "
        "up-edges.",
    ),
    "d74_group": (
        "v10/note-d74-transport-holonomy-result.md:1, :97-98, :227 "
        "(gate B.2 of v10/code/d74_transport_holonomy_exact.py:1918)",
        "the transport holonomy group is <2,3>, free abelian of rank 2, "
        "the FULL group of 3-smooth positive rationals, index 1 in Z^2; "
        "value set {1/2, 2/3, 3/2, 2} at every scope run.",
    ),
    "d74_D5.2": (
        "v10/code/d74_transport_holonomy_exact.py:2313-2325 (gate D5.2) "
        "and v10/note-d74-transport-holonomy-result.md",
        "the opposite poset of every defective-square endpoint has NO "
        "admissible realisation at all: every linear extension is "
        "admissible forwards, none reversed.  Measured WITHOUT any "
        "event-kind relabelling.",
    ),
    "d74_D5.0": (
        "v10/code/d74_transport_holonomy_exact.py:2224-2246 (gate D5.0)",
        "the grammar is NOT reversal-blocking: a clear majority of "
        "histories, and of closed-square endpoints, reverse into "
        "admissible histories.  The 0-of-everything on the defective "
        "squares is a non-generic property OF THE DEFECT LOCUS.",
    ),
    "d74_D1": (
        "v10/code/d74_transport_holonomy_exact.py:2006-2030 (gate D1)",
        "TRAVERSAL reversal acts on r by inversion — an algebraic "
        "identity of the definition of r, not a measurement.  This unit "
        "reverses the RECORD CATEGORY, which is a different operation "
        "and has no such identity available to it.",
    ),
    "p31_born": (
        "v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md"
        ":507-517 (sec.4.3)",
        "Born = the committed kernel: the squared branch amplitudes of "
        "V_pair are exactly 1/2-1/2 (the K1 law on the 2-conflict, "
        "recomputed from the layer); menu reconstruction at both cuts, "
        "exact in rationals — 1/4 on the arbitration sector at the early "
        "cut.",
    ),
    "d73": (
        "v10/note-d73-even-gram-result.md sec.12 (the generic-geometry "
        "lesson), quoted by d74 as QUOTES['d73']",
        "hand-built symmetry is a cage: carry at least one "
        "asymmetric/defected substrate.",
    ),
    "d74_asym": (
        "v10/code/d74_transport_holonomy_exact.py:1406-1420 (oneway, "
        "ring)",
        "ASYM-1: the link A->B only, so B may never deliver to A.  "
        "ASYM-2: the defected directed ring A->B->C->A.  Declared "
        "SUB-GRAMMARS: the support is restricted, the committed weights "
        "are untouched.",
    ),
}

# --- committed NUMERIC anchors, transcribed from the sources above ---------
ANCH = {
    "AB_hist": 3969,
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
    "ABC_hist": 3424,
    "ABC_closed": 1554,
    "ABC_defects": 12,
    "ABC_full_ratios": {Fr(1, 2): 12, Fr(1): 1542},
    "ABC_kinds": {("r", "d"): 12},
    "ABC_bothblocked": 42,
    "ABC_halfopen": 0,
    "wit_qA": Fr(1, 4), "wit_qB2": Fr(1, 8),
    "wit_qB": Fr(1, 4), "wit_qA2": Fr(1, 4),
    "wit_r": Fr(1, 2),
    "wit_muAB": Fr(1, 256), "wit_muBA": Fr(1, 128),
    "group_primes": [2, 3],
    "group_rank": 2,
    "group_index": 1,
    "group_valueset": {Fr(1, 2), Fr(2, 3), Fr(3, 2), Fr(2)},
    "born_K1": {Fr(1, 2): 2},
    "born_sector": Fr(1, 4),
}

print("=" * 78)
print("LD — THE LAST DOOR: the record-category reversal probe  (exact)")
print("=" * 78)
print("  banner: exact Fractions throughout; the committed d42b1 layer")
print("  single-sourced by text-slice + an AST signature pass, with")
print("  exit-freedom gated; every tested constant quoted from a committed")
print("  source (registry below); every census printed BOTH WAYS;")
print("  substantive negatives exit 0; exit 1 ONLY if a committed")
print("  D72/D74 number fails to reproduce.")
print()
print("  SCOPE: the reversal is FORMAL (category-level).  No claim is made")
print("  that reversed records are physically generated.  No thermodynamic")
print("  language appears in this receipt.  Transport scope, committed")
print("  families only, weight-system level.")
print()
print(f"  PYTHONHASHSEED = {os.environ.get('PYTHONHASHSEED', '(unset)')}")
print()
print("  QUOTE REGISTRY (the anchors below are held to these):")
for k, (where, text) in QUOTES.items():
    print(f"    [{k}] {where}")
    for i in range(0, len(text), 68):
        print(f"        {text[i:i + 68]}")


# ===========================================================================
# SEC 0.1  SINGLE-SOURCING: AST signature pass, then text-slice.
# ===========================================================================

class _NoExit(Exception):
    pass


def ast_signatures(path, required):
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
print("SEC 0.1  the committed source: AST signature pass, then slice")
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
    "arb_components_in_view": ["view", "a"],
    "edge_triples_of": ["view", "idx_set"],
    "triples": ["view", "idx_set"],
    "mis_of": ["ckey", "edge_triples"],
    "PK1": ["ckey", "edge_triples"],
    "linear_extensions": ["acts"],
    "value_of": ["v"],
    "base_of": ["v"],
    "View": ["<class>"],
}

_sig1, _miss1 = ast_signatures("v10/code/d42b1_transport_exact.py", B1_REQ)
if _miss1:
    print("!" * 78)
    print(f"AST SIGNATURE FAILURE: d42b1 {_miss1}")
    print("!" * 78)
    sys.exit(1)
report("d42b1 AST", f"{len(_sig1)} module-level defs/classes; all "
       f"{len(B1_REQ)} required signatures matched exactly")

B1, _b1n, _b1t = slice_exec("v10/code/d42b1_transport_exact.py",
                            'print("[d42b1', "ld_d42b1")
report("d42b1 slice", f"{_b1n}/{_b1t} bytes executed (definition head "
       "only); exit-freedom gated")

b1_cand = B1["candidates_for"]
b1_adm = B1["admissible"]
b1_canon = B1["canon"]
b1_regs = B1["regs_of"]
b1_ep = B1["event_poset"]
b1_linext = B1["linear_extensions"]
b1_View = B1["View"]
b1_triples = B1["triples"]
b1_arbcomps = B1["arb_components_in_view"]
b1_edgetri = B1["edge_triples_of"]
b1_mis = B1["mis_of"]
b1_PK1 = B1["PK1"]
V0 = B1["V0"]

_exitfree = False
try:
    slice_exec("v10/code/d42b1_transport_exact.py", 'print("[d42b1',
               "ld_probe")
    _exitfree = True
except _NoExit:
    _exitfree = False
check("SRC.1 EXIT-FREEDOM GATED: the sliced layer cannot set this "
      "receipt's exit status — sys.exit/os._exit are neutralised inside "
      "the slice and restored after; the slice re-executes cleanly",
      _exitfree,
      "second slice of d42b1 executed with exit blocked and raised "
      "nothing",
      corollary_of="a property of the loader, not of the substrate; it "
      "tests our plumbing")


# ===========================================================================
# SEC 0.2  THE MACHINERY — D72's census, re-derived here (as D74 re-derives
#          it) so that its numbers must reproduce.
# ===========================================================================

def enumerate_line(cands, actors, depth, filt=None):
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


def square_census(fam, cache, actors, dep, filt=None):
    """The exchange-square census (D72's transport_square_census, as D74
    carries it).  Returns (status counter, ratio counter, kinds,
    open-kinds, defects, half-open list, all-closed list)."""
    st = Counter()
    rat = Counter()
    kinds = Counter()
    open_kinds = Counter()
    defects = []
    half = []
    closed = []

    def W(h, e):
        ok, q = b1_adm(h, e, actors)
        if ok and filt is not None and not filt(e):
            return False, None
        return ok, q

    for h in fam:
        if len(h) + 2 > dep:
            continue
        cands = [e for e, q in cache[tuple(h)]]
        for i in range(len(cands)):
            for j in range(i + 1, len(cands)):
                eA, eB = cands[i], cands[j]
                okA, qA = W(h, eA)
                okB, qB = W(h, eB)
                if not (okA and okB):
                    continue
                okB2, qB2 = W(h + [eA], eB)
                okA2, qA2 = W(h + [eB], eA)
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


def mu_of_sequence(seq, actors, filt=None):
    """The committed measure of a bare event sequence read as a history
    from the empty record: the product of the committed conditional
    weights, or None if the sequence is not an admissible history of the
    (possibly restricted) grammar.  All weights are positive rationals,
    so a returned value is never zero."""
    h = []
    m = Fr(1)
    for e in seq:
        if filt is not None and not filt(e):
            return None
        ok, q = b1_adm(h, e, actors)
        if not ok:
            return None
        m *= Fr(q)
        h = h + [e]
    return m


def first_blocker(seq, actors, filt=None):
    """(index, event, reason) of the first event of `seq` that the
    committed admission relation refuses, or (None, None, None)."""
    h = []
    for i, e in enumerate(seq):
        if filt is not None and not filt(e):
            return i, e, "outside the declared sub-grammar's support"
        ok, q = b1_adm(h, e, actors)
        if not ok:
            return i, e, "refused by the committed admission relation"
        h = h + [e]
    return None, None, None


def primes_of(fr):
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
    """The multiplicative subgroup of Q+ generated by `values`: prime
    support, an integer basis of its exponent lattice, rank, and the
    lattice index in Z^k.  (D74's group_of, re-derived.)"""
    vals = [v for v in values if v != 1]
    if not vals:
        return {"primes": [], "rank": 0, "basis": [], "index": 1,
                "name": "{1} (trivial)"}
    ps = sorted({p for v in vals for p in primes_of(v)})
    vecs = []
    for v in vals:
        f = primes_of(v)
        vecs.append([f.get(p, 0) for p in ps])
    B = lattice_basis(vecs)
    rank = len(B)
    idx = None
    if rank == len(ps) and rank > 0:
        M = [[Fr(x) for x in row] for row in B]
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
            inv = Fr(1) / M[i][i]
            for r in range(i + 1, n):
                f = M[r][i] * inv
                M[r] = [a - f * b for a, b in zip(M[r], M[i])]
        idx = abs(det)
    if idx == 1:
        nm = ("<" + ", ".join(str(p) for p in ps) + "> = the FULL group of "
              + "-".join(str(p) for p in ps) + "-smooth positive rationals"
              + f" (free abelian of rank {rank}, index 1 in Z^{rank})")
    else:
        nm = ("subgroup of <" + ", ".join(str(p) for p in ps)
              + f"> of rank {rank}, index {idx}")
    return {"primes": ps, "rank": rank, "basis": B, "index": idx,
            "name": nm}


# ===========================================================================
# SEC 1.  ANCHORS — D72's / D74's committed census must reproduce EXACTLY.
#         exit 1 here only.
# ===========================================================================

print()
print("-" * 78)
print("SEC 1  ANCHORS — the committed transport census (exit 1 on failure)")
print("-" * 78)

AB = ("A", "B")
ABC = ("A", "B", "C")

ARMS = {}
_t = time.time()

for _nm, _actors, _dep, _pref in (("AB4", AB, 4, "AB"),
                                  ("ABC3", ABC, 3, "ABC")):
    fam, cache = enumerate_line(b1_cand, _actors, _dep)
    st, rat, kinds, okinds, defs, half, closed = square_census(
        fam, cache, _actors, _dep)
    dely = sum(1 for h, eA, eB, r, *_ in defs if 'd' in (eA[0], eB[0]))
    dely_h = sum(1 for h, eA, eB, k in half if 'd' in (eA[0], eB[0]))
    mind = min((len(h) + 2 for h, *_ in defs), default=None)
    ARMS[_nm] = dict(label=f"{_nm} {_actors} depth<={_dep}", actors=_actors,
                     dep=_dep, fam=fam, cache=cache, st=st, rat=rat,
                     kinds=kinds, okinds=okinds, defs=defs, half=half,
                     closed=closed, filt=None,
                     nonunit=Counter({k: v for k, v in rat.items()
                                      if k != 1}))
    report(f"{_nm} family", f"{len(fam)} histories")
    report(f"{_nm} exchange-square census", dict(st))
    report(f"{_nm} exact ratios dP_AB/dP_BA", fmt(rat))
    report(f"{_nm} defect kinds", fmtk(kinds))
    report(f"{_nm} half-open kinds", fmtk(okinds))

    anchor(f"{_nm}.1 D72's T6.1 row reproduces EXACTLY — history count, "
           f"closed-square count, the full ratio multiset (unit AND "
           f"non-unit), the kind census, the both-blocked count, the "
           f"delivery-bearing fraction and the shallowest defect depth",
           len(fam) == ANCH[_pref + "_hist"]
           and st["closed"] == ANCH[_pref + "_closed"]
           and dict(rat) == ANCH[_pref + "_full_ratios"]
           and dict(kinds) == ANCH[_pref + "_kinds"]
           and dely == len(defs) == ANCH[_pref + "_defects"]
           and st["both-blocked"] == ANCH[_pref + "_bothblocked"]
           and mind == ANCH["AB_mindepth"],
           f"histories {len(fam)} (quoted {ANCH[_pref + '_hist']}); closed "
           f"{st['closed']} (quoted {ANCH[_pref + '_closed']}); non-unit "
           f"{len(defs)} (quoted {ANCH[_pref + '_defects']}); ratios "
           f"{fmt(rat)}; kinds match = "
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
           f"{ANCH[_pref + '_halfopen']}); kinds {fmtk(okinds)}; "
           f"delivery-bearing {dely_h}/{len(half)}")

# --- the minimal witness, digit for digit (T6.4) ---------------------------
_A = ARMS["AB4"]
_wit = min(_A["defs"], key=lambda z: (len(z[0]), sk((z[0], z[1], z[2]))))
_h, _eA, _eB, _r, _qA, _qB2, _qB, _qA2 = _wit
_mu = {(): Fr(1)}
for _hh in sorted(_A["fam"], key=len):
    if _hh:
        _par = tuple(_hh[:-1])
        _mu[tuple(_hh)] = _mu[_par] * Fr(
            [q for ee, q in _A["cache"][_par] if ee == _hh[-1]][0])
_muAB = _mu[_h] * _qA * _qB2
_muBA = _mu[_h] * _qB * _qA2
print("  [DATA] THE MINIMAL WITNESS (AB4), in full:")
print(f"           h   = {list(_h)}")
print(f"           eA  = {_eA}")
print(f"           eB  = {_eB}")
print(f"           q(eA|h) = {_qA} , q(eB|h.eA) = {_qB2}")
print(f"           q(eB|h) = {_qB} , q(eA|h.eB) = {_qA2}")
print(f"           dP_AB/dP_BA = {_r};  mu(h.eA.eB) = {_muAB} vs "
      f"mu(h.eB.eA) = {_muBA}")
anchor("W.1 D72's T6.4 minimal witness reproduces digit for digit — all "
       "four step weights, the ratio, and both whole-history mu values",
       (_qA, _qB2, _qB, _qA2, _r, _muAB, _muBA)
       == (ANCH["wit_qA"], ANCH["wit_qB2"], ANCH["wit_qB"], ANCH["wit_qA2"],
           ANCH["wit_r"], ANCH["wit_muAB"], ANCH["wit_muBA"]),
       f"({_qA}, {_qB2}, {_qB}, {_qA2}) -> {_r}; mu {_muAB} vs {_muBA}")

# --- D74's group, recomputed ----------------------------------------------
_valset = set(ARMS["AB4"]["nonunit"]) | set(ARMS["ABC3"]["nonunit"])
_G = group_of(_valset)
report("the transport holonomy group, recomputed as an integer exponent "
       "lattice (Hermite reduction on the prime valuations)",
       f"value set {sorted(str(x) for x in _valset)}; prime support "
       f"{_G['primes']}; lattice basis {_G['basis']}; rank {_G['rank']}; "
       f"index in Z^{_G['rank']} = {_G['index']}; group {_G['name']}")
anchor("G.1 D74's group row reproduces EXACTLY: the value set is "
       "{1/2, 2/3, 3/2, 2} and the group it generates is <2,3>, free "
       "abelian of rank 2, index 1 in Z^2 — the FULL group of 3-smooth "
       "positive rationals",
       _valset == ANCH["group_valueset"]
       and _G["primes"] == ANCH["group_primes"]
       and _G["rank"] == ANCH["group_rank"]
       and _G["index"] == ANCH["group_index"],
       f"value set matches = {_valset == ANCH['group_valueset']}; primes "
       f"{_G['primes']}; rank {_G['rank']}; index {_G['index']}")

report("SEC 1 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 2.  LD-A — THE REVERSAL FUNCTOR
# ===========================================================================

print()
print("-" * 78)
print("SEC 2  LD-A — THE REVERSAL FUNCTOR ON THE COMMITTED TRANSPORT LAYER")
print("-" * 78)

print("""  THE CONSTRUCTION, STATED BEFORE IT IS RUN.  A committed record is a
  sequence of events; its causal order is the committed event_poset,
  generated by register overlap in sequence order.  The record-category
  reversal is the formal opposite of that order.  It is realised on
  sequences by

      R(e_1, ..., e_n) = (rho(e_n), ..., rho(e_1))

  where rho is the EVENT-KIND RELABELLING that reversal forces.  Only one
  committed event kind carries a direction in its own data — delivery,
  ('d', s, r, v), whose sender and receiver are distinct fields.  A send
  read backwards is a receive, so rho transposes them.  Every other
  committed kind is a single-carrier local event whose data carries no
  direction, so rho fixes it: the polarity of p, r, m is carried by the
  POSET, not by the label, and the poset is what R reverses.

  THE RELABELLING TABLE (the deliverable), with the register set each
  kind occupies — regs_of is what generates the causal order, so rho must
  preserve it for R to be poset reversal at all:

    kind  committed form         rho(e)                 regs_of        dual
    ----  ---------------------  ---------------------  -------------  ----
    n     ('n', a)               ('n', a)               {a}            self
    p     ('p', a, b, x)         ('p', a, b, x)         {a}            self
    r     ('r', a, ck, wk)       ('r', a, ck, wk)       props+created  self
    m     ('m', a, pk, w)        ('m', a, pk, w)        {a, mw}        self
    d     ('d', s, r, v)         ('d', r, s, v)         {s, r}         SWAP

  rho is an involution by inspection and by exhaustive gate A.1.  It
  preserves regs_of because regs_of('d', s, r, v) = {s, r} is unordered
  (gate A.2) — which is precisely why R is EXACTLY poset reversal
  (gate A.4) and not merely something like it.""")

_t = time.time()


def rho(e):
    """The forced event-kind relabelling.  Delivery transposes sender and
    receiver; every other committed kind is self-dual as a label."""
    if e[0] == 'd':
        return ('d', e[2], e[1], e[3])
    return e


def rev(seq):
    """The reversal functor on records: reverse the sequence and relabel.
    R(R(h)) = h identically, gated at A.3."""
    return tuple(rho(e) for e in reversed(tuple(seq)))


def rho_id(e):
    """CONTROL: reversal with NO relabelling (D74's D5 arm's operation)."""
    return e


def rev_with(seq, r_):
    return tuple(r_(e) for e in reversed(tuple(seq)))


# the full realised event alphabet, over every arm built so far
def alphabet_of(arm):
    out = set()
    for h, c in arm["cache"].items():
        out.update(h)
        for e, q in c:
            out.add(e)
    for h in arm["fam"]:
        out.update(h)
    return out


ALPHA = set()
for _nm in ("AB4", "ABC3"):
    ALPHA |= alphabet_of(ARMS[_nm])
report("the realised event alphabet of the anchor arms",
       f"{len(ALPHA)} distinct events; kinds "
       f"{fmtk(Counter(e[0] for e in ALPHA))}")

check("A.1 rho IS AN INVOLUTION ON THE COMMITTED EVENT ALPHABET, "
      "EXHAUSTIVELY: rho(rho(e)) = e for every event the committed layer "
      "realises in either anchor arm, structure-equal, not merely equal "
      "up to a canonical form",
      all(rho(rho(e)) == e for e in ALPHA) and len(ALPHA) > 0,
      f"{sum(1 for e in ALPHA if rho(rho(e)) == e)}/{len(ALPHA)} events "
      f"satisfy rho^2 = id; the {sum(1 for e in ALPHA if e[0] == 'd')} "
      f"delivery events are the ones rho moves, "
      f"{sum(1 for e in ALPHA if rho(e) != e)} events moved in total")

check("A.2 rho PRESERVES THE REGISTER SET, EXHAUSTIVELY: regs_of(rho(e)) "
      "= regs_of(e) for every realised event.  This is not decoration — "
      "the committed causal order is GENERATED by register overlap, so "
      "this identity is exactly the reason R is poset reversal.  It holds "
      "because the delivery's register set {s, r} is unordered: the "
      "committed layer already treats a delivery as a JOIN of two "
      "carriers and records no direction in the register geometry.  The "
      "direction lives only in the field order, which is what rho acts on",
      all(b1_regs(rho(e)) == b1_regs(e) for e in ALPHA),
      f"{sum(1 for e in ALPHA if b1_regs(rho(e)) == b1_regs(e))}/"
      f"{len(ALPHA)} events preserve their register set under rho")

# --- A.3  involutivity of R on records -------------------------------------
_inv_tot = _inv_ok = 0
for _nm in ("AB4", "ABC3"):
    for _hh in ARMS[_nm]["fam"]:
        _inv_tot += 1
        if rev(rev(_hh)) == tuple(_hh):
            _inv_ok += 1
check("A.3 THE INVOLUTIVITY GATE (pin LD-A): R(R(h)) RESTORES THE "
      "ORIGINAL RECORD EXACTLY, ON EVERY RECORD OF EVERY ARM.  The "
      "comparison is structural tuple equality on the full event "
      "sequence — every field of every event, in order — not equality of "
      "a canonical form and not equality of a derived invariant.  The "
      "functor is therefore an involution on records, and the door it "
      "opens or shuts is not opened or shut by an artefact of the "
      "construction",
      _inv_ok == _inv_tot and _inv_tot > 0,
      f"{_inv_ok}/{_inv_tot} records over both anchor arms satisfy "
      f"R(R(h)) == h, structure-equal")

# --- A.4  R is exactly poset reversal --------------------------------------
def poset_pairs(seq):
    p = b1_ep(list(seq))
    return set((i, j) for j in range(len(seq)) for i in p[j])


_pos_tot = _pos_ok = 0
for _nm in ("AB4", "ABC3"):
    for _hh in ARMS[_nm]["fam"]:
        n = len(_hh)
        P = poset_pairs(tuple(_hh))
        Q = poset_pairs(rev(_hh))
        Qm = {(n - 1 - i, n - 1 - j) for (i, j) in Q}
        _pos_tot += 1
        if Qm == {(j, i) for (i, j) in P}:
            _pos_ok += 1
check("A.4 R IS EXACTLY POSET REVERSAL, NOT AN APPROXIMATION OF IT: for "
      "every record of both anchor arms, the committed event_poset of "
      "R(h), pulled back along the index reversal i -> n-1-i, is the "
      "OPPOSITE of the committed event_poset of h — the full relation, "
      "pair for pair, in both directions.  This is the sense in which "
      "this unit reverses the RECORD CATEGORY rather than a traversal "
      "direction (QUOTES['d74_D1']: traversal reversal is an algebraic "
      "identity of the definition of r and says nothing about the "
      "category)",
      _pos_ok == _pos_tot and _pos_tot > 0,
      f"{_pos_ok}/{_pos_tot} records: event_poset(R(h)) = "
      f"event_poset(h)^op exactly")

# --- A.5  the pushforward reading is an identity ---------------------------
check("A.5 THE PUSHFORWARD READING CARRIES NO INFORMATION, AND IS "
      "DECLARED SO BEFORE THE CENSUS.  One can always define the opposite "
      "weighted category C^op abstractly by DECREEING q^op(rho(e) | R(h.e)) "
      ":= q(e | h).  Then mu^op(R(sigma)) = mu(sigma) for every record by "
      "construction, so every holonomy value is trivially INVARIANT and "
      "the census would answer its own question.  Every category has an "
      "opposite; the content of the last door is not whether C^op EXISTS "
      "but whether it is REALISED by the committed law — whether the "
      "committed admission relation and the committed weights price the "
      "reversed record.  That, and only that, is what SEC 3 measures",
      True,
      "stated, not measured: mu^op(R(sigma)) := mu(sigma) is a definition",
      corollary_of="an identity of the definition of the pushforward; it "
      "has no failing branch on any grammar and is recorded so that the "
      "census cannot later be read as having tested it")

report("SEC 2 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 3.  LD-B — THE CENSUS
# ===========================================================================

print()
print("-" * 78)
print("SEC 3  LD-B — THE CENSUS: every holonomy-carrying loop, reversed")
print("-" * 78)

print("""  THE QUANTITY, AND THE CONVENTION, STATED BEFORE IT IS RUN.  A closed
  exchange square is the loop h -> h.eA -> h.eA.eB = h.eB.eA -> h.eB -> h.
  Its committed holonomy is

      v = q(eA|h) q(eB|h.eA) / q(eB|h) q(eA|h.eB) = mu(sigma_AB)/mu(sigma_BA)

  with sigma_AB = h.eA.eB and sigma_BA = h.eB.eA — the common prefix
  cancels (gated at B.0).  Under R the two endpoint records go to
  R(sigma_AB) and R(sigma_BA), so the reversed counterpart is

      v_rev := mu(R(sigma_AB)) / mu(R(sigma_BA))                [CONVENTION]

  the FUNCTOR-IMAGE convention: the numerator of v_rev is the image of the
  numerator of v.  mu is the COMMITTED measure — the product of the
  committed conditional weights, read from the empty record by the
  committed admission relation.  Nothing here is decreed; the committed
  law is asked to price a record it did not build.

  THE FOUR CLASSES.
     INVERSION   v_rev = v^-1        the classical transformation law
     INVARIANT   v_rev = v           the fixed sector
     OTHER       v_rev defined, neither         <- the door opening
     UNDEFINED   R(sigma_AB) or R(sigma_BA) is not an admissible record of
                 the committed grammar, so the committed law assigns the
                 reversed record no weight at all

  On a loop with v = 1 the first two classes COINCIDE (1 = 1^-1); those
  are counted separately and never as evidence of either.  The orientation
  convention above exchanges INVERSION and INVARIANT if flipped, and the
  flipped reading is reported at B.5 (CTL-ORDER).  OTHER and UNDEFINED are
  CONVENTION-FREE: no choice of orientation can move a loop into or out of
  them.  The verdict therefore rests on convention-free classes.""")

_t = time.time()


def classify(v, v_rev):
    if v_rev is None:
        return "UNDEFINED"
    if v == 1:
        return "unit (INVERSION = INVARIANT)" if v_rev == 1 else "OTHER"
    if v_rev == Fr(1) / v:
        return "INVERSION"
    if v_rev == v:
        return "INVARIANT"
    return "OTHER"


def reversal_census(arm, relab=rho, opp_filt="mirror"):
    """The LD-B census on one arm.  `opp_filt`: the sub-grammar in which
    the reversed record is asked for admission.  'mirror' = the rho-image
    of the arm's own declared sub-grammar (the honest opposite of a
    DIRECTED schedule: the opposite of 'A may send to B' is 'B may send
    to A'); 'same' = the arm's own sub-grammar, kept as a control."""
    actors = arm["actors"]
    f = arm["filt"]
    if f is None:
        of = None
    elif opp_filt == "mirror":
        of = (lambda e: f(relab(e)))
    else:
        of = f
    rows = []
    for h, eA, eB, v in arm["closed"]:
        sAB = tuple(h) + (eA, eB)
        sBA = tuple(h) + (eB, eA)
        RA = rev_with(sAB, relab)
        RB = rev_with(sBA, relab)
        mA = mu_of_sequence(RA, actors, of)
        mB = mu_of_sequence(RB, actors, of)
        v_rev = (mA / mB) if (mA is not None and mB is not None) else None
        rows.append((h, eA, eB, v, v_rev, mA is not None, mB is not None,
                     RA, RB))
    return rows, of


def census_tables(label, rows):
    """Print the census BOTH WAYS: by value class and by loop class."""
    cls = Counter(classify(v, vr) for _h, _a, _b, v, vr, _oa, _ob, _RA, _RB
                  in rows)
    print(f"  [DATA] {label} — classification totals: {fmtk(cls)}")

    # WAY 1: by value class (the holonomy value v)
    byval = defaultdict(Counter)
    for _h, _a, _b, v, vr, _oa, _ob, _RA, _RB in rows:
        byval[v][classify(v, vr)] += 1
    print(f"  [DATA] {label} — BOTH WAYS (1/2), BY VALUE CLASS:")
    print(f"           {'v':>8}  {'loops':>6}  classification")
    for v in sorted(byval, key=lambda z: (z != 1, z)):
        print(f"           {str(v):>8}  {sum(byval[v].values()):>6}  "
              f"{fmtk(byval[v])}")

    # WAY 2: by loop class (the ordered kind pair of the two exchanged
    # events, which is D72's / D74's own defect-kind axis)
    bykind = defaultdict(Counter)
    for _h, eA, eB, v, vr, _oa, _ob, _RA, _RB in rows:
        bykind[(eA[0], eB[0])][classify(v, vr)] += 1
    print(f"  [DATA] {label} — BOTH WAYS (2/2), BY LOOP CLASS (kind pair):")
    print(f"           {'kinds':>8}  {'loops':>6}  classification")
    for k in sorted(bykind, key=str):
        print(f"           {str(k):>8}  {sum(bykind[k].values()):>6}  "
              f"{fmtk(bykind[k])}")

    # the holonomy-carrying sub-census, isolated
    carry = [row for row in rows if row[3] != 1]
    ccls = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in carry)
    print(f"  [DATA] {label} — THE HOLONOMY-CARRYING LOOPS ONLY "
          f"({len(carry)} of {len(rows)}): {fmtk(ccls)}")
    return cls, ccls, carry


# --- B.0  the mu-ratio form of v is the census form -------------------------
_mr_tot = _mr_ok = 0
for _nm in ("AB4", "ABC3"):
    arm = ARMS[_nm]
    for h, eA, eB, v in arm["closed"]:
        mA = mu_of_sequence(tuple(h) + (eA, eB), arm["actors"])
        mB = mu_of_sequence(tuple(h) + (eB, eA), arm["actors"])
        _mr_tot += 1
        if mA is not None and mB is not None and mA / mB == v:
            _mr_ok += 1
check("B.0 THE FORM v = mu(sigma_AB)/mu(sigma_BA) IS THE CENSUS FORM, "
      "EXACTLY.  The census computes v from the four step weights; the "
      "reversed side must compute it from whole records, because R does "
      "not preserve the common-prefix structure — under R the two "
      "exchanged events move to the FRONT and the prefix h becomes a "
      "common SUFFIX.  This gate confirms the two forms agree on every "
      "closed square of both anchor arms before the reversed side uses "
      "the second one, so no step of the comparison is smuggled",
      _mr_ok == _mr_tot and _mr_tot > 0,
      f"{_mr_ok}/{_mr_tot} closed squares: the whole-record mu ratio "
      f"equals the four-step ratio exactly")

# --- B.1  the anchor arms ---------------------------------------------------
print()
print("  [B.1]  THE ANCHOR ARMS.")
ROWS = {}
for _nm in ("AB4", "ABC3"):
    rows, _of = reversal_census(ARMS[_nm])
    ROWS[_nm] = rows
    census_tables(ARMS[_nm]["label"], rows)

_carry_all = [row for _nm in ("AB4", "ABC3") for row in ROWS[_nm]
              if row[3] != 1]
_carry_cls = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in _carry_all)
check("B.1 THE CENSUS ON THE COMMITTED HOLONOMY-CARRYING LOOPS.  Every "
      "one of D74's 88 non-unit squares at (A,B) d<=4 and 12 at (A,B,C) "
      "d<=3 is carried through the functor and its reversed counterpart "
      "computed exactly.  NOT ONE of them has a reversed counterpart at "
      "all: for every single holonomy-carrying loop, the committed "
      "admission relation refuses the reversed record, so the committed "
      "law assigns it no weight and there is no v_rev to classify.  The "
      "classification of the holonomy-carrying sector is therefore "
      "0 INVERSION, 0 INVARIANT, 0 OTHER, 100 UNDEFINED",
      _carry_cls["UNDEFINED"] == len(_carry_all)
      and len(_carry_all) == ANCH["AB_defects"] + ANCH["ABC_defects"],
      f"holonomy-carrying loops {len(_carry_all)} (= {ANCH['AB_defects']} "
      f"+ {ANCH['ABC_defects']}, the committed counts); classification "
      f"{fmtk(_carry_cls)}")

_flat_all = [row for _nm in ("AB4", "ABC3") for row in ROWS[_nm]
             if row[3] == 1]
_flat_def = [row for row in _flat_all if row[4] is not None]
_flat_one = [row for row in _flat_def if row[4] == 1]
check("B.2 WHERE THE FUNCTOR DOES LAND, IT LANDS ON 1.  Every loop whose "
      "reversed counterpart the committed law does price is a FLAT loop, "
      "and its reversed counterpart is flat too: v = v_rev = 1, so "
      "INVERSION and INVARIANT coincide and neither is evidence.  The "
      "census contains no loop at which the two classes are "
      "distinguishable, in either direction",
      len(_flat_one) == len(_flat_def) and len(_flat_def) > 0
      and all(row[4] is None for row in _carry_all),
      f"{len(_flat_def)} of {len(_flat_all) + len(_carry_all)} loops have "
      f"a priced reversed counterpart; {len(_flat_one)}/{len(_flat_def)} "
      f"of those have v = v_rev = 1; loops with v != 1 and a priced "
      f"counterpart: "
      f"{sum(1 for row in _carry_all if row[4] is not None)}")

# --- B.3  the half-open squares --------------------------------------------
print()
print("  [B.3]  THE 40 HALF-OPEN SQUARES (committed T6.2).  A half-open")
print("         square carries no holonomy value — one traversal order is")
print("         blocked — so the question R asks of it is different: does")
print("         the functor carry its ADMISSIBLE endpoint to an admissible")
print("         record, and does the half-openness transpose?")
_ho_rows = []
for _nm in ("AB4", "ABC3"):
    arm = ARMS[_nm]
    for h, eA, eB, side in arm["half"]:
        good = (eA, eB) if side == "AB-only" else (eB, eA)
        bad = (eB, eA) if side == "AB-only" else (eA, eB)
        sg = tuple(h) + good
        sb = tuple(h) + bad
        mg = mu_of_sequence(rev(sg), arm["actors"])
        mb = mu_of_sequence(rev(sb), arm["actors"])
        _ho_rows.append((_nm, side, mg is not None, mb is not None))
_ho = Counter((r[1], "R(open) priced" if r[2] else "R(open) refused",
               "R(blocked) priced" if r[3] else "R(blocked) refused")
              for r in _ho_rows)
report("half-open squares under R, both ways (by side, by image status)",
       fmtk(_ho))
check("B.3 THE HALF-OPEN SQUARES DO NOT SURVIVE THE FUNCTOR EITHER.  All "
      "40 committed half-open squares are delivery-bearing (T6.2) and the "
      "functor carries the admissible endpoint of every one of them to a "
      "record the committed law refuses.  There is no transposed "
      "half-openness to read, because there is no priced image to read it "
      "from",
      all(not r[2] for r in _ho_rows) and len(_ho_rows) == 40,
      f"{sum(1 for r in _ho_rows if not r[2])}/{len(_ho_rows)} half-open "
      f"squares have their open endpoint refused under R; "
      f"{sum(1 for r in _ho_rows if r[3])} have their blocked endpoint "
      f"priced under R")

# --- B.4  the Born = K1 arbitration row ------------------------------------
print()
print("  [B.4]  THE BORN = K1 ARBITRATION ROW (paper 31 sec.4.3).")
print("""         The committed row is the 2-conflict: two incomparable live
         proposals on the same base with different values, arbitrated by
         one holder.  Paper 31 states the squared branch amplitudes of
         V_pair are exactly 1/2-1/2 — the K1 law on the 2-conflict,
         recomputed from the layer — and that the arbitration sector of
         the menu reconstructs to 1/4.  Both are recomputed here from the
         committed layer, and then the SAME row is asked of the reversed
         record.""")

_born_fix = []
for _hh in ARMS["AB4"]["fam"]:
    for e, q in ARMS["AB4"]["cache"][tuple(_hh)]:
        if e[0] == 'r' and len(e[2]) == 2:
            _born_fix.append((tuple(_hh), e, Fr(q)))
_born_fix.sort(key=lambda z: (len(z[0]), sk((z[0], z[1]))))
_bh, _be, _bq = _born_fix[0]
_acts2 = list(_bh) + [_be]
_bview = b1_View(_acts2, b1_ep(_acts2), b1_ep(_acts2)[len(_acts2) - 1])
_bcomp = [c for c in b1_arbcomps(_bview, _be[1])
          if b1_triples(_bview, c[1]) == _be[2]][0]
_bet = b1_edgetri(_bview, _bcomp[1])
_bK1 = b1_PK1(_be[2], _bet)
_bbranches = sorted(((x, Fr(qq)) for x, qq in ARMS["AB4"]["cache"][_bh]
                     if x[0] == 'r' and x[1] == _be[1] and x[2] == _be[2]),
                    key=lambda z: sk(z[0]))
print(f"           h  = {list(_bh)}")
print(f"           e  = arbitration by {_be[1]} on the 2-conflict")
print(f"           K1(ckey) = "
      f"{ {str(sorted(k, key=str)): str(v) for k, v in sorted(_bK1.items(), key=lambda z: sk(z[0]))} }")
print(f"           committed branch weights = "
      f"{[str(q) for x, q in _bbranches]}; sector total = "
      f"{sum(q for x, q in _bbranches)}")
_bK1vals = Counter(_bK1.values())
_bsector = sum(q for x, q in _bbranches)
anchor("K1.1 paper 31 sec.4.3's Born = K1 row reproduces EXACTLY from the "
       "committed layer: the K1 branch weights on the 2-conflict are "
       "1/2-1/2 and the arbitration sector of the menu is 1/4",
       dict(_bK1vals) == ANCH["born_K1"] and _bsector == ANCH["born_sector"]
       and len(_bbranches) == 2,
       f"K1 branch multiset {fmt(_bK1vals)} (quoted {{1/2: 2}}); "
       f"arbitration sector {_bsector} (quoted {ANCH['born_sector']}); "
       f"{len(_bbranches)} branches")

_bRA = rev(tuple(_bh) + (_be,))
_bmu_f = mu_of_sequence(tuple(_bh) + (_be,), AB)
_bmu_r = mu_of_sequence(_bRA, AB)
_bi, _bblk, _bwhy = first_blocker(_bRA, AB)
print(f"           R(record) = {[x[0] for x in _bRA]} (kinds, in order)")
print(f"           mu(record) = {_bmu_f};  mu(R(record)) = {_bmu_r}")
print(f"           first blocker: index {_bi}, kind '{_bblk[0]}', {_bwhy}")
check("B.4 THE BORN = K1 ROW HAS NO REVERSED COUNTERPART.  The committed "
      "record prices to an exact rational; its image under R is refused "
      "by the committed admission relation at its very first event — the "
      "arbitration, which in the reversed record stands BEFORE the two "
      "proposals whose conflict it resolves.  The K1 kernel is a function "
      "of the live-proposal component visible in the arbitrator's past "
      "cone; in the reversed record that past cone is empty, so there is "
      "no component, no ckey, no K1 weight and no Born split to compare.  "
      "The row does not invert, does not stay fixed, and is not OTHER: it "
      "is not there",
      _bmu_f is not None and _bmu_r is None and _bi == 0
      and _bblk[0] == 'r',
      f"forward mu = {_bmu_f}; reversed mu = {_bmu_r}; first blocker at "
      f"index {_bi}, kind '{_bblk[0]}'")

# --- B.5  CTL-ORDER: the orientation convention ----------------------------
print()
print("  [B.5]  CTL-ORDER — the orientation convention, controlled.")
_flip = Counter()
for _nm in ("AB4", "ABC3"):
    for _h, _a, _b, v, vr, *_ in ROWS[_nm]:
        _flip[classify(v, (Fr(1) / vr) if vr is not None else None)] += 1
_fwdcls = Counter(classify(v, vr) for _nm in ("AB4", "ABC3")
                  for _h, _a, _b, v, vr, *_ in ROWS[_nm])
report("classification under the functor-image convention", fmtk(_fwdcls))
report("classification under the FLIPPED convention "
       "(v_rev := mu(R(sigma_BA))/mu(R(sigma_AB)))", fmtk(_flip))
check("B.5 THE VERDICT IS CONVENTION-FREE.  Flipping the orientation "
      "convention exchanges INVERSION with INVARIANT and can do nothing "
      "else, since the two readings differ by an exact reciprocal.  Both "
      "convention-free classes — OTHER and UNDEFINED — have identical "
      "counts under both readings, and in particular the count of OTHER "
      "is 0 either way and the count of UNDEFINED is the same either way.  "
      "No choice of orientation opens or shuts the door",
      _flip["OTHER"] == _fwdcls["OTHER"]
      and _flip["UNDEFINED"] == _fwdcls["UNDEFINED"],
      f"OTHER {_fwdcls['OTHER']} vs {_flip['OTHER']}; UNDEFINED "
      f"{_fwdcls['UNDEFINED']} vs {_flip['UNDEFINED']}")

# --- B.6  the relabelling control ------------------------------------------
print()
print("  [B.6]  THE RELABELLING CONTROL — is the negative an artefact of")
print("         the chosen rho?  Every involutive relabelling available at")
print("         transport scope is run: the identity (no relabelling, which")
print("         is D74's D5 arm's operation), the forced delivery")
print("         transposition, and each of those composed with every actor")
print("         relabelling of the arm's own pool (the pool's symmetry")
print("         group).  The swept class is: {identity, delivery")
print("         transposition} x pool permutations.  It is NOT exhaustive")
print("         over all involutive regs_of-preserving relabellings of the")
print("         realised alphabet (the hostile round exhibited the")
print("         proposal-bit swap on 'p' events: involutive, admissible,")
print("         unswept — and verdict-preserving, 0/100 curved loops")
print("         priced under it); irreparability therefore rests on C.3's")
print("         argument, not on sweep exhaustiveness.")


def actor_perm_relab(perm, swap_d):
    """Relabel actors by `perm` (a dict), optionally transposing delivery.
    Applied to every actor field the committed alphabet carries, including
    those inside proposal triples, arb ckeys/wkeys and merge pair keys."""
    def act(x):
        return perm.get(x, x)

    def fixv(v):
        if v == V0:
            return v
        if v[1] == 'm':
            return ('v', 'm', tuple(sorted((fixv(v[2][0]), fixv(v[2][1])),
                                           key=repr)), v[3], act(v[4]))
        return ('v', v[1], v[2], tuple(sorted(act(a) for a in v[3])),
                act(v[4]))

    def fixtrip(t):
        return (act(t[0]), fixv(t[1]), t[2])

    def f(e):
        k = e[0]
        if k == 'n':
            return ('n', act(e[1]))
        if k == 'p':
            return ('p', act(e[1]), fixv(e[2]), e[3])
        if k == 'd':
            s, r = (e[2], e[1]) if swap_d else (e[1], e[2])
            return ('d', act(s), act(r), fixv(e[3]))
        if k == 'r':
            return ('r', act(e[1]),
                    frozenset(fixtrip(t) for t in e[2]),
                    frozenset(fixtrip(t) for t in e[3]))
        return ('m', act(e[1]),
                tuple(sorted((fixv(e[2][0]), fixv(e[2][1])), key=repr)),
                e[3] if e[3] == 'both' else fixv(e[3]))
    return f


_relabs = []
for _nm in ("AB4", "ABC3"):
    pool = ARMS[_nm]["actors"]
    for perm_t in sorted(permutations(pool)):
        perm = dict(zip(pool, perm_t))
        for swap_d in (False, True):
            nm = (("swap-d" if swap_d else "id-d") + " x "
                  + ("id-actors" if perm_t == pool
                     else "actors " + "".join(perm_t)))
            _relabs.append((_nm, nm, actor_perm_relab(perm, swap_d), perm_t,
                            swap_d))
_relab_rows = []
for _nm, nm, f, perm_t, swap_d in _relabs:
    arm = ARMS[_nm]
    invol = all(f(f(e)) == e for e in alphabet_of(arm))
    ok = 0
    tot = 0
    for h, eA, eB, v, *_ in arm["defs"]:
        tot += 1
        mA = mu_of_sequence(rev_with(tuple(h) + (eA, eB), f), arm["actors"])
        mB = mu_of_sequence(rev_with(tuple(h) + (eB, eA), f), arm["actors"])
        if mA is not None and mB is not None:
            ok += 1
    _relab_rows.append((_nm, nm, invol, ok, tot))
    report(f"{_nm} relabelling {nm}",
           f"involutive = {invol}; holonomy-carrying loops with a priced "
           f"reversed counterpart: {ok}/{tot}")
_relab_inv = [r for r in _relab_rows if r[2]]
_relab_non = [r for r in _relab_rows if not r[2]]
check("B.6 NO INVOLUTIVE RELABELLING AVAILABLE AT TRANSPORT SCOPE RESCUES "
      "THE FUNCTOR.  The pin's construction requires rho to be an "
      "INVOLUTION, so the gate is stated on the involutive relabellings "
      "only — the identity, the forced delivery transposition, and each "
      "composed with every involutive actor permutation of the arm's "
      "pool, applied to every actor field the alphabet carries (proposal "
      "triples, arb ckeys and wkeys, merge pair keys, version "
      "authorship).  Not one holonomy-carrying loop acquires a priced "
      "reversed counterpart under any of them.  The negative is a "
      "property of the grammar, not of a choice of rho",
      all(r[3] == 0 for r in _relab_inv) and len(_relab_inv) > 0,
      f"{len(_relab_inv)} involutive relabellings: "
      + "; ".join(f"{r[0]} {r[1]}: {r[3]}/{r[4]}" for r in _relab_inv))
check("B.6b THE NON-INVOLUTIVE SWEEP, REPORTED SEPARATELY AND NOT AS "
      "EVIDENCE FOR THE PIN'S CONSTRUCTION.  The 3-cycles of the "
      "three-actor pool are not involutions, so a reversal built on them "
      "would fail the involutivity gate A.3 by construction and is not a "
      "relabelling this unit admits.  They are swept anyway, so that the "
      "reader can see the census does not move under them either",
      all(r[3] == 0 for r in _relab_non) and len(_relab_non) > 0,
      f"{len(_relab_non)} non-involutive relabellings: "
      + "; ".join(f"{r[0]} {r[1]}: {r[3]}/{r[4]}" for r in _relab_non))

report("SEC 3 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 4.  LD-C — THE OBSTRUCTION, CHARACTERIZED EXACTLY
# ===========================================================================

print()
print("-" * 78)
print("SEC 4  LD-C — THE OBSTRUCTION, CHARACTERIZED EXACTLY")
print("-" * 78)
_t = time.time()

print("""  The functor is an involution on records (A.3) and is exactly poset
  reversal (A.4).  What it is not is an operation on the committed
  GRAMMAR: its image leaves the grammar's support.  This section says
  where, on what, and why — exactly.""")

# --- C.1  the first blocker ------------------------------------------------
_blk = Counter()
_blk_by_arm = defaultdict(Counter)
_blk_pos = Counter()
_blk_rows = []
for _nm in ("AB4", "ABC3"):
    arm = ARMS[_nm]
    for h, eA, eB, v, vr, oA, oB, RA, RB in ROWS[_nm]:
        for R_, oo in ((RA, oA), (RB, oB)):
            if oo:
                continue
            i, e, why = first_blocker(R_, arm["actors"])
            _blk[e[0]] += 1
            _blk_by_arm[_nm][e[0]] += 1
            _blk_pos[i] += 1
            _blk_rows.append((_nm, v, i, e, R_))
report("first-blocking event KIND over every refused reversed record "
       "(both anchor arms)", fmtk(_blk))
report("first-blocking event kind, by arm",
       {k: fmtk(v) for k, v in sorted(_blk_by_arm.items())})
report("first-blocking POSITION in the reversed record", fmtk(_blk_pos))

_consuming = {'p', 'r', 'm', 'd'}
check("C.1 EVERY FIRST BLOCKER IS A CONSUMING KIND (a subset statement: "
      "the merge, also consuming, never appears because it is never "
      "realised at these depths — D.4), AND IDLE NEVER BLOCKS (a "
      "corollary, not a discovery: the idle's admission is unconditional "
      "in the committed layer, so this clause has no failing branch).  "
      "Every first blocker is one "
      "of the kinds whose admission relation reads its own causal "
      "past: a proposal (needs its base version held and not superseded), "
      "an arbitration (needs a live-proposal component in the "
      "arbitrator's past cone), a delivery (needs the sender to hold the "
      "version)",
      set(_blk) <= _consuming and 'n' not in _blk and sum(_blk.values()) > 0,
      f"blocking kinds {sorted(_blk)}; idle blocks "
      f"{_blk.get('n', 0)} times of {sum(_blk.values())} refusals")

# --- C.2  consumer before producer -----------------------------------------
_cbp_ok = _cbp_tot = 0
for _nm, v, i, e, R_ in _blk_rows:
    n = len(R_)
    # the blocker's forward causal past: in the forward record the blocker
    # sits at index n-1-i, and R is exactly poset reversal (A.4), so the
    # blocker's forward predecessors are exactly its reversed successors.
    P = b1_ep(list(R_))
    succ = {j for j in range(n) if i in P[j]}
    _cbp_tot += 1
    if succ:
        _cbp_ok += 1
check("C.2 THE OBSTRUCTION IS CONSUMPTION-BEFORE-PRODUCTION, AND IT IS "
      "EXACT.  For every refused reversed record, the first blocking "
      "event has a NON-EMPTY causal future in the reversed record — "
      "equivalently, by A.4, a non-empty causal past in the forward "
      "record.  The committed admission relation is past-relative: it "
      "reads the event's own past cone and admits only what that cone "
      "supports.  Reversal moves an event's whole support into its "
      "future, so a consuming event is offered to the admission relation "
      "before anything has produced what it consumes.  Nothing about the "
      "weights is involved; the refusal is at admission",
      _cbp_ok == _cbp_tot and _cbp_tot > 0,
      f"{_cbp_ok}/{_cbp_tot} refused reversed records have a first "
      f"blocker with non-empty causal future in the reversed record")

# --- C.3  the alphabet has no dual kind ------------------------------------
print()
print("""  [C.3]  WHY NO RELABELLING CAN REPAIR IT — the exact statement.
         A relabelling repairs the reversal only if it sends each
         consuming kind to a kind that PRODUCES what the original
         consumed: the dual of an arbitration (which consumes live
         proposals and produces a version) would have to consume a
         version and produce live proposals.  The committed alphabet is
         {n, p, r, m, d} and every one of p, r, m, d is monotone in the
         same direction — each ADDS to the record state (a live triple, a
         created version, a merged version, a holding) and none removes
         anything: the committed layer has no retraction, no withdrawal,
         no un-delivery and no un-merge.  The alphabet contains no
         annihilation kind, so no bijection of it can be a duality, and
         B.6 measures exactly that: every involutive relabelling in the
         alphabet's own symmetry group leaves the census at 0.""")
_creating = Counter()
for e in ALPHA:
    _creating[e[0]] += 1
report("committed event kinds and their state action",
       "{'n': consumes nothing, produces nothing (the residual-budget "
       "idle); 'p': consumes a held base version, produces a live "
       "proposal triple; 'r': consumes live proposal triples, produces a "
       "created version; 'm': consumes two held created versions, "
       "produces a merged version; 'd': consumes a holding of the sender, "
       "produces a holding of the receiver} — four producers, no "
       "annihilators")

# --- C.3a  the obstruction is EXACTLY the arbitration kind -----------------
def arb_table(names):
    """(record contains an arbitration event?) x (is its image priced?),
    over the closed squares of the named arms."""
    t = Counter()
    for nm in names:
        for h, eA, eB, v, vr, oA, oB, RA, RB in ROWS[nm]:
            s = tuple(h) + (eA, eB)
            t[(any(e[0] == 'r' for e in s), vr is not None)] += 1
    return t


_arbt = arb_table(("AB4", "ABC3"))
report("the obstruction, cross-tabulated: (record carries an arbitration) "
       "x (its image is priced), both anchor arms",
       {f"arb={k[0]}, priced={k[1]}": v
        for k, v in sorted(_arbt.items(), key=str)})
check("C.3a THE OBSTRUCTION IS EXACTLY ONE EVENT KIND — THE ARBITRATION — "
      "AND THE CHARACTERIZATION IS EXACT IN BOTH DIRECTIONS.  A closed "
      "square's reversed counterpart is priced by the committed law IF "
      "AND ONLY IF its endpoint record carries no arbitration event.  Not "
      "'mostly', not 'except for a residue': every one of the records "
      "carrying an arbitration is refused, and every one of the records "
      "carrying none is priced, on every closed square of both anchor "
      "arms.  The unifying mechanism: the arbitration is the only "
      "realised kind that CREATES a version and supersedes a base, so "
      "reversal puts consumers of created state before its creation.  "
      "The 'r' first blockers refuse on the emptied joint past cone (the "
      "live-proposal component with its incomparability edges); the "
      "census's 'p' and 'd' first blockers refuse on a created, non-V0 "
      "version read before its creator (classification per the hostile "
      "round, over all 144 non-arbitration blockers of C.1's census).  "
      "The arb-free direction is FORCED, not coincidental: an "
      "arbitration-free record holds only V0 versions, so no consumer "
      "can precede a creator there (the round verified additionally: at "
      "most one live proposal per (actor, base), 0 violations, all four "
      "arms)",
      _arbt[(True, True)] == 0 and _arbt[(False, False)] == 0
      and _arbt[(True, False)] > 0 and _arbt[(False, True)] > 0,
      f"arb-carrying and priced: {_arbt[(True, True)]}; arb-free and "
      f"refused: {_arbt[(False, False)]}; arb-carrying and refused: "
      f"{_arbt[(True, False)]}; arb-free and priced: "
      f"{_arbt[(False, True)]}")

# --- C.3b  every curved loop carries an arbitration ------------------------
_carry_arb = Counter()
for _nm in ("AB4", "ABC3"):
    for h, eA, eB, v, vr, *_ in ROWS[_nm]:
        if v != 1:
            _carry_arb[any(e[0] == 'r' for e in tuple(h) + (eA, eB))] += 1
check("C.3b EVERY HOLONOMY-CARRYING LOOP'S RECORD CARRIES AN ARBITRATION.  "
      "D72's committed kind census attributes only 68 of the 88 defects "
      "at (A,B) d<=4 to an exchanged pair containing an arbitration; the "
      "other 20 are (d,n), (d,d) and (n,d).  Measured on the WHOLE "
      "endpoint record rather than the exchanged pair, all of them carry "
      "one — the arbitration sits in the common prefix.  [MEASURED] on "
      "this window",
      _carry_arb[False] == 0 and _carry_arb[True] > 0,
      f"holonomy-carrying loops whose record carries an arbitration: "
      f"{_carry_arb[True]}; without: {_carry_arb[False]}")

# --- C.4  the disjointness statement ---------------------------------------
_def_rows = [row for _nm in ("AB4", "ABC3") for row in ROWS[_nm]
             if row[4] is not None]
_def_nonunit = [row for row in _def_rows if row[3] != 1]
check("C.4 REVERSAL-DEFINEDNESS AND HOLONOMY-CARRYING ARE DISJOINT ON "
      "THIS WINDOW.  Every loop whose reversed counterpart the committed "
      "law prices has v = 1; not one loop with v != 1 has a priced "
      "reversed counterpart.  The implication is one-directional — "
      "flatness does not buy reverse-definedness, since many flat loops "
      "are refused too.  The sharp form of the finding is a strict "
      "containment: the functor's domain is the arbitration-free locus "
      "(C.3a), and curvature implies arbitration (C.3b), so the curved "
      "locus lies strictly inside the refusal set — which also holds "
      "every flat arbitration-carrying loop",
      len(_def_nonunit) == 0 and len(_def_rows) > 0,
      f"loops with a priced reversed counterpart {len(_def_rows)}, of "
      f"which non-unit {len(_def_nonunit)}; flat loops refused "
      f"{sum(1 for row in _flat_all if row[4] is None)}",
      corollary_of="C.3a and C.3b together: every curved loop carries an "
      "arbitration (C.3b), and exactly the arbitration-carrying records "
      "are refused (C.3a).  C.4 is their conjunction and adds nothing to "
      "them")

# --- C.5  the negative is non-generic, not a support fact ------------------
_famrev = _famrev_ok = 0
for _nm in ("AB4", "ABC3"):
    arm = ARMS[_nm]
    for _hh in arm["fam"]:
        if len(_hh) < 2:
            continue
        _famrev += 1
        if mu_of_sequence(rev(_hh), arm["actors"]) is not None:
            _famrev_ok += 1
check("C.5 THE GRAMMAR IS NOT REVERSAL-BLOCKING — THE REFUSAL IS A "
      "PROPERTY OF THE ARBITRATION-CARRYING LOCUS (WHICH CONTAINS THE "
      "WHOLE CURVED LOCUS), NOT OF THE SUPPORT (D74's D5.0 "
      "lesson, re-measured under the RELABELLED reversal).  A clear "
      "majority of this grammar's records reverse, under R, into records "
      "the committed law prices.  So the 0-of-everything at the "
      "holonomy-carrying loops is not the generic fate of a reversed "
      "record; it is a sharp and highly non-generic property of the "
      "arbitration-carrying locus, which holds every loop that carries "
      "the transport curvature and the flat arbitration-carrying loops "
      "besides",
      _famrev_ok * 2 > _famrev and _famrev > 0,
      f"{_famrev_ok}/{_famrev} records (|h| >= 2) of the anchor arms have "
      f"a priced image under R")

# --- C.6  the all-linear-extensions control --------------------------------
print()
print("  [C.6]  THE ALL-LINEAR-EXTENSIONS CONTROL (D74 D5.2's idiom,")
print("         carried under the relabelling).  Refusal of ONE order is")
print("         not refusal of the opposite poset.  For every")
print("         holonomy-carrying loop of both anchor arms, every linear")
print("         extension of the reversed record's event poset is built")
print("         and offered to the committed admission relation.")
_le_tot = _le_fwd = _le_rev = _le_seq = 0
_le_arm = {}
for _nm in ("AB4", "ABC3"):
    arm = ARMS[_nm]
    a_tot = a_fwd = a_rev = a_seq = a_norel = 0
    for h, eA, eB, v, *_ in arm["defs"]:
        for s in (tuple(h) + (eA, eB), tuple(h) + (eB, eA)):
            a_seq += 1
            acts = list(s)
            for perm in b1_linext(acts):
                a_tot += 1
                seq = [acts[i] for i in perm]
                if mu_of_sequence(seq, arm["actors"]) is not None:
                    a_fwd += 1
                if mu_of_sequence(rev(seq), arm["actors"]) is not None:
                    a_rev += 1
                if mu_of_sequence(rev_with(seq, rho_id),
                                  arm["actors"]) is not None:
                    a_norel += 1
    _le_arm[_nm] = (a_seq, a_tot, a_fwd, a_rev, a_norel)
    _le_seq += a_seq
    _le_tot += a_tot
    _le_fwd += a_fwd
    _le_rev += a_rev
    report(f"{_nm} all linear extensions of the holonomy-carrying endpoints",
           f"{a_seq} endpoint records; {a_tot} linear extensions of their "
           f"committed event posets; {a_fwd} priced forwards; {a_rev} "
           f"priced under R; {a_norel} priced under reversal WITHOUT "
           f"relabelling")
anchor("D5.2 D74's committed order-dual row reproduces EXACTLY: at (A,B) "
       "d<=4 the 88 defective squares have 176 endpoint records with 304 "
       "linear extensions of their committed event posets, all 304 "
       "admissible forwards and 0 admissible reversed.  D74 measured this "
       "WITHOUT any event-kind relabelling; that reading is recomputed "
       "here alongside the relabelled one, and both are 0",
       _le_arm["AB4"][0] == 176 and _le_arm["AB4"][1] == 304
       and _le_arm["AB4"][2] == 304 and _le_arm["AB4"][4] == 0
       and _le_arm["AB4"][3] == 0,
       f"AB4: {_le_arm['AB4'][0]} endpoints (quoted 176), "
       f"{_le_arm['AB4'][1]} linear extensions (quoted 304), "
       f"{_le_arm['AB4'][2]}/{_le_arm['AB4'][1]} forwards (quoted 304), "
       f"{_le_arm['AB4'][4]}/{_le_arm['AB4'][1]} reversed without "
       f"relabelling (quoted 0), {_le_arm['AB4'][3]}/{_le_arm['AB4'][1]} "
       f"reversed with the forced relabelling")
report("all linear extensions of the holonomy-carrying endpoints, both "
       "anchor arms",
       f"{_le_seq} endpoint records; {_le_tot} linear extensions of their "
       f"committed event posets; {_le_fwd} priced forwards; {_le_rev} "
       f"priced under R")
check("C.6 THE OPPOSITE RECORD HAS NO PRICED REALISATION IN ANY ORDER.  "
      "Every linear extension of every holonomy-carrying endpoint's "
      "committed event poset is priced forwards — so the poset genuinely "
      "is the record's own causal order and nothing is smuggled — and NOT "
      "ONE of them is priced under R.  The refusal is of the opposite "
      "POSET, not of an enumeration order",
      _le_rev == 0 and _le_fwd == _le_tot and _le_tot > 0,
      f"{_le_fwd}/{_le_tot} priced forwards, {_le_rev}/{_le_tot} priced "
      f"under R, over {_le_seq} endpoints")

# --- C.7  the non-empty-prefix control -------------------------------------
print()
print("  [C.7]  THE NON-EMPTY-PREFIX CONTROL.  Reading the reversed")
print("         record from the EMPTY record is the strictest demand.  The")
print("         weaker one — does the reversed record occur ANYWHERE in")
print("         the grammar — is run here against every admissible prefix")
print("         of length <= 2 of each anchor arm.")
_pref_hits = 0
_pref_tot = 0
_pref_n = 0
for _nm in ("AB4", "ABC3"):
    arm = ARMS[_nm]
    prefixes = sorted((tuple(x) for x in arm["fam"] if len(x) <= 2), key=sk)
    _pref_n = max(_pref_n, len(prefixes))
    for h, eA, eB, v, *_ in arm["defs"]:
        for s in (tuple(h) + (eA, eB), tuple(h) + (eB, eA)):
            Rs = rev(s)
            _pref_tot += 1
            for p in prefixes:
                if mu_of_sequence(tuple(p) + Rs, arm["actors"]) is not None:
                    _pref_hits += 1
                    break
report("non-empty-prefix control",
       f"{_pref_tot} reversed holonomy-carrying endpoints tested against "
       f"up to {_pref_n} admissible prefixes each (|prefix| <= 2); "
       f"{_pref_hits} found a prefix that lets the committed law price "
       f"them")
check("C.7 THE REFUSAL IS NOT AN ARTEFACT OF STARTING FROM THE EMPTY "
      "RECORD.  Offered every admissible prefix of length <= 2 of its own "
      "arm as a context, not one reversed holonomy-carrying endpoint "
      "becomes priceable.  Supplying the missing past does not help, and "
      "the reason is structural: what the reversed record needs in its "
      "past are the very events it itself contains later, and the "
      "committed admission relation refuses a second live copy of a "
      "triple already live",
      _pref_hits == 0 and _pref_tot > 0,
      f"{_pref_hits}/{_pref_tot} reversed endpoints priced under some "
      f"prefix of length <= 2")

report("SEC 4 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 5.  LD-D — THE ASYMMETRIC / DEFECTED SCHEDULE FAMILIES
# ===========================================================================

print()
print("-" * 78)
print("SEC 5  LD-D — THE DEFECTED SCHEDULE FAMILIES (D73's lesson)")
print("-" * 78)
_t = time.time()

print("""  QUOTES['d73']: hand-built symmetry is a cage; carry at least one
  asymmetric substrate.  The two committed defected families are D74's
  own (QUOTES['d74_asym']): ASYM-1, the one-way link A->B, and ASYM-2,
  the defected directed ring A->B->C->A.  Both are declared SUB-GRAMMARS
  — the support is restricted, the committed weights are untouched.

  THE HONEST OPPOSITE OF A DIRECTED SCHEDULE IS THE MIRRORED SCHEDULE.
  rho transposes deliveries, so the rho-image of 'A may send to B' is
  'B may send to A'.  Asking the reversed record for admission in the
  arm's OWN sub-grammar would be a rigged test — it would fail on the
  link direction alone and tell us nothing about the record category.
  The census below therefore asks the reversed record for admission in
  the MIRROR sub-grammar, which is the categorical opposite of the
  schedule; the arm's own sub-grammar is kept as the second reading.""")


def oneway(e):
    """ASYM-1 (D74): the link A->B only."""
    return not (e[0] == 'd' and (e[1], e[2]) != ('A', 'B'))


def ring(e):
    """ASYM-2 (D74): the defected directed ring A->B->C->A."""
    return not (e[0] == 'd' and (e[1], e[2]) not in
                (('A', 'B'), ('B', 'C'), ('C', 'A')))


for _nm, _actors, _dep, _filt in (
        ("ASYM1", AB, 5, oneway),
        ("ASYM2", ABC, 4, ring)):
    fam, cache = enumerate_line(b1_cand, _actors, _dep - 2, filt=_filt)
    st, rat, kinds, okinds, defs, half, closed = square_census(
        fam, cache, _actors, _dep, filt=_filt)
    ARMS[_nm] = dict(label=(f"{_nm} {_actors} depth<={_dep} "
                            + ("one-way A->B" if _nm == "ASYM1"
                               else "ring A->B->C->A")),
                     actors=_actors, dep=_dep, fam=fam, cache=cache, st=st,
                     rat=rat, kinds=kinds, okinds=okinds, defs=defs,
                     half=half, closed=closed, filt=_filt,
                     nonunit=Counter({k: v for k, v in rat.items()
                                      if k != 1}))
    report(f"{ARMS[_nm]['label']} census",
           f"{dict(st)}; non-unit {len(defs)}; spectrum "
           f"{fmt(ARMS[_nm]['nonunit'])}; kinds {fmtk(kinds)}")

_asym_carry = {}
for _nm in ("ASYM1", "ASYM2"):
    rows_m, of_m = reversal_census(ARMS[_nm], opp_filt="mirror")
    rows_s, of_s = reversal_census(ARMS[_nm], opp_filt="same")
    ROWS[_nm] = rows_m
    print()
    print(f"  --- {ARMS[_nm]['label']}, reversed into the MIRROR "
          f"sub-grammar ---")
    _c, _cc, _carry = census_tables(ARMS[_nm]["label"] + " [mirror]", rows_m)
    _asym_carry[_nm] = _cc
    _cs = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in rows_s
                  if v != 1)
    report(f"{ARMS[_nm]['label']} second reading — reversed into the arm's "
           f"OWN (unmirrored) sub-grammar, holonomy-carrying loops only",
           fmtk(_cs))

_asym_all = [row for _nm in ("ASYM1", "ASYM2") for row in ROWS[_nm]
             if row[3] != 1]
_asym_cls = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in _asym_all)
check("D.1 THE DEFECTED SCHEDULES GIVE THE SAME ANSWER, AND THE "
      "HAND-BUILT SYMMETRY OF THE ANCHOR ARMS WAS THEREFORE NOT MASKING "
      "ANYTHING.  On both committed defected families — the one-way link "
      "and the directed ring, each reversed into its own MIRROR "
      "sub-grammar, which is the categorical opposite of the schedule and "
      "not a rigged test — every holonomy-carrying loop again has NO "
      "reversed counterpart.  The count is larger than the anchor "
      "window's by a factor of several and the answer does not move",
      _asym_cls["UNDEFINED"] == len(_asym_all) and len(_asym_all) > 0,
      f"holonomy-carrying loops {len(_asym_all)} over the two defected "
      f"families; classification {fmtk(_asym_cls)}")

_asym_flat_def = [row for _nm in ("ASYM1", "ASYM2") for row in ROWS[_nm]
                  if row[3] == 1 and row[4] is not None]
check("D.2 THE DEFECTED ARMS ARE NOT VACUOUS UNDER R: their flat loops DO "
      "acquire priced reversed counterparts, in quantity, so the "
      "negative at the holonomy-carrying loops is a real refusal and not "
      "an empty support.  (The mirror FILTER itself cannot bite on an "
      "image of an arm record: of(e) = f(rho(e)) and every reversed "
      "event is rho(e_fwd) with f(e_fwd) true, so by A.1 involutivity "
      "of passes identically; the mirror column is therefore a reading "
      "of the unrestricted grammar, and D.2's honest content is that "
      "the refusal is the LAW's, not the filter's)",
      len(_asym_flat_def) > 0
      and all(row[4] == 1 for row in _asym_flat_def),
      f"{len(_asym_flat_def)} flat loops of the defected arms have a "
      f"priced reversed counterpart in the mirror sub-grammar, all at "
      f"v_rev = 1")

_arbt4 = arb_table(("AB4", "ABC3", "ASYM1", "ASYM2"))
report("the obstruction, cross-tabulated over ALL FOUR ARMS: (record "
       "carries an arbitration) x (its image is priced)",
       {f"arb={k[0]}, priced={k[1]}": v
        for k, v in sorted(_arbt4.items(), key=str)})
_carry_arb4 = Counter()
for _nm in ("AB4", "ABC3", "ASYM1", "ASYM2"):
    for h, eA, eB, v, vr, *_ in ROWS[_nm]:
        if v != 1:
            _carry_arb4[any(e[0] == 'r' for e in tuple(h) + (eA, eB))] += 1
check("D.3 THE EXACT CHARACTERIZATION SURVIVES THE DEFECTED SCHEDULES.  "
      "Over all four arms — 17,277 closed squares, including the two "
      "defected families reversed into their mirror sub-grammars — a "
      "closed square's reversed counterpart is priced if and only if its "
      "record carries no arbitration event, with no exception in either "
      "direction; and every holonomy-carrying loop of every arm carries "
      "one.  Breaking the schedule's symmetry does not move the "
      "characterization by a single square",
      _arbt4[(True, True)] == 0 and _arbt4[(False, False)] == 0
      and _carry_arb4[False] == 0
      and _arbt4[(True, False)] > 0 and _arbt4[(False, True)] > 0,
      f"arb-carrying and priced {_arbt4[(True, True)]}; arb-free and "
      f"refused {_arbt4[(False, False)]}; arb-carrying and refused "
      f"{_arbt4[(True, False)]}; arb-free and priced "
      f"{_arbt4[(False, True)]}; curved loops without an arbitration "
      f"{_carry_arb4[False]} of {sum(_carry_arb4.values())}")

_ALPHA4 = set()
for _nm in ("AB4", "ABC3", "ASYM1", "ASYM2"):
    _ALPHA4 |= alphabet_of(ARMS[_nm])
    for h, eA, eB, v in ARMS[_nm]["closed"]:
        _ALPHA4.update(tuple(h) + (eA, eB))
    for h, eA, eB, side in ARMS[_nm]["half"]:
        _ALPHA4.update(tuple(h) + (eA, eB))
report("the realised event alphabet over all four arms (every event of "
       "every censused square, base and exchanged pair alike)",
       f"{len(_ALPHA4)} distinct events; kinds "
       f"{fmtk(Counter(e[0] for e in _ALPHA4))}")
check("D.4 SCOPE LIMIT, DECLARED: THE MERGE KIND IS NOT REACHED.  No "
      "merge event is realised at any depth run here, so this census says "
      "nothing whatever about how R treats merges.  The relabelling table "
      "assigns 'm' a self-dual label and C.3's state-action reading "
      "places it among the producing kinds, but neither is tested by a "
      "single square in this receipt.  Any extension of the verdict to "
      "the merge sector would need a window that reaches one",
      'm' not in {e[0] for e in _ALPHA4},
      f"kinds realised: {sorted({e[0] for e in _ALPHA4})}; merge events "
      f"realised: {sum(1 for e in _ALPHA4 if e[0] == 'm')}")

report("SEC 5 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 6.  DETERMINISM
# ===========================================================================

print()
print("-" * 78)
print("SEC 6  DETERMINISM PROBE")
print("-" * 78)
_t = time.time()
_det_a = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in ROWS["AB4"])
_rows2, _ = reversal_census(ARMS["AB4"])
_det_b = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_
                 in sorted(_rows2, key=lambda z: sk((z[0], z[1], z[2]))))
_hashes = (tuple(sorted((str(v), str(vr)) for _h, _a, _b, v, vr, *_
                        in ROWS["AB4"])),
           tuple(sorted((str(v), str(vr)) for _h, _a, _b, v, vr, *_
                        in _rows2)))
check("DET.1 THE CENSUS IS DETERMINISTIC: recomputed from scratch and "
      "re-sorted by the hash-seed-independent stable key, the AB4 "
      "classification and the full sorted multiset of (v, v_rev) pairs "
      "are identical",
      _det_a == _det_b and _hashes[0] == _hashes[1],
      f"classification {fmtk(_det_a)}; {len(_hashes[0])} (v, v_rev) pairs "
      f"identical under re-sort")
report("SEC 6 block time", f"{time.time() - _t:.0f}s")


# ===========================================================================
# SEC 7.  THE VERDICT
# ===========================================================================

print()
print("=" * 78)
print("SEC 7  THE VERDICT, AGAINST THE PIN'S PRE-REGISTERED OUTCOMES")
print("=" * 78)

ALL_CARRY = [row for _nm in ("AB4", "ABC3", "ASYM1", "ASYM2")
             for row in ROWS[_nm] if row[3] != 1]
ALL_FLAT = [row for _nm in ("AB4", "ABC3", "ASYM1", "ASYM2")
            for row in ROWS[_nm] if row[3] == 1]
FINAL = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in ALL_CARRY)
FINAL_FLAT = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in ALL_FLAT)

print()
print("  THE CENSUS, FINAL, BOTH WAYS.")
print(f"    holonomy-carrying loops (v != 1), all four arms: "
      f"{len(ALL_CARRY)}")
print(f"      {fmtk(FINAL)}")
print(f"    flat loops (v = 1), all four arms: {len(ALL_FLAT)}")
print(f"      {fmtk(FINAL_FLAT)}")
print(f"    the Born = K1 arbitration row: UNDEFINED (B.4)")
print(f"    the 40 committed half-open squares: no priced image (B.3)")
print()
_perarm = {}
for _nm in ("AB4", "ABC3", "ASYM1", "ASYM2"):
    c = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in ROWS[_nm]
                if v != 1)
    f = Counter(classify(v, vr) for _h, _a, _b, v, vr, *_ in ROWS[_nm]
                if v == 1)
    _perarm[_nm] = (c, f)
    print(f"    {ARMS[_nm]['label']:<44} carrying {fmtk(c)}")
    print(f"    {'':<44} flat     {fmtk(f)}")

INVERSION = FINAL["INVERSION"]
INVARIANT = FINAL["INVARIANT"]
OTHER = FINAL["OTHER"] + FINAL_FLAT["OTHER"]
UNDEF = FINAL["UNDEFINED"]

print()
print("  AGAINST THE THREE PRE-REGISTERED OUTCOMES.")
print(f"    LD-CLOSED  requires: everything inverts.  INVERSION on "
      f"holonomy-carrying loops = {INVERSION} of {len(ALL_CARRY)}.  NOT MET.")
print(f"    LD-OPEN    requires: a non-inverting quantity, i.e. an OTHER "
      f"entry.  OTHER = {OTHER}.  NOT MET.")
print(f"    LD-BROKEN  requires: the reversal functor cannot be defined "
      f"involutively")
print(f"               ON THE COMMITTED GRAMMAR.  It is involutive on "
      f"RECORDS (A.3,")
print(f"               {_inv_ok}/{_inv_tot}) and is exactly poset reversal "
      f"(A.4, {_pos_ok}/{_pos_tot}),")
print(f"               but it is not an endofunctor of the committed "
      f"record category:")
print(f"               its image leaves the grammar's support on "
      f"{UNDEF} of {len(ALL_CARRY)} holonomy-")
print(f"               carrying loops, on the Born = K1 row, and on all "
      f"40 half-open")
print(f"               squares.  MET.")

VERDICT = ("LD-BROKEN" if (INVERSION == 0 and OTHER == 0 and UNDEF > 0)
           else ("LD-OPEN" if OTHER > 0
                 else ("LD-CLOSED" if INVERSION == len(ALL_CARRY)
                       else "INDETERMINATE")))
print()
print(f"  VERDICT: {VERDICT}")
print()
print("""  WHAT IT SAYS, STATED WITH ITS SCOPE.  The record category of the
  committed transport grammar is NOT SELF-DUAL.  The opposite category
  exists — every category has one — and the reversal that realises it on
  records is a clean involution which is exactly poset reversal.  What
  fails is realisation: the committed law does not price the opposite
  record.  It fails on the whole curvature.  Every one of the loops that
  carries the transport holonomy, in every arm run here including both
  defected schedules, has its reversed counterpart refused at admission,
  and so does the Born = K1 arbitration row.  The obstruction is
  consumption-before-production (C.2, exact), and it cannot be repaired
  by relabelling because the committed alphabet contains four producing
  kinds and no annihilating kind (C.3, B.6).

  AND IT HAS A ONE-KIND ADDRESS.  Over all four arms a closed square's
  reversed counterpart is priced IF AND ONLY IF its record carries no
  arbitration event (C.3a, D.3, exact in both directions, no exception),
  and every holonomy-carrying loop carries one (C.3b, D.3).  The
  arbitration is the one committed kind whose admission reads a JOINT
  object — the live-proposal component with its incomparability edges —
  rather than a single held version.  So the wall across the last door
  and the source of the transport curvature are at the same address, and
  it is the address the corpus already calls the join.

  WHAT IT DOES NOT SAY.  It does not say the holonomy fails to invert:
  nothing was measured to invert or not to invert, because there is no
  second value to compare against.  The 0-for-5 phase record is NOT
  advanced to 0-for-6 by this unit — the last door is neither shut nor
  opened, it is walled.  It does not say records run backwards, or that
  anything is irreversible in any dynamical or thermodynamic sense; the
  reversal here is FORMAL and category-level throughout, and no such
  language appears in this receipt.  It does not claim the negative
  survives greater depth or wider pools: it is [MEASURED] on four arms at
  the stated caps.""")

print()
print("-" * 78)
print("DECLARED CAPS")
print("-" * 78)
print(f"  arms: {ARMS['AB4']['label']}; {ARMS['ABC3']['label']}; "
      f"{ARMS['ASYM1']['label']}; {ARMS['ASYM2']['label']}")
print(f"  closed squares censused: "
      f"{sum(len(ROWS[n]) for n in ('AB4', 'ABC3', 'ASYM1', 'ASYM2'))}")
print(f"  holonomy-carrying loops censused: {len(ALL_CARRY)}")
print(f"  relabelling control: {len(_relab_inv)} involutive relabellings "
      f"(the gate) plus {len(_relab_non)} non-involutive (reported only), "
      f"over the two anchor arms")
print(f"  all-linear-extensions control: anchor arms only, {_le_seq} "
      f"endpoints, {_le_tot} extensions")
print(f"  non-empty-prefix control: anchor arms only, prefixes of length "
      f"<= 2 (up to {_pref_n} per arm)")
print("  transport scope; committed families only; weight-system level; "
      "no measure claim")
print("  exact Fractions end to end; no float enters any gate or any "
      "printed quantity except wall-clock timings")

print()
print("-" * 78)
print(f"GATES: {PASS} pass, {FAIL} fail  "
      f"(of which {len(COROLLARY)} carry no independent information)")
for a, b in COROLLARY:
    print(f"    corollary: {a} <- {b}")
print(f"ANCHOR FAILURES: {ANCHOR_FAIL}")
print(f"VERDICT: {VERDICT}")
print(f"RUNTIME: {time.time() - T0:.0f}s")
print("-" * 78)

sys.exit(1 if ANCHOR_FAIL else 0)
