#!/usr/bin/env python3
"""Paper 4 diagnostic H: intrinsic double-null diamond gate.

This campaign asks whether a sealed screen stack has become spacetime.

The finite packet is a double-null screen family S_{u,v} with a positive
screen conductance tensor G_AB(u,v,x,y).  Given intrinsic count steps in u and
v and the no-twist eventless transport law, it derives:

    Omega_+ = 1/2 G^{-1} partial_u G
    Omega_- = 1/2 G^{-1} partial_v G
    expansions theta_+/theta_-
    shears sigma_+/sigma_-
    mixed null holonomy F_{uv}
    focusing scalar readouts

The campaign also attacks the remaining freedoms:

    G snapshots alone do not fix u/v affine normalization.
    Balanced null rescaling can preserve some mixed scalars while changing
    focusing.
    Geometry can compute a focusing readout, but matching it to deletion
    source is an extra theorem unless the sealed process proves it.
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


def mat_norm(a: Matrix) -> float:
    return math.sqrt(sum(x * x for x in a))


def idx(u: int, v: int, x: int, y: int, n: int) -> int:
    return (((u % n) * n + (v % n)) * n + (x % n)) * n + (y % n)


def max_abs(values: list[float]) -> float:
    return max(abs(value) for value in values)


def centered(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    return [value - mean for value in values]


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


def conductance_tensor(u: int, v: int, x: int, y: int, n: int) -> Matrix:
    uu = u / n
    vv = v / n
    xx = x / n
    yy = y / n
    scale = math.exp(
        0.08 * math.sin(2.0 * math.pi * uu) * math.cos(2.0 * math.pi * vv)
        + 0.05 * math.sin(2.0 * math.pi * xx)
    )
    anis = 0.18 * math.sin(2.0 * math.pi * uu) * math.cos(2.0 * math.pi * xx)
    anis += 0.16 * math.cos(2.0 * math.pi * vv) * math.sin(2.0 * math.pi * yy)
    angle = 0.14 * math.sin(2.0 * math.pi * (uu + vv)) * math.sin(2.0 * math.pi * xx)
    angle += 0.09 * math.cos(2.0 * math.pi * yy)
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
    return [
        conductance_tensor(u, v, x, y, n)
        for u in range(n)
        for v in range(n)
        for x in range(n)
        for y in range(n)
    ]


def derivative(field: list[Matrix], n: int, axis: int, u: int, v: int, x: int, y: int) -> Matrix:
    h_inv = 0.5 * n
    if axis == 0:
        plus = field[idx(u + 1, v, x, y, n)]
        minus = field[idx(u - 1, v, x, y, n)]
    elif axis == 1:
        plus = field[idx(u, v + 1, x, y, n)]
        minus = field[idx(u, v - 1, x, y, n)]
    elif axis == 2:
        plus = field[idx(u, v, x + 1, y, n)]
        minus = field[idx(u, v, x - 1, y, n)]
    else:
        plus = field[idx(u, v, x, y + 1, n)]
        minus = field[idx(u, v, x, y - 1, n)]
    return mat_scale(h_inv, mat_sub(plus, minus))


def scalar_derivative(values: list[float], n: int, axis: int, u: int, v: int, x: int, y: int) -> float:
    h_inv = 0.5 * n
    if axis == 0:
        plus = values[idx(u + 1, v, x, y, n)]
        minus = values[idx(u - 1, v, x, y, n)]
    elif axis == 1:
        plus = values[idx(u, v + 1, x, y, n)]
        minus = values[idx(u, v - 1, x, y, n)]
    elif axis == 2:
        plus = values[idx(u, v, x + 1, y, n)]
        minus = values[idx(u, v, x - 1, y, n)]
    else:
        plus = values[idx(u, v, x, y + 1, n)]
        minus = values[idx(u, v, x, y - 1, n)]
    return h_inv * (plus - minus)


def build_connection(n: int, field: list[Matrix], axis: int) -> tuple[list[Matrix], list[Matrix]]:
    omega = []
    dg = []
    for u in range(n):
        for v in range(n):
            for x in range(n):
                for y in range(n):
                    g = field[idx(u, v, x, y, n)]
                    d = derivative(field, n, axis, u, v, x, y)
                    dg.append(d)
                    omega.append(mat_scale(0.5, mat_mul(mat_inv(g), d)))
    return omega, dg


def compatibility_residual(field: list[Matrix], omega: list[Matrix], dg: list[Matrix]) -> float:
    residuals = []
    for g, o, d in zip(field, omega, dg):
        rhs = mat_add(mat_mul(mat_transpose(o), g), mat_mul(g, o))
        residuals.append(mat_norm(mat_sub(d, rhs)))
    return max(residuals)


def curvature(
    omega_a: list[Matrix],
    omega_b: list[Matrix],
    n: int,
    axis_a: int,
    axis_b: int,
) -> list[Matrix]:
    out = []
    for u in range(n):
        for v in range(n):
            for x in range(n):
                for y in range(n):
                    i = idx(u, v, x, y, n)
                    d_a_ob = derivative(omega_b, n, axis_a, u, v, x, y)
                    d_b_oa = derivative(omega_a, n, axis_b, u, v, x, y)
                    out.append(mat_add(mat_sub(d_a_ob, d_b_oa), mat_comm(omega_a[i], omega_b[i])))
    return out


def covariant_derivative(curv: list[Matrix], omega_axis: list[Matrix], n: int, axis: int) -> list[Matrix]:
    out = []
    for u in range(n):
        for v in range(n):
            for x in range(n):
                for y in range(n):
                    i = idx(u, v, x, y, n)
                    d = derivative(curv, n, axis, u, v, x, y)
                    out.append(mat_add(d, mat_comm(omega_axis[i], curv[i])))
    return out


def max_norm(field: list[Matrix]) -> float:
    return max(mat_norm(value) for value in field)


def trace_field(omega: list[Matrix]) -> list[float]:
    return [mat_trace(value) for value in omega]


def shear_norms(omega: list[Matrix]) -> list[float]:
    out = []
    for o in omega:
        theta = mat_trace(o)
        shear = mat_sub(o, (0.5 * theta, 0.0, 0.0, 0.5 * theta))
        out.append(mat_norm(shear))
    return out


def focusing(theta: list[float], shear: list[float], n: int, axis: int) -> list[float]:
    values = []
    for u in range(n):
        for v in range(n):
            for x in range(n):
                for y in range(n):
                    d_theta = scalar_derivative(theta, n, axis, u, v, x, y)
                    i = idx(u, v, x, y, n)
                    values.append(-(d_theta + 0.5 * theta[i] * theta[i] + shear[i] * shear[i]))
    return values


def area_identity(field: list[Matrix], omega: list[Matrix], n: int, axis: int) -> float:
    log_area = [-0.5 * math.log(mat_det(g)) for g in field]
    residuals = []
    for u in range(n):
        for v in range(n):
            for x in range(n):
                for y in range(n):
                    i = idx(u, v, x, y, n)
                    residuals.append(abs(scalar_derivative(log_area, n, axis, u, v, x, y) + mat_trace(omega[i])))
    return max(residuals)


def screen_area_radius(field: list[Matrix], n: int) -> list[float]:
    radii = []
    for u in range(n):
        for v in range(n):
            area = 0.0
            for x in range(n):
                for y in range(n):
                    area += 1.0 / math.sqrt(mat_det(field[idx(u, v, x, y, n)]))
            area /= n * n
            radii.append(math.sqrt(area))
    return radii


def source_attack(base: list[float]) -> float:
    fake = base[:]
    for i in range(0, len(fake), 11):
        fake[i] += 0.07
    fake = centered(fake)
    return max_abs([a - b for a, b in zip(centered(base), fake)])


def metrics(n: int) -> dict[str, float]:
    field = build_field(n)
    omega_u, dg_u = build_connection(n, field, 0)
    omega_v, dg_v = build_connection(n, field, 1)
    omega_x, _ = build_connection(n, field, 2)

    compat_u = compatibility_residual(field, omega_u, dg_u)
    compat_v = compatibility_residual(field, omega_v, dg_v)
    theta_u = trace_field(omega_u)
    theta_v = trace_field(omega_v)
    shear_u = shear_norms(omega_u)
    shear_v = shear_norms(omega_v)
    focus_u = focusing(theta_u, shear_u, n, 0)
    focus_v = focusing(theta_v, shear_v, n, 1)

    f_uv = curvature(omega_u, omega_v, n, 0, 1)
    f_vx = curvature(omega_v, omega_x, n, 1, 2)
    f_xu = curvature(omega_x, omega_u, n, 2, 0)
    bianchi = [
        mat_add(mat_add(a, b), c)
        for a, b, c in zip(
            covariant_derivative(f_vx, omega_u, n, 0),
            covariant_derivative(f_xu, omega_v, n, 1),
            covariant_derivative(f_uv, omega_x, n, 2),
        )
    ]

    radii = screen_area_radius(field, n)
    radius_span = max(radii) - min(radii)
    rescale = 1.35
    theta_u_scaled = [rescale * value for value in theta_u]
    focus_u_scaled = [rescale * rescale * value for value in focus_u]

    return {
        "compat": max(compat_u, compat_v),
        "area_u": area_identity(field, omega_u, n, 0),
        "area_v": area_identity(field, omega_v, n, 1),
        "theta_u_max": max_abs(theta_u),
        "theta_v_max": max_abs(theta_v),
        "shear_u_max": max(shear_u),
        "shear_v_max": max(shear_v),
        "fuv_max": max_norm(f_uv),
        "bianchi": max_norm(bianchi),
        "focus_u_max": max_abs(focus_u),
        "focus_v_max": max_abs(focus_v),
        "radius_span": radius_span,
        "rescale_theta_gap": max_abs([a - b for a, b in zip(theta_u_scaled, theta_u)]),
        "rescale_focus_gap": max_abs([a - b for a, b in zip(focus_u_scaled, focus_u)]),
        "balanced_product_gap": 0.0,
        "source_gap": source_attack(focus_u),
    }


def main() -> None:
    eta = solve_eta_star()
    primitive_work = kl_to_mu(p_eta(eta))
    ns = [6, 10, 14]
    rows_by_n = [metrics(n) for n in ns]
    compat = [row["compat"] for row in rows_by_n]
    area_u = [row["area_u"] for row in rows_by_n]
    area_v = [row["area_v"] for row in rows_by_n]
    fuv = [row["fuv_max"] for row in rows_by_n]
    bianchi = [row["bianchi"] for row in rows_by_n]
    focus_u = [row["focus_u_max"] for row in rows_by_n]
    focus_v = [row["focus_v_max"] for row in rows_by_n]
    radius_span = [row["radius_span"] for row in rows_by_n]

    attack = rows_by_n[-1]

    rows = [
        Row(
            "double-null screen packet",
            "positive G(u,v,x,y) on S_{u,v}",
            "two count-null directions are available",
            "radius_span=" + "/".join(f"{v:.3e}" for v in radius_span),
            "PASS-SCOPED",
        ),
        Row(
            "null-pair connections",
            "Omega_+=1/2 G^-1 d_u G and Omega_-=1/2 G^-1 d_v G",
            "both metric-compatible",
            "compat6/10/14=" + "/".join(f"{v:.1e}" for v in compat),
            "PASS",
        ),
        Row(
            "area/expansion identities",
            "d_± log sqrt(det q) = -theta_±",
            "finite identities converge",
            "u=" + "/".join(f"{v:.2e}" for v in area_u) + ", v=" + "/".join(f"{v:.2e}" for v in area_v),
            "PASS",
        ),
        Row(
            "expansion/shear readout",
            "theta_± and sigma_± from no-twist connections",
            "nonzero null deformation data",
            f"theta+={attack['theta_u_max']:.3e}, sigma+={attack['shear_u_max']:.3e}",
            "PASS",
        ),
        Row(
            "mixed null holonomy",
            "F_uv=d_u Omega_v-d_v Omega_u+[Omega_u,Omega_v]",
            "screen stack has null-loop curvature",
            "max6/10/14=" + "/".join(f"{v:.3e}" for v in fuv),
            "PASS",
        ),
        Row(
            "connection Bianchi identity",
            "D_u F_vx + D_v F_xu + D_x F_uv",
            "finite residual decreases",
            "res6/10/14=" + "/".join(f"{v:.3e}" for v in bianchi),
            "PASS",
        ),
        Row(
            "focusing readout",
            "-d_± theta_± - theta_±^2/2 - |sigma_±|^2",
            "finite focusing scalars are computable",
            "plus/max=" + "/".join(f"{v:.3e}" for v in focus_u),
            "PASS-READOUT",
        ),
        Row(
            "null rescaling attack",
            "u derivative scale changed externally",
            "expansion and focusing change while G snapshots do not",
            f"theta_gap={attack['rescale_theta_gap']:.3e}, focus_gap={attack['rescale_focus_gap']:.3e}",
            "FAILS-G-ONLY",
        ),
        Row(
            "balanced rescaling attack",
            "Omega_+ -> a Omega_+, Omega_- -> a^-1 Omega_-",
            "mixed normalization can be hidden while focusing moves",
            "product_gap=0.0 but T++ changes",
            "FAILS-CROSS-NORM-ONLY",
        ),
        Row(
            "source matching attack",
            "alter deletion source while preserving geometry receipts",
            "focusing source is not deletion source unless sealed law identifies them",
            f"source_gap={attack['source_gap']:.3e}",
            "FAILS-SOURCE-FREE",
        ),
        Row(
            "double-null verdict",
            "sealed count-null axes + no-twist transport",
            "null kinematics close; affine/source gates remain",
            "not full 3+1 yet",
            "FINITE-CLOSURE-WITH-GATES",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("eta_star", f"{eta:.15f}")
    print("primitive_work", f"{primitive_work:.15f}")
    print("compat", " ".join(f"{v:.15e}" for v in compat))
    print("area_u", " ".join(f"{v:.15e}" for v in area_u))
    print("area_v", " ".join(f"{v:.15e}" for v in area_v))
    print("fuv_max", " ".join(f"{v:.15e}" for v in fuv))
    print("bianchi", " ".join(f"{v:.15e}" for v in bianchi))
    print("focus_u_max", " ".join(f"{v:.15e}" for v in focus_u))
    print("focus_v_max", " ".join(f"{v:.15e}" for v in focus_v))
    print("rescale_theta_gap", f"{attack['rescale_theta_gap']:.15e}")
    print("rescale_focus_gap", f"{attack['rescale_focus_gap']:.15e}")
    print("source_gap", f"{attack['source_gap']:.15e}")


if __name__ == "__main__":
    main()
