#!/usr/bin/env python3
"""Run every exact Paper 2 result and write a reproducible receipt."""
from __future__ import annotations

import sys
from fractions import Fraction
from itertools import permutations

from core import (
    DynamicChart,
    Q,
    Token,
    canonical_maps,
    descent_data_errors,
    full_automorphisms,
    full_isomorphisms,
    graph_supported,
    identity_perm,
    induced_token_maps,
    inverse_perm,
    provenance_compatible,
    realized_isomorphisms,
    same_fact_by_extension,
    same_fact_by_witness,
    solve_descent,
)
from models import (
    accidental_equal_marginals_joint,
    anticorrelated_joint,
    common_witness_joint,
    counterfactual_completion_charts,
    same_fact_joint,
)


class Receipts:
    def __init__(self, mutant: bool = False) -> None:
        self.rows = []
        self.mutant = mutant

    def check(self, label, computed, expected) -> None:
        if self.mutant and label == "A full automorphism group is trivial":
            expected = 2
            print("[MUTANT] deliberately breaking the automorphism-count anchor")
        ok = computed == expected
        self.rows.append((label, computed, expected, ok))
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: {computed!r}")

    def finish(self) -> int:
        failures = [r for r in self.rows if not r[3]]
        print("-" * 78)
        print(f"{len(self.rows)} checks: {len(self.rows)-len(failures)} pass, {len(failures)} fail")
        return len(failures)


R = Receipts(mutant="--mutant" in sys.argv[1:])

print("=" * 78)
print("PAPER 2 -- RECORD CO-REFERENCE AND EFFECTIVE DESCENT")
print("Exact standard-library reproduction")
print("=" * 78)

# ---------------------------------------------------------------------------
print("\n1. FACT IDENTITY IS NOT VALUE OR DISTRIBUTION EQUALITY")
R.check("same-fact diagonal extension certifies", same_fact_by_extension(same_fact_joint()), True)
R.check(
    "equal marginals under independent product do not certify one fact",
    same_fact_by_extension(accidental_equal_marginals_joint()),
    False,
)
anti = anticorrelated_joint()
R.check("perfect anticorrelation is not identity of values", same_fact_by_extension(anti), False)
R.check("perfect anticorrelation lies on the flip graph", graph_supported(anti, {"0": "1", "1": "0"}), True)
R.check("third-record witness certifies sameness", same_fact_by_witness(common_witness_joint()), True)

# ---------------------------------------------------------------------------
print("\n2. FACT IDENTITY IS NOT EVENT-TOKEN IDENTITY")
original = Token("R", ("0", "1"), ("write-1", "original"), True, True)
copy = Token("R-copy", ("0", "1"), ("write-2", "copy-of-R"), True, True)
R.check("redundant records carry one fact", same_fact_by_extension(same_fact_joint()), True)
R.check("original and copy are different occurrences", provenance_compatible(original, copy), False)
erased = Token("R-erased", ("0", "1"), ("write-1", "original"), True, False)
never = None
R.check("erased token remains a historical occurrence", erased.occurred, True)
R.check("erased token is not presently available", erased.available, False)
R.check("never-written chart has no historical token", never is None, True)
R.check("empty available/available comparison is vacuous, not forced", (not erased.available and never is None), True)

# ---------------------------------------------------------------------------
print("\n3. EFFECTIVE DESCENT: SET, GROUPOID, UNDERDETERMINED, NO-DESCENT")
# Set amalgam: three singleton charts.
phi_set = {(a, b): ((0,),) for a in range(3) for b in range(3) if a != b}
aut_set = [((0,),)] * 3
res_set = solve_descent([1, 1, 1], phi_set, aut_set)
R.check("set model verdict", res_set.verdict, "SET-AMALGAM")
R.check("set model coherent families", res_set.coherent_families, 1)
R.check("set model stabilizer", res_set.representative_stabilizer, 1)
R.check("set model injective colimit", res_set.injective_colimit, True)

# Symmetric duplicate: all two-token bijections allowed, S2 automorphisms.
S2 = tuple(tuple(p) for p in permutations(range(2)))
phi_groupoid = {(a, b): S2 for a in range(3) for b in range(3) if a != b}
aut_groupoid = [S2, S2, S2]
res_groupoid = solve_descent([2, 2, 2], phi_groupoid, aut_groupoid)
R.check(
    "symmetric model gauge action validates",
    descent_data_errors([2, 2, 2], phi_groupoid, aut_groupoid),
    (),
)
R.check("symmetric model verdict", res_groupoid.verdict, "GROUPOID-AMALGAM")
R.check("symmetric model coherent families", res_groupoid.coherent_families, 4)
R.check("symmetric model gauge orbits", res_groupoid.gauge_orbits, 1)
R.check("symmetric model stabilizer", res_groupoid.representative_stabilizer, 2)
R.check("symmetric model injective colimit", res_groupoid.injective_colimit, True)

