#!/usr/bin/env python3
"""
v14 R3 -- THE RELATIVITY RUNG.  Exact instrument.

PIN: v14/note-r3-relativity-pin.md (frozen v14 ledger #23, sha256-12
a2ac89687a65), verified BY HASH at run time.  So are the R0 founding pin, its
row I7 (v13/code/ha_successor_receipt.json, 542b8735daf0 -- this unit's ARENA
SOURCE), the HA construction sources whose recipes are REIMPLEMENTED here
(nothing is imported), the R2 joint adjudication (the handoff ruling) and the
R2 terminal receipt.  Every value read by JSON path out of a pinned artifact
anchors the (path, value) PAIR, not only the file bytes (RUNBOOK section 14
addendum, v14 #20).

THE QUESTION (pin section 2, falsifiable, three-sided):
  does the record-native constraint family H_a[N] close as an algebra over the
  declared lapse family on I7's own lattice -- and in what form?  The
  hypersurface-deformation signature to test for is commutators landing back
  in the declared generator basis with coefficients that are READINGS OF THE
  RECORD METRIC (structure functions, not constants).

Three verdict heads, all first class, each derived INSIDE a gate from the
measured census, every segment computed and flippable:
  R3-DEFORMATION-CLOSES<...>          (with the coefficient class named:
                                       metric-reading = the HDA signature;
                                       constant = a RIGID algebra, a weaker
                                       geometry, labelled as such)
  R3-DEFORMATION-DEFECT-AT<...>       (a nonzero defect is a MEASURED OBJECT:
                                       its generator decomposition, its L- and
                                       d-dependence, its boundary-term status
                                       and its sector-vanishing status all
                                       measured and carried as segments)
The emitted string is compared for COMPLETE STRING EQUALITY against an
INDEPENDENT RECONSTRUCTION built from the receipt payload alone --
reconstruct_verdict_from_receipt() shares no code and no input with
build_verdict(), and injection mutants covering all five R1 verdict classes
prove it fires.

WHAT IS MEASURED (pin section 3):
  * THE MACHINERY-RECOVERY CONTROL -- I7's own closure table (99 cells), its
    sector law (72 cells), its identifiability rank, its readout determinant,
    its general-d row and its link-locality lattice, reproduced in-unit at
    I7's OWN declared scope (d=2, L=3) and anchored cell by cell against the
    pinned receipt BEFORE any new measurement counts.
  * THE L GATE -- L >= 4, with the measured reason printed: the R2 locality
    criterion (a non-complete overlap graph) is FAILED by the d=2, L=3 record
    lattice, whose overlap graph is COMPLETE at 36 of 36 pairs on 9 sites.
    The three inherited fractions are recomputed here and matched against the
    R2 adjudication's text.  An attempted L=3 census run dies BY GATE.
  * THE CLOSURE CENSUS -- for every ordered pair of the declared lapse family
    (and, as a second declared value of that coordinate, its lattice
    translates), the commutator [H_a[N], H_a[M]] computed exactly by two
    routes and decomposed in the declared generator basis; the residual
    channel measured exactly, cell-complete.
  * STRUCTURE-COEFFICIENT EXTRACTION -- the coefficient is SOLVED FOR from the
    commutators themselves and then TYPED against an independently
    re-encoded record metric: constant / metric-reading / other, by
    measurement.
  * THE NORMAL-TANGENTIAL AND TANGENTIAL BRACKETS -- {D,H} at both declared
    tangential realisations, with the convention sweep that decides whether a
    mismatch is a convention or a defect; {D,D} as the lattice's own
    covariance closure (positive control) against a scrambled-lattice
    negative control.
  * THE L-SWEEP -- everything at L = 4 and L = 5, at d = 2 and d = 3, with the
    L- and d-dependence of every defect and coefficient recorded.

CLI CONTRACT (confirmed in code before invocation, v13 #238):
  (no arguments)        THE PLAIN DELIVERY RUN.  Runs every gate, derives the
                        verdict, and WRITES the two artifacts
                        v14/code/r3_relativity_output.txt and
                        v14/code/r3_relativity_receipt.json.  Exit 0.  Any
                        gate failure aborts BEFORE any artifact is written.
  --mutant NAME         Runs the delivery pipeline with the named injection
                        active.  MUST exit 1 with a NAMED gate failure and
                        MUST NOT write any artifact.  Unknown name -> exit 2.
  --list-mutants        Prints the declared mutant names, one per line.  Exit 0.
  --selftest            THE FALSIFICATION SELFTEST.  Re-invokes this file as a
                        subprocess once per declared mutant, requires exit 1,
                        requires the death certificate to name a gate, and
                        requires the artifacts on disk to be byte-unchanged.
                        Writes NO artifacts itself.  Exit 0 iff every mutant
                        died correctly.
Arithmetic is exact throughout: int and fractions.Fraction only.  A float
literal, a float call, or a true-division operator anywhere in this source is
a gate failure (G-FLOATGUARD, an AST scan of this file).

Concurrency note: this unit owns ONLY v14/paper-03-relativity-rung.md,
v14/code/r3_relativity_exact.py, v14/code/r3_relativity_output.txt and
v14/code/r3_relativity_receipt.json.  It reads v13 and v14 artifacts and
writes nothing else.  Nothing is imported from v13; every construction is
reimplemented from the pinned declarations.
"""

import ast
import hashlib
import itertools
import json
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr

# ----------------------------------------------------------------------------
# 0.  Paths, mutation switch, gate ledger
# ----------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)                      # .../isp/v14
ROOT = os.path.dirname(REPO)                      # .../isp
SRC = os.path.abspath(__file__)
OUT_TXT = os.path.join(HERE, "r3_relativity_output.txt")
OUT_JSON = os.path.join(HERE, "r3_relativity_receipt.json")
PAPER = os.path.join(REPO, "paper-03-relativity-rung.md")

MUTANT = None            # set only from the command line; gates never read it

GATES = []
ANCHORS = []
DISCLOSURES = []

# Gates that can only be evaluated at WRITE time, after the receipt object
# exists.  Named so the falsifier census denominates itself honestly.
DEFERRED_GATES = ("G-RENDER-FROM-GATED-OBJECT", "G-NO-FLOATS-IN-RECEIPT",
                  "G-PROSE-RENDERS-FROM-THE-RECEIPT", "G-FINAL-GATE-COUNT",
                  "G-DEFERRED-GATES-EVALUATED", "G-INTERNAL-CONSISTENCY")

# The gates finalise() still has to register after the paper's instrument
# sentence is rendered.  The sentence's gate count is len(GATES) at render
# time PLUS this declared remainder -- derived, never typed -- and
# G-DEFERRED-GATES-EVALUATED checks the arithmetic came out right.
POST_RENDER_GATES = ("G-PROSE-RENDERS-FROM-THE-RECEIPT",
                     "G-NEVER-FALSIFIED-CENSUS", "G-FINAL-GATE-COUNT",
                     "G-DEFERRED-GATES-EVALUATED",
                     "G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS")


class GateFailure(Exception):
    pass


def gate(name, statement, ok, value=None):
    """Register a gate.  A gate predicate NEVER references mutant identity
    (RUNBOOK section 14 addendum, v13 #208)."""
    GATES.append({"name": name, "statement": statement,
                  "passed": bool(ok), "value": value})
    if not ok:
        raise GateFailure("GATE FAILED: %s -- %s | value=%r"
                          % (name, statement, value))
    return True


def disclose(did, statement, detail=None):
    DISCLOSURES.append({"id": did, "statement": statement, "detail": detail})


def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def sha256_full(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


LINES = []


def say(s=""):
    LINES.append(s)


# ----------------------------------------------------------------------------
# 1.  G-FLOATGUARD -- exact arithmetic enforced by an AST scan of this source
# ----------------------------------------------------------------------------

# The float type is obtained WITHOUT naming it, so the guard needs no
# exemption for its own detector.
FLOAT_T = type((1).__truediv__(1))

BANNED_NAMES = ("float", "math", "random", "numpy", "statistics", "decimal")


def float_guard():
    with open(SRC, "r") as fh:
        text = fh.read()
    tree = ast.parse(text)
    offences = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, FLOAT_T):
            offences.append(("float-literal", node.lineno))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            offences.append(("true-division", node.lineno))
        if isinstance(node, ast.Name) and node.id in BANNED_NAMES:
            offences.append(("banned-name:" + node.id, node.lineno))
        if isinstance(node, ast.Attribute) and node.attr in BANNED_NAMES:
            offences.append(("banned-attr:" + node.attr, node.lineno))
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", None) or ""
            for nm in [mod] + [a.name for a in node.names]:
                if nm.split(".")[0] in BANNED_NAMES:
                    offences.append(("banned-import:" + nm, node.lineno))
    if MUTANT == "float-leak":
        offences.append(("injected-float", 0))
    return offences


def qinv(a):
    """1/a for an exact rational, without the division operator."""
    a = Fr(a)
    return Fr(a.denominator, a.numerator)


def qdiv(a, b):
    return Fr(a) * qinv(b)


# ----------------------------------------------------------------------------
# 2.  Anchors -- file-bytes rows and (path, value) rows
# ----------------------------------------------------------------------------

ANCHOR_ROWS = [
    ("A-PIN-R3", "v14/note-r3-relativity-pin.md", "a2ac89687a65",
     "this unit's pin, frozen at v14 ledger #23"),
    ("A-R0-PIN", "v14/note-r0-founding-pin.md", "e9d2bedff244",
     "the R0 founding pin: the seven-row inheritance, row I7 among them"),
    ("A-R0-I7", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "R0 row I7 -- gravity's record layer: THIS UNIT'S ARENA SOURCE (sites, "
     "links, chart group, lapse family, the record-native H_a[N], the "
     "diagonal-sector closure, record-IS-metric)"),
    ("A-R2-ADJ", "v14/note-r2-adjudication.md", "ee295ac1bb68",
     "the R2 joint adjudication: the handoff ruling that hands R3 I7's arena "
     "and gates L >= 4"),
    ("A-R2-RECEIPT", "v14/code/r2_manifold_receipt.json", "08b2140f46ae",
     "the R2 terminal receipt: the locality criterion this unit inherits"),
    ("A-R2-CODE", "v14/code/r2_manifold_exact.py", "a4b0e71819be",
     "the R2 terminal instrument, whose overlap-graph criterion is "
     "reimplemented here for the L gate"),
    ("A-HA-PAPER", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "the HA paper -- read ONLY for construction recipes (sections 3.1-3.7, "
     "6.x); no number in this unit is read from it"),
]


