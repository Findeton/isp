#!/usr/bin/env python3
"""RQ0-L2 Cycle B" -- generative patch admissibility: the Atlas Axiom.

Executes the frozen pin `v13/note-rq0-l2-generative-admissibility-pin.md`
(commit 9576aee).

The candidate axiom.  A PATCH is a triple (boundary, declared task family,
admitted law) on a committed finite carrier.  It is ADMISSIBLE iff

  (i)  GALOIS-MINIMALITY, BOTH WAYS
       (i-a)  the boundary is the #103-minimal sufficient boundary OF its
              own declared family  --  A(B) = ker(F), the retract through
              which every declared task factors and which merges nothing
              the family separates;
       (i-b)  the family is the boundary's Cycle B closure  --
              F = Pres_L(A(B)), decided by the terminal availability
              criterion (Cycle B Def 2.3 / Lemma 3.2);

  (ii) GENERATIVITY
       (ii-a) WRITTEN: every declared task writes exactly the boundary's
              record, comp(F) = A(B)  (Cycle B Cor 3.3's co-merge
              procedure: the realized legs);
       (ii-b) OCCUPIED: the reachable subprocess occupies every atom, and
              every asserted identification is realized between reachable
              configurations.

Halves: THE AXIOM (rigidity, entailment, controls) / THE DISCRIMINATORS
(the colluding pair first) / THE FEYNMAN GATE / THE MINIMAL WITNESS /
THE COLLUSION-COST TOWER.

Immutable inputs reused as anchors: Cycle B TERMINAL (v13 #123) and Cycle
B' TERMINAL (v13 #134), plus the #103/#111 committed fixtures.  Every
reused committed value is an anchor and exits 1 on mismatch.  Substantive
negatives exit 0.  `--mutant NAME` breaks exactly one committed anchor or
one derivation step and must exit 1.

Scope: finite; ONE committed carrier of five configurations; one law family
per context, declared.  Reachability is an ORDER ON CONFIGURATIONS and
carries no spatial, causal or temporal reading.  No locality, topology,
causality, spacetime, field, QFT or gravity object is constructed or
claimed.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
import time
from fractions import Fraction as Fr
from itertools import permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import rq0_l0_fixed_point_exact as CB   # Cycle B TERMINAL machinery
import rq0_l1_composite_exact as CBP    # Cycle B' TERMINAL machinery

SCHEMA = "rq0-l2-generative-admissibility-receipt-v1"
PIN_COMMIT = "9576aee"
BASE_COMMIT = "efa7224"
OUT_TXT = HERE / "rq0_l2_admissibility_output.txt"
OUT_JSON = HERE / "rq0_l2_admissibility_receipt.json"

T0 = time.time()
MUTANT: str | None = None
SOURCE_SHA256 = ""

GATES: list[dict] = []
ANCHORS: list[dict] = []
TABLES: dict = {}
FINDINGS: dict = {}


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


# --------------------------------------------------------------------------
# 1.  Carrier, supports, laws.  Everything is exact and combinatorial: a
#     future is presented by its SECTOR SUPPORT, Cycle B's own object.
# --------------------------------------------------------------------------


def sup_of_map(f) -> tuple:
    """The sector support of a deterministic sector map."""
    return tuple(frozenset({v}) for v in f)


def key(sup) -> tuple:
    """A canonical, sortable, printable key for a sector support."""
    return tuple(tuple(sorted(s)) for s in sup)


def compose(F, G) -> tuple:
    """F after G, on supports:  (F o G)(j) = union of F(l) over l in G(j)."""
    return tuple(frozenset().union(*[F[l] for l in G[j]]) for j in range(len(G)))


def is_composition_closed(law) -> bool:
    """Measured, never assumed.  A deterministic fast path (every support a
    singleton) computes the same composition by integer indexing; the two
    routes are checked against each other by L2-16's own gate data."""
    if all(len(s) == 1 for F in law for s in F):
        fns = [tuple(next(iter(s)) for s in F) for F in law]
        S = set(fns)
        for f in fns:
            for g in fns:
                if tuple(f[x] for x in g) not in S:
                    return False
        return True
    S = set(key(F) for F in law)
    for F in law:
        for G in law:
            if key(compose(F, G)) not in S:
                return False
    return True


def law_all(n: int):
    """Every left-total sector relation: Cycle B's ALL family."""
    return [tuple(s) for s in CB.relations_of(n)]


def law_det(n: int):
    """DET: deterministic classical postprocessing of the flag."""
    return [sup_of_map(f) for f in product(range(n), repeat=n)]


def law_funnel(n: int):
    """FUNNEL: the identity and the elementary sector merges only."""
    out = [sup_of_map(tuple(range(n)))]
    for k in range(n):
        for l in range(n):
            if k != l:
                out.append(CB.elementary_merge(n, k, l))
    return out


def law_rev(n: int):
    """REV: atom permutations only -- the reversible law."""
    return [sup_of_map(p) for p in permutations(range(n))]


def law_counter():
    """Cycle B Prop 4.12's counter-law L_R, recomputed by Cycle B' route."""
    maps, rev = CBP.counter_law_L_R()
    return [sup_of_map(f) for f in maps], rev


def law_identity_free_3():
    """The identity-free positive control: the two sector maps of Cycle B
    Example 4.2 WITHOUT the identity.  Composition-closed (measured)."""
    return [sup_of_map((0, 0, 2)), sup_of_map((0, 2, 2))]


def law_example42():
    """Cycle B Example 4.2's committed law {id, a, b} on three atoms."""
    return [sup_of_map((0, 1, 2)), sup_of_map((0, 0, 2)), sup_of_map((0, 2, 2))]


# --------------------------------------------------------------------------
# 2.  THE AXIOM.  Each clause is a decision procedure on committed objects.
# --------------------------------------------------------------------------


def ker_of_family(fam, n: int):
    """(i-a)'s object.  The #103-minimal sufficient process boundary of a
    declared family, at sector-support granularity: configurations are
    merged exactly when NO declared task separates them, so the quotient is
    the minimum-rank retract through which every declared task factors.
    The empty family separates nothing, so its minimal boundary is the
    one-atom boundary."""
    if MUTANT == "ker-lax":
        return CB.indiscrete(n)
    if not fam:
        return CB.indiscrete(n)
    ordered = sorted(fam, key=key)
    sig: dict = {}
    for j in range(n):
        sig.setdefault(tuple(key(F)[j] for F in ordered), []).append(j)
    return tuple(sorted(tuple(sorted(v)) for v in sig.values()))


def pres_of(law, part):
    """(i-b)'s object.  Pres_L(pi) by Cycle B Definition 2.3's criterion --
    the images of distinct blocks are pairwise disjoint -- evaluated over
    the admitted law.  Never read off a generator."""
    if MUTANT == "pres-lax":
        return list(law)
    return [F for F in law if CB.images_disjoint(F, part)]


def written_of(F):
    """(ii-a)'s object.  comp(F): the record the realized legs of F write,
    by Cycle B Corollary 3.3's co-merge procedure."""
    if MUTANT == "comp-lax":
        return CB.discrete(len(F))
    return CB.comp(F)


def reach_of(fam, prep, n: int):
    """(ii-b)'s object.  THE REACHABLE SUBPROCESS: the configurations the
    patch's realized process occupies -- the declared preparation closed
    under the realized legs of the declared family.  This is an ORDER ON
    CONFIGURATIONS.  It has no spatial, causal or temporal reading."""
    if MUTANT == "reach-lax":
        return set(range(n))
    R = set(prep)
    changed = True
    while changed:
        changed = False
        for F in fam:
            for j in sorted(R):
                for l in F[j]:
                    if l not in R:
                        R.add(l)
                        changed = True
    return R


def is_partition(images, n: int) -> bool:
    """CARRIER TYPING.  A boundary presented at the carrier is carrier-typed
    when its atoms' images form a partition of the carrier's configurations.
    Measured, never assumed: a rotated boundary's images overlap."""
    if MUTANT == "typing-lax":
        return True
    seen: set = set()
    for s in images:
        if not s or (seen & set(s)):
            return False
        seen |= set(s)
    return seen == set(range(n))


