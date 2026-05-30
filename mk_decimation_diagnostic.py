#!/usr/bin/env python3
"""Dependency-free Migdal-Kadanoff character-flow diagnostic.

This is a numerical diagnostic only.  It applies the standard character
coefficient MK-style recursion with scale factor b=2 in d=4:

    F_r = projection of f(U) ** zeta, zeta=b**(d-2)
    c_r(new) = (F_r / F_0 / dim(r)) ** (b*b)

For SU(2), r is spin j with j2=2*j.  For U(1), r is Fourier mode n.

The reported "beta_eff" is inferred from the lightest-channel weak-coupling
tree relation:

    SU(2):  m_{1/2} ~= 3/(2 beta_eff)
    U(1):   m_1     ~= 1/(2 beta_eff)

This checks whether the block coefficient flow remains tree-level/classical or
develops an RG-flow signal.  It is not a proof of anything about the hypercubic
lattice.

For the SU(2) heat-kernel line, the weak-coupling asymptotic of this diagnostic
has beta_eff(n)-beta_eff(n+1) -> 1/4.  This is close to, but not identical with,
the one-loop hypercubic SU(2) scale-two decrement.
"""

from __future__ import annotations

import argparse
import math
from typing import List, Sequence, Tuple


def su2_character(j2: int, alpha: float) -> float:
    """SU(2) character chi_j(alpha), with j2=2*j and tr U=2 cos alpha."""
    d = j2 + 1
    s = math.sin(alpha)
    if abs(s) < 1e-14:
        return float(d)
    return math.sin(d * alpha) / s


def make_su2_grid(n_grid: int, j2_max: int) -> Tuple[List[float], List[List[float]]]:
    h = math.pi / n_grid
    weights: List[float] = []
    chars: List[List[float]] = [[] for _ in range(j2_max + 1)]
    for k in range(n_grid):
        alpha = (k + 0.5) * h
        w = (2.0 / math.pi) * (math.sin(alpha) ** 2) * h
        weights.append(w)
        for j2 in range(j2_max + 1):
            chars[j2].append(su2_character(j2, alpha))
    return weights, chars


def project_su2(
    values: Sequence[float],
    weights: Sequence[float],
    chars: Sequence[Sequence[float]],
    j2_max: int,
    warn_threshold: float,
) -> Tuple[List[float], float, int]:
    """Project a positive class function to normalized SU(2) coefficients."""
    a0 = sum(w * v for w, v in zip(weights, values))
    coeffs = [1.0]
    negative_raw = 0
    for j2 in range(1, j2_max + 1):
        aj = sum(weights[k] * values[k] * chars[j2][k] for k in range(len(values)))
        raw = aj / ((j2 + 1) * a0)
        if raw < -warn_threshold:
            negative_raw += 1
        coeffs.append(raw)
    return coeffs, a0, negative_raw


def su2_function_from_coeffs(
    coeffs: Sequence[float],
    chars: Sequence[Sequence[float]],
    k: int,
) -> float:
    value = 1.0
    for j2 in range(1, len(coeffs)):
        value += (j2 + 1) * coeffs[j2] * chars[j2][k]
    return value


def initial_su2_coeffs(
    beta: float,
    weights: Sequence[float],
    chars: Sequence[Sequence[float]],
    j2_max: int,
    warn_threshold: float,
) -> Tuple[List[float], float, int]:
    values = []
    n_grid = len(weights)
    h = math.pi / n_grid
    for k in range(n_grid):
        alpha = (k + 0.5) * h
        values.append(math.exp(beta * (math.cos(alpha) - 1.0)))
    return project_su2(values, weights, chars, j2_max, warn_threshold)


