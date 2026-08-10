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
        RUNS THE #20 INSTRUMENT AGAINST PATH (this unit's paper by default):
        the whole derivation is rebuilt and the paper gates -- claim
        rendering, numeral coverage and claim POLARITY -- are evaluated with
        PATH as the object under test.  Exits 1 on any drift, 0 on a clean
        paper, and 2 if PATH does not exist.  Writes nothing.

    Any other argument, any unknown flag argument, any missing flag argument
    and any --verify-paper PATH that does not exist exits 2.  No flag is
    mutant-only, and no flag is a no-op.

THE GATE-TO-DISK SEAL (RUNBOOK 14 addendum, this unit's engraving).  A gate
that fires on an object which is still mutable when the artifact is built has
not gated the artifact.  Every published object is DIGESTED AT THE MOMENT ITS
GATE PASSES (`SEAL`); the payload may only be sealed if every earlier seal
still verifies; the artifacts are written FROM the sealed payload; and the
terminal integrity gate compares the BYTES ON DISK against the gate-time seal.
A re-derivation from disk is not an integrity check -- it confirms corruption.

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
    ("VB-WIDENED-GENERATOR", "A-REV-EFFECTUS", "G-ARENA-ARTIFACT-WITNESS",
     "> c_a = 1/2, c₋ₐ = i·√3/2, c₀ = 0 →\n"
     "> **unitary** (all lags verified), **support 2** (non-monomial),\n"
     "> **⟨Δx⟩ = −1/2 ≠ 0** (motion)"),
]

# --- the frozen digest of every verbatim window (#62) -----------------------
# A window is an ANCHOR only if its bytes are pinned.  Bare substring presence
# admits a window truncated to a decoration; these digests do not.
WINDOW_DIGESTS = {
    "VB-DISPERSION-57": "508f67433486",
    "VB-DRIFT-TABLE": "d8c389ecdf60",
    "VB-K3-NO-MOMENTUM": "ed819ea09c6a",
    "VB-K3-SYMBOL": "6c95fefc3a11",
    "VB-PROPAGATOR": "ab21344b844a",
    "VB-CEILINGS": "aac35ce16ca7",
    "VB-CONNECTIVE": "37bb69c658cb",
    "VB-SUCCESSOR": "9ffa39e20ca3",
    "VB-ALPHABET": "d21521ca4f99",
    "VB-UNITARITY": "4ba66899d14a",
    "VB-GENERATOR": "83ceeb0b0e63",
    "VB-PIN-OUTCOMES": "bc3ce14bef66",
    "VB-PIN-LATTICE": "581f8f6845e1",
    "VB-WIDENED-GENERATOR": "85f986613574",
}

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
           "the group velocity is a discrete derivative of the phase on the dual "
           "torus whose TWO COORDINATES ARE DATA: the difference STENCIL "
           "(forward | backward | central), FORCED to {forward, backward} by the "
           "declared monomial normalisation, and the antipodal-TIE LIFT "
           "(tie-averaged | positive | negative), SELECTED to tie-averaged in "
           "this arena by the drift = winding identity.  The residual fiber is 2 "
           "-- forward and backward -- measured inert on every quantity this "
           "unit reports and differing only in the cell-level labelling of "
           "signed velocity",
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
# the stencil coordinate the declared monomial normalisation admits: a monomial
# shift by an offset o must have velocity o.  Measured, not asserted.
STENCIL_FORCED = ("FORWARD", "BACKWARD")
# the even sizes at which the VMAX = diameter theorem is exercised
STRUCTURAL_SIZES = (4, 6, 8, 10, 12)

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


def charpoly(a):
    """the characteristic polynomial of MULTIPLICATION BY a on the Q-basis
    (1, z, z^2, z^3), exactly, by Faddeev--LeVerrier.  Returns the four
    coefficients (c1, c2, c3, c4) of x^4 + c1 x^3 + c2 x^2 + c3 x + c4.  This
    is the load-bearing step of the Kronecker argument: a unit-modulus element
    is a root of unity only once it is known to be an ALGEBRAIC INTEGER, and
    that is exactly the statement that these four rationals are integers.
    ((3+4i)/5 has all conjugates of modulus one and is not a root of unity.)"""
    A = [[a[0], -a[3], -a[2], -a[1]],
         [a[1], a[0], -a[3], -a[2]],
         [a[2], a[1], a[0], -a[3]],
         [a[3], a[2], a[1], a[0]]]

    def mm(X, Y):
        return [[sum(X[i][t] * Y[t][j] for t in range(4)) for j in range(4)]
                for i in range(4)]

    cs, Mk = [], A
    for k in range(1, 5):
        ck = Fraction(-sum(Mk[i][i] for i in range(4)), k)
        cs.append(ck)
        if k < 4:
            Mk = mm(A, [[Mk[i][j] + (ck if i == j else Q0) for j in range(4)]
                        for i in range(4)])
    return tuple(cs)


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


# the only THREE gates with no declared mutant: all three are evaluated OUTSIDE
# the in-process mutant runner, so a mutant could not reach them.  Each
# registers the mechanism that falsifies it instead (#34).
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
                            "to be detected -- and its reference value is the "
                            "GATE-TIME SEAL, whose in-run half G-SEAL-COMPLETE "
                            "carries the injection falsifier MUT-SEAL-BROKEN",
    "G-PAPER-COVERAGE-FINAL": "evaluated after the mutant sweep closes the "
                              "instrument's totals, so no in-process mutant "
                              "can reach it; the claims that render from the "
                              "CLOSED totals (the mutant sweep's own result) "
                              "exist only at this evaluation, and its in-run "
                              "twins G-PAPER-CLAIMS, G-PAPER-NUMERAL-COVERAGE "
                              "and G-PAPER-CLAIM-POLARITY carry the three "
                              "injection falsifiers and die on every sweep",
}


# ---------------------------------------------------------------------------
# THE GATE-TIME SEAL (the engraving this unit buys).  A value is digested at
# the moment its gate passes; the payload may only be sealed once every earlier
# seal still verifies; the artifacts are written FROM the sealed payload; and
# the terminal integrity gate compares the bytes on disk against these digests.
# ---------------------------------------------------------------------------