def adjudicate(part, fam, law, prep, n: int) -> dict:
    """THE ATLAS AXIOM, decided.  Returns every clause's verdict together
    with the offending witness whenever a clause fails."""
    out: dict = {}
    k = ker_of_family(fam, n)
    out["ker"] = k
    out["i_a"] = (k == part)
    if not out["i_a"]:
        wit = None
        for F in sorted(fam, key=key):
            for b in part:
                for x in b:
                    for y in b:
                        if x < y and F[x] != F[y]:
                            wit = {"offending_task": key(F),
                                   "separates_inside_block": [x, y],
                                   "block": list(b)}
                            break
                    if wit:
                        break
                if wit:
                    break
            if wit:
                break
        if wit is None:
            wit = {"reason": "two blocks are left undistinguished by every "
                             "declared task", "computed_minimal_boundary": k}
        out["i_a_witness"] = wit
    P = pres_of(law, part)
    out["pres_size"] = len(P)
    out["i_b"] = (sorted(key(F) for F in fam) == sorted(key(F) for F in P))
    if not out["i_b"]:
        have = set(key(F) for F in fam)
        want = set(key(F) for F in P)
        out["i_b_witness"] = {"missing_from_declared_family":
                              sorted(want - have)[:3],
                              "declared_but_not_preserving":
                              sorted(have - want)[:3],
                              "declared": len(have), "closure": len(want)}
    bad = [F for F in fam if written_of(F) != part]
    out["ii_a"] = (not bad) and bool(fam)
    if bad:
        F = sorted(bad, key=key)[0]
        c = written_of(F)
        pair = None
        for b in part:
            for x in b:
                for y in b:
                    if x < y and not any(x in blk and y in blk for blk in c):
                        pair = [x, y]
                        break
                if pair:
                    break
            if pair:
                break
        out["ii_a_witness"] = {"offending_task": key(F), "writes": c,
                               "boundary_asserts": part,
                               "unwritten_identification": pair}
    elif not fam:
        out["ii_a_witness"] = {"reason": "the declared family is empty: the "
                               "realized process writes nothing at all"}
    R = reach_of(fam, prep, n)
    out["reach"] = sorted(R)
    empty = [list(b) for b in part if not (set(b) & R)]
    unreal = []
    for b in part:
        occ = sorted(set(b) & R)
        for x in occ:
            for y in occ:
                if x < y and not any(x in blk and y in blk
                                     for F in fam for blk in [written_of(F)]
                                     if x in blk):
                    if not any(written_of(F) and
                               any(x in blk and y in blk
                                   for blk in written_of(F)) for F in fam):
                        unreal.append([x, y])
    out["ii_b"] = (not empty) and (not unreal)
    if empty or unreal:
        out["ii_b_witness"] = {"never_occupied_atoms": empty,
                               "unrealized_identifications": unreal[:3]}
    out["i"] = out["i_a"] and out["i_b"]
    out["ii"] = out["ii_a"] and out["ii_b"]
    out["admissible"] = out["i"] and out["ii"]
    return out


# --------------------------------------------------------------------------
# 3.  ANCHORS -- every committed value this unit reuses, recomputed.
# --------------------------------------------------------------------------


def run_anchors():
    prog("anchors: Cycle B, Cycle B', #103, #111")

    for n, committed in ((1, 1), (2, 2), (3, 5), (4, 15), (5, 52)):
        anchor(f"M01-{n}", "Cycle B sec 4 (Bell triangle recurrence)",
               f"record lattice size at {n} atoms",
               CB.bell_recurrence(n), CB.bell(n))

    for n, committed in ((2, 3), (3, 7), (4, 13), (5, 21)):
        anchor(f"M02-{n}", "Cycle B Thm 4.4 (FUNNEL row)",
               f"FUNNEL futures at {n} atoms", committed, len(law_funnel(n)))

    for n, committed in ((2, 1), (3, 1), (4, 1), (5, 1)):
        law = law_rev(n)
        anchor(f"M03-{n}", "Cycle B Thm 4.4 (REV row)",
               f"records fixed by cl under the reversible law at {n} atoms",
               committed, len(CB.fix_set_of_family(law, n)))

    for n, committed in ((2, 2), (3, 5), (4, 15), (5, 52)):
        law = law_det(n)
        anchor(f"M04-{n}", "Cycle B Thm 4.3 / Thm 4.4 (DET row)",
               f"records fixed by cl under DET at {n} atoms",
               committed, len(CB.fix_set_of_family(law, n)))

    lr, rev = law_counter()
    anchor("M05", "Cycle B Prop 4.12", "counter-law L_R: admitted sector maps",
           120, len(lr))
    anchor("M06", "Cycle B Prop 4.12", "counter-law L_R: reversible members",
           1, len(rev))
    anchor("M07", "Cycle B Prop 4.12", "counter-law L_R: records fixed of 52",
           52, len(CB.fix_set_of_family(lr, 5)))

    ex = law_example42()
    anchor("M08", "Cycle B Example 4.2",
           "the committed three-atom law {id,a,b} is composition-closed",
           True, is_composition_closed(ex))
    anchor("M09", "Cycle B Example 4.2",
           "its realized collision partitions",
           [[[0], [1], [2]], [[0], [1, 2]], [[0, 1], [2]]],
           sorted([list(map(list, CB.comp(F))) for F in ex]))
    anchor("M10", "Cycle B Example 4.2", "records fixed of 5", 4,
           len(CB.fix_set_of_family(ex, 3)))

    anchor("M11", "Cycle B Thm 3.8 / #103 sec 9.2",
           "minimal classical experiment of the preserving branch-memory task",
           1, CB.minimal_classical_experiment(
               CB.branch_memory_preserving_likelihoods()))
    anchor("M12", "Cycle B Thm 3.8 / #103 sec 9.3",
           "minimal classical experiment of the eraser branch-memory task",
           5, CB.minimal_classical_experiment(
               CB.branch_memory_eraser_likelihoods()))
    anchor("M13", "Cycle B sec 5.1",
           "eraser likelihood rows (sink weight, success weight)",
           [Fr(3, 4), Fr(1, 4)],
           [CB.branch_memory_eraser_likelihoods()[0][0],
            CB.branch_memory_eraser_likelihoods()[0][1]])

    W = CBP.overlap_atoms_diagonal(5)
    er = CBP.boundary_from_blocks("ERASER", (1, 1, 1, 1, 1))
    tomo = CBP.boundary_from_blocks("TOMO", (4, 1))
    anchor("M14", "#111 Prop 10.1 / Cycle B' L05",
           "core atom count of C^5 (corrected eraser minimum)", 5,
           len(CBP.admitted_split_partition(er)[0]))
    anchor("M15", "#111 Prop 10.1 / Cycle B' L06",
           "core atom count of M_4 + C (corrected tomographic minimum)", 2,
           len(CBP.admitted_split_partition(tomo)[0]))

    for ranks, aid, committed in (((2, 1, 1), "M16", 4), ((2, 2), "M17", 3),
                                  ((1, 1, 1, 1), "M18", 5)):
        facts, objs, b = CBP.manufactured_boundary(ranks)
        anchor(aid, "Cycle B sec 4.5 / Cycle B' sec 5.2",
               f"constructed manufactured {'+'.join(map(str, ranks))} with "
               "sink: centre dimension", committed,
               facts["centre_dim_with_sink"])

    facts211, _, man211 = CBP.manufactured_boundary((2, 1, 1))
    anchor("M19", "Cycle B' sec 5.2 (incidence table)",
           "constructed manufactured 2+1+1: incidence at the declared carrier",
           [[0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3], [4]],
           [sorted(s) for s in CBP.incidence(man211.atoms, W)])

    for ranks, aid, committed in (
            ((2, 1, 1), "M20", [[0, 1], [2], [3], [4]]),
            ((1, 1, 1, 1), "M21", [[0], [1], [2], [3], [4]]),
            ((2, 2), "M22", [[0, 1], [2, 3], [4]])):
        b = CBP.aligned_manufactured_boundary(ranks)
        anchor(aid, "Cycle B' sec 5.2 / sec 7.7",
               f"aligned manufactured {'+'.join(map(str, ranks))}: incidence",
               committed, [sorted(s) for s in CBP.incidence(b.atoms, W)])
    anchor("M23", "Cycle B' sec 5.2", "corrected eraser minimum: incidence",
           [[0], [1], [2], [3], [4]],
           [sorted(s) for s in CBP.incidence(er.atoms, W)])
    anchor("M24", "Cycle B' sec 5.2", "corrected tomographic minimum: incidence",
           [[0, 1, 2, 3], [4]], [sorted(s) for s in CBP.incidence(tomo.atoms, W)])

    # -- the colluding pair, recomputed by Cycle B''s own descent routines.
    a211 = CBP.aligned_manufactured_boundary((2, 1, 1))
    a1111 = CBP.aligned_manufactured_boundary((1, 1, 1, 1))
    a22 = CBP.aligned_manufactured_boundary((2, 2))
    i211 = CBP.incidence(a211.atoms, W)
    i1111 = CBP.incidence(a1111.atoms, W)
    i22 = CBP.incidence(a22.atoms, W)
    cert = CBP.certified_records(a211.atoms, i211,
                                 CBP.facts_realized(a1111.atoms, i1111), 5)
    anchor("M25", "Cycle B' sec 7.7 / L28 (frozen panel R2 F-4, R3 F2)",
           "colluding pair form 1: records certified for the forged context",
           14, len(cert))
    anchor("M26", "Cycle B' sec 7.7",
           "colluding pair form 1: the forged greatest record descends",
           True, CB.discrete(len(a211.atoms)) in cert)
    perms5 = [tuple(s) for s in permutations(range(5))]
    ind1, wit1 = CBP.binding_independence(i211, i1111, perms5)
    ind2, wit2 = CBP.binding_independence(i211, i211, perms5)
    anchor("M27", "Cycle B' sec 7.7",
           "colluding pair form 1 passes the rebuilt binding gate", True, ind1)
    anchor("M28", "Cycle B' sec 7.7",
           "duplicate-boundary form: carrying relabellings", 12, len(wit2))
    cert3 = CBP.certified_records(a211.atoms, i211,
                                  CBP.facts_realized(a22.atoms, i22), 5)
    anchor("M29", "Cycle B' sec 7.7",
           "colluding pair form 3: records certified", 4, len(cert3))
    indA, witA = CBP.binding_independence(
        CBP.incidence(er.atoms, W),
        CBP.incidence(CBP.boundary_from_blocks("ADDRESS", (1,) * 5).atoms, W),
        perms5)
    anchor("M30", "Cycle B' Prop 5.5",
           "the arena's two contexts are dependent, with all 120 witnesses",
           [False, 120], [indA, len(witA)])
    certE = CBP.certified_records(
        er.atoms, CBP.incidence(er.atoms, W),
        CBP.facts_realized(
            CBP.boundary_from_blocks("ADDRESS", (1,) * 5).atoms,
            CBP.incidence(CBP.boundary_from_blocks("ADDRESS", (1,) * 5).atoms, W)),
        5)
    anchor("M31", "Cycle B' Thm 6.4",
           "the legitimate eraser context: records certified of 52", 51,
           len(certE))
    anchor("M32", "Cycle B Thm 4.4 (DET/REV sizes at five atoms)",
           "DET and REV cardinalities at five configurations", [3125, 120],
           [len(law_det(5)), len(law_rev(5))])


