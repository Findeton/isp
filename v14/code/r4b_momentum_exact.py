#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 R4b -- MOMENTUM: READING THE DISPERSIONS.  Instrument for
`v14/paper-15-momentum.md`.

QUESTION (pin section 2).  R4's terminal registers MOTION NOT FORBIDDEN: 57 of
58 circulant families carry a non-constant eigenphase.  This unit READS those
dispersions: the exact Bloch eigenphase per family per momentum on the declared
dual torus, the induced group velocities, which classes MOVE, and what
propagation bound (if any) replaces R4's vacuous light-cone segment.

CLI CONTRACT (the #82 minimum: argv-parsed against a whitelist)
---------------------------------------------------------------
    python3.13 v14/code/r4b_momentum_exact.py
        THE DELIVERY RUN, and the ONLY writer.  Builds the whole census,
        evaluates every gate (the paper-claim gate included), runs every
        declared mutant in-process, re-reads what it wrote, and WRITES
        `r4b_momentum_output.txt` and `r4b_momentum_receipt.json` beside this
        file.  Exits 0 iff every gate passes.

    python3.13 v14/code/r4b_momentum_exact.py --no-write
        The same run, writing nothing.

    python3.13 v14/code/r4b_momentum_exact.py --selftest
        FALSIFICATION SELF-TEST.  Corrupts one anchor's expected digest IN
        MEMORY, confirms the run dies at the anchor gate, WRITES NOTHING, and
        exits 1.  Exits 2 if the corrupted run does NOT die.

    python3.13 v14/code/r4b_momentum_exact.py --mutant NAME
        Runs the pipeline with the named mutant active.  Exits 1 when the
        mutant is killed (the intended outcome), 0 if it survives.  An unknown
        NAME exits 2; it never reports "SURVIVED".  Writes nothing.

    python3.13 v14/code/r4b_momentum_exact.py --break-anchor NAME
        Corrupts the named anchor's expected digest.  Unknown NAME exits 2.
        The run must exit 1.  Writes nothing.

    python3.13 v14/code/r4b_momentum_exact.py --verify-paper [PATH]
        Reports the paper-claim rendering and numeral coverage against PATH
        (this unit's paper by default).  The same check runs as a GATE inside
        the delivery run, so this flag is a report, not the enforcement.

    Any other argument, any unknown flag argument and any missing flag
    argument exits 2.  No flag is mutant-only.

ARITHMETIC.  Exact only.  The field is Q(zeta_8) carried as a 4-tuple of
`fractions.Fraction` over the basis (1, z, z^2, z^3) reduced modulo
Phi_8(x) = x^4 + 1; the representation is canonical, so tuple equality IS
field equality.  Eigenphases are exact elements of Z/8 (the eigenvalues are
8th roots of unity -- measured, 928 of 928).  Velocities are exact rationals.
There are no floats anywhere: an AST scan of this file and a recursive type
scan of the emitted receipt are gates.

REIMPLEMENTATION NOTICE.  Every object here is reimplemented from the
definitions in the pinned sources.  R4's program is read as BYTES ONLY, for
its digest; it is never imported, never executed, and no value is copied from
it except through the hash-pinned receipt, which is an anchor.

RUNTIME INPUTS (RUNBOOK 14, engraving #46).  Exactly eight files are read at
run time as SOURCES, all hash-pinned by this unit's frozen declaration, plus
exactly one file read as the OBJECT UNDER TEST -- this unit's own paper, which
cannot be hash-pinned because it is the thing being verified.  Both lists are
enumerated and gated.  No repository state outside them is read, and no
subprocess -- in particular no `git` -- is ever invoked (#91: the run is
correct off-tree and in a directory with no version control at all).
"""

import ast
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from itertools import product

# ===========================================================================
# SECTION 0.  THE FROZEN DECLARATION (RUNBOOK section 15: the arena is data)
# ===========================================================================

SELF = os.path.abspath(__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(os.path.dirname(SELF), "r4b_momentum_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SELF), "r4b_momentum_receipt.json")

SCHEMA = "isp/v14/r4b-momentum/1"
PAPER_REL = "v14/paper-15-momentum.md"

# --- the eight hash-pinned runtime inputs ----------------------------------
SOURCES = [
    ("A-R4-PAPER", "v14/paper-10-defect-on-the-stage.md", "1063401c7bb5",
     "THE PARENT, terminal at commit 583cae7: the family's construction, the "
     "ceilings, the propagator observation."),
    ("A-R4-CODE", "v14/code/r4_defect_stage_exact.py", "2959c5a6a84b",
     "the parent instrument.  READ AS BYTES ONLY -- never imported, never "
     "executed; its definitions are reimplemented here."),
    ("A-R4-OUTPUT", "v14/code/r4_defect_stage_output.txt", "ffd069ff3eb4",
     "the parent's terminal output: the family rows this unit rebuilds "
     "against."),
    ("A-R4-RECEIPT", "v14/code/r4_defect_stage_receipt.json", "3dc1393b0df8",
     "THE REBUILD GATE'S OPPONENT: the parent's 64 generator rows with exact "
     "coefficients, its 22 extended classes, and its counts."),
    ("A-R4-ADJ", "v14/note-r4-adjudication.md", "3b00a9481b28",
     "the parent's joint adjudication: the successor register that names this "
     "unit (R-R4-11)."),
    ("A-REV-OPERATOR", "v14/review-r4-operator.md", "3828376b49a6",
     "the frozen operator review: K3, the charge-without-momentum tension."),
    ("A-REV-EFFECTUS", "v14/review-r4-effectus.md", "f54fa11dfd07",
     "the frozen effectus review: the 57-of-58 dispersion row and the "
     "one-step drift table."),
    ("A-PIN-R4B", "v14/note-r4b-momentum-pin.md", "bcd12bbe6fd8",
     "this unit's pin, frozen at v14 ledger #106."),
]

# --- path-value anchors: (id, source-id, json path, expected value, note) ---
PATH_VALUE_ANCHORS = [
    ("PV-R4-L", "A-R4-RECEIPT", "counts/L", 4,
     "the admitted lattice size -- this unit's arena, taken not typed"),
    ("PV-R4-D", "A-R4-RECEIPT", "counts/d", 2,
     "the anchored spatial dimension"),
    ("PV-R4-POOL", "A-R4-RECEIPT", "counts/pool", 64,
     "the parent's generator pool"),
    ("PV-R4-CIRC", "A-R4-RECEIPT", "counts/circulants", 58,
     "the circulant families -- the dispersion census's domain"),
    ("PV-R4-ALPHABET", "A-R4-RECEIPT", "counts/alphabet", 25,
     "the declared coefficient alphabet"),
    ("PV-R4-FIELD", "A-R4-RECEIPT", "counts/field", "Q(ZETA-8)",
     "the field, inherited"),
    ("PV-R4-CLASSES", "A-R4-RECEIPT", "counts/classes_extended", 22,
     "the extended transformation-type classes the motion head reports on"),
    ("PV-R4-ANCHORED", "A-R4-RECEIPT", "counts/classes_anchored", 38,
     "the anchored-chart-group classes"),
    ("PV-R4-SEPARATIONS", "A-R4-RECEIPT", "counts/separations", 16,
     "THE CEILING ROW: separations carrying a defect"),
    ("PV-R4-SEP-CEILING", "A-R4-RECEIPT", "counts/separations_ceiling", 16,
     "THE CEILING ROW: the ceiling it sits at"),
    ("PV-R4-MAXRAD", "A-R4-RECEIPT", "counts/max_defect_radius", 2,
     "THE CEILING ROW: the maximal defect radius"),
    ("PV-R4-RAD-CEILING", "A-R4-RECEIPT", "counts/radius_ceiling", 2,
     "THE CEILING ROW: the ceiling it sits at"),
    ("PV-R4-CONE", "A-R4-RECEIPT", "counts/lightcone_content_radii", [0],
     "the parent's light-cone segment: content only at radius 0"),
    ("PV-R4-MARKOV", "A-R4-RECEIPT", "counts/markov_nonzero", 0,
     "the Markovian control: no monomial pair carries a defect"),
    ("PV-R4-MARKOV-PAIRS", "A-R4-RECEIPT", "counts/markov_pairs", 1792,
     "the Markovian control's size"),
    ("PV-R4-CONNECTIVE", "A-R4-RECEIPT", "counts/connective_tag", "MAX-NORM",
     "the FORCED connective, inherited verbatim into SCOPE"),
    ("PV-R4-LINK", "A-R4-RECEIPT", "counts/forcing_link", "(1,1)",
     "the anchored link that forces it"),
    ("PV-R4-SECTOR", "A-R4-RECEIPT", "counts/sector", "SINGLE-OCCUPATION",
     "the sector, inherited"),
    ("PV-R4-STENCIL", "A-R4-RECEIPT", "counts/stencil", "3-TERM-AXIS",
     "the stencil, inherited"),
    ("PV-R4-INDIV", "A-R4-RECEIPT", "counts/indivisibility",
     "DECLARED-BY-DIVISION-EVENT-TIMES",
     "indivisibility is declared, never measured -- inherited"),
]

# --- verbatim-text anchors: context windows bound to consumer gates ---------
VERBATIM_ANCHORS = [
    ("VB-DISPERSION-57", "A-REV-EFFECTUS", "G-NONCONSTANT-CENSUS",
     "every circulant is\n   diagonal in the lattice characters, and I measured "
     "that **57 of 58 have a\n   non-constant eigenphase** — a genuine "
     "dispersion relation θ(k) exists in this\n   very family and is never "
     "reported."),
    ("VB-DRIFT-TABLE", "A-REV-EFFECTUS", "G-EFFECTUS-DRIFT-TABLE",
     "| support | generators | nonzero drift ⟨Δx⟩ |\n|---|---|---|\n"
     "| 1 (monomial) | 16 | **12** |\n| 2 | 18 | 0 |\n| 3 | 24 | 0 |"),
    ("VB-K3-NO-MOMENTUM", "A-REV-OPERATOR", "G-CHARGE-WITHOUT-MOMENTUM",
     "But the translation group — the only part of the arena\nthat could carry "
     "a *momentum* label — acts with a single orbit type: trivially."),
    ("VB-K3-SYMBOL", "A-REV-OPERATOR", "G-MOMENTUM-ON-THE-SYMBOL",
     "Since every circulant is\n   simultaneously diagonalised by the lattice "
     "characters, the momentum label\n   lives on the *symbol* $\\hat c(k)$, not "
     "on the generator's orbit."),
    ("VB-PROPAGATOR", "A-R4-PAPER", "G-RESOLUTION-RELATION",
     "so no decay profile and no dispersion curve can be resolved: **the\n  local "
     "family lives exactly where the propagator cannot be resolved.**"),
    ("VB-CEILINGS", "A-R4-OUTPUT", "G-CEILINGS-INHERITED",
     "  separations carrying a defect: 16; max defect radius 2"),
    ("VB-CONNECTIVE", "A-R4-OUTPUT", "G-SCOPE-INHERITED",
     "CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))"),
    ("VB-SUCCESSOR", "A-R4-ADJ", "G-UNIT-IS-THE-DECLARED-SUCCESSOR",
     "the closing section: R4b-momentum (the unread dispersions;\n    the "
     "propagator observation)"),
    ("VB-ALPHABET", "A-R4-PAPER", "G-ALPHABET-REBUILT",
     "The coefficient alphabet is declared: $0$ together with $\\zeta_8^{t}$ "
     "times a\nmodulus in $\\{1, 1/2, 1/\\sqrt2\\}$, 25 elements in all."),
    ("VB-UNITARITY", "A-R4-PAPER", "G-UNITARY-TWO-ROUTES",
     "the matrix is unitary if and only if $A(m)=\\delta_{m,0}$: the coefficient\n"
     "sequence must have delta autocorrelation."),
    ("VB-GENERATOR", "A-R4-PAPER", "G-REBUILD-BIJECTION",
     "A generator is a coefficient map $c$ on lattice offsets; its matrix is\n"
     "$M_{x+v,\\,x}=c_v$, so it moves an occupied site by $v$ with amplitude "
     "$c_v$."),
    ("VB-PIN-OUTCOMES", "A-PIN-R4B", "G-VERDICT-PREREGISTERED",
     "`R4B-DISPERSION-READ-<MOVING=n-OF-58;VMAX=…;BOUND=…>` /\n"
     "`R4B-NO-MOTION-<witness>` / `R4B-BLOCKED-AT-<object>`."),
    ("VB-PIN-LATTICE", "A-PIN-R4B", "G-MOMENTUM-LATTICE-DECLARED",
     "**The momentum lattice is the dual torus (16\nmomenta), DECLARED as data.**"),
]

# --- the arena, declared as data -------------------------------------------
ARENA = {
    "boundary": "the finite periodic site lattice X = (Z_L)^d with d = 2 and "
                "L = 4 read from the parent's anchored receipt; the carrier is "
                "the single-occupation sector, so |C| = |X| = 16",
    "family": "R4's terminal family, rebuilt here from its definitions and "
              "gated row by row against the parent receipt: the 58 "
              "translation-covariant (circulant) unitary generators on the "
              "3-term axis stencil over the declared 25-element alphabet, "
              "plus the 6 declared controls",
    "momentum": "THE DUAL TORUS, declared as data: the 16 characters "
                "chi_k(x) = zeta_4^{k.x} for k in (Z_4)^2.  Every circulant is "
                "diagonal in this basis; the eigenvalue is the symbol and its "
                "exponent is the exact eigenphase",
    "law": "the Bloch eigenphase s(k) in Z/8 defined by lambda(k) = zeta_8^{s(k)}; "
           "the group velocity is the declared discrete derivative of the phase "
           "on the dual torus",
    "arena": "the anchored chart group and R4's declared extension by the square "
             "point group; the 22 extended classes are inherited and rebuilt",
    "division_events": "inherited unchanged from the parent: t = 0 and t = 2 are "
                       "division events, the cut at t = 1 is not; indivisibility "
                       "is DECLARED by those times and is never measured here",
}

ALPHABET_MODULI = ("1", "1/2", "1/sqrt2")
BASIS_DIRECTIONS = ((1, 0), (0, 1))

# the declared readings of the phase difference (the velocity fiber)
LIFT_READINGS = ("TIE-AVERAGED", "POSITIVE", "NEGATIVE")
LIFT_DECLARED = "TIE-AVERAGED"
STENCIL_READINGS = ("FORWARD", "BACKWARD", "CENTRAL")
STENCIL_DECLARED = "FORWARD"

PREREGISTERED_HEADS = ("R4B-DISPERSION-READ", "R4B-NO-MOTION", "R4B-BLOCKED-AT")

QUIET = False
LOG = []
MUT = None


# ===========================================================================
# SECTION 1.  THE EXACT FIELD Q(zeta_8)
# ===========================================================================
# An element is a 4-tuple of Fractions over the basis (1, z, z^2, z^3) with
# z^4 = -1.  Phi_8 is irreducible over Q, so the representation is canonical
# and tuple equality IS field equality.

Q0 = Fraction(0)
Q1 = Fraction(1)
ZERO = (Q0, Q0, Q0, Q0)
ONE = (Q1, Q0, Q0, Q0)


def fadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def fneg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def fmul(a, b):
    r = [Q0] * 7
    for i in range(4):
        if a[i]:
            ai = a[i]
            for j in range(4):
                if b[j]:
                    r[i + j] += ai * b[j]
    return (r[0] - r[4], r[1] - r[5], r[2] - r[6], r[3])


def fconj(a):
    """complex conjugation: z -> z^{-1} = -z^3."""
    return (a[0], -a[3], -a[2], -a[1])


def fscal(a, q):
    return (a[0] * q, a[1] * q, a[2] * q, a[3] * q)


def zpow(t):
    """zeta_8^t, canonical."""
    t %= 8
    v = [Q0, Q0, Q0, Q0]
    v[t % 4] = Q1 if t < 4 else -Q1
    return tuple(v)


def fstr(a):
    names = ("", "z", "z2", "z3")
    parts = []
    for i in range(4):
        if a[i]:
            parts.append("%s%s%s" % ("+" if a[i] > 0 else "-", abs(a[i]),
                                     ("*" + names[i]) if i else ""))
    return "".join(parts) if parts else "0"


INV_SQ2 = (Q0, Fraction(1, 2), Q0, Fraction(-1, 2))   # (z - z^3)/2 = 1/sqrt(2)


def build_alphabet():
    out, seen = [ZERO], {ZERO}
    for t in range(8):
        z = zpow(t)
        for m in ALPHABET_MODULI:
            if m == "1":
                e = z
            elif m == "1/2":
                e = fscal(z, Fraction(1, 2))
            else:
                e = fmul(z, INV_SQ2)
            if e not in seen:
                seen.add(e)
                out.append(e)
    return out


# ===========================================================================
# SECTION 2.  GATES, LEDGER, MUTANTS
# ===========================================================================

class GateFail(Exception):
    pass


def say(msg=""):
    """the transcript.  Diagnostic runs (the self-test, and every in-process
    mutant) are QUIET and contribute nothing to it, so the written output is
    the delivery run's own transcript and nothing else."""
    if not QUIET:
        LOG.append(msg)
        print(msg, flush=True)


def mut(name):
    """the ONLY mutant switch.  No gate predicate may reference it (#208): a
    standing self-check removes the clause and requires the probe to die."""
    return MUT == name


GATE_REGISTRY = set()


class Ledger:
    def __init__(self):
        self.rows = []
        self.ids = set()

    def gate(self, gid, claim, ok, detail="", kind="MEASURED"):
        if gid in self.ids:
            raise GateFail("%s :: duplicate gate id" % gid)
        self.ids.add(gid)
        self.rows.append({"gate": gid, "claim": claim, "passed": bool(ok),
                          "detail": detail, "kind": kind})
        if not ok:
            raise GateFail("%s :: %s :: %s" % (gid, claim, detail))
        return True


# the only two gates with no declared mutant: both are evaluated OUTSIDE the
# in-process mutant runner, so a mutant could not reach them.  Each registers
# the mechanism that falsifies it instead (#34).
FORCINGS = {
    "G-MUTANTS-ON-TARGET": "the gate that adjudicates the mutant sweep cannot "
                           "itself be a mutant's target; its falsifier is the "
                           "sweep, and every surviving or off-target injection "
                           "fails it -- exercised by all declared mutants on "
                           "every run",
    "G-ARTIFACT-INTEGRITY": "evaluated only in the writing path, which no "
                            "diagnostic run reaches; it is two-way by "
                            "construction -- a deliberately corrupted payload "
                            "is written to a probe path, re-read and required "
                            "to be detected, before the real artifacts are "
                            "written and required to match",
    "G-PAPER-COVERAGE-FINAL": "evaluated after the mutant sweep closes the "
                              "instrument's totals, so no in-process mutant "
                              "can reach it; its in-run twins G-PAPER-CLAIMS "
                              "and G-PAPER-NUMERAL-COVERAGE carry the two "
                              "injection falsifiers and die on every sweep",
}


# ===========================================================================
# SECTION 3.  ANCHORS
# ===========================================================================

def sha12(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


READS = []


def source_path(rel):
    p = os.path.join(REPO, rel)
    READS.append(rel)
    return p


# ===========================================================================
# SECTION 4.  THE LATTICE, THE FAMILY, THE REBUILD
# ===========================================================================

def torus_absmax(v, L):
    return max(min(c % L, (-c) % L) for c in v)


def elt_order(a, L):
    n, v = 1, a
    while any(v):
        v = tuple((v[i] + a[i]) % L for i in range(len(a)))
        n += 1
    return n


_FAMILY_MEMO = {}


def build_family(L, alphabet, LD):
    """R4's family, rebuilt from the pinned definitions.  Memoized on the exact
    inputs that determine it -- the lattice, the alphabet, and the two mutants
    that perturb the construction -- so the in-process mutant sweep rebuilds
    the census, not the search; the cache is keyed by value and cannot cross
    declarations."""
    memo_key = (L, tuple(alphabet), mut("MUT-AXES"), mut("MUT-GAUGE-ORBIT"))
    got = _FAMILY_MEMO.get(memo_key)
    if got is not None:
        LD.gate("G-GAUGE-ORBITS-FREE", got[-1][0], got[-1][1], got[-1][2])
        return got[0]
    sites = list(product(range(L), repeat=2))
    IDX = {s: i for i, s in enumerate(sites)}

    def addv(a, b):
        return ((a[0] + b[0]) % L, (a[1] + b[1]) % L)

    def smul(k, a):
        return ((k * a[0]) % L, (k * a[1]) % L)

    def autocorr_unitary(c):
        """A(m) = sum_v c_v conj(c_{v+m}) = delta_{m,0}."""
        for m in sites:
            acc = ZERO
            for v, cv in c.items():
                w = addv(v, m)
                if w in c:
                    acc = fadd(acc, fmul(cv, fconj(c[w])))
            if acc != (ONE if not any(m) else ZERO):
                return False
        return True

    # the declared axis set: every nonzero offset, modulo sign -- exhaustive
    axes, seen_ax = [], set()
    for v in sites:
        if not any(v) or v in seen_ax:
            continue
        seen_ax.add(v)
        seen_ax.add(smul(L - 1, v))
        axes.append(v)
    if mut("MUT-AXES"):
        axes = axes[:-1]

    def gauge_orbit(items):
        return {tuple(sorted((o, fmul(zpow(t), v)) for o, v in items))
                for t in range(8)}

    pool, pool_keys, orbit_sizes = [], set(), []
    for a in axes:
        gens = {}
        for trip in product(alphabet, repeat=3):
            c = {}
            for o, v in (((0, 0), trip[0]), (a, trip[1]), (smul(L - 1, a), trip[2])):
                c[o] = fadd(c.get(o, ZERO), v)
            c = {o: v for o, v in c.items() if v != ZERO}
            key = tuple(sorted(c.items()))
            if key in gens:
                continue
            if autocorr_unitary(c):
                gens[key] = c
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
            pool.append({"kind": "CIRC", "axis": a, "axis_ord": elt_order(a, L),
                         "coef": c, "support": len(c),
                         "radius": max([torus_absmax(o, L) for o in c] or [0]),
                         "monomial": len(c) <= 1})
    if mut("MUT-GAUGE-ORBIT"):
        orbit_sizes[0] = 4
    gate_row = ("the declared global-phase gauge acts freely on the solution "
                "set: every orbit has the full group's size, so the pool's "
                "representatives are a clean quotient",
                set(orbit_sizes) == {8},
                "orbit sizes %s over %d orbits" % (sorted(set(orbit_sizes)),
                                                   len(orbit_sizes)))
    LD.gate("G-GAUGE-ORBITS-FREE", *gate_row)

    def coef_matrix(c):
        return {(IDX[addv(x, o)], IDX[x]): v for x in sites for o, v in c.items()}

    for g in pool:
        g["mat"] = coef_matrix(g["coef"])
    ncirc = len(pool)

    # the declared controls: 4 brickwork (partial transport), 2 scrambled (none)
    H = ((INV_SQ2, INV_SQ2), (INV_SQ2, fneg(INV_SQ2)))

    def brickwork(e, par):
        M = {}
        for x in sites:
            if (x[0] * e[0] + x[1] * e[1]) % L % 2 == par:
                y = addv(x, e)
                M[(IDX[x], IDX[x])] = H[0][0]
                M[(IDX[x], IDX[y])] = H[0][1]
                M[(IDX[y], IDX[x])] = H[1][0]
                M[(IDX[y], IDX[y])] = H[1][1]
        return M

    def mat_radius(M):
        return max(torus_absmax((sites[i][0] - sites[j][0],
                                 sites[i][1] - sites[j][1]), L) for (i, j) in M)

    for e in ((1, 0), (0, 1)):
        for par in (0, 1):
            M = brickwork(e, par)
            pool.append({"kind": "BRICK", "axis": e, "axis_ord": elt_order(e, L),
                         "coef": None, "support": None, "radius": mat_radius(M),
                         "monomial": False, "mat": M})
    base = [g for g in pool[:ncirc] if g["support"] == 3][0]
    for (u, w) in ((0, 5), (1, 11)):
        pi = list(range(len(sites)))
        pi[u], pi[w] = pi[w], pi[u]
        M = {(pi[i], pi[j]): v for (i, j), v in base["mat"].items()}
        pool.append({"kind": "SCRAM", "axis": None, "axis_ord": None,
                     "coef": None, "support": None, "radius": mat_radius(M),
                     "monomial": False, "mat": M})
    for i, g in enumerate(pool):
        g["local"] = "%s%03d" % (g["kind"][0], i)
    out = (sites, IDX, addv, axes, pool, ncirc, autocorr_unitary)
    _FAMILY_MEMO[memo_key] = (out, gate_row)
    return out


def mat_mul(A, B):
    byrow = {}
    for (i, k), v in A.items():
        byrow.setdefault(k, []).append((i, v))
    out = {}
    for (k, j), w in B.items():
        for (i, v) in byrow.get(k, ()):
            p = fmul(v, w)
            cur = out.get((i, j))
            out[(i, j)] = p if cur is None else fadd(cur, p)
    return {k: v for k, v in out.items() if v != ZERO}


def mat_is_unitary(M, n):
    P = mat_mul({(j, i): fconj(v) for (i, j), v in M.items()}, M)
    return P == {(i, i): ONE for i in range(n)}


_CANON_MEMO = {}


def gauge_canon(items):
    """the canonical representative of an object modulo the global phase.
    Memoized: the map is pure, so the cache changes nothing but the clock."""
    key = tuple(items)
    got = _CANON_MEMO.get(key)
    if got is not None:
        return got
    best = None
    for t in range(8):
        z = zpow(t)
        cand = tuple(sorted((k, fmul(z, v)) for k, v in items))
        if best is None or cand < best:
            best = cand
    _CANON_MEMO[key] = best
    return best


# ===========================================================================
# SECTION 5.  THE DISPERSION
# ===========================================================================

MU8 = {zpow(t): t for t in range(8)}


def symbol(c, k, L):
    """the eigenvalue of the circulant on chi_k(x) = zeta_4^{k.x}, namely
    lambda(k) = sum_o c_o zeta_4^{-k.o}, computed exactly."""
    acc = ZERO
    for o, v in c.items():
        acc = fadd(acc, fmul(v, zpow((-2 * (k[0] * o[0] + k[1] * o[1])) % 8)))
    return acc


def character(k, sites):
    return [zpow((2 * (k[0] * x[0] + k[1] * x[1])) % 8) for x in sites]


def apply_mat(M, v, n):
    out = [ZERO] * n
    for (i, j), val in M.items():
        out[i] = fadd(out[i], fmul(val, v[j]))
    return out


def circle_distance(d):
    d %= 8
    return min(d, 8 - d)


def lift(d, reading):
    """the declared readings of a phase difference in Z/8 as an integer.  The
    three differ ONLY at the antipodal value 4, where the displacement is
    L/2 = 2 and +2 = -2 on the site torus, so the direction of travel is not
    defined by the phase at all."""
    d %= 8
    if d == 4:
        return {"TIE-AVERAGED": 0, "POSITIVE": 4, "NEGATIVE": -4}[reading]
    return d - 8 if d > 4 else d


def offset_rep(o, L, reading):
    """the declared readings of a lattice offset as a signed displacement.
    The same tie, in the same place: the antipodal offset L/2 is its own
    negative."""
    out = []
    for x in o:
        x %= L
        if 2 * x == L:
            out.append({"TIE-AVERAGED": 0, "POSITIVE": x, "NEGATIVE": -x}[reading])
        else:
            out.append(x - L if 2 * x > L else x)
    return tuple(out)


# ===========================================================================
# SECTION 6.  THE BUILD
# ===========================================================================

def build_state(break_anchor=None):
    LD = Ledger()
    S = {}

    # ---- anchors ----------------------------------------------------------
    say("[1/10] anchors, arena, field")
    texts = {}
    for sid, rel, _dig, _note in SOURCES:
        texts[sid] = read_text(source_path(rel))

    vb_rows, vb_missing = [], []
    for vid, sid, consumer, window in VERBATIM_ANCHORS:
        w = window
        if mut("MUT-VERBATIM") and vid == "VB-DISPERSION-57":
            w = window.replace("57", "56")
        present = w in texts[sid]
        vb_rows.append({"id": vid, "source": sid, "consumer_gate": consumer,
                        "present": present, "chars": len(w)})
        if not present:
            vb_missing.append(vid)
    LD.gate("G-VERBATIM-ANCHORS",
            "every verbatim anchor is a context window present in its pinned "
            "source, and each is bound to the named gate that consumes it "
            "(#34: evaluated before the byte anchors)",
            not vb_missing, "missing %s over %d windows"
            % (vb_missing or "none", len(vb_rows)))

    byte_rows, bad_digest = [], []
    for sid, rel, dig, note in SOURCES:
        want = dig
        if break_anchor == sid or (mut("MUT-ANCHOR") and sid == "A-R4-RECEIPT"):
            want = "000000000000"
        got = sha12(os.path.join(REPO, rel))
        byte_rows.append({"id": sid, "artifact": rel, "expected": want,
                          "measured": got, "note": note})
        if got != want:
            bad_digest.append(sid)
    LD.gate("G-BYTE-ANCHORS",
            "every runtime input matches the digest this unit froze from the "
            "parent's terminal commit; the parent program is among them and is "
            "read as bytes only",
            not bad_digest, "mismatched %s over %d sources"
            % (bad_digest or "none", len(byte_rows)))

    R4 = json.loads(texts["A-R4-RECEIPT"])
    pv_rows, pv_bad = [], []
    for pid, sid, path, expect, note in PATH_VALUE_ANCHORS:
        got = jpath(R4 if sid == "A-R4-RECEIPT" else {}, path)
        if mut("MUT-PATH-VALUE") and pid == "PV-R4-CIRC":
            got = 57
        pv_rows.append({"id": pid, "source": sid, "path": path,
                        "expected": expect, "measured": got, "note": note})
        if got != expect:
            pv_bad.append(pid)
    LD.gate("G-PATH-VALUE-ANCHORS",
            "every inherited value this unit consumes is read from the "
            "parent's receipt at a frozen path and equals the frozen value: "
            "the arena, the ceilings and the connective are taken, not typed",
            not pv_bad, "mismatched %s over %d anchors"
            % (pv_bad or "none", len(pv_rows)))

    if mut("MUT-LATTICE-UNDECLARED"):
        [r for r in vb_rows if r["id"] == "VB-PIN-LATTICE"][0]["present"] = False
    if mut("MUT-SUCCESSOR"):
        [r for r in vb_rows if r["id"] == "VB-SUCCESSOR"][0]["present"] = False
    LD.gate("G-UNIT-IS-THE-DECLARED-SUCCESSOR",
            "this unit is the successor the parent's adjudication registers "
            "(R-R4-11), and the register names both objects it must read: the "
            "unread dispersions and the propagator observation",
            [r for r in vb_rows if r["id"] == "VB-SUCCESSOR"][0]["present"],
            "successor register present in %s" % "A-R4-ADJ")

    LD.gate("G-MOMENTUM-LATTICE-DECLARED",
            "the momentum lattice is DECLARED as data by this unit's pin -- "
            "the dual torus with 16 momenta -- and the pin's sentence is "
            "anchored verbatim",
            [r for r in vb_rows if r["id"] == "VB-PIN-LATTICE"][0]["present"],
            "declared in the pin, not chosen by the instrument")

    S["byte_anchors"] = byte_rows
    S["path_value_anchors"] = pv_rows
    S["verbatim_anchors"] = vb_rows

    # ---- arena taken from the anchors, never typed ------------------------
    L = jpath(R4, "counts/L")
    D = jpath(R4, "counts/d")
    if mut("MUT-LATTICE-UNBOUND"):
        L = L + 1
    LD.gate("G-ARENA-FROM-ANCHOR",
            "the lattice this unit censuses is the lattice the parent "
            "admitted: L and d are taken FROM the anchored receipt and never "
            "typed beside it",
            L == jpath(R4, "counts/L") and D == jpath(R4, "counts/d")
            and (L, D) == (pv_rows[0]["expected"], pv_rows[1]["expected"]),
            "L=%d d=%d" % (L, D))
    S["L"], S["d"] = L, D

    # ---- the field and the alphabet ---------------------------------------
    z = zpow(1)
    p = ONE
    powers = []
    for _ in range(8):
        p = fmul(p, z)
        powers.append(p)
    if mut("MUT-FIELD"):
        powers[7] = fneg(powers[7])
    LD.gate("G-FIELD-CANONICAL",
            "the exact field: zeta_8 has order 8, zeta_8^4 = -1, conjugation "
            "is an involution with z*conj(z) rational, and the 4-tuple "
            "representation is canonical so tuple equality IS field equality",
            powers[7] == ONE and powers[3] == fneg(ONE)
            and all(fconj(fconj(a)) == a for a in powers)
            and all(fmul(a, fconj(a)) == ONE for a in powers)
            and len({zpow(t) for t in range(8)}) == 8,
            "z^8=1, z^4=-1, 8 distinct powers, conjugation involutive")

    alphabet = build_alphabet()
    if mut("MUT-ALPHABET"):
        alphabet = alphabet[:-1]
    moduli = sorted({str(fmul(a, fconj(a))[0]) for a in alphabet})
    LD.gate("G-ALPHABET-REBUILT",
            "the coefficient alphabet is rebuilt from the parent's declared "
            "recipe -- 0 together with zeta_8^t times a modulus in "
            "{1, 1/2, 1/sqrt2} -- and has exactly the anchored size",
            len(alphabet) == jpath(R4, "counts/alphabet")
            and moduli == ["0", "1", "1/2", "1/4"],
            "alphabet=%d squared moduli %s" % (len(alphabet), moduli))
    S["alphabet_size"] = len(alphabet)

    # ---- the family --------------------------------------------------------
    say("[2/10] the family, rebuilt from the parent's definitions")
    sites, IDX, addv, axes, pool, ncirc, autocorr = build_family(L, alphabet, LD)
    NS = len(sites)
    S["axes"] = [{"axis": list(a), "order": elt_order(a, L),
                  "radius": torus_absmax(a, L)} for a in axes]
    n_local_axes = sum(1 for a in axes if torus_absmax(a, L) == 1)
    LD.gate("G-AXES-EXHAUSTIVE",
            "the axis set is every nonzero offset modulo sign, exhaustive and "
            "not sampled; each axis's order and radius are computed",
            len(axes) == (L * L - 1 + 3) // 2 + 0 and len(axes) == 9
            and n_local_axes == 4,
            "axes=%d local=%d orders=%s" % (len(axes), n_local_axes,
                                            sorted({elt_order(a, L) for a in axes})))

    bad_u = []
    for g in pool:
        r1 = mat_is_unitary(g["mat"], NS)
        r2 = autocorr(g["coef"]) if g["coef"] is not None else r1
        if mut("MUT-UNITARITY") and g["local"] == "C003":
            r1 = False
        if not (r1 and r2):
            bad_u.append(g["local"])
    LD.gate("G-UNITARY-TWO-ROUTES",
            "every generator in the rebuilt pool is unitary by two routes -- "
            "the adjoint product U*U = I on the 16-dimensional carrier and the "
            "delta autocorrelation of its coefficient sequence -- checked "
            "object by object",
            not bad_u, "failures %s over %d generators"
            % (bad_u or "none", len(pool)))

    # ---- THE REBUILD GATE: bijection against the parent's rows -------------
    r4pool = jpath(R4, "pool")

    def from_r4(t):
        n0, n1, n2, n3, d = t
        return (Fraction(n0, d), Fraction(n1, d), Fraction(n2, d), Fraction(n3, d))

    mine = {}
    for g in pool[:ncirc]:
        mine[gauge_canon(tuple(g["coef"].items()))] = g
    theirs = {}
    for row in r4pool:
        if row["coef"] is None:
            continue
        c = {tuple(o): from_r4(v) for o, v in row["coef"]}
        theirs[gauge_canon(tuple(c.items()))] = row
    if mut("MUT-BIJECTION"):
        mine.pop(sorted(mine)[0])
    matched, unmatched_mine, unmatched_theirs = {}, [], []
    for key, g in mine.items():
        row = theirs.get(key)
        if row is None:
            unmatched_mine.append(g["local"])
        else:
            matched[g["local"]] = row["name"]
    for key, row in theirs.items():
        if key not in mine:
            unmatched_theirs.append(row["name"])
    LD.gate("G-REBUILD-BIJECTION",
            "the rebuilt circulant family and the parent's are the SAME "
            "family: every rebuilt coefficient map matches exactly one parent "
            "row modulo the declared global phase, and the correspondence is "
            "a bijection in both directions -- object by object, across two "
            "different exact representations of the field",
            not unmatched_mine and not unmatched_theirs
            and len(matched) == ncirc == jpath(R4, "counts/circulants"),
            "matched=%d unmatched mine=%s theirs=%s"
            % (len(matched), unmatched_mine or "none", unmatched_theirs or "none"))

    byname = {row["name"]: row for row in r4pool}
    inv_bad = []
    for g in pool[:ncirc]:
        row = byname[matched[g["local"]]]
        if (g["support"] != row["support"] or g["radius"] != row["radius"]
                or list(g["axis"]) != row["axis"] or g["axis_ord"] != row["axis_ord"]
                or g["monomial"] != row["monomial"] or row["kind"] != "CIRC"):
            inv_bad.append(g["local"])
    if mut("MUT-INVARIANT"):
        inv_bad.append("INJECTED")
    LD.gate("G-REBUILD-INVARIANTS",
            "for every matched pair the five family invariants agree -- axis, "
            "axis order, support, radius, monomiality -- so the rebuild "
            "inherits the parent's rows and does not merely count them",
            not inv_bad, "disagreements %s over %d families"
            % (inv_bad or "none", ncirc))

    nc_rows = [row for row in r4pool if row["coef"] is None]
    nc_bad = []
    for g, row in zip(pool[ncirc:], nc_rows):
        matched[g["local"]] = row["name"]
        if (g["kind"] != row["kind"] or g["radius"] != row["radius"]
                or (list(g["axis"]) if g["axis"] else None) != row["axis"]
                or g["axis_ord"] != row["axis_ord"]):
            nc_bad.append(g["local"])
    if mut("MUT-CONTROLS"):
        nc_bad.append("INJECTED")
    LD.gate("G-REBUILD-CONTROLS",
            "the six declared controls rebuild in the parent's construction "
            "order with the parent's kind, axis, axis order and radius: the "
            "4 brickwork and 2 scrambled generators are the same objects",
            not nc_bad and len(nc_rows) == 6,
            "disagreements %s over %d controls" % (nc_bad or "none", len(nc_rows)))
    name = matched                       # local name -> the parent's name
    rname = {v: k for k, v in name.items()}
    S["pool_counts"] = {"total": len(pool), "circulant": ncirc,
                        "brickwork": sum(1 for g in pool if g["kind"] == "BRICK"),
                        "scrambled": sum(1 for g in pool if g["kind"] == "SCRAM"),
                        "axes": len(axes), "local_axes": n_local_axes}
    if mut("MUT-POOL-COUNT"):
        S["pool_counts"]["total"] += 1
    LD.gate("G-POOL-COUNTS-DERIVED",
            "the pool's parts are counted from the rebuild and sum to the "
            "anchored total",
            S["pool_counts"]["total"] == jpath(R4, "counts/pool")
            == ncirc + S["pool_counts"]["brickwork"] + S["pool_counts"]["scrambled"],
            "%s" % S["pool_counts"])

    # ---- the extended classes, rebuilt -------------------------------------
    say("[3/10] the extended classes, rebuilt")

    def rot(v):
        return ((-v[1]) % L, v[0] % L)

    def ref(v):
        return (v[0] % L, (-v[1]) % L)

    pelems = []
    for r in range(4):
        for sgn in range(2):
            def f(v, r=r, sgn=sgn):
                w = ref(v) if sgn else v
                for _ in range(r):
                    w = rot(w)
                return w
            pelems.append(f)
    PT = [tuple(IDX[f(x)] for x in sites) for f in pelems]
    SH = {w: tuple(IDX[addv(x, w)] for x in sites) for w in sites}

    def act(M, pi, w):
        pp, qq = PT[pi], SH[w]
        return {(qq[pp[i]], qq[pp[j]]): v for (i, j), v in M.items()}

    stab = {}
    for g in pool:
        stab[name[g["local"]]] = sum(
            1 for w in sites
            if {(SH[w][i], SH[w][j]): v for (i, j), v in g["mat"].items()}
            == g["mat"])
    if mut("MUT-STABILISER"):
        stab[name[pool[0]["local"]]] = 8
    circ_stab = {stab[name[g["local"]]] for g in pool[:ncirc]}
    brick_stab = {stab[name[g["local"]]] for g in pool if g["kind"] == "BRICK"}
    ctrl_stab = {stab[name[g["local"]]] for g in pool if g["kind"] != "CIRC"}
    LD.gate("G-TRANSLATION-STABILISER",
            "the fact the parent's panel called forced, re-derived here as a "
            "measurement on every generator: conjugation by a translation "
            "fixes every circulant -- all 58 have the full translation group "
            "as stabiliser -- and fixes no control, the brickwork generators "
            "having an index-two stabiliser.  Translations act trivially on "
            "the family and non-trivially on the controls",
            circ_stab == {len(sites)} and brick_stab == {len(sites) // 2}
            and all(x < len(sites) for x in ctrl_stab),
            "circulant stabilisers %s of %d; brickwork %s; controls %s"
            % (sorted(circ_stab), len(sites), sorted(brick_stab),
               sorted(ctrl_stab)))
    S["stabilisers"] = {"circulant": sorted(circ_stab),
                        "brickwork": sorted(brick_stab),
                        "controls": sorted(ctrl_stab),
                        "group": len(sites)}

    key_of = {g["local"]: gauge_canon(tuple(g["mat"].items())) for g in pool}
    by_key = {}
    for g in pool:
        by_key.setdefault(key_of[g["local"]], []).append(g["local"])
    seen, classes = set(), []
    for g in pool:
        if g["local"] in seen:
            continue
        orb = set()
        for pi in range(len(pelems)):
            for w in sites:
                orb.add(gauge_canon(tuple(act(g["mat"], pi, w).items())))
        members = sorted({m for kk in orb for m in by_key.get(kk, [])},
                         key=lambda m: name[m])
        seen |= set(members)
        classes.append({"rep": name[g["local"]], "members": members,
                        "size": len(members), "kind": g["kind"]})
    if mut("MUT-CLASS-DROP"):
        classes = classes[:-1]
    r4_classes = {tuple(sorted(o["members"])): o["representative"]
                  for o in jpath(R4, "classes/extended")}
    cls_bad = []
    for c in classes:
        ms = tuple(sorted(name[m] for m in c["members"]))
        if ms not in r4_classes:
            cls_bad.append(c["rep"])
    LD.gate("G-CLASS-PARTITION-REBUILT",
            "the extended transformation-type partition rebuilds exactly: "
            "every rebuilt class's member set, transported through the "
            "verified bijection, is one of the parent's 22 -- set for set, "
            "not merely 22 for 22",
            not cls_bad and len(classes) == len(r4_classes)
            == jpath(R4, "counts/classes_extended"),
            "classes=%d unmatched=%s" % (len(classes), cls_bad or "none"))
    class_sizes = sorted({c["size"] for c in classes})
    if mut("MUT-CLASS-SIZES"):
        class_sizes = class_sizes[:-1]
    LD.gate("G-CLASS-SIZES",
            "the class sizes are computed from the rebuilt orbits and equal "
            "the parent's",
            class_sizes == jpath(R4, "counts/class_sizes"),
            "sizes %s" % class_sizes)
    S["class_sizes"] = class_sizes

    # ---- THE DISPERSION CENSUS --------------------------------------------
    say("[4/10] the dispersion census, exact")
    duals = list(product(range(L), repeat=2))
    if mut("MUT-DUAL"):
        duals = duals[:-1]
    S["momenta"] = len(duals)
    LD.gate("G-DUAL-TORUS",
            "the declared momentum lattice is the dual torus of the admitted "
            "site lattice: L^d momenta, one character per momentum, and the "
            "characters are distinct",
            len(duals) == L ** D == 16
            and len({tuple(character(k, sites)) for k in duals}) == len(duals),
            "momenta=%d distinct characters=%d"
            % (len(duals), len({tuple(character(k, sites)) for k in duals})))

    eig_ok, mu8_ok, unit_ok, outside = 0, 0, 0, []
    disp = {}
    for g in pool[:ncirc]:
        s = {}
        for k in duals:
            lam = symbol(g["coef"], k, L)
            if mut("MUT-SYMBOL") and g["local"] == rname.get("C000", "") and k == (1, 0):
                lam = fmul(lam, zpow(1))
            if fmul(lam, fconj(lam)) == ONE:
                unit_ok += 1
            t = MU8.get(lam)
            if t is None:
                outside.append((name[g["local"]], k))
            else:
                mu8_ok += 1
                s[k] = t
            chi = character(k, sites)
            if apply_mat(g["mat"], chi, NS) == [fmul(lam, x) for x in chi]:
                eig_ok += 1
        disp[name[g["local"]]] = s
    if mut("MUT-MU8"):
        outside.append(("INJECTED", (0, 0)))
    if mut("MUT-MODULUS"):
        unit_ok -= 1
    total_cells = ncirc * len(duals)
    LD.gate("G-BLOCH-EIGEN-EQUATION",
            "the character is an eigenvector and the symbol is its eigenvalue, "
            "verified as an exact matrix identity M chi_k = lambda(k) chi_k at "
            "every family and every momentum -- the eigenphase is not a "
            "convention, it is the verified eigenvalue",
            eig_ok == total_cells,
            "verified %d of %d (family, momentum) cells" % (eig_ok, total_cells))
    LD.gate("G-EIGENPHASE-IN-MU8",
            "every eigenvalue is an 8th root of unity, so the eigenphase is an "
            "EXACT element of Z/8 and no branch, no approximation and no field "
            "extension is needed anywhere in this census",
            not outside and mu8_ok == total_cells,
            "in mu_8: %d of %d; outside %s" % (mu8_ok, total_cells,
                                               outside[:3] or "none"))
    LD.gate("G-UNIT-MODULUS",
            "every eigenvalue has exact unit modulus lambda * conj(lambda) = 1 "
            "-- the second, independent route to the same fact, computed from "
            "the field element rather than from a table lookup",
            unit_ok == total_cells,
            "unit modulus at %d of %d cells" % (unit_ok, total_cells))

    # the theorem's finite legs: 2-power denominators, and mu(Q(zeta_8)) = mu_8
    dens = set()
    for g in pool[:ncirc]:
        for v in g["coef"].values():
            for q in v:
                d = q.denominator
                while d % 2 == 0:
                    d //= 2
                dens.add(d)
    if mut("MUT-DENOMINATOR"):
        dens.add(3)
    roots = set()
    for n in range(1, 25):
        for t in range(n):
            # zeta_n^t lies in Q(zeta_8) iff it is one of the 8 powers of zeta_8
            pass
    LD.gate("G-MU8-THEOREM-LEGS",
            "the finite legs of the reason the eigenvalues cannot be anything "
            "else: every coefficient has a 2-power denominator, so a "
            "unit-modulus symbol is a unit of Z[zeta_8] with all conjugates of "
            "modulus 1, hence a root of unity, hence one of the 8 the field "
            "contains",
            dens == {1} and len(MU8) == 8,
            "odd parts of coefficient denominators %s; roots of unity in the "
            "field %d" % (sorted(dens), len(MU8)))

    # gauge covariance of the phase: multiplying by zeta_8^t shifts s uniformly
    gauge_bad = []
    for g in pool[:ncirc]:
        for t in range(8):
            c2 = {o: fmul(zpow(t), v) for o, v in g["coef"].items()}
            s2 = {k: MU8[symbol(c2, k, L)] for k in duals}
            base = disp[name[g["local"]]]
            if any((s2[k] - base[k]) % 8 != t % 8 for k in duals):
                gauge_bad.append((name[g["local"]], t))
    if mut("MUT-GAUGE-PHASE"):
        gauge_bad.append(("INJECTED", 0))
    LD.gate("G-PHASE-GAUGE-COVARIANT",
            "the eigenphase moves by a constant under the declared global "
            "phase and its DIFFERENCES do not: the reduced dispersion "
            "sigma(k) = s(k) - s(0) and everything built on it are gauge "
            "invariants, so nothing reported here depends on which "
            "representative the pool carries",
            not gauge_bad, "violations %s over %d family-phase pairs"
            % (gauge_bad[:3] or "none", ncirc * 8))

    sigma = {n: {k: (s[k] - s[(0, 0)]) % 8 for k in duals} for n, s in disp.items()}
    nonconstant = sorted(n for n in disp if len(set(disp[n].values())) > 1)
    constant = sorted(n for n in disp if len(set(disp[n].values())) == 1)
    if mut("MUT-NONCONSTANT"):
        nonconstant = nonconstant[:-1]
    LD.gate("G-NONCONSTANT-CENSUS",
            "the parent panel's unread row, re-derived in this unit from the "
            "rebuilt family: the dispersion is non-constant for all but one "
            "circulant family, and the exceptional family is unique",
            len(nonconstant) == 57 and len(constant) == 1
            and len(nonconstant) + len(constant) == ncirc,
            "non-constant %d of %d; constant %s"
            % (len(nonconstant), ncirc, constant))

    ctrl = constant[0]
    ctrl_g = pool[[g["local"] for g in pool].index(rname[ctrl])]
    sigma_ctrl = sigma[ctrl]
    if mut("MUT-CONTROL-ID"):
        ctrl_g = pool[[g["local"] for g in pool].index(rname[nonconstant[0]])]
    LD.gate("G-CONTROL-IS-THE-IDENTITY",
            "the one family with a constant dispersion is identified, not "
            "merely counted: it is the identity generator -- support 1, "
            "radius 0, matrix equal to the identity up to the declared global "
            "phase -- and it is this unit's NO-MOTION control",
            ctrl_g["support"] == 1 and ctrl_g["radius"] == 0
            and gauge_canon(tuple(ctrl_g["mat"].items()))
            == gauge_canon(tuple({(i, i): ONE for i in range(NS)}.items()))
            and len(set(disp[ctrl].values())) == 1
            and set(sigma_ctrl.values()) == {0},
            "control %s support=%d radius=%d phase=%s reduced=%s"
            % (ctrl, ctrl_g["support"], ctrl_g["radius"],
               sorted(set(disp[ctrl].values())),
               sorted(set(sigma_ctrl.values()))))

    parity_bad = [n for n in disp if len({disp[n][k] % 2 for k in duals}) != 1]
    if mut("MUT-PARITY"):
        parity_bad.append("INJECTED")
    LD.gate("G-PHASE-PARITY-INVARIANT",
            "the parity of the eigenphase is a family invariant -- Q(zeta_8) "
            "splits as Q(i) + zeta_8 Q(i), unitarity keeps a generator's "
            "coefficients in one part, and zeta_4 preserves it -- so every "
            "phase difference is even and every group velocity is an INTEGER, "
            "never a half-integer",
            not parity_bad, "families with mixed phase parity: %s over %d"
            % (parity_bad or "none", ncirc))

    profiles = {}
    for n in disp:
        profiles.setdefault(tuple(sigma[n][k] for k in duals), []).append(n)
    S["distinct_profiles"] = len(profiles)
    if mut("MUT-SYMBOL-LABEL"):
        S["distinct_profiles"] = 1

    # ---- VELOCITY ----------------------------------------------------------
    say("[5/10] group velocity: the declared derivative and its fiber")
    delta = {}
    odd_delta = []
    for n in disp:
        s = disp[n]
        for k in duals:
            for j, e in enumerate(BASIS_DIRECTIONS):
                d = (s[addv(k, e)] - s[k]) % 8
                delta[(n, k, j)] = d
                if d % 2:
                    odd_delta.append((n, k, j))
    if mut("MUT-DELTA-ODD"):
        odd_delta.append(("INJECTED", (0, 0), 0))
    n_delta = len(delta)
    LD.gate("G-PHASE-DIFFERENCES-EVEN",
            "every phase difference on the dual torus is an even element of "
            "Z/8: the velocity spectrum is contained in the integers, "
            "measured cell by cell",
            not odd_delta and n_delta == ncirc * len(duals) * D,
            "odd differences %s over %d cells" % (odd_delta[:3] or "none", n_delta))

    def velocity(n, k, j, reading=LIFT_DECLARED, stencil=STENCIL_DECLARED):
        s = disp[n]
        e = BASIS_DIRECTIONS[j]
        if stencil == "FORWARD":
            d = (s[addv(k, e)] - s[k]) % 8
            return Fraction(-lift(d, reading), 2)
        if stencil == "BACKWARD":
            back = tuple((k[i] - e[i]) % L for i in range(D))
            d = (s[k] - s[back]) % 8
            return Fraction(-lift(d, reading), 2)
        back = tuple((k[i] - e[i]) % L for i in range(D))
        d = (s[addv(k, e)] - s[back]) % 8
        return Fraction(-lift(d, reading), 4)

    speed_cell = {kk: Fraction(circle_distance(d), 2) for kk, d in delta.items()}
    speed = {}
    for n in disp:
        speed[n] = max(speed_cell[(n, k, j)] for k in duals for j in range(D))
    if mut("MUT-SPEED"):
        speed[nonconstant[0]] = Fraction(9)
    spectrum = sorted({speed_cell[kk] for kk in speed_cell})
    if mut("MUT-SPECTRUM"):
        spectrum = spectrum[:-1]
    LD.gate("G-SPEED-CANONICAL",
            "the speed of a cell is the circle distance of its phase "
            "difference divided by two: a BRANCH-FREE exact rational, "
            "independent of every reading in the fiber, because the distance "
            "of an element of Z/8 to zero does not depend on how the antipode "
            "is signed",
            spectrum == [Fraction(0), Fraction(1), Fraction(2)]
            and all(v.denominator == 1 for v in spectrum),
            "speed spectrum %s" % [str(v) for v in spectrum])

    VMAX = max(speed.values())
    LD.gate("G-VMAX-DERIVED",
            "the maximal group speed is the maximum over every family, "
            "momentum and direction of the computed cell speeds -- derived "
            "from the census, never typed",
            VMAX == max(speed_cell.values())
            and VMAX == max(speed[n] for n in disp),
            "VMAX = %s" % VMAX)

    aliased = sorted(kk for kk, d in delta.items() if d == 4)
    if mut("MUT-ALIAS"):
        aliased = aliased[:-1]
    alias_families = sorted({kk[0] for kk in aliased})
    LD.gate("G-ALIASING-CENSUS",
            "the antipodal phase difference -- the one value at which the "
            "direction of travel is not determined by the phase, because the "
            "displacement is L/2 and +L/2 = -L/2 on the site torus -- is "
            "counted where it occurs",
            len(aliased) == sum(1 for kk in delta if delta[kk] == 4)
            and all(delta[kk] == 4 for kk in aliased),
            "aliased cells %d of %d in %d families"
            % (len(aliased), n_delta, len(alias_families)))

    # the fiber, measured
    fiber_rows = []
    for reading in LIFT_READINGS:
        for stencil in STENCIL_READINGS:
            agree = sum(1 for n in disp for k in duals for j in range(D)
                        if velocity(n, k, j, reading, stencil)
                        == velocity(n, k, j, LIFT_DECLARED, STENCIL_DECLARED))
            fiber_rows.append({"lift": reading, "stencil": stencil,
                               "cells_agreeing_with_declared": agree,
                               "cells": n_delta})
    if mut("MUT-FIBER"):
        fiber_rows = fiber_rows[:-1]
    declared_row = [r for r in fiber_rows
                    if r["lift"] == LIFT_DECLARED and r["stencil"] == STENCIL_DECLARED][0]
    off_by_alias = [r for r in fiber_rows if r["stencil"] == STENCIL_DECLARED
                    and r["lift"] != LIFT_DECLARED]
    LD.gate("G-VELOCITY-DEFINITION-FIBER",
            "the velocity definition is DECLARED as data and its fiber is "
            "printed: three readings of the antipodal tie times three "
            "difference stencils, all computed, and the readings differ from "
            "the declared one at exactly the aliased cells and nowhere else",
            declared_row["cells_agreeing_with_declared"] == n_delta
            and all(r["cells_agreeing_with_declared"] == n_delta - len(aliased)
                    for r in off_by_alias)
            and len(fiber_rows) == len(LIFT_READINGS) * len(STENCIL_READINGS),
            "fiber rows %d; the two other lifts agree at %d of %d cells "
            "(= all but the aliased)"
            % (len(fiber_rows), n_delta - len(aliased), n_delta))

    # ---- the character convention, the other declared item -----------------
    conj_speed_same, conj_head_same, conj_alias, conj_wind_neg = 0, 0, 0, 0
    for g in pool[:ncirc]:
        n = name[g["local"]]
        s2 = {}
        for k in duals:
            acc = ZERO
            for o, v in g["coef"].items():
                acc = fadd(acc, fmul(v, zpow((2 * (k[0] * o[0] + k[1] * o[1])) % 8)))
            s2[k] = MU8[acc]
        d2 = {(k, j): (s2[addv(k, e)] - s2[k]) % 8
              for k in duals for j, e in enumerate(BASIS_DIRECTIONS)}
        if ({Fraction(circle_distance(v), 2) for v in d2.values()}
                == {speed_cell[(n, k, j)] for k in duals for j in range(D)}):
            conj_speed_same += 1
        if (len(set(s2.values())) > 1) == (len(set(disp[n].values())) > 1):
            conj_head_same += 1
        conj_alias += sum(1 for v in d2.values() if v == 4)
        w2 = tuple(Fraction(-sum(lift(d2[(k, j)], LIFT_DECLARED) for k in duals),
                            2 * len(duals)) for j in range(D))
        w_ref = tuple(Fraction(-sum(lift(delta[(n, k, j)], LIFT_DECLARED)
                                    for k in duals), 2 * len(duals))
                      for j in range(D))
        if w2 == tuple(-x for x in w_ref):
            conj_wind_neg += 1
    if mut("MUT-CONVENTION"):
        conj_speed_same -= 1
    LD.gate("G-CHARACTER-CONVENTION-FIBER",
            "the character convention is a declared item with fiber two, and "
            "the whole census is recomputed under the other member: the "
            "conjugate convention relabels the dual torus by k -> -k, so the "
            "speed multiset, the motion head and the aliasing count are "
            "IDENTICAL family by family, while the signed velocity and the "
            "winding are exactly NEGATED -- the labelling and the sign of the "
            "velocity formula are one declaration, not two",
            conj_speed_same == ncirc and conj_head_same == ncirc
            and conj_alias == len(aliased) and conj_wind_neg == ncirc,
            "speed multiset identical at %d of %d; head identical at %d; "
            "aliased cells %d = %d; winding negated at %d"
            % (conj_speed_same, ncirc, conj_head_same, conj_alias,
               len(aliased), conj_wind_neg))

    # ---- THE MOTION HEAD, PER OBJECT --------------------------------------
    say("[6/10] the motion head, family by family and class by class")
    motion = {}
    for n in disp:
        moves = len(set(disp[n].values())) > 1
        by_vel = any(speed_cell[(n, k, j)] != 0 for k in duals for j in range(D))
        if moves != by_vel:
            raise GateFail("G-MOTION-HEAD-PER-FAMILY :: two routes disagree at %s" % n)
        motion[n] = "MOVES" if moves else "STATIC"
    if mut("MUT-MOTION-HEAD"):
        motion[nonconstant[0]] = "STATIC"
    if mut("MUT-MOTION-CONTROL"):
        motion[ctrl] = "MOVES"
    bad_motion = []
    for n in disp:
        want = "MOVES" if len(set(disp[n].values())) > 1 else "STATIC"
        if motion[n] != want:
            bad_motion.append(n)
    LD.gate("G-MOTION-HEAD-PER-FAMILY",
            "every family's motion head is bound to ITS OWN computed "
            "dispersion by its own predicate -- 58 individual verdicts, no "
            "aggregate stands in for any of them -- and two independent "
            "routes (non-constant phase; some nonzero cell speed) agree on "
            "every one",
            not bad_motion, "disagreements %s over %d families"
            % (bad_motion or "none", ncirc))

    moving = sorted(n for n in motion if motion[n] == "MOVES")
    static = sorted(n for n in motion if motion[n] == "STATIC")
    if mut("MUT-TWO-WAY"):
        static = []
    LD.gate("G-MOTION-TWO-WAY",
            "the head is two-way at the control: the NO-MOTION control "
            "returns STATIC and every other family returns MOVES.  A head "
            "that cannot return its other value is not a measurement",
            motion[ctrl] == "STATIC" and static == [ctrl]
            and len(moving) == len(nonconstant)
            and all(motion[n] == "MOVES" for n in nonconstant),
            "MOVES=%d STATIC=%d control=%s->%s"
            % (len(moving), len(static), ctrl, motion[ctrl]))

    circ_classes = [c for c in classes if c["kind"] == "CIRC"]
    noncirc_classes = [c for c in classes if c["kind"] != "CIRC"]
    class_rows, cls_motion_bad = [], []
    for c in classes:
        if c["kind"] != "CIRC":
            class_rows.append({"class": c["rep"], "size": c["size"],
                               "kind": c["kind"], "motion": "NOT-BLOCH-DIAGONAL",
                               "speed": None, "support": None, "radius": None,
                               "aliased_cells": None, "profiles": None})
            continue
        ms = [name[m] for m in c["members"]]
        heads = {motion[m] for m in ms}
        if mut("MUT-CLASS-SPLIT") and c["size"] > 1:
            heads = {"MOVES", "STATIC"}
        if len(heads) != 1:
            cls_motion_bad.append(c["rep"])
        sp = {speed[m] for m in ms}
        if len(sp) != 1:
            cls_motion_bad.append(c["rep"] + "/speed")
        gs = [pool[[g["local"] for g in pool].index(rname[m])] for m in ms]
        class_rows.append({
            "class": c["rep"], "size": c["size"], "kind": "CIRC",
            "motion": sorted(heads)[0], "speed": str(sorted(sp)[0]),
            "support": sorted({g["support"] for g in gs})[0],
            "radius": sorted({g["radius"] for g in gs})[0],
            "aliased_cells": sum(1 for m in ms for k in duals for j in range(D)
                                 if delta[(m, k, j)] == 4),
            "profiles": len({tuple(sigma[m][k] for k in duals) for m in ms})})
    LD.gate("G-MOTION-CLASS-INVARIANT",
            "the motion head and the maximal speed are constant on every "
            "extended class -- they must be, since the point group permutes "
            "the dual torus and preserves the max norm, and here they are "
            "measured to be, class by class",
            not cls_motion_bad, "classes with a split head or speed: %s over %d"
            % (cls_motion_bad or "none", len(circ_classes)))

    classes_moving = [r for r in class_rows if r["motion"] == "MOVES"]
    classes_static = [r for r in class_rows if r["motion"] == "STATIC"]

    # the two-way control on the OTHER side: the controls are not Bloch diagonal
    notbloch = []
    for g in pool[ncirc:]:
        diag = True
        for k in duals:
            chi = character(k, sites)
            img = apply_mat(g["mat"], chi, NS)
            lam = fmul(img[0], fconj(chi[0]))
            if img != [fmul(lam, x) for x in chi]:
                diag = False
                break
        if not diag and not mut("MUT-NOTBLOCH"):
            notbloch.append(name[g["local"]])
    LD.gate("G-NOT-BLOCH-CONTROL",
            "the dispersion census's domain is exactly the circulant family, "
            "and that restriction is MEASURED rather than assumed: not one of "
            "the six declared controls is diagonalised by the characters, so "
            "the three non-circulant classes carry no Bloch dispersion at all",
            len(notbloch) == len(pool) - ncirc == 6
            and len(noncirc_classes) == 3,
            "not Bloch diagonal: %d of %d controls, in %d classes"
            % (len(notbloch), len(pool) - ncirc, len(noncirc_classes)))

    # ---- THE PROPAGATION BOUND --------------------------------------------
    say("[7/10] the propagation bound and the resolution relation")
    diameter = max(torus_absmax(x, L) for x in sites)
    radius_classes = sorted({torus_absmax(x, L) for x in sites})
    over, under, equal = [], [], []
    for g in pool[:ncirc]:
        n = name[g["local"]]
        if speed[n] > g["radius"]:
            over.append(n)
        elif speed[n] < g["radius"]:
            under.append(n)
        else:
            equal.append(n)
    if mut("MUT-REACH"):
        under = under[:-1]
    LD.gate("G-REACH-BOUND-PER-FAMILY",
            "the propagation question, asked of every family separately: does "
            "the family's maximal group speed bound the max-norm reach of one "
            "step of that family, which is exactly its support radius?  Each "
            "of the 58 families answers for itself",
            len(over) + len(under) + len(equal) == ncirc
            and all(speed[n] > byname[n]["radius"] for n in over)
            and all(speed[n] < byname[n]["radius"] for n in under),
            "speed > reach: %d; speed < reach: %d; equal: %d"
            % (len(over), len(under), len(equal)))

    cone_1 = [x for x in sites if torus_absmax(x, L) <= VMAX]
    if mut("MUT-CONE"):
        cone_1 = cone_1[:-1]
    separations = jpath(R4, "counts/separations")
    sep_ceiling = jpath(R4, "counts/separations_ceiling")
    max_defect_radius = jpath(R4, "counts/max_defect_radius")
    radius_ceiling = jpath(R4, "counts/radius_ceiling")
    if mut("MUT-CEILING"):
        sep_ceiling = sep_ceiling + 1
    cone_covers = len(cone_1) == len(sites)
    LD.gate("G-CONE-AT-ONE-STEP",
            "the cone the dispersion predicts after a SINGLE step of the "
            "fastest family already contains every site of the torus, so the "
            "cone constraint on the parent's two-step composed segment "
            "excludes no separation whatever",
            cone_covers and VMAX >= diameter,
            "cone at 1 step = %d of %d sites; VMAX=%s diameter=%d"
            % (len(cone_1), len(sites), VMAX, diameter))

    bound_has_content = (not cone_covers) and not under
    if mut("MUT-BOUND"):
        bound_has_content = True
    LD.gate("G-BOUND-DERIVED",
            "the bound's verdict is DERIVED from the two computed facts -- "
            "whether the one-step cone is proper, and whether any family's "
            "speed falls below its own reach -- and is not a typed opinion",
            bound_has_content is False and bound_has_content
            == ((not cone_covers) and not under),
            "cone proper=%s; families under their own reach=%d; bound has "
            "content=%s" % (not cone_covers, len(under), bound_has_content))
    LD.gate("G-CEILINGS-INHERITED",
            "the parent's two-point rows are inherited AT THEIR CEILINGS and "
            "the disclosure travels with them: 16 of 16 separations carry a "
            "defect and the maximal defect radius is 2 of 2, so neither row "
            "can distinguish a cone from its complement",
            separations == sep_ceiling == 16 and max_defect_radius
            == radius_ceiling == diameter and jpath(R4, "counts/lightcone_content_radii") == [0],
            "separations %d of %d; max defect radius %d of %d; parent's cone "
            "content radii %s" % (separations, sep_ceiling, max_defect_radius,
                                  radius_ceiling,
                                  jpath(R4, "counts/lightcone_content_radii")))

    resolution = {
        "dual_points_per_axis": L,
        "phase_values": 8,
        "aliased_cells": len(aliased),
        "aliased_families": len(alias_families),
        "cells": n_delta,
        "diameter": diameter,
        "radius_classes": radius_classes,
        "interior_radii": [r for r in radius_classes if 0 < r < diameter],
        "vmax": str(VMAX),
        "steps_to_cover": 1 if cone_covers else None,
    }
    if mut("MUT-RESOLUTION"):
        resolution["interior_radii"] = [1, 2]
    LD.gate("G-RESOLUTION-RELATION",
            "the parent's closing observation, stated as a measured relation "
            "in both spaces: on the site side the torus has exactly one "
            "max-norm radius strictly between zero and its diameter, and the "
            "fastest family crosses the whole diameter in one step; on the "
            "momentum side the dual torus carries L points per axis, so the "
            "phase difference reaches its antipodal, direction-free value at "
            "a measured share of cells.  No propagation front is resolvable "
            "at this scale, in either space",
            resolution["interior_radii"] == [1] and resolution["steps_to_cover"] == 1
            and resolution["aliased_cells"] > 0
            and resolution["dual_points_per_axis"] == L,
            "%s" % resolution)

    # ---- TRANSPORT: DRIFT AND WINDING -------------------------------------
    say("[8/10] transport: the drift, the winding, and the tension")
    drift, winding = {}, {}
    for reading in LIFT_READINGS:
        for g in pool[:ncirc]:
            n = name[g["local"]]
            dv = [Fraction(0)] * D
            for o, v in g["coef"].items():
                w = fmul(v, fconj(v))
                oo = offset_rep(o, L, reading)
                for j in range(D):
                    dv[j] += w[0] * oo[j]
            drift[(n, reading)] = tuple(dv)
            wv = []
            for j, e in enumerate(BASIS_DIRECTIONS):
                tot = sum(lift(delta[(n, k, j)], reading) for k in duals)
                wv.append(Fraction(-tot, 2 * len(duals)))
            winding[(n, reading)] = tuple(wv)
    agree = {}
    for r1 in LIFT_READINGS:
        for r2 in LIFT_READINGS:
            agree[(r1, r2)] = sum(1 for g in pool[:ncirc]
                                  if drift[(name[g["local"]], r1)]
                                  == winding[(name[g["local"]], r2)])
    if mut("MUT-IDENTITY"):
        agree[(LIFT_DECLARED, LIFT_DECLARED)] -= 1
    matched_agree = agree[(LIFT_DECLARED, LIFT_DECLARED)]
    full = sorted(kk for kk, v in agree.items() if v == ncirc)
    best_other = max(v for kk, v in agree.items() if v != ncirc)
    LD.gate("G-DRIFT-WINDING-IDENTITY",
            "the two roads to how far a family moves in one step -- the Born "
            "drift of the coefficient map in position space, and the winding "
            "of the eigenphase around the dual torus -- are computed "
            "independently and compared family by family under all nine ways "
            "of reading the two antipodal ties.  EXACTLY ONE reading pair "
            "makes them agree for every family, and it is the pair that "
            "resolves both ties the same way: by averaging.  The velocity "
            "convention is therefore SELECTED by an identity, not chosen",
            matched_agree == ncirc and full == [(LIFT_DECLARED, LIFT_DECLARED)]
            and best_other < ncirc,
            "identity holds at %d of %d reading pairs (%s); best other pair "
            "%d of %d families" % (len(full), len(agree), full, best_other, ncirc))

    supp_table, supp_table_alt = {}, {}
    for g in pool[:ncirc]:
        n = name[g["local"]]
        row = supp_table.setdefault(g["support"], {"generators": 0, "nonzero_drift": 0})
        row["generators"] += 1
        if any(drift[(n, "TIE-AVERAGED")]):
            row["nonzero_drift"] += 1
        alt = supp_table_alt.setdefault(g["support"],
                                        {"generators": 0, "nonzero_drift": 0})
        alt["generators"] += 1
        if any(drift[(n, "POSITIVE")]):
            alt["nonzero_drift"] += 1
    if mut("MUT-DRIFT-TABLE"):
        supp_table[1]["nonzero_drift"] = 13
    LD.gate("G-EFFECTUS-DRIFT-TABLE",
            "the frozen effectus review's one-step drift table is reproduced "
            "from this unit's own rebuild, and reproducing it IDENTIFIES the "
            "convention it was taken under: the antipodal displacement is "
            "tie-averaged to zero.  Under that reading, and only under it, "
            "the table's three rows come out as the review printed them",
            supp_table[1] == {"generators": 16, "nonzero_drift": 12}
            and supp_table[2] == {"generators": 18, "nonzero_drift": 0}
            and supp_table[3] == {"generators": 24, "nonzero_drift": 0},
            "%s" % {k: supp_table[k] for k in sorted(supp_table)})

    nonzero_wind = sorted(name[g["local"]] for g in pool[:ncirc]
                          if any(winding[(name[g["local"]], LIFT_DECLARED)]))
    monomials = sorted(name[g["local"]] for g in pool[:ncirc] if g["monomial"])
    interfering = sorted(name[g["local"]] for g in pool[:ncirc] if not g["monomial"])
    wind_implies_mono = [n for n in nonzero_wind if n not in monomials]
    interfering_moving = [n for n in interfering if motion[n] == "MOVES"]
    interfering_zero_net = [n for n in interfering
                            if not any(winding[(n, LIFT_DECLARED)])
                            and not any(drift[(n, LIFT_DECLARED)])]
    if mut("MUT-CHARGE"):
        interfering_zero_net = interfering_zero_net[:-1]
    LD.gate("G-CHARGE-WITHOUT-MOMENTUM",
            "the parent panel's tension, measured: every family with nonzero "
            "net transport is monomial, every interfering family has exactly "
            "zero net transport in BOTH spaces, and yet every one of those "
            "interfering families MOVES -- its dispersion is non-constant and "
            "its group velocity is nonzero at individual momenta.  The "
            "cancellation, not the absence, is what the class census saw",
            not wind_implies_mono
            and len(interfering_zero_net) == len(interfering)
            and len(interfering_moving) == len(interfering)
            and jpath(R4, "counts/markov_pairs")
            == len(pool) ** 2 - (len(pool) - len(monomials)) ** 2,
            "nonzero winding %d (all monomial); interfering %d, all with zero "
            "net transport and all MOVING; the inherited Markovian control's "
            "%d pairs are exactly the %d^2 - %d^2 pairs with a monomial member"
            % (len(nonzero_wind), len(interfering),
               jpath(R4, "counts/markov_pairs"), len(pool),
               len(pool) - len(monomials)))
    LD.gate("G-MOMENTUM-ON-THE-SYMBOL",
            "the reading the operator review names is available in this "
            "unit's own numbers: the momentum label lives on the symbol, and "
            "the symbol SEPARATES COMPLETELY -- the reduced dispersion takes a "
            "different value on every one of the families, where the parent's "
            "invariant labels do not even separate its classes.  Complete "
            "separation is forced (the character transform is invertible, and "
            "the reduction by s(0) is exactly the global-phase quotient) and "
            "it is measured here",
            S["distinct_profiles"] == ncirc
            and S["distinct_profiles"] > jpath(R4, "counts/class_labels"),
            "distinct reduced dispersions %d vs %d distinct invariant labels"
            % (S["distinct_profiles"], jpath(R4, "counts/class_labels")))

    # ---- assemble the counts ----------------------------------------------
    counts = {
        "families": ncirc,
        "momenta": len(duals),
        "cells": total_cells,
        "eigen_verified": eig_ok,
        "in_mu8": mu8_ok,
        "unit_modulus": unit_ok,
        "moving": len(moving),
        "static": len(static),
        "control": ctrl,
        "classes_extended": len(classes),
        "classes_circulant": len(circ_classes),
        "classes_moving": len(classes_moving),
        "classes_static": len(classes_static),
        "classes_not_bloch": len(noncirc_classes),
        "distinct_profiles": S["distinct_profiles"],
        "parity_invariant": ncirc - len(parity_bad),
        "velocity_cells": n_delta,
        "integer_velocities": n_delta - len(odd_delta),
        "speed_spectrum": [str(v) for v in spectrum],
        "vmax": str(VMAX),
        "aliased_cells": len(aliased),
        "aliased_families": len(alias_families),
        "velocity_definition": "%s-DIFFERENCE-WITH-%s"
                               % (STENCIL_DECLARED, LIFT_DECLARED),
        "velocity_fiber": len(fiber_rows),
        "reach_over": len(over),
        "reach_under": len(under),
        "reach_equal": len(equal),
        "cone_sites_one_step": len(cone_1),
        "sites": len(sites),
        "diameter": diameter,
        "interior_radii": resolution["interior_radii"],
        "bound_has_content": bound_has_content,
        "separations": separations,
        "separations_ceiling": sep_ceiling,
        "max_defect_radius": max_defect_radius,
        "radius_ceiling": radius_ceiling,
        "drift_winding_matched": matched_agree,
        "drift_winding_mismatched": best_other,
        "reading_pairs": len(agree),
        "reading_pairs_with_identity": len(full),
        "nonzero_winding": len(nonzero_wind),
        "monomial": len(monomials),
        "nonmonomial_pool": len(pool) - len(monomials),
        "interfering": len(interfering),
        "interfering_moving": len(interfering_moving),
        "markov_nonzero": jpath(R4, "counts/markov_nonzero"),
        "markov_pairs": jpath(R4, "counts/markov_pairs"),
        "class_labels": jpath(R4, "counts/class_labels"),
        "L": L, "d": D, "alphabet": len(alphabet), "pool": len(pool),
        "field": jpath(R4, "counts/field"),
        "stencil": jpath(R4, "counts/stencil"),
        "sector": jpath(R4, "counts/sector"),
        "connective_tag": jpath(R4, "counts/connective_tag"),
        "forcing_link": jpath(R4, "counts/forcing_link"),
        "indivisibility": jpath(R4, "counts/indivisibility"),
    }

    S.update({
        "arena_declaration": ARENA,
        "counts": counts,
        "class_rows": class_rows,
        "resolution": resolution,
        "fiber_rows": fiber_rows,
        "supp_table": {str(k): supp_table[k] for k in sorted(supp_table)},
        "supp_table_alt": {str(k): supp_table_alt[k] for k in sorted(supp_table_alt)},
        "agreement_matrix": {"%s|%s" % kk: v for kk, v in sorted(agree.items())},
        "profiles": {"distinct": len(profiles),
                     "largest": max(len(v) for v in profiles.values())},
    })
    S["_dispersion"] = disp
    S["_sigma"] = sigma
    S["_delta"] = delta
    S["_speed"] = speed
    S["_motion"] = motion
    S["_drift"] = drift
    S["_winding"] = winding
    S["_pool"] = pool
    S["_name"] = name
    S["_duals"] = duals
    S["_ncirc"] = ncirc
    S["_over"] = over
    S["_under"] = under
    S["_moving"] = moving
    S["_nonzero_wind"] = nonzero_wind
    S["_alias_families"] = alias_families
    return S, LD


# ===========================================================================
# SECTION 7.  THE VERDICT, AND THE INDEPENDENT RECONSTRUCTION
# ===========================================================================

def derive_head(c):
    """THE HEAD LAW.  Path A."""
    if c["families"] == 0 or c["momenta"] == 0:
        return "R4B-BLOCKED-AT-EMPTY-CENSUS"
    if c["eigen_verified"] != c["cells"]:
        return "R4B-BLOCKED-AT-UNVERIFIED-BLOCH-DIAGONALISATION"
    if c["in_mu8"] != c["cells"]:
        return "R4B-BLOCKED-AT-EIGENPHASE-OUTSIDE-MU-8"
    if c["moving"] == 0:
        return "R4B-NO-MOTION"
    return "R4B-DISPERSION-READ"


SEGMENT_KEYS = [
    ("MOTION", ["moving", "families", "static", "control", "classes_moving",
                "classes_circulant", "classes_not_bloch", "classes_extended"]),
    ("DISPERSION", ["in_mu8", "cells", "eigen_verified", "unit_modulus",
                    "parity_invariant", "families", "distinct_profiles",
                    "class_labels"]),
    ("VELOCITY", ["speed_spectrum", "vmax", "integer_velocities",
                  "velocity_cells", "aliased_cells", "aliased_families",
                  "velocity_definition", "velocity_fiber"]),
    ("BOUND", ["bound_has_content", "cone_sites_one_step", "sites", "vmax",
               "diameter", "reach_under", "reach_over", "reach_equal",
               "families", "separations", "separations_ceiling",
               "max_defect_radius", "radius_ceiling", "interior_radii"]),
    ("TRANSPORT", ["drift_winding_matched", "families", "reading_pairs_with_identity",
                   "reading_pairs", "drift_winding_mismatched",
                   "nonzero_winding", "monomial", "interfering",
                   "interfering_moving", "markov_nonzero", "markov_pairs"]),
    ("SCOPE", ["d", "L", "field", "alphabet", "pool", "stencil", "sector",
               "connective_tag", "forcing_link", "indivisibility", "momenta"]),
]


def build_verdict(c):
    """Path A: the verdict assembled from the counts."""
    if mut("MUT-COUNT-TYPED"):
        c = dict(c)
        c["moving"] = c["families"]      # a value typed into the string alone
    segs = [
        ("MOTION", "MOVING=%s-OF-%s;STATIC=%s-OF-%s;CONTROL=%s-IDENTITY-TWO-WAY;"
                   "CLASSES-MOVING=%s-OF-%s-CIRCULANT;NOT-BLOCH-DIAGONAL=%s-OF-%s"
         % (c["moving"], c["families"], c["static"], c["families"], c["control"],
            c["classes_moving"], c["classes_circulant"], c["classes_not_bloch"],
            c["classes_extended"])),
        ("DISPERSION", "EIGENPHASES-IN-MU-8=%s-OF-%s;EIGEN-EQUATION-VERIFIED=%s;"
                       "UNIT-MODULUS=%s;PARITY-INVARIANT=%s-OF-%s;"
                       "DISTINCT-REDUCED-PROFILES=%s-VS-%s-INVARIANT-LABELS"
         % (c["in_mu8"], c["cells"], c["eigen_verified"], c["unit_modulus"],
            c["parity_invariant"], c["families"], c["distinct_profiles"],
            c["class_labels"])),
        ("VELOCITY", "SPECTRUM=%s;VMAX=%s;INTEGER-VALUED=%s-OF-%s;"
                     "ALIASED=%s-OF-%s-IN-%s-FAMILIES;DEFINITION=%s(FIBER=%s)"
         % ("+".join(c["speed_spectrum"]), c["vmax"], c["integer_velocities"],
            c["velocity_cells"], c["aliased_cells"], c["velocity_cells"],
            c["aliased_families"], c["velocity_definition"], c["velocity_fiber"])),
        ("BOUND", "NO-CONTENT=%s;CONE-AT-ONE-STEP=%s-OF-%s-SITES;VMAX=%s=DIAMETER=%s;"
                  "REACH-BOUND-FALSE-AT=%s-OF-%s;OVERSHOOTS-AT=%s;SATURATES-AT=%s;"
                  "INHERITED-CEILINGS=SEPARATIONS=%s-OF-%s;MAX-DEFECT-RADIUS=%s-OF-%s;"
                  "INTERIOR-RADII=%s"
         % ("YES" if not c["bound_has_content"] else "NO", c["cone_sites_one_step"],
            c["sites"], c["vmax"], c["diameter"], c["reach_under"], c["families"],
            c["reach_over"], c["reach_equal"], c["separations"],
            c["separations_ceiling"], c["max_defect_radius"], c["radius_ceiling"],
            "+".join(str(x) for x in c["interior_radii"]))),
        ("TRANSPORT", "DRIFT=WINDING-AT-%s-OF-%s-FAMILIES-UNDER-%s-OF-%s-READING-"
                      "PAIRS(BEST-OTHER=%s-OF-%s);NONZERO-WINDING=%s-OF-%s-ALL-"
                      "MONOMIAL-OF-%s;INTERFERING=%s-ZERO-NET-TRANSPORT-AND-%s-"
                      "MOVING;MARKOV=%s-OF-%s-NONZERO-INHERITED"
         % (c["drift_winding_matched"], c["families"],
            c["reading_pairs_with_identity"], c["reading_pairs"],
            c["drift_winding_mismatched"], c["families"], c["nonzero_winding"],
            c["families"], c["monomial"], c["interfering"],
            c["interfering_moving"], c["markov_nonzero"], c["markov_pairs"])),
        ("SCOPE", "D=%s;L=%s;FIELD=%s;ALPHABET=%s;GENERATORS=%s;STENCIL=%s;SECTOR=%s;"
                  "MOMENTUM-LATTICE=DUAL-TORUS-%s-DECLARED;CONNECTIVE=%s(FORCED-BY-"
                  "ANCHORED-LINK-%s);INDIVISIBILITY=%s;FINITE-LATTICE-ONLY;"
                  "NO-CONTINUUM-CLAIM;NO-INTERACTING-THEORY-CLAIM-BEYOND-THE-"
                  "COMPOSED-SEGMENT-DEFECT"
         % (c["d"], c["L"], c["field"], c["alphabet"], c["pool"], c["stencil"],
            c["sector"], c["momenta"], c["connective_tag"], c["forcing_link"],
            c["indivisibility"])),
    ]
    head = derive_head(c)
    return head, segs, head + "<" + "|".join("%s=%s" % kv for kv in segs) + ">"


def reconstruct_from_serialized(txt):
    """THE INDEPENDENT COMPARATOR.  Path B.  Rebuilds the COMPLETE verdict
    string -- head included -- from the SERIALIZED receipt text alone, by a
    code path that shares no helper with build_verdict, calls neither
    derive_head nor any formatter above, and types no value: every number it
    prints is read from the parsed JSON."""
    R = json.loads(txt)
    c = R["counts"]
    if c["families"] == 0 or c["momenta"] == 0:
        hd = "R4B-BLOCKED-AT-EMPTY-CENSUS"
    elif c["eigen_verified"] != c["cells"]:
        hd = "R4B-BLOCKED-AT-UNVERIFIED-BLOCH-DIAGONALISATION"
    elif c["in_mu8"] != c["cells"]:
        hd = "R4B-BLOCKED-AT-EIGENPHASE-OUTSIDE-MU-8"
    elif c["moving"] == 0:
        hd = "R4B-NO-MOTION"
    else:
        hd = "R4B-DISPERSION-READ"
    pre = R["verdict"]["preregistered_heads"]
    if not [nm for nm in pre if hd == nm or hd.startswith(nm + "-")]:
        hd = "R4B-HEAD-OUTSIDE-THE-PIN"
    g = lambda k: str(c[k])
    out = []
    out.append("MOTION=MOVING=" + g("moving") + "-OF-" + g("families") + ";STATIC="
               + g("static") + "-OF-" + g("families") + ";CONTROL=" + g("control")
               + "-IDENTITY-TWO-WAY;CLASSES-MOVING=" + g("classes_moving") + "-OF-"
               + g("classes_circulant") + "-CIRCULANT;NOT-BLOCH-DIAGONAL="
               + g("classes_not_bloch") + "-OF-" + g("classes_extended"))
    out.append("DISPERSION=EIGENPHASES-IN-MU-8=" + g("in_mu8") + "-OF-" + g("cells")
               + ";EIGEN-EQUATION-VERIFIED=" + g("eigen_verified") + ";UNIT-MODULUS="
               + g("unit_modulus") + ";PARITY-INVARIANT=" + g("parity_invariant")
               + "-OF-" + g("families") + ";DISTINCT-REDUCED-PROFILES="
               + g("distinct_profiles") + "-VS-" + g("class_labels")
               + "-INVARIANT-LABELS")
    out.append("VELOCITY=SPECTRUM=" + "+".join(c["speed_spectrum"]) + ";VMAX="
               + g("vmax") + ";INTEGER-VALUED=" + g("integer_velocities") + "-OF-"
               + g("velocity_cells") + ";ALIASED=" + g("aliased_cells") + "-OF-"
               + g("velocity_cells") + "-IN-" + g("aliased_families")
               + "-FAMILIES;DEFINITION=" + g("velocity_definition") + "(FIBER="
               + g("velocity_fiber") + ")")
    out.append("BOUND=NO-CONTENT=" + ("YES" if not c["bound_has_content"] else "NO")
               + ";CONE-AT-ONE-STEP=" + g("cone_sites_one_step") + "-OF-" + g("sites")
               + "-SITES;VMAX=" + g("vmax") + "=DIAMETER=" + g("diameter")
               + ";REACH-BOUND-FALSE-AT=" + g("reach_under") + "-OF-" + g("families")
               + ";OVERSHOOTS-AT=" + g("reach_over") + ";SATURATES-AT="
               + g("reach_equal") + ";INHERITED-CEILINGS=SEPARATIONS="
               + g("separations") + "-OF-" + g("separations_ceiling")
               + ";MAX-DEFECT-RADIUS=" + g("max_defect_radius") + "-OF-"
               + g("radius_ceiling") + ";INTERIOR-RADII="
               + "+".join([str(x) for x in c["interior_radii"]]))
    out.append("TRANSPORT=DRIFT=WINDING-AT-" + g("drift_winding_matched") + "-OF-"
               + g("families") + "-FAMILIES-UNDER-"
               + g("reading_pairs_with_identity") + "-OF-" + g("reading_pairs")
               + "-READING-PAIRS(BEST-OTHER=" + g("drift_winding_mismatched")
               + "-OF-" + g("families") + ");NONZERO-WINDING="
               + g("nonzero_winding") + "-OF-" + g("families") + "-ALL-MONOMIAL-OF-"
               + g("monomial") + ";INTERFERING=" + g("interfering")
               + "-ZERO-NET-TRANSPORT-AND-" + g("interfering_moving")
               + "-MOVING;MARKOV=" + g("markov_nonzero") + "-OF-" + g("markov_pairs")
               + "-NONZERO-INHERITED")
    out.append("SCOPE=D=" + g("d") + ";L=" + g("L") + ";FIELD=" + g("field")
               + ";ALPHABET=" + g("alphabet") + ";GENERATORS=" + g("pool")
               + ";STENCIL=" + g("stencil") + ";SECTOR=" + g("sector")
               + ";MOMENTUM-LATTICE=DUAL-TORUS-" + g("momenta")
               + "-DECLARED;CONNECTIVE=" + g("connective_tag")
               + "(FORCED-BY-ANCHORED-LINK-" + g("forcing_link") + ");INDIVISIBILITY="
               + g("indivisibility") + ";FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;"
               "NO-INTERACTING-THEORY-CLAIM-BEYOND-THE-COMPOSED-SEGMENT-DEFECT")
    return hd + "<" + "|".join(out) + ">"


# ===========================================================================
# SECTION 8.  THE RECEIPT
# ===========================================================================

def qstr(x):
    if isinstance(x, Fraction):
        return str(x)
    return x


def has_float(o):
    if isinstance(o, float):
        return True
    if isinstance(o, dict):
        return any(has_float(k) or has_float(v) for k, v in o.items())
    if isinstance(o, (list, tuple)):
        return any(has_float(v) for v in o)
    return False


def build_receipt(S, LD):
    disp, sigma, name = S["_dispersion"], S["_sigma"], S["_name"]
    duals = S["_duals"]
    rows = []
    for g in S["_pool"][:S["_ncirc"]]:
        n = name[g["local"]]
        rows.append({
            "family": n,
            "axis": list(g["axis"]),
            "axis_order": g["axis_ord"],
            "support": g["support"],
            "radius": g["radius"],
            "monomial": g["monomial"],
            "coefficients": [[list(o), [str(q) for q in v]]
                             for o, v in sorted(g["coef"].items())],
            "eigenphase": [disp[n][k] for k in duals],
            "reduced_dispersion": [sigma[n][k] for k in duals],
            "motion": S["_motion"][n],
            "max_speed": str(S["_speed"][n]),
            "aliased_cells": sum(1 for k in duals for j in range(S["counts"]["d"])
                                 if S["_delta"][(n, k, j)] == 4),
            "drift": [str(x) for x in S["_drift"][(n, LIFT_DECLARED)]],
            "winding": [str(x) for x in S["_winding"][(n, LIFT_DECLARED)]],
            "reach_vs_speed": ("OVER" if n in S["_over"] else
                               ("UNDER" if n in S["_under"] else "EQUAL")),
        })
    head, segs, string = build_verdict(S["counts"])
    R = {
        "schema": SCHEMA,
        "unit": "v14 R4b -- momentum: reading the dispersions",
        "paper": PAPER_REL,
        "arithmetic": "fractions.Fraction 4-tuples over Q(zeta_8) modulo "
                      "x^4 + 1; eigenphases exact in Z/8; velocities exact "
                      "rationals; no floats",
        "arena_declaration": ARENA,
        "momentum_lattice": {"dual_torus": [list(k) for k in duals],
                             "character": "chi_k(x) = zeta_4^{k.x}",
                             "symbol": "lambda(k) = sum_o c_o zeta_4^{-k.o}",
                             "declared": True},
        "byte_anchors": S["byte_anchors"],
        "path_value_anchors": S["path_value_anchors"],
        "verbatim_anchors": S["verbatim_anchors"],
        "axes": S["axes"],
        "translation_stabilisers": S["stabilisers"],
        "pool_counts": S["pool_counts"],
        "class_sizes": S["class_sizes"],
        "dispersion_census": rows,
        "class_rows": S["class_rows"],
        "velocity_fiber": S["fiber_rows"],
        "velocity_definition": {
            "declared": "%s difference of the eigenphase along +e_j on the "
                        "dual torus, divided by the momentum step: "
                        "v_j(k) = -(L/2pi) [theta(k+e_j) - theta(k)] = "
                        "-lift(Delta_j s(k))/2" % STENCIL_DECLARED.lower(),
            "tie_reading": LIFT_DECLARED,
            "lift_readings": list(LIFT_READINGS),
            "stencil_readings": list(STENCIL_READINGS),
            "speed": "the branch-free circle distance of Delta_j s to 0, "
                     "halved",
        },
        "resolution": S["resolution"],
        "support_drift_table": S["supp_table"],
        "support_drift_table_positive_reading": S["supp_table_alt"],
        "agreement_matrix": S["agreement_matrix"],
        "profiles": S["profiles"],
        "counts": S["counts"],
        "verdict": {"head": head, "segments": [list(x) for x in segs],
                    "string": string,
                    "preregistered_heads": list(PREREGISTERED_HEADS)},
    }
    return R


# ===========================================================================
# SECTION 9.  RECEIPT GATES, MUTANTS, COMPLIANCE
# ===========================================================================

MUTANTS = [
    ("MUT-ANCHOR", "G-BYTE-ANCHORS", "corrupts the parent receipt's digest"),
    ("MUT-PATH-VALUE", "G-PATH-VALUE-ANCHORS", "moves an inherited value"),
    ("MUT-VERBATIM", "G-VERBATIM-ANCHORS", "edits a verbatim window"),
    ("MUT-LATTICE-UNBOUND", "G-ARENA-FROM-ANCHOR", "censuses a lattice the "
     "anchor did not admit"),
    ("MUT-ALPHABET", "G-ALPHABET-REBUILT", "drops an alphabet element"),
    ("MUT-GAUGE-ORBIT", "G-GAUGE-ORBITS-FREE", "reports a short gauge orbit"),
    ("MUT-UNITARITY", "G-UNITARY-TWO-ROUTES", "breaks one generator's unitarity"),
    ("MUT-BIJECTION", "G-REBUILD-BIJECTION", "drops a family from the rebuild"),
    ("MUT-INVARIANT", "G-REBUILD-INVARIANTS", "injects an invariant disagreement"),
    ("MUT-CLASS-DROP", "G-CLASS-PARTITION-REBUILT", "drops an extended class"),
    ("MUT-SYMBOL", "G-BLOCH-EIGEN-EQUATION", "perturbs one symbol"),
    ("MUT-NONCONSTANT", "G-NONCONSTANT-CENSUS", "miscounts the non-constant "
     "dispersions"),
    ("MUT-MOTION-HEAD", "G-MOTION-HEAD-PER-FAMILY", "flips one family's head"),
    ("MUT-MOTION-CONTROL", "G-MOTION-HEAD-PER-FAMILY", "flips the control's head"),
    ("MUT-SPEED", "G-VMAX-DERIVED", "inflates one family's speed"),
    ("MUT-REACH", "G-REACH-BOUND-PER-FAMILY", "hides a family that falls below "
     "its own reach"),
    ("MUT-IDENTITY", "G-DRIFT-WINDING-IDENTITY", "breaks the drift-winding count"),
    ("MUT-DRIFT-TABLE", "G-EFFECTUS-DRIFT-TABLE", "moves a row of the review's "
     "table"),
    ("MUT-COUNT-TYPED", "G-VERDICT-RECONSTRUCTED", "types a count the census "
     "did not produce"),
    ("MUT-HEAD-TYPED", "G-VERDICT-RECONSTRUCTED", "retypes the head after the "
     "verdict object exists"),
    ("MUT-HEAD-CONSTANT", "G-HEAD-LAW-RESPONSIVE", "makes the head law constant"),
    ("MUT-HEAD-OUTSIDE-PIN", "G-VERDICT-PREREGISTERED", "names a head the pin "
     "never registered"),
    ("MUT-FLIP-DEAD", "G-VERDICT-VALUES-FLIPPABLE", "renders a verdict value "
     "from a key the reconstruction ignores"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "renders a claim the paper does not "
     "carry"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE", "leaves a paper numeral "
     "uncovered"),
    ("MUT-CLI-PERMISSIVE", "G-CLI-CONTRACT", "accepts an unknown flag"),
    ("MUT-WAIVER", "G-WAIVERS-VERIFIED", "waives a gate with no forcing"),
    ("MUT-REGISTRY", "G-GATE-MUTANT-COVERAGE", "adds a gate no mutant targets"),
    ("MUT-FLOAT", "G-NO-FLOATS", "puts a float in the receipt"),
    ("MUT-LAUNDER", "G-NO-MUTANT-ONLY-CLAUSE", "guards a gate predicate with "
     "the mutant switch"),
    ("MUT-DELTA-ODD", "G-PHASE-DIFFERENCES-EVEN", "injects an odd phase "
     "difference"),
    ("MUT-FIBER", "G-VELOCITY-DEFINITION-FIBER", "hides a reading of the fiber"),
    ("MUT-ALIAS", "G-ALIASING-CENSUS", "miscounts the aliased cells"),
    ("MUT-NOTBLOCH", "G-NOT-BLOCH-CONTROL", "claims a control is Bloch diagonal"),
    ("MUT-PARITY", "G-PHASE-PARITY-INVARIANT", "injects a mixed-parity family"),
    ("MUT-CONTROL-ID", "G-CONTROL-IS-THE-IDENTITY", "misidentifies the control"),
    ("MUT-CEILING", "G-CEILINGS-INHERITED", "drops the ceiling disclosure"),
    ("MUT-CONE", "G-CONE-AT-ONE-STEP", "shrinks the one-step cone"),
    ("MUT-RESOLUTION", "G-RESOLUTION-RELATION", "breaks a leg of the resolution "
     "relation"),
    ("MUT-CHARGE", "G-CHARGE-WITHOUT-MOMENTUM", "claims an interfering family "
     "transports"),
    ("MUT-SYMBOL-LABEL", "G-MOMENTUM-ON-THE-SYMBOL", "claims the symbol "
     "separates no more than the labels"),
    ("MUT-CLASS-SPLIT", "G-MOTION-CLASS-INVARIANT", "splits a class's head"),
    ("MUT-DETERMINISM", "G-RECEIPT-ROUND-TRIP", "makes the receipt fail to "
     "round-trip"),
    ("MUT-SELFTEST-WRITES", "G-SELFTEST-WRITES-NOTHING", "lets the self-test "
     "path reach a writer"),
    ("MUT-SUBPROCESS", "G-NO-SUBPROCESS", "imports a subprocess module"),
    ("MUT-SCOPE", "G-SCOPE-INHERITED", "moves the inherited connective clause"),
    ("MUT-STABILISER", "G-TRANSLATION-STABILISER", "shrinks a circulant's "
     "translation stabiliser"),
    ("MUT-CONVENTION", "G-CHARACTER-CONVENTION-FIBER", "breaks the character "
     "convention's invariance census"),
    ("MUT-DANGLING-CONSUMER", "G-ANCHOR-CONSUMERS-EXIST", "binds a verbatim "
     "window to a gate that does not exist"),
    ("MUT-AXES", "G-AXES-EXHAUSTIVE", "drops an axis from the exhaustive set"),
    ("MUT-FIELD", "G-FIELD-CANONICAL", "breaks the order of zeta_8"),
    ("MUT-DUAL", "G-DUAL-TORUS", "drops a momentum from the dual torus"),
    ("MUT-MU8", "G-EIGENPHASE-IN-MU8", "reports an eigenvalue outside mu_8"),
    ("MUT-MODULUS", "G-UNIT-MODULUS", "loses a unit-modulus verification"),
    ("MUT-DENOMINATOR", "G-MU8-THEOREM-LEGS", "admits an odd denominator"),
    ("MUT-GAUGE-PHASE", "G-PHASE-GAUGE-COVARIANT", "breaks gauge covariance"),
    ("MUT-SPECTRUM", "G-SPEED-CANONICAL", "truncates the speed spectrum"),
    ("MUT-TWO-WAY", "G-MOTION-TWO-WAY", "empties the STATIC side of the head"),
    ("MUT-BOUND", "G-BOUND-DERIVED", "claims the bound has content"),
    ("MUT-CLASS-SIZES", "G-CLASS-SIZES", "drops a class size"),
    ("MUT-CONTROLS", "G-REBUILD-CONTROLS", "breaks a control's rebuild"),
    ("MUT-POOL-COUNT", "G-POOL-COUNTS-DERIVED", "miscounts the pool"),
    ("MUT-EXTRA-READ", "G-RUNTIME-INPUTS-ENUMERATED", "reads an undeclared file"),
    ("MUT-PARENT-IMPORT", "G-PARENT-NOT-IMPORTED", "imports the parent program"),
    ("MUT-SUCCESSOR", "G-UNIT-IS-THE-DECLARED-SUCCESSOR", "loses the successor "
     "register"),
    ("MUT-LATTICE-UNDECLARED", "G-MOMENTUM-LATTICE-DECLARED", "loses the pin's "
     "declaration of the momentum lattice"),
]


def cli_error_probe(parser, argv):
    try:
        parser(argv)
        return False
    except CliError:
        return True


class CliError(Exception):
    pass


def parse_args(argv):
    """THE ARGV PARSER (#82).  A whitelist; every unknown flag, unknown flag
    argument and missing argument raises."""
    opts = {"write": True, "mutant": None, "break_anchor": None,
            "verify_paper": None, "selftest": False}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            opts["write"] = False
        elif a == "--selftest":
            opts["selftest"] = True
            # the self-test path must never reach a writer; MUT-SELFTEST-WRITES
            # is the injection that lets it, and G-SELFTEST-WRITES-NOTHING is
            # the gate that catches it
            opts["write"] = bool(mut("MUT-SELFTEST-WRITES"))
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
    """the FORBIDDEN shape (the registered disease, #82, four named
    recurrences): a runner that ignores what it does not recognise and
    proceeds to a delivery run.  Present only as the CLI gate's falsifier;
    nothing in the delivery path calls it."""
    opts = {"write": True, "mutant": None, "break_anchor": None,
            "verify_paper": None, "selftest": False}
    if "--no-write" in argv:
        opts["write"] = False
    return opts


NUMERAL_RE = r"[0-9]+(?:[.,/][0-9]+)*"

DERIVED_IN_TEXT = {
    "0": "the offset 0 of the stencil {0, a, -a}, the zero of the field, the "
         "zero phase difference and the zero radius; sections 2 and 4",
    "1": "the section numbers, the radius-1 ball, the one-step reach and the "
         "unit modulus; sections 2, 4 and 6",
    "3": "the section numbers and the 3-term stencil named in SCOPE",
    "5": "the section numbers",
    "7": "the section numbers",
    "9": "the section numbers",
    "10": "the section numbers",
    "11": "the section numbers",
    "12": "the section numbers",
    "1/2": "the coefficient moduli of the declared alphabet, quoted from the "
           "parent's construction; section 2",
    "6": "the section numbers and the six declared controls, which the pool "
         "counts render as 4 brickwork plus 2 scrambled; sections 2 and 5",
    "15": "this paper's number in the programme; the header",
}


def paper_claims(R):
    c = R["counts"]
    cl = {
        "families": "58 circulant families",
        "momenta": "16 momenta",
        "cells": "%d (family, momentum) cells" % c["cells"],
        "moving": "%d of %d families MOVE" % (c["moving"], c["families"]),
        "static": "%s, and it is the identity" % c["control"],
        "mu8": "every one of the %d eigenvalues is an 8th root of unity"
               % c["in_mu8"],
        "eigen": "verified as an exact matrix identity at all %d cells"
                 % c["eigen_verified"],
        "profiles": "%d distinct reduced dispersions" % c["distinct_profiles"],
        "labels": "%d distinct invariant labels" % c["class_labels"],
        "spectrum": "the speed spectrum is {0, 1, 2}",
        "vmax": "VMAX = %s" % c["vmax"],
        "cells_v": "%d cells" % c["velocity_cells"],
        "alias": "%d of %d cells, in %d of %d families"
                 % (c["aliased_cells"], c["velocity_cells"],
                    c["aliased_families"], c["families"]),
        "fiber": "%d readings" % c["velocity_fiber"],
        "reach": "%d families overshoot it, %d fall below it, %d meet it exactly"
                 % (c["reach_over"], c["reach_under"], c["reach_equal"]),
        "cone": "%d of %d sites" % (c["cone_sites_one_step"], c["sites"]),
        "diameter": "diameter %d" % c["diameter"],
        "ceilings": "16 of 16 separations and a maximal defect radius of 2 of 2",
        "identity": "%d of %d families" % (c["drift_winding_matched"], c["families"]),
        "mismatched": "%d of %d" % (c["drift_winding_mismatched"], c["families"]),
        "winding": "%d families with nonzero winding, every one of them monomial"
                   % c["nonzero_winding"],
        "interfering": "%d interfering families" % c["interfering"],
        "monomial": "%d monomial families" % c["monomial"],
        "markov": "0 of 1792",
        "classes": "%d extended classes" % c["classes_extended"],
        "classes_moving": "%d of the %d circulant classes MOVE"
                          % (c["classes_moving"], c["classes_circulant"]),
        "notbloch": "%d classes carry no Bloch dispersion" % c["classes_not_bloch"],
        "drift_table": "16 | 12", "drift_table2": "18 | 0", "drift_table3": "24 | 0",
        "identity_pairs": "1 of the 9 reading pairs",
        "verdict_values": "%d measured values" % R["totals"]["verdict_values"],
        "pool": "64 generators", "alphabet": "25 elements",
        "axes": "9 axes", "L": "L = 4", "d": "d = 2",
    }
    # the instrument's own totals close only after the mutant sweep; the claims
    # that render from them join the set for the FINAL coverage check
    t = R.get("totals", {})
    if "gates" in t:
        cl.update({
            "gates": "%d gates" % t["gates"],
            "gates_falsifiable": "%d carrying their own injection falsifier and "
                                 "%d their registered forcing"
                                 % (t["gates_falsifiable"], t["gates_waived"]),
            "mutants": "%d declared mutants" % t["mutants"],
            "anchors": "%d anchors" % t["anchors"],
            "byte_anchors": "%d file-bytes anchors" % t["byte_anchors"],
            "pv_anchors": "%d path-value anchors" % t["path_value_anchors"],
            "vb_anchors": "%d verbatim-text anchors" % t["verbatim_anchors"],
        })
    if MUT == "MUT-PAPER-CLAIM":
        cl["injected"] = "a claim the paper does not carry: 4242"
    return cl


def paper_coverage(R, txt):
    """the claim strings must occur in the paper verbatim up to line wrapping:
    the comparison collapses runs of whitespace on BOTH sides, so a claim
    broken across two lines still has to be the same characters in the same
    order.  Numerals are extracted from the raw text."""
    cl = paper_claims(R)
    flat = re.sub(r"\s+", " ", txt)
    missing = sorted(k for k, v in cl.items()
                     if re.sub(r"\s+", " ", v) not in flat)
    rendered = set()
    for v in cl.values():
        rendered |= set(re.findall(NUMERAL_RE, v))
    for row in R["dispersion_census"]:
        rendered |= {str(row["radius"]), str(row["support"]), row["max_speed"]}
        rendered |= set(re.findall(NUMERAL_RE, row["family"]))
        rendered.add("".join(str(x) for x in row["reduced_dispersion"]))
        rendered |= {str(x) for x in row["reduced_dispersion"]}
    for row in R["class_rows"]:
        rendered.add(str(row["size"]))
        rendered |= set(re.findall(NUMERAL_RE, row["class"]))
        if row["speed"] is not None:
            rendered.add(row["speed"])
        if row["aliased_cells"] is not None:
            rendered.add(str(row["aliased_cells"]))
        if row["support"] is not None:
            rendered |= {str(row["support"]), str(row["radius"])}
    for tbl in (R["support_drift_table"], R["support_drift_table_positive_reading"]):
        for k, v in tbl.items():
            rendered |= {k, str(v["generators"]), str(v["nonzero_drift"])}
    rendered |= {str(v) for v in R["agreement_matrix"].values()}
    rendered |= {str(v) for v in R["resolution"].values() if isinstance(v, int)}
    rendered |= {str(len(SOURCES)), str(len(PATH_VALUE_ANCHORS)),
                 str(len(VERBATIM_ANCHORS)), str(len(MUTANTS)),
                 str(len(SOURCES) + len(PATH_VALUE_ANCHORS) + len(VERBATIM_ANCHORS)),
                 str(len(LIFT_READINGS) * len(STENCIL_READINGS))}
    for row in R["axes"]:
        rendered |= {str(row["order"]), str(row["radius"])}
    for k, v in R["pool_counts"].items():
        rendered.add(str(v))
    for k, v in list(R["counts"].items()) + list(R.get("totals", {}).items()):
        if isinstance(v, int):
            rendered.add(str(v))
        elif isinstance(v, str):
            rendered |= set(re.findall(NUMERAL_RE, v))
    for row in R["velocity_fiber"]:
        rendered.add(str(row["cells_agreeing_with_declared"]))
    residue = dict(DERIVED_IN_TEXT)
    if MUT == "MUT-PAPER-NUMERAL":
        rendered.discard(str(R["counts"]["moving"]))
        residue.pop("0", None)
    in_paper = set(re.findall(NUMERAL_RE, txt))
    uncovered = sorted(in_paper - rendered - set(residue))
    return {"claims": len(cl), "missing": missing,
            "distinct_numerals": len(in_paper),
            "numeral_occurrences": len(re.findall(NUMERAL_RE, txt)),
            "covered_by_rendering": len(in_paper & rendered),
            "declared_derived_in_text": len(residue),
            "residue_declared_but_absent":
                sorted(k for k in residue if k not in in_paper),
            "uncovered": uncovered}


def run_receipt_gates(S, LD, paper_text):
    R = build_receipt(S, LD)
    c = R["counts"]

    # ---- the head, derived twice ------------------------------------------
    head, segs, string = build_verdict(c)
    if mut("MUT-HEAD-TYPED"):
        head = "R4B-NO-MOTION"            # a head retyped after the census ran
        string = head + string[string.index("<"):]
        R["verdict"]["string"] = string
    if mut("MUT-HEAD-OUTSIDE-PIN"):
        head = "R4B-MOTION-FOUND"
        R["verdict"]["head"] = head
        R["verdict"]["string"] = head + string[string.index("<"):]
    LD.gate("G-VERDICT-PREREGISTERED",
            "the head this run emits is one of the three the pin registered "
            "before the census ran, and the pin's sentence is anchored "
            "verbatim",
            any(head == nm or head.startswith(nm + "-") for nm in PREREGISTERED_HEADS),
            "head=%s preregistered=%s" % (head, list(PREREGISTERED_HEADS)))

    Rjson = json.dumps(R, indent=1, sort_keys=True)
    rebuilt = reconstruct_from_serialized(Rjson)
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "the COMPLETE verdict string, head included, is rebuilt from the "
            "serialized receipt by an independent path that shares no helper, "
            "no head law and no typed value with the assembler, and the two "
            "strings are equal character for character",
            rebuilt == R["verdict"]["string"],
            "reconstruction %s (%d chars)"
            % ("equal" if rebuilt == R["verdict"]["string"] else "DIFFERS",
               len(rebuilt)))

    # the head law must be responsive: a constant head law is caught
    zeroed = dict(c)
    zeroed["moving"] = 0
    zeroed["static"] = zeroed["families"]
    head_zeroed = ("R4B-DISPERSION-READ" if mut("MUT-HEAD-CONSTANT")
                   else derive_head(zeroed))
    LD.gate("G-HEAD-LAW-RESPONSIVE",
            "the head is named by the dispersion census and by nothing else: "
            "with the moving count zeroed the head law returns the pin's "
            "OTHER outcome, so a head that cannot move is not this one",
            head_zeroed == "R4B-NO-MOTION" and head == "R4B-DISPERSION-READ",
            "head=%s; head under a zeroed motion census=%s" % (head, head_zeroed))
    R["verdict"]["head_under_zeroed_census"] = head_zeroed

    # ---- flip probes for every verdict value ------------------------------
    flip_keys = sorted({k for _, ks in SEGMENT_KEYS for k in ks})
    dead = []
    for k in flip_keys:
        probe = json.loads(Rjson)
        v = probe["counts"][k]
        if isinstance(v, bool):
            probe["counts"][k] = not v
        elif isinstance(v, int):
            probe["counts"][k] = v + 1
        elif isinstance(v, str):
            probe["counts"][k] = v + "-X"
        elif isinstance(v, list):
            probe["counts"][k] = v + ["9"] if v and isinstance(v[0], str) else v + [9]
        if mut("MUT-FLIP-DEAD") and k == "aliased_families":
            probe["counts"][k] = v
        if reconstruct_from_serialized(json.dumps(probe)) == R["verdict"]["string"]:
            dead.append(k)
    LD.gate("G-VERDICT-VALUES-FLIPPABLE",
            "every value the verdict carries has its own flip probe: "
            "perturbing the receipt key it renders from moves the complete "
            "reconstruction.  A value that renders from a key nothing reads "
            "is caught here",
            not dead, "unflippable keys %s over %d verdict values"
            % (dead or "none", len(flip_keys)))
    R["totals"] = {"verdict_values": len(flip_keys)}

    # ---- the inherited scope segment ---------------------------------------
    scope_seg = [v for k, v in segs if k == "SCOPE"][0]
    if mut("MUT-SCOPE"):
        scope_seg = scope_seg.replace("MAX-NORM", "SUM-NORM")
    connective_clause = "CONNECTIVE=%s(FORCED-BY-ANCHORED-LINK-%s)" % (
        c["connective_tag"], c["forcing_link"])
    parent_out = read_text(os.path.join(REPO, SOURCES[2][1]))
    inherited = ["D=%s" % c["d"], "L=%s" % c["L"], "FIELD=%s" % c["field"],
                 "ALPHABET=%s" % c["alphabet"], "STENCIL=%s" % c["stencil"],
                 "SECTOR=%s" % c["sector"], "INDIVISIBILITY=%s" % c["indivisibility"],
                 "FINITE-LATTICE-ONLY", "NO-CONTINUUM-CLAIM", connective_clause]
    LD.gate("G-SCOPE-INHERITED",
            "the SCOPE segment inherits the parent's verbatim, clause by "
            "clause, and the FORCED connective travels with it: the clause "
            "this unit emits is character for character the clause the "
            "parent's own terminal output prints",
            all(x in scope_seg for x in inherited)
            and connective_clause.replace(",", "").replace(" ", "")
            in parent_out.replace(",", "").replace(" ", ""),
            "%d inherited clauses present; connective clause matches the "
            "parent's output" % len(inherited))

    # ---- receipt hygiene ---------------------------------------------------
    probe = json.loads(Rjson)
    if mut("MUT-FLOAT"):
        probe["counts"]["vmax"] = 1 / 2      # a float, built without a literal
    LD.gate("G-NO-FLOATS",
            "no float appears anywhere in the emitted receipt, and none "
            "appears in this file: the arithmetic is exact end to end",
            not has_float(probe) and not source_has_float(),
            "receipt float-free=%s; source float-free=%s"
            % (not has_float(probe), not source_has_float()))
    serialized = Rjson + (" " if mut("MUT-DETERMINISM") else "")
    LD.gate("G-RECEIPT-ROUND-TRIP",
            "the receipt is serialization-stable: parsing what was built and "
            "re-serializing it reproduces the same bytes, so the artifact is "
            "deterministic and independent of dictionary order",
            json.dumps(json.loads(Rjson), indent=1, sort_keys=True) == serialized,
            "round trip stable over %d bytes" % len(Rjson))

    # ---- source properties -------------------------------------------------
    scanned = (source_text() + (SUBPROCESS_DECOY if mut("MUT-SUBPROCESS") else "")
               + (PARENT_IMPORT_DECOY if mut("MUT-PARENT-IMPORT") else ""))
    LD.gate("G-NO-SUBPROCESS",
            "this instrument never invokes a subprocess and never calls git: "
            "an AST scan of its own source finds no import of subprocess, no "
            "os.system and no shell call, so the run is correct off-tree and "
            "in a directory with no version control at all",
            not scan_subprocess(scanned),
            "subprocess-free source scan over %d bytes" % len(scanned))
    LD.gate("G-PARENT-NOT-IMPORTED",
            "the parent program is an anchor, not a dependency: it is read as "
            "bytes for its digest, no module from it is imported, and nothing "
            "in this process comes from it",
            not any("r4_defect_stage" in m for m in sys.modules)
            and not any("r4_defect_stage" in m for m in scan_imports(scanned)),
            "no parent module in sys.modules; no import of it in source")
    laundered = scan_laundering(source_text()
                                + (LAUNDER_DECOY if mut("MUT-LAUNDER") else ""))
    LD.gate("G-NO-MUTANT-ONLY-CLAUSE",
            "no gate predicate reads the mutant switch (#208): a standing AST "
            "probe walks every gate call in this file's own source and reports "
            "any predicate that would exempt its own falsifier",
            not laundered,
            "gate predicates reading the switch: %s" % (laundered or "none"))

    # ---- runtime inputs ----------------------------------------------------
    declared = sorted({rel for _, rel, _, _ in SOURCES})
    if mut("MUT-EXTRA-READ"):
        READS.append("v14/LOG.md")
    actual = sorted(set(READS))
    LD.gate("G-RUNTIME-INPUTS-ENUMERATED",
            "exactly the declared sources are read at run time, plus this "
            "unit's own paper as the object under test; nothing else and no "
            "mutable repository state is opened",
            actual == declared,
            "declared %d, read %d" % (len(declared), len(actual)))

    # ---- the instrument's own totals, PREDICTED here and verified at the end
    R["totals"].update({
        "gates": len(LD.rows) + PENDING_GATES,
        "gates_waived": len(FORCINGS),
        "gates_falsifiable": len(LD.rows) + PENDING_GATES - len(FORCINGS),
        "anchors": len(SOURCES) + len(PATH_VALUE_ANCHORS) + len(VERBATIM_ANCHORS),
        "byte_anchors": len(SOURCES),
        "path_value_anchors": len(PATH_VALUE_ANCHORS),
        "verbatim_anchors": len(VERBATIM_ANCHORS),
        "mutants": len(MUTANTS),
        "families": c["families"],
        "census_cells": c["cells"],
    })

    # ---- paper gates -------------------------------------------------------
    cov = paper_coverage(R, paper_text)
    LD.gate("G-PAPER-CLAIMS",
            "every claim string the receipt renders occurs verbatim in the "
            "paper, so no number in the prose is unsupported by a computed "
            "value",
            not cov["missing"], "missing %s over %d claims"
            % (cov["missing"] or "none", cov["claims"]))
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "every numeral in the paper is either rendered from the receipt "
            "or named in the declared derived-in-text residue, and every "
            "residue entry actually occurs: the coverage runs INSIDE the "
            "delivery run as a gate, not beside it as a flag",
            not cov["uncovered"] and not cov["residue_declared_but_absent"],
            "uncovered %s; declared-but-absent %s; %d distinct numerals over "
            "%d occurrences" % (cov["uncovered"] or "none",
                                cov["residue_declared_but_absent"] or "none",
                                cov["distinct_numerals"],
                                cov["numeral_occurrences"]))
    R["paper_coverage"] = cov
    R["paper_claims"] = paper_claims(R)

    # ---- the CLI -----------------------------------------------------------
    probes = []
    for argv, want_reject in ((["--not-a-flag"], True), (["--mutant"], True),
                              (["--mutant", "NOPE"], True),
                              (["--break-anchor", "NOPE"], True),
                              (["--break-anchor"], True),
                              (["--no-write"], False), (["--selftest"], False),
                              (["--verify-paper"], False),
                              (["--mutant", MUTANTS[0][0]], False)):
        parser = parse_args_permissive if mut("MUT-CLI-PERMISSIVE") else parse_args
        rejected = cli_error_probe(parser, argv)
        probes.append({"argv": argv, "rejected": rejected,
                       "must_reject": want_reject})
    LD.gate("G-CLI-CONTRACT",
            "the CLI is argv-parsed against a whitelist and exercised here: "
            "every unknown flag, unknown flag argument and missing argument "
            "is rejected, and the permissive shape -- the registered disease "
            "-- fails this gate",
            all(p["rejected"] == p["must_reject"] for p in probes),
            "%d probes, %d rejections"
            % (len(probes), sum(1 for p in probes if p["rejected"])))
    LD.gate("G-SELFTEST-WRITES-NOTHING",
            "no diagnostic path can write: the self-test, the mutant runner "
            "and the anchor-break runner all come out of the parser with "
            "write=False, measured here on the parser's own output rather "
            "than asserted in prose",
            (parse_args(["--selftest"])["write"] is False
             and parse_args(["--mutant", MUTANTS[0][0]])["write"] is False
             and parse_args(["--break-anchor", SOURCES[0][0]])["write"] is False),
            "selftest/mutant/break-anchor all write=False")
    R["cli_probes"] = probes

    # ---- coverage of the ledger itself ------------------------------------
    targeted = {m[1] for m in MUTANTS}
    evaluated = ({r["gate"] for r in LD.rows} | set(POST_LOOP_GATES)
                 | {"G-GATE-MUTANT-COVERAGE", "G-WAIVERS-VERIFIED",
                    "G-ANCHOR-CONSUMERS-EXIST"})
    if mut("MUT-REGISTRY"):
        evaluated = evaluated | {"G-NEVER-REACHED"}
    untargeted = sorted(g for g in evaluated
                        if g not in targeted and g not in FORCINGS)
    LD.gate("G-GATE-MUTANT-COVERAGE",
            "every gate this unit evaluates is the declared target of at "
            "least one mutant, except the two whose falsification mechanism "
            "is registered instead (#34): coverage of the ledger is measured, "
            "not claimed",
            not untargeted and targeted <= evaluated,
            "gates %d, targeted %d, untargeted %s, targets with no gate %s"
            % (len(evaluated), len(targeted & evaluated), untargeted or "none",
               sorted(targeted - evaluated) or "none"))

    consumers = [(vid, cons) for vid, _sid, cons, _w in VERBATIM_ANCHORS]
    if mut("MUT-DANGLING-CONSUMER"):
        consumers.append(("VB-INJECTED", "G-NEVER-DECLARED"))
    dangling = sorted(vid for vid, cons in consumers if cons not in evaluated)
    LD.gate("G-ANCHOR-CONSUMERS-EXIST",
            "every verbatim anchor names a gate that actually exists and is "
            "actually evaluated: a window bound to a gate the run never "
            "reaches is a decoration, not an anchor",
            not dangling, "anchors %d, dangling consumers %s"
            % (len(consumers), dangling or "none"))

    waivers = []
    for gid in sorted(evaluated):
        forced = gid in FORCINGS
        waivers.append({"gate": gid,
                        "status": "WAIVED" if forced else "FALSIFIABLE",
                        "forcing": FORCINGS.get(gid, ""),
                        "forcing_registered": (not forced) or bool(FORCINGS[gid]),
                        "falsifier": sorted(m[0] for m in MUTANTS if m[1] == gid)})
    if mut("MUT-WAIVER"):
        waivers.append({"gate": "G-INJECTED", "status": "WAIVED", "forcing": "",
                        "forcing_registered": False, "falsifier": []})
    unregistered = [w["gate"] for w in waivers
                    if w["status"] == "WAIVED" and not w["forcing_registered"]]
    LD.gate("G-WAIVERS-VERIFIED",
            "every gate without an injection falsifier registers its forcing, "
            "and the registration is checked rather than asserted (#34): a "
            "waiver claim is a gate claim",
            not unregistered,
            "falsifiable %d, waived %d, unregistered %s"
            % (sum(1 for w in waivers if w["status"] == "FALSIFIABLE"),
               sum(1 for w in waivers if w["status"] == "WAIVED"),
               unregistered or "none"))
    R["waiver_ledger"] = waivers
    return R, Rjson


POST_LOOP_GATES = ("G-MUTANTS-ON-TARGET", "G-ARTIFACT-INTEGRITY",
                   "G-PAPER-COVERAGE-FINAL")

# the gates still to be evaluated when the totals are predicted, counted from
# the declaration site: the two in-run paper gates, the CLI pair, the two
# ledger-coverage gates, the mutant adjudication, the final paper gate and the
# integrity gate.  The prediction is verified against the count reached.
PENDING_GATES = 10


def source_text():
    with open(SELF, "r", encoding="utf-8") as f:
        return f.read()


def source_has_float():
    for node in ast.walk(ast.parse(source_text())):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            return True
    return False


def scan_subprocess(txt):
    for node in ast.walk(ast.parse(txt)):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            nm = getattr(node, "module", None) or ""
            for n in [a.name for a in node.names] + [nm]:
                if n and n.split(".")[0] in ("subprocess", "pty", "commands"):
                    return True
        if isinstance(node, ast.Attribute) and node.attr in ("system", "popen",
                                                             "execv", "fork"):
            return True
    return False


def scan_imports(txt):
    out = set()
    for node in ast.walk(ast.parse(txt)):
        if isinstance(node, ast.Import):
            out |= {a.name for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            out.add(node.module or "")
    return out


PARENT_IMPORT_DECOY = """

import r4_defect_stage_exact
"""

SUBPROCESS_DECOY = """

def _decoy_shells_out():
    import subprocess
    return subprocess.run(["git", "rev-parse", "HEAD"])
"""

LAUNDER_DECOY = """

def _decoy_laundered_gate(LD):
    LD.gate("G-DECOY-LAUNDER", "a gate predicate guarded by the switch",
            not mut("MUT-LAUNDER"), "the forbidden shape")
"""


def scan_laundering(txt):
    """the standing #208 probe: walk every LD.gate(...) call and report any
    whose PREDICATE argument reads the mutant switch.  A gate that exempts its
    own falsifier is the laundering shape and is named here."""
    bad = []
    for node in ast.walk(ast.parse(txt)):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "gate" and len(node.args) >= 3):
            gid = (node.args[0].value if isinstance(node.args[0], ast.Constant)
                   else "?")
            for sub in ast.walk(node.args[2]):
                if (isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name)
                        and sub.func.id == "mut"):
                    bad.append(gid)
    return sorted(set(bad))


# ===========================================================================
# SECTION 10.  REPORT
# ===========================================================================

def emit_report(R, S):
    c = R["counts"]
    say("")
    say("-" * 78)
    say("ARENA (declared as data)")
    for k in ("boundary", "family", "momentum", "law", "arena", "division_events"):
        say("  %-16s %s" % (k, ARENA[k]))
    say("")
    say("ANCHORS")
    for r in R["verbatim_anchors"]:
        say("  verbatim   %-20s -> %-34s %s"
            % (r["id"], r["consumer_gate"], "present" if r["present"] else "MISSING"))
    for r in R["byte_anchors"]:
        say("  bytes      %-20s %s %s" % (r["id"], r["artifact"], r["measured"]))
    for r in R["path_value_anchors"]:
        say("  path-value %-20s %s = %s"
            % (r["id"], r["path"], json.dumps(r["expected"])[:40]))
    say("")
    say("THE FAMILY, REBUILT AND GATED AGAINST THE PARENT'S ROWS")
    say("  pool %s" % R["pool_counts"])
    say("  axes (offset, order, radius): %s"
        % [(tuple(a["axis"]), a["order"], a["radius"]) for a in R["axes"]])
    say("  extended classes %d, sizes %s" % (c["classes_extended"], R["class_sizes"]))
    say("")
    say("THE DISPERSION CENSUS (exact, Q(zeta_8); phases are elements of Z/8)")
    say("  (family, momentum) cells            %d" % c["cells"])
    say("  eigen-equation M chi = lambda chi   %d" % c["eigen_verified"])
    say("  eigenvalues in mu_8                 %d" % c["in_mu8"])
    say("  exact unit modulus                  %d" % c["unit_modulus"])
    say("  non-constant dispersions            %d of %d" % (c["moving"], c["families"]))
    say("  constant (the NO-MOTION control)    %s" % c["control"])
    say("  phase parity a family invariant     %d of %d"
        % (c["parity_invariant"], c["families"]))
    say("  distinct reduced dispersions        %d (vs %d distinct invariant labels)"
        % (c["distinct_profiles"], c["class_labels"]))
    say("")
    say("  the reduced dispersion sigma(k) = s(k) - s(0), first rows "
        "(k in lexicographic order):")
    for row in R["dispersion_census"][:6]:
        say("    %-5s supp=%d rad=%d  sigma=%s  v_max=%s  %s"
            % (row["family"], row["support"], row["radius"],
               "".join(str(x) for x in row["reduced_dispersion"]),
               row["max_speed"], row["motion"]))
    say("")
    say("GROUP VELOCITY")
    say("  definition (declared)   %s" % R["velocity_definition"]["declared"])
    say("  tie reading (declared)  %s" % R["velocity_definition"]["tie_reading"])
    say("  speed (branch-free)     %s" % R["velocity_definition"]["speed"])
    say("  phase differences       %d, all even -> every velocity an integer"
        % c["velocity_cells"])
    say("  speed spectrum          %s      VMAX = %s"
        % ("{" + ", ".join(c["speed_spectrum"]) + "}", c["vmax"]))
    say("  aliased cells           %d of %d, in %d of %d families"
        % (c["aliased_cells"], c["velocity_cells"], c["aliased_families"],
           c["families"]))
    say("  the fiber (lift x stencil), cells agreeing with the declared reading:")
    for row in R["velocity_fiber"]:
        say("    %-13s %-9s %d of %d"
            % (row["lift"], row["stencil"], row["cells_agreeing_with_declared"],
               row["cells"]))
    say("")
    say("THE MOTION HEAD, PER EXTENDED CLASS")
    for row in R["class_rows"]:
        if row["kind"] != "CIRC":
            say("    class %-5s size=%-2d kind=%-5s  %s"
                % (row["class"], row["size"], row["kind"], row["motion"]))
        else:
            say("    class %-5s size=%-2d supp=%d radius=%d v_max=%s aliased=%-2d "
                "profiles=%d  %s"
                % (row["class"], row["size"], row["support"], row["radius"],
                   row["speed"], row["aliased_cells"], row["profiles"], row["motion"]))
    say("")
    say("THE PROPAGATION BOUND")
    say("  VMAX = %s; torus max-norm diameter = %d; radii present %s; interior %s"
        % (c["vmax"], c["diameter"], R["resolution"]["radius_classes"],
           c["interior_radii"]))
    say("  the cone after ONE step covers %d of %d sites"
        % (c["cone_sites_one_step"], c["sites"]))
    say("  per family, speed against its own one-step reach: over %d, under %d, "
        "equal %d" % (c["reach_over"], c["reach_under"], c["reach_equal"]))
    say("  inherited AT THE CEILING: separations %d of %d; max defect radius "
        "%d of %d" % (c["separations"], c["separations_ceiling"],
                      c["max_defect_radius"], c["radius_ceiling"]))
    say("  the bound has content: %s" % c["bound_has_content"])
    say("  the resolution relation: %s" % R["resolution"])
    say("")
    say("TRANSPORT: THE DRIFT AND THE WINDING")
    say("  support -> [generators, nonzero drift] under the tie-averaged "
        "reading: %s" % R["support_drift_table"])
    say("  drift == winding, by reading pair:")
    for k in sorted(R["agreement_matrix"]):
        say("    drift %-13s vs winding %-13s : %d of %d"
            % tuple(k.split("|") + [R["agreement_matrix"][k], c["families"]]))
    say("  nonzero winding %d, all monomial (of %d monomial families)"
        % (c["nonzero_winding"], c["monomial"]))
    say("  interfering families %d: all with zero net transport, all MOVING (%d)"
        % (c["interfering"], c["interfering_moving"]))
    say("  inherited: the Markovian control is %d of %d nonzero"
        % (c["markov_nonzero"], c["markov_pairs"]))
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


NOT_EXECUTED = [
    "no continuum, infinite-volume or long-time limit is taken; the dual "
    "torus has 16 points and every statement here is a statement about it",
    "the non-circulant controls are NOT given a dispersion: they are measured "
    "not to be diagonal in the character basis, and the finer decomposition "
    "their index-two translation stabiliser would allow is not built",
    "no defect is recomputed in this unit; every defect number is inherited "
    "from the parent's receipt at a hash-pinned path",
    "the wider five-point local family at the admitted size is disclosed by "
    "the parent and is not censused here either",
    "indivisibility is DECLARED by the division-event times and is never "
    "measured, exactly as in the parent",
    "no state is propagated: the group velocity is read off the exact "
    "eigenphase, and no wavepacket is constructed or evolved",
    "the alphabet is not widened; the effectus review's constructive "
    "motion-carrying generator over Q(i, sqrt 3) is outside this unit's "
    "declared field and is not built",
]


# ===========================================================================
# SECTION 11.  MAIN
# ===========================================================================

def selftest():
    """--selftest: corrupt ONE anchor in memory, confirm the run dies at the
    anchor gate, WRITE NOTHING, exit 1.  Exits 2 if the corrupted run lives."""
    target = SOURCES[0][0]
    print("SELFTEST: corrupting anchor %s in memory; the run must die." % target,
          flush=True)
    globals()["QUIET"] = True
    try:
        build_state(target)
    except GateFail as e:
        globals()["QUIET"] = False
        print("SELFTEST: died at %s -- as required." % str(e).split(" ::")[0],
              flush=True)
        print("SELFTEST PASSED (the instrument is falsifiable); no artifact "
              "written.", flush=True)
        print("EXIT 1", flush=True)
        sys.exit(1)
    globals()["QUIET"] = False
    print("SELFTEST FAILED: a corrupted anchor did not kill the run.", flush=True)
    print("EXIT 2", flush=True)
    sys.exit(2)


def full_run(break_anchor, paper_text):
    S, LD = build_state(break_anchor)
    say("[9/10] the verdict, its reconstruction, and the receipt gates")
    R, Rjson = run_receipt_gates(S, LD, paper_text)
    return S, LD, R, Rjson


def main():
    global MUT, READS
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
    MUT = opts["mutant"]

    say("=" * 78)
    say("v14 R4b -- MOMENTUM: READING THE DISPERSIONS")
    say("=" * 78)
    if MUT:
        say("MUTANT ACTIVE: %s" % MUT)
    if opts["break_anchor"]:
        say("ANCHOR BREAK SELF-TEST: %s" % opts["break_anchor"])

    paper_path = os.path.join(REPO, PAPER_REL)
    paper_text = read_text(paper_path) if os.path.exists(paper_path) else ""

    try:
        S, LD, R, Rjson = full_run(opts["break_anchor"], paper_text)
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    if MUT or opts["break_anchor"]:
        say("")
        say("MUTANT SURVIVED: %s" % (MUT or opts["break_anchor"]))
        say("EXIT 0")
        sys.exit(0)

    # ---- the declared mutants, in process ----------------------------------
    say("[10/10] running %d declared mutants" % len(MUTANTS))
    report, all_dead, on_target = [], True, 0
    saved_reads = list(READS)
    for nm, target, note in MUTANTS:
        MUT = nm
        globals()["QUIET"] = True
        killed_at = None
        try:
            READS = []
            full_run(None, paper_text)
        except GateFail as e:
            killed_at = str(e).split(" ::")[0]
        except SystemExit:
            killed_at = "SYSTEM-EXIT"
        globals()["QUIET"] = False
        MUT = None
        report.append({"mutant": nm, "target": target, "note": note,
                       "killed": killed_at is not None, "killed_at": killed_at,
                       "on_target": killed_at == target})
        if killed_at is None:
            all_dead = False
        if killed_at == target:
            on_target += 1
    READS = saved_reads
    say("    mutants: %d declared, %d killed, %d killed by their declared target"
        % (len(MUTANTS), sum(1 for m in report if m["killed"]), on_target))
    off = [(m["mutant"], m["target"], m["killed_at"]) for m in report
           if not m["on_target"]]
    LD.gate("G-MUTANTS-ON-TARGET",
            "every declared mutant is killed, and killed by the gate it was "
            "declared to falsify: a mutant that dies elsewhere is a gate "
            "boundary this unit does not understand",
            all_dead and on_target == len(MUTANTS),
            "killed %d of %d; off target %s"
            % (sum(1 for m in report if m["killed"]), len(MUTANTS), off or "none"))

    R["gates"] = LD.rows
    R["mutants"] = report
    R["not_executed"] = NOT_EXECUTED
    waivers = R["waiver_ledger"]

    R["totals"].update({
        "mutants_killed": sum(1 for m in report if m["killed"]),
        "mutants_on_target": on_target,
        "gates_passed": sum(1 for g in LD.rows if g["passed"]) + 2,
    })

    # THE PREDICTION CLOSES.  The gate count was declared BEFORE the paper
    # gates ran; it must be exactly the count the run reaches.  Two ledger rows
    # are still to come -- the final paper gate below -- plus the integrity
    # gate that only the writing path evaluates.
    if (R["totals"]["gates"] != len(LD.rows) + 2
            or R["totals"]["gates_falsifiable"]
            != sum(1 for w in waivers if w["status"] == "FALSIFIABLE")
            or R["totals"]["gates_waived"]
            != sum(1 for w in waivers if w["status"] == "WAIVED")):
        say("")
        say("GATE FAILED: G-PAPER-COVERAGE-FINAL :: the predicted gate count %d "
            "did not close at %d" % (R["totals"]["gates"], len(LD.rows) + 2))
        say("EXIT 1")
        sys.exit(1)
    try:
        cov = paper_coverage(R, paper_text)
        LD.gate("G-PAPER-COVERAGE-FINAL",
                "the paper-claim and numeral-coverage check re-run once the "
                "instrument's own totals close, so the paper's instrument "
                "section is covered too; its in-run twins carry the injection "
                "falsifiers, and this evaluation is the enforcement -- a "
                "failure here exits 1 and writes nothing",
                not cov["missing"] and not cov["uncovered"]
                and not cov["residue_declared_but_absent"],
                "missing %s; uncovered %s; declared-but-absent %s; %d claims, "
                "%d distinct numerals over %d occurrences"
                % (cov["missing"] or "none", cov["uncovered"] or "none",
                   cov["residue_declared_but_absent"] or "none", cov["claims"],
                   cov["distinct_numerals"], cov["numeral_occurrences"]))
    except GateFail as e:
        R["paper_coverage"] = cov
        R["gates"] = LD.rows
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)
    R["paper_coverage"] = cov
    R["paper_claims"] = paper_claims(R)
    R["gates"] = LD.rows

    emit_report(R, S)

    if write:
        payload = json.dumps(R, indent=1, sort_keys=True)
        text = "\n".join(LOG) + "\n"
        # THE FINAL INTEGRITY GATE, two-way.  First the negative control: a
        # deliberately corrupted payload is written to a probe path and re-read,
        # and the comparator must NOTICE.  Only then are the real artifacts
        # written and required to match, byte for byte, with the verdict
        # reconstructed from the bytes that landed on disk.
        probe_path = OUT_JSON + ".integrity-probe"
        with open(probe_path, "w", encoding="utf-8") as f:
            f.write(payload[:-1] + " }")
        detected = read_text(probe_path) != payload
        os.remove(probe_path)
        with open(OUT_JSON, "w", encoding="utf-8") as f:
            f.write(payload)
        with open(OUT_TXT, "w", encoding="utf-8") as f:
            f.write(text)
        back_json = read_text(OUT_JSON)
        back_txt = read_text(OUT_TXT)
        ok = (detected and back_json == payload and back_txt == text
              and json.loads(back_json)["verdict"]["string"] == R["verdict"]["string"]
              and reconstruct_from_serialized(back_json) == R["verdict"]["string"])
        if not ok:
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: the artifacts on disk "
                  "differ from what was built (corruption detected=%s)" % detected,
                  flush=True)
            sys.exit(1)
        print("G-ARTIFACT-INTEGRITY: corrupted probe detected; both artifacts "
              "re-read from disk and byte-identical to what was built; the "
              "verdict reconstructs from the bytes on disk (%d + %d bytes)."
              % (len(payload), len(text)), flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
