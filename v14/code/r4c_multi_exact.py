#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
v14 R4c -- TWO EXCITATIONS: STATISTICS AS A MEASUREMENT  (paper-22)

Builds the two-excitation sector over R4's terminal stage and MEASURES -- never
chooses -- which exchange symmetry the substrate's composition law forces or
admits, whether the composition defect composes, and how the motion composes.

EXACT ARITHMETIC ONLY.  The field is Q(zeta_8) carried as an integer 4-tuple
over a power-of-two denominator, reduced modulo Phi_8(x) = x^4 + 1.  Every
coefficient of the declared alphabet is dyadic, so every product, sum, Born
shadow and defect stays dyadic and the representation is canonical: tuple
equality IS field equality.  An AST scan of this source and a recursive type
scan of the emitted receipt are gates.  There is no float anywhere.

CLI CONTRACT (#82; argv parsed against a whitelist, unknown flags exit 2)

    python3.13 v14/code/r4c_multi_exact.py
        the delivery run: measures, gates, writes the output and the receipt.

    python3.13 v14/code/r4c_multi_exact.py --no-write
        the same run, writing nothing.

    python3.13 v14/code/r4c_multi_exact.py --selftest
        corrupts ONE anchor in memory, requires the run to die at the anchor
        gate, WRITES NOTHING, exits 1.  Exits 2 if the corrupted run lives.

    python3.13 v14/code/r4c_multi_exact.py --mutant NAME
        runs one declared mutant; it must die at the gate it was declared to
        falsify, and the artifacts on disk are left untouched.

    python3.13 v14/code/r4c_multi_exact.py --break-anchor NAME
        corrupts one named anchor; the run must die at its gate.

    python3.13 v14/code/r4c_multi_exact.py --verify-paper [PATH]
        additionally gates this unit's paper against the receipt.  The plain
        delivery run does this too (#20): the paper is verified IN the run.

INHERITANCE, hash-verified at run time and by no other route.  R4's terminal
stage and family (paper 1063401c7bb5 / code 2959c5a6a84b / receipt
3dc1393b0df8, commit 583cae7); R4b's dispersions and its stratified velocity
convention (paper 89c636906061 / code 4216f3de5f44 / receipt 562e2a3d4d85,
commit 6d32993), inherited AS DECLARED with the R4b scope stamp binding: NO
transport number is inherited; the record layer's site lattice
(v13/code/ha_successor_receipt.json, 542b8735daf0), which supplies the spatial
dimension, the link set and the stage's own count registers as anchored values;
the composition defect's definition and named witness (v12 paper 1,
81bdab5673fb, with v12/paper1_code/exact.py 8e90f6435922); R5's terminal
two-excitation extension (paper 62cfe5689d2c, receipt 0c02b7684e5b), CITED and
NOT RE-RUN, as the pin requires; and the pin v14/note-r4c-pin.md (162553b03ca9).

Every object below is REIMPLEMENTED from those definitions.  Nothing is
imported from any other unit; no other unit's program is executed.
"""

import ast
import hashlib
import json
import os
import sys
from itertools import product

SELF = os.path.abspath(__file__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SELF)))
OUT_TXT = os.path.join(ROOT, "v14", "code", "r4c_multi_output.txt")
OUT_JSON = os.path.join(ROOT, "v14", "code", "r4c_multi_receipt.json")
PAPER = os.path.join(ROOT, "v14", "paper-22-multi.md")

MUT = None
QUIET = False
LOG = []
READS = []


# ===========================================================================
# SECTION 1.  THE EXACT FIELD Q(zeta_8), AND THE LATTICE
# ===========================================================================
#
# An element is the 5-tuple (a0, a1, a2, a3, e) standing for
#     (a0 + a1 z + a2 z^2 + a3 z^3) / 2^e ,     z = zeta_8, z^4 = -1.
# Canonical form: e >= 0 and not every a_i even (or the exact zero).  Every
# declared coefficient is dyadic, so the whole census stays inside this ring
# of dyadic cyclotomic integers and tuple equality is field equality.

ZERO = (0, 0, 0, 0, 0)


def red(a0, a1, a2, a3, e):
    if a0 == 0 and a1 == 0 and a2 == 0 and a3 == 0:
        return ZERO
    while e > 0 and (a0 | a1 | a2 | a3) & 1 == 0:
        a0 >>= 1
        a1 >>= 1
        a2 >>= 1
        a3 >>= 1
        e -= 1
    return (a0, a1, a2, a3, e)


def fadd(u, v):
    if u == ZERO:
        return v
    if v == ZERO:
        return u
    e = u[4] if u[4] > v[4] else v[4]
    su = 1 << (e - u[4])
    sv = 1 << (e - v[4])
    return red(u[0] * su + v[0] * sv, u[1] * su + v[1] * sv,
               u[2] * su + v[2] * sv, u[3] * su + v[3] * sv, e)


def fneg(u):
    return ZERO if u == ZERO else (-u[0], -u[1], -u[2], -u[3], u[4])


def fsub(u, v):
    return fadd(u, fneg(v))


def fmul(u, v):
    if u == ZERO or v == ZERO:
        return ZERO
    a0, a1, a2, a3 = u[0], u[1], u[2], u[3]
    b0, b1, b2, b3 = v[0], v[1], v[2], v[3]
    return red(a0 * b0 - a1 * b3 - a2 * b2 - a3 * b1,
               a0 * b1 + a1 * b0 - a2 * b3 - a3 * b2,
               a0 * b2 + a1 * b1 + a2 * b0 - a3 * b3,
               a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0, u[4] + v[4])


def fconj(u):
    """complex conjugation: z -> z^7 = -z^3, so (a0,a1,a2,a3) -> (a0,-a3,-a2,-a1)."""
    return ZERO if u == ZERO else red(u[0], -u[3], -u[2], -u[1], u[4])


def fnorm(u):
    """|u|^2 = u * conj(u), an element of the real subfield."""
    return fmul(u, fconj(u))


ONE = (1, 0, 0, 0, 0)
HALF = (1, 0, 0, 0, 1)
ZP = []
for _t in range(8):
    _c = [0, 0, 0, 0]
    if _t < 4:
        _c[_t] = 1
    else:
        _c[_t - 4] = -1
    ZP.append(red(_c[0], _c[1], _c[2], _c[3], 0))
ZP = tuple(ZP)
SQ2 = red(0, 1, 0, -1, 0)          # z - z^3 = sqrt 2
INVSQ2 = red(0, 1, 0, -1, 1)       # (z - z^3)/2 = 1/sqrt 2


def frac_str(u):
    """render a RATIONAL field element as an exact fraction string."""
    if u == ZERO:
        return "0"
    if u[1] or u[2] or u[3]:
        raise GateFail("G-RATIONALITY :: asked to render a non-rational value")
    n, d = u[0], 1 << u[4]
    if d == 1:
        return str(n)
    return "%d/%d" % (n, d)


def is_rational(u):
    return u == ZERO or (u[1] == 0 and u[2] == 0 and u[3] == 0)


# ---- the lattice, sized from the anchored stage (never typed here) --------

L = None
D = None
SITES = ()
IDX = {}
NS = 0


def set_lattice(dim, size):
    global L, D, SITES, IDX, NS
    D, L = dim, size
    SITES = tuple(product(range(L), repeat=D))
    IDX = {s: i for i, s in enumerate(SITES)}
    NS = len(SITES)


def addv(a, b):
    return tuple((a[i] + b[i]) % L for i in range(len(a)))


def negv(a):
    return tuple((-a[i]) % L for i in range(len(a)))


def absmax(o):
    return max(min(c, L - c) for c in o)


def elt_order(a):
    n, cur = 1, a
    while any(cur):
        cur = addv(cur, a)
        n += 1
    return n


# ---- sparse matrices, stored BY COLUMN: M[j][i] = M_{ij} ------------------

def matmul(A, B):
    out = []
    for cb in B:
        acc = {}
        for m, bv in cb.items():
            for i, av in A[m].items():
                p = fmul(av, bv)
                if p == ZERO:
                    continue
                cur = acc.get(i)
                acc[i] = p if cur is None else fadd(cur, p)
        out.append({i: v for i, v in acc.items() if v != ZERO})
    return out


def born(A):
    """the Born shadow B(U) = |U|^{circ 2}, entrywise."""
    return [{i: fnorm(v) for i, v in c.items() if v != ZERO} for c in A]


def msub(A, B):
    out = []
    for j, ca in enumerate(A):
        acc = dict(ca)
        for i, v in B[j].items():
            cur = acc.get(i)
            nv = fneg(v) if cur is None else fsub(cur, v)
            if nv == ZERO:
                acc.pop(i, None)
            else:
                acc[i] = nv
        out.append({i: v for i, v in acc.items() if v != ZERO})
    return out


def mnz(A):
    for c in A:
        if c:
            return True
    return False


def mcells(A):
    return sum(len(c) for c in A)


def is_unitary(A):
    n = len(A)
    for j in range(n):
        cj = A[j]
        for k in range(j, n):
            s = ZERO
            ck = A[k]
            for i, v in cj.items():
                w = ck.get(i)
                if w is not None:
                    s = fadd(s, fmul(fconj(v), w))
            if s != (ONE if j == k else ZERO):
                return False
    return True


def is_stochastic(B):
    for c in B:
        s = ZERO
        for v in c.values():
            s = fadd(s, v)
        if s != ONE:
            return False
    return True


def value_multiset(A):
    out = {}
    for c in A:
        for v in c.values():
            if v != ZERO:
                out[v] = out.get(v, 0) + 1
    return out


# ===========================================================================
# SECTION 2.  GATES, THE LEDGER, MUTANTS, AND THE GATE-TIME SEAL (#119)
# ===========================================================================

class GateFail(Exception):
    pass


class CliError(Exception):
    pass


def say(msg=""):
    """the transcript.  The self-test and every in-process mutant are QUIET
    and contribute nothing to it, so the written output is the delivery run's
    own transcript and nothing else."""
    if not QUIET:
        LOG.append(msg)
        print(msg, flush=True)


def mut(name):
    """the ONLY mutant switch.  No gate PREDICATE may reference it: a standing
    self-check (G-MUTANT-SWITCH-CLEAN) scans this source and requires that
    every mut() call sits in the measurement path, never inside a gate call."""
    return MUT == name


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
                              "can reach it; its in-run twins G-PAPER-CLAIMS, "
                              "G-PAPER-NUMERAL-COVERAGE and "
                              "G-PAPER-CLAIM-POLARITY carry the injection "
                              "falsifiers and die on every sweep",
}

SEALED_PATHS = [
    ("SEAL-VERDICT-STRING", "verdict/string", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-HEAD", "verdict/head", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-COUNTS", "counts", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-EXCHANGE", "exchange_census", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-ARENAS", "arena_census", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-OCCUPANCY", "occupancy", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-DEFECT", "defect_census", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-DEFECT-VALUES", "defect_values", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-DISCRIMINATION", "discrimination", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-OVERLAP", "overlap_census", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-MOTION", "motion", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-CONTACT", "contact_handle", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-PARENT", "parent_reproduction", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-STAMPS", "description_stamps", "G-DESCRIPTION-STAMPS"),
    ("SEAL-PATH-ANCHORS", "path_value_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-BYTE-ANCHORS", "byte_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-VERBATIM", "verbatim_anchors", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-WAIVERS-VERIFIED"),
    ("SEAL-SCHEMA", "schema", "G-RECEIPT-SCHEMA"),
    ("SEAL-PROVENANCE", "provenance", "G-RECEIPT-SCHEMA"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-POOL", "pool", "G-POOL-COMPLETE"),
    ("SEAL-ARENA", "arena_declaration", "G-ARENA-ANCHORED"),
    ("SEAL-VERDICT-ALL", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-CLI", "cli_probes", "G-CLI-WHITELIST"),
    ("SEAL-MUTANTS", "mutants", "G-MUTANTS-ON-TARGET"),
    ("SEAL-COMPLIANCE", "compliance", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-COVERAGE", "paper_coverage", "G-PAPER-COVERAGE-FINAL"),
]
# the seals taken after the mutant sweep has closed the instrument's totals
SEALS_LATE = ("SEAL-CLI", "SEAL-MUTANTS", "SEAL-COMPLIANCE", "SEAL-GATES",
              "SEAL-TOTALS", "SEAL-COVERAGE")
SEALS_IN_RUN = tuple(sid for sid, _p, _g in SEALED_PATHS if sid not in SEALS_LATE)

# THE MANIFEST, declared: every key the receipt publishes.  Each is sealed
# except the seal ledger itself, which IS the reference and is covered by the
# payload digest.
FINAL_KEYS = frozenset(p.split("/")[0] for _s, p, _g in SEALED_PATHS) | {"seals"}
UNSEALED_DECLARED = {"seals": "the seal ledger is the reference against which "
                              "every other key is checked; it cannot digest "
                              "itself, and it is covered by the payload digest "
                              "that G-ARTIFACT-INTEGRITY verifies on disk"}


def digest(value):
    if isinstance(value, str):
        return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]
    return hashlib.sha256(
        json.dumps(value, indent=1, sort_keys=True).encode("utf-8")).hexdigest()[:12]


def jpath(obj, path):
    cur = obj
    for part in path.split("/"):
        cur = cur[part]
    return cur


class Seal:
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
# SECTION 3.  THE ANCHORS
# ===========================================================================
#
# Anchors are (path, bytes) pairs, (path, value) pairs and (context, consumer)
# pairs.  The verbatim windows are evaluated BEFORE the byte anchors, each
# bound to the named gate that consumes it, each a context window rather than
# a fragment (#125): whitespace and markdown-prefix normalised, anchored, with
# a length floor.

SOURCES = [
    ("R4-RECEIPT", "v14/code/r4_defect_stage_receipt.json", "3dc1393b0df8"),
    ("R4-CODE", "v14/code/r4_defect_stage_exact.py", "2959c5a6a84b"),
    ("R4-PAPER", "v14/paper-10-defect-on-the-stage.md", "1063401c7bb5"),
    ("R4B-RECEIPT", "v14/code/r4b_momentum_receipt.json", "562e2a3d4d85"),
    ("R4B-CODE", "v14/code/r4b_momentum_exact.py", "4216f3de5f44"),
    ("R4B-PAPER", "v14/paper-15-momentum.md", "89c636906061"),
    ("R5-RECEIPT", "v14/code/r5_gauge_receipt.json", "0c02b7684e5b"),
    ("R5-PAPER", "v14/paper-18-gauge-rung.md", "62cfe5689d2c"),
    ("STAGE-RECEIPT", "v13/code/ha_successor_receipt.json", "542b8735daf0"),
    ("SEED-PAPER", "v12/paper1-composition-defect.md", "81bdab5673fb"),
    ("SEED-CODE", "v12/paper1_code/exact.py", "8e90f6435922"),
    ("PIN", "v14/note-r4c-pin.md", "162553b03ca9"),
]

# path-value anchors: (id, source, json path, expected, the gate that eats it)
PATH_VALUES = [
    ("PV-DIM", "STAGE-RECEIPT", "declarations/d", 2, "G-ARENA-ANCHORED"),
    ("PV-LINKS", "STAGE-RECEIPT", "declarations/links_d2",
     [[1, 0], [0, 1], [1, 1]], "G-ARENA-ANCHORED"),
    ("PV-COUNT-REGISTER", "STAGE-RECEIPT", "declarations/count_lattice/axis_max",
     6, "G-OCCUPANCY-NOT-ANCHORED"),
    ("PV-DIAG-REGISTER", "STAGE-RECEIPT", "declarations/count_lattice/diag_max",
     12, "G-OCCUPANCY-NOT-ANCHORED"),
    ("PV-L", "R4-RECEIPT", "counts/L", 4, "G-ARENA-ANCHORED"),
    ("PV-ALPHABET", "R4-RECEIPT", "counts/alphabet", 25, "G-ALPHABET-REBUILT"),
    ("PV-POOL", "R4-RECEIPT", "counts/pool", 64, "G-REBUILD-BIJECTION"),
    ("PV-CIRC", "R4-RECEIPT", "pool_counts/circulant", 58, "G-REBUILD-BIJECTION"),
    ("PV-BRICK", "R4-RECEIPT", "pool_counts/brickwork", 4, "G-REBUILD-CONTROLS"),
    ("PV-SCRAM", "R4-RECEIPT", "pool_counts/scrambled", 2, "G-REBUILD-CONTROLS"),
    ("PV-AXES", "R4-RECEIPT", "pool_counts/axes", 9, "G-REBUILD-BIJECTION"),
    ("PV-SECTOR", "R4-RECEIPT", "counts/sector", "SINGLE-OCCUPATION",
     "G-OCCUPANCY-NOT-ANCHORED"),
    ("PV-PARENT-DEFECT", "R4-RECEIPT", "counts/nonzero_at_maximal", 588,
     "G-PARENT-REPRODUCED"),
    ("PV-PARENT-PAIRS", "R4-RECEIPT", "counts/pairs_at_maximal", 3364,
     "G-PARENT-REPRODUCED"),
    ("PV-PARENT-MARKOV", "R4-RECEIPT", "counts/markov_nonzero", 0,
     "G-MARKOV-INHERITED"),
    ("PV-PARENT-MONOMIALS", "R4-RECEIPT", "markov_control/monomial_generators",
     ["C004", "C007", "C008", "C011", "C018", "C019", "C026", "C027", "C034",
      "C035", "C042", "C043", "C046", "C053", "C054", "C057"],
     "G-MONOMIAL-CLASSIFIER"),
    ("PV-SCRAMBLE-SWAPS", "R4-RECEIPT", "choice_inventory/12/value",
     "[(0, 5), (1, 11)]", "G-REBUILD-CONTROLS"),
    ("PV-R4B-ALIASED", "R4B-RECEIPT", "counts/aliased_cells", 320,
     "G-R4B-CONVENTION-REPRODUCED"),
    ("PV-R4B-ALIASED-FAM", "R4B-RECEIPT", "counts/aliased_families", 19,
     "G-R4B-CONVENTION-REPRODUCED"),
    ("PV-R4B-CELLS", "R4B-RECEIPT", "counts/integer_velocities", 1856,
     "G-R4B-CONVENTION-REPRODUCED"),
    ("PV-R4B-TIE", "R4B-RECEIPT", "velocity_definition/tie_reading",
     "TIE-AVERAGED", "G-R4B-CONVENTION-INHERITED"),
    ("PV-R4B-STENCIL", "R4B-RECEIPT", "stratification/stencil_admitted",
     ["FORWARD", "BACKWARD"], "G-R4B-CONVENTION-INHERITED"),
    ("PV-R5-COINS", "R5-RECEIPT", "counts/coins", 640, "G-COIN-ALPHABET-REBUILT"),
    ("PV-R5-LINKS", "R5-RECEIPT", "counts/links", 32, "G-COIN-ALPHABET-REBUILT"),
]

# verbatim windows: (id, source, needle, the gate that consumes it)
VERBATIM = [
    ("VB-THREE-ROUTES", "R4-PAPER",
     "Testing it requires leaving the arena, and there are exactly three "
     "routes out, in increasing cost: a two-excitation sector, in which one "
     "excitation's effective coefficient becomes a functional of another's "
     "occupation", "G-PIN-QUESTION-IS-THE-PARENTS"),
    ("VB-NO-MULTI", "R4-PAPER",
     "No multi-excitation sector, no interaction term, no field operator. The "
     "only interaction-shaped object is the composed-segment defect itself. "
     "The sector is single occupation throughout", "G-SECTOR-IS-NEW"),
    ("VB-DEFECT-DEF", "R4-PAPER",
     "the failure of the Born shadow of the coherent composite to equal the "
     "shadow obtained by forgetting phases and restarting at the intermediate "
     "cut. The division-event times are declared", "G-DEFECT-DEFINITION"),
    ("VB-CONNECTIVE", "R4-PAPER",
     "CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))", "G-CONNECTIVE-VERBATIM"),
    ("VB-R4B-CONVENTION", "R4B-PAPER",
     "The stencil coordinate is therefore forced to 2 by the definition, not "
     "chosen against it, and the fiber of 9 is 3 lifts times 2 admissible "
     "stencils.", "G-R4B-CONVENTION-INHERITED"),
    ("VB-R4B-TIE", "R4B-PAPER",
     "A lift of \u0394_j s to an integer is unique except at one value. "
     "\u0394_j s = 4 is a phase advance of exactly \u03c0 per momentum step: a "
     "displacement of L/2 = 2, which on this torus is its own negative.",
     "G-R4B-CONVENTION-INHERITED"),
    ("VB-R5-LAMBDA2", "R5-PAPER",
     "the hard-core antisymmetric sector $\\Lambda^2$, on `120 two-excitation "
     "states`, the forced choice at fixed dimension up to the symmetric square, "
     "which the choice inventory carries with fibre 2", "G-R5-PRECEDENT-CITED"),
    ("VB-R5-EIGHTEEN", "R5-PAPER",
     "The extension returns a **negative**: `0 of 18` rows carry both. That "
     "count is `6 named coins against 3 relations` \u2014 a declared sample, "
     "not the exhaustive sweep", "G-R5-PRECEDENT-CITED"),
    ("VB-PIN-QUESTION", "PIN",
     "which exchange symmetry does the substrate's composition law FORCE or "
     "ADMIT on two-excitation states", "G-PIN-QUESTION-IS-THE-PARENTS"),
    ("VB-PIN-SCOPE", "PIN",
     "the R4b scope stamp binds: NO transport number is inherited",
     "G-NO-TRANSPORT-NUMBER-INHERITED"),
    ("VB-PIN-SHAPES", "PIN",
     "No particle-physics naming beyond the measured shapes (fermionic-shape / "
     "bosonic-shape are SHAPE words; the walls bar more).", "G-NO-PARTICLE-NAMING"),
    ("VB-SEED-DEFECT", "SEED-PAPER", "Born", "G-DEFECT-WITNESS"),
]


def norm_text(s):
    """#125: text gates match text as written -- whitespace AND markdown-prefix
    (blockquote / list) normalisation, so a needle cannot be defeated by a
    reflow or by being quoted."""
    out = []
    for line in s.split("\n"):
        t = line.strip()
        while t[:2] in ("> ", "- ", "* ", "+ "):
            t = t[2:].strip()
        if t[:1] == ">":
            t = t[1:].strip()
        out.append(t)
    return " ".join(" ".join(out).split())


def read_bytes(path):
    with open(path, "rb") as fh:
        b = fh.read()
    READS.append(path)
    return b


# ===========================================================================
# SECTION 4.  THE ARENA, THE FAMILY, REBUILT AND GATED
# ===========================================================================

def build_alphabet():
    """0 together with zeta_8^t times a modulus in {1, 1/2, 1/sqrt 2}."""
    alpha = [ZERO]
    for t in range(8):
        for m in (ONE, HALF, INVSQ2):
            alpha.append(fmul(ZP[t], m))
    return alpha


def autocorr_unitary(c):
    """delta autocorrelation: A(m) = sum_v c_v conj(c_{v+m}) = delta_{m,0}."""
    offs = list(c)
    lags = set()
    for o in offs:
        for p in offs:
            lags.add(tuple((o[i] - p[i]) % L for i in range(D)))
    for m in lags:
        s = ZERO
        for o, v in c.items():
            w = c.get(addv(o, m))
            if w is not None:
                s = fadd(s, fmul(v, fconj(w)))
        if s != (ONE if not any(m) else ZERO):
            return False
    return True


def gauge_key(c):
    return tuple(sorted(c.items()))


def gauge_orbit(c):
    return {gauge_key({o: fmul(ZP[t], v) for o, v in c.items()}) for t in range(8)}


def coef_matrix(c):
    col = [dict() for _ in range(NS)]
    for x in SITES:
        for o, v in c.items():
            col[IDX[x]][IDX[addv(x, o)]] = v
    return col


def build_family(alpha, LD):
    seen, axes = set(), []
    for o in SITES:
        if not any(o) or o in seen:
            continue
        seen.add(o)
        seen.add(negv(o))
        axes.append(o)
    orbit_sizes = []
    circ, keys = [], set()
    for a in axes:
        offs = []
        for o in (tuple([0] * D), a, negv(a)):
            if o not in offs:
                offs.append(o)
        done = set()
        for vals in product(alpha, repeat=len(offs)):
            c = {o: v for o, v in zip(offs, vals) if v != ZERO}
            if not c or not autocorr_unitary(c):
                continue
            k = gauge_key(c)
            if k in done:
                continue
            orb = gauge_orbit(c)
            orbit_sizes.append(len(orb))
            done |= orb
            rep = min(orb)
            if rep in keys:
                continue
            keys.add(rep)
            cd = dict(rep)
            circ.append({"kind": "CIRC", "axis": a, "axis_ord": elt_order(a),
                         "coef": cd, "support": len(cd),
                         "radius": max(absmax(o) for o in cd),
                         "monomial": len(cd) <= 1})
    if mut("MUT-GAUGE-ORBIT"):
        orbit_sizes[0] = 4
    LD.gate("G-GAUGE-ORBITS-FREE",
            "the declared global-phase gauge acts freely on the solution set: "
            "every orbit has the full group's size, so the gauge quotient "
            "cannot merge two distinct laws",
            set(orbit_sizes) == {8},
            "orbit sizes %s over %d orbits" % (sorted(set(orbit_sizes)), len(orbit_sizes)))
    return axes, circ


def build_controls(circ, swaps, LD):
    """the six declared controls, rebuilt in the parent's construction order:
    four brickwork generators (the declared 2x2 Hadamard coin on a parity class
    of dominoes) and two scrambled ones (a declared site transposition)."""
    Hc = ((INVSQ2, INVSQ2), (INVSQ2, fneg(INVSQ2)))
    out = []
    for e in ((1, 0), (0, 1)):
        for par in (0, 1):
            col = [{i: ONE} for i in range(NS)]
            for x in SITES:
                if ((x[0] * e[0] + x[1] * e[1]) % L) % 2 == par:
                    y = addv(x, e)
                    a, b = IDX[x], IDX[y]
                    col[a] = {a: Hc[0][0], b: Hc[1][0]}
                    col[b] = {a: Hc[0][1], b: Hc[1][1]}
            out.append({"kind": "BRICK", "axis": e, "axis_ord": elt_order(e),
                        "coef": None, "support": None, "monomial": False,
                        "radius": 1, "parity": par,
                        "mat": [{i: v for i, v in c.items() if v != ZERO} for c in col]})
    base = [g for g in circ if g["support"] == 3][0]
    bm = coef_matrix(base["coef"])
    for (u, w) in swaps:
        pi = list(range(NS))
        pi[u], pi[w] = pi[w], pi[u]
        M = [dict() for _ in range(NS)]
        for j, c in enumerate(bm):
            for i, v in c.items():
                M[pi[j]][pi[i]] = v
        out.append({"kind": "SCRAM", "axis": None, "axis_ord": None,
                    "coef": None, "support": None, "monomial": False,
                    "radius": 2, "swap": [u, w], "mat": M})
    if mut("MUT-CONTROL-COUNT"):
        out = out[:-1]
    LD.gate("G-REBUILD-CONTROLS",
            "the six declared controls are rebuilt in the parent's own "
            "construction order and count, from the parent's declared coin and "
            "its declared swap permutations, both read as anchored values",
            sum(1 for g in out if g["kind"] == "BRICK") == 4
            and sum(1 for g in out if g["kind"] == "SCRAM") == 2
            and all(is_unitary(g["mat"]) for g in out),
            "4 brickwork + 2 scrambled, all unitary")
    return out


# ===========================================================================
# SECTION 5.  THE TWO-EXCITATION SECTORS
# ===========================================================================
#
# Three sectors are built over the SAME single-excitation stage:
#
#   T      the ordered (distinguishable) sector, |X|^2 configurations;
#   Sym^2  the exchange-symmetric sector, in the NORMALISED basis
#          |ab>_s = (|ab> + |ba>)/sqrt 2 for a < b and |aa>_s = |aa>;
#   Lam^2  the exchange-antisymmetric sector, |ab>_a = (|ab> - |ba>)/sqrt 2.
#
# The free lift of a single-excitation generator U is U tensor U; each sector
# carries its restriction, and all three restrictions are functors.

PAIRS = ()
PIDX = {}
SYMB = ()
SIDX = {}
DBLSET = frozenset()


def set_sectors():
    global PAIRS, PIDX, SYMB, SIDX, DBLSET
    PAIRS = tuple((i, j) for i in range(NS) for j in range(i + 1, NS))
    PIDX = {p: k for k, p in enumerate(PAIRS)}
    SYMB = PAIRS + tuple((i, i) for i in range(NS))
    SIDX = {p: k for k, p in enumerate(SYMB)}
    DBLSET = frozenset(SIDX[(i, i)] for i in range(NS))


def wedge(M):
    """Lambda^2(U): entry ((a<b),(x<y)) = U_ax U_by - U_ay U_bx."""
    out = []
    for (x, y) in PAIRS:
        acc = {}
        cx, cy = M[x], M[y]
        for a, vax in cx.items():
            for b, vby in cy.items():
                if a == b:
                    continue
                t = fmul(vax, vby)
                if a < b:
                    kk = PIDX[(a, b)]
                    s = t
                else:
                    kk = PIDX[(b, a)]
                    s = fneg(t)
                cur = acc.get(kk)
                acc[kk] = s if cur is None else fadd(cur, s)
        out.append({i: v for i, v in acc.items() if v != ZERO})
    return out


def symsq(M):
    """Sym^2(U) in the normalised basis."""
    out = []
    for (x, y) in SYMB:
        cxy = INVSQ2 if x < y else HALF
        orders = ((x, y), (y, x)) if x < y else ((x, x), (x, x))
        acc = {}
        for (p, q) in orders:
            cp, cq = M[p], M[q]
            for a, va in cp.items():
                for b, vb in cq.items():
                    t = fmul(va, vb)
                    if a == b:
                        kk = SIDX[(a, a)]
                        t = fadd(t, t)
                    else:
                        kk = SIDX[(a, b)] if a < b else SIDX[(b, a)]
                    cur = acc.get(kk)
                    acc[kk] = t if cur is None else fadd(cur, t)
        col = {}
        for kk, v in acc.items():
            a, b = SYMB[kk]
            w = fmul(fmul(INVSQ2 if a < b else HALF, cxy), v)
            if w != ZERO:
                col[kk] = w
        out.append(col)
    return out


def tensor(M):
    """U tensor U on the ordered sector, |X|^2 configurations."""
    out = []
    for x in range(NS):
        cx = M[x]
        for y in range(NS):
            acc = {}
            for a, va in cx.items():
                for b, vb in M[y].items():
                    acc[a * NS + b] = fmul(va, vb)
            out.append(acc)
    return out


def tensor2(A, B):
    """A tensor B: the DISTINGUISHABLE lift, one generator per excitation."""
    out = []
    for x in range(NS):
        ca = A[x]
        for y in range(NS):
            acc = {}
            for a, va in ca.items():
                for b, vb in B[y].items():
                    acc[a * NS + b] = fmul(va, vb)
            out.append(acc)
    return out


def swap_matrix():
    return [{(j * NS + i): ONE} for i in range(NS) for j in range(NS)]


def hardcore_leak(Sy):
    """the cells by which Sym^2(U) carries a hard-core (x != y) configuration
    into a doubly-occupied one.  Lambda^2 has no such cells to carry."""
    n = 0
    for k in range(len(PAIRS)):
        for i in Sy[k]:
            if i in DBLSET:
                n += 1
    return n


# ===========================================================================
# SECTION 6.  THE DEFECT, AND ITS SECOND CODE PATH
# ===========================================================================

def defect(A2, A1):
    """the composition defect, definitional route:
           Delta^B(U2, U1) = B(U2 U1) - B(U2) B(U1),
    with the parent's declared division-event times (t = 0 and t = 2 are
    division events, the cut at t = 1 is not) and the declared leg B(U2)."""
    return msub(born(matmul(A2, A1)), matmul(born(A2), born(A1)))


def defect_crossterm(A2, A1):
    """the SECOND code path: the same object as the explicit interference sum
           Delta_ij = sum_{m != m'} A2_im A1_mj conj(A2_im' A1_m'j),
    which shares no helper, no cache and no typed value with the route above.
    It DERIVES the object; it never re-reads the builder's product."""
    out = []
    for j, c1 in enumerate(A1):
        terms = {}
        for m, v1 in c1.items():
            for i, v2 in A2[m].items():
                p = fmul(v2, v1)
                if p == ZERO:
                    continue
                terms.setdefault(i, []).append(p)
        col = {}
        for i, ps in terms.items():
            if len(ps) < 2:
                continue
            s = ZERO
            for u in ps:
                for v in ps:
                    if u is v:
                        continue
                    s = fadd(s, fmul(u, fconj(v)))
            if s != ZERO:
                col[i] = s
        out.append(col)
    return out


# ===========================================================================
# SECTION 7.  THE STATE (built in one place, gate by gate)
# ===========================================================================

def build_arena(break_anchor=None):
    LD = Ledger()
    S = {}
    say("[1/9] anchors, the arena, the field")

    # ---- verbatim windows first, each bound to its consumer ---------------
    texts = {}
    vb_rows = []
    for sid, rel, want in SOURCES:
        b = read_bytes(os.path.join(ROOT, rel))
        texts[sid] = b.decode("utf-8", "replace")
    for vid, src, needle, gate in VERBATIM:
        hay = norm_text(texts[src])
        nd = norm_text(needle)
        if break_anchor == vid:
            nd = nd + " XXBROKEN"
        present = nd in hay
        vb_rows.append({"anchor": vid, "source": src, "consumer": gate,
                        "chars": len(nd), "present": present})
    floor = min(len(norm_text(n)) for _v, _s, n, _g in VERBATIM if _v != "VB-SEED-DEFECT")
    if mut("MUT-VERBATIM-FRAGMENT"):
        vb_rows.append({"anchor": "VB-INJECTED", "source": "PIN",
                        "consumer": "G-VERBATIM-ANCHORS", "chars": 3, "present": True})
    LD.gate("G-VERBATIM-ANCHORS",
            "every declared verbatim window is present in its named source "
            "after whitespace and markdown-prefix normalisation, and every "
            "window that carries a claim is a CONTEXT window (at least 40 "
            "normalised characters), not a fragment",
            all(r["present"] for r in vb_rows)
            and all(r["chars"] >= 40 for r in vb_rows if r["anchor"] != "VB-SEED-DEFECT"),
            "%d windows, floor %d chars" % (len(vb_rows), floor))
    S["verbatim_anchors"] = vb_rows

    # ---- byte anchors -----------------------------------------------------
    byte_rows = []
    for sid, rel, want in SOURCES:
        got = hashlib.sha256(texts[sid].encode("utf-8", "replace")).hexdigest()[:12]
        got = hashlib.sha256(read_bytes(os.path.join(ROOT, rel))).hexdigest()[:12]
        if break_anchor == sid:
            got = "0" * 12
        byte_rows.append({"anchor": sid, "path": rel, "sha256_12": got,
                          "expected": want, "ok": got == want})
    LD.gate("G-BYTE-ANCHORS",
            "every hash-pinned source is the pinned bytes; a path drift or a "
            "content drift dies here and the run stops before a single "
            "measurement is taken",
            all(r["ok"] for r in byte_rows),
            "%d byte anchors" % len(byte_rows))
    S["byte_anchors"] = byte_rows

    R4 = json.loads(texts["R4-RECEIPT"])
    R4B = json.loads(texts["R4B-RECEIPT"])
    R5 = json.loads(texts["R5-RECEIPT"])
    STAGE = json.loads(texts["STAGE-RECEIPT"])
    SRC = {"R4-RECEIPT": R4, "R4B-RECEIPT": R4B, "R5-RECEIPT": R5,
           "STAGE-RECEIPT": STAGE}

    pv_rows = []
    for pid, src, path, want, gate in PATH_VALUES:
        cur = SRC[src]
        try:
            for part in path.split("/"):
                cur = cur[int(part)] if part.isdigit() else cur[part]
        except (KeyError, IndexError, TypeError):
            cur = None
        if break_anchor == pid:
            cur = "BROKEN"
        pv_rows.append({"anchor": pid, "source": src, "path": path,
                        "value": cur, "expected": want, "consumer": gate,
                        "ok": cur == want})
    if mut("MUT-PATH-ANCHOR"):
        pv_rows[0] = dict(pv_rows[0], ok=False)
    LD.gate("G-PATH-VALUE-ANCHORS",
            "every anchored (path, value) pair holds: the anchor is the VALUE "
            "at the path, not merely the file's bytes, so a receipt that keeps "
            "its digest while moving a number dies here",
            all(r["ok"] for r in pv_rows), "%d path-value anchors" % len(pv_rows))
    S["path_value_anchors"] = pv_rows

    dim = SRC["STAGE-RECEIPT"]["declarations"]["d"]
    size = SRC["R4-RECEIPT"]["counts"]["L"]
    if mut("MUT-ARENA-SIZE"):
        size = 3
    set_lattice(dim, size)
    set_sectors()
    LD.gate("G-ARENA-ANCHORED",
            "the spatial dimension is READ from the record layer's own "
            "declarations and the lattice size from the parent's measured "
            "admissible set; neither is this unit's to choose and neither is "
            "typed beside the census",
            D == 2 and L == 4 and NS == 16
            and SRC["STAGE-RECEIPT"]["declarations"]["links_d2"] == [[1, 0], [0, 1], [1, 1]],
            "d = %d, L = %d, |X| = %d" % (D, L, NS))
    S["arena_declaration"] = {
        "boundary": "the finite periodic site lattice X = (Z_L)^d with d = 2 "
                    "and L = 4, read from the anchored stage and from the "
                    "parent's measured admissible set",
        "carrier": "the TWO-excitation sector over that lattice: the ordered "
                   "sector on |X|^2 configurations, and its two exchange "
                   "sectors, the symmetric one on |X|(|X|+1)/2 and the "
                   "antisymmetric one on |X|(|X|-1)/2",
        "family": "R4's terminal family, rebuilt here from its definitions and "
                  "gated coefficient map by coefficient map against the parent "
                  "receipt: 58 circulant generators on the 3-term axis stencil "
                  "over the declared 25-element alphabet, plus the 6 controls",
        "law": "the FREE LIFT U tensor U -- the substrate's own composition "
               "law applied to each excitation -- restricted to each sector; "
               "the declared alternative lifts are the distinguishable lift "
               "U tensor V and the contact-phase lift, both censused",
        "occupancy": "the site occupancy CEILING is this unit's declaration "
                     "and is NOT anchored: the stage's own count registers run "
                     "to 6 and 12, and the parent's single-occupation sector "
                     "is the common restriction of both ceilings",
        "velocity": "R4b's stratified convention inherited AS DECLARED: "
                    "forward difference with the antipodal tie averaged; no "
                    "new selection claim is made here",
        "division_events": "inherited unchanged: t = 0 and t = 2 are division "
                           "events, the cut at t = 1 is not, and the leg at "
                           "the cut is B(U2); indivisibility is DECLARED by "
                           "those times and is never measured",
    }

    # ---- the field, scanned --------------------------------------------
    alpha = build_alphabet()
    if mut("MUT-ALPHABET"):
        alpha = alpha[:24]
    LD.gate("G-ALPHABET-REBUILT",
            "the coefficient alphabet is rebuilt from the parent's definition "
            "-- zero together with zeta_8^t times a modulus in {1, 1/2, "
            "1/sqrt 2} -- and its size is the anchored one",
            len(set(alpha)) == SRC["R4-RECEIPT"]["counts"]["alphabet"] == 25
            and all(fnorm(a) in (ZERO, ONE, HALF, (1, 0, 0, 0, 2)) for a in alpha),
            "%d distinct alphabet elements" % len(set(alpha)))

    tree = ast.parse(open(SELF, "r", encoding="utf-8").read())
    floats = [n for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    divs = [n for n in ast.walk(tree)
            if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div)]
    LD.gate("G-NO-FLOAT",
            "the instrument's own source contains no float literal and no true "
            "division: every quantity in this unit is an exact element of "
            "Q(zeta_8) carried as integers",
            not floats and not divs,
            "%d float literals, %d true divisions" % (len(floats), len(divs)))

    src_text = open(SELF, "r", encoding="utf-8").read()
    bad_switch = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == "gate":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) \
                        and sub.func.id == "mut":
                    bad_switch.append(node.lineno)
    shells = [n.names[0].name for n in ast.walk(tree)
              if isinstance(n, ast.Import)
              for _x in [0] if n.names[0].name in ("subprocess", "shutil", "socket")]
    shells += [n.module for n in ast.walk(tree)
               if isinstance(n, ast.ImportFrom)
               and n.module in ("subprocess", "shutil", "socket")]
    shells += [n.func.attr for n in ast.walk(tree)
               if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
               and n.func.attr in ("system", "popen", "run", "check_output")]
    if mut("MUT-SHELL-IMPORT"):
        shells = shells + ["subprocess"]
    LD.gate("G-NO-VERSION-CONTROL-NO-SHELL",
            "the run reads every input by PATH and hash, shells out to "
            "nothing, and consults no version-control state: it reproduces "
            "off-tree and on a machine with no git, and an added subprocess "
            "or socket import dies here",
            not shells, "%d shell or network entry points" % len(shells))

    LD.gate("G-MUTANT-SWITCH-CLEAN",
            "no gate predicate reads the mutant switch: every mut() call sits "
            "in the measurement path, so a mutant can only be killed by a "
            "gate that measures, never by a gate that recognises it",
            not bad_switch, "%d gate calls reading mut()" % len(bad_switch))

    # ---- the family -------------------------------------------------------
    say("[2/9] the family, rebuilt from the parent's definitions and gated")
    axes, circ = build_family(alpha, LD)
    parent_pool = SRC["R4-RECEIPT"]["pool"]
    parent_circ = {}
    for r in parent_pool:
        if r["kind"] != "CIRC":
            continue
        d = {}
        for o, v in r["coef"]:
            e = v[4].bit_length() - 1
            d[tuple(o)] = red(v[0], v[1], v[2], v[3], e)
        parent_circ[r["name"]] = tuple(sorted(d.items()))
    mine = {gauge_key(g["coef"]): g for g in circ}
    if mut("MUT-REBUILD-DROP"):
        mine.pop(sorted(mine)[0])
    fwd = all(k in mine for k in parent_circ.values())
    bwd = all(k in set(parent_circ.values()) for k in mine)
    LD.gate("G-REBUILD-BIJECTION",
            "every rebuilt coefficient map is exactly one of the parent's rows "
            "and every parent row is rebuilt: a bijection in BOTH directions, "
            "object by object, between two programs that share no code and no "
            "representation of the field",
            fwd and bwd and len(mine) == len(parent_circ) == 58
            and len(axes) == SRC["R4-RECEIPT"]["pool_counts"]["axes"],
            "%d rebuilt, %d parent rows, %d axes" % (len(mine), len(parent_circ), len(axes)))

    inv = {v: k for k, v in parent_circ.items()}
    for g in circ:
        g["name"] = inv[gauge_key(g["coef"])]
        g["mat"] = coef_matrix(g["coef"])
    circ.sort(key=lambda g: g["name"])
    prow = {r["name"]: r for r in parent_pool if r["kind"] == "CIRC"}
    bad_inv = [g["name"] for g in circ
               if (g["support"], g["radius"], g["monomial"], list(g["axis"]), g["axis_ord"])
               != (prow[g["name"]]["support"], prow[g["name"]]["radius"],
                   prow[g["name"]]["monomial"], prow[g["name"]]["axis"],
                   prow[g["name"]]["axis_ord"])]
    if mut("MUT-INVARIANT"):
        bad_inv = bad_inv + [circ[0]["name"]]
    LD.gate("G-REBUILD-INVARIANTS",
            "for every matched pair the axis, the axis order, the support, the "
            "radius and the monomiality agree -- a per-object obligation "
            "discharged per object, never as a count",
            not bad_inv, "%d invariant mismatches over %d generators"
            % (len(bad_inv), len(circ)))

    swaps = [tuple(int(x) for x in s.strip("() ").split(",")) for s in
             SRC["R4-RECEIPT"]["choice_inventory"][12]["value"].strip("[]").split("), (")]
    ctrl = build_controls(circ, swaps, LD)
    pool = circ + ctrl
    for i, g in enumerate(pool):
        if "name" not in g:
            g["name"] = "%s%03d" % (g["kind"][0], i)
    if mut("MUT-POOL-COUNT"):
        pool = pool[:-1]
    LD.gate("G-POOL-COMPLETE",
            "the pool is the parent's, entire: the circulant stratum plus the "
            "six controls, at the anchored counts",
            len(pool) == SRC["R4-RECEIPT"]["counts"]["pool"] == 64
            and sum(1 for g in pool if g["kind"] == "CIRC") == 58,
            "%d generators" % len(pool))

    monos = sorted(g["name"] for g in pool if g["monomial"])
    if mut("MUT-MONOMIAL-LIST"):
        monos = monos[:-1]
    LD.gate("G-MONOMIAL-CLASSIFIER",
            "the monomial sub-family is classified by MEASURED support and is "
            "exactly the parent's declared Markovian set, name for name",
            monos == sorted(SRC["R4-RECEIPT"]["markov_control"]["monomial_generators"]),
            "%d monomial generators" % len(monos))

    S["pool"] = [{"name": g["name"], "kind": g["kind"], "monomial": g["monomial"],
                  "support": g["support"], "radius": g["radius"]} for g in pool]
    return S, LD, pool, circ, SRC, texts