SEALED_PATHS = [
    ("SEAL-VERDICT-STRING", "verdict/string", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-HEAD", "verdict/head", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-CENSUS", "dispersion_census", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-CLASS-ROWS", "class_rows", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-FIBER", "velocity_fiber", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-AGREEMENT", "agreement_matrix", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-DRIFT-TABLES", "support_drift_tables", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-STRATIFICATION", "stratification", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-RESOLUTION", "resolution", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-PATH-ANCHORS", "path_value_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-BYTE-ANCHORS", "byte_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-WAIVERS-VERIFIED"),
    ("SEAL-MUTANTS", "mutants", "G-MUTANTS-ON-TARGET"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-COVERAGE", "paper_coverage", "G-PAPER-COVERAGE-FINAL"),
]
# the seals taken before the mutant sweep -- the ones an in-process gate can
# verify, and the ones MUT-SEAL-BROKEN is measured against
SEALS_IN_RUN = tuple(sid for sid, _p, g in SEALED_PATHS
                     if g not in ("G-MUTANTS-ON-TARGET", "G-PAPER-COVERAGE-FINAL"))


def digest(value):
    """the canonical digest of a receipt object: its deterministic
    serialization, hashed.  Strings are hashed as themselves."""
    if isinstance(value, str):
        return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]
    return hashlib.sha256(
        json.dumps(value, indent=1, sort_keys=True).encode("utf-8")
    ).hexdigest()[:12]


class Seal:
    """the gate-time seal.  `take` digests an object at the moment its gate
    passed; `verify` re-digests the object as it stands NOW and names every
    seal that has since been broken; `close` refuses to seal the payload
    unless every earlier seal still holds."""

    def __init__(self):
        self.rows = []
        self.index = {}
        self.verdict_string = None
        self.payload = None
        self.payload_sha = None
        self.transcript = None
        self.transcript_sha = None

    def take(self, sid, obj):
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        gate = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        value = jpath(obj, path)
        d = digest(value)
        self.rows.append({"seal": sid, "path": path, "sealed_at_gate": gate,
                          "sha256_12": d})
        self.index[sid] = d
        if sid == "SEAL-VERDICT-STRING":
            self.verdict_string = value

    def verify(self, obj, only=None):
        broken = []
        for row in self.rows:
            if only is not None and row["seal"] not in only:
                continue
            try:
                now = digest(jpath(obj, row["path"]))
            except (KeyError, IndexError, TypeError):
                broken.append(row["seal"])
                continue
            if now != row["sha256_12"]:
                broken.append(row["seal"])
        return broken

    def close(self, obj, payload):
        """seal the payload -- only if every object seal still verifies."""
        broken = self.verify(obj)
        if broken:
            raise GateFail("G-ARTIFACT-INTEGRITY :: the payload was sealed over "
                           "a broken seal :: %s" % broken)
        self.payload = payload
        self.payload_sha = digest(payload)

    def close_transcript(self, text):
        self.transcript = text
        self.transcript_sha = digest(text)


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
        # NOTE on the sweep.  The stencil is the SET {0, a, -a}, which at the
        # three order-2 axes has only two distinct offsets: there the two
        # signed entries are ADDED, so the coefficient at that offset ranges
        # over the SUMSET of the declared alphabet rather than over the
        # alphabet itself.  That is a strictly wider search, not a narrower
        # one, and it admits no extra unitary -- the rebuild is a bijection
        # onto the parent's 58 rows (G-REBUILD-BIJECTION), which is what
        # establishes that the widening changes nothing.
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


def arena_artifact_witness():
    """THE SCOPE WITNESS.  The drift = winding identity that selects the tie in
    this arena is a property of THIS ALPHABET, not of the velocity definition.
    The parent's effectus panel exhibits, at the SAME lattice size, a unitary
    two-term generator over the wider field Q(i, sqrt 3) = Q(zeta_12):
    c_a = 1/2 at a = (1,0), c_{-a} = i sqrt3 / 2.  It is rebuilt here exactly,
    in a second field this unit constructs for the purpose and uses nowhere
    else, and its drift and its winding are computed and compared.  Q(zeta_12)
    is carried as 4-tuples over (1, w, w^2, w^3) modulo Phi_12 = x^4 - x^2 + 1,
    so w^4 = w^2 - 1 and w^6 = -1; the representation is canonical."""
    Z = Fraction(0)
    U = (Fraction(1), Z, Z, Z)

    def a12(x, y):
        return (x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3])

    def m12(x, y):
        r = [Z] * 7
        for i in range(4):
            if x[i]:
                for j in range(4):
                    if y[j]:
                        r[i + j] += x[i] * y[j]
        return (r[0] - r[4] - r[6], r[1] - r[5], r[2] + r[4], r[3] + r[5])

    def w12(t):
        p = U
        for _ in range(t % 12):
            p = m12(p, (Z, Fraction(1), Z, Z))
        return p

    def c12(x):
        """conjugation: w -> w^{-1} = w^{11}."""
        acc, p = (Z, Z, Z, Z), U
        for i in range(4):
            acc = a12(acc, tuple(x[i] * q for q in p))
            p = m12(p, w12(11))
        return acc

    MU12 = {w12(t): t for t in range(12)}
    i_ = w12(3)                                   # i = zeta_12^3
    sqrt3 = a12(w12(1), w12(11))                  # 2 cos(pi/6) = sqrt 3
    half = Fraction(1, 2)
    coef = {(1, 0): tuple(half * q for q in U),
            (3, 0): tuple(half * q for q in m12(i_, sqrt3))}
    LW = 4
    lags_ok = True
    for m in product(range(LW), repeat=2):
        acc = (Z, Z, Z, Z)
        for v, cv in coef.items():
            w = ((v[0] + m[0]) % LW, (v[1] + m[1]) % LW)
            if w in coef:
                acc = a12(acc, m12(cv, c12(coef[w])))
        if acc != (U if not any(m) else (Z, Z, Z, Z)):
            lags_ok = False
    s = {}
    for k in product(range(LW), repeat=2):
        acc = (Z, Z, Z, Z)
        for o, cv in coef.items():
            acc = a12(acc, m12(cv, w12((-3 * (k[0] * o[0] + k[1] * o[1])) % 12)))
        s[k] = MU12.get(acc)
    in_mu12 = sum(1 for v in s.values() if v is not None)

    def lift12(d):
        d %= 12
        return d - 12 if d > 6 else d

    diffs = [lift12(s[((kx + 1) % LW, 0)] - s[(kx, 0)]) for kx in range(LW)]
    # v = -(L/N) lift(Delta) with L = 4, N = 12
    wind = Fraction(-sum(lift12(s[((k[0] + 1) % LW, k[1])] - s[k])
                         for k in product(range(LW), repeat=2)), 3 * LW * LW)
    dr = sum(m12(cv, c12(cv))[0] * (o[0] - LW if 2 * o[0] > LW else o[0])
             for o, cv in coef.items())
    return {"field": "Q(i,sqrt3) = Q(zeta_12)",
            "generator": "c_(1,0) = 1/2, c_(3,0) = i sqrt3 / 2",
            "unitary_all_lags": lags_ok,
            "root_order": 12,
            "eigenphases_in_mu_12": in_mu12,
            "eigenphase_row_k_y_0": [s[(kx, 0)] for kx in range(LW)],
            "forward_differences_lifted": diffs,
            "difference_sum": sum(diffs),
            "winding": str(wind),
            "born_drift": str(dr),
            "identity_holds": wind == dr,
            "cells": LW * LW,
            "eigenphases_outside_mu_8": sum(1 for v in s.values() if v % 3 != 0)}


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
        if mut("MUT-QUOTE-TRUNCATE"):
            w = w[:4]                    # every window reduced to a decoration
        present = w in texts[sid]
        vb_rows.append({"id": vid, "source": sid, "consumer_gate": consumer,
                        "present": present, "chars": len(w),
                        "occurrences": texts[sid].count(w),
                        "window_sha256_12": digest(w)})
        if not present:
            vb_missing.append(vid)
    if mut("MUT-QUOTE-AMBIGUOUS"):
        vb_rows[0]["occurrences"] = 2
    LD.gate("G-VERBATIM-ANCHORS",
            "every verbatim anchor is a context window present in its pinned "
            "source, and each is bound to the named gate that consumes it "
            "(#34: evaluated before the byte anchors)",
            not vb_missing, "missing %s over %d windows"
            % (vb_missing or "none", len(vb_rows)))
    bad_window = sorted(r["id"] for r in vb_rows
                        if r["window_sha256_12"] != WINDOW_DIGESTS.get(r["id"]))
    LD.gate("G-VERBATIM-WINDOW-DIGESTS",
            "a window is an ANCHOR only if its BYTES are pinned: every "
            "verbatim window's sha256-12 equals the digest this unit froze, so "
            "a window silently shortened to a decoration -- the failure mode a "
            "bare substring test admits -- is caught rather than displayed "
            "(#62, the parent's window_sha256_12 field restored)",
            not bad_window, "windows off their frozen digest: %s over %d"
            % (bad_window or "none", len(vb_rows)))
    ambiguous = sorted(r["id"] for r in vb_rows if r["occurrences"] != 1)
    LD.gate("G-VERBATIM-WINDOWS-UNIQUE",
            "every verbatim window occurs EXACTLY ONCE in its pinned source: a "
            "window that matches in several places does not identify the "
            "sentence it claims to quote",
            not ambiguous, "windows not occurring exactly once: %s over %d"
            % (ambiguous or "none", len(vb_rows)))

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
                        "scrambled": sorted({stab[name[g["local"]]]
                                             for g in pool
                                             if g["kind"] == "SCRAM"}),
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
    # THE LOAD-BEARING LEG.  Kronecker's theorem needs an ALGEBRAIC INTEGER,
    # and that does not follow from unit modulus alone.  It is measured here:
    # the characteristic polynomial of multiplication by each symbol has
    # integer coefficients, at every one of the census cells.
    nonintegral = []
    for g in pool[:ncirc]:
        for k in duals:
            cs = charpoly(symbol(g["coef"], k, L))
            if any(q.denominator != 1 for q in cs):
                nonintegral.append((name[g["local"]], k))
    if mut("MUT-INTEGRALITY"):
        nonintegral.append(("INJECTED", (0, 0)))
    LD.gate("G-MU8-THEOREM-LEGS",
            "the finite legs of the reason the eigenvalues cannot be anything "
            "else: every coefficient has a 2-power denominator, and 2 is "
            "totally ramified in Q(zeta_8), so a unit-modulus symbol is an "
            "ALGEBRAIC INTEGER -- measured here as the integrality of the "
            "characteristic polynomial of multiplication by the symbol at "
            "every cell -- and a unit of Z[zeta_8] all of whose conjugates "
            "have modulus 1, hence a root of unity, hence one of the 8 the "
            "field contains",
            dens == {1} and len(MU8) == 8 and not nonintegral,
            "odd parts of coefficient denominators %s; roots of unity in the "
            "field %d; symbols with a non-integral characteristic polynomial "
            "%s over %d cells"
            % (sorted(dens), len(MU8), nonintegral[:3] or "none", total_cells))

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
            "independent of every reading OF THE TIE -- of all three lifts -- "
            "because the distance of an element of Z/8 to zero does not depend "
            "on how the antipode is signed.  (Independence of the STENCIL "
            "coordinate is a different statement and is measured separately, "
            "at G-RESIDUAL-FIBER-INERT.)",
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

    # ---- THE STENCIL COORDINATE IS FORCED BY THE DECLARED NORMALISATION ----
    # The definition's own sign-fixing requirement -- a monomial shift by an
    # offset o has velocity o -- is a CRITERION, not a remark.  Measured over
    # every monomial family, every momentum, every direction and every
    # non-antipodal offset coordinate (where the requirement is not degenerate).
    norm_rows = []
    for stencil in STENCIL_READINGS:
        ok = tot = 0
        for g in pool[:ncirc]:
            if not g["monomial"]:
                continue
            n = name[g["local"]]
            o = list(g["coef"])[0] if g["coef"] else (0, 0)
            for k in duals:
                for j in range(D):
                    oj = o[j] % L
                    if 2 * oj == L:
                        continue          # the antipodal coordinate: degenerate
                    want = oj - L if 2 * oj > L else oj
                    tot += 1
                    if velocity(n, k, j, LIFT_DECLARED, stencil) == want:
                        ok += 1
        norm_rows.append({"stencil": stencil, "satisfied": ok,
                          "coordinates": tot,
                          "admitted": ok == tot})
    if mut("MUT-STENCIL-CENTRAL"):
        [r for r in norm_rows if r["stencil"] == "CENTRAL"][0]["admitted"] = True
    admitted = tuple(r["stencil"] for r in norm_rows if r["admitted"])
    LD.gate("G-STENCIL-FORCED-BY-NORMALISATION",
            "the STENCIL coordinate of the velocity definition is not free: "
            "the definition's own declared normalisation -- a monomial shift "
            "by an offset o has velocity o -- is evaluated as a CRITERION over "
            "every monomial family, momentum, direction and non-antipodal "
            "offset coordinate, and it admits exactly the forward and backward "
            "stencils, at every one of those coordinates, while the central "
            "stencil FAILS it.  The fiber of 9 is therefore 3 lifts times 2 "
            "admissible stencils, and the third stencil is excluded by the "
            "definition rather than by fiat",
            admitted == STENCIL_FORCED
            and all(r["satisfied"] == r["coordinates"] for r in norm_rows
                    if r["stencil"] in STENCIL_FORCED)
            and all(r["satisfied"] < r["coordinates"] for r in norm_rows
                    if r["stencil"] not in STENCIL_FORCED),
            "admitted %s; %s" % (list(admitted),
                                 [(r["stencil"], "%d/%d" % (r["satisfied"],
                                                            r["coordinates"]))
                                  for r in norm_rows]))

    # ---- THE RESIDUAL FIBER, MEASURED INERT --------------------------------
    # What the normalisation forces and the identity selects leaves 2: forward
    # and backward.  Every quantity this unit reports is required to be
    # IDENTICAL under both, and the disclosure -- where they differ at all --
    # is measured rather than argued.
    def back_delta(n, k, j):
        e = BASIS_DIRECTIONS[j]
        prev = tuple((k[i] - e[i]) % L for i in range(D))
        return (disp[n][k] - disp[n][prev]) % 8

    speed_back, alias_back, signed_diff = {}, 0, 0
    for n in disp:
        mx = Fraction(0)
        for k in duals:
            for j in range(D):
                d = back_delta(n, k, j)
                mx = max(mx, Fraction(circle_distance(d), 2))
                if d == 4:
                    alias_back += 1
                if (Fraction(-lift(d, LIFT_DECLARED), 2)
                        != velocity(n, k, j, LIFT_DECLARED, STENCIL_DECLARED)):
                    signed_diff += 1
        speed_back[n] = mx
    if mut("MUT-RESIDUAL-FIBER"):
        speed_back[nonconstant[0]] = Fraction(9)
    spectrum_back = sorted({Fraction(circle_distance(back_delta(n, k, j)), 2)
                            for n in disp for k in duals for j in range(D)})
    alias_fams_back = len({n for n in disp for k in duals for j in range(D)
                           if back_delta(n, k, j) == 4})
    residual = {"residual_fiber": len(STENCIL_FORCED),
                "members": list(STENCIL_FORCED),
                "per_family_max_speed_identical": speed_back == speed,
                "spectrum_identical": spectrum_back == spectrum,
                "aliased_cells_identical": alias_back == len(aliased),
                "aliased_families_identical": alias_fams_back == len(alias_families),
                "motion_head_identical": all((speed_back[n] != 0)
                                             == (speed[n] != 0) for n in disp),
                "signed_velocity_cells_differing": signed_diff,
                "cells": n_delta}
    LD.gate("G-RESIDUAL-FIBER-INERT",
            "the residual fiber is 2 -- forward and backward -- and it is "
            "measured INERT, not asserted inert: the per-family maximal speed, "
            "the speed spectrum, VMAX, the aliasing census and the motion head "
            "are identical under both admissible stencils, family by family "
            "and cell count for cell count.  The two readings are not the same "
            "velocity field: they disagree on the SIGN of the velocity at a "
            "measured share of cells, and that is the whole of the residual "
            "declaration",
            residual["per_family_max_speed_identical"]
            and residual["spectrum_identical"]
            and residual["aliased_cells_identical"]
            and residual["aliased_families_identical"]
            and residual["motion_head_identical"]
            and max(speed_back.values()) == VMAX
            and 0 < signed_diff < n_delta,
            "%s" % residual)

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

    # the same fact, FORCED rather than merely measured -- this is what the
    # gauge rung inherits
    full_stab = sorted(n for n in stab if stab[n] == len(sites))
    circ_names = sorted(name[g["local"]] for g in pool[:ncirc])
    ctrl_names = sorted(name[g["local"]] for g in pool[ncirc:])
    if mut("MUT-NOTBLOCH-FORCED"):
        full_stab = full_stab[:-1]
    LD.gate("G-NOT-BLOCH-FORCED",
            "the non-diagonality of the controls is a THEOREM, not only a "
            "measurement: a generator is diagonal in the lattice characters if "
            "and only if it commutes with every translation, i.e. iff its "
            "translation stabiliser is the whole group.  Measured here: the "
            "generators with the full stabiliser are exactly the circulant "
            "family, every control's stabiliser is proper -- the brickwork "
            "generators' is of INDEX TWO -- and therefore no control can be "
            "Bloch diagonal.  The measurement above and this forcing agree",
            full_stab == circ_names
            and all(stab[n] < len(sites) for n in ctrl_names)
            and sorted(brick_stab)[0] * 2 == len(sites)
            and sorted(notbloch) == ctrl_names,
            "full-stabiliser generators %d = the %d circulants; control "
            "stabilisers %s, all proper; brickwork index %d; measured "
            "not-Bloch %d of %d"
            % (len(full_stab), ncirc, sorted({stab[n] for n in ctrl_names}),
               len(sites) // sorted(brick_stab)[0], len(notbloch),
               len(ctrl_names)))

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

    # an UPPER bound is falsified by the overshooters, and only by them
    upper_falsifiers, lower_falsifiers = list(over), list(under)
    if mut("MUT-REACH-DIRECTION"):
        upper_falsifiers, lower_falsifiers = lower_falsifiers, upper_falsifiers
    upper_bound_holds = not upper_falsifiers
    lower_bound_holds = not lower_falsifiers
    LD.gate("G-REACH-BOUND-DIRECTION",
            "which count falsifies which bound is DERIVED, not labelled: an "
            "upper bound on the one-step reach is falsified exactly by the "
            "families whose speed EXCEEDS their own reach, and a lower bound "
            "exactly by the families whose speed falls BELOW it.  Both fail "
            "here, at different counts, and the verdict carries both",
            all(speed[n] > byname[n]["radius"] for n in upper_falsifiers)
            and all(speed[n] < byname[n]["radius"] for n in lower_falsifiers)
            and len(upper_falsifiers) + len(lower_falsifiers) + len(equal) == ncirc
            and upper_bound_holds is False and lower_bound_holds is False,
            "upper bound holds=%s (falsified by the %d overshooters); lower "
            "bound holds=%s (falsified by the %d undershooters); saturating %d"
            % (upper_bound_holds, len(upper_falsifiers), lower_bound_holds,
               len(lower_falsifiers), len(equal)))

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

    bound_has_content = (not cone_covers) and upper_bound_holds
    if mut("MUT-BOUND"):
        bound_has_content = True
    LD.gate("G-BOUND-DERIVED",
            "the bound's verdict is DERIVED from the two computed facts a "
            "propagation bound actually asserts -- whether the one-step cone "
            "is proper, and whether the speed is an UPPER bound on the reach "
            "it is supposed to constrain -- and is not a typed opinion.  The "
            "undershooting families are consistent with an upper bound and "
            "enter only the lower-bound clause",
            bound_has_content is False and bound_has_content
            == ((not cone_covers) and upper_bound_holds),
            "cone proper=%s; families over their own reach=%d; bound has "
            "content=%s" % (not cone_covers, len(over), bound_has_content))

    # ---- VMAX = DIAMETER IS STRUCTURAL, NOT A FACT ABOUT THIS SIZE ---------
    # The group speed is a phase advance per momentum step, so it is bounded by
    # L/2, which IS the max-norm diameter of (Z_L)^d for even L; and the
    # monomial shift by the antipodal offset (L/2, 0) is a unitary member of
    # the axis family at EVERY even L and attains it.  Exercised at five sizes.
    structural = []
    for LL in STRUCTURAL_SIZES:
        pts = list(product(range(LL), repeat=2))
        diam = max(torus_absmax(x, LL) for x in pts)
        o = (LL // 2, 0)
        top = Fraction(0)
        for k in pts:
            for j, e in enumerate(BASIS_DIRECTIONS):
                s1 = (-((k[0] + e[0]) * o[0] + (k[1] + e[1]) * o[1])) % LL
                s0 = (-(k[0] * o[0] + k[1] * o[1])) % LL
                dd = (s1 - s0) % LL
                top = max(top, Fraction(min(dd, LL - dd)))
        radii = sorted({torus_absmax(x, LL) for x in pts})
        structural.append({"L": LL, "diameter": diam,
                           "antipodal_monomial_speed": str(top),
                           "vmax_equals_diameter": top == diam,
                           "cone_covers_torus": top >= diam,
                           "interior_radii": [r for r in radii if 0 < r < diam],
                           "interior_radius_count":
                               len([r for r in radii if 0 < r < diam])})
    if mut("MUT-STRUCTURAL-L"):
        structural[2]["vmax_equals_diameter"] = False
    LD.gate("G-CONE-VACUITY-STRUCTURAL",
            "the emptiness of the one-step cone is a THEOREM about even "
            "periodic lattices, not a resolution failure of the admitted size: "
            "the group speed is a phase advance per momentum step and is "
            "therefore bounded by L/2, which is exactly the max-norm diameter, "
            "and the monomial shift by the antipodal offset is a family member "
            "at every even L and attains it.  Exercised at five sizes: the "
            "cone covers the whole torus at every one of them, so no "
            "enlargement of the lattice makes the constraint bite.  What the "
            "admitted size does control is the number of INTERIOR max-norm "
            "radii -- one here, three at L = 8 -- which is the genuine "
            "resolution parameter",
            all(r["vmax_equals_diameter"] and r["cone_covers_torus"]
                for r in structural)
            and structural[0]["L"] == L
            and structural[0]["interior_radius_count"] == 1
            and [r for r in structural if r["L"] == 8][0]["interior_radius_count"] == 3,
            "%s" % [(r["L"], r["diameter"], r["antipodal_monomial_speed"],
                     r["interior_radius_count"]) for r in structural])

    # the disclosure the exclusion of the central stencil buys: what the census
    # would have said under the reading the normalisation rejects
    central = {"vmax": None, "aliased_cells": 0, "aliased_families": 0,
               "reach_over": 0, "reach_under": 0, "reach_equal": 0,
               "cone_sites_one_step": 0}
    csp, cfam = {}, set()
    for g in pool[:ncirc]:
        n = name[g["local"]]
        mx = Fraction(0)
        for k in duals:
            for j, e in enumerate(BASIS_DIRECTIONS):
                fw = addv(k, e)
                bk = tuple((k[i] - e[i]) % L for i in range(D))
                dd = (disp[n][fw] - disp[n][bk]) % 8
                mx = max(mx, Fraction(circle_distance(dd), 4))
                if dd == 4:
                    central["aliased_cells"] += 1
                    cfam.add(n)
        csp[n] = mx
    central["vmax"] = str(max(csp.values()))
    central["aliased_families"] = len(cfam)
    for g in pool[:ncirc]:
        n = name[g["local"]]
        if csp[n] > g["radius"]:
            central["reach_over"] += 1
        elif csp[n] < g["radius"]:
            central["reach_under"] += 1
        else:
            central["reach_equal"] += 1
    central["cone_sites_one_step"] = sum(
        1 for x in sites if torus_absmax(x, L) <= max(csp.values()))
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
    # the winding under each admissible stencil, so the identity's blindness to
    # the stencil coordinate is MEASURED rather than inferred
    winding_st = {}
    for reading in LIFT_READINGS:
        for stencil in STENCIL_READINGS:
            for g in pool[:ncirc]:
                n = name[g["local"]]
                winding_st[(n, reading, stencil)] = tuple(
                    sum((velocity(n, k, j, reading, stencil) for k in duals),
                        Fraction(0)) / len(duals)
                    for j in range(D))
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
    agree27 = {}
    for r1 in LIFT_READINGS:
        for r2 in LIFT_READINGS:
            for st in STENCIL_READINGS:
                agree27[(r1, r2, st)] = sum(
                    1 for g in pool[:ncirc]
                    if drift[(name[g["local"]], r1)]
                    == winding_st[(name[g["local"]], r2, st)])
    full27 = sorted(kk for kk, v in agree27.items() if v == ncirc)
    stencil_blind = all(winding_st[(name[g["local"]], r, "FORWARD")]
                        == winding_st[(name[g["local"]], r, "BACKWARD")]
                        for g in pool[:ncirc] for r in LIFT_READINGS)
    LD.gate("G-DRIFT-WINDING-IDENTITY",
            "the two roads to how far a family moves in one step -- the Born "
            "drift of the coefficient map in position space, and the winding "
            "of the eigenphase around the dual torus -- are computed "
            "independently and compared family by family under all nine ways "
            "of reading the two antipodal TIES.  Exactly one tie-reading pair "
            "makes them agree for every family, and it is the pair that "
            "resolves both ties the same way: by averaging.  What the identity "
            "selects is therefore the TIE, uniquely; it is BLIND to the "
            "stencil -- measured here: the winding is identical family by "
            "family under the forward and the backward difference, so both "
            "reach the identity and TWO of the 27 lift x lift x stencil "
            "readings do, not one",
            matched_agree == ncirc and full == [(LIFT_DECLARED, LIFT_DECLARED)]
            and best_other < ncirc and stencil_blind
            and full27 == sorted([(LIFT_DECLARED, LIFT_DECLARED, st)
                                  for st in STENCIL_FORCED]),
            "identity holds at %d of %d tie-reading pairs (%s); best other "
            "pair %d of %d families; over the 27 lift x lift x stencil "
            "readings it holds at %d, namely %s; winding stencil-blind=%s"
            % (len(full), len(agree), full, best_other, ncirc, len(full27),
               full27, stencil_blind))

    witness = arena_artifact_witness()
    if mut("MUT-ARENA-WITNESS"):
        witness["identity_holds"] = True
    LD.gate("G-ARENA-ARTIFACT-WITNESS",
            "the selecting identity is an ARENA ARTIFACT and may serve as an "
            "instrument, never as a conclusion about the velocity definition "
            "(RUNBOOK section 15).  The parent panel's constructive "
            "widened-alphabet generator -- anchored verbatim, at the SAME "
            "lattice size -- is rebuilt here exactly over Q(zeta_12): it is "
            "unitary at all 16 lags, its eigenphases leave the declared field, "
            "its Born drift is the value the panel published, its winding is a "
            "DIFFERENT number, and the identity therefore FAILS at the first "
            "widening of the modulus set",
            witness["unitary_all_lags"]
            and witness["eigenphases_in_mu_12"] == witness["cells"]
            and witness["eigenphases_outside_mu_8"] == witness["cells"]
            and witness["born_drift"] == "-1/2"
            and witness["winding"] == "-1"
            and witness["identity_holds"] is False
            and witness["difference_sum"] == 12
            and [r for r in vb_rows
                 if r["id"] == "VB-WIDENED-GENERATOR"][0]["present"],
            "%s" % witness)

    supp_tables = {}
    for reading in LIFT_READINGS:
        tbl = {}
        for g in pool[:ncirc]:
            n = name[g["local"]]
            row = tbl.setdefault(g["support"], {"generators": 0,
                                                "nonzero_drift": 0})
            row["generators"] += 1
            if any(drift[(n, reading)]):
                row["nonzero_drift"] += 1
        supp_tables[reading] = tbl
    supp_table = supp_tables[LIFT_DECLARED]
    if mut("MUT-DRIFT-TABLE"):
        supp_table[1]["nonzero_drift"] = 13
    if mut("MUT-DRIFT-ALT"):
        supp_tables["POSITIVE"] = {k: dict(v) for k, v in supp_table.items()}
    review_rows = {1: {"generators": 16, "nonzero_drift": 12},
                   2: {"generators": 18, "nonzero_drift": 0},
                   3: {"generators": 24, "nonzero_drift": 0}}
    reproduces = sorted(r for r in LIFT_READINGS
                        if {k: supp_tables[r][k] for k in sorted(supp_tables[r])}
                        == review_rows)
    LD.gate("G-EFFECTUS-DRIFT-TABLE",
            "the frozen effectus review's one-step drift table is reproduced "
            "from this unit's own rebuild, and reproducing it IDENTIFIES the "
            "convention it was taken under: the antipodal displacement is "
            "tie-averaged to zero.  Under that reading, and ONLY under it, the "
            "table's three rows come out as the review printed them -- the "
            "exclusion is evaluated here, over all three lifts, and not "
            "asserted: the positive and the negative readings are both "
            "computed and both required to FAIL",
            supp_table[1] == review_rows[1] and supp_table[2] == review_rows[2]
            and supp_table[3] == review_rows[3]
            and reproduces == [LIFT_DECLARED],
            "readings reproducing the review's rows: %s; tie-averaged %s; "
            "positive %s; negative %s"
            % (reproduces,
               {k: supp_tables["TIE-AVERAGED"][k] for k in sorted(supp_table)},
               {k: supp_tables["POSITIVE"][k] for k in sorted(supp_table)},
               {k: supp_tables["NEGATIVE"][k] for k in sorted(supp_table)}))

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
            "net transport is monomial, every NON-MONOMIAL family has exactly "
            "zero net transport in BOTH spaces at the selected reading, and "
            "yet every one of those families MOVES -- its dispersion is "
            "non-constant and its group velocity is nonzero at individual "
            "momenta.  The zero is a sum of nonzero summands, not an absence "
            "of motion; how much of it survives the other tie readings is "
            "measured separately at G-CANCELLATION-ROBUSTNESS",
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
    # ---- how much of the zero is reading-independent ------------------------
    drift_all_readings = sorted(n for n in interfering
                                if all(not any(drift[(n, r)])
                                       for r in LIFT_READINGS))
    wind_all_readings = sorted(n for n in interfering
                               if all(not any(winding[(n, r)])
                                      for r in LIFT_READINGS))
    if mut("MUT-ROBUSTNESS"):
        drift_all_readings = drift_all_readings[:-1]
    # the second route: the complement, taken over readings rather than over
    # families, so a count moved on one side does not move on the other
    drift_route2 = len(interfering) - len({n for n in interfering
                                           for r in LIFT_READINGS
                                           if any(drift[(n, r)])})
    wind_route2 = len(interfering) - len({n for n in interfering
                                          for r in LIFT_READINGS
                                          if any(winding[(n, r)])})
    robust = {"non_monomial": len(interfering),
              "zero_drift_all_readings": len(drift_all_readings),
              "zero_drift_averaged_only": len(interfering) - len(drift_all_readings),
              "zero_winding_all_readings": len(wind_all_readings),
              "zero_winding_averaged_only": len(interfering) - len(wind_all_readings),
              "winding_averaged_only_are_the_aliased":
                  sorted(set(interfering) - set(wind_all_readings))
                  == sorted(set(interfering) & set(alias_families))}
    LD.gate("G-CANCELLATION-ROBUSTNESS",
            "the zero net transport of the non-monomial families is stratified "
            "by how much of it survives the tie: for a measured subset the "
            "zero holds under ALL THREE tie readings and no convention can "
            "undo it; for the remainder the zero IS the antipodal average, and "
            "those families are exactly the non-monomials that carry aliased "
            "cells.  The two spaces split differently, and the verdict carries "
            "both numbers rather than the unqualified count",
            robust["zero_drift_all_readings"] == drift_route2
            and robust["zero_winding_all_readings"] == wind_route2
            and robust["zero_drift_all_readings"] + robust["zero_drift_averaged_only"]
            == len(interfering)
            and robust["zero_winding_all_readings"]
                + robust["zero_winding_averaged_only"] == len(interfering)
            and 0 < robust["zero_drift_all_readings"] < len(interfering)
            and 0 < robust["zero_winding_all_readings"] < len(interfering)
            and robust["winding_averaged_only_are_the_aliased"],
            "%s" % robust)

    # ---- the word "interfering", bound to the parent's own defect rows ------
    parent_rows = {(r["U"], r["V"]): r for r in jpath(R4, "census_rows")}
    diag_nonzero = sorted(n for n in
                          [name[g["local"]] for g in pool[:ncirc]]
                          if parent_rows[(n, n)]["nonzero_cells"] > 0)
    defect_free = sorted(n for n in [name[g["local"]] for g in pool[:ncirc]]
                         if all(parent_rows[(u, v)]["nonzero_cells"] == 0
                                for (u, v) in parent_rows if u == n or v == n))
    if mut("MUT-DEFECT-BINDING"):
        diag_nonzero = diag_nonzero[:-1]
    LD.gate("G-NON-MONOMIAL-DEFECT-BOUND",
            "the word this unit uses for the 42 is bound to the parent's own "
            "rows and is not a rename: the generators whose DIAGONAL "
            "composition defect is nonzero in the parent's 4096-row census are "
            "exactly this unit's non-monomial families, object by object, and "
            "the generators on which the defect vanishes across EVERY pair "
            "they appear in are exactly its 16 monomials.  No defect is "
            "recomputed here; the binding is to the anchored receipt",
            diag_nonzero == interfering and defect_free == monomials
            and len(parent_rows) == jpath(R4, "counts/pairs_total"),
            "non-monomial with a nonzero diagonal defect %d of %d; "
            "defect-free across every pair %d = the %d monomials; parent rows "
            "%d" % (len(diag_nonzero), len(interfering), len(defect_free),
                    len(monomials), len(parent_rows)))

    # ---- the like-for-like class separation --------------------------------
    circ_class_rows = [c for c in classes if c["kind"] == "CIRC"]
    multisets = {}
    for c in circ_class_rows:
        key = tuple(sorted(tuple(sigma[name[m]][k] for k in duals)
                           for m in c["members"]))
        multisets.setdefault(key, []).append(c["rep"])
    class_constant = sorted(c["rep"] for c in circ_class_rows
                            if len({tuple(sigma[name[m]][k] for k in duals)
                                    for m in c["members"]}) == 1)
    n_multisets = len(multisets)
    if mut("MUT-CLASS-MULTISET"):
        n_multisets -= 1
    LD.gate("G-CLASS-SEPARATION-BY-MULTISET",
            "the like-for-like comparison the parent's label deficit actually "
            "calls for: the reduced dispersion is NOT a class invariant -- it "
            "is constant only on the singleton classes -- so a count of "
            "distinct profiles per FAMILY is not a class separation.  The "
            "MULTISET of member reduced dispersions is a class invariant by "
            "construction, and it separates every one of the circulant "
            "classes, where the parent's conjugacy invariants give fewer "
            "labels than it has classes",
            n_multisets == len(circ_class_rows)
            and len(class_constant) == sum(1 for c in circ_class_rows
                                           if c["size"] == 1)
            and jpath(R4, "counts/class_labels")
            < jpath(R4, "counts/classes_extended"),
            "distinct dispersion multisets %d over %d circulant classes; the "
            "reduced dispersion is constant on %d of them (the singletons %s); "
            "the parent's invariant labels: %d for %d extended classes"
            % (n_multisets, len(circ_class_rows), len(class_constant),
               class_constant, jpath(R4, "counts/class_labels"),
               jpath(R4, "counts/classes_extended")))

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
        "class_separation_multisets": n_multisets,
        "algebraic_integers": total_cells - len(nonintegral),
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
        "stencil_admitted": len(admitted),
        "stencil_normalisation_coordinates": norm_rows[0]["coordinates"],
        "residual_fiber": len(STENCIL_FORCED),
        "residual_fiber_cells_differing": signed_diff,
        # POLARITY RENDERED FROM THE RECEIPT (#20): the direction of these
        # three claims is a computed word, so a prose inversion of them cannot
        # survive the claim check even when it moves no numeral
        "residual_fiber_inert": ("INERT" if all(
            residual[k] for k in ("per_family_max_speed_identical",
                                  "spectrum_identical", "aliased_cells_identical",
                                  "aliased_families_identical",
                                  "motion_head_identical")) else "LIVE"),
        "character_convention_fiber": 2,
        "reach_over": len(over),
        "reach_under": len(under),
        "reach_equal": len(equal),
        "cone_sites_one_step": len(cone_1),
        "sites": len(sites),
        "diameter": diameter,
        "interior_radii": resolution["interior_radii"],
        "structural_sizes": len(structural),
        "interior_radii_at_l8": [r for r in structural
                                 if r["L"] == 8][0]["interior_radius_count"],
        "bound_has_content": bound_has_content,
        "separations": separations,
        "separations_ceiling": sep_ceiling,
        "max_defect_radius": max_defect_radius,
        "radius_ceiling": radius_ceiling,
        "drift_winding_matched": matched_agree,
        "drift_winding_mismatched": best_other,
        "reading_pairs": len(agree),
        "reading_pairs_with_identity": len(full),
        "full_readings": len(agree27),
        "full_readings_with_identity": len(full27),
        "witness_winding": witness["winding"],
        "witness_drift": witness["born_drift"],
        "witness_root_order": witness["root_order"],
        "witness_identity": "FAILS" if not witness["identity_holds"] else "HOLDS",
        "nonzero_winding": len(nonzero_wind),
        "monomial": len(monomials),
        "nonmonomial_pool": len(pool) - len(monomials),
        "interfering": len(interfering),
        "interfering_moving": len(interfering_moving),
        "interfering_zero_net": len(interfering_zero_net),
        "zero_drift_all_readings": robust["zero_drift_all_readings"],
        "zero_winding_all_readings": robust["zero_winding_all_readings"],
        "diagonal_defect_nonzero": len(diag_nonzero),
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
        "supp_tables": {r: {str(k): supp_tables[r][k]
                            for k in sorted(supp_tables[r])}
                        for r in LIFT_READINGS},
        "agreement_matrix": {"%s|%s" % kk: v for kk, v in sorted(agree.items())},
        "agreement_matrix_full": {"%s|%s|%s" % kk: v
                                  for kk, v in sorted(agree27.items())},
        "profiles": {"distinct": len(profiles),
                     "largest": max(len(v) for v in profiles.values())},
        "stratification": {
            "stencil_normalisation": norm_rows,
            "stencil_admitted": list(admitted),
            "residual_fiber": residual,
            "structural_vmax": structural,
            "central_stencil_disclosure": central,
            "arena_artifact_witness": witness,
            "cancellation_robustness": robust,
            "class_separation": {
                "circulant_classes": len(circ_class_rows),
                "distinct_dispersion_multisets": n_multisets,
                "classes_with_a_constant_dispersion": class_constant,
                "parent_invariant_labels": jpath(R4, "counts/class_labels"),
                "parent_extended_classes": jpath(R4, "counts/classes_extended")},
            "reach_direction": {
                "upper_bound_holds": upper_bound_holds,
                "upper_bound_falsified_by": len(over),
                "lower_bound_holds": lower_bound_holds,
                "lower_bound_falsified_by": len(under),
                "saturating": len(equal)},
            "defect_binding": {
                "non_monomial_with_nonzero_diagonal_defect": len(diag_nonzero),
                "defect_free_across_every_pair": len(defect_free),
                "parent_rows_read": len(parent_rows)},
        },
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
    S["_r4"] = R4
    S["_class_rows_src"] = classes
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
                    "algebraic_integers", "parity_invariant", "families",
                    "distinct_profiles", "class_separation_multisets",
                    "classes_circulant", "class_labels", "classes_extended"]),
    ("VELOCITY", ["speed_spectrum", "vmax", "integer_velocities",
                  "velocity_cells", "aliased_cells", "aliased_families",
                  "velocity_definition", "velocity_fiber", "stencil_admitted",
                  "stencil_normalisation_coordinates", "residual_fiber",
                  "residual_fiber_cells_differing"]),
    ("BOUND", ["bound_has_content", "cone_sites_one_step", "sites", "vmax",
               "diameter", "structural_sizes", "reach_under", "reach_over",
               "reach_equal", "families", "separations", "separations_ceiling",
               "max_defect_radius", "radius_ceiling", "interior_radii",
               "interior_radii_at_l8"]),
    ("TRANSPORT", ["drift_winding_matched", "families", "reading_pairs_with_identity",
                   "reading_pairs", "drift_winding_mismatched",
                   "full_readings_with_identity", "full_readings",
                   "witness_root_order", "witness_winding", "witness_drift",
                   "nonzero_winding", "monomial", "interfering",
                   "interfering_moving", "interfering_zero_net",
                   "zero_drift_all_readings", "zero_winding_all_readings",
                   "diagonal_defect_nonzero", "markov_nonzero", "markov_pairs"]),
    ("SCOPE", ["d", "L", "field", "alphabet", "pool", "stencil", "sector",
               "connective_tag", "forcing_link", "indivisibility", "momenta",
               "character_convention_fiber"]),
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
                       "UNIT-MODULUS=%s;ALGEBRAIC-INTEGERS=%s;"
                       "PARITY-INVARIANT=%s-OF-%s;DISTINCT-REDUCED-PROFILES=%s-"
                       "OF-%s-FAMILIES(FORCED-BY-INVERTIBILITY);CLASS-SEPARATION"
                       "=%s-OF-%s-CIRCULANT-BY-DISPERSION-MULTISET-VS-%s-LABELS-"
                       "FOR-%s-CLASSES"
         % (c["in_mu8"], c["cells"], c["eigen_verified"], c["unit_modulus"],
            c["algebraic_integers"], c["parity_invariant"], c["families"],
            c["distinct_profiles"], c["families"],
            c["class_separation_multisets"], c["classes_circulant"],
            c["class_labels"], c["classes_extended"])),
        ("VELOCITY", "SPECTRUM=%s;VMAX=%s;INTEGER-VALUED=%s-OF-%s;"
                     "ALIASED=%s-OF-%s-IN-%s-FAMILIES;DEFINITION=%s(FIBER=%s;"
                     "STENCIL-FORCED-TO-%s-BY-MONOMIAL-NORMALISATION-AT-%s-OF-%s;"
                     "LIFT-SELECTED-1-OF-3-BY-DRIFT=WINDING;RESIDUAL-FIBER=%s-"
                     "MEASURED-INERT-DIFFERING-AT-%s-OF-%s-SIGNED-CELLS)"
         % ("+".join(c["speed_spectrum"]), c["vmax"], c["integer_velocities"],
            c["velocity_cells"], c["aliased_cells"], c["velocity_cells"],
            c["aliased_families"], c["velocity_definition"], c["velocity_fiber"],
            c["stencil_admitted"], c["stencil_normalisation_coordinates"],
            c["stencil_normalisation_coordinates"], c["residual_fiber"],
            c["residual_fiber_cells_differing"], c["velocity_cells"])),
        ("BOUND", "NO-CONTENT=%s;CONE-AT-ONE-STEP=%s-OF-%s-SITES;VMAX=%s=DIAMETER"
                  "=%s(CEILING-FORCED;ATTAINMENT-MEASURED;STRUCTURAL-AT-EVERY-"
                  "EVEN-L-AT-%s-SIZES);REACH-UPPER-BOUND-FALSE-AT=%s-OF-%s;"
                  "REACH-LOWER-BOUND-FALSE-AT=%s-OF-%s;SATURATES-AT=%s;"
                  "INHERITED-CEILINGS=SEPARATIONS=%s-OF-%s;MAX-DEFECT-RADIUS=%s-"
                  "OF-%s;INTERIOR-RADII=%s-HERE-%s-AT-L-8;RESIDUAL-FIBER-"
                  "INVARIANT=YES"
         % ("YES" if not c["bound_has_content"] else "NO", c["cone_sites_one_step"],
            c["sites"], c["vmax"], c["diameter"], c["structural_sizes"],
            c["reach_over"], c["families"], c["reach_under"], c["families"],
            c["reach_equal"], c["separations"], c["separations_ceiling"],
            c["max_defect_radius"], c["radius_ceiling"],
            "+".join(str(x) for x in c["interior_radii"]),
            c["interior_radii_at_l8"])),
        ("TRANSPORT", "DRIFT=WINDING-AT-%s-OF-%s-FAMILIES-UNDER-%s-OF-%s-TIE-"
                      "READING-PAIRS(BEST-OTHER=%s-OF-%s;STENCIL-BLIND-SO-%s-OF-"
                      "%s-FULL-READINGS);IDENTITY=ARENA-INSTRUMENT-FAILS-AT-MU-"
                      "%s-WINDING=%s-VS-DRIFT=%s;NONZERO-WINDING=%s-OF-%s-ALL-"
                      "MONOMIAL-OF-%s;NON-MONOMIAL=%s-MOVING=%s;ZERO-NET-"
                      "TRANSPORT-AT-SELECTED-READING=%s;READING-INDEPENDENT-ZERO-"
                      "DRIFT=%s-OF-%s;READING-INDEPENDENT-ZERO-WINDING=%s-OF-%s;"
                      "DIAGONAL-DEFECT-NONZERO=%s-INHERITED;MARKOV=%s-OF-%s-"
                      "NONZERO-INHERITED"
         % (c["drift_winding_matched"], c["families"],
            c["reading_pairs_with_identity"], c["reading_pairs"],
            c["drift_winding_mismatched"], c["families"],
            c["full_readings_with_identity"], c["full_readings"],
            c["witness_root_order"], c["witness_winding"], c["witness_drift"],
            c["nonzero_winding"], c["families"], c["monomial"],
            c["interfering"], c["interfering_moving"], c["interfering_zero_net"],
            c["zero_drift_all_readings"], c["interfering"],
            c["zero_winding_all_readings"], c["interfering"],
            c["diagonal_defect_nonzero"], c["markov_nonzero"],
            c["markov_pairs"])),
        ("SCOPE", "D=%s;L=%s;FIELD=%s;ALPHABET=%s;GENERATORS=%s;STENCIL=%s;SECTOR=%s;"
                  "MOMENTUM-LATTICE=DUAL-TORUS-%s-DECLARED;VELOCITY-READING=%s"
                  "(STENCIL-FORCED-TO-%s;LIFT-SELECTED-BY-AN-ARENA-INSTRUMENT;"
                  "RESIDUAL-FIBER=%s);CHARACTER-CONVENTION=DECLARED-JOINTLY-WITH-"
                  "VELOCITY-SIGN(FIBER=%s);CONNECTIVE=%s(FORCED-BY-"
                  "ANCHORED-LINK-%s);INDIVISIBILITY=%s;FINITE-LATTICE-ONLY;"
                  "NO-CONTINUUM-CLAIM;NO-INTERACTING-THEORY-CLAIM-BEYOND-THE-"
                  "COMPOSED-SEGMENT-DEFECT"
         % (c["d"], c["L"], c["field"], c["alphabet"], c["pool"], c["stencil"],
            c["sector"], c["momenta"], c["velocity_definition"],
            c["stencil_admitted"], c["residual_fiber"],
            c["character_convention_fiber"], c["connective_tag"],
            c["forcing_link"], c["indivisibility"])),
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
               + g("unit_modulus") + ";ALGEBRAIC-INTEGERS=" + g("algebraic_integers")
               + ";PARITY-INVARIANT=" + g("parity_invariant")
               + "-OF-" + g("families") + ";DISTINCT-REDUCED-PROFILES="
               + g("distinct_profiles") + "-OF-" + g("families")
               + "-FAMILIES(FORCED-BY-INVERTIBILITY);CLASS-SEPARATION="
               + g("class_separation_multisets") + "-OF-" + g("classes_circulant")
               + "-CIRCULANT-BY-DISPERSION-MULTISET-VS-" + g("class_labels")
               + "-LABELS-FOR-" + g("classes_extended") + "-CLASSES")
    out.append("VELOCITY=SPECTRUM=" + "+".join(c["speed_spectrum"]) + ";VMAX="
               + g("vmax") + ";INTEGER-VALUED=" + g("integer_velocities") + "-OF-"
               + g("velocity_cells") + ";ALIASED=" + g("aliased_cells") + "-OF-"
               + g("velocity_cells") + "-IN-" + g("aliased_families")
               + "-FAMILIES;DEFINITION=" + g("velocity_definition") + "(FIBER="
               + g("velocity_fiber") + ";STENCIL-FORCED-TO-" + g("stencil_admitted")
               + "-BY-MONOMIAL-NORMALISATION-AT-"
               + g("stencil_normalisation_coordinates") + "-OF-"
               + g("stencil_normalisation_coordinates")
               + ";LIFT-SELECTED-1-OF-3-BY-DRIFT=WINDING;RESIDUAL-FIBER="
               + g("residual_fiber") + "-MEASURED-INERT-DIFFERING-AT-"
               + g("residual_fiber_cells_differing") + "-OF-" + g("velocity_cells")
               + "-SIGNED-CELLS)")
    out.append("BOUND=NO-CONTENT=" + ("YES" if not c["bound_has_content"] else "NO")
               + ";CONE-AT-ONE-STEP=" + g("cone_sites_one_step") + "-OF-" + g("sites")
               + "-SITES;VMAX=" + g("vmax") + "=DIAMETER=" + g("diameter")
               + "(CEILING-FORCED;ATTAINMENT-MEASURED;STRUCTURAL-AT-EVERY-EVEN-L-AT-"
               + g("structural_sizes") + "-SIZES);REACH-UPPER-BOUND-FALSE-AT="
               + g("reach_over") + "-OF-" + g("families")
               + ";REACH-LOWER-BOUND-FALSE-AT=" + g("reach_under") + "-OF-"
               + g("families") + ";SATURATES-AT="
               + g("reach_equal") + ";INHERITED-CEILINGS=SEPARATIONS="
               + g("separations") + "-OF-" + g("separations_ceiling")
               + ";MAX-DEFECT-RADIUS=" + g("max_defect_radius") + "-OF-"
               + g("radius_ceiling") + ";INTERIOR-RADII="
               + "+".join([str(x) for x in c["interior_radii"]]) + "-HERE-"
               + g("interior_radii_at_l8") + "-AT-L-8;RESIDUAL-FIBER-INVARIANT=YES")
    out.append("TRANSPORT=DRIFT=WINDING-AT-" + g("drift_winding_matched") + "-OF-"
               + g("families") + "-FAMILIES-UNDER-"
               + g("reading_pairs_with_identity") + "-OF-" + g("reading_pairs")
               + "-TIE-READING-PAIRS(BEST-OTHER=" + g("drift_winding_mismatched")
               + "-OF-" + g("families") + ";STENCIL-BLIND-SO-"
               + g("full_readings_with_identity") + "-OF-" + g("full_readings")
               + "-FULL-READINGS);IDENTITY=ARENA-INSTRUMENT-FAILS-AT-MU-"
               + g("witness_root_order") + "-WINDING=" + g("witness_winding")
               + "-VS-DRIFT=" + g("witness_drift") + ";NONZERO-WINDING="
               + g("nonzero_winding") + "-OF-" + g("families") + "-ALL-MONOMIAL-OF-"
               + g("monomial") + ";NON-MONOMIAL=" + g("interfering") + "-MOVING="
               + g("interfering_moving") + ";ZERO-NET-TRANSPORT-AT-SELECTED-READING="
               + g("interfering_zero_net") + ";READING-INDEPENDENT-ZERO-DRIFT="
               + g("zero_drift_all_readings") + "-OF-" + g("interfering")
               + ";READING-INDEPENDENT-ZERO-WINDING="
               + g("zero_winding_all_readings") + "-OF-" + g("interfering")
               + ";DIAGONAL-DEFECT-NONZERO=" + g("diagonal_defect_nonzero")
               + "-INHERITED;MARKOV=" + g("markov_nonzero") + "-OF-"
               + g("markov_pairs") + "-NONZERO-INHERITED")
    out.append("SCOPE=D=" + g("d") + ";L=" + g("L") + ";FIELD=" + g("field")
               + ";ALPHABET=" + g("alphabet") + ";GENERATORS=" + g("pool")
               + ";STENCIL=" + g("stencil") + ";SECTOR=" + g("sector")
               + ";MOMENTUM-LATTICE=DUAL-TORUS-" + g("momenta")
               + "-DECLARED;VELOCITY-READING=" + g("velocity_definition")
               + "(STENCIL-FORCED-TO-" + g("stencil_admitted")
               + ";LIFT-SELECTED-BY-AN-ARENA-INSTRUMENT;RESIDUAL-FIBER="
               + g("residual_fiber") + ");CHARACTER-CONVENTION=DECLARED-JOINTLY-"
               + "WITH-VELOCITY-SIGN(FIBER=" + g("character_convention_fiber")
               + ");CONNECTIVE=" + g("connective_tag")
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


def census_rows(S):
    """the PUBLISHED census rows, rendered from the state.  Called once by the
    receipt builder and once, independently, by G-PUBLISHED-ROWS-BOUND, which
    compares the emitted table against a fresh rendering field by field: a row
    that carries a control's datum under a census label, or one field moved in
    one row, is caught at emission (#87 extended from the objects to the
    rows)."""
    disp, sigma, name = S["_dispersion"], S["_sigma"], S["_name"]
    duals = S["_duals"]
    rows = []
    for g in S["_pool"][:S["_ncirc"]]:
        n = name[g["local"]]
        if g["kind"] != "CIRC" or g["coef"] is None:
            raise GateFail("G-PUBLISHED-ROWS-BOUND :: a control reached the "
                           "census table :: %s" % g["local"])
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
    return rows


def build_receipt(S, LD):
    rows = census_rows(S)
    duals = S["_duals"]
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
        "support_drift_tables": S["supp_tables"],
        "agreement_matrix": S["agreement_matrix"],
        "agreement_matrix_full": S["agreement_matrix_full"],
        "stratification": S["stratification"],
        "profiles": S["profiles"],
        "source_sha256": hashlib.sha256(source_text().encode("utf-8")).hexdigest(),
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
    ("MUT-QUOTE-TRUNCATE", "G-VERBATIM-WINDOW-DIGESTS", "shortens every "
     "verbatim window to a four-byte decoration"),
    ("MUT-QUOTE-AMBIGUOUS", "G-VERBATIM-WINDOWS-UNIQUE", "reports a window "
     "that matches its source in more than one place"),
    ("MUT-INTEGRALITY", "G-MU8-THEOREM-LEGS", "admits a symbol that is not an "
     "algebraic integer"),
    ("MUT-STENCIL-CENTRAL", "G-STENCIL-FORCED-BY-NORMALISATION", "admits the "
     "central stencil the declared normalisation rejects"),
    ("MUT-RESIDUAL-FIBER", "G-RESIDUAL-FIBER-INERT", "perturbs one family "
     "under the backward stencil"),
    ("MUT-STRUCTURAL-L", "G-CONE-VACUITY-STRUCTURAL", "breaks the VMAX = "
     "diameter theorem at one lattice size"),
    ("MUT-REACH-DIRECTION", "G-REACH-BOUND-DIRECTION", "falsifies the UPPER "
     "bound with the undershooting families"),
    ("MUT-DRIFT-ALT", "G-EFFECTUS-DRIFT-TABLE", "makes the positive reading "
     "reproduce the review's rows too"),
    ("MUT-ARENA-WITNESS", "G-ARENA-ARTIFACT-WITNESS", "claims the identity "
     "survives the widened alphabet"),
    ("MUT-ROBUSTNESS", "G-CANCELLATION-ROBUSTNESS", "miscounts the "
     "reading-independent zeros"),
    ("MUT-DEFECT-BINDING", "G-NON-MONOMIAL-DEFECT-BOUND", "unbinds a "
     "non-monomial from its diagonal defect row"),
    ("MUT-CLASS-MULTISET", "G-CLASS-SEPARATION-BY-MULTISET", "miscounts the "
     "dispersion multisets"),
    ("MUT-NOTBLOCH-FORCED", "G-NOT-BLOCH-FORCED", "breaks the "
     "stabiliser-to-diagonality forcing"),
    ("MUT-ROW-FIELD", "G-PUBLISHED-ROWS-BOUND", "moves one field in one "
     "published census row"),
    ("MUT-ROW-SWAP", "G-PUBLISHED-ROWS-BOUND", "publishes a control's datum "
     "under a census label"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE", "mutates a sealed object after its "
     "gate has passed"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY", "declares a negator the "
     "paper's claim window carries"),
    ("MUT-PAPER-OCCURRENCES", "G-PAPER-CLAIM-POLARITY", "expects a claim "
     "occurrence count the paper does not have"),
    ("MUT-VERIFY-PAPER-DEAD", "G-VERIFY-PAPER-LIVE", "makes --verify-paper "
     "swallow its argument"),
    ("MUT-HEAD-THIRD-OUTCOME", "G-HEAD-LAW-RESPONSIVE", "makes the head law's "
     "BLOCKED branch unreachable"),
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
                if not mut("MUT-VERIFY-PAPER-DEAD"):
                    opts["verify_paper"] = argv[i + 1]
                i += 1
            # a documented flag that swallows its argument is the #82 disease
            # in its next dress: the PATH is resolved and required to exist
            p = opts["verify_paper"]
            if not os.path.exists(p if os.path.isabs(p)
                                  else os.path.join(REPO, p)):
                raise CliError("no such paper %r" % p)
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
    "5": "the section numbers, and the programme's false-claim register count "
         "as the parent's adjudication left it; section 12",
    "7": "the section numbers",
    "9": "the section numbers",
    "10": "the section numbers",
    "11": "the section numbers",
    "12": "the section numbers",
    "1/2": "the coefficient moduli of the declared alphabet, quoted from the "
           "parent's construction; section 2",
    "3/2": "the tokenizer's reading of sqrt3/2, the second coefficient of the "
           "widened-alphabet scope witness, quoted from the parent panel's "
           "construction; section 7",
    "6": "the section numbers and the six declared controls, which the pool "
         "counts render as 4 brickwork plus 2 scrambled; sections 2 and 5",
    "15": "this paper's number in the programme; the header, and the RUNBOOK "
          "section this unit's scope discipline cites in sections 7 and 12",
}

