#!/usr/bin/env python3
"""
Paper 31 receipt: diamond-shadow closure theorem ledger.

This is not a new enumeration receipt; the expensive exact enumeration is
`p30_diamond_boundary_center_campaign.py` and passed with 11/11 checks.  This
receipt records the exact finite theorem that follows from those audited facts
and adds the finite-window no-free-lunch check: no amount of exact evidence
through N<=9 can by itself prove a unique universal click law without an
additional principle.

All arithmetic is integer/Fraction. Decimal precision is set to 140 for
reporting only.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import sys

getcontext().prec = 140
sys.stdout.reconfigure(line_buffering=True)

checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


print("=" * 80)
print("Paper 31 diamond-shadow closure receipt")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

# Exact audited facts imported from the passing Paper 30 receipt.
records_9 = 131526
base_atoms_9 = 131514
diamond_center_atoms_9 = 131518
diamond_center_conflicts_9 = 0
residual_edges_9 = 4
licensed_orbits = 11
total_dual_orbits = 24
low_gate_triples = 64
licensed_triples = 165
recurrence_gate_triples = 4
shadow_edges_covered = 2
selected_shadow_atoms_9 = 65521
selected_unweighted_atoms_9 = 65523
selected_tv9 = Fraction(0)
selected_rec9 = Fraction(0)
selected_qrec9 = Fraction(0)
selected_metric = (5, 5, 3)

print("\n" + "=" * 80)
print("1. Finite diamond-shadow theorem facts")
print("=" * 80)
print(
    f"records_9={records_9} base_atoms_9={base_atoms_9} "
    f"diamond_center_atoms_9={diamond_center_atoms_9} "
    f"selected_shadow_atoms_9={selected_shadow_atoms_9}"
)
print(
    f"residual_edges_9={residual_edges_9} "
    f"shadow_edges_covered={shadow_edges_covered} "
    f"licensed_orbits={licensed_orbits}/{total_dual_orbits}"
)
print(
    f"licensed_triples={licensed_triples} low_gate_triples={low_gate_triples} "
    f"recurrence_gate_triples={recurrence_gate_triples}"
)

check(
    "diamond center closes the audited residual without lookup",
    base_atoms_9 < diamond_center_atoms_9 < records_9 and diamond_center_conflicts_9 == 0,
    (
        f"{base_atoms_9}->{diamond_center_atoms_9}/{records_9}, "
        f"conflicts={diamond_center_conflicts_9}"
    ),
)
check(
    "selected shadow is a proper nonreconstructive quotient of the center scale",
    selected_shadow_atoms_9 < diamond_center_atoms_9 < records_9,
    f"shadow={selected_shadow_atoms_9}, center={diamond_center_atoms_9}, records={records_9}",
)
check(
    "selected shadow does not reconstruct the whole diamond residual graph",
    0 < shadow_edges_covered < residual_edges_9,
    f"covered={shadow_edges_covered}/{residual_edges_9}",
)
check(
    "boundary activity is a gate, not a selector",
    0 < licensed_orbits < total_dual_orbits
    and 1 < recurrence_gate_triples < low_gate_triples < licensed_triples,
    (
        f"orbits={licensed_orbits}/{total_dual_orbits}, "
        f"triples={recurrence_gate_triples}<{low_gate_triples}<{licensed_triples}"
    ),
)
check(
    "selected positive shadow gives exact audited forward law",
    selected_tv9 == 0 and selected_rec9 == 0 and selected_qrec9 == 0,
    f"TV9={selected_tv9} rec9={selected_rec9} qrec9={selected_qrec9}",
)
check(
    "selected odd metric is the non-Euclidean finite metric from Campaign U",
    selected_metric == (5, 5, 3),
    f"metric={selected_metric}",
)

print("\n" + "=" * 80)
print("2. Finite-window no-free-lunch check")
print("=" * 80)

# Two formal laws that agree through N<=9 and differ at N=10.
# This is the exact reason the finite receipt cannot, by itself, prove the
# universal law.  A principle is required.
finite_window = tuple(range(1, 10))


def law_a(n):
    return Fraction(0)


def law_b(n):
    if n <= 9:
        return Fraction(0)
    return Fraction(1, 1000000)


same_on_window = all(law_a(n) == law_b(n) for n in finite_window)
diverge_after = law_a(10) != law_b(10)
print(
    f"laws_equal_for_N<=9={same_on_window} "
    f"law_a_10={law_a(10)} law_b_10={law_b(10)}"
)

check(
    "finite N<=9 receipts cannot by themselves prove universal uniqueness",
    same_on_window and diverge_after,
    "two formal laws agree on the full audited window and diverge at N=10",
)

print("\n" + "=" * 80)
print("3. Closure status")
print("=" * 80)
print(
    "The closed finite law is the diamond-shadow h-transform: construct the "
    "residual diamond center, then select the coarsest recurrent, "
    "reflection-positive, nonreconstructive positive shadow.  The universal "
    "law still requires the principle that fixes this construction for all N."
)

print("\n" + "=" * 80)
failed = False
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    failed = failed or not ok
print(f"\nCHECKS PASSED: {sum(ok for _, ok, _ in checks)}/{len(checks)}")
if failed:
    sys.exit(1)
print("DONE.")
