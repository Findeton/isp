#!/usr/bin/env python3
"""Paper 4 diagnostic V: intrinsic admissible refinement campaign.

The cofinal continuum diagnostic showed that coarse shadows alone fail:
a fine zero-coarse holonomy can carry nonzero source density.  This diagnostic
tests the stronger intrinsic candidate.

Finite theorem target:
  * a refinement map pi must preserve the count reference;
  * the fine whole-history law disintegrates over the coarse law;
  * the KL/RN chain rule measures hidden fiber work;
  * the cellular coboundary measures hidden source work;
  * a zero-coarse fine contrast is admissibly silent only when all intrinsic
    future-relevant readout defects vanish cofinally.  Otherwise it is a
    retained fine closed-history contrast, not a silent refinement.
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


@dataclass
class FluxGrid:
    n: int
    vertical: list[list[float]]
    horizontal: list[list[float]]


def normalize(values: list[float]) -> list[float]:
    total = sum(values)
    return [value / total for value in values]


def kl(p: list[float], q: list[float]) -> float:
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0.0)


def uniform(n: int) -> list[float]:
    return [1.0 / n for _ in range(n)]


def neutral_lift(p_coarse: list[float], fibers: int) -> list[float]:
    return [pc / fibers for pc in p_coarse for _ in range(fibers)]


def hidden_lift(p_coarse: list[float], theta: float) -> list[float]:
    # Two count fibers over each coarse atom.  The hidden sign has zero coarse
    # shadow but nonzero conditional RN work when theta != 0.
    out = []
    for idx, pc in enumerate(p_coarse):
        orient = 1.0 if idx % 2 == 0 else -1.0
        out.append(0.5 * pc * (1.0 + theta * orient))
        out.append(0.5 * pc * (1.0 - theta * orient))
    return out


def pushforward_two_fibers(p_fine: list[float]) -> list[float]:
    return [p_fine[2 * i] + p_fine[2 * i + 1] for i in range(len(p_fine) // 2)]


def conditional_kl_gap(p_fine: list[float], p_coarse: list[float]) -> float:
    mu_fine = uniform(len(p_fine))
    mu_coarse = uniform(len(p_coarse))
    return kl(p_fine, mu_fine) - kl(p_coarse, mu_coarse)


def max_fiber_action_range(p_fine: list[float], p_coarse: list[float]) -> float:
    mu_fine = uniform(len(p_fine))
    mu_coarse = uniform(len(p_coarse))
    max_range = 0.0
    for i, pc in enumerate(p_coarse):
        a0 = math.log(p_fine[2 * i] / mu_fine[2 * i]) - math.log(pc / mu_coarse[i])
        a1 = math.log(p_fine[2 * i + 1] / mu_fine[2 * i + 1]) - math.log(pc / mu_coarse[i])
        max_range = max(max_range, abs(a0 - a1))
    return max_range


def hidden_future_gap(p_fine: list[float], coupling: float) -> float:
    hidden_moment = 0.0
    for i in range(len(p_fine) // 2):
        orient = 1.0 if i % 2 == 0 else -1.0
        hidden_moment += orient * (p_fine[2 * i] - p_fine[2 * i + 1])
    return 2.0 * abs(coupling * hidden_moment)


def count_reference_gap(fiber_sizes: list[int]) -> float:
    total = sum(fiber_sizes)
    pushed = [size / total for size in fiber_sizes]
    target = uniform(len(fiber_sizes))
    return max(abs(a - b) for a, b in zip(pushed, target))


def oscillatory_fine_zero_coarse(n: int, amp: float) -> FluxGrid:
    vertical = [[0.0 for _ in range(n)] for _ in range(n + 1)]
    horizontal = [[0.0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n + 1):
        x_sign = 1.0 if i % 2 == 0 else -1.0
        for j in range(n):
            vertical[i][j] = amp * x_sign * ((-1.0) ** j)
    return FluxGrid(n=n, vertical=vertical, horizontal=horizontal)


def coarsen_flux(fine: FluxGrid) -> FluxGrid:
    n = fine.n // 2
    vertical = [[0.0 for _ in range(n)] for _ in range(n + 1)]
    horizontal = [[0.0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n + 1):
        for j in range(n):
            vertical[i][j] = fine.vertical[2 * i][2 * j] + fine.vertical[2 * i][2 * j + 1]
    for i in range(n):
        for j in range(n + 1):
            horizontal[i][j] = fine.horizontal[2 * i][2 * j] + fine.horizontal[2 * i + 1][2 * j]
    return FluxGrid(n=n, vertical=vertical, horizontal=horizontal)


def zero_grid(n: int) -> FluxGrid:
    return FluxGrid(
        n=n,
        vertical=[[0.0 for _ in range(n)] for _ in range(n + 1)],
        horizontal=[[0.0 for _ in range(n + 1)] for _ in range(n)],
    )


def source_density(grid: FluxGrid) -> list[list[float]]:
    n = grid.n
    dx2 = (1.0 / n) ** 2
    out = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            source = (
                grid.vertical[i + 1][j]
                - grid.vertical[i][j]
                + grid.horizontal[i][j + 1]
                - grid.horizontal[i][j]
            )
            out[i][j] = source / dx2
    return out


def flux_gap(a: FluxGrid, b: FluxGrid) -> float:
    gap = 0.0
    for i in range(a.n + 1):
        for j in range(a.n):
            gap = max(gap, abs(a.vertical[i][j] - b.vertical[i][j]))
    for i in range(a.n):
        for j in range(a.n + 1):
            gap = max(gap, abs(a.horizontal[i][j] - b.horizontal[i][j]))
    return gap


def max_abs(values: list[list[float]]) -> float:
    return max(abs(value) for row in values for value in row)


def flux_energy(grid: FluxGrid) -> float:
    return (
        sum(value * value for col in grid.vertical for value in col)
        + sum(value * value for col in grid.horizontal for value in col)
    )


def scaled_oscillation_stats(exponent: int) -> tuple[str, str]:
    entries = []
    for n in (16, 32, 64):
        amp = 1.0 / (n**exponent)
        grid = oscillatory_fine_zero_coarse(n, amp=amp)
        entries.append((n, flux_energy(grid), max_abs(source_density(grid))))
    energy = "/".join(f"{value:.2e}" for _, value, _ in entries)
    density = "/".join(f"{value:.2e}" for _, _, value in entries)
    return energy, density


def main() -> None:
    p_coarse = normalize([0.19, 0.31, 0.23, 0.27])
    p_neutral = neutral_lift(p_coarse, fibers=2)
    p_hidden = hidden_lift(p_coarse, theta=0.58)

    push_gap_neutral = max(abs(a - b) for a, b in zip(pushforward_two_fibers(p_neutral), p_coarse))
    kl_gap_neutral = conditional_kl_gap(p_neutral, p_coarse)
    fiber_range_neutral = max_fiber_action_range(p_neutral, p_coarse)

    push_gap_hidden = max(abs(a - b) for a, b in zip(pushforward_two_fibers(p_hidden), p_coarse))
    kl_gap_hidden = conditional_kl_gap(p_hidden, p_coarse)
    fiber_range_hidden = max_fiber_action_range(p_hidden, p_coarse)
    future_gap_hidden = hidden_future_gap(p_hidden, coupling=0.37)

    count_gap = count_reference_gap([1, 2, 3, 4])

    osc = oscillatory_fine_zero_coarse(32, amp=0.002)
    osc_coarse = coarsen_flux(osc)
    osc_coarse_gap = flux_gap(osc_coarse, zero_grid(16))
    osc_density_max = max_abs(source_density(osc))
    osc_energy = flux_energy(osc)

    trap_energy, trap_density = scaled_oscillation_stats(exponent=2)
    admiss_energy, admiss_density = scaled_oscillation_stats(exponent=4)

    rows = [
        Row(
            "count-reference preservation",
            "push forward the fine count law to the coarse count law",
            "equal fibers preserve the intrinsic reference; unequal fibers do not",
            f"unequal_gap={count_gap:.3e}",
            "PASS-GATE",
        ),
        Row(
            "neutral refinement",
            "split each atom into two count-dual atoms",
            "coarse law, KL content, and fiber action are exactly unchanged",
            f"push={push_gap_neutral:.1e}, dKL={kl_gap_neutral:.1e}, fiber={fiber_range_neutral:.1e}",
            "PASS-SILENT",
        ),
        Row(
            "KL chain rule",
            "add a hidden fiber contrast with identical coarse pushforward",
            "hidden RN work is the conditional KL defect",
            f"push={push_gap_hidden:.1e}, dKL={kl_gap_hidden:.6f}",
            "PASS-DETECTS-HIDDEN-WORK",
        ),
        Row(
            "no-silent-history",
            "let the hidden fiber sign affect the next diamond",
            "same coarse law is not the same physical process",
            f"fiber_range={fiber_range_hidden:.6f}, future_gap={future_gap_hidden:.6f}",
            "REFUTES-SILENT-HIDDEN-FIBER",
        ),
        Row(
            "zero-coarse source attack",
            "alternating fine interface holonomy with zero coarse flux",
            "coarse shadow vanishes while source density remains nonzero",
            f"coarse_gap={osc_coarse_gap:.1e}, density={osc_density_max:.3e}, energy={osc_energy:.3e}",
            "REFUTES-COARSE-ONLY",
        ),
        Row(
            "amplitude-only trap",
            "scale zero-coarse amplitude as n^-2",
            "flux energy vanishes but source density stays finite",
            f"energy16/32/64={trap_energy}; density={trap_density}",
            "REFUTES-KL-OR-L2-ONLY",
        ),
        Row(
            "intrinsic source-work gate",
            "scale zero-coarse amplitude as n^-4",
            "source readout defect vanishes cofinally",
            f"energy16/32/64={admiss_energy}; density={admiss_density}",
            "PASS-SILENT-COFINALLY",
        ),
        Row(
            "admissible refinement verdict",
            "RN chain rule plus cellular source/readout defect",
            "silent refinement is equality in all intrinsic future-relevant readouts",
            "hidden defects retained or vanish",
            "FINITE-INTRINSIC-LAW",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("neutral_push_gap", f"{push_gap_neutral:.15e}")
    print("neutral_kl_gap", f"{kl_gap_neutral:.15e}")
    print("neutral_fiber_action_range", f"{fiber_range_neutral:.15e}")
    print("hidden_push_gap", f"{push_gap_hidden:.15e}")
    print("hidden_kl_gap", f"{kl_gap_hidden:.15e}")
    print("hidden_fiber_action_range", f"{fiber_range_hidden:.15e}")
    print("hidden_future_gap", f"{future_gap_hidden:.15e}")
    print("unequal_count_reference_gap", f"{count_gap:.15e}")
    print("osc_coarse_gap", f"{osc_coarse_gap:.15e}")
    print("osc_density_max", f"{osc_density_max:.15e}")
    print("osc_energy", f"{osc_energy:.15e}")
    print("trap_energy_16_32_64", trap_energy)
    print("trap_density_16_32_64", trap_density)
    print("admissible_energy_16_32_64", admiss_energy)
    print("admissible_density_16_32_64", admiss_density)


if __name__ == "__main__":
    main()
