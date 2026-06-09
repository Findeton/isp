"""
v6 Paper 3 section 28: intrinsic R_x and RN-unit resolution campaign.

Question:
    Can a sealed finite diamond intrinsically supply both the collar separator
    R_x and fixed KL/RN units, rather than taking them as inputs?

Finite answer:
    Not for arbitrary sealed laws.  Symmetric/tied laws, role-split laws,
    tiny defects, drifting refinements, supplied cuts, label cuts, non-log
    scores, and local/role-dependent unit rescalings all fail.

    A positive finite class exists:

      1. Scan all nontrivial collar partitions R.
      2. For each R compute the RN/KL factorization defect

             Delta_R(P)=D(P || Pi_R(P)).

      3. If exactly one nontrivial R has Delta_R=0, the diamond is eventless
         with intrinsic separator R.
      4. If no nontrivial zero exists and exactly one R minimizes positive
         Delta_R with an isolated margin and cofinal floor, the diamond is
         event-producing with intrinsic separator R.
      5. The action unit is the log Radon-Nikodym unit: it is additive under
         sealed composition.  A global bits/nats conversion is conventional;
         local or role-dependent scales are extra physics.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import exp, log, sqrt

from v6_p3d_feynman_record_channel import Distribution
from v6_p3o_intrinsic_collar_separator_theorem import (
    CROSS_BLOCKS,
    NODES,
    PAIR_BLOCKS,
    ROLE_NAMES,
    Partition,
    partition_label,
)
from v6_p3q_eventless_defect_campaign import (
    block_factorization_defect,
    block_law,
    ising_distribution,
)


EPS = 1.0e-10
DEFECT_FLOOR = 0.035
MARGIN_FLOOR = 0.025


@dataclass(frozen=True)
class ResolutionCase:
    name: str
    rule: str
    laws_by_role: dict[str, Distribution] | None
    intrinsic_law: bool
    supplied_partition: Partition | None
    label_partition: bool
    unit_rule: str
    stable: bool


@dataclass
class ResolutionAudit:
    candidate: str
    rule: str
    intrinsic: str
    status: str
    partition: str
    defect: float
    margin: float
    unit_error: float
    unit_drift: float
    role_blind: str
    verdict: str


def normalize_partition(groups: list[list[int]]) -> Partition:
    return tuple(sorted((tuple(sorted(group)) for group in groups), key=lambda item: item[0]))


def all_partitions(items: tuple[int, ...] = NODES) -> list[Partition]:
    out: set[Partition] = set()

    def extend(index: int, labels: list[int], max_label: int) -> None:
        if index == len(items):
            groups: dict[int, list[int]] = {}
            for item, label in zip(items, labels):
                groups.setdefault(label, []).append(item)
            partition = normalize_partition(list(groups.values()))
            if len(partition) >= 2:
                out.add(partition)
            return
        for label in range(max_label + 2):
            labels.append(label)
            extend(index + 1, labels, max(max_label, label))
            labels.pop()

    extend(0, [], -1)
    return sorted(out, key=lambda part: (len(part), partition_label(part)))


PARTITIONS = all_partitions()


def coupled_pair_law(partition: Partition, bridge: float = 0.62) -> Distribution:
    return block_law(partition, internal=1.15, bridge=bridge)


def uniform_law() -> Distribution:
    return {bits: 1.0 / 16.0 for bits in product((0, 1), repeat=len(NODES))}


def tied_symmetric_law(strength: float = 0.45) -> Distribution:
    return ising_distribution({edge: strength for edge in combinations(NODES, 2)})


def defect_spectrum(dist: Distribution) -> list[tuple[float, Partition]]:
    return sorted(
        ((block_factorization_defect(dist, partition), partition) for partition in PARTITIONS),
        key=lambda item: (item[0], partition_label(item[1])),
    )


def derive_partition(dist: Distribution) -> tuple[str, Partition | None, float, float, str]:
    spectrum = defect_spectrum(dist)
    zeros = [(value, partition) for value, partition in spectrum if value <= EPS]
    positives = [(value, partition) for value, partition in spectrum if value > EPS]
    if zeros:
        if len(zeros) != 1:
            return "ambiguous-zero", None, 0.0, 0.0, "nonunique"
        margin = positives[0][0] if positives else 0.0
        return "eventless", zeros[0][1], 0.0, margin, "unique"
    if not positives:
        return "empty", None, 0.0, 0.0, "nonunique"
    best_value, best_partition = positives[0]
    tied = [partition for value, partition in positives if abs(value - best_value) <= EPS]
    if len(tied) != 1:
        return "ambiguous-positive", None, best_value, 0.0, "nonunique"
    margin = positives[1][0] - best_value if len(positives) > 1 else best_value
    return "event", best_partition, best_value, margin, "unique"


def phi(value: float, unit_rule: str) -> float:
    if unit_rule in {"rn-log", "global-bits"}:
        scale = 1.0 / log(2.0) if unit_rule == "global-bits" else 1.0
        return scale * value
    if unit_rule == "sqrt-score":
        return sqrt(max(0.0, value))
    if unit_rule == "local-scale":
        return 1.7 * value
    if unit_rule == "role-scale":
        return value
    raise ValueError(unit_rule)


def unit_chain_error(value: float, unit_rule: str) -> float:
    left = 0.63 * value + 0.041
    right = 0.37 * value + 0.019
    return abs(phi(left + right, unit_rule) - phi(left, unit_rule) - phi(right, unit_rule))


def unit_drift(unit_rule: str) -> float:
    if unit_rule == "local-scale":
        return 0.70
    if unit_rule == "role-scale":
        return 0.45
    return 0.0


def role_unit_blind(unit_rule: str) -> bool:
    return unit_rule != "role-scale"


def audit(case: ResolutionCase) -> ResolutionAudit:
    if case.laws_by_role is None:
        status = "none"
        partition = None
        defect = 0.0
        margin = 0.0
        role_blind = False
    elif case.supplied_partition is not None:
        status = "supplied"
        partition = case.supplied_partition
        defect = min(block_factorization_defect(law, partition) for law in case.laws_by_role.values())
        margin = 0.0
        role_blind = True
    elif case.label_partition:
        status = "label"
        partition = PAIR_BLOCKS
        defect = min(block_factorization_defect(law, partition) for law in case.laws_by_role.values())
        margin = 0.0
        role_blind = True
    else:
        derived = {role: derive_partition(law) for role, law in case.laws_by_role.items()}
        labels = {partition_label(data[1]) for data in derived.values()}
        statuses = {data[0] for data in derived.values()}
        role_blind = len(labels) == 1 and len(statuses) == 1 and "--" not in labels
        if role_blind:
            first = next(iter(derived.values()))
            status, partition, defect, margin, _ = first
        else:
            status = next(iter(statuses)) if len(statuses) == 1 else "--"
            partition = None
            defect = min((data[2] for data in derived.values()), default=0.0)
            margin = min((data[3] for data in derived.values()), default=0.0)

    intrinsic = (
        case.intrinsic_law
        and case.laws_by_role is not None
        and case.supplied_partition is None
        and not case.label_partition
    )
    unit_error = unit_chain_error(defect, case.unit_rule)
    drift = unit_drift(case.unit_rule)
    role_blind = role_blind and role_unit_blind(case.unit_rule)

    unit_ok = (
        case.unit_rule in {"rn-log", "global-bits"}
        and unit_error <= EPS
        and drift <= EPS
        and role_unit_blind(case.unit_rule)
    )
    event_ok = (
        status == "event"
        and defect >= DEFECT_FLOOR
        and margin >= MARGIN_FLOOR
    )
    eventless_ok = status == "eventless" and margin >= MARGIN_FLOOR
    passes = intrinsic and unit_ok and role_blind and case.stable and (event_ok or eventless_ok)

    if passes and status == "event":
        verdict = (
            "PASS-INTRINSIC-RX-RN"
            if case.unit_rule == "rn-log"
            else "PASS-GLOBAL-CONVENTION"
        )
    elif passes and status == "eventless":
        verdict = "PASS-EVENTLESS-RX"
    elif case.laws_by_role is None:
        verdict = "FAIL-NO-SEALEDDIAMOND-LAW"
    elif case.supplied_partition is not None:
        verdict = "FAIL-SUPPLIED-RX"
    elif case.label_partition:
        verdict = "FAIL-RELABELING"
    elif not intrinsic:
        verdict = "FAIL-NOT-INTRINSIC"
    elif case.unit_rule == "sqrt-score":
        verdict = "FAIL-NONADDITIVE-SCORE"
    elif case.unit_rule in {"local-scale", "role-scale"}:
        verdict = "FAIL-FREE-RN-UNIT"
    elif status.startswith("ambiguous"):
        verdict = "FAIL-NONUNIQUE-RX"
    elif not role_blind:
        verdict = "FAIL-ROLE-SPLIT"
    elif status == "event" and defect < DEFECT_FLOOR:
        verdict = "FAIL-NO-SOURCE-FLOOR"
    elif status == "event" and margin < MARGIN_FLOOR:
        verdict = "FAIL-NO-ISOLATED-MINIMUM"
    elif status == "eventless" and margin < MARGIN_FLOOR:
        verdict = "FAIL-DEGENERATE-EVENTLESS"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    else:
        verdict = "FAIL"

    return ResolutionAudit(
        candidate=case.name,
        rule=case.rule,
        intrinsic="yes" if intrinsic else "no",
        status=status,
        partition=partition_label(partition),
        defect=defect,
        margin=margin,
        unit_error=unit_error,
        unit_drift=drift,
        role_blind="yes" if role_blind else "no",
        verdict=verdict,
    )


def same_for_roles(dist: Distribution) -> dict[str, Distribution]:
    return {role: dist for role in ROLE_NAMES}


def cases() -> list[ResolutionCase]:
    eventless = block_law(PAIR_BLOCKS, internal=1.15, bridge=0.0)
    event = coupled_pair_law(PAIR_BLOCKS, bridge=0.62)
    small_event = coupled_pair_law(PAIR_BLOCKS, bridge=0.12)
    symmetric = tied_symmetric_law()
    return [
        ResolutionCase(
            "order/counts only",
            "no probability law",
            None,
            False,
            None,
            False,
            "rn-log",
            True,
        ),
        ResolutionCase(
            "supplied separator",
            "hand R_x",
            same_for_roles(event),
            True,
            PAIR_BLOCKS,
            False,
            "rn-log",
            True,
        ),
        ResolutionCase(
            "node-label separator",
            "label R_x",
            same_for_roles(event),
            True,
            None,
            True,
            "rn-log",
            True,
        ),
        ResolutionCase(
            "eventless factorization",
            "zero RN defect scan",
            same_for_roles(eventless),
            True,
            None,
            False,
            "rn-log",
            True,
        ),
        ResolutionCase(
            "fully independent collar",
            "zero RN defect scan",
            same_for_roles(uniform_law()),
            True,
            None,
            False,
            "rn-log",
            True,
        ),
        ResolutionCase(
            "symmetric tied law",
            "minimum RN defect scan",
            same_for_roles(symmetric),
            True,
            None,
            False,
            "rn-log",
            True,
        ),
        ResolutionCase(
            "role-split minimum",
            "minimum RN defect scan",
            {
                "record": event,
                "source": coupled_pair_law(CROSS_BLOCKS, bridge=0.62),
                "causal": event,
                "screen": event,
            },
            True,
            None,
            False,
            "rn-log",
            True,
        ),
        ResolutionCase(
            "small positive minimum",
            "minimum RN defect scan",
            same_for_roles(small_event),
            True,
            None,
            False,
            "rn-log",
            True,
        ),
        ResolutionCase(
            "drifting minimum",
            "minimum RN defect scan",
            same_for_roles(event),
            True,
            None,
            False,
            "rn-log",
            False,
        ),
        ResolutionCase(
            "sqrt regraduation",
            "minimum defect scan",
            same_for_roles(event),
            True,
            None,
            False,
            "sqrt-score",
            True,
        ),
        ResolutionCase(
            "local RN rescale",
            "minimum defect scan",
            same_for_roles(event),
            True,
            None,
            False,
            "local-scale",
            True,
        ),
        ResolutionCase(
            "role RN rescale",
            "minimum defect scan",
            same_for_roles(event),
            True,
            None,
            False,
            "role-scale",
            True,
        ),
        ResolutionCase(
            "global bits convention",
            "minimum RN defect scan",
            same_for_roles(event),
            True,
            None,
            False,
            "global-bits",
            True,
        ),
        ResolutionCase(
            "minimum positive RN defect",
            "minimum RN defect scan",
            same_for_roles(event),
            True,
            None,
            False,
            "rn-log",
            True,
        ),
    ]


def print_rows(rows: list[ResolutionAudit]) -> None:
    print("intrinsic R_x and RN-unit resolution audit")
    print("------------------------------------------")
    print(
        "candidate                    rule                    intrinsic status      "
        "partition defect margin unit_error unit_drift role_blind verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:28s} "
            f"{row.rule:23s} "
            f"{row.intrinsic:9s} "
            f"{row.status:11s} "
            f"{row.partition:9s} "
            f"{row.defect:6.4f} "
            f"{row.margin:6.4f} "
            f"{row.unit_error:10.3e} "
            f"{row.unit_drift:10.3e} "
            f"{row.role_blind:10s} "
            f"{row.verdict}"
        )
    print()


def diagnostic_numbers() -> None:
    event = coupled_pair_law(PAIR_BLOCKS, bridge=0.62)
    status, partition, defect, margin, _ = derive_partition(event)
    spectrum = defect_spectrum(event)[:5]
    print("POSITIVE TARGET RECEIPTS")
    print("------------------------")
    print(f"derived status = {status}")
    print(f"derived partition = {partition_label(partition)}")
    print(f"minimum RN defect = {defect:.6f}")
    print(f"isolation margin = {margin:.6f}")
    print("lowest five partition defects:")
    for value, part in spectrum:
        print(f"  {partition_label(part):7s} {value:.6f}")
    print(f"RN chain error = {unit_chain_error(defect, 'rn-log'):.3e}")
    print(f"sqrt-score chain error = {unit_chain_error(defect, 'sqrt-score'):.3e}")
    print("global bits/nats conversion is additive but not a local physical parameter.")
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    print("=" * 124)
    print("v6 Paper 3 section 28: intrinsic R_x and RN-unit resolution campaign")
    print("=" * 124)
    print_rows(rows)
    diagnostic_numbers()
    print("VERDICT")
    print("-------")
    print("R_x and the RN unit are derived in the positive finite class by scanning")
    print("all nontrivial partitions and selecting the unique zero or minimum")
    print("positive log-RN factorization defect.  This is not universal: tied,")
    print("degenerate, role-split, tiny-defect, drifting, supplied-cut, and free-unit")
    print("diamonds remain explicit branch-B or no-event cases.")


if __name__ == "__main__":
    main()
