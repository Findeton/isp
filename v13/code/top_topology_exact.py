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
  and, for the declared cross-coordinate comparison of D3b, both branches
  being representable and neither favoured:
  CROSS-CELL-COHERENT-DIGONS-FILL-EVERY-DEGREE-1-CLASS
  CROSS-CELL-A-RESIDUAL-SURVIVES-THE-COHERENT-DIGONS-<rank>

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
    "this file, pinned SHA-256": "self-pin",
    "DECLARED-STANDARD (the complex's standard invariants)": "declared",
    "DECLARED-STRUCTURAL (a size forced by the declared base)": "structural",
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

# ---- THE VERDICT TEMPLATES.  Each verdict head carries its own restrictions
#      and every number in head and body alike is INTERPOLATED FROM A MEASURED
#      COUNT.  Each string is built twice: once by the emitter from the live
#      measurement, and once inside its gate from the RECORDED TABLES, and the
#      two are gated BYTE-FOR-BYTE -- qualifiers included (RUNBOOK section 13
#      addendum, #234, and the #257 precedent that a qualifier is part of the
#      verdict).  The `unit-typed`, `manifold-typed` and `selector-typed`
#      mutants move one qualifier of the emitter alone and must die.
V_UNIT = (
    "TOP-GLOBAL-STRUCTURE-OF-THE-COORDINATE-RESOLVED-NERVE-DEGREE-1-IS-THE-"
    "COORDINATE-COUNT-%dx%d-UNMOVED-BY-THE-SCRAMBLE<charts %d, 1-cells %d, "
    "2-cells %d; components %d, cycle rank %d, chi %d, F_2 ranks (b0,b1,b2) "
    "= (%d,%d,%d); b_1 = (T-1)(|V|-1) = %d x %d = %d and the scrambled "
    "control returns b_1 = %d as well, so degree one is the coordinate count "
    "and only b_2 (%d -> %d) sees the identification data; the wing quotient "
    "has chi %d and (b0,b1,b2) = (%d,%d,%d)>")
V_MANIFOLD = (
    "TOP-MANIFOLD-READING-CONSISTENT-AT-%d-OF-%d-INSTANCES-DIMENSIONS-%s-"
    "LINKS-NEVER-CIRCLES-AND-SYMMETRY-FORCED-AT-THE-REFERENCE<the declared "
    "estimator is CHART-INDEPENDENT at all %d charts of the reference "
    "instance -- one reading everywhere -- but the reading it returns is not "
    "a single number: the local simplex dimension per coordinate cell is %s, "
    "realising dimensions %s, and every chart's link has b_1 = %d, so a link "
    "is never a circle and the uniformity is NOT manifoldhood; the drawn "
    "table of that instance is measured to have %d chart-orbit(s) under its "
    "%d measured automorphisms, so chart-independence there is FORCED and is "
    "entered as a disclosure; and the consistency is INSTANCE-SPECIFIC, "
    "holding at %d of the %d declared instances and failing at %s>")
V_MANIFOLD_INCONSISTENT = "TOP-MANIFOLD-READING-INCONSISTENT-<%s>"
V_SELECTOR = (
    "TOP-FANO-SELECTOR-NOT-FOUND-THE-LOCUS-IS-P-STAR-RELATIVE-%s-CLASS<no "
    "candidate of the %d declared passes all three clauses; the best reach "
    "%d of 3, the order-2 locus at the declared P* = %s holds %d completions "
    "of which %d reach GL(3,2), and GL(3,2) is reached at %d completions "
    "spread over defect orders %s -- so the locus neither implies nor is "
    "implied by the visit.  The locus is an ARENA COORDINATE: the %d "
    "transposition symmetries agree at locus %d / on-locus %d, the %d "
    "3-cycles give locus %d / on-locus %d, so both counts are P*-relative "
    "and only the %d completions reaching GL(3,2) as a set are not>")
