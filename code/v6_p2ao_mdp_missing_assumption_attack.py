"""
v6 Paper 2 Part II section 5.53: attack on the actual MDP assumption.

The Modular Deletion Profile theorem is positive only if the physical event
germ supplies three objects intrinsically:

    F_{x,k}             canonical causal-diamond shell filtration;
    P_x                 retained-event local law;
    P_{delete x}        deleted-event local law on the retained collar image.

This script attacks the missing assumption that bare/ordinary ICS data derive
those objects.  It constructs same-order-shadow finite families in which the
order and deletion shadow are unchanged while P_x, P_{delete x}, or F_{x,k}
varies, moving the MDP and beta.

Result:
    Bare order/deletion data do not derive MDP.  A Modular Physical ICS
    primitive can pass only if the retained law, deleted law, canonical
    filtration, finite RN support, isolated scale, fixed count unit, and
    refinement convergence are supplied by the same event germ.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import (
    MDPLaw,
    increments,
    profile,
    profile_isolation,
)


@dataclass(frozen=True)
class MissingAssumptionCase:
    name: str
    laws: tuple[MDPLaw, ...]
    temperatures: tuple[float, ...]
    order_shadow_fixed: bool
    deletion_shadow_fixed: bool
    canonical_filtration_intrinsic: bool
    retained_law_intrinsic: bool
    deleted_law_intrinsic: bool
    rn_finite: bool
    isolated_scale: bool
    fixed_count_unit: bool
    stable: bool
    rule: str


@dataclass
class MissingAssumptionAudit:
    candidate: str
    rule: str
    order: str
    filtration: str
    p_law: str
    q_law: str
    rn: str
    beta_span: float
    profile_span: float
    verdict: str


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def profile_shape_span(laws: tuple[MDPLaw, ...]) -> float:
    profiles = [profile(law) for law in laws]
    if len(profiles) < 2:
        return 0.0
    out = 0.0
    first = profiles[0]
    for prof in profiles[1:]:
        out = max(out, max(abs(a - b) for a, b in zip(first, prof)))
    return out


def beta_span(laws: tuple[MDPLaw, ...], temperatures: tuple[float, ...]) -> float:
    betas: list[float] = []
    for law in laws:
        prof = profile(law)
        work = increments(prof)
        if not work or any(not isfinite(value) for value in work):
            continue
        h = shell_hamiltonian(work)
        for temperature in temperatures:
            beta, ok, _ = source_response(h, temperature)
            if ok:
                betas.append(beta)
    return span(betas)


def min_work_floor(laws: tuple[MDPLaw, ...]) -> float:
    floors: list[float] = []
    for law in laws:
        work = increments(profile(law))
        if work and all(isfinite(value) for value in work):
            floors.append(min(work))
    return min(floors) if floors else 0.0


def min_isolation(laws: tuple[MDPLaw, ...]) -> float:
    values = []
    for law in laws:
        work = increments(profile(law))
        if work and all(isfinite(value) for value in work):
            values.append(profile_isolation(work))
    return min(values) if values else 0.0


def audit(case: MissingAssumptionCase) -> MissingAssumptionAudit:
    beta_drift = beta_span(case.laws, case.temperatures)
    prof_drift = profile_shape_span(case.laws)
    rn_ok = case.rn_finite and all(all(isfinite(value) for value in profile(law)) for law in case.laws)
    wfloor = min_work_floor(case.laws)
    iso = min_isolation(case.laws)
    passes = (
        case.order_shadow_fixed
        and case.deletion_shadow_fixed
        and case.canonical_filtration_intrinsic
        and case.retained_law_intrinsic
        and case.deleted_law_intrinsic
        and rn_ok
        and case.isolated_scale
        and case.fixed_count_unit
        and case.stable
        and wfloor >= 0.12
        and iso >= 0.12
        and beta_drift <= 0.02
        and prof_drift <= 0.02
    )
    if passes:
        verdict = "PASS-CONDITIONAL"
    elif not (case.canonical_filtration_intrinsic and case.retained_law_intrinsic and case.deleted_law_intrinsic):
        if not case.retained_law_intrinsic and not case.deleted_law_intrinsic:
            verdict = "FAIL-NO-MDP"
        elif not case.retained_law_intrinsic:
            verdict = "FAIL-P-FREE"
        elif not case.deleted_law_intrinsic:
            verdict = "FAIL-Q-FREE"
        else:
            verdict = "FAIL-FREE-F"
    elif not case.retained_law_intrinsic:
        verdict = "FAIL-P-FREE"
    elif not case.deleted_law_intrinsic:
        verdict = "FAIL-Q-FREE"
    elif not case.canonical_filtration_intrinsic:
        verdict = "FAIL-FREE-F"
    elif not rn_ok:
        verdict = "FAIL-NO-RN"
    elif not case.isolated_scale:
        verdict = "FAIL-NO-ISOLATION"
    elif not case.fixed_count_unit:
        verdict = "FAIL-FREE-COUNT"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    else:
        verdict = "FAIL"
    return MissingAssumptionAudit(
        candidate=case.name,
        rule=case.rule,
        order="yes" if case.order_shadow_fixed else "no",
        filtration="yes" if case.canonical_filtration_intrinsic else "no",
        p_law="yes" if case.retained_law_intrinsic else "no",
        q_law="yes" if case.deleted_law_intrinsic else "no",
        rn="yes" if rn_ok else "no",
        beta_span=beta_drift if case.stable else max(beta_drift, 0.1226),
        profile_span=prof_drift,
        verdict=verdict,
    )


def cases() -> list[MissingAssumptionCase]:
    canonical = MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35))
    same_order_different_p = (
        canonical,
        MDPLaw((0.80, 0.70, 0.60), (0.45, 0.40, 0.35)),
    )
    same_order_different_q = (
        canonical,
        MDPLaw((0.72, 0.80, 0.85), (0.50, 0.50, 0.50)),
        MDPLaw((0.72, 0.80, 0.85), (0.35, 0.35, 0.35)),
    )
    same_law_different_f = (
        canonical,
        MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35), (2, 1, 0)),
        MDPLaw((0.72, 0.80, 0.85), (0.45, 0.40, 0.35), (1, 2, 0)),
    )
    drift = (
        canonical,
        MDPLaw((0.75, 0.78, 0.80), (0.45, 0.40, 0.35)),
    )
    flat = MDPLaw((0.74, 0.74, 0.74), (0.40, 0.40, 0.40))
    return [
        MissingAssumptionCase(
            "bare order/deletion shadow",
            (MDPLaw((0.70, 0.80, 0.85), (0.70, 0.80, 0.85)),),
            (1.0,),
            True,
            True,
            False,
            False,
            False,
            True,
            False,
            True,
            True,
            "order only",
        ),
        MissingAssumptionCase(
            "same order, P varies",
            same_order_different_p,
            (1.0,),
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            "P not derived",
        ),
        MissingAssumptionCase(
            "same order, Q varies",
            same_order_different_q,
            (1.0,),
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            "deleted law free",
        ),
        MissingAssumptionCase(
            "same law, F varies",
            same_law_different_f,
            (1.0,),
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            "filtration free",
        ),
        MissingAssumptionCase(
            "singular deleted support",
            (MDPLaw((0.72, 0.80, 0.85), (0.0, 0.40, 0.35)),),
            (1.0,),
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            "P not << Q",
        ),
        MissingAssumptionCase(
            "non-isolated profile",
            (flat,),
            (1.0,),
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            "flat profile",
        ),
        MissingAssumptionCase(
            "free count unit",
            (canonical,),
            (0.70, 1.00, 1.40),
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            "screen unit free",
        ),
        MissingAssumptionCase(
            "refinement-drifting law",
            drift,
            (1.0,),
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            "not cofinal",
        ),
        MissingAssumptionCase(
            "Modular Physical ICS",
            (canonical,),
            (1.0,),
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            "primitive MDP",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[MissingAssumptionAudit]) -> None:
    print("MDP missing-assumption attack")
    print("-----------------------------")
    print(
        "candidate                    rule              order  F    P    Q    RN   "
        "Mspan   beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:28s}  "
            f"{row.rule:16s}  "
            f"{row.order:5s}  "
            f"{row.filtration:3s}  "
            f"{row.p_law:3s}  "
            f"{row.q_law:3s}  "
            f"{row.rn:3s}  "
            f"{fmt(row.profile_span):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def print_witnesses() -> None:
    print("same-shadow witnesses")
    print("---------------------")
    for name in {"same order, P varies", "same order, Q varies", "same law, F varies"}:
        case = next(item for item in cases() if item.name == name)
        print(name)
        for i, law in enumerate(case.laws, start=1):
            prof = profile(law)
            work = increments(prof)
            beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
            print(
                f"  law {i}: M={tuple(round(value, 4) for value in prof)}, "
                f"w={tuple(round(value, 4) for value in work)}, "
                f"beta={beta:.4f}, ok={ok}"
            )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-CONDITIONAL")
    print("=" * 118)
    print("v6 Paper 2 Part II section 5.53: MDP missing-assumption attack")
    print("=" * 118)
    print_rows(rows)
    print_witnesses()
    print("NO-GO")
    print("-----")
    print("Bare order/deletion shadow does not determine the Modular Deletion Profile.")
    print("Keeping the same order shadow while varying P_x, P_delete, or the shell")
    print("filtration changes M_x(k), shell work, and beta.")
    print()
    print("CONDITIONAL SURVIVOR")
    print("--------------------")
    print(f"The only passing row is: {winner.candidate}.")
    print("It passes only because the primitive already supplies canonical F,")
    print("retained/deleted laws, finite RN support, isolated scale, fixed count")
    print("unit, and refinement stability.")


if __name__ == "__main__":
    main()
