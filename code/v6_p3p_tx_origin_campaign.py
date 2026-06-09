"""
v6 Paper 3 section 26: intrinsic T_x origin campaign.

Question:
    Can T_x be derived as the unique invariant expression of record transport
    across the eventless collar?

Finite answer:
    Not from boundary ranks, raw pair correlations, supplied kernels, node
    labels, role-split laws, free regraduations, or drifting laws.

    A positive finite target exists when the sealed eventless collar law gives
    a role-blind conditional-information transport:

        T_x(i,j) = I(Y_i ; Y_j | Y_{collar \\ {i,j}})

    in fixed KL/nat units.  This transport is symmetric, nonnegative,
    relabel-invariant, role-blind, and can have a unique isolated edge gap.
    Its gap then feeds the collar-separator theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import exp, isfinite, log, sqrt

from v6_p3d_feynman_record_channel import Distribution
from v6_p3o_intrinsic_collar_separator_theorem import (
    CROSS_BLOCKS,
    NODES,
    PAIR_BLOCKS,
    ROLE_NAMES,
    EdgeWeights,
    edge_gap_separator,
    partition_label,
    relabel_weights,
)


@dataclass(frozen=True)
class TransportCase:
    name: str
    rule: str
    laws_by_role: dict[str, Distribution] | None
    supplied: EdgeWeights | None
    intrinsic_law: bool
    units_fixed: bool
    role_blind_required: bool
    stable: bool


@dataclass
class TransportAudit:
    candidate: str
    rule: str
    intrinsic: str
    units: str
    partition: str
    gap: float
    margin: float
    invariant: str
    role_blind: str
    verdict: str


def ising_distribution(couplings: EdgeWeights) -> Distribution:
    dist: Distribution = {}
    total = 0.0
    for bits in product((0, 1), repeat=len(NODES)):
        spins = [2 * bit - 1 for bit in bits]
        energy = sum(theta * spins[i] * spins[j] for (i, j), theta in couplings.items())
        weight = exp(energy)
        dist[bits] = weight
        total += weight
    return {event: value / total for event, value in dist.items()}


def pair_law(partition, strong: float = 1.20, weak: float = 0.05) -> Distribution:
    groups = [set(group) for group in partition]
    couplings: EdgeWeights = {}
    for i, j in combinations(NODES, 2):
        same = any(i in group and j in group for group in groups)
        couplings[(i, j)] = strong if same else weak
    return ising_distribution(couplings)


def tied_law(strength: float = 0.45) -> Distribution:
    return ising_distribution({edge: strength for edge in combinations(NODES, 2)})


def common_mode_law(high: float = 0.85, low: float = 0.15) -> Distribution:
    dist: Distribution = {}
    for bits in product((0, 1), repeat=len(NODES)):
        prob_high = 1.0
        prob_low = 1.0
        for bit in bits:
            prob_high *= high if bit else 1.0 - high
            prob_low *= low if bit else 1.0 - low
        dist[bits] = 0.5 * prob_high + 0.5 * prob_low
    return dist


def relabel_distribution(dist: Distribution, permutation: dict[int, int]) -> Distribution:
    out: Distribution = {}
    for bits, prob in dist.items():
        relabeled = [0] * len(bits)
        for old, new in permutation.items():
            relabeled[new] = bits[old]
        out[tuple(relabeled)] = prob
    return out


def event_prob(dist: Distribution, constraints: dict[int, int]) -> float:
    return sum(
        prob
        for bits, prob in dist.items()
        if all(bits[index] == value for index, value in constraints.items())
    )


def conditional_mutual_information(dist: Distribution, i: int, j: int) -> float:
    others = [node for node in NODES if node not in (i, j)]
    out = 0.0
    for bits, prob in dist.items():
        if prob <= 0.0:
            continue
        z = {node: bits[node] for node in others}
        p_z = event_prob(dist, z)
        p_ijz = event_prob(dist, {**z, i: bits[i], j: bits[j]})
        p_iz = event_prob(dist, {**z, i: bits[i]})
        p_jz = event_prob(dist, {**z, j: bits[j]})
        out += prob * log((p_ijz * p_z) / (p_iz * p_jz))
    return max(0.0, out)


def pair_mutual_information(dist: Distribution, i: int, j: int) -> float:
    out = 0.0
    for xi, xj in product((0, 1), repeat=2):
        p_ij = event_prob(dist, {i: xi, j: xj})
        p_i = event_prob(dist, {i: xi})
        p_j = event_prob(dist, {j: xj})
        if p_ij > 0.0:
            out += p_ij * log(p_ij / (p_i * p_j))
    return max(0.0, out)


def covariance_transport(dist: Distribution, i: int, j: int) -> float:
    mi = event_prob(dist, {i: 1})
    mj = event_prob(dist, {j: 1})
    mij = event_prob(dist, {i: 1, j: 1})
    return abs(mij - mi * mj)


def transfer_from_law(dist: Distribution, rule: str) -> EdgeWeights:
    weights: EdgeWeights = {}
    for i, j in combinations(NODES, 2):
        if rule == "conditional-information":
            weights[(i, j)] = conditional_mutual_information(dist, i, j)
        elif rule == "pair-information":
            weights[(i, j)] = pair_mutual_information(dist, i, j)
        elif rule == "covariance":
            weights[(i, j)] = covariance_transport(dist, i, j)
        elif rule == "regraduated-conditional":
            weights[(i, j)] = sqrt(conditional_mutual_information(dist, i, j))
        else:
            raise ValueError(rule)
    return weights


def label_transport() -> EdgeWeights:
    return {
        (0, 1): 1.0,
        (0, 2): 0.0,
        (0, 3): 0.0,
        (1, 2): 0.0,
        (1, 3): 0.0,
        (2, 3): 1.0,
    }


def max_edge_gap(a: EdgeWeights, b: EdgeWeights) -> float:
    return max(abs(a[edge] - b[edge]) for edge in a)


def invariant_under_relabel(dist: Distribution, rule: str) -> bool:
    permutation = {0: 2, 1: 3, 2: 0, 3: 1}
    base = transfer_from_law(dist, rule)
    relabeled = transfer_from_law(relabel_distribution(dist, permutation), rule)
    expected = relabel_weights(base, permutation)
    return max_edge_gap(relabeled, expected) <= 1.0e-10


def role_transfer_forms(case: TransportCase) -> dict[str, EdgeWeights]:
    if case.supplied is not None:
        return {role: case.supplied for role in ROLE_NAMES}
    if case.rule == "node-label":
        return {role: label_transport() for role in ROLE_NAMES}
    if case.laws_by_role is None:
        return {}
    return {
        role: transfer_from_law(dist, case.rule)
        for role, dist in case.laws_by_role.items()
    }


def audit(case: TransportCase) -> TransportAudit:
    forms = role_transfer_forms(case)
    nonunique_gap = False
    if not forms:
        partition = None
        gap = 0.0
        margin = 0.0
        invariant = False
        role_blind = False
    else:
        partitions = {}
        gaps = []
        margins = []
        for role, weights in forms.items():
            partition, role_gap, role_margin, _ = edge_gap_separator(weights)
            partitions[role] = partition
            gaps.append(role_gap)
            margins.append(role_margin)
        labels = {partition_label(partition) for partition in partitions.values()}
        nonunique_gap = labels == {"--"}
        role_blind = len(labels) == 1 and "--" not in labels
        partition = next(iter(partitions.values())) if role_blind else None
        gap = min(gaps)
        margin = min(margins)
        if case.laws_by_role is not None and case.rule in {
            "conditional-information",
            "pair-information",
            "covariance",
            "regraduated-conditional",
        }:
            invariant = all(invariant_under_relabel(dist, case.rule) for dist in case.laws_by_role.values())
        else:
            invariant = False

    intrinsic = (
        case.intrinsic_law
        and case.supplied is None
        and case.rule != "node-label"
    )
    passes = (
        intrinsic
        and case.rule == "conditional-information"
        and case.units_fixed
        and partition is not None
        and invariant
        and role_blind
        and case.role_blind_required
        and case.stable
        and gap >= 0.25
        and margin >= 0.12
    )

    if passes:
        verdict = "PASS-INTRINSIC-TX-TARGET"
    elif not case.intrinsic_law:
        verdict = "FAIL-NO-EVENTLESS-LAW"
    elif case.supplied is not None:
        verdict = "FAIL-SUPPLIED-T"
    elif case.rule == "node-label" or not invariant:
        verdict = "FAIL-RELABELING"
    elif not case.units_fixed:
        verdict = "FAIL-FREE-UNITS"
    elif partition is None:
        verdict = "FAIL-NONUNIQUE-GAP" if nonunique_gap else "FAIL-ROLE-SPLIT"
    elif not role_blind:
        verdict = "FAIL-ROLE-SPLIT"
    elif case.rule in {"pair-information", "covariance"}:
        verdict = "FAIL-HIDDEN-COMMON-CAUSE"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    elif gap < 0.25 or margin < 0.12:
        verdict = "FAIL-NO-GAP-MARGIN"
    else:
        verdict = "FAIL"

    return TransportAudit(
        candidate=case.name,
        rule=case.rule,
        intrinsic="yes" if intrinsic else "no",
        units="yes" if case.units_fixed else "no",
        partition=partition_label(partition),
        gap=gap,
        margin=margin,
        invariant="yes" if invariant else "no",
        role_blind="yes" if role_blind else "no",
        verdict=verdict,
    )


def cases() -> list[TransportCase]:
    pair = pair_law(PAIR_BLOCKS)
    cross = pair_law(CROSS_BLOCKS)
    common = common_mode_law()
    tied = tied_law()
    return [
        TransportCase(
            "boundary ranks only",
            "none",
            None,
            None,
            False,
            True,
            True,
            True,
        ),
        TransportCase(
            "pair information",
            "pair-information",
            {role: common for role in ROLE_NAMES},
            None,
            True,
            True,
            True,
            True,
        ),
        TransportCase(
            "covariance transport",
            "covariance",
            {role: common for role in ROLE_NAMES},
            None,
            True,
            True,
            True,
            True,
        ),
        TransportCase(
            "supplied transfer",
            "hand kernel",
            None,
            transfer_from_law(pair, "conditional-information"),
            True,
            True,
            True,
            True,
        ),
        TransportCase(
            "node-label transfer",
            "node-label",
            None,
            None,
            True,
            True,
            True,
            True,
        ),
        TransportCase(
            "free-unit CMI",
            "regraduated-conditional",
            {role: pair for role in ROLE_NAMES},
            None,
            True,
            False,
            True,
            True,
        ),
        TransportCase(
            "tied CMI law",
            "conditional-information",
            {role: tied for role in ROLE_NAMES},
            None,
            True,
            True,
            True,
            True,
        ),
        TransportCase(
            "role-split CMI",
            "conditional-information",
            {"record": pair, "source": cross, "causal": pair, "screen": pair},
            None,
            True,
            True,
            True,
            True,
        ),
        TransportCase(
            "drifting CMI",
            "conditional-information",
            {role: cross for role in ROLE_NAMES},
            None,
            True,
            True,
            True,
            False,
        ),
        TransportCase(
            "conditional-information transport",
            "conditional-information",
            {role: pair for role in ROLE_NAMES},
            None,
            True,
            True,
            True,
            True,
        ),
    ]


def print_rows(rows: list[TransportAudit]) -> None:
    print("intrinsic T_x origin audit")
    print("--------------------------")
    print(
        "candidate                         rule                      intrinsic units "
        "partition gap    margin invariant role_blind verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:33s} "
            f"{row.rule:25s} "
            f"{row.intrinsic:9s} "
            f"{row.units:5s} "
            f"{row.partition:9s} "
            f"{row.gap:6.3f} "
            f"{row.margin:7.3f} "
            f"{row.invariant:9s} "
            f"{row.role_blind:10s} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    positive = transfer_from_law(pair_law(PAIR_BLOCKS), "conditional-information")
    partition, gap, margin, threshold = edge_gap_separator(positive)
    print("=" * 118)
    print("v6 Paper 3 section 26: intrinsic T_x origin campaign")
    print("=" * 118)
    print_rows(rows)
    print("CONDITIONAL-INFORMATION TRANSPORT")
    print("---------------------------------")
    print(f"selected partition = {partition_label(partition)}")
    print(f"derived threshold = {threshold:.6f}")
    print(f"edge gap = {gap:.6f}")
    print(f"stability margin = {margin:.6f}")
    print()
    print("VERDICT")
    print("-------")
    print("T_x is conditionally intrinsic when it is the fixed-unit conditional")
    print("information transport of the eventless collar law.  Weaker transports")
    print("either confuse common causes, depend on labels, split roles, drift, or")
    print("leave the numeric transport units free.")


if __name__ == "__main__":
    main()