# --- #20, the polarity half ------------------------------------------------
# The numeral instrument is complete and blind to DIRECTION: a sentence can be
# inverted wherever its claim string also occurs elsewhere, and freely wherever
# the inversion introduces no new numeral.  Two declared legs close that.
#
# (1) EXPECTED_OCCURRENCES: a claim must occur the number of times the
#     instrument expects, so an inversion that survives on a second occurrence
#     is caught by the count.
# (2) POLARITY_GUARDS: for the polarity-bearing claims, a declared list of
#     negators that must not appear in a fixed window before the claim.
POLARITY_WINDOW = 64

EXPECTED_OCCURRENCES = {
    "moving": 3, "moving_bold": 1, "classes_moving": 1,
    "classes_moving_lower": 2, "monomial_only": 1, "interfering_move": 2,
    "notbloch": 2, "spectrum": 1, "vmax": 3,
}

POLARITY_GUARDS = [
    ("moving", ("fail", "not ", "never")),
    ("moving_bold", ("fail", "not ", "never")),
    ("classes_moving", ("fail", "not ", "never")),
    ("classes_moving_lower", ("fail", "not ", "never")),
    ("monomial_only", ("non-", "fail", "never")),
    ("interfering_move", ("fail", "never")),
]


def paper_polarity(R, txt):
    """the polarity instrument: every declared claim must occur the expected
    number of times, and no polarity-bearing claim may sit inside a window
    carrying a declared negator."""
    cl = paper_claims(R)
    flat = re.sub(r"\s+", " ", txt)
    if mut("MUT-PAPER-POLARITY"):
        # the inversion the numeral instrument cannot see: a negator inserted
        # in front of a claim that carries no new numeral
        k0 = POLARITY_GUARDS[0][0]
        v0 = re.sub(r"\s+", " ", cl[k0])
        flat = flat.replace(v0, "fail to " + v0, 1)
    exp = dict(EXPECTED_OCCURRENCES)
    if mut("MUT-PAPER-OCCURRENCES"):
        exp["moving"] = exp["moving"] + 1
    miscounted, inverted = [], []
    for k, want in sorted(exp.items()):
        if k not in cl:
            miscounted.append(k)
            continue
        got = flat.count(re.sub(r"\s+", " ", cl[k]))
        if got != want:
            miscounted.append("%s:%d!=%d" % (k, got, want))
    guards = list(POLARITY_GUARDS)
    for k, negators in guards:
        if k not in cl:
            inverted.append(k)
            continue
        v = re.sub(r"\s+", " ", cl[k])
        start = 0
        while True:
            at = flat.find(v, start)
            if at < 0:
                break
            window = flat[max(0, at - POLARITY_WINDOW):at].lower()
            for neg in negators:
                if neg in window:
                    inverted.append("%s@%d:%r" % (k, at, neg))
            start = at + 1
    return {"claims_with_expected_occurrences": len(exp),
            "polarity_guarded_claims": len(POLARITY_GUARDS),
            "window": POLARITY_WINDOW,
            "miscounted": sorted(miscounted), "inverted": sorted(inverted)}


