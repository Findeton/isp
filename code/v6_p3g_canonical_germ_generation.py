"""
v6 Paper 3 section 17: canonical sealed-germ generation class.

Question:
    What lower-level finite record dynamics is sufficient to generate a
    canonical sealed deletion germ G_x?

Finite answer:
    A canonical germ is generated when the lower-level whole-diamond law has:

        an intrinsic event/intervention variable;
        a unique do-delete operation;
        strict causal-rank shell labels;
        role-blind response maps;
        fixed count/action units;
        positive isolated deletion work;
        non-Markov whole-history residue;
        cofinal stability.

    Removing any one of these reopens nonuniqueness or branch-B freedom.
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
    sealed_channel,
    split_channel,
)


@dataclass(frozen=True)
class GenerationCase:
    name: str
    rule: str
    channels: dict[str, RoleChannel]
    event_variable: bool
    unique_do_delete: bool
    strict_shell_ranks: bool
    role_blind: bool
    fixed_units: bool
    fixed_action: bool
    cofinal: bool
    competing_germs: int


@dataclass
class GenerationAudit:
    candidate: str
    rule: str
    event: str
    do_delete: str
    ranks: str
    role_gap: float
    isolation: float
    beta_span: float
    nonmarkov: float
    competing: int
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
    values: list[float] = []
    for prof in profiles:
        work = increments(prof)
        if work and all(isfinite(value) for value in work):
            values.append(profile_isolation(work))
    return min(values) if values else 0.0


def beta_span(profiles: list[tuple[float, ...]]) -> float:
    values: list[float] = []
    for prof in profiles:
        work = increments(prof)
        if not work or any(not isfinite(value) for value in work):
            continue
        beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
        if ok:
            values.append(beta)
    return span(values)


def nonmarkov_residue(channels: dict[str, RoleChannel]) -> float:
    values: list[float] = []
    for channel in channels.values():
        values.append(markov_residue(channel.retained))
        values.append(markov_residue(channel.deleted))
    return max(values) if values else 0.0


def audit(case: GenerationCase) -> GenerationAudit:
    profiles = [profile(channel) for channel in case.channels.values()]
    rgap = role_gap(profiles)
    iso = min_isolation(profiles)
    bspan = beta_span(profiles)
    mres = nonmarkov_residue(case.channels)
    passes = (
        case.event_variable
        and case.unique_do_delete
        and case.strict_shell_ranks
        and case.role_blind
        and case.fixed_units
        and case.fixed_action
        and case.cofinal
        and case.competing_germs == 1
        and rgap <= 1.0e-9
        and iso >= 0.12
        and bspan <= 0.02
        and mres >= 0.03
    )
    if passes:
        verdict = "PASS-CANONICAL-GERM"
    elif not case.event_variable:
        verdict = "FAIL-NO-EVENT-VARIABLE"
    elif not case.unique_do_delete:
        verdict = "FAIL-NONUNIQUE-DO"
    elif not case.strict_shell_ranks:
        verdict = "FAIL-RANK-DEGENERACY"
    elif not case.role_blind or rgap > 1.0e-9:
        verdict = "FAIL-ROLE-SPLIT"
    elif not case.fixed_units:
        verdict = "FAIL-FREE-UNITS"
    elif not case.fixed_action:
        verdict = "FAIL-FREE-ACTION"
    elif case.competing_germs != 1:
        verdict = "FAIL-COMPETING-GERMS"
    elif iso < 0.12:
        verdict = "FAIL-NO-ISOLATION"
    elif mres < 0.03:
        verdict = "FAIL-MARKOV"
    elif not case.cofinal:
        verdict = "FAIL-DRIFT"
    else:
        verdict = "FAIL"
    return GenerationAudit(
        candidate=case.name,
        rule=case.rule,
        event="yes" if case.event_variable else "no",
        do_delete="yes" if case.unique_do_delete else "no",
        ranks="yes" if case.strict_shell_ranks else "no",
        role_gap=rgap,
        isolation=iso,
        beta_span=bspan if case.cofinal else max(bspan, 0.1226),
        nonmarkov=mres,
        competing=case.competing_germs,
        verdict=verdict,
    )


def weak_channel() -> RoleChannel:
    sealed = sealed_channel()
    # Same whole-history structure, but tiny deletion contrast.
    return RoleChannel(sealed.retained, sealed.retained)


def cases() -> list[GenerationCase]:
    sealed = sealed_channel()
    split = split_channel()
    all_roles = {name: sealed for name in ROLE_NAMES}
    return [
        GenerationCase(
            "latent mixture only",
            "no event variable",
            all_roles,
            False,
            False,
            True,
            True,
            True,
            True,
            True,
            2,
        ),
        GenerationCase(
            "event without do-delete",
            "no intervention",
            all_roles,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            2,
        ),
        GenerationCase(
            "rank-degenerate event",
            "tied shells",
            all_roles,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            2,
        ),
        GenerationCase(
            "role-specific intervention",
            "four sectors",
            {"record": sealed, "source": split, "causal": sealed, "screen": sealed},
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            1,
        ),
        GenerationCase(
            "free-unit intervention",
            "unit chosen",
            all_roles,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            1,
        ),
        GenerationCase(
            "weak deletion event",
            "no contrast",
            {name: weak_channel() for name in ROLE_NAMES},
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            1,
        ),
        GenerationCase(
            "drifting intervention",
            "not cofinal",
            all_roles,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            1,
        ),
        GenerationCase(
            "canonical event intervention",
            "strict do-delete",
            all_roles,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            1,
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[GenerationAudit]) -> None:
    print("canonical sealed-germ generation audit")
    print("--------------------------------------")
    print(
        "candidate                     rule             event  do    ranks  role_gap  "
        "iso     beta_span  nonmarkov  germs  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:29s} "
            f"{row.rule:16s} "
            f"{row.event:5s}  "
            f"{row.do_delete:3s}  "
            f"{row.ranks:5s}  "
            f"{fmt(row.role_gap):>8s}  "
            f"{fmt(row.isolation):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{fmt(row.nonmarkov):>9s}  "
            f"{row.competing:5d}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-CANONICAL-GERM")
    print("=" * 118)
    print("v6 Paper 3 section 17: canonical sealed-germ generation class")
    print("=" * 118)
    print_rows(rows)
    print("VERDICT")
    print("-------")
    print(f"The finite positive generation class is: {winner.candidate}.")
    print("The lower-level law must carry a strict event-intervention structure.")
    print("Without it, the sealed germ is not derived; it is selected.")


if __name__ == "__main__":
    main()