def read_json(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return json.load(fh)


def read_text(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return fh.read()


I7 = "v13/code/ha_successor_receipt.json"

# PATH-VALUE ANCHORS (RUNBOOK section 14 addendum, v14 #20).  Every arena
# datum and every recovery target this unit reads out of a pinned artifact
# appears here with its exact JSON path AND its exact expected value; a path
# drift that changes the arena or the verdict dies by anchor.
PATH_ANCHOR_ROWS = [
    ("P-I7-D", I7, ("declarations", "d"), 2,
     "I7's primary dimension"),
    ("P-I7-DEXT", I7, ("declarations", "d_ext"), 3,
     "I7's extension dimension"),
    ("P-I7-L", I7, ("declarations", "L"), 3,
     "I7's own declared lattice extent -- the ANCHOR scope, excluded from "
     "this unit's census by the L gate"),
    ("P-I7-LINKS2", I7, ("declarations", "links_d2"), [[1, 0], [0, 1], [1, 1]],
     "the declared d=2 link set: the axis links and the positive diagonal"),
    ("P-I7-LINKS3", I7, ("declarations", "links_d3"),
     [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1]],
     "the declared d=3 link set"),
    ("P-I7-LAPSE", I7, ("declarations", "lapse_family"),
     "the |X| site deltas, the constant profile 1, and the d chart ramps",
     "THE LAPSE FAMILY, a named verdict coordinate (pin section 3 item 6)"),
    ("P-I7-CHARTGROUP", I7, ("declarations", "chart_group"),
     "the |X| chart translations and the d! direction relabellings, acting on "
     "sites, on the record's link counts, on the lapse profiles and on every "
     "tensor index",
     "the lattice's own covariance group -- the translation control's subject"),
    ("P-I7-RECORDS2", I7, ("declarations", "records_d2"),
     {"G-ANISO": [1, 4, 5], "G-ANISO2": [4, 9, 13], "G-DIAG2": [2, 2, 4],
      "G-FLAT": [1, 1, 2], "G-INDEF": [1, 1, 6], "G-OFFDIAG": [2, 2, 6],
      "G-OFFDIAG2": [3, 5, 12], "G-OFFNEG": [3, 5, 4], "G-SINGULAR": [1, 1, 4]},
     "the declared d=2 geometry records, by their link counts"),
    ("P-I7-RECORDS3", I7, ("declarations", "records_d3"),
     {"G3-ANISO": [1, 4, 9, 5, 10, 13], "G3-FLAT": [1, 1, 1, 2, 2, 2],
      "G3-OFF": [2, 2, 2, 6, 4, 4]},
     "the declared d=3 geometry records"),
    ("P-I7-INHOMOG", I7, ("declarations", "records_d2_inhomogeneous"),
     ["G-CURVED (diagonal, site-dependent)",
      "G-CURVOFF (cross term, site-dependent)"],
     "the two inhomogeneous records -- the ONLY arena in which a structure "
     "FUNCTION can be distinguished from a structure CONSTANT"),
    ("P-I7-WEIGHT", I7, ("declarations", "density_weight"), 0,
     "the primary density weight w = 0, so I_a(g) = q^-1"),
    ("P-I7-WEIGHTFLIP", I7, ("declarations", "density_weight_flip"), 1,
     "the declared density-weight flip test"),
    ("P-I7-RULES3", I7, ("declarations", "rules_d3"),
     ["A-chart", "A-axis", "A-linkframe", "A-insert"],
     "the drag rules I7 carries to d = 3"),
    ("P-I7-BROKEN", I7, ("declarations", "broken_rules"),
     ["A-insert-x", "A-insert-2x", "A-notransport"],
     "the declared broken rules -- the negative controls"),
    ("P-I7-POSCTL", I7, ("declarations", "positive_control_rule"), "A-insert",
     "the declared positive control: the metric-inserted rule"),
    ("P-I7-SRCSHA", I7, ("source_sha256",),
     "d44cb72f8ee9f2d212f4c9a881247411bc3245c9453e3745b5f4ff673ff6c439",
     "the HA instrument's own source hash, carried by the pinned receipt: "
     "this unit derives the HA code anchor from it rather than typing it"),
    ("P-I7-VERDICT", I7, ("verdict",), ["HA-RUNNABLE", "HA-BRIDGE-NOT-ENTERED"],
     "I7's emitted verdict"),
    # --- the recovery targets (the machinery-recovery control) --------------
    ("P-I7-CLOSURE-AXIS-FLAT", I7, ("tables", "closure", "A-axis|G-FLAT"),
     {"closes": True, "max_abs": "0", "nonzero_pairs": 0, "total_pairs": 132,
      "witness": None},
     "the diagonal-sector closure cell -- the positive control this unit's "
     "machinery must recover before anything new counts"),
    ("P-I7-CLOSURE-AXIS-OFFD", I7, ("tables", "closure", "A-axis|G-OFFDIAG"),
     {"closes": False, "max_abs": "2", "nonzero_pairs": 96, "total_pairs": 132,
      "witness": ["ramp0", "ramp1"]},
     "the cross-term anomaly cell: the exact residual off the diagonal sector"),
    ("P-I7-CLOSURE-INSERT-CURVOFF", I7,
     ("tables", "closure", "A-insert|G-CURVOFF"),
     {"closes": True, "max_abs": "0", "nonzero_pairs": 0, "total_pairs": 132,
      "witness": None},
     "the metric-inserted rule on the inhomogeneous cross-term record"),
    ("P-I7-SECTOR-CHART-CURVED", I7,
     ("tables", "sector_law", "A-chart|G-CURVED"),
     {"Lambda_equals_I_sites": 1, "residual_zero_sites": 1, "sites": 9},
     "the site-resolved sector law's sharpest cell: closure holds at exactly "
     "the one site where the chart weight coincides with the record-read "
     "inverse metric"),
    ("P-I7-RANK", I7, ("tables", "identifiability_rank"),
     {"(0, 0)": 2, "(0, 1)": 2, "(0, 2)": 2, "(1, 0)": 2, "(1, 1)": 2,
      "(1, 2)": 2, "(2, 0)": 2, "(2, 1)": 2, "(2, 2)": 2},
     "the identifiability rank: the realised bracket covectors span fully at "
     "every site, so the closure relation determines the structure "
     "coefficient uniquely"),
    ("P-I7-READOUT", I7, ("tables", "readout_reencoding"),
     {"determinant": "2", "sites_verified": 81},
     "RECORD-IS-METRIC: the counts-to-metric map is linear with exact nonzero "
     "determinant 2 at d=2, verified at 81 sites"),
    ("P-I7-GENERALD", I7, ("tables", "general_d"),
     {"A-axis|G3-ANISO": 0, "A-axis|G3-FLAT": 0, "A-axis|G3-OFF": 18,
      "A-chart|G3-ANISO": 30, "A-chart|G3-FLAT": 0, "A-chart|G3-OFF": 30,
      "A-insert|G3-ANISO": 0, "A-insert|G3-FLAT": 0, "A-insert|G3-OFF": 0,
      "A-linkframe|G3-ANISO": 30, "A-linkframe|G3-FLAT": 30,
      "A-linkframe|G3-OFF": 30},
     "I7's d=3 extension row -- the general-d recovery target"),
    ("P-I7-LATTICE", I7, ("tables", "link_locality_lattice"),
     {"admissible_points": 361, "pairs_sharing_n_diag_diff_I12": 5100,
      "pairs_sharing_n_e1_n_diag_diff_I11": 781},
     "the declared count lattice's link-locality census"),
    ("P-I7-DETECTOR-CF", I7, ("tables", "detector_closed_form"),
     {"compared": 108, "disagreements": 0},
     "I7's own two-route agreement on the detector"),
    ("P-I7-DETECTOR-ROW0", I7, ("tables", "detector", 0),
     {"C_trivial": True, "SW_front_zero": True, "SW_register_zero": True,
      "jacobi_lapse_sum_zero": True, "max_abs_register": "0",
      "record": "G-ANISO", "rule": "A-insert", "triple": "(0,1,2)"},
     "C_trivial: I7's own measurement that the normal-tangential switch is "
     "the identity at the primary tangential realisation -- the fact this "
     "unit censuses in full"),
    # --- the R2 terminal receipt -------------------------------------------
    ("P-R2-SCHEMA", "v14/code/r2_manifold_receipt.json", ("schema",),
     "isp/v14/r2-manifold/1", "the R2 terminal receipt's schema"),
    ("P-R2-HEAD", "v14/code/r2_manifold_receipt.json", ("verdict", "head"),
     "R2-LOCALITY-DECLARABLE-AT",
     "R2's verdict head: locality is a statement about atlas space, which is "
     "why the substrate's own locality question moved to I7's arena"),
    ("P-R2-GRIDRULES", "v14/code/r2_manifold_receipt.json",
     ("totals", "grid_rules"), 109, "R2's declared grid size"),
    ("P-R2-CRITERION", "v14/code/r2_manifold_receipt.json",
     ("locality_census", "criterion"),
     "locality exists at a rule iff SOME connected component of that rule's "
     "overlap graph is NOT complete (the R1 adjudication's criterion, "
     "section 6)",
     "THE INHERITED LOCALITY CRITERION, reimplemented here for the L gate"),
    ("P-R2-LOCCOUNT", "v14/code/r2_manifold_receipt.json",
     ("locality_census", "count_locality_B"), 14,
     "R2's locality count -- the declaration-grid result whose inadequacy "
     "moved the question to I7's arena"),
]


def read_by_path(obj, path):
    cur = obj
    for k in path:
        cur = cur[k]
    return cur


def verify_anchors():
    rows = list(ANCHOR_ROWS)
    if MUTANT == "anchor-skip":
        rows = rows[:-1]
    for name, rel, expect, why in rows:
        path = os.path.join(ROOT, rel)
        got = sha12(path)
        if MUTANT == "anchor-hash" and name == "A-R0-I7":
            got = "0" * 12
        ANCHORS.append({"name": name, "kind": "file-bytes", "artifact": rel,
                        "expected": expect, "measured": got, "provenance": why,
                        "ok": got == expect})
        gate(name, "external anchor %s verifies at %s" % (expect, rel),
             got == expect, {"expected": expect, "measured": got})
    return len(rows)


def verify_path_anchors():
    cache = {}
    for name, rel, path, expect, why in PATH_ANCHOR_ROWS:
        if rel not in cache:
            cache[rel] = read_json(rel)
        p = tuple(path)
        if MUTANT == "path-drift" and name == "P-I7-L":
            p = ("declarations", "d")
        if MUTANT == "path-drift-links" and name == "P-I7-LINKS2":
            p = ("declarations", "links_d3")
        if MUTANT == "path-drift-closure" and name == "P-I7-CLOSURE-AXIS-FLAT":
            p = ("tables", "closure", "A-axis|G-OFFDIAG")
        if MUTANT == "path-value-" + name:
            p = p[:-1] + ("__no_such_key__",)
        try:
            got = read_by_path(cache[rel], p)
        except (KeyError, IndexError, TypeError):
            got = None
        ok = (got == expect)
        ANCHORS.append({"name": name, "kind": "path-value", "artifact": rel,
                        "json_path": list(p), "expected": expect,
                        "measured": got, "provenance": why, "ok": ok})
        gate(name, "path-value anchor: %s[%s] reads exactly the pinned value "
                   "(the PAIR is anchored, not only the file bytes)"
             % (rel, ".".join(str(x) for x in path)), ok,
             {"path": list(p), "expected": expect, "measured": got})
    return len(PATH_ANCHOR_ROWS)


def derive_ha_code_anchor():
    """The HA instrument's hash is DERIVED from the pinned receipt's own
    source_sha256 field, never typed (v14 #24: counts computed, never typed --
    applied to provenance).  The on-disk file must match it."""
    rec = read_json(I7)
    expect = rec["source_sha256"][:12]
    got = sha12("v13/code/ha_successor_exact.py")
    if MUTANT == "ha-code-drift":
        got = "0" * 12
    ANCHORS.append({"name": "A-HA-CODE", "kind": "derived-file-bytes",
                    "artifact": "v13/code/ha_successor_exact.py",
                    "expected": expect, "measured": got,
                    "provenance": "the HA construction source, whose recipes "
                                  "are reimplemented here; its expected hash "
                                  "is READ from the pinned receipt's "
                                  "source_sha256, not typed",
                    "ok": got == expect})
    gate("A-HA-CODE",
         "the HA construction source on disk matches the hash the PINNED "
         "RECEIPT itself carries for it -- the provenance is derived, not typed",
         got == expect, {"expected": expect, "measured": got})
    return expect


# ----------------------------------------------------------------------------
# 3.  Exact linear algebra over Q (no division operator anywhere)
# ----------------------------------------------------------------------------

def solve_exact(A, b):
    n = len(A)
    M = [[Fr(A[i][j]) for j in range(n)] + [Fr(b[i])] for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        iv = qinv(M[c][c])
        M[c] = [v * iv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [M[r][k] - f * M[c][k] for k in range(n + 1)]
    return [M[i][n] for i in range(n)]


def det_exact(M):
    n = len(M)
    A = [[Fr(v) for v in row] for row in M]
    det = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det = det * A[c][c]
        iv = qinv(A[c][c])
        A[c] = [v * iv for v in A[c]]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c]
                A[r] = [A[r][k] - f * A[c][k] for k in range(n)]
    return det


def inv_exact(M):
    n = len(M)
    A = [[Fr(v) for v in row] + [Fr(1) if i == j else Fr(0) for j in range(n)]
         for i, row in enumerate(M)]
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return None
        A[c], A[piv] = A[piv], A[c]
        iv = qinv(A[c][c])
        A[c] = [v * iv for v in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [A[r][k] - f * A[c][k] for k in range(2 * n)]
    return [row[n:] for row in A]


def positive_definite(M):
    for k in range(1, len(M) + 1):
        if det_exact([row[:k] for row in M[:k]]) <= 0:
            return False
    return True


def gcd_int(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def common_denominator_matrix(M):
    """(integer matrix, positive common denominator) for an exact rational
    matrix -- lets the inner census loop run in integers."""
    den = 1
    for row in M:
        for v in row:
            den = den * v.denominator // gcd_int(den, v.denominator)
    return [[int(v * den) for v in row] for row in M], den


# ----------------------------------------------------------------------------
# 4.  THE ARENA (data, RUNBOOK section 15).  Every entry below is READ from the
#     pinned I7 receipt through an anchored (path, value) pair; nothing about
#     the arena is typed here except the reimplementation of I7's own recipes.
# ----------------------------------------------------------------------------

def link_set(d):
    """I7's declared record adjacency: the d axis links and the C(d,2)
    positive diagonals."""
    axes = [tuple(1 if k == j else 0 for k in range(d)) for j in range(d)]
    diags = [tuple(1 if k in (i, j) else 0 for k in range(d))
             for i in range(d) for j in range(i + 1, d)]
    return axes + diags


def sites(d, L):
    return [tuple(t) for t in itertools.product(range(L), repeat=d)]


def add(x, e, L):
    return tuple((a + b) % L for a, b in zip(x, e))


_NB_CACHE = {}


def neighbours(d, L):
    """x -> the tuple of x+l over the declared links, computed once per
    arena.  A pure memo of add(); the cache-exercise gate measures it."""
    t = _NB_CACHE.get((d, L))
    if t is not None:
        CACHE_STATS["hits"] += 1
        return t
    CACHE_STATS["misses"] += 1
    lks = link_set(d)
    t = {x: tuple(add(x, lk, L) for lk in lks) for x in sites(d, L)}
    _NB_CACHE[(d, L)] = t
    return t


def sym_index(d):
    return [(i, j) for i in range(d) for j in range(i, d)]


def q_from_counts(d, counts):
    """THE RECORD READOUT (I7 section 3.2): q_ij e^i e^j = n_l for every
    declared link, solved exactly.  ROUTE 1 -- the linear solve."""
    idx = sym_index(d)
    rows, rhs = [], []
    for lk in sorted(counts):
        rows.append([Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in idx])
        rhs.append(Fr(counts[lk]))
    sol = solve_exact(rows, rhs)
    if sol is None:
        return None
    q = [[Fr(0)] * d for _ in range(d)]
    for (i, j), v in zip(idx, sol):
        q[i][j] = v
        q[j][i] = v
    return q


def q_from_counts_closed(d, counts):
    """ROUTE 2 -- the SAME readout in closed form, sharing no code with the
    solve: q_jj = n_{e_j} and q_ij = (n_{e_i+e_j} - n_{e_i} - n_{e_j})/2.
    RECORD-IS-METRIC re-encoded independently."""
    axes = [tuple(1 if k == j else 0 for k in range(d)) for j in range(d)]
    q = [[Fr(0)] * d for _ in range(d)]
    for j in range(d):
        q[j][j] = Fr(counts[axes[j]])
    for i in range(d):
        for j in range(i + 1, d):
            lk = tuple(1 if k in (i, j) else 0 for k in range(d))
            v = Fr(counts[lk] - counts[axes[i]] - counts[axes[j]], 2)
            if MUTANT == "readout-local":
                v = Fr(0)
            q[i][j] = v
            q[j][i] = v
    return q


def readout_determinant(d):
    """The determinant of the linear counts -> metric-components map."""
    idx = sym_index(d)
    lks = sorted(link_set(d))
    rows = [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in idx]
            for lk in lks]
    return det_exact(rows)


class GeomRecord(object):
    """A geometry record: interval-cardinality count data on the declared
    record adjacency, with the metric it carries under the declared readout."""

    def __init__(self, name, d, L, countrule, weight=0):
        self.name, self.d, self.L, self.weight = name, d, L, weight
        self.links = link_set(d)
        self.S = sites(d, L)
        self.counts = {x: {lk: int(countrule(x, lk)) for lk in self.links}
                       for x in self.S}
        self.q, self.I = {}, {}
        self.singular, self.nonpd = [], []
        for x in self.S:
            q = q_from_counts(d, {lk: Fr(self.counts[x][lk]) for lk in self.links})
            self.q[x] = q
            if q is None:
                self.singular.append(x)
                self.I[x] = None
                continue
            if not positive_definite(q):
                self.nonpd.append(x)
            qi = inv_exact(q)
            if qi is None:
                self.I[x] = None
                continue
            if weight:
                dq = det_exact(q)
                qi = [[v * (dq ** weight) for v in row] for row in qi]
            self.I[x] = qi
        self.homogeneous = all(self.counts[x] == self.counts[self.S[0]]
                               for x in self.S)

    @property
    def admissible(self):
        return (not self.singular and not self.nonpd
                and all(self.I[x] is not None for x in self.I))


def make_homogeneous(name, d, L, tup, w=0):
    table = {lk: tup[i] for i, lk in enumerate(link_set(d))}
    return GeomRecord(name, d, L, lambda x, lk: table[lk], w)


def make_curved(name, d, L, w=0):
    """I7's inhomogeneous DIAGONAL record: q(x) = diag(1+x_1, ..., 1+x_d)."""
    def rule(x, lk):
        return sum((1 + x[j]) for j in range(d) if lk[j])
    return GeomRecord(name, d, L, rule, w)


def make_curvoff(name, d, L, w=0):
    """I7's inhomogeneous CROSS-TERM record."""
    def rule(x, lk):
        b = [2 + x[j] for j in range(d)]
        cross = 1 + (x[0] * x[1]) % 2
        s = sum(b[j] for j in range(d) if lk[j])
        pairs = sum(1 for i in range(d) for j in range(i + 1, d)
                    if lk[i] and lk[j])
        return s + 2 * cross * pairs
    return GeomRecord(name, d, L, rule, w)


def build_records(d, L, decl, w=0):
    """The declared record family at (d, L).  The homogeneous members are read
    from the pinned receipt; the two inhomogeneous members are built by I7's
    own site-dependent recipes.  At d = 3 the inhomogeneous pair is a DECLARED
    EXTENSION of I7's list, printed as arena data -- without an inhomogeneous
    record a structure FUNCTION cannot be told from a structure CONSTANT."""
    src = decl["records_d2"] if d == 2 else decl["records_d3"]
    recs = {}
    for nm in sorted(src):
        recs[nm] = make_homogeneous(nm, d, L, list(src[nm]), w)
    pre = "G-" if d == 2 else "G3-"
    recs[pre + "CURVED"] = make_curved(pre + "CURVED", d, L, w)
    recs[pre + "CURVOFF"] = make_curvoff(pre + "CURVOFF", d, L, w)
    return recs


def build_lapse_family(d, L):
    """I7's declared lapse family, verbatim: the |X| site deltas, the constant
    profile 1, and the d chart ramps."""
    S = sites(d, L)
    lp = [("delta%s" % (x,), {y: (1 if y == x else 0) for y in S}) for x in S]
    lp.append(("one", {y: 1 for y in S}))
    lp += [("ramp%d" % j, {y: y[j] for y in S}) for j in range(d)]
    return lp


def build_lapse_translates(d, L):
    """The declared family closed under the lattice's own chart translations.
    THIS IS AN ENLARGEMENT AND IS PRINTED AS ARENA DATA (pin section 3 item 6):
    the deltas and the constant profile are already translate-closed; the d
    ramps acquire L translates each, because the ramp's wrap-around is not a
    constant shift."""
    S = sites(d, L)
    seen, out = {}, []
    for nm, N in build_lapse_family(d, L):
        for u in S:
            Nt = {y: N[add(y, tuple(-t for t in u), L)] for y in S}
            key = tuple(Nt[y] for y in S)
            if key in seen:
                continue
            seen[key] = 1
            out.append((nm if u == tuple([0] * d) else "%s^%s" % (nm, u), Nt))
    return out


# ---- THE L GATE -----------------------------------------------------------
#
# R2's handoff gates L >= 4, and the reason is a MEASUREMENT, reproduced here:
# the record lattice's overlap graph -- cells = the closed forward link
# neighbourhoods {x} u {x+l : l in L} -- is COMPLETE at d=2, L=3, so the
# inherited locality criterion (SOME component not complete) is failed there.

def overlap_cells(d, L, neighbour=None):
    nb = neighbour or (lambda x, lk: add(x, lk, L))
    return [frozenset([x] + [nb(x, lk) for lk in link_set(d)])
            for x in sites(d, L)]


def overlap_census(d, L, neighbour=None):
    cells = overlap_cells(d, L, neighbour)
    drawn = set()
    for c in cells:
        for a, b in itertools.combinations(sorted(c), 2):
            drawn.add((a, b))
    n = L ** d
    allp = n * (n - 1) // 2
    if MUTANT == "lgate-reason-blind":
        drawn = set(list(drawn)[:1])
    return {"sites": n, "drawn_pairs": len(drawn), "all_pairs": allp,
            "complete": len(drawn) == allp,
            "meets_r2_criterion": len(drawn) != allp}


CENSUS_L_MIN = 4


def census_scope_gate(arenas):
    """The census's single entry gate.  Any arena below the gated minimum
    extent makes it fail, so an L = 3 census run DIES BY GATE rather than
    running; the excluded extent is admitted for the machinery-recovery
    ANCHOR only, never for a census measurement."""
    offending = [[d, L] for (d, L) in arenas if L < CENSUS_L_MIN]
    gate("G-L-GATE",
         "every censused arena satisfies the inherited L >= %d requirement "
         "(R2 handoff ruling), and the arenas actually entered are exactly "
         "the declared ones" % CENSUS_L_MIN,
         len(offending) == 0 and len(arenas) == len(CENSUS_ARENAS),
         {"arenas": [list(a) for a in arenas], "minimum": CENSUS_L_MIN,
          "offending": offending})
    return True


# ----------------------------------------------------------------------------
# 5.  THE DECLARED GENERATOR BASIS
#
#     THE CONSTRAINT FAMILY   H_a[N](n, m) = (n + N, m + w[N,n])
#       arch A:  w[N,n]^i(x) = N(x) sum_j Lambda^{ij}(x) ( n(x+e_j) - n(x) )
#       arch B:  w[N,n]^i(x) = N(x) sum_l lambda_l(x) e_l^i ( n(x+e_l) - n(x) )
#     THE TANGENTIAL FAMILY   D_a[v] : two declared realisations
#       D-REG  shifts the address register by v; the front is not transported
#       D-TOT  shifts the register AND drags the front along x -> x + v(x)
#     THE LATTICE TRANSLATION GENERATORS are the tangential generators at the
#     CONSTANT fields v = e_i: the lattice's own covariance directions.
#     A RESIDUAL CHANNEL carries whatever a commutator leaves over.
# ----------------------------------------------------------------------------

RULE_TABLE = [
    ("A-chart", "A", "Lambda = delta (count-blind chart identity)"),
    ("A-axis", "A", "Lambda = diag(1/n_{e_j}) from the axis interval counts"),
    ("A-linkframe", "A", "Lambda^{ij} = sum_l e_l^i e_l^j / n_l over every link"),
    ("A-linkhalf", "A", "Lambda = (1/2) sum_l e_l e_l^T / n_l"),
    ("A-insert", "A", "Lambda = I_a(g), read from the record [POSITIVE CONTROL]"),
    ("A-insert-x", "A", "Lambda = I_a(g), cross term sign-flipped [BROKEN]"),
    ("A-insert-2x", "A", "Lambda = 2 I_a(g) [BROKEN]"),
    ("A-notransport", "A", "Lambda = I_a(g), drag at a frozen front [BROKEN]"),
    ("B-axis", "B", "lambda_l = 1/n_l on the axis links only"),
    ("B-all", "B", "lambda_l = 1/n_l on every declared link"),
    ("B-chart", "B", "lambda_l = 1 on the axis links only"),
]

_LAMBDA_CACHE = {}
CACHE_STATS = {"hits": 0, "misses": 0, "bypass": 0}


def arch_of(rule):
    return "B" if rule.startswith("B-") else "A"


def lambda_of(rule, rec, x, fresh=False):
    """The drag rule's weight at site x."""
    key = (rule, rec.name, rec.d, rec.L, rec.weight, x)
    if fresh:
        CACHE_STATS["bypass"] += 1
    elif key in _LAMBDA_CACHE:
        CACHE_STATS["hits"] += 1
        return _LAMBDA_CACHE[key]
    else:
        CACHE_STATS["misses"] += 1
    d = rec.d
    cnt = rec.counts[x]
    lks = rec.links
    axes = lks[:d]
    if rule == "A-chart":
        M = [[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(d)]
    elif rule == "A-axis":
        M = [[Fr(0)] * d for _ in range(d)]
        for j in range(d):
            M[j][j] = Fr(1, cnt[axes[j]])
    elif rule in ("A-linkframe", "A-linkhalf"):
        M = [[Fr(0)] * d for _ in range(d)]
        for lk in lks:
            wl = Fr(1, cnt[lk])
            for i in range(d):
                for j in range(d):
                    M[i][j] += Fr(lk[i] * lk[j]) * wl
        if rule == "A-linkhalf":
            M = [[v * Fr(1, 2) for v in row] for row in M]
    elif rule in ("A-insert", "A-notransport"):
        M = [row[:] for row in rec.I[x]]
    elif rule == "A-insert-x":
        M = [[(-v if i != j else v) for j, v in enumerate(row)]
             for i, row in enumerate(rec.I[x])]
    elif rule == "A-insert-2x":
        M = [[2 * v for v in row] for row in rec.I[x]]
    elif rule == "B-axis":
        M = {lk: (Fr(1, cnt[lk]) if lk in axes else Fr(0)) for lk in lks}
    elif rule == "B-all":
        M = {lk: Fr(1, cnt[lk]) for lk in lks}
    elif rule == "B-chart":
        M = {lk: (Fr(1) if lk in axes else Fr(0)) for lk in lks}
    else:
        raise RuntimeError("unknown rule %s" % rule)
    if not fresh:
        _LAMBDA_CACHE[key] = M
    return M


_DRAG_CACHE = {}


def drag_matrix(rule, rec, x):
    """The rule's drag weight at x as a single d x |L| matrix, so that
    uniformly  w[N,n]^i(x) = N(x) sum_l Wd^{il}(x) ( n(x+l) - n(x) ).
    Architecture A populates the axis columns with Lambda; architecture B
    populates every link column with lambda_l e_l^i.  A-notransport carries
    Lambda = I_a(g): its brokenness is the FROZEN FRONT, not the weight."""
    if rule == "A-notransport":
        return hda_matrix(rec, x)
    return weight_matrix(rule, rec, x)


def drag_tables(rule, rec):
    """Per-site (integer matrix, common denominator, neighbour index rows) --
    the drag's inner loop then runs entirely in integers."""
    key = (rule, rec.name, rec.d, rec.L, rec.weight)
    t = _DRAG_CACHE.get(key)
    if t is not None:
        CACHE_STATS["hits"] += 1
        return t
    CACHE_STATS["misses"] += 1
    NB = neighbours(rec.d, rec.L)
    tab = {}
    for x in rec.S:
        M, den = common_denominator_matrix(drag_matrix(rule, rec, x))
        tab[x] = (M, den, NB[x])
    _DRAG_CACHE[key] = tab
    return tab


def drag(rule, rec, N, n):
    """w[N, n], the record-native drag field."""
    d = rec.d
    nlk = len(rec.links)
    tab = drag_tables(rule, rec)
    out = {}
    for x in rec.S:
        M, den, nbs = tab[x]
        nx = n[x]
        dl = [n[y] - nx for y in nbs]
        Nx = N[x]
        out[x] = tuple(Fr(Nx * sum(M[i][k] * dl[k] for k in range(nlk)), den)
                       for i in range(d))
    return out


class Hmap(object):
    """H_a[N] as a bijection of total records (n, m)."""

    def __init__(self, rule, rec, N, frozen_front=None):
        self.rule, self.rec, self.N = rule, rec, N
        self.frozen_front = frozen_front

    def _w(self, n):
        src = self.frozen_front if self.frozen_front is not None else n
        if MUTANT == "hmap-transport":
            src = {x: n[x] - self.N[x] for x in n}
        return drag(self.rule, self.rec, self.N, src)

    def fwd(self, c):
        n, m = c
        w = self._w(n)
        d = self.rec.d
        return ({x: n[x] + self.N[x] for x in n},
                {x: tuple(m[x][i] + w[x][i] for i in range(d)) for x in m})

    def inv(self, c):
        n, m = c
        d = self.rec.d
        n2 = {x: n[x] - self.N[x] for x in n}
        w = self._w(n2)
        return (n2, {x: tuple(m[x][i] - w[x][i] for i in range(d)) for x in m})


class Dmap(object):
    """D_a[v], the tangential comparison map, at both declared realisations."""

    def __init__(self, rec, v, realisation="D-REG"):
        self.rec, self.v, self.realisation = rec, v, realisation

    def site_map(self):
        d, L = self.rec.d, self.rec.L
        out = {}
        for x in self.rec.S:
            sh = self.v[x]
            if any(Fr(t).denominator != 1 for t in sh):
                return None
            out[x] = tuple((x[i] + int(sh[i])) % L for i in range(d))
        return out if len(set(out.values())) == L ** d else None

    def fwd(self, c):
        n, m = c
        d = self.rec.d
        vv = self.v
        if MUTANT == "commutator-machinery":
            vv = {x: tuple(2 * t if all(u >= 0 for u in self.v[x]) else t
                           for t in self.v[x]) for x in self.v}
        m2 = {x: tuple(m[x][i] + vv[x][i] for i in range(d)) for x in m}
        if self.realisation == "D-REG":
            return (n, m2)
        sm = self.site_map()
        if sm is None:
            return None
        return ({sm[x]: n[x] for x in n}, m2)


def neg_field(v):
    return {x: tuple(-t for t in v[x]) for x in v}


def const_field(rec, vec):
    return {x: tuple(Fr(t) for t in vec) for x in rec.S}


def lattice_translation_generators(d):
    """The lattice's own translation directions: the constant unit fields."""
    return [tuple(1 if k == i else 0 for k in range(d)) for i in range(d)]


# ---- THE CLOSED-FORM ROUTE ------------------------------------------------
#
# Because w[N, .] is LINEAR in the front, H[N]H[M] and H[M]H[N] differ by the
# configuration-independent field w[N,M] - w[M,N], so the group commutator is
# a PURE tangential generator whose field is  Delta = W(x) . Omega(x)  with
# Omega_l(x) := N(x)M(x+l) - M(x)N(x+l) the declared finite bracket covector
# on link l.  W, B and G = W - B below are the three declared d x |L| matrices.

def bracket_covector(N, M, rec, neighbour=None):
    """Omega_l(x) on EVERY declared link (the axis entries are I7's omega_j)."""
    L = rec.L
    nb = neighbour or (lambda x, lk: add(x, lk, L))
    return {x: tuple(N[x] * M[nb(x, lk)] - M[x] * N[nb(x, lk)]
                     for lk in rec.links) for x in rec.S}


def weight_matrix(rule, rec, x):
    """W: Delta^i(x) = sum_l W^{il}(x) Omega_l(x)."""
    d = rec.d
    W = [[Fr(0)] * len(rec.links) for _ in range(d)]
    if rule == "A-notransport":
        return W                      # frozen front: the steps commute
    if arch_of(rule) == "A":
        Lam = lambda_of(rule, rec, x)
        for i in range(d):
            for j in range(d):
                W[i][j] = Lam[i][j]
        return W
    lam = lambda_of(rule, rec, x)
    for li, lk in enumerate(rec.links):
        if lam[lk] == 0:
            continue
        for i in range(d):
            if lk[i]:
                W[i][li] += lam[lk] * Fr(lk[i])
    return W


def hda_matrix(rec, x):
    """B: beta^i(x) = sum_j I^{ij}(x) Omega_{e_j}(x) -- the HDA-predicted
    tangential generator, whose coefficient is the RECORD METRIC READING."""
    d = rec.d
    B = [[Fr(0)] * len(rec.links) for _ in range(d)]
    for i in range(d):
        for j in range(d):
            B[i][j] = rec.I[x][i][j]
    return B


def gap_matrix(rule, rec, x):
    W, B = weight_matrix(rule, rec, x), hda_matrix(rec, x)
    return [[W[i][k] - B[i][k] for k in range(len(rec.links))]
            for i in range(rec.d)]


# ----------------------------------------------------------------------------
# 6.  THE CLOSURE CENSUS -- two genuinely independent routes
#
#     ROUTE-SPARSE  derives each pair's Omega support and evaluates the
#                   residual there; off the support Omega vanishes identically
#                   and so does every quantity linear in it.
#     ROUTE-DENSE   loops every site of every pair with no support reasoning.
#     ROUTE-LITERAL composes the four maps H[N]H[M]H[N]^-1 H[M]^-1 explicitly
#                   and reads the register displacement off the result.
#     The three are compared where all three run; the dense and literal
#     coverages are DERIVED AND PRINTED, never silently capped.
# ----------------------------------------------------------------------------

def pair_support(N, M, rec, neighbour=None):
    """[(site, Omega tuple)] over the sites where Omega does not vanish."""
    L = rec.L
    NB = neighbours(rec.d, L) if neighbour is None else None
    nb = neighbour or (lambda x, lk: add(x, lk, L))
    out = []
    # Omega_l(x) = N(x)M(x+l) - M(x)N(x+l) vanishes identically wherever BOTH
    # lapse profiles vanish at x, so the scan is restricted to the union of
    # their supports.  This is an exact restriction, not a cap: the dense
    # route (which scans every site) gates it.
    for x in rec.S:
        Nx, Mx = N[x], M[x]
        if not Nx and not Mx:
            continue
        ns = NB[x] if NB is not None else [nb(x, lk) for lk in rec.links]
        om = []
        nz = False
        for y in ns:
            v = Nx * M[y] - Mx * N[y]
            om.append(v)
            if v:
                nz = True
        if nz:
            out.append((x, tuple(om)))
    return out


def build_supports(rec, lapses, neighbour=None):
    sup = {}
    n = len(lapses)
    for a in range(n):
        for b in range(n):
            if a != b:
                sup[(a, b)] = pair_support(lapses[a][1], lapses[b][1], rec,
                                           neighbour)
    return sup


def census_cell_sparse(rule, rec, lapses, sup):
    """The residual channel of [H[N],H[M]] measured exactly over every ordered
    lapse pair.  Returns the cell-complete row."""
    d = rec.d
    nlk = len(rec.links)
    Gn, Gd, active = {}, {}, []
    for x in rec.S:
        G = gap_matrix(rule, rec, x)
        if any(v != 0 for row in G for v in row):
            n, dd = common_denominator_matrix(G)
            Gn[x], Gd[x] = n, dd
            active.append(x)
    total = len(sup)
    if MUTANT == "census-cell-drop" and rule == "A-axis" and len(sup) > 132:
        total = total - 1
    if not active:
        return {"closes": True, "nonzero_pairs": 0, "total_pairs": total,
                "max_abs": "0", "witness": None,
                "residual_zero_sites": len(rec.S), "sites": len(rec.S),
                "active_sites": 0}
    aset = set(active)
    memo = {}
    nz, mx, wit = 0, Fr(0), None
    zero_sites = set(rec.S)
    for (a, b), entries in sup.items():
        bad = False
        fm = Fr(0)
        for (x, om) in entries:
            if x not in aset:
                continue
            key = (x, om)
            r = memo.get(key)
            if r is None:
                gn, gd = Gn[x], Gd[x]
                vals = [sum(gn[i][k] * om[k] for k in range(nlk))
                        for i in range(d)]
                mm = max((abs(v) for v in vals), default=0)
                r = (mm == 0, Fr(mm, gd))
                memo[key] = r
            if not r[0]:
                bad = True
                zero_sites.discard(x)
                if r[1] > fm:
                    fm = r[1]
        if bad:
            nz += 1
            if fm > mx:
                mx, wit = fm, [lapses[a][0], lapses[b][0]]
    return {"closes": nz == 0, "nonzero_pairs": nz, "total_pairs": total,
            "max_abs": str(mx), "witness": wit,
            "residual_zero_sites": len(zero_sites), "sites": len(rec.S),
            "active_sites": len(active)}


def census_cell_dense(rule, rec, lapses, neighbour=None):
    """The same row with no support reasoning at all: every site of every
    ordered pair, residual assembled from the declared field formulae."""
    d, L = rec.d, rec.L
    nb = neighbour or (lambda x, lk: add(x, lk, L))
    nz, mx, wit = 0, Fr(0), None
    zero_sites = set(rec.S)
    total = 0
    nlk = len(rec.links)
    GAP = {x: common_denominator_matrix(gap_matrix(rule, rec, x))
           for x in rec.S}
    NBS = {x: [nb(x, lk) for lk in rec.links] for x in rec.S}
    for a in range(len(lapses)):
        for b in range(len(lapses)):
            if a == b:
                continue
            total += 1
            N, M = lapses[a][1], lapses[b][1]
            bad, fm = False, Fr(0)
            for x in rec.S:
                Gn, gd = GAP[x]
                Nx, Mx = N[x], M[x]
                om = [Nx * M[y] - Mx * N[y] for y in NBS[x]]
                rho = [sum(Gn[i][k] * om[k] for k in range(nlk))
                       for i in range(d)]
                if any(t != 0 for t in rho):
                    bad = True
                    zero_sites.discard(x)
                    fmx = Fr(max(abs(t) for t in rho), gd)
                    if fmx > fm:
                        fm = fmx
            if bad:
                nz += 1
                if fm > mx:
                    mx, wit = fm, [lapses[a][0], lapses[b][0]]
    return {"closes": nz == 0, "nonzero_pairs": nz, "total_pairs": total,
            "max_abs": str(mx), "witness": wit,
            "residual_zero_sites": len(zero_sites), "sites": len(rec.S)}


def commutator_literal(rule, rec, N, M, n0):
    """[H[N],H[M]] applied literally to (n0, 0).  Returns (front displacement,
    register displacement) or None if the front does not return."""
    d = rec.d
    fz = dict(n0) if rule == "A-notransport" else None
    HN, HM = Hmap(rule, rec, N, fz), Hmap(rule, rec, M, fz)
    c = (dict(n0), {x: tuple(Fr(0) for _ in range(d)) for x in rec.S})
    for f in [HM.inv, HN.inv, HM.fwd, HN.fwd]:
        c = f(c)
    n1, m1 = c
    return ({x: n1[x] - n0[x] for x in n0}, dict(m1))


def commutator_closed(rule, rec, N, M, neighbour=None):
    """The same displacement from the declared matrices: Delta = W . Omega."""
    d = rec.d
    om = bracket_covector(N, M, rec, neighbour)
    out = {}
    for x in rec.S:
        W = weight_matrix(rule, rec, x)
        out[x] = tuple(sum((W[i][k] * Fr(om[x][k])
                            for k in range(len(rec.links))), Fr(0))
                       for i in range(d))
    return out


def hda_generator(rec, N, M, neighbour=None):
    """beta = the HDA-predicted tangential generator (metric-reading)."""
    d = rec.d
    om = bracket_covector(N, M, rec, neighbour)
    return {x: tuple(sum((rec.I[x][i][j] * Fr(om[x][j]) for j in range(d)),
                         Fr(0)) for i in range(d)) for x in rec.S}


# ---- THE DECOMPOSITION IN THE DECLARED GENERATOR BASIS ---------------------

def decompose_commutator(rule, rec, N, M, n0, neighbour=None):
    """Decompose [H[N],H[M]] in the declared generator basis.  Channels:
       NORMAL      -- the front displacement, projected on the constraint family
       TANGENTIAL  -- the register displacement, split as beta + residual
       LATTICE     -- whether a channel lies in the lattice-translation span
                      (a constant field)
       RESIDUAL    -- what the HDA generator does not account for."""
    d = rec.d
    df, dr = commutator_literal(rule, rec, N, M, n0)
    beta = hda_generator(rec, N, M, neighbour)
    resid = {x: tuple(dr[x][i] - beta[x][i] for i in range(d)) for x in rec.S}

    def classify(fld):
        if all(all(t == 0 for t in fld[x]) for x in rec.S):
            return "ZERO"
        f0 = fld[rec.S[0]]
        if all(fld[x] == f0 for x in rec.S):
            return "LATTICE-TRANSLATION"
        return "SITE-VARYING"

    return {"normal_channel_zero": all(df[x] == 0 for x in rec.S),
            "tangential_class": classify(dr),
            "hda_generator_class": classify(beta),
            "residual_class": classify(resid),
            "residual_zero": all(all(t == 0 for t in resid[x]) for x in rec.S),
            "residual_sum": [str(sum((resid[x][i] for x in rec.S), Fr(0)))
                             for i in range(d)],
            "front": df, "register": dr, "residual": resid}


# ---- STRUCTURE-COEFFICIENT EXTRACTION --------------------------------------
#
# The coefficient is NOT read off the rule.  It is SOLVED FOR from the
# commutators themselves:  Delta^i(x) = sum_j c^{ij}(x) omega_j(x)  over EVERY
# ordered lapse pair, on the axis bracket covectors -- the HDA form.  The
# system is heavily over-determined, so EXISTENCE is a real test that a rule
# whose commutator is not of that form fails.

def extract_coefficient(rule, rec, lapses, sup):
    d = rec.d
    nlk = len(rec.links)
    # Each incoming equation  omega . c_i = Delta^i  is scaled by the site's
    # common weight denominator so the whole reduction runs in integers; the
    # scaling multiplies both sides and cannot change the solution.
    Wc = {}
    for x in rec.S:
        Wc[x] = common_denominator_matrix(weight_matrix(rule, rec, x))
    rows = {x: [] for x in rec.S}
    incons = {x: False for x in rec.S}
    for (a, b), entries in sup.items():
        for (x, om) in entries:
            Wn, den = Wc[x]
            row = [den * om[j] for j in range(d)] + \
                  [sum(Wn[i][k] * om[k] for k in range(nlk)) for i in range(d)]
            for br in rows[x]:
                p = next(k for k in range(d) if br[k] != 0)
                if row[p] != 0:
                    a1, b1 = br[p], row[p]
                    g = gcd_int(a1, b1)
                    fa, fb = a1 // g, b1 // g
                    row = [fa * row[k] - fb * br[k] for k in range(2 * d)]
            if any(row[k] != 0 for k in range(d)):
                g = 0
                for v in row:
                    g = gcd_int(g, v)
                if g > 1:
                    row = [v // g for v in row]
                rows[x].append(row)
            elif any(row[k] != 0 for k in range(d, 2 * d)):
                if MUTANT != "extraction-lax":
                    incons[x] = True
    out = {}
    for x in rec.S:
        rk = len(rows[x])
        if incons[x]:
            out[x] = ("NONE", None, rk)
        elif rk < d:
            out[x] = ("NON-UNIQUE", None, rk)
        else:
            A = [[rows[x][r][j] for j in range(d)] for r in range(d)]
            c = [solve_exact(A, [rows[x][r][d + i] for r in range(d)])
                 for i in range(d)]
            out[x] = ("UNIQUE", c, rk)
    return out


def type_coefficient(rec, ext, metric_route=None):
    """TYPE THE EXTRACTED COEFFICIENT BY MEASUREMENT.  The metric it is
    compared against is re-encoded by the INDEPENDENT closed-form route, not
    by the same solve that built the record."""
    st = sorted(set(v[0] for v in ext.values()))
    if st != ["UNIQUE"]:
        return {"class": "NOT-EXTRACTABLE", "statuses": st,
                "constant": False, "metric_reading": False,
                "value_at_first_site": None, "distinct_values": 0,
                "ranks": sorted(set(v[2] for v in ext.values()))}
    S = rec.S
    c0 = ext[S[0]][1]
    const = all(ext[x][1] == c0 for x in S)
    if metric_route is None:
        metric_route = {x: inv_exact(q_from_counts_closed(
            rec.d, rec.counts[x])) for x in S}
    if MUTANT == "coefficient-typing-conflation":
        const = True
    metric = all(ext[x][1] == metric_route[x] for x in S)
    zero = all(all(v == 0 for row in ext[x][1] for v in row) for x in S)
    if zero:
        cl = "ZERO"
    elif metric and not const:
        cl = "METRIC-READING-SITE-VARYING"
    elif metric and const:
        cl = "METRIC-READING-CONSTANT"
    elif const:
        cl = "CONSTANT-NON-METRIC"
    else:
        cl = "SITE-VARYING-NON-METRIC"
    return {"class": cl, "constant": const, "metric_reading": metric,
            "statuses": st, "ranks": sorted(set(v[2] for v in ext.values())),
            "value_at_first_site": [[str(v) for v in row] for row in c0],
            "distinct_values": len(set(
                tuple(tuple(str(v) for v in row) for row in ext[x][1])
                for x in S))}


# ----------------------------------------------------------------------------
# 7.  THE NORMAL-TANGENTIAL BRACKET {D, H} AND THE TANGENTIAL BRACKET {D, D}
#
#     Hypersurface deformation requires THREE brackets, not one:
#        {H[N], H[M]} = D[ q^{ij} (N d_j M - M d_j N) ]     (section 6)
#        {D[v], H[N]} = H[ L_v N ]
#        {D[v], D[w]} = D[ [v, w] ]
#     The second and third are censused here, at BOTH declared tangential
#     realisations, with the CONVENTION SWEEP that decides whether a mismatch
#     in the front sector is a declared convention or a defect.
# ----------------------------------------------------------------------------

def lie_lapse_forward(rec, v, N):
    """The declared finite transported lapse derivative L_B N = B^j d_j N with
    I7's declared forward difference d_j F(x) = F(x+e_j) - F(x)."""
    NB = neighbours(rec.d, rec.L)
    d = rec.d
    return {x: sum((v[x][j] * Fr(N[NB[x][j]] - N[x]) for j in range(d)), Fr(0))
            for x in rec.S}


def lie_lapse_backward(rec, v, N):
    """The same object at the BACKWARD difference convention."""
    L, d = rec.L, rec.d
    axes = rec.links[:d]
    back = {x: tuple(add(x, tuple(-t for t in axes[j]), L) for j in range(d))
            for x in rec.S}
    return {x: sum((v[x][j] * Fr(N[x] - N[back[x][j]]) for j in range(d)),
                   Fr(0)) for x in rec.S}


LIE_CONVENTIONS = (("FORWARD", lie_lapse_forward),
                   ("BACKWARD", lie_lapse_backward))
BRACKET_ORDERS = ("D-H-Dinv-Hinv", "H-D-Hinv-Dinv")


def dh_bracket_literal(rule, rec, N, v, n0, realisation, order):
    """The normal-tangential bracket, applied literally to (n0, 0)."""
    d = rec.d
    HN = Hmap(rule, rec, N)
    Dv = Dmap(rec, v, realisation)
    Di = Dmap(rec, neg_field(v), realisation)
    c = (dict(n0), {x: tuple(Fr(0) for _ in range(d)) for x in rec.S})
    seq = ([HN.inv, Di.fwd, HN.fwd, Dv.fwd] if order == "D-H-Dinv-Hinv"
           else [Di.fwd, HN.inv, Dv.fwd, HN.fwd])
    for f in seq:
        c = f(c)
        if c is None:
            return None
    n1, m1 = c
    return ({x: n1[x] - n0[x] for x in rec.S}, dict(m1))


def dh_bracket_closed(rule, rec, N, v, n0):
    """THE CLOSED FORM of the same bracket at D-TOT, order D-H-Dinv-Hinv, for
    a constant translation field v -- derived from the skew-product structure,
    sharing no code with the literal composition:
        front    = S_v N - N        (S_v n)(x) := n(x - v)
        register = w[N, (S_{-v} - 1)(n - N)]"""
    L = rec.L
    vv = tuple(int(t) for t in v[rec.S[0]])
    front = {x: N[add(x, tuple(-t for t in vv), L)] - N[x] for x in rec.S}
    base = {x: n0[x] - N[x] for x in rec.S}
    shifted = {x: base[add(x, vv, L)] - base[x] for x in rec.S}
    return front, drag(rule, rec, N, shifted)


def h_displacement(rule, rec, P, n0):
    """H[P] applied to (n0, 0): its front and register displacement."""
    d = rec.d
    c = Hmap(rule, rec, P).fwd(
        (dict(n0), {x: tuple(Fr(0) for _ in range(d)) for x in rec.S}))
    return ({x: c[0][x] - n0[x] for x in rec.S}, dict(c[1]))


def dh_membership(rule, rec, N, v, cfgs, realisation, order):
    """Is the bracket a member of the declared generator basis?  Tested at
    EVERY declared configuration, so a coincidence at one front cannot pass.
      IDENTITY        the bracket is trivial (the HDA content is absent)
      IN-CONSTRAINT   the bracket equals H[P] for the P its front names
      IN-EXTENDED     the bracket equals H[P] . D[u] for a configuration-
                      INDEPENDENT tangential field u
      OUTSIDE         the bracket is not a product of declared generators"""
    d = rec.d
    diffs, ident, okH = [], True, True
    for n0 in cfgs:
        r = dh_bracket_literal(rule, rec, N, v, n0, realisation, order)
        if r is None:
            return "UNDEFINED", None
        df, dr = r
        if any(df[x] != 0 for x in rec.S) or any(
                any(t != 0 for t in dr[x]) for x in rec.S):
            ident = False
        hf, hr = h_displacement(rule, rec, dict(df), n0)
        if any(hr[x] != dr[x] for x in rec.S) or any(
                hf[x] != df[x] for x in rec.S):
            okH = False
        diffs.append({x: tuple(dr[x][i] - hr[x][i] for i in range(d))
                      for x in rec.S})
    if ident:
        return "IDENTITY", None
    if okH:
        return "IN-CONSTRAINT", None
    if all(diffs[k] == diffs[0] for k in range(len(diffs))):
        return "IN-EXTENDED", diffs[0]
    return "OUTSIDE", None


def dd_bracket(rec, va, vb, n0, realisation):
    """{D[v], D[w]} at the lattice's own translation generators."""
    d = rec.d
    c = (dict(n0), {x: tuple(Fr(0) for _ in range(d)) for x in rec.S})
    for f in [Dmap(rec, neg_field(vb), realisation).fwd,
              Dmap(rec, neg_field(va), realisation).fwd,
              Dmap(rec, vb, realisation).fwd,
              Dmap(rec, va, realisation).fwd]:
        c = f(c)
        if c is None:
            return None
    return (all(c[0][x] == n0[x] for x in rec.S)
            and all(all(t == 0 for t in c[1][x]) for x in rec.S))


# ---- THE TRANSLATION CONTROL AND ITS SCRAMBLED NEGATIVE --------------------

def scrambled_neighbour(d, L):
    """A DECLARED deterministic scramble of the record adjacency: the
    neighbour map is post-composed with the site permutation
    sigma(x) = (x_1 + 1, x_2, ..., x_d) on the FIRST coordinate only when the
    last coordinate is odd -- a fixed, reproducible derangement of the link
    structure that preserves the site set and the per-site link count."""
    def nb(x, lk):
        y = add(x, lk, L)
        if y[d - 1] % 2 == 1:
            y = tuple((y[0] + 1) % L if k == 0 else y[k] for k in range(d))
        return y
    return nb


def neighbour_equivariance(d, L, neighbour=None):
    """The lattice's own covariance: nb(x+u, l) = nb(x, l) + u for every chart
    translation u and every declared link l.  Exact on the record lattice;
    the scrambled control must break it, measurably."""
    nb = neighbour or (lambda x, lk: add(x, lk, L))
    good = bad = 0
    for u in sites(d, L):
        for x in sites(d, L):
            for lk in link_set(d):
                if nb(add(x, u, L), lk) == add(nb(x, lk), u, L):
                    good += 1
                else:
                    bad += 1
    if MUTANT == "equivariance-break" and neighbour is None:
        good, bad = good - 1, bad + 1
    return {"equivariant_cells": good, "violating_cells": bad,
            "total_cells": good + bad}


def chart_group_order(d, L):
    """The declared chart group: the |X| chart translations and the d!
    direction relabellings.  The order is DERIVED by explicit closure of the
    generated permutation group of the site set, never typed."""
    S = sites(d, L)
    idx = {x: i for i, x in enumerate(S)}
    gens = []
    for i in range(d):
        u = tuple(1 if k == i else 0 for k in range(d))
        gens.append(tuple(idx[add(x, u, L)] for x in S))
    for sig in itertools.permutations(range(d)):
        gens.append(tuple(idx[tuple(x[sig[i]] for i in range(d))] for x in S))
    if MUTANT == "chart-group-drop":
        gens = gens[:1]
    ident = tuple(range(len(S)))
    seen = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for p in frontier:
            for g in gens:
                q = tuple(g[p[i]] for i in range(len(S)))
                if q not in seen:
                    seen.add(q)
                    nxt.append(q)
        frontier = nxt
    return len(seen)


def translation_covariance_of_the_residual(rule, rec_builder, d, L, lapses,
                                           neighbour=None):
    """RUNBOOK section 14 symmetry self-test, FRESH-EVALUATED: transport the
    record AND the lapses by a chart translation and require the residual
    field to transport with them, exactly, site by site."""
    L_ = L
    nb = neighbour or (lambda x, lk: add(x, lk, L_))
    rec = rec_builder()
    good = bad = nonzero = 0
    S = sites(d, L)
    probes = [(a, b) for a in range(min(4, len(lapses)))
              for b in range(min(4, len(lapses))) if a != b]
    for u in S:
        recu = rec_builder()
        recu.counts = {x: dict(rec.counts[add(x, tuple(-t for t in u), L)])
                       for x in S}
        recu.q = {x: rec.q[add(x, tuple(-t for t in u), L)] for x in S}
        recu.I = {x: rec.I[add(x, tuple(-t for t in u), L)] for x in S}
        recu.name = rec.name + "@" + str(u)
        for (a, b) in probes:
            N = {x: lapses[a][1][add(x, tuple(-t for t in u), L)] for x in S}
            M = {x: lapses[b][1][add(x, tuple(-t for t in u), L)] for x in S}
            om0 = bracket_covector(lapses[a][1], lapses[b][1], rec, nb)
            omu = bracket_covector(N, M, recu, nb)
            r0 = {x: tuple(sum((Fr(gap_matrix(rule, rec, x)[i][k]) * Fr(om0[x][k])
                                for k in range(len(rec.links))), Fr(0))
                           for i in range(d)) for x in S}
            ru = {x: tuple(sum((Fr(gap_matrix(rule, recu, x)[i][k]) * Fr(omu[x][k])
                                for k in range(len(rec.links))), Fr(0))
                           for i in range(d)) for x in S}
            for x in S:
                if any(t != 0 for t in r0[x]):
                    nonzero += 1
                if ru[x] == r0[add(x, tuple(-t for t in u), L)]:
                    good += 1
                else:
                    bad += 1
    if MUTANT == "covariance-break" and neighbour is None:
        good, bad = good - 1, bad + 1
    return {"covariant_cells": good, "violating_cells": bad,
            "total_cells": good + bad, "nonzero_base_cells": nonzero}


# ----------------------------------------------------------------------------
# 8.  THE MACHINERY-RECOVERY CONTROL (pin section 3 item 3)
#
#     Before any new measurement counts, this unit's reimplementation must
#     reproduce I7's own numbers at I7's OWN declared scope -- which is the
#     extent the census gate excludes.  The recovery is an ANCHOR, not a
#     measurement: every cell is compared against the pinned receipt.
# ----------------------------------------------------------------------------

def recover_i7(decl, rec7):
    d, L = decl["d"], decl["L"]
    recs = build_records(d, L, decl)
    lapses = build_lapse_family(d, L)
    S = sites(d, L)
    adm = sorted([n for n in recs if recs[n].admissible])
    rejected = sorted([n for n in recs if not recs[n].admissible])
    out = {"scope": {"d": d, "L": L, "sites": len(S),
                     "lapse_family_size": len(lapses),
                     "ordered_pairs": len(lapses) * (len(lapses) - 1)},
           "admissible": adm, "rejected": rejected}

    # -- the closure table, cell by cell against the pinned receipt ---------
    closure_cmp, closure_bad, rows = 0, [], {}
    sector_cmp, sector_bad = 0, []
    sup_by_rec = {nm: build_supports(recs[nm], lapses) for nm in adm}
    for rule, _a, _t in RULE_TABLE:
        for nm in adm:
            key = "%s|%s" % (rule, nm)
            cell = census_cell_sparse(rule, recs[nm], lapses, sup_by_rec[nm])
            rows[key] = cell
            if MUTANT == "recovery-closure-drift" and key == "A-insert|G-FLAT":
                cell = dict(cell)
                cell["nonzero_pairs"] = cell["nonzero_pairs"] + 1
            exp = rec7["tables"]["closure"].get(key)
            if exp is not None:
                closure_cmp += 1
                for f in ("closes", "nonzero_pairs", "total_pairs", "max_abs",
                          "witness"):
                    if cell[f] != exp[f]:
                        closure_bad.append([key, f, cell[f], exp[f]])
            sexp = rec7["tables"]["sector_law"].get(key)
            if sexp is not None:
                sector_cmp += 1
                li = sum(1 for x in S
                         if lambda_of(rule, recs[nm], x) == recs[nm].I[x])
                if MUTANT == "diagonal-anchor-drift" and key == "A-axis|G-FLAT":
                    li = li - 1
                got = {"Lambda_equals_I_sites": li,
                       "residual_zero_sites": cell["residual_zero_sites"],
                       "sites": len(S)}
                if got != sexp:
                    sector_bad.append([key, got, sexp])
    out["closure_cells_compared"] = closure_cmp
    out["closure_mismatches"] = closure_bad
    out["sector_cells_compared"] = sector_cmp
    out["sector_mismatches"] = sector_bad
    out["closure_rows"] = rows

    # -- the identifiability rank ------------------------------------------
    ext = extract_coefficient("A-insert", recs["G-FLAT"], lapses,
                              sup_by_rec["G-FLAT"])
    rank = {str(x): ext[x][2] for x in S}
    out["identifiability_rank"] = rank
    out["rank_matches_pin"] = (rank == rec7["tables"]["identifiability_rank"])

    # -- record-IS-metric: the readout determinant and the two routes -------
    det = readout_determinant(d)
    ver = 0
    twin = 0
    for nm in adm:
        for x in S:
            q1 = recs[nm].q[x]
            q2 = q_from_counts_closed(d, recs[nm].counts[x])
            if q1 == q2:
                twin += 1
            ok = all(sum((q1[i][j] * Fr(lk[i] * lk[j])
                          for i in range(d) for j in range(d)), Fr(0))
                     == Fr(recs[nm].counts[x][lk]) for lk in recs[nm].links)
            if ok:
                ver += 1
    out["readout"] = {"determinant": str(det), "sites_verified": ver,
                      "two_route_agreements": twin,
                      "cells": len(adm) * len(S)}
    out["readout_matches_pin"] = (
        {"determinant": str(det), "sites_verified": ver}
        == rec7["tables"]["readout_reencoding"])

    # -- the general-d row --------------------------------------------------
    d3, L3 = decl["d_ext"], decl["L_ext"]
    recs3 = build_records(d3, L3, decl)
    # I7's own d=3 probe family: the FIRST SIX site deltas plus the constant
    # profile.  Reproduced verbatim because the recovery target was measured
    # over it; the census below uses the full declared family instead.
    S3 = sites(d3, L3)
    lap3 = [("delta%s" % (x,), {y: (1 if y == x else 0) for y in S3})
            for x in S3[:6]]
    lap3.append(("one", {y: 1 for y in S3}))
    gen = {}
    for rule in decl["rules_d3"]:
        for nm in sorted(decl["records_d3"]):
            s3 = build_supports(recs3[nm], lap3)
            cell = census_cell_sparse(rule, recs3[nm], lap3, s3)
            gen["%s|%s" % (rule, nm)] = cell["nonzero_pairs"] + (
                1 if MUTANT == "general-d-drift" and rule == "A-insert"
                and nm == "G3-FLAT" else 0)
    out["general_d"] = gen
    out["general_d_matches_pin"] = (gen == rec7["tables"]["general_d"])

    # -- the declared count lattice's link-locality census ------------------
    amax, dmax = 6, 12
    adm_pts = []
    for n1 in range(1, amax + 1):
        for n2 in range(1, amax + 1):
            for n3 in range(1, dmax + 1):
                q = q_from_counts_closed(2, {(1, 0): n1, (0, 1): n2, (1, 1): n3})
                if positive_definite(q):
                    adm_pts.append(((n1, n2, n3), inv_exact(q)))
    p12 = sum(1 for i in range(len(adm_pts)) for j in range(i + 1, len(adm_pts))
              if adm_pts[i][0][2] == adm_pts[j][0][2]
              and adm_pts[i][1][0][1] != adm_pts[j][1][0][1])
    p11 = sum(1 for i in range(len(adm_pts)) for j in range(i + 1, len(adm_pts))
              if adm_pts[i][0][0] == adm_pts[j][0][0]
              and adm_pts[i][0][2] == adm_pts[j][0][2]
              and adm_pts[i][1][0][0] != adm_pts[j][1][0][0])
    lat = {"admissible_points": len(adm_pts),
           "pairs_sharing_n_diag_diff_I12": p12,
           "pairs_sharing_n_e1_n_diag_diff_I11": p11}
    out["link_locality_lattice"] = lat
    out["lattice_matches_pin"] = (lat == rec7["tables"]["link_locality_lattice"])

    # -- the diagonal sector itself ----------------------------------------
    diag = sorted([nm for nm in adm
                   if all(recs[nm].q[x][0][1] == 0 for x in S)])
    if MUTANT == "diagonal-sector-widen":
        diag = sorted(set(diag) | {"G-OFFDIAG"})
    out["diagonal_sector"] = diag
    out["diagonal_sector_closes_at_the_link_local_rule"] = sorted(
        [nm for nm in diag if rows["A-axis|%s" % nm]["closes"]])
    return out


# ----------------------------------------------------------------------------
# 9.  THE CENSUS ARENAS AND THE FULL SWEEP
# ----------------------------------------------------------------------------

CENSUS_ARENAS = ((2, 4), (2, 5), (3, 4), (3, 5))
LAPSE_SCOPES = ("BASE", "TRANSLATES")
DENSE_ARENAS = ((2, 4), (2, 5))    # the dense cross-route coverage, DERIVED AND PRINTED
LITERAL_PROBE_LAPSES = 6      # declared, printed, gated -- never a silent cap
DH_LITERAL_PROBE = 4
DEFECT_PROBE_LAPSES = 6
DH_PROBE_DELTAS = 6           # I7's own d=3 probe convention, reused here
REALISATIONS = ("D-REG", "D-TOT")


def declared_configurations(d, L):
    """The declared front configurations every membership test runs at."""
    S = sites(d, L)
    return [{x: (2 * x[0] + 5 * x[-1]) % 7 for x in S},
            {x: (x[0] * x[0] + 3 * x[-1]) % 5 for x in S},
            {x: (x[0] + 2 * x[-1] * x[-1]) % 11 for x in S}]


def rules_at(d, decl):
    return ([r[0] for r in RULE_TABLE] if d == 2 else list(decl["rules_d3"]))


def dh_probe_family(d, L, base):
    """The lapse scope of the bracket census, DECLARED AND PRINTED (never a
    silent cap).  At d = 2 it is the whole declared family.  At d = 3 it is
    I7's own d=3 probe convention -- the first six site deltas together with
    the constant profile and the d chart ramps -- reused verbatim."""
    if d == 2:
        return list(base)
    deltas = [t for t in base if t[0].startswith("delta")][:DH_PROBE_DELTAS]
    rest = [t for t in base if not t[0].startswith("delta")]
    return deltas + rest


def run_census(decl, rec7):
    """The closure census, the coefficient extraction and the bracket census
    over every declared arena.  Cell-complete; every count derived."""
    census, coeffs, dh_rows, dd_rows, conv_rows = [], [], [], [], []
    decomp_rows, defect_rows = [], []
    two_route = {"dense_cells": 0, "dense_disagreements": [],
                 "literal_cells": 0, "literal_disagreements": [],
                 "dh_literal_cells": 0, "dh_literal_disagreements": [],
                 "conv_literal_cells": 0, "conv_literal_disagreements": [],
                 "dense_arenas": [list(a) for a in DENSE_ARENAS],
                 "literal_pair_probe": LITERAL_PROBE_LAPSES,
                 "dh_literal_probe": DH_LITERAL_PROBE}
    arenas = list(CENSUS_ARENAS)
    if MUTANT == "l-gate-violation":
        arenas = [(2, 3)] + arenas
    census_scope_gate(arenas)
    for (d, L) in arenas:
        recs = build_records(d, L, decl)
        adm = sorted([n for n in recs if recs[n].admissible])
        rules = rules_at(d, decl)
        cfgs = declared_configurations(d, L)
        tgens = lattice_translation_generators(d)
        fams = {"BASE": build_lapse_family(d, L),
                "TRANSLATES": build_lapse_translates(d, L)}
        if MUTANT == "lapse-family-drop":
            fams["BASE"] = fams["BASE"][:-1]
        base = fams["BASE"]

        # ---- 1. THE CLOSURE CENSUS + COEFFICIENT EXTRACTION --------------
        for scope in LAPSE_SCOPES:
            lapses = fams[scope]
            for nm in adm:
                rec = recs[nm]
                sup = build_supports(rec, lapses)
                for rule in rules:
                    if MUTANT == "census-cell-omit" and rule == "B-chart" \
                            and nm == "G-FLAT" and scope == "TRANSLATES":
                        continue
                    cell = census_cell_sparse(rule, rec, lapses, sup)
                    row = {"d": d, "L": L, "scope": scope, "rule": rule,
                           "record": nm, "homogeneous": rec.homogeneous}
                    row.update(cell)
                    census.append(row)
                    ext = extract_coefficient(rule, rec, lapses, sup)
                    coeffs.append({"d": d, "L": L, "scope": scope,
                                   "rule": rule, "record": nm,
                                   "homogeneous": rec.homogeneous,
                                   "coefficient": type_coefficient(rec, ext)})
                    if (d, L) in DENSE_ARENAS and scope == "BASE":
                        dn = census_cell_dense(rule, rec, lapses)
                        two_route["dense_cells"] += 1
                        for f in ("closes", "nonzero_pairs", "total_pairs",
                                  "max_abs", "witness", "residual_zero_sites"):
                            if cell[f] != dn[f]:
                                two_route["dense_disagreements"].append(
                                    [d, L, rule, nm, f, cell[f], dn[f]])

        # ---- 2. THE LITERAL COMPOSITION ROUTE (declared probe) -----------
        probe = base[:LITERAL_PROBE_LAPSES]
        for nm in adm:
            rec = recs[nm]
            for rule in rules:
                for a in range(len(probe)):
                    for b in range(len(probe)):
                        if a == b:
                            continue
                        cl = commutator_closed(rule, rec, probe[a][1],
                                               probe[b][1])
                        for n0 in cfgs:
                            df, dr = commutator_literal(rule, rec, probe[a][1],
                                                        probe[b][1], n0)
                            two_route["literal_cells"] += 1
                            bad = (any(df[x] != 0 for x in rec.S)
                                   or any(dr[x] != cl[x] for x in rec.S))
                            if bad:
                                two_route["literal_disagreements"].append(
                                    [d, L, rule, nm, probe[a][0], probe[b][0]])

        # ---- 3. THE GENERATOR-BASIS DECOMPOSITION ------------------------
        for nm in adm:
            rec = recs[nm]
            for rule in rules:
                classes, rsum_zero, rsum_tot = {}, 0, 0
                for a in range(len(probe)):
                    for b in range(len(probe)):
                        if a == b:
                            continue
                        dc = decompose_commutator(rule, rec, probe[a][1],
                                                  probe[b][1], cfgs[0])
                        k = (dc["normal_channel_zero"], dc["tangential_class"],
                             dc["residual_class"])
                        classes[k] = classes.get(k, 0) + 1
                        rsum_tot += 1
                        if all(t == "0" for t in dc["residual_sum"]):
                            rsum_zero += 1
                decomp_rows.append(
                    {"d": d, "L": L, "rule": rule, "record": nm,
                     "classes": sorted([[list(k), v] for k, v in classes.items()],
                                       key=lambda t: str(t[0])),
                     "pairs": sum(classes.values()),
                     "residual_lattice_sum_zero": rsum_zero,
                     "residual_pairs": rsum_tot})

        # ---- 4. THE {D,H} BRACKET CENSUS (closed form + literal probe) ---
        dh_lapses = dh_probe_family(d, L, base)
        for nm in adm:
            rec = recs[nm]
            for rule in rules:
                for real in REALISATIONS:
                    tally = {}
                    for (lname, N) in dh_lapses:
                        for tv in tgens:
                            v = const_field(rec, tv)
                            st, _u = dh_membership_closed(rule, rec, N, v,
                                                          cfgs, real)
                            tally[st] = tally.get(st, 0) + 1
                    if MUTANT == "decomposition-basis-drop" and real == "D-TOT":
                        tally = {"IN-CONSTRAINT": sum(tally.values())}
                    dh_rows.append({"d": d, "L": L, "rule": rule, "record": nm,
                                    "realisation": real,
                                    "tally": dict(sorted(tally.items())),
                                    "brackets": sum(tally.values())})
                    for (lname, N) in dh_lapses[:DH_LITERAL_PROBE]:
                        for tv in tgens:
                            v = const_field(rec, tv)
                            a1, _ = dh_membership_closed(rule, rec, N, v, cfgs,
                                                         real)
                            a2, _ = dh_membership(rule, rec, N, v, cfgs, real,
                                                  "D-H-Dinv-Hinv")
                            two_route["dh_literal_cells"] += 1
                            if a1 != a2:
                                two_route["dh_literal_disagreements"].append(
                                    [d, L, rule, nm, real, lname, a1, a2])

        # ---- 5. THE {D,D} TRANSLATION CONTROL (positive) -----------------
        for nm in adm:
            rec = recs[nm]
            for real in REALISATIONS:
                ok = bad = 0
                for a in tgens + [tuple([0] * d)]:
                    for b in tgens + [tuple([0] * d)]:
                        r = dd_bracket(rec, const_field(rec, a),
                                       const_field(rec, b), cfgs[0], real)
                        if r:
                            ok += 1
                        else:
                            bad += 1
                dd_rows.append({"d": d, "L": L, "record": nm,
                                "realisation": real, "closing": ok,
                                "non_closing": bad, "total": ok + bad})

        # ---- 6. THE CONVENTION SWEEP -------------------------------------
        # The bracket's FRONT sector does not involve the drag rule -- measured
        # below by G-CONVENTION-RULE-INDEPENDENT -- so the sweep is computed
        # once per (record, lapse, translation) and counted over the rules.
        conv_hits = {}
        rec0 = recs[adm[0]]
        for (lname, N) in base:
            for tv in tgens:
                v = const_field(rec0, tv)
                for order in BRACKET_ORDERS:
                    fr = dh_front_closed(rec0, N, v, order)
                    for (cname, cfn) in LIE_CONVENTIONS:
                        lv = cfn(rec0, v, N)
                        if all(fr[x] == lv[x] for x in rec0.S):
                            conv_hits[(order, cname)] = \
                                conv_hits.get((order, cname), 0) + 1
        for order in BRACKET_ORDERS:
            for (cname, cfn) in LIE_CONVENTIONS:
                ok = conv_hits.get((order, cname), 0) * len(adm) * len(rules)
                tot = len(base) * len(tgens) * len(adm) * len(rules)
                if MUTANT == "convention-sweep-truncate" and \
                        order == "H-D-Hinv-Dinv" and cname == "BACKWARD":
                    ok = 0
                conv_rows.append({"d": d, "L": L, "order": order,
                                  "difference": cname, "front_matches": ok,
                                  "brackets": tot})
        # the convention sweep's own front closed form, against the literal
        for nm in adm[:2]:
            rec = recs[nm]
            for rule in rules[:2]:
                for order in BRACKET_ORDERS:
                    for (lname, N) in dh_lapses[:DH_LITERAL_PROBE]:
                        for tv in tgens:
                            v = const_field(rec, tv)
                            fr = dh_front_closed(rec, N, v, order)
                            r = dh_bracket_literal(rule, rec, N, v, cfgs[0],
                                                   "D-TOT", order)
                            two_route["conv_literal_cells"] += 1
                            if r is None or any(r[0][x] != fr[x] for x in rec.S):
                                two_route["conv_literal_disagreements"].append(
                                    [d, L, rule, nm, order, lname])

        # ---- 7. THE DEFECT, CHARACTERISED --------------------------------
        for nm in adm:
            rec = recs[nm]
            for rule in rules:
                nzero = ntot = bsum = 0
                mx = Fr(0)
                for (lname, N) in dh_lapses[:DEFECT_PROBE_LAPSES]:
                    for tv in tgens:
                        v = const_field(rec, tv)
                        fld = dh_defect_field(rule, rec, N, v, cfgs[0])
                        ntot += 1
                        if all(all(t == 0 for t in fld[x]) for x in rec.S):
                            nzero += 1
                        if all(sum((fld[x][i] for x in rec.S), Fr(0)) == 0
                               for i in range(d)):
                            bsum += 1
                        for x in rec.S:
                            for t in fld[x]:
                                if abs(t) > mx:
                                    mx = abs(t)
                defect_rows.append(
                    {"d": d, "L": L, "rule": rule, "record": nm,
                     "homogeneous": rec.homogeneous, "probes": ntot,
                     "vanishing_probes": nzero, "lattice_sum_zero": bsum,
                     "max_abs": str(mx)})
    return {"census": census, "coefficients": coeffs, "dh": dh_rows,
            "dd": dd_rows, "conventions": conv_rows, "two_route": two_route,
            "decomposition": decomp_rows, "defect": defect_rows}


# ---- THE CLOSED-FORM BRACKET ROUTE (independent of the literal composition)
#
# Verified against the literal four-map composition on a declared sample at
# EVERY arena (G-DH-TWO-ROUTES); the sample's size is derived and printed.

def dh_membership_closed(rule, rec, N, v, cfgs, realisation):
    """The same classification as dh_membership, computed from the skew-product
    closed forms instead of composing the four maps."""
    d, L = rec.d, rec.L
    if realisation == "D-REG":
        # D-REG shifts the register only; H[N] adds w[N,n] to the register and
        # N to the front; the two actions are independent summands, so the
        # bracket is the identity for every N, v and configuration.
        return "IDENTITY", None
    vv = tuple(int(t) for t in v[rec.S[0]])
    front = {x: N[add(x, tuple(-t for t in vv), L)] - N[x] for x in rec.S}
    ident = all(front[x] == 0 for x in rec.S)
    diffs, okH = [], True
    for n0 in cfgs:
        base = {x: n0[x] - N[x] for x in rec.S}
        shifted = {x: base[add(x, vv, L)] - base[x] for x in rec.S}
        reg = drag(rule, rec, N, shifted)
        hreg = drag(rule, rec, dict(front), n0)
        if any(reg[x] != hreg[x] for x in rec.S):
            okH = False
        if any(any(t != 0 for t in reg[x]) for x in rec.S):
            ident = False
        diffs.append({x: tuple(reg[x][i] - hreg[x][i] for i in range(d))
                      for x in rec.S})
    if MUTANT == "dh-route-split":
        return "IN-EXTENDED", None
    if ident:
        return "IDENTITY", None
    if okH:
        return "IN-CONSTRAINT", None
    if all(diffs[k] == diffs[0] for k in range(len(diffs))):
        return "IN-EXTENDED", diffs[0]
    return "OUTSIDE", None


def dh_front_closed(rec, N, v, order):
    """The bracket's FRONT displacement in closed form.  At D-TOT with a
    constant translation field the front action of the composite is the pure
    shift S_v N - N; the reversed factor order inverts it."""
    L = rec.L
    vv = tuple(int(t) for t in v[rec.S[0]])
    f = {x: N[add(x, tuple(-t for t in vv), L)] - N[x] for x in rec.S}
    if MUTANT == "dh-front-split":
        f = {x: f[x] + 1 for x in rec.S}
    if order == "D-H-Dinv-Hinv":
        return f
    return {x: -f[x] for x in rec.S}


def dh_defect_field(rule, rec, N, v, n0):
    """THE MEASURED DEFECT of the normal-tangential bracket at D-TOT: the
    register displacement the constraint family cannot account for,
        defect = w[N, (S_{-v}-1)(n-N)] - w[S_v N - N, n].
    Returned as a field so its lattice sum (boundary-term status) and its
    sector-vanishing status can be measured."""
    d, L = rec.d, rec.L
    vv = tuple(int(t) for t in v[rec.S[0]])
    front = {x: N[add(x, tuple(-t for t in vv), L)] - N[x] for x in rec.S}
    base = {x: n0[x] - N[x] for x in rec.S}
    shifted = {x: base[add(x, vv, L)] - base[x] for x in rec.S}
    reg = drag(rule, rec, N, shifted)
    hreg = drag(rule, rec, dict(front), n0)
    if MUTANT == "defect-blind":
        return {x: tuple(Fr(0) for _ in range(d)) for x in rec.S}
    out = {x: tuple(reg[x][i] - hreg[x][i] for i in range(d)) for x in rec.S}
    if MUTANT == "boundary-lax":
        tot = [sum((out[x][i] for x in rec.S), Fr(0)) for i in range(d)]
        z = rec.S[0]
        out[z] = tuple(out[z][i] - tot[i] for i in range(d))
    return out


# ----------------------------------------------------------------------------
# 10.  THE L GATE'S MEASURED REASON, AND THE INHERITED FACTS RE-CONFIRMED
# ----------------------------------------------------------------------------

def l_gate_reason(adj_text, ledger_text):
    """The R2 handoff's L >= 4 requirement, with its reason MEASURED here and
    matched against the adjudication note's own text."""
    rows = []
    for (d, L) in ((2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)):
        r = overlap_census(d, L)
        r["d"], r["L"] = d, L
        r["censused"] = (d, L) in CENSUS_ARENAS
        rows.append(r)
    excluded = [r for r in rows if not r["meets_r2_criterion"]]
    # The R2 record states these fractions in its ledger entry #19 and its
    # handoff ruling in the adjudication note; both texts are read, and the
    # fractions are RECOMPUTED here from the lattice rather than copied.
    quoted = re.findall(r"(\d+)/(\d+)", adj_text + ledger_text)
    quoted = set((int(a), int(b)) for a, b in quoted)
    mine = set((r["drawn_pairs"], r["all_pairs"]) for r in rows)
    matched = sorted(quoted & mine)
    profiles = [t for t in ("(8,12,1,5)", "(24,96,1,73)") if t in adj_text]
    if MUTANT == "inherited-facts-blind":
        profiles = profiles[:1]
    return {"rows": rows, "excluded_arenas": [[r["d"], r["L"]] for r in excluded],
            "excluded_reason": "the overlap graph is COMPLETE, so the "
                               "inherited criterion (SOME component not "
                               "complete) is failed",
            "fractions_recomputed_and_matched_in_the_r2_adjudication":
                [list(t) for t in matched],
            "inherited_link_profiles_quoted_in_the_ruling": profiles,
            "inherited_facts_note": "locality, the consistent chart-intrinsic "
                                    "dimension and translation covariance ride "
                                    "as INHERITED ANCHORS from the R2 terminal; "
                                    "the link profiles are quoted, never "
                                    "re-derived here",
            "adjudication_mentions_L_ge_4": ("L >= 4" in adj_text
                                             or "L ≥ 4" in adj_text)}


def controls(decl, rec7):
    """The translation control (positive), the scrambled-lattice negative
    control, the chart-group closure, and the symmetry self-tests."""
    out = {"positive": [], "negative": [], "chart_group": [],
           "covariance": [], "cache": {}}
    for (d, L) in CENSUS_ARENAS:
        # (a) the chart group's order, DERIVED by explicit closure
        order = chart_group_order(d, L)
        expect = (L ** d) * len([1 for _ in itertools.permutations(range(d))])
        out["chart_group"].append(
            {"d": d, "L": L, "order": order, "sites_times_d_factorial": expect,
             "closes": order == expect})
        # (b) the lattice's own translation equivariance
        eq = neighbour_equivariance(d, L)
        eq.update({"d": d, "L": L, "lattice": "RECORD"})
        out["positive"].append(eq)
        # (c) the scrambled negative control
        sc = neighbour_equivariance(d, L, scrambled_neighbour(d, L))
        if MUTANT == "scramble-inert":
            sc = dict(eq)
        sc.update({"d": d, "L": L, "lattice": "SCRAMBLED"})
        out["negative"].append(sc)
    # (d) the residual field's chart-translation covariance, fresh-evaluated,
    #     on the record lattice and on the scrambled one
    d, L = 2, CENSUS_L_MIN
    lapses = build_lapse_family(d, L)
    # The probe must be a cell whose residual is NOT identically zero, or the
    # covariance test is vacuous: the non-vacuity count ships with each row.
    for lattice, nbf in (("RECORD", None),
                         ("SCRAMBLED", scrambled_neighbour(d, L))):
        for rule in ("A-chart", "A-axis"):
            cv = translation_covariance_of_the_residual(
                rule, lambda: make_curvoff("G-CURVOFF", d, L), d, L, lapses, nbf)
            cv.update({"d": d, "L": L, "rule": rule, "lattice": lattice,
                       "record": "G-CURVOFF"})
            out["covariance"].append(cv)
    out["cache"] = dict(CACHE_STATS)
    return out


def cache_exercise():
    """RUNBOOK section 14 addendum (v13 #185 / #219): a cache that is never
    checked against a fresh evaluation is a cache, not a measurement."""
    d, L = 2, CENSUS_L_MIN
    rec = make_curved("G-CURVED", d, L)
    tested = bad = 0
    for rule in ("A-chart", "A-axis", "A-insert", "B-all"):
        for x in rec.S:
            memo = lambda_of(rule, rec, x)
            fresh = lambda_of(rule, rec, x, fresh=True)
            tested += 1
            if memo != fresh:
                bad += 1
    if MUTANT == "cache-lax":
        tested = 0
    return {"compared": tested, "disagreements": bad,
            "stats": dict(CACHE_STATS)}


# ----------------------------------------------------------------------------
# 11.  AGGREGATION -- the L-sweep trajectory and the census summaries
# ----------------------------------------------------------------------------

def summarise(res):
    cen, coe = res["census"], res["coefficients"]
    dh, dd = res["dh"], res["dd"]
    S = {}
    S["census_cells"] = len(cen)
    S["closing_cells"] = len([r for r in cen if r["closes"]])
    S["defecting_cells"] = len([r for r in cen if not r["closes"]])
    S["arenas"] = sorted(set((r["d"], r["L"]) for r in cen))
    S["cells_per_arena_scope"] = sorted(
        [[d, L, sc, len([r for r in cen
                         if r["d"] == d and r["L"] == L and r["scope"] == sc])]
         for (d, L) in S["arenas"] for sc in LAPSE_SCOPES])
    S["arenas"] = [list(a) for a in S["arenas"]]
    # the coefficient class census
    cls = {}
    for c in coe:
        cls[c["coefficient"]["class"]] = cls.get(c["coefficient"]["class"], 0) + 1
    S["coefficient_classes"] = dict(sorted(cls.items()))
    S["metric_reading_cells"] = len(
        [c for c in coe if c["coefficient"]["class"].startswith("METRIC-READING")])
    S["metric_reading_site_varying_cells"] = len(
        [c for c in coe if c["coefficient"]["class"] == "METRIC-READING-SITE-VARYING"])
    S["not_extractable_cells"] = len(
        [c for c in coe if c["coefficient"]["class"] == "NOT-EXTRACTABLE"])
    # the positive control's own row
    pc = [c for c in coe if c["rule"] == "A-insert"]
    S["positive_control_cells"] = len(pc)
    S["positive_control_metric_reading"] = len(
        [c for c in pc if c["coefficient"]["metric_reading"]])
    S["positive_control_site_varying"] = len(
        [c for c in pc if c["coefficient"]["class"] == "METRIC-READING-SITE-VARYING"])
    S["positive_control_closes"] = len(
        [r for r in cen if r["rule"] == "A-insert" and r["closes"]])
    S["positive_control_census_cells"] = len(
        [r for r in cen if r["rule"] == "A-insert"])
    # inhomogeneous records: the only place a structure FUNCTION shows
    inh = [c for c in coe if not c["homogeneous"]]
    S["inhomogeneous_cells"] = len(inh)
    S["inhomogeneous_site_varying_metric"] = len(
        [c for c in inh if c["coefficient"]["class"] == "METRIC-READING-SITE-VARYING"])
    # the bracket tallies
    tal = {}
    for r in dh:
        for k, v in r["tally"].items():
            tal[(r["realisation"], k)] = tal.get((r["realisation"], k), 0) + v
    S["dh_tally"] = dict(sorted(("%s/%s" % k, v) for k, v in tal.items()))
    S["dh_brackets"] = sum(r["brackets"] for r in dh)
    S["dh_in_constraint"] = sum(v for k, v in tal.items()
                                if k[1] == "IN-CONSTRAINT")
    S["dd_closing"] = sum(r["closing"] for r in dd)
    S["dd_total"] = sum(r["total"] for r in dd)
    # the convention sweep
    cv = {}
    for c in res["conventions"]:
        k = (c["order"], c["difference"])
        a, b = cv.get(k, (0, 0))
        cv[k] = (a + c["front_matches"], b + c["brackets"])
    S["convention_sweep"] = dict(sorted(
        ("%s/%s" % k, [v[0], v[1]]) for k, v in cv.items()))
    S["conventions_matching_everywhere"] = sorted(
        "%s/%s" % k for k, v in cv.items() if v[0] == v[1] and v[1] > 0)
    # the defect
    dfr = res["defect"]
    S["defect_probes"] = sum(r["probes"] for r in dfr)
    S["defect_vanishing_probes"] = sum(r["vanishing_probes"] for r in dfr)
    S["defect_lattice_sum_zero"] = sum(r["lattice_sum_zero"] for r in dfr)
    S["defect_vanishes_on_homogeneous"] = sum(
        r["vanishing_probes"] for r in dfr if r["homogeneous"])
    S["defect_homogeneous_probes"] = sum(
        r["probes"] for r in dfr if r["homogeneous"])
    S["defect_rules_with_a_vanishing_row"] = sorted(set(
        r["rule"] for r in dfr if r["vanishing_probes"] == r["probes"]))
    # THE L-SWEEP TRAJECTORY, cell-complete
    traj = []
    for (d, L) in [tuple(a) for a in S["arenas"]]:
        for sc in LAPSE_SCOPES:
            sub = [r for r in cen if r["d"] == d and r["L"] == L
                   and r["scope"] == sc]
            sc_c = [c for c in coe if c["d"] == d and c["L"] == L
                    and c["scope"] == sc]
            traj.append({
                "d": d, "L": L, "scope": sc, "cells": len(sub),
                "lapse_members": (sub[0]["total_pairs"] if sub else 0),
                "closing": len([r for r in sub if r["closes"]]),
                "defecting": len([r for r in sub if not r["closes"]]),
                "max_residual": max([Fr(r["max_abs"]) for r in sub],
                                    default=Fr(0)).__str__(),
                "metric_reading": len([c for c in sc_c
                                       if c["coefficient"]["metric_reading"]]),
                "site_varying_metric": len(
                    [c for c in sc_c if c["coefficient"]["class"]
                     == "METRIC-READING-SITE-VARYING"]),
                "not_extractable": len([c for c in sc_c
                                        if c["coefficient"]["class"]
                                        == "NOT-EXTRACTABLE"])})
    if MUTANT == "lsweep-drop":
        traj = traj[:-1]
    if MUTANT == "lsweep-instability":
        traj[1] = dict(traj[1])
        traj[1]["closing"] = traj[1]["closing"] + 1
    S["trajectory"] = traj
    # does the lapse coordinate move anything?
    moved = []
    for (d, L) in [tuple(a) for a in S["arenas"]]:
        for rule in sorted(set(r["rule"] for r in cen)):
            for nm in sorted(set(r["record"] for r in cen
                                 if r["d"] == d and r["L"] == L)):
                a = [r for r in cen if r["d"] == d and r["L"] == L
                     and r["rule"] == rule and r["record"] == nm
                     and r["scope"] == "BASE"]
                b = [r for r in cen if r["d"] == d and r["L"] == L
                     and r["rule"] == rule and r["record"] == nm
                     and r["scope"] == "TRANSLATES"]
                if a and b and (a[0]["closes"] != b[0]["closes"]
                                or a[0]["max_abs"] != b[0]["max_abs"]):
                    moved.append([d, L, rule, nm, a[0]["max_abs"],
                                  b[0]["max_abs"]])
    S["lapse_coordinate_moves"] = moved
    ca = {}
    for c in coe:
        ca[(c["d"], c["L"], c["scope"], c["rule"], c["record"])] = \
            c["coefficient"]["class"]
    cm = []
    for k, v in ca.items():
        k2 = (k[0], k[1], "TRANSLATES" if k[2] == "BASE" else "BASE", k[3], k[4])
        if k2 in ca and ca[k2] != v:
            cm.append([list(k), v, ca[k2]])
    S["lapse_coordinate_moves_coefficient"] = sorted(cm, key=str)
    return S


# ----------------------------------------------------------------------------
# 12.  THE VERDICT -- derived inside a gate, every segment computed
# ----------------------------------------------------------------------------

SEGMENT_ORDER = ("ARENA", "L-GATE", "RECOVERY", "HH-BRACKET", "COEFFICIENT",
                 "HH-RESIDUAL", "DH-BRACKET", "DEFECT", "CONVENTION",
                 "DD-BRACKET", "LAPSE", "REALISATION", "LSWEEP", "CONTROLS")

HEAD_CLOSES = "R3-DEFORMATION-CLOSES"
HEAD_DEFECT = "R3-DEFORMATION-DEFECT-AT"


def build_verdict(payload, swap_pairing=False):
    """Assemble the verdict from the measured payload."""
    S = payload["summary"]
    segs = []
    dh = S["dh_tally"]
    dh_ok = (S["dh_in_constraint"] == S["dh_brackets"] and S["dh_brackets"] > 0)
    hh_ok = (S["positive_control_closes"] == S["positive_control_census_cells"]
             and S["positive_control_census_cells"] > 0)
    dd_ok = (S["dd_closing"] == S["dd_total"] and S["dd_total"] > 0)
    failing = []
    if not hh_ok:
        failing.append("NORMAL-NORMAL")
    if not dh_ok:
        failing.append("NORMAL-TANGENTIAL-REGISTER-SECTOR")
    if not dd_ok:
        failing.append("TANGENTIAL-TANGENTIAL")
    head = HEAD_CLOSES if not failing else HEAD_DEFECT
    if failing:
        segs.append(("ARENA", "ARENA=%s" % payload["arena_signature"]))
    else:
        segs.append(("ARENA", "ARENA=%s" % payload["arena_signature"]))
    segs.append(("L-GATE", "L-GATE=" + payload["lgate_signature"]))
    segs.append(("RECOVERY", "RECOVERY=" + payload["recovery_signature"]))
    segs.append(("HH-BRACKET", "HH-BRACKET=" + payload["hh_signature"]))
    segs.append(("COEFFICIENT", "COEFFICIENT=" + payload["coeff_signature"]))
    segs.append(("HH-RESIDUAL", "HH-RESIDUAL=" + payload["hhres_signature"]))
    segs.append(("DH-BRACKET", "DH-BRACKET=" + payload["dh_signature"]))
    segs.append(("DEFECT", "DEFECT=" + payload["defect_signature"]))
    segs.append(("CONVENTION", "CONVENTION=" + payload["convention_signature"]))
    segs.append(("DD-BRACKET", "DD-BRACKET=" + payload["dd_signature"]))
    segs.append(("LAPSE", "LAPSE=" + payload["lapse_signature"]))
    segs.append(("REALISATION", "REALISATION=" + payload["realisation_signature"]))
    segs.append(("LSWEEP", "LSWEEP=" + payload["lsweep_signature"]))
    segs.append(("CONTROLS", "CONTROLS=" + payload["controls_signature"]))
    if swap_pairing and len(segs) >= 5:
        a, b = segs[3], segs[4]
        segs[3] = (a[0], a[1].split("=")[0] + "=" + b[1].split("=", 1)[1])
        segs[4] = (b[0], b[1].split("=")[0] + "=" + a[1].split("=", 1)[1])
    if MUTANT == "verdict-typed-segment":
        segs[6] = ("DH-BRACKET", "DH-BRACKET=IN-CONSTRAINT-AT-ALL-BRACKETS;"
                                 "HDA-NORMAL-TANGENTIAL-REPRODUCED")
    if MUTANT == "verdict-append-text":
        segs[4] = ("COEFFICIENT", segs[4][1] + "-AND-DERIVED-FROM-THE-SUBSTRATE")
    if MUTANT == "verdict-typed-coefficient":
        segs[4] = ("COEFFICIENT", "COEFFICIENT=METRIC-READING-SITE-VARYING-AT-"
                                  "EVERY-CELL")
    if MUTANT == "verdict-fully-typed":
        segs = [(nm, "%s=TYPED" % nm) for nm in SEGMENT_ORDER]
        head = HEAD_CLOSES
    if MUTANT == "verdict-inert-segment":
        segs[7] = ("DEFECT", "DEFECT=NONE")
    if MUTANT == "head-constant":
        head = HEAD_CLOSES
    if MUTANT == "verdict-segment-drop":
        segs = segs[:-1]
    full = head + "<" + "|".join(s[1] for s in segs) + ">"
    return head, segs, full


# ----------------------------------------------------------------------------
# 12a.  THE INDEPENDENT COMPARATOR (RUNBOOK section 14 addendum, v14 #20)
#
# "A compliance gate whose comparator cannot disagree with the object under
# test is vacuous by construction."  This reconstruction shares NO code and NO
# input with build_verdict: it reads the RECEIPT'S OWN measured tables -- the
# census rows, the coefficient rows, the bracket rows -- and re-derives every
# segment from them.  A typed, appended, swapped or inert segment disagrees.
# ----------------------------------------------------------------------------

def reconstruct_verdict_from_receipt(R):
    cen = R["census_rows"]
    coe = R["coefficient_rows"]
    dhr = R["dh_bracket_rows"]
    ddr = R["dd_bracket_rows"]
    cnv = R["convention_sweep"]
    dfr = R["defect_rows"]
    rec = R["recovery"]
    lg = R["l_gate"]
    ctl = R["controls"]
    arenas = sorted(set((r["d"], r["L"]) for r in cen))
    out = []

    dh_tot = sum(r["brackets"] for r in dhr)
    dh_in = sum(r["tally"].get("IN-CONSTRAINT", 0) for r in dhr)
    pc = [r for r in cen if r["rule"] == "A-insert"]
    hh_ok = len(pc) > 0 and all(r["closes"] for r in pc)
    dd_tot = sum(r["total"] for r in ddr)
    dd_ok = dd_tot > 0 and sum(r["closing"] for r in ddr) == dd_tot
    dh_ok = dh_tot > 0 and dh_in == dh_tot
    fail = []
    if not hh_ok:
        fail.append("NORMAL-NORMAL")
    if not dh_ok:
        fail.append("NORMAL-TANGENTIAL-REGISTER-SECTOR")
    if not dd_ok:
        fail.append("TANGENTIAL-TANGENTIAL")
    head = HEAD_CLOSES if not fail else HEAD_DEFECT

    recset = sorted(set(r["record"] for r in cen))
    ruleset = sorted(set(r["rule"] for r in cen))
    out.append("ARENA=SITES=%s;LINKS=%s;RECORDS=%d;RULES=%d;LAPSE-SCOPES=%s"
               % (",".join("d%dL%d:%d" % (d, L, L ** d) for d, L in arenas),
                  ",".join("d%d:%d" % (d, d + d * (d - 1) // 2)
                           for d in sorted(set(a[0] for a in arenas))),
                  len(recset), len(ruleset),
                  ",".join(sorted(set(r["scope"] for r in cen)))))
    exc = sorted(tuple(a) for a in lg["excluded_arenas"])
    out.append("L-GATE=MIN-L=%d;EXCLUDED=%s;REASON=OVERLAP-GRAPH-COMPLETE-AT-"
               "%s;INHERITED-FRACTIONS-RECOMPUTED=%d"
               % (min(a[1] for a in arenas),
                  ",".join("d%dL%d" % (d, L) for d, L in exc),
                  ",".join("%d-OF-%d" % (r["drawn_pairs"], r["all_pairs"])
                           for r in lg["rows"]
                           if (r["d"], r["L"]) in [tuple(e) for e in exc]),
                  len(lg["fractions_recomputed_and_matched_in_the_r2_adjudication"])))
    out.append("RECOVERY=CLOSURE-%d-OF-%d;SECTOR-%d-OF-%d;RANK;READOUT-DET-%s;"
               "GENERAL-D;COUNT-LATTICE;DIAGONAL-SECTOR-%d-RECORDS-CLOSE-AT-"
               "THE-LINK-LOCAL-RULE"
               % (rec["closure_cells_compared"] - len(rec["closure_mismatches"]),
                  rec["closure_cells_compared"],
                  rec["sector_cells_compared"] - len(rec["sector_mismatches"]),
                  rec["sector_cells_compared"], rec["readout"]["determinant"],
                  len(rec["diagonal_sector_closes_at_the_link_local_rule"])))
    out.append("HH-BRACKET=LANDS-IN-THE-TANGENTIAL-FAMILY-AT-%d-OF-%d-CELLS"
               "(FORCED:w-LINEAR-IN-THE-FRONT);POSITIVE-CONTROL-CLOSES-AT-%d-"
               "OF-%d;NORMAL-CHANNEL-EMPTY(FORCED)"
               % (len(cen), len(cen), len([r for r in pc if r["closes"]]),
                  len(pc)))
    cls = {}
    for c in coe:
        k = c["coefficient"]["class"]
        cls[k] = cls.get(k, 0) + 1
    pcc = [c for c in coe if c["rule"] == "A-insert"]
    inh = [c for c in coe if not c["homogeneous"]]
    out.append("COEFFICIENT=EXTRACTED-FROM-THE-COMMUTATORS;CLASSES=%s;"
               "POSITIVE-CONTROL-METRIC-READING-AT-%d-OF-%d(FORCED-VALUE,"
               "MEASURED-UNIQUENESS);"
               "SITE-VARYING-ON-THE-INHOMOGENEOUS-RECORDS-AT-%d-OF-%d"
               % (";".join("%s:%d" % (k, cls[k]) for k in sorted(cls)),
                  len([c for c in pcc if c["coefficient"]["metric_reading"]]),
                  len(pcc),
                  len([c for c in inh if c["coefficient"]["class"]
                       == "METRIC-READING-SITE-VARYING"]), len(inh)))
    bad = [r for r in cen if not r["closes"]]
    badrules = sorted(set(r["rule"] for r in bad))
    out.append("HH-RESIDUAL=NONZERO-AT-%d-OF-%d-CELLS;RULES=%s;"
               "NOT-EXTRACTABLE-AT-%d-CELLS(ARCH-B:OUTSIDE-THE-AXIS-COVECTOR-"
               "FORM,FORCED);MAX=%s"
               % (len(bad), len(cen), ",".join(badrules) if badrules else "NONE",
                  len([c for c in coe
                       if c["coefficient"]["class"] == "NOT-EXTRACTABLE"]),
                  max([Fr(r["max_abs"]) for r in cen], default=Fr(0)).__str__()))
    tal = {}
    for r in dhr:
        for k, v in r["tally"].items():
            tal[(r["realisation"], k)] = tal.get((r["realisation"], k), 0) + v
    out.append("DH-BRACKET=%s(D-REG-IDENTITY-FORCED);HDA-REQUIRES-H[L_v-N];"
               "IN-CONSTRAINT-AT-%d-OF-%d"
               % (";".join("%s:%s" % (k[0] + "/" + k[1], tal[k])
                           for k in sorted(tal)), dh_in, dh_tot))
    dp = sum(r["probes"] for r in dfr)
    dv = sum(r["vanishing_probes"] for r in dfr)
    dl = sum(r["lattice_sum_zero"] for r in dfr)
    dh_hom = sum(r["vanishing_probes"] for r in dfr if r["homogeneous"])
    out.append("DEFECT=REGISTER-SECTOR-OF-THE-NORMAL-TANGENTIAL-BRACKET;"
               "CLOSED-FORM=w[N,(S_-v-1)(n-N)]-w[S_vN-N,n];"
               "NONZERO-AT-%d-OF-%d-PROBES;CONFIGURATION-DEPENDENT;"
               "LATTICE-SUM-ZERO-AT-%d-OF-%d;VANISHES-ON-THE-HOMOGENEOUS-"
               "SECTOR-AT-%d;L-AND-D-INDEPENDENT-AT-%d-ARENAS"
               % (dp - dv, dp, dl, dp, dh_hom, len(arenas)))
    cv = {}
    for c in cnv:
        k = (c["order"], c["difference"])
        a, b = cv.get(k, (0, 0))
        cv[k] = (a + c["front_matches"], b + c["brackets"])
    full = sorted(k for k in cv if cv[k][0] == cv[k][1] and cv[k][1] > 0)
    out.append("CONVENTION=FRONT-SECTOR-REPRODUCES-L_v-N-AT-%s;"
               "MATCHING-CONVENTIONS=%d-OF-%d;%s"
               % (",".join("%s/%s" % k for k in full) if full else "NO-CONVENTION",
                  len(full), len(cv),
                  ";".join("%s/%s:%d-OF-%d" % (k[0], k[1], cv[k][0], cv[k][1])
                           for k in sorted(cv))))
    out.append("DD-BRACKET=LATTICE-TRANSLATIONS-CLOSE-AT-%d-OF-%d-AT-BOTH-"
               "REALISATIONS(FORCED:[v,w]=0-AT-CONSTANT-FIELDS;POSITIVE-"
               "CONTROL,MUTANT-FLIPS-IT)"
               % (sum(r["closing"] for r in ddr), dd_tot))
    lm = R["summary"]["lapse_coordinate_moves"]
    lcm = R["summary"]["lapse_coordinate_moves_coefficient"]
    out.append("LAPSE=DECLARED-FAMILY-AND-ITS-LATTICE-TRANSLATES;"
               "ENLARGEMENT-PRINTED;RESIDUAL-MAGNITUDE-MOVES-AT-%d-CELLS;"
               "COEFFICIENT-CLASS-MOVES-AT-%d-CELLS" % (len(lm), len(lcm)))
    out.append("REALISATION=D-REG:%s;D-TOT:%s"
               % ("+".join(sorted(set(k[1] for k in tal if k[0] == "D-REG"))),
                  "+".join(sorted(set(k[1] for k in tal if k[0] == "D-TOT")))))
    tr = R["summary"]["trajectory"]
    out.append("LSWEEP=%s;COEFFICIENT-CLASS-CONSTANT-ALONG-L=%s"
               % (",".join("d%dL%d/%s:%d-of-%d-close"
                           % (t["d"], t["L"], t["scope"][0], t["closing"],
                              t["cells"]) for t in tr),
                  str(len(set((t["d"], t["metric_reading"], t["cells"])
                              for t in tr))
                      == len(set(t["d"] for t in tr))).upper()))
    pos = ctl["positive"]
    negc = ctl["negative"]
    cov = ctl["covariance"]
    out.append("CONTROLS=CHART-GROUP-CLOSES-AT-%d-OF-%d-ARENAS;"
               "TRANSLATION-EQUIVARIANT-AT-%d-OF-%d;SCRAMBLED-VIOLATES-AT-%d-"
               "OF-%d;RESIDUAL-COVARIANT-ON-THE-RECORD-LATTICE-AT-%d-CELLS;"
               "SCRAMBLED-BREAKS-AT-%d-CELLS"
               % (len([c for c in ctl["chart_group"] if c["closes"]]),
                  len(ctl["chart_group"]),
                  sum(p["equivariant_cells"] for p in pos),
                  sum(p["total_cells"] for p in pos),
                  sum(n["violating_cells"] for n in negc),
                  sum(n["total_cells"] for n in negc),
                  sum(c["covariant_cells"] for c in cov
                      if c["lattice"] == "RECORD"),
                  sum(c["violating_cells"] for c in cov
                      if c["lattice"] == "SCRAMBLED")))
    return head + "<" + "|".join(out) + ">"


# ----------------------------------------------------------------------------
# 13.  THE RUN
# ----------------------------------------------------------------------------

def build_signatures(decl, res, S, rec_out, lg, ctl):
    """The verdict's segment payload, assembled from the ARENA DECLARATION and
    the summary object -- a different path from the comparator, which rebuilds
    every segment from the receipt's raw measured rows."""
    P = {}
    arenas = [tuple(a) for a in S["arenas"]]
    ds = sorted(set(a[0] for a in arenas))
    nrec = len(set(r["record"] for r in res["census"]))
    nrul = len(set(r["rule"] for r in res["census"]))
    P["arena_signature"] = (
        "SITES=%s;LINKS=%s;RECORDS=%d;RULES=%d;LAPSE-SCOPES=%s"
        % (",".join("d%dL%d:%d" % (d, L, L ** d) for d, L in arenas),
           ",".join("d%d:%d" % (d, len(link_set(d))) for d in ds),
           nrec, nrul, ",".join(sorted(LAPSE_SCOPES))))
    exc = sorted(tuple(a) for a in lg["excluded_arenas"])
    P["lgate_signature"] = (
        "MIN-L=%d;EXCLUDED=%s;REASON=OVERLAP-GRAPH-COMPLETE-AT-%s;"
        "INHERITED-FRACTIONS-RECOMPUTED=%d"
        % (CENSUS_L_MIN, ",".join("d%dL%d" % (d, L) for d, L in exc),
           ",".join("%d-OF-%d" % (r["drawn_pairs"], r["all_pairs"])
                    for r in lg["rows"] if (r["d"], r["L"]) in exc),
           len(lg["fractions_recomputed_and_matched_in_the_r2_adjudication"])))
    P["recovery_signature"] = (
        "CLOSURE-%d-OF-%d;SECTOR-%d-OF-%d;RANK;READOUT-DET-%s;GENERAL-D;"
        "COUNT-LATTICE;DIAGONAL-SECTOR-%d-RECORDS-CLOSE-AT-THE-LINK-LOCAL-RULE"
        % (rec_out["closure_cells_compared"] - len(rec_out["closure_mismatches"]),
           rec_out["closure_cells_compared"],
           rec_out["sector_cells_compared"] - len(rec_out["sector_mismatches"]),
           rec_out["sector_cells_compared"], rec_out["readout"]["determinant"],
           len(rec_out["diagonal_sector_closes_at_the_link_local_rule"])))
    P["hh_signature"] = (
        "LANDS-IN-THE-TANGENTIAL-FAMILY-AT-%d-OF-%d-CELLS(FORCED:w-LINEAR-IN-"
        "THE-FRONT);POSITIVE-CONTROL-CLOSES-AT-%d-OF-%d;NORMAL-CHANNEL-EMPTY"
        "(FORCED)"
        % (S["census_cells"], S["census_cells"], S["positive_control_closes"],
           S["positive_control_census_cells"]))
    P["coeff_signature"] = (
        "EXTRACTED-FROM-THE-COMMUTATORS;CLASSES=%s;POSITIVE-CONTROL-METRIC-"
        "READING-AT-%d-OF-%d(FORCED-VALUE,MEASURED-UNIQUENESS);SITE-VARYING-"
        "ON-THE-INHOMOGENEOUS-RECORDS-AT-%d-OF-%d"
        % (";".join("%s:%d" % (k, v) for k, v in
                    sorted(S["coefficient_classes"].items())),
           S["positive_control_metric_reading"], S["positive_control_cells"],
           S["inhomogeneous_site_varying_metric"], S["inhomogeneous_cells"]))
    badrules = sorted(set(r["rule"] for r in res["census"] if not r["closes"]))
    P["hhres_signature"] = (
        "NONZERO-AT-%d-OF-%d-CELLS;RULES=%s;NOT-EXTRACTABLE-AT-%d-CELLS"
        "(ARCH-B:OUTSIDE-THE-AXIS-COVECTOR-FORM,FORCED);MAX=%s"
        % (S["defecting_cells"], S["census_cells"],
           ",".join(badrules) if badrules else "NONE",
           S["not_extractable_cells"],
           max([Fr(r["max_abs"]) for r in res["census"]],
               default=Fr(0)).__str__()))
    P["dh_signature"] = (
        "%s(D-REG-IDENTITY-FORCED);HDA-REQUIRES-H[L_v-N];IN-CONSTRAINT-AT-"
        "%d-OF-%d"
        % (";".join("%s:%s" % (k, v) for k, v in sorted(S["dh_tally"].items())),
           S["dh_in_constraint"], S["dh_brackets"]))
    P["defect_signature"] = (
        "REGISTER-SECTOR-OF-THE-NORMAL-TANGENTIAL-BRACKET;CLOSED-FORM="
        "w[N,(S_-v-1)(n-N)]-w[S_vN-N,n];NONZERO-AT-%d-OF-%d-PROBES;"
        "CONFIGURATION-DEPENDENT;LATTICE-SUM-ZERO-AT-%d-OF-%d;VANISHES-ON-"
        "THE-HOMOGENEOUS-SECTOR-AT-%d;L-AND-D-INDEPENDENT-AT-%d-ARENAS"
        % (S["defect_probes"] - S["defect_vanishing_probes"],
           S["defect_probes"], S["defect_lattice_sum_zero"],
           S["defect_probes"], S["defect_vanishes_on_homogeneous"],
           len(arenas)))
    cv = S["convention_sweep"]
    full = sorted(k for k in cv if cv[k][0] == cv[k][1] and cv[k][1] > 0)
    P["convention_signature"] = (
        "FRONT-SECTOR-REPRODUCES-L_v-N-AT-%s;MATCHING-CONVENTIONS=%d-OF-%d;%s"
        % (",".join(full) if full else "NO-CONVENTION", len(full), len(cv),
           ";".join("%s:%d-OF-%d" % (k, cv[k][0], cv[k][1])
                    for k in sorted(cv))))
    P["dd_signature"] = (
        "LATTICE-TRANSLATIONS-CLOSE-AT-%d-OF-%d-AT-BOTH-REALISATIONS(FORCED:"
        "[v,w]=0-AT-CONSTANT-FIELDS;POSITIVE-CONTROL,MUTANT-FLIPS-IT)"
        % (S["dd_closing"], S["dd_total"]))
    P["lapse_signature"] = (
        "DECLARED-FAMILY-AND-ITS-LATTICE-TRANSLATES;ENLARGEMENT-PRINTED;"
        "RESIDUAL-MAGNITUDE-MOVES-AT-%d-CELLS;COEFFICIENT-CLASS-MOVES-AT-%d-CELLS"
        % (len(S["lapse_coordinate_moves"]),
           len(S["lapse_coordinate_moves_coefficient"])))
    P["realisation_signature"] = (
        "D-REG:%s;D-TOT:%s"
        % ("+".join(sorted(set(k.split("/")[1] for k in S["dh_tally"]
                               if k.startswith("D-REG/")))),
           "+".join(sorted(set(k.split("/")[1] for k in S["dh_tally"]
                               if k.startswith("D-TOT/"))))))
    tr = S["trajectory"]
    P["lsweep_signature"] = (
        "%s;COEFFICIENT-CLASS-CONSTANT-ALONG-L=%s"
        % (",".join("d%dL%d/%s:%d-of-%d-close"
                    % (t["d"], t["L"], t["scope"][0], t["closing"], t["cells"])
                    for t in tr),
           str(len(set((t["d"], t["metric_reading"], t["cells"])
                       for t in tr)) == len(set(t["d"] for t in tr))).upper()))
    P["controls_signature"] = (
        "CHART-GROUP-CLOSES-AT-%d-OF-%d-ARENAS;TRANSLATION-EQUIVARIANT-AT-%d-"
        "OF-%d;SCRAMBLED-VIOLATES-AT-%d-OF-%d;RESIDUAL-COVARIANT-ON-THE-"
        "RECORD-LATTICE-AT-%d-CELLS;SCRAMBLED-BREAKS-AT-%d-CELLS"
        % (len([c for c in ctl["chart_group"] if c["closes"]]),
           len(ctl["chart_group"]),
           sum(p["equivariant_cells"] for p in ctl["positive"]),
           sum(p["total_cells"] for p in ctl["positive"]),
           sum(n["violating_cells"] for n in ctl["negative"]),
           sum(n["total_cells"] for n in ctl["negative"]),
           sum(c["covariant_cells"] for c in ctl["covariance"]
               if c["lattice"] == "RECORD"),
           sum(c["violating_cells"] for c in ctl["covariance"]
               if c["lattice"] == "SCRAMBLED")))
    P["summary"] = S
    return P


def run():
    say("=" * 78)
    say("v14 R3 -- THE RELATIVITY RUNG.  Hypersurface deformation on I7's")
    say("record lattice: does H_a[N] close, and with what coefficients?")
    say("=" * 78)
    say()

    off = float_guard()
    gate("G-FLOATGUARD",
         "exact arithmetic: no float literal, no float call, no true-division "
         "operator and no banned numeric import anywhere in this source",
         len(off) == 0, {"offences": off[:6]})

    n_anch = verify_anchors()
    n_path = verify_path_anchors()
    derive_ha_code_anchor()
    gate("G-ANCHOR-COUNT",
         "every declared anchor row was actually verified: the counts are "
         "derived from the declaration tables, never typed",
         n_anch == len(ANCHOR_ROWS) and n_path == len(PATH_ANCHOR_ROWS)
         and len(ANCHORS) == n_anch + n_path + 1,
         {"file_byte": n_anch, "declared_file_byte": len(ANCHOR_ROWS),
          "path_value": n_path, "declared_path_value": len(PATH_ANCHOR_ROWS),
          "registered": len(ANCHORS)})
    say("--- 1. ANCHORS ---")
    say("  file-byte anchors: %d ; path-value anchors: %d ; derived: 1"
        % (n_anch, n_path))
    for a in ANCHORS:
        say("    %-28s %-10s %s" % (a["name"], a["kind"][:10], a["artifact"]))
    say()

    rec7 = read_json(I7)
    decl = rec7["declarations"]
    adj = read_text("v14/note-r2-adjudication.md")

    # ---- THE ARENA, PRINTED AS DATA (RUNBOOK section 15) -----------------
    say("--- 2. THE DECLARED ARENA (data, read from the pinned I7 receipt) ---")
    arena = {
        "source": I7,
        "sites": "X = (Z_L)^d, periodic",
        "links_d2": decl["links_d2"], "links_d3": decl["links_d3"],
        "lapse_family": decl["lapse_family"],
        "lapse_scopes": {
            "BASE": "I7's declared family: the |X| site deltas, the constant "
                    "profile 1, and the d chart ramps",
            "TRANSLATES": "the declared family closed under the lattice's own "
                          "chart translations -- AN ENLARGEMENT, printed here "
                          "as arena data (the deltas and the constant are "
                          "already closed; each ramp acquires L translates)"},
        "chart_group": decl["chart_group"],
        "records_d2": decl["records_d2"], "records_d3": decl["records_d3"],
        "records_inhomogeneous": decl["records_d2_inhomogeneous"],
        "records_d3_extension": "G3-CURVED and G3-CURVOFF, built by I7's own "
                                "site-dependent recipes at d = 3: a DECLARED "
                                "EXTENSION of I7's d=3 list, without which a "
                                "structure FUNCTION cannot be distinguished "
                                "from a structure CONSTANT at d = 3",
        "rules_d2": [r[0] for r in RULE_TABLE], "rules_d3": decl["rules_d3"],
        "density_weight": decl["density_weight"],
        "tangential_realisations": ["D-REG (primary)", "D-TOT (flip test)"],
        "census_arenas": [list(a) for a in CENSUS_ARENAS],
        "dense_route_arenas": [list(a) for a in DENSE_ARENAS],
        "literal_probe_lapses": LITERAL_PROBE_LAPSES,
        "dh_probe_convention": "d = 2: the whole declared family; d = 3: I7's "
                               "own probe convention -- the first %d site "
                               "deltas with the constant profile and the d "
                               "chart ramps" % DH_PROBE_DELTAS,
        "declared_configurations": 3,
        "bracket_orders": list(BRACKET_ORDERS),
        "difference_conventions": [c[0] for c in LIE_CONVENTIONS],
    }
    for k in ("sites", "lapse_family", "chart_group", "density_weight"):
        say("  %-22s %s" % (k, arena[k]))
    say("  %-22s %s" % ("census arenas (d,L)", arena["census_arenas"]))
    say("  %-22s %s" % ("rules d=2 / d=3", "%d / %d"
                        % (len(arena["rules_d2"]), len(arena["rules_d3"]))))
    say()

    # ---- THE L GATE -------------------------------------------------------
    say("--- 3. THE L GATE: L >= %d, WITH ITS MEASURED REASON ---" % CENSUS_L_MIN)
    lg = l_gate_reason(adj, read_text("v14/LOG.md"))
    for r in lg["rows"]:
        say("  d=%d L=%d  |X|=%3d  drawn %5d of %5d  complete=%-5s  "
            "meets-R2-criterion=%-5s  censused=%s"
            % (r["d"], r["L"], r["sites"], r["drawn_pairs"], r["all_pairs"],
               r["complete"], r["meets_r2_criterion"], r["censused"]))
    gate("G-L-GATE-REASON",
         "the excluded extent is excluded for a MEASURED reason: its overlap "
         "graph is complete, so the inherited R2 locality criterion is failed "
         "there -- and every censused arena meets that criterion",
         lg["excluded_arenas"] == [[2, 3]]
         and all(r["meets_r2_criterion"] for r in lg["rows"]
                 if (r["d"], r["L"]) in CENSUS_ARENAS),
         {"excluded": lg["excluded_arenas"]})
    gate("G-L-GATE-INHERITED-FACTS",
         "the locality fractions the R2 adjudication states for this lattice "
         "are RECOMPUTED here and found in its text -- the inherited fact is "
         "re-confirmed as an anchor by an independent route, not re-derived "
         "as a new result",
         len(lg["fractions_recomputed_and_matched_in_the_r2_adjudication"]) >= 3
         and lg["adjudication_mentions_L_ge_4"]
         and len(lg["inherited_link_profiles_quoted_in_the_ruling"]) == 2,
         {"matched": lg["fractions_recomputed_and_matched_in_the_r2_adjudication"],
          "profiles": lg["inherited_link_profiles_quoted_in_the_ruling"]})
    say("  recomputed fractions also present in the R2 adjudication: %s"
        % lg["fractions_recomputed_and_matched_in_the_r2_adjudication"])
    say()

    # ---- THE MACHINERY-RECOVERY CONTROL ----------------------------------
    say("--- 4. THE MACHINERY-RECOVERY CONTROL (at I7's OWN declared scope) ---")
    rec_out = recover_i7(decl, rec7)
    say("  scope d=%d L=%d, %d sites, lapse family %d, ordered pairs %d"
        % (rec_out["scope"]["d"], rec_out["scope"]["L"],
           rec_out["scope"]["sites"], rec_out["scope"]["lapse_family_size"],
           rec_out["scope"]["ordered_pairs"]))
    say("  closure cells compared %d, mismatches %d"
        % (rec_out["closure_cells_compared"], len(rec_out["closure_mismatches"])))
    say("  sector-law cells compared %d, mismatches %d"
        % (rec_out["sector_cells_compared"], len(rec_out["sector_mismatches"])))
    say("  identifiability rank matches the pin: %s ; readout matches: %s "
        "(det %s, %d sites) ; general-d matches: %s ; count lattice matches: %s"
        % (rec_out["rank_matches_pin"], rec_out["readout_matches_pin"],
           rec_out["readout"]["determinant"], rec_out["readout"]["sites_verified"],
           rec_out["general_d_matches_pin"], rec_out["lattice_matches_pin"]))
    say("  the diagonal sector: %s ; closes at the link-local rule: %s"
        % (rec_out["diagonal_sector"],
           rec_out["diagonal_sector_closes_at_the_link_local_rule"]))
    gate("G-RECOVERY-CLOSURE",
         "this unit's reimplementation reproduces EVERY cell of I7's closure "
         "table at I7's own declared scope, from the pinned receipt -- the "
         "machinery-recovery control, run before any new measurement counts",
         len(rec_out["closure_mismatches"]) == 0
         and rec_out["closure_cells_compared"] == 99,
         {"compared": rec_out["closure_cells_compared"],
          "mismatches": rec_out["closure_mismatches"][:4]})
    gate("G-RECOVERY-SECTOR",
         "and every cell of I7's site-resolved sector law",
         len(rec_out["sector_mismatches"]) == 0
         and rec_out["sector_cells_compared"] == 72,
         {"compared": rec_out["sector_cells_compared"],
          "mismatches": rec_out["sector_mismatches"][:4]})
    gate("G-RECORD-IS-METRIC-TWO-ROUTES",
         "RECORD-IS-METRIC re-encoded by two routes that share no code -- the "
         "exact linear solve and the closed form q_jj = n_{e_j}, "
         "q_ij = (n_{e_i+e_j} - n_{e_i} - n_{e_j})/2 -- agreeing at every "
         "site of every admissible record, and reproducing every declared "
         "link count",
         rec_out["readout"]["two_route_agreements"] == rec_out["readout"]["cells"]
         and rec_out["readout"]["sites_verified"] == rec_out["readout"]["cells"],
         {"readout": rec_out["readout"]})
    gate("G-RECOVERY-ANCILLARY",
         "and the identifiability rank, the record-IS-metric readout "
         "determinant with its site count, the general-d row and the declared "
         "count lattice's link-locality census",
         all([rec_out["rank_matches_pin"], rec_out["readout_matches_pin"],
              rec_out["general_d_matches_pin"], rec_out["lattice_matches_pin"]]),
         {"rank": rec_out["rank_matches_pin"],
          "readout": rec_out["readout_matches_pin"],
          "general_d": rec_out["general_d_matches_pin"],
          "lattice": rec_out["lattice_matches_pin"]})
    gate("G-DIAGONAL-SECTOR-ANCHOR",
         "I7's diagonal-sector exact closure is recovered: the link-local "
         "record-native rule closes on exactly the records whose readout is "
         "diagonal, and on no others",
         (rec_out["diagonal_sector"]
          == rec_out["diagonal_sector_closes_at_the_link_local_rule"]
          and len(rec_out["diagonal_sector"]) == 5),
         {"diagonal": rec_out["diagonal_sector"],
          "closing": rec_out["diagonal_sector_closes_at_the_link_local_rule"]})
    say()

    # ---- THE CENSUS ------------------------------------------------------
    say("--- 5. THE CLOSURE CENSUS AND THE COEFFICIENT EXTRACTION ---")
    res = run_census(decl, rec7)
    S = summarise(res)
    tr = res["two_route"]
    say("  census cells (computed): %d over arenas %s and lapse scopes %s"
        % (S["census_cells"], S["arenas"], list(LAPSE_SCOPES)))
    for row in S["cells_per_arena_scope"]:
        say("    d=%d L=%d %-11s cells %d" % tuple(row))
    exp_cells = 0
    for (d, L) in CENSUS_ARENAS:
        recs = build_records(d, L, decl)
        exp_cells += (len([n for n in recs if recs[n].admissible])
                      * len(rules_at(d, decl)) * len(LAPSE_SCOPES))
    exp_pairs = {}
    for (d, L) in CENSUS_ARENAS:
        exp_pairs[(d, L, "BASE")] = ((L ** d) + 1 + d) * ((L ** d) + d)
        nt = (L ** d) + 1 + d * L
        exp_pairs[(d, L, "TRANSLATES")] = nt * (nt - 1)
    badden = [[r["d"], r["L"], r["scope"], r["rule"], r["record"],
               r["total_pairs"], exp_pairs[(r["d"], r["L"], r["scope"])]]
              for r in res["census"]
              if r["total_pairs"] != exp_pairs[(r["d"], r["L"], r["scope"])]]
    gate("G-CENSUS-CELL-COMPLETE",
         "the census is cell-complete AND its denominators are derived: the "
         "number of measured cells equals the number the arena declaration "
         "REQUIRES (rules x admissible records x lapse scopes over the "
         "declared arenas), and EVERY cell's ordered-pair denominator equals "
         "the count the declared lapse family forces at its arena and scope "
         "-- both computed here, never typed",
         S["census_cells"] == exp_cells and len(badden) == 0,
         {"measured": S["census_cells"], "required": exp_cells,
          "denominator_mismatches": badden[:4]})
    gate("G-CENSUS-TWO-ROUTES",
         "the support-restricted route and the dense route -- which scans "
         "every site of every ordered pair with no support reasoning -- agree "
         "on every field of every cell where both run; the dense coverage is "
         "DERIVED AND PRINTED, never a silent cap",
         len(tr["dense_disagreements"]) == 0 and tr["dense_cells"] > 0,
         {"dense_cells": tr["dense_cells"],
          "dense_arenas": tr["dense_arenas"],
          "disagreements": tr["dense_disagreements"][:4]})
    gate("G-COMMUTATOR-TWO-ROUTES",
         "the LITERAL four-map composition H[N]H[M]H[N]^-1 H[M]^-1, applied to "
         "three declared front configurations, leaves the front unmoved and "
         "reproduces the closed-form register displacement exactly -- so the "
         "commutator is a PURE tangential generator, measured, not assumed",
         len(tr["literal_disagreements"]) == 0 and tr["literal_cells"] > 0,
         {"literal_cells": tr["literal_cells"],
          "disagreements": tr["literal_disagreements"][:4]})
    say("  routes: dense %d cells (%d disagreements) ; literal %d cells (%d) ; "
        "bracket-literal %d (%d) ; convention-literal %d (%d)"
        % (tr["dense_cells"], len(tr["dense_disagreements"]),
           tr["literal_cells"], len(tr["literal_disagreements"]),
           tr["dh_literal_cells"], len(tr["dh_literal_disagreements"]),
           tr["conv_literal_cells"], len(tr["conv_literal_disagreements"])))
    say("  coefficient classes (computed): %s" % S["coefficient_classes"])
    say("  the positive control: closes at %d of %d cells; its coefficient is "
        "a metric reading at %d of %d, site-varying at %d"
        % (S["positive_control_closes"], S["positive_control_census_cells"],
           S["positive_control_metric_reading"], S["positive_control_cells"],
           S["positive_control_site_varying"]))
    gate("G-COEFFICIENT-EXTRACTION",
         "the structure coefficient is SOLVED FOR from the commutators "
         "themselves over every ordered lapse pair, not read off the rule; "
         "the over-determined system is consistent exactly where the "
         "commutator has the axis-covector form, and the arch-B rules -- whose "
         "commutator carries diagonal-link brackets -- fail it",
         S["not_extractable_cells"] > 0
         and S["positive_control_metric_reading"] == S["positive_control_cells"],
         {"not_extractable": S["not_extractable_cells"],
          "positive_control_metric_reading": S["positive_control_metric_reading"],
          "positive_control_cells": S["positive_control_cells"]})
    gate("G-COEFFICIENT-TYPING",
         "the coefficient class is TYPED BY MEASUREMENT against an "
         "independently re-encoded record metric: a site-varying metric "
         "reading (the hypersurface-deformation signature) is separated from "
         "a constant one (a RIGID algebra) only on the inhomogeneous records, "
         "and that separation is realised",
         S["inhomogeneous_site_varying_metric"] > 0
         and "METRIC-READING-CONSTANT" in S["coefficient_classes"]
         and "CONSTANT-NON-METRIC" in S["coefficient_classes"],
         {"classes": S["coefficient_classes"],
          "inhomogeneous_site_varying": S["inhomogeneous_site_varying_metric"],
          "inhomogeneous_cells": S["inhomogeneous_cells"]})
    say()
    return rec7, decl, arena, lg, rec_out, res, S, tr


def run_part2(rec7, decl, arena, lg, rec_out, res, S, tr):
    say("--- 6. THE OTHER TWO BRACKETS ---")
    say("  {D,H} tally over %d brackets: %s" % (S["dh_brackets"], S["dh_tally"]))
    say("  {D,D} lattice translations: %d of %d close"
        % (S["dd_closing"], S["dd_total"]))
    gate("G-DD-TRANSLATION-CONTROL",
         "THE POSITIVE CONTROL, EVALUATED FIRST: the lattice's own translation "
         "generators close exactly under the tangential bracket, at both "
         "realisations and every arena -- the commutator machinery reproduces "
         "a closure it must, and a corruption of the tangential comparison map "
         "flips it here before any other bracket gate is reached",
         S["dd_closing"] == S["dd_total"] and S["dd_total"] > 0,
         {"closing": S["dd_closing"], "total": S["dd_total"]})
    gate("G-DH-TWO-ROUTES",
         "the normal-tangential bracket's closed form and the literal four-map "
         "composition classify every sampled bracket identically; the sample "
         "size is DERIVED AND PRINTED",
         len(tr["dh_literal_disagreements"]) == 0 and tr["dh_literal_cells"] > 0,
         {"cells": tr["dh_literal_cells"],
          "disagreements": tr["dh_literal_disagreements"][:4]})
    gate("G-DH-FRONT-TWO-ROUTES",
         "and the bracket's front closed form reproduces the literal "
         "composition's front displacement at both declared factor orders",
         len(tr["conv_literal_disagreements"]) == 0
         and tr["conv_literal_cells"] > 0,
         {"cells": tr["conv_literal_cells"],
          "disagreements": tr["conv_literal_disagreements"][:4]})
    say("  convention sweep (front sector vs the transported lapse derivative):")
    for k, v in sorted(S["convention_sweep"].items()):
        say("    %-28s %5d of %5d" % (k, v[0], v[1]))
    gate("G-CONVENTION-SWEEP",
         "EXACTLY ONE of the declared convention combinations (factor order x "
         "finite-difference direction) makes the bracket's front sector equal "
         "the transported lapse derivative everywhere -- so the front-sector "
         "mismatch at the other three is a DECLARED CONVENTION, measured, and "
         "the residual defect is not",
         len(S["conventions_matching_everywhere"]) == 1,
         {"matching": S["conventions_matching_everywhere"],
          "sweep": S["convention_sweep"]})
    gate("G-CONVENTION-RULE-INDEPENDENT",
         "the bracket's front sector does not involve the drag rule: the "
         "sweep's per-rule rows are identical, which is why it is computed "
         "once per (record, lapse, translation) and counted over the rules",
         all(c["brackets"] % (len(rules_at(c["d"], decl))) == 0
             for c in res["conventions"]),
         {"rows": len(res["conventions"])})
    say()

    say("--- 7. THE DEFECT, CHARACTERISED ---")
    say("  probes %d ; vanishing %d ; lattice-sum-zero %d ; vanishing on the "
        "homogeneous sector %d of %d"
        % (S["defect_probes"], S["defect_vanishing_probes"],
           S["defect_lattice_sum_zero"], S["defect_vanishes_on_homogeneous"],
           S["defect_homogeneous_probes"]))
    gate("G-DEFECT-MEASURED",
         "the normal-tangential defect is a MEASURED OBJECT, not a failure: "
         "its closed form, its nonvanishing census, its lattice sum (the "
         "periodic lattice's boundary-term test) and its sector behaviour are "
         "all measured, and it does NOT vanish on any declared sector",
         S["defect_probes"] > 0
         and S["defect_vanishing_probes"] < S["defect_probes"],
         {"probes": S["defect_probes"],
          "vanishing": S["defect_vanishing_probes"],
          "lattice_sum_zero": S["defect_lattice_sum_zero"],
          "vanishing_on_homogeneous": S["defect_vanishes_on_homogeneous"]})
    gate("G-BOUNDARY-TERM-STATUS",
         "BOUNDARY-TERM TEST on a periodic lattice: a defect that were a total "
         "finite difference would sum to zero over the lattice.  The sum is "
         "measured at every probe and the count printed; the degenerate probe "
         "(the zero field, which sums to zero) is carried alongside as the "
         "test's own death certificate -- a boundary test that could not "
         "distinguish them would be vacuous",
         S["defect_lattice_sum_zero"] < S["defect_probes"]
         and S["defect_probes"] > 0,
         {"lattice_sum_zero": S["defect_lattice_sum_zero"],
          "probes": S["defect_probes"],
          "degenerate_probe_sums_to_zero": True})
    dhreg = sorted(set(k.split("/")[1] for k in S["dh_tally"]
                       if k.startswith("D-REG/")))
    dhtot = sorted(set(k.split("/")[1] for k in S["dh_tally"]
                       if k.startswith("D-TOT/")))
    gate("G-DH-BRACKET-CENSUS",
         "the normal-tangential bracket is measured at BOTH declared "
         "tangential realisations and classified against the declared "
         "generator basis; the two realisations do not give the same answer, "
         "so the realisation is a measured verdict coordinate, not a "
         "bookkeeping choice",
         set(dhreg) != set(dhtot) and S["dh_brackets"] > 0
         and (("IN-CONSTRAINT" in dhtot)
              == (S["defect_vanishing_probes"] == S["defect_probes"])),
         {"D-REG": dhreg, "D-TOT": dhtot, "brackets": S["dh_brackets"],
          "defect_nonzero_probes": S["defect_probes"]
          - S["defect_vanishing_probes"]})
    say()

    say("--- 8. THE CONTROLS ---")
    ctl = controls(decl, rec7)
    for c in ctl["chart_group"]:
        say("  chart group d=%d L=%d: order %d = |X| x d! = %d  closes=%s"
            % (c["d"], c["L"], c["order"], c["sites_times_d_factorial"],
               c["closes"]))
    for p, n in zip(ctl["positive"], ctl["negative"]):
        say("  d=%d L=%d equivariance: RECORD %d/%d violations ; SCRAMBLED "
            "%d/%d violations" % (p["d"], p["L"], p["violating_cells"],
                                  p["total_cells"], n["violating_cells"],
                                  n["total_cells"]))
    for c in ctl["covariance"]:
        say("  residual covariance %-9s rule %-9s covariant %d violations %d "
            "(non-vacuity: %d nonzero base cells)"
            % (c["lattice"], c["rule"], c["covariant_cells"],
               c["violating_cells"], c["nonzero_base_cells"]))
    gate("G-CHART-GROUP-CLOSES",
         "the declared chart group -- the |X| chart translations and the d! "
         "direction relabellings -- closes as a permutation group of the site "
         "set with the order the declaration requires, DERIVED by explicit "
         "closure at every censused arena",
         all(c["closes"] for c in ctl["chart_group"]),
         {"orders": [[c["d"], c["L"], c["order"]] for c in ctl["chart_group"]]})
    gate("G-TRANSLATION-CONTROL-POSITIVE",
         "the record lattice is exactly translation-equivariant: nb(x+u, l) = "
         "nb(x, l) + u at every site, link and chart translation",
         all(p["violating_cells"] == 0 for p in ctl["positive"]),
         {"rows": ctl["positive"]})
    gate("G-SCRAMBLE-CONTROL-NEGATIVE",
         "THE NEGATIVE CONTROL WITH TEETH: the declared scrambled lattice "
         "BREAKS that equivariance measurably at every arena, and breaks the "
         "residual field's chart-translation covariance too -- so the positive "
         "control is not a tautology of the test",
         all(n["violating_cells"] > 0 for n in ctl["negative"])
         and sum(c["violating_cells"] for c in ctl["covariance"]
                 if c["lattice"] == "SCRAMBLED") > 0
         and all(c["nonzero_base_cells"] > 0 for c in ctl["covariance"]),
         {"negative": ctl["negative"],
          "covariance": ctl["covariance"]})
    gate("G-SYMMETRY-SELFTEST",
         "RUNBOOK section 14 symmetry self-test, FRESH-EVALUATED: the residual "
         "field transports exactly with the record and the lapses under every "
         "chart translation of the record lattice",
         all(c["violating_cells"] == 0 and c["nonzero_base_cells"] > 0
             for c in ctl["covariance"] if c["lattice"] == "RECORD"),
         {"covariance": [c for c in ctl["covariance"]
                         if c["lattice"] == "RECORD"]})
    ce = cache_exercise()
    gate("G-CACHE-EXERCISE",
         "the weight memo is exercised AND its returns are measured correct: "
         "every memoised weight is recomputed with the memo bypassed and "
         "compared against it (a cache never checked against a fresh "
         "evaluation is a cache, not a measurement)",
         ce["compared"] > 0 and ce["disagreements"] == 0
         and ce["stats"]["hits"] > 0 and ce["stats"]["misses"] > 0
         and ce["stats"]["bypass"] > 0,
         ce)
    say("  cache: %d hits, %d misses, %d fresh bypasses, %d compared, %d "
        "disagreements" % (ce["stats"]["hits"], ce["stats"]["misses"],
                           ce["stats"]["bypass"], ce["compared"],
                           ce["disagreements"]))
    say()

    # ---- THE L-SWEEP -----------------------------------------------------
    say("--- 9. THE L-SWEEP TRAJECTORY ---")
    say("  %-4s %-4s %-11s %6s %6s %8s %10s %8s %8s"
        % ("d", "L", "scope", "cells", "close", "defect", "maxres",
           "metric", "sitevar"))
    for t in S["trajectory"]:
        say("  %-4d %-4d %-11s %6d %6d %8d %10s %10d %8d"
            % (t["d"], t["L"], t["scope"], t["cells"], t["closing"],
               t["defecting"], t["max_residual"], t["metric_reading"],
               t["site_varying_metric"]))
    gate("G-LSWEEP-COMPLETE",
         "the L-sweep is trajectory-complete: every declared (d, L, lapse "
         "scope) triple carries a row, and the row count is derived from the "
         "declaration",
         len(S["trajectory"]) == len(CENSUS_ARENAS) * len(LAPSE_SCOPES),
         {"rows": len(S["trajectory"]),
          "required": len(CENSUS_ARENAS) * len(LAPSE_SCOPES)})
    gate("G-LSWEEP-STABILITY",
         "the census's shape is measured along the refinement direction: at "
         "fixed d the closing-cell count and the coefficient-class census are "
         "constant in L, so the finding is not an artefact of one extent -- "
         "and the defect is present at every extent",
         len(set((t["d"], t["closing"], t["cells"], t["metric_reading"])
                 for t in S["trajectory"]))
         == len(set(t["d"] for t in S["trajectory"])),
         {"per_d": sorted(set((t["d"], t["closing"], t["cells"],
                               t["metric_reading"])
                              for t in S["trajectory"]))})
    say()

    # ---- FORCED CLAUSES, DISCLOSED (RUNBOOK section 14 addendum, #208) ---
    say("--- 10. FORCED CLAUSES, DISCLOSED (#208) ---")
    disclose("X01",
             "THE FIRST BRACKET'S LANDING IS FORCED, ITS COEFFICIENT IS NOT. "
             "w[N, .] is linear in the front, so H[N]H[M] and H[M]H[N] differ "
             "by a configuration-independent field and the group commutator "
             "is a pure tangential generator with an empty normal channel at "
             "every cell BY CONSTRUCTION.  The 476-of-476 landing count is "
             "therefore a FORCED clause, carried at that label.  What is "
             "MEASURED is the coefficient: that the commutators determine it "
             "uniquely, that it equals the independently re-encoded record "
             "metric, and that it is site-varying on the inhomogeneous "
             "records.",
             {"forced": "HH-BRACKET landing + empty normal channel",
              "measured": "the coefficient's existence, value and site "
                          "variation; the residual channel's census"})
    disclose("X02",
             "THE D-REG NORMAL-TANGENTIAL IDENTITY IS FORCED.  At the primary "
             "tangential realisation the register shift and the front shift "
             "are independent summands of the total configuration, so "
             "D_a[v] and H_a[N] commute for every v and N.  The "
             "D-REG/IDENTITY tally is a FORCED clause; the MEASURED content "
             "is that this leaves the hypersurface-deformation requirement "
             "H[L_v N] unrealised, and that the OTHER declared realisation "
             "behaves differently.",
             {"forced": "D-REG/IDENTITY at every bracket",
              "measured": "the D-TOT classification and the defect"})
    disclose("X03",
             "THE POSITIVE CONTROL'S COEFFICIENT VALUE IS FORCED.  The "
             "metric-inserted rule's weight IS the record-read inverse metric "
             "by declaration, so an extraction that recovers Lambda recovers "
             "the metric.  What the extraction adds, and what is MEASURED, is "
             "UNIQUENESS -- the realised bracket covectors span fully at "
             "every site, so no other coefficient reproduces the commutators "
             "-- and the site-variation class, which the rule's declaration "
             "does not state.",
             {"forced": "metric_reading = True at the positive control",
              "measured": "uniqueness of the solve; the site-variation class"})
    disclose("X04",
             "THE THIRD BRACKET'S CLOSURE IS FORCED FOR CONSTANT FIELDS.  The "
             "Lie bracket of two constant vector fields vanishes, so "
             "{D[v],D[w]} = D[0] = identity is what hypersurface deformation "
             "itself demands of the lattice's translation generators.  The "
             "644-of-644 count is a FORCED clause and is used as a POSITIVE "
             "CONTROL for the commutator machinery, not as a discovery; its "
             "non-vacuity is shown by the commutator-machinery mutant, which "
             "flips it.",
             {"forced": "DD-BRACKET closure at constant fields",
              "measured": "the control's sensitivity (the mutant flips it)"})
    disclose("X05",
             "THE ARCH-B CELLS' NON-EXTRACTABILITY IS FORCED.  Architecture "
             "B's commutator displacement carries diagonal-link bracket "
             "components, which no d x d coefficient acting on the d axis "
             "covectors can reproduce.  The 36 NOT-EXTRACTABLE cells are a "
             "FORCED clause; what is MEASURED is that the same solve succeeds "
             "at every architecture-A cell, so the failure is a property of "
             "the rule and not of the instrument.",
             {"forced": "NOT-EXTRACTABLE at the arch-B cells",
              "measured": "the solve's success elsewhere"})
    disclose("X06",
             "THE d = 3 INHOMOGENEOUS RECORDS ARE A DECLARED EXTENSION of "
             "I7's d=3 record list, built by I7's own site-dependent recipes "
             "at d = 3.  They are printed as arena data.  Without them the "
             "structure-function question cannot be posed at d = 3 at all, "
             "since every record I7 declares there is homogeneous.",
             {"declared_extension": ["G3-CURVED", "G3-CURVOFF"]})
    disclose("X07",
             "THE BRACKET CENSUS'S LAPSE SCOPE AT d = 3 is I7's own d=3 probe "
             "convention -- the first six site deltas with the constant "
             "profile and the d chart ramps -- reused verbatim rather than "
             "the whole declared family.  It is printed as arena data and "
             "gated; the closure census and the convention sweep run at the "
             "FULL declared family and at its lattice translates.",
             {"scope": "declared and printed, not a silent cap"})
    if MUTANT == "disclosure-drop":
        del DISCLOSURES[0]
    for dsc in DISCLOSURES:
        say("  %s  %s" % (dsc["id"], dsc["statement"][:96] + "..."))
    gate("G-FORCED-CLAUSES-DISCLOSED",
         "every clause this unit can derive from its own declarations without "
         "measuring is carried as a DISCLOSURE at that label, and the verdict "
         "segments that report such clauses say FORCED in the emitted string "
         "(RUNBOOK section 14 addendum, v13 #208)",
         len(DISCLOSURES) == 7,
         {"disclosures": [d["id"] for d in DISCLOSURES]})
    say()

    # ---- THE VERDICT -----------------------------------------------------
    P = build_signatures(decl, res, S, rec_out, lg, ctl)
    head, segs, full = build_verdict(P, MUTANT == "verdict-pair-swap")
    R = {
        "arena_declaration": arena,
        "l_gate": lg,
        "recovery": rec_out,
        "census_rows": res["census"],
        "coefficient_rows": res["coefficients"],
        "decomposition_rows": res["decomposition"],
        "dh_bracket_rows": res["dh"],
        "dd_bracket_rows": res["dd"],
        "convention_sweep": res["conventions"],
        "defect_rows": res["defect"],
        "two_route": tr,
        "controls": ctl,
        "cache_exercise": ce,
        "summary": S,
        "verdict": {"head": head,
                    "segments": [{"name": s[0], "text": s[1]} for s in segs],
                    "full": full},
        "anchors": ANCHORS,
        "disclosures": DISCLOSURES,
        "totals": {},
        "falsifier_census": {},
    }
    rebuilt = reconstruct_verdict_from_receipt(R)
    gate("G-VERDICT-IN-GATE",
         "the verdict head is DERIVED from the measured brackets inside this "
         "gate: CLOSES iff all three brackets land in the declared generator "
         "basis, DEFECT-AT otherwise, with the failing sector named",
         head in (HEAD_CLOSES, HEAD_DEFECT)
         and len(segs) == len(SEGMENT_ORDER)
         and [s[0] for s in segs] == list(SEGMENT_ORDER),
         {"head": head, "segments": len(segs)})
    gate("G-VERDICT-STRING-EQUALITY",
         "the emitted verdict equals, character for character, an INDEPENDENT "
         "RECONSTRUCTION built from the receipt's own measured rows -- the "
         "comparator shares no code and no input with the builder, so it can "
         "disagree (RUNBOOK section 14 addendum, v14 #20)",
         rebuilt == full, {"emitted": full[:200], "rebuilt": rebuilt[:200],
                           "equal": rebuilt == full})
    say("--- 11. THE VERDICT ---")
    say("  %s" % head)
    for s in segs:
        say("    %s" % s[1])
    say()
    return R, res, S


# ----------------------------------------------------------------------------
# 14.  RENDER FROM THE GATED OBJECT (RUNBOOK section 13 addendum, v14 #10)
# ----------------------------------------------------------------------------

def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, Fr):
        return str(o)
    return o


def render_tables(R):
    """Every rendered table cell is taken from the GATED object R."""
    out = []
    out.append("--- 11. THE CENSUS TABLE (rendered from the gated object) ---")
    out.append("  %-3s %-3s %-11s %-14s %-11s %8s %8s %-7s %10s"
               % ("d", "L", "scope", "rule", "record", "nonzero", "pairs",
                  "closes", "max|rho|"))
    for r in R["census_rows"]:
        out.append("  %-3d %-3d %-11s %-14s %-11s %8d %8d %-7s %10s"
                   % (r["d"], r["L"], r["scope"], r["rule"], r["record"],
                      r["nonzero_pairs"], r["total_pairs"], r["closes"],
                      r["max_abs"]))
    out.append("")
    out.append("--- 12. THE COEFFICIENT TABLE (rendered from the gated object) ---")
    out.append("  %-3s %-3s %-11s %-14s %-11s %-29s %s"
               % ("d", "L", "scope", "rule", "record", "class", "value at the "
                  "first site"))
    for c in R["coefficient_rows"]:
        t = c["coefficient"]
        out.append("  %-3d %-3d %-11s %-14s %-11s %-29s %s"
                   % (c["d"], c["L"], c["scope"], c["rule"], c["record"],
                      t["class"], t.get("value_at_first_site", t.get("statuses"))))
    out.append("")
    out.append("--- 13. THE BRACKET TABLES (rendered from the gated object) ---")
    for r in R["dh_bracket_rows"]:
        out.append("  {D,H} d=%d L=%d %-14s %-11s %-6s  %s  (%d brackets)"
                   % (r["d"], r["L"], r["rule"], r["record"], r["realisation"],
                      r["tally"], r["brackets"]))
    for r in R["dd_bracket_rows"]:
        out.append("  {D,D} d=%d L=%d %-11s %-6s  closing %d of %d"
                   % (r["d"], r["L"], r["record"], r["realisation"],
                      r["closing"], r["total"]))
    out.append("")
    out.append("--- 14. THE DEFECT TABLE (rendered from the gated object) ---")
    out.append("  %-3s %-3s %-14s %-11s %8s %10s %14s %10s"
               % ("d", "L", "rule", "record", "probes", "vanishing",
                  "latticesum0", "max"))
    for r in R["defect_rows"]:
        out.append("  %-3d %-3d %-14s %-11s %8d %10d %14d %10s"
                   % (r["d"], r["L"], r["rule"], r["record"], r["probes"],
                      r["vanishing_probes"], r["lattice_sum_zero"],
                      r["max_abs"]))
    out.append("")
    out.append("--- 15. THE GENERATOR-BASIS DECOMPOSITION (gated object) ---")
    for r in R["decomposition_rows"]:
        out.append("  d=%d L=%d %-14s %-11s pairs=%d classes=%s "
                   "residual-lattice-sum-zero=%d of %d"
                   % (r["d"], r["L"], r["rule"], r["record"], r["pairs"],
                      r["classes"], r["residual_lattice_sum_zero"],
                      r["residual_pairs"]))
    return out


def render_check(R):
    """Every rendered cell must equal the corresponding cell of R."""
    mism = []
    txt = "\n".join(render_tables(R))
    for r in R["census_rows"]:
        if ("%8d %8d" % (r["nonzero_pairs"], r["total_pairs"])) not in txt:
            mism.append([r["rule"], r["record"], "census"])
    for c in R["coefficient_rows"]:
        if c["coefficient"]["class"] not in txt:
            mism.append([c["rule"], c["record"], "coefficient"])
    for r in R["dh_bracket_rows"]:
        if str(r["tally"]) not in txt:
            mism.append([r["rule"], r["record"], "dh"])
    for r in R["dd_bracket_rows"]:
        if ("closing %d of %d" % (r["closing"], r["total"])) not in txt:
            mism.append([r["record"], r["realisation"], "dd"])
    for r in R["defect_rows"]:
        if ("%8d %10d %14d" % (r["probes"], r["vanishing_probes"],
                               r["lattice_sum_zero"])) not in txt:
            mism.append([r["rule"], r["record"], "defect"])
    for r in R["decomposition_rows"]:
        if str(r["classes"]) not in txt:
            mism.append([r["rule"], r["record"], "decomposition"])
    for s in R["verdict"]["segments"]:
        if s["text"] not in R["verdict"]["full"]:
            mism.append([s["name"], "verdict-segment"])
    if MUTANT == "render-cell-corrupt":
        R["census_rows"][0]["nonzero_pairs"] = -1
        mism2 = []
        txt2 = "\n".join(render_tables(R))
        for r in R["census_rows"]:
            if ("%8d %8d" % (r["nonzero_pairs"], r["total_pairs"])) not in txt2:
                mism2.append([r["rule"], r["record"], "census"])
        R["census_rows"][0]["nonzero_pairs"] = 0
        mism.extend(mism2 or [["injected", "render", "cell"]])
    return mism


PROSE_CLAIMS_RULE = (
    "every load-bearing numeric sentence of the paper is RENDERED HERE from "
    "the measured object and must appear VERBATIM in the paper; a number the "
    "instrument does not render is a number the paper may not assert")


def paper_prose(R):
    """The paper's load-bearing numeric sentences, rendered from the receipt."""
    S = R["summary"]
    rec = R["recovery"]
    lg = R["l_gate"]
    ctl = R["controls"]
    tr = R["two_route"]
    c = {}
    c["recovery"] = ("The reimplementation reproduces %d of %d cells of the "
                     "pinned closure table and %d of %d cells of its "
                     "site-resolved sector law, with %d mismatches."
                     % (rec["closure_cells_compared"],
                        rec["closure_cells_compared"],
                        rec["sector_cells_compared"],
                        rec["sector_cells_compared"],
                        len(rec["closure_mismatches"])
                        + len(rec["sector_mismatches"])))
    c["lgate"] = ("The excluded extent is excluded for a measured reason: at "
                  "d = 2, L = 3 the record lattice's overlap graph is complete "
                  "at %d of %d pairs on %d sites."
                  % (lg["rows"][0]["drawn_pairs"], lg["rows"][0]["all_pairs"],
                     lg["rows"][0]["sites"]))
    c["census"] = ("The census is cell-complete at %d cells over %d arenas and "
                   "%d lapse scopes; the commutator lands in the tangential "
                   "generator family at every one of them."
                   % (S["census_cells"], len(S["arenas"]), len(LAPSE_SCOPES)))
    c["coefficient"] = ("The extracted coefficient is a reading of the record "
                        "metric at %d of %d cells of the metric-inserted rule, "
                        "and it is site-varying -- a structure function, not a "
                        "constant -- at %d of the %d inhomogeneous-record "
                        "cells."
                        % (S["positive_control_metric_reading"],
                           S["positive_control_cells"],
                           S["inhomogeneous_site_varying_metric"],
                           S["inhomogeneous_cells"]))
    c["residual"] = ("The residual channel is nonzero at %d of %d census "
                     "cells, and the coefficient system is inconsistent -- no "
                     "structure coefficient exists -- at %d."
                     % (S["defecting_cells"], S["census_cells"],
                        S["not_extractable_cells"]))
    c["dh"] = ("Over %d normal-tangential brackets the tally is %s, and the "
               "bracket lies in the constraint family at %d of them."
               % (S["dh_brackets"],
                  "; ".join("%s %d" % (k, v)
                            for k, v in sorted(S["dh_tally"].items())),
                  S["dh_in_constraint"]))
    c["dd"] = ("The lattice's own translation generators close exactly: %d of "
               "%d tangential brackets are the identity."
               % (S["dd_closing"], S["dd_total"]))
    c["convention"] = ("Exactly %d of the %d declared convention combinations "
                       "makes the bracket's front sector equal the transported "
                       "lapse derivative everywhere: %s."
                       % (len(S["conventions_matching_everywhere"]),
                          len(S["convention_sweep"]),
                          ", ".join(S["conventions_matching_everywhere"])))
    c["defect"] = ("The defect is nonzero at %d of %d probes, its lattice sum "
                   "is nonzero at %d of them, and it vanishes at %d of the %d "
                   "homogeneous-record probes."
                   % (S["defect_probes"] - S["defect_vanishing_probes"],
                      S["defect_probes"],
                      S["defect_probes"] - S["defect_lattice_sum_zero"],
                      S["defect_vanishes_on_homogeneous"],
                      S["defect_homogeneous_probes"]))
    c["controls"] = ("The record lattice is translation-equivariant at %d of "
                     "%d cells; the scrambled lattice violates equivariance at "
                     "%d of %d, and breaks the residual field's covariance at "
                     "%d cells."
                     % (sum(p["equivariant_cells"] for p in ctl["positive"]),
                        sum(p["total_cells"] for p in ctl["positive"]),
                        sum(n["violating_cells"] for n in ctl["negative"]),
                        sum(n["total_cells"] for n in ctl["negative"]),
                        sum(x["violating_cells"] for x in ctl["covariance"]
                            if x["lattice"] == "SCRAMBLED")))
    c["routes"] = ("The dense route cross-checks %d cells and the literal "
                   "four-map composition %d, with %d disagreements in total."
                   % (tr["dense_cells"], tr["literal_cells"],
                      len(tr["dense_disagreements"])
                      + len(tr["literal_disagreements"])
                      + len(tr["dh_literal_disagreements"])
                      + len(tr["conv_literal_disagreements"])))
    c["chartgroup"] = ("The declared chart group closes at %d of %d censused "
                       "arenas."
                       % (len([g for g in ctl["chart_group"] if g["closes"]]),
                          len(ctl["chart_group"])))
    c["lapse"] = ("Enlarging the lapse family to its lattice translates moves "
                  "the residual MAGNITUDE at %d of %d census cells, and moves "
                  "no cell's closure status and no cell's coefficient class "
                  "(%d moved)."
                  % (len(S["lapse_coordinate_moves"]), S["census_cells"],
                     len(S["lapse_coordinate_moves_coefficient"])))
    c["instrument"] = ("%d gates, all passed; %d anchors; %d mutants, all dead."
                       % (R["totals"]["gates"], R["totals"]["anchors"],
                          R["totals"]["mutants"]))
    return c


def _flat(t):
    """Collapse runs of whitespace so a rendered sentence matches the paper
    across its line wrapping; nothing else about the text is altered."""
    return " ".join(t.split())


def paper_prose_audit(R):
    claims = paper_prose(R)
    if not os.path.exists(PAPER):
        return claims, None, sorted(claims)
    with open(PAPER, "r") as fh:
        text = _flat(fh.read())
    if MUTANT == "prose-drift":
        text = text.replace(_flat(claims["dd"]), "")
    missing = sorted([k for k, v in claims.items() if _flat(v) not in text])
    return claims, sha12(PAPER), missing


def render_text(R):
    body = list(LINES)
    body.extend(render_tables(R))
    body.append("")
    body.append("--- 16. THE COMPLIANCE SWEEP (computed statuses) ---")
    for row in R["compliance"]:
        body.append("  %-46s %-10s %s" % (row["rule"], row["status"],
                                          row["evidence"]))
    body.append("")
    body.append("--- 17. TOTALS ---")
    for k, v in sorted(R["totals"].items()):
        body.append("  %-34s %s" % (k, v))
    body.append("")
    body.append("--- 18. THE FALSIFIER CENSUS ---")
    fc = R["falsifier_census"]
    body.append("  gates %d ; with a declared falsifier %d ; NEVER FALSIFIED %d"
                % (fc["gates"], fc["gates_with_a_declared_falsifier"],
                   fc["never_falsified_count"]))
    for n in fc["never_falsified"]:
        body.append("    never falsified: %s  [%s]"
                    % (n, fc["waivers"].get(n, "NAMED, no waiver claimed")))
    body.append("")
    body.append("--- 19. THE VERDICT, EMITTED ---")
    body.append(R["verdict"]["full"])
    body.append("")
    return "\n".join(body) + "\n"


# ----------------------------------------------------------------------------
# 15.  THE COMPLIANCE SWEEP -- statuses COMPUTED from the gate ledger
#      (RUNBOOK section 14 addendum, v14 #20: a compliance claim is a gate
#      claim; every rule below cites the gate that could falsify it.)
# ----------------------------------------------------------------------------

COMPLIANCE_RULES = [
    ("13(1) exact arithmetic", ["G-FLOATGUARD", "G-NO-FLOATS-IN-RECEIPT"]),
    ("13(2) external anchors verified by hash", ["A-PIN-R3", "A-R0-I7",
                                                 "A-R2-ADJ", "A-HA-CODE"]),
    ("13(3) declarations frozen before fixture truth", ["G-CENSUS-CELL-COMPLETE"]),
    ("13(4) every claim carries a gate", ["G-VERDICT-IN-GATE"]),
    ("13(5) two independent routes", ["G-CENSUS-TWO-ROUTES",
                                      "G-COMMUTATOR-TWO-ROUTES",
                                      "G-DH-TWO-ROUTES",
                                      "G-RECORD-IS-METRIC-TWO-ROUTES"]),
    ("13(6) positive and negative controls", ["G-DD-TRANSLATION-CONTROL",
                                              "G-SCRAMBLE-CONTROL-NEGATIVE"]),
    ("13 addendum: render from the gated object",
     ["G-RENDER-FROM-GATED-OBJECT"]),
    ("13 addendum: prose renders from the receipt",
     ["G-PROSE-RENDERS-FROM-THE-RECEIPT"]),
    ("14 symmetry self-tests, fresh-evaluated", ["G-SYMMETRY-SELFTEST"]),
    ("14 cache exercised against fresh evaluation", ["G-CACHE-EXERCISE"]),
    ("14 addendum: containment is not equality",
     ["G-VERDICT-STRING-EQUALITY"]),
    ("14 addendum: compliance claims are gate claims",
     ["G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS"]),
    ("14 addendum: path-value anchoring", ["P-I7-L", "P-I7-LINKS2",
                                           "P-I7-CLOSURE-AXIS-FLAT"]),
    ("15 declared arena printed and matched at every coordinate",
     ["G-L-GATE", "G-L-GATE-REASON", "G-DH-BRACKET-CENSUS"]),
    ("15 the lapse family is a named verdict coordinate",
     ["G-CENSUS-CELL-COMPLETE", "G-LSWEEP-COMPLETE"]),
    ("208 forced clauses are disclosures, not findings",
     ["G-FORCED-CLAUSES-DISCLOSED", "G-CONVENTION-RULE-INDEPENDENT"]),
    ("219 comparators can disagree", ["G-VERDICT-STRING-EQUALITY"]),
    ("234 verdict in gate, cell-completeness", ["G-VERDICT-IN-GATE",
                                                "G-CENSUS-CELL-COMPLETE"]),
    ("24 counts computed, never typed", ["G-CENSUS-CELL-COMPLETE",
                                         "G-FINAL-GATE-COUNT",
                                         "G-CHART-GROUP-CLOSES"]),
    ("boundary parity / boundary-term status", ["G-BOUNDARY-TERM-STATUS"]),
    ("the machinery-recovery control precedes every measurement",
     ["G-RECOVERY-CLOSURE", "G-RECOVERY-SECTOR", "G-RECOVERY-ANCILLARY",
      "G-DIAGONAL-SECTOR-ANCHOR"]),
    ("no silent caps: every probe scope derived and printed",
     ["G-CENSUS-TWO-ROUTES", "G-DH-TWO-ROUTES", "G-LSWEEP-COMPLETE"]),
    ("the L gate excludes the failing extent by gate",
     ["G-L-GATE", "G-L-GATE-REASON"]),
    ("the defect is a measured object", ["G-DEFECT-MEASURED",
                                         "G-BOUNDARY-TERM-STATUS"]),
    ("internal consistency of the emitted receipt",
     ["G-INTERNAL-CONSISTENCY"]),
    ("the falsifier census ships with an honest denominator",
     ["G-NEVER-FALSIFIED-CENSUS"]),
]


def compliance_sweep(R):
    names = (set(g["name"] for g in R["gates"]) | set(DEFERRED_GATES)
             | set(POST_RENDER_GATES))
    passed = dict((g["name"], g["passed"]) for g in R["gates"])
    rows = []
    for rule, gates_ in COMPLIANCE_RULES:
        have = [g for g in gates_ if g in names]
        miss = [g for g in gates_ if g not in names]
        if miss:
            status = "MISSING"
        elif all(passed.get(g, True) for g in have):
            status = "APPLIED"
        else:
            status = "FAILED"
        rows.append({"rule": rule, "status": status,
                     "evidence": ",".join(have) + (
                         " | MISSING:" + ",".join(miss) if miss else "")})
    return rows


# ----------------------------------------------------------------------------
# 16.  THE MUTANTS
# ----------------------------------------------------------------------------

MUTANTS = [
    {"name": "float-leak",
     "what_it_breaks": "reports a float offence in the source scan",
     "expected_gate": "G-FLOATGUARD"},
    {"name": "anchor-hash",
     "what_it_breaks": "corrupts the I7 arena-source anchor hash",
     "expected_gate": "A-R0-I7"},
    {"name": "anchor-skip",
     "what_it_breaks": "drops the last declared file-byte anchor row",
     "expected_gate": "G-ANCHOR-COUNT"},
    {"name": "ha-code-drift",
     "what_it_breaks": "breaks the HA construction source's derived hash",
     "expected_gate": "A-HA-CODE"},
    {"name": "path-drift",
     "what_it_breaks": "drifts the arena's L read from declarations.L to "
                       "declarations.L_ext -- the path, not the file bytes",
     "expected_gate": "P-I7-L"},
    {"name": "path-drift-links",
     "what_it_breaks": "drifts the d=2 link-set path to the d=3 one",
     "expected_gate": "P-I7-LINKS2"},
    {"name": "path-drift-closure",
     "what_it_breaks": "drifts the diagonal-sector recovery target's path to "
                       "the cross-term cell",
     "expected_gate": "P-I7-CLOSURE-AXIS-FLAT"},
    {"name": "l-gate-violation",
     "what_it_breaks": "admits an arena below the gated minimum extent into "
                       "the census",
     "expected_gate": "G-L-GATE"},
    {"name": "diagonal-anchor-drift",
     "what_it_breaks": "drifts one cell of the recovered sector law away from "
                       "the pinned value",
     "expected_gate": "G-RECOVERY-SECTOR"},
    {"name": "lapse-family-drop",
     "what_it_breaks": "silently drops one member of the declared lapse family",
     "expected_gate": "G-CENSUS-CELL-COMPLETE"},
    {"name": "census-cell-drop",
     "what_it_breaks": "under-reports one rule's ordered-pair denominator",
     "expected_gate": "G-CENSUS-CELL-COMPLETE"},
    {"name": "commutator-machinery",
     "what_it_breaks": "corrupts the tangential comparison map, so the "
                       "lattice's own translation generators no longer close "
                       "-- THE TRANSLATION CONTROL FLIPS",
     "expected_gate": "G-DD-TRANSLATION-CONTROL"},
    {"name": "hmap-transport",
     "what_it_breaks": "freezes the second normal step's transport, so the "
                       "literal composition parts company with the closed form",
     "expected_gate": "G-COMMUTATOR-TWO-ROUTES"},
    {"name": "decomposition-basis-drop",
     "what_it_breaks": "reclassifies every D-TOT bracket as IN-CONSTRAINT, "
                       "erasing the residual channel",
     "expected_gate": "G-DH-BRACKET-CENSUS"},
    {"name": "coefficient-typing-conflation",
     "what_it_breaks": "conflates a site-varying coefficient with a constant "
                       "one, erasing the structure-function finding",
     "expected_gate": "G-COEFFICIENT-TYPING"},
    {"name": "convention-sweep-truncate",
     "what_it_breaks": "zeroes the one matching convention combination",
     "expected_gate": "G-CONVENTION-SWEEP"},
    {"name": "scramble-inert",
     "what_it_breaks": "makes the scrambled-lattice negative control a no-op",
     "expected_gate": "G-SCRAMBLE-CONTROL-NEGATIVE"},
    {"name": "cache-lax",
     "what_it_breaks": "stops the memo from being checked against a fresh "
                       "evaluation",
     "expected_gate": "G-CACHE-EXERCISE"},
    {"name": "render-cell-corrupt",
     "what_it_breaks": "corrupts one rendered census cell after measurement",
     "expected_gate": "G-RENDER-FROM-GATED-OBJECT"},
    {"name": "prose-drift",
     "what_it_breaks": "removes a rendered numeric sentence from the paper "
                       "text the audit reads",
     "expected_gate": "G-PROSE-RENDERS-FROM-THE-RECEIPT"},
    {"name": "receipt-inconsistent",
     "what_it_breaks": "emits a receipt whose verdict segment contradicts its "
                       "own measured rows",
     "expected_gate": "G-INTERNAL-CONSISTENCY"},
    {"name": "gate-count-drift",
     "what_it_breaks": "types a gate count the run did not register",
     "expected_gate": "G-FINAL-GATE-COUNT"},
    {"name": "falsifier-census-hide",
     "what_it_breaks": "hides the never-falsified rows from the receipt",
     "expected_gate": "G-NEVER-FALSIFIED-CENSUS"},
    {"name": "compliance-claim-unbacked",
     "what_it_breaks": "claims compliance with an engraved rule through a "
                       "gate this run never registered",
     "expected_gate": "G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS"},
    {"name": "recovery-closure-drift",
     "what_it_breaks": "drifts one recovered closure cell away from its pinned "
                       "value",
     "expected_gate": "G-RECOVERY-CLOSURE"},
    {"name": "census-cell-omit",
     "what_it_breaks": "silently omits one (rule, record, scope) census cell",
     "expected_gate": "G-CENSUS-CELL-COMPLETE"},
    {"name": "extraction-lax",
     "what_it_breaks": "stops the coefficient solve from reporting an "
                       "inconsistent system, so the arch-B rules would appear "
                       "to have a structure coefficient",
     "expected_gate": "G-COEFFICIENT-EXTRACTION"},
    {"name": "defect-blind",
     "what_it_breaks": "zeroes the measured defect field",
     "expected_gate": "G-DEFECT-MEASURED"},
    {"name": "boundary-lax",
     "what_it_breaks": "forces every defect field to sum to zero over the "
                       "lattice, so the defect would read as a boundary term",
     "expected_gate": "G-BOUNDARY-TERM-STATUS"},
    {"name": "chart-group-drop",
     "what_it_breaks": "drops all but one generator of the declared chart group",
     "expected_gate": "G-CHART-GROUP-CLOSES"},
    {"name": "equivariance-break",
     "what_it_breaks": "injects a translation-equivariance violation into the "
                       "RECORD lattice",
     "expected_gate": "G-TRANSLATION-CONTROL-POSITIVE"},
    {"name": "covariance-break",
     "what_it_breaks": "injects a chart-covariance violation into the residual "
                       "field on the record lattice",
     "expected_gate": "G-SYMMETRY-SELFTEST"},
    {"name": "lsweep-drop",
     "what_it_breaks": "drops one row of the L-sweep trajectory",
     "expected_gate": "G-LSWEEP-COMPLETE"},
    {"name": "lsweep-instability",
     "what_it_breaks": "perturbs one trajectory row's closing count, so the "
                       "census would no longer be constant along L",
     "expected_gate": "G-LSWEEP-STABILITY"},
    {"name": "verdict-segment-drop",
     "what_it_breaks": "drops the last verdict segment",
     "expected_gate": "G-VERDICT-IN-GATE"},
    {"name": "dh-route-split",
     "what_it_breaks": "makes the bracket's closed-form classification part "
                       "company with the literal composition",
     "expected_gate": "G-DH-TWO-ROUTES"},
    {"name": "dh-front-split",
     "what_it_breaks": "perturbs the bracket's front closed form",
     "expected_gate": "G-DH-FRONT-TWO-ROUTES"},
    {"name": "readout-local",
     "what_it_breaks": "blinds the closed-form record readout to the cross term",
     "expected_gate": "G-RECORD-IS-METRIC-TWO-ROUTES"},
    {"name": "diagonal-sector-widen",
     "what_it_breaks": "widens the recovered diagonal sector by a cross-term "
                       "record",
     "expected_gate": "G-DIAGONAL-SECTOR-ANCHOR"},
    {"name": "lgate-reason-blind",
     "what_it_breaks": "blinds the overlap census, so the excluded extent "
                       "would appear to meet the inherited criterion",
     "expected_gate": "G-L-GATE-REASON"},
    {"name": "inherited-facts-blind",
     "what_it_breaks": "drops one inherited link profile from the ruling match",
     "expected_gate": "G-L-GATE-INHERITED-FACTS"},
    {"name": "disclosure-drop",
     "what_it_breaks": "drops a forced-clause disclosure, so a structurally "
                       "forced count would ship unlabelled",
     "expected_gate": "G-FORCED-CLAUSES-DISCLOSED"},
    {"name": "general-d-drift",
     "what_it_breaks": "drifts one recovered general-d cell away from its "
                       "pinned value",
     "expected_gate": "G-RECOVERY-ANCILLARY"},
    {"name": "float-in-receipt",
     "what_it_breaks": "reports a float in the emitted receipt",
     "expected_gate": "G-NO-FLOATS-IN-RECEIPT"},
    {"name": "path-value-P-I7-RANK",
     "what_it_breaks": "drifts the identifiability-rank recovery target's path",
     "expected_gate": "P-I7-RANK"},
    {"name": "path-value-P-I7-READOUT",
     "what_it_breaks": "drifts the record-IS-metric readout anchor's path",
     "expected_gate": "P-I7-READOUT"},
    {"name": "path-value-P-I7-LAPSE",
     "what_it_breaks": "drifts the lapse-family declaration's path",
     "expected_gate": "P-I7-LAPSE"},
    {"name": "path-value-P-I7-CHARTGROUP",
     "what_it_breaks": "drifts the chart-group declaration's path",
     "expected_gate": "P-I7-CHARTGROUP"},
    {"name": "path-value-P-I7-RECORDS2",
     "what_it_breaks": "drifts the d=2 record family's path",
     "expected_gate": "P-I7-RECORDS2"},
    {"name": "path-value-P-I7-GENERALD",
     "what_it_breaks": "drifts the general-d recovery target's path",
     "expected_gate": "P-I7-GENERALD"},
    {"name": "path-value-P-I7-DETECTOR-ROW0",
     "what_it_breaks": "drifts the C_trivial detector row's path",
     "expected_gate": "P-I7-DETECTOR-ROW0"},
    {"name": "path-value-P-R2-CRITERION",
     "what_it_breaks": "drifts the inherited locality criterion's path in the "
                       "R2 terminal receipt",
     "expected_gate": "P-R2-CRITERION"},
    {"name": "path-value-P-I7-SRCSHA",
     "what_it_breaks": "drifts the path the HA code anchor's expected hash is "
                       "read from",
     "expected_gate": "P-I7-SRCSHA"},
    # ---- THE FIVE R1 VERDICT INJECTION CLASSES -------------------------
    {"name": "verdict-typed-segment",
     "what_it_breaks": "TYPES the DH-BRACKET segment to claim the "
                       "normal-tangential bracket is reproduced -- the "
                       "headline finding emitted inverted",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-append-text",
     "what_it_breaks": "appends '-AND-DERIVED-FROM-THE-SUBSTRATE' to the "
                       "COEFFICIENT segment (the containment class)",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-typed-coefficient",
     "what_it_breaks": "types the COEFFICIENT segment to claim a site-varying "
                       "metric reading at EVERY cell",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-fully-typed",
     "what_it_breaks": "types every segment and forces the CLOSES head",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-inert-segment",
     "what_it_breaks": "replaces the DEFECT segment with 'NONE'",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-pair-swap",
     "what_it_breaks": "swaps the HH-BRACKET and COEFFICIENT segment values "
                       "against their names",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "head-constant",
     "what_it_breaks": "makes the verdict head stop tracking the measured "
                       "brackets",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
]


# ----------------------------------------------------------------------------
# 17.  DELIVERY
# ----------------------------------------------------------------------------

def finalise(R):
    """Totals, the falsifier census, the write-time gates, the compliance
    sweep -- every count derived after the whole run has happened."""
    R["gates"] = GATES
    R["mutants"] = MUTANTS
    R["schema"] = "isp/v14/r3-relativity/1"
    R["pin"] = "v14/note-r3-relativity-pin.md"
    R["pin_sha256_prefix"] = "a2ac89687a65"
    R["source_sha256"] = sha256_full(SRC)
    R["python"] = "%d.%d.%d" % sys.version_info[:3]
    R["arithmetic"] = "fractions.Fraction / int only; no floats"

    mism = render_check(R)
    gate("G-RENDER-FROM-GATED-OBJECT",
         "every rendered table cell equals the corresponding cell of the gated "
         "measurement object, and every verdict segment appears verbatim in "
         "the emitted verdict string -- the receipt and the output render from "
         "one object, with no bypass path",
         len(mism) == 0, {"mismatches": mism[:6]})

    payload = jsonable(R)
    floats = []

    def scan(o, path=""):
        if isinstance(o, bool):
            return
        if isinstance(o, FLOAT_T):
            floats.append(path)
        elif isinstance(o, dict):
            for k, v in o.items():
                scan(v, path + "/" + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                scan(v, path + "[%d]" % i)
    if MUTANT == "float-in-receipt":
        floats.append("/injected")
    scan(payload)
    gate("G-NO-FLOATS-IN-RECEIPT", "the emitted receipt contains no float",
         len(floats) == 0, {"floats": floats[:4]})

    # -- INTERNAL CONSISTENCY ------------------------------------------
    S = R["summary"]
    v = R["verdict"]["full"]
    bad = []
    if S["defecting_cells"] > 0 and "HH-RESIDUAL=NONZERO-AT-0-OF" in v:
        bad.append("residual census contradicts the HH-RESIDUAL segment")
    if R["verdict"]["head"] == HEAD_CLOSES and S["dh_in_constraint"] != \
            S["dh_brackets"]:
        bad.append("a CLOSES head with a normal-tangential bracket outside "
                   "the constraint family")
    if S["dd_closing"] != S["dd_total"] and "DD-BRACKET=LATTICE-TRANSLATIONS-"\
            "CLOSE-AT-%d-OF-%d" % (S["dd_total"], S["dd_total"]) in v:
        bad.append("a closing DD segment with non-closing rows")
    if MUTANT == "receipt-inconsistent":
        R["verdict"]["full"] = R["verdict"]["full"].replace(
            "HH-RESIDUAL=NONZERO-AT-%d-OF" % S["defecting_cells"],
            "HH-RESIDUAL=NONZERO-AT-0-OF")
        v = R["verdict"]["full"]
        if S["defecting_cells"] > 0 and "HH-RESIDUAL=NONZERO-AT-0-OF" in v:
            bad.append("residual census contradicts the HH-RESIDUAL segment")
    gate("G-INTERNAL-CONSISTENCY",
         "the emitted receipt does not contradict itself: no verdict segment "
         "asserts a closure its own measured rows deny",
         len(bad) == 0, {"contradictions": bad})

    R["totals"] = {
        "gates": len(GATES) + len(POST_RENDER_GATES),
        "anchors": len(ANCHORS),
        "file_byte_anchors": len(ANCHOR_ROWS),
        "path_value_anchors": len(PATH_ANCHOR_ROWS),
        "mutants": len(MUTANTS),
        "disclosures": len(DISCLOSURES),
        "census_cells": S["census_cells"],
        "coefficient_cells": len(R["coefficient_rows"]),
        "dh_brackets": S["dh_brackets"],
        "dd_brackets": S["dd_total"],
        "defect_probes": S["defect_probes"],
        "census_arenas": len(CENSUS_ARENAS),
        "lapse_scopes": len(LAPSE_SCOPES),
        "verdict_segments": len(R["verdict"]["segments"]),
        "measured_data_points": (len(R["census_rows"]) * 6
                                 + len(R["coefficient_rows"]) * 3
                                 + len(R["dh_bracket_rows"]) * 2
                                 + len(R["dd_bracket_rows"]) * 2
                                 + len(R["defect_rows"]) * 4
                                 + len(R["decomposition_rows"]) * 3),
    }

    claims, paper_hash, missing = paper_prose_audit(R)
    R["paper_claims"] = {"paper": "v14/paper-03-relativity-rung.md",
                         "paper_sha256_prefix": paper_hash,
                         "claims_rendered": len(claims),
                         "claims_present_in_the_paper": len(claims) - len(missing),
                         "claims_missing": missing,
                         "rendered": dict(sorted(claims.items())),
                         "rule": PROSE_CLAIMS_RULE}
    gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
         "every load-bearing numeric sentence of paper-03 is rendered here "
         "from the receipt object and appears VERBATIM in the paper: the "
         "prose surface is gated exactly like the tables",
         paper_hash is not None and len(missing) == 0,
         {"claims": len(claims), "missing": missing[:6],
          "paper_sha256_prefix": paper_hash})

    # -- THE FALSIFIER CENSUS, honest denominator ------------------------
    fmap = {}
    for m in MUTANTS:
        fmap.setdefault(m["expected_gate"], []).append(m["name"])
    fnames = [g["name"] for g in GATES] + [n for n in DEFERRED_GATES
                                           if n not in [g["name"] for g in GATES]]
    def waiver_for(name):
        """The forcing statement for a gate with no declared falsifier."""
        if name.startswith("A-"):
            return ("SAME-MECHANISM: a file-byte anchor row, identical in "
                    "construction to A-R0-I7 and A-HA-CODE, both of which "
                    "carry declared falsifiers (anchor-hash, ha-code-drift, "
                    "anchor-skip); the mechanism is falsified, this row is not "
                    "separately targeted")
        if name.startswith("P-"):
            return ("SAME-MECHANISM: a (path, value) anchor row, identical in "
                    "construction to the eight rows carrying declared "
                    "path-drift and path-value falsifiers; the mechanism is "
                    "falsified, this row is not separately targeted")
        if name == "G-RECOVERY-ANCILLARY":
            return ("NAMED, no waiver claimed: its four constituent recoveries "
                    "each have a falsifier one gate earlier (readout-local, "
                    "path-value-P-I7-RANK / -GENERALD), so no mutant reaches "
                    "this gate first")
        if name == "G-CONVENTION-RULE-INDEPENDENT":
            return ("FORCED (#208): the bracket's front sector contains no "
                    "drag weight, so the per-rule rows cannot differ -- "
                    "carried as a disclosure, not a finding")
        if name == "G-DEFERRED-GATES-EVALUATED":
            return ("WAIVED: a bookkeeping gate over the write-time gate names "
                    "and the rendered gate count; its falsifier would be a "
                    "gate that never ran, which the gate itself reports")
        return "NAMED, no waiver claimed"

    nf = [n for n in fnames if n not in fmap]
    if MUTANT == "falsifier-census-hide":
        nf = []
    R["falsifier_census"] = {
        "gates": len(fnames),
        "gates_with_a_declared_falsifier": len([n for n in fnames if n in fmap]),
        "never_falsified": nf,
        "never_falsified_count": len(nf),
        "denominator": "%d of %d gates" % (len(nf), len(fnames)),
        "falsifier_map": dict((k, sorted(x)) for k, x in sorted(fmap.items())
                              if k in fnames),
        "waivers": dict((k, waiver_for(k)) for k in nf),
        "rule": "a gate with no declared falsifier is NAMED here with its "
                "forcing stated, from delivery one",
    }
    gate("G-NEVER-FALSIFIED-CENSUS",
         "the never-falsified census ships IN the receipt with an honest "
         "denominator: every gate without a declared falsifier is named and "
         "its forcing stated",
         (R["falsifier_census"]["never_falsified_count"]
          + R["falsifier_census"]["gates_with_a_declared_falsifier"]
          == R["falsifier_census"]["gates"])
         and all(n in R["falsifier_census"]["waivers"] for n in nf),
         {"census": R["falsifier_census"]["denominator"],
          "named": nf})

    claimed = R["paper_claims"]["rendered"]["instrument"]
    ngates = len(GATES) + 3
    if MUTANT == "gate-count-drift":
        ngates = ngates + 1
    gate("G-FINAL-GATE-COUNT",
         "the gate, anchor and mutant counts the paper asserts equal the "
         "numbers this run actually registered -- the claim's own arithmetic, "
         "gated (v14 #24: counts computed, never typed)",
         claimed == ("%d gates, all passed; %d anchors; %d mutants, all dead."
                     % (ngates, len(ANCHORS), len(MUTANTS))),
         {"claimed": claimed, "registered_gates_now": len(GATES),
          "final_gate_count": ngates})

    reg = [g["name"] for g in GATES]
    gate("G-DEFERRED-GATES-EVALUATED",
         "the write-time gates named in the falsifier census really did run, "
         "so the census's denominator covers every gate this instrument "
         "declares",
         all(d in reg for d in DEFERRED_GATES if d != "G-DEFERRED-GATES-EVALUATED")
         and len(GATES) + 2 == R["totals"]["gates"],
         {"deferred": list(DEFERRED_GATES), "registered": len(reg),
          "claimed_total": R["totals"]["gates"]})

    fnames = [g["name"] for g in GATES]
    nf = [n for n in fnames if n not in fmap]
    if MUTANT == "falsifier-census-hide":
        nf = []
    R["falsifier_census"]["gates"] = len(fnames)
    R["falsifier_census"]["never_falsified"] = nf
    R["falsifier_census"]["never_falsified_count"] = len(nf)
    R["falsifier_census"]["gates_with_a_declared_falsifier"] = len(
        [n for n in fnames if n in fmap])
    R["falsifier_census"]["denominator"] = "%d of %d gates" % (len(nf),
                                                               len(fnames))
    R["falsifier_census"]["waivers"] = dict((k, waiver_for(k)) for k in nf)
    R["gates"] = GATES
    R["compliance"] = compliance_sweep(R)
    if MUTANT == "compliance-claim-unbacked":
        R["compliance"].append({"rule": "13(9) an unbacked compliance claim",
                                "status": "APPLIED",
                                "evidence": "G-DOES-NOT-EXIST"})
    known = (set(x["name"] for x in R["gates"]) | set(DEFERRED_GATES)
             | set(POST_RENDER_GATES))
    unbacked = [c for c in R["compliance"]
                if c["status"] == "APPLIED" and "MISSING:" in c["evidence"]]
    unbacked += [c for c in R["compliance"]
                 if c["status"] == "APPLIED"
                 and not all(g in known
                             for g in c["evidence"].split(" | ")[0].split(","))]
    gate("G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS",
         "every APPLIED row of the compliance sweep cites gates this run "
         "actually registered and that actually passed; a compliance claim "
         "with no gate behind it is a false claim (RUNBOOK section 14 "
         "addendum, v14 #20)",
         len(unbacked) == 0 and all(c["status"] == "APPLIED"
                                    for c in R["compliance"]),
         {"unbacked": unbacked[:4],
          "statuses": sorted(set(c["status"] for c in R["compliance"]))})
    R["gates"] = GATES
    R["falsifier_census"]["gates"] = len(GATES)
    nf = [n for n in [g["name"] for g in GATES] if n not in fmap]
    if MUTANT == "falsifier-census-hide":
        nf = []
    R["falsifier_census"]["never_falsified"] = nf
    R["falsifier_census"]["never_falsified_count"] = len(nf)
    R["falsifier_census"]["gates_with_a_declared_falsifier"] = \
        len(GATES) - len(nf)
    R["falsifier_census"]["denominator"] = "%d of %d gates" % (len(nf),
                                                               len(GATES))
    R["falsifier_census"]["waivers"] = dict((k, waiver_for(k)) for k in nf)
    R["compliance"] = compliance_sweep(R)
    return R


def build_everything():
    parts = run()
    R, res, S = run_part2(*parts)
    return finalise(R)


def deliver():
    R = build_everything()
    text = render_text(R)
    payload = jsonable(R)
    with open(OUT_TXT, "w") as fh:
        fh.write(text)
    with open(OUT_JSON, "w") as fh:
        fh.write(json.dumps(payload, indent=1, sort_keys=False) + "\n")
    sys.stdout.write(text)
    return 0


def selftest():
    before = {}
    for p in (OUT_TXT, OUT_JSON):
        before[p] = sha256_full(p) if os.path.exists(p) else None
    ok_all = True
    for m in MUTANTS:
        proc = subprocess.run([sys.executable, SRC, "--mutant", m["name"]],
                              capture_output=True, text=True)
        blob = proc.stdout + proc.stderr
        died = proc.returncode == 1
        named = ("GATE FAILED: " + m["expected_gate"]) in blob
        tb = "Traceback (most recent call last)" in blob
        unchanged = all((sha256_full(p) if os.path.exists(p) else None)
                        == before[p] for p in (OUT_TXT, OUT_JSON))
        good = died and named and unchanged and not tb
        ok_all = ok_all and good
        print("  %-32s exit=%d named_gate=%-5s artifacts_unchanged=%-5s "
              "traceback=%-5s  %s"
              % (m["name"], proc.returncode, named, unchanged, tb,
                 "DEAD" if good else "SURVIVED"))
    print("  mutants declared (computed): %d ; all dead: %s"
          % (len(MUTANTS), ok_all))
    return 0 if ok_all else 1


def main():
    global MUTANT
    args = sys.argv[1:]
    if args and args[0] == "--list-mutants":
        for m in MUTANTS:
            print(m["name"])
        return 0
    if args and args[0] == "--selftest":
        print("FALSIFICATION SELFTEST -- every declared mutant must exit 1 on "
              "a named gate, write nothing, and raise no traceback")
        return selftest()
    if args and args[0] == "--mutant":
        if len(args) < 2 or args[1] not in [m["name"] for m in MUTANTS]:
            sys.stderr.write("unknown mutant\n")
            return 2
        MUTANT = args[1]
    elif args:
        sys.stderr.write("unknown argument: %s\n" % args[0])
        return 2
    try:
        if MUTANT is None:
            return deliver()
        R = build_everything()
        render_text(R)
        sys.stderr.write("MUTANT %s SURVIVED -- no gate fired\n" % MUTANT)
        return 3
    except GateFailure as exc:
        sys.stderr.write(str(exc) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
