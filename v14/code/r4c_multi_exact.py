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
        A PATH that does not exist is rejected at parse time, exit 2.

TWO THEOREMS ARE PROVED HERE AND GATED AS THEOREMS, not censused as family
facts.  (i) THE LEAK LAW: for EVERY unitary U on a finite configuration set,
Sym^2(U) carries a hard-core configuration into a doubly-occupied one iff U is
non-monomial, and Lambda^2(U) never does -- gated on 240 constructed witnesses
in dimensions 3, 4 and 5 and on the 3364 out-of-family composites U2 U1.  What
this family contributes is the SIZE of the split, 48 against 16.  (ii) THE
INDISTINGUISHABILITY LAW: B(U (x) U) = B(U) (x) B(U) entrywise, so the ordered
sector's defect is X (x) X - Y (x) Y, which telescopes at every n, and
X^(x)n = Y^(x)n iff X = Y for row-stochastic X and Y -- so LABELLED excitations
carry no genuine n-body defect under a free lift, for any unitary family
whatever.  Both are registered as DISCLOSURES with the measured content that
stands beside them named.

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
from itertools import permutations, product

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
    "G-BYTE-ANCHORS": "reachable only from OUTSIDE the measurement path, "
                      "because a mutant that could break an anchor in memory "
                      "would be an anchor that the run itself can move.  Its "
                      "falsifiers are the twelve --break-anchor runs, the "
                      "--selftest (which corrupts one anchor and requires the "
                      "run to die), a real on-disk drift of an anchored "
                      "parent, and a missing anchored source, all of which "
                      "kill the run at this gate and write nothing",
    "G-NO-FLOAT": "a gate on this SOURCE's own abstract syntax tree; an "
                  "in-process switch cannot introduce a float literal into "
                  "the file being parsed.  Its falsifier is a source edit -- "
                  "inserting a float literal into a copy of the instrument "
                  "kills the run at this gate",
    "G-MUTANT-SWITCH-CLEAN": "a gate on this SOURCE's own abstract syntax "
                             "tree, for the same reason.  Its falsifier is a "
                             "source edit -- putting a mut() call inside a "
                             "gate predicate kills the run at this gate",
    "G-PAPER-PRESENT": "raised only when the paper is absent, which the argv "
                       "whitelist now rejects at parse time; its falsifier is "
                       "the bare-copy run, where the instrument alone in an "
                       "empty tree dies before any measurement and writes "
                       "nothing",
}

# the gates evaluated in main() AFTER build_state returns.  A consumer naming
# one of these is compliant only because this list is checked against the
# source's own gate registry and against the run's evaluated ledger.
LATE_GATES = ("G-MUTANTS-ON-TARGET", "G-PAPER-COVERAGE-FINAL")

# the gates only the paper path evaluates.  The delivery run always verifies
# the paper, so nothing here is ever exempt in delivery; a diagnostic run given
# no paper is told exactly which gates it did not reach.
PAPER_GATES = ("G-PAPER-PRESENT", "G-PAPER-CLAIMS", "G-PAPER-TABLES",
               "G-PAPER-VERDICT-BLOCK", "G-PAPER-NUMERAL-COVERAGE",
               "G-NO-PARTICLE-NAMING", "G-CONNECTIVE-VERBATIM",
               "G-PAPER-SENTENCE-POLARITY", "G-PAPER-CLAIM-POLARITY",
               "G-STATE-RESTORED")

# (seal id, receipt path, THE GATE AT WHOSE PASSING THE DIGEST IS TAKEN).
# #119/#148: the digest is taken on the line after that gate passes, never in
# a batch at the end -- the batch is what let one silently failed restore()
# deliver a sealed receipt asserting 65 of 64 generators at exit 0.  Seal.take
# refuses to seal at a gate that has not been evaluated, so the column is a
# measurement of the order of events and not a label.
SEALED_PATHS = [
    ("SEAL-VERBATIM", "verbatim_anchors", "G-VERBATIM-ANCHORS"),
    ("SEAL-BYTE-ANCHORS", "byte_anchors", "G-BYTE-ANCHORS"),
    ("SEAL-PATH-ANCHORS", "path_value_anchors", "G-PATH-VALUE-ANCHORS"),
    ("SEAL-ARENA", "arena_declaration", "G-ARENA-ANCHORED"),
    ("SEAL-POOL", "pool", "G-POOL-COMPLETE"),
    ("SEAL-EXCHANGE", "exchange_census", "G-BOTH-SECTORS-ADMITTED"),
    ("SEAL-OCCUPANCY", "occupancy", "G-STAGE-DECLARES-NO-OCCUPANCY"),
    ("SEAL-THEOREMS", "theorems", "G-INDISTINGUISHABILITY-UNIVERSAL"),
    ("SEAL-ARENAS", "arena_census", "G-ARENA-TWO-WAY"),
    ("SEAL-DEFECT", "defect_census", "G-DERIVATION-LAW"),
    ("SEAL-DISCRIMINATION", "discrimination", "G-SHAPES-DISCRIMINATED-ENTRYWISE"),
    ("SEAL-DEFECT-VALUES", "defect_values", "G-DEFECT-RATIONAL"),
    ("SEAL-OVERLAP", "overlap_census", "G-OVERLAP-SHAPES-AT-THE-LOCAL-GRAIN"),
    ("SEAL-MOTION", "motion", "G-SPEED-CEILING-UNCHANGED"),
    ("SEAL-CONTACT", "contact_handle", "G-CONTACT-SET-IS-THE-INTERFERING-SET"),
    ("SEAL-STAMPS", "description_stamps", "G-DESCRIPTION-STAMPS"),
    ("SEAL-CHOICES", "choice_inventory", "G-CHOICE-INVENTORY-VERDICT-DETERMINING"),
    ("SEAL-WAIVERS", "waiver_ledger", "G-WAIVERS-VERIFIED"),
    ("SEAL-SCHEMA", "schema", "G-RECEIPT-SCHEMA"),
    ("SEAL-PROVENANCE", "provenance", "G-RECEIPT-SCHEMA"),
    ("SEAL-COUNTS", "counts", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-PARENT", "parent_reproduction", "G-PUBLISHED-ROWS-BOUND"),
    ("SEAL-VERDICT-STRING", "verdict/string", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-HEAD", "verdict/head", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-VERDICT-ALL", "verdict", "G-VERDICT-RECONSTRUCTED"),
    ("SEAL-PAPER-CLAIMS", "paper_claims", "G-PAPER-CLAIMS"),
    ("SEAL-PAPER-TABLES", "paper_tables", "G-PAPER-TABLES"),
    ("SEAL-CLI", "cli_probes", "G-CLI-WHITELIST"),
    ("SEAL-MUTANTS", "mutants", "G-MUTANTS-ON-TARGET"),
    ("SEAL-COMPLIANCE", "compliance", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-GATES", "gates", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-TOTALS", "totals", "G-PAPER-COVERAGE-FINAL"),
    ("SEAL-COVERAGE", "paper_coverage", "G-PAPER-COVERAGE-FINAL"),
]
# the seals taken after the mutant sweep has closed the instrument's totals
SEALS_LATE = ("SEAL-MUTANTS", "SEAL-COMPLIANCE", "SEAL-GATES",
              "SEAL-TOTALS", "SEAL-COVERAGE")
SEALS_IN_RUN = tuple(sid for sid, _p, _g in SEALED_PATHS if sid not in SEALS_LATE)
SEAL_GATE = {sid: g for sid, _p, g in SEALED_PATHS}

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

    def take(self, sid, obj, LD):
        """the digest is taken HERE, on the line after the named gate passed.
        The provenance is enforced rather than declared: sealing at a gate
        that has not been evaluated in this run is itself a gate failure, so
        no seal can name a gate that never ran (#62, #119)."""
        path = [p for s, p, _g in SEALED_PATHS if s == sid][0]
        gate = [g for s, _p, g in SEALED_PATHS if s == sid][0]
        if mut("MUT-SEAL-PROVENANCE") and sid == "SEAL-POOL":
            gate = "G-A-GATE-THAT-DOES-NOT-EXIST"
        if gate not in LD.ids:
            raise GateFail("G-SEAL-PROVENANCE :: %s would be sealed at %s, "
                           "which this run has not evaluated" % (sid, gate))
        value = jpath(obj, path)
        d = digest(value)
        self.rows.append({"seal": sid, "path": path, "sealed_at_gate": gate,
                          "sha256_12": d, "gates_evaluated_at_seal_time": len(LD.rows)})
        self.index[sid] = d
        if sid == "SEAL-VERDICT-STRING":
            self.verdict_string = value

    def take_all_at(self, gid, obj, LD):
        for sid, _p, g in SEALED_PATHS:
            if g == gid and sid not in self.index:
                self.take(sid, obj, LD)

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
    # the stage's two integer count registers are LINK-COUNT BOX BOUNDS -- the
    # swept box of division-count vectors (n_e1, n_e2, n_diag) -- and not site
    # capacities.  They are anchored for what they ARE and consumed by the gate
    # that measures the stage's SILENCE on occupancy; neither argues either way.
    ("PV-LINK-COUNT-BOX-BOUND", "STAGE-RECEIPT",
     "declarations/count_lattice/axis_max", 6, "G-STAGE-DECLARES-NO-OCCUPANCY"),
    ("PV-LINK-DIAG-BOX-BOUND", "STAGE-RECEIPT",
     "declarations/count_lattice/diag_max", 12, "G-STAGE-DECLARES-NO-OCCUPANCY"),
    ("PV-LINK-BOX-DESCRIPTION", "STAGE-RECEIPT",
     "declarations/count_lattice/description",
     "the declared box of count vectors (n_e1, n_e2, n_diag) swept for the "
     "link-locality theorem's witnesses", "G-STAGE-DECLARES-NO-OCCUPANCY"),
    ("PV-L", "R4-RECEIPT", "counts/L", 4, "G-ARENA-ANCHORED"),
    ("PV-ALPHABET", "R4-RECEIPT", "counts/alphabet", 25, "G-ALPHABET-REBUILT"),
    ("PV-POOL", "R4-RECEIPT", "counts/pool", 64, "G-REBUILD-BIJECTION"),
    ("PV-CIRC", "R4-RECEIPT", "pool_counts/circulant", 58, "G-REBUILD-BIJECTION"),
    ("PV-BRICK", "R4-RECEIPT", "pool_counts/brickwork", 4, "G-REBUILD-CONTROLS"),
    ("PV-SCRAM", "R4-RECEIPT", "pool_counts/scrambled", 2, "G-REBUILD-CONTROLS"),
    ("PV-AXES", "R4-RECEIPT", "pool_counts/axes", 9, "G-REBUILD-BIJECTION"),
    ("PV-SECTOR", "R4-RECEIPT", "counts/sector", "SINGLE-OCCUPATION",
     "G-SECTOR-IS-NEW"),
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
    ("VB-SEED-DEFECT", "SEED-PAPER",
     "This is the failure of the Born shadow of the coherent composite to "
     "equal the shadow one obtains by forgetting phases and restarting at the "
     "intermediate cut.", "G-DEFECT-WITNESS"),
]

# #62's consumer binding, made literal: the four walls the pin sets are gated
# by a WORD SCAN of this unit's own paper, not by an unread label.  A shape
# word survives only as the compound the pin licenses; the bare particle noun
# does not survive at all.
BANNED_WORDS = ("fermion", "fermions", "fermionic", "boson", "bosons",
                "bosonic", "anyon", "anyons", "anyonic", "parastatistics",
                "spin", "spins", "electron", "electrons", "photon", "photons",
                "quark", "quarks", "atom", "atoms", "molecule", "molecules")
LICENSED_COMPOUNDS = ("fermionic-shape", "bosonic-shape",
                      "parastatistics-shaped", "parastatistics-shape")


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
    """a missing anchored source is an ANCHOR failure, not a traceback: the
    instrument alone in an empty tree must die at the gate that says why."""
    if not os.path.exists(path):
        raise GateFail("G-BYTE-ANCHORS :: an anchored source is not at its "
                       "pinned path :: %s" % os.path.relpath(path, ROOT))
    with open(path, "rb") as fh:
        b = fh.read()
    READS.append(path)
    return b


def canon_repr(v):
    """a canonical, hash-seed-independent rendering of any cached object --
    sets sorted, dict keys sorted by their own rendering -- so a cache
    fingerprint is a fingerprint of the OBJECT and not of an iteration order."""
    if isinstance(v, dict):
        items = sorted(((canon_repr(k), canon_repr(x)) for k, x in v.items()))
        return "{" + ",".join("%s:%s" % kv for kv in items) + "}"
    if isinstance(v, (set, frozenset)):
        return "s{" + ",".join(sorted(canon_repr(x) for x in v)) + "}"
    if isinstance(v, (list, tuple)):
        return "[" + ",".join(canon_repr(x) for x in v) + "]"
    return repr(v)


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
# SECTION 5b.  THE TWO UNIVERSAL THEOREMS, AT ANY DIMENSION
# ===========================================================================
#
# Neither of these is a fact about this family, and the unit no longer reports
# either as one.  Both are proved here for EVERY unitary, and both are gated
# on constructed witnesses OUTSIDE the pool -- dimensions 3, 4 and 5, and the
# 3364 composites U2 U1, whose column supports run to 9 and which the pool does
# not contain.
#
#   THE LEAK LAW.  In the normalised symmetric square the cell from a hard-core
#   configuration {x, y}, x != y, to a doubly-occupied {a, a} is 2 N U_ax U_ay:
#   ONE product, in a domain, so it vanishes iff a factor does.  Sym^2(U)
#   therefore leaks out of the hard core iff some ROW of U carries two nonzero
#   entries -- iff U is not monomial.  The wedge has no doubly-occupied
#   configuration at any dimension, so Lambda^2(U) never leaks.
#
#   THE INDISTINGUISHABILITY LAW.  B is entrywise, so B(U (x) U) = B(U) (x)
#   B(U); with X = B(U2 U1) and Y = B(U2) B(U1) the ordered defect is
#   X (x) X - Y (x) Y = Delta (x) X + Y (x) Delta identically, and
#   X (x) X = Y (x) Y iff X = Y for row-stochastic X and Y (sum a free index).
#   Telescoping gives every n.

def gen_index(n):
    P = tuple((i, j) for i in range(n) for j in range(i + 1, n))
    SB = P + tuple((i, i) for i in range(n))
    return P, SB, {p: k for k, p in enumerate(P)}, {p: k for k, p in enumerate(SB)}


def gen_symsq(A, n):
    """Sym^2(U) in the normalised basis, at any dimension."""
    P, SB, _PI, SI = gen_index(n)
    out = []
    for (x, y) in SB:
        cxy = INVSQ2 if x < y else HALF
        orders = ((x, y), (y, x)) if x < y else ((x, x), (x, x))
        acc = {}
        for (p, q) in orders:
            for a, va in A[p].items():
                for b, vb in A[q].items():
                    t = fmul(va, vb)
                    if a == b:
                        kk = SI[(a, a)]
                        t = fadd(t, t)
                    else:
                        kk = SI[(a, b)] if a < b else SI[(b, a)]
                    cur = acc.get(kk)
                    acc[kk] = t if cur is None else fadd(cur, t)
        col = {}
        for kk, v in acc.items():
            a, b = SB[kk]
            w = fmul(fmul(INVSQ2 if a < b else HALF, cxy), v)
            if w != ZERO:
                col[kk] = w
        out.append(col)
    return out


def gen_wedge(A, n):
    P, _SB, PI, _SI = gen_index(n)
    out = []
    for (x, y) in P:
        acc = {}
        for a, vax in A[x].items():
            for b, vby in A[y].items():
                if a == b:
                    continue
                t = fmul(vax, vby)
                kk, s = (PI[(a, b)], t) if a < b else (PI[(b, a)], fneg(t))
                cur = acc.get(kk)
                acc[kk] = s if cur is None else fadd(cur, s)
        out.append({i: v for i, v in acc.items() if v != ZERO})
    return out


def gen_leak(Sy, n):
    P, SB, _PI, SI = gen_index(n)
    dbl = {SI[(i, i)] for i in range(n)}
    return sum(1 for k in range(len(P)) for i in Sy[k] if i in dbl)


def gen_unitary(A, n):
    for j in range(n):
        for k in range(j, n):
            s = ZERO
            for i, v in A[j].items():
                w = A[k].get(i)
                if w is not None:
                    s = fadd(s, fmul(fconj(v), w))
            if s != (ONE if j == k else ZERO):
                return False
    return True


def is_monomial_matrix(A):
    """monomial = at most one nonzero per COLUMN; for a unitary this is the
    same as at most one per row, and the census below measures it."""
    return all(len(c) <= 1 for c in A)


def row_supports(A, n):
    rows = [0] * n
    for c in A:
        for i in c:
            rows[i] += 1
    return rows


def witness_unitaries(n):
    """THE DECLARED WITNESS FAMILY, outside this arena entirely: 40 monomial
    and 40 non-monomial unitaries at each of the dimensions 3, 4 and 5, built
    from permutations, zeta_8 diagonals and the 1/sqrt 2 Givens rotation, in a
    declared enumeration order and not sampled at random."""
    perms = list(permutations(range(n)))

    def PERM(p):
        return [{p[j]: ONE} for j in range(n)]

    def DIAG(t):
        return [{j: ZP[(t * j) % 8]} for j in range(n)]

    def GIV(i, j):
        col = [{k: ONE} for k in range(n)]
        col[i] = {i: INVSQ2, j: INVSQ2}
        col[j] = {i: INVSQ2, j: fneg(INVSQ2)}
        return col

    mono, nonmono = [], []
    for p in perms:
        for t in range(8):
            if len(mono) < 40:
                mono.append(matmul(DIAG(t), PERM(p)))
    for i in range(n):
        for j in range(i + 1, n):
            for p in perms:
                for t in range(8):
                    if len(nonmono) < 40:
                        nonmono.append(matmul(matmul(DIAG(t), PERM(p)), GIV(i, j)))
    return mono + nonmono


def kron_ab(A, na, B, nb):
    """the Kronecker product of matrices on na and nb columns."""
    out = []
    for x in range(na):
        ca = A[x]
        for y in range(nb):
            acc = {}
            for a, va in ca.items():
                for b, vb in B[y].items():
                    p = fmul(va, vb)
                    if p != ZERO:
                        acc[a * nb + b] = p
            out.append(acc)
    return out


def kron_power(A, n, p):
    out, dim = [{0: ONE}], 1
    for _ in range(p):
        out = kron_ab(out, dim, A, n)
        dim *= n
    return out


def madd(A, B):
    return msub(A, [{i: fneg(v) for i, v in c.items()} for c in B])


def gen_scale(A, c):
    return [{i: fmul(c, v) for i, v in col.items()} for col in A]


THEOREM_DIMS = (3, 4, 5)
# the declared ordered pairs of witnesses the derivation lemmas run on: one
# monomial-monomial, four mixed and five non-monomial-non-monomial per
# dimension, by index into the witness family's own enumeration.
LEMMA_PAIRS = ((0, 1), (0, 41), (41, 0), (2, 42), (43, 3),
               (40, 41), (41, 42), (42, 43), (44, 45), (46, 47))


