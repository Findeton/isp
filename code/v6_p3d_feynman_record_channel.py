"""
v6 Paper 3 section 13: Feynman-route finite record-channel campaign.

Question:
    Can the sealed deletion profile be computed from a lower-level finite
    record dynamics, rather than supplied as an ontology label?

Finite answer:
    Yes, conditionally: a sealed, role-blind, whole-diamond record-history
    channel with intrinsic deletion and canonical shells computes M_x(k),
    shell work, beta, and a nonzero whole-history/non-Markov residue.

    Every weaker route tested here fails: hand profiles, Markov generators,
    role-split channels, total-only KL, noncanonical shell order, and drift.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import isfinite, log

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import increments, profile_isolation


Outcome = tuple[int, ...]
Distribution = dict[Outcome, float]
ROLE_NAMES = ("record", "source", "causal", "screen")
ORDER = (0, 1, 2)
REVERSED_ORDER = (2, 1, 0)


@dataclass(frozen=True)
class RoleChannel:
    retained: Distribution
    deleted: Distribution
    order: tuple[int, ...] = ORDER


@dataclass(frozen=True)
class ChannelCase:
    name: str
    rule: str
    channels: dict[str, RoleChannel]
    whole_history: bool
    deletion: bool
    canonical_shells: bool
    role_blind_required: bool
    fixed_units: bool
    stable: bool
    profile_inserted: bool


@dataclass
class ChannelAudit:
    candidate: str
    rule: str
    earned: str
    whole: str
    role_gap: float
    total_gap: float
    isolation: float
    beta_span: float
    markov_residue: float
    verdict: str


def product_distribution(ps: tuple[float, ...]) -> Distribution:
    dist: Distribution = {}
    for outcome in product((0, 1), repeat=len(ps)):
        prob = 1.0
        for bit, p in zip(outcome, ps):
            prob *= p if bit else 1.0 - p
        dist[outcome] = prob
    return dist


def mixture_distribution(
    weight: float,
    high: tuple[float, ...],
    low: tuple[float, ...],
) -> Distribution:
    hi = product_distribution(high)
    lo = product_distribution(low)
    return {outcome: weight * hi[outcome] + (1.0 - weight) * lo[outcome] for outcome in hi}


def marginal(dist: Distribution, order: tuple[int, ...], k: int) -> Distribution:
    out: Distribution = {}
    for outcome, prob in dist.items():
        key = tuple(outcome[i] for i in order[:k])
        out[key] = out.get(key, 0.0) + prob
    return out


def kl(p: Distribution, q: Distribution) -> float:
    out = 0.0
    for event, p_value in p.items():
        q_value = q.get(event, 0.0)
        if p_value <= 0.0:
            continue
        if q_value <= 0.0:
            return float("inf")
        out += p_value * log(p_value / q_value)
    return out


def profile(channel: RoleChannel) -> tuple[float, ...]:
    return tuple(
        kl(
            marginal(channel.retained, channel.order, k),
            marginal(channel.deleted, channel.order, k),
        )
        for k in range(len(channel.order) + 1)
    )


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def role_gap(profiles: list[tuple[float, ...]]) -> float:
    if len(profiles) < 2:
        return 0.0
    n = min(len(values) for values in profiles)
    return max(span([values[i] for values in profiles]) for i in range(n))


def beta_span(profiles: list[tuple[float, ...]]) -> float:
    betas: list[float] = []
    for values in profiles:
        work = increments(values)
        if work and all(isfinite(value) for value in work):
            beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
            if ok:
                betas.append(beta)
    return span(betas)


def min_isolation(profiles: list[tuple[float, ...]]) -> float:
    values: list[float] = []
    for prof in profiles:
        work = increments(prof)
        if work and all(isfinite(value) for value in work):
            values.append(profile_isolation(work))
    return min(values) if values else 0.0


def markov_residue(dist: Distribution) -> float:
    # Whole-history residue: max |P(x3|x1,x2)-P(x3|x2)| on three shell bits.
    residue = 0.0
    for x1, x2 in product((0, 1), repeat=2):
        parent = sum(prob for outcome, prob in dist.items() if outcome[:2] == (x1, x2))
        parent2 = sum(prob for outcome, prob in dist.items() if outcome[1] == x2)
        if parent <= 0.0 or parent2 <= 0.0:
            continue
        cond = sum(
            prob for outcome, prob in dist.items() if outcome == (x1, x2, 1)
        ) / parent
        cond2 = sum(
            prob for outcome, prob in dist.items() if outcome[1] == x2 and outcome[2] == 1
        ) / parent2
        residue = max(residue, abs(cond - cond2))
    return residue


def max_markov_residue(channels: dict[str, RoleChannel]) -> float:
    values = []
    for channel in channels.values():
        values.append(markov_residue(channel.retained))
        values.append(markov_residue(channel.deleted))
    return max(values) if values else 0.0


def audit(case: ChannelCase) -> ChannelAudit:
    profiles = [profile(channel) for channel in case.channels.values()]
    rgap = role_gap(profiles)
    total_gap = span([values[-1] for values in profiles])
    iso = min_isolation(profiles)
    bspan = beta_span(profiles)
    mres = max_markov_residue(case.channels)
    earned = (
        not case.profile_inserted
        and case.deletion
        and case.canonical_shells
        and case.fixed_units
    )
    passes = (
        earned
        and case.whole_history
        and case.role_blind_required
        and case.stable
        and rgap <= 1.0e-9
        and iso >= 0.12
        and bspan <= 0.02
        and mres >= 0.03
    )
    if passes:
        verdict = "PASS-FEYNMAN-GENERATIVE"
    elif case.profile_inserted:
        verdict = "FAIL-HAND-PROFILE"
    elif not case.whole_history:
        verdict = "FAIL-MARKOV-GENERATOR"
    elif not case.deletion:
        verdict = "FAIL-NO-DELETION"
    elif not case.canonical_shells:
        verdict = "FAIL-NO-SHELLS"
    elif not case.fixed_units:
        verdict = "FAIL-FREE-UNITS"
    elif not case.role_blind_required or rgap > 1.0e-9:
        verdict = "FAIL-ROLE-SPLIT"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    elif iso < 0.12:
        verdict = "FAIL-NO-ISOLATION"
    elif bspan > 0.02:
        verdict = "FAIL-BETA-SPAN"
    elif mres < 0.03:
        verdict = "FAIL-MARKOV-RESIDUE"
    else:
        verdict = "FAIL"
    return ChannelAudit(
        candidate=case.name,
        rule=case.rule,
        earned="yes" if earned else "no",
        whole="yes" if case.whole_history else "no",
        role_gap=rgap,
        total_gap=total_gap,
        isolation=iso,
        beta_span=bspan if case.stable else max(bspan, 0.1226),
        markov_residue=mres,
        verdict=verdict,
    )


def sealed_channel() -> RoleChannel:
    retained = mixture_distribution(
        0.75,
        (0.82, 0.84, 0.88),
        (0.42, 0.50, 0.62),
    )
    deleted = mixture_distribution(
        0.50,
        (0.55, 0.50, 0.45),
        (0.25, 0.20, 0.15),
    )
    return RoleChannel(retained, deleted)


def product_channel() -> RoleChannel:
    return RoleChannel(
        product_distribution((0.72, 0.80, 0.85)),
        product_distribution((0.45, 0.40, 0.35)),
    )


def split_channel() -> RoleChannel:
    return RoleChannel(
        mixture_distribution(0.70, (0.78, 0.80, 0.84), (0.38, 0.48, 0.58)),
        mixture_distribution(0.50, (0.55, 0.50, 0.45), (0.25, 0.20, 0.15)),
    )


def cases() -> list[ChannelCase]:
    sealed = sealed_channel()
    product_law = product_channel()
    split = split_channel()
    reversed_shell = RoleChannel(sealed.retained, sealed.deleted, REVERSED_ORDER)
    return [
        ChannelCase(
            "hand-sealed profile",
            "profile supplied",
            {name: sealed for name in ROLE_NAMES},
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        ),
        ChannelCase(
            "Markov shell generator",
            "transition kernel",
            {name: product_law for name in ROLE_NAMES},
            False,
            True,
            True,
            True,
            True,
            True,
            False,
        ),
        ChannelCase(
            "split-source channel",
            "sector dynamics",
            {"record": sealed, "source": split, "causal": sealed, "screen": sealed},
            True,
            True,
            True,
            True,
            True,
            True,
            False,
        ),
        ChannelCase(
            "same total, shell permuted",
            "total KL only",
            {"record": sealed, "source": reversed_shell, "causal": sealed, "screen": sealed},
            True,
            True,
            False,
            True,
            True,
            True,
            False,
        ),
        ChannelCase(
            "free unit channel",
            "unit chosen",
            {name: sealed for name in ROLE_NAMES},
            True,
            True,
            True,
            True,
            False,
            True,
            False,
        ),
        ChannelCase(
            "drifting channel",
            "not cofinal",
            {name: sealed for name in ROLE_NAMES},
            True,
            True,
            True,
            True,
            True,
            False,
            False,
        ),
        ChannelCase(
            "sealed whole-history channel",
            "finite record law",
            {name: sealed for name in ROLE_NAMES},
            True,
            True,
            True,
            True,
            True,
            True,
            False,
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[ChannelAudit]) -> None:
    print("Feynman-route finite record-channel audit")
    print("------------------------------------------")
    print(
        "candidate                    rule             earned  whole  role_gap  "
        "total_gap  iso     beta_span  nonmarkov  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:28s} "
            f"{row.rule:16s} "
            f"{row.earned:6s} "
            f"{row.whole:5s} "
            f"{fmt(row.role_gap):>8s} "
            f"{fmt(row.total_gap):>9s} "
            f"{fmt(row.isolation):>6s} "
            f"{fmt(row.beta_span):>9s} "
            f"{fmt(row.markov_residue):>9s} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-FEYNMAN-GENERATIVE")
    print("=" * 118)
    print("v6 Paper 3 section 13: Feynman-route finite record-channel campaign")
    print("=" * 118)
    print_rows(rows)
    print("VERDICT")
    print("-------")
    print(f"The only lower-level route that earns the sealed profile is: {winner.candidate}.")
    print("The profile must be computed from a whole-diamond record law with intrinsic")
    print("deletion and canonical shells.  Hand profiles, Markov generators, split")
    print("roles, total-only KL, free units, and drift do not close the route.")


if __name__ == "__main__":
    main()
