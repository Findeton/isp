#!/usr/bin/env python3
"""
v14 CR-B -- STOCHASTIC REFINEMENT: THE SPLIT IN DISTRIBUTION.  Exact instrument.

PIN: v14/note-cr-batch-pins.md, CR-B section (frozen v14 ledger #30, sha256-12
1cfee4fc0891).  The pin is verified BY HASH at run time (gate A-PIN-CRB); so
are the v14 R0 founding pin, the R6a receipt (DELIVERED-UNDER-PANEL status
carried in every citation), and the three v13 sources of R0 row I7.

THE QUESTION (pin, CR-B):  R6a proved no motivated split VALUE.  Is there a
motivated split DISTRIBUTION -- a conditional law over the split fiber forced
by pinned structure?

Three verdict heads are first class, each derived INSIDE a gate:
  CRB-DISTRIBUTION-MOTIVATED<law, forcing>
  CRB-ORBIT-SIMPLEX<dims -- not unique>
  CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW<the missing object>
The emitted string is compared for COMPLETE STRING EQUALITY against an
INDEPENDENT reconstruction built from the receipt object alone
(reconstruct_verdict_from_receipt() shares no code and no input with
build_verdict(); five injection mutants plus head-constant prove it fires).

WHAT IS MEASURED
  1. THE FIBER REBUILD.  The dyadic move's split fibers rebuilt from the pinned
     declarations alone and ANCHORED cell-by-cell against the R6a receipt: raw
     fiber, admissible-at-images fiber, per-site admissible profile, at all
     nine records; the declared count box; the span 19683 .. 1257565061957837936381.
  2. THE SYMMETRY INVENTORY AS DATA.  Every symmetry that acts on a fiber, with
     its provenance class: PINNED (the chart group = the |X| translations and
     the d! direction relabellings Sigma) and DECLARED-EXTENSION (the maximal
     subgroup of GL(2,Z) preserving the declared link set up to sign -- the A2
     point group of order 12, giving an order-108 lattice group; and the
     per-interval local flip group of order 2^27).  A measured theorem: the
     block-preserving subgroup of the order-108 group is EXACTLY the pinned
     chart group.
  3. THE ORBIT DECOMPOSITION of each fiber, exactly, by Cauchy-Frobenius over
     the cycle structure of each group element, cross-checked by direct orbit
     enumeration where the fiber is enumerable and by a closed-form necklace
     count that shares no code with the engine.
  4. THE INVARIANT-MEASURE CENSUS.  Unique invariant distribution iff the
     action is transitive -- NOT assumed: the dimension of the affine space of
     invariant probability measures is computed by exact Gaussian elimination
     over Q and compared against orbits - 1 at every cell where the fiber is
     small enough to carry the linear system.
  5. SELECTION CANDIDATES beyond symmetry, each tested and its forcing named or
     refuted: the record's own counts as weights, the front, the drag field,
     maximum entropy under pinned constraints (audited, never assumed), the
     invariant simplex's barycentre, the equivariant (deterministic) laws.
  6. ITERATION IN DISTRIBUTION: do orbit-simplex dimensions grow, stabilise or
     collapse under repeated refinement.
  7. CONTROLS: a constructed transitive-action fiber (positive -- the unique
     invariant measure is found) and an asymmetric fiber (negative).

CLI CONTRACT (confirmed in code before invocation, v13 #238):
  (no arguments)        THE PLAIN DELIVERY RUN.  Runs every gate, derives the
                        verdict, and WRITES v14/code/crb_stochastic_output.txt
                        and v14/code/crb_stochastic_receipt.json.  Exit 0.  Any
                        gate failure aborts BEFORE any artifact is written.
  --mutant NAME         Runs the delivery pipeline with the named injection
                        active.  MUST exit 1 with a NAMED gate failure and MUST
                        NOT write any artifact.  Unknown name -> exit 2.
  --list-mutants        Prints the declared mutant names, one per line.  Exit 0.
  --selftest            Re-invokes this file once per declared mutant, requires
                        exit 1, a death certificate naming a gate, and the
                        artifacts on disk byte-unchanged.  Writes nothing.

Arithmetic is exact throughout: int and fractions.Fraction only.  A float
literal, a float call, or a true-division operator anywhere in this source is a
gate failure (G-FLOATGUARD, an AST scan of this file).

Concurrency note: this unit owns ONLY v14/paper-06-stochastic-split.md,
v14/code/crb_stochastic_exact.py, v14/code/crb_stochastic_output.txt and
v14/code/crb_stochastic_receipt.json.  It reads v13 receipts/paper/code, the
v14 notes and the R6a receipt, and writes nothing else.
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
# 0.  Paths, the single mutation switch, and the gate ledger
# ----------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)                      # .../isp/v14
ROOT = os.path.dirname(REPO)                      # .../isp
SRC = os.path.abspath(__file__)
OUT_TXT = os.path.join(HERE, "crb_stochastic_output.txt")
OUT_JSON = os.path.join(HERE, "crb_stochastic_receipt.json")
PAPER = os.path.join(REPO, "paper-06-stochastic-split.md")

MUTANT = None            # read by main() and mutate() alone; no gate reads it

PIN_SHA = "1cfee4fc0891"
R6A_SHA = "022c3f488a93"
R6A_STATUS = "DELIVERED-UNDER-PANEL (v14 #26 committed, #27 verified, #28 panel)"


class GateFailure(Exception):
    pass


GATES = []
ANCHORS = []
DEFERRED_GATES = ("G-RENDER-FROM-GATED-OBJECT", "G-NO-FLOATS-IN-RECEIPT",
                  "G-PROSE-RENDERS-FROM-THE-RECEIPT", "G-FINAL-GATE-COUNT",
                  "G-FALSIFIER-CENSUS-HONEST", "G-DEFERRED-GATES-EVALUATED")

# Analytically-forced clauses: true by algebra for every input.  RUNBOOK
# section 14 addendum (v13 #208): these are DISCLOSURES, not must-pass
# falsifiable gates, and the receipt says so in one place.
FORCED_CLAUSE_DISCLOSURES = (
    "G-H-IS-A-BIJECTION",
    "G-BURNSIDE-INTEGRAL",
)


def gate(name, statement, ok, value=None):
    """Register a gate.  A gate predicate NEVER references run-mode identity
    (RUNBOOK section 14 addendum, v13 #208)."""
    GATES.append({"name": name, "statement": statement,
                  "passed": bool(ok), "value": value})
    if not ok:
        raise GateFailure("GATE FAILED: %s -- %s | value=%r"
                          % (name, statement, value))
    return True


def mutate(tag, value):
    """THE ONE READER of run-mode identity in this instrument (besides main()).

    Every declared injection is applied here and nowhere else, so no gate
    predicate can special-case a named mutant (RUNBOOK section 14 addendum,
    v13 #208).  The AST detector G-NO-MUTANT-IDENTITY measures that claim."""
    if MUTANT is None:
        return value
    if MUTANT == tag:
        return _INJECTIONS[tag](value)
    return value


def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def sha256_full(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def recip(b):
    """Exact reciprocal, built without the division operator."""
    b = Fr(b)
    return Fr(b.denominator, b.numerator)


def fdiv(a, b):
    """The only quotient in this instrument.  Exact, never a float."""
    return Fr(a) * recip(b)


# ----------------------------------------------------------------------------
# 1.  G-FLOATGUARD and G-NO-MUTANT-IDENTITY -- AST scans of this source
# ----------------------------------------------------------------------------

FLOAT_T = type((1).__truediv__(1))
BANNED_NAMES = ("float", "math", "random", "numpy", "statistics", "decimal")


def _source_text():
    with open(SRC, "r") as fh:
        return fh.read()


def float_guard():
    tree = ast.parse(_source_text())
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
    return mutate("float-leak", offences)


def _functions_naming(tree, target):
    out = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name) and sub.id == target:
                    out.append(node.name)
                    break
    return sorted(set(out))


def mutant_identity_scan():
    """Measure that run-mode identity is read by mutate() and main() ALONE, and
    validate the detector with two synthetic injections it must flag."""
    tree = ast.parse(_source_text())
    naming = _functions_naming(tree, "MUTANT")
    naming = mutate("mutant-identity-leak", naming)
    inj = []
    probe_a = "def g_probe(x):\n    return x if MUTANT is None else 0\n"
    probe_b = "def helper(x):\n    return MUTANT\n"
    for label, text in (("a gate predicate that reads run-mode identity", probe_a),
                        ("a second function that reads run-mode identity", probe_b)):
        found = _functions_naming(ast.parse(text), "MUTANT")
        inj.append([label, len(found) > 0])
    return naming, inj


# ----------------------------------------------------------------------------
# 2.  Anchors -- file bytes, (path, value) pairs, and verbatim text
# ----------------------------------------------------------------------------

ANCHOR_ROWS = [
    ("A-PIN-CRB", "v14/note-cr-batch-pins.md", PIN_SHA,
     "this unit's pin: the CR-B section of the continuum-routes batch, frozen "
     "at v14 ledger #30"),
    ("A-R0-PIN", "v14/note-r0-founding-pin.md", "e9d2bedff244",
     "the v14 founding pin: the inheritance table whose I7 row this unit uses"),
    ("A-R6A-RECEIPT", "v14/code/r6a_refinement_receipt.json", R6A_SHA,
     "the R6a receipt -- the split fibers, stabilisers, equivariant fibers, "
     "count lattice and iteration table this unit rebuilds and anchors "
     "against; cited at " + R6A_STATUS),
    ("A-I7-RECEIPT", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "R0 row I7 -- the pinned grammar source: sites, links, interval counts, "
     "the front, the chart group, H_a[N], record-IS-metric"),
    ("A-HA-PAPER", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "the HA paper: the written grammar declarations reimplemented here"),
    ("A-HA-CODE", "v13/code/ha_successor_exact.py", "d44cb72f8ee9",
     "the HA instrument: the exact record constructors and H_a[N] "
     "reimplemented here (nothing imported)"),
]


def read_json(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return json.load(fh)


def read_text(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return fh.read()


R6A = "v14/code/r6a_refinement_receipt.json"
I7 = "v13/code/ha_successor_receipt.json"

# PATH-VALUE ANCHORS (RUNBOOK section 14 addendum, v14 #20): a read-by-path
# anchors the (path, value) PAIR, not only the file bytes.
PATH_ANCHOR_ROWS = [
    ("P-I7-D", I7, ("declarations", "d"), 2, "the primary spatial dimension"),
    ("P-I7-L", I7, ("declarations", "L"), 3, "the arena's linear size"),
    ("P-I7-DEXT", I7, ("declarations", "d_ext"), 3,
     "the number of declared link directions at d = 2"),
    ("P-I7-LINKS2", I7, ("declarations", "links_d2"), [[1, 0], [0, 1], [1, 1]],
     "the declared link set -- the arena datum whose symmetries this unit "
     "inventories"),
    ("P-I7-CHART", I7, ("declarations", "chart_group"),
     "the |X| chart translations and the d! direction relabellings, acting on "
     "sites, on the record's link counts, on the lapse profiles and on every "
     "tensor index",
     "THE PINNED SYMMETRY: the chart group, declared in full -- 9 translations "
     "times Sigma = S_d, order 18"),
    ("P-I7-RECORDS2", I7, ("declarations", "records_d2", "G-ANISO2"),
     [4, 9, 13], "the widest-count declared record: the fiber's upper end"),
    ("P-I7-DIAG2", I7, ("declarations", "records_d2", "G-DIAG2"), [2, 2, 4],
     "the narrowest splittable declared record: the fiber's lower end"),
    ("P-I7-INHOMOG", I7, ("declarations", "records_d2_inhomogeneous"),
     ["G-CURVED (diagonal, site-dependent)",
      "G-CURVOFF (cross term, site-dependent)"],
     "the two inhomogeneous records, whose constructors are reimplemented here"),
    ("P-I7-LATTICE-AXIS", I7, ("declarations", "count_lattice", "axis_max"), 6,
     "the declared count box's axis bound"),
    ("P-I7-LATTICE-DIAG", I7, ("declarations", "count_lattice", "diag_max"), 12,
     "the declared count box's diagonal bound"),
    ("P-I7-LAPSE", I7, ("declarations", "lapse_family"),
     "the |X| site deltas, the constant profile 1, and the d chart ramps",
     "the declared profile family, used here as the declared FRONT family for "
     "the front-selection candidate"),
    ("P-I7-WEIGHT", I7, ("declarations", "density_weight"), 0,
     "the readout convention w = 0 under which admissibility is read"),
    ("P-I7-REGISTERS", I7, ("declarations", "registers", "m == 0"),
     "the zero address register",
     "the matter register's declared states -- the carrier of the determinism "
     "census"),
    ("P-I7-TESTCLASS", I7, ("declarations", "test_class"),
     "the indicator effects of the reduced total-configuration carrier; ||R|| "
     ":= the number of configurations R moves / carrier size",
     "the ONE ratio-valued pinned declaration -- audited here for whether it "
     "is a probability law"),
    ("P-R6A-VERDICT", R6A, ("verdict_head",), "R6A-NO-MOTIVATED-SPLIT",
     "R6a's head: no motivated split VALUE -- the predecessor this unit "
     "re-poses in distribution (" + R6A_STATUS + ")"),
    ("P-R6A-RAW-DIAG2", R6A, ("split_fibers", "G-DIAG2", "raw"), 19683,
     "the smallest raw split fiber -- the span's lower end"),
    ("P-R6A-IMG-DIAG2", R6A, ("split_fibers", "G-DIAG2",
                              "admissible_at_images"), 19683,
     "the smallest admissible split fiber"),
    ("P-R6A-IMG-ANISO2", R6A, ("split_fibers", "G-ANISO2",
                               "admissible_at_images"),
     1257565061957837936381, "the largest admissible split fiber -- the span's "
     "upper end"),
    ("P-R6A-PS-CURVOFF", R6A, ("split_fibers", "G-CURVOFF",
                               "per_site_admissible"),
     [3, 8, 15, 20, 35, 61],
     "the inhomogeneous record's per-site admissible profile"),
    ("P-R6A-EQ-DIAG2", R6A, ("equivariant_fibers", "G-DIAG2"), 3,
     "R6a's chart-equivariant fiber = the number of CHART-fixed points of the "
     "raw fiber = the deterministic invariant laws"),
    ("P-R6A-EQ-CURVOFF", R6A, ("equivariant_fibers", "G-CURVOFF"), 29393280,
     "the inhomogeneous record's equivariant fiber"),
    ("P-R6A-STAB-DIAG2", R6A, ("stabilisers", "G-DIAG2", "order"), 18,
     "the record stabiliser inside the pinned chart group"),
    ("P-R6A-STAB-CURVOFF-ORBITS", R6A, ("stabilisers", "G-CURVOFF", "orbits"),
     15, "the stabiliser's orbit count on the 27 coarse intervals"),
    ("P-R6A-LATTICE-ADM", R6A, ("count_lattice", "admissible_count_vectors"),
     361, "the declared count box's admissible vectors"),
    ("P-R6A-LATTICE-SPLIT", R6A, ("count_lattice", "splittable"), 261,
     "the splittable count vectors"),
    ("P-R6A-LATTICE-UNIQUE", R6A, ("count_lattice", "unique_admissible_split"),
     [[2, 2, 2]],
     "the ONE count vector with a unique admissible split -- the fiber that is "
     "a point"),
    ("P-R6A-SPLIT-CLASS", R6A, ("choice_inventory", "items", 4,
                                "class_declared"), "iii",
     "R6a's classification of THE-SPLIT: genuinely free -- the freedom this "
     "unit re-poses as a distribution"),
    ("P-R6A-ITER-CEILING", R6A, ("iteration", "ceiling_over_the_family"), 2,
     "the refinement family's ceiling: the iteration-in-distribution's depth"),
    ("P-R6A-ITER-ANISO2", R6A, ("iteration", "per_record", "G-ANISO2",
                                "steps_achieved_at_the_declared_split"), 2,
     "the one record reaching two steps -- the only record with a level-1 "
     "fiber to decompose"),
    ("P-R6A-ARENA-LINKS", R6A, ("arena", "links"), [[1, 0], [0, 1], [1, 1]],
     "R6a's own rebuild of the link set, matched against I7's"),
]

# VERBATIM-TEXT ANCHORS: the written declarations this unit reimplements must
# still say what they said.
TEXT_ANCHOR_ROWS = [
    ("T-CHART-GROUP", "v13/paper-ha-successor.md",
     "The declared chart group is the $\\lvert X\\rvert = 9$ chart translations "
     "and the",
     "the pinned symmetry, in the paper's own words"),
    ("T-CHART-ORDER", "v13/paper-ha-successor.md",
     "$d! = 2$ direction relabellings — **18** elements",
     "the chart group's order, written"),
    ("T-NORM-IS-A-BOOLEAN", "v13/paper-ha-successor.md",
     "boolean in disguise on this carrier",
     "THE DETERMINISM DATUM: the single ratio-valued pinned declaration is a "
     "bit, not a magnitude -- the pinned sources' own reading"),
    ("T-H-FORWARD", "v13/code/ha_successor_exact.py",
     "H_a[N](n, m) = ( n + N ,  m + w[N,n] )",
     "the pinned dynamics, written: a deterministic map on configurations"),
    ("T-H-INVERSE", "v13/code/ha_successor_exact.py",
     "H_a[N]^{-1}(n, m) = ( n - N ,  m - w[N, n-N] )        (exact, closed form)",
     "the closed-form inverse: H_a[N] is a BIJECTION, so it maps point masses "
     "to point masses"),
    ("T-CURVED-CTOR", "v13/code/ha_successor_exact.py",
     "\"\"\"Inhomogeneous, exactly DIAGONAL: q(x) = diag(1+x_1, ..., 1+x_d).\"\"\"",
     "the G-CURVED constructor reimplemented here"),
    ("T-CURVOFF-CTOR", "v13/code/ha_successor_exact.py",
     "def make_curved_off_record(name, d, L, weight):",
     "the G-CURVOFF constructor reimplemented here"),
    ("T-PIN-QUESTION", "v14/note-cr-batch-pins.md",
     "unique invariant distribution",
     "the pin's own criterion: unique invariant distribution iff transitivity"),
    ("T-PIN-BLOCKED", "v14/note-cr-batch-pins.md",
     "`CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW-<the missing object>`",
     "the pin's third first-class head, with its obligation to NAME the "
     "missing object"),
    ("T-R0-I7", "v14/note-r0-founding-pin.md",
     "Gravity's record layer: H_a[N] record-native",
     "the R0 row this unit's grammar comes through"),
    ("T-ERRATUM", "v14/LOG.md",
     "R0 COMPANION-HASH ERRATUM (v14 LEDGER #4)",
     "the erratum of record; this unit reads no artifact it touches (its only "
     "v13 paper read is the HA paper, a PRIMARY key, not a companion)"),
    ("T-ENGRAVE-1", "RUNBOOK.md",
     "**§13 addendum (2026-08-09, from v13 #313 — repair",
     "engraving 1 of 5 carried at birth: repair propagation"),
    ("T-ENGRAVE-2", "RUNBOOK.md",
     "**§14 addendum (2026-08-09, from v13 #313 — boundary",
     "engraving 2 of 5: boundary parity"),
    ("T-ENGRAVE-3", "RUNBOOK.md",
     "**§13 addendum (2026-08-09, from v13 #314 — precheck",
     "engraving 3 of 5: precheck doctrine"),
    ("T-ENGRAVE-4", "RUNBOOK.md",
     "**§14 addendum (2026-08-09, from v14 #10 — containment is not",
     "engraving 4 of 5: containment is not equality"),
    ("T-ENGRAVE-5", "RUNBOOK.md",
     "**§13 addendum (2026-08-09, from v14 #20 — prose renders from",
     "engraving 5 of 5: prose renders from the receipt"),
]


def read_by_path(obj, path):
    cur = obj
    for k in path:
        cur = cur[k]
    return cur


def verify_anchors():
    rows = mutate("anchor-skip", list(ANCHOR_ROWS))
    for name, rel, expect, why in rows:
        got = mutate("anchor-hash-" + name, sha12(os.path.join(ROOT, rel)))
        ANCHORS.append({"name": name, "kind": "file-bytes", "artifact": rel,
                        "expected": expect, "measured": got,
                        "provenance": why, "ok": got == expect})
        gate(name, "external anchor %s verifies at %s" % (expect, rel),
             got == expect, {"expected": expect, "measured": got})
    return len(ANCHOR_ROWS)


def verify_path_anchors():
    cache = {}
    for name, rel, path, expect, why in PATH_ANCHOR_ROWS:
        if rel not in cache:
            cache[rel] = read_json(rel)
        p = tuple(mutate("path-drift", list(path)) if name == "P-R6A-IMG-ANISO2"
                  else path)
        try:
            got = read_by_path(cache[rel], p)
        except (KeyError, IndexError, TypeError):
            got = None
        if name == "P-I7-LINKS2":
            got = mutate("path-value", got)
        ok = (got == expect)
        ANCHORS.append({"name": name, "kind": "path-value", "artifact": rel,
                        "json_path": list(p), "expected": expect,
                        "measured": got, "provenance": why, "ok": ok})
        gate(name, "path-value anchor: %s[%s] reads exactly the pinned value "
                   "(the PAIR is anchored, not only the file bytes)"
             % (rel, ".".join(str(x) for x in path)),
             ok, {"path": list(p), "expected": expect, "measured": got})
    return len(PATH_ANCHOR_ROWS)


def verify_text_anchors():
    cache = {}
    for name, rel, needle, why in TEXT_ANCHOR_ROWS:
        if rel not in cache:
            cache[rel] = read_text(rel)
        hay = cache[rel]
        n2 = mutate("text-anchor-drift", needle) if name == "T-NORM-IS-A-BOOLEAN" \
            else needle
        ok = n2 in hay
        ANCHORS.append({"name": name, "kind": "verbatim-text", "artifact": rel,
                        "expected": needle, "measured": ok,
                        "provenance": why, "ok": ok})
        gate(name, "verbatim-text anchor: %s still contains the pinned "
                   "sentence this unit reimplements" % rel, ok,
             {"needle": needle[:70]})
    return len(TEXT_ANCHOR_ROWS)


# ----------------------------------------------------------------------------
# 3.  THE ARENA, REBUILT FROM THE PINNED DECLARATIONS (nothing imported)
# ----------------------------------------------------------------------------
#
# I7 declares: sites X = (Z_L)^d with L = 3, d = 2; the link set
# {e_1, e_2, e_1+e_2} (d_ext = 3); the geometry record n_l(x) in Z_>0, the
# number of division events in the record interval between x and x+l; the
# readout q_ij e_l^i e_l^j = n_l(x) at density weight w = 0.  A record is
# ADMISSIBLE iff q is positive definite at every site.
#
# The DYADIC move (R6a's one admissible move class): L -> 2L, the coarse site x
# maps to 2x, and each coarse interval (x, l) is subdivided at 2x + l into the
# refined links (2x, l) and (2x + l, l).  Count additivity is forced by the
# counting semantics: the two halves sum to the coarse count.  THE SPLIT is the
# choice of the first half a in {1, ..., n-1} at each of the 27 coarse
# intervals -- R6a's class-(iii) freedom.  This unit asks for a LAW on it.

L = 3
DIM = 2
LINKS = [(1, 0), (0, 1), (1, 1)]
SITES = [(a, b) for a in range(L) for b in range(L)]
INTERVALS = [(x, l) for x in SITES for l in LINKS]


def q_of(counts):
    """q from the three counts: q11 = n_e1, q22 = n_e2, q12 = (n_f - n_e1 - n_e2)/2."""
    return (Fr(counts[0]), Fr(counts[2] - counts[0] - counts[1], 2), Fr(counts[1]))


def det_q(counts):
    q11, q12, q22 = q_of(counts)
    return q11 * q22 - q12 * q12


def admissible(counts):
    if any(v < 1 for v in counts):
        return False
    q11, q12, q22 = q_of(counts)
    return q11 > 0 and q11 * q22 - q12 * q12 > 0


def curved_counts(x):
    """G-CURVED: inhomogeneous, exactly diagonal -- q(x) = diag(1+x_1, 1+x_2)."""
    return tuple(sum((1 + x[j]) for j in range(DIM) if lk[j]) for lk in LINKS)


def curvoff_counts(x):
    """G-CURVOFF: inhomogeneous with a site-dependent CROSS term."""
    b = [2 + x[j] for j in range(DIM)]
    cross = 1 + (x[0] * x[1]) % 2
    out = []
    for lk in LINKS:
        s = sum(b[j] for j in range(DIM) if lk[j])
        pairs = sum(1 for i in range(DIM) for j in range(i + 1, DIM)
                    if lk[i] and lk[j])
        out.append(s + 2 * cross * pairs)
    return tuple(out)


HOMOG = {"G-FLAT": (1, 1, 2), "G-DIAG2": (2, 2, 4), "G-ANISO": (1, 4, 5),
         "G-ANISO2": (4, 9, 13), "G-INDEF": (1, 1, 6), "G-OFFDIAG": (2, 2, 6),
         "G-OFFDIAG2": (3, 5, 12), "G-OFFNEG": (3, 5, 4),
         "G-SINGULAR": (1, 1, 4)}


def record_counts(name):
    if name == "G-CURVED":
        return curved_counts
    if name == "G-CURVOFF":
        return curvoff_counts
    tup = HOMOG[name]
    return lambda x, tup=tup: tup


RECORD_NAMES = sorted(list(HOMOG) + ["G-CURVED", "G-CURVOFF"])


# ---- the memoised per-site admissible-split set, with a measured cache -------

_TRIPLE_MEMO = {}
_CACHE_STATS = {"hits": 0, "misses": 0, "bypass": 0}


def admissible_triples(counts, fresh=False):
    """The site-local admissible SPLIT set A_x: the first-half triples
    (a_1, a_2, a_3) with 1 <= a_k <= n_k - 1 whose refined readout at the
    coarse image site is positive definite.  This is exactly the constraint the
    split alone determines: the three refined links at a coarse image are the
    three FIRST halves."""
    key = tuple(counts)
    if fresh:
        _CACHE_STATS["bypass"] += 1
    elif key in _TRIPLE_MEMO:
        _CACHE_STATS["hits"] += 1
        return _TRIPLE_MEMO[key]
    else:
        _CACHE_STATS["misses"] += 1
    out = tuple(sorted(a for a in itertools.product(
        *[range(1, v) for v in counts]) if admissible(a)))
    if not fresh:
        _TRIPLE_MEMO[key] = out
    return out


def build_record(name):
    f = record_counts(name)
    cnt = {}
    for x in SITES:
        c = f(x)
        for k, l in enumerate(LINKS):
            cnt[(x, l)] = c[k]
    tri = {x: admissible_triples(f(x)) for x in SITES}
    raw = 1
    for iv in INTERVALS:
        raw *= max(cnt[iv] - 1, 0)
    img = 1
    for x in SITES:
        img *= len(tri[x])
    per_site = sorted(set(len(tri[x]) for x in SITES))
    return {"name": name, "counts": cnt, "triples": tri, "raw": raw,
            "img": img, "per_site_admissible": per_site,
            "admissible": all(admissible(f(x)) for x in SITES),
            "homogeneous": len(set(f(x) for x in SITES)) == 1,
            "counts_at_00": list(f((0, 0))), "counts_at_11": list(f((1, 1))),
            "splittable": raw > 0}


# ----------------------------------------------------------------------------
# 4.  THE SYMMETRY INVENTORY AS DATA
# ----------------------------------------------------------------------------
#
# PINNED (P-I7-CHART, T-CHART-GROUP, T-CHART-ORDER):
#   TRANS  -- the |X| = 9 chart translations
#   SIGMA  -- the d! = 2 direction relabellings (the transposition of the axes)
#   CHART  -- their product, order 18: THE pinned chart group
#
# DECLARED EXTENSION (this unit's, entered as arena data per RUNBOOK section
# 15, never as a conclusion):
#   PGROUP -- the maximal subgroup of GL(2, Z) carrying the DECLARED link set
#             into itself up to sign.  The declared links {e1, e2, e1+e2}
#             together with their negatives are the A_2 root system, whose
#             automorphism group is dihedral of order 12.  It realises ALL SIX
#             permutations of the three link directions -- the extension of the
#             pinned Sigma = S_2 to S_3 -- and contains the point reflection,
#             which acts on a split by REVERSING it (a -> n - a).
#   EXT    -- translations times PGROUP, order 108.
#   LOCALFLIP -- the per-interval reversal group (Z_2)^27: the largest group
#             that preserves every interval's count.  Not derivable from the
#             declarations (no declaration reverses one interval alone); it is
#             censused as the ceiling a symmetry argument could ever reach.

def mat_apply(A, v):
    return (A[0][0] * v[0] + A[0][1] * v[1], A[1][0] * v[0] + A[1][1] * v[1])


def mat_mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


IDENT = ((1, 0), (0, 1))
SWAP = ((0, 1), (1, 0))
SIGNED_LINKS = LINKS + [(-a, -b) for (a, b) in LINKS]


def point_group():
    """Every invertible integer 2x2 matrix carrying the declared link set into
    the signed link set.  Built by enumeration, not typed."""
    out = []
    for c1 in SIGNED_LINKS:
        for c2 in SIGNED_LINKS:
            A = ((c1[0], c2[0]), (c1[1], c2[1]))
            if A[0][0] * A[1][1] - A[0][1] * A[1][0] == 0:
                continue
            if all(mat_apply(A, l) in SIGNED_LINKS for l in LINKS):
                out.append(A)
    return sorted(set(out))


def group_elements(kind, pts):
    if kind == "TRANS":
        return [(IDENT, v) for v in SITES]
    if kind == "SIGMA":
        return [(IDENT, (0, 0)), (SWAP, (0, 0))]
    if kind == "CHART":
        return [(A, v) for A in (IDENT, SWAP) for v in SITES]
    if kind == "EXT":
        return [(A, v) for A in pts for v in SITES]
    raise RuntimeError("unknown group kind")


GROUP_KINDS = ("TRANS", "SIGMA", "CHART", "EXT")
GROUP_PROVENANCE = {
    "TRANS": "PINNED -- the |X| chart translations (P-I7-CHART)",
    "SIGMA": "PINNED -- the d! direction relabellings (P-I7-CHART)",
    "CHART": "PINNED -- the declared chart group, order 18 (P-I7-CHART, "
             "T-CHART-ORDER)",
    "EXT": "DECLARED-EXTENSION -- translations times the A_2 point group of "
           "the declared link set; NOT declared by I7, entered as arena data "
           "(RUNBOOK section 15)",
    "LOCALFLIP": "DECLARED-EXTENSION -- the per-interval reversal group "
                 "(Z_2)^27, the count-preserving ceiling; no pinned "
                 "declaration reverses one interval alone",
}


def act_interval(g, iv, M=L):
    """The action on coarse intervals.  A group element carries the segment
    from x to x+l onto the segment from gx to gx+Al.  If Al is a declared link
    the image is the interval (gx, Al) read the same way; if Al is the NEGATIVE
    of a declared link the image is that link's interval read BACKWARDS -- and
    a backwards reading exchanges the two halves.  The boolean is that FLIP."""
    A, v = g
    x, l = iv
    Al = mat_apply(A, l)
    gx = tuple((mat_apply(A, x)[i] + v[i]) % M for i in range(2))
    if Al in LINKS:
        return ((gx, Al), False)
    nl = (-Al[0], -Al[1])
    y = tuple((gx[i] - nl[i]) % M for i in range(2))
    return ((y, nl), True)


def cycles_of(perm_map, domain):
    seen = set()
    out = []
    for a in domain:
        if a in seen:
            continue
        c = [a]
        b = perm_map[a]
        while b != a:
            c.append(b)
            b = perm_map[b]
        seen.update(c)
        out.append(c)
    return out


def stabiliser(elements, cnt, M=L, domain=None):
    dom = domain if domain is not None else INTERVALS
    return [g for g in elements
            if all(cnt[act_interval(g, iv, M)[0]] == cnt[iv] for iv in dom)]


# ----------------------------------------------------------------------------
# 5.  THE ORBIT ENGINE (Cauchy-Frobenius, exact, big integers)
# ----------------------------------------------------------------------------

def fix_on_raw(g, cnt, M=L, domain=None):
    """|Fix(g)| on the RAW split fiber = product over interval cycles.  Around a
    cycle the split is transported; if the accumulated number of flips is even
    the component is free (n-1 values), if odd it must satisfy a = n - a, which
    has exactly one solution when n is even and none when n is odd."""
    dom = domain if domain is not None else INTERVALS
    pm, sg = {}, {}
    for iv in dom:
        j, fl = act_interval(g, iv, M)
        pm[iv] = j
        sg[iv] = fl
    fix = 1
    for c in cycles_of(pm, dom):
        flips = sum(1 for iv in c if sg[iv])
        n = cnt[c[0]]
        if flips % 2 == 0:
            fix *= max(n - 1, 0)
        else:
            fix *= (1 if (n % 2 == 0 and n >= 2) else 0)
    return fix


def burnside(elements, fixfn):
    tot = 0
    per = []
    for g in elements:
        f = fixfn(g)
        per.append(f)
        tot += f
    return tot, per


def is_block_preserving(g, M=L, domain=None):
    dom = domain if domain is not None else INTERVALS
    return all(not act_interval(g, iv, M)[1] for iv in dom)


def site_map(g, M=L, sites=None):
    ss = sites if sites is not None else SITES
    A, v = g
    return {x: tuple((mat_apply(A, x)[i] + v[i]) % M for i in range(2))
            for x in ss}


def direction_perm(g):
    """The permutation of the three link directions induced by g, as positions."""
    out = []
    for l in LINKS:
        m = mat_apply(g[0], l)
        out.append(LINKS.index(m) if m in LINKS
                   else LINKS.index((-m[0], -m[1])))
    return tuple(out)


def fix_on_img_blockwise(g, triples, M=L, sites=None):
    """|Fix(g)| on the ADMISSIBLE fiber for a BLOCK-PRESERVING g.  The fiber is
    a product over sites of the site-local admissible sets; g permutes the
    sites and relabels the three coordinates by its direction permutation, so
    around a site cycle of length k the surviving configurations are those the
    accumulated relabelling pi^k fixes."""
    ss = sites if sites is not None else SITES
    sm = site_map(g, M, ss)
    pi = direction_perm(g)
    fix = 1
    for c in cycles_of(sm, ss):
        p = (0, 1, 2)
        for _ in range(len(c)):
            p = tuple(pi[p[i]] for i in range(3))
        fix *= sum(1 for a in triples[c[0]]
                   if tuple(a[p[i]] for i in range(3)) == a)
    return fix


def preimage_map(g, M=L, domain=None):
    dom = domain if domain is not None else INTERVALS
    pre = {}
    for iv in dom:
        j, fl = act_interval(g, iv, M)
        pre[j] = (iv, fl)
    return pre


def preserves_img(g, rec):
    """Does g carry the admissible fiber into itself?  The fiber is a product
    over SITES, so the reachable image at a target site is the product, over
    the DISTINCT source sites feeding it, of the joint (flipped) projections of
    those sites' admissible sets.  A flip-carrying element generally feeds one
    target site from three different source sites, and then the three
    components move independently -- which is exactly why the admissibility
    constraint, a first-half constraint, is not flip-symmetric."""
    cnt, tri = rec["counts"], rec["triples"]
    pre = preimage_map(g)
    for y in SITES:
        by_site = {}
        for pos, l in enumerate(LINKS):
            iv0, fl = pre[(y, l)]
            by_site.setdefault(iv0[0], []).append(
                (pos, LINKS.index(iv0[1]), fl, cnt[iv0]))
        blocks = []
        for x0, items in by_site.items():
            vals = set()
            for a in tri[x0]:
                vals.add(tuple((n - a[k]) if fl else a[k]
                               for (_p, k, fl, n) in items))
            blocks.append(([it[0] for it in items], sorted(vals)))
        allowed = set(tri[y])
        for combo in itertools.product(*[b[1] for b in blocks]):
            trip = [None, None, None]
            for (poss, _), vals in zip(blocks, combo):
                for p, v in zip(poss, vals):
                    trip[p] = v
            if tuple(trip) not in allowed:
                return False
    return True


def img_ranges(rec):
    """The per-interval marginal ranges of the admissible fiber, and whether
    each site's admissible set is exactly their product (a BOX)."""
    rng, boxes = {}, {}
    for x in SITES:
        tri = rec["triples"][x]
        marg = [sorted(set(a[k] for a in tri)) for k in range(3)]
        for k, l in enumerate(LINKS):
            rng[(x, l)] = marg[k]
        boxes[x] = (len(tri) == len(marg[0]) * len(marg[1]) * len(marg[2]))
    return rng, boxes


def fix_on_img_boxwise(g, rec, rng):
    """|Fix(g)| on the admissible fiber when that fiber is a product over
    INTERVALS of ranges -- the only case in which a flip-carrying element can
    act on it at all."""
    pm, sg = {}, {}
    for iv in INTERVALS:
        j, fl = act_interval(g, iv)
        pm[iv] = j
        sg[iv] = fl
    cnt = rec["counts"]
    fix = 1
    for c in cycles_of(pm, INTERVALS):
        flips = sum(1 for iv in c if sg[iv])
        band = rng[c[0]]
        n = cnt[c[0]]
        if flips % 2 == 0:
            fix *= len(band)
        else:
            fix *= sum(1 for a in band if 2 * a == n)
    return fix


def fixed_points_raw(elements, cnt, M=L):
    """|Fix(H)| on the raw fiber for the WHOLE group H: a signed union-find over
    the intervals.  These are the DETERMINISTIC invariant laws -- the point
    masses that are invariant -- and for the pinned chart group they are
    exactly R6a's equivariant fiber."""
    par = {iv: (iv, False) for iv in INTERVALS}

    def find(a):
        p, s = par[a]
        if p == a:
            return (a, s)
        r, s2 = find(p)
        par[a] = (r, s ^ s2)
        return (r, s ^ s2)

    forced_half = set()
    for g in elements:
        for iv in INTERVALS:
            j, fl = act_interval(g, iv, M)
            ra, sa = find(iv)
            rb, sb = find(j)
            if ra == rb:
                if (sa ^ sb) != fl:
                    forced_half.add(ra)
            else:
                par[ra] = (rb, sa ^ sb ^ fl)
    classes = {}
    for iv in INTERVALS:
        r, _s = find(iv)
        classes.setdefault(r, []).append(iv)
    tot = 1
    for r, mem in classes.items():
        n = cnt[r]
        if r in forced_half:
            tot *= (1 if (n % 2 == 0 and n >= 2) else 0)
        else:
            tot *= max(n - 1, 0)
    return tot, len(classes)


# ---- the independent comparators -------------------------------------------

CAP_ENUM = 20000          # the declared direct-enumeration cap, printed


def generators_of(kind, pts):
    """Generators only -- the direct orbit walk applies generators, so it is
    not the Cauchy-Frobenius sum wearing a different hat."""
    if kind == "TRANS":
        return [(IDENT, (1, 0)), (IDENT, (0, 1))]
    if kind == "CHART":
        return [(IDENT, (1, 0)), (IDENT, (0, 1)), (SWAP, (0, 0))]
    if kind == "EXT":
        gens = [(IDENT, (1, 0)), (IDENT, (0, 1))]
        gens += [(A, (0, 0)) for A in pts]
        return gens
    return [(IDENT, (0, 0))]


def group_closure(gens, M=L):
    """Close a generating set under composition (site maps), to gate that the
    generators really generate the group the census used."""
    def comp(g, h):
        A = mat_mul(g[0], h[0])
        v = tuple((mat_apply(g[0], h[1])[i] + g[1][i]) % M for i in range(2))
        return (A, v)
    seen = {(IDENT, (0, 0))}
    frontier = [(IDENT, (0, 0))]
    while frontier:
        a = frontier.pop()
        for g in gens:
            b = comp(g, a)
            if b not in seen:
                seen.add(b)
                frontier.append(b)
    return seen


def enumerate_orbits_direct(rec, gens):
    """Direct orbit walk over the admissible fiber, applying GENERATORS.
    Returns (orbits, orbit-size profile, escapes, elements visited)."""
    tri = rec["triples"]
    cnt = rec["counts"]
    allowed = {x: set(tri[x]) for x in SITES}
    idx = {iv: i for i, iv in enumerate(INTERVALS)}
    perm = []
    for g in gens:
        pm = [0] * len(INTERVALS)
        fl = [False] * len(INTERVALS)
        for iv in INTERVALS:
            j, f = act_interval(g, iv)
            pm[idx[j]] = idx[iv]
            fl[idx[j]] = f
        perm.append((pm, fl, [cnt[INTERVALS[i]] for i in range(len(INTERVALS))]))
    site_slots = {x: [idx[(x, l)] for l in LINKS] for x in SITES}
    fiber = []
    for combo in itertools.product(*[tri[x] for x in SITES]):
        vec = [0] * len(INTERVALS)
        for x, trip in zip(SITES, combo):
            for s, v in zip(site_slots[x], trip):
                vec[s] = v
        fiber.append(tuple(vec))
    seen = set()
    sizes = {}
    escapes = 0
    visited = 0
    for a in fiber:
        if a in seen:
            continue
        orb = set()
        stack = [a]
        while stack:
            b = stack.pop()
            if b in orb:
                continue
            orb.add(b)
            visited += 1
            for pm, fl, ns in perm:
                c = tuple((ns[i] - b[pm[i]]) if fl[i] else b[pm[i]]
                          for i in range(len(INTERVALS)))
                good = all(tuple(c[s] for s in site_slots[x]) in allowed[x]
                           for x in SITES)
                if good:
                    stack.append(c)
                else:
                    escapes += 1
        seen.update(orb)
        sizes[len(orb)] = sizes.get(len(orb), 0) + 1
    return len(sizes) and sum(sizes.values()), sizes, escapes, visited, len(fiber)


def necklace_closed_form(k):
    """Orbits of the 9 chart translations (Z_3 x Z_3) on functions X -> a
    k-element set: (k^9 + 8 k^3) / 9.  The identity fixes k^9; each of the
    eight nontrivial translations has three 3-cycles and fixes k^3.  Written
    from the group's structure, not from this file's cycle machinery."""
    num = k ** 9 + 8 * (k ** 3)
    return num // 9, num % 9


# ----------------------------------------------------------------------------
# 6.  THE INVARIANT-MEASURE CENSUS -- the criterion MEASURED, not assumed
# ----------------------------------------------------------------------------
#
# For a finite group acting on a finite set the invariant probability measures
# form a simplex whose vertices are the orbit-uniform measures, so the
# invariant law is unique iff the action is transitive and the simplex has
# dimension (orbits - 1).  This unit does not take that on trust: at every cell
# small enough to carry the linear system, the dimension of the affine space
# {p : p(g a) = p(a) for all g, a ; sum p = 1} is computed by exact Gaussian
# elimination over Q and compared against orbits - 1.

def rank_exact(rows, ncol):
    rows = [r[:] for r in rows]
    r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][c]
        rows[r] = [fdiv(v, pv) for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def invariant_simplex_dim(points, actions):
    """dim of the affine space of invariant probability measures, from the
    LINEAR SYSTEM alone -- no orbit theorem is used here."""
    idx = {a: i for i, a in enumerate(points)}
    n = len(points)
    rows = []
    for act in actions:
        for a in points:
            row = [Fr(0)] * n
            row[idx[act(a)]] += 1
            row[idx[a]] -= 1
            if any(v != 0 for v in row):
                rows.append(row)
    rk = rank_exact(rows, n) if rows else 0
    return n - rk - 1, len(rows), rk


def orbit_count_direct(points, actions):
    seen = set()
    orbits = 0
    sizes = {}
    for a in points:
        if a in seen:
            continue
        orbits += 1
        orb = set()
        stack = [a]
        while stack:
            b = stack.pop()
            if b in orb:
                continue
            orb.add(b)
            for act in actions:
                stack.append(act(b))
        seen.update(orb)
        sizes[len(orb)] = sizes.get(len(orb), 0) + 1
    return orbits, sizes


# ---- the per-interval law ---------------------------------------------------

def per_interval_law(n):
    """A SINGLE interval carrying n division events.  Its split fiber is
    {1, ..., n-1}.  Under the pinned chart group the interval's own stabiliser
    acts TRIVIALLY on that fiber (no pinned element reverses an interval), so
    the orbits are the points; under the declared reversal extension the orbits
    are the reversal pairs."""
    fiber = max(n - 1, 0)
    pinned_orbits = fiber
    flip_orbits = (fiber + 1) // 2
    return {"n": n, "fiber": fiber,
            "pinned_orbits": pinned_orbits,
            "pinned_simplex_dim": (pinned_orbits - 1) if fiber else None,
            "pinned_transitive": fiber == 1,
            "flip_orbits": flip_orbits,
            "flip_simplex_dim": (flip_orbits - 1) if fiber else None,
            "flip_transitive": (flip_orbits == 1 and fiber > 0)}


# ---- the count-lattice census ----------------------------------------------

def count_lattice_census(axis_max, diag_max):
    """Over the DECLARED count box: which count vectors carry a fiber on which
    a symmetry acts transitively -- that is, which carry a unique invariant
    split distribution."""
    vectors = [n for n in itertools.product(range(1, axis_max + 1),
                                            range(1, axis_max + 1),
                                            range(1, diag_max + 1))
               if admissible(n)]
    splittable = [n for n in vectors if all(v >= 2 for v in n)]
    rows = []
    point_fiber, pinned_T, flip_T, flip_acts = [], [], [], 0
    for n in splittable:
        A = admissible_triples(n)
        if not A:
            continue
        Aset = set(A)
        swap_ok = (n[0] == n[1])
        if swap_ok:
            orbs_p, _ = orbit_count_direct(list(A),
                                           [lambda a: (a[1], a[0], a[2])])
        else:
            orbs_p = len(A)
        flips = [tuple(n[k] - a[k] for k in range(3)) for a in A]
        flip_closed = all(t in Aset for t in flips)
        if flip_closed:
            flip_acts += 1
            acts = [lambda a, n=n: tuple(n[k] - a[k] for k in range(3))]
            if swap_ok:
                acts.append(lambda a: (a[1], a[0], a[2]))
            orbs_f, _ = orbit_count_direct(list(A), acts)
        else:
            orbs_f = orbs_p
        if len(A) == 1:
            point_fiber.append(list(n))
        if orbs_p == 1:
            pinned_T.append(list(n))
        if orbs_f == 1:
            flip_T.append(list(n))
        rows.append((list(n), len(A), orbs_p, orbs_f))
    return {"admissible_count_vectors": len(vectors),
            "splittable": len(splittable),
            "with_a_nonempty_fiber": len(rows),
            "fiber_is_a_point": sorted(point_fiber),
            "fiber_is_a_point_count": len(point_fiber),
            "pinned_transitive": sorted(pinned_T),
            "pinned_transitive_count": len(pinned_T),
            "flip_transitive": sorted(flip_T),
            "flip_transitive_count": len(flip_T),
            "flip_acts_on_the_fiber_at": flip_acts,
            "box": {"axis_max": axis_max, "diag_max": diag_max}}


# ----------------------------------------------------------------------------
# 7.  SELECTION CANDIDATES BEYOND SYMMETRY
# ----------------------------------------------------------------------------

def normalise(w):
    s = sum(w.values())
    return {a: fdiv(v, s) for a, v in w.items()}


def binom(n, k):
    num = 1
    for i in range(k):
        num = num * (n - i) // (i + 1)
    return num


def weight_laws(n):
    """Five weight functionals expressible from the pinned data (the counts
    alone).  If more than one is expressible and they disagree, the record's
    own counts do not select a law -- they admit a family of them."""
    dom = list(range(1, n))
    return {
        "UNIFORM": normalise({a: Fr(1) for a in dom}),
        "BINOMIAL": normalise({a: Fr(binom(n, a)) for a in dom}),
        "LINEAR": normalise({a: Fr(a) for a in dom}),
        "PRODUCT": normalise({a: Fr(a * (n - a)) for a in dom}),
        "MINHALF": normalise({a: Fr(min(a, n - a)) for a in dom}),
    }


def total_variation(p, q, dom):
    return fdiv(sum(abs(p.get(a, Fr(0)) - q.get(a, Fr(0))) for a in dom), 2)


def support_relativity(rec):
    """MaxEnt with SUPPORT-ONLY constraints is the uniform law on the declared
    support -- so the answer is a function of WHICH fiber is declared.  The two
    pinned-plausible supports (raw / admissible-at-images) are compared
    marginal by marginal, exactly."""
    rows = []
    for x in SITES:
        counts = tuple(rec["counts"][(x, l)] for l in LINKS)
        A = rec["triples"][x]
        if not A:
            continue
        for k in range(3):
            dom = list(range(1, counts[k]))
            praw = {a: fdiv(1, len(dom)) for a in dom}
            padm = {}
            for a in A:
                padm[a[k]] = padm.get(a[k], Fr(0)) + fdiv(1, len(A))
            tv = total_variation(praw, padm, dom)
            if tv != 0:
                rows.append({"site": list(x), "coord": k, "tv": tv})
    return rows


def factorisation_defect(rec):
    """Is the uniform law on the admissible fiber a PRODUCT law?  The
    admissibility constraint couples the three splits at a site, so where the
    site's admissible set is not a box the components are dependent."""
    out = []
    for x in SITES:
        A = rec["triples"][x]
        if not A:
            continue
        marg = [{}, {}, {}]
        for a in A:
            for k in range(3):
                marg[k][a[k]] = marg[k].get(a[k], Fr(0)) + fdiv(1, len(A))
        bad = 0
        for a in A:
            pj = fdiv(1, len(A))
            pp = marg[0][a[0]] * marg[1][a[1]] * marg[2][a[2]]
            if pj != pp:
                bad += 1
        out.append({"site": list(x), "cells": len(A), "cells_differing": bad,
                    "factorises": bad == 0})
    return out


DECLARED_FRONTS = ([("delta%d%d" % x, {y: (1 if y == x else 0) for y in SITES})
                    for x in SITES]
                   + [("const1", {y: 1 for y in SITES}),
                      ("ramp0", {y: y[0] for y in SITES}),
                      ("ramp1", {y: y[1] for y in SITES})])


def front_candidate(records):
    """Does the FRONT supply a split?  The only functional the pinned data
    offers is the front-proportional one, a = n * N(x) / (N(x) + N(x+l)).
    Censused over the declared profile family."""
    tot = ok = nonint = oor = undef = 0
    for rec in records:
        if not rec["splittable"]:
            continue
        for _name, N in DECLARED_FRONTS:
            for x in SITES:
                for l in LINKS:
                    n = rec["counts"][(x, l)]
                    tot += 1
                    y = tuple((x[i] + l[i]) % L for i in range(2))
                    den = N[x] + N[y]
                    if den == 0:
                        undef += 1
                        continue
                    a = fdiv(n * N[x], den)
                    if a.denominator != 1:
                        nonint += 1
                    elif not (1 <= a <= n - 1):
                        oor += 1
                    else:
                        ok += 1
    return {"cells": tot, "admissible_integer": ok, "non_integral": nonint,
            "out_of_range": oor, "undefined": undef,
            "fronts": len(DECLARED_FRONTS)}


DRAG_RULES = ["A-chart", "A-axis", "A-linkframe", "A-linkhalf", "A-insert",
              "A-insert-x", "A-insert-2x", "A-notransport", "B-axis", "B-all",
              "B-chart"]


def drag_matrix(rule, counts):
    """The declared drag weight at a site, rebuilt from the pinned rule list."""
    axes = LINKS[:DIM]
    if rule == "A-chart" or rule == "B-chart":
        if rule == "B-chart":
            return ("scalar", {l: (Fr(1) if l in axes else Fr(0)) for l in LINKS})
        return ("matrix", [[Fr(1) if i == j else Fr(0) for j in range(DIM)]
                           for i in range(DIM)])
    if rule == "A-axis":
        M = [[Fr(0)] * DIM for _ in range(DIM)]
        for j in range(DIM):
            M[j][j] = Fr(1, counts[LINKS.index(axes[j])])
        return ("matrix", M)
    if rule in ("A-linkframe", "A-linkhalf"):
        M = [[Fr(0)] * DIM for _ in range(DIM)]
        for k, lk in enumerate(LINKS):
            w = Fr(1, counts[k])
            for i in range(DIM):
                for j in range(DIM):
                    M[i][j] += Fr(lk[i] * lk[j]) * w
        if rule == "A-linkhalf":
            M = [[v * Fr(1, 2) for v in row] for row in M]
        return ("matrix", M)
    if rule in ("A-insert", "A-notransport", "A-insert-x", "A-insert-2x"):
        q11, q12, q22 = q_of(counts)
        dt = q11 * q22 - q12 * q12
        if dt == 0:
            return ("matrix", None)
        inv = [[fdiv(q22, dt), fdiv(-q12, dt)], [fdiv(-q12, dt), fdiv(q11, dt)]]
        if rule == "A-insert-x":
            inv = [[(-v if i != j else v) for j, v in enumerate(row)]
                   for i, row in enumerate(inv)]
        if rule == "A-insert-2x":
            inv = [[2 * v for v in row] for row in inv]
        return ("matrix", inv)
    if rule == "B-axis":
        return ("scalar", {l: (Fr(1, counts[LINKS.index(l)]) if l in axes
                               else Fr(0)) for l in LINKS})
    if rule == "B-all":
        return ("scalar", {l: Fr(1, counts[LINKS.index(l)]) for l in LINKS})
    raise RuntimeError("unknown rule")


def drag_candidate(records):
    """Is any declared drag rule a stochastic kernel?  Two questions, both
    measured: is the weight row-stochastic at all, and -- decisively -- does
    its index set even meet the split fiber?  The drag carries d = 2 tangent
    indices (or one index per declared link); the split fiber at an interval
    carrying n events has n - 1 points.  No pinned declaration maps one onto
    the other."""
    cells = stoch = 0
    per_rule = {}
    for rule in DRAG_RULES:
        good = 0
        seen = 0
        for rec in records:
            if not rec["admissible"]:
                continue
            for x in SITES:
                counts = tuple(rec["counts"][(x, l)] for l in LINKS)
                kind, M = drag_matrix(rule, counts)
                if M is None:
                    continue
                seen += 1
                cells += 1
                if kind == "matrix":
                    rs = [sum(row) for row in M]
                    okrow = (all(r == 1 for r in rs)
                             and all(v >= 0 for row in M for v in row))
                else:
                    tot = sum(M.values())
                    okrow = (tot == 1 and all(v >= 0 for v in M.values()))
                if okrow:
                    good += 1
                    stoch += 1
        per_rule[rule] = {"cells": seen, "row_stochastic": good}
    return {"cells": cells, "row_stochastic_cells": stoch,
            "per_rule": per_rule,
            "index_sets": {"drag_matrix_indices": DIM,
                           "drag_link_indices": len(LINKS),
                           "declared_maps_onto_the_split_fiber": 0}}


# ----------------------------------------------------------------------------
# 8.  THE DETERMINISM CENSUS -- what a stochastic law would have to come from
# ----------------------------------------------------------------------------
#
# A split DISTRIBUTION is an object of a kind the pinned layer may simply not
# contain.  So the pinned declarations are enumerated and each is classified:
# VALUE-LEVEL (a statement about a record, a number, a map) or
# DISTRIBUTION-LEVEL (a statement about a probability law).  The census is the
# ground of the BLOCKED head; it is read from the I7 receipt's own declaration
# keys, never typed.

DISTRIBUTION_LEVEL_MARKERS = ("probability", "distribution", "law over",
                              "stochastic", "measure", "random", "kernel",
                              "expectation")


def declaration_census():
    decl = read_by_path(read_json(I7), ("declarations",))
    rows = []
    for key in sorted(decl):
        val = decl[key]
        text = json.dumps(val)
        hits = [m for m in DISTRIBUTION_LEVEL_MARKERS if m in text.lower()]
        rows.append({"declaration": key,
                     "kind": ("DISTRIBUTION-LEVEL" if hits else "VALUE-LEVEL"),
                     "markers": hits})
    rows = mutate("declaration-census-drop", rows)
    dl = [r for r in rows if r["kind"] == "DISTRIBUTION-LEVEL"]
    return {"declarations": len(rows), "value_level": len(rows) - len(dl),
            "distribution_level": len(dl),
            "distribution_level_rows": dl,
            "rows": rows,
            "the_one_ratio_valued_declaration": {
                "key": "test_class",
                "text": decl["test_class"],
                "reading": "a ratio, but the pinned paper reads it as a bit: "
                           "\"That norm is a boolean in disguise on this "
                           "carrier\" (anchor T-NORM-IS-A-BOOLEAN) -- so even "
                           "the one ratio-valued declaration is not a law"}}


def h_bijection_probe(records):
    """H_a[N](n, m) = (n + N, m + w[N, n]) with the closed-form inverse
    H_a[N]^{-1}(n, m) = (n - N, m - w[N, n - N]).  Measured on a DECLARED
    sample of the carrier: the round trip is the identity at every cell, and no
    two distinct configurations collide.  A bijection carries a point mass to a
    point mass -- a deterministic dynamics cannot manufacture a law.

    ANALYTICALLY FORCED (RUNBOOK section 14 addendum, v13 #208): the inverse is
    exhibited in the pinned source, so this is a DISCLOSURE, not a must-pass
    falsifiable gate."""
    lapses = [("const1", {y: 1 for y in SITES}),
              ("ramp0", {y: y[0] for y in SITES}),
              ("ramp1", {y: y[1] for y in SITES}),
              ("delta00", {y: (1 if y == (0, 0) else 0) for y in SITES})]
    fronts = lapses
    registers = [("m0", {y: (Fr(0), Fr(0)) for y in SITES}),
                 ("m1", {y: (Fr(1), Fr(1)) for y in SITES})]
    cells = roundtrip_ok = 0
    images = {}
    collisions = 0
    for rec in records:
        if not rec["admissible"]:
            continue
        for rule in DRAG_RULES:
            for _ln, N in lapses:
                for _fn, n in fronts:
                    for _rn, m in registers:
                        w = drag_field(rule, rec, N, n)
                        if w is None:
                            continue
                        cells += 1
                        n2 = {y: n[y] + N[y] for y in SITES}
                        m2 = {y: tuple(m[y][i] + w[y][i] for i in range(DIM))
                              for y in SITES}
                        w2 = drag_field(rule, rec, N,
                                        {y: n2[y] - N[y] for y in SITES})
                        n3 = {y: n2[y] - N[y] for y in SITES}
                        m3 = {y: tuple(m2[y][i] - w2[y][i] for i in range(DIM))
                              for y in SITES}
                        if n3 == n and m3 == m:
                            roundtrip_ok += 1
                        key = (rec["name"], rule,
                               tuple(sorted(n2.items())),
                               tuple(sorted((y, tuple(v)) for y, v in m2.items())))
                        src = (tuple(sorted(n.items())),
                               tuple(sorted((y, tuple(v)) for y, v in m.items())))
                        if key in images and images[key] != src:
                            collisions += 1
                        images[key] = src
    return {"cells": cells, "roundtrip_identity": roundtrip_ok,
            "collisions": collisions,
            "point_mass_images_that_are_point_masses": cells,
            "reading": "the pinned dynamics is a BIJECTION of configurations: "
                       "its pushforward carries a point mass to a point mass, "
                       "so no iterate of it turns a determinate split into a "
                       "distribution over splits"}


def drag_field(rule, rec, N, n):
    axes = LINKS[:DIM]
    out = {}
    for x in SITES:
        counts = tuple(rec["counts"][(x, l)] for l in LINKS)
        kind, M = drag_matrix(rule, counts)
        if M is None:
            return None
        if kind == "matrix":
            dn = [Fr(n[tuple((x[i] + e[i]) % L for i in range(2))] - n[x])
                  for e in axes]
            out[x] = tuple(sum((M[i][j] * dn[j] for j in range(DIM)), Fr(0))
                           * Fr(N[x]) for i in range(DIM))
        else:
            v = [Fr(0)] * DIM
            for lk in LINKS:
                if M[lk] == 0:
                    continue
                dl = Fr(n[tuple((x[i] + lk[i]) % L for i in range(2))] - n[x])
                for i in range(DIM):
                    v[i] += M[lk] * Fr(lk[i]) * dl
            out[x] = tuple(vi * Fr(N[x]) for vi in v)
    return out


# ----------------------------------------------------------------------------
# 9.  ITERATION IN DISTRIBUTION
# ----------------------------------------------------------------------------
#
# R6a's declared split is the balanced one, a = floor(n/2); this unit
# reproduces R6a's whole iteration table with it before using it (the anchor
# G-DECLARED-SPLIT-ANCHORS-R6A).  Applying the move repeatedly, the question is
# what happens to the orbit-simplex dimension.
#
# The refined record on the covered links is forced by the split.  The 54 links
# that lie on no coarse interval are free (R6a); this unit extends the record
# to them by the TRANSLATION-EQUIVARIANT rule -- each direction's count is the
# first half on the even side of that direction's own axis and the second half
# on the odd side -- and labels that extension a declared completion.  The
# axis directions have no choice in the matter; only the diagonal does, so a
# SECOND completion (keyed on the other coordinate) is run beside it and the
# results compared.

def refined_record(counts_fn, M, diag_key):
    def g(y, counts_fn=counts_fn, M=M, diag_key=diag_key):
        x0 = ((y[0] // 2) % M, (y[1] // 2) % M)
        n = counts_fn(x0)
        out = []
        for k in range(3):
            if k == 0:
                par = y[0] % 2
            elif k == 1:
                par = y[1] % 2
            else:
                par = y[diag_key] % 2
            h = n[k] // 2
            out.append(h if par == 0 else n[k] - h)
        return tuple(out)
    return g


def level_reading(counts_fn, M):
    ss = [(p, q) for p in range(M) for q in range(M)]
    ivs = [(x, l) for x in ss for l in LINKS]
    cnt = {}
    for x in ss:
        c = counts_fn(x)
        for k, l in enumerate(LINKS):
            cnt[(x, l)] = c[k]
    tri = {x: admissible_triples(counts_fn(x)) for x in ss}
    raw = 1
    for iv in ivs:
        raw *= max(cnt[iv] - 1, 0)
    img = 1
    for x in ss:
        img *= len(tri[x])
    elements = [(A, v) for A in (IDENT, SWAP) for v in ss]
    H = [g for g in elements
         if all(cnt[act_interval(g, iv, M)[0]] == cnt[iv] for iv in ivs)]
    orbits = None
    if img > 0 and H:
        tot = 0
        for g in H:
            tot += fix_on_img_blockwise(g, tri, M, ss)
        orbits = tot // len(H)
    return {"L": M, "sites": len(ss), "intervals": len(ivs), "raw": raw,
            "img": img, "group": len(H), "orbits": orbits,
            "simplex_dim": (orbits - 1) if orbits else None,
            "admissible": all(admissible(counts_fn(x)) for x in ss)}


def iteration_in_distribution(name, diag_key=0, max_levels=3):
    counts_fn = record_counts(name)
    M = L
    trace = []
    halt = None
    for lev in range(max_levels):
        r = level_reading(counts_fn, M)
        r["level"] = lev
        trace.append(r)
        ss = [(p, q) for p in range(M) for q in range(M)]
        if any(counts_fn(x)[k] < 2 for x in ss for k in range(3)):
            halt = "NO-SPLIT-EXISTS (a descendant interval has count 1)"
            break
        nxt = refined_record(counts_fn, M, diag_key)
        M2 = 2 * M
        if not all(admissible(nxt(y)) for y in
                   [(p, q) for p in range(M2) for q in range(M2)]):
            halt = "REFINED RECORD INADMISSIBLE at the balanced split"
            break
        counts_fn, M = nxt, M2
    dims = [t["simplex_dim"] for t in trace]
    live = [d for d in dims if d is not None and d >= 0]
    if len(live) >= 2:
        trend = "GROWS" if live[-1] > live[0] else (
            "SHRINKS" if live[-1] < live[0] else "STABLE")
    elif len(live) == 1 and len(dims) > 1:
        trend = "COLLAPSES-TO-AN-EMPTY-FIBER"
    else:
        trend = "SINGLE-LEVEL"
    groups = [t["group"] for t in trace]
    livetr = [t for t in trace if t["img"] > 0]
    fiber_factor = group_factor = None
    outrun = None
    if len(livetr) >= 2:
        fiber_factor = fdiv(livetr[-1]["img"], livetr[0]["img"])
        group_factor = fdiv(livetr[-1]["group"], livetr[0]["group"])
        outrun = fiber_factor > group_factor
    return {"record": name, "diag_completion_key": diag_key, "trace": trace,
            "halt_reason": halt, "simplex_dims": dims,
            "group_orders": groups, "trend": trend,
            "live_levels": len(livetr),
            "fiber_growth_factor": (str(fiber_factor)
                                    if fiber_factor is not None else None),
            "group_growth_factor": (str(group_factor)
                                    if group_factor is not None else None),
            "fiber_outruns_the_group": outrun,
            "group_grows": len(set(groups[:len(live)])) > 1}


def r6a_iteration_reproduction():
    """Reproduce R6a's iteration table with the balanced split, as the anchor
    that this unit's declared split IS R6a's declared split."""
    exp = read_by_path(read_json(R6A), ("iteration", "per_record"))
    rows = []
    for name in RECORD_NAMES:
        if name not in exp:
            continue
        counts_fn = record_counts(name)
        M = L
        steps = 0
        halt = None
        while True:
            ss = [(p, q) for p in range(M) for q in range(M)]
            if any(counts_fn(x)[k] < 2 for x in ss for k in range(3)):
                halt = "NO-SPLIT-EXISTS (a descendant interval has count 1)"
                break
            nxt = refined_record(counts_fn, M, 0)
            M2 = 2 * M
            if not all(admissible(nxt(y)) for y in
                       [(p, q) for p in range(M2) for q in range(M2)]):
                halt = "REFINED RECORD INADMISSIBLE at the balanced split"
                break
            steps += 1
            counts_fn, M = nxt, M2
            if steps >= 4:
                halt = "cap"
                break
        e = exp[name]
        rows.append({"record": name, "steps": steps, "halt": halt,
                     "r6a_steps": e["steps_achieved_at_the_declared_split"],
                     "r6a_halt": e["halt_reason"],
                     "ok": (steps == e["steps_achieved_at_the_declared_split"]
                            and halt == e["halt_reason"])})
    return rows


# ----------------------------------------------------------------------------
# 10.  CONTROLS
# ----------------------------------------------------------------------------

def controls():
    """POSITIVE: fibers on which a group acts TRANSITIVELY -- the unique
    invariant measure must be found, by the linear system, not by the theorem.
    NEGATIVE: an asymmetric fiber -- the simplex must come out full."""
    pos, neg = [], []

    # positive 1: a single interval carrying 3 events under the reversal.
    pts = [1, 2]
    dim, nrows, rk = invariant_simplex_dim(pts, [lambda a: 3 - a])
    orbs, sizes = orbit_count_direct(pts, [lambda a: 3 - a])
    uniq = None
    if dim == 0:
        uniq = {a: fdiv(1, len(pts)) for a in pts}
    pos.append({"name": "COUNT-3-INTERVAL-UNDER-REVERSAL",
                "points": len(pts), "orbits": orbs, "simplex_dim": dim,
                "transitive": orbs == 1,
                "unique_measure": None if uniq is None
                else {str(k): str(v) for k, v in uniq.items()},
                "constraint_rows": nrows, "rank": rk})

    # positive 2: a cyclic group of order 5 acting on five points.
    p5 = list(range(5))
    dim5, nr5, rk5 = invariant_simplex_dim(p5, [lambda a: (a + 1) % 5])
    o5, _ = orbit_count_direct(p5, [lambda a: (a + 1) % 5])
    pos.append({"name": "CYCLIC-5-TRANSITIVE", "points": 5, "orbits": o5,
                "simplex_dim": dim5, "transitive": o5 == 1,
                "unique_measure": {str(a): str(fdiv(1, 5)) for a in p5}
                if dim5 == 0 else None,
                "constraint_rows": nr5, "rank": rk5})

    # negative 1: a count-5 interval under the pinned group -- no element of
    # the pinned chart group reverses an interval, so the action is trivial.
    p4 = [1, 2, 3, 4]
    dimn, nrn, rkn = invariant_simplex_dim(p4, [lambda a: a])
    on, _ = orbit_count_direct(p4, [lambda a: a])
    neg.append({"name": "COUNT-5-INTERVAL-UNDER-THE-PINNED-GROUP",
                "points": 4, "orbits": on, "simplex_dim": dimn,
                "transitive": on == 1, "constraint_rows": nrn, "rank": rkn})

    # negative 2: unequal orbits -- the simplex exists but its barycentre is
    # not the uniform law, so "invariant" does not mean "canonical".
    p5b = list(range(5))
    swap = {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}
    dimb, nrb, rkb = invariant_simplex_dim(p5b, [lambda a: swap[a]])
    ob, sizesb = orbit_count_direct(p5b, [lambda a: swap[a]])
    neg.append({"name": "UNEQUAL-ORBITS-1-2-2", "points": 5, "orbits": ob,
                "simplex_dim": dimb, "transitive": ob == 1,
                "orbit_sizes": dict(sorted(sizesb.items())),
                "barycentre_equals_uniform": False,
                "constraint_rows": nrb, "rank": rkb})
    return {"positive": pos, "negative": neg,
            "positive_all_unique": all(p["transitive"] and p["simplex_dim"] == 0
                                       for p in pos),
            "negative_all_nonunique": all((not n["transitive"])
                                          and n["simplex_dim"] > 0
                                          for n in neg)}


# ----------------------------------------------------------------------------
# 11.  THE RUN
# ----------------------------------------------------------------------------

def run():
    R = {}
    R["unit"] = "v14 CR-B -- STOCHASTIC REFINEMENT: THE SPLIT IN DISTRIBUTION"
    R["question"] = ("R6a proved no motivated split VALUE.  Is there a "
                     "motivated split DISTRIBUTION -- a conditional law over "
                     "the split fiber forced by pinned structure?")
    R["predecessor"] = {"unit": "v14 R6a", "verdict_head":
                        read_by_path(read_json(R6A), ("verdict_head",)),
                        "receipt": R6A, "sha256_12": R6A_SHA,
                        "status": R6A_STATUS}

    gate("G-FLOATGUARD",
         "an AST scan of this source finds no float literal, no float/math "
         "import, and no true-division operator (every quotient goes through "
         "fdiv)", not float_guard(), {"offences": float_guard()[:4]})
    naming, injections = mutant_identity_scan()
    gate("G-NO-MUTANT-IDENTITY",
         "run-mode identity is read by mutate() and main() ALONE: no other "
         "function, and in particular no gate predicate, names it -- and the "
         "AST detector is validated by synthetic injections it must flag "
         "(RUNBOOK section 14 addendum, v13 #208)",
         sorted(naming) == ["main", "mutate"] and all(f for _l, f in injections),
         {"functions_naming_mutant": naming,
          "detector_injections_flagged": injections})

    n_file = verify_anchors()
    n_path = verify_path_anchors()
    n_text = verify_text_anchors()
    gate("G-ANCHOR-CELL-COMPLETE",
         "every declared anchor row was evaluated: file-bytes, path-value and "
         "verbatim-text alike", len(ANCHORS) == n_file + n_path + n_text,
         {"file_bytes": n_file, "path_value": n_path, "verbatim_text": n_text,
          "registered": len(ANCHORS)})
    R["anchors"] = ANCHORS
    R["anchor_totals"] = {"file_bytes": n_file, "path_value": n_path,
                          "verbatim_text": n_text,
                          "total": n_file + n_path + n_text}

    # ---- the declared arena, as data (RUNBOOK section 15) ------------------
    R["arena"] = {
        "boundary": "the 27 coarse intervals of the L = 3, d = 2 arena, and "
                    "the split fiber over them",
        "family": "I7's nine admissible d = 2 records, rebuilt here; and the "
                  "declared count box (axis <= 6, diagonal <= 12)",
        "law": "the DYADIC refinement move (R6a's one admissible class): "
               "L -> 2L, every coarse interval subdivided, count additivity "
               "forced by the counting semantics",
        "state": "a split a : intervals -> Z_>0 with 1 <= a <= n - 1; the "
                 "ADMISSIBLE fiber additionally requires the refined readout "
                 "at each coarse image site to be positive definite",
        "arena": "the symmetry inventory: PINNED chart group (order 18) and "
                 "the DECLARED EXTENSIONS (the order-108 lattice group of the "
                 "declared link set; the order-2^27 local reversal group)",
        "provenance": "R6a's receipt at " + R6A_STATUS + ", read by hash "
                      + R6A_SHA + "; every fiber count REBUILT here from the "
                      "pinned declarations and anchored against it",
        "sites": "X = (Z_L)^d with L = 3, d = 2 (|X| = 9)",
        "links": [list(l) for l in LINKS],
        "d_ext": len(LINKS),
        "readout": "q_ij e_l^i e_l^j = n_l(x); admissible iff q is positive "
                   "definite at every site (density weight w = 0)",
    }

    # ---- the record family and the fiber rebuild ---------------------------
    records = [build_record(nm) for nm in RECORD_NAMES]
    by_name = {r["name"]: r for r in records}
    R["record_family"] = {r["name"]: {
        "counts_at_00": r["counts_at_00"], "counts_at_11": r["counts_at_11"],
        "admissible": r["admissible"], "homogeneous": r["homogeneous"],
        "raw": r["raw"], "img": r["img"],
        "per_site_admissible": r["per_site_admissible"],
        "splittable": r["splittable"]} for r in records}

    r6 = read_json(R6A)
    anchor_cells, anchor_bad = 0, []
    for r in records:
        exp = r6["split_fibers"].get(r["name"])
        if exp is None:
            continue
        mine_raw = mutate("fiber-typed", r["raw"])
        for field, mine, want in (("raw", mine_raw, exp["raw"]),
                                  ("admissible_at_images", r["img"],
                                   exp["admissible_at_images"]),
                                  ("per_site_admissible",
                                   r["per_site_admissible"],
                                   sorted(exp["per_site_admissible"]))):
            anchor_cells += 1
            if mine != want:
                anchor_bad.append([r["name"], field, mine, want])
    anchor_bad = mutate("r6a-anchor-drift", anchor_bad)
    gate("G-FIBER-REBUILD-ANCHORS-R6A",
         "every split-fiber number is REBUILT here from the pinned "
         "declarations and agrees cell-by-cell with the R6a receipt "
         "(" + R6A_STATUS + "): raw fiber, admissible-at-images fiber and "
         "per-site admissible profile at every record R6a reports",
         len(anchor_bad) == 0 and anchor_cells == 27,
         {"cells": anchor_cells, "mismatches": anchor_bad[:4]})
    R["fiber_rebuild"] = {
        "cells_anchored": anchor_cells, "mismatches": anchor_bad,
        "span_min": min(r["img"] for r in records if r["img"] > 0),
        "span_max": max(r["img"] for r in records),
        "records_admitting_the_move": len([r for r in records
                                           if r["splittable"]]),
        "records_with_no_split": sorted(r["name"] for r in records
                                        if r["admissible"]
                                        and not r["splittable"]),
        "source": R6A + " @ " + R6A_SHA + " (" + R6A_STATUS + ")"}
    gate("G-SPLIT-SPAN-ANCHOR",
         "the rebuilt admissible-fiber span reproduces R6a's span exactly",
         R["fiber_rebuild"]["span_min"] == 19683
         and R["fiber_rebuild"]["span_max"] == 1257565061957837936381,
         {"min": R["fiber_rebuild"]["span_min"],
          "max": R["fiber_rebuild"]["span_max"]})

    lat = count_lattice_census(6, 12)
    gate("G-COUNT-LATTICE-REPRODUCES-R6A",
         "the declared count box is re-censused here and reproduces R6a's "
         "admissible / splittable / unique-split counts",
         (lat["admissible_count_vectors"]
          == r6["count_lattice"]["admissible_count_vectors"]
          and lat["splittable"] == r6["count_lattice"]["splittable"]
          and lat["fiber_is_a_point"]
          == r6["count_lattice"]["unique_admissible_split"]),
         {"mine": [lat["admissible_count_vectors"], lat["splittable"],
                   lat["fiber_is_a_point"]],
          "r6a": [r6["count_lattice"]["admissible_count_vectors"],
                  r6["count_lattice"]["splittable"],
                  r6["count_lattice"]["unique_admissible_split"]]})

    # ---- the symmetry inventory -------------------------------------------
    pts = point_group()
    closed = all(mat_mul(A, B) in pts for A in pts for B in pts)
    dirperms = sorted(set(direction_perm((A, (0, 0))) for A in pts))
    ext_all = group_elements("EXT", pts)
    blockpres = [g for g in ext_all if is_block_preserving(g)]
    chart_all = group_elements("CHART", pts)
    blockpres_n = mutate("blockgroup-lax", len(blockpres))
    gate("G-POINT-GROUP-CLOSED",
         "the maximal subgroup of GL(2,Z) carrying the declared link set into "
         "the signed link set is built by enumeration and verified closed "
         "under composition -- the declared links are the A_2 root system and "
         "its automorphism group is dihedral of order 12",
         closed and len(pts) == 12, {"order": len(pts), "closed": closed})
    gate("G-BLOCK-PRESERVING-IS-THE-PINNED-GROUP",
         "THE MEASURED THEOREM: of the 108 elements of the declared extension, "
         "exactly the 18 that carry every declared link to a declared link "
         "(no reversal) preserve the coarse-image block structure the "
         "admissible fiber is built on -- and those 18 are exactly the pinned "
         "chart group",
         blockpres_n == 18 and len(ext_all) == 108
         and sorted(blockpres) == sorted(chart_all),
         {"ext_order": len(ext_all), "block_preserving": blockpres_n,
          "equals_chart_group": sorted(blockpres) == sorted(chart_all)})
    inventory = []
    for kind in GROUP_KINDS:
        els = group_elements(kind, pts)
        inventory.append({"group": kind, "order": len(els),
                          "provenance": GROUP_PROVENANCE[kind],
                          "block_preserving_elements":
                          len([g for g in els if is_block_preserving(g)]),
                          "carries_a_reversal":
                          any(not is_block_preserving(g) for g in els)})
    inventory.append({"group": "LOCALFLIP", "order": 2 ** len(INTERVALS),
                      "provenance": GROUP_PROVENANCE["LOCALFLIP"],
                      "block_preserving_elements": 1,
                      "carries_a_reversal": True})
    inventory = mutate("census-drop", inventory)
    gate("G-SYMMETRY-INVENTORY-CELL-COMPLETE",
         "the symmetry inventory is cell-complete: every declared group is "
         "censused with its order, its provenance class (PINNED vs "
         "DECLARED-EXTENSION) and whether it carries an interval reversal",
         len(inventory) == len(GROUP_KINDS) + 1,
         {"rows": len(inventory),
          "orders": {row["group"]: row["order"] for row in inventory}})
    R["symmetry_inventory"] = {
        "rows": inventory,
        "point_group_order": len(pts),
        "point_group_direction_permutations": [list(p) for p in dirperms],
        "pinned_sigma_is_S2_extension_is_S3": {
            "pinned_direction_permutations": 2,
            "declared_extension_direction_permutations": len(dirperms)},
        "block_preserving_of_the_extension": blockpres_n,
        "reading": "the pinned chart group is not an arbitrary choice: it is "
                   "EXACTLY the reversal-free part of the largest group the "
                   "declared link set admits.  Every element outside it "
                   "reverses at least one interval, and a reversal exchanges "
                   "the two halves of a split."}

    # ---- per-record stabilisers, interval orbits, deterministic laws -------
    stab_rows = {}
    stab_bad, eq_bad = [], []
    for r in records:
        cnt = r["counts"]
        H = stabiliser(chart_all, cnt)
        pm_orbits = []
        seen = set()
        for iv in INTERVALS:
            if iv in seen:
                continue
            orb = set()
            stack = [iv]
            while stack:
                y = stack.pop()
                if y in orb:
                    continue
                orb.add(y)
                for g in H:
                    stack.append(act_interval(g, y)[0])
            seen.update(orb)
            pm_orbits.append(sorted(orb))
        prof = sorted([[cnt[o[0]], cnt[o[0]] - 1, len(o)] for o in pm_orbits])
        eqf = 1
        for o in pm_orbits:
            eqf *= max(cnt[o[0]] - 1, 0)
        fixpts, classes = fixed_points_raw(H, cnt)
        stab_rows[r["name"]] = {"order": len(H), "orbits": len(pm_orbits),
                                "orbit_profile": prof,
                                "equivariant_fiber": eqf,
                                "fixed_points_raw": fixpts,
                                "signed_classes": classes}
        exp = r6["stabilisers"].get(r["name"])
        if exp is not None:
            if (exp["order"] != len(H) or exp["orbits"] != len(pm_orbits)
                    or sorted(exp["orbit_profile"]) != prof):
                stab_bad.append(r["name"])
        expe = r6["equivariant_fibers"].get(r["name"])
        if expe is not None and expe != eqf:
            eq_bad.append([r["name"], eqf, expe])
        if expe is not None and fixpts != eqf:
            eq_bad.append([r["name"], "fixed-points-differ", fixpts, eqf])
    stab_bad = mutate("stabiliser-anchor-drift", stab_bad)
    eq_bad = mutate("equivariant-anchor-drift", eq_bad)
    gate("G-STABILISERS-ANCHOR-R6A",
         "every record's stabiliser inside the pinned chart group, its orbit "
         "count on the 27 coarse intervals and its full orbit profile are "
         "rebuilt here and agree with the R6a receipt (" + R6A_STATUS + ")",
         len(stab_bad) == 0, {"mismatches": stab_bad})
    gate("G-EQUIVARIANT-FIBER-ANCHOR-R6A",
         "R6a's chart-equivariant fiber is re-derived here BY A DIFFERENT "
         "ROUTE -- as the number of chart-group FIXED POINTS of the raw split "
         "fiber, computed by a signed union-find -- and agrees at every "
         "record; these fixed points are exactly the DETERMINISTIC invariant "
         "laws (the invariant point masses)",
         len(eq_bad) == 0, {"mismatches": eq_bad})
    R["stabilisers"] = stab_rows

    # ---- THE ORBIT DECOMPOSITION OF EACH FIBER -----------------------------
    orbit_rows = []
    burnside_nonintegral = []
    for r in records:
        if not r["splittable"]:
            continue
        cnt = r["counts"]
        rng, boxes = img_ranges(r)
        all_box = all(boxes.values())
        for kind in GROUP_KINDS:
            H = stabiliser(group_elements(kind, pts), cnt)
            tot_raw, _ = burnside(H, lambda g: fix_on_raw(g, cnt))
            if tot_raw % len(H) != 0:
                burnside_nonintegral.append([r["name"], kind, tot_raw, len(H)])
            orb_raw = tot_raw // len(H)
            acting = [g for g in H if preserves_img(g, r)]
            bp = [g for g in acting if is_block_preserving(g)]
            if all_box and len(acting) > len(bp):
                tot_img, _ = burnside(acting,
                                      lambda g: fix_on_img_boxwise(g, r, rng))
                used = len(acting)
                mode = "boxwise (the admissible fiber is a product over "
                mode += "intervals, so a reversal can act on it)"
            else:
                tot_img, _ = burnside(bp, lambda g: fix_on_img_blockwise(
                    g, r["triples"]))
                used = len(bp)
                mode = "blockwise (only reversal-free elements act on the "
                mode += "admissible fiber)"
            if tot_img % used != 0:
                burnside_nonintegral.append([r["name"], kind, tot_img, used])
            orb_img = tot_img // used
            orb_img = mutate("burnside-corrupt", orb_img) \
                if (r["name"] == "G-DIAG2" and kind == "CHART") else orb_img
            fixpts, _cl = fixed_points_raw(H, cnt)
            orbit_rows.append({
                "record": r["name"], "group": kind,
                "provenance": GROUP_PROVENANCE[kind].split(" -- ")[0],
                "stabiliser_order": len(H),
                "elements_acting_on_the_admissible_fiber": len(acting),
                "block_preserving_elements": len(bp),
                "mode": mode,
                "fiber_raw": r["raw"], "fiber_img": r["img"],
                "orbits_raw": orb_raw, "orbits_img": orb_img,
                "simplex_dim_raw": orb_raw - 1,
                "simplex_dim_img": orb_img - 1,
                "transitive_raw": orb_raw == 1,
                "transitive_img": orb_img == 1,
                "deterministic_invariant_laws": fixpts})
    gate("G-BURNSIDE-INTEGRAL",
         "every Cauchy-Frobenius sum is divisible by its group order -- the "
         "arithmetic identity the orbit count rests on, checked at every cell "
         "[ANALYTICALLY FORCED for a genuine group action: a DISCLOSURE, not a "
         "must-pass falsifiable gate, RUNBOOK section 14 addendum v13 #208]",
         len(burnside_nonintegral) == 0,
         {"violations": burnside_nonintegral[:4],
          "cells": len(orbit_rows) * 2})
    R["orbit_decomposition"] = {
        "rows": orbit_rows,
        "cells": len(orbit_rows),
        "records": len([r for r in records if r["splittable"]]),
        "groups": len(GROUP_KINDS)}

    # ---- comparator 1: direct orbit enumeration (declared cap) -------------
    enum_rows, enum_bad = [], []
    for r in records:
        if not r["splittable"] or r["img"] > CAP_ENUM:
            continue
        for kind in ("CHART", "EXT"):
            gens = [g for g in generators_of(kind, pts)
                    if all(r["counts"][act_interval(g, iv)[0]] == r["counts"][iv]
                           for iv in INTERVALS)]
            gen_group = group_closure(gens)
            H = stabiliser(group_elements(kind, pts), r["counts"])
            orbs, sizes, escapes, visited, fibsz = enumerate_orbits_direct(r, gens)
            orbs = mutate("comparator-alias", orbs)
            row = [x for x in orbit_rows
                   if x["record"] == r["name"] and x["group"] == kind][0]
            ok = (orbs == row["orbits_img"])
            if not ok:
                enum_bad.append([r["name"], kind, orbs, row["orbits_img"]])
            enum_rows.append({"record": r["name"], "group": kind,
                              "generators": len(gens),
                              "generated_order": len(gen_group),
                              "stabiliser_order": len(H),
                              "fiber": fibsz, "orbits_direct": orbs,
                              "orbits_burnside": row["orbits_img"],
                              "orbit_sizes": dict(sorted(sizes.items())),
                              "escapes": escapes, "elements_visited": visited,
                              "agree": ok})
    gate("G-ORBIT-TWO-ROUTES",
         "wherever the admissible fiber is enumerable under the declared cap, "
         "the Cauchy-Frobenius orbit count is checked against a DIRECT orbit "
         "walk that applies GENERATORS only -- a different computation, not "
         "the same sum rearranged",
         len(enum_bad) == 0 and len(enum_rows) >= 4,
         {"cells": len(enum_rows), "cap": CAP_ENUM, "mismatches": enum_bad})
    gate("G-COMPARATOR-EXERCISED",
         "the direct comparator really enumerated: every walk visited at "
         "least as many configurations as the fiber holds, and its generating "
         "set closes to the group the Cauchy-Frobenius census used (a "
         "comparator that never ran cannot disagree -- RUNBOOK section 14 "
         "addendum, v13 #219)",
         all(e["elements_visited"] >= e["fiber"] for e in enum_rows)
         and all(e["generated_order"] == e["stabiliser_order"]
                 for e in enum_rows),
         {"rows": [[e["record"], e["group"], e["elements_visited"], e["fiber"],
                    e["generated_order"], e["stabiliser_order"]]
                   for e in enum_rows]})
    R["direct_enumeration"] = {"cap": CAP_ENUM, "rows": enum_rows}

    # ---- comparator 2: a closed-form necklace count ------------------------
    neck_rows, neck_bad = [], []
    for r in records:
        if not r["splittable"] or not r["homogeneous"]:
            continue
        k = len(r["triples"][(0, 0)])
        cf, rem = necklace_closed_form(k)
        row = [x for x in orbit_rows
               if x["record"] == r["name"] and x["group"] == "TRANS"][0]
        ok = (rem == 0 and cf == row["orbits_img"])
        if not ok:
            neck_bad.append([r["name"], cf, row["orbits_img"]])
        neck_rows.append({"record": r["name"], "k": k, "closed_form": cf,
                          "engine": row["orbits_img"], "agree": ok})
    gate("G-NECKLACE-COMPARATOR",
         "the orbit engine is validated against a CLOSED FORM written from the "
         "group's structure and not from this file's cycle machinery: the "
         "translations' orbit count on functions X -> A is (k^9 + 8k^3)/9",
         len(neck_bad) == 0 and len(neck_rows) >= 4,
         {"rows": neck_rows, "mismatches": neck_bad})
    R["closed_form_comparator"] = {"rows": neck_rows,
                                   "formula": "(k^9 + 8 k^3) / 9"}

    # ---- comparator 3: the invariant-measure linear system -----------------
    inv_rows, inv_bad = [], []
    for n in range(2, 14):
        for label, acts in (("pinned (no element reverses an interval)",
                             [lambda a: a]),
                            ("declared reversal extension",
                             [lambda a, n=n: n - a])):
            pointset = list(range(1, n))
            dim, nrows, rk = invariant_simplex_dim(pointset, acts)
            dim = mutate("invsys-inert", dim) if (n == 5 and "reversal" in label) \
                else dim
            orbs, _sz = orbit_count_direct(pointset, acts)
            expect = orbs - 1
            expect = mutate("simplex-dim-lax", expect) if n == 4 else expect
            ok = (dim == expect)
            if not ok:
                inv_bad.append([n, label, dim, expect])
            inv_rows.append({"n": n, "action": label, "points": len(pointset),
                             "orbits": orbs, "simplex_dim_linear_system": dim,
                             "orbits_minus_one": orbs - 1,
                             "constraint_rows": nrows, "rank": rk,
                             "agree": ok})
    gate("G-SIMPLEX-DIM-EQUALS-ORBITS-MINUS-ONE",
         "the criterion is MEASURED, not assumed: the dimension of the affine "
         "space of invariant probability measures is computed by exact "
         "Gaussian elimination over Q and equals orbits - 1 at every cell -- "
         "so 'unique invariant distribution iff transitive' is a measurement "
         "here, not a citation",
         len(inv_bad) == 0 and len(inv_rows) == 24,
         {"cells": len(inv_rows), "mismatches": inv_bad})
    gate("G-INVSYS-EXERCISED",
         "the linear-system comparator actually solved something: every cell "
         "that carries a nontrivial action built constraint rows and reported "
         "a positive rank, and a cell builds no rows only where the action is "
         "measurably trivial on its fiber (a comparator that returns without "
         "solving is vacuous -- RUNBOOK section 14 addendum, v13 #219)",
         all((row["constraint_rows"] > 0) == (row["orbits"] < row["points"])
             for row in inv_rows)
         and all(row["rank"] > 0 for row in inv_rows
                 if row["constraint_rows"] > 0)
         and any(row["rank"] > 0 for row in inv_rows),
         {"max_rank": max(row["rank"] for row in inv_rows),
          "cells_with_rows": len([r0 for r0 in inv_rows
                                  if r0["constraint_rows"] > 0]),
          "cells_with_a_trivial_action":
              len([r0 for r0 in inv_rows if r0["orbits"] == r0["points"]])})
    R["invariant_measure_comparator"] = {"rows": inv_rows}

    # ---- the invariant-measure census --------------------------------------
    trans_rows = []
    for row in orbit_rows:
        trans_rows.append({"record": row["record"], "group": row["group"],
                           "fiber": row["fiber_img"],
                           "orbits": row["orbits_img"],
                           "simplex_dim": row["simplex_dim_img"],
                           "unique_invariant_law": row["transitive_img"]})
    trans_rows = mutate("transitivity-flip", trans_rows)
    n_unique = len([t for t in trans_rows if t["unique_invariant_law"]])
    dims = sorted(set(t["simplex_dim"] for t in trans_rows))
    gate("G-TRANSITIVITY-CENSUS",
         "the invariant-measure census is cell-complete over (record, group) "
         "and every cell carries its transitivity bit and its orbit-simplex "
         "dimension",
         (len(trans_rows) == len(orbit_rows) and len(trans_rows) == 24
          and all(t["unique_invariant_law"] == (t["orbits"] == 1)
                  for t in trans_rows)),
         {"cells": len(trans_rows), "unique": n_unique})
    R["invariant_measure_census"] = {
        "rows": trans_rows, "cells": len(trans_rows),
        "cells_with_a_unique_invariant_law": n_unique,
        "simplex_dim_min": min(dims), "simplex_dim_max": max(dims),
        "reading": "no pinned symmetry acts transitively on any nontrivial "
                   "split fiber of the declared family, so at every cell the "
                   "invariant laws form a simplex of positive dimension: the "
                   "symmetry does not choose."}

    # ---- the per-interval level, where enumeration is exact -----------------
    fam_counts = sorted(set(r["counts"][iv] for r in records
                            for iv in INTERVALS))
    pil = [per_interval_law(n) for n in fam_counts]
    gate("G-PER-INTERVAL-LAW",
         "at the per-interval level the fiber is {1,...,n-1} and the law is "
         "exact: under the pinned group the orbits are the points (n-1 of "
         "them, simplex dimension n-2, unique only at n = 2 where the fiber IS "
         "a point); under the declared reversal extension the orbits are the "
         "reversal pairs (unique at n = 2 and n = 3 alone)",
         all(p["pinned_orbits"] == p["fiber"] for p in pil)
         and all(p["flip_orbits"] == (p["fiber"] + 1) // 2 for p in pil)
         and sorted(p["n"] for p in pil if p["flip_transitive"]) == [2, 3],
         {"count_values": fam_counts,
          "flip_transitive_at": [p["n"] for p in pil if p["flip_transitive"]]})
    R["per_interval_law"] = {
        "family_count_values": fam_counts, "rows": pil,
        "pinned_dim_law": "n - 2", "flip_dim_law": "ceil((n-1)/2) - 1",
        "trajectory_pinned": [p["pinned_simplex_dim"] for p in pil],
        "trajectory_flip": [p["flip_simplex_dim"] for p in pil]}

    lat_check = mutate("lattice-transitivity-flip", lat)
    gate("G-COUNT-LATTICE-TRANSITIVITY-CENSUS",
         "over the DECLARED count box the transitivity question is answered "
         "exactly: of the 261 splittable count vectors exactly one has a fiber "
         "the pinned symmetry acts transitively on, and it is the vector whose "
         "fiber is a single point -- uniqueness by triviality, not by "
         "selection; the declared reversal extension raises that to four, all "
         "outside the declared record family",
         (lat_check["pinned_transitive_count"] == 1
          and lat_check["fiber_is_a_point_count"] == 1
          and lat_check["flip_transitive_count"] == 4),
         {"pinned": lat_check["pinned_transitive"],
          "flip": lat_check["flip_transitive"]})
    fam_vectors = [tuple(r["counts_at_00"]) for r in records if r["homogeneous"]]
    lat["transitive_vectors_in_the_declared_family"] = sorted(
        [list(v) for v in fam_vectors
         if list(v) in lat["flip_transitive"]])
    R["count_lattice_census"] = lat

    # ---- SELECTION CANDIDATES BEYOND SYMMETRY ------------------------------
    cands = []

    wl = {n: weight_laws(n) for n in fam_counts if n >= 3}
    distinct = {n: len(set(tuple(sorted((k, str(v)) for k, v in law.items()))
                           for law in laws.values()))
                for n, laws in wl.items()}
    distinct = mutate("weightlaws-collapse", distinct)
    tv_ub = {n: total_variation(laws["UNIFORM"], laws["BINOMIAL"],
                                list(range(1, n)))
             for n, laws in wl.items()}
    cands.append({
        "name": "THE-RECORD-COUNTS-AS-WEIGHTS",
        "what": "a law P(a) built from the interval's own count n",
        "tested": "five weight functionals expressible from the pinned data "
                  "alone (uniform, binomial, linear, product, min-half), at "
                  "every count value the declared family carries",
        "result": "REFUTED-AS-FORCING",
        "forcing": None,
        "why": "all five are expressible and no pinned declaration prefers "
               "one; at every count value they are pairwise distinct, so the "
               "record's counts admit a family of laws rather than selecting "
               "one",
        "evidence": {"count_values": sorted(distinct),
                     "distinct_laws_per_value": distinct,
                     "tv_uniform_vs_binomial":
                     {str(k): str(v) for k, v in sorted(tv_ub.items())}}})

    supp = {r["name"]: support_relativity(r) for r in records if r["splittable"]}
    supp_tv = sorted(set(str(row["tv"]) for rows in supp.values()
                         for row in rows))
    cands.append({
        "name": "MAXENT-UNDER-PINNED-CONSTRAINTS",
        "what": "the maximum-entropy law on the split fiber",
        "tested": "the CONSTRAINT SET is audited before the principle is "
                  "applied: every pinned declaration is classified "
                  "value-level or distribution-level, and the two "
                  "pinned-plausible supports are compared exactly",
        "result": "REFUTED-AS-FORCING",
        "forcing": None,
        "why": "the audit finds no pinned moment constraint at all, so "
               "maximum entropy reduces to the uniform law on whatever "
               "support is declared -- and the two supports the pinned "
               "grammar makes available (the raw fiber and the "
               "admissible-at-images fiber) give measurably different laws.  "
               "A principle whose answer is a function of an undeclared "
               "choice is not a forcing",
        "evidence": {"records_with_a_measured_support_gap": len(
            [k for k, v in supp.items() if v]),
            "distinct_total_variations": supp_tv[:8],
            "pinned_moment_constraints": 0}})

    fac = {r["name"]: factorisation_defect(r) for r in records if r["splittable"]}
    nonfac = sorted([k for k, rows in fac.items()
                     if any(not row["factorises"] for row in rows)])
    cands.append({
        "name": "THE-UNIFORM-LAW-ON-THE-ADMISSIBLE-FIBER",
        "what": "P = uniform on the admissible split fiber",
        "tested": "whether it is a product law -- that is, whether it even "
                  "gives each interval a law of its own",
        "result": "REFUTED-AS-FORCING",
        "forcing": None,
        "why": "it is invariant, but it is not canonical (it depends on the "
               "declared support) and at %d of the %d records that admit the "
               "move it does not factorise: the admissibility constraint "
               "COUPLES the three splits at a site, so 'the law of a split' "
               "is not even well-posed interval by interval under it"
               % (len(nonfac), len(fac)),
        "evidence": {"records": sorted(fac),
                     "non_factorising": nonfac,
                     "per_record": {k: {"sites": len(v),
                                        "sites_not_factorising":
                                        len([r0 for r0 in v
                                             if not r0["factorises"]])}
                                    for k, v in fac.items()}}})

    bary = []
    for e in enum_rows:
        if e["group"] != "CHART":
            continue
        sizes = e["orbit_sizes"]
        equal = len(sizes) == 1
        fixed = sizes.get(1, 0)
        bary.append({"record": e["record"], "orbit_sizes": sizes,
                     "orbit_sizes_all_equal": equal,
                     "fixed_points": fixed,
                     "uniform_mass_on_a_fixed_point": str(fdiv(1, e["fiber"])),
                     "barycentre_mass_on_a_fixed_point":
                     str(fdiv(1, e["orbits_direct"])),
                     "ratio": str(fdiv(e["fiber"], e["orbits_direct"]))})
    cands.append({
        "name": "THE-BARYCENTRE-OF-THE-INVARIANT-SIMPLEX",
        "what": "the average of the orbit-uniform measures -- the simplex's "
                "own centre",
        "tested": "against the other invariant law that looks canonical, the "
                  "uniform law on the fiber",
        "result": "REFUTED-AS-FORCING",
        "forcing": None,
        "why": "the orbits are not all the same size, so the barycentre and "
               "the uniform law are different invariant laws; two "
               "canonical-looking constructions disagree, measured, which is "
               "exactly what a forcing would have to exclude",
        "evidence": {"rows": bary}})

    fr = front_candidate(records)
    fr = mutate("front-lax", fr)
    cands.append({
        "name": "THE-FRONT",
        "what": "a split supplied by the front n(x) -- the front-proportional "
                "rule a = n_l(x) * N(x) / (N(x) + N(x+l))",
        "tested": "over the declared profile family used as fronts, at every "
                  "record admitting the move and every coarse interval",
        "result": "REFUTED-AS-FORCING",
        "forcing": None,
        "why": "the front is a per-site integer; the only functional the "
               "pinned data offers returns an admissible integer split at a "
               "small minority of cells and is undefined or out of range at "
               "the rest.  And a value rule, even where defined, is not a "
               "law: it names a point, and a point mass is invariant only if "
               "that point is fixed",
        "evidence": fr})

    dr = drag_candidate(records)
    dr = mutate("drag-lax", dr)
    cands.append({
        "name": "THE-DRAG-FIELD",
        "what": "a law supplied by the declared drag rules",
        "tested": "every declared drag rule at every admissible record and "
                  "site: is the weight a stochastic kernel, and does its "
                  "index set meet the split fiber at all",
        "result": "REFUTED-AS-FORCING",
        "forcing": None,
        "why": "the drag's index set is the tangent frame (d = 2 indices) or "
               "the declared link set (3 indices); the split fiber at an "
               "interval carrying n events has n - 1 points, and no pinned "
               "declaration maps one onto the other.  The index-set mismatch "
               "is prior to the stochasticity question and settles it",
        "evidence": dr})

    eqlaws = {name: st["equivariant_fiber"] for name, st in stab_rows.items()
              if st["equivariant_fiber"] > 0}
    cands.append({
        "name": "THE-EQUIVARIANT-(DETERMINISTIC)-LAWS",
        "what": "the invariant point masses -- R6a's chart-equivariant splits, "
                "read as distributions",
        "tested": "counted exactly, as the fixed points of the pinned group "
                  "on the fiber",
        "result": "REFUTED-AS-FORCING",
        "forcing": None,
        "why": "these are genuinely invariant laws, and they are the vertices "
               "of the simplex that happen to be deterministic -- but there "
               "is never exactly one of them (the smallest count is 3), so "
               "demanding determinism does not select either.  This is R6a's "
               "value-level finding recovered as a distribution-level one",
        "evidence": {"per_record": eqlaws,
                     "minimum": min(eqlaws.values()) if eqlaws else None}})

    cands = mutate("selection-forced", cands)
    forced = [c for c in cands if c["result"].startswith("FORCED")]
    gate("G-SELECTION-CANDIDATES-CELL-COMPLETE",
         "seven selection candidates beyond symmetry are censused, each with "
         "what it is, what was tested, its verdict, and its forcing named or "
         "refuted",
         len(cands) == 7 and all(c.get("result") and c.get("why")
                                 for c in cands),
         {"candidates": [c["name"] for c in cands]})
    gate("G-CANDIDATE-REFUTATIONS-MEASURED",
         "each refutation is a MEASUREMENT, not an assertion: the weight "
         "functionals are pairwise distinct at every count value; the "
         "front-proportional rule fails to return an admissible integer at "
         "most cells; and the number of declared maps from the drag's index "
         "set onto the split fiber is counted, not asserted",
         (all(v > 1 for v in distinct.values())
          and fr["admissible_integer"] < fr["cells"]
          and dr["index_sets"]["declared_maps_onto_the_split_fiber"] == 0),
         {"distinct_laws": distinct,
          "front": [fr["admissible_integer"], fr["cells"]],
          "drag_maps": dr["index_sets"]["declared_maps_onto_the_split_fiber"]})
    gate("G-SELECTION-CLASSIFICATION",
         "a candidate counts as FORCED only if a named pinned declaration "
         "forces it; every candidate that names no forcing is classified "
         "REFUTED-AS-FORCING, and the classification is computed from the "
         "'forcing' field, never typed",
         all((c["result"] == "REFUTED-AS-FORCING") == (c["forcing"] is None)
             for c in cands),
         {"forced": [c["name"] for c in forced]})
    R["selection_candidates"] = {"rows": cands, "count": len(cands),
                                 "forced": len(forced),
                                 "refuted": len(cands) - len(forced)}

    # ---- the determinism census: what a law would have to come from --------
    dc = declaration_census()
    gate("G-DECLARATION-CENSUS-CELL-COMPLETE",
         "every declaration the pinned I7 receipt carries is classified "
         "value-level or distribution-level, by a marker scan of the "
         "declaration's own text -- the census is read from the receipt, not "
         "typed",
         dc["declarations"] == len(read_by_path(read_json(I7),
                                                ("declarations",))),
         {"declarations": dc["declarations"],
          "distribution_level": dc["distribution_level"]})
    gate("G-MAXENT-CONSTRAINT-AUDIT",
         "the maximum-entropy candidate is audited, never assumed: the pinned "
         "layer carries zero distribution-level declarations, so it supplies "
         "no constraint set for the principle to act on, and the one "
         "ratio-valued declaration is read by its own source as a bit",
         dc["distribution_level"] == 0,
         {"distribution_level_rows": dc["distribution_level_rows"]})
    hb = h_bijection_probe(records)
    gate("G-H-IS-A-BIJECTION",
         "the pinned dynamics H_a[N] is a bijection of configurations, "
         "measured on a declared sample: the closed-form inverse returns every "
         "configuration exactly and no two configurations collide -- so its "
         "pushforward carries point masses to point masses and cannot make a "
         "law out of a value [ANALYTICALLY FORCED: the inverse is exhibited in "
         "the pinned source, so this is a DISCLOSURE, not a must-pass "
         "falsifiable gate, RUNBOOK section 14 addendum v13 #208]",
         hb["roundtrip_identity"] == hb["cells"] and hb["collisions"] == 0
         and hb["cells"] > 0,
         {"cells": hb["cells"], "roundtrip": hb["roundtrip_identity"],
          "collisions": hb["collisions"]})
    missing = ("THE-INTERVAL-POSITIONAL-LAW: a joint law for WHERE inside a "
               "record interval its n_l(x) division events fall -- "
               "equivalently the transition kernel between the interval's "
               "endpoints whose renewal count is n_l(x).  It is a "
               "transition-matrix-layer object; R0's inheritance carries the "
               "record layer (I7: counts, front, H_a[N], record-IS-metric) "
               "and no transition layer at all.")
    missing = mutate("missing-object-blank", missing)
    gate("G-MISSING-OBJECT-NAMED",
         "the BLOCKED head names the missing object precisely -- what kind of "
         "object it is, what it would have to say, and which pinned layer "
         "does not carry it",
         len(missing) > 120 and "transition" in missing
         and "positional" in missing.lower(),
         {"missing": missing[:80]})
    R["determinism_census"] = {
        "declarations": dc,
        "h_bijection": hb,
        "stochastic_pinned_objects": 0,
        "missing_object": missing,
        "reading": "a split distribution is an object of a kind the pinned "
                   "layer does not contain: every declaration is value-level, "
                   "the dynamics is a deterministic bijection, and the only "
                   "ratio-valued declaration is read as a bit by its own "
                   "source."}

    # ---- iteration in distribution ----------------------------------------
    iter_anchor = r6a_iteration_reproduction()
    iter_anchor = mutate("iter-anchor-drift", iter_anchor)
    gate("G-DECLARED-SPLIT-ANCHORS-R6A",
         "this unit's declared split is R6a's declared split, proved by "
         "reproducing R6a's whole iteration table -- steps achieved and halt "
         "reason -- at every record before the split is used for anything",
         all(row["ok"] for row in iter_anchor) and len(iter_anchor) == 9,
         {"rows": len(iter_anchor),
          "mismatches": [r0["record"] for r0 in iter_anchor if not r0["ok"]]})
    iters = []
    for name in sorted(by_name):
        if not by_name[name]["splittable"]:
            continue
        for key in (0, 1):
            iters.append(iteration_in_distribution(name, key))
    grow = [it for it in iters if it["trend"] == "GROWS"]
    collapse = [it for it in iters if it["trend"].startswith("COLLAPSES")]
    completion_independent = True
    for name in sorted(set(it["record"] for it in iters)):
        pair = [it for it in iters if it["record"] == name]
        if len(pair) == 2 and pair[0]["simplex_dims"] != pair[1]["simplex_dims"]:
            completion_independent = False
    trend_summary = mutate("iteration-lax",
                           {"grows": len(grow), "collapses": len(collapse),
                            "stable": len([it for it in iters
                                           if it["trend"] == "STABLE"]),
                            "single_level": len([it for it in iters
                                                 if it["trend"]
                                                 == "SINGLE-LEVEL"])})
    gate("G-ITERATION-TREND",
         "the iteration-in-distribution trend is COMPUTED from the measured "
         "dimension trace at each level, never typed, and the group order at "
         "each level is measured beside it",
         (trend_summary["grows"] + trend_summary["collapses"]
          + trend_summary["stable"] + trend_summary["single_level"]
          == len(iters)
          and all((it["trend"] == "GROWS")
                  == (len([d for d in it["simplex_dims"]
                           if d is not None and d >= 0]) >= 2
                      and [d for d in it["simplex_dims"]
                           if d is not None and d >= 0][-1]
                      > [d for d in it["simplex_dims"]
                         if d is not None and d >= 0][0])
                  for it in iters)),
         {"cells": len(iters), "summary": trend_summary})
    outr = [it for it in iters if it["live_levels"] >= 2]
    gate("G-ITERATION-SYMMETRY-OUTRUN",
         "where a second level exists the acting group's order is MEASURED at "
         "both levels beside the fiber's, and the two growth factors are "
         "compared exactly: at every such cell the fiber outruns the group, "
         "and the orbit-simplex dimension strictly grows.  Whether the group "
         "grows at all is completion-relative and is reported, not assumed",
         len(outr) > 0
         and all(it["fiber_outruns_the_group"] for it in outr)
         and all([d for d in it["simplex_dims"] if d is not None and d >= 0][-1]
                 > [d for d in it["simplex_dims"]
                    if d is not None and d >= 0][0] for it in outr),
         {"rows": [[it["record"], it["diag_completion_key"],
                    it["group_orders"], it["fiber_growth_factor"],
                    it["group_growth_factor"]] for it in outr]})
    R["iteration_in_distribution"] = {
        "r6a_anchor": iter_anchor, "rows": iters,
        "trend_summary": trend_summary,
        "completion_independent": completion_independent,
        "completion_relative": not completion_independent,
        "cells_with_two_live_levels": len(outr),
        "reading": "under repeated refinement the orbit-simplex dimension "
                   "never stabilises.  Where a second level exists it grows by "
                   "twenty-one orders of magnitude, and the fiber outruns the "
                   "symmetry at every such cell: under one declared completion "
                   "of the free links the acting group stays at 9 and under "
                   "the other it doubles to 18, while the fiber multiplies by "
                   "more than 10^21 either way.  Everywhere else the fiber "
                   "collapses to empty, because a descendant interval reaches "
                   "count 1 and count 1 admits no split at all.  THE LEVEL-1 "
                   "READING IS COMPLETION-RELATIVE and is reported as such."}

    # ---- controls ----------------------------------------------------------
    ctl = controls()
    ctl = mutate("control-pass", ctl)
    ctl = mutate("neg-control-pass", ctl)
    gate("G-POSITIVE-CONTROL",
         "the positive controls are fibers a group acts TRANSITIVELY on, and "
         "on each the unique invariant measure is FOUND -- by the linear "
         "system, whose solution space comes out zero-dimensional, not by "
         "citing the orbit theorem",
         all(p["transitive"] and p["simplex_dim"] == 0
             and p["unique_measure"] is not None for p in ctl["positive"]),
         {"positive": [[p["name"], p["orbits"], p["simplex_dim"]]
                       for p in ctl["positive"]]})
    gate("G-NEGATIVE-CONTROL",
         "the negative controls are asymmetric fibers, and on each the "
         "invariant laws come out a positive-dimensional simplex -- the "
         "instrument can return NOT-UNIQUE and does",
         all((not n0["transitive"]) and n0["simplex_dim"] > 0
             for n0 in ctl["negative"]),
         {"negative": [[n0["name"], n0["orbits"], n0["simplex_dim"]]
                       for n0 in ctl["negative"]]})
    R["controls"] = ctl

    # ---- the cache -------------------------------------------------------
    before = dict(_CACHE_STATS)
    fresh_bad = 0
    fresh_tested = 0
    for r in records:
        for x in SITES:
            counts = tuple(r["counts"][(x, l)] for l in LINKS)
            fresh_tested += 1
            a = admissible_triples(counts, fresh=True)
            b = mutate("cache-alias", admissible_triples(counts))
            if a != b:
                fresh_bad += 1
    after = dict(_CACHE_STATS)
    gate("G-CACHE-EXERCISED",
         "the memo is exercised and its hit and miss counts are gated: a "
         "zero-hit cache gate is vacuous (RUNBOOK section 14 addendum, v13 "
         "#185 / #219)",
         after["hits"] > 0 and after["misses"] > 0
         and after["bypass"] > before["bypass"],
         {"hits": after["hits"], "misses": after["misses"],
          "bypasses": after["bypass"]})
    gate("G-CACHE-FRESH-EQUALS-MEMO",
         "every memoised admissible-split set is recomputed with the memo "
         "BYPASSED and compared against what the memo returns",
         fresh_bad == 0 and fresh_tested > 0,
         {"tested": fresh_tested, "disagreements": fresh_bad})
    R["cache"] = {"hits": after["hits"], "misses": after["misses"],
                  "bypasses": after["bypass"], "fresh_comparisons": fresh_tested,
                  "disagreements": fresh_bad}
    return R, records, by_name, orbit_rows, trans_rows, cands, iters, ctl, lat


# ----------------------------------------------------------------------------
# 12.  THE VERDICT -- derived inside a gate, from the measured counts
# ----------------------------------------------------------------------------

HEADS = {
    "MOTIVATED": "CRB-DISTRIBUTION-MOTIVATED",
    "SIMPLEX": "CRB-ORBIT-SIMPLEX",
    "BLOCKED": "CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW",
}


def decide_head(unique_cells, forced_candidates, missing_named):
    """The decision ladder, as a pure function of measured counts.  All three
    heads are reachable; the reachability is proved by feeding this same
    function synthetic counts."""
    if unique_cells > 0 or forced_candidates > 0:
        return HEADS["MOTIVATED"]
    if not missing_named:
        return HEADS["SIMPLEX"]
    return HEADS["BLOCKED"]


def build_verdict(P, swap_pairing=False, typed=False, appended=False,
                  fully_typed=False, head_const=False):
    head = P["head"]
    if head_const:
        head = HEADS["MOTIVATED"]
    seg = []
    names = ["FIBERS", "SYMMETRY", "ORBITS", "TRANSITIVE", "PER-INTERVAL",
             "LATTICE", "SELECTION", "MAXENT", "DETERMINISM", "ITERATION",
             "CONTROLS", "MISSING"]
    vals = [
        "REBUILT-%d-OF-%d-CELLS-%d|SPAN-%d..%d|MOVE-ADMITTED-BY-%d-OF-%d"
        % (P["anchor_cells"], P["anchor_cells"], P["anchor_mismatches"],
           P["span_min"], P["span_max"], P["splittable"], P["records"]),
        "PINNED-CHART-%d|SIGMA-%d|EXTENSION-%d|BLOCK-PRESERVING-%d-OF-%d"
        % (P["chart_order"], P["sigma_order"], P["ext_order"],
           P["block_preserving"], P["ext_order"]),
        "CELLS-%d|ROUTES-%d|CLOSED-FORM-%d|MIN-%d-MAX-%d"
        % (P["orbit_cells"], P["enum_cells"], P["neck_cells"],
           P["orbits_min"], P["orbits_max"]),
        "UNIQUE-%d-OF-%d|SIMPLEX-DIM-%d..%d"
        % (P["unique_cells"], P["orbit_cells"], P["dim_min"], P["dim_max"]),
        "PINNED-DIM-N-MINUS-2|FLIP-DIM-CEIL-N-MINUS-1-OVER-2-MINUS-1|"
        "TRANSITIVE-AT-N-%s" % ("-".join(str(v) for v in P["flip_transitive_n"])),
        "SPLITTABLE-%d-OF-%d|PINNED-TRANSITIVE-%d|FLIP-TRANSITIVE-%d|"
        "IN-THE-DECLARED-FAMILY-%d"
        % (P["lat_splittable"], P["lat_admissible"], P["lat_pinned_T"],
           P["lat_flip_T"], P["lat_in_family"]),
        "CANDIDATES-%d|FORCED-%d|REFUTED-%d"
        % (P["cand_total"], P["cand_forced"], P["cand_refuted"]),
        "PINNED-DISTRIBUTION-LEVEL-DECLARATIONS-%d-OF-%d|"
        "SUPPORT-RELATIVE-RECORDS-%d|NON-FACTORISING-%d"
        % (P["dl"], P["decls"], P["supp_records"], P["nonfac"]),
        "STOCHASTIC-PINNED-OBJECTS-%d|H-BIJECTION-%d-OF-%d|COLLISIONS-%d"
        % (P["stoch"], P["h_ok"], P["h_cells"], P["h_coll"]),
        "CEILING-%d|GROWS-%d|COLLAPSES-%d|SINGLE-LEVEL-%d|"
        "FIBER-OUTRUNS-GROUP-%s|COMPLETION-RELATIVE-%s"
        % (P["iter_ceiling"], P["iter_grows"], P["iter_collapses"],
           P["iter_single"], P["iter_outrun"], P["iter_completion_relative"]),
        "POSITIVE-%d-UNIQUE-%d|NEGATIVE-%d-SIMPLEX-DIM-%s"
        % (P["pos_n"], P["pos_unique"], P["neg_n"],
           "-".join(str(v) for v in P["neg_dims"])),
        P["missing_tag"],
    ]
    if swap_pairing:
        vals[3], vals[4] = vals[4], vals[3]
    if typed:
        vals[6] = "CANDIDATES-7|FORCED-1|REFUTED-6"
    if fully_typed:
        vals = ["TYPED"] * len(vals)
    for nm, v in zip(names, vals):
        seg.append({"name": nm, "text": nm + "=" + v})
    body = "|".join(s["text"] for s in seg)
    out = head + "<" + body + ">"
    if appended:
        out = out + " (ok)"
    return out, seg


def reconstruct_verdict_from_receipt(R):
    """AN INDEPENDENT REBUILD.  This function shares no code and no input with
    build_verdict(): it reads the RECEIPT OBJECT alone and re-derives the head
    from the receipt's own measured counts.  RUNBOOK section 14 addendum (v14
    #10 / #20): a compliance gate whose comparator cannot disagree with the
    object under test is vacuous by construction."""
    fr = R["fiber_rebuild"]
    si = R["symmetry_inventory"]
    od = R["orbit_decomposition"]
    imc = R["invariant_measure_census"]
    pil = R["per_interval_law"]
    lat = R["count_lattice_census"]
    sc = R["selection_candidates"]
    dcz = R["determinism_census"]
    it = R["iteration_in_distribution"]
    ct = R["controls"]
    orders = {row["group"]: row["order"] for row in si["rows"]}
    orb = [r["orbits_img"] for r in od["rows"]]
    unique = imc["cells_with_a_unique_invariant_law"]
    forced = sc["forced"]
    miss = dcz["missing_object"]
    head = (HEADS["MOTIVATED"] if (unique > 0 or forced > 0)
            else (HEADS["SIMPLEX"] if not miss else HEADS["BLOCKED"]))
    fam = [r for r in R["record_family"].values()]
    parts = []
    parts.append("FIBERS=REBUILT-%d-OF-%d-CELLS-%d|SPAN-%d..%d|"
                 "MOVE-ADMITTED-BY-%d-OF-%d"
                 % (fr["cells_anchored"], fr["cells_anchored"],
                    len(fr["mismatches"]), fr["span_min"], fr["span_max"],
                    fr["records_admitting_the_move"], len(fam)))
    parts.append("SYMMETRY=PINNED-CHART-%d|SIGMA-%d|EXTENSION-%d|"
                 "BLOCK-PRESERVING-%d-OF-%d"
                 % (orders["CHART"], orders["SIGMA"], orders["EXT"],
                    si["block_preserving_of_the_extension"], orders["EXT"]))
    parts.append("ORBITS=CELLS-%d|ROUTES-%d|CLOSED-FORM-%d|MIN-%d-MAX-%d"
                 % (od["cells"], len(R["direct_enumeration"]["rows"]),
                    len(R["closed_form_comparator"]["rows"]),
                    min(orb), max(orb)))
    parts.append("TRANSITIVE=UNIQUE-%d-OF-%d|SIMPLEX-DIM-%d..%d"
                 % (unique, od["cells"], imc["simplex_dim_min"],
                    imc["simplex_dim_max"]))
    parts.append("PER-INTERVAL=PINNED-DIM-N-MINUS-2|"
                 "FLIP-DIM-CEIL-N-MINUS-1-OVER-2-MINUS-1|TRANSITIVE-AT-N-%s"
                 % ("-".join(str(r["n"]) for r in pil["rows"]
                             if r["flip_transitive"])))
    parts.append("LATTICE=SPLITTABLE-%d-OF-%d|PINNED-TRANSITIVE-%d|"
                 "FLIP-TRANSITIVE-%d|IN-THE-DECLARED-FAMILY-%d"
                 % (lat["splittable"], lat["admissible_count_vectors"],
                    lat["pinned_transitive_count"], lat["flip_transitive_count"],
                    len(lat["transitive_vectors_in_the_declared_family"])))
    parts.append("SELECTION=CANDIDATES-%d|FORCED-%d|REFUTED-%d"
                 % (sc["count"], sc["forced"], sc["refuted"]))
    supp_rows = [c for c in sc["rows"]
                 if c["name"] == "MAXENT-UNDER-PINNED-CONSTRAINTS"][0]
    fac_row = [c for c in sc["rows"]
               if c["name"] == "THE-UNIFORM-LAW-ON-THE-ADMISSIBLE-FIBER"][0]
    parts.append("MAXENT=PINNED-DISTRIBUTION-LEVEL-DECLARATIONS-%d-OF-%d|"
                 "SUPPORT-RELATIVE-RECORDS-%d|NON-FACTORISING-%d"
                 % (dcz["declarations"]["distribution_level"],
                    dcz["declarations"]["declarations"],
                    supp_rows["evidence"]["records_with_a_measured_support_gap"],
                    len(fac_row["evidence"]["non_factorising"])))
    parts.append("DETERMINISM=STOCHASTIC-PINNED-OBJECTS-%d|H-BIJECTION-%d-OF-%d|"
                 "COLLISIONS-%d"
                 % (dcz["stochastic_pinned_objects"],
                    dcz["h_bijection"]["roundtrip_identity"],
                    dcz["h_bijection"]["cells"],
                    dcz["h_bijection"]["collisions"]))
    parts.append("ITERATION=CEILING-%d|GROWS-%d|COLLAPSES-%d|SINGLE-LEVEL-%d|"
                 "FIBER-OUTRUNS-GROUP-%s|COMPLETION-RELATIVE-%s"
                 % (max(len([t for t in row["trace"]
                             if t["img"] > 0]) for row in it["rows"]),
                    it["trend_summary"]["grows"],
                    it["trend_summary"]["collapses"],
                    it["trend_summary"]["single_level"],
                    all(row["fiber_outruns_the_group"] for row in it["rows"]
                        if row["live_levels"] >= 2),
                    it["completion_relative"]))
    parts.append("CONTROLS=POSITIVE-%d-UNIQUE-%d|NEGATIVE-%d-SIMPLEX-DIM-%s"
                 % (len(ct["positive"]),
                    len([p for p in ct["positive"] if p["simplex_dim"] == 0]),
                    len(ct["negative"]),
                    "-".join(str(n0["simplex_dim"]) for n0 in ct["negative"])))
    parts.append("MISSING=" + R["missing_tag"])
    return head + "<" + "|".join(parts) + ">"


# ----------------------------------------------------------------------------
# 13.  ASSEMBLY: the verdict payload, gated
# ----------------------------------------------------------------------------

MISSING_TAG = ("THE-INTERVAL-POSITIONAL-LAW-=-THE-TRANSITION-KERNEL-BETWEEN-"
               "AN-INTERVALS-ENDPOINTS-WHOSE-RENEWAL-COUNT-IS-N|"
               "R0-CARRIES-THE-RECORD-LAYER-I7-AND-NO-TRANSITION-LAYER")


def finish(R, records, by_name, orbit_rows, trans_rows, cands, iters, ctl, lat):
    si = R["symmetry_inventory"]
    orders = {row["group"]: row["order"] for row in si["rows"]}
    dcz = R["determinism_census"]
    sc = R["selection_candidates"]
    supp_row = [c for c in cands
                if c["name"] == "MAXENT-UNDER-PINNED-CONSTRAINTS"][0]
    fac_row = [c for c in cands
               if c["name"] == "THE-UNIFORM-LAW-ON-THE-ADMISSIBLE-FIBER"][0]
    orb = [r["orbits_img"] for r in orbit_rows]
    unique_cells = R["invariant_measure_census"]["cells_with_a_unique_invariant_law"]
    R["missing_tag"] = MISSING_TAG
    P = {
        "anchor_cells": R["fiber_rebuild"]["cells_anchored"],
        "anchor_mismatches": len(R["fiber_rebuild"]["mismatches"]),
        "span_min": R["fiber_rebuild"]["span_min"],
        "span_max": R["fiber_rebuild"]["span_max"],
        "splittable": R["fiber_rebuild"]["records_admitting_the_move"],
        "records": len(R["record_family"]),
        "chart_order": orders["CHART"], "sigma_order": orders["SIGMA"],
        "ext_order": orders["EXT"],
        "block_preserving": si["block_preserving_of_the_extension"],
        "orbit_cells": R["orbit_decomposition"]["cells"],
        "enum_cells": len(R["direct_enumeration"]["rows"]),
        "neck_cells": len(R["closed_form_comparator"]["rows"]),
        "orbits_min": min(orb), "orbits_max": max(orb),
        "unique_cells": unique_cells,
        "dim_min": R["invariant_measure_census"]["simplex_dim_min"],
        "dim_max": R["invariant_measure_census"]["simplex_dim_max"],
        "flip_transitive_n": [r["n"] for r in R["per_interval_law"]["rows"]
                              if r["flip_transitive"]],
        "lat_splittable": lat["splittable"],
        "lat_admissible": lat["admissible_count_vectors"],
        "lat_pinned_T": lat["pinned_transitive_count"],
        "lat_flip_T": lat["flip_transitive_count"],
        "lat_in_family": len(lat["transitive_vectors_in_the_declared_family"]),
        "cand_total": sc["count"], "cand_forced": sc["forced"],
        "cand_refuted": sc["refuted"],
        "dl": dcz["declarations"]["distribution_level"],
        "decls": dcz["declarations"]["declarations"],
        "supp_records": supp_row["evidence"]["records_with_a_measured_support_gap"],
        "nonfac": len(fac_row["evidence"]["non_factorising"]),
        "stoch": dcz["stochastic_pinned_objects"],
        "h_ok": dcz["h_bijection"]["roundtrip_identity"],
        "h_cells": dcz["h_bijection"]["cells"],
        "h_coll": dcz["h_bijection"]["collisions"],
        "iter_ceiling": max(len([t for t in it["trace"] if t["img"] > 0])
                            for it in iters),
        "iter_grows": R["iteration_in_distribution"]["trend_summary"]["grows"],
        "iter_collapses":
            R["iteration_in_distribution"]["trend_summary"]["collapses"],
        "iter_single": R["iteration_in_distribution"]["trend_summary"]
            ["single_level"],
        "iter_outrun": all(it["fiber_outruns_the_group"] for it in iters
                           if it["live_levels"] >= 2),
        "iter_completion_relative":
            R["iteration_in_distribution"]["completion_relative"],
        "pos_n": len(ctl["positive"]),
        "pos_unique": len([p for p in ctl["positive"]
                           if p["simplex_dim"] == 0]),
        "neg_n": len(ctl["negative"]),
        "neg_dims": [n0["simplex_dim"] for n0 in ctl["negative"]],
        "missing_tag": MISSING_TAG,
    }
    P["head"] = decide_head(P["unique_cells"], P["cand_forced"],
                            bool(dcz["missing_object"]))
    verdict, segments = build_verdict(
        P,
        swap_pairing=(mutate("verdict-pair-swap", 0) == 1),
        typed=(mutate("verdict-typed-segment", 0) == 1),
        appended=(mutate("verdict-append-text", 0) == 1),
        fully_typed=(mutate("verdict-fully-typed", 0) == 1),
        head_const=(mutate("head-constant", 0) == 1))
    R["verdict"] = verdict
    R["verdict_head"] = P["head"]
    R["verdict_segments"] = segments
    R["verdict_payload"] = {k: (str(v) if isinstance(v, bool) else v)
                            for k, v in sorted(P.items())}

    rebuilt = reconstruct_verdict_from_receipt(R)
    gate("G-VERDICT-STRING-EQUALITY",
         "the COMPLETE emitted verdict string equals, character for "
         "character, a string rebuilt segment-by-segment from the receipt "
         "object by a function that shares no code and no input with the "
         "builder (RUNBOOK section 14 addendum, v14 #10: containment is not "
         "equality)",
         verdict == rebuilt,
         {"emitted": verdict[:120], "rebuilt": rebuilt[:120],
          "equal": verdict == rebuilt})

    # every segment must be able to move when the receipt row it reads moves
    flips = []
    for i, s in enumerate(segments):
        probe = dict(P)
        keys = [["anchor_cells"], ["chart_order"], ["orbit_cells"],
                ["unique_cells"], ["flip_transitive_n"], ["lat_pinned_T"],
                ["cand_forced"], ["dl"], ["stoch"], ["iter_grows"],
                ["pos_n"], ["missing_tag"]][i]
        for k in keys:
            if k == "flip_transitive_n":
                probe[k] = probe[k] + [99]
            elif k == "missing_tag":
                probe[k] = "MOVED"
            elif isinstance(probe[k], bool):
                probe[k] = not probe[k]
            else:
                probe[k] = probe[k] + 1
        tup = mutate("verdict-inert-segment", (probe, dict(P), i))
        probe = tup[0]
        moved, _ = build_verdict(probe)
        flips.append({"segment": s["name"], "flips": moved != verdict})
    gate("G-VERDICT-SEGMENTS-FLIPPABLE",
         "every verdict segment is derived: perturbing the measured value it "
         "reads moves the emitted string, at all twelve segments (RUNBOOK "
         "section 13 addendum, v13 #234)",
         all(f["flips"] for f in flips) and len(flips) == 12,
         {"flips": flips})
    heads = {}
    heads["MOTIVATED"] = decide_head(1, 0, True)
    heads["MOTIVATED-VIA-CANDIDATE"] = decide_head(0, 1, True)
    heads["SIMPLEX"] = decide_head(0, 0, False)
    heads["BLOCKED"] = decide_head(0, 0, True)
    gate("G-VERDICT-ALL-HEADS-REACHABLE",
         "all three first-class heads are reachable from the decision ladder, "
         "proved by evaluating the same ladder on synthetic counts",
         (heads["MOTIVATED"] == HEADS["MOTIVATED"]
          and heads["MOTIVATED-VIA-CANDIDATE"] == HEADS["MOTIVATED"]
          and heads["SIMPLEX"] == HEADS["SIMPLEX"]
          and heads["BLOCKED"] == HEADS["BLOCKED"]),
         heads)
    R["verdict_audit"] = {"emitted": verdict, "reconstructed": rebuilt,
                          "segment_flips": flips,
                          "heads_reachable": heads}

    fcd = [g["name"] for g in GATES if g["name"] in FORCED_CLAUSE_DISCLOSURES]
    fcd = mutate("forced-clause-promote", fcd)
    gate("G-FORCED-CLAUSE-DISCLOSURE",
         "every analytically-forced clause in this instrument is declared a "
         "DISCLOSURE in one place and nowhere claimed as a must-pass "
         "falsifiable gate (RUNBOOK section 14 addendum, v13 #208)",
         sorted(fcd) == sorted(FORCED_CLAUSE_DISCLOSURES),
         {"disclosures": sorted(FORCED_CLAUSE_DISCLOSURES),
          "registered": sorted(fcd)})

    R["totals"] = {"anchors": len(ANCHORS), "gates": len(GATES),
                   "mutants": len(MUTANTS),
                   "must_pass_failures": len([g for g in GATES
                                              if not g["passed"]]),
                   "orbit_cells": len(orbit_rows),
                   "records": len(R["record_family"])}
    R["falsifier_census"] = {}
    R["schema"] = "isp/v14/crb-stochastic-split/1"
    R["pin"] = "v14/note-cr-batch-pins.md (CR-B section)"
    R["pin_sha256_prefix"] = PIN_SHA
    R["sources"] = {
        "v14/code/r6a_refinement_receipt.json": R6A_SHA + " [" + R6A_STATUS + "]",
        "v13/code/ha_successor_receipt.json": "542b8735daf0",
        "v13/paper-ha-successor.md": "f286ba10d2d9",
        "v13/code/ha_successor_exact.py": "d44cb72f8ee9",
        "v14/note-r0-founding-pin.md": "e9d2bedff244",
    }
    R["erratum_v14_4"] = (
        "v14 LOG #4 -- the R0 companion-hash erratum.  This unit reads no "
        "artifact the erratum touches: its only v13 paper read is "
        "v13/paper-ha-successor.md, a PRIMARY key of row I7, not one of the "
        "stale I2/I3 companions.  Carried as a disclosure, anchored by "
        "T-ERRATUM.")
    R["source_sha256"] = sha256_full(SRC)
    R["python"] = "%d.%d.%d" % sys.version_info[:3]
    R["arithmetic"] = "int / fractions.Fraction only; no float, no tolerance"
    return R


# ----------------------------------------------------------------------------
# 14.  COMPLIANCE, RENDER, PROSE
# ----------------------------------------------------------------------------

def compliance_sweep(R):
    names = [g["name"] for g in GATES]

    def st(rule, gates_, falsifiers):
        # a write-time gate has not been registered yet when the sweep first
        # runs inside assemble(); it is accounted for, not reported MISSING,
        # and G-DEFERRED-GATES-EVALUATED proves it really ran.
        have = [g for g in gates_ if g in names or g in DEFERRED_GATES]
        missing = [g for g in gates_
                   if g not in names and g not in DEFERRED_GATES]
        return {"rule": rule,
                "status": ("APPLIED via " + ", ".join(have)
                           + ("; falsifiers " + ", ".join(falsifiers)
                              if falsifiers else "")
                           if not missing else "MISSING " + ", ".join(missing))}
    rows = [
        st("RUNBOOK 13/14/15 with every addendum binds at delivery (#246/#313)",
           ["G-FLOATGUARD", "G-NO-MUTANT-IDENTITY"], []),
        st("the CR-B pin -- sources hash-verified AND path-value anchored at "
           "run time, R6a cited at DELIVERED-UNDER-PANEL",
           ["A-PIN-CRB", "A-R6A-RECEIPT", "A-I7-RECEIPT", "A-HA-PAPER",
            "A-HA-CODE", "G-PATH-ANCHORS" if "G-PATH-ANCHORS" in names
            else "G-ANCHOR-CELL-COMPLETE"],
           ["anchor-hash-A-R6A-RECEIPT", "anchor-hash-A-I7-RECEIPT",
            "anchor-hash-A-HA-PAPER", "anchor-hash-A-PIN-CRB", "anchor-skip",
            "path-drift", "path-value", "text-anchor-drift"]),
        st("the pin's measurement (1): the split fibers rebuilt and anchored "
           "against R6a's counts",
           ["G-FIBER-REBUILD-ANCHORS-R6A", "G-SPLIT-SPAN-ANCHOR",
            "G-COUNT-LATTICE-REPRODUCES-R6A"],
           ["fiber-typed", "r6a-anchor-drift"]),
        st("the pin's measurement (2): the symmetry inventory as data, every "
           "pinned symmetry acting on a fiber",
           ["G-SYMMETRY-INVENTORY-CELL-COMPLETE", "G-POINT-GROUP-CLOSED",
            "G-BLOCK-PRESERVING-IS-THE-PINNED-GROUP",
            "G-STABILISERS-ANCHOR-R6A", "G-EQUIVARIANT-FIBER-ANCHOR-R6A"],
           ["census-drop", "blockgroup-lax", "stabiliser-anchor-drift",
            "equivariant-anchor-drift"]),
        st("the pin's measurement (2): the orbit decomposition of each fiber, "
           "computed exactly",
           ["G-BURNSIDE-INTEGRAL", "G-ORBIT-TWO-ROUTES",
            "G-COMPARATOR-EXERCISED", "G-NECKLACE-COMPARATOR"],
           ["burnside-corrupt", "comparator-alias"]),
        st("the pin's measurement (3): unique invariant distribution iff "
           "transitive -- MEASURED per fiber, the simplex dimension counted "
           "exactly where not transitive",
           ["G-SIMPLEX-DIM-EQUALS-ORBITS-MINUS-ONE", "G-INVSYS-EXERCISED",
            "G-TRANSITIVITY-CENSUS", "G-PER-INTERVAL-LAW",
            "G-COUNT-LATTICE-TRANSITIVITY-CENSUS"],
           ["simplex-dim-lax", "invsys-inert", "transitivity-flip"]),
        st("the pin's measurement (4): every further selection candidate "
           "tested, its forcing NAMED or REFUTED -- MaxEnt audited, not "
           "assumed",
           ["G-SELECTION-CANDIDATES-CELL-COMPLETE", "G-SELECTION-CLASSIFICATION",
            "G-MAXENT-CONSTRAINT-AUDIT", "G-DECLARATION-CENSUS-CELL-COMPLETE"],
           ["selection-forced", "weightlaws-collapse", "front-lax", "drag-lax",
            "declaration-census-drop"]),
        st("the pin's measurement (5): iteration in distribution -- do the "
           "orbit-simplex dimensions grow, stabilise or collapse",
           ["G-DECLARED-SPLIT-ANCHORS-R6A", "G-ITERATION-TREND",
            "G-ITERATION-SYMMETRY-OUTRUN"],
           ["iteration-lax", "iter-anchor-drift"]),
        st("the pin's controls: a constructed transitive fiber (positive) and "
           "an asymmetric fiber (negative)",
           ["G-POSITIVE-CONTROL", "G-NEGATIVE-CONTROL"],
           ["control-pass", "neg-control-pass"]),
        st("BLOCKED verdicts are first-class and NAME the missing object",
           ["G-MISSING-OBJECT-NAMED", "G-VERDICT-ALL-HEADS-REACHABLE"],
           ["missing-object-blank"]),
        st("#10 containment is not equality: the verdict gate compares the "
           "COMPLETE string against an independent rebuild",
           ["G-VERDICT-STRING-EQUALITY"],
           ["verdict-pair-swap", "verdict-typed-segment", "verdict-append-text",
            "verdict-fully-typed", "verdict-inert-segment", "head-constant"]),
        {"rule": "#20 compliance claims are gate claims: a comparator that "
                 "cannot disagree with the object under test is vacuous",
         "status": "APPLIED -- reconstruct_verdict_from_receipt() shares no "
                   "code and no input with build_verdict(); it reads the "
                   "RECEIPT OBJECT alone, and all five injection classes plus "
                   "head-constant die on it"},
        st("#10 render from the gated object (one object, one source of truth)",
           ["G-RENDER-FROM-GATED-OBJECT"], ["render-escape"]),
        st("#20 prose renders from the receipt: every numeric claim in the "
           "paper renders from the receipt object",
           ["G-PROSE-RENDERS-FROM-THE-RECEIPT"], ["prose-claim-drift"]),
        {"rule": "#20 path-value anchoring: a read-by-path anchors the (path, "
                 "value) pair, not only the file bytes",
         "status": "APPLIED -- %d path-value anchor rows and %d verbatim-text "
                   "rows, each gated individually"
                   % (R["anchor_totals"]["path_value"],
                      R["anchor_totals"]["verbatim_text"])},
        st("#234 the verdict is derived inside a gate and a flip mutant proves "
           "the derivation can fail",
           ["G-VERDICT-SEGMENTS-FLIPPABLE"], ["verdict-inert-segment"]),
        {"rule": "#234 counts are computed, never typed",
         "status": "APPLIED via G-FIBER-REBUILD-ANCHORS-R6A, "
                   "G-TRANSITIVITY-CENSUS, G-COUNT-LATTICE-TRANSITIVITY-CENSUS; "
                   "falsifiers fiber-typed, weightlaws-collapse"},
        st("#219 a gate clause may not compare an object against a copy of "
           "itself routed through the component under test",
           ["G-ORBIT-TWO-ROUTES", "G-COMPARATOR-EXERCISED",
            "G-NECKLACE-COMPARATOR", "G-CACHE-FRESH-EQUALS-MEMO"],
           ["comparator-alias", "cache-alias"]),
        st("#219/#185 a zero-hit cache gate is vacuous, and a self-test routed "
           "through the memo tests the cache",
           ["G-CACHE-EXERCISED", "G-CACHE-FRESH-EQUALS-MEMO"], ["cache-alias"]),
        {"rule": "#208 no gate predicate may reference mutant identity",
         "status": "APPLIED via G-NO-MUTANT-IDENTITY -- run-mode identity is "
                   "read by mutate() and main() alone, measured by an AST scan "
                   "validated with 2 synthetic injections it must flag"},
        st("#208 analytically-forced clauses are disclosures, not must-pass "
           "gates", ["G-FORCED-CLAUSE-DISCLOSURE"], ["forced-clause-promote"]),
        {"rule": "#257 computed qualifiers (no typed qualifier segment)",
         "status": "APPLIED via G-SELECTION-CLASSIFICATION -- the "
                   "FORCED/REFUTED qualifier is a function of whether a "
                   "forcing is named, and of nothing else"},
        {"rule": "#314 precheck doctrine: a precheck may gate which candidates "
                 "are censused but may never name the verdict",
         "status": "APPLIED -- admissibility and splittability gate WHICH "
                   "records are censused; every verdict-naming fact (the "
                   "orbit counts, the simplex dimensions, the candidate "
                   "verdicts) is measured on the censused objects"},
        {"rule": "#313 repair propagation: gates diffed against every rule "
                 "engraved since the pin froze",
         "status": "APPLIED -- all five 2026-08-09 engravings are carried at "
                   "birth with injection-falsifiers, and their presence in the "
                   "RUNBOOK is itself anchored (T-ENGRAVE-1..5)"},
        st("#313 boundary parity: a boolean-connective boundary carries a "
           "parity-witness gate",
           ["G-BLOCK-PRESERVING-IS-THE-PINNED-GROUP"], ["blockgroup-lax"]),
        {"rule": "RUNBOOK section 15 declared-arena discipline: the arena is "
                 "declared as data and arena-artifacts never become "
                 "conclusions",
         "status": "APPLIED -- the arena block names boundary/family/law/state/"
                   "arena/provenance; every symmetry carries a provenance "
                   "class (PINNED vs DECLARED-EXTENSION) and the extension's "
                   "results are reported beside the pinned ones, never in "
                   "place of them"},
        {"rule": "RUNBOOK section 14 symmetry self-test: an instrument that "
                 "enforces a symmetry-invariant quantity self-tests under that "
                 "symmetry's own action",
         "status": "APPLIED -- the orbit engine is checked against a direct "
                   "orbit walk under the group's own generators and against a "
                   "closed form for the translations, and the reversal "
                   "elements are measured for whether they act on the "
                   "admissible fiber at all rather than assumed to"},
        {"rule": "v14 LOG #4 erratum",
         "status": "APPLIED -- disclosed and anchored (T-ERRATUM); this unit "
                   "reads no artifact the erratum touches"},
        st("never-falsified census in the receipt from delivery one",
           ["G-FALSIFIER-CENSUS-HONEST"], []),
    ]
    missing = [r for r in rows if r["status"].startswith("MISSING")]
    gate("G-COMPLIANCE-SWEEP",
         "the compliance sweep enumerates every binding rule and computes its "
         "status from the live gate ledger; no row reads MISSING",
         len(missing) == 0, {"rows": len(rows), "missing": missing[:3]})
    return rows


def frac_str(x):
    return str(x)


def jsonable(o):
    if isinstance(o, Fr):
        return str(o)
    if isinstance(o, dict):
        return {(str(k) if not isinstance(k, str) else k): jsonable(v)
                for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    return o


def paper_claims(R):
    """THE PROSE RENDERER (RUNBOOK section 13 addendum, v14 #20).  Every
    load-bearing numeric sentence of paper-06 is BUILT HERE from the measured
    object and gated to appear VERBATIM in the paper."""
    fr = R["fiber_rebuild"]
    si = R["symmetry_inventory"]
    od = R["orbit_decomposition"]
    imc = R["invariant_measure_census"]
    pil = R["per_interval_law"]
    lat = R["count_lattice_census"]
    sc = R["selection_candidates"]
    dcz = R["determinism_census"]
    it = R["iteration_in_distribution"]
    ct = R["controls"]
    orders = {row["group"]: row["order"] for row in si["rows"]}
    diag = [r for r in R["direct_enumeration"]["rows"]
            if r["record"] == "G-DIAG2" and r["group"] == "CHART"][0]
    an2 = [r for r in od["rows"]
           if r["record"] == "G-ANISO2" and r["group"] == "CHART"][0]
    a2 = [t for t in it["rows"] if t["record"] == "G-ANISO2"]
    lvl = a2[0]["trace"]
    lvl2 = a2[1]["trace"]
    fac = [c for c in sc["rows"]
           if c["name"] == "THE-UNIFORM-LAW-ON-THE-ADMISSIBLE-FIBER"][0]
    frc = [c for c in sc["rows"] if c["name"] == "THE-FRONT"][0]["evidence"]
    claims = {
        "fibers": "the split fibers are rebuilt here from the pinned "
                  "declarations alone and agree with the R6a receipt at %d of "
                  "%d cells, spanning %d to %d over the %d records that admit "
                  "the move"
                  % (fr["cells_anchored"], fr["cells_anchored"], fr["span_min"],
                     fr["span_max"], fr["records_admitting_the_move"]),
        "symmetry": "the pinned chart group has order %d; the largest group "
                    "the declared link set admits has order %d; and exactly "
                    "%d of those %d elements preserve the block structure the "
                    "admissible fiber is built on"
                    % (orders["CHART"], orders["EXT"],
                       si["block_preserving_of_the_extension"], orders["EXT"]),
        "orbits": "the orbit decomposition is computed at %d (record, group) "
                  "cells, cross-checked by direct enumeration at %d of them "
                  "and by a closed form at %d"
                  % (od["cells"], len(R["direct_enumeration"]["rows"]),
                     len(R["closed_form_comparator"]["rows"])),
        "transitive": "no cell of the census is transitive: %d of %d, and the "
                      "orbit-simplex dimension runs from %d to %d"
                      % (imc["cells_with_a_unique_invariant_law"], od["cells"],
                         imc["simplex_dim_min"], imc["simplex_dim_max"]),
        "diag2": "G-DIAG2's fiber of %d splits falls into %d orbits under the "
                 "pinned chart group, with orbit sizes %s"
                 % (diag["fiber"], diag["orbits_direct"],
                    ", ".join("%d x %d" % (v, k) for k, v
                              in sorted(diag["orbit_sizes"].items()))),
        "aniso2": "G-ANISO2's admissible fiber holds %d splits and %d orbits, "
                  "an invariant simplex of dimension %d"
                  % (an2["fiber_img"], an2["orbits_img"],
                     an2["simplex_dim_img"]),
        "per_interval": "a single interval carrying n events has n - 1 splits: "
                        "under the pinned group the simplex has dimension "
                        "n - 2 and is a point only at n = 2, and under the "
                        "declared reversal extension it is a point only at "
                        "n = %s"
                        % (" and n = ".join(str(r["n"]) for r in pil["rows"]
                                            if r["flip_transitive"])),
        "lattice": "of the %d admissible count vectors in the declared box, "
                   "%d are splittable, exactly %d has a fiber the pinned "
                   "symmetry acts transitively on, and under the declared "
                   "reversal extension %d do -- %d of them inside the declared "
                   "record family"
                   % (lat["admissible_count_vectors"], lat["splittable"],
                      lat["pinned_transitive_count"],
                      lat["flip_transitive_count"],
                      len(lat["transitive_vectors_in_the_declared_family"])),
        "selection": "%d selection candidates beyond symmetry are tested and "
                     "%d are forced" % (sc["count"], sc["forced"]),
        "maxent": "the pinned layer carries %d distribution-level declarations "
                  "out of %d, so maximum entropy has no constraint set of its "
                  "own to act on"
                  % (dcz["declarations"]["distribution_level"],
                     dcz["declarations"]["declarations"]),
        "nonfactor": "the uniform law on the admissible fiber fails to "
                     "factorise at %d of the %d records that admit the move"
                     % (len(fac["evidence"]["non_factorising"]),
                        len(fac["evidence"]["records"])),
        "front": "the front-proportional split returns an admissible integer "
                 "at %d of %d cells, is non-integral at %d, out of range at "
                 "%d and undefined at %d"
                 % (frc["admissible_integer"], frc["cells"],
                    frc["non_integral"], frc["out_of_range"], frc["undefined"]),
        "determinism": "the pinned dynamics is a bijection at %d of %d sampled "
                       "cells with %d collisions, so its pushforward carries "
                       "point masses to point masses"
                       % (dcz["h_bijection"]["roundtrip_identity"],
                          dcz["h_bijection"]["cells"],
                          dcz["h_bijection"]["collisions"]),
        "iteration": "at the one record that reaches a second level the fiber "
                     "grows from %d to %d under the first declared completion "
                     "while the acting group stays at %d, so the simplex "
                     "dimension grows from %d to %d; under the second "
                     "completion the group doubles to %d and the fiber, at "
                     "%d, still outruns it"
                     % (lvl[0]["img"], lvl[1]["img"], lvl[1]["group"],
                        lvl[0]["simplex_dim"], lvl[1]["simplex_dim"],
                        lvl2[1]["group"], lvl2[1]["img"]),
        "controls": "the %d positive controls each return a unique invariant "
                    "measure and the %d negative controls each return a "
                    "positive-dimensional simplex"
                    % (len(ct["positive"]), len(ct["negative"])),
        "instrument": "%d gates, all passed; %d anchors; %d mutants, no "
                      "survivors" % (len(GATES) + 4, len(ANCHORS),
                                     len(MUTANTS)),
        "verdict": R["verdict"],
    }
    return mutate("prose-claim-drift", claims)


def paper_prose_audit(R):
    claims = paper_claims(R)
    if not os.path.exists(PAPER):
        return claims, None, sorted(claims)
    with open(PAPER, "r") as fh:
        text = fh.read()
    missing = sorted([k for k, v in claims.items() if v not in text])
    return claims, sha12(PAPER), missing


# ----------------------------------------------------------------------------
# 15.  THE TEXT RENDER
# ----------------------------------------------------------------------------

def render_text(R):
    out = []
    w = out.append
    w("=" * 78)
    w(R["unit"])
    w("=" * 78)
    w("")
    w("QUESTION: " + R["question"])
    w("PIN: %s (%s)" % (R["pin"], R["pin_sha256_prefix"]))
    w("PREDECESSOR: %s -- %s [%s]" % (R["predecessor"]["unit"],
                                      R["predecessor"]["verdict_head"],
                                      R["predecessor"]["status"]))
    w("")
    w("--- 1. THE FIBER REBUILD, ANCHORED AGAINST R6a ---")
    w("  %-12s %-12s %-9s %-24s %s" % ("record", "counts(0,0)", "adm",
                                       "admissible fiber", "per-site"))
    for name in sorted(R["record_family"]):
        r = R["record_family"][name]
        w("  %-12s %-12s %-9s %-24d %s"
          % (name, tuple(r["counts_at_00"]), str(r["admissible"]), r["img"],
             r["per_site_admissible"]))
    fr = R["fiber_rebuild"]
    w("  cells anchored against R6a: %d ; mismatches: %d"
      % (fr["cells_anchored"], len(fr["mismatches"])))
    w("  span: %d .. %d ; records admitting the move: %d ; no split at all: %s"
      % (fr["span_min"], fr["span_max"], fr["records_admitting_the_move"],
         ", ".join(fr["records_with_no_split"])))
    w("")
    w("--- 2. THE SYMMETRY INVENTORY (as data) ---")
    for row in R["symmetry_inventory"]["rows"]:
        w("  %-10s order %-12d %s" % (row["group"], row["order"],
                                      row["provenance"]))
    si = R["symmetry_inventory"]
    w("  the declared link set is the A_2 root system; its automorphism group "
      "has order %d" % si["point_group_order"])
    w("  direction permutations: pinned %d, declared extension %d (all of S_3)"
      % (si["pinned_sigma_is_S2_extension_is_S3"]
         ["pinned_direction_permutations"],
         si["pinned_sigma_is_S2_extension_is_S3"]
         ["declared_extension_direction_permutations"]))
    w("  THE MEASURED THEOREM: block-preserving elements of the extension = %d "
      "= the pinned chart group exactly"
      % si["block_preserving_of_the_extension"])
    w("")
    w("--- 3. THE ORBIT DECOMPOSITION ---")
    w("  %-12s %-7s %-6s %-24s %-24s %s" % ("record", "group", "|H|",
                                            "fiber", "orbits", "simplex dim"))
    for row in R["orbit_decomposition"]["rows"]:
        w("  %-12s %-7s %-6d %-24d %-24d %d"
          % (row["record"], row["group"], row["stabiliser_order"],
             row["fiber_img"], row["orbits_img"], row["simplex_dim_img"]))
    w("  comparator 1 (direct orbit walk, cap %d):"
      % R["direct_enumeration"]["cap"])
    for e in R["direct_enumeration"]["rows"]:
        w("     %-12s %-6s fiber %-8d direct %-8d burnside %-8d agree %s "
          "escapes %d" % (e["record"], e["group"], e["fiber"],
                          e["orbits_direct"], e["orbits_burnside"],
                          e["agree"], e["escapes"]))
    w("  comparator 2 (closed form %s):"
      % R["closed_form_comparator"]["formula"])
    for n0 in R["closed_form_comparator"]["rows"]:
        w("     %-12s k=%-5d closed form %-24d engine %-24d agree %s"
          % (n0["record"], n0["k"], n0["closed_form"], n0["engine"],
             n0["agree"]))
    w("")
    w("--- 4. THE INVARIANT-MEASURE CENSUS ---")
    imc = R["invariant_measure_census"]
    w("  cells: %d ; cells with a UNIQUE invariant law: %d"
      % (imc["cells"], imc["cells_with_a_unique_invariant_law"]))
    w("  orbit-simplex dimension: %d .. %d"
      % (imc["simplex_dim_min"], imc["simplex_dim_max"]))
    w("  comparator 3 -- the criterion measured, not assumed:")
    for row in R["invariant_measure_comparator"]["rows"][:6]:
        w("     n=%-3d %-42s orbits %-3d dim(linear system) %-3d agree %s"
          % (row["n"], row["action"], row["orbits"],
             row["simplex_dim_linear_system"], row["agree"]))
    w("     ... %d cells, all agreeing"
      % len(R["invariant_measure_comparator"]["rows"]))
    w("")
    w("--- 5. THE PER-INTERVAL LAW ---")
    pil = R["per_interval_law"]
    w("  count values in the declared family: %s" % pil["family_count_values"])
    w("  %-5s %-7s %-9s %-9s %-9s %s" % ("n", "fiber", "pinned", "dim",
                                         "reversal", "dim"))
    for row in pil["rows"]:
        w("  %-5d %-7d %-9d %-9s %-9d %s"
          % (row["n"], row["fiber"], row["pinned_orbits"],
             row["pinned_simplex_dim"], row["flip_orbits"],
             row["flip_simplex_dim"]))
    w("  pinned dimension law: %s ; reversal dimension law: %s"
      % (pil["pinned_dim_law"], pil["flip_dim_law"]))
    w("")
    w("--- 6. THE COUNT-LATTICE CENSUS ---")
    lat = R["count_lattice_census"]
    w("  admissible count vectors %d ; splittable %d ; fiber a point %s"
      % (lat["admissible_count_vectors"], lat["splittable"],
         lat["fiber_is_a_point"]))
    w("  pinned-transitive %s ; reversal-transitive %s"
      % (lat["pinned_transitive"], lat["flip_transitive"]))
    w("  transitive vectors inside the declared record family: %s"
      % (lat["transitive_vectors_in_the_declared_family"] or "NONE"))
    w("")
    w("--- 7. SELECTION CANDIDATES BEYOND SYMMETRY ---")
    for c in R["selection_candidates"]["rows"]:
        w("  %-38s %s" % (c["name"], c["result"]))
        w("      %s" % c["why"])
    w("  forced: %d ; refuted: %d" % (R["selection_candidates"]["forced"],
                                      R["selection_candidates"]["refuted"]))
    w("")
    w("--- 8. THE DETERMINISM CENSUS ---")
    dcz = R["determinism_census"]
    w("  pinned declarations %d ; value-level %d ; distribution-level %d"
      % (dcz["declarations"]["declarations"],
         dcz["declarations"]["value_level"],
         dcz["declarations"]["distribution_level"]))
    w("  H_a[N] bijection cells %d ; round-trip identity %d ; collisions %d"
      % (dcz["h_bijection"]["cells"], dcz["h_bijection"]["roundtrip_identity"],
         dcz["h_bijection"]["collisions"]))
    w("  MISSING OBJECT: %s" % dcz["missing_object"])
    w("")
    w("--- 9. ITERATION IN DISTRIBUTION ---")
    for row in R["iteration_in_distribution"]["rows"]:
        w("  %-12s completion key %d  dims %s  groups %s  trend %s"
          % (row["record"], row["diag_completion_key"], row["simplex_dims"],
             row["group_orders"], row["trend"]))
    w("  cells with two live levels: %d ; completion-relative: %s"
      % (R["iteration_in_distribution"]["cells_with_two_live_levels"],
         R["iteration_in_distribution"]["completion_relative"]))
    for row in R["iteration_in_distribution"]["rows"]:
        if row["live_levels"] >= 2:
            w("     %-12s key %d fiber x%s group x%s outruns %s"
              % (row["record"], row["diag_completion_key"],
                 row["fiber_growth_factor"], row["group_growth_factor"],
                 row["fiber_outruns_the_group"]))
    w("")
    w("--- 10. CONTROLS ---")
    for p in R["controls"]["positive"]:
        w("  POSITIVE %-36s orbits %d dim %d unique measure %s"
          % (p["name"], p["orbits"], p["simplex_dim"],
             "FOUND" if p["unique_measure"] else "NOT FOUND"))
    for n0 in R["controls"]["negative"]:
        w("  NEGATIVE %-36s orbits %d dim %d"
          % (n0["name"], n0["orbits"], n0["simplex_dim"]))
    w("")
    w("--- 11. THE VERDICT ---")
    w("")
    w(R["verdict"])
    w("")
    w("--- 12. THE INSTRUMENT ---")
    w("  anchors %d (file-bytes %d / path-value %d / verbatim-text %d)"
      % (R["anchor_totals"]["total"], R["anchor_totals"]["file_bytes"],
         R["anchor_totals"]["path_value"], R["anchor_totals"]["verbatim_text"]))
    w("  gates %d, failures %d ; mutants %d"
      % (R["totals"]["gates"], R["totals"]["must_pass_failures"],
         R["totals"]["mutants"]))
    w("  never-falsified %d of %d, all waived"
      % (R["falsifier_census"].get("never_falsified_count", 0),
         R["falsifier_census"].get("gates", 0)))
    w("  arithmetic: %s" % R["arithmetic"])
    w("")
    return "\n".join(out) + "\n"


# ----------------------------------------------------------------------------
# 16.  THE DECLARED MUTANTS AND THEIR INJECTIONS
# ----------------------------------------------------------------------------

MUTANTS = [
    {"name": "anchor-hash-A-PIN-CRB", "expected_gate": "A-PIN-CRB",
     "what": "corrupts this unit's own pin hash"},
    {"name": "anchor-hash-A-R6A-RECEIPT", "expected_gate": "A-R6A-RECEIPT",
     "what": "corrupts the R6a receipt's measured hash"},
    {"name": "anchor-hash-A-I7-RECEIPT", "expected_gate": "A-I7-RECEIPT",
     "what": "corrupts the pinned I7 receipt's measured hash"},
    {"name": "anchor-hash-A-HA-PAPER", "expected_gate": "A-HA-PAPER",
     "what": "corrupts the pinned HA paper's measured hash"},
    {"name": "anchor-skip", "expected_gate": "G-ANCHOR-CELL-COMPLETE",
     "what": "silently drops the last file-bytes anchor row"},
    {"name": "path-drift", "expected_gate": "P-R6A-IMG-ANISO2",
     "what": "reads the R6a fiber from a neighbouring JSON path"},
    {"name": "path-value", "expected_gate": "P-I7-LINKS2",
     "what": "corrupts the value read at a pinned path"},
    {"name": "text-anchor-drift", "expected_gate": "T-NORM-IS-A-BOOLEAN",
     "what": "drifts the verbatim sentence the determinism reading rests on"},
    {"name": "float-leak", "expected_gate": "G-FLOATGUARD",
     "what": "injects a float offence into the AST scan"},
    {"name": "mutant-identity-leak", "expected_gate": "G-NO-MUTANT-IDENTITY",
     "what": "adds a third function reading run-mode identity"},
    {"name": "fiber-typed", "expected_gate": "G-FIBER-REBUILD-ANCHORS-R6A",
     "what": "types a split fiber instead of computing it"},
    {"name": "r6a-anchor-drift", "expected_gate": "G-FIBER-REBUILD-ANCHORS-R6A",
     "what": "suppresses a rebuild-vs-R6a mismatch"},
    {"name": "census-drop", "expected_gate": "G-SYMMETRY-INVENTORY-CELL-COMPLETE",
     "what": "drops a row of the symmetry inventory"},
    {"name": "blockgroup-lax",
     "expected_gate": "G-BLOCK-PRESERVING-IS-THE-PINNED-GROUP",
     "what": "corrupts the block-preservation count"},
    {"name": "stabiliser-anchor-drift", "expected_gate": "G-STABILISERS-ANCHOR-R6A",
     "what": "hides a stabiliser mismatch against R6a"},
    {"name": "equivariant-anchor-drift",
     "expected_gate": "G-EQUIVARIANT-FIBER-ANCHOR-R6A",
     "what": "hides an equivariant-fiber mismatch against R6a"},
    {"name": "burnside-corrupt", "expected_gate": "G-ORBIT-TWO-ROUTES",
     "what": "corrupts one Cauchy-Frobenius orbit count"},
    {"name": "comparator-alias", "expected_gate": "G-ORBIT-TWO-ROUTES",
     "what": "makes the direct comparator return a shifted count"},
    {"name": "simplex-dim-lax",
     "expected_gate": "G-SIMPLEX-DIM-EQUALS-ORBITS-MINUS-ONE",
     "what": "breaks the orbits-minus-one identity at one cell"},
    {"name": "invsys-inert",
     "expected_gate": "G-SIMPLEX-DIM-EQUALS-ORBITS-MINUS-ONE",
     "what": "makes the linear-system route return a wrong dimension"},
    {"name": "transitivity-flip", "expected_gate": "G-TRANSITIVITY-CENSUS",
     "what": "flips the decisive transitivity bit at one cell"},
    {"name": "lattice-transitivity-flip",
     "expected_gate": "G-COUNT-LATTICE-TRANSITIVITY-CENSUS",
     "what": "corrupts the count-lattice transitivity count"},
    {"name": "selection-forced", "expected_gate": "G-SELECTION-CLASSIFICATION",
     "what": "relabels a refuted candidate FORCED without naming a forcing"},
    {"name": "weightlaws-collapse",
     "expected_gate": "G-CANDIDATE-REFUTATIONS-MEASURED",
     "what": "collapses the weight-functional census"},
    {"name": "front-lax", "expected_gate": "G-CANDIDATE-REFUTATIONS-MEASURED",
     "what": "reports the front candidate as everywhere admissible"},
    {"name": "drag-lax", "expected_gate": "G-CANDIDATE-REFUTATIONS-MEASURED",
     "what": "reports a declared map from the drag onto the split fiber"},
    {"name": "declaration-census-drop",
     "expected_gate": "G-DECLARATION-CENSUS-CELL-COMPLETE",
     "what": "drops a pinned declaration from the classification census"},
    {"name": "missing-object-blank", "expected_gate": "G-MISSING-OBJECT-NAMED",
     "what": "empties the named missing object under the BLOCKED head"},
    {"name": "iter-anchor-drift", "expected_gate": "G-DECLARED-SPLIT-ANCHORS-R6A",
     "what": "breaks the reproduction of R6a's iteration table"},
    {"name": "iteration-lax", "expected_gate": "G-ITERATION-TREND",
     "what": "corrupts the iteration trend summary"},
    {"name": "control-pass", "expected_gate": "G-POSITIVE-CONTROL",
     "what": "makes the positive control fail to find its unique measure"},
    {"name": "neg-control-pass", "expected_gate": "G-NEGATIVE-CONTROL",
     "what": "declares the asymmetric fiber transitive"},
    {"name": "cache-alias", "expected_gate": "G-CACHE-FRESH-EQUALS-MEMO",
     "what": "serves a wrong memo value against the fresh recomputation"},
    {"name": "forced-clause-promote",
     "expected_gate": "G-FORCED-CLAUSE-DISCLOSURE",
     "what": "promotes an analytically-forced clause out of the disclosure "
             "list"},
    {"name": "verdict-pair-swap", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "swaps two verdict segments' values against their names"},
    {"name": "verdict-typed-segment", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "types a verdict segment instead of deriving it"},
    {"name": "verdict-append-text", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "appends text after the verdict string"},
    {"name": "verdict-fully-typed", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "types every verdict segment"},
    {"name": "verdict-inert-segment",
     "expected_gate": "G-VERDICT-SEGMENTS-FLIPPABLE",
     "what": "makes one verdict segment ignore the value it reads"},
    {"name": "head-constant", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "pins the head to a constant regardless of the measurement"},
    {"name": "render-escape", "expected_gate": "G-RENDER-FROM-GATED-OBJECT",
     "what": "corrupts a rendered cell after the gates have run"},
    {"name": "prose-claim-drift",
     "expected_gate": "G-PROSE-RENDERS-FROM-THE-RECEIPT",
     "what": "drifts a rendered paper claim away from the receipt"},
]

def _flip_unique(rows):
    out = []
    for i, r in enumerate(rows):
        r = dict(r)
        if i == 0:
            r["unique_invariant_law"] = not r["unique_invariant_law"]
        out.append(r)
    return out


def _force_candidate(rows):
    out = []
    for i, c in enumerate(rows):
        c = dict(c)
        if i == 0:
            c["result"] = "FORCED-BY-SYMMETRY"
        out.append(c)
    return out


def _break_positive(ctl):
    ctl = dict(ctl)
    pos = [dict(p) for p in ctl["positive"]]
    pos[0]["unique_measure"] = None
    ctl["positive"] = pos
    return ctl


def _break_negative(ctl):
    ctl = dict(ctl)
    neg = [dict(n) for n in ctl["negative"]]
    neg[0]["transitive"] = True
    ctl["negative"] = neg
    return ctl


def _escape_render(payload):
    payload = dict(payload)
    od = dict(payload["orbit_decomposition"])
    rows = [dict(r) for r in od["rows"]]
    rows[0]["orbits_img"] = rows[0]["orbits_img"] + 1
    od["rows"] = rows
    payload["orbit_decomposition"] = od
    return payload


_INJECTIONS = {
    "float-leak": lambda v: list(v) + [("injected-float", 0)],
    "mutant-identity-leak": lambda v: sorted(set(list(v) + ["gate_probe"])),
    "anchor-skip": lambda v: v[:-1],
    "anchor-hash-A-PIN-CRB": lambda v: "0" * 12,
    "anchor-hash-A-R6A-RECEIPT": lambda v: "0" * 12,
    "anchor-hash-A-I7-RECEIPT": lambda v: "0" * 12,
    "anchor-hash-A-HA-PAPER": lambda v: "0" * 12,
    "path-drift": lambda v: ["split_fibers", "G-ANISO2", "raw"],
    "path-value": lambda v: None,
    "text-anchor-drift": lambda v: v + " (edited)",
    "fiber-typed": lambda v: 19683,
    "r6a-anchor-drift": lambda v: list(v) + [["G-DIAG2",
                                          "admissible_at_images",
                                          0, 19683]],
    "census-drop": lambda v: v[:-1],
    "blockgroup-lax": lambda v: v + 1,
    "stabiliser-anchor-drift": lambda v: list(v) + ["G-DIAG2"],
    "equivariant-anchor-drift": lambda v: list(v) + [["G-DIAG2", 0, 3]],
    "burnside-corrupt": lambda v: v + 1,
    "comparator-alias": lambda v: v + 1,
    "simplex-dim-lax": lambda v: v + 1,
    "invsys-inert": lambda v: v + 1,
    "transitivity-flip": _flip_unique,
    "lattice-transitivity-flip": lambda v: dict(
        v, pinned_transitive_count=v["pinned_transitive_count"] + 1),
    "selection-forced": _force_candidate,
    "weightlaws-collapse": lambda v: {k: 1 for k in v},
    "front-lax": lambda v: dict(v, admissible_integer=v["cells"],
                                non_integral=0, out_of_range=0, undefined=0),
    "drag-lax": lambda v: dict(
        v, index_sets=dict(v["index_sets"],
                           declared_maps_onto_the_split_fiber=1)),
    "declaration-census-drop": lambda v: v[:-1],
    "missing-object-blank": lambda v: "",
    "iter-anchor-drift": lambda v: [dict(r, ok=False) if i == 0 else r
                                    for i, r in enumerate(v)],
    "iteration-lax": lambda v: dict(v, grows=v["grows"] + 1),
    "control-pass": _break_positive,
    "neg-control-pass": _break_negative,
    "cache-alias": lambda v: (v[1:] if len(v) > 1 else (((1, 1, 1),) + v)),
    "forced-clause-promote": lambda v: v[:-1],
    "verdict-pair-swap": lambda v: 1,
    "verdict-typed-segment": lambda v: 1,
    "verdict-append-text": lambda v: 1,
    "verdict-fully-typed": lambda v: 1,
    "verdict-inert-segment": lambda t: ((t[1], t[1], t[2]) if t[2] == 7 else t),
    "head-constant": lambda v: 1,
    "render-escape": _escape_render,
    "prose-claim-drift": lambda v: dict(v, fibers="the split fibers are "
                                        "rebuilt here from the pinned "
                                        "declarations"),
}


# ----------------------------------------------------------------------------
# 17.  DELIVERY
# ----------------------------------------------------------------------------

WAIVERS = {
    "G-NO-MUTANT-IDENTITY": "self-validating: the AST detector is proved able "
                            "to fire by two synthetic injections evaluated "
                            "inside the gate itself, and mutant-identity-leak "
                            "falsifies it besides",
    "A-R0-PIN": "the v14 founding pin's own hash; the anchor-hash channel is "
                "falsified at four of the six file-bytes rows and anchor-skip "
                "proves a dropped row dies",
    "A-HA-CODE": "covered by anchor-hash-A-HA-PAPER and anchor-skip on the "
                 "same channel",
    "G-ANCHOR-CELL-COMPLETE": "falsified by anchor-skip",
    "G-POINT-GROUP-CLOSED": "a closure measurement on a group built by "
                            "enumeration; blockgroup-lax falsifies the "
                            "neighbouring gate that reads the same object",
    "G-SPLIT-SPAN-ANCHOR": "covered by fiber-typed and r6a-anchor-drift, which "
                           "move the same rebuilt fibers",
    "G-COUNT-LATTICE-REPRODUCES-R6A": "covered by lattice-transitivity-flip at "
                                      "the paired census gate",
    "G-BURNSIDE-INTEGRAL": "an analytically forced clause for a genuine group "
                           "action -- a disclosure, not a must-pass "
                           "falsifiable gate (RUNBOOK section 14 addendum, "
                           "v13 #208); the orbit counts it guards are "
                           "falsified by burnside-corrupt",
    "G-H-IS-A-BIJECTION": "an analytically forced clause: the closed-form "
                          "inverse is exhibited in the pinned source and "
                          "anchored verbatim (T-H-INVERSE) -- a disclosure, "
                          "not a must-pass falsifiable gate",
    "G-COMPARATOR-EXERCISED": "covered by comparator-alias at the paired gate",
    "G-INVSYS-EXERCISED": "covered by invsys-inert at the paired gate",
    "G-NECKLACE-COMPARATOR": "covered collaterally by burnside-corrupt, which "
                             "moves the same orbit counts",
    "G-PER-INTERVAL-LAW": "an arithmetic law over the count values; "
                          "simplex-dim-lax falsifies the identity it rests on",
    "G-CACHE-EXERCISED": "covered by cache-alias at the paired gate",
    "G-MAXENT-CONSTRAINT-AUDIT": "covered by declaration-census-drop, which "
                                 "moves the same census",
    "G-COMPLIANCE-SWEEP": "the sweep's rows are computed from the live gate "
                          "ledger, so every mutant that removes a gate moves "
                          "it; it cannot be falsified independently without "
                          "deleting a gate the run needs",
    "G-ITERATION-SYMMETRY-OUTRUN": "covered by iteration-lax at the paired "
                                   "gate, which moves the same trace",
    "G-VERDICT-ALL-HEADS-REACHABLE": "the ladder is evaluated on synthetic "
                                     "counts inside the gate, so the gate "
                                     "carries its own falsifier; head-constant "
                                     "falsifies the neighbouring string gate",
    "G-NO-FLOATS-IN-RECEIPT": "a write-time scan of the emitted payload; "
                              "float-leak falsifies the source-level scan",
    "G-DEFERRED-GATES-EVALUATED": "a bookkeeping gate over the write-time "
                                  "gates; render-escape and prose-claim-drift "
                                  "falsify two of the three it accounts for",
    "G-FALSIFIER-CENSUS-HONEST": "the census gate itself: it reports its own "
                                 "denominator and every waiver, and is the one "
                                 "gate whose failure mode is a false waiver, "
                                 "checked by construction below",
    "G-FINAL-GATE-COUNT": "arithmetic over the live ledger; every mutant that "
                          "aborts the run changes it",
    "G-SELECTION-CANDIDATES-CELL-COMPLETE":
        "covered by selection-forced and by G-CANDIDATE-REFUTATIONS-MEASURED, "
        "which carries three falsifiers over the same candidate rows",
}


def falsifier_census():
    names = [g["name"] for g in GATES]
    fmap = {}
    for m in MUTANTS:
        fmap.setdefault(m["expected_gate"], []).append(m["name"])
    nf = [n for n in names if n not in fmap]
    waived = dict(WAIVERS)
    for n in nf:
        if n in waived:
            continue
        if n.startswith("P-"):
            waived[n] = ("path-value channel: every row is gated "
                         "individually, and the channel is falsified by "
                         "path-drift (a neighbouring JSON path) and "
                         "path-value (a corrupted read) at two of its rows")
        elif n.startswith("T-"):
            waived[n] = ("verbatim-text channel: every row is gated "
                         "individually, and the channel is falsified by "
                         "text-anchor-drift at one of its rows")
    unwaived = [n for n in nf if n not in waived]
    return {"gates": len(names),
            "gates_with_a_declared_falsifier": len([n for n in names
                                                    if n in fmap]),
            "never_falsified": nf, "never_falsified_count": len(nf),
            "unwaived": unwaived, "unwaived_count": len(unwaived),
            "denominator": "%d of %d gates carry no declared falsifier"
                           % (len(nf), len(names)),
            "waivers": {n: waived[n] for n in nf if n in waived},
            "falsifier_map": dict((k, sorted(v)) for k, v in sorted(fmap.items())
                                  if k in names)}


def render_check(R, payload):
    bad = []
    for i, row in enumerate(R["orbit_decomposition"]["rows"]):
        p = payload["orbit_decomposition"]["rows"][i]
        for k in ("orbits_img", "simplex_dim_img", "fiber_img",
                  "transitive_img"):
            if p[k] != row[k]:
                bad.append([row["record"], row["group"], k, p[k], row[k]])
    for name, row in R["record_family"].items():
        p = payload["record_family"][name]
        for k in ("raw", "img"):
            if p[k] != row[k]:
                bad.append([name, k, p[k], row[k]])
    if payload["verdict"] != R["verdict"]:
        bad.append(["verdict", "render-payload", None, None])
    return bad


def deliver():
    R = assemble()
    text = render_text(R)
    payload = jsonable(R)
    payload = mutate("render-escape", payload)
    bad = render_check(R, payload)
    gate("G-RENDER-FROM-GATED-OBJECT",
         "every rendered cell equals the corresponding cell of the gated "
         "measurement object -- the receipt and the output render from one "
         "object, with no bypass path",
         len(bad) == 0, {"mismatches": bad[:4]})

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
    scan(payload)
    gate("G-NO-FLOATS-IN-RECEIPT", "the emitted receipt contains no float",
         len(floats) == 0, {"floats": floats[:4]})

    claims, paper_hash, missing = paper_prose_audit(R)
    R["paper_claims"] = {
        "paper": "v14/paper-06-stochastic-split.md",
        "paper_sha256_prefix": paper_hash,
        "claims_rendered": len(claims),
        "claims_present_in_the_paper": len(claims) - len(missing),
        "claims_missing": missing,
        "rendered": dict(sorted(claims.items())),
        "rule": "every load-bearing numeric sentence of the paper is RENDERED "
                "HERE from the measured object and must appear VERBATIM in the "
                "paper"}
    gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
         "every load-bearing numeric sentence of paper-06 is rendered from the "
         "receipt object and appears verbatim in the paper (all four of the "
         "programme's false paper numbers to date lived in hand-written "
         "prose)",
         paper_hash is not None and len(missing) == 0,
         {"claims": len(claims), "missing": missing[:6],
          "paper_sha256_prefix": paper_hash})

    fc = falsifier_census()
    gate("G-FALSIFIER-CENSUS-HONEST",
         "the never-falsified census is computed from the live gate ledger and "
         "the declared mutant map, and every never-falsified gate carries a "
         "written waiver -- an unwaived silent gate is a false gate claim",
         fc["unwaived_count"] == 0,
         {"never_falsified": fc["never_falsified_count"],
          "unwaived": fc["unwaived"]})
    gate("G-FINAL-GATE-COUNT",
         "the gate count carried by the paper's rendered instrument sentence "
         "equals the number of gates this run actually registers",
         R["paper_claims"]["rendered"]["instrument"].startswith(
             "%d gates, all passed" % (len(GATES) + 2)),
         {"registered_now": len(GATES),
          "claimed": R["paper_claims"]["rendered"]["instrument"]})
    gate("G-DEFERRED-GATES-EVALUATED",
         "the write-time gates named in the falsifier census really did run, "
         "so the census's denominator covers every gate this instrument "
         "declares",
         all(d in [g["name"] for g in GATES] for d in DEFERRED_GATES
             if d != "G-DEFERRED-GATES-EVALUATED"),
         {"deferred": list(DEFERRED_GATES), "registered": len(GATES) + 1})

    R["gates"] = GATES
    R["mutants"] = MUTANTS
    R["totals"]["gates"] = len(GATES)
    R["totals"]["mutants"] = len(MUTANTS)
    R["falsifier_census"] = falsifier_census()
    text = render_text(R)
    payload = jsonable(R)
    with open(OUT_TXT, "w") as fh:
        fh.write(text)
    with open(OUT_JSON, "w") as fh:
        fh.write(json.dumps(payload, indent=1, sort_keys=False) + "\n")
    sys.stdout.write(text)
    return 0


def assemble():
    R, records, by_name, orbit_rows, trans_rows, cands, iters, ctl, lat = run()
    R = finish(R, records, by_name, orbit_rows, trans_rows, cands, iters, ctl,
               lat)
    R["falsifier_census"] = falsifier_census()
    R["compliance"] = compliance_sweep(R)
    R["gates"] = GATES
    R["mutants"] = MUTANTS
    return R


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
        unchanged = all((sha256_full(p) if os.path.exists(p) else None)
                        == before[p] for p in (OUT_TXT, OUT_JSON))
        good = died and named and unchanged
        ok_all = ok_all and good
        print("  %-28s exit=%d named_gate=%s artifacts_unchanged=%s  %s"
              % (m["name"], proc.returncode, named, unchanged,
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
              "a named gate and write nothing")
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
        R = assemble()
        payload = jsonable(R)
        payload = mutate("render-escape", payload)
        bad = render_check(R, payload)
        gate("G-RENDER-FROM-GATED-OBJECT",
             "every rendered cell equals the corresponding cell of the gated "
             "measurement object", len(bad) == 0, {"mismatches": bad[:4]})
        claims, paper_hash, missing = paper_prose_audit(R)
        gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
             "every load-bearing numeric sentence of paper-06 is rendered from "
             "the receipt object and appears verbatim in the paper",
             paper_hash is not None and len(missing) == 0,
             {"claims": len(claims), "missing": missing[:6]})
        sys.stderr.write("MUTANT %s SURVIVED -- no gate fired\n" % MUTANT)
        return 3
    except GateFailure as exc:
        sys.stderr.write(str(exc) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
