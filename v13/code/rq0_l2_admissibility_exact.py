#!/usr/bin/env python3
"""RQ0-L2 Cycle B" -- generative patch admissibility: the Atlas Axiom.

Executes the frozen pin `v13/note-rq0-l2-generative-admissibility-pin.md`
(commit 9576aee).

The candidate axiom.  A PATCH is a QUADRUPLE (boundary, declared task
family, declared preparation, admitted law) on a committed finite carrier
-- the preparation is a component because clause (ii-b) reads it and two
patches agreeing on the other three receive opposite verdicts (W1 vs W3).
A patch is ADMISSIBLE iff

  (i)  TWO-SIDED MINIMALITY, THE ker-PAIRING
       (i-a)  the boundary is the #103-minimal sufficient boundary OF its
              own declared family  --  A(B) = ker(F), the COARSEST retract
              through which every declared task factors, which merges
              nothing the family separates;
       (i-b)  the family is the boundary's Cycle B closure  --
              F = Pres_L(A(B)), decided by the terminal availability
              criterion (Cycle B Def 2.3 / Lemma 3.2);
       (i-a) is NOT Cycle B's Core: Core is monotone in the family and is
       Pres's own adjoint, ker is antitone and is the adjoint of a
       DIFFERENT connection.  Cycle B Thm 3.8 records the conflation as
       the one to avoid; L2-22 measures what the substitution buys.

  (ii) GENERATIVITY
       (ii-a) WRITTEN: the declared family is non-empty and every declared
              task writes exactly the boundary's record, comp(F) = A(B)
              (Cycle B Cor 3.3's co-merge procedure: the realized legs);
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
from itertools import combinations, permutations, product
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


def closure_of_maps(gens, n: int):
    """The composition closure of a set of deterministic sector maps, BUILT
    by saturation rather than characterized.  Returns sorted tuples."""
    S = set(gens)
    frontier = list(S)
    while frontier:
        nxt = []
        for f in list(S):
            for g in frontier:
                for h in (tuple(f[x] for x in g), tuple(g[x] for x in f)):
                    if h not in S:
                        S.add(h)
                        nxt.append(h)
        frontier = nxt
    return sorted(S)


_FUNNEL_CL: dict = {}


def law_funnel_closure(n: int):
    """FUNNEL's composition closure.  FUNNEL itself is composition-closed at
    n = 2 only (measured, L2-21), so it is a declared TASK FAMILY and not a
    law in the sense of Definition 2.1 at n >= 3; this is the law it
    generates, and the rigidity sweep is re-run on it."""
    if n not in _FUNNEL_CL:
        gens = [tuple(next(iter(s)) for s in F) for F in law_funnel(n)]
        _FUNNEL_CL[n] = [sup_of_map(f) for f in closure_of_maps(gens, n)]
    return _FUNNEL_CL[n]


def block_min_idempotent(part, n: int):
    """The BLOCK-MINIMUM IDEMPOTENT of a partition: send every configuration
    to the least member of its block.  Composition-closed on its own,
    writes exactly `part`, and its kernel is exactly `part` -- so {this} is
    a law in which `part` is admissible.  This is the addition that makes
    the REV counterexample to the exact-cost claim run."""
    if MUTANT == "forgery-lax":
        return sup_of_map(tuple(range(n)))
    where = {x: min(b) for b in part for x in b}
    return sup_of_map(tuple(where[x] for x in range(n)))


def has_identity(law, n: int) -> bool:
    return any(key(F) == key(sup_of_map(tuple(range(n)))) for F in law)


def has_reversible(law, n: int) -> bool:
    """A member is reversible when its supports are singletons forming a
    permutation of the carrier."""
    for F in law:
        if all(len(s) == 1 for s in F) and \
                len(set(next(iter(s)) for s in F)) == n:
            return True
    return False


_T3_LAWS: list = []


def laws_of_T3():
    """THE CENSUS POPULATION: every composition-closed law on three
    configurations generated by at most three deterministic sector maps.
    Built by saturation and deduplicated; the order is deterministic."""
    if not _T3_LAWS:
        seen = set()
        for r in (1, 2, 3):
            for gens in combinations(list(product(range(3), repeat=3)), r):
                seen.add(frozenset(closure_of_maps(gens, 3)))
        _T3_LAWS.extend(sorted(seen, key=lambda L: (len(L), sorted(L))))
    if MUTANT == "census-lax":
        return [L for L in _T3_LAWS if (0, 1, 2) in L]
    return _T3_LAWS


_T4_LAWS: list = []


def laws_of_T4_sample():
    """A DECLARED, DETERMINISTIC sample at four configurations: every law
    generated by one map of T_4, together with every law generated by a
    pair drawn from the fixed stride sample T_4[::7].  Named as a sample,
    never as an exhaustive census."""
    if not _T4_LAWS:
        T4 = list(product(range(4), repeat=4))
        seen = set(frozenset(closure_of_maps((f,), 4)) for f in T4)
        for gens in combinations(T4[::7], 2):
            seen.add(frozenset(closure_of_maps(gens, 4)))
        _T4_LAWS.extend(sorted(seen, key=lambda L: (len(L), sorted(L))))
    return _T4_LAWS


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


_CENSUS: dict = {}


def census_T3() -> dict:
    """ONE pass over the census population, feeding five gates: the rigidity
    DICHOTOMY (both directions), the comparable-pairs strengthening, the
    entailment theorem's corroboration population, the equality criterion
    for the forging cost, and covariance where it can actually bite.

    Every count here is over the same declared population and the same
    protocol as Section 6: the declared family is the boundary's closure and
    the declared preparation is the whole carrier."""
    if _CENSUS and _CENSUS.get("mutant") == MUTANT:
        return _CENSUS
    n, D = 3, CB.discrete(3)
    parts = CB.parts_of(3)
    c = {"mutant": MUTANT, "laws": 0, "identity_containing": 0,
         "reversible_containing": 0, "reversible_but_no_identity": 0,
         "admitting_a_proper_boundary": 0,
         "identity_containing_with_a_proper_boundary": 0,
         "identity_free_with_no_proper_boundary": 0,
         "discrete_admissible_iff_identity": 0,
         "admitting_both_a_coarse_and_the_discrete_boundary": 0,
         "admitting_the_coarse_boundary_only": 0,
         "admitting_the_discrete_boundary_only": 0,
         "laws_with_more_than_one_admissible_boundary": 0,
         "admissible_pairs": 0, "comparable_admissible_pairs": 0,
         "condition_i_instances": 0, "condition_i_at_proper_boundaries": 0,
         "condition_i_with_ii_a_failing": 0,
         "coarsest_retract_checked": 0, "coarsest_retract_mismatches": 0,
         "cost_pairs": 0, "complement_does_not_admit": 0,
         "complement_non_empty_and_does_not_admit": 0,
         "covariance_tests": 0, "covariance_violations": 0}
    coarse = ((0, 1), (2,))
    for Lf in laws_of_T3():
        law = [sup_of_map(f) for f in sorted(Lf)]
        c["laws"] += 1
        hid, hrev = has_identity(law, n), has_reversible(law, n)
        c["identity_containing"] += hid
        c["reversible_containing"] += hrev
        c["reversible_but_no_identity"] += (hrev and not hid)
        adm, verd = [], {}
        for q in parts:
            fam = pres_of(law, q)
            v = adjudicate(q, fam, law, frozenset(range(n)), n)
            verd[q] = v
            if v["i"]:
                c["condition_i_instances"] += 1
                c["condition_i_at_proper_boundaries"] += (q != D)
                c["condition_i_with_ii_a_failing"] += (not v["ii_a"])
            if v["admissible"]:
                adm.append(q)
            # (i-a)'s object IS the coarsest retract every declared task
            # factors through -- measured, not asserted (Appendix A.4).
            cands = [r for r in parts
                     if all(all(F[x] == F[y] for b in r for x in b for y in b)
                            for F in fam)]
            if cands:
                c["coarsest_retract_checked"] += 1
                if min(cands, key=lambda r: (len(r), r)) != v["ker"]:
                    c["coarsest_retract_mismatches"] += 1
            if q != D:
                c["cost_pairs"] += 1
                O = obstruction_set(law, q)
                Ok = set(key(F) for F in O)
                Lt = [F for F in law if key(F) not in Ok]
                if not adjudicate(q, pres_of(Lt, q), Lt,
                                  frozenset(range(n)), n)["admissible"]:
                    c["complement_does_not_admit"] += 1
                    c["complement_non_empty_and_does_not_admit"] += bool(Lt)
        proper = [q for q in adm if q != D]
        c["admitting_a_proper_boundary"] += bool(proper)
        c["identity_containing_with_a_proper_boundary"] += (hid and bool(proper))
        c["identity_free_with_no_proper_boundary"] += ((not hid) and not proper)
        c["discrete_admissible_iff_identity"] += ((D in adm) == hid)
        c["admitting_both_a_coarse_and_the_discrete_boundary"] += (
            coarse in adm and D in adm)
        c["admitting_the_coarse_boundary_only"] += (coarse in adm and D not in adm)
        c["admitting_the_discrete_boundary_only"] += (D in adm and coarse not in adm)
        c["laws_with_more_than_one_admissible_boundary"] += (len(adm) > 1)
        for x, y in combinations(adm, 2):
            c["admissible_pairs"] += 1
            if CB.refines(x, y) or CB.refines(y, x):
                c["comparable_admissible_pairs"] += 1
        for s in permutations(range(n)):
            inv = [s.index(i) for i in range(n)]
            if frozenset(tuple(s[f[inv[i]]] for i in range(n))
                         for f in Lf) != Lf:
                continue
            for q in parts:
                c["covariance_tests"] += 1
                qs = CB.relabel_part(q, s)
                if verd[q]["admissible"] != verd[qs]["admissible"]:
                    c["covariance_violations"] += 1
    _CENSUS.clear()
    _CENSUS.update(c)
    return c


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
                if x < y and not any(
                        any(x in blk and y in blk for blk in written_of(F))
                        for F in fam):
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
    identity, plus the counter-law at five configurations, plus FUNNEL's
    composition closure wherever FUNNEL itself is not a law (n >= 3)."""
    out = [("DET", law_det(n)), ("FUNNEL", law_funnel(n)), ("REV", law_rev(n))]
    if n >= 3:
        out.append(("FUNNEL-CLOSURE", law_funnel_closure(n)))
    if n <= 4:
        out.append(("ALL", law_all(n)))
    if n == 5:
        out.append(("COUNTER-LAW", law_counter()[0]))
    return out


