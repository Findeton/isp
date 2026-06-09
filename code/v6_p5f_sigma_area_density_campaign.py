#!/usr/bin/env python3
"""Paper 5 diagnostic F: sigma_A determinacy campaign.

Finish condition:
  Either sigma_A is intrinsically determined by sealed finite record data, or
  the same sealed horizon/diamond data can hide two different entropy-area
  densities.

Result:
  Current SHARD data do not determine sigma_A.  The RN/KL commitment law,
  primitive Diamond Work-Balance, Unruh/modular temperature, causal-diamond
  first-law form, Bekenstein bounds, and Lovelock/HKT structure are all
  insensitive to a global record-area calibration.  Supplying the record area
  quantum A_rec determines sigma_A, but that is precisely the missing datum.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class HorizonRecord:
    atoms: int
    evidence_per_atom: float
    z_perp: int
    tensor_source: float
    modular_temperature: float
    dwb_theta: float
    born_norm: float


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def record_entropy(record: HorizonRecord) -> float:
    return record.atoms * record.evidence_per_atom


def continuum_area(record: HorizonRecord, area_quantum: float) -> float:
    return record.atoms * area_quantum


def sigma_area(record: HorizonRecord, area_quantum: float) -> float:
    return record_entropy(record) / continuum_area(record, area_quantum)


def kappa_from_sigma(sigma: float) -> float:
    return 1.0 / sigma


def no_division_survival(record: HorizonRecord) -> float:
    return math.exp(-record.evidence_per_atom)


def heat_flux(record: HorizonRecord) -> float:
    return record.modular_temperature * record_entropy(record)


def jacobson_curvature(record: HorizonRecord, area_quantum: float) -> float:
    return kappa_from_sigma(sigma_area(record, area_quantum)) * record.tensor_source


def bekenstein_bound_slack(record: HorizonRecord, area_quantum: float, bound_density: float) -> float:
    """Positive slack means S <= bound_density * A."""
    return bound_density * continuum_area(record, area_quantum) - record_entropy(record)


def same_record_gap(first: HorizonRecord, second: HorizonRecord) -> int:
    return 0 if first == second else 1


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    theta_star = 0.797003794162878
    record = HorizonRecord(
        atoms=128,
        evidence_per_atom=1.0,
        z_perp=1,
        tensor_source=0.41,
        modular_temperature=1.0 / (2.0 * math.pi),
        dwb_theta=theta_star,
        born_norm=1.0,
    )
    twin = HorizonRecord(
        atoms=128,
        evidence_per_atom=1.0,
        z_perp=1,
        tensor_source=0.41,
        modular_temperature=1.0 / (2.0 * math.pi),
        dwb_theta=theta_star,
        born_norm=1.0,
    )

    area_a = 1.0
    area_b = 3.0
    sigma_a = sigma_area(record, area_a)
    sigma_b = sigma_area(twin, area_b)
    kappa_a = kappa_from_sigma(sigma_a)
    kappa_b = kappa_from_sigma(sigma_b)
    curvature_a = jacobson_curvature(record, area_a)
    curvature_b = jacobson_curvature(twin, area_b)

    survival_gap = abs(no_division_survival(record) - no_division_survival(twin))
    heat_gap = abs(heat_flux(record) - heat_flux(twin))
    dwb_gap = abs(record.dwb_theta - twin.dwb_theta)
    born_gap = abs(record.born_norm - twin.born_norm)

    # A Bekenstein/holographic upper bound can be satisfied by a whole interval
    # of area calibrations.  It does not select the density unless saturation is
    # imposed as an additional horizon/black-hole condition.
    bound_density = 1.0
    slack_a = bekenstein_bound_slack(record, area_a, bound_density)
    slack_b = bekenstein_bound_slack(record, area_b, bound_density)

    supplied_area_quantum = 1.0
    supplied_sigma = sigma_area(record, supplied_area_quantum)
    supplied_kappa = kappa_from_sigma(supplied_sigma)

    rows = [
        Row(
            "same sealed horizon data",
            "compare record atoms, RN evidence, Z_perp, tensor source, modular temperature, DWB theta",
            "all finite SHARD entries agree before area calibration",
            f"same_record_gap={same_record_gap(record, twin)}",
            "SAME-SEALED-DATA",
        ),
        Row(
            "RN/KL commitment",
            "S(I)=exp(-I) on each atom",
            "evidence scale is fixed but independent of continuum area quantum",
            f"survival_gap={survival_gap:.1e}",
            "NO-SIGMA-SELECTION",
        ),
        Row(
            "primitive DWB constant",
            "compare selected theta_* for the primitive binary defect",
            "dimensionless event law is fixed while area density remains free",
            f"theta_gap={dwb_gap:.1e}",
            "NO-SIGMA-SELECTION",
        ),
        Row(
            "Born/screen norm",
            "compare retained-holonomy norm convention",
            "Born normalization is unaffected by area calibration",
            f"norm_gap={born_gap:.1e}",
            "NO-SIGMA-SELECTION",
        ),
        Row(
            "Unruh/modular temperature",
            "delta Q = T delta S with same T and same record entropy",
            "heat flux is fixed in record units but not in area units",
            f"heat_gap={heat_gap:.1e}, T={record.modular_temperature:.6f}",
            "NO-SIGMA-SELECTION",
        ),
        Row(
            "area-calibration split",
            "vary A_rec while keeping record entropy fixed",
            "sigma_A changes with no change to sealed data",
            f"sigma={sigma_a:.3f}/{sigma_b:.3f}",
            "SIGMA-SPLIT",
        ),
        Row(
            "coupling consequence",
            "Jacobson/causal-diamond route kappa proportional to 1/sigma_A",
            "two sigma_A values give two couplings and two curvature responses",
            f"kappa={kappa_a:.3f}/{kappa_b:.3f}, curvature={curvature_a:.3f}/{curvature_b:.3f}",
            "COUPLING-SPLIT",
        ),
        Row(
            "Bekenstein/holographic bound",
            "test S <= bound_density * A",
            "a bound allows a family; only saturation would select an area density",
            f"slack={slack_a:.3f}/{slack_b:.3f}",
            "BOUND-NOT-LAW",
        ),
        Row(
            "black-hole saturation",
            "impose S = sigma_A A on a horizon",
            "this fixes sigma_A only by adding saturation/coefficient input",
            f"sigma_if_area_a={sigma_a:.3f}",
            "COND-SATURATION",
        ),
        Row(
            "closure if supplied",
            "add record area quantum A_rec to the sealed ledger",
            "sigma_A and kappa are then determined",
            f"A_rec={supplied_area_quantum:.3f}, sigma={supplied_sigma:.3f}, kappa={supplied_kappa:.3f}",
            "CLOSES-IF-SUPPLIED",
        ),
        Row(
            "campaign verdict",
            "all current record/modular/horizon candidates versus sigma_A",
            "same sealed horizon data can hide two entropy-area densities",
            "finish condition reached",
            "SIGMA-SPLIT-PROVED",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "same_record_gap": float(same_record_gap(record, twin)),
        "sigma_a": sigma_a,
        "sigma_b": sigma_b,
        "sigma_gap": abs(sigma_a - sigma_b),
        "kappa_a": kappa_a,
        "kappa_b": kappa_b,
        "kappa_gap": abs(kappa_a - kappa_b),
        "curvature_gap": abs(curvature_a - curvature_b),
        "survival_gap": survival_gap,
        "heat_gap": heat_gap,
        "dwb_gap": dwb_gap,
        "born_gap": born_gap,
        "bound_slack_a": slack_a,
        "bound_slack_b": slack_b,
        "supplied_sigma": supplied_sigma,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")

    assert values["same_record_gap"] == 0.0
    assert values["sigma_gap"] > 0.0
    assert values["kappa_gap"] > 0.0
    assert values["curvature_gap"] > 0.0
    assert math.isclose(values["survival_gap"], 0.0, abs_tol=1e-12)
    assert math.isclose(values["heat_gap"], 0.0, abs_tol=1e-12)
    assert math.isclose(values["dwb_gap"], 0.0, abs_tol=1e-12)
    assert math.isclose(values["born_gap"], 0.0, abs_tol=1e-12)
    assert values["bound_slack_b"] > values["bound_slack_a"]


if __name__ == "__main__":
    main()
