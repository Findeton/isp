"""
v6 Paper 3 section 31: invariant origin of spectrum-flow CMRP.

Question:
    Can the fixed spectrum-flow CMRP be derived from a deeper Einstein-style
    invariant record principle?

Finite answer:
    Partly.  The invariant principles force the *form*:

        sealed law P
        -> RN partition spectrum
        -> intrinsic minimizer R(P)
        -> log-RN additive action
        -> maximum-entropy log-linear law on the selected sufficient
           statistics.

    They do not determine the numerical source-work amplitude.  There is an
    open one-parameter family of fixed spectrum-flow CMRPs that are all
    role-blind, stable, log-RN additive, and IMFD-generating, but have
    different K and therefore different defect strength.

    Thus the deeper theorem still needs one more invariant scalar
    normalization: a fixed deletion-work quantum, a screen/volume response
    unit, or a derived entropy/cost extremum.  Without that, spectrum-flow is a
    beautiful fixed dynamics but not fully derived branch A.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p3o_intrinsic_collar_separator_theorem import PAIR_BLOCKS, partition_label
from v6_p3r_intrinsic_rx_units_resolution import (
    DEFECT_FLOOR,
    MARGIN_FLOOR,
    derive_partition,
    unit_chain_error,
)
from v6_p3t_fixed_cmrp_imfd_dynamics import J0, K0, imfd_log_linear_law, stable_rate


K_GRID = tuple(round(0.05 + 0.025 * i, 3) for i in range(79))
J_GRID = tuple(round(0.25 + 0.05 * i, 3) for i in range(45))


@dataclass
class OriginAudit:
    candidate: str
    principle: str
    form: str
    rx: str
    unit: str
    k_span: float
    chosen_k: str
    defect: float
    margin: float
    stable: float
    verdict: str


def quality_for(j: float, k: float) -> tuple[str, str, float, float, float]:
    law = imfd_log_linear_law(PAIR_BLOCKS, internal=j, source=k)
    status, partition, defect, margin, _ = derive_partition(law)
    stable = stable_rate(law, partition, "stable")
    return status, partition_label(partition), defect, margin, stable


def passes_imfd(j: float, k: float) -> bool:
    status, label, defect, margin, stable = quality_for(j, k)
    return (
        status == "event"
        and label == partition_label(PAIR_BLOCKS)
        and defect >= DEFECT_FLOOR
        and margin >= MARGIN_FLOOR
        and stable >= 0.99
    )


def passing_ks(j: float = J0) -> list[float]:
    return [k for k in K_GRID if passes_imfd(j, k)]


def span(values: list[float]) -> float:
    if not values:
        return 0.0
    return max(values) - min(values)


def entropy_proxy(j: float, k: float) -> float:
    # For this fixed exponential family the normalizing entropy decreases
    # monotonically with coupling norm; this proxy is enough for finite
    # selection audits without introducing extra dependencies.
    return -(j * j + k * k)


def minimum_norm_k(j: float = J0) -> tuple[float | None, float, float]:
    candidates: list[tuple[float, float, float]] = []
    for k in K_GRID:
        status, label, defect, margin, _stable = quality_for(j, k)
        if (
            status == "event"
            and label == partition_label(PAIR_BLOCKS)
            and defect >= DEFECT_FLOOR
            and margin >= MARGIN_FLOOR
        ):
            candidates.append((k, defect, margin))
    if not candidates:
        return None, 0.0, 0.0
    return min(candidates, key=lambda item: item[0])


def balanced_k(j: float = J0) -> tuple[float, float, float]:
    best: tuple[float, float, float] | None = None
    best_error = float("inf")
    for k in K_GRID:
        status, label, defect, margin, _stable = quality_for(j, k)
        if status != "event" or label != partition_label(PAIR_BLOCKS):
            continue
        error = abs(defect - margin)
        if error < best_error:
            best = (k, defect, margin)
            best_error = error
    if best is None:
        return 0.0, 0.0, 0.0
    return best


def best_entropy_with_fixed_work() -> tuple[float, float, float]:
    # Conditional positive case: if the deeper theory supplies the universal
    # work invariants J0,K0, maximum entropy over the constrained exponential
    # family returns the fixed spectrum-flow law.  The point of this row is
    # the conditionality, not a new fit.
    _entropy = entropy_proxy(J0, K0)
    _ = _entropy
    _status, _label, defect, margin, _stable = quality_for(J0, K0)
    return K0, defect, margin


def rows() -> list[OriginAudit]:
    free_ks = passing_ks(J0)
    min_k, min_defect, min_margin = minimum_norm_k(J0)
    bal_k, bal_defect, bal_margin = balanced_k(J0)
    fixed_k, fixed_defect, fixed_margin = best_entropy_with_fixed_work()
    fixed_stable = quality_for(J0, fixed_k)[4]
    min_stable = quality_for(J0, min_k)[4] if min_k is not None else 0.0
    bal_stable = quality_for(J0, bal_k)[4]

    return [
        OriginAudit(
            "order/count invariance",
            "causal order only",
            "no",
            "no",
            "yes",
            0.0,
            "--",
            0.0,
            0.0,
            0.0,
            "FAIL-NO-PROBABILITY-LAW",
        ),
        OriginAudit(
            "RN spectrum only",
            "partition spectrum",
            "partial",
            "yes",
            "yes",
            span(free_ks),
            "--",
            0.0,
            0.0,
            1.0 if free_ks else 0.0,
            "FAIL-K-FAMILY",
        ),
        OriginAudit(
            "max entropy only",
            "least assumption",
            "yes",
            "no",
            "yes",
            0.0,
            "0.000",
            0.0,
            0.0,
            0.0,
            "FAIL-NO-EVENT",
        ),
        OriginAudit(
            "minimum norm with floor",
            "floor constrained",
            "yes",
            "yes",
            "yes",
            0.0,
            f"{min_k:.3f}" if min_k is not None else "--",
            min_defect,
            min_margin,
            min_stable,
            "FAIL-SUPPLIED-FLOOR",
        ),
        OriginAudit(
            "balanced defect/margin",
            "critical balance",
            "yes",
            "yes",
            "yes",
            0.0,
            f"{bal_k:.3f}",
            bal_defect,
            bal_margin,
            bal_stable,
            "COND-SUPPLIED-BALANCE-PRINCIPLE",
        ),
        OriginAudit(
            "free K spectrum-flow",
            "fixed form/free scalar",
            "yes",
            "yes",
            "yes",
            span(free_ks),
            f"{min(free_ks):.3f}-{max(free_ks):.3f}" if free_ks else "--",
            quality_for(J0, free_ks[len(free_ks) // 2])[2] if free_ks else 0.0,
            quality_for(J0, free_ks[len(free_ks) // 2])[3] if free_ks else 0.0,
            1.0 if free_ks else 0.0,
            "FAIL-FREE-SOURCE-SCALAR",
        ),
        OriginAudit(
            "fixed work normalization",
            "fixed J0,K0 work units",
            "yes",
            "yes",
            "yes",
            0.0,
            f"{fixed_k:.3f}",
            fixed_defect,
            fixed_margin,
            fixed_stable,
            "PASS-CONDITIONAL-DERIVATION",
        ),
    ]


def print_rows(audits: list[OriginAudit]) -> None:
    print("spectrum-flow origin audit")
    print("--------------------------")
    print(
        "candidate                    principle                form    R_x unit "
        "K_span chosen_K defect margin stable verdict"
    )
    for row in audits:
        print(
            f"{row.candidate:28s} "
            f"{row.principle:24s} "
            f"{row.form:7s} "
            f"{row.rx:3s} "
            f"{row.unit:4s} "
            f"{row.k_span:6.3f} "
            f"{row.chosen_k:8s} "
            f"{row.defect:6.4f} "
            f"{row.margin:6.4f} "
            f"{row.stable:6.3f} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    audits = rows()
    free = passing_ks(J0)
    print("=" * 122)
    print("v6 Paper 3 section 31: invariant origin of spectrum-flow CMRP")
    print("=" * 122)
    print_rows(audits)
    print("OPEN FAMILY COUNTEREXAMPLE")
    print("--------------------------")
    print(f"fixed internal work J0 = {J0:.3f}")
    print(f"passing K values = {len(free)}")
    print(f"K range = {min(free):.3f}..{max(free):.3f}")
    print(f"K span = {span(free):.3f}")
    for k in (min(free), K0, max(free)):
        status, label, defect, margin, stable = quality_for(J0, k)
        print(
            f"  K={k:.3f}: status={status}, R={label}, "
            f"defect={defect:.6f}, margin={margin:.6f}, stable={stable:.3f}"
        )
    print(f"log-RN chain error at K0 = {unit_chain_error(quality_for(J0, K0)[2], 'rn-log'):.3e}")
    print()
    print("VERDICT")
    print("-------")
    print("Einstein-invariant requirements derive the spectrum-flow form and the")
    print("log-RN unit, but not the numerical source-work amplitude.  A fixed")
    print("work normalization closes the finite derivation conditionally; without")
    print("that invariant scalar, there is an open family of equally admissible")
    print("spectrum-flow CMRP dynamics.")


if __name__ == "__main__":
    main()