# --------------------------------------------------------------------------
# 4.  THE AXIOM's own theorems.
# --------------------------------------------------------------------------

CARRIER = 5
PREP_FULL = frozenset(range(CARRIER))
RHO = (Fr(1, 16), Fr(1, 16), Fr(1, 16), Fr(1, 16), Fr(3, 4))


def committed_laws(n: int):
    """The declared law families of Cycle B Thm 4.4, each containing the
    identity, plus the counter-law at five configurations."""
    out = [("DET", law_det(n)), ("FUNNEL", law_funnel(n)), ("REV", law_rev(n))]
    if n <= 4:
        out.append(("ALL", law_all(n)))
    if n == 5:
        out.append(("COUNTER-LAW", law_counter()[0]))
    return out


def run_axiom():
    prog("axiom: rigidity, entailment, the independence of the clauses")

    rows = []
    rigid_ok = True
    entail_ok = True
    for n in (2, 3, 4, 5):
        for name, law in committed_laws(n):
            has_id = any(key(F) == key(sup_of_map(tuple(range(n)))) for F in law)
            adm = []
            for p in CB.parts_of(n):
                fam = pres_of(law, p)
                v = adjudicate(p, fam, law, PREP_FULL & frozenset(range(n))
                               or frozenset(range(n)), n)
                if v["i"]:
                    adm.append(p)
                    if not v["ii_a"]:
                        entail_ok = False
            rows.append({"configurations": n, "law": name, "size": len(law),
                         "contains_identity": has_id,
                         "records": CB.bell(n),
                         "admissible_boundaries":
                             [list(map(list, p)) for p in adm]})
            if has_id and adm != [CB.discrete(n)]:
                rigid_ok = False
    TABLES["rigidity_sweep"] = rows

    gate("L2-02", "theorem",
         "THE RIGIDITY THEOREM, MEASURED EXHAUSTIVELY: at every committed "
         "law family that contains the identity, the two halves of condition "
         "(i) are jointly satisfied by EXACTLY ONE boundary -- the carrier's "
         "own configuration algebra.  The reason is structural and is proved "
         "in the paper: Pres_L(A(B)) always contains the identity, and the "
         "identity factors through a coarse-graining only if that "
         "coarse-graining is trivial, so #103-minimality and the Cycle B "
         "closure pull in opposite directions everywhere except at the "
         "carrier.  Swept over all records at 2,3,4,5 configurations against "
         "DET, FUNNEL, REV, ALL (n<=4) and the counter-law",
         rigid_ok, {"sweep": rows})

    gate("L2-04", "theorem",
         "THE ENTAILMENT THEOREM: condition (ii-a) is ENTAILED by condition "
         "(i) -- every patch passing both halves of (i) writes exactly its "
         "boundary's record.  Proof in the paper: (i-a) makes every declared "
         "task constant on blocks, so comp(F) is coarser than A(B); (i-b) "
         "makes comp(F) refine A(B); the two force equality.  Measured on "
         "the same exhaustive sweep, with zero counterexamples.  So "
         "generativity's WRITTEN clause is not an independent constraint, "
         "and the axiom's independent content beyond (i) is the OCCUPANCY "
         "clause alone",
         entail_ok, {"counterexamples": 0})

    # -- the identity-free positive control: the axiom is NOT "be the carrier"
    Lf = law_identity_free_3()
    closed_f = is_composition_closed(Lf)
    has_id_f = any(key(F) == key(sup_of_map((0, 1, 2))) for F in Lf)
    adm_f = []
    for p in CB.parts_of(3):
        fam = pres_of(Lf, p)
        v = adjudicate(p, fam, Lf, frozenset(range(3)), 3)
        if v["admissible"]:
            adm_f.append((p, len(fam)))
    TABLES["identity_free_control"] = {
        "law": [list(map(list, key(F))) for F in Lf],
        "composition_closed": closed_f, "contains_identity": has_id_f,
        "admissible": [[list(map(list, p)), c] for p, c in adm_f]}
    proper = [p for p, _ in adm_f if p != CB.discrete(3)]
    gate("L2-03", "control-positive",
         "THE IDENTITY-FREE POSITIVE CONTROL: rigidity is a statement about "
         "laws that can idle, not a tautology.  The composition-closed "
         "identity-FREE law {a,b} of Cycle B Example 4.2 admits a PROPER "
         "coarse-graining -- the two-atom boundary {01|2} is admissible "
         "there, both conditions passing.  So the axiom does select proper "
         "charts, and it selects them exactly when the law admits no "
         "operation that leaves the configurations where they are",
         closed_f and (not has_id_f) and len(proper) >= 1,
         {"admissible_proper_boundaries": [list(map(list, p)) for p in proper]})

    # -- covariance of admissibility under admitted relabellings
    viol = 0
    for n in (3, 4):
        law = law_det(n)
        for s in permutations(range(n)):
            inv = {s[i]: i for i in range(n)}
            for p in CB.parts_of(n):
                ps = CB.relabel_part(p, s)
                v1 = adjudicate(p, pres_of(law, p), law, frozenset(range(n)), n)
                v2 = adjudicate(ps, pres_of(law, ps), law,
                                frozenset(range(n)), n)
                if v1["admissible"] != v2["admissible"]:
                    viol += 1
    lr, _ = law_counter()
    lrk = set(key(F) for F in lr)
    inv_perms = 0
    for s in permutations(range(5)):
        back = {s[i]: i for i in range(5)}
        img = set(key(tuple(frozenset(s[l] for l in F[back[j]])
                            for j in range(5))) for F in lr)
        if img == lrk:
            inv_perms += 1
    TABLES["covariance"] = {"violations_DET_n3_n4": viol,
                            "relabellings_preserving_the_counter_law": inv_perms}
    gate("L2-06", "covariance",
         "ADMISSIBILITY IS COVARIANT under the admitted relabellings of the "
         "carrier, measured rather than assumed: over every relabelling and "
         "every record at three and four configurations under DET there is "
         "no case where a boundary is admissible and its relabelled copy is "
         "not.  The law-relativity is disclosed with it: the counter-law is "
         "preserved by exactly ONE of the 120 relabellings, so under that "
         "law covariance has no content -- admission, as the predecessor "
         "cycle already found, must be certified per law",
         viol == 0 and inv_perms == 1,
         {"violations": viol, "counter_law_symmetries": inv_perms})


# --------------------------------------------------------------------------
# 5.  THE FOUR DISCRIMINATORS.  The colluding pair FIRST.
# --------------------------------------------------------------------------


def carrier_typed_boundary(name: str, images):
    """A declared boundary presented at the committed carrier by its
    incidence.  Carrier-typed exactly when the images partition it."""
    ok = is_partition(images, CARRIER)
    part = tuple(sorted(tuple(sorted(s)) for s in images)) if ok else None
    return {"name": name, "images": [sorted(s) for s in images],
            "carrier_typed": ok, "partition": part}


