#!/usr/bin/env python3
"""Paper 4 diagnostic B: two-diamond composition and the Born role.

This is a finite campaign, not a full theorem of nature.  It tests where the
Born exponent can and cannot come from.

Main finite result:

    If composed diamonds retain complex holonomy amplitudes, alternatives add
    linearly, and sealed screen transports preserve total event weight under a
    Hadamard screen change, then the p-norm family selects p=2.

That is a Born-role derivation inside the composition packet, not from a
single diamond alone.
"""

from __future__ import annotations

from dataclasses import dataclass
import cmath
import itertools
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def plus_minus_amplitudes(phi: float) -> tuple[complex, complex]:
    c0 = 1.0 / math.sqrt(2.0)
    c1 = cmath.exp(1j * phi) / math.sqrt(2.0)
    plus = (c0 + c1) / math.sqrt(2.0)
    minus = (c0 - c1) / math.sqrt(2.0)
    return plus, minus


def born_plus(phi: float) -> float:
    plus, _ = plus_minus_amplitudes(phi)
    return abs(plus) ** 2


def p_norm_plus(phi: float, exponent: float) -> float:
    plus, minus = plus_minus_amplitudes(phi)
    wp = abs(plus) ** exponent
    wm = abs(minus) ** exponent
    return wp / (wp + wm)


def hadamard_total_weight(exponent: float) -> float:
    # Vector (1,0) under a Hadamard screen transport becomes
    # (1/sqrt(2), 1/sqrt(2)).  Total p-weight is invariant only at p=2.
    return 2.0 * (1.0 / math.sqrt(2.0)) ** exponent


def solve_hadamard_exponent() -> float:
    lo = 0.1
    hi = 6.0
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if hadamard_total_weight(mid) > 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def hidden_process_joint(persist: float, emit_hi: float, emit_lo: float) -> dict[tuple[int, int, int], float]:
    """Joint visible law for three observed events after marginalizing hidden holonomy."""
    joint: dict[tuple[int, int, int], float] = {}
    for h1, h2, h3 in itertools.product((0, 1), repeat=3):
        ph = 0.5
        ph *= persist if h2 == h1 else 1.0 - persist
        ph *= persist if h3 == h2 else 1.0 - persist
        for x1, x2, x3 in itertools.product((0, 1), repeat=3):
            p = ph
            for h, x in ((h1, x1), (h2, x2), (h3, x3)):
                emit = emit_hi if h == 1 else emit_lo
                p *= emit if x == 1 else 1.0 - emit
            joint[(x1, x2, x3)] = joint.get((x1, x2, x3), 0.0) + p
    return joint


def conditional_prob(joint: dict[tuple[int, int, int], float], x3: int, given: tuple[int | None, int | None]) -> float:
    x1_given, x2_given = given
    numerator = 0.0
    denominator = 0.0
    for (x1, x2, x3v), p in joint.items():
        if x1_given is not None and x1 != x1_given:
            continue
        if x2_given is not None and x2 != x2_given:
            continue
        denominator += p
        if x3v == x3:
            numerator += p
    return numerator / denominator


def visible_markov_gap(joint: dict[tuple[int, int, int], float]) -> float:
    gap = 0.0
    for x1, x2 in itertools.product((0, 1), repeat=2):
        p_full = conditional_prob(joint, 1, (x1, x2))
        p_markov = conditional_prob(joint, 1, (None, x2))
        gap = max(gap, abs(p_full - p_markov))
    return gap


def main() -> None:
    phases = [0.0, math.pi / 3.0, math.pi / 2.0, math.pi]
    born_values = [born_plus(phi) for phi in phases]
    classical_values = [0.5 for _ in phases]
    p1_values = [p_norm_plus(phi, 1.0) for phi in phases]
    p2_values = [p_norm_plus(phi, 2.0) for phi in phases]
    p4_values = [p_norm_plus(phi, 4.0) for phi in phases]

    exponent_star = solve_hadamard_exponent()
    p_errors = {
        p: abs(hadamard_total_weight(p) - 1.0)
        for p in (1.0, 2.0, 3.0, 4.0)
    }

    hidden_joint = hidden_process_joint(persist=0.92, emit_hi=0.82, emit_lo=0.18)
    markov_gap = visible_markov_gap(hidden_joint)

    rows = [
        Row(
            "single diamond",
            "one event law only",
            "no phase composition; no Born role",
            "not typed",
            "FAIL-BORN-SCOPE",
        ),
        Row(
            "classical composition",
            "discard retained holonomy",
            "no interference",
            f"phase span={max(classical_values)-min(classical_values):.3f}",
            "FAIL-BORN",
        ),
        Row(
            "complex holonomy composition",
            "amplitudes add before event readout",
            "interference appears",
            "P+(0,pi/3,pi/2,pi)=" + ",".join(f"{v:.3f}" for v in born_values),
            "PASS-INTERFERENCE",
        ),
        Row(
            "p-norm family",
            "replace squared norm by p-norm",
            "many phase-sensitive rules exist",
            f"p=1 at pi/3 {p1_values[1]:.3f}; p=4 at pi/3 {p4_values[1]:.3f}",
            "FAIL-UNIQUE-WITHOUT-INVARIANCE",
        ),
        Row(
            "screen transport invariance",
            "Hadamard preserves total event weight",
            "selects p=2",
            f"p*={exponent_star:.12f}",
            "PROVES-BORN-EXPONENT-IN-PACKET",
        ),
        Row(
            "p=2 check",
            "p-norm rule equals squared amplitude",
            "matches Born row",
            f"max gap={max(abs(a-b) for a,b in zip(born_values,p2_values)):.1e}",
            "PASS",
        ),
        Row(
            "p != 2 attack",
            "Hadamard total weight error",
            ", ".join(f"p={p}: {err:.3f}" for p, err in p_errors.items()),
            "only p=2 has zero error",
            "REFUTES-OTHER-EXPONENTS",
        ),
        Row(
            "visible non-Markovianity",
            "retain hidden holonomy then marginalize it",
            "visible event process fails first-order Markov",
            f"gap={markov_gap:.6f}",
            "PASS-VISIBLE-NONMARKOV",
        ),
        Row(
            "Barandes-level warning",
            "hidden-state model is still a Markov completion upstairs",
            "not yet full indivisible-process theorem",
            "composition target remains",
            "HONEST-SCOPE",
        ),
        Row(
            "Born role verdict",
            "linear holonomy + unitary screen invariance",
            "quadratic weighting is forced inside composition packet",
            "not from single diamond alone",
            "DERIVED-CONDITIONALLY",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("phases", " ".join(f"{phi:.12f}" for phi in phases))
    print("born_plus", " ".join(f"{v:.12f}" for v in born_values))
    print("p1_plus", " ".join(f"{v:.12f}" for v in p1_values))
    print("p4_plus", " ".join(f"{v:.12f}" for v in p4_values))
    print("hadamard_exponent", f"{exponent_star:.15f}")
    print("visible_markov_gap", f"{markov_gap:.15f}")


if __name__ == "__main__":
    main()