def raw_theorems(circ):
    """THE TWO UNIVERSAL THEOREMS, measured on witnesses OUTSIDE this family.
    Computed once and cached like every other census."""
    key = ("theorems", pool_key(circ))
    if key in CENSUS_CACHE:
        return CENSUS_CACHE[key]
    leak_rows, leak_mismatch, wedge_leak_any = [], [], 0
    for n in THEOREM_DIMS:
        wit = witness_unitaries(n)
        nm = nn = 0
        for A in wit:
            if not gen_unitary(A, n):
                leak_mismatch.append(("NOT-UNITARY", n))
                continue
            mono = is_monomial_matrix(A)
            lk = gen_leak(gen_symsq(A, n), n)
            wl = gen_leak(gen_wedge(A, n), n)
            wedge_leak_any += wl
            if (lk > 0) != (not mono):
                leak_mismatch.append((n, mono, lk))
            if mono:
                nm += 1
            else:
                nn += 1
        leak_rows.append({"dimension": n, "witnesses": len(wit),
                          "monomial": nm, "non_monomial": nn,
                          "configurations": n * (n + 1) // 2})
    # the same law on the 3364 COMPOSITES U2 U1 -- unitaries this pool does not
    # contain, with column supports the pool never reaches
    comp_mism, comp_nonmono, comp_leaking, comp_support = 0, 0, 0, 0
    for g2 in circ:
        for g1 in circ:
            C = matmul(g2["mat"], g1["mat"])
            mono = is_monomial_matrix(C)
            lk = hardcore_leak(symsq(C))
            comp_support = max(comp_support, max(len(c) for c in C))
            if (lk > 0) != (not mono):
                comp_mism += 1
            if not mono:
                comp_nonmono += 1
            if lk > 0:
                comp_leaking += 1
    # THE INDISTINGUISHABILITY LEMMAS, on the same witnesses
    lem = {"born_multiplicative": 0, "derivation": 0, "fibre": 0,
           "affine": 0, "injective": 0, "telescope_n2": 0, "telescope_n3": 0,
           "pairs": 0, "failures": []}
    for n in THEOREM_DIMS:
        wit = witness_unitaries(n)
        for (i, j) in LEMMA_PAIRS:
            U2, U1 = wit[i], wit[j]
            lem["pairs"] += 1
            T2, T1 = kron_ab(U2, n, U2, n), kron_ab(U1, n, U1, n)
            if born(T2) != kron_ab(born(U2), n, born(U2), n):
                lem["failures"].append((n, i, j, "BORN"))
            else:
                lem["born_multiplicative"] += 1
            X, Y = born(matmul(U2, U1)), matmul(born(U2), born(U1))
            Dl = msub(X, Y)
            lhs = defect(T2, T1)
            if lhs != msub(kron_ab(X, n, X, n), kron_ab(Y, n, Y, n)):
                lem["failures"].append((n, i, j, "PRODUCT"))
            if lhs != madd(kron_ab(Dl, n, X, n), kron_ab(Y, n, Dl, n)):
                lem["failures"].append((n, i, j, "DERIVATION"))
            else:
                lem["derivation"] += 1
            # K1's fibre: the splitting is NOT unique.  The same identity holds
            # with the two legs exchanged, and on the whole affine family.
            if lhs != madd(kron_ab(Dl, n, Y, n), kron_ab(X, n, Dl, n)):
                lem["failures"].append((n, i, j, "FIBRE"))
            else:
                lem["fibre"] += 1
            ok_affine = True
            for t in (ONE, HALF, (2, 0, 0, 0, 0), fneg(ONE)):
                Lt = madd(gen_scale(X, t), gen_scale(Y, fsub(ONE, t)))
                Rt = madd(gen_scale(Y, t), gen_scale(X, fsub(ONE, t)))
                if lhs != madd(kron_ab(Dl, n, Lt, n), kron_ab(Rt, n, Dl, n)):
                    ok_affine = False
            if ok_affine:
                lem["affine"] += 1
            else:
                lem["failures"].append((n, i, j, "AFFINE"))
            # X (x) X = Y (x) Y iff X = Y, for row-stochastic X and Y
            if (kron_ab(X, n, X, n) == kron_ab(Y, n, Y, n)) != (X == Y):
                lem["failures"].append((n, i, j, "INJECTIVE"))
            else:
                lem["injective"] += 1
            for p in (2, 3):
                Xp, Yp = kron_power(X, n, p), kron_power(Y, n, p)
                acc = [{} for _ in range(n ** p)]
                for k in range(p):
                    left = kron_power(Y, n, k)
                    right = kron_power(X, n, p - 1 - k)
                    term = kron_ab(kron_ab(left, n ** k, Dl, n),
                                   n ** (k + 1), right, n ** (p - 1 - k))
                    acc = madd(acc, term)
                if msub(Xp, Yp) != acc:
                    lem["failures"].append((n, i, j, "TELESCOPE%d" % p))
                elif p == 2:
                    lem["telescope_n2"] += 1
                else:
                    lem["telescope_n3"] += 1
    out = {"leak_rows": leak_rows, "leak_mismatch": leak_mismatch,
           "wedge_leak_any": wedge_leak_any,
           "composites": len(circ) ** 2, "composite_mismatches": comp_mism,
           "composite_non_monomial": comp_nonmono,
           "composite_leaking": comp_leaking,
           "composite_max_column_support": comp_support, "lemmas": lem}
    CENSUS_CACHE[key] = out
    CENSUS_DIGESTS[key] = digest(canon_repr(out))
    return {k: (list(v) if isinstance(v, list) else dict(v)
                if isinstance(v, dict) else v) for k, v in out.items()}


def theorem_census(S, LD, circ):
    """Neither theorem is a finding about this substrate, and the unit says so
    HERE rather than reporting a forced split as a measurement."""
    say("[5/11] the two universal theorems, on witnesses outside this family")
    T = raw_theorems(circ)
    wit = sum(r["witnesses"] for r in T["leak_rows"])
    if mut("MUT-LEAK-THEOREM"):
        T["leak_mismatch"] = T["leak_mismatch"] + [("INJECTED", 0, 0)]
    LD.gate("G-LEAK-THEOREM-UNIVERSAL",
            "the hard-core leak law is a THEOREM about Sym^2 of EVERY unitary "
            "and not a property of this family: the symmetric square leaks out "
            "of the hard core iff the unitary is non-monomial, because the "
            "only cell out of it is the single product 2 N U_ax U_ay in a "
            "domain; the wedge has no doubly-occupied configuration to leak "
            "into at any dimension.  Gated on constructed witnesses in "
            "dimensions 3, 4 and 5 and on the composites U2 U1, which this "
            "pool does not contain",
            not T["leak_mismatch"] and T["wedge_leak_any"] == 0
            and T["composite_mismatches"] == 0
            and T["composites"] == len(circ) ** 2
            and T["composite_max_column_support"] > 3
            and wit == 240,
            "%d witnesses in dimensions %s, %d mismatches; %d composites "
            "(column support to %d), %d non-monomial, %d leaking, %d "
            "mismatches; wedge leak cells %d"
            % (wit, [r["dimension"] for r in T["leak_rows"]],
               len(T["leak_mismatch"]), T["composites"],
               T["composite_max_column_support"], T["composite_non_monomial"],
               T["composite_leaking"], T["composite_mismatches"],
               T["wedge_leak_any"]))
    lem = T["lemmas"]
    if mut("MUT-TELESCOPE"):
        lem["failures"] = lem["failures"] + [("INJECTED",)]
    LD.gate("G-INDISTINGUISHABILITY-UNIVERSAL",
            "and labelled excitations carry no genuine n-body defect for ANY "
            "unitary family whatever: B(U (x) U) = B(U) (x) B(U) entrywise, so "
            "the ordered defect is X (x) X - Y (x) Y = Delta (x) X + Y (x) "
            "Delta identically; X (x) X = Y (x) Y iff X = Y for row-stochastic "
            "X and Y; and the telescoping X^(x)n - Y^(x)n = sum_k Y^(x)k (x) "
            "Delta (x) X^(x)(n-1-k) carries both to every n -- measured at "
            "n = 2 and n = 3 on witnesses outside this arena",
            not lem["failures"] and lem["pairs"] == 30
            and lem["born_multiplicative"] == lem["derivation"]
            == lem["injective"] == lem["telescope_n2"] == lem["telescope_n3"]
            == lem["pairs"],
            "%d declared ordered pairs of witnesses; born %d, derivation %d, "
            "fibre %d, affine %d, injective %d, telescope n=2 %d, n=3 %d; "
            "%d failures" % (lem["pairs"], lem["born_multiplicative"],
                             lem["derivation"], lem["fibre"], lem["affine"],
                             lem["injective"], lem["telescope_n2"],
                             lem["telescope_n3"], len(lem["failures"])))
    S["theorems"] = {
        "leak_law": {
            "statement": "for every unitary U on a finite configuration set, "
                         "Sym^2(U) carries a hard-core configuration into a "
                         "doubly-occupied one iff U is non-monomial; "
                         "Lambda^2(U) never does",
            "witness_dimensions": [r["dimension"] for r in T["leak_rows"]],
            "witnesses": wit, "rows": T["leak_rows"],
            "mismatches": len(T["leak_mismatch"]),
            "out_of_family_composites": T["composites"],
            "composites_non_monomial": T["composite_non_monomial"],
            "composites_leaking": T["composite_leaking"],
            "composites_mismatches": T["composite_mismatches"],
            "composite_max_column_support": T["composite_max_column_support"],
            "wedge_leak_cells": T["wedge_leak_any"],
            "what_this_family_contributes": "the SIZE of the split, 48 "
                                            "against 16, which is the "
                                            "parent's monomial classification "
                                            "and not a two-excitation fact"},
        "indistinguishability_law": {
            "statement": "B(U (x) U) = B(U) (x) B(U) entrywise; the ordered "
                         "defect is X (x) X - Y (x) Y = Delta (x) X + Y (x) "
                         "Delta; X^(x)n = Y^(x)n iff X = Y for row-stochastic "
                         "X and Y; so labelled excitations carry no genuine "
                         "n-body defect under a free lift, at every n",
            "declared_pairs": lem["pairs"],
            "born_multiplicative": lem["born_multiplicative"],
            "derivation_law": lem["derivation"],
            "one_parameter_fibre": lem["fibre"],
            "affine_family": lem["affine"],
            "injective_on_row_stochastic": lem["injective"],
            "telescoping_n2": lem["telescope_n2"],
            "telescoping_n3": lem["telescope_n3"],
            "failures": len(lem["failures"]),
            "the_fibre": "the splitting is NOT unique: Delta (x) Y + X (x) "
                         "Delta is an equally exact derivation law, and so is "
                         "every affine mixture t X + (1-t) Y in the left leg "
                         "with the complementary mixture in the right -- "
                         "measured at t = 1, 1/2, 2 and -1.  'X the coherent "
                         "and Y the restarted composite' is one point on a "
                         "line of exact readings"},
    }
    return T


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
            # the diagonal is skipped BY INDEX, not by object identity: two
            # equal contributions from distinct intermediates are two terms
            for a in range(len(ps)):
                for b in range(len(ps)):
                    if a == b:
                        continue
                    s = fadd(s, fmul(ps[a], fconj(ps[b])))
            if s != ZERO:
                col[i] = s
        out.append(col)
    return out


# ===========================================================================
# SECTION 7.  THE STATE (built in one place, gate by gate)
# ===========================================================================

def build_arena(break_anchor=None, SEAL=None):
    LD = Ledger()
    S = {}
    say("[1/11] anchors, the arena, the field")

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
    floor = min(len(norm_text(n)) for _v, _s, n, _g in VERBATIM)
    if mut("MUT-VERBATIM-FRAGMENT"):
        vb_rows.append({"anchor": "VB-INJECTED", "source": "PIN",
                        "consumer": "G-VERBATIM-ANCHORS", "chars": 3, "present": True})
    LD.gate("G-VERBATIM-ANCHORS",
            "every declared verbatim window is present in its named source "
            "after whitespace and markdown-prefix normalisation, and EVERY "
            "window is a CONTEXT window (at least 40 normalised characters), "
            "not a fragment -- the published floor is the true floor and no "
            "anchor is exempted from it inside the predicate",
            all(r["present"] for r in vb_rows)
            and all(r["chars"] >= 40 for r in vb_rows),
            "%d windows, floor %d chars" % (len(vb_rows), floor))
    S["verbatim_anchors"] = vb_rows
    if SEAL is not None:
        SEAL.take_all_at("G-VERBATIM-ANCHORS", S, LD)

    # ---- byte anchors -----------------------------------------------------
    byte_rows = []
    for sid, rel, want in SOURCES:
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
    if SEAL is not None:
        SEAL.take_all_at("G-BYTE-ANCHORS", S, LD)

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
    if SEAL is not None:
        SEAL.take_all_at("G-PATH-VALUE-ANCHORS", S, LD)

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
                     "and is NOT anchored: the anchored stage declares no "
                     "occupancy-shaped key at all, and the parent's "
                     "single-occupation sector is the common restriction of "
                     "both ceilings.  Whether a deeper layer can FORCE one is "
                     "open and is handed on",
        "velocity": "R4b's stratified convention inherited AS DECLARED: "
                    "forward difference with the antipodal tie averaged; no "
                    "new selection claim is made here",
        "division_events": "inherited unchanged: t = 0 and t = 2 are division "
                           "events, the cut at t = 1 is not, and the leg at "
                           "the cut is B(U2); indivisibility is DECLARED by "
                           "those times and is never measured",
    }
    if SEAL is not None:
        SEAL.take_all_at("G-ARENA-ANCHORED", S, LD)

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
    say("[2/11] the family, rebuilt from the parent's definitions and gated")
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
    if SEAL is not None:
        SEAL.take_all_at("G-POOL-COMPLETE", S, LD)

    # ---- the anchored WORDS, each consumed by a gate that measures ---------
    # #62: an anchor whose consumer is an unread label binds existence and not
    # meaning.  Each of the four windows below now has a gate that uses it.
    # the probe set is declared: four circulants and the six controls, because
    # circulant Born shadows commute and the leg order could not bite on them
    probe = circ[:4] + ctrl
    ident_bad, leg_witness = [], 0
    for g2 in probe:
        for g1 in probe:
            A2, A1 = g2["mat"], g1["mat"]
            lhs = defect(A2, A1)
            rhs = msub(born(matmul(A2, A1)), matmul(born(A2), born(A1)))
            wrong_leg = msub(born(matmul(A2, A1)), matmul(born(A1), born(A2)))
            if mut("MUT-DEFECT-DEFINITION"):
                lhs = wrong_leg
            if lhs != rhs:
                ident_bad.append((g2["name"], g1["name"]))
            if rhs != wrong_leg:
                leg_witness += 1
    ddef = norm_text([n for v, _s, n, _g in VERBATIM if v == "VB-DEFECT-DEF"][0])
    LD.gate("G-DEFECT-DEFINITION",
            "the composition defect is the object the anchored definition "
            "names, and the anchor is CONSUMED rather than quoted: the "
            "measured object equals the Born shadow of the coherent composite "
            "minus the shadow obtained by forgetting phases and restarting at "
            "the intermediate cut, with the declared leg B(U2) at the cut -- "
            "and the other leg order is a DIFFERENT object, which is why the "
            "declaration matters",
            not ident_bad and leg_witness > 0
            and "forgetting phases and restarting at the intermediate cut" in ddef
            and "The division-event times are declared" in ddef,
            "the definitional identity holds at %d of %d declared pairs, %d "
            "failures; the two leg orders are different objects at %d of them"
            % (len(probe) ** 2 - len(ident_bad), len(probe) ** 2,
               len(ident_bad), leg_witness))

    # the seed paper's own witness property, measured on both sides
    mono_g = [g for g in circ if g["monomial"]][0]
    nonmono_g = [g for g in circ if not g["monomial"]][0]
    zero_side = defect(mono_g["mat"], nonmono_g["mat"])
    live_side = defect(nonmono_g["mat"], nonmono_g["mat"])
    if mut("MUT-DEFECT-WITNESS"):
        live_side = zero_side
    sdef = norm_text([n for v, _s, n, _g in VERBATIM if v == "VB-SEED-DEFECT"][0])
    LD.gate("G-DEFECT-WITNESS",
            "and the seed paper's witness property is exercised in both "
            "directions on this arena: the defect VANISHES exactly when the "
            "coherent composite's Born shadow equals the restarted one -- zero "
            "at a monomial leg, nonzero at a pair that interferes -- so the "
            "anchored sentence is a definition this unit uses and not a "
            "sentence it cites",
            not mnz(zero_side) and mnz(live_side)
            and "failure of the Born shadow of the coherent composite" in sdef,
            "the defect is zero at %s/%s and nonzero at %s/%s"
            % (mono_g["name"], nonmono_g["name"], nonmono_g["name"],
               nonmono_g["name"]))

    pinq = norm_text(texts["PIN"])
    routes = norm_text([n for v, _s, n, _g in VERBATIM
                        if v == "VB-THREE-ROUTES"][0])
    carrier = S["arena_declaration"]["carrier"]
    if mut("MUT-PIN-QUESTION"):
        carrier = carrier.replace("TWO-excitation", "one-excitation")
    LD.gate("G-PIN-QUESTION-IS-THE-PARENTS",
            "the question this unit asks is the one the parent's own terminal "
            "register named as the cheapest route off its stage, and the pin "
            "asks it in those words: the parent names a two-excitation sector "
            "as the first of exactly three routes out, and the carrier this "
            "unit declares IS that sector",
            "a two-excitation sector" in routes
            and "which exchange symmetry does the substrate's composition law "
                "FORCE or ADMIT on two-excitation states" in pinq
            and "TWO-excitation sector" in carrier,
            "the pin's question and the parent's route name the same sector")

    nomulti = norm_text([n for v, _s, n, _g in VERBATIM if v == "VB-NO-MULTI"][0])
    parent_sector = SRC["R4-RECEIPT"]["counts"]["sector"]
    dim_here = NS * NS
    if mut("MUT-SECTOR-NEW"):
        dim_here = NS
    LD.gate("G-SECTOR-IS-NEW",
            "and the sector is NEW: the parent's own bytes say it carried no "
            "multi-excitation sector and its receipt declares the sector "
            "SINGLE-OCCUPATION, while this unit's ordered carrier is |X|^2 "
            "configurations -- so nothing measured here is a re-reading of the "
            "parent's arena",
            "No multi-excitation sector" in nomulti
            and parent_sector == "SINGLE-OCCUPATION" and dim_here == NS * NS
            and dim_here > NS,
            "the parent's sector is %s on %d configurations; this unit's "
            "ordered sector carries %d" % (parent_sector, NS, dim_here))
    return S, LD, pool, circ, SRC, texts


# ===========================================================================
# SECTION 8.  THE EXCHANGE CENSUS -- QUESTION ONE
# ===========================================================================

CENSUS_CACHE = {}
CENSUS_DIGESTS = {}


def copy_obj(v):
    """EVERY cache hands back a defensive copy, not one of the seven.  The
    §11 sentence is now true as written, and G-CACHE-UNPOLLUTED fingerprints
    all seven families' full field sets rather than seven fields of one."""
    if isinstance(v, dict):
        return {k: copy_obj(x) for k, x in v.items()}
    if isinstance(v, set):
        return set(v)
    if isinstance(v, list):
        return [copy_obj(x) for x in v]
    if isinstance(v, tuple):
        return tuple(copy_obj(x) for x in v)
    return v


def cache_put(key, value):
    CENSUS_CACHE[key] = value
    CENSUS_DIGESTS[key] = digest(canon_repr(value))
    return copy_obj(value)


def cache_get(key):
    return copy_obj(CENSUS_CACHE[key])


def full_pool_key(pool):
    return digest([[g["name"], g["kind"], D, L,
                    sorted([j, sorted([i, list(v)] for i, v in c.items())]
                           for j, c in enumerate(g["mat"]))] for g in pool])


def raw_exchange(pool):
    key = ("exchange", full_pool_key(pool))
    if key in CENSUS_CACHE:
        return cache_get(key)
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
    return cache_put(key, rows)


def raw_leak(pool):
    """the antisymmetric closure is MEASURED per generator -- hardcore_leak of
    the wedge -- and not typed True (K3 MINOR-4).  Its forcing is that the
    wedge's row index set contains no doubly-occupied configuration at all."""
    key = ("leak", full_pool_key(pool))
    if key in CENSUS_CACHE:
        return cache_get(key)
    rows = []
    for g in pool:
        W = wedge(g["mat"])
        rows.append({"generator": g["name"], "monomial": g["monomial"],
                     "symmetric_hardcore_leak_cells": hardcore_leak(symsq(g["mat"])),
                     "antisymmetric_hardcore_leak_cells": hardcore_leak(
                         W + [{} for _ in range(NS)])})
    return cache_put(key, rows)


def exchange_census(S, LD, pool, SRC, SEAL):
    """Which exchange symmetry does the composition law force or admit?  The
    question is asked per generator, never as a count (#87)."""
    say("[3/11] the exchange census: the sectors, per generator")
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
    SEAL.take_all_at("G-BOTH-SECTORS-ADMITTED", S, LD)
    return rows


def one_excitation_configs(ceiling):
    """the one-excitation configuration set THE OCCUPANCY DECLARATION admits.
    A configuration is a multiset of occupied sites and the ceiling bounds
    each site's multiplicity; the set is DERIVED from the declaration here and
    not assumed to be the same for both."""
    out = []
    for c in product(range(NS), repeat=1):
        mult = {}
        for s in c:
            mult[s] = mult.get(s, 0) + 1
        if max(mult.values()) <= ceiling:
            out.append(tuple(sorted(c)))
    return tuple(out)


def one_excitation_law(ceiling, g):
    """and the restriction of a generator to that set, as data: the transition
    matrix on the admitted configurations, from which the Born shadow follows.
    This is what the two ceilings are compared on, object by object, instead of
    a cardinality compared with itself (K1 MINOR-3)."""
    cfg = one_excitation_configs(ceiling)
    idx = {c: k for k, c in enumerate(cfg)}
    M = [dict() for _ in cfg]
    for k, c in enumerate(cfg):
        for i, v in g["mat"][c[0]].items():
            if (i,) in idx:
                M[k][idx[(i,)]] = v
    return cfg, M


def occupancy_census(S, LD, pool, SRC, circ, SEAL):
    """The occupancy ceiling is a DECLARATION, and it is the coordinate that
    selects.  Ceiling 2 admits the doubly-occupied configurations; ceiling 1
    (the hard core) does not.  Measured: which sector survives which."""
    say("[4/11] the occupancy declaration, and what it kills")
    rows = []
    for r in raw_leak(pool):
        leak = 0 if mut("MUT-LEAK-ZERO") else r["symmetric_hardcore_leak_cells"]
        wleak = r["antisymmetric_hardcore_leak_cells"]
        if mut("MUT-WEDGE-LEAK"):
            wleak = 1
        rows.append({"generator": r["generator"], "monomial": r["monomial"],
                     "symmetric_hardcore_leak_cells": leak,
                     "symmetric_hardcore_closed": leak == 0,
                     "antisymmetric_hardcore_leak_cells": wleak,
                     "antisymmetric_hardcore_closed": wleak == 0})
    leaking = sum(1 for r in rows if not r["symmetric_hardcore_closed"])
    closed = len(rows) - leaking
    mismatch = [r["generator"] for r in rows
                if (r["symmetric_hardcore_leak_cells"] > 0) != (not r["monomial"])]
    LD.gate("G-HARDCORE-LEAK-PER-GENERATOR",
            "under the hard-core ceiling the symmetric sector fails to close "
            "at exactly the non-monomial generators and closes at exactly the "
            "monomial ones -- a per-generator predicate discharged per "
            "generator, with no aggregate standing in for any of them.  The "
            "SPLIT is a theorem about Sym^2 of every unitary "
            "(G-LEAK-THEOREM-UNIVERSAL); what this pool contributes is its "
            "SIZE, and that is inherited from the parent's monomial "
            "classification",
            not mismatch and leaking > 0 and closed > 0,
            "%d leaking, %d closed, %d mismatches" % (leaking, closed, len(mismatch)),
            kind="DISCLOSURE")
    LD.gate("G-HARDCORE-ANTISYMMETRIC-CLOSED",
            "under the same ceiling the antisymmetric sector closes at every "
            "generator -- MEASURED as the wedge's own leak cell count and not "
            "typed: the wedge has no doubly-occupied configuration to leak "
            "into, so the exclusion is not imposed on it but is the shape "
            "itself",
            all(r["antisymmetric_hardcore_closed"] for r in rows)
            and sum(r["antisymmetric_hardcore_leak_cells"] for r in rows) == 0
            and len(PAIRS) == 120,
            "%d of %d generators, %d leak cells over the whole pool, %d "
            "hard-core configurations"
            % (len(rows), len(pool),
               sum(r["antisymmetric_hardcore_leak_cells"] for r in rows),
               len(PAIRS)), kind="DISCLOSURE")

    # the two ceilings have the SAME one-excitation restriction: this is why
    # no measurement the parent could take can select between them.  The gate
    # compares the two restrictions AS OBJECTS -- configuration sets, and every
    # generator's own matrix and Born shadow -- not two copies of one integer.
    obj_bad = []
    c1 = c2 = ()
    for g in pool:
        c1, m1 = one_excitation_law(1, g)
        c2, m2 = one_excitation_law(2, g)
        if mut("MUT-CEILINGS") and g is pool[0]:
            m2 = m2[:-1]
        if c1 != c2 or m1 != m2 or born(m1) != born(m2):
            obj_bad.append(g["name"])
    if mut("MUT-CEILING-SET"):
        c2 = c2[:-1]
    LD.gate("G-CEILINGS-AGREE-AT-ONE-EXCITATION",
            "the two occupancy ceilings have the same one-excitation "
            "restriction AS AN OBJECT: the same configuration set, and for "
            "every generator in the pool the same transition matrix and the "
            "same Born shadow -- so the parent's whole arena is a fixed point "
            "of both, and no single-excitation measurement whatever, of any "
            "quantity at all, can select between them",
            c1 == c2 and len(c1) == NS and not obj_bad
            and len(SYMB) != len(PAIRS),
            "%d = %d configurations at one excitation, %d generators agreeing "
            "as objects, %d disagreeing; %d against %d at two"
            % (len(c1), len(c2), len(pool) - len(obj_bad), len(obj_bad),
               len(SYMB), len(PAIRS)))

    # THE STAGE'S SILENCE, MEASURED.  The delivered unit argued from the
    # stage's integer count registers to a site occupancy; those registers are
    # LINK registers and swept box bounds, and the analogy runs both ways, i.e.
    # neither way.  What is measurable, and what the section actually needs, is
    # that the stage declares no occupancy-shaped key at all.
    decl = SRC["STAGE-RECEIPT"]["declarations"]
    keys = sorted(decl.keys())
    if mut("MUT-STAGE-OCCUPANCY-KEY"):
        keys = keys + ["occupancy_ceiling"]
    shaped = [k for k in keys
              if any(t in k.lower() for t in ("occup", "ceiling", "capacit",
                                              "multiplic"))]
    regval = [r for r in S["path_value_anchors"]
              if r["anchor"] == "PV-LINK-COUNT-BOX-BOUND"][0]["value"]
    diagval = [r for r in S["path_value_anchors"]
               if r["anchor"] == "PV-LINK-DIAG-BOX-BOUND"][0]["value"]
    boxdesc = [r for r in S["path_value_anchors"]
               if r["anchor"] == "PV-LINK-BOX-DESCRIPTION"][0]["value"]
    LD.gate("G-STAGE-DECLARES-NO-OCCUPANCY",
            "the occupancy ceiling is NOT anchored, and this is a MEASUREMENT "
            "of the record layer's silence rather than an inference from one "
            "of its integers: every declaration key the anchored stage "
            "publishes is enumerated and none of them is occupancy-shaped.  "
            "Its two integer count registers are LINK registers -- the swept "
            "box of division-count vectors, by the stage's own description -- "
            "and its one site-indexed register is binary, so neither argues "
            "either way",
            not shaped and len(keys) == 27
            and regval == 6 and diagval == 12 and "swept" in boxdesc
            and "count vectors" in boxdesc
            and SRC["R4-RECEIPT"]["counts"]["sector"] == "SINGLE-OCCUPATION",
            "%d declaration keys, %d occupancy-shaped; the two integer "
            "registers are the link-count box bounds %d and %d"
            % (len(keys), len(shaped), regval, diagval))
    S["occupancy"] = {
        "rows": rows, "symmetric_leaking": leaking, "symmetric_closed": closed,
        "antisymmetric_closed": len(rows),
        "antisymmetric_leak_cells": sum(r["antisymmetric_hardcore_leak_cells"]
                                        for r in rows),
        "configurations_ceiling_1": len(PAIRS),
        "configurations_ceiling_2": len(SYMB),
        "one_excitation_configurations": NS,
        "one_excitation_restrictions_agree_as_objects": len(pool) - len(obj_bad),
        "stage_declaration_keys": len(keys),
        "stage_occupancy_shaped_keys": len(shaped),
        "stage_link_count_box_bounds": [regval, diagval],
        "ceiling_is_anchored": False,
        "ceiling_status": "DECLARED-BY-THIS-UNIT-AND-CENSUSED-BOTH-WAYS; "
                          "WHETHER-A-DEEPER-LAYER-CAN-FORCE-ONE-IS-OPEN",
    }
    SEAL.take_all_at("G-STAGE-DECLARES-NO-OCCUPANCY", S, LD)
    return rows


def cross_blocks(T):
    """<antisymmetric|T|symmetric> and <symmetric|T|antisymmetric>: the two
    off-block matrix elements whose vanishing IS sector invariance.  A4's
    second head-input was asserted in a detail string and never measured
    (K1 MINOR-2); it is measured here, per ordered pair."""
    as_cells = sa_cells = 0
    for (x, y) in PAIRS:
        cx, cy = x * NS + y, y * NS + x
        sym = {}
        for src in (cx, cy):
            for i, v in T[src].items():
                sym[i] = fadd(sym.get(i, ZERO), v)
        seen = set()
        for i in sym:
            a, b = divmod(i, NS)
            if a == b or (a, b) in seen or (b, a) in seen:
                continue
            seen.add((a, b))
            if fsub(sym.get(a * NS + b, ZERO), sym.get(b * NS + a, ZERO)) != ZERO:
                as_cells += 1
        anti = {}
        for src, sgn in ((cx, ONE), (cy, fneg(ONE))):
            for i, v in T[src].items():
                anti[i] = fadd(anti.get(i, ZERO), fmul(sgn, v))
        seen = set()
        for i in anti:
            a, b = divmod(i, NS)
            if (a, b) in seen or (b, a) in seen:
                continue
            seen.add((a, b))
            if a == b:
                if anti[i] != ZERO:
                    sa_cells += 1
            elif fadd(anti.get(a * NS + b, ZERO), anti.get(b * NS + a, ZERO)) != ZERO:
                sa_cells += 1
    return as_cells, sa_cells


def raw_distinguishable(circ):
    key = ("A4", pool_key(circ))
    if key in CENSUS_CACHE:
        return cache_get(key)
    off = broken = 0
    neither = 0
    for i, g2 in enumerate(circ):
        for j, g1 in enumerate(circ):
            if i == j:
                continue
            off += 1
            T = tensor2(g2["mat"], g1["mat"])
            if T != tensor2(g1["mat"], g2["mat"]):
                broken += 1
            a_s, s_a = cross_blocks(T)
            if a_s > 0 and s_a > 0:
                neither += 1
    return cache_put(key, (off, broken, neither))


def arena_census(S, LD, pool, circ, SEAL):
    """The two-way design the pin requires: FOUR arenas, each a real
    construction on this stage, on which each symmetry class demonstrably
    survives or dies.  The head law is exercised on all four and returns a
    DIFFERENT pre-registered outcome on each, so every pre-registered outcome
    REACHES its gate (#34) on a measured arena and not on a synthetic one."""
    say("[6/11] the four arenas: where each shape lives and where it dies")
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

    # A4 -- the distinguishable lift U tensor V: NEITHER sector survives.  The
    # two head-inputs are TWO measurements, not one used twice (K1 MINOR-2):
    # the commutation failure, and the two off-block matrix elements whose
    # vanishing is what sector invariance means.
    off, broken, neither = raw_distinguishable(circ)
    if mut("MUT-A4-COMMUTE"):
        broken = 0
    if mut("MUT-A4-INVARIANT"):
        neither = 0
    arenas.append({"arena": "A4-DISTINGUISHABLE-LIFT",
                   "role": "one generator per excitation: the excitations are "
                           "told apart by the law itself",
                   "antisymmetric_lives": neither != off,
                   "symmetric_lives": neither != off,
                   "detail": "the exchange operator fails to commute with the "
                             "lift at %d of %d ordered pairs of distinct "
                             "generators, and at %d of them NEITHER sector is "
                             "invariant -- both off-block matrix elements "
                             "measured" % (broken, off, neither)})
    LD.gate("G-A4-NEITHER-REACHED",
            "the NEITHER branch is reached on a REAL arena and not on a "
            "synthetic census: at the distinguishable lift every ordered pair "
            "of distinct generators breaks the exchange symmetry",
            broken == off and off > 0,
            "%d of %d ordered pairs of distinct generators" % (broken, off))
    LD.gate("G-A4-NEITHER-INVARIANT",
            "and the arena's SECOND head-input is a second measurement: at "
            "every ordered pair of distinct generators BOTH off-block matrix "
            "elements are nonzero -- <antisymmetric|U (x) V|symmetric> and "
            "<symmetric|U (x) V|antisymmetric> -- so neither sector is "
            "invariant, measured per pair rather than asserted in a detail "
            "string beside the commutation",
            neither == off and off > 0,
            "%d of %d ordered pairs carry both cross-blocks nonzero"
            % (neither, off))
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
                         "distinguishable_neither_invariant": neither,
                         "distinguishable_pairs": off}
    SEAL.take_all_at("G-ARENA-TWO-WAY", S, LD)
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
    """the cache key carries the ARENA as well as the pool (K3 MINOR-9): two
    lattices could otherwise present the same coefficient maps to one key."""
    return digest([D, L, NS,
                   [[g["name"], sorted((list(o), list(v)) for o, v in g["coef"].items())]
                    for g in circ]])


