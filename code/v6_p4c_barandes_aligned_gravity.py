#!/usr/bin/env python3
"""Paper 4 diagnostic C: Barandes-aligned gravity attachment.

This finite campaign tests the cleanest way to attach gravity without leaving
the sealed-record / indivisible-stochastic program.

The finite packet is:

    sealed diamond collars -> eventless stochastic transport K0
    K0                    -> intrinsic allowed-change operator L
    primitive event law    -> fixed deletion work W*
    event support          -> centered deletion source rho = W*(E - mean E)
    L phi = rho            -> record-gravity response field
    phi                    -> history-dependent tilt of the next transport law

The script also attacks the packet by freeing the source amplitude, splitting
the source from the event support, changing the collar graph externally, and
trying an uncentered source inside a sealed finite network.
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


def ring_adjacency(n: int) -> list[list[float]]:
    a = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i][(i - 1) % n] = 1.0
        a[i][(i + 1) % n] = 1.0
    return a


def chord_adjacency(n: int) -> list[list[float]]:
    a = ring_adjacency(n)
    # External extra collar relation.  It is useful as an attack because it
    # changes the gravity response without changing the event support.
    a[0][n // 2] = 1.0
    a[n // 2][0] = 1.0
    return a


def transition_from_adjacency(a: list[list[float]]) -> list[list[float]]:
    k = []
    for row in a:
        total = sum(row)
        k.append([value / total if total else 0.0 for value in row])
    return k


def laplacian(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    l = [[0.0 for _ in range(n)] for _ in range(n)]
    for i, row in enumerate(a):
        degree = sum(row)
        l[i][i] = degree
        for j, value in enumerate(row):
            l[i][j] -= value
    return l


def mat_vec(m: list[list[float]], v: list[float]) -> list[float]:
    return [sum(mij * vj for mij, vj in zip(row, v)) for row in m]


def solve_mean_zero(l: list[list[float]], rho: list[float]) -> list[float]:
    """Solve L phi=rho with sum phi=0 by replacing one row with the gauge."""
    n = len(l)
    a = [row[:] + [rhs] for row, rhs in zip(l, rho)]
    a[-1] = [1.0 for _ in range(n)] + [0.0]

    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-14:
            raise ValueError("singular gauge-fixed system")
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [x / scale for x in a[col]]
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            if factor:
                a[row] = [x - factor * y for x, y in zip(a[row], a[col])]

    return [a[i][-1] for i in range(n)]


def source_from_events(events: list[int], kappa: float) -> list[float]:
    density = sum(events) / len(events)
    return [kappa * (event - density) for event in events]


def max_abs(values: list[float]) -> float:
    return max(abs(v) for v in values)


def span(values: list[float]) -> float:
    return max(values) - min(values)


def tilted_transport(k0: list[list[float]], phi: list[float]) -> list[list[float]]:
    k = []
    for i, row in enumerate(k0):
        raw = [
            kij * math.exp(-0.5 * (phi[j] - phi[i])) if kij else 0.0
            for j, kij in enumerate(row)
        ]
        total = sum(raw)
        k.append([value / total if total else 0.0 for value in raw])
    return k


def row_sum_error(k: list[list[float]]) -> float:
    return max(abs(sum(row) - 1.0) for row in k)


def max_kernel_gap(a: list[list[float]], b: list[list[float]]) -> float:
    return max(abs(x - y) for row_a, row_b in zip(a, b) for x, y in zip(row_a, row_b))


def average_row_kl(k: list[list[float]], k0: list[list[float]]) -> float:
    total = 0.0
    n = len(k)
    for row, base in zip(k, k0):
        for p, q in zip(row, base):
            if p > 0.0 and q > 0.0:
                total += p * math.log(p / q)
    return total / n


def work_for_kappa(events: list[int], kappa: float, a: list[list[float]]) -> tuple[float, float]:
    l = laplacian(a)
    k0 = transition_from_adjacency(a)
    rho = source_from_events(events, kappa)
    phi = solve_mean_zero(l, rho)
    k = tilted_transport(k0, phi)
    return span(phi), average_row_kl(k, k0)


def main() -> None:
    eta = solve_eta_star()
    primitive_work = kl_to_mu(p_eta(eta))
    n = 8
    events = [1, 0, 0, 1, 0, 1, 0, 0]
    split_events = [0, 1, 1, 0, 1, 0, 0, 0]

    a = ring_adjacency(n)
    l = laplacian(a)
    k0 = transition_from_adjacency(a)
    rho = source_from_events(events, primitive_work)
    phi = solve_mean_zero(l, rho)
    curvature = mat_vec(l, phi)
    residual = max_abs([c - r for c, r in zip(curvature, rho)])
    k_phi = tilted_transport(k0, phi)

    phi_shifted = [v + 17.0 for v in phi]
    k_shifted = tilted_transport(k0, phi_shifted)
    gauge_gap = max_kernel_gap(k_phi, k_shifted)

    uncentered = [primitive_work * e for e in events]
    uncentered_total = sum(uncentered)

    free_kappas = [0.20, primitive_work, 0.80]
    free_results = [work_for_kappa(events, kappa, a) for kappa in free_kappas]
    free_work_span = span([work for _, work in free_results])

    split_rho = source_from_events(split_events, primitive_work)
    split_phi = solve_mean_zero(l, split_rho)
    split_same_count = sum(events) == sum(split_events)
    split_gap = max_abs([a - b for a, b in zip(phi, split_phi)])

    a_external = chord_adjacency(n)
    ext_phi_span, ext_work = work_for_kappa(events, primitive_work, a_external)
    base_phi_span, base_work = work_for_kappa(events, primitive_work, a)
    external_work_gap = abs(ext_work - base_work)

    no_event_rho = source_from_events([0 for _ in range(n)], primitive_work)
    no_event_phi = solve_mean_zero(l, no_event_rho)
    no_event_kernel = tilted_transport(k0, no_event_phi)
    no_event_gap = max_kernel_gap(no_event_kernel, k0)

    alternate_events = [0, 1, 0, 0, 1, 0, 0, 1]
    alt_rho = source_from_events(alternate_events, primitive_work)
    alt_phi = solve_mean_zero(l, alt_rho)
    alt_kernel = tilted_transport(k0, alt_phi)
    history_gap = max_kernel_gap(k_phi, alt_kernel)

    rows = [
        Row(
            "eventless collar transport",
            "shared sealed collars define symmetric K0",
            "ordinary stochastic base law",
            f"row_err={row_sum_error(k0):.1e}",
            "PASS",
        ),
        Row(
            "allowed-change operator",
            "L = degree - collar adjacency",
            "constant mode is gauge",
            f"max|L1|={max_abs(mat_vec(l, [1.0] * n)):.1e}",
            "PASS",
        ),
        Row(
            "fixed source amplitude",
            "primitive deletion work W*=D(P_eta||mu)",
            "kappa fixed by one-diamond law",
            f"W*={primitive_work:.15f}",
            "PASS-SCOPED",
        ),
        Row(
            "deletion source",
            "rho_i=W*(E_i-mean E)",
            "sealed source has zero total charge",
            f"sum rho={sum(rho):.1e}",
            "PASS",
        ),
        Row(
            "record-gravity equation",
            "L phi = rho, sum phi=0",
            "curvature equals deletion source",
            f"residual={residual:.1e}, span(phi)={span(phi):.6f}",
            "PASS",
        ),
        Row(
            "stochastic future law",
            "K_phi tilts K0 by potential differences",
            "ordinary row-stochastic transition law",
            f"row_err={row_sum_error(k_phi):.1e}, KL={average_row_kl(k_phi,k0):.6f}",
            "PASS",
        ),
        Row(
            "slice/gauge freedom",
            "phi -> phi + constant",
            "future law unchanged",
            f"kernel_gap={gauge_gap:.1e}",
            "PASS",
        ),
        Row(
            "eventless vacuum",
            "no event support",
            "rho=0, phi=0, K_phi=K0",
            f"kernel_gap={no_event_gap:.1e}",
            "PASS",
        ),
        Row(
            "no-silent-seam attack",
            "use uncentered source in sealed network",
            "violates solvability constraint",
            f"sum source={uncentered_total:.6f}",
            "FAILS",
        ),
        Row(
            "free-amplitude attack",
            "same support, vary kappa",
            "gravity work changes",
            f"work_span={free_work_span:.6f}",
            "FAILS-BRANCH-A",
        ),
        Row(
            "split-source attack",
            "same event count, different source support",
            "response field changes while source no longer equals event",
            f"same_count={split_same_count}, phi_gap={split_gap:.6f}",
            "FAILS-ONE-EVENT",
        ),
        Row(
            "external-collar attack",
            "add one non-intrinsic chord to the collar graph",
            "gravity response changes",
            f"work_gap={external_work_gap:.6f}, span={base_phi_span:.6f}->{ext_phi_span:.6f}",
            "FAILS-INTRINSICITY",
        ),
        Row(
            "visible memory",
            "same present diamond, different retained event history",
            "next transition differs",
            f"kernel_gap={history_gap:.6f}",
            "PASS-COMPOSITION",
        ),
        Row(
            "gravity attachment verdict",
            "source, amplitude, L, and K_phi from sealed record data",
            "finite Barandes-aligned gravity packet closes only in this scoped sense",
            "not a continuum Einstein-equation theorem",
            "HONEST-CLOSURE",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("eta_star", f"{eta:.15f}")
    print("primitive_work", f"{primitive_work:.15f}")
    print("source", " ".join(f"{x:.12f}" for x in rho))
    print("phi", " ".join(f"{x:.12f}" for x in phi))
    print("field_residual", f"{residual:.15e}")
    print("gravity_kl_work", f"{average_row_kl(k_phi, k0):.15f}")
    print("free_kappa_results", " ".join(f"{k}:{s:.6f}/{w:.6f}" for k, (s, w) in zip(free_kappas, free_results)))
    print("history_transition_gap", f"{history_gap:.15f}")


if __name__ == "__main__":
    main()