def closure_status(name: str, law, n: int) -> dict:
    """Composition-closure per law, honestly labelled: MEASURED where the
    check is affordable, PROVED where the family is closed by construction
    (DET is every map, REV is a group, ALL is every left-total relation, and
    the funnel closure is built by saturation)."""
    if name in ("DET", "REV", "ALL", "FUNNEL-CLOSURE"):
        return {"composition_closed": True, "how": "by construction"}
    return {"composition_closed": is_composition_closed(law),
            "how": "measured"}


def run_axiom():
    prog("axiom: rigidity, entailment, the independence of the clauses")

    rows = []
    rigid_ok = True
    entail_ok = True
    entail_instances = 0
    for n in (2, 3, 4, 5):
        for name, law in committed_laws(n):
            has_id = has_identity(law, n)
            adm = []
            for p in CB.parts_of(n):
                fam = pres_of(law, p)
                v = adjudicate(p, fam, law, PREP_FULL & frozenset(range(n))
                               or frozenset(range(n)), n)
                if v["i"]:
                    adm.append(p)
                    entail_instances += 1
                    if not v["ii_a"]:
                        entail_ok = False
            row = {"configurations": n, "law": name, "size": len(law),
                   "contains_identity": has_id,
                   "contains_a_reversible_operation": has_reversible(law, n),
                   "records": CB.bell(n),
                   "admissible_boundaries": [list(map(list, p)) for p in adm]}
            row.update(closure_status(name, law, n))
            rows.append(row)
            if has_id and adm != [CB.discrete(n)]:
                rigid_ok = False
    TABLES["rigidity_sweep"] = rows
    committed_rows = [r for r in rows if r["law"] != "FUNNEL-CLOSURE"]
    closure_rows = [r for r in rows if r["law"] == "FUNNEL-CLOSURE"]

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
         "DET, FUNNEL, REV, ALL (n<=4) and the counter-law -- sixteen sweeps "
         "-- and over three further sweeps on FUNNEL's composition closure, "
         "the law FUNNEL generates where FUNNEL itself is not one (L2-21).  "
         "Nineteen sweeps, one admissible boundary each, no exceptions",
         rigid_ok and len(committed_rows) == 16 and len(closure_rows) == 3,
         {"sweep": rows, "committed_sweeps": len(committed_rows),
          "funnel_closure_sweeps": len(closure_rows)})

    # -- FUNNEL is a declared TASK FAMILY, not a law at n >= 3.  Measured.
    funnel_closed = {n: is_composition_closed(law_funnel(n))
                     for n in (2, 3, 4, 5)}
    funnel_witness = None
    f01, f12 = CB.elementary_merge(3, 0, 1), CB.elementary_merge(3, 1, 2)
    funnel_witness = {"f_0to1": key(f01), "f_1to2": key(f12),
                      "composite": key(compose(f01, f12)),
                      "composite_in_FUNNEL":
                          key(compose(f01, f12)) in
                          set(key(F) for F in law_funnel(3))}
    TABLES["funnel_closure"] = {
        "FUNNEL_is_composition_closed": {str(n): v
                                         for n, v in funnel_closed.items()},
        "witness_at_three_configurations": funnel_witness,
        "closure_sizes": {str(n): len(law_funnel_closure(n))
                          for n in (3, 4, 5)},
        "closure_is_the_identity_plus_the_non_injective_maps": {
            str(n): all(len(set(tuple(next(iter(s)) for s in F))) < n
                        or key(F) == key(sup_of_map(tuple(range(n))))
                        for F in law_funnel_closure(n)) for n in (3, 4, 5)},
        "re_run_sweeps": closure_rows}
    gate("L2-21", "scope",
         "FUNNEL IS NOT A LAW AT THREE CONFIGURATIONS OR MORE, and the three "
         "sweeps that used it are re-run on the law it generates.  "
         "Definition 2.1 requires an admitted law to be composition-closed.  "
         "Measured: FUNNEL is composition-closed at n = 2 ONLY; at n = 3 the "
         "composite f_{0->1} o f_{1->2} = (1,2,2) moves two configurations "
         "and is neither the identity nor an elementary merge, so it lies "
         "outside FUNNEL; the same failure occurs at 4 and 5.  FUNNEL is "
         "therefore a declared TASK FAMILY, and its composition closure -- "
         "the identity together with every non-injective map, of sizes 22, "
         "233 and 3006 -- is the law it generates.  The three affected "
         "rigidity sweeps are re-run on that closure and NOTHING MOVES: the "
         "admissible set is the singleton {discrete} in each, as rigidity "
         "requires of any law containing the identity",
         funnel_closed[2] and not any(funnel_closed[n] for n in (3, 4, 5))
         and not funnel_witness["composite_in_FUNNEL"]
         and all(r["admissible_boundaries"] ==
                 [list(map(list, CB.discrete(r["configurations"])))]
                 for r in closure_rows)
         and all(TABLES["funnel_closure"]
                 ["closure_is_the_identity_plus_the_non_injective_maps"][str(n)]
                 for n in (3, 4, 5)),
         TABLES["funnel_closure"])

    cen = census_T3()
    gate("L2-04", "theorem",
         "THE ENTAILMENT THEOREM: at any NON-EMPTY admitted law, condition "
         "(ii-a) is ENTAILED by condition (i) -- every patch passing both "
         "halves of (i) writes exactly its boundary's record.  Proof in the "
         "paper: (i) forces the declared family to be non-empty unless the "
         "law is; (i-a) then makes every declared task constant on blocks, "
         "so comp(F) is coarser than A(B); (i-b) makes comp(F) refine A(B); "
         "the two force equality.  The empty law at the one-atom boundary is "
         "the degenerate case the non-emptiness requirement in (ii-a) "
         "excludes, and the decision procedure and Definition 2.2 agree on "
         "it because the clause says so.  Corroborated "
         "where it can actually bite: rigidity leaves the committed sweep "
         "only 19 condition-(i) instances, one per law and every one of them "
         "the discrete boundary, so that sweep is nearly vacuous as evidence "
         "for this theorem.  The population reported here is the census of "
         "every composition-closed law on three configurations generated by "
         "at most three maps -- 687 laws, 1004 condition-(i) instances, 745 "
         "of them at PROPER boundaries -- with ZERO (ii-a) failures.  So "
         "generativity's WRITTEN clause is not an independent constraint, "
         "and the axiom's independent content beyond (i) is the OCCUPANCY "
         "clause alone",
         entail_ok and cen["condition_i_with_ii_a_failing"] == 0
         and entail_instances == len(rows)
         and cen["condition_i_instances"] == 1004
         and cen["condition_i_at_proper_boundaries"] == 745,
         {"counterexamples_in_the_committed_sweep": 0,
          "condition_i_instances_in_the_committed_sweep": entail_instances,
          "census_laws": cen["laws"],
          "census_condition_i_instances": cen["condition_i_instances"],
          "census_at_proper_boundaries": cen["condition_i_at_proper_boundaries"],
          "census_ii_a_failures": cen["condition_i_with_ii_a_failing"]})

    gate("L2-23", "theorem",
         "#103-MINIMALITY IS WHAT (i-a) COMPUTES, proved and now gated.  The "
         "quotient by ker is the COARSEST partition on whose blocks every "
         "declared task is constant -- one line: a partition r is a retract "
         "through which every task factors exactly when every task is "
         "constant on r's blocks, i.e. exactly when r refines ker, and the "
         "coarsest such r is ker itself.  The identification was asserted "
         "and never gated; it is measured here by brute force over every "
         "boundary of every law in the census, recomputing the minimum-atom "
         "retract independently of ker and comparing",
         cen["coarsest_retract_mismatches"] == 0,
         {"families_checked": cen["coarsest_retract_checked"],
          "mismatches": cen["coarsest_retract_mismatches"]})

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
    instances = nonvacuous = 0
    for n in (3, 4):
        law = law_det(n)
        for s in permutations(range(n)):
            inv = {s[i]: i for i in range(n)}
            for p in CB.parts_of(n):
                ps = CB.relabel_part(p, s)
                v1 = adjudicate(p, pres_of(law, p), law, frozenset(range(n)), n)
                v2 = adjudicate(ps, pres_of(law, ps), law,
                                frozenset(range(n)), n)
                instances += 1
                nonvacuous += v1["admissible"]
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
    TABLES["covariance"] = {
        "violations_DET_n3_n4": viol,
        "instances_DET_n3_n4": instances,
        "instances_with_a_true_antecedent": nonvacuous,
        "census_tests_against_each_law's_own_symmetry_group":
            cen["covariance_tests"],
        "census_violations": cen["covariance_violations"],
        "relabellings_preserving_the_counter_law": inv_perms}
    gate("L2-06", "covariance",
         "ADMISSIBILITY IS COVARIANT under the admitted relabellings of the "
         "carrier, measured rather than assumed: over every relabelling and "
         "every record at three and four configurations under DET there is "
         "no case where a boundary is admissible and its relabelled copy is "
         "not.  THE VACUITY IS DISCLOSED WITH IT: of those 390 instances the "
         "antecedent holds in exactly 30 -- rigidity leaves one admissible "
         "boundary per relabelling and it is the discrete one carried to "
         "itself -- so the DET sweep tests one boundary.  Covariance is "
         "therefore re-run where it can bite, over the census of 687 laws at "
         "three configurations against EACH LAW'S OWN symmetry group, "
         "including the identity-free laws whose admissible boundaries are "
         "proper: 4620 tests, zero violations.  The law-relativity is "
         "disclosed too: the counter-law is preserved by exactly ONE of the "
         "120 relabellings, so under that law covariance has no content -- "
         "admission, as the predecessor cycle already found, must be "
         "certified per law",
         viol == 0 and inv_perms == 1 and instances == 390 and nonvacuous == 30
         and cen["covariance_violations"] == 0
         and cen["covariance_tests"] == 4620,
         {"violations": viol, "counter_law_symmetries": inv_perms,
          "instances": instances, "non_vacuous": nonvacuous,
          "census_tests": cen["covariance_tests"],
          "census_violations": cen["covariance_violations"]})

    # -- THE MECHANISM: (i-a) is the ker-pairing, NOT Cycle B's Core.
    a3, b3 = sup_of_map((0, 0, 2)), sup_of_map((0, 2, 2))
    monotone = {"family": [key(a3)], "superfamily": [key(a3), key(b3)],
                "Core_of_family": CB.core_of_family([a3], 3),
                "Core_of_superfamily": CB.core_of_family([a3, b3], 3),
                "ker_of_family": ker_of_family([a3], 3),
                "ker_of_superfamily": ker_of_family([a3, b3], 3)}
    core_rows = []
    for n in (2, 3, 4, 5):
        law = law_det(n)
        core_rows.append({
            "configurations": n, "law": "DET", "records": CB.bell(n),
            "records_fixed_by_Core_after_Pres": len(CB.fix_set_of_family(law, n)),
            "records_fixed_by_ker_after_Pres":
                sum(1 for p in CB.parts_of(n)
                    if ker_of_family(pres_of(law, p), n) == p)})
    lrc, _ = law_counter()
    core_rows.append({
        "configurations": 5, "law": "COUNTER-LAW", "records": 52,
        "records_fixed_by_Core_after_Pres": len(CB.fix_set_of_family(lrc, 5)),
        "records_fixed_by_ker_after_Pres":
            sum(1 for p in CB.parts_of(5)
                if ker_of_family(pres_of(lrc, p), 5) == p)})
    TABLES["mechanism"] = {"opposite_monotonicity": monotone,
                           "fixed_records": core_rows}
    gate("L2-22", "mechanism",
         "CONDITION (i) IS THE ker-PAIRING, NOT CYCLE B'S TWO-SIDED FIXED "
         "POINT, and this is where the axiom's selectivity comes from.  "
         "(i-b) uses Pres, Cycle B's right adjoint; (i-a) uses ker, which is "
         "NOT Core.  They move in OPPOSITE directions with the family: "
         "enlarging {a} to {a,b} COARSENS Core from {01|2} to the one-atom "
         "boundary and REFINES ker from {01|2} to the discrete boundary -- "
         "exhibited here.  Cycle B Theorem 3.8 records exactly this "
         "conflation as the one to avoid.  Measured consequence: the genuine "
         "two-sided Cycle B condition Core(Pres(pi)) = pi fixes EVERY record "
         "-- 2 of 2, 5 of 5, 15 of 15, 52 of 52 under DET and 52 of 52 under "
         "the counter-law -- while the mixed ker(Pres(pi)) = pi fixes "
         "EXACTLY ONE at every count.  The selectivity is neither inherited "
         "from Cycle B nor a discovery about competing minimalities: it is "
         "produced by the substitution, and RIGIDITY IS THE SIGNATURE OF THE "
         "MISMATCHED PAIRING",
         all(r["records_fixed_by_Core_after_Pres"] == r["records"]
             and r["records_fixed_by_ker_after_Pres"] == 1 for r in core_rows)
         and monotone["Core_of_family"] == ((0, 1), (2,))
         and monotone["Core_of_superfamily"] == CB.indiscrete(3)
         and monotone["ker_of_family"] == ((0, 1), (2,))
         and monotone["ker_of_superfamily"] == CB.discrete(3),
         TABLES["mechanism"])

    # -- THE DICHOTOMY: proved, and its census in both directions.
    n4rows = {"laws": 0, "discrete_admissible_iff_identity": 0,
              "identity_containing_with_a_proper_boundary": 0}
    for Lf in laws_of_T4_sample():
        law = [sup_of_map(f) for f in sorted(Lf)]
        n4rows["laws"] += 1
        hid = has_identity(law, 4)
        dadm = adjudicate(CB.discrete(4), pres_of(law, CB.discrete(4)), law,
                          frozenset(range(4)), 4)["admissible"]
        n4rows["discrete_admissible_iff_identity"] += (dadm == hid)
        proper = any(adjudicate(p, pres_of(law, p), law, frozenset(range(4)),
                                4)["admissible"]
                     for p in CB.parts_of(4) if p != CB.discrete(4))
        n4rows["identity_containing_with_a_proper_boundary"] += (hid and proper)
    TABLES["dichotomy"] = {"census_at_three_configurations": cen,
                           "sample_at_four_configurations": n4rows}
    gate("L2-24", "theorem",
         "THE RIGIDITY DICHOTOMY, BOTH DIRECTIONS.  Theorem 3.1 gives one "
         "half; the converse is two lines and is proved in the paper: n "
         "pairwise-disjoint non-empty supports inside an n-configuration "
         "carrier force every support to be a singleton, so Pres_L(discrete) "
         "is exactly the reversible members of L, and any of them separates "
         "every pair; hence the carrier's own algebra is admissible IFF the "
         "law contains a reversible operation IFF (finite order) it contains "
         "the identity.  THE TRIGGER IS REVERSIBILITY, NOT IDLING.  Census "
         "over the 687 composition-closed laws on three configurations: the "
         "biconditional holds 687 of 687; laws containing a reversible "
         "operation 259, laws containing the identity 259, reversible-but-no-"
         "identity 0; laws admitting a proper boundary 428; "
         "identity-containing laws admitting a proper boundary 0; "
         "identity-free laws admitting NO proper boundary 0.  So every law "
         "has either exactly one chart -- the carrier's -- or no carrier "
         "chart at all and possibly several proper ones; there is nothing in "
         "between.  Re-measured on a declared sample of 865 laws at four "
         "configurations: zero failures in both directions",
         cen["discrete_admissible_iff_identity"] == cen["laws"]
         and cen["reversible_but_no_identity"] == 0
         and cen["reversible_containing"] == cen["identity_containing"]
         and cen["identity_containing_with_a_proper_boundary"] == 0
         and cen["identity_free_with_no_proper_boundary"] == 0
         and n4rows["discrete_admissible_iff_identity"] == n4rows["laws"]
         and n4rows["identity_containing_with_a_proper_boundary"] == 0,
         TABLES["dichotomy"])


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
         "killing conditions are measured, not assumed: for the boundary's "
         "own closure -- the only declaration that could ever satisfy (i-b), "
         "and the one this section substitutes -- (i-a) AND (ii-a) both "
         "fail, on the SAME witness, a declared task that separates the two "
         "configurations the boundary asserts are one atom.  The boundary "
         "claims an identification its own realized legs never write.  Under "
         "any OTHER declared family the patch fails (i-b) instead: the "
         "verdict is declaration-independent, the kill-list is not, and "
         "L2-26 measures it.  The verdict is also law-relative -- member 1 "
         "is inadmissible at every law CONTAINING THE IDENTITY, and L2-27 "
         "exhibits an identity-free law where it is admissible.  MEMBER 2 is "
         "admissible, and correctly so: as a boundary it IS the legitimate "
         "address algebra, and the collusion lives entirely in member 1's "
         "forged patch",
         pair_ok and (not m1["admissible"]) and m2["admissible"],
         {"member_1": m1, "member_2": m2})
    cen = census_T3()
    gate("L2-08", "discriminator",
         "THE PAIR IS JOINTLY UNFORGEABLE AT A SHARED LAW.  Stronger than "
         "rejection: no SINGLE admitted law makes both members admissible at "
         "once.  Pres(discrete) is contained in Pres(forged) -- measured -- "
         "so any law under which the forged boundary's preserving family "
         "fails to separate configurations 0 and 1 is a law under which the "
         "second member's family fails to separate them either, and the "
         "second member stops being admissible.  The theorem is general in "
         "the pair: NO law admits two strictly COMPARABLE boundaries, of "
         "which the colluding pair is the instance.  The hypothesis is "
         "load-bearing and is stated: both contexts must declare the SAME "
         "law.  Under the pin's own one-law-family-per-context reading the "
         "adversary may declare a law per context, and then the escape of "
         "L2-27 exists",
         contained and all(not r["both"] for r in joint),
         {"laws_tested": joint,
          "structural": "Pres(discrete) subset Pres(forged)",
          "hypothesis": "both contexts declare the same admitted law"})

    # -- the comparable-pairs strengthening, censused
    n4pairs = n4joint = 0
    for nm, lw in (("DET", law_det(4)), ("REV", law_rev(4)),
                   ("FUNNEL-CLOSURE", law_funnel_closure(4))):
        adms = [p for p in CB.parts_of(4)
                if adjudicate(p, pres_of(lw, p), lw, frozenset(range(4)),
                              4)["admissible"]]
        for x, y in combinations(CB.parts_of(4), 2):
            if CB.refines(x, y) or CB.refines(y, x):
                n4pairs += 1
                n4joint += (x in adms and y in adms)
    TABLES["comparable_pairs"] = {
        "census_at_three_configurations": {
            "laws": cen["laws"],
            "laws_with_more_than_one_admissible_boundary":
                cen["laws_with_more_than_one_admissible_boundary"],
            "unordered_admissible_pairs": cen["admissible_pairs"],
            "comparable_among_them": cen["comparable_admissible_pairs"],
            "laws_admitting_both_{01|2}_and_the_discrete_boundary":
                cen["admitting_both_a_coarse_and_the_discrete_boundary"],
            "the_coarse_boundary_only":
                cen["admitting_the_coarse_boundary_only"],
            "the_discrete_boundary_only":
                cen["admitting_the_discrete_boundary_only"]},
        "at_four_configurations": {"laws": ["DET", "REV", "FUNNEL-CLOSURE"],
                                   "comparable_pairs": n4pairs,
                                   "jointly_admissible": n4joint}}
    gate("L2-25", "theorem",
         "NO LAW ADMITS TWO STRICTLY COMPARABLE BOUNDARIES -- the general "
         "form of joint unforgeability, which costs nothing and is strictly "
         "stronger.  The proof uses nothing about the arena: if pi strictly "
         "refines pi' then Pres_L(pi) is contained in Pres_L(pi') for every "
         "L, and the coarser member's admissibility forces the finer "
         "member's kernel to merge a pair the finer boundary separates.  "
         "Measured over the census: 277 of 687 laws have more than one "
         "admissible boundary, 357 unordered admissible pairs occur, and "
         "ZERO of them are comparable; 0 of 687 laws admit both {01|2} and "
         "the discrete boundary (246 the coarse one only, 259 the fine one "
         "only).  At four configurations, over DET, REV and the funnel "
         "closure: 135 comparable pairs, zero jointly admissible.  "
         "Incomparable boundaries genuinely differ -- the identity-free "
         "control's two proper charts coexist -- so comparability is the "
         "sharp hypothesis",
         cen["comparable_admissible_pairs"] == 0 and n4joint == 0
         and cen["admissible_pairs"] == 357 and n4pairs == 135
         and cen["admitting_both_a_coarse_and_the_discrete_boundary"] == 0,
         TABLES["comparable_pairs"])

    # -- THE MIXED-LAW ESCAPE: one law per context, the pin's own scope.
    esc_law = [sup_of_map((0, 0, 2, 3, 4))]
    p_forged = tuple(sorted(tuple(sorted(s))
                            for s in ctx["ALIGNED211"]["images"]))
    v_esc1 = adjudicate(p_forged, pres_of(esc_law, p_forged), esc_law,
                        PREP_FULL, CARRIER)
    v_esc2 = adjudicate(CB.discrete(CARRIER),
                        pres_of(law, CB.discrete(CARRIER)), law, PREP_FULL,
                        CARRIER)
    TABLES["mixed_law_escape"] = {
        "member_1": {"law": "{(0,0,2,3,4)}, composition-closed and "
                            "identity-free",
                     "law_is_composition_closed":
                         is_composition_closed(esc_law),
                     "law_contains_identity": has_identity(esc_law, CARRIER),
                     "declared_family_size": v_esc1["pres_size"],
                     "i_a": v_esc1["i_a"], "i_b": v_esc1["i_b"],
                     "ii_a": v_esc1["ii_a"], "ii_b": v_esc1["ii_b"],
                     "admissible": v_esc1["admissible"]},
        "member_2": {"law": "DET", "declared_family_size": v_esc2["pres_size"],
                     "admissible": v_esc2["admissible"]},
        "open_question": "the MIXED-LAW ARENA: what binds two patches that "
                         "declare different admitted laws.  Nothing in this "
                         "cycle measures it, and physically it is the "
                         "realistic case -- patches with different effective "
                         "laws"}
    gate("L2-27", "discriminator-negative",
         "THE MIXED-LAW ESCAPE EXISTS, and it is reported as a limitation of "
         "the unforgeability theorem rather than absorbed.  The scope line "
         "declares ONE LAW FAMILY PER CONTEXT.  An adversary who uses that "
         "freedom holds both members: member 1, the forged 2+1+1 boundary, "
         "is ADMISSIBLE under the composition-closed identity-free law "
         "{(0,0,2,3,4)} -- all four clauses passing, declared family of one "
         "task -- while member 2 is admissible under DET, exactly as Section "
         "6 reports.  The axiom rejects neither.  So 'no admitted law "
         "whatsoever' is false and 'no SINGLE admitted law' is what is "
         "proved; joint unforgeability is a statement about one law, not "
         "about one adversary.  Whether the predecessor's record-descent "
         "attack still runs at the escape law is NOT measured here.  THE "
         "MIXED-LAW ARENA IS THE NAMED OPEN QUESTION",
         v_esc1["admissible"] and v_esc2["admissible"]
         and is_composition_closed(esc_law)
         and not has_identity(esc_law, CARRIER),
         TABLES["mixed_law_escape"])

    # -- R3's declaration-relativity: Section 6 reads the ADVERSARY's family.
    decls = [
        ("the boundary's closure -- the canonical substitution",
         pres_of(law, p_forged)),
        ("the written-exact subfamily {F : comp(F) = pi_1}",
         [F for F in law if written_of(F) == p_forged]),
        ("the merging subfamily inside the closure {F in Pres : F(0) = F(1)}",
         [F for F in pres_of(law, p_forged) if F[0] == F[1]]),
        ("the merging subfamily of the whole law {F in L : F(0) = F(1)}",
         [F for F in law if F[0] == F[1]]),
        ("the single repreparation task (0,0,2,3,4)",
         [sup_of_map((0, 0, 2, 3, 4))]),
        ("the identity alone", [sup_of_map(tuple(range(CARRIER)))]),
    ]
    drows = []
    for nm, fam in decls:
        if MUTANT == "declaration-lax":
            fam = pres_of(law, p_forged)
        v = adjudicate(p_forged, fam, law, PREP_FULL, CARRIER)
        drows.append({"declared_family": nm, "size": len(fam),
                      "admissible": v["admissible"],
                      "killed_by": ", ".join(
                          c for c, ok in (("(i-a)", v["i_a"]),
                                          ("(i-b)", v["i_b"]),
                                          ("(ii-a)", v["ii_a"]),
                                          ("(ii-b)", v["ii_b"])) if not ok)})
    ib = iib = ia_iff = iia_iff = 0
    for p in CB.parts_of(CARRIER):
        v = adjudicate(p, pres_of(law, p), law, PREP_FULL, CARRIER)
        ib += v["i_b"]
        iib += v["ii_b"]
        ia_iff += (v["i_a"] == (p == CB.discrete(CARRIER)))
        iia_iff += (v["ii_a"] == (p == CB.discrete(CARRIER)))
    TABLES["declaration_relativity"] = {
        "boundary": [list(b) for b in p_forged],
        "declarations": drows,
        "over_all_52_records_under_DET": {
            "(i-b)_true_by_construction": ib,
            "(ii-b)_true_by_construction": iib,
            "(i-a)_equivalent_to_the_boundary_being_discrete": ia_iff,
            "(ii-a)_equivalent_to_the_boundary_being_discrete": iia_iff,
            "records": CB.bell(CARRIER)}}
    gate("L2-26", "discriminator",
         "THE KILL-LIST IS DECLARATION-RELATIVE, and Section 6's table is "
         "read against the adversary's ACTUAL declarations rather than the "
         "one the unit substitutes.  The VERDICT at the forged boundary is "
         "declaration-independent -- inadmissible under every declaration, "
         "as (i-b) and rigidity together require -- but the IDENTITY OF THE "
         "KILLING CONDITION is not.  Measured at pi_1 under DET: under the "
         "boundary's closure (240 tasks, the canonical substitution) the "
         "kill is (i-a)+(ii-a); under the written-exact declaration and "
         "under the merging declaration inside the closure -- the same 120 "
         "tasks, measured -- the kill is (i-b) ALONE; under the merging "
         "subfamily of the whole law (625 tasks) it is (i-b)+(ii-a); under "
         "the single repreparation task it is (i-b) alone; under the "
         "identity alone all four clauses fail.  Two consequences are "
         "disclosed with it: in Section 6 the family is SET to the closure "
         "and the preparation to the whole carrier, so (i-b) and (ii-b) hold "
         "by construction -- 52 of 52 records each -- and with (i-b) imposed "
         "and the identity present, (i-a) and (ii-a) each reduce to the "
         "single bit 'is the presented boundary the carrier's own algebra', "
         "52 of 52.  The nine-row table has ONE measured degree of freedom "
         "per row",
         all(not r["admissible"] for r in drows)
         and drows[0]["killed_by"] == "(i-a), (ii-a)"
         and drows[1]["killed_by"] == "(i-b)"
         and drows[2]["killed_by"] == "(i-b)"
         and drows[1]["size"] == drows[2]["size"] == 120
         and ib == iib == ia_iff == iia_iff == CB.bell(CARRIER),
         TABLES["declaration_relativity"])

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


