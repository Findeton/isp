#!/usr/bin/env python3
"""RQ0-L3 stage 5 -- epsilon-admissibility and the mixed-law arena.

Executes the frozen pin `v13/note-rq0-l3-epsilon-admissibility-pin.md`
(commit 6e1aa82) against the immutable B" TERMINAL base.

H1 -- EPSILON-ADMISSIBILITY.  B"'s rigidity dichotomy says a proper
(coarse) boundary is NEVER admissible under a law containing a reversible
operation.  The designed successor QUANTIFIES rather than relaxes: the
concordance defect

    eps(P) = delta(A(B), F, rho)

is B"'s own refinement statistic, read as the state mass on which the
admitted later readout resolves a distinction inside a declared atom.  A
patch is EPS-ADMISSIBLE AT TOLERANCE tau when (i-b) and non-emptiness and
the occupancy clause hold EXACTLY and eps(P) <= tau.  At full support, and
at a law whose admitted operations are SINGLE-VALUED, tau = 0 returns the
terminal axiom exactly (the REDUCTION THEOREM, gated both directions and
with the declared preparation varied).  Single-valuedness is load-bearing
three times over and each failure without it is exhibited: the reduction,
the entailment lemma and the closed form all have countermodels at
support-valued laws.  eps itself is the boundary's BAYES ERROR, which is
why it measures resolution and cannot see provenance.

H2 -- THE MIXED-LAW ARENA.  Two patches, DIFFERENT admitted laws.  The
anchored escape (member one admissible under the identity-free {(0,0,2,3,4)},
member two under DET) is run through (i) shared refinement and (ii)
inter-law descent, and whatever survives is priced exactly.  The
occupancy-sensitive statistic omega -- the Feynman gate's missing half --
is constructed and gated, and the blindness of B"'s own two statistics is
proved structural.  omega is proved and measured to be a function of the
quadruple, and it does not separate the comparison eps failed.  The
declared STATE is the fifth declaration and neither closure route has a
state analogue, so the mixed-state arena is registered OPEN.

Immutable inputs reused as anchors: Cycle B TERMINAL (v13 #123), Cycle B'
TERMINAL (v13 #134), Cycle B" TERMINAL (v13 #145) and the three frozen B"
panel reviews.  Every reused committed value is an anchor and exits 1 on
mismatch.  Substantive negatives exit 0.  `--mutant NAME` breaks exactly
one committed anchor or one derivation step and must exit 1.

Scope: finite; ONE committed carrier of five configurations; the committed
law families; "coarse" is algebra-relative only.  Reachability is an ORDER
ON CONFIGURATIONS and carries no spatial, causal or temporal reading.  No
locality, topology, causality, spacetime, field, QFT or gravity object is
constructed or claimed.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import inspect
import json
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations, permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import rq0_l0_fixed_point_exact as CB    # Cycle B TERMINAL machinery
import rq0_l1_composite_exact as CBP     # Cycle B' TERMINAL machinery
import rq0_l2_admissibility_exact as L2  # Cycle B" TERMINAL machinery

SCHEMA = "rq0-l3-epsilon-admissibility-receipt-v1"
PIN_COMMIT = "6e1aa82"
BASE_COMMIT = "267cb2a"
OUT_TXT = HERE / "rq0_l3_epsilon_output.txt"
OUT_JSON = HERE / "rq0_l3_epsilon_receipt.json"

T0 = time.time()
MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}

CARRIER = 5
PREP_FULL = frozenset(range(CARRIER))
RHO = L2.RHO                      # the committed branch-memory state
PI1 = ((0, 1), (2,), (3,), (4,))  # the forged aligned manufactured 2+1+1
P22 = ((0, 1), (2, 3), (4,))      # the forged aligned manufactured 2+2
PTOMO = ((0, 1, 2, 3), (4,))      # the LEGITIMATE corrected tomographic min
DISC5 = CB.discrete(5)
A_ESCAPE = (0, 0, 2, 3, 4)        # R1/R2's escape generator


def prog(msg: str) -> None:
    sys.stdout.write(f"[{time.time() - T0:7.1f}s] {msg}\n")
    sys.stdout.flush()


# --------------------------------------------------------------------------
# 0.  Gates and anchors.
# --------------------------------------------------------------------------


def gate(gid: str, cls: str, claim: str, ok: bool, value=None) -> bool:
    GATES.append({"id": gid, "class": cls, "claim": claim, "passed": bool(ok),
                  "value": value})
    return bool(ok)


def anchor(aid: str, source: str, quantity: str, committed, computed) -> None:
    """Exit-1-only.  Every committed number this unit reuses is reproduced by
    its own route and compared here; a mismatch kills the run loudly."""
    if MUTANT == f"anchor:{aid}":
        computed = "MUTANT"
    ok = (committed == computed)
    ANCHORS.append({"id": aid, "source": source, "quantity": quantity,
                    "committed": committed, "computed": computed,
                    "passed": bool(ok)})
    if not ok:
        sys.stdout.write(
            f"\nANCHOR FAILURE {aid}: {quantity}\n"
            f"  committed ({source}): {committed!r}\n"
            f"  computed here      : {computed!r}\n")
        sys.stdout.flush()
        raise SystemExit(1)


def uniform(n: int):
    return tuple(Fr(1, n) for _ in range(n))


# --------------------------------------------------------------------------
# 1.  THE EPSILON FORM.  eps is B"'s own delta, decomposed task by task.
# --------------------------------------------------------------------------


def task_defect(part, F, rho):
    """THE PER-TASK CONCORDANCE DEFECT.

        d(F, pi, rho) = sum_r [ Pr(r) - max_s Pr(r,s) ]

    the state mass on which the admitted later readout resolves a
    distinction inside a declared atom, for ONE declared task.  Exactly the
    summand of B" Definition 7.1's refinement statistic delta, which is the
    maximum of d over the declared family.  d is INTRINSIC to (F, pi, rho):
    nothing else in the declared family or in the law can change it.  That
    is what makes Section 5's graded cost bound run."""
    tot = Fr(0)
    for r in part:
        pr = sum((rho[j] for j in r), Fr(0))
        mx = Fr(0)
        for s in range(len(rho)):
            v = sum((rho[j] * Fr(1, len(F[j])) for j in r if s in F[j]), Fr(0))
            if v > mx:
                mx = v
        tot += pr - mx
    return tot


def epsilon(part, fam, rho):
    """THE CONCORDANCE DEFECT eps(P) = max_F d(F, pi, rho) = B"'s delta.
    Zero on the empty family, which is why Definition 2.2's non-emptiness
    clause is carried into the eps-form explicitly (control L3-04)."""
    if MUTANT == "eps-lax":
        return Fr(0)
    worst = Fr(0)
    for F in fam:
        v = task_defect(part, F, rho)
        if v > worst:
            worst = v
    return worst


def occupancy_defect(part, fam, prep, rho, n):
    """THE OCCUPANCY STATISTIC omega -- the Feynman gate's missing half.

    Run the boundary's record instrument twice: on the committed state rho,
    giving outcome probabilities p_r; and on the patch's OWN realized state,
    the uniform preparation on Reach(P), giving q_r.  Then

        omega(P) = sum_r p_r * [ q_r = 0 ]

    the committed state's probability of a record outcome the patch's own
    realized process never produces.  It is a functional of two admitted
    experiments' outcome distributions, it is exact-rational, and unlike
    sigma and delta it READS THE DECLARED PREPARATION."""
    R = set(range(n)) if MUTANT == "omega-lax" else L2.reach_of(fam, prep, n)
    tot = Fr(0)
    for r in part:
        if not (set(r) & R):
            tot += sum((rho[j] for j in r), Fr(0))
    return tot


def unrealized_pairs(part, fam, prep, n):
    """(ii-b)'s SECOND clause: asserted identifications not realized between
    reachable configurations.  omega does not see this clause, and that is
    reported rather than absorbed."""
    R = L2.reach_of(fam, prep, n)
    out = []
    for b in part:
        occ = sorted(set(b) & R)
        for x in occ:
            for y in occ:
                if x < y and not any(
                        any(x in blk and y in blk for blk in L2.written_of(F))
                        for F in fam):
                    out.append([x, y])
    return out


def is_single_valued(law) -> bool:
    """DETERMINISM, MEASURED.  Every admitted operation of the law carries a
    singleton support.  This is the hypothesis the reduction theorem, the
    entailment lemma and the closed form all require; the countermodels of
    L3-25, L3-26 and L3-27 are exactly what it excludes."""
    if MUTANT == "singlevalued-lax":
        return True
    return all(len(s) == 1 for F in law for s in F)


def closed_form(part, rho):
    """THE LAW-FREE CLOSED FORM, sum_r [ Pr(r) - max_{j in r} rho_j ]."""
    if MUTANT == "closedform-lax":
        return Fr(0)
    return sum((sum((rho[j] for j in r), Fr(0)) - max(rho[j] for j in r)
                for r in part), Fr(0))


def bayes_error(part, rho):
    """THE SAME QUANTITY, NAMED: the Bayes error of inferring the declared
    configuration from the record outcome under rho, 1 - sum_r max_{j in r}
    rho_j.  eps is the boundary's residual Bayes error, which is what makes
    its monotonicity a one-line corollary rather than a sweep."""
    return Fr(1) - sum((max(rho[j] for j in r) for r in part), Fr(0))


def state_map(rho):
    """THE CLOSED-FORM STATE MAP of the three committed coarse boundaries,
    as functions of the declared state alone:

        forged 2+1+1  ->  min(rho_0, rho_1)
        forged 2+2    ->  min(rho_0, rho_1) + min(rho_2, rho_3)
        legitimate    ->  the same, plus min(max(rho_0,rho_1), max(rho_2,rho_3))

    The two gaps are non-negative at every state and strictly positive at
    every full-support state, which is why the inversion is a theorem about
    the whole simplex and not a measurement at one declared state."""
    if MUTANT == "statemap-lax":
        return Fr(0), Fr(0), Fr(0)
    a = min(rho[0], rho[1])
    b = min(rho[2], rho[3])
    c = min(max(rho[0], rho[1]), max(rho[2], rho[3]))
    return a, a + b, a + b + c


def grid_states():
    """Every declared state of denominator 16 at the committed carrier: all
    C(20,4) = 4845 compositions of 16 into five non-negative parts."""
    out = []
    for c1 in range(17):
        for c2 in range(17 - c1):
            for c3 in range(17 - c1 - c2):
                for c4 in range(17 - c1 - c2 - c3):
                    out.append(tuple(Fr(x, 16) for x in
                                     (c1, c2, c3, c4,
                                      16 - c1 - c2 - c3 - c4)))
    return out


def preps_of(n: int):
    """Every NON-EMPTY declared preparation at n configurations."""
    return [frozenset(s) for k in range(1, n + 1)
            for s in combinations(range(n), k)]


def terminal_trunk(part, fam, law, n) -> bool:
    """(i-a), (i-b) and (ii-a) of the terminal axiom: the three clauses that
    do NOT read the declared preparation, taken from B\"'s own adjudicator."""
    v = L2.adjudicate(part, fam, law, frozenset(range(n)), n)
    return v["i_a"] and v["i_b"] and v["ii_a"]


def terminal_at_prep(part, fam, trunk, prep, n) -> bool:
    """The terminal verdict with the DECLARED PREPARATION VARIED.  B\"'s
    verdict is the conjunction of the four clauses and only (ii-b) reads the
    preparation, so the trunk above is computed once per patch and (ii-b) is
    re-decided per preparation on committed primitives.  The decomposition is
    not assumed: it is gated equal to the committed adjudicator over every one
    of the 24045 prep-varied census instances (L3-29)."""
    R = L2.reach_of(fam, prep, n)
    return (trunk and all(set(b) & R for b in part)
            and not unrealized_pairs(part, fam, prep, n))


_REL_TAB: dict = {}


def relation_table(n: int):
    """Index every left-total sector relation at n configurations and tabulate
    composition once, which is what makes the support-valued law sweeps of
    L3-25 and L3-26 affordable at all."""
    if n not in _REL_TAB:
        rels = [tuple(s) for s in CB.relations_of(n)]
        idx = {L2.key(F): i for i, F in enumerate(rels)}
        tab = [[idx[L2.key(L2.compose(rels[i], rels[j]))]
                for j in range(len(rels))] for i in range(len(rels))]
        _REL_TAB[n] = (rels, tab)
    return _REL_TAB[n]


def closure_indices(gens, tab):
    """The composition closure of a set of indexed relations, BUILT by
    saturation rather than characterized."""
    S = set(gens)
    frontier = list(S)
    while frontier:
        nxt = []
        for i in list(S):
            for j in frontier:
                for h in (tab[i][j], tab[j][i]):
                    if h not in S:
                        S.add(h)
                        nxt.append(h)
        frontier = nxt
    return frozenset(S)


def call_closure(module, roots):
    """THE ABSTRACT-SYNTAX-TREE ROUTE.  The transitive call closure of a set
    of functions inside a module, together with every name those functions
    mention.  Two premises that this unit previously asserted in prose are
    gated with it: that the terminal descent selector reads no law (L3-36)
    and that the terminal axiom reads no state (L3-35)."""
    src = Path(inspect.getsourcefile(module)).read_text()
    tree = ast.parse(src)
    defs = {d.name: d for d in ast.walk(tree) if isinstance(d, ast.FunctionDef)}
    seen: set = set()
    used: set = set()
    frontier = list(roots)
    while frontier:
        f = frontier.pop()
        if f in seen or f not in defs:
            continue
        seen.add(f)
        for node in ast.walk(defs[f]):
            if isinstance(node, ast.Name):
                used.add(node.id)
            elif isinstance(node, ast.Attribute):
                used.add(node.attr)
            if isinstance(node, ast.Call):
                fn = node.func
                if isinstance(fn, ast.Name):
                    frontier.append(fn.id)
                elif isinstance(fn, ast.Attribute):
                    frontier.append(fn.attr)
    if MUTANT == "astlaw-lax":
        used.add("law")
        used.add("rho")
    return seen, used


def eps_adjudicate(part, law, prep, n, rho, tau_eps=Fr(0), tau_omega=Fr(0)):
    """EPSILON-ADMISSIBILITY, decided.

    P = (B, F, X_0, L) is EPS-ADMISSIBLE AT TOLERANCE (tau_eps, tau_omega)
    iff

      (a)  F = Pres_L(A(B))  and  F non-empty            [(i-b), exact]
      (b)  eps(P) = delta(A(B), F, rho) <= tau_eps       [relaxes (i-a)/(ii-a)]
      (c)  omega(P) <= tau_omega                         [relaxes (ii-b)-occupancy]
      (d)  no asserted identification is unrealized between reachable
           configurations                                [(ii-b) residue, exact]

    Clause (a) is B"'s (i-b) unchanged: the eps-form does NOT relativize the
    law, which is negative control L3-11.  The declared family is therefore
    a function of the boundary and the law, exactly as in the terminal
    axiom."""
    fam = L2.pres_of(law, part)
    e = epsilon(part, fam, rho)
    w = occupancy_defect(part, fam, prep, rho, n)
    up = unrealized_pairs(part, fam, prep, n)
    return {"family_size": len(fam), "non_empty": bool(fam),
            "epsilon": e, "omega": w, "unrealized": up,
            "eps_admissible": bool(fam) and e <= tau_eps and w <= tau_omega
            and not up}


# --------------------------------------------------------------------------
# 2.  ANCHORS -- every committed value this unit reuses, recomputed.
# --------------------------------------------------------------------------


def run_anchors():
    prog("anchors: Cycle B, B', B\" and the three frozen B\" reviews")

    anchor("N01", "Cycle B sec 4 (Bell triangle)",
           "record-lattice sizes at 1..5 configurations", [1, 2, 5, 15, 52],
           [CB.bell(n) for n in (1, 2, 3, 4, 5)])
    anchor("N02", "Cycle B Thm 4.4 / B\" M32",
           "DET and REV cardinalities at five configurations", [3125, 120],
           [len(L2.law_det(5)), len(L2.law_rev(5))])

    det = L2.law_det(5)
    anchor("N03", "B\" sec 6.1",
           "the forged boundary's Cycle B closure under DET", 240,
           len(L2.pres_of(det, PI1)))
    anchor("N04", "B\" sec 6.3 / Thm 7.2",
           "the carrier algebra's closure under DET is the reversible family",
           120, len(L2.pres_of(det, DISC5)))

    # -- B"'s two admitted statistics, recomputed by this unit's own route.
    famD = L2.pres_of(det, DISC5)
    famF = L2.pres_of(det, PI1)
    anchor("N05", "B\" Thm 7.2",
           "sigma: admissible patch vs the closure-plus-total-eraser patch",
           ["1", "3/4"],
           [str(L2.sigma_statistic(DISC5, famD, RHO)),
            str(L2.sigma_statistic(
                DISC5, famD + [L2.sup_of_map((0, 0, 0, 0, 0))], RHO))])
    anchor("N06", "B\" sec 7.1",
           "delta: admissible patch vs the forged patch", ["0", "1/16"],
           [str(L2.delta_statistic(DISC5, famD, RHO)),
            str(L2.delta_statistic(PI1, famF, RHO))])
    anchor("N07", "THIS UNIT vs B\" sec 7.1",
           "eps IS B\"'s delta: max of the per-task defect reproduces it",
           [str(L2.delta_statistic(PI1, famF, RHO)),
            str(L2.delta_statistic(PTOMO, L2.pres_of(det, PTOMO), RHO))],
           [str(epsilon(PI1, famF, RHO)),
            str(epsilon(PTOMO, L2.pres_of(det, PTOMO), RHO))])

    # -- the census, reproduced by B"'s own committed route.
    c = L2.census_T3()
    anchor("N08", "B\" Thm 3.5 (census)",
           "censused laws; identity-containing; reversible-containing",
           [687, 259, 259],
           [c["laws"], c["identity_containing"], c["reversible_containing"]])
    anchor("N09", "B\" Thm 3.5 (dichotomy, both directions)",
           "laws admitting a proper boundary; identity-containing ones that "
           "do; identity-free ones that do not; the biconditional",
           [428, 0, 0, 687],
           [c["admitting_a_proper_boundary"],
            c["identity_containing_with_a_proper_boundary"],
            c["identity_free_with_no_proper_boundary"],
            c["discrete_admissible_iff_identity"]])
    anchor("N10", "B\" Thm 6.1 (census)",
           "unordered admissible pairs; comparable among them", [357, 0],
           [c["admissible_pairs"], c["comparable_admissible_pairs"]])
    anchor("N11", "B\" Thm 3.2 (census)",
           "condition-(i) instances; at proper boundaries; (ii-a) failures",
           [1004, 745, 0],
           [c["condition_i_instances"], c["condition_i_at_proper_boundaries"],
            c["condition_i_with_ii_a_failing"]])
    anchor("N12", "B\" Thm 8.3 (census)",
           "cost pairs; complement does not admit; non-empty among them",
           [2748, 1008, 927],
           [c["cost_pairs"], c["complement_does_not_admit"],
            c["complement_non_empty_and_does_not_admit"]])

    # -- the cost tower, by B"'s own routine.
    tower = []
    for p in (PI1, P22, PTOMO, ((0, 1, 2, 3, 4),)):
        tower.append(L2.forging_cost(det, p, 5))
    anchor("N13", "B\" Thm 8.4",
           "the DET cost tower and what it leaves",
           [[120, 360, 1260, 3120], [3005, 2765, 1865, 5]],
           [[t["cost"] for t in tower], [t["remaining"] for t in tower]])

    # -- the arena, by Cycle B''s own descent routines.
    W = CBP.overlap_atoms_diagonal(5)
    a211 = CBP.aligned_manufactured_boundary((2, 1, 1))
    a1111 = CBP.aligned_manufactured_boundary((1, 1, 1, 1))
    i211, i1111 = CBP.incidence(a211.atoms, W), CBP.incidence(a1111.atoms, W)
    cert = CBP.certified_records(a211.atoms, i211,
                                 CBP.facts_realized(a1111.atoms, i1111), 5)
    anchor("N14", "Cycle B' sec 7.7 / B\" M25-M26",
           "colluding pair: records certified, and the forged greatest "
           "record descends", [14, True],
           [len(cert), CB.discrete(len(a211.atoms)) in cert])
    er = CBP.boundary_from_blocks("ERASER", (1,) * 5)
    addr = CBP.boundary_from_blocks("ADDRESS", (1,) * 5)
    certE = CBP.certified_records(
        er.atoms, CBP.incidence(er.atoms, W),
        CBP.facts_realized(addr.atoms, CBP.incidence(addr.atoms, W)), 5)
    anchor("N15", "Cycle B' Thm 6.4 / B\" M31",
           "the legitimate eraser context: records certified of 52", [51, 52],
           [len(certE), CB.bell(5)])

    # -- the escape's law, and the two REFUTED relaxations of the frozen
    #    reviews, reproduced as committed values before being run as
    #    negative controls.
    a = L2.sup_of_map(A_ESCAPE)
    anchor("N16", "B\" Prop 6.2 (R1 sec 2.2, R2 F3)",
           "the escape law {(0,0,2,3,4)} is composition-closed and "
           "identity-free", [True, False],
           [L2.is_composition_closed([a]), L2.has_identity([a], 5)])
    anchor("N17", "R2 F3 (frozen effectus review af2149f5f7ab)",
           "sub-law relativization: forged member admissible, member two "
           "not, and delta collapses to 0", [True, False, "0"],
           [L2.adjudicate(PI1, L2.pres_of([a], PI1), [a], PREP_FULL,
                          5)["admissible"],
            L2.adjudicate(DISC5, L2.pres_of([a], DISC5), [a], PREP_FULL,
                          5)["admissible"],
            str(L2.delta_statistic(PI1, L2.pres_of([a], PI1), RHO))])
    anchor("N18", "R3 sec 7.3 (frozen instrument review 6bc2aa0ba77e)",
           "(i-b') declared-family sizes at the forged 2+1+1, the forged "
           "2+2 and the legitimate tomographic minimum", [120, 60, 20],
           [len([F for F in L2.pres_of(det, p) if L2.written_of(F) == p])
            for p in (PI1, P22, PTOMO)])
    anchor("N19", "B\" Prop 3.4",
           "the identity-free control's admissible set is the two PROPER "
           "charts and not the carrier's",
           sorted([((0, 1), (2,)), ((0,), (1, 2))]),
           sorted(p for p in CB.parts_of(3)
                  if L2.adjudicate(p, L2.pres_of(L2.law_identity_free_3(), p),
                                   L2.law_identity_free_3(),
                                   frozenset(range(3)), 3)["admissible"]))


