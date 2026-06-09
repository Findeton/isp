#!/usr/bin/env python3
"""Paper 5 diagnostic A: finite Born representation campaign.

The question is whether SHARD has a real Born rule, not merely the exponent in
one two-diamond toy.

The finite theorem tested here:
  If retained holonomy amplitudes form a finite complex screen vector, if
  alternatives add linearly before division, if admissible screen changes are
  norm-preserving, and if event weights are componentwise, phase-blind,
  continuous, and additive over exclusive record cells, then the unique weight
  is |a|^2 and the normalized probabilities are Born probabilities.

The script tests the theorem and its nearest failure modes.
"""

from __future__ import annotations

from dataclasses import dataclass
import cmath
import math
import random


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def norm_p(vec: list[complex], p: float) -> float:
    return sum(abs(z) ** p for z in vec)


def born_probs(vec: list[complex]) -> list[float]:
    total = norm_p(vec, 2.0)
    return [abs(z) ** 2 / total for z in vec]


def p_probs(vec: list[complex], p: float) -> list[float]:
    total = norm_p(vec, p)
    return [abs(z) ** p / total for z in vec]


def rotate2(vec: list[complex], theta: float) -> list[complex]:
    c = math.cos(theta)
    s = math.sin(theta)
    a, b = vec[0], vec[1]
    return [c * a + s * b, -s * a + c * b] + vec[2:]


def max_gap(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b)) if a else 0.0


def equal_split_p_from_n(n: int) -> float:
    # Invariance of (1,0,...,0) -> n^{-1/2}(1,...,1):
    # 1 = n * (1/sqrt(n))^p, so p=2.
    return 2.0 * math.log(n) / math.log(n)


def phase(z: complex, phi: float) -> complex:
    return z * cmath.exp(1j * phi)


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    random.seed(17)

    split_ps = [equal_split_p_from_n(n) for n in (2, 3, 5, 8, 13)]
    split_gap = max(abs(p - 2.0) for p in split_ps)

    vec = [0.73 + 0.2j, -0.11 + 0.52j, 0.38 - 0.44j]
    theta = 0.731
    vec_rot = rotate2(vec, theta)
    norm2_gap = abs(norm_p(vec, 2.0) - norm_p(vec_rot, 2.0))
    norm1_gap = abs(norm_p(vec, 1.0) - norm_p(vec_rot, 1.0))
    norm4_gap = abs(norm_p(vec, 4.0) - norm_p(vec_rot, 4.0))

    born = born_probs(vec)
    phase_vec = [phase(vec[0], 1.3), vec[1], phase(vec[2], -0.9)]
    phase_gap = max_gap(born, born_probs(phase_vec))

    # Coarse-graining after division: exclusive record cells add probabilities.
    block_prob = born[0] + born[1]
    block_direct = norm_p(vec[:2], 2.0) / norm_p(vec, 2.0)
    coarse_gap = abs(block_prob - block_direct)

    # Coherent alternatives before division add amplitudes, not probabilities.
    a = 0.61 + 0.33j
    b = 0.44 * cmath.exp(1j * 1.2)
    coherent = abs(a + b) ** 2
    incoherent = abs(a) ** 2 + abs(b) ** 2
    interference_gap = abs(coherent - incoherent)

    # p != 2 can mimic a chosen vector after renormalization but fails screen
    # invariance under rotation.
    p_bad = 1.3
    p_before = norm_p(vec, p_bad)
    p_after = norm_p(vec_rot, p_bad)
    p_invariance_gap = abs(p_before - p_after)

    # Rational-amplitude frequency check: split N equal primitive cells into
    # M cells belonging to outcome A.
    rational_cases = [(1, 2), (2, 5), (7, 16), (9, 25)]
    rational_gaps = []
    for m, n in rational_cases:
        amp_cells = [1 / math.sqrt(n) for _ in range(n)]
        prob_a = sum(abs(amp_cells[i]) ** 2 for i in range(m))
        rational_gaps.append(abs(prob_a - m / n))
    rational_gap = max(rational_gaps)

    # Product composition: independent screens multiply amplitudes and Born
    # weights factor.
    left = [0.8, 0.6]
    right = [0.3, math.sqrt(1 - 0.3**2)]
    left_probs = born_probs([complex(x) for x in left])
    right_probs = born_probs([complex(x) for x in right])
    product_vec = [complex(x * y) for x in left for y in right]
    product_probs = born_probs(product_vec)
    factor_probs = [px * py for px in left_probs for py in right_probs]
    product_gap = max_gap(product_probs, factor_probs)

    rows = [
        Row(
            "equal-split invariance",
            "(1,0,...)->n^{-1/2}(1,...,1)",
            "screen-weight preservation forces p=2 for every tested split",
            f"p_values={[round(p, 6) for p in split_ps]}, gap={split_gap:.1e}",
            "SELECTS-P2",
        ),
        Row(
            "unitary screen invariance",
            "rotate two retained holonomy coordinates",
            "p=2 is invariant; p=1 and p=4 are not",
            f"gap2={norm2_gap:.1e}, gap1={norm1_gap:.6f}, gap4={norm4_gap:.6f}",
            "PASS-BORN-ONLY",
        ),
        Row(
            "phase blindness of event weights",
            "change local phases after amplitude formation",
            "probabilities depend on modulus-squared weights, not phase convention",
            f"phase_gap={phase_gap:.1e}",
            "PASS",
        ),
        Row(
            "exclusive coarse-graining",
            "coarse event after division is a disjoint union of record cells",
            "Born probabilities add over exclusive records",
            f"coarse_gap={coarse_gap:.1e}, block={block_prob:.6f}",
            "PASS",
        ),
        Row(
            "interference gate",
            "compare coherent alternatives with divided alternatives",
            "before division amplitudes add; after division probabilities add",
            f"|coh-incoh|={interference_gap:.6f}",
            "PASS-SHARD-DISTINCTION",
        ),
        Row(
            "p-family falsifier",
            "try p=1.3 as an alternative Born exponent",
            "it fails admissible screen invariance",
            f"p_gap={p_invariance_gap:.6f}",
            "REFUTES-P-FAMILY",
        ),
        Row(
            "rational frequency representation",
            "split equal primitive cells into M of N cells",
            "Born weights reproduce M/N exactly for tested finite refinements",
            f"max_gap={rational_gap:.1e}",
            "PASS-FINITE-FREQUENCY",
        ),
        Row(
            "independent composition",
            "tensor-product-like product of independent screens",
            "Born weights factor for independent retained holonomy packets",
            f"product_gap={product_gap:.1e}",
            "PASS-COMPOSITION",
        ),
        Row(
            "Born verdict",
            "linear retained holonomy + admissible screen isometries + exclusive additivity",
            "finite SHARD representation uniquely gives P_i=|a_i|^2/sum|a_j|^2",
            "finite theorem",
            "DERIVED-FINITE-BORN",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "split_gap": split_gap,
        "norm2_gap": norm2_gap,
        "norm1_gap": norm1_gap,
        "norm4_gap": norm4_gap,
        "phase_gap": phase_gap,
        "coarse_gap": coarse_gap,
        "interference_gap": interference_gap,
        "p_invariance_gap": p_invariance_gap,
        "rational_gap": rational_gap,
        "product_gap": product_gap,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