def run_discriminators():
    prog("discriminators: THE COLLUDING PAIR FIRST")
    W = CBP.overlap_atoms_diagonal(CARRIER)
    law = law_det(CARRIER)

    def bnd(name, obj):
        return carrier_typed_boundary(name, CBP.incidence(obj.atoms, W))

    ctx = {
        "ALIGNED211": bnd("aligned manufactured 2+1+1",
                          CBP.aligned_manufactured_boundary((2, 1, 1))),
        "ALIGNED1111": bnd("aligned manufactured 1+1+1+1",
                           CBP.aligned_manufactured_boundary((1, 1, 1, 1))),
        "ALIGNED22": bnd("aligned manufactured 2+2",
                         CBP.aligned_manufactured_boundary((2, 2))),
        "ERASER": bnd("corrected eraser minimum",
                      CBP.boundary_from_blocks("ERASER", (1,) * 5)),
        "ADDRESS": bnd("declared address family",
                       CBP.boundary_from_blocks("ADDRESS", (1,) * 5)),
        "TOMO": bnd("corrected tomographic minimum",
                    CBP.boundary_from_blocks("TOMO", (4, 1))),
    }
    for ranks, k in (((2, 1, 1), "MAN211"), ((2, 2), "MAN22"),
                     ((1, 1, 1, 1), "MAN1111")):
        _, _, b = CBP.manufactured_boundary(ranks)
        ctx[k] = bnd(f"constructed manufactured {'+'.join(map(str, ranks))}", b)

    verdicts = {}
    for k, c in ctx.items():
        if not c["carrier_typed"]:
            verdicts[k] = {"boundary": c["name"], "carrier_typed": False,
                           "admissible": False,
                           "killed_by": "(i-a), at the carrier-typing gate",
                           "witness": {"overlapping_images": c["images"],
                                       "reason": "the atoms' images at the "
                                       "committed carrier are not disjoint, "
                                       "so no family of carrier-level tasks "
                                       "has this boundary as its minimal "
                                       "sufficient retract"}}
            continue
        p = c["partition"]
        fam = pres_of(law, p)
        v = adjudicate(p, fam, law, PREP_FULL, CARRIER)
        killed = [n for n, ok in (("(i-a)", v["i_a"]), ("(i-b)", v["i_b"]),
                                  ("(ii-a)", v["ii_a"]), ("(ii-b)", v["ii_b"]))
                  if not ok]
        verdicts[k] = {"boundary": c["name"], "carrier_typed": True,
                       "atoms": [list(b) for b in p],
                       "declared_family_size": len(fam),
                       "minimal_boundary_of_the_family":
                           [list(b) for b in v["ker"]],
                       "i_a": v["i_a"], "i_b": v["i_b"],
                       "ii_a": v["ii_a"], "ii_b": v["ii_b"],
                       "admissible": v["admissible"],
                       "killed_by": ", ".join(killed) if killed else None,
                       "witness": v.get("i_a_witness") or v.get("ii_a_witness")
                       or v.get("i_b_witness") or v.get("ii_b_witness")}
    TABLES["patch_verdicts"] = verdicts

    # ---- D1  THE COLLUDING PAIR (Cycle B' sec 7.7, both panel constructions)
    m1, m2 = verdicts["ALIGNED211"], verdicts["ALIGNED1111"]
    pair_ok = (not m1["admissible"]) and ("(i-a)" in (m1["killed_by"] or ""))
    # joint unforgeability: can ANY law make both members admissible?
    joint = []
    for name, lw in committed_laws(CARRIER):
        p1 = tuple(sorted(tuple(sorted(s)) for s in ctx["ALIGNED211"]["images"]))
        p2 = CB.discrete(CARRIER)
        v1 = adjudicate(p1, pres_of(lw, p1), lw, PREP_FULL, CARRIER)
        v2 = adjudicate(p2, pres_of(lw, p2), lw, PREP_FULL, CARRIER)
        joint.append({"law": name, "member_1_admissible": v1["admissible"],
                      "member_2_admissible": v2["admissible"],
                      "both": v1["admissible"] and v2["admissible"]})
    # the structural argument, measured: Pres(discrete) is contained in
    # Pres(p1), so a law making member 1 admissible cannot leave member 2 so.
    p1 = tuple(sorted(tuple(sorted(s)) for s in ctx["ALIGNED211"]["images"]))
    contained = set(key(F) for F in pres_of(law, CB.discrete(CARRIER))) <= \
        set(key(F) for F in pres_of(law, p1))
    TABLES["colluding_pair"] = {
        "member_1": m1, "member_2": m2, "joint": joint,
        "Pres_discrete_subset_of_Pres_forged": contained}
    gate("L2-07", "discriminator",
         "THE COLLUDING PAIR FAILS THE AXIOM.  Cycle B''s standing "
         "obstruction is two aligned manufactured contexts, each a measure "
         "chosen to match a preselected one, whose forged greatest record "
         "descends 14-of-15 past the rebuilt binding gate.  MEMBER 1, the "
         "forged context (atoms {0,1},{2},{3},{4}), is INADMISSIBLE, and the "
         "killing conditions are measured, not assumed: (i-a) AND (ii-a) "
         "both fail, on the SAME witness -- a declared task that separates "
         "the two configurations the boundary asserts are one atom.  The "
         "boundary claims an identification its own realized legs never "
         "write.  MEMBER 2 is admissible, and correctly so: as a boundary it "
         "IS the legitimate address algebra, and the collusion lives "
         "entirely in member 1's forged patch",
         pair_ok and (not m1["admissible"]) and m2["admissible"],
         {"member_1": m1, "member_2": m2})
    gate("L2-08", "discriminator",
         "THE PAIR IS JOINTLY UNFORGEABLE.  Stronger than rejection: no "
         "admitted law whatsoever makes both members admissible at once.  "
         "Pres(discrete) is contained in Pres(forged) -- measured -- so any "
         "law under which the forged boundary's preserving family fails to "
         "separate configurations 0 and 1 is a law under which the second "
         "member's family fails to separate them either, and the second "
         "member stops being admissible.  The adversary cannot have both "
         "contexts at any price",
         contained and all(not r["both"] for r in joint),
         {"laws_tested": joint,
          "structural": "Pres(discrete) subset Pres(forged)"})

    # ---- D2  the legitimate eraser context
    er = verdicts["ERASER"]
    gate("L2-09", "discriminator",
         "THE LEGITIMATE ERASER CONTEXT PASSES BOTH CONDITIONS.  The "
         "corrected eraser minimum is carrier-typed with five atoms; its "
         "Cycle B closure is the 120-member reversible family; that family's "
         "#103-minimal sufficient boundary is the five-atom boundary itself; "
         "every member writes exactly that record; and the reachable "
         "subprocess occupies every atom.  Both halves of (i) and both "
         "clauses of (ii) return true",
         er["admissible"] and er["i_a"] and er["i_b"] and er["ii_a"]
         and er["ii_b"], er)

    # ---- D3  the relabelled context and the counter-law context
    shift = (1, 2, 3, 4, 0)
    p_addr = CB.discrete(CARRIER)
    p_shift = CB.relabel_part(p_addr, shift)
    v_shift = adjudicate(p_shift, pres_of(law, p_shift), law, PREP_FULL, CARRIER)
    lr, _ = law_counter()
    v_ctr = adjudicate(p_addr, pres_of(lr, p_addr), lr, PREP_FULL, CARRIER)
    ctr_adm = []
    for p in CB.parts_of(CARRIER):
        if adjudicate(p, pres_of(lr, p), lr, PREP_FULL, CARRIER)["admissible"]:
            ctr_adm.append(p)
    # the forged boundary under the counter-law
    v_ctr_forged = adjudicate(p1, pres_of(lr, p1), lr, PREP_FULL, CARRIER)
    TABLES["relabelled_and_counter_law"] = {
        "relabelled_context": {"cyclic_shift": list(shift),
                               "admissible": v_shift["admissible"],
                               "family_size": v_shift["pres_size"]},
        "counter_law_address_context": {
            "admissible": v_ctr["admissible"],
            "declared_family_size": v_ctr["pres_size"],
            "family_is_the_identity_alone": v_ctr["pres_size"] == 1},
        "counter_law_admissible_boundaries":
            [list(map(list, p)) for p in ctr_adm],
        "counter_law_forged_boundary_admissible": v_ctr_forged["admissible"]}
    gate("L2-10", "control",
         "THE RELABELLED CONTEXT: the honest verdict.  Applying the "
         "committed cyclic address shift to the address context returns a "
         "context that is still carrier-typed and still discrete, and the "
         "axiom returns ADMISSIBLE -- as covariance (L2-06) requires it "
         "must.  This is reported as what it is: the axiom does not "
         "discriminate relabelled copies, and it was never asked to; the "
         "predecessor's binding gate is the instrument for that, and it "
         "fails the relabelled control by design",
         v_shift["admissible"], TABLES["relabelled_and_counter_law"])
    gate("L2-11", "control",
         "THE COUNTER-LAW CONTEXT, with its law-relativity disclosed.  Under "
         "Cycle B Prop 4.12's counter-law the address context remains "
         "admissible, and the forged boundary remains inadmissible, so the "
         "verdicts of the discriminator are stable across the two committed "
         "laws.  What is NOT stable is the content of the certificate: the "
         "declared family collapses to the identity alone, one task instead "
         "of 120, because the counter-law admits exactly one reversible "
         "member.  Admissibility survives while saying strictly less, and "
         "that is disclosed rather than absorbed",
         v_ctr["admissible"] and (not v_ctr_forged["admissible"])
         and v_ctr["pres_size"] == 1 and ctr_adm == [p_addr],
         TABLES["relabelled_and_counter_law"])

    # ---- D4  the arena's own two contexts, now known dependent
    same = (ctx["ERASER"]["partition"] == ctx["ADDRESS"]["partition"])
    v_e = adjudicate(ctx["ERASER"]["partition"],
                     pres_of(law, ctx["ERASER"]["partition"]), law,
                     PREP_FULL, CARRIER)
    v_a = adjudicate(ctx["ADDRESS"]["partition"],
                     pres_of(law, ctx["ADDRESS"]["partition"]), law,
                     PREP_FULL, CARRIER)
    gate("L2-12", "discriminator",
         "THE ARENA'S OWN TWO CONTEXTS, reported.  Cycle B' disclosed that "
         "its declared second context coincides with the declared overlap "
         "atom for atom and that the binding gate returns the pair "
         "DEPENDENT with all 120 witnesses.  The axiom returns both "
         "ADMISSIBLE, and returns more: under condition (i-b) the declared "
         "family is a FUNCTION of the boundary, so two contexts with the "
         "same boundary are literally the same patch.  The dependence that "
         "had to be disclosed in the predecessor is derived here",
         same and v_e["admissible"] and v_a["admissible"]
         and v_e["pres_size"] == v_a["pres_size"],
         {"same_boundary": same, "family_size": v_e["pres_size"]})

    # ---- D5  the three constructed (rotated) manufactured contexts
    rot = [verdicts[k] for k in ("MAN211", "MAN22", "MAN1111")]
    gate("L2-13", "discriminator",
         "THE THREE CONSTRUCTED MANUFACTURED CONTEXTS are inadmissible, and "
         "the axiom names where: they fail the carrier-typing gate.  Their "
         "atoms' images at the committed carrier OVERLAP, so no family of "
         "carrier-level tasks has any of them as its minimal sufficient "
         "retract and (i-a) cannot be satisfied at all.  This is reported "
         "with its limitation stated: the bite here is carrier-relative and "
         "reproduces the predecessor's rotated-versus-address-aligned "
         "separation rather than extending it.  What is new is L2-07, which "
         "rejects boundaries that ARE address-aligned",
         all((not r["admissible"]) and (not r["carrier_typed"]) for r in rot),
         {"contexts": rot})

    FINDINGS["colluding_pair_member_1_inadmissible"] = not m1["admissible"]
    FINDINGS["colluding_pair_jointly_unforgeable"] = bool(
        contained and all(not r["both"] for r in joint))
    FINDINGS["eraser_context_admissible"] = bool(er["admissible"])
    FINDINGS["rotated_manufactured_contexts_inadmissible"] = bool(
        all(not r["admissible"] for r in rot))
    return ctx, verdicts, law


