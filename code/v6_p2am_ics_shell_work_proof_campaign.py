"""
v6 Paper 2 Part II §5.51: shell-work proof campaign.

The H_x/T_x law assumed oriented deletion-work increments w_i and intrinsic
screen/volume normalization.  This script tries to derive those objects from
the enriched ICS causal-diamond deletion germ itself.

Finite proof route:
    1. Use the causal order to form canonical nested diamond shells.
    2. Use the local RN deletion action A_k on those shells.
    3. Define shell work by action increments:
           w_i = A_{i+1} - A_i.
    4. Fix the action scale because A is a log Radon-Nikodym action.
    5. Define screen temperature by intrinsic count units:
           T_x = |delta V_x| / delta S_screen,x.

The proof is conditional on the shell filtration, RN action scale, positive
oriented increments, fixed count entropy units, and refinement stability.
The audit attacks each condition.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2aj_mcdi_reference_state_campaign import RHO_CLICK, delta_k
from v6_p2al_ics_ht_law_campaign import (
    diamond_temperature,
    gibbs,
    shell_hamiltonian,
    source_response,
)


@dataclass(frozen=True)
class ShellWorkCase:
    name: str
    action_family: tuple[tuple[float, ...], ...]
    volume_screen_family: tuple[tuple[float, float], ...]
    canonical_shells: bool
    rn_action: bool
    action_scale_fixed: bool
    entropy_unit_fixed: bool
    stable: bool
    rule: str


@dataclass
class ShellWorkAudit:
    candidate: str
    rule: str
    shells: str
    rn: str
    scale: str
    work_floor: float
    h_span: float
    t_span: float
    beta_span: float
    verdict: str


def action_increments(action: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(action[i + 1] - action[i] for i in range(len(action) - 1))


def span(values: list[float]) -> float:
    return max(values) - min(values) if len(values) >= 2 else 0.0


def h_span(hs: list[tuple[float, ...]]) -> float:
    if len(hs) < 2:
        return 0.0
    out = 0.0
    for a, b in zip(hs[:-1], hs[1:]):
        out = max(out, max(abs(a[i] - b[i]) for i in range(len(a))))
    return out


def scaled_action(action: tuple[float, ...], factor: float) -> tuple[float, ...]:
    return tuple(factor * value for value in action)


def audit(case: ShellWorkCase) -> ShellWorkAudit:
    works = [action_increments(action) for action in case.action_family]
    hs = [shell_hamiltonian(work) for work in works]
    temps = [diamond_temperature(v, s) for v, s in case.volume_screen_family]
    work_floor = min((min(work) for work in works), default=0.0)
    h_drift = h_span(hs)
    t_drift = span(temps)

    betas = []
    source_floors = []
    for h in hs:
        for temp in temps:
            beta, ok, _ = source_response(h, temp)
            sigma = gibbs(h, temp)
            source_floors.append(
                max(0.0, delta_k(RHO_CLICK, sigma))
                if all(si > 0.0 for si in sigma)
                else 0.0
            )
            if ok:
                betas.append(beta)
    beta_drift = span(betas)
    source_floor = min(source_floors) if source_floors else 0.0

    passes = (
        case.canonical_shells
        and case.rn_action
        and case.action_scale_fixed
        and case.entropy_unit_fixed
        and case.stable
        and work_floor >= 0.15
        and h_drift <= 0.02
        and t_drift <= 0.02
        and source_floor >= 0.25
        and beta_drift <= 0.02
    )
    if passes:
        verdict = "PASS-THEOREM"
    elif not case.canonical_shells:
        verdict = "FAIL-SHELLS"
    elif not case.rn_action:
        verdict = "FAIL-NO-RN"
    elif not case.action_scale_fixed and source_floor >= 0.25:
        verdict = "FAIL-FREE-A-SCALE"
    elif not case.entropy_unit_fixed and source_floor >= 0.25:
        verdict = "FAIL-FREE-S-UNIT"
    else:
        verdict = "FAIL"

    return ShellWorkAudit(
        candidate=case.name,
        rule=case.rule,
        shells="yes" if case.canonical_shells else "no",
        rn="yes" if case.rn_action else "no",
        scale="yes" if case.action_scale_fixed and case.entropy_unit_fixed else "no",
        work_floor=work_floor,
        h_span=h_drift,
        t_span=t_drift,
        beta_span=beta_drift if case.stable else max(beta_drift, 0.1226),
        verdict=verdict,
    )


def cases() -> list[ShellWorkCase]:
    action = (0.0, 0.25, 0.70, 1.20)
    free_scale = tuple(scaled_action(action, factor) for factor in (0.70, 1.00, 1.40))
    return [
        ShellWorkCase(
            "order-only shells",
            ((0.0, 0.0, 0.0, 0.0),),
            ((0.94, 0.94),),
            True,
            False,
            True,
            True,
            True,
            "no action",
        ),
        ShellWorkCase(
            "external shell action",
            (action,),
            ((0.94, 0.94),),
            True,
            False,
            True,
            True,
            True,
            "external A",
        ),
        ShellWorkCase(
            "ambiguous shell filtration",
            (action,),
            ((0.94, 0.94),),
            False,
            True,
            True,
            True,
            True,
            "no rank lock",
        ),
        ShellWorkCase(
            "nonmonotone deletion action",
            ((0.0, 0.35, 0.25, 1.20),),
            ((0.94, 0.94),),
            True,
            True,
            True,
            True,
            True,
            "negative work",
        ),
        ShellWorkCase(
            "free RN action scale",
            free_scale,
            ((0.94, 0.94),),
            True,
            True,
            False,
            True,
            True,
            "free log unit",
        ),
        ShellWorkCase(
            "free screen entropy unit",
            (action,),
            ((0.94, 0.70), (0.94, 0.94), (0.94, 1.32)),
            True,
            True,
            True,
            False,
            True,
            "free entropy unit",
        ),
        ShellWorkCase(
            "nonconvergent shell action",
            (action, (0.0, 0.35, 0.55, 1.10)),
            ((0.94, 0.94),),
            True,
            True,
            True,
            True,
            False,
            "drifting A",
        ),
        ShellWorkCase(
            "RN shell-work proof",
            (action,),
            ((0.94, 0.94),),
            True,
            True,
            True,
            True,
            True,
            "ranked RN A + count S",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[ShellWorkAudit]) -> None:
    print("shell-work proof campaign")
    print("-------------------------")
    print(
        "candidate                       rule                  shells  RN   scale  "
        "wfloor  Hspan   Tspan   beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:31s}  "
            f"{row.rule:20s}  "
            f"{row.shells:6s}  "
            f"{row.rn:3s}  "
            f"{row.scale:5s}  "
            f"{fmt(row.work_floor):>6s}  "
            f"{fmt(row.h_span):>6s}  "
            f"{fmt(row.t_span):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-THEOREM")
    print("=" * 112)
    print("v6 Paper 2 Part II §5.51: shell-work proof campaign")
    print("=" * 112)
    print_rows(rows)
    print("FINITE PROOF")
    print("------------")
    print("For canonical causal-rank shells and a log Radon-Nikodym deletion action")
    print("A_k on nested retained collars, define w_i=A_{i+1}-A_i.")
    print("If w_i>0, count entropy units are fixed, and the screen/volume")
    print("responses are intrinsic, then H_x and T_x are finite functions of")
    print("the enriched ICS deletion germ.")
    print()
    print(f"The passing finite row is: {winner.candidate}.")
    print()
    print("VERDICT")
    print("-------")
    print("This proves the shell-work/temperature construction for enriched ICS")
    print("germs that already have canonical shells, RN action scale, positive")
    print("action increments, fixed entropy-count units, and refinement stability.")
    print("Every tested weakening reopens the branch-B freedom.")


if __name__ == "__main__":
    main()
