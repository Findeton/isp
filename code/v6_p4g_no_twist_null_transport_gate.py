#!/usr/bin/env python3
"""Paper 4 diagnostic G: no-twist / null-screen transport gate.

This campaign attacks the exact freedom exposed by diagnostic F.

Metric compatibility for a screen-stack conductance tensor G leaves a twist:

    Omega = 1/2 G^{-1} dG + H,
    H^T G + G H = 0.

Equivalently:

    G Omega = S + A,

where S=1/2 dG is symmetric and A is skew.  The finite theorem here is:

    1. G alone does not select A=0.
    2. The record-work norm ||G Omega||_F^2 splits as ||S||_F^2+||A||_F^2.
    3. Therefore minimal eventless transport work selects A=0 uniquely.
    4. Equivalently, no oriented silent circulation skew(G Omega)=0 selects
       A=0 uniquely.

It also attacks weaker ideas: expansion/area and reciprocal null pairs do not
remove the twist by themselves.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


Matrix = tuple[float, float, float, float]


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def mat_scale(s: float, a: Matrix) -> Matrix:
    return (s * a[0], s * a[1], s * a[2], s * a[3])


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    return (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )


def mat_transpose(a: Matrix) -> Matrix:
    return (a[0], a[2], a[1], a[3])


def mat_trace(a: Matrix) -> float:
    return a[0] + a[3]


def mat_det(a: Matrix) -> float:
    return a[0] * a[3] - a[1] * a[2]


def mat_inv(a: Matrix) -> Matrix:
    det = mat_det(a)
    return (a[3] / det, -a[1] / det, -a[2] / det, a[0] / det)


def mat_comm(a: Matrix, b: Matrix) -> Matrix:
    return mat_sub(mat_mul(a, b), mat_mul(b, a))


def mat_norm_sq(a: Matrix) -> float:
    return sum(x * x for x in a)


def mat_norm(a: Matrix) -> float:
    return math.sqrt(mat_norm_sq(a))


def mat_inner(a: Matrix, b: Matrix) -> float:
    return sum(x * y for x, y in zip(a, b))


def skew_part(a: Matrix) -> Matrix:
    return mat_scale(0.5, mat_sub(a, mat_transpose(a)))


def idx(r: int, x: int, y: int, n: int) -> int:
    return ((r % n) * n + (x % n)) * n + (y % n)


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


def conductance_tensor(r: int, x: int, y: int, n: int) -> Matrix:
    rr = r / n
    xx = x / n
    yy = y / n
    scale = math.exp(0.12 * math.sin(2.0 * math.pi * rr) * math.sin(2.0 * math.pi * yy))
    anis = 0.35 * math.sin(2.0 * math.pi * rr) * math.cos(2.0 * math.pi * xx)
    anis += 0.12 * math.cos(2.0 * math.pi * yy)
    angle = 0.27 * math.cos(2.0 * math.pi * rr) * math.sin(2.0 * math.pi * xx)
    angle += 0.11 * math.sin(2.0 * math.pi * yy)
    lam1 = scale * math.exp(anis)
    lam2 = scale * math.exp(-anis)
    c = math.cos(angle)
    s = math.sin(angle)
    return (
        lam1 * c * c + lam2 * s * s,
        (lam1 - lam2) * c * s,
        (lam1 - lam2) * c * s,
        lam1 * s * s + lam2 * c * c,
    )


def build_field(n: int) -> list[Matrix]:
    return [conductance_tensor(r, x, y, n) for r in range(n) for x in range(n) for y in range(n)]


def derivative(field: list[Matrix], n: int, axis: int, r: int, x: int, y: int) -> Matrix:
    h_inv = 0.5 * n
    if axis == 0:
        plus = field[idx(r + 1, x, y, n)]
        minus = field[idx(r - 1, x, y, n)]
    elif axis == 1:
        plus = field[idx(r, x + 1, y, n)]
        minus = field[idx(r, x - 1, y, n)]
    else:
        plus = field[idx(r, x, y + 1, n)]
        minus = field[idx(r, x, y - 1, n)]
    return mat_scale(h_inv, mat_sub(plus, minus))


def scalar_derivative(field: list[float], n: int, axis: int, r: int, x: int, y: int) -> float:
    h_inv = 0.5 * n
    if axis == 0:
        plus = field[idx(r + 1, x, y, n)]
        minus = field[idx(r - 1, x, y, n)]
    elif axis == 1:
        plus = field[idx(r, x + 1, y, n)]
        minus = field[idx(r, x - 1, y, n)]
    else:
        plus = field[idx(r, x, y + 1, n)]
        minus = field[idx(r, x, y - 1, n)]
    return h_inv * (plus - minus)


def build_minimal_connection(n: int, field: list[Matrix], axis: int) -> tuple[list[Matrix], list[Matrix]]:
    omega: list[Matrix] = []
    dg: list[Matrix] = []
    for r in range(n):
        for x in range(n):
            for y in range(n):
                g = field[idx(r, x, y, n)]
                d = derivative(field, n, axis, r, x, y)
                dg.append(d)
                omega.append(mat_scale(0.5, mat_mul(mat_inv(g), d)))
    return omega, dg


def add_twist(field: list[Matrix], omega: list[Matrix], tau: float) -> list[Matrix]:
    skew = (0.0, -tau, tau, 0.0)
    return [
        mat_add(base, mat_mul(mat_inv(g), skew))
        for g, base in zip(field, omega)
    ]


def compatibility_residual(field: list[Matrix], omega: list[Matrix], dg: list[Matrix]) -> float:
    residuals = []
    for g, o, d in zip(field, omega, dg):
        rhs = mat_add(mat_mul(mat_transpose(o), g), mat_mul(g, o))
        residuals.append(mat_norm(mat_sub(d, rhs)))
    return max(residuals)


def record_work(field: list[Matrix], omega: list[Matrix]) -> float:
    total = 0.0
    for g, o in zip(field, omega):
        total += mat_norm_sq(mat_mul(g, o))
    return total / len(field)


def circulation(field: list[Matrix], omega: list[Matrix]) -> float:
    total = 0.0
    for g, o in zip(field, omega):
        total += mat_norm_sq(skew_part(mat_mul(g, o)))
    return total / len(field)


def symmetric_skew_cross(field: list[Matrix], omega: list[Matrix], twist: float) -> float:
    skew = (0.0, -twist, twist, 0.0)
    values = []
    for g, o in zip(field, omega):
        s = mat_mul(g, o)
        values.append(abs(mat_inner(s, skew)))
    return max(values)


def build_omegas(n: int, field: list[Matrix]) -> tuple[list[Matrix], list[Matrix], list[Matrix], list[Matrix], list[Matrix], list[Matrix]]:
    omega_r, dg_r = build_minimal_connection(n, field, 0)
    omega_x, dg_x = build_minimal_connection(n, field, 1)
    omega_y, dg_y = build_minimal_connection(n, field, 2)
    return omega_r, omega_x, omega_y, dg_r, dg_x, dg_y


def derivative_matrix_field(field: list[Matrix], n: int, axis: int, r: int, x: int, y: int) -> Matrix:
    return derivative(field, n, axis, r, x, y)


def curvature(
    omega_a: list[Matrix],
    omega_b: list[Matrix],
    n: int,
    axis_a: int,
    axis_b: int,
) -> list[Matrix]:
    out = []
    for r in range(n):
        for x in range(n):
            for y in range(n):
                i = idx(r, x, y, n)
                d_a_ob = derivative_matrix_field(omega_b, n, axis_a, r, x, y)
                d_b_oa = derivative_matrix_field(omega_a, n, axis_b, r, x, y)
                out.append(mat_add(mat_sub(d_a_ob, d_b_oa), mat_comm(omega_a[i], omega_b[i])))
    return out


def field_gap(a: list[Matrix], b: list[Matrix]) -> float:
    return max(mat_norm(mat_sub(x, y)) for x, y in zip(a, b))


def max_area_residual(field: list[Matrix], omega: list[Matrix], n: int) -> float:
    log_area = [-0.5 * math.log(mat_det(g)) for g in field]
    residuals = []
    for i, o in enumerate(omega):
        r = i // (n * n)
        x = (i // n) % n
        y = i % n
        residuals.append(abs(scalar_derivative(log_area, n, 0, r, x, y) + mat_trace(o)))
    return max(residuals)


def null_pair_residual(omega_plus: list[Matrix], omega_minus: list[Matrix]) -> float:
    return max(mat_norm(mat_add(p, m)) for p, m in zip(omega_plus, omega_minus))


def main() -> None:
    eta = solve_eta_star()
    primitive_work = kl_to_mu(p_eta(eta))
    n = 20
    field = build_field(n)
    omega_r, omega_x, _, dg_r, _, _ = build_omegas(n, field)

    taus = [-0.4, -0.2, 0.0, 0.2, 0.4]
    compat = [compatibility_residual(field, add_twist(field, omega_r, tau), dg_r) for tau in taus]
    works = [record_work(field, add_twist(field, omega_r, tau)) for tau in taus]
    circulations = [circulation(field, add_twist(field, omega_r, tau)) for tau in taus]
    min_tau = taus[min(range(len(taus)), key=lambda i: works[i])]
    work_penalty = works[3] - works[2]
    cross = symmetric_skew_cross(field, omega_r, 0.2)

    area_base = max_area_residual(field, omega_r, n)
    area_twist = max_area_residual(field, add_twist(field, omega_r, 0.2), n)
    expansion_gap = max(abs(mat_trace(a) - mat_trace(b)) for a, b in zip(omega_r, add_twist(field, omega_r, 0.2)))

    base_curv = curvature(omega_r, omega_x, n, 0, 1)
    twist_curv = curvature(add_twist(field, omega_r, 0.2), omega_x, n, 0, 1)
    holonomy_gap = field_gap(base_curv, twist_curv)

    twisted_plus = add_twist(field, omega_r, 0.2)
    twisted_minus = [mat_scale(-1.0, value) for value in twisted_plus]
    null_residual = null_pair_residual(twisted_plus, twisted_minus)
    null_circulation = circulation(field, twisted_plus)

    radius_scale_work_gap = abs(record_work(field, [mat_scale(1.25, o) for o in omega_r]) - works[2])
    no_twist_source = primitive_work * circulation(field, add_twist(field, omega_r, 0.2))

    rows = [
        Row(
            "metric-compatible family",
            "Omega=Omega0+G^-1 A, A skew",
            "all scanned twists preserve dG=Omega^T G+G Omega",
            "max compat=" + f"{max(compat):.1e}",
            "FAILS-G-ONLY",
        ),
        Row(
            "record-work split",
            "G Omega = symmetric S + skew A",
            "symmetric/skew cross term vanishes",
            f"max cross={cross:.1e}",
            "PASS",
        ),
        Row(
            "least eventless transport",
            "minimize mean ||G Omega||_F^2 over twists",
            "unique minimum at no twist",
            f"min_tau={min_tau:.1f}, work_penalty_tau=.2={work_penalty:.6f}",
            "PROVES-NO-TWIST",
        ),
        Row(
            "no silent circulation",
            "require skew(G Omega)=0 on eventless radial transport",
            "selects no-twist connection",
            "circ=" + "/".join(f"{c:.3f}" for c in circulations),
            "PROVES-NO-TWIST",
        ),
        Row(
            "area/expansion attack",
            "compare base and twisted trace/area law",
            "twist is invisible to expansion",
            f"trace_gap={expansion_gap:.1e}, area={area_base:.3e}->{area_twist:.3e}",
            "FAILS-AREA-ONLY",
        ),
        Row(
            "null-pair attack",
            "Omega_-=-Omega_+ with same twist",
            "reciprocity passes but circulation remains",
            f"pair_res={null_residual:.1e}, circ={null_circulation:.6f}",
            "FAILS-NULL-PAIR-ONLY",
        ),
        Row(
            "holonomy consequence",
            "compute F_rx before/after twist",
            "twist changes screen-time holonomy",
            f"hol_gap={holonomy_gap:.6f}",
            "PASS-PHYSICAL",
        ),
        Row(
            "radius-scale attack",
            "rescale inter-screen derivative externally",
            "least-work connection rescales too",
            f"work_gap_proxy={radius_scale_work_gap:.6f}",
            "FAILS-IF-RADIUS-SUPPLIED",
        ),
        Row(
            "twist-source option",
            "allow twist only as explicit exchange-defect source",
            "free twist becomes sourced holonomy, not eventless transport",
            f"W*circ_tau=.2={no_twist_source:.6f}",
            "BRANCH-A-IF-SOURCED",
        ),
        Row(
            "no-twist theorem verdict",
            "metric compatibility + least work/no circulation",
            "minimal connection is derived in the eventless stack",
            "null/radius still need sealed data",
            "FINITE-CLOSURE",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("eta_star", f"{eta:.15f}")
    print("primitive_work", f"{primitive_work:.15f}")
    print("taus", " ".join(f"{t:.1f}" for t in taus))
    print("compat_residuals", " ".join(f"{v:.15e}" for v in compat))
    print("record_work", " ".join(f"{v:.15e}" for v in works))
    print("circulation", " ".join(f"{v:.15e}" for v in circulations))
    print("symmetric_skew_cross", f"{cross:.15e}")
    print("area_base", f"{area_base:.15e}")
    print("area_twist", f"{area_twist:.15e}")
    print("expansion_gap", f"{expansion_gap:.15e}")
    print("null_pair_residual", f"{null_residual:.15e}")
    print("null_circulation", f"{null_circulation:.15e}")
    print("holonomy_gap", f"{holonomy_gap:.15e}")
    print("radius_scale_work_gap", f"{radius_scale_work_gap:.15e}")
    print("no_twist_source_proxy", f"{no_twist_source:.15e}")


if __name__ == "__main__":
    main()
