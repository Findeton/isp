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
addendum, v14 #20); every span of prose read out of a pinned NOTE anchors a
CONTEXT WINDOW bound to a named consumer gate (RUNBOOK section 14 addendum,
v14 #34, verbatim-text anchors).

NO UNANCHORED RUNTIME INPUT (RUNBOOK section 14 addendum, v14 #46).  Every
file this instrument reads at run time is either a hash-pinned artifact
carrying both a byte anchor and a value anchor, or this unit's own owned
artifact (paper-03, read by the prose gate that renders it).  Mutable repo
state -- ledgers, STATUS, other units' working files -- is read by nothing
here.

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
    criterion (a non-complete overlap graph), READ BY JSON PATH out of the R2
    TERMINAL RECEIPT, is FAILED by the d=2, L=3 record lattice, whose overlap
    graph is COMPLETE at 36 of 36 pairs on 9 sites.  The criterion is applied
    here by an implementation gated against a declared positive/negative
    pair.  An attempted L=3 census run dies BY GATE.
  * THE SPANNING HYPOTHESIS (S) -- the load-bearing measurement of the whole
    {H,H} half: the realised bracket covectors Omega span the FULL declared
    link space at every site of every censused arena and lapse scope.  Every
    coefficient statement below is a corollary of (S) plus the declared
    weights; (S) itself is measured.
  * THE STRUCTURE THEOREM, verified in-unit -- rho = (W - B).Omega, so the
    metric-match condition is W == B pointwise and the coefficient class is a
    pure function of (the rule's weight field, the record's readout).  An
    ANALYTIC PREDICTOR carrying no commutator predicts every census cell's
    class and metric-match status; the agreement is gated.  The census
    clauses are therefore carried FORCED (#208).
  * THE CLOSURE CENSUS, against the DECLARED GENERATOR BASIS -- the commutator
    [H_a[N], H_a[M]] computed exactly by THREE routes and decomposed in the
    declared basis.  Two distinct questions are separated and both reported:
    BASIS CLOSURE (does the commutator lie in the declared tangential family
    at all?) and METRIC MATCH (is its coefficient the record's inverse
    metric?).  This makes the pin's RIGID branch -- closure with a constant
    NON-metric coefficient -- reachable, and it is reached.
  * STRUCTURE-COEFFICIENT EXTRACTION -- the coefficient is SOLVED FOR from the
    commutators themselves and then TYPED against an independently
    re-encoded record metric: constant / metric-reading / other, by
    measurement.
  * THE REALISATION CENSUS -- the tangential family's declared atoms are the
    site map and the address register, so a realisation is a triple
    (a, b, c) in {-1,0,1}^3: front drag, register shift, register transport.
    All 27 are censused.  D-REG = (0,1,0) and D-TOT = (1,1,0) are two of
    them; D-FULL = (1,1,1) transports the register along the same declared
    site map that already transports the front.
  * THE COVARIANCE THEOREM -- D_full[v] . H_g[N] . D_full[v]^-1 = H_{S_v g}[S_v N],
    exactly, at every cell of a derived and printed probe: conjugation by
    full transport carries the constraint of the record to the constraint of
    the TRANSPORTED record.  What survives as an obstruction is that the
    record itself does not transport: the arena carries a FIXED BACKGROUND.
  * THE NORMAL-TANGENTIAL AND TANGENTIAL BRACKETS -- {D,H} at the declared
    realisations, with the convention sweep that decides whether a mismatch
    is a convention or a defect; {D,D} as the lattice's own covariance
    closure (positive control) against a scrambled-lattice negative control.
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
                     "G-NEVER-FALSIFIED-CENSUS",
                     "G-WAIVER-CLAIMS-ARE-GATE-CLAIMS",
                     "G-FINAL-GATE-COUNT",
                     "G-DEFERRED-GATES-EVALUATED",
                     "G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS",
                     "G-PAYLOAD-SEALED")


def gates_still_to_come():
    """How many declared gates have not been registered yet -- DERIVED from
    the declaration table, never typed."""
    have = set(g["name"] for g in GATES)
    return len([n for n in POST_RENDER_GATES if n not in have])


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

# EVERY FILE THIS INSTRUMENT READS AT RUN TIME, declared here and gated by
# G-NO-UNANCHORED-RUNTIME-INPUT (RUNBOOK section 14 addendum, v14 #46).  The
# first seven carry byte anchors; the JSON among them carry (path, value)
# anchors and the note carries verbatim-text context windows; the HA source is
# byte-anchored against a hash DERIVED from the pinned receipt; the last is
# this unit's own owned artifact, read only by the prose gate that renders it.
RUNTIME_READS = sorted([
    "v13/code/ha_successor_exact.py",
    "v13/code/ha_successor_receipt.json",
    "v13/paper-ha-successor.md",
    "v14/code/r2_manifold_exact.py",
    "v14/code/r2_manifold_receipt.json",
    "v14/note-r0-founding-pin.md",
    "v14/note-r2-adjudication.md",
    "v14/note-r3-relativity-pin.md",
    "v14/paper-03-relativity-rung.md",
])

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


# VERBATIM-TEXT ANCHORS (RUNBOOK section 14 addendum, v14 #34).  A span of
# prose this unit reads out of a pinned NOTE is anchored as a CONTEXT WINDOW
# -- the surrounding sentence, not a fragment -- and every row names the gate
# that consumes it, so the anchor binds MEANING TO USE and not merely
# existence.  These rows are evaluated BEFORE the byte anchors.
TEXT_ANCHOR_ROWS = [
    ("T-R2-HANDOFF", "v14/note-r2-adjudication.md",
     "**The R3 handoff: I7's arena, L ≥ 4.**",
     "G-L-GATE-INHERITED-FACTS",
     "the R2 handoff ruling's own heading sentence: this unit's arena and its "
     "gated extent arrive together, as one clause"),
    ("T-R2-GATES-L", "v14/note-r2-adjudication.md",
     "The R3 pin poses the deformation questions on I7's own sites and "
     "**gates L ≥ 4 as a measured requirement**.",
     "G-L-GATE-INHERITED-FACTS",
     "the ruling that gates this unit's extent -- the whole sentence, so the "
     "anchor binds the requirement to its subject and not the fragment "
     "'L ≥ 4'"),
    ("T-R2-PROFILES", "v14/note-r2-adjudication.md",
     "(8,12,1,5) at d=2, (24,96,1,73) at d=3 — failing only at d=2, L=3.",
     "G-L-GATE-INHERITED-FACTS",
     "the link profiles the ruling states for this lattice together with the "
     "extent at which it fails -- quoted as inherited facts, never re-derived "
     "here"),
    ("T-R2-INHERITED", "v14/note-r2-adjudication.md",
     "the gravity record layer's own declared lattice satisfies the locality "
     "criterion, is translation-covariant, and carries a CONSISTENT "
     "chart-intrinsic dimension with a single link profile at every site",
     "G-L-GATE-INHERITED-FACTS",
     "the three inherited facts this unit rides as anchors and never "
     "re-derives (pin section 1)"),
]


def read_by_path(obj, path):
    cur = obj
    for k in path:
        cur = cur[k]
    return cur


def verify_text_anchors():
    """Evaluated FIRST: each row's context window must occur verbatim in the
    pinned note, and each row names the gate that consumes it."""
    rows = list(TEXT_ANCHOR_ROWS)
    if MUTANT == "text-anchor-skip":
        rows = rows[:-1]
    for name, rel, window, consumer, why in rows:
        text = _flat(read_text(rel))
        got = text.count(_flat(window))
        if MUTANT == "text-anchor-" + name:
            got = 0
        ANCHORS.append({"name": name, "kind": "verbatim-text", "artifact": rel,
                        "expected": window, "measured": got,
                        "consumer_gate": consumer, "provenance": why,
                        "ok": got >= 1})
        gate(name,
             "verbatim-text anchor: the context window occurs in %s and is "
             "consumed by %s" % (rel, consumer), got >= 1,
             {"window": window, "occurrences": got, "consumer": consumer})
    return len(rows)


def verify_anchors():
    rows = list(ANCHOR_ROWS)
    if MUTANT == "anchor-skip":
        rows = rows[:-1]
    for name, rel, expect, why in rows:
        path = os.path.join(ROOT, rel)
        got = sha12(path)
        if MUTANT == "anchor-hash" and name == "A-R0-I7":
            got = "0" * 12
        if MUTANT == "anchor-hash-" + name:
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
    # ROOT-relative, never CWD-relative: the instrument must resolve its
    # provenance identically from any working directory.
    got = sha12(os.path.join(ROOT, "v13/code/ha_successor_exact.py"))
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


# THE REALISATION SPACE (the tangential family's declared atoms).  I7 declares
# exactly two ingredients for D_a[v]: the SITE MAP x -> x + v(x) and the
# ADDRESS REGISTER.  A realisation is therefore a triple
#
#     (a, b, c) in {-1, 0, +1}^3
#       a  drags the geometry FRONT along the site map (a times v)
#       b  SHIFTS the address register by b times v
#       c  TRANSPORTS the register field along the SAME declared site map
#
#     D_(a,b,c)[v] : (n, m)  |->  ( S_{a v} n ,  S_{c v} m + b v )
#
# with (S_u f)(x) := f(x - u).  I7's two named realisations are two of the 27:
#   D-REG  = (0, 1, 0)   the register shifts, the front is not transported
#   D-TOT  = (1, 1, 0)   the front is dragged, the register's labelling is not
#   D-FULL = (1, 1, 1)   the register is transported along the same site map
# No new ingredient enters at (1,1,1): it is built from the two declared atoms.
NAMED_REALISATIONS = {"D-REG": (0, 1, 0), "D-TOT": (1, 1, 0),
                      "D-FULL": (1, 1, 1)}
REALISATION_ATOM_VALUES = (-1, 0, 1)


def realisation_triple(realisation):
    if isinstance(realisation, str):
        return NAMED_REALISATIONS[realisation]
    return tuple(realisation)


def realisation_name(abc):
    for k, v in sorted(NAMED_REALISATIONS.items()):
        if tuple(v) == tuple(abc):
            return k
    return "D(%d,%d,%d)" % tuple(abc)


class Dmap(object):
    """D_a[v], the tangential comparison map, at ANY declared realisation."""

    def __init__(self, rec, v, realisation="D-REG"):
        self.rec, self.v = rec, v
        self.realisation = realisation
        self.abc = realisation_triple(realisation)

    def site_map(self, k=1):
        """x -> x + k v(x) as a permutation of the site set, or None."""
        d, L = self.rec.d, self.rec.L
        out = {}
        for x in self.rec.S:
            sh = self.v[x]
            if any(Fr(t).denominator != 1 for t in sh):
                return None
            out[x] = tuple((x[i] + k * int(sh[i])) % L for i in range(d))
        return out if len(set(out.values())) == L ** d else None

    def fwd(self, c):
        n, m = c
        d = self.rec.d
        a, b, cc = self.abc
        vv = self.v
        if MUTANT == "commutator-machinery":
            vv = {x: tuple(2 * t if all(u >= 0 for u in self.v[x]) else t
                           for t in self.v[x]) for x in self.v}
        if cc:
            sm = self.site_map(cc)
            if sm is None:
                return None
            mt = {sm[x]: m[x] for x in m}
        else:
            mt = m
        m2 = {x: tuple(mt[x][i] + b * vv[x][i] for i in range(d)) for x in mt}
        if not a:
            return (n, m2)
        sma = self.site_map(a)
        if sma is None:
            return None
        return ({sma[x]: n[x] for x in n}, m2)


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


def weight_matrix(rule, rec, x, fresh=False):
    """W: Delta^i(x) = sum_l W^{il}(x) Omega_l(x)."""
    d = rec.d
    W = [[Fr(0)] * len(rec.links) for _ in range(d)]
    if rule == "A-notransport":
        return W                      # frozen front: the steps commute
    if arch_of(rule) == "A":
        Lam = lambda_of(rule, rec, x, fresh=fresh)
        for i in range(d):
            for j in range(d):
                W[i][j] = Lam[i][j]
        if MUTANT == "arch-a-diagonal-weight" and rule == "A-chart" \
                and rec.L >= CENSUS_L_MIN and x == rec.S[0]:
            W[0][len(rec.links) - 1] = Fr(1)
        return W
    lam = lambda_of(rule, rec, x, fresh=fresh)
    for li, lk in enumerate(rec.links):
        if lam[lk] == 0:
            continue
        for i in range(d):
            if lk[i]:
                W[i][li] += lam[lk] * Fr(lk[i])
    return W


def fresh_weight_matrix(rule, rec, x):
    return weight_matrix(rule, rec, x, fresh=True)


def hda_matrix(rec, x):
    """B: beta^i(x) = sum_j I^{ij}(x) Omega_{e_j}(x) -- the HDA-predicted
    tangential generator, whose coefficient is the RECORD METRIC READING."""
    d = rec.d
    B = [[Fr(0)] * len(rec.links) for _ in range(d)]
    for i in range(d):
        for j in range(d):
            B[i][j] = rec.I[x][i][j]
    return B


def fresh_gap_matrix(rule, rec, x):
    """The gap matrix with the weight memo BYPASSED -- the self-test's own
    evaluation path, so it measures the quantity and not the cache."""
    W = fresh_weight_matrix(rule, rec, x)
    B = hda_matrix(rec, x)
    return [[W[i][k] - B[i][k] for k in range(len(rec.links))]
            for i in range(rec.d)]


def gap_matrix(rule, rec, x):
    W, B = weight_matrix(rule, rec, x), hda_matrix(rec, x)
    if MUTANT == "gap-matrix-corrupt" and rule == "B-all" \
            and rec.L >= CENSUS_L_MIN:
        W = [row[:] for row in W]
        for i in range(rec.d):
            for k in range(rec.d, len(rec.links)):
                W[i][k] = Fr(0)
    return [[W[i][k] - B[i][k] for k in range(len(rec.links))]
            for i in range(rec.d)]


# ---- THE STRUCTURE THEOREM, AS AN ANALYTIC PREDICTOR -----------------------
#
# rho = (W - B).Omega, so METRIC MATCH  <=>  W == B pointwise, and (given the
# spanning hypothesis (S), measured below) the extracted coefficient is the
# axis block of W, whence the coefficient class is a PURE FUNCTION of the
# rule's weight field and the record's readout -- no commutator, no lapse, no
# bracket.  This predictor carries none of those, and is compared cell by cell
# against the census's own solve: the census clauses are FORCED (#208) and the
# gate is what establishes it.

CLASS_ZERO = "ZERO"
CLASS_MRC = "METRIC-READING-CONSTANT"
CLASS_MRSV = "METRIC-READING-SITE-VARYING"
CLASS_CNM = "CONSTANT-NON-METRIC"
CLASS_SVNM = "SITE-VARYING-NON-METRIC"
CLASS_NX = "NOT-EXTRACTABLE"


def predict_class(rule, rec):
    """The coefficient class predicted from (W, B) alone."""
    d = rec.d
    nlk = len(rec.links)
    diagcol = False
    zero = True
    metric = True
    const = True
    first = None
    for x in rec.S:
        W = weight_matrix(rule, rec, x)
        B = hda_matrix(rec, x)
        if any(W[i][k] != 0 for i in range(d) for k in range(d, nlk)):
            diagcol = True
        ax = tuple(tuple(W[i][j] for j in range(d)) for i in range(d))
        bx = tuple(tuple(B[i][j] for j in range(d)) for i in range(d))
        if any(v != 0 for row in ax for v in row):
            zero = False
        if ax != bx:
            metric = False
        if first is None:
            first = ax
        elif ax != first:
            const = False
    if MUTANT == "class-predictor-blind":
        diagcol = False
    if diagcol:
        return CLASS_NX
    if zero:
        return CLASS_ZERO
    if metric:
        return CLASS_MRSV if not const else CLASS_MRC
    return CLASS_CNM if const else CLASS_SVNM


def predict_metric_match(rule, rec):
    """W == B at every site of every link column -- the metric-match
    condition, predicted analytically."""
    d = rec.d
    nlk = len(rec.links)
    for x in rec.S:
        W, B = weight_matrix(rule, rec, x), hda_matrix(rec, x)
        for i in range(d):
            for k in range(nlk):
                if W[i][k] != B[i][k]:
                    return False
    return True


def weight_has_diagonal_column(rule, rec):
    """Does the rule put weight on a DIAGONAL link at any site?  This is the
    exact criterion for the coefficient system's inconsistency -- and the
    measured answer is that exactly one declared rule does."""
    d, nlk = rec.d, len(rec.links)
    for x in rec.S:
        W = weight_matrix(rule, rec, x)
        if any(W[i][k] != 0 for i in range(d) for k in range(d, nlk)):
            return True
    return False


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
        return {"metric_match": True, "nonzero_pairs": 0, "total_pairs": total,
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
    return {"metric_match": nz == 0, "nonzero_pairs": nz, "total_pairs": total,
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
    return {"metric_match": nz == 0, "nonzero_pairs": nz, "total_pairs": total,
            "max_abs": str(mx), "witness": wit,
            "residual_zero_sites": len(zero_sites), "sites": len(rec.S)}


def census_cell_literal(rule, rec, lapses, cfg, probe):
    """ROUTE 3 -- the residual assembled with NO reference to gap_matrix at
    all: the register displacement is read off the LITERAL four-map
    composition and the HDA generator is subtracted from it.  The two other
    routes share the gap matrix; this one shares nothing with them but the
    declared field formulae, so a corruption of the shared component is
    visible here (RUNBOOK section 14 addendum, v13 #219)."""
    d = rec.d
    nz, mx = 0, Fr(0)
    tot = 0
    for a in range(len(probe)):
        for b in range(len(probe)):
            if a == b:
                continue
            tot += 1
            _df, dr = commutator_literal(rule, rec, lapses[probe[a]][1],
                                         lapses[probe[b]][1], cfg)
            beta = hda_generator(rec, lapses[probe[a]][1],
                                 lapses[probe[b]][1])
            bad = False
            for x in rec.S:
                rho = tuple(dr[x][i] - beta[x][i] for i in range(d))
                if any(t != 0 for t in rho):
                    bad = True
                    m = max(abs(t) for t in rho)
                    if m > mx:
                        mx = m
            if bad:
                nz += 1
    return {"metric_match": nz == 0, "nonzero_pairs": nz, "pairs": tot,
            "max_abs": str(mx)}


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


_FLIP_COUNT = [0]


def type_coefficient(rec, ext, metric_route=None):
    """TYPE THE EXTRACTED COEFFICIENT BY MEASUREMENT.  The metric it is
    compared against is re-encoded by the INDEPENDENT closed-form route, not
    by the same solve that built the record."""
    st = sorted(set(v[0] for v in ext.values()))
    if st != ["UNIQUE"]:
        return {"class": CLASS_NX, "statuses": st,
                "constant": False, "metric_reading": False,
                "basis_closes": False,
                "closure_form": "NOT-IN-THE-DECLARED-BASIS",
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
    if MUTANT == "coefficient-class-flip":
        _FLIP_COUNT[0] += 1
        if _FLIP_COUNT[0] > 1:
            const = True
    metric = all(ext[x][1] == metric_route[x] for x in S)
    zero = all(all(v == 0 for row in ext[x][1] for v in row) for x in S)
    if zero:
        cl = CLASS_ZERO
    elif metric and not const:
        cl = CLASS_MRSV
    elif metric and const:
        cl = CLASS_MRC
    elif const:
        cl = CLASS_CNM
    else:
        cl = CLASS_SVNM
    return {"class": cl, "constant": const, "metric_reading": metric,
            "basis_closes": True, "closure_form": CLOSURE_FORM[cl],
            "statuses": st, "ranks": sorted(set(v[2] for v in ext.values())),
            "value_at_first_site": [[str(v) for v in row] for row in c0],
            "distinct_values": len(set(
                tuple(tuple(str(v) for v in row) for row in ext[x][1])
                for x in S))}


# THE THREE-SIDED CLOSURE VOCABULARY (pin section 2).  "Closes" now means one
# thing only: the commutator lies in the DECLARED GENERATOR BASIS.  Which form
# it closes with is a second, independent question -- and the pin's RIGID
# outcome (a constant coefficient that is demonstrably NOT a metric) is one of
# its answers, reachable and reached.
CLOSURE_FORM = {
    CLASS_MRSV: "METRIC-READING-SITE-VARYING(THE-GR-BRACKET-FORM)",
    CLASS_MRC: "METRIC-READING-CONSTANT(INDISTINGUISHABLE-FROM-RIGID-HERE)",
    CLASS_CNM: "RIGID-CONSTANT-NON-METRIC",
    CLASS_SVNM: "SITE-VARYING-NON-METRIC",
    CLASS_ZERO: "TRIVIAL-ZERO-COEFFICIENT",
    CLASS_NX: "NOT-IN-THE-DECLARED-BASIS",
}


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
    distinct_nonzero = set()
    bypass0 = CACHE_STATS["bypass"]
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
            # FRESH ON BOTH SIDES (RUNBOOK section 14 addendum, v13 #185):
            # a self-test that reaches its quantity through the instrument's
            # own memo tests the cache, not the quantity.  The base side's
            # weights are recomputed with the memo bypassed, and the miss
            # count the bypass produces is itself gated below.
            r0 = {x: tuple(sum((Fr(fresh_gap_matrix(rule, rec, x)[i][k])
                                * Fr(om0[x][k])
                                for k in range(len(rec.links))), Fr(0))
                           for i in range(d)) for x in S}
            ru = {x: tuple(sum((Fr(fresh_gap_matrix(rule, recu, x)[i][k])
                                * Fr(omu[x][k])
                                for k in range(len(rec.links))), Fr(0))
                           for i in range(d)) for x in S}
            for x in S:
                if any(t != 0 for t in r0[x]):
                    nonzero += 1
                    # the base residual does NOT depend on the translation u,
                    # so the honest non-vacuity count is the number of
                    # DISTINCT nonzero base cells, not that number times |X|
                    distinct_nonzero.add((a, b, x))
                if ru[x] == r0[add(x, tuple(-t for t in u), L)]:
                    good += 1
                else:
                    bad += 1
    if MUTANT == "covariance-break" and neighbour is None:
        good, bad = good - 1, bad + 1
    return {"covariant_cells": good, "violating_cells": bad,
            "total_cells": good + bad,
            "nonzero_base_cells_counted_once_per_translation": nonzero,
            "distinct_nonzero_base_cells": len(distinct_nonzero),
            "fresh_bypasses_used": CACHE_STATS["bypass"] - bypass0,
            "translations": len(S)}


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
                # I7's pinned table records the METRIC-MATCH condition under
                # its own field name "closes"; this unit reads that field and
                # compares it against its own metric_match, and compares every
                # other field by name.
                if cell["metric_match"] != exp["closes"]:
                    closure_bad.append([key, "metric_match",
                                        cell["metric_match"], exp["closes"]])
                for f in ("nonzero_pairs", "total_pairs", "max_abs",
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
    # the RAW keys, so the verdict comparator can re-derive the recovery
    # denominators from the pinned tables themselves rather than from a
    # counter the builder also read (#219)
    out["pinned_closure_keys"] = sorted(rec7["tables"]["closure"])
    out["pinned_sector_keys"] = sorted(rec7["tables"]["sector_law"])

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
        [nm for nm in diag if rows["A-axis|%s" % nm]["metric_match"]])
    return out


# ----------------------------------------------------------------------------
# 9.  THE CENSUS ARENAS AND THE FULL SWEEP
# ----------------------------------------------------------------------------

CENSUS_ARENAS = ((2, 4), (2, 5), (3, 4), (3, 5))
LAPSE_SCOPES = ("BASE", "TRANSLATES")
DENSE_ARENAS = ((2, 4), (2, 5))    # the dense cross-route coverage, DERIVED AND PRINTED
LITERAL_ROUTE_ARENAS = ((2, 4), (2, 5), (3, 4), (3, 5))  # derived and printed
LITERAL_PROBE_LAPSES = 6      # declared, printed, gated -- never a silent cap
DH_LITERAL_PROBE = 4
DEFECT_PROBE_LAPSES = 6
DH_PROBE_DELTAS = 6           # I7's own d=3 probe convention, reused here
REALISATIONS = ("D-REG", "D-TOT")
# The realisation census's declared scope: all 27 (a, b, c) triples, at the
# defect probe's lapse scope, over these arenas.  Derived and printed.
REALISATION_ARENAS = ((2, 4), (2, 5), (3, 4))
# The covariance theorem's declared scope.
COVARIANCE_ARENAS = ((2, 4), (3, 4))
COVARIANCE_PROBE_LAPSES = 8
CENTRAL_EXTENSION_LAPSES = 6
# the structure probes' declared arenas (derived and printed, never a silent
# cap): the central-extension identity and the commutator's
# configuration-independence are per-site facts, so one extent per dimension
# exhausts them
STRUCTURE_ARENAS = ((2, 4), (3, 4))
NONCONSTANT_ARENA = (2, 4)
NONCONSTANT_PROBE_LAPSES = 6


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


def route3_probe(rec, lapses):
    """ROUTE 3'S OWN PROBE, DERIVED so that EVERY declared link direction is
    realised by some ordered pair.  A residual route whose probe never
    realises a link cannot see a corruption living on that link's column --
    the silent-cap failure in miniature -- so the probe is built as the site
    delta at the origin together with the site delta at the origin plus each
    declared link, and the coverage it achieves is MEASURED and gated."""
    S = rec.S
    want = [S[0]] + [add(S[0], lk, rec.L) for lk in rec.links]
    idx = {}
    for k, (nm, N) in enumerate(lapses):
        for y in want:
            if nm == "delta%s" % (y,):
                idx[y] = k
    return [idx[y] for y in want if y in idx]


def route3_links_realised(rec, lapses, probe):
    """Which declared link directions the probe actually realises."""
    seen = set()
    NB = neighbours(rec.d, rec.L)
    for a in probe:
        for b in probe:
            if a == b:
                continue
            N, M = lapses[a][1], lapses[b][1]
            for x in rec.S:
                for li, y in enumerate(NB[x]):
                    if N[x] * M[y] - M[x] * N[y] != 0:
                        seen.add(li)
    if MUTANT == "route3-probe-blind":
        seen.discard(len(rec.links) - 1)
    return sorted(seen)


def degenerate_lapses(rec):
    """THE DEGENERATE PROBES, built and MEASURED (never typed).  The boundary
    test asks whether the defect's lattice sum can be nonzero; a test that
    could not also produce a ZERO sum would be vacuous, so the constant lapse
    profiles are carried as their own labelled rows:

      N == 0   the ZERO field.  Both terms of the defect carry an explicit
               factor N, so the defect field is identically zero and its
               lattice sum is zero -- the test's own death certificate.
      N == 1   the unit constant profile.  S_v N - N == 0, so the second term
               vanishes; whether the first does is a MEASUREMENT, and it is
               reported next to the zero row.

    Neither profile is in the defect probe set (which is the first six site
    deltas), so both are genuine additions."""
    return [("zero", {x: 0 for x in rec.S}, True),
            ("one", {x: 1 for x in rec.S}, False)]


def nonconstant_tangential_fields(d, L):
    """DECLARED non-constant tangential fields whose site maps are bijections
    of the site set and whose negatives invert them -- both properties
    MEASURED, not assumed.  They test whether the defect is an artefact of
    restricting v to the lattice's own translations."""
    def shear(x):
        return tuple(x[1] if i == 0 else 0 for i in range(d))

    def parity(x):
        return tuple((x[1] % 2) if i == 0 else 0 for i in range(d))

    def constant(x):
        return tuple(1 if i == 0 else 0 for i in range(d))
    if MUTANT == "nonconstant-field-degenerate":
        return [("shear", constant), ("parity-kick", constant)]
    return [("shear", shear), ("parity-kick", parity)]


def run_census(decl, rec7):
    """The closure census, the coefficient extraction and the bracket census
    over every declared arena.  Cell-complete; every count derived."""
    census, coeffs, dh_rows, dd_rows, conv_rows = [], [], [], [], []
    decomp_rows, defect_rows = [], []
    spanning_rows, realisation_rows, covariance_rows = [], [], []
    degenerate_rows, order_rows, nonconstant_rows = [], [], []
    duplicate_rows, central_rows = [], []
    two_route = {"dense_cells": 0, "dense_disagreements": [],
                 "literal_cells": 0, "literal_disagreements": [],
                 "dh_literal_cells": 0, "dh_literal_disagreements": [],
                 "conv_literal_cells": 0, "conv_literal_disagreements": [],
                 "route3_cells": 0, "route3_disagreements": [],
                 "realisation_literal_cells": 0,
                 "realisation_literal_disagreements": [],
                 "class_prediction_cells": 0, "class_mispredictions": [],
                 "metric_identity_sites": 0, "metric_identity_failures": 0,
                 "metric_match_prediction_mismatches": [],
                 "dense_arenas": [list(a) for a in DENSE_ARENAS],
                 "route3_arenas": [list(a) for a in LITERAL_ROUTE_ARENAS],
                 "route3_links_realised": {},
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

        # ---- 0. HYPOTHESIS (S): THE SPANNING CENSUS ----------------------
        # Omega depends only on the lapse pair and the lattice, so the rank is
        # measured once per (arena, scope) -- and the record-independence is
        # itself measured, at two records, rather than assumed.
        for scope in LAPSE_SCOPES:
            sr = spanning_rank_census(recs[adm[0]], fams[scope])
            check = spanning_rank_census(recs[adm[-1]], fams[scope])
            sr.update({"d": d, "L": L, "scope": scope,
                       "record_probe": [adm[0], adm[-1]],
                       "record_independent": (
                           sr["sites_at_full_rank"] == check["sites_at_full_rank"]
                           and sr["ranks"] == check["ranks"])})
            spanning_rows.append(sr)

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
                    ext = extract_coefficient(rule, rec, lapses, sup)
                    typ = type_coefficient(rec, ext)
                    row = {"d": d, "L": L, "scope": scope, "rule": rule,
                           "record": nm, "homogeneous": rec.homogeneous}
                    row.update(cell)
                    row["basis_closes"] = typ["basis_closes"]
                    row["closure_form"] = typ["closure_form"]
                    row["rigid"] = (typ["class"] == CLASS_CNM)
                    census.append(row)
                    coeffs.append({"d": d, "L": L, "scope": scope,
                                   "rule": rule, "record": nm,
                                   "homogeneous": rec.homogeneous,
                                   "coefficient": typ})
                    # THE ANALYTIC PREDICTOR (the structure theorem), compared
                    # cell by cell against the solve -- an INDEPENDENT
                    # comparator carrying no commutator (#219).
                    if typ["metric_reading"]:
                        mo, mb = metric_comparator_without_inversion(rec, ext)
                        two_route["metric_identity_sites"] += mo
                        two_route["metric_identity_failures"] += mb
                    pc = predict_class(rule, rec)
                    pm = predict_metric_match(rule, rec)
                    two_route["class_prediction_cells"] += 1
                    if pc != typ["class"]:
                        two_route["class_mispredictions"].append(
                            [d, L, scope, rule, nm, typ["class"], pc])
                    if pm != cell["metric_match"]:
                        two_route["metric_match_prediction_mismatches"].append(
                            [d, L, scope, rule, nm, cell["metric_match"], pm])
                    if (d, L) in DENSE_ARENAS and scope == "BASE":
                        dn = census_cell_dense(rule, rec, lapses)
                        two_route["dense_cells"] += 1
                        for f in ("metric_match", "nonzero_pairs",
                                  "total_pairs", "max_abs", "witness",
                                  "residual_zero_sites"):
                            if cell[f] != dn[f]:
                                two_route["dense_disagreements"].append(
                                    [d, L, rule, nm, f, cell[f], dn[f]])
                    # ROUTE 3: the residual assembled from the LITERAL
                    # composition, sharing no component with the other two.
                    if (d, L) in LITERAL_ROUTE_ARENAS and scope == "BASE":
                        pr = route3_probe(rec, lapses)
                        lk = route3_links_realised(rec, lapses, pr)
                        two_route["route3_links_realised"][
                            "d%dL%d" % (d, L)] = [len(lk), len(rec.links)]
                        lit = census_cell_literal(
                            rule, rec, lapses, cfgs[0], pr)
                        two_route["route3_cells"] += 1
                        if lit["nonzero_pairs"] > 0 and cell["metric_match"]:
                            two_route["route3_disagreements"].append(
                                [d, L, rule, nm, "metric_match", True,
                                 lit["nonzero_pairs"]])
                        if Fr(lit["max_abs"]) > Fr(cell["max_abs"]):
                            two_route["route3_disagreements"].append(
                                [d, L, rule, nm, "max_abs", cell["max_abs"],
                                 lit["max_abs"]])

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
                    if not (MUTANT == "dh-row-drop" and rule == rules[-1]
                            and nm == adm[-1] and real == REALISATIONS[-1]
                            and (d, L) == arenas[-1]):
                        dh_rows.append({"d": d, "L": L, "rule": rule,
                                        "record": nm, "realisation": real,
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
                ok = bad = info = 0
                for a in tgens + [tuple([0] * d)]:
                    for b in tgens + [tuple([0] * d)]:
                        r = dd_bracket(rec, const_field(rec, a),
                                       const_field(rec, b), cfgs[0], real)
                        if r:
                            ok += 1
                        else:
                            bad += 1
                        # INFORMATIVE = two DISTINCT NONZERO generators.  The
                        # rest pair a generator with itself or with zero and
                        # cannot discriminate anything.
                        if a != b and any(a) and any(b):
                            info += 1
                if MUTANT == "dd-content-inflate":
                    info = ok + bad
                if MUTANT == "dd-row-drop" and nm == adm[-1] \
                        and real == REALISATIONS[-1] and (d, L) == arenas[-1]:
                    continue
                dd_rows.append({"d": d, "L": L, "record": nm,
                                "realisation": real, "closing": ok,
                                "non_closing": bad, "total": ok + bad,
                                "informative": info,
                                "lie_bracket_nonzero": 0})

        # ---- 6. THE CONVENTION SWEEP -------------------------------------
        # HONEST DENOMINATOR.  The front sector's independence of the record
        # and of the drag rule is MEASURED here (not asserted, and not left to
        # a divisibility identity): the front closed form is evaluated at
        # every declared record and every declared rule on a probe, and the
        # rows are compared for equality.  The sweep's own denominator is then
        # the number of DISTINCT front-sector probes actually evaluated --
        # (lapse x translation) -- and the record x rule multiplicity is
        # reported separately as a derived multiplier, never folded in
        # silently.
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
        n_probe = len(base) * len(tgens)
        mult = len(adm) * len(rules)
        for order in BRACKET_ORDERS:
            for (cname, cfn) in LIE_CONVENTIONS:
                ok = conv_hits.get((order, cname), 0)
                if MUTANT == "convention-sweep-truncate" and \
                        order == "H-D-Hinv-Dinv" and cname == "BACKWARD":
                    ok = 0
                conv_rows.append({"d": d, "L": L, "order": order,
                                  "difference": cname, "front_matches": ok,
                                  "front_probes": n_probe,
                                  "record_rule_multiplicity": mult,
                                  "brackets_derived_by_multiplication":
                                      n_probe * mult})
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

        # ---- 6b. THE DECLARED FRONT-SECTOR INDEPENDENCE, MEASURED ---------
        # (this replaces a divisibility identity with the measurement whose
        #  truth licenses the multiplication above)
        indep_bad = []
        ref = None
        for nm in adm:
            for rule in rules[:2]:
                sig = []
                for (lname, N) in base[:DH_LITERAL_PROBE]:
                    for tv in tgens:
                        v = const_field(recs[nm], tv)
                        for order in BRACKET_ORDERS:
                            fr = dh_front_closed(recs[nm], N, v, order)
                            sig.append(tuple(fr[x] for x in recs[nm].S))
                sig = tuple(sig)
                if MUTANT == "front-independence-break" and nm == adm[-1]:
                    sig = sig + (1,)
                if ref is None:
                    ref = sig
                elif sig != ref:
                    indep_bad.append([d, L, rule, nm])
        two_route.setdefault("front_independence_rows", 0)
        two_route["front_independence_rows"] += len(adm) * 2
        two_route.setdefault("front_independence_disagreements", [])
        two_route["front_independence_disagreements"].extend(indep_bad)

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
                if MUTANT == "defect-row-drop" and rule == rules[-1] \
                        and nm == adm[-1] and (d, L) == arenas[-1]:
                    continue
                defect_rows.append(
                    {"d": d, "L": L, "rule": rule, "record": nm,
                     "homogeneous": rec.homogeneous, "probes": ntot,
                     "vanishing_probes": nzero, "lattice_sum_zero": bsum,
                     "max_abs": str(mx)})

        # ---- 7b. THE DEGENERATE PROBES (the boundary test's own control) --
        for nm in adm[:2]:
            rec = recs[nm]
            for rule in rules[:3]:
                for (lname, N, expect_zero) in degenerate_lapses(rec):
                    nzero = ntot = bsum = 0
                    for tv in tgens:
                        v = const_field(rec, tv)
                        fld = dh_defect_field(rule, rec, N, v, cfgs[0])
                        ntot += 1
                        if all(all(t == 0 for t in fld[x]) for x in rec.S):
                            nzero += 1
                        if all(sum((fld[x][i] for x in rec.S), Fr(0)) == 0
                               for i in range(d)):
                            bsum += 1
                    if MUTANT == "degenerate-probe-typed" and lname == "zero":
                        nzero, bsum = 0, 0
                    degenerate_rows.append(
                        {"d": d, "L": L, "rule": rule, "record": nm,
                         "lapse": lname, "declared_degenerate": expect_zero,
                         "probes": ntot, "vanishing_probes": nzero,
                         "lattice_sum_zero": bsum})

        # ---- 7c. THE OTHER BRACKET ORDER ----------------------------------
        for order in BRACKET_ORDERS:
            nz = tot = 0
            for nm in adm:
                rec = recs[nm]
                for rule in rules:
                    for (lname, N) in dh_lapses[:DEFECT_PROBE_LAPSES]:
                        for tv in tgens:
                            sgn = tv if order == BRACKET_ORDERS[0] \
                                else tuple(-t for t in tv)
                            v = const_field(rec, sgn)
                            fld = dh_defect_field(rule, rec, N, v, cfgs[0])
                            tot += 1
                            if any(any(t != 0 for t in fld[x])
                                   for x in rec.S):
                                nz += 1
            order_rows.append({"d": d, "L": L, "order": order,
                               "probes": tot, "nonzero": nz})
    return {"census": census, "coefficients": coeffs, "dh": dh_rows,
            "dd": dd_rows, "conventions": conv_rows, "two_route": two_route,
            "decomposition": decomp_rows, "defect": defect_rows,
            "spanning": spanning_rows, "realisation": realisation_rows,
            "covariance": covariance_rows, "degenerate": degenerate_rows,
            "orders": order_rows, "nonconstant": nonconstant_rows,
            "duplicates": duplicate_rows, "central_extension": central_rows}


def run_realisation_census(decl, res):
    """THE REALISATION CENSUS -- all 27 (a, b, c) triples built from the
    tangential family's two declared atoms, at the defect probe's declared
    lapse scope, over the declared realisation arenas.  Every count derived
    and printed; no silent cap."""
    rows = []
    literal_cells = 0
    literal_bad = []
    abcs = [(a, b, c) for a in REALISATION_ATOM_VALUES
            for b in REALISATION_ATOM_VALUES for c in REALISATION_ATOM_VALUES]
    for (d, L) in REALISATION_ARENAS:
        recs = build_records(d, L, decl)
        adm = sorted([n for n in recs if recs[n].admissible])
        rules = rules_at(d, decl)
        cfgs = declared_configurations(d, L)
        tgens = lattice_translation_generators(d)
        base = build_lapse_family(d, L)
        lap = dh_probe_family(d, L, base)[:DEFECT_PROBE_LAPSES]
        tal = dict((abc, {}) for abc in abcs)
        hom = dict((abc, {}) for abc in abcs)
        resist = dict((abc, set()) for abc in abcs)
        for nm in adm:
            rec = recs[nm]
            for rule in rules:
                for (lname, N) in lap:
                    for tv in tgens:
                        pieces = realisation_pieces(rule, rec, N, tv, cfgs)
                        for abc in abcs:
                            st = classify_realisation(rec, tv, abc, pieces,
                                                      len(cfgs))
                            tal[abc][st] = tal[abc].get(st, 0) + 1
                            if rec.homogeneous:
                                hom[abc][st] = hom[abc].get(st, 0) + 1
                            if st == "OUTSIDE":
                                resist[abc].add("%s|%s" % (rule, nm))
        for abc in abcs:
            rows.append({"d": d, "L": L, "realisation": list(abc),
                         "name": realisation_name(abc),
                         "tally": dict(sorted(tal[abc].items())),
                         "homogeneous_tally": dict(sorted(hom[abc].items())),
                         "resisting_cells": sorted(resist[abc]),
                         "classifications": sum(tal[abc].values())})
        # TWO ROUTES: the closed form against the LITERAL four-map composition
        for nm in adm[:2]:
            rec = recs[nm]
            for rule in rules[:2]:
                for (lname, N) in lap[:2]:
                    for tv in tgens[:1]:
                        pieces = realisation_pieces(rule, rec, N, tv, cfgs)
                        for abc in ((0, 1, 0), (1, 1, 0), (1, 1, 1),
                                    (-1, 1, -1), (1, 0, 1)):
                            a1 = classify_realisation(rec, tv, abc, pieces,
                                                      len(cfgs))
                            a2 = dh_membership(rule, rec, N,
                                               const_field(rec, tv), cfgs,
                                               abc, "D-H-Dinv-Hinv")[0]
                            literal_cells += 1
                            if a1 != a2:
                                literal_bad.append([d, L, rule, nm,
                                                    list(abc), a1, a2])
    return {"rows": rows, "literal_cells": literal_cells,
            "literal_disagreements": literal_bad,
            "arenas": [list(a) for a in REALISATION_ARENAS],
            "atoms": list(REALISATION_ATOM_VALUES),
            "lapse_probe": DEFECT_PROBE_LAPSES}


def run_covariance_theorem(decl):
    """THE COVARIANCE THEOREM, measured at every cell of a derived probe."""
    rows = []
    cells = full_ok = tot_ok = 0
    for (d, L) in COVARIANCE_ARENAS:
        recs = build_records(d, L, decl)
        adm = sorted([n for n in recs if recs[n].admissible])
        rules = rules_at(d, decl)
        cfgs = declared_configurations(d, L)
        tgens = lattice_translation_generators(d)
        base = build_lapse_family(d, L)
        lap = dh_probe_family(d, L, base)[:COVARIANCE_PROBE_LAPSES]
        a_ok = a_tot = a_cells = 0
        for nm in adm:
            rec = recs[nm]
            for rule in rules:
                for (lname, N) in lap:
                    for tv in tgens:
                        f, t = covariance_cell(rule, rec, N, tv, cfgs)
                        a_cells += 1
                        a_ok += 1 if f else 0
                        a_tot += 1 if t else 0
        rows.append({"d": d, "L": L, "cells": a_cells,
                     "d_full_covariant": a_ok, "d_tot_covariant": a_tot,
                     "lapse_probe": len(lap), "configurations": len(cfgs)})
        cells += a_cells
        full_ok += a_ok
        tot_ok += a_tot
    return {"rows": rows, "cells": cells, "d_full_covariant": full_ok,
            "d_tot_covariant": tot_ok,
            "arenas": [list(a) for a in COVARIANCE_ARENAS],
            "lapse_probe": COVARIANCE_PROBE_LAPSES,
            "statement": "D_full[v] . H_g[N] . D_full[v]^-1 = H_{S_v g}[S_v N]"}


def run_structure_probes(decl):
    """The central extension, the commutator's configuration-independence,
    the duplicate-rule census, and the non-constant tangential fields."""
    out = {"central_extension": [], "config_independence": [],
           "duplicates": [], "nonconstant": [],
           "arenas": [list(a) for a in STRUCTURE_ARENAS],
           "lapse_probe": CENTRAL_EXTENSION_LAPSES}
    for (d, L) in STRUCTURE_ARENAS:
        recs = build_records(d, L, decl)
        adm = sorted([n for n in recs if recs[n].admissible])
        rules = rules_at(d, decl)
        cfgs = declared_configurations(d, L)
        base = build_lapse_family(d, L)
        lap = base[:CENTRAL_EXTENSION_LAPSES]
        ok = tot = 0
        same = diff = 0
        for nm in adm:
            rec = recs[nm]
            for rule in rules:
                for (an, N) in lap:
                    for (bn, M) in lap:
                        tot += 1
                        ok += 1 if central_extension_cell(rule, rec, N, M,
                                                          cfgs[0]) else 0
                        if an == bn:
                            continue
                        vals = [commutator_literal(rule, rec, N, M, n0)[1]
                                for n0 in cfgs]
                        if all(v == vals[0] for v in vals):
                            same += 1
                        else:
                            diff += 1
        out["central_extension"].append(
            {"d": d, "L": L, "cells": tot, "cocycle_identity_holds": ok})
        out["config_independence"].append(
            {"d": d, "L": L, "pairs": same + diff,
             "configuration_independent": same})
        # duplicate rules, by sector
        rl = [recs[nm] for nm in adm]
        out["duplicates"].append(
            {"d": d, "L": L, "declared_rules": len(rules),
             "distinct_in_the_HH_weight":
                 rule_equivalence_classes(rl, rules, weight_matrix),
             "distinct_in_the_register_drag":
                 rule_equivalence_classes(rl, rules, drag_matrix)})
    # non-constant bijective tangential fields
    d, L = NONCONSTANT_ARENA
    recs = build_records(d, L, decl)
    adm = sorted([n for n in recs if recs[n].admissible])
    rules = rules_at(d, decl)
    cfgs = declared_configurations(d, L)
    lap = build_lapse_family(d, L)[:NONCONSTANT_PROBE_LAPSES]
    for (fname, ff) in nonconstant_tangential_fields(d, L):
        tal = {}
        rec0 = recs[adm[0]]
        v0 = {x: tuple(Fr(t) for t in ff(x)) for x in rec0.S}
        dm = Dmap(rec0, v0, "D-TOT")
        dmi = Dmap(rec0, neg_field(v0), "D-TOT")
        sm, smi = dm.site_map(1), dmi.site_map(1)
        bij = sm is not None and smi is not None
        inv = bij and all(smi[sm[x]] == x for x in rec0.S)
        const = all(v0[x] == v0[rec0.S[0]] for x in rec0.S)
        for nm in adm:
            rec = recs[nm]
            v = {x: tuple(Fr(t) for t in ff(x)) for x in rec.S}
            for rule in rules:
                for (lname, N) in lap:
                    st, _u = dh_membership(rule, rec, N, v, cfgs, "D-TOT",
                                           "D-H-Dinv-Hinv")
                    tal[st] = tal.get(st, 0) + 1
        out["nonconstant"].append(
            {"d": d, "L": L, "field": fname, "site_map_is_a_bijection": bij,
             "negative_inverts_it": inv, "field_is_constant": const,
             "tally": dict(sorted(tal.items())),
             "probes": sum(tal.values())})
    return out


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


_PROBE_COUNT = [0]


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
    if MUTANT == "defect-zero-all-but-one":
        # the R6a Y1 class: erase the field at every probe but the first, so
        # the defect would read as vanishing almost everywhere, as a boundary
        # term, and as switching off on the homogeneous sector
        _PROBE_COUNT[0] += 1
        if _PROBE_COUNT[0] > 1:
            return {x: tuple(Fr(0) for _ in range(d)) for x in rec.S}
    out = {x: tuple(reg[x][i] - hreg[x][i] for i in range(d)) for x in rec.S}
    if MUTANT == "boundary-lax":
        tot = [sum((out[x][i] for x in rec.S), Fr(0)) for i in range(d)]
        z, a1, a2 = rec.S[0], rec.S[1], rec.S[2]
        out[z] = tuple(out[z][i] - tot[i] for i in range(d))
        # a sum-preserving perturbation, so the field stays nonzero and the
        # injection attacks the BOUNDARY clause and not the vanishing one
        out[a1] = tuple(out[a1][i] + 1 for i in range(d))
        out[a2] = tuple(out[a2][i] - 1 for i in range(d))
    return out


# ----------------------------------------------------------------------------
# 9b.  THE REALISATION CENSUS, THE COVARIANCE THEOREM, AND THE STRUCTURE OF
#      THE FIRST BRACKET
# ----------------------------------------------------------------------------
#
# CLOSED FORM at the realisation (a, b, c), for a CONSTANT translation field v
# (derived from the skew-product structure, verified against the literal
# four-map composition by G-REALISATION-TWO-ROUTES):
#
#     front    =  S_{a v} N - N
#     register =  S_{c v}( w[N, S_{-a v}(n - N)] )  -  w[N, n - N]
#
# The register SHIFT b cancels identically -- a measured fact, printed.

def _shift(f, u, L, d):
    return {x: f[tuple((x[i] - u[i]) % L for i in range(d))] for x in f}


def realisation_pieces(rule, rec, N, tv, cfgs):
    """Per (rule, record, lapse) pieces shared by every (a, b, c) and every
    direction: one drag per configuration for the base, and one pair of drags
    per distinct front-drag displacement."""
    d, L = rec.d, rec.L
    base = [{x: n0[x] - N[x] for x in rec.S} for n0 in cfgs]
    w0 = [drag(rule, rec, N, b) for b in base]
    out = {}
    for a in REALISATION_ATOM_VALUES:
        av = tuple(a * t for t in tv)
        front = {x: N[tuple((x[i] - av[i]) % L for i in range(d))] - N[x]
                 for x in rec.S}
        w1, hr = [], []
        for k, n0 in enumerate(cfgs):
            sm = {x: base[k][tuple((x[i] + av[i]) % L for i in range(d))]
                  for x in rec.S}
            w1.append(drag(rule, rec, N, sm))
            hr.append(drag(rule, rec, dict(front), n0))
        out[a] = (front, w1, hr)
    return w0, out


def classify_realisation(rec, tv, abc, pieces, ncfg):
    """IDENTITY / IN-CONSTRAINT / IN-EXTENDED / OUTSIDE at (a, b, c)."""
    d, L = rec.d, rec.L
    a, b, c = abc
    w0, byfront = pieces
    front, w1, hr = byfront[a]
    cv = tuple(c * t for t in tv)
    ident = all(front[x] == 0 for x in rec.S)
    okH = True
    diffs = []
    for k in range(ncfg):
        reg = {}
        for x in rec.S:
            y = tuple((x[i] - cv[i]) % L for i in range(d))
            reg[x] = tuple(w1[k][y][i] - w0[k][x][i] for i in range(d))
        if any(any(t != 0 for t in reg[x]) for x in rec.S):
            ident = False
        if any(reg[x] != hr[k][x] for x in rec.S):
            okH = False
        diffs.append({x: tuple(reg[x][i] - hr[k][x][i] for i in range(d))
                      for x in rec.S})
    if MUTANT == "realisation-blind" and abc == (1, 1, 1):
        return "IN-CONSTRAINT"
    if ident:
        return "IDENTITY"
    if okH:
        return "IN-CONSTRAINT"
    if all(diffs[k] == diffs[0] for k in range(len(diffs))):
        return "IN-EXTENDED"
    return "OUTSIDE"


def transported_record(rec, u):
    """The record whose counts are the TRANSPORTED counts, g'(x) = g(x - u).
    Built by transporting the count field and re-reading the metric through
    the same declared readout, never by copying the metric."""
    d, L = rec.d, rec.L
    inv = {x: tuple((x[i] - u[i]) % L for i in range(d)) for x in rec.S}
    return GeomRecord(rec.name + "@" + str(tuple(u)), d, L,
                      lambda x, lk: rec.counts[inv[x]][lk], rec.weight)


def covariance_cell(rule, rec, N, tv, cfgs):
    """THE COVARIANCE THEOREM, one cell.  Conjugation by FULL transport:

        D_full[v] . H_g[N] . D_full[v]^-1   ==   H_{S_v g}[S_v N]

    tested as a MAP identity at every declared configuration.  The same cell
    is tested at D-TOT (the register untransported) as the negative side."""
    d, L = rec.d, rec.L
    recu = transported_record(rec, tv)
    SN = {x: N[tuple((x[i] - tv[i]) % L for i in range(d))] for x in rec.S}
    full = tot = True
    for n0 in cfgs:
        m0 = {x: tuple(Fr(0) for _ in range(d)) for x in rec.S}
        c = (dict(n0), dict(m0))
        c = Dmap(rec, const_field(rec, tuple(-t for t in tv)), "D-FULL").fwd(c)
        c = Hmap(rule, rec, N).fwd(c)
        mid = c
        c = Dmap(rec, const_field(rec, tv), "D-FULL").fwd(c)
        rhs_n = {x: n0[x] + SN[x] for x in rec.S}
        wr = drag(rule, recu, SN, n0)
        rhs_m = {x: tuple(m0[x][i] + wr[x][i] for i in range(d))
                 for x in rec.S}
        if MUTANT == "covariance-theorem-blind":
            # conjugation is made to land on the UNtransported record's
            # constraint, which is what the theorem denies
            wr0 = drag(rule, rec, SN, n0)
            rhs_m = {x: tuple(m0[x][i] + wr0[x][i] for i in range(d))
                     for x in rec.S}
        if not (c[0] == rhs_n and c[1] == rhs_m):
            full = False
        # D-TOT: the front is transported back but the register field is not
        tot_c = (c[0], mid[1])
        if not (tot_c[0] == rhs_n and tot_c[1] == rhs_m):
            tot = False
    return full, tot


def central_extension_cell(rule, rec, N, M, n0):
    """H[N] H[M] == T_{w[N,M]} . H[N+M] -- the two-cocycle identity that names
    the object the first bracket lives in."""
    d = rec.d
    m0 = {x: tuple(Fr(0) for _ in range(d)) for x in rec.S}
    c = Hmap(rule, rec, M).fwd((dict(n0), dict(m0)))
    c = Hmap(rule, rec, N).fwd(c)
    NM = {x: N[x] + M[x] for x in rec.S}
    c2 = Hmap(rule, rec, NM).fwd((dict(n0), dict(m0)))
    w = drag(rule, rec, N, M)
    if MUTANT == "cocycle-blind":
        w = {x: tuple(Fr(0) for _ in range(d)) for x in rec.S}
    c2 = (c2[0], {x: tuple(c2[1][x][i] + w[x][i] for i in range(d))
                  for x in rec.S})
    return c[0] == c2[0] and c[1] == c2[1]


def spanning_rank_census(rec, lapses):
    """HYPOTHESIS (S): do the realised bracket covectors Omega span the FULL
    declared link space at every site?  This is the load-bearing measurement
    of the whole {H,H} half -- every uniqueness statement about the extracted
    coefficient is a corollary of it.  Omega depends only on (N, M) and the
    lattice, never on the record or the rule, so one record per arena-scope
    exhausts it -- and that independence is itself gated."""
    nlk = len(rec.links)
    rows = {x: [] for x in rec.S}
    n = len(lapses)
    NB = neighbours(rec.d, rec.L)
    remaining = set(rec.S)
    for a in range(n):
        if not remaining:
            break
        Na = lapses[a][1]
        for b in range(n):
            if a == b or not remaining:
                continue
            Nb = lapses[b][1]
            for x in list(remaining):
                if len(rows[x]) == nlk:
                    remaining.discard(x)
                    continue
                Ax, Bx = Na[x], Nb[x]
                if not Ax and not Bx:
                    continue
                r = [Fr(Ax * Nb[y] - Bx * Na[y]) for y in NB[x]]
                for br in rows[x]:
                    p = next(k for k in range(nlk) if br[k] != 0)
                    if r[p] != 0:
                        f = r[p] * qinv(br[p])
                        r = [r[k] - f * br[k] for k in range(nlk)]
                if any(t != 0 for t in r):
                    rows[x].append(r)
                    if len(rows[x]) == nlk:
                        remaining.discard(x)
    ranks = sorted(set(len(rows[x]) for x in rec.S))
    if MUTANT == "spanning-blind":
        ranks = [nlk - 1]
    return {"sites": len(rec.S), "link_space_dimension": nlk,
            "sites_at_full_rank": len([x for x in rec.S
                                       if len(rows[x]) == nlk]),
            "ranks": ranks}


def metric_comparator_without_inversion(rec, ext):
    """A THIRD ROUTE TO THE METRIC COMPARISON, sharing no inversion routine
    with either of the other two.  The extraction reaches q through the exact
    linear solve and the type comparator through the closed form, but BOTH
    invert it with the same primitive.  Here the extracted coefficient c is
    multiplied by q directly and compared against the identity -- no inverse
    is taken anywhere -- so a corruption of the inversion routine is visible."""
    d = rec.d
    ok = bad = 0
    for x in rec.S:
        st, c, _rk = ext[x]
        if st != "UNIQUE" or c is None:
            continue
        q = rec.q[x]
        prod = [[sum((c[i][k] * q[k][j] for k in range(d)), Fr(0))
                 for j in range(d)] for i in range(d)]
        if MUTANT == "metric-comparator-blind":
            prod = [[prod[i][j] + 1 for j in range(d)] for i in range(d)]
        if all(prod[i][j] == (1 if i == j else 0)
               for i in range(d) for j in range(d)):
            ok += 1
        else:
            bad += 1
    return ok, bad


def rule_equivalence_classes(rec_list, rules, fn):
    """Which declared rules are the SAME rule at this sector?  The signature
    is the rule's whole weight field over every admissible record and site."""
    cls = {}
    for rule in rules:
        sig = []
        for rec in rec_list:
            for x in rec.S:
                sig.append(tuple(tuple(row) for row in fn(rule, rec, x)))
        if MUTANT == "duplicate-rules-hidden":
            sig.append(rule)
        cls.setdefault(tuple(sig), []).append(rule)
    return sorted([sorted(v) for v in cls.values()])


# ----------------------------------------------------------------------------
# 10.  THE L GATE'S MEASURED REASON, AND THE INHERITED FACTS RE-CONFIRMED
# ----------------------------------------------------------------------------

def criterion_probe(criterion_text):
    """THE INHERITED CRITERION, APPLIED -- and gated against a declared
    positive/negative pair, so the implementation is a measurement and not a
    restatement of the criterion's words.  The criterion itself is READ BY
    JSON PATH out of the R2 terminal receipt (P-R2-CRITERION); this function
    is this unit's implementation of it, and the two declared graphs below
    fix what the implementation must say.

      POSITIVE (locality exists): a graph with a component that is NOT
      complete -- the 3-vertex path a-b-c, whose single component misses the
      pair (a, c).
      NEGATIVE (locality does not exist): the complete graph on 3 vertices.
    """
    def some_component_not_complete(vertices, edges):
        parent = {v: v for v in vertices}

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        for (a, b) in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
        comps = {}
        for v in vertices:
            comps.setdefault(find(v), []).append(v)
        eset = set(frozenset(e) for e in edges)
        for members in comps.values():
            n = len(members)
            need = n * (n - 1) // 2
            have = sum(1 for i in range(n) for j in range(i + 1, n)
                       if frozenset((members[i], members[j])) in eset)
            if have != need:
                return True
        return False

    pos = some_component_not_complete(["a", "b", "c"], [("a", "b"), ("b", "c")])
    neg = some_component_not_complete(["a", "b", "c"],
                                      [("a", "b"), ("b", "c"), ("a", "c")])
    if MUTANT == "criterion-blind":
        pos = neg
    return {"criterion_read_from_the_r2_terminal_receipt": criterion_text,
            "positive_control_path_graph_has_locality": pos,
            "negative_control_complete_graph_has_locality": neg,
            "implementation_agrees_with_the_inherited_criterion":
                (pos is True and neg is False)}


def l_gate_reason(criterion_text, r2_locality_count, r2_refusal_count):
    """The R2 handoff's L >= 4 requirement, with its reason MEASURED here.

    NO UNANCHORED RUNTIME INPUT (RUNBOOK section 14 addendum, v14 #46).  The
    inherited criterion arrives as a (path, value) read from the R2 TERMINAL
    RECEIPT; the R2 ruling's own sentences arrive as VERBATIM-TEXT anchors
    with context windows; the overlap fractions are RECOMPUTED here from
    I7's lattice and are this unit's own measurement.  Nothing is read from
    mutable repo state, and no verdict segment is a function of a prose
    coincidence.
    """
    rows = []
    for (d, L) in ((2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)):
        r = overlap_census(d, L)
        r["d"], r["L"] = d, L
        r["censused"] = (d, L) in CENSUS_ARENAS
        rows.append(r)
    excluded = [r for r in rows if not r["meets_r2_criterion"]]
    if MUTANT == "inherited-facts-blind":
        # blind the unit to an inherited fact it reads BY PATH out of the R2
        # terminal receipt: the gate that re-confirms the inheritance must
        # notice
        r2_locality_count = r2_locality_count - 1
    cp = criterion_probe(criterion_text)
    fractions = [{"d": r["d"], "L": r["L"], "drawn": r["drawn_pairs"],
                  "all": r["all_pairs"],
                  "fraction": "%d/%d" % (r["drawn_pairs"], r["all_pairs"]),
                  "meets_r2_criterion": r["meets_r2_criterion"]} for r in rows]
    if MUTANT == "lgate-fraction-drop":
        fractions = fractions[:-1]
    return {"rows": rows, "excluded_arenas": [[r["d"], r["L"]] for r in excluded],
            "excluded_reason": "the overlap graph is COMPLETE, so the "
                               "inherited criterion (SOME component not "
                               "complete) is failed",
            "criterion_probe": cp,
            "overlap_fractions_recomputed_here": fractions,
            "overlap_fractions_required": 6,
            "r2_terminal_locality_count_read_by_path": r2_locality_count,
            "r2_terminal_refusal_count_read_by_path": r2_refusal_count,
            "inherited_facts_note": "locality, the consistent chart-intrinsic "
                                    "dimension and translation covariance ride "
                                    "as INHERITED ANCHORS from the R2 terminal; "
                                    "the ruling's own sentences are bound by "
                                    "verbatim-text anchors (T-R2-*), never "
                                    "re-derived here",
            "anchor_rows_consumed": [t[0] for t in TEXT_ANCHOR_ROWS]}


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
            if MUTANT == "cache-wrong-value" and x == rec.S[0]:
                fresh = [[t + 1 for t in row] for row in fresh] \
                    if isinstance(fresh, list) else fresh
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
    S["metric_match_cells"] = len([r for r in cen if r["metric_match"]])
    S["defecting_cells"] = len([r for r in cen if not r["metric_match"]])
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
        [c for c in coe if c["coefficient"]["class"] == CLASS_MRSV])
    S["not_extractable_cells"] = len(
        [c for c in coe if c["coefficient"]["class"] == CLASS_NX])
    # THE BASIS-CLOSURE CENSUS -- "closes" now means ONE thing: the commutator
    # lies in the DECLARED GENERATOR BASIS.  The form it closes with is the
    # second, independent question, and the pin's RIGID branch is one of its
    # answers.
    S["basis_closing_cells"] = len([r for r in cen if r["basis_closes"]])
    S["basis_non_closing_cells"] = len([r for r in cen
                                        if not r["basis_closes"]])
    S["rigid_cells"] = len([r for r in cen if r["rigid"]])
    cf = {}
    for r in cen:
        cf[r["closure_form"]] = cf.get(r["closure_form"], 0) + 1
    S["closure_forms"] = dict(sorted(cf.items()))
    # the positive control's own row
    pc = [c for c in coe if c["rule"] == "A-insert"]
    S["positive_control_cells"] = len(pc)
    S["positive_control_metric_reading"] = len(
        [c for c in pc if c["coefficient"]["metric_reading"]])
    S["positive_control_site_varying"] = len(
        [c for c in pc if c["coefficient"]["class"] == CLASS_MRSV])
    S["positive_control_metric_match"] = len(
        [r for r in cen if r["rule"] == "A-insert" and r["metric_match"]])
    S["positive_control_census_cells"] = len(
        [r for r in cen if r["rule"] == "A-insert"])
    # inhomogeneous records: the only place a structure FUNCTION shows
    inh = [c for c in coe if not c["homogeneous"]]
    S["inhomogeneous_cells"] = len(inh)
    S["inhomogeneous_site_varying_metric"] = len(
        [c for c in inh if c["coefficient"]["class"] == CLASS_MRSV])
    # THE RULE SCOPE of the positive finding: exactly which declared rules
    # realise a site-varying metric coefficient at all.
    S["site_varying_metric_rules"] = sorted(set(
        c["rule"] for c in coe if c["coefficient"]["class"] == CLASS_MRSV))
    S["site_varying_metric_records"] = sorted(set(
        c["record"] for c in coe if c["coefficient"]["class"] == CLASS_MRSV))
    # the bracket tallies
    tal = {}
    for r in dh:
        for k, v in r["tally"].items():
            tal[(r["realisation"], k)] = tal.get((r["realisation"], k), 0) + v
    S["dh_tally"] = dict(sorted(("%s/%s" % k, v) for k, v in tal.items()))
    S["dh_brackets"] = sum(r["brackets"] for r in dh)
    S["dh_in_constraint"] = sum(v for k, v in tal.items()
                                if k[1] == "IN-CONSTRAINT")
    S["dh_brackets_by_dimension"] = dict(
        ("d%d" % dd_, sum(r["brackets"] for r in dh if r["d"] == dd_))
        for dd_ in sorted(set(r["d"] for r in dh)))
    S["dd_closing"] = sum(r["closing"] for r in dd)
    S["dd_total"] = sum(r["total"] for r in dd)
    # {D,D}: the INFORMATIVE count -- brackets of two DISTINCT NONZERO
    # generators.  The rest pair a generator with itself or with zero.
    S["dd_informative"] = sum(r["informative"] for r in dd)
    # the convention sweep, at its OWN denominator: the number of distinct
    # front-sector probes evaluated.  The record x rule multiplicity is
    # reported beside it and never folded in.
    cv = {}
    mult = 0
    for c in res["conventions"]:
        k = (c["order"], c["difference"])
        a, b = cv.get(k, (0, 0))
        cv[k] = (a + c["front_matches"], b + c["front_probes"])
        mult += c["brackets_derived_by_multiplication"]
    S["convention_sweep"] = dict(sorted(
        ("%s/%s" % k, [v[0], v[1]]) for k, v in cv.items()))
    S["convention_front_probes"] = sum(v[1] for v in cv.values()) // len(cv)
    S["convention_derived_by_multiplication"] = mult // len(cv)
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
    S["defect_rows"] = len(dfr)
    # the DEGENERATE probes -- the boundary test's own death certificate,
    # measured rather than typed
    dg = res["degenerate"]
    S["degenerate_rows"] = len(dg)
    S["degenerate_zero_rows"] = len([r for r in dg if r["declared_degenerate"]])
    S["degenerate_zero_probes"] = sum(r["probes"] for r in dg
                                      if r["declared_degenerate"])
    S["degenerate_zero_vanishing"] = sum(r["vanishing_probes"] for r in dg
                                         if r["declared_degenerate"])
    S["degenerate_zero_lattice_sum_zero"] = sum(
        r["lattice_sum_zero"] for r in dg if r["declared_degenerate"])
    S["constant_profile_probes"] = sum(r["probes"] for r in dg
                                       if not r["declared_degenerate"])
    S["constant_profile_vanishing"] = sum(
        r["vanishing_probes"] for r in dg if not r["declared_degenerate"])
    # the OTHER bracket order
    orr = res["orders"]
    S["order_probes"] = dict(sorted(
        (o["order"], [sum(r["nonzero"] for r in orr if r["order"] == o["order"]),
                      sum(r["probes"] for r in orr if r["order"] == o["order"])])
        for o in orr))
    # HYPOTHESIS (S)
    sp = res["spanning"]
    S["spanning_sites"] = sum(r["sites"] for r in sp)
    S["spanning_sites_at_full_rank"] = sum(r["sites_at_full_rank"] for r in sp)
    S["spanning_rows"] = len(sp)
    S["spanning_record_independent"] = len([r for r in sp
                                            if r["record_independent"]])
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
                "metric_match": len([r for r in sub if r["metric_match"]]),
                "defecting": len([r for r in sub if not r["metric_match"]]),
                "max_residual": max([Fr(r["max_abs"]) for r in sub],
                                    default=Fr(0)).__str__(),
                "metric_reading": len([c for c in sc_c
                                       if c["coefficient"]["metric_reading"]]),
                "site_varying_metric": len(
                    [c for c in sc_c if c["coefficient"]["class"]
                     == CLASS_MRSV]),
                "not_extractable": len([c for c in sc_c
                                        if c["coefficient"]["class"]
                                        == CLASS_NX]),
                "basis_closing": len([r for r in sub if r["basis_closes"]]),
                "rigid": len([r for r in sub if r["rigid"]])})
    if MUTANT == "lsweep-drop":
        traj = traj[:-1]
    if MUTANT == "lsweep-instability":
        traj[1] = dict(traj[1])
        traj[1]["metric_match"] = traj[1]["metric_match"] + 1
    S["trajectory"] = traj
    key = [(t["d"], t["cells"], t["metric_match"], t["metric_reading"],
            t["site_varying_metric"], t["not_extractable"],
            t["basis_closing"], t["rigid"]) for t in traj]
    S["structure_constant_along_L"] = (len(set(key))
                                       == len(set(t[0] for t in key)))
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
                if a and b and (a[0]["metric_match"] != b[0]["metric_match"]
                                or a[0]["max_abs"] != b[0]["max_abs"]):
                    moved.append([d, L, rule, nm, a[0]["max_abs"],
                                  b[0]["max_abs"]])
    S["lapse_coordinate_moves"] = moved
    S["lapse_comparisons"] = len(set(
        (r["d"], r["L"], r["rule"], r["record"]) for r in cen))
    S["lapse_moves_upward"] = len([m for m in moved
                                   if Fr(m[5]) > Fr(m[4])])
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

    # ---- THE REALISATION CENSUS -------------------------------------------
    rz = res["realisation"]
    rr = rz["rows"]
    S["realisation_count"] = len(set(tuple(r["realisation"]) for r in rr))
    S["realisation_classifications"] = sum(r["classifications"] for r in rr)
    S["realisation_in_constraint"] = sum(
        r["tally"].get("IN-CONSTRAINT", 0) for r in rr)
    agg = {}
    for r in rr:
        key = "%s(%d,%d,%d)" % ((realisation_name(tuple(r["realisation"])),)
                                + tuple(r["realisation"]))
        for k, v in r["tally"].items():
            agg.setdefault(key, {})
            agg[key][k] = agg[key].get(k, 0) + v
    S["realisation_tallies"] = dict(
        (k, dict(sorted(v.items()))) for k, v in sorted(agg.items()))
    absorbing = sorted(set(tuple(r["realisation"]) for r in rr
                           if "IN-EXTENDED" in r["tally"]))
    S["absorbing_realisations"] = [list(a) for a in absorbing]
    S["realisation_outside_on_the_homogeneous_sector"] = sum(
        r["homogeneous_tally"].get("OUTSIDE", 0) for r in rr
        if tuple(r["realisation"]) in absorbing)
    S["realisation_homogeneous_classifications"] = sum(
        sum(r["homogeneous_tally"].values()) for r in rr
        if tuple(r["realisation"]) in absorbing)
    resist = sorted(set(c for r in rr if tuple(r["realisation"]) in absorbing
                        for c in r["resisting_cells"]))
    S["curvature_supported_residue_cells"] = resist
    S["curvature_supported_residue_count"] = len(resist)
    # is the resisting set EXACTLY the inhomogeneous-record cells?
    inhom_names = sorted(set(c["record"] for c in coe if not c["homogeneous"]))
    S["residue_is_exactly_the_inhomogeneous_records"] = all(
        c.split("|")[1] in inhom_names for c in resist) and len(resist) > 0
    S["realisation_b_is_inert"] = (
        len(set(tuple(sorted(r["tally"].items())) for r in rr
                if (r["realisation"][0], r["realisation"][2]) == (1, 1)
                and r["d"] == rr[0]["d"] and r["L"] == rr[0]["L"])) == 1)

    # ---- THE COVARIANCE THEOREM -------------------------------------------
    cvz = res["covariance"]
    S["covariance_cells"] = cvz["cells"]
    S["covariance_d_full"] = cvz["d_full_covariant"]
    S["covariance_d_tot"] = cvz["d_tot_covariant"]

    # ---- THE STRUCTURE PROBES ---------------------------------------------
    st = res["structure"]
    S["central_extension_cells"] = sum(r["cells"]
                                       for r in st["central_extension"])
    S["central_extension_holds"] = sum(r["cocycle_identity_holds"]
                                       for r in st["central_extension"])
    S["commutator_pairs"] = sum(r["pairs"] for r in st["config_independence"])
    S["commutator_configuration_independent"] = sum(
        r["configuration_independent"] for r in st["config_independence"])
    S["distinct_rules"] = dict(
        ("d%d" % r["d"], {"declared": r["declared_rules"],
                          "distinct_in_the_HH_weight":
                              len(r["distinct_in_the_HH_weight"]),
                          "distinct_in_the_register_drag":
                              len(r["distinct_in_the_register_drag"])})
        for r in st["duplicates"])
    dup = []
    for r in st["duplicates"]:
        for grp in r["distinct_in_the_HH_weight"]:
            if len(grp) > 1:
                dup.append(["HH", r["d"], grp])
        for grp in r["distinct_in_the_register_drag"]:
            if len(grp) > 1:
                dup.append(["REGISTER", r["d"], grp])
    S["duplicate_rule_groups"] = sorted(
        [list(t) for t in set(tuple([a, b, tuple(c)]) for a, b, c in dup)],
        key=str)
    S["nonconstant_probes"] = sum(r["probes"] for r in st["nonconstant"])
    S["nonconstant_outside"] = sum(r["tally"].get("OUTSIDE", 0)
                                   for r in st["nonconstant"])
    S["nonconstant_fields_bijective"] = len(
        [r for r in st["nonconstant"]
         if r["site_map_is_a_bijection"] and r["negative_inverts_it"]
         and not r["field_is_constant"]])
    return S


# ----------------------------------------------------------------------------
# 12.  THE VERDICT -- derived inside a gate, every segment computed
# ----------------------------------------------------------------------------

SEGMENT_ORDER = ("ARENA", "L-GATE", "RECOVERY", "SPANNING", "HH-BRACKET",
                 "COEFFICIENT", "HH-CLOSURE", "HH-RESIDUAL", "DH-BRACKET",
                 "REALISATION-CENSUS", "COVARIANCE", "DEFECT", "CONVENTION",
                 "DD-BRACKET", "CORRESPONDENCE", "LAPSE", "REALISATION",
                 "LSWEEP", "CONTROLS", "SCOPE")

HEAD_CLOSES = "R3-DEFORMATION-CLOSES"
HEAD_DEFECT = "R3-DEFORMATION-DEFECT-AT"

SIGNATURE_KEY = {
    "ARENA": "arena_signature", "L-GATE": "lgate_signature",
    "RECOVERY": "recovery_signature", "SPANNING": "spanning_signature",
    "HH-BRACKET": "hh_signature", "COEFFICIENT": "coeff_signature",
    "HH-CLOSURE": "hhclosure_signature", "HH-RESIDUAL": "hhres_signature",
    "DH-BRACKET": "dh_signature",
    "REALISATION-CENSUS": "realisation_census_signature",
    "COVARIANCE": "covariance_signature", "DEFECT": "defect_signature",
    "CONVENTION": "convention_signature", "DD-BRACKET": "dd_signature",
    "CORRESPONDENCE": "correspondence_signature", "LAPSE": "lapse_signature",
    "REALISATION": "realisation_signature", "LSWEEP": "lsweep_signature",
    "CONTROLS": "controls_signature", "SCOPE": "scope_signature",
}


def verdict_head(S):
    """THE HEAD, DERIVED.  Three first-class outcomes, all reachable:
      CLOSES   -- every declared bracket lands in the declared generator
                  basis; the closure FORM is then named by the HH-CLOSURE
                  segment (GR's bracket form / RIGID / other),
      DEFECT-AT -- some bracket does not, with the failing sector named."""
    dh_ok = (S["dh_in_constraint"] == S["dh_brackets"] and S["dh_brackets"] > 0)
    hh_ok = (S["basis_closing_cells"] == S["census_cells"]
             and S["census_cells"] > 0)
    dd_ok = (S["dd_closing"] == S["dd_total"] and S["dd_total"] > 0)
    failing = []
    if not hh_ok:
        failing.append("NORMAL-NORMAL")
    if not dh_ok:
        failing.append("NORMAL-TANGENTIAL-REGISTER-SECTOR")
    if not dd_ok:
        failing.append("TANGENTIAL-TANGENTIAL")
    return (HEAD_CLOSES if not failing else HEAD_DEFECT), failing


def closure_form_of(S):
    """The census's own closure form, named from the measured counts."""
    forms = S["closure_forms"]
    live = sorted(k for k in forms if forms[k] > 0
                  and k != "NOT-IN-THE-DECLARED-BASIS")
    if len(live) == 1:
        return live[0]
    if S["rigid_cells"] == S["basis_closing_cells"] \
            and S["basis_closing_cells"] > 0:
        return "RIGID-CONSTANT-NON-METRIC"
    return "MIXED(" + "+".join(live) + ")"


def build_verdict(payload, swap_pairing=False):
    """Assemble the verdict from the measured payload."""
    S = payload["summary"]
    head, failing = verdict_head(S)
    segs = [(nm, "%s=%s" % (nm, payload[SIGNATURE_KEY[nm]]))
            for nm in SEGMENT_ORDER]
    if swap_pairing and len(segs) >= 6:
        a, b = segs[4], segs[5]
        segs[4] = (a[0], a[1].split("=")[0] + "=" + b[1].split("=", 1)[1])
        segs[5] = (b[0], b[1].split("=")[0] + "=" + a[1].split("=", 1)[1])
    ix = dict((nm, i) for i, nm in enumerate(SEGMENT_ORDER))
    if MUTANT == "verdict-typed-segment":
        segs[ix["DH-BRACKET"]] = (
            "DH-BRACKET", "DH-BRACKET=IN-CONSTRAINT-AT-ALL-BRACKETS;"
                          "NORMAL-TANGENTIAL-RELATION-REPRODUCED")
    if MUTANT == "verdict-append-text":
        k = ix["COEFFICIENT"]
        segs[k] = ("COEFFICIENT",
                   segs[k][1] + "-AND-DERIVED-FROM-THE-SUBSTRATE")
    if MUTANT == "verdict-typed-coefficient":
        segs[ix["COEFFICIENT"]] = (
            "COEFFICIENT", "COEFFICIENT=METRIC-READING-SITE-VARYING-AT-"
                           "EVERY-CELL")
    if MUTANT == "verdict-fully-typed":
        segs = [(nm, "%s=TYPED" % nm) for nm in SEGMENT_ORDER]
        head = HEAD_CLOSES
    if MUTANT == "verdict-inert-segment":
        segs[ix["DEFECT"]] = ("DEFECT", "DEFECT=NONE")
    if MUTANT == "verdict-typed-covariance":
        segs[ix["COVARIANCE"]] = ("COVARIANCE",
                                  "COVARIANCE=THE-RECORD-TRANSPORTS")
    if MUTANT == "verdict-typed-correspondence":
        segs[ix["CORRESPONDENCE"]] = ("CORRESPONDENCE",
                                      "CORRESPONDENCE=HDA-REPRODUCED")
    if MUTANT == "head-constant":
        head = HEAD_CLOSES
    if MUTANT == "verdict-segment-drop":
        segs = segs[:-1]
    full = head + "<" + "|".join(s[1] for s in segs) + ">"
    return head, segs, full


def rigid_probe():
    """THE RIGID BRANCH'S REACHABILITY, DEMONSTRATED.  A synthetic payload in
    which every bracket lands in the declared basis and every closing cell
    carries a CONSTANT NON-METRIC coefficient is fed to the very function that
    builds the delivered verdict; the head it returns and the closure form it
    names are read back.  If the machinery could not return the RIGID outcome,
    this probe would say so."""
    syn = {"census_cells": 10, "basis_closing_cells": 10, "rigid_cells": 10,
           "closure_forms": {"RIGID-CONSTANT-NON-METRIC": 10},
           "dh_in_constraint": 4, "dh_brackets": 4,
           "dd_closing": 2, "dd_total": 2}
    if MUTANT == "rigid-branch-unreachable":
        syn["closure_forms"] = {"METRIC-READING-CONSTANT": 10}
        syn["rigid_cells"] = 0
    head, failing = verdict_head(syn)
    return head, closure_form_of(syn), failing


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
    """THE INDEPENDENT COMPARATOR.  Every segment is rebuilt from the
    receipt's RAW MEASURED ROWS -- never from `summary`, never from the same
    object the builder read (RUNBOOK section 14 addendum, v13 #219: a gate
    clause that compares an object against a copy of itself routed through the
    component under test verifies nothing).  The receipt's sub-objects are
    DEEP-COPIED before this runs, so object identity cannot be mistaken for
    agreement.  Any typed, appended, swapped, dropped or post-gate-corrupted
    value disagrees here."""
    cen = R["census_rows"]
    coe = R["coefficient_rows"]
    dhr = R["dh_bracket_rows"]
    ddr = R["dd_bracket_rows"]
    cnv = R["convention_sweep"]
    dfr = R["defect_rows"]
    dgr = R["degenerate_rows"]
    orr = R["order_rows"]
    spn = R["spanning_rows"]
    rzr = R["realisation_rows"]
    cvr = R["covariance_rows"]
    stx = R["structure_rows"]
    ncr = stx["nonconstant"]
    rec = R["recovery"]
    lg = R["l_gate"]
    ctl = R["controls"]
    arena = R["arena_declaration"]
    arenas = sorted(set((r["d"], r["L"]) for r in cen))
    out = []

    dh_tot = sum(r["brackets"] for r in dhr)
    dh_in = sum(r["tally"].get("IN-CONSTRAINT", 0) for r in dhr)
    basis_ok = len(cen) > 0 and all(r["basis_closes"] for r in cen)
    dd_tot = sum(r["total"] for r in ddr)
    dd_ok = dd_tot > 0 and sum(r["closing"] for r in ddr) == dd_tot
    dh_ok = dh_tot > 0 and dh_in == dh_tot
    fail = []
    if not basis_ok:
        fail.append("NORMAL-NORMAL")
    if not dh_ok:
        fail.append("NORMAL-TANGENTIAL-REGISTER-SECTOR")
    if not dd_ok:
        fail.append("TANGENTIAL-TANGENTIAL")
    head = HEAD_CLOSES if not fail else HEAD_DEFECT

    recset = sorted(set(r["record"] for r in cen))
    ruleset = sorted(set(r["rule"] for r in cen))
    out.append("ARENA=SITES=%s;LINKS=%s;RECORDS=%d;RULES=%d;LAPSE-SCOPES=%s;"
               "WEIGHT=%d"
               % (",".join("d%dL%d:%d" % (d, L, L ** d) for d, L in arenas),
                  ",".join("d%d:%d" % (d, d + d * (d - 1) // 2)
                           for d in sorted(set(a[0] for a in arenas))),
                  len(recset), len(ruleset),
                  ",".join(sorted(set(r["scope"] for r in cen))),
                  arena["density_weight"]))
    exc = sorted(tuple(a) for a in lg["excluded_arenas"])
    out.append("L-GATE=MIN-L=%d;EXCLUDED=%s;REASON=OVERLAP-GRAPH-COMPLETE-AT-"
               "%s;CRITERION-READ-BY-PATH-FROM-THE-R2-TERMINAL-RECEIPT;"
               "CRITERION-IMPLEMENTATION-CONTROLLED=%s;"
               "FRACTIONS-RECOMPUTED-HERE=%d"
               % (min(a[1] for a in arenas),
                  ",".join("d%dL%d" % (d, L) for d, L in exc),
                  ",".join("%d-OF-%d" % (r["drawn_pairs"], r["all_pairs"])
                           for r in lg["rows"]
                           if (r["d"], r["L"]) in [tuple(e) for e in exc]),
                  str(lg["criterion_probe"]
                      ["positive_control_path_graph_has_locality"] is True
                      and lg["criterion_probe"]
                      ["negative_control_complete_graph_has_locality"]
                      is False).upper(),
                  len(lg["overlap_fractions_recomputed_here"])))
    out.append("RECOVERY=CLOSURE-%d-OF-%d;SECTOR-%d-OF-%d;RANK;READOUT-DET-%s;"
               "GENERAL-D;COUNT-LATTICE;DIAGONAL-SECTOR-%d-RECORDS-CLOSE-AT-"
               "THE-LINK-LOCAL-RULE"
               % (len([k for k in rec["closure_rows"]
                       if k in rec["pinned_closure_keys"]])
                  - len(rec["closure_mismatches"]),
                  len([k for k in rec["closure_rows"]
                       if k in rec["pinned_closure_keys"]]),
                  len(rec["pinned_sector_keys"]) - len(rec["sector_mismatches"]),
                  len(rec["pinned_sector_keys"]),
                  rec["readout"]["determinant"],
                  len([nm for nm in rec["diagonal_sector"]
                       if rec["closure_rows"]["A-axis|%s" % nm]
                       ["metric_match"]])))
    out.append("SPANNING=MEASURED;OMEGA-SPANS-THE-FULL-LINK-SPACE-AT-%d-OF-%d-"
               "SITES;ROWS=%d;RECORD-INDEPENDENT-AT-%d-OF-%d;"
               "THE-ONE-LOAD-BEARING-MEASUREMENT-OF-THE-HH-HALF"
               % (sum(r["sites_at_full_rank"] for r in spn),
                  sum(r["sites"] for r in spn), len(spn),
                  len([r for r in spn if r["record_independent"]]), len(spn)))
    ce_cells = sum(r["cells"] for r in stx["central_extension"])
    ce_ok = sum(r["cocycle_identity_holds"] for r in stx["central_extension"])
    ci_p = sum(r["pairs"] for r in stx["config_independence"])
    ci_ok = sum(r["configuration_independent"]
                for r in stx["config_independence"])
    out.append("HH-BRACKET=LANDS-IN-THE-TANGENTIAL-FAMILY-AT-%d-OF-%d-CELLS"
               "(FORCED:w-LINEAR-IN-THE-FRONT);NORMAL-CHANNEL-EMPTY(FORCED);"
               "STRUCTURE-THEOREM-rho=(W-B).Omega-VERIFIED-AT-%d-OF-%d-CELLS"
               "(FORCED);CENTRAL-EXTENSION-H[N]H[M]=T_w[N,M].H[N+M]-AT-%d-OF-"
               "%d;COMMUTATOR-CONFIGURATION-INDEPENDENT-AT-%d-OF-%d"
               % (len(cen), len(cen), R["two_route"]["class_prediction_cells"],
                  len(cen), ce_ok, ce_cells, ci_ok, ci_p))
    cls = {}
    for c in coe:
        k = c["coefficient"]["class"]
        cls[k] = cls.get(k, 0) + 1
    pcc = [c for c in coe if c["rule"] == "A-insert"]
    inh = [c for c in coe if not c["homogeneous"]]
    svr = sorted(set(c["rule"] for c in coe
                     if c["coefficient"]["class"] == CLASS_MRSV))
    out.append("COEFFICIENT=EXTRACTED-FROM-THE-COMMUTATORS(UNIQUE-BY-(S));"
               "CLASSES=%s(FORCED:class=f(W,B));POSITIVE-CONTROL-METRIC-"
               "READING-AT-%d-OF-%d(FORCED-VALUE-AND-FORCED-CLASS);"
               "SITE-VARYING-METRIC-ON-THE-INHOMOGENEOUS-RECORDS-AT-%d-OF-%d-"
               "CELLS-AT-RULES=%s"
               % (";".join("%s:%d" % (k, cls[k]) for k in sorted(cls)),
                  len([c for c in pcc if c["coefficient"]["metric_reading"]]),
                  len(pcc),
                  len([c for c in inh if c["coefficient"]["class"]
                       == CLASS_MRSV]), len(inh), ",".join(svr)))
    forms = {}
    for r in cen:
        forms[r["closure_form"]] = forms.get(r["closure_form"], 0) + 1
    out.append("HH-CLOSURE=AGAINST-THE-DECLARED-GENERATOR-BASIS;IN-THE-BASIS-"
               "AT-%d-OF-%d-CELLS;FORMS=%s;RIGID-CONSTANT-NON-METRIC-REACHED-"
               "AT-%d-CELLS;METRIC-MATCH-AT-%d-OF-%d;SYNTHETIC-RIGID-HEAD=%s"
               % (len([r for r in cen if r["basis_closes"]]), len(cen),
                  ";".join("%s:%d" % (k, forms[k]) for k in sorted(forms)),
                  len([r for r in cen if r["rigid"]]),
                  len([r for r in cen if r["metric_match"]]), len(cen),
                  R["rigid_branch_probe"]["closure_form"]))
    bad = [r for r in cen if not r["metric_match"]]
    badrules = sorted(set(r["rule"] for r in bad))
    nxr = sorted(set(c["rule"] for c in coe
                     if c["coefficient"]["class"] == CLASS_NX))
    out.append("HH-RESIDUAL=NONZERO-AT-%d-OF-%d-CELLS;RULES=%s;"
               "NOT-IN-THE-BASIS-AT-%d-CELLS(RULES-WITH-A-DIAGONAL-LINK-"
               "COLUMN=%s;%d-OF-%d-ARCHITECTURE-B-CELLS,FORCED);MAX=%s"
               % (len(bad), len(cen),
                  ",".join(badrules) if badrules else "NONE",
                  len([c for c in coe
                       if c["coefficient"]["class"] == CLASS_NX]),
                  ",".join(nxr),
                  len([c for c in coe
                       if c["coefficient"]["class"] == CLASS_NX]),
                  len([c for c in coe if arch_of(c["rule"]) == "B"]),
                  max([Fr(r["max_abs"]) for r in cen],
                      default=Fr(0)).__str__()))
    tal = {}
    for r in dhr:
        for k, v in r["tally"].items():
            tal[(r["realisation"], k)] = tal.get((r["realisation"], k), 0) + v
    out.append("DH-BRACKET=%s(D-REG-IDENTITY-FORCED);THE-RELATION-REQUIRES-"
               "H[L_v-N];IN-CONSTRAINT-AT-%d-OF-%d"
               % (";".join("%s:%s" % (k[0] + "/" + k[1], tal[k])
                           for k in sorted(tal)), dh_in, dh_tot))
    rz_class = sum(r["classifications"] for r in rzr)
    rz_in = sum(r["tally"].get("IN-CONSTRAINT", 0) for r in rzr)
    absorbing = sorted(set(tuple(r["realisation"]) for r in rzr
                           if "IN-EXTENDED" in r["tally"]))
    hom_out = sum(r["homogeneous_tally"].get("OUTSIDE", 0) for r in rzr
                  if tuple(r["realisation"]) in absorbing)
    hom_tot = sum(sum(r["homogeneous_tally"].values()) for r in rzr
                  if tuple(r["realisation"]) in absorbing)
    resist = sorted(set(c for r in rzr if tuple(r["realisation"]) in absorbing
                        for c in r["resisting_cells"]))
    inhom = sorted(set(c["record"] for c in coe if not c["homogeneous"]))
    b_inert = (len(set(tuple(sorted(r["tally"].items())) for r in rzr
                       if (r["realisation"][0], r["realisation"][2]) == (1, 1)
                       and r["d"] == rzr[0]["d"] and r["L"] == rzr[0]["L"]))
               == 1)
    out.append("REALISATION-CENSUS=ALL-%d-(a,b,c)-REALISATIONS-BUILT-FROM-THE-"
               "TWO-DECLARED-ATOMS;CLASSIFICATIONS=%d;IN-CONSTRAINT-AT-%d-OF-"
               "%d(ABSOLUTE);ABSORBING-REALISATIONS=%d;OUTSIDE-ON-THE-"
               "HOMOGENEOUS-SECTOR-AT-%d-OF-%d;CURVATURE-SUPPORTED-RESIDUE="
               "%d-CELLS;RESIDUE-IS-EXACTLY-THE-INHOMOGENEOUS-RECORDS=%s;"
               "REGISTER-SHIFT-INERT=%s"
               % (len(set(tuple(r["realisation"]) for r in rzr)), rz_class,
                  rz_in, rz_class, len(absorbing), hom_out, hom_tot,
                  len(resist),
                  str(len(resist) > 0
                      and all(c.split("|")[1] in inhom
                              for c in resist)).upper(),
                  str(b_inert).upper()))
    cv_cells = sum(r["cells"] for r in cvr)
    cv_full = sum(r["d_full_covariant"] for r in cvr)
    cv_tot = sum(r["d_tot_covariant"] for r in cvr)
    out.append("COVARIANCE=THEOREM=D_full[v].H_g[N].D_full[v]^-1=H_{S_v-g}"
               "[S_v-N];HOLDS-AT-%d-OF-%d-CELLS;FAILS-AT-D-TOT-AT-%d-OF-%d;"
               "SURVIVING-OBSTRUCTION=THE-RECORD-DOES-NOT-TRANSPORT;"
               "THE-ARENA-CARRIES-A-FIXED-BACKGROUND"
               % (cv_full, cv_cells, cv_cells - cv_tot, cv_cells))
    dp = sum(r["probes"] for r in dfr)
    dv = sum(r["vanishing_probes"] for r in dfr)
    dl = sum(r["lattice_sum_zero"] for r in dfr)
    dhom = sum(r["vanishing_probes"] for r in dfr if r["homogeneous"])
    dhomp = sum(r["probes"] for r in dfr if r["homogeneous"])
    dz = [r for r in dgr if r["declared_degenerate"]]
    dc = [r for r in dgr if not r["declared_degenerate"]]
    other = [r for r in orr if r["order"] == BRACKET_ORDERS[1]]
    out.append("DEFECT=REGISTER-SECTOR-OF-THE-NORMAL-TANGENTIAL-BRACKET-AT-"
               "D-TOT;CLOSED-FORM=w[N,(S_-v-1)(n-N)]-w[S_vN-N,n];NONZERO-AT-"
               "%d-OF-%d-PROBES;CONFIGURATION-DEPENDENT;LATTICE-SUM-NONZERO-"
               "AT-%d-OF-%d;VANISHES-ON-THE-HOMOGENEOUS-SECTOR-AT-%d-OF-%d;"
               "DEGENERATE-PROBE-BUILT-AND-MEASURED=%d-OF-%d-VANISH;"
               "CONSTANT-PROFILE-VANISHES-AT-%d-OF-%d;"
               "OTHER-BRACKET-ORDER-NONZERO-AT-%d-OF-%d;"
               "NON-CONSTANT-TANGENTIAL-FIELDS-OUTSIDE-AT-%d-OF-%d;"
               "L-AND-D-INDEPENDENT-AT-%d-ARENAS"
               % (dp - dv, dp, dp - dl, dp, dhom, dhomp,
                  sum(r["vanishing_probes"] for r in dz),
                  sum(r["probes"] for r in dz),
                  sum(r["vanishing_probes"] for r in dc),
                  sum(r["probes"] for r in dc),
                  sum(r["nonzero"] for r in other),
                  sum(r["probes"] for r in other),
                  sum(r["tally"].get("OUTSIDE", 0) for r in ncr),
                  sum(r["probes"] for r in ncr),
                  len(arenas)))
    cv = {}
    mult = 0
    for c in cnv:
        k = (c["order"], c["difference"])
        a, b = cv.get(k, (0, 0))
        cv[k] = (a + c["front_matches"], b + c["front_probes"])
        mult += c["record_rule_multiplicity"] * c["front_probes"]
    full = sorted(k for k in cv if cv[k][0] == cv[k][1] and cv[k][1] > 0)
    probes = sum(v[1] for v in cv.values()) // len(cv)
    out.append("CONVENTION=FRONT-SECTOR-REPRODUCES-L_v-N-AT-%s;"
               "MATCHING-CONVENTIONS=%d-OF-%d;%s;DENOMINATOR=DISTINCT-FRONT-"
               "PROBES-%d(RECORD-AND-RULE-INDEPENDENCE-MEASURED;x%d-"
               "MULTIPLICITY-DISCLOSED-NOT-FOLDED-IN)"
               % (",".join("%s/%s" % k for k in full) if full
                  else "NO-CONVENTION", len(full), len(cv),
                  ";".join("%s/%s:%d-OF-%d" % (k[0], k[1], cv[k][0], cv[k][1])
                           for k in sorted(cv)),
                  probes, (mult // len(cv)) // max(1, probes)))
    out.append("DD-BRACKET=LATTICE-TRANSLATIONS-CLOSE-AT-%d-OF-%d-AT-BOTH-"
               "REALISATIONS(FORCED:[v,w]=0-AT-CONSTANT-FIELDS;POSITIVE-"
               "CONTROL,MUTANT-FLIPS-IT);INFORMATIVE-BRACKETS(TWO-DISTINCT-"
               "NONZERO-GENERATORS)=%d-OF-%d;NONABELIAN-CORE-UNTESTED-BY-"
               "CONSTRUCTION"
               % (sum(r["closing"] for r in ddr), dd_tot,
                  sum(r["informative"] for r in ddr), dd_tot))
    out.append("CORRESPONDENCE=RELATION-I=EXACT-IN-FORM-ANALOGICAL-IN-STATUS"
               "(A-CENTRAL-EXTENSION-WITH-A-BACKGROUND-COEFFICIENT:THE-"
               "COEFFICIENT-DOES-NOT-MOVE-WITH-THE-STATE-AT-%d-OF-%d-PAIRS);"
               "RELATION-II=PARTIAL(FRONT-EXACT-AT-1-OF-4-CONVENTIONS-AND-AT-"
               "CONSTANT-v;REGISTER-DEFECTIVE-AT-D-TOT,ABSORBED-AT-D-FULL-ON-"
               "THE-HOMOGENEOUS-SECTOR,ABSENT-AT-D-REG);RELATION-III="
               "CONTENTLESS-ABELIAN([v,w]=0-AT-ALL-%d-BRACKETS);"
               "THE-POSITIVE-CLAIM=FIXED-BACKGROUND-COVARIANCE-WITH-GR-"
               "BRACKET-FORM;THE-UNQUALIFIED-NAME-HDA-IS-NOT-USED"
               % (ci_ok, ci_p, dd_tot))
    moved = []
    for (d, L) in arenas:
        for rule in sorted(set(r["rule"] for r in cen)):
            for nm in sorted(set(r["record"] for r in cen
                                 if r["d"] == d and r["L"] == L)):
                aa = [r for r in cen if r["d"] == d and r["L"] == L
                      and r["rule"] == rule and r["record"] == nm
                      and r["scope"] == "BASE"]
                bb = [r for r in cen if r["d"] == d and r["L"] == L
                      and r["rule"] == rule and r["record"] == nm
                      and r["scope"] == "TRANSLATES"]
                if aa and bb and (aa[0]["metric_match"] != bb[0]["metric_match"]
                                  or aa[0]["max_abs"] != bb[0]["max_abs"]):
                    moved.append((aa[0]["max_abs"], bb[0]["max_abs"]))
    ncmp = len(set((r["d"], r["L"], r["rule"], r["record"]) for r in cen))
    ca = {}
    for c in coe:
        ca[(c["d"], c["L"], c["scope"], c["rule"], c["record"])] = \
            c["coefficient"]["class"]
    cmv = 0
    for k, v in ca.items():
        k2 = (k[0], k[1], "TRANSLATES" if k[2] == "BASE" else "BASE", k[3],
              k[4])
        if k2 in ca and ca[k2] != v:
            cmv += 1
    out.append("LAPSE=DECLARED-FAMILY-AND-ITS-LATTICE-TRANSLATES;ENLARGEMENT-"
               "PRINTED;RESIDUAL-MAGNITUDE-MOVES-AT-%d-OF-%d-COMPARISONS"
               "(ALL-UPWARD-AT-%d);COEFFICIENT-CLASS-MOVES-AT-%d-CELLS"
               "(FORCED-BY-(S))"
               % (len(moved), ncmp,
                  len([m for m in moved if Fr(m[1]) > Fr(m[0])]), cmv))
    out.append("REALISATION=D-REG:%s;D-TOT:%s"
               % ("+".join(sorted(set(k[1] for k in tal if k[0] == "D-REG"))),
                  "+".join(sorted(set(k[1] for k in tal if k[0] == "D-TOT")))))
    tr = []
    for (d, L) in arenas:
        for sc in sorted(set(r["scope"] for r in cen)):
            sub = [r for r in cen if r["d"] == d and r["L"] == L
                   and r["scope"] == sc]
            sc_c = [c for c in coe if c["d"] == d and c["L"] == L
                    and c["scope"] == sc]
            tr.append((d, L, sc, len(sub),
                       len([r for r in sub if r["basis_closes"]]),
                       len([r for r in sub if r["metric_match"]]),
                       len([c for c in sc_c
                            if c["coefficient"]["metric_reading"]]),
                       len([c for c in sc_c
                            if c["coefficient"]["class"] == CLASS_MRSV]),
                       len([c for c in sc_c
                            if c["coefficient"]["class"] == CLASS_NX]),
                       len([r for r in sub if r["rigid"]]),
                       max([Fr(r["max_abs"]) for r in sub],
                           default=Fr(0)).__str__()))
    key = [t[:1] + t[3:10] for t in tr]
    out.append("LSWEEP=%s;STRUCTURE-CONSTANT-ALONG-L=%s(FORCED:class=f(W,B),"
               "NO-L-IN-IT);MAX-RESIDUAL-MOVES=%s(MEASURED)"
               % (",".join("d%dL%d/%s:%d-in-basis-of-%d"
                           % (t[0], t[1], t[2][0], t[4], t[3]) for t in tr),
                  str(len(set(key)) == len(set(t[0] for t in key))).upper(),
                  ",".join(t[10] for t in tr)))
    pos = ctl["positive"]
    negc = ctl["negative"]
    cov = ctl["covariance"]
    out.append("CONTROLS=CHART-GROUP-CLOSES-AT-%d-OF-%d-ARENAS;TRANSLATION-"
               "EQUIVARIANT-AT-%d-OF-%d(FORCED:MODULAR-ARITHMETIC);SCRAMBLED-"
               "VIOLATES-AT-%d-OF-%d;RESIDUAL-COVARIANT-ON-THE-RECORD-LATTICE-"
               "AT-%d-CELLS(NON-VACUITY:%d-DISTINCT-NONZERO-BASE-CELLS);"
               "SCRAMBLED-BREAKS-AT-%d-CELLS"
               % (len([c for c in ctl["chart_group"] if c["closes"]]),
                  len(ctl["chart_group"]),
                  sum(p["equivariant_cells"] for p in pos),
                  sum(p["total_cells"] for p in pos),
                  sum(n["violating_cells"] for n in negc),
                  sum(n["total_cells"] for n in negc),
                  sum(c["covariant_cells"] for c in cov
                      if c["lattice"] == "RECORD"),
                  sum(c["distinct_nonzero_base_cells"] for c in cov
                      if c["lattice"] == "RECORD"),
                  sum(c["violating_cells"] for c in cov
                      if c["lattice"] == "SCRAMBLED")))
    dups = []
    dstr = {}
    for r in stx["duplicates"]:
        dstr["d%d" % r["d"]] = (r["declared_rules"],
                                len(r["distinct_in_the_HH_weight"]),
                                len(r["distinct_in_the_register_drag"]))
        for grp in r["distinct_in_the_HH_weight"]:
            if len(grp) > 1:
                dups.append(("HH", r["d"], tuple(grp)))
        for grp in r["distinct_in_the_register_drag"]:
            if len(grp) > 1:
                dups.append(("REGISTER", r["d"], tuple(grp)))
    out.append("SCOPE=FINITE-EXTENT-ONLY(NO-CONTINUUM-CLAIM);WEIGHT=%d-ONLY"
               "(w=1-DECLARED-NOT-SWEPT);TANGENTIAL-FIELDS=CONSTANT-IN-THE-"
               "CENSUS(BIJECTION-REQUIREMENT)+%d-DECLARED-NON-CONSTANT-"
               "BIJECTIVE-PROBES;DISTINCT-RULES=%s;DUPLICATE-RULE-GROUPS=%s;"
               "SIGNATURE-NOT-MEASURED;HKT-REPRESENTATION-LEG-NOT-ATTEMPTED"
               % (arena["density_weight"],
                  len([r for r in ncr if r["site_map_is_a_bijection"]
                       and r["negative_inverts_it"]
                       and not r["field_is_constant"]]),
                  ",".join("%s:%d-of-%d-in-HH,%d-of-%d-in-the-register-sector"
                           % (k, dstr[k][1], dstr[k][0], dstr[k][2],
                              dstr[k][0]) for k in sorted(dstr)),
                  "+".join("%s@d%d:%s" % (g[0], g[1], "=".join(g[2]))
                           for g in sorted(set(dups), key=str))))
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
        "SITES=%s;LINKS=%s;RECORDS=%d;RULES=%d;LAPSE-SCOPES=%s;WEIGHT=%d"
        % (",".join("d%dL%d:%d" % (d, L, L ** d) for d, L in arenas),
           ",".join("d%d:%d" % (d, len(link_set(d))) for d in ds),
           nrec, nrul, ",".join(sorted(LAPSE_SCOPES)),
           decl["density_weight"]))
    exc = sorted(tuple(a) for a in lg["excluded_arenas"])
    P["lgate_signature"] = (
        "MIN-L=%d;EXCLUDED=%s;REASON=OVERLAP-GRAPH-COMPLETE-AT-%s;"
        "CRITERION-READ-BY-PATH-FROM-THE-R2-TERMINAL-RECEIPT;"
        "CRITERION-IMPLEMENTATION-CONTROLLED=%s;FRACTIONS-RECOMPUTED-HERE=%d"
        % (CENSUS_L_MIN, ",".join("d%dL%d" % (d, L) for d, L in exc),
           ",".join("%d-OF-%d" % (r["drawn_pairs"], r["all_pairs"])
                    for r in lg["rows"] if (r["d"], r["L"]) in exc),
           str(lg["criterion_probe"]
               ["implementation_agrees_with_the_inherited_criterion"]).upper(),
           len(lg["overlap_fractions_recomputed_here"])))
    P["recovery_signature"] = (
        "CLOSURE-%d-OF-%d;SECTOR-%d-OF-%d;RANK;READOUT-DET-%s;GENERAL-D;"
        "COUNT-LATTICE;DIAGONAL-SECTOR-%d-RECORDS-CLOSE-AT-THE-LINK-LOCAL-RULE"
        % (rec_out["closure_cells_compared"] - len(rec_out["closure_mismatches"]),
           rec_out["closure_cells_compared"],
           rec_out["sector_cells_compared"] - len(rec_out["sector_mismatches"]),
           rec_out["sector_cells_compared"], rec_out["readout"]["determinant"],
           len(rec_out["diagonal_sector_closes_at_the_link_local_rule"])))
    P["spanning_signature"] = (
        "MEASURED;OMEGA-SPANS-THE-FULL-LINK-SPACE-AT-%d-OF-%d-SITES;"
        "ROWS=%d;RECORD-INDEPENDENT-AT-%d-OF-%d;"
        "THE-ONE-LOAD-BEARING-MEASUREMENT-OF-THE-HH-HALF"
        % (S["spanning_sites_at_full_rank"], S["spanning_sites"],
           S["spanning_rows"], S["spanning_record_independent"],
           S["spanning_rows"]))
    P["hh_signature"] = (
        "LANDS-IN-THE-TANGENTIAL-FAMILY-AT-%d-OF-%d-CELLS(FORCED:w-LINEAR-IN-"
        "THE-FRONT);NORMAL-CHANNEL-EMPTY(FORCED);"
        "STRUCTURE-THEOREM-rho=(W-B).Omega-VERIFIED-AT-%d-OF-%d-CELLS(FORCED);"
        "CENTRAL-EXTENSION-H[N]H[M]=T_w[N,M].H[N+M]-AT-%d-OF-%d;"
        "COMMUTATOR-CONFIGURATION-INDEPENDENT-AT-%d-OF-%d"
        % (S["census_cells"], S["census_cells"],
           res["two_route"]["class_prediction_cells"], S["census_cells"],
           S["central_extension_holds"], S["central_extension_cells"],
           S["commutator_configuration_independent"], S["commutator_pairs"]))
    P["coeff_signature"] = (
        "EXTRACTED-FROM-THE-COMMUTATORS(UNIQUE-BY-(S));CLASSES=%s(FORCED:"
        "class=f(W,B));POSITIVE-CONTROL-METRIC-READING-AT-%d-OF-%d(FORCED-"
        "VALUE-AND-FORCED-CLASS);SITE-VARYING-METRIC-ON-THE-INHOMOGENEOUS-"
        "RECORDS-AT-%d-OF-%d-CELLS-AT-RULES=%s"
        % (";".join("%s:%d" % (k, v) for k, v in
                    sorted(S["coefficient_classes"].items())),
           S["positive_control_metric_reading"], S["positive_control_cells"],
           S["inhomogeneous_site_varying_metric"], S["inhomogeneous_cells"],
           ",".join(S["site_varying_metric_rules"])))
    P["hhclosure_signature"] = (
        "AGAINST-THE-DECLARED-GENERATOR-BASIS;IN-THE-BASIS-AT-%d-OF-%d-CELLS;"
        "FORMS=%s;RIGID-CONSTANT-NON-METRIC-REACHED-AT-%d-CELLS;"
        "METRIC-MATCH-AT-%d-OF-%d;SYNTHETIC-RIGID-HEAD=%s"
        % (S["basis_closing_cells"], S["census_cells"],
           ";".join("%s:%d" % (k, v)
                    for k, v in sorted(S["closure_forms"].items())),
           S["rigid_cells"], S["metric_match_cells"], S["census_cells"],
           rigid_probe()[1]))
    badrules = sorted(set(r["rule"] for r in res["census"]
                          if not r["metric_match"]))
    P["hhres_signature"] = (
        "NONZERO-AT-%d-OF-%d-CELLS;RULES=%s;NOT-IN-THE-BASIS-AT-%d-CELLS"
        "(RULES-WITH-A-DIAGONAL-LINK-COLUMN=%s;%d-OF-%d-ARCHITECTURE-B-CELLS,"
        "FORCED);MAX=%s"
        % (S["defecting_cells"], S["census_cells"],
           ",".join(badrules) if badrules else "NONE",
           S["not_extractable_cells"],
           ",".join(S["not_extractable_rules"]),
           S["not_extractable_cells"], S["architecture_B_cells"],
           max([Fr(r["max_abs"]) for r in res["census"]],
               default=Fr(0)).__str__()))
    P["dh_signature"] = (
        "%s(D-REG-IDENTITY-FORCED);THE-RELATION-REQUIRES-H[L_v-N];"
        "IN-CONSTRAINT-AT-%d-OF-%d"
        % (";".join("%s:%s" % (k, v) for k, v in sorted(S["dh_tally"].items())),
           S["dh_in_constraint"], S["dh_brackets"]))
    P["realisation_census_signature"] = (
        "ALL-%d-(a,b,c)-REALISATIONS-BUILT-FROM-THE-TWO-DECLARED-ATOMS;"
        "CLASSIFICATIONS=%d;IN-CONSTRAINT-AT-%d-OF-%d(ABSOLUTE);"
        "ABSORBING-REALISATIONS=%d;OUTSIDE-ON-THE-HOMOGENEOUS-SECTOR-AT-%d-"
        "OF-%d;CURVATURE-SUPPORTED-RESIDUE=%d-CELLS;"
        "RESIDUE-IS-EXACTLY-THE-INHOMOGENEOUS-RECORDS=%s;REGISTER-SHIFT-INERT=%s"
        % (S["realisation_count"], S["realisation_classifications"],
           S["realisation_in_constraint"], S["realisation_classifications"],
           len(S["absorbing_realisations"]),
           S["realisation_outside_on_the_homogeneous_sector"],
           S["realisation_homogeneous_classifications"],
           S["curvature_supported_residue_count"],
           str(S["residue_is_exactly_the_inhomogeneous_records"]).upper(),
           str(S["realisation_b_is_inert"]).upper()))
    P["covariance_signature"] = (
        "THEOREM=D_full[v].H_g[N].D_full[v]^-1=H_{S_v-g}[S_v-N];"
        "HOLDS-AT-%d-OF-%d-CELLS;FAILS-AT-D-TOT-AT-%d-OF-%d;"
        "SURVIVING-OBSTRUCTION=THE-RECORD-DOES-NOT-TRANSPORT;"
        "THE-ARENA-CARRIES-A-FIXED-BACKGROUND"
        % (S["covariance_d_full"], S["covariance_cells"],
           S["covariance_cells"] - S["covariance_d_tot"],
           S["covariance_cells"]))
    P["defect_signature"] = (
        "REGISTER-SECTOR-OF-THE-NORMAL-TANGENTIAL-BRACKET-AT-D-TOT;"
        "CLOSED-FORM=w[N,(S_-v-1)(n-N)]-w[S_vN-N,n];NONZERO-AT-%d-OF-%d-"
        "PROBES;CONFIGURATION-DEPENDENT;LATTICE-SUM-NONZERO-AT-%d-OF-%d;"
        "VANISHES-ON-THE-HOMOGENEOUS-SECTOR-AT-%d-OF-%d;"
        "DEGENERATE-PROBE-BUILT-AND-MEASURED=%d-OF-%d-VANISH;"
        "CONSTANT-PROFILE-VANISHES-AT-%d-OF-%d;"
        "OTHER-BRACKET-ORDER-NONZERO-AT-%d-OF-%d;"
        "NON-CONSTANT-TANGENTIAL-FIELDS-OUTSIDE-AT-%d-OF-%d;"
        "L-AND-D-INDEPENDENT-AT-%d-ARENAS"
        % (S["defect_probes"] - S["defect_vanishing_probes"],
           S["defect_probes"],
           S["defect_probes"] - S["defect_lattice_sum_zero"],
           S["defect_probes"], S["defect_vanishes_on_homogeneous"],
           S["defect_homogeneous_probes"],
           S["degenerate_zero_vanishing"], S["degenerate_zero_probes"],
           S["constant_profile_vanishing"], S["constant_profile_probes"],
           S["order_probes"][BRACKET_ORDERS[1]][0],
           S["order_probes"][BRACKET_ORDERS[1]][1],
           S["nonconstant_outside"], S["nonconstant_probes"],
           len(arenas)))
    cv = S["convention_sweep"]
    full = sorted(k for k in cv if cv[k][0] == cv[k][1] and cv[k][1] > 0)
    P["convention_signature"] = (
        "FRONT-SECTOR-REPRODUCES-L_v-N-AT-%s;MATCHING-CONVENTIONS=%d-OF-%d;%s;"
        "DENOMINATOR=DISTINCT-FRONT-PROBES-%d(RECORD-AND-RULE-INDEPENDENCE-"
        "MEASURED;x%d-MULTIPLICITY-DISCLOSED-NOT-FOLDED-IN)"
        % (",".join(full) if full else "NO-CONVENTION", len(full), len(cv),
           ";".join("%s:%d-OF-%d" % (k, cv[k][0], cv[k][1])
                    for k in sorted(cv)),
           S["convention_front_probes"],
           S["convention_derived_by_multiplication"]
           // max(1, S["convention_front_probes"])))
    P["dd_signature"] = (
        "LATTICE-TRANSLATIONS-CLOSE-AT-%d-OF-%d-AT-BOTH-REALISATIONS(FORCED:"
        "[v,w]=0-AT-CONSTANT-FIELDS;POSITIVE-CONTROL,MUTANT-FLIPS-IT);"
        "INFORMATIVE-BRACKETS(TWO-DISTINCT-NONZERO-GENERATORS)=%d-OF-%d;"
        "NONABELIAN-CORE-UNTESTED-BY-CONSTRUCTION"
        % (S["dd_closing"], S["dd_total"], S["dd_informative"],
           S["dd_total"]))
    P["correspondence_signature"] = (
        "RELATION-I=EXACT-IN-FORM-ANALOGICAL-IN-STATUS(A-CENTRAL-EXTENSION-"
        "WITH-A-BACKGROUND-COEFFICIENT:THE-COEFFICIENT-DOES-NOT-MOVE-WITH-THE-"
        "STATE-AT-%d-OF-%d-PAIRS);RELATION-II=PARTIAL(FRONT-EXACT-AT-1-OF-4-"
        "CONVENTIONS-AND-AT-CONSTANT-v;REGISTER-DEFECTIVE-AT-D-TOT,ABSORBED-"
        "AT-D-FULL-ON-THE-HOMOGENEOUS-SECTOR,ABSENT-AT-D-REG);"
        "RELATION-III=CONTENTLESS-ABELIAN([v,w]=0-AT-ALL-%d-BRACKETS);"
        "THE-POSITIVE-CLAIM=FIXED-BACKGROUND-COVARIANCE-WITH-GR-BRACKET-FORM;"
        "THE-UNQUALIFIED-NAME-HDA-IS-NOT-USED"
        % (S["commutator_configuration_independent"], S["commutator_pairs"],
           S["dd_total"]))
    P["lapse_signature"] = (
        "DECLARED-FAMILY-AND-ITS-LATTICE-TRANSLATES;ENLARGEMENT-PRINTED;"
        "RESIDUAL-MAGNITUDE-MOVES-AT-%d-OF-%d-COMPARISONS(ALL-UPWARD-AT-%d);"
        "COEFFICIENT-CLASS-MOVES-AT-%d-CELLS(FORCED-BY-(S))"
        % (len(S["lapse_coordinate_moves"]), S["lapse_comparisons"],
           S["lapse_moves_upward"],
           len(S["lapse_coordinate_moves_coefficient"])))
    P["realisation_signature"] = (
        "D-REG:%s;D-TOT:%s"
        % ("+".join(sorted(set(k.split("/")[1] for k in S["dh_tally"]
                               if k.startswith("D-REG/")))),
           "+".join(sorted(set(k.split("/")[1] for k in S["dh_tally"]
                               if k.startswith("D-TOT/"))))))
    tr = S["trajectory"]
    P["lsweep_signature"] = (
        "%s;STRUCTURE-CONSTANT-ALONG-L=%s(FORCED:class=f(W,B),NO-L-IN-IT);"
        "MAX-RESIDUAL-MOVES=%s(MEASURED)"
        % (",".join("d%dL%d/%s:%d-in-basis-of-%d"
                    % (t["d"], t["L"], t["scope"][0], t["basis_closing"],
                       t["cells"]) for t in tr),
           str(S["structure_constant_along_L"]).upper(),
           ",".join("%s" % t["max_residual"] for t in tr)))
    P["controls_signature"] = (
        "CHART-GROUP-CLOSES-AT-%d-OF-%d-ARENAS;TRANSLATION-EQUIVARIANT-AT-%d-"
        "OF-%d(FORCED:MODULAR-ARITHMETIC);SCRAMBLED-VIOLATES-AT-%d-OF-%d;"
        "RESIDUAL-COVARIANT-ON-THE-RECORD-LATTICE-AT-%d-CELLS(NON-VACUITY:%d-"
        "DISTINCT-NONZERO-BASE-CELLS);SCRAMBLED-BREAKS-AT-%d-CELLS"
        % (len([c for c in ctl["chart_group"] if c["closes"]]),
           len(ctl["chart_group"]),
           sum(p["equivariant_cells"] for p in ctl["positive"]),
           sum(p["total_cells"] for p in ctl["positive"]),
           sum(n["violating_cells"] for n in ctl["negative"]),
           sum(n["total_cells"] for n in ctl["negative"]),
           sum(c["covariant_cells"] for c in ctl["covariance"]
               if c["lattice"] == "RECORD"),
           sum(c["distinct_nonzero_base_cells"] for c in ctl["covariance"]
               if c["lattice"] == "RECORD"),
           sum(c["violating_cells"] for c in ctl["covariance"]
               if c["lattice"] == "SCRAMBLED")))
    P["scope_signature"] = (
        "FINITE-EXTENT-ONLY(NO-CONTINUUM-CLAIM);WEIGHT=%d-ONLY(w=1-DECLARED-"
        "NOT-SWEPT);TANGENTIAL-FIELDS=CONSTANT-IN-THE-CENSUS(BIJECTION-"
        "REQUIREMENT)+%d-DECLARED-NON-CONSTANT-BIJECTIVE-PROBES;"
        "DISTINCT-RULES=%s;DUPLICATE-RULE-GROUPS=%s;"
        "SIGNATURE-NOT-MEASURED;HKT-REPRESENTATION-LEG-NOT-ATTEMPTED"
        % (decl["density_weight"], S["nonconstant_fields_bijective"],
           ",".join("%s:%d-of-%d-in-HH,%d-of-%d-in-the-register-sector"
                    % (k, S["distinct_rules"][k]["distinct_in_the_HH_weight"],
                       S["distinct_rules"][k]["declared"],
                       S["distinct_rules"][k]["distinct_in_the_register_drag"],
                       S["distinct_rules"][k]["declared"])
                    for k in sorted(S["distinct_rules"])),
           "+".join("%s@d%d:%s" % (g[0], g[1], "=".join(g[2]))
                    for g in S["duplicate_rule_groups"])))
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

    n_text = verify_text_anchors()
    n_anch = verify_anchors()
    n_path = verify_path_anchors()
    derive_ha_code_anchor()
    gate("G-ANCHOR-COUNT",
         "every declared anchor row was actually verified: the counts are "
         "derived from the declaration tables, never typed",
         n_anch == len(ANCHOR_ROWS) and n_path == len(PATH_ANCHOR_ROWS)
         and n_text == len(TEXT_ANCHOR_ROWS)
         and len(ANCHORS) == n_anch + n_path + n_text + 1,
         {"verbatim_text": n_text, "declared_text": len(TEXT_ANCHOR_ROWS),
          "file_byte": n_anch, "declared_file_byte": len(ANCHOR_ROWS),
          "path_value": n_path, "declared_path_value": len(PATH_ANCHOR_ROWS),
          "registered": len(ANCHORS)})
    consumers = set(t[3] for t in TEXT_ANCHOR_ROWS)
    gate("G-NO-UNANCHORED-RUNTIME-INPUT",
         "every file this instrument reads at run time is a hash-pinned "
         "artifact carrying BOTH a byte anchor and a value anchor (path-value "
         "for JSON, verbatim-text context window for prose), or this unit's "
         "own owned artifact; no mutable repo state -- no ledger, no STATUS, "
         "no other unit's working file -- is read anywhere (RUNBOOK section "
         "14 addendum, v14 #46)",
         (sorted(set(r[1] for r in TEXT_ANCHOR_ROWS))
          == ["v14/note-r2-adjudication.md"]
          and all(any(a[1] == r[1] for a in ANCHOR_ROWS)
                  for r in TEXT_ANCHOR_ROWS)
          and all(any(a[1] == r[1] for a in ANCHOR_ROWS)
                  for r in PATH_ANCHOR_ROWS)
          and RUNTIME_READS == sorted(set(
              [r[1] for r in ANCHOR_ROWS] + ["v13/code/ha_successor_exact.py",
                                             "v14/paper-03-relativity-rung.md"]))),
         {"declared_runtime_reads": RUNTIME_READS,
          "text_anchor_consumers": sorted(consumers)}) \
        if MUTANT != "runtime-read-undeclared" else gate(
            "G-NO-UNANCHORED-RUNTIME-INPUT",
            "every input this instrument reads at run time is anchored",
            False, {"undeclared": "v14/LOG.md"})
    say("--- 1. ANCHORS ---")
    say("  verbatim-text anchors: %d ; file-byte anchors: %d ; path-value "
        "anchors: %d ; derived: 1" % (n_text, n_anch, n_path))
    for a in ANCHORS:
        say("    %-28s %-10s %s" % (a["name"], a["kind"][:10], a["artifact"]))
    say()

    rec7 = read_json(I7)
    decl = rec7["declarations"]
    r2 = read_json("v14/code/r2_manifold_receipt.json")

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
        "density_weight_scope": "w = 0 ONLY.  I7 also declares a weight flip "
                                "w = 1 (anchored at P-I7-WEIGHTFLIP); this "
                                "unit does not sweep it, and every "
                                "coefficient statement below is at w = 0",
        "tangential_realisations": ["D-REG = (0,1,0) (I7's primary)",
                                    "D-TOT = (1,1,0) (I7's flip test)",
                                    "D-FULL = (1,1,1) (the register "
                                    "transported along the same declared "
                                    "site map)",
                                    "and the other 24 of the 27 (a,b,c) "
                                    "triples, all censused"],
        "tangential_field_scope": "CONSTANT fields only in the bracket "
                                  "census, because x -> x + v(x) must be a "
                                  "bijection of the site set; two DECLARED "
                                  "non-constant bijective fields are run "
                                  "separately.  Consequence: the Lie bracket "
                                  "[v,w] vanishes identically on the censused "
                                  "family, so the third relation carries no "
                                  "discriminating content here",
        "census_arenas": [list(a) for a in CENSUS_ARENAS],
        "dense_route_arenas": [list(a) for a in DENSE_ARENAS],
        "literal_route_arenas": [list(a) for a in LITERAL_ROUTE_ARENAS],
        "realisation_arenas": [list(a) for a in REALISATION_ARENAS],
        "covariance_arenas": [list(a) for a in COVARIANCE_ARENAS],
        "covariance_probe_lapses": COVARIANCE_PROBE_LAPSES,
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
    lg = l_gate_reason(
        read_by_path(r2, ("locality_census", "criterion")),
        read_by_path(r2, ("locality_census", "count_locality_B")),
        read_by_path(r2, ("locality_census", "count_refuses_B")))
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
         "the L gate rests on ANCHORED inputs only: the locality criterion is "
         "READ BY JSON PATH out of the R2 terminal receipt and this unit's "
         "implementation of it is gated against a declared positive/negative "
         "graph pair; the ruling's own sentences arrive as verbatim-text "
         "anchors with context windows; and the overlap fractions are this "
         "unit's own cell-complete recomputation over the six declared "
         "extents.  Nothing here is a coincidence test against prose and "
         "nothing here is read from mutable repo state",
         (lg["criterion_probe"]
          ["implementation_agrees_with_the_inherited_criterion"]
          and len(lg["overlap_fractions_recomputed_here"])
          == lg["overlap_fractions_required"]
          and lg["r2_terminal_locality_count_read_by_path"] == 14
          and lg["r2_terminal_refusal_count_read_by_path"] == 5
          and sorted(lg["anchor_rows_consumed"])
          == sorted(t[0] for t in TEXT_ANCHOR_ROWS
                    if t[3] == "G-L-GATE-INHERITED-FACTS")),
         {"criterion_probe": lg["criterion_probe"],
          "fractions": [f["fraction"] for f in
                        lg["overlap_fractions_recomputed_here"]],
          "text_anchors": lg["anchor_rows_consumed"]})
    say("  overlap fractions recomputed here: %s"
        % ", ".join("d%dL%d %s" % (f["d"], f["L"], f["fraction"])
                    for f in lg["overlap_fractions_recomputed_here"]))
    say("  the inherited criterion, read by path from the R2 terminal "
        "receipt, applied: positive control %s, negative control %s"
        % (lg["criterion_probe"]["positive_control_path_graph_has_locality"],
           lg["criterion_probe"]
           ["negative_control_complete_graph_has_locality"]))
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
    res["realisation"] = run_realisation_census(decl, res)
    res["covariance"] = run_covariance_theorem(decl)
    res["structure"] = run_structure_probes(decl)
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
    gate("G-SPANNING-HYPOTHESIS",
         "HYPOTHESIS (S), MEASURED: the realised bracket covectors Omega span "
         "the FULL declared link space at EVERY site of every censused arena "
         "and lapse scope.  This is the load-bearing measurement of the whole "
         "{H,H} half -- it is what makes the extracted coefficient a "
         "DETERMINATION rather than a reading, and every uniqueness and "
         "scope-inertness statement below is a corollary of it.  Omega's "
         "independence of the record is measured, not assumed",
         (S["spanning_sites_at_full_rank"] == S["spanning_sites"]
          and S["spanning_rows"] == len(CENSUS_ARENAS) * len(LAPSE_SCOPES)
          and S["spanning_record_independent"] == S["spanning_rows"]
          and all(r["ranks"] == [r["link_space_dimension"]]
                  for r in res["spanning"])),
         {"sites_at_full_rank": S["spanning_sites_at_full_rank"],
          "sites": S["spanning_sites"], "rows": S["spanning_rows"],
          "record_independent": S["spanning_record_independent"]})
    gate("G-COMMUTATOR-TWO-ROUTES",
         "the LITERAL four-map composition H[N]H[M]H[N]^-1 H[M]^-1, applied to "
         "three declared front configurations, leaves the front unmoved and "
         "reproduces the closed-form register displacement exactly -- so the "
         "commutator is a PURE tangential generator, measured, not assumed",
         len(tr["literal_disagreements"]) == 0 and tr["literal_cells"] > 0,
         {"literal_cells": tr["literal_cells"],
          "disagreements": tr["literal_disagreements"][:4]})
    gate("G-CENSUS-THREE-ROUTES",
         "THREE routes, and the third shares no component with the other "
         "two: the support-restricted route and the dense route both build "
         "the residual from the gap matrix W - B, so a corruption of that "
         "shared component would move both together (RUNBOOK section 14 "
         "addendum, v13 #219); the third route reads the register "
         "displacement off the LITERAL four-map composition and subtracts the "
         "HDA generator, touching the gap matrix nowhere.  All three agree "
         "at every cell where they run, and every coverage is DERIVED AND "
         "PRINTED, never a silent cap -- including route 3's own probe, which "
         "is built so that EVERY declared link direction is realised, and "
         "whose realised-link count is part of this predicate: a route whose "
         "probe never touches a link cannot see a corruption living on that "
         "link's column",
         (len(tr["dense_disagreements"]) == 0 and tr["dense_cells"] > 0
          and len(tr["route3_disagreements"]) == 0 and tr["route3_cells"] > 0
          and len(tr["route3_links_realised"]) == len(LITERAL_ROUTE_ARENAS)
          and all(v[0] == v[1]
                  for v in tr["route3_links_realised"].values())),
         {"dense_cells": tr["dense_cells"],
          "dense_arenas": tr["dense_arenas"],
          "route3_cells": tr["route3_cells"],
          "route3_arenas": tr["route3_arenas"],
          "route3_links_realised": tr["route3_links_realised"],
          "dense_disagreements": tr["dense_disagreements"][:4],
          "route3_disagreements": tr["route3_disagreements"][:4]})
    say("  routes: dense %d cells (%d disagreements) ; literal %d cells (%d) ; "
        "bracket-literal %d (%d) ; convention-literal %d (%d)"
        % (tr["dense_cells"], len(tr["dense_disagreements"]),
           tr["literal_cells"], len(tr["literal_disagreements"]),
           tr["dh_literal_cells"], len(tr["dh_literal_disagreements"]),
           tr["conv_literal_cells"], len(tr["conv_literal_disagreements"])))
    say("  coefficient classes (computed): %s" % S["coefficient_classes"])
    say("  closure forms (computed): %s" % S["closure_forms"])
    say("  basis closure: %d of %d cells lie in the declared generator basis; "
        "%d of them close with a CONSTANT NON-METRIC coefficient (the pin's "
        "RIGID form)"
        % (S["basis_closing_cells"], S["census_cells"], S["rigid_cells"]))
    say("  the positive control: metric-matches at %d of %d cells; its "
        "coefficient is a metric reading at %d of %d, site-varying at %d"
        % (S["positive_control_metric_match"],
           S["positive_control_census_cells"],
           S["positive_control_metric_reading"], S["positive_control_cells"],
           S["positive_control_site_varying"]))
    # THE NON-EXTRACTABILITY CRITERION, computed rather than asserted: the
    # coefficient system is inconsistent at exactly the cells whose weight
    # matrix carries a NONZERO DIAGONAL-LINK COLUMN.  Which declared rules
    # those are is a MEASUREMENT, and it is not "the architecture-B rules".
    nx_pred, nx_meas, nx_rules, archb_cells = [], [], set(), 0
    for (dd, LL) in CENSUS_ARENAS:
        rr = build_records(dd, LL, decl)
        ad = sorted([n for n in rr if rr[n].admissible])
        for rule in rules_at(dd, decl):
            for nm in ad:
                if weight_has_diagonal_column(rule, rr[nm]):
                    nx_pred.append((dd, LL, rule, nm))
                    nx_rules.add(rule)
                if arch_of(rule) == "B":
                    archb_cells += len(LAPSE_SCOPES)
    nx_meas = sorted(set((c["d"], c["L"], c["rule"], c["record"])
                         for c in res["coefficients"]
                         if c["coefficient"]["class"] == CLASS_NX))
    if MUTANT == "not-extractable-attribution":
        nx_rules = set(r[0] for r in RULE_TABLE if arch_of(r[0]) == "B")
    nx_meas_rules = sorted(set(c["rule"] for c in res["coefficients"]
                               if c["coefficient"]["class"] == CLASS_NX))
    gate("G-COEFFICIENT-EXTRACTION",
         "the structure coefficient is SOLVED FOR from the commutators "
         "themselves over every ordered lapse pair, not read off the rule; "
         "and the over-determined system is inconsistent at EXACTLY the cells "
         "whose weight matrix carries a nonzero DIAGONAL-LINK column -- the "
         "iff, computed over every census cell, not asserted of a rule class.  "
         "THE ATTRIBUTION IS PART OF THE PREDICATE, twice over: the set of "
         "rules the mechanism names must equal the set of rules the census "
         "measures, so naming a rule CLASS instead of the measured rules "
         "fails here; and architecture A populates only axis columns BY "
         "CONSTRUCTION, so an architecture-A rule acquiring a diagonal-link "
         "column fails here too",
         (S["not_extractable_cells"] > 0
          and sorted(set(nx_pred)) == nx_meas
          and sorted(nx_rules) == nx_meas_rules
          and all(arch_of(r) == "B" for r in nx_rules)
          and S["positive_control_metric_reading"]
          == S["positive_control_cells"]),
         {"not_extractable": S["not_extractable_cells"],
          "predicted": len(set(nx_pred)), "measured": len(nx_meas),
          "rules_with_a_diagonal_column": sorted(nx_rules),
          "rules_measured_not_extractable": nx_meas_rules,
          "architecture_B_cells": archb_cells,
          "positive_control_metric_reading": S["positive_control_metric_reading"],
          "positive_control_cells": S["positive_control_cells"]})
    S["not_extractable_rules"] = sorted(nx_rules)
    S["architecture_B_cells"] = archb_cells
    # the class census's own INDEPENDENT expectation, from the predictor
    exp_classes = set()
    for (dd, LL) in CENSUS_ARENAS:
        rr = build_records(dd, LL, decl)
        for rule in rules_at(dd, decl):
            for nm in sorted([n for n in rr if rr[n].admissible]):
                exp_classes.add(predict_class(rule, rr[nm]))
    gate("G-METRIC-COMPARATOR-INDEPENDENT",
         "THE METRIC COMPARISON HAS A THIRD ROUTE that shares no inversion "
         "primitive with the other two.  The extraction reaches q through the "
         "exact linear solve and the type comparator through the closed form, "
         "but both invert it with the same routine -- a residual #219 "
         "exposure.  Here every cell typed a metric reading has its extracted "
         "coefficient multiplied by q directly and compared against the "
         "identity, with no inverse taken anywhere",
         (tr["metric_identity_sites"] > 0
          and tr["metric_identity_failures"] == 0),
         {"sites_verified": tr["metric_identity_sites"],
          "failures": tr["metric_identity_failures"]})
    gate("G-COEFFICIENT-TYPING",
         "the coefficient class is TYPED BY MEASUREMENT against an "
         "independently re-encoded record metric: a site-varying metric "
         "reading (GR's bracket form) is separated from a constant one only "
         "on the inhomogeneous records, and that separation is realised.  "
         "(The class census's agreement with the analytic predictor is the "
         "structure theorem's own gate, cell by cell, which is strictly "
         "stronger than a comparison of class SETS.)",
         S["inhomogeneous_site_varying_metric"] > 0
         and CLASS_MRC in S["coefficient_classes"]
         and CLASS_CNM in S["coefficient_classes"],
         {"classes": S["coefficient_classes"],
          "expected_classes": sorted(exp_classes),
          "inhomogeneous_site_varying": S["inhomogeneous_site_varying_metric"],
          "inhomogeneous_cells": S["inhomogeneous_cells"]})
    gate("G-STRUCTURE-THEOREM",
         "THE STRUCTURE THEOREM, verified cell by cell: rho = (W - B).Omega, "
         "so METRIC MATCH is W == B pointwise and -- given (S) -- the "
         "coefficient class is a PURE FUNCTION of the rule's weight field and "
         "the record's readout.  An analytic predictor carrying NO commutator, "
         "no lapse and no bracket reproduces every census cell's class and "
         "every cell's metric-match status.  The census clauses are therefore "
         "carried FORCED (#208), and this gate is what establishes it",
         (len(tr["class_mispredictions"]) == 0
          and len(tr["metric_match_prediction_mismatches"]) == 0
          and tr["class_prediction_cells"] == S["census_cells"]),
         {"cells": tr["class_prediction_cells"],
          "class_mispredictions": tr["class_mispredictions"][:4],
          "metric_match_mismatches":
              tr["metric_match_prediction_mismatches"][:4]})
    gate("G-RIGID-BRANCH-REACHABLE",
         "THE PIN'S THIRD OUTCOME IS REACHABLE, and reached.  Closure is "
         "tested against the DECLARED GENERATOR BASIS, not against the answer "
         "being looked for, so a cell may close with a coefficient that is "
         "constant and demonstrably NOT the record metric -- the pin's RIGID "
         "form.  Measured: the rigid cells are non-empty, they are disjoint "
         "from the metric-matching cells, and the verdict machinery returns "
         "the RIGID head on a synthetic payload built to exhibit it",
         (S["rigid_cells"] > 0
          and all(not r["metric_match"] for r in res["census"] if r["rigid"])
          and all(r["basis_closes"] for r in res["census"] if r["rigid"])
          and rigid_probe()[0] == HEAD_CLOSES
          and "RIGID-CONSTANT-NON-METRIC" in rigid_probe()[1]),
         {"rigid_cells": S["rigid_cells"],
          "basis_closing": S["basis_closing_cells"],
          "synthetic_head": rigid_probe()[0],
          "synthetic_closure_segment": rigid_probe()[1]})
    say()
    return rec7, decl, arena, lg, rec_out, res, S, tr


def run_part2(rec7, decl, arena, lg, rec_out, res, S, tr):
    # the realisation census's and the covariance theorem's own denominators,
    # DERIVED from the declaration
    exp_realisation = 0
    for (dd_, LL) in REALISATION_ARENAS:
        rr = build_records(dd_, LL, decl)
        exp_realisation += (len([n for n in rr if rr[n].admissible])
                            * len(rules_at(dd_, decl)) * DEFECT_PROBE_LAPSES
                            * dd_ * len(REALISATION_ATOM_VALUES) ** 3)
    exp_covariance = 0
    for (dd_, LL) in COVARIANCE_ARENAS:
        rr = build_records(dd_, LL, decl)
        exp_covariance += (len([n for n in rr if rr[n].admissible])
                           * len(rules_at(dd_, decl))
                           * COVARIANCE_PROBE_LAPSES * dd_)
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
    gate("G-CONVENTION-FRONT-INDEPENDENT",
         "THE MULTIPLICATION'S LICENCE, MEASURED.  The convention sweep is "
         "evaluated once per (lapse, translation) probe and its result then "
         "holds across records and rules -- so the record- and "
         "rule-independence of the bracket's FRONT sector is the premise the "
         "whole denominator rests on, and it is CHECKED here by evaluating "
         "the front closed form at every declared record and at two declared "
         "rules per arena and comparing the rows for equality.  (The gate it "
         "replaces was a divisibility identity: true for any input the arena "
         "admits, and therefore no gate at all.)  The sweep's own reported "
         "denominator is the DISTINCT PROBE COUNT; the record x rule "
         "multiplicity is disclosed beside it, never folded in",
         (len(tr["front_independence_disagreements"]) == 0
          and tr["front_independence_rows"] > 0),
         {"rows": tr["front_independence_rows"],
          "disagreements": tr["front_independence_disagreements"][:4],
          "distinct_front_probes": S["convention_front_probes"],
          "derived_by_multiplication":
              S["convention_derived_by_multiplication"]})
    say()

    say("--- 7. THE DEFECT, CHARACTERISED ---")
    say("  probes %d ; vanishing %d ; lattice-sum-zero %d ; vanishing on the "
        "homogeneous sector %d of %d"
        % (S["defect_probes"], S["defect_vanishing_probes"],
           S["defect_lattice_sum_zero"], S["defect_vanishes_on_homogeneous"],
           S["defect_homogeneous_probes"]))
    # DERIVED DENOMINATORS for the three bracket tables and the defect table:
    # every row count and every probe count is what the arena declaration
    # forces, computed here.  A dropped row or a zeroed field cannot hide
    # behind a "> 0" threshold.
    exp_defect_rows = exp_defect_probes = 0
    exp_dh_rows = exp_dh_brackets = 0
    exp_dd_rows = exp_dd_brackets = 0
    for (dd_, LL) in CENSUS_ARENAS:
        rr = build_records(dd_, LL, decl)
        nadm = len([n for n in rr if rr[n].admissible])
        nrul = len(rules_at(dd_, decl))
        nlap = len(dh_probe_family(dd_, LL, build_lapse_family(dd_, LL)))
        exp_defect_rows += nadm * nrul
        exp_defect_probes += nadm * nrul * DEFECT_PROBE_LAPSES * dd_
        exp_dh_rows += nadm * nrul * len(REALISATIONS)
        exp_dh_brackets += nadm * nrul * len(REALISATIONS) * nlap * dd_
        exp_dd_rows += nadm * len(REALISATIONS)
        exp_dd_brackets += nadm * len(REALISATIONS) * (dd_ + 1) ** 2
    gate("G-DEFECT-MEASURED",
         "the normal-tangential defect is a MEASURED OBJECT, not a failure, "
         "and every clause of that sentence is a PREDICATE here against a "
         "DERIVED denominator: the probe count is what the declaration "
         "forces, the defect vanishes at ZERO probes, and it vanishes on the "
         "homogeneous sector at ZERO probes.  Erasing the field cannot pass "
         "this gate.  (The lattice-sum clause is the boundary gate's own, "
         "next, so that each gate carries the clause its own falsifier "
         "attacks.)",
         (S["defect_probes"] == exp_defect_probes
          and S["defect_rows"] == exp_defect_rows
          and S["defect_vanishing_probes"] == 0
          and S["defect_vanishes_on_homogeneous"] == 0),
         {"probes": S["defect_probes"], "required_probes": exp_defect_probes,
          "rows": S["defect_rows"], "required_rows": exp_defect_rows,
          "vanishing": S["defect_vanishing_probes"],
          "lattice_sum_zero": S["defect_lattice_sum_zero"],
          "vanishing_on_homogeneous": S["defect_vanishes_on_homogeneous"]})
    gate("G-BOUNDARY-TERM-STATUS",
         "BOUNDARY-TERM TEST on a periodic lattice: a defect that were a total "
         "finite difference would sum to zero over the lattice.  It does not, "
         "at any probe.  THE DEGENERATE PROBE IS BUILT AND MEASURED, not "
         "typed: the ZERO lapse profile gives a defect field that is "
         "identically zero and whose lattice sum IS zero, at every one of its "
         "probes -- the test's own death certificate, computed.  The unit "
         "constant profile is measured beside it and is reported at whatever "
         "it comes out",
         (S["defect_lattice_sum_zero"] == 0 and S["defect_probes"] > 0
          and S["degenerate_zero_probes"] > 0
          and S["degenerate_zero_vanishing"] == S["degenerate_zero_probes"]
          and S["degenerate_zero_lattice_sum_zero"]
          == S["degenerate_zero_probes"]),
         {"lattice_sum_zero": S["defect_lattice_sum_zero"],
          "probes": S["defect_probes"],
          "degenerate_probes": S["degenerate_zero_probes"],
          "degenerate_vanishing": S["degenerate_zero_vanishing"],
          "degenerate_lattice_sum_zero":
              S["degenerate_zero_lattice_sum_zero"],
          "constant_profile_probes": S["constant_profile_probes"],
          "constant_profile_vanishing": S["constant_profile_vanishing"]})
    gate("G-BRACKET-TABLES-CELL-COMPLETE",
         "the {D,H}, {D,D} and defect tables are cell-complete against "
         "DERIVED denominators: row counts and bracket counts equal what the "
         "arena declaration forces.  A dropped row moves a number this gate "
         "recomputes",
         (len(res["dh"]) == exp_dh_rows
          and S["dh_brackets"] == exp_dh_brackets
          and len(res["dd"]) == exp_dd_rows
          and S["dd_total"] == exp_dd_brackets
          and S["defect_rows"] == exp_defect_rows),
         {"dh_rows": len(res["dh"]), "required_dh_rows": exp_dh_rows,
          "dh_brackets": S["dh_brackets"],
          "required_dh_brackets": exp_dh_brackets,
          "dd_rows": len(res["dd"]), "required_dd_rows": exp_dd_rows,
          "dd_brackets": S["dd_total"],
          "required_dd_brackets": exp_dd_brackets,
          "defect_rows": S["defect_rows"],
          "required_defect_rows": exp_defect_rows})
    gate("G-REALISATION-CENSUS",
         "THE REALISATION CENSUS: all 27 (a, b, c) triples built from the "
         "tangential family's TWO DECLARED ATOMS -- the site map and the "
         "address register -- are censused, with the classification count "
         "DERIVED from the declaration.  Two results are measured: "
         "IN-CONSTRAINT is reached at ZERO classifications, at EVERY "
         "declared-expressible realisation (the DEFECT head is therefore "
         "realisation-INDEPENDENT); and at the realisations that transport "
         "the register along the same declared site map, the bracket lands in "
         "the extended basis on the WHOLE homogeneous sector, resisting "
         "exactly on the inhomogeneous records -- the residue is "
         "CURVATURE-SUPPORTED",
         (S["realisation_count"] == len(REALISATION_ATOM_VALUES) ** 3
          and S["realisation_classifications"] == exp_realisation
          and S["realisation_in_constraint"] == 0
          and len(S["absorbing_realisations"]) > 0
          and S["realisation_outside_on_the_homogeneous_sector"] == 0
          and S["residue_is_exactly_the_inhomogeneous_records"]
          and len(res["realisation"]["literal_disagreements"]) == 0
          and res["realisation"]["literal_cells"] > 0),
         {"realisations": S["realisation_count"],
          "classifications": S["realisation_classifications"],
          "required": exp_realisation,
          "in_constraint": S["realisation_in_constraint"],
          "absorbing": S["absorbing_realisations"],
          "outside_on_the_homogeneous_sector":
              S["realisation_outside_on_the_homogeneous_sector"],
          "residue_cells": S["curvature_supported_residue_count"],
          "literal_cross_check_cells":
              res["realisation"]["literal_cells"],
          "literal_disagreements":
              res["realisation"]["literal_disagreements"][:4]})
    gate("G-COVARIANCE-THEOREM",
         "THE COVARIANCE THEOREM, measured: conjugation by FULL transport "
         "carries the constraint of the record to the constraint of the "
         "TRANSPORTED record, D_full[v] . H_g[N] . D_full[v]^-1 = "
         "H_{S_v g}[S_v N], exactly, at every cell of a DERIVED probe -- and "
         "it FAILS at D-TOT, which transports the front but not the "
         "register's labelling.  The negative side is what makes the "
         "positive one a measurement.  What survives as an obstruction is "
         "that the record itself does not transport: the arena carries a "
         "FIXED BACKGROUND, and this functional is the instrument that "
         "detects it",
         (S["covariance_cells"] == exp_covariance
          and S["covariance_d_full"] == S["covariance_cells"]
          and S["covariance_d_tot"] < S["covariance_cells"]),
         {"cells": S["covariance_cells"], "required": exp_covariance,
          "d_full_covariant": S["covariance_d_full"],
          "d_tot_covariant": S["covariance_d_tot"]})
    gate("G-CENTRAL-EXTENSION",
         "THE OBJECT THE FIRST BRACKET LIVES IN, named and measured: "
         "H[N] H[M] = T_{w[N,M]} . H[N+M] at every cell of a derived probe, "
         "so the constraint family generates a two-step nilpotent group -- a "
         "CENTRAL EXTENSION of the abelian group of lapse profiles by the "
         "register fields, with w as its two-cocycle -- and the extracted "
         "'structure coefficient' is that cocycle's antisymmetrisation.  "
         "Measured beside it: the commutator field is CONFIGURATION-"
         "INDEPENDENT at every pair, which is exactly the property an open "
         "algebra must not have",
         (S["central_extension_holds"] == S["central_extension_cells"]
          and S["central_extension_cells"] > 0
          and S["commutator_configuration_independent"]
          == S["commutator_pairs"] and S["commutator_pairs"] > 0),
         {"cells": S["central_extension_cells"],
          "holds": S["central_extension_holds"],
          "pairs": S["commutator_pairs"],
          "configuration_independent":
              S["commutator_configuration_independent"]})
    gate("G-DEFECT-ROBUSTNESS",
         "the defect survives the two attacks its own declarations invite: "
         "the OTHER declared bracket order (the one whose front sector "
         "reproduces L_v N under the declared backward convention), and "
         "DECLARED NON-CONSTANT tangential fields whose site maps are "
         "measured bijections with measured inverses.  Neither kills it",
         (S["order_probes"][BRACKET_ORDERS[1]][0]
          == S["order_probes"][BRACKET_ORDERS[1]][1]
          and S["order_probes"][BRACKET_ORDERS[1]][1] > 0
          and S["nonconstant_fields_bijective"] > 0
          and S["nonconstant_outside"] == S["nonconstant_probes"]
          and S["nonconstant_probes"] > 0),
         {"orders": S["order_probes"],
          "nonconstant_outside": S["nonconstant_outside"],
          "nonconstant_probes": S["nonconstant_probes"],
          "bijective_fields": S["nonconstant_fields_bijective"]})
    gate("G-DD-RELATION-CONTENT",
         "the third relation's content, measured rather than implied: of the "
         "tangential brackets censused, the INFORMATIVE ones -- those pairing "
         "two DISTINCT NONZERO generators -- are counted, and the Lie bracket "
         "[v, w] vanishes at every one of them because the declared family "
         "contains only constant fields.  The relation's nonabelian core is "
         "therefore untested BY CONSTRUCTION, and the census says so instead "
         "of reporting a closure it could not fail",
         (S["dd_informative"] > 0 and S["dd_informative"] < S["dd_total"]
          and all(r["lie_bracket_nonzero"] == 0 for r in res["dd"])),
         {"informative": S["dd_informative"], "total": S["dd_total"],
          "lie_bracket_nonzero": sum(r["lie_bracket_nonzero"]
                                     for r in res["dd"])})
    gate("G-DUPLICATE-RULES-DISCLOSED",
         "the declared rule list contains EXACT DUPLICATES, and the census "
         "says which and where: the rules are partitioned by their whole "
         "weight field over every admissible record and site, separately in "
         "the {H,H} sector and in the register sector, and the distinct-rule "
         "counts are reported next to the declared count",
         (len(S["duplicate_rule_groups"]) > 0
          and all(v["distinct_in_the_HH_weight"] <= v["declared"]
                  and v["distinct_in_the_register_drag"] <= v["declared"]
                  for v in S["distinct_rules"].values())),
         {"distinct": S["distinct_rules"],
          "duplicate_groups": S["duplicate_rule_groups"]})
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
               c["violating_cells"], c["distinct_nonzero_base_cells"]))
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
         and all(c["distinct_nonzero_base_cells"] > 0
                 for c in ctl["covariance"]),
         {"negative": ctl["negative"],
          "covariance": ctl["covariance"]})
    gate("G-SYMMETRY-SELFTEST",
         "RUNBOOK section 14 symmetry self-test, FRESH-EVALUATED ON BOTH "
         "SIDES: the residual field transports exactly with the record and "
         "the lapses under every chart translation of the record lattice, "
         "with the weight memo BYPASSED on the base side as well as the "
         "transported one -- and the number of fresh bypasses the self-test "
         "actually performed is gated, because a self-test that never leaves "
         "the cache tests the cache and not the quantity (RUNBOOK section 14 "
         "addendum, v13 #185)",
         (all(c["violating_cells"] == 0
              and c["distinct_nonzero_base_cells"] > 0
              and c["fresh_bypasses_used"] > 0
              for c in ctl["covariance"] if c["lattice"] == "RECORD")),
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
    say("  %-4s %-4s %-11s %6s %7s %6s %7s %10s %8s %8s"
        % ("d", "L", "scope", "cells", "inbasis", "rigid", "metric",
           "maxres", "mreading", "sitevar"))
    for t in S["trajectory"]:
        say("  %-4d %-4d %-11s %6d %7d %6d %7d %10s %8d %8d"
            % (t["d"], t["L"], t["scope"], t["cells"], t["basis_closing"],
               t["rigid"], t["metric_match"], t["max_residual"],
               t["metric_reading"], t["site_varying_metric"]))
    gate("G-LSWEEP-COMPLETE",
         "the L-sweep is trajectory-complete: every declared (d, L, lapse "
         "scope) triple carries a row, and the row count is derived from the "
         "declaration",
         len(S["trajectory"]) == len(CENSUS_ARENAS) * len(LAPSE_SCOPES),
         {"rows": len(S["trajectory"]),
          "required": len(CENSUS_ARENAS) * len(LAPSE_SCOPES)})
    gate("G-LSWEEP-STABILITY",
         "the census's WHOLE SHAPE is measured along the refinement "
         "direction: at fixed d the cell count, the basis-closure count, the "
         "rigid count, the metric-match count and every coefficient-class "
         "count are constant in L and in the lapse scope.  Per the structure "
         "theorem this constancy is FORCED -- the per-cell class is a "
         "function of (rule, record) alone, in which neither L nor the lapse "
         "family appears -- and it is carried at that label; what genuinely "
         "MOVES along the sweep is the residual's MAGNITUDE, reported beside "
         "it",
         (S["structure_constant_along_L"]
          and len(set(t["max_residual"] for t in S["trajectory"])) > 1),
         {"per_d": sorted(set((t["d"], t["cells"], t["basis_closing"],
                               t["rigid"], t["metric_match"],
                               t["metric_reading"], t["site_varying_metric"],
                               t["not_extractable"])
                              for t in S["trajectory"])),
          "max_residuals": [t["max_residual"] for t in S["trajectory"]]})
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
             {"forced": ["HH-BRACKET landing + empty normal channel",
                         "the closure census, the coefficient-class census "
                         "and every class count, all of which the structure "
                         "theorem rho = (W - B).Omega derives from the "
                         "declarations with no commutator anywhere",
                         "the L-constancy and lapse-scope inertness of the "
                         "structural columns"],
              "measured": ["hypothesis (S): the spanning of the realised "
                           "bracket covectors, which is what makes the "
                           "coefficient a determination",
                           "the residual MAGNITUDES, which do move",
                           "the literal-composition agreements",
                           "the sector arithmetic"]})
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
             "AT THE POSITIVE CONTROL BOTH THE COEFFICIENT'S VALUE AND ITS "
             "SITE-VARIATION CLASS ARE FORCED.  The metric-inserted rule's "
             "weight IS the record-read inverse metric by declaration, so an "
             "extraction that recovers Lambda recovers the metric; and "
             "CONSTANT versus SITE-VARYING then asks only whether the "
             "record's own count field is constant, which is a property of "
             "the ARENA and contains no bracket.  What is MEASURED is "
             "UNIQUENESS -- hypothesis (S), the full spanning of the realised "
             "bracket covectors, so no other coefficient reproduces the "
             "commutators -- and the class census at the rules that do NOT "
             "insert the metric.",
             {"forced": ["metric_reading = True at the positive control",
                         "its site-variation class, inherited from the "
                         "record's inhomogeneity"],
              "measured": ["hypothesis (S)",
                           "the class census away from the positive control"]})
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
             "NON-EXTRACTABILITY IS FORCED, AND IT IS A PROPERTY OF ONE "
             "DECLARED RULE, NOT OF AN ARCHITECTURE.  The coefficient system "
             "is inconsistent at exactly the cells whose weight matrix "
             "carries a nonzero DIAGONAL-LINK column, because no d x d "
             "coefficient acting on the d axis covectors can reproduce a "
             "diagonal-link bracket.  MEASURED: the rules with such a column "
             "are %s -- %d of the %d architecture-B cells, not all of them.  "
             "The other architecture-B rules weight only the axis links and "
             "are extractable at every one of their cells."
             % (", ".join(S["not_extractable_rules"]),
                S["not_extractable_cells"], S["architecture_B_cells"]),
             {"forced": "NOT-EXTRACTABLE where the weight has a diagonal-link "
                        "column",
              "measured": "which declared rules those are, and that the same "
                          "solve succeeds everywhere else"})
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
    disclose("X08",
             "THE TANGENTIAL FAMILY IS RESTRICTED TO CONSTANT FIELDS IN THE "
             "CENSUS, and the reason is the bijection requirement: D_a[v] "
             "acts on sites through x -> x + v(x), which must be a "
             "permutation of the site set.  This restriction has TWO COSTS, "
             "both carried at the claim.  (i) The Lie bracket [v, w] vanishes "
             "identically on the censused family, so the third relation "
             "{D[v],D[w]} = D[[v,w]] carries NO discriminating content here: "
             "its nonabelian core is untested BY CONSTRUCTION, not merely "
             "forced.  (ii) The generator the first bracket produces is "
             "itself generally not a member of the family the second bracket "
             "uses, so the three relations are not simultaneously realisable "
             "on one declared tangential family at this arena.  Two DECLARED "
             "non-constant bijective fields are run separately, and the "
             "defect survives both.",
             {"restriction": "constant tangential fields in the census",
              "reason": "x -> x + v(x) must be a bijection",
              "costs": ["relation III contentless", "one realisation for "
                        "three relations not available here"]})
    disclose("X09",
             "THE WHOLE UNIT RUNS AT DENSITY WEIGHT w = 0.  I7 declares a "
             "weight flip w = 1 as well (anchored here at P-I7-WEIGHTFLIP), "
             "and the density weight is exactly the property that ties the "
             "normal-tangential relation to the Lie-derivative form of its "
             "right-hand side.  This unit does not sweep it.  Every "
             "coefficient, closure and defect statement below is at w = 0, "
             "and the ARENA segment carries that scope.",
             {"scope": "w = 0 only", "declared_and_not_swept": "w = 1"})
    disclose("X10",
             "THE DECLARED RULE LIST CONTAINS EXACT DUPLICATES, measured "
             "here: %s.  The distinct-rule counts are %s.  Every count over "
             "'rules' in this unit is a count over the DECLARED list, and the "
             "duplicate structure is what makes some of those counts smaller "
             "than they look."
             % ("; ".join("%s at d=%d: %s" % (g[0], g[1], " = ".join(g[2]))
                          for g in S["duplicate_rule_groups"]),
                ", ".join("d=%s: %d of %d distinct in the {H,H} weight, %d of "
                          "%d in the register sector"
                          % (k[1:], S["distinct_rules"][k]
                             ["distinct_in_the_HH_weight"],
                             S["distinct_rules"][k]["declared"],
                             S["distinct_rules"][k]
                             ["distinct_in_the_register_drag"],
                             S["distinct_rules"][k]["declared"])
                          for k in sorted(S["distinct_rules"]))),
             {"duplicate_groups": S["duplicate_rule_groups"],
              "distinct": S["distinct_rules"]})
    disclose("X11",
             "THE TRANSLATION CONTROL'S 100%% IS FORCED BY MODULAR "
             "ARITHMETIC.  nb(x+u, l) = (x+u)+l = (x+l)+u = nb(x,l)+u holds "
             "identically on (Z_L)^d, so the equivariance count cannot come "
             "out otherwise on the record lattice.  It is carried as a "
             "FORCED clause and its value is the SCRAMBLED lattice's "
             "violation count, which is a measurement and is nonzero.",
             {"forced": "translation equivariance on the record lattice",
              "measured": "the scrambled lattice's violations"})
    disclose("X12",
             "THE CONVENTION SWEEP'S REPORTED DENOMINATOR IS ITS DISTINCT "
             "PROBE COUNT.  The bracket's front sector is a function of the "
             "lapse and the translation alone -- measured, not asserted, by "
             "G-CONVENTION-FRONT-INDEPENDENT -- so the sweep is evaluated "
             "once per (lapse, translation) probe.  The record x rule "
             "multiplicity is DISCLOSED beside the probe count and is never "
             "folded into it: a count obtained by multiplying a measured "
             "sample by an unvaried axis is an argument, not a census.",
             {"probes": S["convention_front_probes"],
              "derived_by_multiplication":
                  S["convention_derived_by_multiplication"]})
    if MUTANT == "disclosure-drop":
        del DISCLOSURES[0]
    for dsc in DISCLOSURES:
        say("  %s  %s" % (dsc["id"], dsc["statement"][:96] + "..."))
    gate("G-FORCED-CLAUSES-DISCLOSED",
         "every clause this unit can derive from its own declarations without "
         "measuring is carried as a DISCLOSURE at that label, and the verdict "
         "segments that report such clauses say FORCED in the emitted string "
         "(RUNBOOK section 14 addendum, v13 #208)",
         len(DISCLOSURES) == 12
         and sorted(d["id"] for d in DISCLOSURES)
         == ["X%02d" % k for k in range(1, 13)],
         {"disclosures": [d["id"] for d in DISCLOSURES]})
    say()

    # ---- THE VERDICT -----------------------------------------------------
    P = build_signatures(decl, res, S, rec_out, lg, ctl)
    head, segs, full = build_verdict(P, MUTANT == "verdict-pair-swap")
    rp = rigid_probe()
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
        "degenerate_rows": res["degenerate"],
        "order_rows": res["orders"],
        "spanning_rows": res["spanning"],
        "realisation_rows": res["realisation"]["rows"],
        "realisation_census": dict((k, v) for k, v in
                                   res["realisation"].items() if k != "rows"),
        "covariance_rows": res["covariance"]["rows"],
        "covariance": dict((k, v) for k, v in res["covariance"].items()
                           if k != "rows"),
        "structure_rows": res["structure"],
        "rigid_branch_probe": {"head": rp[0], "closure_form": rp[1],
                               "failing_sectors": rp[2],
                               "note": "a synthetic payload in which every "
                                       "bracket lands in the declared basis "
                                       "with a CONSTANT NON-METRIC "
                                       "coefficient, fed to the delivered "
                                       "verdict builder: the pin's RIGID "
                                       "outcome is reachable and this is the "
                                       "demonstration"},
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
    # DEEP-COPY the sub-objects the comparator reads, so object identity can
    # never be mistaken for agreement (RUNBOOK section 14 addendum, v13 #219).
    rebuilt = reconstruct_verdict_from_receipt(
        json.loads(json.dumps(jsonable(R))))
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

# THE GATED SUBTREE.  Every measured object a gate reads is named here; the
# seal below is a digest of exactly these, taken AFTER the last measurement
# gate and re-verified at write time.  A mutation of R between the gates and
# the write -- the post-gate corruption class -- moves the seal and dies.
SEALED_KEYS = ("arena_declaration", "l_gate", "recovery", "census_rows",
               "coefficient_rows", "decomposition_rows", "dh_bracket_rows",
               "dd_bracket_rows", "convention_sweep", "defect_rows",
               "degenerate_rows", "order_rows", "spanning_rows",
               "realisation_rows", "realisation_census", "covariance_rows",
               "covariance", "structure_rows", "rigid_branch_probe",
               "two_route", "controls", "cache_exercise", "summary",
               "verdict", "anchors", "disclosures")


def payload_seal(R):
    blob = json.dumps([jsonable(R[k]) for k in SEALED_KEYS],
                      sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


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
                  "metric", "max|rho|"))
    for r in R["census_rows"]:
        out.append("  %-3d %-3d %-11s %-14s %-11s %8d %8d %-7s %10s"
                   % (r["d"], r["L"], r["scope"], r["rule"], r["record"],
                      r["nonzero_pairs"], r["total_pairs"],
                      r["metric_match"],
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
    out.append("")
    out.append("--- 15a. THE SPANNING CENSUS, HYPOTHESIS (S) (gated object) ---")
    for r in R["spanning_rows"]:
        out.append("  d=%d L=%d %-11s sites %3d  link space %d  full rank at "
                   "%3d  ranks %s  record-independent %s"
                   % (r["d"], r["L"], r["scope"], r["sites"],
                      r["link_space_dimension"], r["sites_at_full_rank"],
                      r["ranks"], r["record_independent"]))
    out.append("")
    out.append("--- 15b. THE REALISATION CENSUS, 27 (a,b,c) (gated object) ---")
    for r in R["realisation_rows"]:
        out.append("  d=%d L=%d %-12s (%2d,%2d,%2d)  %-52s resisting %d cells"
                   % (r["d"], r["L"], r["name"], r["realisation"][0],
                      r["realisation"][1], r["realisation"][2],
                      str(r["tally"]), len(r["resisting_cells"])))
    out.append("")
    out.append("--- 15c. THE COVARIANCE THEOREM (gated object) ---")
    out.append("  %s" % R["covariance"]["statement"])
    for r in R["covariance_rows"]:
        out.append("  d=%d L=%d cells %4d  D-FULL covariant %4d  D-TOT "
                   "covariant %4d  (lapse probe %d, %d configurations)"
                   % (r["d"], r["L"], r["cells"], r["d_full_covariant"],
                      r["d_tot_covariant"], r["lapse_probe"],
                      r["configurations"]))
    out.append("")
    out.append("--- 15d. THE DEGENERATE PROBES AND THE OTHER ORDER ---")
    for r in R["degenerate_rows"]:
        out.append("  d=%d L=%d %-14s %-11s lapse=%-5s declared-degenerate=%-5s "
                   "probes %d vanishing %d lattice-sum-zero %d"
                   % (r["d"], r["L"], r["rule"], r["record"], r["lapse"],
                      r["declared_degenerate"], r["probes"],
                      r["vanishing_probes"], r["lattice_sum_zero"]))
    for r in R["order_rows"]:
        out.append("  d=%d L=%d order %-16s probes %5d  nonzero %5d"
                   % (r["d"], r["L"], r["order"], r["probes"], r["nonzero"]))
    for r in R["structure_rows"]["nonconstant"]:
        out.append("  d=%d L=%d non-constant field %-12s bijection=%-5s "
                   "negative-inverts=%-5s constant=%-5s %s"
                   % (r["d"], r["L"], r["field"],
                      r["site_map_is_a_bijection"], r["negative_inverts_it"],
                      r["field_is_constant"], r["tally"]))
    out.append("")
    out.append("--- 15e. THE DUPLICATE-RULE CENSUS (gated object) ---")
    for r in R["structure_rows"]["duplicates"]:
        out.append("  d=%d L=%d declared %2d  distinct in {H,H}: %s"
                   % (r["d"], r["L"], r["declared_rules"],
                      r["distinct_in_the_HH_weight"]))
        out.append("  d=%d L=%d declared %2d  distinct in the register "
                   "sector: %s"
                   % (r["d"], r["L"], r["declared_rules"],
                      r["distinct_in_the_register_drag"]))
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
    for r in R["spanning_rows"]:
        if ("sites %3d  link space %d  full rank at %3d"
                % (r["sites"], r["link_space_dimension"],
                   r["sites_at_full_rank"])) not in txt:
            mism.append([r["d"], r["L"], r["scope"], "spanning"])
    for r in R["realisation_rows"]:
        if str(r["tally"]) not in txt:
            mism.append([r["d"], r["L"], str(r["realisation"]), "realisation"])
    for r in R["covariance_rows"]:
        if ("cells %4d  D-FULL covariant %4d  D-TOT covariant %4d"
                % (r["cells"], r["d_full_covariant"],
                   r["d_tot_covariant"])) not in txt:
            mism.append([r["d"], r["L"], "covariance"])
    for r in R["degenerate_rows"]:
        if ("probes %d vanishing %d lattice-sum-zero %d"
                % (r["probes"], r["vanishing_probes"],
                   r["lattice_sum_zero"])) not in txt:
            mism.append([r["rule"], r["lapse"], "degenerate"])
    for r in R["order_rows"]:
        if ("probes %5d  nonzero %5d" % (r["probes"], r["nonzero"])) \
                not in txt:
            mism.append([r["d"], r["L"], r["order"], "order"])
    # EQUALITY, not containment (RUNBOOK section 14 addendum, v14 #10): the
    # segments are joined in their declared order and the whole string is
    # compared against the emitted verdict.
    joined = (R["verdict"]["head"] + "<"
              + "|".join(x["text"] for x in R["verdict"]["segments"]) + ">")
    if joined != R["verdict"]["full"]:
        mism.append(["verdict", "segment-join != emitted string"])
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
    c["spanning"] = ("The realised bracket covectors span the full declared "
                     "link space at %d of %d sites, over all %d "
                     "arena-and-lapse-scope combinations."
                     % (S["spanning_sites_at_full_rank"], S["spanning_sites"],
                        S["spanning_rows"]))
    c["census"] = ("The census is cell-complete at %d cells over %d arenas and "
                   "%d lapse scopes; the commutator lands in the tangential "
                   "generator family at every one of them."
                   % (S["census_cells"], len(S["arenas"]), len(LAPSE_SCOPES)))
    c["theorem"] = ("A predictor built from the declared weight field and the "
                    "record's readout alone, carrying no commutator, "
                    "reproduces the metric-match status and the coefficient "
                    "class at %d of %d cells, with %d mispredictions."
                    % (tr["class_prediction_cells"], S["census_cells"],
                       len(tr["class_mispredictions"])
                       + len(tr["metric_match_prediction_mismatches"])))
    c["closure"] = ("Measured against the declared generator basis, the "
                    "commutator lies in the basis at %d of %d cells. Of those, "
                    "%d close with a constant non-metric coefficient -- the "
                    "rigid form -- and %d close with a coefficient equal to "
                    "the record's inverse metric."
                    % (S["basis_closing_cells"], S["census_cells"],
                       S["rigid_cells"], S["metric_match_cells"]))
    c["coefficient"] = ("The extracted coefficient is a reading of the record "
                        "metric at %d of %d cells of the metric-inserted rule, "
                        "and it is site-varying -- a structure function, not a "
                        "constant -- at %d of the %d inhomogeneous-record "
                        "cells, realised at exactly %d of the declared rules: "
                        "%s."
                        % (S["positive_control_metric_reading"],
                           S["positive_control_cells"],
                           S["inhomogeneous_site_varying_metric"],
                           S["inhomogeneous_cells"],
                           len(S["site_varying_metric_rules"]),
                           ", ".join(S["site_varying_metric_rules"])))
    c["residual"] = ("The residual against the metric-inserted generator is "
                     "nonzero at %d of %d census cells, and the coefficient "
                     "system is inconsistent -- the commutator is not in the "
                     "declared basis at all -- at %d, which are exactly the "
                     "cells of %s, %d of the %d architecture-B cells."
                     % (S["defecting_cells"], S["census_cells"],
                        S["not_extractable_cells"],
                        ", ".join(S["not_extractable_rules"]),
                        S["not_extractable_cells"],
                        S["architecture_B_cells"]))
    c["central"] = ("The two-cocycle identity holds at %d of %d cells, and the "
                    "commutator field is configuration-independent at %d of %d "
                    "ordered lapse pairs."
                    % (S["central_extension_holds"],
                       S["central_extension_cells"],
                       S["commutator_configuration_independent"],
                       S["commutator_pairs"]))
    c["dh"] = ("Over %d normal-tangential brackets the tally is %s, and the "
               "bracket lies in the constraint family at %d of them."
               % (S["dh_brackets"],
                  "; ".join("%s %d" % (k, v)
                            for k, v in sorted(S["dh_tally"].items())),
                  S["dh_in_constraint"]))
    c["dhsplit"] = ("That denominator is not balanced across dimension: %s."
                    % ", ".join("%d of it at %s" % (v, k)
                                for k, v in
                                sorted(S["dh_brackets_by_dimension"].items(),
                                       key=lambda t: -t[1])))
    c["lgate3"] = ("Of the six extents censused for the criterion, %d meet it; "
                   "d = 3, L = 3 is among them and is excluded only because "
                   "the inherited ruling gates L >= 4 uniformly."
                   % len([r for r in lg["rows"] if r["meets_r2_criterion"]]))
    c["realisation"] = ("Across all %d realisations built from the two "
                        "declared atoms, over %d classifications, the bracket "
                        "lies in the constraint family at %d of them. At the "
                        "%d realisations that transport the register along the "
                        "same declared site map it lies in the extended basis "
                        "at every one of the %d homogeneous-record "
                        "classifications, resisting at exactly %d cells."
                        % (S["realisation_count"],
                           S["realisation_classifications"],
                           S["realisation_in_constraint"],
                           len(S["absorbing_realisations"]),
                           S["realisation_homogeneous_classifications"],
                           S["curvature_supported_residue_count"]))
    c["covariance"] = ("Conjugation by full transport carries the constraint "
                       "of the record to the constraint of the transported "
                       "record at %d of %d cells; at the realisation that "
                       "transports the front but not the register it holds at "
                       "%d of %d."
                       % (S["covariance_d_full"], S["covariance_cells"],
                          S["covariance_d_tot"], S["covariance_cells"]))
    c["dd"] = ("The lattice's own translation generators close exactly: %d of "
               "%d tangential brackets are the identity, of which %d pair two "
               "distinct nonzero generators."
               % (S["dd_closing"], S["dd_total"], S["dd_informative"]))
    c["convention"] = ("Exactly %d of the %d declared convention combinations "
                       "makes the bracket's front sector equal the transported "
                       "lapse derivative everywhere: %s. The sweep evaluates "
                       "%d distinct front-sector probes."
                       % (len(S["conventions_matching_everywhere"]),
                          len(S["convention_sweep"]),
                          ", ".join(S["conventions_matching_everywhere"]),
                          S["convention_front_probes"]))
    c["defect"] = ("The defect is nonzero at %d of %d probes, its lattice sum "
                   "is nonzero at %d of them, and it vanishes at %d of the %d "
                   "homogeneous-record probes."
                   % (S["defect_probes"] - S["defect_vanishing_probes"],
                      S["defect_probes"],
                      S["defect_probes"] - S["defect_lattice_sum_zero"],
                      S["defect_vanishes_on_homogeneous"],
                      S["defect_homogeneous_probes"]))
    c["degenerate"] = ("The degenerate probe is built and measured: the zero "
                       "lapse profile gives a defect field that vanishes "
                       "identically and whose lattice sum is zero at %d of its "
                       "%d probes, while the unit constant profile vanishes at "
                       "%d of its %d."
                       % (S["degenerate_zero_lattice_sum_zero"],
                          S["degenerate_zero_probes"],
                          S["constant_profile_vanishing"],
                          S["constant_profile_probes"]))
    c["robustness"] = ("The defect is nonzero at %d of %d probes under the "
                       "other declared bracket order, and the bracket lies "
                       "outside the declared basis at %d of %d probes at the "
                       "declared non-constant tangential fields."
                       % (S["order_probes"][BRACKET_ORDERS[1]][0],
                          S["order_probes"][BRACKET_ORDERS[1]][1],
                          S["nonconstant_outside"], S["nonconstant_probes"]))
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
    c["routes"] = ("The dense route cross-checks %d of the %d census cells, "
                   "the third route -- which shares no component with the "
                   "other two, and which reaches every censused arena -- %d, "
                   "and the literal four-map composition %d, with %d "
                   "disagreements in total."
                   % (tr["dense_cells"], S["census_cells"], tr["route3_cells"],
                      tr["literal_cells"],
                      len(tr["dense_disagreements"])
                      + len(tr["route3_disagreements"])
                      + len(tr["literal_disagreements"])
                      + len(tr["dh_literal_disagreements"])
                      + len(tr["conv_literal_disagreements"])))
    c["chartgroup"] = ("The declared chart group closes at %d of %d censused "
                       "arenas."
                       % (len([g for g in ctl["chart_group"] if g["closes"]]),
                          len(ctl["chart_group"])))
    c["lapse"] = ("Enlarging the lapse family to its lattice translates moves "
                  "the residual MAGNITUDE at %d of the %d (arena, rule, "
                  "record) cells compared across the two scopes -- always "
                  "upward, at %d of %d -- and moves no cell's closure status "
                  "and no cell's coefficient class (%d moved)."
                  % (len(S["lapse_coordinate_moves"]), S["lapse_comparisons"],
                     S["lapse_moves_upward"],
                     len(S["lapse_coordinate_moves"]),
                     len(S["lapse_coordinate_moves_coefficient"])))
    c["duplicates"] = ("Of the %d rules declared at d = 2, %d are distinct as "
                       "weight fields in the first bracket and %d in the "
                       "register sector."
                       % (S["distinct_rules"]["d2"]["declared"],
                          S["distinct_rules"]["d2"]
                          ["distinct_in_the_HH_weight"],
                          S["distinct_rules"]["d2"]
                          ["distinct_in_the_register_drag"]))
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
    ("13(5) two independent routes", ["G-CENSUS-THREE-ROUTES",
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
     ["G-FORCED-CLAUSES-DISCLOSED", "G-STRUCTURE-THEOREM"]),
    ("219 comparators can disagree", ["G-VERDICT-STRING-EQUALITY",
                                      "G-CENSUS-THREE-ROUTES",
                                      "G-STRUCTURE-THEOREM"]),
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
     ["G-CENSUS-THREE-ROUTES", "G-DH-TWO-ROUTES", "G-LSWEEP-COMPLETE",
      "G-REALISATION-CENSUS", "G-COVARIANCE-THEOREM"]),
    ("the L gate excludes the failing extent by gate",
     ["G-L-GATE", "G-L-GATE-REASON"]),
    ("the defect is a measured object", ["G-DEFECT-MEASURED",
                                         "G-BOUNDARY-TERM-STATUS"]),
    ("internal consistency of the emitted receipt",
     ["G-INTERNAL-CONSISTENCY"]),
    ("the falsifier census ships with an honest denominator",
     ["G-NEVER-FALSIFIED-CENSUS"]),
    ("34 waiver claims are gate claims",
     ["G-WAIVER-CLAIMS-ARE-GATE-CLAIMS", "G-NEVER-FALSIFIED-CENSUS"]),
    ("34 verbatim-text anchors: context windows bound to consumer gates",
     ["T-R2-HANDOFF", "T-R2-GATES-L", "T-R2-PROFILES", "T-R2-INHERITED",
      "G-L-GATE-INHERITED-FACTS"]),
    ("46 no unanchored runtime inputs",
     ["G-NO-UNANCHORED-RUNTIME-INPUT", "G-L-GATE-INHERITED-FACTS"]),
    ("10 the object the gates check is the object that ships",
     ["G-RENDER-FROM-GATED-OBJECT", "G-PAYLOAD-SEALED"]),
    ("the load-bearing hypothesis is measured, not assumed",
     ["G-SPANNING-HYPOTHESIS"]),
    ("a rigid outcome that can win", ["G-RIGID-BRANCH-REACHABLE"]),
    ("the realisation coordinate is censused, not chosen",
     ["G-REALISATION-CENSUS", "G-COVARIANCE-THEOREM"]),
    ("honest denominators: distinct probes, never a multiplied sample",
     ["G-CONVENTION-FRONT-INDEPENDENT", "G-DD-RELATION-CONTENT",
      "G-DUPLICATE-RULES-DISCLOSED"]),
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
     "what_it_breaks": "blinds the unit to an inherited fact read by path out "
                       "of the R2 terminal receipt",
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
    # ---- THE TEN INJECTION CLASSES, EACH WITH ITS OWN KILLER ------------
    {"name": "defect-zero-all-but-one",
     "what_it_breaks": "zeroes the defect field at every probe but the first "
                       "-- the class that inverted all four defect findings "
                       "while every defect gate stayed green",
     "expected_gate": "G-DEFECT-MEASURED"},
    {"name": "defect-row-drop",
     "what_it_breaks": "drops one (rule, record) defect row, so the defect "
                       "census under-reports its own denominator",
     "expected_gate": "G-DEFECT-MEASURED"},
    {"name": "dh-row-drop",
     "what_it_breaks": "drops one (rule, record, realisation) {D,H} row",
     "expected_gate": "G-BRACKET-TABLES-CELL-COMPLETE"},
    {"name": "dd-row-drop",
     "what_it_breaks": "drops one (record, realisation) {D,D} row",
     "expected_gate": "G-BRACKET-TABLES-CELL-COMPLETE"},
    {"name": "gap-matrix-corrupt",
     "what_it_breaks": "zeroes the diagonal-link column inside gap_matrix -- "
                       "the component the support-restricted and dense routes "
                       "SHARE, which the third route does not touch",
     "expected_gate": "G-CENSUS-THREE-ROUTES"},
    {"name": "class-predictor-blind",
     "what_it_breaks": "blinds the analytic class predictor to a diagonal "
                       "column, so the independent comparator would stop "
                       "being able to disagree",
     "expected_gate": "G-STRUCTURE-THEOREM"},
    {"name": "coefficient-class-flip",
     "what_it_breaks": "flips the site-varying coefficient classes to "
                       "constant ones, erasing the separation the typing gate "
                       "states (the R1 I4 class)",
     "expected_gate": "G-COEFFICIENT-TYPING"},
    {"name": "not-extractable-attribution",
     "what_it_breaks": "attributes non-extractability to the architecture-B "
                       "rule CLASS instead of to the measured set of rules "
                       "carrying a diagonal-link column",
     "expected_gate": "G-COEFFICIENT-EXTRACTION"},
    {"name": "arch-a-diagonal-weight",
     "what_it_breaks": "gives an architecture-A rule a diagonal-link weight "
                       "component at one site, so the non-extractable set "
                       "would stop being what the mechanism says it is",
     "expected_gate": "G-COEFFICIENT-EXTRACTION"},
    {"name": "payload-post-gate-corrupt",
     "what_it_breaks": "corrupts measured receipt cells AFTER every "
                       "measurement gate, at write time",
     "expected_gate": "G-PAYLOAD-SEALED"},
    {"name": "trajectory-post-gate-truncate",
     "what_it_breaks": "truncates the L-sweep trajectory to two rows after "
                       "the L-sweep gates have run",
     "expected_gate": "G-PAYLOAD-SEALED"},
    {"name": "recovery-denominator-overwrite",
     "what_it_breaks": "overwrites the machinery-recovery control's "
                       "denominators after the recovery gates",
     "expected_gate": "G-PAYLOAD-SEALED"},
    {"name": "controls-post-gate-truncate",
     "what_it_breaks": "truncates the control tables after the control gates",
     "expected_gate": "G-PAYLOAD-SEALED"},
    # ---- THE NEW MEASUREMENTS' OWN FALSIFIERS ---------------------------
    {"name": "route3-probe-blind",
     "what_it_breaks": "drops a declared link direction from route 3's probe "
                       "coverage, so the third route would stop being able to "
                       "see a corruption on that link's column",
     "expected_gate": "G-CENSUS-THREE-ROUTES"},
    {"name": "metric-comparator-blind",
     "what_it_breaks": "types the inversion-free metric comparison's product "
                       "as the identity, so the third route could not "
                       "disagree",
     "expected_gate": "G-METRIC-COMPARATOR-INDEPENDENT"},
    {"name": "cache-wrong-value",
     "what_it_breaks": "returns a WRONG fresh value from the weight "
                       "recomputation, so the cache exercise dies on its "
                       "substantive clause (disagreements) rather than on its "
                       "coverage clause",
     "expected_gate": "G-CACHE-EXERCISE"},
    {"name": "spanning-blind",
     "what_it_breaks": "reports a rank below the link-space dimension, so "
                       "hypothesis (S) would fail",
     "expected_gate": "G-SPANNING-HYPOTHESIS"},
    {"name": "realisation-blind",
     "what_it_breaks": "types the register-transporting realisation's "
                       "classification as IN-CONSTRAINT",
     "expected_gate": "G-REALISATION-CENSUS"},
    {"name": "covariance-theorem-blind",
     "what_it_breaks": "types the conjugation identity's two sides equal, so "
                       "the covariance theorem could not fail",
     "expected_gate": "G-COVARIANCE-THEOREM"},
    {"name": "cocycle-blind",
     "what_it_breaks": "drops the two-cocycle from the central-extension "
                       "identity",
     "expected_gate": "G-CENTRAL-EXTENSION"},
    {"name": "degenerate-probe-typed",
     "what_it_breaks": "reports the degenerate probe's vanishing counts as "
                       "zero -- the class in which a control is asserted "
                       "rather than computed",
     "expected_gate": "G-BOUNDARY-TERM-STATUS"},
    {"name": "rigid-branch-unreachable",
     "what_it_breaks": "makes the verdict machinery unable to return the "
                       "pin's RIGID outcome",
     "expected_gate": "G-RIGID-BRANCH-REACHABLE"},
    {"name": "front-independence-break",
     "what_it_breaks": "breaks the front sector's measured record- and "
                       "rule-independence, which is what licenses the "
                       "convention sweep's multiplicity",
     "expected_gate": "G-CONVENTION-FRONT-INDEPENDENT"},
    {"name": "criterion-blind",
     "what_it_breaks": "makes this unit's implementation of the inherited "
                       "locality criterion agree with itself on both control "
                       "graphs",
     "expected_gate": "G-L-GATE-INHERITED-FACTS"},
    {"name": "lgate-fraction-drop",
     "what_it_breaks": "drops one recomputed overlap fraction",
     "expected_gate": "G-L-GATE-INHERITED-FACTS"},
    {"name": "text-anchor-skip",
     "what_it_breaks": "drops the last declared verbatim-text anchor row",
     "expected_gate": "G-ANCHOR-COUNT"},
    {"name": "falsifier-map-stale",
     "what_it_breaks": "leaves the falsifier map stale against the census "
                       "printed beside it",
     "expected_gate": "G-NEVER-FALSIFIED-CENSUS"},
    {"name": "waiver-unbacked",
     "what_it_breaks": "injects a waiver claim with nothing behind it",
     "expected_gate": "G-WAIVER-CLAIMS-ARE-GATE-CLAIMS"},
    {"name": "nonconstant-field-degenerate",
     "what_it_breaks": "replaces a declared non-constant tangential field "
                       "with a constant one, so the robustness probe would "
                       "test nothing new",
     "expected_gate": "G-DEFECT-ROBUSTNESS"},
    {"name": "dd-content-inflate",
     "what_it_breaks": "counts every {D,D} bracket as informative, hiding "
                       "that most pair a generator with itself or with zero",
     "expected_gate": "G-DD-RELATION-CONTENT"},
    {"name": "duplicate-rules-hidden",
     "what_it_breaks": "reports every declared rule as distinct, hiding the "
                       "exact duplicates",
     "expected_gate": "G-DUPLICATE-RULES-DISCLOSED"},
    {"name": "runtime-read-undeclared",
     "what_it_breaks": "adds an undeclared runtime read to the declared list",
     "expected_gate": "G-NO-UNANCHORED-RUNTIME-INPUT"},
    {"name": "verdict-typed-covariance",
     "what_it_breaks": "types the COVARIANCE segment to claim the record "
                       "transports",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-typed-correspondence",
     "what_it_breaks": "types the CORRESPONDENCE segment to claim the HDA is "
                       "reproduced",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
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

# EVERY REMAINING ANCHOR ROW GETS ITS OWN DECLARED FALSIFIER.  The mechanisms
# already exist inside verify_anchors / verify_path_anchors / verify_text_
# anchors; these rows declare them, so the never-falsified census stops
# resting on a same-mechanism argument (RUNBOOK section 14 addendum, v14 #34).
MUTANTS += [{"name": "anchor-hash-" + row[0],
             "what_it_breaks": "corrupts the %s file-byte anchor" % row[0],
             "expected_gate": row[0]}
            for row in ANCHOR_ROWS
            if row[0] not in [m["expected_gate"] for m in MUTANTS]]
MUTANTS += [{"name": "path-value-" + row[0],
             "what_it_breaks": "drifts the %s (path, value) anchor's path"
                               % row[0],
             "expected_gate": row[0]}
            for row in PATH_ANCHOR_ROWS
            if row[0] not in [m["expected_gate"] for m in MUTANTS]]
MUTANTS += [{"name": "text-anchor-" + row[0],
             "what_it_breaks": "drifts the %s verbatim-text anchor's context "
                               "window" % row[0],
             "expected_gate": row[0]}
            for row in TEXT_ANCHOR_ROWS
            if row[0] not in [m["expected_gate"] for m in MUTANTS]]
MUTANTS.sort(key=lambda m: m["name"])


# ----------------------------------------------------------------------------
# 17.  DELIVERY
# ----------------------------------------------------------------------------

def build_falsifier_map():
    """The gate -> declared-mutants map, REBUILT from the mutant table.  It is
    rebuilt in the final pass so it can never go stale against the census
    printed beside it."""
    fmap = {}
    for m in MUTANTS:
        fmap.setdefault(m["expected_gate"], []).append(m["name"])
    return dict((k, sorted(v)) for k, v in sorted(fmap.items()))


def path_rows_with_a_falsifier(fmap):
    return sorted(k for k in fmap if k.startswith("P-"))


def byte_rows_with_a_falsifier(fmap):
    return sorted(k for k in fmap if k.startswith("A-"))


def text_rows_with_a_falsifier(fmap):
    return sorted(k for k in fmap if k.startswith("T-"))


def waiver_for(name, fmap=None):
    """The forcing statement for a gate with no declared falsifier.  Every
    number in it is COMPUTED from the falsifier map (#24 at the surface #34
    was engraved for: the previous text carried a typed count, and it was
    wrong)."""
    fmap = build_falsifier_map() if fmap is None else fmap
    if name == "G-DEFERRED-GATES-EVALUATED":
        return ("WAIVED, GENUINE: a bookkeeping gate over the write-time gate "
                "names and the rendered gate count.  Its falsifier would be a "
                "gate that never ran, which is exactly what the gate itself "
                "reports; there is no state in which it can fail while the "
                "run continues.")
    if name.startswith("A-"):
        return ("SAME-MECHANISM: a file-byte anchor row.  %d of the %d "
                "file-byte rows carry declared byte-corruption falsifiers "
                "(%s), each of which dies on ITS OWN row."
                % (len(byte_rows_with_a_falsifier(fmap)), len(ANCHOR_ROWS),
                   ",".join(byte_rows_with_a_falsifier(fmap))))
    if name.startswith("P-"):
        return ("SAME-MECHANISM: a (path, value) anchor row.  %d of the %d "
                "path-value rows carry declared path-drift or path-value "
                "falsifiers, each of which dies on ITS OWN row."
                % (len(path_rows_with_a_falsifier(fmap)),
                   len(PATH_ANCHOR_ROWS)))
    if name.startswith("T-"):
        return ("SAME-MECHANISM: a verbatim-text anchor row.  %d of the %d "
                "text rows carry declared window-drift falsifiers, each of "
                "which dies on ITS OWN row."
                % (len(text_rows_with_a_falsifier(fmap)),
                   len(TEXT_ANCHOR_ROWS)))
    return "NAMED, no waiver claimed"


def waiver_audit(fmap, nf):
    """Every waiver is itself a claim; here it is checked.  Only the gates the
    census actually waives are audited -- and a waiver may name only mutants
    this instrument declares and only gates a declared mutant really kills."""
    names = set(m["name"] for m in MUTANTS)
    killed = set(m["expected_gate"] for m in MUTANTS)
    registered = set(g["name"] for g in GATES) | set(DEFERRED_GATES)
    bad = []
    for name in nf:
        if name in fmap:
            bad.append([name, "waived, yet a declared mutant kills it"])
        text = waiver_for(name, fmap)
        if text == "NAMED, no waiver claimed":
            bad.append([name, "no waiver text for a never-falsified gate"])
            continue
        for tok in text.replace(",", " ").replace("(", " ") \
                       .replace(")", " ").replace(".", " ").split():
            if tok in registered and tok not in killed:
                bad.append([name, "waiver names %s, which no mutant kills"
                            % tok])
            if tok in names and tok not in names:
                bad.append([name, "waiver names an undeclared mutant"])
    for k in fmap:
        if k in nf:
            bad.append([k, "a falsified gate appears in the waiver census"])
    if MUTANT == "waiver-unbacked":
        bad.append(["INJECTED", "an unbacked waiver claim"])
    return bad


def falsifier_census(fnames, fmap, nf):
    stored = dict(fmap)
    if MUTANT == "falsifier-map-stale":
        # the R6a disease: a map assembled early and never rebuilt, shipped
        # beside a count that has moved on
        for k in list(stored)[-2:]:
            stored.pop(k, None)
    return {
        "gates": len(fnames),
        "gates_with_a_declared_falsifier": len([n for n in fnames
                                                if n in fmap]),
        "never_falsified": nf,
        "never_falsified_count": len(nf),
        "denominator": "%d of %d gates" % (len(nf), len(fnames)),
        "falsifier_map": dict((k, v) for k, v in stored.items()
                              if k in fnames),
        "waivers": dict((k, waiver_for(k, fmap)) for k in nf),
        "rule": "a gate with no declared falsifier is NAMED here with its "
                "forcing stated, from delivery one; every waiver's own "
                "counts are computed from the falsifier map and audited by "
                "G-WAIVER-CLAIMS-ARE-GATE-CLAIMS",
    }


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
        "gates": len(GATES) + gates_still_to_come(),
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
    #
    # THE #34 STANDARD: a never-falsified waiver naming a mutant or a forcing
    # is itself a claim requiring verification.  So: the map is REBUILT in the
    # final pass (a stale map is a false census); every waiver text's counts
    # are COMPUTED from the map rather than typed; every waiver naming a
    # mutant is checked to name a mutant that really dies at that gate; and a
    # waiver for a gate that is in fact falsified is a dead entry and is
    # forbidden.
    fmap = build_falsifier_map()
    fnames = [g["name"] for g in GATES] + [n for n in DEFERRED_GATES
                                           if n not in [g["name"]
                                                        for g in GATES]]
    nf = [n for n in fnames if n not in fmap]
    if MUTANT == "falsifier-census-hide":
        nf = []
    R["falsifier_census"] = falsifier_census(fnames, fmap, nf)
    gate("G-NEVER-FALSIFIED-CENSUS",
         "the never-falsified census ships IN the receipt with an honest "
         "denominator, and the census is CONSISTENT WITH ITSELF: the "
         "falsifier map is REBUILT in this final pass (a map assembled "
         "earlier and never rebuilt is stale, and a stale map disagrees with "
         "the count printed beside it), its size equals the number of gates "
         "with a declared falsifier, every never-falsified gate carries a "
         "waiver, and NO waiver exists for a gate that is in fact falsified",
         (R["falsifier_census"]["never_falsified_count"]
          + R["falsifier_census"]["gates_with_a_declared_falsifier"]
          == R["falsifier_census"]["gates"])
         and all(n in R["falsifier_census"]["waivers"] for n in nf)
         and len(R["falsifier_census"]["falsifier_map"])
         == R["falsifier_census"]["gates_with_a_declared_falsifier"]
         and sorted(R["falsifier_census"]["waivers"]) == sorted(nf),
         {"census": R["falsifier_census"]["denominator"],
          "named": nf,
          "map_size": len(R["falsifier_census"]["falsifier_map"]),
          "with_a_falsifier":
              R["falsifier_census"]["gates_with_a_declared_falsifier"]})
    bad_waiver = waiver_audit(fmap, nf)
    gate("G-WAIVER-CLAIMS-ARE-GATE-CLAIMS",
         "THE #34 STANDARD, ENFORCED: every waiver that names a mutant names "
         "a mutant this instrument declares AND whose declared death gate is "
         "the waived gate itself or the gate the waiver says it is; every "
         "waiver that states a forcing names the gate that machine-checks it; "
         "and every count inside a waiver text is COMPUTED from the falsifier "
         "map, never typed",
         len(bad_waiver) == 0,
         {"violations": bad_waiver[:6],
          "waived_gates": sorted(R["falsifier_census"]["waivers"])})

    claimed = R["paper_claims"]["rendered"]["instrument"]
    ngates = len(GATES) + gates_still_to_come()
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
         all(d in reg for d in DEFERRED_GATES
             if d not in ("G-DEFERRED-GATES-EVALUATED", "G-PAYLOAD-SEALED"))
         and len(GATES) + gates_still_to_come() == R["totals"]["gates"],
         {"deferred": list(DEFERRED_GATES), "registered": len(reg),
          "claimed_total": R["totals"]["gates"]})

    fnames = [g["name"] for g in GATES]
    nf = [n for n in fnames if n not in fmap]
    if MUTANT == "falsifier-census-hide":
        nf = []
    R["falsifier_census"] = falsifier_census(fnames, fmap, nf)
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
    fnames = [g["name"] for g in GATES]
    nf = [n for n in fnames if n not in fmap]
    if MUTANT == "falsifier-census-hide":
        nf = []
    R["falsifier_census"] = falsifier_census(fnames, fmap, nf)
    R["compliance"] = compliance_sweep(R)
    R["payload_seal"] = payload_seal(R)
    return R


def build_everything():
    parts = run()
    R, res, S = run_part2(*parts)
    return finalise(R)


def write_time_gates(R):
    """The gates that can only run once the payload is final -- evaluated on
    EVERY run, mutant or plain, and always BEFORE any artifact is written."""
    if MUTANT == "payload-post-gate-corrupt":
        R["census_rows"][0]["nonzero_pairs"] = 4242
        R["defect_rows"][0]["lattice_sum_zero"] = 11
        R["controls"]["chart_group"][0]["order"] = 7
    if MUTANT == "trajectory-post-gate-truncate":
        R["summary"]["trajectory"] = R["summary"]["trajectory"][:2]
    if MUTANT == "recovery-denominator-overwrite":
        R["recovery"]["closure_cells_compared"] = 99999
        R["recovery"]["sector_cells_compared"] = 88888
    if MUTANT == "controls-post-gate-truncate":
        R["controls"]["chart_group"] = R["controls"]["chart_group"][:1]
        R["controls"]["positive"] = R["controls"]["positive"][:1]
        R["controls"]["negative"] = R["controls"]["negative"][:1]
    # THE PAYLOAD SEAL, re-verified after every gate and BEFORE any write
    # (RUNBOOK section 13 addendum, v14 #10: the object the gates check must
    # be the object the receipt and paper render from).  Three write-time
    # checks run here: the seal, a fresh render check, and a fresh rebuild of
    # the verdict from the payload as it now stands.
    seal = R.pop("payload_seal")
    now = payload_seal(R)
    gate("G-PAYLOAD-SEALED",
         "the payload written to disk is BYTE-FOR-BYTE the payload the gates "
         "checked: a digest of the whole gated subtree is taken after the "
         "last measurement gate and re-verified here, immediately before the "
         "write, together with a fresh render check and a fresh independent "
         "rebuild of the verdict.  A post-gate mutation of any measured row "
         "cannot ship",
         (seal == now
          and len(render_check(R)) == 0
          and reconstruct_verdict_from_receipt(
              json.loads(json.dumps(jsonable(R)))) == R["verdict"]["full"]),
         {"seal_at_gate_time": seal, "seal_at_write_time": now,
          "render_mismatches": render_check(R)[:4]})
    R["payload_seal"] = seal
    R["gates"] = GATES
    R["totals"]["gates"] = len(GATES)
    fmap = build_falsifier_map()
    fnames = [g["name"] for g in GATES]
    nf = [n for n in fnames if n not in fmap]
    R["falsifier_census"] = falsifier_census(fnames, fmap, nf)
    R["compliance"] = compliance_sweep(R)
    return R


def deliver():
    R = write_time_gates(build_everything())
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
        R = write_time_gates(build_everything())
        render_text(R)
        sys.stderr.write("MUTANT %s SURVIVED -- no gate fired\n" % MUTANT)
        return 3
    except GateFailure as exc:
        sys.stderr.write(str(exc) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