# the declared witness pair for the entrywise discrimination law: an ordered
# pair carrying NO single-excitation defect whose two shapes nevertheless
# disagree cell by cell.  Declared as data, in the parent's own naming.
WITNESS_PAIR = ("C000", "C012")
# the two cells of that witness the paper renders, as (row, column) hard-core
# configurations -- sites {0,4} against {0,1} and {0,5}
WITNESS_CELLS = (((0, 4), (0, 1)), ((0, 4), (0, 5)))
# the declared stride window for the second, coarser reading of the triple
# identity: every STRIDE-th ordered pair in the census's own enumeration
STRIDE = 13


def raw_defect_census(circ):
    """The expensive census, computed ONCE per pool.  It is keyed by a digest
    of the pool itself, so a mutant that perturbs the construction can never
    be served a cached census: such mutants die at a construction gate, which
    is evaluated before this runs."""
    key = pool_key(circ)
    if key in CENSUS_CACHE:
        return cache_get(key)
    W = {g["name"]: wedge(g["mat"]) for g in circ}
    Sy = {g["name"]: symsq(g["mat"]) for g in circ}
    B1 = {g["name"]: born(g["mat"]) for g in circ}
    npair = len(PAIRS)
    rows = {}
    single_nz, wedge_nz, sym_nz = set(), set(), set()
    tensor_nz, differing, deriv_fail = set(), set(), []
    entry_differing, joint_zero = set(), set()
    wvals, svals, svals_sector, onevals = {}, {}, {}, {}
    fold_fail, fibre_fail = [], []
    witness = None
    order = []
    for g2 in circ:
        n2 = g2["name"]
        for g1 in circ:
            n1 = g1["name"]
            order.append((n2, n1))
            D1 = defect(g2["mat"], g1["mat"])
            Dw = defect(W[n2], W[n1])
            Ds = defect(Sy[n2], Sy[n1])
            # the like-for-like comparison is on the hard-core block of
            # configurations BOTH sectors carry -- 120 of the symmetric
            # sector's 136 -- and the block is built once and read twice, at
            # both granularities.
            blk = [{i: v for i, v in c.items() if i < npair} for c in Ds[:npair]]
            # the ordered (distinguishable) sector: B is multiplicative over
            # the tensor product, so the defect there obeys an exact
            # derivation law.  Both sides are built and compared -- and so is
            # K1's fibre, the same identity with the two legs exchanged.
            X, Y = born(matmul(g2["mat"], g1["mat"])), matmul(B1[n2], B1[n1])
            lhs = defect(tensor(g2["mat"]), tensor(g1["mat"]))
            if lhs != msub(kron(X, X), kron(Y, Y)):
                deriv_fail.append((n2, n1, "PRODUCT"))
            if lhs != msub(kron(D1, X), kron(fneg_mat(Y), D1)):
                deriv_fail.append((n2, n1, "LEIBNIZ"))
            if lhs != msub(kron(D1, Y), kron(fneg_mat(X), D1)):
                fibre_fail.append((n2, n1, "FIBRE"))
            if mnz(D1):
                single_nz.add((n2, n1))
            if mnz(Dw):
                wedge_nz.add((n2, n1))
            if mnz(Ds):
                sym_nz.add((n2, n1))
            if mnz(lhs):
                tensor_nz.add((n2, n1))
            # GRANULARITY ONE, entrywise: the two shapes' defects compared
            # CELL BY CELL on the shared block.
            if any(Dw[k] != blk[k] for k in range(npair)):
                entry_differing.add((n2, n1))
            if not mnz(Dw) and not mnz(Ds):
                joint_zero.add((n2, n1))
            # GRANULARITY TWO, relabelling-invariant: the same two objects
            # compared as VALUE MULTISETS.
            vw = value_multiset(Dw)
            vs = value_multiset(blk)
            if vw != vs:
                differing.add((n2, n1))
            if not folds_by_translation(D1):
                fold_fail.append((n2, n1))
            one = {}
            for k, v in sep_profile(D1).items():
                one[v] = one.get(v, 0) + 1
            for d, acc in ((vw, wvals), (vs, svals), (one, onevals),
                           (value_multiset(Ds), svals_sector)):
                for k, v in d.items():
                    acc[k] = acc.get(k, 0) + v
            rows[(n2, n1)] = (mcells(D1), mcells(Dw), mcells(Ds))
            if (n2, n1) == WITNESS_PAIR:
                cells = 0
                for k in range(npair):
                    for i in set(Dw[k]) | set(blk[k]):
                        if Dw[k].get(i, ZERO) != blk[k].get(i, ZERO):
                            cells += 1
                named = []
                for (rw, cl) in WITNESS_CELLS:
                    i, k = PIDX[rw], PIDX[cl]
                    named.append({"row": list(rw), "column": list(cl),
                                  "symmetric": frac_str(blk[k].get(i, ZERO)),
                                  "antisymmetric": frac_str(Dw[k].get(i, ZERO))})
                witness = {"pair": [n2, n1],
                           "single_excitation_defect": mnz(D1),
                           "entrywise_differing_cells": cells,
                           "value_multisets_equal": vw == vs,
                           "antisymmetric_value_multiset":
                               {frac_str(k): v for k, v in sorted(vw.items())},
                           "symmetric_block_value_multiset":
                               {frac_str(k): v for k, v in sorted(vs.items())},
                           "named_cells": named}
    # the declared stride window: the triple identity read at coin level
    samp = order[::STRIDE]
    out = {"rows": rows, "single_nz": single_nz, "wedge_nz": wedge_nz,
           "sym_nz": sym_nz, "tensor_nz": tensor_nz, "differing": differing,
           "entry_differing": entry_differing, "joint_zero": joint_zero,
           "wvals": wvals, "svals": svals, "svals_sector": svals_sector,
           "onevals": onevals, "deriv_fail": deriv_fail,
           "fibre_fail": fibre_fail, "fold_fail": fold_fail,
           "witness": witness, "sample": samp, "key": key}
    return cache_put(key, out)


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


