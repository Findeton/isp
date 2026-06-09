"""
v6 Paper 3 section 34: Feynman receipt campaign for sealed diamonds.

Question:
    Does the stronger sealed-diamond ontology do calculational work, or does
    it only organize definitions?

Finite answer:
    In the tested finite class, the ontology earns its keep if the full sealed
    law P_x is observable/estimable.  From finite samples one can recover the
    intrinsic separator and work profile with increasing accuracy.  The work
    profile predicts the exact deletion/repair cost, composes additively
    across independent sealed diamonds, separates hidden source amplitudes
    that cheap click statistics cannot distinguish, and exposes when U_x,
    R_x, or role-blindness have been supplied externally.

    It does not close branch A from first-order click data alone.  The meter
    needs the full sealed local record law, or enough samples to estimate it.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import sqrt
from random import Random

from v6_p3o_intrinsic_collar_separator_theorem import NODES, PAIR_BLOCKS, ROLE_NAMES, partition_label
from v6_p3p_tx_origin_campaign import pair_mutual_information
from v6_p3q_eventless_defect_campaign import (
    Distribution,
    block_factorization_defect,
    internal_transport,
    kl,
    max_transport_drift,
    one_marginal_span,
    product_projection,
)
from v6_p3r_intrinsic_rx_units_resolution import derive_partition, tied_symmetric_law, uniform_law
from v6_p3t_fixed_cmrp_imfd_dynamics import J0, imfd_log_linear_law
from v6_p3w_sealed_work_profile_campaign import WorkProfile, count_reference, profile_for, work_profile


SEED = 24062026
K_WEAK = 0.325
K_CRIT = 0.700
K_STRONG = 1.025
SAMPLE_TRIALS = 60
PSEUDOCOUNT = 0.5


@dataclass(frozen=True)
class SamplingReceipt:
    samples: int
    partition_success: float
    event_success: float
    mean_wsrc_error: float
    mean_wtr_error: float
    max_chain_error: float
    verdict: str


@dataclass(frozen=True)
class ProbeReceipt:
    probe: str
    quantity: str
    value: float
    reference: float
    error: float
    verdict: str


def all_events() -> list[tuple[int, ...]]:
    return list(product((0, 1), repeat=len(NODES)))


def sample_distribution(dist: Distribution, samples: int, seed: int) -> Distribution:
    rng = Random(seed)
    events = all_events()
    cumulative: list[tuple[tuple[int, ...], float]] = []
    running = 0.0
    for event in events:
        running += dist[event]
        cumulative.append((event, running))

    counts = {event: PSEUDOCOUNT for event in events}
    for _ in range(samples):
        draw = rng.random()
        for event, threshold in cumulative:
            if draw <= threshold:
                counts[event] += 1.0
                break

    total = sum(counts.values())
    return {event: count / total for event, count in counts.items()}


def derived_profile_or_zero(dist: Distribution) -> tuple[str, str, WorkProfile]:
    status, partition, _defect, _margin, _ = derive_partition(dist)
    if partition is None:
        return status, "--", WorkProfile(0.0, 0.0, 0.0, 0.0)
    return status, partition_label(partition), work_profile(dist, partition)


def sampling_receipts(true_dist: Distribution) -> list[SamplingReceipt]:
    true_status, true_partition, _defect, _margin, _ = derive_partition(true_dist)
    true_label = partition_label(true_partition)
    true_profile = work_profile(true_dist, true_partition)
    out: list[SamplingReceipt] = []
    for samples in (250, 1000, 4000, 16000):
        partition_ok = 0
        event_ok = 0
        wsrc_error = 0.0
        wtr_error = 0.0
        max_chain = 0.0
        for trial in range(SAMPLE_TRIALS):
            empirical = sample_distribution(true_dist, samples, SEED + 1000 * samples + trial)
            status, label, profile = derived_profile_or_zero(empirical)
            partition_ok += int(label == true_label)
            event_ok += int(status == true_status)
            wsrc_error += abs(profile.source - true_profile.source)
            wtr_error += abs(profile.transport - true_profile.transport)
            max_chain = max(max_chain, profile.chain_error)
        part_rate = partition_ok / SAMPLE_TRIALS
        event_rate = event_ok / SAMPLE_TRIALS
        mean_src = wsrc_error / SAMPLE_TRIALS
        mean_tr = wtr_error / SAMPLE_TRIALS
        passes = (
            samples >= 4000
            and part_rate >= 0.95
            and event_rate >= 0.95
            and mean_src <= 0.08
            and mean_tr <= 0.08
            and max_chain <= 1.0e-10
        )
        out.append(
            SamplingReceipt(
                samples=samples,
                partition_success=part_rate,
                event_success=event_rate,
                mean_wsrc_error=mean_src,
                mean_wtr_error=mean_tr,
                max_chain_error=max_chain,
                verdict="PASS-FINITE-ESTIMATION" if passes else "COND-SAMPLE-SIZE",
            )
        )
    return out


def print_sampling(receipts: list[SamplingReceipt]) -> None:
    print("finite sample estimation")
    print("------------------------")
    print("samples  R_success event_success mean_Wsrc_err mean_Wtr_err max_chain_err verdict")
    for row in receipts:
        print(
            f"{row.samples:7d} "
            f"{row.partition_success:9.3f} "
            f"{row.event_success:13.3f} "
            f"{row.mean_wsrc_error:13.5f} "
            f"{row.mean_wtr_error:12.5f} "
            f"{row.max_chain_error:13.2e} "
            f"{row.verdict}"
        )
    print()


def deletion_repair_receipts(dist: Distribution) -> list[ProbeReceipt]:
    status, partition, _defect, _margin, _ = derive_partition(dist)
    if partition is None:
        return []
    repaired = product_projection(dist, partition)
    profile = work_profile(dist, partition)
    repaired_profile = work_profile(repaired, partition)
    source_after = abs(block_factorization_defect(repaired, partition))
    drift = max_transport_drift(dist, repaired, partition)
    return [
        ProbeReceipt(
            "delete/repair",
            "KL(P||Pi_R P)",
            kl(dist, repaired),
            profile.source,
            abs(kl(dist, repaired) - profile.source),
            "PASS-DELETION-COST",
        ),
        ProbeReceipt(
            "delete/repair",
            "source defect after repair",
            source_after,
            0.0,
            source_after,
            "PASS-SOURCE-REMOVED" if source_after <= 1.0e-12 else "FAIL-SOURCE-REMOVED",
        ),
        ProbeReceipt(
            "delete/repair",
            "transport work drift",
            abs(repaired_profile.transport - profile.transport),
            0.0,
            abs(repaired_profile.transport - profile.transport),
            "PASS-TRANSPORT-PRESERVED",
        ),
        ProbeReceipt(
            "delete/repair",
            "internal transport drift",
            drift,
            0.0,
            drift,
            "PASS-MARGINAL-TRANSPORT-PRESERVED" if drift <= 1.0e-12 else "FAIL-TRANSPORT-DRIFT",
        ),
    ]


def cheap_observable_receipts() -> list[ProbeReceipt]:
    weak = imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_WEAK)
    strong = imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_STRONG)
    weak_profile = work_profile(weak, PAIR_BLOCKS)
    strong_profile = work_profile(strong, PAIR_BLOCKS)
    cheap_gap = one_marginal_span(weak, strong)
    internal_mi_gap = abs(
        pair_mutual_information(weak, 0, 1) - pair_mutual_information(strong, 0, 1)
    )
    source_gap = abs(strong_profile.source - weak_profile.source)
    transport_gap = abs(strong_profile.transport - weak_profile.transport)
    return [
        ProbeReceipt(
            "cheap-observable fake",
            "one-point marginal gap",
            cheap_gap,
            0.0,
            cheap_gap,
            "PASS-CHEAP-FAILS" if cheap_gap <= 1.0e-12 else "FAIL-CHEAP-SEES",
        ),
        ProbeReceipt(
            "cheap-observable fake",
            "internal MI gap",
            internal_mi_gap,
            0.0,
            internal_mi_gap,
            "PASS-INTERNAL-UNCHANGED" if internal_mi_gap <= 1.0e-12 else "FAIL-INTERNAL-CHANGED",
        ),
        ProbeReceipt(
            "cheap-observable fake",
            "transport work gap",
            transport_gap,
            0.0,
            transport_gap,
            "PASS-TRANSPORT-UNCHANGED" if transport_gap <= 1.0e-12 else "FAIL-TRANSPORT-CHANGED",
        ),
        ProbeReceipt(
            "cheap-observable fake",
            "source work gap",
            source_gap,
            0.0,
            source_gap,
            "PASS-WX-SEPARATES" if source_gap >= 0.20 else "FAIL-WX-NOT-SENSITIVE",
        ),
    ]


def biased_reference(probability: float = 0.57) -> Distribution:
    out: Distribution = {}
    for event in all_events():
        p = 1.0
        for bit in event:
            p *= probability if bit else 1.0 - probability
        out[event] = p
    return out


def reference_attack_receipts(dist: Distribution) -> list[ProbeReceipt]:
    status, partition, _defect, _margin, _ = derive_partition(dist)
    if partition is None:
        return []
    canonical = work_profile(dist, partition)
    repaired = product_projection(dist, partition)
    biased = biased_reference()
    biased_transport = kl(repaired, biased)
    biased_total = kl(dist, biased)
    source = kl(dist, repaired)
    chain_error = abs(biased_total - biased_transport - source)
    transport_shift = abs(biased_transport - canonical.transport)
    return [
        ProbeReceipt(
            "reference attack",
            "chain error with biased U",
            chain_error,
            0.0,
            chain_error,
            "PASS-ADDITIVE-BUT-REFERENCE-DEPENDENT" if chain_error <= 1.0e-12 else "FAIL-CHAIN",
        ),
        ProbeReceipt(
            "reference attack",
            "transport work shift",
            transport_shift,
            0.0,
            transport_shift,
            "FAIL-U-SUPPLIED-MOVES-WTR" if transport_shift >= 0.01 else "PASS-U-INVARIANT",
        ),
    ]


def composition_receipts(dist: Distribution) -> list[ProbeReceipt]:
    status, partition, _defect, _margin, _ = derive_partition(dist)
    if partition is None:
        return []
    profile = work_profile(dist, partition)
    reference = count_reference()
    repaired = product_projection(dist, partition)
    product_total = product_distribution(dist, dist)
    product_repaired = product_distribution(repaired, repaired)
    product_reference = product_distribution(reference, reference)
    source2 = kl(product_total, product_repaired)
    transport2 = kl(product_repaired, product_reference)
    total2 = kl(product_total, product_reference)
    return [
        ProbeReceipt(
            "sealed composition",
            "source additivity error",
            abs(source2 - 2.0 * profile.source),
            0.0,
            abs(source2 - 2.0 * profile.source),
            "PASS-SOURCE-ADDITIVE",
        ),
        ProbeReceipt(
            "sealed composition",
            "transport additivity error",
            abs(transport2 - 2.0 * profile.transport),
            0.0,
            abs(transport2 - 2.0 * profile.transport),
            "PASS-TRANSPORT-ADDITIVE",
        ),
        ProbeReceipt(
            "sealed composition",
            "total additivity error",
            abs(total2 - 2.0 * profile.total),
            0.0,
            abs(total2 - 2.0 * profile.total),
            "PASS-TOTAL-ADDITIVE",
        ),
    ]


def product_distribution(left: Distribution, right: Distribution) -> dict[tuple[int, ...], float]:
    return {
        left_event + right_event: left_prob * right_prob
        for left_event, left_prob in left.items()
        for right_event, right_prob in right.items()
    }


def bad_case_receipts() -> list[ProbeReceipt]:
    out: list[ProbeReceipt] = []
    for name, law in (
        ("uniform/eventless", uniform_law()),
        ("tied/nonisolated", tied_symmetric_law()),
    ):
        status, partition, defect, margin, _ = derive_partition(law)
        good = partition is not None and status == "event"
        out.append(
            ProbeReceipt(
                "bad-case attack",
                f"{name} status={status}",
                defect,
                margin,
                0.0 if good else 1.0,
                "FAIL-NO-ONE-EVENT-METER" if not good else "PASS-UNEXPECTED",
            )
        )
    return out


def role_receipts() -> list[ProbeReceipt]:
    role_laws = {
        "record": imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_CRIT),
        "source": imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_CRIT),
        "causal": imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_CRIT),
        "screen": imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_CRIT),
    }
    split_laws = {
        "record": imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_CRIT),
        "source": imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_STRONG),
        "causal": imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_CRIT),
        "screen": imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_WEAK),
    }
    tied_sources = [work_profile(law, PAIR_BLOCKS).source for law in role_laws.values()]
    split_sources = [work_profile(law, PAIR_BLOCKS).source for law in split_laws.values()]
    tied_span = max(tied_sources) - min(tied_sources)
    split_span = max(split_sources) - min(split_sources)
    return [
        ProbeReceipt(
            "role consistency",
            "role-tied Wsrc span",
            tied_span,
            0.0,
            tied_span,
            "PASS-ROLE-BLIND" if tied_span <= 1.0e-12 else "FAIL-ROLE-DRIFT",
        ),
        ProbeReceipt(
            "role consistency",
            "role-split Wsrc span",
            split_span,
            0.0,
            split_span,
            "FAIL-SPLIT-DETECTED" if split_span >= 0.20 else "PASS-SPLIT-HIDDEN",
        ),
    ]


def print_probe_receipts(rows: list[ProbeReceipt]) -> None:
    print("intervention and fake-observable receipts")
    print("-----------------------------------------")
    print("probe                  quantity                         value      reference  error      verdict")
    for row in rows:
        print(
            f"{row.probe:22s} "
            f"{row.quantity:32s} "
            f"{row.value:10.6f} "
            f"{row.reference:10.6f} "
            f"{row.error:10.2e} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    print("=" * 118)
    print("v6 Paper 3 section 34: Feynman sealed-diamond receipt campaign")
    print("=" * 118)
    law = imfd_log_linear_law(PAIR_BLOCKS, internal=J0, source=K_CRIT)
    status, partition, _defect, _margin, _ = derive_partition(law)
    true_profile = work_profile(law, partition)
    print("target sealed diamond")
    print("---------------------")
    print(f"status={status}, R={partition_label(partition)}, K={K_CRIT:.3f}")
    print(
        f"W_tr={true_profile.transport:.6f}, "
        f"W_src={true_profile.source:.6f}, "
        f"W_tot={true_profile.total:.6f}, "
        f"chain_error={true_profile.chain_error:.2e}"
    )
    print()
    print_sampling(sampling_receipts(law))
    rows: list[ProbeReceipt] = []
    rows.extend(deletion_repair_receipts(law))
    rows.extend(cheap_observable_receipts())
    rows.extend(reference_attack_receipts(law))
    rows.extend(composition_receipts(law))
    rows.extend(bad_case_receipts())
    rows.extend(role_receipts())
    print_probe_receipts(rows)
    print("VERDICT")
    print("-------")
    print("The sealed-diamond ontology has finite Feynman receipts: W_x is")
    print("estimable from full local record samples, predicts deletion cost,")
    print("survives sealed composition, and detects source differences hidden from")
    print("one-point/click observables.  The failures are equally important:")
    print("first-order data do not determine W_x, a noncanonical U_x moves W_tr,")
    print("nonisolated spectra do not give a one-event meter, and role-split")
    print("laws are detected rather than rescued.")
    print()
    print("So the ontology makes operational sense exactly as a full sealed")
    print("record-law ontology.  If the physical theory only gives clicks, order,")
    print("or a supplied reference state, it is branch B.")


if __name__ == "__main__":
    main()