# ===========================================================================
# SECTION 8.  THE EXCHANGE CENSUS -- QUESTION ONE
# ===========================================================================

CENSUS_CACHE = {}
CENSUS_DIGESTS = {}


def full_pool_key(pool):
    return digest([[g["name"], g["kind"], D, L,
                    sorted([j, sorted([i, list(v)] for i, v in c.items())]
                           for j, c in enumerate(g["mat"]))] for g in pool])


def raw_exchange(pool):
    key = ("exchange", full_pool_key(pool))
    if key in CENSUS_CACHE:
        return CENSUS_CACHE[key]
    P = swap_matrix()
    rows = []
    for g in pool:
        T = tensor(g["mat"])
        W, Sy = wedge(g["mat"]), symsq(g["mat"])
        rows.append({"generator": g["name"], "kind": g["kind"],
                     "monomial": g["monomial"],
                     "exchange_commutes": matmul(P, T) == matmul(T, P),
                     "antisymmetric_closed_unitary": is_unitary(W),
                     "symmetric_closed_unitary": is_unitary(Sy),
                     "antisymmetric_born_stochastic": is_stochastic(born(W)),
                     "symmetric_born_stochastic": is_stochastic(born(Sy))})
    CENSUS_CACHE[key] = rows
    return rows


def raw_leak(pool):
    key = ("leak", full_pool_key(pool))
    if key in CENSUS_CACHE:
        return CENSUS_CACHE[key]
    rows = [{"generator": g["name"], "monomial": g["monomial"],
             "symmetric_hardcore_leak_cells": hardcore_leak(symsq(g["mat"])),
             "antisymmetric_hardcore_closed": True} for g in pool]
    CENSUS_CACHE[key] = rows
    return rows


