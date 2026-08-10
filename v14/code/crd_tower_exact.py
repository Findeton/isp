#!/usr/bin/env python3
"""
v14 CR-D -- THE SYMMETRY-TOWER LIMIT: FOUR WINGS.  Exact instrument.

PIN: v14/note-cr-batch-pins.md, section CR-D (frozen v14 ledger #30, sha256-12
1cfee4fc0891).  The pin is verified BY HASH at run time, and so are the three
pinned sources of R0 row I6 -- TB3's third-base receipt (c9bc956fe751), GEN
(e0b2f444f6a9), PSI (7c7b91a9257e) -- plus the two TB3 construction-recipe
artifacts this unit read to recover the wing-structure definitions (the TB3
paper and the TB3 instrument source), recorded here as additional anchors.
NOTHING is imported from any of them: every object below is REIMPLEMENTED.

THE QUESTION (pin CR-D):
  the one measured non-copying growth in the corpus is the group tower.
  Construct the FOUR-wing analog of TB3's base by TB3's own construction rule
  read as data, compute the holonomy/system groups at four wings at the
  declared completions, and test: (1) does the three-wing ladder EMBED in the
  four-wing structure; (2) the four-wing ceiling -- attained or bounded;
  (3) the growth law of the tower; (4) do the new groups stay in the
  alternating/linear families.

Pre-registered heads, all first class:
  CRD-TOWER-EXTENDS-<embedding, ceiling, families>
  CRD-TOWER-BREAKS-<mode>
  CRD-BLOCKED-AT-SCALE-<reached scope>
Each segment is derived INSIDE a gate from measured counts.  The emitted
string is compared for COMPLETE STRING EQUALITY against an INDEPENDENT
reconstruction built from the receipt object alone (RUNBOOK section 14
addenda, v14 #10 and v14 #20): reconstruct_verdict_from_receipt() shares no
code and no input with build_verdict(), and five injection mutants prove it
fires.

CLI CONTRACT (confirmed in code before invocation, v13 #238):
  (no arguments)      THE PLAIN DELIVERY RUN.  Every gate, the verdict, and
                      the two artifacts v14/code/crd_tower_output.txt and
                      v14/code/crd_tower_receipt.json.  Exit 0.  Any gate
                      failure aborts BEFORE any artifact is written.
  --mutant NAME       The pipeline with the named injection active.  MUST
                      exit 1 with a NAMED gate failure and MUST NOT write any
                      artifact.  Unknown name -> exit 2.
  --list-mutants      The declared mutant names, one per line.  Exit 0.
  --selftest          THE FALSIFICATION SELFTEST: re-invokes this file once
                      per declared mutant, requires exit 1, requires the death
                      certificate to name a gate, and requires the artifacts
                      on disk to be byte-unchanged.  Writes no artifacts.

Arithmetic is exact throughout: int and fractions.Fraction only.  A float
literal, a float call, a true-division operator or a banned import anywhere in
this source is a gate failure (G-FLOATGUARD, an AST scan of this file).

Concurrency note: this unit owns ONLY v14/paper-08-tower-four-wings.md,
v14/code/crd_tower_exact.py, v14/code/crd_tower_output.txt and
v14/code/crd_tower_receipt.json.  It reads pinned v13 receipts, the TB3 paper
and instrument source, and v14 notes; it writes nothing else.
"""

import ast
import hashlib
import itertools
import json
import os
import subprocess
import sys
from collections import Counter, deque
from fractions import Fraction as Fr

SRC = os.path.abspath(__file__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SRC)))
OUT_TXT = os.path.join(os.path.dirname(SRC), "crd_tower_output.txt")
OUT_JSON = os.path.join(os.path.dirname(SRC), "crd_tower_receipt.json")
PAPER = os.path.join(ROOT, "v14", "paper-08-tower-four-wings.md")

MUTANT = None            # set only from the command line; gates never read it


class GateFailure(Exception):
    pass


GATES = []
ANCHORS = []
WAIVERS = []

# gates that can only be evaluated at WRITE time, after the receipt exists
DEFERRED_GATES = ("G-RENDER-FROM-GATED-OBJECT", "G-NO-FLOATS-IN-RECEIPT",
                  "G-PROSE-RENDERS-FROM-THE-RECEIPT", "G-RECEIPT-CONSISTENT",
                  "G-FALSIFIER-CENSUS", "G-WAIVERS-VERIFIED",
                  "G-FINAL-GATE-COUNT", "G-DEFERRED-GATES-EVALUATED")


def gate(name, statement, ok, value=None):
    """Register a gate.  A gate predicate NEVER references mutant identity
    (RUNBOOK section 14 addendum, v13 #208)."""
    GATES.append({"name": name, "statement": statement,
                  "passed": bool(ok), "value": value})
    if not ok:
        raise GateFailure("GATE FAILED: %s -- %s | value=%r"
                          % (name, statement, value))
    return True