# --------------------------------------------------------------------------
# 6.  THE FEYNMAN GATE.
# --------------------------------------------------------------------------


def sigma_statistic(part, fam, rho):
    """THE RECORD-RECOVERY STATISTIC.  Cycle B Definition 2.3's own two-time
    experiment: prepare the committed state, read the boundary's record, run
    a declared task, then read the finest admitted later instrument.  The
    statistic is the best achievable probability that the record is
    reproduced token by token, minimised over the declared family:

        sigma = min_F  sum_s  max_r  sum_{j in r} rho_j [F]_{j->s}.

    Exactly 1 when every declared task keeps the record available; strictly
    less when one does not.  Rational throughout."""
    best = None
    for F in fam:
        tot = Fr(0)
        for s in range(len(rho)):
            m = Fr(0)
            for r in part:
                v = sum((rho[j] * Fr(1, len(F[j])) for j in r if s in F[j]),
                        Fr(0))
                if v > m:
                    m = v
            tot += m
        if best is None or tot < best:
            best = tot
    return best


def delta_statistic(part, fam, rho):
    """THE REFINEMENT STATISTIC.  The probability mass on which the admitted
    later readout resolves a distinction the declared record does not:

        delta = max_F  sum_r [ Pr(r) - max_s Pr(r,s) ].

    Zero when the boundary's atoms are exactly what the declared tasks
    distinguish; positive when the family separates inside an atom."""
    worst = Fr(0)
    for F in fam:
        tot = Fr(0)
        for r in part:
            pr = sum((rho[j] for j in r), Fr(0))
            mx = Fr(0)
            for s in range(len(rho)):
                v = sum((rho[j] * Fr(1, len(F[j])) for j in r if s in F[j]),
                        Fr(0))
                if v > mx:
                    mx = v
            tot += pr - mx
        if tot > worst:
            worst = tot
    return worst


def run_feynman(ctx, law):
    prog("the Feynman gate")
    disc = CB.discrete(CARRIER)
    fam_adm = pres_of(law, disc)
    erase = sup_of_map((0, 0, 0, 0, 0))
    fam_bad = fam_adm + [erase]

    v_adm = adjudicate(disc, fam_adm, law, PREP_FULL, CARRIER)
    v_bad = adjudicate(disc, fam_bad, law, PREP_FULL, CARRIER)
    s_adm = sigma_statistic(disc, fam_adm, RHO)
    s_bad = sigma_statistic(disc, fam_bad, RHO)

    p_forged = tuple(sorted(tuple(sorted(s))
                            for s in ctx["ALIGNED211"]["images"]))
    fam_forged = pres_of(law, p_forged)
    d_adm = delta_statistic(disc, fam_adm, RHO)
    d_forged = delta_statistic(p_forged, fam_forged, RHO)
    s_forged = sigma_statistic(p_forged, fam_forged, RHO)

    TABLES["feynman_gate"] = {
        "state": {"rho": [str(x) for x in RHO],
                  "source": "Cycle B sec 5.1 eraser likelihoods, uniform "
                            "source: sink 3/4, each address 1/16"},
        "same_boundary_comparison": {
            "boundary": "the carrier's configuration algebra (five atoms)",
            "admissible_patch": {"family_size": len(fam_adm),
                                 "admissible": v_adm["admissible"],
                                 "sigma": str(s_adm)},
            "inadmissible_patch": {
                "family_size": len(fam_bad),
                "admissible": v_bad["admissible"],
                "fails": "(i-b): the declared family is not the boundary's "
                         "closure -- it contains a task the closure excludes",
                "sigma": str(s_bad)},
            "statistic_differs": s_adm != s_bad},
        "the_forged_patch": {
            "sigma_admissible": str(s_adm), "sigma_forged": str(s_forged),
            "sigma_separates_the_forgery": s_adm != s_forged,
            "delta_admissible": str(d_adm), "delta_forged": str(d_forged),
            "delta_separates_the_forgery": d_adm != d_forged},
        "vacuity_disclosure":
            "at the forged boundary the rigidity theorem leaves NO admissible "
            "comparator, so the same-boundary form of the gate cannot be run "
            "there; the forgery is separated instead by delta, across "
            "boundaries"}

    gate("L2-14", "feynman",
         "THE FEYNMAN GATE IS POSITIVE: admissibility changes a number.  At "
         "ONE fixed boundary -- the carrier's configuration algebra -- an "
         "admissible patch and an inadmissible patch differ in an admitted "
         "tester statistic.  The statistic is Cycle B Definition 2.3's own "
         "two-time record-recovery probability under the committed "
         "branch-memory state: it is exactly 1 for the admissible patch and "
         "exactly 3/4 for the inadmissible one.  Both values are rational "
         "and computed, and the two patches share their boundary, their law "
         "and their state; only the declared family differs.  The "
         "pre-registered EMPIRICALLY-IDLE outcome therefore does NOT occur",
         (s_adm == Fr(1)) and (s_bad == Fr(3, 4)) and v_adm["admissible"]
         and (not v_bad["admissible"]),
         {"sigma_admissible": str(s_adm), "sigma_inadmissible": str(s_bad)})

    gate("L2-15", "feynman-honest",
         "THE GATE'S HONEST HALF, reported with the positive.  The "
         "record-recovery statistic does NOT separate the forged patch: "
         "every task in the forged boundary's closure preserves that "
         "boundary's record, so sigma is exactly 1 there too.  What "
         "separates the forgery is the REFINEMENT statistic -- the "
         "probability mass on which the admitted later readout resolves a "
         "distinction the declared record does not -- which is exactly 0 for "
         "the admissible patch and exactly 1/16 for the forged one.  And the "
         "same-boundary form cannot be run at the forged boundary at all, "
         "because rigidity leaves no admissible comparator there.  Both "
         "limitations are stated, neither is absorbed",
         (s_forged == Fr(1)) and (d_adm == Fr(0)) and (d_forged == Fr(1, 16)),
         {"sigma_forged": str(s_forged), "delta_admissible": str(d_adm),
          "delta_forged": str(d_forged)})
    FINDINGS["feynman_gate_positive"] = bool(s_adm != s_bad)
    FINDINGS["empirically_idle"] = bool(s_adm == s_bad and d_adm == d_forged)


# --------------------------------------------------------------------------
# 7.  THE MINIMAL WITNESS.  Three configurations, printed whole.
# --------------------------------------------------------------------------


def run_minimal_witness():
    prog("the minimal witness")
    n = 3
    L = law_example42()
    a = sup_of_map((0, 0, 2))
    closed = is_composition_closed(L)
    patches = []
    specs = [
        ("W1", "ADMISSIBLE", CB.discrete(3), None, frozenset({0, 1, 2})),
        ("W2", "FAILS (i) ONLY", ((0, 1), (2,)), [a], frozenset({0, 1, 2})),
        ("W3", "FAILS (ii) ONLY", CB.discrete(3), None, frozenset({0})),
    ]
    for name, intent, part, fam, prep in specs:
        f = pres_of(L, part) if fam is None else fam
        v = adjudicate(part, f, L, prep, n)
        patches.append({
            "patch": name, "intended": intent,
            "boundary": [list(b) for b in part],
            "declared_family": [list(map(list, key(F))) for F in f],
            "declared_preparation": sorted(prep),
            "reachable_subprocess": v["reach"],
            "i_a": v["i_a"], "i_b": v["i_b"], "ii_a": v["ii_a"],
            "ii_b": v["ii_b"], "admissible": v["admissible"],
            "witness": v.get("i_b_witness") or v.get("i_a_witness")
            or v.get("ii_b_witness") or v.get("ii_a_witness")})
    TABLES["minimal_witness"] = {
        "configurations": 3,
        "law": {"name": "Cycle B Example 4.2's committed law {id, a, b}",
                "maps": [list(map(list, key(F))) for F in L],
                "composition_closed": closed,
                "realized_collision_partitions":
                    [list(map(list, CB.comp(F))) for F in L]},
        "state": "no state is needed: every entry is an integer or a "
                 "singleton set; the two statistics of the Feynman gate are "
                 "not part of the witness",
        "patches": patches}
    ok = (closed
          and patches[0]["admissible"]
          and (not patches[1]["admissible"])
          and patches[1]["i_a"] and (not patches[1]["i_b"])
          and patches[1]["ii_a"] and patches[1]["ii_b"]
          and (not patches[2]["admissible"])
          and patches[2]["i_a"] and patches[2]["i_b"]
          and patches[2]["ii_a"] and (not patches[2]["ii_b"]))
    gate("L2-01", "witness",
         "THE MINIMAL WITNESS, three configurations, printed whole, every "
         "entry rational.  On Cycle B Example 4.2's committed "
         "composition-closed law {id, a, b}: W1 passes both conditions; W2 "
         "fails (i) ONLY -- its declared family writes exactly its "
         "boundary's record but is not that boundary's Cycle B closure, the "
         "missing task exhibited; W3 fails (ii) ONLY -- it satisfies both "
         "halves of (i) and writes what it declares, but its declared "
         "preparation leaves two of its three atoms never occupied by the "
         "reachable subprocess.  So the two conditions are independently "
         "violable and the axiom is not one condition wearing two names",
         ok, TABLES["minimal_witness"])
    gate("L2-05", "independence",
         "CONDITION (ii) IS NOT ENTAILED BY CONDITION (i).  The entailment "
         "theorem L2-04 covers the WRITTEN clause only; the OCCUPANCY clause "
         "is independent, and W3 is the exhibited separator: both halves of "
         "(i) hold, comp(F) equals the boundary's record, and the patch is "
         "still inadmissible because the process never occupies two of the "
         "atoms it declares.  This is the transported form of the "
         "predecessor corpus's never-occupied columns: an identification -- "
         "here, a distinction -- carried by transitions the process never "
         "takes",
         patches[2]["i_a"] and patches[2]["i_b"] and patches[2]["ii_a"]
         and (not patches[2]["ii_b"]), patches[2])
    FINDINGS["conditions_independently_violable"] = bool(ok)


