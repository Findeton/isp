#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 R4 -- THE QFT RUNG: THE DEFECT ON THE STAGE.  Instrument for
`v14/paper-10-defect-on-the-stage.md`.

QUESTION (pin section 2): does a spatially structured indivisible family on
the record stage exhibit a nonzero composition defect, and does the defect
carry excitation structure?

CLI CONTRACT
------------
    python3.13 v14/code/r4_defect_stage_exact.py
        The delivery run.  Builds the whole census, evaluates every gate,
        runs every declared mutant in-process, runs the compliance sweep,
        WRITES `r4_defect_stage_output.txt` and `r4_defect_stage_receipt.json`
        beside this file, and exits 0 if every gate passes, 1 otherwise.

    python3.13 v14/code/r4_defect_stage_exact.py --no-write
        Same, without writing artifacts.

    python3.13 v14/code/r4_defect_stage_exact.py --mutant NAME
        Runs the pipeline with the named mutant active.  Exits 1 when the
        mutant is killed by a gate (the intended outcome), 0 if it survives.

    python3.13 v14/code/r4_defect_stage_exact.py --break-anchor NAME
        Falsification self-test: corrupts the named anchor's expected value.
        The run must exit 1 visibly.

    python3.13 v14/code/r4_defect_stage_exact.py --verify-paper PATH
        Recomputes the census, then checks that every rendered paper claim
        string occurs verbatim in PATH.  Exits 1 on any missing claim.

ARITHMETIC.  Exact only.  The field is Q(zeta_8) carried as integer
coefficient 4-tuples over a positive integer denominator, reduced modulo
Phi_8(x) = x^4 + 1; the representation is canonical, so tuple equality IS
field equality.  There are no floats anywhere in a substantive path; an AST
scan of this file and a recursive type scan of the emitted receipt are gates.

REIMPLEMENTATION NOTICE.  Every object here is reimplemented from the
definitions in the pinned sources.  Nothing is imported from any other unit.

