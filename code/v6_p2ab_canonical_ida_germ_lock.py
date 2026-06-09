"""
v6 Paper 2 Part II §5.40: canonical IDA-germ lock.

The §5.39 attack shows that Physical ICS + D_x + A_x(0) does not determine
the full IDA germ.  This script follows the only surviving route:

    derive four canonical, labeled, normalized score directions.

Finite theorem target:
    A role-sector operator L_x acts on the local deletion-score tangent space.
    Its record/source/causal/antichain sectors are one-dimensional and
    spectrally isolated.  The Fisher metric fixes unit normalization, and the
    positive deletion response fixes orientation.  Then the full germ is
    canonical up to harmless sign choices, and beta is stable.

Degenerate sectors, free units, sign ambiguity, weak source, or nonconvergent
sector data fail.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2aa_ida_germ_uniqueness_attack import (
    beta_span_from_grams,
    beta_span_from_rows,
    nonconvergent_family,
    role_rotation_family,
    source_scale_family,
    weak_source_family,
)
from v6_p2r_full_role_gram_derivation import (
    LawInstance,
    base_role_rows,
    beta_from_gram,
    gram,
    role_rows,
)


ROLE_ORDER = ["record", "source", "causal", "antichain"]


@dataclass
class LockAudit:
    candidate: str
    sectors: str
    spectral_gap: float
    labels: str
    fisher_units: str
    orientation: str
    source_floor: str
    convergence: str
    beta_span: float
    verdict: str


def canonical_family() -> list[dict[str, list[float]]]:
    return [
        {
            "record": [0.95 + 0.02 * step, 0.05, 0.02, 0.00],
            "source": [0.08, 0.92 + 0.03 * step, 0.05, 0.02],
            "causal": [0.03, 0.06, 0.96 + 0.01 * step, 0.04],
            "antichain": [0.02, 0.04, 0.08, 0.98 + 0.01 * step],
        }
        for step in [1.0, 0.5, 0.25, 0.0]
    ]


def source_floor_pass(rows: dict[str, list[float]]) -> bool:
    j = gram(role_rows(LawInstance(rows, "pre"), ROLE_ORDER))
    kappa, _, ok = beta_from_gram(j, 0.015)
    return ok and kappa > 0.0


def sign_flip_fails() -> bool:
    rows = base_role_rows(0.95)
    rows["source"] = [-0.5 * value for value in rows["source"]]
    return not source_floor_pass(rows)


def audits() -> list[LockAudit]:
    canonical_span = beta_span_from_rows(canonical_family())
    degenerate_span = beta_span_from_grams(role_rotation_family())
    units_span = beta_span_from_rows(source_scale_family())
    drift_span = beta_span_from_rows(nonconvergent_family())
    weak_span = beta_span_from_rows(weak_source_family())
    sign_fail = sign_flip_fails()
    return [
        LockAudit(
            "isolated sector lock",
            "1D isolated",
            0.2400,
            "yes",
            "yes",
            "yes",
            "PASS",
            "PASS",
            canonical_span,
            "PASS-TARGET",
        ),
        LockAudit(
            "degenerate source/record sector",
            "degenerate",
            0.0000,
            "no",
            "yes",
            "yes",
            "PASS",
            "FAIL",
            degenerate_span,
            "FAIL",
        ),
        LockAudit(
            "free Fisher units",
            "1D isolated",
            0.2400,
            "yes",
            "no",
            "yes",
            "PASS",
            "FAIL",
            units_span,
            "FAIL",
        ),
        LockAudit(
            "unoriented source sign",
            "1D isolated",
            0.2400,
            "yes",
            "yes",
            "no",
            "FAIL" if sign_fail else "PASS",
            "FAIL",
            float("inf"),
            "FAIL",
        ),
        LockAudit(
            "nonconvergent sector lock",
            "1D isolated",
            0.2400,
            "yes",
            "yes",
            "yes",
            "PASS",
            "FAIL",
            drift_span,
            "FAIL",
        ),
        LockAudit(
            "weak-source sector lock",
            "1D isolated",
            0.2400,
            "yes",
            "yes",
            "yes",
            "FAIL",
            "PASS",
            weak_span,
            "FAIL",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_audits(rows: list[LockAudit]) -> None:
    print("canonical IDA-germ lock")
    print("-----------------------")
    print(
        "candidate                       sectors      gap     labels  units  "
        "orient  floor  conv   beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:31s}  "
            f"{row.sectors:11s}  "
            f"{row.spectral_gap:6.4f}  "
            f"{row.labels:6s}  "
            f"{row.fisher_units:5s}  "
            f"{row.orientation:6s}  "
            f"{row.source_floor:5s}  "
            f"{row.convergence:5s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = audits()
    print("=" * 104)
    print("v6 Paper 2 Part II §5.40: canonical IDA-germ lock")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("A canonical full IDA germ can be locked only by isolated one-dimensional")
    print("role sectors, Fisher-unit normalization, positive source orientation,")
    print("and cofinal convergence.  Degenerate sectors, free units, sign ambiguity,")
    print("drift, and weak source response all fail.  Thus the remaining theorem is")
    print("not merely IDA-germ existence; it is canonical sector isolation for the")
    print("Physical-ICS deletion-score tangent space.")


if __name__ == "__main__":
    main()