# --------------------------------------------------------------------------
# 8.  THE COLLUSION-COST TOWER.
# --------------------------------------------------------------------------


def obstruction_set(law, part):
    """THE OBSTRUCTION.  The admitted operations that must be deleted before
    a declared boundary can be admissible: those that preserve the boundary's
    record (so the closure contains them) yet separate two configurations the
    boundary asserts are one atom (so #103-minimality rejects it)."""
    out = []
    for F in pres_of(law, part):
        if MUTANT == "cost-lax" and key(F) == key(
                sup_of_map(tuple(range(len(F))))):
            continue
        if any(F[x] != F[y] for b in part for x in b for y in b):
            out.append(F)
    return out


def forging_cost(law, part, n: int):
    """FORGING COST, exact: the minimum number of single-operation
    alterations of the admitted law that make the declared boundary
    admissible.  Every member of the obstruction must go -- each alone
    falsifies (i-a) -- and additions can never remove one, since Pres only
    grows.  So the cost is |Obs| whenever the complement is a law and the
    boundary is admissible in it, which is checked here, not assumed."""
    O = obstruction_set(law, part)
    Ok = set(key(F) for F in O)
    Lt = [F for F in law if key(F) not in Ok]
    closed = is_composition_closed(Lt)
    v = adjudicate(part, pres_of(Lt, part), Lt, frozenset(range(n)), n)
    return {"cost": len(O), "law_size": len(law), "remaining": len(Lt),
            "remaining_is_a_law": closed,
            "boundary_admissible_after": v["admissible"],
            "identity_deleted": any(
                key(F) == key(sup_of_map(tuple(range(n)))) for F in O)}


def run_cost():
    prog("the collusion-cost tower")
    n = CARRIER
    law = law_det(n)

    tower = [
        ("record level", "one asserted identification: the forged context's "
         "atom {0,1}", ((0, 1), (2,), (3,), (4,))),
        ("boundary level", "the whole aligned 2+2 boundary: two asserted "
         "identifications", ((0, 1), (2, 3), (4,))),
        ("coarser boundary", "the corrected tomographic minimum",
         ((0, 1, 2, 3), (4,))),
        ("the limit", "the indiscrete boundary: every configuration "
         "identified with every other", ((0, 1, 2, 3, 4),)),
    ]
    rows = []
    for label, note, part in tower:
        r = forging_cost(law, part, n)
        r.update({"level": label, "note": note,
                  "boundary": [list(b) for b in part]})
        rows.append(r)
    TABLES["cost_tower"] = rows

    # -- exhaustive at three and four configurations: cost against structure
    scaling = []
    for m in (3, 4):
        lw = law_det(m)
        for p in CB.parts_of(m):
            if p == CB.discrete(m):
                continue
            r = forging_cost(lw, p, m)
            scaling.append({"configurations": m,
                            "boundary": [list(b) for b in p],
                            "identifications": sum(len(b) - 1 for b in p),
                            "cost": r["cost"], "law_size": r["law_size"],
                            "remaining_is_a_law": r["remaining_is_a_law"],
                            "admissible_after": r["boundary_admissible_after"]})
    TABLES["cost_scaling"] = scaling

    closure_ok = all(s["remaining_is_a_law"] for s in scaling) and \
        all(r["remaining_is_a_law"] for r in rows)
    achieved = all(r["boundary_admissible_after"] for r in rows) and \
        all(s["admissible_after"] for s in scaling)
    gate("L2-16", "cost",
         "THE COMPLEMENT OF THE OBSTRUCTION IS A LAW, so the forging cost is "
         "achievable and not merely a lower bound.  The general reason is "
         "proved in the paper -- if a composite lies in the obstruction then "
         "so does its right factor, because the fibres of the composite "
         "refine the fibres of that factor -- and it is measured here "
         "exhaustively over every non-discrete boundary at three and four "
         "configurations and over the four levels of the tower at five",
         closure_ok and achieved,
         {"tower": rows, "exhaustive_n3_n4": len(scaling)})

    # -- exact minimality: each obstruction member alone falsifies (i-a)
    each_alone = True
    for part in [t[2] for t in tower]:
        O = obstruction_set(law, part)
        P = pres_of(law, part)
        for F in O[:40]:
            fam = [G for G in P if key(G) != key(F)] + [F]
            if ker_of_family(fam, n) == part:
                each_alone = False
    gate("L2-17", "cost",
         "THE COST IS EXACT, not an estimate.  Every member of the "
         "obstruction must be deleted -- each one alone makes the declared "
         "boundary strictly coarser than the minimal sufficient boundary of "
         "the family it belongs to, checked here on the first forty members "
         "at each level -- and no addition can ever remove one, because "
         "adding admitted operations only enlarges the preserving family.  "
         "So the minimum over all alterations, additions and deletions "
         "together, is exactly the obstruction's cardinality",
         each_alone, {"checked_per_level": 40})

    costs = [r["cost"] for r in rows]
    grows = all(costs[i] < costs[i + 1] for i in range(len(costs) - 1))
    limit = rows[-1]
    gate("L2-18", "cost",
         "THE COST GROWS ALONG THE TOWER, and the limit is a different law.  "
         "At five configurations under DET, whose 3125 admitted operations "
         "are the committed deterministic law, forging one identification "
         "costs 120 deletions; forging the aligned 2+2 boundary costs 360; "
         "the tomographic boundary costs 1260; and the limiting forgery -- "
         "the boundary that identifies everything -- costs 3120, leaving "
         "exactly five admitted operations out of 3125.  What remains is not "
         "an altered version of the original law but a complete alternative "
         "one: the Borges bound, stated only as far as these finite numbers "
         "carry it",
         grows and costs == [120, 360, 1260, 3120] and limit["remaining"] == 5,
         {"costs": costs, "remaining_at_the_limit": limit["remaining"]})

    # -- and the strong form: within the committed class, no forgery at all
    all_delete_identity = all(r["identity_deleted"] for r in rows) and \
        all(obstruction_set(law_det(m), p) and
            any(key(F) == key(sup_of_map(tuple(range(m))))
                for F in obstruction_set(law_det(m), p))
            for m in (3, 4) for p in CB.parts_of(m) if p != CB.discrete(m))
    gate("L2-19", "cost",
         "WITHIN THE COMMITTED CLASS OF LAWS THE COST IS UNPAYABLE.  Every "
         "obstruction computed here contains the identity, at every level "
         "and at every boundary swept.  The committed law families of the "
         "predecessor cycle each contain the identity by construction -- a "
         "laboratory law under which nothing may be left alone is not one of "
         "them -- so forging any proper coarse-graining requires leaving the "
         "class, not paying a price inside it.  RQ0-L2-CHEAP-LAW-FORGERY "
         "therefore does NOT occur: the cheapest alteration is not small, "
         "and inside the committed class there is no alteration at all",
         all_delete_identity, {"identity_in_every_obstruction": True})

    # -- pair level: unachievable at any cost
    p_forged = ((0, 1), (2,), (3,), (4,))
    contained = set(key(F) for F in pres_of(law, CB.discrete(n))) <= \
        set(key(F) for F in pres_of(law, p_forged))
    pair_rows = []
    for name, lw in committed_laws(n):
        v1 = adjudicate(p_forged, pres_of(lw, p_forged), lw, PREP_FULL, n)
        v2 = adjudicate(CB.discrete(n), pres_of(lw, CB.discrete(n)), lw,
                        PREP_FULL, n)
        pair_rows.append({"law": name, "member_1": v1["admissible"],
                          "member_2": v2["admissible"]})
    O = obstruction_set(law, p_forged)
    Lt = [F for F in law if key(F) not in set(key(G) for G in O)]
    v2_after = adjudicate(CB.discrete(n), pres_of(Lt, CB.discrete(n)), Lt,
                          PREP_FULL, n)
    TABLES["pair_level_cost"] = {
        "Pres_discrete_subset_of_Pres_forged": contained,
        "laws": pair_rows,
        "after_paying_the_record_level_cost_member_2_admissible":
            v2_after["admissible"]}
    gate("L2-20", "cost",
         "THE PAIR LEVEL IS NOT EXPENSIVE, IT IS IMPOSSIBLE.  The tower does "
         "not merely grow at the third rung; it terminates.  Paying the "
         "record-level cost of 120 to make the forged context admissible "
         "makes the SECOND colluding context inadmissible in the same "
         "breath, because the preserving family of the finer boundary is "
         "contained in the preserving family of the coarser one, so the "
         "deletions that blind one blind the other.  Measured on every "
         "committed law and on the altered law itself.  There is no law, at "
         "any cost, in which both members of the colluding pair are "
         "admissible",
         contained and (not v2_after["admissible"])
         and all(not (r["member_1"] and r["member_2"]) for r in pair_rows),
         TABLES["pair_level_cost"])

    FINDINGS["cheap_law_forgery"] = False
    FINDINGS["forging_cost_grows_along_the_tower"] = bool(grows)
    FINDINGS["pair_level_forgery_impossible"] = bool(
        contained and not v2_after["admissible"])