def statistics_of_patch(patch):
    """The two admitted statistics OF A PATCH QUADRUPLE (boundary, family,
    preparation, law).  The preparation component is discarded here, and
    THAT IS THE FINDING: no statistic in this section reads it, so none can
    see a failure of the occupancy clause."""
    part, fam, _prep, _law = patch
    return sigma_statistic(part, fam, RHO), delta_statistic(part, fam, RHO)


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

    # the comparator's kill-list is COMPUTED, never asserted (it is two
    # clauses, not one: the total eraser writes the one-atom record).
    bad_kills = [c for c, ok in (("(i-a)", v_bad["i_a"]), ("(i-b)", v_bad["i_b"]),
                                 ("(ii-a)", v_bad["ii_a"]),
                                 ("(ii-b)", v_bad["ii_b"])) if not ok]
    bad_written = [key(F) for F in fam_bad if written_of(F) != disc]
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
                "declared_family": "the closure plus the TOTAL ERASER to one "
                                   "configuration, (0,0,0,0,0)",
                "admissible": v_bad["admissible"],
                "fails": ", ".join(bad_kills),
                "fails_computed_not_asserted": True,
                "tasks_failing_the_written_clause": bad_written,
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
         "THE FEYNMAN GATE IS POSITIVE VIA CONDITION (i): admissibility "
         "changes a number, and the claim names which condition changes it.  "
         "At ONE fixed boundary -- the carrier's configuration algebra -- an "
         "admissible patch and an inadmissible patch differ in an admitted "
         "tester statistic.  The statistic is Cycle B Definition 2.3's own "
         "two-time record-recovery probability under the committed "
         "branch-memory state: it is exactly 1 for the admissible patch and "
         "exactly 3/4 for the inadmissible one, whose declared family is the "
         "closure plus the TOTAL ERASER to one configuration.  Both values "
         "are rational and computed, and the two patches share their "
         "boundary, their law, their state and their preparation; only the "
         "declared family differs.  The comparator's kill-list is COMPUTED "
         "here, not asserted, and it is TWO clauses: (i-b), because the "
         "declared family is not the boundary's closure, AND (ii-a), because "
         "the total eraser writes the one-atom record rather than the "
         "declared discrete one.  The pre-registered EMPIRICALLY-IDLE "
         "outcome therefore does NOT occur",
         (s_adm == Fr(1)) and (s_bad == Fr(3, 4)) and v_adm["admissible"]
         and (not v_bad["admissible"]) and bad_kills == ["(i-b)", "(ii-a)"]
         and len(bad_written) == 1,
         {"sigma_admissible": str(s_adm), "sigma_inadmissible": str(s_bad),
          "comparator_kill_list": bad_kills})

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
         "because rigidity leaves no admissible comparator there -- and by "
         "L2-26 that holds for EVERY declaration at that boundary, not "
         "merely the canonical one.  Both limitations are stated, neither is "
         "absorbed, and L2-28 states the third",
         (s_forged == Fr(1)) and (d_adm == Fr(0)) and (d_forged == Fr(1, 16)),
         {"sigma_forged": str(s_forged), "delta_admissible": str(d_adm),
          "delta_forged": str(d_forged)})

    # -- THE THIRD HONEST HALF: what the two statistics CANNOT see.
    lrb, _ = law_counter()
    famC = pres_of(lrb, disc)
    prepA = PREP_FULL
    prepB = PREP_FULL if MUTANT == "blind-lax" else frozenset({0})
    patchA = (disc, famC, prepA, lrb)
    patchB = (disc, famC, prepB, lrb)
    vA = adjudicate(patchA[0], patchA[1], patchA[3], patchA[2], CARRIER)
    vB = adjudicate(patchB[0], patchB[1], patchB[3], patchB[2], CARRIER)
    (sA, dA), (sB, dB) = statistics_of_patch(patchA), statistics_of_patch(patchB)
    sig_args = sigma_statistic.__code__.co_varnames[
        :sigma_statistic.__code__.co_argcount]
    del_args = delta_statistic.__code__.co_varnames[
        :delta_statistic.__code__.co_argcount]
    prep_free = ("prep" not in sig_args) and ("prep" not in del_args)
    fam_id = [sup_of_map(tuple(range(CARRIER)))]
    v_id = adjudicate(disc, fam_id, law, PREP_FULL, CARRIER)
    s_id = sigma_statistic(disc, fam_id, RHO)
    sig_dist: dict = {}
    admk = set(key(F) for F in fam_adm)
    for F in law:
        if key(F) in admk:
            continue
        # sigma(closure + {F}) = min(sigma(closure), tot(F)) = tot(F), since
        # every closure task attains 1 -- so one task at a time suffices.
        s1 = str(sigma_statistic(disc, [F], RHO))
        sig_dist[s1] = sig_dist.get(s1, 0) + 1
    TABLES["feynman_blind_spots"] = {
        "occupancy_blindness": {
            "law": "the counter-law; declared family = Pres(discrete) = the "
                   "identity alone",
            "patch_A": {"preparation": sorted(prepA), "reach": vA["reach"],
                        "admissible": vA["admissible"], "sigma": str(sA),
                        "delta": str(dA)},
            "patch_B": {"preparation": sorted(prepB), "reach": vB["reach"],
                        "admissible": vB["admissible"], "sigma": str(sB),
                        "delta": str(dB)},
            "the_two_patches_differ_in_the_preparation_alone": True,
            "neither_statistic_takes_the_preparation_as_an_argument":
                {"sigma_arguments": list(sig_args),
                 "delta_arguments": list(del_args),
                 "preparation_free": prep_free}},
        "omission_blindness": {
            "patch": "the discrete boundary declaring the identity alone",
            "admissible": v_id["admissible"], "sigma": str(s_id),
            "note": "sigma equals the admissible patch's value at an "
                    "INADMISSIBLE patch, so sigma is not a function of "
                    "admissibility at a fixed boundary; it fires in the "
                    "ADDITION direction of (i-b) only"},
        "sigma_over_every_one_task_extension_of_the_closure": {
            "extensions": sum(sig_dist.values()), "distinct_values": sig_dist,
            "minimum": min(sig_dist, key=lambda s: Fr(s)),
            "attained_by": sig_dist[min(sig_dist, key=lambda s: Fr(s))],
            "note": "3/4 is the EXTREME of the comparator family, attained by "
                    "exactly the five constant maps, not a generic "
                    "inadmissible value"}}
    gate("L2-28", "feynman-honest",
         "THE GATE IS BLIND TO THE AXIOM'S INDEPENDENT CLAUSE.  Theorem 3.2 "
         "makes OCCUPANCY the only content the axiom has beyond condition "
         "(i), and neither admitted statistic can see it: sigma and delta "
         "are functions of the boundary, the declared family and the state, "
         "and the declared preparation is not an argument of either.  "
         "Exhibited at the committed carrier under the counter-law, where "
         "the closure of the discrete boundary is the identity alone: two "
         "patches differing in the declared preparation ALONE -- the whole "
         "carrier against {0} -- have opposite verdicts (the second leaves "
         "four atoms never occupied) and IDENTICAL statistics, sigma = 1 and "
         "delta = 0 for both.  Two further blind spots are reported with it: "
         "the inadmissible patch that declares the identity alone at the "
         "discrete boundary also has sigma = 1, so sigma is not a function "
         "of admissibility at a fixed boundary but fires in the ADDITION "
         "direction of (i-b) only; and over all 3005 one-task extensions of "
         "the closure sigma takes four values with minimum exactly 3/4, "
         "attained by exactly the five constant maps -- the positive's 3/4 "
         "is the extreme of that family, not a generic value.  AN "
         "OCCUPANCY-SENSITIVE STATISTIC IS LEFT OPEN",
         vA["admissible"] and (not vB["admissible"]) and sA == sB and dA == dB
         and prep_free and (not v_id["admissible"]) and s_id == s_adm
         and sum(sig_dist.values()) == 3005 and len(sig_dist) == 4
         and min(sig_dist, key=lambda s: Fr(s)) == "3/4"
         and sig_dist["3/4"] == 5,
         TABLES["feynman_blind_spots"])
    FINDINGS["feynman_gate_positive"] = bool(s_adm != s_bad)
    FINDINGS["feynman_gate_blind_to_occupancy"] = bool(sA == sB and dA == dB)
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
    """FORGING COST.  The LOWER BOUND |Obs| is sound for every admitted law,
    additions included: obstruction membership depends only on comp(F),
    which nothing else in the altered law can change, so every member must
    be deleted and no addition removes one.

    The bound is ATTAINED exactly when the complement admits the boundary --
    a separate condition, MEASURED here and never assumed.  It is an IFF:
    an alteration of size |Obs| must delete all of Obs and nothing else, so
    it is the complement itself.  When the complement does not admit, the
    true cost is strictly greater and this function reports no cost at all
    rather than the bound (the REV and const_0 rows of L2-29/L2-30 are
    exactly that case)."""
    O = obstruction_set(law, part)
    Ok = set(key(F) for F in O)
    Lt = [F for F in law if key(F) not in Ok]
    closed = is_composition_closed(Lt)
    v = adjudicate(part, pres_of(Lt, part), Lt, frozenset(range(n)), n)
    attained = bool(v["admissible"])
    return {"lower_bound": len(O), "bound_attained": attained,
            "cost": len(O) if attained else None,
            "law_size": len(law), "remaining": len(Lt),
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
    for lawname, mk in (("DET", law_det), ("ALL", law_all)):
        for m in (3, 4):
            if lawname == "ALL" and m > 3:
                continue
            lw = mk(m)
            for p in CB.parts_of(m):
                if p == CB.discrete(m):
                    continue
                r = forging_cost(lw, p, m)
                scaling.append({"configurations": m, "law": lawname,
                                "boundary": [list(b) for b in p],
                                "identifications": sum(len(b) - 1 for b in p),
                                "lower_bound": r["lower_bound"],
                                "bound_attained": r["bound_attained"],
                                "cost": r["cost"], "law_size": r["law_size"],
                                "remaining_is_a_law": r["remaining_is_a_law"],
                                "admissible_after":
                                    r["boundary_admissible_after"]})
    TABLES["cost_scaling"] = scaling

    closure_ok = all(s["remaining_is_a_law"] for s in scaling) and \
        all(r["remaining_is_a_law"] for r in rows)
    achieved = all(r["boundary_admissible_after"] for r in rows) and \
        all(s["admissible_after"] for s in scaling)
    gate("L2-16", "cost",
         "THE COMPLEMENT OF THE OBSTRUCTION IS A LAW -- and that is ALL this "
         "lemma says.  If a composite lies in the obstruction then so does "
         "its right factor, because the fibres of the composite refine the "
         "fibres of that factor; the relational form of the same argument is "
         "in the paper, since Definition 2.1 admits left-total relations and "
         "not only maps.  The lemma does NOT say the boundary is admissible "
         "in the complement: that is a separate four-clause condition, it is "
         "the hypothesis of the exact-cost statement, and it is MEASURED "
         "here rather than inherited -- under DET exhaustively over every "
         "non-discrete boundary at three and four configurations and over "
         "the four levels of the tower at five, and under the full "
         "left-total family ALL at three.  Every row carries the law it was "
         "measured under; L2-31 exhibits the laws where the hypothesis fails",
         closure_ok and achieved,
         {"tower": rows, "exhaustive_rows": len(scaling),
          "laws_swept": sorted(set(s["law"] for s in scaling))})

    # -- exact minimality: each obstruction member alone falsifies (i-a).
    #    The family tested is the COMPLEMENT plus that one member, so the
    #    test is a function of F -- and it is run on every member, not forty.
    each_alone = True
    members_tested = 0
    for part in [t[2] for t in tower]:
        O = obstruction_set(law, part)
        Ok = set(key(F) for F in O)
        comp_fam = [G for G in pres_of(law, part) if key(G) not in Ok]
        for F in O:
            members_tested += 1
            if ker_of_family(comp_fam + [F], n) == part:
                each_alone = False
    gate("L2-17", "cost",
         "EVERY MEMBER OF THE OBSTRUCTION MUST BE DELETED -- the lower "
         "bound's mechanism, tested on every member rather than sampled.  "
         "Retaining a single obstruction member F leaves the declared "
         "boundary strictly coarser than the minimal sufficient boundary of "
         "the family it belongs to, so (i-a) fails: the family tested here "
         "is the COMPLEMENT PLUS F, and ker of it is compared with the "
         "declared boundary.  Run on all 4860 members across the four levels "
         "of the tower, 120 + 360 + 1260 + 3120, with no exception.  No "
         "addition can remove a member either, because obstruction "
         "membership depends only on comp(F), which nothing else in the "
         "altered law can change.  Hence the cost is at least the "
         "obstruction's cardinality, additions included -- a LOWER BOUND, "
         "sound for every admitted law",
         each_alone and members_tested == 4860,
         {"members_tested": members_tested})

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
         "exactly five admitted operations out of 3125.  These are COSTS, "
         "not merely lower bounds, because under DET the attainment "
         "hypothesis is measured to hold at all four levels (L2-16); under "
         "REV it fails and the same arithmetic would be wrong (L2-29).  What "
         "remains at the limit is not an altered version of the original law "
         "but a complete alternative one: the Borges bound, stated only as "
         "far as these finite numbers carry it, and only under the law they "
         "were measured at",
         grows and costs == [120, 360, 1260, 3120] and limit["remaining"] == 5,
         {"costs": costs, "remaining_at_the_limit": limit["remaining"]})

    # -- and the strong form: within the identity-containing class, no
    #    forgery at all -- general, not a fact about the levels swept.
    all_delete_identity = all(r["identity_deleted"] for r in rows) and \
        all(obstruction_set(law_det(m), p) and
            any(key(F) == key(sup_of_map(tuple(range(m))))
                for F in obstruction_set(law_det(m), p))
            for m in (3, 4) for p in CB.parts_of(m) if p != CB.discrete(m))
    id_in_obs_general = all(
        any(key(F) == key(sup_of_map(tuple(range(m)))) for F in
            obstruction_set(lw, p))
        for m in (3, 4) for nm, lw in (("DET", law_det(m)), ("REV", law_rev(m)),
                                       ("FUNNEL-CLOSURE", law_funnel_closure(m)))
        for p in CB.parts_of(m) if p != CB.discrete(m))
    gate("L2-19", "cost",
         "NO FORGERY AT ANY PRICE INSIDE THE IDENTITY-CONTAINING CLASS -- "
         "and this is a one-line corollary of the rigidity theorem, not a "
         "fact about the levels swept.  comp(id) is discrete, which refines "
         "every boundary, so the identity lies in Pres_L(pi) for EVERY law "
         "and every boundary; and the identity separates every pair, so it "
         "lies in the obstruction of every non-discrete boundary.  Any "
         "admissible altered law must therefore delete the identity and "
         "leave the class.  The class that is provably closed to forgery is "
         "the class of IDENTITY-CONTAINING laws, which is larger than the "
         "five committed families.  Measured at every non-discrete boundary "
         "at three and four configurations under DET, REV and the funnel "
         "closure, and at all four levels of the tower.  The pre-registered "
         "RQ0-L2-CHEAP-LAW-FORGERY does NOT occur at the committed scope: "
         "under DET the cheapest forgery deletes 120 of 3125 operations, "
         "under REV it costs more than the law itself (L2-29), and inside "
         "the identity-containing class it is unavailable at any price.  The "
         "one-operation forgery of L2-30 lives at a degenerate identity-free "
         "law of a single constant operation, outside the committed class, "
         "and is disclosed rather than absorbed",
         all_delete_identity and id_in_obs_general,
         {"identity_in_every_obstruction_measured": True,
          "general_over_identity_containing_laws": id_in_obs_general})

    # -- THE FIRST COUNTEREXAMPLE: REV, where the complement is EMPTY and
    #    the cheapest forgery needs an ADDITION.
    rev_rows = []
    for m in (3, 4):
        rev = law_rev(m)
        for p in CB.parts_of(m):
            if p == CB.discrete(m):
                continue
            O = obstruction_set(rev, p)
            Lt = [F for F in rev if key(F) not in set(key(G) for G in O)]
            a = block_min_idempotent(p, m)
            v_empty = adjudicate(p, pres_of([], p), [], frozenset(range(m)), m)
            v_add = adjudicate(p, pres_of([a], p), [a], frozenset(range(m)), m)
            rev_rows.append({
                "configurations": m, "boundary": [list(b) for b in p],
                "law_size": len(rev), "lower_bound": len(O),
                "complement_size": len(Lt),
                "the_empty_law_is_admissible": v_empty["admissible"],
                "block_minimum_idempotent": key(a),
                "its_law_is_composition_closed": is_composition_closed([a]),
                "boundary_admissible_there": v_add["admissible"],
                "true_cost": len(rev) + 1})
    # a full brute force at three configurations: EVERY composition-closed
    # law at distance at most 7 from REV_3, over the full left-total family.
    rev3 = law_rev(3)
    revk = set(key(F) for F in rev3)
    brute = {"laws_tested": 0, "cheapest": None}
    for p in CB.parts_of(3):
        if p == CB.discrete(3):
            continue
        for Lt in [[]] + [[F] for F in CB.relations_of(3)
                          if key(F) not in revk]:
            if not is_composition_closed(Lt):
                continue
            brute["laws_tested"] += 1
            if adjudicate(p, pres_of(Lt, p), Lt, frozenset(range(3)),
                          3)["admissible"]:
                d = len(rev3) + len(Lt)
                if brute["cheapest"] is None or d < brute["cheapest"]:
                    brute["cheapest"] = d
    TABLES["counterexample_REV"] = {"rows": rev_rows, "brute_force_n3": brute,
                                    "counterexamples": len(rev_rows)}
    gate("L2-29", "cost-counterexample",
         "THE EXACT-COST CLAIM IS FALSE IN GENERAL, and REV refutes it "
         "inside the committed law families.  Every permutation is "
         "collision-free, so comp is discrete, so Pres_REV(pi) is ALL of REV "
         "at every boundary, and every permutation separates every pair: the "
         "obstruction is the whole law and THE COMPLEMENT IS EMPTY.  The "
         "empty declared family fails (i-a) -- its minimal boundary is the "
         "one-atom boundary by the standing convention -- so the boundary is "
         "not admissible in the complement, and an alteration of size |Obs| "
         "must BE the complement.  The cheapest forgery is therefore |REV| + "
         "1 and it requires an ADDITION: delete every permutation and add "
         "the BLOCK-MINIMUM IDEMPOTENT, under which the boundary passes all "
         "four clauses.  6 -> 7 at three configurations (4 boundaries) and "
         "24 -> 25 at four (14 boundaries): 18 counterexamples inside the "
         "range the exhaustive tag advertises.  Confirmed at three "
         "configurations by brute force over EVERY composition-closed law at "
         "distance at most 7, drawn from the full left-total family.  So "
         "'additions never help' is withdrawn: an addition can be NECESSARY",
         all(r["lower_bound"] == r["law_size"] and r["complement_size"] == 0
             and not r["the_empty_law_is_admissible"]
             and r["its_law_is_composition_closed"]
             and r["boundary_admissible_there"] for r in rev_rows)
         and len(rev_rows) == 18 and brute["cheapest"] == 7,
         TABLES["counterexample_REV"])

    # -- THE SECOND COUNTEREXAMPLE: |Obs| = 0 at an inadmissible boundary.
    const0 = sup_of_map((0, 0, 0))
    Lc, pc = [const0], ((0,), (1, 2))
    v_c = adjudicate(pc, pres_of(Lc, pc), Lc, frozenset(range(3)), 3)
    add_sols = []
    for F in CB.relations_of(3):
        Lt = [const0, F]
        if key(F) == key(const0) or not is_composition_closed(Lt):
            continue
        if adjudicate(pc, pres_of(Lt, pc), Lt, frozenset(range(3)),
                      3)["admissible"]:
            add_sols.append(key(F))
    v_del = adjudicate(pc, [], [], frozenset(range(3)), 3)
    TABLES["counterexample_const0"] = {
        "law": "{const_0} on three configurations, composition-closed and "
               "identity-free",
        "boundary": [list(b) for b in pc],
        "preserving_family_size": v_c["pres_size"],
        "obstruction_size": len(obstruction_set(Lc, pc)),
        "boundary_admissible_as_declared": v_c["admissible"],
        "the_single_deletion_leaves_the_empty_law_inadmissible":
            not v_del["admissible"],
        "single_additions_that_make_it_admissible": add_sols,
        "true_cost": 1}
    gate("L2-30", "cost-counterexample",
         "AND THE OBSTRUCTION CAN BE EMPTY AT A BOUNDARY THAT IS "
         "INADMISSIBLE AT ANY PRICE -- the sharper failure of the exact-cost "
         "claim.  Take the composition-closed identity-free law {const_0} at "
         "three configurations and the boundary {0|12}.  The images of the "
         "two blocks are {0} and {0}, not disjoint, so the preserving family "
         "is EMPTY, so the obstruction is empty and |Obs| = 0 would report "
         "the boundary as already admissible.  It is not: with an empty "
         "declared family (i-a) fails.  The obstruction sees only "
         "over-separation INSIDE a block and is blind to under-separation "
         "BETWEEN blocks -- the decision procedure's own second witness "
         "branch -- and to (ii-a) and (ii-b) entirely.  The true cost is ONE: "
         "deleting const_0 leaves the empty law, still inadmissible, but a "
         "single ADDITION suffices, and three distinct additions achieve it, "
         "because const_0 never enters the declared family and so never "
         "needs removing",
         v_c["pres_size"] == 0 and len(obstruction_set(Lc, pc)) == 0
         and (not v_c["admissible"]) and (not v_del["admissible"])
         and len(add_sols) == 3,
         TABLES["counterexample_const0"])

    # -- THE EQUALITY CRITERION, and the census of where it fails.
    cen = census_T3()
    TABLES["cost_equality_criterion"] = {
        "population": "every composition-closed law on three configurations "
                      "generated by at most three maps, against every "
                      "non-discrete boundary",
        "laws": cen["laws"], "pairs": cen["cost_pairs"],
        "complement_does_not_admit": cen["complement_does_not_admit"],
        "of_those_with_a_non_empty_complement":
            cen["complement_non_empty_and_does_not_admit"],
        "DET_and_ALL_rows_all_attain": achieved}
    gate("L2-31", "cost",
         "THE COST EQUALS THE OBSTRUCTION'S SIZE EXACTLY WHEN THE COMPLEMENT "
         "ADMITS THE BOUNDARY -- an IFF, which is the corrected statement.  "
         "One direction is the lower bound plus the complement; the other is "
         "forced, since an alteration of size |Obs| must delete all of Obs "
         "and nothing else and therefore IS the complement.  So the "
         "hypothesis is not a convenience, it is the exact criterion.  "
         "Censused over the 687 composition-closed laws at three "
         "configurations against every non-discrete boundary: in 1008 of the "
         "2748 pairs the complement does not admit the boundary, so in every "
         "one of those the true cost is STRICTLY GREATER than the "
         "obstruction's size; 927 of them have a non-empty complement, so "
         "this is not an artefact of emptiness.  The committed law of the "
         "tower is clean: DET at three, four and five configurations attains "
         "the bound everywhere swept, and so does the full left-total family "
         "at three.  That is why the tower stands and the general claim does "
         "not",
         cen["cost_pairs"] == 2748 and cen["complement_does_not_admit"] == 1008
         and cen["complement_non_empty_and_does_not_admit"] == 927
         and achieved,
         TABLES["cost_equality_criterion"])

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
         "committed law and on the altered law itself.  There is no SINGLE "
         "law, at any cost, in which both members of the colluding pair are "
         "admissible -- the quantifier is one law shared by both contexts, "
         "which is the theorem's hypothesis; L2-27 exhibits the escape when "
         "each context declares its own",
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
                    "L2-13", "L2-21", "L2-22", "L2-23", "L2-24", "L2-25",
                    "L2-26", "L2-27"))
    feyn_ok = all(g["passed"] for g in GATES if g["id"] in ("L2-14", "L2-15",
                                                            "L2-28"))
    cost_ok = all(g["passed"] for g in GATES if g["id"] in
                  ("L2-16", "L2-17", "L2-18", "L2-19", "L2-20", "L2-29",
                   "L2-30", "L2-31"))
    if axiom_ok:
        v["registered"].append({
            "rung": "RQ0-L2-GENERATIVE-ATLAS-AXIOM",
            "status": "earned at the declared scope",
            "content":
                "the two-condition axiom is well posed, decidable, and "
                "discriminating in both directions: the colluding pair's "
                "forged member is rejected with the killing conditions named "
                "-- declaration-relative, and the declaration disclosed -- "
                "and a witness exhibited; the pair is jointly unforgeable at "
                "any SHARED law, with the mixed-law escape exhibited and the "
                "mixed-law arena named open; the legitimate eraser context "
                "passes both conditions; the relabelled and counter-law "
                "contexts get honest verdicts with the law-relativity "
                "disclosed; and the arena's dependent pair is returned as "
                "one patch",
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
                "the rigidity DICHOTOMY, proved in both directions: the "
                "carrier's own configuration algebra is admissible if and "
                "only if the law contains the identity, equivalently if and "
                "only if it contains any reversible operation -- so a law "
                "has either exactly one chart, the carrier's, or no carrier "
                "chart at all and possibly several proper ones, with nothing "
                "in between.  The trigger is REVERSIBILITY, not idling.  The "
                "axiom therefore certifies relative to a declared carrier "
                "rather than deriving one, and the de-smuggling question "
                "moves up one level, from the boundary to the carrier.  The "
                "block is not the only available diagnosis: condition (i) "
                "pairs ker with Pres, which are adjoints of DIFFERENT "
                "connections, and the selectivity is produced by that "
                "substitution (L2-22)",
            "scope": "the same declared scope; the theorem is proved and "
                     "measured exhaustively, not sampled"})
    v["not_occurring"] = [
        {"rung": "RQ0-L2-EMPIRICALLY-IDLE",
         "why": "the Feynman gate is positive: at one fixed boundary an "
                "admissible and an inadmissible patch differ in an admitted "
                "tester statistic, exactly 1 against exactly 3/4"},
        {"rung": "RQ0-L2-CHEAP-LAW-FORGERY",
         "why": "at the committed scope the cheapest forgery deletes 120 of "
                "3125 admitted operations, the identity lies in the "
                "obstruction of every non-discrete boundary at every "
                "identity-containing law so no forgery is available inside "
                "that class at any price, the cost grows 120 to 360 to 1260 "
                "to 3120 along the tower, and at the pair level the forgery "
                "is impossible at any cost.  Disclosed with it: under REV "
                "the cheapest forgery costs more than the whole law, and at "
                "the degenerate identity-free law {const_0} outside the "
                "committed class a single addition suffices"}]
    v["feynman_gate"] = "POSITIVE" if feyn_ok else "NOT ESTABLISHED"
    v["collusion_cost"] = "POSITIVE, GROWING, AND TERMINATING AT THE PAIR " \
                          "LEVEL" if cost_ok else "NOT ESTABLISHED"
    return v


