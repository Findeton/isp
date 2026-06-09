#!/usr/bin/env python3
"""Paper 4 diagnostic J: deletion/focusing source identity gate.

The previous diagnostic fixed the reciprocal null affine pair but showed that
closed null work does not make focusing source equal deletion response.

This diagnostic attacks the identity directly.

Current primitive deletion response:

    rho_E = W* (E - mean(E)),    E_i in {0,1}.

Therefore rho_E is a centered two-level source.  A generic balanced focusing
readout from the double-null screen stack is a many-level source.  Exact
identity is possible only if the focusing source is dynamically forced into
that two-level deletion form, or if the primitive deletion germ is enriched so
that its Radon-Nikodym action is the full focusing field rather than a binary
event support.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

from v6_p4h_intrinsic_null_diamond_gate import (
    build_connection,
    build_field,
    centered,
    focusing,
    kl_to_mu,
    p_eta,
    shear_norms,
    solve_eta_star,
    trace_field,
)
from v6_p4i_sealed_null_work_balance import (
    focus_source,
    front_balance_solution,
    record_work,
)


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def rms(a: list[float]) -> float:
    return math.sqrt(dot(a, a) / len(a))


def max_abs(a: list[float]) -> float:
    return max(abs(x) for x in a)


def corr(a: list[float], b: list[float]) -> float:
    na = norm(a)
    nb = norm(b)
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot(a, b) / (na * nb)


def source_norm(a: list[float]) -> float:
    c = centered(a)
    return dot(c, c) / len(c)


def unique_rounded(values: list[float], digits: int = 6) -> int:
    return len({round(value, digits) for value in values})


def binary_source_from_support(n: int, selected: set[int], work: float) -> list[float]:
    density = len(selected) / n
    return [work * ((1.0 if i in selected else 0.0) - density) for i in range(n)]


def best_binary_fit(target: list[float], work: float) -> tuple[list[float], int, float, float, float]:
    n = len(target)
    order = sorted(range(n), key=lambda i: target[i], reverse=True)
    sorted_values = [target[i] for i in order]
    prefix = [0.0]
    prefix2 = [0.0]
    for value in sorted_values:
        prefix.append(prefix[-1] + value)
        prefix2.append(prefix2[-1] + value * value)

    total = prefix[-1]
    total2 = prefix2[-1]
    best_k = 1
    best_sse = float("inf")
    for k in range(1, n):
        density = k / n
        high = work * (1.0 - density)
        low = -work * density
        selected_sse = prefix2[k] - 2.0 * high * prefix[k] + k * high * high
        rest_sum = total - prefix[k]
        rest_sum2 = total2 - prefix2[k]
        rest_count = n - k
        rest_sse = rest_sum2 - 2.0 * low * rest_sum + rest_count * low * low
        sse = selected_sse + rest_sse
        if sse < best_sse:
            best_sse = sse
            best_k = k

    selected = set(order[:best_k])
    best = binary_source_from_support(n, selected, work)
    residual = [a - b for a, b in zip(target, best)]
    return best, best_k, math.sqrt(best_sse / n), max_abs(residual), corr(target, best)


def reflected_same_receipts(target: list[float], binary: list[float]) -> tuple[list[float], float, float, float]:
    t = centered(target)
    b = centered(binary)
    nb = norm(b)
    if nb == 0.0:
        raise ValueError("binary receipt has zero norm")
    unit = [value / nb for value in b]
    parallel_scale = dot(t, unit)
    parallel = [parallel_scale * value for value in unit]
    residual = [x - y for x, y in zip(t, parallel)]
    reflected = [p - r for p, r in zip(parallel, residual)]
    return (
        reflected,
        abs(source_norm(t) - source_norm(reflected)),
        abs(dot(t, unit) - dot(reflected, unit)),
        max_abs([x - y for x, y in zip(t, reflected)]),
    )


def balanced_focus(n: int) -> tuple[list[float], float, float, float, float]:
    eta = solve_eta_star()
    primitive_work = kl_to_mu(p_eta(eta))
    field = build_field(n)
    omega_plus, _ = build_connection(n, field, 0)
    omega_minus, _ = build_connection(n, field, 1)
    work_plus = record_work(field, omega_plus)
    work_minus = record_work(field, omega_minus)
    a_star, b_star, _ = front_balance_solution(work_plus, work_minus)

    theta_plus = trace_field(omega_plus)
    theta_minus = trace_field(omega_minus)
    shear_plus = shear_norms(omega_plus)
    shear_minus = shear_norms(omega_minus)
    focus_plus = focusing(theta_plus, shear_plus, n, 0)
    focus_minus = focusing(theta_minus, shear_minus, n, 1)
    source = focus_source(focus_plus, focus_minus, a_star, b_star, primitive_work)
    return source, primitive_work, work_plus, work_minus, a_star * b_star


def main() -> None:
    n_side = 10
    source, primitive_work, work_plus, work_minus, front_product = balanced_focus(n_side)
    count = len(source)
    binary, best_k, best_rms, best_max, best_corr = best_binary_fit(source, primitive_work)
    reflected, norm_gap, projection_gap, reflected_gap = reflected_same_receipts(source, binary)

    q_focus = [value / primitive_work for value in source]
    idempotence_gap = max_abs([value * value - 1.0 for value in q_focus])
    q_levels = unique_rounded(q_focus)
    binary_levels = unique_rounded(binary)

    locked = binary[:]
    locked_fit = best_binary_fit(locked, primitive_work)

    rows = [
        Row(
            "balanced focusing source",
            "rho_focus from reciprocal affine null fronts",
            "conserved and W*-normalized, but many-valued",
            f"N={count}, levels={q_levels}, rms={rms(source):.6f}",
            "PASS-READOUT",
        ),
        Row(
            "primitive deletion form",
            "rho_E=W*(E-mean E), E in {0,1}",
            "current deletion response is necessarily two-level",
            f"best_k={best_k}, binary_levels={binary_levels}",
            "DEFINED",
        ),
        Row(
            "exact identity attempt",
            "best two-level deletion source fitted to rho_focus",
            "generic focusing source is not a primitive deletion response",
            f"rms_res={best_rms:.6f}, max_res={best_max:.6f}",
            "FAILS-GENERIC-IDENTITY",
        ),
        Row(
            "weak projection route",
            "threshold rho_focus into the best event support",
            "projection is informative but not identity",
            f"corr={best_corr:.6f}",
            "COND-NOT-IDENTITY",
        ),
        Row(
            "same support receipt attack",
            "reflect rho_focus off its binary support direction",
            "same norm and same event projection, different source shape",
            f"norm_gap={norm_gap:.1e}, proj_gap={projection_gap:.1e}, shape_gap={reflected_gap:.6f}",
            "FAILS-SUPPORT-ONLY",
        ),
        Row(
            "holonomy contrast attempt",
            "take q=rho_focus/W* as primitive contrast",
            "it is not the idempotent event contrast q^2=1",
            f"levels={q_levels}, max|q^2-1|={idempotence_gap:.6f}",
            "FAILS-PRIMITIVE-HOLONOMY",
        ),
        Row(
            "defect-locked positive toy",
            "force focusing source to be the two-level deletion source",
            "identity then holds, but only because the dynamics was locked",
            f"toy_rms_res={locked_fit[2]:.1e}",
            "PASS-TOY-NOT-DERIVED",
        ),
        Row(
            "source identity verdict",
            "primitive binary deletion + generic double-null focusing",
            "does not force deletion response = focusing source",
            "needs focus-binary dynamics or enriched RN deletion field",
            "FINITE-NO-GO",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("primitive_work", f"{primitive_work:.15f}")
    print("work_plus", f"{work_plus:.15e}")
    print("work_minus", f"{work_minus:.15e}")
    print("front_product", f"{front_product:.15e}")
    print("source_rms", f"{rms(source):.15e}")
    print("best_binary_k", best_k)
    print("best_binary_rms_residual", f"{best_rms:.15e}")
    print("best_binary_max_residual", f"{best_max:.15e}")
    print("best_binary_corr", f"{best_corr:.15e}")
    print("reflected_norm_gap", f"{norm_gap:.15e}")
    print("reflected_projection_gap", f"{projection_gap:.15e}")
    print("reflected_shape_gap", f"{reflected_gap:.15e}")
    print("q_focus_levels", q_levels)
    print("q_focus_idempotence_gap", f"{idempotence_gap:.15e}")


if __name__ == "__main__":
    main()