def paper_claims(R):
    c = R["counts"]
    cl = {
        "families": "58 circulant families",
        "momenta": "16 momenta",
        "cells": "%d (family, momentum) cells" % c["cells"],
        "moving": "%d of %d families MOVE" % (c["moving"], c["families"]),
        "moving_bold": "**%d of %d families MOVE**" % (c["moving"], c["families"]),
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
        "interfering": "%d non-monomial families" % c["interfering"],
        "interfering_move": "all %d of them MOVE" % c["interfering"],
        "monomial": "%d monomial families" % c["monomial"],
        "monomial_only": "precisely this unit's %d monomial families"
                         % c["monomial"],
        "markov": "0 of 1792",
        "classes": "%d extended classes" % c["classes_extended"],
        "classes_moving": "%d of the %d circulant classes MOVE"
                          % (c["classes_moving"], c["classes_circulant"]),
        "classes_moving_lower": "%d of the %d circulant classes move"
                                % (c["classes_moving"], c["classes_circulant"]),
        "notbloch": "%d classes carry no Bloch dispersion" % c["classes_not_bloch"],
        "drift_table": "16 | 12", "drift_table2": "18 | 0", "drift_table3": "24 | 0",
        "drift_table_alt": "16 | 15, 18 | 10 and 24 | 8",
        "identity_pairs": "1 of the 9 tie-reading pairs",
        "identity_full": "%d of the %d readings"
                         % (c["full_readings_with_identity"], c["full_readings"]),
        "normalisation": "%d of %d non-antipodal monomial coordinates"
                         % (c["stencil_normalisation_coordinates"],
                            c["stencil_normalisation_coordinates"]),
        "stencil_forced": "forced to %d" % c["stencil_admitted"],
        "residual": "residual fiber is %d" % c["residual_fiber"],
        "residual_cells": "%d of %d cells" % (c["residual_fiber_cells_differing"],
                                              c["velocity_cells"]),
        "witness": "the Born drift is %s and the winding is %s"
                   % (c["witness_drift"], c["witness_winding"]),
        "identity_polarity": "the identity %s" % c["witness_identity"].lower(),
        "bound_polarity": "propagation bound is %s"
                          % ("empty" if not c["bound_has_content"]
                             else "carrying content"),
        "residual_polarity": "measured %s" % c["residual_fiber_inert"].lower(),
        "witness_field": "exact in Z/%d" % c["witness_root_order"],
        "robust_drift": "%d of the %d in position space"
                        % (c["zero_drift_all_readings"], c["interfering"]),
        "robust_winding": "%d of the %d on the dual torus"
                          % (c["zero_winding_all_readings"], c["interfering"]),
        "reach_upper": "%d families overshoot" % c["reach_over"],
        "reach_lower": "%d fall below" % c["reach_under"],
        "structural": "L in {4, 6, 8, 10, 12}",
        "interior_l8": "one here, %d at L = 8" % c["interior_radii_at_l8"],
        "class_separation": "%d of %d circulant classes"
                            % (c["class_separation_multisets"],
                               c["classes_circulant"]),
        "integrality": "all %d symbols are algebraic integers"
                       % c["algebraic_integers"],
        "diag_defect": "%d of %d" % (c["diagonal_defect_nonzero"],
                                     c["interfering"]),
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
            "gates_in_receipt": "%d of them evaluated inside the receipt"
                                % t["gates_in_receipt"],
            "gates_falsifiable": "%d carrying their own injection falsifier and "
                                 "%d their registered forcing"
                                 % (t["gates_falsifiable"], t["gates_waived"]),
            "mutants": "%d declared mutants" % t["mutants"],
            "anchors": "%d anchors" % t["anchors"],
            "byte_anchors": "%d file-bytes anchors" % t["byte_anchors"],
            "pv_anchors": "%d path-value anchors" % t["path_value_anchors"],
            "vb_anchors": "%d verbatim-text anchors" % t["verbatim_anchors"],
            "seals": "%d sealed objects" % t["seals"],
        })
    # the claims that render from the CLOSED totals exist only at the FINAL
    # coverage gate: the mutant sweep's own result cannot be known before it
    if "mutants_killed" in t:
        cl.update({
            "mutants_dead": "%d declared mutants, all dead" % t["mutants_killed"],
        })
    if mut("MUT-PAPER-CLAIM"):
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
    for tbl in R["support_drift_tables"].values():
        for k, v in tbl.items():
            rendered |= {k, str(v["generators"]), str(v["nonzero_drift"])}
    rendered |= {str(v) for v in R["agreement_matrix"].values()}
    rendered |= {str(v) for v in R["agreement_matrix_full"].values()}
    rendered |= {str(v) for v in R["resolution"].values() if isinstance(v, int)}
    st = R["stratification"]
    for row in st["stencil_normalisation"]:
        rendered |= {str(row["satisfied"]), str(row["coordinates"])}
    for row in st["structural_vmax"]:
        rendered |= {str(row["L"]), str(row["diameter"]),
                     row["antipodal_monomial_speed"],
                     str(row["interior_radius_count"])}
        rendered |= {str(x) for x in row["interior_radii"]}
    for blk in (st["residual_fiber"], st["central_stencil_disclosure"],
                st["cancellation_robustness"], st["class_separation"],
                st["reach_direction"], st["defect_binding"],
                st["arena_artifact_witness"]):
        for v in blk.values():
            if isinstance(v, bool):
                continue
            if isinstance(v, int):
                rendered.add(str(v))
            elif isinstance(v, str):
                rendered |= set(re.findall(NUMERAL_RE, v))
            elif isinstance(v, list):
                for x in v:
                    if isinstance(x, int):
                        rendered.add(str(x))
                    elif isinstance(x, str):
                        rendered |= set(re.findall(NUMERAL_RE, x))
    rendered |= {str(len(SOURCES)), str(len(PATH_VALUE_ANCHORS)),
                 str(len(VERBATIM_ANCHORS)), str(len(MUTANTS)),
                 str(len(SOURCES) + len(PATH_VALUE_ANCHORS) + len(VERBATIM_ANCHORS)),
                 str(len(LIFT_READINGS) * len(STENCIL_READINGS)),
                 str(len(LIFT_READINGS)), str(len(STENCIL_READINGS)),
                 str(len(STENCIL_FORCED)), str(len(STRUCTURAL_SIZES)),
                 str(len(SEALED_PATHS)), str(POLARITY_WINDOW)}
    rendered |= {str(v) for v in R["translation_stabilisers"].values()
                 if isinstance(v, int)}
    for v in R["translation_stabilisers"].values():
        if isinstance(v, list):
            rendered |= {str(x) for x in v}
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
    if mut("MUT-PAPER-NUMERAL"):
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
    SEAL = Seal()
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
    # THE SEAL, taken at the moment the gate passed.  Everything downstream of
    # this line is measured against these digests, never against R.
    SEAL.take("SEAL-VERDICT-STRING", R)
    SEAL.take("SEAL-VERDICT-HEAD", R)
    SEAL.take("SEAL-COUNTS", R)

    # the head law must be responsive, in ALL THREE of its outcomes
    zeroed = dict(c)
    zeroed["moving"] = 0
    zeroed["static"] = zeroed["families"]
    head_zeroed = ("R4B-DISPERSION-READ" if mut("MUT-HEAD-CONSTANT")
                   else derive_head(zeroed))
    blocked = dict(c)
    blocked["in_mu8"] = blocked["cells"] - 1
    head_blocked = ("R4B-DISPERSION-READ" if mut("MUT-HEAD-THIRD-OUTCOME")
                    else derive_head(blocked))
    LD.gate("G-HEAD-LAW-RESPONSIVE",
            "the head is named by the dispersion census and by nothing else, "
            "and ALL THREE of the law's outcomes are exercised rather than "
            "read off the source: with the moving count zeroed the law returns "
            "the pin's NO-MOTION outcome, and with one eigenvalue outside "
            "mu_8 it returns the pin's BLOCKED outcome -- the branch the "
            "census closes.  A head that cannot move is not this one",
            head_zeroed == "R4B-NO-MOTION" and head == "R4B-DISPERSION-READ"
            and head_blocked == "R4B-BLOCKED-AT-EIGENPHASE-OUTSIDE-MU-8",
            "head=%s; under a zeroed motion census=%s; under an eigenvalue "
            "outside mu_8=%s" % (head, head_zeroed, head_blocked))
    R["verdict"]["head_under_zeroed_census"] = head_zeroed
    R["verdict"]["head_under_eigenphase_outside_mu8"] = head_blocked

    # ---- the PUBLISHED rows, bound at emission (#87 extended) --------------
    fresh_rows = census_rows(S)
    if mut("MUT-ROW-FIELD"):
        R["dispersion_census"][1] = dict(R["dispersion_census"][1])
        R["dispersion_census"][1]["max_speed"] = "0"
    if mut("MUT-ROW-SWAP"):
        ctrl_row = S["_pool"][S["_ncirc"]]
        R["dispersion_census"][55] = dict(R["dispersion_census"][55])
        R["dispersion_census"][55]["radius"] = ctrl_row["radius"]
    circ_names = {S["_name"][g["local"]] for g in S["_pool"][:S["_ncirc"]]}
    ctrl_names = {S["_name"][g["local"]] for g in S["_pool"][S["_ncirc"]:]}
    published_bad = sorted(
        R["dispersion_census"][i]["family"]
        for i in range(len(fresh_rows))
        if R["dispersion_census"][i] != fresh_rows[i])
    class_fresh = [{"class": cc["rep"], "size": cc["size"], "kind": cc["kind"]}
                   for cc in S["_class_rows_src"]]
    class_bad = [r["class"] for r, f in zip(R["class_rows"], class_fresh)
                 if (r["class"], r["size"]) != (f["class"], f["size"])]
    anchor_bad = [a["id"] for a in R["path_value_anchors"]
                  if a["measured"] != jpath(S["_r4"], a["path"])]
    LD.gate("G-PUBLISHED-ROWS-BOUND",
            "the rows the artifact SHIPS are bound to the state that produced "
            "them, field by field: every published census row is re-rendered "
            "from the state and compared entry for entry, the class table is "
            "re-derived from the rebuilt partition, and every path-value "
            "anchor's measured value is re-read from the parent's receipt at "
            "its frozen path.  No published row may carry a control's datum "
            "under a census label, and no field may move after the object "
            "gates closed",
            not published_bad and not class_bad and not anchor_bad
            and len(R["dispersion_census"]) == len(fresh_rows)
            and {r["family"] for r in R["dispersion_census"]} == circ_names
            and not ({r["family"] for r in R["dispersion_census"]} & ctrl_names),
            "rows differing from a fresh rendering %s over %d; class rows %s; "
            "path-value anchors %s"
            % (published_bad or "none", len(fresh_rows), class_bad or "none",
               anchor_bad or "none"))
    for sid, _p, gname in SEALED_PATHS:
        if gname == "G-PUBLISHED-ROWS-BOUND":
            SEAL.take(sid, R)

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
        # the receipt can carry every gate but the terminal integrity gate,
        # which is evaluated in the writing path -- after the payload it
        # verifies has been serialized.  The count says so rather than
        # anticipating it (the delivered figure is what was EVALUATED here).
        "gates_in_receipt": len(LD.rows) + PENDING_GATES - 1,
        "integrity_gate": "EVALUATED-IN-THE-WRITING-PATH-AGAINST-THE-GATE-TIME-"
                          "SEAL-REPORTED-ON-STDOUT",
        "gates_waived": len(FORCINGS),
        "gates_falsifiable": len(LD.rows) + PENDING_GATES - len(FORCINGS),
        "anchors": len(SOURCES) + len(PATH_VALUE_ANCHORS) + len(VERBATIM_ANCHORS),
        "byte_anchors": len(SOURCES),
        "path_value_anchors": len(PATH_VALUE_ANCHORS),
        "verbatim_anchors": len(VERBATIM_ANCHORS),
        "mutants": len(MUTANTS),
        "seals": len(SEALED_PATHS),
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
    pol = paper_polarity(R, paper_text)
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "the paper-claim instrument is given DIRECTION: every declared "
            "claim must occur the number of times the receipt expects -- so an "
            "inversion that survives on a second occurrence of the same string "
            "is caught by the count -- and no polarity-bearing claim may sit "
            "behind a declared negator.  A numeral-complete check is blind to "
            "an inverted sentence that introduces no numeral; this is not",
            not pol["miscounted"] and not pol["inverted"],
            "miscounted %s; inverted %s; %d counted claims, %d guarded"
            % (pol["miscounted"] or "none", pol["inverted"] or "none",
               pol["claims_with_expected_occurrences"],
               pol["polarity_guarded_claims"]))
    R["paper_coverage"] = cov
    R["paper_polarity"] = pol
    R["paper_claims"] = paper_claims(R)

    # ---- the CLI -----------------------------------------------------------
    probes = []
    for argv, want_reject in ((["--not-a-flag"], True), (["--mutant"], True),
                              (["--mutant", "NOPE"], True),
                              (["--break-anchor", "NOPE"], True),
                              (["--break-anchor"], True),
                              (["--no-write"], False), (["--selftest"], False),
                              (["--verify-paper"], False),
                              (["--verify-paper", PAPER_REL], False),
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
    vp_default = parse_args(["--verify-paper"])["verify_paper"]
    vp_named = parse_args(["--verify-paper", SOURCES[7][1]])["verify_paper"]
    LD.gate("G-VERIFY-PAPER-LIVE",
            "--verify-paper is not a documented no-op: the parser carries the "
            "PATH it was given rather than swallowing it, a PATH that does not "
            "exist is rejected before any run begins, and the flag's run "
            "evaluates the same paper gates the delivery run does",
            vp_default == PAPER_REL and vp_named == SOURCES[7][1]
            and cli_error_probe(parse_args, ["--verify-paper", "v14/NOPE.md"]),
            "default=%s; named path carried=%s; nonexistent path rejected"
            % (vp_default, vp_named))
    R["cli_probes"] = probes

    # ---- coverage of the ledger itself ------------------------------------
    targeted = {m[1] for m in MUTANTS}
    evaluated = ({r["gate"] for r in LD.rows} | set(POST_LOOP_GATES)
                 | {"G-GATE-MUTANT-COVERAGE", "G-WAIVERS-VERIFIED",
                    "G-ANCHOR-CONSUMERS-EXIST", "G-SEAL-COMPLETE"})
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
    SEAL.take("SEAL-WAIVERS", R)

    # ---- THE GATE-TO-DISK SEAL, in-run half --------------------------------
    if mut("MUT-SEAL-BROKEN"):
        R["counts"] = dict(R["counts"])
        R["counts"]["moving"] = 0        # the post-gate window, exercised
    broken = SEAL.verify(R)
    LD.gate("G-SEAL-COMPLETE",
            "every object this run will publish was DIGESTED AT THE MOMENT ITS "
            "GATE PASSED, and every one of those digests still describes the "
            "object now: a gate that fires on something still mutable when the "
            "artifact is built has not gated the artifact.  The seals taken "
            "before the mutant sweep are enumerated against the frozen "
            "declaration and re-verified here; the remainder are sealed at "
            "their own gates and checked against the BYTES ON DISK by the "
            "terminal integrity gate",
            not broken
            and sorted(r["seal"] for r in SEAL.rows) == sorted(SEALS_IN_RUN),
            "seals taken %d of %d declared; broken %s"
            % (len(SEAL.rows), len(SEALED_PATHS), broken or "none"))
    R["seals"] = SEAL.rows
    return R, Rjson, SEAL


POST_LOOP_GATES = ("G-MUTANTS-ON-TARGET", "G-ARTIFACT-INTEGRITY",
                   "G-PAPER-COVERAGE-FINAL")

# the gates still to be evaluated when the totals are predicted, counted from
# the declaration site: the three in-run paper gates (claims, numerals,
# polarity), the CLI trio (contract, selftest-writes-nothing, verify-paper),
# the three ledger-coverage gates (mutant coverage, anchor consumers, waivers),
# the seal gate, then -- outside this function -- the mutant adjudication, the
# final paper gate and the terminal integrity gate.  The prediction is verified
# against the count actually reached, in both directions.
PENDING_GATES = 13


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
    whose PREDICATE argument reads the mutant switch -- BY EITHER SHAPE: a call
    to mut(...), or a bare load of the MUT global, which is the bypass the
    call-shaped scan misses.  A gate that exempts its own falsifier is the
    laundering shape and is named here."""
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
                if (isinstance(sub, ast.Name) and sub.id == "MUT"
                        and isinstance(sub.ctx, ast.Load)):
                    bad.append(gid)
    return sorted(set(bad))


# ===========================================================================
# SECTION 10.  REPORT
# ===========================================================================

def emit_report(R, S, SEAL):
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
    say("  translation stabilisers %s" % R["translation_stabilisers"])
    say("  the instrument that produced this receipt: %s"
        % R["source_sha256"][:12])
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
    say("THE VELOCITY READING, STRATIFIED")
    st = R["stratification"]
    say("  the declared normalisation (a monomial shift by o has velocity o), "
        "by stencil:")
    for row in st["stencil_normalisation"]:
        say("    %-9s %d of %d non-antipodal monomial coordinates   %s"
            % (row["stencil"], row["satisfied"], row["coordinates"],
               "ADMITTED" if row["admitted"] else "REJECTED"))
    say("  stencil FORCED to %s; lift SELECTED by the identity; residual fiber "
        "%d" % (st["stencil_admitted"], st["residual_fiber"]["residual_fiber"]))
    say("  the residual fiber, measured inert: %s" % st["residual_fiber"])
    say("  what the rejected stencil would have said: %s"
        % st["central_stencil_disclosure"])
    say("  VMAX = diameter, at every even L:")
    for row in st["structural_vmax"]:
        say("    L=%-3d diameter %d  antipodal monomial speed %s  interior "
            "radii %s" % (row["L"], row["diameter"],
                          row["antipodal_monomial_speed"],
                          row["interior_radii"]))
    say("  the reach bound, by direction: %s" % st["reach_direction"])
    say("")
    say("TRANSPORT: THE DRIFT AND THE WINDING")
    for reading in LIFT_READINGS:
        say("  support -> [generators, nonzero drift] under the %-13s "
            "reading: %s" % (reading, R["support_drift_tables"][reading]))
    say("  drift == winding, by tie-reading pair:")
    for k in sorted(R["agreement_matrix"]):
        say("    drift %-13s vs winding %-13s : %d of %d"
            % tuple(k.split("|") + [R["agreement_matrix"][k], c["families"]]))
    say("  over the %d lift x lift x stencil readings the identity holds at %d"
        % (c["full_readings"], c["full_readings_with_identity"]))
    say("  THE SCOPE WITNESS (the identity is an arena instrument): %s"
        % st["arena_artifact_witness"])
    say("  nonzero winding %d, all monomial (of %d monomial families)"
        % (c["nonzero_winding"], c["monomial"]))
    say("  non-monomial families %d: all MOVING (%d), all with zero net "
        "transport at the selected reading (%d)"
        % (c["interfering"], c["interfering_moving"], c["interfering_zero_net"]))
    say("  the zero, stratified by the tie: %s" % st["cancellation_robustness"])
    say("  the word bound to the parent's rows: %s" % st["defect_binding"])
    say("  the like-for-like class separation: %s" % st["class_separation"])
    say("  inherited: the Markovian control is %d of %d nonzero"
        % (c["markov_nonzero"], c["markov_pairs"]))
    say("")
    say("PAPER CLAIM COVERAGE")
    say("  %s" % R["paper_coverage"])
    say("  polarity %s" % R["paper_polarity"])
    say("")
    say("THE GATE-TIME SEAL")
    for row in R["seals"]:
        say("  %-22s %-24s sealed at %-26s %s"
            % (row["seal"], row["path"], row["sealed_at_gate"],
               row["sha256_12"]))
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
    say("ALL GATES PASSED (%d/%d IN THE RECEIPT; the last of the %d declared "
        "is the terminal integrity gate, evaluated in the writing path); ALL "
        "MUTANTS DEAD (%d/%d)"
        % (R["totals"]["gates_passed_in_receipt"], R["totals"]["gates_in_receipt"],
           R["totals"]["gates"], R["totals"]["mutants_killed"],
           R["totals"]["mutants"]))
    say("EXIT 0")
    # the transcript is sealed AT THE MOMENT IT IS COMPOSED, so there is no
    # window between the last line written and the digest the writer is
    # measured against
    SEAL.close_transcript("\n".join(LOG) + "\n")


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
    "the alphabet is NOT widened as a census: the parent panel's "
    "motion-carrying generator over Q(i, sqrt 3) is rebuilt as a single SCOPE "
    "WITNESS -- one generator, in a second field used nowhere else -- to show "
    "that the selecting identity fails there.  No census is run over the wider "
    "field and no result of this unit is claimed for it",
    "the selection criterion's DOMAIN is not censused: one counterexample is "
    "exhibited, not a sweep, so whether the drift = winding identity fails "
    "generically over widened alphabets is open and is this unit's most "
    "consequential registered open",
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
    say("[9/10] the verdict, its reconstruction, the seal and the receipt gates")
    R, Rjson, SEAL = run_receipt_gates(S, LD, paper_text)
    return S, LD, R, Rjson, SEAL


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

    paper_rel = opts["verify_paper"] or PAPER_REL
    paper_path = (paper_rel if os.path.isabs(paper_rel)
                  else os.path.join(REPO, paper_rel))
    if opts["verify_paper"]:
        say("VERIFY-PAPER: the object under test is %s" % paper_rel)
    paper_text = read_text(paper_path) if os.path.exists(paper_path) else ""

    try:
        S, LD, R, Rjson, SEAL = full_run(opts["break_anchor"], paper_text)
    except GateFail as e:
        say("")
        say("GATE FAILED: %s" % e)
        say("EXIT 1")
        sys.exit(1)

    if opts["verify_paper"]:
        say("")
        say("VERIFY-PAPER: %s" % paper_rel)
        say("  coverage %s" % R["paper_coverage"])
        say("  polarity %s" % R["paper_polarity"])
        say("  every claim rendered, every numeral covered, every polarity "
            "held: the three paper gates passed on this file.")
        say("EXIT 0")
        sys.exit(0)

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

    R["mutants"] = report
    SEAL.take("SEAL-MUTANTS", R)
    R["gates"] = LD.rows
    R["not_executed"] = NOT_EXECUTED
    waivers = R["waiver_ledger"]

    R["totals"].update({
        "mutants_killed": sum(1 for m in report if m["killed"]),
        "mutants_on_target": on_target,
        "gates_passed_in_receipt": sum(1 for g in LD.rows if g["passed"]) + 1,
    })

    # THE PREDICTION CLOSES.  The gate count was declared BEFORE the paper
    # gates ran; it must be exactly the count the run reaches.  One ledger row
    # is still to come -- the final paper gate below -- plus the integrity gate
    # that only the writing path evaluates and that the receipt therefore
    # cannot carry.
    if (R["totals"]["gates"] != len(LD.rows) + 2
            or R["totals"]["gates_in_receipt"] != len(LD.rows) + 1
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
    R["paper_polarity"] = paper_polarity(R, paper_text)
    R["paper_claims"] = paper_claims(R)
    R["gates"] = LD.rows
    SEAL.take("SEAL-GATES", R)
    SEAL.take("SEAL-TOTALS", R)
    SEAL.take("SEAL-COVERAGE", R)

    # THE PAYLOAD IS SEALED HERE, at the moment the last receipt gate passed,
    # and only if every earlier seal still verifies.  Nothing below this line
    # can reach the bytes that will be written.
    SEAL.close(R, json.dumps(R, indent=1, sort_keys=True))
    emit_report(R, S, SEAL)

    if write:
        payload, text = SEAL.payload, SEAL.transcript
        # THE FINAL INTEGRITY GATE, two-way, AGAINST THE SEAL.  First the
        # negative control: a deliberately corrupted payload is written to a
        # probe path and re-read, and the comparator must NOTICE.  Then the
        # artifacts are written to temporaries, re-read, and required to match
        # the GATE-TIME SEAL -- never a re-derivation from the bytes on disk,
        # which would confirm a corruption rather than catch it.  Only then are
        # the temporaries moved into place, and the final files are verified
        # again.  A failure leaves the previous artifacts untouched.
        probe_path = OUT_JSON + ".integrity-probe"
        with open(probe_path, "w", encoding="utf-8") as f:
            f.write(payload[:-1] + " }")
        detected = digest(read_text(probe_path)) != SEAL.payload_sha
        os.remove(probe_path)

        def against_the_seal(js, tx):
            if digest(js) != SEAL.payload_sha or digest(tx) != SEAL.transcript_sha:
                return False
            disk = json.loads(js)
            if SEAL.verify(disk):
                return False
            return (disk["verdict"]["string"] == SEAL.verdict_string
                    and reconstruct_from_serialized(js) == SEAL.verdict_string)

        tmp_json, tmp_txt = OUT_JSON + ".tmp", OUT_TXT + ".tmp"
        with open(tmp_json, "w", encoding="utf-8") as f:
            f.write(payload)
        with open(tmp_txt, "w", encoding="utf-8") as f:
            f.write(text)
        ok = detected and against_the_seal(read_text(tmp_json), read_text(tmp_txt))
        if not ok:
            os.remove(tmp_json)
            os.remove(tmp_txt)
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: what was about to be "
                  "written does not match the gate-time seal (corruption "
                  "detected=%s); nothing written" % detected, flush=True)
            sys.exit(1)
        os.replace(tmp_json, OUT_JSON)
        os.replace(tmp_txt, OUT_TXT)
        if not against_the_seal(read_text(OUT_JSON), read_text(OUT_TXT)):
            print("GATE FAILED: G-ARTIFACT-INTEGRITY :: the artifacts on disk "
                  "differ from the gate-time seal", flush=True)
            sys.exit(1)
        print("G-ARTIFACT-INTEGRITY: corrupted probe detected; both artifacts "
              "written from the SEALED payload, re-read from disk and matched "
              "against the gate-time seal -- %d sealed objects, payload %s, "
              "transcript %s (%d + %d bytes)."
              % (len(SEAL.rows), SEAL.payload_sha, SEAL.transcript_sha,
                 len(payload), len(text)), flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
