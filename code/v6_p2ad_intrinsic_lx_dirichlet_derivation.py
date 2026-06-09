"""
v6 Paper 2 Part II §5.42: intrinsic L_x Dirichlet derivation.

This is the constructive follow-up to §5.41.

Given a finite Physical-ICS deletion action germ, define:

    G_x(u,v) = Fisher covariance of score functions;
    Q_x(u,v) = deletion Dirichlet form, measuring how scores change under D_x;
    L_x      = G_x^{-1} Q_x.

Because Q_x and G_x are built from P_n and D_x, L_x is intrinsic if these two
forms are.  The finite theorem target then becomes spectral: four isolated
one-dimensional eigen-sectors must line up with record/source/causal/antichain,
have fixed Fisher units, positive source response, and converge under
refinement.

No numpy is used; the examples are diagonal in the role basis so the
generalized eigenvalues are explicit ratios Q_rr/G_rr.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2r_full_role_gram_derivation import (
    ROLE_ORDER,
    LawInstance,
    beta_from_gram,
    gram,
    role_rows,
)


@dataclass
class IntrinsicLxCandidate:
    name: str
    g_diag: list[float]
    q_diag: list[float]
    rows: dict[str, list[float]]
    intrinsic_g: bool
    intrinsic_q: bool
    labels_intrinsic: bool
    source_internal: bool
    convergent: bool


@dataclass
class IntrinsicLxAudit:
    candidate: str
    intrinsic: str
    labels: str
    eigvals: list[float]
    min_gap: float
    isolated: str
    source: str
    beta_span: float
    verdict: str


def rows_from_diag(source_strength: float = 0.95) -> dict[str, list[float]]:
    return {
        "record": [0.95, 0.05, 0.02, 0.00],
        "source": [0.08, source_strength, 0.05, 0.02],
        "causal": [0.03, 0.06, 0.96, 0.04],
        "antichain": [0.02, 0.04, 0.08, 0.98],
    }


def generalized_eigvals(g_diag: list[float], q_diag: list[float]) -> list[float]:
    return [q / g for q, g in zip(q_diag, g_diag)]


def min_gap(values: list[float]) -> float:
    ordered = sorted(values)
    return min(ordered[i + 1] - ordered[i] for i in range(len(ordered) - 1))


def beta_span(rows_family: list[dict[str, list[float]]]) -> float:
    betas = []
    for rows in rows_family:
        j = gram(role_rows(LawInstance(rows, "pre"), ROLE_ORDER))
        _, beta, ok = beta_from_gram(j, 0.015)
        if ok:
            betas.append(beta)
    return max(betas) - min(betas) if len(betas) >= 2 else float("inf")


def source_pass(rows: dict[str, list[float]]) -> bool:
    j = gram(role_rows(LawInstance(rows, "pre"), ROLE_ORDER))
    kappa, _, ok = beta_from_gram(j, 0.015)
    return ok and kappa > 0.0


def candidate_families() -> list[tuple[IntrinsicLxCandidate, list[dict[str, list[float]]]]]:
    canonical_rows = [
        {
            "record": [0.95 + 0.02 * step, 0.05, 0.02, 0.00],
            "source": [0.08, 0.92 + 0.03 * step, 0.05, 0.02],
            "causal": [0.03, 0.06, 0.96 + 0.01 * step, 0.04],
            "antichain": [0.02, 0.04, 0.08, 0.98 + 0.01 * step],
        }
        for step in [1.0, 0.5, 0.25, 0.0]
    ]
    plateau_rows = [rows_from_diag(0.95) for _ in range(4)]
    drift_rows = [rows_from_diag(strength) for strength in [0.55, 1.15, 0.65, 1.05]]
    weak_rows = []
    for strength in [0.04, 0.05, 0.06, 0.05]:
        rows = rows_from_diag(0.95)
        rows["source"] = [0.02, strength, 0.01, 0.00]
        weak_rows.append(rows)

    return [
        (
            IntrinsicLxCandidate(
                "intrinsic Dirichlet Lx",
                [1.0, 1.0, 1.0, 1.0],
                [0.18, 0.47, 0.82, 1.21],
                canonical_rows[-1],
                True,
                True,
                True,
                True,
                True,
            ),
            canonical_rows,
        ),
        (
            IntrinsicLxCandidate(
                "no deletion Q",
                [1.0, 1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 0.0],
                rows_from_diag(0.95),
                True,
                False,
                False,
                False,
                False,
            ),
            plateau_rows,
        ),
        (
            IntrinsicLxCandidate(
                "degenerate Dirichlet Lx",
                [1.0, 1.0, 1.0, 1.0],
                [0.18, 0.18, 0.82, 1.21],
                rows_from_diag(0.95),
                True,
                True,
                False,
                True,
                False,
            ),
            plateau_rows,
        ),
        (
            IntrinsicLxCandidate(
                "external Q choice",
                [1.0, 1.0, 1.0, 1.0],
                [0.22, 0.49, 0.81, 1.20],
                rows_from_diag(0.95),
                True,
                False,
                False,
                True,
                False,
            ),
            plateau_rows,
        ),
        (
            IntrinsicLxCandidate(
                "wrong role ordering",
                [1.0, 1.0, 1.0, 1.0],
                [0.47, 0.18, 0.82, 1.21],
                rows_from_diag(0.95),
                True,
                True,
                False,
                True,
                False,
            ),
            plateau_rows,
        ),
        (
            IntrinsicLxCandidate(
                "nonconvergent Dirichlet Lx",
                [1.0, 1.0, 1.0, 1.0],
                [0.18, 0.47, 0.82, 1.21],
                drift_rows[-1],
                True,
                True,
                True,
                True,
                False,
            ),
            drift_rows,
        ),
        (
            IntrinsicLxCandidate(
                "weak-source Dirichlet Lx",
                [1.0, 1.0, 1.0, 1.0],
                [0.18, 0.47, 0.82, 1.21],
                weak_rows[-1],
                True,
                True,
                True,
                True,
                True,
            ),
            weak_rows,
        ),
    ]


def audit(candidate: IntrinsicLxCandidate, family: list[dict[str, list[float]]]) -> IntrinsicLxAudit:
    eigvals = generalized_eigvals(candidate.g_diag, candidate.q_diag)
    gap = min_gap(eigvals)
    isolated = gap > 0.08
    source_ok = candidate.source_internal and source_pass(candidate.rows)
    span = beta_span(family)
    beta_ok = span <= 0.02
    intrinsic = candidate.intrinsic_g and candidate.intrinsic_q
    passes = (
        intrinsic
        and candidate.labels_intrinsic
        and isolated
        and source_ok
        and candidate.convergent
        and beta_ok
    )
    return IntrinsicLxAudit(
        candidate=candidate.name,
        intrinsic="PASS" if intrinsic else "FAIL",
        labels="PASS" if candidate.labels_intrinsic else "FAIL",
        eigvals=eigvals,
        min_gap=gap,
        isolated="PASS" if isolated else "FAIL",
        source="PASS" if source_ok else "FAIL",
        beta_span=span,
        verdict="PASS-TARGET" if passes else "FAIL",
    )


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def fmt_eigs(values: list[float]) -> str:
    return "[" + ",".join(f"{value:.2f}" for value in values) + "]"


def print_audits(rows: list[IntrinsicLxAudit]) -> None:
    print("intrinsic L_x Dirichlet derivation")
    print("----------------------------------")
    print(
        "candidate                    intrinsic  labels  eigvals              "
        "gap     isolated  source  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:28s}  "
            f"{row.intrinsic:9s}  "
            f"{row.labels:6s}  "
            f"{fmt_eigs(row.eigvals):20s}  "
            f"{row.min_gap:6.4f}  "
            f"{row.isolated:8s}  "
            f"{row.source:6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(candidate, family) for candidate, family in candidate_families()]
    print("=" * 104)
    print("v6 Paper 2 Part II §5.42: intrinsic L_x Dirichlet derivation")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("The finite construction L_x = G_x^{-1} Q_x is intrinsic when G_x is")
    print("the IDA Fisher metric and Q_x is the deletion Dirichlet form.  It")
    print("derives the role sectors only if the generalized spectrum has four")
    print("isolated, correctly labeled one-dimensional sectors with positive")
    print("source response and cofinal beta convergence.  Missing Q, degeneracy,")
    print("external Q, wrong labels, drift, and weak source response all fail.")


if __name__ == "__main__":
    main()