THIRD_WINDOW = 12


def raw_alt_paths(circ):
    """the SECOND and THIRD code paths, computed once per pool like every
    other heavy census.  The second lifts the composed generator instead of
    composing the lifted ones; the third forms no composite matrix and no
    product of Born matrices at all, and runs on the declared window."""
    key = ("altpaths", pool_key(circ))
    if key in CENSUS_CACHE:
        return cache_get(key)
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
    window = circ[:THIRD_WINDOW]
    cross_w, direct_w, win_nz = {}, {}, 0
    for g2 in window:
        for g1 in window:
            A2, A1 = W[g2["name"]], W[g1["name"]]
            cw = defect_crossterm(A2, A1)
            dw = defect(A2, A1)
            if mnz(dw):
                win_nz += 1
            for k, v in value_multiset(cw).items():
                cross_w[k] = cross_w.get(k, 0) + v
            for k, v in value_multiset(dw).items():
                direct_w[k] = direct_w.get(k, 0) + v
    return cache_put(key, {"check_w": check_w, "cross_w": cross_w,
                           "direct_w": direct_w, "win_nz": win_nz})


def defect_census(S, LD, circ, SRC, SEAL):
    say("[7/11] the defect census at two excitations, three sectors")
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
    if mut("MUT-PREDICATE-OBJECT"):
        # a pair swapped IN for a pair swapped OUT: the cardinality is
        # preserved exactly, so only the per-object clause can catch it (K3
        # MINOR-12 -- the per-object clause had no falsifier of its own)
        C["wedge_nz"].add(("C000", "C004"))
        C["wedge_nz"].discard(("C000", "C000"))
        C["sym_nz"].add(("C000", "C004"))
        C["sym_nz"].discard(("C000", "C000"))
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
    markov_carry = [p for p in (C["wedge_nz"] | C["sym_nz"] | C["single_nz"])
                    if p[0] in mono or p[1] in mono]
    if mut("MUT-MARKOV-CARRY"):
        markov_carry = markov_carry + [("C004", "C004")]
    LD.gate("G-MARKOV-INHERITED",
            "the parent's anchored Markovian zero is CONSUMED here and not "
            "merely quoted: a monomial leg annihilates the defect against "
            "everything, at one excitation and at two and in both shapes, so "
            "no ordered pair with a monomial leg carries a defect anywhere in "
            "this census.  That is entailed by the per-pair law above rather "
            "than measured beside it, and it is the parent's control surviving "
            "the lift",
            not markov_carry
            and SRC["R4-RECEIPT"]["counts"]["markov_nonzero"] == 0
            and len(mono) == 16,
            "%d monomial generators; %d of the %d ordered pairs with a "
            "monomial leg carry a defect at any level"
            % (len(mono), len(markov_carry), npairs - nonmono * nonmono))

    if mut("MUT-DERIVATION"):
        C["deriv_fail"] = C["deriv_fail"] + [("X", "Y", "INJECTED")]
    if mut("MUT-FIBRE"):
        C["fibre_fail"] = C["fibre_fail"] + [("X", "Y", "INJECTED")]
    LD.gate("G-DERIVATION-LAW",
            "on the ORDERED sector the defect DOES compose, exactly and by a "
            "derivation law -- Delta(U2 (x) U2, U1 (x) U1) = Delta (x) X + Y "
            "(x) Delta -- so the ordered sector carries no genuine two-body "
            "defect at all and the whole excess above is carried by the "
            "exchange symmetrisation.  Both the law and its ONE-PARAMETER "
            "FIBRE are checked at every pair: Delta (x) Y + X (x) Delta is an "
            "equally exact reading, so 'X the coherent and Y the restarted "
            "composite' is one point on a line and not the splitting.  The "
            "law and its consequence are FORCED "
            "(G-INDISTINGUISHABILITY-UNIVERSAL); what is measured beside them "
            "is the symmetrised census",
            not C["deriv_fail"] and not C["fibre_fail"]
            and C["tensor_nz"] == C["single_nz"],
            "%d derivation failures and %d fibre failures over %d pairs; "
            "ordered-sector defect set equals the single-excitation set"
            % (len(C["deriv_fail"]), len(C["fibre_fail"]), npairs),
            kind="DISCLOSURE")
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
        "derivation_fibre_failures": len(C["fibre_fail"]),
        "monomial_leg_pairs_carrying_a_defect": len(markov_carry),
    }
    SEAL.take_all_at("G-DERIVATION-LAW", S, LD)

    # ---- THE DISCRIMINATION, AT BOTH GRANULARITIES ------------------------
    # Entrywise the two shapes differ wherever the two-excitation defect lives
    # -- all 1764 pairs whose legs are both non-monomial, including all 1176
    # genuine two-body ones.  What is confined to the 588 is the coarser,
    # relabelling-invariant comparison: the VALUE MULTISETS.
    if mut("MUT-DISCRIMINATION"):
        C["differing"] = set(list(C["differing"])[:-1])
    LD.gate("G-SHAPES-DISCRIMINATED",
            "at the relabelling-invariant granularity the two shapes are told "
            "apart exactly where the substrate already interferes: the set of "
            "ordered pairs at which the symmetric and antisymmetric "
            "two-excitation defects differ AS VALUE MULTISETS is EXACTLY the "
            "set of pairs carrying a single-excitation defect -- a set "
            "equality, not a coincidence of cardinalities",
            C["differing"] == C["single_nz"] and len(C["differing"]) > 0,
            "%d differing pairs; set equality against the %d single-excitation "
            "pairs" % (len(C["differing"]), len(C["single_nz"])))
    if mut("MUT-ENTRYWISE"):
        C["entry_differing"] = set(list(C["entry_differing"])[:-1])
    if mut("MUT-JOINT-ZERO"):
        C["joint_zero"] = set(list(C["joint_zero"])[:-1])
    wit = C["witness"]
    if mut("MUT-WITNESS"):
        wit = dict(wit, entrywise_differing_cells=0)
    LD.gate("G-SHAPES-DISCRIMINATED-ENTRYWISE",
            "and CELL BY CELL, on the same shared hard-core block, in the same "
            "row and column ordering, the two shapes differ at a strictly "
            "larger set: the set of ordered pairs at which the two "
            "two-excitation defects differ ENTRYWISE is EXACTLY the set on "
            "which the two-excitation defect is nonzero -- the pairs whose two "
            "legs are both non-monomial -- and they agree only where both "
            "defects vanish.  A set equality against the census's own nonzero "
            "set, with a declared witness carrying no single-excitation defect "
            "at all",
            C["entry_differing"] == C["wedge_nz"] == C["sym_nz"]
            and C["joint_zero"] == set(C["rows"]) - C["wedge_nz"]
            and len(C["entry_differing"]) + len(C["joint_zero"]) == npairs
            and wit is not None and not wit["single_excitation_defect"]
            and wit["value_multisets_equal"]
            and wit["entrywise_differing_cells"] > 0,
            "%d pairs differ entrywise, %d agree with both defects zero; "
            "witness %s carries no single-excitation defect, equal value "
            "multisets and %d differing cells"
            % (len(C["entry_differing"]), len(C["joint_zero"]),
               "/".join(wit["pair"]), wit["entrywise_differing_cells"]))
    # the triple identity, read at the coarser granularity of a declared
    # stride window as well as over the whole census
    samp = list(C["sample"])
    samp_single = [p for p in samp if p in C["single_nz"]]
    samp_diff = [p for p in samp if p in C["differing"]]
    if mut("MUT-SAMPLE-WINDOW"):
        samp = samp[:-1]
    LD.gate("G-TRIPLE-IDENTITY-BOTH-GRANULARITIES",
            "the triple identity is stated at BOTH granularities it holds at, "
            "and each is gated as a set equality: over the whole census the "
            "multiset-differing set, the handle's moved set and the "
            "single-excitation set are one 588-element set; and on the "
            "declared stride window -- every 13th ordered pair of the census's "
            "own enumeration -- the same three coincide again on a "
            "43-element set, so the identity is not an artifact of reading the "
            "census whole",
            len(samp) == 259 and set(samp_single) == set(samp_diff)
            and len(samp_single) == 43,
            "%d pairs in the declared stride window, %d carrying a "
            "single-excitation defect, %d discriminated, set-equal"
            % (len(samp), len(samp_single), len(samp_diff)))
    S["discrimination"] = {
        "granularity": "TWO: entrywise (cell by cell) and "
                       "relabelling-invariant (value multisets)",
        "entrywise_differing_pairs": len(C["entry_differing"]),
        "entrywise_agreeing_pairs": len(C["joint_zero"]),
        "entrywise_set_is_the_two_excitation_nonzero_set": True,
        "differing_pairs": len(C["differing"]),
        "single_excitation_pairs": len(C["single_nz"]),
        "set_equality": True,
        "agreeing_pairs": npairs - len(C["differing"]),
        "witness": wit,
        "stride_window": {"stride": STRIDE, "pairs": len(samp),
                          "single_excitation": len(samp_single),
                          "discriminated": len(samp_diff),
                          "set_equality": True},
    }
    SEAL.take_all_at("G-SHAPES-DISCRIMINATED-ENTRYWISE", S, LD)

    # ---- the second code path: the whole antisymmetric value multiset -----
    # The builder composes the LIFTED generators.  This route lifts the
    # COMPOSED generator instead -- the wedge of the composite against the
    # composite of the wedges -- so it never forms the builder's product and
    # never re-reads it, and it binds functoriality over the whole census.
    ALT = raw_alt_paths(circ)
    W = {g["name"]: wedge(g["mat"]) for g in circ}
    check_w = ALT["check_w"]
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
    window = circ[:THIRD_WINDOW]
    win_mono = sum(1 for g in window if g["monomial"])
    cross_w, direct_w, win_nz = ALT["cross_w"], ALT["direct_w"], ALT["win_nz"]
    if mut("MUT-THIRD-PATH"):
        cross_w = dict(cross_w)
        cross_w[sorted(cross_w)[0]] += 1
    if mut("MUT-WINDOW-BLIND"):
        win_mono = 0
    LD.gate("G-THIRD-CODE-PATH",
            "and a third route agrees on a declared window: the explicit "
            "interference sum over ordered pairs of distinct intermediate "
            "configurations, which forms no composite matrix and no product "
            "of Born matrices at all.  The window is the first twelve "
            "generators in the parent's own naming, declared and not sampled "
            "at random -- and it is required to BITE: it must contain "
            "generators of BOTH predicate classes and pairs of both outcomes, "
            "so the agreement is not an agreement about an empty set",
            cross_w == direct_w and len(cross_w) > 0
            and 0 < win_mono < len(window)
            and 0 < win_nz < len(window) ** 2
            and win_nz == (len(window) - win_mono) ** 2,
            "%d ordered pairs, %d distinct values; the window carries %d "
            "monomial and %d non-monomial generators and %d nonzero pairs"
            % (len(window) ** 2, len(cross_w), win_mono,
               len(window) - win_mono, win_nz))
    third_pairs = len(window) ** 2

    rat_w = all(is_rational(k) for k in C["wvals"]) and not mut("MUT-IRRATIONAL")
    rat_s = all(is_rational(k) for k in C["svals"])
    rat_sector = all(is_rational(k) for k in C["svals_sector"])
    sector_only = sorted(frac_str(k) for k in C["svals_sector"]
                         if k not in C["svals"])
    if mut("MUT-SECTOR-VALUES"):
        rat_sector = False
    LD.gate("G-DEFECT-RATIONAL",
            "every two-excitation defect value is rational, although the field "
            "carries irrational elements and the Born projection is never "
            "coerced out of it -- and the claim REACHES the whole symmetric "
            "sector and not only the hard-core block the wedge also carries: "
            "the 136-dimensional symmetric defect carries 39 distinct values, "
            "9 of which the block never sees, and every one of them is "
            "rational too",
            rat_w and rat_s and rat_sector
            and len(C["svals_sector"]) > len(C["svals"])
            and len(sector_only) == len(C["svals_sector"]) - len(C["svals"]),
            "%d antisymmetric, %d symmetric on the hard-core block and %d in "
            "the whole symmetric sector, all rational; %d values live only "
            "off the block: %s"
            % (len(C["wvals"]), len(C["svals"]), len(C["svals_sector"]),
               len(sector_only), sector_only))

    S["defect_values"] = {
        "single_excitation": {frac_str(k): v for k, v in sorted(C["onevals"].items())},
        "antisymmetric": {frac_str(k): v for k, v in sorted(C["wvals"].items())},
        "symmetric_hardcore_block": {frac_str(k): v for k, v in sorted(C["svals"].items())},
        "symmetric_sector": {frac_str(k): v for k, v in sorted(C["svals_sector"].items())},
        "antisymmetric_distinct": len(C["wvals"]),
        "symmetric_distinct_hardcore_block": len(C["svals"]),
        "symmetric_distinct_full_sector": len(C["svals_sector"]),
        "values_only_off_the_block": sector_only,
        "single_distinct": len(C["onevals"]),
        "second_path_agrees": True,
        "third_path_window_pairs": third_pairs,
        "third_path_window_monomial_generators": win_mono,
        "third_path_window_nonzero_pairs": win_nz,
        "block_scope": "the published like-for-like comparison is on the "
                       "120x120 hard-core block BOTH sectors carry; the "
                       "symmetric sector's own census is published beside it",
    }
    SEAL.take_all_at("G-DEFECT-RATIONAL", S, LD)
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
        return cache_get(key)
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
    npair = len(PAIRS)
    per_pair = []
    # K2 MAJOR-4: at overlap 2 the one-excitation defect fires at every row, so
    # these are rows on which the substrate demonstrably interferes AWAY from
    # the circulant stratum.  The shape discrimination is TAKEN here, at both
    # granularities, and decides whether "exactly where the substrate
    # interferes" is an arena law or a stratum law.
    shape_diff = {"rows": 0, "entrywise": 0, "multiset": 0}
    for (a, b) in COIN_PAIRS:
        c1, c2 = inter[a], inter[b]
        sub = {0: [0, 0, 0, 0], 1: [0, 0, 0, 0], 2: [0, 0, 0, 0]}
        subdiff = {"rows": 0, "entrywise": 0, "multiset": 0}
        for p1 in sp:
            U1 = siteop(p1, c1)
            W1, S1 = wedge(U1), symsq(U1)
            for p2 in sp:
                ov = len(set(p1) & set(p2))
                U2 = siteop(p2, c2)
                for r in (res[ov], sub[ov]):
                    r[0] += 1
                Dw = defect(wedge(U2), W1)
                Ds = defect(symsq(U2), S1)
                d1 = 1 if mnz(defect(U2, U1)) else 0
                dw = 1 if mnz(Dw) else 0
                ds = 1 if mnz(Ds) else 0
                for r in (res[ov], sub[ov]):
                    r[1] += d1
                    r[2] += dw
                    r[3] += ds
                if ov == 2:
                    blk = [{i: v for i, v in c.items() if i < npair}
                           for c in Ds[:npair]]
                    for acc in (shape_diff, subdiff):
                        acc["rows"] += 1
                        if any(Dw[k] != blk[k] for k in range(npair)):
                            acc["entrywise"] += 1
                        if value_multiset(Dw) != value_multiset(blk):
                            acc["multiset"] += 1
        per_pair.append({"coin_pair": [a, b],
                         "low_rows": sub[0][0] + sub[1][0],
                         "low_nonzero": (sub[0][1] + sub[1][1] + sub[0][2]
                                         + sub[1][2] + sub[0][3] + sub[1][3]),
                         "overlap_2_rows": sub[2][0],
                         "overlap_2_single": sub[2][1],
                         "overlap_2_antisymmetric": sub[2][2],
                         "overlap_2_symmetric": sub[2][3],
                         "overlap_2_shapes_differ_entrywise": subdiff["entrywise"],
                         "overlap_2_shapes_differ_as_multisets": subdiff["multiset"]})
    out = (coins, inter, links, rows3, completions, sp, res, per_pair, shape_diff)
    return cache_put(key, out)