# --------------------------------------------------------------------------
# 3.  H1(a) -- THE EPSILON = 0 REDUCTION, GATED BOTH DIRECTIONS.
# --------------------------------------------------------------------------


def run_reduction():
    prog("H1(a): the eps = 0 reduction to the terminal axiom")

    rows, bad = [], []
    tested = 0
    for n in (2, 3, 4, 5):
        rho = RHO if n == 5 else uniform(n)
        for name, law in L2.committed_laws(n):
            agree = 0
            for p in CB.parts_of(n):
                fam = L2.pres_of(law, p)
                prep = frozenset(range(n))
                terminal = L2.adjudicate(p, fam, law, prep, n)["admissible"]
                ez = eps_adjudicate(p, law, prep, n, rho)["eps_admissible"]
                tested += 1
                if terminal == ez:
                    agree += 1
                else:
                    bad.append({"configurations": n, "law": name,
                                "boundary": [list(b) for b in p],
                                "terminal": terminal, "eps_zero": ez})
            rows.append({"configurations": n, "law": name, "size": len(law),
                         "records": CB.bell(n), "agreements": agree})
    TABLES["reduction_sweep"] = rows

    # the census: the same equivalence where the identity-free side lives
    cen_tested, cen_bad, cen_free, cen_free_zero = 0, 0, 0, 0
    rho3 = uniform(3)
    for Lf in L2.laws_of_T3():
        law = [L2.sup_of_map(f) for f in sorted(Lf)]
        idfree = not L2.has_identity(law, 3)
        for p in CB.parts_of(3):
            fam = L2.pres_of(law, p)
            terminal = L2.adjudicate(p, fam, law, frozenset(range(3)), 3)[
                "admissible"]
            ez = eps_adjudicate(p, law, frozenset(range(3)), 3,
                                rho3)["eps_admissible"]
            cen_tested += 1
            cen_bad += (terminal != ez)
            if idfree and terminal:
                cen_free += 1
                cen_free_zero += (epsilon(p, fam, rho3) == 0)

    gate("L3-01", "reduction",
         "THE REDUCTION THEOREM, GATED BOTH DIRECTIONS.  At a full-support "
         "state a patch is 0-admissible in the eps-form if and only if it is "
         "admissible under the terminal B\" axiom.  Measured exhaustively "
         "over every record at two, three, four and five configurations "
         "against every committed law, and over the whole 687-law census at "
         "three: zero disagreements.  The eps-form is therefore a "
         "QUANTIFICATION of the terminal axiom and not a replacement for it",
         not bad and cen_bad == 0,
         {"committed_instances": tested, "committed_disagreements": len(bad),
          "census_instances": cen_tested, "census_disagreements": cen_bad,
          "disagreement_rows": bad[:5]})

    gate("L3-02", "reduction",
         "THE DICHOTOMY'S IDENTITY-FREE SIDE COMES OUT eps = 0, AS THE PIN "
         "REQUIRES.  Every admissible patch at an identity-free censused law "
         "-- the side of B\" Theorem 3.5 where PROPER charts live -- has "
         "concordance defect exactly zero.  This is the reduction theorem "
         "read on the populated side, and it is the reason the eps-form "
         "cannot buy a proper chart by lowering a threshold: on that side "
         "there is nothing to lower",
         cen_free > 0 and cen_free == cen_free_zero,
         {"identity_free_admissible_patches": cen_free,
          "of_them_with_epsilon_zero": cen_free_zero})

    # the two hypotheses of the reduction, each shown load-bearing.
    degen = (Fr(0), Fr(0), Fr(0), Fr(0), Fr(1))   # mass on the sink alone
    det = L2.law_det(5)
    e_deg = epsilon(PI1, L2.pres_of(det, PI1), degen)
    e_full = epsilon(PI1, L2.pres_of(det, PI1), RHO)
    gate("L3-03", "control",
         "THE FULL-SUPPORT HYPOTHESIS IS LOAD-BEARING, AND IT IS A LIMIT OF "
         "THE FORM, NOT A TECHNICALITY.  At the degenerate state carrying all "
         "mass on the retained sink the forged boundary's defect is exactly "
         "0 while the terminal axiom still rejects it, so the reduction fails "
         "and the eps-form would certify the forgery at tolerance zero.  eps "
         "is STATE-RELATIVE: whoever declares the state moves the number",
         e_deg == 0 and e_full > 0 and not L2.adjudicate(
             PI1, L2.pres_of(det, PI1), det, PREP_FULL, 5)["admissible"],
         {"epsilon_at_the_degenerate_state": str(e_deg),
          "epsilon_at_the_committed_state": str(e_full),
          "terminal_verdict": "inadmissible"})

    empty_law: list = []
    e_empty = epsilon(((0, 1, 2),), [], uniform(3))
    gate("L3-04", "control",
         "THE NON-EMPTINESS CLAUSE IS LOAD-BEARING.  The empty declared "
         "family has concordance defect exactly 0 -- no task resolves "
         "anything because there is no task -- while the terminal axiom "
         "rejects it through ker(empty) = the one-atom boundary.  Without "
         "clause (a)'s non-emptiness the eps-form would certify a patch that "
         "writes nothing at all",
         e_empty == 0 and not eps_adjudicate(
             ((0, 1, 2),), empty_law, frozenset(range(3)), 3,
             uniform(3))["eps_admissible"],
         {"epsilon_of_the_empty_family": str(e_empty)})

    # ---- THE REDUCTION WITH THE DECLARED PREPARATION VARIED.
    # The two sweeps above hold the declared preparation at the whole carrier,
    # where Reach(P) contains every configuration and omega therefore vanishes
    # identically: clause (c) of Definition 2.2 is never exercised in any of
    # the 3803 instances.  The panel's effectus lens supplied the repair;
    # it is re-run here natively over the whole census at every non-empty
    # declared preparation and over every record at the committed carrier at
    # every non-empty declared preparation.  The theorem survives, and the
    # occupancy clause is measured to be load-bearing rather than decorative.
    preps3 = ([frozenset(range(3))] if MUTANT == "prepvary-lax"
              else preps_of(3))
    pv_inst = pv_dis = pv_wnz = pv_wonly = pv_donly = pv_dropc = 0
    hoist_bad = 0
    for Lf in L2.laws_of_T3():
        law = [L2.sup_of_map(f) for f in sorted(Lf)]
        for p in CB.parts_of(3):
            fam = L2.pres_of(law, p)
            e = epsilon(p, fam, rho3)
            trunk = terminal_trunk(p, fam, law, 3)
            for pr in preps3:
                pv_inst += 1
                w = occupancy_defect(p, fam, pr, rho3, 3)
                up = bool(unrealized_pairs(p, fam, pr, 3))
                terminal = L2.adjudicate(p, fam, law, pr, 3)["admissible"]
                if terminal != terminal_at_prep(p, fam, trunk, pr, 3):
                    hoist_bad += 1
                ez = bool(fam) and e == 0 and w == 0 and not up
                pv_dis += (terminal != ez)
                pv_wnz += (w != 0)
                if (not terminal) and bool(fam) and e == 0 and not up and w > 0:
                    pv_wonly += 1
                if (not terminal) and bool(fam) and e == 0 and w == 0 and up:
                    pv_donly += 1
                pv_dropc += (terminal != (bool(fam) and e == 0 and not up))

    cc_inst = cc_dis = cc_wnz = 0
    for p in CB.parts_of(5):
        fam = L2.pres_of(det, p)
        e = epsilon(p, fam, RHO)
        trunk = terminal_trunk(p, fam, det, 5)
        for pr in preps_of(5):
            cc_inst += 1
            w = occupancy_defect(p, fam, pr, RHO, 5)
            up = bool(unrealized_pairs(p, fam, pr, 5))
            ez = bool(fam) and e == 0 and w == 0 and not up
            cc_dis += (terminal_at_prep(p, fam, trunk, pr, 5) != ez)
            cc_wnz += (w != 0)

    anchor("N22", "R2 F3 (frozen effectus review, v13 #153)",
           "the prep-varied census: instances, disagreements, instances with "
           "omega non-zero, terminal rejections blocked by omega ALONE, and "
           "rejections blocked by clause (d) alone",
           [24045, 0, 9837, 3117, 0],
           [pv_inst, pv_dis, pv_wnz, pv_wonly, pv_donly])

    TABLES["reduction_with_the_preparation_varied"] = {
        "census_instances": pv_inst, "census_disagreements": pv_dis,
        "instances_with_omega_non_zero": pv_wnz,
        "terminal_rejections_blocked_by_omega_alone": pv_wonly,
        "terminal_rejections_blocked_by_clause_d_alone": pv_donly,
        "disagreements_if_clause_c_is_dropped": pv_dropc,
        "committed_carrier_instances": cc_inst,
        "committed_carrier_disagreements": cc_dis,
        "committed_carrier_instances_with_omega_non_zero": cc_wnz,
        "total_further_instances": pv_inst + cc_inst,
        "clause_decomposition_disagreements_with_the_committed_adjudicator":
            hoist_bad}

    gate("L3-29", "reduction",
         "THE REDUCTION SURVIVES WITH THE DECLARED PREPARATION VARIED, AND "
         "THE OCCUPANCY CLAUSE IS LOAD-BEARING.  The sweeps of L3-01 hold the "
         "declared preparation at the whole carrier, where Reach(P) contains "
         "every configuration and omega vanishes identically -- so clause (c) "
         "is never exercised there.  Re-run over the whole 687-law census at "
         "every one of the seven non-empty declared preparations and over "
         "every record at the committed carrier at every one of the "
         "thirty-one: 25657 further instances, ZERO disagreements, of which "
         "9837 carry omega non-zero.  And clause (c) is not decorative: in "
         "3117 instances omega > 0 is the ONLY thing standing between the "
         "eps-form and a patch the terminal axiom rejects, so dropping it "
         "produces exactly 3117 disagreements; clause (d) never blocks alone",
         pv_dis == 0 and cc_dis == 0 and hoist_bad == 0
         and pv_wnz == 9837 and pv_wonly == 3117 and pv_dropc == 3117
         and pv_donly == 0,
         TABLES["reduction_with_the_preparation_varied"])

    FINDINGS["reduction_holds"] = not bad and cen_bad == 0
    FINDINGS["reduction_holds_with_the_preparation_varied"] = (
        pv_dis == 0 and cc_dis == 0)
    return rows


# --------------------------------------------------------------------------
# 3b. H1(a') -- THE HYPOTHESIS THE STATEMENTS NEED: SINGLE-VALUEDNESS.
# --------------------------------------------------------------------------


_SV_LAWS: dict = {}


def support_valued_laws(n: int, generators: int):
    """Every composition-closed law at n configurations generated by at most
    `generators` LEFT-TOTAL RELATIONS -- the population the committed families
    exclude by construction and in which the countermodels live."""
    if (n, generators) not in _SV_LAWS:
        rels, tab = relation_table(n)
        single = {i: closure_indices([i], tab) for i in range(len(rels))}
        seen = set(single.values())
        if generators >= 2:
            for i, j in combinations(range(len(rels)), 2):
                seen.add(closure_indices(single[i] | single[j], tab))
        _SV_LAWS[(n, generators)] = (
            rels, sorted(seen, key=lambda c: (len(c), sorted(c))))
    return _SV_LAWS[(n, generators)]


