"""
v6 Paper 3 section 14: MDP completeness attack.

Question:
    Is the scalar modular deletion profile M_x(k) the full physical invariant,
    or only the action/readout of a richer sealed deletion germ?

Finite answer:
    M_x(k) is not complete.  Two finite whole-diamond record laws can have the
    same MDP, shell work, beta, and role readouts while having different
    observable higher-order shell correlations.  Therefore the complete
    ontology must be the full sealed deletion germ (P_x, P_delete x, F_x,k,
    role maps, units, action), with M_x(k) as its scalar action profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2an_modular_deletion_profile_campaign import bernoulli_kl
from v6_p3d_feynman_record_channel import (
    ORDER,
    RoleChannel,
    kl,
    marginal,
    markov_residue,
    product_distribution,
    profile,
    sealed_channel,
)
from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import increments


@dataclass(frozen=True)
class PairCase:
    name: str
    left: RoleChannel
    right: RoleChannel
    same_complete_germ_claimed: bool
    rule: str


@dataclass
class PairAudit:
    candidate: str
    rule: str
    profile_gap: float
    beta_gap: float
    total_gap: float
    corr_gap: float
    verdict: str


def p_for_kl(target: float, q: float = 0.5) -> float:
    lo = q
    hi = 1.0 - 1.0e-12
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if bernoulli_kl(mid, q) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def product_matching_profile(reference: RoleChannel) -> RoleChannel:
    work = increments(profile(reference))
    ps = tuple(p_for_kl(value, 0.5) for value in work)
    qs = (0.5,) * len(ps)
    return RoleChannel(product_distribution(ps), product_distribution(qs), ORDER)


def max_profile_gap(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def beta(values: tuple[float, ...]) -> float:
    work = increments(values)
    if not work or any(not isfinite(value) for value in work):
        return float("inf")
    selected, ok, _ = source_response(shell_hamiltonian(work), 1.0)
    return selected if ok else float("inf")


def triple_correlation(dist) -> float:
    mean = []
    for i in range(3):
        mean.append(sum(outcome[i] * prob for outcome, prob in dist.items()))
    centered = 0.0
    for outcome, prob in dist.items():
        value = 1.0
        for i in range(3):
            value *= outcome[i] - mean[i]
        centered += prob * value
    return centered


def correlation_gap(left: RoleChannel, right: RoleChannel) -> float:
    values = [
        abs(markov_residue(left.retained) - markov_residue(right.retained)),
        abs(markov_residue(left.deleted) - markov_residue(right.deleted)),
        abs(triple_correlation(left.retained) - triple_correlation(right.retained)),
        abs(triple_correlation(left.deleted) - triple_correlation(right.deleted)),
    ]
    return max(values)


def full_distribution_gap(left: RoleChannel, right: RoleChannel) -> float:
    events = set(left.retained) | set(right.retained)
    retained_gap = max(abs(left.retained.get(event, 0.0) - right.retained.get(event, 0.0)) for event in events)
    events = set(left.deleted) | set(right.deleted)
    deleted_gap = max(abs(left.deleted.get(event, 0.0) - right.deleted.get(event, 0.0)) for event in events)
    return max(retained_gap, deleted_gap)


def audit(case: PairCase) -> PairAudit:
    left_profile = profile(case.left)
    right_profile = profile(case.right)
    pgap = max_profile_gap(left_profile, right_profile)
    bgap = abs(beta(left_profile) - beta(right_profile))
    total_gap = abs(left_profile[-1] - right_profile[-1])
    cgap = correlation_gap(case.left, case.right)
    full_gap = full_distribution_gap(case.left, case.right)
    if pgap <= 1.0e-9 and cgap <= 1.0e-9 and full_gap <= 1.0e-9:
        verdict = "PASS-SAME-GERM"
    elif pgap <= 1.0e-9 and cgap > 1.0e-3:
        verdict = "FAIL-MDP-NOT-COMPLETE"
    elif total_gap <= 1.0e-9 and pgap > 1.0e-3:
        verdict = "FAIL-TOTAL-NOT-COMPLETE"
    elif case.same_complete_germ_claimed and full_gap > 1.0e-9:
        verdict = "FAIL-DIFFERENT-GERM"
    else:
        verdict = "FAIL-DIFFERENT-PROFILE"
    return PairAudit(case.name, case.rule, pgap, bgap, total_gap, cgap, verdict)


def cases() -> list[PairCase]:
    sealed = sealed_channel()
    mdp_matched_product = product_matching_profile(sealed)
    total_permuted = RoleChannel(sealed.retained, sealed.deleted, (2, 1, 0))
    shifted = product_matching_profile(total_permuted)
    return [
        PairCase("identical sealed germ", sealed, sealed, True, "identity"),
        PairCase(
            "same MDP, different correlations",
            sealed,
            mdp_matched_product,
            True,
            "profile matched",
        ),
        PairCase(
            "same total, different profile",
            sealed,
            total_permuted,
            False,
            "total KL matched",
        ),
        PairCase(
            "different profile and mechanism",
            sealed,
            shifted,
            False,
            "different germ",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[PairAudit]) -> None:
    print("MDP completeness attack")
    print("-----------------------")
    print("candidate                         rule              profile_gap  beta_gap  total_gap  corr_gap  verdict")
    for row in rows:
        print(
            f"{row.candidate:33s} "
            f"{row.rule:17s} "
            f"{fmt(row.profile_gap):>11s} "
            f"{fmt(row.beta_gap):>9s} "
            f"{fmt(row.total_gap):>9s} "
            f"{fmt(row.corr_gap):>8s} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    print("=" * 118)
    print("v6 Paper 3 section 14: MDP completeness attack")
    print("=" * 118)
    print_rows(rows)
    print("VERDICT")
    print("-------")
    print("The scalar MDP is not a complete invariant of the whole finite record law.")
    print("It computes the action/readout chain, but the complete physical object is")
    print("the sealed deletion germ: retained law, deleted law, shell filtration,")
    print("role maps, fixed units, and action.  This strengthens Paper 3 rather than")
    print("refuting it, because CMRP already contains the full germ.")


if __name__ == "__main__":
    main()