def mk_step_su2(
    coeffs: Sequence[float],
    weights: Sequence[float],
    chars: Sequence[Sequence[float]],
    j2_max: int,
    zeta: int,
    r: int,
    warn_threshold: float,
) -> Tuple[List[float], float, int, float]:
    values: List[float] = []
    min_f = float("inf")
    for k in range(len(weights)):
        f = su2_function_from_coeffs(coeffs, chars, k)
        min_f = min(min_f, f)
        values.append(f**zeta)
    raw_coeffs, a0, negative_raw = project_su2(
        values, weights, chars, j2_max, warn_threshold
    )
    new_coeffs = [1.0]
    for c in raw_coeffs[1:]:
        new_coeffs.append(c**r)
    return new_coeffs, a0, negative_raw, min_f


def make_u1_grid(n_grid: int, n_max: int) -> Tuple[List[float], List[List[float]]]:
    h = 2.0 * math.pi / n_grid
    weights = [h / (2.0 * math.pi)] * n_grid
    cosines: List[List[float]] = [[] for _ in range(n_max + 1)]
    for k in range(n_grid):
        theta = (k + 0.5) * h
        for n in range(n_max + 1):
            cosines[n].append(math.cos(n * theta))
    return weights, cosines


def project_u1(
    values: Sequence[float],
    weights: Sequence[float],
    cosines: Sequence[Sequence[float]],
    n_max: int,
    warn_threshold: float,
) -> Tuple[List[float], float, int]:
    a0 = sum(w * v for w, v in zip(weights, values))
    coeffs = [1.0]
    negative_raw = 0
    for n in range(1, n_max + 1):
        an = sum(weights[k] * values[k] * cosines[n][k] for k in range(len(values)))
        raw = an / a0
        if raw < -warn_threshold:
            negative_raw += 1
        coeffs.append(raw)
    return coeffs, a0, negative_raw


def u1_function_from_coeffs(
    coeffs: Sequence[float],
    cosines: Sequence[Sequence[float]],
    k: int,
) -> float:
    value = 1.0
    for n in range(1, len(coeffs)):
        value += 2.0 * coeffs[n] * cosines[n][k]
    return value


def initial_u1_coeffs(
    beta: float,
    weights: Sequence[float],
    cosines: Sequence[Sequence[float]],
    n_max: int,
    warn_threshold: float,
) -> Tuple[List[float], float, int]:
    values = []
    n_grid = len(weights)
    h = 2.0 * math.pi / n_grid
    for k in range(n_grid):
        theta = (k + 0.5) * h
        values.append(math.exp(beta * (math.cos(theta) - 1.0)))
    return project_u1(values, weights, cosines, n_max, warn_threshold)


def mk_step_u1(
    coeffs: Sequence[float],
    weights: Sequence[float],
    cosines: Sequence[Sequence[float]],
    n_max: int,
    zeta: int,
    r: int,
    warn_threshold: float,
) -> Tuple[List[float], float, int, float]:
    values: List[float] = []
    min_f = float("inf")
    for k in range(len(weights)):
        f = u1_function_from_coeffs(coeffs, cosines, k)
        min_f = min(min_f, f)
        values.append(f**zeta)
    raw_coeffs, a0, negative_raw = project_u1(
        values, weights, cosines, n_max, warn_threshold
    )
    new_coeffs = [1.0]
    for c in raw_coeffs[1:]:
        new_coeffs.append(c**r)
    return new_coeffs, a0, negative_raw, min_f


def gap_from_coeff(c: float) -> float:
    c = max(min(c, 1.0 - 1e-300), 1e-300)
    return -math.log(c)


def summarize_su2(beta0: float, coeffs: Sequence[float]) -> Tuple[float, float, float]:
    m = gap_from_coeff(coeffs[1])
    beta_eff = 3.0 / (2.0 * m) if m > 0 else float("inf")
    return m, beta_eff, beta_eff - beta0


def summarize_u1(beta0: float, coeffs: Sequence[float]) -> Tuple[float, float, float]:
    m = gap_from_coeff(coeffs[1])
    beta_eff = 1.0 / (2.0 * m) if m > 0 else float("inf")
    return m, beta_eff, beta_eff - beta0


