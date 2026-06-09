"""
v6 Paper 2 Part II §5.44: signature-origin audit.

After L_x is constructed from G_x^{-1}Q_x, and after eigenmodes are labeled by
signature functionals, one final loophole remains: the signatures themselves
must be intrinsic to Physical ICS.

This audit tests the origin of the four signatures:

    record evidence;
    source deletion energy/amplitude;
    causal-link sensitivity;
    antichain-density sensitivity.

If the source signature is external, or if the signatures fail to be a
full-rank stable quartet, beta remains free.  The surviving theorem target is
Physical ICS deriving the signature quartet from its own record/order/deletion
dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2aa_ida_germ_uniqueness_attack import beta_span_from_rows, source_row_family
from v6_p2ab_canonical_ida_germ_lock import canonical_family, weak_source_family
from v6_p2ae_lx_eigenlabel_derivation import diagonal_margin, rank


@dataclass
class SignatureAudit:
    candidate: str
    record: str
    source: str
    causal: str
    antichain: str
    rank: int
    margin: float
    stable: str
    beta_span: float
    verdict: str


GOOD = [
    [0.94, 0.04, 0.02, 0.00],
    [0.06, 0.91, 0.05, 0.02],
    [0.02, 0.05, 0.93, 0.04],
    [0.01, 0.02, 0.06, 0.95],
]

NO_SOURCE = [
    [0.94, 0.04, 0.02, 0.00],
    [0.00, 0.00, 0.00, 0.00],
    [0.02, 0.05, 0.93, 0.04],
    [0.01, 0.02, 0.06, 0.95],
]

EXTERNAL_SOURCE = [
    [0.94, 0.04, 0.02, 0.00],
    [0.06, 0.60, 0.38, 0.02],
    [0.02, 0.05, 0.93, 0.04],
    [0.01, 0.02, 0.06, 0.95],
]

DEGENERATE = [
    [0.94, 0.04, 0.02, 0.00],
    [0.06, 0.50, 0.50, 0.02],
    [0.02, 0.50, 0.50, 0.04],
    [0.01, 0.02, 0.06, 0.95],
]


def audit(
    candidate: str,
    matrix: list[list[float]],
    record: bool,
    source: bool,
    causal: bool,
    antichain: bool,
    stable: bool,
    beta_span: float,
) -> SignatureAudit:
    sig_rank = rank(matrix)
    margin = diagonal_margin(matrix)
    passes = (
        record
        and source
        and causal
        and antichain
        and stable
        and sig_rank == 4
        and margin >= 0.20
        and beta_span <= 0.02
    )
    return SignatureAudit(
        candidate=candidate,
        record="yes" if record else "no",
        source="yes" if source else "no",
        causal="yes" if causal else "no",
        antichain="yes" if antichain else "no",
        rank=sig_rank,
        margin=margin,
        stable="PASS" if stable and beta_span <= 0.02 else "FAIL",
        beta_span=beta_span,
        verdict="PASS-TARGET" if passes else "FAIL",
    )


def audits() -> list[SignatureAudit]:
    return [
        audit(
            "intrinsic signature quartet",
            GOOD,
            True,
            True,
            True,
            True,
            True,
            beta_span_from_rows(canonical_family()),
        ),
        audit(
            "no source signature",
            NO_SOURCE,
            True,
            False,
            True,
            True,
            True,
            float("inf"),
        ),
        audit(
            "external source signature",
            EXTERNAL_SOURCE,
            True,
            False,
            True,
            True,
            True,
            beta_span_from_rows(source_row_family()),
        ),
        audit(
            "source/causal ambiguous",
            DEGENERATE,
            True,
            True,
            True,
            True,
            True,
            beta_span_from_rows(canonical_family()),
        ),
        audit(
            "weak source signature",
            GOOD,
            True,
            True,
            True,
            True,
            True,
            beta_span_from_rows(weak_source_family()),
        ),
        audit(
            "signature refinement drift",
            GOOD,
            True,
            True,
            True,
            True,
            False,
            0.1226,
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_audits(rows: list[SignatureAudit]) -> None:
    print("signature-origin audit")
    print("----------------------")
    print(
        "candidate                     rec  src  caus  anti  rank  margin  "
        "stable  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:29s}  "
            f"{row.record:3s}  "
            f"{row.source:3s}  "
            f"{row.causal:4s}  "
            f"{row.antichain:4s}  "
            f"{row.rank:4d}  "
            f"{row.margin:6.4f}  "
            f"{row.stable:6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = audits()
    print("=" * 104)
    print("v6 Paper 2 Part II §5.44: signature-origin audit")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("L_x eigenlabels are intrinsic only if Physical ICS derives the whole")
    print("signature quartet.  Missing, external, ambiguous, weak, or drifting")
    print("source signatures fail.  The final theorem target is an intrinsic")
    print("record/source/causal/antichain signature quartet plus the Dirichlet")
    print("operator L_x = G_x^{-1} Q_x.")


if __name__ == "__main__":
    main()