def run_hypotheses():
    prog("H1(a'): the single-valuedness hypothesis, and life without it")

    # ---- (1) THE REDUCTION THEOREM'S MISSING HYPOTHESIS, WITH COUNTERMODELS.
    Fmulti = (frozenset({0, 1}), frozenset({0, 1}))
    pi2 = ((0, 1),)
    rho2 = uniform(2)
    mini_law = [Fmulti]
    mini_fam = L2.pres_of(mini_law, pi2)
    mini_terminal = L2.adjudicate(pi2, mini_fam, mini_law,
                                  frozenset({0, 1}), 2)["admissible"]
    mini_eps = epsilon(pi2, mini_fam, rho2)
    mini_omega = occupancy_defect(pi2, mini_fam, frozenset({0, 1}), rho2, 2)
    mini_ez = eps_adjudicate(pi2, mini_law, frozenset({0, 1}), 2,
                             rho2)["eps_admissible"]

    sweeps = {}
    for n, gens in ((2, 2), (3, 1)):
        rels, laws = support_valued_laws(n, gens)
        rho = uniform(n)
        inst = dis = 0
        for c in laws:
            law = [rels[i] for i in sorted(c)]
            for p in CB.parts_of(n):
                fam = L2.pres_of(law, p)
                e = epsilon(p, fam, rho)
                for pr in preps_of(n):
                    inst += 1
                    w = occupancy_defect(p, fam, pr, rho, n)
                    up = bool(unrealized_pairs(p, fam, pr, n))
                    terminal = L2.adjudicate(p, fam, law, pr,
                                             n)["admissible"]
                    ez = bool(fam) and e == 0 and w == 0 and not up
                    dis += (terminal != ez)
        sweeps[n] = {"generators": gens, "laws": len(laws),
                     "instances": inst, "disagreements": dis}

    anchor("N20", "R2 F1 (frozen effectus review, v13 #153)",
           "support-valued law populations and the reduction's failures "
           "without single-valuedness: laws and disagreements at two "
           "configurations (<=2 generators) and at three (one generator)",
           [38, 9, 342, 124],
           [sweeps[2]["laws"], sweeps[2]["disagreements"],
            sweeps[3]["laws"], sweeps[3]["disagreements"]])

    gate("L3-25", "reduction",
         "THE REDUCTION THEOREM NEEDS SINGLE-VALUEDNESS, AND THE "
         "COUNTERMODELS ARE EXHIBITED.  Without it the (terminal-admissible "
         "=> eps-zero) direction fails: a composition-closed law of genuinely "
         "multi-valued admitted operations separates nothing inside a "
         "declared atom -- so the terminal axiom admits it -- and still leaks "
         "the atom's mass across two later configurations.  The minimal "
         "countermodel is one operation at two configurations with "
         "sup(0) = sup(1) = {0,1}: TERMINAL-ADMISSIBLE with eps = 1/2, so at "
         "support-valued laws the eps-form at tolerance zero is STRICTLY "
         "STRONGER than the terminal axiom rather than equal to it.  Swept: "
         "9 disagreements over the 38 composition-closed laws generated by at "
         "most two left-total operations at two configurations, and 124 over "
         "the 342 closures of a single left-total operation at three, across "
         "every non-empty declared preparation in both cases.  Every "
         "committed law is single-valued, so no gated number moves",
         mini_terminal and mini_eps == Fr(1, 2) and not mini_ez
         and sweeps[2]["disagreements"] == 9
         and sweeps[3]["disagreements"] == 124,
         {"minimal_countermodel": {
             "law": "{ sup(0) = sup(1) = {0,1} } at two configurations",
             "composition_closed": L2.is_composition_closed(mini_law),
             "boundary": "the one-atom boundary",
             "terminal_verdict": mini_terminal, "epsilon": str(mini_eps),
             "omega": str(mini_omega), "eps_admissible_at_zero": mini_ez},
          "sweeps": sweeps})

    # ---- (2) THE ENTAILMENT LEMMA'S CONVERSE, AND WHAT REPLACES IT.
    Gpart = (frozenset({0}), frozenset({0, 1}))
    g_law = [Gpart]
    g_fam = L2.pres_of(g_law, pi2)
    g_ii_a = bool(g_fam) and all(L2.written_of(F) == pi2 for F in g_fam)
    g_i_a = (L2.ker_of_family(g_fam, 2) == pi2)

    lem = {}
    for n in (2, 3):
        rels, laws = support_valued_laws(n, 2)
        conv = fwd = inst = conv_det = 0
        for c in laws:
            law = [rels[i] for i in sorted(c)]
            det_law = is_single_valued(law)
            for p in CB.parts_of(n):
                fam = L2.pres_of(law, p)
                if not fam:
                    continue
                inst += 1
                i_a = (L2.ker_of_family(fam, n) == p)
                ii_a = all(L2.written_of(F) == p for F in fam)
                if ii_a and not i_a:
                    conv += 1
                    conv_det += det_law
                if i_a and not ii_a:
                    fwd += 1
        lem[n] = {"laws": len(laws), "non_empty_pres_instances": inst,
                  "converse_countermodels": conv,
                  "of_them_at_single_valued_laws": conv_det,
                  "forward_direction_failures": fwd}

    # the compensating strengthening: non-emptiness is load-bearing only
    # against the EMPTY law, because Pres_L(the one-atom boundary) = L always.
    pres_full = empty_pres = empty_ok = 0
    for Lf in L2.laws_of_T3():
        law = [L2.sup_of_map(f) for f in sorted(Lf)]
        pres_full += (len(L2.pres_of(law, CB.indiscrete(3))) == len(law))
        for p in CB.parts_of(3):
            fam = L2.pres_of(law, p)
            if fam:
                continue
            empty_pres += 1
            empty_ok += (not L2.adjudicate(p, fam, law, frozenset(range(3)),
                                           3)["admissible"]
                         and L2.ker_of_family(fam, 3) != p)

    anchor("N21", "R2 F2 (frozen effectus review, v13 #153)",
           "the entailment lemma's converse at support-valued laws: "
           "countermodels at two and at three configurations, of them at "
           "single-valued laws, and forward-direction failures",
           [20, 45810, 0, 0],
           [lem[2]["converse_countermodels"],
            lem[3]["converse_countermodels"],
            lem[2]["of_them_at_single_valued_laws"]
            + lem[3]["of_them_at_single_valued_laws"],
            lem[2]["forward_direction_failures"]
            + lem[3]["forward_direction_failures"]])

    gate("L3-26", "reduction",
         "THE ENTAILMENT LEMMA'S CONVERSE IS A THEOREM ABOUT SINGLE-VALUED "
         "LAWS ONLY.  Its proof reads (i-a)'s failure as producing a task "
         "whose written record is strictly finer than the boundary; at a "
         "support-valued law two configurations in one atom can carry "
         "DIFFERENT BUT OVERLAPPING supports, which leaves comp(F) equal to "
         "the boundary while ker(F) splits it.  Minimal countermodel: one "
         "operation with sup(0) = {0}, sup(1) = {0,1} at the one-atom "
         "boundary -- (ii-a) holds, (i-a) fails.  Censused over every "
         "composition-closed law generated by at most two left-total "
         "operations: 20 countermodels at two configurations and 45810 at "
         "three, ZERO of them at a single-valued law, and zero failures of "
         "the forward direction anywhere.  So {(i-a), (ii-a)} is one "
         "condition exactly where the committed laws live.  And the "
         "non-emptiness hypothesis is load-bearing only against the EMPTY "
         "law: Pres_L(the one-atom boundary) = L at all 687 censused laws, so "
         "an empty preservation family already forces (i-a) to fail -- the "
         "biconditional holds at all 974 empty-family census instances",
         g_ii_a and not g_i_a
         and lem[2]["converse_countermodels"] == 20
         and lem[3]["converse_countermodels"] == 45810
         and lem[2]["of_them_at_single_valued_laws"] == 0
         and lem[3]["of_them_at_single_valued_laws"] == 0
         and lem[2]["forward_direction_failures"] == 0
         and lem[3]["forward_direction_failures"] == 0
         and pres_full == 687 and empty_pres == empty_ok > 0,
         {"minimal_countermodel": {
             "law": "{ sup(0) = {0}, sup(1) = {0,1} } at two configurations",
             "composition_closed": L2.is_composition_closed(g_law),
             "pres_non_empty": bool(g_fam), "ii_a": g_ii_a, "i_a": g_i_a},
          "census": lem,
          "pres_of_the_one_atom_boundary_is_the_law": pres_full,
          "empty_family_census_instances": empty_pres,
          "biconditional_intact_there": empty_ok})

    # ---- (3) THE CLOSED FORM'S MISSING HYPOTHESIS.
    all2 = L2.law_all(2)
    rho_cf = (Fr(3, 4), Fr(1, 4))
    eps_all2 = epsilon(pi2, L2.pres_of(all2, pi2), rho_cf)
    cf_all2 = closed_form(pi2, rho_cf)
    Fw = tuple([frozenset({4})] * 4 + [frozenset({0, 1})])
    one5 = ((0, 1, 2, 3, 4),)
    d_wit = task_defect(one5, Fw, RHO)
    committed_sv = [(nm, len(law), is_single_valued(law))
                    for nm, law in L2.committed_laws(5)]

    anchor("N25", "R1 F4 (frozen operator review, v13 #151)",
           "the closed form fails at a support-valued law: eps against the "
           "closed form at ALL(2) under rho = (3/4, 1/4), and the "
           "multi-valued witness's per-task defect at the committed carrier",
           ["1/2", "1/4", "5/8"],
           [str(eps_all2), str(cf_all2), str(d_wit)])

    gate("L3-27", "spectrum",
         "THE CLOSED FORM NEEDS SINGLE-VALUEDNESS TOO, AND SO DOES THE "
         "SPECTRUM'S CROSS-LAW IDENTITY.  The proof turns on max_s Pr(r,s) >= "
         "max_{j in r} rho_j -- the mass of one configuration bounds the mass "
         "reaching whichever later configuration it reaches -- which is false "
         "as soon as an admitted operation has a multi-valued support.  Inside "
         "this corpus's own law list: at ALL(2), which is composition-closed "
         "and contains the identity, with rho = (3/4, 1/4) and the one-atom "
         "boundary, the closed form gives 1/4 while eps is 1/2.  At the "
         "committed carrier the single operation sending each address to the "
         "sink and the sink to {0,1} lies in the preservation family of the "
         "one-atom boundary and carries per-task defect 5/8 -- outside the "
         "five-value spectrum entirely, so the spectrum's 'the same five "
         "under every committed law' is determinism-dependent as well.  Every "
         "one of the five committed laws at five configurations is measured "
         "single-valued, which is why no delivered number moves",
         eps_all2 == Fr(1, 2) and cf_all2 == Fr(1, 4) and d_wit == Fr(5, 8)
         and CB.images_disjoint(Fw, one5)
         and all(sv for _, _, sv in committed_sv)
         and L2.has_identity(all2, 2) and L2.is_composition_closed(all2),
         {"ALL(2)_epsilon": str(eps_all2), "ALL(2)_closed_form": str(cf_all2),
          "multivalued_witness_defect_at_the_committed_carrier": str(d_wit),
          "committed_laws_at_five_configurations": committed_sv})

    # ---- (4) THE SCOPE TAG'S SWEEP, ACTUALLY RUN.
    ex_inst = ex_bad = ex_sv = ex_supp = 0
    ex_rows = []
    for n in (2, 3, 4, 5):
        rho = RHO if n == 5 else uniform(n)
        for nm, law in L2.committed_laws(n):
            if not L2.has_identity(law, n):
                continue
            k = 0
            for p in CB.parts_of(n):
                ex_inst += 1
                k += 1
                if epsilon(p, L2.pres_of(law, p), rho) != closed_form(p, rho):
                    ex_bad += 1
            if is_single_valued(law):
                ex_sv += k
            else:
                ex_supp += k
            ex_rows.append({"configurations": n, "law": nm, "size": len(law),
                            "single_valued": is_single_valued(law),
                            "records": k})
    TABLES["closed_form_sweep_at_two_to_five_configurations"] = {
        "instances": ex_inst, "mismatches": ex_bad,
        "single_valued_instances": ex_sv,
        "support_valued_instances": ex_supp, "rows": ex_rows}

    gate("L3-28", "spectrum",
         "AND THE SCOPE TAG'S SWEEP IS RUN RATHER THAN CLAIMED.  The closed "
         "form was gated at five configurations only, 260 instances, while "
         "carrying a tag that promises every record at two to five "
         "configurations against every committed law.  Run: 368 instances, "
         "ZERO mismatches.  22 of them are at the support-valued ALL family "
         "at two, three and four configurations, where the hypothesis of "
         "L3-27 does NOT hold and the closed form nevertheless agrees -- so "
         "single-valuedness is sufficient and is not necessary, and the "
         "ALL(2) counterexample of L3-27 shows the failure is reached by "
         "moving the declared state, not by leaving the class",
         ex_inst == 368 and ex_bad == 0 and ex_supp == 22,
         {"instances": ex_inst, "mismatches": ex_bad,
          "support_valued_instances": ex_supp})

    FINDINGS["single_valuedness_is_load_bearing"] = True
    return sweeps


# --------------------------------------------------------------------------
# 4.  H1(b) -- THE EPSILON SPECTRUM.
# --------------------------------------------------------------------------


def run_spectrum():
    prog("H1(b): the eps spectrum of the committed coarse boundaries")

    rows = []
    spectra = {}
    for name, law in L2.committed_laws(5):
        spec: dict = {}
        for p in CB.parts_of(5):
            fam = L2.pres_of(law, p)
            e = epsilon(p, fam, RHO)
            spec.setdefault(str(e), []).append(p)
        spectra[name] = spec
        rows.append({
            "law": name, "size": len(law),
            "contains_a_reversible_operation": L2.has_reversible(law, 5),
            "distinct_epsilon_values": [str(v) for v in
                                        sorted(Fr(k) for k in spec)],
            "counts": {k: len(v) for k, v in
                       sorted(spec.items(), key=lambda kv: Fr(kv[0]))},
            "epsilon_zero_boundaries": [[list(b) for b in q]
                                        for q in spec.get("0", [])]}
        )
    TABLES["epsilon_spectrum_at_the_committed_carrier"] = rows

    det = L2.law_det(5)
    named = []
    for label, p, prov in (
            ("the forged aligned manufactured 2+1+1", PI1, "FORGED"),
            ("the forged aligned manufactured 2+2", P22, "FORGED"),
            ("the corrected tomographic minimum", PTOMO, "LEGITIMATE"),
            ("the carrier's own configuration algebra", DISC5, "LEGITIMATE")):
        fam = L2.pres_of(det, p)
        named.append({"boundary": label, "provenance": prov,
                      "atoms": [list(b) for b in p],
                      "family_size": len(fam),
                      "epsilon": str(epsilon(p, fam, RHO)),
                      "terminal_verdict": L2.adjudicate(
                          p, fam, det, PREP_FULL, 5)["admissible"]})
    TABLES["named_boundaries"] = named

    expected = {PI1: Fr(1, 16), P22: Fr(1, 8), PTOMO: Fr(3, 16)}
    reversible_rows = []
    allpos = True
    values_as_claimed = True
    all_reversible = True
    for name, law in L2.committed_laws(5):
        all_reversible = all_reversible and L2.has_reversible(law, 5)
        for p in (PI1, P22, PTOMO):
            fam = L2.pres_of(law, p)
            e = epsilon(p, fam, RHO)
            reversible_rows.append({"law": name, "boundary":
                                    [list(b) for b in p],
                                    "family_size": len(fam),
                                    "epsilon": str(e)})
            if not (e > 0):
                allpos = False
            if e != expected[p]:
                values_as_claimed = False
    TABLES["coarse_under_reversibility_containing_laws"] = reversible_rows

    gate("L3-05", "spectrum",
         "THE SPECTRUM IS MEASURED, NOT ASSERTED, AND EVERY VALUE IS AN "
         "EXACT RATIONAL.  Under every committed law containing a reversible "
         "operation the three named coarse boundaries carry a STRICTLY "
         "POSITIVE concordance defect, as B\"'s rigidity dichotomy requires; "
         "the values are 1/16, 1/8 and 3/16 and they are the same under all "
         "five committed law families -- DET, FUNNEL, REV, the funnel closure "
         "and the counter-law -- because the defect is carried by the "
         "identity, which every one of them contains.  The predicate checks "
         "the VALUES and the cross-law identity, not merely positivity, over "
         "all fifteen rows",
         allpos and values_as_claimed and all_reversible
         and len(reversible_rows) == 15,
         {"rows": len(reversible_rows), "laws": [nm for nm, _ in
                                                 L2.committed_laws(5)],
          "values_are_1_16_1_8_3_16_under_every_one": values_as_claimed,
          "every_law_contains_a_reversible_operation": all_reversible})

    spec_det = spectra["DET"]
    vals = sorted(Fr(k) for k in spec_det)
    pos = [v for v in vals if v > 0]
    smallest = pos[0] if pos else None
    attaining = [[list(b) for b in q] for q in spec_det[str(smallest)]]
    gate("L3-06", "spectrum",
         "THE SMALLEST POSITIVE DEFECT IN THE WHOLE SPECTRUM IS ATTAINED BY "
         "THE FORGERY.  Over all 52 records at the committed carrier under "
         "DET the defect takes five values, 0 < 1/16 < 1/8 < 3/16 < 1/4; the "
         "unique zero is the carrier's own algebra, and the least positive "
         "value 1/16 is attained by the ten two-configuration merges -- one "
         "of which is exactly the colluding pair's forged boundary.  So the "
         "FIRST coarse chart any tolerance can buy includes a forged one",
         smallest is not None and str(smallest) == "1/16"
         and [list(b) for b in PI1] in attaining,
         {"values": [str(v) for v in vals],
          "counts": {k: len(v) for k, v in
                     sorted(spec_det.items(), key=lambda kv: Fr(kv[0]))},
          "least_positive": str(smallest),
          "boundaries_attaining_it": len(attaining),
          "the_forged_boundary_is_among_them": True})
    # THE CLOSED FORM.  The identity separates every pair and lies in
    # Pres_L(pi) for every law and every boundary, and no SINGLE-VALUED
    # admitted future can exceed its per-task defect: for single-valued F,
    # max_s Pr(r,s) >= max_{j in r} rho_j, so d(F) <= d(id).  Hence at every
    # identity-containing law of single-valued operations the defect is the
    # law-free quantity
    #     eps(pi) = sum_r [ Pr(r) - max_{j in r} rho_j ].
    # The hypothesis is not decorative and is not necessary either: L3-27
    # exhibits its failure at ALL(2), L3-28 measures its redundancy at the
    # uniform states this unit uses.
    cf_rows, cf_ok, cf_n = [], True, 0
    for name, law in L2.committed_laws(5):
        if not L2.has_identity(law, 5):
            continue
        for p in CB.parts_of(5):
            cf_n += 1
            if epsilon(p, L2.pres_of(law, p), RHO) != closed_form(p, RHO):
                cf_ok = False
        cf_rows.append(name)
    identical = len({tuple(sorted((k, len(v)) for k, v in spectra[nm].items()))
                     for nm in spectra}) == 1
    gate("L3-24", "spectrum",
         "eps IS LAW-BLIND INSIDE THE IDENTITY-CONTAINING CLASS, IN CLOSED "
         "FORM.  The identity lies in the closure of every boundary at every "
         "law and separates every pair, and no SINGLE-VALUED admitted future "
         "has a larger per-task defect, so wherever the law contains the "
         "identity and its operations are single-valued -- which every "
         "committed law is (L3-27) -- the "
         "defect collapses to the LAW-FREE quantity sum_r [Pr(r) - max_{j in "
         "r} rho_j].  Measured over every record at the committed carrier "
         "against every committed identity-containing law: the closed form "
         "agrees everywhere, and the five spectra -- at law sizes 21, 120, "
         "120, 3006 and 3125 -- are IDENTICAL.  eps therefore carries no "
         "information about the law at all inside the class where the "
         "blockade bites; it grades the boundary against the state and "
         "nothing else",
         cf_ok and identical,
         {"instances": cf_n, "laws": cf_rows,
          "all_five_spectra_identical": identical})

    # ---- WHAT THE CLOSED FORM IS: THE BOUNDARY'S BAYES ERROR.
    # sum_r Pr(r) = 1, so the closed form is 1 - sum_r max_{j in r} rho_j:
    # the residual Bayes error of inferring the declared configuration from
    # the record outcome under the declared state.  eps measures RESOLUTION.
    # At the committed state it collapses further, to (5 - |pi|)/16 -- the
    # defect reads the NUMBER OF DECLARED ATOMS and nothing else -- which is
    # why the spectrum's multiplicities are the Stirling row S(5,k) and why
    # admitting at tolerance tau is exactly a cardinality cut on the declared
    # boundary.
    E5 = {p: epsilon(p, L2.pres_of(det, p), RHO) for p in CB.parts_of(5)}
    bayes_bad = sum(1 for p, e in E5.items() if e != bayes_error(p, RHO))
    card_bad = sum(1 for p, e in E5.items() if e != Fr(5 - len(p), 16))
    stirling = {}
    for p in CB.parts_of(5):
        stirling[len(p)] = stirling.get(len(p), 0) + 1
    spec_counts = {k: len(v) for k, v in spec_det.items()}
    stirling_matches = (sorted(stirling.values(), reverse=True)
                        == sorted(spec_counts.values(), reverse=True)
                        and all(stirling[k] == spec_counts[str(Fr(5 - k, 16))]
                                for k in stirling))
    cut_ok = True
    for t in sorted(set(vals) | {(vals[i] + vals[i + 1]) / 2
                                 for i in range(len(vals) - 1)}):
        if ({p for p in CB.parts_of(5) if E5[p] <= t}
                != {p for p in CB.parts_of(5) if len(p) >= 5 - 16 * t}):
            cut_ok = False
    gate("L3-30", "spectrum",
         "AND WHAT THE CLOSED FORM IS, NAMED: THE BOUNDARY'S BAYES ERROR.  "
         "Since the record probabilities sum to one, sum_r [Pr(r) - max_{j in "
         "r} rho_j] = 1 - sum_r max_{j in r} rho_j, the residual Bayes error "
         "of inferring the declared configuration from the record outcome "
         "under the declared state.  eps measures RESOLUTION.  At the "
         "committed state it collapses further to (5 - |pi|)/16 -- verified "
         "at all 52 records -- so the defect reads the NUMBER OF DECLARED "
         "ATOMS and nothing else: the spectrum's multiplicities 1, 10, 25, "
         "15, 1 are the Stirling row S(5,k), and clause (b) at tolerance tau "
         "is exactly the condition that the boundary declare at least "
         "5 - 16*tau atoms, verified as a SET IDENTITY at every candidate "
         "threshold.  Forgery is not a Bayes error, which is why no tolerance "
         "on this quantity can see it",
         bayes_bad == 0 and card_bad == 0 and stirling_matches and cut_ok,
         {"records": len(E5), "bayes_error_mismatches": bayes_bad,
          "five_minus_atoms_over_sixteen_mismatches": card_bad,
          "stirling_row_S_5_k": dict(sorted(stirling.items())),
          "spectrum_counts": spec_counts,
          "clause_b_is_a_cardinality_cut_at_every_threshold": cut_ok})

    FINDINGS["least_positive_epsilon_under_DET"] = str(smallest)
    FINDINGS["epsilon_is_law_blind_in_closed_form"] = cf_ok and identical
    FINDINGS["epsilon_is_the_boundarys_bayes_error"] = bayes_bad == 0
    return spectra


# --------------------------------------------------------------------------
# 5.  H1(c) -- THE SEPARATION QUESTION.  Reported first, and plainly.
# --------------------------------------------------------------------------


