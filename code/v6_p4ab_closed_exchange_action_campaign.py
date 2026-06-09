#!/usr/bin/env python3
"""Paper 4 diagnostic AB: v1-v5 closed-exchange action campaign.

The v1-v5 clue is strong: the missing law should be a whole-slab/history law
whose action is the complete closed exchange-holonomy ledger.  This diagnostic
tests the strongest finite version of that idea against the parity no-go.

Finite result:
  The closed-exchange Gibbs/RN form is exactly the right representation class:
      P_h(omega) = U(omega) exp(<h, chi(omega)> - psi(h)).
  But the structural v1-v5 receipts do not select h.  They identify the action
  shape and the normalized continuum bracket, not the raw whole-process
  coefficient.  Therefore the whole ISP process law is still the primitive
  selector of h/P^{hist}.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


Atom3 = tuple[int, int, int]


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def atoms3() -> list[Atom3]:
    return [(a, b, c) for a in (-1, 1) for b in (-1, 1) for c in (-1, 1)]


def holonomy(atom: Atom3) -> int:
    a, b, c = atom
    return a * b * c


def uniform() -> dict[Atom3, float]:
    return {atom: 0.125 for atom in atoms3()}


def parity_law(theta: float) -> dict[Atom3, float]:
    return {atom: 0.125 * (1.0 + theta * holonomy(atom)) for atom in atoms3()}


def gibbs_law(eta: float) -> dict[Atom3, float]:
    weights = {atom: math.exp(eta * holonomy(atom)) for atom in atoms3()}
    z = sum(0.125 * w for w in weights.values())
    return {atom: 0.125 * w / z for atom, w in weights.items()}


def tv(p: dict[Atom3, float], q: dict[Atom3, float]) -> float:
    return 0.5 * sum(abs(p[atom] - q[atom]) for atom in p)


def entropy(p: dict[Atom3, float]) -> float:
    return -sum(prob * math.log(prob) for prob in p.values() if prob > 0.0)


def marginal(p: dict[Atom3, float], keep: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    out: dict[tuple[int, ...], float] = {}
    for atom, prob in p.items():
        key = tuple(atom[i] for i in keep)
        out[key] = out.get(key, 0.0) + prob
    return out


def max_pairwise_gap(p: dict[Atom3, float], q: dict[Atom3, float]) -> float:
    gaps = []
    for keep in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
        mp = marginal(p, keep)
        mq = marginal(q, keep)
        gaps.append(max(abs(mp[key] - mq[key]) for key in mp))
    return max(gaps)


def cmi_a_c_given_b(p: dict[Atom3, float]) -> float:
    p_ab = marginal(p, (0, 1))
    p_bc = marginal(p, (1, 2))
    p_b = marginal(p, (1,))
    total = 0.0
    for atom, prob in p.items():
        a, b, c = atom
        if prob > 0.0:
            total += prob * math.log(prob * p_b[(b,)] / (p_ab[(a, b)] * p_bc[(b, c)]))
    return total


def mean_holonomy(p: dict[Atom3, float]) -> float:
    return sum(prob * holonomy(atom) for atom, prob in p.items())


def atanh(x: float) -> float:
    return 0.5 * math.log((1.0 + x) / (1.0 - x))


def max_entropy_eta(grid: list[float]) -> float:
    return max(grid, key=lambda eta: entropy(gibbs_law(eta)))


def max_memory_eta(grid: list[float]) -> float:
    return max(grid, key=lambda eta: cmi_a_c_given_b(gibbs_law(eta)))


def regularized_eta(alpha: float, grid: list[float]) -> float:
    return max(grid, key=lambda eta: cmi_a_c_given_b(gibbs_law(eta)) - alpha * eta * eta)


def born_ratio(scale: float, base: tuple[float, float]) -> float:
    x, y = base
    wx = (scale * x) ** 2
    wy = (scale * y) ** 2
    return wx / (wx + wy)


def normalized_orientation(eta: float) -> float:
    return 0.0 if eta == 0.0 else eta / abs(eta)


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    theta_a = 0.32
    theta_b = 0.74
    eta_a = atanh(theta_a)
    eta_b = atanh(theta_b)
    p_a = gibbs_law(eta_a)
    p_b = gibbs_law(eta_b)

    schema_gap = max(tv(p_a, parity_law(theta_a)), tv(p_b, parity_law(theta_b)))
    pair_gap = max_pairwise_gap(p_a, p_b)
    full_gap = tv(p_a, p_b)
    eta_span = abs(eta_b - eta_a)

    mean_a = mean_holonomy(p_a)
    eta_from_mean_a = atanh(mean_a)
    maxent_recon_gap = abs(eta_from_mean_a - eta_a)

    grid = [k / 100.0 for k in range(0, 301)]
    entropy_eta = max_entropy_eta(grid)
    memory_eta = max_memory_eta(grid)
    reg_eta_weak = regularized_eta(0.02, grid)
    reg_eta_strong = regularized_eta(0.10, grid)

    born_scale_a = born_ratio(abs(eta_a), (1.0, 2.0))
    born_scale_b = born_ratio(abs(eta_b), (1.0, 2.0))
    born_gap = abs(born_scale_a - born_scale_b)

    orient_gap = abs(normalized_orientation(eta_a) - normalized_orientation(eta_b))
    future_gap = abs(mean_holonomy(p_a) - mean_holonomy(p_b))

    rows = [
        Row(
            "closed-exchange Gibbs form",
            "represent parity whole-history laws as U exp(eta H)",
            "the v1-v5 action shape exactly represents the complete law family",
            f"schema_gap={schema_gap:.1e}",
            "PASS-SCHEMA",
        ),
        Row(
            "coefficient selection",
            "compare two eta values with same lower shadows",
            "both are positive closed-holonomy laws but predict different future memory",
            f"pair_gap={pair_gap:.1e}, TV={full_gap:.6f}, eta_span={eta_span:.6f}",
            "FINITE-NO-GO",
        ),
        Row(
            "maximum caliber with fixed holonomy mean",
            "recover eta from E[H]",
            "works only after the complete whole-history moment is supplied",
            f"mean={mean_a:.6f}, recon_gap={maxent_recon_gap:.1e}",
            "READOUT-NOT-SELECTION",
        ),
        Row(
            "entropy and memory selectors",
            "maximize entropy or conditional memory over eta",
            "entropy gives divisible vacuum; memory runs to the grid boundary",
            f"eta_entropy={entropy_eta:.2f}, eta_memory={memory_eta:.2f}",
            "FAILS-AS-LAW",
        ),
        Row(
            "regularized memory selector",
            "maximize CMI - alpha eta^2",
            "a nice interior optimum exists but moves with the free coefficient alpha",
            f"eta_a2={reg_eta_weak:.2f}, eta_a10={reg_eta_strong:.2f}",
            "BRANCH-B-COEFFICIENT",
        ),
        Row(
            "Born exponent compatibility",
            "compare square readout under common holonomy rescaling",
            "the square exponent fixes relative readout but not raw eta magnitude",
            f"born_gap={born_gap:.1e}",
            "EXPONENT-NOT-SCALE",
        ),
        Row(
            "onset-renormalized universality",
            "compare normalized holonomy orientation",
            "the normalized bracket can agree while raw future memory differs",
            f"orient_gap={orient_gap:.1e}, future_gap={future_gap:.6f}",
            "UNIVERSALITY-NOT-LAW",
        ),
        Row(
            "v1-v5 law verdict",
            "finite slabs + exchange holonomy + projectivity + Born readout",
            "these identify the correct law schema but not the cofinal coefficient field",
            "P_hist=P_h, h still selected by whole ISP process",
            "SCHEMA-CLOSED-LAW-OPEN",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "theta_a": theta_a,
        "theta_b": theta_b,
        "eta_a": eta_a,
        "eta_b": eta_b,
        "schema_gap": schema_gap,
        "pairwise_shadow_gap": pair_gap,
        "full_total_variation": full_gap,
        "eta_span": eta_span,
        "mean_holonomy_a": mean_a,
        "eta_from_mean_a": eta_from_mean_a,
        "maxent_reconstruction_gap": maxent_recon_gap,
        "entropy_selector_eta": entropy_eta,
        "memory_selector_eta": memory_eta,
        "regularized_eta_alpha_0p02": reg_eta_weak,
        "regularized_eta_alpha_0p10": reg_eta_strong,
        "born_scale_gap": born_gap,
        "normalized_orientation_gap": orient_gap,
        "future_memory_gap": future_gap,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