NONCLAIMS = [
    "REACHABILITY IS AN ORDER ON CONFIGURATIONS.  It carries no spatial, "
    "causal, temporal or spacetime reading of any kind, and the reachable "
    "subprocess is not a region, a light cone, a neighbourhood or a history.",
    "no locality, topology, atlas-as-place, manifold or geometric object; "
    "the word patch names a QUADRUPLE of committed operational data -- "
    "boundary, declared family, declared preparation, admitted law -- and "
    "nothing else",
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
    "NO CLAIM THAT THE FORGING COST EQUALS THE OBSTRUCTION'S SIZE IN "
    "GENERAL: that is false, refuted here at REV and at a law with an empty "
    "obstruction.  What is claimed is the lower bound, sound everywhere, and "
    "the equality exactly where the complement admits the boundary -- "
    "measured under DET, where the tower runs",
    "no claim that condition (i) is Cycle B's two-sided Galois fixed point: "
    "it pairs ker with Pres, which are adjoints of different connections, "
    "and Cycle B Theorem 3.8 records the conflation as the one to avoid",
    "no claim that joint unforgeability holds across DIFFERENT declared "
    "laws: it is a statement about one law shared by both contexts, and the "
    "mixed-law escape is exhibited",
    "no claim that an admitted statistic can see the occupancy clause: "
    "neither tester statistic reads the declared preparation, and an "
    "occupancy-sensitive statistic is left open",
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
                "census-lax": "the census population is restricted to the "
                              "identity-containing laws, so the dichotomy, "
                              "the comparable-pairs strengthening, the "
                              "entailment population and the cost equality "
                              "criterion all lose the half of the population "
                              "that carries them",
                "forgery-lax": "the block-minimum idempotent is replaced by "
                               "the identity, so the REV counterexample's "
                               "cheapest forgery cannot be exhibited",
                "declaration-lax": "every declared family in the "
                                   "declaration-relative table is replaced by "
                                   "the boundary's closure, so the kill-list "
                                   "stops being declaration-relative",
                "blind-lax": "the occupancy-blindness comparison gives both "
                             "patches the full preparation, so the two "
                             "verdicts agree and the blind spot cannot fire",
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
    A("THE AXIOM.  A patch is a QUADRUPLE (boundary, declared task family,")
    A("declared preparation, admitted law) on the committed carrier.  It is")
    A("ADMISSIBLE iff")
    A("  (i-a)  A(B) = ker(F)          the boundary is the #103-minimal")
    A("                               sufficient boundary of its own family")
    A("                               -- ker, NOT Cycle B's Core (L2-22)")
    A("  (i-b)  F   = Pres_L(A(B))     the family is the boundary's Cycle B")
    A("                               closure (availability criterion)")
    A("  (ii-a) the family is non-empty and comp(F) = A(B) for all F in it")
    A("                               -- the realized legs write exactly")
    A("                               what the boundary asserts")
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
    A(f"  jointly unforgeable AT A SHARED LAW: no committed law admits both "
      f"--  {[r for r in cp['joint']]}")
    mx = rec["tables"]["mixed_law_escape"]
    A(f"  THE MIXED-LAW ESCAPE (one law per context, the declared scope): "
      f"member 1 is")
    A(f"    ADMISSIBLE under {mx['member_1']['law']} "
      f"(family {mx['member_1']['declared_family_size']}), member 2 "
      f"admissible under DET.")
    A(f"    {mx['open_question']}")
    A("")
    A("THE KILL-LIST IS DECLARATION-RELATIVE (at the forged boundary, DET):")
    dr = rec["tables"]["declaration_relativity"]
    A(f"{'declared family':<66}{'size':<7}{'adm':<6}killed by")
    for r in dr["declarations"]:
        A(f"{r['declared_family']:<66}{r['size']:<7}"
          f"{str(r['admissible']):<6}{r['killed_by']}")
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
    A(f"    the comparator's kill-list, COMPUTED: "
      f"{sb['inadmissible_patch']['fails']}")
    A(f"  the forged patch: sigma = {tf['sigma_forged']} (does NOT separate); "
      f"delta = {tf['delta_forged']} against {tf['delta_admissible']} "
      f"(separates)")
    A(f"  {fg['vacuity_disclosure']}")
    bs = rec["tables"]["feynman_blind_spots"]
    ob = bs["occupancy_blindness"]
    A("  BLIND TO OCCUPANCY -- the axiom's only independent clause.  Two "
      "patches under the")
    A(f"    counter-law differing in the PREPARATION alone: "
      f"{ob['patch_A']['preparation']} -> admissible "
      f"{ob['patch_A']['admissible']}, sigma {ob['patch_A']['sigma']}, delta "
      f"{ob['patch_A']['delta']};")
    A(f"    {ob['patch_B']['preparation']} -> admissible "
      f"{ob['patch_B']['admissible']} (reach {ob['patch_B']['reach']}), "
      f"sigma {ob['patch_B']['sigma']}, delta {ob['patch_B']['delta']}.")
    A(f"    Neither statistic takes the preparation as an argument: "
      f"sigma{tuple(ob['neither_statistic_takes_the_preparation_as_an_argument']['sigma_arguments'])}.")
    A(f"  BLIND IN THE OMISSION DIRECTION: "
      f"{bs['omission_blindness']['patch']} is admissible "
      f"{bs['omission_blindness']['admissible']} with sigma "
      f"{bs['omission_blindness']['sigma']}.")
    sd = bs["sigma_over_every_one_task_extension_of_the_closure"]
    A(f"  sigma over all {sd['extensions']} one-task extensions: "
      f"{sd['distinct_values']}; minimum {sd['minimum']} attained by exactly "
      f"{sd['attained_by']}.")
    A("  AN OCCUPANCY-SENSITIVE STATISTIC IS LEFT OPEN.")
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
    A(f"  pair level: IMPOSSIBLE at any cost, at a SHARED law.  After paying "
      f"the record-level cost the second member is admissible = "
      f"{pl['after_paying_the_record_level_cost_member_2_admissible']}")
    ce = rec["tables"]["cost_equality_criterion"]
    A(f"  the cost equals |Obs| EXACTLY WHEN the complement admits the "
      f"boundary.  Over the")
    A(f"  {ce['laws']}-law census, {ce['complement_does_not_admit']} of "
      f"{ce['pairs']} pairs fail that condition "
      f"({ce['of_those_with_a_non_empty_complement']} with a non-empty "
      f"complement),")
    A(f"  so their true cost is strictly greater; DET and ALL attain it "
      f"everywhere swept.")
    rv = rec["tables"]["counterexample_REV"]
    A(f"  COUNTEREXAMPLE 1 -- REV: {rv['counterexamples']} boundaries at "
      f"n=3,4 with an EMPTY complement;")
    A(f"    the cheapest forgery needs an ADDITION and costs n!+1 "
      f"(6->7, 24->25); brute force at")
    A(f"    n=3 over every law at distance <= 7 confirms "
      f"{rv['brute_force_n3']['cheapest']}.")
    c0 = rec["tables"]["counterexample_const0"]
    A(f"  COUNTEREXAMPLE 2 -- {{const_0}} at {c0['boundary']}: |Obs| = "
      f"{c0['obstruction_size']} while the boundary is")
    A(f"    inadmissible; true cost {c0['true_cost']}, by any of "
      f"{len(c0['single_additions_that_make_it_admissible'])} single "
      f"additions.")
    A("")
    A("-" * 78)
    A("THE RIGIDITY SWEEP")
    A("-" * 78)
    A(f"{'n':<4}{'law':<16}{'|L|':<8}{'id':<6}{'rev':<6}{'closed':<22}"
      f"{'records':<10}admissible boundaries")
    for r in rec["tables"]["rigidity_sweep"]:
        A(f"{r['configurations']:<4}{r['law']:<16}{r['size']:<8}"
          f"{str(r['contains_identity']):<6}"
          f"{str(r['contains_a_reversible_operation']):<6}"
          f"{str(r['composition_closed']) + ' (' + r['how'] + ')':<22}"
          f"{r['records']:<10}{r['admissible_boundaries']}")
    ifc = rec["tables"]["identity_free_control"]
    A(f"  identity-free control: law {ifc['law']}  closed="
      f"{ifc['composition_closed']}  contains identity="
      f"{ifc['contains_identity']}")
    A(f"      admissible boundaries (with family size): {ifc['admissible']}")
    fc = rec["tables"]["funnel_closure"]
    A(f"  FUNNEL is composition-closed at: "
      f"{fc['FUNNEL_is_composition_closed']} -- a declared TASK FAMILY, not "
      f"a law at n>=3;")
    A(f"      the law it generates has sizes {fc['closure_sizes']} and the "
      f"three re-run sweeps move nothing.")
    dc = rec["tables"]["dichotomy"]["census_at_three_configurations"]
    A(f"  THE DICHOTOMY, censused over {dc['laws']} laws at three "
      f"configurations:")
    A(f"      the carrier's algebra is admissible IFF the law contains the "
      f"identity: {dc['discrete_admissible_iff_identity']} of {dc['laws']}")
    A(f"      identity-containing {dc['identity_containing']} = "
      f"reversible-containing {dc['reversible_containing']}  "
      f"(reversible but no identity: {dc['reversible_but_no_identity']})")
    A(f"      laws admitting a PROPER boundary "
      f"{dc['admitting_a_proper_boundary']}; of them, identity-containing "
      f"{dc['identity_containing_with_a_proper_boundary']}")
    A(f"      admissible pairs {dc['admissible_pairs']}, comparable among "
      f"them {dc['comparable_admissible_pairs']}")
    mech = rec["tables"]["mechanism"]
    A("  THE MECHANISM: condition (i) pairs ker with Pres -- adjoints of "
      "DIFFERENT connections.")
    A(f"{'':<6}{'n':<4}{'law':<14}{'records':<10}{'Core.Pres fixes':<18}"
      f"ker.Pres fixes")
    for r in mech["fixed_records"]:
        A(f"{'':<6}{r['configurations']:<4}{r['law']:<14}{r['records']:<10}"
          f"{r['records_fixed_by_Core_after_Pres']:<18}"
          f"{r['records_fixed_by_ker_after_Pres']}")
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
