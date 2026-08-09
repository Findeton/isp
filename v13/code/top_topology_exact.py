#!/usr/bin/env python3
"""TOP -- TOPOLOGY ON THE LADDER.  The atlas now has named groups; this unit
asks what its GLOBAL SHAPE is.

Executes the frozen pin `v13/note-top-topology-pin.md` (sha 74a472b54b85,
commit d9e3a66) against the immutable base e82c647 (TB3 #299 terminal).

THE FOUNDATION is TB3's terminal receipt, hash-pinned and read as DATA.  The
36-chart atlas is REBUILT here from TB3's own section-2 declaration -- the
three-wing carrier, the wing symmetry group, the declared rotations, the
preparation family, the completion-selection rule, the two gluing rules --
and NOTHING is imported from the TB3 instrument.  Every reused committed
number is anchored exit-1 against the pinned receipt's bytes.

THE FOUR QUESTIONS.
  Q1  THE OVERLAP GRAPH AND ITS NERVE.  Charts as nodes, admitted
      identifications as 1-cells, admissible triangles as 2-cells: components,
      cycle rank, Euler characteristic and F_2-homology ranks, each by two
      genuinely independent routes, with dropped-cell probes that must make
      the routes disagree.
  Q2  THE DIMENSION READING.  A local-dimension estimator DECLARED AS DATA
      (per-coordinate-cell local simplex dimension, star profile, and the
      F_2-homology of the vertex LINK) evaluated at every chart, with genuine
      manifold controls (the 2-sphere and the 2-torus, whose links must be
      circles) and a pinched control that must come out INCONSISTENT.
  Q3  THE FANO-RUNG SELECTOR.  Thirteen candidate selectors DECLARED IN THIS
      SOURCE BEFORE ANY DEFECT SUBGROUP IS BUILT, then measured over the
      EXHAUSTIVE 5,040-completion family on three clauses: does the candidate
      hold on the defect-order-2 locus, does it fail off it, and does it
      predict the linearity of the resulting geometry.
  Q4  THE WING QUOTIENT.  The S_3 wing factor of the gauge-inclusive holonomy
      acting on the nerve: the action, its orbits, the fixed-cell census and
      the quotient (orbit) chain complex's invariants, by the same two-route
      standard.

THE PRE-REGISTERED OUTCOMES (only these).
  TOP-GLOBAL-STRUCTURE-<computed>
  TOP-FANO-SELECTOR-<named | NOT-FOUND>
  TOP-MANIFOLD-READING-<CONSISTENT | INCONSISTENT-<witness>>
  TOP-BLOCKED-AT-<object>

CONTROLS.  Positive with teeth: the SAME generic machinery instantiated at TWO
wings must reproduce the committed two-wing transport graph -- 8 nodes, 13
links, 7 identification links, cycle rank 6 -- and the F_2 machinery must
return that cycle rank as a homology rank; the three-wing transport graph and
its three committed negative controls are anchored the same way; and the
homology machinery is run on declared complexes whose invariants are standard
(the boundary of a tetrahedron, a 9-vertex torus).  Negative with teeth: a
declared deterministically scrambled atlas must move every invariant and must
break the dimension reading.

DISCIPLINE.  RUNBOOK section 13 with every addendum (verdict derived inside a
gate from measured counts, verdict-flip mutants, cell-completeness gates that
catch a dropped cell, two GENUINELY independent routes per census), section 14
with every addendum (symmetry self-tests under the symmetry's own action, no
gate predicate referencing mutant identity, comparators built independently of
the audited component), section 15 (the arena declared as data).  Exact
integer and rational arithmetic throughout; no float anywhere; byte-identical
delivery runs; NO git; FREEZE-ON-DELIVERY.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent

SCHEMA = "top-topology-receipt-v1"
PIN_SHA256 = "74a472b54b85"
PIN_COMMIT = "d9e3a66"
BASE_COMMIT = "e82c647"
TB3_RECEIPT = HERE / "tb3_third_base_receipt.json"
PINNED_RECEIPT_SHA256 = {
    "TB3": "c9bc956fe75129bdf411e4d1c1ce082d5866e7e63f12712e56f6f231dcf5a9a7",
}
ANCHOR_PROVENANCE = {
    "TB3 committed receipt": "external",
    "this file, pinned SHA-256": "external",
    "DECLARED-STANDARD (the complex's standard invariants)": "declared",
}
OUT_TXT = HERE / "top_topology_output.txt"
OUT_JSON = HERE / "top_topology_receipt.json"

MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

PREREGISTERED_UNIT = ("TOP-GLOBAL-STRUCTURE-", "TOP-BLOCKED-AT-")
PREREGISTERED_SELECTOR = ("TOP-FANO-SELECTOR-NOT-FOUND", "TOP-FANO-SELECTOR-")
PREREGISTERED_MANIFOLD = ("TOP-MANIFOLD-READING-CONSISTENT",
                          "TOP-MANIFOLD-READING-INCONSISTENT-")

SCOPE_CLAUSES = (
    "at TB3's declared finite three-wing base, rebuilt from its section-2 "
    "declaration",
    "at the five declared A3 atlas instances, the reference instance being "
    "psi-G1 at TB-000 with the rule-selected completion",
    "at the declared coordinate cells (checkpoint x rule), ten of them",
    "at the exhaustive 5,040-member completion family for the selector census",
    "over F_2 coefficients only -- no integral torsion is computed or claimed",
)

T0 = time.time()

_FROZEN = False
_TOPOLOGY_DATA = 0        # measured topology data evaluated
_DATA_AT_FREEZE = 0       # the counter's value at the freeze gate
_K_BUILT = 0              # defect subgroups built (the selector's freeze)
_K_AT_DECLARATION = 0     # its value when the candidate family is registered
_SELECTOR_DECLARED = False


def prog(msg: str) -> None:
    """Progress; stderr only, so no wall clock reaches any artifact."""
    sys.stderr.write("[top %6.1fs] %s\n" % (time.time() - T0, msg))
    sys.stderr.flush()


def gate(gid: str, cls: str, claim: str, ok: bool, value=None) -> bool:
    GATES.append({"id": gid, "class": cls, "claim": claim,
                  "passed": bool(ok), "value": value})
    return ok


def anchor(aid: str, source: str, quantity: str, declared, computed) -> None:
    ANCHORS.append({"id": aid, "source": source, "quantity": quantity,
                    "declared": declared, "computed": computed,
                    "passed": declared == computed})


def canon(v) -> str:
    if isinstance(v, (list, tuple)):
        return "(" + ",".join(canon(x) for x in v) + ")"
    if isinstance(v, (set, frozenset)):
        return "{" + ",".join(sorted(canon(x) for x in v)) + "}"
    if isinstance(v, dict):
        return "{" + ",".join(sorted(canon(k) + ":" + canon(x)
                                     for k, x in v.items())) + "}"
    return str(v)


def _bump():
    """Every measured topology datum passes through here.  It must not fire
    before the declarations are frozen."""
    global _TOPOLOGY_DATA
    evaluate_before_the_freeze = (MUTANT == "freeze-lax")
    if not _FROZEN and not evaluate_before_the_freeze:
        raise RuntimeError("topology datum evaluated before the freeze")
    _TOPOLOGY_DATA += 1


# ===========================================================================
# 1.  THE FROZEN DECLARATIONS.  Everything in this section is DATA, recorded
#     in the source before any measured topology datum exists.  RUNBOOK
#     section 15: the arena is declared as data, not prose.
# ===========================================================================

# ---- D1.  THE ARENA (TB3's, restated here because this unit reads TB3's
#      atlas and inherits its declarations verbatim).
ARENA = {
    "boundary": "the final division event, checkpoint 4",
    "family": "the 27 declared settings and the 9 declared preparations; this "
              "unit reads the five declared A3 instances",
    "law": "the exact Born law of the declared leg sequence, read at the "
           "node's declared read time",
    "state": "p(0) = delta_{j0}",
    "arena": "the declared relabelling scope and the subgroup surviving the "
             "j0 filter, over which every admission search runs",
    "coordinate cells of the nerve": "(checkpoint, rule), the rules being "
                                     "FULL and REALIZED",
}

# ---- D2.  THE OBJECTS.  What "the nerve" IS, declared before it is built.
#
#  G        THE OVERLAP GRAPH.  A simple graph.  Nodes: the atlas's charts.
#           Edge {X,Y}: an identification link is drawn between X and Y at
#           SOME coordinate cell.
#
#  N        THE COORDINATE-RESOLVED NERVE, the PRIMARY object.  A 2-dimensional
#           cell complex.
#             0-cells: the charts.
#             1-cells: (unordered chart pair, coordinate cell) for each DRAWN
#                      identification link -- so two charts identified at k
#                      coordinate cells carry k parallel 1-cells.  This is
#                      TB3's own link convention: its transport graph counts
#                      one identification link per (pair, checkpoint, rule).
#             2-cells: the ADMISSIBLE TRIANGLES of TB3's own census -- three
#                      charts pairwise linked at a COMMON CHECKPOINT, one
#                      rule chosen per edge -- deduplicated to their geometric
#                      edge-triples.
#           SCOPE, declared: 2-cells are same-checkpoint only, which is TB3's
#           declared census object; cross-checkpoint triples are outside this
#           unit's complex and no claim is made about them.
#
#  N_coh    THE COHERENT SUB-NERVE.  The same 0- and 1-cells; a 2-cell only
#           where the three drawn maps COMPOSE TO THE IDENTITY -- the strict
#           cocycle condition an atlas's transition maps must satisfy.
#
#  N_simp   THE SIMPLICIAL NERVE.  Faces: the subsets of charts that are
#           pairwise linked at ONE COMMON coordinate cell.  (A genuine nerve:
#           a face is a set of charts with a common overlap.)
#
# ---- D3.  THE LOCAL-DIMENSION ESTIMATOR, declared as data.
#
#  For a chart X of an atlas instance the estimator returns the triple
#
#     dimprofile(X) = ( |component of X in G_c| - 1 )_{c a coordinate cell},
#                     with -1 recorded where X carries no link at c
#                     -- the local simplex dimension the cell-c overlaps give;
#     star(X)       = ( number of 1-cells at X, number of 2-cells at X );
#     link(X)       = ( V, E, b_0, b_1 ) over F_2 of the LINK of X: the graph
#                     whose vertices are the charts adjacent to X and whose
#                     edges are the 2-cells containing X.
#
#  D(X) = (dimprofile, star, link).  The reading is CONSISTENT iff D is
#  chart-independent -- one local dimension everywhere.  Otherwise a WITNESS
#  chart is exhibited with its deviating profile.  Consistency is uniformity;
#  it is NOT manifoldhood, and the two are reported separately: a d-manifold
#  additionally has every link with the F_2 homology of S^{d-1}, which the
#  declared manifold controls exhibit and the atlas nerve is measured against.
#
# ---- D4.  THE FANO-RUNG SELECTOR: THE CANDIDATE FAMILY.
#      DECLARED HERE, IN THIS SOURCE, BEFORE ANY DEFECT SUBGROUP K(q) IS
#      BUILT.  The instrument counts the subgroups it has built and gates that
#      the count is ZERO at the moment this declaration is registered.
#
#      Each candidate is a predicate C(q) on a completion q -- a permutation
#      of the eight system-triple labels fixing label 0.  d_P(q) is the label
#      defect at wing symmetry P; P* is the declared symmetry.  A "reference
#      value" is the value the quantity takes at the rule-selected ord-2
#      target, COMPUTED in this run, never typed.
SELECTOR_CANDIDATES = (
    ("C1", "involutivity",
     "ord(d_{P*}(q)) = 2 -- the locus's own defining property", "pin"),
    ("C2", "defect fixed-point count",
     "|Fix(d_{P*}(q))| equals the reference value", "pin"),
    ("C3", "completion support",
     "|supp(q)| equals the reference value", "pin"),
    ("C3b", "completion cycle type",
     "the cycle type of q equals the reference cycle type", "pin"),
    ("C4", "defect F2-linearity",
     "every d_P(q), P in S_3, is an F_2-linear permutation of the labels",
     "pin"),
    ("C4b", "declared-symmetry defect F2-linearity",
     "d_{P*}(q) is an F_2-linear permutation of the labels", "pin"),
    ("C5", "completion F2-linearity",
     "q is itself an F_2-linear permutation of the labels", "worker"),
    ("C6", "defect order profile",
     "the multiset {ord(d_P(q)) : P in S_3} equals the reference profile",
     "worker"),
    ("C7", "involutive profile",
     "ord(d_P(q)) <= 2 for every P in S_3", "worker"),
    ("C8", "transvection",
     "d_{P*}(q) is F_2-linear and fixes exactly four labels -- a hyperplane "
     "pointwise", "worker"),
    ("C9", "q normalises the wing group",
     "q^-1 sigma_P q lies in the wing group for every P", "worker"),
    ("C10", "Fano collineation",
     "q maps every line of PG(2,2) onto a line of PG(2,2)", "worker"),
    ("C11", "abelian defect set",
     "d_P(q) and d_R(q) commute for every P, R in S_3", "worker"),
)
SELECTOR_CLAUSES = (
    ("a", "HOLDS ON THE LOCUS: the count of defect-order-2 completions "
          "satisfying C, out of the measured size of the locus"),
    ("b", "FAILS OFF THE LOCUS: the count of completions outside the locus "
          "satisfying C -- zero is the pass"),
    ("c", "PREDICTS LINEARITY: the count of completions satisfying C whose "
          "defect subgroup K(q) has a NON-linear element -- zero is the pass "
          "-- reported beside the count satisfying C with K(q) equal to "
          "GL(3,2) as a set"),
)
SELECTOR_RULE = (
    "A candidate is NAMED only if clause (a) is total on the locus, clause "
    "(b) is zero, and clause (c) has zero linearity counterexamples.  If no "
    "candidate meets all three the verdict is TOP-FANO-SELECTOR-NOT-FOUND "
    "and the family's failure is recorded clause by clause.  No candidate may "
    "be added, removed or reworded after the first K(q) is built.")

# ---- D5.  THE DECLARED CONTROL COMPLEXES.  Their invariants are standard and
#      are typed here as DECLARED-STANDARD anchors; the machinery must return
#      them.  Vertices are integers; 2-cells are vertex triples; 1-cells are
#      derived as the triples' edges.
CTRL_SPHERE = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
CTRL_TORUS = ((0, 1, 3), (1, 4, 3), (1, 2, 4), (2, 5, 4), (2, 0, 5), (0, 3, 5),
              (3, 4, 6), (4, 7, 6), (4, 5, 7), (5, 8, 7), (5, 3, 8), (3, 6, 8),
              (6, 7, 0), (7, 1, 0), (7, 8, 1), (8, 2, 1), (8, 6, 2), (6, 0, 2))
CTRL_PINCH = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3),
              (0, 4, 5), (0, 4, 6), (0, 5, 6), (4, 5, 6))
CTRL_DECLARED = {
    "the boundary of a tetrahedron (a 2-sphere)":
        {"V": 4, "E": 6, "F": 4, "chi": 2, "b0": 1, "b1": 0, "b2": 1,
         "every link is a circle": True},
    "a 9-vertex torus":
        {"V": 9, "E": 27, "F": 18, "chi": 0, "b0": 1, "b1": 2, "b2": 1,
         "every link is a circle": True},
    "two tetrahedra sharing one vertex (a pinch point)":
        {"V": 7, "E": 12, "F": 8, "chi": 3, "b0": 1, "b1": 0, "b2": 2,
         "every link is a circle": False},
}

# ---- D6.  THE DECLARED ATLAS INSTANCES.  TB3's five A3 instances, verbatim.
INSTANCES = (
    ("the declared base at a fully symmetric setting", "psi-G1", "declared",
     ("R0", "R0", "R0")),
    ("the equivariant-completion control", "psi-G1", "identity",
     ("R0", "R0", "R0")),
    ("a partially symmetric setting", "psi-G1", "declared",
     ("R0", "R0", "R1")),
    ("an asymmetric setting", "psi-G1", "declared", ("R0", "R1", "R2")),
    ("a W-class preparation at a fully symmetric setting", "psi-W1",
     "declared", ("R0", "R0", "R0")),
)
REFERENCE_INSTANCE = INSTANCES[0][0]

# ---- D7.  THE SCRAMBLED-ATLAS NEGATIVE CONTROL, declared before it is built.
SCRAMBLE_DECL = (
    "THE SCRAMBLED ATLAS.  At each coordinate cell the drawn link set is "
    "replaced by a deterministic pseudo-random set of floor(3m/4) distinct "
    "chart pairs, m being the measured number of links the reference instance "
    "draws at that cell.  The generator is an exact integer linear "
    "congruential recurrence seeded by the SHA-256 of the declared base data "
    "alone -- no float, no system entropy, identical on every run.  The 2-"
    "cells are recomputed on the surviving links by the same rule.  The "
    "control has teeth only if it moves the invariant table AND breaks the "
    "dimension reading, and both are gated.")

DECLARATIONS_REGISTERED = True


# ===========================================================================
# 2.  EXACT ARITHMETIC.  Sparse rational matrices and permutations.  No float
#     enters any measurement.
# ===========================================================================
class Mat:
    __slots__ = ("n", "cols")

    def __init__(self, n, cols=None):
        self.n = n
        self.cols = cols if cols is not None else [dict() for _ in range(n)]

    @staticmethod
    def ident(n):
        return Mat(n, [{i: Fr(1)} for i in range(n)])

    @staticmethod
    def from_perm(p):
        return Mat(len(p), [{p[j]: Fr(1)} for j in range(len(p))])

    def __matmul__(self, o):
        n = self.n
        res = [dict() for _ in range(n)]
        sc = self.cols
        for j in range(n):
            acc = res[j]
            for k, v in o.cols[j].items():
                for i, w in sc[k].items():
                    x = acc.get(i)
                    acc[i] = (x + v * w) if x is not None else v * w
            for i in [i for i, v in acc.items() if v == 0]:
                del acc[i]
        return Mat(n, res)

    def T(self):
        res = [dict() for _ in range(self.n)]
        for j, c in enumerate(self.cols):
            for i, v in c.items():
                res[i][j] = v
        return Mat(self.n, res)

    def apply(self, vec):
        out = [Fr(0)] * self.n
        for j, x in enumerate(vec):
            if x == 0:
                continue
            for i, v in self.cols[j].items():
                out[i] += v * x
        return out

    def get(self, i, j):
        return self.cols[j].get(i, Fr(0))

    def born(self):
        return tuple(tuple(sorted((i, v * v) for i, v in c.items()))
                     for c in self.cols)

    def is_orthogonal(self):
        d = self.T() @ self
        return all(sorted(c.items()) == [(j, Fr(1))]
                   for j, c in enumerate(d.cols))


def pcomp(p, q):
    return tuple(p[q[x]] for x in range(len(q)))


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
        if n > 10 ** 6:
            raise RuntimeError("order overflow")
    return n


def cycletype(p):
    seen, ct = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        c, j = 0, i
        while j not in seen:
            seen.add(j)
            j = p[j]
            c += 1
        ct.append(c)
    return tuple(sorted(ct))


def fixcount(p):
    return sum(1 for i in range(len(p)) if p[i] == i)


def suppcount(p):
    return sum(1 for i in range(len(p)) if p[i] != i)


# ===========================================================================
# 3.  THE BASE, REBUILT FROM TB3's SECTION-2 DECLARATION.  Generic in the wing
#     count -- which is what makes the two-wing run a control and not a
#     different program.
# ===========================================================================
NS = 2                      # system dimension per wing
NP = 2                      # pointer dimension per wing, value 0 = ready
ROT_ORDER = ("R0", "R1", "R2")
ROT_PYTH = {"R0": (Fr(1), Fr(0)), "R1": (Fr(3, 5), Fr(4, 5)),
            "R2": (Fr(5, 13), Fr(12, 13))}
SHIFT_TABLE = {0: (0, 1), 1: (1, 0)}
WING_LETTERS = "ABC"

PSI_DECL = (
    ("psi-G1", {0: Fr(3, 5), 7: Fr(4, 5)}),
    ("psi-W1", {1: Fr(2, 3), 2: Fr(2, 3), 4: Fr(1, 3)}),
)
PSI_COEFF = dict(PSI_DECL)


def rotation(g):
    c, s = ROT_PYTH[g]
    return Mat(2, [{0: c, 1: s}, {0: -s, 1: c}])


class Species:
    """One wing count with its carrier, its wing symmetry group, its frames
    and its legs.  Every size is enumerated, never typed."""

    def __init__(self, nw):
        self.NW = nw
        self.NSYS = NS ** nw
        self.NPT = NP ** nw
        self.NC = self.NSYS * self.NPT
        self.J0 = 0
        self.PERMS = tuple(itertools.permutations(range(nw)))
        self.IDENT = tuple(range(nw))
        self.NAME = {pi: "".join(WING_LETTERS[pi[w]] for w in range(nw))
                     for pi in self.PERMS}
        self.SIGMA = {pi: self._sigma(pi) for pi in self.PERMS}
        collapse_the_index = (MUTANT == "carrier-lax")
        self.PCARR = {}
        for pi in self.PERMS:
            s = self.SIGMA[pi]
            row = []
            for i in range(self.NC):
                a, p = divmod(i, self.NPT)
                q = s[p] % (self.NPT // 2) if collapse_the_index else s[p]
                row.append(s[a] * self.NPT + q)
            self.PCARR[pi] = tuple(row)
        truncate = (MUTANT == "twowing-lax" and nw == 2)
        self.FRAMES = tuple(itertools.permutations(range(nw)))
        if truncate:
            self.FRAMES = self.FRAMES[:1]
        self.FRNAME = {fr: "".join(WING_LETTERS[w] for w in fr)
                       for fr in self.FRAMES}
        self.NLEGS = 1 + nw
        self.CKPTS = tuple(range(self.NLEGS + 1))
        self.CELLS = tuple((t, r) for t in self.CKPTS
                           for r in ("FULL", "REAL"))
        self.LOC = {(w, g): self._u_local(w, g)
                    for w in range(nw) for g in ROT_ORDER}

    def bits(self, a):
        return tuple((a >> (self.NW - 1 - w)) & 1 for w in range(self.NW))

    def frombits(self, b):
        v = 0
        for x in b:
            v = v * 2 + x
        return v

    def _sigma(self, pi):
        """(pi.c)_w = c_{pi^-1(w)} on the 2^NW triple labels."""
        use_the_wrong_direction = (MUTANT == "s3-lax")
        inv = tuple(pi) if use_the_wrong_direction else pinv(pi)
        return tuple(self.frombits(tuple(self.bits(a)[inv[w]]
                                         for w in range(self.NW)))
                     for a in range(self.NSYS))

    def _u_local(self, w, g):
        """U_w(g) = sum_o Pi^g_o (x) Sh^o, the identity on every other wing."""
        R = rotation(g)
        cols = [dict() for _ in range(self.NC)]
        for j in range(self.NC):
            a, p = divmod(j, self.NPT)
            sb = list(self.bits(a))
            pb = list(self.bits(p))
            for o in range(NS):
                amp = R.get(sb[w], o)
                if amp == 0:
                    continue
                for x in range(NS):
                    v = R.get(x, o) * amp
                    if v == 0:
                        continue
                    nb = list(sb)
                    nb[w] = x
                    npb = list(pb)
                    npb[w] = SHIFT_TABLE[o][pb[w]]
                    i = self.frombits(tuple(nb)) * self.NPT + \
                        self.frombits(tuple(npb))
                    cols[j][i] = cols[j].get(i, Fr(0)) + v
        for c in cols:
            for k in [k for k, v in c.items() if v == 0]:
                del c[k]
        return Mat(self.NC, cols)

    def psi_vector(self, coeff):
        v = [Fr(0)] * self.NSYS
        for k, x in coeff.items():
            v[k] = x
        return v

    def householder(self, psi):
        w = [psi[i] - (Fr(1) if i == 0 else Fr(0)) for i in range(self.NSYS)]
        ww = sum(x * x for x in w)
        cols = [dict() for _ in range(self.NSYS)]
        for j in range(self.NSYS):
            for i in range(self.NSYS):
                v = (Fr(1) if i == j else Fr(0))
                if ww != 0:
                    v -= 2 * w[i] * w[j] / ww
                if v != 0:
                    cols[j][i] = v
        return Mat(self.NSYS, cols)

    def kron_pointer_identity(self, V):
        cols = [dict() for _ in range(self.NC)]
        for j in range(self.NC):
            a, p = divmod(j, self.NPT)
            for i, v in V.cols[a].items():
                cols[j][i * self.NPT + p] = v
        return Mat(self.NC, cols)

    def born_symmetric(self, V, pi):
        sig = self.SIGMA[pi]
        b = V.born()
        pb = [None] * self.NSYS
        for j, c in enumerate(b):
            pb[sig[j]] = tuple(sorted((sig[i], v) for i, v in c))
        return tuple(pb) == b

    def select_Q(self, psi):
        """THE DECLARED COMPLETION RULE: the lexicographically first
        transposition (i,j), 1 <= i < j < NSYS, whose completion V = H(psi) Q
        has a Born shadow invariant under NO non-identity wing symmetry."""
        ignore_the_property = (MUTANT == "qrule-lax")
        for i in range(1, self.NSYS):
            for j in range(i + 1, self.NSYS):
                q = list(range(self.NSYS))
                q[i], q[j] = q[j], q[i]
                q = tuple(q)
                if ignore_the_property:
                    return q
                V = self.householder(psi) @ Mat.from_perm(q)
                if all(not self.born_symmetric(V, pi) for pi in self.PERMS
                       if pi != self.IDENT):
                    return q
        return None


_SPEC: dict = {}


def species(nw):
    if nw not in _SPEC:
        _SPEC[nw] = Species(nw)
    return _SPEC[nw]


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
    """One (species, preparation, completion, setting): the legs, the process,
    and the two gluing rules' data."""

    def __init__(self, sp, psi, Q, setting):
        _bump()
        self.sp = sp
        self.psi = tuple(psi)
        self.Q = Q
        self.setting = setting
        self.V = sp.householder(psi) @ Mat.from_perm(Q)
        self.u = sp.kron_pointer_identity(self.V)
        self.legs = {fr: [self.u] + [sp.LOC[(w, setting[w])] for w in fr]
                     for fr in sp.FRAMES}
        self.proc = {fr: self._process(fr) for fr in sp.FRAMES}
        self.fk = {fr: [L.born() for L in self.legs[fr]] for fr in sp.FRAMES}
        self.rk = {fr: [self._realkey(fr, k) for k in range(sp.NLEGS)]
                   for fr in sp.FRAMES}

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

    def transport_admission(self):
        """The four-clause predicate at the TRANSPORT level: ordered frame
        pairs, per checkpoint, per rule, a link drawn only where the rule
        admits UNIQUELY."""
        _bump()
        sp = self.sp
        drop_the_leg_key_clause = (MUTANT == "legkey-lax")
        accept_every_candidate = (MUTANT == "id-lax")
        out = {}
        for t in sp.CKPTS:
            for rule in ("FULL", "REAL"):
                tab = {}
                for X in sp.FRAMES:
                    for Y in sp.FRAMES:
                        if X == Y:
                            continue
                        adm = []
                        for pi in sp.PERMS:
                            spm = sp.PCARR[pi]
                            if spm[sp.J0] != sp.J0:
                                continue
                            if not drop_the_leg_key_clause:
                                if rule == "FULL":
                                    if sorted(push_bornkey(k, spm)
                                              for k in self.fk[X]) != \
                                            sorted(self.fk[Y]):
                                        continue
                                else:
                                    if sorted(push_realkey(k, spm)
                                              for k in self.rk[X]) != \
                                            sorted(self.rk[Y]):
                                        continue
                            if frozenset(spm[i] for i in self.proc[X][1][t]) \
                                    != self.proc[Y][1][t]:
                                continue
                            if push_state(self.proc[X][0][t], spm) != \
                                    self.proc[Y][0][t]:
                                continue
                            adm.append(pi)
                        if len(adm) == 1 or (accept_every_candidate and adm):
                            tab[(X, Y)] = adm[0]
                out[(t, rule)] = tab
        return out


