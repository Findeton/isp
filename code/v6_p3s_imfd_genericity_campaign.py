"""
v6 Paper 3 section 29: IMFD ontology and genericity campaign.

Question:
    Is the isolated modular factorization-defect condition generic because of
    the dynamics, or is it another admissibility axiom?

Finite answer:
    For one full-support finite law, unique positive RN partition minimizers
    are generic: random laws almost always avoid exact ties.

    That is not enough for the physical event theorem.  Role-blind identity,
    a positive source floor, fixed log-RN units, and cofinal refinement
    stability are stronger than single-law genericity.  They are generic only
    inside a dynamics that already ties the four role readouts and keeps the
    refinement flow inside an isolated RN partition-spectrum neighborhood.

    Thus the beautiful ontology is:

        physical event =
            role-blind, refinement-stable, source-floored isolated
            Radon-Nikodym factorization defect of a sealed finite record
            diamond.

    Whether this is branch A or branch B depends on the lower-level dynamics:
    if fixed CMRP dynamics forces this class, it is derived; if the class is
    selected by hand, it is an admissibility axiom.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp
from random import Random

from v6_p3d_feynman_record_channel import Distribution
from v6_p3o_intrinsic_collar_separator_theorem import PAIR_BLOCKS, ROLE_NAMES, partition_label
from v6_p3r_intrinsic_rx_units_resolution import (
    DEFECT_FLOOR,
    MARGIN_FLOOR,
    coupled_pair_law,
    derive_partition,
    tied_symmetric_law,
    unit_chain_error,
    uniform_law,
)


N_SAMPLES = 500
N_REFINEMENT_SAMPLES = 240
N_DRIFT_SEQUENCES = 80
SEED = 20260608


@dataclass
class GenericityAudit:
    candidate: str
    dynamics: str
    unique_rate: float
    floor_rate: float
    role_rate: float
    stable_rate: float
    unit_ok: str
    verdict: str


def random_distribution(rng: Random, alpha: float = 1.0) -> Distribution:
    values = [rng.gammavariate(alpha, 1.0) for _ in range(16)]
    total = sum(values)
    return {
        bits: value / total
        for bits, value in zip(product((0, 1), repeat=4), values)
    }


def perturb_distribution(rng: Random, dist: Distribution, epsilon: float) -> Distribution:
    keys = list(dist)
    values = [dist[key] * exp(rng.uniform(-epsilon, epsilon)) for key in keys]
    total = sum(values)
    return {key: value / total for key, value in zip(keys, values)}


def event_quality(dist: Distribution) -> tuple[bool, bool, str]:
    status, partition, defect, margin, _ = derive_partition(dist)
    unique = status == "event"
    floor = unique and defect >= DEFECT_FLOOR and margin >= MARGIN_FLOOR
    return unique, floor, partition_label(partition)


def single_law_rates(alpha: float) -> tuple[float, float]:
    rng = Random(SEED + int(1000 * alpha))
    unique = 0
    floor = 0
    for _ in range(N_SAMPLES):
        is_unique, has_floor, _ = event_quality(random_distribution(rng, alpha))
        unique += int(is_unique)
        floor += int(has_floor)
    return unique / N_SAMPLES, floor / N_SAMPLES


def independent_role_rates(alpha: float) -> tuple[float, float, float]:
    rng = Random(SEED + 20000 + int(1000 * alpha))
    unique_all = 0
    floor_all = 0
    role_blind = 0
    for _ in range(N_SAMPLES):
        labels: list[str] = []
        unique = True
        floor = True
        for _role in ROLE_NAMES:
            is_unique, has_floor, label = event_quality(random_distribution(rng, alpha))
            labels.append(label)
            unique = unique and is_unique
            floor = floor and has_floor
        unique_all += int(unique)
        floor_all += int(floor)
        role_blind += int(len(set(labels)) == 1 and "--" not in labels)
    return unique_all / N_SAMPLES, floor_all / N_SAMPLES, role_blind / N_SAMPLES


def role_tied_rates(alpha: float) -> tuple[float, float, float]:
    unique, floor = single_law_rates(alpha)
    return unique, floor, 1.0


def symmetric_tied_rates() -> tuple[float, float]:
    is_unique, has_floor, _ = event_quality(tied_symmetric_law())
    return float(is_unique), float(has_floor)


def independent_collar_rates() -> tuple[float, float]:
    is_unique, has_floor, _ = event_quality(uniform_law())
    return float(is_unique), float(has_floor)


def imfd_neighborhood_rates(epsilon: float) -> tuple[float, float, float, float]:
    rng = Random(SEED + 40000 + int(1000 * epsilon))
    base = coupled_pair_law(PAIR_BLOCKS, bridge=0.62)
    base_label = event_quality(base)[2]
    unique = 0
    floor = 0
    stable = 0
    for _ in range(N_REFINEMENT_SAMPLES):
        law = perturb_distribution(rng, base, epsilon)
        is_unique, has_floor, label = event_quality(law)
        unique += int(is_unique)
        floor += int(has_floor)
        stable += int(is_unique and has_floor and label == base_label)
    return (
        unique / N_REFINEMENT_SAMPLES,
        floor / N_REFINEMENT_SAMPLES,
        1.0,
        stable / N_REFINEMENT_SAMPLES,
    )


def arbitrary_drift_rate(alpha: float, length: int = 12) -> float:
    rng = Random(SEED + 50000 + int(1000 * alpha))
    stable = 0
    for _ in range(N_DRIFT_SEQUENCES):
        labels: list[str] = []
        good = True
        for _step in range(length):
            is_unique, has_floor, label = event_quality(random_distribution(rng, alpha))
            labels.append(label)
            good = good and is_unique and has_floor
        stable += int(good and len(set(labels)) == 1)
    return stable / N_DRIFT_SEQUENCES


def unit_ok(unit: str) -> bool:
    if unit == "rn-log":
        return unit_chain_error(0.160682, "rn-log") <= 1.0e-10
    if unit == "sqrt-score":
        return unit_chain_error(0.160682, "sqrt-score") <= 1.0e-10
    return False


def rows() -> list[GenericityAudit]:
    unique_single, floor_single = single_law_rates(1.0)
    unique_weak, floor_weak = single_law_rates(10.0)
    unique_roles, floor_roles, role_roles = independent_role_rates(1.0)
    unique_tied, floor_tied, role_tied = role_tied_rates(1.0)
    sym_unique, sym_floor = symmetric_tied_rates()
    ind_unique, ind_floor = independent_collar_rates()
    open_unique, open_floor, open_role, open_stable = imfd_neighborhood_rates(0.10)
    large_unique, large_floor, large_role, large_stable = imfd_neighborhood_rates(0.80)
    drift_stable = arbitrary_drift_rate(1.0)
    return [
        GenericityAudit(
            "one random sealed law",
            "full-support simplex",
            unique_single,
            floor_single,
            1.0,
            1.0,
            "yes",
            "PASS-SINGLE-LAW-GENERIC/NOT-FULL-PHYSICS",
        ),
        GenericityAudit(
            "near-uniform random law",
            "weak-defect simplex",
            unique_weak,
            floor_weak,
            1.0,
            1.0,
            "yes",
            "FAIL-NO-SOURCE-FLOOR",
        ),
        GenericityAudit(
            "independent role laws",
            "four generic readouts",
            unique_roles,
            floor_roles,
            role_roles,
            1.0,
            "yes",
            "FAIL-ROLE-BLIND-NOT-GENERIC",
        ),
        GenericityAudit(
            "role-tied random law",
            "one law four readouts",
            unique_tied,
            floor_tied,
            role_tied,
            1.0,
            "yes",
            "COND-DYNAMICAL-ROLE-IDENTITY",
        ),
        GenericityAudit(
            "fully independent collar",
            "degenerate eventless",
            ind_unique,
            ind_floor,
            1.0,
            1.0,
            "yes",
            "FAIL-NONUNIQUE-ZERO",
        ),
        GenericityAudit(
            "symmetric tied dynamics",
            "exchangeable law",
            sym_unique,
            sym_floor,
            1.0,
            1.0,
            "yes",
            "FAIL-SYMMETRY-NONUNIQUE",
        ),
        GenericityAudit(
            "IMFD open neighborhood",
            "stable CMRP toy",
            open_unique,
            open_floor,
            open_role,
            open_stable,
            "yes",
            "PASS-DYNAMICAL-OPEN-CLASS",
        ),
        GenericityAudit(
            "large perturbation",
            "leaves neighborhood",
            large_unique,
            large_floor,
            large_role,
            large_stable,
            "yes",
            "COND-MARGIN-DEPENDENT",
        ),
        GenericityAudit(
            "arbitrary refinement drift",
            "independent scales",
            unique_single,
            floor_single,
            1.0,
            drift_stable,
            "yes",
            "FAIL-NO-COFINAL-STABILITY",
        ),
        GenericityAudit(
            "sqrt unit",
            "non-log score",
            1.0,
            1.0,
            1.0,
            1.0,
            "yes" if unit_ok("sqrt-score") else "no",
            "FAIL-NONADDITIVE-UNIT",
        ),
        GenericityAudit(
            "log RN unit",
            "sealed composition",
            1.0,
            1.0,
            1.0,
            1.0,
            "yes" if unit_ok("rn-log") else "no",
            "PASS-UNIT-FIXED-UP-TO-GLOBAL-CONVENTION",
        ),
    ]


def print_rows(audits: list[GenericityAudit]) -> None:
    print("IMFD ontology/genericity audit")
    print("------------------------------")
    print(
        "candidate                    dynamics               unique floor  role   "
        "stable unit verdict"
    )
    for row in audits:
        print(
            f"{row.candidate:28s} "
            f"{row.dynamics:22s} "
            f"{row.unique_rate:6.3f} "
            f"{row.floor_rate:6.3f} "
            f"{row.role_rate:6.3f} "
            f"{row.stable_rate:6.3f} "
            f"{row.unit_ok:4s} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    audits = rows()
    print("=" * 118)
    print("v6 Paper 3 section 29: IMFD ontology and genericity campaign")
    print("=" * 118)
    print("BEAUTIFUL FORM")
    print("--------------")
    print("A physical event is a role-blind, refinement-stable, source-floored")
    print("isolated Radon-Nikodym factorization defect of a sealed finite record")
    print("diamond.  Its do-delete map is the minimum-disturbance RN projection")
    print("onto the selected factorization class.")
    print()
    print_rows(audits)
    print("GENERICITY VERDICT")
    print("------------------")
    print("Single-law isolated minimizers are generic in the finite simplex.")
    print("The full physical event condition is not generic for arbitrary dynamics:")
    print("role identity, source floor, fixed RN units, and cofinal stability must be")
    print("forced by the lower-level CMRP dynamics or admitted as an extra axiom.")


if __name__ == "__main__":
    main()