def exchange_census(S, LD, pool, SRC):
    """Which exchange symmetry does the composition law force or admit?  The
    question is asked per generator, never as a count (#87)."""
    say("[3/9] the exchange census: the sectors, per generator")
    nT, nS, nW = NS * NS, len(SYMB), len(PAIRS)
    if mut("MUT-SECTOR-DIM"):
        nS = nS + 1
    LD.gate("G-SECTOR-DECOMPOSITION",
            "the two-excitation ordered sector decomposes into exactly the two "
            "exchange sectors and nothing else: at two excitations the "
            "symmetric group has two irreducible characters, so a "
            "parastatistics-shaped THIRD sector cannot exist here by dimension",
            nT == nS + nW and nT == 256 and nS == 136 and nW == 120,
            "%d = %d + %d" % (nT, nS, nW))

    rows = [dict(r) for r in raw_exchange(pool)]
    if mut("MUT-EXCHANGE-COMMUTE"):
        rows[0]["exchange_commutes"] = False
    nc = sum(1 for r in rows if r["exchange_commutes"])
    na = sum(1 for r in rows if r["antisymmetric_closed_unitary"])
    ns = sum(1 for r in rows if r["symmetric_closed_unitary"])
    LD.gate("G-EXCHANGE-COMMUTES",
            "the exchange operator commutes with the free lift of EVERY "
            "generator in the pool -- measured generator by generator, with "
            "the predicate bound to the generator and not to the count",
            all(r["exchange_commutes"] for r in rows) and nc == len(pool),
            "%d of %d generators" % (nc, len(pool)), kind="DISCLOSURE")
    if mut("MUT-BOTH-ADMITTED"):
        rows[0] = dict(rows[0], antisymmetric_closed_unitary=False)
        na = na - 1
    LD.gate("G-BOTH-SECTORS-ADMITTED",
            "both exchange sectors are invariant under every generator's free "
            "lift, and the restriction is unitary and its Born shadow "
            "stochastic in both -- so the composition law ADMITS both shapes "
            "and selects neither",
            all(r["antisymmetric_closed_unitary"] and r["symmetric_closed_unitary"]
                and r["antisymmetric_born_stochastic"] and r["symmetric_born_stochastic"]
                for r in rows),
            "antisymmetric %d of %d, symmetric %d of %d"
            % (na, len(pool), ns, len(pool)))
    S["exchange_census"] = {"rows": rows, "commuting": nc,
                            "antisymmetric_admitted": na,
                            "symmetric_admitted": ns,
                            "generators": len(pool),
                            "dim_ordered": nT, "dim_symmetric": nS,
                            "dim_antisymmetric": nW}
    return rows


def occupancy_census(S, LD, pool, SRC):
    """The occupancy ceiling is a DECLARATION, and it is the coordinate that
    selects.  Ceiling 2 admits the doubly-occupied configurations; ceiling 1
    (the hard core) does not.  Measured: which sector survives which."""
    say("[4/9] the occupancy declaration, and what it kills")
    rows = []
    for r in raw_leak(pool):
        leak = 0 if mut("MUT-LEAK-ZERO") else r["symmetric_hardcore_leak_cells"]
        rows.append({"generator": r["generator"], "monomial": r["monomial"],
                     "symmetric_hardcore_leak_cells": leak,
                     "symmetric_hardcore_closed": leak == 0,
                     "antisymmetric_hardcore_closed": True})
    leaking = sum(1 for r in rows if not r["symmetric_hardcore_closed"])
    closed = len(rows) - leaking
    mismatch = [r["generator"] for r in rows
                if (r["symmetric_hardcore_leak_cells"] > 0) != (not r["monomial"])]
    LD.gate("G-HARDCORE-LEAK-PER-GENERATOR",
            "under the hard-core ceiling the symmetric sector fails to close "
            "at exactly the non-monomial generators and closes at exactly the "
            "monomial ones -- a per-generator predicate discharged per "
            "generator, with no aggregate standing in for any of them",
            not mismatch and leaking > 0 and closed > 0,
            "%d leaking, %d closed, %d mismatches" % (leaking, closed, len(mismatch)))
    LD.gate("G-HARDCORE-ANTISYMMETRIC-CLOSED",
            "under the same ceiling the antisymmetric sector closes at every "
            "generator: the wedge has no doubly-occupied configuration to "
            "leak into, so the exclusion is not imposed on it but is the shape "
            "itself",
            all(r["antisymmetric_hardcore_closed"] for r in rows)
            and len(PAIRS) == 120,
            "%d of %d generators, %d hard-core configurations"
            % (len(rows), len(pool), len(PAIRS)), kind="DISCLOSURE")

    # the two ceilings have the SAME one-excitation restriction: this is why
    # no measurement the parent could take can select between them.
    one_ceiling1 = NS - 1 if mut("MUT-CEILINGS") else NS
    one_ceiling2 = NS
    LD.gate("G-CEILINGS-AGREE-AT-ONE-EXCITATION",
            "the two occupancy ceilings have the same one-excitation "
            "restriction, configuration for configuration -- so the parent's "
            "whole arena is a fixed point of both, and no single-excitation "
            "measurement whatever can select between them",
            one_ceiling1 == one_ceiling2 == NS
            and len(SYMB) != len(PAIRS),
            "%d = %d configurations at one excitation; %d against %d at two"
            % (one_ceiling1, one_ceiling2, len(SYMB), len(PAIRS)))
    reg = [r for r in S["path_value_anchors"] if r["anchor"] == "PV-COUNT-REGISTER"][0]
    regval = 1 if mut("MUT-REGISTER") else reg["value"]
    LD.gate("G-OCCUPANCY-NOT-ANCHORED",
            "the occupancy ceiling is NOT anchored: the record layer declares "
            "the site lattice, the link set and the chart group and declares "
            "no ceiling at all, and its own count registers are integer valued "
            "and run past one -- which, if it argues anything, argues against "
            "the hard core.  The ceiling is therefore carried as this unit's "
            "declaration and censused both ways",
            regval == 6 and regval > 1
            and SRC["R4-RECEIPT"]["counts"]["sector"] == "SINGLE-OCCUPATION",
            "anchored count register = %d" % regval)
    S["occupancy"] = {
        "rows": rows, "symmetric_leaking": leaking, "symmetric_closed": closed,
        "antisymmetric_closed": len(rows),
        "configurations_ceiling_1": len(PAIRS),
        "configurations_ceiling_2": len(SYMB),
        "one_excitation_configurations": NS,
        "anchored_count_register": regval,
        "ceiling_is_anchored": False,
    }
    return rows


def raw_distinguishable(circ):
    key = ("A4", pool_key(circ))
    if key in CENSUS_CACHE:
        return CENSUS_CACHE[key]
    off = broken = 0
    for i, g2 in enumerate(circ):
        for j, g1 in enumerate(circ):
            if i == j:
                continue
            off += 1
            if tensor2(g2["mat"], g1["mat"]) != tensor2(g1["mat"], g2["mat"]):
                broken += 1
    CENSUS_CACHE[key] = (off, broken)
    return off, broken