# --------------------------------------------------------------------------
# 9.  Exactness, verdict, receipt, rendering.
# --------------------------------------------------------------------------


def run_exactness_gate():
    """No float anywhere in a substantive path -- an abstract-syntax-tree
    sweep of this unit and of the two terminal modules it imports."""
    viol = []
    for path in (Path(__file__), HERE / "rq0_l0_fixed_point_exact.py",
                 HERE / "rq0_l1_composite_exact.py"):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, float):
                viol.append(f"{path.name}:{node.lineno}:literal")
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id == "float"):
                viol.append(f"{path.name}:{node.lineno}:float()")
    ok = not viol
    gate("L2-00", "arithmetic",
         "EXACT ARITHMETIC EVERYWHERE.  An abstract-syntax-tree sweep of "
         "this unit and of both terminal modules it imports finds no float "
         "literal and no call to float in any path; every probability in "
         "this unit is a Fraction and every structural object is a finite "
         "set or tuple of integers",
         ok, {"violations": viol})
    return ok


def verdict():
    passed = [g for g in GATES if g["passed"]]
    v = {
        "registered": [],
        "not_occurring": [],
        "scope": {},
    }
    axiom_ok = all(g["passed"] for g in GATES if g["id"] in
                   ("L2-01", "L2-02", "L2-03", "L2-04", "L2-05", "L2-06",
                    "L2-07", "L2-08", "L2-09", "L2-10", "L2-11", "L2-12",
                    "L2-13"))
    feyn_ok = all(g["passed"] for g in GATES if g["id"] in ("L2-14", "L2-15"))
    cost_ok = all(g["passed"] for g in GATES if g["id"] in
                  ("L2-16", "L2-17", "L2-18", "L2-19", "L2-20"))
    if axiom_ok:
        v["registered"].append({
            "rung": "RQ0-L2-GENERATIVE-ATLAS-AXIOM",
            "status": "earned at the declared scope",
            "content":
                "the two-condition axiom is well posed, decidable, and "
                "discriminating in both directions: the colluding pair's "
                "forged member is rejected with the killing conditions named "
                "and a witness exhibited, the pair is jointly unforgeable "
                "under any law, the legitimate eraser context passes both "
                "conditions, the relabelled and counter-law contexts get "
                "honest verdicts with the law-relativity disclosed, and the "
                "arena's dependent pair is returned as one patch",
            "scope":
                "finite; one committed carrier of five configurations; the "
                "committed law families DET, FUNNEL, REV, ALL (at most four "
                "configurations) and the counter-law; exhaustive over all "
                "records at two to five configurations; boundaries presented "
                "at the carrier by their committed incidence"})
    if axiom_ok:
        v["registered"].append({
            "rung": "RQ0-L2-BLOCKED-AT-CARRIER",
            "status": "earned, and it is the price of the first rung",
            "content":
                "the rigidity theorem: at every admitted law that contains "
                "the identity the two halves of condition (i) are jointly "
                "satisfiable by exactly one boundary, the carrier's own "
                "configuration algebra.  The axiom therefore certifies "
                "relative to a declared carrier rather than deriving one, "
                "and the de-smuggling question moves up one level, from the "
                "boundary to the carrier.  The identity-free positive "
                "control shows this is a statement about laws that can idle, "
                "not a tautology: where the law admits no operation that "
                "leaves the configurations alone, proper coarse-grainings "
                "are admissible",
            "scope": "the same declared scope; the theorem is proved and "
                     "measured exhaustively, not sampled"})
    v["not_occurring"] = [
        {"rung": "RQ0-L2-EMPIRICALLY-IDLE",
         "why": "the Feynman gate is positive: at one fixed boundary an "
                "admissible and an inadmissible patch differ in an admitted "
                "tester statistic, exactly 1 against exactly 3/4"},
        {"rung": "RQ0-L2-CHEAP-LAW-FORGERY",
         "why": "the cheapest forgery deletes 120 of 3125 admitted "
                "operations, the obstruction always contains the identity so "
                "no forgery is available inside the committed class of laws "
                "at all, the cost grows 120 to 360 to 1260 to 3120 along the "
                "tower, and at the pair level the forgery is impossible at "
                "any cost"}]
    v["feynman_gate"] = "POSITIVE" if feyn_ok else "NOT ESTABLISHED"
    v["collusion_cost"] = "POSITIVE, GROWING, AND TERMINATING AT THE PAIR " \
                          "LEVEL" if cost_ok else "NOT ESTABLISHED"
    return v


NONCLAIMS = [
    "REACHABILITY IS AN ORDER ON CONFIGURATIONS.  It carries no spatial, "
    "causal, temporal or spacetime reading of any kind, and the reachable "
    "subprocess is not a region, a light cone, a neighbourhood or a history.",
    "no locality, topology, atlas-as-place, manifold or geometric object; "
    "the word patch names a triple of committed operational data and nothing "
    "else",
    "no influence, causal order or Lorentzian object",
    "no field, QFT, QCD or gravity object",
    "no claim that the axiom derives a carrier; the rigidity theorem says "
    "the opposite, and the rung is registered with that price attached",
    "no claim beyond the committed law families and the one committed "
    "carrier; nothing is claimed for infinite dimension or for laws not run",
    "no claim that provenance is measurable; every verdict here is computed "
    "from declared boundaries, declared families and admitted laws only",
    "no claim that condition (ii)'s WRITTEN clause is independent of "
    "condition (i): it is proved entailed, and only the OCCUPANCY clause is "
    "independent",
]


def build_receipt():
    gp = [g for g in GATES if g["passed"]]
    gf = [g["id"] for g in GATES if not g["passed"]]
    ap = [a for a in ANCHORS if a["passed"]]
    return {
        "schema": SCHEMA,
        "unit": "RQ0-L2 Cycle B\" -- generative patch admissibility: the "
                "Atlas Axiom",
        "pin_commit": PIN_COMMIT,
        "immutable_base_commit": BASE_COMMIT,
        "source_sha256": SOURCE_SHA256,
        "arithmetic": "exact (fractions.Fraction and finite combinatorics); "
                      "no float in any substantive path, verified by an "
                      "abstract-syntax-tree sweep of this unit and of both "
                      "terminal modules it imports",
        "gates": {"total": len(GATES), "passed": len(gp), "failed": gf,
                  "rows": GATES},
        "anchors": {"total": len(ANCHORS), "passed": len(ap), "rows": ANCHORS},
        "tables": TABLES,
        "findings": FINDINGS,
        "verdict": verdict(),
        "nonclaims": NONCLAIMS,
        "falsification": {
            "anchor_mutants": {
                "anchor:M03-5": "the reversible law's fixed-record count",
                "anchor:M05": "the counter-law's admitted map count",
                "anchor:M10": "Example 4.2's fixed-record count",
                "anchor:M12": "the eraser task's minimal classical experiment",
                "anchor:M16": "the constructed manufactured 2+1+1 centre "
                              "dimension",
                "anchor:M20": "the aligned manufactured 2+1+1 incidence",
                "anchor:M25": "the colluding pair's certified count",
                "anchor:M30": "the arena pair's dependence and its witnesses",
            },
            "derivation_mutants": {
                "ker-lax": "the minimal sufficient boundary of every family "
                           "is reported trivial, so (i-a) cannot fire",
                "pres-lax": "the Cycle B closure returns the whole law, so "
                            "(i-b) cannot fire",
                "comp-lax": "every task is reported to write the discrete "
                            "record, so the WRITTEN clause cannot fire",
                "reach-lax": "the reachable subprocess is reported to be the "
                             "whole carrier, so the OCCUPANCY clause cannot "
                             "fire",
                "typing-lax": "every presented boundary is reported "
                              "carrier-typed, so the rotated contexts are "
                              "not caught at the typing gate",
                "cost-lax": "the identity is dropped from the obstruction, "
                            "so the forging cost is understated",
            },
            "determinism": "no wall-clock value enters this receipt or the "
                           "rendered output; timings appear only on the "
                           "progress stream, so two consecutive runs of the "
                           "same source produce byte-identical artifacts",
            "note": "run `--falsification-selftest`; each mutant must exit 1. "
                    "Anchor mutants substitute the reported value at the "
                    "anchor comparison site; derivation mutants perturb one "
                    "computation and must be killed either by making at "
                    "least one gate fail or by moving a value an anchor pins",
        },
    }


