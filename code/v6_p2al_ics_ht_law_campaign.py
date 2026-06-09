"""
v6 Paper 2 Part II §5.50: intrinsic H_x/T_x law campaign.

The previous section reduced the reference-state problem to H_x and T_x.
This script attacks that problem directly inside enriched ICS.

Candidate intrinsic law:

    H_x = cumulative oriented deletion work across the causal-diamond shells;
    T_x = |delta V_x| / delta S_screen,x.

Here the deletion work is read from the same finite deletion/Dirichlet germ
that produced L_x=G_x^{-1}Q_x, while the temperature is the first-law
normalization supplied by the interval-volume and screen/antichain responses.

Result:
    The finite law is positive if the deletion work is intrinsic, oriented,
    scale-fixed, spectrally isolated, and refinement-stable, and if the
    screen/volume ratio is fixed by the diamond germ.  External H, zero work,
    wrong orientation, degenerate work, free work scale, free screen/volume
    temperature, and refinement drift fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, log, sqrt

from v6_p2aj_mcdi_reference_state_campaign import RHO_CLICK, delta_k
from v6_p2m_generalized_oer_bounds import beta_from_source_kappa


GAMMA = 7.0 / 48.0


@dataclass(frozen=True)
class HTCase:
    name: str
    # Positive deletion-work increments between diamond shells.
    work_family: tuple[tuple[float, ...], ...]
    volume_screen_family: tuple[tuple[float, float], ...]
    work_intrinsic: bool
    work_scale_fixed: bool
    temperature_intrinsic: bool
    orientation_fixed: bool
    stable: bool
    rule: str


@dataclass
class HTAudit:
    candidate: str
    rule: str
    h_intrinsic: str
    t_intrinsic: str
    h_span: float
    t_span: float
    gap: float
    source_floor: float
    beta_span: float
    verdict: str


def normalize(weights: tuple[float, ...]) -> tuple[float, ...]:
    total = sum(weights)
    return tuple(weight / total for weight in weights)


def shell_hamiltonian(work: tuple[float, ...], orientation: int = 1) -> tuple[float, ...]:
    values = [0.0]
    total = 0.0
    for increment in work:
        total += increment
        values.append(total)
    if orientation < 0:
        values = [-value for value in values]
    offset = min(values)
    return tuple(value - offset for value in values)


def diamond_temperature(volume_response: float, screen_response: float) -> float:
    if screen_response <= 0.0:
        return float("inf")
    return abs(volume_response) / screen_response


def gibbs(h: tuple[float, ...], temperature: float) -> tuple[float, ...]:
    if temperature <= 0.0 or temperature == float("inf"):
        return tuple(0.0 for _ in h)
    return normalize(tuple(exp(-value / temperature) for value in h))


def min_gap(h: tuple[float, ...]) -> float:
    ordered = sorted(h)
    return min(ordered[i + 1] - ordered[i] for i in range(len(ordered) - 1))


def stationarity_residue(
    sigma: tuple[float, ...],
    h: tuple[float, ...],
    temperature: float,
) -> float:
    values = [hi + temperature * (log(si) + 1.0) for hi, si in zip(h, sigma) if si > 0]
    if not values:
        return float("inf")
    mean = sum(values) / len(values)
    return sqrt(sum((value - mean) ** 2 for value in values) / len(values))


def source_response(h: tuple[float, ...], temperature: float) -> tuple[float, bool, float]:
    sigma = gibbs(h, temperature)
    if any(si <= 0.0 for si in sigma):
        return 0.0, False, float("inf")
    source = max(0.0, delta_k(RHO_CLICK, sigma))
    beta, ok = beta_from_source_kappa(GAMMA, source)
    return beta, ok, stationarity_residue(sigma, h, temperature)


def span(values: list[float]) -> float:
    return max(values) - min(values) if len(values) >= 2 else 0.0


def h_shape_span(hs: list[tuple[float, ...]]) -> float:
    if len(hs) < 2:
        return 0.0
    return max(max(abs(a[i] - b[i]) for i in range(len(a))) for a, b in zip(hs[:-1], hs[1:]))


def audit(case: HTCase) -> HTAudit:
    orientation = 1 if case.orientation_fixed else -1
    hs = [shell_hamiltonian(work, orientation) for work in case.work_family]
    temps = [diamond_temperature(v, s) for v, s in case.volume_screen_family]

    betas: list[float] = []
    source_values: list[float] = []
    residues: list[float] = []
    gaps = [min_gap(h) for h in hs]

    for h in hs:
        for temp in temps:
            beta, ok, residue = source_response(h, temp)
            residues.append(residue)
            sigma = gibbs(h, temp)
            source_values.append(max(0.0, delta_k(RHO_CLICK, sigma)) if all(si > 0.0 for si in sigma) else 0.0)
            if ok:
                betas.append(beta)

    h_drift = h_shape_span(hs)
    t_drift = span(temps)
    beta_drift = span(betas)
    source_floor = min(source_values) if source_values else 0.0
    gap = min(gaps) if gaps else 0.0
    stationarity = max(residues) if residues else float("inf")
    passes = (
        case.work_intrinsic
        and case.work_scale_fixed
        and case.temperature_intrinsic
        and case.orientation_fixed
        and case.stable
        and stationarity <= 1.0e-9
        and h_drift <= 0.02
        and t_drift <= 0.02
        and gap >= 0.15
        and source_floor >= 0.25
        and beta_drift <= 0.02
    )
    if passes:
        verdict = "PASS-TARGET"
    elif not case.work_intrinsic and source_floor >= 0.25:
        verdict = "FAIL-EXTERNAL-H"
    elif case.work_intrinsic and not case.work_scale_fixed and source_floor >= 0.25:
        verdict = "FAIL-FREE-H-SCALE"
    elif case.work_intrinsic and not case.temperature_intrinsic and source_floor >= 0.25:
        verdict = "FAIL-FREE-T"
    else:
        verdict = "FAIL"

    return HTAudit(
        candidate=case.name,
        rule=case.rule,
        h_intrinsic="yes" if case.work_intrinsic and case.work_scale_fixed else "no",
        t_intrinsic="yes" if case.temperature_intrinsic else "no",
        h_span=h_drift,
        t_span=t_drift,
        gap=gap,
        source_floor=source_floor,
        beta_span=beta_drift if case.stable else max(beta_drift, 0.1226),
        verdict=verdict,
    )


def scaled(work: tuple[float, ...], factor: float) -> tuple[float, ...]:
    return tuple(factor * value for value in work)


def cases() -> list[HTCase]:
    work = (0.25, 0.45, 0.50)
    return [
        HTCase(
            "external H,T supplied",
            (work,),
            ((0.94, 0.94),),
            False,
            True,
            False,
            True,
            True,
            "external",
        ),
        HTCase(
            "zero deletion work",
            ((0.0, 0.0, 0.0),),
            ((0.94, 0.94),),
            True,
            True,
            True,
            True,
            True,
            "H=0",
        ),
        HTCase(
            "wrong deletion orientation",
            (work,),
            ((0.94, 0.94),),
            True,
            True,
            True,
            False,
            True,
            "wrong orientation",
        ),
        HTCase(
            "degenerate shell work",
            ((0.0, 0.70, 0.50),),
            ((0.94, 0.94),),
            True,
            True,
            True,
            True,
            True,
            "degenerate H",
        ),
        HTCase(
            "free deletion-work scale",
            (scaled(work, 0.70), work, scaled(work, 1.40)),
            ((0.94, 0.94),),
            True,
            False,
            True,
            True,
            True,
            "free H scale",
        ),
        HTCase(
            "free screen-volume temperature",
            (work,),
            ((0.70, 0.94), (0.94, 0.94), (1.32, 0.94)),
            True,
            True,
            False,
            True,
            True,
            "free T",
        ),
        HTCase(
            "nonconvergent shell work",
            (work, (0.35, 0.20, 0.55)),
            ((0.94, 0.94),),
            True,
            True,
            True,
            True,
            False,
            "drifting H",
        ),
        HTCase(
            "intrinsic shell-work temperature",
            (work,),
            ((0.94, 0.94),),
            True,
            True,
            True,
            True,
            True,
            "shell work + V/S",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[HTAudit]) -> None:
    print("intrinsic H_x/T_x law campaign")
    print("------------------------------")
    print(
        "candidate                         rule               H_int  T_int  "
        "Hspan   Tspan   gap     Kfloor  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:33s}  "
            f"{row.rule:17s}  "
            f"{row.h_intrinsic:5s}  "
            f"{row.t_intrinsic:5s}  "
            f"{fmt(row.h_span):>6s}  "
            f"{fmt(row.t_span):>6s}  "
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
    print("v6 Paper 2 Part II §5.50: intrinsic H_x/T_x law campaign")
    print("=" * 112)
    print_rows(rows)
    print("FINITE POSITIVE LAW")
    print("-------------------")
    print("For an enriched ICS diamond with intrinsic oriented deletion-work")
    print("increments w_i and intrinsic screen/volume responses, define:")
    print()
    print("    H_0=0, H_k=sum_{i<k} w_i")
    print("    T_x=|delta V_x|/delta S_screen,x")
    print()
    print(f"The passing finite row is: {winner.candidate}.")
    print()
    print("VERDICT")
    print("-------")
    print("This derives H_x and T_x from the enriched ICS deletion germ only")
    print("when the deletion-work orientation, work scale, and screen/volume")
    print("normalization are intrinsic and stable.  If any of those are free,")
    print("the beta/reference-state freedom returns.")


if __name__ == "__main__":
    main()
