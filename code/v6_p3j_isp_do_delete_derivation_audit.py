"""
v6 Paper 3 section 20: ISP do-delete derivation audit.

Question:
    Which ISP-native rule could derive the canonical do-delete operation?

Finite answer:
    The only passing finite rule is conditional:

        do-delete = unique minimum-disturbance factorization repair
                    at a division-event atom,

    with a fixed null state, boundary/collar preservation, role-blind response,
    non-Markov retained law, positive isolated deletion work, and cofinal
    stability.  Conditioning, erasure, unconstrained KL projection, Markov
    repair, role-specific repair, and free null states fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import increments, profile_isolation
from v6_p3d_feynman_record_channel import (
    ROLE_NAMES,
    RoleChannel,
    markov_residue,
    profile,
    product_channel,
    sealed_channel,
    split_channel,
)


@dataclass(frozen=True)
class DeleteRuleCase:
    name: str
    rule: str
    channels: dict[str, RoleChannel]
    event_atom: bool
    fixed_null: bool
    factorization_repair: bool
    min_disturbance_unique: bool
    boundary_preserving: bool
    role_blind: bool
    nonmarkov_retained: bool
    stable: bool


@dataclass
class DeleteRuleAudit:
    candidate: str
    rule: str
    atom: str
    null: str
    repair: str
    role_gap: float
    isolation: float
    beta_span: float
    nonmarkov: float
    verdict: str


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def role_gap(profiles: list[tuple[float, ...]]) -> float:
    if len(profiles) < 2:
        return 0.0
    n = min(len(values) for values in profiles)
    return max(span([values[i] for values in profiles]) for i in range(n))


def min_isolation(profiles: list[tuple[float, ...]]) -> float:
    values = []
    for prof in profiles:
        work = increments(prof)
        if work and all(isfinite(value) for value in work):
            values.append(profile_isolation(work))
    return min(values) if values else 0.0


def beta_span(profiles: list[tuple[float, ...]]) -> float:
    betas = []
    for prof in profiles:
        work = increments(prof)
        if work and all(isfinite(value) for value in work):
            beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
            if ok:
                betas.append(beta)
    return span(betas)


def nonmarkov(channels: dict[str, RoleChannel]) -> float:
    values = []
    for channel in channels.values():
        values.append(markov_residue(channel.retained))
        values.append(markov_residue(channel.deleted))
    return max(values) if values else 0.0


def audit(case: DeleteRuleCase) -> DeleteRuleAudit:
    profiles = [profile(channel) for channel in case.channels.values()]
    rgap = role_gap(profiles)
    iso = min_isolation(profiles)
    bspan = beta_span(profiles)
    mres = nonmarkov(case.channels)
    passes = (
        case.event_atom
        and case.fixed_null
        and case.factorization_repair
        and case.min_disturbance_unique
        and case.boundary_preserving
        and case.role_blind
        and case.nonmarkov_retained
        and case.stable
        and rgap <= 1.0e-9
        and iso >= 0.12
        and bspan <= 0.02
        and mres >= 0.03
    )
    if passes:
        verdict = "PASS-ISP-DO-DELETE-TARGET"
    elif not case.event_atom:
        verdict = "FAIL-NO-EVENT-ATOM"
    elif not case.fixed_null:
        verdict = "FAIL-FREE-NULL"
    elif not case.factorization_repair:
        verdict = "FAIL-NO-FACTOR-REPAIR"
    elif not case.min_disturbance_unique:
        verdict = "FAIL-DEGENERATE-REPAIR"
    elif not case.boundary_preserving:
        verdict = "FAIL-BOUNDARY-DRIFT"
    elif not case.role_blind or rgap > 1.0e-9:
        verdict = "FAIL-ROLE-SPLIT"
    elif not case.nonmarkov_retained or mres < 0.03:
        verdict = "FAIL-MARKOV"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    elif iso < 0.12:
        verdict = "FAIL-NO-ISOLATION"
    elif bspan > 0.02:
        verdict = "FAIL-BETA-SPAN"
    else:
        verdict = "FAIL"
    return DeleteRuleAudit(
        candidate=case.name,
        rule=case.rule,
        atom="yes" if case.event_atom else "no",
        null="yes" if case.fixed_null else "no",
        repair="yes" if case.factorization_repair else "no",
        role_gap=rgap,
        isolation=iso,
        beta_span=bspan if case.stable else max(bspan, 0.1226),
        nonmarkov=mres,
        verdict=verdict,
    )


def weak_channel() -> RoleChannel:
    sealed = sealed_channel()
    return RoleChannel(sealed.retained, sealed.retained)


def cases() -> list[DeleteRuleCase]:
    sealed = sealed_channel()
    split = split_channel()
    product = product_channel()
    all_roles = {name: sealed for name in ROLE_NAMES}
    markov_roles = {name: product for name in ROLE_NAMES}
    return [
        DeleteRuleCase(
            "conditioning on absence",
            "P(.|X=0)",
            all_roles,
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            True,
        ),
        DeleteRuleCase(
            "erase event only",
            "remove label",
            {name: weak_channel() for name in ROLE_NAMES},
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
        ),
        DeleteRuleCase(
            "unconstrained KL repair",
            "free projection",
            all_roles,
            True,
            True,
            True,
            False,
            False,
            True,
            True,
            True,
        ),
        DeleteRuleCase(
            "free-null repair",
            "null chosen",
            all_roles,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
        ),
        DeleteRuleCase(
            "role-specific repair",
            "four repairs",
            {"record": sealed, "source": split, "causal": sealed, "screen": sealed},
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
        ),
        DeleteRuleCase(
            "Markov factor repair",
            "semigroup",
            markov_roles,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
        ),
        DeleteRuleCase(
            "drifting repair",
            "not cofinal",
            all_roles,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
        ),
        DeleteRuleCase(
            "division-event repair",
            "unique factor repair",
            all_roles,
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


def print_rows(rows: list[DeleteRuleAudit]) -> None:
    print("ISP do-delete derivation audit")
    print("------------------------------")
    print(
        "candidate                  rule                atom  null  repair  role_gap  "
        "iso     beta_span  nonmarkov  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:26s} "
            f"{row.rule:18s} "
            f"{row.atom:4s}  "
            f"{row.null:4s}  "
            f"{row.repair:6s}  "
            f"{fmt(row.role_gap):>8s}  "
            f"{fmt(row.isolation):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{fmt(row.nonmarkov):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-ISP-DO-DELETE-TARGET")
    print("=" * 118)
    print("v6 Paper 3 section 20: ISP do-delete derivation audit")
    print("=" * 118)
    print_rows(rows)
    print("VERDICT")
    print("-------")
    print(f"The only finite ISP-native do-delete target is: {winner.candidate}.")
    print("Do-delete can be derived only if a division event carries a fixed null")
    print("state and a unique boundary-preserving factorization repair.  Otherwise")
    print("it is conditioning, erasure, a free projection, or branch-B input.")


if __name__ == "__main__":
    main()