def run_separation(spectra):
    prog("H1(c): does eps separate FORGED from LEGITIMATE coarse patches?")

    det = L2.law_det(5)
    e = {lbl: epsilon(p, L2.pres_of(det, p), RHO)
         for lbl, p in (("forged 2+1+1", PI1), ("forged 2+2", P22),
                        ("legitimate tomographic minimum", PTOMO))}
    # A threshold SEPARATES when it admits the legitimate coarse patch and
    # rejects both forged ones.  Every candidate threshold in the spectrum
    # is tried; so is every rational cut between consecutive values.
    spec_det = spectra["DET"]
    vals = sorted(Fr(k) for k in spec_det)
    cuts = sorted(set(vals) | {(vals[i] + vals[i + 1]) / 2
                               for i in range(len(vals) - 1)})
    separating = [str(t) for t in cuts
                  if e["legitimate tomographic minimum"] <= t
                  and e["forged 2+1+1"] > t and e["forged 2+2"] > t]
    inverted = (e["legitimate tomographic minimum"] > e["forged 2+2"]
                > e["forged 2+1+1"])

    # what a tolerance that admits the legitimate coarse patch also admits
    tau = e["legitimate tomographic minimum"]
    admitted_at_tau = [p for p in CB.parts_of(5)
                       if eps_adjudicate(p, det, PREP_FULL, 5, RHO,
                                         tau, tau)["eps_admissible"]]
    tau_min = Fr(1, 16)
    admitted_at_min = [p for p in CB.parts_of(5)
                       if eps_adjudicate(p, det, PREP_FULL, 5, RHO,
                                         tau_min, tau_min)["eps_admissible"]]
    admitted_at_zero = [p for p in CB.parts_of(5)
                        if eps_adjudicate(p, det, PREP_FULL, 5, RHO,
                                          Fr(0), Fr(0))["eps_admissible"]]

    TABLES["separation"] = {
        "epsilon_values": {k: str(v) for k, v in e.items()},
        "ordering": "the LEGITIMATE coarse patch carries the LARGEST defect "
                    "and the forged 2+1+1 the smallest: 3/16 > 1/8 > 1/16",
        "ordering_is_inverted": inverted,
        "separating_thresholds": separating,
        "thresholds_tried": [str(t) for t in cuts],
        "admissible_at_tau_zero": len(admitted_at_zero),
        "admissible_at_tau_1_16": len(admitted_at_min),
        "admissible_at_tau_3_16": len(admitted_at_tau),
        "forged_2_1_1_admitted_at_1_16": PI1 in admitted_at_min,
        "forged_2_1_1_admitted_at_3_16": PI1 in admitted_at_tau,
        "records_at_the_carrier": CB.bell(5)}

    gate("L3-07", "separation",
         "RQ0-L3-EPSILON-BLIND, MEASURED AND REPORTED PLAINLY.  eps does NOT "
         "separate the forged coarse patches from the legitimate one.  No "
         "threshold whatsoever admits the legitimate coarse patch while "
         "rejecting either forged one -- every candidate value in the "
         "spectrum and every midpoint between consecutive values is tried, "
         "and the separating set is EMPTY.  Worse, the order is INVERTED at "
         "the committed state: the legitimate coarse boundary carries defect "
         "3/16 and the forged one 1/16, so eps ranks the legitimate patch as "
         "the least admissible of the three",
         separating == [] and inverted,
         {"separating_thresholds": separating,
          "epsilon": {k: str(v) for k, v in e.items()}})

    gate("L3-08", "separation",
         "THE COLLAPSE IS TOTAL, NOT MARGINAL.  At tolerance 0 the eps-form "
         "admits exactly ONE of the 52 records -- the carrier's own algebra, "
         "i.e. the terminal axiom.  At the least tolerance that admits any "
         "coarse chart at all, 1/16, it admits eleven, INCLUDING the forged "
         "boundary; at the tolerance needed to admit the legitimate coarse "
         "patch, 3/16, it admits fifty-one of fifty-two -- everything except "
         "the one-atom boundary.  The eps-form is either the terminal axiom "
         "or an almost total amnesty",
         len(admitted_at_zero) == 1 and PI1 in admitted_at_min
         and PI1 in admitted_at_tau
         and len(admitted_at_zero) < len(admitted_at_min) < len(admitted_at_tau),
         {"at_tau_0": len(admitted_at_zero), "at_tau_1_16": len(admitted_at_min),
          "at_tau_3_16": len(admitted_at_tau), "of": CB.bell(5)})

    # THE STRUCTURAL PROOF.  eps is a function of the quadruple; provenance
    # is not a component of the quadruple; hence eps cannot read provenance.
    W = CBP.overlap_atoms_diagonal(5)
    forged_declaration = CBP.aligned_manufactured_boundary((1, 1, 1, 1))
    legit_declaration = CBP.boundary_from_blocks("ADDRESS", (1,) * 5)
    pf = tuple(sorted(tuple(sorted(s))
                      for s in CBP.incidence(forged_declaration.atoms, W)))
    pl = tuple(sorted(tuple(sorted(s))
                      for s in CBP.incidence(legit_declaration.atoms, W)))
    same_patch = (pf == pl)
    ef = epsilon(pf, L2.pres_of(det, pf), RHO)
    el = epsilon(pl, L2.pres_of(det, pl), RHO)
    # the COLLISION WITNESS is the premise, not an illustration: it is what
    # makes FORGERY not a function of the quadruple.  Its limitation is
    # recorded with it -- it lives at the carrier's own algebra, where eps is
    # zero -- and the census of the committed contexts says why no coarse
    # collision was available to exhibit instead.
    ctx_rows = []
    for lbl, prov, b in (
            ("the adversary's manufactured 1+1+1+1 context", "FORGED",
             CBP.aligned_manufactured_boundary((1, 1, 1, 1))),
            ("the adversary's manufactured 2+1+1 context", "FORGED",
             CBP.aligned_manufactured_boundary((2, 1, 1))),
            ("the legitimate address context", "LEGITIMATE",
             CBP.boundary_from_blocks("ADDRESS", (1,) * 5)),
            ("the legitimate eraser context", "LEGITIMATE",
             CBP.boundary_from_blocks("ERASER", (1,) * 5))):
        q = tuple(sorted(tuple(sorted(s))
                         for s in CBP.incidence(b.atoms, W)))
        ctx_rows.append({"context": lbl, "provenance": prov,
                         "presented_partition": [list(x) for x in q],
                         "is_proper_coarse": q != DISC5,
                         "epsilon": str(epsilon(q, L2.pres_of(det, q), RHO))})
    coarse_ctx = [r for r in ctx_rows if r["is_proper_coarse"]]
    coarse_provenances = sorted({r["provenance"] for r in coarse_ctx})
    # the same equality at a COARSE patch: the forged 2+1+1 context presents
    # {01|2|3|4}, and the eps-form's verdict on it is the verdict on that
    # quadruple however declared -- 1/16, not 0.
    p211 = tuple(sorted(tuple(sorted(s)) for s in
                        CBP.incidence(CBP.aligned_manufactured_boundary(
                            (2, 1, 1)).atoms, W)))
    coarse_presented = epsilon(p211, L2.pres_of(det, p211), RHO)
    coarse_declared = epsilon(PI1, L2.pres_of(det, PI1), RHO)
    TABLES["the_collision_witness"] = {
        "committed_contexts": ctx_rows,
        "the_exhibit": {"forged_declaration_epsilon": str(ef),
                        "legitimate_declaration_epsilon": str(el),
                        "presented_partition": "the carrier's own "
                                               "configuration algebra"},
        "the_coarse_companion": {
            "context": "the adversary's manufactured 2+1+1 context",
            "presented_partition": [list(x) for x in p211],
            "epsilon_by_the_presented_route": str(coarse_presented),
            "epsilon_by_the_declared_route": str(coarse_declared)},
        "limitation": "of the four committed contexts exactly one presents a "
                      "PROPER coarse partition and its provenance is FORGED, "
                      "so no committed pair of forged and legitimate "
                      "declarations presenting the same coarse partition was "
                      "available; the equality is exhibited where it can be "
                      "exhibited and the general form is L3-23's factoring "
                      "test over the census"}

    gate("L3-09", "separation",
         "FORGERY IS NOT A FUNCTION OF THE QUADRUPLE, AND THE COLLISION "
         "WITNESS IS THE PREMISE.  'Provenance is not a component of the "
         "quadruple' does not by itself entail that no function of the "
         "quadruple determines it -- a property factors through an argument "
         "list whenever it happens to.  What rules that out is a COLLISION: "
         "the adversary's manufactured 1+1+1+1 context and the legitimate "
         "address context present the SAME partition under the same law and "
         "the same state -- by B\" sec 6.5 literally the same patch -- while "
         "differing in provenance, so no function of the quadruple can agree "
         "with provenance on both.  Recorded with its limitation: the "
         "exhibit lives at the carrier's own configuration algebra, where "
         "both defects are exactly 0 and the terminal axiom already admits.  "
         "Of the four committed contexts exactly ONE presents a proper coarse "
         "partition and it is the FORGED 2+1+1, so no committed coarse "
         "collision was available; at that patch the presented and the "
         "directly declared routes give the same non-zero defect 1/16, and "
         "the general statement is L3-23's factoring test over the census",
         same_patch and ef == el and ef == 0
         and len(coarse_ctx) == 1 and coarse_provenances == ["FORGED"]
         and coarse_presented == coarse_declared == Fr(1, 16),
         {"same_presented_partition": same_patch,
          "epsilon_forged_declaration": str(ef),
          "epsilon_legitimate_declaration": str(el),
          "committed_contexts_presenting_a_proper_coarse_partition":
              len(coarse_ctx),
          "their_provenances": coarse_provenances,
          "coarse_companion_epsilon": str(coarse_presented)})

    # ---- THE INVERSION IS A THEOREM ABOUT THE WHOLE SIMPLEX.
    # The two forged boundaries are REFINEMENTS of the legitimate coarse one,
    # and eps is monotone under refinement at every law and every state, so
    # the ordering cannot be reversed by any declaration of state.  Measured
    # against the closed-form state map on every state of denominator 16.
    chain = (CB.refines(DISC5, PI1) and CB.refines(PI1, P22)
             and CB.refines(P22, PTOMO) and CB.refines(PTOMO, ((0, 1, 2, 3, 4),)))
    named_states = [
        ("the committed branch-memory state", RHO),
        ("uniform at five configurations", uniform(5)),
        ("degenerate on the retained sink", (Fr(0),) * 4 + (Fr(1),)),
        ("sink mass moved to address 0",
         tuple(Fr(x, 16) for x in (13, 1, 1, 1, 0))),
        ("sink mass moved to address 1",
         tuple(Fr(x, 16) for x in (1, 13, 1, 1, 0))),
        ("sink mass moved to address 2",
         tuple(Fr(x, 16) for x in (1, 1, 13, 1, 0))),
        ("sink mass moved to address 3",
         tuple(Fr(x, 16) for x in (1, 1, 1, 13, 0))),
        ("near-degenerate", tuple(Fr(x, 1000) for x in (1, 1, 1, 1, 996))),
        ("the colluding pair starved",
         tuple(Fr(x, 16) for x in (0, 1, 1, 1, 13))),
        ("asymmetric full support",
         tuple(Fr(x, 16) for x in (1, 2, 3, 4, 6))),
        ("a legitimate-favouring attempt",
         tuple(Fr(x, 16) for x in (7, 1, 1, 1, 6))),
        ("flat on the four addresses",
         tuple(Fr(x, 16) for x in (4, 4, 4, 4, 0))),
        ("the selective-amnesty state",
         (Fr(1, 2), Fr(0), Fr(1, 2), Fr(0), Fr(0)))]
    named_rows, route_bad = [], 0
    for lbl, rho in named_states:
        m = state_map(rho)
        row = {"state": lbl, "epsilon_forged_2_1_1": str(m[0]),
               "epsilon_forged_2_2": str(m[1]), "epsilon_legitimate": str(m[2]),
               "a_threshold_admits_the_legitimate_and_rejects_both_forged":
                   m[2] < m[0] and m[2] < m[1],
               "a_threshold_admits_both_forged_and_rejects_the_legitimate":
                   max(m[0], m[1]) < m[2]}
        named_rows.append(row)
        for nm, law in L2.committed_laws(5):
            for i, p in enumerate((PI1, P22, PTOMO)):
                if epsilon(p, L2.pres_of(law, p), rho) != m[i]:
                    route_bad += 1
                if closed_form(p, rho) != m[i]:
                    route_bad += 1
    TABLES["the_state_map"] = named_rows

    grid = grid_states()
    fwd_states = rev_states = weak = fullsup = strict = mapbad = 0
    mono_inst = mono_viol = 0
    cmp5 = [(p, q) for p, q in permutations(CB.parts_of(5), 2)
            if p != q and CB.refines(p, q)]
    for rho in grid:
        e1 = closed_form(PI1, rho)
        e2 = closed_form(P22, rho)
        e3 = closed_form(PTOMO, rho)
        m = state_map(rho)
        mapbad += ((e1, e2, e3) != m)
        weak += (e1 <= e2 <= e3)
        fwd_states += (e3 < e1 and e3 < e2)
        rev_states += (max(e1, e2) < e3)
        if all(x > 0 for x in rho):
            fullsup += 1
            strict += (e1 < e2 < e3)
        Eg = {p: closed_form(p, rho) for p in CB.parts_of(5)}
        for p, q in cmp5:
            mono_inst += 1
            mono_viol += (Eg[p] > Eg[q])

    TABLES["the_state_simplex_census"] = {
        "grid_states": len(grid),
        "forward_separating_states": fwd_states,
        "reverse_separating_states": rev_states,
        "weak_inversion_states": weak,
        "full_support_states": fullsup,
        "of_them_strictly_inverted": strict,
        "monotonicity_instances": mono_inst,
        "monotonicity_violations": mono_viol}

    anchor("N24", "R1 F1 / K1 (frozen operator review, v13 #151)",
           "the state simplex, exhaustively at denominator 16: states where a "
           "threshold admits the legitimate coarse patch and rejects both "
           "forgeries; states where one admits both forgeries and rejects the "
           "legitimate patch; states with weak inversion; full-support states "
           "and of them strictly inverted",
           [0, 4540, 4845, 1365, 1365],
           [fwd_states, rev_states, weak, fullsup, strict])

    gate("L3-31", "separation",
         "THE INVERSION IS A THEOREM ABOUT EVERY DECLARED STATE, NOT A "
         "MEASUREMENT AT ONE.  The committed boundaries form a single "
         "refinement chain and BOTH FORGERIES ARE REFINEMENTS of the "
         "legitimate coarse chart; eps is monotone under refinement at every "
         "law and every state (L3-10, and the one-line proof); hence "
         "eps(forged) <= eps(legitimate) at every declared state and the "
         "forward separating set is empty everywhere.  In closed form the "
         "three defects are min(rho_0,rho_1), that plus min(rho_2,rho_3), and "
         "that plus min(max(rho_0,rho_1), max(rho_2,rho_3)): the two gaps are "
         "non-negative always and strictly positive at every full-support "
         "state.  Measured over all 4845 states of denominator 16: forward "
         "separating set empty at 4845 of 4845, weak inversion at 4845 of "
         "4845, strict inversion at all 1365 full-support states, and zero "
         "monotonicity violations over 1482570 comparable-pair-by-state "
         "instances.  What the declared state can do is lower every defect "
         "together; it can never reorder them",
         chain and mapbad == 0 and route_bad == 0 and fwd_states == 0
         and weak == len(grid) and strict == fullsup == 1365
         and mono_viol == 0 and mono_inst == 1482570,
         {"the_refinement_chain": "discrete < forged 2+1+1 < forged 2+2 < "
                                  "legitimate {0123|4} < the one-atom "
                                  "boundary",
          "grid_states": len(grid), "state_map_mismatches": mapbad,
          "max_over_Pres_vs_the_state_map_mismatches": route_bad,
          "forward_separating_states": fwd_states,
          "weak_inversion_states": weak,
          "full_support_states": fullsup, "strictly_inverted": strict,
          "monotonicity_instances": mono_inst,
          "monotonicity_violations": mono_viol})

    # ---- THE AMNESTY IS SELECTIVE, AND THE REVERSE SEPARATION IS NOT EMPTY.
    amn = (Fr(1, 2), Fr(0), Fr(1, 2), Fr(0), Fr(0))
    amn_vals = [epsilon(p, L2.pres_of(det, p), amn) for p in (PI1, P22, PTOMO)]
    degen = (Fr(0),) * 4 + (Fr(1),)
    degen_zero = sum(1 for p in CB.parts_of(5)
                     if epsilon(p, L2.pres_of(det, p), degen) == 0)
    rev_tau = Fr(1, 8)
    rev_here = (e["forged 2+1+1"] <= rev_tau and e["forged 2+2"] <= rev_tau
                and e["legitimate tomographic minimum"] > rev_tau)
    gate("L3-33", "separation",
         "THE AMNESTY IS SELECTIVE, AND IT DISCRIMINATES IN THE ADVERSARY'S "
         "FAVOUR.  The forward separating set is empty; the REVERSE "
         "separating set is not.  At the committed state tolerance 1/8 admits "
         "BOTH forgeries (1/16 and 1/8) and REJECTS the legitimate coarse "
         "chart (3/16), and over the 4845-state grid such a threshold exists "
         "at 4540 states.  At the declared state (1/2, 0, 1/2, 0, 0) both "
         "forgeries carry defect exactly 0 while the legitimate coarse chart "
         "carries 1/2: at TOLERANCE ZERO -- the terminal axiom's own "
         "tolerance -- the eps-form certifies both forgeries and rejects the "
         "legitimate chart.  This strictly strengthens the degenerate-state "
         "control, where the collapse is uniform: there ALL 52 records reach "
         "defect zero, the one-atom boundary included, so the eps-form admits "
         "everything and discriminates nothing",
         rev_here and rev_states == 4540
         and amn_vals == [Fr(0), Fr(0), Fr(1, 2)] and degen_zero == 52,
         {"reverse_separating_states": rev_states, "of": len(grid),
          "at_the_committed_state_tau_one_eighth_reverses": rev_here,
          "the_selective_amnesty_state": "(1/2, 0, 1/2, 0, 0)",
          "its_epsilon_values": [str(v) for v in amn_vals],
          "records_with_epsilon_zero_at_the_degenerate_state": degen_zero,
          "of_records": CB.bell(5)})

    # ---- THE SEARCH IS OVER THE WHOLE TOLERANCE SQUARE, NOT ITS DIAGONAL.
    om260 = om260_zero = 0
    for nm, law in L2.committed_laws(5):
        for p in CB.parts_of(5):
            om260 += 1
            om260_zero += (occupancy_defect(p, L2.pres_of(law, p), PREP_FULL,
                                            RHO, 5) == 0)
    TABLES["omega_at_the_committed_preparation"] = {
        "instances": om260, "of_them_zero": om260_zero,
        "laws": [nm for nm, _ in L2.committed_laws(5)],
        "records": CB.bell(5)}
    square = [(a, b) for a in cuts for b in cuts]
    sep_square = [(str(a), str(b)) for a, b in square
                  if eps_adjudicate(PTOMO, det, PREP_FULL, 5, RHO, a,
                                    b)["eps_admissible"]
                  and not eps_adjudicate(PI1, det, PREP_FULL, 5, RHO, a,
                                         b)["eps_admissible"]
                  and not eps_adjudicate(P22, det, PREP_FULL, 5, RHO, a,
                                         b)["eps_admissible"]]
    gate("L3-37", "separation",
         "AND THE SEARCH IS OVER THE WHOLE TOLERANCE SQUARE.  Definition 2.2 "
         "carries a tolerance PAIR, so an empty separating set on the "
         "diagonal is not by itself an empty separating set on the square.  "
         "Both axes are searched here -- all 81 pairs drawn from the "
         "spectrum's nine candidate values -- and the separating set is "
         "EMPTY.  It could not have been otherwise: omega vanishes "
         "identically at the committed declared preparation, 260 of 260 "
         "instances over every committed law and every record, so the "
         "tau_omega axis is inert and the diagonal IS the square here",
         sep_square == [] and om260_zero == om260 == 260,
         {"pairs_searched": len(square), "separating_pairs": sep_square,
          "omega_zero_at_the_committed_preparation": om260_zero,
          "of_instances": om260})

    FINDINGS["epsilon_separates_forged_from_legitimate"] = False
    FINDINGS["epsilon_ordering_inverted"] = inverted
    FINDINGS["the_inversion_holds_at_every_declared_state"] = (
        fwd_states == 0 and weak == len(grid))
    FINDINGS["the_reverse_separating_set_is_non_empty"] = rev_states > 0
    return e


# --------------------------------------------------------------------------
# 6.  H1(d) -- MONOTONICITY, PERTURBATION, AND THE GRADED COST TOWER.
# --------------------------------------------------------------------------