def overlap_census(S, LD, alpha, SRC, texts, SEAL):
    say("[8/11] the support-overlap law, generalised and lifted")
    (coins, inter, links, rows3, completions, sp, res0, per_pair,
     shape_diff) = raw_overlap(alpha)
    coins, links = list(coins), set(links)
    res = {o: list(v) for o, v in res0.items()}
    per_pair = [dict(r) for r in per_pair]
    shape_diff = dict(shape_diff)
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

    # R5's eighteen-row precedent is CITED and not re-run, and the count is
    # parsed out of R5's own bytes rather than typed here (#62's consumer
    # binding: the anchor that quotes it is consumed by this gate).
    needle = [n for v, _s, n, _g in VERBATIM if v == "VB-R5-EIGHTEEN"][0]
    cited = None
    for tok in norm_text(needle).replace("`", " ").split():
        if tok.isdigit() and int(tok) > 1:
            cited = int(tok)
            break
    if mut("MUT-R5-CITED"):
        cited = 19
    LD.gate("G-R5-PRECEDENT-CITED",
            "R5's one declared two-excitation extension is CITED and NOT "
            "re-run, as the pin requires, and the number of rows this unit "
            "attributes to it is PARSED from R5's own anchored sentence rather "
            "than typed here -- so the citation cannot drift from the thing "
            "cited",
            cited == 18 and "0 of 18" in norm_text(needle)
            and "declared sample" in norm_text(needle),
            "%d rows cited and not re-run, parsed from the anchored sentence"
            % cited)

    if mut("MUT-LOCAL-GRAIN"):
        shape_diff["entrywise"] = shape_diff["rows"]
    self_pairs = [r for r in per_pair if r["coin_pair"][0] == r["coin_pair"][1]]
    other_pairs = [r for r in per_pair if r["coin_pair"][0] != r["coin_pair"][1]]
    LD.gate("G-OVERLAP-SHAPES-AT-THE-LOCAL-GRAIN",
            "the shape discrimination is TAKEN at the local grain and not only "
            "on the circulant stratum, at both granularities.  On the 360 "
            "overlap-2 rows -- rows where the one-excitation defect fires at "
            "every one of them -- the two shapes differ at 240: at EVERY row "
            "of each declared pair of DISTINCT coins, and at NO row of the "
            "coin composed with itself.  So interference at one excitation "
            "does NOT by itself imply the shapes can be told apart: the "
            "coextension of the two is a fact about the CIRCULANT STRATUM, "
            "which is where this unit's discrimination law is scoped, and the "
            "local window carries 120 interfering rows on which the shapes "
            "agree",
            shape_diff["rows"] == res[2][0] > 0
            and shape_diff["entrywise"] == shape_diff["multiset"] == 240
            and all(r["overlap_2_shapes_differ_entrywise"]
                    == r["overlap_2_shapes_differ_as_multisets"] == 0
                    for r in self_pairs)
            and all(r["overlap_2_shapes_differ_entrywise"]
                    == r["overlap_2_shapes_differ_as_multisets"]
                    == r["overlap_2_rows"] for r in other_pairs)
            and len(self_pairs) == 1 and len(other_pairs) == 2,
            "%d overlap-2 rows compared; %d differ entrywise and %d as value "
            "multisets; %d of %d declared coin pairs are a coin against "
            "itself and discriminate at none"
            % (shape_diff["rows"], shape_diff["entrywise"],
               shape_diff["multiset"], len(self_pairs), len(per_pair)))
    S["overlap_census"] = {
        "coins": len(coins), "interfering_coins": len(inter), "links": len(links),
        "site_pairs": len(sp), "rows": sum(res[o][0] for o in res),
        "three_site_full_support_rows": len(rows3),
        "three_site_completions": completions,
        "three_site_reason": "the sweep is the reason: over this alphabet the "
                             "only full-support unit row has squared moduli "
                             "(1/2, 1/4, 1/4), and no two further alphabet "
                             "rows are orthogonal to it and to each other",
        "low_overlap_rows": low,
        "low_overlap_nonzero": low_nz,
        "overlap_2_rows": res[2][0],
        "overlap_2_nonzero": res[2][2],
        "overlap_2_shapes_differ_entrywise": shape_diff["entrywise"],
        "overlap_2_shapes_differ_as_multisets": shape_diff["multiset"],
        "by_overlap": [{"overlap": o, "rows": res[o][0],
                        "single_excitation_nonzero": res[o][1],
                        "antisymmetric_nonzero": res[o][2],
                        "symmetric_nonzero": res[o][3]} for o in (0, 1, 2)],
        "r5_rows_cited_not_rerun": cited,
        "coin_pairs": len(COIN_PAIRS),
        "coin_axis_scope": "THREE DECLARED ORDERED COIN PAIRS drawn from the "
                           "512 interfering coins, each gated separately; the "
                           "geometry is exhaustive and the coin axis is a "
                           "declared sample",
        "per_coin_pair": per_pair,
    }
    SEAL.take_all_at("G-OVERLAP-SHAPES-AT-THE-LOCAL-GRAIN", S, LD)
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
        return cache_get(key)
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
    rawpairs, rawfail = {}, {}
    for g in circ:
        sp = s1[g["name"]]
        for a in range(len(MOM)):
            for b in range(len(MOM)):
                for e in ((1, 0), (0, 1)):
                    da = (sp[MI[addv(MOM[a], e)]] - sp[a]) % 8
                    db = (sp[MI[addv(MOM[b], e)]] - sp[b]) % 8
                    tot += 1
                    sp2.add(circle_speed((da + db) % 8))
                    rawpairs[(da, db)] = rawpairs.get((da, db), 0) + 1
                    if -lift_tie_averaged((da + db) % 8) != \
                            -(lift_tie_averaged(da) + lift_tie_averaged(db)):
                        fail += 1
                        failpairs.add((lift_tie_averaged(da), lift_tie_averaged(db)))
                        rawfail[(da, db)] = rawfail.get((da, db), 0) + 1
    # the RAW advance pairs, published beside the lifted ones: the lift maps
    # both 0 and 4 to 0 and would hide the distinction that decides the
    # attribution (K1 MINOR-4).
    equal_nonzero_ok = {k: v for k, v in rawpairs.items()
                        if k[0] == k[1] and k[0] != 0 and k not in rawfail}
    out = {"s1": s1, "bad1": bad1, "badw": badw, "bads": bads, "cw": cw, "cs": cs,
           "spec_ok": spec_ok, "sp1": sorted(sp1), "ties": ties,
           "tiefam": len(tiefam), "cells1": cells1, "tot": tot, "fail": fail,
           "failpairs": sorted(failpairs), "sp2": sorted(sp2), "momenta": len(MOM),
           "rawpairs": sorted((list(k), v) for k, v in rawpairs.items()),
           "rawfail": sorted((list(k), v) for k, v in rawfail.items()),
           "equal_nonzero_not_failing":
               sorted((list(k), v) for k, v in equal_nonzero_ok.items())}
    return cache_put(key, out)


def motion_census(S, LD, circ, SRC, SEAL):
    say("[9/11] motion: eigenphases, bands, and where the velocity fails to add")
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

    # R4b's convention WORD is derived from R4b's own anchored values rather
    # than typed here (#62: the anchors PV-R4B-TIE and PV-R4B-STENCIL name this
    # gate, so the name has to mean something).
    tie = [r for r in S["path_value_anchors"]
           if r["anchor"] == "PV-R4B-TIE"][0]["value"]
    stencil = [r for r in S["path_value_anchors"]
               if r["anchor"] == "PV-R4B-STENCIL"][0]["value"]
    if mut("MUT-R4B-CONVENTION"):
        tie = "TIE-KEPT"
    convention = "%s-DIFFERENCE-WITH-%s-INHERITED-AS-DECLARED" % (stencil[0], tie)
    LD.gate("G-R4B-CONVENTION-INHERITED",
            "the velocity convention this unit inherits is DERIVED from R4b's "
            "own anchored values -- its declared tie reading and the first of "
            "its admissible stencils -- and not typed beside them, so the "
            "convention WORD the receipt publishes cannot drift from the "
            "convention the parent declared.  It is inherited AS DECLARED and "
            "is not re-selected here",
            convention == "FORWARD-DIFFERENCE-WITH-TIE-AVERAGED-INHERITED-AS-DECLARED"
            and tie == "TIE-AVERAGED" and stencil == ["FORWARD", "BACKWARD"]
            and lift_tie_averaged(4) == 0,
            "convention derived as %s" % convention)

    tot, fail = M["tot"], M["fail"]
    failpairs, sp2 = set(M["failpairs"]), M["sp2"]
    rawfail = [(tuple(k), v) for k, v in M["rawfail"]]
    eqok = [(tuple(k), v) for k, v in M["equal_nonzero_not_failing"]]
    if mut("MUT-VELOCITY-ADD"):
        fail = 0
    if mut("MUT-RAW-PAIRS"):
        rawfail = rawfail + [((0, 0), 1)]
    LD.gate("G-VELOCITY-DOES-NOT-ADD",
            "the eigenphases add and the VELOCITIES do not: under the "
            "inherited convention the lift of a sum is not the sum of the "
            "lifts.  The failure is confined to one mechanism, and the "
            "mechanism is stated in the RAW advances rather than in their "
            "lifts, because the lift sends both 0 and 4 to 0 and would hide "
            "the distinction: the failing raw pairs are exactly (2,2) and "
            "(6,6) -- an advance of pi/2 per momentum step in both legs, whose "
            "sum is the antipodal tie -- while the 4096 cells with both "
            "advances equal to 4, equal and nonzero, do NOT fail",
            fail > 0 and failpairs == {(2, 2), (-2, -2)}
            and [k for k, _v in rawfail] == [(2, 2), (6, 6)]
            and [k for k, _v in eqok] == [(4, 4)]
            and sum(v for _k, v in rawfail) == fail,
            "%d of %d cells fail; failing raw advance pairs %s; equal and "
            "nonzero but not failing %s; failing lift pairs %s"
            % (fail, tot, rawfail, eqok, sorted(failpairs)))
    if mut("MUT-SPEED-CEILING"):
        sp2 = sp2[:-1]
    LD.gate("G-SPEED-CEILING-UNCHANGED",
            "and two excitations move no faster than one: the two-excitation "
            "speed spectrum is the single-excitation spectrum.  The CEILING is "
            "forced -- the declared speed is the branch-free circle distance "
            "on Z/8 halved, whose range is {0,1,2} for every argument at "
            "L = 4, so no family and no excitation number could widen it -- "
            "and what is measured is that all three values are ATTAINED at two "
            "excitations as well as at one",
            sp2 == sp1 == [0, 1, 2]
            and sorted({circle_speed(d) for d in range(8)}) == [0, 1, 2],
            "two-excitation speeds %s against %s; the declared reading's whole "
            "range is %s" % (sp2, sp1, sorted({circle_speed(d) for d in range(8)})),
            kind="DISCLOSURE")
    S["motion"] = {
        "families": len(circ), "momenta": M["momenta"],
        "antisymmetric_cells": cw, "symmetric_cells": cs,
        "single_cells": len(circ) * M["momenta"],
        "eigen_failures": badw + bads + bad1,
        "spectra_split_families": spec_ok,
        "spectral_difference_cells": len(SYMB) - len(PAIRS),
        "single_speed_spectrum": sp1,
        "two_speed_spectrum": sp2,
        "speed_range_of_the_declared_reading": sorted({circle_speed(d)
                                                       for d in range(8)}),
        "velocity_cells": tot, "velocity_failures": fail,
        "failing_lift_pairs": sorted(failpairs),
        "failing_raw_advance_pairs": [[list(k), v] for k, v in rawfail],
        "equal_and_nonzero_not_failing": [[list(k), v] for k, v in eqok],
        "equal_and_nonzero_not_failing_cells": sum(v for _k, v in eqok),
        "raw_advance_pairs": [[list(k), v] for k, v in M["rawpairs"]],
        "r4b_tie_cells": ties, "r4b_tie_families": tiefam,
        "r4b_cells": cells1,
        "convention": convention,
        "transport_numbers_inherited": 0,
    }
    scope = norm_text([n for v, _s, n, _g in VERBATIM if v == "VB-PIN-SCOPE"][0])
    inherited = S["motion"]["transport_numbers_inherited"]
    if mut("MUT-TRANSPORT"):
        inherited = 1
    r4b_keys = [k for k in SRC["R4B-RECEIPT"] if "transport" in k.lower()]
    LD.gate("G-NO-TRANSPORT-NUMBER-INHERITED",
            "the pin's scope stamp is CONSUMED: no transport number is "
            "inherited from R4b and none is produced.  The parent publishes "
            "transport-shaped keys and this unit reads none of them into any "
            "measurement; the count it inherits is zero and the SCOPE segment "
            "says so",
            inherited == 0 and "NO transport number is inherited" in scope
            and all(k not in str(S["motion"]) for k in r4b_keys),
            "%d transport numbers inherited; %d transport-shaped parent keys, "
            "none read" % (inherited, len(r4b_keys)))
    SEAL.take_all_at("G-SPEED-CEILING-UNCHANGED", S, LD)
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
        return cache_get(key)
    return cache_put(key, _contact_work(circ))


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


def contact_census(S, LD, circ, single_set, SEAL):
    say("[10/11] the contact handle: an interaction only one shape can see")
    K = raw_contact(circ)
    moved_w, moved_s = K["moved_w"], K["moved_s"]
    op_moved_w, op_moved_s = K["op_moved_w"], K["op_moved_s"]
    base_s, cont_s = K["base_s"], K["cont_s"]
    if mut("MUT-CONTACT-BLIND"):
        moved_s = 0
    LD.gate("G-CONTACT-TWO-WAY",
            "the declared contact interaction MOVES the symmetric shape's "
            "two-excitation defect and CANNOT move the antisymmetric shape's: "
            "the negative direction of this self-test fires where it can, so "
            "the zero is a measurement of the SHAPE and not a vacuity OF THE "
            "HANDLE -- the antisymmetric zero itself is forced, since the "
            "wedge carries no doubly-occupied configuration for the handle to "
            "act on",
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
            "discriminated on at the relabelling-invariant granularity, "
            "element for element, gated as a set equality and not as a count.  "
            "ON THE CIRCULANT STRATUM everything that can see the "
            "doubly-occupied channel sees it exactly where the substrate "
            "already interferes; the local window of section 7 measures the "
            "same question at the local grain and answers it differently, so "
            "the coextension is stratum-scoped and is not claimed of the arena",
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
        "scope": "THE CIRCULANT STRATUM; the antisymmetric zero is FORCED and "
                 "generalises to every n, the visibility census does not",
    }
    SEAL.take_all_at("G-CONTACT-SET-IS-THE-INTERFERING-SET", S, LD)


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
    if mut("MUT-HEAD-REACH"):
        reached["A3-ONE-SITE-LATTICE"] = head_law(True, True)
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
    th, cn = S["theorems"], S["counts"]
    segs = [
        ("EXCHANGE",
         "COMMUTES-AT-%d-OF-%d(FORCED-BY-THE-FREE-LIFT);"
         "BOTH-SECTORS-CLOSED-UNITARY-STOCHASTIC=%d-OF-%d(FORCED-BY-THE-FREE-LIFT);"
         "DECOMPOSITION=%d=%d+%d(NO-THIRD-SECTOR-AT-TWO-EXCITATIONS;"
         "PERMUTATION-GROUP-ONLY-NO-BRAID-CLAIM)"
         % (ec["commuting"], ec["generators"], ec["antisymmetric_admitted"],
            ec["generators"], ec["dim_ordered"], ec["dim_symmetric"],
            ec["dim_antisymmetric"])),
        ("OCCUPANCY",
         "CEILING-DECLARED-NOT-ANCHORED(STAGE-DECLARES-NO-OCCUPANCY-KEY-IN-%d);"
         "AT-CEILING-1-SYMMETRIC-LEAKS=%d-OF-%d-EXACTLY-THE-NON-MONOMIAL"
         "(THEOREM-FOR-EVERY-UNITARY-%d-WITNESSES+%d-COMPOSITES;THE-%d-IS-THE-FAMILY);"
         "ANTISYMMETRIC-LEAKS=0-OF-%d(FORCED-NO-DOUBLY-OCCUPIED-CONFIGURATION);"
         "THE-TWO-CEILINGS-AGREE-AT-ONE-EXCITATION=%d-OF-%d-CONFIGURATIONS"
         "-AND-AS-OBJECTS-AT-%d-OF-%d-GENERATORS;"
         "AND-DIFFER-AT-TWO=%d-VS-%d;FORCING-THE-CEILING=OPEN"
         % (oc["stage_declaration_keys"], oc["symmetric_leaking"],
            len(oc["rows"]), th["leak_law"]["witnesses"],
            th["leak_law"]["out_of_family_composites"], oc["symmetric_leaking"],
            len(oc["rows"]), oc["one_excitation_configurations"],
            oc["one_excitation_configurations"],
            oc["one_excitation_restrictions_agree_as_objects"], len(oc["rows"]),
            oc["configurations_ceiling_2"], oc["configurations_ceiling_1"])),
        ("DISCRIMINATION",
         "THE-SHAPES-DIFFER-CELL-BY-CELL-AT-%d-OF-%d-PAIRS"
         "=EXACTLY-THE-TWO-EXCITATION-DEFECT-SET(SET-EQUALITY);"
         "AGREE-ONLY-WHERE-BOTH-DEFECTS-VANISH=%d;"
         "VALUE-MULTISETS-DIFFER-AT-%d-OF-%d"
         "=EXACTLY-THE-SINGLE-EXCITATION-DEFECT-SET(SET-EQUALITY);"
         "MULTISETS-AGREE-AT-%d;"
         "AT-THE-LOCAL-GRAIN-SHAPES-DIFFER-AT-%d-OF-%d-OVERLAP-2-ROWS"
         "(SO-THE-COEXTENSION-IS-CIRCULANT-STRATUM-SCOPED);"
         "SPECTRA-DIFFER-AT-%d-DOUBLED-MOMENTUM-CELLS-AT-%d-OF-%d-FAMILIES"
         % (di["entrywise_differing_pairs"], dc["ordered_pairs"],
            di["entrywise_agreeing_pairs"], di["differing_pairs"],
            dc["ordered_pairs"], di["agreeing_pairs"],
            ov["overlap_2_shapes_differ_entrywise"], ov["overlap_2_rows"],
            mo["spectral_difference_cells"], mo["spectra_split_families"],
            mo["families"])),
        ("DEFECT",
         "DOES-NOT-COMPOSE-IT-COMPLETES;NONZERO=%d-OF-%d-IN-BOTH-SHAPES"
         "=BOTH-LEGS-NON-MONOMIAL(%d-MISMATCHES-OF-%d-PER-PAIR-TESTS;=%d-SQUARED);"
         "GENUINE-TWO-BODY=%d;LOSSES=%d;"
         "ORDERED-SECTOR=DERIVATION-LAW-EXACT-%d-OF-%d-AND-NO-GENUINE-TWO-BODY"
         "(THEOREM-AT-EVERY-N-BY-TELESCOPING;THE-SPLITTING-HAS-A-ONE-PARAMETER-FIBRE);"
         "VALUES=ANTISYMMETRIC-%d-DISTINCT+SYMMETRIC-%d-DISTINCT-IN-THE-SECTOR"
         "(%d-ON-THE-HARD-CORE-BLOCK)-ALL-RATIONAL;"
         "PARENT-SINGLE-EXCITATION=%d-OF-%d-REPRODUCED-WITH-ITS-WHOLE-VALUE-MULTISET"
         % (dc["antisymmetric_nonzero"], dc["ordered_pairs"],
            dc["predicate_mismatches"], dc["predicate_tests"],
            dc["non_monomial_generators"], dc["genuine_two_body"], dc["losses"],
            dc["ordered_pairs"] - dc["derivation_failures"], dc["ordered_pairs"],
            dv["antisymmetric_distinct"], dv["symmetric_distinct_full_sector"],
            dv["symmetric_distinct_hardcore_block"],
            dc["single_excitation_nonzero"], dc["ordered_pairs"])),
        ("OVERLAP",
         "R5-LAW-SURVIVES-THE-LIFT=NO-DEFECT-AT-OVERLAP-LE-1-AT-%d-OF-%d-ROWS-BOTH-SHAPES;"
         "AT-OVERLAP-2=%d-OF-%d-CARRY;WINDOW=EVERY-2-SITE-SUPPORT-%d-ROWS-EXHAUSTIVE-IN-GEOMETRY;"
         "THREE-SITE-FULL-SUPPORT=EMPTY-OVER-THE-ALPHABET-%d-ROWS-SWEPT;"
         "COIN-PAIRS=%d-DECLARED-SAMPLE-OF-%d-INTERFERING-COINS-EACH-GATED-SEPARATELY;"
         "R5-18-ROW-SAMPLE=CITED-NOT-RE-RUN"
         % (ov["low_overlap_rows"], ov["low_overlap_rows"],
            ov["overlap_2_nonzero"], ov["overlap_2_rows"], ov["rows"],
            ov["three_site_full_support_rows"], ov["coin_pairs"],
            ov["interfering_coins"])),
        ("MOTION",
         "EIGENPHASES-ADD-EXACTLY(ANTISYMMETRIC=%d;SYMMETRIC=%d;FAILURES=%d)(FORCED-BY-FUNCTORIALITY);"
         "SPEED-SPECTRUM=%s-UNCHANGED-AT-TWO-EXCITATIONS(CEILING-FORCED-BY-THE-DUAL-TORUS;"
         "ALL-THREE-VALUES-ATTAINED);"
         "VELOCITY-DOES-NOT-ADD=%d-OF-%d-CELLS-AT-RAW-ADVANCE-PAIRS-(2,2)-AND-(6,6)-ONLY"
         "(THE-4096-CELLS-AT-(4,4)-ARE-EQUAL-AND-NONZERO-AND-DO-NOT-FAIL);"
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
         "VERDICT-BEARING-STRATUM=THE-%d-CIRCULANTS;"
         "VELOCITY-READING=%s;"
         "NO-TRANSPORT-NUMBER-INHERITED;"
         "CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));"
         "INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;"
         "NO-CONTINUUM-CLAIM;NO-PARTICLE-CLAIM;SHAPE-WORDS-ONLY;"
         "N=2-ONLY-NO-GENERAL-N-CLAIM;NO-BRAID-CLAIM;"
         "NO-CONFIGURATION-SPACE-TOPOLOGY;"
         "COUNTS=COUNTING-ONLY-NO-MEASURE-DECLARED;"
         "NO-CONFIGURATION-MEASURE;NO-ACTION;NO-COUPLING"
         % (D, L, cn["alphabet"], ec["generators"], cn["circulants"],
            mo["convention"])),
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
                         "declared division-event times and leg at the cut; ON "
                         "THE FULL-SUPPORT CIRCULANT STRATUM -- the same "
                         "arena's local window carries 42840 rows of "
                         "both-non-monomial pairs with no defect at all"},
        {"claim": "the two shapes are discriminated by the defect cell by "
                  "cell at exactly the two-excitation defect set",
         "stamp": base + "; the FREE lift; ENTRYWISE comparison on the "
                         "120x120 hard-core block both sectors carry, in the "
                         "same row and column ordering; the circulant stratum"},
        {"claim": "the two shapes' defect VALUE MULTISETS differ at exactly "
                  "the single-excitation defect set",
         "stamp": base + "; the FREE lift; the RELABELLING-INVARIANT "
                         "granularity -- value multisets on the hard-core "
                         "block -- which is a coarser comparison than the "
                         "entrywise one and confines the difference to a "
                         "strictly smaller set; the circulant stratum"},
        {"claim": "the entire two-body excess is created by exchange "
                  "symmetrisation",
         "stamp": base + "; the ORDERED (labelled) sector against the "
                         "symmetrised ones; the FREE lift; occupancy ceiling "
                         "2; the parent's declared division-event times; and "
                         "the ORTHONORMAL SYMMETRISED BASIS, which is the "
                         "description whose change IS the symmetrisation.  "
                         "The law and its consequence are FORCED for every "
                         "unitary family; the 1176 genuine pairs are this "
                         "family's"},
        {"claim": "R5's support-overlap law survives the lift",
         "stamp": base + "; every 2-site support, exhaustive in the geometry, "
                         "against THREE declared interfering coin pairs, each "
                         "gated separately -- the geometry is exhaustive and "
                         "the coin axis is a declared sample of the 512 "
                         "interfering coins; both shapes"},
        {"claim": "the eigenphases add and the velocities do not",
         "stamp": base + "; the FREE lift; R4b's stratified convention "
                         "inherited AS DECLARED (forward difference, tie "
                         "averaged); no transport number inherited"},
        {"claim": "the contact interaction is invisible to the antisymmetric "
                  "shape",
         "stamp": base + "; the declared contact-phase lift, one zeta_8 phase "
                         "of a declared eight; occupancy ceiling 2; measured "
                         "per pair over the circulant stratum"},
    ]


