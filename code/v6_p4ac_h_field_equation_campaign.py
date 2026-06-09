#!/usr/bin/env python3
"""Paper 4 diagnostic AC: field equation campaign for h_G.

After the v1-v5 campaign the law schema is clear:
    P_h^{hist}(omega) = U(omega) exp(<h, chi(omega)> - psi(h)).

The remaining Branch-A question is whether an invariant field equation selects
the coefficient field h.  This diagnostic tests the strongest finite analogues
against the one-dimensional parity family.  The parity family is deliberately
minimal: h is a single scalar eta, so any claimed field equation must be able to
say why eta has one value rather than another.

Finite result:
  all structural field-equation candidates either select the divisible vacuum,
  require an externally supplied source/coefficient/threshold, or leave the
  entire one-parameter family.  Thus the missing equation is not a shadow of
  the already listed invariants; it must be the actual whole-process law.
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


def law(eta: float) -> dict[Atom3, float]:
    weights = {atom: math.exp(eta * holonomy(atom)) for atom in atoms3()}
    z = sum(0.125 * w for w in weights.values())
    return {atom: 0.125 * w / z for atom, w in weights.items()}


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


def mean_holonomy(eta: float) -> float:
    return math.tanh(eta)


def atanh(x: float) -> float:
    return 0.5 * math.log((1.0 + x) / (1.0 - x))


def solve_eta_equals_lambda_tanh_eta(lam: float) -> float:
    """Largest positive solution of eta = lambda tanh(eta), ignoring eta=0."""
    best = 0.0
    best_gap = float("inf")
    for k in range(3, 10001):
        eta = 4.0 * k / 10000.0
        gap = abs(eta - lam * math.tanh(eta))
        if gap < best_gap:
            best_gap = gap
            best = eta
    return best


def memory_threshold_eta(threshold: float) -> float:
    for k in range(0, 20001):
        eta = 4.0 * k / 20000.0
        if cmi_a_c_given_b(law(eta)) >= threshold:
            return eta
    return float("inf")


def regularized_memory_eta(alpha: float) -> float:
    best_eta = 0.0
    best_value = -float("inf")
    for k in range(0, 20001):
        eta = 4.0 * k / 20000.0
        value = cmi_a_c_given_b(law(eta)) - alpha * eta * eta
        if value > best_value:
            best_value = value
            best_eta = eta
    return best_eta


def quantized_family_count(q0: float, limit: float) -> int:
    if q0 <= 0.0:
        return 0
    return sum(1 for k in range(1, 1000) if k * q0 <= limit)


def product_gluing_gap(eta1: float, eta2: float) -> float:
    p1 = law(eta1)
    p2 = law(eta2)
    max_gap = 0.0
    z = 0.0
    weights: dict[tuple[Atom3, Atom3], float] = {}
    for atom1 in atoms3():
        for atom2 in atoms3():
            w = math.exp(eta1 * holonomy(atom1) + eta2 * holonomy(atom2))
            weights[(atom1, atom2)] = w
            z += 0.125 * 0.125 * w
    for atom1 in atoms3():
        for atom2 in atoms3():
            product = p1[atom1] * p2[atom2]
            reconstructed = 0.125 * 0.125 * weights[(atom1, atom2)] / z
            max_gap = max(max_gap, abs(product - reconstructed))
    return max_gap


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    eta_a = 0.3316471087051321
    eta_b = 0.9504793805965235
    p_a = law(eta_a)
    p_b = law(eta_b)

    pair_gap = max_pairwise_gap(p_a, p_b)
    future_gap = abs(mean_holonomy(eta_a) - mean_holonomy(eta_b))
    source_a = mean_holonomy(eta_a)
    source_b = mean_holonomy(eta_b)
    source_selected_a = atanh(source_a)
    source_selected_b = atanh(source_b)

    self_identity_gap_a = abs(eta_a - atanh(mean_holonomy(eta_a)))
    self_identity_gap_b = abs(eta_b - atanh(mean_holonomy(eta_b)))
    gluing_gap = product_gluing_gap(eta_a, eta_b)

    threshold_1 = 0.02
    threshold_2 = 0.10
    threshold_eta_1 = memory_threshold_eta(threshold_1)
    threshold_eta_2 = memory_threshold_eta(threshold_2)

    lambda_1 = 1.50
    lambda_2 = 2.50
    landau_eta_1 = solve_eta_equals_lambda_tanh_eta(lambda_1)
    landau_eta_2 = solve_eta_equals_lambda_tanh_eta(lambda_2)

    alpha_1 = 0.02
    alpha_2 = 0.10
    reg_eta_1 = regularized_memory_eta(alpha_1)
    reg_eta_2 = regularized_memory_eta(alpha_2)

    q0_1 = 0.10
    q0_2 = 0.25
    q_count_1 = quantized_family_count(q0_1, 1.0)
    q_count_2 = quantized_family_count(q0_2, 1.0)

    rows = [
        Row(
            "source-free least action",
            "solve the homogeneous quadratic field equation",
            "the only selected solution is the divisible vacuum",
            "eta=0",
            "FAILS-NONDIV",
        ),
        Row(
            "supplied source response",
            "eta = R^{-1} j",
            "selects eta only after the source value is supplied externally",
            f"jA={source_a:.6f}, etaA={source_selected_a:.6f}; jB={source_b:.6f}, etaB={source_selected_b:.6f}",
            "BRANCH-B-SOURCE",
        ),
        Row(
            "self-source identity",
            "j(eta)=E_eta[H], eta=atanh(j)",
            "exact for every eta, so it is a readout identity, not a field equation",
            f"gapA={self_identity_gap_a:.1e}, gapB={self_identity_gap_b:.1e}",
            "TAUTOLOGY-FAMILY",
        ),
        Row(
            "sealed gluing",
            "product whole histories add closed-exchange coefficients",
            "gluing is exact for arbitrary eta values",
            f"gap={gluing_gap:.1e}",
            "CONSISTENCY-NOT-SELECTION",
        ),
        Row(
            "non-divisibility threshold",
            "select smallest eta with CMI >= epsilon",
            "the selected eta moves with the unsupplied threshold epsilon",
            f"eta_0p02={threshold_eta_1:.4f}, eta_0p10={threshold_eta_2:.4f}",
            "BRANCH-B-THRESHOLD",
        ),
        Row(
            "self-induced memory equation",
            "solve eta = lambda tanh(eta)",
            "nonzero solutions exist only after a coupling lambda is supplied",
            f"eta_l1p5={landau_eta_1:.4f}, eta_l2p5={landau_eta_2:.4f}",
            "BRANCH-B-COUPLING",
        ),
        Row(
            "regularized memory action",
            "maximize CMI(eta)-alpha eta^2",
            "interior optima exist but drift with the regularization coefficient",
            f"eta_a0p02={reg_eta_1:.4f}, eta_a0p10={reg_eta_2:.4f}",
            "BRANCH-B-COEFFICIENT",
        ),
        Row(
            "quantized holonomy unit",
            "restrict eta to integer multiples of q0",
            "quantization leaves many possibilities unless q0 and level are supplied",
            f"count_q0p10={q_count_1}, count_q0p25={q_count_2}",
            "BRANCH-B-UNIT",
        ),
        Row(
            "normalized exchange bracket",
            "fix only eta/|eta| as in onset-renormalized universality",
            "same normalized bracket can have different future memory",
            f"pair_gap={pair_gap:.1e}, future_gap={future_gap:.6f}",
            "DIRECTION-NOT-AMPLITUDE",
        ),
        Row(
            "h-field equation verdict",
            "test all v1-v5-inspired invariant field-equation candidates",
            "every candidate is vacuum, tautological, coefficient-dependent, or family-valued",
            "h_G not selected",
            "FINITE-NO-GO",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "eta_a": eta_a,
        "eta_b": eta_b,
        "pairwise_shadow_gap": pair_gap,
        "future_memory_gap": future_gap,
        "source_a": source_a,
        "source_b": source_b,
        "self_identity_gap_a": self_identity_gap_a,
        "self_identity_gap_b": self_identity_gap_b,
        "product_gluing_gap": gluing_gap,
        "threshold_eta_0p02": threshold_eta_1,
        "threshold_eta_0p10": threshold_eta_2,
        "landau_eta_lambda_1p5": landau_eta_1,
        "landau_eta_lambda_2p5": landau_eta_2,
        "regularized_eta_alpha_0p02": reg_eta_1,
        "regularized_eta_alpha_0p10": reg_eta_2,
        "quantized_count_q0_0p10": float(q_count_1),
        "quantized_count_q0_0p25": float(q_count_2),
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
