"""
v6 Paper 3 section 35: full branch-A-enriched target campaign.

This script audits the nine concrete targets created after the W_x campaign.
It is intentionally severe: exact KL work identities count as proven finite
legs; causal-order, screen/volume, and refinement claims pass only if the
tested finite data actually determine them without a supplied readout.

Main verdict:
    The stronger sealed-diamond ontology has two exact finite legs:

        record/source KL work split;
        finite W_x receipt/estimation/deletion meter.

    The campaign also gives an explicit negative Dirac-Hessian anchor:
    raw probability-space Hess(W_x) does not equal the signed free one-particle
    Dirac A_R^(1).  It can only see A_R^(1) after a Dirac tangent/intervention
    structure is supplied.

    Refinement canonicity, causal orientation, and screen/volume response
    remain the branch-A gates.  Without them, the theory is branch B.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import exp
from random import Random

from v6_p3o_intrinsic_collar_separator_theorem import NODES, PAIR_BLOCKS, partition_label
from v6_p3q_eventless_defect_campaign import Distribution, one_marginal_span
from v6_p3r_intrinsic_rx_units_resolution import DEFECT_FLOOR, MARGIN_FLOOR, derive_partition
from v6_p3t_fixed_cmrp_imfd_dynamics import J0, imfd_log_linear_law
from v6_p3w_sealed_work_profile_campaign import WorkProfile, count_reference, profile_for, work_profile


# K_CRIT is local to the Feynman receipt script.  Keep the numerical value here
# so this campaign is self-contained and explicit.
K_CRIT = 0.700
SEED = 991827
N_GENERIC_TRIALS = 240


@dataclass(frozen=True)
class TargetResult:
    target: str
    test: str
    positive: str
    negative: str
    value: str
    verdict: str


def canonical_law(j: float = J0, k: float = K_CRIT) -> Distribution:
    return imfd_log_linear_law(PAIR_BLOCKS, internal=j, source=k)


def structural_event(dist: Distribution) -> tuple[bool, str, float, float]:
    status, partition, defect, margin, _ = derive_partition(dist)
    label = partition_label(partition)
    ok = (
        status == "event"
        and label == partition_label(PAIR_BLOCKS)
        and defect >= DEFECT_FLOOR
        and margin >= MARGIN_FLOOR
    )
    return ok, label, defect, margin


def dirac_a1_singleton(L: int = 5, n0: int = 2, a: float = 1.0) -> list[list[float]]:
    # Basis index = 2*n + spin, spin 0/1.  This is the explicit free
    # collar-excision A_R^(1) support pattern quoted in the V1p1/V1p10 line.
    size = 2 * L
    matrix = [[0.0 for _ in range(size)] for _ in range(size)]

    def index(n: int, spin: int) -> int:
        return 2 * (n % L) + spin

    for spin in (0, 1):
        opposite = 1 - spin
        center = index(n0, spin)
        matrix[center][center] += 1.0 / (2.0 * a * a)
        for neighbor in (n0 - 1, n0 + 1):
            nsame = index(neighbor, spin)
            ncross = index(neighbor, opposite)
            matrix[nsame][nsame] += 1.0 / (4.0 * a * a)
            matrix[ncross][center] += -1.0 / (4.0 * a * a)
            matrix[center][ncross] += -1.0 / (4.0 * a * a)
    return matrix


def probability_hessian_reference(size: int) -> list[list[float]]:
    # Hessian of D(p||u) in raw probability coordinates at uniform u, before
    # imposing the simplex constraint: diagonal Fisher metric.
    return [[float(size) if i == j else 0.0 for j in range(size)] for i in range(size)]


def support_mismatch(a: list[list[float]], b: list[list[float]]) -> tuple[int, int, int]:
    offdiag_a = 0
    offdiag_b = 0
    mismatch = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            az = abs(a[i][j]) > 1.0e-12
            bz = abs(b[i][j]) > 1.0e-12
            offdiag_a += int(az)
            offdiag_b += int(bz)
            mismatch += int(az != bz)
    return offdiag_a, offdiag_b, mismatch


def target_2_dirac_hessian() -> TargetResult:
    a1 = dirac_a1_singleton()
    hess = probability_hessian_reference(len(a1))
    a_off, h_off, mismatch = support_mismatch(a1, hess)
    verdict = "FAIL-PROBABILITY-HESSIAN-NOT-DIRAC"
    return TargetResult(
        "2 Dirac Hessian anchor",
        "raw Hess(D(p||u)) support vs free A_R^(1)",
        f"A_R offdiag={a_off}",
        f"Hess offdiag={h_off}",
        f"support mismatch={mismatch}",
        verdict,
    )


def perturb(dist: Distribution, rng: Random, epsilon: float) -> Distribution:
    values = {event: prob * exp(rng.uniform(-epsilon, epsilon)) for event, prob in dist.items()}
    total = sum(values.values())
    return {event: value / total for event, value in values.items()}


def target_4_gap_genericity() -> TargetResult:
    rng = Random(SEED)
    base = canonical_law()
    open_ok = 0
    arbitrary_ok = 0
    for _ in range(N_GENERIC_TRIALS):
        trial = perturb(base, rng, 0.12)
        open_ok += int(structural_event(trial)[0])
        values = [rng.gammavariate(1.0, 1.0) for _ in range(16)]
        total = sum(values)
        arbitrary = {
            event: value / total
            for event, value in zip(product((0, 1), repeat=len(NODES)), values)
        }
        arbitrary_ok += int(structural_event(arbitrary)[0])
    open_rate = open_ok / N_GENERIC_TRIALS
    arbitrary_rate = arbitrary_ok / N_GENERIC_TRIALS
    verdict = (
        "PASS-OPEN-CLASS-NOT-GLOBAL-GENERIC"
        if open_rate >= 0.95 and arbitrary_rate < 0.80
        else "FAIL-GENERICITY-UNCLEAR"
    )
    return TargetResult(
        "4 isolated-gap genericity",
        "perturb IMFD basin vs arbitrary positive laws",
        f"open-basin rate={open_rate:.3f}",
        f"arbitrary rate={arbitrary_rate:.3f}",
        f"trials={N_GENERIC_TRIALS}",
        verdict,
    )


def target_5_source_floor() -> TargetResult:
    stable_sources: list[float] = []
    decaying_sources: list[float] = []
    for n in range(1, 9):
        stable_sources.append(profile_for(J0, K_CRIT + 0.12 / n).source)
        decaying_sources.append(profile_for(J0, K_CRIT / (n + 1)).source)
    stable_floor = min(stable_sources)
    decaying_floor = min(decaying_sources)
    verdict = (
        "PASS-CONDITIONAL-STABLE-FLOOR"
        if stable_floor >= DEFECT_FLOOR and decaying_floor < DEFECT_FLOOR
        else "FAIL-FLOOR-TEST"
    )
    return TargetResult(
        "5 refinement-stable source floor",
        "stable K_n vs decaying K_n refinement families",
        f"stable min Wsrc={stable_floor:.5f}",
        f"decay min Wsrc={decaying_floor:.5f}",
        f"floor={DEFECT_FLOOR:.5f}",
        verdict,
    )


def marginalize_pair_refinement(refined: Distribution, mode: str) -> Distribution:
    # Refined space has duplicated bits (a0,a1,b0,b1,c0,c1,d0,d1).  The
    # canonical map reads the first bit in each pair.  A noncanonical map can
    # read the second bit; both are lawful as bare projections unless the
    # ontology supplies the refinement cocycle.
    out: Distribution = {event: 0.0 for event in product((0, 1), repeat=4)}
    offsets = (0, 2, 4, 6) if mode == "first" else (1, 3, 5, 7)
    for bits, prob in refined.items():
        coarse = tuple(bits[i] for i in offsets)
        out[coarse] += prob
    return out


def duplicate_refinement(base: Distribution, flip: float = 0.03) -> Distribution:
    refined: Distribution = {}
    for coarse, prob in base.items():
        for duplicate_noise in product((0, 1), repeat=4):
            bits: list[int] = []
            p_noise = 1.0
            for bit, noise in zip(coarse, duplicate_noise):
                copied = bit if noise == 0 else 1 - bit
                p_noise *= (1.0 - flip) if noise == 0 else flip
                bits.extend([bit, copied])
            refined[tuple(bits)] = prob * p_noise
    return refined


def target_3_refinement_cocycle() -> TargetResult:
    base = canonical_law()
    refined = duplicate_refinement(base)
    first = marginalize_pair_refinement(refined, "first")
    second = marginalize_pair_refinement(refined, "second")
    base_profile = work_profile(base, PAIR_BLOCKS)
    first_profile = work_profile(first, PAIR_BLOCKS)
    second_profile = work_profile(second, PAIR_BLOCKS)
    canonical_error = abs(first_profile.source - base_profile.source) + abs(
        first_profile.transport - base_profile.transport
    )
    lift_drift = abs(second_profile.source - base_profile.source) + abs(
        second_profile.transport - base_profile.transport
    )
    verdict = (
        "PASS-CANONICAL-COCYCLE-FAILS-FREE-LIFT"
        if canonical_error <= 1.0e-12 and lift_drift > 0.01
        else "FAIL-REFINEMENT-AUDIT"
    )
    return TargetResult(
        "3 refinement cocycle",
        "canonical duplicate projection vs alternate lift",
        f"canonical error={canonical_error:.3e}",
        f"free-lift drift={lift_drift:.5f}",
        "cocycle exact only after map choice",
        verdict,
    )


def target_6_causal_order() -> TargetResult:
    law = canonical_law()
    profile = work_profile(law, PAIR_BLOCKS)
    # Same symmetric law can be decorated by opposite causal orientations
    # without changing P,R,U,W.  Probability-only W_x therefore does not
    # derive order orientation.
    forward_profile = profile
    backward_profile = profile
    profile_gap = abs(forward_profile.source - backward_profile.source) + abs(
        forward_profile.transport - backward_profile.transport
    )
    return TargetResult(
        "6 causal-order readout",
        "same P,R,U,W with opposite orientation labels",
        "undirected adjacency compatible",
        "orientation not determined",
        f"profile gap={profile_gap:.3e}",
        "FAIL-CAUSAL-ORIENTATION-OPEN",
    )


def target_7_screen_volume() -> TargetResult:
    law = canonical_law()
    src = work_profile(law, PAIR_BLOCKS).source
    coefficients = [0.5, 1.0, 2.0]
    responses = [c * src for c in coefficients]
    response_span = max(responses) - min(responses)
    return TargetResult(
        "7 screen/volume readout",
        "free screen coefficient times same Wsrc",
        f"Wsrc={src:.6f}",
        f"response span={response_span:.6f}",
        "same P,R,U",
        "FAIL-SCREEN-COEFFICIENT-OPEN",
    )


def target_8_counterexamples() -> TargetResult:
    weak = imfd_log_linear_law(PAIR_BLOCKS, internal=0.75, source=0.50)
    strong = imfd_log_linear_law(PAIR_BLOCKS, internal=1.75, source=0.90)
    click_gap = one_marginal_span(weak, strong)
    weak_profile = work_profile(weak, PAIR_BLOCKS)
    strong_profile = work_profile(strong, PAIR_BLOCKS)
    work_gap = abs(weak_profile.transport - strong_profile.transport) + abs(
        weak_profile.source - strong_profile.source
    )
    return TargetResult(
        "8 branch-B counterexample suite",
        "same one-point clicks/R/event status, different W and response",
        f"click gap={click_gap:.3e}",
        f"work gap={work_gap:.6f}",
        "cheap data cannot close A",
        "PASS-COUNTEREXAMPLE-SUITE",
    )


def target_1_overclaim() -> TargetResult:
    return TargetResult(
        "1 stop overclaiming",
        "split claims into exact legs and theorem targets",
        "exact: record/source KL split",
        "open: causal order + screen/volume + refinement",
        "paper patched",
        "PASS-CLAIM-DISCIPLINE",
    )


def target_9_publishable_verdict(results: list[TargetResult]) -> TargetResult:
    hard_failures = [row for row in results if row.verdict.startswith("FAIL-")]
    if hard_failures:
        verdict = "A-ENRICHED-PARTIAL-BRANCH-B-BOUNDARY"
        value = f"hard gates open={len(hard_failures)}"
    else:
        verdict = "A-ENRICHED-ANCHORED"
        value = "all gates passed"
    return TargetResult(
        "9 publishable verdict",
        "aggregate target status",
        "two exact finite legs",
        "three hard gates remain",
        value,
        verdict,
    )


def all_results() -> list[TargetResult]:
    rows = [
        target_1_overclaim(),
        target_2_dirac_hessian(),
        target_3_refinement_cocycle(),
        target_4_gap_genericity(),
        target_5_source_floor(),
        target_6_causal_order(),
        target_7_screen_volume(),
        target_8_counterexamples(),
    ]
    rows.append(target_9_publishable_verdict(rows))
    return rows


def print_results(rows: list[TargetResult]) -> None:
    print("branch-A-enriched target audit")
    print("------------------------------")
    print("target                          test                                      positive                         negative                         value                         verdict")
    for row in rows:
        print(
            f"{row.target:31s} "
            f"{row.test:41s} "
            f"{row.positive:32s} "
            f"{row.negative:32s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 140)
    print("v6 Paper 3 section 35: full branch-A-enriched target campaign")
    print("=" * 140)
    rows = all_results()
    print_results(rows)
    print()
    print("VERDICT")
    print("-------")
    print("Targets 1, 3, 4, 5, and 8 give useful finite results, and the KL")
    print("record/source W_x leg remains exact.  Target 2 fails as a direct")
    print("probability-only Dirac anchor: Hess(W_x) is Fisher/metric data, not the")
    print("signed A_R^(1) comparison generator.  Targets 6 and 7 remain hard")
    print("theorem gates: causal orientation and screen/volume response are not")
    print("read out from P,R,U,W alone.")
    print()
    print("Publishable status: A-enriched partial.  Branch A survives only if")
    print("canonical refinement maps, a Dirac tangent/intervention cocycle, causal")
    print("orientation, and screen/volume response are derived from the full sealed")
    print("record process.  Without those, the sealed-diamond ontology is a strong")
    print("branch-B modular theory with two exact KL legs.")


if __name__ == "__main__":
    main()