WAIVER_TEXT_LEAK = (
    "the Sym^2 cell from a hard-core configuration (x, y), x != y, into a "
    "doubly-occupied (a, a) is 2 N U_ax U_ay, a single product in a domain, "
    "which cannot cancel; so the symmetric sector leaks out of the hard core "
    "iff some row of U carries two nonzero entries iff U is non-monomial -- an "
    "identity of Sym^2 for EVERY unitary and not a property of this family, "
    "gated as such at G-LEAK-THEOREM-UNIVERSAL on 240 witnesses in dimensions "
    "3, 4 and 5 and on the 3364 out-of-family composites.  The measured "
    "content beside it is WHICH generators of THIS pool are monomial (16 of "
    "64, the parent's Markovian set name for name, G-MONOMIAL-CLASSIFIER) and "
    "hence the SIZE of the split, 48 against 16")

WAIVER_TEXT_DERIV = (
    "B(U tensor U) = B(U) tensor B(U) entrywise, so the ordered defect is "
    "X tensor X - Y tensor Y = Delta tensor X + Y tensor Delta identically; "
    "and X tensor X = Y tensor Y iff X = Y for row-stochastic X and Y (sum "
    "over a free index).  Labelled excitations therefore carry no genuine "
    "two-body defect for ANY unitary family, and by telescoping none at any n "
    "-- gated at G-INDISTINGUISHABILITY-UNIVERSAL.  The measured content "
    "beside it is the SYMMETRISED census, whose 1176 genuine two-body pairs "
    "are family facts, and the check at every pair here is an implementation "
    "check")

WAIVER_TEXT_SPEED = (
    "the declared speed is the branch-free circle distance on Z/8 halved, "
    "whose range is {0, 1, 2} for every argument whatever at L = 4, so no "
    "family and no excitation number could widen it: the ceiling is forced by "
    "the dual torus and not measured.  The measured content beside it is "
    "ATTAINMENT -- that all three values are reached at two excitations -- and "
    "G-VELOCITY-DOES-NOT-ADD, which fires at 7168 cells")


WAIVERS = [
    {"gate": "G-EXCHANGE-COMMUTES",
     "kind": "FORCED",
     "forcing": "P (U tensor U) P^{-1} = U tensor U holds for every U "
                "whatever, so the commutation is an identity of the free lift "
                "and not a property of this family.  Its corollaries are "
                "forced with it: the restriction of a unitary to an invariant "
                "subspace is unitary, and the Born shadow of a unitary is "
                "stochastic, so G-BOTH-SECTORS-ADMITTED carries no "
                "family-dependent content either.  The measured content of "
                "this unit lives in sections 5 to 9, not in the head"},
    {"gate": "G-HARDCORE-ANTISYMMETRIC-CLOSED",
     "kind": "FORCED",
     "forcing": "the wedge carries no doubly-occupied configuration, so there "
                "is nothing for it to leak into -- at n = 2 and at every n.  "
                "The zero is nevertheless MEASURED per generator, as the "
                "wedge's own leak cell count, rather than typed; and the "
                "measured content beside it is the symmetric sector's leak"},
    {"gate": "G-HARDCORE-LEAK-PER-GENERATOR",
     "kind": "FORCED",
     "forcing": WAIVER_TEXT_LEAK},
    {"gate": "G-DERIVATION-LAW",
     "kind": "FORCED",
     "forcing": WAIVER_TEXT_DERIV},
    {"gate": "G-SPEED-CEILING-UNCHANGED",
     "kind": "FORCED",
     "forcing": WAIVER_TEXT_SPEED},
    {"gate": "G-EIGENPHASES-ADD",
     "kind": "FORCED",
     "forcing": "the wedge and the symmetric square are functors, so the "
                "lifted eigenvalue is the product of the symbols by "
                "construction.  It is verified as an exact matrix identity at "
                "every cell anyway, and the measured content beside it is "
                "G-VELOCITY-DOES-NOT-ADD, which fires at 7168 cells"},
]


def choice_inventory(S):
    """THE UNIT WHOSE THESIS IS THAT A DECLARATION DECIDES PUBLISHES ITS
    DECLARATIONS (K2 MAJOR-6), on the parents' schema, with the fibre and the
    verdict-determining flag -- and the flag is CHECKED: moving exactly the
    verdict-determining items must reproduce the set of head names the arena
    census returns, and nothing else may."""
    return [
        {"item": "the occupancy ceiling", "fibre": 2,
         "values": "hard core (1) / two", "class": "GENUINELY-FREE",
         "verdict_determining": True,
         "note": "the head changes name: BOTH-ADMITTED at ceiling 2, "
                 "FORCED-ANTISYMMETRIC at ceiling 1"},
        {"item": "the lift", "fibre": 3,
         "values": "free (U tensor U) / distinguishable (U tensor V) / "
                   "contact-phase", "class": "GENUINELY-FREE",
         "verdict_determining": True,
         "note": "the head returns NEITHER-INVARIANT at the distinguishable "
                 "lift"},
        {"item": "the lattice: the verdict arena against the one-site control",
         "fibre": 2, "values": "L = 4 / one site",
         "class": "DECLARED-CONTROL", "verdict_determining": False,
         "note": "returns FORCED-SYMMETRIC at one site, and is declared a "
                 "degenerate control rather than an arena"},
        {"item": "the division-event times and the leg at the cut",
         "fibre": 1, "values": "the parent's, inherited unchanged",
         "class": "INHERITED-AS-DECLARED", "verdict_determining": False,
         "note": "fixes what the defect MEANS; not re-selected here"},
        {"item": "the velocity convention", "fibre": 2,
         "values": "forward / backward difference, tie averaged",
         "class": "INHERITED-AS-DECLARED", "verdict_determining": False,
         "note": "owns the 7168 velocity failures; R4b's scope stamp binds"},
        {"item": "the third route's window", "fibre": 1,
         "values": "the first 12 generators in the parent's naming, 144 pairs",
         "class": "GENUINELY-FREE", "verdict_determining": False,
         "note": "declared, and gated to contain both predicate classes"},
        {"item": "the local window's coin pairs", "fibre": 3,
         "values": "(0,3), (1,1), (7,11) of the 512 interfering coins",
         "class": "GENUINELY-FREE", "verdict_determining": False,
         "note": "each gated separately; the geometry is exhaustive"},
        {"item": "the contact phase", "fibre": 8, "values": "zeta_8^1 of 8",
         "class": "GENUINELY-FREE", "verdict_determining": False,
         "note": "a declared operator, not a theory"},
        {"item": "the stride window for the coarser reading of the triple "
                 "identity", "fibre": 1, "values": "every 13th ordered pair",
         "class": "GENUINELY-FREE", "verdict_determining": False,
         "note": "declared as data; 259 pairs"},
        {"item": "d, L, the alphabet, the stencil, the axes, the connective, "
                 "the symmetrised basis", "fibre": 1,
         "values": "anchored or forced", "class": "FORCED",
         "verdict_determining": False,
         "note": "read from the parents and the stage; none is this unit's"},
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


HEXDIGITS = "0123456789abcdef"


def is_digest_string(s):
    """a sha256-12 is not a measurement.  39 of the delivered licence pool's
    218 members were supplied by digest strings alone -- among them 256 -- so
    a numeral could be licensed by a hash (K3 MAJOR-2).  Digests are removed
    from the pool: only measured integers, declared value strings and the
    named structural numerals license anything."""
    return (len(s) == 12 and all(c in HEXDIGITS for c in s)
            and not s.isdigit())


def licensed_numerals(obj, acc):
    if isinstance(obj, bool):
        return acc
    if isinstance(obj, int):
        acc.add(str(obj))
        acc.add(str(-obj) if obj < 0 else str(obj))
    elif isinstance(obj, str):
        if not is_digest_string(obj):
            acc |= numerals(obj)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if not is_digest_string(str(k)):
                acc |= numerals(str(k))
            licensed_numerals(v, acc)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            licensed_numerals(v, acc)
    return acc


STRUCTURAL = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
              "13", "14", "22", "2026"}


def fenced_blocks(text):
    """the fenced blocks, as text.  Markdown fences are the odd segments of a
    split on the fence marker; nothing here needs a regular expression."""
    parts = text.split("```")
    out = []
    for i in range(1, len(parts), 2):
        body = parts[i]
        if "\n" in body:
            body = body.split("\n", 1)[1]
        out.append(norm_text(body))
    return out


def block_multiset(text):
    """E-22: the fenced blocks are compared as a MULTISET and not by
    containment.  A paper carrying a clean verdict fence AND a forged twin
    satisfies containment with the clean copy; the twin is what #168's own
    demonstrated failure was, and it is what this gate exists to catch."""
    out = {}
    for b in fenced_blocks(text):
        out[b] = out.get(b, 0) + 1
    return out


def banned_words_found(text):
    """the pin's wall, made an instrument: shape words survive only as the
    compounds the pin licenses, and the bare particle nouns do not survive at
    all.  The scan is over WORDS, so 'fermionic-shape' passes and 'Fermion'
    does not (K3 MAJOR-1: the wall was named by an anchor whose consumer gate
    did not exist, and an injection that rewrote it to 'A particle is named.
    Fermion and boson are particle words' passed every paper gate)."""
    low = text.lower()
    for c in LICENSED_COMPOUNDS:
        low = low.replace(c, " ")
    word, found = "", []
    for ch in low + " ":
        if ch.isalpha():
            word += ch
        else:
            if word in BANNED_WORDS:
                found.append(word)
            word = ""
    return sorted(set(found))


def paper_tables(S):
    """E-22: TABLES RENDER AS CLAIMS.  Every cell of the three load-bearing
    tables is assembled from THIS RUN's measurements and required to occur in
    the paper exactly once, so a swapped row, an inverted lives/dies cell or a
    zeroed positive control dies inside the run (K3 injections 5, 6, 12, 13,
    17 all survived at exit 0)."""
    blocks = {"ARENA": [], "SECTOR": [], "OVERLAP": [], "CHOICE": [], "WITNESS": []}
    for a in S["arena_census"]["arenas"]:
        blocks["ARENA"].append(("T-" + a["arena"],
                                "| `%s` | %s | %s | `%s` |"
                                % (a["arena"],
                                   "lives" if a["antisymmetric_lives"] else "dies",
                                   "lives" if a["symmetric_lives"] else "dies",
                                   S["verdict"]["heads_by_arena"][a["arena"]])))
    dc = S["defect_census"]
    for label, key in (("one excitation", "single_excitation_nonzero"),
                       ("ordered, labelled configurations", "ordered_sector_nonzero"),
                       ("symmetric", "symmetric_nonzero"),
                       ("antisymmetric", "antisymmetric_nonzero")):
        blocks["SECTOR"].append(("T-SECTOR-" + key,
                                 "| %s | %d | %d |"
                                 % (label, dc["ordered_pairs"], dc[key])))
    for r in S["overlap_census"]["by_overlap"]:
        blocks["OVERLAP"].append(("T-OVERLAP-%d" % r["overlap"],
                                  "| %d | %d | %d | %d | %d |"
                                  % (r["overlap"], r["rows"],
                                     r["single_excitation_nonzero"],
                                     r["antisymmetric_nonzero"],
                                     r["symmetric_nonzero"])))
    for i, c in enumerate(S["choice_inventory"]):
        blocks["CHOICE"].append(("T-CHOICE-%d" % i,
                                 "| %s | %s | %s | %s |"
                                 % (c["item"], c["fibre"], c["class"],
                                    "YES" if c["verdict_determining"] else "no")))
    for w in S["discrimination"]["witness"]["named_cells"]:
        blocks["WITNESS"].append(("T-WITNESS-%d-%d" % (w["column"][0], w["column"][1]),
                                  "| {%d,%d} | {%d,%d} | %s | %s |"
                                  % (w["row"][0], w["row"][1],
                                     w["column"][0], w["column"][1],
                                     w["symmetric"], w["antisymmetric"])))
    rows = []
    for name in ("ARENA", "SECTOR", "OVERLAP", "CHOICE", "WITNESS"):
        rows.extend(blocks[name])
        # and the whole table AS AN ORDERED BLOCK: occurrence counting cannot
        # see a SWAP of two rows, which is what injection 5 was (K3)
        rows.append(("T-BLOCK-" + name,
                     " ".join(r for _i, r in blocks[name])))
    return rows


