#!/usr/bin/env python3
"""Paper 3 section 64 diagnostic.

Campaign target:

    Does sealed indivisibility force a primitive binary modular defect?

The answer found here is negative for weak/natural meanings of indivisibility
and positive only after a stronger invariant is added: saturated two-endpoint
modular contrast.
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


def normalize(values: list[float], counts: list[int] | None = None) -> tuple[list[float], list[float]]:
    if counts is None:
        counts = [1] * len(values)
    total = float(sum(counts))
    weights = [c / total for c in counts]
    mean = sum(w * v for w, v in zip(weights, values))
    var = sum(w * (v - mean) ** 2 for w, v in zip(weights, values))
    if var <= 0.0:
        raise ValueError("constant score")
    return [(v - mean) / math.sqrt(var) for v in values], weights


def level_count(values: list[float], tol: float = 1e-10) -> int:
    levels: list[float] = []
    for v in values:
        if not any(abs(v - u) <= tol for u in levels):
            levels.append(v)
    return len(levels)


def work_response(values: list[float], weights: list[float], eta: float) -> tuple[float, float]:
    exponents = [eta * v for v in values]
    max_exp = max(exponents)
    raw = [w * math.exp(e - max_exp) for w, e in zip(weights, exponents)]
    z = sum(raw)
    probs = [r / z for r in raw]
    psi = math.log(z) + max_exp
    mean = sum(p * v for p, v in zip(probs, values))
    work = eta * mean - psi
    response = sum(p * (v - mean) ** 2 for p, v in zip(probs, values))
    return work, response


def residual(values: list[float], weights: list[float], eta: float) -> float:
    work, response = work_response(values, weights, eta)
    return work - response


def roots(values: list[float], weights: list[float], max_eta: float = 20.0, steps: int = 10000) -> list[float]:
    out: list[float] = []
    prev_eta = 0.0
    prev = residual(values, weights, prev_eta)
    for i in range(1, steps + 1):
        eta = max_eta * i / steps
        cur = residual(values, weights, eta)
        if cur * prev < 0.0:
            lo = prev_eta
            hi = eta
            flo = prev
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                fm = residual(values, weights, mid)
                if fm * flo <= 0.0:
                    hi = mid
                else:
                    lo = mid
                    flo = fm
            out.append(0.5 * (lo + hi))
        prev_eta = eta
        prev = cur
    return out


def matrix_rank(matrix: list[list[float]], tol: float = 1e-10) -> int:
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    col = 0
    while rank < rows and col < cols:
        pivot = max(range(rank, rows), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) <= tol:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_val = a[rank][col]
        a[rank] = [v / pivot_val for v in a[rank]]
        for r in range(rows):
            if r == rank:
                continue
            factor = a[r][col]
            a[r] = [v - factor * p for v, p in zip(a[r], a[rank])]
        rank += 1
        col += 1
    return rank


def popoviciu_ratio(values: list[float], weights: list[float]) -> float:
    mean = sum(w * v for w, v in zip(weights, values))
    var = sum(w * (v - mean) ** 2 for w, v in zip(weights, values))
    span = max(values) - min(values)
    return var / (span * span / 4.0)


def main() -> None:
    rows: list[Row] = []

    # 1. Prime atom count: no nontrivial Cartesian product size, but three levels.
    prime_values, prime_weights = normalize([-1.0, 0.0, 1.0])
    rows.append(
        Row(
            "product indivisibility",
            "3 atoms have no nontrivial Cartesian product factorization",
            "indecomposable but nonbinary",
            f"levels={level_count(prime_values)}, roots={len(roots(prime_values, prime_weights))}",
            "REFUTES-WEAK-INDIV",
        )
    )

    # 2. One-dimensional score geometry: one score direction, three levels.
    rows.append(
        Row(
            "rank-one score geometry",
            "single exponential parameter over three score levels",
            "Fisher rank one but nonbinary",
            f"levels={level_count(prime_values)}",
            "REFUTES-RANK1-IMPLIES-BINARY",
        )
    )

    # 3. Unique work-balance root is not enough to imply binary.
    three_roots = roots(prime_values, prime_weights)
    rows.append(
        Row(
            "unique DWB root",
            "three-shell score has one W=J crossing",
            "unique root but nonbinary",
            ", ".join(f"{r:.12f}" for r in three_roots),
            "REFUTES-ROOT-IMPLIES-BINARY",
        )
    )

    # 4. Rank-one collar interaction can still have three score levels.
    lower = [-1.0, 0.0, 1.0]
    upper = [-1.0, 0.0, 1.0]
    interaction = [[a * b for b in upper] for a in lower]
    flat_interaction = [v for row in interaction for v in row]
    inter_values, inter_weights = normalize(flat_interaction)
    rows.append(
        Row(
            "rank-one collar interaction",
            "q(i,j)=a_i b_j has interaction matrix rank one",
            "collar interaction rank one but nonbinary",
            f"rank={matrix_rank(interaction)}, levels={level_count(inter_values)}",
            "REFUTES-COLLAR-RANK1",
        )
    )

    # 5. General one-dimensional spectra can even defeat uniqueness.
    bad_raw = [
        -15.848391065169443,
        -15.26135706229148,
        -6.540840401342667,
        0.8016439899950072,
        18.903204268406732,
    ]
    bad_counts = [1_141_481, 45, 1_310_511, 67, 3]
    bad_values, bad_weights = normalize(bad_raw, bad_counts)
    bad_roots = roots(bad_values, bad_weights, max_eta=8.0, steps=12000)
    rows.append(
        Row(
            "general score spectrum",
            "finite uniform multiset represented by multiplicities",
            "one-dimensional DWB can have three roots",
            f"atoms={sum(bad_counts)}, roots={len(bad_roots)}",
            "REFUTES-GENERAL-PRIMITIVE",
        )
    )

    # 6. The only clean finite implication found: saturated contrast.
    binary_values, binary_weights = normalize([-1.0, 1.0])
    three_ratio = popoviciu_ratio(prime_values, prime_weights)
    binary_ratio = popoviciu_ratio(binary_values, binary_weights)
    rows.append(
        Row(
            "saturated contrast",
            "Popoviciu ratio Var/(range^2/4)",
            "saturation forces endpoint-only score",
            f"binary={binary_ratio:.3f}, three-shell={three_ratio:.3f}",
            "PROVES-BINARY-IF-AXIOM",
        )
    )

    rows.append(
        Row(
            "current sealed indivisibility",
            "product/rank/root/collar indivisibility audits",
            "does not force binary",
            "counterexamples above",
            "DISCARDED-AS-DERIVATION",
        )
    )

    rows.append(
        Row(
            "stronger invariant",
            "saturated Boolean modular contrast",
            "would force primitive binary defects",
            "new physical law/principle",
            "REQUIRED-TO-CLOSE",
        )
    )

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("prime_levels", level_count(prime_values))
    print("prime_roots", " ".join(f"{r:.15f}" for r in three_roots))
    print("rank_one_interaction_rank", matrix_rank(interaction))
    print("rank_one_interaction_levels", level_count(inter_values))
    print("bad_root_count", len(bad_roots))
    print("bad_roots", " ".join(f"{r:.15f}" for r in bad_roots))
    print("binary_popoviciu_ratio", f"{binary_ratio:.15f}")
    print("three_shell_popoviciu_ratio", f"{three_ratio:.15f}")


if __name__ == "__main__":
    main()