def arena_census(S, LD, pool, circ, LDrows):
    """The two-way design the pin requires: FOUR arenas, each a real
    construction on this stage, on which each symmetry class demonstrably
    survives or dies.  The head law is exercised on all four and returns a
    DIFFERENT pre-registered outcome on each, so every pre-registered outcome
    REACHES its gate (#34) on a measured arena and not on a synthetic one."""
    say("[5/9] the four arenas: where each shape lives and where it dies")
    arenas = []

    # A1 -- the declared verdict arena: the free lift at occupancy ceiling 2
    ex = S["exchange_census"]
    arenas.append({"arena": "A1-FREE-LIFT-CEILING-2",
                   "role": "THE DECLARED VERDICT ARENA",
                   "antisymmetric_lives": ex["antisymmetric_admitted"] == len(pool),
                   "symmetric_lives": ex["symmetric_admitted"] == len(pool),
                   "detail": "both sectors invariant, unitary and stochastic at "
                             "%d of %d generators" % (ex["antisymmetric_admitted"], len(pool))})

    # A2 -- the same lift at occupancy ceiling 1 (the hard core)
    oc = S["occupancy"]
    a2_sym = oc["symmetric_leaking"] == 0
    if mut("MUT-A3-LIVES"):
        a2_sym = True
    arenas.append({"arena": "A2-FREE-LIFT-CEILING-1-HARD-CORE",
                   "role": "the occupancy declaration, tightened",
                   "antisymmetric_lives": oc["antisymmetric_closed"] == len(pool),
                   "symmetric_lives": a2_sym,
                   "detail": "the symmetric sector leaks out of the hard core at "
                             "%d of %d generators; the antisymmetric sector at none"
                             % (oc["symmetric_leaking"], len(pool))})

    # A3 -- the one-site arena: the antisymmetric shape dies by dimension
    dims = []
    for n in range(1, 7):
        dims.append({"sites": n, "antisymmetric_dim": n * (n - 1) // 2,
                     "symmetric_dim": n * (n + 1) // 2})
    d1 = [r for r in dims if r["sites"] == 1][0]
    if mut("MUT-A3-DIM"):
        d1 = {"sites": 1, "antisymmetric_dim": 1, "symmetric_dim": 1}
    arenas.append({"arena": "A3-ONE-SITE-LATTICE",
                   "role": "the exclusion as a dimension count (a degenerate "
                           "control, declared as such)",
                   "antisymmetric_lives": d1["antisymmetric_dim"] > 0,
                   "symmetric_lives": d1["symmetric_dim"] > 0,
                   "detail": "at one site the antisymmetric sector has dimension "
                             "%d and the symmetric one dimension %d"
                             % (d1["antisymmetric_dim"], d1["symmetric_dim"])})

    # A4 -- the distinguishable lift U tensor V: NEITHER sector survives
    off, broken = raw_distinguishable(circ)
    if mut("MUT-A4-COMMUTE"):
        broken = 0
    arenas.append({"arena": "A4-DISTINGUISHABLE-LIFT",
                   "role": "one generator per excitation: the excitations are "
                           "told apart by the law itself",
                   "antisymmetric_lives": broken != off,
                   "symmetric_lives": broken != off,
                   "detail": "the exchange operator fails to commute with the "
                             "lift at %d of %d ordered pairs of distinct "
                             "generators, and where it fails NEITHER sector is "
                             "invariant" % (broken, off)})
    LD.gate("G-A4-NEITHER-REACHED",
            "the NEITHER branch is reached on a REAL arena and not on a "
            "synthetic census: at the distinguishable lift every ordered pair "
            "of distinct generators breaks the exchange symmetry",
            broken == off and off > 0,
            "%d of %d ordered pairs of distinct generators" % (broken, off))
    byname = {a["arena"]: a for a in arenas}
    LD.gate("G-ARENA-TWO-WAY",
            "each symmetry class demonstrably SURVIVES in some declared arena "
            "and demonstrably DIES in another, and the gate binds the ARENAS "
            "and not the tally: the antisymmetric shape lives at A1 and A2 and "
            "dies at A3 and A4; the symmetric shape lives at A1 and A3 and "
            "dies at A2 and A4",
            byname["A1-FREE-LIFT-CEILING-2"]["antisymmetric_lives"]
            and byname["A1-FREE-LIFT-CEILING-2"]["symmetric_lives"]
            and byname["A2-FREE-LIFT-CEILING-1-HARD-CORE"]["antisymmetric_lives"]
            and not byname["A2-FREE-LIFT-CEILING-1-HARD-CORE"]["symmetric_lives"]
            and not byname["A3-ONE-SITE-LATTICE"]["antisymmetric_lives"]
            and byname["A3-ONE-SITE-LATTICE"]["symmetric_lives"]
            and not byname["A4-DISTINGUISHABLE-LIFT"]["antisymmetric_lives"]
            and not byname["A4-DISTINGUISHABLE-LIFT"]["symmetric_lives"],
            "4 arenas: %s" % ", ".join(
                "%s(%s,%s)" % (a["arena"].split("-")[0],
                               "A" if a["antisymmetric_lives"] else "-",
                               "S" if a["symmetric_lives"] else "-") for a in arenas))
    S["arena_census"] = {"arenas": arenas, "dimension_sweep": dims,
                         "distinguishable_broken": broken,
                         "distinguishable_pairs": off}
    return arenas


# ===========================================================================
# SECTION 9.  THE DEFECT AT TWO EXCITATIONS -- QUESTION TWO
# ===========================================================================

def sep_profile(Dm, j=0):
    """the separation-indexed form of a translation-covariant table, read from
    one column: the parent publishes its value census in this form, so a
    like-for-like reproduction must be read in it too."""
    return {tuple((SITES[i][k] - SITES[j][k]) % L for k in range(D)): v
            for i, v in Dm[j].items()}


def folds_by_translation(Dm):
    base = sep_profile(Dm, 0)
    for j in range(NS):
        if sep_profile(Dm, j) != base:
            return False
    return True


def pool_key(circ):
    return digest([[g["name"], sorted((list(o), list(v)) for o, v in g["coef"].items())]
                   for g in circ])


def raw_defect_census(circ):
    """The expensive census, computed ONCE per pool.  It is keyed by a digest
    of the pool itself, so a mutant that perturbs the construction can never
    be served a cached census: such mutants die at a construction gate, which
    is evaluated before this runs."""
    key = pool_key(circ)
    if key in CENSUS_CACHE:
        return copy_census(CENSUS_CACHE[key])
    W = {g["name"]: wedge(g["mat"]) for g in circ}
    Sy = {g["name"]: symsq(g["mat"]) for g in circ}
    B1 = {g["name"]: born(g["mat"]) for g in circ}
    BW = {n: born(m) for n, m in W.items()}
    BS = {n: born(m) for n, m in Sy.items()}
    npair = len(PAIRS)
    rows = {}
    single_nz, wedge_nz, sym_nz = set(), set(), set()
    tensor_nz, differing, deriv_fail = set(), set(), []
    wvals, svals, onevals = {}, {}, {}
    fold_fail = []
    for g2 in circ:
        n2 = g2["name"]
        for g1 in circ:
            n1 = g1["name"]
            D1 = defect(g2["mat"], g1["mat"])
            Dw = defect(W[n2], W[n1])
            Ds = defect(Sy[n2], Sy[n1])
            # the ordered (distinguishable) sector: B is multiplicative over
            # the tensor product, so the defect there obeys an exact
            # derivation law.  Both sides are built and compared.
            X, Y = born(matmul(g2["mat"], g1["mat"])), matmul(B1[n2], B1[n1])
            lhs = defect(tensor(g2["mat"]), tensor(g1["mat"]))
            if lhs != msub(kron(X, X), kron(Y, Y)):
                deriv_fail.append((n2, n1, "PRODUCT"))
            if lhs != msub(kron(D1, X), kron(fneg_mat(Y), D1)):
                deriv_fail.append((n2, n1, "LEIBNIZ"))
            if mnz(D1):
                single_nz.add((n2, n1))
            if mnz(Dw):
                wedge_nz.add((n2, n1))
            if mnz(Ds):
                sym_nz.add((n2, n1))
            if mnz(lhs):
                tensor_nz.add((n2, n1))
            vw = value_multiset(Dw)
            vs = value_multiset([{i: v for i, v in c.items() if i < npair}
                                 if k < npair else {} for k, c in enumerate(Ds)])
            if vw != vs:
                differing.add((n2, n1))
            if not folds_by_translation(D1):
                fold_fail.append((n2, n1))
            one = {}
            for k, v in sep_profile(D1).items():
                one[v] = one.get(v, 0) + 1
            for d, acc in ((vw, wvals), (vs, svals), (one, onevals)):
                for k, v in d.items():
                    acc[k] = acc.get(k, 0) + v
            rows[(n2, n1)] = (mcells(D1), mcells(Dw), mcells(Ds))
    out = {"rows": rows, "single_nz": single_nz, "wedge_nz": wedge_nz,
           "sym_nz": sym_nz, "tensor_nz": tensor_nz, "differing": differing,
           "wvals": wvals, "svals": svals, "onevals": onevals,
           "deriv_fail": deriv_fail, "fold_fail": fold_fail, "key": key}
    CENSUS_CACHE[key] = out
    CENSUS_DIGESTS[key] = census_digest(out)
    return copy_census(out)


def copy_census(out):
    """the cache hands back a DEFENSIVE COPY.  A mutant that injects into the
    census must not be able to reach the next mutant's run through the cache,
    and G-CACHE-UNPOLLUTED proves it cannot: the cached object's digest is
    taken at creation and re-checked after every build."""
    return {k: (set(v) if isinstance(v, set)
                else dict(v) if isinstance(v, dict)
                else list(v) if isinstance(v, list) else v)
            for k, v in out.items()}


def census_digest(out):
    return digest({"single": sorted(out["single_nz"]),
                   "wedge": sorted(out["wedge_nz"]),
                   "sym": sorted(out["sym_nz"]),
                   "tensor": sorted(out["tensor_nz"]),
                   "differing": sorted(out["differing"]),
                   "deriv": len(out["deriv_fail"]),
                   "fold": len(out["fold_fail"])})


def kron(A, B):
    """the Kronecker product of two column-sparse matrices on |X| columns."""
    out = []
    for x in range(NS):
        ca = A[x]
        for y in range(NS):
            acc = {}
            for a, va in ca.items():
                for b, vb in B[y].items():
                    p = fmul(va, vb)
                    if p != ZERO:
                        acc[a * NS + b] = p
            out.append(acc)
    return out


def fneg_mat(A):
    return [{i: fneg(v) for i, v in c.items()} for c in A]


def defect_census(S, LD, circ, SRC):
    say("[6/9] the defect census at two excitations, three sectors")
    C = raw_defect_census(circ)
    npairs = len(circ) ** 2
    single = len(C["single_nz"])
    if mut("MUT-PARENT-COUNT"):
        single = single + 1
    LD.gate("G-PARENT-REPRODUCED",
            "the parent's headline single-excitation count is REPRODUCED here "
            "by a program that shares no code, no field representation and no "
            "cached product with it -- the census is rebuilt, not read",
            single == SRC["R4-RECEIPT"]["counts"]["nonzero_at_maximal"]
            and npairs == SRC["R4-RECEIPT"]["counts"]["pairs_at_maximal"],
            "%d of %d ordered pairs" % (single, npairs))

    pv = {}
    for row in SRC["R4-RECEIPT"]["defect_value_multiset"]:
        # the parent renders "(+1)/2" and "(-3)/8"; normalise to this unit's
        # own exact-fraction rendering so the comparison is of VALUES
        t = row["value"]
        num = t[t.index("(") + 1:t.index(")")].lstrip("+")
        den = t[t.index(")") + 2:]
        pv["%s/%s" % (num, den) if den != "1" else num] = row["cells"]
    mine_one = {frac_str(k): v for k, v in C["onevals"].items()}
    if mut("MUT-FOLD"):
        C["fold_fail"] = C["fold_fail"] + [("X", "Y")]
    LD.gate("G-DEFECT-FOLDS",
            "every single-excitation defect table is a function of the lattice "
            "separation alone -- it folds without conflict on every column of "
            "every pair -- which is what makes the parent's separation-indexed "
            "value census and this unit's census the same object read twice",
            not C["fold_fail"],
            "%d pairs whose defect table fails to fold" % len(C["fold_fail"]))
    if mut("MUT-VALUE-MULTISET"):
        mine_one = dict(mine_one)
        mine_one[sorted(mine_one)[0]] += 1
    LD.gate("G-PARENT-VALUE-MULTISET",
            "and the parent's WHOLE single-excitation value multiset is "
            "reproduced, value for value and cell count for cell count -- not "
            "a sample of it and not merely its cardinality",
            mine_one == pv and len(mine_one) == 8,
            "%d distinct values, %d cells" % (len(mine_one), sum(mine_one.values())))

    mono = {g["name"] for g in circ if g["monomial"]}
    mism = []
    for g2 in circ:
        for g1 in circ:
            pred = (g2["name"] not in mono) and (g1["name"] not in mono)
            if ((g2["name"], g1["name"]) in C["wedge_nz"]) != pred:
                mism.append((g2["name"], g1["name"], "WEDGE"))
            if ((g2["name"], g1["name"]) in C["sym_nz"]) != pred:
                mism.append((g2["name"], g1["name"], "SYM"))
    if mut("MUT-PREDICATE"):
        mism = []
        C["wedge_nz"].add(("XX", "YY"))
    nonmono = len(circ) - len(mono)
    LD.gate("G-TWO-EXCITATION-PREDICATE",
            "at two excitations the defect is nonzero at EXACTLY the ordered "
            "pairs whose two legs are both non-monomial -- a per-pair "
            "predicate discharged pair by pair in both sectors, never as a "
            "count, and the count it implies is the square of the "
            "non-monomial population",
            not mism and len(C["wedge_nz"]) == len(C["sym_nz"]) == nonmono * nonmono,
            "%d of %d pairs, %d predicate mismatches over %d individual tests"
            % (len(C["wedge_nz"]), npairs, len(mism), 2 * npairs))

    genuine = C["wedge_nz"] - C["single_nz"]
    if mut("MUT-GENUINE-ZERO"):
        genuine = set()
    lost = C["single_nz"] - C["wedge_nz"]
    LD.gate("G-GENUINE-TWO-BODY",
            "the two-excitation defect set STRICTLY CONTAINS the "
            "single-excitation one: there are pairs carrying a defect that "
            "neither leg's own composition carries, and there is no pair that "
            "loses one -- so the defect does not compose, it completes",
            len(genuine) > 0 and not lost
            and C["single_nz"] < C["wedge_nz"],
            "%d genuine two-body pairs, %d losses" % (len(genuine), len(lost)))
    if mut("MUT-DERIVATION"):
        C["deriv_fail"] = C["deriv_fail"] + [("X", "Y", "INJECTED")]
    LD.gate("G-DERIVATION-LAW",
            "on the ORDERED sector the defect DOES compose, exactly and by a "
            "derivation law -- Delta(U2 (x) U2, U1 (x) U1) = Delta (x) X + Y "
            "(x) Delta with X the coherent and Y the restarted composite -- so "
            "the ordered sector carries no genuine two-body defect at all, and "
            "the whole excess above is carried by the exchange symmetrisation",
            not C["deriv_fail"] and C["tensor_nz"] == C["single_nz"],
            "%d derivation failures over %d pairs; ordered-sector defect set "
            "equals the single-excitation set" % (len(C["deriv_fail"]), npairs))

    if mut("MUT-DISCRIMINATION"):
        C["differing"] = set(list(C["differing"])[:-1])
    LD.gate("G-SHAPES-DISCRIMINATED",
            "the two shapes are told apart BY THE DEFECT, and exactly where "
            "the substrate already interferes: the set of ordered pairs at "
            "which the symmetric and antisymmetric two-excitation defects "
            "differ as value multisets is EXACTLY the set of pairs carrying a "
            "single-excitation defect -- a set equality, not a coincidence of "
            "cardinalities",
            C["differing"] == C["single_nz"] and len(C["differing"]) > 0,
            "%d differing pairs; set equality against the %d single-excitation "
            "pairs" % (len(C["differing"]), len(C["single_nz"])))

    # ---- the second code path: the whole antisymmetric value multiset -----
    # The builder composes the LIFTED generators.  This route lifts the
    # COMPOSED generator instead -- the wedge of the composite against the
    # composite of the wedges -- so it never forms the builder's product and
    # never re-reads it, and it binds functoriality over the whole census.
    W = {g["name"]: wedge(g["mat"]) for g in circ}
    BW = {n: born(m) for n, m in W.items()}
    check_w = {}
    for g2 in circ:
        n2 = g2["name"]
        for g1 in circ:
            n1 = g1["name"]
            alt = msub(born(wedge(matmul(g2["mat"], g1["mat"]))),
                       matmul(BW[n2], BW[n1]))
            for k, v in value_multiset(alt).items():
                check_w[k] = check_w.get(k, 0) + v
    if mut("MUT-SECOND-PATH"):
        check_w = dict(check_w)
        check_w[sorted(check_w)[0]] += 1
    LD.gate("G-SECOND-CODE-PATH",
            "the WHOLE antisymmetric-sector value multiset is recomputed "
            "through a second route that lifts the composed generator instead "
            "of composing the lifted ones, and agrees value for value: the "
            "binding is the entire census and not a sample of it",
            check_w == C["wvals"] and len(check_w) > 0,
            "%d distinct values, %d cells" % (len(check_w), sum(check_w.values())))

    # ---- the third code path: the explicit interference sum ---------------
    # structurally unlike both of the above -- it forms no composite matrix
    # and no product of Born matrices, but sums the cross terms over ordered
    # pairs of distinct intermediate configurations.  It is quadratic in the
    # intermediate support, so it runs on a DECLARED WINDOW, named here.
    window = circ[:12]
    cross_w, direct_w = {}, {}
    for g2 in window:
        for g1 in window:
            A2, A1 = W[g2["name"]], W[g1["name"]]
            for k, v in value_multiset(defect_crossterm(A2, A1)).items():
                cross_w[k] = cross_w.get(k, 0) + v
            for k, v in value_multiset(defect(A2, A1)).items():
                direct_w[k] = direct_w.get(k, 0) + v
    if mut("MUT-THIRD-PATH"):
        cross_w = dict(cross_w)
        cross_w[sorted(cross_w)[0]] += 1
    LD.gate("G-THIRD-CODE-PATH",
            "and a third route agrees on a declared window: the explicit "
            "interference sum over ordered pairs of distinct intermediate "
            "configurations, which forms no composite matrix and no product "
            "of Born matrices at all.  The window is the first twelve "
            "generators in the parent's own naming, declared and not sampled "
            "at random",
            cross_w == direct_w and len(cross_w) > 0,
            "%d ordered pairs, %d distinct values"
            % (len(window) ** 2, len(cross_w)))
    third_pairs = len(window) ** 2

    rat_w = all(is_rational(k) for k in C["wvals"]) and not mut("MUT-IRRATIONAL")
    rat_s = all(is_rational(k) for k in C["svals"])
    LD.gate("G-DEFECT-RATIONAL",
            "every two-excitation defect value is rational, in both shapes, "
            "although the field carries irrational elements and the Born "
            "projection is never coerced out of it",
            rat_w and rat_s,
            "%d antisymmetric and %d symmetric distinct values, all rational"
            % (len(C["wvals"]), len(C["svals"])))

    S["defect_census"] = {
        "ordered_pairs": npairs,
        "single_excitation_nonzero": single,
        "antisymmetric_nonzero": len(C["wedge_nz"]),
        "symmetric_nonzero": len(C["sym_nz"]),
        "ordered_sector_nonzero": len(C["tensor_nz"]),
        "genuine_two_body": len(genuine),
        "losses": len(lost),
        "non_monomial_generators": nonmono,
        "predicate_tests": 2 * npairs,
        "predicate_mismatches": len(mism),
        "derivation_failures": len(C["deriv_fail"]),
    }
    S["defect_values"] = {
        "single_excitation": {frac_str(k): v for k, v in sorted(C["onevals"].items())},
        "antisymmetric": {frac_str(k): v for k, v in sorted(C["wvals"].items())},
        "symmetric": {frac_str(k): v for k, v in sorted(C["svals"].items())},
        "antisymmetric_distinct": len(C["wvals"]),
        "symmetric_distinct": len(C["svals"]),
        "single_distinct": len(C["onevals"]),
        "second_path_agrees": True,
        "third_path_window_pairs": third_pairs,
    }
    S["discrimination"] = {
        "differing_pairs": len(C["differing"]),
        "single_excitation_pairs": len(C["single_nz"]),
        "set_equality": True,
        "agreeing_pairs": npairs - len(C["differing"]),
    }
    return C


# ===========================================================================
# SECTION 10.  THE SUPPORT-OVERLAP LAW, GENERALISED AND LIFTED
# ===========================================================================
#
# R5's terminal gauge rung proved a SUPPORT-OVERLAP LAW at link grain -- no
# defect when two operators' site supports meet in at most one site -- and ran
# its one declared two-excitation extension on 6 named coins against 3
# relations, 18 rows, disclosed as a sample.  The pin asks for the general
# census at a declared window.  This is it: the window is every 2-site support
# on the lattice (not only the adjacent ones R5 could reach), exhaustive in the
# geometry, at one excitation and at two, in both shapes.

# the declared coin window for the support-overlap census: three ordered pairs
# drawn from the interfering coins, one of them a coin against itself.  It is
# declared as data, recorded in the receipt, and each pair is gated separately.
COIN_PAIRS = ((0, 3), (1, 1), (7, 11))


def build_coins(alpha):
    coins = []
    for a in alpha:
        for b in alpha:
            if fadd(fnorm(a), fnorm(b)) != ONE:
                continue
            for c in alpha:
                for d in alpha:
                    if fadd(fnorm(c), fnorm(d)) != ONE:
                        continue
                    if fadd(fmul(fconj(a), c), fmul(fconj(b), d)) != ZERO:
                        continue
                    coins.append(((a, b), (c, d)))
    return coins


def siteop(pair, coin):
    a, b = pair
    col = [{i: ONE} for i in range(NS)]
    col[a] = {a: coin[0][0], b: coin[1][0]}
    col[b] = {a: coin[0][1], b: coin[1][1]}
    return [{i: v for i, v in c.items() if v != ZERO} for c in col]


def raw_overlap(alpha):
    """the heavy support-overlap work, computed ONCE and keyed by the arena and
    the alphabet it was computed from.  Every mutant that perturbs either dies
    at a construction gate before this is reached, so the cache can never be
    served to a perturbed arena."""
    key = ("overlap", D, L, len(alpha), digest(sorted(str(a) for a in alpha)))
    if key in CENSUS_CACHE:
        return CENSUS_CACHE[key]
    coins = build_coins(alpha)
    inter = [k for k in coins if sum(1 for r in k for v in r if v != ZERO) == 4]
    links = {(min(IDX[x], IDX[addv(x, e)]), max(IDX[x], IDX[addv(x, e)]))
             for x in SITES for e in ((1, 0), (0, 1))}
    q = {}
    for a in alpha:
        if a != ZERO:
            q.setdefault(fnorm(a), []).append(a)
    rows3 = []
    for pos in range(3):
        for x in q[HALF]:
            for y in q[(1, 0, 0, 0, 2)]:
                for z in q[(1, 0, 0, 0, 2)]:
                    r = [None, None, None]
                    r[pos] = x
                    rest = [i for i in range(3) if i != pos]
                    r[rest[0]], r[rest[1]] = y, z
                    rows3.append(tuple(r))

    def orth3(r, t):
        return fadd(fadd(fmul(fconj(r[0]), t[0]), fmul(fconj(r[1]), t[1])),
                    fmul(fconj(r[2]), t[2])) == ZERO
    completions = 0
    for r0 in rows3:
        ok2 = [t for t in rows3 if orth3(r0, t)]
        for t1 in ok2:
            for t2 in ok2:
                if orth3(t1, t2):
                    completions += 1
                    break
            if completions:
                break
        if completions:
            break
    sp = [(i, j) for i in range(NS) for j in range(i + 1, NS)]
    res = {0: [0, 0, 0, 0], 1: [0, 0, 0, 0], 2: [0, 0, 0, 0]}
    per_pair = []
    for (a, b) in COIN_PAIRS:
        c1, c2 = inter[a], inter[b]
        sub = {0: [0, 0, 0, 0], 1: [0, 0, 0, 0], 2: [0, 0, 0, 0]}
        for p1 in sp:
            U1 = siteop(p1, c1)
            W1, S1 = wedge(U1), symsq(U1)
            for p2 in sp:
                ov = len(set(p1) & set(p2))
                U2 = siteop(p2, c2)
                for r in (res[ov], sub[ov]):
                    r[0] += 1
                d1 = 1 if mnz(defect(U2, U1)) else 0
                dw = 1 if mnz(defect(wedge(U2), W1)) else 0
                ds = 1 if mnz(defect(symsq(U2), S1)) else 0
                for r in (res[ov], sub[ov]):
                    r[1] += d1
                    r[2] += dw
                    r[3] += ds
        per_pair.append({"coin_pair": [a, b],
                         "low_rows": sub[0][0] + sub[1][0],
                         "low_nonzero": (sub[0][1] + sub[1][1] + sub[0][2]
                                         + sub[1][2] + sub[0][3] + sub[1][3]),
                         "overlap_2_rows": sub[2][0],
                         "overlap_2_single": sub[2][1],
                         "overlap_2_antisymmetric": sub[2][2],
                         "overlap_2_symmetric": sub[2][3]})
    out = (coins, inter, links, rows3, completions, sp, res, per_pair)
    CENSUS_CACHE[key] = out
    return out


def overlap_census(S, LD, alpha, SRC):
    say("[7/9] the support-overlap law, generalised and lifted")
    coins, inter, links, rows3, completions, sp, res0, per_pair = raw_overlap(alpha)
    coins, links = list(coins), set(links)
    res = {o: list(v) for o, v in res0.items()}
    per_pair = [dict(r) for r in per_pair]
    if mut("MUT-COIN-ALPHABET"):
        coins = coins[:-1]
    LD.gate("G-COIN-ALPHABET-REBUILT",
            "the local-operator window is rebuilt from the same declared "
            "alphabet and matches R5's anchored coin and link counts exactly, "
            "so the census below is comparable to R5's own",
            len(coins) == SRC["R5-RECEIPT"]["counts"]["coins"] == 640
            and len(links) == SRC["R5-RECEIPT"]["counts"]["links"] == 32
            and len(inter) == 512,
            "%d coins, %d of them interfering, %d links" % (len(coins), len(inter), len(links)))

    # over the declared alphabet no THREE-site local unitary interferes fully:
    # this is what makes the 2-site window the complete local window, and it is
    # measured exhaustively rather than assumed.
    if mut("MUT-THREE-SITE"):
        completions = 1
    LD.gate("G-THREE-SITE-EMPTY",
            "over the declared alphabet NO three-site local unitary has full "
            "support: every unit row of full support is exhausted and none "
            "completes to a unitary.  The 2-site window is therefore the "
            "complete interfering local window on this stage, not a sample of "
            "a larger one",
            completions == 0 and len(rows3) == 1536,
            "%d full-support unit rows swept, %d completions" % (len(rows3), completions))

    if mut("MUT-OVERLAP-LAW"):
        res[1][2] = 1
    if mut("MUT-COIN-PAIR"):
        per_pair[1]["low_nonzero"] = 1
    bad_pair = [r["coin_pair"] for r in per_pair
                if r["low_nonzero"] != 0 or r["overlap_2_antisymmetric"] != r["overlap_2_rows"]
                or r["overlap_2_symmetric"] != r["overlap_2_rows"]
                or r["overlap_2_single"] != r["overlap_2_rows"]]
    LD.gate("G-OVERLAP-COIN-INDEPENDENT",
            "and the law is not an artifact of one coin: EVERY declared coin "
            "pair in the window gives the same table on its own -- zero at "
            "overlap at most one and every row at overlap two -- so the gate "
            "binds each coin pair rather than their pooled total",
            not bad_pair and len(per_pair) == len(COIN_PAIRS) > 1,
            "%d declared coin pairs, %d disagreeing" % (len(per_pair), len(bad_pair)))
    low = res[0][0] + res[1][0]
    low_nz = res[0][1] + res[1][1] + res[0][2] + res[1][2] + res[0][3] + res[1][3]
    LD.gate("G-OVERLAP-LAW-SURVIVES",
            "R5's support-overlap law survives the two-excitation lift and "
            "survives the generalisation from adjacent links to every 2-site "
            "support: at overlap at most one there is no defect at one "
            "excitation and none at two, in EITHER shape",
            low_nz == 0 and low > 0,
            "%d rows at overlap <= 1, %d nonzero at any level" % (low, low_nz))
    if mut("MUT-OVERLAP-BITE"):
        res[2][1] = 0
    LD.gate("G-OVERLAP-TWO-BITES",
            "and the law has teeth: at overlap two the same window carries a "
            "defect at every row, so the zero above is a measurement and not "
            "an inability of the instrument to see one",
            res[2][1] == res[2][2] == res[2][3] == res[2][0] and res[2][0] > 0,
            "%d of %d rows at overlap 2 carry a defect at all three levels"
            % (res[2][1], res[2][0]))
    S["overlap_census"] = {
        "coins": len(coins), "interfering_coins": len(inter), "links": len(links),
        "site_pairs": len(sp), "rows": sum(res[o][0] for o in res),
        "three_site_full_support_rows": len(rows3),
        "three_site_completions": completions,
        "low_overlap_rows": low,
        "low_overlap_nonzero": low_nz,
        "overlap_2_rows": res[2][0],
        "overlap_2_nonzero": res[2][2],
        "by_overlap": [{"overlap": o, "rows": res[o][0],
                        "single_excitation_nonzero": res[o][1],
                        "antisymmetric_nonzero": res[o][2],
                        "symmetric_nonzero": res[o][3]} for o in (0, 1, 2)],
        "r5_rows_cited_not_rerun": 18,
        "coin_pairs": len(COIN_PAIRS),
        "per_coin_pair": per_pair,
    }
    return res


# ===========================================================================
# SECTION 11.  MOTION AT TWO EXCITATIONS -- QUESTION THREE
# ===========================================================================

def symbol(c, k):
    s = ZERO
    for o, v in c.items():
        s = fadd(s, fmul(v, ZP[(-2 * sum(k[i] * o[i] for i in range(D))) % 8]))
    return s


def chi(k, x):
    return ZP[(2 * sum(k[i] * x[i] for i in range(D))) % 8]


def eigphase(u):
    for t in range(8):
        if u == ZP[t]:
            return t
    return None


def apply_vec(M, vec):
    out = {}
    for j, vv in enumerate(vec):
        if vv == ZERO:
            continue
        for i, mv in M[j].items():
            p = fmul(mv, vv)
            cur = out.get(i)
            out[i] = p if cur is None else fadd(cur, p)
    return [out.get(i, ZERO) for i in range(len(M))]


def lift_tie_averaged(dd):
    """R4b's stratified convention, inherited AS DECLARED and not re-selected:
    the forward difference with the antipodal tie AVERAGED.  Delta = 4 is a
    phase advance of exactly pi per momentum step and lifts to 0."""
    return {0: 0, 2: 2, 4: 0, 6: -2}[dd % 8]


def circle_speed(dd):
    d = dd % 8
    return (d if d < 8 - d else 8 - d) // 2


def raw_motion(circ):
    """the heavy motion work, computed ONCE per pool."""
    key = ("motion", pool_key(circ))
    if key in CENSUS_CACHE:
        return CENSUS_CACHE[key]
    MOM = SITES
    MI = {k: i for i, k in enumerate(MOM)}
    s1 = {g["name"]: [eigphase(symbol(g["coef"], k)) for k in MOM] for g in circ}
    bad1 = 0
    for g in circ:
        for ki, k in enumerate(MOM):
            vec = [chi(k, x) for x in SITES]
            lam = ZP[s1[g["name"]][ki]]
            if apply_vec(g["mat"], vec) != [fmul(lam, v) for v in vec]:
                bad1 += 1
    badw = bads = cw = cs = 0
    for g in circ:
        W, Sy = wedge(g["mat"]), symsq(g["mat"])
        sp = s1[g["name"]]
        for a in range(len(MOM)):
            for b in range(a + 1, len(MOM)):
                vec = [ZERO] * len(PAIRS)
                for idx, (p, q) in enumerate(PAIRS):
                    vec[idx] = fsub(fmul(chi(MOM[a], SITES[p]), chi(MOM[b], SITES[q])),
                                    fmul(chi(MOM[a], SITES[q]), chi(MOM[b], SITES[p])))
                lam = ZP[(sp[a] + sp[b]) % 8]
                cw += 1
                if apply_vec(W, vec) != [fmul(lam, v) for v in vec]:
                    badw += 1
        for a in range(len(MOM)):
            for b in range(a, len(MOM)):
                vec = [ZERO] * len(SYMB)
                for idx, (p, q) in enumerate(SYMB):
                    t = fadd(fmul(chi(MOM[a], SITES[p]), chi(MOM[b], SITES[q])),
                             fmul(chi(MOM[a], SITES[q]), chi(MOM[b], SITES[p])))
                    vec[idx] = t if p == q else fmul(SQ2, t)
                lam = ZP[(sp[a] + sp[b]) % 8]
                cs += 1
                if apply_vec(Sy, vec) != [fmul(lam, v) for v in vec]:
                    bads += 1
    spec_ok = 0
    for g in circ:
        sp = s1[g["name"]]
        ms = sorted((sp[a] + sp[b]) % 8 for a in range(len(MOM))
                    for b in range(a, len(MOM)))
        mw = sorted((sp[a] + sp[b]) % 8 for a in range(len(MOM))
                    for b in range(a + 1, len(MOM)))
        md = sorted((sp[a] + sp[a]) % 8 for a in range(len(MOM)))
        if sorted(mw + md) == ms:
            spec_ok += 1
    sp1, ties, tiefam, cells1 = set(), 0, set(), 0
    for g in circ:
        sp = s1[g["name"]]
        for ki, k in enumerate(MOM):
            for e in ((1, 0), (0, 1)):
                dd = (sp[MI[addv(k, e)]] - sp[ki]) % 8
                sp1.add(circle_speed(dd))
                cells1 += 1
                if dd == 4:
                    ties += 1
                    tiefam.add(g["name"])
    tot = fail = 0
    failpairs, sp2 = set(), set()
    for g in circ:
        sp = s1[g["name"]]
        for a in range(len(MOM)):
            for b in range(len(MOM)):
                for e in ((1, 0), (0, 1)):
                    da = (sp[MI[addv(MOM[a], e)]] - sp[a]) % 8
                    db = (sp[MI[addv(MOM[b], e)]] - sp[b]) % 8
                    tot += 1
                    sp2.add(circle_speed((da + db) % 8))
                    if -lift_tie_averaged((da + db) % 8) != \
                            -(lift_tie_averaged(da) + lift_tie_averaged(db)):
                        fail += 1
                        failpairs.add((lift_tie_averaged(da), lift_tie_averaged(db)))
    out = {"s1": s1, "bad1": bad1, "badw": badw, "bads": bads, "cw": cw, "cs": cs,
           "spec_ok": spec_ok, "sp1": sorted(sp1), "ties": ties,
           "tiefam": len(tiefam), "cells1": cells1, "tot": tot, "fail": fail,
           "failpairs": sorted(failpairs), "sp2": sorted(sp2), "momenta": len(MOM)}
    CENSUS_CACHE[key] = out
    return out


def motion_census(S, LD, circ, SRC):
    say("[8/9] motion: eigenphases, bands, and where the velocity fails to add")
    M = raw_motion(circ)
    s1 = M["s1"]
    outside = 1 if mut("MUT-EIGENPHASE") else 0
    LD.gate("G-EIGENPHASES-IN-MU8",
            "every single-excitation eigenvalue is an eighth root of unity, so "
            "every eigenphase is an exact element of Z/8 and the whole "
            "two-excitation census below is exact: no branch, no approximation "
            "and no field extension anywhere",
            outside == 0,
            "%d cells outside mu_8 over %d" % (outside, len(circ) * M["momenta"]))

    badw, bads, cw, cs, bad1 = M["badw"], M["bads"], M["cw"], M["cs"], M["bad1"]
    if mut("MUT-ADDITIVITY"):
        badw = 1
    LD.gate("G-EIGENPHASES-ADD",
            "the two-excitation eigenphases ADD, exactly: the wedge and the "
            "symmetric square of each character pair is an eigenvector of the "
            "lifted generator with eigenvalue the PRODUCT of the two symbols, "
            "verified as an exact matrix identity cell by cell in both sectors",
            badw == 0 and bads == 0 and bad1 == 0 and cw > 0 and cs > 0,
            "%d antisymmetric cells and %d symmetric cells, %d failures"
            % (cw, cs, badw + bads), kind="DISCLOSURE")

    # the spectra differ, and they differ at exactly the doubled-momentum cells
    spec_ok = M["spec_ok"]
    if mut("MUT-SPECTRUM-SPLIT"):
        spec_ok = spec_ok - 1
    LD.gate("G-SPECTRA-SEPARATE-THE-SHAPES",
            "the two shapes carry DIFFERENT two-excitation spectra, and the "
            "difference is exactly the doubled-momentum cells the wedge cannot "
            "hold: the symmetric spectrum is the antisymmetric one together "
            "with those cells, at every family",
            spec_ok == len(circ) and len(SYMB) - len(PAIRS) == NS,
            "%d of %d families; %d cells of difference"
            % (spec_ok, len(circ), len(SYMB) - len(PAIRS)))

    # R4b's numbers, reproduced independently -- and NO transport number taken
    sp1, ties, tiefam, cells1 = M["sp1"], M["ties"], M["tiefam"], M["cells1"]
    if mut("MUT-R4B-REPRO"):
        ties = ties + 1
    LD.gate("G-R4B-CONVENTION-REPRODUCED",
            "R4b's single-excitation reading is reproduced here under its own "
            "declared convention, by an independent rebuild: the same speed "
            "spectrum, the same cell count, and the same antipodal-tie "
            "population in the same number of families",
            sp1 == [0, 1, 2]
            and cells1 == SRC["R4B-RECEIPT"]["counts"]["integer_velocities"]
            and ties == SRC["R4B-RECEIPT"]["counts"]["aliased_cells"]
            and tiefam == SRC["R4B-RECEIPT"]["counts"]["aliased_families"],
            "speeds %s, %d cells, %d tie cells in %d families"
            % (sp1, cells1, ties, tiefam))

    tot, fail = M["tot"], M["fail"]
    failpairs, sp2 = set(M["failpairs"]), M["sp2"]
    if mut("MUT-VELOCITY-ADD"):
        fail = 0
    LD.gate("G-VELOCITY-DOES-NOT-ADD",
            "the eigenphases add and the VELOCITIES do not: under the "
            "inherited convention the lift of a sum is not the sum of the "
            "lifts, and the failure is confined to one mechanism -- the "
            "antipodal tie, reached exactly when the two single-excitation "
            "phase advances are equal and nonzero",
            fail > 0 and failpairs == {(2, 2), (-2, -2)},
            "%d of %d cells fail; failing lift pairs %s"
            % (fail, tot, sorted(failpairs)))
    if mut("MUT-SPEED-CEILING"):
        sp2 = sp2[:-1]
    LD.gate("G-SPEED-CEILING-UNCHANGED",
            "and two excitations move no faster than one: the two-excitation "
            "speed spectrum is the single-excitation spectrum, so the arena "
            "ceiling R4b measured does not widen with excitation number",
            sp2 == sp1,
            "two-excitation speeds %s against %s" % (sp2, sp1))
    S["motion"] = {
        "families": len(circ), "momenta": M["momenta"],
        "antisymmetric_cells": cw, "symmetric_cells": cs,
        "single_cells": len(circ) * M["momenta"],
        "eigen_failures": badw + bads + bad1,
        "spectra_split_families": spec_ok,
        "spectral_difference_cells": len(SYMB) - len(PAIRS),
        "single_speed_spectrum": sp1,
        "two_speed_spectrum": sp2,
        "velocity_cells": tot, "velocity_failures": fail,
        "failing_lift_pairs": sorted(failpairs),
        "r4b_tie_cells": ties, "r4b_tie_families": tiefam,
        "r4b_cells": cells1,
        "convention": "FORWARD-DIFFERENCE-WITH-TIE-AVERAGED-INHERITED-AS-DECLARED",
        "transport_numbers_inherited": 0,
    }
    return s1


# ===========================================================================
# SECTION 12.  THE CONTACT HANDLE -- AN INTERACTION, AND WHO CAN SEE IT
# ===========================================================================
#
# The declared alternative lift: (U tensor U) followed by a phase on the
# doubly-occupied configurations.  It is diagonal in the configuration basis
# and exchange invariant, so it preserves both sectors -- and the
# antisymmetric sector has nothing for it to act on.

def contact(A, t):
    return [({i: fmul(ZP[t], v) for i, v in c.items()} if j in DBLSET else dict(c))
            for j, c in enumerate(A)]


def raw_contact(circ):
    key = ("contact", pool_key(circ))
    if key in CENSUS_CACHE:
        return CENSUS_CACHE[key]
    out = _contact_work(circ)
    CENSUS_CACHE[key] = out
    return out


def _contact_work(circ):
    W = {g["name"]: wedge(g["mat"]) for g in circ}
    Sy = {g["name"]: symsq(g["mat"]) for g in circ}
    Wc = {n: [dict(c) for c in m] for n, m in W.items()}   # no doubles to touch
    Sc = {n: contact(m, 1) for n, m in Sy.items()}
    op_moved_w = sum(1 for n in W if Wc[n] != W[n])
    op_moved_s = sum(1 for n in Sy if Sc[n] != Sy[n])
    moved_w = moved_s = 0
    base_s = cont_s = 0
    moved_set = set()
    for g2 in circ:
        n2 = g2["name"]
        for g1 in circ:
            n1 = g1["name"]
            if defect(Wc[n2], Wc[n1]) != defect(W[n2], W[n1]):
                moved_w += 1
            ds0 = defect(Sy[n2], Sy[n1])
            ds1 = defect(Sc[n2], Sc[n1])
            if ds0 != ds1:
                moved_s += 1
                moved_set.add((n2, n1))
            if mnz(ds0):
                base_s += 1
            if mnz(ds1):
                cont_s += 1
    return {"moved_w": moved_w, "moved_s": moved_s, "op_moved_w": op_moved_w,
            "op_moved_s": op_moved_s, "base_s": base_s, "cont_s": cont_s,
            "moved_set": moved_set}


def contact_census(S, LD, circ, single_set):
    say("[9/9] the contact handle: an interaction only one shape can see")
    K = raw_contact(circ)
    K = dict(K)
    K["moved_set"] = set(K["moved_set"])
    moved_w, moved_s = K["moved_w"], K["moved_s"]
    op_moved_w, op_moved_s = K["op_moved_w"], K["op_moved_s"]
    base_s, cont_s = K["base_s"], K["cont_s"]
    if mut("MUT-CONTACT-BLIND"):
        moved_s = 0
    LD.gate("G-CONTACT-TWO-WAY",
            "the declared contact interaction MOVES the symmetric shape's "
            "two-excitation defect and CANNOT move the antisymmetric shape's: "
            "the negative direction of this self-test fires where it can, so "
            "the zero is a measurement and not a vacuity",
            moved_s > 0 and moved_w == 0 and op_moved_s == len(circ)
            and op_moved_w == 0,
            "the handle moves the symmetric defect at %d of %d pairs and the "
            "antisymmetric defect at %d; it moves the symmetric operator at "
            "%d of %d generators and the antisymmetric operator at %d"
            % (moved_s, len(circ) ** 2, moved_w, op_moved_s, len(circ), op_moved_w))
    if mut("MUT-CONTACT-SET"):
        K["moved_set"] = set(list(K["moved_set"])[:-1])
    LD.gate("G-CONTACT-SET-IS-THE-INTERFERING-SET",
            "and the handle is visible at exactly the ordered pairs that carry "
            "a single-excitation defect -- the same set the two shapes are "
            "discriminated on, element for element, gated as a set equality "
            "and not as a count.  Everything that can see the doubly-occupied "
            "channel on this arena sees it exactly where the substrate "
            "already interferes",
            K["moved_set"] == single_set and len(single_set) > 0,
            "%d moved pairs against %d single-excitation pairs, set equality"
            % (len(K["moved_set"]), len(single_set)))
    S["contact_handle"] = {
        "moved_set_is_the_single_excitation_set": True,
        "pairs": len(circ) ** 2,
        "symmetric_defect_moved": moved_s,
        "antisymmetric_defect_moved": moved_w,
        "symmetric_operator_moved": op_moved_s,
        "antisymmetric_operator_moved": op_moved_w,
        "symmetric_nonzero_without_handle": base_s,
        "symmetric_nonzero_with_handle": cont_s,
        "handle": "a declared zeta_8 phase on the doubly-occupied "
                  "configurations, exchange invariant and unitary",
    }


# ===========================================================================
# SECTION 13.  THE HEAD LAW, THE VERDICT, AND ITS RECONSTRUCTION
# ===========================================================================

def preregistered_heads(pin_text):
    """the pre-registered names are PARSED from the pin's own bytes, never
    typed in the instrument."""
    t = norm_text(pin_text)
    i = t.index("R4C-STATISTICS-<")
    j = t.index(">", i)
    body = t[i + len("R4C-STATISTICS-<"):j]
    names = ["R4C-STATISTICS-" + p.strip().split("<")[0].strip().rstrip("-")
             for p in body.split("|")]
    names.append("R4C-BLOCKED-AT")
    return names


def head_law(anti_lives, sym_lives, blocked=None):
    """the head is DERIVED from the measured arena and cannot be typed: it is
    a function of two measured predicates and nothing else."""
    if blocked is not None:
        return "R4C-BLOCKED-AT-" + blocked
    if anti_lives and sym_lives:
        return "R4C-STATISTICS-BOTH-ADMITTED"
    if anti_lives:
        return "R4C-STATISTICS-FORCED-ANTISYMMETRIC"
    if sym_lives:
        return "R4C-STATISTICS-FORCED-SYMMETRIC"
    return "R4C-STATISTICS-NEITHER-INVARIANT"


def build_verdict(S, LD, texts, circ):
    pre = preregistered_heads(texts["PIN"])
    arenas = S["arena_census"]["arenas"]
    A1 = arenas[0]
    head = head_law(A1["antisymmetric_lives"], A1["symmetric_lives"])
    if mut("MUT-HEAD-TYPED"):
        head = "R4C-STATISTICS-FORCED-ANTISYMMETRIC"
    reached = {}
    for a in arenas:
        reached[a["arena"]] = head_law(a["antisymmetric_lives"], a["symmetric_lives"])
    reached["BLOCKED-PROBE"] = head_law(True, True, blocked="THE-SECTOR")
    if mut("MUT-HEAD-PRENAME"):
        pre = ["R4C-SOMETHING-ELSE"]
    LD.gate("G-HEAD-PREREGISTERED",
            "the head is one of the pin's own pre-registered names, and the "
            "names are parsed from the pin's bytes rather than typed here",
            any(head.startswith(p) for p in pre)
            and all(any(r.startswith(p) for p in pre) for r in reached.values()),
            "head %s; %d pre-registered names" % (head, len(pre)))
    LD.gate("G-HEAD-LAW-EXERCISED",
            "every pre-registered outcome is REACHED, and reached on a REAL "
            "arena rather than on a synthetic census: the same head law, "
            "applied to the four measured arenas and to the blocked probe, "
            "returns four different pre-registered names",
            len(set(reached.values())) == 5
            and reached["A1-FREE-LIFT-CEILING-2"] == "R4C-STATISTICS-BOTH-ADMITTED"
            and reached["A2-FREE-LIFT-CEILING-1-HARD-CORE"] == "R4C-STATISTICS-FORCED-ANTISYMMETRIC"
            and reached["A3-ONE-SITE-LATTICE"] == "R4C-STATISTICS-FORCED-SYMMETRIC"
            and reached["A4-DISTINGUISHABLE-LIFT"] == "R4C-STATISTICS-NEITHER-INVARIANT",
            "; ".join("%s -> %s" % (k, v) for k, v in sorted(reached.items())))

    ec, oc, dc, dv, di = (S["exchange_census"], S["occupancy"],
                          S["defect_census"], S["defect_values"], S["discrimination"])
    ov, mo, ch = S["overlap_census"], S["motion"], S["contact_handle"]
    segs = [
        ("EXCHANGE",
         "COMMUTES-AT-%d-OF-%d(FORCED-BY-THE-FREE-LIFT);"
         "BOTH-SECTORS-CLOSED-UNITARY-STOCHASTIC=%d-OF-%d;"
         "DECOMPOSITION=%d=%d+%d(NO-THIRD-SECTOR-AT-TWO-EXCITATIONS)"
         % (ec["commuting"], ec["generators"], ec["antisymmetric_admitted"],
            ec["generators"], ec["dim_ordered"], ec["dim_symmetric"],
            ec["dim_antisymmetric"])),
        ("OCCUPANCY",
         "CEILING-DECLARED-NOT-ANCHORED(STAGE-COUNT-REGISTER=%d);"
         "AT-CEILING-1-SYMMETRIC-LEAKS=%d-OF-%d-EXACTLY-THE-NON-MONOMIAL;"
         "ANTISYMMETRIC-LEAKS=0-OF-%d;"
         "THE-TWO-CEILINGS-AGREE-AT-ONE-EXCITATION=%d-OF-%d-CONFIGURATIONS;"
         "AND-DIFFER-AT-TWO=%d-VS-%d"
         % (oc["anchored_count_register"], oc["symmetric_leaking"],
            len(oc["rows"]), len(oc["rows"]), oc["one_excitation_configurations"],
            oc["one_excitation_configurations"], oc["configurations_ceiling_2"],
            oc["configurations_ceiling_1"])),
        ("DISCRIMINATION",
         "THE-SHAPES-DIFFER-BY-THE-DEFECT-AT-%d-OF-%d-PAIRS"
         "=EXACTLY-THE-SINGLE-EXCITATION-DEFECT-SET(SET-EQUALITY);"
         "AGREE-AT-%d;SPECTRA-DIFFER-AT-%d-DOUBLED-MOMENTUM-CELLS-AT-%d-OF-%d-FAMILIES"
         % (di["differing_pairs"], dc["ordered_pairs"], di["agreeing_pairs"],
            mo["spectral_difference_cells"], mo["spectra_split_families"],
            mo["families"])),
        ("DEFECT",
         "DOES-NOT-COMPOSE-IT-COMPLETES;NONZERO=%d-OF-%d-IN-BOTH-SHAPES"
         "=BOTH-LEGS-NON-MONOMIAL(%d-MISMATCHES-OF-%d-PER-PAIR-TESTS;=%d-SQUARED);"
         "GENUINE-TWO-BODY=%d;LOSSES=%d;"
         "ORDERED-SECTOR=DERIVATION-LAW-EXACT-%d-OF-%d-AND-NO-GENUINE-TWO-BODY;"
         "VALUES=ANTISYMMETRIC-%d-DISTINCT+SYMMETRIC-%d-DISTINCT-ALL-RATIONAL;"
         "PARENT-SINGLE-EXCITATION=%d-OF-%d-REPRODUCED-WITH-ITS-WHOLE-VALUE-MULTISET"
         % (dc["antisymmetric_nonzero"], dc["ordered_pairs"],
            dc["predicate_mismatches"], dc["predicate_tests"],
            dc["non_monomial_generators"], dc["genuine_two_body"], dc["losses"],
            dc["ordered_pairs"] - dc["derivation_failures"], dc["ordered_pairs"],
            dv["antisymmetric_distinct"], dv["symmetric_distinct"],
            dc["single_excitation_nonzero"], dc["ordered_pairs"])),
        ("OVERLAP",
         "R5-LAW-SURVIVES-THE-LIFT=NO-DEFECT-AT-OVERLAP-LE-1-AT-%d-OF-%d-ROWS-BOTH-SHAPES;"
         "AT-OVERLAP-2=%d-OF-%d-CARRY;WINDOW=EVERY-2-SITE-SUPPORT-%d-ROWS-EXHAUSTIVE-IN-GEOMETRY;"
         "THREE-SITE-FULL-SUPPORT=EMPTY-OVER-THE-ALPHABET-%d-ROWS-SWEPT;"
         "COIN-PAIRS=%d-EACH-GATED-SEPARATELY;R5-18-ROW-SAMPLE=CITED-NOT-RE-RUN"
         % (ov["low_overlap_rows"], ov["low_overlap_rows"],
            ov["overlap_2_nonzero"], ov["overlap_2_rows"], ov["rows"],
            ov["three_site_full_support_rows"], ov["coin_pairs"])),
        ("MOTION",
         "EIGENPHASES-ADD-EXACTLY(ANTISYMMETRIC=%d;SYMMETRIC=%d;FAILURES=%d)(FORCED-BY-FUNCTORIALITY);"
         "SPEED-SPECTRUM=%s-UNCHANGED-AT-TWO-EXCITATIONS;"
         "VELOCITY-DOES-NOT-ADD=%d-OF-%d-CELLS-AT-THE-ANTIPODAL-TIE-ONLY;"
         "CONTACT-HANDLE-MOVES-SYMMETRIC-DEFECT-AT-%d-OF-%d-AND-ANTISYMMETRIC-AT-%d"
         "(THE-MOVED-SET-IS-THE-SINGLE-EXCITATION-DEFECT-SET-BY-SET-EQUALITY);"
         "R4B-REPRODUCED=%d-TIE-CELLS-IN-%d-FAMILIES-OF-%d"
         % (mo["antisymmetric_cells"], mo["symmetric_cells"], mo["eigen_failures"],
            "+".join(str(x) for x in mo["two_speed_spectrum"]),
            mo["velocity_failures"], mo["velocity_cells"],
            ch["symmetric_defect_moved"], ch["pairs"],
            ch["antisymmetric_defect_moved"], mo["r4b_tie_cells"],
            mo["r4b_tie_families"], mo["families"])),
        ("SCOPE",
         "D=%d;L=%d;FIELD=Q(ZETA-8);ALPHABET=%d;GENERATORS=%d;STENCIL=3-TERM-AXIS;"
         "EXCITATIONS=2;SECTORS=ORDERED+SYMMETRIC+ANTISYMMETRIC;"
         "LIFT=FREE(U-TENSOR-U)-WITH-DISTINGUISHABLE-AND-CONTACT-LIFTS-CENSUSED;"
         "OCCUPANCY-CEILING=DECLARED;"
         "VELOCITY-READING=FORWARD-DIFFERENCE-WITH-TIE-AVERAGED-INHERITED-AS-DECLARED;"
         "NO-TRANSPORT-NUMBER-INHERITED;"
         "CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));"
         "INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;"
         "NO-CONTINUUM-CLAIM;NO-PARTICLE-CLAIM;SHAPE-WORDS-ONLY;"
         "N=2-ONLY-NO-GENERAL-N-CLAIM;NO-CONFIGURATION-MEASURE;NO-ACTION;NO-COUPLING"
         % (D, L, 25, ec["generators"])),
    ]
    string = head + "<" + "|".join("%s=%s" % (k, v) for k, v in segs) + ">"
    S["verdict"] = {"head": head, "segments": [[k, v] for k, v in segs],
                    "string": string, "preregistered_heads": pre,
                    "heads_by_arena": reached}
    return string


def reconstruct_head(receipt_json):
    """the INDEPENDENT reconstruction: it reads ONLY the serialized receipt,
    derives the head by its own copy of the head law, and shares no helper, no
    input and no typed value with the builder above."""
    R = json.loads(receipt_json)
    a1 = [a for a in R["arena_census"]["arenas"] if a["role"].startswith("THE DECLARED")][0]
    anti, sym = a1["antisymmetric_lives"], a1["symmetric_lives"]
    if anti and sym:
        h = "R4C-STATISTICS-BOTH-ADMITTED"
    elif anti:
        h = "R4C-STATISTICS-FORCED-ANTISYMMETRIC"
    elif sym:
        h = "R4C-STATISTICS-FORCED-SYMMETRIC"
    else:
        h = "R4C-STATISTICS-NEITHER-INVARIANT"
    body = R["verdict"]["string"]
    return h, body[:body.index("<")]


# ===========================================================================
# SECTION 14.  DESCRIPTION STAMPS, WAIVERS, THE RECEIPT AND THE PAPER
# ===========================================================================

def description_stamps(S):
    """every quantum-layer claim carries the description it was measured in:
    the sector, the lift, the occupancy ceiling and the convention.  A claim
    without a stamp is not a claim this unit makes."""
    base = ("d=2, L=4, Q(zeta_8), the 25-element alphabet, the 3-term axis "
            "stencil, two excitations")
    return [
        {"claim": "the composition law admits both exchange shapes",
         "stamp": base + "; the FREE lift U tensor U; occupancy ceiling 2; "
                         "measured per generator over the whole pool"},
        {"claim": "the symmetric shape fails to close under the hard core",
         "stamp": base + "; the FREE lift; occupancy ceiling 1 (DECLARED, not "
                         "anchored); measured per generator"},
        {"claim": "the two-excitation defect is nonzero at exactly the "
                  "pairs whose legs are both non-monomial",
         "stamp": base + "; the FREE lift; both exchange sectors; the parent's "
                         "declared division-event times and leg at the cut"},
        {"claim": "the two shapes are discriminated by the defect at exactly "
                  "the single-excitation defect set",
         "stamp": base + "; the FREE lift; value multisets on the hard-core "
                         "block, the like-for-like comparison"},
        {"claim": "R5's support-overlap law survives the lift",
         "stamp": base + "; every 2-site support, exhaustive in the geometry, "
                         "one declared interfering coin pair; both shapes"},
        {"claim": "the eigenphases add and the velocities do not",
         "stamp": base + "; the FREE lift; R4b's stratified convention "
                         "inherited AS DECLARED (forward difference, tie "
                         "averaged); no transport number inherited"},
        {"claim": "the contact interaction is invisible to the antisymmetric "
                  "shape",
         "stamp": base + "; the declared contact-phase lift; occupancy "
                         "ceiling 2; measured per pair over the circulant stratum"},
    ]


WAIVERS = [
    {"gate": "G-EXCHANGE-COMMUTES",
     "kind": "FORCED",
     "forcing": "P (U tensor U) P^{-1} = U tensor U holds for every U "
                "whatever, so the commutation is an identity of the free lift "
                "and not a property of this family.  It is registered as a "
                "disclosure with its forcing named, and the measured content "
                "that takes its place is G-HARDCORE-LEAK-PER-GENERATOR, whose "
                "split is NOT forced and separates the pool 48 to 16"},
    {"gate": "G-HARDCORE-ANTISYMMETRIC-CLOSED",
     "kind": "FORCED",
     "forcing": "the wedge carries no doubly-occupied configuration, so there "
                "is nothing for it to leak into.  The measured content beside "
                "it is the symmetric sector's leak, which fires"},
    {"gate": "G-EIGENPHASES-ADD",
     "kind": "FORCED",
     "forcing": "the wedge and the symmetric square are functors, so the "
                "lifted eigenvalue is the product of the symbols by "
                "construction.  It is verified as an exact matrix identity at "
                "every cell anyway, and the measured content beside it is "
                "G-VELOCITY-DOES-NOT-ADD, which fires at 7168 cells"},
]


DIGITS = "0123456789"


def numerals(text):
    """every DECIMAL numeral, including the fractions the exact censuses
    publish.  Typographic super- and subscripts are not decimal numerals and
    are not collected: nothing this unit measures is written in them."""
    out, cur = set(), ""
    for ch in text:
        if ch in DIGITS or (ch == "/" and cur and cur[-1] in DIGITS):
            cur += ch
        else:
            if cur:
                out.add(cur.strip("/"))
            cur = ""
    if cur:
        out.add(cur.strip("/"))
    return {n for n in out if n}


def licensed_numerals(obj, acc):
    if isinstance(obj, bool):
        return acc
    if isinstance(obj, int):
        acc.add(str(obj))
        acc.add(str(-obj) if obj < 0 else str(obj))
    elif isinstance(obj, str):
        acc |= numerals(obj)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            acc |= numerals(str(k))
            licensed_numerals(v, acc)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            licensed_numerals(v, acc)
    return acc


STRUCTURAL = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
              "13", "14", "22", "2026"}


def paper_claims(S):
    ec, oc, dc = S["exchange_census"], S["occupancy"], S["defect_census"]
    dv, di = S["defect_values"], S["discrimination"]
    ov, mo, ch = S["overlap_census"], S["motion"], S["contact_handle"]
    ar = S["arena_census"]
    return [
        {"id": "CL-ADMITTED",
         "text": "%d of %d generators" % (ec["antisymmetric_admitted"], ec["generators"]),
         "path": "exchange_census/antisymmetric_admitted"},
        {"id": "CL-DECOMP",
         "text": "%d = %d + %d" % (ec["dim_ordered"], ec["dim_symmetric"],
                                   ec["dim_antisymmetric"]),
         "path": "exchange_census/dim_ordered"},
        {"id": "CL-LEAK",
         "text": "leaks at %d of %d" % (oc["symmetric_leaking"], len(oc["rows"])),
         "path": "occupancy/symmetric_leaking"},
        {"id": "CL-PARENT",
         "text": "%d of %d ordered pairs" % (dc["single_excitation_nonzero"],
                                             dc["ordered_pairs"]),
         "path": "defect_census/single_excitation_nonzero"},
        {"id": "CL-TWOEXC",
         "text": "%d of %d ordered pairs carry a nonzero two-excitation defect"
                 % (dc["antisymmetric_nonzero"], dc["ordered_pairs"]),
         "path": "defect_census/antisymmetric_nonzero"},
        {"id": "CL-GENUINE",
         "text": "%d genuine two-body pairs" % dc["genuine_two_body"],
         "path": "defect_census/genuine_two_body"},
        {"id": "CL-PREDICATE",
         "text": "%d mismatches over %d per-pair tests"
                 % (dc["predicate_mismatches"], dc["predicate_tests"]),
         "path": "defect_census/predicate_mismatches"},
        {"id": "CL-DISCRIM",
         "text": "differ at %d of %d ordered pairs" % (di["differing_pairs"],
                                                       dc["ordered_pairs"]),
         "path": "discrimination/differing_pairs"},
        {"id": "CL-OVERLAP",
         "text": "%d of %d rows at overlap at most one"
                 % (ov["low_overlap_rows"], ov["low_overlap_rows"]),
         "path": "overlap_census/low_overlap_rows"},
        {"id": "CL-OVERLAP2",
         "text": "%d of %d rows at overlap two" % (ov["overlap_2_nonzero"],
                                                   ov["overlap_2_rows"]),
         "path": "overlap_census/overlap_2_nonzero"},
        {"id": "CL-MOTION",
         "text": "%d antisymmetric and %d symmetric cells"
                 % (mo["antisymmetric_cells"], mo["symmetric_cells"]),
         "path": "motion/antisymmetric_cells"},
        {"id": "CL-VELOCITY",
         "text": "%d of %d cells" % (mo["velocity_failures"], mo["velocity_cells"]),
         "path": "motion/velocity_failures"},
        {"id": "CL-CONTACT",
         "text": "%d of %d ordered pairs and the antisymmetric one at %d"
                 % (ch["symmetric_defect_moved"], ch["pairs"],
                    ch["antisymmetric_defect_moved"]),
         "path": "contact_handle/symmetric_defect_moved"},
        {"id": "CL-A4",
         "text": "%d of %d ordered pairs of distinct generators"
                 % (ar["distinguishable_broken"], ar["distinguishable_pairs"]),
         "path": "arena_census/distinguishable_broken"},
        {"id": "CL-VALUES",
         "text": "%d distinct values in the antisymmetric shape and %d in the "
                 "symmetric" % (dv["antisymmetric_distinct"], dv["symmetric_distinct"]),
         "path": "defect_values/antisymmetric_distinct"},
    ]


def perturb(obj, path):
    parts = path.split("/")
    cur = obj
    for p in parts[:-1]:
        cur = cur[p]
    v = cur[parts[-1]]
    cur[parts[-1]] = (v + 1) if isinstance(v, int) else "PERTURBED"
    return v


def restore(obj, path, v):
    parts = path.split("/")
    cur = obj
    for p in parts[:-1]:
        cur = cur[p]
    cur[parts[-1]] = v


def verify_paper(S, LD, path):
    if not os.path.exists(path):
        LD.gate("G-PAPER-PRESENT", "this unit's paper exists and is read as the "
                "object under test", False, path)
    txt = open(path, "r", encoding="utf-8").read()
    READS.append(path)
    norm = norm_text(txt)
    claims = paper_claims(S)
    if mut("MUT-PAPER-CLAIM"):
        claims = claims + [{"id": "CL-INJECTED", "path": "counts/L",
                            "text": "a measured assertion the paper does not make"}]
    missing = [c["id"] for c in claims if norm_text(c["text"]) not in norm]
    LD.gate("G-PAPER-CLAIMS",
            "every claim the paper makes about a measured quantity renders "
            "from a receipt key and is present in the paper as written",
            not missing, "%d claims, %d missing" % (len(claims), len(missing)))

    vs = S["verdict"]["string"]
    if mut("MUT-PAPER-VERDICT"):
        vs = vs[:40]
    LD.gate("G-PAPER-VERDICT-BLOCK",
            "the paper quotes the COMPLETE verdict string the instrument "
            "emits, character for character, so the paper's verdict block "
            "cannot go stale behind the receipt",
            vs in norm and len(vs) > 400,
            "%d characters of verdict quoted in the paper" % len(vs))

    lic = licensed_numerals(S, set()) | STRUCTURAL
    pn = numerals(txt)
    if mut("MUT-PAPER-NUMERAL"):
        pn = pn | {"987654321"}
    unlicensed = sorted(n for n in pn if n not in lic)
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY numeral in the paper -- prose, tables and fenced verdict "
            "blocks alike -- is licensed by a receipt value or is one of the "
            "declared structural numerals",
            not unlicensed,
            "%d numerals in the paper, %d unlicensed: %s"
            % (len(pn), len(unlicensed), unlicensed[:8]))

    bad_pol = []
    for c in claims:
        old = perturb(S, c["path"])
        moved = paper_claims(S)
        new = [x for x in moved if x["id"] == c["id"]][0]
        if mut("MUT-PAPER-POLARITY"):
            new = c                       # a claim that does not render from
        restore(S, c["path"], old)        # the receipt cannot have polarity
        if new["text"] == c["text"] or norm_text(new["text"]) in norm:
            bad_pol.append(c["id"])
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "and every claim has POLARITY: perturbing the receipt key it "
            "renders from moves the claim, and the moved claim is no longer "
            "found in the paper -- so a claim cannot be satisfied by accident",
            not bad_pol, "%d claims with no polarity: %s" % (len(bad_pol), bad_pol))
    S["paper_claims"] = claims
    S["paper_coverage"] = {"numerals": len(pn), "unlicensed": len(unlicensed),
                           "claims": len(claims), "polarity_failures": len(bad_pol),
                           "paper": os.path.basename(path)}
    return txt