# Same local candidate maps but no chart automorphisms: four inequivalent orbits.
aut_trivial = [((0, 1),)] * 3
res_under = solve_descent([2, 2, 2], phi_groupoid, aut_trivial)
R.check("unquotiented symmetric data are underdetermined", res_under.verdict, "UNDERDETERMINED")
R.check("underdetermined coherent families", res_under.coherent_families, 4)
R.check("underdetermined gauge orbits", res_under.gauge_orbits, 4)

# Twisted triangle: id, id, swap, with inverse edges declared consistently.
id2, sw2 = (0, 1), (1, 0)
phi_twist = {
    (0, 1): (id2,), (1, 0): (id2,),
    (1, 2): (id2,), (2, 1): (id2,),
    (0, 2): (sw2,), (2, 0): (sw2,),
}
res_twist = solve_descent([2, 2, 2], phi_twist, aut_trivial)
R.check("twisted triangle verdict", res_twist.verdict, "NO-DESCENT")
R.check("twisted triangle coherent families", res_twist.coherent_families, 0)

# Missing edge.
phi_missing = dict(phi_twist)
phi_missing[(0, 2)] = ()
res_missing = solve_descent([2, 2, 2], phi_missing, aut_trivial)
R.check("missing pair verdict", res_missing.verdict, "ABSENT-PAIR")

# A non-equivariant candidate set is not a gauge action. The old solver
# silently classified this input; the repaired instrument must reject it.
phi_not_gauge_closed = {(a, b): (id2,) for a in range(3) for b in range(3) if a != b}
try:
    solve_descent([2, 2, 2], phi_not_gauge_closed, aut_groupoid)
    rejected_non_equivariant = False
except ValueError:
    rejected_non_equivariant = True
R.check("non-equivariant candidate data are rejected", rejected_non_equivariant, True)

# ---------------------------------------------------------------------------
print("\n4. NO NATURAL CHOICE IN THE PRESENCE OF TOKEN SYMMETRY")
canon = canonical_maps(S2, S2, S2)
R.check("canonical maps fixed by independent S2 automorphisms", len(canon), 0)

# ---------------------------------------------------------------------------
print("\n5. COUNTERFACTUAL-COMPLETION SENSITIVITY")
A, B_id, B_swap, P = counterfactual_completion_charts()
R.check("A full automorphism group is trivial", len(full_automorphisms(A)), 1)
R.check("the two completions have the same realized distribution", B_id.realized_distribution(), B_swap.realized_distribution())
R.check("the two completions have the same actual record law", B_id.record_law(), B_swap.record_law())

real_id = realized_isomorphisms(A, B_id)
real_swap = realized_isomorphisms(A, B_swap)
R.check("realized-support A<-B_id candidate count", len(real_id), 4)
R.check("realized-support A<-B_swap candidate count", len(real_swap), 4)
R.check("realized token maps are identity and swap", {x[1] for x in real_id}, {(0, 1), (1, 0)})
R.check("same realized token-map set for both completions", {x[1] for x in real_id}, {x[1] for x in real_swap})

# Provenance is load-bearing in event-token identity and is now consumed by
# the chart-isomorphism enumerator itself, not merely checked on the side.
same_provenance = induced_token_maps(A, A, identity_perm(A.n), range(A.n))
changed_tokens = (
    Token("A-prime", A.tokens[0].values_by_configuration, ("different-origin",)),
    A.tokens[1],
)
A_changed = DynamicChart("A_changed", A.transition, A.initial, changed_tokens)
changed_provenance = induced_token_maps(A_changed, A, identity_perm(A.n), range(A.n))
R.check("matched provenance permits the identity token map", same_provenance, ((0, 1),))
R.check("changed provenance blocks the token map", changed_provenance, ())

full_id = full_isomorphisms(A, B_id)
full_swap = full_isomorphisms(A, B_swap)
R.check("full A<-B_id isomorphism count", len(full_id), 1)
R.check("full A<-B_id token map", full_id[0][1], (0, 1))
R.check("full A<-B_swap isomorphism count", len(full_swap), 1)
R.check("full A<-B_swap token map", full_swap[0][1], (1, 0))
R.check("swap completion is generated by P", full_swap[0][0], P)

print("\nTHEOREM READOUT")
print("  Same realized process + same actual record law admit two token maps.")
print("  Two counterfactual completions select opposite maps uniquely.")
print("  Therefore no realized-only co-reference rule can reproduce full-law")
print("  event-token identity on both completions.")

failures = R.finish()
sys.exit(1 if failures else 0)
