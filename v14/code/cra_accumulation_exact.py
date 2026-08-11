#!/usr/bin/env python3
"""
v14 CR-A -- REFINEMENT BY ACCUMULATION.  Exact instrument.

PIN: v14/note-cr-batch-pins.md, section CR-A (frozen v14 ledger #30, sha256-12
1cfee4fc0891).  The pin is verified BY HASH at run time (anchor A-PIN-CRA), and
so are the three pinned sources: I7's receipt (542b8735daf0), the HA paper
(f286ba10d2d9) and the HA instrument (d44cb72f8ee9).  Every value this unit
reads out of the pinned receipt is anchored as a (path, value) PAIR, never as
file bytes alone (RUNBOOK section 14 addendum, v14 #20).

THE QUESTION (pin section CR-A, three-way, every head first class):
  H_a[N] advances the FRONT n(x); the geometry record s = {n_l(x)} is
  background.  (1) Does the pinned grammar contain any geometry-record-
  ADVANCING move -- an analog of front advance that writes new interval
  events?  (2) For each admissible mover, does the RESCALED geometry converge
  along the declared schedules?  (3) A hand-declared external growth move must
  be flagged FOREIGN by the same audit.

Registered heads (pin, verbatim):
  CRA-RESCALED-CONVERGES-<move, schedule, limit>
  CRA-DIVERGES-<mode>
  CRA-BLOCKED-AT-STATIC-GEOMETRY
Each is derived INSIDE a gate from measured counts.  The emitted string is
compared for COMPLETE STRING EQUALITY against an INDEPENDENT RECONSTRUCTION
built from the receipt object alone; rebuild_verdict_from_receipt() shares no
code and no input with build_verdict(), and five injection mutants prove the
comparator fires (RUNBOOK section 14 addenda, v14 #10 and v14 #20).

CLI CONTRACT (confirmed in code before invocation, v13 #238):
  (no arguments)     THE PLAIN DELIVERY RUN.  Runs every gate, derives the
                     verdict, WRITES v14/code/cra_accumulation_output.txt and
                     v14/code/cra_accumulation_receipt.json.  Exit 0.  Any gate
                     failure aborts BEFORE any artifact is written.
  --mutant NAME      Runs the delivery pipeline with the named injection
                     active.  MUST exit 1 with a NAMED gate failure and MUST
                     NOT write any artifact.  Unknown name -> exit 2.
  --list-mutants     Prints the declared mutant names, one per line.  Exit 0.
  --selftest         THE FALSIFICATION SELFTEST.  Re-invokes this file as a
                     subprocess once per declared mutant, requires exit 1, a
                     death certificate naming a gate, and byte-unchanged
                     artifacts on disk.  Writes NO artifacts itself.

Arithmetic is exact throughout: int and fractions.Fraction only.  A float
literal, a float call, a banned module or a true-division operator anywhere in
this source is a gate failure (G-FLOATGUARD, an AST scan of this file).

Concurrency note: this unit owns ONLY v14/paper-05-accumulation.md,
v14/code/cra_accumulation_exact.py, v14/code/cra_accumulation_output.txt and
v14/code/cra_accumulation_receipt.json.  It reads v13 receipts, the v13 HA
paper and code, the v14 notes and RUNBOOK.md, and writes nothing else.
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

# ---------------------------------------------------------------------------
# 0.  Paths, the mutation switch, the gate ledger
# ---------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
V14 = os.path.dirname(HERE)
ROOT = os.path.dirname(V14)
SRC = os.path.abspath(__file__)
OUT_TXT = os.path.join(HERE, "cra_accumulation_output.txt")
OUT_JSON = os.path.join(HERE, "cra_accumulation_receipt.json")
PAPER = os.path.join(V14, "paper-05-accumulation.md")

MUTANT = None            # set only from the command line; gates never read it

GATES = []
ANCHORS = []
DISCLOSURES = []
LINES = []


class GateFailure(Exception):
    pass


# The gates that can only be evaluated at WRITE time, after the receipt object
# exists.  Named here so the compliance sweep does not mis-denominate itself;
# deliver() gates that every one of them really ran.
DEFERRED_GATES = ("G-PAPER-NUMBERS-IN-RECEIPT",
                  "G-RENDER-FROM-GATED-OBJECT",
                  "G-VERDICT-STILL-EQUAL-AT-WRITE-TIME",
                  "G-NO-FLOATS-IN-RECEIPT",
                  "G-PROSE-RENDERS-FROM-THE-RECEIPT",
                  "G-BLOCKS-RENDER-FROM-THE-RECEIPT",
                  "G-NEVER-FALSIFIED-CENSUS", "G-FINAL-COUNTS",
                  "G-DEFERRED-GATES-EVALUATED")

# The never-falsified census seeds its denominator with the WHOLE declared
# deferred list above, so the gates that have not yet registered when the
# census is taken are still counted; G-DEFERRED-GATES-EVALUATED proves that
# list is complete, and the census's own gate -- registered last of all --
# re-derives the denominator from the live registry.
#
# The declared cardinality of the never-falsified census: every must-pass gate
# and every anchor that no declared mutant kills.  It is a DECLARED number,
# checked against the live registry by the last gate of the run, so a gate
# added without a falsifier -- or a falsifier dropped -- fails the delivery
# instead of quietly moving the count.
NEVER_FALSIFIED_EXPECTED = 45


def gate(name, statement, ok, value=None, must_pass=True):
    """Register a gate.  A gate predicate NEVER references mutant identity
    (RUNBOOK section 14 addendum, v13 #208)."""
    GATES.append({"name": name, "statement": statement, "passed": bool(ok),
                  "must_pass": bool(must_pass), "value": value})
    if must_pass and not ok:
        raise GateFailure("GATE FAILED: %s -- %s | value=%r"
                          % (name, statement, value))
    return bool(ok)


def anchor(name, quantity, expected, measured, source):
    ok = (expected == measured)
    ANCHORS.append({"name": name, "quantity": quantity, "expected": expected,
                    "measured": measured, "ok": ok, "source": source})
    if not ok:
        raise GateFailure("ANCHOR FAILED: %s -- %s | expected=%r measured=%r"
                          % (name, quantity, expected, measured))
    return True


def disclose(did, statement, detail=None):
    DISCLOSURES.append({"id": did, "statement": statement, "detail": detail})


def say(s=""):
    LINES.append(s)


def progress(s):
    sys.stderr.write("  .. %s\n" % s)
    sys.stderr.flush()


def sha256_full(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def sha12(path):
    return sha256_full(path)[:12]


def divf(a, b):
    """Exact division.  Written without the '/' operator so the float guard
    needs no exemption for its own arithmetic."""
    return Fr(a).__truediv__(Fr(b))


# ---------------------------------------------------------------------------
# 1.  G-FLOATGUARD -- exact arithmetic enforced by an AST scan of this source
# ---------------------------------------------------------------------------

FLOAT_T = type((1).__truediv__(1))
BANNED_NAMES = ("float", "math", "random", "numpy", "statistics", "decimal",
                "complex")


def float_guard():
    with open(SRC, "r") as fh:
        tree = ast.parse(fh.read())
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, FLOAT_T):
            bad.append(("float-literal", node.lineno))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            bad.append(("true-division", node.lineno))
        if isinstance(node, ast.Name) and node.id in BANNED_NAMES:
            bad.append(("banned-name:" + node.id, node.lineno))
        if isinstance(node, ast.Attribute) and node.attr in BANNED_NAMES:
            bad.append(("banned-attr:" + node.attr, node.lineno))
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mod = getattr(node, "module", None) or ""
            for nm in [mod] + [a.name for a in node.names]:
                if nm.split(".")[0] in BANNED_NAMES:
                    bad.append(("banned-import:" + nm, node.lineno))
    if MUTANT == "float-leak":
        bad.append(("injected-float", 0))
    return bad


def mutant_blindness_scan():
    """No gate-registering function may read run-mode identity.  Validated by
    four synthetic injections, one per channel, each of which it must flag."""
    with open(SRC, "r") as fh:
        text = fh.read()
    tree = ast.parse(text)
    offences = []
    channels = {"MUTANT", "DELIVERY_RUN", "argv"}

    def reads_mode(fn):
        found = set()
        for node in ast.walk(fn):
            if isinstance(node, ast.Name) and node.id in channels:
                found.add(node.id)
            if isinstance(node, ast.Attribute) and node.attr in channels:
                found.add(node.attr)
        return found

    def registers_gate(fn):
        for node in ast.walk(fn):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                    and node.func.id in ("gate", "anchor"):
                return True
        return False

    for fn in [n for n in ast.walk(tree)
               if isinstance(n, ast.FunctionDef)]:
        if fn.name in ("gate", "anchor"):
            continue
        if registers_gate(fn):
            hit = reads_mode(fn)
            if hit:
                offences.append((fn.name, sorted(hit)))
    # four synthetic injections the scanner MUST flag
    synth = [
        "def f():\n    if MUTANT == 'x':\n        pass\n    gate('a','b',True)\n",
        "def f():\n    if DELIVERY_RUN:\n        pass\n    gate('a','b',True)\n",
        "def f():\n    v = sys.argv\n    gate('a','b',True)\n",
        "def f():\n    anchor('a','b',1,1,'s')\n    return MUTANT\n",
    ]
    caught = 0
    for s in synth:
        t2 = ast.parse(s)
        for fn in [n for n in ast.walk(t2) if isinstance(n, ast.FunctionDef)]:
            if registers_gate(fn) and reads_mode(fn):
                caught += 1
    return offences, caught, len(synth)


# ---------------------------------------------------------------------------
# 2.  The pinned sources -- file-hash anchors and path-value anchors
# ---------------------------------------------------------------------------

SRC_ROWS = [
    ("A-PIN-CRA", "v14/note-cr-batch-pins.md", "1cfee4fc0891",
     "this unit's pin, frozen at v14 ledger #30"),
    ("A-I7-RECEIPT", "v13/code/ha_successor_receipt.json", "542b8735daf0",
     "R0 row I7 -- gravity's record layer: the arena, the record family, the "
     "lapse family, the closure census"),
    ("A-HA-PAPER", "v13/paper-ha-successor.md", "f286ba10d2d9",
     "the HA paper: the GW1 permitted list, the definitions, the frozen "
     "geometry sector"),
    ("A-HA-CODE", "v13/code/ha_successor_exact.py", "d44cb72f8ee9",
     "the HA instrument: the declared record/lapse constructions, read as a "
     "reference and never imported"),
    ("A-R0-PIN", "v14/note-r0-founding-pin.md", "e9d2bedff244",
     "the v14 founding pin -- the I7 row's provenance"),
]

# PATH-VALUE ANCHORS: the (path, value) pair, not the file bytes.
PATH_ROWS = [
    ("P-I7-D", ("declarations", "d"), 2,
     "the spatial dimension of the primary arena"),
    ("P-I7-L", ("declarations", "L"), 3, "sites per direction"),
    ("P-I7-LINKS", ("declarations", "links_d2"), [[1, 0], [0, 1], [1, 1]],
     "the declared link set: the d axis links and the one positive diagonal"),
    ("P-I7-WEIGHT", ("declarations", "density_weight"), 0,
     "the declared density weight w = 0 -- every closure statement is at w=0"),
    ("P-I7-RECORDS", ("declarations", "records_d2"),
     {"G-ANISO": [1, 4, 5], "G-ANISO2": [4, 9, 13], "G-DIAG2": [2, 2, 4],
      "G-FLAT": [1, 1, 2], "G-INDEF": [1, 1, 6], "G-OFFDIAG": [2, 2, 6],
      "G-OFFDIAG2": [3, 5, 12], "G-OFFNEG": [3, 5, 4],
      "G-SINGULAR": [1, 1, 4]},
     "the declared homogeneous record family, counts (n_e1, n_e2, n_diag)"),
    ("P-I7-LAPSE", ("declarations", "lapse_family"),
     "the |X| site deltas, the constant profile 1, and the d chart ramps",
     "the declared lapse family, rebuilt here from this sentence"),
    ("P-I7-RULES", ("declarations", "transported_rules"),
     ["A-chart", "A-axis", "A-linkframe", "A-linkhalf", "A-insert",
      "A-insert-x", "A-insert-2x"],
     "the transported architecture-A drag rules"),
    ("P-I7-RANK", ("tables", "identifiability_rank", "(0, 0)"), 2,
     "the lapse-pair rank at the detector site -- full"),
    ("P-I7-REENCODE", ("tables", "readout_reencoding"),
     {"determinant": "2", "sites_verified": 81},
     "record-IS-metric: the counts->q map is linear with determinant 2 and "
     "reproduces every declared link count at 81 of 81 sites"),
    ("P-I7-LATTICE", ("tables", "link_locality_lattice"),
     {"admissible_points": 361, "pairs_sharing_n_diag_diff_I12": 5100,
      "pairs_sharing_n_e1_n_diag_diff_I11": 781},
     "the link-locality count lattice"),
    ("P-I7-SECTOR-NOTRANSPORT",
     ("tables", "sector_law", "A-notransport|G-FLAT"),
     {"Lambda_equals_I_sites": 9, "residual_zero_sites": 0, "sites": 9},
     "insertion alone does not buy closure -- the frozen-front row"),
]

# The pinned CLAUSES.  Each is quoted VERBATIM from a pinned source and the
# quote is gate-verified against the file on disk; each carries the constraint
# it places on a geometry-record-advancing move.
CLAUSE_ROWS = [
    ("C-TYPE", "v13/paper-ha-successor.md",
     "the interval cardinality $n_\\ell(x)\\in\\mathbb Z_{>0}$",
     "TYPE", "s' must remain a positive integer count at every site and link"),
    ("C-ADMISSIBLE", "v13/paper-ha-successor.md",
     "A record is **admissible** when $q$ is\nnonsingular and positive "
     "definite at every site",
     "ADMISSIBLE", "q(s') must be nonsingular and positive definite"),
    ("C-PERMITTED", "v13/paper-ha-successor.md",
     "GW1 §1.2 permits event counts and record adjacency explicitly.",
     "EXPRESSIBLE", "the atoms must be event counts or record adjacency"),
    ("C-INGREDIENTS", "v13/paper-ha-successor.md",
     "The drag has exactly two ingredients: the **front tilt** $n(x+e)-n(x)$, "
     "a\ndifference of committed division-event counts, and the **eventwise "
     "lapse value**\n$N(x)$.",
     "EXPRESSIBLE", "the two ingredients the pinned dynamics itself uses"),
    ("C-CHART", "v13/paper-ha-successor.md",
     "Equivariance of the residual field is measured over the **whole** group",
     "EQUIVARIANT", "the move must be equivariant for the declared chart "
     "group"),
    ("C-FROZEN", "v13/paper-ha-successor.md",
     "**The geometry sector is frozen under $H_a[N]$.**  The "
     "interval-cardinality\n   record $s$ is a configuration variable that "
     "$H_a[N]$ does not move; only the\n   front does.",
     "FROZEN", "the ONLY pinned statement about s-evolution: the move is the "
     "identity"),
    ("C-NOLAW", "v13/paper-ha-successor.md",
     "**No geometry-update law is constructed**",
     "MISSING", "the missing object, named by the pinned source itself"),
    ("C-OPEN", "v13/paper-ha-successor.md",
     "a geometry-update law, and hence anything bearing on v4 paper 7 Theorem\n"
     "6.1",
     "MISSING", "the same object, carried in the pinned source's OPENS"),
]

# The five 2026-08-09 RUNBOOK engravings, quoted verbatim and gate-verified.
ENGRAVING_ROWS = [
    ("E-REPAIR-PROPAGATION",
     "parallel-built units inherit repairs"),
    ("E-BOUNDARY-PARITY",
     "Boolean-connective boundaries in incidence/complex\nconstructions carry "
     "a parity-witness gate"),
    ("E-PRECHECK",
     "A precheck-level quantity may gate\nwhich candidates are censused, but "
     "may never by itself name\nthe verdict."),
    ("E-CONTAINMENT",
     "a verdict gate compares the complete emitted\nstring for equality "
     "against a string rebuilt segment-by-\nsegment from the measured "
     "values"),
    ("E-RENDER",
     "the object the gates check must be the\nobject the receipt and paper "
     "render from"),
    ("E-PROSE",
     "every numeric claim in a paper renders from\nthe receipt object or is "
     "explicitly marked derived-in-text at\nits derivation site"),
    ("E-COMPLIANCE",
     "a gate asserting compliance with an\nengraved rule ships with an "
     "injection-falsifier demonstrating\nthe gate can fail"),
    ("E-PATHVALUE",
     "a read-by-path from a pinned artifact anchors\nthe (path, value) pair, "
     "not only the file bytes"),
]


# --- the mutable declaration accessors.  EVERY run-mode branch in this file
# --- lives in one of these helpers; none of them registers a gate or an
# --- anchor, and the AST guard measures that separation (RUNBOOK section 14
# --- addendum, v13 #208; HA's disclosure X03 is the precedent).

def src_rows():
    """[instrument -- mutable] the declared source-hash rows."""
    return SRC_ROWS[1:] if MUTANT == "anchor-skip" else list(SRC_ROWS)


def expected_src_hash(name, exp):
    """[instrument -- mutable]"""
    if MUTANT == "anchor-hash-drift" and name == "A-I7-RECEIPT":
        return "000000000000"
    return exp


def path_for(name, path):
    """[instrument -- mutable]"""
    if MUTANT == "path-drift" and name == "P-I7-RECORDS":
        return ("declarations", "records_d3")
    return path


def clause_rows():
    """[instrument -- mutable]"""
    if MUTANT == "clause-drop":
        return [r for r in CLAUSE_ROWS if r[0] != "C-FROZEN"]
    return list(CLAUSE_ROWS)


def quote_for(cid, quote):
    """[instrument -- mutable]"""
    if MUTANT == "quote-drift" and cid == "C-NOLAW":
        return quote.replace("No geometry-update law", "A geometry-update law")
    return quote


def expressibility_split():
    """[instrument -- mutable] the expressible atoms and the banned ones."""
    if MUTANT == "expressibility-lax":
        return list(ATOM_TABLE), []
    return ([r for r in ATOM_TABLE if r[3]],
            [r for r in ATOM_TABLE if not r[3]])


def selector_rows(rows):
    """[instrument -- mutable]"""
    return rows[:-1] if MUTANT == "selector-drop" else list(rows)


def movers_tested():
    """[instrument -- mutable]"""
    return MOVERS[:-1] if MUTANT == "mover-drop" else list(MOVERS)


def schedules_tested():
    """[instrument -- mutable]"""
    return SCHEDULES[:-1] if MUTANT == "schedule-drop" else list(SCHEDULES)


def normalizer(kind, Ef, Ei):
    """[instrument -- mutable] the declared per-accumulated-event denominator.
    NORM-FRONT counts division events committed at sites; NORM-INT counts
    division events written into intervals."""
    if MUTANT == "norm-collapse":
        return Ef
    return Ef if kind == "NORM-FRONT" else Ei


def compliance_rows(rows):
    """[instrument -- mutable]"""
    if MUTANT == "compliance-fake":
        return rows + [("a rule this run never gated", "G-NOT-A-GATE")]
    return list(rows)


def heads_from(builder, payloads):
    """[instrument -- mutable] the three synthetic payloads' heads."""
    if MUTANT == "head-constant":
        return [builder(payloads[0])[0]] * len(payloads)
    return [builder(p)[0] for p in payloads]


def clause_is_binding(kind):
    """[instrument -- mutable] whether a clause of this kind constrains the
    geometry move."""
    if MUTANT == "frozen-clause-inert":
        return False
    return kind == "FROZEN"


def motivated_count(class_i):
    """[instrument -- mutable] the number of movers whose every freedom is
    class-(i) or class-(ii)."""
    return 1 if MUTANT == "motivated-inject" else class_i


def blind_witness_of(cands):
    """[instrument -- mutable]"""
    if MUTANT == "blind-witness-suppress" or not cands:
        return None
    best = max(cands, key=lambda z: (z[0], [-ord(ch) for ch in
                                            "".join(z[1])]))
    return (best[1], best[2])


def orbit_dedup(key):
    """[instrument -- mutable] the s-coordinate the orbit instrument records."""
    if MUTANT == "orbit-blind":
        return "CONSTANT"
    return key


def readout_counts(cnt):
    """[instrument -- mutable] the declared link counts entering the readout."""
    if MUTANT == "readout-perturb":
        return {lk: cnt[lk] + (1 if lk == LINKS[2] else 0) for lk in cnt}
    return cnt


def read_link_table():
    """[instrument -- mutable] each drag rule's read-link set: the links whose
    interval count its weight actually consults."""
    if MUTANT == "readlink-hide":
        return {k: v for k, v in READ_LINKS.items() if k != "A-axis"}
    return dict(READ_LINKS)


def chart_act(pc):
    """[instrument -- mutable] The declared chart group's direction
    relabelling e_1 <-> e_2 permutes the two axis coefficient blocks and fixes
    the diagonal block."""
    if MUTANT == "chart-lax":
        return pc
    return (pc[1], pc[0], pc[2])


def block_text(bid, txt):
    """[instrument -- mutable] the rendered result BLOCKS (the verdict, the
    static-geometry theorem, the section 15 historical sentence).  Unlike the
    single-line prose sentences these are matched under the #125
    normalisation, so the paper may wrap them."""
    if MUTANT == "block-drift" and bid == "THEOREM":
        return txt.replace("Then NO admissible", "Then SOME admissible")
    return txt


def separated_route2(n):
    """[instrument -- mutable] the second route to the separated-pair count of
    a discriminator coordinate: 36 minus the collisions inside each group of
    equal readouts."""
    return n + 1 if MUTANT == "discriminator-census-fake" else n


def hex_schedule_census(dec):
    """[instrument -- mutable] mover -> the set of declared schedules at which
    the mover-blind rescaled limit is reached."""
    if MUTANT == "schedule-census-fake":
        return {k: set(SCHEDULES) for k in dec}
    return {k: set(v) for k, v in dec.items()}


def uniform_increment_rows(rows):
    """[instrument -- mutable] one row per mover reaching the blind limit,
    carrying its SCH-CONST increments."""
    return rows[:-1] if MUTANT == "uniform-increment-drop" else list(rows)


def tilt_net_total(v):
    """[instrument -- mutable] the net of a mover's writes over a cell."""
    return v + 1 if MUTANT == "tilt-net-fake" else v


def weld_scale(k):
    """[instrument -- mutable] |X| * |L|, the declared normalisation under
    which the accumulation limit is read."""
    return k - 1 if MUTANT == "unit-record-scale-drift" else k


NUMBER_TOKEN = r"(?<![\w/.-])\d+(?:/\d+)?(?![\w.-])"
MD_PREFIX = re.compile(r"^\s*(?:>+\s*|[-*+]\s+|\d+\.\s+)+")


def norm125(txt):
    """The RUNBOOK section 14 #125 normalisation, applied to BOTH sides of a
    text gate: markdown blockquote / list prefixes stripped line by line, the
    inline-code marker stripped, then every whitespace run collapsed to one
    space.  Nothing else is touched -- emphasis markers, math delimiters and
    every character of the claim itself must match as written."""
    return " ".join(" ".join(MD_PREFIX.sub("", ln).replace("`", "")
                             for ln in txt.split("\n")).split())


def paper_number_tokens(txt):
    """[instrument -- mutable] every numeric token of the paper."""
    toks = re.findall(NUMBER_TOKEN, txt)
    if MUTANT == "paper-number-inject":
        toks.append("31337")
    return toks


def receipt_number_set(R):
    """Every numeric token the receipt object carries, at any depth, including
    numbers embedded inside its strings."""
    out = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(k)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        else:
            t = str(o)
            out.add(t)
            for m in re.findall(r"\d+(?:/\d+)?", t):
                out.add(m)
    walk(R)
    return out


def post_gate_injection(R):
    """[instrument -- mutable] injections that live in the RENDERED object,
    after every gate has run -- the v14 #10 INJ_D class."""
    if MUTANT == "traj-corrupt":
        R["tables"]["trajectory_summary"]["converges"] += 1
    if MUTANT == "limit-typed":
        R["tables"]["trajectory_summary"]["limit_classes"][0]["limit"] = \
            ["0", "0", "0"]
        R["tables"]["trajectory_summary"]["distinct_limit_classes"] += 1
    return R


def read_json(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return json.load(fh)


def read_text(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return fh.read()


def dig(obj, path):
    for k in path:
        obj = obj[k]
    return obj


# ---------------------------------------------------------------------------
# 3.  The arena -- rebuilt from the pinned declarations
# ---------------------------------------------------------------------------

D = 2
LL = 3
LINKS = [(1, 0), (0, 1), (1, 1)]
SITES = [tuple(t) for t in itertools.product(range(LL), repeat=D)]


def shift(x, e):
    return tuple((x[i] + e[i]) % LL for i in range(D))


def build_lapse_family():
    """The pinned lapse sentence, rebuilt: |X| site deltas, the constant
    profile 1, the d chart ramps."""
    lp = [("delta%d%d" % x, {y: (1 if y == x else 0) for y in SITES})
          for x in SITES]
    lp.append(("one", {y: 1 for y in SITES}))
    lp += [("ramp%d" % j, {y: y[j] for y in SITES}) for j in range(D)]
    if MUTANT == "lapse-drop":
        lp = lp[:-1]
    return lp


def hom_record(tup):
    return {x: {lk: tup[i] for i, lk in enumerate(LINKS)} for x in SITES}


def curved_record():
    """HA's declared inhomogeneous DIAGONAL record: q(x) = diag(1+x_1,...)."""
    return {x: {lk: sum((1 + x[j]) for j in range(D) if lk[j])
                for lk in LINKS} for x in SITES}


def curvoff_record():
    """HA's declared inhomogeneous CROSS-TERM record."""
    out = {}
    for x in SITES:
        b = [2 + x[j] for j in range(D)]
        cross = 1 + (x[0] * x[1]) % 2
        out[x] = {lk: (sum(b[j] for j in range(D) if lk[j])
                       + 2 * cross * sum(1 for i in range(D)
                                         for j in range(i + 1, D)
                                         if lk[i] and lk[j]))
                  for lk in LINKS}
    return out


def build_records(decl_records):
    recs = {}
    for nm, tup in sorted(decl_records.items()):
        recs[nm] = hom_record(tuple(tup))
    recs["G-CURVED"] = curved_record()
    recs["G-CURVOFF"] = curvoff_record()
    return recs


def qmat(cnt):
    """The declared readout: interval cardinality as squared separation.
    q_ij e^i_l e^j_l = n_l.  At d=2 the three links determine the three
    components exactly."""
    c = readout_counts(cnt)
    n1, n2, nd = c[LINKS[0]], c[LINKS[1]], c[LINKS[2]]
    q12 = Fr(nd - n1 - n2, 2)
    return [[Fr(n1), q12], [q12, Fr(n2)]]


def qdet(q):
    return q[0][0] * q[1][1] - q[0][1] * q[1][0]


def qinv(q):
    det = qdet(q)
    if det == 0:
        return None
    return [[divf(q[1][1], det), divf(-q[0][1], det)],
            [divf(-q[1][0], det), divf(q[0][0], det)]]


def posdef(q):
    return q[0][0] > 0 and qdet(q) > 0


def admissible(rec):
    """A record is admissible when q is nonsingular and positive definite at
    every site, by the exact Sylvester criterion (positive definiteness at
    d = 2 already gives det > 0, hence nonsingularity and an exact inverse)."""
    for x in SITES:
        if not posdef(qmat(rec[x])):
            return False
    return True


# ---------------------------------------------------------------------------
# 4.  The drag rules and H_a[N] on the TRIPLE state (s, n, m)
# ---------------------------------------------------------------------------

_LAM_CACHE = {}
_CACHE = {"hits": 0, "misses": 0, "bypass": 0}


def lambda_of(rule, recname, rec, x, fresh=False):
    """The drag rule's weight at site x.  [instrument -- mutable cache path]"""
    key_name = recname.split("@")[0] if MUTANT == "cache-alias" else recname
    key = (rule, key_name, x)
    use_cache = (not fresh) or (MUTANT == "cache-lax")
    if fresh and MUTANT != "cache-lax":
        _CACHE["bypass"] += 1
    if use_cache and key in _LAM_CACHE:
        _CACHE["hits"] += 1
        return _LAM_CACHE[key]
    if use_cache:
        _CACHE["misses"] += 1
    cnt = rec[x]
    n1, n2, nd = cnt[LINKS[0]], cnt[LINKS[1]], cnt[LINKS[2]]
    q = qmat(cnt)
    inv = qinv(q)
    if rule == "A-chart":
        M = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    elif rule == "A-axis":
        M = [[Fr(1, n1), Fr(0)], [Fr(0), Fr(1, n2)]]
    elif rule in ("A-linkframe", "A-linkhalf"):
        M = [[Fr(0), Fr(0)], [Fr(0), Fr(0)]]
        for lk, c in ((LINKS[0], n1), (LINKS[1], n2), (LINKS[2], nd)):
            for i in range(D):
                for j in range(D):
                    M[i][j] += Fr(lk[i] * lk[j], c)
        if rule == "A-linkhalf":
            M = [[divf(v, 2) for v in row] for row in M]
    elif rule in ("A-insert", "A-notransport"):
        M = [row[:] for row in inv]
    elif rule == "A-insert-x":
        M = [[(-v if i != j else v) for j, v in enumerate(row)]
             for i, row in enumerate(inv)]
    elif rule == "A-insert-2x":
        M = [[2 * v for v in row] for row in inv]
    elif rule == "B-axis":
        M = {LINKS[0]: Fr(1, n1), LINKS[1]: Fr(1, n2), LINKS[2]: Fr(0)}
    elif rule == "B-all":
        M = {LINKS[0]: Fr(1, n1), LINKS[1]: Fr(1, n2), LINKS[2]: Fr(1, nd)}
    elif rule == "B-chart":
        M = {LINKS[0]: Fr(1), LINKS[1]: Fr(1), LINKS[2]: Fr(0)}
    else:
        raise RuntimeError("unknown rule " + rule)
    if use_cache:
        _LAM_CACHE[key] = M
    return M


ARCH_B = ("B-axis", "B-all", "B-chart")


def drag(rule, recname, rec, N, n):
    """w[N,n] -- the record-native drag field, HA section 3.3, both
    architectures."""
    out = {}
    for x in SITES:
        Lam = lambda_of(rule, recname, rec, x)
        if rule in ARCH_B:
            v = [Fr(0)] * D
            for lk in LINKS:
                if Lam[lk] == 0:
                    continue
                dl = Fr(n[shift(x, lk)] - n[x])
                for i in range(D):
                    if lk[i]:
                        v[i] += Lam[lk] * Fr(lk[i]) * dl
            out[x] = tuple(Fr(N[x]) * v[i] for i in range(D))
        else:
            dn = [Fr(n[shift(x, LINKS[j])] - n[x]) for j in range(D)]
            out[x] = tuple(sum((Lam[i][j] * dn[j] for j in range(D)), Fr(0))
                           * Fr(N[x]) for i in range(D))
    return out


def H_forward(rule, recname, rec, N, state):
    """H_a[N](s, n, m) = (s, n+N, m+w[N,n]).  The geometry sector s is passed
    through UNTOUCHED: that is the pinned definition, and section A measures
    it rather than asserting it."""
    s, n, m = state
    w = drag(rule, recname, rec, N, n)
    s2 = s
    if MUTANT == "s-writes":
        s2 = {x: {lk: s[x][lk] + N[x] for lk in LINKS} for x in SITES}
    n2 = {x: n[x] + N[x] for x in SITES}
    m2 = {x: tuple(m[x][i] + w[x][i] for i in range(D)) for x in SITES}
    return (s2, n2, m2)


def H_inverse(rule, recname, rec, N, state):
    s, n, m = state
    n2 = {x: n[x] - N[x] for x in SITES}
    w = drag(rule, recname, rec, N, n2)
    m2 = {x: tuple(m[x][i] - w[x][i] for i in range(D)) for x in SITES}
    s2 = s
    if MUTANT == "s-writes":
        s2 = {x: {lk: s[x][lk] - N[x] for lk in LINKS} for x in SITES}
    return (s2, n2, m2)


def D_forward(v, state):
    """D_a[v] in the declared D-REG realisation: the address register shifts,
    the geometry front is not transported."""
    s, n, m = state
    return (s, n, {x: tuple(m[x][i] + v[x][i] for i in range(D))
                   for x in SITES})


def s_key(s):
    return tuple(tuple(s[x][lk] for lk in LINKS) for x in SITES)


def rec_tag(recname, rec):
    """A memo name that is determined by the record's CONTENTS, so two
    different derived records can never share a memo entry.  The cache-alias
    falsifier strips everything after the '@' and therefore serves a derived
    record the base record's cached weight."""
    return "%s@%s" % (recname, hashlib.sha256(
        repr(s_key(rec)).encode()).hexdigest()[:12])


# ---------------------------------------------------------------------------
# 5.  The advancing-move design space -- atoms, expressibility, candidates
# ---------------------------------------------------------------------------

ATOM_TABLE = [
    # (family, symbol, prose, expressible, the pinned clause that licenses it)
    ("LIN", "U", "1 -- the declared link exists (record adjacency)",
     True, "C-PERMITTED"),
    ("LIN", "NS", "N(x) -- the eventwise lapse value at the source endpoint",
     True, "C-INGREDIENTS"),
    ("LIN", "NT", "N(x+l) -- the eventwise lapse value at the target endpoint",
     True, "C-INGREDIENTS"),
    ("LIN", "FS", "n(x) -- division events committed at the source site",
     True, "C-PERMITTED"),
    ("LIN", "FT", "n(x+l) -- division events committed at the target site",
     True, "C-PERMITTED"),
    ("LIN", "IC", "n_l(x) -- division events in the record interval",
     True, "C-PERMITTED"),
    ("BIL", "NS*FS", "N(x) n(x)", True, "C-INGREDIENTS"),
    ("BIL", "NS*FT", "N(x) n(x+l)", True, "C-INGREDIENTS"),
    ("BIL", "NS*IC", "N(x) n_l(x)", True, "C-INGREDIENTS"),
    ("BIL", "NT*FS", "N(x+l) n(x)", True, "C-INGREDIENTS"),
    ("BIL", "NT*FT", "N(x+l) n(x+l)", True, "C-INGREDIENTS"),
    ("BIL", "NT*IC", "N(x+l) n_l(x)", True, "C-INGREDIENTS"),
    # THE EXPRESSIBILITY NEGATIVE CONTROL: a held-out chart label.  GW1 1.2's
    # second bullet bans held-out embedding coordinates and planted frames.
    ("BANNED", "SIDX", "the site's index in the declared enumeration -- a "
     "held-out chart label, on no permitted list", False, None),
]

ATOMS = {"LIN": [r[1] for r in ATOM_TABLE if r[0] == "LIN"],
         "BIL": [r[1] for r in ATOM_TABLE if r[0] == "BIL"]}
NA = 6
BOX = (-1, 0, 1, 2)


def atomvec(fam, x, lk, N, n, s):
    ns, nt = N[x], N[shift(x, lk)]
    fs, ft = n[x], n[shift(x, lk)]
    ic = s[x][lk]
    if fam == "LIN":
        return (1, ns, nt, fs, ft, ic)
    return (ns * fs, ns * ft, ns * ic, nt * fs, nt * ft, nt * ic)


def dot(c, a):
    return (c[0] * a[0] + c[1] * a[1] + c[2] * a[2]
            + c[3] * a[3] + c[4] * a[4] + c[5] * a[5])


# The declared probe fronts: the census is evaluated at these fronts, at every
# declared record and every declared lapse profile.
def probe_fronts():
    return [("n-zero", {x: 0 for x in SITES}),
            ("n-ramp", {x: x[0] for x in SITES}),
            ("n-site", {x: (1 if x == (0, 0) else 0) for x in SITES}),
            ("n-const", {x: 1 for x in SITES})]


def probe_cells(fam, recs, lapses, fronts):
    """The deduplicated site-level probe cells: for each (record, lapse,
    front, site) the three link atom vectors and the three base counts.
    [instrument -- mutable]"""
    out = set()
    for rn in sorted(recs):
        s = recs[rn]
        for ln, N in lapses:
            for fn, n in fronts:
                for x in SITES:
                    out.add((tuple(atomvec(fam, x, lk, N, n, s)
                                   for lk in LINKS),
                             tuple(s[x][lk] for lk in LINKS)))
    out = sorted(out)
    if MUTANT == "census-cell-drop":
        out = out[1:]
    return out


def probe_cells_route2(fam, recs, lapses, fronts):
    """An INDEPENDENT enumeration of the same cell set, built by iterating the
    product in a different order through an accumulating dict rather than a
    set of tuples.  It is NOT mutated, so a silently dropped cell shows up as
    a set difference (RUNBOOK section 13 addendum, v13 #234: a
    cell-completeness gate must catch a dropped cell)."""
    acc = {}
    for x in SITES:
        for fn, n in fronts:
            for ln, N in lapses:
                for rn in sorted(recs):
                    s = recs[rn]
                    key = (tuple(atomvec(fam, x, lk, N, n, s) for lk in LINKS),
                           tuple(s[x][lk] for lk in LINKS))
                    acc[key] = acc.get(key, 0) + 1
    return sorted(acc), sum(acc.values())


ADM_STEPS = (1, 2, 3)


def run_census(fam, cells):
    """The advancing-move census.  Filters, in order: ADVANCING (delta >= 0
    everywhere and > 0 somewhere) and ADMISSIBLE (the k-fold frozen-probe
    record stays positive definite for k = 1,2,3)."""
    avs = sorted(set(a for (av, b) in cells for a in av))
    adv, adm = [], []
    for c in itertools.product(BOX, repeat=NA):
        neg = False
        pos = False
        for a in avs:
            v = dot(c, a)
            if v < 0:
                neg = True
                break
            if v > 0:
                pos = True
        if neg or not pos:
            continue
        adv.append(c)
        good = True
        for (av, b) in cells:
            ds = [dot(c, a) for a in av]
            u = ds[2] - ds[0] - ds[1]
            v0 = b[2] - b[0] - b[1]
            for k in (3, 1, 2):
                A = b[0] + k * ds[0]
                B = b[1] + k * ds[1]
                Q = v0 + k * u
                if A <= 0 or B <= 0 or 4 * A * B - Q * Q <= 0:
                    good = False
                    break
            if not good:
                break
        if good:
            adm.append(c)
    return adv, adm


def run_census_route2(fam, cells):
    """An INDEPENDENT recomputation of the two census counts.  It does not
    call run_census, does not share its short-circuit structure, and builds
    its own predicate from the record readout rather than from the algebraic
    determinant expression (RUNBOOK section 14 addendum, v13 #219)."""
    nadv = 0
    nadm = 0
    for c in itertools.product(BOX, repeat=NA):
        deltas = []
        for (av, b) in cells:
            deltas.append(([dot(c, a) for a in av], b))
        if any(v < 0 for (ds, b) in deltas for v in ds):
            continue
        if not any(v > 0 for (ds, b) in deltas for v in ds):
            continue
        nadv += 1
        ok = True
        for (ds, b) in deltas:
            for k in ADM_STEPS:
                cnt = {LINKS[i]: b[i] + k * ds[i] for i in range(3)}
                if any(cnt[lk] <= 0 for lk in LINKS):
                    ok = False
                    break
                if not posdef(qmat(cnt)):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            nadm += 1
    if MUTANT == "fiber-corrupt":
        nadm += 1
    return nadv, nadm


# ---------------------------------------------------------------------------
# 6.  The named movers, the schedules, the trajectories
# ---------------------------------------------------------------------------

MOVERS = [
    ("M-NONE", "LIN", (0, 0, 0, 0, 0, 0),
     "the pinned forced move: delta = 0, the frozen reduction"),
    ("M-CLOSED", "LIN", (0, 1, 1, 0, 0, 0),
     "closed-interval transfer: an event at either endpoint is IN the "
     "interval"),
    ("M-SOURCE", "LIN", (0, 1, 0, 0, 0, 0),
     "half-open transfer [x, x+l): the source endpoint only"),
    ("M-TARGET", "LIN", (0, 0, 1, 0, 0, 0),
     "half-open transfer (x, x+l]: the target endpoint only"),
    ("M-FRONT", "LIN", (0, 0, 0, 1, 0, 0),
     "front-value transfer: the interval gains the source site's whole "
     "committed count"),
    ("M-TILT", "LIN", (0, 0, 0, -1, 1, 0),
     "front-tilt transfer: HA's own drag ingredient used as a geometry "
     "writer"),
    ("M-DILATE", "LIN", (0, 0, 0, 0, 0, 1),
     "record dilation: every interval count grows by its own value"),
    ("M-LAPDIL", "BIL", (0, 0, 1, 0, 0, 0),
     "lapse-driven dilation: N(x) n_l(x)"),
    ("M-FIAT", "LIN", (1, 0, 0, 0, 0, 0),
     "THE FOREIGN CONTROL: +1 into every interval count per step, by fiat"),
]

SCHEDULES = ["SCH-CONST", "SCH-RAMP0", "SCH-RAMP1", "SCH-DELTA-FIX",
             "SCH-DELTA-CYC", "SCH-MIX"]
T_MAX = 20
NORMS = ["NORM-FRONT", "NORM-INT"]


def schedule_of(name, lapses, T):
    LD = dict(lapses)
    if name == "SCH-CONST":
        return [LD["one"]] * T
    if name == "SCH-RAMP0":
        return [LD["ramp0"]] * T
    if name == "SCH-RAMP1":
        return [LD["ramp1"]] * T
    if name == "SCH-DELTA-FIX":
        return [LD["delta00"]] * T
    if name == "SCH-DELTA-CYC":
        return [LD["delta%d%d" % SITES[t % len(SITES)]] for t in range(T)]
    if name == "SCH-MIX":
        return [LD["one"] if t % 2 == 0 else LD["ramp0"] for t in range(T)]
    raise RuntimeError("unknown schedule " + name)


def trajectory(fam, c, schedname, rec, lapses, T=T_MAX):
    """One accumulation trajectory: at each step the front advances by N_t and
    the geometry record advances by delta[N_t, n, s].  Exact integers."""
    s = {x: dict(rec[x]) for x in SITES}
    n = {x: 0 for x in SITES}
    Ns = schedule_of(schedname, lapses, T)
    Ef = 0
    Ei = 0
    rows = []
    for t in range(T):
        N = Ns[t]
        ds = {x: {lk: dot(c, atomvec(fam, x, lk, N, n, s)) for lk in LINKS}
              for x in SITES}
        s = {x: {lk: s[x][lk] + ds[x][lk] for lk in LINKS} for x in SITES}
        n = {x: n[x] + N[x] for x in SITES}
        Ef += sum(N[x] for x in SITES)
        Ei += sum(ds[x][lk] for x in SITES for lk in LINKS)
        rows.append((t + 1, Ef, Ei,
                     {x: dict(s[x]) for x in SITES}))
    return rows


# ---- exact sequence classification ---------------------------------------

MAXDEG = 6
MAXRATIO = 16


def diffs(seq):
    return [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]


def classify_poly(seq):
    """Return (deg, leading coefficient) if seq is a polynomial in t of degree
    <= MAXDEG, certified by a vanishing finite difference with at least three
    window points to spare; else None.  Finite-difference reconstruction is
    exact, so the certificate reproduces EVERY window value."""
    cur = list(seq)
    fact = 1
    for k in range(0, MAXDEG + 1):
        if len(cur) < 3:
            return None
        if all(v == cur[0] for v in cur):
            if k == 0:
                return (0, Fr(cur[0]))
            return (k, divf(Fr(cur[0]), fact))
        cur = diffs(cur)
        fact = fact * (k + 1)
    return None


def classify_expc(seq):
    """Return (r, c, k) if seq(t) = c*r^t + k exactly on the window for an
    integer ratio 2 <= r <= MAXRATIO; else None.  Certified by exact
    reproduction of every window value."""
    if len(seq) < 5:
        return None
    d1 = diffs(seq)
    if any(v == 0 for v in d1):
        return None
    r0 = divf(Fr(d1[1]), Fr(d1[0]))
    if r0.denominator != 1 or r0 < 2 or r0 > MAXRATIO:
        return None
    r = int(r0)
    for i in range(len(d1) - 1):
        if Fr(d1[i + 1]) != r * Fr(d1[i]):
            return None
    # seq(t) = c r^t + k with t = 1.. ; d1[0] = seq(2)-seq(1) = c r (r-1)
    c = divf(Fr(d1[0]), Fr(r * (r - 1)))
    k = Fr(seq[0]) - c * Fr(r)
    for i, v in enumerate(seq):
        if Fr(v) != c * Fr(r ** (i + 1)) + k:
            return None
    return (r, c, k)


def classify_seq(seq):
    p = classify_poly(seq)
    if p is not None:
        return ("POLY", p[0], p[1])
    e = classify_expc(seq)
    if e is not None:
        return ("EXPC", e[0], e[1])
    return ("UNCLASSIFIED", None, None)


def limit_of(numcls, dencls):
    """The exact limit of num(t)/den(t) from the two certified
    classifications."""
    kn, an, bn = numcls
    kd, ad, bd = dencls
    if kn == "UNCLASSIFIED" or kd == "UNCLASSIFIED":
        return ("UNCLASSIFIED", None)
    if bd == 0:
        return ("UNCLASSIFIED", None)
    if kn == "POLY" and kd == "POLY":
        if an < ad:
            return ("LIMIT", Fr(0))
        if an == ad:
            return ("LIMIT", divf(bn, bd))
        return ("DIVERGES", "POLY-DEGREE-%d" % (an - ad))
    if kn == "EXPC" and kd == "EXPC":
        if an != ad:
            return ("DIVERGES", "EXP-RATIO-%d-OVER-%d" % (an, ad)) \
                if an > ad else ("LIMIT", Fr(0))
        if bd == 0:
            return ("UNCLASSIFIED", None)
        return ("LIMIT", divf(bn, bd))
    if kn == "EXPC" and kd == "POLY":
        return ("DIVERGES", "EXPONENTIAL-RATIO-%d" % an)
    if kn == "POLY" and kd == "EXPC":
        return ("LIMIT", Fr(0))
    return ("UNCLASSIFIED", None)


def window_type(seq):
    """The pin's own three-way typing, measured on the window."""
    T = len(seq)
    for t0 in range(T - 4):
        if all(v == seq[t0] for v in seq[t0:]):
            return "EVENTUALLY-CONSTANT"
    for p in range(1, 7):
        for t0 in range(T - 2 * p - 1):
            if all(seq[i + p] == seq[i] for i in range(t0, T - p)):
                return "EVENTUALLY-PERIODIC-%d" % p
    return "NEITHER"


# ---------------------------------------------------------------------------
# 7.  The coupling instrument -- what makes a move FOREIGN
# ---------------------------------------------------------------------------

def coupling_profile(fam, c, recs, lapses):
    """Measured functional dependence of delta on each pinned field.  A move
    blind to all three is FOREIGN: it reads nothing the process carries."""
    fronts = probe_fronts()
    base_rec = recs["G-FLAT"]
    base_N = dict(lapses)["one"]
    base_n = dict(fronts)["n-zero"]

    def vals(varyN=False, varyn=False, varys=False):
        out = set()
        Ns = [N for (nm, N) in lapses] if varyN else [base_N]
        ns = [n for (nm, n) in fronts] if varyn else [base_n]
        ss = [recs[k] for k in sorted(recs)] if varys else [base_rec]
        for N in Ns:
            for n in ns:
                for s in ss:
                    for x in SITES:
                        for lk in LINKS:
                            out.add(dot(c, atomvec(fam, x, lk, N, n, s)))
        return out

    if MUTANT == "foreign-blind":
        return {"N": True, "n": True, "s": True, "blind": False,
                "advancing": True}
    if MUTANT == "coupling-dead":
        return {"N": False, "n": False, "s": False, "blind": True,
                "advancing": True}
    prof = {"N": len(vals(varyN=True)) > 1,
            "n": len(vals(varyn=True)) > 1,
            "s": len(vals(varys=True)) > 1}
    prof["blind"] = not (prof["N"] or prof["n"] or prof["s"])
    # ADVANCING is measured, so the identity move leaves the FOREIGN class by
    # a property and never by its name (RUNBOOK section 14 addendum, v13 #208:
    # no gate predicate may reference a named object's identity).
    allv = vals(varyN=True, varyn=True, varys=True)
    prof["advancing"] = any(v > 0 for v in allv) and \
        not any(v < 0 for v in allv)
    return prof


# ---------------------------------------------------------------------------
# 8.  Selectors -- each declared, each measured, none of them pinned
# ---------------------------------------------------------------------------

READ_LINKS = {
    "A-chart": (), "B-chart": (),
    "A-axis": (0, 1), "B-axis": (0, 1),
    "A-linkframe": (0, 1, 2), "A-linkhalf": (0, 1, 2), "B-all": (0, 1, 2),
    "A-insert": (0, 1, 2), "A-insert-x": (0, 1, 2),
    "A-insert-2x": (0, 1, 2), "A-notransport": (0, 1, 2),
}
FRONT_ATOM_IDX = {"LIN": (3, 4), "BIL": (0, 1, 3, 4)}


def delta_at(fam, c, x, li, N, n, s):
    return dot(c, atomvec(fam, x, LINKS[li], N, n, s))


def sel_zero_on_links(fam, c, links, recnames, recs, lapses, fronts):
    """[instrument -- mutable] does the move leave every link the rule's
    weight reads untouched at every probe cell?"""
    if MUTANT == "commute-lax":
        return True
    for rn in recnames:
        s = recs[rn]
        for ln, N in lapses:
            for fn, n in fronts:
                for x in SITES:
                    for li in links:
                        if delta_at(fam, c, x, li, N, n, s) != 0:
                            return False
    return True


def sel_no_front_dependence(fam, c):
    return all(c[i] == 0 for i in FRONT_ATOM_IDX[fam])


def sel_preserves_diagonal_sector(fam, c, diagnames, recs, lapses, fronts):
    """A-axis / B-axis close exactly on the records whose readout is diagonal.
    The sector survives a move iff delta_diag = delta_1 + delta_2 there."""
    for rn in diagnames:
        s = recs[rn]
        for ln, N in lapses:
            for fn, n in fronts:
                for x in SITES:
                    ds = [delta_at(fam, c, x, i, N, n, s) for i in range(3)]
                    if ds[2] != ds[0] + ds[1]:
                        return False
    return True


def commutation_defect_closed(fam, c, rule, recname, rec, N, n):
    """CLOSED FORM.  Advance-then-write vs write-then-advance:
      s-defect  = delta[N, n+N, s] - delta[N, n, s]
      m-defect  = w[N, n; Lambda(s)] - w[N, n; Lambda(s + delta)]"""
    nadv = {x: n[x] + N[x] for x in SITES}
    ds_a = {x: {lk: dot(c, atomvec(fam, x, lk, N, nadv, rec)) for lk in LINKS}
            for x in SITES}
    ds_b = {x: {lk: dot(c, atomvec(fam, x, lk, N, n, rec)) for lk in LINKS}
            for x in SITES}
    if MUTANT == "closed-form-skew":
        ds_a = {x: {lk: ds_a[x][lk] + 1 for lk in LINKS} for x in SITES}
    sdef = {x: {lk: ds_a[x][lk] - ds_b[x][lk] for lk in LINKS} for x in SITES}
    moved = {x: {lk: rec[x][lk] + ds_b[x][lk] for lk in LINKS} for x in SITES}
    if not admissible(moved):
        return (sdef, None, "MOVED-RECORD-INADMISSIBLE")
    w0 = drag(rule, recname, rec, N, n)
    w1 = drag(rule, rec_tag(recname, moved), moved, N, n)
    mdef = {x: tuple(w0[x][i] - w1[x][i] for i in range(D)) for x in SITES}
    return (sdef, mdef, "OK")


def commutation_defect_literal(fam, c, rule, recname, rec, N, state):
    """LITERAL route: compose the two maps on the triple state, both orders,
    and difference the results.  Shares no code with the closed form."""
    s0, n0, m0 = state

    def G(st):
        s, n, m = st
        ds = {x: {lk: dot(c, atomvec(fam, x, lk, N, n, s)) for lk in LINKS}
              for x in SITES}
        return ({x: {lk: s[x][lk] + ds[x][lk] for lk in LINKS}
                 for x in SITES}, n, m)

    aHG = G(H_forward(rule, recname, rec, N, state))
    gs, gn, gm = G(state)
    gmoved = {x: dict(gs[x]) for x in SITES}
    if not admissible(gmoved):
        return (None, None, "MOVED-RECORD-INADMISSIBLE")
    aGH = H_forward(rule, rec_tag(recname, gmoved), gmoved, N, (gs, gn, gm))
    sdef = {x: {lk: aHG[0][x][lk] - aGH[0][x][lk] for lk in LINKS}
            for x in SITES}
    mdef = {x: tuple(aHG[2][x][i] - aGH[2][x][i] for i in range(D))
            for x in SITES}
    return (sdef, mdef, "OK")


# ---------------------------------------------------------------------------
# 9.  The verdict -- built from the measured payload, rebuilt from the receipt
# ---------------------------------------------------------------------------

def build_verdict(P):
    """Assemble the verdict from the measured payload.  Returns
    (head, segments, full)."""
    if P["motivated"] == 0:
        head = "CRA-BLOCKED-AT-STATIC-GEOMETRY"
    elif P["motivated_all_converge"]:
        head = "CRA-RESCALED-CONVERGES"
    else:
        head = "CRA-DIVERGES"
    segs = []
    segs.append("MISSING=%s" % P["missing"])
    segs.append("EXPRESSIBLE=%d/%d" % (P["expressible"], P["atoms_declared"]))
    segs.append("CENSUS=%d|ADVANCING=%d|ADMISSIBLE=%d"
                % (P["candidates"], P["advancing"], P["admissible"]))
    segs.append("FORCED=%d|FORCED-ADVANCING=%d"
                % (P["forced"], P["forced_advancing"]))
    segs.append("INVENTORY=i:%d,ii:%d,iii:%d"
                % (P["class_i"], P["class_ii"], P["class_iii"]))
    segs.append("SELECTOR-CLOSURE-FIBER=%d" % P["closure_fiber"])
    segs.append("COMMUTING-ADVANCING=%d-AT-%d-OF-%d-RULES"
                % (P["commuting_advancing"], P["count_reading_rules"],
                   P["rules"]))
    segs.append("TRAJ=CONVERGES:%d,DIVERGES:%d,UNDEF:%d,UNCLASSIFIED:%d"
                % (P["tr_conv"], P["tr_div"], P["tr_undef"], P["tr_unc"]))
    segs.append("LIMIT-CLASSES=%d|MOVER-BLIND-LIMIT=%s"
                % (P["limit_classes"], P["blind_limit"]))
    segs.append("NORMALIZATION-FLIPS=%d" % P["norm_flips"])
    segs.append("FOREIGN-FLAGGED=%d/%d" % (P["foreign_flagged"],
                                           P["foreign_declared"]))
    if MUTANT == "verdict-typed-segment":
        segs[6] = "COMMUTING-ADVANCING=7-AT-9-OF-11-RULES"
    if MUTANT == "verdict-append-text":
        segs[0] = segs[0] + "-AND-SUPPLIED-BY-THE-PIN"
    if MUTANT == "verdict-value-swap":
        segs[4] = "INVENTORY=i:%d,ii:%d,iii:%d" % (P["class_iii"],
                                                   P["class_ii"], P["class_i"])
    if MUTANT == "verdict-fully-typed":
        head = "CRA-RESCALED-CONVERGES"
        segs = ["MISSING=NOTHING", "EXPRESSIBLE=13/13", "CENSUS=1|ADVANCING=1"
                "|ADMISSIBLE=1", "FORCED=1|FORCED-ADVANCING=1",
                "INVENTORY=i:1,ii:0,iii:0", "SELECTOR-CLOSURE-FIBER=1",
                "COMMUTING-ADVANCING=1-AT-9-OF-11-RULES",
                "TRAJ=CONVERGES:1,DIVERGES:0,UNDEF:0,UNCLASSIFIED:0",
                "LIMIT-CLASSES=1|MOVER-BLIND-LIMIT=NO",
                "NORMALIZATION-FLIPS=0", "FOREIGN-FLAGGED=1/1"]
    if MUTANT == "verdict-inert-segment":
        segs[9] = "NORMALIZATION-FLIPS=CONSTANT"
    return head, segs, head + "-<" + "; ".join(segs) + ">"


def rebuild_verdict_from_receipt(R):
    """The INDEPENDENT comparator.  It shares no code and no input with
    build_verdict: it reads the RECEIPT OBJECT -- the same object the artifacts
    render from -- and reassembles the string segment by segment.  (RUNBOOK
    section 14 addendum, v14 #10: containment is not equality; v14 #20: a
    compliance gate whose comparator cannot disagree is vacuous.)"""
    t = R["tables"]
    inv = t["choice_inventory"]
    cen = t["census"]
    tr = t["trajectory_summary"]
    # THE HEAD-SELECTING QUANTITY IS DERIVED HERE, NOT RE-READ.  The builder's
    # own copy (choice_inventory/class_i_motivated_movers) is never consulted:
    # a motivated mover is one every freedom of which is class-(i) or
    # class-(ii), so the comparator adds the two separately measured and
    # separately gated components and derives the head from the sum.  A typed
    # or drifted class_i therefore breaks string equality instead of being
    # confirmed by a copy of itself.
    class_i = inv["forced_advancing_movers"] + inv["class_ii_selected"]
    if class_i == 0:
        head = "CRA-BLOCKED-AT-STATIC-GEOMETRY"
    elif tr["motivated_all_converge"]:
        head = "CRA-RESCALED-CONVERGES"
    else:
        head = "CRA-DIVERGES"
    out = []
    out.append("MISSING=" + t["missing_object"]["token"])
    out.append("EXPRESSIBLE=" + str(t["atoms"]["expressible"]) + "/"
               + str(t["atoms"]["declared"]))
    out.append("CENSUS=" + str(cen["candidates"]) + "|ADVANCING="
               + str(cen["advancing"]) + "|ADMISSIBLE="
               + str(cen["admissible"]))
    out.append("FORCED=" + str(inv["forced_movers"]) + "|FORCED-ADVANCING="
               + str(inv["forced_advancing_movers"]))
    out.append("INVENTORY=i:" + str(class_i) + ",ii:"
               + str(inv["class_ii_selected"]) + ",iii:"
               + str(inv["class_iii_fiber"]))
    out.append("SELECTOR-CLOSURE-FIBER="
               + str(t["selectors"]["closure_preservation_fiber"]))
    out.append("COMMUTING-ADVANCING="
               + str(t["selectors"]["commuting_advancing"]) + "-AT-"
               + str(t["selectors"]["count_reading_rules"]) + "-OF-"
               + str(t["selectors"]["rules"]) + "-RULES")
    out.append("TRAJ=CONVERGES:" + str(tr["converges"]) + ",DIVERGES:"
               + str(tr["diverges"]) + ",UNDEF:"
               + str(tr["undefined_normalization"]) + ",UNCLASSIFIED:"
               + str(tr["unclassified"]))
    out.append("LIMIT-CLASSES=" + str(tr["distinct_limit_classes"])
               + "|MOVER-BLIND-LIMIT=" + tr["mover_blind_limit"])
    out.append("NORMALIZATION-FLIPS=" + str(tr["normalization_flips"]))
    out.append("FOREIGN-FLAGGED=" + str(t["foreign_control"]["flagged"]) + "/"
               + str(t["foreign_control"]["declared"]))
    if MUTANT == "verdict-inert-segment":
        out[9] = "NORMALIZATION-FLIPS=CONSTANT"
    return head + "-<" + "; ".join(out) + ">"


# ---------------------------------------------------------------------------
# 10.  THE RUN
# ---------------------------------------------------------------------------

def run_unit():
    R = {"schema": "cra-accumulation-receipt-v1",
         "pin": "v14/note-cr-batch-pins.md (section CR-A)",
         "python": "%d.%d.%d" % sys.version_info[:3],
         "arithmetic": "int / fractions.Fraction only; no floats, no "
                       "tolerances",
         "source_sha256": sha256_full(SRC),
         "declarations": {}, "tables": {}}

    say("=" * 78)
    say("v14 CR-A -- REFINEMENT BY ACCUMULATION")
    say("Does the pinned grammar contain a geometry-record-ADVANCING move?")
    say("=" * 78)
    say()

    # ---- 0. the float guard and the mutant-blindness guard -----------------
    off = float_guard()
    gate("G-FLOATGUARD",
         "no float literal, true division, banned name or banned import "
         "anywhere in this source (AST scan)", not off, off[:8])
    mo, caught, nsyn = mutant_blindness_scan()
    gate("G-MUTANT-BLINDNESS",
         "no gate-registering function reads run-mode identity (MUTANT / "
         "DELIVERY_RUN / argv); the scanner is validated by four synthetic "
         "injections it must flag",
         (not mo) and caught == nsyn, {"offences": mo, "synthetic_caught":
                                       caught, "synthetic": nsyn})
    say("[0] float guard clean; mutant-blindness scan clean "
        "(%d/%d synthetic injections flagged)." % (caught, nsyn))

    # ---- 1. the pinned sources --------------------------------------------
    rows = src_rows()
    for nm, rel, exp, prov in rows:
        got = sha12(os.path.join(ROOT, rel))
        anchor(nm, "sha256-12 of " + rel, expected_src_hash(nm, exp), got,
               prov)
    gate("G-ANCHOR-COUNT",
         "every declared source-hash row is evaluated",
         len(rows) == len(SRC_ROWS), {"rows": len(rows),
                                      "declared": len(SRC_ROWS)})
    say("[1] %d pinned source hashes verified: %s"
        % (len(SRC_ROWS), ", ".join(r[0] for r in SRC_ROWS)))

    I7 = read_json("v13/code/ha_successor_receipt.json")
    for nm, path, exp, prov in PATH_ROWS:
        p = path_for(nm, path)
        anchor(nm, "I7 receipt path " + "/".join(str(z) for z in p),
               exp, dig(I7, p), prov)
    say("[1] %d path-value anchors verified (the (path, value) pair, not the "
        "file bytes)." % len(PATH_ROWS))

    # the pinned clause quotes, verbatim
    HAP = read_text("v13/paper-ha-successor.md")
    CLAUSES = clause_rows()
    missing_q = [cid for cid, rel, quote, kind, effect in CLAUSES
                 if quote_for(cid, quote) not in HAP]
    gate("G-CLAUSES-VERBATIM",
         "every pinned clause this unit reasons from is quoted VERBATIM from "
         "the pinned source on disk",
         not missing_q, {"clauses": len(CLAUSES), "missing": missing_q})
    gate("G-CLAUSE-TABLE-COMPLETE",
         "the clause table carries every declared clause",
         len(CLAUSES) == len(CLAUSE_ROWS),
         {"carried": len(CLAUSES), "declared": len(CLAUSE_ROWS)})
    say("[1] %d pinned clauses verified verbatim against "
        "v13/paper-ha-successor.md." % len(CLAUSES))

    RB = read_text("RUNBOOK.md")
    eng_missing = [e for e, q in ENGRAVING_ROWS if q not in RB]
    gate("G-ENGRAVINGS-PRESENT",
         "the engraved rules this unit's compliance gates cite are quoted "
         "VERBATIM from RUNBOOK.md on disk",
         not eng_missing, {"engravings": len(ENGRAVING_ROWS),
                           "missing": eng_missing})
    say("[1] %d RUNBOOK engravings verified verbatim (the five 2026-08-09 "
        "engravings and their companions)." % len(ENGRAVING_ROWS))

    # ---- 2. the arena, rebuilt --------------------------------------------
    decl_recs = dig(I7, ("declarations", "records_d2"))
    RECS_ALL = build_records(decl_recs)
    RECS = {k: v for k, v in RECS_ALL.items() if admissible(v)}
    REJECTED = sorted(set(RECS_ALL) - set(RECS))
    anchor("N-ADMISSIBLE-RECORDS", "admissible records rebuilt from I7",
           9, len(RECS), "HA section 4.1: nine records admissible, the two "
           "declared negative controls rejected")
    anchor("N-REJECTED-RECORDS", "the rejected negative controls",
           ["G-INDEF", "G-SINGULAR"], REJECTED,
           "HA section 4.1: one rejection in each failure mode")
    LAPSES = build_lapse_family()
    anchor("N-LAPSE-SIZE", "the declared lapse family size",
           12, len(LAPSES), "HA section 3.1: 12 members at d = 2")
    anchor("N-LAPSE-PAIRS", "ordered lapse pairs",
           132, len(LAPSES) * (len(LAPSES) - 1),
           "HA section 3.1: 132 ordered pairs")
    FRONTS = probe_fronts()
    DIAG = sorted(k for k, s in RECS.items()
                  if all(s[x][LINKS[2]] == s[x][LINKS[0]] + s[x][LINKS[1]]
                         for x in SITES))
    anchor("N-DIAGONAL-SECTOR", "the diagonal sector, recomputed",
           ["G-ANISO", "G-ANISO2", "G-CURVED", "G-DIAG2", "G-FLAT"], DIAG,
           "HA section 6.1: the five records whose order+count readout is "
           "diagonal")
    say("[2] arena rebuilt: |X| = %d sites, %d links, %d admissible records "
        "(%s rejected), %d lapse profiles, %d ordered pairs; diagonal sector "
        "= %s." % (len(SITES), len(LINKS), len(RECS), "/".join(REJECTED),
                   len(LAPSES), len(LAPSES) * (len(LAPSES) - 1),
                   ", ".join(DIAG)))

    # ---- the record-IS-metric re-encoding, recomputed ---------------------
    reenc_ok = 0
    for rn in sorted(RECS):
        for x in SITES:
            q = qmat(RECS[rn][x])
            if all(sum(q[i][j] * lk[i] * lk[j] for i in range(D)
                       for j in range(D)) == RECS[rn][x][lk] for lk in LINKS):
                reenc_ok += 1
    anchor("N-REENCODE-SITES", "sites at which q reproduces every declared "
           "link count", 81, reenc_ok,
           "I7 tables/readout_reencoding: 81 of 81 (record-IS-metric)")

    # ---- the closure census, recomputed and anchored against I7 -----------
    def closure_row(rule):
        out = {}
        for rn in sorted(RECS):
            rec = RECS[rn]
            Lm = {x: lambda_of(rule, rn, rec, x) for x in SITES}
            Iv = {x: qinv(qmat(rec[x])) for x in SITES}
            nz = 0
            for (an, N), (bn, M) in itertools.permutations(LAPSES, 2):
                bad = False
                for x in SITES:
                    om = [N[x] * M[shift(x, LINKS[j])]
                          - M[x] * N[shift(x, LINKS[j])] for j in range(D)]
                    for i in range(D):
                        if sum((Lm[x][i][j] - Iv[x][i][j]) * om[j]
                               for j in range(D)) != 0:
                            bad = True
                            break
                    if bad:
                        break
                if bad:
                    nz += 1
            out[rn] = nz
        return out

    ORDER = ["G-FLAT", "G-DIAG2", "G-ANISO", "G-ANISO2", "G-CURVED",
             "G-OFFDIAG", "G-OFFDIAG2", "G-OFFNEG", "G-CURVOFF"]
    closure = {}
    for rule in ("A-chart", "A-axis", "A-insert", "A-linkframe",
                 "A-insert-x", "A-insert-2x"):
        row = closure_row(rule)
        closure[rule] = row
        mine = [row[r] for r in ORDER]
        theirs = [dig(I7, ("tables", "closure", rule + "|" + r,
                           "nonzero_pairs")) for r in ORDER]
        anchor("N-CLOSURE-" + rule, "the closure row of " + rule
               + " (nonzero pairs of 132)", theirs, mine,
               "I7 tables/closure -- recomputed here from the closed form "
               "rho = (Lambda - I) omega")
    say("[2] the closure census recomputed independently and anchored: 6 "
        "rules x 9 records = 54 cells, all matching I7.")

    # rank
    rank = {}
    for x in SITES:
        rows_ = []
        for (an, N), (bn, M) in itertools.permutations(LAPSES, 2):
            rows_.append(tuple(N[x] * M[shift(x, LINKS[j])]
                               - M[x] * N[shift(x, LINKS[j])]
                               for j in range(D)))
        indep = 0
        basis = []
        for r_ in rows_:
            v = list(Fr(z) for z in r_)
            for b in basis:
                p = next((i for i in range(D) if b[i] != 0), None)
                if p is not None and v[p] != 0:
                    f = divf(v[p], b[p])
                    v = [v[i] - f * b[i] for i in range(D)]
            if any(z != 0 for z in v):
                basis.append(v)
                indep += 1
        rank[str(x)] = indep
    anchor("N-RANK", "the lapse-pair rank at every site",
           {str(x): 2 for x in SITES}, rank,
           "I7 tables/identifiability_rank: full rank 2 at all 9 sites")

    # link-locality lattice
    lat = []
    for a in range(1, 7):
        for b in range(1, 7):
            for c_ in range(1, 13):
                cnt = {LINKS[0]: a, LINKS[1]: b, LINKS[2]: c_}
                q = qmat(cnt)
                if posdef(q):
                    lat.append((a, b, c_, qinv(q)))
    p1 = sum(1 for u, v in itertools.combinations(lat, 2)
             if u[2] == v[2] and u[3][0][1] != v[3][0][1])
    p2 = sum(1 for u, v in itertools.combinations(lat, 2)
             if u[0] == v[0] and u[2] == v[2] and u[3][0][0] != v[3][0][0])
    anchor("N-LATTICE",
           "the link-locality count lattice (admissible points; pairs "
           "sharing n_diag with different I12; pairs sharing (n_e1, n_diag) "
           "with different I11)",
           [361, 5100, 781], [len(lat), p1, p2],
           "I7 tables/link_locality_lattice")
    say("[2] I7's rank (2 at 9 of 9), re-encoding (81 of 81) and count "
        "lattice (361 / 5100 / 781) reproduced.")

    R["declarations"] = {
        "d": D, "L": LL, "links": [list(lk) for lk in LINKS],
        "sites": len(SITES),
        "records": sorted(RECS), "rejected_records": REJECTED,
        "diagonal_sector": DIAG,
        "lapse_family": [nm for nm, _ in LAPSES],
        "probe_fronts": [nm for nm, _ in FRONTS],
        "atom_box": list(BOX),
        "atoms_LIN": ATOMS["LIN"], "atoms_BIL": ATOMS["BIL"],
        "banned_atom": "SIDX",
        "admissibility_probe_steps": list(ADM_STEPS),
        "movers": [{"name": m[0], "family": m[1], "coefficients": list(m[2]),
                    "prose": m[3]} for m in MOVERS],
        "schedules": SCHEDULES, "horizon": T_MAX, "normalizations": NORMS,
        "drag_rules": sorted(READ_LINKS),
    }

    # =====================================================================
    # SECTION A -- THE ANCHOR OBSERVATION: H_a[N] DOES NOT TOUCH s
    # =====================================================================
    progress("section A: the s-frozen verification")
    say()
    say("-" * 78)
    say("A.  THE ANCHOR OBSERVATION: H_a[N] does not touch the geometry "
        "record")
    say("-" * 78)

    regs = [("m-zero", {x: tuple(Fr(0) for _ in range(D)) for x in SITES}),
            ("m-one", {x: tuple(Fr(1) for _ in range(D)) for x in SITES})]
    inst = 0
    smoved = 0
    for rule in sorted(READ_LINKS):
        for rn in sorted(RECS):
            rec = RECS[rn]
            for ln, N in LAPSES:
                for gn, m0 in regs:
                    n0 = {x: 0 for x in SITES}
                    st = (rec, n0, m0)
                    fwd = H_forward(rule, rn, rec, N, st)
                    bwd = H_inverse(rule, rn, rec, N, fwd)
                    inst += 1
                    if s_key(fwd[0]) != s_key(rec):
                        smoved += 1
                    if s_key(bwd[0]) != s_key(rec):
                        smoved += 1
                    if bwd[1] != n0 or bwd[2] != m0:
                        smoved += 1
    gate("G-S-FROZEN-POINTWISE",
         "over every (rule, record, lapse, register) instance the geometry "
         "sector s is bit-identical after H_a[N] and after H_a[N]^{-1}, and "
         "the (n, m) sectors invert exactly",
         smoved == 0, {"instances": inst, "s_moved_or_noninvertible": smoved})
    anchor("N-S-FROZEN-INSTANCES", "the s-frozen instance count",
           11 * 9 * 12 * 2, inst,
           "11 drag rules x 9 records x 12 lapses x 2 registers, computed")
    say("A.1  s is bit-identical after H_a[N] and its inverse at %d of %d "
        "(rule, record, lapse, register) instances." % (inst, inst))

    # the ORBIT measurement: the pinned move monoid's image in the s
    # coordinate.  This could have come out otherwise, and the positive
    # control proves the instrument sees motion when there is motion.
    def s_orbit(gens, depth, rec, rn):
        """The reachable s-values of the move monoid generated by `gens`,
        by exhaustive breadth-first expansion to the declared depth.  No
        truncation: the visited-node count is returned and gated."""
        n0 = {x: 0 for x in SITES}
        m0 = {x: tuple(Fr(0) for _ in range(D)) for x in SITES}
        frontier = [(rec, n0, m0)]
        seen = {orbit_dedup(s_key(rec))}
        visited = 1
        for _ in range(depth):
            nxt = []
            for st in frontier:
                for g in gens:
                    st2 = g(st)
                    key = (s_key(st2[0]),
                           tuple(st2[1][x] for x in SITES),
                           tuple(st2[2][x] for x in SITES))
                    seen.add(orbit_dedup(key[0]))
                    nxt.append(st2)
                    visited += 1
            frontier = nxt
        return seen, visited

    rec0 = RECS["G-FLAT"]
    LD = dict(LAPSES)
    pin_gens = [
        (lambda st, N=LD["one"]: H_forward("A-axis", "G-FLAT", rec0, N, st)),
        (lambda st, N=LD["one"]: H_inverse("A-axis", "G-FLAT", rec0, N, st)),
        (lambda st, N=LD["ramp0"]: H_forward("A-insert", "G-FLAT", rec0, N,
                                             st)),
        (lambda st: D_forward({x: (Fr(1), Fr(1)) for x in SITES}, st)),
    ]

    def fiat(st):
        s, n, m = st
        return ({x: {lk: s[x][lk] + 1 for lk in LINKS} for x in SITES}, n, m)

    ODEPTH = 4
    orb_pin, vis_pin = s_orbit(pin_gens, ODEPTH, rec0, "G-FLAT")
    orb_ctl, vis_ctl = s_orbit(pin_gens + [fiat], ODEPTH, rec0, "G-FLAT")
    gate("G-S-ORBIT-SINGLETON",
         "the s-image of the pinned move monoid (H_a[N], its inverse, D_a[v]) "
         "is a SINGLE point at depth 4 -- the pinned layer has no "
         "geometry-record motion at all",
         len(orb_pin) == 1 and vis_pin == sum(len(pin_gens) ** k
                                              for k in range(ODEPTH + 1)),
         {"pinned_orbit": len(orb_pin), "depth": ODEPTH,
          "nodes_visited": vis_pin, "truncated": False})
    gate("G-S-ORBIT-INSTRUMENT-SEES-MOTION",
         "POSITIVE CONTROL: the same orbit instrument, given one extra "
         "geometry-writing generator, returns an orbit of size depth+1 -- so "
         "the singleton above is a measurement, not a property of the "
         "instrument",
         len(orb_ctl) == ODEPTH + 1,
         {"controlled_orbit": len(orb_ctl), "depth": ODEPTH,
          "nodes_visited": vis_ctl})
    say("A.2  the s-orbit of the pinned move monoid at depth 4: %d point.  "
        "With one geometry-writing generator added: %d points (positive "
        "control)." % (len(orb_pin), len(orb_ctl)))
    R["tables"]["s_frozen"] = {"instances": inst, "s_moved": smoved,
                               "pinned_s_orbit": len(orb_pin), "orbit_nodes": vis_pin,
                               "controlled_s_orbit": len(orb_ctl),
                               "orbit_depth": 4}

    # =====================================================================
    # SECTION B -- EXPRESSIBILITY
    # =====================================================================
    progress("section B: the atom expressibility census")
    say()
    say("-" * 78)
    say("B.  THE ATOMS, and which of them the pinned grammar can express")
    say("-" * 78)
    expressible, banned = expressibility_split()
    gate("G-ATOM-EXPRESSIBILITY",
         "every atom in the design space is licensed by a quoted pinned "
         "clause, and the declared NEGATIVE CONTROL atom (a held-out chart "
         "label) is excluded",
         len(banned) == 1 and all(r[4] for r in expressible),
         {"expressible": len(expressible), "banned": [r[1] for r in banned]})
    say("B.1  %d of %d declared atoms are expressible from the pinned "
        "clauses; the negative control SIDX (a held-out chart label) is "
        "excluded." % (len(expressible), len(ATOM_TABLE)))
    R["tables"]["atoms"] = {
        "declared": len(ATOM_TABLE), "expressible": len(expressible),
        "banned": [r[1] for r in banned],
        "table": [{"family": r[0], "symbol": r[1], "prose": r[2],
                   "expressible": r[3], "licensed_by": r[4]}
                  for r in ATOM_TABLE]}

    # =====================================================================
    # SECTION C -- THE ADVANCING-MOVE CENSUS
    # =====================================================================
    progress("section C: the advancing-move census")
    say()
    say("-" * 78)
    say("C.  THE ADVANCING-MOVE CENSUS")
    say("-" * 78)
    cens = {}
    ADM = {}
    ADV = {}
    for fam in ("LIN", "BIL"):
        cells = probe_cells(fam, RECS, LAPSES, FRONTS)
        adv, adm = run_census(fam, cells)
        n2adv, n2adm = run_census_route2(fam, cells)
        gate("G-CENSUS-TWO-ROUTES-" + fam,
             "the %s census counts are reproduced by an INDEPENDENT "
             "recomputation that builds its admissibility predicate from the "
             "record readout rather than from the determinant expression "
             "(RUNBOOK section 14 addendum, v13 #219)" % fam,
             (len(adv), len(adm)) == (n2adv, n2adm),
             {"route1": [len(adv), len(adm)], "route2": [n2adv, n2adm]})
        expected_cells = len(RECS) * len(LAPSES) * len(FRONTS) * len(SITES)
        cells2, prod2 = probe_cells_route2(fam, RECS, LAPSES, FRONTS)
        gate("G-CENSUS-CELLS-COMPLETE-" + fam,
             "the %s probe-cell set equals an INDEPENDENT enumeration of the "
             "complete (record, lapse, front, site) product, and that product "
             "has the declared size -- a silently dropped cell cannot shrink "
             "the census" % fam,
             cells == cells2 and prod2 == expected_cells,
             {"cells": len(cells), "route2_cells": len(cells2),
              "full_product": prod2, "declared_product": expected_cells})
        cens[fam] = {"candidates": len(BOX) ** NA, "advancing": len(adv),
                     "admissible": len(adm), "probe_cells": len(cells),
                     "full_product": expected_cells}
        ADM[fam] = adm
        ADV[fam] = adv
        say("C.1  family %s: %d declared candidates -> %d advancing "
            "(delta >= 0 everywhere, > 0 somewhere) -> %d admissible (the "
            "record stays positive definite under 1, 2 and 3 applications).  "
            "%d deduplicated probe cells from a %d-cell product."
            % (fam, len(BOX) ** NA, len(adv), len(adm), len(cells),
               expected_cells))
    tot_cand = sum(cens[f]["candidates"] for f in cens)
    tot_adv = sum(cens[f]["advancing"] for f in cens)
    tot_adm = sum(cens[f]["admissible"] for f in cens)
    R["tables"]["census"] = {"per_family": cens, "candidates": tot_cand,
                             "advancing": tot_adv, "admissible": tot_adm}
    say("C.2  TOTAL: %d candidates, %d advancing, %d admissible advancing "
        "movers." % (tot_cand, tot_adv, tot_adm))

    # =====================================================================
    # SECTION D -- THE CHOICE INVENTORY
    # =====================================================================
    progress("section D: the choice inventory")
    say()
    say("-" * 78)
    say("D.  THE CHOICE INVENTORY (forced / stabilizer-fixed / genuinely "
        "free)")
    say("-" * 78)

    # class (i): what the pinned clauses FORCE.
    forced = []
    for fam in ("LIN", "BIL"):
        for c in itertools.product(BOX, repeat=NA):
            ok = True
            for cid, rel, quote, kind, effect in CLAUSES:
                if clause_is_binding(kind) and any(z != 0 for z in c):
                    ok = False
                    break
            if ok:
                forced.append((fam, c))
    forced_zero = [z for z in forced if all(v == 0 for v in z[1])]
    forced_adv = [z for z in forced if z in
                  [(f, c) for f in ADM for c in ADM[f]]]
    gate("G-FORCED-SET-COMPUTED",
         "the class-(i) forced set is COMPUTED from the quoted pinned clause "
         "table, not typed: the only clause that speaks to s-evolution is "
         "C-FROZEN, and it forces the identity",
         len(forced) == len(forced_zero) and len(forced) == 2,
         {"forced": len(forced), "identity_members": len(forced_zero)})
    gate("G-FORCED-ADVANCING-EMPTY",
         "no pinned clause forces an ADVANCING geometry move: the forced set "
         "meets the admissible advancing set in the empty set",
         len(forced_adv) == 0, {"forced_advancing": len(forced_adv)})
    say("D.1  class (i) FORCED: the pinned clause table forces exactly %d "
        "movers (the identity, one per declared family), and neither is "
        "advancing.  Forced advancing movers: %d."
        % (len(forced), len(forced_adv)))

    # class (ii): the chart group's action.
    # The declared uniform space is chart-fixed pointwise.  The POSITIVE
    # CONTROL is the per-link space, on which the same instrument measures a
    # genuinely nontrivial action.
    SMALL = (0, 1)
    perlink = list(itertools.product(
        list(itertools.product(SMALL, repeat=NA)), repeat=3))

    seen = set()
    orbits = 0
    fixedpts = 0
    for pc in perlink:
        if pc in seen:
            continue
        o = {pc, chart_act(pc)}
        seen |= o
        orbits += 1
        if len(o) == 1:
            fixedpts += 1
    equivariant = [pc for pc in perlink if chart_act(pc) == pc]
    uniform = [pc for pc in perlink if pc[0] == pc[1] == pc[2]]
    # THE CLASS-(ii) SELECTION, MEASURED.  A censused candidate is selected by
    # the stabilizer exactly when the chart action MOVES it; the count is
    # computed from the action, never typed, because it is one of the two
    # quantities the verdict HEAD is derived from.
    selected_ii_points = [pc for pc in uniform if chart_act(pc) != pc]
    selected_ii = len(selected_ii_points)
    gate("G-CHART-ACTION-NONTRIVIAL",
         "POSITIVE CONTROL for the stabilizer instrument: on the declared "
         "per-link coefficient space the chart group acts with orbits of size "
         "2, so the instrument can detect a nontrivial action",
         orbits < len(perlink) and fixedpts < len(perlink),
         {"space": len(perlink), "orbits": orbits, "fixed_points": fixedpts})
    gate("G-CLASS-II-SELECTS-NOTHING",
         "the chart symmetry REDUCES the design space (per-link -> "
         "chart-equivariant) but SELECTS no mover: every candidate of the "
         "censused uniform space is a fixed point, so the stabilizer leaves "
         "the whole fiber standing",
         selected_ii == 0 and len(equivariant) > 1,
         {"per_link": len(perlink), "chart_equivariant": len(equivariant),
          "uniform": len(uniform), "selected": selected_ii})
    say("D.2  class (ii) STABILIZER: on the per-link coefficient space "
        "(%d points) the chart group has %d orbits and %d fixed points -- the "
        "instrument sees a nontrivial action.  Chart-equivariance cuts that "
        "space to %d; the censused uniform space (%d points there) is fixed "
        "POINTWISE, so the symmetry reduces and selects nothing."
        % (len(perlink), orbits, fixedpts, len(equivariant), len(uniform)))

    class_iii = tot_adm
    # THE HEAD-SELECTING QUANTITY, DERIVED FROM TWO MEASUREMENTS.  A mover is
    # MOTIVATED when every freedom in it is class-(i) or class-(ii): it is
    # either forced by a pinned clause while advancing, or selected by the
    # pinned stabilizer.  Both components are measured above -- forced_adv from
    # the quoted clause table against the admissible advancing census, and
    # selected_ii from the chart action on the censused space -- and each is
    # separately gated (G-FORCED-ADVANCING-EMPTY, G-CLASS-II-SELECTS-NOTHING).
    # The head is derived from their sum; nothing here is typed.
    motivated_pairs = set(forced_adv) | set(
        (fam, pc[0]) for fam in ("LIN", "BIL") for pc in selected_ii_points)
    motivated_movers = sorted(m[0] for m in MOVERS
                              if (m[1], m[2]) in motivated_pairs)
    motivated = motivated_count(len(forced_adv) + selected_ii)
    gate("G-CLASS-III-FIBER",
         "every admissible advancing mover is class-(iii): no pinned clause "
         "forces it and no pinned symmetry selects it; the fiber is counted "
         "exactly",
         class_iii == tot_adm and motivated == 0,
         {"class_iii_fiber": class_iii, "motivated": motivated})
    say("D.3  class (iii) GENUINELY FREE: the fiber is %d movers exactly.  "
        "MOTIVATED movers (every freedom class-(i) or class-(ii)): %d."
        % (class_iii, motivated))
    R["tables"]["choice_inventory"] = {
        "forced_movers": len(forced), "forced_advancing_movers":
        len(forced_adv), "class_i_motivated_movers": motivated,
        "class_ii_selected": selected_ii,
        "motivated_movers": motivated_movers,
        "class_iii_fiber": class_iii,
        "per_link_space": len(perlink), "per_link_orbits": orbits,
        "per_link_fixed_points": fixedpts,
        "chart_equivariant": len(equivariant), "uniform_space": len(uniform)}

    # =====================================================================
    # SECTION E -- THE SELECTOR CENSUS AND THE STATIC-GEOMETRY THEOREM
    # =====================================================================
    progress("section E: the selector census")
    say()
    say("-" * 78)
    say("E.  THE SELECTOR CENSUS -- can anything expressible SELECT a mover?")
    say("-" * 78)

    closure_fiber = []
    commute_axis = []
    commute_insert = []
    for fam in ("LIN", "BIL"):
        for c in ADM[fam]:
            if sel_preserves_diagonal_sector(fam, c, DIAG, RECS, LAPSES,
                                             FRONTS):
                closure_fiber.append((fam, c))
            if sel_zero_on_links(fam, c, (0, 1), DIAG, RECS, LAPSES, FRONTS) \
                    and sel_no_front_dependence(fam, c):
                commute_axis.append((fam, c))
            if sel_zero_on_links(fam, c, (0, 1, 2), sorted(RECS), RECS,
                                 LAPSES, FRONTS) \
                    and sel_no_front_dependence(fam, c):
                commute_insert.append((fam, c))
    joint = [z for z in closure_fiber if z in commute_axis]

    SELECTORS = [
        ("SEL-TYPE", "PINNED (clause C-TYPE)", "s' stays a positive integer "
         "count", tot_adv),
        ("SEL-ADMISSIBLE", "PINNED (clause C-ADMISSIBLE)", "q(s') stays "
         "positive definite", tot_adm),
        ("SEL-CHART", "PINNED (clause C-CHART)", "chart equivariance",
         len(equivariant)),
        ("SEL-CLOSURE", "DECLARED BY THIS UNIT", "the diagonal sector on "
         "which the record-native rule closes survives the move",
         len(closure_fiber)),
        ("SEL-COMMUTE-AXIS", "DECLARED BY THIS UNIT", "the move commutes with "
         "H_a[N] for the record-native closing rule A-axis",
         len(commute_axis)),
        ("SEL-COMMUTE-INSERT", "DECLARED BY THIS UNIT", "the move commutes "
         "with H_a[N] for the metric-inserted rule A-insert",
         len(commute_insert)),
        ("SEL-JOINT", "DECLARED BY THIS UNIT", "closure preservation AND "
         "commutation, together", len(joint)),
    ]
    sels = selector_rows(SELECTORS)
    gate("G-SELECTOR-CENSUS-COMPLETE",
         "every declared selector is censused",
         len(sels) == len(SELECTORS),
         {"censused": len(sels), "declared": len(SELECTORS)})
    pinned_selectors = [s for s in SELECTORS if s[1].startswith("PINNED")]
    gate("G-NO-PINNED-SELECTOR-SELECTS",
         "no PINNED selector cuts the fiber to one: the pinned clauses "
         "constrain the design space and never determine a member of it",
         all(s[3] > 1 for s in pinned_selectors),
         {s[0]: s[3] for s in pinned_selectors})
    for nm, kind, prose, fib in sels:
        say("E.1  %-20s %-24s fiber = %d" % (nm, kind, fib))

    # THE THEOREM.
    RL = read_link_table()
    count_reading = [r for r in RL if RL[r]]
    blind_rules = [r for r in RL if not RL[r]]
    distinct_sets = sorted(set(tuple(sorted(RL[r])) for r in count_reading))
    measured_sets = sorted({tuple(sorted((0, 1))), tuple(sorted((0, 1, 2)))})
    gate("G-READ-LINK-CENSUS-COMPLETE",
         "the commutation requirement depends on a drag rule only through its "
         "READ-LINK SET (the links whose interval count its weight consults). "
         "The count-reading rules realise exactly the read-link sets measured "
         "below, so the theorem's rule scope is a complete census over the "
         "distinct requirement classes and not an extrapolation from two "
         "samples",
         distinct_sets == measured_sets and len(RL) == 11
         and len(count_reading) == 9,
         {"rules": len(RL), "count_reading": len(count_reading),
          "distinct_read_link_sets": [list(z) for z in distinct_sets],
          "measured_read_link_sets": [list(z) for z in measured_sets],
          "read_link_table": {r: list(RL[r]) for r in sorted(RL)}})
    say("E.1b  the 11 drag rules realise %d distinct read-link sets among the "
        "%d that read a count -- %s -- and both are measured below: the "
        "theorem's scope is a census, not an extrapolation."
        % (len(distinct_sets), len(count_reading),
           " and ".join(str([z + 1 for z in ds]) for ds in distinct_sets)))
    gate("G-STATIC-GEOMETRY-THEOREM",
         "THE STATIC-GEOMETRY THEOREM: no admissible advancing mover commutes "
         "with H_a[N] for any count-reading drag rule -- the fiber is empty "
         "for the record-native closing rule A-axis and for the "
         "metric-inserted rule A-insert alike",
         len(commute_axis) == 0 and len(commute_insert) == 0
         and len(joint) == 0,
         {"commute_axis": len(commute_axis),
          "commute_insert": len(commute_insert), "joint": len(joint),
          "count_reading_rules": len(count_reading),
          "distinct_read_link_sets": [list(z) for z in distinct_sets],
          "count_blind_rules": sorted(blind_rules)})
    gate("G-COUNT-BLIND-EXCEPTION",
         "the two-sided reading: the exception is exactly the two count-blind "
         "rules, and each of them closes on exactly one record -- G-FLAT -- "
         "which every advancing move destroys",
         sorted(blind_rules) == ["A-chart", "B-chart"]
         and closure["A-chart"]["G-FLAT"] == 0
         and all(closure["A-chart"][r] > 0 for r in RECS if r != "G-FLAT"),
         {"count_blind": sorted(blind_rules),
          "A-chart_closing_records": [r for r in ORDER
                                      if closure["A-chart"][r] == 0]})
    say("E.2  THE STATIC-GEOMETRY THEOREM: commuting AND advancing movers = "
        "%d, at %d of %d drag rules (every rule whose weight reads an "
        "interval count).  The exception is exactly the %d count-blind rules "
        "%s, which close on G-FLAT alone."
        % (len(commute_axis), len(count_reading), len(RL),
           len(blind_rules), ", ".join(sorted(blind_rules))))

    # the two-route commutation defect
    lit_cells = 0
    lit_bad = 0
    for nm, fam, c, prose in [(m[0], m[1], m[2], m[3]) for m in MOVERS]:
        for rule in ("A-chart", "A-axis", "A-insert", "A-linkframe"):
            for rn in sorted(RECS):
                rec = RECS[rn]
                for ln, N in LAPSES[:6] + LAPSES[9:]:
                    n0 = {x: (x[0] + 1) for x in SITES}
                    m0 = {x: tuple(Fr(0) for _ in range(D)) for x in SITES}
                    a = commutation_defect_closed(fam, c, rule, rn, rec, N, n0)
                    b = commutation_defect_literal(fam, c, rule, rn, rec, N,
                                                   (rec, n0, m0))
                    lit_cells += 1
                    if a[2] != b[2]:
                        lit_bad += 1
                        continue
                    if a[2] != "OK":
                        continue
                    if s_key(a[0]) != s_key(b[0]) or a[1] != b[1]:
                        lit_bad += 1
    gate("G-COMMUTE-TWO-ROUTES",
         "the commutation defect computed by LITERAL composition of the two "
         "maps on the triple state agrees with the independently built closed "
         "form at every tested cell",
         lit_bad == 0, {"cells": lit_cells, "disagreements": lit_bad})
    say("E.3  the commutation defect by literal composition and by the "
        "independent closed form: %d cells, %d disagreements."
        % (lit_cells, lit_bad))
    R["tables"]["selectors"] = {
        "table": [{"selector": s[0], "status": s[1], "statement": s[2],
                   "fiber": s[3]} for s in SELECTORS],
        "closure_preservation_fiber": len(closure_fiber),
        "closure_preservation_members": sorted(
            "%s%s" % (f, list(c)) for f, c in closure_fiber),
        "commuting_advancing": len(commute_axis),
        "commuting_advancing_insert": len(commute_insert),
        "joint": len(joint),
        "count_reading_rules": len(count_reading), "rules": len(RL),
        "read_link_table": {r: list(RL[r]) for r in sorted(RL)},
        "distinct_read_link_sets": [list(z) for z in distinct_sets],
        "count_blind_rules": sorted(blind_rules),
        "commutation_two_route_cells": lit_cells,
        "commutation_two_route_disagreements": lit_bad}

    # =====================================================================
    # SECTION F -- THE RESCALED TRAJECTORIES
    # =====================================================================
    progress("section F: the rescaled trajectories")
    say()
    say("-" * 78)
    say("F.  THE RESCALED-GEOMETRY TRAJECTORIES")
    say("-" * 78)
    movs = movers_tested()
    scheds = schedules_tested()
    DET = (0, 0)
    traj_rows = []
    conv = 0
    div = 0
    unc = 0
    undef = 0
    cert_fail = 0
    cross_fail = 0
    limitset = {}
    for mname, fam, c, prose in movs:
        for sch in scheds:
            for rn in sorted(RECS):
                rows = trajectory(fam, c, sch, RECS[rn], LAPSES)
                comp = {"q11": [], "q12": [], "q22": []}
                Ef = []
                Ei = []
                adm_all = True
                for (t, ef, ei, s) in rows:
                    q = qmat(s[DET])
                    comp["q11"].append(q[0][0])
                    comp["q12"].append(q[0][1])
                    comp["q22"].append(q[1][1])
                    Ef.append(Fr(ef))
                    Ei.append(Fr(ei))
                    if not admissible(s):
                        adm_all = False
                for norm in NORMS:
                    E = [normalizer(norm, Ef[i], Ei[i])
                         for i in range(len(Ef))]
                    ecls = classify_seq(E)
                    cellres = {}
                    for k in ("q11", "q12", "q22"):
                        ncls = classify_seq(comp[k])
                        if ncls[0] == "UNCLASSIFIED" or \
                                ecls[0] == "UNCLASSIFIED":
                            cert_fail += 1
                        kind, val = limit_of(ncls, ecls)
                        cellres[k] = (kind, val, ncls, ecls)
                    kinds = set(v[0] for v in cellres.values())
                    if E[-1] == 0:
                        celltype = "UNDEFINED-NORMALIZATION"
                        undef += 1
                    elif "UNCLASSIFIED" in kinds:
                        celltype = "UNCLASSIFIED"
                        unc += 1
                    elif "DIVERGES" in kinds:
                        celltype = "DIVERGES"
                        div += 1
                    else:
                        celltype = "CONVERGES"
                        conv += 1
                    wt = window_type([divf(comp["q11"][i], E[i])
                                      for i in range(len(E)) if E[i] != 0]
                                     or [Fr(0)])
                    lim = None
                    if celltype == "CONVERGES":
                        lim = tuple(str(cellres[k][1])
                                    for k in ("q11", "q12", "q22"))
                        limitset.setdefault(lim, []).append(
                            (mname, sch, rn, norm))
                    traj_rows.append({
                        "mover": mname, "schedule": sch, "record": rn,
                        "normalization": norm, "type": celltype,
                        "window_type": wt, "limit": list(lim) if lim else None,
                        "mode": ([cellres[k][1] for k in
                                  ("q11", "q12", "q22")
                                  if cellres[k][0] == "DIVERGES"] or [None])[0],
                        "admissible_throughout": adm_all})
    gate("G-TRAJ-CELLS-COMPLETE",
         "the trajectory census is the complete (mover, schedule, record, "
         "normalization) product",
         len(traj_rows) == len(MOVERS) * len(SCHEDULES) * len(RECS)
         * len(NORMS),
         {"cells": len(traj_rows),
          "declared": len(MOVERS) * len(SCHEDULES) * len(RECS) * len(NORMS),
          "converges": conv, "diverges": div,
          "undefined_normalization": undef, "unclassified": unc})
    # THE DOUBLED-HORIZON RECHECK.  A spurious low-degree fit on a short
    # window survives the classifier; it does NOT survive re-classification at
    # twice the horizon.  Declared scope: every mover and schedule, at two
    # declared records, at both normalizations.
    recheck_cells = 0
    for mname, fam, c, prose in movs:
        for sch in scheds:
            for rn in ("G-FLAT", "G-OFFDIAG"):
                rows2 = trajectory(fam, c, sch, RECS[rn], LAPSES,
                                   T=2 * T_MAX)
                Ef2 = [Fr(r[1]) for r in rows2]
                Ei2 = [Fr(r[2]) for r in rows2]
                q2 = {"q11": [], "q12": [], "q22": []}
                for (t, ef, ei, s) in rows2:
                    q = qmat(s[DET])
                    q2["q11"].append(q[0][0])
                    q2["q12"].append(q[0][1])
                    q2["q22"].append(q[1][1])
                for norm in NORMS:
                    E2 = [normalizer(norm, Ef2[i], Ei2[i])
                          for i in range(len(Ef2))]
                    for k in ("q11", "q12", "q22"):
                        long_ = limit_of(classify_seq(q2[k]),
                                         classify_seq(E2))
                        short_ = limit_of(classify_seq(q2[k][:T_MAX]),
                                          classify_seq(E2[:T_MAX]))
                        recheck_cells += 1
                        if long_ != short_:
                            cross_fail += 1
    gate("G-TRAJ-CLASSIFICATION-CERTIFIED",
         "every sequence entering a limit is certified POLY or EXPC by exact "
         "reproduction of every window value, and the classification is "
         "STABLE under doubling the horizon: a spurious short-window fit "
         "would change its limit and does not",
         cross_fail == 0,
         {"unclassified_component_slots": cert_fail,
          "doubled_horizon_recheck_cells": recheck_cells,
          "recheck_disagreements": cross_fail, "horizon": T_MAX,
          "doubled_horizon": 2 * T_MAX})
    say("F.1  %d trajectory cells (%d movers x %d schedules x %d records x %d "
        "normalizations), horizon t = %d, exact rationals throughout: "
        "%d CONVERGES, %d DIVERGES, %d UNDEFINED-NORMALIZATION, %d "
        "UNCLASSIFIED."
        % (len(traj_rows), len(MOVERS), len(SCHEDULES), len(RECS),
           len(NORMS), T_MAX, conv, div, undef, unc))

    # the classifier's declinations, characterized rather than tolerated
    NONSTATIONARY = ("SCH-DELTA-CYC", "SCH-MIX")
    unc_rows = [r for r in traj_rows if r["type"] == "UNCLASSIFIED"]
    unc_acct = [r for r in unc_rows
                if r["schedule"] in NONSTATIONARY
                or r["mover"] == "M-LAPDIL"]
    gate("G-UNCLASSIFIED-CHARACTERIZED",
         "every cell the classifier declines is accounted for by a named "
         "mechanism -- a NON-STATIONARY schedule (the lapse profile changes "
         "with t, so the counts are quasi-polynomial rather than polynomial) "
         "or the lapse-modulated dilation, whose growth ratio 1+N(x) is "
         "site-dependent so the record is not a single geometric sequence.  "
         "There is no unexplained residue",
         len(unc_rows) == len(unc_acct),
         {"unclassified": len(unc_rows), "accounted": len(unc_acct),
          "residue": [[r["mover"], r["schedule"], r["record"],
                       r["normalization"]]
                      for r in unc_rows if r not in unc_acct][:6],
          "non_stationary_schedules": list(NONSTATIONARY)})
    say("F.1b  the classifier declines %d cells; all %d are accounted for by "
        "a non-stationary schedule (%s) or by the site-dependent growth ratio "
        "of the lapse-modulated dilation -- no unexplained residue."
        % (len(unc_rows), len(unc_acct), ", ".join(NONSTATIONARY)))

    # the normalization-relativity measurement
    bykey = {}
    for r in traj_rows:
        bykey.setdefault((r["mover"], r["schedule"], r["record"]), {})[
            r["normalization"]] = r["type"]
    norm_flips = sum(1 for k, v in bykey.items()
                     if len(set(v.values())) > 1)
    gate("G-NORMALIZATION-RELATIVITY",
         "MEASURED, not assumed: the convergence TYPE moves with the declared "
         "normalization at a nonzero number of cells -- 'the rescaled "
         "geometry converges' is a statement about the declared "
         "per-event denominator, and the count is reported",
         norm_flips > 0,
         {"cells": len(bykey), "type_flips_between_normalizations":
          norm_flips})
    say("F.2  NORMALIZATION-RELATIVITY: of %d (mover, schedule, record) "
        "cells, %d change convergence type between NORM-FRONT and NORM-INT."
        % (len(bykey), norm_flips))

    # the mover-blindness of the limit
    cands = [(len(set(w[0] for w in who)), lim, sorted(set(w[0] for w in who)))
             for lim, who in sorted(limitset.items())
             if "M-FIAT" in set(w[0] for w in who)
             and len(set(w[0] for w in who)) > 2]
    blind_witness = blind_witness_of(cands)
    blind_limit = "YES" if blind_witness else "NO"
    gate("G-LIMIT-MOVER-BLIND",
         "the decisive trajectory finding, measured: at least one exact "
         "rescaled limit is shared by the FOREIGN fiat move and by two or "
         "more structurally different coupled movers -- convergence of the "
         "rescaled geometry does not discriminate the mover",
         blind_witness is not None,
         {"witness_limit": list(blind_witness[0]) if blind_witness else None,
          "movers_sharing_it": blind_witness[1] if blind_witness else None})
    say("F.3  MOVER-BLINDNESS of the limit: the exact rescaled limit %s is "
        "reached by %s -- including the foreign fiat move."
        % (("(" + ", ".join(blind_witness[0]) + ")") if blind_witness
           else "(none)",
           ", ".join(blind_witness[1]) if blind_witness else "(none)"))
    # THE SECOND HEAD-SELECTING QUANTITY, MEASURED.  The convergence bit the
    # verdict reads is a statement about the MOTIVATED movers of section D --
    # measured over the trajectory census, not typed.  The motivated set is
    # empty here, which is exactly what the blocked head reports.
    motivated_all_converge = all(r["type"] == "CONVERGES" for r in traj_rows
                                 if r["mover"] in motivated_movers)
    R["tables"]["trajectories"] = traj_rows
    R["tables"]["trajectory_summary"] = {
        "cells": len(traj_rows), "converges": conv, "diverges": div,
        "unclassified": unc, "undefined_normalization": undef,
        "horizon": T_MAX,
        "distinct_limit_classes": len(limitset),
        "normalization_flips": norm_flips,
        "mover_blind_limit": blind_limit,
        "mover_blind_witness": {"limit": list(blind_witness[0]),
                                "movers": blind_witness[1]}
        if blind_witness else None,
        "motivated_movers": motivated_movers,
        "motivated_all_converge": motivated_all_converge,
        "limit_classes": [{"limit": list(k),
                           "cells": len(v),
                           "movers": sorted(set(w[0] for w in v)),
                           "schedules": sorted(set(w[1] for w in v)),
                           "normalizations": sorted(set(w[3] for w in v))}
                          for k, v in sorted(limitset.items())]}

    # =====================================================================
    # SECTION G -- THE FOREIGN CONTROL
    # =====================================================================
    progress("section G: the foreign control")
    say()
    say("-" * 78)
    say("G.  THE FOREIGN CONTROL")
    say("-" * 78)
    profiles = {}
    for mname, fam, c, prose in MOVERS:
        profiles[mname] = coupling_profile(fam, c, RECS, LAPSES)
    declared_foreign = ["M-FIAT"]
    flagged = [m for m in profiles if profiles[m]["blind"]
               and profiles[m]["advancing"]]
    coupled = [m for m in profiles if not profiles[m]["blind"]]
    inert = [m for m in profiles if profiles[m]["blind"]
             and not profiles[m]["advancing"]]
    gate("G-COUPLING-INSTRUMENT-SEPARATES",
         "POSITIVE CONTROL, gated BEFORE the flag it licenses: the same "
         "instrument reports COUPLED for movers that read the lapse, the "
         "front and the record respectively, so the FOREIGN flag is a "
         "measurement and not a constant",
         profiles["M-CLOSED"]["N"] and profiles["M-FRONT"]["n"]
         and profiles["M-DILATE"]["s"] and len(coupled) >= 3,
         {"coupled": sorted(coupled),
          "M-CLOSED": profiles["M-CLOSED"], "M-FRONT": profiles["M-FRONT"],
          "M-DILATE": profiles["M-DILATE"]})
    gate("G-FOREIGN-FLAGGED",
         "the declared external growth move (+1 into every interval count per "
         "step, by fiat) is flagged FOREIGN by the coupling instrument -- it "
         "reads no pinned field",
         sorted(flagged) == sorted(declared_foreign),
         {"flagged": sorted(flagged), "declared": declared_foreign,
          "blind_but_not_advancing": sorted(inert)})
    # WHICH OF THE NAMED MOVERS THE CENSUS ACTUALLY CONTAINS.  class (iii) is
    # the residue of the ADMISSIBLE ADVANCING census, so a named mover outside
    # that census is not a class-(iii) member of it; the nine are carried
    # through the trajectory measurement as the design space's structural
    # classes, and their membership is measured here rather than assumed.
    ADV_SET = set((f, cc) for f in ADV for cc in ADV[f])
    ADM_SET = set((f, cc) for f in ADM for cc in ADM[f])
    membership = [{"mover": m[0], "family": m[1],
                   "advancing": (m[1], m[2]) in ADV_SET,
                   "admissible_advancing": (m[1], m[2]) in ADM_SET,
                   "coupling": ("FOREIGN" if m[0] in flagged else
                                ("COUPLED" if m[0] in coupled else
                                 "BLIND-NOT-ADVANCING"))}
                  for m in MOVERS]
    in_census = sorted(r["mover"] for r in membership
                       if r["admissible_advancing"])
    outside_census = sorted(r["mover"] for r in membership
                            if not r["admissible_advancing"])
    coupled_in = sorted(r["mover"] for r in membership
                        if r["admissible_advancing"] and r["mover"] in coupled)
    coupled_out = sorted(r["mover"] for r in membership
                         if not r["admissible_advancing"]
                         and r["mover"] in coupled)
    R["tables"]["named_mover_membership"] = {
        "table": membership, "named": len(MOVERS),
        "in_the_admissible_advancing_census": in_census,
        "carried_from_outside_it": outside_census,
        "coupled_in_the_census": coupled_in,
        "coupled_outside_the_census": coupled_out,
        "advancing_but_inadmissible": sorted(
            r["mover"] for r in membership
            if r["advancing"] and not r["admissible_advancing"]),
        "not_advancing": sorted(r["mover"] for r in membership
                                if not r["advancing"])}
    # and the audit must ALSO refuse the coupled movers, for a different
    # measured reason: no pinned clause forces or selects any of them.
    gate("G-FOREIGN-AND-UNMOTIVATED-ARE-DIFFERENT-FINDINGS",
         "the audit separates two gradings: FOREIGN (blind to every pinned "
         "field) and UNMOTIVATED (nothing pinned forces or selects it).  The "
         "fiat move is both; every coupled mover is the second and not the "
         "first -- those inside the admissible advancing census as its "
         "class-(iii) members, those outside it as movers the census excludes, "
         "and the two lists together are exactly the coupled set",
         len(flagged) == 1 and motivated == 0 and len(coupled) >= 3
         and sorted(coupled_in + coupled_out) == sorted(coupled)
         and len(coupled_out) > 0,
         {"foreign": sorted(flagged), "coupled_but_unmotivated":
          sorted(coupled), "motivated": motivated,
          "coupled_in_the_census": coupled_in,
          "coupled_outside_the_census": coupled_out})
    say("G.1  coupling profiles: %s"
        % "; ".join("%s reads {%s}" % (m, ",".join(
            k for k in ("N", "n", "s") if profiles[m][k]) or "nothing")
            for m in sorted(profiles)))
    say("G.2  FOREIGN flagged: %s (declared: %s).  COUPLED: %s -- %d of them "
        "class-(iii) members of the admissible advancing census (%s) and %d "
        "carried from outside it (%s), none motivated by anything pinned, "
        "which is a different finding."
        % (", ".join(sorted(flagged)), ", ".join(declared_foreign),
           ", ".join(sorted(coupled)), len(coupled_in),
           ", ".join(coupled_in), len(coupled_out), ", ".join(coupled_out)))
    R["tables"]["foreign_control"] = {
        "profiles": profiles, "flagged": len(flagged),
        "declared": len(declared_foreign),
        "flagged_names": sorted(flagged), "coupled_names": sorted(coupled),
        "blind_but_not_advancing": sorted(inert)}

    # =====================================================================
    # SECTION H -- THE DISCRIMINATOR CENSUS
    # =====================================================================
    progress("section H: the discriminator census")
    say()
    say("-" * 78)
    say("H.  THE DISCRIMINATOR CENSUS")
    say("-" * 78)
    readouts = {}
    for mname, fam, c, prose in MOVERS:
        rec = RECS["G-OFFDIAG"]
        N = dict(LAPSES)["one"]
        n0 = {x: (x[0] + 1) for x in SITES}
        moved = {x: {lk: rec[x][lk] + dot(c, atomvec(fam, x, lk, N, n0, rec))
                     for lk in LINKS} for x in SITES}
        q = qmat(moved[DET])
        readouts[mname] = (str(q[0][0]), str(q[0][1]), str(q[1][1]),
                           str(qdet(q)))
    pairs = list(itertools.combinations(sorted(readouts), 2))
    separated = [p for p in pairs if readouts[p[0]] != readouts[p[1]]]
    gate("G-DISCRIMINATOR-CENSUS",
         "the one-step record readout separates most but NOT all pairs of "
         "named movers: pairs that agree at one declared coordinate are "
         "counted rather than assumed away",
         len(separated) < len(pairs),
         {"pairs": len(pairs), "separated": len(separated),
          "indistinguishable": ["|".join(p) for p in pairs
                                if readouts[p[0]] == readouts[p[1]]]})
    say("H.1  of %d ordered-free pairs of named movers, %d are separated by "
        "the one-step readout at the declared coordinate; %d are not."
        % (len(pairs), len(separated), len(pairs) - len(separated)))
    R["tables"]["discriminator"] = {
        "readouts": {k: list(v) for k, v in readouts.items()},
        "pairs": len(pairs), "separated": len(separated),
        "indistinguishable": ["|".join(p) for p in pairs
                              if readouts[p[0]] == readouts[p[1]]]}

    # ---- H.2  THE DISCRIMINATOR COORDINATE IS A FREE CHOICE, AND ITS WHOLE
    # ---- FIBER IS CENSUSED.  The count above is a property of ONE coordinate;
    # ---- the readout is therefore swept over the complete declared (record,
    # ---- lapse, front, site) product -- the unit's own probe product, no
    # ---- enlargement -- and the separation count is reported as a range with
    # ---- the fiber that carries it (RUNBOOK section 15: a quantity that moves
    # ---- across a declared free axis is an instrument, never a conclusion).
    progress("section H.2: the discriminator coordinate census")

    def readout_at(fam, c, rec, N, n, x):
        moved = {lk: rec[x][lk] + dot(c, atomvec(fam, x, lk, N, n, rec))
                 for lk in LINKS}
        qq = qmat(moved)
        return (str(qq[0][0]), str(qq[0][1]), str(qq[1][1]), str(qdet(qq)))

    # the set whose pairs the delivered coordinate cannot separate is
    # MEASURED, never named: it is the largest group of named movers sharing a
    # readout there.
    grp_delivered = {}
    for mname in readouts:
        grp_delivered.setdefault(readouts[mname], []).append(mname)
    FOURSET = sorted(max(sorted(grp_delivered.values()), key=len))
    four_pairs = [p for p in pairs if p[0] in FOURSET and p[1] in FOURSET]
    hist = {}
    seps = []
    fullsep = 0
    coord_best = None
    coord_worst = None
    route_bad = 0
    for rn in sorted(RECS):
        rec = RECS[rn]
        for ln, N in LAPSES:
            for fn, n in FRONTS:
                for x in SITES:
                    ro = {m[0]: readout_at(m[1], m[2], rec, N, n, x)
                          for m in MOVERS}
                    nsep = len([p for p in pairs if ro[p[0]] != ro[p[1]]])
                    # ROUTE 2, independent: the separated pairs are all pairs
                    # minus the collisions inside each group of equal readouts.
                    grp = {}
                    for mname in ro:
                        grp[ro[mname]] = grp.get(ro[mname], 0) + 1
                    coll = sum(g * (g - 1) // 2 for g in grp.values())
                    if separated_route2(len(pairs) - coll) != nsep:
                        route_bad += 1
                    seps.append(nsep)
                    hist[len(pairs) - nsep] = hist.get(len(pairs) - nsep,
                                                       0) + 1
                    if all(ro[p[0]] != ro[p[1]] for p in four_pairs):
                        fullsep += 1
                    if coord_best is None or nsep > coord_best[0]:
                        coord_best = (nsep, rn, ln, fn, list(x))
                    if coord_worst is None or nsep < coord_worst[0]:
                        coord_worst = (nsep, rn, ln, fn, list(x))
    declared_coords = len(RECS) * len(LAPSES) * len(FRONTS) * len(SITES)
    better = sum(1 for z in seps if z > len(separated))
    equal = sum(1 for z in seps if z == len(separated))
    fewer = sum(1 for z in seps if z < len(separated))
    delivered_four = len([p for p in four_pairs
                          if readouts[p[0]] != readouts[p[1]]])
    gate("G-DISCRIMINATOR-COORDINATE-CENSUS",
         "the discriminator's coordinate is a FREE choice with an exactly "
         "counted fiber, and the whole fiber is censused: over every declared "
         "(record, lapse, front, site) coordinate the separation count is "
         "measured by two independent routes (pairwise comparison, and the "
         "complement of the collisions inside each group of equal readouts), "
         "the range is reported with the fiber, and the coordinates that "
         "separate EVERY pair of the set the delivered coordinate cannot "
         "separate are counted",
         route_bad == 0 and len(seps) == declared_coords
         and sum(hist.values()) == declared_coords and fullsep > 0
         and min(seps) < max(seps),
         {"coordinates": declared_coords, "route_disagreements": route_bad,
          "min_separated": min(seps), "max_separated": max(seps),
          "pairs": len(pairs), "four_set": FOURSET,
          "four_set_pairs": len(four_pairs),
          "separating_the_four_set": fullsep})
    say("H.2  the discriminator coordinate is free with a fiber of %d: over "
        "the whole declared product the separation count ranges from %d to %d "
        "of %d, and %d coordinates separate every one of the %d pairs inside "
        "%s -- the set the delivered coordinate separates %d of."
        % (declared_coords, min(seps), max(seps), len(pairs), fullsep,
           len(four_pairs), ", ".join(FOURSET), delivered_four))
    R["tables"]["discriminator_coordinate_census"] = {
        "coordinates": declared_coords, "pairs": len(pairs),
        "min_separated": min(seps), "max_separated": max(seps),
        "best_coordinate": {"separated": coord_best[0],
                            "record": coord_best[1], "lapse": coord_best[2],
                            "front": coord_best[3], "site": coord_best[4]},
        "worst_coordinate": {"separated": coord_worst[0],
                             "record": coord_worst[1], "lapse": coord_worst[2],
                             "front": coord_worst[3], "site": coord_worst[4]},
        "indistinguishable_histogram": {str(k): hist[k]
                                        for k in sorted(hist)},
        "four_set": FOURSET, "four_set_pairs": len(four_pairs),
        "separating_the_four_set": fullsep,
        "route_disagreements": route_bad,
        "delivered_coordinate": {
            "record": "G-OFFDIAG", "lapse": "one", "site": list(DET),
            "front": "the two-route probe front n(x) = x_1 + 1, which is NOT "
                     "one of the four declared probe fronts",
            "separated": len(separated),
            "four_set_pairs_separated": delivered_four},
        "declared_coordinates_separating_more": better,
        "declared_coordinates_separating_the_same": equal,
        "declared_coordinates_separating_fewer": fewer}

    # =====================================================================
    # SECTION I -- WHAT THE MOVER-BLIND LIMIT IS A PROPERTY OF, THE
    # CONSERVATION LAW THE PER-EVENT DENOMINATOR CANNOT SEE, AND THE ARENA
    # THE LIMIT IS
    # =====================================================================
    progress("section I: the schedule census, the conservation law, the arena")
    say()
    say("-" * 78)
    say("I.  THE MOVER-BLIND LIMIT, DECOMPOSED")
    say("-" * 78)

    # ---- I.1  the blind class, decomposed by SCHEDULE ----------------------
    wl = tuple(blind_witness[0])
    dec1 = {}
    for (mv_, sch_, rn_, nm_) in limitset[wl]:
        dec1.setdefault(mv_, set()).add(sch_)
    dec1 = hex_schedule_census(dec1)
    dec2 = {}
    for r in traj_rows:
        if r["limit"] == list(wl):
            dec2.setdefault(r["mover"], set()).add(r["schedule"])
    hexcells = [r for r in traj_rows if r["limit"] == list(wl)]
    blind_foreign = sorted(m for m in dec1 if m in flagged)
    blind_coupled = sorted(m for m in dec1 if m in coupled)
    shared_scheds = sorted(set.intersection(*[set(dec1[m])
                                              for m in blind_coupled])) \
        if blind_coupled else []
    hexF = tuple(Fr(z) for z in wl)
    nc = {"cells": 0, "converges": 0, "equal_to_the_limit": 0,
          "not_a_metric": 0, "proportional": 0, "other": 0}
    nc_scalars = set()
    for r in traj_rows:
        if r["mover"] not in blind_coupled or r["schedule"] in shared_scheds \
                or r["normalization"] != "NORM-INT":
            continue
        nc["cells"] += 1
        if r["type"] != "CONVERGES":
            continue
        nc["converges"] += 1
        v = tuple(Fr(z) for z in r["limit"])
        if v == hexF:
            nc["equal_to_the_limit"] += 1
        elif any(z == 0 for z in v) or v[0] * v[2] - v[1] * v[1] <= 0:
            nc["not_a_metric"] += 1
        else:
            rat = set(divf(a, b) for a, b in zip(v, hexF))
            if len(rat) == 1:
                nc["proportional"] += 1
                nc_scalars.add(str(sorted(rat)[0]))
            else:
                nc["other"] += 1
    gate("G-BLIND-LIMIT-SCHEDULE-CENSUS",
         "the mover-blind limit is a property of ONE declared schedule, and "
         "the split is measured by two independent routes (the limit-class "
         "aggregation and the trajectory table): the FOREIGN move reaches it "
         "at every declared schedule, every COUPLED mover that reaches it at "
         "all reaches it at exactly one and the same one, and at the other "
         "schedules no coupled mover reaches the value -- so the licensed "
         "statement is existential and the schedule is part of it",
         dec1 == dec2 and len(hexcells) == len(limitset[wl])
         and len(blind_foreign) == 1
         and set(dec1[blind_foreign[0]]) == set(SCHEDULES)
         and len(shared_scheds) == 1
         and all(set(dec1[m]) == set(shared_scheds) for m in blind_coupled)
         and nc["equal_to_the_limit"] == 0,
         {"limit": list(wl), "cells": len(hexcells),
          "foreign": blind_foreign, "coupled": blind_coupled,
          "schedules_declared": len(SCHEDULES),
          "foreign_schedules": sorted(dec1[blind_foreign[0]]),
          "coupled_schedules": shared_scheds,
          "by_mover": {m: sorted(dec1[m]) for m in sorted(dec1)},
          "at_the_other_schedules": nc,
          "proportionality_scalars": sorted(nc_scalars)})
    say("I.1  the blind class holds %d cells: the foreign move %s reaches the "
        "limit at %d of %d declared schedules, and the %d coupled movers "
        "reach it at %d -- %s -- and at no other.  At the other %d schedules "
        "those movers converge at %d of %d cells, %d to a form that is not a "
        "metric and %d to a form proportional to the limit at a different "
        "scale (%s), and at %d of them to the value itself."
        % (len(hexcells), blind_foreign[0], len(dec1[blind_foreign[0]]),
           len(SCHEDULES), len(blind_coupled), len(shared_scheds),
           ", ".join(shared_scheds), len(SCHEDULES) - len(shared_scheds),
           nc["converges"], nc["cells"], nc["not_a_metric"],
           nc["proportional"], ", ".join(sorted(nc_scalars)),
           nc["equal_to_the_limit"]))

    # ---- I.2  why they agree there: the constant lapse is a degeneracy -----
    uni_rows = []
    for mname, fam, c, prose in MOVERS:
        if mname not in dec1:
            continue
        vals = set()
        uni = True
        for rn in sorted(RECS):
            s = {x: dict(RECS[rn][x]) for x in SITES}
            n = {x: 0 for x in SITES}
            Ns = schedule_of(shared_scheds[0], LAPSES, T_MAX)
            for t in range(T_MAX):
                N = Ns[t]
                ds = {x: {lk: dot(c, atomvec(fam, x, lk, N, n, s))
                          for lk in LINKS} for x in SITES}
                flat = set(ds[x][lk] for x in SITES for lk in LINKS)
                if len(flat) != 1:
                    uni = False
                vals |= flat
                s = {x: {lk: s[x][lk] + ds[x][lk] for lk in LINKS}
                     for x in SITES}
                n = {x: n[x] + N[x] for x in SITES}
        uni_rows.append({"mover": mname, "uniform_at_every_step": uni,
                         "increments": [str(v) for v in sorted(vals)]})
    uni_rows = uniform_increment_rows(uni_rows)
    gate("G-SCH-CONST-UNIFORM-INCREMENT",
         "the mechanism at that one schedule is measured and is a DEGENERACY "
         "of it: there every mover of the blind class writes a site- and "
         "link-uniform increment at every step of the declared horizon, at "
         "every record, so a per-event denominator divides their scalars out "
         "and the shared limit is forced -- the blindness is close to a "
         "tautology at the one schedule where it is measured",
         len(uni_rows) == len(dec1)
         and all(r["uniform_at_every_step"] for r in uni_rows),
         {"schedule": shared_scheds, "movers": [r["mover"] for r in uni_rows],
          "horizon": T_MAX, "records": len(RECS), "rows": uni_rows})
    say("I.2  at %s every one of the %d movers of the blind class writes a "
        "site- and link-uniform increment at every step, at every record: %s."
        % (", ".join(shared_scheds), len(uni_rows),
           "; ".join("%s writes %s" % (r["mover"], ",".join(r["increments"]))
                     for r in uni_rows)))

    # ---- I.3  the undefined normalization is not always an absence of
    # ---- writes: a conservation law can defeat a per-event denominator.
    undef_movers = sorted(set(r["mover"] for r in traj_rows
                              if r["type"] == "UNDEFINED-NORMALIZATION"))
    cons_rows = []
    sample = None
    for mname, fam, c, prose in MOVERS:
        if mname not in undef_movers:
            continue
        cells_ = 0
        netzero = 0
        wrote = 0
        for sch in SCHEDULES:
            for rn in sorted(RECS):
                s = {x: dict(RECS[rn][x]) for x in SITES}
                n = {x: 0 for x in SITES}
                Ns = schedule_of(sch, LAPSES, T_MAX)
                tot = 0
                nz = 0
                for t in range(T_MAX):
                    N = Ns[t]
                    ds = {x: {lk: dot(c, atomvec(fam, x, lk, N, n, s))
                              for lk in LINKS} for x in SITES}
                    for x in SITES:
                        for lk in LINKS:
                            tot += ds[x][lk]
                            if ds[x][lk] != 0:
                                nz += 1
                    s = {x: {lk: s[x][lk] + ds[x][lk] for lk in LINKS}
                         for x in SITES}
                    n = {x: n[x] + N[x] for x in SITES}
                cells_ += 1
                if tilt_net_total(tot) == 0:
                    netzero += 1
                if nz > 0:
                    wrote += 1
        cons_rows.append({"mover": mname, "cells": cells_,
                          "net_zero_cells": netzero,
                          "cells_with_writes": wrote})
        if wrote > 0 and sample is None:
            # the declared sample: six steps of one non-constant schedule from
            # one declared record, reported write by write.
            s = {x: dict(RECS["G-FLAT"][x]) for x in SITES}
            n = {x: 0 for x in SITES}
            Ns = schedule_of("SCH-RAMP0", LAPSES, 6)
            nzw = 0
            mag = 0
            net = 0
            for t in range(6):
                N = Ns[t]
                ds = {x: {lk: dot(c, atomvec(fam, x, lk, N, n, s))
                          for lk in LINKS} for x in SITES}
                for x in SITES:
                    for lk in LINKS:
                        if ds[x][lk] != 0:
                            nzw += 1
                        mag += abs(ds[x][lk])
                        net += ds[x][lk]
                s = {x: {lk: s[x][lk] + ds[x][lk] for lk in LINKS}
                     for x in SITES}
                n = {x: n[x] + N[x] for x in SITES}
            sample = {"mover": mname, "schedule": "SCH-RAMP0",
                      "record": "G-FLAT", "steps": 6, "nonzero_writes": nzw,
                      "absolute_magnitude": mag, "net": tilt_net_total(net),
                      "record_moved": s_key(s) != s_key(RECS["G-FLAT"])}
    gate("G-UNDEFINED-NORMALIZATION-MECHANISM",
         "the undefined normalizations are of TWO kinds, and the second is a "
         "conservation law rather than a silence: over every (schedule, "
         "record) cell of every mover whose NORM-INT normalization is "
         "undefined, the writes sum to exactly zero -- and at the cells where "
         "that mover writes at all the record demonstrably moves while the "
         "per-event denominator registers nothing",
         all(r["net_zero_cells"] == r["cells"] for r in cons_rows)
         and sample is not None and sample["nonzero_writes"] > 0
         and sample["absolute_magnitude"] > 0 and sample["net"] == 0
         and sample["record_moved"],
         {"movers": cons_rows, "sample": sample})
    say("I.3  the undefined-normalization movers: %s.  Every one of them sums "
        "its writes to exactly zero over every (schedule, record) cell; the "
        "writing one moves the record at %d of its %d cells, and over %d "
        "steps of %s from %s it makes %d nonzero writes of total magnitude "
        "%d for a net of %d."
        % ("; ".join("%s (writes at %d of %d cells)"
                     % (r["mover"], r["cells_with_writes"], r["cells"])
                     for r in cons_rows),
           [r for r in cons_rows if r["mover"] == sample["mover"]][0]
           ["cells_with_writes"],
           [r for r in cons_rows if r["mover"] == sample["mover"]][0]["cells"],
           sample["steps"], sample["schedule"], sample["record"],
           sample["nonzero_writes"], sample["absolute_magnitude"],
           sample["net"]))
    R["tables"]["blind_limit_schedule_census"] = {
        "limit": list(wl), "cells": len(hexcells),
        "normalizations": sorted(set(r["normalization"] for r in hexcells)),
        "records": len(set(r["record"] for r in hexcells)),
        "foreign": blind_foreign, "coupled": blind_coupled,
        "declared_schedules": len(SCHEDULES),
        "foreign_schedules": sorted(dec1[blind_foreign[0]]),
        "coupled_schedules": shared_scheds,
        "by_mover": {m: {"schedules": len(dec1[m]),
                         "schedule_names": sorted(dec1[m]),
                         "cells": len([r for r in hexcells
                                       if r["mover"] == m])}
                     for m in sorted(dec1)},
        "at_the_other_schedules": nc,
        "proportionality_scalars": sorted(nc_scalars),
        "uniform_increment_rows": uni_rows,
        "uniform_increment_horizon": T_MAX}
    R["tables"]["undefined_normalization"] = {
        "movers": cons_rows, "sample": sample,
        "cells": sum(r["cells"] for r in cons_rows)}

    # ---- I.4  THE ARENA THE LIMIT IS --------------------------------------
    unit_rec = {lk: 1 for lk in LINKS}
    qw = qmat(unit_rec)
    wscale = weld_scale(len(SITES) * len(LINKS))
    qw_scaled = (divf(qw[0][0], wscale), divf(qw[0][1], wscale),
                 divf(qw[1][1], wscale))
    weld_declared = [rn for rn in sorted(RECS)
                     if all(RECS[rn][x][lk] == 1 for x in SITES
                            for lk in LINKS)]
    gate("G-UNIT-RECORD-IS-THE-BLIND-LIMIT",
         "the record whose every declared link count is 1 has a readout "
         "which, normalised by |X| x |L|, is EXACTLY the mover-blind rescaled "
         "limit measured above -- the accumulation limit of this arena IS a "
         "record's own readout, computed here from this unit's own readout "
         "map; the record is admissible by this unit's test and is not one of "
         "the declared ones",
         tuple(str(z) for z in qw_scaled) == wl and posdef(qw)
         and not weld_declared,
         {"record": [unit_rec[lk] for lk in LINKS],
          "readout": [str(qw[0][0]), str(qw[0][1]), str(qw[1][1])],
          "determinant": str(qdet(qw)), "scale": wscale,
          "scaled": [str(z) for z in qw_scaled], "limit": list(wl),
          "one_of_the_declared_records": weld_declared})
    say("I.4  the record (%s) reads out as (%s) with determinant %s; divided "
        "by |X| x |L| = %d that is (%s) -- the mover-blind limit exactly.  It "
        "is admissible here and is not one of the %d declared records."
        % (", ".join(str(unit_rec[lk]) for lk in LINKS),
           ", ".join([str(qw[0][0]), str(qw[0][1]), str(qw[1][1])]),
           str(qdet(qw)), wscale, ", ".join(str(z) for z in qw_scaled),
           len(RECS)))
    R["tables"]["unit_record_arena"] = {
        "record": [unit_rec[lk] for lk in LINKS],
        "readout": [str(qw[0][0]), str(qw[0][1]), str(qw[1][1])],
        "determinant": str(qdet(qw)),
        "scale": wscale, "scale_reading": "|X| x |L|",
        "scaled_readout": [str(z) for z in qw_scaled],
        "blind_limit": list(wl),
        "equals_the_blind_limit": tuple(str(z) for z in qw_scaled) == wl,
        "admissible_here": posdef(qw),
        "one_of_the_declared_records": weld_declared}

    # the missing object, named by the pinned source itself
    R["tables"]["missing_object"] = {
        "token": "A-GEOMETRY-UPDATE-LAW",
        "named_by": "v13/paper-ha-successor.md sections 12(7) and 14, quoted "
                    "verbatim at clauses C-NOLAW and C-OPEN",
        "quote": "**No geometry-update law is constructed**",
        "consequence": "v4 paper 7 Theorem 6.1 is untouched by the pinned "
                       "layer, and accumulation-refinement has nothing to "
                       "iterate"}

    # ---- the cache gate ---------------------------------------------------
    fresh_cmp = 0
    fresh_bad = 0
    for rule in ("A-axis", "A-insert", "B-all"):
        for rn in sorted(RECS):
            moved = {x: {lk: RECS[rn][x][lk] + 1 for lk in LINKS}
                     for x in SITES}
            for x in SITES:
                a = lambda_of(rule, rn, RECS[rn], x)
                b = lambda_of(rule, rn, RECS[rn], x, fresh=True)
                fresh_cmp += 1
                if a != b:
                    fresh_bad += 1
                # the ALIAS path: a record that differs from the base must not
                # be served the base record's cached weight
                am = lambda_of(rule, rec_tag(rn, moved), moved, x)
                bm = lambda_of(rule, rec_tag(rn, moved), moved, x, fresh=True)
                fresh_cmp += 1
                if am != bm:
                    fresh_bad += 1
    gate("G-CACHE-EXERCISED",
         "the weight memo is exercised AND what it returns is right: hits, "
         "misses and fresh bypasses are all nonzero and every fresh "
         "recomputation matches the memo (a zero-hit or zero-lookup cache "
         "gate is vacuous -- RUNBOOK section 14 addendum, v13 #219)",
         _CACHE["hits"] > 0 and _CACHE["misses"] > 0 and _CACHE["bypass"] > 0
         and fresh_bad == 0,
         {"hits": _CACHE["hits"], "misses": _CACHE["misses"],
          "bypass": _CACHE["bypass"], "fresh_comparisons": fresh_cmp,
          "disagreements": fresh_bad})
    R["tables"]["cache"] = {"hits": _CACHE["hits"], "misses": _CACHE["misses"],
                            "bypass": _CACHE["bypass"],
                            "fresh_comparisons": fresh_cmp,
                            "disagreements": fresh_bad}

    # =====================================================================
    # THE VERDICT
    # =====================================================================
    progress("the verdict")
    payload = {
        "missing": R["tables"]["missing_object"]["token"],
        "expressible": len(expressible), "atoms_declared": len(ATOM_TABLE),
        "candidates": tot_cand, "advancing": tot_adv, "admissible": tot_adm,
        "forced": len(forced), "forced_advancing": len(forced_adv),
        "class_i": motivated, "class_ii": selected_ii,
        "class_iii": class_iii,
        "closure_fiber": len(closure_fiber),
        "commuting_advancing": len(commute_axis),
        "count_reading_rules": len(count_reading), "rules": len(RL),
        "read_link_table": {r: list(RL[r]) for r in sorted(RL)},
        "distinct_read_link_sets": [list(z) for z in distinct_sets],
        "tr_conv": conv, "tr_div": div, "tr_unc": unc, "tr_undef": undef,
        "limit_classes": len(limitset), "blind_limit": blind_limit,
        "norm_flips": norm_flips,
        "foreign_flagged": len(flagged), "foreign_declared":
        len(declared_foreign),
        "motivated": motivated,
        "motivated_all_converge": motivated_all_converge,
    }
    head, segs, full = build_verdict(payload)
    R["verdict"] = full
    R["verdict_head"] = head
    R["verdict_segments"] = segs
    R["anchors"] = ANCHORS
    R["gates"] = GATES
    R["disclosures"] = DISCLOSURES

    rebuilt = rebuild_verdict_from_receipt(R)
    gate("G-VERDICT-STRING-EQUALITY",
         "the COMPLETE emitted verdict string equals a string reconstructed "
         "segment by segment from the RECEIPT OBJECT by a function sharing no "
         "code and no input with the builder -- equality, never containment "
         "(RUNBOOK section 14 addendum, v14 #10)",
         rebuilt == full, {"emitted": full, "rebuilt": rebuilt})

    # every segment must be able to move
    flips = []
    for i, seg in enumerate(segs):
        Rp = json.loads(json.dumps(R))
        t = Rp["tables"]
        t["missing_object"]["token"] = "SOMETHING-ELSE"
        t["atoms"]["expressible"] = t["atoms"]["expressible"] + 1
        t["census"]["candidates"] += 1
        t["census"]["advancing"] += 1
        t["census"]["admissible"] += 1
        t["choice_inventory"]["forced_movers"] += 1
        t["choice_inventory"]["forced_advancing_movers"] += 1
        t["choice_inventory"]["class_ii_selected"] += 1
        t["choice_inventory"]["class_iii_fiber"] += 1
        t["selectors"]["closure_preservation_fiber"] += 1
        t["selectors"]["commuting_advancing"] += 1
        t["selectors"]["count_reading_rules"] += 1
        t["selectors"]["rules"] += 1
        t["trajectory_summary"]["converges"] += 1
        t["trajectory_summary"]["diverges"] += 1
        t["trajectory_summary"]["unclassified"] += 1
        t["trajectory_summary"]["undefined_normalization"] += 1
        t["trajectory_summary"]["distinct_limit_classes"] += 1
        t["trajectory_summary"]["mover_blind_limit"] = "NO"
        t["trajectory_summary"]["normalization_flips"] += 1
        t["foreign_control"]["flagged"] += 1
        t["foreign_control"]["declared"] += 1
        moved = rebuild_verdict_from_receipt(Rp)
        seg_moved = moved.split("-<")[1][:-1].split("; ")[i] != seg
        flips.append((seg, seg_moved))
    gate("G-VERDICT-SEGMENTS-FLIPPABLE",
         "every verdict segment tracks a measured value: perturbing the "
         "receipt object moves every one of them (an inert segment carries no "
         "content even when string equality holds)",
         all(f[1] for f in flips),
         {"segments": len(segs),
          "inert": [f[0] for f in flips if not f[1]]})

    # all three registered heads reachable, by the SAME derivation
    p_blocked = dict(payload)
    p_conv = dict(payload)
    p_conv["motivated"] = 1
    p_conv["motivated_all_converge"] = True
    p_div = dict(payload)
    p_div["motivated"] = 1
    p_div["motivated_all_converge"] = False
    heads = heads_from(build_verdict, [p_blocked, p_conv, p_div])
    gate("G-VERDICT-ALL-THREE-HEADS-REACHABLE",
         "all three registered heads are emitted by the SAME derivation run "
         "on synthetic payloads that differ only in the measured motivation "
         "and convergence bits -- a head that could not come out otherwise is "
         "not a verdict",
         sorted(set(heads)) == ["CRA-BLOCKED-AT-STATIC-GEOMETRY",
                                "CRA-DIVERGES", "CRA-RESCALED-CONVERGES"],
         {"heads": heads})
    say()
    say("-" * 78)
    say("THE VERDICT")
    say("-" * 78)
    say(full)
    say()

    # ---- compliance -------------------------------------------------------
    comp = []
    comp.append(("RUNBOOK 13 addendum v14 #20 (prose renders from the "
                 "receipt)", "G-PROSE-RENDERS-FROM-THE-RECEIPT"))
    comp.append(("RUNBOOK 13 addendum v14 #10 (render from the gated object)",
                 "G-RENDER-FROM-GATED-OBJECT"))
    comp.append(("RUNBOOK 14 addendum v14 #10 (containment is not equality)",
                 "G-VERDICT-STRING-EQUALITY"))
    comp.append(("RUNBOOK 14 addendum v14 #20 (path-value anchoring)",
                 "P-I7-RECORDS"))
    comp.append(("RUNBOOK 14 addendum v13 #208 (no gate reads mutant "
                 "identity)", "G-MUTANT-BLINDNESS"))
    comp.append(("RUNBOOK 14 addendum v13 #219 (independent comparator; "
                 "exercised cache)", "G-CENSUS-TWO-ROUTES-LIN"))
    comp.append(("RUNBOOK 13 addendum v13 #234 (verdict derived in a gate; "
                 "cell completeness)", "G-VERDICT-SEGMENTS-FLIPPABLE"))
    comp.append(("RUNBOOK 13 addendum v13 #314 (precheck may gate the census, "
                 "never name the verdict)", "G-CLASS-III-FIBER"))
    comp.append(("RUNBOOK 14 (symmetry self-test)",
                 "G-CHART-ACTION-NONTRIVIAL"))
    comp.append(("RUNBOOK 15 (declared arena as data)",
                 "G-NORMALIZATION-RELATIVITY"))
    comp.append(("RUNBOOK 13 addendum v14 #20 (the hand-written-prose "
                 "surface swept mechanically)", "G-PAPER-NUMBERS-IN-RECEIPT"))
    comp = compliance_rows(comp)
    R["tables"]["compliance"] = [{"rule": a, "gate": b} for a, b in comp]
    names = (set(g["name"] for g in GATES) | set(a["name"] for a in ANCHORS)
             | set(DEFERRED_GATES))
    gate("G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS",
         "every compliance claim names a gate that actually ran in this run "
         "(RUNBOOK section 14 addendum, v14 #20: a compliance gate whose "
         "comparator cannot disagree with the object under test is vacuous)",
         all(b in names for a, b in comp),
         {"claims": len(comp),
          "unbacked": [b for a, b in comp if b not in names]})

    disclose("X-PRECHECK",
             "The frozen-geometry observation of section A is a PRECHECK: it "
             "gates which candidates are censused (none, under the pinned "
             "dynamics) but never by itself names the verdict.  The "
             "verdict-naming facts -- the census counts, the choice "
             "inventory, the selector fibers and the trajectory types -- are "
             "measured on the CENSUSED objects (RUNBOOK section 13 addendum, "
             "v13 #314).")
    disclose("X-FORCED-CLAUSES",
             "Three clauses are analytically forced once the design space is "
             "uniform in the link index: chart equivariance of every censused "
             "candidate, the pointwise fixedness of the uniform space under "
             "the chart action, and the vanishing of the s-defect for "
             "front-blind movers.  All three are RECORDED as disclosures and "
             "the gates that carry them are paired with the per-link positive "
             "control, which is not forced and does move.")
    disclose("X-BOX",
             "The coefficient box {-1,0,1,2} and the two atom families are "
             "DECLARED arena data.  Every count in the census is relative to "
             "them.  The box-independent statements are: the forced set is "
             "the identity alone; the stabilizer selects nothing; and the "
             "strongest declared selector leaves a fiber of at least two "
             "movers that are separated by a pinned-visible readout.")
    disclose("X-HORIZON",
             "Convergence is typed on the declared horizon t <= %d.  Limits "
             "are exact and are certified by exact reproduction of every "
             "window value under the POLY / EXPC classification; no limit is "
             "claimed for a sequence the classifier does not certify."
             % T_MAX)
    disclose("X-SELECTORS-NOT-PINNED",
             "SEL-CLOSURE, SEL-COMMUTE-AXIS, SEL-COMMUTE-INSERT and SEL-JOINT "
             "are DECLARED BY THIS UNIT.  No pinned source requires a "
             "geometry move to preserve closure or to commute with H_a[N] -- "
             "the pinned source freezes s instead, so the question never "
             "arises there.  Their fibers are reported as what a successor "
             "would inherit if it adopted them, never as pinned forcings.")
    disclose("X-COMPANION-HASHES",
             "The v14 LOG #4 erratum records that two R0 companion hashes "
             "were stale by one commit.  This unit's three pinned sources are "
             "anchored by their own sha256-12 at run time and all three "
             "verify; no value here reads from a companion hash.")
    R["disclosures"] = DISCLOSURES
    R["gates"] = GATES
    R["anchors"] = ANCHORS
    return R, payload


# ---------------------------------------------------------------------------
# 11.  Prose rendered FROM the receipt object
# ---------------------------------------------------------------------------

def render_prose(R):
    t = R["tables"]
    s = []
    s.append("H_a[N] leaves the geometry record bit-identical at %d of %d "
             "(rule, record, lapse, register) instances, and the s-image of "
             "the whole pinned move monoid is a single point at depth %d, "
             "against %d points when one geometry-writing generator is added."
             % (t["s_frozen"]["instances"], t["s_frozen"]["instances"],
                t["s_frozen"]["orbit_depth"], t["s_frozen"]["pinned_s_orbit"]
                + t["s_frozen"]["controlled_s_orbit"]
                - t["s_frozen"]["pinned_s_orbit"]))
    s.append("Of %d declared candidate moves, %d are advancing and %d are "
             "admissible advancing movers."
             % (t["census"]["candidates"], t["census"]["advancing"],
                t["census"]["admissible"]))
    s.append("The pinned clause table forces exactly %d movers -- the "
             "identity, one per declared coefficient family -- and %d "
             "advancing ones."
             % (t["choice_inventory"]["forced_movers"],
                t["choice_inventory"]["forced_advancing_movers"]))
    s.append("On the per-link coefficient space of %d points the chart group "
             "has %d orbits and %d fixed points; chart equivariance cuts that "
             "space to %d, and the censused uniform space is fixed pointwise, "
             "so the stabilizer selects nothing."
             % (t["choice_inventory"]["per_link_space"],
                t["choice_inventory"]["per_link_orbits"],
                t["choice_inventory"]["per_link_fixed_points"],
                t["choice_inventory"]["chart_equivariant"]))
    s.append("The strongest declared selector, closure preservation, leaves a "
             "fiber of %d movers; commuting advancing movers number %d at %d "
             "of %d drag rules."
             % (t["selectors"]["closure_preservation_fiber"],
                t["selectors"]["commuting_advancing"],
                t["selectors"]["count_reading_rules"],
                t["selectors"]["rules"]))
    s.append("The commutation defect computed by literal composition and by "
             "the independent closed form agrees at %d of %d cells."
             % (t["selectors"]["commutation_two_route_cells"]
                - t["selectors"]["commutation_two_route_disagreements"],
                t["selectors"]["commutation_two_route_cells"]))
    s.append("Across %d trajectory cells at horizon t = %d, %d converge, %d "
             "diverge, %d have an undefined normalization and %d are "
             "unclassified, in %d distinct exact limit classes."
             % (t["trajectory_summary"]["cells"],
                t["trajectory_summary"]["horizon"],
                t["trajectory_summary"]["converges"],
                t["trajectory_summary"]["diverges"],
                t["trajectory_summary"]["undefined_normalization"],
                t["trajectory_summary"]["unclassified"],
                t["trajectory_summary"]["distinct_limit_classes"]))
    s.append("The convergence type changes with the declared normalization at "
             "%d of the %d (mover, schedule, record) cells."
             % (t["trajectory_summary"]["normalization_flips"],
                t["trajectory_summary"]["cells"] // 2))
    if t["trajectory_summary"]["mover_blind_witness"]:
        w = t["trajectory_summary"]["mover_blind_witness"]
        s.append("The exact rescaled limit (%s) is reached by %s -- including "
                 "the foreign fiat move."
                 % (", ".join(w["limit"]), ", ".join(w["movers"])))
    s.append("The coupling instrument flags %d of %d declared external growth "
             "moves FOREIGN, and reports %d coupled movers, %d of them "
             "class-(iii) members of the admissible advancing census and %d "
             "carried from outside it, none motivated by anything pinned."
             % (t["foreign_control"]["flagged"],
                t["foreign_control"]["declared"],
                len(t["foreign_control"]["coupled_names"]),
                len(t["named_mover_membership"]["coupled_in_the_census"]),
                len(t["named_mover_membership"]["coupled_outside_the_census"])
                ))
    s.append("Of %d pairs of named movers, %d are separated by the one-step "
             "record readout at the declared coordinate."
             % (t["discriminator"]["pairs"], t["discriminator"]["separated"]))
    dc = t["discriminator_coordinate_census"]
    s.append("Over the %d declared (record, lapse, front, site) coordinates "
             "the one-step readout separates between %d and %d of the %d "
             "pairs, and %d of them separate all %d pairs inside the set the "
             "delivered coordinate separates none of."
             % (dc["coordinates"], dc["min_separated"], dc["max_separated"],
                dc["pairs"], dc["separating_the_four_set"],
                dc["four_set_pairs"]))
    bl = t["blind_limit_schedule_census"]
    s.append("The mover-blind limit is reached by the foreign move at %d of "
             "%d declared schedules and by each of the %d coupled movers at "
             "exactly %d of them, %s, where every one of the %d writes a "
             "site- and link-uniform increment at every step; over the %d "
             "cells at the other %d schedules the coupled movers reach that "
             "value %d times."
             % (len(bl["foreign_schedules"]), bl["declared_schedules"],
                len(bl["coupled"]), len(bl["coupled_schedules"]),
                ", ".join(bl["coupled_schedules"]),
                len(bl["uniform_increment_rows"]),
                bl["at_the_other_schedules"]["cells"],
                bl["declared_schedules"] - len(bl["coupled_schedules"]),
                bl["at_the_other_schedules"]["equal_to_the_limit"]))
    un = t["undefined_normalization"]
    sm = un["sample"]
    wrow = [r for r in un["movers"] if r["mover"] == sm["mover"]][0]
    s.append("%s makes %d nonzero interval writes of total magnitude %d for a "
             "net of %d over %d steps of %s from %s, and its writes sum to "
             "zero at all %d of its (schedule, record) cells -- at %d of "
             "which it writes at all."
             % (sm["mover"], sm["nonzero_writes"], sm["absolute_magnitude"],
                sm["net"], sm["steps"], sm["schedule"], sm["record"],
                wrow["cells"], wrow["cells_with_writes"]))
    if MUTANT == "prose-drift":
        s[1] = s[1].replace("advancing", "ADVANCING")
    return s


def render_blocks(R):
    """The multi-line BLOCKS the paper states as results -- its own verdict,
    the static-geometry theorem and the section 15 arena sentence -- rendered
    HERE from the receipt object, with every numeral and every polarity word
    derived from a measured value.  They are matched against the paper under
    the #125 normalisation rather than character for character, because the
    paper wraps them across lines and quotes them as blockquotes."""
    t = R["tables"]
    sel = t["selectors"]
    ua = t["unit_record_arena"]
    out = [("VERDICT", R["verdict"])]
    pol = "NO" if sel["commuting_advancing"] == 0 else "SOME"
    emp = ("empty" if (sel["commuting_advancing"] == 0
                       and sel["commuting_advancing_insert"] == 0
                       and sel["joint"] == 0) else "NOT empty")
    out.append((
        "THEOREM",
        "**Theorem (static geometry).** Let $r$ be any of the %d declared "
        "drag rules whose weight reads at least one interval count. Then %s "
        "admissible advancing mover in the declared design space commutes "
        "with $H_a[N]$ for every declared lapse profile; the only commuting "
        "mover is $\\Delta \\equiv 0$, which does not advance. In particular "
        "the fiber is %s for the record-native closing rule `A-axis` and for "
        "the metric-inserted rule `A-insert` alike, and the joint fiber with "
        "closure preservation is %s."
        % (sel["count_reading_rules"], pol, emp, emp)))
    out.append((
        "ARENA",
        "The record whose three declared link counts are (%s) reads out as "
        "(%s) with determinant %s, and divided by the declared %s = %d that "
        "is (%s) -- the mover-blind rescaled limit of section 7 exactly, "
        "reached here as a rescaled limit and there as a record."
        % (", ".join(str(z) for z in ua["record"]),
           ", ".join(ua["readout"]), ua["determinant"], ua["scale_reading"],
           ua["scale"], ", ".join(ua["scaled_readout"]))))
    return [(bid, block_text(bid, txt)) for bid, txt in out]


# ---------------------------------------------------------------------------
# 12.  Delivery
# ---------------------------------------------------------------------------

def json_floats(o, path=""):
    bad = []
    if isinstance(o, dict):
        for k, v in o.items():
            bad += json_floats(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            bad += json_floats(v, path + "/%d" % i)
    elif isinstance(o, FLOAT_T):
        bad.append(path)
    return bad


def digest(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True,
                                     default=str).encode()).hexdigest()


def deliver(R, payload):
    # THE GATED OBJECT AND THE RENDERED OBJECT ARE ONE OBJECT.
    gated = {k: R["tables"][k] for k in
             ("s_frozen", "census", "choice_inventory", "selectors",
              "trajectory_summary", "foreign_control", "discriminator",
              "atoms", "missing_object")}
    d_before = digest(gated)
    R = post_gate_injection(R)
    gated2 = {k: R["tables"][k] for k in
              ("s_frozen", "census", "choice_inventory", "selectors",
               "trajectory_summary", "foreign_control", "discriminator",
               "atoms", "missing_object")}
    gate("G-RENDER-FROM-GATED-OBJECT",
         "the object the gates checked is bit-identical to the object the "
         "receipt and the paper render from (RUNBOOK section 13 addendum, "
         "v14 #10)",
         digest(gated2) == d_before,
         {"digest_at_gate_time": d_before[:16],
          "digest_at_write_time": digest(gated2)[:16]})
    # re-derive the verdict from the (now final) receipt object
    gate("G-VERDICT-STILL-EQUAL-AT-WRITE-TIME",
         "the verdict reconstructed from the FINAL receipt object still "
         "equals the emitted string",
         rebuild_verdict_from_receipt(R) == R["verdict"],
         {"rebuilt": rebuild_verdict_from_receipt(R)})
    bad = json_floats(R)
    gate("G-NO-FLOATS-IN-RECEIPT",
         "no float reaches the receipt: every exact quantity is carried as an "
         "int or as a string of a Fraction",
         not bad, {"float_paths": bad[:8]})

    prose = render_prose(R)
    blocks = render_blocks(R)
    R["prose"] = prose
    R["blocks"] = [{"id": bid, "text": txt} for bid, txt in blocks]
    missing = []
    missing_blocks = []
    if os.path.exists(PAPER):
        with open(PAPER, "r") as fh:
            ptxt = fh.read()
        missing = [p for p in prose if p not in ptxt]
        pnorm = norm125(ptxt)
        missing_blocks = [bid for bid, txt in blocks
                          if norm125(txt) not in pnorm]
    else:
        missing = ["<paper file absent>"]
        missing_blocks = ["<paper file absent>"]
    for p in prose:
        say("PROSE| " + p)
        progress("PROSE| " + p)
    gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
         "every load-bearing numeric sentence of the paper is rendered HERE "
         "from the receipt object and appears VERBATIM in "
         "v14/paper-05-accumulation.md (RUNBOOK section 13 addendum, v14 #20)",
         not missing, {"sentences": len(prose), "missing": missing})
    for bid, txt in blocks:
        say("BLOCK| " + bid + " | " + txt)
        progress("BLOCK| " + bid)
    gate("G-BLOCKS-RENDER-FROM-THE-RECEIPT",
         "the paper's multi-line RESULT BLOCKS -- its own verdict block, the "
         "static-geometry theorem and the section 15 arena sentence -- are "
         "rendered HERE from the receipt object, every numeral and every "
         "polarity word derived from a measured value, and each appears in "
         "v14/paper-05-accumulation.md under the RUNBOOK section 14 #125 "
         "normalisation (markdown blockquote prefixes and inline-code markers "
         "stripped, whitespace collapsed).  A stated theorem, a quoted "
         "verdict or a quoted arena that its own measurement no longer "
         "supports cannot survive this gate",
         not missing_blocks, {"blocks": [b[0] for b in blocks],
                              "missing": missing_blocks})

    # THE NEVER-FALSIFIED CENSUS -- the honest denominator.  It is the WHOLE
    # ledger: every must-pass gate registered so far, UNION the declared
    # deferred gates that still have to register (G-DEFERRED-GATES-EVALUATED
    # proves that declaration is complete), UNION every anchor, minus every
    # gate a declared mutant kills.  The SET is computed here because the
    # receipt's counts are finalised before the paper sweep, so the paper's
    # own quotation of them is swept like every other number; the CHECK is
    # registered LAST, after every other gate has run, against the live
    # registry.
    killed = set(m["expected_gate"] for m in MUTANTS)
    denom = (set(g["name"] for g in R["gates"] if g["must_pass"])
             | set(DEFERRED_GATES) | set(a["name"] for a in R["anchors"]))
    never = sorted(denom - killed)
    R["never_falsified"] = never
    R["mutants_declared"] = [m["name"] for m in MUTANTS]
    R["tables"]["never_falsified_census"] = {
        "must_pass_gates_and_anchors": len(denom),
        "killed_by_a_declared_mutant": len(killed),
        "never_falsified": len(never),
        "declared_expectation": NEVER_FALSIFIED_EXPECTED,
        "names": never}
    # The receipt's own counts are finalised BEFORE the paper number sweep, so
    # that a paper quoting them is swept like every other number.  The gates
    # still to run are exactly the declared deferred ones that have not run.
    ran0 = set(g["name"] for g in GATES)
    todo = [g for g in DEFERRED_GATES if g not in ran0]
    R["counts"] = {"gates": len(GATES) + len(todo),
                   "must_pass_gates": (sum(1 for g in GATES if g["must_pass"])
                                       + len(todo)),
                   "anchors": len(ANCHORS), "mutants": len(MUTANTS),
                   "disclosures": len(DISCLOSURES),
                   "never_falsified": len(never)}

    # THE PAPER NUMBER SWEEP.  All four of the programme's false paper numbers
    # to date lived in hand-written prose.  Every numeric token of the paper --
    # not only the rendered sentences -- must be a number the receipt object
    # carries (RUNBOOK section 13 addendum, v14 #20).
    allowed = receipt_number_set(R)
    paper_txt = ""
    if os.path.exists(PAPER):
        with open(PAPER, "r") as fh:
            paper_txt = fh.read()
    toks = paper_number_tokens(paper_txt)
    unbacked = sorted(set(t for t in toks if t not in allowed))
    gate("G-PAPER-NUMBERS-IN-RECEIPT",
         "every numeric token appearing in the paper is a number the receipt "
         "object carries: the hand-written-prose surface is swept "
         "mechanically, not trusted",
         not unbacked and len(toks) > 0,
         {"tokens": len(toks), "distinct": len(set(toks)),
          "unbacked": unbacked[:12]})
    say("paper number sweep: %d numeric tokens, %d distinct, %d unbacked."
        % (len(toks), len(set(toks)), len(unbacked)))


    ran = set(g["name"] for g in GATES)
    LAST_GATES = ("G-DEFERRED-GATES-EVALUATED", "G-FINAL-COUNTS",
                  "G-NEVER-FALSIFIED-CENSUS")
    gate("G-DEFERRED-GATES-EVALUATED",
         "every gate declared DEFERRED (evaluable only after the receipt "
         "object exists) really ran in this run",
         all(g in ran or g in LAST_GATES for g in DEFERRED_GATES),
         {"deferred": list(DEFERRED_GATES),
          "evaluated_after_this_one": ["G-FINAL-COUNTS",
                                       "G-NEVER-FALSIFIED-CENSUS"],
          "not_run": [g for g in DEFERRED_GATES
                      if g not in ran and g not in LAST_GATES]})

    still = [g for g in DEFERRED_GATES
             if g not in set(z["name"] for z in GATES)]
    gate("G-FINAL-COUNTS",
         "the receipt's own gate count, predicted from the ledger plus the "
         "declared deferred gates before the paper sweep, equals the count "
         "actually reached -- so a gate added or dropped anywhere breaks it",
         len(GATES) + len(still) == R["counts"]["gates"]
         and len(ANCHORS) == R["counts"]["anchors"],
         {"predicted": R["counts"]["gates"],
          "reached": len(GATES) + len(still), "still_to_register": still,
          "anchors": len(ANCHORS), "mutants": len(MUTANTS),
          "disclosures": len(DISCLOSURES)})

    # LAST OF ALL: the never-falsified census, checked against the registry
    # every other gate has now finished writing.  The only name this gate has
    # to supply for itself is its own -- it cannot be in the live list at the
    # moment its own predicate is evaluated.
    live = (set(g["name"] for g in GATES if g["must_pass"])
            | set(["G-NEVER-FALSIFIED-CENSUS"])
            | set(a["name"] for a in ANCHORS))
    gate("G-NEVER-FALSIFIED-CENSUS",
         "the never-falsified census is in the receipt from delivery one AND "
         "its denominator is the honest one: this gate runs after every other "
         "gate has registered and requires the published census to be exactly "
         "the live registry of must-pass gates and anchors -- this gate "
         "included -- minus the gates the declared mutants kill, at the "
         "declared cardinality",
         set(never) == live - killed
         and len(never) == NEVER_FALSIFIED_EXPECTED
         and len(live) == len(denom),
         {"never_falsified": len(never),
          "declared_expectation": NEVER_FALSIFIED_EXPECTED,
          "denominator_at_census_time": len(denom),
          "live_denominator": len(live), "killed": len(killed),
          "missing_from_the_census": sorted((live - killed) - set(never)),
          "not_in_the_live_registry": sorted(set(never) - (live - killed))})

    say()
    say("-" * 78)
    say("RECEIPT")
    say("-" * 78)
    say("gates %d (%d must-pass, 0 failures) | anchors %d | mutants %d | "
        "disclosures %d | never-falsified %d"
        % (R["counts"]["gates"], R["counts"]["must_pass_gates"], len(ANCHORS),
           len(MUTANTS), len(DISCLOSURES), len(never)))
    if never:
        say("never falsified: " + ", ".join(never))
    say("verdict: " + R["verdict"])

    with open(OUT_TXT, "w") as fh:
        fh.write("\n".join(LINES) + "\n")
    with open(OUT_JSON, "w") as fh:
        json.dump(R, fh, indent=1, sort_keys=True, default=str)
    return 0


# ---------------------------------------------------------------------------
# 13.  The declared mutants
# ---------------------------------------------------------------------------

MUTANTS = [
    {"name": "float-leak", "expected_gate": "G-FLOATGUARD",
     "breaks": "reports a float offence in the source scan"},
    {"name": "anchor-hash-drift", "expected_gate": "A-I7-RECEIPT",
     "breaks": "drifts the expected sha256-12 of the I7 receipt"},
    {"name": "anchor-skip", "expected_gate": "G-ANCHOR-COUNT",
     "breaks": "silently drops one declared source-hash row"},
    {"name": "path-drift", "expected_gate": "P-I7-RECORDS",
     "breaks": "drifts ONE JSON path component (records_d2 -> records_d3): a "
               "different arena with every file-bytes anchor green"},
    {"name": "quote-drift", "expected_gate": "G-CLAUSES-VERBATIM",
     "breaks": "inverts the missing-object quote so it no longer matches the "
               "pinned source"},
    {"name": "clause-drop", "expected_gate": "G-CLAUSE-TABLE-COMPLETE",
     "breaks": "drops the frozen-reduction clause, the one clause that "
               "computes the forced set"},
    {"name": "s-writes", "expected_gate": "G-S-FROZEN-POINTWISE",
     "breaks": "makes H_a[N] write the lapse into every interval count"},
    {"name": "lapse-drop", "expected_gate": "N-LAPSE-SIZE",
     "breaks": "drops one declared lapse profile"},
    {"name": "census-cell-drop", "expected_gate": "G-CENSUS-CELLS-COMPLETE-LIN",
     "breaks": "drops one probe cell from the census"},
    {"name": "fiber-corrupt", "expected_gate": "G-CENSUS-TWO-ROUTES-LIN",
     "breaks": "corrupts the independent recomputation's admissible count"},
    {"name": "expressibility-lax", "expected_gate": "G-ATOM-EXPRESSIBILITY",
     "breaks": "admits the banned held-out chart label into the design space"},
    {"name": "chart-lax", "expected_gate": "G-CHART-ACTION-NONTRIVIAL",
     "breaks": "makes the chart action the identity, so the stabilizer "
               "instrument can no longer see motion"},
    {"name": "commute-lax", "expected_gate": "G-STATIC-GEOMETRY-THEOREM",
     "breaks": "blinds the front-dependence half of the commutation predicate"},
    {"name": "selector-drop", "expected_gate": "G-SELECTOR-CENSUS-COMPLETE",
     "breaks": "drops the joint selector from the census"},
    {"name": "mover-drop", "expected_gate": "G-TRAJ-CELLS-COMPLETE",
     "breaks": "drops the foreign mover from the trajectory census"},
    {"name": "schedule-drop", "expected_gate": "G-TRAJ-CELLS-COMPLETE",
     "breaks": "drops one declared schedule"},
    {"name": "norm-collapse", "expected_gate": "G-NORMALIZATION-RELATIVITY",
     "breaks": "suppresses the measured normalization-relativity finding"},
    {"name": "foreign-blind", "expected_gate": "G-FOREIGN-FLAGGED",
     "breaks": "makes the coupling instrument report COUPLED for everything, "
               "so the foreign move stops being flagged"},
    {"name": "cache-lax", "expected_gate": "G-CACHE-EXERCISED",
     "breaks": "routes the fresh recomputation back through the memo, so the "
               "bypass count goes to zero"},
    {"name": "cache-alias", "expected_gate": "G-CACHE-EXERCISED",
     "breaks": "serves a moved record the base record's cached weight"},
    {"name": "traj-corrupt", "expected_gate": "G-RENDER-FROM-GATED-OBJECT",
     "breaks": "corrupts a trajectory count AFTER the gates, in the object "
               "the receipt renders from (the v14 #10 INJ_D class)"},
    {"name": "limit-typed", "expected_gate": "G-RENDER-FROM-GATED-OBJECT",
     "breaks": "types a limit value into the rendered object after the gates"},
    {"name": "prose-drift", "expected_gate": "G-PROSE-RENDERS-FROM-THE-RECEIPT",
     "breaks": "perturbs one rendered sentence so it no longer appears "
               "verbatim in the paper"},
    {"name": "compliance-fake",
     "expected_gate": "G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS",
     "breaks": "asserts compliance without the gate having run"},
    # ---- the five verdict injection classes -------------------------------
    {"name": "verdict-typed-segment", "expected_gate":
     "G-VERDICT-STRING-EQUALITY",
     "breaks": "TYPES the theorem segment -- the headline negative finding "
               "emitted inverted (7 commuting advancing movers)"},
    {"name": "verdict-append-text", "expected_gate":
     "G-VERDICT-STRING-EQUALITY",
     "breaks": "appends '-AND-SUPPLIED-BY-THE-PIN' to the MISSING segment "
               "(the containment class)"},
    {"name": "verdict-value-swap", "expected_gate":
     "G-VERDICT-STRING-EQUALITY",
     "breaks": "swaps the class-(i) and class-(iii) values inside the "
               "inventory segment"},
    {"name": "verdict-fully-typed", "expected_gate":
     "G-VERDICT-STRING-EQUALITY",
     "breaks": "replaces every segment with a literal and flips the head"},
    {"name": "verdict-inert-segment", "expected_gate":
     "G-VERDICT-SEGMENTS-FLIPPABLE",
     "breaks": "makes the normalization segment a constant in BOTH the "
               "builder and the comparator: string equality still holds and "
               "the segment stops carrying content"},
    {"name": "head-constant", "expected_gate":
     "G-VERDICT-ALL-THREE-HEADS-REACHABLE",
     "breaks": "the head stops tracking the measured bits, so two of the "
               "three registered heads become unreachable"},
    # ---- falsifiers for the unit's own decisive claims --------------------
    {"name": "orbit-blind", "expected_gate":
     "G-S-ORBIT-INSTRUMENT-SEES-MOTION",
     "breaks": "the orbit instrument records a constant s-coordinate, so it "
               "would report a singleton whatever the generators do"},
    {"name": "frozen-clause-inert", "expected_gate": "G-FORCED-SET-COMPUTED",
     "breaks": "the frozen-reduction clause stays in the table but constrains "
               "nothing, so the forced set stops being computed from it"},
    {"name": "motivated-inject", "expected_gate": "G-CLASS-III-FIBER",
     "breaks": "types one motivated mover into the choice inventory -- the "
               "verdict head's own decisive bit"},
    {"name": "blind-witness-suppress", "expected_gate": "G-LIMIT-MOVER-BLIND",
     "breaks": "suppresses the shared-limit witness, so the mover-blindness "
               "finding is emitted as absent"},
    {"name": "closed-form-skew", "expected_gate": "G-COMMUTE-TWO-ROUTES",
     "breaks": "perturbs the closed-form commutation defect only, so the two "
               "routes must disagree"},
    {"name": "coupling-dead", "expected_gate":
     "G-COUPLING-INSTRUMENT-SEPARATES",
     "breaks": "makes the coupling instrument report BLIND for every mover, "
               "so the FOREIGN flag stops being a measurement"},
    {"name": "readlink-hide", "expected_gate":
     "G-READ-LINK-CENSUS-COMPLETE",
     "breaks": "hides one drag rule from the read-link table, so the "
               "theorem's rule scope stops being a complete census"},
    {"name": "paper-number-inject", "expected_gate":
     "G-PAPER-NUMBERS-IN-RECEIPT",
     "breaks": "injects one numeric token the receipt does not carry into the "
               "paper number sweep"},
    {"name": "readout-perturb", "expected_gate": "N-REENCODE-SITES",
     "breaks": "perturbs the record readout by one diagonal count: the "
               "record-IS-metric re-encoding and every recomputed closure row "
               "must fail"},
    # ---- the falsifiers of the rendered blocks and of the five measurements
    # ---- added with them: the coordinate census, the schedule census, the
    # ---- constant-lapse degeneracy, the telescoping writes, and the arena.
    {"name": "block-drift", "expected_gate":
     "G-BLOCKS-RENDER-FROM-THE-RECEIPT",
     "breaks": "inverts the polarity word of the rendered static-geometry "
               "theorem, so the block the paper states is no longer the block "
               "the measurement renders"},
    {"name": "discriminator-census-fake", "expected_gate":
     "G-DISCRIMINATOR-COORDINATE-CENSUS",
     "breaks": "perturbs the second route to the separated-pair count, so the "
               "coordinate census's two routes must disagree"},
    {"name": "schedule-census-fake", "expected_gate":
     "G-BLIND-LIMIT-SCHEDULE-CENSUS",
     "breaks": "reports every mover of the blind class at every schedule -- "
               "the generalization the schedule census exists to refuse"},
    {"name": "uniform-increment-drop", "expected_gate":
     "G-SCH-CONST-UNIFORM-INCREMENT",
     "breaks": "drops one mover from the uniform-increment measurement, so "
               "the degeneracy is claimed for fewer movers than it is "
               "measured on"},
    {"name": "tilt-net-fake", "expected_gate":
     "G-UNDEFINED-NORMALIZATION-MECHANISM",
     "breaks": "perturbs the net of the writes, so the telescoping "
               "conservation law stops being exact"},
    {"name": "unit-record-scale-drift", "expected_gate":
     "G-UNIT-RECORD-IS-THE-BLIND-LIMIT",
     "breaks": "drifts the declared normalisation |X| x |L| by one, so the "
               "unit record's readout no longer equals the measured limit"},
]


# ---------------------------------------------------------------------------
# 14.  CLI
# ---------------------------------------------------------------------------

def selftest():
    before = {}
    for p in (OUT_TXT, OUT_JSON):
        before[p] = sha256_full(p) if os.path.exists(p) else None
    ok = True
    for i, m in enumerate(MUTANTS):
        sys.stderr.write("  [%2d/%2d] %s\n" % (i + 1, len(MUTANTS), m["name"]))
        sys.stderr.flush()
        r = subprocess.run([sys.executable, SRC, "--mutant", m["name"]],
                           capture_output=True, text=True)
        cert = (r.stdout + r.stderr).strip().splitlines()
        cert = cert[-1] if cert else ""
        died = (r.returncode == 1) and (m["expected_gate"] in (r.stdout
                                                              + r.stderr))
        after = {p: (sha256_full(p) if os.path.exists(p) else None)
                 for p in (OUT_TXT, OUT_JSON)}
        unchanged = (after == before)
        print("%-28s exit=%d expected=%-42s %s%s"
              % (m["name"], r.returncode, m["expected_gate"],
                 "DIED-CORRECTLY" if died else "*** SURVIVED ***",
                 "" if unchanged else " *** ARTIFACTS MOVED ***"))
        if not (died and unchanged):
            ok = False
            print("    certificate: " + cert[:220])
    print("SELFTEST %s (%d mutants)" % ("PASS" if ok else "FAIL",
                                        len(MUTANTS)))
    return 0 if ok else 1


def main():
    global MUTANT
    argv = sys.argv[1:]
    if argv[:1] == ["--list-mutants"]:
        for m in MUTANTS:
            print(m["name"])
        return 0
    if argv[:1] == ["--selftest"]:
        return selftest()
    if argv[:1] == ["--mutant"]:
        if len(argv) < 2 or argv[1] not in [m["name"] for m in MUTANTS]:
            sys.stderr.write("unknown mutant\n")
            return 2
        MUTANT = argv[1]
    elif argv:
        sys.stderr.write("unknown argument\n")
        return 2
    try:
        R, payload = run_unit()
        rc = deliver(R, payload)
    except GateFailure as e:
        sys.stderr.write("\n%s\n" % e)
        return 1
    print("\n".join(LINES))
    return rc


if __name__ == "__main__":
    sys.exit(main())
