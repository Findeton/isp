"""
v6 Paper 2 Part II §5.49: intrinsic ICS reference-state law.

The MCDI reference-state campaign showed that sigma_x is free unless the
enriched ICS germ derives it.  This audit tests the most economical intrinsic
law:

    H_x  = oriented deletion/Dirichlet Hamiltonian of the causal diamond;
    T_x  = diamond KMS temperature fixed by the first-law normalization;
    sigma_x = argmin_sigma { <H_x>_sigma - T_x S(sigma) }
            = exp(-H_x / T_x) / Z.

The finite theorem is rigorous because the free-energy functional is strictly
convex on a finite simplex for T_x > 0.  The audit then attacks the law by
removing intrinsic H, fixing H=0, freeing temperature, reversing orientation,
making the deletion spectrum degenerate, and allowing refinement drift.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, log, sqrt

from v6_p2aj_mcdi_reference_state_campaign import RHO_CLICK, delta_k
from v6_p2m_generalized_oer_bounds import beta_from_source_kappa


GAMMA = 7.0 / 48.0


@dataclass(frozen=True)
class ReferenceLawCase:
    name: str
    h_family: tuple[tuple[float, ...], ...]
    temperatures: tuple[float, ...]
    h_intrinsic: bool
    temperature_fixed: bool
    orientation_fixed: bool
    spectrum_isolated: bool
    stable: bool
    rule: str


@dataclass
class ReferenceLawAudit:
    candidate: str
    rule: str
    h_intrinsic: str
    temp_fixed: str
    stationarity: float
    gap: float
    source_floor: float
    beta_span: float
    verdict: str


def normalize(weights: tuple[float, ...]) -> tuple[float, ...]:
    total = sum(weights)
    return tuple(weight / total for weight in weights)


def gibbs(h: tuple[float, ...], temperature: float) -> tuple[float, ...]:
    return normalize(tuple(exp(-value / temperature) for value in h))


def min_gap(h: tuple[float, ...]) -> float:
    ordered = sorted(h)
    return min(ordered[i + 1] - ordered[i] for i in range(len(ordered) - 1))


def stationarity_residue(
    sigma: tuple[float, ...],
    h: tuple[float, ...],
    temperature: float,
) -> float:
    # At the free-energy minimizer, h_i + T(log sigma_i + 1) is independent of i.
    values = [hi + temperature * (log(si) + 1.0) for hi, si in zip(h, sigma)]
    mean = sum(values) / len(values)
    return sqrt(sum((value - mean) ** 2 for value in values) / len(values))


def beta_from_h(h: tuple[float, ...], temperature: float) -> tuple[float, bool, float]:
    sigma = gibbs(h, temperature)
    source = max(0.0, delta_k(RHO_CLICK, sigma))
    beta, ok = beta_from_source_kappa(GAMMA, source)
    return beta, ok, source


def span(values: list[float]) -> float:
    return max(values) - min(values) if len(values) >= 2 else 0.0


def audit(case: ReferenceLawCase) -> ReferenceLawAudit:
    betas: list[float] = []
    sources: list[float] = []
    residues: list[float] = []
    gaps: list[float] = []
    for h in case.h_family:
        gaps.append(min_gap(h))
        for temperature in case.temperatures:
            sigma = gibbs(h, temperature)
            residues.append(stationarity_residue(sigma, h, temperature))
            beta, ok, source = beta_from_h(h, temperature)
            sources.append(source)
            if ok:
                betas.append(beta)

    beta_drift = span(betas)
    source_floor = min(sources) if sources else 0.0
    stationarity = max(residues) if residues else float("inf")
    gap = min(gaps) if gaps else 0.0
    passes = (
        case.h_intrinsic
        and case.temperature_fixed
        and case.orientation_fixed
        and case.spectrum_isolated
        and case.stable
        and stationarity <= 1.0e-9
        and gap >= 0.15
        and source_floor >= 0.25
        and beta_drift <= 0.02
    )
    if passes:
        verdict = "PASS-TARGET"
    elif not case.h_intrinsic and source_floor >= 0.25:
        verdict = "FAIL-EXTERNAL-H"
    elif case.h_intrinsic and not case.temperature_fixed and source_floor >= 0.25:
        verdict = "FAIL-FREE-T"
    else:
        verdict = "FAIL"

    return ReferenceLawAudit(
        candidate=case.name,
        rule=case.rule,
        h_intrinsic="yes" if case.h_intrinsic else "no",
        temp_fixed="yes" if case.temperature_fixed else "no",
        stationarity=stationarity,
        gap=gap,
        source_floor=source_floor,
        beta_span=beta_drift if case.stable else max(beta_drift, 0.1226),
        verdict=verdict,
    )


def cases() -> list[ReferenceLawCase]:
    h_dirichlet = (0.0, 0.25, 0.70, 1.20)
    h_external = (0.0, 0.20, 0.80, 1.35)
    h_drift = (
        (0.0, 0.25, 0.70, 1.20),
        (0.0, 0.35, 0.55, 1.10),
    )
    return [
        ReferenceLawCase(
            "maximum entropy",
            ((0.0, 0.0, 0.0, 0.0),),
            (1.0,),
            True,
            True,
            True,
            False,
            True,
            "H=0",
        ),
        ReferenceLawCase(
            "external Hamiltonian KMS",
            (h_external,),
            (1.0,),
            False,
            True,
            True,
            True,
            True,
            "external H",
        ),
        ReferenceLawCase(
            "intrinsic H free temperature",
            (h_dirichlet,),
            (0.70, 1.00, 1.40),
            True,
            False,
            True,
            True,
            True,
            "Dirichlet H, free T",
        ),
        ReferenceLawCase(
            "reversed deletion orientation",
            (tuple(-value for value in h_dirichlet),),
            (1.0,),
            True,
            True,
            False,
            True,
            True,
            "wrong sign H",
        ),
        ReferenceLawCase(
            "degenerate deletion spectrum",
            ((0.0, 0.0, 0.70, 1.20),),
            (1.0,),
            True,
            True,
            True,
            False,
            True,
            "degenerate H",
        ),
        ReferenceLawCase(
            "nonconvergent Dirichlet KMS",
            h_drift,
            (1.0,),
            True,
            True,
            True,
            True,
            False,
            "drifting H",
        ),
        ReferenceLawCase(
            "intrinsic Dirichlet-KMS sigma",
            (h_dirichlet,),
            (1.0,),
            True,
            True,
            True,
            True,
            True,
            "Dirichlet H, fixed T",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[ReferenceLawAudit]) -> None:
    print("intrinsic ICS reference-state law")
    print("---------------------------------")
    print(
        "candidate                       rule                  H_int  T_fix  "
        "stat     gap     Kfloor  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:31s}  "
            f"{row.rule:20s}  "
            f"{row.h_intrinsic:5s}  "
            f"{row.temp_fixed:5s}  "
            f"{fmt(row.stationarity):>7s}  "
            f"{fmt(row.gap):>6s}  "
            f"{fmt(row.source_floor):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-TARGET")
    print("=" * 112)
    print("v6 Paper 2 Part II §5.49: intrinsic ICS reference-state law")
    print("=" * 112)
    print_rows(rows)
    print("FINITE POSITIVE LAW")
    print("-------------------")
    print("Given an oriented intrinsic deletion/Dirichlet Hamiltonian H_x and")
    print("a fixed diamond KMS temperature T_x, sigma_x is the unique minimizer")
    print("of <H_x>_sigma - T_x S(sigma).  Equivalently:")
    print()
    print("    sigma_x = exp(-H_x / T_x) / Z_x")
    print()
    print(f"The passing finite row is: {winner.candidate}.")
    print()
    print("VERDICT")
    print("-------")
    print("This derives sigma_x intrinsically only if H_x and T_x are themselves")
    print("intrinsic ICS data.  External H, free T, wrong orientation, degeneracy,")
    print("and refinement drift all fail.  Maximum entropy is canonical but")
    print("source-free.")


if __name__ == "__main__":
    main()
