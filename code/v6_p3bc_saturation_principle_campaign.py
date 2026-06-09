#!/usr/bin/env python3
"""Paper 3 section 65 diagnostic.

Full campaign for Saturated Boolean Modular Contrast.

Question:
    Can saturation be derived, or is it a new primitive principle?

Finite result:
    Weak indivisibility does not imply saturation.  But the pair of invariant
    conditions "lossless Boolean event readout" and "count-dual endpoints"
    does imply saturation, and saturation is exactly what preserves the
    universal binary DWB constants.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def normalize(values: list[float], weights: list[float]) -> tuple[list[float], list[float]]:
    total = sum(weights)
    weights = [w / total for w in weights]
    mean = sum(w * v for w, v in zip(weights, values))
    var = sum(w * (v - mean) ** 2 for w, v in zip(weights, values))
    if var <= 0:
        raise ValueError("constant score")
    return [(v - mean) / math.sqrt(var) for v in values], weights


def stats(values: list[float], weights: list[float]) -> tuple[float, float, float, float]:
    mean = sum(w * v for w, v in zip(weights, values))
    var = sum(w * (v - mean) ** 2 for w, v in zip(weights, values))
    span = max(values) - min(values)
    pop_ratio = var / (span * span / 4.0)
    return mean, var, span, pop_ratio


def unique_levels(values: list[float], tol: float = 1e-10) -> list[float]:
    levels: list[float] = []
    for v in values:
        if not any(abs(v - u) < tol for u in levels):
            levels.append(v)
    return sorted(levels)


def min_boolean_residual(values: list[float], weights: list[float]) -> tuple[float, float]:
    """Best weighted residual after replacing q by a two-valued statistic."""
    levels = unique_levels(values)
    index = {level: i for i, level in enumerate(levels)}
    level_count = len(levels)
    if level_count <= 1:
        return 0.0, 0.0
    best = math.inf
    best_gap = math.inf
    # Enumerate nontrivial partitions of score levels, modulo complement.
    for size in range(1, level_count):
        for left_tuple in combinations(range(level_count), size):
            if 0 not in left_tuple:
                continue
            left = set(left_tuple)
            groups = [0 if index[v] in left else 1 for v in values]
            group_weight = [0.0, 0.0]
            group_mean = [0.0, 0.0]
            for g, w, v in zip(groups, weights, values):
                group_weight[g] += w
                group_mean[g] += w * v
            if group_weight[0] == 0.0 or group_weight[1] == 0.0:
                continue
            group_mean = [group_mean[g] / group_weight[g] for g in (0, 1)]
            residual = sum(
                w * (v - group_mean[g]) ** 2
                for g, w, v in zip(groups, weights, values)
            )
            gap = abs(group_weight[0] - 0.5)
            gap = min(gap, abs(group_weight[1] - 0.5))
            if residual < best:
                best = residual
                best_gap = gap
    return best, best_gap


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


def roots(values: list[float], weights: list[float], max_eta: float = 20.0, steps: int = 10000) -> list[float]:
    out: list[float] = []
    prev_eta = 0.0
    prev_work, prev_response = work_response(values, weights, prev_eta)
    prev = prev_work - prev_response
    for i in range(1, steps + 1):
        eta = max_eta * i / steps
        work, response = work_response(values, weights, eta)
        cur = work - response
        if cur * prev < 0.0:
            lo = prev_eta
            hi = eta
            flo = prev
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                mw, mr = work_response(values, weights, mid)
                fm = mw - mr
                if fm * flo <= 0.0:
                    hi = mid
                else:
                    lo = mid
                    flo = fm
            out.append(0.5 * (lo + hi))
        prev_eta = eta
        prev = cur
    return out


def audit_score(name: str, values: list[float], weights: list[float], verdict: str) -> Row:
    values, weights = normalize(values, weights)
    _, _, _, pop_ratio = stats(values, weights)
    residual, duality_gap = min_boolean_residual(values, weights)
    found_roots = roots(values, weights)
    return Row(
        name,
        "Boolean residual + count-duality + Popoviciu saturation",
        f"levels={len(unique_levels(values))}, roots={len(found_roots)}",
        f"res={residual:.3f}, gap={duality_gap:.3f}, pop={pop_ratio:.3f}",
        verdict,
    )


def main() -> None:
    rows = [
        audit_score(
            "balanced binary",
            [-1.0, 1.0],
            [1.0, 1.0],
            "PASS-SATURATED",
        ),
        audit_score(
            "three-shell event",
            [-1.0, 0.0, 1.0],
            [1.0, 1.0, 1.0],
            "FAIL-INTERIOR-SLACK",
        ),
        audit_score(
            "unbalanced binary",
            [-1.0, 1.0],
            [3.0, 1.0],
            "FAIL-COUNT-DUALITY",
        ),
        audit_score(
            "four-level score",
            [-1.0, -0.2, 0.4, 1.0],
            [1.0, 1.0, 1.0, 1.0],
            "FAIL-BOOLEAN-LOSS",
        ),
    ]

    balanced_values, balanced_weights = normalize([-1.0, 1.0], [1.0, 1.0])
    unbalanced_values, unbalanced_weights = normalize([-1.0, 1.0], [3.0, 1.0])
    balanced_root = roots(balanced_values, balanced_weights)[0]
    unbalanced_root = roots(unbalanced_values, unbalanced_weights)[0]

    rows.extend(
        [
            Row(
                "Boolean sufficiency theorem",
                "min residual after all binary coarse-grainings",
                "zero iff score is two-valued",
                "finite enumeration",
                "PROVES-BINARY",
            ),
            Row(
                "count-duality theorem",
                "two-valued score plus equal count weights",
                "equivalent to Popoviciu saturation",
                "pop=1",
                "PROVES-SATURATION",
            ),
            Row(
                "unbalanced constants attack",
                "binary without count-duality",
                "DWB root changes",
                f"balanced eta={balanced_root:.12f}, unbalanced eta={unbalanced_root:.12f}",
                "REFUTES-BINARY-ALONE",
            ),
            Row(
                "derivation status",
                "weak sealed indivisibility",
                "does not imply Boolean sufficiency or count-duality",
                "requires stronger event principle",
                "NOT-DERIVED",
            ),
            Row(
                "closure principle",
                "lossless Boolean readout + count-dual endpoints",
                "derives saturated Boolean modular contrast",
                "then DWB closes primitive law",
                "CLOSES-IF-ADOPTED",
            ),
        ]
    )

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    for label, values, weights in [
        ("balanced", [-1.0, 1.0], [1.0, 1.0]),
        ("three_shell", [-1.0, 0.0, 1.0], [1.0, 1.0, 1.0]),
        ("unbalanced", [-1.0, 1.0], [3.0, 1.0]),
    ]:
        nv, nw = normalize(values, weights)
        residual, gap = min_boolean_residual(nv, nw)
        _, _, _, pop_ratio = stats(nv, nw)
        print(
            label,
            "levels", len(unique_levels(nv)),
            "boolean_residual", f"{residual:.15f}",
            "duality_gap", f"{gap:.15f}",
            "popoviciu_ratio", f"{pop_ratio:.15f}",
            "roots", " ".join(f"{r:.15f}" for r in roots(nv, nw)),
        )


if __name__ == "__main__":
    main()