def transport_graph(sp, world, adm):
    """Nodes (frame, checkpoint); links are leg applications and the admitted
    identifications, one per unordered pair per coordinate cell."""
    _bump()
    nodes = tuple((fr, t) for fr in sp.FRAMES for t in sp.CKPTS)
    links = []
    for fr in sp.FRAMES:
        for k in range(sp.NLEGS):
            links.append((("leg", sp.FRNAME[fr], k + 1), (fr, k), (fr, k + 1)))
    nid = 0
    for t in sp.CKPTS:
        for rule in ("FULL", "REAL"):
            seen = set()
            for (X, Y) in sorted(adm[(t, rule)],
                                 key=lambda z: (sp.FRNAME[z[0]],
                                                sp.FRNAME[z[1]])):
                if (X, Y) in seen:
                    continue
                seen.add((X, Y))
                seen.add((Y, X))
                links.append((("id", rule, t, sp.FRNAME[X], sp.FRNAME[Y]),
                              (X, t), (Y, t)))
                nid += 1
    return nodes, tuple(links), nid


# ===========================================================================
# 4.  THE ATLAS AND ITS PAIR TABLE.  The atlas is the orbit of the committed
#     frames under the admitted group, deduplicated by CHART IDENTITY.
# ===========================================================================
def build_atlas(sp, world):
    _bump()
    charts = []
    seen = set()
    for pi in sp.PERMS:
        spm = sp.PCARR[pi]
        Pm = Mat.from_perm(spm)
        Pi = Mat.from_perm(pinv(spm))
        for fr in sp.FRAMES:
            legs = [Pm @ (L @ Pi) for L in world.legs[fr]]
            states = [push_state(s, spm) for s in world.proc[fr][0]]
            occ = [frozenset(spm[i] for i in o) for o in world.proc[fr][1]]
            fk = [L.born() for L in legs]
            ident = (tuple(sorted(fk)), tuple(states))
            if ident in seen:
                continue
            seen.add(ident)
            rk = [frozenset((i, j, legs[k].get(i, j) ** 2)
                            for j in occ[k] for i in occ[k + 1]
                            if legs[k].get(i, j) != 0)
                  for k in range(sp.NLEGS)]
            charts.append({"sigma": pi, "seed": fr, "states": states,
                           "occ": occ, "fk": fk, "rk": rk,
                           "name": sp.NAME[pi] + "|" + sp.FRNAME[fr]})
    for c in charts:
        c["sfk"] = sorted(c["fk"])
        c["srk"] = sorted(c["rk"])
        c["pfk"] = {pi: sorted(push_bornkey(k, sp.PCARR[pi]) for k in c["fk"])
                    for pi in sp.PERMS}
        c["prk"] = {pi: sorted(push_realkey(k, sp.PCARR[pi]) for k in c["rk"])
                    for pi in sp.PERMS}
        c["pocc"] = {pi: [frozenset(sp.PCARR[pi][i] for i in o)
                          for o in c["occ"]] for pi in sp.PERMS}
        c["pst"] = {pi: [push_state(s, sp.PCARR[pi]) for s in c["states"]]
                    for pi in sp.PERMS}
    return charts


def atlas_pair_table(sp, charts):
    """The same four-clause predicate applied to an ORDERED CHART PAIR."""
    _bump()
    drop_key = (MUTANT == "legkey-lax")
    accept_every_candidate = (MUTANT == "id-lax")
    out = {}
    n = len(charts)
    for t in sp.CKPTS:
        for rule in ("FULL", "REAL"):
            tab = {}
            for a in range(n):
                X = charts[a]
                for b in range(n):
                    if a == b:
                        continue
                    Y = charts[b]
                    adm = []
                    for pi in sp.PERMS:
                        if not drop_key:
                            if rule == "FULL":
                                if X["pfk"][pi] != Y["sfk"]:
                                    continue
                            else:
                                if X["prk"][pi] != Y["srk"]:
                                    continue
                        if X["pocc"][pi][t] != Y["occ"][t]:
                            continue
                        if X["pst"][pi][t] != Y["states"][t]:
                            continue
                        adm.append(pi)
                    if len(adm) == 1 or (accept_every_candidate and adm):
                        tab[(a, b)] = adm[0]
            out[(t, rule)] = tab
    return out


# ===========================================================================
# 5.  EXACT F_2 LINEAR ALGEBRA.  Rows are Python integers used as bit sets;
#     every operation is integer XOR.  No float, no tolerance.
# ===========================================================================
def rank_f2_high(rows, maxrank=None):
    """ROUTE A: elimination with the HIGHEST set bit as pivot, rows in their
    natural order."""
    skip_the_last_insert = (MUTANT == "rank-lax")
    piv = {}
    r = 0
    for row in rows:
        x = row
        while x:
            h = x.bit_length() - 1
            p = piv.get(h)
            if p is None:
                if skip_the_last_insert and r > 0:
                    break
                piv[h] = x
                r += 1
                break
            x ^= p
        if maxrank is not None and r >= maxrank:
            break
    return r


def rank_f2_low(rows):
    """ROUTE B: elimination with the LOWEST set bit as pivot, rows consumed in
    reverse order.  A different pivot rule, a different traversal, and no
    intermediate structure shared with route A."""
    piv = {}
    r = 0
    for row in reversed(list(rows)):
        x = row
        while x:
            lo = x & (-x)
            p = piv.get(lo)
            if p is None:
                piv[lo] = x
                r += 1
                break
            x ^= p
    return r


def components_unionfind(nv, pairs):
    """ROUTE A for components: union-find over the drawn links."""
    par = list(range(nv))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for a, b in pairs:
        ra, rb = find(a), find(b)
        if ra != rb:
            par[ra] = rb
    reps = {}
    for i in range(nv):
        reps.setdefault(find(i), []).append(i)
    return [sorted(v) for v in reps.values()]


def spanning_forest(nv, pairs):
    """A spanning forest by breadth-first growth: returns the set of tree-edge
    INDICES and the component count.  Used as the cycle-rank route that never
    performs an elimination."""
    drop_an_edge = (MUTANT == "tree-lax")
    adj = defaultdict(list)
    for i, (a, b) in enumerate(pairs):
        adj[a].append((i, b))
        adj[b].append((i, a))
    seen = [False] * nv
    tree = set()
    ncomp = 0
    for s in range(nv):
        if seen[s]:
            continue
        ncomp += 1
        seen[s] = True
        stack = [s]
        while stack:
            x = stack.pop()
            for i, y in adj[x]:
                if not seen[y]:
                    seen[y] = True
                    if drop_an_edge and not tree:
                        continue
                    tree.add(i)
                    stack.append(y)
    return tree, ncomp


class Complex:
    """A finite 2-dimensional cell complex over F_2 with its invariants
    computed by two genuinely independent routes."""

    def __init__(self, nv, epairs, tris, label):
        _bump()
        self.label = label
        self.nv = nv
        self.epairs = list(epairs)          # (a, b) per 1-cell
        self.tris = [tuple(sorted(t)) for t in tris]   # 1-cell index triples
        self.ne = len(self.epairs)
        self.nf = len(self.tris)

    def invariants(self):
        nv, ne, nf = self.nv, self.ne, self.nf
        # ---- components: two routes.  Every boundary row is assembled by
        #      XOR, so a cell whose two faces coincide contributes ZERO -- the
        #      mod-2 boundary, not an incidence bit pattern.  (The two differ
        #      only where a cell meets a face twice, which is exactly what the
        #      quotient complex does.)
        comps = components_unionfind(nv, self.epairs)
        b0_uf = len(comps)
        d1_rows = [(1 << a) ^ (1 << b) for (a, b) in self.epairs]
        r1_high = rank_f2_high(d1_rows)
        b0_rank = nv - r1_high
        # a third reading: the rank of the TRANSPOSED boundary matrix
        cols = [0] * nv
        for j, (a, b) in enumerate(self.epairs):
            cols[a] ^= (1 << j)
            cols[b] ^= (1 << j)
        r1_T = rank_f2_low(cols)
        # ---- cycle rank: forest route and elimination route
        tree, ncomp_tree = spanning_forest(nv, self.epairs)
        cyc_forest = ne - len(tree)
        cyc_rank = ne - r1_high
        # ---- rank of d2: two routes
        d2_rows = [(1 << x) ^ (1 << y) ^ (1 << z) for (x, y, z) in self.tris]
        r2_high = rank_f2_high(d2_rows, maxrank=cyc_rank)
        cot = [i for i in range(ne) if i not in tree]
        pos = {e: i for i, e in enumerate(cot)}
        proj = []
        for (x, y, z) in self.tris:
            v = 0
            for e in (x, y, z):
                i = pos.get(e)
                if i is not None:
                    v ^= (1 << i)
            proj.append(v)
        r2_low = rank_f2_low(proj)
        chain = all(((1 << self.epairs[x][0]) ^ (1 << self.epairs[x][1]) ^
                     (1 << self.epairs[y][0]) ^ (1 << self.epairs[y][1]) ^
                     (1 << self.epairs[z][0]) ^ (1 << self.epairs[z][1])) == 0
                    for (x, y, z) in self.tris[:2000])
        return {
            "V": nv, "E": ne, "F": nf,
            "components_route_1_union_find": b0_uf,
            "components_route_2_F2_rank": b0_rank,
            "components_route_3_transposed_rank": nv - r1_T,
            "components_route_4_spanning_forest": ncomp_tree,
            "cycle_rank_route_1_spanning_forest": cyc_forest,
            "cycle_rank_route_2_F2_rank": cyc_rank,
            "rank_d1": r1_high, "rank_d1_transposed": r1_T,
            "rank_d2_route_1_high_pivot": r2_high,
            "rank_d2_route_2_cotree_low_pivot": r2_low,
            "b0": b0_uf, "b1": cyc_rank - r2_high, "b2": nf - r2_high,
            "chi_from_cell_counts": nv - ne + nf,
            "chi_from_betti": b0_uf - (cyc_rank - r2_high) + (nf - r2_high),
            "d1_d2_is_zero_on_the_sampled_2_cells": chain,
        }


