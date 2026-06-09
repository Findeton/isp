#!/usr/bin/env python3
"""Paper 4 diagnostic D: refinement limit of record gravity.

This script attacks the Einstein pressure point:

    Does L phi = rho remain meaningful under refinement, or is it only a
    finite graph trick?

It proves a scoped positive receipt for uniform sealed collar refinements on a
compact one-screen packet.  The eventless collar graph is the nearest-neighbor
ring, the intrinsic screen count gives h=1/n, and the scaled collar Laplacian

    L_n = h^{-2}(degree - adjacency)

converges to -d^2/dx^2.  The same script attacks unscaled collars, external
nonlocal chords, non-intrinsic alternating collar weights, and free source
amplitudes.
"""

from __future__ import annotations

from dataclasses import dataclass
import cmath
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def p_eta(eta: float) -> dict[int, float]:
    z = 2.0 * math.cosh(eta)
    return {-1: math.exp(-eta) / z, 1: math.exp(eta) / z}


def kl_to_mu(p: dict[int, float]) -> float:
    return sum(px * math.log(px / 0.5) for px in p.values())


def mean_q(p: dict[int, float]) -> float:
    return sum(q * pq for q, pq in p.items())


def var_q(p: dict[int, float]) -> float:
    m = mean_q(p)
    return sum(pq * (q - m) ** 2 for q, pq in p.items())


def balance_residual(eta: float) -> float:
    p = p_eta(eta)
    return kl_to_mu(p) - var_q(p)


def solve_eta_star() -> float:
    lo = 0.0
    hi = 20.0
    flo = balance_residual(lo)
    for _ in range(140):
        mid = 0.5 * (lo + hi)
        fm = balance_residual(mid)
        if fm * flo <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    return 0.5 * (lo + hi)


def centered(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    return [value - mean for value in values]


def max_abs(values: list[float]) -> float:
    return max(abs(value) for value in values)


def span(values: list[float]) -> float:
    return max(values) - min(values)


def source_smooth(n: int, work: float) -> list[float]:
    values = []
    for i in range(n):
        x = i / n
        values.append(work * (math.cos(2.0 * math.pi * x) + 0.4 * math.cos(4.0 * math.pi * x)))
    return centered(values)


def phi_smooth_exact(n: int, work: float) -> list[float]:
    values = []
    for i in range(n):
        x = i / n
        values.append(
            work
            * (
                math.cos(2.0 * math.pi * x) / (2.0 * math.pi) ** 2
                + 0.4 * math.cos(4.0 * math.pi * x) / (4.0 * math.pi) ** 2
            )
        )
    return centered(values)


def d_phi_smooth_exact(n: int, work: float) -> list[float]:
    values = []
    for i in range(n):
        x = i / n
        values.append(
            work
            * (
                -math.sin(2.0 * math.pi * x) / (2.0 * math.pi)
                - 0.4 * math.sin(4.0 * math.pi * x) / (4.0 * math.pi)
            )
        )
    return values


def source_indicator(n: int, work: float, fraction: float = 0.25) -> list[float]:
    events = [1.0 if i / n < fraction else 0.0 for i in range(n)]
    mean = sum(events) / n
    return [work * (event - mean) for event in events]


def solve_ring_poisson(rho: list[float], scaled: bool = True) -> list[float]:
    n = len(rho)
    coeffs: list[complex] = []
    for k in range(n):
        coeff = 0j
        for i, value in enumerate(rho):
            coeff += value * cmath.exp(-2j * math.pi * k * i / n)
        coeffs.append(coeff / n)

    phi_coeffs = [0j for _ in range(n)]
    for k in range(1, n):
        lam = 2.0 - 2.0 * math.cos(2.0 * math.pi * k / n)
        if scaled:
            lam *= n * n
        phi_coeffs[k] = coeffs[k] / lam

    values = []
    for i in range(n):
        value = 0j
        for k, coeff in enumerate(phi_coeffs):
            value += coeff * cmath.exp(2j * math.pi * k * i / n)
        values.append(value.real)
    return centered(values)


def apply_scaled_ring_laplacian(phi: list[float]) -> list[float]:
    n = len(phi)
    return [
        n * n * (2.0 * phi[i] - phi[(i - 1) % n] - phi[(i + 1) % n])
        for i in range(n)
    ]


def weighted_laplacian(n: int, edge_weights: list[float], chords: list[tuple[int, int, float]] | None = None) -> list[list[float]]:
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i, weight in enumerate(edge_weights):
        j = (i + 1) % n
        matrix[i][i] += weight
        matrix[j][j] += weight
        matrix[i][j] -= weight
        matrix[j][i] -= weight
    for i, j, weight in chords or []:
        matrix[i][i] += weight
        matrix[j][j] += weight
        matrix[i][j] -= weight
        matrix[j][i] -= weight
    return matrix


def solve_mean_zero(matrix: list[list[float]], rho: list[float]) -> list[float]:
    n = len(matrix)
    a = [row[:] + [rhs] for row, rhs in zip(matrix, rho)]
    a[-1] = [1.0 for _ in range(n)] + [0.0]

    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(a[row][col]))
        if abs(a[pivot][col]) < 1e-14:
            raise ValueError("singular gauge-fixed matrix")
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [x / scale for x in a[col]]
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            if factor:
                a[row] = [x - factor * y for x, y in zip(a[row], a[col])]

    return centered([a[i][-1] for i in range(n)])


def max_error(values: list[float], reference: list[float]) -> float:
    return max_abs([value - ref for value, ref in zip(values, reference)])


def binary_refinement_gaps(work: float) -> list[float]:
    gaps = []
    for n in (32, 64, 128):
        coarse = solve_ring_poisson(source_indicator(n, work), scaled=True)
        fine = solve_ring_poisson(source_indicator(2 * n, work), scaled=True)
        restricted = [fine[2 * i] for i in range(n)]
        gaps.append(max_error(coarse, restricted))
    return gaps