def run(args: argparse.Namespace) -> None:
    b = args.block
    d = args.dim
    zeta = b ** (d - 2)
    r = b * b
    b0_su2 = 11.0 / (24.0 * math.pi * math.pi)
    one_loop_delta_beta = 8.0 * b0_su2 * math.log(b)
    su2_mk_delta_beta = 0.25

    print("MK-style character-flow diagnostic")
    print(f"b={b}, d={d}, zeta=b^(d-2)={zeta}, strengthening r=b^2={r}")
    print(f"SU(2) heat-kernel MK asymptotic beta decrement: {su2_mk_delta_beta:.9f}")
    print(f"SU(2) one-loop weak-coupling beta decrement for b={b}: {one_loop_delta_beta:.9f}")
    print("Convention: beta_eff is inferred from the lightest-channel tree gap.")
    print()

    su2_weights, su2_chars = make_su2_grid(args.grid_su2, args.j2_max)
    u1_weights, u1_cos = make_u1_grid(args.grid_u1, args.n_max)

    for beta0 in args.beta:
        print("=" * 88)
        print(f"initial beta={beta0:g}")
        print("- SU(2)")
        coeffs, _, neg = initial_su2_coeffs(
            beta0, su2_weights, su2_chars, args.j2_max, args.warn_threshold
        )
        if neg:
            print(f"  warning: initial projection had {neg} negative raw coefficients")
        print("  step      m_1/2        beta_eff      beta_eff-beta0    step_delta_beta")
        prev_beta_eff = None
        for step in range(args.steps + 1):
            m, beta_eff, beta_shift = summarize_su2(beta0, coeffs)
            step_delta = float("nan") if prev_beta_eff is None else prev_beta_eff - beta_eff
            print(
                f"  {step:>3d}  {m:12.6e}  {beta_eff:13.6f}  "
                f"{beta_shift:15.6f}  {step_delta:15.6f}"
            )
            prev_beta_eff = beta_eff
            if step != args.steps:
                coeffs, _, neg, _ = mk_step_su2(
                    coeffs,
                    su2_weights,
                    su2_chars,
                    args.j2_max,
                    zeta,
                    r,
                    args.warn_threshold,
                )
                if neg:
                    print(f"       warning: step projection had {neg} negative raw coefficients")

        print("- U(1)")
        coeffs_u1, _, neg = initial_u1_coeffs(
            beta0, u1_weights, u1_cos, args.n_max, args.warn_threshold
        )
        if neg:
            print(f"  warning: initial projection had {neg} negative raw coefficients")
        print("  step      m_1          beta_eff      beta_eff-beta0    step_delta_beta")
        prev_beta_eff = None
        for step in range(args.steps + 1):
            m, beta_eff, beta_shift = summarize_u1(beta0, coeffs_u1)
            step_delta = float("nan") if prev_beta_eff is None else prev_beta_eff - beta_eff
            print(
                f"  {step:>3d}  {m:12.6e}  {beta_eff:13.6f}  "
                f"{beta_shift:15.6f}  {step_delta:15.6f}"
            )
            prev_beta_eff = beta_eff
            if step != args.steps:
                coeffs_u1, _, neg, _ = mk_step_u1(
                    coeffs_u1,
                    u1_weights,
                    u1_cos,
                    args.n_max,
                    zeta,
                    r,
                    args.warn_threshold,
                )
                if neg:
                    print(f"       warning: step projection had {neg} negative raw coefficients")
        print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--beta", type=float, nargs="+", default=[10.0, 20.0, 50.0, 100.0])
    parser.add_argument("--steps", type=int, default=4)
    parser.add_argument("--block", type=int, default=2)
    parser.add_argument("--dim", type=int, default=4)
    parser.add_argument("--grid-su2", type=int, default=4096)
    parser.add_argument("--grid-u1", type=int, default=4096)
    parser.add_argument("--j2-max", type=int, default=80)
    parser.add_argument("--n-max", type=int, default=80)
    parser.add_argument("--warn-threshold", type=float, default=1e-10)
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