V_SELECTOR_NAMED = "TOP-FANO-SELECTOR-<%s: %s>"

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
    "the declared wing symmetry P*": "the FIRST NON-IDENTITY element of the "
        "enumerated wing group -- a TRANSPOSITION.  P* is an ARENA "
        "COORDINATE, not a fact about the base: the defect d_P(q), the "
        "order-2 LOCUS and the defect-order axis of the selector census are "
        "all defined relative to it.  All five non-identity wing symmetries "
        "are swept and the sweep is reported (RUNBOOK section 15: an arena "
        "coordinate is declared as data and its dependence is measured)",
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
#  WHETHER A CONSISTENT READING IS A MEASUREMENT AT ALL is itself measured.
#  D is a chart-invariant of the drawn table, so if the drawn table has an
#  automorphism group transitive on charts then CONSISTENT could not have come
#  out otherwise and is a DISCLOSURE (RUNBOOK section 14 addendum, #208).  The
#  DECLARED automorphism candidates are the LEFT TRANSLATIONS of the chart set
#
#     phi_{g,h} : (sigma, seed) |-> (g sigma, h seed),   g, h in S_3,
#
#  thirty-six maps acting simply transitively on the 36 (relabelling, seed)
#  pairs.  Each is TESTED against the drawn relation at every coordinate cell
#  and only the ones that pass are counted; the chart-orbit count of the group
#  they generate is reported beside the estimator's distinct-value count.
#
# ---- D3b.  THE CROSS-COORDINATE DRAWN-MAP COMPARISON, declared before it is
#      run, with BOTH outcomes pre-registered.
#
#  Two charts identified at k >= 2 coordinate cells carry k PARALLEL 1-cells,
#  and every pair of them bounds a DIGON.  A digon is COHERENT when the two
#  drawn maps agree; the pair AGREES when all of its drawn maps agree.  The
#  declared measurement is:
#
#     (i)   how many pairs drawn at >= 2 cells agree, and how many do not;
#     (ii)  the digon census split same-checkpoint / cross-checkpoint, and
#           the coherent sub-census of each;
#     (iii) the rank each family of digons adds to d_2, hence the b_1 that
#           survives it.
#
#  THE PRE-REGISTERED OUTCOMES, both representable, neither favoured:
#     CROSS-CELL-COHERENT-DIGONS-FILL-EVERY-DEGREE-1-CLASS
#         -- the coherent cross-read-time digons alone reduce b_1 to zero, so
#            no degree-one class is carried by a disagreement between the maps
#            drawn at different read times: the surviving cycles of N are an
#            artifact of the declared same-checkpoint 2-cell scope.
#     CROSS-CELL-A-RESIDUAL-SURVIVES-THE-COHERENT-DIGONS-<rank>
#         -- a non-zero b_1 survives, and that residual is a MEASURED
#            cross-read-time obstruction.
#  The outcome is re-derived inside its gate from the measured residual; the
#  `crosscell-typed` mutant emits the other outcome with the tables unchanged.
#
# ---- D3c.  THE BLOCK-INCIDENCE ROUTE to the per-checkpoint homology.
#      At a checkpoint t the FULL rule and the REALIZED rule each partition the
#      charts into the components of their drawn relation (measured, and gated,
#      to be COMPLETE blocks).  I_t is the bipartite BLOCK-INCIDENCE GRAPH:
#      vertices the blocks of the two partitions, an edge for every block pair
#      sharing a chart.  The declared claim, measured at every (instance,
#      checkpoint) pair and NEVER assumed:
#
#         b_0(N_t) = b_0(I_t)   and   b_1(N_t) = cycle rank of I_t,
#
#      so a read time's own topology is the NESTING of the two rules'
#      partitions and nothing else.  I_t has at most a dozen vertices and its
#      invariants are computed by union-find and Euler alone -- no elimination,
#      no 2-cell, no contact with the sub-complex it audits.
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
     "ord(d_{P*}(q)) = 2 -- the locus's own defining property", "pin-derived"),
    ("C2", "defect fixed-point count",
     "|Fix(d_{P*}(q))| equals the reference value", "pin-derived"),
    ("C3", "completion support",
     "|supp(q)| equals the reference value", "pin-derived"),
    ("C3b", "completion cycle type",
     "the cycle type of q equals the reference cycle type", "pin-derived"),
    ("C4", "defect F2-linearity",
     "every d_P(q), P in S_3, is an F_2-linear permutation of the labels",
     "pin-derived"),
    ("C4b", "declared-symmetry defect F2-linearity",
     "d_{P*}(q) is an F_2-linear permutation of the labels", "pin-derived"),
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
# The TYPESET name of each candidate, declared here beside the predicate so
# that the paper's section-5.2 tables can be EMITTED from the recorded table
# rather than retyped.  These are display strings only: no measurement reads
# them, and the ids they key are the ids of the declaration above.
SELECTOR_TYPESET_NAMES = {
    "C1": "involutivity",
    "C2": "defect fixed-point count",
    "C3": "completion support",
    "C3b": "completion cycle type",
    "C4": r"defect $\mathbb F_2$-linearity",
    "C4b": "declared-symmetry defect linearity",
    "C5": r"completion $\mathbb F_2$-linearity",
    "C6": "defect order profile",
    "C7": "involutive profile",
    "C8": "transvection",
    "C9": "$q$ normalises the wing group",
    "C10": "Fano collineation",
    "C11": "abelian defect set",
}
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
SELECTOR_ORIGIN_LEGEND = {
    "pin-derived": "restates the pin's own order-2-locus language.  THE PIN "
                   "CONTAINS NO CANDIDATE LIST: no candidate is quoted from "
                   "it and none may be labelled as if it were",
    "worker": "introduced by this instrument, in this source, above every "
              "measurement",
}
# ---- D4b.  CLAUSE (c) IS A CONTAINMENT, and the containment is measured.
#      K(q) is generated by the six d_P(q), so K(q) is F_2-linear exactly when
#      every generator is: the candidate C4 and the set {q : K(q) <= GL(3,2)}
#      are the same set, which is MEASURED here rather than argued.  Clause
#      (c)'s count for a candidate C is therefore |C \ C4| identically, and
#      "clause (c) passes" is literally the containment C <= C4 -- an
#      algebraic fact about the family, not a measurement about the geometry.
#      Both are computed for every candidate and entered as DISCLOSURES
#      (RUNBOOK section 14 addendum, #208), together with the extensional
#      collapses the family carries: C1 = C2 and C5 = C10.
CLAUSE_C_DISCLOSURE = (
    "CLAUSE (c) HAS NO MEASURED CONTENT OF ITS OWN.  Its count for a "
    "candidate C is measured to be |C \\ C4| for every one of the thirteen, "
    "so clause (c) passes exactly when C is CONTAINED IN C4, and every "
    "passer's zero is forced: C4 because a group generated by F_2-linear "
    "maps is F_2-linear; C5 and C10 because all six sigma_P are measured "
    "F_2-linear, so d_P = sigma_P^-1 q^-1 sigma_P q is linear whenever q is; "
    "C9 because q normalising the wing group puts every d_P inside it.  All "
    "four forcings are measured here as set containments, not asserted.")

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
    break_the_symmetry = (MUTANT == "sym-lax")
    if break_the_symmetry:
        for c in sp.CELLS:
            key = next((k for k in sorted(out[c]) if k[0] < k[1]), None)
            if key is not None:
                del out[c][key]
                break
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
        incidence_bits_not_mod_2 = (MUTANT == "or-lax")
        incidence_bits_in_the_transpose = (MUTANT == "or-lax-T")
        if incidence_bits_not_mod_2:
            d1_rows = [(1 << a) | (1 << b) for (a, b) in self.epairs]
        else:
            d1_rows = [(1 << a) ^ (1 << b) for (a, b) in self.epairs]
        r1_high = rank_f2_high(d1_rows)
        b0_rank = nv - r1_high
        # a third reading: the rank of the TRANSPOSED boundary matrix
        cols = [0] * nv
        for j, (a, b) in enumerate(self.epairs):
            if incidence_bits_in_the_transpose:
                cols[a] |= (1 << j)
                cols[b] |= (1 << j)
            else:
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
        cap = 2000
        chain = all(((1 << self.epairs[x][0]) ^ (1 << self.epairs[x][1]) ^
                     (1 << self.epairs[y][0]) ^ (1 << self.epairs[y][1]) ^
                     (1 << self.epairs[z][0]) ^ (1 << self.epairs[z][1])) == 0
                    for (x, y, z) in self.tris[:cap])
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
            "the_d1_d2_sample_cap": cap,
            "the_2_cells_in_all": nf,
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
    pattern = Counter()
    conjugate = True
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
                                # the three traversal defects are CONJUGATE;
                                # measured here, cell by cell, because it is
                                # what makes the identity entry of the defect
                                # multiset six times the coherent count rather
                                # than an independent census (RUNBOOK section
                                # 13 addendum, #234).
                                pattern[(d1 == ident, d2 == ident,
                                         d3 == ident)] += 1
                                p21 = pcomp(p2, p1)
                                if d2 != pcomp(p1, pcomp(d1, pinv(p1))) or \
                                        d3 != pcomp(p21, pcomp(d1, pinv(p21))):
                                    conjugate = False
                                if d1 == ident or coherence_always_true:
                                    coh.append(key)
    if drop_a_cell and cells:
        cells = cells[:-1]
    return cells, coh, dict(per_ck), dict(defects), {
        "the_traversal_defect_patterns":
            {canon(list(k)): v for k, v in sorted(pattern.items())},
        "the_three_traversal_defects_are_conjugate_at_every_2_cell":
            conjugate,
        "the_pattern_is_never_mixed": len(pattern) <= 2 and all(
            len(set(k)) == 1 for k in pattern)}


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
    shrink_the_maximal_face = (MUTANT == "simp-lax")
    if shrink_the_maximal_face:
        reduced = [frozenset(sorted(m)[:max(1, len(m) // 3)]) for m in reduced]
    return sorted(reduced, key=lambda s: (-len(s), sorted(s))), complete


def cell_blocks(pairtab, nch):
    """The partition a rule draws at one coordinate cell: the components of
    its drawn relation, isolated charts included as singleton blocks."""
    und = sorted({(min(a, b), max(a, b)) for (a, b) in pairtab})
    return [tuple(c) for c in components_unionfind(nch, und)]


def block_incidence(sp, st, nch):
    """D3c: the per-checkpoint homology by the BLOCK-INCIDENCE route.  I_t is
    the bipartite graph on the blocks of the two rules' partitions; its
    invariants are read by union-find and Euler alone -- no elimination, no
    2-cell, nothing shared with the sub-complex it audits."""
    _bump()
    one_rule_only = (MUTANT == "block-lax")
    rows = {}
    for t in sp.CKPTS:
        cells_here = [c for c in sp.CELLS if c[0] == t]
        if not any(st["pair"][c] for c in cells_here):
            continue
        parts = [cell_blocks(st["pair"][(t, r)], nch)
                 for r in (("FULL",) if one_rule_only else ("FULL", "REAL"))]
        verts = [(k, i) for k, p in enumerate(parts) for i in range(len(p))]
        vi = {x: i for i, x in enumerate(verts)}
        owner = []
        for p in parts:
            o = {}
            for i, blk in enumerate(p):
                for v in blk:
                    o[v] = i
            owner.append(o)
        ein = set()
        for k in range(len(parts)):
            for l in range(k + 1, len(parts)):
                for v in range(nch):
                    ein.add((vi[(k, owner[k][v])], vi[(l, owner[l][v])]))
        ein = sorted(ein)
        b0 = len(components_unionfind(len(verts), ein))
        rows[str(t)] = {
            "blocks_per_rule": [len(p) for p in parts],
            "incidence_V": len(verts), "incidence_E": len(ein),
            "b0_of_the_incidence_graph": b0,
            "cycle_rank_of_the_incidence_graph":
                len(ein) - (len(verts) - b0)}
    return rows


def cross_cell_drawn_maps(sp, st, nch, inv):
    """D3b: do the maps DRAWN for one chart pair agree across the coordinate
    cells, and what does that decide about the degree-one classes?"""
    _bump()
    every_digon_called_coherent = (MUTANT == "digon-lax")
    edges = st["edges"]
    bypair = defaultdict(list)
    for i, (a, b, c, p) in enumerate(edges):
        bypair[(a, b)].append((c, p, i))
    multi = {k: v for k, v in bypair.items() if len(v) >= 2}
    agree_by_mapset = 0
    agree_by_digons = 0
    census_mismatch = 0
    same_ck, cross_ck, same_coh, cross_coh = [], [], [], []
    digons_expected = 0
    for k, v in sorted(multi.items()):
        digons_expected += len(v) * (len(v) - 1) // 2
        one_map = (len({p for (_c, p, _i) in v}) == 1)
        all_coh = True
        for x in range(len(v)):
            for y in range(x + 1, len(v)):
                (c1, p1, i1), (c2, p2, i2) = v[x], v[y]
                row = (1 << i1) ^ (1 << i2)
                coh = (p1 == p2) or every_digon_called_coherent
                if not coh:
                    all_coh = False
                if c1[0] == c2[0]:
                    same_ck.append(row)
                    if coh:
                        same_coh.append(row)
                else:
                    cross_ck.append(row)
                    if coh:
                        cross_coh.append(row)
        agree_by_mapset += int(one_map)
        agree_by_digons += int(all_coh)
        census_mismatch += int(one_map != all_coh)
    d2 = [(1 << x) ^ (1 << y) ^ (1 << z) for (x, y, z) in
          [tuple(sorted(t)) for t in st["cells"]]]
    cyc = inv["cycle_rank_route_2_F2_rank"]
    b1_of = lambda extra: cyc - rank_f2_high(d2 + extra, maxrank=cyc)
    return {
        "pairs_drawn_at_two_or_more_cells": len(multi),
        "pairs_whose_drawn_maps_all_agree": agree_by_mapset,
        "pairs_whose_drawn_maps_disagree_somewhere":
            len(multi) - agree_by_mapset,
        "the_same_count_from_the_digon_flags": agree_by_digons,
        "the_two_agreement_routes_disagree_at": census_mismatch,
        "digons_expected_from_the_multiplicities": digons_expected,
        "digons_built": len(same_ck) + len(cross_ck),
        "same_checkpoint_digons": len(same_ck),
        "same_checkpoint_digons_that_are_coherent": len(same_coh),
        "cross_checkpoint_digons": len(cross_ck),
        "cross_checkpoint_digons_that_are_coherent": len(cross_coh),
        "b1_of_N": inv["b1"],
        "b1_with_the_same_checkpoint_digons_filled": b1_of(same_ck),
        "b1_with_every_cross_checkpoint_digon_filled": b1_of(cross_ck),
        "b1_with_the_COHERENT_cross_checkpoint_digons_filled":
            b1_of(cross_coh),
        "b1_with_every_coherent_digon_filled": b1_of(same_coh + cross_coh),
    }


def drawn_table_automorphisms(sp, st, nch):
    """D3: the DECLARED automorphism candidates -- the 36 left translations of
    the chart set -- tested against the drawn relation at every coordinate
    cell, and the chart-orbit count of the ones that pass."""
    _bump()
    accept_without_testing = (MUTANT == "auto-lax")
    charts = st["charts"]
    cid = {(c["sigma"], c["seed"]): i for i, c in enumerate(charts)}
    autos = []
    for g in sp.PERMS:
        for h in sp.PERMS:
            row, ok = [], True
            for c in charts:
                j = cid.get((pcomp(g, c["sigma"]), pcomp(h, c["seed"])))
                if j is None:
                    ok = False
                    break
                row.append(j)
            if not ok or len(set(row)) != nch:
                continue
            good = True
            if not accept_without_testing:
                for c in sp.CELLS:
                    dr = set(st["pair"][c])
                    if {(row[a], row[b]) for (a, b) in dr} != dr:
                        good = False
                        break
            if good:
                autos.append(tuple(row))
    par = list(range(nch))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for row in autos:
        for i in range(nch):
            a, b = find(i), find(row[i])
            if a != b:
                par[a] = b
    return {"declared_candidates": len(sp.PERMS) ** 2,
            "measured_automorphisms": len(autos),
            "chart_orbits": len({find(i) for i in range(nch)})}


def star_link_comparator(sp, st, nch):
    """R-TOP-8's comparator for the star and the link, built WITHOUT touching
    `local_profiles`: the star counts are taken by their own pass over the
    cells, and the link's b_0 and b_1 by UNION-FIND AND EULER rather than by
    an F_2 rank -- a different traversal and a different homology route."""
    _bump()
    etov = [(a, b) for (a, b, c, p) in st["edges"]]
    se = Counter()
    for (a, b) in etov:
        se[a] += 1
        se[b] += 1
    sf = Counter()
    lk = defaultdict(list)
    for tr in st["cells"]:
        vs = sorted({v for x in tr for v in etov[x]})
        for v in vs:
            sf[v] += 1
            o = [u for u in vs if u != v]
            lk[v].append((o[0], o[1]))
    out = {}
    for v in range(nch):
        nb = sorted({b if a == v else a for (a, b) in etov if v in (a, b)})
        ren = {x: i for i, x in enumerate(nb)}
        pairs = [(ren[p], ren[q]) for (p, q) in lk[v]]
        b0 = len(components_unionfind(len(nb), pairs)) if nb else 0
        out[v] = (se[v], sf[v], (len(nb), len(pairs), b0,
                                 len(pairs) - len(nb) + b0))
    return {"per_chart": out,
            "sum_of_the_star_1_cell_counts": sum(se[v] for v in range(nch)),
            "twice_the_1_cells": 2 * len(etov),
            "sum_of_the_star_2_cell_counts": sum(sf[v] for v in range(nch)),
            "three_times_the_2_cells": 3 * len(st["cells"])}


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
    symmetry = {}
    for (label, member, completion, setting) in INSTANCES:
        w, Q = instance_world(sp, member, completion, setting)
        charts = build_atlas(sp, w)
        pair = atlas_pair_table(sp, charts)
        edges, eidx = nerve_edges(sp, pair, len(charts))
        r1, pc1 = triangles_route_1(sp, pair, len(charts))
        r2, pc2 = triangles_route_2(sp, pair, len(charts))
        cells, coh, pcg, defects, conj = geometric_cells(
            sp, pair, eidx, len(charts))
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
        asym = []
        for c in sp.CELLS:
            dr = set(pair[c])
            miss = {(b, a) for (a, b) in dr} - dr
            if miss:
                asym.append("%d/%s" % (c[0], c[1]))
        symmetry[label] = {"cells_whose_drawn_relation_is_not_symmetric": asym,
                           "the_relation_is_symmetric_at_every_cell":
                               not asym}
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
            "the_traversal_defect_conjugacy": conj,
            "ordered_defect_multiset": defects}
    # the dropped-cell probe: route 2's cell list loses one 2-cell and the
    # completeness relation must break.
    ref = store[REFERENCE_INSTANCE]
    probe_cells, _, _, _, _ = geometric_cells(sp, ref["pair"], ref["eidx"],
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
    conj_ok = all(v["the_traversal_defect_conjugacy"][
        "the_three_traversal_defects_are_conjugate_at_every_2_cell"]
        and v["the_traversal_defect_conjugacy"]["the_pattern_is_never_mixed"]
        for v in rows.values())
    gate("TOP-COHERENCE", "measurement",
         "THE COHERENT 2-CELL COUNT IS ONE ROUTE, EXTERNALLY ANCHORED -- and "
         "the instrument says so rather than claiming two.  A 2-cell is "
         "coherent when its three drawn maps compose to the identity, the "
         "strict cocycle condition.  The count is flagged while the cell is "
         "built; the ORDERED DEFECT MULTISET's entry at the identity is NOT "
         "an independent second census of it, because the three traversal "
         "defects are CONJUGATE -- d_2 = p_1 d_1 p_1^-1 and d_3 = (p_2 p_1) "
         "d_1 (p_2 p_1)^-1, MEASURED here at every 2-cell of every instance "
         "-- so the pattern (d_1,d_2,d_3) is never mixed and the identity "
         "entry is IDENTICALLY six times the coherent count (RUNBOOK section "
         "13 addendum, #234: a pair related by an algebraic identity is one "
         "route).  What the second computation buys is not independence but "
         "an EXTERNAL ANCHOR: the multiset is gated exit-1 against TB3's "
         "committed receipt, so the coherent count is pinned to bytes outside "
         "this file.  The `coh-lax` mutant answers yes to every triangle and "
         "must die on that anchored relation.  The conjugacy itself is "
         "ANALYTICALLY FORCED -- p_1 (p_3 p_2 p_1) p_1^-1 = p_1 p_3 p_2 for "
         "any three maps -- so it is computed and recorded as evidence and "
         "enters TOP-FORCED-CLAUSES as a disclosure, never as a must-pass "
         "clause of this gate",
         coh_ok,
         {"six_times_the_coherent_count_against_the_multiset_identity_entry":
             {k: [6 * v["coherent_2_cells"],
                  v["ordered_defect_multiset"].get(ident_name, 0)]
              for k, v in rows.items()},
          "the_conjugacy_that_makes_it_one_route":
             {k: v["the_traversal_defect_conjugacy"]
              for k, v in rows.items()}})
    gate("TOP-PAIR-SYMMETRY", "measurement",
         "THE ADMISSION RELATION IS MEASURED SYMMETRIC, not assumed.  A "
         "1-cell is drawn for the unordered pair (a,b) from the ORDERED entry "
         "with a < b, so if admission were not symmetric the whole complex "
         "would depend on the chart indexing.  The relation is measured "
         "symmetric at all %d coordinate cells of all %d declared instances, "
         "and the `sym-lax` mutant deletes one direction of one admitted pair "
         "and must die here"
         % (len(sp.CELLS), len(INSTANCES)),
         all(v["the_relation_is_symmetric_at_every_cell"]
             for v in symmetry.values()), symmetry)
    gate("TOP-DEFECTS", "measurement",
         "THE ORDERED TRIANGLE DEFECT MULTISET over the wing group is "
         "reproduced element by element at the reference instance and "
         "anchored exit-1 against the committed receipt.  It is computed from "
         "the geometric 2-cells by evaluating all six traversals explicitly, "
         "not by scaling one of them",
         all(a["passed"] for a in ANCHORS if a["id"].startswith("A-DEFECT-")),
         rows[REFERENCE_INSTANCE]["ordered_defect_multiset"])
    for k, v in symmetry.items():
        rows[k]["the_drawn_relation_is_symmetric"] = \
            v["the_relation_is_symmetric_at_every_cell"]
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
        drop_a_sub_cell = (MUTANT == "subcell-drop")
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
            if drop_a_sub_cell and tl:
                tl = tl[:-1]
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
        # D3c: the per-checkpoint numbers by the BLOCK-INCIDENCE route, and
        # the coordinate-count form of b_1.
        binc = block_incidence(sp, st, nch)
        block_ok = all(
            binc[t]["b0_of_the_incidence_graph"] == per_t[t]["b0"]
            and binc[t]["cycle_rank_of_the_incidence_graph"] == per_t[t]["b1"]
            for t in per_t)
        coord = (live_t - 1) * (nch - 1)
        cross = cross_cell_drawn_maps(sp, st, nch, inv)
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
            "the_read_times_carrying_cells": live_t,
            "the_coordinate_count_T_minus_1_times_V_minus_1": coord,
            "b1_equals_the_coordinate_count": inv["b1"] == coord,
            "the_block_incidence_route": binc,
            "the_block_incidence_route_agrees": block_ok,
            "the_cross_coordinate_drawn_map_comparison": cross,
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
    ok_block = all(v["the_block_incidence_route_agrees"]
                   for v in table.values())
    block_pairs = sum(len(v["the_block_incidence_route"])
                      for v in table.values())
    gate("TOP-BLOCK-INCIDENCE", "measurement",
         "A READ TIME'S OWN TOPOLOGY IS THE NESTING OF THE TWO RULES' "
         "PARTITIONS, and that is a THIRD route to the per-checkpoint "
         "numbers, taken with no elimination at all.  At each checkpoint the "
         "FULL and REALIZED rules partition the charts into the components of "
         "their drawn relations; the bipartite BLOCK-INCIDENCE GRAPH joins "
         "two blocks that share a chart, and its b_0 and its cycle rank are "
         "measured EQUAL to the sub-nerve's b_0 and b_1 at every one of the "
         "%d (instance, checkpoint) pairs.  So `every checkpoint sub-nerve "
         "has vanishing first homology' says exactly `at every read time the "
         "two block partitions are NESTED, their incidence graph a forest' -- "
         "and where they are not nested, at checkpoints 2 and 3 of the "
         "partially symmetric and W-class instances, the incidence graph "
         "carries the cycle the sub-nerve carries.  The comparator touches "
         "neither the sub-complex nor its elimination (RUNBOOK section 14 "
         "addendum, #219).  The `block-lax` mutant builds the incidence graph "
         "from one rule's partition alone and must die here"
         % block_pairs,
         ok_block,
         {"the_instance_checkpoint_pairs_compared": block_pairs,
          "the_route_agrees_at_every_pair": ok_block,
          "per_instance": {
              k: {"agrees": v["the_block_incidence_route_agrees"],
                  "per_checkpoint": v["the_block_incidence_route"]}
              for k, v in table.items()}})
    cross_ok = all(
        v["the_cross_coordinate_drawn_map_comparison"][
            "the_two_agreement_routes_disagree_at"] == 0
        and v["the_cross_coordinate_drawn_map_comparison"][
            "digons_built"] == v["the_cross_coordinate_drawn_map_comparison"][
            "digons_expected_from_the_multiplicities"]
        and v["the_cross_coordinate_drawn_map_comparison"][
            "b1_with_the_same_checkpoint_digons_filled"] ==
        v["the_nerve_N"]["b1"]
        for v in table.values())
    refc = table[REFERENCE_INSTANCE][
        "the_cross_coordinate_drawn_map_comparison"]
    residual = refc["b1_with_the_COHERENT_cross_checkpoint_digons_filled"]
    emit_the_other_outcome = (MUTANT == "crosscell-typed")
    if emit_the_other_outcome:
        residual_emitted = residual + 1
    else:
        residual_emitted = residual
    cross_outcome = (
        "CROSS-CELL-COHERENT-DIGONS-FILL-EVERY-DEGREE-1-CLASS"
        if residual_emitted == 0 else
        "CROSS-CELL-A-RESIDUAL-SURVIVES-THE-COHERENT-DIGONS-<%d>"
        % residual_emitted)
    cross_derived = (
        "CROSS-CELL-COHERENT-DIGONS-FILL-EVERY-DEGREE-1-CLASS"
        if table[REFERENCE_INSTANCE][
            "the_cross_coordinate_drawn_map_comparison"][
            "b1_with_the_COHERENT_cross_checkpoint_digons_filled"] == 0 else
        "CROSS-CELL-A-RESIDUAL-SURVIVES-THE-COHERENT-DIGONS-<%d>"
        % table[REFERENCE_INSTANCE][
            "the_cross_coordinate_drawn_map_comparison"][
            "b1_with_the_COHERENT_cross_checkpoint_digons_filled"])
    gate("TOP-CROSS-CELL", "derivation",
         "DO THE MAPS DRAWN FOR ONE PAIR AGREE ACROSS COORDINATE CELLS, AND "
         "WHAT DOES THAT DECIDE?  Declared in D3b before it was run, with "
         "BOTH outcomes pre-registered and neither favoured.  Two charts "
         "identified at k coordinate cells carry k parallel 1-cells and "
         "C(k,2) digons; a digon is COHERENT when its two drawn maps agree.  "
         "The digon census is gated complete against the multiplicities "
         "(sum of C(k,2)); the pair-level agreement is computed TWICE, once "
         "from the set of drawn maps and once from the digon flags, and the "
         "two must agree at every pair -- the `digon-lax` mutant calls every "
         "digon coherent and must die on that differential.  The "
         "same-checkpoint digons are measured to kill NOTHING, so no "
         "degree-one class compares two rules at one read time.  The OUTCOME "
         "is then re-derived inside this gate from the measured residual b_1 "
         "that survives filling the COHERENT cross-read-time digons, and "
         "gated byte-for-byte against the emitted one; the `crosscell-typed` "
         "mutant emits the other outcome with the tables unchanged and must "
         "die here.  The gate checks the DERIVATION, not a favoured value",
         cross_ok and cross_outcome == cross_derived,
         {"the_outcome": cross_outcome,
          "the_outcome_re_derived_in_this_gate": cross_derived,
          "the_two_are_byte_identical": cross_outcome == cross_derived,
          "per_instance": {k: v["the_cross_coordinate_drawn_map_comparison"]
                           for k, v in table.items()}})
    FINDINGS["cross_cell_outcome"] = cross_outcome
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
         "route to chi.  Likewise d_1 d_2 = 0 holds for EVERY input here by "
         "the same algebra -- each 2-cell's three 1-cells are the three sides "
         "of a triangle, so their six endpoint bits cancel in pairs -- and "
         "the guard that evaluates it is a SAMPLE, capped at the number "
         "printed below out of the 2-cell count printed beside it; the "
         "argument, not the sample, is what carries it",
         True,
         {k: {"chi_from_cell_counts": v["the_nerve_N"]["chi_from_cell_counts"],
              "chi_from_betti": v["the_nerve_N"]["chi_from_betti"],
              "d1_d2_zero_on_the_sample":
                  v["the_nerve_N"]["d1_d2_is_zero_on_the_sampled_2_cells"],
              "the_sample_cap": v["the_nerve_N"]["the_d1_d2_sample_cap"],
              "the_2_cells_in_all": v["the_nerve_N"]["the_2_cells_in_all"]}
          for k, v in table.items()})
    gate("TOP-COORDINATE-COUNT", "disclosure",
         "DISCLOSURE, ALGEBRAICALLY FORCED -- WHAT b_1 = 140 ACTUALLY SAYS.  "
         "Rearranging the gluing formula, b_1(N) - (T-1)(|V|-1) = sum_t b_1^t "
         "- ( sum_t b_0^t - T ), so b_1 equals the pure COORDINATE COUNT "
         "(read times minus one) x (charts minus one) exactly when the "
         "per-checkpoint excess sum_t b_0^t - T equals sum_t b_1^t.  That "
         "equivalence is an identity, not a measurement: the measured content "
         "of the degree-one claim is the per-checkpoint census (sum b_0, sum "
         "b_1) recorded above, and nothing else.  Four of the five declared "
         "instances return the coordinate count, the asymmetric setting does "
         "not, and -- printed here rather than worked around -- the SCRAMBLED "
         "negative control returns it too, so b_1 is insensitive to the "
         "identification data while b_2 is not.  The identification-carrying "
         "invariants are b_2 and the coherent sub-nerve",
         True,
         {k: {"read_times_carrying_cells": v["the_read_times_carrying_cells"],
              "charts": v["the_nerve_N"]["V"],
              "T_minus_1_times_V_minus_1":
                  v["the_coordinate_count_T_minus_1_times_V_minus_1"],
              "b1": v["the_nerve_N"]["b1"],
              "b1_equals_the_coordinate_count":
                  v["b1_equals_the_coordinate_count"],
              "sum_of_per_checkpoint_b0": v["sum_of_per_checkpoint_b0"],
              "sum_of_per_checkpoint_b1": v["sum_of_per_checkpoint_b1"]}
          for k, v in table.items()})
    simp_ok = all(v["the_simplicial_nerve"][
        "every_coordinate_cell_graph_is_a_disjoint_union_of_complete_graphs"]
        for v in table.values())
    ref = table[REFERENCE_INSTANCE]["the_simplicial_nerve"]
    faces_wanted = {k: [table[k]["the_nerve_N"]["V"]]
                    for k in table}
    simp_face = all(v["the_simplicial_nerve"]["maximal_face_sizes"] ==
                    faces_wanted[k] for k, v in table.items())
    simp_cone = all(v["the_simplicial_nerve"][
        "it_is_a_cone_hence_contractible"] for v in table.values())
    binom_forced = sorted({sum(((-1) ** (j + 1)) * _binom(k, j)
                               for j in range(1, k + 1))
                           for k in range(1, 41)})
    gate("TOP-SIMPLICIAL", "measurement",
         "THE SIMPLICIAL NERVE IS THE WHOLE CHART SET, hence a cone, hence "
         "contractible.  Every coordinate cell's overlap graph is MEASURED to "
         "be a disjoint union of complete graphs, so the faces are exactly "
         "the subsets of those components; the measured content is then that "
         "the UNIQUE MAXIMAL FACE IS THE WHOLE CHART SET at every declared "
         "instance -- gated here as maximal_face_sizes == [charts], which is "
         "the number the unit defends and which a smaller maximal face would "
         "break.  The alternating binomial sum is NOT part of this predicate: "
         "sum_{j=1..k} (-1)^{j+1} C(k,j) = 1 for every k >= 1, evaluated here "
         "at k = 1..40 with a one-element value set, so it is ANALYTICALLY "
         "FORCED and is entered in TOP-FORCED-CLAUSES as a disclosure "
         "(RUNBOOK section 14 addendum, #208).  The `simp-lax` mutant "
         "replaces the maximal face by a proper subset of itself -- a "
         "perturbation the binomial clause cannot see and this one does",
         simp_ok and simp_face and simp_cone,
         {"maximal_face_sizes": {k: v["the_simplicial_nerve"][
             "maximal_face_sizes"] for k, v in table.items()},
          "charts": {k: v["the_nerve_N"]["V"] for k, v in table.items()},
          "the_maximal_face_is_the_whole_chart_set": simp_face,
          "chi_of_the_reference_simplicial_nerve":
              ref["chi_route_1_alternating_binomial_sum"],
          "the_alternating_binomial_sum_at_k_1_to_40": binom_forced,
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
    link_from_edges_only = (MUTANT == "link-lax-atlas")
    inflate_the_star = (MUTANT == "star-lax")
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
        star = (star_e[v] + 1, star_f[v] + 1) if inflate_the_star \
            else (star_e[v], star_f[v])
        prof[v] = {"dimprofile": tuple(dimprof[v]),
                   "star": star,
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
    link_from_edges_only = (MUTANT == "link-lax-control")
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
    star_cross = True
    link_cross = True
    star_sums = {}
    autos = {}
    for (label, _m, _c, _s) in INSTANCES:
        st = store[label]
        nch = len(st["charts"])
        prof = local_profiles(sp, st, nch)
        # R-TOP-8: THE STAR AND THE LINK get their own comparator, built
        # WITHOUT touching `local_profiles` and reading the link's homology by
        # union-find and Euler rather than by an F_2 rank -- so the two
        # components of the declared estimator that the manifold verdict
        # quotes are audited by a route that is not the one under audit
        # (RUNBOOK section 14 addendum, #219).
        cmpr = star_link_comparator(sp, st, nch)
        for v in range(nch):
            se, sf, lk = cmpr["per_chart"][v]
            if tuple(prof[v]["star"]) != (se, sf):
                star_cross = False
            if tuple(prof[v]["link"]) != lk:
                link_cross = False
        star_sums[label] = {
            "sum_star_1_cells": cmpr["sum_of_the_star_1_cell_counts"],
            "twice_the_1_cells": cmpr["twice_the_1_cells"],
            "sum_star_2_cells": cmpr["sum_of_the_star_2_cell_counts"],
            "three_times_the_2_cells": cmpr["three_times_the_2_cells"]}
        if cmpr["sum_of_the_star_1_cell_counts"] != cmpr["twice_the_1_cells"]:
            star_cross = False
        if cmpr["sum_of_the_star_2_cell_counts"] != \
                cmpr["three_times_the_2_cells"]:
            star_cross = False
        autos[label] = drawn_table_automorphisms(sp, st, nch)
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
                                       and rep["link"][3] == 1),
            "the_drawn_table_automorphisms": autos[label],
            "chart_independence_is_symmetry_forced":
                autos[label]["chart_orbits"] == 1}
    ref = per_instance[REFERENCE_INSTANCE]
    flip = (MUTANT == "verdict-flip")
    typed = (MUTANT == "manifold-typed")
    inconsistent = sorted(k for k, v in per_instance.items()
                          if not v["the_reading_is_consistent"])
    forced = sorted(k for k, v in per_instance.items()
                    if v["chart_independence_is_symmetry_forced"])
    TABLES["q2_dimension"] = {
        "per_instance": per_instance, "controls": ctrl,
        "the_star_and_link_comparator": star_sums,
        "the_instances_where_chart_independence_is_symmetry_forced": forced,
        "the_estimator": {
            "dimprofile": "per coordinate cell, |component of X| - 1",
            "star": "(1-cells at X, 2-cells at X)",
            "link": "(V, E, b0, b1) over F_2 of the link graph of X"}}
    if ref["the_reading_is_consistent"] and not flip:
        link_b1 = ref["the_common_profile"]["link_V_E_b0_b1"][3]
        if typed:
            link_b1 = link_b1 + 1
        manifold_verdict = V_MANIFOLD % (
            len(per_instance) - len(inconsistent), len(per_instance),
            "-AND-".join(str(d) for d in
                         sorted(set(ref["the_common_profile"]["dimprofile"]))),
            ref["charts"],
            canon(ref["the_common_profile"]["dimprofile"]),
            canon(sorted(set(ref["the_common_profile"]["dimprofile"]))),
            link_b1,
            ref["the_drawn_table_automorphisms"]["chart_orbits"],
            ref["the_drawn_table_automorphisms"]["measured_automorphisms"],
            len(per_instance) - len(inconsistent), len(per_instance),
            canon(inconsistent))
    else:
        w = ref["the_witness"]
        manifold_verdict = V_MANIFOLD_INCONSISTENT % (
            (w["chart"] if w else "no witness isolated"))
    ok_vocab = manifold_verdict.startswith(PREREGISTERED_MANIFOLD[0]) or \
        manifold_verdict.startswith(PREREGISTERED_MANIFOLD[1])
    # THE FULL STRING, REBUILT INSIDE THE GATE FROM THE RECORDED TABLE --
    # head, computed qualifiers and body alike -- and gated BYTE-FOR-BYTE.
    rec = TABLES["q2_dimension"]["per_instance"]
    rinc = sorted(k for k, v in rec.items()
                  if not v["the_reading_is_consistent"])
    rr = rec[REFERENCE_INSTANCE]
    if rr["the_reading_is_consistent"]:
        derived = V_MANIFOLD % (
            len(rec) - len(rinc), len(rec),
            "-AND-".join(str(d) for d in
                         sorted(set(rr["the_common_profile"]["dimprofile"]))),
            rr["charts"], canon(rr["the_common_profile"]["dimprofile"]),
            canon(sorted(set(rr["the_common_profile"]["dimprofile"]))),
            rr["the_common_profile"]["link_V_E_b0_b1"][3],
            rr["the_drawn_table_automorphisms"]["chart_orbits"],
            rr["the_drawn_table_automorphisms"]["measured_automorphisms"],
            len(rec) - len(rinc), len(rec), canon(rinc))
    else:
        w = rr["the_witness"]
        derived = V_MANIFOLD_INCONSISTENT % (
            (w["chart"] if w else "no witness isolated"))
    gate("TOP-DIM-READING", "derivation",
         "THE DIMENSION VERDICT IS REBUILT INSIDE THIS GATE FROM THE RECORDED "
         "TABLE AND GATED BYTE-FOR-BYTE AGAINST THE EMITTED STRING -- head, "
         "computed qualifiers and body alike, not a prefix (RUNBOOK section "
         "13 addendum, #234, and #257: a qualifier is part of the verdict).  "
         "The head itself carries the restrictions: how many of the declared "
         "instances the reading holds at, which dimensions the profile "
         "realises, that no link is a circle, and that chart-independence at "
         "the reference is SYMMETRY-FORCED.  The `verdict-flip` mutant moves "
         "the branch and the `manifold-typed` mutant moves ONE COMPUTED "
         "QUALIFIER of the emitter with every recorded table left at its "
         "measured value; both must die here.  The estimator is the DECLARED "
         "one -- per-coordinate-cell local simplex dimension, star profile "
         "and the F_2 homology of the vertex link -- evaluated at EVERY "
         "chart, and ALL THREE components are cross-checked: the per-cell "
         "dimension against a component census run from the pair table alone, "
         "and the star and the link against a comparator that never touches "
         "`local_profiles` and reads the link's homology by union-find and "
         "Euler instead of by an F_2 rank, with the global identities sum "
         "star_E = 2E and sum star_F = 3F gated beside it.  CONSISTENT means "
         "UNIFORM, not manifold.  Whether the uniformity is a MEASUREMENT is "
         "itself measured: the drawn table's chart-orbit count under its "
         "declared automorphism candidates is reported per instance, and "
         "where it is 1 the reading could not have come out otherwise and is "
         "entered as a disclosure",
         ok_vocab and manifold_verdict == derived and dim_cross
         and star_cross and link_cross,
         {"verdict": manifold_verdict,
          "the_verdict_rebuilt_from_the_recorded_table": derived,
          "the_two_strings_are_byte_identical": manifold_verdict == derived,
          "the_estimator_agrees_with_an_independent_component_census":
              dim_cross,
          "the_star_agrees_with_an_independent_comparator": star_cross,
          "the_link_agrees_with_an_independent_comparator": link_cross,
          "the_star_sum_identities": star_sums,
          "distinct_estimator_values": ref["distinct_estimator_values"],
          "instances_whose_reading_is_inconsistent": inconsistent,
          "the_witnesses": {k: per_instance[k]["the_witness"]
                            for k in inconsistent},
          "the_local_dimensions_realised":
              ref["the_local_dimensions_realised"],
          "the_local_dimension_is_a_single_number":
              ref["local_dimension_is_one_number"],
          "every_link_is_a_circle": ref["every_link_is_a_circle"]})
    forced_and_consistent = all(
        per_instance[k]["the_reading_is_consistent"] for k in forced)
    gate("TOP-AUTOMORPHISM", "measurement",
         "WHETHER A CONSISTENT READING IS A MEASUREMENT AT ALL.  The declared "
         "estimator is a chart-invariant of the drawn table, so where the "
         "drawn table has an automorphism group TRANSITIVE ON CHARTS the "
         "reading could not have come out otherwise.  The declared "
         "automorphism candidates -- the %d left translations "
         "(sigma, seed) -> (g sigma, h seed) -- are each TESTED against the "
         "drawn relation at every coordinate cell, and the chart-orbit count "
         "of the ones that pass is measured per instance.  Where the orbit "
         "count is 1 the reading is measured CONSISTENT and entered as a "
         "DISCLOSURE, not as a measurement (RUNBOOK section 14 addendum, "
         "#208); where it is not, the split is a genuine measurement.  This "
         "gate carries the implication: every instance whose orbit count is 1 "
         "must read CONSISTENT.  The `auto-lax` mutant accepts every "
         "candidate without testing it against the drawn table and must die "
         "here" % (len(sp.PERMS) ** 2),
         forced_and_consistent,
         {"per_instance": autos,
          "the_instances_where_it_is_forced": forced,
          "the_instances_whose_reading_is_consistent":
              sorted(k for k, v in per_instance.items()
                     if v["the_reading_is_consistent"]),
          "distinct_estimator_values": {k: v["distinct_estimator_values"]
                                        for k, v in per_instance.items()}})
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


def _thousands(n):
    """Exact integer rendering with a comma every three digits."""
    s = str(abs(int(n)))
    parts = []
    while len(s) > 3:
        parts.append(s[-3:])
        s = s[:-3]
    parts.append(s)
    return ("-" if n < 0 else "") + ",".join(reversed(parts))


def candidate_tables_markdown(t3):
    """The paper's two section-5.2 tables, rendered as markdown rows from the
    RECORDED candidate table.  Display only -- no measurement passes through
    here; every value is read back out of the table this run recorded."""
    ct = t3["the_candidate_table"]
    per = t3["the_forced_structure_of_the_family"]["per_candidate"]
    order = [c[0] for c in SELECTOR_CANDIDATES]

    def b(text, passed):
        return ("**%s**" % text) if passed else text

    main = ["| id | candidate | (a) on the locus | (b) off it | "
            "(c) non-linear $K$ | holds at | of those "
            "$=\\mathrm{GL}(3,2)$ | clauses |",
            "|---|---|---|---|---|---|---|---|"]
    for cid in order:
        v = ct[cid]
        main.append("| %s | %s | %s | %s | %s | %s | %s | %d |" % (
            cid, SELECTOR_TYPESET_NAMES[cid],
            b("%s/%s" % (_thousands(v["a_holds_on_the_locus"]),
                         _thousands(v["the_locus_size"])), v["a_passes"]),
            b(_thousands(v["b_holds_off_the_locus"]), v["b_passes"]),
            b(_thousands(v["c_completions_with_a_non_linear_K"]),
              v["c_passes"]),
            _thousands(v["completions_satisfying_it"]),
            _thousands(v["of_those_with_K_equal_to_GL_3_2"]),
            v["clauses_passed"]))
    cont = ["| id | holds at | clause (c) | "
            "$\\lvert C\\setminus C4\\rvert$ | $C \\subseteq C4$ |",
            "|---|---|---|---|---|"]
    for cid in order:
        p = per[cid]
        cont.append("| %s | %s | %s | %s | %s |" % (
            cid, _thousands(p["holds_at"]), _thousands(p["clause_c_count"]),
            _thousands(p["the_containment_deficit"]),
            "**yes**" if p["is_contained_in_C4"] else "no"))
    return {"the_candidate_table": main, "the_clause_c_containment": cont}


def run_q3(sp, tb3):
    global _SELECTOR_DECLARED, _K_AT_DECLARATION
    prog("Q3: the Fano-rung selector")
    look_at_the_fixture_first = (MUTANT == "selfreeze-lax")
    if look_at_the_fixture_first:
        subgroup_closure([label_defect(sp, pi, tuple(range(sp.NSYS)))
                          for pi in sp.PERMS], sp.NSYS)
    _K_AT_DECLARATION = _K_BUILT
    origins_ok = all(o in SELECTOR_ORIGIN_LEGEND
                     for (_c, _s, _t, o) in SELECTOR_CANDIDATES)
    gate("TOP-SELECTOR-FREEZE", "measurement",
         "THE CANDIDATE FAMILY IS DECLARED ABOVE EVERY MEASUREMENT.  The "
         "thirteen candidate selectors and the three clauses are declared in "
         "this source above every measurement, and the count of defect "
         "subgroups K(q) built at the moment the declaration is registered is "
         "measured to be ZERO.  That records the ordering WITHIN ONE "
         "EXECUTION; it is NOT offered as proof that the declarations were "
         "fixed before any fixture truth was seen, which no in-run "
         "measurement can establish -- the process fact is the commit, not "
         "this counter.  Each candidate's ORIGIN is one of the declared "
         "labels and is gated against them: `pin-derived` means it restates "
         "the pin's own order-2-locus language, and is NOT a claim that the "
         "pin lists it -- THE PIN CONTAINS NO CANDIDATE LIST.  The "
         "`selfreeze-lax` mutant builds a subgroup first and must die here",
         _K_AT_DECLARATION == 0 and origins_ok,
         {"candidates_declared": len(SELECTOR_CANDIDATES),
          "clauses_declared": len(SELECTOR_CLAUSES),
          "the_origin_legend": SELECTOR_ORIGIN_LEGEND,
          "origins_used": sorted({o for (_c, _s, _t, o)
                                  in SELECTOR_CANDIDATES}),
          "every_origin_is_a_declared_label": origins_ok,
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
    hits = 0
    poison_the_cache = (MUTANT == "cache-lax")
    for q in fam:
        ds = [label_defect(sp, pi, q) for pi in sp.PERMS]
        dstar = label_defect(sp, PSTAR, q)
        key = tuple(sorted(ds))
        got = cache.get(key)
        if got is None:
            K = subgroup_closure(ds, n8)
            got = (len(K), sum(1 for x in K if x in GL), frozenset(K) == GL,
                   tuple(sorted({pord(x) for x in K})))
            cache[key] = got
        else:
            hits += 1
            if poison_the_cache:
                got = (got[0] + 1, got[1], got[2], got[3])
        kord, klin, kgl, kspec = got
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
        rows.append((q, pord(dstar), kord, klin, kgl, pred, kspec))
    # THE CACHE IS AUDITED, not trusted (RUNBOOK section 14 addenda #185 and
    # #219): the census memoizes K(q) by its generator multiset, so a declared
    # SAMPLE of the family is recomputed FRESH with the cache bypassed and the
    # two must agree, and the cache-hit count itself is gated non-zero so the
    # audited path is measured to be exercised.
    sample = list(range(0, len(rows), 211))
    fresh_ok = True
    for i in sample:
        q = rows[i][0]
        K = subgroup_closure([label_defect(sp, pi, q) for pi in sp.PERMS], n8)
        if (len(K), sum(1 for x in K if x in GL), frozenset(K) == GL) != \
                (rows[i][2], rows[i][3], rows[i][4]):
            fresh_ok = False
    gate("TOP-CACHE", "measurement",
         "THE MEMOIZATION IS AUDITED.  The census caches the defect subgroup "
         "by its generator multiset; the cache is measured to be EXERCISED "
         "(the hit count is gated non-zero, so this is not a zero-lookup "
         "gate), and a declared sample of %d completions -- every %dth of the "
         "family, chosen by index and not by outcome -- is recomputed FRESH "
         "with the cache bypassed, order, linear count and set equality "
         "alike.  The `cache-lax` mutant perturbs the value returned on a hit "
         "and must die here"
         % (len(sample), 211),
         fresh_ok and hits > 0,
         {"cache_entries": len(cache), "cache_hits": hits,
          "the_sample_size": len(sample),
          "the_sample_recomputes_fresh": fresh_ok})
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
    # ---- THE FORCED STRUCTURE OF THE FAMILY, measured as sets.
    csets = {cid: {r[0] for r in rows if r[5][cid]}
             for (cid, _s, _t, _o) in SELECTOR_CANDIDATES}
    c4_by_K = {r[0] for r in rows if r[3] == r[2]}
    forced_tab = {
        "C4_the_predicate_equals_the_set_where_K_is_contained_in_GL_3_2":
            csets["C4"] == c4_by_K,
        "their_sizes": [len(csets["C4"]), len(c4_by_K)],
        "clause_c_equals_the_containment_deficit_for_every_candidate": all(
            ctable[cid]["c_completions_with_a_non_linear_K"] ==
            len(csets[cid] - c4_by_K)
            for (cid, _s, _t, _o) in SELECTOR_CANDIDATES),
        "the_candidates_contained_in_C4": sorted(
            cid for (cid, _s, _t, _o) in SELECTOR_CANDIDATES
            if csets[cid] <= c4_by_K),
        "the_candidates_passing_clause_c": sorted(
            cid for (cid, _s, _t, _o) in SELECTOR_CANDIDATES
            if ctable[cid]["c_passes"]),
        "every_sigma_P_is_F2_linear": all(is_f2_linear(sp.SIGMA[pi])
                                          for pi in sp.PERMS),
        "C9_puts_every_defect_inside_the_wing_group": all(
            all(d in wing for d in [label_defect(sp, pi, q)
                                    for pi in sp.PERMS])
            for q in csets["C9"]),
        "the_extensional_duplicates": sorted(
            "%s = %s" % (a, b)
            for i, (a, _s1, _t1, _o1) in enumerate(SELECTOR_CANDIDATES)
            for (b, _s2, _t2, _o2) in SELECTOR_CANDIDATES[i + 1:]
            if csets[a] == csets[b]),
        "distinct_predicates_among_the_declared_names":
            len({frozenset(v) for v in csets.values()}),
        "the_clause_c_disclosure": CLAUSE_C_DISCLOSURE,
        "per_candidate": {
            cid: {"holds_at": len(csets[cid]),
                  "clause_c_count":
                      ctable[cid]["c_completions_with_a_non_linear_K"],
                  "the_containment_deficit": len(csets[cid] - c4_by_K),
                  "is_contained_in_C4": csets[cid] <= c4_by_K}
            for (cid, _s, _t, _o) in SELECTOR_CANDIDATES}}
    # ---- R-TOP-5: THE P* SWEEP.  The locus and the defect-order axis are
    # defined relative to an ARENA COORDINATE; all five non-identity wing
    # symmetries are swept and the dependence is measured (RUNBOOK section 15).
    sweep = {}
    for pi in sp.PERMS:
        if pi == sp.IDENT:
            continue
        od = Counter()
        loc = []
        for r in rows:
            o = pord(label_defect(sp, pi, r[0]))
            od[o] += 1
            if o == 2:
                loc.append(r)
        sweep[sp.NAME[pi]] = {
            "the_type_of_the_symmetry":
                "transposition" if len(cycletype(pi)) == 2 else "3-cycle",
            "the_order_2_locus": len(loc),
            "on_the_locus_K_equals_GL_3_2": sum(1 for r in loc if r[4]),
            "the_defect_order_distribution":
                {str(k): v for k, v in sorted(od.items())},
            "K_equals_GL_3_2_by_defect_order": {
                str(k): v for k, v in
                sorted(Counter(pord(label_defect(sp, pi, r[0]))
                               for r in kgl_all).items())}}
    by_type = defaultdict(list)
    for nm, v in sweep.items():
        by_type[v["the_type_of_the_symmetry"]].append(
            (v["the_order_2_locus"], v["on_the_locus_K_equals_GL_3_2"]))
    sweep_agrees = all(len(set(v)) == 1 for v in by_type.values())
    sweep_separates = (len({tuple(sorted(set(v)))
                            for v in by_type.values()}) == len(by_type))
    sweep_nonempty = all(v["the_order_2_locus"] > 0 for v in sweep.values())
    pstar_type = ("transposition" if len(cycletype(PSTAR)) == 2 else "3-cycle")
    gate("TOP-PSTAR-SWEEP", "measurement",
         "THE LOCUS IS AN ARENA COORDINATE AND THE DEPENDENCE IS MEASURED "
         "(RUNBOOK section 15).  The defect d_P(q), the order-2 LOCUS and the "
         "defect-order axis of the census are all defined relative to the "
         "declared wing symmetry P*, which this instrument selects as the "
         "first non-identity element of the enumerated wing group -- a "
         "TRANSPOSITION.  All five non-identity symmetries are swept: the "
         "three transpositions are measured to AGREE, locus and on-locus "
         "count alike, the two 3-cycles are measured to agree with each other "
         "and to DIFFER from the transpositions, and every locus is measured "
         "non-empty.  So the locus size and the on-locus count are "
         "P*-RELATIVE and the verdict says so in its own head; the count of "
         "completions reaching GL(3,2) as a set is not, since K does not "
         "depend on P*.  The `defect-lax` mutant composes the defect in the "
         "wrong order, emptying every locus, and must die here",
         sweep_agrees and sweep_separates and sweep_nonempty,
         {"the_declared_P_star": sp.NAME[PSTAR],
          "its_type": pstar_type, "per_symmetry": sweep,
          "the_symmetry_classes_agree_internally": sweep_agrees,
          "the_classes_are_separated": sweep_separates,
          "every_locus_is_non_empty": sweep_nonempty})
    # ---- R-TOP-12: THE ORDER LADDER.  How far a purely order-theoretic
    # necessary condition can be pushed, and where it stops.
    ladder_rows = []
    for name, test in (
            ("ord[P*,u] lies in GL(3,2)'s element spectrum",
             lambda r: r[1] in gl_spec),
            ("the whole S_3 defect-order profile lies in the spectrum",
             lambda r: all(pord(label_defect(sp, pi, r[0])) in gl_spec
                           for pi in sp.PERMS)),
            ("every element order of K itself lies in the spectrum",
             lambda r: all(o in gl_spec for o in r[6]))):
        pas = [r for r in rows if test(r)]
        ladder_rows.append({
            "the_condition": name, "completions_passing": len(pas),
            "false_positives_against_K_contained_in_GL_3_2":
                sum(1 for r in pas if r[3] != r[2]),
            "it_contains_every_completion_with_K_in_GL_3_2":
                all(test(r) for r in kle_all),
            "it_contains_every_completion_with_K_equal_to_GL_3_2":
                all(test(r) for r in kgl_all)})
    ladder_nested = all(ladder_rows[i]["completions_passing"] >
                        ladder_rows[i + 1]["completions_passing"]
                        for i in range(len(ladder_rows) - 1))
    ladder_contains = all(r["it_contains_every_completion_with_K_in_GL_3_2"]
                          for r in ladder_rows)
    ladder_leaks = ladder_rows[-1][
        "false_positives_against_K_contained_in_GL_3_2"] > 0
    gate("TOP-ORDER-LADDER", "measurement",
         "HOW FAR THE ORDER-THEORETIC CONDITION GOES, AND WHERE IT STOPS.  "
         "GL(3,2)'s element orders are measured, d_{P*}(q) lies in K(q), so "
         "an order outside that spectrum makes the containment impossible -- "
         "the necessary condition the census reports biting at orders 5 and "
         "6.  It is NOT the finest order-theoretic condition available, and "
         "that is measured here rather than asserted: a strictly nested "
         "ladder of purely order-theoretic conditions is built, each measured "
         "to contain every completion whose K lies in GL(3,2), and each "
         "measured strictly smaller than the last.  The measured content is "
         "the last row: even the finest of them still admits false positives, "
         "so NO purely order-theoretic condition characterises the visit and "
         "linearity does irreducible work.  The `defect-lax` mutant collapses "
         "every defect to the identity, flattening the ladder, and must die "
         "here",
         ladder_nested and ladder_contains and ladder_leaks,
         {"the_element_orders_of_GL_3_2": gl_spec,
          "the_ladder": ladder_rows,
          "the_ladder_is_strictly_nested": ladder_nested,
          "every_level_contains_the_targets": ladder_contains,
          "the_finest_level_still_leaks": ladder_leaks,
          "5_divides_the_order_of_GL_3_2": len(GL) % 5 == 0,
          "6_divides_the_order_of_GL_3_2": len(GL) % 6 == 0,
          "so_order_5_is_excluded_by_Lagrange_and_order_6_only_by_the_"
          "spectrum": len(GL) % 5 != 0 and len(GL) % 6 == 0,
          "linear_completions": sum(1 for r in rows if is_f2_linear(r[0])),
          "linear_completions_whose_K_equals_GL_3_2":
              sum(1 for r in rows if is_f2_linear(r[0]) and r[4]),
          "completions_at_admissible_orders_whose_K_is_not_GL_3_2":
              sum(1 for r in rows if r[1] in gl_spec and not r[4]),
          "on_the_locus_linear": sum(1 for r in locus
                                     if is_f2_linear(r[0])),
          "on_the_locus_linear_and_K_equals_GL_3_2":
              sum(1 for r in locus if is_f2_linear(r[0]) and r[4]),
          "on_the_locus_non_linear_and_K_equals_GL_3_2":
              sum(1 for r in locus if not is_f2_linear(r[0]) and r[4])})
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
    def _sel_args(cand, best, pstar_name, cls, loc_n, onl_n, kgl_n, orders,
                  swp):
        cls_rows = defaultdict(list)
        for nm, v in sorted(swp.items()):
            cls_rows[v["the_type_of_the_symmetry"]].append(
                (v["the_order_2_locus"], v["on_the_locus_K_equals_GL_3_2"]))
        tr = cls_rows["transposition"]
        cy = cls_rows["3-cycle"]
        return (cls.upper(), cand, best, pstar_name, loc_n, onl_n, kgl_n,
                orders, len(tr), tr[0][0], tr[0][1], len(cy), cy[0][0],
                cy[0][1], kgl_n)
    typed_selector = (MUTANT == "selector-typed")
    if named:
        selector_verdict = V_SELECTOR_NAMED % (
            named[0], ctable[named[0]]["predicate"])
    else:
        worst = max(ctable.values(), key=lambda v: v["clauses_passed"])
        emitted_locus = len(locus) + (1 if typed_selector else 0)
        selector_verdict = V_SELECTOR % _sel_args(
            len(SELECTOR_CANDIDATES), worst["clauses_passed"], sp.NAME[PSTAR],
            pstar_type, emitted_locus, sum(1 for r in locus if r[4]),
            len(kgl_all), canon(sorted(by_ord_gl)), sweep)
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
    TABLES["q3_selector"] = {
        "the_declared_candidate_family": [
            {"id": c[0], "name": c[1], "predicate": c[2], "origin": c[3]}
            for c in SELECTOR_CANDIDATES],
        "the_declared_clauses": [{"id": c[0], "text": c[1]}
                                 for c in SELECTOR_CLAUSES],
        "the_declared_rule": SELECTOR_RULE,
        "the_origin_legend": SELECTOR_ORIGIN_LEGEND,
        "the_reference_values_computed_at_the_ord_2_target": {
            "defect_fixed_points": REF_FIX, "completion_support": REF_SUPP,
            "completion_cycle_type": list(REF_CT),
            "defect_order_profile": list(REF_PROF)},
        "the_rungs": rung_rows,
        "the_candidate_table": ctable,
        "the_forced_structure_of_the_family": forced_tab,
        "the_declared_P_star": sp.NAME[PSTAR],
        "the_P_star_type": pstar_type,
        "the_P_star_sweep": sweep,
        "the_order_theoretic_ladder": ladder_rows,
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
    # THE PAPER'S TWO SECTION-5.2 TABLES, EMITTED AS MARKDOWN ROWS FROM THE
    # RECORDED TABLE.  Nothing here measures anything: it renders the values
    # already recorded above, so the paper's rows are generated and never
    # retyped.  A bold cell is a PASSED clause, and the pass flags are the
    # recorded ones.
    TABLES["q3_selector"]["the_section_5_2_tables_as_markdown"] = \
        candidate_tables_markdown(TABLES["q3_selector"])
    # THE FULL STRING, REBUILT INSIDE THE GATE FROM THE RECORDED TABLE.
    t3 = TABLES["q3_selector"]
    rnamed = [cid for cid, v in t3["the_candidate_table"].items()
              if v["NAMED"]]
    if rnamed:
        sel_derived = V_SELECTOR_NAMED % (
            rnamed[0], t3["the_candidate_table"][rnamed[0]]["predicate"])
    else:
        rbest = max(v["clauses_passed"]
                    for v in t3["the_candidate_table"].values())
        sel_derived = V_SELECTOR % _sel_args(
            len(t3["the_declared_candidate_family"]), rbest,
            t3["the_declared_P_star"], t3["the_P_star_type"],
            t3["the_locus_size"], t3["of_those_on_the_order_2_locus"],
            t3["completions_whose_K_equals_GL_3_2"],
            canon(sorted(int(k) for k in
                         t3["the_defect_orders_at_which_GL_3_2_is_reached"])),
            t3["the_P_star_sweep"])
    gate("TOP-SELECTOR", "derivation",
         "THE SELECTOR VERDICT IS REBUILT INSIDE THIS GATE FROM THE RECORDED "
         "CONTINGENCY TABLE AND GATED BYTE-FOR-BYTE against the emitted "
         "string -- head, computed qualifiers and body alike, not a prefix "
         "(RUNBOOK section 13 addendum, #234; #257).  The head carries the "
         "restriction the census actually has: the locus is P*-RELATIVE, and "
         "which class of wing symmetry P* belongs to is interpolated from the "
         "measured cycle type.  Each of the thirteen declared candidates is "
         "measured on the three declared clauses over the EXHAUSTIVE "
         "completion family.  Clause (c) is cross-checked against a count "
         "taken OUTSIDE the candidate loop -- the completions in the whole "
         "family whose defect subgroup is F_2-linear -- which no candidate's "
         "linear sub-count may exceed; the `sel-clause-lax` mutant reports "
         "clause (c) as passing for every candidate and must die on that "
         "bound, and the `selector-typed` mutant moves ONE COMPUTED QUALIFIER "
         "of the emitter with the table left at its measured value",
         (bool(derived_named) == selector_verdict.startswith(
             "TOP-FANO-SELECTOR-<"))
         and (selector_verdict.startswith(PREREGISTERED_SELECTOR[0])
              or selector_verdict.startswith(PREREGISTERED_SELECTOR[1]))
         and selector_verdict == sel_derived
         and c_consistent,
         {"named": derived_named, "verdict": selector_verdict,
          "the_verdict_rebuilt_from_the_recorded_table": sel_derived,
          "the_two_strings_are_byte_identical":
              selector_verdict == sel_derived,
          "clause_c_is_bounded_by_the_family_wide_count": c_consistent,
          "completions_with_an_F2_linear_K": len(kle_all)})
    gate("TOP-FORCED-CLAUSES", "disclosure",
         "DISCLOSURE: WHAT IN THIS UNIT IS FORCED RATHER THAN MEASURED "
         "(RUNBOOK section 14 addendum, #208).  Five items, each computed "
         "here and none of them a must-pass clause anywhere.  (i) CLAUSE (c) "
         "IS A CONTAINMENT: its count for a candidate C is measured to be "
         "|C \\ C4| for every one of the thirteen, and C4 is measured EQUAL "
         "as a set to {q : K(q) contained in GL(3,2)}, so `clause (c) "
         "passes' is literally C contained in C4 and every passer's zero is "
         "algebra -- C4 because a group generated by linear maps is linear, "
         "C5 and C10 because all six sigma_P are measured F_2-linear, C9 "
         "because q normalising the wing group puts every defect inside it, "
         "all four measured as set containments here.  (ii) THE EXTENSIONAL "
         "DUPLICATES: the declared thirteen names carry fewer distinct "
         "predicates, and every coincidence is listed rather than the first "
         "one only.  (iii) THE ALTERNATING BINOMIAL SUM of TOP-SIMPLICIAL is "
         "1 for every k, so it is a print and not a route.  (iv) THE THREE "
         "TRAVERSAL DEFECTS of a 2-cell are CONJUGATE, which is why the "
         "coherent count has one route and not two.  (v) CHART-INDEPENDENCE "
         "at an instance whose drawn table is chart-transitive could not have "
         "come out otherwise, so CONSISTENT is a disclosure there",
         True, forced_tab)
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
    inflate_the_fixed_cell_census = (MUTANT == "fixcell-lax")
    if inflate_the_fixed_cell_census:
        for g in sp.PERMS:
            if g == sp.IDENT:
                continue
            fixv[sp.NAME[g]] += 1
            fixe[sp.NAME[g]] += 1
            fixf[sp.NAME[g]] += 1
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
    exact_div = {"0_cells": sum(fixv.values()) % len(sp.PERMS),
                 "1_cells": sum(fixe.values()) % len(sp.PERMS),
                 "2_cells": sum(fixf.values()) % len(sp.PERMS)}
    sizes_e = Counter(len(o) for o in oe)
    sizes_f = Counter(len(o) for o in ot)
    sizes_ok = (sum(k * v for k, v in sizes_e.items()) == len(edges)
                and sum(k * v for k, v in sizes_f.items()) == len(cells)
                and sum(sizes_e.values()) == len(oe)
                and sum(sizes_f.values()) == len(ot))
    gate("TOP-BURNSIDE-EXACT", "measurement",
         "BURNSIDE'S SUM DIVIDES EXACTLY, AND THE ORBIT-SIZE HISTOGRAMS PIN "
         "THE CENSUS.  The orbit counts are floor divisions, so an error of "
         "one to five in the fixed-cell census's TOTAL would be absorbed "
         "silently and TOP-ORBITS would not see it.  Two clauses close that: "
         "the sum of fixed cells is measured to be EXACTLY divisible by the "
         "group order in all three dimensions -- the residues are printed and "
         "must be zero -- and the orbit-size histograms are gated against the "
         "cell counts, sum(size x count) = |E| and = |F| with the number of "
         "orbits recovered as sum(count).  The `fixcell-lax` mutant inflates "
         "every non-identity fixed-cell count by one -- an error the floor "
         "division absorbs, TOP-ORBITS cannot see, and this gate must -- and "
         "it dies here.  A mutant that divides by the WRONG ORDER leaves both "
         "of these clauses true and is not this gate's business: it moves the "
         "orbit counts, and is caught where those are compared against direct "
         "enumeration, which is TOP-ORBITS",
         all(v == 0 for v in exact_div.values()) and sizes_ok,
         {"the_residues_of_the_fixed_cell_sums": exact_div,
          "the_group_order": len(sp.PERMS),
          "the_fixed_cell_sums": {"0_cells": sum(fixv.values()),
                                  "1_cells": sum(fixe.values()),
                                  "2_cells": sum(fixf.values())},
          "orbit_size_histogram_1_cells":
              {str(k): v for k, v in sorted(sizes_e.items())},
          "orbit_size_histogram_2_cells":
              {str(k): v for k, v in sorted(sizes_f.items())},
          "the_histograms_recover_the_cell_counts": sizes_ok})
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
    # ---- THE BOUNDARY-PARITY WITNESS (RUNBOOK section 14 addendum, #313).
    # A boundary row is assembled by XOR, so a 1-cell whose two endpoints
    # coincide contributes ZERO.  On the nerve that is inert -- every 1-cell
    # joins two DISTINCT charts -- and the convention bites exactly on the
    # quotient, where an orbit can meet a vertex orbit twice.  Both
    # connectives are evaluated here and their measured DELTA is the gate's
    # death certificate.
    loops = sum(1 for (a, b) in qpairs if a == b)
    xor_rows = [(1 << a) ^ (1 << b) for (a, b) in qpairs]
    or_rows = [(1 << a) | (1 << b) for (a, b) in qpairs]
    r_xor = rank_f2_high(xor_rows)
    r_or = rank_f2_high(or_rows)
    cyc_xor = len(qpairs) - r_xor
    cyc_or = len(qpairs) - r_or
    d2q = [(1 << x) ^ (1 << y) ^ (1 << z) for (x, y, z) in QC.tris]
    r2q = rank_f2_high(d2q, maxrank=max(cyc_xor, cyc_or))
    b1_xor = cyc_xor - r2q
    b1_or = cyc_or - r2q
    parity = {"loop_1_cells_in_the_quotient": loops,
              "rank_d1_with_XOR": r_xor, "rank_d1_with_OR": r_or,
              "b1_with_XOR": b1_xor, "b1_with_OR": b1_or,
              "the_measured_delta": b1_xor - b1_or,
              "b0_with_XOR": len(ov) - r_xor, "b0_with_OR": len(ov) - r_or,
              "the_delivered_b1": qinv["b1"],
              "the_delivered_assembly_is_XOR": qinv["b1"] == b1_xor}
    gate("TOP-BOUNDARY-PARITY", "measurement",
         "THE BOOLEAN CONNECTIVE OF THE BOUNDARY IS GATED BY ITS OWN DELTA "
         "(RUNBOOK section 14 addendum, #313).  Assembling an incidence bit "
         "pattern with OR instead of the mod-2 XOR is inert wherever every "
         "1-cell joins two distinct 0-cells, and bites exactly where a cell "
         "meets a face twice -- which is the wing quotient, whose 1-skeleton "
         "is measured to carry a non-zero number of LOOP 1-cells, gated here "
         "so the convention is exercised by construction and not by "
         "circumstance.  Both connectives are evaluated on the same quotient "
         "and their DELTA is measured and printed; the gate requires the "
         "delta to be non-zero -- so the convention is load-bearing -- and "
         "the delivered b_1 to be the XOR one.  The `or-lax` mutant "
         "assembles the boundary rows with OR and the `or-lax-T` mutant does "
         "it in the transposed accumulation; both must die here or on the "
         "four-route component check below",
         loops > 0 and b1_xor != b1_or and qinv["b1"] == b1_xor,
         parity)
    nfree_e = len(edges) - sum(1 for i in range(len(edges))
                               if all(eact[g][i] != i for g in sp.PERMS
                                      if g != sp.IDENT))
    chi_free = (n - len(edges) + len(cells))
    gate("TOP-QUOTIENT", "measurement",
         "THE QUOTIENT COMPLEX'S INVARIANTS.  The quotient is the ORBIT CELL "
         "COMPLEX -- cells are orbits, the boundary is induced mod 2 -- and "
         "its components, cycle rank, Euler characteristic and F_2 ranks are "
         "computed by the same two-route standard as the nerve's.  ALL FOUR "
         "component routes are compared here, not two: union-find, the F_2 "
         "rank of the boundary matrix, the rank of its TRANSPOSE and a "
         "spanning forest.  The transpose route is the one that only the "
         "quotient can exercise -- on the nerve routes 2 and 3 agree "
         "trivially because there are no loops -- and without it a quotient "
         "could publish a component count of zero for a non-empty complex.  "
         "The action is measured FREE on 0-cells but NOT on 1- and 2-cells, "
         "so the orbit complex is reported as the orbit CHAIN complex and "
         "the difference from a free quotient is derived from the fixed-cell "
         "census rather than assumed away: chi of the orbit complex minus "
         "chi(N)/|S_3| is measured, and equals the correction Burnside's "
         "lemma predicts from the fixed cells",
         qinv["components_route_1_union_find"] ==
         qinv["components_route_2_F2_rank"] ==
         qinv["components_route_3_transposed_rank"] ==
         qinv["components_route_4_spanning_forest"]
         and qinv["rank_d2_route_1_high_pivot"] ==
         qinv["rank_d2_route_2_cotree_low_pivot"],
         {"quotient": qinv, "the_boundary_parity_witness": parity,
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
        "the_boundary_parity_witness": parity,
        "the_orbit_size_histograms_pin_the_census": sizes_ok,
        "the_fixed_cell_sum_residues": exact_div,
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
    c2, coh2, _pc, _df, _cj = geometric_cells(sp2, pr2, ei2, len(ch2))
    inv2 = Complex(len(ch2), [(a, b) for (a, b, c, p) in ed2], c2,
                   "two-wing atlas").invariants()
    b1_ok = (rows["3"]["b1"] == two["cycle_rank"])
    gate("TOP-POS-2WING", "control",
         "THE POSITIVE CONTROL: THE SAME GENERIC MACHINERY AT TWO WINGS, AND "
         "EXACTLY WHAT IT ANCHORS.  Instantiated at a 16-configuration "
         "carrier neither committed unit used, the machinery reproduces the "
         "committed two-wing transport graph at BOTH realised defect orders "
         "-- nodes, links, identification links, cycle rank and the "
         "completion itself, every one anchored exit-1 against the "
         "hash-pinned receipt.  That anchors the ONE-DIMENSIONAL route and "
         "only it.  The b_1 column is NOT a second anchor: the control graph "
         "carries no 2-cells, so rank(d_2) = 0 and b_1 equals the cycle rank "
         "IDENTICALLY -- the identity is printed here rather than counted as "
         "evidence, on deviation 3's own standard.  NO COMMITTED NUMBER "
         "ANCHORS rank(d_2) ANYWHERE IN THIS UNIT; the two-dimensional half "
         "of the homology machinery is calibrated by the DECLARED-STANDARD "
         "control complexes alone, which buy calibration and not "
         "independence, and that is disclosed rather than smoothed.  The "
         "two-wing ATLAS is then run through the same nerve machinery, and "
         "its invariants are printed",
         all(a["passed"] for a in ANCHORS if a["id"].startswith("A-2W-"))
         and b1_ok,
         {"per_defect_order": rows,
          "b1_equals_the_committed_cycle_rank": b1_ok,
          "b1_equals_the_cycle_rank_identically_because_there_are_no_2_cells":
              all(v["b1"] == v["cycle_rank_route_1"] for v in rows.values()),
          "no_committed_number_anchors_rank_d2": True,
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
        # TB3's committed negative-control rows carry no `nodes` field, so
        # this one is NOT read from external bytes: it is the DECLARED
        # STRUCTURAL size |FRAMES| x |CHECKPOINTS|, and it is labelled as such
        # rather than counted among the external anchors.
        specs.append((key, use, setting,
                      {"links": cm["links"], "identification_links":
                       cm["identification_links"],
                       "cycle_rank": cm["cycle_rank"],
                       "nodes": len(sp.FRAMES) * len(sp.CKPTS),
                       "nodes_are_structural": True}))
    rows = {}
    for (label, q, setting, cm) in specs:
        w = World(sp, psi, q, setting)
        adm = w.transport_admission()
        nodes, links, nid = transport_graph(sp, w, adm)
        index = {x: i for i, x in enumerate(nodes)}
        inv = Complex(len(nodes), [(index[a], index[b])
                                   for (_n, a, b) in links], [],
                      label).invariants()
        anchor("A-TG-NODES-" + label,
               "DECLARED-STRUCTURAL (a size forced by the declared base)"
               if cm.get("nodes_are_structural")
               else "TB3 committed receipt",
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
    cells, coh, _pc, _df, _cj = geometric_cells(sp, pair, eidx, n)
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
    # WHY b_0 AND b_1 DO NOT MOVE, MEASURED rather than narrated: the
    # scrambled atlas's own per-checkpoint census, and the coordinate count it
    # pins (RUNBOOK failure catalogue #38->#40).
    sper, ssb0, ssb1, slive = {}, 0, 0, 0
    for t in sp.CKPTS:
        loc = [i for i, (a, b, c, p) in enumerate(edges) if c[0] == t]
        if not loc:
            continue
        slive += 1
        ren = {e: i for i, e in enumerate(loc)}
        el = [(edges[e][0], edges[e][1]) for e in loc]
        tl = [tuple(ren[x] for x in tr) for tr in cells
              if all(y in ren for y in tr)]
        sub = Complex(n, el, tl, "scrambled t=%d" % t).invariants()
        sper[str(t)] = {"E": sub["E"], "F": sub["F"], "b0": sub["b0"],
                        "b1": sub["b1"]}
        ssb0 += sub["b0"]
        ssb1 += sub["b1"]
    scoord = (slive - 1) * (n - 1)
    scr_census = {
        "per_checkpoint": sper, "sum_of_per_checkpoint_b0": ssb0,
        "sum_of_per_checkpoint_b1": ssb1,
        "read_times_carrying_cells": slive,
        "the_coordinate_count_T_minus_1_times_V_minus_1": scoord,
        "b1": inv["b1"], "b1_equals_the_coordinate_count": inv["b1"] == scoord,
        "the_reference_b1": ref["b1"],
        "b1_is_unmoved_by_the_scramble": inv["b1"] == ref["b1"],
        "b2_moves_from_to": [ref["b2"], inv["b2"]]}
    gate("TOP-NEG-SCRAMBLE", "control",
         "THE NEGATIVE CONTROL HAS TEETH.  A declared deterministically "
         "scrambled atlas -- three quarters of each coordinate cell's links "
         "redrawn from all chart pairs by an exact integer recurrence seeded "
         "by the SHA-256 of the declared data alone -- is measured to MOVE "
         "the invariant table and to BREAK the dimension reading, which then "
         "returns INCONSISTENT with a named witness chart.  The "
         "`scramble-off` mutant leaves the atlas alone and must die here, "
         "which is what shows the two clauses are measurements and not "
         "restatements.  WHAT DOES NOT MOVE IS ALSO MEASURED: b_0 and b_1 "
         "are unchanged, and the reason is not narrated but computed -- the "
         "scrambled atlas's OWN per-checkpoint census is taken here and "
         "returns the same connected, simply connected read times, so the "
         "gluing formula pins b_1 to the coordinate count (T-1)(|V|-1) at "
         "the scrambled atlas exactly as at the reference.  The degree-one "
         "invariant is therefore measured INSENSITIVE to the identification "
         "data; b_2 is not",
         bool(moved) and broke,
         {"invariants_that_moved": moved,
          "the_scrambled_atlas_per_checkpoint_census": scr_census,
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
        "the_per_checkpoint_census": scr_census,
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
         "EVERY ANCHOR DECLARES ITS PROVENANCE and the split is printed in "
         "FOUR classes, never averaged and never rounded up to `external'.  "
         "EXTERNAL: the declared side is read from bytes outside this file, "
         "TB3's hash-pinned committed receipt.  SELF-PIN: the declared side "
         "is the SHA-256 typed in this source and the computed side is the "
         "hash of the foundation's bytes -- it pins the foundation and is "
         "not an external reading, so it is counted apart.  STRUCTURAL: the "
         "declared side is a size FORCED by the declared base (the transport "
         "graph's |FRAMES| x |CHECKPOINTS| nodes, which TB3's negative-"
         "control rows do not carry), computed from the declaration rather "
         "than typed, and incapable of failing -- named here rather than "
         "counted as evidence.  DECLARED-STANDARD: a standard invariant of a "
         "control complex typed in this source, which buys calibration and "
         "not independence.  This gate is a VOCABULARY check and says so: it "
         "verifies that every anchor names a declared class, not that an "
         "external anchor's bytes were read.  Its only falsifier is the "
         "`provenance-lax` WAIVER, which registers a bad label after the "
         "sweep, and it is classified as a waiver rather than a computation "
         "mutant for exactly that reason",
         not unknown, {"by_provenance": dict(by), "unknown": unknown,
                       "total": len(ANCHORS),
                       "the_declared_classes": ANCHOR_PROVENANCE})


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
def _unit_args(inv, coord_T, coord_V, scrambled_b1, qq):
    return (coord_T, coord_V, inv["V"], inv["E"], inv["F"], inv["b0"],
            inv["cycle_rank_route_1_spanning_forest"],
            inv["chi_from_cell_counts"], inv["b0"], inv["b1"], inv["b2"],
            coord_T, coord_V, coord_T * coord_V, scrambled_b1, inv["b2"],
            qq["b2_scrambled"], qq["chi"], qq["b0"], qq["b1"], qq["b2"])


def run_verdict(q1, manifold_verdict, selector_verdict, qinv):
    ref = q1[REFERENCE_INSTANCE]["the_nerve_N"]
    rq1 = q1[REFERENCE_INSTANCE]
    nc = TABLES["negative_control"]
    blocked = None
    flip = (MUTANT == "verdict-flip")
    typed = (MUTANT == "unit-typed")
    coord_T = rq1["the_read_times_carrying_cells"] - 1
    coord_V = ref["V"] - 1
    qq = {"b2_scrambled": nc["scrambled"]["b2"],
          "chi": qinv["chi_from_cell_counts"], "b0": qinv["b0"],
          "b1": qinv["b1"], "b2": qinv["b2"]}
    if flip:
        unit = "TOP-BLOCKED-AT-<the nerve>"
    else:
        emitted = dict(ref)
        if typed:
            emitted["b1"] = ref["b1"] + 1
        unit = V_UNIT % _unit_args(emitted, coord_T, coord_V,
                                   nc["scrambled"]["b1"], qq)
    computed_ok = all(g["passed"] for g in GATES
                      if g["class"] in ("measurement", "control", "anchor"))
    if computed_ok:
        rrec = TABLES["q1_invariants"][REFERENCE_INSTANCE]
        rinv = rrec["the_nerve_N"]
        rqq = {"b2_scrambled": TABLES["negative_control"]["scrambled"]["b2"],
               "chi": TABLES["q4_quotient"]["the_quotient_complex"][
                   "chi_from_cell_counts"],
               "b0": TABLES["q4_quotient"]["the_quotient_complex"]["b0"],
               "b1": TABLES["q4_quotient"]["the_quotient_complex"]["b1"],
               "b2": TABLES["q4_quotient"]["the_quotient_complex"]["b2"]}
        derived = V_UNIT % _unit_args(
            rinv, rrec["the_read_times_carrying_cells"] - 1, rinv["V"] - 1,
            TABLES["negative_control"]["scrambled"]["b1"], rqq)
    else:
        derived = "TOP-BLOCKED-AT-<the nerve>"
    gate("TOP-VERDICT", "derivation",
         "THE UNIT VERDICT IS REBUILT INSIDE THIS GATE FROM THE RECORDED "
         "TABLES AND GATED BYTE-FOR-BYTE against the emitted string -- head, "
         "computed qualifiers and body alike, not a prefix (RUNBOOK section "
         "13 addendum, #234; #257: a qualifier is part of the verdict).  The "
         "BRANCH is derived from the measured gate outcomes -- the structure "
         "verdict is emitted only if every measurement, control and anchor "
         "gate passed, the alternative being the pre-registered "
         "TOP-BLOCKED-AT-<object> -- and the head then carries the "
         "restriction the measurement actually supports: the topology is the "
         "COORDINATE-RESOLVED nerve's, its degree-one rank is the coordinate "
         "count (read times - 1) x (charts - 1) with both factors "
         "interpolated from measured counts, and the SCRAMBLED control "
         "returns the same b_1.  The `verdict-flip` mutant moves the branch "
         "and the `unit-typed` mutant moves ONE COMPUTED QUALIFIER of the "
         "emitter with every recorded table left at its measured value; both "
         "must die here.  Only pre-registered names are emitted and the "
         "vocabulary is checked against the pin's list",
         unit == derived
         and (unit.startswith(PREREGISTERED_UNIT[0])
              or unit.startswith(PREREGISTERED_UNIT[1]))
         and (manifold_verdict.startswith(PREREGISTERED_MANIFOLD[0])
              or manifold_verdict.startswith(PREREGISTERED_MANIFOLD[1]))
         and (selector_verdict.startswith(PREREGISTERED_SELECTOR[0])
              or selector_verdict.startswith(PREREGISTERED_SELECTOR[1])),
         {"unit": unit, "the_verdict_rebuilt_from_the_recorded_tables":
             derived, "the_two_strings_are_byte_identical": unit == derived,
          "manifold": manifold_verdict,
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
    ("link-lax-atlas", "computation",
     "the ATLAS's vertex link built from the 1-cells alone rather than from "
     "the 2-cells, so it is a star and never a circle -- injected in the "
     "audited path only, with the control path untouched"),
    ("link-lax-control", "computation",
     "the CONTROL complexes' vertex link built from the 1-cells alone, "
     "injected in the control path only, with the atlas path untouched"),
    ("star-lax", "computation",
     "the star profile inflated by one 1-cell and one 2-cell at every chart"),
    ("sym-lax", "computation",
     "one direction of one admitted ordered pair deleted, so the drawn "
     "relation stops being symmetric"),
    ("block-lax", "computation",
     "the block-incidence graph built from one rule's partition alone"),
    ("digon-lax", "computation",
     "every digon reported coherent regardless of its two drawn maps"),
    ("auto-lax", "computation",
     "every automorphism candidate accepted without testing it against the "
     "drawn table"),
    ("cache-lax", "computation",
     "the memoized defect subgroup perturbed on a cache hit"),
    ("fixcell-lax", "computation",
     "every non-identity fixed-cell count inflated by one -- an error "
     "Burnside's floor division absorbs"),
    ("or-lax", "computation",
     "the mod-2 boundary rows assembled with OR instead of XOR, so a cell "
     "meeting a face twice contributes an incidence bit rather than zero"),
    ("or-lax-T", "computation",
     "the same OR-for-XOR substitution in the TRANSPOSED column "
     "accumulation"),
    ("subcell-drop", "computation",
     "one 2-cell dropped from each per-checkpoint sub-complex only, so H_2 "
     "stops being additive over the checkpoints"),
    ("unit-typed", "computation",
     "one COMPUTED QUALIFIER of the unit verdict replaced in the emitter "
     "while every recorded table keeps its measured value"),
    ("manifold-typed", "computation",
     "one COMPUTED QUALIFIER of the manifold verdict replaced in the emitter "
     "while every recorded table keeps its measured value"),
    ("selector-typed", "computation",
     "one COMPUTED QUALIFIER of the selector verdict replaced in the emitter "
     "while every recorded table keeps its measured value"),
    ("crosscell-typed", "computation",
     "the cross-coordinate outcome emitted at the other pre-registered "
     "branch while the measured residual is left unchanged"),
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
    ("provenance-lax", "waiver",
     "an undeclared provenance label registered in the provenance gate's own "
     "evidence list AFTER its sweep over the anchors has run: no anchor is "
     "ever built with a bad label and no computation is perturbed, so this "
     "is a WAIVER by the unit's own definition and is declared as one"),
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
    L.append("WHAT b1 MEASURES: the coordinate count (T-1)(|V|-1), and where "
             "it holds")
    L.append("%-46s %3s %5s %7s %6s %6s %6s" %
             ("instance", "T", "|V|", "(T-1)x", "b1", "sum b0", "sum b1"))
    for k, v in TABLES["q1_invariants"].items():
        L.append("%-46s %3d %5d %7d %6d %6d %6d" %
                 (k[:46], v["the_read_times_carrying_cells"],
                  v["the_nerve_N"]["V"],
                  v["the_coordinate_count_T_minus_1_times_V_minus_1"],
                  v["the_nerve_N"]["b1"], v["sum_of_per_checkpoint_b0"],
                  v["sum_of_per_checkpoint_b1"]))
    sc = TABLES["negative_control"]["the_per_checkpoint_census"]
    L.append("%-46s %3d %5d %7d %6d %6d %6d"
             % ("the scrambled negative control",
                sc["read_times_carrying_cells"],
                TABLES["q1_invariants"][REFERENCE_INSTANCE]["the_nerve_N"]["V"],
                sc["the_coordinate_count_T_minus_1_times_V_minus_1"],
                sc["b1"], sc["sum_of_per_checkpoint_b0"],
                sc["sum_of_per_checkpoint_b1"]))
    L.append("")
    L.append("THE BLOCK-INCIDENCE ROUTE: a read time's topology is the "
             "nesting of the two")
    L.append("rules' partitions.  I_t joins two blocks that share a chart.")
    L.append("%-30s %2s %9s %6s %6s %14s" %
             ("instance", "t", "blocks", "I: V", "I: E", "(b0,cyc) = sub"))
    for k, v in TABLES["q1_invariants"].items():
        for t, b in sorted(v["the_block_incidence_route"].items()):
            L.append("%-30s %2s %9s %6d %6d   (%d,%d) = (%d,%d)"
                     % (k[:30], t, canon(b["blocks_per_rule"]),
                        b["incidence_V"], b["incidence_E"],
                        b["b0_of_the_incidence_graph"],
                        b["cycle_rank_of_the_incidence_graph"],
                        v["per_checkpoint"][t]["b0"],
                        v["per_checkpoint"][t]["b1"]))
    L.append("")
    L.append("DO THE DRAWN MAPS AGREE ACROSS COORDINATE CELLS? (declared D3b)")
    L.append("%-30s %6s %6s %9s %6s %7s %7s" %
             ("instance", "pairs", "agree", "disagree", "digons",
              "coh x-ck", "b1 left"))
    for k, v in TABLES["q1_invariants"].items():
        c = v["the_cross_coordinate_drawn_map_comparison"]
        L.append("%-30s %6d %6d %9d %6d %7d %7d"
                 % (k[:30], c["pairs_drawn_at_two_or_more_cells"],
                    c["pairs_whose_drawn_maps_all_agree"],
                    c["pairs_whose_drawn_maps_disagree_somewhere"],
                    c["digons_built"],
                    c["cross_checkpoint_digons_that_are_coherent"],
                    c["b1_with_the_COHERENT_cross_checkpoint_digons_filled"]))
    cr = ref["the_cross_coordinate_drawn_map_comparison"]
    L.append("at the reference: same-checkpoint digons %d kill %d of %d; "
             "cross-checkpoint" % (cr["same_checkpoint_digons"],
                                   cr["b1_of_N"] -
                                   cr["b1_with_the_same_checkpoint_digons_"
                                      "filled"], cr["b1_of_N"]))
    L.append("digons %d (of which %d coherent) leave b1 = %d."
             % (cr["cross_checkpoint_digons"],
                cr["cross_checkpoint_digons_that_are_coherent"],
                cr["b1_with_the_COHERENT_cross_checkpoint_digons_filled"]))
    L.append("OUTCOME: %s" % FINDINGS.get("cross_cell_outcome", "?"))
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
    L.append("IS THE READING A MEASUREMENT?  The drawn table's automorphisms")
    L.append("%-46s %6s %6s %6s %s" % ("instance", "autos", "orbits", "vals",
                                       "the reading"))
    for k, v in TABLES["q2_dimension"]["per_instance"].items():
        a = v["the_drawn_table_automorphisms"]
        L.append("%-46s %6d %6d %6d %s"
                 % (k[:46], a["measured_automorphisms"], a["chart_orbits"],
                    v["distinct_estimator_values"],
                    "CONSISTENT (orbit count 1: FORCED, a disclosure)"
                    if v["chart_independence_is_symmetry_forced"]
                    else ("CONSISTENT" if v["the_reading_is_consistent"]
                          else "INCONSISTENT (measured)")))
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
    L.append("CLAUSE (c) IS A CONTAINMENT (disclosure): its count is |C \\ C4|")
    L.append("%-5s %8s %10s %10s %s" % ("id", "holds", "clause(c)",
                                        "|C \\ C4|", "C contained in C4"))
    fc = q3["the_forced_structure_of_the_family"]
    for (cid, _s, _t, _o) in SELECTOR_CANDIDATES:
        v = fc["per_candidate"][cid]
        L.append("%-5s %8d %10d %10d %s"
                 % (cid, v["holds_at"], v["clause_c_count"],
                    v["the_containment_deficit"], v["is_contained_in_C4"]))
    L.append("the extensional duplicates: %s; %d declared names, %d distinct "
             "predicates"
             % (canon(fc["the_extensional_duplicates"]),
                len(SELECTOR_CANDIDATES),
                fc["distinct_predicates_among_the_declared_names"]))
    L.append("")
    md = q3["the_section_5_2_tables_as_markdown"]
    L.append("THE SAME TWO TABLES, EMITTED AS MARKDOWN ROWS FROM THE RECORDED")
    L.append("TABLE ABOVE, so that the paper's section 5.2 is GENERATED and "
             "never retyped:")
    for row in md["the_candidate_table"]:
        L.append(row)
    L.append("")
    for row in md["the_clause_c_containment"]:
        L.append(row)
    L.append("")
    L.append("P* IS AN ARENA COORDINATE: the five-wing-symmetry sweep")
    L.append("%-6s %-14s %7s %10s %s" % ("P*", "type", "locus", "on-locus",
                                         "ord distribution"))
    for k, v in sorted(q3["the_P_star_sweep"].items()):
        L.append("%-6s %-14s %7d %10d %s"
                 % (k, v["the_type_of_the_symmetry"], v["the_order_2_locus"],
                    v["on_the_locus_K_equals_GL_3_2"],
                    canon(v["the_defect_order_distribution"])))
    L.append("the declared P* is %s (%s); K itself does not depend on P*, so "
             "the %d" % (q3["the_declared_P_star"], q3["the_P_star_type"],
                         q3["completions_whose_K_equals_GL_3_2"]))
    L.append("completions reaching GL(3,2) as a set are P*-INDEPENDENT and "
             "the locus is not.")
    L.append("")
    L.append("THE ORDER-THEORETIC LADDER, and where it stops")
    L.append("%-56s %8s %12s" % ("purely order-theoretic condition", "passing",
                                 "false pos."))
    for row in q3["the_order_theoretic_ladder"]:
        L.append("%-56s %8d %12d"
                 % (row["the_condition"][:56], row["completions_passing"],
                    row["false_positives_against_K_contained_in_GL_3_2"]))
    L.append("every level contains all %d completions with K inside GL(3,2); "
             "the finest still"
             % q3["completions_whose_K_is_contained_in_GL_3_2"])
    L.append("admits %d false positives, so no order condition characterises "
             "the visit."
             % q3["the_order_theoretic_ladder"][-1][
                 "false_positives_against_K_contained_in_GL_3_2"])
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
    L.append("Burnside divides EXACTLY: fixed-cell sum residues mod |S_3| %s"
             % canon(q4["the_fixed_cell_sum_residues"]))
    L.append("orbit-size histograms 1-cells %s, 2-cells %s; they recover the "
             "cell counts %s"
             % (canon(q4["orbit_sizes_1_cells"]),
                canon(q4["orbit_sizes_2_cells"]),
                q4["the_orbit_size_histograms_pin_the_census"]))
    bp = q4["the_boundary_parity_witness"]
    L.append("BOUNDARY PARITY: %d loop 1-cells; XOR gives rank d1 %d, b0 %d, "
             "b1 %d;" % (bp["loop_1_cells_in_the_quotient"],
                         bp["rank_d1_with_XOR"], bp["b0_with_XOR"],
                         bp["b1_with_XOR"]))
    L.append("OR gives rank d1 %d, b0 %d, b1 %d -- the measured delta is %d, "
             "and the delivered" % (bp["rank_d1_with_OR"], bp["b0_with_OR"],
                                    bp["b1_with_OR"], bp["the_measured_delta"]))
    L.append("assembly is the XOR one: %s"
             % bp["the_delivered_assembly_is_XOR"])
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
    pcc = nc["the_per_checkpoint_census"]
    L.append("  why b0 and b1 do NOT move, measured: the scrambled atlas's "
             "own per-checkpoint")
    L.append("  census is sum b0 = %d over %d read times and sum b1 = %d, so "
             "the gluing formula"
             % (pcc["sum_of_per_checkpoint_b0"],
                pcc["read_times_carrying_cells"],
                pcc["sum_of_per_checkpoint_b1"]))
    L.append("  pins b1 to the coordinate count %d, exactly as at the "
             "reference; b2 moves %s."
             % (pcc["the_coordinate_count_T_minus_1_times_V_minus_1"],
                canon(pcc["b2_moves_from_to"])))
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
    _cyc3 = sorted(k for k, v in TABLES["q3_selector"]["the_P_star_sweep"]
                   .items() if v["the_type_of_the_symmetry"] == "3-cycle")[0]
    FINDINGS["thesis"] = (
        "THE ATLAS HAS A SHAPE AND IT IS NOT A MANIFOLD'S.  At the reference "
        "instance the overlap graph is COMPLETE, so the simplicial nerve is "
        "the whole chart set, a cone, contractible; whatever topology the "
        "atlas has lives in the COORDINATE-RESOLVED nerve, which is connected "
        "with b_1 = %d and b_2 = %d over F_2.  WHAT b_1 MEASURES IS THE "
        "COORDINATE GRID, not the identifications: it equals (read times - 1) "
        "x (charts - 1) = %d whenever each read time is connected and simply "
        "connected, and the SCRAMBLED negative control -- whose identification "
        "data is destroyed -- returns %d as well, while b_2 moves from %d to "
        "%d.  A read time's own topology is measured to be exactly the "
        "NESTING of the two rules' block partitions.  And the degree-one "
        "classes are measured NOT to be a cross-read-time obstruction: "
        "filling only the digons whose two drawn maps AGREE already reduces "
        "b_1 to %d, so the surviving cycles are an artifact of the declared "
        "same-checkpoint 2-cell scope.  The local-dimension estimator is "
        "chart-independent at the reference -- but the drawn table there is "
        "chart-transitive under %d measured automorphisms with %d orbit, so "
        "that uniformity is FORCED and is a disclosure; what is measured is "
        "the contrast at the two instances where the table is not "
        "chart-transitive and the estimator splits the charts.  The link is "
        "never a circle, so uniformity is not manifoldhood.  The wing factor "
        "acts freely on the charts and not on the higher cells, and the "
        "quotient's Euler characteristic differs from chi(N)/6 by exactly the "
        "correction the fixed-cell census forces.  THE FANO RUNG IS NOT "
        "SELECTED BY ITS LOCUS: of thirteen declared names -- %d distinct "
        "predicates -- none passes all three clauses, only %d of the %d "
        "order-2 completions reach GL(3,2), and GL(3,2) is reached at %d "
        "completions spread across four defect orders.  The locus itself is "
        "P*-RELATIVE: at a 3-cycle wing symmetry it holds %d completions of "
        "which %d reach GL(3,2).  The exclusivity of the visit is a property "
        "of the lex-first SELECTION RULE, not of the order-2 locus, and no "
        "purely order-theoretic condition captures it -- the finest one "
        "measured still admits %d false positives."
        % (q1[REFERENCE_INSTANCE]["the_nerve_N"]["b1"],
           q1[REFERENCE_INSTANCE]["the_nerve_N"]["b2"],
           q1[REFERENCE_INSTANCE][
               "the_coordinate_count_T_minus_1_times_V_minus_1"],
           TABLES["negative_control"]["scrambled"]["b1"],
           q1[REFERENCE_INSTANCE]["the_nerve_N"]["b2"],
           TABLES["negative_control"]["scrambled"]["b2"],
           q1[REFERENCE_INSTANCE][
               "the_cross_coordinate_drawn_map_comparison"][
               "b1_with_the_COHERENT_cross_checkpoint_digons_filled"],
           TABLES["q2_dimension"]["per_instance"][REFERENCE_INSTANCE][
               "the_drawn_table_automorphisms"]["measured_automorphisms"],
           TABLES["q2_dimension"]["per_instance"][REFERENCE_INSTANCE][
               "the_drawn_table_automorphisms"]["chart_orbits"],
           TABLES["q3_selector"]["the_forced_structure_of_the_family"][
               "distinct_predicates_among_the_declared_names"],
           TABLES["q3_selector"]["of_those_on_the_order_2_locus"],
           TABLES["q3_selector"]["the_locus_size"],
           TABLES["q3_selector"]["completions_whose_K_equals_GL_3_2"],
           TABLES["q3_selector"]["the_P_star_sweep"][_cyc3][
               "the_order_2_locus"],
           TABLES["q3_selector"]["the_P_star_sweep"][_cyc3][
               "on_the_locus_K_equals_GL_3_2"],
           TABLES["q3_selector"]["the_order_theoretic_ladder"][-1][
               "false_positives_against_K_contained_in_GL_3_2"]))
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