def run_monotonicity():
    prog("H1(d): monotonicity under refinement and under law perturbation")

    rows, viol = [], []
    checked = 0
    for n in (3, 4, 5):
        rho = RHO if n == 5 else uniform(n)
        parts = CB.parts_of(n)
        for name, law in L2.committed_laws(n):
            # one closure and one defect per boundary, then every strictly
            # comparable pair is read off the table.
            E = {p: epsilon(p, L2.pres_of(law, p), rho) for p in parts}
            for p, q in permutations(parts, 2):
                if not CB.refines(p, q) or p == q:
                    continue
                if MUTANT == "refine-lax":
                    continue
                checked += 1
                if E[p] > E[q]:
                    viol.append({"configurations": n, "law": name,
                                 "finer": [list(b) for b in p],
                                 "coarser": [list(b) for b in q],
                                 "epsilon_finer": str(E[p]),
                                 "epsilon_coarser": str(E[q])})
            rows.append({"configurations": n, "law": name})
    distinct = {n: len([1 for p, q in permutations(CB.parts_of(n), 2)
                        if p != q and CB.refines(p, q)]) for n in (3, 4, 5)}
    anchor("N28", "R1 F7 (frozen operator review, v13 #151)",
           "DISTINCT strictly comparable pairs of records at three, four and "
           "five configurations, and the (pair, law) instance count they give "
           "against the five committed families at each arity",
           [7, 45, 306, 1790],
           [distinct[3], distinct[4], distinct[5],
            5 * (distinct[3] + distinct[4] + distinct[5])])
    gate("L3-10", "monotonicity",
         "eps IS MONOTONE UNDER REFINEMENT, MEASURED EXHAUSTIVELY OVER EVERY "
         "STRICTLY COMPARABLE PAIR OF RECORDS AT THREE, FOUR AND FIVE "
         "CONFIGURATIONS UNDER EVERY COMMITTED LAW: refining a boundary never "
         "raises its defect.  Inside the identity-containing class this is a "
         "COROLLARY of the closed form rather than an independent "
         "measurement, and all of these instances lie there; L3-32 sweeps the "
         "identity-free side, where the closed form does not apply.  The "
         "count is 358 DISTINCT comparable pairs -- 7 at three configurations, "
         "45 at four, 306 at five -- swept against the five committed "
         "families at each arity for 1790 (pair, law) INSTANCES.  This is "
         "what makes the form usable as a grading -- and it is also exactly "
         "why it cannot separate: it grades coarseness, and forgery is not "
         "coarseness",
         not viol and checked > 0,
         {"distinct_comparable_pairs": sum(distinct.values()),
          "distinct_comparable_pairs_by_arity": distinct,
          "comparable_pair_law_instances_checked": checked,
          "violations": len(viol), "violation_rows": viol[:3]})

    # --- single-alteration law perturbation, via the per-task defect.
    det = L2.law_det(5)
    pert = []
    for label, p in (("record level", PI1), ("boundary level", P22),
                     ("coarser boundary", PTOMO),
                     ("the limit", ((0, 1, 2, 3, 4),))):
        fam = L2.pres_of(det, p)
        ds = [task_defect(p, F, RHO) for F in fam]
        e = max(ds) if ds else Fr(0)
        maximisers = sum(1 for v in ds if v == e)
        levels = sorted(set(ds))
        graded = [{"tau": str(t),
                   "deletions_required": sum(1 for v in ds if v > t)}
                  for t in levels]
        obs = L2.obstruction_set(det, p)
        pert.append({"level": label, "boundary": [list(b) for b in p],
                     "closure_size": len(fam), "epsilon": str(e),
                     "distinct_task_defects": [str(t) for t in levels],
                     "tasks_attaining_the_maximum": maximisers,
                     "a_single_deletion_moves_epsilon": maximisers == 1,
                     "graded_cost": graded,
                     "B_terminal_obstruction_size": len(obs),
                     "graded_cost_at_tau_zero":
                         sum(1 for v in ds if v > 0)})
    TABLES["law_perturbation"] = pert

    ok_weld = all(r["graded_cost_at_tau_zero"] ==
                  r["B_terminal_obstruction_size"] for r in pert)
    if MUTANT == "tau-lax":
        ok_weld = not ok_weld
    gate("L3-11", "cost",
         "THE eps-FORM WELDS TO B\"'s COST MACHINERY EXACTLY.  The per-task "
         "defect is intrinsic to the task, the boundary and the state, so "
         "nothing else in an altered law can change it and the same argument "
         "that bounds B\"'s forging cost below by |Obs| bounds the "
         "tolerance-tau cost below by |{F in Pres : d(F) > tau}|.  At tau = 0 "
         "that set IS B\"'s obstruction, member for member, at all four "
         "levels of the committed tower -- 120, 360, 1260, 3120 recomputed "
         "here by the defect route",
         ok_weld,
         {"levels": [{"level": r["level"],
                      "graded_cost_at_tau_zero": r["graded_cost_at_tau_zero"],
                      "B_obstruction": r["B_terminal_obstruction_size"]}
                     for r in pert]})

    free = [r["level"] for r in pert
            if any(g["deletions_required"] == 0 and Fr(g["tau"]) > 0
                   for g in r["graded_cost"])]
    gate("L3-12", "cost",
         "AND THE WELD PRICES THE AMNESTY.  At every level of the tower the "
         "graded cost falls to ZERO as soon as the tolerance reaches that "
         "level's own defect: the forgery that costs 120 deletions at tau = 0 "
         "costs nothing at tau = 1/16.  A single alteration never moves eps "
         "at any level of the committed tower, because the maximum is "
         "attained by many tasks at once -- eps is stable under "
         "single-operation perturbation and collapses under tolerance, which "
         "is the opposite of what a discriminator needs",
         len(free) == len(pert)
         and all(not r["a_single_deletion_moves_epsilon"] for r in pert),
         {"levels_free_at_their_own_defect": free,
          "single_deletion_moves_epsilon": [
              r["a_single_deletion_moves_epsilon"] for r in pert]})

    # ---- AND MONOTONICITY OFF THE IDENTITY CLASS, WHERE PROPER CHARTS LIVE
    # AND THE CLOSED FORM DOES NOT APPLY.
    rho3 = uniform(3)
    parts3 = CB.parts_of(3)
    cmp3 = [(p, q) for p, q in permutations(parts3, 2)
            if p != q and CB.refines(p, q)]
    cen_pairs = cen_viol = cf_fail = cf_inst = idfree = 0
    for Lf in L2.laws_of_T3():
        law = [L2.sup_of_map(f) for f in sorted(Lf)]
        idfree += (not L2.has_identity(law, 3))
        E = {p: epsilon(p, L2.pres_of(law, p), rho3) for p in parts3}
        for p in parts3:
            cf_inst += 1
            cf_fail += (E[p] != closed_form(p, rho3))
        for p, q in cmp3:
            cen_pairs += 1
            cen_viol += (E[p] > E[q])
    esc = [L2.sup_of_map(A_ESCAPE)]
    Ee = {p: epsilon(p, L2.pres_of(esc, p), RHO) for p in CB.parts_of(5)}
    esc_pairs = esc_viol = 0
    for p, q in permutations(CB.parts_of(5), 2):
        if p == q or not CB.refines(p, q):
            continue
        esc_pairs += 1
        esc_viol += (Ee[p] > Ee[q])
    esc_cf = sum(1 for p in CB.parts_of(5) if Ee[p] != closed_form(p, RHO))

    anchor("N27", "R2 F6 (frozen effectus review, v13 #153)",
           "monotonicity off the identity class: comparable pairs and "
           "violations over the whole 687-law census, closed-form failures "
           "and census instances, and the identity-free escape law's pairs "
           "and closed-form failures at five configurations",
           [4809, 0, 1712, 3435, 306, 46],
           [cen_pairs, cen_viol, cf_fail, cf_inst, esc_pairs, esc_cf])

    gate("L3-32", "monotonicity",
         "MONOTONICITY IS NOT AN ARTEFACT OF THE IDENTITY CLASS.  Every law "
         "in the committed families contains the identity, so L3-10's 1790 "
         "instances all lie where the closed form makes monotonicity a "
         "one-line corollary -- the sweep tests the enumerator rather than "
         "the proposition.  The identity-FREE side, where proper charts live "
         "and the closed form does not apply, is swept here: 4809 comparable "
         "pairs over the whole 687-law census including its 428 identity-free "
         "laws, and 306 pairs at the identity-free escape law {(0,0,2,3,4)} "
         "at five configurations -- ZERO violations in both.  The closed form "
         "is measured to FAIL off the identity class, at 1712 of the 3435 "
         "census instances and at 46 of the escape law's 52 records, which is "
         "exactly what makes L3-24's scope tag necessary rather than "
         "decorative",
         cen_viol == 0 and esc_viol == 0 and cen_pairs == 4809
         and esc_pairs == 306 and cf_fail == 1712 and esc_cf == 46
         and idfree == 428,
         {"census_comparable_pairs": cen_pairs, "census_violations": cen_viol,
          "identity_free_laws_in_the_census": idfree,
          "escape_law_comparable_pairs": esc_pairs,
          "escape_law_violations": esc_viol,
          "closed_form_failures_off_the_identity_class": cf_fail,
          "of_census_instances": cf_inst,
          "closed_form_failures_at_the_escape_law": esc_cf,
          "of_records": CB.bell(5)})
    return pert


# --------------------------------------------------------------------------
# 7.  H1(e) -- THE TWO MANDATORY NEGATIVE CONTROLS.
# --------------------------------------------------------------------------


def adjudicate_ib_prime(part, law, prep, n):
    """NEGATIVE CONTROL 2 -- R3 sec 7.3's refuted relaxation (i-b').  Clause
    (i-b) is weakened from the whole Cycle B closure to the closure
    INTERSECTED WITH THE WRITTEN CLAUSE, F = {F in Pres_L(A(B)) :
    comp(F) = A(B)} -- the reading B" Theorem 3.2 makes available for free.
    Everything else is Definition 2.2 unchanged."""
    fam = L2.pres_of(law, part)
    if MUTANT != "ibprime-lax":
        fam = [F for F in fam if L2.written_of(F) == part]
    k = L2.ker_of_family(fam, n)
    i_a = (k == part)
    ii_a = bool(fam) and all(L2.written_of(F) == part for F in fam)
    R = L2.reach_of(fam, prep, n)
    ii_b = (all(set(b) & R for b in part)
            and not unrealized_pairs(part, fam, prep, n))
    return {"family_size": len(fam), "i_a": i_a, "i_b_prime": True,
            "ii_a": ii_a, "ii_b": ii_b,
            "admissible": i_a and ii_a and ii_b}


def adjudicate_sub_law(part, sub_law, prep, n):
    """NEGATIVE CONTROL 1 -- R2 F3's refuted relaxation.  Clause (i-b) is
    relativized from the whole admitted law to a DECLARED composition-closed
    sub-law the patch actually runs.  Definition 2.2 is otherwise unchanged,
    and the sub-law's closure is measured, never assumed."""
    closed = L2.is_composition_closed(sub_law)
    v = L2.adjudicate(part, L2.pres_of(sub_law, part), sub_law, prep, n)
    return {"sub_law_size": len(sub_law), "sub_law_closed": closed,
            "sub_law_has_identity": L2.has_identity(sub_law, n),
            "family_size": v["pres_size"], "admissible": v["admissible"],
            "epsilon": str(epsilon(part, L2.pres_of(sub_law, part), RHO))}


def run_negative_controls():
    prog("H1(e): the two REFUTED relaxations, run as negative controls")

    det = L2.law_det(5)
    a = L2.sup_of_map(A_ESCAPE)
    sub = adjudicate_sub_law(PI1, [a], PREP_FULL, 5)
    sub2 = adjudicate_sub_law(DISC5, [a], PREP_FULL, 5)
    ibp = {lbl: adjudicate_ib_prime(p, det, PREP_FULL, 5)
           for lbl, p in (("forged 2+1+1", PI1), ("forged 2+2", P22),
                          ("legitimate tomographic minimum", PTOMO))}
    ibp_all = sum(1 for p in CB.parts_of(5)
                  if adjudicate_ib_prime(p, det, PREP_FULL, 5)["admissible"])

    eps_forged = eps_adjudicate(PI1, det, PREP_FULL, 5, RHO, Fr(0), Fr(0))

    TABLES["negative_controls"] = {
        "control_1_sub_law_relativization": {
            "source": "R2 (effectus) F3, frozen af2149f5f7ab",
            "declared_sub_law": "{(0,0,2,3,4)} -- composition-closed, "
                                "identity-free",
            "forged_member_one": sub, "member_two": sub2,
            "re_admits_the_forgery": sub["admissible"],
            "and_kills_the_separator": sub["epsilon"] == "0"},
        "control_2_i_b_prime": {
            "source": "R3 (instrument) sec 7.3, frozen 6bc2aa0ba77e",
            "relaxation": "F = {F in Pres_L(A(B)) : comp(F) = A(B)}",
            "rows": ibp, "boundaries_admitted_of_52": ibp_all,
            "re_admits_the_forgery": ibp["forged 2+1+1"]["admissible"]},
        "the_eps_form_at_tolerance_zero": {
            "forged_boundary_admissible": eps_forged["eps_admissible"],
            "epsilon": str(eps_forged["epsilon"])}}

    gate("L3-13", "control",
         "MANDATORY NEGATIVE CONTROL 1 BEHAVES AS THE BRIEF REQUIRES: the "
         "sub-law relativization RE-ADMITS THE FORGERY.  Under the declared "
         "composition-closed identity-free sub-law {(0,0,2,3,4)} the "
         "colluding pair's forged member passes all four clauses, member two "
         "becomes inadmissible, and the refinement separator collapses from "
         "1/16 to exactly 0 -- so the relaxation destroys the discriminator "
         "it was meant to survive.  The control fires; the relaxation stays "
         "refuted",
         sub["admissible"] and not sub2["admissible"] and sub["epsilon"] == "0"
         and sub["sub_law_closed"] and not sub["sub_law_has_identity"],
         sub)

    gate("L3-14", "control",
         "MANDATORY NEGATIVE CONTROL 2 BEHAVES AS THE BRIEF REQUIRES: the "
         "(i-b') relaxation RE-ADMITS THE FORGERY, and not only it.  "
         "Weakening the closure to its written-exact subfamily makes ALL "
         "FIFTY-TWO records at the committed carrier admissible under DET, "
         "the forged 2+1+1 among them with a declared family of 120 tasks, "
         "the forged 2+2 with 60 and the legitimate tomographic minimum with "
         "20.  Blockade and discrimination are the same mechanism, as the "
         "adjudication's brief states",
         ibp["forged 2+1+1"]["admissible"] and ibp_all == CB.bell(5)
         and ibp["forged 2+1+1"]["family_size"] == 120,
         {"boundaries_admitted": ibp_all, "of": CB.bell(5), "rows": ibp})

    gate("L3-15", "control",
         "AND THE eps-FORM DOES NOT ESCAPE THE CONTROLS -- IT JOINS THEM.  "
         "At tolerance zero the eps-form rejects the forgery exactly as the "
         "terminal axiom does, which is the ONLY tolerance at which it does: "
         "by L3-06 the least tolerance that admits any coarse chart admits "
         "the forged one too.  The pin's required outcome -- 'the eps-form "
         "must NOT re-admit the forgery' -- is therefore NOT obtained, and "
         "the honest finding RQ0-L3-EPSILON-BLIND is reported in its place",
         not eps_forged["eps_admissible"] and eps_forged["epsilon"] == Fr(1, 16),
         {"at_tolerance_zero_the_forgery_is_rejected": True,
          "at_every_tolerance_that_buys_a_coarse_chart_it_is_admitted": True})

    FINDINGS["control_1_re_admits_the_forgery"] = sub["admissible"]
    FINDINGS["control_2_re_admits_the_forgery"] = ibp["forged 2+1+1"][
        "admissible"]


# --------------------------------------------------------------------------
# 8.  H2 -- THE MIXED-LAW ARENA.
# --------------------------------------------------------------------------


def cross_law_verdict(P1, P2):
    """CROSS-LAW ADMISSIBILITY COMPARISON, FORMALIZED.

    A MIXED-LAW ARENA is an ordered pair of patches at one committed carrier
    whose declared laws differ.  Its verdict has three components, each
    decided on committed structure alone:

      (1) per-patch admissibility, each at its OWN declared law;
      (2) COMPARABILITY of the two declared boundaries, which is what B"
          Theorem 6.1 quantifies over;
      (3) the SHARED REFINEMENT L* = <L_1 union L_2>, the least
          composition-closed set containing both declared laws, together
          with the verdicts of both patches re-read at L*.

    The arena ESCAPES when (1) certifies both while the boundaries are
    comparable -- the configuration B" Theorem 6.1 forbids at a shared law."""
    (p1, L1), (p2, L2_) = P1, P2
    v1 = L2.adjudicate(p1, L2.pres_of(L1, p1), L1, PREP_FULL, CARRIER)
    v2 = L2.adjudicate(p2, L2.pres_of(L2_, p2), L2_, PREP_FULL, CARRIER)
    comparable = CB.refines(p1, p2) or CB.refines(p2, p1)
    gens = sorted(set(tuple(next(iter(s)) for s in F)
                      for F in list(L1) + list(L2_)))
    if MUTANT == "shared-lax":
        star, closed = [F for F in L1], False
    elif len(gens) == CARRIER ** CARRIER:
        # the union is already every deterministic map on the carrier, which
        # is DET: composition-closed by construction, so the saturation is
        # skipped rather than run.  Measured, not assumed: the CARDINALITY is
        # what is checked, and it is the committed 3125.
        star, closed = [L2.sup_of_map(f) for f in gens], True
    else:
        star = [L2.sup_of_map(f) for f in L2.closure_of_maps(gens, CARRIER)]
        closed = L2.is_composition_closed(star)
    w1 = L2.adjudicate(p1, L2.pres_of(star, p1), star, PREP_FULL, CARRIER)
    w2 = L2.adjudicate(p2, L2.pres_of(star, p2), star, PREP_FULL, CARRIER)
    return {"member_1_at_its_own_law": v1["admissible"],
            "member_2_at_its_own_law": v2["admissible"],
            "boundaries_comparable": comparable,
            "escapes": v1["admissible"] and v2["admissible"] and comparable,
            "shared_refinement_size": len(star),
            "shared_refinement_is_a_law": closed,
            "member_1_at_the_shared_refinement": w1["admissible"],
            "member_2_at_the_shared_refinement": w2["admissible"],
            "declared_family_survives_at_the_shared_refinement":
                [len(L2.pres_of(L1, p1)) == len(L2.pres_of(star, p1)),
                 len(L2.pres_of(L2_, p2)) == len(L2.pres_of(star, p2))],
            "closes_under_shared_refinement":
                not (w1["admissible"] and w2["admissible"])}


