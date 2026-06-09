"""
v6 Paper 3 section 30: fixed CMRP dynamics for IMFDs.

Question:
    Can we exhibit a fixed CMRP dynamics whose stable local diamonds are
    isolated modular factorization defects, rather than imposing IMFD as an
    admissibility axiom?

Finite answer:
    Yes, conditionally and constructively, in a finite toy class.

    The fixed dynamics is a spectrum-flow CMRP:

        1. Given a sealed law P, compute the intrinsic RN partition spectrum.
        2. If it has a unique minimizer R(P), use that R(P) internally.
        3. Flow to a fixed log-linear record law E_R(J0, K0) with fixed
           internal transport J0 and fixed source-defect amplitude K0.
        4. Copy the same law to record/source/causal/screen readouts.

    No separator, threshold, source amplitude, or unit is chosen per event.
    The stable fixed points of this finite map are IMFDs.

    This is not a proof that established ISP dynamics has this form.  It is a
    finite existence theorem for a branch-A-enriched CMRP dynamics and an
    attack surface for the physical theorem still missing.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import exp, log, sqrt
from random import Random

from v6_p3d_feynman_record_channel import Distribution
from v6_p3o_intrinsic_collar_separator_theorem import (
    CROSS_BLOCKS,
    NODES,
    PAIR_BLOCKS,
    ROLE_NAMES,
    Partition,
    partition_label,
)
from v6_p3q_eventless_defect_campaign import block_law, ising_distribution
from v6_p3r_intrinsic_rx_units_resolution import (
    DEFECT_FLOOR,
    MARGIN_FLOOR,
    derive_partition,
    tied_symmetric_law,
    uniform_law,
    unit_chain_error,
)


J0 = 1.15
K0 = 0.62
WEAK_K = 0.12
SEED = 8675309
N_STABILITY = 180


@dataclass(frozen=True)
class DynamicsCase:
    name: str
    rule: str
    seed_by_role: dict[str, Distribution] | None
    source_amplitude: float
    fixed_source: bool
    role_tied_output: bool
    supplied_partition: Partition | None
    unit_rule: str
    refinement: str
    intrinsic_law: bool


@dataclass
class DynamicsAudit:
    candidate: str
    rule: str
    intrinsic: str
    partition: str
    defect: float
    margin: float
    role_blind: str
    stable: float
    fixed: str
    unit_ok: str
    verdict: str


def bridge_for_partition(partition: Partition) -> tuple[int, int]:
    if len(partition) < 2:
        raise ValueError("need at least two blocks")
    return min((min(a), min(b)) for a, b in combinations(partition, 2))


def imfd_log_linear_law(partition: Partition, internal: float = J0, source: float = K0) -> Distribution:
    groups = [set(group) for group in partition]
    bridge = bridge_for_partition(partition)
    couplings: dict[tuple[int, int], float] = {}
    for i, j in combinations(NODES, 2):
        same = any(i in group and j in group for group in groups)
        couplings[(i, j)] = internal if same else 0.0
    couplings[(min(bridge), max(bridge))] = source
    return ising_distribution(couplings)


def pair_seed() -> Distribution:
    return block_law(PAIR_BLOCKS, internal=J0, bridge=K0)


def cross_seed() -> Distribution:
    return block_law(CROSS_BLOCKS, internal=J0, bridge=K0)


def random_distribution(rng: Random) -> Distribution:
    values = [rng.gammavariate(1.0, 1.0) for _ in range(16)]
    total = sum(values)
    return {
        bits: value / total
        for bits, value in zip(product((0, 1), repeat=4), values)
    }


def perturb_distribution(rng: Random, dist: Distribution, epsilon: float) -> Distribution:
    keys = list(dist)
    values = [dist[key] * exp(rng.uniform(-epsilon, epsilon)) for key in keys]
    total = sum(values)
    return {key: value / total for key, value in zip(keys, values)}


def spectrum_flow(seed: Distribution, source: float, supplied: Partition | None) -> tuple[str, Partition | None, Distribution | None]:
    if supplied is not None:
        return "supplied", supplied, imfd_log_linear_law(supplied, source=source)
    status, partition, _defect, _margin, _ = derive_partition(seed)
    if partition is None or status.startswith("ambiguous"):
        return status, None, None
    return status, partition, imfd_log_linear_law(partition, source=source)


def run_case(case: DynamicsCase) -> tuple[dict[str, Distribution], dict[str, str], dict[str, Partition | None]]:
    if case.seed_by_role is None:
        return {}, {}, {}
    laws: dict[str, Distribution] = {}
    statuses: dict[str, str] = {}
    partitions: dict[str, Partition | None] = {}
    first_law: Distribution | None = None
    first_partition: Partition | None = None
    first_status = ""
    for role in ROLE_NAMES:
        status, partition, law = spectrum_flow(
            case.seed_by_role[role],
            case.source_amplitude,
            case.supplied_partition,
        )
        statuses[role] = status
        partitions[role] = partition
        if law is None:
            continue
        if case.role_tied_output:
            if first_law is None:
                first_law = law
                first_partition = partition
                first_status = status
            laws[role] = first_law
            statuses[role] = first_status
            partitions[role] = first_partition
        else:
            laws[role] = law
    return laws, statuses, partitions


def law_quality(law: Distribution) -> tuple[str, Partition | None, float, float]:
    status, partition, defect, margin, _ = derive_partition(law)
    return status, partition, defect, margin


def unit_ok(unit_rule: str, defect: float) -> bool:
    if unit_rule == "rn-log":
        return unit_chain_error(defect, "rn-log") <= 1.0e-10
    if unit_rule == "global-bits":
        return unit_chain_error(defect, "global-bits") <= 1.0e-10
    if unit_rule == "sqrt-score":
        return unit_chain_error(defect, "sqrt-score") <= 1.0e-10
    return False


def stable_rate(law: Distribution | None, partition: Partition | None, refinement: str) -> float:
    if law is None or partition is None:
        return 0.0
    if refinement == "stable":
        epsilon = 0.08
    elif refinement == "large":
        epsilon = 0.80
    elif refinement == "drift":
        rng = Random(SEED + 701)
        ok = 0
        label = partition_label(partition)
        for _ in range(N_STABILITY):
            status, trial_partition, defect, margin, _ = derive_partition(random_distribution(rng))
            ok += int(
                status == "event"
                and partition_label(trial_partition) == label
                and defect >= DEFECT_FLOOR
                and margin >= MARGIN_FLOOR
            )
        return ok / N_STABILITY
    else:
        epsilon = 0.0
    rng = Random(SEED + int(1000 * epsilon))
    ok = 0
    label = partition_label(partition)
    for _ in range(N_STABILITY):
        trial = perturb_distribution(rng, law, epsilon)
        status, trial_partition, defect, margin, _ = derive_partition(trial)
        ok += int(
            status == "event"
            and partition_label(trial_partition) == label
            and defect >= DEFECT_FLOOR
            and margin >= MARGIN_FLOOR
        )
    return ok / N_STABILITY


def audit(case: DynamicsCase) -> DynamicsAudit:
    laws, statuses, partitions = run_case(case)
    if not laws:
        role_blind = False
        stable = 0.0
        defect = 0.0
        margin = 0.0
        partition = None
    else:
        qualities = {role: law_quality(law) for role, law in laws.items()}
        labels = {partition_label(data[1]) for data in qualities.values()}
        role_blind = len(laws) == len(ROLE_NAMES) and len(labels) == 1 and "--" not in labels
        if role_blind:
            status, partition, defect, margin = next(iter(qualities.values()))
            stable = stable_rate(next(iter(laws.values())), partition, case.refinement)
        else:
            partition = None
            defect = min((data[2] for data in qualities.values()), default=0.0)
            margin = min((data[3] for data in qualities.values()), default=0.0)
            stable = 0.0

    intrinsic = (
        case.intrinsic_law
        and case.seed_by_role is not None
        and case.supplied_partition is None
    )
    fixed = case.fixed_source
    unit = unit_ok(case.unit_rule, defect)
    source_floor = defect >= DEFECT_FLOOR and margin >= MARGIN_FLOOR
    passes = (
        case.rule == "spectrum-flow CMRP"
        and intrinsic
        and role_blind
        and stable >= 0.99
        and fixed
        and unit
        and source_floor
    )

    if passes:
        verdict = "PASS-FIXED-CMRP-IMFD"
    elif case.seed_by_role is None:
        verdict = "FAIL-NO-SEALEDDIAMOND-LAW"
    elif case.supplied_partition is not None:
        verdict = "FAIL-SUPPLIED-RX"
    elif not intrinsic:
        verdict = "FAIL-NOT-INTRINSIC"
    elif not laws:
        verdict = "FAIL-NONUNIQUE-RX"
    elif not role_blind:
        verdict = "FAIL-ROLE-SPLIT"
    elif not fixed:
        verdict = "FAIL-FREE-SOURCE-AMPLITUDE"
    elif not source_floor:
        verdict = "FAIL-NO-SOURCE-FLOOR"
    elif not unit:
        verdict = "FAIL-NONADDITIVE-UNIT"
    elif stable < 0.99:
        verdict = "FAIL-NO-COFINAL-STABILITY"
    else:
        verdict = "FAIL"

    return DynamicsAudit(
        candidate=case.name,
        rule=case.rule,
        intrinsic="yes" if intrinsic else "no",
        partition=partition_label(partition),
        defect=defect,
        margin=margin,
        role_blind="yes" if role_blind else "no",
        stable=stable,
        fixed="yes" if fixed else "no",
        unit_ok="yes" if unit else "no",
        verdict=verdict,
    )


def same_roles(dist: Distribution) -> dict[str, Distribution]:
    return {role: dist for role in ROLE_NAMES}


def cases() -> list[DynamicsCase]:
    pair = pair_seed()
    return [
        DynamicsCase(
            "no probability dynamics",
            "order/counts",
            None,
            K0,
            True,
            True,
            None,
            "rn-log",
            "stable",
            False,
        ),
        DynamicsCase(
            "independent Markov collar",
            "spectrum-flow CMRP",
            same_roles(uniform_law()),
            K0,
            True,
            True,
            None,
            "rn-log",
            "stable",
            True,
        ),
        DynamicsCase(
            "exchangeable dynamics",
            "spectrum-flow CMRP",
            same_roles(tied_symmetric_law()),
            K0,
            True,
            True,
            None,
            "rn-log",
            "stable",
            True,
        ),
        DynamicsCase(
            "supplied-R flow",
            "spectrum-flow CMRP",
            same_roles(pair),
            K0,
            True,
            True,
            PAIR_BLOCKS,
            "rn-log",
            "stable",
            True,
        ),
        DynamicsCase(
            "free-source flow",
            "spectrum-flow CMRP",
            same_roles(pair),
            0.74,
            False,
            True,
            None,
            "rn-log",
            "stable",
            True,
        ),
        DynamicsCase(
            "weak-source flow",
            "spectrum-flow CMRP",
            same_roles(pair),
            WEAK_K,
            True,
            True,
            None,
            "rn-log",
            "stable",
            True,
        ),
        DynamicsCase(
            "role-split flow",
            "spectrum-flow CMRP",
            {
                "record": pair_seed(),
                "source": cross_seed(),
                "causal": pair_seed(),
                "screen": pair_seed(),
            },
            K0,
            True,
            False,
            None,
            "rn-log",
            "stable",
            True,
        ),
        DynamicsCase(
            "drifting refinement flow",
            "spectrum-flow CMRP",
            same_roles(pair),
            K0,
            True,
            True,
            None,
            "rn-log",
            "drift",
            True,
        ),
        DynamicsCase(
            "sqrt-action flow",
            "spectrum-flow CMRP",
            same_roles(pair),
            K0,
            True,
            True,
            None,
            "sqrt-score",
            "stable",
            True,
        ),
        DynamicsCase(
            "large-noise flow",
            "spectrum-flow CMRP",
            same_roles(pair),
            K0,
            True,
            True,
            None,
            "rn-log",
            "large",
            True,
        ),
        DynamicsCase(
            "fixed spectrum-flow CMRP",
            "spectrum-flow CMRP",
            same_roles(pair),
            K0,
            True,
            True,
            None,
            "rn-log",
            "stable",
            True,
        ),
    ]


def print_rows(rows: list[DynamicsAudit]) -> None:
    print("fixed CMRP -> IMFD dynamics audit")
    print("---------------------------------")
    print(
        "candidate                  rule               intrinsic partition defect "
        "margin role stable fixed unit verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:26s} "
            f"{row.rule:18s} "
            f"{row.intrinsic:9s} "
            f"{row.partition:9s} "
            f"{row.defect:6.4f} "
            f"{row.margin:6.4f} "
            f"{row.role_blind:4s} "
            f"{row.stable:6.3f} "
            f"{row.fixed:5s} "
            f"{row.unit_ok:4s} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    positive = next(row for row in rows if row.verdict == "PASS-FIXED-CMRP-IMFD")
    print("=" * 118)
    print("v6 Paper 3 section 30: fixed CMRP dynamics for IMFDs")
    print("=" * 118)
    print_rows(rows)
    print("POSITIVE DYNAMICS")
    print("-----------------")
    print("Phi(P): derive R(P) from the RN partition spectrum, then flow to the")
    print("fixed log-linear law E_R(J0,K0) with J0=1.15 and K0=0.62.")
    print(f"derived partition = {positive.partition}")
    print(f"RN defect = {positive.defect:.6f}")
    print(f"isolation margin = {positive.margin:.6f}")
    print(f"stability rate = {positive.stable:.3f}")
    print(f"log-RN chain error = {unit_chain_error(positive.defect, 'rn-log'):.3e}")
    print()
    print("VERDICT")
    print("-------")
    print("A fixed finite spectrum-flow CMRP can have stable IMFD diamonds without")
    print("supplying R_x, the source amplitude, or the action unit per event.  This")
    print("is an existence theorem for the enriched ontology, not yet a derivation")
    print("from established ISP dynamics.")


if __name__ == "__main__":
    main()