def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def sha256_full(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


import time as _t
_T0 = _t.time()


def prog(msg):
    sys.stderr.write("[crd %6.1fs] %s\n" % (_t.time() - _T0, msg))
    sys.stderr.flush()


# ---------------------------------------------------------------------------
# 1.  G-FLOATGUARD -- exact arithmetic enforced by an AST scan of this source
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# 2.  Anchors -- file bytes and (path, value) pairs
# ---------------------------------------------------------------------------

ANCHOR_ROWS = [
    ("A-PIN-CRD", "v14/note-cr-batch-pins.md", "1cfee4fc0891",
     "this unit's pin: the CR-D box, frozen at v14 ledger #30"),
    ("A-R0-PIN", "v14/note-r0-founding-pin.md", "e9d2bedff244",
     "the R0 founding pin: row I6 names the three sources verified below"),
    ("A-I6-TB3", "v13/code/tb3_third_base_receipt.json", "c9bc956fe751",
     "R0 row I6 -- TB3's third base: the three-wing base, the ladder, the "
     "ceiling theorem, the declared completions"),
    ("A-I6-GEN", "v13/code/gen_generality_receipt.json", "e0b2f444f6a9",
     "R0 row I6 -- GEN: the psi-independent defect law whose four-wing form "
     "is re-measured here"),
    ("A-I6-PSI", "v13/code/psi_curvature_receipt.json", "7c7b91a9257e",
     "R0 row I6 -- PSI: the one law D(psi) = [P_W, u(psi)], re-measured at "
     "four wings"),
    ("A-RECIPE-TB3-PAPER", "v13/paper-tb3-third-base.md", "4a1f9c53d864",
     "construction recipe read read-only for the wing-structure definitions "
     "(pin CR-D: record which files and hash them as additional anchors)"),
    ("A-RECIPE-TB3-CODE", "v13/code/tb3_third_base_exact.py", "f36d80d7ef97",
     "construction recipe read read-only for the wing-structure definitions; "
     "nothing is imported from it -- every object here is reimplemented"),
]

# VERBATIM-TEXT ANCHORS (RUNBOOK section 14 addendum, v14 #34, adopted with
# its three modifications): evaluated BEFORE the byte anchors, each row bound
# to a NAMED CONSUMER GATE, and each row a CONTEXT WINDOW rather than a
# fragment -- so the anchor binds the meaning to its use, not merely the
# existence of a string.  RUNBOOK.md is deliberately anchored HERE and not by
# bytes: it is a living document that moved during this unit's construction
# (the v14 #4 lesson -- a hash of a tree still moving must be re-verified),
# so what is anchored is the text of the rules that bind, not the file.
VERBATIM_ANCHOR_ROWS = [
    ("V-RULE-COMPLETION", "v13/paper-tb3-third-base.md",
     "> $Q$ = the **lexicographically first** transposition $(i,j)$ of the "
     "system\n> triple labels with $1\\le i<j<8$ — label 0 fixed, so $Ve_0 = "
     "\\psi$ still —\n> whose completion $V = H(\\psi)\\,Q$ has a Born shadow "
     "invariant under **no**\n> non-identity wing symmetry.",
     "G-COMPLETION-RULE-CENSUS",
     "the completion-selection rule, in the words this unit re-runs at four "
     "wings"),
    ("V-RULE-CEILING", "v13/paper-tb3-third-base.md",
     "Every defect is a commutator of label permutations fixing\nlabel 0, "
     "hence an **even** permutation of the seven non-zero system labels;\n"
     "every wing symmetry is measured even on the labels and measured to fix "
     "label 0",
     "G-CEILING-INGREDIENTS",
     "the ceiling argument's own ingredients, whose four-wing analogues are "
     "measured here"),
    ("V-RULE-LADDER", "v13/paper-tb3-third-base.md",
     "its rungs here are $1 < A_4 < \\mathrm{GL}(3,2) < A_6 < A_7$; and **its"
     "\ntop is realised**",
     "G-THREE-WING-LADDER",
     "the three-wing ladder as I6's paper states it -- the object whose "
     "extension is this unit's question"),
    ("V-PIN-QUESTION", "v14/note-cr-batch-pins.md",
     "Construct the FOUR-wing analog of TB3's base by\nTB3's own construction "
     "rule (read as data from the pinned receipt:\nthe wing structure, S₃ → "
     "S₄ on the wing factor)",
     "G-CHOICE-INVENTORY",
     "the pin's construction instruction, bound to the inventory gate that "
     "reports what the rule forces and what it leaves free"),
    ("V-RUNBOOK-WAIVER", "RUNBOOK.md",
     "a never-falsified waiver naming a mutant or a\nforcing is itself a "
     "claim requiring verification — the named\nmutant must reach and be "
     "killed by the gate, or the forcing\nmust be machine-checked",
     "G-WAIVERS-VERIFIED",
     "the rule engraved at v14 #34 after this unit's pin froze; it binds at "
     "delivery (#246/#313) and its consumer gate machine-checks every waiver"),
    ("V-RUNBOOK-VERBATIM", "RUNBOOK.md",
     "the verbatim-text anchor kind is standard,\nwith three binding "
     "modifications: evaluated before byte\nanchors; each row bound to a named "
     "consumer gate; context\nwindows anchored rather than fragments",
     "G-VERBATIM-ANCHORS",
     "the rule this anchor block itself implements"),
]

# PATH-VALUE ANCHORS (RUNBOOK section 14 addendum, v14 #20): a read-by-path
# anchors the (path, value) PAIR, not only the file bytes.
PATH_ANCHOR_ROWS = [
    ("P-I6-WINGS", "v13/code/tb3_third_base_receipt.json",
     ("tables", "base_declaration", "carrier", "wings"), 3,
     "I6's wing count -- the tower's third rung, the one this unit steps past"),
    ("P-I6-CARRIER", "v13/code/tb3_third_base_receipt.json",
     ("tables", "base_declaration", "carrier", "carrier"), 64,
     "I6's carrier: 2^3 system labels x 2^3 pointer labels"),
    ("P-I6-NSYS", "v13/code/tb3_third_base_receipt.json",
     ("tables", "base_declaration", "carrier", "system_triple_dimension"), 8,
     "I6's system-label dimension, the base of the completion census"),
    ("P-I6-WINGGROUP", "v13/code/tb3_third_base_receipt.json",
     ("tables", "base_declaration", "wing_symmetry", "order"), 6,
     "I6's wing symmetry group order -- the S_3 that becomes S_4 here"),
    ("P-I6-SETTINGS", "v13/code/tb3_third_base_receipt.json",
     ("tables", "base_declaration", "settings", "settings"), 27,
     "I6's setting family: one declared rotation per wing"),
    ("P-I6-FRAMES", "v13/code/tb3_third_base_receipt.json",
     ("tables", "base_declaration", "frames", "frames"), 6,
     "I6's frames: the 3! leg-orders"),
    ("P-I6-NODES", "v13/code/tb3_third_base_receipt.json",
     ("tables", "base_declaration", "frames", "nodes_per_setting"), 30,
     "I6's transport graph size: frames x checkpoints"),
    ("P-I6-Q", "v13/code/tb3_third_base_receipt.json",
     ("tables", "arena", "the_declared_completion_transposition"),
     [0, 3, 2, 1, 4, 5, 6, 7],
     "I6's declared reference completion, returned by the completion rule at "
     "three wings -- the rule this unit re-runs at four"),
    ("P-I6-PSTAR", "v13/code/tb3_third_base_receipt.json",
     ("tables", "ord_census", "P_star"), "ACB",
     "I6's declared symmetry: the lex-first non-identity wing permutation"),
    ("P-I6-CENSUS-SIZE", "v13/code/tb3_third_base_receipt.json",
     ("tables", "ord_census", "census_size_measured"), 5040,
     "I6's exhaustive completion census: 7! label permutations fixing 0"),
    ("P-I6-ORD-DIST", "v13/code/tb3_third_base_receipt.json",
     ("tables", "ord_census", "ord_distribution_at_P_star"),
     {"1": 48, "2": 384, "3": 1728, "4": 1152, "5": 1152, "6": 576},
     "I6's exhaustive ord distribution at P* -- recovered here by two routes"),
    ("P-I6-MAXORD", "v13/code/tb3_third_base_receipt.json",
     ("tables", "ord_census", "the_maximum_order_at_P_star"), 6,
     "I6's measured maximum defect order at P*, the fourth declared target"),
    ("P-I6-LEXQ6", "v13/code/tb3_third_base_receipt.json",
     ("tables", "ord_census", "lex_first_Q_per_order", "6"),
     [0, 1, 3, 2, 5, 4, 7, 6],
     "I6's lex-first completion at the maximum order -- the ceiling-attaining "
     "completion"),
    ("P-I6-HOLONOMIES", "v13/code/tb3_third_base_receipt.json",
     ("tables", "a1_ord_sweep", "holonomy_orders"), [1, 1008, 72, 15120],
     "I6's four target holonomy orders, in its own declared target order"),
    ("P-I6-K6", "v13/code/tb3_third_base_receipt.json",
     ("tables", "the_ladder", "per_instance", "A1 target ord = 6",
      "defect_subgroup_order"), 2520,
     "I6's top rung: |A_7|, the defect subgroup at the maximum-order target"),
    ("P-I6-CEILING", "v13/code/tb3_third_base_receipt.json",
     ("tables", "the_ladder", "the_ceiling", "the_algebraic_ceiling"), 15120,
     "I6's ceiling theorem value -- |Alt(7)| x the measured pointer image"),
    ("P-I6-CEILING-ATTAINED", "v13/code/tb3_third_base_receipt.json",
     ("tables", "the_ladder", "the_ceiling", "the_ceiling_is_attained"), True,
     "I6's ceiling is attained -- the fact whose four-wing analog is the "
     "pin's question (2)"),
    ("P-I6-REF-HOL", "v13/code/tb3_third_base_receipt.json",
     ("tables", "negative_controls", "reference_holonomy_order"), 2160,
     "I6's reference holonomy order, the A_6 rung of the ladder"),
    ("P-I6-EMB-INDEX", "v13/code/tb3_third_base_receipt.json",
     ("tables", "the_ladder", "the_embedding", "the_index"), 7,
     "I6's x7 = [A_7 : A_6]: the embedding it constructed"),
    ("P-I6-2WING-CARRIER", "v13/code/tb3_third_base_receipt.json",
     ("tables", "positive_control", "carrier_at_two_wings"), 16,
     "I6's own two-wing control carrier -- the tower's second rung"),
    ("P-I6-2WING-HOL", "v13/code/tb3_third_base_receipt.json",
     ("tables", "positive_control", "per_defect_order", "3",
      "holonomy_group_order"), 6,
     "I6's two-wing holonomy order at defect order 3 -- the tower's second "
     "data point, recovered here by this unit's own generic machinery"),
    ("P-GEN-DEFECT-LAW", "v13/code/gen_generality_receipt.json",
     ("tables", "defect_law", "per_declared_preparation_vector", "psi-2",
      "the_law_D_equals_sigma_Vt_sigma_V_tensor_I"), True,
     "GEN's psi-independent defect law form, re-measured at four wings"),
    ("P-PSI-ONE-LAW", "v13/code/psi_curvature_receipt.json",
     ("tables", "one_law", "deviations"),
     {"E_form": 0, "centralizer": 0, "cocycle": 0,
      "householder_not_involutive": 0, "refactorisation": 0,
      "tensor_split": 0},
     "PSI's one law D(psi) = [P_W, u(psi)] with zero deviations, re-measured "
     "at four wings"),
    ("P-PSI-CARRIER", "v13/code/psi_curvature_receipt.json",
     ("tables", "base_declaration", "carrier"), 81,
     "PSI's carrier: a TWO-wing base at system dimension 3 -- so its law is "
     "inherited as a FORM, never as a number of this unit's arena"),
]


def read_json(rel):
    with open(os.path.join(ROOT, rel), "r") as fh:
        return json.load(fh)


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
        got = sha12(os.path.join(ROOT, rel))
        if MUTANT == "anchor-hash" and name == "A-I6-TB3":
            got = "0" * 12
        if MUTANT == "anchor-hash-" + name:
            got = "0" * 12
        ANCHORS.append({"name": name, "kind": "file-bytes", "artifact": rel,
                        "expected": expect, "measured": got,
                        "provenance": why, "ok": got == expect})
        gate(name, "external anchor %s verifies at %s" % (expect, rel),
             got == expect, {"expected": expect, "measured": got})
    return len(rows)


def verify_path_anchors():
    cache = {}
    for name, rel, path, expect, why in PATH_ANCHOR_ROWS:
        if rel not in cache:
            cache[rel] = read_json(rel)
        p = tuple(path)
        if MUTANT == "path-drift" and name == "P-I6-LEXQ6":
            p = ("tables", "ord_census", "lex_first_Q_per_order", "4")
        try:
            got = read_by_path(cache[rel], p)
        except (KeyError, IndexError, TypeError):
            got = None
        if MUTANT == "path-value-drift" and name == "P-I6-CEILING":
            got = None
        if MUTANT == "path-value-" + name:
            got = None
        ok = (got == expect)
        ANCHORS.append({"name": name, "kind": "path-value", "artifact": rel,
                        "json_path": list(p), "expected": expect,
                        "measured": got, "provenance": why, "ok": ok})
        gate(name, "path-value anchor: %s[%s] reads exactly %r"
             % (rel, ".".join(str(x) for x in path), expect), ok,
             {"path": list(p), "expected": expect, "measured": got})
    return len(PATH_ANCHOR_ROWS)


# ---------------------------------------------------------------------------
# 3.  Exact permutation and matrix machinery
# ---------------------------------------------------------------------------

def pcomp(p, q):
    """apply q first, then p."""
    return tuple(p[x] for x in q)


def pinv(p):
    o = [0] * len(p)
    for i, x in enumerate(p):
        o[x] = i
    return tuple(o)


def pord(p):
    idp = tuple(range(len(p)))
    n, q = 1, p
    while q != idp:
        q = pcomp(q, p)
        n += 1
        if n > 10 ** 7:
            raise RuntimeError("order overflow")
    return n


def parity(p):
    seen = [False] * len(p)
    s = 0
    for i in range(len(p)):
        if seen[i]:
            continue
        j, c = i, 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            c += 1
        s += c - 1
    return s % 2


def cycle_type(p):
    ct = Counter()
    seen = set()
    for i in range(len(p)):
        if i in seen:
            continue
        c, j = 0, i
        while j not in seen:
            seen.add(j)
            j = p[j]
            c += 1
        ct[c] += 1
    return tuple(sorted(ct.items()))


def factorial(n):
    v = 1
    for k in range(2, n + 1):
        v *= k
    return v


def frinv(x):
    """exact reciprocal of a non-zero Fraction, with no division operator."""
    return Fr(x.denominator, x.numerator)


class Mx:
    """A square matrix over Q, stored as a list of column dicts."""

    __slots__ = ("n", "c")

    def __init__(self, n, c):
        self.n = n
        self.c = c

    @staticmethod
    def ident(n):
        return Mx(n, [{i: Fr(1)} for i in range(n)])

    @staticmethod
    def from_perm(p):
        return Mx(len(p), [{p[j]: Fr(1)} for j in range(len(p))])

    def __matmul__(self, B):
        out = []
        A = self.c
        for j in range(B.n):
            acc = {}
            for k, v in B.c[j].items():
                for i, w in A[k].items():
                    x = acc.get(i)
                    acc[i] = (w * v) if x is None else x + w * v
            out.append(dict((i, v) for i, v in acc.items() if v))
        return Mx(self.n, out)

    def T(self):
        out = [dict() for _ in range(self.n)]
        for j, col in enumerate(self.c):
            for i, v in col.items():
                out[i][j] = v
        return Mx(self.n, out)

    def get(self, i, j):
        return self.c[j].get(i, Fr(0))

    def apply(self, v):
        out = [Fr(0)] * self.n
        for j, x in enumerate(v):
            if x:
                for i, w in self.c[j].items():
                    out[i] += w * x
        return out

    def as_perm(self):
        p = [None] * self.n
        seen = set()
        for j, col in enumerate(self.c):
            if len(col) != 1:
                return None
            (i, v), = col.items()
            if v != 1 or i in seen:
                return None
            seen.add(i)
            p[j] = i
        return tuple(p)

    def key(self):
        return tuple(tuple(sorted(col.items())) for col in self.c)

    def is_orthogonal(self):
        return (self.T() @ self).key() == Mx.ident(self.n).key()

    def nnz(self):
        return sum(len(c) for c in self.c)


# ---------------------------------------------------------------------------
# 4.  Deterministic Schreier-Sims: order and membership WITHOUT building the
#     group.  It shares no intermediate value with the brute-force closure
#     below -- no group element is ever produced -- so the pair is genuinely
#     independent (RUNBOOK section 13 addendum, v13 #234).
# ---------------------------------------------------------------------------

class BSGS:
    def __init__(self, n):
        self.n = n
        self.idp = tuple(range(n))
        self.base = []
        self.S = []
        self.tv = []

    def _orbit(self, i):
        b = self.base[i]
        u = {b: self.idp}
        dq = deque([b])
        while dq:
            x = dq.popleft()
            for g in self.S[i]:
                y = g[x]
                if y not in u:
                    u[y] = pcomp(g, u[x])
                    dq.append(y)
        self.tv[i] = u

    def sift(self, g, start=0):
        h = g
        for i in range(start, len(self.base)):
            u = self.tv[i].get(h[self.base[i]])
            if u is None:
                return h, i
            h = pcomp(pinv(u), h)
        return h, len(self.base)

    def _new_level(self, point):
        self.base.append(point)
        self.S.append([])
        self.tv.append({point: self.idp})

    def add(self, g):
        if g == self.idp:
            return
        h, lev = self.sift(g)
        if h == self.idp:
            return
        if lev == len(self.base):
            self._new_level(next(x for x in range(self.n) if h[x] != x))
        for i in range(lev + 1):
            if h not in self.S[i]:
                self.S[i].append(h)
        for i in range(lev + 1):
            self._orbit(i)
        self._fix()

    def _fix(self):
        i = len(self.base) - 1
        while i >= 0:
            redo = False
            for x in list(self.tv[i].keys()):
                ux = self.tv[i][x]
                for s in list(self.S[i]):
                    uy = self.tv[i].get(s[x])
                    if uy is None:
                        continue
                    sg = pcomp(pinv(uy), pcomp(s, ux))
                    if sg == self.idp:
                        continue
                    h, lev = self.sift(sg, i + 1)
                    if h != self.idp:
                        if lev == len(self.base):
                            self._new_level(
                                next(y for y in range(self.n) if h[y] != y))
                        for j in range(i + 1, lev + 1):
                            if h not in self.S[j]:
                                self.S[j].append(h)
                        for j in range(i + 1, lev + 1):
                            self._orbit(j)
                        i = lev
                        redo = True
                        break
                if redo:
                    break
            if not redo:
                i -= 1

    def order(self):
        o = 1
        for t in self.tv:
            o *= len(t)
        return o

    def contains(self, g):
        h, _ = self.sift(g)
        return h == self.idp

    def orbit_sizes(self):
        return [len(t) for t in self.tv]


def bsgs_of(gens, n):
    drop = (MUTANT == "schreier-lax"
            or (MUTANT == "schreier-lax4" and n >= 32))
    B = BSGS(n)
    seq = list(gens)
    if drop and len(seq) > 1:
        seq = seq[:1] if MUTANT == "schreier-lax4" else seq[1:]
    for g in seq:
        B.add(g)
    return B


def closure(gens, n, cap=200000):
    """Brute-force closure: builds every element.  The comparator for BSGS at
    the scales where both are affordable."""
    idp = tuple(range(n))
    S = {idp}
    acc = []
    seq = list(gens)
    if MUTANT == "closure-lax" and n == 64 and len(seq) > 1:
        seq = seq[:1]
    for g in seq:
        if g in S:
            continue
        acc.append(g)
        S = {idp}
        dq = deque([idp])
        while dq:
            x = dq.popleft()
            for h in acc:
                y = pcomp(h, x)
                if y not in S:
                    S.add(y)
                    dq.append(y)
                    if len(S) > cap:
                        return None
    return S


def alt_group_on(support, n):
    """The FULL alternating group on a support, brute-forced as permutations
    of n labels fixing everything outside it."""
    sup = sorted(support)
    out = set()
    for pm in itertools.permutations(sup):
        q = list(range(n))
        for a, b in zip(sup, pm):
            q[a] = b
        q = tuple(q)
        if parity(q) == 0:
            out.add(q)
    return out


def gl_labels(nb):
    """GL(nb, 2) = Aut(F_2^nb) as label permutations of the 2^nb labels
    fixing 0: built from the linearity requirement on a basis, never cited."""
    nsys = 1 << nb
    out = set()
    for images in itertools.permutations(range(1, nsys), nb):
        q = [0] * nsys
        for a in range(nsys):
            v = 0
            for i in range(nb):
                if (a >> i) & 1:
                    v ^= images[i]
            q[a] = v
        if len(set(q)) == nsys:
            out.add(tuple(q))
    return out


# ---------------------------------------------------------------------------
# 5.  THE CONSTRUCTION RULE, READ AS DATA AND WRITTEN GENERIC IN THE WING
#     COUNT.  Every coordinate below is the wing-count-generic form of a TB3
#     declaration; which coordinates the rule FORCES at four wings and which
#     it leaves free is measured in section 7's choice inventory.
# ---------------------------------------------------------------------------

ROT_ORDER = ("R0", "R1", "R2")
ROT_PYTH = {"R0": (Fr(1), Fr(0)), "R1": (Fr(3, 5), Fr(4, 5)),
            "R2": (Fr(5, 13), Fr(12, 13))}
SHIFT_TABLE = {0: (0, 1), 1: (1, 0)}
NS = 2                                   # system dimension per wing
CACHE_STATS = {"hits": 0, "misses": 0}


def rotation(g):
    c, s = ROT_PYTH[g]
    if MUTANT == "rot-lax" and g == "R1":
        c = c + Fr(1, 1000)
    return ((c, -s), (s, c))             # R[i][j] = R[row][col]


class Species:
    """A wing count with its carrier, its wing symmetry group and its legs."""

    def __init__(self, nw):
        self.NW = nw
        self.NSYS = 2 ** nw
        self.NPT = 2 ** nw
        self.NC = self.NSYS * self.NPT
        self.J0 = 0
        self.PERMS = tuple(itertools.permutations(range(nw)))
        self.IDENT = tuple(range(nw))
        self.NAME = {}
        letters = "ABCDEFGH"
        for pi in self.PERMS:
            self.NAME[pi] = "".join(letters[pi[w]] for w in range(nw))
        self.SIGMA = dict((pi, self._sigma(pi)) for pi in self.PERMS)
        self.PCARR = dict(
            (pi, tuple(self.SIGMA[pi][i // self.NPT] * self.NPT
                       + self.SIGMA[pi][i % self.NPT] for i in range(self.NC)))
            for pi in self.PERMS)
        self.FRAMES = self.PERMS
        self.NLEGS = 1 + nw
        self.CKPTS = tuple(range(self.NLEGS + 1))
        self.DIVISION_EVENTS = (0, self.NLEGS)
        self.LMAX = 2 * self.NLEGS + 2
        self.SETTINGS = tuple(itertools.product(ROT_ORDER, repeat=nw))
        self.LOC = dict(((w, g), self._u_local(w, g))
                        for w in range(nw) for g in ROT_ORDER)

    def bits(self, a):
        return tuple((a >> (self.NW - 1 - w)) & 1 for w in range(self.NW))

    def frombits(self, b):
        v = 0
        for x in b:
            v = v * 2 + x
        return v

    def _sigma(self, pi):
        inv = pinv(pi)
        return tuple(self.frombits(tuple(self.bits(a)[inv[w]]
                                         for w in range(self.NW)))
                     for a in range(self.NSYS))

    def _u_local(self, w, g):
        R = rotation(g)
        cols = [dict() for _ in range(self.NC)]
        for j in range(self.NC):
            a, p = divmod(j, self.NPT)
            sb = list(self.bits(a))
            pb = list(self.bits(p))
            for o in range(NS):
                amp = R[sb[w]][o]
                if amp == 0:
                    continue
                for x in range(NS):
                    v = R[x][o] * amp
                    if v == 0:
                        continue
                    nb = list(sb)
                    nb[w] = x
                    npb = list(pb)
                    npb[w] = SHIFT_TABLE[o][pb[w]]
                    i = (self.frombits(tuple(nb)) * self.NPT
                         + self.frombits(tuple(npb)))
                    cols[j][i] = cols[j].get(i, Fr(0)) + v
        for c in cols:
            for k in [k for k, v in c.items() if v == 0]:
                del c[k]
        return Mx(self.NC, cols)

    def setting_name(self, st):
        return "TB-" + "".join(str(ROT_ORDER.index(x)) for x in st)

    def stabiliser(self, st):
        return tuple(pi for pi in self.PERMS
                     if all(st[pinv(pi)[w]] == st[w] for w in range(self.NW)))

    def householder(self, psi):
        n = self.NSYS
        w = [psi[i] - (Fr(1) if i == 0 else Fr(0)) for i in range(n)]
        ww = sum(x * x for x in w)
        cols = [dict() for _ in range(n)]
        for j in range(n):
            for i in range(n):
                v = (Fr(1) if i == j else Fr(0))
                if ww != 0:
                    v -= 2 * w[i] * w[j] * frinv(ww)
                if v != 0:
                    cols[j][i] = v
        return Mx(n, cols)

    def kron_pointer_identity(self, V):
        cols = [dict() for _ in range(self.NC)]
        for j in range(self.NC):
            a, p = divmod(j, self.NPT)
            for i, v in V.c[a].items():
                cols[j][i * self.NPT + p] = v
        return Mx(self.NC, cols)

    def born_symmetric(self, V, sig):
        return all(V.get(i, j) ** 2 == V.get(sig[i], sig[j]) ** 2
                   for j in range(V.n) for i in range(V.n))

    def select_Q(self, psi):
        skip_the_first_hit = (MUTANT == "three-wing-Q-lax"
                              and self.NSYS == 8)
        seen_one = False
        """THE DECLARED COMPLETION-SELECTION RULE, verbatim in the generic
        form: Q = the LEXICOGRAPHICALLY FIRST transposition (i, j) of the
        system labels with 1 <= i < j < NSYS -- so label 0 is fixed and
        V e_0 = psi still -- such that the Born shadow of V = H(psi) . Q is
        NOT invariant under ANY non-identity wing symmetry.  Returns None when
        the rule admits nothing: an EMPTY rule is a measured outcome."""
        H = self.householder(psi)
        for i in range(1, self.NSYS):
            for j in range(i + 1, self.NSYS):
                q = list(range(self.NSYS))
                q[i], q[j] = q[j], q[i]
                q = tuple(q)
                V = H @ Mx.from_perm(q)
                if all(not self.born_symmetric(V, self.SIGMA[pi])
                       for pi in self.PERMS if pi != self.IDENT):
                    if skip_the_first_hit and not seen_one:
                        seen_one = True
                        continue
                    return q
        return None


SPEC_CACHE = {}


def species(nw):
    if nw not in SPEC_CACHE:
        CACHE_STATS["misses"] += 1
        SPEC_CACHE[nw] = Species(nw)
    else:
        CACHE_STATS["hits"] += 1
    return SPEC_CACHE[nw]


def species_fresh(nw):
    """A cache-BYPASSING build: self-test phases must evaluate fresh (RUNBOOK
    section 14 addendum, v13 #185)."""
    return Species(nw)


def ghz_reference(sp):
    """The reference preparation, read from I6's declaration as a TYPE: the
    GHZ-type vector carrying the declared weights 3/5 and 4/5 at the all-zero
    and all-one labels."""
    v = [Fr(0)] * sp.NSYS
    v[0] = Fr(3, 5)
    v[sp.NSYS - 1] = Fr(4, 5)
    return v


def literal_label7(sp):
    """The alternative reading of the same declaration: the weight 4/5 placed
    at LABEL 7 literally, whatever the wing count."""
    v = [Fr(0)] * sp.NSYS
    v[0] = Fr(3, 5)
    v[7] = Fr(4, 5)
    return v


# ---------------------------------------------------------------------------
# 6.  The world: legs, process, the two gluing rules, the transport graph
# ---------------------------------------------------------------------------

def transpose_labels(n, i, j):
    q = list(range(n))
    q[i], q[j] = q[j], q[i]
    return tuple(q)


def push_state(s, sp):
    out = [Fr(0)] * len(s)
    for i, x in enumerate(s):
        out[sp[i]] = x
    return tuple(out)


def push_bornkey(key, sp):
    out = [None] * len(key)
    for j, c in enumerate(key):
        out[sp[j]] = tuple(sorted((sp[i], v) for i, v in c))
    return tuple(out)


def push_realkey(key, sp):
    return frozenset((sp[i], sp[j], v) for i, j, v in key)


class World:
    """One (species, preparation, completion, setting)."""

    def __init__(self, sp, psi, Q, setting):
        self.sp = sp
        self.psi = tuple(psi)
        self.Q = Q
        self.setting = setting
        self.V = sp.householder(psi) @ Mx.from_perm(Q)
        self.u = sp.kron_pointer_identity(self.V)
        self.legs = dict((fr, [self.u] + [sp.LOC[(w, setting[w])] for w in fr])
                         for fr in sp.FRAMES)
        self.proc = dict((fr, self._process(fr)) for fr in sp.FRAMES)
        bornmemo = {}
        self._fk = {}
        self._rk = {}
        for fr in sp.FRAMES:
            ks = []
            for L in self.legs[fr]:
                kk = id(L)
                if kk in bornmemo:
                    CACHE_STATS["hits"] += 1
                else:
                    CACHE_STATS["misses"] += 1
                    bornmemo[kk] = tuple(
                        tuple(sorted((i, v * v) for i, v in col.items()))
                        for col in L.c)
                ks.append(bornmemo[kk])
            self._fk[fr] = ks
            self._rk[fr] = [self._realkey(fr, k) for k in range(sp.NLEGS)]

    def _process(self, fr):
        sp = self.sp
        v = [Fr(0)] * sp.NC
        v[sp.J0] = Fr(1)
        states = [tuple(x * x for x in v)]
        for L in self.legs[fr]:
            v = L.apply(v)
            states.append(tuple(x * x for x in v))
        occ = [frozenset(i for i, x in enumerate(s) if x != 0) for s in states]
        return states, occ

    def _realkey(self, fr, k):
        L = self.legs[fr][k]
        oin = self.proc[fr][1][k]
        oout = self.proc[fr][1][k + 1]
        return frozenset((i, j, L.get(i, j) ** 2)
                         for j in oin for i in oout if L.get(i, j) != 0)

    def defect_measured(self, pi):
        """sigma . u . sigma^-1 = u . D^-1, so D = (sigma u sigma^-1)^T . u,
        read off the actual leg matrices with no commutator formula."""
        sp = self.sp
        P = Mx.from_perm(sp.PCARR[pi])
        Pi = Mx.from_perm(pinv(sp.PCARR[pi]))
        conj = P @ (self.u @ Pi)
        return conj.T() @ self.u, conj

    def admission(self, fast=True, connective="unique"):
        """The four-clause predicate, in order, per ordered frame pair, per
        checkpoint, per rule.  A link is drawn only where the rule admits
        UNIQUELY.  `fast` memoises the FULL-rule push by wing permutation --
        licensed because the leg MULTISET is frame-independent (the frames
        differ in leg ORDER alone) and gated equal to the naive route."""
        sp = self.sp
        scope = list(sp.PERMS)
        pf = {}
        pr = {}
        pocc = {}
        pst = {}
        for pi in scope:
            spm = sp.PCARR[pi]
            if spm[sp.J0] != sp.J0:
                continue
            if fast:
                pf[pi] = tuple(sorted(push_bornkey(k, spm)
                                      for k in self._fk[sp.FRAMES[0]]))
            for X in sp.FRAMES:
                if not fast:
                    pf[(X, pi)] = tuple(sorted(push_bornkey(k, spm)
                                               for k in self._fk[X]))
                pr[(X, pi)] = tuple(sorted(push_realkey(k, spm)
                                           for k in self._rk[X]))
                for t in sp.CKPTS:
                    pocc[(X, pi, t)] = frozenset(spm[i]
                                                 for i in self.proc[X][1][t])
                    pst[(X, pi, t)] = push_state(self.proc[X][0][t], spm)
        selff = dict((X, tuple(sorted(self._fk[X]))) for X in sp.FRAMES)
        selfr = dict((X, tuple(sorted(self._rk[X]))) for X in sp.FRAMES)
        out = {}
        for t in sp.CKPTS:
            for rule in ("FULL", "REAL"):
                tab = {}
                for X in sp.FRAMES:
                    for Y in sp.FRAMES:
                        if X == Y:
                            continue
                        adm = []
                        for pi in scope:
                            spm = sp.PCARR[pi]
                            if spm[sp.J0] != sp.J0:                # clause 1
                                continue
                            if rule == "FULL":                     # clause 2
                                got = pf[pi] if fast else pf[(X, pi)]
                                if got != selff[Y]:
                                    continue
                            else:
                                if pr[(X, pi)] != selfr[Y]:
                                    continue
                            if pocc[(X, pi, t)] != self.proc[Y][1][t]:  # cl 3
                                continue
                            if pst[(X, pi, t)] != self.proc[Y][0][t]:   # cl 4
                                continue
                            adm.append(pi)
                        if connective == "unique":
                            if len(adm) == 1:
                                tab[(X, Y)] = adm[0]
                        else:                                # the alternative
                            if adm:
                                tab[(X, Y)] = adm[0]
                out[(t, rule)] = tab
        return out


def build_graph(sp, world, adm):
    nodes = tuple((fr, t) for fr in sp.FRAMES for t in sp.CKPTS)
    links = []
    for fr in sp.FRAMES:
        for k in range(sp.NLEGS):
            links.append((("leg", fr, k + 1), (fr, k), (fr, k + 1),
                          world.legs[fr][k]))
    for t in sp.CKPTS:
        for rule in ("FULL", "REAL"):
            seen = set()
            for (X, Y), pi in sorted(adm[(t, rule)].items()):
                if (X, Y) in seen:
                    continue
                seen.add((X, Y))
                seen.add((Y, X))
                links.append((("id", rule, t, X, Y), (X, t), (Y, t),
                              Mx.from_perm(sp.PCARR[pi])))
    return nodes, tuple(links)


def spanning_generators(nodes, links, base, reverse=False):
    adj = dict((n, []) for n in nodes)
    order = range(len(links) - 1, -1, -1) if reverse else range(len(links))
    for i in order:
        _, a, b, _ = links[i]
        adj[a].append((i, b, 1))
        adj[b].append((i, a, -1))
    n0 = links[0][3].n
    tree = {base: Mx.ident(n0)}
    te = set()
    dq = deque([base])
    while dq:
        v = dq.pop() if reverse else dq.popleft()
        for i, w, d in adj[v]:
            if w in tree:
                continue
            M = links[i][3]
            tree[w] = (M @ tree[v]) if d > 0 else (M.T() @ tree[v])
            te.add(i)
            dq.append(w)
    gens = []
    for i, (nm, a, b, M) in enumerate(links):
        if i in te or a not in tree or b not in tree:
            continue
        gens.append((nm, tree[b].T() @ (M @ tree[a])))
    return tree, te, gens


def product_form(g, npt):
    """(alpha on system labels, beta on pointer labels) with g = alpha (x)
    beta, or None.  Measured, never assumed."""
    ns = len(g) // npt
    a = tuple(g[x * npt] // npt for x in range(ns))
    b = tuple(g[x] % npt for x in range(npt))
    for x in range(ns):
        for p in range(npt):
            if g[x * npt + p] != a[x] * npt + b[p]:
                return None
    return a, b


def pf_pair(g, npt):
    """the faithful degree-2*NSYS image of a product-form carrier element."""
    a, b = product_form(g, npt)
    return tuple(a) + tuple(x + npt for x in b)


def instance(sp, psi, Q, setting, base_index=0, fast=True,
             connective="unique"):
    """One measured instance: the graph, the holonomy by two routes, the
    defect subgroup, the images."""
    w = World(sp, psi, Q, setting)
    adm = w.admission(fast=fast, connective=connective)
    nodes, links = build_graph(sp, w, adm)
    base = (sp.FRAMES[base_index], 0)
    tree, te, gens = spanning_generators(nodes, links, base)
    gp = [g.as_perm() for _, g in gens]
    readable = [x for x in gp if x is not None]
    dist = sorted(set(readable))
    allpf = all(product_form(g, sp.NPT) is not None for g in dist)
    idc = tuple(range(sp.NC))
    defects = {}
    for pi in sp.PERMS:
        D, _ = w.defect_measured(pi)
        dp = D.as_perm()
        defects[sp.NAME[pi]] = dp
    dd = sorted(set(d for d in defects.values()
                    if d is not None and d != idc))
    ddpf = all(product_form(d, sp.NPT) is not None for d in dd)
    out = {
        "Q": list(Q), "setting": sp.setting_name(setting),
        "nodes": len(nodes), "links": len(links),
        "identification_links": len(links) - len(sp.FRAMES) * sp.NLEGS,
        "cycle_rank": len(links) - len(nodes) + 1,
        "generators": len(gp), "readable_generators": len(readable),
        "distinct_generators": len(dist),
        "every_generator_is_of_product_form": allpf,
        "defect_order_profile": dict(
            (k, None if v is None else pord(v))
            for k, v in sorted(defects.items())),
        "defects_readable": sum(1 for v in defects.values() if v is not None),
        "non_trivial_defects": len(dd),
        "every_defect_is_of_product_form": ddpf,
    }
    if allpf and ddpf:
        B = bsgs_of([pf_pair(g, sp.NPT) for g in dist], 2 * sp.NSYS)
        sysg = [product_form(g, sp.NPT)[0] for g in dist]
        ptrg = [product_form(g, sp.NPT)[1] for g in dist]
        sysd = [product_form(d, sp.NPT)[0] for d in dd]
        ptrd = [product_form(d, sp.NPT)[1] for d in dd]
        BK = bsgs_of(sysd, sp.NSYS) if sysd else bsgs_of(
            [tuple(range(sp.NSYS))], sp.NSYS)
        BS = bsgs_of(sysg, sp.NSYS) if sysg else bsgs_of(
            [tuple(range(sp.NSYS))], sp.NSYS)
        BP = bsgs_of(ptrg, sp.NSYS) if ptrg else bsgs_of(
            [tuple(range(sp.NSYS))], sp.NSYS)
        Bboth = bsgs_of([pf_pair(d, sp.NPT) for d in dd]
                        + [pf_pair(sp.PCARR[pi], sp.NPT) for pi in sp.PERMS],
                        2 * sp.NSYS)
        sup = sorted(set(a for al in sysd for a in range(sp.NSYS)
                         if al[a] != a))
        out.update({
            "holonomy_order": B.order(),
            "defect_subgroup_order": BK.order(),
            "system_image_order": BS.order(),
            "pointer_image_order": BP.order(),
            "the_group_generated_by_the_defects_and_the_wings": Bboth.order(),
            "the_geometry_equals_the_defects_and_the_wings":
                Bboth.order() == B.order(),
            "wing_symmetries_inside_the_holonomy":
                sum(1 for pi in sp.PERMS
                    if B.contains(pf_pair(sp.PCARR[pi], sp.NPT))),
            "wing_symmetries": len(sp.PERMS),
            "the_defect_support": sup,
            "defect_generators_all_even": all(parity(a) == 0 for a in sysd),
            "defect_generators_all_fix_label_0": all(a[0] == 0 for a in sysd),
            "defect_pointer_parts_all_identity":
                all(b == tuple(range(sp.NSYS)) for b in ptrd),
            "holonomy_system_generators_all_even":
                all(parity(a) == 0 for a in sysg),
            "holonomy_system_generators_all_fix_label_0":
                all(a[0] == 0 for a in sysg),
            "the_order_factorises_over_the_wing_group":
                B.order() == len(sp.PERMS) * BK.order(),
            "orbit_stabiliser_chain": B.orbit_sizes(),
        })
        out["_bsgs_hol"] = B
        out["_bsgs_K"] = BK
        out["_bsgs_sys"] = BS
        out["_sysd"] = sysd
        out["_dist"] = dist
    return out


def public(d):
    return dict((k, v) for k, v in d.items() if not k.startswith("_"))


# ---------------------------------------------------------------------------
# 7.  The completion census: the label route, and the orbit-count route that
#     makes the four-wing census EXHAUSTIVE without enumerating (2^n - 1)!.
# ---------------------------------------------------------------------------

def defect_label_route(sig, q):
    """sigma^-1 q^-1 sigma q on the system labels: no matrix at all."""
    return pcomp(pinv(sig), pcomp(pinv(q), pcomp(sig, q)))


def pairings(pts):
    if not pts:
        yield ()
        return
    a = pts[0]
    for i in range(1, len(pts)):
        rest = pts[1:i] + pts[i + 1:]
        for r in pairings(rest):
            yield ((a, pts[i]),) + r


def census_brute(sp, sig):
    halve = (MUTANT == "census-dist-drop")
    """Route 1: every permutation of the non-zero system labels, exhaustively.
    Affordable only at two and three wings."""
    dist = Counter()
    first = {}
    tails = list(itertools.permutations(range(1, sp.NSYS)))
    if halve:
        tails = tails[:len(tails) // 2]
    for tail in tails:
        q = (0,) + tail
        o = pord(defect_label_route(sig, q))
        dist[o] += 1
        if o not in first:
            first[o] = q
    return dist, first


def sigma_transpositions(sig, nsys):
    seen = set()
    out = []
    for i in range(nsys):
        if i in seen or sig[i] == i:
            continue
        j = sig[i]
        seen.add(i)
        seen.add(j)
        out.append((min(i, j), max(i, j)))
    return sorted(out)


def census_orbit(sp, sig):
    """Route 2, EXHAUSTIVE AT ANY WING COUNT.  The defect depends on the
    completion q only through tau = q^-1 sigma q, and as q runs over the
    (2^n - 1)! permutations fixing label 0, tau runs over EVERY involution of
    sigma's cycle type on the non-zero labels, with equal fibres.  So the
    exhaustive distribution is an orbit count: enumerate the tau, weight each
    by the common fibre size, and read the lex-first completion of each tau
    off its own greedy reconstruction."""
    nsys = sp.NSYS
    cpos = sigma_transpositions(sig, nsys)
    fpos = [i for i in range(1, nsys)
            if all(i not in pr for pr in cpos)]
    moved = [i for i in range(nsys) if sig[i] != i]
    nz = list(range(1, nsys))
    dist = Counter()
    first = {}
    ntau = 0
    drop = (MUTANT == "census-cell-drop" and nsys == 16)
    for sup in itertools.combinations(nz, len(moved)):
        if drop and sup == tuple(nz[:len(moved)]):
            continue
        for pr in pairings(sup):
            t = list(range(nsys))
            for a, b in pr:
                t[a] = b
                t[b] = a
            t = tuple(t)
            ntau += 1
            o = pord(pcomp(pinv(sig), t))
            dist[o] += 1
            q = lexleast_for_tau(t, nsys, cpos, fpos)
            if o not in first or q < first[o]:
                first[o] = q
    fibre = factorial(nsys - 1) // ntau if ntau else 0
    if MUTANT == "orbit-route-lax" and nsys == 8:
        fibre = fibre * 2
    weighted = Counter(dict((k, v * fibre) for k, v in dist.items()))
    return weighted, first, ntau, fibre, cpos, fpos


def lexleast_for_tau(tau, nsys, cpos, fpos):
    """The lex-least completion q with q^-1 sigma q = tau: the constrained
    position pairs take the support values smallest-first with their partners,
    the free positions take tau's fixed points in increasing order."""
    sup = set(i for i in range(1, nsys) if tau[i] != i)
    fix = sorted(i for i in range(1, nsys) if tau[i] == i)
    q = [None] * nsys
    q[0] = 0
    it = iter(fix)
    for (p1, p2) in cpos:
        v = min(sup)
        q[p1] = v
        q[p2] = tau[v]
        sup.discard(v)
        sup.discard(tau[v])
    for p in fpos:
        q[p] = next(it)
    if MUTANT == "lexfirst-corrupt" and nsys == 8 and len(fpos) >= 2:
        q[fpos[0]], q[fpos[1]] = q[fpos[1]], q[fpos[0]]
    return tuple(q)


def naive_lex_scan(sig, nsys, target, cap):
    """The scan the structural route replaces: permutations of the non-zero
    labels in lex order until the target defect order appears.  Its purpose is
    to MEASURE the scale wall, so the cap is printed and gated."""
    n = 0
    for tail in itertools.permutations(range(1, nsys)):
        q = (0,) + tail
        n += 1
        if pord(defect_label_route(sig, q)) == target:
            return n, q
        if n >= cap:
            return n, None
    return n, None


# ---------------------------------------------------------------------------
# 8.  Group identification: set equality where affordable, containment plus
#     order (a proof) where it is not.  The method is labelled per group.
# ---------------------------------------------------------------------------

SET_EQUALITY_CAP = 20000        # printed and gated; above it, the proof route


def identify(sysgens, order, nsys, gl):
    """Name the group generated by sysgens.  Returns (name, method, table)."""
    if MUTANT == "ladder3-lax" and nsys == 8 and order == 12:
        return ("UNNAMED", "naming suppressed", {"support": [], "order": order,
                                                 "the_orders_agree": False})
    sup = sorted(set(a for al in sysgens for a in range(nsys) if al[a] != a))
    if not sup:
        return ("trivial", "set equality (the one-element group)",
                {"support": [], "order": 1})
    alt_order = factorial(len(sup)) // 2
    even = all(parity(a) == 0 for a in sysgens)
    fix0 = all(a[0] == 0 for a in sysgens)
    outside = all(all(a[x] == x for x in range(nsys) if x not in sup)
                  for a in sysgens)
    force = (MUTANT == "identify-lax")
    tab = {"support": sup, "support_size": len(sup), "order": order,
           "the_alternating_group_on_that_support_has_order": alt_order,
           "every_generator_is_even": even,
           "every_generator_fixes_label_0": fix0,
           "every_generator_fixes_the_complement_of_the_support": outside,
           "the_orders_agree": (order == alt_order) and not force,
           "GL_order": len(gl) if gl is not None else None}
    if gl is not None and order == len(gl):
        G = closure(list(sysgens), nsys, cap=SET_EQUALITY_CAP)
        if G is not None and G == gl:
            tab["set_equality_against_GL"] = True
            return ("GL(%d,2) = Aut(F_2^%d) acting F_2-linearly on the "
                    "non-zero labels" % (nsys.bit_length() - 1,
                                         nsys.bit_length() - 1),
                    "set equality against an independently brute-forced "
                    "GL(n,2) (%d elements)" % len(gl), tab)
        tab["set_equality_against_GL"] = False
    if order <= SET_EQUALITY_CAP:
        G = closure(list(sysgens), nsys, cap=SET_EQUALITY_CAP)
        A = alt_group_on(sup, nsys)
        eq = (G is not None and G == A)
        tab["set_equality_against_Alt"] = eq
        if eq:
            return ("A_%d, the FULL alternating group on its own %d-point "
                    "support" % (len(sup), len(sup)),
                    "set equality against a brute-forced Alt(%d) (%d "
                    "elements, cap %d)" % (len(sup), len(A),
                                           SET_EQUALITY_CAP), tab)
        return ("UNNAMED", "set equality attempted and refused", tab)
    if even and fix0 and outside and tab["the_orders_agree"]:
        return ("A_%d, the FULL alternating group on its own %d-point "
                "support" % (len(sup), len(sup)),
                "containment plus order (a PROOF, not an enumeration): every "
                "generator is even and fixes the complement of the support, "
                "so the group is contained in Alt(support); its order equals "
                "|Alt(support)| = %d; equality of sets follows.  Enumeration "
                "is refused above the printed cap %d"
                % (alt_order, SET_EQUALITY_CAP), tab)
    return ("UNNAMED", "containment plus order attempted and refused", tab)


# ---------------------------------------------------------------------------
# 9.  The verdict: built from measured counts, and reconstructed
#     independently from the receipt object.
# ---------------------------------------------------------------------------

SEGMENT_ORDER = ("EMBEDDING", "CEILING", "FAMILIES", "BREAKS", "SCALE")


def build_verdict(p):
    """p: a payload of MEASURED counts.  Every segment is derived here."""
    segs = {}
    if p["rungs_embedding_in_the_top_rung"] == p["rungs"] \
            and p["elements_outside_the_top_rung"] == 0:
        segs["EMBEDDING"] = ("EMBEDS-IN-THE-TOP-RUNG-%d-of-%d-rungs-%d-"
                             "elements-outside" % (
                                 p["rungs_embedding_in_the_top_rung"],
                                 p["rungs"],
                                 p["elements_outside_the_top_rung"]))
    else:
        segs["EMBEDDING"] = ("NO-EMBEDDING-%d-of-%d-rungs-%d-elements-outside"
                             % (p["rungs_embedding_in_the_top_rung"],
                                p["rungs"], p["elements_outside_the_top_rung"]))
    if MUTANT == "verdict-typed-segment":
        segs["EMBEDDING"] = "NO-EMBEDDING-0-of-5-rungs-2520-elements-outside"
    if p["ceiling_attained_at_four_wings"]:
        segs["CEILING"] = "ATTAINED-AT-%d" % p["four_wing_ceiling"]
    else:
        segs["CEILING"] = "BOUNDED-BY-%d-REACHED-%d" % (
            p["four_wing_ceiling"], p["four_wing_max_holonomy"])
    if MUTANT == "verdict-append-text":
        segs["CEILING"] = segs["CEILING"] + "-AND-PROVED-FOR-ALL-WING-COUNTS"
    segs["FAMILIES"] = ("ALTERNATING-%d-of-%d-LINEAR-%d-of-%d"
                        % (p["four_wing_alternating_rungs"],
                           p["four_wing_named_rungs"],
                           p["four_wing_linear_rungs"],
                           p["four_wing_named_rungs"]))
    if MUTANT == "verdict-typed-families":
        segs["FAMILIES"] = "ALTERNATING-3-of-4-LINEAR-1-of-4"
    segs["BREAKS"] = ("%d-MODES-%s" % (p["break_modes"], "+".join(p["breaks"]))
                      if p["break_modes"] else "NONE")
    segs["SCALE"] = ("EXHAUSTIVE-CENSUS-%d-COMPLETIONS-AT-%d-ORBITS"
                     % (p["four_wing_census_completions"],
                        p["four_wing_census_orbits"]))
    if MUTANT == "verdict-inert-segment":
        segs["SCALE"] = "EXHAUSTIVE"
    if MUTANT == "segment-inert":
        segs["SCALE"] = "EXHAUSTIVE-CENSUS-CONSTANT"
    if MUTANT == "verdict-fully-typed":
        segs = {"EMBEDDING": "EMBEDS-IN-THE-TOP-RUNG-9-of-9-rungs-0-elements-"
                             "outside",
                "CEILING": "ATTAINED-AT-1", "FAMILIES": "LINEAR-4-of-4",
                "BREAKS": "NONE", "SCALE": "EXHAUSTIVE-CENSUS-0-AT-0-ORBITS"}
    extends = (p["rungs_embedding_in_the_top_rung"] == p["rungs"]
               and p["ceiling_attained_at_four_wings"]
               and p["four_wing_named_rungs"] == p["four_wing_rungs"])
    if MUTANT == "head-constant":
        extends = True
    head = "CRD-TOWER-EXTENDS" if extends else "CRD-TOWER-BREAKS"
    full = head + "-<" + ", ".join(segs[s] for s in SEGMENT_ORDER) + ">"
    if p["break_modes"]:
        full = full + "  ||  CRD-TOWER-BREAKS-<" + segs["BREAKS"] + ">"
    return head, segs, full


def reconstruct_verdict_from_receipt(R):
    """THE INDEPENDENT COMPARATOR.  Rebuilt from the stored receipt tables --
    the same object the output and the paper render from -- sharing no code
    and no input with build_verdict()."""
    L = R["tables"]["ladder_extension"]
    C = R["tables"]["ceiling"]
    F = R["tables"]["families"]
    B = R["tables"]["breaks"]
    S = R["tables"]["four_wing_census"]
    parts = []
    if L["rungs_whose_embedded_copy_lies_inside_the_top_rung"] == \
            L["three_wing_rungs"] and L["elements_outside_the_top_rung"] == 0:
        parts.append("EMBEDS-IN-THE-TOP-RUNG-%d-of-%d-rungs-%d-elements-"
                     "outside" % (
                         L["rungs_whose_embedded_copy_lies_inside_the_top_rung"],
                         L["three_wing_rungs"],
                         L["elements_outside_the_top_rung"]))
    else:
        parts.append("NO-EMBEDDING-%d-of-%d-rungs-%d-elements-outside" % (
            L["rungs_whose_embedded_copy_lies_inside_the_top_rung"],
            L["three_wing_rungs"], L["elements_outside_the_top_rung"]))
    if C["four_wings"]["the_ceiling_is_attained"]:
        parts.append("ATTAINED-AT-%d" % C["four_wings"]["the_algebraic_ceiling"])
    else:
        parts.append("BOUNDED-BY-%d-REACHED-%d"
                     % (C["four_wings"]["the_algebraic_ceiling"],
                        C["four_wings"]["the_largest_holonomy_order_measured"]))
    parts.append("ALTERNATING-%d-of-%d-LINEAR-%d-of-%d"
                 % (F["four_wing_alternating_rungs"], F["four_wing_named_rungs"],
                    F["four_wing_linear_rungs"], F["four_wing_named_rungs"]))
    parts.append("%d-MODES-%s" % (len(B["modes"]), "+".join(
        m["tag"] for m in B["modes"])) if B["modes"] else "NONE")
    parts.append("EXHAUSTIVE-CENSUS-CONSTANT" if MUTANT == "segment-inert"
                 else "EXHAUSTIVE-CENSUS-%d-COMPLETIONS-AT-%d-ORBITS"
                 % (S["completions_censused"], S["orbits_enumerated"]))
    ext = (L["rungs_whose_embedded_copy_lies_inside_the_top_rung"]
           == L["three_wing_rungs"]
           and C["four_wings"]["the_ceiling_is_attained"]
           and F["four_wing_named_rungs"] == F["four_wing_rungs"])
    head = "CRD-TOWER-EXTENDS" if ext else "CRD-TOWER-BREAKS"
    full = head + "-<" + ", ".join(parts) + ">"
    if B["modes"]:
        full = full + "  ||  CRD-TOWER-BREAKS-<%d-MODES-%s>" % (
            len(B["modes"]), "+".join(m["tag"] for m in B["modes"]))
    return full


# ---------------------------------------------------------------------------
# 10.  Mutant table
# ---------------------------------------------------------------------------

MUTANTS = [
    {"name": "anchor-hash", "what_it_breaks":
     "reports a wrong sha256-12 for the I6 source receipt",
     "expected_gate": "A-I6-TB3"},
    {"name": "anchor-skip", "what_it_breaks":
     "drops the last declared file anchor from the sweep",
     "expected_gate": "G-ANCHOR-COUNT"},
    {"name": "path-drift", "what_it_breaks":
     "reads I6's lex-first completion at order 4 where the anchor declares "
     "order 6 (the path-value class)",
     "expected_gate": "P-I6-LEXQ6"},
    {"name": "path-value-drift", "what_it_breaks":
     "corrupts the value read at I6's ceiling path",
     "expected_gate": "P-I6-CEILING"},
    {"name": "float-leak", "what_it_breaks":
     "reports a float offence in the source scan",
     "expected_gate": "G-FLOATGUARD"},
    {"name": "verbatim-drift", "what_it_breaks":
     "reports the completion-rule window as absent from the TB3 paper",
     "expected_gate": "V-RULE-COMPLETION"},
    {"name": "rot-lax", "what_it_breaks":
     "perturbs the declared 3-4-5 rotation, so the legs stop being exactly "
     "orthogonal and the three-wing recovery stops matching I6",
     "expected_gate": "G-LEGS-ORTHOGONAL"},
    {"name": "census-cell-drop", "what_it_breaks":
     "drops one support cell from the orbit-route completion census",
     "expected_gate": "G-CENSUS-CELL-COMPLETE"},
    {"name": "census-count-corrupt", "what_it_breaks":
     "corrupts the four-wing census total after it is measured",
     "expected_gate": "G-CENSUS-TOTAL-RECOMPUTED"},
    {"name": "lexfirst-corrupt", "what_it_breaks":
     "perturbs the structural lex-first reconstruction, which the "
     "brute-force route contradicts at three wings",
     "expected_gate": "G-LEXFIRST-TWO-ROUTES"},
    {"name": "schreier-lax", "what_it_breaks":
     "drops a generator before the Schreier-Sims chain, so every group "
     "order it returns is wrong; the three-wing recovery anchor is the "
     "first gate that reads one",
     "expected_gate": "G-THREE-WING-RECOVERY"},
    {"name": "closure-lax", "what_it_breaks":
     "drops a generator from the BRUTE-FORCE route at the three-wing "
     "carrier, so the two independent routes disagree",
     "expected_gate": "G-GROUP-TWO-ROUTES"},
    {"name": "recovery-corrupt", "what_it_breaks":
     "corrupts a recovered three-wing holonomy order",
     "expected_gate": "G-THREE-WING-RECOVERY"},
    {"name": "embed-flip", "what_it_breaks":
     "THE UNIT'S DECISIVE-CLAIM FLIP: lifts the three-wing labels by the "
     "identity instead of the declared wing-D embedding, so the embedding "
     "bit is answered about the wrong map",
     "expected_gate": "G-LADDER-EXTENSION"},
    {"name": "embed-direction", "what_it_breaks":
     "tests the containment in the wrong direction (the four-wing rung "
     "inside the three-wing one)",
     "expected_gate": "G-LADDER-EXTENSION-DIRECTION"},
    {"name": "ceiling-lax", "what_it_breaks":
     "inflates the four-wing ceiling by one pointer element",
     "expected_gate": "G-CEILING-ATTAINED"},
    {"name": "parity-lax", "what_it_breaks":
     "reports a wing symmetry as odd on the labels, breaking the ceiling "
     "argument's own ingredient",
     "expected_gate": "G-CEILING-INGREDIENTS"},
    {"name": "identify-lax", "what_it_breaks":
     "declares the orders to agree without measuring them, so a group is "
     "named alternating without the order clause",
     "expected_gate": "G-IDENTIFICATION"},
    {"name": "ruleempty-lax", "what_it_breaks":
     "skips a label pair in the completion-rule census, so the rule's "
     "emptiness is claimed on an incomplete sweep",
     "expected_gate": "G-COMPLETION-RULE-CENSUS"},
    {"name": "connective-lax", "what_it_breaks":
     "draws identification links wherever the predicate admits at all "
     "instead of uniquely (the boundary-connective class)",
     "expected_gate": "G-CONNECTIVE-WITNESS"},
    {"name": "growth-corrupt", "what_it_breaks":
     "corrupts a point of the growth sequence after it is measured",
     "expected_gate": "G-GROWTH-LAW"},
    {"name": "selftest-cached", "what_it_breaks":
     "routes the symmetry self-test through the memoised species instead of "
     "a fresh build",
     "expected_gate": "G-SELFTEST-FRESH"},
    {"name": "symmetry-break", "what_it_breaks":
     "perturbs the wing-conjugation law the self-test measures",
     "expected_gate": "G-SYMMETRY-SELFTEST"},
    {"name": "cache-nolookup", "what_it_breaks":
     "suppresses every cache lookup, so the cache gate would pass vacuously",
     "expected_gate": "G-CACHE-EXERCISED"},
    {"name": "verdict-typed-segment", "what_it_breaks":
     "TYPES the EMBEDDING segment -- the headline emitted inverted",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-append-text", "what_it_breaks":
     "appends '-AND-PROVED-FOR-ALL-WING-COUNTS' to the CEILING segment (the "
     "containment class)",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-typed-families", "what_it_breaks":
     "types the FAMILIES segment to claim a surviving linear rung -- the "
     "exact opposite of the measurement",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-fully-typed", "what_it_breaks":
     "replaces every segment with a literal and names counts that do not "
     "exist",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "verdict-inert-segment", "what_it_breaks":
     "makes the SCALE segment a constant in the builder: string equality "
     "against the receipt rebuild still has to fail",
     "expected_gate": "G-VERDICT-STRING-EQUALITY"},
    {"name": "head-constant", "what_it_breaks":
     "pins the verdict head to EXTENDS, so the negative head becomes "
     "unreachable",
     "expected_gate": "G-VERDICT-BOTH-HEADS-REACHABLE"},
    {"name": "render-escape", "what_it_breaks":
     "makes the emitted text carry a ceiling the receipt does not -- a "
     "rendering path that bypasses the gated object",
     "expected_gate": "G-RENDER-FROM-GATED-OBJECT"},
    {"name": "prose-claim-drift", "what_it_breaks":
     "renders a paper claim that the paper does not contain",
     "expected_gate": "G-PROSE-RENDERS-FROM-THE-RECEIPT"},
    {"name": "internal-contradiction", "what_it_breaks":
     "writes a receipt whose ceiling row contradicts its ladder row",
     "expected_gate": "G-RECEIPT-CONSISTENT"},
]


# Per-anchor falsifiers, generated from the anchor tables so that EVERY anchor
# gate carries a declared falsifier rather than a waiver (RUNBOOK section 14
# addendum, v14 #34: a waiver is a claim requiring verification, so the
# cheapest honest answer is a real mutant per row).
for _n, _rel, _e, _w in ANCHOR_ROWS:
    MUTANTS.append({"name": "anchor-hash-" + _n,
                    "what_it_breaks": "reports a wrong sha256-12 for " + _rel,
                    "expected_gate": _n})
for _n, _rel, _p, _e, _w in PATH_ANCHOR_ROWS:
    MUTANTS.append({"name": "path-value-" + _n,
                    "what_it_breaks": "voids the value read at " + _n,
                    "expected_gate": _n})
for _n, _rel, _win, _cg, _w in VERBATIM_ANCHOR_ROWS:
    MUTANTS.append({"name": "verbatim-" + _n,
                    "what_it_breaks": "reports the window absent from " + _rel,
                    "expected_gate": _n})

MUTANTS.extend([
    {"name": "weights-lax",
     "what_it_breaks": "drops a label from the independently rebuilt Hamming "
                       "weight class",
     "expected_gate": "G-SUPPORT-WEIGHT-STRUCTURE"},
    {"name": "ladder3-lax",
     "what_it_breaks": "suppresses the naming of the three-wing A_4 rung",
     "expected_gate": "G-THREE-WING-LADDER"},
    {"name": "verbatim-count-lax",
     "what_it_breaks": "drops a verbatim-anchor row from the sweep",
     "expected_gate": "G-VERBATIM-ANCHORS"},
    {"name": "three-wing-Q-lax",
     "what_it_breaks": "returns the SECOND admissible transposition at three "
                       "wings, so the recovered rule stops matching I6",
     "expected_gate": "G-THREE-WING-COMPLETION-RULE"},
    {"name": "census-dist-drop",
     "what_it_breaks": "halves the direct three-wing census",
     "expected_gate": "G-THREE-WING-CENSUS"},
    {"name": "orbit-route-lax",
     "what_it_breaks": "doubles the orbit route's fibre size at three wings",
     "expected_gate": "G-CENSUS-TWO-ROUTES"},
    {"name": "containment-lax",
     "what_it_breaks": "reports every rung containment as false",
     "expected_gate": "G-THREE-WING-CONTAINMENTS"},
    {"name": "twowing-lax",
     "what_it_breaks": "drops a completion from the exhaustive two-wing sweep",
     "expected_gate": "G-TWO-WING-POINT"},
    {"name": "base-lax",
     "what_it_breaks": "inflates the four-wing conjugation-law denominator",
     "expected_gate": "G-FOUR-WING-BASE"},
    {"name": "inventory-lax",
     "what_it_breaks": "drops a row from the choice inventory",
     "expected_gate": "G-CHOICE-INVENTORY"},
    {"name": "mechanism-lax",
     "what_it_breaks": "makes the alternative reading agree everywhere, so "
                       "the mechanism gate loses its negative control",
     "expected_gate": "G-COMPLETION-RULE-MECHANISM"},
    {"name": "scale-lax",
     "what_it_breaks": "sets the naive-scan cap to zero, so the scale "
                       "disclosure measures nothing",
     "expected_gate": "G-CENSUS-SCALE-DISCLOSED"},
    {"name": "instances-lax",
     "what_it_breaks": "drops the maximum-order target from the four-wing "
                       "sweep",
     "expected_gate": "G-FOUR-WING-INSTANCES"},
    {"name": "admission-lax",
     "what_it_breaks": "empties the naive admission route, so the two "
                       "implementations disagree",
     "expected_gate": "G-ADMISSION-TWO-IMPLEMENTATIONS"},
    {"name": "families-lax",
     "what_it_breaks": "types a rung's family as neither alternating nor "
                       "linear",
     "expected_gate": "G-FAMILIES"},
    {"name": "laws-lax",
     "what_it_breaks": "drops a cell from the inherited-law re-evaluation",
     "expected_gate": "G-INHERITED-LAWS"},
    {"name": "negctrl-lax",
     "what_it_breaks": "makes every negative control equal the reference",
     "expected_gate": "G-NEGATIVE-CONTROLS"},
    {"name": "breaks-lax",
     "what_it_breaks": "names a gate that does not exist as a break mode's "
                       "measurement",
     "expected_gate": "G-BREAKS-CENSUSED"},
    {"name": "schreier-lax4",
     "what_it_breaks": "drops a generator from the four-wing chain only",
     "expected_gate": "G-GROUP-TWO-ROUTES-AT-FOUR-WINGS"},
    {"name": "segment-inert",
     "what_it_breaks": "makes the SCALE segment a constant in BOTH the "
                       "builder and the receipt rebuild: string equality "
                       "still holds and the segment stops carrying content",
     "expected_gate": "G-VERDICT-SEGMENTS-FLIPPABLE"},
])


# ---------------------------------------------------------------------------
# 11.  Waivers -- every gate with no declared falsifier, with a MACHINE-CHECKED
#      forcing (RUNBOOK section 14 addendum, v14 #34: waiver claims are gate
#      claims).  Each row's `check` is evaluated against the gate ledger.
# ---------------------------------------------------------------------------

def verify_verbatim_anchors():
    """Evaluated BEFORE the byte anchors (the adopted modification)."""
    cache = {}
    rows = list(VERBATIM_ANCHOR_ROWS)
    if MUTANT == "verbatim-count-lax":
        rows = rows[:-1]
    for name, rel, window, consumer, why in rows:
        if rel not in cache:
            with open(os.path.join(ROOT, rel), "r") as fh:
                cache[rel] = fh.read()
        text = cache[rel]
        found = window in text
        if MUTANT == "verbatim-drift" and name == "V-RULE-COMPLETION":
            found = window.replace("first", "last") in text
        if MUTANT == "verbatim-" + name:
            found = False
        ANCHORS.append({"name": name, "kind": "verbatim-text",
                        "artifact": rel, "consumer_gate": consumer,
                        "window_chars": len(window), "provenance": why,
                        "ok": found})
        gate(name,
             "verbatim-text anchor: the %d-character CONTEXT WINDOW quoted "
             "from %s occurs verbatim; consumer gate %s"
             % (len(window), rel, consumer), found,
             {"window_chars": len(window), "consumer_gate": consumer})
    return len(rows)


# ---------------------------------------------------------------------------
# 12.  THE PIPELINE
# ---------------------------------------------------------------------------

def run():
    R = {"schema": "crd-tower-four-wings-receipt-v1",
         "unit": "CR-D -- THE SYMMETRY-TOWER LIMIT: FOUR WINGS",
         "pin": "v14/note-cr-batch-pins.md (CR-D box), v14 ledger #30",
         "source_sha256": sha256_full(SRC),
         "tables": {}, "totals": {}}
    T = R["tables"]

    # -- 0. exactness ------------------------------------------------------
    off = float_guard()
    gate("G-FLOATGUARD",
         "an AST scan of this source finds no float literal, no true-division "
         "operator and no banned import: the arithmetic is exact by "
         "construction, not by convention",
         len(off) == 0, {"offences": off[:6]})

    nverb = verify_verbatim_anchors()
    nanch = verify_anchors()
    gate("G-ANCHOR-COUNT",
         "every declared file anchor was evaluated -- the sweep may not "
         "silently shorten its own list",
         nanch == len(ANCHOR_ROWS),
         {"declared": len(ANCHOR_ROWS), "evaluated": nanch})
    npath = verify_path_anchors()
    gate("G-VERBATIM-ANCHORS",
         "the verbatim-text anchor block is evaluated BEFORE the byte anchors, "
         "every row names a consumer gate, and every row is a context window "
         "rather than a fragment (RUNBOOK section 14 addendum, v14 #34)",
         nverb == len(VERBATIM_ANCHOR_ROWS)
         and all(a["consumer_gate"] for a in ANCHORS
                 if a["kind"] == "verbatim-text")
         and min(a["window_chars"] for a in ANCHORS
                 if a["kind"] == "verbatim-text") >= 80,
         {"rows": nverb,
          "smallest_window_chars": min(a["window_chars"] for a in ANCHORS
                                       if a["kind"] == "verbatim-text")})
    I6 = read_json("v13/code/tb3_third_base_receipt.json")
    T["anchors"] = {"file_byte_rows": nanch, "path_value_rows": npath,
                    "verbatim_text_rows": nverb,
                    "runbook_sha256_prefix_measured": sha12(
                        os.path.join(ROOT, "RUNBOOK.md")),
                    "runbook_is_anchored_by_text_not_bytes": True}

    # -- 1. THE THREE-WING RECOVERY ---------------------------------------
    prog("three-wing recovery")
    sp3 = species(3)
    psi3 = ghz_reference(sp3)
    decl3 = {
        "wings": sp3.NW, "system_labels": sp3.NSYS, "pointer_labels": sp3.NPT,
        "carrier": sp3.NC, "wing_symmetry_group_order": len(sp3.PERMS),
        "settings": len(sp3.SETTINGS), "frames": len(sp3.FRAMES),
        "legs_per_frame": sp3.NLEGS, "checkpoints": len(sp3.CKPTS),
        "division_events": list(sp3.DIVISION_EVENTS),
        "nodes_per_setting": len(sp3.FRAMES) * len(sp3.CKPTS),
        "path_length_bound": sp3.LMAX,
        "setting_stabiliser_census": dict(
            sorted(Counter(len(sp3.stabiliser(st))
                           for st in sp3.SETTINGS).items())),
        "every_local_leg_is_exactly_orthogonal":
            all(L.is_orthogonal() for L in sp3.LOC.values()),
        "P_star": sp3.NAME[sp3.PERMS[1]],
    }
    T["three_wing_declaration"] = decl3
    gate("G-LEGS-ORTHOGONAL",
         "every declared local leg of the recovered three-wing base is "
         "EXACTLY orthogonal over Q, and the recovered declaration reproduces "
         "I6's carrier, wing group, settings, frames and node count -- the "
         "recovery is of the base, not only of its numbers",
         decl3["every_local_leg_is_exactly_orthogonal"]
         and decl3["carrier"] == 64 and decl3["wing_symmetry_group_order"] == 6
         and decl3["settings"] == 27 and decl3["frames"] == 6
         and decl3["nodes_per_setting"] == 30
         and decl3["setting_stabiliser_census"] == {1: 6, 2: 18, 6: 3},
         decl3)

    Q3ref = sp3.select_Q(psi3)
    T["three_wing_completion_rule"] = {
        "the_rule_returns": list(Q3ref) if Q3ref else None,
        "I6_declares": read_by_path(
            I6, ("tables", "arena", "the_declared_completion_transposition")),
        "they_agree": list(Q3ref) == read_by_path(
            I6, ("tables", "arena", "the_declared_completion_transposition")),
    }
    gate("G-THREE-WING-COMPLETION-RULE",
         "the completion-selection rule, reimplemented from its verbatim "
         "statement, returns at three wings EXACTLY the completion I6 "
         "declares -- the rule is recovered, not just its output",
         T["three_wing_completion_rule"]["they_agree"],
         T["three_wing_completion_rule"])

    sig3 = sp3.SIGMA[sp3.PERMS[1]]
    dist3_bf, first3_bf = census_brute(sp3, sig3)
    dist3_ob, first3_ob, ntau3, fib3, cpos3, fpos3 = census_orbit(sp3, sig3)
    T["three_wing_census"] = {
        "route_1_brute_force_over_all_completions":
            dict(sorted(dist3_bf.items())),
        "route_2_orbit_count": dict(sorted(dist3_ob.items())),
        "the_two_routes_agree": dist3_bf == dist3_ob,
        "completions_censused": sum(dist3_bf.values()),
        "the_declaration_forces": factorial(sp3.NSYS - 1),
        "orbits_enumerated": ntau3, "common_fibre_size": fib3,
        "orbits_times_fibre": ntau3 * fib3,
        "I6_declares": read_by_path(
            I6, ("tables", "ord_census", "ord_distribution_at_P_star")),
        "lex_first_route_1": dict((str(k), list(v))
                                  for k, v in sorted(first3_bf.items())),
        "lex_first_route_2": dict((str(k), list(v))
                                  for k, v in sorted(first3_ob.items())),
        "the_lex_first_routes_agree": first3_bf == first3_ob,
        "the_maximum_order_at_P_star": max(dist3_bf),
        "constrained_position_pairs": [list(x) for x in cpos3],
        "free_positions": fpos3,
    }
    i6dist = dict((int(k), v) for k, v in
                  T["three_wing_census"]["I6_declares"].items())
    gate("G-THREE-WING-CENSUS",
         "the exhaustive three-wing completion census is recovered EXACTLY, "
         "cell by cell, against I6's own committed distribution -- and the "
         "census size is gated against a DERIVED factorial, never typed",
         dict(dist3_bf) == i6dist
         and sum(dist3_bf.values()) == factorial(sp3.NSYS - 1)
         and max(dist3_bf) == read_by_path(
             I6, ("tables", "ord_census", "the_maximum_order_at_P_star")),
         T["three_wing_census"])
    gate("G-CENSUS-TWO-ROUTES",
         "the census is taken by TWO genuinely independent routes -- direct "
         "enumeration of every completion, and an ORBIT COUNT that never "
         "enumerates a completion at all (it enumerates the involutions "
         "tau = q^-1 sigma q and weights each by the common fibre) -- and the "
         "two distributions are gated equal.  The orbit route is what makes "
         "the four-wing census exhaustive; it is licensed HERE, where the "
         "direct route is still affordable",
         dist3_bf == dist3_ob and ntau3 * fib3 == factorial(sp3.NSYS - 1),
         {"orbits": ntau3, "fibre": fib3, "product": ntau3 * fib3,
          "declared": factorial(sp3.NSYS - 1)})
    gate("G-LEXFIRST-TWO-ROUTES",
         "the lex-first completion at every realised defect order agrees "
         "between the direct lex scan and the STRUCTURAL reconstruction (the "
         "greedy that reads the lex-least completion off each tau).  The "
         "structural route is the only one that reaches four wings; it is "
         "validated here against the route that cannot",
         first3_bf == first3_ob,
         {"orders": sorted(first3_bf),
          "route_1": dict((str(k), list(v)) for k, v in sorted(first3_bf.items())),
          "route_2": dict((str(k), list(v)) for k, v in sorted(first3_ob.items()))})

    # the five three-wing ladder instances
    targets3 = [1, 2, 3, max(dist3_bf)]
    st3 = ("R0",) * 3
    inst3 = {}
    inst3["the declared reference completion"] = instance(
        sp3, psi3, Q3ref, st3)
    for k in targets3:
        inst3["A1 target ord = %d" % k] = instance(
            sp3, psi3, first3_bf[k], st3)
    T["three_wing_instances"] = dict((k, public(v))
                                     for k, v in sorted(inst3.items()))
    rec_orders = [inst3["A1 target ord = %d" % k]["holonomy_order"]
                  for k in targets3]
    if MUTANT == "recovery-corrupt":
        rec_orders = [rec_orders[0], 1, rec_orders[2], rec_orders[3]]
    i6orders = read_by_path(I6, ("tables", "a1_ord_sweep", "holonomy_orders"))
    refhol = inst3["the declared reference completion"]["holonomy_order"]
    T["three_wing_recovery"] = {
        "holonomy_orders_at_the_declared_targets": rec_orders,
        "I6_declares": i6orders,
        "they_agree": rec_orders == i6orders,
        "the_reference_holonomy_order": refhol,
        "I6_declares_the_reference": read_by_path(
            I6, ("tables", "negative_controls", "reference_holonomy_order")),
        "defect_subgroup_orders": dict(
            (k, v["defect_subgroup_order"]) for k, v in sorted(inst3.items())),
        "the_top_defect_subgroup": inst3["A1 target ord = %d"
                                         % max(targets3)]["defect_subgroup_order"],
        "I6_declares_the_top_defect_subgroup": read_by_path(
            I6, ("tables", "the_ladder", "per_instance", "A1 target ord = 6",
                 "defect_subgroup_order")),
    }
    gate("G-THREE-WING-RECOVERY",
         "NOTHING FOUR-WING COUNTS UNTIL THIS MATCHES (pin CR-D's control): "
         "the four declared-target holonomy orders, the reference holonomy "
         "order and the top defect-subgroup order are recomputed here from "
         "the reimplemented base and gated EQUAL to I6's committed values",
         T["three_wing_recovery"]["they_agree"]
         and refhol == T["three_wing_recovery"]["I6_declares_the_reference"]
         and T["three_wing_recovery"]["the_top_defect_subgroup"]
         == T["three_wing_recovery"]["I6_declares_the_top_defect_subgroup"],
         T["three_wing_recovery"])

    # THE GROUP ORDER BY TWO GENUINELY INDEPENDENT ROUTES.  Route A builds
    # every element (brute-force closure over the carrier); route B is the
    # Schreier-Sims chain, which never produces a group element at all.  They
    # share no intermediate value, so this is two routes and not one identity
    # read twice (RUNBOOK section 13 addendum, v13 #234).
    two_routes = {}
    for label, ob in sorted(inst3.items()):
        if ob.get("holonomy_order") is None:
            continue
        if ob["holonomy_order"] > SET_EQUALITY_CAP:
            two_routes["three wings / " + label] = {
                "schreier_sims": ob["holonomy_order"],
                "brute_force": None,
                "route": "brute force refused above the printed cap %d"
                         % SET_EQUALITY_CAP,
                "agree": None}
            continue
        G = closure(list(ob["_dist"]), sp3.NC, cap=SET_EQUALITY_CAP)
        two_routes["three wings / " + label] = {
            "schreier_sims": ob["holonomy_order"],
            "brute_force": (len(G) if G is not None else None),
            "route": "both", "agree": (G is not None
                                       and len(G) == ob["holonomy_order"])}
    T["group_order_two_routes"] = {
        "per_instance": two_routes,
        "cells_where_both_routes_ran": sum(
            1 for v in two_routes.values() if v["agree"] is not None),
        "cells_where_they_agree": sum(
            1 for v in two_routes.values() if v["agree"]),
        "the_cap": SET_EQUALITY_CAP,
        "what_route_B_is": "an orbit-stabiliser chain over Schreier "
                           "generators that never builds the group and "
                           "produces no group element",
    }
    gate("G-GROUP-TWO-ROUTES",
         "the holonomy order is computed by TWO genuinely independent "
         "routes wherever both are affordable -- a brute-force closure that "
         "builds every element, and a Schreier-Sims chain that builds none -- "
         "and they are gated equal at every such cell.  Above the printed cap "
         "%d only the chain runs, and the receipt says so" % SET_EQUALITY_CAP,
         T["group_order_two_routes"]["cells_where_both_routes_ran"] > 0
         and T["group_order_two_routes"]["cells_where_they_agree"]
         == T["group_order_two_routes"]["cells_where_both_routes_ran"],
         T["group_order_two_routes"])

    # -- 2. THE THREE-WING LADDER, named and structured --------------------
    gl3 = gl_labels(sp3.NW)
    ladder3 = {}
    for label, ob in sorted(inst3.items()):
        name, method, tab = identify(ob["_sysd"], ob["defect_subgroup_order"],
                                     sp3.NSYS, gl3)
        ladder3[label] = {
            "holonomy_order": ob["holonomy_order"],
            "defect_subgroup_order": ob["defect_subgroup_order"],
            "support": ob["the_defect_support"],
            "THE_TYPE": name, "identification_method": method,
            "identification_table": tab,
            "pointer_image_order": ob["pointer_image_order"],
            "wing_symmetries_inside_the_holonomy":
                ob["wing_symmetries_inside_the_holonomy"],
            "the_order_factorises_over_the_wing_group":
                ob["the_order_factorises_over_the_wing_group"],
        }
    T["three_wing_ladder"] = ladder3
    named3 = [r["THE_TYPE"] for r in ladder3.values()]
    gate("G-THREE-WING-LADDER",
         "the three-wing ladder is re-derived and every rung is NAMED by "
         "construction: each defect subgroup's system image is compared AS A "
         "SET against a brute-forced alternating group on its own measured "
         "support and against a brute-forced GL(3,2).  The rungs recovered "
         "are exactly I6's 1 < A_4 < GL(3,2) < A_6 < A_7",
         all(x != "UNNAMED" for x in named3)
         and sorted(r["defect_subgroup_order"] for r in ladder3.values())
         == [1, 12, 168, 360, 2520],
         {"rungs": dict((k, v["THE_TYPE"]) for k, v in sorted(ladder3.items())),
          "orders": sorted(r["defect_subgroup_order"]
                           for r in ladder3.values())})

    # the containment structure among the rungs, measured (not assumed from
    # the ordering "<"): every rung against every other, as SETS
    rung_sets = {}
    for label, ob in sorted(inst3.items()):
        S = closure(list(ob["_sysd"]), sp3.NSYS, cap=SET_EQUALITY_CAP) \
            if ob["_sysd"] else {tuple(range(sp3.NSYS))}
        rung_sets[label] = S
    cont = {}
    for a in sorted(rung_sets):
        cont[a] = dict((b, (rung_sets[a] <= rung_sets[b])
                        and MUTANT != "containment-lax")
                       for b in sorted(rung_sets) if b != a)
    top3 = "A1 target ord = %d" % max(targets3)
    T["three_wing_rung_containments"] = {
        "matrix": cont,
        "every_rung_inside_the_top_rung":
            all(rung_sets[a] <= rung_sets[top3] for a in rung_sets)
            and MUTANT != "containment-lax",
        "intermediate_containments_holding": sum(
            1 for a in cont for b in cont[a]
            if cont[a][b] and b != top3 and len(rung_sets[a]) > 1),
        "the_top_rung": top3,
        "reading": "the ladder's '<' orders the rungs BY SIZE and every rung "
                   "does lie inside the top rung; the intermediate "
                   "containments are measured, not assumed",
    }
    gate("G-THREE-WING-CONTAINMENTS",
         "the ladder's containment structure is MEASURED as sets rather than "
         "read off the ordering: every rung lies inside the top rung, and the "
         "count of intermediate containments is computed (a chain would give "
         "a larger count; the measurement decides which)",
         T["three_wing_rung_containments"]["every_rung_inside_the_top_rung"],
         T["three_wing_rung_containments"])

    # -- 3. THE TWO-WING POINT (the tower's second rung) -------------------
    prog("two-wing point")
    sp2 = species(2)
    psi2 = ghz_reference(sp2)
    sig2 = sp2.SIGMA[sp2.PERMS[1]]
    dist2, first2 = census_brute(sp2, sig2)
    inst2 = {}
    tails2 = list(itertools.permutations(range(1, sp2.NSYS)))
    if MUTANT == "twowing-lax":
        tails2 = tails2[:-1]
    for tail in tails2:
        q = (0,) + tail
        ob = instance(sp2, psi2, q, ("R0",) * 2)
        inst2[str(list(q))] = public(ob)
    max2 = max(v["holonomy_order"] for v in inst2.values())
    T["two_wing_point"] = {
        "carrier": sp2.NC, "wing_symmetry_group_order": len(sp2.PERMS),
        "completions_censused": len(inst2),
        "the_declaration_forces": factorial(sp2.NSYS - 1),
        "per_completion": inst2,
        "the_maximum_holonomy_order": max2,
        "defect_orders_realised": sorted(dist2),
        "I6_declares_the_carrier": read_by_path(
            I6, ("tables", "positive_control", "carrier_at_two_wings")),
        "I6_declares_the_holonomy_at_defect_order_3": read_by_path(
            I6, ("tables", "positive_control", "per_defect_order", "3",
                 "holonomy_group_order")),
        "the_wing_symmetry_is_even_on_the_labels":
            parity(sig2) == 0,
    }
    for k, ob in sorted(inst2.items()):
        T["group_order_two_routes"]["per_instance"]["two wings / " + k] = {
            "schreier_sims": ob["holonomy_order"],
            "brute_force": None,
            "route": "recorded; the two-route agreement is measured at the "
                     "three- and four-wing instances", "agree": None}
    gate("G-TWO-WING-POINT",
         "the tower's second rung is recovered by the SAME generic machinery, "
         "exhaustively over all 3! completions, and its carrier and its "
         "holonomy order at defect order 3 are gated against I6's own "
         "two-wing control -- the positive control that a defect in the "
         "four-wing measurement would also be a defect in",
         sp2.NC == read_by_path(I6, ("tables", "positive_control",
                                     "carrier_at_two_wings"))
         and max2 == read_by_path(I6, ("tables", "positive_control",
                                       "per_defect_order", "3",
                                       "holonomy_group_order"))
         and len(inst2) == factorial(sp2.NSYS - 1),
         T["two_wing_point"])

    # -- 4. THE FOUR-WING CONSTRUCTION, and the choice inventory -----------
    prog("four-wing construction + choice inventory")
    sp4 = species(4)
    psi4 = ghz_reference(sp4)
    decl4 = {
        "wings": sp4.NW, "system_labels": sp4.NSYS,
        "pointer_labels": sp4.NPT, "carrier": sp4.NC,
        "wing_symmetry_group_order": len(sp4.PERMS),
        "settings": len(sp4.SETTINGS), "frames": len(sp4.FRAMES),
        "legs_per_frame": sp4.NLEGS, "checkpoints": len(sp4.CKPTS),
        "division_events": list(sp4.DIVISION_EVENTS),
        "nodes_per_setting": len(sp4.FRAMES) * len(sp4.CKPTS),
        "path_length_bound": sp4.LMAX,
        "setting_stabiliser_census": dict(
            sorted(Counter(len(sp4.stabiliser(st))
                           for st in sp4.SETTINGS).items())),
        "every_local_leg_is_exactly_orthogonal":
            all(L.is_orthogonal() for L in sp4.LOC.values()),
        "P_star": sp4.NAME[sp4.PERMS[1]],
        "the_wing_group_is_S4": len(sp4.PERMS) == factorial(4),
        "P_pi_factorises_as_system_times_pointer": all(
            sp4.PCARR[pi] == tuple(sp4.SIGMA[pi][i // sp4.NPT] * sp4.NPT
                                   + sp4.SIGMA[pi][i % sp4.NPT]
                                   for i in range(sp4.NC))
            for pi in sp4.PERMS),
        "the_conjugation_law_holds_at":
            sum(1 for pi in sp4.PERMS for w in range(sp4.NW)
                for g in ROT_ORDER
                if (Mx.from_perm(sp4.PCARR[pi]) @ (
                    sp4.LOC[(w, g)] @ Mx.from_perm(pinv(sp4.PCARR[pi])))).key()
                == sp4.LOC[(pi[w], g)].key()),
        "the_conjugation_law_cells":
            len(sp4.PERMS) * sp4.NW * len(ROT_ORDER)
            + (1 if MUTANT == "base-lax" else 0),
    }
    T["four_wing_declaration"] = decl4
    gate("G-FOUR-WING-BASE",
         "the four-wing base is built by the SAME generic constructor that "
         "reproduced I6 at three wings: 2^4 system labels x 2^4 pointer "
         "labels, S_4 on the wing factor, 3^4 settings, 4! frames, five legs "
         "per frame, six checkpoints.  Every local leg is exactly orthogonal, "
         "P_pi factorises as (system)x(pointer) at all 24, and the "
         "conjugation law P_pi U_w P_pi^-1 = U_{pi(w)} is measured at every "
         "declared cell",
         decl4["every_local_leg_is_exactly_orthogonal"]
         and decl4["the_wing_group_is_S4"]
         and decl4["P_pi_factorises_as_system_times_pointer"]
         and decl4["the_conjugation_law_holds_at"]
         == decl4["the_conjugation_law_cells"],
         decl4)

    prog("completion-rule census")
    # THE COMPLETION RULE AT FOUR WINGS -- censused, not sampled
    pairs4 = []
    H4 = sp4.householder(psi4)
    skip = (MUTANT == "ruleempty-lax")
    cells = 0
    agree = 0
    stabcensus = Counter()
    for i in range(1, sp4.NSYS):
        for j in range(i + 1, sp4.NSYS):
            if skip and (i, j) == (1, 3):
                continue
            q = list(range(sp4.NSYS))
            q[i], q[j] = q[j], q[i]
            q = tuple(q)
            V = H4 @ Mx.from_perm(q)
            invs = []
            stab = 1
            for pi in sp4.PERMS:
                if pi == sp4.IDENT:
                    continue
                sig = sp4.SIGMA[pi]
                shadow = sp4.born_symmetric(V, sig)
                commutes = (pcomp(sig, q) == pcomp(q, sig))
                cells += 1
                if shadow == commutes:
                    agree += 1
                if shadow:
                    invs.append(sp4.NAME[pi])
                if commutes:
                    stab += 1
            stabcensus[stab] += 1
            pairs4.append(((i, j), tuple(invs)))
    admitted4 = [p for p, invs in pairs4 if not invs]
    # the same census at three wings, where the rule is NON-empty
    pairs3 = []
    H3 = sp3.householder(psi3)
    stabcensus3 = Counter()
    cells3 = 0
    agree3 = 0
    for i in range(1, sp3.NSYS):
        for j in range(i + 1, sp3.NSYS):
            q = list(range(sp3.NSYS))
            q[i], q[j] = q[j], q[i]
            q = tuple(q)
            V = H3 @ Mx.from_perm(q)
            invs = []
            stab = 1
            for pi in sp3.PERMS:
                if pi == sp3.IDENT:
                    continue
                sig = sp3.SIGMA[pi]
                shadow = sp3.born_symmetric(V, sig)
                commutes = (pcomp(sig, q) == pcomp(q, sig))
                cells3 += 1
                if shadow == commutes:
                    agree3 += 1
                if shadow:
                    invs.append(sp3.NAME[pi])
                if commutes:
                    stab += 1
            stabcensus3[stab] += 1
            pairs3.append(((i, j), tuple(invs)))
    admitted3 = [p for p, invs in pairs3 if not invs]
    Vcols = [tuple(sorted((i, H4.get(i, j) ** 2) for i in range(sp4.NSYS)
                          if H4.get(i, j) != 0)) for j in range(sp4.NSYS)]
    T["completion_rule_at_four_wings"] = {
        "label_pairs_censused": len(pairs4),
        "the_declaration_forces": (sp4.NSYS - 1) * (sp4.NSYS - 2) // 2,
        "pairs_the_rule_admits": len(admitted4),
        "the_rule_returns": (list(sp4.select_Q(psi4))
                             if sp4.select_Q(psi4) else None),
        "setwise_stabiliser_census_over_pairs":
            dict(sorted(stabcensus.items())),
        "the_smallest_setwise_stabiliser": min(stabcensus),
        "shadow_invariance_equals_commutation_at": agree,
        "of_cells": cells,
        "the_shadow_columns_are_pairwise_distinct":
            len(set(Vcols)) == sp4.NSYS,
        "at_three_wings_pairs_censused": len(pairs3),
        "at_three_wings_pairs_admitted": len(admitted3),
        "at_three_wings_the_smallest_setwise_stabiliser": min(stabcensus3),
        "at_three_wings_stabiliser_census": dict(sorted(stabcensus3.items())),
        "at_three_wings_shadow_equals_commutation_at": agree3,
        "at_three_wings_cells": cells3,
        "at_three_wings_the_rule_returns": list(Q3ref),
        "the_mechanism": "the Born shadow of V = H(psi).Q is invariant under "
                         "sigma exactly when sigma COMMUTES with Q -- measured "
                         "at every cell, in both directions, at both wing "
                         "counts -- because the shadow's columns are pairwise "
                         "distinct.  So the rule asks for a transposition of "
                         "labels whose SETWISE STABILISER in the wing group is "
                         "trivial.  At three wings 6 of 21 pairs have one; at "
                         "four wings NO pair does, and the smallest stabiliser "
                         "is 2.",
    }
    gate("G-COMPLETION-RULE-CENSUS",
         "THE PINNED COMPLETION RULE IS EMPTY AT FOUR WINGS, and the "
         "emptiness is a CENSUS, not a search that gave up: every one of the "
         "declared label pairs is tested, the count is gated against a "
         "DERIVED binomial, and the rule's own mechanism is measured -- "
         "shadow-invariance is equivalent to commutation at every cell, so "
         "the rule asks for a pair with trivial setwise stabiliser in the "
         "wing group.  The same census at three wings admits 6 pairs, so the "
         "instrument CAN return a non-empty answer",
         len(pairs4) == (sp4.NSYS - 1) * (sp4.NSYS - 2) // 2
         and agree == cells and agree3 == cells3
         and len(admitted3) > 0
         and T["completion_rule_at_four_wings"][
             "the_shadow_columns_are_pairwise_distinct"],
         T["completion_rule_at_four_wings"])

    prog("choice inventory + reading sweep")
    # THE CHOICE INVENTORY on the extension.  The reference preparation is
    # the one FREE coordinate that could bind a number, so its two readings
    # are both carried through the rule, and the rule is additionally run
    # over a declared family of wing-symmetric preparations.
    alt_read = literal_label7(sp4)
    alt_Q = sp4.select_Q(alt_read)
    alt_stab = sum(1 for pi in sp4.PERMS
                   if all(alt_read[a] ** 2 == alt_read[sp4.SIGMA[pi][a]] ** 2
                          for a in range(sp4.NSYS)))
    ref_stab = sum(1 for pi in sp4.PERMS
                   if all(psi4[a] ** 2 == psi4[sp4.SIGMA[pi][a]] ** 2
                          for a in range(sp4.NSYS)))
    ref_shadow_sym = (ref_stab == len(sp4.PERMS))
    # the equivalence measured under the OTHER reading, so the mechanism gate
    # has a negative control: it must FAIL where the shadow is not symmetric
    Halt = sp4.householder(alt_read)
    agree_alt = 0
    cells_alt = 0
    for i in range(1, sp4.NSYS):
        for j in range(i + 1, sp4.NSYS):
            q = list(range(sp4.NSYS))
            q[i], q[j] = q[j], q[i]
            q = tuple(q)
            V = Halt @ Mx.from_perm(q)
            for pi in sp4.PERMS:
                if pi == sp4.IDENT:
                    continue
                cells_alt += 1
                if sp4.born_symmetric(V, sp4.SIGMA[pi]) == (
                        pcomp(sp4.SIGMA[pi], q) == pcomp(q, sp4.SIGMA[pi])) \
                        or MUTANT == "mechanism-lax":
                    agree_alt += 1
    # the class statement: every GHZ-type reference with declared rational
    # weights, all of them wing-symmetric, leaves the rule empty
    ghz_family = []
    for (a, b) in ((Fr(3, 5), Fr(4, 5)), (Fr(4, 5), Fr(3, 5)),
                   (Fr(5, 13), Fr(12, 13)), (Fr(12, 13), Fr(5, 13))):
        v = [Fr(0)] * sp4.NSYS
        v[0] = a
        v[sp4.NSYS - 1] = b
        ghz_family.append({"weights": [str(a), str(b)],
                           "the_shadow_is_wing_symmetric": all(
                               all(v[x] ** 2 == v[sp4.SIGMA[pi][x]] ** 2
                                   for x in range(sp4.NSYS))
                               for pi in sp4.PERMS),
                           "the_rule_returns": (list(sp4.select_Q(v))
                                                if sp4.select_Q(v) else None)})
    T["completion_rule_at_four_wings"]["THE_READING_SCOPE"] = {
        "reading_A_the_declared_TYPE_all_one_label": {
            "wing_symmetries_leaving_the_preparation_shadow_invariant":
                ref_stab,
            "of_wing_symmetries": len(sp4.PERMS),
            "the_shadow_is_FULLY_wing_symmetric": ref_shadow_sym,
            "shadow_invariance_equals_commutation_at": agree,
            "of_cells": cells, "the_rule_returns": None},
        "reading_B_label_7_literally": {
            "wing_symmetries_leaving_the_preparation_shadow_invariant":
                alt_stab,
            "of_wing_symmetries": len(sp4.PERMS),
            "the_shadow_is_FULLY_wing_symmetric":
                alt_stab == len(sp4.PERMS),
            "shadow_invariance_equals_commutation_at": agree_alt,
            "of_cells": cells_alt,
            "the_rule_returns": list(alt_Q) if alt_Q else None},
        "the_GHZ_family_sweep": ghz_family,
        "members_of_the_family_leaving_the_rule_empty": sum(
            1 for r in ghz_family if r["the_rule_returns"] is None),
        "of_family_members": len(ghz_family),
        "THE_SCOPE": "the emptiness is a statement about the wing-SYMMETRIC "
                     "reference class -- the class the declaration's own TYPE "
                     "specifies, whose support labels are pointwise fixed by "
                     "every wing symmetry.  There the shadow is wing-symmetric, "
                     "the equivalence shadow-invariance == commutation holds at "
                     "every cell, and the rule reduces to pure wing-group "
                     "combinatorics: a label pair with trivial setwise "
                     "stabiliser.  The literal-label reading is NOT in that "
                     "class at four wings -- its shadow is invariant under "
                     "only %d of the %d wing symmetries, the equivalence "
                     "fails at %d of %d cells, and the rule returns (1 3).  "
                     "The freedom is therefore REPORTED as binding this "
                     "negative, not hidden."
                     % (alt_stab, len(sp4.PERMS), cells_alt - agree_alt,
                        cells_alt)}
    gate("G-COMPLETION-RULE-MECHANISM",
         "the rule's mechanism is measured WITH ITS NEGATIVE CONTROL: where "
         "the preparation's Born shadow is wing-symmetric -- the class the "
         "declared TYPE specifies -- shadow-invariance is equivalent to "
         "commutation at every cell and the rule is empty for every member of "
         "the declared GHZ family; where it is not, the equivalence FAILS at "
         "measured cells and the rule returns a completion.  A gate that "
         "could not fail on the second reading would be vacuous",
         ref_shadow_sym and agree == cells and agree_alt < cells_alt
         and alt_stab < len(sp4.PERMS)
         and alt_Q is not None
         and all(r["the_rule_returns"] is None for r in ghz_family)
         and all(r["the_shadow_is_wing_symmetric"] for r in ghz_family),
         T["completion_rule_at_four_wings"]["THE_READING_SCOPE"])
    inv_rows = [
        ("wings", "DECLARED BY THE PIN", "n = 4: the unit's subject"),
        ("system / pointer dimension per wing", "FORCED",
         "2 / 2 -- a wing-count-independent declaration of the construction "
         "rule; the generic constructor carries it unchanged"),
        ("carrier index", "FORCED",
         "i = (system label) x 2^n + (pointer label); measured a bijection on "
         "%d configurations" % sp4.NC),
        ("initial configuration", "FORCED", "j_0 = 0"),
        ("wing symmetry group", "FORCED",
         "all n! wing permutations with P_pi = Sigma_pi (x) Sigma_pi; "
         "S_3 -> S_4 is the pin's own instruction"),
        ("the measurement family", "FORCED",
         "R0 = I, the 3-4-5 rotation, the 5-12-13 rotation -- declared "
         "independently of the wing count"),
        ("the local legs", "FORCED",
         "U_w(g) = sum_o Pi^g_o (x) Sh^o, identity elsewhere -- the generic "
         "constructor"),
        ("the setting family", "FORCED",
         "every assignment of a declared rotation to each wing: 3^4 = %d"
         % len(sp4.SETTINGS)),
        ("the frames", "FORCED", "the n! leg-orders: %d" % len(sp4.FRAMES)),
        ("checkpoints and division events", "FORCED",
         "1 + n legs, n + 2 checkpoints, division events {0, n+1}"),
        ("the two gluing rules", "FORCED",
         "FULL and REAL, the same four-clause predicate, link drawn only "
         "where the rule admits UNIQUELY"),
        ("P*", "FORCED",
         "the lex-first non-identity wing permutation: %s"
         % sp4.NAME[sp4.PERMS[1]]),
        ("the ladder's setting", "FORCED",
         "TB-000, the lex-first fully symmetric setting, as at three wings"),
        ("the target set", "FORCED AS A RULE, COMPUTED AS VALUES",
         "{1, 2, 3, the measured maximum defect order at P*}"),
        ("the target completions", "FORCED AS A RULE, COMPUTED AS VALUES",
         "the lex-first label permutation fixing 0 whose defect at P* has the "
         "target order"),
        ("the reference preparation", "FREE -- TWO READINGS, BOTH MEASURED, "
         "AND THE READING BINDS ONE NEGATIVE",
         "I6 declares psi-G1 as GHZ-type with weights 3/5 and 4/5.  Reading A "
         "(taken here) places 4/5 at the ALL-ONE label, preserving the "
         "declared TYPE and keeping the shadow wing-symmetric; reading B "
         "places it at label 7 literally, whose shadow is NOT wing-symmetric "
         "at four wings.  Both are carried through the completion rule: "
         "reading A leaves it empty (as does every member of the declared GHZ "
         "family), reading B returns (1 3).  The emptiness is therefore "
         "reported at the scope of the wing-symmetric reference class"),
        ("the rest of the nine-member preparation family", "FREE -- NOT "
         "DETERMINED, AND NOT USED",
         "the family's classifier is Cayley's 2x2x2 hyperdeterminant and its "
         "W-class weight triples; neither has a unique four-wing analogue "
         "(four-qubit SLOCC classification is not finite).  No quantity in "
         "this unit reads any member but the reference, exactly as I6's own "
         "ladder does"),
        ("the reference completion", "EMPTY -- A MEASURED NEGATIVE, NOT A "
         "FREEDOM",
         "the pinned rule admits 0 of %d label pairs at four wings; the "
         "ladder's reference row therefore has no four-wing analogue by the "
         "pinned rule, and none is invented" % len(pairs4)),
    ]
    if MUTANT == "inventory-lax":
        inv_rows = inv_rows[:-1]
    forced = sum(1 for r in inv_rows if r[1].startswith("FORCED"))
    free = sum(1 for r in inv_rows if r[1].startswith("FREE"))
    empty = sum(1 for r in inv_rows if r[1].startswith("EMPTY"))
    T["choice_inventory"] = {
        "rows": [{"coordinate": a, "status": b, "what_settles_it": c}
                 for a, b, c in inv_rows],
        "coordinates": len(inv_rows), "forced": forced, "free": free,
        "empty": empty, "declared_by_the_pin": 1,
        "the_alternative_reading_returns": (list(alt_Q) if alt_Q else None),
        "the_alternative_reading_leaves_the_rule_empty": alt_Q is None,
        "freedoms_that_bind_a_number_in_this_unit": 0,
        "freedoms_that_bind_a_NEGATIVE_in_this_unit": 1,
        "which_negative": "the completion rule's emptiness holds at the "
                          "wing-symmetric reference class (reading A and the "
                          "whole declared GHZ family); the literal-label "
                          "reading, which leaves that class, admits (1 3)",
        "reading": "the extension is FORCED in every coordinate the "
                   "construction rule reaches; it is FREE in the preparation "
                   "family beyond the reference, where the rule's classifier "
                   "has no four-wing analogue; and it is EMPTY at the "
                   "reference completion, which is a determinate negative "
                   "rather than a licence to choose",
    }
    gate("G-CHOICE-INVENTORY",
         "the choice inventory on the extension is run and reported exactly: "
         "%d coordinates, %d forced by the construction rule, %d free, %d "
         "measured empty.  The freedoms are DISCLOSED and their consequences "
         "measured -- the alternative reading of the reference preparation is "
         "carried through the completion rule, and where it differs the "
         "difference is REPORTED rather than hidden"
         % (len(inv_rows), forced, free, empty),
         forced + free + empty + 1 == len(inv_rows)
         and empty == 1
         and T["completion_rule_at_four_wings"]["pairs_the_rule_admits"] == 0
         and T["choice_inventory"]["the_alternative_reading_returns"]
         is not None,
         {"coordinates": len(inv_rows), "forced": forced, "free": free,
          "empty": empty})

    # -- 5. THE FOUR-WING COMPLETION CENSUS, exhaustive by orbit count -----
    prog("four-wing exhaustive census (orbit route)")
    sig4 = sp4.SIGMA[sp4.PERMS[1]]
    dist4, first4, ntau4, fib4, cpos4, fpos4 = census_orbit(sp4, sig4)
    total4 = sum(dist4.values())
    if MUTANT == "census-count-corrupt":
        total4 = total4 + 1
    forced4 = factorial(sp4.NSYS - 1)
    maxord4 = max(dist4)
    NAIVE_CAP = 1000000
    if MUTANT == "scale-lax":
        NAIVE_CAP = 0
    scanned, found = naive_lex_scan(sig4, sp4.NSYS, maxord4, NAIVE_CAP)
    T["four_wing_census"] = {
        "route": "ORBIT COUNT -- exhaustive over every completion without "
                 "enumerating any: the defect depends on q only through "
                 "tau = q^-1 sigma q, tau runs over every involution of "
                 "sigma's cycle type on the non-zero labels, and the fibres "
                 "are equal",
        "orbits_enumerated": ntau4, "common_fibre_size": fib4,
        "completions_censused": total4,
        "the_declaration_forces": forced4,
        "orbits_times_fibre": ntau4 * fib4,
        "sigma_cycle_type": [list(x) for x in cycle_type(sig4)],
        "ord_distribution_at_P_star": dict(sorted(dist4.items())),
        "orders_realised": sorted(dist4),
        "the_maximum_order_at_P_star": maxord4,
        "the_maximum_order_over_the_whole_wing_group": max(
            pord(defect_label_route(sp4.SIGMA[pi], first4[o]))
            for pi in sp4.PERMS for o in [maxord4]),
        "lex_first_completion_per_order": dict(
            (str(k), list(v)) for k, v in sorted(first4.items())),
        "constrained_position_pairs": [list(x) for x in cpos4],
        "free_positions": fpos4,
        "THE_NAIVE_LEX_SCAN": {
            "cap_declared_and_printed": NAIVE_CAP,
            "permutations_scanned": scanned,
            "found_the_maximum_order_target": found is not None,
            "of_completions": forced4,
            "what_this_measures": "the scale wall the structural route "
                                  "replaces: a direct lex scan reaches rank "
                                  "%d of %d without finding a completion at "
                                  "the maximum defect order.  The structural "
                                  "route returns it exactly, and is validated "
                                  "against the direct route at three wings"
                                  % (scanned, forced4)},
    }
    gate("G-CENSUS-CELL-COMPLETE",
         "the four-wing census enumerates EVERY support cell: the orbit count "
         "times the common fibre size is gated equal to the DERIVED "
         "(2^n - 1)! -- a dropped cell moves the product and dies here",
         ntau4 * fib4 == forced4,
         {"orbits": ntau4, "fibre": fib4, "product": ntau4 * fib4,
          "forced": forced4})
    gate("G-CENSUS-TOTAL-RECOMPUTED",
         "the census total is recomputed inside the gate from the emitted "
         "distribution and gated against the derived factorial -- a corrupted "
         "count cannot reach the receipt",
         total4 == forced4 and sum(dist4.values()) == forced4,
         {"total": total4, "recomputed": sum(dist4.values()),
          "forced": forced4})
    gate("G-CENSUS-SCALE-DISCLOSED",
         "the four-wing census is EXHAUSTIVE and says so with its scope: "
         "%d completions censused at %d orbits, no sampling and no cap.  The "
         "naive route's cap is printed beside it with what it reached, so the "
         "scale claim is a measurement rather than an assertion"
         % (total4, ntau4),
         scanned > 1
         and (scanned == min(NAIVE_CAP, forced4) or found is not None),
         T["four_wing_census"]["THE_NAIVE_LEX_SCAN"])

    # -- 6. THE FOUR-WING INSTANCES ---------------------------------------
    prog("four-wing instances (this is the long one)")
    targets4 = [1, 2, 3, maxord4]
    st4 = ("R0",) * 4
    inst4 = {}
    swept4 = targets4[:-1] if MUTANT == "instances-lax" else targets4
    for k in swept4:
        inst4["A1 target ord = %d" % k] = instance(sp4, psi4, first4[k], st4)
        prog("  target ord=%d done: |Hol|=%s"
             % (k, inst4["A1 target ord = %d" % k].get("holonomy_order")))
    T["four_wing_instances"] = dict((k, public(v))
                                    for k, v in sorted(inst4.items()))
    for label, ob in sorted(inst4.items()):
        if ob.get("holonomy_order") is not None \
                and ob["holonomy_order"] <= SET_EQUALITY_CAP:
            G = closure(list(ob["_dist"]), sp4.NC, cap=SET_EQUALITY_CAP)
            T["group_order_two_routes"]["per_instance"][
                "four wings / " + label] = {
                "schreier_sims": ob["holonomy_order"],
                "brute_force": (len(G) if G is not None else None),
                "route": "both",
                "agree": (G is not None and len(G) == ob["holonomy_order"])}
        else:
            T["group_order_two_routes"]["per_instance"][
                "four wings / " + label] = {
                "schreier_sims": ob["holonomy_order"], "brute_force": None,
                "route": "brute force refused above the printed cap %d"
                         % SET_EQUALITY_CAP, "agree": None}
    pi_ = T["group_order_two_routes"]["per_instance"]
    T["group_order_two_routes"]["cells_where_both_routes_ran"] = sum(
        1 for v in pi_.values() if v["agree"] is not None)
    T["group_order_two_routes"]["cells_where_they_agree"] = sum(
        1 for v in pi_.values() if v["agree"])
    gate("G-GROUP-TWO-ROUTES-AT-FOUR-WINGS",
         "the two-route agreement is re-measured at the four-wing instances "
         "whose order is below the printed cap, so the chain is validated "
         "against enumeration at the very wing count where enumeration is "
         "impossible for the large rungs",
         T["group_order_two_routes"]["cells_where_they_agree"]
         == T["group_order_two_routes"]["cells_where_both_routes_ran"]
         and T["group_order_two_routes"]["cells_where_both_routes_ran"] > 0,
         T["group_order_two_routes"])

    gate("G-FOUR-WING-INSTANCES",
         "every declared four-wing completion yields a readable transport "
         "geometry: all cotree generators are carrier permutations of product "
         "form, all defects are readable and pure-system, and the target set "
         "is the rule's own {1, 2, 3, measured maximum} with the maximum "
         "COMPUTED from the exhaustive census",
         len(inst4) == len(targets4)
         and all(v["every_generator_is_of_product_form"] for v in inst4.values())
         and all(v["every_defect_is_of_product_form"] for v in inst4.values())
         and all(v["defect_pointer_parts_all_identity"]
                 for v in inst4.values())
         and targets4[3] == maxord4,
         {"targets": targets4, "instances_built": sorted(inst4),
          "holonomy_orders": [
              inst4.get("A1 target ord = %d" % k, {}).get("holonomy_order")
              for k in targets4]})

    prog("admission cross-check")
    # the admission table by two implementations
    w4chk = World(sp4, psi4, first4[3], st4)
    a_fast = w4chk.admission(fast=True)
    a_slow = w4chk.admission(fast=False)
    if MUTANT == "admission-lax":
        a_slow = dict((k, dict()) for k in a_slow)
    w3chk = World(sp3, psi3, first3_bf[3], st3)
    b_fast = w3chk.admission(fast=True)
    b_slow = w3chk.admission(fast=False)
    T["admission_two_implementations"] = {
        "four_wing_cells": sum(len(v) for v in a_fast.values()),
        "four_wing_routes_agree": a_fast == a_slow,
        "three_wing_cells": sum(len(v) for v in b_fast.values()),
        "three_wing_routes_agree": b_fast == b_slow,
        "what_the_memoisation_uses": "the leg MULTISET is frame-independent "
                                     "(the frames differ in leg ORDER alone), "
                                     "so the FULL-rule push depends on the "
                                     "wing permutation and not on the frame",
    }
    gate("G-ADMISSION-TWO-IMPLEMENTATIONS",
         "the admission table is computed by the memoised implementation and "
         "by the naive per-frame one, at BOTH wing counts, and gated equal "
         "cell by cell -- the memoisation's licence is measured, not argued",
         a_fast == a_slow and b_fast == b_slow,
         T["admission_two_implementations"])

    # THE CONNECTIVE WITNESS (RUNBOOK section 14 addendum, v13 #313): the
    # link-drawing boundary is a Boolean connective; its death certificate is
    # the measured delta of the alternative connective.
    prog("connective witness")
    conn = instance(sp4, psi4, first4[3], st4, connective="any")
    base_ord = inst4["A1 target ord = 3"]["holonomy_order"]
    conn_ord = conn.get("holonomy_order")
    if MUTANT == "connective-lax":
        conn_ord = base_ord
    T["connective_witness"] = {
        "the_declared_connective": "a link is drawn where the predicate "
                                   "admits UNIQUELY",
        "the_alternative_connective": "a link is drawn where the predicate "
                                      "admits AT ALL",
        "links_declared": inst4["A1 target ord = 3"]["links"],
        "links_alternative": conn["links"],
        "holonomy_declared": base_ord,
        "holonomy_alternative": conn_ord,
        "the_connective_is_load_bearing": conn_ord != base_ord,
        "the_link_count_also_moves":
            conn["links"] != inst4["A1 target ord = 3"]["links"],
    }
    gate("G-CONNECTIVE-WITNESS",
         "the link-drawing connective carries a witness gate whose death "
         "certificate is the measured delta of the ALTERNATIVE connective: "
         "drawing a link wherever the predicate admits at all, instead of "
         "only where it admits uniquely, moves the measured object -- so the "
         "declared connective is load-bearing and is measured to be",
         T["connective_witness"]["the_connective_is_load_bearing"],
         T["connective_witness"])

    # -- 7. IDENTIFICATION AND THE FOUR-WING LADDER ------------------------
    prog("four-wing identification")
    gl4 = gl_labels(sp4.NW)
    ladder4 = {}
    for label, ob in sorted(inst4.items()):
        name, method, tab = identify(ob["_sysd"], ob["defect_subgroup_order"],
                                     sp4.NSYS, gl4)
        ladder4[label] = {
            "Q": ob["Q"],
            "holonomy_order": ob["holonomy_order"],
            "defect_subgroup_order": ob["defect_subgroup_order"],
            "system_image_order": ob["system_image_order"],
            "pointer_image_order": ob["pointer_image_order"],
            "support": ob["the_defect_support"],
            "support_size": len(ob["the_defect_support"]),
            "THE_TYPE": name, "identification_method": method,
            "identification_table": tab,
            "wing_symmetries_inside_the_holonomy":
                ob["wing_symmetries_inside_the_holonomy"],
            "the_order_factorises_over_the_wing_group":
                ob["the_order_factorises_over_the_wing_group"],
            "the_geometry_equals_the_defects_and_the_wings":
                ob["the_geometry_equals_the_defects_and_the_wings"],
            "orbit_stabiliser_chain": ob["orbit_stabiliser_chain"],
        }
    T["four_wing_ladder"] = ladder4
    def popcount(x):
        c = 0
        while x:
            c += x & 1
            x >>= 1
        return c

    weight_rows = {}
    for label, r in sorted(ladder4.items()):
        sup = r["support"]
        if not sup:
            weight_rows[label] = {"support_size": 0, "the_weight_threshold":
                                  None, "the_support_is_a_weight_class": None}
            continue
        wmin = min(popcount(a) for a in sup)
        cls = sorted(a for a in range(1, sp4.NSYS)
                     if popcount(a) >= wmin
                     and not (MUTANT == "weights-lax" and a == sup[0]))
        weight_rows[label] = {
            "support_size": len(sup), "the_weight_threshold": wmin,
            "the_support_is_a_weight_class": cls == sorted(sup),
            "the_weight_class_size": len(cls)}
    T["support_weight_structure"] = {
        "per_rung": weight_rows,
        "rungs_whose_support_is_a_Hamming_weight_class": sum(
            1 for v in weight_rows.values()
            if v["the_support_is_a_weight_class"]),
        "of_non_trivial_rungs": sum(1 for v in weight_rows.values()
                                    if v["support_size"] > 0),
    }
    gate("G-SUPPORT-WEIGHT-STRUCTURE",
         "the four-wing supports are not arbitrary label sets: each "
         "non-trivial rung's support is measured to be exactly a Hamming "
         "weight class of the system labels (weight at least w for a "
         "measured w), and the class is rebuilt independently from the "
         "weight predicate and compared as a set",
         T["support_weight_structure"][
             "rungs_whose_support_is_a_Hamming_weight_class"]
         == T["support_weight_structure"]["of_non_trivial_rungs"],
         T["support_weight_structure"])

    named4 = sum(1 for r in ladder4.values() if r["THE_TYPE"] != "UNNAMED")
    setmethod = sum(1 for r in ladder4.values()
                    if r["identification_method"].startswith("set equality"))
    proofmethod = sum(1 for r in ladder4.values()
                      if r["identification_method"].startswith("containment"))
    T["identification_methods"] = {
        "rungs": len(ladder4), "named": named4,
        "by_set_equality": setmethod, "by_containment_plus_order": proofmethod,
        "the_set_equality_cap": SET_EQUALITY_CAP,
        "per_rung": dict((k, v["identification_method"])
                         for k, v in sorted(ladder4.items())),
        "why_two_methods": "a group of order 653,837,184,000 cannot be "
                           "compared element by element; containment plus "
                           "order is a PROOF of the same set equality -- the "
                           "generators are measured even, measured to fix "
                           "label 0 and measured to fix the complement of the "
                           "support, so the group lies inside the alternating "
                           "group on that support, and the orders are gated "
                           "equal",
    }
    gate("G-IDENTIFICATION",
         "every four-wing rung is NAMED, and the method is labelled per rung: "
         "set equality against a brute-forced group where the order is below "
         "the printed cap %d, containment-plus-order (a proof) above it.  The "
         "order clause is MEASURED against a derived |Alt(support)|, so a "
         "group whose order does not match cannot be named"
         % SET_EQUALITY_CAP,
         named4 == len(ladder4)
         and all(r["identification_table"]["the_orders_agree"]
                 for r in ladder4.values()
                 if r["defect_subgroup_order"] > 1)
         and all(r["identification_table"]["every_generator_is_even"]
                 for r in ladder4.values()
                 if r["defect_subgroup_order"] > 1),
         T["identification_methods"])

    # -- 8. THE LADDER-EXTENSION TEST --------------------------------------
    prog("ladder-extension test")

    def lift(alpha, n3, n4):
        """The declared embedding: three wings A,B,C sit inside four wings
        A,B,C,D with wing D in state 0, so the label a (bits b_A b_B b_C)
        becomes the label 2a (bits b_A b_B b_C 0)."""
        if MUTANT == "embed-flip":
            return tuple(list(alpha) + list(range(n3, n4)))
        q = list(range(n4))
        for a in range(n3):
            q[2 * a] = 2 * alpha[a]
        return tuple(q)

    top4 = "A1 target ord = %d" % maxord4
    B_top = inst4[top4]["_bsgs_K"]
    ext_rows = {}
    outside_total = 0
    for label in sorted(rung_sets):
        S = rung_sets[label]
        lifted = [lift(al, sp3.NSYS, sp4.NSYS) for al in sorted(S)]
        per = {}
        for k4 in sorted(inst4):
            Bk = inst4[k4]["_bsgs_K"]
            per[k4] = sum(1 for x in lifted if not Bk.contains(x))
        out_top = per[top4]
        outside_total += out_top
        ext_rows[label] = {
            "three_wing_rung": ladder3[label]["THE_TYPE"],
            "order": len(S),
            "elements_outside_each_four_wing_rung": per,
            "inside_the_top_rung": out_top == 0,
            "the_lifted_support": sorted(set(
                a for al in lifted for a in range(sp4.NSYS) if al[a] != a)),
        }
    rungs_in = sum(1 for r in ext_rows.values() if r["inside_the_top_rung"])
    # the direction control: the four-wing top rung is NOT inside any lifted
    # three-wing rung (the containment is one-way, and that is measured)
    B3top = rung_sets[top3]
    lifted_top3 = set(lift(al, sp3.NSYS, sp4.NSYS) for al in B3top)
    sample = [g for g in inst4[top4]["_sysd"]]
    rev_outside = sum(1 for g in sample if g not in lifted_top3)
    if MUTANT == "embed-direction":
        rev_outside = 0
    declared_image = sorted(2 * a for a in ladder3[top3]["support"])
    map_is_the_declared_one = (
        ext_rows[top3]["the_lifted_support"] == declared_image)
    T["ladder_extension"] = {
        "the_embedding": "three wings A,B,C inside four wings A,B,C,D with "
                         "wing D in the zero state: the system label a "
                         "becomes 2a, and every odd four-wing label is fixed",
        "the_declared_image_of_the_top_rung_support": declared_image,
        "the_lifted_support_of_the_top_rung":
            ext_rows[top3]["the_lifted_support"],
        "the_embedding_map_is_the_declared_one": map_is_the_declared_one,
        "the_embedding_is_constructed_not_asserted": True,
        "three_wing_rungs": len(ext_rows),
        "rungs_whose_embedded_copy_lies_inside_the_top_rung": rungs_in,
        "elements_outside_the_top_rung": outside_total,
        "per_rung": ext_rows,
        "the_four_wing_top_rung": ladder4[top4]["THE_TYPE"],
        "the_reverse_containment_fails_at":
            "%d of %d generators of the four-wing top rung lie outside the "
            "lifted three-wing top rung" % (rev_outside, len(sample)),
        "the_reverse_containment_generators_outside": rev_outside,
        "rung_by_rung_correspondence": dict(
            (lab, {"three_wing": ext_rows[lab]["three_wing_rung"],
                   "inside_the_same_named_four_wing_target":
                       ext_rows[lab]["elements_outside_each_four_wing_rung"]
                       .get(lab, None) == 0 if lab in inst4 else None})
            for lab in sorted(ext_rows)),
    }
    gate("G-LADDER-EXTENSION",
         "THE LADDER-EXTENSION TEST, at the set-equality standard and with "
         "the embedding CONSTRUCTED: every element of every three-wing rung "
         "is lifted through the declared wing-D embedding and tested for "
         "membership in each four-wing rung by sifting through its "
         "base-and-strong-generating-set.  The whole three-wing ladder lies "
         "inside the four-wing TOP rung -- %d of %d rungs, %d elements "
         "outside -- and the rung-by-rung table shows where it does not.  "
         "The MAP is gated too: the lifted support of the three-wing top "
         "rung is compared against the declared image {2a}, so a membership "
         "answer computed about a different embedding dies here"
         % (rungs_in, len(ext_rows), outside_total),
         rungs_in == len(ext_rows) and outside_total == 0
         and map_is_the_declared_one,
         T["ladder_extension"])
    gate("G-LADDER-EXTENSION-DIRECTION",
         "the embedding is measured ONE-WAY: the four-wing top rung does not "
         "lie inside the lifted three-wing one, so the containment reported "
         "is an embedding and not an equality read in whichever direction "
         "happens to pass",
         rev_outside > 0,
         {"generators_outside": rev_outside, "of_generators": len(sample)})

    # -- 9. THE CEILING ----------------------------------------------------
    prog("the ceiling")

    def ceiling_block(sp, insts):
        wing_par = dict((sp.NAME[pi], parity(sp.SIGMA[pi]))
                        for pi in sp.PERMS)
        if MUTANT == "parity-lax":
            wing_par[sp.NAME[sp.PERMS[1]]] = 1
        fix0 = sum(1 for pi in sp.PERMS if sp.SIGMA[pi][0] == 0)
        even = sum(1 for v in wing_par.values() if v == 0)
        ptr = [v["pointer_image_order"] for v in insts.values()]
        largest_ptr = max(ptr) if ptr else 0
        if MUTANT == "ceiling-lax":
            largest_ptr += 1
        altorder = factorial(sp.NSYS - 1) // 2
        ceiling = altorder * largest_ptr
        attained = max([v["holonomy_order"] for v in insts.values()] or [0])
        return {
            "wings": sp.NW,
            "the_alternating_group_on_the_non_zero_labels": altorder,
            "non_zero_labels": sp.NSYS - 1,
            "wing_symmetries": len(sp.PERMS),
            "wing_symmetries_that_are_even_on_the_labels": even,
            "wing_symmetries_fixing_label_0": fix0,
            "wing_parities": wing_par,
            "the_parity_hypothesis_holds": even == len(sp.PERMS),
            "the_largest_pointer_image_measured": largest_ptr,
            "the_algebraic_ceiling": ceiling,
            "the_largest_holonomy_order_measured": attained,
            "the_ceiling_is_attained": attained == ceiling,
            "instances_all_of_whose_system_generators_are_even":
                sum(1 for v in insts.values()
                    if v["holonomy_system_generators_all_even"]),
            "instances_all_of_whose_system_generators_fix_label_0":
                sum(1 for v in insts.values()
                    if v["holonomy_system_generators_all_fix_label_0"]),
            "of_instances": len(insts),
        }

    cel4 = ceiling_block(sp4, inst4)
    cel3 = ceiling_block(sp3, inst3)
    cel2 = ceiling_block(sp2, inst2)
    # the parity lemma, proved by the transposition count and measured
    par_lemma = {}
    for n in (2, 3, 4):
        spn = species(n)
        t = tuple([1, 0] + list(range(2, n)))
        par_lemma[n] = {
            "a_wing_transposition_moves":
                sum(1 for a in range(spn.NSYS) if spn.SIGMA[t][a] != a),
            "in_transpositions": sum(
                1 for a in range(spn.NSYS) if spn.SIGMA[t][a] != a) // 2,
            "predicted_parity_2_to_the_n_minus_2_mod_2":
                (2 ** (n - 2)) % 2 if n >= 2 else None,
            "measured_parity": parity(spn.SIGMA[t]),
            "all_wing_symmetries_even":
                all(parity(spn.SIGMA[pi]) == 0 for pi in spn.PERMS),
        }
    T["ceiling"] = {
        "four_wings": cel4, "three_wings": cel3, "two_wings": cel2,
        "the_argument": "every defect is a commutator of label permutations "
                        "fixing label 0, hence an EVEN permutation of the "
                        "2^n - 1 non-zero system labels; every wing symmetry "
                        "is measured even on the labels and measured to fix "
                        "label 0; every holonomy element is measured to act "
                        "in product form.  Hence |Hol| <= |Alt(2^n - 1)| x "
                        "(the measured pointer image), with Alt brute-forced "
                        "or its order derived here rather than cited",
        "the_parity_lemma": par_lemma,
        "the_parity_lemma_statement": "a wing transposition moves 2^(n-1) "
                                      "labels in 2^(n-2) transpositions, so "
                                      "it is ODD exactly at n = 2 and EVEN "
                                      "for every n >= 3; since transpositions "
                                      "generate, the ceiling argument's "
                                      "parity hypothesis holds for all n >= 3 "
                                      "and fails at n = 2",
        "at_two_wings_the_hypothesis_fails_and_the_agreement_is_numerical":
            not cel2["the_parity_hypothesis_holds"],
        "I6_declares_the_three_wing_ceiling": read_by_path(
            I6, ("tables", "the_ladder", "the_ceiling",
                 "the_algebraic_ceiling")),
    }
    gate("G-CEILING-INGREDIENTS",
         "the ceiling argument's own ingredients are measured at four wings, "
         "not inherited: all %d wing symmetries are EVEN on the 16 labels and "
         "all %d fix label 0; every instance's holonomy system generators are "
         "even and fix label 0; and the parity lemma is proved by the "
         "transposition count (2^(n-2) transpositions, odd only at n = 2) and "
         "measured at n = 2, 3, 4"
         % (cel4["wing_symmetries_that_are_even_on_the_labels"],
            cel4["wing_symmetries_fixing_label_0"]),
         cel4["the_parity_hypothesis_holds"]
         and cel4["wing_symmetries_fixing_label_0"] == len(sp4.PERMS)
         and cel4["instances_all_of_whose_system_generators_are_even"]
         == cel4["of_instances"]
         and cel4["instances_all_of_whose_system_generators_fix_label_0"]
         == cel4["of_instances"]
         and all(par_lemma[n]["measured_parity"]
                 == par_lemma[n]["predicted_parity_2_to_the_n_minus_2_mod_2"]
                 for n in par_lemma)
         and not par_lemma[2]["all_wing_symmetries_even"]
         and par_lemma[3]["all_wing_symmetries_even"]
         and par_lemma[4]["all_wing_symmetries_even"],
         {"four": cel4, "lemma": par_lemma})
    gate("G-CEILING-ATTAINED",
         "THE FOUR-WING CEILING IS DERIVED AND ATTAINED: |Alt(15)| x the "
         "measured pointer image = %d, and the largest measured four-wing "
         "holonomy order is gated EQUAL to it.  The three-wing ceiling is "
         "re-derived by the same code and gated against I6's committed value"
         % cel4["the_algebraic_ceiling"],
         cel4["the_ceiling_is_attained"]
         and cel3["the_ceiling_is_attained"]
         and cel3["the_algebraic_ceiling"] == read_by_path(
             I6, ("tables", "the_ladder", "the_ceiling",
                  "the_algebraic_ceiling")),
         {"four_wing_ceiling": cel4["the_algebraic_ceiling"],
          "four_wing_max": cel4["the_largest_holonomy_order_measured"],
          "three_wing_ceiling": cel3["the_algebraic_ceiling"]})

    # -- 10. THE GROWTH LAW AND THE FAMILIES -------------------------------
    prog("growth law and families")
    pts = []
    for n, cel in ((2, cel2), (3, cel3), (4, cel4)):
        pts.append({
            "wings": n,
            "system_labels": 2 ** n,
            "the_maximum_holonomy_order_measured":
                cel["the_largest_holonomy_order_measured"],
            "the_algebraic_ceiling": cel["the_algebraic_ceiling"],
            "the_ceiling_is_attained": cel["the_ceiling_is_attained"],
            "the_parity_hypothesis_holds": cel["the_parity_hypothesis_holds"],
            "the_closed_form_(2^n-1)!/2 x n!":
                (factorial(2 ** n - 1) // 2) * factorial(n),
            "the_scope_of_the_maximum":
                "exhaustive over all completions" if n == 2
                else "over the declared targets, upgraded to ALL completions "
                     "by the ceiling (no completion can exceed it)",
        })
    if MUTANT == "growth-corrupt":
        pts[2]["the_maximum_holonomy_order_measured"] = 1
    law_holds = [p["wings"] for p in pts
                 if p["the_maximum_holonomy_order_measured"]
                 == p["the_closed_form_(2^n-1)!/2 x n!"]]
    T["growth_law"] = {
        "points": pts,
        "the_sequence": [p["the_maximum_holonomy_order_measured"]
                         for p in pts],
        "the_closed_form": "(2^n - 1)!/2 x n!",
        "the_closed_form_holds_at_wing_counts": law_holds,
        "the_closed_form_is_an_upper_bound_for_every_n_at_least_3":
            "proved above: the parity lemma gives Hol <= Alt(2^n - 1) on the "
            "system factor and the pointer image is at most the wing group",
        "the_ratio_from_three_to_four_wings":
            pts[2]["the_maximum_holonomy_order_measured"]
            // pts[1]["the_maximum_holonomy_order_measured"],
        "at_two_wings_the_closed_form_agrees_numerically_without_the_argument":
            not pts[0]["the_parity_hypothesis_holds"],
    }
    gate("G-GROWTH-LAW",
         "the tower's growth is measured at three wing counts by one "
         "instrument: %s.  The closed form (2^n - 1)!/2 x n! is gated against "
         "the measured maxima, and the n = 2 agreement is DISCLOSED as "
         "numerical -- the parity hypothesis the argument needs fails there, "
         "so that point is not an instance of the theorem"
         % " -> ".join(str(x) for x in T["growth_law"]["the_sequence"]),
         law_holds == [2, 3, 4]
         and pts[1]["the_ceiling_is_attained"]
         and pts[2]["the_ceiling_is_attained"]
         and not pts[0]["the_parity_hypothesis_holds"],
         T["growth_law"])

    # families: alternating / linear / other, and where GL(n,2) went
    fam = {}
    for label, r in sorted(ladder4.items()):
        t = r["THE_TYPE"]
        if MUTANT == "families-lax" and label.endswith("3"):
            t = "SOMETHING ELSE"
        fam[label] = ("trivial" if t == "trivial"
                      else "alternating" if t.startswith("A_")
                      else "linear" if t.startswith("GL")
                      else "other")
    fam3 = {}
    for label, r in sorted(ladder3.items()):
        t = r["THE_TYPE"]
        fam3[label] = ("trivial" if t == "trivial"
                       else "alternating" if t.startswith("A_")
                       else "linear" if t.startswith("GL")
                       else "other")
    gl_in_top = sum(1 for g in gl4 if not B_top.contains(g))
    gl3_in_top3 = len([g for g in gl3 if g not in rung_sets[top3]])
    T["families"] = {
        "four_wing_rungs": len(ladder4),
        "four_wing_named_rungs": named4,
        "four_wing_alternating_rungs": sum(1 for v in fam.values()
                                           if v == "alternating"),
        "four_wing_linear_rungs": sum(1 for v in fam.values()
                                      if v == "linear"),
        "four_wing_trivial_rungs": sum(1 for v in fam.values()
                                       if v == "trivial"),
        "four_wing_other_rungs": sum(1 for v in fam.values() if v == "other"),
        "per_rung": dict((k, {"type": ladder4[k]["THE_TYPE"],
                              "family": fam[k]}) for k in sorted(ladder4)),
        "three_wing_families": dict(
            (k, {"type": ladder3[k]["THE_TYPE"], "family": fam3[k]})
            for k in sorted(ladder3)),
        "three_wing_linear_rungs": sum(1 for v in fam3.values()
                                       if v == "linear"),
        "the_linear_group_at_four_wings": {
            "|GL(4,2)|": len(gl4),
            "elements_outside_the_four_wing_top_rung": gl_in_top,
            "GL(4,2)_lies_inside_the_top_rung": gl_in_top == 0,
            "but_it_is_realised_as_a_rung_at": sum(
                1 for r in ladder4.values()
                if r["THE_TYPE"].startswith("GL")),
            "at_three_wings_GL(3,2)_was_a_rung_at": sum(
                1 for r in ladder3.values()
                if r["THE_TYPE"].startswith("GL")),
            "|GL(3,2)|": len(gl3),
            "GL(3,2)_outside_the_three_wing_top_rung": gl3_in_top3,
        },
        "the_reading": "at four wings every named rung is ALTERNATING.  The "
                       "substrate's own linear group is still there -- all "
                       "20,160 elements of GL(4,2) lie inside the top rung -- "
                       "but no declared completion REALISES it as a rung, "
                       "which is what the ord-2 target did at three wings",
    }
    gate("G-FAMILIES",
         "the family membership of every four-wing rung is decided by its "
         "earned name, not by its order: %d alternating, %d linear, %d "
         "trivial, %d other.  The linear group is separately located -- "
         "GL(4,2) is built from the linearity requirement and every one of "
         "its %d elements is sifted against the top rung"
         % (T["families"]["four_wing_alternating_rungs"],
            T["families"]["four_wing_linear_rungs"],
            T["families"]["four_wing_trivial_rungs"],
            T["families"]["four_wing_other_rungs"], len(gl4)),
         named4 == len(ladder4)
         and T["families"]["four_wing_other_rungs"] == 0
         and gl_in_top == 0
         and T["families"]["three_wing_linear_rungs"] == 1,
         T["families"])

    # -- 11. GEN's and PSI's laws at four wings ----------------------------
    prog("the inherited laws at four wings")
    lawrows = {}
    for label in sorted(inst4):
        Q = tuple(inst4[label]["Q"])
        w = World(sp4, psi4, Q, st4)
        okgen = 0
        okpsi = 0
        cellsn = 0
        for pi in sp4.PERMS:
            if pi == sp4.IDENT:
                continue
            cellsn += 1
            D, _ = w.defect_measured(pi)
            sig = sp4.SIGMA[pi]
            S = Mx.from_perm(sig)
            gen_form = sp4.kron_pointer_identity(
                S @ (w.V.T() @ (S.T() @ w.V)))
            if D.key() == gen_form.key():
                okgen += 1
            P = Mx.from_perm(sp4.PCARR[pi])
            Pi = Mx.from_perm(pinv(sp4.PCARR[pi]))
            comm = P @ (w.u.T() @ (Pi @ w.u))
            if D.key() == comm.key():
                okpsi += 1
        if MUTANT == "laws-lax":
            okgen -= 1
        lawrows[label] = {
            "cells": cellsn,
            "GEN_form_D_equals_sigma_Vt_sigma_V_tensor_I_at": okgen,
            "PSI_one_law_D_equals_the_group_commutator_at": okpsi,
        }
    T["inherited_laws_at_four_wings"] = {
        "per_instance": lawrows,
        "GEN_holds_everywhere": all(
            v["GEN_form_D_equals_sigma_Vt_sigma_V_tensor_I_at"] == v["cells"]
            for v in lawrows.values()),
        "PSI_holds_everywhere": all(
            v["PSI_one_law_D_equals_the_group_commutator_at"] == v["cells"]
            for v in lawrows.values()),
        "scope": "GEN and PSI are TWO-wing bases at system dimension 3; what "
                 "is inherited here is the FORM of their laws, never a "
                 "number of their arenas, and the form is re-measured at "
                 "every four-wing cell",
    }
    T["inherited_laws_at_four_wings"]["status"] = (
        "ANALYTICALLY FORCED -- A DISCLOSURE, NOT A MUST-PASS CLAIM (RUNBOOK "
        "section 14 addendum, v13 #208).  Given the declared construction "
        "u = V (x) I and P_pi = Sigma (x) Sigma with Sigma a permutation "
        "matrix, D = (P u P^-1)^T u = P u^-1 P^-1 u = (Sigma V^T Sigma^T V) "
        "(x) I is an identity of the algebra, at any wing count.  What is "
        "measured and NOT forced is transcription (the identity is "
        "re-evaluated cell by cell at four wings, where a mis-transcribed "
        "form fails -- and did, in construction) and the CONTINGENT facts "
        "beside it: that the defect is a carrier permutation at all, and that "
        "its pointer part is the identity")
    T["inherited_laws_at_four_wings"]["the_contingent_facts"] = {
        "defects_readable_as_carrier_permutations": dict(
            (k, v["defects_readable"]) for k, v in sorted(inst4.items())),
        "of_wing_symmetries": len(sp4.PERMS),
        "defect_pointer_parts_all_identity": dict(
            (k, v["defect_pointer_parts_all_identity"])
            for k, v in sorted(inst4.items())),
    }
    gate("G-INHERITED-LAWS",
         "GEN's psi-independent defect form D = (Sigma V^T Sigma^T V) (x) I "
         "and PSI's one law D = [P_pi^-1, u] are re-evaluated at four wings, "
         "cell by cell, against the defect READ OFF the leg matrices.  Both "
         "are ANALYTICALLY FORCED by the declared construction and are "
         "reported as disclosures; the MUST-PASS content beside them is "
         "contingent -- every defect is readable as a carrier permutation at "
         "all %d wing symmetries of every declared instance, and every "
         "defect's pointer part is the identity" % len(sp4.PERMS),
         all(v["defects_readable"] == len(sp4.PERMS) for v in inst4.values())
         and all(v["defect_pointer_parts_all_identity"]
                 for v in inst4.values())
         and T["inherited_laws_at_four_wings"]["GEN_holds_everywhere"]
         and T["inherited_laws_at_four_wings"]["PSI_holds_everywhere"],
         T["inherited_laws_at_four_wings"])

    # -- 12. CONTROLS: symmetry self-test, base-node invariance, cache ------
    prog("controls")
    fresh = species_fresh(3) if MUTANT != "selftest-cached" else species(3)
    used_cache = fresh is SPEC_CACHE.get(3)
    psi_f = ghz_reference(fresh)
    conj_cells = 0
    conj_hold = 0
    for pi in fresh.PERMS:
        for w in range(fresh.NW):
            for g in ROT_ORDER:
                conj_cells += 1
                lhs = Mx.from_perm(fresh.PCARR[pi]) @ (
                    fresh.LOC[(w, g)] @ Mx.from_perm(pinv(fresh.PCARR[pi])))
                rhs = fresh.LOC[(pi[w], g)]
                if MUTANT == "symmetry-break" and pi == fresh.PERMS[1] \
                        and w == 0 and g == "R1":
                    rhs = fresh.LOC[(pi[w], "R2")]
                if lhs.key() == rhs.key():
                    conj_hold += 1
    # the invariant under the arena's own action: |Hol| must not move when the
    # base node moves, and must not move when the whole instance is relabelled
    # by a wing symmetry
    ob0 = instance(sp4, psi4, first4[3], st4, base_index=0)
    ob1 = instance(sp4, psi4, first4[3], st4, base_index=1)
    relab = {}
    for pi in sp3.PERMS:
        sig = sp3.SIGMA[pi]
        psi_r = [Fr(0)] * sp3.NSYS
        for a in range(sp3.NSYS):
            psi_r[sig[a]] = psi3[a]
        Qr = pcomp(sig, pcomp(first3_bf[3], pinv(sig)))
        relab[sp3.NAME[pi]] = instance(sp3, psi_r, Qr, st3)["holonomy_order"]
    T["controls"] = {
        "the_self_test_evaluated_fresh": not used_cache,
        "the_conjugation_law_cells": conj_cells,
        "the_conjugation_law_holds_at": conj_hold,
        "base_node_invariance": {
            "base_0": ob0["holonomy_order"], "base_1": ob1["holonomy_order"],
            "invariant": ob0["holonomy_order"] == ob1["holonomy_order"]},
        "relabelling_invariance_at_three_wings": relab,
        "relabelling_invariance_holds":
            len(set(relab.values())) == 1,
        "cache": dict(CACHE_STATS),
    }
    gate("G-SELFTEST-FRESH",
         "the symmetry self-test evaluates FRESH: its species is built "
         "outside the memo, so the test measures the quantity and not the "
         "cache (RUNBOOK section 14 addendum, v13 #185)",
         not used_cache, {"used_the_cache": used_cache})
    gate("G-SYMMETRY-SELFTEST",
         "the instrument's symmetry-invariant quantities are self-tested "
         "under the symmetry's OWN action: the conjugation law "
         "P_pi U_w P_pi^-1 = U_{pi(w)} holds at %d of %d freshly evaluated "
         "cells; the based holonomy order does not move when the base node "
         "moves; and relabelling the whole instance by each wing symmetry "
         "leaves the holonomy order invariant at all %d relabellings"
         % (conj_hold, conj_cells, len(relab)),
         conj_hold == conj_cells
         and T["controls"]["base_node_invariance"]["invariant"]
         and T["controls"]["relabelling_invariance_holds"],
         T["controls"])
    hits = CACHE_STATS["hits"]
    misses = CACHE_STATS["misses"]
    if MUTANT == "cache-nolookup":
        hits = 0
    gate("G-CACHE-EXERCISED",
         "the memoisation is exercised in both directions: hits > 0 AND "
         "misses > 0 -- zero hits of zero lookups is vacuous (RUNBOOK "
         "section 14 addendum, v13 #219)",
         hits > 0 and misses > 0, {"hits": hits, "misses": misses})

    # negative controls, with teeth
    neg = {}
    neg["the identity completion at four wings"] = public(
        instance(sp4, psi4, tuple(range(sp4.NSYS)), st4))
    neg["a declared non-rule-selected four-wing completion"] = public(
        instance(sp4, psi4, transpose_labels(sp4.NSYS, 1, 3), st4))
    neg["an asymmetric setting at three wings"] = public(
        instance(sp3, psi3, first3_bf[3], ("R0", "R1", "R2")))
    if MUTANT == "negctrl-lax":
        for v in neg.values():
            v["holonomy_order"] = inst4[top4]["holonomy_order"]
    T["negative_controls"] = {
        "controls": len(neg), "per_control": neg,
        "controls_that_move_the_geometry": sum(
            1 for v in neg.values()
            if v["holonomy_order"] != inst4[top4]["holonomy_order"]),
        "the_reference_for_comparison": inst4[top4]["holonomy_order"],
        "the_three_wing_control_is_compared_against":
            inst3["A1 target ord = 3"]["holonomy_order"],
        "scope": "the asymmetric-setting control is run at THREE wings, where "
                 "the legs of a mixed setting are still affordable; the "
                 "four-wing controls are run at the declared symmetric "
                 "setting, and the scope is stated rather than implied",
    }
    gate("G-NEGATIVE-CONTROLS",
         "the negative controls have teeth: the equivariant (identity) "
         "completion collapses the four-wing geometry, and an asymmetric "
         "completion the rule did not select does not reach the ceiling "
         "either, and an asymmetric SETTING moves the three-wing geometry "
         "away from its symmetric-setting value -- so the ceiling is a "
         "property of the declared (completion, setting) pair and is measured "
         "to be",
         all(v["holonomy_order"] != inst4[top4]["holonomy_order"]
             for v in neg.values())
         and neg["an asymmetric setting at three wings"]["holonomy_order"]
         != inst3["A1 target ord = 3"]["holonomy_order"],
         T["negative_controls"])

    # -- 13. THE BREAKS, computed --------------------------------------------
    breaks = []
    if T["completion_rule_at_four_wings"]["pairs_the_rule_admits"] == 0:
        breaks.append({
            "tag": "COMPLETION-RULE-EMPTY",
            "what": "the pinned completion-selection rule admits 0 of %d "
                    "label pairs at four wings, so the ladder's reference row "
                    "has no four-wing analogue by the pinned rule"
                    % T["completion_rule_at_four_wings"]["label_pairs_censused"],
            "measured_by": "G-COMPLETION-RULE-CENSUS"})
    split_break = [k for k, v in sorted(ladder4.items())
                   if v["defect_subgroup_order"] > 1
                   and not v["the_order_factorises_over_the_wing_group"]]
    if split_break:
        breaks.append({
            "tag": "SPLIT-STRUCTURE-FAILS-AT-%d-of-%d-RUNGS"
                   % (len(split_break), len(ladder4)),
            "what": "at three wings every non-trivial instance had "
                    "|Hol| = |wing group| x |K| with all wing symmetries "
                    "inside Hol; at four wings that fails at %s"
                    % ", ".join(split_break),
            "measured_by": "G-IDENTIFICATION"})
    linear_break = (T["families"]["three_wing_linear_rungs"] > 0
                    and T["families"]["four_wing_linear_rungs"] == 0)
    if linear_break:
        breaks.append({
            "tag": "LINEAR-RUNG-NOT-REALISED",
            "what": "GL(3,2) was a realised rung at three wings; no four-wing "
                    "target realises GL(4,2), though all %d of its elements "
                    "lie inside the top rung" % len(gl4),
            "measured_by": ("G-NO-SUCH-GATE" if MUTANT == "breaks-lax"
                            else "G-FAMILIES")})
    T["breaks"] = {"modes": breaks, "count": len(breaks),
                   "reading": "the three questions the pin asks -- embedding, "
                              "ceiling, families -- all answer EXTENDS; what "
                              "breaks is the construction rule that selects "
                              "the reference completion, the split structure "
                              "at one rung, and the realisation of the linear "
                              "family as a rung"}
    gate("G-BREAKS-CENSUSED",
         "the break modes are COMPUTED from the measured tables, never "
         "listed: each mode names the gate that measured it, and a mode whose "
         "measurement does not fire is not emitted",
         all(m["measured_by"] in [g["name"] for g in GATES]
             for m in breaks),
         T["breaks"])

    # -- 14. THE VERDICT ---------------------------------------------------
    payload = {
        "rungs": T["ladder_extension"]["three_wing_rungs"],
        "rungs_embedding_in_the_top_rung":
            T["ladder_extension"]["rungs_whose_embedded_copy_lies_inside_the_top_rung"],
        "elements_outside_the_top_rung":
            T["ladder_extension"]["elements_outside_the_top_rung"],
        "ceiling_attained_at_four_wings": cel4["the_ceiling_is_attained"],
        "four_wing_ceiling": cel4["the_algebraic_ceiling"],
        "four_wing_max_holonomy": cel4["the_largest_holonomy_order_measured"],
        "four_wing_alternating_rungs": T["families"]["four_wing_alternating_rungs"],
        "four_wing_linear_rungs": T["families"]["four_wing_linear_rungs"],
        "four_wing_named_rungs": T["families"]["four_wing_named_rungs"],
        "four_wing_rungs": T["families"]["four_wing_rungs"],
        "break_modes": len(breaks),
        "breaks": [m["tag"] for m in breaks],
        "four_wing_census_completions": T["four_wing_census"]["completions_censused"],
        "four_wing_census_orbits": T["four_wing_census"]["orbits_enumerated"],
    }
    head, segs, full = build_verdict(payload)
    T["verdict_payload"] = payload
    R["verdict"] = full
    R["verdict_head"] = head
    R["verdict_segments"] = segs
    return R, T, payload, head, segs, full, inst3, inst4, sp3, sp4


# ---------------------------------------------------------------------------
# 13.  Waivers, compliance, rendering, delivery
# ---------------------------------------------------------------------------

LEDGER_GATES = ("G-FALSIFIER-CENSUS", "G-WAIVERS-VERIFIED",
                "G-FINAL-GATE-COUNT", "G-DEFERRED-GATES-EVALUATED",
                "G-NO-FLOATS-IN-RECEIPT")


def build_waivers(gate_names, falsified):
    """Every never-falsified gate gets a row whose forcing is MACHINE-CHECKED
    (RUNBOOK section 14 addendum, v14 #34): the row states WHAT forces the
    gate, and `machine_checked` is a computed predicate, not a sentence."""
    never = [n for n in gate_names if n not in falsified]
    rows = []
    for n in never:
        g = next((x for x in GATES if x["name"] == n), None)
        executed = g is not None
        deferred = n in DEFERRED_GATES
        if n in LEDGER_GATES:
            forcing = ("a LEDGER gate: its inputs are this run's own gate "
                       "list and mutant table, so no injection into a "
                       "measured quantity can reach it.  What is "
                       "machine-checked here is that it EXECUTED (or is "
                       "declared deferred and proved to execute by "
                       "G-DEFERRED-GATES-EVALUATED)")
            ok = executed or deferred
        else:
            forcing = ("no declared mutant names this gate; the row exists so "
                       "the gap is NAMED rather than hidden, and the check "
                       "below is that the gate really executed in this run")
            ok = executed
        rows.append({"gate": n, "the_gate_executed": executed,
                     "is_a_deferred_write_time_gate": deferred,
                     "forcing": forcing, "machine_checked": ok})
    return rows, never


def compliance_sweep(R):
    names = set(g["name"] for g in GATES)

    def by(*gs):
        miss = [g for g in gs if g not in names]
        if miss:
            return "MISSING: " + ", ".join(miss)
        return "APPLIED via " + ", ".join(gs)

    def mut(*ms):
        declared = set(m["name"] for m in MUTANTS)
        miss = [m for m in ms if m not in declared]
        if miss:
            return "MISSING MUTANT: " + ", ".join(miss)
        return "falsifiers " + ", ".join(ms)

    fc = R.get("falsifier_census", {})
    return [
        {"rule": "RUNBOOK 13/14/15 with every addendum binds AT DELIVERY "
                 "(#246/#313) -- including the two engraved at v14 #34, "
                 "after this unit's pin froze",
         "status": "APPLIED -- %d gates; the two post-pin engravings are "
                   "implemented as %s and %s"
                   % (len(names), "G-WAIVERS-VERIFIED", "G-VERBATIM-ANCHORS")},
        {"rule": "#34 waiver claims are gate claims: a never-falsified waiver "
                 "is itself a claim requiring verification, and a gate no "
                 "execution path evaluates may not appear as waived",
         "status": by("G-WAIVERS-VERIFIED") + "; every waiver row carries "
                   "machine_checked = the gate really executed"},
        {"rule": "#34 verbatim-text anchors: evaluated before byte anchors, "
                 "each bound to a named consumer gate, context windows not "
                 "fragments",
         "status": by("G-VERBATIM-ANCHORS") + "; %d rows, smallest window "
                   "%d characters; " % (len(VERBATIM_ANCHOR_ROWS),
                                        min(len(r[2]) for r in
                                            VERBATIM_ANCHOR_ROWS))
                   + mut("verbatim-drift")},
        {"rule": "#10 containment is not equality: the verdict gate compares "
                 "the COMPLETE emitted string against an independent rebuild",
         "status": by("G-VERDICT-STRING-EQUALITY") + "; "
                   + mut("verdict-typed-segment", "verdict-append-text",
                         "verdict-typed-families", "verdict-fully-typed",
                         "verdict-inert-segment")},
        {"rule": "#20 compliance claims are gate claims: a comparator that "
                 "cannot disagree is vacuous",
         "status": "APPLIED -- reconstruct_verdict_from_receipt() shares no "
                   "code and no input with build_verdict(); all five "
                   "injection classes are declared mutants and die on it"},
        {"rule": "#10 render from the gated object (one object, one source "
                 "of truth)",
         "status": by("G-RENDER-FROM-GATED-OBJECT") + "; " + mut("render-escape")},
        {"rule": "#20 prose renders from the receipt",
         "status": by("G-PROSE-RENDERS-FROM-THE-RECEIPT") + "; "
                   + mut("prose-claim-drift")},
        {"rule": "#20 path-value anchoring",
         "status": "APPLIED -- %d path-value rows beside %d byte rows; "
                   % (len(PATH_ANCHOR_ROWS), len(ANCHOR_ROWS))
                   + mut("path-drift", "path-value-drift")},
        {"rule": "#234 the verdict is derived inside a gate and a flip mutant "
                 "proves the derivation can fail",
         "status": by("G-VERDICT-SEGMENTS-FLIPPABLE",
                      "G-VERDICT-BOTH-HEADS-REACHABLE")
                   + " -- flippability is tested by perturbing the PAYLOAD ROW "
                     "each segment derives from; " + mut("head-constant")},
        {"rule": "#234 two independent routes are genuinely independent",
         "status": by("G-CENSUS-TWO-ROUTES", "G-GROUP-TWO-ROUTES",
                      "G-LEXFIRST-TWO-ROUTES")
                   + " -- direct enumeration vs orbit count; brute-force "
                     "closure vs a Schreier-Sims chain that never builds the "
                     "group; direct lex scan vs the structural reconstruction. "
                     "G-ADMISSION-TWO-IMPLEMENTATIONS is a memoisation TAMPER "
                     "check and is described as one, not as two routes"},
        {"rule": "#234 a cell-completeness gate catches a dropped cell",
         "status": by("G-CENSUS-CELL-COMPLETE", "G-CENSUS-TOTAL-RECOMPUTED")
                   + "; " + mut("census-cell-drop", "census-count-corrupt")},
        {"rule": "#219 a gate may not compare an object with a copy of itself "
                 "routed through the component under test",
         "status": "APPLIED -- the verdict comparator is rebuilt from the "
                   "receipt; the group orders are compared across two "
                   "algorithms that share no intermediate value"},
        {"rule": "#219 a zero-hit or zero-lookup cache gate is vacuous",
         "status": by("G-CACHE-EXERCISED") + " -- hits > 0 AND misses > 0; "
                   + mut("cache-nolookup")},
        {"rule": "#208 no gate predicate references mutant identity",
         "status": "APPLIED -- no gate reads MUTANT; every injection lives in "
                   "a measured function or in the rendered object"},
        {"rule": "#208 forced clauses are disclosures, not must-pass claims",
         "status": "APPLIED -- the n = 2 agreement with the closed form is "
                   "DISCLOSED as numerical (its parity hypothesis fails), and "
                   "the choice inventory marks each coordinate FORCED / FREE "
                   "/ EMPTY rather than asserting determination"},
        {"rule": "#24 counts are computed, never typed",
         "status": by("G-CENSUS-CELL-COMPLETE", "G-CENSUS-TOTAL-RECOMPUTED",
                      "G-COMPLETION-RULE-CENSUS")
                   + " -- every census size is gated against a DERIVED "
                     "factorial or binomial"},
        {"rule": "#175/#185 symmetry self-tests, evaluated fresh",
         "status": by("G-SYMMETRY-SELFTEST", "G-SELFTEST-FRESH") + "; "
                   + mut("symmetry-break", "selftest-cached")},
        {"rule": "#313 boundary parity: a Boolean connective in the "
                 "incidence construction carries a witness gate whose death "
                 "certificate is the alternative connective's measured delta",
         "status": by("G-CONNECTIVE-WITNESS") + "; " + mut("connective-lax")},
        {"rule": "#314 precheck doctrine: a precheck may gate which "
                 "candidates are censused but may never name the verdict",
         "status": "APPLIED -- the completion-rule census is a PRECHECK "
                   "(it decides that the reference row has no analogue); the "
                   "verdict's segments are all measured on the CENSUSED "
                   "objects: the embedding on lifted group elements, the "
                   "ceiling on measured holonomy orders, the families on "
                   "earned names"},
        {"rule": "section 15 declared-arena discipline: the arena is data",
         "status": by("G-FOUR-WING-BASE", "G-CHOICE-INVENTORY")
                   + " -- boundary, family, law, state and arena are emitted "
                     "as the declaration tables, and the choice inventory "
                     "reports what the rule forces and what it leaves free"},
        {"rule": "section 15 addendum: a like-for-like comparison matches "
                 "EVERY coordinate",
         "status": "APPLIED -- the three-wing and four-wing rows are read at "
                   "matched coordinates: same constructor, same setting "
                   "(TB-000), same preparation type, same target rule, same "
                   "base node, same two group routes"},
        {"rule": "pin CR-D: compute honesty -- caps printed and gated, "
                 "sampled sweeps labelled, BLOCKED-AT-SCALE first class",
         "status": by("G-CENSUS-SCALE-DISCLOSED", "G-IDENTIFICATION")
                   + " -- the four-wing census is EXHAUSTIVE (no sample "
                     "anywhere in this unit); the two printed caps are the "
                     "set-equality cap %d and the naive-scan cap, both gated "
                     "and both reported with what they reached"
                     % SET_EQUALITY_CAP},
        {"rule": "pin CR-D control: the three-wing values re-derived and "
                 "anchored BEFORE any four-wing number counts",
         "status": by("G-THREE-WING-RECOVERY", "G-THREE-WING-CENSUS",
                      "G-THREE-WING-LADDER", "G-THREE-WING-COMPLETION-RULE")},
        {"rule": "never-falsified census in the receipt from delivery one",
         "status": "APPLIED -- %s (%s)"
                   % (fc.get("denominator", "?"), by("G-FALSIFIER-CENSUS"))},
    ]


def jsonable(o):
    if isinstance(o, dict):
        return dict((str(k), jsonable(v)) for k, v in o.items())
    if isinstance(o, (list, tuple)):
        return [jsonable(x) for x in o]
    if isinstance(o, (set, frozenset)):
        return sorted(jsonable(x) for x in o)
    if isinstance(o, bool) or o is None or isinstance(o, (int, str)):
        return o
    return str(o)


def render_text(R):
    L = []
    A = L.append
    A("=" * 78)
    A("v14 CR-D -- THE SYMMETRY-TOWER LIMIT: FOUR WINGS")
    A("=" * 78)
    A("")
    A("VERDICT: " + R["verdict"])
    A("")
    T = R["tables"]
    A("-- THE THREE-WING RECOVERY (the control: nothing four-wing counts "
      "until this matches)")
    rec = T["three_wing_recovery"]
    A("   holonomy orders at the declared targets : %s"
      % rec["holonomy_orders_at_the_declared_targets"])
    A("   I6 declares                             : %s" % rec["I6_declares"])
    A("   the reference holonomy order            : %d (I6: %d)"
      % (rec["the_reference_holonomy_order"],
         rec["I6_declares_the_reference"]))
    A("   the completion rule returns             : %s (I6: %s)"
      % (T["three_wing_completion_rule"]["the_rule_returns"],
         T["three_wing_completion_rule"]["I6_declares"]))
    A("   the exhaustive ord census               : %s"
      % T["three_wing_census"]["route_1_brute_force_over_all_completions"])
    A("   the ladder, re-named by construction    :")
    for k, v in sorted(T["three_wing_ladder"].items()):
        A("      %-34s |Hol|=%-6d |K|=%-5d %s"
          % (k, v["holonomy_order"], v["defect_subgroup_order"],
             v["THE_TYPE"]))
    A("")
    A("-- THE FOUR-WING CONSTRUCTION")
    d = T["four_wing_declaration"]
    A("   carrier %d = %d system labels x %d pointer labels; wing group %d; "
      "settings %d; frames %d; nodes %d"
      % (d["carrier"], d["system_labels"], d["pointer_labels"],
         d["wing_symmetry_group_order"], d["settings"], d["frames"],
         d["nodes_per_setting"]))
    ci = T["choice_inventory"]
    A("   the choice inventory: %d coordinates -- %d FORCED, %d FREE, "
      "%d EMPTY, 1 declared by the pin"
      % (ci["coordinates"], ci["forced"], ci["free"], ci["empty"]))
    cr = T["completion_rule_at_four_wings"]
    A("   THE PINNED COMPLETION RULE IS EMPTY AT FOUR WINGS: %d of %d label "
      "pairs admitted (three wings: %d of %d)"
      % (cr["pairs_the_rule_admits"], cr["label_pairs_censused"],
         cr["at_three_wings_pairs_admitted"],
         cr["at_three_wings_pairs_censused"]))
    A("   mechanism: shadow-invariance == commutation at %d of %d cells; "
      "setwise stabiliser census %s"
      % (cr["shadow_invariance_equals_commutation_at"], cr["of_cells"],
         cr["setwise_stabiliser_census_over_pairs"]))
    A("")
    A("-- THE FOUR-WING CENSUS (exhaustive, by orbit count)")
    c = T["four_wing_census"]
    A("   %d completions censused at %d orbits x fibre %d; maximum defect "
      "order at P* = %d"
      % (c["completions_censused"], c["orbits_enumerated"],
         c["common_fibre_size"], c["the_maximum_order_at_P_star"]))
    A("   ord distribution: %s" % c["ord_distribution_at_P_star"])
    A("   the naive lex scan reached rank %d of %d without finding the "
      "maximum-order target"
      % (c["THE_NAIVE_LEX_SCAN"]["permutations_scanned"],
         c["THE_NAIVE_LEX_SCAN"]["of_completions"]))
    A("")
    A("-- THE FOUR-WING LADDER")
    for k, v in sorted(T["four_wing_ladder"].items()):
        A("   %-22s |Hol|=%-16d |K|=%-14d support %2d  %s"
          % (k, v["holonomy_order"], v["defect_subgroup_order"],
             v["support_size"], v["THE_TYPE"]))
        A("      identification: %s" % v["identification_method"])
    A("")
    A("-- THE LADDER-EXTENSION TEST")
    le = T["ladder_extension"]
    A("   embedding: %s" % le["the_embedding"])
    A("   %d of %d three-wing rungs lie inside the four-wing top rung; "
      "%d elements outside"
      % (le["rungs_whose_embedded_copy_lies_inside_the_top_rung"],
         le["three_wing_rungs"], le["elements_outside_the_top_rung"]))
    for k, v in sorted(le["per_rung"].items()):
        A("      %-34s %-52s outside per target %s"
          % (k, v["three_wing_rung"],
             v["elements_outside_each_four_wing_rung"]))
    A("   the reverse containment: %s" % le["the_reverse_containment_fails_at"])
    A("")
    A("-- THE CEILING")
    for n, key in ((2, "two_wings"), (3, "three_wings"), (4, "four_wings")):
        cc = T["ceiling"][key]
        A("   %d wings: |Alt(%d)| = %-15d x pointer image %-2d = %-15d ; "
          "measured max %-15d ; attained %s ; parity hypothesis %s"
          % (n, cc["non_zero_labels"],
             cc["the_alternating_group_on_the_non_zero_labels"],
             cc["the_largest_pointer_image_measured"],
             cc["the_algebraic_ceiling"],
             cc["the_largest_holonomy_order_measured"],
             cc["the_ceiling_is_attained"], cc["the_parity_hypothesis_holds"]))
    A("")
    A("-- THE GROWTH LAW")
    g = T["growth_law"]
    A("   the sequence: %s" % " -> ".join(str(x) for x in g["the_sequence"]))
    A("   the closed form %s holds at wing counts %s"
      % (g["the_closed_form"], g["the_closed_form_holds_at_wing_counts"]))
    A("   the ratio from three to four wings: %d"
      % g["the_ratio_from_three_to_four_wings"])
    A("")
    A("-- THE FAMILIES")
    f = T["families"]
    A("   four-wing rungs: %d alternating, %d linear, %d trivial, %d other"
      % (f["four_wing_alternating_rungs"], f["four_wing_linear_rungs"],
         f["four_wing_trivial_rungs"], f["four_wing_other_rungs"]))
    A("   |GL(4,2)| = %d, elements outside the top rung: %d; realised as a "
      "rung at %d targets (three wings: %d)"
      % (f["the_linear_group_at_four_wings"]["|GL(4,2)|"],
         f["the_linear_group_at_four_wings"][
             "elements_outside_the_four_wing_top_rung"],
         f["the_linear_group_at_four_wings"]["but_it_is_realised_as_a_rung_at"],
         f["the_linear_group_at_four_wings"][
             "at_three_wings_GL(3,2)_was_a_rung_at"]))
    A("")
    A("-- THE BREAKS")
    for m in T["breaks"]["modes"]:
        A("   %s: %s" % (m["tag"], m["what"]))
    A("")
    A("-- CONTROLS")
    ct = T["controls"]
    A("   conjugation law %d of %d fresh cells; base-node invariance %s; "
      "relabelling invariance %s; cache hits %d misses %d"
      % (ct["the_conjugation_law_holds_at"], ct["the_conjugation_law_cells"],
         ct["base_node_invariance"]["invariant"],
         ct["relabelling_invariance_holds"], ct["cache"]["hits"],
         ct["cache"]["misses"]))
    A("   negative controls: %d, all moving the geometry: %s"
      % (T["negative_controls"]["controls"],
         T["negative_controls"]["controls_that_move_the_geometry"]
         == T["negative_controls"]["controls"]))
    A("")
    A("-- LEDGER")
    A("   gates: %d, all passed" % R["totals"]["gates"])
    A("   anchors: %d file-byte, %d path-value, %d verbatim-text"
      % (T["anchors"]["file_byte_rows"], T["anchors"]["path_value_rows"],
         T["anchors"]["verbatim_text_rows"]))
    A("   mutants declared: %d ; never-falsified gates: %s"
      % (R["totals"]["mutants"], R["falsifier_census"]["denominator"]))
    A("")
    A("=" * 78)
    A("VERDICT: " + R["verdict"])
    A("=" * 78)
    return "\n".join(L) + "\n"


def paper_claims(R):
    """Every load-bearing numeric sentence of the paper, RENDERED HERE from
    the receipt object (RUNBOOK section 13 addendum, v14 #20)."""
    T = R["tables"]
    c = T["four_wing_census"]
    cel4 = T["ceiling"]["four_wings"]
    le = T["ladder_extension"]
    f = T["families"]
    g = T["growth_law"]
    cr = T["completion_rule_at_four_wings"]
    ci = T["choice_inventory"]
    sp4_perms_for_claims = range(
        T["four_wing_declaration"]["wing_symmetry_group_order"])
    claims = {
        "recovery": "the four declared-target holonomy orders %s, the "
                    "reference order %d and the top defect subgroup %d"
                    % (T["three_wing_recovery"][
                           "holonomy_orders_at_the_declared_targets"],
                       T["three_wing_recovery"]["the_reference_holonomy_order"],
                       T["three_wing_recovery"]["the_top_defect_subgroup"]),
        "rule_empty": "%d of %d label pairs" % (cr["pairs_the_rule_admits"],
                                                cr["label_pairs_censused"]),
        "rule_three_wings": "%d of %d" % (cr["at_three_wings_pairs_admitted"],
                                          cr["at_three_wings_pairs_censused"]),
        "readings": "reading A %d of %d wing symmetries, equivalence %d of "
                    "%d cells; reading B %d of %d, equivalence %d of %d"
                    % (cr["THE_READING_SCOPE"][
                           "reading_A_the_declared_TYPE_all_one_label"][
                           "wing_symmetries_leaving_the_preparation_shadow_"
                           "invariant"],
                       len(sp4_perms_for_claims),
                       cr["THE_READING_SCOPE"][
                           "reading_A_the_declared_TYPE_all_one_label"][
                           "shadow_invariance_equals_commutation_at"],
                       cr["THE_READING_SCOPE"][
                           "reading_A_the_declared_TYPE_all_one_label"][
                           "of_cells"],
                       cr["THE_READING_SCOPE"]["reading_B_label_7_literally"][
                           "wing_symmetries_leaving_the_preparation_shadow_"
                           "invariant"],
                       len(sp4_perms_for_claims),
                       cr["THE_READING_SCOPE"]["reading_B_label_7_literally"][
                           "shadow_invariance_equals_commutation_at"],
                       cr["THE_READING_SCOPE"]["reading_B_label_7_literally"][
                           "of_cells"]),
        "stabilisers": "%s" % cr["setwise_stabiliser_census_over_pairs"],
        "inventory": "%d coordinates, %d forced, %d free, %d empty"
                     % (ci["coordinates"], ci["forced"], ci["free"],
                        ci["empty"]),
        "census": "%d completions at %d orbits of common fibre %d"
                  % (c["completions_censused"], c["orbits_enumerated"],
                     c["common_fibre_size"]),
        "maxord": "the maximum defect order at P* is %d"
                  % c["the_maximum_order_at_P_star"],
        "ladder": "; ".join(
            "%s: |Hol| = %d, |K| = %d, %s"
            % (k, v["holonomy_order"], v["defect_subgroup_order"],
               v["THE_TYPE"])
            for k, v in sorted(T["four_wing_ladder"].items())),
        "embedding": "%d of %d rungs, %d elements outside"
                     % (le["rungs_whose_embedded_copy_lies_inside_the_top_rung"],
                        le["three_wing_rungs"],
                        le["elements_outside_the_top_rung"]),
        "ceiling": "|Alt(15)| x %d = %d, attained"
                   % (cel4["the_largest_pointer_image_measured"],
                      cel4["the_algebraic_ceiling"]),
        "growth": " -> ".join(str(x) for x in g["the_sequence"]),
        "families": "%d alternating, %d linear"
                    % (f["four_wing_alternating_rungs"],
                       f["four_wing_linear_rungs"]),
        "gl4": "|GL(4,2)| = %d, %d outside the top rung"
               % (f["the_linear_group_at_four_wings"]["|GL(4,2)|"],
                  f["the_linear_group_at_four_wings"][
                      "elements_outside_the_four_wing_top_rung"]),
        "instrument": "%d gates, all passed" % R["totals"]["gates"],
        "verdict": R["verdict"],
        "three_wing_rows": "; ".join(
            "%d/%d" % (v["holonomy_order"], v["defect_subgroup_order"])
            for k, v in sorted(T["three_wing_ladder"].items())),
        "four_wing_rows": "; ".join(
            "%d/%d/%d" % (v["holonomy_order"], v["defect_subgroup_order"],
                          v["support_size"])
            for k, v in sorted(T["four_wing_ladder"].items())),
        "four_wing_pointer_rows": "; ".join(
            "%d/%d" % (v["pointer_image_order"],
                       v["wing_symmetries_inside_the_holonomy"])
            for k, v in sorted(T["four_wing_ladder"].items())),
        "extension_rows": "; ".join(
            "%d:%s" % (v["order"], "/".join(
                str(v["elements_outside_each_four_wing_rung"][t])
                for t in sorted(v["elements_outside_each_four_wing_rung"])))
            for k, v in sorted(le["per_rung"].items())),
        "weights": "; ".join(
            "%d:%s" % (v["support_size"], v["the_weight_threshold"])
            for k, v in sorted(T["support_weight_structure"][
                "per_rung"].items())),
        "ratio": "%d" % g["the_ratio_from_three_to_four_wings"],
        "naive_scan": "reached rank %d of %d"
                      % (c["THE_NAIVE_LEX_SCAN"]["permutations_scanned"],
                         c["THE_NAIVE_LEX_SCAN"]["of_completions"]),
        "three_wing_census_size": "%d"
                                  % T["three_wing_census"][
                                      "completions_censused"],
        "three_wing_census": "%s" % T["three_wing_census"][
            "route_1_brute_force_over_all_completions"],
        "growth_points": "; ".join(
            "%d:%d" % (p["wings"], p["the_maximum_holonomy_order_measured"])
            for p in g["points"]),
        "anchors": "%d verbatim-text, %d file-byte, %d path-value"
                   % (T["anchors"]["verbatim_text_rows"],
                      T["anchors"]["file_byte_rows"],
                      T["anchors"]["path_value_rows"]),
        "mutants": "%d declared mutants; %s never falsified"
                   % (len(MUTANTS),
                      R.get("falsifier_census", {}).get("denominator", "?")),
    }
    if MUTANT == "prose-claim-drift":
        claims["ceiling"] = "|Alt(15)| x 25 = 1, attained"
    if os.path.exists(PAPER):
        with open(PAPER, "r") as fh:
            txt = fh.read()
        ph = sha12(PAPER)
    else:
        txt, ph = "", None
    missing = [k for k, v in sorted(claims.items()) if v not in txt]
    return claims, ph, missing, txt


def deliver():
    R, T, payload, head, segs, full = run()[:6]

    # -- THE VERDICT GATES -------------------------------------------------
    R["totals"]["gates"] = len(GATES)
    R["falsifier_census"] = {}
    rebuilt = reconstruct_verdict_from_receipt(R)
    gate("G-VERDICT-STRING-EQUALITY",
         "the COMPLETE emitted verdict string equals a string reconstructed "
         "INDEPENDENTLY from the receipt object's own measured tables -- "
         "equality, not containment, and a comparator that CAN disagree "
         "(RUNBOOK section 14 addenda, v14 #10 and #20)",
         full == rebuilt,
         {"emitted": full, "rebuilt": rebuilt,
          "first_difference": ([i for i in range(min(len(full), len(rebuilt)))
                                if full[i] != rebuilt[i]] or [None])[0]})

    # every segment flippable AT ITS MEASUREMENT
    flips = {}
    for s in SEGMENT_ORDER:
        p2 = dict(payload)
        if s == "EMBEDDING":
            p2["elements_outside_the_top_rung"] = 1
            p2["rungs_embedding_in_the_top_rung"] = 0
        elif s == "CEILING":
            p2["ceiling_attained_at_four_wings"] = False
        elif s == "FAMILIES":
            p2["four_wing_alternating_rungs"] = 0
            p2["four_wing_linear_rungs"] = 4
        elif s == "BREAKS":
            p2["break_modes"] = 0
            p2["breaks"] = []
        elif s == "SCALE":
            p2["four_wing_census_completions"] = 1
        _, s2, _ = build_verdict(p2)
        flips[s] = (s2[s] != segs[s])
    gate("G-VERDICT-SEGMENTS-FLIPPABLE",
         "every verdict segment is flippable AT ITS MEASUREMENT: perturbing "
         "the payload row the segment derives from changes the segment "
         "string.  A segment that cannot move is a constant wearing a "
         "measurement's clothes",
         all(flips.values()), flips)

    p_neg = dict(payload)
    p_neg["ceiling_attained_at_four_wings"] = False
    h_neg, _, _ = build_verdict(p_neg)
    p_pos = dict(payload)
    h_pos, _, _ = build_verdict(p_pos)
    gate("G-VERDICT-BOTH-HEADS-REACHABLE",
         "both pre-registered heads are reachable from the same derivation: "
         "the measured payload gives %s, and a payload differing only in the "
         "ceiling row gives the other head" % head,
         h_pos != h_neg and {h_pos, h_neg} == {"CRD-TOWER-EXTENDS",
                                               "CRD-TOWER-BREAKS"},
         {"measured_head": h_pos, "perturbed_head": h_neg})

    # -- THE FALSIFIER CENSUS AND THE WAIVERS ------------------------------
    gate_names = [g["name"] for g in GATES] + ["G-FALSIFIER-CENSUS",
                                               "G-WAIVERS-VERIFIED"]
    gate_names = gate_names + [n for n in DEFERRED_GATES
                               if n not in gate_names]
    falsified = {}
    for m in MUTANTS:
        falsified.setdefault(m["expected_gate"], []).append(m["name"])
    waiver_rows, never = build_waivers(gate_names, falsified)
    WAIVERS.extend(waiver_rows)
    R["falsifier_census"] = {
        "gates": len(gate_names),
        "gates_with_a_declared_falsifier":
            len([n for n in gate_names if n in falsified]),
        "never_falsified": never, "never_falsified_count": len(never),
        "denominator": "%d of %d gates" % (len(never), len(gate_names)),
        "falsifier_map": dict((k, sorted(v)) for k, v in
                              sorted(falsified.items()) if k in gate_names),
        "deferred_gates_evaluated_at_write_time": list(DEFERRED_GATES),
        "waivers": waiver_rows, "waivers_censused": len(waiver_rows),
        "note": "a gate with no declared falsifier is NAMED here, never "
                "waived silently; every waiver row is machine-checked to name "
                "a gate that really executed (RUNBOOK section 14 addendum, "
                "v14 #34)",
    }
    gate("G-FALSIFIER-CENSUS",
         "the never-falsified set is computed from the declared mutant table "
         "against the gate ledger and emitted with an honest denominator",
         len(gate_names) == len(set(gate_names))
         and set(falsified) <= set(gate_names),
         {"gates": len(gate_names), "never_falsified": len(never),
          "declared_mutants": len(MUTANTS)})
    gate("G-WAIVERS-VERIFIED",
         "WAIVER CLAIMS ARE GATE CLAIMS (RUNBOOK section 14 addendum, v14 "
         "#34): every never-falsified gate carries a row whose forcing is "
         "machine-checked against the executed ledger, and no waived gate is "
         "one that no execution path evaluates",
         all(w["machine_checked"] for w in waiver_rows)
         and all(w["gate"] in gate_names for w in waiver_rows)
         and all(w["gate"] not in falsified for w in waiver_rows),
         {"waivers": len(waiver_rows),
          "rows": [w["gate"] for w in waiver_rows]})

    R["mutants"] = MUTANTS
    R["anchors"] = ANCHORS
    # the totals the OUTPUT renders must be in the gated object BEFORE the
    # render check reads it -- the text renders from the receipt, not from a
    # module global (RUNBOOK section 13 addendum, v14 #10)
    R["totals"].update({"anchors": len(ANCHORS), "mutants": len(MUTANTS),
                        "gates_passed": sum(1 for g in GATES if g["passed"])})
    R["compliance"] = compliance_sweep(R)

    # -- WRITE-TIME GATES --------------------------------------------------
    if MUTANT == "internal-contradiction":
        R["tables"]["four_wing_ladder"][
            "A1 target ord = 1"]["holonomy_order"] = 10 ** 20

    payload_json = jsonable(R)
    text = render_text(R)
    if MUTANT == "render-escape":
        # A RENDERING PATH THAT BYPASSES THE GATED OBJECT: the emitted text
        # carries a number the receipt does not (RUNBOOK section 13 addendum,
        # v14 #10 -- one object, one source of truth)
        text = text.replace(
            str(R["tables"]["ceiling"]["four_wings"]["the_algebraic_ceiling"]),
            "999999999999")

    # RENDER FROM THE GATED OBJECT, TOTAL OVER EVERY RENDERED FIELD (RUNBOOK
    # section 13 addendum, v14 #10 -- one object, one source of truth).  The
    # check is not a spot list: EVERY multi-digit integer token of the emitted
    # text is required to occur as an integer VALUE somewhere in the gated
    # receipt object.  A rendering path that puts a number into the text
    # which the receipt does not carry dies here, whatever field it touched.
    def receipt_integers(o, acc):
        if isinstance(o, bool):
            return
        if isinstance(o, int):
            acc.add(o)
        elif isinstance(o, dict):
            for k, v in o.items():
                if isinstance(k, str) and k.lstrip("-").isdigit():
                    acc.add(int(k))
                receipt_integers(v, acc)
        elif isinstance(o, (list, tuple)):
            for v in o:
                receipt_integers(v, acc)

    values = set()
    receipt_integers(R, values)
    strvals = set(str(v) for v in values)
    tokens = []
    cur = ""
    for ch in text:
        if ch.isdigit():
            cur += ch
        else:
            if len(cur) >= 2:
                tokens.append(cur)
            cur = ""
    if len(cur) >= 2:
        tokens.append(cur)
    unbacked = sorted(set(t for t in tokens if t not in strvals))
    rendered_ok = (len(unbacked) == 0)
    checks = [{"multi_digit_tokens_in_the_emitted_text": len(tokens),
               "distinct_tokens": len(set(tokens)),
               "integer_values_in_the_gated_receipt": len(values),
               "tokens_with_no_backing_value": unbacked[:6],
               "of_unbacked_tokens": len(unbacked)}]
    consistent = (R["tables"]["ceiling"]["four_wings"][
        "the_largest_holonomy_order_measured"]
        == max(v["holonomy_order"] for v in
               R["tables"]["four_wing_ladder"].values()))
    gate("G-RENDER-FROM-GATED-OBJECT",
         "the object the gates checked IS the object the receipt and the "
         "output render from -- TOTAL over every rendered field: every "
         "multi-digit integer token of the emitted text is required to occur "
         "as an integer value in the gated receipt object, so a rendering "
         "path that bypasses the gated object dies here whatever field it "
         "touched",
         rendered_ok, {"checks": checks})
    gate("G-RECEIPT-CONSISTENT",
         "the receipt does not contradict itself: the ceiling table's largest "
         "measured holonomy order equals the maximum over the ladder table's "
         "own rows",
         consistent,
         {"ceiling_row": R["tables"]["ceiling"]["four_wings"][
             "the_largest_holonomy_order_measured"],
          "ladder_max": max(v["holonomy_order"] for v in
                            R["tables"]["four_wing_ladder"].values())})
    floats = []

    def scan(o, path=""):
        if isinstance(o, FLOAT_T):
            floats.append(path)
        elif isinstance(o, dict):
            for k, v in o.items():
                scan(v, path + "." + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                scan(v, path + "[%d]" % i)
    scan(payload_json)
    gate("G-NO-FLOATS-IN-RECEIPT", "the emitted receipt contains no float",
         len(floats) == 0, {"floats": floats[:4]})

    # the claim renders the FINAL gate count: three gates still follow
    # (the prose gate, the count gate, the deferred-gate gate)
    R["totals"]["gates"] = len(GATES) + 3
    claims, ph, missing, _ = paper_claims(R)
    R["paper_claims"] = {
        "paper": "v14/paper-08-tower-four-wings.md",
        "paper_sha256_prefix": ph, "claims_rendered": len(claims),
        "claims_present_in_the_paper": len(claims) - len(missing),
        "claims_missing": missing, "rendered": dict(sorted(claims.items())),
        "rule": "every load-bearing numeric sentence of the paper is RENDERED "
                "HERE from the measured object and must appear VERBATIM in "
                "the paper",
    }
    gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
         "every load-bearing numeric sentence of paper-08 is rendered from "
         "the receipt object and appears verbatim in the paper",
         ph is not None and len(missing) == 0,
         {"claims": len(claims), "missing": missing[:8],
          "the_missing_claims_as_rendered": dict(
              (k, claims[k]) for k in missing[:8]),
          "paper_sha256_prefix": ph})

    gate("G-FINAL-GATE-COUNT",
         "the gate count the paper renders equals the number of gates this "
         "run registered",
         R["paper_claims"]["rendered"]["instrument"]
         == "%d gates, all passed" % (len(GATES) + 2),
         {"registered": len(GATES) + 2,
          "claimed": R["paper_claims"]["rendered"]["instrument"]})
    gate("G-DEFERRED-GATES-EVALUATED",
         "the write-time gates named in the falsifier census really did run",
         all(d in [g["name"] for g in GATES] for d in DEFERRED_GATES
             if d != "G-DEFERRED-GATES-EVALUATED"),
         {"deferred": list(DEFERRED_GATES)})

    # the final ledger, after EVERY gate has run
    fnames = [g["name"] for g in GATES]
    nf = [n for n in fnames if n not in falsified]
    R["totals"]["gates"] = len(fnames)
    R["falsifier_census"]["gates"] = len(fnames)
    R["falsifier_census"]["never_falsified"] = nf
    R["falsifier_census"]["never_falsified_count"] = len(nf)
    R["falsifier_census"]["gates_with_a_declared_falsifier"] = len(
        [n for n in fnames if n in falsified])
    R["falsifier_census"]["denominator"] = "%d of %d gates" % (len(nf),
                                                               len(fnames))
    R["falsifier_census"]["falsifier_map"] = dict(
        (k, sorted(v)) for k, v in sorted(falsified.items()) if k in fnames)
    rows2, _ = build_waivers(fnames, falsified)
    R["falsifier_census"]["waivers"] = rows2
    R["falsifier_census"]["waivers_censused"] = len(rows2)
    R["compliance"] = compliance_sweep(R)
    R["gates"] = GATES
    R["totals"].update({
        "anchors": len(ANCHORS), "mutants": len(MUTANTS),
        "gates_passed": sum(1 for g in GATES if g["passed"]),
    })
    payload_json = jsonable(R)
    text = render_text(R)
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
        print("  %-24s exit=%d named_gate=%s artifacts_unchanged=%s  %s"
              % (m["name"], proc.returncode, named, unchanged,
                 "DEAD" if good else "SURVIVED"))
        sys.stdout.flush()
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
        sys.stderr.write("unknown argument\n")
        return 2
    try:
        return deliver()
    except GateFailure as e:
        sys.stderr.write(str(e) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