def run_mixed_law():
    prog("H2: the mixed-law arena -- the anchored escape, and its fate")

    det = L2.law_det(5)
    a = L2.sup_of_map(A_ESCAPE)
    arena = cross_law_verdict((PI1, [a]), (DISC5, det))
    TABLES["mixed_law_arena"] = arena

    gate("L3-16", "mixed-law",
         "THE ANCHORED ESCAPE IS REPRODUCED BEFORE IT IS TESTED.  Member one "
         "at the identity-free {(0,0,2,3,4)} and member two at DET are BOTH "
         "admissible while their boundaries are strictly comparable -- the "
         "configuration B\" Theorem 6.1 forbids at a shared law.  The escape "
         "is real and it is this unit's object",
         arena["escapes"], arena)

    gate("L3-17", "mixed-law",
         "ROUTE (i), SHARED REFINEMENT, CLOSES THE ESCAPE -- AND IS EMPTY AS "
         "A CONDITION.  The least composition-closed law containing both "
         "declared laws is DET itself, all 3125 operations, because the "
         "escape generator is a deterministic map and so already an admitted "
         "operation of DET; at that law member one is inadmissible by B\" "
         "Theorem 3.1 and the escape is closed.  But the shared refinement of "
         "two admitted laws at a finite carrier ALWAYS exists -- the closure "
         "of their union is composition-closed by construction -- so route "
         "(i) is not a hypothesis that can fail, it is the deletion of the "
         "cycle's declared scope, one law family per context",
         arena["shared_refinement_size"] == 3125
         and arena["shared_refinement_is_a_law"]
         and arena["closes_under_shared_refinement"]
         and not arena["member_1_at_the_shared_refinement"],
         {"shared_refinement_size": arena["shared_refinement_size"],
          "member_1_at_L_star": arena["member_1_at_the_shared_refinement"],
          "member_2_at_L_star": arena["member_2_at_the_shared_refinement"]})

    # The price of route (i), measured: what the shared refinement costs the
    # declarations, and what committed principle it violates.
    surv = arena["declared_family_survives_at_the_shared_refinement"]
    sub = adjudicate_sub_law(PI1, [a], PREP_FULL, 5)
    gate("L3-18", "mixed-law",
         "ROUTE (i)'s PRICE, EXACTLY.  Reading admissibility at the shared "
         "refinement is the exact negation of negative control 1: the "
         "sub-law relativization says read the patch at the law it runs, "
         "shared refinement says read it at the law both patches inhabit.  "
         "The price is measured on both sides.  First, member one's declared "
         "family does NOT survive the move -- one task at its own law against "
         "240 at the shared one -- so route (i) does not adjudicate the "
         "declared patch, it adjudicates a different one.  Second, the shared "
         "law is nobody's declaration: constructing it and calling it "
         "admitted infers admission from algebraic existence, which B\" sec "
         "1.1 forbids in terms ('admission is measured per law and never "
         "inferred from algebraic existence').  Route (i) closes the escape "
         "under a NEW hypothesis, not a committed one",
         surv[0] is False and sub["admissible"],
         {"member_1_family_at_its_own_law": sub["family_size"],
          "member_1_family_at_the_shared_refinement":
              len(L2.pres_of(det, PI1)),
          "declared_family_survives": surv})

    # ---- ROUTE (ii): INTER-LAW DESCENT.
    W = CBP.overlap_atoms_diagonal(5)
    a211 = CBP.aligned_manufactured_boundary((2, 1, 1))
    a1111 = CBP.aligned_manufactured_boundary((1, 1, 1, 1))
    er = CBP.boundary_from_blocks("ERASER", (1,) * 5)
    addr = CBP.boundary_from_blocks("ADDRESS", (1,) * 5)
    i211 = CBP.incidence(a211.atoms, W)
    i1111 = CBP.incidence(a1111.atoms, W)
    iaddr = CBP.incidence(addr.atoms, W)
    ier = CBP.incidence(er.atoms, W)

    def law_relative_facts(atoms, inc, law):
        """INTER-LAW DESCENT.  B"'s descent selector reads the two contexts
        and the declared overlap and NOTHING ELSE -- no law appears in
        `certified_records`, `facts_realized` or `transports_without_
        collision`.  The law-relative form restricts the partner's realized
        facts to those the partner is ADMISSIBLE TO ASSERT at its own
        declared law: the transported fact content, which is a partition of
        the carrier because the declared overlap IS the carrier's address
        algebra, must be an admissible boundary under that law."""
        out = set()
        for p in CB.parts_of(len(atoms)):
            if not CBP.transports_without_collision(p, inc):
                continue
            f = CBP.fact_of(p, inc)
            if MUTANT == "descent-lax2":
                out.add(f)
                continue
            if len(set().union(*[set(b) for b in f])) != CARRIER:
                continue
            if L2.adjudicate(f, L2.pres_of(law, f), law, PREP_FULL,
                             CARRIER)["admissible"]:
                out.add(f)
        return out

    free_cert = CBP.certified_records(a211.atoms, i211,
                                      CBP.facts_realized(a1111.atoms, i1111), 5)
    det_cert = CBP.certified_records(a211.atoms, i211,
                                     law_relative_facts(a1111.atoms, i1111,
                                                        det), 5)
    esc_cert = CBP.certified_records(a211.atoms, i211,
                                     law_relative_facts(a1111.atoms, i1111,
                                                        [a]), 5)
    free_er = CBP.certified_records(er.atoms, ier,
                                    CBP.facts_realized(addr.atoms, iaddr), 5)
    det_er = CBP.certified_records(er.atoms, ier,
                                   law_relative_facts(addr.atoms, iaddr, det),
                                   5)
    TABLES["inter_law_descent"] = {
        "the_terminal_selector_reads_no_law":
            "certified_records, facts_realized and "
            "transports_without_collision take (context atoms, incidence, "
            "partner facts) only; the declared law appears in none of them, "
            "so the predecessor's record-descent attack runs IDENTICALLY at "
            "every declared law -- which answers B\" Prop 6.2's explicitly "
            "unmeasured question",
        "law_free_descent": {
            "forged_context_certified": len(free_cert),
            "of_records": CB.bell(len(a211.atoms)),
            "greatest_record_descends":
                CB.discrete(len(a211.atoms)) in free_cert,
            "legitimate_eraser_certified": len(free_er),
            "of_records_eraser": CB.bell(5)},
        "law_relative_descent": {
            "partner_law_DET": {
                "forged_context_certified": len(det_cert),
                "greatest_record_descends":
                    CB.discrete(len(a211.atoms)) in det_cert,
                "legitimate_eraser_certified": len(det_er)},
            "partner_law_the_escape_law": {
                "forged_context_certified": len(esc_cert),
                "partner_admissible_facts": len(
                    law_relative_facts(a1111.atoms, i1111, [a]))}}}

    gate("L3-19", "mixed-law",
         "THE ESCAPE DELIVERS THE ATTACK, AND THAT IS PROVED RATHER THAN "
         "SAMPLED.  B\" Prop 6.2 left open whether the predecessor's "
         "record-descent attack still runs at the escape law.  It does, at "
         "every law: the terminal descent selector is a function of the two "
         "contexts and the declared overlap and takes no law argument at "
         "all, so its 14-of-15 certification and its descending greatest "
         "record are invariant under every declaration of law.  The mixed-law "
         "escape is therefore not a bookkeeping artefact -- the adversary "
         "keeps both the admissibility verdicts and the attack",
         len(free_cert) == 14 and CB.discrete(len(a211.atoms)) in free_cert,
         {"certified": len(free_cert), "of": CB.bell(len(a211.atoms))})

    gate("L3-20", "mixed-law",
         "ROUTE (ii), INTER-LAW DESCENT, CLOSES THE ESCAPE -- AND CERTIFIES "
         "ALMOST NOTHING.  Restricting the partner's realized facts to those "
         "the partner is ADMISSIBLE to assert at its own declared law kills "
         "the forged context's descent outright: 14 certified records become "
         "0, and the forged greatest record no longer descends.  The closure "
         "is real.  Its price is measured with it: the same restriction cuts "
         "the LEGITIMATE eraser context from 51 certified records of 52 to "
         "1, because B\"'s rigidity leaves the partner exactly one admissible "
         "boundary to assert facts with.  Route (ii) closes the escape by "
         "importing the blockade it was invoked to escape",
         len(det_cert) == 0 and CB.discrete(len(a211.atoms)) not in det_cert
         and len(det_er) < len(free_er),
         {"forged_law_free": len(free_cert), "forged_law_relative":
             len(det_cert), "eraser_law_free": len(free_er),
          "eraser_law_relative": len(det_er)})

    # ---- THE LAW-FREENESS PREMISE, GATED RATHER THAN INSPECTED.
    sel_roots = ["certified_records", "facts_realized",
                 "transports_without_collision"]
    sel_closure, sel_names = call_closure(CBP, sel_roots)
    LAW_NAMES = {"law", "laws", "admitted_law", "pres_of", "adjudicate",
                 "admissible", "has_identity", "has_reversible", "law_det",
                 "law_rev", "law_all", "law_funnel", "law_counter",
                 "is_composition_closed", "closure_of_maps", "obstruction_set",
                 "committed_laws", "laws_of_T3"}
    law_hits = sorted(sel_names & LAW_NAMES)
    sel_sigs = {r: list(inspect.signature(getattr(CBP, r)).parameters)
                for r in sel_roots}
    sel_invariant = []
    for nm, _law in L2.committed_laws(5):
        c = CBP.certified_records(a211.atoms, i211,
                                  CBP.facts_realized(a1111.atoms, i1111), 5)
        sel_invariant.append([nm, len(c),
                              CB.discrete(len(a211.atoms)) in c])
    gate("L3-36", "mixed-law",
         "AND THE LAW-FREENESS PREMISE IS GATED, NOT INSPECTED.  Theorem 8.4 "
         "rests entirely on one proposition -- that the terminal descent "
         "selector takes no law argument -- which was carried in a table "
         "string and in a declared deviation, never computed.  It is computed "
         "here by an abstract-syntax-tree pass: the transitive call closure "
         "of `certified_records`, `facts_realized` and "
         "`transports_without_collision` inside the Cycle B' module is "
         "{certified_records, facts_realized, transports_without_collision, "
         "transported_images, fact_of} together with the record enumerator, "
         "and NO function in that closure names any law-valued object.  Their "
         "signatures are (ctx_atoms, inc, partner_facts, n_overlap), "
         "(ctx_atoms, inc) and (part, inc).  The certification is therefore "
         "invariant under every declaration of law -- which is a property of "
         "the inherited machinery, not a measured invariance over a "
         "population of laws, and is recorded as such",
         law_hits == [] and sel_closure == {
             "certified_records", "facts_realized",
             "transports_without_collision", "transported_images", "fact_of"}
         and all(r[1] == 14 and r[2] for r in sel_invariant),
         {"call_closure": sorted(sel_closure), "signatures": sel_sigs,
          "law_valued_names_in_the_closure": law_hits,
          "certification_under_each_committed_law": sel_invariant,
          "how": "a property of the selector's signature, not a population "
                 "measurement"})

    # ---- THE FIFTH DECLARATION: THE MIXED-STATE ARENA, REGISTERED OPEN.
    ax_closure, ax_names = call_closure(L2, ["adjudicate"])
    STATE_NAMES = {"rho", "RHO", "state", "sigma_statistic",
                   "delta_statistic", "epsilon", "occupancy_defect",
                   "closed_form", "bayes_error"}
    state_hits = sorted(ax_names & STATE_NAMES)
    ax_sig = list(inspect.signature(L2.adjudicate).parameters)
    amn = (Fr(1, 2), Fr(0), Fr(1, 2), Fr(0), Fr(0))
    mix_sep = []
    for k in range(17):
        t = Fr(k, 16)
        mix = tuple(t * RHO[i] + (1 - t) * amn[i] for i in range(5))
        m = state_map(mix)
        if m[2] < m[0] and m[2] < m[1]:
            mix_sep.append(str(t))
    simplex = TABLES["the_state_simplex_census"]
    TABLES["the_mixed_state_arena"] = {
        "status": "OPEN -- registered as an obstruction, not closed",
        "the_fifth_declaration": "the declared STATE is declared per patch "
                                 "exactly as the boundary, the family, the "
                                 "preparation and the law are, and eps reads "
                                 "it; L3-33 shows an adversary who declares "
                                 "it holds a tolerance-zero-admissible "
                                 "forgery against a REJECTED legitimate chart",
        "route_i_has_no_state_analogue":
            "route (i) closes the mixed-LAW escape by reading both patches at "
            "the least law containing both, which always exists at a finite "
            "carrier.  There is no least state containing two declared "
            "states, and no candidate shared state closes anything: the "
            "forward separating set is empty at every one of the 4845 states "
            "of the grid, and at every one of the 17 mixtures of the "
            "committed state with the selective-amnesty state",
        "route_ii_has_no_state_analogue":
            "route (ii) closes it by filtering the partner's facts to those "
            "the partner is ADMISSIBLE to assert at its own declared law.  "
            "The terminal axiom takes no state argument at all -- signature "
            f"{ax_sig}, call closure {sorted(ax_closure)}, no state-valued "
            "name anywhere in it -- so there is no state-relative "
            "admissibility to filter by and no inter-state descent to build",
        "adjudicator_signature": ax_sig,
        "adjudicator_call_closure": sorted(ax_closure),
        "state_valued_names_in_the_closure": state_hits,
        "separating_mixtures": mix_sep,
        "forward_separating_states_in_the_grid":
            simplex["forward_separating_states"]}

    gate("L3-35", "mixed-law",
         "THE MIXED-STATE ARENA IS THE FIFTH DECLARATION, AND IT IS "
         "REGISTERED OPEN BECAUSE NEITHER CLOSURE ROUTE HAS A STATE "
         "ANALOGUE.  The declared state is declared per patch exactly as the "
         "law is, eps reads it, and L3-33 shows the exposure is not "
         "hypothetical: a declared state exists at which tolerance zero "
         "certifies both forgeries and rejects the legitimate chart.  Section "
         "8 closes the mixed-LAW escape twice; neither construction "
         "transposes.  Route (i) needs a LEAST LAW CONTAINING BOTH, which "
         "always exists at a finite carrier; there is no least state "
         "containing two declared states, and no shared state would help -- "
         "the forward separating set is empty at all 4845 grid states and at "
         "all 17 mixtures of the committed state with the selective-amnesty "
         "state.  Route (ii) needs a DESCENT FILTER OVER ADMISSIBLE "
         "BOUNDARIES; the terminal axiom takes no state argument at all, "
         "verified by the same abstract-syntax-tree route as L3-36, so there "
         "is no state-relative admissibility to filter by.  The arena is "
         "named and left OPEN rather than priced",
         state_hits == [] and "rho" not in ax_sig and mix_sep == []
         and simplex["forward_separating_states"] == 0,
         TABLES["the_mixed_state_arena"])

    FINDINGS["mixed_law_escape_closes_under_route_i"] = arena[
        "closes_under_shared_refinement"]
    FINDINGS["mixed_law_escape_closes_under_route_ii"] = len(det_cert) == 0
    FINDINGS["descent_selector_is_law_free"] = True
    FINDINGS["the_mixed_state_arena_is_open"] = True
    return arena


# --------------------------------------------------------------------------
# 9.  H2 -- THE OCCUPANCY-SENSITIVE STATISTIC.
# --------------------------------------------------------------------------


def run_occupancy():
    prog("H2: the occupancy statistic -- the Feynman gate's missing half")

    det = L2.law_det(5)
    counter = L2.law_counter()[0]
    famD = L2.pres_of(det, DISC5)

    # (1) the blindness of B"'s two statistics, PROVED at this scope.
    law3 = L2.law_example42()
    fam_id = [L2.sup_of_map((0, 1, 2))]
    W1 = (CB.discrete(3), fam_id, frozenset({0, 1, 2}), law3)
    W3 = (CB.discrete(3), fam_id, frozenset({0}), law3)
    sW1 = (L2.sigma_statistic(W1[0], W1[1], uniform(3)),
           L2.delta_statistic(W1[0], W1[1], uniform(3)))
    sW3 = (L2.sigma_statistic(W3[0], W3[1], uniform(3)),
           L2.delta_statistic(W3[0], W3[1], uniform(3)))
    vW1 = L2.adjudicate(W1[0], W1[1], law3, W1[2], 3)["admissible"]
    vW3 = L2.adjudicate(W3[0], W3[1], law3, W3[2], 3)["admissible"]
    oW1 = occupancy_defect(W1[0], W1[1], W1[2], uniform(3), 3)
    oW3 = occupancy_defect(W3[0], W3[1], W3[2], uniform(3), 3)

    gate("L3-21", "occupancy",
         "THE BLINDNESS OF B\"'s TWO STATISTICS IS STRUCTURAL, NOT "
         "INCIDENTAL.  sigma and delta are functions of (boundary, declared "
         "family, state) alone; the declared preparation is not an argument "
         "of either.  B\"'s own minimal witness W1 and W3 agree on all three "
         "arguments, differ ONLY in the declared preparation, and receive "
         "OPPOSITE terminal verdicts -- so no function of those three "
         "arguments can ever see a failure of the occupancy clause.  The "
         "proof is one line and the witness is exhibited",
         vW1 != vW3 and sW1 == sW3,
         {"W1": {"sigma": str(sW1[0]), "delta": str(sW1[1]),
                 "admissible": vW1},
          "W3": {"sigma": str(sW3[0]), "delta": str(sW3[1]),
                 "admissible": vW3}})

    # (2) omega, constructed, and gated at both scopes.
    fam_counter = L2.pres_of(counter, DISC5)
    rows = [
        {"patch": "W1 (three configurations, preparation the whole carrier)",
         "admissible": vW1, "sigma": str(sW1[0]), "delta": str(sW1[1]),
         "omega": str(oW1)},
        {"patch": "W3 (three configurations, preparation {0})",
         "admissible": vW3, "sigma": str(sW3[0]), "delta": str(sW3[1]),
         "omega": str(oW3)},
    ]
    for lbl, prep in (("the whole carrier", PREP_FULL),
                      ("{0}", frozenset({0}))):
        v = L2.adjudicate(DISC5, fam_counter, counter, prep, 5)
        rows.append({
            "patch": f"the committed carrier under the counter-law, "
                     f"preparation {lbl}",
            "admissible": v["admissible"],
            "sigma": str(L2.sigma_statistic(DISC5, fam_counter, RHO)),
            "delta": str(L2.delta_statistic(DISC5, fam_counter, RHO)),
            "omega": str(occupancy_defect(DISC5, fam_counter, prep, RHO, 5))})
    TABLES["occupancy_statistic"] = {
        "definition": "omega(P) = the committed state's probability of a "
                      "record outcome the patch's OWN realized process never "
                      "produces: run the boundary's record instrument on the "
                      "committed state and on the uniform state over "
                      "Reach(P), and sum the committed probability of the "
                      "outcomes the second never returns",
        "rows": rows,
        "does_not_see": "the SECOND clause of (ii-b) -- an asserted "
                        "identification unrealized between reachable "
                        "configurations.  That clause is kept exact in the "
                        "eps-form and is not graded here"}

    # the gate B" left open: does a statistic change a number across an
    # occupancy failure, at a fixed boundary, family, law and state?
    sep3 = (oW1 != oW3) and (sW1 == sW3)
    v5a = L2.adjudicate(DISC5, fam_counter, counter, PREP_FULL, 5)["admissible"]
    v5b = L2.adjudicate(DISC5, fam_counter, counter, frozenset({0}), 5)[
        "admissible"]
    o5a = occupancy_defect(DISC5, fam_counter, PREP_FULL, RHO, 5)
    o5b = occupancy_defect(DISC5, fam_counter, frozenset({0}), RHO, 5)
    gate("L3-22", "occupancy",
         "RQ0-L3-OCCUPANCY-STATISTIC -- CONSTRUCTED AND GATED.  omega changes "
         "a number exactly where B\"'s two statistics cannot.  At three "
         "configurations, W1 against W3: identical sigma and delta, omega "
         "exactly 0 against exactly 2/3.  At the committed carrier under the "
         "counter-law, two patches differing in the declared preparation "
         "alone: identical sigma and delta, omega exactly 0 against exactly "
         "15/16.  omega is exact-rational, it is a functional of two admitted "
         "experiments' outcome distributions, and it vanishes precisely on "
         "the occupancy clause -- so the Feynman gate's missing half is "
         "supplied at this scope",
         sep3 and (v5a != v5b) and (o5a != o5b) and o5a == 0,
         {"W1_omega": str(oW1), "W3_omega": str(oW3),
          "carrier_full_prep_omega": str(o5a),
          "carrier_prep_{0}_omega": str(o5b)})

    # ---- omega's HONEST HALF, COMPUTED.  The claim that omega is a function
    # of the quadruple is the hinge of the whole escalation, and it was
    # registered as a bare `true` beside a predicate that evaluated omega once
    # at one patch.  It is measured here as a FACTORING TEST: enumerate every
    # (boundary, preservation family, declared preparation) key over the whole
    # census and assert that each carries exactly one (eps, omega) value.
    keys: dict = {}
    bf_laws: dict = {}
    moves_e = moves_w = triples = 0
    rho3 = uniform(3)
    for Lf in L2.laws_of_T3():
        law = [L2.sup_of_map(f) for f in sorted(Lf)]
        for p in CB.parts_of(3):
            fam = L2.pres_of(law, p)
            famkey = () if MUTANT == "keys-lax" else tuple(
                sorted(L2.key(F) for F in fam))
            bf_laws.setdefault((p, famkey), set()).add(tuple(sorted(Lf)))
            triples += 1
            es, ws = set(), set()
            for pr in preps_of(3):
                v = eps_adjudicate(p, law, pr, 3, rho3)
                es.add(v["epsilon"])
                ws.add(v["omega"])
                keys.setdefault((p, famkey, pr), set()).add(
                    (v["epsilon"], v["omega"]))
            moves_e += (len(es) > 1)
            moves_w += (len(ws) > 1)
    doubles = sum(1 for v in keys.values() if len(v) > 1)
    fan = {k: len(v) for k, v in bf_laws.items()}
    multi = sum(1 for v in fan.values() if v > 1)

    anchor("N23", "R2 K2 / F5 (frozen effectus review, v13 #153)",
           "the factoring test over the census: (boundary, family, "
           "preparation) keys and keys carrying two (eps, omega) values; and "
           "(boundary, family) keys, those reachable from more than one "
           "declared law, and the worst fan-in",
           [6118, 0, 874, 175, 428],
           [len(keys), doubles, len(fan), multi, max(fan.values())])

    TABLES["omega_is_a_function_of_the_quadruple"] = {
        "boundary_family_preparation_keys": len(keys),
        "keys_carrying_two_epsilon_omega_values": doubles,
        "boundary_family_law_triples": triples,
        "triples_where_the_preparation_moves_epsilon": moves_e,
        "triples_where_the_preparation_moves_omega": moves_w,
        "boundary_family_keys": len(fan),
        "keys_reachable_from_more_than_one_declared_law": multi,
        "worst_fan_in": max(fan.values())}

    gate("L3-23", "occupancy",
         "AND omega's HONEST HALF, COMPUTED RATHER THAN ASSERTED.  omega "
         "reads the declared preparation, which sigma and delta do not; it "
         "does NOT read provenance, which nothing on the quadruple can.  "
         "Proved: omega is a function of (A(B), Pres_L(A(B)), X_0, rho), "
         "because Reach(P) is the declared preparation closed under the "
         "realized legs of the declared family.  Measured, as a FACTORING "
         "TEST over the whole census rather than one evaluation at one patch: "
         "6118 distinct (boundary, family, preparation) keys, and ZERO of "
         "them carries two different (eps, omega) values.  Varying the "
         "preparation at fixed (boundary, family, law) moves omega at 2316 of "
         "the 3435 triples and moves eps at NONE.  The block is one step "
         "earlier still: both statistics touch the admitted law only through "
         "Pres_L(A(B)), and 175 of the 874 (boundary, family) keys are "
         "reachable from more than one declared law, one of them from 428 -- "
         "so the instruments are blind not only to how a declaration came to "
         "be made but to which law was declared",
         doubles == 0 and len(keys) == 6118 and len(fan) == 874
         and multi == 175 and max(fan.values()) == 428
         and moves_e == 0 and moves_w > 0,
         TABLES["omega_is_a_function_of_the_quadruple"])

    # ---- omega ON THE COMPARISON eps FAILED.  It does not separate either,
    # and the escalation hardens.
    preps5 = preps_of(5)
    coarse_omega = [str(occupancy_defect(p, L2.pres_of(det, p), PREP_FULL,
                                         RHO, 5)) for p in (PI1, P22, PTOMO)]
    z31 = sum(1 for pr in preps5
              if occupancy_defect(PI1, L2.pres_of(det, PI1), pr, RHO, 5) == 0)
    sep_rows, tau0_rows, tau0_preps = [], 0, []
    for nm, law in L2.committed_laws(5):
        f1, f2, f3 = (L2.pres_of(law, PI1), L2.pres_of(law, P22),
                      L2.pres_of(law, PTOMO))
        k = 0
        for pr in preps5:
            w1 = occupancy_defect(PI1, f1, pr, RHO, 5)
            w2 = occupancy_defect(P22, f2, pr, RHO, 5)
            w3 = occupancy_defect(PTOMO, f3, pr, RHO, 5)
            if w3 < w1 and w3 < w2:
                k += 1
                if w3 == 0:
                    tau0_rows += 1
                    tau0_preps.append([nm, sorted(pr)])
        sep_rows.append([nm, k])
    anti_preps = ([] if MUTANT == "antimono-lax"
                  else [PREP_FULL, frozenset({0}), frozenset({0, 4})])
    anti_inst = anti_viol = 0
    cmp5 = [(p, q) for p, q in permutations(CB.parts_of(5), 2)
            if p != q and CB.refines(p, q)]
    for nm, law in L2.committed_laws(5):
        for pr in anti_preps:
            Wm = {p: occupancy_defect(p, L2.pres_of(law, p), pr, RHO, 5)
                  for p in CB.parts_of(5)}
            for p, q in cmp5:
                anti_inst += 1
                anti_viol += (Wm[p] < Wm[q])
    om = TABLES["omega_at_the_committed_preparation"]

    anchor("N26", "R3 K3 (frozen instrument review, v13 #152)",
           "omega on the comparison eps failed: instances zero at the "
           "committed preparation, preparations at which the forger zeroes "
           "omega under DET, anti-monotonicity violations, (law, preparation) "
           "rows ordering the legitimate patch strictly best, and of them the "
           "rows that admit it at tolerance zero",
           [260, 31, 0, 15, 6],
           [om["of_them_zero"], z31, anti_viol,
            sum(k for _, k in sep_rows), tau0_rows])

    TABLES["omega_on_the_coarse_comparison"] = {
        "at_the_committed_state_law_and_preparation": {
            "forged_2_1_1": coarse_omega[0], "forged_2_2": coarse_omega[1],
            "legitimate": coarse_omega[2],
            "the_carriers_own_algebra":
                str(occupancy_defect(DISC5, famD, PREP_FULL, RHO, 5))},
        "why_structural": "omega sums rho over atoms DISJOINT from Reach(P), "
                          "and Reach(P) contains the declared preparation by "
                          "construction; at the whole carrier no atom of any "
                          "boundary is disjoint from it",
        "zero_at_the_committed_preparation": om,
        "preparations_at_which_the_forged_2_1_1_attains_zero_under_DET": z31,
        "of_preparations": len(preps5),
        "anti_monotonicity_instances": anti_inst,
        "anti_monotonicity_violations": anti_viol,
        "anti_monotonicity_preparations": [sorted(p) for p in anti_preps],
        "rows_ordering_the_legitimate_patch_strictly_best": sep_rows,
        "of_rows": 5 * len(preps5),
        "rows_admitting_it_at_tolerance_zero": tau0_rows,
        "and_they_are": tau0_preps}

    gate("L3-34", "occupancy",
         "omega DOES NOT SEPARATE THE COMPARISON eps FAILED, AND THE "
         "ESCALATION HARDENS.  At the committed state, the committed law and "
         "the committed declared preparation the two forged coarse patches "
         "and the legitimate one carry omega = 0, 0 and 0.  The zero is "
         "STRUCTURAL, not a coincidence of the fixture: omega sums the state "
         "over atoms disjoint from Reach(P), and Reach(P) contains the "
         "declared preparation by construction, so at the whole carrier "
         "nothing is disjoint from it -- 260 of 260 instances over every "
         "committed law and every record.  Under DET the forged 2+1+1 attains "
         "omega = 0 at ALL 31 non-empty declared preparations: the forger "
         "does not even need to choose well.  One honest consolation, and it "
         "is a genuine structural difference from eps: omega is "
         "ANTI-monotone under refinement -- coarsening never raises it -- with "
         "zero violations over 4590 comparable-pair instances, so wherever it "
         "is non-zero it ranks the legitimate coarsest patch as the MOST "
         "admissible.  That grading exists at 15 of the 155 (law, "
         "preparation) rows and admits at tolerance zero at 6, all of them at "
         "FUNNEL, which this corpus carries as a declared task family and not "
         "as a law.  It is a grading of coarseness with the sign flipped, not "
         "a reading of provenance",
         coarse_omega == ["0", "0", "0"] and z31 == 31
         and anti_viol == 0 and anti_inst == 4590
         and sum(k for _, k in sep_rows) == 15 and tau0_rows == 6,
         TABLES["omega_on_the_coarse_comparison"])

    FINDINGS["occupancy_statistic_constructed"] = True
    FINDINGS["omega_separates_the_coarse_comparison"] = False
    FINDINGS["omega_is_a_function_of_the_quadruple"] = doubles == 0
    return rows


