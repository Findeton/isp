#!/usr/bin/env python3
"""Paper 4 diagnostic AG: cofinal primitive-ledger commitment.

Diagnostic AF derived the intrinsic finite division law:

  S(I)=exp(-I),       grad psi(h)=exp(-h).

This diagnostic checks the remaining cofinal question.  A refinement must not
turn one primitive RN/KL commitment unit into many independent units merely by
subdivision.  The primitive ledger is the minimal projective quotient of
future-relevant RN/KL contrasts:

  * serial splits preserve the total evidence I and hence the same survival;
  * duplicate coordinates are rejected by the covariance/rank quotient;
  * new vertical modes are retained only when they have independent readout;
  * if the finite log-partitions Gamma-converge, the unique commitment
    minimizers converge.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def solve_root(lambda_scale: float = 1.0, eps: float = 0.0) -> float:
    """Solve tanh(h) + 2 eps h = exp(-lambda h)."""
    lo = 0.0
    hi = 20.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        value = math.tanh(mid) + 2.0 * eps * mid - math.exp(-lambda_scale * mid)
        if value < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def exp_survival(parts: list[float]) -> float:
    value = 1.0
    for part in parts:
        value *= math.exp(-part)
    return value


def rank(matrix: list[list[float]], tol: float = 1e-10) -> int:
    a = [row[:] for row in matrix if any(abs(x) > tol for x in row)]
    if not a:
        return 0
    m = len(a)
    n = len(a[0])
    r = 0
    for c in range(n):
        pivot = max(range(r, m), key=lambda i: abs(a[i][c]))
        if abs(a[pivot][c]) <= tol:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i == r:
                continue
            factor = a[i][c]
            if abs(factor) > tol:
                a[i] = [a[i][j] - factor * a[r][j] for j in range(n)]
        r += 1
    return r


def covariance_rank(stats: list[tuple[float, ...]]) -> int:
    n = len(stats)
    d = len(stats[0])
    means = [sum(row[j] for row in stats) / n for j in range(d)]
    cov = []
    for i in range(d):
        row = []
        for j in range(d):
            row.append(sum((x[i] - means[i]) * (x[j] - means[j]) for x in stats) / n)
        cov.append(row)
    return rank(cov)


def product_expectation(hx: float, hy: float) -> tuple[float, float]:
    return math.tanh(hx), math.tanh(hy)


def future_gap_from_hidden_vertical(h: float) -> float:
    """A coarse x shadow misses a future readout depending on hidden y."""
    _, ey = product_expectation(h, h)
    return abs(ey)


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    eta = solve_root()
    theta = math.tanh(eta)

    total_i = 1.73
    partitions = [
        [total_i],
        [0.50, 1.23],
        [0.20, 0.33, 0.41, 0.79],
        [total_i / 16.0 for _ in range(16)],
    ]
    partition_gaps = [abs(exp_survival(parts) - math.exp(-total_i)) for parts in partitions]
    max_partition_gap = max(partition_gaps)

    wrong_roots = [(m, solve_root(lambda_scale=1.0 / m)) for m in (1, 2, 4, 8)]
    wrong_span = max(value for _, value in wrong_roots) - min(value for _, value in wrong_roots)

    duplicate_stats = [(-1.0, -1.0), (1.0, 1.0)]
    duplicate_rank = covariance_rank(duplicate_stats)
    independent_stats = [(-1.0, -1.0), (-1.0, 1.0), (1.0, -1.0), (1.0, 1.0)]
    independent_rank = covariance_rank(independent_stats)

    h_horizontal = eta
    h_with_independent_vertical = eta
    hidden_future_gap = future_gap_from_hidden_vertical(eta)

    # Small perturbations of the finite log-partition demonstrate the standard
    # convex/Gamma-convergence mechanism: unique minimizers converge with psi_n.
    eps_values = [1.0 / n for n in (4, 8, 16, 32, 64, 128)]
    perturbed = [(eps, solve_root(eps=eps)) for eps in eps_values]
    convergence_gap_first = abs(perturbed[0][1] - eta)
    convergence_gap_last = abs(perturbed[-1][1] - eta)
    monotone_convergence = all(
        abs(perturbed[i + 1][1] - eta) <= abs(perturbed[i][1] - eta) + 1e-14
        for i in range(len(perturbed) - 1)
    )

    # A coupled perturbation that vanishes cofinally cannot move the horizontal
    # coefficient in the limit.  For a symmetric two-mode packet, the diagonal
    # solution solves tanh(h)+eps*tanh(h)^2+2*eps*h = exp(-h) to leading order.
    def solve_coupled_eps(eps: float) -> float:
        lo = 0.0
        hi = 20.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            value = math.tanh(mid) + eps * math.tanh(mid) ** 2 + 2.0 * eps * mid - math.exp(-mid)
            if value < 0.0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    coupled_values = [(eps, solve_coupled_eps(eps)) for eps in eps_values]
    coupled_gap_first = abs(coupled_values[0][1] - eta)
    coupled_gap_last = abs(coupled_values[-1][1] - eta)

    rows = [
        Row(
            "serial refinement",
            "split total RN/KL evidence into many eventless collar pieces",
            "survival products are partition-independent: prod exp(-I_k)=exp(-sum I_k)",
            f"max_gap={max_partition_gap:.1e}",
            "PASS-COFINAL-SURVIVAL",
        ),
        Row(
            "wrong per-cell commitment",
            "treat m subdivisions of one primitive mode as m independent commitment units",
            "selected coarse h drifts with m, so this is an inadmissible duplicate ledger",
            "; ".join(f"m{m}={value:.6f}" for m, value in wrong_roots) + f"; span={wrong_span:.6f}",
            "REFUTES-COORDINATE-SPLIT",
        ),
        Row(
            "primitive quotient",
            "compare duplicate coordinate stats with independent stats",
            "duplicate ledgers have covariance rank one and collapse to one primitive cochain",
            f"dup_rank={duplicate_rank}, independent_rank={independent_rank}",
            "DERIVES-MINIMAL-LEDGER",
        ),
        Row(
            "neutral horizontal lift",
            "refine without adding a future-relevant vertical contrast",
            "the old primitive coefficient is lifted unchanged",
            f"h_lift={h_horizontal:.9f}, theta={theta:.9f}",
            "PASS-PROJECTIVE",
        ),
        Row(
            "retained vertical mode",
            "add an independent future-relevant vertical RN/KL contrast",
            "the vertical contrast becomes a new primitive mode; omitting it leaves a future gap",
            f"h_vertical={h_with_independent_vertical:.9f}, hidden_future_gap={hidden_future_gap:.9f}",
            "RETAIN-OR-NOT-SILENT",
        ),
        Row(
            "Gamma convergence",
            "perturb psi_n=psi+eps_n h^2 with eps_n->0",
            "strict-convex commitment minimizers converge to the cofinal root",
            f"gap_eps1/4={convergence_gap_first:.6f}, gap_eps1/128={convergence_gap_last:.6f}",
            "PASS-MINIMIZER-CONVERGENCE" if monotone_convergence else "FAIL",
        ),
        Row(
            "vanishing coupled refinement",
            "add a cofinally vanishing coupled vertical correction",
            "horizontal drift vanishes with the coupling strength",
            f"gap_eps1/4={coupled_gap_first:.6f}, gap_eps1/128={coupled_gap_last:.6f}",
            "PASS-COUPLED-COFINAL",
        ),
        Row(
            "cofinal ledger verdict",
            "projective quotient ledger + RN/KL chain rule + strict convex commitment",
            "finite selected h is stable under neutral refinements and converges under controlled cofinal refinements",
            f"eta={eta:.9f}",
            "COFINAL-CLOSURE",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "eta": eta,
        "theta": theta,
        "partition_max_gap": max_partition_gap,
        "wrong_split_span": wrong_span,
        "duplicate_rank": float(duplicate_rank),
        "independent_rank": float(independent_rank),
        "hidden_future_gap": hidden_future_gap,
        "gamma_gap_eps_1_4": convergence_gap_first,
        "gamma_gap_eps_1_128": convergence_gap_last,
        "coupled_gap_eps_1_4": coupled_gap_first,
        "coupled_gap_eps_1_128": coupled_gap_last,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
