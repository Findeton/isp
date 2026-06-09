"""
v6 Paper 3 section 25: intrinsic collar-separator theorem campaign.

Question:
    Does a sealed finite record diamond intrinsically determine the
    eventless collar separator R_x?

Finite answer:
    Not from generic boundary/collar data.  The finite positive theorem
    requires a specific internal datum: a role-blind collar transfer form with
    an isolated edge gap.  Then the separator is canonical:

        sort internal collar transfer weights;
        choose the unique largest gap;
        put strong edges above its midpoint;
        take connected components.

    This construction is invariant under relabeling and stable under
    perturbations smaller than the gap margin.  Boundary-only data,
    supplied thresholds, node-label cuts, gap degeneracy, role splitting, and
    refinement drift fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations


Node = int
Partition = tuple[tuple[Node, ...], ...]
EdgeWeights = dict[tuple[Node, Node], float]

NODES = (0, 1, 2, 3)
PAIR_BLOCKS: Partition = ((0, 1), (2, 3))
CROSS_BLOCKS: Partition = ((0, 2), (1, 3))
SINGLES: Partition = ((0,), (1,), (2,), (3,))
ALL: Partition = ((0, 1, 2, 3),)
ROLE_NAMES = ("record", "source", "causal", "screen")


@dataclass(frozen=True)
class SeparatorCase:
    name: str
    rule: str
    transfers: dict[str, EdgeWeights] | None
    boundary_intrinsic: bool
    transfer_intrinsic: bool
    threshold_supplied: bool
    node_label_rule: bool
    role_blind_required: bool
    stable: bool


@dataclass
class SeparatorAudit:
    candidate: str
    rule: str
    intrinsic: str
    partition: str
    gap: float
    margin: float
    invariant: str
    role_blind: str
    verdict: str


def canonical_transfer(partition: Partition, high: float = 0.82, low: float = 0.12) -> EdgeWeights:
    groups = [set(group) for group in partition]
    weights: EdgeWeights = {}
    for i, j in combinations(NODES, 2):
        same = any(i in group and j in group for group in groups)
        weights[(i, j)] = high if same else low
    return weights


def no_gap_transfer() -> EdgeWeights:
    values = (0.52, 0.51, 0.50, 0.49, 0.48, 0.47)
    return {edge: value for edge, value in zip(combinations(NODES, 2), values)}


def tied_gap_transfer() -> EdgeWeights:
    values = (0.90, 0.60, 0.60, 0.30, 0.30, 0.00)
    return {edge: value for edge, value in zip(combinations(NODES, 2), values)}


def label_rule_partition() -> Partition:
    return PAIR_BLOCKS


def normalize_partition(groups: list[list[int]]) -> Partition:
    return tuple(sorted((tuple(sorted(group)) for group in groups), key=lambda item: item[0]))


def partition_label(partition: Partition | None) -> str:
    if partition is None:
        return "--"
    return "|".join("".join(str(node) for node in group) for group in partition)


def components_from_strong_edges(strong_edges: list[tuple[int, int]]) -> Partition:
    parent = {node: node for node in NODES}

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

    for i, j in strong_edges:
        union(i, j)

    groups: dict[int, list[int]] = {}
    for node in NODES:
        groups.setdefault(find(node), []).append(node)
    return normalize_partition(list(groups.values()))


def edge_gap_separator(weights: EdgeWeights) -> tuple[Partition | None, float, float, float | None]:
    ordered = sorted(set(weights.values()))
    if len(ordered) < 2:
        return None, 0.0, 0.0, None
    gaps = [ordered[i + 1] - ordered[i] for i in range(len(ordered) - 1)]
    best = max(gaps)
    if sum(1 for gap in gaps if abs(gap - best) <= 1.0e-12) != 1:
        return None, best, best / 2.0, None
    index = gaps.index(best)
    threshold = 0.5 * (ordered[index] + ordered[index + 1])
    strong = [edge for edge, weight in weights.items() if weight > threshold]
    return components_from_strong_edges(strong), best, best / 2.0, threshold


def relabel_weights(weights: EdgeWeights, permutation: dict[int, int]) -> EdgeWeights:
    out: EdgeWeights = {}
    for (i, j), weight in weights.items():
        a = permutation[i]
        b = permutation[j]
        out[(min(a, b), max(a, b))] = weight
    return out


def relabel_partition(partition: Partition, permutation: dict[int, int]) -> Partition:
    return normalize_partition([[permutation[node] for node in group] for group in partition])


def invariant_under_relabel(weights: EdgeWeights, partition: Partition) -> bool:
    permutation = {0: 2, 1: 3, 2: 0, 3: 1}
    relabeled_weights = relabel_weights(weights, permutation)
    relabeled_partition, _, _, _ = edge_gap_separator(relabeled_weights)
    return relabeled_partition == relabel_partition(partition, permutation)


def label_rule_invariant() -> bool:
    permutation = {0: 0, 1: 2, 2: 1, 3: 3}
    return label_rule_partition() == relabel_partition(label_rule_partition(), permutation)


def role_partitions(transfers: dict[str, EdgeWeights]) -> tuple[dict[str, Partition | None], float, float]:
    partitions: dict[str, Partition | None] = {}
    gaps: list[float] = []
    margins: list[float] = []
    for role, weights in transfers.items():
        partition, gap, margin, _ = edge_gap_separator(weights)
        partitions[role] = partition
        gaps.append(gap)
        margins.append(margin)
    return partitions, min(gaps) if gaps else 0.0, min(margins) if margins else 0.0


def audit(case: SeparatorCase) -> SeparatorAudit:
    nonunique_gap = False
    if case.node_label_rule:
        partition = label_rule_partition()
        invariant = label_rule_invariant()
        role_blind = True
        gap = 0.0
        margin = 0.0
    elif case.transfers is None:
        partition = None
        invariant = False
        role_blind = False
        gap = 0.0
        margin = 0.0
    else:
        partitions, gap, margin = role_partitions(case.transfers)
        labels = {partition_label(partition) for partition in partitions.values()}
        role_blind = len(labels) == 1 and "--" not in labels
        nonunique_gap = labels == {"--"}
        partition = next(iter(partitions.values())) if role_blind else None
        first_weights = next(iter(case.transfers.values()))
        invariant = invariant_under_relabel(first_weights, partition) if partition is not None else False

    intrinsic = case.boundary_intrinsic and case.transfer_intrinsic and not case.threshold_supplied and not case.node_label_rule
    passes = (
        intrinsic
        and partition is not None
        and invariant
        and role_blind
        and case.role_blind_required
        and case.stable
        and gap >= 0.30
        and margin >= 0.15
    )

    if passes:
        verdict = "PASS-COLLAR-SEPARATOR-TARGET"
    elif not case.boundary_intrinsic:
        verdict = "FAIL-BOUNDARY-ONLY"
    elif not case.transfer_intrinsic:
        verdict = "FAIL-NO-INTRINSIC-TRANSFER"
    elif case.threshold_supplied:
        verdict = "FAIL-SUPPLIED-THRESHOLD"
    elif case.node_label_rule:
        verdict = "FAIL-RELABELING"
    elif partition is None:
        verdict = "FAIL-NONUNIQUE-GAP" if nonunique_gap else "FAIL-ROLE-SPLIT"
    elif not role_blind:
        verdict = "FAIL-ROLE-SPLIT"
    elif not invariant:
        verdict = "FAIL-RELABELING"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    elif gap < 0.30 or margin < 0.15:
        verdict = "FAIL-NO-GAP-MARGIN"
    else:
        verdict = "FAIL"

    return SeparatorAudit(
        candidate=case.name,
        rule=case.rule,
        intrinsic="yes" if intrinsic else "no",
        partition=partition_label(partition),
        gap=gap,
        margin=margin,
        invariant="yes" if invariant else "no",
        role_blind="yes" if role_blind else "no",
        verdict=verdict,
    )


def cases() -> list[SeparatorCase]:
    positive = {role: canonical_transfer(PAIR_BLOCKS) for role in ROLE_NAMES}
    role_split = {
        "record": canonical_transfer(PAIR_BLOCKS),
        "source": canonical_transfer(CROSS_BLOCKS),
        "causal": canonical_transfer(PAIR_BLOCKS),
        "screen": canonical_transfer(PAIR_BLOCKS),
    }
    no_gap = {role: no_gap_transfer() for role in ROLE_NAMES}
    tied_gap = {role: tied_gap_transfer() for role in ROLE_NAMES}
    drift = {role: canonical_transfer(CROSS_BLOCKS) for role in ROLE_NAMES}
    return [
        SeparatorCase(
            "boundary ranks only",
            "no transfer form",
            None,
            False,
            False,
            False,
            False,
            True,
            True,
        ),
        SeparatorCase(
            "collar correlations only",
            "no isolated transfer",
            no_gap,
            True,
            False,
            False,
            False,
            True,
            True,
        ),
        SeparatorCase(
            "supplied threshold",
            "hand cut level",
            positive,
            True,
            True,
            True,
            False,
            True,
            True,
        ),
        SeparatorCase(
            "node-label separator",
            "first two nodes",
            None,
            True,
            True,
            False,
            True,
            True,
            True,
        ),
        SeparatorCase(
            "tied edge gap",
            "two equal gaps",
            tied_gap,
            True,
            True,
            False,
            False,
            True,
            True,
        ),
        SeparatorCase(
            "role-split transfer",
            "four transfer forms",
            role_split,
            True,
            True,
            False,
            False,
            True,
            True,
        ),
        SeparatorCase(
            "drifting transfer",
            "not cofinal",
            drift,
            True,
            True,
            False,
            False,
            True,
            False,
        ),
        SeparatorCase(
            "intrinsic gap transfer",
            "unique edge gap",
            positive,
            True,
            True,
            False,
            False,
            True,
            True,
        ),
    ]


def print_rows(rows: list[SeparatorAudit]) -> None:
    print("intrinsic collar-separator theorem audit")
    print("----------------------------------------")
    print(
        "candidate                 rule                 intrinsic partition "
        "gap    margin invariant role_blind verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:25s} "
            f"{row.rule:20s} "
            f"{row.intrinsic:9s} "
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
    positive = canonical_transfer(PAIR_BLOCKS)
    partition, gap, margin, threshold = edge_gap_separator(positive)
    print("=" * 118)
    print("v6 Paper 3 section 25: intrinsic collar-separator theorem campaign")
    print("=" * 118)
    print_rows(rows)
    print("EDGE-GAP CONSTRUCTION")
    print("---------------------")
    print(f"selected partition = {partition_label(partition)}")
    print(f"derived threshold = {threshold:.3f}")
    print(f"edge gap = {gap:.3f}")
    print(f"stability margin = {margin:.3f}")
    print()
    print("VERDICT")
    print("-------")
    print("The collar separator is not derived from generic boundary data.  It is")
    print("conditionally derived when B_x contains a role-blind intrinsic collar")
    print("transfer form with a unique isolated edge gap.  The threshold is then")
    print("derived from the gap, not supplied.")


if __name__ == "__main__":
    main()