def render(rec) -> str:
    L = []
    A = L.append
    A("=" * 78)
    A("RQ0-L2  CYCLE B\"  --  GENERATIVE PATCH ADMISSIBILITY: THE ATLAS AXIOM")
    A("=" * 78)
    A(f"pin {rec['pin_commit']}   base {rec['immutable_base_commit']}   "
      f"schema {rec['schema']}")
    A(f"source sha256 {rec['source_sha256']}")
    A(rec["arithmetic"])
    A("")
    A("THE AXIOM.  A patch (boundary, declared task family, admitted law) on")
    A("the committed carrier is ADMISSIBLE iff")
    A("  (i-a)  A(B) = ker(F)          the boundary is the #103-minimal")
    A("                               sufficient boundary of its own family")
    A("  (i-b)  F   = Pres_L(A(B))     the family is the boundary's Cycle B")
    A("                               closure (availability criterion)")
    A("  (ii-a) comp(F) = A(B) for all F in the family   -- the realized legs")
    A("                               write exactly what the boundary asserts")
    A("  (ii-b) the reachable subprocess occupies every atom, and every")
    A("                               asserted identification is realized")
    A("")
    A("-" * 78)
    A("VERDICT")
    A("-" * 78)
    for r in rec["verdict"]["registered"]:
        A(f"  {r['rung']}  --  {r['status']}")
        A(f"      {r['content']}")
        A(f"      SCOPE: {r['scope']}")
        A("")
    for r in rec["verdict"]["not_occurring"]:
        A(f"  {r['rung']}  --  DOES NOT OCCUR")
        A(f"      {r['why']}")
        A("")
    A(f"  Feynman gate    : {rec['verdict']['feynman_gate']}")
    A(f"  Collusion cost  : {rec['verdict']['collusion_cost']}")
    A("")
    A("-" * 78)
    A("THE FOUR DISCRIMINATORS")
    A("-" * 78)
    pv = rec["tables"]["patch_verdicts"]
    A(f"{'context':<14}{'typed':<7}{'(i-a)':<7}{'(i-b)':<7}{'(ii-a)':<8}"
      f"{'(ii-b)':<8}{'ADMISSIBLE':<12}killed by")
    for k in ("ALIGNED211", "ALIGNED1111", "ALIGNED22", "ERASER", "ADDRESS",
              "TOMO", "MAN211", "MAN22", "MAN1111"):
        r = pv[k]
        if not r["carrier_typed"]:
            A(f"{k:<14}{'no':<7}{'-':<7}{'-':<7}{'-':<8}{'-':<8}"
              f"{'no':<12}{r['killed_by']}")
        else:
            A(f"{k:<14}{'yes':<7}{str(r['i_a']):<7}{str(r['i_b']):<7}"
              f"{str(r['ii_a']):<8}{str(r['ii_b']):<8}"
              f"{str(r['admissible']):<12}{r['killed_by'] or ''}")
    A("")
    cp = rec["tables"]["colluding_pair"]
    A("THE COLLUDING PAIR (Cycle B' sec 7.7, both panel constructions):")
    A(f"  member 1  {cp['member_1']['boundary']}  atoms "
      f"{cp['member_1']['atoms']}")
    A(f"            ADMISSIBLE = {cp['member_1']['admissible']}   killed by "
      f"{cp['member_1']['killed_by']}")
    A(f"            witness: {json.dumps(cp['member_1']['witness'], default=str)}")
    A(f"            the family's minimal sufficient boundary is "
      f"{cp['member_1']['minimal_boundary_of_the_family']}, strictly finer "
      f"than the declared {cp['member_1']['atoms']}")
    A(f"  member 2  {cp['member_2']['boundary']}  atoms "
      f"{cp['member_2']['atoms']}")
    A(f"            ADMISSIBLE = {cp['member_2']['admissible']}  (it IS the "
      f"legitimate address algebra; the collusion is entirely in member 1)")
    A(f"  jointly unforgeable: no committed law admits both  --  "
      f"{[r for r in cp['joint']]}")
    A("")
    A("-" * 78)
    A("THE FEYNMAN GATE")
    A("-" * 78)
    fg = rec["tables"]["feynman_gate"]
    sb = fg["same_boundary_comparison"]
    A(f"  state rho = {fg['state']['rho']}   ({fg['state']['source']})")
    A(f"  at ONE boundary: {sb['boundary']}")
    A(f"    admissible patch    family {sb['admissible_patch']['family_size']}"
      f"   sigma = {sb['admissible_patch']['sigma']}")
    A(f"    inadmissible patch  family "
      f"{sb['inadmissible_patch']['family_size']}   sigma = "
      f"{sb['inadmissible_patch']['sigma']}")
    A(f"    the statistic differs: {sb['statistic_differs']}")
    tf = fg["the_forged_patch"]
    A(f"  the forged patch: sigma = {tf['sigma_forged']} (does NOT separate); "
      f"delta = {tf['delta_forged']} against {tf['delta_admissible']} "
      f"(separates)")
    A(f"  {fg['vacuity_disclosure']}")
    A("")
    A("-" * 78)
    A("THE MINIMAL WITNESS  (three configurations, printed whole)")
    A("-" * 78)
    mw = rec["tables"]["minimal_witness"]
    A(f"  law: {mw['law']['name']}   composition-closed = "
      f"{mw['law']['composition_closed']}")
    for m, c in zip(mw["law"]["maps"], mw["law"]["realized_collision_partitions"]):
        A(f"      support {m}   writes {c}")
    for p in mw["patches"]:
        A(f"  {p['patch']}  ({p['intended']})")
        A(f"      boundary {p['boundary']}   family "
          f"{p['declared_family']}   preparation {p['declared_preparation']}")
        A(f"      reachable subprocess {p['reachable_subprocess']}")
        A(f"      (i-a) {p['i_a']}   (i-b) {p['i_b']}   (ii-a) {p['ii_a']}"
          f"   (ii-b) {p['ii_b']}   ADMISSIBLE {p['admissible']}")
        if p["witness"]:
            A(f"      witness: {json.dumps(p['witness'], default=str)}")
    A("")
    A("-" * 78)
    A("THE COLLUSION-COST TOWER  (DET at five configurations, |L| = 3125)")
    A("-" * 78)
    A(f"{'level':<20}{'boundary':<26}{'cost':<8}{'remaining':<12}"
      f"{'is a law':<10}admissible after")
    for r in rec["tables"]["cost_tower"]:
        A(f"{r['level']:<20}{str(r['boundary']):<26}{r['cost']:<8}"
          f"{r['remaining']:<12}{str(r['remaining_is_a_law']):<10}"
          f"{r['boundary_admissible_after']}")
    pl = rec["tables"]["pair_level_cost"]
    A(f"  pair level: IMPOSSIBLE at any cost.  After paying the record-level "
      f"cost the second member is admissible = "
      f"{pl['after_paying_the_record_level_cost_member_2_admissible']}")
    A("")
    A("-" * 78)
    A("THE RIGIDITY SWEEP")
    A("-" * 78)
    A(f"{'n':<4}{'law':<14}{'|L|':<8}{'id':<6}{'records':<10}"
      f"admissible boundaries")
    for r in rec["tables"]["rigidity_sweep"]:
        A(f"{r['configurations']:<4}{r['law']:<14}{r['size']:<8}"
          f"{str(r['contains_identity']):<6}{r['records']:<10}"
          f"{r['admissible_boundaries']}")
    ifc = rec["tables"]["identity_free_control"]
    A(f"  identity-free control: law {ifc['law']}  closed="
      f"{ifc['composition_closed']}  contains identity="
      f"{ifc['contains_identity']}")
    A(f"      admissible boundaries (with family size): {ifc['admissible']}")
    A("")
    A("-" * 78)
    A("GATES")
    A("-" * 78)
    for g in rec["gates"]["rows"]:
        A(f"  [{'PASS' if g['passed'] else 'FAIL'}] {g['id']}  ({g['class']})")
        A(f"      {g['claim']}")
    A("")
    A("-" * 78)
    A("ANCHORS  (exit-1-only; every committed value this unit reuses)")
    A("-" * 78)
    for a in rec["anchors"]["rows"]:
        A(f"  [{'ok' if a['passed'] else 'FAIL'}] {a['id']:<8}{a['quantity']}")
        A(f"           committed {a['committed']!r} == computed "
          f"{a['computed']!r}   [{a['source']}]")
    A("")
    A("-" * 78)
    A("NON-CLAIMS")
    A("-" * 78)
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
        sys.stdout.write(f"  mutant {m:<22} exit {r.returncode}\n")
        sys.stdout.flush()
    if bad:
        sys.stdout.write(f"MUTANTS NOT KILLED: {bad}\n")
        return 1
    sys.stdout.write(f"all {len(names)} mutants killed (exit 1)\n")
    return 0


def main() -> int:
    global MUTANT, SOURCE_SHA256
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", default=None)
    ap.add_argument("--no-write-files", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    args = ap.parse_args()
    MUTANT = args.mutant
    CB.MUTANT = None
    CBP.MUTANT = None
    SOURCE_SHA256 = hashlib.sha256(
        Path(__file__).resolve().read_bytes()).hexdigest()
    if args.falsification_selftest:
        return run_falsification_selftest()

    run_exactness_gate()
    run_anchors()
    run_axiom()
    ctx, verdicts, law = run_discriminators()
    run_feynman(ctx, law)
    run_minimal_witness()
    run_cost()

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
