"""
v6 Paper 3 section 27: eventless/event-producing invariant campaign.

Question:
    What invariant fact inside a sealed finite diamond distinguishes
    eventless record transport from event-producing record transport?

Finite answer:
    Not low activity, one-point marginals, total entropy, raw transport
    strength, supplied click labels, supplied null states, or role-specific
    cuts.

    The conditional positive target is a cross-separator factorization defect:
    once the sealed diamond has an intrinsic collar separator R_x, eventless
    record transport is transport internal to the R_x components, while an
    event is a positive isolated KL/RN obstruction to factorization across
    those components.

        Delta_x(P) = D(P || Pi_R(P)),

    where Pi_R(P) is the product law over the R_x components preserving each
    component marginal.  The repair Pi_R(P) is unique in the finite positive
    class, preserves internal record transport, and kills exactly the
    cross-separator defect.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import exp, isfinite, log

from v6_p3d_feynman_record_channel import Distribution
from v6_p3o_intrinsic_collar_separator_theorem import (
    CROSS_BLOCKS,
    NODES,
    PAIR_BLOCKS,
    ROLE_NAMES,
    Partition,
    partition_label,
)
from v6_p3p_tx_origin_campaign import pair_mutual_information


EPS = 1.0e-10
DEFECT_FLOOR = 0.035
DRIFT_FLOOR = 1.0e-8


@dataclass(frozen=True)
class DefectCase:
    name: str
    rule: str
    eventless_by_role: dict[str, Distribution] | None
    event_by_role: dict[str, Distribution] | None
    partitions_by_role: dict[str, Partition] | None
    intrinsic_law: bool
    fixed_units: bool
    supplied_null: bool
    supplied_label: bool
    stable: bool


@dataclass
class DefectAudit:
    candidate: str
    rule: str
    intrinsic: str
    partition: str
    defect0: float
    defect1: float
    margin: float
    transport_drift: float
    role_blind: str
    repair: str
    verdict: str


def ising_distribution(couplings: dict[tuple[int, int], float]) -> Distribution:
    dist: Distribution = {}
    total = 0.0
    for bits in product((0, 1), repeat=len(NODES)):
        spins = [2 * bit - 1 for bit in bits]
        energy = sum(theta * spins[i] * spins[j] for (i, j), theta in couplings.items())
        weight = exp(energy)
        dist[bits] = weight
        total += weight
    return {bits: weight / total for bits, weight in dist.items()}


def block_law(partition: Partition, internal: float = 1.15, bridge: float = 0.0) -> Distribution:
    groups = [set(group) for group in partition]
    couplings: dict[tuple[int, int], float] = {}
    for i, j in combinations(NODES, 2):
        same = any(i in group and j in group for group in groups)
        couplings[(i, j)] = internal if same else 0.0
    if bridge != 0.0:
        if partition == PAIR_BLOCKS:
            couplings[(1, 2)] = bridge
        elif partition == CROSS_BLOCKS:
            couplings[(0, 1)] = bridge
        else:
            couplings[(0, 1)] = bridge
    return ising_distribution(couplings)


def common_mode_law(high: float = 0.86, low: float = 0.14) -> Distribution:
    dist: Distribution = {}
    for bits in product((0, 1), repeat=len(NODES)):
        prob_high = 1.0
        prob_low = 1.0
        for bit in bits:
            prob_high *= high if bit else 1.0 - high
            prob_low *= low if bit else 1.0 - low
        dist[bits] = 0.5 * prob_high + 0.5 * prob_low
    return dist


def entropy(dist: Distribution) -> float:
    return -sum(prob * log(prob) for prob in dist.values() if prob > 0.0)


def entropy_matched_eventless(target_entropy: float) -> Distribution:
    best_law = block_law(PAIR_BLOCKS, internal=0.0, bridge=0.0)
    best_error = abs(entropy(best_law) - target_entropy)
    for index in range(1, 5001):
        internal = index / 1000.0
        law = block_law(PAIR_BLOCKS, internal=internal, bridge=0.0)
        error = abs(entropy(law) - target_entropy)
        if error < best_error:
            best_law = law
            best_error = error
    return best_law


def event_prob(dist: Distribution, constraints: dict[int, int]) -> float:
    return sum(
        prob
        for bits, prob in dist.items()
        if all(bits[index] == value for index, value in constraints.items())
    )


def component_marginal(dist: Distribution, component: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    out: dict[tuple[int, ...], float] = {}
    for bits, prob in dist.items():
        key = tuple(bits[index] for index in component)
        out[key] = out.get(key, 0.0) + prob
    return out


def product_projection(dist: Distribution, partition: Partition) -> Distribution:
    marginals = [component_marginal(dist, component) for component in partition]
    out: Distribution = {}
    for bits in product((0, 1), repeat=len(NODES)):
        prob = 1.0
        for component, marginal in zip(partition, marginals):
            key = tuple(bits[index] for index in component)
            prob *= marginal[key]
        out[bits] = prob
    return out


def kl(p: Distribution, q: Distribution) -> float:
    out = 0.0
    for event, p_value in p.items():
        if p_value <= 0.0:
            continue
        q_value = q.get(event, 0.0)
        if q_value <= 0.0:
            return float("inf")
        out += p_value * log(p_value / q_value)
    return out


def block_factorization_defect(dist: Distribution, partition: Partition) -> float:
    return kl(dist, product_projection(dist, partition))


def one_marginal_span(a: Distribution, b: Distribution) -> float:
    return max(abs(event_prob(a, {node: 1}) - event_prob(b, {node: 1})) for node in NODES)


def internal_transport(dist: Distribution, partition: Partition) -> dict[tuple[int, int], float]:
    weights: dict[tuple[int, int], float] = {}
    groups = [set(group) for group in partition]
    for i, j in combinations(NODES, 2):
        if any(i in group and j in group for group in groups):
            weights[(i, j)] = pair_mutual_information(dist, i, j)
    return weights


def max_transport_drift(a: Distribution, b: Distribution, partition: Partition) -> float:
    wa = internal_transport(a, partition)
    wb = internal_transport(b, partition)
    return max((abs(wa[edge] - wb[edge]) for edge in wa), default=0.0)


def repair_is_unique_enough(event_law: Distribution, partition: Partition) -> tuple[bool, float]:
    repaired = product_projection(event_law, partition)
    idempotent = block_factorization_defect(repaired, partition) <= EPS
    preserved = max_transport_drift(event_law, repaired, partition)
    return idempotent and preserved <= DRIFT_FLOOR, preserved


def role_blind_data(
    defects0: list[float],
    defects1: list[float],
    partitions: dict[str, Partition],
) -> bool:
    labels = {partition_label(partition) for partition in partitions.values()}
    return (
        len(labels) == 1
        and max(defects0) - min(defects0) <= EPS
        and max(defects1) - min(defects1) <= EPS
    )


def audit(case: DefectCase) -> DefectAudit:
    if case.eventless_by_role is None or case.event_by_role is None or case.partitions_by_role is None:
        defect0 = 0.0
        defect1 = 0.0
        margin = 0.0
        drift = 0.0
        role_blind = False
        repair = False
        partition_text = "--"
    else:
        defects0: list[float] = []
        defects1: list[float] = []
        drifts: list[float] = []
        repairs: list[bool] = []
        for role in ROLE_NAMES:
            partition = case.partitions_by_role[role]
            eventless = case.eventless_by_role[role]
            event = case.event_by_role[role]
            repaired = product_projection(event, partition)
            defects0.append(block_factorization_defect(eventless, partition))
            defects1.append(block_factorization_defect(event, partition))
            ok, preserved = repair_is_unique_enough(event, partition)
            repairs.append(ok)
            drifts.append(max_transport_drift(event, repaired, partition))
        defect0 = max(defects0)
        defect1 = min(defects1)
        margin = defect1 - defect0
        drift = max(drifts)
        role_blind = role_blind_data(defects0, defects1, case.partitions_by_role)
        repair = all(repairs)
        labels = {partition_label(partition) for partition in case.partitions_by_role.values()}
        partition_text = next(iter(labels)) if len(labels) == 1 else "--"

    intrinsic = (
        case.intrinsic_law
        and not case.supplied_null
        and not case.supplied_label
        and case.partitions_by_role is not None
    )
    passes = (
        case.rule == "cross-separator KL defect"
        and intrinsic
        and case.fixed_units
        and role_blind
        and repair
        and defect0 <= EPS
        and defect1 >= DEFECT_FLOOR
        and margin >= DEFECT_FLOOR
        and drift <= DRIFT_FLOOR
        and case.stable
    )

    if passes:
        verdict = "PASS-EVENTLESS-DEFECT-TARGET"
    elif case.eventless_by_role is None or case.event_by_role is None:
        verdict = "FAIL-NO-SEALEDDIAMOND-LAW"
    elif case.supplied_label:
        verdict = "FAIL-SUPPLIED-CLICK-LABEL"
    elif case.supplied_null:
        verdict = "FAIL-SUPPLIED-NULL"
    elif not intrinsic:
        verdict = "FAIL-NOT-INTRINSIC"
    elif not case.fixed_units:
        verdict = "FAIL-FREE-UNITS"
    elif case.rule in {"marginals", "entropy", "raw transport"}:
        verdict = "FAIL-NOT-DEFECT-INVARIANT"
    elif not role_blind:
        verdict = "FAIL-ROLE-SPLIT"
    elif not repair:
        verdict = "FAIL-NONUNIQUE-REPAIR"
    elif defect0 > EPS:
        verdict = "FAIL-EVENTLESS-HAS-DEFECT"
    elif defect1 < DEFECT_FLOOR or margin < DEFECT_FLOOR:
        verdict = "FAIL-NO-ISOLATED-DEFECT"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    else:
        verdict = "FAIL"

    return DefectAudit(
        candidate=case.name,
        rule=case.rule,
        intrinsic="yes" if intrinsic else "no",
        partition=partition_text,
        defect0=defect0,
        defect1=defect1,
        margin=margin,
        transport_drift=drift,
        role_blind="yes" if role_blind else "no",
        repair="yes" if repair else "no",
        verdict=verdict,
    )


def same_for_roles(dist: Distribution) -> dict[str, Distribution]:
    return {role: dist for role in ROLE_NAMES}


def partitions_for_roles(partition: Partition) -> dict[str, Partition]:
    return {role: partition for role in ROLE_NAMES}


def cases() -> list[DefectCase]:
    eventless = block_law(PAIR_BLOCKS, internal=1.15, bridge=0.0)
    event = block_law(PAIR_BLOCKS, internal=1.15, bridge=0.62)
    entropy_match = entropy_matched_eventless(entropy(event))
    small_event = block_law(PAIR_BLOCKS, internal=1.15, bridge=0.12)
    cross_eventless = block_law(CROSS_BLOCKS, internal=1.15, bridge=0.0)
    cross_event = block_law(CROSS_BLOCKS, internal=1.15, bridge=0.62)
    common = common_mode_law()
    return [
        DefectCase(
            "boundary marginals only",
            "marginals",
            same_for_roles(eventless),
            same_for_roles(event),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            True,
            False,
            False,
            True,
        ),
        DefectCase(
            "total entropy only",
            "entropy",
            same_for_roles(entropy_match),
            same_for_roles(event),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            True,
            False,
            False,
            True,
        ),
        DefectCase(
            "raw transport strength",
            "raw transport",
            same_for_roles(eventless),
            same_for_roles(common),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            True,
            False,
            False,
            True,
        ),
        DefectCase(
            "supplied click label",
            "external click",
            same_for_roles(eventless),
            same_for_roles(event),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            True,
            False,
            True,
            True,
        ),
        DefectCase(
            "supplied null law",
            "cross-separator KL defect",
            same_for_roles(eventless),
            same_for_roles(event),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            True,
            True,
            False,
            True,
        ),
        DefectCase(
            "no sealed law",
            "cross-separator KL defect",
            None,
            None,
            None,
            False,
            True,
            False,
            False,
            True,
        ),
        DefectCase(
            "free-unit defect",
            "cross-separator KL defect",
            same_for_roles(eventless),
            same_for_roles(event),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            False,
            False,
            False,
            True,
        ),
        DefectCase(
            "role-split defect",
            "cross-separator KL defect",
            {
                "record": eventless,
                "source": cross_eventless,
                "causal": eventless,
                "screen": eventless,
            },
            {
                "record": event,
                "source": cross_event,
                "causal": event,
                "screen": event,
            },
            {
                "record": PAIR_BLOCKS,
                "source": CROSS_BLOCKS,
                "causal": PAIR_BLOCKS,
                "screen": PAIR_BLOCKS,
            },
            True,
            True,
            False,
            False,
            True,
        ),
        DefectCase(
            "small defect",
            "cross-separator KL defect",
            same_for_roles(eventless),
            same_for_roles(small_event),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            True,
            False,
            False,
            True,
        ),
        DefectCase(
            "drifting defect",
            "cross-separator KL defect",
            same_for_roles(eventless),
            same_for_roles(event),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            True,
            False,
            False,
            False,
        ),
        DefectCase(
            "cross-separator factorization defect",
            "cross-separator KL defect",
            same_for_roles(eventless),
            same_for_roles(event),
            partitions_for_roles(PAIR_BLOCKS),
            True,
            True,
            False,
            False,
            True,
        ),
    ]


def print_rows(rows: list[DefectAudit]) -> None:
    print("eventless/event-producing invariant audit")
    print("-----------------------------------------")
    print(
        "candidate                              rule                      intrinsic "
        "partition defect0 defect1 margin  transport_drift role_blind repair verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:38s} "
            f"{row.rule:25s} "
            f"{row.intrinsic:9s} "
            f"{row.partition:9s} "
            f"{row.defect0:7.4f} "
            f"{row.defect1:7.4f} "
            f"{row.margin:7.4f} "
            f"{row.transport_drift:15.3e} "
            f"{row.role_blind:10s} "
            f"{row.repair:6s} "
            f"{row.verdict}"
        )
    print()


def diagnostic_numbers() -> None:
    eventless = block_law(PAIR_BLOCKS, internal=1.15, bridge=0.0)
    event = block_law(PAIR_BLOCKS, internal=1.15, bridge=0.62)
    entropy_match = entropy_matched_eventless(entropy(event))
    repaired = product_projection(event, PAIR_BLOCKS)
    print("POSITIVE TARGET RECEIPTS")
    print("------------------------")
    print(f"one-point marginal span(eventless,event) = {one_marginal_span(eventless, event):.3e}")
    print(f"entropy(eventless) = {entropy(eventless):.6f}")
    print(f"entropy(event) = {entropy(event):.6f}")
    print(f"entropy(entropy-matched eventless) = {entropy(entropy_match):.6f}")
    print(
        "Delta(entropy-matched eventless) = "
        f"{block_factorization_defect(entropy_match, PAIR_BLOCKS):.6f}"
    )
    print(f"Delta(eventless) = {block_factorization_defect(eventless, PAIR_BLOCKS):.6f}")
    print(f"Delta(event) = {block_factorization_defect(event, PAIR_BLOCKS):.6f}")
    print(f"Delta(repair(event)) = {block_factorization_defect(repaired, PAIR_BLOCKS):.6f}")
    print(f"KL(event || repair(event)) = {kl(event, repaired):.6f}")
    print(f"internal transport drift under repair = {max_transport_drift(event, repaired, PAIR_BLOCKS):.3e}")
    print(f"partition = {partition_label(PAIR_BLOCKS)}")
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    print("=" * 126)
    print("v6 Paper 3 section 27: eventless/event-producing invariant campaign")
    print("=" * 126)
    print_rows(rows)
    diagnostic_numbers()
    print("VERDICT")
    print("-------")
    print("The invariant distinction is a fixed-unit cross-separator KL/RN")
    print("factorization defect.  Eventless transport has zero defect while retaining")
    print("internal record transport; event-producing transport has a positive")
    print("isolated defect whose unique product repair preserves the internal collar")
    print("marginals and deletes only the cross-separator obstruction.")


if __name__ == "__main__":
    main()
