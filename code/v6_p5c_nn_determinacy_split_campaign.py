#!/usr/bin/env python3
"""Paper 5 diagnostic C: normal-normal determinacy-or-split campaign.

Finish condition:
  Either chi_NN is intrinsically determined by sealed finite record data, or
  the same sealed data can hide two different normal-normal responses.

This diagnostic proves the second side for the current SHARD GR-facing sealed
data.  It builds a cofinal projective family whose sealed shadows are identical
while the normal-normal coordinate has two actual values with stable positive
conditional mass.

The counterfamily is deliberately minimal.  It does not attack an enriched
theory that declares chi_NN itself to be part of the sealed primitive ledger.
It attacks the current claim that screen/source/hyp/rectangle sealed data alone
intrinsically determine the normal sector.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Atom:
    level: int
    branch: int
    copy: int


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def atoms(level: int) -> list[Atom]:
    return [Atom(level, branch, copy) for branch in (0, 1) for copy in range(level)]


def prob(level: int, atom: Atom) -> float:
    del atom
    return 1.0 / (2.0 * level)


def sealed_shadow(atom: Atom) -> tuple[str, str, str, str]:
    """Current sealed data excluding the disputed normal-normal coordinate."""
    del atom
    return ("hyp:h0", "nn-rectangle:ell0", "screen:q0", "source:rho0")


def chi_nn(atom: Atom) -> int:
    """The hidden normal-normal second-response coordinate."""
    return -1 if atom.branch == 0 else 1


def completed_shadow(atom: Atom) -> tuple[str, str, str, str, int]:
    """What happens if the ontology simply includes chi_NN."""
    return (*sealed_shadow(atom), chi_nn(atom))


def grouped(level: int, key_fn, value_fn) -> dict[object, list[tuple[object, float]]]:
    groups: dict[object, list[tuple[object, float]]] = defaultdict(list)
    for atom in atoms(level):
        groups[key_fn(atom)].append((value_fn(atom), prob(level, atom)))
    return groups


def conditional_variance(level: int, key_fn, value_fn) -> float:
    total = 0.0
    for entries in grouped(level, key_fn, value_fn).values():
        mass = sum(p for _, p in entries)
        mean = sum(v * p for v, p in entries) / mass
        var = sum(((v - mean) ** 2) * p for v, p in entries) / mass
        total += mass * var
    return total


def best_deterministic_success(level: int, key_fn, value_fn) -> float:
    """Best success probability for any map K(sealed_key) -> chi value."""
    success = 0.0
    for entries in grouped(level, key_fn, value_fn).values():
        counts: dict[object, float] = defaultdict(float)
        for value, p in entries:
            counts[value] += p
        success += max(counts.values())
    return success


def two_copy_split_mass(level: int, key_fn, value_fn) -> float:
    """Mass of two independent same-key draws with different chi values."""
    mass = 0.0
    for entries in grouped(level, key_fn, value_fn).values():
        counts: dict[object, float] = defaultdict(float)
        for value, p in entries:
            counts[value] += p
        fiber_mass = sum(counts.values())
        same_value = sum(p * p for p in counts.values())
        mass += fiber_mass * fiber_mass - same_value
    return mass


def pushforward_to_base_gap(level: int) -> float:
    """Exact projective compatibility to the two-row base split."""
    base_mass = {0: 0.5, 1: 0.5}
    pushed = {0: 0.0, 1: 0.0}
    for atom in atoms(level):
        pushed[atom.branch] += prob(level, atom)
    return max(abs(pushed[k] - base_mass[k]) for k in base_mass)


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    levels = [1, 2, 4, 8, 16, 32]

    shadow_counts = [len({sealed_shadow(atom) for atom in atoms(level)}) for level in levels]
    chi_counts = [len({chi_nn(atom) for atom in atoms(level)}) for level in levels]
    variances = [conditional_variance(level, sealed_shadow, chi_nn) for level in levels]
    successes = [best_deterministic_success(level, sealed_shadow, chi_nn) for level in levels]
    split_masses = [two_copy_split_mass(level, sealed_shadow, chi_nn) for level in levels]
    push_gaps = [pushforward_to_base_gap(level) for level in levels]

    completed_variances = [conditional_variance(level, completed_shadow, chi_nn) for level in levels]
    completed_successes = [best_deterministic_success(level, completed_shadow, chi_nn) for level in levels]

    rows = [
        Row(
            "same sealed shadow",
            "all atoms share X_hyp, H_NN, screen, and source data",
            "sealed data have one value while chi_NN has two values",
            f"shadow_counts={shadow_counts}, chi_counts={chi_counts}",
            "SAME-SEALED-DATA",
        ),
        Row(
            "positive actual split",
            "compute Var(chi_NN | sealed shadow)",
            "normal-normal response is not measurable with respect to current sealed data",
            f"vars={[round(v, 6) for v in variances]}",
            "SPLIT-POSITIVE",
        ),
        Row(
            "determinacy refuter",
            "best K(sealed_shadow)->chi_NN predictor",
            "no intrinsic map can succeed with probability tending to one",
            f"success={[round(s, 6) for s in successes]}",
            "REFUTES-DETERMINACY",
        ),
        Row(
            "two-copy witness",
            "two independent actual records with same sealed shadow",
            "different chi_NN occurs with stable positive same-law mass",
            f"mass={[round(m, 6) for m in split_masses]}",
            "FEYNMAN-SPLIT",
        ),
        Row(
            "cofinal refinement",
            "split each branch into level-many copies and push to base",
            "actual law and sealed shadows are projectively compatible",
            f"push_gaps={[f'{g:.1e}' for g in push_gaps]}",
            "COFINAL",
        ),
        Row(
            "completion check",
            "include chi_NN in the sealed primitive ledger",
            "determinacy becomes tautological, showing exactly what must be added",
            f"completed_var={completed_variances[-1]:.1e}, completed_success={completed_successes[-1]:.1f}",
            "ENRICHMENT-NOT-DERIVATION",
        ),
        Row(
            "campaign verdict",
            "current sealed data versus chi_NN",
            "same sealed finite record data can hide two normal-normal responses cofinally",
            "finish condition reached",
            "NN-SPLIT-PROVED",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "max_pushforward_gap": max(push_gaps),
        "min_conditional_variance": min(variances),
        "max_best_deterministic_success": max(successes),
        "min_two_copy_split_mass": min(split_masses),
        "completed_conditional_variance": completed_variances[-1],
        "completed_best_success": completed_successes[-1],
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")

    # Hard guards: this script is a proof receipt, not a visualization.
    assert max(push_gaps) == 0.0
    assert math.isclose(min(variances), 1.0)
    assert math.isclose(max(successes), 0.5)
    assert math.isclose(min(split_masses), 0.5)
    assert math.isclose(completed_variances[-1], 0.0)
    assert math.isclose(completed_successes[-1], 1.0)


if __name__ == "__main__":
    main()
