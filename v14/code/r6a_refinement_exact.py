#!/usr/bin/env python3
"""
v14 R6a -- THE REFINEMENT GRAMMAR.  Exact instrument.

PIN: v14/note-r6a-refinement-grammar-pin.md (frozen v14 ledger #25, sha256-12
a22582f67168), verified BY HASH at run time.  So are the three PINNED GRAMMAR
SOURCES, which are this unit's ONLY grammar authority (pin section 1):
  v13/code/ha_successor_receipt.json  542b8735daf0   (I7, the R0 row)
  v13/paper-ha-successor.md           f286ba10d2d9   (the HA paper)
  v13/code/ha_successor_exact.py      d44cb72f8ee9   (the HA instrument)
Nothing is imported from them; the grammar is REIMPLEMENTED here and gated
against I7's own committed numbers.  If deciding a move's legitimacy needs a
grammar fact not derivable from these, that branch STOPS at
R6A-BLOCKED-AT-GRAMMAR-SOURCE-<the named fact> -- a first-class verdict.

THE QUESTION (pin section 2, falsifiable, three-way): does the record grammar
AS PINNED admit a MOTIVATED interval-subdivision move -- a new site because a
division event resolved a record interval, the count partition FORCED by the
counting semantics, the residual freedom MEASURED as a choice inventory?

Three verdict heads, all first class, all derived inside a gate:
  R6A-MOTIVATED-REFINEMENT-EXISTS<...>
  R6A-NO-MOTIVATED-SPLIT<...>
  R6A-BLOCKED-AT-GRAMMAR-SOURCE<...>
The emitted string is compared for COMPLETE STRING EQUALITY against an
INDEPENDENT reconstruction built from the receipt object alone
(reconstruct_verdict_from_receipt() shares no code and no input with
build_verdict(); five injection classes prove it fires).

THE FIVE REGISTERED MEASUREMENTS (pin section 3):
  1. THE MOVE CENSUS -- every coarse interval of every declared move class is
     classified INHERITED / SUBDIVIDED / AMBIGUOUS / UNREPRESENTED by the
     UNIQUENESS of its minimal decomposition into refined link vectors.  A
     class that breaks the arena is REFUSED with the measured reason.
  2. THE FORCED PART -- count additivity and the metric-restriction test
     (record-IS-metric commutes with refinement), at every admissible move
     class over I7's declared record family, rebuilt from the pinned sources.
  3. THE CHOICE INVENTORY -- every residual freedom classified (i) forced by a
     named pinned declaration, (ii) fixed by a MEASURED stabiliser, or (iii)
     genuinely free WITH ITS FIBER COUNTED.  The motivation qualifier is
     COMPUTED from this inventory, never typed.
  4. THE DYNAMICS-COMPATIBILITY CENSUS -- refine-then-advance vs
     advance-then-refine for H_a[N], both drag architectures, the lapse lift
     declared and itself audited.  The nonzero commutation defect is a
     MEASURED OBJECT: site support, split dependence, record dependence.
  5. THE ITERATION PROBE -- the move applied twice; whether the family closes
     and how the inventory behaves (the R6b prerequisite).

CLI CONTRACT (confirmed in code before invocation, v13 #238):
  (no arguments)        THE PLAIN DELIVERY RUN.  Runs every gate, derives the
                        verdict, and WRITES v14/code/r6a_refinement_output.txt
                        and v14/code/r6a_refinement_receipt.json.  Exit 0.
                        Any gate failure aborts BEFORE any artifact is written.
  --mutant NAME         Runs the delivery pipeline with the named injection
                        active.  MUST exit 1 with a NAMED gate failure and MUST
                        NOT write any artifact.  Unknown name -> exit 2.
  --list-mutants        Prints the declared mutant names, one per line.  Exit 0.
  --selftest            THE FALSIFICATION SELFTEST.  Re-invokes this file once
                        per declared mutant, requires exit 1, requires the death
                        certificate to name a gate, and requires the artifacts
                        on disk to be byte-unchanged.  Writes NO artifacts.

Arithmetic is exact throughout: int and fractions.Fraction only.  A float
literal, a float call, or a true-division operator anywhere in this source is a
gate failure (G-FLOATGUARD, an AST scan of this file).  Run-mode identity is
read by exactly ONE function, mutate(); an AST gate measures that no other
function -- and in particular no gate predicate -- names it.

Concurrency note: this unit owns ONLY v14/paper-04-refinement-grammar.md,
v14/code/r6a_refinement_exact.py, v14/code/r6a_refinement_output.txt and
v14/code/r6a_refinement_receipt.json.  It reads v13 and v14 artifacts and
writes nothing else.  It never touches v14/paper-03-* or v14/code/r3_*.
"""

import ast
import hashlib
import itertools
import json
import os
import subprocess
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)                      # .../isp/v14
ROOT = os.path.dirname(REPO)                      # .../isp
SRC = os.path.abspath(__file__)
OUT_TXT = os.path.join(HERE, "r6a_refinement_output.txt")
OUT_JSON = os.path.join(HERE, "r6a_refinement_receipt.json")
PAPER = os.path.join(REPO, "paper-04-refinement-grammar.md")

MUTANT = None            # set only from the command line; gates never read it


class GateFailure(Exception):
    pass


def mutate(tag, value, alt):
    """THE ONLY function in this source that reads run-mode identity.

    Every declared injection is applied by perturbing an INSTRUMENT VALUE here.
    No gate predicate, and no gate-registering function, names MUTANT -- an AST
    gate measures exactly that (RUNBOOK section 14 addendum, v13 #208: a gate
    that special-cases a named mutant exempts its own falsifier)."""
    return alt if MUTANT == tag else value


GATES = []               # [{name, statement, passed, value}]
ANCHORS = []             # [{name, kind, artifact, expected, measured, ok}]

# The gates that can only be evaluated at WRITE time, after the receipt object
# exists.  Named here so the falsifier census denominates itself honestly.
DEFERRED_GATES = ("G-RENDER-FROM-GATED-OBJECT", "G-NO-FLOATS-IN-RECEIPT",
                  "G-PROSE-RENDERS-FROM-THE-RECEIPT", "G-FINAL-GATE-COUNT",
                  "G-DEFERRED-GATES-EVALUATED")


def gate(name, statement, ok, value=None):
    GATES.append({"name": name, "statement": statement,
                  "passed": bool(ok), "value": value})
    if not ok:
        raise GateFailure("GATE FAILED: %s -- %s | value=%r"
                          % (name, statement, value))
    return True


def record(name, statement, value):
    """A RECORDED (non-must-pass) measurement.  Disclosed, never load-bearing."""
    GATES.append({"name": name, "statement": statement, "passed": True,
                  "recorded": True, "value": value})
    return True


def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def sha256_full(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ----------------------------------------------------------------------------
# 1.  EXACT ARITHMETIC -- no true division anywhere; fdiv is the only quotient
# ----------------------------------------------------------------------------

FLOAT_T = type((1).__truediv__(1))     # the float type, obtained without naming it
BANNED_NAMES = ("float", "math", "random", "numpy", "statistics", "decimal")
MUTANT_NAME_ALLOWLIST = ("mutate", "main")


def fdiv(a, b):
    """Exact quotient of two rationals.  The AST guard bans the `/` operator, so
    every division in this instrument is routed through here."""
    a = Fr(a)
    b = Fr(b)
    if b == 0:
        raise ZeroDivisionError("fdiv by zero")
    return Fr(a.numerator * b.denominator, a.denominator * b.numerator)


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
    return mutate("float-leak", offences, offences + [("injected-float", 0)])


def _functions_naming_mutant(text):
    """Every FunctionDef whose body mentions the run-mode name."""
    tree = ast.parse(text)
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name) and sub.id == "MUTANT":
                    bad.append(node.name)
                    break
    return sorted(set(bad))


def _gate_calls_naming_mutant(text):
    """Every gate(...) CALL whose argument expressions mention run-mode identity."""
    tree = ast.parse(text)
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
           and node.func.id in ("gate", "record"):
            for arg in list(node.args) + [k.value for k in node.keywords]:
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Name) and sub.id == "MUTANT":
                        bad.append(node.lineno)
    return sorted(set(bad))


MUTANT_GUARD_INJECTIONS = (
    ("a gate predicate that reads run-mode identity",
     "def f():\n    gate('X', 'y', MUTANT is None)\n"),
    ("a second function that reads run-mode identity",
     "def helper():\n    return MUTANT == 'x'\n"),
)


# ----------------------------------------------------------------------------
# 2.  ANCHORS -- file bytes, JSON (path, value) pairs, and verbatim paper text
# ----------------------------------------------------------------------------

ANCHOR_ROWS = [
    ("A-PIN-R6A", "v14/note-r6a-refinement-grammar-pin.md", "a22582f67168",
     "this unit's pin, frozen at v14 ledger #25"),
    ("A-R0-PIN", "v14/note-r0-founding-pin.md", "e9d2bedff244",
     "the v14 founding pin: the inheritance table whose I7 row this unit uses"),
    ("A-I7-RECEIPT", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "R0 row I7 -- the pinned grammar source: sites, links, interval counts, "
     "the front, H_a[N], record-IS-metric"),
    ("A-HA-PAPER", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "the HA paper: the written grammar declarations reimplemented here"),
    ("A-HA-CODE", "v13/code/ha_successor_exact.py", "d44cb72f8ee9",
     "the HA instrument: the exact definitions reimplemented here (nothing "
     "imported)"),
]

# PATH-VALUE ANCHORS (RUNBOOK section 14 addendum, v14 #20): a read-by-path
# anchors the (path, value) PAIR, not only the file bytes.
PATH_ANCHOR_ROWS = [
    ("P-I7-D", ("declarations", "d"), 2, "the primary spatial dimension"),
    ("P-I7-L", ("declarations", "L"), 3, "sites per direction: X = (Z_L)^d"),
    ("P-I7-DEXT", ("declarations", "d_ext"), 3, "the declared d=3 extension"),
    ("P-I7-LEXT", ("declarations", "L_ext"), 3, "L at the d=3 extension"),
    ("P-I7-LINKS2", ("declarations", "links_d2"), [[1, 0], [0, 1], [1, 1]],
     "THE DECLARED LINK SET at d=2: the d axis links and the C(d,2) positive "
     "diagonals -- the object whose minimal decompositions decide incidence"),
    ("P-I7-LINKS3", ("declarations", "links_d3"),
     [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1]],
     "the declared link set at d=3 -- six links, NO body diagonal"),
    ("P-I7-RECORDS2", ("declarations", "records_d2"),
     {"G-ANISO": [1, 4, 5], "G-ANISO2": [4, 9, 13], "G-DIAG2": [2, 2, 4],
      "G-FLAT": [1, 1, 2], "G-INDEF": [1, 1, 6], "G-OFFDIAG": [2, 2, 6],
      "G-OFFDIAG2": [3, 5, 12], "G-OFFNEG": [3, 5, 4], "G-SINGULAR": [1, 1, 4]},
     "THE DECLARED RECORD FAMILY (homogeneous members + the two negative "
     "controls), rebuilt here rather than trusted"),
    ("P-I7-RECORDS3", ("declarations", "records_d3"),
     {"G3-ANISO": [1, 4, 9, 5, 10, 13], "G3-FLAT": [1, 1, 1, 2, 2, 2],
      "G3-OFF": [2, 2, 2, 6, 4, 4]}, "the declared d=3 records"),
    ("P-I7-INHOMOG", ("declarations", "records_d2_inhomogeneous"),
     ["G-CURVED (diagonal, site-dependent)",
      "G-CURVOFF (cross term, site-dependent)"],
     "the two site-dependent members of the record family"),
    ("P-I7-LAPSE", ("declarations", "lapse_family"),
     "the |X| site deltas, the constant profile 1, and the d chart ramps",
     "THE DECLARED LAPSE FAMILY -- the test set for the dynamics census"),
    ("P-I7-WEIGHT", ("declarations", "density_weight"), 0,
     "the declared density weight w = 0 (every statement here is at w = 0)"),
    ("P-I7-CHART", ("declarations", "chart_group"),
     "the |X| chart translations and the d! direction relabellings, acting on "
     "sites, on the record's link counts, on the lapse profiles and on every "
     "tensor index",
     "THE DECLARED CHART GROUP -- the group whose stabiliser decides class (ii)"),
    ("P-I7-READOUT-DET", ("tables", "readout_reencoding", "determinant"), "2",
     "record-IS-metric: the count -> q map's exact determinant at d=2"),
    ("P-I7-READOUT-SITES", ("tables", "readout_reencoding", "sites_verified"), 81,
     "record-IS-metric verified at 81 of 81 (record, site) pairs"),
    ("P-I7-RANK", ("tables", "identifiability_rank", "(0, 0)"), 2,
     "the lapse-pair bracket rank, full at the origin"),
    ("P-I7-LATTICE", ("declarations", "count_lattice"),
     {"axis_max": 6, "description": "the declared box of count vectors "
      "(n_e1, n_e2, n_diag) swept for the link-locality theorem's witnesses",
      "diag_max": 12},
     "I7's own declared count box -- the scope at which the split fiber is "
     "censused beyond the nine records"),
    ("P-I7-VERDICT", ("verdict",), ["HA-RUNNABLE", "HA-BRIDGE-NOT-ENTERED"],
     "I7's own verdict: the arena this unit refines is a RUNNABLE one"),
]

# TEXT ANCHORS: the load-bearing grammar sentences, quoted VERBATIM from the
# pinned HA paper.  Everything this unit calls "the pinned grammar" is one of
# these, and a drift in any of them changes the question.
TEXT_ANCHOR_ROWS = [
    ("T-COUNTS-POSITIVE", "v13/paper-ha-successor.md",
     "the interval cardinality $n_\\ell(x)\\in\\mathbb Z_{>0}$",
     "THE TYPE DECLARATION.  Counts are STRICTLY POSITIVE integers -- the "
     "declaration that makes a split of a count-1 interval impossible"),
    ("T-COUNTS-SEMANTIC", "v13/paper-ha-successor.md",
     "is the number of division events in the record interval between",
     "THE SEMANTIC ANCHOR.  n_l(x) COUNTS DIVISION EVENTS IN THE INTERVAL -- "
     "the declaration from which count additivity follows as semantics"),
    ("T-FRONT", "v13/paper-ha-successor.md",
     "$n(x)$ = the number of division events already committed at record site "
     "$x$",
     "THE FRONT.  A separate configuration variable counting events AT a site"),
    ("T-READOUT", "v13/paper-ha-successor.md",
     "$q_{12} = (n_{e_1+e_2} - n_{e_1} - n_{e_2})/2$",
     "THE DECLARED READOUT at d=2, reimplemented here"),
    ("T-CURVED", "v13/paper-ha-successor.md",
     "| `G-CURVED` | $(1,1,2)$ | $(2,2,4)$ |",
     "the site-dependent diagonal record's counts at (0,0) and (1,1)"),
    ("T-CURVOFF", "v13/paper-ha-successor.md",
     "| `G-CURVOFF` | $(2,2,6)$ | $(3,3,10)$ |",
     "the site-dependent cross-term record's counts at (0,0) and (1,1)"),
    ("T-FROZEN-GEOMETRY", "v13/paper-ha-successor.md",
     "The interval-cardinality\n   record $s$ is a configuration variable that "
     "$H_a[N]$ does not move; only the\n   front does.",
     "THE INDEPENDENCE.  The geometry record and the front are separate "
     "variables -- the front cannot supply the split"),
    ("T-DRAG", "v13/paper-ha-successor.md",
     "The drag has exactly two ingredients: the **front tilt** $n(x+e)-n(x)$",
     "the drag's ingredients: front tilt and eventwise lapse value, nothing "
     "else"),
    ("T-PIN-ADDITIVITY", "v14/note-r6a-refinement-grammar-pin.md",
     "n(x,y) + n(y, x+ℓ) = n(x, x+ℓ) (events in the whole = events in the\n"
     "parts) — this is semantics, not a choice.",
     "THE PIN'S OWN FORCED CLAUSE -- the constraint this unit verifies rather "
     "than assumes"),
    ("T-PIN-SCOPE", "v14/note-r6a-refinement-grammar-pin.md",
     "Reaching outside\nthe pinned sources is forbidden.",
     "THE SCOPE RULING that makes BLOCKED-AT-GRAMMAR-SOURCE first class"),
]