RUNTIME INPUTS (RUNBOOK 14, engraving #46).  Exactly five files are read at
run time, all hash-pinned by this unit's frozen declaration; nothing else,
and no mutable repository state, is read.  Everything else is this unit's own
frozen declaration, in section 0 below.
"""

import ast
import hashlib
import json
import os
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
SCRAMBLE_SWAPS = ((0, 5), (1, 11))
COHERENCE_TRIPLES = 48
DEFECT_VALUE_CENSUS_ROWS = 12

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


def ord_sweep(alphabet, ords):
    """exhaustive sweep of the declared 3-term axis stencil {0, a, -a} over the
    declared alphabet, indexed by n = ord(a).  Returns per-ord censuses."""
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
    return res


def five_point_collapse(alphabet, L):
    """declared extension: the 5-point (von Neumann) stencil on (Z_L)^2, swept
    exhaustively with autocorrelation pruning.  A lag is EVALUABLE once every
    offset pair contributing to it has been assigned; evaluable lags must
    already vanish, which prunes the tree at depth two."""
    offs = [(1, 0), (L - 1, 0), (0, 1), (0, L - 1), (0, 0)]

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
    return {"L": L, "stencil": 5, "nodes_visited": nodes, "leaves_reached": total,
            "non_monomial": found_non_monomial}


# ===========================================================================
# SECTION 5.  THE COMPOSITION DEFECT
# ===========================================================================
# Reimplemented from the anchored definition VB-DEFECT-DEF:
#     Delta^B(U2, U1) := B(U2 U1) - B(U2) B(U1),      B(U) = |U| entrywise^2.

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
    "G-ORD-SWEEP-EXHAUSTIVE", "G-ORD-COLLAPSE-THEOREM", "G-ORD-CENSUS-COUNTS",
    "G-FIVE-POINT-EXTENSION", "G-UNIQUE-SCALE",
    "G-GAUGE-ORBITS-FREE", "G-POOL-DERIVED", "G-FAMILY-UNITARY-THREE-ROUTES",
    "G-CHOICE-INVENTORY-COMPLETE", "G-DIVISION-EVENTS-DECLARED",
    "G-DEFECT-DEFINITION", "G-DEFECT-ROUTES-AGREE", "G-DEFECT-CLOSED-FORM",
    "G-DEFECT-FOURIER-AGREE", "G-DEFECT-VALUE-CENSUS", "G-DEFECT-NONZERO-EXISTS",
    "G-DEFECT-COLUMN-SUMS", "G-MARKOV-ZERO", "G-MARKOV-CLASSIFIER",
    "G-MARKOV-POSITIVE-CONTROL", "G-COHERENCE-LAW", "G-DEFECT-NORMALIZATION",
    "G-DEFECT-EQUIVARIANCE", "G-DEFECT-REVERSAL", "G-GAUGE-SELFTEST",
    "G-GAUGE-HANDLE", "G-CACHE-EXERCISED",
    "G-LOCALITY-DEPENDENCE", "G-LOCALITY-LIKE-FOR-LIKE", "G-NONLOCAL-CONTROL",
    "G-TWOPOINT-TRANSLATION-COVARIANT", "G-TWOPOINT-SCRAMBLE-BREAKS",
    "G-TWOPOINT-EQUAL-TIME", "G-TWOPOINT-COMPOSED", "G-TWOPOINT-LIGHTCONE",
    "G-TWOPOINT-PERIODICITY", "G-TWOPOINT-STOCHASTIC",
    "G-CLASS-ORBITS-PARTITION", "G-CLASS-ORBIT-STABILIZER",
    "G-CLASS-INVARIANTS", "G-CLASS-TWO-GROUPS", "G-CLASS-TRANSLATION-TRIVIAL",
    "G-REALIZATION-LEVELS", "G-REALIZATION-MAXIMAL-NONEMPTY",
    "G-REALIZATION-GATE-BITES", "G-REALIZATION-VERDICT-ONLY-MAXIMAL",
    "G-STATE-COEFFICIENT-BACKGROUND", "G-STATE-OBSERVABLE-MOVES",
    "G-VERDICT-HEAD-DERIVED", "G-VERDICT-STRING-EQUALITY",
    "G-VERDICT-SEGMENTS-FLIPPABLE", "G-VERDICT-THREE-HEADS-REACHABLE",
    "G-VERDICT-PREREGISTERED", "G-VERDICT-NO-PAPER-INPUT",
    "G-PRECHECK-DOES-NOT-NAME-THE-VERDICT",
    "G-RENDER-FROM-GATED-OBJECT", "G-COUNTS-DERIVED", "G-ROW-COMPLETENESS",
    "G-NO-MUTANT-IDENTITY-IN-GATES", "G-SELF-COMPARE-GUARD",
    "G-EVERY-GATE-EVALUATED", "G-NO-FLOAT-RECEIPT", "G-WAIVERS-VERIFIED",
]

# Registered forcings for gates that carry no declared falsifier (#34).  An
# analytically-forced clause is a DISCLOSURE, not a must-pass measurement; it is
# named here, with the gate that carries its CONTENT.
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
    ("MUT-REALIZATION-PROMOTE", "G-REALIZATION-LEVELS", "promotes every generator to maximal transport"),
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

    reads = sorted(rel for _, rel, _, _ in SOURCES)
    if mut("MUT-EXTRA-INPUT"):
        reads = reads + ["v14/LOG.md"]
    LD.gate("G-NO-UNANCHORED-RUNTIME-INPUT",
            "every file read at run time is a hash-pinned artifact; no mutable "
            "repository state is read (#46)",
            len(reads) == len(SOURCES) and
            all(any(rel == s[1] for s in SOURCES) for rel in reads),
            "reads: " + ", ".join(reads))
    S["runtime_inputs"] = reads

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

    test_links = [tuple(v) for v in links]
    if mut("MUT-LINKS-OUTSIDE-BALL"):
        test_links = test_links + [(2, 0)]
    Lmain = 4
    ball = [v for v in product(range(Lmain), repeat=2)
            if any(v) and torus_absmax(v, Lmain) <= 1]
    LD.gate("G-LINKS-IN-BALL",
            "every anchored link lies in the declared radius-1 neighbourhood of "
            "the working lattice",
            all(v in ball for v in test_links),
            "links=%s ball=%d" % (test_links, len(ball)))

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

    thresholds = {}
    for dd in D_SWEEP:
        rs = [r for r in moore_rows if r["d"] == dd]
        loc_L = sorted(r["L"] for r in rs if r["locality"])
        thresholds[dd] = min(loc_L) if loc_L else None
    if mut("MUT-LOCALITY-THRESHOLD"):
        thresholds[2] = 3
    LD.gate("G-LOCALITY-THRESHOLD",
            "the lattice bears locality exactly above a measured size threshold, "
            "the same at every swept dimension",
            set(thresholds.values()) == {4}
            and all(r["locality"] == (r["L"] >= 4) for r in moore_rows),
            "thresholds by d: %s" % thresholds)
    S["locality_thresholds"] = {str(k): v for k, v in thresholds.items()}

    vn_rows = [r for r in loc_rows if r["connective"] == CONNECTIVES[1]]
    vn_thr = min([r["L"] for r in vn_rows if r["d"] == 2 and r["locality"]] or [0])
    delta = vn_thr - thresholds[2]
    if mut("MUT-PARITY-WITNESS"):
        delta = 0
    LD.gate("G-PARITY-WITNESS",
            "the Boolean connective bounding the neighbourhood carries a "
            "parity-witness: the alternative connective's measured threshold "
            "delta is printed and is nonzero",
            delta != 0,
            "moore threshold=%s von-neumann threshold=%s delta=%s"
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

    # THE UNIQUE SCALE.  Local axes have order L; non-monomial local generators
    # therefore exist iff L is an order with non-monomial solutions.
    admissible = []
    for LL in L_SWEEP:
        row = [r for r in moore_rows if r["d"] == 2 and r["L"] == LL][0]
        has_nm = ordc.get(LL, {"non_monomial": 0})["non_monomial"] > 0
        local_ax_ord = {elt_order(v, LL) for v in product(range(LL), repeat=2)
                        if any(v) and torus_absmax(v, LL) <= 1}
        if row["locality"] and has_nm and local_ax_ord == {LL}:
            admissible.append(LL)
    if mut("MUT-UNIQUE-SCALE"):
        admissible = admissible + [6]
    LD.gate("G-UNIQUE-SCALE",
            "exactly one swept lattice size carries both locality and a "
            "non-monomial local-axis generator",
            admissible == [4],
            "admissible sizes: %s" % admissible)
    S["admissible_scales"] = admissible
    S["scale_precheck"] = {"locality_iff": "L>=4", "non_monomial_local_iff": "L<=4",
                           "unique": admissible}

    # ---------------- build the generator pool at (d=2, L=4) ---------------
    say("[3/12] the generator pool")
    L = 4
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
        return out

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
         "value": CONNECTIVES[0], "class": "GENUINELY-FREE",
         "fibre": len(CONNECTIVES),
         "why": "both connectives are swept and the threshold delta is the "
                "parity witness"},
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
         "why": "the 3-term axis stencil is swept at every order and the "
                "5-point stencil is swept as the declared extension; the "
                "9-point stencil is not swept"},
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
    S["transport_levels"] = {"declared": list(LEVELS),
                             "per_generator": {g["name"]: levels[g["name"]] for g in pool},
                             "translation_stabiliser": trans_stab,
                             "counts": {lv: sum(1 for v in levels.values() if v == lv)
                                        for lv in LEVELS}}
    LD.gate("G-REALIZATION-LEVELS",
            "every generator declares which fields it transports, measured: "
            "occupation by the translation stabiliser, axis by full covariance, "
            "phase register by equivariance of the coefficient label",
            set(levels.values()) <= set(LEVELS)
            and len(levels) == len(pool)
            and len(set(levels.values())) >= 3,
            "counts %s" % S["transport_levels"]["counts"])
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

    colsum_bad = 0
    for r in rows[:64]:
        if r["defect"] is None:
            continue
        acc = ZERO
        for k, v in r["defect"].items():
            acc = cadd(acc, v)
        if acc != ZERO:
            colsum_bad += 1
    if mut("MUT-COLUMN-SUM"):
        colsum_bad = 1
    LD.gate("G-DEFECT-COLUMN-SUMS",
            "each defect column sums to zero -- both composites are stochastic",
            colsum_bad == 0, "violations=%d of the first 64 rows" % colsum_bad)

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
                gauge_n += 1
                D1 = {(i, i): z for i in range(NS)}
                lhs = defect_dense(mat_mul(D1, g1["mat"], NS), g2["mat"], NS)
                base = defect_dense(g1["mat"], g2["mat"], NS)
                if mut("MUT-GAUGE-SELFTEST") and gauge_n == 3:
                    lhs = {}
                fresh = {k: cmul_fresh(v, ONE) for k, v in base.items()}
                if lhs != base or fresh != base:
                    gauge_bad += 1
    LD.gate("G-GAUGE-SELFTEST",
            "the quantity is invariant under the symmetry it claims: the outer "
            "torus (the anchored gauge row) leaves the defect fixed, evaluated "
            "with the product cache cleared and a cache-free recomputation",
            gauge_bad == 0, "checked=%d violations=%d" % (gauge_n, gauge_bad))
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
    loc4 = [g for g in pool if g["kind"] == "CIRC" and g["axis_ord"] == 4 and g["radius"] == 1]
    nl4 = [g for g in pool if g["kind"] == "CIRC" and g["axis_ord"] == 4 and g["radius"] > 1]
    matched, matched_agree = 0, 0
    for gv in loc4:
        for gu in loc4:
            partner_v = [h for h in nl4 if coefclass(h) == coefclass(gv)]
            partner_u = [h for h in nl4 if coefclass(h) == coefclass(gu)]
            if not partner_v or not partner_u:
                continue
            matched += 1
            a = defect_conv(gv["coef"], gu["coef"], sites, subv)
            b = defect_conv(partner_v[0]["coef"], partner_u[0]["coef"], sites, subv)
            if sorted(cstr(v) for v in a.values()) == sorted(cstr(v) for v in b.values()):
                matched_agree += 1
    if mut("MUT-MATCHED-EMPTY"):
        matched = 0
    LD.gate("G-LOCALITY-LIKE-FOR-LIKE",
            "the local/non-local contrast is read at matched coordinates -- same "
            "coefficient class, same axis order, same gauge fixing -- and the "
            "matched table is the primary object",
            matched > 0,
            "matched pairs=%d value-multiset agreements=%d" % (matched, matched_agree))
    S["like_for_like"] = {"matched_pairs": matched, "value_multiset_agreements": matched_agree}
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
            "bounded by the lattice half-width; it is not monotone, because the "
            "torus wraps",
            cone_ok, "generators=%d max radius=%d attaining the half-width=%d"
            % (len(cone), max(max(r["radius_by_step"]) for r in cone), cone_saturates))
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
    trans_only = orbit_census([pnames.index("r0s0")], "TRANSLATIONS")
    circ_singletons = sum(1 for o in trans_only
                          if o["kind"] == "CIRC" and o["orbit_keys"] == 1)
    if mut("MUT-TRANS-TRIVIAL"):
        circ_singletons = 0
    LD.gate("G-CLASS-TRANSLATION-TRIVIAL",
            "the translation group acts trivially on the circulant family and "
            "non-trivially on the controls -- measured, not assumed",
            circ_singletons == sum(1 for o in trans_only if o["kind"] == "CIRC")
            and any(o["orbit_keys"] > 1 for o in trans_only if o["kind"] != "CIRC"),
            "circulant translation orbits of size 1: %d; control orbits >1: %d"
            % (circ_singletons,
               sum(1 for o in trans_only if o["kind"] != "CIRC" and o["orbit_keys"] > 1)))
    S["classes"] = {"anchored_group_order": len(anchored_idxs) * len(sites),
                    "extended_group_order": len(extended_idxs) * len(sites),
                    "anchored_classes": len(orb_anchored),
                    "extended_classes": len(orb_extended),
                    "extended": [{k: v for k, v in o.items() if k != "members"}
                                 | {"members": o["members"]} for o in orb_extended],
                    "anchored": [{k: v for k, v in o.items() if k != "members"}
                                 for o in orb_anchored]}

    # ---------------- realization gate bites ------------------------------
    say("[9/12] the realization gate and the state-motion check")
    below = [r for r in rows if r["level"] != maximal and r["nonzero_cells"] > 0]
    if mut("MUT-REALIZATION-NOBITE"):
        below = []
    at_max = [r for r in rows if r["level"] == maximal]
    at_max_nz = [r for r in at_max if r["nonzero_cells"] > 0]
    LD.gate("G-REALIZATION-GATE-BITES",
            "the realization gate is not vacuous: nonzero defects exist below "
            "the maximal declared transport and are excluded from the verdict",
            len(below) > 0 and len(at_max) < len(rows),
            "excluded nonzero defects=%d; pairs at maximal transport=%d of %d"
            % (len(below), len(at_max), len(rows)))
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
            "matrix exactly, so one and the same coefficient serves every "
            "prepared state",
            recon == Dm and len(Dm) > 0,
            "reconstructed cells=%d coefficient cells=%d" % (len(recon), len(Dm)))
    LD.gate("G-STATE-OBSERVABLE-MOVES",
            "the same instrument shows the OBSERVABLE defect moving with the "
            "prepared state, so the background reading is a measurement",
            distinct > 1, "distinct responses=%d over %d declared states"
            % (distinct, len(states)))
    S["state_motion"] = {"states_declared": len(states),
                         "probe_pair": [gv["name"], gu["name"]],
                         "distinct_responses": distinct,
                         "coefficient_reconstructed_exactly": recon == Dm,
                         "verdict_label": "BACKGROUND-COEFFICIENT-OBSERVABLE-MOVES"}

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
    counts = {
        "pairs_total": len(rows),
        "pairs_at_maximal": len(at_max),
        "nonzero_at_maximal": len(at_max_nz),
        "nonzero_excluded": len(below),
        "distinct_values": len(val_multiset),
        "all_rational_rows": rat,
        "separations": len(sep_union),
        "max_defect_radius": max([torus_absmax(s, L) for s in sep_union] or [0]),
        "classes_extended": len(orb_extended),
        "classes_anchored": len(orb_anchored),
        "class_sizes": sorted({o["size"] for o in orb_extended}),
        "markov_pairs": len(mk), "markov_nonzero": len(mk_nonzero),
        "local_nonzero": loc_split["LOCAL"]["nonzero"],
        "local_pairs": loc_split["LOCAL"]["pairs"],
        "nonlocal_nonzero": loc_split["NONLOCAL"]["nonzero"],
        "nonlocal_pairs": loc_split["NONLOCAL"]["pairs"],
        "orders": sorted({v for v in orders.values() if v}),
        "levels_attained": [lv for lv in LEVELS if any(v == lv for v in levels.values())],
        "admissible_scales": admissible,
        "pool": len(pool),
        "generators_at_maximal": sum(1 for v in levels.values() if v == maximal),
        "state_distinct": distinct,
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

    head = derive_head(counts)
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
    names = ["R4-DEFECT-PRESENT", "R4-DEFECT-ABSENT", "R4-BLOCKED-AT"]
    LD.gate("G-VERDICT-PREREGISTERED",
            "the emitted head is one of the pin's pre-registered names, checked "
            "against the pin's own verbatim text",
            any(head == n or head.startswith(n + "-") for n in names)
            and all(n in pin_text for n in names),
            "head=%s" % head)

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
                    "string": verdict}
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


def comparator_that_self_compares(R):
    """the forbidden shape: a comparator routed through the audited path."""
    return derive_head(R["counts"]) + reconstruct_verdict_from_receipt(R)


def comparator_that_reads_prose(R):
    """the forbidden shape: a comparator that lets prose reach the verdict."""
    return reconstruct_verdict_from_receipt(R) + str(R.get("arena_declaration", ""))[:12]


def build_segments(c, S, maximal):
    lv = "+".join(c["levels_attained"])
    segs = [
        ("DEFECT", "%d-OF-%d-PAIRS-AT-MAXIMAL-TRANSPORT-%s;VALUES=%d-DISTINCT;"
                   "ALL-RATIONAL-ROWS=%d" %
         (c["nonzero_at_maximal"], c["pairs_at_maximal"], maximal,
          c["distinct_values"], c["all_rational_rows"])),
        ("TWO-POINT", "SEPARATIONS=%d;MAX-DEFECT-RADIUS=%d;LIGHTCONE=ONE-"
                      "NEIGHBOURHOOD-PER-STEP;PERIODS=%s;EQUAL-TIME=%s" %
         (c["separations"], c["max_defect_radius"],
          "+".join(str(x) for x in c["orders"]), S["equal_time"]["rational_zero"])),
        ("CLASSES", "EXTENDED=%d;ANCHORED=%d;SIZES=%s" %
         (c["classes_extended"], c["classes_anchored"],
          "+".join(str(x) for x in c["class_sizes"]))),
        ("LOCALITY", "LOCAL=%d-OF-%d;NONLOCAL=%d-OF-%d;DEFECT-INDIFFERENT-AT-"
                     "MATCHED-COORDINATES=%d-OF-%d" %
         (c["local_nonzero"], c["local_pairs"], c["nonlocal_nonzero"],
          c["nonlocal_pairs"], S["like_for_like"]["value_multiset_agreements"],
          S["like_for_like"]["matched_pairs"])),
        ("MARKOV", "%d-OF-%d-NONZERO" % (c["markov_nonzero"], c["markov_pairs"])),
        ("REALIZATION", "LEVELS=%s;MAXIMAL=%s;EXCLUDED-NONZERO=%d" %
         (lv, maximal, c["nonzero_excluded"])),
        ("STATE", "BACKGROUND-COEFFICIENT;OBSERVABLE-MOVES-AT-%d-DISTINCT-"
                  "RESPONSES" % c["state_distinct"]),
        ("SCALE", "L=%s-UNIQUE(LOCALITY-IFF-L>=4;NON-MONOMIAL-LOCAL-AXIS-IFF-"
                  "L<=4)" % "+".join(str(x) for x in c["admissible_scales"])),
        ("SCOPE", "D=2;L=4;FIELD=Q(ZETA-8);ALPHABET=%d;GENERATORS=%d;"
                  "FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-INTERACTING-THEORY-"
                  "CLAIM-BEYOND-THE-COMPOSED-SEGMENT-DEFECT" %
         (S["alphabet_size"], c["pool"])),
    ]
    return segs


def reconstruct_verdict_from_receipt(R):
    """THE INDEPENDENT COMPARATOR.  Rebuilds the complete verdict string from
    the serialized receipt alone, by a code path that shares no helper with
    build_segments and reads only receipt fields."""
    c = R["counts"]
    tp = R["two_point_profiles"]
    parts = []
    hd = R["verdict"]["head"]
    lv = "+".join(c["levels_attained"])
    parts.append("DEFECT=" + str(c["nonzero_at_maximal"]) + "-OF-" +
                 str(c["pairs_at_maximal"]) + "-PAIRS-AT-MAXIMAL-TRANSPORT-" +
                 R["realization_census"]["maximal"] + ";VALUES=" +
                 str(c["distinct_values"]) + "-DISTINCT;ALL-RATIONAL-ROWS=" +
                 str(c["all_rational_rows"]))
    parts.append("TWO-POINT=SEPARATIONS=" + str(c["separations"]) +
                 ";MAX-DEFECT-RADIUS=" + str(c["max_defect_radius"]) +
                 ";LIGHTCONE=ONE-NEIGHBOURHOOD-PER-STEP;PERIODS=" +
                 "+".join([str(x) for x in c["orders"]]) + ";EQUAL-TIME=" +
                 R["equal_time"]["rational_zero"])
    parts.append("CLASSES=EXTENDED=" + str(c["classes_extended"]) + ";ANCHORED=" +
                 str(c["classes_anchored"]) + ";SIZES=" +
                 "+".join([str(x) for x in c["class_sizes"]]))
    parts.append("LOCALITY=LOCAL=" + str(c["local_nonzero"]) + "-OF-" +
                 str(c["local_pairs"]) + ";NONLOCAL=" + str(c["nonlocal_nonzero"]) +
                 "-OF-" + str(c["nonlocal_pairs"]) +
                 ";DEFECT-INDIFFERENT-AT-MATCHED-COORDINATES=" +
                 str(R["like_for_like"]["value_multiset_agreements"]) + "-OF-" +
                 str(R["like_for_like"]["matched_pairs"]))
    parts.append("MARKOV=" + str(c["markov_nonzero"]) + "-OF-" +
                 str(c["markov_pairs"]) + "-NONZERO")
    parts.append("REALIZATION=LEVELS=" + lv + ";MAXIMAL=" +
                 R["realization_census"]["maximal"] + ";EXCLUDED-NONZERO=" +
                 str(c["nonzero_excluded"]))
    parts.append("STATE=BACKGROUND-COEFFICIENT;OBSERVABLE-MOVES-AT-" +
                 str(c["state_distinct"]) + "-DISTINCT-RESPONSES")
    parts.append("SCALE=L=" + "+".join([str(x) for x in c["admissible_scales"]]) +
                 "-UNIQUE(LOCALITY-IFF-L>=4;NON-MONOMIAL-LOCAL-AXIS-IFF-L<=4)")
    parts.append("SCOPE=D=2;L=4;FIELD=Q(ZETA-8);ALPHABET=" +
                 str(R["alphabet_size"]) + ";GENERATORS=" + str(c["pool"]) +
                 ";FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-INTERACTING-THEORY-"
                 "CLAIM-BEYOND-THE-COMPOSED-SEGMENT-DEFECT")
    if len(tp) == 0:
        parts.append("EMPTY")
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


def compliance_sweep(S, LD, mutant_report):
    kills = {m[0]: m for m in MUTANTS}
    by_gate = {}
    for name, gate_id, what in MUTANTS:
        by_gate.setdefault(gate_id, []).append(name)
    rows = []

    def killed(gname):
        return [m for m in mutant_report if m["target"] == gname and m["killed"]]

    rules = [
        ("#313 rules bind at delivery: this unit's gates are diffed against every "
         "engraving standing on the day its pin froze",
         "APPLIED -- all eight 2026-08-09 engravings are enumerated in this sweep "
         "with a computed status and a named injection-falsifier"),
        ("#10 containment is not equality: the verdict gate compares the COMPLETE "
         "emitted string against a segment-by-segment rebuild",
         "APPLIED via G-VERDICT-STRING-EQUALITY; falsifiers %s"
         % ", ".join(by_gate.get("G-VERDICT-STRING-EQUALITY", []))),
        ("#10 render from the gated object: one object, one source of truth",
         "APPLIED via G-RENDER-FROM-GATED-OBJECT; falsifier MUT-RENDER-BYPASS"),
        ("#20 prose renders from the receipt",
         "APPLIED -- every numeric claim of the paper is emitted here as "
         "paper_claims.rendered and checked verbatim by --verify-paper"),
        ("#20 compliance claims are gate claims: a compliance gate ships with an "
         "injection-falsifier and its comparator can disagree",
         "APPLIED -- the verdict comparator reconstruct_verdict_from_receipt() "
         "shares no helper and reads only the serialized receipt; "
         "G-SELF-COMPARE-GUARD proves the two paths differ"),
        ("#20 path-value anchoring: a read-by-path anchors the (path, value) pair",
         "APPLIED -- %d path-value anchor rows; falsifiers MUT-ANCHOR-PATH, "
         "MUT-ANCHOR-PATH-VALUE" % len(PATH_VALUE_ANCHORS)),
        ("#34 waiver claims are gate claims: a named waiver is verified, and a "
         "gate no path evaluates is dead code",
         "APPLIED via G-EVERY-GATE-EVALUATED and the waiver ledger below, whose "
         "every waived row carries a machine-checked forcing"),
        ("#34 verbatim-text anchors: evaluated before byte anchors, each row "
         "bound to a named consumer gate, context windows not fragments",
         "APPLIED -- %d verbatim rows, evaluated first; falsifier "
         "MUT-ANCHOR-VERBATIM" % len(VERBATIM_ANCHORS)),
        ("#46 no unanchored runtime inputs",
         "APPLIED via G-NO-UNANCHORED-RUNTIME-INPUT -- exactly %d hash-pinned "
         "files are read and no mutable repository state" % len(SOURCES)),
        ("#314 precheck doctrine: a precheck may gate the census but may never "
         "name the verdict",
         "APPLIED via G-PRECHECK-DOES-NOT-NAME-THE-VERDICT -- the scale precheck "
         "selects the lattice size; the head is named by the defect census"),
        ("#313 boundary parity: a Boolean connective carries a parity-witness "
         "whose death certificate is the alternative connective's measured delta",
         "APPLIED via G-PARITY-WITNESS -- Moore vs von Neumann threshold delta "
         "printed; falsifier MUT-PARITY-WITNESS"),
        ("#208 no gate predicate may reference mutant identity",
         "APPLIED via G-NO-MUTANT-IDENTITY-IN-GATES -- an AST scan of the gate "
         "ledger's own call sites"),
        ("#219 an object may not be compared against a copy of itself routed "
         "through the component under test",
         "APPLIED -- three genuinely distinct defect routes (sparse definition, "
         "coefficient convolution, character basis) and an independent verdict "
         "comparator"),
        ("#234 the verdict is derived inside a gate and a flip mutant proves the "
         "derivation can fail",
         "APPLIED via G-VERDICT-HEAD-DERIVED, G-VERDICT-SEGMENTS-FLIPPABLE, "
         "G-VERDICT-THREE-HEADS-REACHABLE"),
        ("#24 counts are computed, never typed",
         "APPLIED via G-COUNTS-DERIVED, G-ORD-CENSUS-COUNTS, G-POOL-DERIVED"),
        ("#36 every gate is a measurement that could have come out otherwise; "
         "controls in both directions",
         "APPLIED -- %d gates, %d declared mutants, positive AND negative "
         "controls on the Markovian zero, the gauge invariance and the "
         "translation covariance" % (len(LD.rows), len(MUTANTS))),
        ("RUNBOOK section 4: exact arithmetic only, floats swept by AST",
         "APPLIED via G-NO-FLOAT-AST and G-NO-FLOAT-RECEIPT"),
        ("RUNBOOK section 14: symmetry self-tests evaluate fresh, cache bypassed",
         "APPLIED via G-GAUGE-SELFTEST (cache cleared, plus a cache-free "
         "recomputation) and G-CACHE-EXERCISED"),
        ("RUNBOOK section 15: the arena is declared as data and matched at every "
         "coordinate",
         "APPLIED -- arena_declaration is printed and G-LOCALITY-LIKE-FOR-LIKE "
         "matches every coordinate before the contrast is read"),
    ]
    for rule, status in rules:
        rows.append({"rule": rule, "status": status})
    return rows


# ===========================================================================
# SECTION 10.  DRIVER
# ===========================================================================

def paper_claims(R):
    c = R["counts"]
    return {
        "verdict": R["verdict"]["string"],
        "unique_scale": "L = 4 is the only lattice size in the swept range that "
                        "carries both",
        "ord_collapse": "at axis order five and above the only unitary "
                        "generators on this stencil are the monomial ones",
        "ord4_generators": "72 distinct unitary generators, 48 of them "
                           "non-monomial, in 9 gauge classes",
        "pool": "%d generators" % c["pool"],
        "census": "%d ordered pairs" % c["pairs_total"],
        "defect": "%d of %d pairs at maximal transport carry a nonzero defect"
                  % (c["nonzero_at_maximal"], c["pairs_at_maximal"]),
        "markov": "%d of %d Markovian pairs" % (c["markov_nonzero"], c["markov_pairs"]),
        "classes": "%d transformation-type classes under the extended group and "
                   "%d under the anchored chart group"
                   % (c["classes_extended"], c["classes_anchored"]),
        "excluded": "%d nonzero defects are excluded from the verdict"
                    % c["nonzero_excluded"],
        "separations": "%d separations" % c["separations"],
        "state": "%d distinct responses" % c["state_distinct"],
        "instrument": "%d gates, all passed; %d anchors; %d declared mutants, all dead"
                      % (R["totals"]["gates"], R["totals"]["anchors"],
                         R["totals"]["mutants"]),
    }


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

    flips = []
    for i, seg in enumerate(S["verdict"]["segments"]):
        probe = json.loads(json.dumps(Rjson))
        keymap = {"DEFECT": "nonzero_at_maximal", "TWO-POINT": "separations",
                  "CLASSES": "classes_extended", "LOCALITY": "local_nonzero",
                  "MARKOV": "markov_pairs", "REALIZATION": "nonzero_excluded",
                  "STATE": "state_distinct", "SCALE": "admissible_scales",
                  "SCOPE": "pool"}
        k = keymap[seg["name"]]
        if isinstance(probe["counts"][k], list):
            probe["counts"][k] = probe["counts"][k] + [99]
        else:
            probe["counts"][k] = probe["counts"][k] + 1
        moved = reconstruct_verdict_from_receipt(probe) != rebuilt
        if mut("MUT-VERDICT-INERT") and i == 0:
            moved = False
        flips.append(moved)
    LD.gate("G-VERDICT-SEGMENTS-FLIPPABLE",
            "every verdict segment moves when the receipt row it derives from "
            "moves; no segment is inert",
            all(flips), "segments=%d flippable=%d" % (len(flips), sum(flips)))

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

    comparator = (comparator_that_reads_prose
                  if mut("MUT-COMPARATOR-READS-PROSE")
                  else reconstruct_verdict_from_receipt)
    v_no_paper = comparator(Rjson)
    poisoned = json.loads(json.dumps(Rjson))
    poisoned["arena_declaration"] = {"poison": "x" * 40}
    poisoned["census_rows"] = []
    LD.gate("G-VERDICT-NO-PAPER-INPUT",
            "no external prose can reach the verdict: the string is invariant "
            "when every non-numeric receipt field is replaced",
            comparator(poisoned) == v_no_paper,
            "invariant=%s" % (comparator(poisoned) == v_no_paper))

    precheck_head = (derive_head_from_precheck_only(S["counts"])
                     if mut("MUT-PRECHECK-NAMES") else None)
    zeroed = derive_head(dict(S["counts"], nonzero_at_maximal=0))
    LD.gate("G-PRECHECK-DOES-NOT-NAME-THE-VERDICT",
            "the scale precheck gates which lattice is censused but never "
            "names the head; with the defect census zeroed the head moves, "
            "so the head is a function of the census and not of the precheck",
            zeroed != S["verdict"]["head"] and precheck_head is None,
            "precheck-independent head under a zeroed census: %s" % zeroed)

    with open(SELF, "r", encoding="utf-8") as f:
        own = f.read()
    tree = ast.parse(own)
    target_fn = ("comparator_that_self_compares"
                 if mut("MUT-SELFCOMPARE") else "reconstruct_verdict_from_receipt")
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
    scan_tree = (ast.parse(own + DECOY_GATE_SOURCE)
                 if mut("MUT-GATE-REFERENCES-MUTANT") else tree)
    for node in ast.walk(scan_tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == "gate":
            gate_calls += 1
            for n in ast.walk(node):
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                        and n.func.id == "mut":
                    badmut.append(node.args[0].value if node.args else "?")
    for node in ast.walk(scan_tree):
        if isinstance(node, ast.FunctionDef) and node.name in (
                "reconstruct_verdict_from_receipt", "derive_head", "build_segments"):
            for n in ast.walk(node):
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                        and n.func.id == "mut":
                    badmut.append(node.name)
    LD.gate("G-NO-MUTANT-IDENTITY-IN-GATES",
            "no gate predicate and no verdict-deriving or comparing function "
            "references mutant identity: an AST scan of every gate call site "
            "and of the three verdict functions (#208)",
            not badmut and gate_calls >= len(GATE_REGISTRY),
            "gate call sites scanned=%d offenders: %s"
            % (gate_calls, badmut or "none"))

    float_probe = dict(Rjson)
    if mut("MUT-FLOAT-RECEIPT"):
        float_probe["_float_probe"] = 10 ** -1
    LD.gate("G-NO-FLOAT-RECEIPT",
            "the emitted receipt object contains no float at any depth",
            not has_float(float_probe),
            "recursive scan of the serialized receipt")

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


def main():
    global MUT
    args = sys.argv[1:]
    write = True
    break_anchor = None
    verify_paper = None
    if "--no-write" in args:
        write = False
    if "--mutant" in args:
        MUT = args[args.index("--mutant") + 1]
        write = False
    if "--break-anchor" in args:
        break_anchor = args[args.index("--break-anchor") + 1]
        write = False
    if "--verify-paper" in args:
        verify_paper = args[args.index("--verify-paper") + 1]
        write = False

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
    R["compliance"] = compliance_sweep(S, LD, report)
    R["paper_claims"] = {"paper": "v14/paper-10-defect-on-the-stage.md",
                         "rendered": paper_claims(R)}
    R["not_executed"] = [
        "the 9-point Moore stencil is not swept; only the 3-term axis stencil "
        "(exhaustive over the declared alphabet at every swept order) and the "
        "5-point stencil (at one lattice size above the collapse threshold)",
        "coefficients outside the declared 25-element alphabet are not swept; "
        "the order-5-and-above collapse is proved in the paper and is "
        "alphabet-independent, but the order-3 emptiness is alphabet-relative",
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
        with open(verify_paper, "r", encoding="utf-8") as f:
            txt = f.read()
        missing = [k for k, v in R["paper_claims"]["rendered"].items() if v not in txt]
        print("PAPER CLAIM VERIFICATION: %d claims, %d missing %s"
              % (len(R["paper_claims"]["rendered"]), len(missing), missing))
        sys.exit(1 if missing else 0)

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
    say("THE STAGE: locality by the ported criterion (Moore connective, d=2)")
    for row in R["locality_sweep"]:
        if row["d"] == 2 and row["connective"] == CONNECTIVES[0]:
            say("  L=%d offsets=%2d neighbours=%2d complete=%-5s locality=%s"
                % (row["L"], row["offsets"], row["neighbours"],
                   row["complete"], row["locality"]))
    say("  parity witness: %s" % R["parity_witness"])
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
    say("REALIZATION CENSUS (the mandatory gate)")
    for lv in LEVELS:
        say("  %-9s %d generators" % (lv, R["realization_census"]["levels"][lv]))
    say("  maximal declared transport: %s" % R["realization_census"]["maximal"])
    say("  defects entering the verdict: only at %s" % R["realization_census"]["maximal"])
    say("")
    say("STATE MOTION")
    say("  %s" % R["state_motion"])
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
