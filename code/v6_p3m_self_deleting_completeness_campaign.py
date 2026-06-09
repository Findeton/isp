"""
v6 Paper 3 section 23: self-deleting defect completeness campaign.

Question:
    Is the self-deleting factorization-defect law complete, or can two
    internally indistinguishable diamonds require different deletion maps?

Finite answer:
    Weaker internal readouts are not complete.  Same scalar action, same
    boundary marginals, or the same retained law with an unfixed factorization
    cut can leave different deletion repairs.  The full self-deleting law is
    complete at finite level only after the null-factorization target is
    internally fixed:

        same retained law P_x + same internally defined null class N_x(B_x)
        => same entropy repair P_{delete x}.

    The campaign also exposes a technical correction: the naive product
    factorization family is not convex under mixture.  Uniqueness must be
    proved either by the product-family KL chain rule for a fixed partition,
    or by replacing the null class with a genuinely convex repair class.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import isfinite, log, sqrt

from v6_p2an_modular_deletion_profile_campaign import increments
from v6_p3d_feynman_record_channel import (
    ORDER,
    Distribution,
    RoleChannel,
    kl,
    marginal,
    mixture_distribution,
    product_distribution,
    profile,
    sealed_channel,
)


SINGLES = ((0,), (1,), (2,))
FIRST_REST = ((0,), (1, 2))
PAIR_LAST = ((0, 1), (2,))


@dataclass(frozen=True)
class CompletenessCase:
    name: str
    readout: str
    same_internal: bool
    p_left: Distribution
    q_left: Distribution
    p_right: Distribution
    q_right: Distribution
    cut_fixed: bool
    null_convex: bool
    unique_theorem: bool
    note: str


@dataclass
class CompletenessAudit:
    candidate: str
    readout: str
    same: str
    cut: str
    convex: str
    action_gap: float
    repair_gap: float
    scale_gap: float
    verdict: str


def product_projection(p: Distribution, groups: tuple[tuple[int, ...], ...]) -> Distribution:
    n = len(next(iter(p)))
    group_marginals: list[tuple[tuple[int, ...], Distribution]] = []
    for group in groups:
        dist: Distribution = {}
        for outcome, prob in p.items():
            key = tuple(outcome[i] for i in group)
            dist[key] = dist.get(key, 0.0) + prob
        group_marginals.append((group, dist))

    q: Distribution = {}
    for outcome in product((0, 1), repeat=n):
        prob = 1.0
        for group, dist in group_marginals:
            key = tuple(outcome[i] for i in group)
            prob *= dist[key]
        q[outcome] = prob
    return q


def mixture(a: Distribution, b: Distribution, weight: float) -> Distribution:
    return {event: weight * a[event] + (1.0 - weight) * b[event] for event in a}


def distribution_gap(a: Distribution, b: Distribution) -> float:
    events = set(a) | set(b)
    return max(abs(a.get(event, 0.0) - b.get(event, 0.0)) for event in events)


def action(p: Distribution, q: Distribution) -> float:
    return kl(p, q)


def scale_proxy(p: Distribution, q: Distribution) -> float:
    values = profile(RoleChannel(p, q, ORDER))
    work = increments(values)
    positive = [value for value in work if isfinite(value) and value > 1.0e-12]
    if not positive:
        return float("inf")
    return 1.0 / sqrt(max(positive))


def factorization_residual(q: Distribution, groups: tuple[tuple[int, ...], ...]) -> float:
    return distribution_gap(q, product_projection(q, groups))


def find_weight_for_action(
    target: float,
    high: tuple[float, ...],
    low: tuple[float, ...],
) -> float:
    def value(weight: float) -> float:
        p = mixture_distribution(weight, high, low)
        q = product_projection(p, SINGLES)
        return action(p, q) - target

    previous_weight = 0.0
    previous_value = value(previous_weight)
    for step in range(1, 1001):
        weight = step / 1000.0
        current_value = value(weight)
        if previous_value * current_value <= 0.0 and weight > 0.0:
            lo = previous_weight
            hi = weight
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                mid_value = value(mid)
                if value(lo) * mid_value <= 0.0:
                    hi = mid
                else:
                    lo = mid
            return 0.5 * (lo + hi)
        previous_weight = weight
        previous_value = current_value
    raise RuntimeError("no action-matching weight found")


def same_scalar_action_case() -> CompletenessCase:
    p_left = sealed_channel().retained
    q_left = product_projection(p_left, SINGLES)
    target = action(p_left, q_left)
    high = (0.90, 0.20, 0.75)
    low = (0.10, 0.85, 0.25)
    weight = find_weight_for_action(target, high, low)
    p_right = mixture_distribution(weight, high, low)
    q_right = product_projection(p_right, SINGLES)
    return CompletenessCase(
        "same scalar action",
        "A_x only",
        True,
        p_left,
        q_left,
        p_right,
        q_right,
        True,
        False,
        False,
        "two different retained laws can have the same total defect action",
    )


def boundary_only_case() -> CompletenessCase:
    p_left = sealed_channel().retained
    q_left = product_projection(p_left, SINGLES)
    p_right = q_left
    q_right = product_projection(p_right, SINGLES)
    return CompletenessCase(
        "same shell boundary",
        "one-shell marginals",
        True,
        p_left,
        q_left,
        p_right,
        q_right,
        True,
        False,
        False,
        "same one-shell marginals do not determine the retained whole law",
    )


def cut_free_case() -> CompletenessCase:
    p = sealed_channel().retained
    return CompletenessCase(
        "same P, cut free",
        "P_x without N_x",
        True,
        p,
        product_projection(p, SINGLES),
        p,
        product_projection(p, FIRST_REST),
        False,
        False,
        False,
        "same retained law has different repairs if the null cut is not intrinsic",
    )


def fixed_cut_case() -> CompletenessCase:
    p = sealed_channel().retained
    q = product_projection(p, SINGLES)
    return CompletenessCase(
        "same P and same N_x",
        "full defect law",
        True,
        p,
        q,
        p,
        q,
        True,
        False,
        True,
        "fixed product partition has a unique KL repair by the chain rule",
    )


def same_boundary_different_p_case() -> CompletenessCase:
    p_left = sealed_channel().retained
    q_left = product_projection(p_left, SINGLES)
    p_right = mixture(p_left, q_left, 0.35)
    q_right = product_projection(p_right, SINGLES)
    return CompletenessCase(
        "same boundary, different P",
        "boundary not full law",
        False,
        p_left,
        q_left,
        p_right,
        q_right,
        True,
        False,
        True,
        "full retained laws differ, so the diamonds are not internally indistinguishable",
    )


def nonconvexity_case() -> CompletenessCase:
    q1 = product_distribution((0.20, 0.80, 0.20))
    q2 = product_distribution((0.80, 0.20, 0.80))
    mixed = mixture(q1, q2, 0.5)
    return CompletenessCase(
        "naive product convexity",
        "N_x convexity",
        True,
        mixed,
        q1,
        mixed,
        q2,
        True,
        factorization_residual(mixed, SINGLES) <= 1.0e-12,
        False,
        "mixtures of product laws are generally not product laws",
    )


def audit(case: CompletenessCase) -> CompletenessAudit:
    agap = abs(action(case.p_left, case.q_left) - action(case.p_right, case.q_right))
    rgap = distribution_gap(case.q_left, case.q_right)
    left_scale = scale_proxy(case.p_left, case.q_left)
    right_scale = scale_proxy(case.p_right, case.q_right)
    if left_scale == float("inf") and right_scale == float("inf"):
        sgap = 0.0
    else:
        sgap = abs(left_scale - right_scale)

    if case.name == "same scalar action":
        verdict = "FAIL-SCALAR-NOT-COMPLETE" if rgap > 1.0e-3 else "PASS"
    elif case.name == "same shell boundary":
        verdict = "FAIL-BOUNDARY-NOT-COMPLETE"
    elif case.name == "same P, cut free":
        verdict = "FAIL-CUT-NOT-INTERNAL" if rgap > 1.0e-3 else "PASS"
    elif case.name == "same P and same N_x":
        verdict = "PASS-FINITE-COMPLETE" if rgap <= 1.0e-12 and sgap <= 1.0e-12 else "FAIL"
    elif case.name == "same boundary, different P":
        verdict = "PASS-DISTINGUISHED-BY-FULL-LAW" if not case.same_internal else "FAIL"
    elif case.name == "naive product convexity":
        residual = factorization_residual(case.p_left, SINGLES)
        verdict = "FAIL-NAIVE-CONVEXITY" if residual > 1.0e-3 else "PASS-CONVEX"
    elif case.unique_theorem and rgap <= 1.0e-12:
        verdict = "PASS-FINITE-COMPLETE"
    else:
        verdict = "FAIL"

    return CompletenessAudit(
        candidate=case.name,
        readout=case.readout,
        same="yes" if case.same_internal else "no",
        cut="yes" if case.cut_fixed else "no",
        convex="yes" if case.null_convex else "no",
        action_gap=agap,
        repair_gap=rgap,
        scale_gap=sgap if isfinite(sgap) else float("inf"),
        verdict=verdict,
    )


def projection_margin(p: Distribution, groups: tuple[tuple[int, ...], ...]) -> float:
    q_star = product_projection(p, groups)
    base = action(p, q_star)
    marginals = []
    for i in range(3):
        marginals.append(sum(prob for outcome, prob in p.items() if outcome[i] == 1))
    deltas = (-0.16, -0.08, 0.08, 0.16)
    best = float("inf")
    for shifts in product(deltas, repeat=3):
        ps = tuple(min(0.95, max(0.05, m + s)) for m, s in zip(marginals, shifts))
        q_alt = product_distribution(ps)
        best = min(best, action(p, q_alt) - base)
    return best


def print_rows(rows: list[CompletenessAudit]) -> None:
    print("self-deleting completeness audit")
    print("--------------------------------")
    print(
        "candidate                    readout            same  cut  convex  "
        "action_gap repair_gap scale_gap verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:28s} "
            f"{row.readout:18s} "
            f"{row.same:5s} "
            f"{row.cut:4s} "
            f"{row.convex:7s} "
            f"{row.action_gap:10.4g} "
            f"{row.repair_gap:10.4g} "
            f"{row.scale_gap:9.4g} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    cases = [
        same_scalar_action_case(),
        boundary_only_case(),
        cut_free_case(),
        same_boundary_different_p_case(),
        nonconvexity_case(),
        fixed_cut_case(),
    ]
    rows = [audit(case) for case in cases]
    p = sealed_channel().retained
    margin = projection_margin(p, SINGLES)
    residual = factorization_residual(
        mixture(
            product_distribution((0.20, 0.80, 0.20)),
            product_distribution((0.80, 0.20, 0.80)),
            0.5,
        ),
        SINGLES,
    )

    print("=" * 118)
    print("v6 Paper 3 section 23: self-deleting defect completeness campaign")
    print("=" * 118)
    print_rows(rows)
    print("FIXED-CUT UNIQUENESS CHECK")
    print("--------------------------")
    print(f"minimum sampled KL margin above product repair = {margin:.6f}")
    print(f"mixture residual showing product-family nonconvexity = {residual:.6f}")
    print()
    print("VERDICT")
    print("-------")
    print("The ontology is complete at finite level only for the full self-deleting")
    print("defect law: same retained law and same internally fixed null-factorization")
    print("target give the same deletion repair.  Weaker readouts are refuted.")
    print("The theorem target must not rely on naive convexity of product laws; it must")
    print("prove a canonical fixed partition/product projection, or a genuinely convex")
    print("eventless repair class.")


if __name__ == "__main__":
    main()