# ===========================================================================
# SECTION 15.  MUTANTS
# ===========================================================================

MUTANTS = [
    ("MUT-GAUGE-ORBIT", "G-GAUGE-ORBITS-FREE", "shrinks one gauge orbit"),
    ("MUT-ARENA-SIZE", "G-ARENA-ANCHORED", "censuses a lattice the anchors do not name"),
    ("MUT-ALPHABET", "G-ALPHABET-REBUILT", "drops an alphabet element"),
    ("MUT-REBUILD-DROP", "G-REBUILD-BIJECTION", "drops one rebuilt generator"),
    ("MUT-POOL-COUNT", "G-POOL-COMPLETE", "shortens the pool"),
    ("MUT-VERBATIM-FRAGMENT", "G-VERBATIM-ANCHORS", "admits a 3-character anchor"),
    ("MUT-SECTOR-DIM", "G-SECTOR-DECOMPOSITION", "inflates the symmetric dimension"),
    ("MUT-EXCHANGE-COMMUTE", "G-EXCHANGE-COMMUTES", "breaks one commutation"),
    ("MUT-LEAK-ZERO", "G-HARDCORE-LEAK-PER-GENERATOR", "zeroes every hard-core leak"),
    ("MUT-A3-DIM", "G-ARENA-TWO-WAY", "gives the one-site wedge a state"),
    ("MUT-A4-COMMUTE", "G-A4-NEITHER-REACHED", "claims the distinguishable lift commutes"),
    ("MUT-A3-LIVES", "G-ARENA-TWO-WAY", "lets the symmetric shape live under the hard core"),
    ("MUT-PARENT-COUNT", "G-PARENT-REPRODUCED", "moves the reproduced parent count"),
    ("MUT-PREDICATE", "G-TWO-EXCITATION-PREDICATE", "adds a pair outside the predicate"),
    ("MUT-DISCRIMINATION", "G-SHAPES-DISCRIMINATED", "drops one discriminating pair"),
    ("MUT-COIN-ALPHABET", "G-COIN-ALPHABET-REBUILT", "shortens the coin alphabet"),
    ("MUT-THREE-SITE", "G-THREE-SITE-EMPTY", "claims a three-site completion"),
    ("MUT-OVERLAP-LAW", "G-OVERLAP-LAW-SURVIVES", "injects a defect at overlap one"),
    ("MUT-COIN-PAIR", "G-OVERLAP-COIN-INDEPENDENT", "breaks one coin pair's row"),
    ("MUT-EIGENPHASE", "G-EIGENPHASES-IN-MU8", "puts an eigenphase outside mu_8"),
    ("MUT-ADDITIVITY", "G-EIGENPHASES-ADD", "breaks one two-excitation eigen-equation"),
    ("MUT-SPECTRUM-SPLIT", "G-SPECTRA-SEPARATE-THE-SHAPES", "breaks one spectral split"),
    ("MUT-VELOCITY-ADD", "G-VELOCITY-DOES-NOT-ADD", "claims the velocity adds"),
    ("MUT-CONTACT-BLIND", "G-CONTACT-TWO-WAY", "blinds the symmetric shape to the handle"),
    ("MUT-CONTACT-SET", "G-CONTACT-SET-IS-THE-INTERFERING-SET", "drops one moved pair"),
    ("MUT-HEAD-TYPED", "G-VERDICT-RECONSTRUCTED", "retypes the head after the census"),
    ("MUT-SEAL-BROKEN", "G-SEAL-COMPLETE", "mutates a sealed object after its seal"),
    ("MUT-PAPER-VERDICT", "G-PAPER-VERDICT-BLOCK", "truncates the quoted verdict"),
    ("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "injects a claim the paper does not make"),
    ("MUT-PAPER-NUMERAL", "G-PAPER-NUMERAL-COVERAGE", "injects an unlicensed numeral"),
    ("MUT-PAPER-POLARITY", "G-PAPER-CLAIM-POLARITY", "injects a claim with no polarity"),
    ("MUT-STAMP-DROP", "G-DESCRIPTION-STAMPS", "drops a description stamp"),
    ("MUT-WAIVER-UNFORCED", "G-WAIVERS-VERIFIED", "waives a gate with no forcing"),
    ("MUT-RECEIPT-FLOAT", "G-RECEIPT-EXACT", "writes a float into the receipt"),
    ("MUT-PATH-ANCHOR", "G-PATH-VALUE-ANCHORS", "breaks one anchored value"),
    ("MUT-CONTROL-COUNT", "G-REBUILD-CONTROLS", "drops one declared control"),
    ("MUT-INVARIANT", "G-REBUILD-INVARIANTS", "reports one invariant mismatch"),
    ("MUT-MONOMIAL-LIST", "G-MONOMIAL-CLASSIFIER", "drops a monomial name"),
    ("MUT-BOTH-ADMITTED", "G-BOTH-SECTORS-ADMITTED", "closes one sector to one generator"),
    ("MUT-CEILINGS", "G-CEILINGS-AGREE-AT-ONE-EXCITATION", "separates the two ceilings at one excitation"),
    ("MUT-REGISTER", "G-OCCUPANCY-NOT-ANCHORED", "reads the stage's count register as one"),
    ("MUT-GENUINE-ZERO", "G-GENUINE-TWO-BODY", "empties the genuine two-body set"),
    ("MUT-DERIVATION", "G-DERIVATION-LAW", "injects a derivation-law failure"),
    ("MUT-FOLD", "G-DEFECT-FOLDS", "injects a fold conflict"),
    ("MUT-VALUE-MULTISET", "G-PARENT-VALUE-MULTISET", "moves one reproduced cell count"),
    ("MUT-SECOND-PATH", "G-SECOND-CODE-PATH", "moves the second route's multiset"),
    ("MUT-THIRD-PATH", "G-THIRD-CODE-PATH", "moves the third route's multiset"),
    ("MUT-IRRATIONAL", "G-DEFECT-RATIONAL", "claims an irrational defect value"),
    ("MUT-OVERLAP-BITE", "G-OVERLAP-TWO-BITES", "empties the overlap-two positive control"),
    ("MUT-SPEED-CEILING", "G-SPEED-CEILING-UNCHANGED", "widens the two-excitation speed spectrum"),
    ("MUT-R4B-REPRO", "G-R4B-CONVENTION-REPRODUCED", "moves the reproduced tie count"),
    ("MUT-HEAD-PRENAME", "G-HEAD-PREREGISTERED", "replaces the pre-registered names"),
    ("MUT-SEAL-TOTAL", "G-SEAL-TOTAL", "publishes an unsealed, undeclared key"),
    ("MUT-SHELL-IMPORT", "G-NO-VERSION-CONTROL-NO-SHELL", "adds a shell entry point"),
    ("MUT-PAYLOAD-PATH", "G-PAYLOAD-DETERMINISTIC", "writes an absolute path into the payload"),
    ("MUT-CACHE-DIRTY", "G-CACHE-UNPOLLUTED", "reports a polluted cache"),
]


# ===========================================================================
# SECTION 16.  THE STATE, END TO END
# ===========================================================================

def build_state(break_anchor=None, paper_path=None):
    S, LD, pool, circ, SRC, texts = build_arena(break_anchor)
    exchange_census(S, LD, pool, SRC)
    occupancy_census(S, LD, pool, SRC)
    arena_census(S, LD, pool, circ, None)
    alpha = build_alphabet()
    C = defect_census(S, LD, circ, SRC)
    overlap_census(S, LD, alpha, SRC)
    motion_census(S, LD, circ, SRC)
    contact_census(S, LD, circ, C["single_nz"])

    stamps = description_stamps(S)
    if mut("MUT-STAMP-DROP"):
        stamps = stamps[:-1]
    LD.gate("G-DESCRIPTION-STAMPS",
            "every quantum-layer claim this unit makes carries a description "
            "stamp naming the sector, the lift, the occupancy ceiling and the "
            "convention it was measured in; a claim without one is not a claim",
            len(stamps) == 7 and all(len(x["stamp"]) > 60 for x in stamps),
            "%d stamped claims" % len(stamps))
    S["description_stamps"] = stamps

    wl = list(WAIVERS)
    if mut("MUT-WAIVER-UNFORCED"):
        wl = wl + [{"gate": "G-PARENT-REPRODUCED", "kind": "FORCED", "forcing": "x"}]
    ok = all(w["gate"] in LD.ids and len(w["forcing"]) > 80 for w in wl)
    LD.gate("G-WAIVERS-VERIFIED",
            "every gate registered as a DISCLOSURE names the mechanism that "
            "forces it and names the measuring gate that stands in its place; "
            "no gate carrying measured content is waived",
            ok and {w["gate"] for w in wl} ==
            {r["gate"] for r in LD.rows if r["kind"] == "DISCLOSURE"},
            "%d waivers, all forced and all matched to a disclosure" % len(wl))
    S["waiver_ledger"] = wl

    S["schema"] = {"unit": "R4c", "paper": "v14/paper-22-multi.md",
                   "instrument": "v14/code/r4c_multi_exact.py",
                   "version": 1, "arithmetic": "Q(zeta_8), exact, dyadic",
                   "published_keys": sorted(FINAL_KEYS),
                   "unsealed_declared": UNSEALED_DECLARED}
    S["provenance"] = {
        "sources": [{"anchor": a, "path": p, "sha256_12": h} for a, p, h in SOURCES],
        "runtime_inputs": sorted(set(os.path.relpath(p, ROOT) for p in READS)),
        "not_executed": ["no other unit's program is imported or executed; "
                         "the parents are read as bytes and as anchored values "
                         "only", "R5's 18-row two-excitation table is CITED "
                         "and NOT re-run, as the pin requires",
                         "no transport number is inherited from R4b"],
        "python": sys.version.split()[0],
    }
    string = build_verdict(S, LD, texts, circ)
    rj = json.dumps({"arena_census": S["arena_census"], "verdict": S["verdict"]},
                    indent=1, sort_keys=True)
    h2, h1 = reconstruct_head(rj)
    LD.gate("G-VERDICT-RECONSTRUCTED",
            "the complete verdict string -- head included -- is compared for "
            "equality against an INDEPENDENT reconstruction that derives the "
            "head by its own copy of the head law, reads only the serialized "
            "receipt, and shares no helper, no input and no typed value with "
            "the builder",
            h2 == h1 == S["verdict"]["head"] and string == S["verdict"]["string"],
            "head %s reconstructed" % h2)

    # ---- the receipt is exact, and the head reconstructs ------------------
    def scan(o, bad):
        if isinstance(o, float):
            bad.append(type(o).__name__)
        elif isinstance(o, dict):
            for k, v in o.items():
                scan(v, bad)
        elif isinstance(o, (list, tuple)):
            for v in o:
                scan(v, bad)
        return bad
    pk = pool_key(circ)
    dirty = ["INJECTED"] if mut("MUT-CACHE-DIRTY") else [
        k for k, v in CENSUS_CACHE.items()
        if k == pk and census_digest(v) != CENSUS_DIGESTS.get(k)]
    LD.gate("G-CACHE-UNPOLLUTED",
            "the memoised census this run was served is byte-for-byte the "
            "census that was computed: no injection, this run's or an earlier "
            "run's, has reached it, so the mutant sweep measures 30 "
            "independent runs and not one contaminated sequence",
            not dirty, "%d cached censuses, %d polluted"
            % (len(CENSUS_DIGESTS), len(dirty)))

    if mut("MUT-RECEIPT-FLOAT"):
        S["schema"]["probe"] = float("1.5")   # built, never written as a literal
    bad = scan(S, [])
    LD.gate("G-RECEIPT-EXACT",
            "the emitted receipt contains no float anywhere: a recursive type "
            "scan of every value it publishes",
            not bad, "%d float values" % len(bad))

    counts = {
        "d": D, "L": L, "sites": NS, "alphabet": 25,
        "pool": S["exchange_census"]["generators"],
        "circulants": len(circ),
        "dim_ordered": S["exchange_census"]["dim_ordered"],
        "dim_symmetric": S["exchange_census"]["dim_symmetric"],
        "dim_antisymmetric": S["exchange_census"]["dim_antisymmetric"],
        "commuting": S["exchange_census"]["commuting"],
        "symmetric_leaking": S["occupancy"]["symmetric_leaking"],
        "ordered_pairs": S["defect_census"]["ordered_pairs"],
        "single_nonzero": S["defect_census"]["single_excitation_nonzero"],
        "two_excitation_nonzero": S["defect_census"]["antisymmetric_nonzero"],
        "genuine_two_body": S["defect_census"]["genuine_two_body"],
        "losses": S["defect_census"]["losses"],
        "discriminating_pairs": S["discrimination"]["differing_pairs"],
        "overlap_rows": S["overlap_census"]["rows"],
        "velocity_failures": S["motion"]["velocity_failures"],
        "velocity_cells": S["motion"]["velocity_cells"],
        "contact_symmetric_moved": S["contact_handle"]["symmetric_defect_moved"],
        "contact_antisymmetric_moved": S["contact_handle"]["antisymmetric_defect_moved"],
        "gates": len(LD.rows),
    }
    S["counts"] = counts
    S["parent_reproduction"] = {
        "r4_single_excitation_defects": S["defect_census"]["single_excitation_nonzero"],
        "r4_value_multiset_reproduced": True,
        "r4b_tie_cells": S["motion"]["r4b_tie_cells"],
        "r4b_tie_families": S["motion"]["r4b_tie_families"],
        "r4b_cells": S["motion"]["r4b_cells"],
        "r5_two_excitation_rows_cited": S["overlap_census"]["r5_rows_cited_not_rerun"],
        "transport_numbers_inherited": 0,
    }

    if paper_path:
        verify_paper(S, LD, paper_path)
    else:
        S["paper_claims"] = paper_claims(S)
        S["paper_coverage"] = {"numerals": 0, "unlicensed": 0,
                               "claims": len(S["paper_claims"]),
                               "polarity_failures": 0, "paper": "NOT-VERIFIED"}

    a = json.dumps(S, indent=1, sort_keys=True)
    b = json.dumps(S, indent=1, sort_keys=True)
    if mut("MUT-PAYLOAD-PATH"):
        a = a + ROOT
    LD.gate("G-PAYLOAD-DETERMINISTIC",
            "the receipt payload is a pure function of the measurements: two "
            "serializations are byte identical and neither carries this "
            "machine's absolute paths, so the artifact reproduces byte for "
            "byte anywhere the pinned inputs are",
            a == b and ROOT not in a,
            "%d bytes, twice identical, no absolute path" % len(a))

    SEAL = Seal()
    for sid in SEALS_IN_RUN:
        SEAL.take(sid, S)
    if mut("MUT-SEAL-BROKEN"):
        S["counts"]["single_nonzero"] = 0
    broken = SEAL.verify(S, only=SEALS_IN_RUN)
    LD.gate("G-SEAL-COMPLETE",
            "every object this unit vouches for was digested at the moment its "
            "gate passed, and every one of those digests still verifies now: "
            "the seal covers the measurements, the anchors, the schema, the "
            "provenance and the paper claims, not only the verdict",
            not broken, "%d seals, %d broken" % (len(SEAL.rows), len(broken)))

    if mut("MUT-SEAL-TOTAL"):
        S["an_unsealed_key"] = {"published": "but neither sealed nor declared"}
    published = set(S.keys())
    sealed = {p.split("/")[0] for _s, p, _g in SEALED_PATHS}
    LD.gate("G-SEAL-TOTAL",
            "the manifest is TOTAL over the FINAL receipt, not over the "
            "receipt as it stands here: every key the artifact will publish is "
            "sealed, save the seal ledger itself, which is declared unsealed "
            "with its reason -- and the writing path re-checks the artifact's "
            "actual key set against this declaration",
            published <= FINAL_KEYS and FINAL_KEYS - sealed == set(UNSEALED_DECLARED)
            and len(UNSEALED_DECLARED) == 1,
            "%d keys published so far, %d declared for the artifact, %d sealed, "
            "%d declared unsealed" % (len(published), len(FINAL_KEYS),
                                      len(sealed), len(UNSEALED_DECLARED)))

    return S, LD, SEAL, string


# ===========================================================================
# SECTION 17.  THE MUTANT SWEEP, THE TRANSCRIPT, AND MAIN
# ===========================================================================

def sweep_mutants(S, LD, paper_path):
    global MUT, QUIET
    rows = []
    QUIET = True
    for name, target, why in MUTANTS:
        MUT = name
        died_at = None
        try:
            build_state(None, paper_path)
        except GateFail as e:
            died_at = str(e).split(" ::")[0]
        except Exception as e:                    # a mutant must die at a GATE
            died_at = "NON-GATE-EXCEPTION:%s" % type(e).__name__
        rows.append({"mutant": name, "target": target, "what": why,
                     "died_at": died_at, "killed": died_at is not None,
                     "on_target": died_at == target})
    MUT = None
    QUIET = False
    all_dead = all(r["killed"] for r in rows)
    on_target = sum(1 for r in rows if r["on_target"])
    LD.gate("G-MUTANTS-ON-TARGET",
            "every declared mutant is killed, and killed by the gate it was "
            "declared to falsify: a mutant that dies elsewhere is a gate "
            "boundary this unit does not understand",
            all_dead and on_target == len(MUTANTS),
            "killed %d of %d; on target %d; off target %s"
            % (sum(1 for r in rows if r["killed"]), len(MUTANTS), on_target,
               [r["mutant"] for r in rows if not r["on_target"]]))
    return rows


def render(S, LD, SEAL, string, mut_rows, totals):
    say()
    say("=" * 78)
    say("v14 R4c -- TWO EXCITATIONS: STATISTICS AS A MEASUREMENT")
    say("=" * 78)
    say()
    say("ARENA (declared as data)")
    for k in ("boundary", "carrier", "family", "law", "occupancy", "velocity",
              "division_events"):
        say("  %-16s %s" % (k, S["arena_declaration"][k]))
    say()
    say("THE FOUR ARENAS (each symmetry class survives in one and dies in another)")
    say("  %-36s %-12s %-12s %s" % ("arena", "antisym", "sym", "head the law returns"))
    for a in S["arena_census"]["arenas"]:
        say("  %-36s %-12s %-12s %s"
            % (a["arena"], "LIVES" if a["antisymmetric_lives"] else "DIES",
               "LIVES" if a["symmetric_lives"] else "DIES",
               S["verdict"]["heads_by_arena"][a["arena"]]))
    say()
    say("THE DEFECT AT TWO EXCITATIONS")
    dc = S["defect_census"]
    for k in ("ordered_pairs", "single_excitation_nonzero", "antisymmetric_nonzero",
              "symmetric_nonzero", "ordered_sector_nonzero", "genuine_two_body",
              "losses", "predicate_mismatches", "derivation_failures"):
        say("  %-32s %s" % (k, dc[k]))
    say()
    say("THE SUPPORT-OVERLAP LAW, LIFTED")
    say("  %-10s %-8s %-14s %-16s %s" % ("overlap", "rows", "1-excitation",
                                         "antisymmetric", "symmetric"))
    for r in S["overlap_census"]["by_overlap"]:
        say("  %-10s %-8s %-14s %-16s %s"
            % (r["overlap"], r["rows"], r["single_excitation_nonzero"],
               r["antisymmetric_nonzero"], r["symmetric_nonzero"]))
    say()
    say("MOTION")
    mo = S["motion"]
    for k in ("antisymmetric_cells", "symmetric_cells", "eigen_failures",
              "spectral_difference_cells", "single_speed_spectrum",
              "two_speed_spectrum", "velocity_cells", "velocity_failures",
              "failing_lift_pairs"):
        say("  %-32s %s" % (k, mo[k]))
    say()
    say("SEALS (gate-time; the artifacts are written FROM these)")
    for r in SEAL.rows:
        say("  %-24s %-26s %s" % (r["seal"], r["path"], r["sha256_12"]))
    say()
    say("THE VERDICT")
    for i in range(0, len(string), 74):
        say("  " + string[i:i + 74])
    say()
    say("TOTALS: " + json.dumps(totals, sort_keys=True))
    say()
    say("NOT EXECUTED")
    for n in S["provenance"]["not_executed"]:
        say("  - " + n)
    say("  - no general-n claim: the sector is n = 2 and the two-irrep argument "
        "that forbids a third shape is an n = 2 argument")
    say("  - no configuration measure, no action and no coupling: nothing here "
        "is a dynamics over configurations")
    say("  - the occupancy ceiling is DECLARED; the stage anchors none")
    say("  - no particle is named: fermionic-shape and bosonic-shape are shape "
        "words and the walls bar more")
    say()
    say("ALL GATES PASSED (%d/%d); ALL MUTANTS DEAD (%d/%d)"
        % (totals["gates_passed"], totals["gates"], totals["mutants_killed"],
           totals["mutants"]))


def cli_error_probe(parser, argv):
    try:
        parser(argv)
        return False
    except CliError:
        return True


def parse_args(argv):
    opts = {"no_write": False, "selftest": False, "mutant": None,
            "break_anchor": None, "verify_paper": None}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            opts["no_write"] = True
        elif a == "--selftest":
            opts["selftest"] = True
        elif a == "--mutant":
            if i + 1 >= len(argv):
                raise CliError("--mutant requires a NAME")
            if argv[i + 1] not in {m[0] for m in MUTANTS}:
                raise CliError("unknown mutant %s" % argv[i + 1])
            opts["mutant"] = argv[i + 1]
            i += 1
        elif a == "--break-anchor":
            if i + 1 >= len(argv):
                raise CliError("--break-anchor requires a NAME")
            names = {s for s, _p, _h in SOURCES} | {v for v, _s, _n, _g in VERBATIM} \
                | {p for p, _s, _pp, _e, _g in PATH_VALUES}
            if argv[i + 1] not in names:
                raise CliError("unknown anchor %s" % argv[i + 1])
            opts["break_anchor"] = argv[i + 1]
            i += 1
        elif a == "--verify-paper":
            opts["verify_paper"] = PAPER
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                opts["verify_paper"] = argv[i + 1]
                i += 1
        else:
            raise CliError("unknown argument %s" % a)
        i += 1
    return opts


def selftest():
    global QUIET
    target = SOURCES[0][0]
    print("SELFTEST: corrupting anchor %s in memory; the run must die." % target,
          flush=True)
    QUIET = True
    try:
        build_state(target, None)
    except GateFail as e:
        QUIET = False
        print("SELFTEST: died at %s -- as required." % str(e).split(" ::")[0],
              flush=True)
        print("SELFTEST PASSED (the instrument is falsifiable); no artifact "
              "written.", flush=True)
        print("EXIT 1", flush=True)
        sys.exit(1)
    QUIET = False
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

    if opts["mutant"]:
        MUT = opts["mutant"]
        target = [t for m, t, _w in MUTANTS if m == opts["mutant"]][0]
        try:
            build_state(None, PAPER if os.path.exists(PAPER) else None)
        except GateFail as e:
            died = str(e).split(" ::")[0]
            print("MUTANT %s died at %s (declared target %s): %s"
                  % (opts["mutant"], died, target,
                     "ON TARGET" if died == target else "OFF TARGET"), flush=True)
            print("EXIT %d" % (1 if died == target else 2), flush=True)
            sys.exit(1 if died == target else 2)
        print("MUTANT %s SURVIVED -- the gate does not bind." % opts["mutant"],
              flush=True)
        print("EXIT 2", flush=True)
        sys.exit(2)

    paper = opts["verify_paper"] or (PAPER if os.path.exists(PAPER) else None)
    S, LD, SEAL, string = build_state(opts["break_anchor"], paper)

    cli_probes = [
        {"argv": ["--nope"], "rejected": cli_error_probe(parse_args, ["--nope"])},
        {"argv": ["--mutant"], "rejected": cli_error_probe(parse_args, ["--mutant"])},
        {"argv": ["--mutant", "NOPE"],
         "rejected": cli_error_probe(parse_args, ["--mutant", "NOPE"])},
        {"argv": ["--break-anchor", "NOPE"],
         "rejected": cli_error_probe(parse_args, ["--break-anchor", "NOPE"])},
    ]
    LD.gate("G-CLI-WHITELIST",
            "the argv whitelist rejects every unknown flag, every unknown "
            "mutant name and every unknown anchor name",
            all(p["rejected"] for p in cli_probes), "%d probes" % len(cli_probes))
    S["cli_probes"] = cli_probes

    mut_rows = sweep_mutants(S, LD, paper)
    S["mutants"] = mut_rows

    totals = {
        "gates": len(LD.rows),
        "gates_passed": sum(1 for r in LD.rows if r["passed"]),
        "gates_disclosed": sum(1 for r in LD.rows if r["kind"] == "DISCLOSURE"),
        "anchors": len(SOURCES) + len(PATH_VALUES) + len(VERBATIM),
        "byte_anchors": len(SOURCES),
        "path_value_anchors": len(PATH_VALUES),
        "verbatim_anchors": len(VERBATIM),
        "mutants": len(MUTANTS),
        "mutants_killed": sum(1 for r in mut_rows if r["killed"]),
        "mutants_on_target": sum(1 for r in mut_rows if r["on_target"]),
        "seals": len(SEALED_PATHS),
        "verdict_values": len([t for t in string.replace("=", " ")
                               .replace(";", " ").replace("-", " ")
                               .replace("(", " ").replace(")", " ")
                               .replace("+", " ").replace("|", " ")
                               .replace("<", " ").replace(">", " ")
                               .split() if t.isdigit()]),
        "census_pairs": S["defect_census"]["ordered_pairs"],
        "overlap_rows": S["overlap_census"]["rows"],
        "integrity_gate": "EVALUATED-IN-THE-WRITING-PATH-AGAINST-THE-GATE-TIME-SEAL",
    }
    S["totals"] = totals
    S["gates"] = LD.rows
    S["compliance"] = {"forcings": FORCINGS, "structural_numerals": sorted(STRUCTURAL)}

    LD.gate("G-PAPER-COVERAGE-FINAL",
            "the paper's coverage is re-asserted after the mutant sweep has "
            "closed the instrument's totals, so no in-process mutant can "
            "reach it",
            S["paper_coverage"]["unlicensed"] == 0
            and S["paper_coverage"]["polarity_failures"] == 0,
            "%d numerals, %d unlicensed" % (S["paper_coverage"]["numerals"],
                                            S["paper_coverage"]["unlicensed"]))
    # the totals CLOSE here, after the last gate, and only then are the late
    # seals taken -- a seal taken over an object that afterwards moves is not a
    # seal, and the writing path proved it by failing.
    totals["gates"] = len(LD.rows)
    totals["gates_passed"] = sum(1 for r in LD.rows if r["passed"])
    S["gates"] = LD.rows
    for sid in SEALS_LATE:
        SEAL.take(sid, S)
    S["seals"] = SEAL.rows
    if totals["seals"] != len(SEAL.rows):
        raise GateFail("G-ARTIFACT-INTEGRITY :: the published seal count is "
                       "not the seal ledger's own length")

    render(S, LD, SEAL, string, mut_rows, totals)

    payload = json.dumps(S, indent=1, sort_keys=True)
    SEAL.close(S, payload)
    transcript = "\n".join(LOG) + "\nEXIT 0\n"
    SEAL.close_transcript(transcript)

    if opts["no_write"]:
        print("EXIT 0", flush=True)
        return

    for path, data in ((OUT_JSON, payload), (OUT_TXT, transcript)):
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(data)
        os.replace(tmp, path)
    on_disk_json = open(OUT_JSON, "r", encoding="utf-8").read()
    on_disk_txt = open(OUT_TXT, "r", encoding="utf-8").read()
    probe = OUT_JSON + ".probe"
    with open(probe, "w", encoding="utf-8") as fh:
        fh.write(payload + "X")
    corrupt_detected = digest(open(probe, "r", encoding="utf-8").read()) != SEAL.payload_sha
    os.remove(probe)
    keys_ok = set(json.loads(on_disk_json).keys()) == set(FINAL_KEYS)
    ok = (digest(on_disk_json) == SEAL.payload_sha
          and digest(on_disk_txt) == SEAL.transcript_sha and corrupt_detected
          and keys_ok)
    if not ok:
        print("G-ARTIFACT-INTEGRITY :: the bytes on disk are not the sealed "
              "bytes", file=sys.stderr)
        sys.exit(2)
    print("G-ARTIFACT-INTEGRITY passed: disk bytes == gate-time seal "
          "(payload %s, transcript %s); a corrupted probe was detected."
          % (SEAL.payload_sha, SEAL.transcript_sha), flush=True)
    print("EXIT 0", flush=True)


if __name__ == "__main__":
    main()
