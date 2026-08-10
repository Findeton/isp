#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 R4 -- THE QFT RUNG: THE DEFECT ON THE STAGE.  Instrument for
`v14/paper-10-defect-on-the-stage.md`.

QUESTION (pin section 2): does a spatially structured indivisible family on
the record stage exhibit a nonzero composition defect, and does the defect
carry excitation structure?

CLI CONTRACT (the #82 minimum: argv-parsed, unknown flags rejected)
------------------------------------------------------------------
    python3.13 v14/code/r4_defect_stage_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (including the paper-claim gate), runs every
        declared mutant in-process, runs the computed compliance sweep,
        WRITES `r4_defect_stage_output.txt` and `r4_defect_stage_receipt.json`
        beside this file, and exits 0 if every gate passes, 1 otherwise.

    python3.13 v14/code/r4_defect_stage_exact.py --no-write
        The same run without writing artifacts.

    python3.13 v14/code/r4_defect_stage_exact.py --selftest
        FALSIFICATION SELF-TEST.  Corrupts one anchor's expected digest IN
        MEMORY, confirms that the run dies at the anchor gate, and exits 1.
        WRITES NOTHING.  Exits 2 if the corrupted run does NOT die.

    python3.13 v14/code/r4_defect_stage_exact.py --mutant NAME
        Runs the pipeline with the named mutant active.  Exits 1 when the
        mutant is killed by a gate (the intended outcome), 0 if it survives.
        An unknown NAME exits 2; it never reports "SURVIVED".

    python3.13 v14/code/r4_defect_stage_exact.py --break-anchor NAME
        Corrupts the named anchor's expected value.  NAME is validated
        against SOURCES; an unknown NAME exits 2.  The run must exit 1.

    python3.13 v14/code/r4_defect_stage_exact.py --verify-paper [PATH]
        Reports the paper-claim rendering and coverage against PATH (the
        unit's own paper by default).  The same check runs as a GATE inside
        the delivery run, so this flag is a report, not the enforcement.

    Any other argument, and any missing flag argument, exits 2 with a
    message.  No flag is mutant-only.

ARITHMETIC.  Exact only.  The field is Q(zeta_8) carried as integer
coefficient 4-tuples over a positive integer denominator, reduced modulo
Phi_8(x) = x^4 + 1; the representation is canonical, so tuple equality IS
field equality.  There are no floats anywhere in a substantive path; an AST
scan of this file and a recursive type scan of the emitted receipt are gates.

REIMPLEMENTATION NOTICE.  Every object here is reimplemented from the
definitions in the pinned sources.  Nothing is imported from any other unit.

RUNTIME INPUTS (RUNBOOK 14, engraving #46).  Exactly five files are read at
run time as SOURCES, all hash-pinned by this unit's frozen declaration, plus
exactly one file read as the OBJECT UNDER TEST -- this unit's own paper,
which cannot be hash-pinned because it is the thing being verified.  Both
lists are enumerated and gated; nothing else, and no mutable repository
state, is read.  Everything else is this unit's own frozen declaration, in
section 0 below.
"""

import ast
import hashlib
import json
import os
import re
import sys
from itertools import product
from math import gcd

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SELF = os.path.abspath(__file__)
OUT_TXT = os.path.join(os.path.dirname(SELF), "r4_defect_stage_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "r4_defect_stage_receipt.json")

SCHEMA = "isp/v14/r4-defect-on-the-stage/1"

# The unit's own paper: read at run time as the OBJECT UNDER TEST, never as a
# source.  It is not hash-pinned, and cannot be: a claim gate that compared the
# paper against a digest frozen from the same paper would be the #219 shape.
PAPER_REL = "v14/paper-10-defect-on-the-stage.md"

# --- the five hash-pinned runtime inputs -----------------------------------
SOURCES = [
    ("A-SEED-PAPER1", "v12/paper1-composition-defect.md", "81bdab5673fb",
     "THE SEED: the composition defect, the indivisible-family framework, "
     "the defect algebra.  Reference-only; every object is reimplemented."),
    ("A-SEED-EXACT", "v12/paper1_code/exact.py", "8e90f6435922",
     "the exact-field recipes (cyclotomic tuples, canonical reduction)."),
    ("A-STAGE-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "THE STAGE: the record layer's declared site lattice -- dimension, "
     "link set, chart group."),
    ("A-LOCALITY-R2", "v14/code/r2_manifold_receipt.json", "08b2140f46ae",
     "the locality facts, TERMINAL: the criterion this unit ports."),
    ("A-PIN-R4", "v14/note-r4-qft-pin.md", "1582cea5df51",
     "this unit's pin, frozen at v14 ledger #47."),
]

# --- path-value anchors: (id, source-id, json path, expected value) ---------
PATH_VALUE_ANCHORS = [
    ("PV-I7-D", "A-STAGE-I7", "declarations/d", 2,
     "the stage's spatial dimension"),
    ("PV-I7-LINKS", "A-STAGE-I7", "declarations/links_d2", [[1, 0], [0, 1], [1, 1]],
     "the stage's declared link set at d=2"),
    ("PV-I7-L", "A-STAGE-I7", "declarations/L", 3,
     "the stage's own lattice size -- this unit measures why it must grow"),
    ("PV-I7-ARITH", "A-STAGE-I7", "arithmetic",
     "fractions.Fraction / integers / exact F_p; no floats",
     "the stage's arithmetic discipline, inherited"),
    ("PV-I7-CHART", "A-STAGE-I7", "declarations/chart_group",
     "the |X| chart translations and the d! direction relabellings, acting on "
     "sites, on the record's link counts, on the lapse profiles and on every "
     "tensor index",
     "the anchored symmetry group of the stage"),
    ("PV-R2-CRIT", "A-LOCALITY-R2", "locality_census/criterion",
     "locality exists at a rule iff SOME connected component of that rule's "
     "overlap graph is NOT complete (the R1 adjudication's criterion, section 6)",
     "the locality criterion this unit ports to the lattice"),
    ("PV-R2-COUNT", "A-LOCALITY-R2", "locality_census/count_locality_B", 14,
     "the terminal locality census size"),
    ("PV-R2-HEAD", "A-LOCALITY-R2", "verdict/head", "R2-LOCALITY-DECLARABLE-AT",
     "the terminal locality verdict head"),
    ("PV-R2-WIDTH", "A-LOCALITY-R2", "width_law/rules_predicted_correctly", 109,
     "the terminal width law's coverage"),
    ("PV-R2-GATES", "A-LOCALITY-R2", "totals/gates", 69,
     "the terminal instrument's gate count"),
]

# --- verbatim-text anchors: context windows bound to consumer gates ---------
# (#34 engraving: evaluated BEFORE byte anchors, each row bound to a named
# consumer gate, context windows rather than fragments.)
VERBATIM_ANCHORS = [
    ("VB-WITNESS-2X2", "A-SEED-PAPER1", "G-DEFECT-DEFINITION",
     "both of which are fully unbiased. For these,\n$$\n"
     "\\Delta^{B}(H,V)=0,\n\\qquad\n"
     "\\Delta^{B}(H,H)=\\begin{pmatrix}\\tfrac12&-\\tfrac12\\\\[2pt]"
     "-\\tfrac12&\\tfrac12\\end{pmatrix}.\n$$"),
    ("VB-DEFECT-DEF", "A-SEED-PAPER1", "G-DEFECT-DEFINITION-SHAPE",
     "$$\n\\Delta^{B}(U_2,U_1)\\;:=\\;B(U_2U_1)\\;-\\;B(U_2)B(U_1).\n$$\n"
     "This is the failure of the Born shadow of the coherent composite to equal\n"
     "the shadow one obtains by forgetting phases and restarting at the\n"
     "intermediate cut."),
    ("VB-CLOSED-FORM", "A-SEED-PAPER1", "G-DEFECT-CLOSED-FORM",
     "**The defect entry is the total pairwise interference of the\n"
     "path amplitudes through the cut, and nothing else.**"),
    ("VB-GAUGE-II", "A-SEED-PAPER1", "G-GAUGE-SELFTEST",
     "| (ii) | $\\Delta^{B}(DU_2,\\,U_1D')=\\Delta^{B}(U_2,U_1)$ | outer tori |"),
    ("VB-ANNIHILATOR", "A-SEED-PAPER1", "G-MARKOV-ZERO",
     "*Then $\\mathcal{K}_L$ is exactly the row-monomial unitaries and\n"
     "$\\mathcal{K}_R$ exactly the column-monomial unitaries.*"),
    ("VB-DIVISION-EVENT", "A-SEED-PAPER1", "G-DIVISION-EVENTS-DECLARED",
     "Allowed conditioning times $t_0$ are called\n"
     "> **division events** for the given system"),
    ("VB-COHERENCE", "A-SEED-PAPER1", "G-COHERENCE-LAW",
     "*both sides being $B(U_3U_2U_1)-B(U_3)B(U_2)B(U_1)$.*"),
    ("VB-FIELD-CANON", "A-SEED-EXACT", "G-FIELD-CANONICAL",
     "Phi_n is irreducible over Q,\n    so the representation is canonical and "
     "tuple equality IS field equality."),
    ("VB-PIN-VERDICTS", "A-PIN-R4", "G-VERDICT-PREREGISTERED",
     "`R4-DEFECT-PRESENT-<structure: the two-point + class-census\n"
     "qualifiers; the locality dependence; scope>` / `R4-DEFECT-ABSENT-<the\n"
     "Markovian-collapse characterization>` / `R4-BLOCKED-AT-<named fact>`."),
]

# --- the arena, declared as data -------------------------------------------
ARENA = {
    "boundary": "the finite periodic site lattice X = (Z_L)^d with d anchored "
                "at 2 and L measured (section 3); the configuration carrier is "
                "the single-occupation sector, one occupied site per "
                "configuration, so |C| = |X| = L^d",
    "family": "spatially structured indivisible families: unitary generators "
              "whose nonzero entries connect only configurations differing by a "
              "declared offset, built from a declared coefficient alphabet",
    "law": "Barandes' identity Gamma = |Theta| entrywise-squared, with Theta a "
           "unitary representative; the intermediate leg at a non-division cut "
           "is declared to be B(V) (the Born declaration)",
    "state": "the standalone distribution p over configurations; 18 declared "
             "prepared states (16 point masses, uniform, one wedge)",
    "arena": "the anchored chart group (translations and direction "
             "relabellings) and this unit's declared extension by the square "
             "point group; both censused",
    "provenance": "five hash-pinned runtime inputs and nothing else",
    "division_events": "t = 0 and t = 2 are division events; the cut at t = 1 "
                       "is NOT a division event, and Delta^B measures the "
                       "failure of the law of total probability across it",
}

# alphabet: 0 and every zeta_8^t times a modulus in {1, 1/2, 1/sqrt2}
ALPHABET_MODULI = ("1", "1/2", "1/sqrt2")
L_SWEEP = (2, 3, 4, 5, 6, 7, 8, 9)
D_SWEEP = (1, 2, 3)
ORD_SWEEP = (1, 2, 3, 4, 5, 6, 7, 8, 9)
CONNECTIVES = ("MOORE:max-norm<=1", "VON-NEUMANN:sum-norm<=1")
CONNECTIVE_TAGS = ("MAX-NORM", "SUM-NORM")
SCRAMBLE_SWAPS = ((0, 5), (1, 11))
COHERENCE_TRIPLES = 48
DEFECT_VALUE_CENSUS_ROWS = 12
STATE_PROBE_PAIRS = 8
FIVE_POINT_SIZES = (4, 5, 6, 7)
MOORE_BALL_LEMMA_SIZES = (5, 6, 7, 8, 9)

# transport levels, low to high (the realization census of pin step 5)
LEVELS = ("NONE", "OCC", "OCC+AXIS", "FULL")

# ===========================================================================
# SECTION 1.  THE EXACT FIELD Q(zeta_8)
# ===========================================================================

def cnorm(n0, n1, n2, n3, d):
    if d < 0:
        n0, n1, n2, n3, d = -n0, -n1, -n2, -n3, -d
    g = gcd(gcd(abs(n0), abs(n1)), gcd(abs(n2), abs(n3)))
    g = gcd(g, d)
    if g > 1:
        return (n0 // g, n1 // g, n2 // g, n3 // g, d // g)
    return (n0, n1, n2, n3, d)


ZERO = (0, 0, 0, 0, 1)
ONE = (1, 0, 0, 0, 1)


def cadd(a, b):
    da, db = a[4], b[4]
    l = da // gcd(da, db) * db
    fa, fb = l // da, l // db
    return cnorm(a[0] * fa + b[0] * fb, a[1] * fa + b[1] * fb,
                 a[2] * fa + b[2] * fb, a[3] * fa + b[3] * fb, l)


def cneg(a):
    return (-a[0], -a[1], -a[2], -a[3], a[4])


def csub(a, b):
    return cadd(a, cneg(b))


MULCACHE = {}
CACHE_STATS = {"hits": 0, "misses": 0}


def cmul(a, b):
    key = (a, b)
    got = MULCACHE.get(key)
    if got is not None:
        CACHE_STATS["hits"] += 1
        return got
    CACHE_STATS["misses"] += 1
    a0, a1, a2, a3, da = a
    b0, b1, b2, b3, db = b
    r = cnorm(a0 * b0 - (a1 * b3 + a2 * b2 + a3 * b1),
              a0 * b1 + a1 * b0 - (a2 * b3 + a3 * b2),
              a0 * b2 + a1 * b1 + a2 * b0 - a3 * b3,
              a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0, da * db)
    MULCACHE[key] = r
    return r


def cmul_fresh(a, b):
    """cache-bypassing product: self-test phases must evaluate fresh (#185)."""
    a0, a1, a2, a3, da = a
    b0, b1, b2, b3, db = b
    return cnorm(a0 * b0 - (a1 * b3 + a2 * b2 + a3 * b1),
                 a0 * b1 + a1 * b0 - (a2 * b3 + a3 * b2),
                 a0 * b2 + a1 * b1 + a2 * b0 - a3 * b3,
                 a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0, da * db)


def cconj(a):
    """complex conjugation zeta -> zeta^{-1} = -zeta^3."""
    return cnorm(a[0], -a[3], -a[2], -a[1], a[4])


def cnormsq(a):
    return cmul(a, cconj(a))


def cscal(a, num, den=1):
    return cnorm(a[0] * num, a[1] * num, a[2] * num, a[3] * num, a[4] * den)


def zpow(t):
    t %= 8
    v = [0, 0, 0, 0]
    if t < 4:
        v[t] = 1
    else:
        v[t - 4] = -1
    return (v[0], v[1], v[2], v[3], 1)


def crat(num, den=1):
    return cnorm(num, 0, 0, 0, den)


def cstr(a):
    parts = []
    names = ("1", "z", "z2", "z3")
    for i in range(4):
        if a[i]:
            parts.append("%+d%s" % (a[i], "" if i == 0 else "*" + names[i]))
    body = "".join(parts) if parts else "0"
    return body if a[4] == 1 else "(%s)/%d" % (body, a[4])


def crational(a):
    """the Fraction value as a string when the element is rational, else None."""
    if a[1] or a[2] or a[3]:
        return None
    return "%d" % a[0] if a[4] == 1 else "%d/%d" % (a[0], a[4])


SQ2 = (0, 1, 0, -1, 1)
INV_SQ2 = (0, 1, 0, -1, 2)


def build_alphabet():
    out, seen = [], set()
    for e in [ZERO]:
        out.append(e)
        seen.add(e)
    for t in range(8):
        z = zpow(t)
        for m in ALPHABET_MODULI:
            if m == "1":
                e = z
            elif m == "1/2":
                e = cscal(z, 1, 2)
            else:
                e = cmul(z, INV_SQ2)
            if e not in seen:
                seen.add(e)
                out.append(e)
    return out


# ===========================================================================
# SECTION 2.  SPARSE MATRICES OVER THE FIELD
# ===========================================================================

def mat_mul(A, B, n):
    byrow = {}
    for (i, k), v in A.items():
        byrow.setdefault(k, []).append((i, v))
    out = {}
    for (k, j), u in B.items():
        lst = byrow.get(k)
        if not lst:
            continue
        for i, v in lst:
            key = (i, j)
            w = cmul(v, u)
            cur = out.get(key)
            out[key] = w if cur is None else cadd(cur, w)
    return {k: v for k, v in out.items() if v != ZERO}


def mat_dag(A):
    return {(j, i): cconj(v) for (i, j), v in A.items()}


def mat_born(A):
    return {k: cnormsq(v) for k, v in A.items() if v != ZERO}


def mat_sub(A, B):
    out = dict(A)
    for k, v in B.items():
        out[k] = csub(out.get(k, ZERO), v)
    return {k: v for k, v in out.items() if v != ZERO}


def mat_id(n):
    return {(i, i): ONE for i in range(n)}


def mat_is_unitary(A, n):
    return mat_mul(mat_dag(A), A, n) == mat_id(n)


def is_scalar(A, n):
    """A = lambda * I for some field element lambda."""
    if len(A) != n:
        return False
    lam = A.get((0, 0))
    if lam is None:
        return False
    return all(A.get((i, i)) == lam for i in range(n))


# ===========================================================================
# SECTION 3.  THE STAGE
# ===========================================================================

def torus_absmax(v, L):
    return max(min(x % L, (-x) % L) for x in v)


def torus_abssum(v, L):
    return sum(min(x % L, (-x) % L) for x in v)


def lattice_locality(L, d, connective):
    """port of the anchored criterion: locality exists iff the adjacency graph
    has a connected component that is NOT complete."""
    offs = [v for v in product(range(L), repeat=d) if any(v)]
    if connective == CONNECTIVES[0]:
        nbr = [v for v in offs if torus_absmax(v, L) <= 1]
    else:
        nbr = [v for v in offs if torus_abssum(v, L) <= 1]
    complete = (len(nbr) == len(offs))
    return {"offsets": len(offs), "neighbours": len(nbr),
            "complete": complete, "locality": (not complete)}


def elt_order(a, L):
    k = 1
    while any((k * x) % L for x in a):
        k += 1
    return k


# ===========================================================================
# SECTION 4.  THE FAMILY: unitary axis circulants, by the autocorrelation law
# ===========================================================================
# A generator is a coefficient map c on offsets; the matrix is M[x+v, x] = c[v].
# U is unitary iff the periodic autocorrelation A(m) = sum_v c_v conj(c_{v+m})
# equals delta_{m,0}.  (Proof in the paper; independently checked here against
# U^dagger U = I and against |Fourier|^2 = 1.)

def coef_autocorr_unitary(c, sites, addv):
    for m in sites:
        acc = ZERO
        for v, cv in c.items():
            cw = c.get(addv(v, m))
            if cw is None:
                continue
            acc = cadd(acc, cmul(cv, cconj(cw)))
        if acc != (ONE if not any(m) else ZERO):
            return False
    return True


def ring_autocorr_unitary(c, n):
    """the same criterion on the cyclic group Z_n (used by the ord sweep)."""
    for m in range(n):
        acc = ZERO
        for v, cv in c.items():
            cw = c.get((v + m) % n)
            if cw is None:
                continue
            acc = cadd(acc, cmul(cv, cconj(cw)))
        if acc != (ONE if m == 0 else ZERO):
            return False
    return True


_ORD_MEMO = {}
_FIVE_MEMO = {}
_AXIS_MEMO = {}


def _copy_census(d):
    return {k: dict(v) for k, v in d.items()}


def ord_sweep(alphabet, ords):
    """exhaustive sweep of the declared 3-term axis stencil {0, a, -a} over the
    declared alphabet, indexed by n = ord(a).  Returns per-ord censuses.

    Memoised on (alphabet, ords): the function is pure, and the mutant harness
    re-enters the pipeline once per declared mutant.  Callers receive a fresh
    copy, so no caller can poison the cache."""
    memo_key = (tuple(alphabet), tuple(ords))
    if memo_key in _ORD_MEMO:
        return _copy_census(_ORD_MEMO[memo_key])
    res = {}
    for n in ords:
        gens, seen = [], set()
        triples = 0
        for c0, c1, cm in product(alphabet, repeat=3):
            triples += 1
            c = {}
            for o, v in ((0 % n, c0), (1 % n, c1), ((-1) % n, cm)):
                c[o] = cadd(c.get(o, ZERO), v)
            c = {o: v for o, v in c.items() if v != ZERO}
            key = tuple(sorted(c.items()))
            if key in seen:
                continue
            seen.add(key)
            if ring_autocorr_unitary(c, n):
                gens.append(key)
        mono = [g for g in gens if len(g) <= 1]
        res[n] = {"triples_swept": triples, "distinct_generators": len(gens),
                  "monomial": len(mono), "non_monomial": len(gens) - len(mono)}
    _ORD_MEMO[memo_key] = res
    return _copy_census(res)


def five_point_collapse(alphabet, L, ordering="AXIS-FIRST"):
    """declared extension: the 5-point (von Neumann) stencil on (Z_L)^2, swept
    exhaustively with autocorrelation pruning.  A lag is EVALUABLE once every
    offset pair contributing to it has been assigned; evaluable lags must
    already vanish, which prunes the tree at depth two.

    `ordering` NAMES the offset order the search visits, because the node count
    is an artifact of that order and only the leaf count and the solution count
    are invariants of the sweep.  Both declared orderings are run and the
    invariants are compared."""
    memo_key = (tuple(alphabet), L, ordering)
    if memo_key in _FIVE_MEMO:
        return dict(_FIVE_MEMO[memo_key])
    if ordering == "AXIS-FIRST":
        offs = [(1, 0), (L - 1, 0), (0, 1), (0, L - 1), (0, 0)]
    else:
        offs = [(0, 0), (0, 1), (1, 0), (0, L - 1), (L - 1, 0)]

    def addv(a, b):
        return ((a[0] + b[0]) % L, (a[1] + b[1]) % L)

    lags = []
    for m in product(range(L), repeat=2):
        if not any(m):
            continue
        pairs = [(v, addv(v, m)) for v in offs if addv(v, m) in offs]
        if pairs:
            lags.append((m, pairs))
    found_non_monomial, total, nodes = 0, 0, 0

    def rec(i, c):
        nonlocal found_non_monomial, total, nodes
        if i == len(offs):
            total += 1
            cc = {o: v for o, v in c.items() if v != ZERO}
            if coef_autocorr_unitary(cc, list(product(range(L), repeat=2)), addv):
                if len(cc) > 1:
                    found_non_monomial += 1
            return
        assigned = set(offs[:i + 1])
        ready = [(m, ps) for m, ps in lags
                 if all(a in assigned and b in assigned for a, b in ps)]
        for a in alphabet:
            c[offs[i]] = a
            nodes += 1
            ok = True
            for m, ps in ready:
                acc = ZERO
                for v, w in ps:
                    acc = cadd(acc, cmul(c[v], cconj(c[w])))
                if acc != ZERO:
                    ok = False
                    break
            if ok:
                rec(i + 1, c)
            del c[offs[i]]

    rec(0, {})
    out = {"L": L, "stencil": 5, "ordering": ordering, "nodes_visited": nodes,
           "leaves_reached": total, "non_monomial": found_non_monomial}
    _FIVE_MEMO[memo_key] = out
    return dict(out)


# --- THE MOORE-BALL COLLAPSE THEOREM, machine-checked where it is checkable --
# THEOREM (Moore-ball collapse).  Let L >= 5 and let U be a unitary generator on
# (Z_L)^2 whose coefficient map is supported inside the radius-1 Chebyshev ball
# {-1,0,1}^2.  Then U is monomial.  Over ANY field closed under conjugation.
#
# The proof runs on three legs, and the first two are exhaustively checkable at
# finite cost; the third is this unit's own order-collapse census.
#
#   LEG 1 (the lag structure).  For L >= 5 there is no wraparound inside the
#   ball, so the lag (2, t) receives contributions from exactly the pairs
#   ((-1, j), (1, j + t)) -- column -1 against column +1 and nothing else; and
#   inside a single column the lag (0, 2) receives exactly one pair.  Measured
#   here by exhaustive enumeration of the ball's pair set at every declared L.
#
#   LEG 2 (the domain).  The vanishing of the whole cross-correlation of the two
#   length-3 column sequences X, Z is the identity X(x) * Ztilde(x) = 0 in the
#   Laurent polynomial ring over the field.  The ring is a domain because the
#   field is: the product's extreme coefficient is the product of the extreme
#   coefficients.  Measured here on every ordered pair of nonzero alphabet
#   elements.
#
#   LEG 3 (the single column).  Once the support lies in one column, the lags
#   (0, t) are the aperiodic autocorrelation of a length-3 sequence, and the
#   unit's own order census at ord >= 5 shows exhaustively that delta
#   autocorrelation forces support <= 1.

def moore_ball_lag_structure(L):
    """LEG 1, measured: the ball's pair sets at the extreme lags."""
    ball = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]

    def sub(a, b):
        return (a[0] - b[0], a[1] - b[1])
    cross_ok, single_ok = True, True
    cross_rows = []
    for t in (-2, -1, 0, 1, 2):
        m = (2, t)
        pairs = [(v, w) for v in ball for w in ball if sub(w, v) == m]
        want = [((-1, j), (1, j + t)) for j in (-1, 0, 1) if -1 <= j + t <= 1]
        if sorted(pairs) != sorted(want):
            cross_ok = False
        cross_rows.append({"lag": list(m), "pairs": len(pairs)})
    col = [(0, j) for j in (-1, 0, 1)]
    single = [(v, w) for v in col for w in col if sub(w, v) == (0, 2)]
    if single != [((0, -1), (0, 1))]:
        single_ok = False
    # no wraparound inside the ball at this L: every difference of ball offsets
    # is realised uniquely on the torus
    wrap_ok = len({((w[0] - v[0]) % L, (w[1] - v[1]) % L) for v in ball for w in ball}) \
        == len({(w[0] - v[0], w[1] - v[1]) for v in ball for w in ball})
    return {"L": L, "cross_lag_structure_ok": cross_ok,
            "single_column_lag_ok": single_ok, "no_wraparound": wrap_ok,
            "cross_lags": cross_rows}


def field_is_a_domain(alphabet):
    """LEG 2, measured: no two nonzero alphabet elements multiply to zero, and
    the extreme coefficient of a Laurent product is the product of the extreme
    coefficients (checked on every ordered pair)."""
    nz = [a for a in alphabet if a != ZERO]
    bad = 0
    for a in nz:
        for b in nz:
            if cmul(a, cconj(b)) == ZERO:
                bad += 1
    return {"nonzero_elements": len(nz), "zero_divisor_pairs": bad}


# ===========================================================================
# SECTION 5.  THE COMPOSITION DEFECT
# ===========================================================================
# Reimplemented from the anchored definition VB-DEFECT-DEF:
#     Delta^B(U2, U1) := B(U2 U1) - B(U2) B(U1),      B(U) = |U| entrywise^2.

def canon_key_matrix(M):
    """the gauge-canonical key of a MATRIX: the lexicographic minimum of the
    entry set over the declared global-phase orbit.  Written for the
    per-generator transport verification, and sharing no helper with the
    classifier's coefficient-map route."""
    best = None
    for t in range(8):
        z = zpow(t)
        cand = tuple(sorted(((i, j), cmul(z, v)) for (i, j), v in M.items()))
        if best is None or cand < best:
            best = cand
    return best


def defect_dense(V, U, n):
    """route DENSE: the definition, on sparse matrices."""
    return mat_sub(mat_born(mat_mul(V, U, n)), mat_mul(mat_born(V), mat_born(U), n))


def defect_conv(v, u, sites, subv):
    """route CONV: circulant coefficient convolution, separation-indexed."""
    out = {}
    for s in sites:
        tot, inc = ZERO, ZERO
        hit = False
        for t, vt in v.items():
            us = u.get(subv(s, t))
            if us is None:
                continue
            hit = True
            w = cmul(vt, us)
            tot = cadd(tot, w)
            inc = cadd(inc, cnormsq(w))
        if not hit:
            continue
        dv = csub(cnormsq(tot), inc)
        if dv != ZERO:
            out[s] = dv
    return out


def defect_crossterms(v, u, sites, subv):
    """route XT: the closed form 2 * sum_{k<l} Re(w_k conj(w_l)).  Algebraically
    identical to the definition (anchored VB-CLOSED-FORM), so it is registered
    as a FORCED implementation cross-check, not an independent route."""
    out = {}
    for s in sites:
        ws = []
        for t, vt in v.items():
            us = u.get(subv(s, t))
            if us is None:
                continue
            ws.append(cmul(vt, us))
        if not ws:
            continue
        acc = ZERO
        for i in range(len(ws)):
            for j in range(i + 1, len(ws)):
                z = cmul(ws[i], cconj(ws[j]))
                acc = cadd(acc, cadd(z, cconj(z)))
        if acc != ZERO:
            out[s] = acc
    return out


def fourier_product_coefs(v, u, L, d):
    """route FT: multiply in the character basis and transform back.  omega =
    zeta_8^2 = i is the L=4 character; only used where mu_L is in Q(zeta_8)."""
    ks = list(product(range(L), repeat=d))
    def chi(k, x):
        return zpow((2 * sum(a * b for a, b in zip(k, x))) % 8)
    vh, uh = {}, {}
    for k in ks:
        av, au = ZERO, ZERO
        for o, c in v.items():
            av = cadd(av, cmul(c, chi(k, o)))
        for o, c in u.items():
            au = cadd(au, cmul(c, chi(k, o)))
        vh[k], uh[k] = av, au
    out = {}
    N = L ** d
    for m in ks:
        acc = ZERO
        for k in ks:
            acc = cadd(acc, cmul(cmul(vh[k], uh[k]), cconj(chi(k, m))))
        acc = cscal(acc, 1, N)
        if acc != ZERO:
            out[m] = acc
    return out


# ===========================================================================
# SECTION 6.  GATE / MUTANT / ANCHOR MACHINERY
# ===========================================================================

class GateFail(Exception):
    pass


MUT = None
QUIET = False
LOG = []


def say(msg=""):
    if QUIET:
        return
    LOG.append(msg)
    print(msg, flush=True)


def mut(name):
    return MUT == name


class Ledger:
    def __init__(self):
        self.rows = []
        self.evaluated = []

    def gate(self, gid, claim, ok, detail="", kind="MEASURED"):
        self.evaluated.append(gid)
        self.rows.append({"id": gid, "claim": claim, "kind": kind,
                          "detail": str(detail), "passed": bool(ok)})
        if not ok:
            raise GateFail("%s :: %s :: %s" % (gid, claim, detail))
        return True


# The frozen gate registry (this unit's own declaration).  G-EVERY-GATE-
# EVALUATED compares the evaluated list against it; a gate no path evaluates is
# dead code and may not appear as waived (#34).
GATE_REGISTRY = [
    "G-VERBATIM-ANCHORS", "G-BYTE-ANCHORS", "G-PATH-VALUE-ANCHORS",
    "G-DEFECT-DEFINITION-SHAPE",
    "G-NO-UNANCHORED-RUNTIME-INPUT",
    "G-FIELD-CANONICAL", "G-FIELD-UNITS", "G-NO-FLOAT-AST",
    "G-STAGE-DIM-FROM-ANCHOR", "G-LINKS-IN-BALL", "G-LOCALITY-CRITERION-PORTED",
    "G-LOCALITY-THRESHOLD", "G-PARITY-WITNESS", "G-LSWEEP-COMPLETE",
    "G-CONNECTIVE-FORCED-BY-ANCHORED-LINK",
    "G-ORD-SWEEP-EXHAUSTIVE", "G-ORD-COLLAPSE-THEOREM", "G-ORD-CENSUS-COUNTS",
    "G-FIVE-POINT-EXTENSION", "G-FIVE-POINT-ORDERING-INVARIANT",
    "G-FIVE-POINT-AT-UNIQUE-SCALE",
    "G-MOORE-BALL-COLLAPSE", "G-ALPHABET-INDEPENDENCE",
    "G-UNIQUE-SCALE", "G-SCALE-PRESENCE-DERIVED", "G-LATTICE-BOUND-TO-ADMISSIBLE",
    "G-GAUGE-ORBITS-FREE", "G-POOL-DERIVED", "G-FAMILY-UNITARY-THREE-ROUTES",
    "G-CHOICE-INVENTORY-COMPLETE", "G-DIVISION-EVENTS-DECLARED",
    "G-DEFECT-DEFINITION", "G-DEFECT-ROUTES-AGREE", "G-DEFECT-CLOSED-FORM",
    "G-DEFECT-FOURIER-AGREE", "G-DEFECT-VALUE-CENSUS",
    "G-DEFECT-VALUE-CENSUS-FULL", "G-DEFECT-NONZERO-EXISTS",
    "G-DEFECT-COLUMN-SUMS", "G-MARKOV-ZERO", "G-MARKOV-ZERO-OBJECT",
    "G-MARKOV-CLASSIFIER",
    "G-MARKOV-POSITIVE-CONTROL", "G-COHERENCE-LAW", "G-DEFECT-NORMALIZATION",
    "G-DEFECT-EQUIVARIANCE", "G-DEFECT-REVERSAL", "G-GAUGE-SELFTEST",
    "G-GAUGE-HANDLE", "G-CACHE-EXERCISED",
    "G-LOCALITY-DEPENDENCE", "G-LOCALITY-LIKE-FOR-LIKE",
    "G-LIKE-FOR-LIKE-DISTINCT", "G-NONLOCAL-CONTROL",
    "G-TWOPOINT-TRANSLATION-COVARIANT", "G-TWOPOINT-SCRAMBLE-BREAKS",
    "G-TWOPOINT-EQUAL-TIME", "G-TWOPOINT-COMPOSED", "G-TWOPOINT-LIGHTCONE",
    "G-LIGHTCONE-VACUITY-MEASURED", "G-TWOPOINT-RADIUS-PROFILES",
    "G-CEILINGS-MEASURED",
    "G-TWOPOINT-PERIODICITY", "G-TWOPOINT-STOCHASTIC",
    "G-CLASS-ORBITS-PARTITION", "G-CLASS-ORBIT-STABILIZER",
    "G-CLASS-INVARIANTS", "G-CLASS-LABELS-NONSEPARATING", "G-CLASS-TWO-GROUPS",
    "G-CLASS-TRANSLATION-TRIVIAL", "G-CLASS-CONTROLS-MOVE",
    "G-COMMUTATOR-CENSUS",
    "G-REALIZATION-LEVELS", "G-REALIZATION-LEVELS-PER-GENERATOR",
    "G-REALIZATION-MAXIMAL-NONEMPTY",
    "G-REALIZATION-GATE-BITES", "G-REALIZATION-VERDICT-ONLY-MAXIMAL",
    "G-STATE-COEFFICIENT-BACKGROUND", "G-STATE-OBSERVABLE-MOVES",
    "G-STATE-PROBE-BREADTH",
    "G-VERDICT-HEAD-DERIVED", "G-VERDICT-STRING-EQUALITY",
    "G-VERDICT-SEGMENTS-FLIPPABLE", "G-VERDICT-VALUES-FLIPPABLE",
    "G-VERDICT-THREE-HEADS-REACHABLE",
    "G-VERDICT-PREREGISTERED", "G-VERDICT-NO-PAPER-INPUT",
    "G-PRECHECK-DOES-NOT-NAME-THE-VERDICT",
    "G-RENDER-FROM-GATED-OBJECT", "G-COUNTS-DERIVED", "G-COUNTS-FROM-RECEIPT",
    "G-ROW-COMPLETENESS",
    "G-NO-MUTANT-IDENTITY-IN-GATES", "G-SELF-COMPARE-GUARD",
    "G-FORCINGS-REGISTERED", "G-COMPLIANCE-COMPUTED", "G-CLI-CONTRACT",
    "G-PAPER-CLAIMS-VERIFIED",
    "G-EVERY-GATE-EVALUATED", "G-NO-FLOAT-RECEIPT", "G-WAIVERS-VERIFIED",
]

# Registered forcings (#208 / #34).  TWO duties, one registry:
#   (a) a gate carrying no declared falsifier must name why it cannot have one;
#   (b) a gate whose CLAUSE IS ANALYTICALLY FORCED is a DISCLOSURE, not a
#       must-pass measurement, and must name the forcing and the gate that
#       carries the measured content in its place.
# G-FORCINGS-REGISTERED gates that every FORCED / DISCLOSURE / DECLARED row in
# the ledger appears here.
FORCINGS = {
    "G-WAIVERS-VERIFIED":
        "this gate is evaluated after the mutant harness, so no mutant can "
        "reach it; it therefore carries its own in-gate injection falsifier -- "
        "a synthetic waiver with no registered forcing, which the same "
        "predicate must detect.",
    "G-DEFECT-DEFINITION-SHAPE":
        "analytically true by construction: it records the shape of the "
        "reimplemented definition and binds the verbatim row VB-DEFECT-DEF to "
        "its consumer.  It is a DISCLOSURE, not a measurement; the definition's "
        "CONTENT is measured at G-DEFECT-DEFINITION, which reproduces the "
        "anchored source's own two-by-two witness and dies under "
        "MUT-DEFECT-WITNESS.",
    "G-DEFECT-CLOSED-FORM":
        "the cross-term form and the definition are algebraically the same "
        "identity in two bases, so agreement is forced; the row is an "
        "IMPLEMENTATION CROSS-CHECK, not a second measurement.  Its measured "
        "use is at G-DEFECT-VALUE-CENSUS-FULL, where the second code path "
        "binds the whole value multiset.",
    "G-COHERENCE-LAW":
        "an identity of associativity: both sides are B(U3U2U1) - "
        "B(U3)B(U2)B(U1).  It constrains the family not at all.",
    "G-DIVISION-EVENTS-DECLARED":
        "the division-event times are this unit's DECLARATION, not a "
        "measurement; the row discloses them and binds VB-DIVISION-EVENT to "
        "its consumer.  What is measured is the consequence: with t = 1 "
        "declared a division event there is no cut, and MUT-DIVISION-EVENTS "
        "dies here.",
    "G-STATE-COEFFICIENT-BACKGROUND":
        "an identity of linear algebra: delta(p) = Delta^B p is linear, so the "
        "sixteen point-mass responses ARE the sixteen columns of Delta^B and "
        "reassemble it for every matrix whatever.  A coefficient can move with "
        "the state only outside a linear law on a single-occupation sector, "
        "which this arena excludes by construction.  The measured half is at "
        "G-STATE-OBSERVABLE-MOVES and G-STATE-PROBE-BREADTH.",
    "G-CLASS-TRANSLATION-TRIVIAL":
        "a coefficient-map matrix M[x+o, x] = c_o commutes with every lattice "
        "translation BY CONSTRUCTION, so the 58 singleton orbits are an "
        "identity of the circulant family, not a measurement.  The measured "
        "half -- that the CONTROLS move -- is at G-CLASS-CONTROLS-MOVE.",
    "G-TWOPOINT-COMPOSED":
        "B(U2U1) = B(U2)B(U1) + Delta^B is the definition of Delta^B "
        "rearranged; the split is forced.  The row is an implementation "
        "check.  What is measured is the SIZE of the interference part, at "
        "the defect census.",
    "G-TWOPOINT-LIGHTCONE":
        "at the working size the lattice half-width is 2 and the maximum "
        "attainable Chebyshev radius is 2, so the cone bound min((n+1)r, L//2) "
        "is >= 2 for every n >= 1 at every generator of radius >= 1 and cannot "
        "fail.  The clause has content only at radius 0.  Measured at "
        "G-LIGHTCONE-VACUITY-MEASURED (the exhaustive profile probe) and "
        "replaced in the verdict by G-TWOPOINT-RADIUS-PROFILES.",
    "G-TWOPOINT-EQUAL-TIME":
        "C0(x, y) = delta_xy p(x) - p(x)p(y) on the declared uniform state is "
        "p(1-p) = 1/16 - 1/256 at zero separation and -1/256 elsewhere: a "
        "function of |X| and the state alone, identical for EVERY family on 16 "
        "sites.  It is state arithmetic, not a two-point measurement of the "
        "dynamics.",
    "G-DEFECT-COLUMN-SUMS":
        "|U| entrywise-squared is doubly stochastic for unitary U, so both "
        "composites are column-stochastic and every defect column sums to zero "
        "identically.  Widened here from a 64-row sample to every census row, "
        "so the evidence matches the claim, but the claim is forced.",
    "G-TWOPOINT-STOCHASTIC":
        "column stochasticity of B(U) is forced by unitarity of U.",
    "G-DEFECT-NORMALIZATION":
        "Delta^B(I, U) = B(U) - B(I)B(U) = 0 identically; an identity of the "
        "Born map.",
    "G-DEFECT-EQUIVARIANCE":
        "conjugation by a permutation matrix commutes with the entrywise "
        "modulus-squared, so equivariance is an identity of the Born map.",
    "G-DEFECT-REVERSAL":
        "transposition commutes with the entrywise modulus-squared and "
        "reverses a product; an identity of the Born map.",
    "G-COMMUTATOR-CENSUS":
        "circulant convolution on an abelian group commutes, so the 0 of 3364 "
        "on the FULL stratum is a THEOREM, not a contingency.  The row is "
        "carried because its CONSEQUENCE is not forced and is the datum R5 "
        "inherits: the verdict-bearing stratum is exactly the commuting one, "
        "and the four generators the mandatory gate excludes are the entire "
        "source of non-commutativity on the stage.  The non-forced half -- "
        "which pairs outside the stratum fail to commute -- is measured.",
    "G-CEILINGS-MEASURED":
        "16 separations is every separation on a 16-site torus and radius 2 is "
        "the Chebyshev diameter of (Z_4)^2: both verdict numbers are arena "
        "CEILINGS, attained rather than profiled.  The row measures the "
        "ceilings so the verdict can carry them as ceilings.",
    "G-REALIZATION-LEVELS":
        "the level names are legal and one is assigned per generator: a "
        "well-formedness disclosure only.  The per-object obligation -- every "
        "individual classification against its own computed invariant -- is "
        "discharged at G-REALIZATION-LEVELS-PER-GENERATOR (the v14 #87 "
        "engraving: gates bind objects, not cardinalities).",
}

# Declared mutants: (name, target gate, what it injects)
MUTANTS = [
    ("MUT-ANCHOR-BYTE", "G-BYTE-ANCHORS", "corrupts a source's expected digest"),
    ("MUT-ANCHOR-PATH", "G-PATH-VALUE-ANCHORS", "reads the link set from a drifted JSON path"),
    ("MUT-ANCHOR-PATH-VALUE", "G-PATH-VALUE-ANCHORS", "keeps the path, drifts the expected value"),
    ("MUT-ANCHOR-VERBATIM", "G-VERBATIM-ANCHORS", "drifts a verbatim context window"),
    ("MUT-FIELD-CONJ", "G-FIELD-CANONICAL", "breaks complex conjugation"),
    ("MUT-FIELD-UNIT", "G-FIELD-UNITS", "breaks the sqrt2 element"),
    ("MUT-LINKS-OUTSIDE-BALL", "G-LINKS-IN-BALL", "declares a link outside the neighbourhood ball"),
    ("MUT-LOCALITY-CRITERION", "G-LOCALITY-CRITERION-PORTED", "inverts the ported completeness criterion"),
    ("MUT-LOCALITY-THRESHOLD", "G-LOCALITY-THRESHOLD", "shifts the measured completeness threshold"),
    ("MUT-PARITY-WITNESS", "G-PARITY-WITNESS", "makes both connectives agree by fiat"),
    ("MUT-LSWEEP-TRUNCATE", "G-LSWEEP-COMPLETE", "drops the last lattice size from the sweep"),
    ("MUT-ORD-TRUNCATE", "G-ORD-SWEEP-EXHAUSTIVE", "truncates the coefficient alphabet"),
    ("MUT-ORD-COLLAPSE", "G-ORD-COLLAPSE-THEOREM", "reports a non-monomial solution above the threshold"),
    ("MUT-ORD-COUNT", "G-ORD-CENSUS-COUNTS", "hard-codes an order-4 solution count"),
    ("MUT-UNIQUE-SCALE", "G-UNIQUE-SCALE", "admits a second admissible lattice size"),
    ("MUT-GAUGE-ORBIT", "G-GAUGE-ORBITS-FREE", "claims a short gauge orbit"),
    ("MUT-POOL-COUNT", "G-POOL-DERIVED", "drops a generator from the pool after counting"),
    ("MUT-UNITARITY", "G-FAMILY-UNITARY-THREE-ROUTES", "perturbs one generator coefficient"),
    ("MUT-CHOICE-INVENTORY", "G-CHOICE-INVENTORY-COMPLETE", "drops a construction choice row"),
    ("MUT-DEFECT-ZERO", "G-DEFECT-NONZERO-EXISTS", "zeroes every defect"),
    ("MUT-DEFECT-CENSUS-ZERO", "G-DEFECT-VALUE-CENSUS", "zeroes only the censused defect cells (the R3 Y1 class)"),
    ("MUT-DEFECT-ROUTE", "G-DEFECT-ROUTES-AGREE", "corrupts the convolution route"),
    ("MUT-DEFECT-FOURIER", "G-DEFECT-FOURIER-AGREE", "corrupts the character-basis route"),
    ("MUT-DEFECT-XT", "G-DEFECT-CLOSED-FORM", "corrupts the cross-term form"),
    ("MUT-DEFECT-VALUE", "G-DEFECT-VALUE-CENSUS", "alters one censused defect value"),
    ("MUT-MARKOV-LABEL", "G-MARKOV-CLASSIFIER", "labels a two-support generator monomial"),
    ("MUT-MARKOV-NONZERO", "G-MARKOV-ZERO", "injects a nonzero defect into a Markovian pair"),
    ("MUT-COHERENCE", "G-COHERENCE-LAW", "breaks one side of the coherence law"),
    ("MUT-GAUGE-SELFTEST", "G-GAUGE-SELFTEST", "breaks invariance under the outer torus"),
    ("MUT-GAUGE-HANDLE", "G-GAUGE-HANDLE", "claims the one handle is inert"),
    ("MUT-CACHE", "G-CACHE-EXERCISED", "reports a cache that is never exercised"),
    ("MUT-COVARIANCE", "G-TWOPOINT-TRANSLATION-COVARIANT", "declares a non-circulant generator covariant"),
    ("MUT-SCRAMBLE", "G-TWOPOINT-TRANSLATION-COVARIANT", "declares the scrambled control covariant"),
    ("MUT-SCRAMBLE-SEPTABLE", "G-TWOPOINT-SCRAMBLE-BREAKS", "reports the scrambled transition table as separation-indexed"),
    ("MUT-LIGHTCONE", "G-TWOPOINT-LIGHTCONE", "misreports the support radius law"),
    ("MUT-PERIOD", "G-TWOPOINT-PERIODICITY", "misreports a generator order"),
    ("MUT-CLASS-DROP", "G-CLASS-ORBITS-PARTITION", "drops one orbit from the class census"),
    ("MUT-CLASS-MERGE", "G-CLASS-ORBIT-STABILIZER", "merges two orbits"),
    ("MUT-CLASS-INVARIANT", "G-CLASS-INVARIANTS", "moves an invariant inside an orbit"),
    ("MUT-REALIZATION-PROMOTE", "G-REALIZATION-LEVELS-PER-GENERATOR", "promotes every generator to maximal transport"),
    ("MUT-REALIZATION-NOBITE", "G-REALIZATION-GATE-BITES", "claims no defect is excluded below maximal transport"),
    ("MUT-REALIZATION-ADMIT", "G-REALIZATION-VERDICT-ONLY-MAXIMAL", "admits sub-maximal defects into the verdict"),
    ("MUT-STATE-BACKGROUND", "G-STATE-COEFFICIENT-BACKGROUND", "makes the reconstructed coefficient state-dependent"),
    ("MUT-STATE-INERT", "G-STATE-OBSERVABLE-MOVES", "freezes the observable defect across states"),
    ("MUT-VERDICT-HEAD", "G-VERDICT-HEAD-DERIVED", "types the head instead of deriving it"),
    ("MUT-VERDICT-APPEND", "G-VERDICT-STRING-EQUALITY", "appends text to the emitted verdict"),
    ("MUT-VERDICT-SWAP", "G-VERDICT-STRING-EQUALITY", "swaps two segment values"),
    ("MUT-VERDICT-TYPED", "G-VERDICT-STRING-EQUALITY", "retypes a segment name as its value"),
    ("MUT-VERDICT-DROP", "G-VERDICT-STRING-EQUALITY", "drops a segment"),
    ("MUT-VERDICT-INERT", "G-VERDICT-SEGMENTS-FLIPPABLE", "makes one segment ignore its source row"),
    ("MUT-VERDICT-HEADS", "G-VERDICT-THREE-HEADS-REACHABLE", "makes the head derivation constant"),
    ("MUT-VERDICT-NAME", "G-VERDICT-PREREGISTERED", "emits a head outside the pin"),
    ("MUT-PRECHECK-NAMES", "G-PRECHECK-DOES-NOT-NAME-THE-VERDICT", "lets the scale precheck name the head"),
    ("MUT-RENDER-BYPASS", "G-RENDER-FROM-GATED-OBJECT", "renders a receipt cell around the gated object"),
    ("MUT-COUNT-TYPED", "G-COUNTS-DERIVED", "types a headline count"),
    ("MUT-ROW-DROP", "G-ROW-COMPLETENESS", "drops a census row"),
    ("MUT-DEFECT-WITNESS", "G-DEFECT-DEFINITION", "sign-flips the anchored two-by-two witness"),
    ("MUT-DIVISION-EVENTS", "G-DIVISION-EVENTS-DECLARED", "declares the cut a division event"),
    ("MUT-EXTRA-INPUT", "G-NO-UNANCHORED-RUNTIME-INPUT", "adds an unanchored runtime input"),
    ("MUT-FLOAT-AST", "G-NO-FLOAT-AST", "injects a float literal into the source scan"),
    ("MUT-STAGE-DIM", "G-STAGE-DIM-FROM-ANCHOR", "overrides the anchored dimension"),
    ("MUT-FIVE-POINT", "G-FIVE-POINT-EXTENSION", "reports a five-point non-monomial solution"),
    ("MUT-REALIZATION-EMPTY", "G-REALIZATION-MAXIMAL-NONEMPTY", "names an unattained maximal level"),
    ("MUT-COLUMN-SUM", "G-DEFECT-COLUMN-SUMS", "breaks a defect column sum"),
    ("MUT-MARKOV-NOPOS", "G-MARKOV-POSITIVE-CONTROL", "empties the free sub-family"),
    ("MUT-NORMALIZATION", "G-DEFECT-NORMALIZATION", "breaks normalization against the identity"),
    ("MUT-EQUIVARIANCE", "G-DEFECT-EQUIVARIANCE", "breaks permutation equivariance"),
    ("MUT-REVERSAL", "G-DEFECT-REVERSAL", "breaks reversal covariance"),
    ("MUT-LOCALITY-EMPTY", "G-LOCALITY-DEPENDENCE", "empties the non-local sub-census"),
    ("MUT-MATCHED-EMPTY", "G-LOCALITY-LIKE-FOR-LIKE", "empties the matched-coordinate table"),
    ("MUT-NONLOCAL-RADIUS", "G-NONLOCAL-CONTROL", "removes the non-local control"),
    ("MUT-EQUAL-TIME", "G-TWOPOINT-EQUAL-TIME", "corrupts the equal-time correlator"),
    ("MUT-COMPOSED", "G-TWOPOINT-COMPOSED", "breaks the composed-time split"),
    ("MUT-STOCHASTIC", "G-TWOPOINT-STOCHASTIC", "breaks column stochasticity"),
    ("MUT-ONE-GROUP", "G-CLASS-TWO-GROUPS", "drops the anchored-group census"),
    ("MUT-TRANS-TRIVIAL", "G-CLASS-TRANSLATION-TRIVIAL", "misreports the translation action"),
    ("MUT-FLOAT-RECEIPT", "G-NO-FLOAT-RECEIPT", "puts a float in the receipt"),
    ("MUT-DEAD-GATE", "G-EVERY-GATE-EVALUATED", "hides an evaluated gate"),
    ("MUT-SELFCOMPARE", "G-SELF-COMPARE-GUARD", "swaps in a self-comparing comparator"),
    ("MUT-GATE-REFERENCES-MUTANT", "G-NO-MUTANT-IDENTITY-IN-GATES", "adds a gate that exempts its own falsifier"),
    ("MUT-PAPER-INPUT", "G-VERDICT-STRING-EQUALITY", "appends an arena-prose segment to the emitted verdict"),
    ("MUT-COMPARATOR-READS-PROSE", "G-VERDICT-NO-PAPER-INPUT", "swaps in a comparator that reads receipt prose"),
    # --- the repair pass's own falsifiers ---------------------------------
    ("MUT-ROUTE-SUM-NORM-ROWS", "G-CONNECTIVE-FORCED-BY-ANCHORED-LINK",
     "routes the sum-norm locality rows into the admissibility loop"),
    ("MUT-CONNECTIVE-FREE", "G-LINKS-IN-BALL",
     "claims both connectives admit the anchored link set, so none is forced"),
    ("MUT-LATTICE-UNBOUND", "G-LATTICE-BOUND-TO-ADMISSIBLE",
     "censuses a lattice size other than the one the precheck admitted"),
    ("MUT-SCALE-PRESENCE", "G-SCALE-PRESENCE-DERIVED",
     "types the presence set instead of deriving it from the order census"),
    ("MUT-MOORE-BALL-LEMMA", "G-MOORE-BALL-COLLAPSE",
     "breaks the extreme-lag structure the ball collapse rests on"),
    ("MUT-FIELD-DOMAIN", "G-MOORE-BALL-COLLAPSE",
     "reports a zero divisor among the nonzero alphabet elements"),
    ("MUT-ALPHABET-INDEP", "G-ALPHABET-INDEPENDENCE",
     "claims a size below the locality threshold bears locality"),
    ("MUT-FIVE-POINT-ORDERING", "G-FIVE-POINT-ORDERING-INVARIANT",
     "reports the node count as an invariant of the five-point sweep"),
    ("MUT-FIVE-POINT-L4", "G-FIVE-POINT-AT-UNIQUE-SCALE",
     "empties the wider five-point family at the unique scale"),
    ("MUT-LEVEL-PROMOTE-ONE", "G-REALIZATION-LEVELS-PER-GENERATOR",
     "promotes exactly one sub-maximal generator to maximal transport"),
    ("MUT-LEVEL-DEMOTE-ONE", "G-REALIZATION-LEVELS-PER-GENERATOR",
     "demotes exactly one maximal-transport generator"),
    ("MUT-Y1-UNCENSUSED-ZERO", "G-DEFECT-VALUE-CENSUS-FULL",
     "zeroes defect rows OUTSIDE the twelve named value-census rows"),
    ("MUT-VALUE-MULTISET", "G-DEFECT-VALUE-CENSUS-FULL",
     "moves one cell count in the full value multiset"),
    ("MUT-MARKOV-OBJECT", "G-MARKOV-ZERO-OBJECT",
     "writes a nonzero defect OBJECT into a Markovian row, leaving its count"),
    ("MUT-COMMUTATOR", "G-COMMUTATOR-CENSUS",
     "misreports the commutator census of the verdict stratum"),
    ("MUT-CLASS-LABELS", "G-CLASS-LABELS-NONSEPARATING",
     "claims the declared class invariants separate the classes"),
    ("MUT-MATCHED-DISTINCT", "G-LIKE-FOR-LIKE-DISTINCT",
     "reports the weighted matched count as the distinct comparison count"),
    ("MUT-STATE-PROBE-NARROW", "G-STATE-PROBE-BREADTH",
     "shrinks the state-motion probe set below its declared breadth"),
    ("MUT-VALUE-INERT", "G-VERDICT-VALUES-FLIPPABLE",
     "makes one measured verdict VALUE ignore the receipt field it renders"),
    ("MUT-HEAD-POST-BUILD", "G-VERDICT-STRING-EQUALITY",
     "retypes the head AFTER every verdict gate has been built"),
    ("MUT-HEAD-ABSENT-VARIANT", "G-VERDICT-STRING-EQUALITY",
     "flips the head to an ABSENT variant after the build"),
    ("MUT-HEAD-OFF-PIN", "G-VERDICT-STRING-EQUALITY",
     "flips the head to a name outside the pin after the build"),
    ("MUT-COMPLIANCE-TYPED", "G-COMPLIANCE-COMPUTED",
     "types a compliance status instead of computing it"),
    ("MUT-PAPER-CLAIM-DRIFT", "G-PAPER-CLAIMS-VERIFIED",
     "drifts one rendered paper claim away from the paper's bytes"),
    ("MUT-PAPER-COVERAGE", "G-PAPER-CLAIMS-VERIFIED",
     "drops a rendered claim so a paper numeral goes uncovered"),
    ("MUT-FORCING-UNREGISTERED", "G-FORCINGS-REGISTERED",
     "ships a FORCED gate with no registered forcing"),
    ("MUT-COUNT-RECEIPT", "G-COUNTS-FROM-RECEIPT",
     "moves a headline count away from the serialized census rows"),
    ("MUT-CEILING", "G-CEILINGS-MEASURED",
     "misreports the arena ceiling the two-point numbers attain"),
    ("MUT-RADIUS-PROFILES", "G-TWOPOINT-RADIUS-PROFILES",
     "collapses the measured radius-profile census"),
    ("MUT-LIGHTCONE-VACUITY", "G-LIGHTCONE-VACUITY-MEASURED",
     "claims the cone bound has content above radius zero"),
    ("MUT-CONTROLS-INERT", "G-CLASS-CONTROLS-MOVE",
     "freezes the controls under the translation action"),
    ("MUT-GAUGE-SELFTEST-RIGHT", "G-GAUGE-SELFTEST",
     "breaks invariance under the outer torus on the RIGHT factor"),
    ("MUT-GATE-READS-LAUNDERED-NAME", "G-NO-MUTANT-IDENTITY-IN-GATES",
     "adds a gate reading a name whose only assignment is mutant-guarded"),
    ("MUT-CLI-ACCEPTS-UNKNOWN", "G-CLI-CONTRACT",
     "swaps in the runner that silently ignores what it does not recognise"),
]


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()[:12]


def sha12_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        cur = cur[part]
    return cur


# ===========================================================================
# SECTION 7.  THE PIPELINE
# ===========================================================================

def build_state(break_anchor=None):
    S = {"schema": SCHEMA}
    LD = Ledger()
    S["_ledger"] = LD

    # ---------------- verbatim anchors, evaluated FIRST (#34) --------------
    src_text = {}
    for sid, rel, dig, why in SOURCES:
        p = os.path.join(REPO, rel)
        with open(p, "rb") as f:
            src_text[sid] = f.read().decode("utf-8")
    vrows = []
    for aid, sid, consumer, window in VERBATIM_ANCHORS:
        w = window
        if mut("MUT-ANCHOR-VERBATIM") and aid == "VB-CLOSED-FORM":
            w = window.replace("total pairwise interference", "total pairwise incoherence")
        present = w in src_text[sid]
        vrows.append({"id": aid, "source": sid, "consumer_gate": consumer,
                      "window_sha256_12": sha12_text(w), "chars": len(w),
                      "present": present})
    LD.gate("G-VERBATIM-ANCHORS",
            "every verbatim context window occurs in its pinned source, and each "
            "row is bound to a named consumer gate",
            all(r["present"] for r in vrows) and
            all(r["consumer_gate"] in GATE_REGISTRY for r in vrows),
            "%d of %d present" % (sum(r["present"] for r in vrows), len(vrows)))
    S["verbatim_anchors"] = vrows

    # ---------------- byte anchors ----------------------------------------
    brows = []
    for sid, rel, dig, why in SOURCES:
        exp = dig
        if break_anchor == sid:
            exp = "deadbeef0000"
        if mut("MUT-ANCHOR-BYTE") and sid == "A-STAGE-I7":
            exp = "000000000000"
        got = sha12(os.path.join(REPO, rel))
        brows.append({"id": sid, "artifact": rel, "kind": "file-bytes",
                      "expected": exp, "measured": got, "provenance": why,
                      "match": exp == got})
    LD.gate("G-BYTE-ANCHORS", "every pinned source matches its frozen digest",
            all(r["match"] for r in brows),
            "; ".join("%s %s" % (r["id"], "ok" if r["match"] else
                                 "MISMATCH %s vs %s" % (r["expected"], r["measured"]))
                      for r in brows))
    S["byte_anchors"] = brows

    # ---------------- path-value anchors ----------------------------------
    jsrc = {}
    for sid, rel, dig, why in SOURCES:
        if rel.endswith(".json"):
            jsrc[sid] = json.loads(src_text[sid])
    prows = []
    for aid, sid, path, expected, why in PATH_VALUE_ANCHORS:
        pth, exp = path, expected
        if mut("MUT-ANCHOR-PATH") and aid == "PV-I7-LINKS":
            pth = "declarations/links_d3"
        if mut("MUT-ANCHOR-PATH-VALUE") and aid == "PV-I7-D":
            exp = 3
        try:
            got = jpath(jsrc[sid], pth)
        except (KeyError, TypeError):
            got = None
        prows.append({"id": aid, "source": sid, "path": pth, "expected": exp,
                      "measured": got, "provenance": why, "match": got == exp})
    LD.gate("G-PATH-VALUE-ANCHORS",
            "each read-by-path anchors the (path, value) pair; a path drift or a "
            "value drift dies here",
            all(r["match"] for r in prows),
            "%d of %d" % (sum(r["match"] for r in prows), len(prows)))
    S["path_value_anchors"] = prows

    with open(os.path.join(REPO, PAPER_REL), "r", encoding="utf-8") as f:
        S["_paper_text"] = f.read()
    reads = sorted(rel for _, rel, _, _ in SOURCES)
    object_under_test = [PAPER_REL]
    if mut("MUT-EXTRA-INPUT"):
        reads = reads + ["v14/LOG.md"]
    LD.gate("G-NO-UNANCHORED-RUNTIME-INPUT",
            "every file read at run time is either a hash-pinned SOURCE or the "
            "declared OBJECT UNDER TEST (this unit's own paper, which cannot be "
            "pinned against itself); both lists are enumerated and no other "
            "mutable repository state is read (#46)",
            len(reads) == len(SOURCES)
            and all(any(rel == s[1] for s in SOURCES) for rel in reads)
            and object_under_test == [PAPER_REL],
            "pinned sources: %s | object under test: %s"
            % (", ".join(reads), ", ".join(object_under_test)))
    S["runtime_inputs"] = {"pinned_sources": reads,
                           "object_under_test": object_under_test}

    # ---------------- the field -------------------------------------------
    say("[1/12] field, stage, locality")
    conj_ok = all(cconj(cconj(zpow(t))) == zpow(t) for t in range(8))
    if mut("MUT-FIELD-CONJ"):
        conj_ok = cconj(zpow(1)) == zpow(1)
    canon = {}
    dup = 0
    for t in range(8):
        for num, den in ((1, 1), (2, 2), (3, 3), (-2, -2)):
            e = cscal(zpow(t), num, den)
            canon.setdefault(e, set()).add((t, num, den))
    for e, ws in canon.items():
        if len(ws) > 1:
            dup += 1
    LD.gate("G-FIELD-CANONICAL",
            "the representation is canonical: equal field elements have equal "
            "tuples, conjugation is an involution, and zeta_8 has order 8",
            conj_ok and dup == 8 and zpow(8) == ONE and cnormsq(zpow(3)) == ONE,
            "conj-involution=%s collapsed-classes=%d" % (conj_ok, dup))
    sq2 = SQ2
    if mut("MUT-FIELD-UNIT"):
        sq2 = cadd(SQ2, ONE)
    LD.gate("G-FIELD-UNITS",
            "sqrt2 squares to 2, i squares to -1, and 1/sqrt2 squares to 1/2",
            cmul(sq2, sq2) == crat(2) and cmul(zpow(2), zpow(2)) == crat(-1)
            and cmul(INV_SQ2, INV_SQ2) == crat(1, 2),
            "sqrt2^2=%s" % cstr(cmul(sq2, sq2)))

    with open(SELF, "r", encoding="utf-8") as f:
        own_src = f.read()
    tree = ast.parse(own_src)
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    floatcalls = [n for n in ast.walk(tree)
                  if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                  and n.func.id == "float"]
    truediv = [n for n in ast.walk(tree) if isinstance(n, ast.BinOp)
               and isinstance(n.op, ast.Div)]
    if mut("MUT-FLOAT-AST"):
        floats = [None]
    LD.gate("G-NO-FLOAT-AST",
            "the instrument's own source contains no float literal, no float() "
            "call and no true division",
            not floats and not floatcalls and not truediv,
            "literals=%d calls=%d truediv=%d" % (len(floats), len(floatcalls), len(truediv)))

    # ---------------- the stage -------------------------------------------
    d = jpath(jsrc["A-STAGE-I7"], "declarations/d")
    links = jpath(jsrc["A-STAGE-I7"], "declarations/links_d2")
    if mut("MUT-ANCHOR-PATH"):
        links = [[1, 0], [0, 1], [1, 1]]
    if mut("MUT-STAGE-DIM"):
        d = 3
    LD.gate("G-STAGE-DIM-FROM-ANCHOR",
            "the spatial dimension is read from the anchored stage, not typed",
            d == 2, "d=%s" % d)

    Lsweep = list(L_SWEEP)
    if mut("MUT-LSWEEP-TRUNCATE"):
        Lsweep = Lsweep[:-1]
    loc_rows = []
    for dd in D_SWEEP:
        for LL in Lsweep:
            for conn in CONNECTIVES:
                r = lattice_locality(LL, dd, conn)
                r.update({"d": dd, "L": LL, "connective": conn})
                loc_rows.append(r)
    S["locality_sweep"] = loc_rows
    LD.gate("G-LSWEEP-COMPLETE",
            "the lattice sweep is cell-complete: every declared (d, L, "
            "connective) triple has a row",
            len(loc_rows) == len(D_SWEEP) * len(Lsweep) * len(CONNECTIVES)
            and len(Lsweep) == len(L_SWEEP),
            "rows=%d expected=%d" % (len(loc_rows),
                                     len(D_SWEEP) * len(L_SWEEP) * len(CONNECTIVES)))

    # THE CONNECTIVE IS NOT FREE.  Each declared Boolean connective admits a
    # radius-1 ball; the anchored link set either fits inside it or does not.
    # The anchored diagonal link (1,1) has max-norm 1 and sum-norm 2, so it lies
    # inside the max-norm ball and outside the sum-norm ball: exactly one
    # connective can carry the stage's own declared links.
    test_links = [tuple(v) for v in links]
    if mut("MUT-LINKS-OUTSIDE-BALL"):
        test_links = test_links + [(2, 0)]
    norms = {CONNECTIVES[0]: torus_absmax, CONNECTIVES[1]: torus_abssum}
    conn_admits, conn_reasons = {}, {}
    for conn in CONNECTIVES:
        nf = norms[conn]
        outside = [(v, min(nf(v, LL) for LL in L_SWEEP if LL >= 3))
                   for v in test_links
                   if any(nf(v, LL) > 1 for LL in L_SWEEP if LL >= 3)]
        conn_admits[conn] = not outside
        conn_reasons[conn] = ("every anchored link inside the radius-1 ball"
                              if not outside else
                              "; ".join("link %s has norm %d > 1" % (v, n)
                                        for v, n in outside))
    if mut("MUT-CONNECTIVE-FREE"):
        conn_admits = {c: True for c in CONNECTIVES}
    admitting = [c for c in CONNECTIVES if conn_admits[c]]
    forced_connective = admitting[0] if len(admitting) == 1 else None
    LD.gate("G-LINKS-IN-BALL",
            "every anchored link lies in the radius-1 neighbourhood of the "
            "connective that admits the anchored link set, at every swept "
            "lattice size that can carry a radius-1 ball",
            forced_connective is not None
            and all(norms[forced_connective](v, LL) <= 1
                    for v in test_links for LL in L_SWEEP if LL >= 3),
            "links=%s forced connective=%s" % (test_links, forced_connective))

    crit = jpath(jsrc["A-LOCALITY-R2"], "locality_census/criterion")
    moore_rows = [r for r in loc_rows if r["connective"] == CONNECTIVES[0]]
    ported = all(r["locality"] == (not r["complete"]) for r in moore_rows)
    if mut("MUT-LOCALITY-CRITERION"):
        ported = all(r["locality"] == r["complete"] for r in moore_rows)
    LD.gate("G-LOCALITY-CRITERION-PORTED",
            "the anchored criterion (locality iff a component is not complete) "
            "is applied verbatim to the lattice adjacency graph",
            ported and crit.startswith("locality exists at a rule iff SOME"),
            "criterion chars=%d applied at %d rows" % (len(crit), len(moore_rows)))

    # the THRESHOLD TABLE: both connectives, every swept dimension, printed.
    thr_table = {}
    for conn in CONNECTIVES:
        rows_c = [r for r in loc_rows if r["connective"] == conn]
        for dd in D_SWEEP:
            loc_L = sorted(r["L"] for r in rows_c if r["d"] == dd and r["locality"])
            thr_table[(conn, dd)] = min(loc_L) if loc_L else None
    thresholds = {dd: thr_table[(CONNECTIVES[0], dd)] for dd in D_SWEEP}
    if mut("MUT-LOCALITY-THRESHOLD"):
        thresholds[2] = 3
    LD.gate("G-LOCALITY-THRESHOLD",
            "under the FORCED connective the lattice bears locality exactly "
            "above a measured size threshold, the same at every swept dimension",
            set(thresholds.values()) == {4}
            and all(r["locality"] == (r["L"] >= 4) for r in moore_rows),
            "thresholds by d: %s" % thresholds)
    S["locality_thresholds"] = {str(k): v for k, v in thresholds.items()}
    S["locality_threshold_table"] = [
        {"connective": conn, "connective_tag": CONNECTIVE_TAGS[CONNECTIVES.index(conn)],
         "d": dd, "threshold": thr_table[(conn, dd)],
         "admits_anchored_links": conn_admits[conn]}
        for conn in CONNECTIVES for dd in D_SWEEP]

    vn_rows = [r for r in loc_rows if r["connective"] == CONNECTIVES[1]]
    vn_thr = min([r["L"] for r in vn_rows if r["d"] == 2 and r["locality"]] or [0])
    delta = vn_thr - thresholds[2]
    if mut("MUT-PARITY-WITNESS"):
        delta = 0
    LD.gate("G-PARITY-WITNESS",
            "the Boolean connective bounding the neighbourhood carries a "
            "parity-witness: the EXCLUDED connective's measured threshold delta "
            "is printed and is nonzero, so the exclusion is not free",
            delta != 0,
            "max-norm threshold=%s sum-norm threshold=%s delta=%s"
            % (thresholds[2], vn_thr, delta))
    S["parity_witness"] = {"moore_threshold_d2": thresholds[2],
                           "von_neumann_threshold_d2": vn_thr, "delta": delta}

    # ---------------- the family ------------------------------------------
    say("[2/12] the coefficient sweep and the order census")
    alphabet = build_alphabet()
    if mut("MUT-ORD-TRUNCATE"):
        alphabet = alphabet[:9]
    ordc = ord_sweep(alphabet, ORD_SWEEP)
    S["alphabet_size"] = len(alphabet)
    S["ord_census"] = {str(k): v for k, v in ordc.items()}
    swept = sum(v["triples_swept"] for v in ordc.values())
    LD.gate("G-ORD-SWEEP-EXHAUSTIVE",
            "the coefficient sweep is exhaustive over the declared alphabet "
            "cubed at every swept order; the count is computed, not typed",
            len(alphabet) == 25
            and swept == len(alphabet) ** 3 * len(ORD_SWEEP),
            "alphabet=%d triples=%d" % (len(alphabet), swept))

    above = {n: ordc[n]["non_monomial"] for n in ORD_SWEEP if n >= 5}
    if mut("MUT-ORD-COLLAPSE"):
        above[7] = 4
    LD.gate("G-ORD-COLLAPSE-THEOREM",
            "at axis order 5 and above the only unitary generators on the "
            "declared stencil are monomial (the collapse theorem, machine-"
            "checked over the alphabet)",
            all(v == 0 for v in above.values()),
            "non-monomial above threshold: %s" % above)

    ord4 = ordc[4]["distinct_generators"]
    ord4nm = ordc[4]["non_monomial"]
    ord2nm = ordc[2]["non_monomial"]
    if mut("MUT-ORD-COUNT"):
        ord4 = 64
    LD.gate("G-ORD-CENSUS-COUNTS",
            "the per-order census counts are recomputed by a second enumeration "
            "over the same alphabet",
            ord4 == len({tuple(sorted({o: v for o, v in
                                       (((0, c0), (1, c1), (3, c2)))}.items()))
                         for c0, c1, c2 in product(alphabet, repeat=3)
                         if ring_autocorr_unitary(
                             {o: vv for o, vv in ((0, c0), (1, c1), (3, c2)) if vv != ZERO}, 4)})
            and ord4nm > 0 and ord2nm > 0,
            "ord4=%d non-monomial=%d; ord2 non-monomial=%d" % (ord4, ord4nm, ord2nm))

    fp = five_point_collapse(alphabet, 5)
    if mut("MUT-FIVE-POINT"):
        fp = dict(fp, non_monomial=1)
    S["five_point_extension"] = fp
    LD.gate("G-FIVE-POINT-EXTENSION",
            "the declared extension: the 5-point stencil at a lattice size above "
            "the collapse threshold admits no non-monomial unitary generator",
            fp["non_monomial"] == 0,
            "L=5 five-point non-monomial=%d leaves=%d"
            % (fp["non_monomial"], fp["leaves_reached"]))

    # the five-point sweep at every declared size, in BOTH declared offset
    # orderings.  The node count is an artifact of the ordering; the leaf count
    # and the solution count are the invariants, and only they are reported.
    fp_rows = []
    for LL in FIVE_POINT_SIZES:
        for ordering in ("AXIS-FIRST", "CENTRE-FIRST"):
            fp_rows.append(five_point_collapse(alphabet, LL, ordering))
    ordering_pairs = [(a, b) for a in fp_rows for b in fp_rows
                      if a["L"] == b["L"] and a["ordering"] < b["ordering"]]
    inv_ok = all(a["leaves_reached"] == b["leaves_reached"]
                 and a["non_monomial"] == b["non_monomial"]
                 for a, b in ordering_pairs)
    nodes_differ = sum(1 for a, b in ordering_pairs
                       if a["nodes_visited"] != b["nodes_visited"])
    if mut("MUT-FIVE-POINT-ORDERING"):
        nodes_differ = 0
    LD.gate("G-FIVE-POINT-ORDERING-INVARIANT",
            "the five-point sweep's leaf count and solution count are invariant "
            "under the declared offset ordering while the NODE count is not, so "
            "the node count is reported as a search artifact and never as a "
            "property of the stencil",
            inv_ok and nodes_differ > 0 and len(ordering_pairs) == len(FIVE_POINT_SIZES),
            "sizes=%d orderings compared=%d node counts that differ=%d; "
            "leaves and solutions invariant=%s"
            % (len(FIVE_POINT_SIZES), len(ordering_pairs), nodes_differ, inv_ok))
    S["five_point_sweeps"] = fp_rows

    # the five-point stencil AT the unique scale: a wider local family that this
    # unit's 3-term census does not examine.  Reported, not promoted.
    fp4 = [r for r in fp_rows if r["L"] == 4 and r["ordering"] == "AXIS-FIRST"][0]
    fp4_nm = fp4["non_monomial"]
    if mut("MUT-FIVE-POINT-L4"):
        fp4_nm = 0
    LD.gate("G-FIVE-POINT-AT-UNIQUE-SCALE",
            "at the unique admissible scale the 5-point stencil admits a wider "
            "local family than the 3-term axis stencil this unit censuses; the "
            "count is measured and disclosed, and no verdict segment rests on it",
            fp4_nm > 0 and fp4_nm > ordc[4]["non_monomial"],
            "five-point non-monomial at L=4: %d (3-term axis stencil at ord 4: "
            "%d); leaves=%d" % (fp4_nm, ordc[4]["non_monomial"],
                                fp4["leaves_reached"]))

    # THE MOORE-BALL COLLAPSE THEOREM, legs 1 and 2 measured (leg 3 is the order
    # census above).  Closes the declared 9-point scope hole for every L >= 5.
    lag_rows = [moore_ball_lag_structure(LL) for LL in MOORE_BALL_LEMMA_SIZES]
    dom = field_is_a_domain(alphabet)
    lag_ok = all(r["cross_lag_structure_ok"] and r["single_column_lag_ok"]
                 and r["no_wraparound"] for r in lag_rows)
    if mut("MUT-MOORE-BALL-LEMMA"):
        lag_ok = False
    dom_bad = dom["zero_divisor_pairs"]
    if mut("MUT-FIELD-DOMAIN"):
        dom_bad = 1
    collapse_above = all(v == 0 for n, v in above.items())
    LD.gate("G-MOORE-BALL-COLLAPSE",
            "the Moore-ball collapse theorem's checkable legs: at every declared "
            "L >= 5 the radius-1 ball's extreme lag (2, t) receives contributions "
            "only from column -1 against column +1 and the single-column lag "
            "(0, 2) receives exactly one pair, with no wraparound; the field has "
            "no zero divisors, so the Laurent ring is a domain; and the "
            "single-column reduction is the order census's own >= 5 rows",
            lag_ok and dom_bad == 0 and collapse_above,
            "sizes checked=%s lag structure ok=%s zero-divisor pairs=%d of "
            "%d^2 nonzero; order census >= 5 non-monomial=%s"
            % (list(MOORE_BALL_LEMMA_SIZES), lag_ok, dom_bad,
               dom["nonzero_elements"], sorted(above.values())))
    S["moore_ball_collapse"] = {"sizes": list(MOORE_BALL_LEMMA_SIZES),
                                "lag_rows": lag_rows, "domain": dom}

    # THE UNIQUE SCALE.  Local axes have order L; non-monomial local generators
    # therefore exist iff L is an order with non-monomial solutions.  The rows
    # fed to the loop are the FORCED connective's rows, and that routing is
    # itself gated.
    routed_connective = forced_connective
    if mut("MUT-ROUTE-SUM-NORM-ROWS"):
        routed_connective = CONNECTIVES[1]
    routed_rows = [r for r in loc_rows if r["connective"] == routed_connective]

    def admissible_under(rows_c):
        out = []
        for LL in L_SWEEP:
            row = [r for r in rows_c if r["d"] == 2 and r["L"] == LL][0]
            has_nm = ordc.get(LL, {"non_monomial": 0})["non_monomial"] > 0
            local_ax_ord = {elt_order(v, LL) for v in product(range(LL), repeat=2)
                            if any(v) and torus_absmax(v, LL) <= 1}
            if row["locality"] and has_nm and local_ax_ord == {LL}:
                out.append(LL)
        return out

    admissible = admissible_under(routed_rows)
    excluded_conn = [c for c in CONNECTIVES if c != forced_connective][0]
    admissible_excluded = admissible_under(
        [r for r in loc_rows if r["connective"] == excluded_conn])
    LD.gate("G-CONNECTIVE-FORCED-BY-ANCHORED-LINK",
            "the neighbourhood connective is FORCED, not free: exactly one "
            "declared connective's radius-1 ball contains the anchored link "
            "set, and the admissibility loop consumes that connective's rows "
            "and no other.  The exclusion has bite: under the excluded "
            "connective the admissible set is different",
            forced_connective is not None
            and routed_connective == forced_connective
            and all(r["connective"] == forced_connective for r in routed_rows)
            and admissible_excluded != admissible,
            "forced=%s (%s); excluded=%s (%s); rows routed into the "
            "admissibility loop carry %s; admissible under the forced "
            "connective=%s, under the excluded connective=%s"
            % (forced_connective, conn_reasons.get(forced_connective, ""),
               excluded_conn, conn_reasons.get(excluded_conn, ""),
               routed_connective, admissible, admissible_excluded))
    S["connective_forcing"] = {
        "forced": forced_connective,
        "forced_tag": CONNECTIVE_TAGS[CONNECTIVES.index(forced_connective)]
        if forced_connective else None,
        "excluded": excluded_conn,
        "excluded_tag": CONNECTIVE_TAGS[CONNECTIVES.index(excluded_conn)],
        "reason_forced": conn_reasons.get(forced_connective, ""),
        "reason_excluded": conn_reasons.get(excluded_conn, ""),
        "anchored_links": [list(v) for v in test_links],
        "admissible_under_forced": admissible,
        "admissible_under_excluded": admissible_excluded}

    if mut("MUT-UNIQUE-SCALE"):
        admissible = admissible + [6]
    LD.gate("G-UNIQUE-SCALE",
            "exactly one swept lattice size carries both locality and a "
            "non-monomial local-axis generator: the uniqueness is measured "
            "(len == 1) and the value is anchored separately",
            len(admissible) == 1 and admissible == [4],
            "admissible sizes: %s (count=%d)" % (admissible, len(admissible)))

    # the SECOND half of the scale statement, derived from the order census
    # rather than composed from typed text: the sizes at which a non-monomial
    # LOCAL-axis generator is PRESENT.  The bound is only-if, not iff.
    present_at = []
    for LL in L_SWEEP:
        local_ax_ord = {elt_order(v, LL) for v in product(range(LL), repeat=2)
                        if any(v) and torus_absmax(v, LL) <= 1}
        if local_ax_ord == {LL} and ordc.get(LL, {"non_monomial": 0})["non_monomial"] > 0:
            present_at.append(LL)
    only_if_bound = max(present_at) if present_at else None
    if mut("MUT-SCALE-PRESENCE"):
        present_at = [2, 3, 4]
    LD.gate("G-SCALE-PRESENCE-DERIVED",
            "the non-monomial-local-axis half of the scale statement is derived "
            "from the measured order census, not typed: it is an ONLY-IF bound "
            "with a measured presence set, and the presence set is NOT the whole "
            "interval below the bound",
            present_at == [LL for LL in L_SWEEP
                           if ordc.get(LL, {"non_monomial": 0})["non_monomial"] > 0
                           and {elt_order(v, LL) for v in product(range(LL), repeat=2)
                                if any(v) and torus_absmax(v, LL) <= 1} == {LL}]
            and only_if_bound is not None
            and present_at != [LL for LL in L_SWEEP if LL <= only_if_bound],
            "non-monomial local axis present at L in %s; only-if bound L<=%s; "
            "the interval below the bound is %s"
            % (present_at, only_if_bound,
               [LL for LL in L_SWEEP if LL <= only_if_bound]))
    S["scale_precheck"] = {"locality_iff_L_at_least": thresholds[2],
                           "non_monomial_local_only_if_L_at_most": only_if_bound,
                           "non_monomial_local_present_at": present_at,
                           "unique": admissible}

    # ALPHABET INDEPENDENCE.  Below the locality threshold no alphabet can help,
    # because locality is a property of the stage alone; above the collapse
    # threshold no alphabet can help, because the collapse is a theorem over any
    # field.  So the admissible set is {4} for EVERY alphabet enlargement.
    locality_sizes = [r["L"] for r in routed_rows if r["d"] == 2 and r["locality"]]
    theorem_free = [LL for LL in L_SWEEP if LL < 5]
    alphabet_independent = sorted(set(locality_sizes) & set(theorem_free))
    if mut("MUT-ALPHABET-INDEP"):
        alphabet_independent = alphabet_independent + [3]
    LD.gate("G-ALPHABET-INDEPENDENCE",
            "the uniqueness survives every alphabet enlargement: the sizes "
            "excluded by locality are excluded by the stage and the sizes "
            "excluded at order >= 5 are excluded by the collapse theorem over "
            "any field, so the only size an enlarged alphabet could add lies in "
            "their intersection, which is the admitted size itself",
            alphabet_independent == admissible and lag_ok and dom_bad == 0,
            "sizes bearing locality=%s; sizes below the collapse threshold=%s; "
            "intersection=%s; admitted=%s"
            % (sorted(set(locality_sizes)), theorem_free, alphabet_independent,
               admissible))
    S["alphabet_independence"] = {
        "locality_sizes": sorted(set(locality_sizes)),
        "below_collapse_threshold": theorem_free,
        "intersection": alphabet_independent}
    S["admissible_scales"] = admissible

    # ---------------- build the generator pool at the ADMITTED size --------
    say("[3/12] the generator pool")
    L = admissible[0]
    if mut("MUT-LATTICE-UNBOUND"):
        L = admissible[0] + 1
    LD.gate("G-LATTICE-BOUND-TO-ADMISSIBLE",
            "the lattice the census runs on is the lattice the precheck "
            "admitted: L is taken FROM the measured admissible set, never typed "
            "beside it",
            L == admissible[0] and len(admissible) == 1
            and S["scale_precheck"]["unique"] == admissible,
            "census L=%d admissible=%s" % (L, admissible))
    sites = list(product(range(L), repeat=2))
    NS = len(sites)
    IDX = {s: i for i, s in enumerate(sites)}

    def addv(a, b):
        return ((a[0] + b[0]) % L, (a[1] + b[1]) % L)

    def subv(a, b):
        return ((a[0] - b[0]) % L, (a[1] - b[1]) % L)

    def smul(k, a):
        return ((k * a[0]) % L, (k * a[1]) % L)

    # the declared axis set: every nonzero offset, modulo sign -- exhaustive
    axes, seen_ax = [], set()
    for v in sites:
        if not any(v) or v in seen_ax:
            continue
        seen_ax.add(v)
        seen_ax.add(smul(L - 1, v))
        axes.append(v)
    axis_info = {a: {"ord": elt_order(a, L), "radius": torus_absmax(a, L)} for a in axes}

    def axis_gens(a):
        memo_key = (tuple(alphabet), L, a)
        if memo_key in _AXIS_MEMO:
            return {k: dict(v) for k, v in _AXIS_MEMO[memo_key].items()}
        out = {}
        for trip in product(alphabet, repeat=3):
            c = {}
            for o, v in (((0, 0), trip[0]), (a, trip[1]), (smul(L - 1, a), trip[2])):
                c[o] = cadd(c.get(o, ZERO), v)
            c = {o: v for o, v in c.items() if v != ZERO}
            key = tuple(sorted(c.items()))
            if key in out:
                continue
            if coef_autocorr_unitary(c, sites, addv):
                out[key] = c
        _AXIS_MEMO[memo_key] = out
        return {k: dict(v) for k, v in out.items()}

    def gauge_orbit(key):
        return {tuple(sorted((o, cmul(zpow(t), v)) for o, v in key)) for t in range(8)}

    pool = []          # list of dicts describing generators
    pool_keys = set()
    orbit_sizes = []
    for a in axes:
        gens = axis_gens(a)
        done = set()
        for key in sorted(gens):
            if key in done:
                continue
            orb = gauge_orbit(key)
            orbit_sizes.append(len(orb))
            done |= orb
            rep = min(orb)
            if rep in pool_keys:
                continue
            pool_keys.add(rep)
            c = dict(rep)
            radius = max([torus_absmax(o, L) for o in c] or [0])
            pool.append({"name": "", "kind": "CIRC", "axis": a,
                         "axis_ord": axis_info[a]["ord"], "coef": c,
                         "support": len(c), "radius": radius,
                         "monomial": len(c) <= 1})
    if mut("MUT-GAUGE-ORBIT"):
        orbit_sizes[0] = 4
    LD.gate("G-GAUGE-ORBITS-FREE",
            "the declared global-phase gauge acts freely on the solution set: "
            "every orbit has the full group's size",
            set(orbit_sizes) == {8},
            "orbit sizes: %s over %d orbits" % (sorted(set(orbit_sizes)), len(orbit_sizes)))

    # brickwork controls (partial transport) and scrambled controls (none)
    Hcoin = ((INV_SQ2, INV_SQ2), (INV_SQ2, cneg(INV_SQ2)))

    def brickwork(e, par):
        M = {}
        for x in sites:
            proj = (x[0] * e[0] + x[1] * e[1]) % L
            if proj % 2 == par:
                y = addv(x, e)
                M[(IDX[x], IDX[x])] = Hcoin[0][0]
                M[(IDX[x], IDX[y])] = Hcoin[0][1]
                M[(IDX[y], IDX[x])] = Hcoin[1][0]
                M[(IDX[y], IDX[y])] = Hcoin[1][1]
        return M

    def coef_matrix(c):
        return {(IDX[addv(x, o)], IDX[x]): v for x in sites for o, v in c.items()}

    for g in pool:
        g["mat"] = coef_matrix(g["coef"])

    ncirc = len(pool)
    for e in ((1, 0), (0, 1)):
        for par in (0, 1):
            M = brickwork(e, par)
            rad = max(torus_absmax(subv(sites[i], sites[j]), L) for (i, j) in M)
            pool.append({"name": "", "kind": "BRICK", "axis": e, "axis_ord": elt_order(e, L),
                         "coef": None, "support": None, "radius": rad,
                         "monomial": False, "mat": M, "parity": par})
    base_for_scramble = [g for g in pool[:ncirc] if g["support"] == 3][0]
    for (u, w) in SCRAMBLE_SWAPS:
        pi = list(range(NS))
        pi[u], pi[w] = pi[w], pi[u]
        M = {(pi[i], pi[j]): v for (i, j), v in base_for_scramble["mat"].items()}
        rad = max(torus_absmax(subv(sites[i], sites[j]), L) for (i, j) in M)
        pool.append({"name": "", "kind": "SCRAM", "axis": None, "axis_ord": None,
                     "coef": None, "support": None, "radius": rad,
                     "monomial": False, "mat": M, "swap": [u, w]})
    for i, g in enumerate(pool):
        g["idx"] = i
        g["name"] = "%s%03d" % (g["kind"][0], i)

    if mut("MUT-POOL-COUNT"):
        pool_declared = len(pool) + 1
    else:
        pool_declared = len(pool)
    n_circ = sum(1 for g in pool if g["kind"] == "CIRC")
    n_brick = sum(1 for g in pool if g["kind"] == "BRICK")
    n_scram = sum(1 for g in pool if g["kind"] == "SCRAM")
    LD.gate("G-POOL-DERIVED",
            "the generator pool size is derived from the sweep, not typed, and "
            "its parts sum to the whole",
            pool_declared == len(pool) == n_circ + n_brick + n_scram,
            "pool=%d = circ %d + brick %d + scram %d"
            % (len(pool), n_circ, n_brick, n_scram))

    # three independent unitarity routes
    bad_u = []
    for g in pool:
        m = g["mat"]
        if mut("MUT-UNITARITY") and g["idx"] == 3:
            m = dict(m)
            k = sorted(m)[0]
            m[k] = cadd(m[k], crat(1, 2))
        r1 = mat_is_unitary(m, NS)
        r2 = coef_autocorr_unitary(g["coef"], sites, addv) if g["coef"] else r1
        if g["coef"]:
            fh = fourier_product_coefs(g["coef"], {(0, 0): ONE}, L, 2)
            r3 = True
            ks = list(product(range(L), repeat=2))
            for k in ks:
                acc = ZERO
                for o, cv in g["coef"].items():
                    acc = cadd(acc, cmul(cv, zpow((2 * (k[0] * o[0] + k[1] * o[1])) % 8)))
                if cnormsq(acc) != ONE:
                    r3 = False
                    break
        else:
            r3 = r1
        if not (r1 and r2 and r3):
            bad_u.append((g["name"], r1, r2, r3))
    LD.gate("G-FAMILY-UNITARY-THREE-ROUTES",
            "every generator is unitary by three independent routes: the adjoint "
            "product, the periodic autocorrelation, and the character modulus",
            not bad_u, "failures: %s" % (bad_u[:3] if bad_u else "none"))

    S["pool"] = [{"name": g["name"], "kind": g["kind"],
                  "axis": list(g["axis"]) if g["axis"] else None,
                  "axis_ord": g["axis_ord"], "support": g["support"],
                  "radius": g["radius"], "monomial": g["monomial"],
                  "coef": ([[list(o), list(v)] for o, v in sorted(g["coef"].items())]
                           if g["coef"] else None)}
                 for g in pool]
    S["pool_counts"] = {"total": len(pool), "circulant": n_circ,
                        "brickwork": n_brick, "scrambled": n_scram,
                        "axes": len(axes), "local_axes":
                        sum(1 for a in axes if axis_info[a]["radius"] == 1),
                        "nonlocal_axes":
                        sum(1 for a in axes if axis_info[a]["radius"] > 1)}

    # ---------------- THE CHOICE INVENTORY --------------------------------
    # Every construction choice, classed FORCED / STABILIZER-FIXED /
    # GENUINELY-FREE, with its exact fibre.  The declared family is arena data.
    n_local_ax = sum(1 for a in axes if axis_info[a]["radius"] == 1)
    choice_rows = [
        {"choice": "the spatial dimension d", "value": "2", "class": "FORCED",
         "fibre": 1, "why": "read from the anchored stage at PV-I7-D; not this "
                            "unit's to choose"},
        {"choice": "the link set", "value": str(links), "class": "FORCED",
         "fibre": 1, "why": "read from the anchored stage at PV-I7-LINKS; the "
                            "radius-1 ball containing it is measured"},
        {"choice": "the neighbourhood connective",
         "value": forced_connective, "class": "FORCED",
         "fibre": 1,
         "why": "FORCED by the anchored link set: the anchored diagonal link "
                "(1,1) has max-norm 1 and sum-norm 2, so it lies inside the "
                "max-norm radius-1 ball and outside the sum-norm one.  Exactly "
                "one of the two declared connectives can carry the stage's own "
                "links; the other is swept only to measure what it would have "
                "cost (threshold delta %d, admissible set %s)"
                % (delta, admissible_excluded)},
        {"choice": "the lattice size L", "value": str(admissible),
         "class": "FORCED", "fibre": len(admissible),
         "why": "measured: exactly one size in the swept range carries both "
                "locality and a non-monomial local axis"},
        {"choice": "the coefficient alphabet", "value": "25 elements",
         "class": "GENUINELY-FREE", "fibre": len(alphabet),
         "why": "declared; the sweep over it is exhaustive, and the collapse "
                "above order four is proved alphabet-independently"},
        {"choice": "the stencil", "value": "3-term axis {0, a, -a}",
         "class": "GENUINELY-FREE", "fibre": 2,
         "why": "free AT the admitted size and only there: the Moore-ball "
                "collapse theorem removes every non-monomial local stencil at "
                "L >= 5 over any field, but at L = 4 the 5-point stencil "
                "carries %d further non-monomial generators that this census "
                "does not examine" % fp4["non_monomial"]},
        {"choice": "the axis set", "value": "%d axes" % len(axes),
         "class": "FORCED", "fibre": len(axes),
         "why": "exhaustive: every nonzero offset modulo sign, %d of them "
                "local and %d non-local" % (n_local_ax, len(axes) - n_local_ax)},
        {"choice": "the global phase of a generator", "value": "gauge",
         "class": "STABILIZER-FIXED", "fibre": 8,
         "why": "the anchored outer-torus row makes the defect invariant; the "
                "orbit is free of size 8 and is self-tested"},
        {"choice": "the gauge representative", "value": "lexicographic minimum",
         "class": "STABILIZER-FIXED", "fibre": 8,
         "why": "any member of the orbit gives the same defect; verified by "
                "the gauge self-test"},
        {"choice": "the division-event times", "value": "{0, 2}, cut at 1",
         "class": "GENUINELY-FREE", "fibre": 1,
         "why": "declared, following the anchored framework: with t=1 a "
                "division event there is no cut to test"},
        {"choice": "the intermediate leg at the cut", "value": "B(V)",
         "class": "GENUINELY-FREE", "fibre": 1,
         "why": "the Born declaration; under it the shadow defect and the "
                "declared residual coincide"},
        {"choice": "the brickwork coin", "value": "the 2x2 Hadamard",
         "class": "GENUINELY-FREE", "fibre": 1,
         "why": "declared; the brickwork family is a transport control only"},
        {"choice": "the scramble permutations", "value": str(list(SCRAMBLE_SWAPS)),
         "class": "GENUINELY-FREE", "fibre": len(SCRAMBLE_SWAPS),
         "why": "declared; negative control only"},
        {"choice": "the symmetry group", "value": "anchored chart group, "
                                                  "extended by the square point group",
         "class": "GENUINELY-FREE", "fibre": 2,
         "why": "both are censused and both class counts are printed"},
        {"choice": "the prepared-state set", "value": "16 point masses, "
                                                      "uniform, wedge",
         "class": "GENUINELY-FREE", "fibre": 18,
         "why": "declared; the coefficient is shown state-independent and the "
                "observable state-dependent"},
    ]
    if mut("MUT-CHOICE-INVENTORY"):
        choice_rows = choice_rows[:-1]
    S["choice_inventory"] = choice_rows
    classes_present = {r["class"] for r in choice_rows}
    LD.gate("G-CHOICE-INVENTORY-COMPLETE",
            "every construction choice is inventoried and classed FORCED, "
            "STABILIZER-FIXED or GENUINELY-FREE with an exact fibre, and the "
            "fibres that are measurable agree with the measurement",
            len(choice_rows) == 15
            and classes_present == {"FORCED", "STABILIZER-FIXED", "GENUINELY-FREE"}
            and all(isinstance(r["fibre"], int) and r["fibre"] >= 1 for r in choice_rows)
            and [r for r in choice_rows if r["choice"] == "the axis set"][0]["fibre"] == len(axes)
            and [r for r in choice_rows if r["choice"] == "the coefficient alphabet"][0]["fibre"] == len(alphabet),
            "rows=%d classes=%s" % (len(choice_rows), sorted(classes_present)))

    # ---------------- transport / realization census ----------------------
    say("[4/12] the realization census")

    def shift(w):
        return {(IDX[addv(x, w)], IDX[x]): ONE for x in sites}

    SHIFTPERM = {w: tuple(IDX[addv(x, w)] for x in sites) for w in sites}

    def conj_shift(w, M):
        """conjugation by a site permutation is an index relabelling."""
        p = SHIFTPERM[w]
        return {(p[i], p[j]): v for (i, j), v in M.items()}

    def point_maps():
        """the square point group acting on offsets, and the anchored subgroup."""
        def rot(v):
            return ((-v[1]) % L, v[0] % L)

        def ref(v):
            return (v[0] % L, (-v[1]) % L)
        elems, names = [], []
        for r in range(4):
            for s in range(2):
                def f(v, r=r, s=s):
                    w = v
                    if s:
                        w = ref(w)
                    for _ in range(r):
                        w = rot(w)
                    return w
                elems.append(f)
                names.append("r%ds%d" % (r, s))
        return elems, names

    pelems, pnames = point_maps()
    swap_idx = pnames.index("r1s1")  # coordinate swap: the anchored relabelling

    PT_PERM = {pi: tuple(IDX[pelems[pi](x)] for x in sites)
               for pi in range(len(pelems))}

    def act_on_matrix(M, pi, w):
        """the point element acting on the MATRIX by relabelling its index
        pair; the transport verification's own route."""
        p = PT_PERM[pi]
        q = tuple(IDX[addv(sites[i], w)] for i in range(NS))
        return {(q[p[i]], q[p[j]]): v for (i, j), v in M.items()}

    trans_stab = {}
    for g in pool:
        st = [w for w in sites if conj_shift(w, g["mat"]) == g["mat"]]
        trans_stab[g["name"]] = len(st)

    def gauge_equiv_in_pool(c):
        key = tuple(sorted(c.items()))
        for t in range(8):
            k2 = tuple(sorted((o, cmul(zpow(t), v)) for o, v in key))
            if k2 in pool_keys:
                return True
        return False

    levels = {}
    for g in pool:
        st = trans_stab[g["name"]]
        if st == NS:
            lvl = "OCC+AXIS"
            if g["coef"] is not None:
                ok = True
                for f in pelems:
                    c2 = {f(o): v for o, v in g["coef"].items()}
                    if not gauge_equiv_in_pool(c2):
                        ok = False
                        break
                    if g["axis"] is not None:
                        img_ax = f(g["axis"])
                        if img_ax not in axes and smul(L - 1, img_ax) not in axes:
                            ok = False
                            break
                if ok:
                    lvl = "FULL"
        elif st > 1:
            lvl = "OCC"
        else:
            lvl = "NONE"
        levels[g["name"]] = lvl
    if mut("MUT-REALIZATION-PROMOTE"):
        for k in levels:
            levels[k] = "FULL"
    if mut("MUT-LEVEL-PROMOTE-ONE"):
        one = sorted(k for k, v in levels.items() if v != "FULL")[-1]
        levels[one] = "FULL"
    if mut("MUT-LEVEL-DEMOTE-ONE"):
        one = sorted(k for k, v in levels.items() if v == "FULL")[0]
        levels[one] = "OCC"
    S["transport_levels"] = {"declared": list(LEVELS),
                             "per_generator": {g["name"]: levels[g["name"]] for g in pool},
                             "translation_stabiliser": trans_stab,
                             "counts": {lv: sum(1 for v in levels.values() if v == lv)
                                        for lv in LEVELS}}
    LD.gate("G-REALIZATION-LEVELS",
            "the transport labels are well formed: every name is legal and "
            "there is exactly one per generator.  This row is a DISCLOSURE; the "
            "per-object obligation is discharged at the gate below",
            set(levels.values()) <= set(LEVELS)
            and len(levels) == len(pool),
            "counts %s" % S["transport_levels"]["counts"], kind="DISCLOSURE")

    # THE PER-OBJECT GATE (v14 #87: gates bind objects, not cardinalities).
    # Every individual classification is recomputed by a route that shares no
    # helper with the classifier: the stabiliser by explicit permutation-matrix
    # products rather than by index relabelling, and the covariance by acting on
    # the MATRIX and testing gauge-canonical membership rather than by acting on
    # the coefficient map.
    pool_canon = {canon_key_matrix(g["mat"]) for g in pool}
    check_levels = {}
    for g in pool:
        st2 = 0
        for w in sites:
            P = {(IDX[addv(x, w)], IDX[x]): ONE for x in sites}
            Pinv = {(j, i): v for (i, j), v in P.items()}
            if mat_mul(mat_mul(P, g["mat"], NS), Pinv, NS) == g["mat"]:
                st2 += 1
        if st2 == NS:
            lvl2 = "OCC+AXIS"
            ok2 = True
            for pi in range(len(pelems)):
                img = act_on_matrix(g["mat"], pi, (0, 0))
                if canon_key_matrix(img) not in pool_canon:
                    ok2 = False
                    break
            if ok2:
                lvl2 = "FULL"
        elif st2 > 1:
            lvl2 = "OCC"
        else:
            lvl2 = "NONE"
        check_levels[g["name"]] = lvl2
    mismatched = sorted(nm for nm in levels if levels[nm] != check_levels[nm])
    LD.gate("G-REALIZATION-LEVELS-PER-GENERATOR",
            "EVERY individual generator's transport classification is verified "
            "against its own computed invariant by an independent route: the "
            "translation stabiliser from explicit permutation-matrix products, "
            "the covariance from the matrix action's gauge-canonical membership "
            "in the pool.  A single promotion or demotion dies here",
            not mismatched and len(check_levels) == len(pool),
            "generators verified=%d mismatched=%s"
            % (len(check_levels), mismatched or "none"))
    S["transport_levels"]["verified_by_second_route"] = len(check_levels)
    maximal = max((lv for lv in LEVELS if any(v == lv for v in levels.values())),
                  key=lambda x: LEVELS.index(x))
    if mut("MUT-REALIZATION-EMPTY"):
        maximal = "OCC+AXIS"
    LD.gate("G-REALIZATION-MAXIMAL-NONEMPTY",
            "the maximal declared transport level is attained by at least one "
            "generator",
            sum(1 for v in levels.values() if v == maximal) > 0,
            "maximal=%s attained by %d generators"
            % (maximal, sum(1 for v in levels.values() if v == maximal)))
    S["maximal_transport"] = maximal

    # ---------------- the defect census -----------------------------------
    say("[5/12] the defect census over %d ordered pairs" % (len(pool) ** 2))
    LD.gate("G-DEFECT-DEFINITION-SHAPE",
            "the defect is reimplemented from the anchored definition: the Born "
            "shadow of the coherent composite minus the shadow restarted at the "
            "intermediate cut",
            True, "Delta^B(V,U) = B(VU) - B(V)B(U); consumer of VB-DEFECT-DEF",
            kind="DISCLOSURE")
    # the reimplementation is checked against the anchored source's OWN named
    # two-by-two witness (verbatim row VB-WITNESS-2X2): Delta(H,V) = 0 and
    # Delta(H,H) = [[1/2,-1/2],[-1/2,1/2]].
    Hm = {(0, 0): INV_SQ2, (0, 1): INV_SQ2, (1, 0): INV_SQ2, (1, 1): cneg(INV_SQ2)}
    Vm = {(0, 0): INV_SQ2, (0, 1): cmul(zpow(2), INV_SQ2),
          (1, 0): cmul(zpow(2), INV_SQ2), (1, 1): INV_SQ2}
    w_hv = defect_dense(Hm, Vm, 2)
    w_hh = defect_dense(Hm, Hm, 2)
    want_hh = {(0, 0): crat(1, 2), (0, 1): crat(-1, 2),
               (1, 0): crat(-1, 2), (1, 1): crat(1, 2)}
    if mut("MUT-DEFECT-WITNESS"):
        w_hh = {k: cneg(v) for k, v in w_hh.items()}
    LD.gate("G-DEFECT-DEFINITION",
            "the reimplemented defect reproduces the anchored source's own named "
            "two-by-two witness values exactly: it vanishes on the Hadamard "
            "against the unbiased V, and returns the half-magnitude alternating "
            "matrix on the Hadamard against itself",
            mat_is_unitary(Hm, 2) and mat_is_unitary(Vm, 2)
            and w_hv == {} and w_hh == want_hh,
            "Delta(H,V)=%s Delta(H,H)=%s"
            % ("0" if not w_hv else "NONZERO",
               "+".join(cstr(w_hh[k]) for k in sorted(w_hh))))
    cut_is_division = "1" in ARENA["division_events"].split("division events")[0]
    if mut("MUT-DIVISION-EVENTS"):
        cut_is_division = True
    LD.gate("G-DIVISION-EVENTS-DECLARED",
            "the division-event times are declared and the cut is not among "
            "them: t=0 and t=2 are division events, t=1 is not, and the defect "
            "measures the failure of the law of total probability across it",
            ARENA["division_events"].startswith("t = 0 and t = 2")
            and not cut_is_division,
            ARENA["division_events"], kind="DECLARED")

    rows = []
    route_mismatch, xt_mismatch, ft_mismatch = 0, 0, 0
    ft_checked, dense_checked, xt_checked = 0, 0, 0
    noncirc_defects = {}
    colsum_all_bad = 0
    for gv in pool:
        for gu in pool:
            circ = gv["coef"] is not None and gu["coef"] is not None
            sep = None
            if circ:
                dc = defect_conv(gv["coef"], gu["coef"], sites, subv)
                if mut("MUT-DEFECT-ZERO"):
                    dc = {}
                sep = dc
                dd = None
                if (gv["idx"] * 7 + gu["idx"]) % 5 == 0:
                    dense_checked += 1
                    if mut("MUT-DEFECT-ROUTE") and dense_checked == 3:
                        dc = dict(dc)
                        dc[(0, 0)] = cadd(dc.get((0, 0), ZERO), ONE)
                        sep = dc
                    dd = defect_dense(gv["mat"], gu["mat"], NS)
                    if mut("MUT-DEFECT-ZERO"):
                        dd = {}
                    folded = {}
                    consistent = True
                    for (i, j), v in dd.items():
                        s = subv(sites[i], sites[j])
                        if s in folded and folded[s] != v:
                            consistent = False
                        folded[s] = v
                    if not consistent or folded != dc:
                        route_mismatch += 1
                if (gv["idx"] * 3 + gu["idx"]) % 7 == 0:
                    xt_checked += 1
                    dx = defect_crossterms(gv["coef"], gu["coef"], sites, subv)
                    if mut("MUT-DEFECT-ZERO"):
                        dx = {}
                    if mut("MUT-DEFECT-XT") and xt_checked == 1:
                        dx = {}
                    if dx != dc:
                        xt_mismatch += 1
                nzc = len(dc)
                if (gv["idx"] + gu["idx"]) % 17 == 0:
                    ft_checked += 1
                    prod_ft = fourier_product_coefs(gv["coef"], gu["coef"], L, 2)
                    if mut("MUT-DEFECT-FOURIER") and ft_checked == 1:
                        prod_ft = {}
                    prod_cv = {}
                    for t, vt in gv["coef"].items():
                        for o, uo in gu["coef"].items():
                            k = addv(t, o)
                            prod_cv[k] = cadd(prod_cv.get(k, ZERO), cmul(vt, uo))
                    prod_cv = {k: v for k, v in prod_cv.items() if v != ZERO}
                    if prod_ft != prod_cv:
                        ft_mismatch += 1
            else:
                dd = defect_dense(gv["mat"], gu["mat"], NS)
                if mut("MUT-DEFECT-ZERO"):
                    dd = {}
                nzc = len(dd)
                noncirc_defects[(gv["name"], gu["name"])] = dd
                acc0 = {}
                for (i, j), v in dd.items():
                    acc0[j] = cadd(acc0.get(j, ZERO), v)
                if any(v != ZERO for v in acc0.values()):
                    colsum_all_bad += 1
            rows.append({"V": gv["name"], "U": gu["name"],
                         "circulant": circ,
                         "level": LEVELS[min(LEVELS.index(levels[gv["name"]]),
                                             LEVELS.index(levels[gu["name"]]))],
                         "monomial_factor": bool(gv["monomial"] or gu["monomial"]),
                         "radius": max(gv["radius"], gu["radius"]),
                         "local": gv["radius"] <= 1 and gu["radius"] <= 1,
                         "nonzero_cells": nzc,
                         "separations": (sorted([list(k) for k in sep]) if sep is not None else None),
                         "values": ([cstr(sep[k]) for k in sorted(sep)] if sep is not None else None),
                         "rational": ([crational(sep[k]) is not None for k in sorted(sep)]
                                      if sep is not None else None),
                         "defect": sep})
    if mut("MUT-ROW-DROP"):
        rows = rows[:-1]
    LD.gate("G-ROW-COMPLETENESS",
            "the census has one row per ordered pair of pool generators, the "
            "count derived from the pool",
            len(rows) == len(pool) ** 2,
            "rows=%d expected=%d" % (len(rows), len(pool) ** 2))
    LD.gate("G-DEFECT-ROUTES-AGREE",
            "the definitional route on sparse matrices and the separation-"
            "indexed convolution route agree on the declared verification "
            "subset of circulant pairs (stride 5 of the ordered census)",
            route_mismatch == 0 and dense_checked > 0,
            "checked=%d mismatches=%d" % (dense_checked, route_mismatch))
    LD.gate("G-DEFECT-CLOSED-FORM",
            "the closed cross-term form reproduces the definition on the "
            "declared subset (FORCED: the two are algebraically identical, so "
            "this is an implementation check, not a second measurement)",
            xt_mismatch == 0 and xt_checked > 0,
            "checked=%d mismatches=%d" % (xt_checked, xt_mismatch), kind="FORCED")
    LD.gate("G-DEFECT-FOURIER-AGREE",
            "the character-basis product agrees with the position-space "
            "convolution on the declared verification subset",
            ft_mismatch == 0 and ft_checked > 0,
            "checked=%d mismatches=%d" % (ft_checked, ft_mismatch))

    nz = [r for r in rows if r["nonzero_cells"] > 0]
    LD.gate("G-DEFECT-NONZERO-EXISTS",
            "the positive control: the instrument does find nonzero defects",
            len(nz) > 0, "nonzero pairs=%d of %d" % (len(nz), len(rows)))

    # the value census -- defect gates are bound to exact values (the R3 Y1 lesson)
    value_rows = []
    nz_circ = [r for r in nz if r["defect"] is not None]
    for r in sorted(nz_circ, key=lambda r: (r["V"], r["U"]))[:DEFECT_VALUE_CENSUS_ROWS]:
        vals = [(list(k), cstr(r["defect"][k]), crational(r["defect"][k]))
                for k in sorted(r["defect"])]
        value_rows.append({"V": r["V"], "U": r["U"], "cells": vals})
    if mut("MUT-DEFECT-CENSUS-ZERO"):
        value_rows = [{"V": vr["V"], "U": vr["U"], "cells": []} for vr in value_rows]
    if mut("MUT-DEFECT-VALUE") and value_rows:
        value_rows[0]["cells"][0] = [value_rows[0]["cells"][0][0], "+0", "0"]
    recomputed = []
    for vr in value_rows:
        gv = [g for g in pool if g["name"] == vr["V"]][0]
        gu = [g for g in pool if g["name"] == vr["U"]][0]
        dd = defect_dense(gv["mat"], gu["mat"], NS)
        fold = {}
        for (i, j), v in dd.items():
            fold[subv(sites[i], sites[j])] = v
        recomputed.append([(list(k), cstr(fold[k]), crational(fold[k]))
                           for k in sorted(fold)])
    ok_values = (len(value_rows) == DEFECT_VALUE_CENSUS_ROWS
                 and all([tuple(map(tuple, [c[0] for c in vr["cells"]])) ==
                          tuple(map(tuple, [c[0] for c in rc]))
                          and [c[1] for c in vr["cells"]] == [c[1] for c in rc]
                          for vr, rc in zip(value_rows, recomputed)])
                 and all(len(vr["cells"]) > 0 for vr in value_rows))
    LD.gate("G-DEFECT-VALUE-CENSUS",
            "the defect census is bound to exact values: every censused cell is "
            "reproduced by an independent recomputation, and a zeroed or altered "
            "defect dies here",
            ok_values,
            "rows=%d cells=%d" % (len(value_rows), sum(len(v["cells"]) for v in value_rows)))
    S["defect_value_census"] = value_rows

    # THE Y1 LESSON AT CENSUS SCALE (v14 #87).  Twelve named rows bind twelve
    # rows; the census is bound when the WHOLE value multiset is bound.  The
    # comparison is against a second code path (the cross-term form), and the
    # multiset carries its own zero-sum identity.
    by_name = {g["name"]: g for g in pool}
    if mut("MUT-Y1-UNCENSUSED-ZERO"):
        censused = {(vr["V"], vr["U"]) for vr in value_rows}
        for r in rows:
            if r["defect"] and (r["V"], r["U"]) not in censused:
                r["defect"] = {}
                r["values"] = []
                r["separations"] = []
                r["rational"] = []
                r["nonzero_cells"] = 0
    at_max_rows = [r for r in rows if r["level"] == maximal]
    full_counts, zsum = {}, ZERO
    for r in at_max_rows:
        if r["values"]:
            for v in r["values"]:
                full_counts[v] = full_counts.get(v, 0) + 1
        if r["defect"]:
            for v in r["defect"].values():
                zsum = cadd(zsum, v)
    recomp_counts = {}
    recomp_rows = 0
    for r in at_max_rows:
        gv2, gu2 = by_name[r["V"]], by_name[r["U"]]
        if gv2["coef"] is None or gu2["coef"] is None:
            continue
        recomp_rows += 1
        dx = defect_crossterms(gv2["coef"], gu2["coef"], sites, subv)
        for k in sorted(dx):
            sv = cstr(dx[k])
            recomp_counts[sv] = recomp_counts.get(sv, 0) + 1
    if mut("MUT-VALUE-MULTISET"):
        full_counts = dict(full_counts)
        full_counts[sorted(full_counts)[0]] += 1
    LD.gate("G-DEFECT-VALUE-CENSUS-FULL",
            "the WHOLE value multiset of the verdict-bearing census -- every "
            "distinct exact value with its cell count -- is bound against a "
            "recomputation by a second code path, and the multiset carries its "
            "own exact zero-sum identity.  Zeroing any row, censused or not, "
            "dies here",
            full_counts == recomp_counts and zsum == ZERO
            and recomp_rows == len(at_max_rows) and len(full_counts) > 0,
            "values=%d rows recomputed=%d of %d; multiset equal=%s; sum of all "
            "cells=%s" % (len(full_counts), recomp_rows, len(at_max_rows),
                          full_counts == recomp_counts, cstr(zsum)))
    S["defect_value_multiset"] = [{"value": k, "cells": full_counts[k]}
                                  for k in sorted(full_counts)]

    colsum_bad = 0
    colsum_checked = 0
    for r in rows:
        if r["defect"] is None:
            continue
        colsum_checked += 1
        acc = ZERO
        for k, v in r["defect"].items():
            acc = cadd(acc, v)
        if acc != ZERO:
            colsum_bad += 1
    colsum_bad += colsum_all_bad
    colsum_checked += len(noncirc_defects)
    if mut("MUT-COLUMN-SUM"):
        colsum_bad = 1
    LD.gate("G-DEFECT-COLUMN-SUMS",
            "each defect column sums to zero -- both composites are stochastic. "
            "FORCED (|U| entrywise-squared is doubly stochastic for unitary U); "
            "the check is widened from a 64-row sample to EVERY census row so "
            "the evidence matches the claim",
            colsum_bad == 0 and colsum_checked == len(rows),
            "violations=%d over %d of %d census rows"
            % (colsum_bad, colsum_checked, len(rows)), kind="DISCLOSURE")

    # ---------------- the Markovian control -------------------------------
    say("[6/12] the Markovian control and the defect algebra")
    mono_names = {g["name"] for g in pool if g["monomial"]}
    if mut("MUT-MARKOV-LABEL"):
        two = [g for g in pool if g["support"] == 2][0]
        mono_names = mono_names | {two["name"]}
    classifier_ok = all((g["support"] is not None and (g["support"] <= 1) == (g["name"] in mono_names))
                        or g["support"] is None for g in pool)
    LD.gate("G-MARKOV-CLASSIFIER",
            "the Markovian sub-family is classified by measured support size, "
            "never by a typed label",
            classifier_ok, "monomial generators=%d" % len(mono_names))
    mk = [r for r in rows if r["V"] in mono_names or r["U"] in mono_names]
    mk_nonzero = [r for r in mk if r["nonzero_cells"] > 0]
    if mut("MUT-MARKOV-NONZERO"):
        mk_nonzero = mk[:1]
    LD.gate("G-MARKOV-ZERO",
            "the Markovian sub-family returns a strictly zero defect: every pair "
            "with a monomial factor has an empty pairwise sum (the anchored "
            "annihilator theorem, measured here)",
            len(mk_nonzero) == 0 and len(mk) > 0,
            "%d of %d Markovian pairs nonzero" % (len(mk_nonzero), len(mk)))

    # the same claim, keyed on the OBJECT rather than on its count (v14 #87).
    # "the pairwise sum through the cut is literally empty" is a statement about
    # the defect dictionaries, so the gate reads the dictionaries.
    mk_obj_bad, mk_obj_checked = [], 0
    for r in mk:
        if r["defect"] is not None:
            obj = r["defect"]
        else:
            obj = noncirc_defects.get((r["V"], r["U"]))
            if obj is None:
                gvx = [g for g in pool if g["name"] == r["V"]][0]
                gux = [g for g in pool if g["name"] == r["U"]][0]
                obj = defect_dense(gvx["mat"], gux["mat"], NS)
        mk_obj_checked += 1
        if mut("MUT-MARKOV-OBJECT") and mk_obj_checked == 1:
            obj = {(0, 0): ONE}
        if obj:
            mk_obj_bad.append((r["V"], r["U"], len(obj)))
    LD.gate("G-MARKOV-ZERO-OBJECT",
            "the Markovian zero is bound to the defect OBJECT and not to a "
            "count: every one of the Markovian rows' defect dictionaries is "
            "read and is literally empty",
            not mk_obj_bad and mk_obj_checked == len(mk),
            "objects read=%d of %d Markovian rows; non-empty=%s"
            % (mk_obj_checked, len(mk), mk_obj_bad[:3] or "none"))
    free_pairs = [r for r in rows if r["V"] not in mono_names and r["U"] not in mono_names]
    free_nz = [r for r in free_pairs if r["nonzero_cells"] > 0]
    if mut("MUT-MARKOV-NOPOS"):
        free_nz = []
    LD.gate("G-MARKOV-POSITIVE-CONTROL",
            "the same instrument returns nonzero on the free sub-family, so the "
            "Markovian zero is a measurement and not an artefact",
            len(free_nz) > 0,
            "%d of %d free pairs nonzero" % (len(free_nz), len(free_pairs)))
    S["markov_control"] = {"monomial_generators": sorted(mono_names),
                           "markov_pairs": len(mk), "markov_nonzero": len(mk_nonzero),
                           "free_pairs": len(free_pairs), "free_nonzero": len(free_nz)}

    # the coherence law on declared triples
    circ_pool = [g for g in pool if g["coef"] is not None]
    tri_bad, tri_n = 0, 0
    for i in range(len(circ_pool)):
        for j in range(len(circ_pool)):
            k = (i + 2 * j) % len(circ_pool)
            if tri_n >= COHERENCE_TRIPLES:
                break
            U3, U2, U1 = circ_pool[i], circ_pool[j], circ_pool[k]
            tri_n += 1
            m32 = mat_mul(U3["mat"], U2["mat"], NS)
            m21 = mat_mul(U2["mat"], U1["mat"], NS)
            lhs = mat_sub(defect_dense(m32, U1["mat"], NS),
                          mat_sub({}, mat_mul(defect_dense(U3["mat"], U2["mat"], NS),
                                              mat_born(U1["mat"]), NS)))
            rhs = mat_sub(defect_dense(U3["mat"], m21, NS),
                          mat_sub({}, mat_mul(mat_born(U3["mat"]),
                                              defect_dense(U2["mat"], U1["mat"], NS), NS)))
            if mut("MUT-COHERENCE") and tri_n == 1:
                rhs = dict(rhs)
                rhs[(0, 0)] = cadd(rhs.get((0, 0), ZERO), ONE)
            if lhs != rhs:
                tri_bad += 1
        if tri_n >= COHERENCE_TRIPLES:
            break
    LD.gate("G-COHERENCE-LAW",
            "the coherence law holds on the declared triples (FORCED: it is an "
            "identity of associativity and constrains the family not at all -- "
            "carried as an implementation check)",
            tri_bad == 0, "triples=%d violations=%d" % (tri_n, tri_bad), kind="FORCED")
    S["coherence"] = {"triples": tri_n, "violations": tri_bad}

    # the defect algebra: normalization, equivariance, reversal
    ident = [g for g in pool if g["monomial"] and g["coef"] and list(g["coef"]) == [(0, 0)]]
    Iden = mat_id(NS)
    norm_bad = sum(1 for g in circ_pool[:20]
                   if defect_dense(Iden, g["mat"], NS) or defect_dense(g["mat"], Iden, NS))
    if mut("MUT-NORMALIZATION"):
        norm_bad = 1
    LD.gate("G-DEFECT-NORMALIZATION",
            "the defect vanishes against the identity on both sides",
            norm_bad == 0, "violations=%d" % norm_bad)
    eq_bad, eq_n = 0, 0
    for w in sites[:2]:
        P = shift(w)
        for g1 in circ_pool[:4]:
            for g2 in circ_pool[:4]:
                eq_n += 1
                lhs = defect_dense(mat_mul(P, g1["mat"], NS), mat_mul(g2["mat"], P, NS), NS)
                rhs = mat_mul(mat_mul(P, defect_dense(g1["mat"], g2["mat"], NS), NS), P, NS)
                if lhs != rhs:
                    eq_bad += 1
    if mut("MUT-EQUIVARIANCE"):
        eq_bad = 1
    LD.gate("G-DEFECT-EQUIVARIANCE",
            "permutation equivariance holds: conjugating the pair by a site "
            "permutation conjugates the defect",
            eq_bad == 0, "checked=%d violations=%d" % (eq_n, eq_bad))
    rev_bad, rev_n = 0, 0
    for g1 in circ_pool[:8]:
        for g2 in circ_pool[:8]:
            rev_n += 1
            t = lambda M: {(j, i): v for (i, j), v in M.items()}
            lhs = t(defect_dense(g1["mat"], g2["mat"], NS))
            rhs = defect_dense(t(g2["mat"]), t(g1["mat"]), NS)
            if lhs != rhs:
                rev_bad += 1
    if mut("MUT-REVERSAL"):
        rev_bad = 1
    LD.gate("G-DEFECT-REVERSAL",
            "reversal covariance holds: transposing the defect reverses the pair",
            rev_bad == 0, "checked=%d violations=%d" % (rev_n, rev_bad))

    # the symmetry self-test (RUNBOOK section 14), cache bypassed
    MULCACHE.clear()
    CACHE_STATS["hits"] = 0
    CACHE_STATS["misses"] = 0
    gauge_bad, gauge_n = 0, 0
    for t in range(8):
        z = zpow(t)
        for g1 in circ_pool[:5]:
            for g2 in circ_pool[:5]:
                gauge_n += 2
                D1 = {(i, i): z for i in range(NS)}
                base = defect_dense(g1["mat"], g2["mat"], NS)
                lhs = defect_dense(mat_mul(D1, g1["mat"], NS), g2["mat"], NS)
                rhs = defect_dense(g1["mat"], mat_mul(g2["mat"], D1, NS), NS)
                if mut("MUT-GAUGE-SELFTEST") and gauge_n == 6:
                    lhs = {}
                if mut("MUT-GAUGE-SELFTEST-RIGHT") and gauge_n == 6:
                    rhs = {}
                fresh = {k: cmul_fresh(v, ONE) for k, v in base.items()}
                if lhs != base or rhs != base or fresh != base:
                    gauge_bad += 1
    LD.gate("G-GAUGE-SELFTEST",
            "the quantity is invariant under the symmetry it claims, on BOTH "
            "factors: a global phase on the left factor and a global phase on "
            "the right factor each leave the defect fixed, evaluated with the "
            "product cache cleared and a cache-free recomputation alongside",
            gauge_bad == 0, "directions checked=%d violations=%d"
            % (gauge_n, gauge_bad))
    handle_moves = 0
    for g1 in circ_pool[:6]:
        for g2 in circ_pool[:6]:
            D = {(i, i): zpow(2 * i) for i in range(NS)}
            if defect_dense(mat_mul(g1["mat"], D, NS), g2["mat"], NS) != \
               defect_dense(g1["mat"], g2["mat"], NS):
                handle_moves += 1
    if mut("MUT-GAUGE-HANDLE"):
        handle_moves = 0
    LD.gate("G-GAUGE-HANDLE",
            "the negative direction of the same self-test: the one handle (an "
            "inner diagonal at the cut) does move the defect, so the invariance "
            "gate is not vacuous",
            handle_moves > 0, "pairs moved=%d" % handle_moves)
    cache_hits, cache_misses = CACHE_STATS["hits"], CACHE_STATS["misses"]
    if mut("MUT-CACHE"):
        cache_hits = 0
    LD.gate("G-CACHE-EXERCISED",
            "the product cache is genuinely exercised and its hit path is "
            "non-vacuous (#219)",
            cache_hits > 0 and cache_misses > 0,
            "hits=%d misses=%d" % (cache_hits, cache_misses))

    # ---------------- locality dependence ---------------------------------
    say("[7/12] locality dependence and the two-point structure")
    full_rows = [r for r in rows if r["level"] == maximal]
    loc_split = {}
    for tag, pred in (("LOCAL", lambda r: r["local"]),
                      ("NONLOCAL", lambda r: not r["local"])):
        sel = [r for r in full_rows if pred(r) and not r["monomial_factor"]]
        loc_split[tag] = {"pairs": len(sel),
                          "nonzero": sum(1 for r in sel if r["nonzero_cells"] > 0),
                          "max_defect_radius": max([max([torus_absmax(tuple(s), L)
                                                         for s in r["separations"]] or [0])
                                                    for r in sel if r["separations"]] or [0])}
    if mut("MUT-LOCALITY-EMPTY"):
        loc_split["NONLOCAL"] = dict(loc_split["NONLOCAL"], pairs=0)
    LD.gate("G-LOCALITY-DEPENDENCE",
            "the defect's response to locality is measured, not assumed: both "
            "the local and the non-local sub-censuses are non-empty and their "
            "nonzero fractions are printed",
            loc_split["LOCAL"]["pairs"] > 0 and loc_split["NONLOCAL"]["pairs"] > 0,
            "%s" % loc_split)
    S["locality_dependence"] = loc_split

    # like-for-like: match every coordinate (coefficient class, axis order,
    # gauge fixing) and vary only the radius
    def coefclass(g):
        return tuple(sorted(cstr(v) for v in g["coef"].values())) if g["coef"] else None
    def axisclass(g):
        """the FULL gauge class relative to the axis: which offset carries
        which value, read in axis coordinates.  Unlike the value multiset this
        holds the gauge fixing equal."""
        if not g["coef"] or g["axis"] is None:
            return None
        a = g["axis"]
        lab = {(0, 0): "0", a: "+a", smul(L - 1, a): "-a"}
        return tuple(sorted((lab.get(o, "?"), cstr(v)) for o, v in g["coef"].items()))

    loc4 = [g for g in pool if g["kind"] == "CIRC" and g["axis_ord"] == 4 and g["radius"] == 1]
    nl4 = [g for g in pool if g["kind"] == "CIRC" and g["axis_ord"] == 4 and g["radius"] > 1]
    matched, matched_agree = 0, 0
    distinct_comparisons = {}
    for gv in loc4:
        for gu in loc4:
            partner_v = [h for h in nl4 if coefclass(h) == coefclass(gv)]
            partner_u = [h for h in nl4 if coefclass(h) == coefclass(gu)]
            if not partner_v or not partner_u:
                continue
            matched += 1
            key = (partner_v[0]["name"], partner_u[0]["name"])
            distinct_comparisons[key] = distinct_comparisons.get(key, 0) + 1
            a = defect_conv(gv["coef"], gu["coef"], sites, subv)
            b = defect_conv(partner_v[0]["coef"], partner_u[0]["coef"], sites, subv)
            if sorted(cstr(v) for v in a.values()) == sorted(cstr(v) for v in b.values()):
                matched_agree += 1
    # the SECOND matching, on the full axis-relative gauge class rather than on
    # the value multiset: the coordinate the first matching does not hold equal.
    gmatched, gmatched_agree = 0, 0
    gdistinct = set()
    for gv in loc4:
        for gu in loc4:
            pv = [h for h in nl4 if axisclass(h) == axisclass(gv)]
            pu = [h for h in nl4 if axisclass(h) == axisclass(gu)]
            if not pv or not pu:
                continue
            gmatched += 1
            gdistinct.add((pv[0]["name"], pu[0]["name"]))
            a = defect_conv(gv["coef"], gu["coef"], sites, subv)
            b = defect_conv(pv[0]["coef"], pu[0]["coef"], sites, subv)
            if sorted(cstr(v) for v in a.values()) == sorted(cstr(v) for v in b.values()):
                gmatched_agree += 1
    if mut("MUT-MATCHED-EMPTY"):
        matched = 0
    LD.gate("G-LOCALITY-LIKE-FOR-LIKE",
            "the local/non-local contrast is read at matched coordinates -- same "
            "coefficient value multiset, same axis order -- and the matched "
            "table is the primary object",
            matched > 0,
            "matched pairs=%d value-multiset agreements=%d" % (matched, matched_agree))
    mult = {}
    for v in distinct_comparisons.values():
        mult[v] = mult.get(v, 0) + 1
    n_distinct = len(distinct_comparisons)
    if mut("MUT-MATCHED-DISTINCT"):
        n_distinct = matched
    LD.gate("G-LIKE-FOR-LIKE-DISTINCT",
            "the matched count is WEIGHTED: the matching selects a partner by "
            "coefficient value multiset, so the ordered comparisons resolve to a "
            "smaller number of DISTINCT non-local comparisons with measured "
            "multiplicities, and both numbers are reported.  A second matching "
            "on the full axis-relative gauge class -- the coordinate the first "
            "does not hold equal -- is measured alongside",
            0 < n_distinct < matched
            and sum(k * v for k, v in mult.items()) == matched
            and gmatched > 0 and len(gdistinct) > n_distinct,
            "value-multiset matching: %d ordered comparisons drawn from %d "
            "distinct non-local pairs, multiplicities %s; gauge-class matching: "
            "%d ordered comparisons from %d distinct pairs, %d agreements"
            % (matched, n_distinct,
               {k: v for k, v in sorted(mult.items(), reverse=True)},
               gmatched, len(gdistinct), gmatched_agree))
    S["like_for_like"] = {"matched_pairs": matched,
                          "value_multiset_agreements": matched_agree,
                          "distinct_comparisons": n_distinct,
                          "multiplicities": {str(k): v for k, v
                                             in sorted(mult.items(), reverse=True)},
                          "matching_species": "coefficient value multiset",
                          "gauge_class_matched_pairs": gmatched,
                          "gauge_class_distinct_comparisons": len(gdistinct),
                          "gauge_class_agreements": gmatched_agree}
    if mut("MUT-NONLOCAL-RADIUS"):
        nl4 = []
    LD.gate("G-NONLOCAL-CONTROL",
            "the non-local control exists in the pool with a measured radius "
            "above the neighbourhood",
            len(nl4) > 0 and all(g["radius"] > 1 for g in nl4),
            "non-local generators=%d radii=%s"
            % (len(nl4), sorted({g["radius"] for g in nl4})))

    # ---------------- two-point structure ---------------------------------
    covariant = {g["name"]: (trans_stab[g["name"]] == NS) for g in pool}
    if mut("MUT-COVARIANCE"):
        covariant[[g for g in pool if g["kind"] == "BRICK"][0]["name"]] = True
    if mut("MUT-SCRAMBLE"):
        covariant[[g for g in pool if g["kind"] == "SCRAM"][0]["name"]] = True
    circ_cov = (all(covariant[g["name"]] for g in pool if g["kind"] == "CIRC")
                and not any(covariant[g["name"]] for g in pool if g["kind"] != "CIRC"))
    LD.gate("G-TWOPOINT-TRANSLATION-COVARIANT",
            "the two-point tables of the declared family are functions of the "
            "lattice separation alone: every circulant generator has the full "
            "translation group as its stabiliser, and its defect folds without "
            "conflict",
            circ_cov and route_mismatch == 0,
            "covariant circulants=%d of %d"
            % (sum(1 for g in pool if g["kind"] == "CIRC" and covariant[g["name"]]), n_circ))
    scram = [g for g in pool if g["kind"] == "SCRAM"]
    scram_broken = sum(1 for g in scram if not covariant[g["name"]])
    S["covariance_reading"] = {g["name"]: covariant[g["name"]] for g in pool}
    def is_separation_table(M):
        """a table is a function of separation iff every separation class is
        either wholly present with one value or wholly absent -- folding without
        a value conflict is NOT sufficient, because a partial class also folds."""
        val = {}
        for (i, j), v in M.items():
            s = subv(sites[i], sites[j])
            if s in val and val[s] != v:
                return False
            val[s] = v
        cnt = {}
        for (i, j) in M:
            s = subv(sites[i], sites[j])
            cnt[s] = cnt.get(s, 0) + 1
        return all(n == NS for n in cnt.values())

    probes = [g for g in circ_pool if g["support"] == 3]
    circ_sep_tables = sum(1 for g in circ_pool if is_separation_table(mat_born(g["mat"])))
    scram_born_sep = sum(1 for g in scram if is_separation_table(mat_born(g["mat"])))
    if mut("MUT-SCRAMBLE-SEPTABLE"):
        scram_born_sep = len(scram)
    scram_probe_total, scram_probe_fails, scram_probe_zero = 0, 0, 0
    for g in scram:
        for p in probes:
            scram_probe_total += 1
            dd = defect_dense(g["mat"], p["mat"], NS)
            if not dd:
                scram_probe_zero += 1
            elif not is_separation_table(dd):
                scram_probe_fails += 1
    LD.gate("G-TWOPOINT-SCRAMBLE-BREAKS",
            "the negative control: the scrambled lattice breaks translation "
            "covariance measurably; its transition table stops being a function "
            "of separation, and every one of its NONZERO defect tables stops "
            "being a separation table -- while every circulant's transition "
            "table still is one",
            scram_broken == len(scram) and scram_born_sep == 0
            and scram_probe_fails == scram_probe_total - scram_probe_zero
            and scram_probe_fails > 0
            and circ_sep_tables == len(circ_pool),
            "covariance broken=%d of %d; scrambled transition tables that are "
            "separation tables=%d; nonzero scrambled defect tables that fail="
            "%d of %d (with %d identically zero); circulant transition tables "
            "that pass=%d of %d"
            % (scram_broken, len(scram), scram_born_sep, scram_probe_fails,
               scram_probe_total - scram_probe_zero, scram_probe_zero,
               circ_sep_tables, len(circ_pool)))
    S["scramble_control"] = {"generators": len(scram),
                             "covariance_broken": scram_broken,
                             "transition_tables_separation_indexed": scram_born_sep,
                             "defect_table_failures": scram_probe_fails,
                             "defect_probes": scram_probe_total,
                             "defect_probes_identically_zero": scram_probe_zero,
                             "circulant_transition_tables_passing": circ_sep_tables}

    # equal-time connected correlator on the declared uniform state
    unif = crat(1, NS)
    eq_time = {}
    for s in sites:
        val = csub(unif if not any(s) else ZERO, cmul(unif, unif))
        eq_time[s] = val
    if mut("MUT-EQUAL-TIME"):
        eq_time[(1, 0)] = ONE
    LD.gate("G-TWOPOINT-EQUAL-TIME",
            "the equal-time connected correlator of the occupation observable is "
            "computed exactly and depends on the separation alone",
            eq_time[(0, 0)] == csub(unif, cmul(unif, unif))
            and len({cstr(v) for k, v in eq_time.items() if any(k)}) == 1,
            "C0(0)=%s C0(s!=0)=%s" % (cstr(eq_time[(0, 0)]), cstr(eq_time[(1, 0)])))
    S["equal_time"] = {"C0_at_zero": cstr(eq_time[(0, 0)]),
                       "C0_at_nonzero": cstr(eq_time[(1, 0)]),
                       "rational_zero": crational(eq_time[(0, 0)]),
                       "rational_nonzero": crational(eq_time[(1, 0)])}

    # composed-time: coherent minus restarted equals the defect times the state
    probe_pairs = [(circ_pool[i], circ_pool[(3 * i + 1) % len(circ_pool)])
                   for i in range(0, len(circ_pool), 3)]
    comp_bad = 0
    profiles = []
    for gv, gu in probe_pairs:
        coh = mat_born(mat_mul(gv["mat"], gu["mat"], NS))
        div = mat_mul(mat_born(gv["mat"]), mat_born(gu["mat"]), NS)
        dif = mat_sub(coh, div)
        if dif != defect_dense(gv["mat"], gu["mat"], NS):
            comp_bad += 1
        prof = defect_conv(gv["coef"], gu["coef"], sites, subv)
        profiles.append({"V": gv["name"], "U": gu["name"],
                         "separations": sorted([list(k) for k in prof]),
                         "values": [cstr(prof[k]) for k in sorted(prof)]})
    if mut("MUT-COMPOSED"):
        comp_bad = 1
    LD.gate("G-TWOPOINT-COMPOSED",
            "the composed-time two-point table splits exactly into the restarted "
            "table plus the defect: the defect IS the interference part of the "
            "two-time correlator",
            comp_bad == 0, "probe pairs=%d violations=%d" % (len(probe_pairs), comp_bad))
    S["two_point_profiles"] = profiles

    stoch_bad = 0
    for g in pool[:20]:
        B = mat_born(g["mat"])
        for j in range(NS):
            acc = ZERO
            for i in range(NS):
                acc = cadd(acc, B.get((i, j), ZERO))
            if acc != ONE:
                stoch_bad += 1
    if mut("MUT-STOCHASTIC"):
        stoch_bad = 1
    LD.gate("G-TWOPOINT-STOCHASTIC",
            "every Born shadow is a column-stochastic transition matrix",
            stoch_bad == 0, "violations=%d" % stoch_bad)

    # light cone and periodicity.  The RAW order of U is not gauge invariant
    # (a global phase rescales every power); the PROJECTIVE period -- the least
    # k with U^k a scalar -- is, and it is the period this unit reports.
    cone, orders, orders_raw = [], {}, {}
    for g in circ_pool:
        c, radii = dict(g["coef"]), []
        cur = dict(c)
        for n in range(1, 5):
            radii.append(max([torus_absmax(o, L) for o in cur] or [0]))
            nxt = {}
            for a1, v1 in cur.items():
                for a2, v2 in c.items():
                    k = addv(a1, a2)
                    nxt[k] = cadd(nxt.get(k, ZERO), cmul(v1, v2))
            cur = {k: v for k, v in nxt.items() if v != ZERO}
        cone.append({"gen": g["name"], "radius_by_step": radii,
                     "single_step_radius": g["radius"]})
        Mt, P, o, po = g["mat"], g["mat"], None, None
        for k in range(1, 49):
            if o is None and P == mat_id(NS):
                o = k
            if po is None and is_scalar(P, NS):
                po = k
            if o is not None and po is not None:
                break
            P = mat_mul(P, Mt, NS)
        orders_raw[g["name"]] = o
        orders[g["name"]] = po
    if mut("MUT-LIGHTCONE"):
        cone[0]["radius_by_step"] = [0, 0, 0, 0]
    if mut("MUT-PERIOD"):
        k0 = sorted(orders)[0]
        orders[k0] = 3
    # the symmetry self-test for the period: the projective period is invariant
    # under the declared global-phase gauge, and the raw order is not
    proj_inv, raw_moves = 0, 0
    for g in circ_pool[:6]:
        for t in range(1, 8):
            z = zpow(t)
            Mz = {k: cmul(z, v) for k, v in g["mat"].items()}
            po, ro = None, None
            P = Mz
            for k in range(1, 49):
                if ro is None and P == mat_id(NS):
                    ro = k
                if po is None and is_scalar(P, NS):
                    po = k
                if po is not None and ro is not None:
                    break
                P = mat_mul(P, Mz, NS)
            if po == orders[g["name"]]:
                proj_inv += 1
            if ro != orders_raw[g["name"]]:
                raw_moves += 1
    cone_ok = all(
        all(row["radius_by_step"][n] <= min((n + 1) * row["single_step_radius"], L // 2)
            for n in range(4))
        and row["radius_by_step"][0] == row["single_step_radius"]
        for row in cone)
    cone_saturates = sum(1 for row in cone if max(row["radius_by_step"]) == L // 2)
    LD.gate("G-TWOPOINT-LIGHTCONE",
            "the support of the composed propagator starts at the generator's "
            "own radius and spreads no faster than one neighbourhood per step, "
            "bounded by the lattice half-width.  DISCLOSURE: at the admitted "
            "size the bound is vacuous above radius 0 -- see the gate below",
            cone_ok, "generators=%d max radius=%d attaining the half-width=%d"
            % (len(cone), max(max(r["radius_by_step"]) for r in cone),
               cone_saturates), kind="DISCLOSURE")

    # HOW MUCH CONTENT the cone bound has at this size, measured exhaustively
    # over every conceivable profile rather than asserted.
    violators = {}
    for prof in product(range(L // 2 + 1), repeat=4):
        r0 = prof[0]
        bad = any(prof[n] > min((n + 1) * r0, L // 2) for n in range(4))
        if bad:
            violators[r0] = violators.get(r0, 0) + 1
    radii_present = sorted({row["single_step_radius"] for row in cone})
    content_radii = sorted(violators)
    if mut("MUT-LIGHTCONE-VACUITY"):
        content_radii = radii_present
    LD.gate("G-LIGHTCONE-VACUITY-MEASURED",
            "the cone bound's content is measured, not assumed: over every "
            "conceivable radius profile at this lattice size the bound can fail "
            "only at single-step radius 0, so for every generator of radius >= 1 "
            "the clause is forced and the verdict must say so",
            content_radii == [0] and len(violators) == 1,
            "profiles swept=%d; single-step radii at which the bound can fail "
            "at all=%s (violating profiles by radius %s); single-step radii "
            "present in the family=%s"
            % ((L // 2 + 1) ** 4, content_radii,
               {k: v for k, v in sorted(violators.items())}, radii_present))
    S["lightcone_vacuity"] = {"profiles_swept": (L // 2 + 1) ** 4,
                              "radii_with_content": content_radii,
                              "violating_profiles": {str(k): v for k, v
                                                     in sorted(violators.items())},
                              "radii_present": radii_present}

    # the MEASURED content the verdict carries in its place.
    prof_counts = {}
    for row in cone:
        prof_counts[tuple(row["radius_by_step"])] = \
            prof_counts.get(tuple(row["radius_by_step"]), 0) + 1
    n_profiles = len(prof_counts)
    if mut("MUT-RADIUS-PROFILES"):
        n_profiles = 1
    LD.gate("G-TWOPOINT-RADIUS-PROFILES",
            "the measurement the cone bound is not: the composed propagator's "
            "radius profile over the first four powers is censused, several "
            "distinct profiles occur, and the half-width is attained by some "
            "generators and not by all",
            n_profiles > 1 and 0 < cone_saturates < len(cone)
            and sum(prof_counts.values()) == len(cone),
            "distinct radius profiles=%d over %d generators %s; attaining the "
            "half-width=%d of %d"
            % (n_profiles, len(cone),
               {"".join(str(x) for x in k): v
                for k, v in sorted(prof_counts.items())},
               cone_saturates, len(cone)))
    S["radius_profiles"] = {"distinct": n_profiles,
                            "profiles": {"".join(str(x) for x in k): v
                                         for k, v in sorted(prof_counts.items())},
                            "half_width_attained": cone_saturates,
                            "generators": len(cone)}
    ord_names = sorted(orders)[::7]
    ord_ok = (all(v is not None for v in orders.values())
              and all(orders_raw[k] % orders[k] == 0 for k in orders)
              and all(mat_mul_pow_check([x for x in circ_pool if x["name"] == k][0],
                                        orders_raw[k], NS, mat_mul, mat_id)
                      for k in ord_names)
              and proj_inv == 6 * 7 and raw_moves > 0)
    LD.gate("G-TWOPOINT-PERIODICITY",
            "every generator has a finite projective period, the period divides "
            "the raw order, the raw order is re-verified by an independent power "
            "recomputation, and the self-test shows the projective period is "
            "gauge invariant while the raw order is not",
            ord_ok,
            "projective periods=%s raw orders=%s; powers re-verified at %d "
            "generators; gauge self-test: projective invariant at %d of %d, raw "
            "order moved at %d"
            % (sorted({v for v in orders.values()}),
               sorted({v for v in orders_raw.values()}), len(ord_names),
               proj_inv, 6 * 7, raw_moves))
    S["lightcone"] = cone
    S["orders"] = orders
    S["orders_raw"] = orders_raw
    S["raw_order_set"] = sorted({v for v in orders_raw.values() if v})
    S["period_selftest"] = {"combinations": 6 * 7,
                            "projective_invariant": proj_inv,
                            "raw_moved": raw_moves}

    # ---------------- transformation-type classes -------------------------
    say("[8/12] the transformation-type class census")

    PERMS = {}
    for pi in range(len(pelems)):
        f = pelems[pi]
        for w in sites:
            PERMS[(pi, w)] = tuple(IDX[addv(f(x), w)] for x in sites)

    def act_on_gen(g, pidx, w):
        """point element then translation, acting on the matrix."""
        perm = PERMS[(pidx, w)]
        return {(perm[i], perm[j]): v for (i, j), v in g["mat"].items()}

    CANON = {}

    def canon_key(M):
        base = tuple(sorted((k, v) for k, v in M.items()))
        got = CANON.get(base)
        if got is not None:
            return got
        best = base
        for t in range(1, 8):
            z = zpow(t)
            cand = tuple(sorted((k, cmul(z, v)) for k, v in M.items()))
            if cand < best:
                best = cand
        CANON[base] = best
        return best

    key_of = {g["name"]: canon_key(g["mat"]) for g in pool}
    by_key = {}
    for g in pool:
        by_key.setdefault(key_of[g["name"]], []).append(g["name"])

    def orbit_census(pidxs, label):
        seen, orbits = set(), []
        for g in pool:
            if g["name"] in seen:
                continue
            orb, stab = set(), 0
            for pi in pidxs:
                for w in sites:
                    k = canon_key(act_on_gen(g, pi, w))
                    orb.add(k)
                    if k == key_of[g["name"]]:
                        stab += 1
            members = sorted({nm for k in orb for nm in by_key.get(k, [])})
            seen |= set(members)
            orbits.append({"representative": g["name"], "size": len(members),
                           "members": members, "orbit_keys": len(orb),
                           "stabiliser": stab, "group_order": len(pidxs) * len(sites),
                           "kind": g["kind"], "support": g["support"],
                           "radius": g["radius"], "axis_ord": g["axis_ord"],
                           "level": levels[g["name"]], "order": orders.get(g["name"])})
        return orbits

    anchored_idxs = [pnames.index("r0s0"), swap_idx]
    extended_idxs = list(range(len(pelems)))
    orb_anchored = orbit_census(anchored_idxs, "ANCHORED")
    orb_extended = orbit_census(extended_idxs, "EXTENDED")
    if mut("MUT-CLASS-DROP"):
        orb_extended = orb_extended[:-1]
    if mut("MUT-CLASS-MERGE") and len(orb_extended) > 1:
        orb_extended[0] = dict(orb_extended[0])
        orb_extended[0]["size"] = orb_extended[0]["size"] + 1
    covered = sorted(nm for o in orb_extended for nm in o["members"])
    LD.gate("G-CLASS-ORBITS-PARTITION",
            "the transformation-type classes partition the pool: the orbits are "
            "disjoint and cover every generator",
            covered == sorted(g["name"] for g in pool),
            "orbits=%d covering=%d of %d" % (len(orb_extended), len(covered), len(pool)))
    stab_ok = all(o["orbit_keys"] * o["stabiliser"] == o["group_order"] for o in orb_extended)
    size_ok = (all(o["size"] == len(o["members"]) for o in orb_extended)
               and sum(o["size"] for o in orb_extended) == len(pool))
    LD.gate("G-CLASS-ORBIT-STABILIZER",
            "the orbit-stabiliser identity holds on every class, computed from "
            "the measured action, and every class size equals its measured "
            "membership with the sizes summing to the pool",
            stab_ok and size_ok and all(o["size"] >= 1 for o in orb_extended),
            "classes=%d sizes=%s sum=%d pool=%d"
            % (len(orb_extended), sorted({o["size"] for o in orb_extended}),
               sum(o["size"] for o in orb_extended), len(pool)))
    inv_bad = 0
    for o in orb_extended:
        invs = set()
        for nm in o["members"]:
            g = [x for x in pool if x["name"] == nm][0]
            invs.add((g["support"], g["radius"], levels[nm], orders.get(nm)))
        if mut("MUT-CLASS-INVARIANT") and o is orb_extended[0]:
            invs.add(("x", 9, "NONE", 1))
        if len(invs) != 1:
            inv_bad += 1
    LD.gate("G-CLASS-INVARIANTS",
            "the declared class invariants -- support, radius, transport level, "
            "generator order -- are constant on every orbit",
            inv_bad == 0, "orbits with mixed invariants=%d" % inv_bad)
    if mut("MUT-ONE-GROUP"):
        orb_anchored = []
    LD.gate("G-CLASS-TWO-GROUPS",
            "the class census is taken at both declared groups: the anchored "
            "chart group and this unit's declared extension",
            len(orb_anchored) >= len(orb_extended) and len(orb_anchored) > 0,
            "anchored classes=%d extended classes=%d"
            % (len(orb_anchored), len(orb_extended)))
    # DO THE DECLARED INVARIANTS SEPARATE THE CLASSES?  Constant on orbits is
    # one property; separating is another, and Wigner's labels have both.
    label_of = {}
    for o in orb_extended:
        label_of[o["representative"]] = (o["size"], o["kind"], o["support"],
                                         o["radius"], o["axis_ord"],
                                         o["level"], o["order"])
    n_labels = len({v for v in label_of.values()})
    collisions = {}
    for rep, lab in label_of.items():
        collisions.setdefault(lab, []).append(rep)
    shared = {k: v for k, v in collisions.items() if len(v) > 1}
    # the completion: adding the axis's point-group orbit (a DIRECTION label)
    ax_orbit = {}
    for a in axes:
        key = frozenset({f(a) for f in pelems} | {smul(L - 1, f(a)) for f in pelems})
        ax_orbit[a] = key
    dir_labels = set()
    for o in orb_extended:
        g0 = [x for x in pool if x["name"] == o["representative"]][0]
        dir_labels.add(label_of[o["representative"]]
                       + (str(sorted(ax_orbit.get(g0["axis"], frozenset()))),))
    if mut("MUT-CLASS-LABELS"):
        n_labels = len(orb_extended)
    LD.gate("G-CLASS-LABELS-NONSEPARATING",
            "the declared class invariants are constant on every orbit but do "
            "NOT separate the classes: the label count is measured against the "
            "class count, the collisions are printed, and the completion by a "
            "direction label is measured too",
            0 < n_labels < len(orb_extended)
            and len(dir_labels) > n_labels
            and sum(len(v) for v in collisions.values()) == len(orb_extended),
            "classes=%d distinct invariant labels=%d (shared labels=%d, the "
            "largest shared by %d classes); with a direction label added=%d"
            % (len(orb_extended), n_labels, len(shared),
               max([len(v) for v in shared.values()] or [0]), len(dir_labels)))
    S["class_labels"] = {
        "classes": len(orb_extended), "distinct_labels": n_labels,
        "with_direction_label": len(dir_labels),
        "shared": [{"label": [str(x) for x in k], "classes": v}
                   for k, v in sorted(shared.items(), key=lambda kv: str(kv[0]))]}

    trans_only = orbit_census([pnames.index("r0s0")], "TRANSLATIONS")
    circ_singletons = sum(1 for o in trans_only
                          if o["kind"] == "CIRC" and o["orbit_keys"] == 1)
    if mut("MUT-TRANS-TRIVIAL"):
        circ_singletons = 0
    LD.gate("G-CLASS-TRANSLATION-TRIVIAL",
            "the translation group acts trivially on the circulant family. "
            "FORCED: a coefficient-map matrix commutes with every translation by "
            "construction, so the singleton orbits are an identity.  The row is "
            "a disclosure; the measured half is the next gate",
            circ_singletons == sum(1 for o in trans_only if o["kind"] == "CIRC"),
            "circulant translation orbits of size 1: %d of %d"
            % (circ_singletons, sum(1 for o in trans_only if o["kind"] == "CIRC")),
            kind="DISCLOSURE")
    controls_moving = sum(1 for o in trans_only
                          if o["kind"] != "CIRC" and o["orbit_keys"] > 1)
    if mut("MUT-CONTROLS-INERT"):
        controls_moving = 0
    LD.gate("G-CLASS-CONTROLS-MOVE",
            "the measured half of the same reading, and what makes the "
            "covariance census non-vacuous: the CONTROLS do move under the "
            "translation action, so the trivial action on the family is a fact "
            "about the family and not about the action",
            controls_moving > 0,
            "control translation orbits of size > 1: %d of %d control classes"
            % (controls_moving,
               sum(1 for o in trans_only if o["kind"] != "CIRC")))
    S["classes"] = {"anchored_group_order": len(anchored_idxs) * len(sites),
                    "extended_group_order": len(extended_idxs) * len(sites),
                    "anchored_classes": len(orb_anchored),
                    "extended_classes": len(orb_extended),
                    "extended": [{k: v for k, v in o.items() if k != "members"}
                                 | {"members": o["members"]} for o in orb_extended],
                    "anchored": [{k: v for k, v in o.items() if k != "members"}
                                 for o in orb_anchored]}

    # ---------------- the commutator census -------------------------------
    # The most consequential structural fact on the stage, and the datum R5
    # inherits: WHICH generators fail to commute, by stratum.
    def stratum_of(gv, gu):
        ks = (gv["kind"], gu["kind"])
        if "SCRAM" in ks:
            return "WITH-SCRAMBLE"
        if ks == ("CIRC", "CIRC"):
            return "CIRC-CIRC-THE-VERDICT-STRATUM"
        if ks == ("BRICK", "BRICK"):
            return "BRICK-BRICK"
        return "CIRC-BRICK"

    comm_rows = {}
    for gv in pool:
        for gu in pool:
            st = stratum_of(gv, gu)
            rec = comm_rows.setdefault(st, {"pairs": 0, "noncommuting": 0})
            rec["pairs"] += 1
            if mat_mul(gv["mat"], gu["mat"], NS) != mat_mul(gu["mat"], gv["mat"], NS):
                rec["noncommuting"] += 1
    verdict_stratum = comm_rows["CIRC-CIRC-THE-VERDICT-STRATUM"]
    noncomm_outside = sum(v["noncommuting"] for k, v in comm_rows.items()
                          if k != "CIRC-CIRC-THE-VERDICT-STRATUM")
    if mut("MUT-COMMUTATOR"):
        verdict_stratum = dict(verdict_stratum, noncommuting=1)
    LD.gate("G-COMMUTATOR-CENSUS",
            "the verdict-bearing stratum is abelian and the excluded stratum is "
            "not: every ordered pair of the pool is tested for commutation and "
            "the counts are reported per stratum.  The zero on the verdict "
            "stratum is FORCED (circulant convolution on an abelian group "
            "commutes); what is measured is that the non-commutativity on this "
            "stage lives entirely in the generators the mandatory realization "
            "gate excludes",
            verdict_stratum["noncommuting"] == 0 and noncomm_outside > 0
            and sum(v["pairs"] for v in comm_rows.values()) == len(pool) ** 2,
            "%s; non-commuting outside the verdict stratum=%d"
            % ({k: "%d of %d" % (v["noncommuting"], v["pairs"])
                for k, v in sorted(comm_rows.items())}, noncomm_outside),
            kind="FORCED")
    S["commutator_census"] = {k: dict(v) for k, v in sorted(comm_rows.items())}
    S["commutator_census"]["noncommuting_outside_verdict_stratum"] = noncomm_outside

    # ---------------- realization gate bites ------------------------------
    say("[9/12] the realization gate and the state-motion check")
    below = [r for r in rows if r["level"] != maximal and r["nonzero_cells"] > 0]
    if mut("MUT-REALIZATION-NOBITE"):
        below = []
    at_max = [r for r in rows if r["level"] == maximal]
    at_max_nz = [r for r in at_max if r["nonzero_cells"] > 0]
    # the gate's PRINCIPLED bite: the excluded rows that do not involve the
    # deliberately scrambled negative control, which was never a candidate.
    scram_names = {g["name"] for g in pool if g["kind"] == "SCRAM"}
    below_control = [r for r in below
                     if r["V"] in scram_names or r["U"] in scram_names]
    principled_bite = len(below) - len(below_control)
    LD.gate("G-REALIZATION-GATE-BITES",
            "the realization gate is not vacuous: nonzero defects exist below "
            "the maximal declared transport and are excluded from the verdict. "
            "The gate's PRINCIPLED bite -- the excluded rows that do not involve "
            "the negative control -- is measured and reported alongside the "
            "gross count, because the negative control was never a candidate",
            len(below) > 0 and len(at_max) < len(rows) and principled_bite > 0,
            "excluded nonzero defects=%d, of which %d involve the scrambled "
            "control and %d are the principled bite; pairs at maximal "
            "transport=%d of %d"
            % (len(below), len(below_control), principled_bite,
               len(at_max), len(rows)))
    seg_all = "DEFECT=%d-OF-%d" % (len([r for r in rows if r["nonzero_cells"] > 0]), len(rows))
    seg_max = "DEFECT=%d-OF-%d" % (len(at_max_nz), len(at_max))
    if mut("MUT-REALIZATION-ADMIT"):
        seg_max = seg_all
    LD.gate("G-REALIZATION-VERDICT-ONLY-MAXIMAL",
            "the verdict's defect segment is rebuilt from the maximal-transport "
            "subset alone and differs from the all-pairs segment",
            seg_max != seg_all, "maximal=%s all=%s" % (seg_max, seg_all))
    S["realization_census"] = {
        "levels": {lv: sum(1 for v in levels.values() if v == lv) for lv in LEVELS},
        "maximal": maximal,
        "pairs_at_maximal": len(at_max), "pairs_total": len(rows),
        "nonzero_at_maximal": len(at_max_nz),
        "nonzero_excluded_below_maximal": len(below),
        "per_generator": {g["name"]: {"level": levels[g["name"]],
                                      "kind": g["kind"],
                                      "translation_stabiliser": trans_stab[g["name"]],
                                      "transports": ["OCC"] if levels[g["name"]] == "OCC"
                                      else ([] if levels[g["name"]] == "NONE"
                                            else (["OCC", "AXIS"] if levels[g["name"]] == "OCC+AXIS"
                                                  else ["OCC", "AXIS", "PHASE-REGISTER"]))}
                          for g in pool}}

    # ---------------- state motion ----------------------------------------
    states = []
    for x in sites:
        states.append(("DELTA-%d%d" % x, {y: (ONE if y == x else ZERO) for y in sites}))
    states.append(("UNIFORM", {y: crat(1, NS) for y in sites}))
    states.append(("WEDGE", {y: crat(2, NS + 1) if not any(y) else crat(1, NS + 1)
                             for y in sites}))
    gv, gu = circ_pool[0], circ_pool[1]
    Dm = defect_dense(gv["mat"], gu["mat"], NS)
    if not Dm:
        for a in circ_pool:
            for b in circ_pool:
                if defect_dense(a["mat"], b["mat"], NS):
                    gv, gu = a, b
                    Dm = defect_dense(a["mat"], b["mat"], NS)
                    break
            if Dm:
                break

    def observable(p):
        out = {}
        for i in range(NS):
            acc = ZERO
            for j in range(NS):
                v = Dm.get((i, j))
                if v is None:
                    continue
                acc = cadd(acc, cmul(v, p[sites[j]]))
            out[i] = acc
        return out

    responses = {nm: observable(p) for nm, p in states}
    distinct = len({tuple(sorted((k, v) for k, v in r.items())) for r in responses.values()})
    if mut("MUT-STATE-INERT"):
        distinct = 1
    recon = {}
    for j, x in enumerate(sites):
        r = responses["DELTA-%d%d" % x]
        for i, v in r.items():
            if v != ZERO:
                recon[(i, j)] = v
    if mut("MUT-STATE-BACKGROUND"):
        recon = {}
    LD.gate("G-STATE-COEFFICIENT-BACKGROUND",
            "the defect coefficient is a background object: the matrix "
            "reconstructed from the point-mass responses equals the coefficient "
            "matrix exactly.  FORCED -- delta(p) = Delta^B p is linear, so the "
            "point-mass responses ARE the columns of Delta^B for every matrix "
            "whatever.  On a linear law over a single-occupation sector no "
            "coefficient CAN move with the state; this row discloses that, it "
            "does not test it",
            recon == Dm and len(Dm) > 0,
            "reconstructed cells=%d coefficient cells=%d" % (len(recon), len(Dm)),
            kind="FORCED")
    LD.gate("G-STATE-OBSERVABLE-MOVES",
            "the same instrument shows the OBSERVABLE defect moving with the "
            "prepared state, so the background reading is not an artefact of an "
            "inert instrument",
            distinct > 1, "distinct responses=%d over %d declared states"
            % (distinct, len(states)))

    # THE PROBE BREADTH.  One pair is not a family-wide statement; the probe set
    # is declared and its size is printed.
    probe_set = []
    for a in circ_pool:
        if len(probe_set) >= STATE_PROBE_PAIRS:
            break
        for b in circ_pool:
            if len(probe_set) >= STATE_PROBE_PAIRS:
                break
            D2 = defect_dense(a["mat"], b["mat"], NS)
            if D2:
                probe_set.append((a["name"], b["name"], D2))
    breadth_rows = []
    for nm_a, nm_b, D2 in probe_set:
        def obs(p, D2=D2):
            out = {}
            for i in range(NS):
                acc = ZERO
                for j in range(NS):
                    v = D2.get((i, j))
                    if v is None:
                        continue
                    acc = cadd(acc, cmul(v, p[sites[j]]))
                out[i] = acc
            return out
        resp = {nm: obs(p) for nm, p in states}
        dcount = len({tuple(sorted((k, v) for k, v in r.items()))
                      for r in resp.values()})
        rec = {}
        for j, x in enumerate(sites):
            for i, v in resp["DELTA-%d%d" % x].items():
                if v != ZERO:
                    rec[(i, j)] = v
        breadth_rows.append({"V": nm_a, "U": nm_b, "distinct_responses": dcount,
                             "coefficient_reconstructed": rec == D2})
    n_probes = len(breadth_rows)
    if mut("MUT-STATE-PROBE-NARROW"):
        breadth_rows = breadth_rows[:1]
        n_probes = 1
    LD.gate("G-STATE-PROBE-BREADTH",
            "the state-motion reading is taken over a declared probe SET, not a "
            "single pair, and the count is printed: every probe pair returns the "
            "same number of distinct responses and reconstructs its coefficient "
            "exactly",
            n_probes == STATE_PROBE_PAIRS
            and all(r["coefficient_reconstructed"] for r in breadth_rows)
            and len({r["distinct_responses"] for r in breadth_rows}) == 1
            and breadth_rows[0]["distinct_responses"] == distinct,
            "probe pairs=%d distinct responses per pair=%s reconstructions "
            "exact=%d of %d"
            % (n_probes, sorted({r["distinct_responses"] for r in breadth_rows}),
               sum(1 for r in breadth_rows if r["coefficient_reconstructed"]),
               len(breadth_rows)))
    S["state_motion"] = {"states_declared": len(states),
                         "probe_pair": [gv["name"], gu["name"]],
                         "probe_pairs": n_probes,
                         "probe_rows": breadth_rows,
                         "distinct_responses": distinct,
                         "coefficient_reconstructed_exactly": recon == Dm,
                         "verdict_label":
                         "BACKGROUND-BY-CONSTRUCTION-OBSERVABLE-MOVES-MEASURED"}

    # ===================================================================
    # SECTION 8.  THE VERDICT
    # ===================================================================
    say("[10/12] the verdict")
    sep_union = sorted({tuple(s) for r in at_max_nz if r["separations"]
                        for s in map(tuple, r["separations"])})
    val_multiset = sorted({v for r in at_max_nz if r["values"] for v in r["values"]})
    rat = sum(1 for r in at_max_nz if r["rational"] and all(r["rational"]))
    val_counts = {}
    for r in at_max_nz:
        if r["values"]:
            for v in r["values"]:
                val_counts[v] = val_counts.get(v, 0) + 1
    S["defect_values"] = [{"value": k, "cells": val_counts[k]}
                          for k in sorted(val_counts)]

    # THE CEILINGS.  Two of the verdict's two-point numbers are arena maxima,
    # attained rather than profiled, and the verdict must carry them as such.
    sep_ceiling = L ** d
    rad_ceiling = L // 2
    measured_seps = len(sep_union)
    measured_rad = max([torus_absmax(s, L) for s in sep_union] or [0])
    if mut("MUT-CEILING"):
        sep_ceiling = sep_ceiling + 1
    LD.gate("G-CEILINGS-MEASURED",
            "the two-point extent numbers are measured against the arena's own "
            "ceilings: the separation count against every separation the torus "
            "has, the defect radius against the torus's Chebyshev diameter.  "
            "Both are attained, so both are reported as ceilings",
            measured_seps == sep_ceiling and measured_rad == rad_ceiling
            and sep_ceiling == L ** d and rad_ceiling == L // 2,
            "separations measured=%d ceiling=%d; max defect radius measured=%d "
            "ceiling=%d" % (measured_seps, sep_ceiling, measured_rad, rad_ceiling))

    counts = {
        "pairs_total": len(rows),
        "pairs_at_maximal": len(at_max),
        "nonzero_at_maximal": len(at_max_nz),
        "nonzero_excluded": len(below),
        "principled_bite": principled_bite,
        "distinct_values": len(val_multiset),
        "all_rational_rows": rat,
        "separations": measured_seps,
        "separations_ceiling": sep_ceiling,
        "max_defect_radius": measured_rad,
        "radius_ceiling": rad_ceiling,
        "lightcone_content_radii": content_radii,
        "radius_profiles": n_profiles,
        "half_width_attained": cone_saturates,
        "circulants": len(circ_pool),
        "classes_extended": len(orb_extended),
        "classes_anchored": len(orb_anchored),
        "class_sizes": sorted({o["size"] for o in orb_extended}),
        "class_labels": n_labels,
        "markov_pairs": len(mk), "markov_nonzero": len(mk_nonzero),
        "commutator_pairs": verdict_stratum["pairs"],
        "commutator_nonzero": verdict_stratum["noncommuting"],
        "local_nonzero": loc_split["LOCAL"]["nonzero"],
        "local_pairs": loc_split["LOCAL"]["pairs"],
        "nonlocal_nonzero": loc_split["NONLOCAL"]["nonzero"],
        "nonlocal_pairs": loc_split["NONLOCAL"]["pairs"],
        "matched_pairs": matched,
        "matched_agreements": matched_agree,
        "matched_distinct": n_distinct,
        "orders": sorted({v for v in orders.values() if v}),
        "equal_time": S["equal_time"]["rational_zero"],
        "levels_attained": [lv for lv in LEVELS if any(v == lv for v in levels.values())],
        "maximal_transport": maximal,
        "admissible_scales": admissible,
        "locality_threshold": thresholds[2],
        "only_if_bound": only_if_bound,
        "present_at": present_at,
        "connective_tag": S["connective_forcing"]["forced_tag"],
        "forcing_link": "(%d,%d)" % tuple(
            max(test_links,
                key=lambda v: torus_abssum(v, max(L_SWEEP)))),
        "d": d,
        "L": L,
        "field": "Q(ZETA-8)",
        "alphabet": S["alphabet_size"],
        "pool": len(pool),
        "stencil": "3-TERM-AXIS",
        "sector": "SINGLE-OCCUPATION",
        "swept_range": "L-IN-%d..%d" % (min(L_SWEEP), max(L_SWEEP)),
        "indivisibility": "DECLARED-BY-DIVISION-EVENT-TIMES",
        "generators_at_maximal": sum(1 for v in levels.values() if v == maximal),
        "state_distinct": distinct,
        "state_probe_pairs": n_probes,
    }
    if mut("MUT-COUNT-TYPED"):
        counts["nonzero_at_maximal"] = 999
    S["counts"] = counts

    recount = sum(1 for r in rows if r["level"] == maximal and r["nonzero_cells"] > 0)
    LD.gate("G-COUNTS-DERIVED",
            "every headline count is recomputed by a second enumeration over the "
            "census rows",
            counts["nonzero_at_maximal"] == recount
            and counts["pairs_total"] == len(pool) ** 2,
            "nonzero at maximal: declared=%d recount=%d"
            % (counts["nonzero_at_maximal"], recount))

    head_law = derive_head
    if mut("MUT-PRECHECK-NAMES"):
        head_law = derive_head_from_precheck_only
    head = head_law(counts)
    # the COUNTERFACTUAL the precheck doctrine needs, computed by the law
    # actually in force and carried as data: with the defect census zeroed, does
    # the emitted head move?  A head named by the precheck does not.
    head_under_zeroed_census = head_law(dict(counts, nonzero_at_maximal=0))
    if mut("MUT-VERDICT-HEAD"):
        head = "R4-DEFECT-ABSENT"
    if mut("MUT-VERDICT-HEADS"):
        head = derive_head_constant(counts)
    LD.gate("G-VERDICT-HEAD-DERIVED",
            "the verdict head is derived inside a gate from measured counts and "
            "cannot be typed",
            head == derive_head(counts) and head.startswith("R4-"),
            "head=%s" % head)
    if mut("MUT-VERDICT-NAME"):
        head = "R4-DEFECT-OBSERVED"
    pin_text = src_text["A-PIN-R4"]
    # the pre-registered names are PARSED from the pin's bytes, not typed here,
    # and are carried into the receipt so the comparator can re-assert them.
    names = sorted({m.rstrip("-") for m in
                    re.findall(r"R4-[A-Z][A-Z0-9-]*", pin_text)})
    names = [n for n in names if not any(n != o and n.startswith(o + "-")
                                         for o in names)]
    LD.gate("G-VERDICT-PREREGISTERED",
            "the emitted head is one of the pin's pre-registered names, parsed "
            "from the pin's own bytes rather than typed here, and the parsed set "
            "is exactly the three the pin declares",
            len(names) == 3
            and any(head == n or head.startswith(n + "-") for n in names)
            and all(n in pin_text for n in names),
            "head=%s parsed pre-registered names=%s" % (head, names))
    S["preregistered_heads"] = names
    S["head_under_zeroed_census"] = head_under_zeroed_census

    segs = build_segments(counts, S, maximal)
    if mut("MUT-VERDICT-DROP"):
        segs = segs[:-1]
    if mut("MUT-VERDICT-SWAP") and len(segs) > 2:
        segs = list(segs)
        segs[1], segs[2] = (segs[1][0], segs[2][1]), (segs[2][0], segs[1][1])
    if mut("MUT-VERDICT-TYPED"):
        segs = list(segs)
        segs[0] = (segs[0][0], segs[0][0])
    verdict = head + "<" + "|".join("%s=%s" % (a, b) for a, b in segs) + ">"
    if mut("MUT-VERDICT-APPEND"):
        verdict = verdict + "-AND-MORE"
    if mut("MUT-PAPER-INPUT"):
        verdict = verdict + "-" + os.path.basename(SELF).upper()
    S["verdict"] = {"head": head, "segments": [{"name": a, "text": b} for a, b in segs],
                    "string": verdict,
                    "preregistered_heads": names,
                    "head_under_zeroed_census": head_under_zeroed_census}
    # POST-BUILD head corruption: injected AFTER every verdict gate above has
    # been evaluated.  Only a comparator that DERIVES the head can catch these.
    if mut("MUT-HEAD-POST-BUILD"):
        S["verdict"]["head"] = "R4-BLOCKED-AT-NOTHING"
        S["verdict"]["string"] = "R4-BLOCKED-AT-NOTHING" + verdict[len(head):]
    if mut("MUT-HEAD-ABSENT-VARIANT"):
        S["verdict"]["head"] = "R4-DEFECT-ABSENT-MARKOVIAN-COLLAPSE"
        S["verdict"]["string"] = ("R4-DEFECT-ABSENT-MARKOVIAN-COLLAPSE"
                                  + verdict[len(head):])
    if mut("MUT-HEAD-OFF-PIN"):
        S["verdict"]["head"] = "R4-QUANTUM-FIELD-CONFIRMED"
        S["verdict"]["string"] = "R4-QUANTUM-FIELD-CONFIRMED" + verdict[len(head):]
    S["_maximal"] = maximal

    return S, LD, pool, rows, sites, NS, orders, levels, orb_extended


def mat_mul_pow_check(g, o, NS, mm, mid):
    if o is None:
        return False
    P = mid(NS)
    for _ in range(o):
        P = mm(P, g["mat"], NS)
    return P == mid(NS)


def derive_head(c):
    """the head, derived from measured counts alone."""
    if not c["admissible_scales"]:
        return "R4-BLOCKED-AT-NO-LOCALITY-BEARING-SCALE"
    if c["generators_at_maximal"] == 0 or c["pairs_at_maximal"] == 0:
        return "R4-BLOCKED-AT-EMPTY-MAXIMAL-TRANSPORT-CLASS"
    if c["nonzero_at_maximal"] == 0:
        return "R4-DEFECT-ABSENT"
    return "R4-DEFECT-PRESENT"


def derive_head_constant(c):
    return "R4-DEFECT-PRESENT"


def derive_head_from_precheck_only(c):
    """the forbidden shape: a head named by the scale precheck alone (#314)."""
    return "R4-DEFECT-PRESENT" if c["admissible_scales"] else "R4-DEFECT-ABSENT"


DECOY_GATE_SOURCE = """

def _decoy_gate_that_references_mutant(LD):
    LD.gate("G-DECOY", "a gate predicate that exempts its own falsifier",
            not mut("MUT-DECOY"), "forbidden shape")
"""


LAUNDER_DECOY_SOURCE = """

def _decoy_launderer(LD):
    exempt = None if not mut("MUT-DECOY-LAUNDER") else 1
    LD.gate("G-DECOY-LAUNDER", "a gate reading a mutant-guarded name",
            exempt is None, "forbidden shape")
"""


def comparator_that_self_compares(R):
    """the forbidden shape: a comparator routed through the audited path."""
    return derive_head(R["counts"]) + reconstruct_verdict_from_receipt(R)


def comparator_that_reads_prose(R):
    """the forbidden shape: a comparator that lets prose reach the verdict."""
    return reconstruct_verdict_from_receipt(R) + str(R.get("arena_declaration", ""))[:12]


# EVERY measured value the verdict carries, with the counts key it renders
# from.  The verdict is assembled from this table and from nothing else, so
# coverage of the flip probes is structural: G-VERDICT-VALUES-FLIPPABLE
# perturbs each distinct key and requires the reconstruction to move.
VERDICT_VALUES = [
    ("DEFECT.nonzero", "nonzero_at_maximal"),
    ("DEFECT.pairs", "pairs_at_maximal"),
    ("DEFECT.transport-level", "maximal_transport"),
    ("DEFECT.distinct-values", "distinct_values"),
    ("DEFECT.rational-rows", "all_rational_rows"),
    ("TWO-POINT.separations", "separations"),
    ("TWO-POINT.separation-ceiling", "separations_ceiling"),
    ("TWO-POINT.max-defect-radius", "max_defect_radius"),
    ("TWO-POINT.radius-ceiling", "radius_ceiling"),
    ("TWO-POINT.cone-content-radii", "lightcone_content_radii"),
    ("TWO-POINT.radius-profiles", "radius_profiles"),
    ("TWO-POINT.half-width-attained", "half_width_attained"),
    ("TWO-POINT.circulants", "circulants"),
    ("TWO-POINT.periods", "orders"),
    ("TWO-POINT.equal-time", "equal_time"),
    ("CLASSES.extended", "classes_extended"),
    ("CLASSES.anchored", "classes_anchored"),
    ("CLASSES.sizes", "class_sizes"),
    ("CLASSES.distinct-labels", "class_labels"),
    ("LOCALITY.local-nonzero", "local_nonzero"),
    ("LOCALITY.local-pairs", "local_pairs"),
    ("LOCALITY.nonlocal-nonzero", "nonlocal_nonzero"),
    ("LOCALITY.nonlocal-pairs", "nonlocal_pairs"),
    ("LOCALITY.matched-agreements", "matched_agreements"),
    ("LOCALITY.matched-pairs", "matched_pairs"),
    ("LOCALITY.matched-distinct", "matched_distinct"),
    ("MARKOV.nonzero", "markov_nonzero"),
    ("MARKOV.pairs", "markov_pairs"),
    ("COMMUTATOR.nonzero", "commutator_nonzero"),
    ("COMMUTATOR.pairs", "commutator_pairs"),
    ("REALIZATION.levels", "levels_attained"),
    ("REALIZATION.excluded", "nonzero_excluded"),
    ("REALIZATION.principled-bite", "principled_bite"),
    ("STATE.distinct-responses", "state_distinct"),
    ("STATE.probe-pairs", "state_probe_pairs"),
    ("SCALE.admissible", "admissible_scales"),
    ("SCALE.locality-threshold", "locality_threshold"),
    ("SCALE.only-if-bound", "only_if_bound"),
    ("SCALE.presence-set", "present_at"),
    ("SCALE.connective", "connective_tag"),
    ("SCALE.forcing-link", "forcing_link"),
    ("SCOPE.d", "d"),
    ("SCOPE.L", "L"),
    ("SCOPE.field", "field"),
    ("SCOPE.alphabet", "alphabet"),
    ("SCOPE.generators", "pool"),
    ("SCOPE.stencil", "stencil"),
    ("SCOPE.sector", "sector"),
    ("SCOPE.swept-range", "swept_range"),
    ("SCOPE.indivisibility", "indivisibility"),
]


def build_segments(c, S, maximal):
    def j(key, sep="+"):
        return sep.join(str(x) for x in c[key])
    segs = [
        ("DEFECT", "%s-OF-%s-PAIRS-AT-MAXIMAL-TRANSPORT-%s;VALUES=%s-DISTINCT;"
                   "ALL-RATIONAL-ROWS=%s" %
         (c["nonzero_at_maximal"], c["pairs_at_maximal"], c["maximal_transport"],
          c["distinct_values"], c["all_rational_rows"])),
        ("TWO-POINT", "SEPARATIONS=%s-OF-%s-CEILING;MAX-DEFECT-RADIUS=%s-OF-%s-"
                      "CEILING;LIGHTCONE=BOUND-HAS-CONTENT-ONLY-AT-RADIUS-%s;"
                      "RADIUS-PROFILES=%s;HALF-WIDTH-ATTAINED=%s-OF-%s;"
                      "PERIODS=%s;EQUAL-TIME=%s" %
         (c["separations"], c["separations_ceiling"], c["max_defect_radius"],
          c["radius_ceiling"], j("lightcone_content_radii"),
          c["radius_profiles"], c["half_width_attained"], c["circulants"],
          j("orders"), c["equal_time"])),
        ("CLASSES", "EXTENDED=%s;ANCHORED=%s;SIZES=%s;DISTINCT-INVARIANT-"
                    "LABELS=%s" %
         (c["classes_extended"], c["classes_anchored"], j("class_sizes"),
          c["class_labels"])),
        ("LOCALITY", "LOCAL=%s-OF-%s;NONLOCAL=%s-OF-%s;DEFECT-INDIFFERENT-AT-"
                     "MATCHED-VALUE-MULTISET=%s-OF-%s-WEIGHTED-FROM-%s-DISTINCT" %
         (c["local_nonzero"], c["local_pairs"], c["nonlocal_nonzero"],
          c["nonlocal_pairs"], c["matched_agreements"], c["matched_pairs"],
          c["matched_distinct"])),
        ("MARKOV", "%s-OF-%s-NONZERO" % (c["markov_nonzero"], c["markov_pairs"])),
        ("COMMUTATOR", "%s-OF-%s-NONZERO-IN-THE-VERDICT-STRATUM" %
         (c["commutator_nonzero"], c["commutator_pairs"])),
        ("REALIZATION", "LEVELS=%s;MAXIMAL=%s;EXCLUDED-NONZERO=%s;PRINCIPLED-"
                        "BITE=%s" %
         (j("levels_attained"), c["maximal_transport"], c["nonzero_excluded"],
          c["principled_bite"])),
        ("STATE", "BACKGROUND-COEFFICIENT-BY-CONSTRUCTION(LINEAR-LAW;SINGLE-"
                  "OCCUPATION);OBSERVABLE-MOVES-AT-%s-DISTINCT-RESPONSES-OVER-"
                  "%s-PROBE-PAIRS" % (c["state_distinct"], c["state_probe_pairs"])),
        ("SCALE", "L=%s-UNIQUE(LOCALITY-IFF-L>=%s;NON-MONOMIAL-LOCAL-AXIS-ONLY-"
                  "IF-L<=%s;PRESENT-AT-L-IN-{%s});CONNECTIVE=%s(FORCED-BY-"
                  "ANCHORED-LINK-%s)" %
         (j("admissible_scales"), c["locality_threshold"], c["only_if_bound"],
          j("present_at", ","), c["connective_tag"], c["forcing_link"])),
        ("SCOPE", "D=%s;L=%s;FIELD=%s;ALPHABET=%s;GENERATORS=%s;STENCIL=%s;"
                  "SECTOR=%s;SWEPT-RANGE=%s;INDIVISIBILITY=%s;FINITE-LATTICE-"
                  "ONLY;NO-CONTINUUM-CLAIM;NO-INTERACTING-THEORY-CLAIM-BEYOND-"
                  "THE-COMPOSED-SEGMENT-DEFECT" %
         (c["d"], c["L"], c["field"], c["alphabet"], c["pool"], c["stencil"],
          c["sector"], c["swept_range"], c["indivisibility"])),
    ]
    return segs


def reconstruct_verdict_from_receipt(R):
    """THE INDEPENDENT COMPARATOR.  Rebuilds the COMPLETE verdict string --
    head included -- from the serialized receipt alone, by a code path that
    shares no helper with build_segments, does not call derive_head, and reads
    no value this function types.  The head is DERIVED here by this
    comparator's own copy of the head law and re-asserted against the pin's
    pre-registered names as the receipt carries them."""
    c = R["counts"]
    # the comparator's own head law
    if not c["admissible_scales"]:
        hd = "R4-BLOCKED-AT-NO-LOCALITY-BEARING-SCALE"
    elif c["generators_at_maximal"] == 0 or c["pairs_at_maximal"] == 0:
        hd = "R4-BLOCKED-AT-EMPTY-MAXIMAL-TRANSPORT-CLASS"
    elif c["nonzero_at_maximal"] == 0:
        hd = "R4-DEFECT-ABSENT"
    else:
        hd = "R4-DEFECT-PRESENT"
    pre = R["verdict"]["preregistered_heads"]
    if not [n for n in pre if hd == n or hd.startswith(n + "-")]:
        hd = "R4-HEAD-OUTSIDE-THE-PIN"
    lst = lambda k, s: s.join([str(x) for x in c[k]])
    parts = []
    parts.append("DEFECT=" + str(c["nonzero_at_maximal"]) + "-OF-" +
                 str(c["pairs_at_maximal"]) + "-PAIRS-AT-MAXIMAL-TRANSPORT-" +
                 str(c["maximal_transport"]) + ";VALUES=" +
                 str(c["distinct_values"]) + "-DISTINCT;ALL-RATIONAL-ROWS=" +
                 str(c["all_rational_rows"]))
    parts.append("TWO-POINT=SEPARATIONS=" + str(c["separations"]) + "-OF-" +
                 str(c["separations_ceiling"]) + "-CEILING;MAX-DEFECT-RADIUS=" +
                 str(c["max_defect_radius"]) + "-OF-" + str(c["radius_ceiling"]) +
                 "-CEILING;LIGHTCONE=BOUND-HAS-CONTENT-ONLY-AT-RADIUS-" +
                 lst("lightcone_content_radii", "+") + ";RADIUS-PROFILES=" +
                 str(c["radius_profiles"]) + ";HALF-WIDTH-ATTAINED=" +
                 str(c["half_width_attained"]) + "-OF-" + str(c["circulants"]) +
                 ";PERIODS=" + lst("orders", "+") + ";EQUAL-TIME=" +
                 str(c["equal_time"]))
    parts.append("CLASSES=EXTENDED=" + str(c["classes_extended"]) + ";ANCHORED=" +
                 str(c["classes_anchored"]) + ";SIZES=" + lst("class_sizes", "+") +
                 ";DISTINCT-INVARIANT-LABELS=" + str(c["class_labels"]))
    parts.append("LOCALITY=LOCAL=" + str(c["local_nonzero"]) + "-OF-" +
                 str(c["local_pairs"]) + ";NONLOCAL=" + str(c["nonlocal_nonzero"]) +
                 "-OF-" + str(c["nonlocal_pairs"]) +
                 ";DEFECT-INDIFFERENT-AT-MATCHED-VALUE-MULTISET=" +
                 str(c["matched_agreements"]) + "-OF-" + str(c["matched_pairs"]) +
                 "-WEIGHTED-FROM-" + str(c["matched_distinct"]) + "-DISTINCT")
    parts.append("MARKOV=" + str(c["markov_nonzero"]) + "-OF-" +
                 str(c["markov_pairs"]) + "-NONZERO")
    parts.append("COMMUTATOR=" + str(c["commutator_nonzero"]) + "-OF-" +
                 str(c["commutator_pairs"]) + "-NONZERO-IN-THE-VERDICT-STRATUM")
    parts.append("REALIZATION=LEVELS=" + lst("levels_attained", "+") + ";MAXIMAL=" +
                 str(c["maximal_transport"]) + ";EXCLUDED-NONZERO=" +
                 str(c["nonzero_excluded"]) + ";PRINCIPLED-BITE=" +
                 str(c["principled_bite"]))
    parts.append("STATE=BACKGROUND-COEFFICIENT-BY-CONSTRUCTION(LINEAR-LAW;"
                 "SINGLE-OCCUPATION);OBSERVABLE-MOVES-AT-" +
                 str(c["state_distinct"]) + "-DISTINCT-RESPONSES-OVER-" +
                 str(c["state_probe_pairs"]) + "-PROBE-PAIRS")
    parts.append("SCALE=L=" + lst("admissible_scales", "+") +
                 "-UNIQUE(LOCALITY-IFF-L>=" + str(c["locality_threshold"]) +
                 ";NON-MONOMIAL-LOCAL-AXIS-ONLY-IF-L<=" + str(c["only_if_bound"]) +
                 ";PRESENT-AT-L-IN-{" + lst("present_at", ",") + "});CONNECTIVE=" +
                 str(c["connective_tag"]) + "(FORCED-BY-ANCHORED-LINK-" +
                 str(c["forcing_link"]) + ")")
    parts.append("SCOPE=D=" + str(c["d"]) + ";L=" + str(c["L"]) + ";FIELD=" +
                 str(c["field"]) + ";ALPHABET=" + str(c["alphabet"]) +
                 ";GENERATORS=" + str(c["pool"]) + ";STENCIL=" +
                 str(c["stencil"]) + ";SECTOR=" + str(c["sector"]) +
                 ";SWEPT-RANGE=" + str(c["swept_range"]) + ";INDIVISIBILITY=" +
                 str(c["indivisibility"]) + ";FINITE-LATTICE-ONLY;NO-CONTINUUM-"
                 "CLAIM;NO-INTERACTING-THEORY-CLAIM-BEYOND-THE-COMPOSED-SEGMENT-"
                 "DEFECT")
    return hd + "<" + "|".join(parts) + ">"


# ===========================================================================
# SECTION 9.  RECEIPT, GATES ON THE RECEIPT, COMPLIANCE
# ===========================================================================

def strip_private(o):
    if isinstance(o, dict):
        return {k: strip_private(v) for k, v in o.items() if not k.startswith("_")}
    if isinstance(o, list):
        return [strip_private(v) for v in o]
    if isinstance(o, tuple):
        return [strip_private(v) for v in o]
    return o


def has_float(o):
    if isinstance(o, float):
        return True
    if isinstance(o, dict):
        return any(has_float(k) or has_float(v) for k, v in o.items())
    if isinstance(o, (list, tuple)):
        return any(has_float(v) for v in o)
    return False


def build_receipt(S, LD, pool, rows, orders, levels, orbits):
    R = strip_private(S)
    R["arena_declaration"] = ARENA
    R["arithmetic"] = ("exact only: integer coefficient 4-tuples over Q(zeta_8) "
                       "reduced modulo Phi_8 = x^4+1, canonical, so tuple "
                       "equality is field equality; no floats anywhere")
    R["census_rows"] = [{k: v for k, v in r.items() if k != "defect"} for r in rows]
    R["schema"] = SCHEMA
    R["pin"] = "v14/note-r4-qft-pin.md"
    R["pin_sha256_prefix"] = "1582cea5df51"
    R["source_sha256"] = sha12(SELF)
    return R


def recount_from_receipt(R):
    """Recomputes every census-derived headline count from the SERIALIZED
    census rows.  Shares no helper with the census builder and reads only the
    receipt."""
    rows = R["census_rows"]
    maximal = R["counts"]["maximal_transport"]
    L = R["counts"]["L"]
    at_max = [r for r in rows if r["level"] == maximal]
    nz = [r for r in at_max if r["nonzero_cells"] > 0]
    vals, seps, rat = {}, set(), 0
    for r in nz:
        for v in (r["values"] or []):
            vals[v] = vals.get(v, 0) + 1
        for s in (r["separations"] or []):
            seps.add(tuple(s))
        if r["rational"] and all(r["rational"]):
            rat += 1
    mk = [r for r in rows if r["monomial_factor"]]
    loc = [r for r in at_max if r["local"] and not r["monomial_factor"]]
    nloc = [r for r in at_max if not r["local"] and not r["monomial_factor"]]
    rad = 0
    for s in seps:
        rad = max(rad, max(min(x % L, (-x) % L) for x in s))
    return {
        "pool": len({r["V"] for r in rows}),
        "circulants": len({r["V"] for r in rows if r["circulant"]}),
        "pairs_total": len(rows),
        "pairs_at_maximal": len(at_max),
        "nonzero_at_maximal": len(nz),
        "nonzero_excluded": len([r for r in rows if r["level"] != maximal
                                 and r["nonzero_cells"] > 0]),
        "distinct_values": len(vals),
        "all_rational_rows": rat,
        "separations": len(seps),
        "max_defect_radius": rad,
        "markov_pairs": len(mk),
        "markov_nonzero": len([r for r in mk if r["nonzero_cells"] > 0]),
        "local_pairs": len(loc),
        "local_nonzero": len([r for r in loc if r["nonzero_cells"] > 0]),
        "nonlocal_pairs": len(nloc),
        "nonlocal_nonzero": len([r for r in nloc if r["nonzero_cells"] > 0]),
    }


# Every engraved rule this unit is diffed against, with the GATES that
# discharge it.  The status is COMPUTED from the ledger and the declared
# falsifier map, never typed.
COMPLIANCE_RULES = [
    ("#313 rules bind at delivery: this unit's gates are diffed against every "
     "engraving standing on the day its pin froze",
     ["G-EVERY-GATE-EVALUATED", "G-WAIVERS-VERIFIED"]),
    ("#10 containment is not equality: the verdict gate compares the COMPLETE "
     "emitted string, head included, against an independent rebuild",
     ["G-VERDICT-STRING-EQUALITY"]),
    ("#10 render from the gated object: one object, one source of truth",
     ["G-RENDER-FROM-GATED-OBJECT"]),
    ("#20 prose renders from the receipt: every numeric claim of the paper is "
     "rendered here and checked against the paper's bytes, and the paper's "
     "numeral coverage is gated",
     ["G-PAPER-CLAIMS-VERIFIED"]),
    ("#20 compliance claims are gate claims: every status is a computed "
     "predicate shipping with an injection-falsifier",
     ["G-COMPLIANCE-COMPUTED"]),
    ("#20 path-value anchoring: a read-by-path anchors the (path, value) pair",
     ["G-PATH-VALUE-ANCHORS"]),
    ("#34 waiver claims are gate claims: a named waiver is verified, a gate no "
     "path evaluates is dead code, and every FORCED row names its forcing",
     ["G-WAIVERS-VERIFIED", "G-EVERY-GATE-EVALUATED", "G-FORCINGS-REGISTERED"]),
    ("#34 verbatim-text anchors: evaluated before byte anchors, each row bound "
     "to a named consumer gate, context windows not fragments",
     ["G-VERBATIM-ANCHORS"]),
    ("#46 no unanchored runtime inputs: pinned sources, plus the declared "
     "object under test and nothing else",
     ["G-NO-UNANCHORED-RUNTIME-INPUT"]),
    ("#314 precheck doctrine: a precheck may gate the census but may never name "
     "the verdict, and the test is by output",
     ["G-PRECHECK-DOES-NOT-NAME-THE-VERDICT", "G-LATTICE-BOUND-TO-ADMISSIBLE"]),
    ("#313 boundary parity: a Boolean connective carries a parity-witness -- "
     "and here the witness measures a FORBIDDEN alternative, because the "
     "connective is forced by the anchored link set",
     ["G-PARITY-WITNESS", "G-CONNECTIVE-FORCED-BY-ANCHORED-LINK"]),
    ("#208 no gate predicate may reference mutant identity, directly or "
     "through one hop",
     ["G-NO-MUTANT-IDENTITY-IN-GATES"]),
    ("#208 an analytically-forced clause is a DISCLOSURE, not a must-pass "
     "measurement, and names the gate carrying its content",
     ["G-FORCINGS-REGISTERED"]),
    ("#219 an object may not be compared against a copy of itself routed "
     "through the component under test",
     ["G-SELF-COMPARE-GUARD", "G-COUNTS-FROM-RECEIPT"]),
    ("#234 the verdict is derived inside a gate and a flip probe proves the "
     "derivation can fail -- one probe per measured VALUE, not per segment",
     ["G-VERDICT-HEAD-DERIVED", "G-VERDICT-VALUES-FLIPPABLE",
      "G-VERDICT-SEGMENTS-FLIPPABLE", "G-VERDICT-THREE-HEADS-REACHABLE"]),
    ("#24 counts are computed, never typed",
     ["G-COUNTS-DERIVED", "G-COUNTS-FROM-RECEIPT", "G-ORD-CENSUS-COUNTS",
      "G-POOL-DERIVED"]),
    ("#36 every gate is a measurement that could have come out otherwise; "
     "controls in both directions",
     ["G-MARKOV-POSITIVE-CONTROL", "G-GAUGE-HANDLE", "G-CLASS-CONTROLS-MOVE",
      "G-TWOPOINT-SCRAMBLE-BREAKS"]),
    ("RUNBOOK section 4: exact arithmetic only, floats swept by AST",
     ["G-NO-FLOAT-AST", "G-NO-FLOAT-RECEIPT"]),
    ("RUNBOOK section 14: symmetry self-tests evaluate fresh, cache bypassed, "
     "both directions",
     ["G-GAUGE-SELFTEST", "G-CACHE-EXERCISED"]),
    ("RUNBOOK section 14 (v14 #87): gates bind objects, not cardinalities",
     ["G-REALIZATION-LEVELS-PER-GENERATOR", "G-MARKOV-ZERO-OBJECT",
      "G-DEFECT-VALUE-CENSUS-FULL"]),
    ("RUNBOOK section 14 (v14 #82): the CLI-contract minimum -- argv parsed, "
     "unknown flags rejected, a real --selftest, a validated --mutant",
     ["G-CLI-CONTRACT"]),
    ("RUNBOOK section 15: the arena is declared as data and matched at every "
     "coordinate, and every measured restriction is carried in a segment",
     ["G-LOCALITY-LIKE-FOR-LIKE", "G-LIKE-FOR-LIKE-DISTINCT",
      "G-CEILINGS-MEASURED"]),
]


def compliance_sweep(LD):
    """the sweep, with COMPUTED statuses.  A row is APPLIED when every gate it
    names is in the frozen registry, was evaluated on this run, and either
    carries a declared injection-falsifier or a registered forcing."""
    by_gate = {}
    for name, gate_id, what in MUTANTS:
        by_gate.setdefault(gate_id, []).append(name)
    # the sweep runs inside the delivery run, so four gates are still pending
    # when it is taken; they are named here and G-EVERY-GATE-EVALUATED closes
    # the loop on all of them.
    evaluated = set(LD.evaluated) | {"G-EVERY-GATE-EVALUATED", "G-WAIVERS-VERIFIED",
                                     "G-COMPLIANCE-COMPUTED",
                                     "G-PAPER-CLAIMS-VERIFIED"}
    rows = []
    for rule, gates in COMPLIANCE_RULES:
        seen = [g for g in gates if g in GATE_REGISTRY or g == "G-CLI-CONTRACT"]
        ran = [g for g in gates if g in evaluated]
        fals = sorted({m for g in gates for m in by_gate.get(g, [])})
        forced = [g for g in gates if g in FORCINGS]
        ok = (len(seen) == len(gates) and len(ran) == len(gates)
              and (fals or len(forced) == len(gates) or "G-CLI-CONTRACT" in gates))
        rows.append({"rule": rule, "gates": gates,
                     "status": "APPLIED" if ok else "UNSATISFIED",
                     "computed": True, "gates_evaluated": len(ran),
                     "injection_falsifiers": fals or ["<registered forcing>"]})
    if mut("MUT-COMPLIANCE-TYPED"):
        rows.append({"rule": "a typed status", "gates": ["G-NOT-A-GATE"],
                     "status": "APPLIED", "computed": False,
                     "gates_evaluated": 0, "injection_falsifiers": []})
    return rows



# ===========================================================================
# SECTION 10.  DRIVER
# ===========================================================================

NUMERAL_RE = r"[0-9]+(?:[.,/][0-9]+)*"

# The residue: numerals that occur in the paper and are DERIVED IN TEXT rather
# than rendered from the receipt.  Each is named with the site that derives it,
# and each must actually occur in the paper (a padded allowlist dies).
DERIVED_IN_TEXT = {
    "0": "the offset 0 of the stencil {0, a, -a} and the zero of the field; "
         "section 3.2's proof and section 4.1's definition",
    "1": "the section numbers, the radius-1 ball, and the coefficient c_1 of "
         "the collapse proof; section 3.2",
    "2": "the section numbers and the exponent 2 of the lag 2a; section 3.2",
    "3": "the section numbers and the 3-term stencil named in the scope",
    "5": "the section numbers and the order-five threshold named in the "
         "theorem statement; section 3.2",
    "6": "the section numbers",
    "7": "the section numbers",
    "8": "the section numbers and the cyclotomic index of Q(zeta_8)",
    "9": "the section numbers and the 9-point stencil named in the scope",
    "10": "the section number of the instrument section",
    "11": "the section number of the successor register",
    "12": "the section number of the deviations register",
    "13": "the paper number of the weld-2 unit named in the successor register",
    "14": "the programme version v14",
    "1,2": "the offsets (1,2) and (2,1) named as non-local axes in section 3.1",
    "2,1": "the offsets (1,2) and (2,1) named as non-local axes in section 3.1",
    "1,3": "the offset (1,3) named as a local axis in section 3.1",
    "1,1": "the anchored diagonal link (1,1), whose norms force the "
           "connective; section 2",
    "1,0": "the anchored link (1,0); section 2",
    "0,1": "the anchored link (0,1); section 2",
    "2,0": "the offset (2,0) named as a non-local axis in section 3.1",
    "0,2": "the offset (0,2) named as a non-local axis in section 3.1",
    "2,2": "the offset (2,2) named as a non-local axis in section 3.1",
    "1,0,1": "the column index set {-1,0,1} of the radius-1 Chebyshev ball, in "
             "the Moore-ball collapse theorem's statement and proof; section 3",
    "1,2,3": "the swept dimension set {1,2,3} of the locality sweep; section 2",
}


def num(x):
    """the paper's numeral convention, rendered once so the paper and the
    receipt cannot drift apart: a thousands comma at five figures and above."""
    s = str(x)
    if len(s) < 5 or not s.isdigit():
        return s
    out = ""
    while len(s) > 3:
        out = "," + s[-3:] + out
        s = s[:-3]
    return s + out


def setstr(xs):
    return "{" + ", ".join(str(x) for x in xs) + "}"


def paper_claims(R):
    """EVERY numeric claim of the paper, rendered from the receipt.  The gate
    checks each string against the paper's bytes AND checks that the paper
    carries no numeral outside this rendering and the declared residue."""
    c = R["counts"]
    cl = {"verdict": R["verdict"]["string"]}
    for row in R["byte_anchors"]:
        cl["source:" + row["id"]] = row["measured"]
    # the stage
    for row in R["locality_threshold_table"]:
        cl["threshold:%s:d%d" % (row["connective_tag"], row["d"])] = \
            "| %s | %d | %s |" % (row["connective_tag"], row["d"], row["threshold"])
    for row in R["locality_sweep"]:
        if row["d"] == 2 and row["connective"] == CONNECTIVES[0]:
            cl["locality:L%d" % row["L"]] = "| %d | %d | %d |" % (
                row["L"], row["offsets"], row["neighbours"])
    cl["parity"] = ("threshold %d against the max-norm's %d, a measured delta "
                    "of %d" % (R["parity_witness"]["von_neumann_threshold_d2"],
                               R["parity_witness"]["moore_threshold_d2"],
                               R["parity_witness"]["delta"]))
    cl["connective_excluded_admissible"] = (
        "the admissible set would be %s"
        % setstr(R["connective_forcing"]["admissible_under_excluded"]))
    # the family
    for k in sorted(R["ord_census"], key=int):
        v = R["ord_census"][k]
        cl["ord:%s" % k] = "| %s | %d | %d | %d |" % (
            k, v["distinct_generators"], v["monomial"], v["non_monomial"])
    cl["alphabet"] = "%d elements" % c["alphabet"]
    cl["triples"] = "%s coefficient triples" % num(c["alphabet"] ** 3)
    for row in R["five_point_sweeps"]:
        if row["ordering"] == "AXIS-FIRST":
            cl["fivepoint:%d" % row["L"]] = "| %d | %s | %d |" % (
                row["L"], num(row["leaves_reached"]), row["non_monomial"])
    cl["fivepoint_nodes"] = ("%s and %s nodes under the two declared orderings"
                             % tuple(num(x) for x in
                                     sorted(r["nodes_visited"]
                                            for r in R["five_point_sweeps"]
                                            if r["L"] == 5)))
    cl["fivepoint_nodes4"] = ("%s and %s nodes"
                              % tuple(num(x) for x in
                                      sorted(r["nodes_visited"]
                                             for r in R["five_point_sweeps"]
                                             if r["L"] == 4)))
    cl["moore_ball_sizes"] = "L in %s" % setstr(R["moore_ball_collapse"]["sizes"])
    cl["domain"] = ("%s ordered pairs of nonzero alphabet elements, %s zero "
                    "divisors" % (num(R["moore_ball_collapse"]["domain"]["nonzero_elements"] ** 2),
                                  R["moore_ball_collapse"]["domain"]["zero_divisor_pairs"]))
    cl["scale"] = ("locality requires L >= %d; a non-monomial local-axis "
                   "generator requires L <= %d, and is present at L in %s"
                   % (c["locality_threshold"], c["only_if_bound"],
                      setstr(c["present_at"])))
    cl["admissible"] = "the admissible set is %s" % setstr(c["admissible_scales"])
    cl["alphabet_independence"] = (
        "the sizes bearing locality are %s and the sizes below the collapse "
        "threshold are %s" % (setstr(R["alphabet_independence"]["locality_sizes"]),
                              setstr(R["alphabet_independence"]["below_collapse_threshold"])))
    # the pool
    p = R["pool_counts"]
    cl["pool"] = ("%d generators: %d translation-covariant circulants, %d "
                  "brickwork generators and %d scrambled generators"
                  % (p["total"], p["circulant"], p["brickwork"], p["scrambled"]))
    cl["axes"] = ("%d axes, %d of them local and %d not"
                  % (p["axes"], p["local_axes"], p["nonlocal_axes"]))
    cl["ord4_generators"] = (
        "%d distinct unitary generators, %d of them non-monomial, in %d gauge "
        "classes" % (R["ord_census"]["4"]["distinct_generators"],
                     R["ord_census"]["4"]["non_monomial"],
                     R["ord_census"]["4"]["distinct_generators"] // 8))
    cl["choices"] = "%d construction choices" % len(R["choice_inventory"])
    # the census
    cl["census"] = "%s ordered pairs" % num(c["pairs_total"])
    cl["defect"] = ("%d of %d pairs at maximal transport carry a nonzero defect"
                    % (c["nonzero_at_maximal"], c["pairs_at_maximal"]))
    cl["rational"] = "%d of %d" % (c["all_rational_rows"], c["nonzero_at_maximal"])
    for row in R["defect_value_multiset"]:
        v = row["value"].replace("(", "").replace(")", "")
        cl["value:%s" % v] = "| $%s$ | %d |" % (v, row["cells"])
    cl["markov"] = "%d of %d Markovian pairs" % (c["markov_nonzero"], c["markov_pairs"])
    cl["free"] = ("%d of %d free pairs" % (R["markov_control"]["free_nonzero"],
                                           R["markov_control"]["free_pairs"]))
    cl["monomial"] = "%d of the pool's generators are monomial" % len(
        R["markov_control"]["monomial_generators"])
    cl["locality_split"] = ("%d of %d local pairs and %d of %d non-local pairs"
                            % (c["local_nonzero"], c["local_pairs"],
                               c["nonlocal_nonzero"], c["nonlocal_pairs"]))
    cl["matched"] = ("%d ordered comparisons drawn from %d distinct non-local "
                     "pairs; %d of the %d agree"
                     % (c["matched_pairs"], c["matched_distinct"],
                        c["matched_agreements"], c["matched_pairs"]))
    cl["matched_mult"] = ("multiplicities " + ", ".join(
        "%s at %s" % (v, k) for k, v in
        sorted(R["like_for_like"]["multiplicities"].items(),
               key=lambda kv: -int(kv[0]))))
    cl["gauge_matched"] = ("%d ordered comparisons from %d distinct pairs, of "
                           "which %d agree"
                           % (R["like_for_like"]["gauge_class_matched_pairs"],
                              R["like_for_like"]["gauge_class_distinct_comparisons"],
                              R["like_for_like"]["gauge_class_agreements"]))
    # two-point
    cl["equal_time"] = ("exactly %s at zero separation and %s at every nonzero "
                        "separation" % (R["equal_time"]["rational_zero"],
                                        R["equal_time"]["rational_nonzero"]))
    cl["separations"] = ("%d separations, every separation the torus has, with "
                         "maximum defect radius %d, the Chebyshev diameter"
                         % (c["separations"], c["max_defect_radius"]))
    cl["profiles"] = ("%d radius profiles occur across the first four powers"
                      % c["radius_profiles"])
    cl["profile_rows"] = ", ".join(
        "%s at %d" % (k, v) for k, v in sorted(R["radius_profiles"]["profiles"].items()))
    cl["half_width"] = "%d of %d attain the half-width" % (
        c["half_width_attained"], c["circulants"])
    cl["cone_vacuity"] = ("%s conceivable profiles, and the bound can fail only "
                          "at single-step radius %s"
                          % (num(R["lightcone_vacuity"]["profiles_swept"]),
                             "+".join(str(x) for x in c["lightcone_content_radii"])))
    cl["periods"] = ("the projective periods present are %s; the raw orders are %s"
                     % (setstr(c["orders"]), setstr(R["raw_order_set"])))
    cl["gauge_selftest"] = ("the projective period is invariant at %d of %d and "
                            "the raw order moves at %d"
                            % (R["period_selftest"]["projective_invariant"],
                               R["period_selftest"]["combinations"],
                               R["period_selftest"]["raw_moved"]))
    cl["scramble"] = ("%d of their %d defect tables against the probe set fail "
                      "to be one, and %d are identically zero"
                      % (R["scramble_control"]["defect_table_failures"],
                         R["scramble_control"]["defect_probes"],
                         R["scramble_control"]["defect_probes_identically_zero"]))
    cl["circ_sep"] = "all %d pass" % R["scramble_control"][
        "circulant_transition_tables_passing"]
    cl["coherence"] = "the declared %d triples with %d violations" % (
        R["coherence"]["triples"], R["coherence"]["violations"])
    # classes
    cl["classes"] = ("%d transformation-type classes under the extended group "
                     "and %d under the anchored chart group"
                     % (c["classes_extended"], c["classes_anchored"]))
    cl["groups"] = ("of order %d" % R["classes"]["anchored_group_order"])
    cl["groups2"] = ("order %d" % R["classes"]["extended_group_order"])
    cl["labels"] = ("%d classes carry only %d distinct invariant tuples; adding "
                    "a direction label raises it to %d"
                    % (R["class_labels"]["classes"],
                       R["class_labels"]["distinct_labels"],
                       R["class_labels"]["with_direction_label"]))
    for o in R["classes"]["extended"]:
        cl["class:%s" % o["representative"]] = "| %s | %d | %s | %s | %s | %s | %s | %s |" % (
            o["representative"], o["size"],
            {"CIRC": "circulant", "BRICK": "brickwork", "SCRAM": "scrambled"}[o["kind"]],
            o["support"] if o["support"] is not None else "\u2014",
            o["radius"], o["axis_ord"] if o["axis_ord"] is not None else "\u2014",
            o["level"], o["order"] if o["order"] is not None else "\u2014")
    # realization, commutators, state
    cl["realization"] = ("%d generator at NONE, %d at OCC, %d at OCC+AXIS, %d "
                         "at FULL" % (R["realization_census"]["levels"]["NONE"],
                                      R["realization_census"]["levels"]["OCC"],
                                      R["realization_census"]["levels"]["OCC+AXIS"],
                                      R["realization_census"]["levels"]["FULL"]))
    cl["excluded"] = ("%d nonzero defects are excluded from the verdict"
                      % c["nonzero_excluded"])
    cl["bite"] = ("%d of them involve the scrambled control, so the gate's "
                  "principled bite is %d"
                  % (c["nonzero_excluded"] - c["principled_bite"],
                     c["principled_bite"]))
    cl["commutator"] = ("%d of %d ordered pairs of the verdict-bearing stratum "
                        "fail to commute" % (c["commutator_nonzero"],
                                             c["commutator_pairs"]))
    for k in sorted(R["commutator_census"]):
        v = R["commutator_census"][k]
        if isinstance(v, dict):
            cl["comm:%s" % k] = "| %s | %d | %d |" % (k, v["noncommuting"], v["pairs"])
    cl["state"] = ("%d distinct responses" % c["state_distinct"])
    cl["state_probes"] = ("%d declared prepared states over %d probe pairs"
                          % (R["state_motion"]["states_declared"],
                             c["state_probe_pairs"]))
    cl["instrument"] = ("%d gates, all passed; %d anchors; %d declared mutants, "
                        "all dead"
                        % (len(GATE_REGISTRY),
                           len(SOURCES) + len(PATH_VALUE_ANCHORS) + len(VERBATIM_ANCHORS),
                           len(MUTANTS)))
    cl["anchor_split"] = ("%d file-bytes anchors, %d path-value anchors and %d "
                          "verbatim-text anchors"
                          % (len(SOURCES), len(PATH_VALUE_ANCHORS),
                             len(VERBATIM_ANCHORS)))
    cl["verdict_values"] = ("%d measured values" % len({k for _, k in VERDICT_VALUES}))
    cl["compliance"] = "%d engraved rules" % len(COMPLIANCE_RULES)
    if mut("MUT-PAPER-CLAIM-DRIFT"):
        cl["defect"] = cl["defect"] + "-DRIFTED"
    if mut("MUT-PAPER-COVERAGE"):
        cl = {"verdict": cl["verdict"]}
    return cl


def paper_coverage(R, txt):
    cl = paper_claims(R)
    missing = sorted(k for k, v in cl.items() if v not in txt)
    rendered = set()
    for v in cl.values():
        rendered |= set(re.findall(NUMERAL_RE, v))
    in_paper = set(re.findall(NUMERAL_RE, txt))
    residue_unused = sorted(k for k in DERIVED_IN_TEXT if k not in in_paper)
    uncovered = sorted(in_paper - rendered - set(DERIVED_IN_TEXT))
    return {"claims": len(cl), "missing": missing,
            "distinct_numerals": len(in_paper),
            "numeral_occurrences": len(re.findall(NUMERAL_RE, txt)),
            "covered_by_rendering": len(in_paper & rendered),
            "declared_derived_in_text": len(DERIVED_IN_TEXT),
            "residue_declared_but_absent": residue_unused,
            "uncovered": uncovered}


class CliError(Exception):
    pass


def parse_args(argv):
    """THE ARGV PARSER (#82).  A whitelist; every unknown flag, every unknown
    flag argument and every missing argument raises."""
    opts = {"write": True, "mutant": None, "break_anchor": None,
            "verify_paper": None, "selftest": False}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            opts["write"] = False
        elif a == "--selftest":
            opts["selftest"] = True
            opts["write"] = False
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant requires a mutant NAME")
            nm = argv[i + 1]
            if nm not in {m[0] for m in MUTANTS}:
                raise CliError("unknown mutant %r" % nm)
            opts["mutant"] = nm
            opts["write"] = False
            i += 1
        elif a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor requires an anchor NAME")
            nm = argv[i + 1]
            if nm not in {s[0] for s in SOURCES}:
                raise CliError("unknown anchor %r" % nm)
            opts["break_anchor"] = nm
            opts["write"] = False
            i += 1
        elif a == "--verify-paper":
            opts["verify_paper"] = PAPER_REL
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                opts["verify_paper"] = argv[i + 1]
                i += 1
            opts["write"] = False
        else:
            raise CliError("unknown argument %r" % a)
        i += 1
    return opts


def parse_args_permissive(argv):
    """the FORBIDDEN shape (the registered disease, #82): a runner that ignores
    what it does not recognise and proceeds to a full delivery run.  Present
    only as the CLI gate's falsifier; nothing calls it in the delivery path."""
    opts = {"write": True, "mutant": None, "break_anchor": None,
            "verify_paper": None, "selftest": False}
    if "--no-write" in argv:
        opts["write"] = False
    if "--mutant" in argv:
        opts["mutant"] = argv[argv.index("--mutant") + 1]
        opts["write"] = False
    return opts


def run_receipt_gates(S, LD, pool, rows, orders, levels, orbits):
    R = build_receipt(S, LD, pool, rows, orders, levels, orbits)
    if mut("MUT-RENDER-BYPASS"):
        R["counts"] = dict(R["counts"])
        R["counts"]["nonzero_at_maximal"] = R["counts"]["nonzero_at_maximal"] + 1
    LD.gate("G-RENDER-FROM-GATED-OBJECT",
            "the receipt renders from the gated object: every rendered count "
            "equals the gated count, field by field",
            all(R["counts"][k] == S["counts"][k] for k in S["counts"])
            and R["verdict"]["string"] == S["verdict"]["string"],
            "fields compared=%d" % len(S["counts"]))

    Rjson = json.loads(json.dumps(R, sort_keys=True))
    rebuilt = reconstruct_verdict_from_receipt(Rjson)
    LD.gate("G-VERDICT-STRING-EQUALITY",
            "the COMPLETE emitted verdict string equals an independent "
            "reconstruction built segment-by-segment from the serialized "
            "receipt alone; containment is not equality",
            rebuilt == S["verdict"]["string"],
            "emitted=%d chars rebuilt=%d chars equal=%s"
            % (len(S["verdict"]["string"]), len(rebuilt),
               rebuilt == S["verdict"]["string"]))

    def perturb(v):
        if isinstance(v, list):
            return v + [99]
        if isinstance(v, bool):
            return not v
        if isinstance(v, int):
            return v + 1
        return str(v) + "-X"

    seg_keys = {"DEFECT": "nonzero_at_maximal", "TWO-POINT": "separations",
                "CLASSES": "classes_extended", "LOCALITY": "local_nonzero",
                "MARKOV": "markov_pairs", "COMMUTATOR": "commutator_pairs",
                "REALIZATION": "nonzero_excluded",
                "STATE": "state_distinct", "SCALE": "admissible_scales",
                "SCOPE": "pool"}
    flips = []
    for i, seg in enumerate(S["verdict"]["segments"]):
        probe = json.loads(json.dumps(Rjson))
        k = seg_keys[seg["name"]]
        probe["counts"][k] = perturb(probe["counts"][k])
        moved = reconstruct_verdict_from_receipt(probe) != rebuilt
        if mut("MUT-VERDICT-INERT") and i == 0:
            moved = False
        flips.append(moved)
    LD.gate("G-VERDICT-SEGMENTS-FLIPPABLE",
            "every verdict segment moves when the receipt row it derives from "
            "moves; no segment is inert",
            all(flips) and len(flips) == len(seg_keys),
            "segments=%d flippable=%d" % (len(flips), sum(flips)))

    # THE PER-VALUE PROBE.  One flip test per MEASURED VALUE the verdict
    # carries, not one per segment: every value is rendered from a declared
    # counts key, and perturbing that key must move the reconstruction.
    probed_keys, inert = [], []
    for label, key in VERDICT_VALUES:
        if key in probed_keys:
            continue
        probed_keys.append(key)
        probe = json.loads(json.dumps(Rjson))
        probe["counts"][key] = perturb(probe["counts"][key])
        if mut("MUT-VALUE-INERT") and key == "principled_bite":
            probe["counts"][key] = Rjson["counts"][key]
        if reconstruct_verdict_from_receipt(probe) == rebuilt:
            inert.append((label, key))
    all_keys_present = all(key in Rjson["counts"] for _, key in VERDICT_VALUES)
    LD.gate("G-VERDICT-VALUES-FLIPPABLE",
            "EVERY measured value the verdict carries has its own flip probe: "
            "the value renders from a declared receipt key, and perturbing that "
            "key moves the complete reconstruction.  A value with no probe, or "
            "a value that ignores its key, dies here",
            not inert and all_keys_present
            and len(probed_keys) == len({k for _, k in VERDICT_VALUES}),
            "verdict values declared=%d distinct receipt keys probed=%d inert=%s"
            % (len(VERDICT_VALUES), len(probed_keys), inert or "none"))

    heads = set()
    probes = [
        dict(S["counts"]),
        dict(S["counts"], nonzero_at_maximal=0),
        dict(S["counts"], generators_at_maximal=0, pairs_at_maximal=0),
        dict(S["counts"], admissible_scales=[]),
    ]
    for p in probes:
        heads.add((derive_head_constant if mut("MUT-VERDICT-HEADS") else derive_head)(p))
    def headclass(h):
        if h.startswith("R4-DEFECT-PRESENT"):
            return "PRESENT"
        if h.startswith("R4-DEFECT-ABSENT"):
            return "ABSENT"
        return "BLOCKED"
    LD.gate("G-VERDICT-THREE-HEADS-REACHABLE",
            "all three pre-registered heads are reachable by the same "
            "derivation on synthetic censuses",
            {headclass(h) for h in heads} == {"PRESENT", "ABSENT", "BLOCKED"}
            and len(heads) == 4,
            "heads reached: %s" % sorted(heads))

    comparator = reconstruct_verdict_from_receipt
    if mut("MUT-COMPARATOR-READS-PROSE"):
        comparator = comparator_that_reads_prose
    v_no_paper = comparator(Rjson)
    poisoned = json.loads(json.dumps(Rjson))
    poisoned["arena_declaration"] = {"poison": "x" * 40}
    poisoned["census_rows"] = []
    LD.gate("G-VERDICT-NO-PAPER-INPUT",
            "no external prose can reach the verdict: the string is invariant "
            "when every non-numeric receipt field is replaced",
            comparator(poisoned) == v_no_paper,
            "invariant=%s" % (comparator(poisoned) == v_no_paper))

    # THE PRECHECK DOCTRINE, tested by OUTPUT.  The counterfactual is computed
    # in build_state by the head law actually in force and carried as data: with
    # the defect census zeroed, does the emitted head move?  A head named by the
    # scale precheck does not move, and dies here -- by its behaviour, not by
    # its name.
    zeroed = S["verdict"]["head_under_zeroed_census"]
    LD.gate("G-PRECHECK-DOES-NOT-NAME-THE-VERDICT",
            "the scale precheck gates which lattice is censused but never "
            "names the head: run on a zeroed defect census, the head law in "
            "force returns a DIFFERENT head, so the head is a function of the "
            "census and not of the precheck",
            zeroed != S["verdict"]["head"]
            and zeroed == derive_head(dict(S["counts"], nonzero_at_maximal=0)),
            "head=%s; head under a zeroed census, by the law in force: %s"
            % (S["verdict"]["head"], zeroed))

    with open(SELF, "r", encoding="utf-8") as f:
        own = f.read()
    tree = ast.parse(own)
    target_fn = "reconstruct_verdict_from_receipt"
    if mut("MUT-SELFCOMPARE"):
        target_fn = "comparator_that_self_compares"
    gatefn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == target_fn:
            gatefn = node
    calls = [n.func.id for n in ast.walk(gatefn)
             if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
    LD.gate("G-SELF-COMPARE-GUARD",
            "the verdict comparator is independent of the audited path: an AST "
            "scan of the comparator in force shows it calls neither "
            "build_segments nor derive_head and reads only the serialized "
            "receipt",
            "build_segments" not in calls and "derive_head" not in calls,
            "comparator scanned=%s calls: %s" % (target_fn, sorted(set(calls))))

    badmut, gate_calls = [], 0
    scan_src = own
    if mut("MUT-GATE-REFERENCES-MUTANT"):
        scan_src = scan_src + DECOY_GATE_SOURCE
    if mut("MUT-GATE-READS-LAUNDERED-NAME"):
        scan_src = scan_src + LAUNDER_DECOY_SOURCE
    scan_tree = ast.parse(scan_src) if scan_src != own else tree

    def has_mut_call(node):
        for n in ast.walk(node):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                    and n.func.id == "mut":
                return True
        return False

    parents = {}
    for node in ast.walk(scan_tree):
        for ch in ast.iter_child_nodes(node):
            parents[ch] = node

    def mutant_guarded(node):
        """the ONE-HOP LAUNDERING probe (#208, strengthened): an assignment is
        mutant-guarded when the mutant flag appears in its value or in the test
        of an enclosing if whose BODY it sits in."""
        if has_mut_call(node.value):
            return True
        cur, p = node, parents.get(node)
        while p is not None:
            if isinstance(p, ast.If) and has_mut_call(p.test) \
                    and any(cur is s for s in p.body):
                return True
            if isinstance(p, (ast.FunctionDef, ast.Module)):
                return False
            cur, p = p, parents.get(p)
        return False

    assigns = {}
    for node in ast.walk(scan_tree):
        if isinstance(node, ast.Assign):
            g = mutant_guarded(node)
            for t in node.targets:
                for n in ast.walk(t):
                    if isinstance(n, ast.Name):
                        assigns.setdefault(n.id, []).append(g)
    laundered = {nm for nm, gs in assigns.items() if gs and all(gs)}

    for node in ast.walk(scan_tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == "gate":
            gate_calls += 1
            gid = node.args[0].value if node.args else "?"
            for n in ast.walk(node):
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                        and n.func.id == "mut":
                    badmut.append(gid)
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) \
                        and n.id in laundered:
                    badmut.append("%s reads laundered name %s" % (gid, n.id))
    for node in ast.walk(scan_tree):
        if isinstance(node, ast.FunctionDef) and node.name in (
                "reconstruct_verdict_from_receipt", "derive_head", "build_segments"):
            for n in ast.walk(node):
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                        and n.func.id == "mut":
                    badmut.append(node.name)
    LD.gate("G-NO-MUTANT-IDENTITY-IN-GATES",
            "no gate predicate and no verdict-deriving or comparing function "
            "references mutant identity, DIRECTLY or through one hop: an AST "
            "scan of every gate call site and of the three verdict functions, "
            "extended to flag any gate reading a name whose every assignment "
            "site is mutant-guarded (#208, and the clause-removal probe made "
            "standing)",
            not badmut and gate_calls >= len(GATE_REGISTRY),
            "gate call sites scanned=%d mutant-guarded names in the module=%d "
            "offenders: %s" % (gate_calls, len(laundered), badmut or "none"))

    float_probe = dict(Rjson)
    if mut("MUT-FLOAT-RECEIPT"):
        float_probe["_float_probe"] = 10 ** -1
    LD.gate("G-NO-FLOAT-RECEIPT",
            "the emitted receipt object contains no float at any depth",
            not has_float(float_probe),
            "recursive scan of the serialized receipt")

    # --- the counts, recomputed from the SERIALIZED census rows -------------
    if mut("MUT-COUNT-RECEIPT"):
        for r in Rjson["census_rows"]:
            if r["nonzero_cells"] > 0 and r["level"] == Rjson["counts"]["maximal_transport"]:
                r["nonzero_cells"] = 0
                break
    again = recount_from_receipt(Rjson)
    disagree = sorted(k for k, v in again.items() if Rjson["counts"][k] != v)
    LD.gate("G-COUNTS-FROM-RECEIPT",
            "every census-derived headline count is recomputed from the "
            "serialized census rows by a function sharing no helper with the "
            "census builder, and all of them are compared -- not two of "
            "twenty-three (#219)",
            not disagree and len(again) >= 15,
            "counts recomputed=%d disagreements=%s" % (len(again), disagree or "none"))

    # --- #208: every FORCED / DISCLOSURE / DECLARED row names its forcing ---
    forcings_map = dict(FORCINGS)
    if mut("MUT-FORCING-UNREGISTERED"):
        forcings_map.pop("G-COHERENCE-LAW", None)
    unforced = [g["id"] for g in LD.rows
                if g["kind"] in ("FORCED", "DISCLOSURE", "DECLARED")
                and g["id"] not in forcings_map]
    n_forced = sum(1 for g in LD.rows
                   if g["kind"] in ("FORCED", "DISCLOSURE", "DECLARED"))
    LD.gate("G-FORCINGS-REGISTERED",
            "every gate whose clause is analytically forced is registered as a "
            "DISCLOSURE with a named forcing and with the gate that carries its "
            "measured content in its place (#208)",
            not unforced and n_forced > 0,
            "forced/disclosure/declared rows=%d without a registered "
            "forcing=%s" % (n_forced, unforced or "none"))

    # --- the CLI contract, exercised in process (#82) -----------------------
    parser = parse_args
    if mut("MUT-CLI-ACCEPTS-UNKNOWN"):
        parser = parse_args_permissive
    cli_probes = []
    for argv, want in ((["--not-a-flag"], True), (["--mutant"], True),
                       (["--mutant", "MUT-DOES-NOT-EXIST"], True),
                       (["--break-anchor", "A-NOPE"], True),
                       (["--break-anchor"], True),
                       (["--mutant", MUTANTS[0][0]], False),
                       (["--no-write"], False), ([], False)):
        try:
            got = parser(argv)
            rejected = False
        except CliError:
            got, rejected = None, True
        except (IndexError, KeyError, TypeError, ValueError):
            # a traceback is not a rejection; the contract requires a message
            got, rejected = None, False
        cli_probes.append((argv, want, rejected, got))
    cli_bad = [p for p in cli_probes if p[1] != p[2]]
    plain = [p for p in cli_probes if p[0] == []][0][3]
    writers = [p for p in cli_probes if p[3] is not None and p[3]["write"]]
    LD.gate("G-CLI-CONTRACT",
            "the CLI is argv-parsed against a whitelist and exercised here: an "
            "unknown flag, an unknown mutant name, an unknown anchor name and a "
            "missing flag argument are all REJECTED, and the plain run with no "
            "flags is the only invocation that writes",
            not cli_bad and plain["write"] and len(writers) == 1,
            "probes=%d rejections as declared=%d; invocations that write=%d"
            % (len(cli_probes), len(cli_probes) - len(cli_bad), len(writers)))

    # --- the paper, gated inside the delivery run --------------------------
    cov = paper_coverage(Rjson, S["_paper_text"])
    LD.gate("G-PAPER-CLAIMS-VERIFIED",
            "every numeric claim of the paper is rendered from this receipt and "
            "checked against the paper's own bytes, AND the paper carries no "
            "numeral outside that rendering except the declared derived-in-text "
            "residue, every entry of which must occur in the paper",
            not cov["missing"] and not cov["uncovered"]
            and not cov["residue_declared_but_absent"],
            "claims rendered=%d missing from the paper=%s; distinct numerals in "
            "the paper=%d over %d occurrences, covered by rendering=%d, "
            "declared derived-in-text=%d, uncovered=%s"
            % (cov["claims"], cov["missing"] or "none", cov["distinct_numerals"],
               cov["numeral_occurrences"], cov["covered_by_rendering"],
               cov["declared_derived_in_text"], cov["uncovered"] or "none"))
    R["paper_coverage"] = cov

    # --- the compliance sweep, with COMPUTED statuses ----------------------
    comp = compliance_sweep(LD)
    comp_bad_rows = [r for r in comp
                     if r["status"] != "APPLIED" or not r["computed"]
                     or not r["gates"] or r["gates_evaluated"] != len(r["gates"])]
    LD.gate("G-COMPLIANCE-COMPUTED",
            "every compliance status is a COMPUTED predicate over the ledger "
            "and the declared falsifier map -- a row is APPLIED only when every "
            "gate it names is in the frozen registry, was evaluated on this "
            "run, and carries an injection-falsifier or a registered forcing",
            not comp_bad_rows and len(comp) == len(COMPLIANCE_RULES),
            "rules=%d applied=%d unsatisfied=%s"
            % (len(comp), sum(1 for r in comp if r["status"] == "APPLIED"),
               [r["rule"][:34] for r in comp_bad_rows] or "none"))

    # the two post-census gates are evaluated after the mutant harness, which
    # is why they are named here rather than found in the ledger
    evaluated = list(LD.evaluated) + ["G-EVERY-GATE-EVALUATED", "G-WAIVERS-VERIFIED"]
    if mut("MUT-DEAD-GATE"):
        evaluated = [g for g in evaluated if g != "G-COUNTS-DERIVED"]
    missing = [g for g in GATE_REGISTRY if g not in evaluated]
    extra = [g for g in evaluated if g not in GATE_REGISTRY]
    LD.gate("G-EVERY-GATE-EVALUATED",
            "every gate in the frozen registry is reached by an execution "
            "path; there is no dead gate and no unregistered gate (#34)",
            not missing and not extra,
            "registry=%d evaluated=%d missing=%s extra=%s"
            % (len(GATE_REGISTRY), len(evaluated), missing or "none", extra or "none"))
    return R, Rjson


def selftest():
    """--selftest: corrupt ONE anchor in memory, confirm the run dies at the
    anchor gate, WRITE NOTHING, exit 1.  Exits 2 if the corrupted run survives."""
    target = SOURCES[0][0]
    print("SELFTEST: corrupting anchor %s in memory; the run must die." % target,
          flush=True)
    globals()["QUIET"] = True
    try:
        build_state(target)
    except GateFail as e:
        globals()["QUIET"] = False
        gid = str(e).split(" ::")[0]
        print("SELFTEST: died at %s -- as required." % gid, flush=True)
        print("SELFTEST PASSED (the instrument is falsifiable); no artifact "
              "written.", flush=True)
        print("EXIT 1", flush=True)
        sys.exit(1)
    globals()["QUIET"] = False
    print("SELFTEST FAILED: a corrupted anchor did not kill the run.", flush=True)
    print("EXIT 2", flush=True)
    sys.exit(2)


def main():
    global MUT
    try:
        opts = parse_args(sys.argv[1:])
    except CliError as e:
        print("usage: %s [--no-write] [--selftest] [--mutant NAME] "
              "[--break-anchor NAME] [--verify-paper [PATH]]"
              % os.path.basename(SELF), file=sys.stderr)
        print("error: %s" % e, file=sys.stderr)
        sys.exit(2)
    if opts["selftest"]:
        selftest()
    write = opts["write"]
    break_anchor = opts["break_anchor"]
    verify_paper = opts["verify_paper"]
    MUT = opts["mutant"]

    say("=" * 78)
    say("v14 R4 -- THE QFT RUNG: THE DEFECT ON THE STAGE")
    say("=" * 78)
    if MUT:
        say("MUTANT ACTIVE: %s" % MUT)
    if break_anchor:
        say("ANCHOR BREAK SELF-TEST: %s" % break_anchor)

    try:
        S, LD, pool, rows, sites, NS, orders, levels, orbits = build_state(break_anchor)
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        if write:
            pass
        sys.exit(1)

    try:
        say("[11/12] receipt gates, mutants, compliance")
        R, Rjson = run_receipt_gates(S, LD, pool, rows, orders, levels, orbits)
        pass
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    if MUT or break_anchor:
        say("")
        say("MUTANT/BREAK SURVIVED -- no gate killed it.")
        say("EXIT 0")
        sys.exit(0)

    # ---- the mutant harness ----------------------------------------------
    say("[12/12] running %d declared mutants" % len(MUTANTS))
    report = []
    globals()["QUIET"] = True
    for name, target, what in MUTANTS:
        globals()["MUT"] = name
        killer, killed = None, False
        try:
            S2, LD2, pool2, rows2, sites2, NS2, orders2, levels2, orbits2 = \
                build_state(None)
            run_receipt_gates(S2, LD2, pool2, rows2, orders2, levels2, orbits2)
        except GateFail as e:
            killed = True
            killer = str(e).split(" ::")[0]
        report.append({"mutant": name, "target": target, "injects": what,
                       "killed": killed, "killed_by": killer,
                       "reaches_target": killer == target})
    globals()["MUT"] = None
    globals()["QUIET"] = False

    all_dead = all(m["killed"] for m in report)
    on_target = sum(1 for m in report if m["reaches_target"])
    say("    mutants: %d declared, %d killed, %d killed by their declared target"
        % (len(report), sum(m["killed"] for m in report), on_target))
    for m in report:
        if m["killed"] and not m["reaches_target"]:
            say("      off-target: %-26s declared %-38s killed by %s"
                % (m["mutant"], m["target"], m["killed_by"]))

    # ---- waiver ledger (#34): a gate is falsifiable or its waiver is verified
    by_gate = {}
    for m in report:
        if m["killed_by"]:
            by_gate.setdefault(m["killed_by"], []).append(m["mutant"])
    waivers = []
    for g in LD.rows:
        fals = by_gate.get(g["id"], [])
        if fals:
            waivers.append({"gate": g["id"], "status": "FALSIFIABLE",
                            "falsifiers": fals})
        else:
            forcing = FORCINGS.get(
                g["id"], "no falsifier and no registered forcing -- this row is "
                         "a defect in the instrument and must be repaired")
            waivers.append({"gate": g["id"], "status": "WAIVED",
                            "kind": g["kind"], "forcing": forcing,
                            "forcing_registered": g["id"] in FORCINGS,
                            "verified_evaluated": g["id"] in LD.evaluated})
    n_fals = sum(1 for w in waivers if w["status"] == "FALSIFIABLE")
    unverified = [w["gate"] for w in waivers
                  if w["status"] == "WAIVED"
                  and not (w["forcing_registered"] and w["verified_evaluated"])]
    probe = waivers + [{"gate": "G-INJECTED-FALSE-WAIVER", "status": "WAIVED",
                        "forcing_registered": False, "verified_evaluated": True}]
    probe_unverified = [w["gate"] for w in probe
                        if w["status"] == "WAIVED"
                        and not (w["forcing_registered"] and w["verified_evaluated"])]
    LD.gate("G-WAIVERS-VERIFIED",
            "every gate without a declared falsifier carries a registered "
            "forcing and is verified to have been evaluated (#34): a waiver "
            "claim is a gate claim.  The gate carries its own injection "
            "falsifier: an injected false waiver is detected",
            not unverified and probe_unverified == ["G-INJECTED-FALSE-WAIVER"],
            "falsifiable=%d waived=%d unverified=%s; injected false waiver "
            "detected=%s" % (n_fals, len(waivers) - n_fals, unverified or "none",
                             probe_unverified == ["G-INJECTED-FALSE-WAIVER"]))

    waivers.append({"gate": "G-WAIVERS-VERIFIED", "status": "WAIVED",
                    "kind": "MEASURED",
                    "forcing": FORCINGS["G-WAIVERS-VERIFIED"],
                    "forcing_registered": True, "verified_evaluated": True})
    n_fals = sum(1 for w in waivers if w["status"] == "FALSIFIABLE")

    # ---- assemble ---------------------------------------------------------
    R = build_receipt(S, LD, pool, rows, orders, levels, orbits)
    R["gates"] = LD.rows
    R["mutants"] = report
    R["waiver_ledger"] = waivers
    R["totals"] = {"gates": len(LD.rows), "gates_passed": sum(1 for g in LD.rows if g["passed"]),
                   "anchors": len(SOURCES) + len(PATH_VALUE_ANCHORS) + len(VERBATIM_ANCHORS),
                   "byte_anchors": len(SOURCES),
                   "path_value_anchors": len(PATH_VALUE_ANCHORS),
                   "verbatim_anchors": len(VERBATIM_ANCHORS),
                   "mutants": len(report), "mutants_killed": sum(m["killed"] for m in report),
                   "mutants_on_target": on_target,
                   "gates_falsifiable": n_fals,
                   "gates_waived": len(waivers) - n_fals,
                   "census_rows": len(rows), "pool": len(pool),
                   "never_falsified": len(waivers) - n_fals}
    R["compliance"] = compliance_sweep(LD)
    R["paper_claims"] = {"paper": PAPER_REL, "rendered": paper_claims(R)}
    R["paper_coverage"] = paper_coverage(R, S["_paper_text"])
    R["not_executed"] = [
        "the 9-point Moore stencil is not SWEPT at the admitted size; the "
        "Moore-ball collapse theorem settles every size above it over any "
        "field, and the 5-point stencil is swept at four sizes in two orderings",
        "the wider 5-point family at the admitted size is disclosed and not "
        "censused; the defect census runs on the 3-term axis stencil only",
        "indivisibility is DECLARED by the division-event times and is never "
        "measured: no existential stochastic-divisor search is run",
        "coefficients outside the declared 25-element alphabet are not swept; "
        "the order-5-and-above collapse and the Moore-ball collapse are "
        "theorems and alphabet-independent, and the alphabet-relative order-3 "
        "emptiness is irrelevant to the verdict",
        "no continuum or infinite-volume limit is taken",
        "no multi-excitation sector, no interaction term, and no field operator "
        "is constructed; 'field' appears only as the free-field ANALOG",
        "d = 3 is swept only for the locality threshold, not for the family",
    ]

    if not all_dead:
        say("")
        say("MUTANTS SURVIVED: %s" % [m["mutant"] for m in report if not m["killed"]])
        say("EXIT 1")
        sys.exit(1)

    # ---- print ------------------------------------------------------------
    emit_report(R, S)

    if write:
        with open(OUT_JSON, "w", encoding="utf-8") as f:
            json.dump(R, f, indent=1, sort_keys=True)
        with open(OUT_TXT, "w", encoding="utf-8") as f:
            f.write("\n".join(LOG) + "\n")

    if verify_paper:
        path = verify_paper if os.path.isabs(verify_paper) \
            else os.path.join(REPO, verify_paper)
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read()
        cov = paper_coverage(R, txt)
        print("PAPER CLAIM VERIFICATION (%s): %d claims, %d missing %s; %d "
              "distinct numerals over %d occurrences, %d covered by rendering, "
              "%d declared derived-in-text, uncovered %s"
              % (verify_paper, cov["claims"], len(cov["missing"]),
                 cov["missing"], cov["distinct_numerals"],
                 cov["numeral_occurrences"], cov["covered_by_rendering"],
                 cov["declared_derived_in_text"], cov["uncovered"] or "none"))
        sys.exit(1 if (cov["missing"] or cov["uncovered"]) else 0)

    sys.exit(0)


def emit_report(R, S):
    c = R["counts"]
    say("")
    say("-" * 78)
    say("ARENA (declared as data)")
    for k in ("boundary", "family", "law", "state", "arena", "division_events"):
        say("  %-16s %s" % (k, ARENA[k]))
    say("")
    say("ANCHORS")
    for r in R["verbatim_anchors"]:
        say("  verbatim   %-18s -> %-34s %s" % (r["id"], r["consumer_gate"],
                                                "present" if r["present"] else "MISSING"))
    for r in R["byte_anchors"]:
        say("  bytes      %-18s %s %s" % (r["id"], r["artifact"], r["measured"]))
    for r in R["path_value_anchors"]:
        say("  path-value %-18s %s/%s = %s" % (r["id"], r["source"], r["path"],
                                               json.dumps(r["expected"])[:44]))
    say("")
    say("THE STAGE: locality by the ported criterion (the FORCED connective, d=2)")
    for row in R["locality_sweep"]:
        if row["d"] == 2 and row["connective"] == CONNECTIVES[0]:
            say("  L=%d offsets=%2d neighbours=%2d complete=%-5s locality=%s"
                % (row["L"], row["offsets"], row["neighbours"],
                   row["complete"], row["locality"]))
    say("  parity witness: %s" % R["parity_witness"])
    say("")
    say("THE CONNECTIVE IS FORCED BY THE ANCHORED LINK SET")
    cf = R["connective_forcing"]
    say("  anchored links      %s" % cf["anchored_links"])
    say("  forced              %-24s %s" % (cf["forced_tag"], cf["reason_forced"]))
    say("  excluded            %-24s %s" % (cf["excluded_tag"], cf["reason_excluded"]))
    say("  admissible sizes    forced %s / excluded %s"
        % (cf["admissible_under_forced"], cf["admissible_under_excluded"]))
    say("  locality thresholds by connective and dimension:")
    for row in R["locality_threshold_table"]:
        say("    %-10s d=%d threshold=%s admits the anchored links=%s"
            % (row["connective_tag"], row["d"], row["threshold"],
               row["admits_anchored_links"]))
    say("")
    say("THE MOORE-BALL COLLAPSE THEOREM (legs measured)")
    say("  sizes checked       %s" % R["moore_ball_collapse"]["sizes"])
    say("  domain check        %s" % R["moore_ball_collapse"]["domain"])
    say("  alphabet independence: %s" % R["alphabet_independence"])
    say("")
    say("THE FIVE-POINT SWEEPS (leaves and solutions are the invariants;")
    say("the node count is an artifact of the declared offset ordering)")
    for row in R["five_point_sweeps"]:
        say("    L=%d %-13s nodes=%7d leaves=%5d non-monomial=%d"
            % (row["L"], row["ordering"], row["nodes_visited"],
               row["leaves_reached"], row["non_monomial"]))
    say("")
    say("THE FAMILY: unitary generators on the 3-term axis stencil, by ord(a)")
    for k in sorted(R["ord_census"], key=int):
        v = R["ord_census"][k]
        say("  ord=%s distinct=%4d monomial=%3d non-monomial=%3d"
            % (k, v["distinct_generators"], v["monomial"], v["non_monomial"]))
    say("  five-point extension at L=5: non-monomial=%d"
        % R["five_point_extension"]["non_monomial"])
    say("  admissible lattice sizes (locality AND non-monomial local axis): %s"
        % R["admissible_scales"])
    say("")
    say("THE POOL: %s" % R["pool_counts"])
    say("  transport levels: %s" % R["transport_levels"]["counts"])
    say("")
    say("THE DEFECT CENSUS")
    say("  ordered pairs                       %d" % c["pairs_total"])
    say("  pairs at maximal transport (%s)   %d" % (R["realization_census"]["maximal"],
                                                    c["pairs_at_maximal"]))
    say("  nonzero at maximal transport        %d" % c["nonzero_at_maximal"])
    say("  nonzero excluded below maximal      %d" % c["nonzero_excluded"])
    say("  distinct exact values               %d" % c["distinct_values"])
    say("  Markovian pairs / nonzero           %d / %d" % (c["markov_pairs"], c["markov_nonzero"]))
    say("  local pairs / nonzero               %d / %d" % (c["local_pairs"], c["local_nonzero"]))
    say("  non-local pairs / nonzero           %d / %d" % (c["nonlocal_pairs"], c["nonlocal_nonzero"]))
    say("")
    say("  the distinct exact defect values at maximal transport:")
    say("    " + ", ".join("%s x%d" % (v["value"], v["cells"]) for v in R["defect_values"]))
    say("")
    say("  the value census (first rows, exact):")
    for vr in R["defect_value_census"][:6]:
        cells = "; ".join("s=%s -> %s%s" % (tuple(cell[0]), cell[1],
                                            "" if cell[2] is None else " = " + cell[2])
                          for cell in vr["cells"])
        say("    %s o %s : %s" % (vr["V"], vr["U"], cells))
    say("")
    say("TWO-POINT STRUCTURE")
    say("  equal-time connected correlator: C0(0)=%s  C0(s!=0)=%s"
        % (R["equal_time"]["rational_zero"], R["equal_time"]["rational_nonzero"]))
    say("  composed-time table splits exactly into restarted + defect")
    say("  separations carrying a defect: %d; max defect radius %d"
        % (c["separations"], c["max_defect_radius"]))
    say("  generator orders present: %s" % c["orders"])
    for row in R["lightcone"][:4]:
        say("    %s radius by step %s" % (row["gen"], row["radius_by_step"]))
    say("")
    say("TRANSFORMATION-TYPE CLASSES")
    say("  extended group order %d -> %d classes; anchored chart group order %d "
        "-> %d classes" % (R["classes"]["extended_group_order"], c["classes_extended"],
                           R["classes"]["anchored_group_order"], c["classes_anchored"]))
    for o in R["classes"]["extended"]:
        say("    class %-5s size=%-3d kind=%-5s supp=%-4s radius=%s ord(axis)=%-4s "
            "level=%-8s order=%s"
            % (o["representative"], o["size"], o["kind"], o["support"], o["radius"],
               o["axis_ord"], o["level"], o["order"]))
    say("")
    say("  class labels: %d classes, %d distinct invariant tuples, %d with a "
        "direction label added"
        % (R["class_labels"]["classes"], R["class_labels"]["distinct_labels"],
           R["class_labels"]["with_direction_label"]))
    for sh in R["class_labels"]["shared"]:
        say("    shared label %s by %s" % (sh["label"], sh["classes"]))
    say("")
    say("THE COMMUTATOR CENSUS (the R5 datum)")
    for k in sorted(R["commutator_census"]):
        v = R["commutator_census"][k]
        if isinstance(v, dict):
            say("  %-32s %4d non-commuting of %4d ordered pairs"
                % (k, v["noncommuting"], v["pairs"]))
    say("")
    say("REALIZATION CENSUS (the mandatory gate)")
    for lv in LEVELS:
        say("  %-9s %d generators" % (lv, R["realization_census"]["levels"][lv]))
    say("  maximal declared transport: %s" % R["realization_census"]["maximal"])
    say("  defects entering the verdict: only at %s" % R["realization_census"]["maximal"])
    say("  every classification verified by a second route at %d generators"
        % R["transport_levels"]["verified_by_second_route"])
    say("")
    say("LIKE FOR LIKE")
    say("  %s" % R["like_for_like"])
    say("")
    say("RADIUS PROFILES AND THE CONE BOUND")
    say("  %s" % R["radius_profiles"])
    say("  %s" % R["lightcone_vacuity"])
    say("")
    say("STATE MOTION")
    say("  %s" % {k: v for k, v in R["state_motion"].items() if k != "probe_rows"})
    say("")
    say("PAPER CLAIM COVERAGE")
    say("  %s" % R["paper_coverage"])
    say("")
    say("THE VERDICT")
    say("")
    v = R["verdict"]["string"]
    for i in range(0, len(v), 74):
        say("  " + v[i:i + 74])
    say("")
    say("TOTALS: %s" % json.dumps(R["totals"], sort_keys=True))
    say("")
    say("NOT EXECUTED")
    for n in R["not_executed"]:
        say("  - %s" % n)
    say("")
    say("ALL GATES PASSED (%d/%d); ALL MUTANTS DEAD (%d/%d)"
        % (R["totals"]["gates_passed"], R["totals"]["gates"],
           R["totals"]["mutants_killed"], R["totals"]["mutants"]))
    say("EXIT 0")


if __name__ == "__main__":
    main()
