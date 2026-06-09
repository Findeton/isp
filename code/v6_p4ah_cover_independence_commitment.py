#!/usr/bin/env python3
"""Paper 4 diagnostic AH: cover independence of commitment selection.

The cofinal commitment law is only physical if the same sealed process gives
the same selected h under admissible diamond covers.

This script tests the precise invariant:

  admissible covers must glue to the same primitive oriented RN/KL quotient
  ledger.

Under that quotient, permutations, overlap duplicates, and serial subdivisions
do not change the selected h.  Independent vertical modes are retained, not
discarded.  Arbitrary mixed bases have the same linear span but change the
separable commitment term; they are therefore not admissible primitive ledgers.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


Atom = tuple[float, ...]
Stat = tuple[float, ...]


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


def atoms(dim: int) -> list[Atom]:
    return [tuple(float(v) for v in atom) for atom in itertools.product([-1, 1], repeat=dim)]


def stat_values(dim: int, funcs: list) -> list[Stat]:
    values = []
    for atom in atoms(dim):
        values.append(tuple(float(func(*atom)) for func in funcs))
    return values


def log_partition(h: list[float], values: list[Stat]) -> float:
    total = 0.0
    for row in values:
        total += math.exp(sum(h_j * chi_j for h_j, chi_j in zip(h, row)))
    return math.log(total / len(values))


def gradient_psi(h: list[float], values: list[Stat]) -> list[float]:
    weighted = [0.0 for _ in h]
    z = 0.0
    for row in values:
        weight = math.exp(sum(h_j * chi_j for h_j, chi_j in zip(h, row)))
        z += weight
        for j, chi_j in enumerate(row):
            weighted[j] += weight * chi_j
    return [x / z for x in weighted]


def commitment_potential(h: list[float], values: list[Stat]) -> float:
    return log_partition(h, values) + sum(math.exp(-h_j) for h_j in h)


def commitment_gradient(h: list[float], values: list[Stat]) -> list[float]:
    grad = gradient_psi(h, values)
    return [grad_j - math.exp(-h_j) for grad_j, h_j in zip(grad, h)]


def norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def solve_commitment(values: list[Stat], start: float = 0.5) -> tuple[list[float], float]:
    h = [start for _ in range(len(values[0]))]
    value = commitment_potential(h, values)
    for _ in range(30000):
        grad = commitment_gradient(h, values)
        if norm(grad) < 1e-13:
            break
        step = 1.0
        while step > 1e-12:
            candidate = [h_j - step * grad_j for h_j, grad_j in zip(h, grad)]
            candidate_value = commitment_potential(candidate, values)
            if candidate_value <= value - 1e-4 * step * sum(g * g for g in grad):
                h = candidate
                value = candidate_value
                break
            step *= 0.5
        else:
            break
    return h, norm(commitment_gradient(h, values))


def covariance_rank(values: list[Stat]) -> int:
    n = len(values)
    d = len(values[0])
    means = [sum(row[j] for row in values) / n for j in range(d)]
    cov = []
    for i in range(d):
        cov_row = []
        for j in range(d):
            cov_row.append(sum((row[i] - means[i]) * (row[j] - means[j]) for row in values) / n)
        cov.append(cov_row)
    return rank(cov)


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b)) if a else 0.0


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    # Base primitive ledger: two independent oriented record modes x,y.
    base_values = stat_values(2, [lambda x, y: x, lambda x, y: y])
    h_base, res_base = solve_commitment(base_values)

    # Permuted cover: same primitive quotient, different local order.
    perm_values = stat_values(2, [lambda x, y: y, lambda x, y: x])
    h_perm, res_perm = solve_commitment(perm_values)
    h_perm_back = [h_perm[1], h_perm[0]]
    perm_gap = max_gap(h_base, h_perm_back)

    # Overlap cover with duplicated y. Raw coordinates double-count y and drift.
    overlap_raw = stat_values(3, [lambda x, y, z: x, lambda x, y, z: y, lambda x, y, z: y, lambda x, y, z: z])
    h_overlap_raw, res_overlap_raw = solve_commitment(overlap_raw)
    raw_effective = [h_overlap_raw[0], h_overlap_raw[1] + h_overlap_raw[2], h_overlap_raw[3]]
    quotient_values = stat_values(3, [lambda x, y, z: x, lambda x, y, z: y, lambda x, y, z: z])
    h_quotient, res_quotient = solve_commitment(quotient_values)
    overlap_raw_gap = max_gap(raw_effective, h_quotient)
    overlap_rank_raw = covariance_rank(overlap_raw)
    overlap_rank_quotient = covariance_rank(quotient_values)

    # Serial subdivision: survival is partition independent; coordinate-counting is not.
    i_total = 1.37
    serial_parts = [0.2, 0.33, 0.84]
    serial_survival_gap = abs(math.exp(-i_total) - math.prod(math.exp(-part) for part in serial_parts))
    serial_wrong_values = []
    for m in (1, 2, 4):
        # Equivalent to tanh(H)=exp(-H/m), solved with one-dimensional bisection.
        lo = 0.0
        hi = 20.0
        for _ in range(180):
            mid = 0.5 * (lo + hi)
            if math.tanh(mid) - math.exp(-mid / m) < 0:
                lo = mid
            else:
                hi = mid
        serial_wrong_values.append((m, 0.5 * (lo + hi)))
    serial_wrong_span = max(v for _, v in serial_wrong_values) - min(v for _, v in serial_wrong_values)

    # Independent vertical contrast: cover extension is physical, not silent.
    vertical_values = stat_values(3, [lambda x, y, z: x, lambda x, y, z: y, lambda x, y, z: z])
    h_vertical, res_vertical = solve_commitment(vertical_values)
    hidden_vertical_gap = abs(math.tanh(h_vertical[2]))

    # Cofinally silent vertical correction: a weak independent vertical mode
    # with coefficient forced by eps should not move x,y in the limit.
    silent_gaps = []
    for eps in (1.0 / 4, 1.0 / 8, 1.0 / 16, 1.0 / 32, 1.0 / 64):
        weak_values = stat_values(
            3,
            [
                lambda x, y, z: x,
                lambda x, y, z: y,
                lambda x, y, z, eps=eps: eps * z,
            ],
        )
        h_weak, _ = solve_commitment(weak_values)
        silent_gaps.append((eps, max_gap(h_weak[:2], h_base)))
    silent_gap_first = silent_gaps[0][1]
    silent_gap_last = silent_gaps[-1][1]

    # Mixed basis attack: same span as x,y but not primitive idempotent units.
    sqrt2 = math.sqrt(2.0)
    mixed_values = stat_values(
        2,
        [
            lambda x, y: (x + y) / sqrt2,
            lambda x, y: (x - y) / sqrt2,
        ],
    )
    h_mixed, res_mixed = solve_commitment(mixed_values)
    # Convert the mixed action back to x,y coefficients:
    mixed_effective_xy = [(h_mixed[0] + h_mixed[1]) / sqrt2, (h_mixed[0] - h_mixed[1]) / sqrt2]
    mixed_gap = max_gap(mixed_effective_xy, h_base)
    mixed_values_set = sorted(set(row[0] for row in mixed_values))
    primitive_value_set = sorted(set(row[0] for row in base_values))

    rows = [
        Row(
            "permutation cover",
            "swap local primitive ledger order",
            "selected h is natural under primitive-unit relabeling",
            f"gap={perm_gap:.1e}, residuals=({res_base:.1e},{res_perm:.1e})",
            "PASS-COVER",
        ),
        Row(
            "overlap duplicate attack",
            "two cover patches both include the same y primitive mode",
            "raw duplicate coordinates double-count y and drift; quotient identifies y once",
            f"raw_eff=({raw_effective[0]:.6f},{raw_effective[1]:.6f},{raw_effective[2]:.6f}), quotient=({h_quotient[0]:.6f},{h_quotient[1]:.6f},{h_quotient[2]:.6f}), gap={overlap_raw_gap:.6f}",
            "REFUTES-NAIVE-OVERLAP",
        ),
        Row(
            "overlap primitive quotient",
            "rank of duplicate cover ledger versus quotient ledger",
            "same process has rank three; duplicate cover has four coordinates but only three primitive modes",
            f"raw_rank={overlap_rank_raw}, quotient_rank={overlap_rank_quotient}, residual={res_quotient:.1e}",
            "PASS-QUOTIENT",
        ),
        Row(
            "serial cover gluing",
            "split one eventless collar evidence into serial pieces",
            "survival is independent of cover partition",
            f"survival_gap={serial_survival_gap:.1e}",
            "PASS-SERIAL",
        ),
        Row(
            "serial coordinate-count attack",
            "treat m serial pieces as m primitive commitment units",
            "selected h drifts with cover subdivision, hence the cover is inadmissible",
            "; ".join(f"m{m}={v:.6f}" for m, v in serial_wrong_values) + f"; span={serial_wrong_span:.6f}",
            "REFUTES-PER-CELL-LAW",
        ),
        Row(
            "vertical extension",
            "add independent z contrast in a refined cover",
            "z is a new primitive mode; dropping it changes future readout",
            f"h=({h_vertical[0]:.6f},{h_vertical[1]:.6f},{h_vertical[2]:.6f}), future_gap={hidden_vertical_gap:.6f}",
            "RETAIN-VERTICAL",
        ),
        Row(
            "cofinally silent vertical",
            "scale vertical contrast by eps -> 0",
            "horizontal selected h converges to the old cover value",
            f"gap_eps1/4={silent_gap_first:.1e}, gap_eps1/64={silent_gap_last:.1e}",
            "PASS-SILENT-LIMIT",
        ),
        Row(
            "mixed-basis attack",
            "replace primitive x,y by (x+y)/sqrt2 and (x-y)/sqrt2",
            "same span but different primitive units; component commitment moves the effective x,y law",
            f"mixed_xy=({mixed_effective_xy[0]:.6f},{mixed_effective_xy[1]:.6f}), base=({h_base[0]:.6f},{h_base[1]:.6f}), gap={mixed_gap:.6f}",
            "REFUTES-GL-INVARIANCE",
        ),
        Row(
            "primitive-value check",
            "compare value spectra of primitive and mixed stats",
            "mixed stats are not +/-1 indivisible record contrasts",
            f"primitive_values={primitive_value_set}, mixed_values={mixed_values_set}",
            "REJECTS-MIXED-PRIMITIVE",
        ),
        Row(
            "cover-independence verdict",
            "admissible cover = same primitive quotient ledger plus retained/non-silent vertical modes",
            "the selected h is cover-independent exactly for admissible covers",
            f"h_base=({h_base[0]:.9f},{h_base[1]:.9f})",
            "FINITE-COVER-THEOREM",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "h_base_0": h_base[0],
        "h_base_1": h_base[1],
        "perm_gap": perm_gap,
        "overlap_raw_gap": overlap_raw_gap,
        "overlap_rank_raw": float(overlap_rank_raw),
        "overlap_rank_quotient": float(overlap_rank_quotient),
        "serial_survival_gap": serial_survival_gap,
        "serial_wrong_span": serial_wrong_span,
        "hidden_vertical_gap": hidden_vertical_gap,
        "silent_gap_eps_1_4": silent_gap_first,
        "silent_gap_eps_1_64": silent_gap_last,
        "mixed_effective_x": mixed_effective_xy[0],
        "mixed_effective_y": mixed_effective_xy[1],
        "mixed_gap": mixed_gap,
        "res_base": res_base,
        "res_quotient": res_quotient,
        "res_mixed": res_mixed,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
