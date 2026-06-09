"""
v6 Paper 2 Part II §5.43: L_x eigenlabel derivation.

The Dirichlet construction L_x = G_x^{-1} Q_x can produce isolated
one-dimensional modes, but eigenvalues alone do not label them as record,
source, causal, and antichain.  This audit tests whether labels can be derived
from intrinsic signature functionals of the Physical-ICS collar:

    record evidence signature;
    source deletion amplitude;
    causal-link sensitivity;
    antichain-density sensitivity.

If the signature matrix is diagonally dominant with a stable margin, labels are
canonical.  If two modes have the same signature, if a label is missing, or if
the signature drifts under refinement, beta is not derived.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2aa_ida_germ_uniqueness_attack import beta_span_from_rows, nonconvergent_family
from v6_p2ab_canonical_ida_germ_lock import canonical_family, weak_source_family


@dataclass
class LabelAudit:
    candidate: str
    isolated_modes: str
    signature_rank: int
    margin: float
    source_label: str
    convergence: str
    beta_span: float
    verdict: str


def determinant(matrix: list[list[float]]) -> float:
    if len(matrix) == 1:
        return matrix[0][0]
    total = 0.0
    for col, value in enumerate(matrix[0]):
        minor = [
            [row[c] for c in range(len(matrix)) if c != col]
            for row in matrix[1:]
        ]
        total += ((-1.0) ** col) * value * determinant(minor)
    return total


def rank(matrix: list[list[float]], tol: float = 1e-9) -> int:
    # Small 4x4 Gaussian elimination.
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0])
    out = 0
    r = 0
    for c in range(cols):
        pivot = max(range(r, rows), key=lambda i: abs(work[i][c]))
        if abs(work[pivot][c]) <= tol:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        scale = work[r][c]
        work[r] = [value / scale for value in work[r]]
        for i in range(rows):
            if i == r:
                continue
            factor = work[i][c]
            work[i] = [a - factor * b for a, b in zip(work[i], work[r])]
        out += 1
        r += 1
        if r == rows:
            break
    return out


def diagonal_margin(signature: list[list[float]]) -> float:
    margins = []
    for i, row in enumerate(signature):
        diag = abs(row[i])
        off = max(abs(value) for j, value in enumerate(row) if j != i)
        margins.append(diag - off)
    return min(margins)


def source_label_positive(signature: list[list[float]]) -> bool:
    source_row = 1
    source_col = 1
    return signature[source_row][source_col] > 0.0 and diagonal_margin(signature) > 0.0


def audits() -> list[LabelAudit]:
    good = [
        [0.94, 0.04, 0.02, 0.00],
        [0.06, 0.91, 0.05, 0.02],
        [0.02, 0.05, 0.93, 0.04],
        [0.01, 0.02, 0.06, 0.95],
    ]
    swapped = [
        [0.94, 0.04, 0.02, 0.00],
        [0.06, 0.05, 0.91, 0.02],
        [0.02, 0.93, 0.05, 0.04],
        [0.01, 0.02, 0.06, 0.95],
    ]
    degenerate = [
        [0.94, 0.04, 0.02, 0.00],
        [0.06, 0.50, 0.50, 0.02],
        [0.02, 0.50, 0.50, 0.04],
        [0.01, 0.02, 0.06, 0.95],
    ]
    weak_source = [
        [0.94, 0.04, 0.02, 0.00],
        [0.06, 0.07, 0.05, 0.02],
        [0.02, 0.05, 0.93, 0.04],
        [0.01, 0.02, 0.06, 0.95],
    ]
    rows = [
        ("intrinsic signature labels", good, True, True, canonical_family()),
        ("swapped source/causal signatures", swapped, True, True, canonical_family()),
        ("degenerate signatures", degenerate, True, True, canonical_family()),
        ("missing source signature", weak_source, True, True, weak_source_family()),
        ("signature drift", good, True, False, nonconvergent_family()),
        ("unisolated modes no labels", good, False, True, canonical_family()),
    ]
    out = []
    for name, signature, isolated, convergent, family in rows:
        sig_rank = rank(signature)
        margin = diagonal_margin(signature)
        source_ok = source_label_positive(signature)
        beta_span = beta_span_from_rows(family)
        passes = (
            isolated
            and sig_rank == 4
            and margin >= 0.20
            and source_ok
            and convergent
            and beta_span <= 0.02
        )
        out.append(
            LabelAudit(
                candidate=name,
                isolated_modes="yes" if isolated else "no",
                signature_rank=sig_rank,
                margin=margin,
                source_label="PASS" if source_ok else "FAIL",
                convergence="PASS" if convergent and beta_span <= 0.02 else "FAIL",
                beta_span=beta_span,
                verdict="PASS-TARGET" if passes else "FAIL",
            )
        )
    return out


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_audits(rows: list[LabelAudit]) -> None:
    print("L_x eigenlabel derivation")
    print("------------------------")
    print(
        "candidate                         isolated  rank  margin  source  "
        "conv   beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:33s}  "
            f"{row.isolated_modes:8s}  "
            f"{row.signature_rank:4d}  "
            f"{row.margin:6.4f}  "
            f"{row.source_label:6s}  "
            f"{row.convergence:5s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = audits()
    print("=" * 104)
    print("v6 Paper 2 Part II §5.43: L_x eigenlabel derivation")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("Isolated L_x modes are labeled intrinsically only when the four")
    print("Physical-ICS signature functionals form a full-rank, diagonally")
    print("dominant, refinement-stable matrix.  Swaps, degeneracy, missing source")
    print("signature, signature drift, or unisolated modes fail.")


if __name__ == "__main__":
    main()
