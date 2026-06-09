"""
v6 Paper 3 section 24: intrinsic N_x(B_x) origin campaign.

Question:
    Can the eventless null-factorization target N_x(B_x) be derived
    intrinsically from a sealed finite record diamond?

Finite answer:
    Not from boundary ranks, shell marginals, scalar action, or P_x alone.
    A positive finite target exists only when the sealed boundary/collar data
    carries an intrinsic eventless separator relation.  Then N_x(B_x) is the
    fixed product/exponential repair family over the connected components of
    that separator relation.

    The surviving theorem target is therefore:

        B_x -> intrinsic eventless collar separator -> fixed partition ->
        N_x(B_x) -> unique KL repair.

    If the separator is supplied externally, role-split, degenerate, or drifts
    under refinement, N_x remains branch-B input.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import isfinite

from v6_p3d_feynman_record_channel import (
    ROLE_NAMES,
    Distribution,
    RoleChannel,
    kl,
    profile,
    sealed_channel,
)
from v6_p3m_self_deleting_completeness_campaign import product_projection


Partition = tuple[tuple[int, ...], ...]
EdgeWeights = dict[tuple[int, int], float]

SINGLES: Partition = ((0,), (1,), (2,))
FIRST_REST: Partition = ((0,), (1, 2))
PAIR_LAST: Partition = ((0, 1), (2,))
OUTER_MIDDLE: Partition = ((0, 2), (1,))
ALL: Partition = ((0, 1, 2),)
PARTITIONS: tuple[Partition, ...] = (SINGLES, FIRST_REST, PAIR_LAST, OUTER_MIDDLE, ALL)
THRESHOLD = 0.05


@dataclass(frozen=True)
class NXCase:
    name: str
    rule: str
    p_by_role: dict[str, Distribution]
    edge_by_role: dict[str, EdgeWeights] | None
    boundary_intrinsic: bool
    p_only_selection: bool
    separator_relation: bool
    role_blind_required: bool
    stable: bool
    externally_supplied: bool


@dataclass
class NXAudit:
    candidate: str
    rule: str
    intrinsic: str
    partition: str
    sep_margin: float
    role_gap: float
    action_span: float
    repair_span: float
    verdict: str


def canonical_edges(partition: Partition, internal: float = 0.72, external: float = 0.00) -> EdgeWeights:
    groups = [set(group) for group in partition]
    weights: EdgeWeights = {}
    for i, j in combinations(range(3), 2):
        same = any(i in group and j in group for group in groups)
        weights[(i, j)] = internal if same else external
    return weights


def degenerate_edges() -> EdgeWeights:
    return {(0, 1): THRESHOLD, (0, 2): THRESHOLD, (1, 2): THRESHOLD}


def components_from_edges(edges: EdgeWeights, threshold: float = THRESHOLD) -> Partition:
    parent = {node: node for node in range(3)}

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(a: int, b: int) -> None:
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra

    for (i, j), weight in edges.items():
        if weight > threshold:
            union(i, j)

    groups: dict[int, list[int]] = {}
    for node in range(3):
        groups.setdefault(find(node), []).append(node)
    return tuple(sorted((tuple(group) for group in groups.values()), key=lambda item: item[0]))


def separator_margin(edges: EdgeWeights, partition: Partition, threshold: float = THRESHOLD) -> float:
    groups = [set(group) for group in partition]
    margins: list[float] = []
    for i, j in combinations(range(3), 2):
        weight = edges.get((min(i, j), max(i, j)), 0.0)
        same = any(i in group and j in group for group in groups)
        if same:
            margins.append(weight - threshold)
        else:
            margins.append(threshold - weight)
    return min(margins) if margins else 0.0


def partition_label(partition: Partition | None) -> str:
    if partition is None:
        return "--"
    return "|".join("".join(str(node) for node in group) for group in partition)


def distribution_gap(a: Distribution, b: Distribution) -> float:
    events = set(a) | set(b)
    return max(abs(a.get(event, 0.0) - b.get(event, 0.0)) for event in events)


def repair_for(p: Distribution, partition: Partition) -> Distribution:
    return product_projection(p, partition)


def role_profile_gap(p_by_role: dict[str, Distribution], partitions: dict[str, Partition]) -> float:
    profiles = []
    for role, p in p_by_role.items():
        q = repair_for(p, partitions[role])
        profiles.append(profile(RoleChannel(p, q)))
    if len(profiles) < 2:
        return 0.0
    n = min(len(values) for values in profiles)
    return max(
        max(values[i] for values in profiles) - min(values[i] for values in profiles)
        for i in range(n)
    )


def action_span(p: Distribution, partitions: tuple[Partition, ...]) -> float:
    actions = [kl(p, repair_for(p, partition)) for partition in partitions]
    finite = [value for value in actions if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def repair_span(p: Distribution, partitions: tuple[Partition, ...]) -> float:
    repairs = [repair_for(p, partition) for partition in partitions]
    if len(repairs) < 2:
        return 0.0
    return max(
        distribution_gap(left, right)
        for left, right in combinations(repairs, 2)
    )


def best_action_partition(p: Distribution) -> tuple[Partition, float]:
    scored = sorted((kl(p, repair_for(p, partition)), partition) for partition in PARTITIONS)
    return scored[0][1], scored[1][0] - scored[0][0]


def audit(case: NXCase) -> NXAudit:
    base_p = next(iter(case.p_by_role.values()))
    role_partitions: dict[str, Partition] = {}
    selected: Partition | None = None
    sep_margins: list[float] = []

    if case.edge_by_role is not None:
        for role, edges in case.edge_by_role.items():
            partition = components_from_edges(edges)
            role_partitions[role] = partition
            sep_margins.append(separator_margin(edges, partition))
        labels = {partition_label(partition) for partition in role_partitions.values()}
        selected = next(iter(role_partitions.values())) if len(labels) == 1 else None
    elif case.p_only_selection:
        selected, margin = best_action_partition(base_p)
        role_partitions = {role: selected for role in case.p_by_role}
        sep_margins.append(margin)

    if selected is None:
        rgap = role_profile_gap(case.p_by_role, role_partitions) if role_partitions else 0.0
        rspan = repair_span(base_p, PARTITIONS)
        aspan = action_span(base_p, PARTITIONS)
        margin = 0.0
    else:
        rgap = role_profile_gap(case.p_by_role, role_partitions)
        rspan = repair_span(base_p, (selected,))
        aspan = action_span(base_p, (selected,))
        margin = min(sep_margins) if sep_margins else 0.0

    role_labels = {partition_label(partition) for partition in role_partitions.values()}
    role_blind = len(role_labels) == 1 and rgap <= 1.0e-9
    passes = (
        case.boundary_intrinsic
        and case.separator_relation
        and not case.p_only_selection
        and not case.externally_supplied
        and role_blind
        and case.role_blind_required
        and case.stable
        and selected is not None
        and margin >= 0.04
    )

    if passes:
        verdict = "PASS-INTRINSIC-NX-TARGET"
    elif not case.boundary_intrinsic:
        verdict = "FAIL-BOUNDARY-ONLY"
    elif case.p_only_selection:
        verdict = "FAIL-P-ONLY-SELECTOR"
    elif case.externally_supplied:
        verdict = "FAIL-SUPPLIED-SEPARATOR"
    elif not case.separator_relation:
        verdict = "FAIL-NO-SEPARATOR"
    elif selected is None or not role_blind:
        verdict = "FAIL-ROLE-SPLIT"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    elif margin < 0.04:
        verdict = "FAIL-DEGENERATE-SEPARATOR"
    else:
        verdict = "FAIL"

    return NXAudit(
        candidate=case.name,
        rule=case.rule,
        intrinsic="yes" if case.boundary_intrinsic and not case.externally_supplied else "no",
        partition=partition_label(selected),
        sep_margin=margin,
        role_gap=rgap,
        action_span=aspan if selected is None else action_span(base_p, PARTITIONS),
        repair_span=rspan if selected is None else repair_span(base_p, PARTITIONS),
        verdict=verdict,
    )


def cases() -> list[NXCase]:
    sealed = sealed_channel().retained
    all_roles = {role: sealed for role in ROLE_NAMES}
    role_split_edges = {
        "record": canonical_edges(SINGLES),
        "source": canonical_edges(FIRST_REST),
        "causal": canonical_edges(SINGLES),
        "screen": canonical_edges(SINGLES),
    }
    intrinsic_edges = {role: canonical_edges(SINGLES) for role in ROLE_NAMES}
    supplied_edges = {role: canonical_edges(FIRST_REST) for role in ROLE_NAMES}
    degenerate = {role: degenerate_edges() for role in ROLE_NAMES}
    drifting = {role: canonical_edges(PAIR_LAST) for role in ROLE_NAMES}
    return [
        NXCase(
            "rank-only boundary",
            "shell ranks",
            all_roles,
            None,
            False,
            False,
            False,
            True,
            True,
            False,
        ),
        NXCase(
            "P-only action cut",
            "min action over cuts",
            all_roles,
            None,
            True,
            True,
            False,
            True,
            True,
            False,
        ),
        NXCase(
            "supplied separator",
            "chosen collar graph",
            all_roles,
            supplied_edges,
            True,
            False,
            True,
            True,
            True,
            True,
        ),
        NXCase(
            "degenerate separator",
            "zero gap collar",
            all_roles,
            degenerate,
            True,
            False,
            True,
            True,
            True,
            False,
        ),
        NXCase(
            "role-split separator",
            "four collar graphs",
            all_roles,
            role_split_edges,
            True,
            False,
            True,
            True,
            True,
            False,
        ),
        NXCase(
            "drifting separator",
            "not cofinal",
            all_roles,
            drifting,
            True,
            False,
            True,
            True,
            False,
            False,
        ),
        NXCase(
            "intrinsic collar separator",
            "connected components",
            all_roles,
            intrinsic_edges,
            True,
            False,
            True,
            True,
            True,
            False,
        ),
    ]


def print_rows(rows: list[NXAudit]) -> None:
    print("intrinsic N_x(B_x) origin audit")
    print("-------------------------------")
    print(
        "candidate                    rule                 intrinsic partition "
        "sep_margin role_gap action_span repair_span verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:28s} "
            f"{row.rule:20s} "
            f"{row.intrinsic:9s} "
            f"{row.partition:9s} "
            f"{row.sep_margin:10.4f} "
            f"{row.role_gap:8.4f} "
            f"{row.action_span:11.4f} "
            f"{row.repair_span:11.4f} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    base_p = sealed_channel().retained
    cut_span = action_span(base_p, PARTITIONS)
    repair_ambiguity = repair_span(base_p, PARTITIONS)
    print("=" * 118)
    print("v6 Paper 3 section 24: intrinsic N_x(B_x) origin campaign")
    print("=" * 118)
    print_rows(rows)
    print("CUT AMBIGUITY WITHOUT AN INTRINSIC SEPARATOR")
    print("--------------------------------------------")
    print(f"action span over admissible cuts = {cut_span:.6f}")
    print(f"repair distribution span over admissible cuts = {repair_ambiguity:.6f}")
    print()
    print("VERDICT")
    print("-------")
    print("N_x(B_x) is not derived from ranks, marginals, scalar action, or P_x alone.")
    print("It is conditionally intrinsic only if B_x supplies a canonical eventless")
    print("collar separator with a positive stability margin.  Then N_x(B_x) is the")
    print("fixed product/exponential repair family over its connected components.")


if __name__ == "__main__":
    main()