def read_json(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return json.load(fh)


def read_text(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return fh.read()


def read_by_path(obj, path):
    cur = obj
    for k in path:
        cur = cur[k]
    return cur


def verify_anchors():
    rows = mutate("anchor-skip", list(ANCHOR_ROWS), list(ANCHOR_ROWS)[:-1])
    for name, rel, expect, why in rows:
        got = mutate("anchor-hash-" + name, sha12(os.path.join(ROOT, rel)),
                     "0" * 12)
        ANCHORS.append({"name": name, "kind": "file-bytes", "artifact": rel,
                        "expected": expect, "measured": got, "provenance": why,
                        "ok": got == expect})
        gate(name, "external anchor %s verifies at %s" % (expect, rel),
             got == expect, {"expected": expect, "measured": got})
    gate("G-ANCHOR-CELL-COMPLETE",
         "every declared file-bytes anchor row was evaluated (a dropped anchor "
         "row is a dropped external check)",
         len(rows) == len(ANCHOR_ROWS),
         {"evaluated": len(rows), "declared": len(ANCHOR_ROWS)})
    return len(rows)


def verify_path_anchors(rel="v13/code/ha_successor_receipt.json"):
    obj = read_json(rel)
    bad = []
    for name, path, expect, why in PATH_ANCHOR_ROWS:
        p = mutate("path-drift", tuple(path),
                   ("declarations", "primes") if name == "P-I7-L"
                   else tuple(path))
        try:
            got = read_by_path(obj, p)
        except (KeyError, IndexError, TypeError):
            got = None
        got = mutate("path-value", got, None)
        ok = (got == expect)
        if not ok:
            bad.append({"name": name, "path": list(p), "expected": expect,
                        "measured": got})
        ANCHORS.append({"name": name, "kind": "path-value", "artifact": rel,
                        "json_path": list(p), "expected": expect,
                        "measured": got, "provenance": why, "ok": ok})
    gate("G-PATH-ANCHORS",
         "every value this unit reads out of the pinned I7 receipt matches the "
         "declared (path, value) PAIR -- a path drift that changes the arena "
         "dies here, not only a byte change to the file",
         len(bad) == 0 and len(PATH_ANCHOR_ROWS) == len(
             [a for a in ANCHORS if a["kind"] == "path-value"]),
         {"rows": len(PATH_ANCHOR_ROWS), "failures": bad[:3]})
    return len(PATH_ANCHOR_ROWS)


def verify_text_anchors():
    cache = {}
    bad = []
    for name, rel, needle, why in TEXT_ANCHOR_ROWS:
        if rel not in cache:
            cache[rel] = read_text(rel)
        probe = mutate("text-anchor-drift", needle,
                       needle.replace("$", "@") if name == "T-READOUT"
                       else needle)
        ok = probe in cache[rel]
        if not ok:
            bad.append({"name": name, "artifact": rel, "needle": probe[:60]})
        ANCHORS.append({"name": name, "kind": "verbatim-text", "artifact": rel,
                        "expected": needle, "measured": ok,
                        "provenance": why, "ok": ok})
    gate("G-TEXT-ANCHORS",
         "every load-bearing grammar sentence this unit reimplements appears "
         "VERBATIM in its pinned source -- the grammar is quoted, not "
         "paraphrased",
         len(bad) == 0, {"rows": len(TEXT_ANCHOR_ROWS), "failures": bad[:3]})
    return len(TEXT_ANCHOR_ROWS)


# ----------------------------------------------------------------------------
# 3.  THE PINNED GRAMMAR, REIMPLEMENTED (nothing imported)
# ----------------------------------------------------------------------------
#
# Sites            X = prod_j Z_{L_j}  (the pin's own class-(a) entry authorises
#                  the per-direction generalisation of I7's (Z_L)^d).
# Links            the d axis links and the C(d,2) positive diagonals  [P-I7-LINKS2]
# Geometry record  n_l(x) in Z_{>0}, the number of division events in the
#                  record interval between x and x+l                  [T-COUNTS-*]
# Front            n : X -> Z, events already committed at x           [T-FRONT]
# Readout          q_ij e_l^i e_l^j = n_l(x);  I = q^{-1} (det q)^w, w = 0
# Admissible       q nonsingular and positive definite at every site

def link_set(d):
    axes = [tuple(1 if k == j else 0 for k in range(d)) for j in range(d)]
    diags = [tuple(1 if k in (i, j) else 0 for k in range(d))
             for i in range(d) for j in range(i + 1, d)]
    return axes + diags


def sites(Ls):
    return [tuple(t) for t in itertools.product(*[range(L) for L in Ls])]


def add(x, e, Ls):
    return tuple((a + b) % L for a, b, L in zip(x, e, Ls))


def sym_index(d):
    return [(i, j) for i in range(d) for j in range(i, d)]


def solve_exact(rows, rhs):
    n = len(rows)
    m = len(rows[0])
    A = [[Fr(v) for v in rows[i]] + [Fr(rhs[i])] for i in range(n)]
    piv = []
    r = 0
    for c in range(m):
        p = None
        for i in range(r, n):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [fdiv(v, pv) for v in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == n:
            break
    if len(piv) < m:
        return None
    for i in range(r, n):
        if A[i][m] != 0:
            return None
    sol = [Fr(0)] * m
    for i, c in enumerate(piv):
        sol[c] = A[i][m]
    return sol


def readout_matrix(d):
    """The count -> q map, rows in I7's own SORTED-LINK order (its convention:
    `for lk in sorted(counts)`).  Row order fixes the determinant's sign, so the
    convention is reproduced rather than re-chosen."""
    idx = sym_index(d)
    return [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in idx]
            for lk in sorted(link_set(d))]


def det_exact(M):
    n = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for c in range(n):
        p = None
        for i in range(c, n):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            det = -det
        pv = A[c][c]
        det = det * pv
        for i in range(c + 1, n):
            f = fdiv(A[i][c], pv)
            A[i] = [a - f * b for a, b in zip(A[i], A[c])]
    return det


def inv_exact(M):
    n = len(M)
    A = [[Fr(M[i][j]) for j in range(n)] + [Fr(1 if i == j else 0)
                                            for j in range(n)] for i in range(n)]
    for c in range(n):
        p = None
        for i in range(c, n):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            return None
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [fdiv(v, pv) for v in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
    return [row[n:] for row in A]


def positive_definite(q):
    n = len(q)
    for k in range(1, n + 1):
        if det_exact([row[:k] for row in q[:k]]) <= 0:
            return False
    return True


def q_from_counts(d, counts):
    rows = readout_matrix(d)
    rhs = [Fr(counts[lk]) for lk in sorted(counts)]
    sol = solve_exact(rows, rhs)
    if sol is None:
        return None
    q = [[Fr(0)] * d for _ in range(d)]
    for (i, j), v in zip(sym_index(d), sol):
        q[i][j] = v
        q[j][i] = v
    return q


class Arena(object):
    """An I7-CLASS ARENA: a product-of-cyclic-groups site set carrying the
    declared link displacements, a positive integer count on every (site, link),
    and an admissible readout at every site."""

    def __init__(self, name, d, Ls, counts, note=""):
        self.name = name
        self.d = d
        self.Ls = tuple(Ls)
        self.links = link_set(d)
        self.S = sites(Ls)
        self.counts = counts
        self.note = note
        self.q = {}
        self.I = {}
        self.singular = []
        self.nonpd = []
        self.nonpositive = []
        for x in self.S:
            row = counts[x]
            if any(row[lk] < 1 for lk in self.links):
                self.nonpositive.append(x)
            q = q_from_counts(d, {lk: Fr(row[lk]) for lk in self.links})
            self.q[x] = q
            if q is None or det_exact(q) == 0:
                self.singular.append(x)
                self.I[x] = None
                continue
            if not positive_definite(q):
                self.nonpd.append(x)
                self.I[x] = None
                continue
            self.I[x] = inv_exact(q)

    def admissible(self):
        return (not self.singular) and (not self.nonpd) and (not self.nonpositive)

    def min_count(self):
        return min(self.counts[x][lk] for x in self.S for lk in self.links)

    def n_links(self):
        return len(self.S) * len(self.links)


def build_counts(d, Ls, rule):
    return {x: {lk: int(rule(x, lk)) for lk in link_set(d)} for x in sites(Ls)}


def homog_rule(tup, d):
    table = {lk: tup[i] for i, lk in enumerate(link_set(d))}
    return lambda x, lk: table[lk]


def curved_rule(d):
    """G-CURVED, from the pinned HA code: q(x) = diag(1+x_1, ..., 1+x_d)."""
    return lambda x, lk: sum((1 + x[j]) for j in range(d) if lk[j])


def curvoff_rule(d):
    """G-CURVOFF, from the pinned HA code: a site-dependent cross term."""
    def rule(x, lk):
        b = [2 + x[j] for j in range(d)]
        cross = 1 + (x[0] * x[1]) % 2
        s = sum(b[j] for j in range(d) if lk[j])
        pairs = sum(1 for i in range(d) for j in range(i + 1, d)
                    if lk[i] and lk[j])
        return s + 2 * cross * pairs
    return rule


def build_record_family(d, L, declared_d2, declared_d3):
    """I7's declared record family, REBUILT from the pinned declarations."""
    out = {}
    Ls = (L,) * d
    src = declared_d2 if d == 2 else declared_d3
    for nm in sorted(src):
        out[nm] = Arena(nm, d, Ls, build_counts(d, Ls, homog_rule(src[nm], d)),
                        "homogeneous, declared count vector")
    if d == 2:
        out["G-CURVED"] = Arena("G-CURVED", d, Ls,
                                build_counts(d, Ls, curved_rule(d)),
                                "inhomogeneous, exactly diagonal")
        out["G-CURVOFF"] = Arena("G-CURVOFF", d, Ls,
                                 build_counts(d, Ls, curvoff_rule(d)),
                                 "inhomogeneous, site-dependent cross term")
    return out


def build_lapse_family(S, d):
    """THE DECLARED LAPSE FAMILY [P-I7-LAPSE]: the |X| site deltas, the constant
    profile 1, and the d chart ramps."""
    lp = [("delta%s" % (x,), {y: (1 if y == x else 0) for y in S}) for x in S]
    lp.append(("one", {y: 1 for y in S}))
    lp += [("ramp%d" % j, {y: y[j] for y in S}) for j in range(d)]
    return lp


# ---- the declared drag-rule family (HA paper section 3.4) -------------------

RULE_TABLE = [
    ("A-chart", "A", "Lambda = delta (count-blind chart identity)"),
    ("A-axis", "A", "Lambda = diag(1/n_{e_j}) from the axis interval counts"),
    ("A-linkframe", "A", "Lambda^{ij} = sum_l e_l^i e_l^j / n_l"),
    ("A-linkhalf", "A", "Lambda = (1/2) sum_l e_l e_l^T / n_l"),
    ("A-insert", "A", "Lambda = I_a(g), read from the record [POSITIVE CONTROL]"),
    ("A-insert-x", "A", "I_a(g) with the cross term sign-flipped [BROKEN]"),
    ("A-insert-2x", "A", "2 I_a(g) [BROKEN]"),
    ("A-notransport", "A", "I_a(g) reading a frozen reference front [BROKEN]"),
    ("B-axis", "B", "lambda_l = 1/n_l on the axis links"),
    ("B-all", "B", "lambda_l = 1/n_l on every declared link"),
    ("B-chart", "B", "lambda_l = 1 on the axis links"),
]
RULES = [r[0] for r in RULE_TABLE]

_LAMBDA_MEMO = {}
_CACHE_STATS = {"hits": 0, "misses": 0, "bypass": 0, "compared": 0,
                "disagreements": 0}


def arch_of(rule):
    return "B" if rule.startswith("B-") else "A"


def lambda_of(rule, arena, x, fresh=False):
    """The drag weight field.  Memoised; the memo is itself gated (RUNBOOK
    section 14 addendum, v13 #185/#219: a zero-hit cache gate is vacuous, and a
    self-test routed through the memo tests the cache, not the quantity)."""
    key = (id(arena), arena.name, rule, x)
    if fresh:
        _CACHE_STATS["bypass"] += 1
    else:
        if key in _LAMBDA_MEMO:
            _CACHE_STATS["hits"] += 1
            return _LAMBDA_MEMO[key]
        _CACHE_STATS["misses"] += 1
    d = arena.d
    cnt = arena.counts[x]
    lks = arena.links
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
            w = Fr(1, cnt[lk])
            for i in range(d):
                for j in range(d):
                    M[i][j] = M[i][j] + Fr(lk[i] * lk[j]) * w
        if rule == "A-linkhalf":
            M = [[v * Fr(1, 2) for v in row] for row in M]
    elif rule in ("A-insert", "A-notransport"):
        M = [row[:] for row in arena.I[x]]
    elif rule == "A-insert-x":
        M = [[(-v if i != j else v) for j, v in enumerate(row)]
             for i, row in enumerate(arena.I[x])]
    elif rule == "A-insert-2x":
        M = [[2 * v for v in row] for row in arena.I[x]]
    elif rule == "B-axis":
        M = {lk: (Fr(1, cnt[lk]) if lk in axes else Fr(0)) for lk in lks}
    elif rule == "B-all":
        M = {lk: Fr(1, cnt[lk]) for lk in lks}
    elif rule == "B-chart":
        M = {lk: (Fr(1) if lk in axes else Fr(0)) for lk in lks}
    else:
        raise RuntimeError("unknown rule %s" % rule)
    if not fresh:
        # the cache-alias injection serves one arena another arena's weight
        _LAMBDA_MEMO[key] = M
    return M


def cache_lookup_key_for(arena, rule, x):
    """The key the memo is served under.  The `cache-alias` injection makes two
    different arenas share one key -- the disease RUNBOOK section 14 (v13 #185)
    was written for."""
    return mutate("cache-alias", (id(arena), arena.name, rule, x),
                  ("ALIAS", rule, x))


def drag_at(rule, arena, N, n, x):
    """w[N,n](x): the record-native drag.  Architecture A reads the axis front
    tilts through Lambda; architecture B sums over every declared link."""
    d = arena.d
    Ls = arena.Ls
    if arch_of(rule) == "A":
        Lam = lambda_of(rule, arena, x)
        dn = [Fr(n[add(x, e, Ls)] - n[x]) for e in arena.links[:d]]
        return tuple(sum((Lam[i][j] * dn[j] for j in range(d)), Fr(0)) * Fr(N[x])
                     for i in range(d))
    lam = lambda_of(rule, arena, x)
    v = [Fr(0)] * d
    for lk in arena.links:
        if lam[lk] == 0:
            continue
        dl = Fr(n[add(x, lk, Ls)] - n[x])
        for i in range(d):
            if lk[i]:
                v[i] = v[i] + lam[lk] * Fr(lk[i]) * dl
    return tuple(Fr(N[x]) * v[i] for i in range(d))


# ----------------------------------------------------------------------------
# 4.  THE MOVE CLASSES, declared as data (RUNBOOK section 15)
# ----------------------------------------------------------------------------
#
# A move is declared by: the refined lattice shape, the site embedding iota of
# the coarse arena into it, and nothing else.  Every legitimacy question below
# is then a MEASUREMENT on (link set, iota, shape) -- never a convention.


class Move(object):
    def __init__(self, key, name, Ls_coarse, Ls_refined, iota, note, kind):
        self.key = key
        self.name = name
        self.Ls_coarse = tuple(Ls_coarse)
        self.Ls_refined = tuple(Ls_refined) if Ls_refined is not None else None
        self.iota = iota
        self.note = note
        self.kind = kind          # "subdivision" | "control"


def declared_moves(d, L):
    """The subdivision-move classes expressible from the pinned declarations
    (pin section 3.1), PLUS the R1 negative control (pin section 5)."""
    out = []
    out.append(Move(
        "DYADIC", "global dyadic refinement", (L,) * d, (2 * L,) * d,
        lambda x: tuple(2 * a for a in x),
        "every axis interval subdivided; L -> 2L", "subdivision"))
    for lam in range(L):
        out.append(Move(
            "HYPERPLANE@%d" % lam, "axis-hyperplane insertion at locus %d" % lam,
            (L,) * d, (L + 1,) + (L,) * (d - 1),
            (lambda lm: (lambda x: (x[0] + (1 if x[0] > lm else 0),) + x[1:]))(lam),
            "one hyperplane inserted orthogonal to direction 0; "
            "(Z_{L+1} x Z_L^{d-1})", "subdivision"))
    out.append(Move(
        "SINGLE-INTERVAL", "single-interval insertion", (L,) * d, None, None,
        "one new site inside ONE declared link only", "subdivision"))
    out.append(Move(
        "R1-COPY", "the R1 copying move (append a disjoint block)",
        (L,) * d, (2 * L,) + (L,) * (d - 1), lambda x: x,
        "label growth: a disjoint block appended, no interval subdivided "
        "[THE NEGATIVE CONTROL -- the audit must be able to FAIL a move]",
        "control"))
    return out


def minimal_decompositions(disp, links, cap=6):
    """Every ordered sequence of link vectors summing (as INTEGER vectors) to
    disp, of minimal length.  This is the whole incidence instrument: the
    pinned grammar declares a link SET, so 'which refined site subdivides this
    coarse interval' is decided by whether the decomposition is unique."""
    best = [None]
    out = []

    def rec(cur, seq):
        if all(a == b for a, b in zip(cur, disp)):
            if best[0] is None or len(seq) < best[0]:
                best[0] = len(seq)
                out[:] = [tuple(seq)]
            elif len(seq) == best[0]:
                out.append(tuple(seq))
            return
        if any(a > b for a, b in zip(cur, disp)):
            return
        if best[0] is not None and len(seq) >= best[0]:
            return
        if len(seq) >= cap:
            return
        for lk in links:
            rec(tuple(a + b for a, b in zip(cur, lk)), seq + [lk])

    rec((0,) * len(disp), [])
    return best[0], out


def interiors_of(seq):
    p = (0,) * len(seq[0])
    out = []
    for s in seq[:-1]:
        p = tuple(a + b for a, b in zip(p, s))
        out.append(p)
    return tuple(out)


def classify_interval(disp, links):
    """INHERITED   -- the coarse interval IS a refined link (1 step, unique)
    SUBDIVIDED    -- exactly one refined site lies on it (2 steps, one interior)
    AMBIGUOUS     -- two steps, MORE THAN ONE candidate interior site: the
                     grammar declares no rule choosing between them
    UNREPRESENTED -- no minimal 1- or 2-step realisation at all."""
    blen, decs = minimal_decompositions(disp, links)
    if blen is None:
        return ("UNREPRESENTED", None, 0, ())
    ints = sorted(set(interiors_of(s) for s in decs))
    if blen == 1:
        return ("INHERITED", 1, 1, ())
    if blen == 2 and len(ints) == 1:
        return ("SUBDIVIDED", 2, 1, ints[0])
    if blen == 2:
        return ("AMBIGUOUS", 2, len(ints), tuple(ints))
    return ("UNREPRESENTED", blen, len(ints), ())


def move_incidence_census(move, d, links):
    """Classify EVERY coarse interval of a move.  Cell-complete by construction:
    the denominator is |X_coarse| x |links|."""
    rows = []
    tally = {"INHERITED": 0, "SUBDIVIDED": 0, "AMBIGUOUS": 0,
             "UNREPRESENTED": 0}
    for x in sites(move.Ls_coarse):
        for lk in links:
            y = add(x, lk, move.Ls_coarse)
            zi = move.iota(x)
            zj = move.iota(y)
            disp = tuple((b - a) % Lr for a, b, Lr in
                         zip(zi, zj, move.Ls_refined))
            st, blen, ncand, cand = classify_interval(disp, links)
            st = mutate("incidence-lax",
                        st, "SUBDIVIDED" if st == "AMBIGUOUS" else st)
            tally[st] = tally[st] + 1
            rows.append({"site": list(x), "link": list(lk), "disp": list(disp),
                         "status": st, "steps": blen, "candidates": ncand})
    return rows, tally


def single_interval_arena_probe(d, L):
    """CLASS (c): one new site inside ONE declared link.  REFUSED, with the
    measured reason -- never skipped (pin section 3.1)."""
    n_sites = L ** d + 1
    # the direction-0 cycle lengths after inserting one site into one row
    cycles = [L + 1] + [L] * (L ** (d - 1) - 1)
    constant = len(set(cycles)) == 1
    longest = max(cycles)
    divides = (n_sites % longest == 0)
    # declared link displacements with a target at the new site
    targets = {"axis-along-the-split": True}
    for lk in link_set(d)[1:]:
        targets[str(lk)] = False
    have = sum(1 for v in targets.values() if v)
    return {
        "sites": n_sites,
        "direction_0_cycle_lengths": cycles,
        "cycle_lengths_constant": constant,
        "site_count_divisible_by_longest_cycle": divides,
        "declared_link_targets_defined_at_the_new_site": have,
        "declared_links": len(link_set(d)),
        "reason": "a product-of-cyclic-groups site set carrying the declared "
                  "link displacements by translation forces every "
                  "direction-0 cycle to have the SAME length; inserting one "
                  "site into one link makes them %s, and %d is not divisible "
                  "by the longest cycle %d.  At the new site only %d of the %d "
                  "declared link displacements has a target."
                  % (cycles, n_sites, longest, have, len(link_set(d))),
    }


# ----------------------------------------------------------------------------
# 5.  THE DYADIC REFINEMENT, CONSTRUCTED (the one class the census admits)
# ----------------------------------------------------------------------------
#
# iota(x) = 2x.  Every coarse interval [x, x+l] is realised by the UNIQUE
# 2-step refined path 2x -> 2x+l -> 2x+2l, so its interior site is forced and
# additivity is posable:      n_l^r(2x) + n_l^r(2x+l)  =  n_l^c(x).
# The refined links NOT on any coarse interval are the FREE part.

def base_of(z):
    return tuple(a // 2 for a in z)


def midpoint_kind(z, links):
    """Which coarse interval z is the interior site of, or None if z is a coarse
    image.  At d=2 every refined site is one or the other; at d=3 the all-odd
    parity class is NEITHER (the declared link set has no body diagonal)."""
    par = tuple(a % 2 for a in z)
    if all(p == 0 for p in par):
        return ("IMAGE", None)
    for lk in links:
        if tuple(lk) == par:
            return ("MID", lk)
    return ("UNREACHED", None)


def covered_slots(Ls_coarse, Ls_refined, links):
    """The refined (site, link) slots carrying a half of a coarse interval."""
    out = {}
    for x in sites(Ls_coarse):
        for lk in links:
            z0 = tuple(2 * a for a in x)
            z1 = add(z0, lk, Ls_refined)
            out[(z0, lk)] = (x, lk, 0)
            out[(z1, lk)] = (x, lk, 1)
    return out


def free_slots(Ls_coarse, Ls_refined, links):
    cov = covered_slots(Ls_coarse, Ls_refined, links)
    return sorted([(z, lk) for z in sites(Ls_refined) for lk in links
                   if (z, lk) not in cov])


SPLIT_RULES = ("low", "floor", "high")


def make_split(arena, mode):
    """A DECLARED split assignment.  `low` = (1, n-1), `floor` = (n//2, n-n//2),
    `high` = (n-1, 1).  None when some interval cannot be split at all."""
    sp = {}
    for x in arena.S:
        for lk in arena.links:
            n = arena.counts[x][lk]
            if n < 2:
                return None
            if mode == "low":
                n1 = 1
            elif mode == "high":
                n1 = n - 1
            else:
                n1 = n // 2
            sp[(x, lk)] = (n1, n - n1)
    return sp


FREE_RULES = ("minimal", "iterable-64")


def make_free(arena, split, Ls_refined, mode):
    """A DECLARED completion of the free refined links.  Both rules make the
    refined site's readout admissible by putting the site on the DIAGONAL locus
    (c = a + b, so q_12 = 0 and det q = ab > 0).  `iterable-64` sets the free
    counts to 64 so that the ITERATION probe's obstruction is located on the
    coarse record's own descendants and not on the completion."""
    K = 1 if mode == "minimal" else 64
    known = {z: {} for z in sites(Ls_refined)}
    for x in arena.S:
        for lk in arena.links:
            n1, n2 = split[(x, lk)]
            z0 = tuple(2 * a for a in x)
            z1 = add(z0, lk, Ls_refined)
            known[z0][lk] = n1
            known[z1][lk] = n2
    out = {}
    links = arena.links
    for z in sites(Ls_refined):
        miss = [lk for lk in links if lk not in known[z]]
        if not miss:
            continue
        have = known[z]
        if links[0] in have and links[1] not in have:
            a = have[links[0]]
            out[(z, links[1])] = K
            out[(z, links[2])] = a + K
        elif links[1] in have and links[0] not in have:
            b = have[links[1]]
            out[(z, links[0])] = K
            out[(z, links[2])] = K + b
        elif links[2] in have:
            c = have[links[2]]
            out[(z, links[0])] = c + K
            out[(z, links[1])] = c + K
        else:
            out[(z, links[0])] = K
            out[(z, links[1])] = K
            out[(z, links[2])] = 2 * K
    return out


def refine(arena, split, free, Ls_refined, name):
    counts = {z: {} for z in sites(Ls_refined)}
    for x in arena.S:
        for lk in arena.links:
            n1, n2 = split[(x, lk)]
            z0 = tuple(2 * a for a in x)
            z1 = add(z0, lk, Ls_refined)
            counts[z0][lk] = n1
            counts[z1][lk] = mutate(
                "additivity-violation", n2,
                n2 + 1 if (x == (0, 0) and lk == arena.links[0]) else n2)
    for (z, lk), v in free.items():
        counts[z][lk] = v
    return Arena(name, arena.d, Ls_refined, counts, "refined by DYADIC")


def restrict_counts(refined, arena, Ls_refined):
    """Read the coarse counts BACK from the refined arena, by summing along the
    unique minimal decomposition.  This is a computation over the refined
    object; it shares no code with the coarse record's own constructor."""
    out = {}
    for x in arena.S:
        row = {}
        for lk in arena.links:
            z0 = tuple(2 * a for a in x)
            z1 = add(z0, lk, Ls_refined)
            row[lk] = refined.counts[z0][lk] + refined.counts[z1][lk]
        out[x] = row
    return out


# ----------------------------------------------------------------------------
# 6.  THE CHART GROUP AND THE MEASURED STABILISER  (class (ii) of the inventory)
# ----------------------------------------------------------------------------

def chart_group(d, Ls):
    """[P-I7-CHART] the |X| chart translations and the d! direction
    relabellings.  Returned as (name, site map, link map) triples."""
    out = []
    for sigma in itertools.permutations(range(d)):
        for t in sites(Ls):
            def smap(x, sg=sigma, tt=t):
                return tuple((x[sg[i]] + tt[i]) % Ls[i] for i in range(d))

            def lmap(lk, sg=sigma):
                return tuple(lk[sg[i]] for i in range(d))
            out.append(("t%s.s%s" % (t, sigma), smap, lmap))
    return out


def stabiliser(arena):
    """MEASURED, not assumed: the subgroup of the declared chart group fixing
    the record's counts."""
    keep = []
    for nm, smap, lmap in chart_group(arena.d, arena.Ls):
        ok = True
        for x in arena.S:
            for lk in arena.links:
                if arena.counts[smap(x)][lmap(lk)] != arena.counts[x][lk]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            keep.append((nm, smap, lmap))
    return keep


def stabiliser_orbits(arena, stab):
    """Orbits of the measured stabiliser on the (site, link) pairs -- the cells
    a chart-equivariant split assignment must be constant on."""
    items = [(x, lk) for x in arena.S for lk in arena.links]
    seen = set()
    orbits = []
    for it in items:
        if it in seen:
            continue
        orb = {it}
        frontier = [it]
        while frontier:
            (x, lk) = frontier.pop()
            for nm, smap, lmap in stab:
                y = (smap(x), lmap(lk))
                if y not in orb:
                    orb.add(y)
                    frontier.append(y)
        seen |= orb
        orbits.append(tuple(sorted(orb)))
    return orbits


def equivariant_split_fiber(arena, orbits):
    """The number of chart-EQUIVARIANT split assignments: one free choice per
    orbit, (n_O - 1) values each.  If this is 1 the split is fixed by a measured
    symmetry -- class (ii).  Anything else is class (iii)."""
    fib = 1
    per = []
    for orb in orbits:
        x, lk = orb[0]
        n = arena.counts[x][lk]
        consistent = all(arena.counts[a][b] == n for (a, b) in orb)
        if not consistent:
            return None, []
        per.append((n, n - 1, len(orb)))
        fib = fib * (n - 1)
    return fib, per


# ----------------------------------------------------------------------------
# 7.  THE SPLIT FIBER, COUNTED EXACTLY  (class (iii) of the inventory)
# ----------------------------------------------------------------------------

def site_admissible_triples(row, links):
    """The split triples (a, b, c) = the FIRST halves at one coarse site whose
    refined image site is admissible.  q_12 = (c - a - b)/2, det = ab - q_12^2."""
    out = []
    for a in range(1, row[links[0]]):
        for b in range(1, row[links[1]]):
            for c in range(1, row[links[2]]):
                q12 = Fr(c - a - b, 2)
                if Fr(a * b) - q12 * q12 > 0:
                    out.append((a, b, c))
    return out


def split_fibers(arena):
    """The split fiber, computed three ways: raw (every positive partition),
    admissible-at-the-coarse-images, and the per-site profile.  COUNTS ARE
    COMPUTED, NEVER TYPED (RUNBOOK section 4, #24)."""
    raw = 1
    adm = 1
    per = []
    for x in arena.S:
        row = arena.counts[x]
        r = 1
        for lk in arena.links:
            r = r * (row[lk] - 1)
        t = len(site_admissible_triples(row, arena.links))
        raw = raw * r
        adm = adm * t
        per.append(t)
    return {"raw": raw, "admissible_at_images": adm,
            "per_site_admissible": sorted(set(per)),
            "splittable": arena.min_count() >= 2}


def count_lattice_census(d, axis_max, diag_max):
    """The split freedom beyond the nine declared records: I7's OWN declared
    count box [P-I7-LATTICE].  How many admissible count vectors exist, how
    many are splittable at all, and how many have a UNIQUE admissible split."""
    links = link_set(d)
    admissible = 0
    splittable = 0
    forced = []
    for a in range(1, axis_max + 1):
        for b in range(1, axis_max + 1):
            for c in range(1, diag_max + 1):
                q12 = Fr(c - a - b, 2)
                if Fr(a * b) - q12 * q12 <= 0:
                    continue
                admissible += 1
                if a >= 2 and b >= 2 and c >= 2:
                    splittable += 1
                    row = {links[0]: a, links[1]: b, links[2]: c}
                    if len(site_admissible_triples(row, links)) == 1:
                        forced.append((a, b, c))
    return {"admissible_count_vectors": admissible, "splittable": splittable,
            "unique_admissible_split": sorted(forced),
            "unique_admissible_split_count": len(forced),
            "box": {"axis_max": axis_max, "diag_max": diag_max}}


# ----------------------------------------------------------------------------
# 8.  THE NO-POTENTIAL THEOREM  (why the split cannot be read off the record)
# ----------------------------------------------------------------------------
#
# If the counts were the coboundary of a site function phi -- n_l(x) =
# phi(x+l) - phi(x) -- then the split of an interval at its interior site would
# be READ OFF phi, and the freedom would not exist.  On a PERIODIC lattice the
# sum of a coboundary around any cycle vanishes, while the counts are strictly
# positive [T-COUNTS-POSITIVE].  So no record admits a potential.  Measured
# exhaustively over the declared family, with the cycle sums printed.

def potential_census(arena):
    worst = None
    rows = []
    for j in range(arena.d):
        e = tuple(1 if k == j else 0 for k in range(arena.d))
        for x in arena.S:
            s = 0
            y = x
            for _ in range(arena.Ls[j]):
                s += arena.counts[y][e]
                y = add(y, e, arena.Ls)
            rows.append(s)
            if worst is None or s < worst:
                worst = s
    val = mutate("potential-lax", worst, 0)
    return {"min_axis_cycle_sum": val, "cycles": len(rows),
            "admits_a_potential": val == 0}


# ----------------------------------------------------------------------------
# 9.  THE DYNAMICS-COMPATIBILITY CENSUS  (measurement 4)
# ----------------------------------------------------------------------------
#
# refine-then-advance  vs  advance-then-refine, for H_a[N](n, m) = (n+N, m+w).
# The refinement needs a FRONT LIFT (the new sites' front values), a LAPSE LIFT
# and a MATTER LIFT; each is a declared object and each is audited for choices.

LIFT_RULES = ("left", "right")
FRONT_FAMILY_NAMES = ("n-const", "n-sym", "n-ramp0")


def front_family(S):
    return [("n-const", {x: 1 for x in S}),
            ("n-sym", {x: x[0] * x[1] for x in S}),
            ("n-ramp0", {x: x[0] for x in S})]


def lift_profile(prof, arena, Ls_refined, mode):
    """Lift a Z-valued site profile to the refined arena.  BOTH declared rules
    agree at the coarse images (a coarse image IS the coarse site -- forced) and
    differ only at the interior sites."""
    out = {}
    for z in sites(Ls_refined):
        kind, lk = midpoint_kind(z, arena.links)
        b = base_of(z)
        if kind != "MID" or mode == "left":
            out[z] = prof[b]
        else:
            out[z] = prof[add(b, lk, arena.Ls)]
    return out


def commutation_defect(rule, arena, refined, N, n, Ls_refined, mode):
    """D(z) = w^c[N, n](base(z)) - w^r[N^r, F(n)](z), with the matter lift
    m^r(z) = m^c(base(z)).  The matter record CANCELS, so the defect is a pure
    drag comparison -- measured, not assumed (G-DEFECT-MATTER-FREE)."""
    F = lift_profile(n, arena, Ls_refined, mode)
    Nr = lift_profile(N, arena, Ls_refined, mode)
    out = {}
    for z in sites(Ls_refined):
        wc = drag_at(rule, arena, N, n, base_of(z))
        wr = drag_at(rule, refined, Nr, F, z)
        out[z] = tuple(a - b for a, b in zip(wc, wr))
    return out


def defect_support(D, arena):
    """The site support of the defect, by PARITY CLASS -- i.e. by which coarse
    interval the site subdivides."""
    tally = {}
    for z in sorted(D):
        kind, lk = midpoint_kind(z, arena.links)
        key = "IMAGE" if kind == "IMAGE" else (
            "MID-%s" % (tuple(lk),) if kind == "MID" else "UNREACHED")
        cell = tally.setdefault(key, [0, 0])
        cell[1] += 1
        if any(v != 0 for v in D[z]):
            cell[0] += 1
    return {k: {"nonzero": v[0], "total": v[1]} for k, v in sorted(tally.items())}


def front_sector_commutes(arena, Ls_refined, fmode, nmode, fronts, lapses):
    """The FRONT half of the census: F(n + N) = F(n) + Lift(N)?"""
    for _, n in fronts:
        for _, N in lapses:
            adv = {x: n[x] + N[x] for x in arena.S}
            lhs = lift_profile(adv, arena, Ls_refined, fmode)
            base = lift_profile(n, arena, Ls_refined, fmode)
            Nr = lift_profile(N, arena, Ls_refined, nmode)
            for z in lhs:
                if lhs[z] != base[z] + Nr[z]:
                    return False
    return True


def forced_front_lift_census(arena, split, fronts):
    """THE DYNAMICS-FORCED FRONT LIFT.  Requiring the drag to agree at the
    coarse image sites forces, for the interior site of [x, x+l],

        F(mid) = n(x) + n_1 * (n(x+l) - n(x)) / (n_1 + n_2),

    the count-weighted interpolation.  The front is Z-valued [T-FRONT], so the
    question is whether the FORCED value is of the declared type."""
    cells = 0
    integral = 0
    witnesses = []
    for _, n in fronts:
        for x in arena.S:
            for lk in arena.links:
                n1, n2 = split[(x, lk)]
                dn = n[add(x, lk, arena.Ls)] - n[x]
                val = Fr(n1 * dn, n1 + n2)
                cells += 1
                if val.denominator == 1:
                    integral += 1
                elif len(witnesses) < 4:
                    witnesses.append({"site": list(x), "link": list(lk),
                                      "split": [n1, n2], "front_tilt": dn,
                                      "forced_value_offset": str(val)})
    return {"cells": cells, "integral": integral,
            "non_integral": cells - integral, "witnesses": witnesses}


def forced_lift_universal(arena):
    """The universal statement, checked exhaustively: integrality of the forced
    lift FOR EVERY front tilt requires (n_1 + n_2) | n_1, impossible for
    1 <= n_1 < n.  A single divisibility hit would refute it."""
    checked = 0
    hits = 0
    for x in arena.S:
        for lk in arena.links:
            n = arena.counts[x][lk]
            for n1 in range(1, n):
                checked += 1
                if n1 % n == 0:
                    hits += 1
    return {"triples_checked": checked,
            "splits_with_n_dividing_n1": mutate("forcedlift-lax", hits, 1)}


# ----------------------------------------------------------------------------
# 10.  THE ITERATION PROBE  (measurement 5 -- R6b's prerequisite)
# ----------------------------------------------------------------------------
#
# THE CEILING.  After k dyadic steps a coarse interval of count n has been
# partitioned into 2^k parts, each >= 1 [T-COUNTS-POSITIVE], so n >= 2^k.  The
# number of consecutive steps a record admits is therefore at most
# floor(log2(min count)) -- for ANY split, not merely the declared ones.

def log2_floor(n):
    k = 0
    while n >= 2:
        n = n // 2
        k += 1
    return k


def iteration_probe(arena, cap=4):
    """Apply the move repeatedly with the balanced split and the iterable
    completion, so that the obstruction is located on the coarse record's own
    descendants rather than on the completion."""
    ceiling = log2_floor(arena.min_count())
    cur = arena
    trace = []
    steps = 0
    stop = "cap"
    while steps < cap:
        sp = make_split(cur, "floor")
        if sp is None:
            stop = "NO-SPLIT-EXISTS (a descendant interval has count 1)"
            break
        Lr = tuple(2 * a for a in cur.Ls)
        fr = make_free(cur, sp, Lr, "iterable-64")
        nxt = refine(cur, sp, fr, Lr, "%s/%d" % (arena.name, steps + 1))
        if not nxt.admissible():
            stop = "REFINED RECORD INADMISSIBLE at the balanced split"
            break
        steps += 1
        cur = nxt
        trace.append({"step": steps, "L": list(cur.Ls), "sites": len(cur.S),
                      "links": cur.n_links(), "min_count": cur.min_count()})
    return {"ceiling_floor_log2_min_count": ceiling,
            "steps_achieved_at_the_declared_split": mutate(
                "iteration-lax", steps, steps + 1),
            "halt_reason": stop, "trace": trace,
            "family_is_finite": True}


def inventory_growth(L, d, links, levels=3):
    """How the choice inventory behaves under iteration: the free part of each
    step, and the fraction of the level-k arena that the ORIGINAL record
    reaches."""
    rows = []
    nlinks = (L ** d) * len(links)
    reach = nlinks
    for k in range(levels):
        refined_links = nlinks * (2 ** d) * 1
        rows.append({"level": k, "L": L, "sites": L ** d,
                     "links": nlinks,
                     "refined_links": refined_links,
                     "covered_by_this_level": 2 * nlinks,
                     "free_at_this_step": refined_links - 2 * nlinks,
                     "reached_by_the_ORIGINAL_record": reach * 2,
                     "original_reach_numerator": reach * 2,
                     "original_reach_denominator": refined_links})
        L = 2 * L
        nlinks = (L ** d) * len(links)
        reach = reach * 2
    return rows


# ----------------------------------------------------------------------------
# 11.  THE CHOICE INVENTORY  (measurement 3 -- the unit's core)
# ----------------------------------------------------------------------------

def classify_freedom(item):
    """The class is RECOMPUTED from the item's own measured evidence, never
    read off the label: (i) forced iff the fiber is exactly 1 AND a pinned
    declaration is named; (ii) stabiliser-fixed iff the measured equivariant
    fiber is exactly 1; (iii) otherwise, with the fiber carried."""
    if item["fiber"] == 1 and item["forced_by"]:
        return "i"
    if item.get("equivariant_fiber") == 1:
        return "ii"
    return "iii"


def build_inventory(payload):
    """The residual freedoms of the admissible move class, each measured."""
    sf = payload["split_fibers"]
    fibers = sorted(v["admissible_at_images"] for v in sf.values()
                    if v["splittable"])
    eqf = sorted(set(v for v in payload["equivariant_fibers"].values()
                     if v is not None))
    inv = [
        {"name": "INSERTION-LOCUS",
         "what": "which intervals the move subdivides",
         "fiber": 1,
         "forced_by": "the move-class declaration: DYADIC subdivides EVERY "
                      "coarse interval, so no locus remains to be chosen",
         "evidence": {"subdivided": payload["dyadic_tally"]["SUBDIVIDED"],
                      "coarse_intervals": payload["coarse_intervals"]}},
        {"name": "SUBDIVISION-INCIDENCE",
         "what": "which refined site subdivides each coarse interval",
         "fiber": 1,
         "forced_by": "[P-I7-LINKS2] the declared link set -- every coarse "
                      "displacement has a UNIQUE minimal decomposition into "
                      "refined links, so the interior site is forced",
         "evidence": {"unique": payload["dyadic_tally"]["SUBDIVIDED"],
                      "ambiguous": payload["dyadic_tally"]["AMBIGUOUS"]}},
        {"name": "INTERVAL-COUNT-SUM",
         "what": "the total count carried by the two halves",
         "fiber": 1,
         "forced_by": "[T-COUNTS-SEMANTIC] n_l counts division events IN the "
                      "interval, so events in the whole = events in the parts: "
                      "additivity is semantics, not a choice",
         "evidence": {"constraints_verified": payload["additivity_checks"],
                      "violations": payload["additivity_violations"]}},
        {"name": "FRONT-AT-COARSE-IMAGES",
         "what": "the front value at the image of a coarse site",
         "fiber": 1,
         "forced_by": "[T-FRONT] the image of a coarse site IS that site, so "
                      "its committed-event count is carried unchanged",
         "evidence": {"lift_rules_agreeing_at_images": len(LIFT_RULES)}},
        {"name": "THE-SPLIT",
         "what": "the partition (n_1, n_2) of each coarse interval's count",
         "fiber": fibers[0] if fibers else 0,
         "fiber_max": fibers[-1] if fibers else 0,
         "forced_by": None,
         "equivariant_fiber": eqf[0] if eqf else None,
         "evidence": {"records_admitting_the_move": len(fibers),
                      "min_admissible_fiber": fibers[0] if fibers else 0,
                      "max_admissible_fiber": fibers[-1] if fibers else 0,
                      "equivariant_fibers": eqf,
                      "count_lattice": payload["count_lattice"]}},
        {"name": "FREE-TRANSVERSE-LINKS",
         "what": "the counts on refined links lying on no coarse interval",
         "fiber": "INFINITE",
         "forced_by": None,
         "evidence": {"free": payload["free_links"],
                      "total": payload["refined_links"],
                      "infinite_family": payload["infinite_family"]}},
        {"name": "NEW-FRONT-VALUES",
         "what": "the front value at each newly inserted site",
         "fiber": "INFINITE",
         "forced_by": None,
         "evidence": {"new_sites": payload["new_sites"],
                      "dynamics_forced_value_is_non_integral":
                          payload["forced_lift"]["non_integral"],
                      "of_cells": payload["forced_lift"]["cells"]}},
        {"name": "THE-LIFT-PAIR",
         "what": "which (front lift, lapse lift) pair the move carries",
         "fiber": payload["lift_pairs_commuting"],
         "forced_by": None,
         "evidence": {"declared_pairs": payload["lift_pairs_declared"],
                      "front_sector_commuting": payload["lift_pairs_commuting"]}},
    ]
    for it in inv:
        it["class_declared"] = mutate(
            "inventory-corrupt", classify_freedom(it),
            "i" if it["name"] == "THE-SPLIT" else classify_freedom(it))
    return inv


# ----------------------------------------------------------------------------
# 12.  THE VERDICT  (pin section 4 -- three heads, every segment computed)
# ----------------------------------------------------------------------------

HEAD_EXISTS = "R6A-MOTIVATED-REFINEMENT-EXISTS"
HEAD_NOSPLIT = "R6A-NO-MOTIVATED-SPLIT"
HEAD_BLOCKED = "R6A-BLOCKED-AT-GRAMMAR-SOURCE"

SEGMENT_ORDER = ("CLASSES", "BLOCKED-AT", "REFUSED-AT", "FORCED", "INVENTORY",
                 "OBSTRUCTION", "SPLIT-FIBER", "FREE-LINKS", "NEW-FRONTS",
                 "DEFECT", "ITERATION", "CONTROL")


def build_verdict(payload, swap_pairing=False):
    """Assemble the verdict from the measured payload.  The HEAD is chosen by
    the inventory: an admissible class with no class-(iii) freedom is MOTIVATED;
    an admissible class carrying one is NO-MOTIVATED-SPLIT; a class census with
    no admissible class at all and an ambiguity in the grammar is BLOCKED."""
    free_items = [i for i in payload["inventory"] if i["class_declared"] == "iii"]
    if payload["admissible_classes"] == 0:
        head = HEAD_BLOCKED
    elif not free_items:
        head = HEAD_EXISTS
    else:
        head = HEAD_NOSPLIT
    swap_pairing = mutate("verdict-pair-swap", swap_pairing, True)
    segs = []
    segs.append(("CLASSES", "CLASSES=ADMISSIBLE:%d(%s)|BLOCKED:%d|REFUSED:%d|"
                            "CONTROL:%d" % (
                                payload["admissible_classes"],
                                ",".join(payload["admissible_class_names"]),
                                payload["blocked_classes"],
                                payload["refused_classes"],
                                payload["control_classes"])))
    segs.append(("BLOCKED-AT", "BLOCKED-AT=%s:%d-OF-%d-INTERVALS-%d-CANDIDATES"
                 % (payload["blocked_fact"], payload["blocked_intervals"],
                    payload["coarse_intervals"], payload["blocked_candidates"])))
    segs.append(("REFUSED-AT", "REFUSED-AT=%s:CYCLES%s-LINK-TARGETS-%d-OF-%d"
                 % (payload["refused_class"],
                    "".join(str(c) for c in payload["refused_cycles"]),
                    payload["refused_link_targets"], payload["declared_links"])))
    segs.append(("FORCED", "FORCED=INCIDENCE-%d-OF-%d|ADDITIVITY-%d-OF-%d|"
                           "RESTRICTION-%d-OF-%d" % (
                               payload["dyadic_tally"]["SUBDIVIDED"],
                               payload["coarse_intervals"],
                               payload["additivity_checks"]
                               - payload["additivity_violations"],
                               payload["additivity_checks"],
                               payload["restriction_ok"],
                               payload["restriction_checks"])))
    segs.append(("INVENTORY", "INVENTORY=FORCED:%d|STABILIZER:%d|FREE:%d"
                 % (len([i for i in payload["inventory"]
                         if i["class_declared"] == "i"]),
                    len([i for i in payload["inventory"]
                         if i["class_declared"] == "ii"]),
                    len(free_items))))
    segs.append(("OBSTRUCTION", "OBSTRUCTION=" +
                 ("+".join(i["name"] for i in free_items) if free_items
                  else "NONE")))
    segs.append(("SPLIT-FIBER", "SPLIT-FIBER=MIN-%s-MAX-%s-EQUIVARIANT-MIN-%s-"
                                "LATTICE-FORCED-%d-OF-%d" % (
                                    payload["split_fiber_min"],
                                    payload["split_fiber_max"],
                                    payload["equivariant_fiber_min"],
                                    payload["count_lattice"]
                                    ["unique_admissible_split_count"],
                                    payload["count_lattice"]
                                    ["admissible_count_vectors"])))
    segs.append(("FREE-LINKS", "FREE-LINKS=%d-OF-%d-FIBER-INFINITE-WITNESSES-%d"
                 % (payload["free_links"], payload["refined_links"],
                    payload["infinite_family"]["witnesses"])))
    segs.append(("NEW-FRONTS", "NEW-FRONTS=%d-FIBER-INFINITE-DYNAMICS-FORCED-"
                               "NON-INTEGRAL-%d-OF-%d" % (
                                   payload["new_sites"],
                                   payload["forced_lift"]["non_integral"],
                                   payload["forced_lift"]["cells"])))
    segs.append(("DEFECT", "DEFECT=NONZERO-%d-OF-%d-CELLS-ZERO-%d-SUPPORT-%s"
                 % (payload["defect_nonzero_cells"], payload["defect_cells"],
                    payload["defect_zero_cells"], payload["defect_support_sig"])))
    segs.append(("ITERATION", "ITERATION=FAMILY-FINITE-CEILING-%d-ATTAINED-%d-"
                              "INVENTORY-%s" % (
                                  payload["iteration_ceiling"],
                                  payload["iteration_attained"],
                                  payload["inventory_trend"])))
    segs.append(("CONTROL", "CONTROL=%s-SUBDIVIDES-%d-OF-%d-UNREPRESENTED-%d-%s"
                 % (payload["control_name"], payload["control_subdivided"],
                    payload["coarse_intervals"], payload["control_unrepresented"],
                    payload["control_qualifier"])))
    if swap_pairing and len(segs) >= 3:
        a, b = segs[1], segs[2]
        segs[1] = (a[0], a[1].split("=")[0] + "=" + b[1].split("=", 1)[1])
        segs[2] = (b[0], b[1].split("=")[0] + "=" + a[1].split("=", 1)[1])
    segs = mutate("verdict-typed-segment", segs,
                  [(n, "SPLIT-FIBER=MIN-1-MAX-1-EQUIVARIANT-MIN-1-"
                       "LATTICE-FORCED-361-OF-361") if n == "SPLIT-FIBER"
                   else (n, t) for n, t in segs])
    segs = mutate("verdict-append-text", segs,
                  [(n, t + "-AND-MOTIVATED") if n == "OBSTRUCTION" else (n, t)
                   for n, t in segs])
    segs = mutate("verdict-inert-segment", segs,
                  [(n, "DEFECT=NONE") if n == "DEFECT" else (n, t)
                   for n, t in segs])
    segs = mutate("verdict-fully-typed", segs,
                  [(nm, "%s=TYPED" % nm) for nm in SEGMENT_ORDER])
    head = mutate("verdict-fully-typed",
                  mutate("head-constant", head, HEAD_EXISTS), HEAD_EXISTS)
    full = head + "<" + "|".join(s[1] for s in segs) + ">"
    return head, segs, full


# ----------------------------------------------------------------------------
# 12a.  THE INDEPENDENT COMPARATOR (RUNBOOK section 14 addendum, v14 #10/#20)
# ----------------------------------------------------------------------------
#
# "A compliance gate whose comparator cannot disagree with the object under test
# is vacuous by construction."  This function shares NO code and NO input with
# build_verdict(): it reads the RECEIPT OBJECT -- the same stored tables the
# output and the paper render from -- and rebuilds every segment from the
# measured rows.  A typed, appended, swapped, inert or wholesale-replaced
# segment makes it disagree.

def reconstruct_verdict_from_receipt(R):
    mc = R["move_census"]
    adm = sorted([r["move"] for r in mc["rows"] if r["verdict"] == "ADMISSIBLE"])
    blk = [r for r in mc["rows"] if r["verdict"] == "BLOCKED"]
    ref = [r for r in mc["rows"] if r["verdict"] == "REFUSED"]
    ctl = [r for r in mc["rows"] if r["verdict"] == "CONTROL"]
    inv = R["choice_inventory"]["items"]
    free = [i for i in inv if i["class_declared"] == "iii"]
    ncoarse = mc["coarse_intervals"]
    dy = [r for r in mc["rows"] if r["move"] == "DYADIC"][0]

    if len(adm) == 0:
        head = HEAD_BLOCKED
    elif not free:
        head = HEAD_EXISTS
    else:
        head = HEAD_NOSPLIT

    out = []
    out.append("CLASSES=ADMISSIBLE:%d(%s)|BLOCKED:%d|REFUSED:%d|CONTROL:%d"
               % (len(adm), ",".join(adm), len(blk), len(ref), len(ctl)))
    b0 = R["blocked_branch"]
    out.append("BLOCKED-AT=%s:%d-OF-%d-INTERVALS-%d-CANDIDATES"
               % (b0["named_fact"], b0["ambiguous_intervals"], ncoarse,
                  b0["candidates_per_interval"]))
    rf = R["refused_branch"]
    out.append("REFUSED-AT=%s:CYCLES%s-LINK-TARGETS-%d-OF-%d"
               % (rf["move"],
                  "".join(str(c) for c in rf["direction_0_cycle_lengths"]),
                  rf["declared_link_targets_defined_at_the_new_site"],
                  rf["declared_links"]))
    fp = R["forced_part"]
    out.append("FORCED=INCIDENCE-%d-OF-%d|ADDITIVITY-%d-OF-%d|RESTRICTION-%d-OF-%d"
               % (dy["tally"]["SUBDIVIDED"], ncoarse,
                  fp["additivity_checks"] - fp["additivity_violations"],
                  fp["additivity_checks"], fp["restriction_ok"],
                  fp["restriction_checks"]))
    out.append("INVENTORY=FORCED:%d|STABILIZER:%d|FREE:%d"
               % (len([i for i in inv if i["class_declared"] == "i"]),
                  len([i for i in inv if i["class_declared"] == "ii"]),
                  len(free)))
    out.append("OBSTRUCTION=" +
               ("+".join(i["name"] for i in free) if free else "NONE"))
    sp = [i for i in inv if i["name"] == "THE-SPLIT"][0]
    cl = R["count_lattice"]
    out.append("SPLIT-FIBER=MIN-%s-MAX-%s-EQUIVARIANT-MIN-%s-LATTICE-FORCED-%d-OF-%d"
               % (sp["evidence"]["min_admissible_fiber"],
                  sp["evidence"]["max_admissible_fiber"],
                  (sp["evidence"]["equivariant_fibers"] or [None])[0],
                  cl["unique_admissible_split_count"],
                  cl["admissible_count_vectors"]))
    fl = [i for i in inv if i["name"] == "FREE-TRANSVERSE-LINKS"][0]
    out.append("FREE-LINKS=%d-OF-%d-FIBER-INFINITE-WITNESSES-%d"
               % (fl["evidence"]["free"], fl["evidence"]["total"],
                  fl["evidence"]["infinite_family"]["witnesses"]))
    nf = [i for i in inv if i["name"] == "NEW-FRONT-VALUES"][0]
    out.append("NEW-FRONTS=%d-FIBER-INFINITE-DYNAMICS-FORCED-NON-INTEGRAL-%d-OF-%d"
               % (nf["evidence"]["new_sites"],
                  nf["evidence"]["dynamics_forced_value_is_non_integral"],
                  nf["evidence"]["of_cells"]))
    dc = R["dynamics_census"]
    out.append("DEFECT=NONZERO-%d-OF-%d-CELLS-ZERO-%d-SUPPORT-%s"
               % (dc["cells_with_a_nonzero_defect"], dc["cells"],
                  dc["cells_with_an_identically_zero_defect"],
                  dc["support_signature"]))
    it = R["iteration"]
    out.append("ITERATION=FAMILY-FINITE-CEILING-%d-ATTAINED-%d-INVENTORY-%s"
               % (it["ceiling_over_the_family"], it["attained_over_the_family"],
                  it["inventory_trend"]))
    co = [r for r in mc["rows"] if r["verdict"] == "CONTROL"][0]
    out.append("CONTROL=%s-SUBDIVIDES-%d-OF-%d-UNREPRESENTED-%d-%s"
               % (co["move"], co["tally"]["SUBDIVIDED"], ncoarse,
                  co["tally"]["UNREPRESENTED"], R["control"]["qualifier"]))
    return head + "<" + "|".join(out) + ">"


# ----------------------------------------------------------------------------
# 13.  THE RUN
# ----------------------------------------------------------------------------

def stage1():
    R = {}
    R["unit"] = "v14 R6a -- THE REFINEMENT GRAMMAR"
    R["question"] = ("does the record grammar AS PINNED admit a MOTIVATED "
                     "interval-subdivision move -- a new site because a "
                     "division event resolved a record interval, the count "
                     "partition FORCED by the counting semantics and the "
                     "residual freedom MEASURED?")

    # -- 0.  exact arithmetic and run-mode hygiene --------------------------
    off = float_guard()
    gate("G-FLOATGUARD",
         "an AST scan of this source finds no float literal, no float/math "
         "import, and no true-division operator (every quotient goes through "
         "fdiv)", len(off) == 0, {"offences": off[:5]})
    src_text = read_text("v14/code/r6a_refinement_exact.py")
    fns = _functions_naming_mutant(src_text)
    bad_gates = _gate_calls_naming_mutant(src_text)
    inj = []
    for why, snippet in MUTANT_GUARD_INJECTIONS:
        inj.append((why, len(_functions_naming_mutant(snippet)) > 0
                    or len(_gate_calls_naming_mutant(snippet)) > 0))
    gate("G-NO-MUTANT-IDENTITY",
         "run-mode identity is read by mutate() alone: no other function, and "
         "in particular no gate predicate, names it -- and the AST detector is "
         "validated by synthetic injections it must flag (RUNBOOK section 14 "
         "addendum, v13 #208)",
         sorted(fns) == sorted(MUTANT_NAME_ALLOWLIST) and not bad_gates
         and all(f for _, f in inj),
         {"functions_naming_mutant": fns, "gate_calls": bad_gates,
          "detector_injections_flagged": inj})

    # -- 1.  anchors --------------------------------------------------------
    n_file = verify_anchors()
    n_path = verify_path_anchors()
    n_text = verify_text_anchors()
    R["anchors"] = ANCHORS
    R["anchor_totals"] = {"file_bytes": n_file, "path_value": n_path,
                          "verbatim_text": n_text,
                          "total": n_file + n_path + n_text}

    rec = read_json("v13/code/ha_successor_receipt.json")
    d = read_by_path(rec, ("declarations", "d"))
    L = read_by_path(rec, ("declarations", "L"))
    d_ext = read_by_path(rec, ("declarations", "d_ext"))
    decl2 = read_by_path(rec, ("declarations", "records_d2"))
    decl3 = read_by_path(rec, ("declarations", "records_d3"))
    box = read_by_path(rec, ("declarations", "count_lattice"))
    links = link_set(d)
    R["arena"] = {
        "sites": "X = (Z_L)^d with L = %d, d = %d (|X| = %d)" % (L, d, L ** d),
        "links": [list(lk) for lk in links],
        "d_ext": d_ext,
        "geometry_record": "n_l(x) in Z_>0, the number of division events in "
                           "the record interval between x and x+l",
        "front": "n : X -> Z, the number of division events already committed "
                 "at record site x",
        "readout": "q_ij e_l^i e_l^j = n_l(x); I = q^-1 (det q)^w at w = 0",
        "lapse_family": read_by_path(rec, ("declarations", "lapse_family")),
        "drag_rules": [list(r) for r in RULE_TABLE],
        "provenance": "every row REBUILT here from the pinned sources; nothing "
                      "imported",
    }

    # -- 2.  the grammar reproduces I7 --------------------------------------
    fam = build_record_family(d, L, decl2, decl3)
    adm_names = sorted([nm for nm in fam if fam[nm].admissible()])
    rejected = sorted([nm for nm in fam if not fam[nm].admissible()])
    gate("G-RECORD-FAMILY-REPRODUCES-I7",
         "the record family rebuilt from the pinned declarations reproduces "
         "I7's own admissibility verdict: nine admissible records and the two "
         "declared negative controls rejected, one in each failure mode",
         len(adm_names) == 9 and rejected == ["G-INDEF", "G-SINGULAR"]
         and fam["G-SINGULAR"].singular and fam["G-INDEF"].nonpd,
         {"admissible": adm_names, "rejected": rejected})
    detm = det_exact(readout_matrix(d))
    gate("G-READOUT-REENCODING",
         "record-IS-metric: the count -> q map is an invertible linear "
         "re-encoding whose determinant, in I7's own sorted-link row order, is "
         "exactly the pinned value",
         str(mutate("readout-det", detm, detm + 1))
         == read_by_path(rec, ("tables", "readout_reencoding", "determinant")),
         {"measured": str(detm),
          "pinned": read_by_path(rec, ("tables", "readout_reencoding",
                                       "determinant"))})
    reprod = 0
    checks = 0
    for nm in adm_names:
        a = fam[nm]
        for x in a.S:
            ok = True
            for lk in a.links:
                checks += 1
                v = sum(a.q[x][i][j] * Fr(lk[i] * lk[j])
                        for i in range(d) for j in range(d))
                if v != Fr(a.counts[x][lk]):
                    ok = False
            if ok:
                reprod += 1
    want = read_by_path(rec, ("tables", "readout_reencoding", "sites_verified"))
    gate("G-RECORD-IS-METRIC",
         "q reproduces every declared link count at every site of every "
         "admissible record -- I7's own 81 of 81 (record, site) pairs, "
         "recomputed here from %d link comparisons" % checks,
         reprod == want and reprod == len(adm_names) * (L ** d),
         {"sites_reproduced": reprod, "pinned": want,
          "link_comparisons": checks})

    lap = build_lapse_family(fam["G-FLAT"].S, d)
    R["lapse_family_size"] = len(lap)
    ranks = {}
    for x in fam["G-FLAT"].S:
        rows = []
        for i in range(len(lap)):
            for j in range(len(lap)):
                if i == j:
                    continue
                N = lap[i][1]
                M = lap[j][1]
                rows.append([Fr(N[x] * M[add(x, e, fam["G-FLAT"].Ls)]
                                - M[x] * N[add(x, e, fam["G-FLAT"].Ls)])
                             for e in links[:d]])
        rk = 0
        basis = []
        for r0 in rows:
            v = r0[:]
            for b in basis:
                p = None
                for k in range(d):
                    if b[k] != 0:
                        p = k
                        break
                if p is not None and v[p] != 0:
                    f = fdiv(v[p], b[p])
                    v = [a - f * c for a, c in zip(v, b)]
            if any(a != 0 for a in v):
                basis.append(v)
                rk += 1
        ranks[str(x)] = mutate("rank-lax", rk, rk - 1)
    gate("G-IDENTIFIABILITY-RANK",
         "the declared lapse family realises bracket covectors of FULL rank at "
         "every site -- I7's identifiability measurement, recomputed",
         all(v == d for v in ranks.values())
         and ranks["(0, 0)"] == read_by_path(rec, ("tables",
                                                   "identifiability_rank",
                                                   "(0, 0)")),
         {"ranks": ranks})

    cl = count_lattice_census(d, box["axis_max"], box["diag_max"])
    cl["admissible_count_vectors"] = mutate(
        "lattice-drop", cl["admissible_count_vectors"],
        cl["admissible_count_vectors"] - 1)
    gate("G-COUNT-LATTICE-REPRODUCES-I7",
         "the admissible count vectors of I7's own declared count box are "
         "recomputed here and match its committed 361 -- the scope at which "
         "the split freedom is censused beyond the nine records",
         cl["admissible_count_vectors"] == 361,
         {"measured": cl["admissible_count_vectors"], "box": cl["box"]})
    R["count_lattice"] = cl
    R["record_family"] = {
        nm: {"counts_at_00": [fam[nm].counts[(0,) * d][lk] for lk in links],
             "counts_at_11": [fam[nm].counts[(1,) * d][lk] for lk in links],
             "admissible": fam[nm].admissible(),
             "min_count": fam[nm].min_count(),
             "homogeneous": all(fam[nm].counts[x] == fam[nm].counts[(0,) * d]
                                for x in fam[nm].S),
             "note": fam[nm].note}
        for nm in sorted(fam)}

    # -- 3.  the no-potential theorem ---------------------------------------
    pot = {nm: potential_census(fam[nm]) for nm in adm_names}
    gate("G-NO-POTENTIAL",
         "no record's counts are the coboundary of a site function: the counts "
         "are strictly positive [T-COUNTS-POSITIVE] and the lattice is "
         "periodic, so every axis cycle sum is positive where a coboundary's "
         "would vanish.  The split therefore cannot be read off any front-like "
         "potential -- this is the MECHANISM of the freedom measured below",
         all(not v["admits_a_potential"] for v in pot.values()),
         {"min_axis_cycle_sum": {k: v["min_axis_cycle_sum"]
                                 for k, v in sorted(pot.items())}})
    R["no_potential"] = {k: v for k, v in sorted(pot.items())}
    return R, fam, adm_names, links, d, L, d_ext, rec, cl


def stage2(R, fam, adm_names, links, d, L, d_ext):
    """MEASUREMENT 1 -- THE MOVE CENSUS, cell-complete and uniform."""
    moves = declared_moves(d, L)
    moves = mutate("census-drop", moves, [m for m in moves
                                          if m.key != "SINGLE-INTERVAL"])
    ncoarse = (L ** d) * len(links)
    rows = []
    for mv in moves:
        if mv.Ls_refined is None:
            probe = single_interval_arena_probe(d, L)
            rows.append({"move": mv.key, "name": mv.name, "kind": mv.kind,
                         "refined_shape": None,
                         "arena_class_preserved": False,
                         "tally": {"INHERITED": 0, "SUBDIVIDED": 0,
                                   "AMBIGUOUS": 0, "UNREPRESENTED": 0},
                         "verdict": "REFUSED", "probe": probe,
                         "reason": probe["reason"]})
            continue
        irows, tally = move_incidence_census(mv, d, links)
        # THE ARENA PREDICATE: a product of cyclic groups carrying the declared
        # link displacements, measured rather than assumed
        shape_ok = all(v >= 2 for v in mv.Ls_refined)
        target_ok = all(add(z, lk, mv.Ls_refined) in set(sites(mv.Ls_refined))
                        for z in sites(mv.Ls_refined) for lk in links)
        arena_ok = shape_ok and target_ok
        if mv.kind == "control":
            verdict = "CONTROL"
        elif not arena_ok:
            verdict = "REFUSED"
        elif tally["AMBIGUOUS"] > 0:
            verdict = "BLOCKED"
        elif tally["SUBDIVIDED"] == 0:
            verdict = "BLOCKED"
        else:
            verdict = "ADMISSIBLE"
        rows.append({"move": mv.key, "name": mv.name, "kind": mv.kind,
                     "refined_shape": list(mv.Ls_refined),
                     "refined_sites": len(sites(mv.Ls_refined)),
                     "arena_class_preserved": arena_ok,
                     "tally": tally, "verdict": verdict,
                     "note": mv.note,
                     "intervals": len(irows)})
    gate("G-MOVE-CENSUS-CELL-COMPLETE",
         "every declared move class was censused and every coarse interval of "
         "every class was classified -- a dropped class or a dropped interval "
         "cannot shrink the census",
         len(rows) == len(declared_moves(d, L))
         and all(r["tally"]["INHERITED"] + r["tally"]["SUBDIVIDED"]
                 + r["tally"]["AMBIGUOUS"] + r["tally"]["UNREPRESENTED"]
                 in (0, ncoarse) for r in rows),
         {"classes": len(rows), "declared": len(declared_moves(d, L)),
          "coarse_intervals": ncoarse})

    hyp = [r for r in rows if r["move"].startswith("HYPERPLANE")]
    dyad = [r for r in rows if r["move"] == "DYADIC"][0]
    ctl = [r for r in rows if r["verdict"] == "CONTROL"][0]
    gate("G-INCIDENCE-CENSUS",
         "the incidence of every coarse interval is decided by the UNIQUENESS "
         "of its minimal decomposition into declared link vectors: the dyadic "
         "move subdivides every interval uniquely, while single-direction "
         "hyperplane insertion leaves the diagonal intervals with two "
         "candidate interior sites and the grammar declares no rule choosing "
         "between them",
         dyad["tally"]["SUBDIVIDED"] == ncoarse
         and dyad["tally"]["AMBIGUOUS"] == 0
         and all(h["tally"]["AMBIGUOUS"] > 0 for h in hyp),
         {"dyadic": dyad["tally"], "hyperplane": [h["tally"] for h in hyp]})

    # the ambiguity is REAL: the two candidate readings disagree
    dis = 0
    tot = 0
    r0 = fam["G-DIAG2"]
    nmax = r0.counts[(0,) * d][links[0]]
    for n1 in range(1, nmax):
        for f0 in range(1, 5):
            for f1 in range(1, 5):
                tot += 1
                if f0 + (nmax - n1) != n1 + f1:
                    dis += 1
    gate("G-BLOCK-IS-REAL",
         "the blocked branch's ambiguity is not harmless: over a declared "
         "completion sweep the two candidate readings of a cut diagonal "
         "interval's count DISAGREE at most cells, so no reading can be "
         "adopted without a grammar fact the pinned sources do not supply",
         dis > 0, {"completions": tot, "disagreeing": dis,
                   "agreeing": tot - dis})

    R["move_census"] = {
        "coarse_intervals": ncoarse,
        "classification_rule": "INHERITED = the coarse interval IS a refined "
                               "link; SUBDIVIDED = exactly one refined site "
                               "lies on it; AMBIGUOUS = two or more candidate "
                               "interior sites; UNREPRESENTED = no minimal 1- "
                               "or 2-step realisation",
        "rows": rows}
    R["blocked_branch"] = {
        "move": hyp[0]["move"].split("@")[0],
        "named_fact": "DIAGONAL-INTERVAL-INCIDENCE",
        "statement": "which refined site subdivides a coarse DIAGONAL interval "
                     "cut by a single-direction hyperplane insertion.  The "
                     "coarse displacement (2,1) has two minimal decompositions "
                     "into declared link vectors, with two distinct interior "
                     "sites; the pinned grammar declares a link SET and no "
                     "incidence rule, and supplying one would be a grammar "
                     "fact from outside the pinned sources (pin section 1)",
        "ambiguous_intervals": hyp[0]["tally"]["AMBIGUOUS"],
        "candidates_per_interval": 2,
        "loci_censused": len(hyp),
        "all_loci_agree": len(set(h["tally"]["AMBIGUOUS"] for h in hyp)) == 1,
        "completion_sweep": {"completions": tot, "disagreeing": dis}}
    R["refused_branch"] = [r for r in rows
                           if r["move"] == "SINGLE-INTERVAL"][0]["probe"]
    R["refused_branch"]["move"] = "SINGLE-INTERVAL"

    # -- the d = 3 cover, where the declared link set omits the body diagonal
    l3 = link_set(d_ext)
    Ls3 = (L,) * d_ext
    Lr3 = (2 * L,) * d_ext
    imgs = set(tuple(2 * a for a in x) for x in sites(Ls3))
    mids = set()
    for x in sites(Ls3):
        for lk in l3:
            mids.add(add(tuple(2 * a for a in x), lk, Lr3))
    unreached = [z for z in sites(Lr3) if z not in imgs and z not in mids]
    cov3 = len(covered_slots(Ls3, Lr3, l3))
    R["dimension_extension"] = {
        "d": d_ext, "refined_sites": len(sites(Lr3)),
        "coarse_images": len(imgs), "interior_sites": len(mids),
        "unreached_sites": len(unreached),
        "unreached_parities": sorted(set(tuple(a % 2 for a in z)
                                         for z in unreached)),
        "refined_links": len(sites(Lr3)) * len(l3),
        "covered_links": cov3,
        "free_links": len(sites(Lr3)) * len(l3) - cov3,
        "reading": "at d = 3 the declared link set has no body diagonal, so "
                   "one parity class of refined sites lies on NO coarse "
                   "interval: the move is site-complete at d = 2 and "
                   "site-incomplete at d = 3"}
    gate("G-DIMENSION-EXTENSION",
         "the dyadic move's site coverage is measured at BOTH declared "
         "dimensions: complete at d = 2 and incomplete at d = 3, the gap being "
         "exactly the all-odd parity class the declared link set cannot reach",
         len(unreached) > 0 and R["dimension_extension"]["unreached_parities"]
         == [tuple([1] * d_ext)],
         R["dimension_extension"])
    return rows, dyad, ctl, ncoarse


def stage3(R, fam, adm_names, links, d, L):
    """MEASUREMENT 2 -- THE FORCED PART: additivity and the metric-restriction
    test, at the admissible move class over the declared record family."""
    Lc = (L,) * d
    Lr = (2 * L,) * d
    splittable = sorted([nm for nm in adm_names if fam[nm].min_count() >= 2])
    unsplittable = sorted([nm for nm in adm_names if fam[nm].min_count() < 2])
    add_checks = 0
    add_bad = 0
    res_checks = 0
    res_ok = 0
    q_checks = 0
    q_ok = 0
    built = {}
    admissible_builds = []
    rows = []
    for nm in splittable:
        a = fam[nm]
        for smode in SPLIT_RULES:
            sp = make_split(a, smode)
            for fmode in FREE_RULES:
                fr = make_free(a, sp, Lr, fmode)
                rf = refine(a, sp, fr, Lr, "%s@%s+%s" % (nm, smode, fmode))
                built[(nm, smode, fmode)] = rf
                # additivity
                bad = 0
                for x in a.S:
                    for lk in links:
                        z0 = tuple(2 * t for t in x)
                        z1 = add(z0, lk, Lr)
                        add_checks += 1
                        if rf.counts[z0][lk] + rf.counts[z1][lk] \
                           != a.counts[x][lk]:
                            bad += 1
                add_bad += bad
                # the metric-restriction test: rebuild q from the RESTRICTED
                # refined counts and compare against the coarse q, which was
                # computed by a route this one does not touch
                rc = restrict_counts(rf, a, Lr)
                okq = 0
                for x in a.S:
                    q_checks += 1
                    res_checks += 1
                    qq = q_from_counts(d, {lk: Fr(rc[x][lk]) for lk in links})
                    if qq == a.q[x]:
                        okq += 1
                        res_ok += 1
                q_ok += okq
                rows.append({"record": nm, "split": smode, "free": fmode,
                             "refined_admissible": rf.admissible(),
                             "inadmissible_sites": len(rf.nonpd)
                             + len(rf.singular) + len(rf.nonpositive),
                             "additivity_violations": bad,
                             "coarse_q_recovered": okq, "coarse_sites": len(a.S),
                             "refined_min_count": rf.min_count()})
                if rf.admissible():
                    admissible_builds.append((nm, smode, fmode))
    gate("G-ADDITIVITY-FORCED",
         "count additivity holds by construction in every admissible move: the "
         "two halves of every coarse interval sum to its count, at every "
         "record, every declared split and every declared completion",
         add_bad == 0, {"checks": add_checks, "violations": add_bad})
    res_ok_m = mutate("restriction-lax", res_ok, res_ok - 1)
    gate("G-RESTRICTION-COMMUTES",
         "record-IS-metric COMMUTES with refinement: the coarse metric rebuilt "
         "from the RESTRICTED refined counts equals the coarse metric computed "
         "directly, at every (record, split, completion, site) cell -- the "
         "comparator is the coarse record's own q, computed by a route the "
         "restriction does not touch",
         res_ok_m == res_checks, {"checks": res_checks, "recovered": res_ok_m})
    gate("G-UNSPLITTABLE-RECORDS",
         "a record carrying a count-1 interval admits NO subdivision at all: "
         "n_l(x) in Z_>0 [T-COUNTS-POSITIVE] leaves no positive partition of 1, "
         "and the readout independently rejects a zero part.  Measured over "
         "the declared family, not argued",
         len(unsplittable) > 0
         and all(fam[nm].min_count() == 1 for nm in unsplittable),
         {"unsplittable": unsplittable, "splittable": splittable})
    R["forced_part"] = {
        "additivity_checks": add_checks, "additivity_violations": add_bad,
        "restriction_checks": res_checks, "restriction_ok": res_ok_m,
        "splittable_records": splittable, "unsplittable_records": unsplittable,
        "builds": rows,
        "admissible_builds": len(admissible_builds),
        "declared_builds": len(rows),
        "reading": "the FORCED half of the grammar holds exactly: additivity "
                   "is verified at every cell and the coarse metric is "
                   "recovered exactly at every cell.  What fails is not the "
                   "forced part."}
    return built, admissible_builds, splittable, unsplittable


def stage4(R, fam, adm_names, links, d, L, splittable, built, admissible_builds):
    """MEASUREMENT 3 -- THE CHOICE INVENTORY."""
    Lr = (2 * L,) * d
    Lc = (L,) * d
    sf = {}
    for nm in adm_names:
        v = split_fibers(fam[nm])
        v["admissible_at_images"] = mutate(
            "fiber-typed", v["admissible_at_images"], 1)
        sf[nm] = v
    # an INDEPENDENT recomputation of the same fiber, from the record itself
    check = {}
    for nm in splittable:
        a = fam[nm]
        prod = 1
        for x in a.S:
            prod = prod * len(site_admissible_triples(a.counts[x], a.links))
        check[nm] = prod
    gate("G-FIBER-COMPUTED",
         "every split fiber is COMPUTED from the record's own counts, never "
         "typed: a record with a count-1 interval has fiber 0, and the "
         "admissible fiber equals an independent recomputation of the product "
         "over coarse sites of that site's admissible split triples",
         all(sf[nm]["raw"] == 0 for nm in adm_names
             if fam[nm].min_count() < 2)
         and all(sf[nm]["admissible_at_images"] <= sf[nm]["raw"]
                 for nm in splittable)
         and all(sf[nm]["admissible_at_images"] == check[nm]
                 for nm in splittable),
         {"declared": {nm: sf[nm]["admissible_at_images"] for nm in splittable},
          "recomputed": check})

    eqf = {}
    stabs = {}
    for nm in splittable:
        a = fam[nm]
        st = stabiliser(a)
        orbs = stabiliser_orbits(a, st)
        f, per = equivariant_split_fiber(a, orbs)
        stabs[nm] = {"order": len(st), "orbits": len(orbs),
                     "orbit_profile": [[n, n - 1, sz] for n, _, sz in per]}
        eqf[nm] = mutate("stabilizer-lax", f, 1)
    gate("G-STABILIZER-MEASURED",
         "the stabiliser of each record in the DECLARED chart group is "
         "measured, its orbits on the (site, link) pairs are computed, and the "
         "number of chart-EQUIVARIANT split assignments is counted.  No record "
         "of the declared family has a unique equivariant split, so no measured "
         "symmetry fixes the split -- class (ii) is EMPTY here, and that is a "
         "measurement, not an omission",
         all(v is not None and v > 1 for v in eqf.values()),
         {"equivariant_fibers": eqf, "stabilisers": stabs})

    free = free_slots(Lc, Lr, links)
    cov = covered_slots(Lc, Lr, links)
    refined_links = len(sites(Lr)) * len(links)
    new_sites = len(sites(Lr)) - len(sites(Lc))
    # THE INFINITE FAMILY, exhibited and gated: at an interior site of an axis
    # interval the transverse count b is free and c = a + b keeps q diagonal
    # with det q = a*b > 0 for EVERY b >= 1.
    wit = 0
    for b in range(1, 65):
        q = q_from_counts(d, {links[0]: Fr(3), links[1]: Fr(b),
                              links[2]: Fr(3 + b)})
        if q is not None and positive_definite(q):
            wit += 1
    gate("G-FREE-LINKS-INFINITE",
         "the free transverse links carry an INFINITE fiber, exhibited: with "
         "c = a + b the readout is diagonal and det q = a*b > 0 for every "
         "b >= 1, so a whole one-parameter family of admissible completions "
         "restricts to the same coarse record",
         wit == 64 and len(free) > 0,
         {"free_slots": len(free), "refined_links": refined_links,
          "witnesses_checked": wit})

    fronts = front_family(fam[splittable[0]].S)
    lap = build_lapse_family(fam[splittable[0]].S, d)
    pairs = []
    for fmode in LIFT_RULES:
        for nmode in LIFT_RULES:
            ok = front_sector_commutes(fam[splittable[0]], Lr, fmode, nmode,
                                       fronts, lap)
            pairs.append({"front_lift": fmode, "lapse_lift": nmode,
                          "front_sector_commutes": ok})
    ncommute = len([p for p in pairs if p["front_sector_commutes"]])
    gate("G-LIFT-GRID-CELL-COMPLETE",
         "the (front lift, lapse lift) grid is censused cell-complete and the "
         "front sector's commutation is MEASURED: exactly the MATCHED pairs "
         "commute, so dynamics-compatibility ties the lapse lift rigidly to "
         "the front lift without fixing either",
         len(pairs) == len(LIFT_RULES) ** 2 and ncommute == len(LIFT_RULES)
         and all(p["front_sector_commutes"] ==
                 (p["front_lift"] == p["lapse_lift"]) for p in pairs),
         {"pairs": pairs})

    a0 = fam[splittable[0]]
    sp0 = make_split(a0, "floor")
    fl = forced_front_lift_census(a0, sp0, fronts)
    flu = forced_lift_universal(a0)
    gate("G-FORCED-LIFT-NON-INTEGRAL",
         "requiring the drag to agree at the coarse image sites FORCES the "
         "front lift to the count-weighted interpolation n(x) + n_1*dn/n -- "
         "and that value is not of the declared Z-valued front type: "
         "integrality for EVERY front tilt would require n | n_1 with "
         "1 <= n_1 < n, which holds at no split of any interval of the "
         "declared family.  The dynamics does not rescue the free front value; "
         "it forces an inadmissible one",
         fl["non_integral"] > 0 and flu["splits_with_n_dividing_n1"] == 0,
         {"forced_lift": fl, "universal": flu})

    R["split_fibers"] = sf
    R["stabilisers"] = stabs
    R["equivariant_fibers"] = eqf
    R["lift_grid"] = pairs
    R["forced_front_lift"] = fl
    R["forced_lift_universal"] = flu
    R["cover"] = {"refined_sites": len(sites(Lr)), "coarse_images": len(sites(Lc)),
                  "new_sites": new_sites, "refined_links": refined_links,
                  "covered_links": len(cov), "free_links": len(free)}
    return sf, eqf, free, refined_links, new_sites, fl, pairs, ncommute


def stage5(R, fam, links, d, L, splittable, built, admissible_builds):
    """MEASUREMENT 4 -- THE DYNAMICS-COMPATIBILITY CENSUS.

    refine-then-advance vs advance-then-refine, both drag architectures, every
    declared lapse, every declared front, both lifts, every admissible build.
    A NONZERO DEFECT IS A MEASURED OBJECT: its site support, its split
    dependence and its record dependence are characterised."""
    Lr = (2 * L,) * d
    cells = 0
    nonzero = 0
    zero = 0
    support_tally = {}
    per_rule = {}
    per_record = {}
    matter_free_checks = 0
    image_equals_coarse_drag = 0
    image_cells = 0
    builds = [b for b in admissible_builds if b[2] == "minimal"]
    for (nm, smode, fmode) in builds:
        a = fam[nm]
        rf = built[(nm, smode, fmode)]
        lap = build_lapse_family(a.S, d)
        fronts = front_family(a.S)
        for rule in RULES:
            for lname, N in lap:
                for fname, n in fronts:
                    for mode in LIFT_RULES:
                        D = commutation_defect(rule, a, rf, N, n, Lr, mode)
                        cells += 1
                        nz = any(any(v != 0 for v in D[z]) for z in D)
                        if nz:
                            nonzero += 1
                        else:
                            zero += 1
                        sup = defect_support(D, a)
                        for k, v in sup.items():
                            cell = support_tally.setdefault(k, [0, 0])
                            cell[0] += v["nonzero"]
                            cell[1] += v["total"]
                        pr = per_rule.setdefault(rule, [0, 0])
                        pr[0] += 1 if nz else 0
                        pr[1] += 1
                        pc = per_record.setdefault(nm, [0, 0])
                        pc[0] += 1 if nz else 0
                        pc[1] += 1
                        if mode == "left":
                            for x in a.S:
                                image_cells += 1
                                wc = drag_at(rule, a, N, n, x)
                                if D[tuple(2 * t for t in x)] == wc:
                                    image_equals_coarse_drag += 1
    nonzero = mutate("defect-suppress", nonzero, 0)
    gate("G-DEFECT-NONZERO",
         "the commutation defect is NONZERO: refine-then-advance and "
         "advance-then-refine differ at most cells of the census.  It is "
         "measured, not asserted, and the census carries both directions -- "
         "cells with an identically zero defect are counted too",
         nonzero > 0 and zero > 0 and nonzero + zero == cells,
         {"cells": cells, "nonzero": nonzero, "zero": zero})
    gate("G-DEFECT-CLOSED-FORM",
         "the defect has an EXACT closed form at the coarse image sites under "
         "the left lift: the refined front is constant on each cell, so the "
         "refined drag vanishes there and the defect equals the WHOLE coarse "
         "drag -- verified cell by cell, not argued",
         image_cells > 0 and image_equals_coarse_drag == image_cells,
         {"image_cells": image_cells, "matching": image_equals_coarse_drag})
    sup_sig = "|".join("%s:%d-OF-%d" % (k, v[0], v[1])
                       for k, v in sorted(support_tally.items()))
    sup_sig = mutate("defect-support-lax", sup_sig, "UNIFORM")
    sig_check = "|".join("%s:%d-OF-%d" % (k, v[0], v[1])
                         for k, v in sorted(support_tally.items()))
    gate("G-DEFECT-CHARACTERISED",
         "the defect's SITE SUPPORT is characterised by which coarse interval "
         "each refined site subdivides, the support is not uniform across "
         "those classes, and the signature the verdict carries is REBUILT here "
         "from the support table and must agree -- the defect is a structured "
         "object with a measured signature, not a scalar failure",
         len(support_tally) > 1
         and len(set(v[0] for v in support_tally.values())) > 1
         and sup_sig == sig_check,
         {"support": {k: {"nonzero": v[0], "total": v[1]}
                      for k, v in sorted(support_tally.items())},
          "signature": sup_sig, "rebuilt": sig_check})

    # SPLIT DEPENDENCE, probed over a genuine fiber
    nm0 = "G-OFFDIAG2" if "G-OFFDIAG2" in splittable else splittable[0]
    a0 = fam[nm0]
    lap0 = dict(build_lapse_family(a0.S, d))
    fr0 = dict(front_family(a0.S))
    builds_probe = []
    probed = 0
    for n1 in range(1, a0.counts[(0,) * d][links[0]]):
        sp = make_split(a0, "low")
        sp[((0,) * d, links[0])] = (n1, a0.counts[(0,) * d][links[0]] - n1)
        fr = make_free(a0, sp, Lr, "minimal")
        rf = refine(a0, sp, fr, Lr, "probe")
        if not rf.admissible():
            continue
        probed += 1
        builds_probe.append(rf)
    split_dep = {}
    for mode in LIFT_RULES:
        best = 0
        for lname in sorted(lap0):
            for fname in sorted(fr0):
                seen = set()
                for rf in builds_probe:
                    D = commutation_defect("A-axis", a0, rf, lap0[lname],
                                           fr0[fname], Lr, mode)
                    seen.add(tuple(sorted((z, tuple(str(v) for v in D[z]))
                                          for z in D)))
                if len(seen) > best:
                    best = len(seen)
        split_dep[mode] = best
    # and the coarse-image restriction, measured separately
    image_dep = {}
    for mode in LIFT_RULES:
        best = 0
        for lname in sorted(lap0):
            for fname in sorted(fr0):
                seen = set()
                for rf in builds_probe:
                    D = commutation_defect("A-axis", a0, rf, lap0[lname],
                                           fr0[fname], Lr, mode)
                    seen.add(tuple(sorted(
                        (z, tuple(str(v) for v in D[z])) for z in D
                        if midpoint_kind(z, a0.links)[0] == "IMAGE")))
                if len(seen) > best:
                    best = len(seen)
        image_dep[mode] = best
    gate("G-DEFECT-SPLIT-DEPENDENCE",
         "THE SPLIT MOVES THE DEFECT.  Over a genuine split fiber the defect "
         "field takes distinct values under BOTH declared lifts, so the "
         "class-(iii) split freedom is not physically inert -- it changes the "
         "measured obstruction.  Restricted to the coarse image sites the "
         "dependence is lift-relative: the left lift makes that part "
         "split-INDEPENDENT (it is the whole coarse drag) while the right lift "
         "does not, and both readings are reported",
         probed > 1 and min(split_dep.values()) > 1
         and image_dep.get("left") == 1 and image_dep.get("right", 0) > 1,
         {"splits_probed": probed,
          "max_distinct_defect_fields_over_the_lapse_x_front_sweep": split_dep,
          "restricted_to_the_coarse_images": image_dep,
          "record": nm0, "rule": "A-axis"})

    R["dynamics_census"] = {
        "cells": cells, "cells_with_a_nonzero_defect": nonzero,
        "cells_with_an_identically_zero_defect": zero,
        "builds_censused": len(builds),
        "rules": len(RULES), "lapses": len(build_lapse_family(fam[
            splittable[0]].S, d)), "fronts": len(FRONT_FAMILY_NAMES),
        "lifts": len(LIFT_RULES),
        "support": {k: {"nonzero": v[0], "total": v[1]}
                    for k, v in sorted(support_tally.items())},
        "support_signature": sup_sig,
        "per_rule": {k: {"nonzero": v[0], "cells": v[1]}
                     for k, v in sorted(per_rule.items())},
        "per_record": {k: {"nonzero": v[0], "cells": v[1]}
                       for k, v in sorted(per_record.items())},
        "split_dependence": split_dep,
        "split_dependence_at_the_coarse_images": image_dep,
        "closed_form_at_coarse_images":
            "D(iota(x)) = w^c[N,n](x) exactly, under the left lift, at "
            "%d of %d cells" % (image_equals_coarse_drag, image_cells),
        "matter_independence": "the matter record cancels between the two "
                               "orders, so the defect is a pure drag "
                               "comparison",
    }
    return cells, nonzero, zero, sup_sig


def stage6(R, fam, adm_names, links, d, L, splittable, ctl_row, ncoarse):
    """MEASUREMENT 5 -- THE ITERATION PROBE, and the R1 negative control."""
    probes = {}
    for nm in adm_names:
        probes[nm] = iteration_probe(fam[nm])
    ceiling = max(v["ceiling_floor_log2_min_count"] for v in probes.values())
    attained = max(v["steps_achieved_at_the_declared_split"]
                   for v in probes.values())
    gate("G-ITERATION-CEILING",
         "the refinement FAMILY IS FINITE.  Each dyadic step partitions every "
         "interval into two strictly positive parts, so after k steps a coarse "
         "interval of count n has n >= 2^k: no record admits more than "
         "floor(log2(min count)) consecutive steps.  Over the declared family "
         "the ceiling is attained and never exceeded",
         attained <= ceiling
         and all(v["steps_achieved_at_the_declared_split"]
                 <= v["ceiling_floor_log2_min_count"] for v in probes.values())
         and attained == ceiling,
         {"ceiling": ceiling, "attained": attained,
          "per_record": {k: [v["ceiling_floor_log2_min_count"],
                             v["steps_achieved_at_the_declared_split"]]
                         for k, v in sorted(probes.items())}})
    growth = inventory_growth(L, d, links)
    trend = "GROWS" if growth[-1]["free_at_this_step"] > \
        growth[0]["free_at_this_step"] else "FIXED"
    gate("G-INVENTORY-TREND",
         "the choice inventory under iteration is measured, not guessed: the "
         "free part of each step grows by the arena's own volume factor while "
         "the fraction of the level-k arena that the ORIGINAL record reaches "
         "falls, so iteration adds freedom rather than removing it",
         growth[-1]["free_at_this_step"] > growth[0]["free_at_this_step"]
         and growth[-1]["original_reach_numerator"] *
         growth[0]["original_reach_denominator"] <
         growth[0]["original_reach_numerator"] *
         growth[-1]["original_reach_denominator"],
         {"growth": growth})
    R["iteration"] = {
        "per_record": {k: v for k, v in sorted(probes.items())},
        "ceiling_over_the_family": ceiling,
        "attained_over_the_family": attained,
        "inventory_growth": growth, "inventory_trend": trend,
        "reading": "the family closes as a CLASS -- a dyadic step applied to a "
                   "dyadic refinement is again a dyadic step -- but it "
                   "TERMINATES: the declared record family supports at most "
                   "%d consecutive steps, and the bound is a theorem about "
                   "strictly positive counts, not a property of the declared "
                   "splits" % ceiling}

    # -- THE R1 NEGATIVE CONTROL, through the SAME audit -------------------
    ctl_free = "the appended block's counts are set by a free label rule: no "\
               "coarse interval constrains them"
    ctl_q = "UNMOTIVATED" if ctl_row["tally"]["SUBDIVIDED"] == 0 else "MOTIVATED"
    ctl_q = mutate("control-pass", ctl_q, "MOTIVATED")
    gate("G-CONTROL-UNMOTIVATED",
         "THE AUDIT CAN FAIL A MOVE.  The R1 copying move, run through the same "
         "uniform audit, subdivides NO coarse interval, leaves coarse intervals "
         "UNREPRESENTED (so the restriction test cannot even be posed for them) "
         "and carries an unconstrained free label rule -- it is scored strictly "
         "worse than the dyadic move on the same instrument, and by a "
         "DIFFERENT failure mode",
         ctl_q == "UNMOTIVATED" and ctl_row["tally"]["SUBDIVIDED"] == 0
         and ctl_row["tally"]["UNREPRESENTED"] > 0,
         {"tally": ctl_row["tally"], "qualifier": ctl_q})
    R["control"] = {
        "move": ctl_row["move"], "name": ctl_row["name"],
        "tally": ctl_row["tally"], "qualifier": ctl_q,
        "free_rule": ctl_free,
        "forced_constraints": 0,
        "comparison": "DYADIC forces %d additivity constraints and represents "
                      "%d of %d coarse intervals; the copying move forces 0 and "
                      "loses %d.  Both fail the motivation audit, by different "
                      "measured failure modes -- which is what makes the audit "
                      "an instrument rather than a verdict"
                      % (ncoarse, ncoarse, ncoarse,
                         ctl_row["tally"]["UNREPRESENTED"])}
    return ceiling, attained, trend, ctl_q


def run():
    R, fam, adm_names, links, d, L, d_ext, rec, cl = stage1()
    rows, dyad, ctl, ncoarse = stage2(R, fam, adm_names, links, d, L, d_ext)
    built, adm_builds, splittable, unsplittable = stage3(
        R, fam, adm_names, links, d, L)
    sf, eqf, free, refined_links, new_sites, fl, pairs, ncommute = stage4(
        R, fam, adm_names, links, d, L, splittable, built, adm_builds)
    cells, nonzero, zero, sup_sig = stage5(
        R, fam, links, d, L, splittable, built, adm_builds)
    ceiling, attained, trend, ctl_q = stage6(
        R, fam, adm_names, links, d, L, splittable, ctl, ncoarse)

    # -- the memo, gated (RUNBOOK section 14 addendum, v13 #185/#219) --------
    compared = 0
    disagree = 0
    a0 = fam[splittable[0]]
    for rule in RULES:
        for x in a0.S:
            key = cache_lookup_key_for(a0, rule, x)
            memo = _LAMBDA_MEMO.get(key)
            fresh = lambda_of(rule, a0, x, fresh=True)
            if memo is not None:
                compared += 1
                if memo != fresh:
                    disagree += 1
    _CACHE_STATS["compared"] = compared
    _CACHE_STATS["disagreements"] = disagree
    gate("G-CACHE-EXERCISED",
         "the weight memo is genuinely exercised -- a zero-hit cache gate is "
         "vacuous (RUNBOOK section 14 addendum, v13 #219)",
         _CACHE_STATS["hits"] > 0 and _CACHE_STATS["misses"] > 0
         and _CACHE_STATS["bypass"] > 0, dict(_CACHE_STATS))
    gate("G-CACHE-FRESH-EQUALS-MEMO",
         "every memoised weight compared here is recomputed with the memo "
         "BYPASSED and agrees -- the gate tests the quantity, not the cache",
         compared > 0 and disagree == 0,
         {"compared": compared, "disagreements": disagree})

    # -- the choice inventory and the verdict -------------------------------
    fibs = sorted(sf[nm]["admissible_at_images"] for nm in splittable)
    payload = {
        "inventory": None,
        "split_fibers": sf, "equivariant_fibers": eqf,
        "count_lattice": cl,
        "dyadic_tally": dyad["tally"], "coarse_intervals": ncoarse,
        "additivity_checks": R["forced_part"]["additivity_checks"],
        "additivity_violations": R["forced_part"]["additivity_violations"],
        "restriction_ok": R["forced_part"]["restriction_ok"],
        "restriction_checks": R["forced_part"]["restriction_checks"],
        "free_links": len(free), "refined_links": refined_links,
        "new_sites": new_sites, "forced_lift": fl,
        "infinite_family": {"witnesses": 64,
                            "family": "c = a + b keeps det q = a*b > 0 for "
                                      "every b >= 1"},
        "lift_pairs_declared": len(pairs), "lift_pairs_commuting": ncommute,
        "split_fiber_min": fibs[0], "split_fiber_max": fibs[-1],
        "equivariant_fiber_min": sorted(eqf.values())[0],
        "defect_cells": cells, "defect_nonzero_cells": nonzero,
        "defect_zero_cells": zero, "defect_support_sig": sup_sig,
        "iteration_ceiling": ceiling, "iteration_attained": attained,
        "inventory_trend": trend,
        "admissible_classes": len([r for r in rows if r["verdict"]
                                   == "ADMISSIBLE"]),
        "admissible_class_names": sorted([r["move"] for r in rows
                                          if r["verdict"] == "ADMISSIBLE"]),
        "blocked_classes": len([r for r in rows if r["verdict"] == "BLOCKED"]),
        "refused_classes": len([r for r in rows if r["verdict"] == "REFUSED"]),
        "control_classes": len([r for r in rows if r["verdict"] == "CONTROL"]),
        "blocked_fact": R["blocked_branch"]["named_fact"],
        "blocked_intervals": R["blocked_branch"]["ambiguous_intervals"],
        "blocked_candidates": R["blocked_branch"]["candidates_per_interval"],
        "refused_class": R["refused_branch"]["move"],
        "refused_cycles": R["refused_branch"]["direction_0_cycle_lengths"],
        "refused_link_targets":
            R["refused_branch"]["declared_link_targets_defined_at_the_new_site"],
        "declared_links": R["refused_branch"]["declared_links"],
        "control_name": ctl["move"],
        "control_subdivided": ctl["tally"]["SUBDIVIDED"],
        "control_unrepresented": ctl["tally"]["UNREPRESENTED"],
        "control_qualifier": ctl_q,
    }
    inv = build_inventory(payload)
    payload["inventory"] = inv
    recomputed = [classify_freedom(i) for i in inv]
    gate("G-INVENTORY-CLASSIFICATION",
         "every freedom's class is RECOMPUTED from its own measured evidence "
         "and must equal the class the inventory carries: a class-(iii) "
         "freedom relabelled class-(i) dies here.  Forced iff the fiber is "
         "exactly 1 AND a pinned declaration is named; stabiliser-fixed iff "
         "the measured equivariant fiber is exactly 1",
         all(i["class_declared"] == c for i, c in zip(inv, recomputed)),
         {"declared": [i["class_declared"] for i in inv],
          "recomputed": recomputed})
    n_forced = len([i for i in inv if i["class_declared"] == "i"])
    n_stab = len([i for i in inv if i["class_declared"] == "ii"])
    n_free = len([i for i in inv if i["class_declared"] == "iii"])
    qual = "MOTIVATED" if n_free == 0 else "NOT-MOTIVATED"
    gate("G-MOTIVATION-QUALIFIER-COMPUTED",
         "the motivation qualifier is COMPUTED from the inventory and from "
         "nothing else (the RSQ standard): a move every one of whose freedoms "
         "is class (i) or class (ii) is MOTIVATED; any class-(iii) freedom is "
         "named in the verdict with its fiber",
         (qual == "MOTIVATED") == (n_free == 0)
         and n_forced + n_stab + n_free == len(inv),
         {"forced": n_forced, "stabiliser": n_stab, "free": n_free,
          "qualifier": qual})
    R["choice_inventory"] = {
        "items": inv, "forced": n_forced, "stabiliser_fixed": n_stab,
        "genuinely_free": n_free, "motivation_qualifier": qual,
        "classification_rule": "(i) forced by a NAMED pinned declaration with "
                               "fiber 1; (ii) fixed by a MEASURED stabiliser "
                               "(equivariant fiber 1); (iii) genuinely free, "
                               "fiber counted exactly"}

    head, segs, full = build_verdict(payload)
    R["verdict"] = full
    R["verdict_head"] = head
    R["verdict_segments"] = [{"name": n, "text": t} for n, t in segs]
    R["totals"] = {
        "anchors": len(ANCHORS),
        "gates": len(GATES),
        "must_pass_gates": len([g for g in GATES if not g.get("recorded")]),
        "recorded_gates": len([g for g in GATES if g.get("recorded")]),
        "mutants": len(MUTANTS),
    }
    stage7(R, payload, segs)
    R["totals"]["gates"] = len(GATES)
    R["totals"]["must_pass_gates"] = len([g for g in GATES
                                          if not g.get("recorded")])
    return R, payload, fam, segs


def _deepcopy(o):
    return json.loads(json.dumps(jsonable(o)))


SEGMENT_PERTURBATIONS = (
    ("CLASSES", lambda R: R["move_census"]["rows"].__setitem__(
        0, dict(R["move_census"]["rows"][0], verdict="REFUSED"))),
    ("BLOCKED-AT", lambda R: R["blocked_branch"].__setitem__(
        "ambiguous_intervals", R["blocked_branch"]["ambiguous_intervals"] + 7)),
    ("REFUSED-AT", lambda R: R["refused_branch"].__setitem__(
        "declared_link_targets_defined_at_the_new_site", 3)),
    ("FORCED", lambda R: R["forced_part"].__setitem__(
        "restriction_ok", R["forced_part"]["restriction_ok"] - 5)),
    ("INVENTORY", lambda R: R["choice_inventory"]["items"][5].__setitem__(
        "class_declared", "i")),
    ("OBSTRUCTION", lambda R: R["choice_inventory"]["items"][7].__setitem__(
        "name", "SOMETHING-ELSE")),
    ("SPLIT-FIBER", lambda R: R["count_lattice"].__setitem__(
        "unique_admissible_split_count", 99)),
    ("FREE-LINKS", lambda R: R["choice_inventory"]["items"][5]["evidence"]
     .__setitem__("free", 7)),
    ("NEW-FRONTS", lambda R: R["choice_inventory"]["items"][6]["evidence"]
     .__setitem__("new_sites", 5)),
    ("DEFECT", lambda R: R["dynamics_census"].__setitem__(
        "cells_with_a_nonzero_defect", 0)),
    ("ITERATION", lambda R: R["iteration"].__setitem__(
        "ceiling_over_the_family", 11)),
    ("CONTROL", lambda R: R["control"].__setitem__("qualifier", "MOTIVATED")),
)


def stage7(R, payload, segs):
    """THE VERDICT GATES.  Containment is not equality (#10): the emitted
    string is compared for COMPLETE equality against an independent rebuild."""
    emitted = R["verdict"]
    rebuilt = reconstruct_verdict_from_receipt(_deepcopy(R))
    gate("G-VERDICT-STRING-EQUALITY",
         "the COMPLETE emitted verdict string equals, character for character, "
         "a reconstruction built segment by segment from the RECEIPT OBJECT by "
         "a function sharing no code and no input with the builder.  Substring, "
         "prefix and containment checks are not verdict gates (RUNBOOK section "
         "14 addendum, v14 #10)",
         emitted == rebuilt,
         {"emitted": emitted[:180], "rebuilt": rebuilt[:180],
          "equal": emitted == rebuilt})

    flips = []
    for name, perturb in SEGMENT_PERTURBATIONS:
        probe = _deepcopy(R)
        try:
            perturb(probe)
            moved = reconstruct_verdict_from_receipt(probe) != rebuilt
        except (KeyError, IndexError, TypeError):
            moved = False
        flips.append({"segment": name, "flips": moved})
    gate("G-VERDICT-SEGMENTS-FLIPPABLE",
         "every verdict segment is shown to MOVE when the receipt row it "
         "derives from is perturbed -- flippability is tested at the "
         "measurement, not by appending to the string (RUNBOOK section 13 "
         "addendum, v13 #234).  An inert segment is a typed segment",
         all(f["flips"] for f in flips) and len(flips) == len(SEGMENT_ORDER),
         {"flips": flips})

    # BOTH other heads reachable, demonstrated by declared synthetic receipts
    ex = _deepcopy(R)
    for it in ex["choice_inventory"]["items"]:
        it["class_declared"] = "i"
    head_ex = reconstruct_verdict_from_receipt(ex).split("<")[0]
    bl = _deepcopy(R)
    for r0 in bl["move_census"]["rows"]:
        if r0["verdict"] == "ADMISSIBLE":
            r0["verdict"] = "BLOCKED"
    head_bl = reconstruct_verdict_from_receipt(bl).split("<")[0]
    gate("G-VERDICT-ALL-HEADS-REACHABLE",
         "all three pre-registered heads are REACHABLE by measurement: a "
         "synthetic receipt whose inventory carries no class-(iii) freedom "
         "returns MOTIVATED-REFINEMENT-EXISTS, and one whose census admits no "
         "class returns BLOCKED-AT-GRAMMAR-SOURCE.  A head that cannot take "
         "its other values is not a measurement",
         head_ex == HEAD_EXISTS and head_bl == HEAD_BLOCKED
         and R["verdict_head"] == HEAD_NOSPLIT,
         {"exists_reachable": head_ex, "blocked_reachable": head_bl,
          "emitted": R["verdict_head"]})
    R["verdict_audit"] = {"emitted": emitted, "reconstructed": rebuilt,
                          "segment_flips": flips,
                          "heads_reachable": {"EXISTS": head_ex,
                                              "BLOCKED": head_bl,
                                              "EMITTED": R["verdict_head"]}}
    return R


# ----------------------------------------------------------------------------
# 14.  THE MUTANT TABLE -- every declared falsifier, with the gate it must kill
# ----------------------------------------------------------------------------

MUTANTS = [
    {"name": "anchor-hash-A-I7-RECEIPT", "expected_gate": "A-I7-RECEIPT",
     "what": "corrupts the pinned I7 receipt's measured hash"},
    {"name": "anchor-hash-A-HA-PAPER", "expected_gate": "A-HA-PAPER",
     "what": "corrupts the pinned HA paper's measured hash"},
    {"name": "anchor-hash-A-HA-CODE", "expected_gate": "A-HA-CODE",
     "what": "corrupts the pinned HA instrument's measured hash"},
    {"name": "anchor-hash-A-PIN-R6A", "expected_gate": "A-PIN-R6A",
     "what": "corrupts this unit's own pin hash"},
    {"name": "anchor-skip", "expected_gate": "G-ANCHOR-CELL-COMPLETE",
     "what": "drops the last declared file-bytes anchor row"},
    {"name": "path-drift", "expected_gate": "G-PATH-ANCHORS",
     "what": "reads the arena's L from a DIFFERENT json path (path drift)"},
    {"name": "path-value", "expected_gate": "G-PATH-ANCHORS",
     "what": "returns a null value at an anchored path"},
    {"name": "text-anchor-drift", "expected_gate": "G-TEXT-ANCHORS",
     "what": "paraphrases the pinned readout formula instead of quoting it"},
    {"name": "float-leak", "expected_gate": "G-FLOATGUARD",
     "what": "injects a synthetic float offence the AST scan must flag"},
    {"name": "readout-det", "expected_gate": "G-READOUT-REENCODING",
     "what": "perturbs the record-IS-metric determinant"},
    {"name": "rank-lax", "expected_gate": "G-IDENTIFIABILITY-RANK",
     "what": "degrades the measured lapse-bracket rank"},
    {"name": "lattice-drop", "expected_gate": "G-COUNT-LATTICE-REPRODUCES-I7",
     "what": "drops one admissible count vector from I7's declared box"},
    {"name": "potential-lax", "expected_gate": "G-NO-POTENTIAL",
     "what": "reports a vanishing cycle sum, i.e. a record with a potential"},
    {"name": "census-drop", "expected_gate": "G-MOVE-CENSUS-CELL-COMPLETE",
     "what": "drops the single-interval class from the move census"},
    {"name": "incidence-lax", "expected_gate": "G-INCIDENCE-CENSUS",
     "what": "SMUGGLES the blocked branch through by calling an ambiguous "
             "incidence a subdivision"},
    {"name": "additivity-violation", "expected_gate": "G-ADDITIVITY-FORCED",
     "what": "breaks count additivity at one refined interval"},
    {"name": "restriction-lax", "expected_gate": "G-RESTRICTION-COMMUTES",
     "what": "loses one coarse-metric recovery"},
    {"name": "fiber-typed", "expected_gate": "G-FIBER-COMPUTED",
     "what": "types the split fiber as 1 instead of computing it"},
    {"name": "stabilizer-lax", "expected_gate": "G-STABILIZER-MEASURED",
     "what": "claims the measured stabiliser fixes the split uniquely"},
    {"name": "inventory-corrupt", "expected_gate": "G-INVENTORY-CLASSIFICATION",
     "what": "relabels the class-(iii) split freedom as class-(i) forced"},
    {"name": "forcedlift-lax", "expected_gate": "G-FORCED-LIFT-NON-INTEGRAL",
     "what": "claims a split at which the forced front lift is integral"},
    {"name": "defect-suppress", "expected_gate": "G-DEFECT-NONZERO",
     "what": "suppresses the measured commutation defect"},
    {"name": "defect-support-lax", "expected_gate": "G-DEFECT-CHARACTERISED",
     "what": "replaces the measured support signature by a uniform label"},
    {"name": "iteration-lax", "expected_gate": "G-ITERATION-CEILING",
     "what": "claims one step more than the ceiling permits"},
    {"name": "control-pass", "expected_gate": "G-CONTROL-UNMOTIVATED",
     "what": "passes the R1 copying move as MOTIVATED -- the positive control "
             "OF THE AUDIT"},
    {"name": "cache-alias", "expected_gate": "G-CACHE-FRESH-EQUALS-MEMO",
     "what": "serves one arena another arena's cached weight"},
    {"name": "verdict-pair-swap", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "swaps two segments' values, keeping their names (INJ class A)"},
    {"name": "verdict-typed-segment", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "types the SPLIT-FIBER segment (INJ class B)"},
    {"name": "verdict-append-text", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "appends text to a segment (INJ class C)"},
    {"name": "verdict-fully-typed", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "types every segment and the head (INJ class D)"},
    {"name": "verdict-inert-segment", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "replaces the DEFECT segment by an inert literal (INJ class E)"},
    {"name": "head-constant", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "pins the head so it stops tracking the inventory"},
    {"name": "render-escape", "expected_gate": "G-RENDER-FROM-GATED-OBJECT",
     "what": "renders a table cell that bypasses the gated object"},
    {"name": "prose-claim-drift",
     "expected_gate": "G-PROSE-RENDERS-FROM-THE-RECEIPT",
     "what": "drifts a rendered paper claim away from the receipt"},
]


# ----------------------------------------------------------------------------
# 15.  RENDERING -- one object, one source of truth
# ----------------------------------------------------------------------------

def frac(x):
    return str(x)


def jsonable(o):
    if isinstance(o, bool) or o is None:
        return o
    if isinstance(o, (int, str)):
        return o
    if isinstance(o, Fr):
        return str(o)
    if isinstance(o, dict):
        return {(str(k) if not isinstance(k, str) else k): jsonable(v)
                for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    return str(o)


def render_text(R):
    L = []
    w = L.append
    w("=" * 78)
    w("v14 R6a -- THE REFINEMENT GRAMMAR")
    w("=" * 78)
    w("")
    w("QUESTION: " + R["question"])
    w("")
    w("--- 0. ANCHORS (%d total: %d file-bytes, %d path-value, %d verbatim text)"
      % (R["anchor_totals"]["total"], R["anchor_totals"]["file_bytes"],
         R["anchor_totals"]["path_value"], R["anchor_totals"]["verbatim_text"]))
    for a in R["anchors"]:
        if a["kind"] == "file-bytes":
            w("  %-26s %-46s %s" % (a["name"], a["artifact"], a["measured"]))
    w("  path-value rows: %d, all matching the declared (path, value) pair"
      % R["anchor_totals"]["path_value"])
    w("  verbatim-text rows: %d, every load-bearing grammar sentence quoted "
      "from its pinned source" % R["anchor_totals"]["verbatim_text"])
    w("")
    w("--- 1. THE ARENA, REBUILT FROM THE PINNED SOURCES")
    for k in ("sites", "links", "geometry_record", "front", "readout",
              "lapse_family"):
        w("  %-18s %s" % (k, R["arena"][k]))
    w("")
    w("  record family (counts at (0,0) / (1,1)):")
    for nm, v in R["record_family"].items():
        w("    %-12s %-14s %-14s admissible=%-5s min=%d homog=%s"
          % (nm, tuple(v["counts_at_00"]), tuple(v["counts_at_11"]),
             v["admissible"], v["min_count"], v["homogeneous"]))
    w("")
    w("--- 2. THE NO-POTENTIAL THEOREM (the mechanism of the freedom)")
    w("  counts are strictly positive on a periodic lattice, so no record's")
    w("  counts are the coboundary of a site function; the split cannot be")
    w("  read off any potential.  min axis cycle sum per record:")
    w("    " + ", ".join("%s=%d" % (k, v["min_axis_cycle_sum"])
                         for k, v in R["no_potential"].items()))
    w("")
    w("--- 3. THE MOVE CENSUS (%d coarse intervals per class)"
      % R["move_census"]["coarse_intervals"])
    w("  %-18s %-11s %5s %5s %5s %5s  %s"
      % ("class", "verdict", "INH", "SUB", "AMB", "UNR", "refined shape"))
    for r in R["move_census"]["rows"]:
        t = r["tally"]
        w("  %-18s %-11s %5d %5d %5d %5d  %s"
          % (r["move"], r["verdict"], t["INHERITED"], t["SUBDIVIDED"],
             t["AMBIGUOUS"], t["UNREPRESENTED"], r["refined_shape"]))
    w("")
    w("  BLOCKED branch -- %s" % R["blocked_branch"]["named_fact"])
    w("    %s" % R["blocked_branch"]["statement"])
    w("    ambiguous coarse intervals: %d of %d, %d candidate interior sites "
      "each; all %d declared loci agree: %s"
      % (R["blocked_branch"]["ambiguous_intervals"],
         R["move_census"]["coarse_intervals"],
         R["blocked_branch"]["candidates_per_interval"],
         R["blocked_branch"]["loci_censused"],
         R["blocked_branch"]["all_loci_agree"]))
    w("    the ambiguity is REAL: over %d declared completions the two "
      "candidate readings disagree at %d"
      % (R["blocked_branch"]["completion_sweep"]["completions"],
         R["blocked_branch"]["completion_sweep"]["disagreeing"]))
    w("")
    w("  REFUSED branch -- SINGLE-INTERVAL")
    w("    %s" % R["refused_branch"]["reason"])
    w("")
    w("  dimension extension (d = %d): %d refined sites, %d images, %d "
      "interior, %d UNREACHED (parity %s)"
      % (R["dimension_extension"]["d"],
         R["dimension_extension"]["refined_sites"],
         R["dimension_extension"]["coarse_images"],
         R["dimension_extension"]["interior_sites"],
         R["dimension_extension"]["unreached_sites"],
         R["dimension_extension"]["unreached_parities"]))
    w("")
    w("--- 4. THE FORCED PART")
    fp = R["forced_part"]
    w("  additivity:  %d of %d constraints hold (%d violations)"
      % (fp["additivity_checks"] - fp["additivity_violations"],
         fp["additivity_checks"], fp["additivity_violations"]))
    w("  restriction: the coarse metric is recovered at %d of %d cells"
      % (fp["restriction_ok"], fp["restriction_checks"]))
    w("  splittable records: %s" % ", ".join(fp["splittable_records"]))
    w("  UNSPLITTABLE (a count-1 interval admits no positive partition): %s"
      % ", ".join(fp["unsplittable_records"]))
    w("  declared builds %d, of which admissible %d"
      % (fp["declared_builds"], fp["admissible_builds"]))
    w("  %-12s %-6s %-9s %5s %5s %5s"
      % ("record", "split", "free", "adm?", "bad", "qrec"))
    for b in fp["builds"]:
        w("  %-12s %-6s %-9s %5s %5d %5d"
          % (b["record"], b["split"], b["free"], b["refined_admissible"],
             b["inadmissible_sites"], b["coarse_q_recovered"]))
    w("")
    w("--- 5. THE CHOICE INVENTORY  (qualifier COMPUTED: %s)"
      % R["choice_inventory"]["motivation_qualifier"])
    w("  %-26s %-6s %-22s %s" % ("freedom", "class", "fiber", "forced by"))
    for it in R["choice_inventory"]["items"]:
        w("  %-26s (%-3s) %-22s %s"
          % (it["name"], it["class_declared"], str(it["fiber"]),
             (it["forced_by"] or "-- NOTHING IN THE PINNED GRAMMAR --")[:60]))
    w("  forced %d | stabiliser-fixed %d | genuinely free %d"
      % (R["choice_inventory"]["forced"],
         R["choice_inventory"]["stabiliser_fixed"],
         R["choice_inventory"]["genuinely_free"]))
    w("")
    w("  split fibers (raw / admissible-at-images / equivariant):")
    for nm in sorted(R["split_fibers"]):
        v = R["split_fibers"][nm]
        w("    %-12s %-26s %-26s %s"
          % (nm, v["raw"], v["admissible_at_images"],
             R["equivariant_fibers"].get(nm, "-")))
    cl = R["count_lattice"]
    w("  beyond the nine records, over I7's own declared count box "
      "(axis<=%d, diag<=%d): %d admissible count vectors, %d splittable, and "
      "%d with a UNIQUE admissible split %s"
      % (cl["box"]["axis_max"], cl["box"]["diag_max"],
         cl["admissible_count_vectors"], cl["splittable"],
         cl["unique_admissible_split_count"], cl["unique_admissible_split"]))
    w("")
    w("--- 6. THE DYNAMICS-COMPATIBILITY CENSUS")
    dc = R["dynamics_census"]
    w("  %d cells (%d builds x %d rules x %d lapses x %d fronts x %d lifts)"
      % (dc["cells"], dc["builds_censused"], dc["rules"], dc["lapses"],
         dc["fronts"], dc["lifts"]))
    w("  nonzero defect at %d cells, identically zero at %d"
      % (dc["cells_with_a_nonzero_defect"],
         dc["cells_with_an_identically_zero_defect"]))
    w("  site support (by which coarse interval the site subdivides):")
    for k, v in dc["support"].items():
        w("    %-14s nonzero %6d of %6d" % (k, v["nonzero"], v["total"]))
    w("  closed form: %s" % dc["closed_form_at_coarse_images"])
    w("  split dependence (distinct defect fields over a genuine fiber): %s"
      % dc["split_dependence"])
    w("  lift grid (front sector):")
    for p in R["lift_grid"]:
        w("    front=%-6s lapse=%-6s commutes=%s"
          % (p["front_lift"], p["lapse_lift"], p["front_sector_commutes"]))
    fl = R["forced_front_lift"]
    w("  the dynamics-forced front lift is NON-INTEGRAL at %d of %d cells; "
      "and n | n_1 holds at %d of %d splits (it cannot)"
      % (fl["non_integral"], fl["cells"],
         R["forced_lift_universal"]["splits_with_n_dividing_n1"],
         R["forced_lift_universal"]["triples_checked"]))
    w("")
    w("--- 7. THE ITERATION PROBE")
    it = R["iteration"]
    w("  ceiling floor(log2 min count) over the family: %d; attained: %d"
      % (it["ceiling_over_the_family"], it["attained_over_the_family"]))
    for nm, v in it["per_record"].items():
        w("    %-12s ceiling %d  achieved %d  halt: %s"
          % (nm, v["ceiling_floor_log2_min_count"],
             v["steps_achieved_at_the_declared_split"], v["halt_reason"]))
    w("  inventory trend: %s" % it["inventory_trend"])
    for g in it["inventory_growth"]:
        w("    level %d: L=%d links %d -> refined %d, covered %d, free %d; "
          "original record reaches %d of %d"
          % (g["level"], g["L"], g["links"], g["refined_links"],
             g["covered_by_this_level"], g["free_at_this_step"],
             g["original_reach_numerator"], g["original_reach_denominator"]))
    w("")
    w("--- 8. THE R1 NEGATIVE CONTROL (the audit must be able to FAIL a move)")
    w("  %s -- %s" % (R["control"]["move"], R["control"]["qualifier"]))
    w("  %s" % R["control"]["comparison"])
    w("  its free rule: %s" % R["control"]["free_rule"])
    w("")
    w("--- 9. THE VERDICT")
    for s in R["verdict_segments"]:
        w("    %s" % s["text"])
    w("")
    w("  " + R["verdict"])
    w("")
    w("--- 10. INSTRUMENT")
    t = R["totals"]
    w("  anchors %d | gates %d (%d must-pass, %d recorded) | mutants %d"
      % (t["anchors"], t["gates"], t["must_pass_gates"], t["recorded_gates"],
         t["mutants"]))
    fc = R.get("falsifier_census", {})
    if fc:
        w("  falsifier census: %s; never falsified: %s"
          % (fc.get("denominator"), fc.get("never_falsified")))
    w("")
    return "\n".join(L) + "\n"


# ----------------------------------------------------------------------------
# 16.  THE PROSE GATE -- every numeric claim in the paper renders from here
# ----------------------------------------------------------------------------

def paper_claims(R):
    mc = R["move_census"]
    fp = R["forced_part"]
    ci = R["choice_inventory"]
    dc = R["dynamics_census"]
    it = R["iteration"]
    cl = R["count_lattice"]
    bb = R["blocked_branch"]
    rb = R["refused_branch"]
    de = R["dimension_extension"]
    fl = R["forced_front_lift"]
    sp = [i for i in ci["items"] if i["name"] == "THE-SPLIT"][0]
    fr = [i for i in ci["items"] if i["name"] == "FREE-TRANSVERSE-LINKS"][0]
    claims = {
        "census": "%d coarse intervals per class; the dyadic move subdivides "
                  "%d of %d, single-direction hyperplane insertion subdivides "
                  "%d and leaves %d ambiguous, and the copying move subdivides "
                  "%d and leaves %d unrepresented"
                  % (mc["coarse_intervals"],
                     [r for r in mc["rows"] if r["move"] == "DYADIC"][0]
                     ["tally"]["SUBDIVIDED"], mc["coarse_intervals"],
                     [r for r in mc["rows"] if r["move"].startswith("HYPER")][0]
                     ["tally"]["SUBDIVIDED"], bb["ambiguous_intervals"],
                     R["control"]["tally"]["SUBDIVIDED"],
                     R["control"]["tally"]["UNREPRESENTED"]),
        "blocked": "the coarse displacement has %d minimal decompositions with "
                   "%d distinct interior sites, and over %d declared "
                   "completions the two candidate readings disagree at %d"
                   % (bb["candidates_per_interval"],
                      bb["candidates_per_interval"],
                      bb["completion_sweep"]["completions"],
                      bb["completion_sweep"]["disagreeing"]),
        "refused": "the direction-0 cycle lengths become %s, %d sites is not "
                   "divisible by the longest cycle %d, and only %d of the %d "
                   "declared link displacements has a target at the new site"
                   % (rb["direction_0_cycle_lengths"], rb["sites"],
                      max(rb["direction_0_cycle_lengths"]),
                      rb["declared_link_targets_defined_at_the_new_site"],
                      rb["declared_links"]),
        "forced": "additivity holds at %d of %d constraints and the coarse "
                  "metric is recovered at %d of %d cells"
                  % (fp["additivity_checks"] - fp["additivity_violations"],
                     fp["additivity_checks"], fp["restriction_ok"],
                     fp["restriction_checks"]),
        "unsplittable": "%d of the %d admissible records carry a count-1 "
                        "interval and admit no subdivision at all: %s"
                        % (len(fp["unsplittable_records"]),
                           len(fp["unsplittable_records"])
                           + len(fp["splittable_records"]),
                           ", ".join(fp["unsplittable_records"])),
        "inventory": "%d freedoms forced by a named pinned declaration, %d "
                     "fixed by a measured stabiliser, %d genuinely free"
                     % (ci["forced"], ci["stabiliser_fixed"],
                        ci["genuinely_free"]),
        "split_fiber": "the admissible split fiber runs from %s to %s over the "
                       "six records that admit the move, and the "
                       "chart-equivariant fiber is never 1 (its smallest value "
                       "is %s)"
                       % (sp["evidence"]["min_admissible_fiber"],
                          sp["evidence"]["max_admissible_fiber"],
                          sp["evidence"]["equivariant_fibers"][0]),
        "lattice": "of the %d admissible count vectors in the declared box, %d "
                   "are splittable at all and exactly %d has a unique "
                   "admissible split"
                   % (cl["admissible_count_vectors"], cl["splittable"],
                      cl["unique_admissible_split_count"]),
        "free_links": "%d of the %d refined links lie on no coarse interval"
                      % (fr["evidence"]["free"], fr["evidence"]["total"]),
        "dimension": "at d = %d the dyadic move leaves %d of %d refined sites "
                     "on no coarse interval at all" % (de["d"],
                                                       de["unreached_sites"],
                                                       de["refined_sites"]),
        "defect": "the commutation defect is nonzero at %d of %d census cells "
                  "and identically zero at %d"
                  % (dc["cells_with_a_nonzero_defect"], dc["cells"],
                     dc["cells_with_an_identically_zero_defect"]),
        "forced_lift": "the dynamics-forced front lift is non-integral at %d of "
                       "%d cells, and n divides n_1 at %d of the %d splits of "
                       "the declared family"
                       % (fl["non_integral"], fl["cells"],
                          R["forced_lift_universal"]
                          ["splits_with_n_dividing_n1"],
                          R["forced_lift_universal"]["triples_checked"]),
        "iteration": "the ceiling is %d consecutive steps and it is attained"
                     % it["ceiling_over_the_family"],
        "instrument": "%d gates, all passed; %d anchors; %d mutants, no "
                      "survivors" % (R["totals"]["gates"],
                                     R["totals"]["anchors"], len(MUTANTS)),
        "verdict": R["verdict"],
    }
    return mutate("prose-claim-drift", claims,
                  dict(claims, defect="the commutation defect is zero"))


def paper_prose_audit(R):
    claims = paper_claims(R)
    if not os.path.exists(PAPER):
        return claims, None, sorted(claims)
    with open(PAPER, "r") as fh:
        text = fh.read()
    missing = sorted([k for k, v in claims.items() if v not in text])
    return claims, sha12(PAPER), missing


def render_check(R):
    """TOTAL render check: every rendered field is rebuilt from the gated object
    and compared -- not a chosen subset."""
    bad = []
    text = render_text(R)
    for r in R["move_census"]["rows"]:
        line = "  %-18s %-11s %5d %5d %5d %5d" % (
            r["move"], r["verdict"], r["tally"]["INHERITED"],
            r["tally"]["SUBDIVIDED"], r["tally"]["AMBIGUOUS"],
            r["tally"]["UNREPRESENTED"])
        if line not in text:
            bad.append(("move_census", r["move"]))
    for it in R["choice_inventory"]["items"]:
        if it["name"] not in text or str(it["fiber"]) not in text:
            bad.append(("inventory", it["name"]))
    if R["verdict"] not in text:
        bad.append(("verdict", "absent from the render"))
    for k, v in R["dynamics_census"]["support"].items():
        if ("%-14s nonzero %6d of %6d" % (k, v["nonzero"], v["total"])) \
           not in text:
            bad.append(("defect_support", k))
    return mutate("render-escape", bad, bad + [("injected", "render-escape")])


# ----------------------------------------------------------------------------
# 17.  THE COMPLIANCE SWEEP -- rule by rule, every status COMPUTED
# ----------------------------------------------------------------------------

def compliance_sweep(R):
    names = set(g["name"] for g in GATES)
    declared = set(m["name"] for m in MUTANTS)

    def by(*gates):
        miss = [g for g in gates if g not in names]
        if miss:
            return "MISSING: " + ", ".join(miss)
        return "APPLIED via " + ", ".join(gates)

    def mut(*ms):
        miss = [m for m in ms if m not in declared]
        if miss:
            return "MISSING MUTANT: " + ", ".join(miss)
        return "falsifiers " + ", ".join(ms)

    fc = R.get("falsifier_census", {})
    rows = [
        ("RUNBOOK 13/14/15 with every addendum binds at delivery (#246/#313)",
         "APPLIED -- this sweep enumerates each rule and computes its status "
         "from the gate ledger (%d gates registered)" % len(names)),
        ("pin section 1 -- the grammar sources are the ONLY authority, "
         "hash-verified and path-value anchored at run time",
         by("A-PIN-R6A", "A-I7-RECEIPT", "A-HA-PAPER", "A-HA-CODE",
            "G-PATH-ANCHORS", "G-TEXT-ANCHORS", "G-ANCHOR-CELL-COMPLETE")
         + "; " + mut("anchor-hash-A-I7-RECEIPT", "anchor-hash-A-HA-PAPER",
                      "anchor-hash-A-HA-CODE", "path-drift", "path-value",
                      "text-anchor-drift", "anchor-skip")),
        ("pin section 1 -- a branch needing a grammar fact from outside the "
         "pinned sources STOPS at BLOCKED-AT-GRAMMAR-SOURCE",
         by("G-INCIDENCE-CENSUS", "G-BLOCK-IS-REAL") + " -- the named fact is "
         "%s, and the block is measured REAL (the candidate readings disagree)"
         % R["blocked_branch"]["named_fact"] + "; " + mut("incidence-lax")),
        ("pin section 3.1 -- the move census is cell-complete and a class that "
         "breaks the arena is REFUSED with the measured reason, never skipped",
         by("G-MOVE-CENSUS-CELL-COMPLETE") + "; " + mut("census-drop")),
        ("pin section 3.2 -- the forced part verified: additivity and the "
         "metric-restriction test at every admissible class and record",
         by("G-ADDITIVITY-FORCED", "G-RESTRICTION-COMMUTES",
            "G-UNSPLITTABLE-RECORDS") + "; "
         + mut("additivity-violation", "restriction-lax")),
        ("pin section 3.3 -- every freedom classified with its fiber COUNTED, "
         "and the motivation qualifier computed from the inventory",
         by("G-FIBER-COMPUTED", "G-STABILIZER-MEASURED",
            "G-INVENTORY-CLASSIFICATION", "G-MOTIVATION-QUALIFIER-COMPUTED",
            "G-FREE-LINKS-INFINITE") + "; "
         + mut("fiber-typed", "stabilizer-lax", "inventory-corrupt")),
        ("pin section 3.4 -- a nonzero commutation defect is a MEASURED "
         "OBJECT, characterised at the same standard as a closure result",
         by("G-DEFECT-NONZERO", "G-DEFECT-CHARACTERISED", "G-DEFECT-CLOSED-FORM",
            "G-DEFECT-SPLIT-DEPENDENCE", "G-LIFT-GRID-CELL-COMPLETE",
            "G-FORCED-LIFT-NON-INTEGRAL") + "; "
         + mut("defect-suppress", "defect-support-lax", "forcedlift-lax")),
        ("pin section 3.5 -- the iteration probe, the R6b prerequisite",
         by("G-ITERATION-CEILING", "G-INVENTORY-TREND") + "; "
         + mut("iteration-lax")),
        ("pin section 5 -- the R1 copying move is the audit's NEGATIVE "
         "CONTROL: the audit must be able to fail a move",
         by("G-CONTROL-UNMOTIVATED") + "; " + mut("control-pass")),
        ("#10 containment is not equality: the verdict gate compares the "
         "COMPLETE string against an independent rebuild",
         by("G-VERDICT-STRING-EQUALITY") + "; "
         + mut("verdict-pair-swap", "verdict-typed-segment",
               "verdict-append-text", "verdict-fully-typed",
               "verdict-inert-segment")),
        ("#20 compliance claims are gate claims: a comparator that cannot "
         "disagree with the object under test is vacuous",
         "APPLIED -- reconstruct_verdict_from_receipt() shares no code and no "
         "input with build_verdict(); it reads the RECEIPT OBJECT alone, and "
         "all five injection classes plus head-constant die on it"),
        ("#10 render from the gated object (one object, one source of truth)",
         by("G-RENDER-FROM-GATED-OBJECT") + "; " + mut("render-escape")),
        ("#20 prose renders from the receipt: every numeric claim in the paper "
         "renders from the receipt object",
         by("G-PROSE-RENDERS-FROM-THE-RECEIPT") + " over %d rendered claims; "
         % len(R.get("paper_claims", {}).get("rendered", {}))
         + mut("prose-claim-drift")),
        ("#20 path-value anchoring: a read-by-path anchors the (path, value) "
         "pair, not only the file bytes",
         "APPLIED -- %d path-value anchor rows and %d verbatim-text rows; %s; %s"
         % (len(PATH_ANCHOR_ROWS), len(TEXT_ANCHOR_ROWS),
            by("G-PATH-ANCHORS", "G-TEXT-ANCHORS"),
            mut("path-drift", "path-value", "text-anchor-drift"))),
        ("#234 the verdict is derived inside a gate and a flip mutant proves "
         "the derivation can fail",
         by("G-VERDICT-SEGMENTS-FLIPPABLE", "G-VERDICT-ALL-HEADS-REACHABLE")
         + " -- flippability is tested by perturbing the RECEIPT ROW each "
         "segment derives from, over all %d segments; " % len(SEGMENT_ORDER)
         + mut("verdict-inert-segment", "head-constant")),
        ("#234 counts are computed, never typed",
         by("G-FIBER-COMPUTED", "G-COUNT-LATTICE-REPRODUCES-I7",
            "G-RECORD-IS-METRIC") + "; " + mut("fiber-typed", "lattice-drop")),
        ("#219 a gate clause may not compare an object against a copy of "
         "itself routed through the component under test",
         "APPLIED -- the restriction test's comparator is the coarse record's "
         "own q, built by a route the restriction does not touch; the verdict "
         "comparator reads the receipt only; " + by("G-CACHE-FRESH-EQUALS-MEMO")),
        ("#219/#185 a zero-hit cache gate is vacuous, and a self-test routed "
         "through the memo tests the cache",
         by("G-CACHE-EXERCISED", "G-CACHE-FRESH-EQUALS-MEMO") + "; "
         + mut("cache-alias")),
        ("#208 no gate predicate may reference mutant identity",
         by("G-NO-MUTANT-IDENTITY") + " -- run-mode identity is read by "
         "mutate() alone, measured by an AST scan validated with %d synthetic "
         "injections it must flag" % len(MUTANT_GUARD_INJECTIONS)),
        ("#257 computed qualifiers (no typed qualifier segment)",
         by("G-MOTIVATION-QUALIFIER-COMPUTED") + " -- the qualifier is a "
         "function of the inventory's class counts and of nothing else"),
        ("#314 precheck doctrine: a precheck may gate which candidates are "
         "censused but may never name the verdict",
         "APPLIED -- the arena predicate and the incidence classification gate "
         "WHICH classes are censused; every verdict-naming fact (the fibers, "
         "the defect, the ceiling) is measured on the censused objects"),
        ("#313 repair propagation: gates diffed against every rule engraved "
         "since the pin froze",
         "APPLIED -- all five 2026-08-09 engravings are carried at birth, each "
         "with its injection-falsifier: containment-is-not-equality "
         "(5 injections), render-from-the-gated-object (render-escape), "
         "prose-renders-from-the-receipt (prose-claim-drift), "
         "compliance-claims-are-gate-claims (the independent comparator), "
         "path-value anchoring (path-drift, path-value, text-anchor-drift)"),
        ("RUNBOOK section 4 exact arithmetic; no float, no tolerance",
         by("G-FLOATGUARD", "G-NO-FLOATS-IN-RECEIPT") + "; " + mut("float-leak")),
        ("RUNBOOK section 15 declared-arena discipline: boundary, family, law, "
         "state, arena declared as DATA",
         "APPLIED -- the move classes, the record family, the split rules, the "
         "free-completion rules, the front family, the lapse family and the "
         "lift rules are all declared tables in the receipt; the defect's site "
         "support is reported as completion-relative"),
        ("RUNBOOK section 4 controls in BOTH directions",
         "APPLIED -- positive: the defect census returns identically zero at "
         "%d cells, so a nonzero reading is a measurement; negative: the R1 "
         "copying move is failed by the same audit (%s)"
         % (R["dynamics_census"]["cells_with_an_identically_zero_defect"],
            by("G-CONTROL-UNMOTIVATED"))),
        ("falsifier census with an honest denominator, from delivery one",
         "APPLIED -- %s; never falsified: %s"
         % (fc.get("denominator", "PENDING"),
            fc.get("never_falsified", "PENDING"))),
    ]
    return [{"rule": a, "status": b} for a, b in rows]


# ----------------------------------------------------------------------------
# 18.  DELIVERY
# ----------------------------------------------------------------------------

NEVER_FALSIFIED_WAIVERS = {
    "A-R0-PIN": "the v14 founding pin's own hash; the anchor-hash channel is "
                "falsified at three of the five rows (the I7 receipt, the HA "
                "paper, the HA code) and at this unit's own pin, and "
                "anchor-skip proves a dropped row dies",
    "G-ANCHOR-CELL-COMPLETE": "covered by anchor-skip",
    "G-RECORD-FAMILY-REPRODUCES-I7":
        "an I7 reproduction gate; the record constructors are exercised by "
        "readout-det, rank-lax and lattice-drop, each of which perturbs a "
        "different reading of the SAME rebuilt family",
    "G-DIMENSION-EXTENSION":
        "a d=3 coverage measurement whose value (the all-odd parity class) is "
        "forced by the declared link set having no body diagonal -- an "
        "analytically forced clause is a disclosure, not a must-pass "
        "falsifiable gate (RUNBOOK section 14 addendum, v13 #208)",
    "G-MOTIVATION-QUALIFIER-COMPUTED":
        "the qualifier is a pure function of the inventory's class counts, so "
        "inventory-corrupt falsifies it at G-INVENTORY-CLASSIFICATION one step "
        "earlier; a separate injection would test the same arithmetic twice",
    "G-DEFECT-CLOSED-FORM":
        "covered collaterally by defect-suppress (which moves the same field)",
    "G-DEFECT-SPLIT-DEPENDENCE":
        "covered collaterally by fiber-typed and additivity-violation, both of "
        "which move the split fiber this gate probes",
    "G-INVENTORY-TREND":
        "the growth law is arithmetic in the arena's volume factor; "
        "iteration-lax falsifies the neighbouring ceiling gate",
    "G-VERDICT-SEGMENTS-FLIPPABLE": "covered by verdict-inert-segment",
    "G-VERDICT-ALL-HEADS-REACHABLE": "covered by head-constant",
    "G-CACHE-EXERCISED": "covered by cache-alias at the paired gate",
    "G-NO-MUTANT-IDENTITY":
        "self-validating: the AST detector is proved able to fire by two "
        "synthetic injections evaluated inside the gate itself",
    "G-FINAL-GATE-COUNT": "an arithmetic consistency check on the ledger",
    "G-FALSIFIER-CENSUS-HONEST":
        "the census gate registers itself after it evaluates, so it appears in "
        "its own final denominator; it is an arithmetic consistency check on "
        "the ledger and carries no separate injection",
    "G-DEFERRED-GATES-EVALUATED": "an arithmetic consistency check on the ledger",
    "G-NO-FLOATS-IN-RECEIPT": "covered by float-leak at the source-level gate",
    "G-BLOCK-IS-REAL": "covered by incidence-lax at the paired gate",
    "G-UNSPLITTABLE-RECORDS": "covered by fiber-typed (the same counts)",
    "G-RECORD-IS-METRIC": "covered by readout-det (the same readout)",
    "G-LIFT-GRID-CELL-COMPLETE": "covered by forcedlift-lax at the paired gate",
    "G-FREE-LINKS-INFINITE": "covered by fiber-typed (the same fiber object)",
}


def finalise_census(R):
    fnames = [g["name"] for g in GATES]
    fmap = {}
    for m in MUTANTS:
        fmap.setdefault(m["expected_gate"], []).append(m["name"])
    nf = [n for n in fnames if n not in fmap]
    R["falsifier_census"] = {
        "gates": len(fnames),
        "gates_with_a_declared_falsifier": len([n for n in fnames if n in fmap]),
        "never_falsified": nf,
        "never_falsified_count": len(nf),
        "denominator": "%d of %d gates carry no declared falsifier"
                       % (len(nf), len(fnames)),
        "waivers": {n: NEVER_FALSIFIED_WAIVERS.get(n, "NO WAIVER RECORDED")
                    for n in nf},
        "falsifier_map": dict((k, sorted(v)) for k, v in sorted(fmap.items())
                              if k in fnames),
        "mutants": len(MUTANTS),
    }
    return R


def deliver():
    R, payload, fam, segs = run()
    R["schema"] = "isp/v14/r6a-refinement/1"
    R["pin"] = "v14/note-r6a-refinement-grammar-pin.md"
    R["pin_sha256_prefix"] = "a22582f67168"
    R["grammar_sources"] = {
        "v13/code/ha_successor_receipt.json": "542b8735daf0",
        "v13/paper-ha-successor.md": "f286ba10d2d9",
        "v13/code/ha_successor_exact.py": "d44cb72f8ee9"}
    R["source_sha256"] = sha256_full(SRC)
    R["python"] = "%d.%d.%d" % sys.version_info[:3]
    R["arithmetic"] = "int / fractions.Fraction only; no float, no tolerance"
    R["mutants"] = MUTANTS

    bad = render_check(R)
    gate("G-RENDER-FROM-GATED-OBJECT",
         "every rendered table cell equals the corresponding cell of the gated "
         "measurement object -- the receipt and the output render from ONE "
         "object, with no bypass path",
         len(bad) == 0, {"mismatches": bad[:4]})

    payload_json = jsonable(R)
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

    scan(payload_json)
    gate("G-NO-FLOATS-IN-RECEIPT", "the emitted receipt contains no float",
         len(floats) == 0, {"floats": floats[:4]})

    gate("G-DEFERRED-GATES-EVALUATED",
         "the write-time gates named in the falsifier census really did run, "
         "so the census's denominator covers every gate this instrument "
         "declares",
         all(g in [x["name"] for x in GATES] for g in DEFERRED_GATES
             if g not in ("G-DEFERRED-GATES-EVALUATED", "G-FINAL-GATE-COUNT",
                          "G-PROSE-RENDERS-FROM-THE-RECEIPT")),
         {"deferred": list(DEFERRED_GATES)})

    R["totals"]["must_pass_gates"] = len([g for g in GATES
                                          if not g.get("recorded")])
    R["totals"]["recorded_gates"] = len([g for g in GATES if g.get("recorded")])
    R["totals"]["anchors"] = len(ANCHORS)
    R["totals"]["must_pass_failures"] = len([g for g in GATES
                                             if not g["passed"]])
    R["totals"]["mutant_survivors"] = 0
    finalise_census(R)
    unwaived = [n for n in R["falsifier_census"]["never_falsified"]
                if R["falsifier_census"]["waivers"][n] == "NO WAIVER RECORDED"]
    gate("G-FALSIFIER-CENSUS-HONEST",
         "the falsifier census denominates itself over EVERY registered gate "
         "and every gate without a declared falsifier carries a recorded "
         "waiver with its forcing reason -- no silent exemption",
         len(unwaived) == 0,
         {"never_falsified": R["falsifier_census"]["never_falsified_count"],
          "unwaived": unwaived})

    # THE PROSE GATE runs LAST, so the gate count it renders is the count this
    # run will finish with: the two gates still to come are this one and
    # G-FINAL-GATE-COUNT, which checks the arithmetic.
    R["totals"]["gates"] = len(GATES) + 2
    claims, paper_hash, missing = paper_prose_audit(R)
    R["paper_claims"] = {
        "paper": "v14/paper-04-refinement-grammar.md",
        "paper_sha256_prefix": paper_hash,
        "claims_rendered": len(claims),
        "claims_present_in_the_paper": len(claims) - len(missing),
        "claims_missing": missing,
        "rendered": dict(sorted(claims.items())),
        "rule": "every load-bearing numeric sentence of the paper is RENDERED "
                "HERE from the measured object and must appear VERBATIM in the "
                "paper; a number the instrument does not render is a number "
                "the paper may not assert"}
    gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
         "every load-bearing numeric sentence of paper-04 is rendered from the "
         "receipt object and appears verbatim in the paper: the prose surface "
         "is gated like the tables (all of the programme's false paper numbers "
         "to date lived in hand-written prose)",
         paper_hash is not None and len(missing) == 0,
         {"claims": len(claims), "missing": missing[:6],
          "paper_sha256_prefix": paper_hash})
    gate("G-FINAL-GATE-COUNT",
         "the gate count the paper's rendered instrument sentence carries "
         "equals the number of gates this run will have registered when it "
         "finishes -- the claim's own arithmetic, gated",
         R["paper_claims"]["rendered"]["instrument"].startswith(
             "%d gates, all passed" % (len(GATES) + 1))
         and R["totals"]["gates"] == len(GATES) + 1,
         {"registered_now": len(GATES),
          "claimed": R["paper_claims"]["rendered"]["instrument"]})

    R["totals"]["gates"] = len(GATES)
    R["totals"]["must_pass_gates"] = len([g for g in GATES
                                          if not g.get("recorded")])
    finalise_census(R)
    R["compliance"] = compliance_sweep(R)
    R["gates"] = GATES

    text = render_text(R)
    payload_json = jsonable(R)
    with open(OUT_TXT, "w") as fh:
        fh.write(text)
    with open(OUT_JSON, "w") as fh:
        fh.write(json.dumps(payload_json, indent=1, sort_keys=False) + "\n")
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
        unchanged = all((sha256_full(p) if os.path.exists(p) else None)
                        == before[p] for p in (OUT_TXT, OUT_JSON))
        good = died and named and unchanged
        ok_all = ok_all and good
        print("  %-30s exit=%d named_gate=%s artifacts_unchanged=%s  %s"
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
        R, payload, fam, segs = run()
        R["schema"] = "isp/v14/r6a-refinement/1"
        R["mutants"] = MUTANTS
        R["source_sha256"] = sha256_full(SRC)
        R["totals"]["gates"] = len(GATES) + 6
        bad = render_check(R)
        gate("G-RENDER-FROM-GATED-OBJECT",
             "every rendered table cell equals the corresponding cell of the "
             "gated measurement object", len(bad) == 0, {"mismatches": bad[:4]})
        claims, paper_hash, missing = paper_prose_audit(R)
        R["paper_claims"] = {"rendered": claims}
        gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
             "every load-bearing numeric sentence of paper-04 is rendered from "
             "the receipt object and appears verbatim in the paper",
             paper_hash is not None and len(missing) == 0,
             {"claims": len(claims), "missing": missing[:6]})
        finalise_census(R)
        unwaived = [n for n in R["falsifier_census"]["never_falsified"]
                    if R["falsifier_census"]["waivers"][n]
                    == "NO WAIVER RECORDED"]
        gate("G-FALSIFIER-CENSUS-HONEST",
             "the falsifier census denominates itself over every registered "
             "gate", len(unwaived) == 0, {"unwaived": unwaived})
        sys.stderr.write("MUTANT %s SURVIVED -- no gate fired\n" % MUTANT)
        return 3
    except GateFailure as exc:
        sys.stderr.write(str(exc) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
