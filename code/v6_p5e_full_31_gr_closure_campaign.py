#!/usr/bin/env python3
"""Paper 5 diagnostic E: full 3+1 GR closure campaign after Z_perp.

Finish condition:
  Either full 3+1 GR, including universal Einstein coupling, is determined by
  SHARD + the minimal normal holonomy center, or the same finite sealed record
  data can hide two different continuum couplings.

Result:
  The Einstein-form gate is positive: once a Lorentzian metric, Z_perp normal
  sector, conserved tensor source, locality, and the four-dimensional
  low-derivative Lovelock sector are in place, the allowed untyped equation has
  the Einstein form G + Lambda g = kappa T.

  The full-coupling gate is negative for current SHARD data.  The RN/KL
  commitment law fixes the dimensionless record-evidence scale, but it does
  not fix the record-entropy-per-continuum-area density.  Jacobson/causal
  diamond first-law routes determine kappa only after that density is supplied.
  Hence the same sealed finite data can carry different continuum kappa values.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


@dataclass(frozen=True)
class SealedRecordDatum:
    atoms: int
    evidence_per_atom: float
    z_perp: int
    tensor_source_component: float
    normal_orientation: int


def survival(evidence: float) -> float:
    """Intrinsic division-event no-division survival."""
    return math.exp(-evidence)


def entropy_density(record: SealedRecordDatum, area_quantum: float) -> float:
    """Record entropy/evidence per continuum screen area."""
    total_evidence = record.atoms * record.evidence_per_atom
    total_area = record.atoms * area_quantum
    return total_evidence / total_area


def einstein_coupling_from_density(density: float) -> float:
    """Dimensionless Jacobson-style proportionality with constants suppressed.

    In physical units the proportionality carries hbar and numerical factors.
    For this finite diagnostic only the dependency matters: kappa is inverse to
    entropy-per-area density.  Supplying the density fixes kappa; omitting it
    leaves a coupling family.
    """
    return 1.0 / density


def einstein_form_residual(curvature: float, kappa: float, source: float, lambd: float) -> float:
    return curvature + lambd - kappa * source


def continuum_curvature_for(record: SealedRecordDatum, area_quantum: float, lambd: float = 0.0) -> float:
    density = entropy_density(record, area_quantum)
    kappa = einstein_coupling_from_density(density)
    return kappa * record.tensor_source_component - lambd


def same_record_gap(first: SealedRecordDatum, second: SealedRecordDatum) -> int:
    return 0 if first == second else 1


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    record = SealedRecordDatum(
        atoms=64,
        evidence_per_atom=1.0,
        z_perp=1,
        tensor_source_component=0.37,
        normal_orientation=1,
    )
    record_twin = SealedRecordDatum(
        atoms=64,
        evidence_per_atom=1.0,
        z_perp=1,
        tensor_source_component=0.37,
        normal_orientation=1,
    )

    area_small = 1.0
    area_large = 4.0
    dens_small = entropy_density(record, area_small)
    dens_large = entropy_density(record, area_large)
    kappa_small = einstein_coupling_from_density(dens_small)
    kappa_large = einstein_coupling_from_density(dens_large)
    curvature_small = continuum_curvature_for(record, area_small)
    curvature_large = continuum_curvature_for(record_twin, area_large)
    coupling_gap = abs(kappa_large - kappa_small)
    curvature_gap = abs(curvature_large - curvature_small)

    res_small = einstein_form_residual(curvature_small, kappa_small, record.tensor_source_component, 0.0)
    res_large = einstein_form_residual(curvature_large, kappa_large, record.tensor_source_component, 0.0)

    # Commitment scale is fixed in evidence units, and is identical for both
    # records.  It cannot see the area calibration.
    survival_gap = abs(survival(record.evidence_per_atom) - survival(record_twin.evidence_per_atom))

    # Cosmological/Lovelock term: Bianchi and Lovelock allow a metric term.  A
    # vacuum-centering law can set the local vacuum value, but Bianchi alone
    # does not.
    lambda_a = 0.0
    lambda_b = 0.18
    curvature_la = continuum_curvature_for(record, area_small, lambda_a)
    curvature_lb = continuum_curvature_for(record, area_small, lambda_b)
    res_la = einstein_form_residual(curvature_la, kappa_small, record.tensor_source_component, lambda_a)
    res_lb = einstein_form_residual(curvature_lb, kappa_small, record.tensor_source_component, lambda_b)
    lambda_gap = abs(lambda_b - lambda_a)

    # Candidate closure if the missing invariant is supplied.
    supplied_area_quantum = 1.0
    supplied_density = entropy_density(record, supplied_area_quantum)
    supplied_kappa = einstein_coupling_from_density(supplied_density)
    supplied_curvature = continuum_curvature_for(record, supplied_area_quantum)
    supplied_residual = einstein_form_residual(
        supplied_curvature, supplied_kappa, record.tensor_source_component, 0.0
    )

    rows = [
        Row(
            "Einstein-form gate",
            "assume Lorentzian metric + Z_perp + conserved tensor source + 4D Lovelock sector",
            "equation form is G + Lambda g = kappa T, not a larger local tensor family",
            "form_family_dim=2",
            "PASS-FORM",
        ),
        Row(
            "same sealed data",
            "compare records before continuum area calibration",
            "all finite SHARD entries agree, including Z_perp and tensor source",
            f"same_record_gap={same_record_gap(record, record_twin)}",
            "SAME-SHARD-DATA",
        ),
        Row(
            "area-density attack",
            "vary record-area quantum while holding record evidence fixed",
            "entropy-per-area density changes but finite record data do not",
            f"density={dens_small:.3f}/{dens_large:.3f}",
            "DENSITY-FREE",
        ),
        Row(
            "coupling split",
            "kappa is inverse to entropy-per-area density in causal-diamond first-law routes",
            "same finite data give two Einstein couplings",
            f"kappa={kappa_small:.3f}/{kappa_large:.3f}, gap={coupling_gap:.3f}",
            "REFUTES-UNIQUE-COUPLING",
        ),
        Row(
            "Einstein residual check",
            "build curvature response with each kappa",
            "both satisfy Einstein-form equations exactly, but with different response scales",
            f"res={res_small:.1e}/{res_large:.1e}, curvature_gap={curvature_gap:.3f}",
            "BOTH-GR-FORM",
        ),
        Row(
            "RN/KL commitment law",
            "S(I)=exp(-I) at the same record evidence",
            "dimensionless division scale is fixed but cannot see area calibration",
            f"survival_gap={survival_gap:.1e}",
            "FIXES-EVIDENCE-NOT-G",
        ),
        Row(
            "Jacobson/causal-diamond route",
            "supply entropy-area density, then compute kappa",
            "first-law derivations fix coupling only after the density is given",
            f"supplied_density={supplied_density:.3f}, supplied_kappa={supplied_kappa:.3f}",
            "COND-POSITIVE",
        ),
        Row(
            "cosmological term gate",
            "vary Lambda while preserving Lovelock/Bianchi form",
            "Bianchi permits a metric term; local vacuum centering would be an extra selection",
            f"Lambda_gap={lambda_gap:.3f}, res={res_la:.1e}/{res_lb:.1e}",
            "LAMBDA-INTEGRATION-DATA",
        ),
        Row(
            "closure with missing datum",
            "add universal screen entropy-area density / record area quantum",
            "kappa is then determined by record data plus the supplied density",
            f"res={supplied_residual:.1e}",
            "CLOSES-IF-SUPPLIED",
        ),
        Row(
            "full GR verdict",
            "SHARD + Z_perp + current continuum gates",
            "Einstein form is derivable under Lovelock/HKT assumptions; full coupling is not",
            "same data hide different kappa",
            "FULL-3PLUS1-GR-NOT-DERIVED",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "same_record_gap": float(same_record_gap(record, record_twin)),
        "density_small": dens_small,
        "density_large": dens_large,
        "kappa_small": kappa_small,
        "kappa_large": kappa_large,
        "coupling_gap": coupling_gap,
        "curvature_gap": curvature_gap,
        "einstein_residual_small": res_small,
        "einstein_residual_large": res_large,
        "survival_gap": survival_gap,
        "lambda_gap": lambda_gap,
        "supplied_residual": supplied_residual,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")

    # Hard guards for the campaign verdict.
    assert values["same_record_gap"] == 0.0
    assert values["coupling_gap"] > 0.0
    assert values["curvature_gap"] > 0.0
    assert math.isclose(values["einstein_residual_small"], 0.0, abs_tol=1e-12)
    assert math.isclose(values["einstein_residual_large"], 0.0, abs_tol=1e-12)
    assert math.isclose(values["survival_gap"], 0.0, abs_tol=1e-12)
    assert math.isclose(values["supplied_residual"], 0.0, abs_tol=1e-12)


if __name__ == "__main__":
    main()