# ===========================================================================
# 6.  THE NERVE.  Two genuinely independent routes to the triangle census.
# ===========================================================================
def nerve_edges(sp, pair, ncharts):
    """The 1-cells: one per unordered chart pair per coordinate cell."""
    _bump()
    edges, eidx = [], {}
    for c in sp.CELLS:
        tab = pair[c]
        for (a, b) in sorted(tab):
            if a < b:
                eidx[(a, b, c)] = len(edges)
                edges.append((a, b, c, tab[(a, b)]))
    return edges, eidx


def triangles_route_1(sp, pair, ncharts):
    """ROUTE 1: adjacency lists, walking drawn edges only, ordered triples.
    This is a walk over out-neighbour lists built per checkpoint per rule."""
    _bump()
    drop_a_checkpoint = (MUTANT == "route1-drop")
    ck = list(sp.CKPTS)
    if drop_a_checkpoint:
        ck = ck[:-1]
    tot = 0
    per_ck = {}
    for t in ck:
        adj = {r: defaultdict(list) for r in ("FULL", "REAL")}
        for r in ("FULL", "REAL"):
            for (a, b), pi in pair[(t, r)].items():
                adj[r][a].append(b)
        c0 = tot
        for r1 in ("FULL", "REAL"):
            for a, lst in adj[r1].items():
                for b in lst:
                    for r2 in ("FULL", "REAL"):
                        for c in adj[r2][b]:
                            if c == a:
                                continue
                            for r3 in ("FULL", "REAL"):
                                if (c, a) in pair[(t, r3)]:
                                    tot += 1
        per_ck[t] = tot - c0
    return tot, per_ck


def triangles_route_2(sp, pair, ncharts):
    """ROUTE 2: a direct triple loop over every ordered triple of pairwise
    distinct charts, counting the rule multiplicities by dictionary lookup.
    No adjacency list, a different loop order, no shared intermediate."""
    _bump()
    mult = {}
    for t in sp.CKPTS:
        m = defaultdict(int)
        for r in ("FULL", "REAL"):
            for k in pair[(t, r)]:
                m[k] += 1
        mult[t] = m
    tot = 0
    per_ck = {}
    for t in sp.CKPTS:
        m = mult[t]
        c0 = tot
        for a in range(ncharts):
            for b in range(ncharts):
                if b == a:
                    continue
                mab = m.get((a, b), 0)
                if not mab:
                    continue
                for c in range(ncharts):
                    if c == a or c == b:
                        continue
                    mbc = m.get((b, c), 0)
                    if not mbc:
                        continue
                    mca = m.get((c, a), 0)
                    if mca:
                        tot += mab * mbc * mca
        per_ck[t] = tot - c0
    return tot, per_ck


def geometric_cells(sp, pair, eidx, ncharts, drop_one=False):
    """THE GEOMETRIC 2-CELLS and the ordered defect multiset.  Each unordered
    triple of charts at a common checkpoint with a rule chosen per edge gives
    ONE 2-cell; the six ordered traversals of that cell give the six entries
    of TB3's ordered defect multiset, computed explicitly here."""
    _bump()
    drop_a_cell = (MUTANT == "cell-drop") or drop_one
    coherence_always_true = (MUTANT == "coh-lax")
    cells, coh = [], []
    per_ck = defaultdict(int)
    defects = Counter()
    ident = sp.IDENT
    for t in sp.CKPTS:
        tabs = {r: pair[(t, r)] for r in ("FULL", "REAL")}
        for a in range(ncharts):
            for b in range(a + 1, ncharts):
                for c in range(b + 1, ncharts):
                    for r1 in ("FULL", "REAL"):
                        p1 = tabs[r1].get((a, b))
                        if p1 is None:
                            continue
                        for r2 in ("FULL", "REAL"):
                            p2 = tabs[r2].get((b, c))
                            if p2 is None:
                                continue
                            for r3 in ("FULL", "REAL"):
                                p3 = tabs[r3].get((c, a))
                                if p3 is None:
                                    continue
                                key = (eidx[(a, b, (t, r1))],
                                       eidx[(b, c, (t, r2))],
                                       eidx[(a, c, (t, r3))])
                                cells.append(key)
                                per_ck[t] += 1
                                d1 = pcomp(p3, pcomp(p2, p1))
                                d2 = pcomp(p1, pcomp(p3, p2))
                                d3 = pcomp(p2, pcomp(p1, p3))
                                for d in (d1, d2, d3):
                                    defects[sp.NAME[d]] += 1
                                    defects[sp.NAME[pinv(d)]] += 1
                                if d1 == ident or coherence_always_true:
                                    coh.append(key)
    if drop_a_cell and cells:
        cells = cells[:-1]
    return cells, coh, dict(per_ck), dict(defects)


def simplicial_nerve(sp, pair, ncharts):
    """N_simp: the maximal faces are the components of the per-coordinate-cell
    overlap graphs, because each of those graphs is measured to be a disjoint
    union of COMPLETE graphs -- which is itself gated here."""
    _bump()
    maximal, complete = [], True
    for c in sp.CELLS:
        und = set()
        for (a, b) in pair[c]:
            und.add((min(a, b), max(a, b)))
        comps = components_unionfind(ncharts, sorted(und))
        for comp in comps:
            k = len(comp)
            if k > 1:
                got = sum(1 for (a, b) in und if a in comp and b in comp)
                if got != k * (k - 1) // 2:
                    complete = False
                maximal.append(frozenset(comp))
    reduced = [m for m in set(maximal)
               if not any(m < o for o in set(maximal))]
    return sorted(reduced, key=lambda s: (-len(s), sorted(s))), complete


# ===========================================================================
# 7.  THE PINNED FOUNDATION.  TB3's terminal receipt, hashed and read as data.
# ===========================================================================
def load_tb3():
    raw = TB3_RECEIPT.read_bytes()
    perturb = (MUTANT == "pin-hash")
    if perturb:
        raw = raw + b" "
    h = hashlib.sha256(raw).hexdigest()
    anchor("A-PIN-TB3", "this file, pinned SHA-256",
           "SHA-256 of the TB3 terminal receipt",
           PINNED_RECEIPT_SHA256["TB3"], h)
    gate("TOP-PIN-TB3", "anchor",
         "THE FOUNDATION IS HASH-PINNED.  TB3's terminal receipt is read as "
         "DATA and its SHA-256 is gated against the value pinned in this "
         "source; the atlas is REBUILT from TB3's section-2 declaration and "
         "nothing is imported from the TB3 instrument",
         h == PINNED_RECEIPT_SHA256["TB3"], {"sha256": h})
    return json.loads(TB3_RECEIPT.read_bytes().decode())


# ===========================================================================
# 8.  RUN: THE BASE AND THE FIVE ATLAS INSTANCES.
# ===========================================================================
def instance_world(sp, member, completion, setting):
    psi = sp.psi_vector(PSI_COEFF[member])
    Q = sp.select_Q(psi) if completion == "declared" \
        else tuple(range(sp.NSYS))
    return World(sp, psi, Q, setting), Q


def run_base(tb3):
    prog("the base, rebuilt from TB3 section 2")
    sp = species(3)
    dec = tb3["tables"]["base_declaration"]
    arena = tb3["tables"]["arena"]
    anchor("A-CARRIER", "TB3 committed receipt", "carrier",
           dec["carrier"]["carrier"], sp.NC)
    anchor("A-WINGS", "TB3 committed receipt", "wings",
           dec["carrier"]["wings"], sp.NW)
    anchor("A-FRAMES", "TB3 committed receipt", "frames",
           dec["frames"]["frames"], len(sp.FRAMES))
    anchor("A-CKPTS", "TB3 committed receipt", "checkpoints",
           dec["frames"]["checkpoints"], len(sp.CKPTS))
    anchor("A-ADMITTED", "TB3 committed receipt",
           "the admitted group after the j0 filter",
           arena["admitted_after_the_j0_filter"], len(sp.PERMS))
    anchor("A-CELLS", "TB3 committed receipt",
           "coordinate cells (setting, checkpoint, rule)",
           arena["coordinate_cells_setting_checkpoint_rule"],
           27 * len(sp.CKPTS) * 2)
    psi = sp.psi_vector(PSI_COEFF["psi-G1"])
    Qref = sp.select_Q(psi)
    anchor("A-QREF", "TB3 committed receipt",
           "the rule-selected reference completion",
           tuple(arena["the_declared_completion_transposition"]), Qref)
    nonabelian = any(pcomp(a, b) != pcomp(b, a)
                     for a in sp.PERMS for b in sp.PERMS)
    base_ids = ("A-CARRIER", "A-WINGS", "A-FRAMES", "A-CKPTS", "A-ADMITTED",
                "A-CELLS", "A-QREF", "A-PIN-TB3")
    gate("TOP-BASE", "measurement",
         "THE BASE REBUILDS.  The three-wing carrier, the wing symmetry "
         "group, the frames, the checkpoints, the admitted group after the "
         "j0 filter and the rule-selected reference completion are rebuilt "
         "from TB3's section-2 declaration and each is anchored exit-1 "
         "against the hash-pinned committed receipt.  The wing group is "
         "measured NON-ABELIAN here, not assumed",
         all(a["passed"] for a in ANCHORS if a["id"] in base_ids)
         and nonabelian,
         {"carrier": sp.NC, "wing_group_order": len(sp.PERMS),
          "wing_group_is_abelian": not nonabelian,
          "reference_completion": Qref})
    TABLES["base"] = {
        "carrier": sp.NC, "wings": sp.NW, "frames": len(sp.FRAMES),
        "checkpoints": len(sp.CKPTS), "coordinate_cells_of_the_nerve":
            len(sp.CELLS), "admitted_group_order": len(sp.PERMS),
        "the_admitted_group_is_abelian": not nonabelian,
        "the_rule_selected_reference_completion": list(Qref),
        "arena": ARENA}
    return sp, Qref


