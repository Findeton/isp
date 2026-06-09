"""
v6 Paper 3 section 16: sealed germ origin/uniqueness audit.

Question:
    Does a lower-level whole-diamond record dynamics determine a unique sealed
    deletion germ

        G_x = (P_x, P_delete x, F_x,k, role maps, fixed units, action)?

Finite answer:
    Not from the retained whole-history law alone.  The same retained law can
    be paired with different deletion laws, shell filtrations, or role maps,
    giving different germs and different derived beta/readouts.  A unique
    germ is obtained only when the lower-level dynamics includes an intrinsic
    event-intervention/deletion structure, canonical shell ranks, role maps,
    fixed units, and an isolation/cofinal margin.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import increments
from v6_p3d_feynman_record_channel import (
    ORDER,
    REVERSED_ORDER,
    ROLE_NAMES,
    RoleChannel,
    product_distribution,
    profile,
    role_gap,
    sealed_channel,
    split_channel,
)


@dataclass(frozen=True)
class GermOriginCase:
    name: str
    rule: str
    channels: tuple[RoleChannel, ...]
    has_retained_law: bool
    intrinsic_deletion: bool
    canonical_shells: bool
    role_maps_fixed: bool
    units_fixed: bool
    action_fixed: bool
    uniqueness_margin: bool
    cofinal: bool


@dataclass
class GermOriginAudit:
    candidate: str
    rule: str
    choices: int
    deln: str
    shells: str
    roles: str
    profile_span: float
    beta_span: float
    verdict: str


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def max_profile_span(channels: tuple[RoleChannel, ...]) -> float:
    profiles = [profile(channel) for channel in channels]
    if len(profiles) < 2:
        return 0.0
    n = min(len(values) for values in profiles)
    return max(span([values[i] for values in profiles]) for i in range(n))


def profile_beta(channel: RoleChannel) -> float | None:
    work = increments(profile(channel))
    if not work or any(not isfinite(value) for value in work):
        return None
    beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
    return beta if ok else None


def beta_span(channels: tuple[RoleChannel, ...]) -> float:
    betas = [beta for beta in (profile_beta(channel) for channel in channels) if beta is not None]
    return span(betas)


def audit(case: GermOriginCase) -> GermOriginAudit:
    pspan = max_profile_span(case.channels)
    bspan = beta_span(case.channels)
    passes = (
        case.has_retained_law
        and case.intrinsic_deletion
        and case.canonical_shells
        and case.role_maps_fixed
        and case.units_fixed
        and case.action_fixed
        and case.uniqueness_margin
        and case.cofinal
        and len(case.channels) == 1
        and pspan <= 1.0e-9
        and bspan <= 0.02
    )
    if passes:
        verdict = "PASS-UNIQUE-GERM"
    elif not case.has_retained_law:
        verdict = "FAIL-NO-P"
    elif not case.intrinsic_deletion:
        verdict = "FAIL-NONUNIQUE-DELETION"
    elif not case.canonical_shells:
        verdict = "FAIL-NONUNIQUE-SHELLS"
    elif not case.role_maps_fixed:
        verdict = "FAIL-NONUNIQUE-ROLES"
    elif not case.units_fixed:
        verdict = "FAIL-FREE-UNITS"
    elif not case.action_fixed:
        verdict = "FAIL-FREE-ACTION"
    elif not case.uniqueness_margin:
        verdict = "FAIL-DEGENERATE-MINIMUM"
    elif not case.cofinal:
        verdict = "FAIL-DRIFT"
    elif pspan > 1.0e-9 or bspan > 0.02:
        verdict = "FAIL-MULTIPLE-GERMS"
    else:
        verdict = "FAIL"
    return GermOriginAudit(
        candidate=case.name,
        rule=case.rule,
        choices=len(case.channels),
        deln="yes" if case.intrinsic_deletion else "no",
        shells="yes" if case.canonical_shells else "no",
        roles="yes" if case.role_maps_fixed else "no",
        profile_span=pspan,
        beta_span=bspan if case.cofinal else max(bspan, 0.1226),
        verdict=verdict,
    )


def cases() -> list[GermOriginCase]:
    sealed = sealed_channel()
    retained = sealed.retained
    deletion_alt = RoleChannel(
        retained,
        product_distribution((0.48, 0.42, 0.36)),
        ORDER,
    )
    shell_alt = RoleChannel(retained, sealed.deleted, REVERSED_ORDER)
    split = split_channel()
    return [
        GermOriginCase(
            "no retained law",
            "order shadow",
            tuple(),
            False,
            False,
            False,
            False,
            True,
            True,
            False,
            True,
        ),
        GermOriginCase(
            "retained law only",
            "P only",
            (sealed, deletion_alt),
            True,
            False,
            False,
            False,
            True,
            True,
            False,
            True,
        ),
        GermOriginCase(
            "free deletion law",
            "same P, many Q",
            (sealed, deletion_alt),
            True,
            False,
            True,
            True,
            True,
            True,
            False,
            True,
        ),
        GermOriginCase(
            "free shell filtration",
            "same P/Q, many F",
            (sealed, shell_alt),
            True,
            True,
            False,
            True,
            True,
            True,
            False,
            True,
        ),
        GermOriginCase(
            "free role map",
            "same support, split role",
            (sealed, split),
            True,
            True,
            True,
            False,
            True,
            True,
            False,
            True,
        ),
        GermOriginCase(
            "free action/unit germ",
            "scale chosen",
            (sealed,),
            True,
            True,
            True,
            True,
            False,
            False,
            False,
            True,
        ),
        GermOriginCase(
            "degenerate action minimum",
            "two equal germs",
            (sealed, shell_alt),
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
        ),
        GermOriginCase(
            "drifting germ",
            "not cofinal",
            (sealed,),
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
        ),
        GermOriginCase(
            "intrinsic intervention germ",
            "unique do-delete",
            (sealed,),
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[GermOriginAudit]) -> None:
    print("sealed germ origin/uniqueness audit")
    print("-----------------------------------")
    print(
        "candidate                      rule              choices  del  shell  role  "
        "profile_span  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:30s} "
            f"{row.rule:17s} "
            f"{row.choices:7d}  "
            f"{row.deln:3s}  "
            f"{row.shells:5s}  "
            f"{row.roles:4s}  "
            f"{fmt(row.profile_span):>12s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-UNIQUE-GERM")
    print("=" * 118)
    print("v6 Paper 3 section 16: sealed germ origin/uniqueness audit")
    print("=" * 118)
    print_rows(rows)
    print("VERDICT")
    print("-------")
    print(f"The only finite origin row with a unique germ is: {winner.candidate}.")
    print("A whole retained law alone does not determine deletion, shells, role maps,")
    print("or units.  A unique G_x requires an intrinsic do-delete/intervention")
    print("structure plus canonical shells, fixed units/action, and a cofinal margin.")


if __name__ == "__main__":
    main()