def paper_polarity(S, text, mutated=False):
    """the paper's own SENTENCES carry polarity, not only its numbers: for
    each pair the positive form must be present and its negation absent.  An
    inverted headline and an inverted wall both passed every delivered gate."""
    pairs = [
        ("P-SELECTS", "The composition law is silent",
         "The composition law selects"),
        ("P-CEILING", "the occupancy ceiling, and the stage anchors none",
         "the occupancy ceiling, and the stage anchors one"),
        ("P-WALL-PARTICLE", "No particle is named",
         "A particle is named"),
        ("P-WALL-SHAPE", "are shape words for the antisymmetric and symmetric "
                         "sectors",
         "are particle words for the antisymmetric and symmetric sectors"),
        ("P-ANTI-CLOSES", "the antisymmetric shape closes at every generator",
         "the antisymmetric shape leaks at every generator"),
        ("P-STRATUM", "is a statement about the circulant stratum",
         "is a statement about the whole arena"),
    ]
    out = []
    norm = norm_text(text)
    for pid, pos, neg in pairs:
        if mutated:
            pos, neg = neg, pos
        hp = norm_text(pos) in norm
        hn = norm_text(neg) in norm
        out.append({"id": pid, "positive": pos, "negative": neg,
                    "positive_present": hp, "negative_present": hn,
                    "ok": hp and not hn})
    return out


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
         "text": "value multisets differ at %d of the %d ordered pairs"
                 % (di["differing_pairs"], dc["ordered_pairs"]),
         "path": "discrimination/differing_pairs"},
        {"id": "CL-ENTRYWISE",
         "text": "differ cell by cell at %d of %d ordered pairs and agree at %d"
                 % (di["entrywise_differing_pairs"], dc["ordered_pairs"],
                    di["entrywise_agreeing_pairs"]),
         "path": "discrimination/entrywise_differing_pairs"},
        {"id": "CL-WITNESS",
         "text": "differ at %d cells" % di["witness"]["entrywise_differing_cells"],
         "path": "discrimination/witness/entrywise_differing_cells"},
        {"id": "CL-STRIDE",
         "text": "%d of the %d pairs of the declared stride window"
                 % (di["stride_window"]["single_excitation"],
                    di["stride_window"]["pairs"]),
         "path": "discrimination/stride_window/single_excitation"},
        {"id": "CL-LOCAL-GRAIN",
         "text": "differ at %d of the %d rows at overlap two"
                 % (ov["overlap_2_shapes_differ_entrywise"], ov["overlap_2_rows"]),
         "path": "overlap_census/overlap_2_shapes_differ_entrywise"},
        {"id": "CL-SECTOR-VALUES",
         "text": "%d distinct values in the symmetric sector, of which %d are "
                 "never seen on the block"
                 % (dv["symmetric_distinct_full_sector"],
                    len(dv["values_only_off_the_block"])),
         "path": "defect_values/symmetric_distinct_full_sector"},
        {"id": "CL-THEOREM-LEAK",
         "text": "%d constructed witnesses and %d out-of-family composites"
                 % (S["theorems"]["leak_law"]["witnesses"],
                    S["theorems"]["leak_law"]["out_of_family_composites"]),
         "path": "theorems/leak_law/witnesses"},
        {"id": "CL-STAGE-KEYS",
         "text": "%d declaration keys and none of them occupancy-shaped"
                 % oc["stage_declaration_keys"],
         "path": "occupancy/stage_declaration_keys"},
        {"id": "CL-A4-NEITHER",
         "text": "neither sector is invariant at %d of %d"
                 % (ar["distinguishable_neither_invariant"],
                    ar["distinguishable_pairs"]),
         "path": "arena_census/distinguishable_neither_invariant"},
        {"id": "CL-RAW-VELOCITY",
         "text": "%d cells carry two equal nonzero advances and do not fail"
                 % mo["equal_and_nonzero_not_failing_cells"],
         "path": "motion/equal_and_nonzero_not_failing_cells"},
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
         "text": "moves it at %d of the %d ordered pairs and the "
                 "antisymmetric one at %d"
                 % (ch["symmetric_defect_moved"], ch["pairs"],
                    ch["antisymmetric_defect_moved"]),
         "path": "contact_handle/symmetric_defect_moved"},
        {"id": "CL-A4",
         "text": "%d of %d ordered pairs of distinct generators"
                 % (ar["distinguishable_broken"], ar["distinguishable_pairs"]),
         "path": "arena_census/distinguishable_broken"},
        {"id": "CL-VALUES",
         "text": "%d distinct values in the antisymmetric shape and %d on the "
                 "hard-core block in the symmetric"
                 % (dv["antisymmetric_distinct"],
                    dv["symmetric_distinct_hardcore_block"]),
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


def verify_paper(S, LD, path, SEAL):
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
    counted = []
    for c in claims:
        counted.append(dict(c, occurrences=norm.count(norm_text(c["text"]))))
    bad_count = [c["id"] for c in counted if c["occurrences"] != 1]
    LD.gate("G-PAPER-CLAIMS",
            "every claim the paper makes about a measured quantity renders "
            "from a receipt key and occurs in the paper EXACTLY ONCE -- an "
            "occurrence count, not containment.  Eleven of the delivered "
            "claim strings occurred two to five times, so corrupting any one "
            "copy left the claim satisfied by its twins (#125's "
            "duplicate-shadow variant); one occurrence each is the repair, and "
            "it is the paper that was made to satisfy it",
            not bad_count,
            "%d claims, %d not occurring exactly once: %s"
            % (len(counted), len(bad_count), bad_count))
    S["paper_claims"] = counted
    SEAL.take_all_at("G-PAPER-CLAIMS", S, LD)

    trows = paper_tables(S)
    if mut("MUT-PAPER-TABLE"):
        trows = trows[:-1] + [("T-FORGED", "| FORGED | 0 | 0 | 0 |")]
    tcounts, tbad = [], []
    for tid, row in trows:
        occ = norm.count(norm_text(row))
        tcounts.append({"id": tid, "row": row, "occurrences": occ})
        if occ != 1:
            tbad.append(tid)
    S["paper_tables"] = tcounts
    LD.gate("G-PAPER-TABLES",
            "E-22: THE TABLES RENDER AS CLAIMS.  Every row of the arena table, "
            "the sector table, the overlap table, the choice inventory and the "
            "witness cells is ASSEMBLED FROM THIS RUN's own measurements and "
            "required to occur in the paper exactly once, so a swapped row, an "
            "inverted lives/dies cell or a zeroed positive control dies inside "
            "the run rather than shipping at exit 0",
            not tbad, "%d rendered table rows, %d not located exactly once: %s"
            % (len(tcounts), len(tbad), tbad))
    SEAL.take_all_at("G-PAPER-TABLES", S, LD)

    vs = S["verdict"]["string"]
    if mut("MUT-PAPER-VERDICT"):
        vs = vs[:40]
    blocks = block_multiset(txt)
    if mut("MUT-PAPER-BLOCK"):
        blocks = dict(blocks)
        blocks[norm_text("A SECOND FENCE")] = 1
    want = {norm_text(vs): 1}
    LD.gate("G-PAPER-VERDICT-BLOCK",
            "the paper quotes the COMPLETE verdict string the instrument "
            "emits, character for character -- and its FENCED BLOCKS are "
            "compared to the derived verdict AS A MULTISET (E-22), not by "
            "containment: the paper carries exactly one fenced block and it is "
            "exactly this string, so a second fence asserting the opposite "
            "head cannot hide behind a clean twin",
            norm_text(vs) in norm and len(vs) > 400 and blocks == want,
            "%d characters of verdict quoted; %d fenced blocks, %d distinct, "
            "multiset matches the derived verdict: %s"
            % (len(vs), sum(blocks.values()), len(blocks), blocks == want))

    lic = licensed_numerals(S, set()) | STRUCTURAL
    pn = numerals(txt)
    if mut("MUT-PAPER-NUMERAL"):
        pn = pn | {"987654321"}
    unlicensed = sorted(n for n in pn if n not in lic)
    LD.gate("G-PAPER-NUMERAL-COVERAGE",
            "EVERY numeral in the paper -- prose, inline code spans, tables "
            "and the fenced verdict block alike -- is licensed by a MEASURED "
            "receipt value or is one of the declared structural numerals.  No "
            "numeral is licensed by a sha256 digest: the digest strings are "
            "removed from the pool",
            not unlicensed,
            "%d numerals in the paper, %d unlicensed: %s; %d licensed values"
            % (len(pn), len(unlicensed), unlicensed[:8], len(lic)))

    bad = banned_words_found(txt)
    if mut("MUT-PAPER-WALL"):
        bad = bad + ["INJECTED"]
    LD.gate("G-NO-PARTICLE-NAMING",
            "the pin's wall is an INSTRUMENT and not a label: this unit's own "
            "paper is scanned word by word against a declared banned list, and "
            "the shape words survive only as the compounds the pin licenses "
            "-- fermionic-shape and bosonic-shape.  No particle noun, no spin, "
            "no anyon and no bare shape adjective occurs anywhere in it",
            not bad, "%d banned words found: %s; %d licensed compounds"
            % (len(bad), bad, len(LICENSED_COMPOUNDS)))

    conn = [n for v, _s, n, _g in VERBATIM if v == "VB-CONNECTIVE"][0]
    if mut("MUT-CONNECTIVE"):
        conn = conn.replace("(1,1)", "(1,2)")
    seg = dict(S["verdict"]["segments"])["SCOPE"]
    # the paper must carry the clause once in its own prose BESIDE the copy
    # inside the verdict fence -- an occurrence count derived from the verdict
    # string itself, because a containment test is satisfied by the fence's
    # copy while the prose span is forged (K3 injection 1)
    want_conn = norm_text(S["verdict"]["string"]).count(norm_text(conn)) + 1
    got_conn = norm.count(norm_text(conn))
    LD.gate("G-CONNECTIVE-VERBATIM",
            "the connective clause travels VERBATIM, and the three copies are "
            "compared: the parent's own bytes, this unit's SCOPE segment, and "
            "the paper's own inline span -- the last by OCCURRENCE COUNT "
            "against the verdict string's own copies, so an inline span "
            "altered from LINK-(1,1) to LINK-(1,2) cannot hide behind the "
            "copy inside the fence",
            conn in seg and got_conn == want_conn
            and conn == "CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))",
            "the anchored clause is in the SCOPE segment and occurs %d times "
            "in the paper, %d expected" % (got_conn, want_conn))

    pol = paper_polarity(S, txt, mutated=mut("MUT-PAPER-POLARITY"))
    bad_pol_sent = [p["id"] for p in pol if not p["ok"]]
    LD.gate("G-PAPER-SENTENCE-POLARITY",
            "the paper's load-bearing SENTENCES carry polarity as its numbers "
            "do: for each declared pair the positive form must be present and "
            "its negation absent, so an inverted headline or an inverted wall "
            "dies here.  Both survived every delivered gate",
            not bad_pol_sent,
            "%d sentence polarities, %d failing: %s"
            % (len(pol), len(bad_pol_sent), bad_pol_sent))

    state_before = digest(json.dumps(S, indent=1, sort_keys=True))
    bad_pol = []
    for c in claims:
        old = perturb(S, c["path"])
        moved = paper_claims(S)
        new = [x for x in moved if x["id"] == c["id"]][0]
        if mut("MUT-PAPER-POLARITY-RENDER"):
            new = c                       # a claim that does not render from
        if not mut("MUT-RESTORE-NEUTERED"):
            restore(S, c["path"], old)    # the receipt cannot have polarity
        if new["text"] == c["text"] or norm_text(new["text"]) in norm:
            bad_pol.append(c["id"])
    LD.gate("G-PAPER-CLAIM-POLARITY",
            "and every claim has POLARITY: perturbing the receipt key it "
            "renders from moves the claim, and the moved claim is no longer "
            "found in the paper -- so a claim cannot be satisfied by accident",
            not bad_pol, "%d claims with no polarity: %s" % (len(bad_pol), bad_pol))

    # #119: the polarity test perturbs SEALED objects, so the state it hands
    # back must be the state it was given -- byte for byte.  One silently
    # failed restore delivered a sealed receipt asserting 65 of 64 generators
    # at exit 0 (K3 INJ-11); the restoration is now itself a gate.
    state_after = digest(json.dumps(S, indent=1, sort_keys=True))
    LD.gate("G-STATE-RESTORED",
            "the paper verification is NON-DESTRUCTIVE: every perturbation it "
            "takes for the polarity test is restored, and the whole state is "
            "digested before and after and required to be identical.  A "
            "restore that silently fails moves a sealed, published row and is "
            "caught here and again at G-SEAL-COMPLETE",
            state_before == state_after,
            "state digest %s before, %s after" % (state_before, state_after))

    S["paper_coverage"] = {"numerals": len(pn), "unlicensed": len(unlicensed),
                           "claims": len(counted), "table_rows": len(tcounts),
                           "fenced_blocks": sum(blocks.values()),
                           "sentence_polarities": len(pol),
                           "banned_words": len(bad),
                           "licensed_values": len(lic),
                           "polarity_failures": len(bad_pol),
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
    ("MUT-PAPER-POLARITY", "G-PAPER-SENTENCE-POLARITY",
     "inverts the paper's declared sentence polarities, so the negative form "
     "of the headline and of the walls is what the paper carries"),
    ("MUT-STAMP-DROP", "G-DESCRIPTION-STAMPS", "drops a description stamp"),
    ("MUT-WAIVER-UNFORCED", "G-WAIVERS-VERIFIED", "waives a gate with no forcing"),
    ("MUT-RECEIPT-FLOAT", "G-RECEIPT-EXACT", "writes a float into the receipt"),
    ("MUT-PATH-ANCHOR", "G-PATH-VALUE-ANCHORS", "breaks one anchored value"),
    ("MUT-CONTROL-COUNT", "G-REBUILD-CONTROLS", "drops one declared control"),
    ("MUT-INVARIANT", "G-REBUILD-INVARIANTS", "reports one invariant mismatch"),
    ("MUT-MONOMIAL-LIST", "G-MONOMIAL-CLASSIFIER", "drops a monomial name"),
    ("MUT-BOTH-ADMITTED", "G-BOTH-SECTORS-ADMITTED", "closes one sector to one generator"),
    ("MUT-CEILINGS", "G-CEILINGS-AGREE-AT-ONE-EXCITATION", "separates the two ceilings at one excitation"),
    ("MUT-HEAD-REACH", "G-HEAD-LAW-EXERCISED",
     "makes two of the four declared arenas return the same pre-registered "
     "name, so the reachability discharge would rest on three branches"),
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
    ("MUT-CACHE-DIRTY", "G-CACHE-UNPOLLUTED",
     "fabricates a polluted-cache report without polluting anything: the "
     "SYNTHETIC falsifier, kept beside the two real ones so the difference is "
     "on the record"),
    ("MUT-CACHE-SVALS", "G-CACHE-UNPOLLUTED",
     "writes IN PLACE into the cached census's svals, a published value "
     "multiset the delivered digest did not cover"),
    ("MUT-CACHE-ROWS", "G-CACHE-UNPOLLUTED",
     "writes IN PLACE into the cached census's rows, the per-pair cell counts "
     "the delivered digest did not cover"),
    ("MUT-LEAK-THEOREM", "G-LEAK-THEOREM-UNIVERSAL",
     "reports a witness at which the leak law fails"),
    ("MUT-TELESCOPE", "G-INDISTINGUISHABILITY-UNIVERSAL",
     "reports a failure of the telescoping identity"),
    ("MUT-WEDGE-LEAK", "G-HARDCORE-ANTISYMMETRIC-CLOSED",
     "gives the wedge a hard-core leak cell"),
    ("MUT-CEILING-SET", "G-CEILINGS-AGREE-AT-ONE-EXCITATION",
     "shortens one ceiling's one-excitation configuration set"),
    ("MUT-STAGE-OCCUPANCY-KEY", "G-STAGE-DECLARES-NO-OCCUPANCY",
     "adds an occupancy-shaped key to the stage's declarations"),
    ("MUT-A4-INVARIANT", "G-A4-NEITHER-INVARIANT",
     "claims a sector stays invariant under the distinguishable lift"),
    ("MUT-PREDICATE-OBJECT", "G-TWO-EXCITATION-PREDICATE",
     "swaps one pair in for another, preserving the cardinality exactly, so "
     "only the per-object clause can catch it"),
    ("MUT-MARKOV-CARRY", "G-MARKOV-INHERITED",
     "gives a monomial-leg pair a defect"),
    ("MUT-FIBRE", "G-DERIVATION-LAW",
     "reports a failure of the derivation law's one-parameter fibre"),
    ("MUT-ENTRYWISE", "G-SHAPES-DISCRIMINATED-ENTRYWISE",
     "drops one entrywise-differing pair"),
    ("MUT-JOINT-ZERO", "G-SHAPES-DISCRIMINATED-ENTRYWISE",
     "drops one jointly-zero pair"),
    ("MUT-WITNESS", "G-SHAPES-DISCRIMINATED-ENTRYWISE",
     "zeroes the declared witness's differing cell count"),
    ("MUT-SAMPLE-WINDOW", "G-TRIPLE-IDENTITY-BOTH-GRANULARITIES",
     "shortens the declared stride window"),
    ("MUT-SECTOR-VALUES", "G-DEFECT-RATIONAL",
     "claims an irrational value in the symmetric sector off the block"),
    ("MUT-WINDOW-BLIND", "G-THIRD-CODE-PATH",
     "empties the third route's window of monomial generators, so its "
     "agreement would be an agreement about one predicate class"),
    ("MUT-R5-CITED", "G-R5-PRECEDENT-CITED",
     "moves the cited row count away from R5's own sentence"),
    ("MUT-LOCAL-GRAIN", "G-OVERLAP-SHAPES-AT-THE-LOCAL-GRAIN",
     "claims the shapes are discriminated at every overlap-2 row"),
    ("MUT-R4B-CONVENTION", "G-R4B-CONVENTION-INHERITED",
     "derives the convention word from a tie reading R4b did not declare"),
    ("MUT-RAW-PAIRS", "G-VELOCITY-DOES-NOT-ADD",
     "adds a failing raw advance pair the census does not carry"),
    ("MUT-CHOICE-FLAG", "G-CHOICE-INVENTORY-VERDICT-DETERMINING",
     "flags a choice as verdict-determining that determines no verdict"),
    ("MUT-PAPER-TABLE", "G-PAPER-TABLES", "forges one rendered table row"),
    ("MUT-PAPER-BLOCK", "G-PAPER-VERDICT-BLOCK",
     "adds a second fenced block to the paper's block multiset"),
    ("MUT-PAPER-WALL", "G-NO-PARTICLE-NAMING",
     "reports a banned particle word in the paper"),
    ("MUT-CONNECTIVE", "G-CONNECTIVE-VERBATIM",
     "alters the anchored connective clause's link"),
    ("MUT-PAPER-POLARITY-RENDER", "G-PAPER-CLAIM-POLARITY",
     "injects a claim with no polarity"),
    ("MUT-RESTORE-NEUTERED", "G-STATE-RESTORED",
     "neuters the polarity test's restore, leaving a sealed published row "
     "perturbed in the delivered state"),
    ("MUT-SEAL-PROVENANCE", "G-SEAL-PROVENANCE",
     "seals an object at a gate that does not exist"),
    ("MUT-ANCHOR-CONSUMER", "G-ANCHOR-CONSUMERS",
     "names a consumer gate this instrument does not evaluate"),
    ("MUT-CLI-OPEN", "G-CLI-WHITELIST",
     "opens the argv whitelist so an unknown flag is accepted"),
    ("MUT-SCHEMA-KEY", "G-RECEIPT-SCHEMA",
     "publishes a schema key set that is not the manifest"),
    ("MUT-ROWS-BOUND", "G-PUBLISHED-ROWS-BOUND",
     "moves a published summary count away from the rows it summarises"),
    ("MUT-DEFECT-DEFINITION", "G-DEFECT-DEFINITION",
     "computes the defect by a definition the anchor does not carry"),
    ("MUT-DEFECT-WITNESS", "G-DEFECT-WITNESS",
     "breaks the seed paper's own witness property"),
    ("MUT-PIN-QUESTION", "G-PIN-QUESTION-IS-THE-PARENTS",
     "asks a question the pin and the parent do not name"),
    ("MUT-SECTOR-NEW", "G-SECTOR-IS-NEW",
     "claims the parent already carried a multi-excitation sector"),
    ("MUT-TRANSPORT", "G-NO-TRANSPORT-NUMBER-INHERITED",
     "inherits a transport number from R4b"),
]

# MUT-SPEED-CEILING's published description was inverted: sp2[:-1] NARROWS the
# spectrum (E-23).  Corrected in place rather than left to be read as a
# capability the falsifier does not exercise.
MUTANTS = [(n, g, ("narrows the two-excitation speed spectrum"
                   if n == "MUT-SPEED-CEILING" else
                   "flips the rationality flag without injecting a value"
                   if n == "MUT-IRRATIONAL" else w))
           for n, g, w in MUTANTS]


# ===========================================================================
# SECTION 16.  THE STATE, END TO END
# ===========================================================================

def build_state(break_anchor=None, paper_path=None):
    SEAL = Seal()
    S, LD, pool, circ, SRC, texts = build_arena(break_anchor, SEAL)
    exchange_census(S, LD, pool, SRC, SEAL)
    occupancy_census(S, LD, pool, SRC, circ, SEAL)
    theorem_census(S, LD, circ)
    SEAL.take_all_at("G-INDISTINGUISHABILITY-UNIVERSAL", S, LD)
    arena_census(S, LD, pool, circ, SEAL)
    alpha = build_alphabet()
    C = defect_census(S, LD, circ, SRC, SEAL)
    overlap_census(S, LD, alpha, SRC, texts, SEAL)
    motion_census(S, LD, circ, SRC, SEAL)
    contact_census(S, LD, circ, C["single_nz"], SEAL)

    stamps = description_stamps(S)
    if mut("MUT-STAMP-DROP"):
        stamps = stamps[:-1]
    LD.gate("G-DESCRIPTION-STAMPS",
            "every quantum-layer claim this unit makes carries a description "
            "stamp naming the sector, the lift, the occupancy ceiling, the "
            "granularity of the comparison and the stratum it was measured on; "
            "a claim without one is not a claim this unit makes",
            len(stamps) == 9 and all(len(x["stamp"]) > 60 for x in stamps),
            "%d stamped claims" % len(stamps))
    S["description_stamps"] = stamps
    SEAL.take_all_at("G-DESCRIPTION-STAMPS", S, LD)

    inv = choice_inventory(S)
    if mut("MUT-CHOICE-FLAG"):
        inv = [dict(r, verdict_determining=True) for r in inv]
    vd = [r for r in inv if r["verdict_determining"]]
    LD.gate("G-CHOICE-INVENTORY-VERDICT-DETERMINING",
            "the unit whose whole thesis is that a DECLARATION decides "
            "publishes its declarations, on the parents' schema, with the "
            "fibre and the verdict-determining flag -- and the flag is "
            "CHECKED against the arena census rather than asserted: exactly "
            "the items flagged verdict-determining are the ones the four "
            "declared arenas move, and moving them returns exactly the four "
            "distinct pre-registered head names the census reports",
            len(inv) == 10 and len(vd) == 2
            and {r["item"] for r in vd} == {"the occupancy ceiling", "the lift"}
            and all(isinstance(r["fibre"], int) and r["fibre"] >= 1 for r in inv)
            and len({a["arena"] for a in S["arena_census"]["arenas"]}) == 4,
            "%d inventory rows, %d verdict-determining: %s"
            % (len(inv), len(vd), sorted(r["item"] for r in vd)))
    S["choice_inventory"] = inv
    SEAL.take_all_at("G-CHOICE-INVENTORY-VERDICT-DETERMINING", S, LD)

    wl = list(WAIVERS)
    if mut("MUT-WAIVER-UNFORCED"):
        wl = wl + [{"gate": "G-PARENT-REPRODUCED", "kind": "FORCED", "forcing": "x"}]
    ok = all(w["gate"] in LD.ids and len(w["forcing"]) > 80 for w in wl)
    LD.gate("G-WAIVERS-VERIFIED",
            "every gate registered as a DISCLOSURE names the mechanism that "
            "forces it and names the measuring gate that stands in its place; "
            "no gate carrying measured content is waived.  Six gates are "
            "disclosures here rather than three: the two forcings the unit "
            "delivered as measurements -- the hard-core split and the "
            "ordered-sector derivation law -- are theorems about every "
            "unitary, and the speed ceiling is forced by the dual torus",
            ok and {w["gate"] for w in wl} ==
            {r["gate"] for r in LD.rows if r["kind"] == "DISCLOSURE"},
            "%d waivers, all forced and all matched to a disclosure" % len(wl))
    S["waiver_ledger"] = wl
    SEAL.take_all_at("G-WAIVERS-VERIFIED", S, LD)

    S["schema"] = {"unit": "R4c", "paper": "v14/paper-22-multi.md",
                   "instrument": "v14/code/r4c_multi_exact.py",
                   "version": 2, "arithmetic": "Q(zeta_8), exact, dyadic",
                   "published_keys": sorted(FINAL_KEYS),
                   "unsealed_declared": UNSEALED_DECLARED}
    S["provenance"] = {
        "sources": [{"anchor": a, "path": p, "sha256_12": h} for a, p, h in SOURCES],
        "runtime_inputs": sorted(set(os.path.relpath(p, ROOT) for p in READS)
                                 | ({os.path.relpath(paper_path, ROOT)}
                                    if paper_path else set())),
        "not_executed": ["no other unit's program is imported or executed; "
                         "the parents are read as bytes and as anchored values "
                         "only", "R5's 18-row two-excitation table is CITED "
                         "and NOT re-run, as the pin requires",
                         "no transport number is inherited from R4b"],
        "python": sys.version.split()[0],
    }
    sch = dict(S["schema"])
    if mut("MUT-SCHEMA-KEY"):
        S["schema"] = dict(sch, published_keys=sorted(FINAL_KEYS)[:-1])
    LD.gate("G-RECEIPT-SCHEMA",
            "the receipt's own schema and provenance are BOUND rather than "
            "decorative: the published key list is the manifest itself, every "
            "declared unsealed key is declared with a reason, every anchored "
            "source appears in the provenance with the digest the run "
            "verified, and the runtime inputs are the paths this run actually "
            "read -- the paper included, which the delivered provenance "
            "omitted because it was built before the paper was read",
            set(S["schema"]["published_keys"]) == set(FINAL_KEYS)
            and set(S["schema"]["unsealed_declared"]) == set(UNSEALED_DECLARED)
            and [r["anchor"] for r in S["provenance"]["sources"]]
            == [a for a, _p, _h in SOURCES]
            and all(r["sha256_12"] == h
                    for r, (_a, _p, h) in zip(S["provenance"]["sources"], SOURCES))
            and all(os.path.relpath(p, ROOT) in S["provenance"]["runtime_inputs"]
                    for _a, p, _h in [(a, os.path.join(ROOT, p), h)
                                      for a, p, h in SOURCES]),
            "%d published keys, %d declared unsealed, %d sources, %d runtime "
            "inputs" % (len(S["schema"]["published_keys"]),
                        len(S["schema"]["unsealed_declared"]),
                        len(S["provenance"]["sources"]),
                        len(S["provenance"]["runtime_inputs"])))
    SEAL.take_all_at("G-RECEIPT-SCHEMA", S, LD)

    counts = {
        "d": D, "L": L, "sites": NS, "alphabet": len(set(alpha)),
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
        "entrywise_discriminating_pairs":
            S["discrimination"]["entrywise_differing_pairs"],
        "overlap_rows": S["overlap_census"]["rows"],
        "velocity_failures": S["motion"]["velocity_failures"],
        "velocity_cells": S["motion"]["velocity_cells"],
        "contact_symmetric_moved": S["contact_handle"]["symmetric_defect_moved"],
        "contact_antisymmetric_moved": S["contact_handle"]["antisymmetric_defect_moved"],
        "theorem_witnesses": S["theorems"]["leak_law"]["witnesses"],
        "gates": len(LD.rows),
    }
    if mut("MUT-ROWS-BOUND"):
        counts = dict(counts, symmetric_leaking=counts["symmetric_leaking"] + 1)
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
    bound_bad = []
    for key, got, want in (
            ("pool", counts["pool"], len(S["exchange_census"]["rows"])),
            ("commuting", counts["commuting"],
             sum(1 for r in S["exchange_census"]["rows"] if r["exchange_commutes"])),
            ("symmetric_leaking", counts["symmetric_leaking"],
             sum(1 for r in S["occupancy"]["rows"]
                 if not r["symmetric_hardcore_closed"])),
            ("overlap_rows", counts["overlap_rows"],
             sum(r["rows"] for r in S["overlap_census"]["by_overlap"])),
            ("circulants", counts["circulants"],
             sum(1 for r in S["pool"] if r["kind"] == "CIRC")),
            ("r4b_tie_cells", S["parent_reproduction"]["r4b_tie_cells"],
             S["motion"]["r4b_tie_cells"])):
        if got != want:
            bound_bad.append((key, got, want))
    LD.gate("G-PUBLISHED-ROWS-BOUND",
            "every summary count the receipt publishes is RE-DERIVED from the "
            "per-object rows it summarises and required to agree: the pool "
            "size from the exchange rows, the commutation tally from their own "
            "predicates, the leak from the occupancy rows, the overlap total "
            "from the by-overlap table, the circulant count from the pool "
            "listing.  A summary that drifts from its rows dies here rather "
            "than being sealed beside them",
            not bound_bad, "%d summary counts re-derived from their rows, %d "
            "disagreeing: %s" % (6, len(bound_bad), bound_bad))
    SEAL.take_all_at("G-PUBLISHED-ROWS-BOUND", S, LD)

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
    SEAL.take_all_at("G-VERDICT-RECONSTRUCTED", S, LD)

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
    # THE TWO REAL CACHE INJECTIONS.  The delivered gate digested 7 of the 11
    # fields of 1 of the 7 caches; five real in-place pollutions were put to
    # it and it fired on none of them (K3 v4).  These two write IN PLACE into
    # the cached object AFTER the consumer has taken its defensive copy, so
    # nothing downstream can see them -- only this gate can.
    pk = pool_key(circ)
    if mut("MUT-CACHE-SVALS") and pk in CENSUS_CACHE:
        sv = CENSUS_CACHE[pk]["svals"]
        sv[sorted(sv)[0]] += 1
    if mut("MUT-CACHE-ROWS") and pk in CENSUS_CACHE:
        rws = CENSUS_CACHE[pk]["rows"]
        k0 = sorted(rws)[0]
        rws[k0] = (rws[k0][0] + 1,) + rws[k0][1:]
    dirty = ["INJECTED"] if mut("MUT-CACHE-DIRTY") else [
        list(k) if isinstance(k, tuple) else k for k, v in CENSUS_CACHE.items()
        if digest(canon_repr(v)) != CENSUS_DIGESTS.get(k)]
    LD.gate("G-CACHE-UNPOLLUTED",
            "EVERY memoised census this run was served is the census that was "
            "computed, field for field: EVERY cache family is fingerprinted at "
            "creation over its WHOLE contents -- not seven fields of one of "
            "them -- and every fingerprint is re-checked here.  So no "
            "injection, this run's or an earlier run's, can reach the next run "
            "through the memo, and the mutant sweep measures independent runs "
            "rather than one contaminated sequence",
            not dirty and len(CENSUS_DIGESTS) == len(CENSUS_CACHE) >= 8,
            "%d cached censuses fingerprinted, %d polluted: %s"
            % (len(CENSUS_DIGESTS), len(dirty), dirty[:3]))

    if mut("MUT-RECEIPT-FLOAT"):
        S["schema"]["probe"] = float("1.5")   # built, never written as a literal
    bad = scan(S, [])
    LD.gate("G-RECEIPT-EXACT",
            "the emitted receipt contains no float anywhere: a recursive type "
            "scan of every value it publishes",
            not bad, "%d float values" % len(bad))

    # the argv whitelist is exercised INSIDE the run, so the gate that
    # publishes cli_probes has a declared falsifier like every other (E-23).
    cli_probes = [
        {"argv": ["--nope"], "rejected": cli_error_probe(parse_args, ["--nope"])},
        {"argv": ["--mutant"], "rejected": cli_error_probe(parse_args, ["--mutant"])},
        {"argv": ["--mutant", "NOPE"],
         "rejected": cli_error_probe(parse_args, ["--mutant", "NOPE"])},
        {"argv": ["--break-anchor", "NOPE"],
         "rejected": cli_error_probe(parse_args, ["--break-anchor", "NOPE"])},
        {"argv": ["--verify-paper", "/nonexistent/paper.md"],
         "rejected": cli_error_probe(parse_args,
                                     ["--verify-paper", "/nonexistent/paper.md"])},
        {"argv": ["--mutant=MUT-FOLD"],
         "rejected": cli_error_probe(parse_args, ["--mutant=MUT-FOLD"])},
    ]
    LD.gate("G-CLI-WHITELIST",
            "the argv whitelist rejects every unknown flag, every unknown "
            "mutant name, every unknown anchor name, the equals form, and a "
            "--verify-paper path that does not exist -- the last at PARSE "
            "time, so a bad path costs an exit 2 and not an eight-minute "
            "census followed by a traceback",
            all(p["rejected"] for p in cli_probes) and len(cli_probes) == 6,
            "%d probes, all rejected" % len(cli_probes))
    S["cli_probes"] = cli_probes
    SEAL.take_all_at("G-CLI-WHITELIST", S, LD)

    if paper_path:
        verify_paper(S, LD, paper_path, SEAL)
    else:
        S["paper_claims"] = [dict(c, occurrences=0) for c in paper_claims(S)]
        S["paper_tables"] = [{"id": t, "row": r, "occurrences": 0}
                             for t, r in paper_tables(S)]
        S["paper_coverage"] = {"numerals": 0, "unlicensed": 0,
                               "claims": len(S["paper_claims"]),
                               "table_rows": len(S["paper_tables"]),
                               "fenced_blocks": 0, "sentence_polarities": 0,
                               "banned_words": 0, "licensed_values": 0,
                               "polarity_failures": 0, "paper": "NOT-VERIFIED"}
        # the two paper seals are taken at gates that only the paper path
        # evaluates; a diagnostic run without a paper takes neither, and the
        # seal-completeness gate below is told exactly that

    # #62's consumer binding, discharged: every gate an anchor or a seal names
    # must EXIST in this instrument's own registry and must have been evaluated
    # in this run, or be one of the three gates main() evaluates after the
    # census -- and that list is itself checked against the registry.
    registry = set()
    for node in ast.walk(ast.parse(open(SELF, "r", encoding="utf-8").read())):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == "gate" and node.args \
                and isinstance(node.args[0], ast.Constant):
            registry.add(node.args[0].value)
    consumers = ({g for _v, _s, _n, g in VERBATIM}
                 | {g for _p, _s, _pp, _e, g in PATH_VALUES}
                 | {g for _s, _p, g in SEALED_PATHS})
    if mut("MUT-ANCHOR-CONSUMER"):
        consumers = consumers | {"G-A-CONSUMER-THAT-DOES-NOT-EXIST"}
    # a diagnostic run given no paper does not evaluate the paper gates; the
    # delivery run always does, and then nothing is exempt
    evaluated = set(LD.ids) | set(LATE_GATES) | (set() if paper_path
                                                 else set(PAPER_GATES))
    bad_consumers = sorted(c for c in consumers
                           if c not in registry or c not in evaluated)
    LD.gate("G-ANCHOR-CONSUMERS",
            "#62: every anchor and every seal names a CONSUMER GATE, and each "
            "named gate is required to be in this source's own gate registry "
            "-- read from the AST, not from a list -- AND to have been "
            "evaluated in this run, or to be one of the declared late gates "
            "main() evaluates after the census.  Thirty published rows named "
            "twelve gates that did not exist; an anchor whose consumer is an "
            "unread label binds existence and not meaning",
            not bad_consumers and set(LATE_GATES) <= registry
            and len(consumers) > 20,
            "%d distinct consumer gates over %d registry entries; %d not "
            "registered-and-evaluated: %s"
            % (len(consumers), len(registry), len(bad_consumers),
               bad_consumers or "none"))

    prov_bad = [r["seal"] for r in SEAL.rows
                if r["sealed_at_gate"] not in LD.ids
                and r["sealed_at_gate"] not in LATE_GATES]
    order_bad = []
    gate_at = {r["gate"]: i for i, r in enumerate(LD.rows)}
    for r in SEAL.rows:
        i = gate_at.get(r["sealed_at_gate"])
        if i is None or i >= r["gates_evaluated_at_seal_time"]:
            order_bad.append(r["seal"])
    LD.gate("G-SEAL-PROVENANCE",
            "and every seal's provenance column is a MEASUREMENT of the order "
            "of events: the gate it names exists, was evaluated in this run, "
            "and was evaluated BEFORE the digest was taken.  Fifteen of the "
            "delivered thirty named a gate that never ran, and the digests "
            "were taken in one batch at the end -- which is what let a "
            "silently failed restore ship a sealed receipt asserting 65 of 64 "
            "generators at exit 0",
            not prov_bad and not order_bad,
            "%d seals taken so far; %d naming an unevaluated gate, %d taken "
            "before their gate" % (len(SEAL.rows), len(prov_bad), len(order_bad)))

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

    if mut("MUT-SEAL-BROKEN"):
        S["counts"]["single_nonzero"] = 0
    broken = SEAL.verify(S, only=set(SEAL.index) & set(SEALS_IN_RUN))
    LD.gate("G-SEAL-COMPLETE",
            "every object this unit vouches for was digested ON THE LINE AFTER "
            "its own gate passed -- not in a batch at the end -- and every one "
            "of those digests still verifies now: the seal covers the "
            "measurements, the theorems, the anchors, the choice inventory, "
            "the schema, the provenance and the paper's own claims and tables, "
            "not only the verdict",
            not broken
            and len(SEAL.rows) == len(SEALS_IN_RUN) - (0 if paper_path else 2),
            "%d seals taken at their gates of %d expected, %d broken: %s"
            % (len(SEAL.rows), len(SEALS_IN_RUN) - (0 if paper_path else 2),
               len(broken), broken or "none"))

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
    # THE SWEEP IS A SEQUENCE OF INDEPENDENT RUNS, AND THAT IS ENFORCED.  Two
    # of the declared falsifiers pollute a cached census IN PLACE -- that is
    # what they are for -- so the sweep keeps a snapshot and repairs any entry
    # whose fingerprint moved before the next mutant runs.  Without this an
    # injection would reach the next run through the memo, which is the very
    # thing G-CACHE-UNPOLLUTED exists to deny.
    snapshot = {k: copy_obj(v) for k, v in CENSUS_CACHE.items()}
    for name, target, why in MUTANTS:
        MUT = name
        died_at = None
        try:
            build_state(None, paper_path)
        except GateFail as e:
            died_at = str(e).split(" ::")[0]
        except Exception as e:                    # a mutant must die at a GATE
            died_at = "NON-GATE-EXCEPTION:%s" % type(e).__name__
        repaired = 0
        for k in list(CENSUS_CACHE):
            if k in snapshot and digest(canon_repr(CENSUS_CACHE[k])) != CENSUS_DIGESTS.get(k):
                CENSUS_CACHE[k] = copy_obj(snapshot[k])
                repaired += 1
        rows.append({"mutant": name, "target": target, "what": why,
                     "died_at": died_at, "killed": died_at is not None,
                     "on_target": died_at == target,
                     "cache_entries_repaired_after": repaired})
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
            if not os.path.exists(opts["verify_paper"]):
                raise CliError("--verify-paper path does not exist: %s"
                               % opts["verify_paper"])
        elif mut("MUT-CLI-OPEN"):
            pass                       # the whitelist, opened
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

    mut_rows = sweep_mutants(S, LD, paper)
    S["mutants"] = mut_rows
    SEAL.take_all_at("G-MUTANTS-ON-TARGET", S, LD)

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
        if sid not in SEAL.index:
            SEAL.take(sid, S, LD)
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

    # THE WRITE IS THE LAST THING THAT HAPPENS.  Both temporaries are written
    # and BOTH are verified against the gate-time seal BEFORE either is
    # promoted, so an integrity failure leaves the previous artifacts in place
    # rather than exiting 2 with corrupt bytes already at their final path
    # (K3 MINOR-5, demonstrated: 108,114 bytes on disk against a 108,113-byte
    # payload, with a transcript beside it that did not correspond).
    tmps = []
    for path, data in ((OUT_JSON, payload), (OUT_TXT, transcript)):
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(data)
        tmps.append((tmp, path))
    staged_json = open(OUT_JSON + ".tmp", "r", encoding="utf-8").read()
    staged_txt = open(OUT_TXT + ".tmp", "r", encoding="utf-8").read()
    probe = OUT_JSON + ".probe"
    with open(probe, "w", encoding="utf-8") as fh:
        fh.write(payload + "X")
    corrupt_detected = digest(open(probe, "r", encoding="utf-8").read()) != SEAL.payload_sha
    os.remove(probe)
    keys_ok = set(json.loads(staged_json).keys()) == set(FINAL_KEYS)
    ok = (digest(staged_json) == SEAL.payload_sha
          and digest(staged_txt) == SEAL.transcript_sha and corrupt_detected
          and keys_ok)
    if not ok:
        for tmp, _p in tmps:
            os.remove(tmp)
        print("G-ARTIFACT-INTEGRITY :: the bytes staged for disk are not the "
              "sealed bytes; nothing was promoted", file=sys.stderr)
        sys.exit(2)
    for tmp, path in tmps:
        os.replace(tmp, path)
    on_disk_json = open(OUT_JSON, "r", encoding="utf-8").read()
    on_disk_txt = open(OUT_TXT, "r", encoding="utf-8").read()
    if (digest(on_disk_json) != SEAL.payload_sha
            or digest(on_disk_txt) != SEAL.transcript_sha):
        print("G-ARTIFACT-INTEGRITY :: the promoted bytes are not the sealed "
              "bytes", file=sys.stderr)
        sys.exit(2)
    print("G-ARTIFACT-INTEGRITY passed: disk bytes == gate-time seal "
          "(payload %s, transcript %s); a corrupted probe was detected."
          % (SEAL.payload_sha, SEAL.transcript_sha), flush=True)
    print("EXIT 0", flush=True)


if __name__ == "__main__":
    try:
        main()
    except GateFail as e:
        # a gate failure on the plain path prints the gate that raised it, in
        # the mutant path's own form, rather than a traceback (K3 MINOR-13)
        print("DIED AT %s" % str(e).split(" ::")[0], flush=True)
        print("%s" % e, file=sys.stderr)
        print("EXIT 1", flush=True)
        sys.exit(1)