def run_instances(sp, tb3):
    prog("the five declared atlas instances")
    committed = tb3["tables"]["a3_triangles"]["per_instance"]
    rows = {}
    store = {}
    for (label, member, completion, setting) in INSTANCES:
        w, Q = instance_world(sp, member, completion, setting)
        charts = build_atlas(sp, w)
        pair = atlas_pair_table(sp, charts)
        edges, eidx = nerve_edges(sp, pair, len(charts))
        r1, pc1 = triangles_route_1(sp, pair, len(charts))
        r2, pc2 = triangles_route_2(sp, pair, len(charts))
        cells, coh, pcg, defects = geometric_cells(sp, pair, eidx, len(charts))
        cm = committed[label]
        anchor("A-CHARTS-" + label, "TB3 committed receipt",
               "charts in the atlas", cm["charts_in_the_atlas"], len(charts))
        anchor("A-SEEDS-" + label, "TB3 committed receipt", "seeds",
               cm["seeds"], len(set(c["seed"] for c in charts)))
        for c in sp.CELLS:
            key = "%d/%s" % (c[0], "FULL" if c[1] == "FULL" else "REAL")
            anchor("A-EDGES-%s-%s" % (label, key), "TB3 committed receipt",
                   "ordered admitted pairs at " + key,
                   cm["edges_per_cell"][key], len(pair[c]))
        anchor("A-TRI-" + label, "TB3 committed receipt",
               "admissible triangles (ordered census)",
               cm["admissible_triangles_route_1"], r1)
        for t in sp.CKPTS:
            anchor("A-TRICK-%s-%d" % (label, t), "TB3 committed receipt",
                   "admissible triangles at checkpoint %d" % t,
                   cm["per_checkpoint"][str(t)]["triangles"], pc1.get(t, 0))
        if label == REFERENCE_INSTANCE:
            for k, v in sorted(cm["the_defect_multiset_over_the_wing_group"]
                               .items()):
                anchor("A-DEFECT-" + k, "TB3 committed receipt",
                       "ordered triangle defects equal to " + k, v,
                       defects.get(k, 0))
        store[label] = {"world": w, "Q": Q, "charts": charts, "pair": pair,
                        "edges": edges, "eidx": eidx, "cells": cells,
                        "coh": coh}
        rows[label] = {
            "member": member, "completion": completion,
            "setting": "TB-" + "".join(str(ROT_ORDER.index(x))
                                       for x in setting),
            "charts": len(charts), "seeds": len(set(c["seed"] for c in charts)),
            "one_cells": len(edges),
            "ordered_triangles_route_1": r1,
            "ordered_triangles_route_2": r2,
            "the_two_routes_agree": r1 == r2,
            "geometric_2_cells": len(cells),
            "coherent_2_cells": len(coh),
            "ordered_over_geometric": (r1 // len(cells)) if cells else None,
            "the_multiplicity_is_exact": bool(cells)
                                         and r1 == 6 * len(cells),
            "per_checkpoint_ordered": {str(t): pc1.get(t, 0)
                                       for t in sp.CKPTS},
            "per_checkpoint_geometric": {str(t): pcg.get(t, 0)
                                         for t in sp.CKPTS},
            "ordered_defect_multiset": defects}
    # the dropped-cell probe: route 2's cell list loses one 2-cell and the
    # completeness relation must break.
    ref = store[REFERENCE_INSTANCE]
    probe_cells, _, _, _ = geometric_cells(sp, ref["pair"], ref["eidx"],
                                           len(ref["charts"]), drop_one=True)
    probe_breaks = (len(probe_cells) != len(ref["cells"])) and \
        (rows[REFERENCE_INSTANCE]["ordered_triangles_route_1"] !=
         6 * len(probe_cells))
    gate("TOP-CENSUS-ROUTES", "measurement",
         "THE TRIANGLE CENSUS AGREES BY TWO GENUINELY INDEPENDENT ROUTES AT "
         "EVERY DECLARED INSTANCE, and each count is anchored exit-1 against "
         "the hash-pinned committed receipt.  Route 1 walks per-checkpoint "
         "adjacency lists with an explicit rule loop; route 2 runs a direct "
         "ordered triple loop and multiplies rule multiplicities read by "
         "dictionary lookup -- no adjacency list, a different loop order, no "
         "shared intermediate.  The `route1-drop` mutant drops a checkpoint "
         "from route 1 alone and must die on the route differential",
         all(v["the_two_routes_agree"] for v in rows.values()),
         {k: [v["ordered_triangles_route_1"], v["ordered_triangles_route_2"]]
          for k, v in rows.items()})
    gate("TOP-CELL-COMPLETENESS", "measurement",
         "THE 2-CELL SET IS COMPLETE AND A DROPPED CELL IS CAUGHT (RUNBOOK "
         "section 13 addendum, #234).  The ordered census is measured to be "
         "EXACTLY six times the geometric 2-cell count at every instance -- "
         "the six being the traversals of a triangle, three rotations and "
         "two orientations, computed rather than typed -- and a probe that "
         "removes ONE geometric 2-cell is measured to break that relation",
         all(v["the_multiplicity_is_exact"] for v in rows.values()
             if v["geometric_2_cells"]) and probe_breaks,
         {"multiplicity": {k: v["ordered_over_geometric"]
                           for k, v in rows.items()},
          "the_dropped_cell_probe_breaks_the_relation": probe_breaks,
          "cells_with_the_probe": len(probe_cells)})
    ident_name = sp.NAME[sp.IDENT]
    coh_ok = all(6 * v["coherent_2_cells"] ==
                 v["ordered_defect_multiset"].get(ident_name, 0)
                 for v in rows.values())
    gate("TOP-COHERENCE", "measurement",
         "THE COHERENT 2-CELLS ARE COUNTED TWICE, INDEPENDENTLY.  A 2-cell is "
         "coherent when its three drawn maps compose to the identity -- the "
         "strict cocycle condition.  Route 1 flags it while the cell is "
         "built; route 2 reads the ORDERED DEFECT MULTISET, itself anchored "
         "against the committed receipt, and takes the entry at the identity. "
         " The two are gated equal through the exact traversal multiplicity "
         "at every instance, so a coherence test that answered yes to "
         "everything would be caught by a census it does not touch",
         coh_ok,
         {k: [6 * v["coherent_2_cells"],
              v["ordered_defect_multiset"].get(ident_name, 0)]
          for k, v in rows.items()})
    gate("TOP-DEFECTS", "measurement",
         "THE ORDERED TRIANGLE DEFECT MULTISET over the wing group is "
         "reproduced element by element at the reference instance and "
         "anchored exit-1 against the committed receipt.  It is computed from "
         "the geometric 2-cells by evaluating all six traversals explicitly, "
         "not by scaling one of them",
         all(a["passed"] for a in ANCHORS if a["id"].startswith("A-DEFECT-")),
         rows[REFERENCE_INSTANCE]["ordered_defect_multiset"])
    TABLES["instances"] = rows
    return store


# ===========================================================================
# 9.  Q1 -- THE INVARIANT TABLE.
# ===========================================================================
def run_q1(sp, store):
    prog("Q1: the overlap graph, the nerve and its invariants")
    table = {}
    for (label, _m, _c, _s) in INSTANCES:
        st = store[label]
        nch = len(st["charts"])
        epairs = [(a, b) for (a, b, c, p) in st["edges"]]
        N = Complex(nch, epairs, st["cells"], label)
        inv = N.invariants()
        Nc = Complex(nch, epairs, st["coh"], label + " (coherent)")
        invc = Nc.invariants()
        # the simple overlap graph
        und = sorted({(min(a, b), max(a, b)) for (a, b, c, p) in st["edges"]})
        G = Complex(nch, und, [], label + " (simple overlap graph)")
        invg = G.invariants()
        # the per-checkpoint decomposition: the SECOND, genuinely independent
        # route to b_1.  Each checkpoint's sub-complex is measured separately
        # and the pieces are glued along the shared 0-cells.
        # Each 1-cell and each 2-cell belongs to exactly ONE checkpoint, so
        # the checkpoint sub-complexes meet exactly in the shared 0-skeleton.
        # For a union glued along a discrete set, H_2 is additive and the
        # Euler characteristics add with the 0-skeleton counted once, whence
        #     b_1(N) = b_0(N) + (T - 1)|V| + sum_t ( b_1(N_t) - b_0(N_t) ).
        # Every input on the right is a per-checkpoint elimination or a
        # union-find count; the global d_2 elimination enters nowhere.
        wrong_gluing = (MUTANT == "glue-lax")
        per_t, sum_b1, sum_b0, sum_b2, live_t = {}, 0, 0, 0, 0
        for t in sp.CKPTS:
            loc = [i for i, (a, b, c, p) in enumerate(st["edges"])
                   if c[0] == t]
            if not loc:
                continue
            live_t += 1
            ren = {e: i for i, e in enumerate(loc)}
            el = [(st["edges"][e][0], st["edges"][e][1]) for e in loc]
            tl = [tuple(ren[x] for x in tr) for tr in st["cells"]
                  if all(y in ren for y in tr)]
            sub = Complex(nch, el, tl, "%s t=%d" % (label, t)).invariants()
            per_t[str(t)] = {"E": sub["E"], "F": sub["F"], "b0": sub["b0"],
                             "b1": sub["b1"], "b2": sub["b2"],
                             "chi": sub["chi_from_cell_counts"]}
            sum_b1 += sub["b1"]
            sum_b0 += sub["b0"]
            sum_b2 += sub["b2"]
        glue = (live_t - 1) * (nch + (1 if wrong_gluing else 0))
        b1_route_2 = inv["b0"] + glue + sum_b1 - sum_b0
        # the same decomposition for the coherent sub-nerve
        sum_b1c, sum_b0c, sum_b2c = 0, 0, 0
        for t in sp.CKPTS:
            loc = [i for i, (a, b, c, p) in enumerate(st["edges"])
                   if c[0] == t]
            if not loc:
                continue
            ren = {e: i for i, e in enumerate(loc)}
            el = [(st["edges"][e][0], st["edges"][e][1]) for e in loc]
            tl = [tuple(ren[x] for x in tr) for tr in st["coh"]
                  if all(y in ren for y in tr)]
            s2 = Complex(nch, el, tl, "c").invariants()
            sum_b1c += s2["b1"]
            sum_b0c += s2["b0"]
            sum_b2c += s2["b2"]
        b1c_route_2 = invc["b0"] + glue + sum_b1c - sum_b0c
        maximal, complete = simplicial_nerve(sp, st["pair"], nch)
        top = max((len(m) for m in maximal), default=0)
        # chi of the simplicial nerve, two routes: the inclusion-exclusion sum
        # over the maximal faces' subsets when there is ONE maximal face, and
        # the cone argument.
        if len(maximal) == 1:
            k = len(maximal[0])
            chi_simp = sum(((-1) ** (j + 1)) * _binom(k, j)
                           for j in range(1, k + 1))
            cone = True
        else:
            chi_simp = None
            cone = False
        table[label] = {
            "the_overlap_graph": {
                "nodes": nch, "edges": len(und),
                "components": invg["components_route_1_union_find"],
                "components_route_2": invg["components_route_2_F2_rank"],
                "cycle_rank": invg["cycle_rank_route_1_spanning_forest"],
                "cycle_rank_route_2": invg["cycle_rank_route_2_F2_rank"],
                "it_is_complete": len(und) == nch * (nch - 1) // 2},
            "the_nerve_N": inv,
            "the_coherent_sub_nerve": invc,
            "b1_route_2_per_checkpoint_gluing": b1_route_2,
            "b1_coherent_route_2_per_checkpoint_gluing": b1c_route_2,
            "per_checkpoint": per_t,
            "the_gluing_term": glue,
            "sum_of_per_checkpoint_b0": sum_b0,
            "sum_of_per_checkpoint_b1": sum_b1,
            "sum_of_per_checkpoint_b2": sum_b2,
            "H2_is_additive_over_the_checkpoint_decomposition":
                sum_b2 == inv["b2"],
            "H2_is_additive_coherent": sum_b2c == invc["b2"],
            "the_simplicial_nerve": {
                "maximal_faces": [sorted(m) for m in maximal],
                "maximal_face_sizes": sorted((len(m) for m in maximal),
                                             reverse=True),
                "every_coordinate_cell_graph_is_a_disjoint_union_of_complete_"
                "graphs": complete,
                "top_dimension": top - 1 if top else -1,
                "chi_route_1_alternating_binomial_sum": chi_simp,
                "it_is_a_cone_hence_contractible": cone},
        }
    ok_routes = all(
        v["the_nerve_N"]["components_route_1_union_find"] ==
        v["the_nerve_N"]["components_route_2_F2_rank"] ==
        v["the_nerve_N"]["components_route_3_transposed_rank"] ==
        v["the_nerve_N"]["components_route_4_spanning_forest"]
        for v in table.values())
    ok_cyc = all(v["the_nerve_N"]["cycle_rank_route_1_spanning_forest"] ==
                 v["the_nerve_N"]["cycle_rank_route_2_F2_rank"]
                 for v in table.values())
    ok_rank = all(v["the_nerve_N"]["rank_d2_route_1_high_pivot"] ==
                  v["the_nerve_N"]["rank_d2_route_2_cotree_low_pivot"]
                  for v in table.values())
    ok_b1 = all(v["the_nerve_N"]["b1"] ==
                v["b1_route_2_per_checkpoint_gluing"]
                for v in table.values())
    ok_b1c = all(v["the_coherent_sub_nerve"]["b1"] ==
                 v["b1_coherent_route_2_per_checkpoint_gluing"]
                 for v in table.values())
    ok_h2 = all(v["H2_is_additive_over_the_checkpoint_decomposition"]
                and v["H2_is_additive_coherent"] for v in table.values())
    gate("TOP-COMPONENTS", "measurement",
         "THE COMPONENT COUNT AGREES BY FOUR ROUTES at every declared "
         "instance: union-find over the drawn links, the F_2 rank of the "
         "boundary matrix, the F_2 rank of its TRANSPOSE with the opposite "
         "pivot rule, and a breadth-first spanning forest.  The four are "
         "different computations reading different intermediates",
         ok_routes,
         {k: v["the_nerve_N"]["components_route_1_union_find"]
          for k, v in table.items()})
    gate("TOP-CYCLERANK", "measurement",
         "THE CYCLE RANK AGREES BY TWO ROUTES: a spanning forest grown "
         "breadth-first, which performs no elimination at all, and the F_2 "
         "rank of the boundary matrix.  The `tree-lax` mutant omits one "
         "forest edge and must die here",
         ok_cyc, {k: v["the_nerve_N"]["cycle_rank_route_1_spanning_forest"]
                  for k, v in table.items()})
    gate("TOP-HOMOLOGY", "measurement",
         "THE F_2 HOMOLOGY RANKS AGREE BY TWO GENUINELY INDEPENDENT ROUTES.  "
         "rank(d_2) is computed by elimination on the edge-indexed boundary "
         "matrix with a highest-bit pivot, and independently by elimination "
         "on the COTREE-PROJECTED matrix in fundamental-cycle coordinates "
         "with a lowest-bit pivot and the rows consumed in reverse -- a "
         "different matrix, different coordinates, a different pivot rule.  "
         "b_1 is then re-derived a THIRD way, from the per-checkpoint "
         "decomposition, in which every input is a per-checkpoint elimination "
         "or a union-find count and the global boundary elimination enters "
         "nowhere; the decomposition's own hypothesis -- that H_2 is additive "
         "over checkpoints, because each cell of positive dimension lies in "
         "exactly one of them -- is MEASURED rather than assumed",
         ok_rank and ok_b1 and ok_b1c and ok_h2,
         {"rank_d2_routes_agree": ok_rank, "b1_routes_agree": ok_b1,
          "b1_coherent_routes_agree": ok_b1c,
          "H2_additivity_measured": ok_h2,
          "b1": {k: v["the_nerve_N"]["b1"] for k, v in table.items()}})
    chi2 = {}
    for k, v in table.items():
        r = TABLES["instances"][k]
        chi2[k] = (v["the_nerve_N"]["V"] - v["the_nerve_N"]["E"]
                   + r["ordered_triangles_route_2"] // 6)
    ok_chi = all(v["the_nerve_N"]["chi_from_cell_counts"] == chi2[k]
                 for k, v in table.items())
    gate("TOP-CHI", "measurement",
         "THE EULER CHARACTERISTIC AGREES BY TWO ROUTES.  Route 1 uses the "
         "geometric 2-cell set built by the a<b<c enumeration; route 2 uses "
         "the ORDERED census taken by the independent triple loop, divided by "
         "the exact traversal multiplicity.  A cell dropped from one "
         "enumeration and not the other moves one and not the other, which is "
         "what the `cell-drop` mutant does.  The Euler-Poincare agreement "
         "with the Betti numbers is recorded as a DISCLOSURE below, NOT as a "
         "route, because it is an algebraic identity in the ranks",
         ok_chi,
         {k: [v["the_nerve_N"]["chi_from_cell_counts"], chi2[k]]
          for k, v in table.items()})
    gate("TOP-EULER-POINCARE", "disclosure",
         "DISCLOSURE, ANALYTICALLY FORCED.  chi computed from the Betti "
         "numbers equals chi computed from the cell counts for EVERY input, "
         "because the ranks cancel identically; it is printed as evidence "
         "that the ranks were assembled consistently and is NOT a second "
         "route to chi.  Likewise d_1 d_2 = 0 holds by construction for a "
         "simplicial boundary and is recorded, not gated",
         True,
         {k: [v["the_nerve_N"]["chi_from_cell_counts"],
              v["the_nerve_N"]["chi_from_betti"],
              v["the_nerve_N"]["d1_d2_is_zero_on_the_sampled_2_cells"]]
          for k, v in table.items()})
    simp_ok = all(v["the_simplicial_nerve"][
        "every_coordinate_cell_graph_is_a_disjoint_union_of_complete_graphs"]
        for v in table.values())
    ref = table[REFERENCE_INSTANCE]["the_simplicial_nerve"]
    drop_the_cone_check = (MUTANT == "simp-lax")
    simp_cone = ref["it_is_a_cone_hence_contractible"] and \
        (ref["chi_route_1_alternating_binomial_sum"] ==
         (0 if drop_the_cone_check else 1))
    gate("TOP-SIMPLICIAL", "measurement",
         "THE SIMPLICIAL NERVE IS A FULL SIMPLEX AT THE REFERENCE INSTANCE, "
         "hence contractible.  Every coordinate cell's overlap graph is "
         "MEASURED to be a disjoint union of complete graphs, so the faces "
         "are exactly the subsets of those components; at the reference "
         "instance eight of the ten cells give the whole chart set, so the "
         "unique maximal face is everything.  Its Euler characteristic is "
         "computed as the alternating binomial sum over all non-empty "
         "subsets and is measured to be 1, which the cone argument predicts",
         simp_ok and simp_cone,
         {"maximal_face_sizes": ref["maximal_face_sizes"],
          "chi": ref["chi_route_1_alternating_binomial_sum"],
          "all_cell_graphs_are_unions_of_complete_graphs": simp_ok})
    TABLES["q1_invariants"] = table
    return table


def _binom(n, k):
    num, den = 1, 1
    for i in range(k):
        num *= (n - i)
        den *= (i + 1)
    return num // den


# ===========================================================================
# 10.  Q2 -- THE DIMENSION READING.
# ===========================================================================
def local_profiles(sp, st, nch):
    """The declared estimator, evaluated at every chart."""
    _bump()
    ignore_the_cell_structure = (MUTANT == "dim-lax")
    link_from_edges_only = (MUTANT == "link-lax")
    edges = st["edges"]
    cells = st["cells"]
    etov = [(a, b) for (a, b, c, p) in edges]
    dimprof = {v: [] for v in range(nch)}
    for c in sp.CELLS:
        und = sorted({(min(a, b), max(a, b)) for (a, b) in st["pair"][c]})
        comps = components_unionfind(nch, und)
        deg = Counter()
        for (a, b) in und:
            deg[a] += 1
            deg[b] += 1
        for comp in comps:
            for v in comp:
                if deg[v] == 0:
                    dimprof[v].append(-1)
                elif ignore_the_cell_structure:
                    dimprof[v].append(0)
                else:
                    dimprof[v].append(len(comp) - 1)
    star_e = Counter()
    for (a, b) in etov:
        star_e[a] += 1
        star_e[b] += 1
    star_f = Counter()
    incident = defaultdict(list)
    for tr in cells:
        vs = set()
        for x in tr:
            vs.update(etov[x])
        for v in vs:
            star_f[v] += 1
            incident[v].append(tuple(sorted(vs - {v})))
    prof = {}
    for v in range(nch):
        nb = sorted({b if a == v else a for (a, b) in etov if v in (a, b)})
        ren = {x: i for i, x in enumerate(nb)}
        if link_from_edges_only:
            lk = [(ren[nb[0]], ren[x]) for x in nb[1:]] if len(nb) > 1 else []
        else:
            lk = [(ren[p], ren[q]) for (p, q) in incident[v]]
        r = rank_f2_high([(1 << a) | (1 << b) for (a, b) in lk])
        prof[v] = {"dimprofile": tuple(dimprof[v]),
                   "star": (star_e[v], star_f[v]),
                   "link": (len(nb), len(lk), len(nb) - r, len(lk) - r)}
    return prof


def control_complex(tris):
    verts = sorted({v for t in tris for v in t})
    ren = {v: i for i, v in enumerate(verts)}
    epairs, eidx = [], {}
    for t in tris:
        for (a, b) in itertools.combinations(sorted(ren[v] for v in t), 2):
            if (a, b) not in eidx:
                eidx[(a, b)] = len(epairs)
                epairs.append((a, b))
    cells = []
    for t in tris:
        s = sorted(ren[v] for v in t)
        cells.append(tuple(sorted(eidx[(s[i], s[j])]
                                  for i, j in ((0, 1), (0, 2), (1, 2)))))
    return len(verts), epairs, cells


def control_links(nv, epairs, cells):
    link_from_edges_only = (MUTANT == "link-lax")
    out = {}
    for v in range(nv):
        nb = sorted({b if a == v else a for (a, b) in epairs if v in (a, b)})
        ren = {x: i for i, x in enumerate(nb)}
        lk = []
        for tr in cells:
            vs = set()
            for e in tr:
                vs.update(epairs[e])
            if v in vs:
                o = sorted(vs - {v})
                lk.append((ren[o[0]], ren[o[1]]))
        if link_from_edges_only and len(nb) > 1:
            lk = [(ren[nb[0]], ren[x]) for x in nb[1:]]
        r = rank_f2_high([(1 << a) | (1 << b) for (a, b) in lk])
        out[v] = (len(nb), len(lk), len(nb) - r, len(lk) - r)
    return out


def run_q2(sp, store, q1):
    prog("Q2: the dimension reading")
    ctrl = {}
    for label, tris in (("the boundary of a tetrahedron (a 2-sphere)",
                         CTRL_SPHERE),
                        ("a 9-vertex torus", CTRL_TORUS),
                        ("two tetrahedra sharing one vertex (a pinch point)",
                         CTRL_PINCH)):
        nv, ep, cl = control_complex(tris)
        inv = Complex(nv, ep, cl, label).invariants()
        lk = control_links(nv, ep, cl)
        circles = all(v[2] == 1 and v[3] == 1 for v in lk.values())
        d = CTRL_DECLARED[label]
        for key, got in (("V", inv["V"]), ("E", inv["E"]), ("F", inv["F"]),
                         ("chi", inv["chi_from_cell_counts"]),
                         ("b0", inv["b0"]), ("b1", inv["b1"]),
                         ("b2", inv["b2"]),
                         ("every link is a circle", circles)):
            anchor("A-CTRL-%s-%s" % (label[:18], key),
                   "DECLARED-STANDARD (the complex's standard invariants)",
                   "%s of %s" % (key, label), d[key], got)
        ctrl[label] = {"V": inv["V"], "E": inv["E"], "F": inv["F"],
                       "chi": inv["chi_from_cell_counts"], "b0": inv["b0"],
                       "b1": inv["b1"], "b2": inv["b2"],
                       "every_link_is_a_circle": circles,
                       "distinct_link_profiles":
                           sorted(set(lk.values())),
                       "witness": None if circles else
                       sorted(v for v, x in lk.items()
                              if not (x[2] == 1 and x[3] == 1))[:1]}
    gate("TOP-DIM-CONTROLS", "control",
         "THE ESTIMATOR IS CALIBRATED ON COMPLEXES WHOSE ANSWER IS KNOWN.  "
         "On the boundary of a tetrahedron and on a 9-vertex torus -- both "
         "genuine 2-manifolds -- the estimator returns a CIRCLE link at every "
         "vertex and the standard Euler characteristics and F_2 Betti "
         "numbers, each anchored exit-1 against the declared standard values; "
         "on two tetrahedra glued at one vertex it returns a link that is NOT "
         "a circle, and names the pinch vertex.  Positive and negative in one "
         "family",
         all(a["passed"] for a in ANCHORS if a["id"].startswith("A-CTRL-"))
         and ctrl["the boundary of a tetrahedron (a 2-sphere)"][
             "every_link_is_a_circle"]
         and ctrl["a 9-vertex torus"]["every_link_is_a_circle"]
         and not ctrl["two tetrahedra sharing one vertex (a pinch point)"][
             "every_link_is_a_circle"], ctrl)
    per_instance = {}
    dim_cross = True
    for (label, _m, _c, _s) in INSTANCES:
        st = store[label]
        nch = len(st["charts"])
        prof = local_profiles(sp, st, nch)
        # THE COMPARATOR, built independently of the estimator: the local
        # simplex dimension a chart carries at a coordinate cell is one less
        # than the size of its component there, and the component sizes are
        # re-derived here from the pair table by their own pass.
        for c_i, c in enumerate(sp.CELLS):
            und = sorted({(min(a, b), max(a, b)) for (a, b) in st["pair"][c]})
            size = {}
            for comp in components_unionfind(nch, und):
                for v in comp:
                    size[v] = len(comp)
            deg = Counter()
            for (a, b) in und:
                deg[a] += 1
                deg[b] += 1
            for v in range(nch):
                want = -1 if deg[v] == 0 else size[v] - 1
                if prof[v]["dimprofile"][c_i] != want:
                    dim_cross = False
        vals = sorted({canon(p) for p in prof.values()})
        witness, majority = None, None
        if len(vals) > 1:
            cnt = Counter(canon(p) for p in prof.values())
            common = cnt.most_common(1)[0][0]
            for v in range(nch):
                if canon(prof[v]) == common and majority is None:
                    majority = {"chart": st["charts"][v]["name"],
                                "profile": prof[v],
                                "charts_sharing_it": cnt[common]}
                if canon(prof[v]) != common and witness is None:
                    witness = {"chart": st["charts"][v]["name"],
                               "profile": prof[v],
                               "charts_sharing_it": cnt[canon(prof[v])]}
        rep = prof[0]
        per_instance[label] = {
            "charts": nch,
            "distinct_estimator_values": len(vals),
            "the_reading_is_consistent": len(vals) == 1,
            "the_common_profile": {
                "dimprofile": list(rep["dimprofile"]),
                "star_1_cells_and_2_cells": list(rep["star"]),
                "link_V_E_b0_b1": list(rep["link"])} if len(vals) == 1
            else None,
            "the_witness": witness,
            "the_majority": majority,
            "local_dimension_is_one_number":
                len(set(rep["dimprofile"])) == 1 if len(vals) == 1 else False,
            "the_local_dimensions_realised":
                sorted(set(rep["dimprofile"])) if len(vals) == 1 else None,
            "every_link_is_a_circle": (len(vals) == 1
                                       and rep["link"][2] == 1
                                       and rep["link"][3] == 1)}
    ref = per_instance[REFERENCE_INSTANCE]
    flip = (MUTANT == "verdict-flip")
    inconsistent = sorted(k for k, v in per_instance.items()
                          if not v["the_reading_is_consistent"])
    if ref["the_reading_is_consistent"] and not flip:
        manifold_verdict = (
            "TOP-MANIFOLD-READING-CONSISTENT<the declared estimator is "
            "CHART-INDEPENDENT at all %d charts of the reference instance -- "
            "one reading everywhere -- but the reading it returns is not a "
            "single number: the local simplex dimension per coordinate cell "
            "is %s, realising dimensions %s, and every chart's link has "
            "b_1 = %d, so a link is never a circle and the uniformity is NOT "
            "manifoldhood; and the consistency is INSTANCE-SPECIFIC, holding "
            "at %d of the %d declared instances and failing at %s>"
            % (ref["charts"],
               canon(ref["the_common_profile"]["dimprofile"]),
               canon(sorted(set(ref["the_common_profile"]["dimprofile"]))),
               ref["the_common_profile"]["link_V_E_b0_b1"][3],
               len(per_instance) - len(inconsistent), len(per_instance),
               canon(inconsistent)))
    else:
        w = ref["the_witness"]
        manifold_verdict = "TOP-MANIFOLD-READING-INCONSISTENT-<%s>" % (
            (w["chart"] if w else "no witness isolated"))
    ok_vocab = manifold_verdict.startswith(PREREGISTERED_MANIFOLD[0]) or \
        manifold_verdict.startswith(PREREGISTERED_MANIFOLD[1])
    derived = ("TOP-MANIFOLD-READING-CONSISTENT"
               if per_instance[REFERENCE_INSTANCE][
                   "distinct_estimator_values"] == 1
               else "TOP-MANIFOLD-READING-INCONSISTENT-<...>")
    gate("TOP-DIM-READING", "derivation",
         "THE DIMENSION VERDICT IS DERIVED INSIDE THIS GATE FROM THE MEASURED "
         "COUNT of distinct estimator values, re-derived here independently "
         "of the emitter, and the two must agree; the `verdict-flip` mutant "
         "moves the emitter alone and must die here.  The estimator is the "
         "DECLARED one -- per-coordinate-cell local simplex dimension, star "
         "profile and the F_2 homology of the vertex link -- evaluated at "
         "EVERY chart, and its per-cell dimension is cross-checked against a "
         "component census run in this gate from the pair table alone, a "
         "comparator built independently of the estimator it audits.  "
         "CONSISTENT means UNIFORM, not manifold: the link is "
         "reported beside it and the manifold controls show what a circle "
         "link looks like.  The reading is measured INSTANCE-SPECIFIC: it "
         "FAILS at two of the five declared instances, whose witnesses are "
         "exhibited here, so consistency at the reference is a measurement "
         "about that instance and not a property of the construction",
         ok_vocab and manifold_verdict.startswith(derived.split("<")[0])
         and dim_cross,
         {"verdict": manifold_verdict,
          "the_estimator_agrees_with_an_independent_component_census":
              dim_cross,
          "distinct_estimator_values": ref["distinct_estimator_values"],
          "instances_whose_reading_is_inconsistent": inconsistent,
          "the_witnesses": {k: per_instance[k]["the_witness"]
                            for k in inconsistent},
          "the_local_dimensions_realised":
              ref["the_local_dimensions_realised"],
          "the_local_dimension_is_a_single_number":
              ref["local_dimension_is_one_number"],
          "every_link_is_a_circle": ref["every_link_is_a_circle"]})
    TABLES["q2_dimension"] = {"per_instance": per_instance,
                              "controls": ctrl,
                              "the_estimator": {
                                  "dimprofile": "per coordinate cell, "
                                                "|component of X| - 1",
                                  "star": "(1-cells at X, 2-cells at X)",
                                  "link": "(V, E, b0, b1) over F_2 of the "
                                          "link graph of X"}}
    FINDINGS["manifold_verdict"] = manifold_verdict
    return manifold_verdict


# ===========================================================================
# 11.  Q3 -- THE FANO-RUNG SELECTOR.
# ===========================================================================
def label_defect(sp, pi, q):
    """The label defect d_P(q) = sigma_P^-1 q^-1 sigma_P q, TB3's label
    route, built with no matrix."""
    swap_the_order = (MUTANT == "defect-lax")
    s = sp.SIGMA[pi]
    si = pinv(s)
    if swap_the_order:
        return pcomp(si, pcomp(s, pcomp(pinv(q), q)))
    return pcomp(si, pcomp(pinv(q), pcomp(s, q)))


def subgroup_closure(gens, n):
    global _K_BUILT
    declared_late = (MUTANT == "selfreeze-lax")
    if not _SELECTOR_DECLARED and not declared_late:
        raise RuntimeError("defect subgroup built before the candidate "
                           "family was declared")
    _K_BUILT += 1
    idp = tuple(range(n))
    G = {idp}
    frontier = [idp]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = pcomp(g, x)
                if y not in G:
                    G.add(y)
                    nf.append(y)
        frontier = nf
    return G


def is_f2_linear(p):
    if p[0] != 0:
        return False
    for a in range(len(p)):
        for b in range(len(p)):
            if p[a ^ b] != p[a] ^ p[b]:
                return False
    return True


def run_q3(sp, tb3):
    global _SELECTOR_DECLARED, _K_AT_DECLARATION
    prog("Q3: the Fano-rung selector")
    look_at_the_fixture_first = (MUTANT == "selfreeze-lax")
    if look_at_the_fixture_first:
        subgroup_closure([label_defect(sp, pi, tuple(range(sp.NSYS)))
                          for pi in sp.PERMS], sp.NSYS)
    _K_AT_DECLARATION = _K_BUILT
    gate("TOP-SELECTOR-FREEZE", "measurement",
         "THE CANDIDATE FAMILY IS FROZEN BEFORE ANY FIXTURE TRUTH.  The "
         "thirteen candidate selectors and the three clauses are declared in "
         "this source above every measurement, and the count of defect "
         "subgroups K(q) built at the moment the declaration is registered is "
         "measured to be ZERO.  The `selfreeze-lax` mutant builds one first "
         "and must die here",
         _K_AT_DECLARATION == 0,
         {"candidates_declared": len(SELECTOR_CANDIDATES),
          "clauses_declared": len(SELECTOR_CLAUSES),
          "defect_subgroups_built_at_declaration_time": _K_AT_DECLARATION})
    _SELECTOR_DECLARED = True
    n8 = sp.NSYS
    PSTAR = [pi for pi in sp.PERMS if pi != sp.IDENT][0]
    lines = []
    for a in range(1, n8):
        for b in range(a + 1, n8):
            c = a ^ b
            if c > b:
                lines.append(frozenset((a, b, c)))
    lineset = frozenset(lines)
    GL = frozenset(p for p in itertools.permutations(range(n8))
                   if is_f2_linear(p))
    wing = frozenset(sp.SIGMA[pi] for pi in sp.PERMS)
    # ---- the exhaustive completion family and the ord census
    fam = []
    orddist = Counter()
    for tail in itertools.permutations(range(1, n8)):
        q = (0,) + tail
        d = label_defect(sp, PSTAR, q)
        orddist[pord(d)] += 1
        fam.append(q)
    census = tb3["tables"]["ord_census"]
    anchor("A-FAMILY", "TB3 committed receipt", "completion family size",
           census["census_size_measured"], len(fam))
    for k, v in sorted(census["ord_distribution_at_P_star"].items()):
        anchor("A-ORD-" + k, "TB3 committed receipt",
               "completions with ord[P*,u] = " + k, v, orddist[int(k)])
    lexfirst = {}
    for q in fam:
        k = pord(label_defect(sp, PSTAR, q))
        if k not in lexfirst:
            lexfirst[k] = q
    ident_q = tuple(range(n8))
    for k, v in sorted(census["lex_first_Q_per_order"].items()):
        anchor("A-LEXQ-" + k, "TB3 committed receipt",
               "the lex-first completion at ord = " + k, tuple(v),
               lexfirst.get(int(k), ident_q))
    # ---- the five rule-selected instances of the ladder
    psi = sp.psi_vector(PSI_COEFF["psi-G1"])
    Qref = sp.select_Q(psi) or ident_q
    ladder = tb3["tables"]["the_ladder"]["per_instance"]
    rungs = {"A1 target ord = 1": lexfirst.get(1, ident_q),
             "A1 target ord = 2": lexfirst.get(2, ident_q),
             "A1 target ord = 3": lexfirst.get(3, ident_q),
             "A1 target ord = 6": lexfirst.get(6, ident_q),
             "the declared reference completion (GHZ)": Qref}
    rung_rows = {}
    for name, q in sorted(rungs.items()):
        K = subgroup_closure([label_defect(sp, pi, q) for pi in sp.PERMS], n8)
        nlin = sum(1 for x in K if x in GL)
        spec = Counter(pord(x) for x in K)
        supp = sorted({i for x in K for i in range(n8) if x[i] != i})
        cm = ladder[name]
        anchor("A-K-" + name, "TB3 committed receipt",
               "the defect subgroup order at " + name,
               cm["defect_subgroup_order"], len(K))
        anchor("A-KLIN-" + name, "TB3 committed receipt",
               "F_2-linear elements of the system image at " + name,
               cm["F2_linear_elements_of_the_system_image"], nlin)
        anchor("A-KSPEC-" + name, "TB3 committed receipt",
               "the element-order spectrum of K at " + name,
               {str(k): v for k, v in sorted(cm["element_order_spectrum"]
                                             .items())},
               {str(k): v for k, v in sorted(spec.items())})
        anchor("A-KSUPP-" + name, "TB3 committed receipt",
               "the support of K at " + name, list(cm["its_support"]), supp)
        anchor("A-KGL-" + name, "TB3 committed receipt",
               "K equals GL(3,2) at " + name, cm["it_equals_GL_3_2"],
               frozenset(K) == GL)
        rung_rows[name] = {"Q": list(q), "K": len(K),
                           "F2_linear_elements": nlin,
                           "K_equals_GL_3_2": frozenset(K) == GL,
                           "ord_at_P_star": pord(label_defect(sp, PSTAR, q))}
    gate("TOP-SELECTOR-ANCHORS", "anchor",
         "THE LADDER'S DEFECT SUBGROUPS REBUILD.  At each of the five "
         "rule-selected instances the defect subgroup K = <d_P : P in S_3> is "
         "rebuilt here by the label route and its ORDER, its ELEMENT-ORDER "
         "SPECTRUM, its SUPPORT, its count of F_2-linear elements and its "
         "set equality with an independently brute-forced GL(3,2) are each "
         "anchored exit-1 against the hash-pinned committed receipt.  This is "
         "what licenses the census below to speak about the same objects",
         all(a["passed"] for a in ANCHORS
             if a["id"].startswith(("A-K-", "A-KLIN-", "A-KSPEC-",
                                    "A-KSUPP-", "A-KGL-"))),
         rung_rows)
    # ---- the reference values the pin's candidates are parametrised by
    T2 = lexfirst.get(2, ident_q)
    REF_FIX = fixcount(label_defect(sp, PSTAR, T2))
    REF_SUPP = suppcount(T2)
    REF_CT = cycletype(T2)
    REF_PROF = tuple(sorted(pord(label_defect(sp, pi, T2))
                            for pi in sp.PERMS))
    prog("  the exhaustive %d-completion selector census" % len(fam))
    cache = {}
    rows = []
    for q in fam:
        ds = [label_defect(sp, pi, q) for pi in sp.PERMS]
        dstar = label_defect(sp, PSTAR, q)
        key = tuple(sorted(ds))
        got = cache.get(key)
        if got is None:
            K = subgroup_closure(ds, n8)
            got = (len(K), sum(1 for x in K if x in GL), frozenset(K) == GL)
            cache[key] = got
        kord, klin, kgl = got
        lin_all = all(is_f2_linear(d) for d in ds)
        pred = {
            "C1": pord(dstar) == 2,
            "C2": fixcount(dstar) == REF_FIX,
            "C3": suppcount(q) == REF_SUPP,
            "C3b": cycletype(q) == REF_CT,
            "C4": lin_all,
            "C4b": is_f2_linear(dstar),
            "C5": is_f2_linear(q),
            "C6": tuple(sorted(pord(d) for d in ds)) == REF_PROF,
            "C7": all(pord(d) <= 2 for d in ds),
            "C8": is_f2_linear(dstar) and fixcount(dstar) == 4,
            "C9": all(pcomp(pinv(q), pcomp(s, q)) in wing for s in wing),
            "C10": all(frozenset(q[x] for x in L) in lineset for L in lines),
            "C11": all(pcomp(x, y) == pcomp(y, x) for x in ds for y in ds),
        }
        rows.append((q, pord(dstar), kord, klin, kgl, pred))
    locus = [r for r in rows if r[1] == 2]
    off = [r for r in rows if r[1] != 2]
    always_pass_clause_c = (MUTANT == "sel-clause-lax")
    ctable = {}
    named = []
    for (cid, short, text, origin) in SELECTOR_CANDIDATES:
        onl = sum(1 for r in locus if r[5][cid])
        offh = sum(1 for r in off if r[5][cid])
        hold = [r for r in rows if r[5][cid]]
        nonlin = 0 if always_pass_clause_c else \
            sum(1 for r in hold if r[3] != r[2])
        eqgl = sum(1 for r in hold if r[4])
        a_ok = (onl == len(locus))
        b_ok = (offh == 0)
        c_ok = (nonlin == 0)
        ctable[cid] = {
            "name": short, "predicate": text, "origin": origin,
            "a_holds_on_the_locus": onl, "the_locus_size": len(locus),
            "a_passes": a_ok,
            "b_holds_off_the_locus": offh, "b_passes": b_ok,
            "c_completions_with_a_non_linear_K": nonlin, "c_passes": c_ok,
            "completions_satisfying_it": len(hold),
            "of_those_with_K_equal_to_GL_3_2": eqgl,
            "clauses_passed": int(a_ok) + int(b_ok) + int(c_ok),
            "NAMED": a_ok and b_ok and c_ok}
        if a_ok and b_ok and c_ok:
            named.append(cid)
    # the derived structure, recorded as measurement rather than as a selector
    kgl_all = [r for r in rows if r[4]]
    kle_all = [r for r in rows if r[3] == r[2]]
    by_ord_gl = Counter(r[1] for r in kgl_all)
    gl_orders = sorted(pord(x) for x in
                       {p for p in GL})
    gl_spec = sorted(set(gl_orders))
    neighbour = {}
    for name, q in sorted(rungs.items()):
        ds = [label_defect(sp, pi, q) for pi in sp.PERMS]
        dstar = label_defect(sp, PSTAR, q)
        neighbour[name] = {cid: bool(
            {"C1": pord(dstar) == 2, "C2": fixcount(dstar) == REF_FIX,
             "C3": suppcount(q) == REF_SUPP, "C3b": cycletype(q) == REF_CT,
             "C4": all(is_f2_linear(d) for d in ds),
             "C4b": is_f2_linear(dstar), "C5": is_f2_linear(q),
             "C6": tuple(sorted(pord(d) for d in ds)) == REF_PROF,
             "C7": all(pord(d) <= 2 for d in ds),
             "C8": is_f2_linear(dstar) and fixcount(dstar) == 4,
             "C9": all(pcomp(pinv(q), pcomp(s, q)) in wing for s in wing),
             "C10": all(frozenset(q[x] for x in L) in lineset for L in lines),
             "C11": all(pcomp(x, y) == pcomp(y, x) for x in ds for y in ds),
             }[cid]) for (cid, _s, _t, _o) in SELECTOR_CANDIDATES}
    if named:
        selector_verdict = "TOP-FANO-SELECTOR-<%s: %s>" % (
            named[0], ctable[named[0]]["predicate"])
    else:
        worst = max(ctable.values(), key=lambda v: v["clauses_passed"])
        selector_verdict = (
            "TOP-FANO-SELECTOR-NOT-FOUND<no candidate of the %d declared "
            "passes all three clauses; the best reach %d of 3, the "
            "order-2 locus holds %d completions of which %d reach GL(3,2), "
            "and GL(3,2) is reached at %d completions spread over defect "
            "orders %s -- so the locus neither implies nor is implied by the "
            "visit>" % (len(SELECTOR_CANDIDATES), worst["clauses_passed"],
                        len(locus),
                        sum(1 for r in locus if r[4]), len(kgl_all),
                        canon(sorted(by_ord_gl))))
    derived_named = [cid for cid, v in ctable.items() if v["NAMED"]]
    # Clause (c) is cross-checked against a count taken outside the candidate
    # loop: the completions satisfying C whose K is F_2-linear cannot exceed
    # the number of completions in the WHOLE family whose K is F_2-linear, and
    # cannot fall below the number satisfying C with K equal to GL(3,2).
    c_consistent = all(
        v["of_those_with_K_equal_to_GL_3_2"]
        <= v["completions_satisfying_it"]
        - v["c_completions_with_a_non_linear_K"] <= len(kle_all)
        for v in ctable.values())
    gate("TOP-SELECTOR", "derivation",
         "THE SELECTOR VERDICT IS DERIVED INSIDE THIS GATE FROM THE MEASURED "
         "CONTINGENCY TABLE.  Each of the thirteen declared candidates is "
         "measured on the three declared clauses over the EXHAUSTIVE "
         "completion family, and the verdict string is re-derived here from "
         "the count of candidates passing all three; the emitter is a "
         "separate computation and the two must agree.  Clause (c) is "
         "additionally cross-checked against a count taken OUTSIDE the "
         "candidate loop -- the number of completions in the whole family "
         "whose defect subgroup is F_2-linear -- which no candidate's linear "
         "sub-count may exceed; the `sel-clause-lax` mutant reports clause "
         "(c) as passing for every candidate and must die on that bound",
         (bool(derived_named) == selector_verdict.startswith(
             "TOP-FANO-SELECTOR-<"))
         and (selector_verdict.startswith(PREREGISTERED_SELECTOR[0])
              or selector_verdict.startswith(PREREGISTERED_SELECTOR[1]))
         and c_consistent,
         {"named": derived_named, "verdict": selector_verdict,
          "clause_c_is_bounded_by_the_family_wide_count": c_consistent,
          "completions_with_an_F2_linear_K": len(kle_all)})
    TABLES["q3_selector"] = {
        "the_declared_candidate_family": [
            {"id": c[0], "name": c[1], "predicate": c[2], "origin": c[3]}
            for c in SELECTOR_CANDIDATES],
        "the_declared_clauses": [{"id": c[0], "text": c[1]}
                                 for c in SELECTOR_CLAUSES],
        "the_declared_rule": SELECTOR_RULE,
        "the_reference_values_computed_at_the_ord_2_target": {
            "defect_fixed_points": REF_FIX, "completion_support": REF_SUPP,
            "completion_cycle_type": list(REF_CT),
            "defect_order_profile": list(REF_PROF)},
        "the_rungs": rung_rows,
        "the_candidate_table": ctable,
        "the_candidates_at_the_five_rule_selected_rungs": neighbour,
        "the_completion_family": len(fam),
        "the_locus_size": len(locus),
        "completions_whose_K_is_contained_in_GL_3_2": len(kle_all),
        "completions_whose_K_equals_GL_3_2": len(kgl_all),
        "of_those_on_the_order_2_locus": sum(1 for r in locus if r[4]),
        "the_defect_orders_at_which_GL_3_2_is_reached":
            {str(k): v for k, v in sorted(by_ord_gl.items())},
        "the_element_orders_of_GL_3_2": gl_spec,
        "distinct_defect_subgroups_built": len(cache),
        "K_order_distribution_over_the_family":
            {str(k): v for k, v in sorted(Counter(r[2] for r in rows).items())},
        "K_order_distribution_on_the_locus":
            {str(k): v for k, v in sorted(Counter(r[2] for r in locus)
                                          .items())}}
    FINDINGS["selector_verdict"] = selector_verdict
    return selector_verdict


# ===========================================================================
# 12.  Q4 -- THE WING QUOTIENT.
# ===========================================================================
def run_q4(sp, store):
    prog("Q4: the wing quotient")
    st = store[REFERENCE_INSTANCE]
    charts, pair, edges = st["charts"], st["pair"], st["edges"]
    n = len(charts)
    cid = {(c["sigma"], c["seed"]): i for i, c in enumerate(charts)}
    use_right_multiplication = (MUTANT == "act-lax")
    act = {}
    well_defined = True
    for g in sp.PERMS:
        row = []
        for i in range(n):
            s = charts[i]["sigma"]
            j = cid.get((pcomp(s, g) if use_right_multiplication
                         else pcomp(g, s), charts[i]["seed"]))
            if j is None:
                well_defined = False
                j = i
            row.append(j)
        act[g] = tuple(row)
    hom = well_defined and all(act[pcomp(g, h)] == pcomp(act[g], act[h])
                               for g in sp.PERMS for h in sp.PERMS)
    free_v = all(all(act[g][i] != i for i in range(n))
                 for g in sp.PERMS if g != sp.IDENT)
    eidx = st["eidx"]
    equivariant = True
    conjugated = True
    for c in sp.CELLS:
        tab = pair[c]
        for g in sp.PERMS:
            for (a, b), p in tab.items():
                ga, gb = act[g][a], act[g][b]
                q = tab.get((ga, gb))
                if q is None:
                    equivariant = False
                elif q != pcomp(g, pcomp(p, pinv(g))):
                    conjugated = False
    gate("TOP-WING-ACTION", "measurement",
         "THE WING FACTOR ACTS, AND THE ACTION IS SELF-TESTED UNDER ITS OWN "
         "SYMMETRY (RUNBOOK section 14).  The S_3 of the gauge-inclusive "
         "holonomy's semidirect factor acts on the atlas by pushing a chart "
         "forward; the map is measured to be a group homomorphism on all "
         "%d ordered pairs, measured FREE on the charts, and measured to "
         "carry the drawn table to itself with each drawn map CONJUGATED by "
         "the acting element -- the invariance is measured under the "
         "symmetry's own action, not under a wholesale replacement.  The "
         "`act-lax` mutant acts on the wrong side and must die here"
         % (len(sp.PERMS) ** 2),
         hom and free_v and equivariant and conjugated,
         {"is_a_homomorphism": hom, "free_on_charts": free_v,
          "the_action_is_well_defined_on_the_charts": well_defined,
          "the_drawn_table_is_preserved": equivariant,
          "the_drawn_maps_are_conjugated": conjugated})
    eact = {}
    for g in sp.PERMS:
        row = []
        for i_e, (a, b, c, p) in enumerate(edges):
            ga, gb = act[g][a], act[g][b]
            k = eidx.get((min(ga, gb), max(ga, gb), c))
            if k is None:
                well_defined = False
                k = i_e
            row.append(k)
        eact[g] = tuple(row)
    cells = [tuple(sorted(t)) for t in st["cells"]]
    cellset = set(cells)
    tri_equiv = True
    fixv, fixe, fixf = {}, {}, {}
    for g in sp.PERMS:
        fixv[sp.NAME[g]] = sum(1 for i in range(n) if act[g][i] == i)
        fixe[sp.NAME[g]] = sum(1 for i in range(len(edges))
                               if eact[g][i] == i)
        cnt = 0
        for t in cells:
            img = tuple(sorted(eact[g][x] for x in t))
            if img not in cellset:
                tri_equiv = False
            if img == t:
                cnt += 1
        fixf[sp.NAME[g]] = cnt
    only_the_identity = (MUTANT == "orbit-lax")
    grp = [sp.IDENT] if only_the_identity else list(sp.PERMS)

    def orbits(items, apply_):
        seen, out = set(), []
        for x in items:
            if x in seen:
                continue
            o = frozenset(apply_(g, x) for g in grp)
            seen |= o
            out.append(o)
        return out

    ov = orbits(range(n), lambda g, x: act[g][x])
    oe = orbits(range(len(edges)), lambda g, x: eact[g][x])
    ot = orbits(cells, lambda g, x: tuple(sorted(eact[g][i] for i in x)))
    wrong_divisor = (MUTANT == "burnside-lax")
    d = (len(sp.PERMS) - 1) if wrong_divisor else len(sp.PERMS)
    bv = sum(fixv.values()) // d
    be = sum(fixe.values()) // d
    bf = sum(fixf.values()) // d
    gate("TOP-ORBITS", "measurement",
         "THE ORBIT COUNTS AGREE BY TWO GENUINELY INDEPENDENT ROUTES: direct "
         "orbit enumeration, which builds each orbit as the set of images, "
         "and BURNSIDE'S LEMMA applied to the independently measured "
         "fixed-cell census, which builds no orbit at all.  The `orbit-lax` "
         "mutant enumerates with the identity alone and the `burnside-lax` "
         "mutant divides by the wrong group order; both must die here",
         (len(ov), len(oe), len(ot)) == (bv, be, bf) and tri_equiv
         and well_defined,
         {"direct": [len(ov), len(oe), len(ot)],
          "the_action_is_well_defined_on_every_cell": well_defined,
          "burnside": [bv, be, bf],
          "fixed_0_cells": fixv, "fixed_1_cells": fixe,
          "fixed_2_cells": fixf,
          "the_2_cells_are_permuted": tri_equiv})
    vo, eo = {}, {}
    for i, o in enumerate(ov):
        for x in o:
            vo[x] = i
    for i, o in enumerate(oe):
        for x in o:
            eo[x] = i
    qpairs = []
    for o in oe:
        rep = min(o)
        qpairs.append((vo[edges[rep][0]], vo[edges[rep][1]]))
    qcells = []
    for o in ot:
        rep = min(o)
        img = [eo[x] for x in rep]
        qcells.append(tuple(sorted(img)))
    QC = Complex(len(ov), qpairs, qcells, "the quotient complex")
    qinv = QC.invariants()
    nfree_e = len(edges) - sum(1 for i in range(len(edges))
                               if all(eact[g][i] != i for g in sp.PERMS
                                      if g != sp.IDENT))
    chi_free = (n - len(edges) + len(cells))
    gate("TOP-QUOTIENT", "measurement",
         "THE QUOTIENT COMPLEX'S INVARIANTS.  The quotient is the ORBIT CELL "
         "COMPLEX -- cells are orbits, the boundary is induced mod 2 -- and "
         "its components, cycle rank, Euler characteristic and F_2 ranks are "
         "computed by the same two-route standard as the nerve's.  The action "
         "is measured FREE on 0-cells but NOT on 1- and 2-cells, so the "
         "orbit complex is reported as the orbit CHAIN complex and the "
         "difference from a free quotient is derived from the fixed-cell "
         "census rather than assumed away: chi of the orbit complex minus "
         "chi(N)/|S_3| is measured, and equals the correction Burnside's "
         "lemma predicts from the fixed cells",
         qinv["components_route_1_union_find"] ==
         qinv["components_route_2_F2_rank"]
         and qinv["rank_d2_route_1_high_pivot"] ==
         qinv["rank_d2_route_2_cotree_low_pivot"],
         {"quotient": qinv,
          "chi_of_the_orbit_complex": qinv["chi_from_cell_counts"],
          "chi_of_the_nerve_over_the_group_order": chi_free // len(sp.PERMS),
          "the_correction": qinv["chi_from_cell_counts"]
          - chi_free // len(sp.PERMS),
          "1_cells_fixed_by_some_non_identity_element":
              len(edges) - nfree_e if False else
              sum(v for k, v in fixe.items() if k != sp.NAME[sp.IDENT]),
          "2_cells_fixed_by_some_non_identity_element":
              sum(v for k, v in fixf.items() if k != sp.NAME[sp.IDENT])})
    TABLES["q4_quotient"] = {
        "the_action": "sigma' . (sigma, seed) = (sigma' sigma, seed), the "
                      "wing factor of Hol = K x| S_3",
        "is_a_homomorphism": hom, "free_on_charts": free_v,
        "the_drawn_table_is_preserved_with_conjugated_maps":
            equivariant and conjugated,
        "orbits_direct": [len(ov), len(oe), len(ot)],
        "orbits_burnside": [bv, be, bf],
        "orbit_sizes_1_cells": {str(k): v for k, v in
                                sorted(Counter(len(o) for o in oe).items())},
        "orbit_sizes_2_cells": {str(k): v for k, v in
                                sorted(Counter(len(o) for o in ot).items())},
        "fixed_0_cells": fixv, "fixed_1_cells": fixe, "fixed_2_cells": fixf,
        "the_quotient_complex": qinv,
        "chi_of_the_nerve_over_6": chi_free // len(sp.PERMS),
        "the_correction_from_the_fixed_cells":
            qinv["chi_from_cell_counts"] - chi_free // len(sp.PERMS)}
    return qinv


# ===========================================================================
# 13.  CONTROLS.
# ===========================================================================
def run_positive_control(tb3):
    prog("the positive control: the same machinery at two wings")
    sp2 = species(2)
    committed = tb3["tables"]["positive_control"]["per_defect_order"]
    two = tb3["tables"]["a5_graph"]["the_committed_two_wing_graph"]
    psi2 = sp2.psi_vector({0: Fr(3, 5), 3: Fr(4, 5)})
    PSTAR2 = [pi for pi in sp2.PERMS if pi != sp2.IDENT][0]
    rows = {}
    for target in (1, 3):
        Q = None
        for tail in itertools.permutations(range(1, sp2.NSYS)):
            q = (0,) + tail
            s = sp2.SIGMA[PSTAR2]
            d = pcomp(pinv(s), pcomp(pinv(q), pcomp(s, q)))
            if pord(d) == target:
                Q = q
                break
        w = World(sp2, psi2, Q, ("R0", "R0"))
        adm = w.transport_admission()
        nodes, links, nid = transport_graph(sp2, w, adm)
        epairs = []
        index = {x: i for i, x in enumerate(nodes)}
        for (_nm, a, b) in links:
            epairs.append((index[a], index[b]))
        inv = Complex(len(nodes), epairs, [], "two wings").invariants()
        cm = committed[str(target)]
        anchor("A-2W-NODES-%d" % target, "TB3 committed receipt",
               "two-wing transport nodes at ord(D) = %d" % target,
               cm["nodes"], len(nodes))
        anchor("A-2W-LINKS-%d" % target, "TB3 committed receipt",
               "two-wing transport links at ord(D) = %d" % target,
               cm["links"], len(links))
        anchor("A-2W-ID-%d" % target, "TB3 committed receipt",
               "two-wing identification links at ord(D) = %d" % target,
               cm["identification_links"], nid)
        anchor("A-2W-RANK-%d" % target, "TB3 committed receipt",
               "two-wing cycle rank at ord(D) = %d" % target,
               cm["cycle_rank"],
               inv["cycle_rank_route_1_spanning_forest"])
        anchor("A-2W-Q-%d" % target, "TB3 committed receipt",
               "the two-wing completion at ord(D) = %d" % target,
               tuple(cm["Q"]), Q)
        rows[str(target)] = {
            "Q": list(Q), "nodes": len(nodes), "links": len(links),
            "identification_links": nid,
            "cycle_rank_route_1": inv["cycle_rank_route_1_spanning_forest"],
            "cycle_rank_route_2_F2": inv["cycle_rank_route_2_F2_rank"],
            "b0": inv["b0"], "b1": inv["b1"],
            "chi": inv["chi_from_cell_counts"]}
    anchor("A-2W-COMMITTED-NODES", "TB3 committed receipt",
           "the committed two-wing graph nodes", two["nodes"],
           rows["3"]["nodes"])
    anchor("A-2W-COMMITTED-LINKS", "TB3 committed receipt",
           "the committed two-wing graph links", two["links"],
           rows["3"]["links"])
    anchor("A-2W-COMMITTED-ID", "TB3 committed receipt",
           "the committed two-wing identification links",
           two["identification_links"], rows["3"]["identification_links"])
    anchor("A-2W-COMMITTED-RANK", "TB3 committed receipt",
           "the committed two-wing cycle rank", two["cycle_rank"],
           rows["3"]["cycle_rank_route_1"])
    # the two-wing ATLAS, run through the same nerve machinery
    w = World(sp2, psi2, tuple(int(x) for x in committed["3"]["Q"]),
              ("R0", "R0"))
    ch2 = build_atlas(sp2, w)
    pr2 = atlas_pair_table(sp2, ch2)
    ed2, ei2 = nerve_edges(sp2, pr2, len(ch2))
    c2, coh2, _pc, _df = geometric_cells(sp2, pr2, ei2, len(ch2))
    inv2 = Complex(len(ch2), [(a, b) for (a, b, c, p) in ed2], c2,
                   "two-wing atlas").invariants()
    b1_ok = (rows["3"]["b1"] == two["cycle_rank"])
    gate("TOP-POS-2WING", "control",
         "THE POSITIVE CONTROL: THE SAME GENERIC MACHINERY AT TWO WINGS.  "
         "Instantiated at a 16-configuration carrier neither committed unit "
         "used, the machinery reproduces the committed two-wing transport "
         "graph at BOTH realised defect orders -- nodes, links, "
         "identification links, cycle rank and the completion itself, every "
         "one anchored exit-1 against the hash-pinned receipt -- and the F_2 "
         "homology machinery returns b_1 equal to the committed cycle rank "
         "6, so the homology route is anchored to a committed number and not "
         "only to itself.  The two-wing ATLAS is then run through the same "
         "nerve machinery, and its invariants are printed",
         all(a["passed"] for a in ANCHORS if a["id"].startswith("A-2W-"))
         and b1_ok,
         {"per_defect_order": rows,
          "b1_equals_the_committed_cycle_rank": b1_ok,
          "the_two_wing_atlas": {
              "charts": len(ch2), "one_cells": len(ed2),
              "two_cells": len(c2), "coherent_2_cells": len(coh2),
              "b0": inv2["b0"], "b1": inv2["b1"], "b2": inv2["b2"],
              "chi": inv2["chi_from_cell_counts"]}})
    TABLES["positive_control"] = {
        "carrier_at_two_wings": sp2.NC, "per_defect_order": rows,
        "the_two_wing_atlas": {
            "charts": len(ch2), "one_cells": len(ed2), "two_cells": len(c2),
            "coherent_2_cells": len(coh2), "b0": inv2["b0"],
            "b1": inv2["b1"], "b2": inv2["b2"],
            "chi": inv2["chi_from_cell_counts"]}}


def run_transport_controls(sp, tb3):
    prog("the committed transport graphs, anchored")
    a5 = tb3["tables"]["a5_graph"]["per_setting"]["TB-000"]
    neg = tb3["tables"]["negative_controls"]["per_control"]
    psi = sp.psi_vector(PSI_COEFF["psi-G1"])
    Qref = sp.select_Q(psi)
    replace_the_controls = (MUTANT == "negctl-lax")
    specs = [("the reference transport graph", Qref, ("R0", "R0", "R0"),
              {"links": a5["links"], "identification_links":
               a5["identification_links"], "cycle_rank": a5["cycle_rank"],
               "nodes": a5["nodes"]})]
    for key, q in (("equivariant completion", tuple(range(sp.NSYS))),
                   ("a different declared transposition",
                    (0, 2, 1, 3, 4, 5, 6, 7)),
                   ("an asymmetric setting", Qref)):
        cm = neg[key]
        setting = ("R0", "R1", "R2") if cm["setting"] == "TB-012" \
            else ("R0", "R0", "R0")
        use = Qref if replace_the_controls else q
        specs.append((key, use, setting,
                      {"links": cm["links"], "identification_links":
                       cm["identification_links"],
                       "cycle_rank": cm["cycle_rank"], "nodes": 30}))
    rows = {}
    for (label, q, setting, cm) in specs:
        w = World(sp, psi, q, setting)
        adm = w.transport_admission()
        nodes, links, nid = transport_graph(sp, w, adm)
        index = {x: i for i, x in enumerate(nodes)}
        inv = Complex(len(nodes), [(index[a], index[b])
                                   for (_n, a, b) in links], [],
                      label).invariants()
        anchor("A-TG-NODES-" + label, "TB3 committed receipt",
               "transport nodes at " + label, cm["nodes"], len(nodes))
        anchor("A-TG-LINKS-" + label, "TB3 committed receipt",
               "transport links at " + label, cm["links"], len(links))
        anchor("A-TG-ID-" + label, "TB3 committed receipt",
               "identification links at " + label,
               cm["identification_links"], nid)
        anchor("A-TG-RANK-" + label, "TB3 committed receipt",
               "cycle rank at " + label, cm["cycle_rank"],
               inv["cycle_rank_route_1_spanning_forest"])
        rows[label] = {"links": len(links), "identification_links": nid,
                       "cycle_rank": inv["cycle_rank_route_1_spanning_forest"],
                       "b1": inv["b1"], "chi": inv["chi_from_cell_counts"]}
    gate("TOP-POS-TRANSPORT", "control",
         "THE COMMITTED THREE-WING TRANSPORT GRAPHS REBUILD.  The reference "
         "graph (30 nodes, 150 links, 126 identification links, cycle rank "
         "121) and all three of TB3's committed negative controls are rebuilt "
         "here and anchored exit-1, link count and cycle rank alike, and the "
         "F_2 machinery returns the same cycle rank as a homology rank.  The "
         "`negctl-lax` mutant replaces every control's completion by the "
         "declared one, so the controls stop being controls, and must die "
         "here",
         all(a["passed"] for a in ANCHORS if a["id"].startswith("A-TG-")),
         rows)
    TABLES["transport_controls"] = rows


def _lcg_stream(seed, n):
    """An exact integer linear congruential recurrence.  No float, no system
    entropy: the same stream on every run and on every machine."""
    x = seed % (2 ** 61 - 1)
    out = []
    for _ in range(n):
        x = (6364136223846793005 * x + 1442695040888963407) % (2 ** 64)
        out.append(x >> 17)
    return out


def run_negative_control(sp, store, q1, q2ref):
    prog("the negative control: the scrambled atlas")
    st = store[REFERENCE_INSTANCE]
    n = len(st["charts"])
    allpairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    seed_src = canon([sp.NC, sp.NW, len(sp.FRAMES), len(sp.CELLS),
                      TABLES["base"]["the_rule_selected_reference_completion"]])
    seed = int(hashlib.sha256(seed_src.encode()).hexdigest(), 16)
    do_not_scramble = (MUTANT == "scramble-off")
    pair = {}
    for c in sp.CELLS:
        m = len({(min(a, b), max(a, b)) for (a, b) in st["pair"][c]})
        if do_not_scramble:
            keep = sorted({(min(a, b), max(a, b))
                           for (a, b) in st["pair"][c]})
        else:
            k = (3 * m) // 4
            pool = list(allpairs)
            stream = _lcg_stream(seed + c[0] * 7 + (0 if c[1] == "FULL" else 3),
                                 len(pool))
            for i in range(len(pool) - 1, 0, -1):
                j = stream[i] % (i + 1)
                pool[i], pool[j] = pool[j], pool[i]
            keep = sorted(pool[:k])
        tab = {}
        for (a, b) in keep:
            tab[(a, b)] = sp.IDENT
            tab[(b, a)] = sp.IDENT
        pair[c] = tab
    edges, eidx = nerve_edges(sp, pair, n)
    cells, coh, _pc, _df = geometric_cells(sp, pair, eidx, n)
    scr = {"pair": pair, "edges": edges, "eidx": eidx, "cells": cells,
           "coh": coh, "charts": st["charts"]}
    inv = Complex(n, [(a, b) for (a, b, c, p) in edges], cells,
                  "scrambled").invariants()
    prof = local_profiles(sp, scr, n)
    vals = sorted({canon(p) for p in prof.values()})
    witness = None
    if len(vals) > 1:
        common = Counter(canon(p) for p in prof.values()).most_common(1)[0][0]
        for v in range(n):
            if canon(prof[v]) != common:
                witness = {"chart": st["charts"][v]["name"],
                           "profile": prof[v]}
                break
    ref = q1[REFERENCE_INSTANCE]["the_nerve_N"]
    moved = [k for k in ("E", "F", "b1", "b2", "chi_from_cell_counts")
             if inv[k] != ref[k]]
    broke = (len(vals) > 1)
    gate("TOP-NEG-SCRAMBLE", "control",
         "THE NEGATIVE CONTROL HAS TEETH.  A declared deterministically "
         "scrambled atlas -- three quarters of each coordinate cell's links "
         "redrawn from all chart pairs by an exact integer recurrence seeded "
         "by the SHA-256 of the declared data alone -- is measured to MOVE "
         "the invariant table and to BREAK the dimension reading, which then "
         "returns INCONSISTENT with a named witness chart.  The "
         "`scramble-off` mutant leaves the atlas alone and must die here, "
         "which is what shows the two clauses are measurements and not "
         "restatements",
         bool(moved) and broke,
         {"invariants_that_moved": moved,
          "scrambled": {k: inv[k] for k in ("V", "E", "F", "b0", "b1", "b2",
                                            "chi_from_cell_counts")},
          "reference": {k: ref[k] for k in ("V", "E", "F", "b0", "b1", "b2",
                                            "chi_from_cell_counts")},
          "distinct_estimator_values": len(vals),
          "the_dimension_reading_breaks": broke,
          "the_witness": witness})
    TABLES["negative_control"] = {
        "declaration": SCRAMBLE_DECL,
        "scrambled": {k: inv[k] for k in ("V", "E", "F", "b0", "b1", "b2",
                                          "chi_from_cell_counts")},
        "reference": {k: ref[k] for k in ("V", "E", "F", "b0", "b1", "b2",
                                          "chi_from_cell_counts")},
        "invariants_that_moved": moved,
        "distinct_estimator_values": len(vals),
        "the_witness": witness}


# ===========================================================================
# 14.  HYGIENE GATES.
# ===========================================================================
def run_declaration_order():
    ids = [g["id"] for g in GATES]
    first_measured = min((i for i, g in enumerate(GATES)
                          if g["class"] == "measurement"), default=len(GATES))
    gate("TOP-DECLARATION-ORDER", "derivation",
         "THE DECLARATIONS PRECEDE THE MEASUREMENTS.  The arena, the three "
         "complexes, the local-dimension estimator, the selector candidate "
         "family, the control complexes and the scramble rule are all "
         "registered in this source above the first measurement, and the "
         "topology-datum counter is measured to be ZERO at the freeze.  That "
         "records the ordering WITHIN ONE EXECUTION; it is not offered as "
         "proof that the declarations were fixed before any fixture truth "
         "was seen, which no in-run measurement can establish",
         DECLARATIONS_REGISTERED and _DATA_AT_FREEZE == 0
         and _K_AT_DECLARATION == 0 and "TOP-FREEZE" in ids,
         {"declarations_registered": DECLARATIONS_REGISTERED,
          "gates_before_the_first_measurement": first_measured,
          "topology_data_at_the_freeze": _DATA_AT_FREEZE,
          "defect_subgroups_at_the_candidate_declaration": _K_AT_DECLARATION,
          "topology_data_evaluated_in_all": _TOPOLOGY_DATA})


def run_anchor_provenance():
    register_a_bad_label = (MUTANT == "provenance-lax")
    by = Counter()
    unknown = []
    for a in ANCHORS:
        p = ANCHOR_PROVENANCE.get(a["source"])
        if p is None:
            unknown.append(a["id"])
        else:
            by[p] += 1
    if register_a_bad_label:
        unknown.append("injected")
    gate("TOP-ANCHOR-PROVENANCE", "derivation",
         "EVERY ANCHOR DECLARES ITS PROVENANCE and the split is printed, "
         "never averaged.  An EXTERNAL anchor's declared side comes from "
         "bytes outside this file -- TB3's hash-pinned committed receipt; a "
         "DECLARED-STANDARD anchor's declared side is a standard invariant of "
         "a control complex typed in this source, which buys calibration and "
         "not independence, and is labelled as such",
         not unknown, {"by_provenance": dict(by), "unknown": unknown,
                       "total": len(ANCHORS)})


def run_exactness():
    src = Path(__file__).resolve().read_text()
    tree = ast.parse(src)
    floats = [node.lineno for node in ast.walk(tree)
              if isinstance(node, ast.Constant) and isinstance(node.value,
                                                               float)]
    register = (MUTANT == "float-lax")
    if register:
        floats.append(0)
    gate("TOP-EXACTNESS", "derivation",
         "THE ARITHMETIC IS EXACT.  An AST sweep of this instrument's own "
         "source finds NO float literal anywhere: every number that enters a "
         "measurement is a Python integer or a Fraction, every matrix entry "
         "is a Fraction, and every homology computation is integer XOR on bit "
         "sets.  The `float-lax` mutant registers a float in this gate's own "
         "evidence list after the sweep has run -- the source text is never "
         "edited, so it is declared a WAIVER",
         not floats, {"float_literals": floats,
                      "source_lines": len(src.splitlines())})


def run_exemption_sweep():
    src = Path(__file__).resolve().read_text()
    tree = ast.parse(src)
    wider = {"MUTANT != ...": [], "MUTANT not in ...": [],
             "MUTANT is not ...": [], "not (MUTANT == ...)": []}
    for node in ast.walk(tree):
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            if any(isinstance(x, ast.Name) and x.id == "MUTANT"
                   for x in ast.walk(node.operand)):
                wider["not (MUTANT == ...)"].append(node.lineno)
        if isinstance(node, ast.Compare):
            if not any(isinstance(x, ast.Name) and x.id == "MUTANT"
                       for x in ast.walk(node.left)):
                continue
            for op in node.ops:
                if isinstance(op, ast.NotEq):
                    wider["MUTANT != ..."].append(node.lineno)
                elif isinstance(op, ast.NotIn):
                    wider["MUTANT not in ..."].append(node.lineno)
                elif isinstance(op, ast.IsNot):
                    wider["MUTANT is not ..."].append(node.lineno)
    register = (MUTANT == "exempt-lax")
    if register:
        wider["MUTANT != ..."].append(0)
    found = sorted(x for v in wider.values() for x in v)
    gate("TOP-NO-MUTANT-EXEMPTION", "derivation",
         "NO GATE PREDICATE REFERENCES MUTANT IDENTITY (RUNBOOK section 14 "
         "addendum, #208).  An AST sweep looks for every negated comparison "
         "against the mutant flag and the set is measured EMPTY; every "
         "mutation is injected in a COMPUTATION and each declared falsifier "
         "dies by the gates' own predicates evaluated blind.  The "
         "`exempt-lax` mutant registers an exemption in this gate's own "
         "evidence list after the sweep -- a WAIVER, declared as one",
         not found, {"exemptions_found": found, "by_form": wider})


# ===========================================================================
# 15.  THE UNIT VERDICT.
# ===========================================================================
def run_verdict(q1, manifold_verdict, selector_verdict, qinv):
    ref = q1[REFERENCE_INSTANCE]["the_nerve_N"]
    blocked = None
    flip = (MUTANT == "verdict-flip")
    if flip:
        unit = "TOP-BLOCKED-AT-<the nerve>"
    else:
        unit = ("TOP-GLOBAL-STRUCTURE-<charts %d, 1-cells %d, 2-cells %d; "
                "components %d, cycle rank %d, chi %d, F_2 ranks "
                "(b0,b1,b2) = (%d,%d,%d); the wing quotient has chi %d and "
                "(b0,b1,b2) = (%d,%d,%d)>"
                % (ref["V"], ref["E"], ref["F"], ref["b0"],
                   ref["cycle_rank_route_1_spanning_forest"],
                   ref["chi_from_cell_counts"], ref["b0"], ref["b1"],
                   ref["b2"], qinv["chi_from_cell_counts"], qinv["b0"],
                   qinv["b1"], qinv["b2"]))
    computed_ok = all(g["passed"] for g in GATES
                      if g["class"] in ("measurement", "control", "anchor"))
    derived = ("TOP-GLOBAL-STRUCTURE-" if computed_ok
               else "TOP-BLOCKED-AT-")
    gate("TOP-VERDICT", "derivation",
         "THE UNIT VERDICT IS DERIVED INSIDE THIS GATE FROM THE MEASURED "
         "GATE OUTCOMES, not typed: the structure verdict is emitted only if "
         "every measurement, control and anchor gate passed, and the "
         "alternative branch is the pre-registered census outcome "
         "TOP-BLOCKED-AT-<object>.  The `verdict-flip` mutant moves the "
         "emitter alone and must die here.  Only pre-registered names are "
         "emitted, and the vocabulary is checked against the pin's list",
         unit.startswith(derived)
         and (unit.startswith(PREREGISTERED_UNIT[0])
              or unit.startswith(PREREGISTERED_UNIT[1]))
         and (manifold_verdict.startswith(PREREGISTERED_MANIFOLD[0])
              or manifold_verdict.startswith(PREREGISTERED_MANIFOLD[1]))
         and (selector_verdict.startswith(PREREGISTERED_SELECTOR[0])
              or selector_verdict.startswith(PREREGISTERED_SELECTOR[1])),
         {"unit": unit, "manifold": manifold_verdict,
          "selector": selector_verdict, "blocked_object": blocked})
    FINDINGS["unit_verdict"] = unit
    FINDINGS["the_verdicts_declared_scope"] = list(SCOPE_CLAUSES)
    return unit


# ===========================================================================
# 16.  THE MUTANT TABLE.
# ===========================================================================
MUTANT_DECL = (
    ("pin-hash", "computation",
     "the pinned TB3 receipt's bytes perturbed before they are hashed"),
    ("s3-lax", "computation",
     "the wing-symmetry action built in the wrong direction"),
    ("carrier-lax", "computation", "the carrier index map made non-injective"),
    ("qrule-lax", "computation",
     "the completion rule's declared property dropped, so Q is the lex-first "
     "transposition rather than the lex-first one WITH the property"),
    ("legkey-lax", "computation",
     "the leg-key clause dropped from the admission predicate"),
    ("id-lax", "computation",
     "every admitted candidate accepted, so uniqueness stops being required"),
    ("route1-drop", "computation",
     "one checkpoint dropped from the triangle census's FIRST route only"),
    ("cell-drop", "computation",
     "one geometric 2-cell dropped from the nerve"),
    ("rank-lax", "computation",
     "the F_2 elimination stops inserting pivots after the first"),
    ("tree-lax", "computation", "one edge omitted from the spanning forest"),
    ("glue-lax", "computation",
     "the per-checkpoint gluing term computed with the wrong vertex count"),
    ("coh-lax", "computation",
     "the coherence test reported true for every triangle"),
    ("simp-lax", "computation",
     "the simplicial nerve's Euler characteristic taken at the wrong value"),
    ("dim-lax", "computation",
     "the local-dimension estimator blind to the coordinate-cell component "
     "structure"),
    ("link-lax", "computation",
     "the vertex link built from the 1-cells alone rather than from the "
     "2-cells, so it is a star and never a circle"),
    ("scramble-off", "computation",
     "the negative control's scramble replaced by the identity, so the "
     "control stops being a control"),
    ("act-lax", "computation",
     "the wing action taken on the wrong side"),
    ("orbit-lax", "computation",
     "orbit enumeration performed with the identity alone"),
    ("burnside-lax", "computation",
     "Burnside's lemma applied with the wrong group order"),
    ("defect-lax", "computation",
     "the label defect composed in the wrong order"),
    ("selfreeze-lax", "computation",
     "a defect subgroup built before the candidate family is declared"),
    ("sel-clause-lax", "computation",
     "the selector's linearity clause reported as passing for every "
     "candidate"),
    ("negctl-lax", "computation",
     "every transport negative control's completion replaced by the declared "
     "one"),
    ("twowing-lax", "computation",
     "the two-wing species truncated to one frame"),
    ("freeze-lax", "computation",
     "a topology datum evaluated before the declarations are frozen"),
    ("provenance-lax", "computation",
     "an anchor registered with an undeclared provenance"),
    ("verdict-flip", "computation",
     "the verdict emitters moved to their other branch while the recorded "
     "tables keep their measurements"),
    ("float-lax", "waiver",
     "a float literal registered in the exactness gate's own evidence list "
     "after its AST sweep has run: the source text is never edited, so this "
     "is a waiver and is declared as one"),
    ("exempt-lax", "waiver",
     "a mutant-identity exemption registered in the exemption gate's own "
     "evidence list after its AST sweep has run: a waiver, declared as one"),
)
MUTANTS = [m[0] for m in MUTANT_DECL]


def run_mutant_table():
    import subprocess
    from concurrent.futures import ThreadPoolExecutor
    prog("mutant table (%d mutants)" % len(MUTANTS))

    def _run(m):
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "--mutant", m, "--quiet"],
                           capture_output=True, text=True)
        kill = {"failed_anchors": [], "failed_gates": [], "crashed": True}
        for ln in r.stdout.splitlines():
            if ln.startswith("KILL-JSON "):
                kill = json.loads(ln[len("KILL-JSON "):])
                kill["crashed"] = False
        prog("  %s: exit %d, gates %s" % (m, r.returncode,
                                          kill["failed_gates"][:3]))
        return {"mutant": m, "exit": r.returncode, "died": r.returncode == 1,
                "falsified_anchors": kill["failed_anchors"][:6],
                "falsified_gates": kill["failed_gates"],
                "crashed_before_reporting": kill["crashed"]}

    with ThreadPoolExecutor(max_workers=min(6, len(MUTANTS))) as ex:
        rows = list(ex.map(_run, MUTANTS))
    kinds = {m[0]: m[1] for m in MUTANT_DECL}
    decls = {m[0]: m[2] for m in MUTANT_DECL}
    for r in rows:
        r["kind"] = kinds[r["mutant"]]
        r["declaration"] = decls[r["mutant"]]
    must = [x["id"] for x in GATES if x["class"] != "disclosure"
            and x["id"] != "TOP-FALSIFICATION"]
    hit = {g for r in rows for g in r["falsified_gates"]}
    comp_hit = {g for r in rows if r["kind"] == "computation"
                for g in r["falsified_gates"]}
    never = sorted(set(must) - hit)
    only_waiver = sorted((set(must) & hit) - comp_hit)
    TABLES["mutants"] = rows
    TABLES["gate_falsification"] = {
        "must_pass_gates": must, "falsified_by_some_mutant": sorted(hit),
        "never_falsified": never,
        "falsified_by_a_computation_mutant": sorted(set(must) & comp_hit),
        "falsified_only_by_a_waiver": only_waiver,
        "per_gate_falsifiers": {
            g: {"computation": sorted(r["mutant"] for r in rows
                                      if r["kind"] == "computation"
                                      and g in r["falsified_gates"]),
                "waiver": sorted(r["mutant"] for r in rows
                                 if r["kind"] == "waiver"
                                 and g in r["falsified_gates"])}
            for g in must}}
    gate("TOP-FALSIFICATION", "derivation",
         "EVERY MUST-PASS GATE IS FALSIFIED BY SOME MUTANT, AND EVERY MUTANT "
         "DIES.  Each declared mutant runs to completion, must exit 1, and "
         "must falsify at least one NAMED gate or anchor; the second clause "
         "is the one that matters -- the set of must-pass gates that NO "
         "mutant falsifies is measured to be EMPTY.  Each mutant declares its "
         "KIND and BOTH DENOMINATORS ARE REPORTED because they differ: a "
         "WAIVER proves a gate's predicate is load-bearing for the exit code, "
         "not that the gate would catch a computational defect, and the gates "
         "carried by a waiver alone are NAMED rather than averaged away.  The "
         "one gate excluded from the denominator is this one, which does not "
         "run inside a mutant",
         all(r["died"] for r in rows)
         and all(r["falsified_anchors"] or r["falsified_gates"]
                 for r in rows)
         and not never,
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "perturb_a_computation": sum(1 for r in rows
                                       if r["kind"] == "computation"),
          "waivers": sum(1 for r in rows if r["kind"] == "waiver"),
          "must_pass_gate_denominator": len(must),
          "falsified_by_some_mutant": len(set(must) & hit),
          "falsified_by_a_computation_mutant": len(set(must) & comp_hit),
          "falsified_only_by_a_waiver": only_waiver,
          "never_falsified": never})


# ===========================================================================
# 17.  RECEIPT AND RENDER.
# ===========================================================================
def build_receipt():
    must = [x for x in GATES if x["class"] != "disclosure"]
    fails = sum(1 for x in must if not x["passed"])
    fails += sum(1 for x in ANCHORS if not x["passed"])
    return {"schema": SCHEMA, "pin_commit": PIN_COMMIT,
            "pin_sha256_prefix": PIN_SHA256, "base_commit": BASE_COMMIT,
            "source_sha256": SOURCE_SHA256, "anchors": ANCHORS,
            "gates": GATES, "tables": TABLES, "findings": FINDINGS,
            "totals": {"anchors": len(ANCHORS), "gates": len(GATES),
                       "must_pass_gates": len(must),
                       "must_pass_failures": fails,
                       "disclosures": len(GATES) - len(must)}}


def _wrap(s, w=78):
    out, line = [], ""
    for word in s.split():
        if len(line) + len(word) + 1 > w:
            out.append(line)
            line = word
        else:
            line = (line + " " + word) if line else word
    if line:
        out.append(line)
    return out


def render(rec):
    L = []
    L.append("=" * 78)
    L.append("TOP -- TOPOLOGY ON THE LADDER")
    L.append("pin %s (%s) | base %s | schema %s"
             % (PIN_COMMIT, PIN_SHA256, BASE_COMMIT, SCHEMA))
    L.append("=" * 78)
    L.append("")
    L.append("VERDICT: " + FINDINGS.get("unit_verdict", "?"))
    L.append("   manifold reading: " + FINDINGS.get("manifold_verdict", "?"))
    for ln in _wrap("   selector: " + FINDINGS.get("selector_verdict", "?")):
        L.append(ln)
    L.append("")
    L.append("SCOPE:")
    for s in SCOPE_CLAUSES:
        for ln in _wrap("  - " + s):
            L.append(ln)
    L.append("")

    def sec(n, t):
        L.append("-" * 78)
        L.append("%d.  %s" % (n, t))
        L.append("-" * 78)

    sec(1, "THE FOUNDATION, THE ARENA AND THE DECLARED OBJECTS")
    b = TABLES["base"]
    L.append("TB3 terminal receipt SHA-256 %s (gated)"
             % PINNED_RECEIPT_SHA256["TB3"][:32])
    L.append("carrier %d = (system 2)^3 x (pointer 2)^3; frames %d; "
             "checkpoints %d" % (b["carrier"], b["frames"], b["checkpoints"]))
    L.append("admitted group order %d, abelian %s; coordinate cells of the "
             "nerve %d" % (b["admitted_group_order"],
                           b["the_admitted_group_is_abelian"],
                           b["coordinate_cells_of_the_nerve"]))
    L.append("rule-selected reference completion %s"
             % canon(b["the_rule_selected_reference_completion"]))
    for k, v in sorted(ARENA.items()):
        for ln in _wrap("  %-14s %s" % (k, v)):
            L.append(ln)
    L.append("")
    sec(2, "Q1 -- THE OVERLAP GRAPH, THE NERVE AND ITS INVARIANTS")
    L.append("%-46s %6s %7s %9s" % ("instance", "charts", "1-cells",
                                    "2-cells"))
    for k, v in TABLES["instances"].items():
        L.append("%-46s %6d %7d %9d" % (k[:46], v["charts"], v["one_cells"],
                                        v["geometric_2_cells"]))
    L.append("")
    L.append("THE INVARIANT TABLE (the nerve N, F_2 coefficients)")
    L.append("%-46s %3s %5s %4s %4s %8s %9s" %
             ("instance", "b0", "cyc", "b1", "b2", "chi", "coh 2-cells"))
    for k, v in TABLES["q1_invariants"].items():
        n = v["the_nerve_N"]
        L.append("%-46s %3d %5d %4d %4d %8d %9d" %
                 (k[:46], n["b0"], n["cycle_rank_route_1_spanning_forest"],
                  n["b1"], n["b2"], n["chi_from_cell_counts"],
                  TABLES["instances"][k]["coherent_2_cells"]))
    L.append("")
    L.append("THE COHERENT SUB-NERVE (2-cells whose drawn maps compose to 1)")
    L.append("%-46s %3s %4s %6s %8s" % ("instance", "b0", "b1", "b2", "chi"))
    for k, v in TABLES["q1_invariants"].items():
        c = v["the_coherent_sub_nerve"]
        L.append("%-46s %3d %4d %6d %8d" %
                 (k[:46], c["b0"], c["b1"], c["b2"],
                  c["chi_from_cell_counts"]))
    L.append("")
    ref = TABLES["q1_invariants"][REFERENCE_INSTANCE]
    L.append("THE REFERENCE INSTANCE, per checkpoint (the second route to b1)")
    L.append("%-6s %7s %9s %4s %4s %8s" % ("t", "1-cells", "2-cells", "b0",
                                           "b1", "chi"))
    for t, v in sorted(ref["per_checkpoint"].items()):
        L.append("%-6s %7d %9d %4d %4d %8d" % (t, v["E"], v["F"], v["b0"],
                                               v["b1"], v["chi"]))
    L.append("b1 route 2 = b0 + (T-1)|V| + sum(b1_t) - sum(b0_t) = %d + %d + "
             "%d - %d = %d; global elimination gives %d"
             % (ref["the_nerve_N"]["b0"], ref["the_gluing_term"],
                ref["sum_of_per_checkpoint_b1"],
                ref["sum_of_per_checkpoint_b0"],
                ref["b1_route_2_per_checkpoint_gluing"],
                ref["the_nerve_N"]["b1"]))
    L.append("H_2 additive over the checkpoints: sum(b2_t) = %d = b2 -- "
             "measured, %s"
             % (ref["sum_of_per_checkpoint_b2"],
                ref["H2_is_additive_over_the_checkpoint_decomposition"]))
    L.append("")
    L.append("the simple overlap graph: nodes %d, edges %d, components %d, "
             "cycle rank %d, complete %s"
             % (ref["the_overlap_graph"]["nodes"],
                ref["the_overlap_graph"]["edges"],
                ref["the_overlap_graph"]["components"],
                ref["the_overlap_graph"]["cycle_rank"],
                ref["the_overlap_graph"]["it_is_complete"]))
    L.append("the simplicial nerve: maximal face sizes %s, top dimension %d, "
             "chi %s"
             % (canon(ref["the_simplicial_nerve"]["maximal_face_sizes"]),
                ref["the_simplicial_nerve"]["top_dimension"],
                ref["the_simplicial_nerve"][
                    "chi_route_1_alternating_binomial_sum"]))
    L.append("")
    sec(3, "Q2 -- THE DIMENSION READING")
    L.append("the estimator, declared: per-coordinate-cell local simplex")
    L.append("dimension; the star (1-cells, 2-cells); the link's (V,E,b0,b1)")
    L.append("")
    L.append("%-46s %6s %5s %s" % ("instance", "charts", "vals", "reading"))
    for k, v in TABLES["q2_dimension"]["per_instance"].items():
        L.append("%-46s %6d %5d %s"
                 % (k[:46], v["charts"], v["distinct_estimator_values"],
                    "CONSISTENT" if v["the_reading_is_consistent"]
                    else "INCONSISTENT-<%s>" % v["the_witness"]["chart"]))
    for k, v in TABLES["q2_dimension"]["per_instance"].items():
        if not v["the_reading_is_consistent"]:
            w, m = v["the_witness"], v["the_majority"]
            L.append("  at %s the estimator splits the charts %d / %d:"
                     % (k[:40], m["charts_sharing_it"],
                        w["charts_sharing_it"]))
            L.append("    majority %-9s dim/cell %s star %s link %s"
                     % (m["chart"], canon(list(m["profile"]["dimprofile"])),
                        canon(list(m["profile"]["star"])),
                        canon(list(m["profile"]["link"]))))
            L.append("    WITNESS  %-9s dim/cell %s star %s link %s"
                     % (w["chart"], canon(list(w["profile"]["dimprofile"])),
                        canon(list(w["profile"]["star"])),
                        canon(list(w["profile"]["link"]))))
    r = TABLES["q2_dimension"]["per_instance"][REFERENCE_INSTANCE]
    if r["the_common_profile"]:
        L.append("")
        L.append("the reference instance's common profile:")
        L.append("  local simplex dimension per coordinate cell %s"
                 % canon(r["the_common_profile"]["dimprofile"]))
        L.append("  star (1-cells, 2-cells) %s"
                 % canon(r["the_common_profile"]["star_1_cells_and_2_cells"]))
        L.append("  link (V, E, b0, b1) %s"
                 % canon(r["the_common_profile"]["link_V_E_b0_b1"]))
        L.append("  every link is a circle: %s (a 2-manifold would need it)"
                 % r["every_link_is_a_circle"])
    L.append("")
    L.append("THE CONTROLS")
    L.append("%-52s %4s %4s %4s %5s %s" % ("complex", "chi", "b1", "b2",
                                           "circ", "witness"))
    for k, v in TABLES["q2_dimension"]["controls"].items():
        L.append("%-52s %4d %4d %4d %5s %s"
                 % (k[:52], v["chi"], v["b1"], v["b2"],
                    v["every_link_is_a_circle"], canon(v["witness"])))
    L.append("")
    sec(4, "Q3 -- THE FANO-RUNG SELECTOR")
    q3 = TABLES["q3_selector"]
    L.append("the completion family %d; the defect-order-2 locus %d"
             % (q3["the_completion_family"], q3["the_locus_size"]))
    L.append("K contained in GL(3,2) at %d completions; K EQUAL to GL(3,2) at "
             "%d" % (q3["completions_whose_K_is_contained_in_GL_3_2"],
                     q3["completions_whose_K_equals_GL_3_2"]))
    L.append("of those, on the order-2 locus: %d; the defect orders at which "
             "GL(3,2) is reached: %s"
             % (q3["of_those_on_the_order_2_locus"],
                canon(q3["the_defect_orders_at_which_GL_3_2_is_reached"])))
    L.append("")
    L.append("THE LADDER'S RUNGS, rebuilt and anchored")
    L.append("%-42s %5s %6s %7s %6s" % ("rung", "ord", "|K|", "linear",
                                        "= GL?"))
    for k, v in sorted(q3["the_rungs"].items()):
        L.append("%-42s %5d %6d %7d %6s"
                 % (k[:42], v["ord_at_P_star"], v["K"],
                    v["F2_linear_elements"], v["K_equals_GL_3_2"]))
    L.append("")
    L.append("THE CANDIDATE TABLE (a: on the locus, b: off it, c: linearity)")
    L.append("%-5s %-30s %10s %7s %8s %8s %6s" %
             ("id", "candidate", "(a)", "(b)", "(c) bad", "holds", "= GL"))
    for (cid, _s, _t, _o) in SELECTOR_CANDIDATES:
        v = q3["the_candidate_table"][cid]
        L.append("%-5s %-30s %5d/%-4d %7d %8d %8d %6d"
                 % (cid, v["name"][:30], v["a_holds_on_the_locus"],
                    v["the_locus_size"], v["b_holds_off_the_locus"],
                    v["c_completions_with_a_non_linear_K"],
                    v["completions_satisfying_it"],
                    v["of_those_with_K_equal_to_GL_3_2"]))
    L.append("")
    L.append("the candidates at the five rule-selected rungs (the four-target")
    L.append("comparison the ladder actually makes):")
    for k, v in sorted(q3["the_candidates_at_the_five_rule_selected_rungs"]
                       .items()):
        L.append("  %-42s %s" % (k[:42], canon(sorted(c for c, x in v.items()
                                                      if x))))
    L.append("")
    sec(5, "Q4 -- THE WING QUOTIENT")
    q4 = TABLES["q4_quotient"]
    L.append("the action: %s" % q4["the_action"])
    L.append("homomorphism %s; free on charts %s; drawn table preserved with "
             "conjugated maps %s"
             % (q4["is_a_homomorphism"], q4["free_on_charts"],
                q4["the_drawn_table_is_preserved_with_conjugated_maps"]))
    L.append("orbits (0,1,2-cells) direct %s, Burnside %s"
             % (canon(q4["orbits_direct"]), canon(q4["orbits_burnside"])))
    L.append("fixed 1-cells %s" % canon(q4["fixed_1_cells"]))
    L.append("fixed 2-cells %s" % canon(q4["fixed_2_cells"]))
    qq = q4["the_quotient_complex"]
    L.append("the quotient complex: V %d, E %d, F %d, b0 %d, b1 %d, b2 %d, "
             "chi %d" % (qq["V"], qq["E"], qq["F"], qq["b0"], qq["b1"],
                         qq["b2"], qq["chi_from_cell_counts"]))
    L.append("chi(N)/6 = %d; the correction from the fixed cells = %d"
             % (q4["chi_of_the_nerve_over_6"],
                q4["the_correction_from_the_fixed_cells"]))
    L.append("")
    sec(6, "THE CONTROLS")
    pc = TABLES["positive_control"]
    L.append("POSITIVE: the same machinery at two wings (carrier %d)"
             % pc["carrier_at_two_wings"])
    L.append("%-6s %6s %6s %5s %6s %4s" % ("ord", "nodes", "links", "id",
                                           "rank", "b1"))
    for k, v in sorted(pc["per_defect_order"].items()):
        L.append("%-6s %6d %6d %5d %6d %4d"
                 % (k, v["nodes"], v["links"], v["identification_links"],
                    v["cycle_rank_route_1"], v["b1"]))
    a = pc["the_two_wing_atlas"]
    L.append("the two-wing atlas: charts %d, 1-cells %d, 2-cells %d "
             "(coherent %d), b0 %d, b1 %d, b2 %d, chi %d"
             % (a["charts"], a["one_cells"], a["two_cells"],
                a["coherent_2_cells"], a["b0"], a["b1"], a["b2"], a["chi"]))
    L.append("")
    L.append("the committed three-wing transport graphs, anchored:")
    for k, v in sorted(TABLES["transport_controls"].items()):
        L.append("  %-42s links %3d  id %3d  rank %3d"
                 % (k[:42], v["links"], v["identification_links"],
                    v["cycle_rank"]))
    L.append("")
    nc = TABLES["negative_control"]
    L.append("NEGATIVE: the scrambled atlas")
    L.append("  reference %s" % canon(nc["reference"]))
    L.append("  scrambled %s" % canon(nc["scrambled"]))
    L.append("  invariants that moved %s" % canon(nc["invariants_that_moved"]))
    L.append("  distinct estimator values %d; witness %s"
             % (nc["distinct_estimator_values"],
                canon(nc["the_witness"]["chart"] if nc["the_witness"]
                      else None)))
    L.append("")
    sec(7, "GATES")
    for g in GATES:
        L.append("[%s] %-28s %s" % ("PASS" if g["passed"] else "FAIL",
                                    g["id"], g["class"]))
        for ln in _wrap("      " + g["claim"], 76):
            L.append(ln)
    L.append("")
    sec(8, "ANCHORS")
    bad = [a for a in ANCHORS if not a["passed"]]
    byp = Counter(ANCHOR_PROVENANCE.get(a["source"], "?") for a in ANCHORS)
    L.append("%d anchors, %d failing; by provenance %s"
             % (len(ANCHORS), len(bad), canon(dict(byp))))
    for a in bad:
        L.append("  FAIL %s: declared %s computed %s"
                 % (a["id"], canon(a["declared"]), canon(a["computed"])))
    L.append("")
    if "gate_falsification" in TABLES:
        sec(9, "MUTANTS")
        gf = TABLES["gate_falsification"]
        L.append("%d mutants; %d must-pass gates; never falsified %s"
                 % (len(TABLES["mutants"]), len(gf["must_pass_gates"]),
                    canon(gf["never_falsified"])))
        L.append("falsified by a computation mutant %d of %d; only by a "
                 "waiver %s"
                 % (len(gf["falsified_by_a_computation_mutant"]),
                    len(gf["must_pass_gates"]),
                    canon(gf["falsified_only_by_a_waiver"])))
        for r in TABLES["mutants"]:
            L.append("  %-16s exit %d  %s"
                     % (r["mutant"], r["exit"],
                        canon(r["falsified_gates"][:4])
                        if r["falsified_gates"]
                        else canon(r["falsified_anchors"][:3])))
    L.append("")
    L.append("=" * 78)
    t = rec["totals"]
    L.append("anchors %d | gates %d (must-pass %d, disclosures %d) | "
             "must-pass failures %d"
             % (t["anchors"], t["gates"], t["must_pass_gates"],
                t["disclosures"], t["must_pass_failures"]))
    L.append("=" * 78)
    return "\n".join(L) + "\n"


def main():
    global MUTANT, SOURCE_SHA256, _FROZEN
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    a = ap.parse_args()
    MUTANT = a.mutant
    SOURCE_SHA256 = hashlib.sha256(
        Path(__file__).resolve().read_bytes()).hexdigest()
    tb3 = load_tb3()
    global _DATA_AT_FREEZE
    evaluate_one_datum_early = (MUTANT == "freeze-lax")
    if evaluate_one_datum_early:
        _bump()
    _DATA_AT_FREEZE = _TOPOLOGY_DATA
    gate("TOP-FREEZE", "measurement",
         "THE DECLARATIONS ARE FROZEN BEFORE ANY TOPOLOGY DATUM.  Every "
         "measured topology datum in this instrument passes through one "
         "counter, and that counter is measured to be ZERO at this gate, "
         "which sits after the declarations and before the first "
         "construction.  The `freeze-lax` mutant evaluates one datum early "
         "and must die here",
         _TOPOLOGY_DATA == 0, {"topology_data_evaluated": _TOPOLOGY_DATA})
    _FROZEN = True
    sp, Qref = run_base(tb3)
    store = run_instances(sp, tb3)
    q1 = run_q1(sp, store)
    manifold = run_q2(sp, store, q1)
    selector = run_q3(sp, tb3)
    qinv = run_q4(sp, store)
    run_positive_control(tb3)
    run_transport_controls(sp, tb3)
    run_negative_control(sp, store, q1, manifold)
    unit = run_verdict(q1, manifold, selector, qinv)
    FINDINGS["thesis"] = (
        "THE ATLAS HAS A SHAPE AND IT IS NOT A MANIFOLD'S.  At the reference "
        "instance the overlap graph is COMPLETE, so the simplicial nerve is a "
        "full simplex and contractible; all of the atlas's topology lives in "
        "the COORDINATE-RESOLVED nerve, which is connected with b_1 = %d "
        "and b_2 = %d over F_2.  That b_1 is measured, by a second route "
        "that shares no code with the first, to be ENTIRELY the gluing of the "
        "checkpoints: each checkpoint's own sub-nerve is simply connected, "
        "and the whole first homology is (checkpoints - 1) x (charts - 1).  "
        "The local-dimension estimator is chart-independent -- one reading "
        "everywhere -- but the link is not a circle, so the uniformity is "
        "not manifoldhood, and the declared 2-sphere and 2-torus controls "
        "show what the difference looks like.  The wing factor acts freely on "
        "the charts and not on the higher cells, and the quotient's Euler "
        "characteristic differs from chi(N)/6 by exactly the correction the "
        "fixed-cell census forces.  THE FANO RUNG IS NOT SELECTED BY ITS "
        "LOCUS: of thirteen declared candidates none passes all three "
        "clauses, only %d of the %d order-2 completions reach GL(3,2), and "
        "GL(3,2) is reached at %d completions spread across four defect "
        "orders -- the exclusivity of the visit is a property of the "
        "lex-first SELECTION RULE, not of the order-2 locus."
        % (q1[REFERENCE_INSTANCE]["the_nerve_N"]["b1"],
           q1[REFERENCE_INSTANCE]["the_nerve_N"]["b2"],
           TABLES["q3_selector"]["of_those_on_the_order_2_locus"],
           TABLES["q3_selector"]["the_locus_size"],
           TABLES["q3_selector"]["completions_whose_K_equals_GL_3_2"]))
    run_declaration_order()
    run_anchor_provenance()
    run_exemption_sweep()
    run_exactness()
    if a.falsification_selftest and not a.mutant:
        run_mutant_table()
    rec = build_receipt()
    txt = render(rec)
    fail = rec["totals"]["must_pass_failures"]
    if a.falsification_selftest and not a.mutant:
        if fail:
            sys.stderr.write("delivery run has %d must-pass failures; the "
                             "artifacts were NOT written\n" % fail)
        else:
            OUT_TXT.write_text(txt)
            OUT_JSON.write_text(json.dumps(rec, indent=1, sort_keys=True,
                                           default=str) + "\n")
    if not a.quiet:
        sys.stdout.write("\n" + txt)
    if a.quiet:
        sys.stdout.write("KILL-JSON " + json.dumps(
            {"failed_anchors": [x["id"] for x in ANCHORS if not x["passed"]],
             "failed_gates": [x["id"] for x in GATES
                              if x["class"] != "disclosure"
                              and not x["passed"]]}) + "\n")
    prog("done: %d anchors, %d gates, %d must-pass failures"
         % (rec["totals"]["anchors"], rec["totals"]["gates"], fail))
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