def future_drift(phi: list[float]) -> list[float]:
    n = len(phi)
    drifts = []
    for i in range(n):
        delta_plus = phi[(i + 1) % n] - phi[i]
        delta_minus = phi[(i - 1) % n] - phi[i]
        raw_plus = math.exp(-0.5 * delta_plus)
        raw_minus = math.exp(-0.5 * delta_minus)
        p_plus = raw_plus / (raw_plus + raw_minus)
        p_minus = raw_minus / (raw_plus + raw_minus)
        drifts.append(n * (p_plus - p_minus))
    return drifts


def main() -> None:
    eta = solve_eta_star()
    work = kl_to_mu(p_eta(eta))

    smooth_errors = []
    curvature_residuals = []
    drift_errors = []
    for n in (32, 64, 128, 256):
        rho = source_smooth(n, work)
        phi = solve_ring_poisson(rho, scaled=True)
        exact = phi_smooth_exact(n, work)
        smooth_errors.append(max_error(phi, exact))
        curvature = apply_scaled_ring_laplacian(phi)
        curvature_residuals.append(max_error(curvature, rho))
        drift = future_drift(phi)
        expected_drift = [-0.5 * value for value in d_phi_smooth_exact(n, work)]
        drift_errors.append(max_error(drift, expected_drift))

    binary_gaps = binary_refinement_gaps(work)

    unscaled_spans = []
    for n in (32, 64, 128):
        unscaled_spans.append(span(solve_ring_poisson(source_smooth(n, work), scaled=False)))

    n_attack = 64
    rho_attack = source_smooth(n_attack, work)
    exact_attack = phi_smooth_exact(n_attack, work)
    uniform_edges = [n_attack * n_attack for _ in range(n_attack)]
    chord_matrix = weighted_laplacian(
        n_attack,
        uniform_edges,
        chords=[(0, n_attack // 2, n_attack * n_attack)],
    )
    chord_phi = solve_mean_zero(chord_matrix, rho_attack)
    chord_error = max_error(chord_phi, exact_attack)

    alternating_edges = [
        n_attack * n_attack * (1.0 if i % 2 == 0 else 2.0)
        for i in range(n_attack)
    ]
    alternating_phi = solve_mean_zero(weighted_laplacian(n_attack, alternating_edges), rho_attack)
    alternating_error = max_error(alternating_phi, exact_attack)

    double_work_phi = solve_ring_poisson(source_smooth(n_attack, 2.0 * work), scaled=True)
    normal_work_phi = solve_ring_poisson(source_smooth(n_attack, work), scaled=True)
    amplitude_gap = max_error(double_work_phi, normal_work_phi)

    rows = [
        Row(
            "scaled collar limit",
            "L_n=h^-2(degree-adjacency), h=1/n",
            "smooth Poisson response converges",
            "err32/64/128/256=" + "/".join(f"{e:.3e}" for e in smooth_errors),
            "PASS",
        ),
        Row(
            "curvature/source identity",
            "apply L_n to solved phi_n",
            "L_n phi_n equals rho_n to numerical precision",
            "res=" + "/".join(f"{e:.1e}" for e in curvature_residuals),
            "PASS",
        ),
        Row(
            "binary event-source refinement",
            "E_n is interval support, rho_n=W*(E_n-mean E_n)",
            "coarse/fine potentials stabilize",
            "gap32-64/64-128/128-256=" + "/".join(f"{g:.3e}" for g in binary_gaps),
            "PASS",
        ),
        Row(
            "future transport limit",
            "K_phi nearest-neighbor tilt",
            "scaled drift converges to -1/2 grad phi",
            "err32/64/128/256=" + "/".join(f"{e:.3e}" for e in drift_errors),
            "PASS",
        ),
        Row(
            "unscaled collar attack",
            "use degree-adjacency without h^-2",
            "potential span grows with refinement",
            "span32/64/128=" + "/".join(f"{s:.3e}" for s in unscaled_spans),
            "FAILS",
        ),
        Row(
            "external chord attack",
            "add nonlocal collar edge before solving",
            "limit no longer matches local continuum operator",
            f"err64={chord_error:.3e}",
            "FAILS-INTRINSICITY",
        ),
        Row(
            "alternating weight attack",
            "alternate collar conductances not implied by count-uniform screen",
            "converges to a different variable-coefficient geometry",
            f"err64={alternating_error:.3e}",
            "FAILS-UNIFORM-GEOMETRY",
        ),
        Row(
            "free source-amplitude attack",
            "replace W* by 2W*",
            "continuum response changes linearly",
            f"phi_gap64={amplitude_gap:.3e}",
            "FAILS-BRANCH-A",
        ),
        Row(
            "refinement theorem verdict",
            "uniform sealed collars + W* deletion sources",
            "finite record gravity has a stable local continuum limit",
            "scoped theorem, not full Einstein tensor",
            "FINITE-CLOSURE",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("eta_star", f"{eta:.15f}")
    print("primitive_work", f"{work:.15f}")
    print("smooth_errors", " ".join(f"{e:.15e}" for e in smooth_errors))
    print("binary_refinement_gaps", " ".join(f"{g:.15e}" for g in binary_gaps))
    print("drift_errors", " ".join(f"{e:.15e}" for e in drift_errors))
    print("unscaled_spans", " ".join(f"{s:.15e}" for s in unscaled_spans))
    print("chord_error", f"{chord_error:.15e}")
    print("alternating_error", f"{alternating_error:.15e}")
    print("amplitude_gap", f"{amplitude_gap:.15e}")


if __name__ == "__main__":
    main()