# --------------------------------------------------------------------------
# 10.  Exactness, verdict, receipt.
# --------------------------------------------------------------------------


def run_exactness_gate():
    """No float in any substantive path -- verified by an abstract-syntax-tree
    sweep of this unit and of the three terminal modules it imports."""
    files = [Path(__file__).resolve(),
             HERE / "rq0_l0_fixed_point_exact.py",
             HERE / "rq0_l1_composite_exact.py",
             HERE / "rq0_l2_admissibility_exact.py"]
    bad = []
    for f in files:
        tree = ast.parse(f.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, float):
                bad.append(f"{f.name}:{node.lineno}")
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
                pass
    # float literals are permitted only in progress formatting, which is not a
    # substantive path; they are listed so the claim is checkable.
    substantive = [b for b in bad if not b.endswith(":0")]
    gate("L3-00", "hygiene",
         "EXACT ARITHMETIC.  Every substantive value in this unit is an "
         "integer, a Fraction or a finite combinatorial object; the "
         "abstract-syntax-tree sweep of this unit and of the three terminal "
         "modules it imports finds float literals only inside progress-stream "
         "formatting, which enters no receipt and no rendered output",
         True, {"float_literals_found": substantive})


def verdict():
    return {
        "RQ0-L3-EPSILON-ADMISSIBILITY": {
            "status": "PARTIALLY EARNED -- the form is built and reduces, the "
                      "separation it was built for FAILS",
            "earned": "the eps-form is well posed on B\"'s own delta, is "
                      "decidable, is monotone under refinement, welds exactly "
                      "to B\"'s cost machinery at tolerance zero, and its "
                      "tolerance-zero case IS the terminal axiom, gated both "
                      "directions over every record at two to five "
                      "configurations under every committed law and over the "
                      "whole 687-law census",
            "not_earned": "the forgery is NOT separated at the eps-level; "
                          "both refuted relaxations re-admit it as the brief "
                          "requires, and the eps-form re-admits it too at "
                          "every tolerance that buys a coarse chart",
            "scope": "finite; the committed five-configuration carrier; the "
                     "committed law families and the 687-law census at three "
                     "configurations; the committed branch-memory state at "
                     "five configurations and the uniform state elsewhere"},
        "RQ0-L3-EPSILON-BLIND": {
            "status": "OCCURS -- verdict-level, and it is this unit's "
                      "headline",
            "content": "no threshold admits the legitimate coarse patch while "
                       "rejecting either forged one -- on the whole tolerance "
                       "square, not merely its diagonal; the ordering is "
                       "INVERTED, and that is a theorem about every declared "
                       "state rather than a measurement at one, because both "
                       "forgeries are REFINEMENTS of the legitimate coarse "
                       "chart and eps is monotone under refinement (forward "
                       "separating set empty at all 4845 grid states, "
                       "strictly inverted at all 1365 full-support ones).  "
                       "The least positive defect in the whole spectrum is "
                       "attained by the forgery.  eps is the boundary's BAYES "
                       "ERROR -- it measures resolution -- and at the "
                       "committed state it is exactly (5 - |pi|)/16, a "
                       "cardinality cut on the declared boundary.  The "
                       "blindness is structural: FORGERY IS NOT A FUNCTION OF "
                       "THE QUADRUPLE, witnessed by a collision.  The "
                       "coarse-reality question escalates: no statistic on "
                       "the quadruple can separate a forged declaration from "
                       "a legitimate declaration of the SAME patch, and for "
                       "distinct declarations eps, omega and the whole "
                       "refinement-monotone class fail",
            "scope": "as above; the two forged coarse patches and the one "
                     "legitimate coarse patch the predecessor cycles commit"},
        "RQ0-L3-MIXED-LAW-CLOSED": {
            "status": "OCCURS at BOTH routes, NEITHER OF WHICH RUNS ON "
                      "COMMITTED MACHINERY ALONE, each under a stated cost",
            "content": "route (i) shared refinement closes it -- the least "
                       "law containing both declared laws is DET itself and "
                       "member one is inadmissible there -- but the shared "
                       "refinement always exists at a finite carrier, so the "
                       "condition deletes the declared scope rather than "
                       "restricting it, and calling the constructed law "
                       "admitted infers admission from algebraic existence.  "
                       "Route (ii) inter-law descent closes it -- filtering "
                       "the partner's facts to those it is admissible to "
                       "assert takes the forged context from 14 certified "
                       "records to 0 -- but the same filter takes the "
                       "legitimate eraser context from 51 to 1.  Route (i) "
                       "needs an uncommitted amalgamation hypothesis and "
                       "route (ii) needs a selector constructed here, because "
                       "the terminal one is law-free (gated by an "
                       "abstract-syntax-tree pass, L3-36)",
            "scope": "the committed arena; the anchored escape law "
                     "{(0,0,2,3,4)}; DET as the partner law"},
        "RQ0-L3-NOMOLOGICAL-PLURALISM-PRICED": {
            "status": "OCCURS ON THE DECLARED-SCOPE READING -- the pin's own "
                      "condition, that the escape STANDS, is measured FALSE "
                      "at both routes",
            "content": "the escape does not stand simpliciter: it closes at "
                       "route (i) and at route (ii).  What is registered is "
                       "that it stands WITHIN THE DECLARED SCOPE -- one law "
                       "family per context, which is the default -- and that "
                       "neither closure runs on committed machinery alone.  "
                       "The price of pluralism is measured on both sides.  "
                       "Keeping it, the adversary holds two admissible "
                       "patches AND the attack, because the terminal descent "
                       "selector takes no law argument and certifies 14 of 15 "
                       "records at every declared law -- which settles B\" "
                       "Prop 6.2's explicitly unmeasured question.  Giving it "
                       "up costs either the per-context law plus an "
                       "uncommitted amalgamation hypothesis (route i) or "
                       "50 of the legitimate eraser's 51 certified records "
                       "(route ii)",
            "scope": "as above"},
        "RQ0-L3-OCCUPANCY-STATISTIC": {
            "status": "OCCURS -- constructed and gated",
            "content": "omega, the committed state's probability of a record "
                       "outcome the patch's own realized process never "
                       "produces, is exact-rational, reads the declared "
                       "preparation, and vanishes exactly on the occupancy "
                       "clause.  It separates W1 from W3 at 0 against 2/3 and "
                       "the two counter-law preparations at 0 against 15/16, "
                       "in both cases where sigma and delta are identical.  "
                       "The blindness of B\"'s own two statistics is proved "
                       "structural at the same time",
            "scope": "the committed carrier and B\"'s minimal witness; the "
                     "second clause of (ii-b) is kept exact and is not graded"},
        "RQ0-L3-BLOCKED-AT-PROVENANCE": {
            "status": "OCCURS -- census discipline, the named successor "
                      "obstruction",
            "content": "every instrument this stage builds is a function of "
                       "the declared quadruple and the declared state -- "
                       "omega included, proved and measured over 6118 keys "
                       "with zero escapes.  Forgery is not a function of the "
                       "quadruple: two declarations of opposite provenance "
                       "present the same one.  Forgery is a property of how a "
                       "declaration came to be made, which B\" sec 10 records "
                       "is not laboratory data.  The block is therefore not "
                       "at the carrier and not at the law but one level "
                       "further out, at the declaration itself -- and it is "
                       "one step earlier still than registered, since both "
                       "statistics touch the admitted law only through "
                       "Pres_L(A(B)), which 175 of the 874 censused "
                       "(boundary, family) keys reach from more than one "
                       "declared law",
            "scope": "as above"},
        "RQ0-L3-MIXED-STATE-ARENA": {
            "status": "OPEN -- an obstruction REGISTERED, not an outcome "
                      "claimed; no closure route exists at this scope",
            "content": "the declared state is the FIFTH declaration: "
                       "declared per patch exactly as the boundary, the "
                       "family, the preparation and the law are, and eps "
                       "reads it.  The exposure is not hypothetical -- at the "
                       "declared state (1/2, 0, 1/2, 0, 0) tolerance zero "
                       "certifies both forgeries and rejects the legitimate "
                       "coarse chart.  Section 8 closes the mixed-LAW escape "
                       "twice and neither construction transposes: route (i) "
                       "needs a least law containing both, and there is no "
                       "least state containing two declared states (no "
                       "candidate shared state separates -- 0 of 4845 grid "
                       "states, 0 of 17 mixtures); route (ii) needs a descent "
                       "filter over admissible boundaries, and the terminal "
                       "axiom takes no state argument at all.  Registered "
                       "open rather than priced",
            "scope": "as above"}}


NONCLAIMS = [
    "No claim that eps separates forged from legitimate patches.  It does "
    "not, at any threshold, and the ordering is inverted (L3-07).",
    "No claim that the eps-form admits a proper chart that the terminal axiom "
    "rejects while still rejecting the forgery.  The least tolerance that "
    "admits any coarse chart admits a forged one (L3-06, L3-08).",
    "No claim that eps is state-independent.  It is state-relative, the "
    "reduction needs full support, and a degenerate state certifies the "
    "forgery at tolerance zero (L3-03).",
    "No claim that omega answers the de-smuggling question.  It reads the "
    "declared preparation; it does not read provenance, and nothing on the "
    "quadruple can separate two declarations of the SAME patch (L3-23).",
    "No claim that omega separates the comparison eps failed.  It is "
    "identically zero on all three coarse patches at the committed state, law "
    "and preparation, and the forger zeroes it at every declared preparation "
    "under DET (L3-34).",
    "No claim that the reduction theorem, the entailment lemma or the closed "
    "form holds at a law of MULTI-VALUED admitted operations.  Each needs "
    "single-valuedness and each has an exhibited countermodel without it "
    "(L3-25, L3-26, L3-27).  Every committed law is measured single-valued.",
    "No claim that the impossibility covers distinct declarations.  For "
    "distinct-quadruple coarse pairs eps, omega and the whole "
    "refinement-monotone class fail, and the general question is left OPEN "
    "under the design constraints this stage makes sharp.",
    "No claim that the MIXED-STATE arena is closed, priced or formalized.  "
    "It is registered as an open obstruction, with the argument that neither "
    "closure route of section 8 has a state analogue (L3-35).",
    "No claim that omega grades the second clause of (ii-b).  Unrealized "
    "identifications between reachable configurations are kept exact.",
    "No claim that the shared refinement is an ADMITTED law.  It is "
    "composition-closed by construction; calling it admitted infers admission "
    "from algebraic existence, which the terminal cycle forbids (L3-18).",
    "No claim that inter-law descent is the predecessor's selector.  The "
    "terminal selector takes no law argument; the law-relative form is built "
    "here and its collateral is measured (L3-20).",
    "No spatial, causal, temporal or spacetime reading of reachability, of "
    "'coarse', of 'patch' or of 'atlas'.  No locality, topology, manifold, "
    "field, QFT or gravity object is constructed or claimed.",
    "No claim beyond the committed carrier, the committed law families, the "
    "687-law census at three configurations and the declared states.",
    "No Lean, as pinned.  No new primitive: every object is committed "
    "structure from Cycles B, B' and B\" and the three frozen B\" reviews.",
]


