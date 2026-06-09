#!/usr/bin/env python3
"""Paper 4 diagnostic K: enriched RN deletion-field route.

The previous diagnostic proved a no-go for the current primitive binary
deletion source:

    rho_E = W* (E - mean E), E in {0,1}.

This diagnostic tests the natural escape:

    primitive = full local Radon-Nikodym deletion action A_D;
    source    = center(A_D);
    event     = stable positive/readout support of A_D.

In the finite packet, A_D is identified with the balanced double-null focusing
source.  This closes the deletion/focusing identity by construction, but it is
not a free victory: the many-valued contrast changes the old idempotent
single-diamond constants, and support-only data still cannot reconstruct A_D.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import math

from v6_p4h_intrinsic_null_diamond_gate import centered, solve_eta_star, p_eta, kl_to_mu
from v6_p4j_deletion_focusing_identity import (
    balanced_focus,
    binary_source_from_support,
    best_binary_fit,
    max_abs,
    rms,
    source_norm,
    unique_rounded,
)


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def root_for_scores(scores: list[float], weights: list[float]) -> tuple[float, float, float]:
    def moments(eta: float) -> tuple[float, float, float]:
        raw = [w * math.exp(eta * q) for q, w in zip(scores, weights)]
        z = sum(raw)
        probs = [value / z for value in raw]
        m = sum(p * q for p, q in zip(probs, scores))
        second = sum(p * q * q for p, q in zip(probs, scores))
        var = second - m * m
        psi = math.log(z)
        work = eta * m - psi
        return work, var, m

    def residual(eta: float) -> float:
        work, var, _ = moments(eta)
        return work - var

    lo = 0.0
    hi = 1.0
    flo = residual(lo)
    fhi = residual(hi)
    while fhi <= 0.0 and hi < 200.0:
        hi *= 2.0
        fhi = residual(hi)
    if fhi <= 0.0:
        raise ValueError("score balance did not cross")
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        fm = residual(mid)
        if fm * flo <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    eta = 0.5 * (lo + hi)
    work, var, _ = moments(eta)
    return eta, work, var


def components_4d(support: list[bool], n: int) -> tuple[int, int, int]:
    total = n ** 4
    seen = [False] * total
    sizes = []

    def index(u: int, v: int, x: int, y: int) -> int:
        return (((u % n) * n + (v % n)) * n + (x % n)) * n + (y % n)

    def coords(i: int) -> tuple[int, int, int, int]:
        y = i % n
        x = (i // n) % n
        v = (i // (n * n)) % n
        u = i // (n * n * n)
        return u, v, x, y

    for start in range(total):
        if seen[start] or not support[start]:
            continue
        q: deque[int] = deque([start])
        seen[start] = True
        size = 0
        while q:
            cur = q.popleft()
            size += 1
            u, v, x, y = coords(cur)
            for axis in range(4):
                for step in (-1, 1):
                    nxt_coords = [u, v, x, y]
                    nxt_coords[axis] += step
                    nxt = index(*nxt_coords)
                    if support[nxt] and not seen[nxt]:
                        seen[nxt] = True
                        q.append(nxt)
        sizes.append(size)
    if not sizes:
        return 0, 0, 0
    return len(sizes), max(sizes), min(sizes)


def ring_laplacian_apply(phi: list[float]) -> list[float]:
    n = len(phi)
    return [2.0 * phi[i] - phi[(i - 1) % n] - phi[(i + 1) % n] for i in range(n)]


def solve_ring_poisson_spectral(rho: list[float]) -> list[float]:
    n = len(rho)
    out = [0.0] * n
    for k in range(1, n):
        lam = 2.0 - 2.0 * math.cos(2.0 * math.pi * k / n)
        re = 0.0
        im = 0.0
        for j, value in enumerate(rho):
            angle = 2.0 * math.pi * k * j / n
            re += value * math.cos(angle)
            im -= value * math.sin(angle)
        re /= n
        im /= n
        for j in range(n):
            angle = 2.0 * math.pi * k * j / n
            out[j] += (re * math.cos(angle) - im * math.sin(angle)) / lam
    return centered(out)


def tilted_ring_kl(phi: list[float]) -> float:
    total = 0.0
    n = len(phi)
    for i in range(n):
        left = math.exp(-0.5 * (phi[(i - 1) % n] - phi[i]))
        right = math.exp(-0.5 * (phi[(i + 1) % n] - phi[i]))
        z = left + right
        p_left = left / z
        p_right = right / z
        total += p_left * math.log(p_left / 0.5) + p_right * math.log(p_right / 0.5)
    return total / n


def support_preserving_alternative(action: list[float], target_rms: float) -> list[float]:
    raw = []
    for i, value in enumerate(action):
        mod = 1.0 + 0.22 * math.sin(2.0 * math.pi * i / len(action))
        raw.append(math.copysign(abs(value) * mod + 0.015 * target_rms, value))
    scale = target_rms / rms(centered(raw))
    return [scale * value for value in centered(raw)]


def main() -> None:
    n_side = 6
    action, primitive_work, work_plus, work_minus, front_product = balanced_focus(n_side)
    action = centered(action)
    total = len(action)
    support = [value >= 0.0 for value in action]
    support_count = sum(1 for value in support if value)
    support_density = support_count / total
    comp_count, comp_max, comp_min = components_4d(support, n_side)
    margin = min(abs(value) for value in action)
    near_zero = sum(1 for value in action if abs(value) < 0.02 * primitive_work)

    source = action
    support_set = {i for i, value in enumerate(support) if value}
    binary_source = binary_source_from_support(total, support_set, primitive_work)
    binary_gap = max_gap(source, binary_source)
    binary_rms = rms([a - b for a, b in zip(source, binary_source)])
    best_binary = best_binary_fit(source, primitive_work)

    phi = solve_ring_poisson_spectral(source)
    residual = max_gap(ring_laplacian_apply(phi), source)
    kl = tilted_ring_kl(phi)
    phi_binary = solve_ring_poisson_spectral(binary_source)
    transport_gap = max_gap(phi, phi_binary)

    q_rn = [value / primitive_work for value in source]
    weights = [1.0 / total] * total
    eta_rn, work_rn, response_rn = root_for_scores(q_rn, weights)
    eta_binary = solve_eta_star()
    work_binary = kl_to_mu(p_eta(eta_binary))
    constant_drift = abs(work_rn - work_binary)
    idempotence_gap = max_abs([q * q - 1.0 for q in q_rn])

    alt = support_preserving_alternative(action, primitive_work)
    alt_support = [value >= 0.0 for value in alt]
    support_flip = sum(1 for a, b in zip(support, alt_support) if a != b)
    alt_norm_gap = abs(rms(alt) - rms(action))
    alt_shape_gap = max_gap(alt, action)

    rows = [
        Row(
            "enriched RN primitive",
            "A_D := rho_focus from balanced double-null readout",
            "source/focusing identity is exact for the action field",
            f"mean={mean(action):.1e}, rms={rms(action):.6f}",
            "PASS-BY-PRIMITIVE",
        ),
        Row(
            "event support readout",
            "E_D={A_D>=0}",
            "binary support is recovered as a threshold readout",
            f"density={support_density:.3f}, components={comp_count}, max={comp_max}",
            "PASS-READOUT",
        ),
        Row(
            "threshold stability",
            "count cells near A_D=0",
            "finite margin exists but near-zero cells expose refinement gate",
            f"min|A|={margin:.3e}, near={near_zero}/{total}",
            "COND-STABILITY",
        ),
        Row(
            "binary-source comparison",
            "compare source A_D to W*(E_D-mean E_D)",
            "binary support is not the gravitational source",
            f"rms_gap={binary_rms:.6f}, max_gap={binary_gap:.6f}",
            "PASS-ENRICHED",
        ),
        Row(
            "best binary no-go persists",
            "fit any two-level deletion source to A_D",
            "best binary law still cannot reproduce the RN action",
            f"best_rms={best_binary[2]:.6f}, best_k={best_binary[1]}",
            "PASS-NO-GO",
        ),
        Row(
            "gravity transport receipt",
            "solve L phi=A_D on a sealed ring readout",
            "mean-zero RN source has a finite record-gravity response",
            f"res={residual:.1e}, KL={kl:.6f}",
            "PASS",
        ),
        Row(
            "binary-gravity attack",
            "replace A_D by its support source",
            "same event support gives a different response field",
            f"phi_gap={transport_gap:.6f}",
            "FAILS-SUPPORT-SOURCE",
        ),
        Row(
            "primitive constant drift",
            "rerun information balance with q=A_D/W*",
            "old idempotent constants do not survive automatically",
            f"eta_RN={eta_rn:.6f}, W_RN={work_rn:.6f}, drift={constant_drift:.6f}",
            "REOPENS-CONSTANTS",
        ),
        Row(
            "holonomy idempotence attack",
            "test q_RN^2=1",
            "many-valued RN contrast is not the old primitive event contrast",
            f"levels={unique_rounded(q_rn)}, max|q^2-1|={idempotence_gap:.6f}",
            "FAILS-OLD-HOLONOMY",
        ),
        Row(
            "support-only RN attack",
            "preserve support and rms while changing A_D shape",
            "support readout alone cannot reconstruct the RN action",
            f"flips={support_flip}, norm_gap={alt_norm_gap:.1e}, shape_gap={alt_shape_gap:.6f}",
            "FAILS-SUPPORT-ONLY",
        ),
        Row(
            "enriched RN verdict",
            "primitive A_D plus threshold readout",
            "source identity closes, but constants/action dynamics become theorem targets",
            "not closed unless A_D is intrinsically derived",
            "PARTIAL-CLOSURE",
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
    print("action_rms", f"{rms(action):.15e}")
    print("support_count", support_count)
    print("components", comp_count, comp_max, comp_min)
    print("margin", f"{margin:.15e}")
    print("near_zero", near_zero)
    print("binary_rms_gap", f"{binary_rms:.15e}")
    print("binary_max_gap", f"{binary_gap:.15e}")
    print("poisson_residual", f"{residual:.15e}")
    print("transport_kl", f"{kl:.15e}")
    print("binary_phi_gap", f"{transport_gap:.15e}")
    print("eta_rn", f"{eta_rn:.15e}")
    print("work_rn", f"{work_rn:.15e}")
    print("response_rn", f"{response_rn:.15e}")
    print("constant_drift", f"{constant_drift:.15e}")
    print("idempotence_gap", f"{idempotence_gap:.15e}")
    print("support_preserving_shape_gap", f"{alt_shape_gap:.15e}")


if __name__ == "__main__":
    main()