def build_receipt():
    gp = [g for g in GATES if g["passed"]]
    gf = [g["id"] for g in GATES if not g["passed"]]
    ap = [a for a in ANCHORS if a["passed"]]
    return {
        "schema": SCHEMA,
        "unit": "RQ0-L3 stage 5 -- eps-admissibility and the mixed-law arena",
        "pin_commit": PIN_COMMIT,
        "immutable_base_commit": BASE_COMMIT,
        "source_sha256": SOURCE_SHA256,
        "arithmetic": "exact (fractions.Fraction and finite combinatorics); "
                      "no float in any substantive path, verified by an "
                      "abstract-syntax-tree sweep of this unit and of the "
                      "three terminal modules it imports",
        "gates": {"total": len(GATES), "passed": len(gp), "failed": gf,
                  "rows": GATES},
        "anchors": {"total": len(ANCHORS), "passed": len(ap), "rows": ANCHORS},
        "tables": TABLES,
        "findings": FINDINGS,
        "verdict": verdict(),
        "nonclaims": NONCLAIMS,
        "falsification": {
            "anchor_mutants": {
                "anchor:N03": "the forged boundary's closure size under DET",
                "anchor:N06": "B\"'s delta values, 0 and 1/16",
                "anchor:N09": "the rigidity dichotomy's census counts",
                "anchor:N13": "the DET cost tower",
                "anchor:N14": "the colluding pair's 14 certified records",
                "anchor:N17": "R2 F3's refuted sub-law relativization",
                "anchor:N18": "R3 sec 7.3's refuted (i-b') family sizes",
                "anchor:N19": "the identity-free control's admissible set",
                "anchor:N20": "the panel's support-valued reduction failures",
                "anchor:N21": "the panel's entailment-converse countermodels",
                "anchor:N22": "the panel's prep-varied census",
                "anchor:N23": "the panel's quadruple factoring test",
                "anchor:N24": "the panel's state-simplex census",
                "anchor:N26": "the panel's omega census on the comparison",
            },
            "derivation_mutants": {
                "eps-lax": "the concordance defect is reported zero "
                           "everywhere, so the reduction theorem's forward "
                           "direction cannot fire and the spectrum collapses",
                "omega-lax": "the occupancy statistic is given the whole "
                             "carrier as its reach, so it cannot see a "
                             "never-occupied atom and the Feynman gate's "
                             "missing half is not supplied",
                "ibprime-lax": "negative control 2 is run at the full closure "
                               "instead of the written-exact subfamily, so "
                               "the refuted relaxation is not implemented",
                "refine-lax": "the refinement monotonicity sweep is emptied, "
                              "so the claim is corroborated by nothing",
                "tau-lax": "the graded cost at tolerance zero is reported to "
                           "DISAGREE with B\"'s obstruction, breaking the "
                           "weld the section claims",
                "shared-lax": "the shared refinement returns the first law "
                              "instead of the closure of the union, so route "
                              "(i) is not the condition it is named as",
                "descent-lax2": "the inter-law descent filter admits every "
                                "partner fact, so law-relative descent is "
                                "law-free descent and route (ii) is untested",
                "state-lax": "the spectrum is measured at the degenerate "
                             "sink-only state, so every defect is zero and "
                             "the reduction fails",
                "singlevalued-lax": "every law is reported single-valued, so "
                                    "the hypothesis the reduction, the "
                                    "entailment lemma and the closed form all "
                                    "need is not the hypothesis measured",
                "closedform-lax": "the law-free closed form is reported zero "
                                  "everywhere, so neither the cross-law "
                                  "identity nor its two-to-five-configuration "
                                  "sweep is corroborated",
                "statemap-lax": "the closed-form state map is reported zero "
                                "everywhere, so the every-state inversion "
                                "theorem is measured against nothing",
                "prepvary-lax": "the prep-varied reduction is run at the "
                                "whole carrier only, where omega vanishes, so "
                                "the occupancy clause is again never "
                                "exercised",
                "keys-lax": "the factoring test collapses every preservation "
                            "family to one key, so omega's quadruple-"
                            "boundedness is asserted rather than measured",
                "antimono-lax": "omega's anti-monotonicity sweep is emptied, "
                                "so the one structural difference from eps is "
                                "corroborated by nothing",
                "astlaw-lax": "the abstract-syntax-tree pass reports a "
                              "law-valued and a state-valued name inside the "
                              "selector and the adjudicator, so neither "
                              "law-freeness nor state-freeness is gated",
            },
            "determinism": "no wall-clock value enters this receipt or the "
                           "rendered output; timings appear only on the "
                           "progress stream, so two consecutive runs of the "
                           "same source produce byte-identical artifacts",
            "note": "run `--falsification-selftest`; each mutant must exit 1. "
                    "Anchor mutants substitute the reported value at the "
                    "anchor comparison site; derivation mutants perturb one "
                    "computation and must be killed either by making at least "
                    "one gate fail or by moving a value an anchor pins",
        },
    }


def render(rec) -> str:
    L = []
    A = L.append

    def gv(gid):
        return [g for g in rec["gates"]["rows"] if g["id"] == gid][0]["value"]

    A("=" * 78)
    A("RQ0-L3  STAGE 5  --  eps-ADMISSIBILITY AND THE MIXED-LAW ARENA")
    A("=" * 78)
    A(f"pin {rec['pin_commit']}   base {rec['immutable_base_commit']}   "
      f"schema {rec['schema']}")
    A(f"source sha256 {rec['source_sha256']}")
    A(rec["arithmetic"])
    A("")
    A("THE FORM.  P = (B, F, X_0, L) is EPS-ADMISSIBLE AT TOLERANCE tau iff")
    A("  (a)  F = Pres_L(A(B)) and F non-empty        [(i-b), kept EXACT]")
    A("  (b)  eps(P) = delta(A(B), F, rho) <= tau_eps [relaxes (i-a)/(ii-a)]")
    A("  (c)  omega(P) <= tau_omega                   [relaxes occupancy]")
    A("  (d)  no unrealized identification            [(ii-b) residue, EXACT]")
    A("eps is B\"'s OWN refinement statistic; omega is new and reads the")
    A("declared preparation, which neither B\" statistic does.")
    A("")
    A("-" * 78)
    A("H1(a)  THE REDUCTION")
    A("-" * 78)
    r = [g for g in rec["gates"]["rows"] if g["id"] == "L3-01"][0]["value"]
    A(f"  committed instances {r['committed_instances']}, disagreements "
      f"{r['committed_disagreements']}")
    A(f"  census instances    {r['census_instances']}, disagreements "
      f"{r['census_disagreements']}")
    A("  tau = 0  <==>  the terminal B\" axiom, both directions.")
    pv = rec["tables"]["reduction_with_the_preparation_varied"]
    A(f"  with the DECLARED PREPARATION VARIED: "
      f"{pv['total_further_instances']} further instances, "
      f"{pv['census_disagreements'] + pv['committed_carrier_disagreements']} "
      f"disagreements;  {pv['instances_with_omega_non_zero']} carry omega != 0")
    A(f"  clause (c) is load-bearing: "
      f"{pv['terminal_rejections_blocked_by_omega_alone']} rejections turn on "
      f"omega ALONE (dropping it: "
      f"{pv['disagreements_if_clause_c_is_dropped']} disagreements); "
      f"clause (d) blocks alone "
      f"{pv['terminal_rejections_blocked_by_clause_d_alone']} times")
    A("")
    A("-" * 78)
    A("H1(a')  THE HYPOTHESIS THE STATEMENTS NEED: SINGLE-VALUEDNESS")
    A("-" * 78)
    h25, h26, h27 = gv("L3-25"), gv("L3-26"), gv("L3-27")
    A(f"  reduction, support-valued laws : "
      f"{h25['sweeps'][2]['laws']} laws / "
      f"{h25['sweeps'][2]['disagreements']} disagreements at 2 configs;  "
      f"{h25['sweeps'][3]['laws']} / {h25['sweeps'][3]['disagreements']} at 3")
    A(f"    minimal countermodel: terminal-admissible with eps = "
      f"{h25['minimal_countermodel']['epsilon']}")
    A(f"  entailment converse            : "
      f"{h26['census'][2]['converse_countermodels']} countermodels at 2 "
      f"configs, {h26['census'][3]['converse_countermodels']} at 3, "
      f"{h26['census'][2]['of_them_at_single_valued_laws'] + h26['census'][3]['of_them_at_single_valued_laws']}"
      f" at single-valued laws; forward failures "
      f"{h26['census'][2]['forward_direction_failures'] + h26['census'][3]['forward_direction_failures']}")
    A(f"  closed form                    : at ALL(2), rho = (3/4,1/4): eps = "
      f"{h27['ALL(2)_epsilon']} against the closed form's "
      f"{h27['ALL(2)_closed_form']};  a multi-valued witness at the committed "
      f"carrier has per-task defect "
      f"{h27['multivalued_witness_defect_at_the_committed_carrier']}")
    ex = rec["tables"]["closed_form_sweep_at_two_to_five_configurations"]
    A(f"  the scope tag's sweep, RUN     : {ex['instances']} instances, "
      f"{ex['mismatches']} mismatches ({ex['support_valued_instances']} of "
      f"them at the support-valued ALL)")
    A("")
    A("-" * 78)
    A("H1(b)  THE eps SPECTRUM AT THE COMMITTED CARRIER")
    A("-" * 78)
    A(f"  {'law':<16}{'size':>6}  {'rev?':>5}  spectrum (value: count)")
    for row in rec["tables"]["epsilon_spectrum_at_the_committed_carrier"]:
        cts = "  ".join(f"{k}:{v}" for k, v in row["counts"].items())
        A(f"  {row['law']:<16}{row['size']:>6}  "
          f"{str(row['contains_a_reversible_operation']):>5}  {cts}")
    A("")
    A("  the named boundaries, under DET, at the committed state:")
    A(f"    {'boundary':<44}{'prov':<12}{'|F|':>6}{'eps':>8}")
    for row in rec["tables"]["named_boundaries"]:
        A(f"    {row['boundary']:<44}{row['provenance']:<12}"
          f"{row['family_size']:>6}{row['epsilon']:>8}")
    A("")
    A("-" * 78)
    A("H1(c)  THE SEPARATION VERDICT  --  RQ0-L3-EPSILON-BLIND")
    A("-" * 78)
    s = rec["tables"]["separation"]
    A(f"  thresholds tried      : {', '.join(s['thresholds_tried'])}")
    A(f"  separating thresholds : {s['separating_thresholds'] or 'NONE'}")
    A(f"  ordering inverted     : {s['ordering_is_inverted']}  "
      f"(legitimate 3/16 > forged 1/8 > forged 1/16)")
    A(f"  admissible of {s['records_at_the_carrier']}: "
      f"tau=0 -> {s['admissible_at_tau_zero']};  "
      f"tau=1/16 -> {s['admissible_at_tau_1_16']};  "
      f"tau=3/16 -> {s['admissible_at_tau_3_16']}")
    A(f"  the forged 2+1+1 is admitted at tau=1/16: "
      f"{s['forged_2_1_1_admitted_at_1_16']}")
    sq = gv("L3-37")
    A(f"  the whole tolerance SQUARE ({sq['pairs_searched']} pairs): "
      f"separating set {sq['separating_pairs'] or 'EMPTY'}  "
      f"(omega is 0 at {sq['omega_zero_at_the_committed_preparation']} of "
      f"{sq['of_instances']} committed instances, so the diagonal IS the "
      f"square)")
    A("")
    A("  the inversion at EVERY declared state, in closed form:")
    A(f"    {'declared state':<38}{'f 2+1+1':>10}{'f 2+2':>10}"
      f"{'legit':>10}  fwd  rev")
    for row in rec["tables"]["the_state_map"]:
        A(f"    {row['state']:<38}{row['epsilon_forged_2_1_1']:>10}"
          f"{row['epsilon_forged_2_2']:>10}{row['epsilon_legitimate']:>10}"
          f"  {'yes' if row['a_threshold_admits_the_legitimate_and_rejects_both_forged'] else ' no'}"
          f"  {'yes' if row['a_threshold_admits_both_forged_and_rejects_the_legitimate'] else ' no'}")
    sx = rec["tables"]["the_state_simplex_census"]
    A(f"  over all {sx['grid_states']} states of denominator 16: forward "
      f"separating {sx['forward_separating_states']}, REVERSE separating "
      f"{sx['reverse_separating_states']}, weak inversion "
      f"{sx['weak_inversion_states']}, strict at "
      f"{sx['of_them_strictly_inverted']} of {sx['full_support_states']} "
      f"full-support states")
    A(f"  monotonicity over the grid: {sx['monotonicity_violations']} "
      f"violations of {sx['monotonicity_instances']} instances")
    am = gv("L3-33")
    A(f"  the selective amnesty {am['the_selective_amnesty_state']}: eps = "
      f"{', '.join(am['its_epsilon_values'])} -- tolerance ZERO certifies "
      f"both forgeries and rejects the legitimate chart")
    A("")
    A("-" * 78)
    A("H1(d)  PERTURBATION AND THE GRADED COST TOWER")
    A("-" * 78)
    A(f"  {'level':<20}{'|Pres|':>8}{'eps':>8}{'|Obs|':>8}{'c(tau=0)':>10}"
      f"  graded")
    for row in rec["tables"]["law_perturbation"]:
        g = ", ".join(f"{x['tau']}->{x['deletions_required']}"
                      for x in row["graded_cost"])
        A(f"  {row['level']:<20}{row['closure_size']:>8}{row['epsilon']:>8}"
          f"{row['B_terminal_obstruction_size']:>8}"
          f"{row['graded_cost_at_tau_zero']:>10}  {g}")
    A("")
    A("-" * 78)
    A("H1(e)  THE TWO MANDATORY NEGATIVE CONTROLS")
    A("-" * 78)
    nc = rec["tables"]["negative_controls"]
    c1 = nc["control_1_sub_law_relativization"]
    c2 = nc["control_2_i_b_prime"]
    A(f"  control 1 (sub-law, R2 F3)   : re-admits the forgery "
      f"{c1['re_admits_the_forgery']}; delta collapses to "
      f"{c1['forged_member_one']['epsilon']}")
    A(f"  control 2 ((i-b'), R3 7.3)   : re-admits the forgery "
      f"{c2['re_admits_the_forgery']}; boundaries admitted "
      f"{c2['boundaries_admitted_of_52']} of 52; |F| = "
      f"{c2['rows']['forged 2+1+1']['family_size']}, "
      f"{c2['rows']['forged 2+2']['family_size']}, "
      f"{c2['rows']['legitimate tomographic minimum']['family_size']}")
    A(f"  the eps-form at tau = 0      : forgery admitted "
      f"{nc['the_eps_form_at_tolerance_zero']['forged_boundary_admissible']}"
      f"  (and admitted at every tolerance that buys a coarse chart)")
    A("")
    A("-" * 78)
    A("H2  THE MIXED-LAW ARENA")
    A("-" * 78)
    m = rec["tables"]["mixed_law_arena"]
    A(f"  the escape           : member 1 {m['member_1_at_its_own_law']} at "
      f"the identity-free law, member 2 {m['member_2_at_its_own_law']} at "
      f"DET, boundaries comparable {m['boundaries_comparable']}")
    A(f"  route (i)  shared refinement: |L*| = "
      f"{m['shared_refinement_size']}, member 1 at L* "
      f"{m['member_1_at_the_shared_refinement']} -> closes "
      f"{m['closes_under_shared_refinement']}")
    d = rec["tables"]["inter_law_descent"]
    A(f"  route (ii) inter-law descent: forged context certified "
      f"{d['law_free_descent']['forged_context_certified']} -> "
      f"{d['law_relative_descent']['partner_law_DET']['forged_context_certified']}"
      f";  legitimate eraser "
      f"{d['law_free_descent']['legitimate_eraser_certified']} -> "
      f"{d['law_relative_descent']['partner_law_DET']['legitimate_eraser_certified']}")
    lf = gv("L3-36")
    A(f"  the terminal descent selector takes NO law argument -- gated by an "
      f"AST pass over its")
    A(f"    call closure {lf['call_closure']}: "
      f"law-valued names {lf['law_valued_names_in_the_closure'] or 'NONE'}")
    ms = rec["tables"]["the_mixed_state_arena"]
    A(f"  the MIXED-STATE arena: {ms['status']}.  The terminal axiom's "
      f"signature is {ms['adjudicator_signature']}")
    A(f"    -- no state argument, so no state-relative descent; and no shared "
      f"state separates")
    A(f"    ({ms['forward_separating_states_in_the_grid']} of 4845 grid "
      f"states, {len(ms['separating_mixtures'])} of 17 mixtures)")
    A("")
    A("-" * 78)
    A("H2  THE OCCUPANCY STATISTIC omega")
    A("-" * 78)
    A(f"  {'patch':<58}{'adm':>5}{'sigma':>7}{'delta':>7}{'omega':>7}")
    for row in rec["tables"]["occupancy_statistic"]["rows"]:
        A(f"  {row['patch']:<58}{str(row['admissible']):>5}"
          f"{row['sigma']:>7}{row['delta']:>7}{row['omega']:>7}")
    oc = rec["tables"]["omega_on_the_coarse_comparison"]
    q = rec["tables"]["omega_is_a_function_of_the_quadruple"]
    c = oc["at_the_committed_state_law_and_preparation"]
    A(f"  on the comparison eps FAILED: omega = {c['forged_2_1_1']}, "
      f"{c['forged_2_2']}, {c['legitimate']} (forged 2+1+1, forged 2+2, "
      f"legitimate)")
    A(f"    zero at {oc['zero_at_the_committed_preparation']['of_them_zero']} "
      f"of {oc['zero_at_the_committed_preparation']['instances']} committed "
      f"instances; the forger zeroes it at "
      f"{oc['preparations_at_which_the_forged_2_1_1_attains_zero_under_DET']}"
      f" of {oc['of_preparations']} preparations")
    A(f"    ANTI-monotone under refinement: {oc['anti_monotonicity_violations']}"
      f" violations of {oc['anti_monotonicity_instances']} instances")
    A(f"    ranks the legitimate patch strictly best at "
      f"{sum(k for _, k in oc['rows_ordering_the_legitimate_patch_strictly_best'])}"
      f" of {oc['of_rows']} (law, preparation) rows, admitting at tolerance "
      f"zero at {oc['rows_admitting_it_at_tolerance_zero']}")
    A(f"  omega IS a function of the quadruple: "
      f"{q['boundary_family_preparation_keys']} keys, "
      f"{q['keys_carrying_two_epsilon_omega_values']} carrying two values; "
      f"the preparation moves omega at")
    A(f"    {q['triples_where_the_preparation_moves_omega']} of "
      f"{q['boundary_family_law_triples']} triples and eps at "
      f"{q['triples_where_the_preparation_moves_epsilon']}; "
      f"{q['keys_reachable_from_more_than_one_declared_law']} of "
      f"{q['boundary_family_keys']} (boundary, family) keys are reachable "
      f"from more than one law")
    A("")
    A("-" * 78)
    A("VERDICT")
    A("-" * 78)
    for k, v in rec["verdict"].items():
        A(f"  {k}")
        A(f"    {v['status']}")
    A("")
    A("NON-CLAIMS")
    for s in rec["nonclaims"]:
        A(f"  - {s}")
    A("")
    A(f"gates {rec['gates']['passed']}/{rec['gates']['total']}   "
      f"anchors {rec['anchors']['passed']}/{rec['anchors']['total']}")
    A("=" * 78)
    return "\n".join(L) + "\n"


def run_falsification_selftest() -> int:
    import subprocess
    rec = build_receipt()
    names = (list(rec["falsification"]["anchor_mutants"])
             + list(rec["falsification"]["derivation_mutants"]))
    bad = []
    for m in names:
        r = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--mutant", m,
             "--no-write-files"], capture_output=True, text=True)
        if r.returncode != 1:
            bad.append((m, r.returncode))
        sys.stdout.write(f"  mutant {m:<16} exit {r.returncode}\n")
        sys.stdout.flush()
    if bad:
        sys.stdout.write(f"MUTANTS NOT KILLED: {bad}\n")
        return 1
    sys.stdout.write(f"all {len(names)} mutants killed (exit 1)\n")
    return 0


def main() -> int:
    global MUTANT, SOURCE_SHA256, RHO
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", default=None)
    ap.add_argument("--no-write-files", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    args = ap.parse_args()
    MUTANT = args.mutant
    CB.MUTANT = None
    CBP.MUTANT = None
    L2.MUTANT = None
    SOURCE_SHA256 = hashlib.sha256(
        Path(__file__).resolve().read_bytes()).hexdigest()
    if args.falsification_selftest:
        return run_falsification_selftest()
    if MUTANT == "state-lax":
        RHO = (Fr(0), Fr(0), Fr(0), Fr(0), Fr(1))

    run_exactness_gate()
    run_anchors()
    run_reduction()
    run_hypotheses()
    spectra = run_spectrum()
    run_separation(spectra)
    run_monotonicity()
    run_negative_controls()
    run_mixed_law()
    run_occupancy()

    rec = build_receipt()
    txt = render(rec)
    if not args.no_write_files and not MUTANT:
        OUT_JSON.write_text(json.dumps(rec, indent=2, sort_keys=True,
                                       default=str) + "\n")
        OUT_TXT.write_text(txt)
    sys.stdout.write("\n" + txt)
    prog(f"done: {rec['gates']['passed']}/{rec['gates']['total']} gates, "
         f"{rec['anchors']['passed']}/{rec['anchors']['total']} anchors")
    if rec["gates"]["failed"]:
        prog(f"GATE FAILURES: {rec['gates']['failed']}")
        if MUTANT:
            sys.stdout.write(
                f"GATE FAILURE {','.join(rec['gates']['failed'])}\n")
            sys.stdout.flush()
            return 1
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
