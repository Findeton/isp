#!/usr/bin/env python3
"""Paper 4 diagnostic AD: overlap/sheaf campaign for h_G.

The previous campaigns showed that product gluing, readout completeness, and
response equations do not select h_G.  The remaining Einstein-style structural
candidate is nontrivial overlap consistency: local sealed diamonds should be
restrictions of one coherent whole-history law, independently of decomposition.

Finite result:
  overlap/sheaf consistency is stronger than product gluing, but it still does
  not select h_G.  On path overlaps arbitrary local closed-holonomy coefficients
  glue exactly.  On a loop cover positivity constrains the coefficient but
  leaves a continuum, and even for fixed local coefficient it leaves hidden
  global four-history holonomy.  Maximum-entropy extension can choose the
  hidden global coefficient after local data are supplied, but it does not
  choose the local coefficient itself.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


Atom = tuple[int, ...]


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


TRIPLES_4 = ((0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1))


def atoms(n: int) -> list[Atom]:
    out: list[Atom] = []
    for mask in range(1 << n):
        out.append(tuple(1 if (mask >> i) & 1 else -1 for i in range(n)))
    return out


def prod(atom: Atom, indices: tuple[int, ...]) -> int:
    value = 1
    for index in indices:
        value *= atom[index]
    return value


def normalize(weights: dict[Atom, float]) -> dict[Atom, float]:
    z = sum(weights.values())
    return {atom: value / z for atom, value in weights.items()}


def triple_law_eta(eta: float) -> dict[Atom, float]:
    weights = {atom: math.exp(eta * prod(atom, (0, 1, 2))) for atom in atoms(3)}
    return normalize(weights)


def triple_law_theta(theta: float) -> dict[Atom, float]:
    return {atom: 0.125 * (1.0 + theta * prod(atom, (0, 1, 2))) for atom in atoms(3)}


def path_overlap_law(eta_left: float, eta_right: float) -> dict[Atom, float]:
    weights = {}
    for atom in atoms(4):
        h_left = prod(atom, (0, 1, 2))
        h_right = prod(atom, (1, 2, 3))
        weights[atom] = math.exp(eta_left * h_left + eta_right * h_right)
    return normalize(weights)


def marginal(p: dict[Atom, float], keep: tuple[int, ...]) -> dict[Atom, float]:
    out: dict[Atom, float] = {}
    for atom, prob in p.items():
        key = tuple(atom[i] for i in keep)
        out[key] = out.get(key, 0.0) + prob
    return out


def max_gap(p: dict[Atom, float], q: dict[Atom, float]) -> float:
    return max(abs(p[key] - q[key]) for key in p)


def entropy(p: dict[Atom, float]) -> float:
    return -sum(prob * math.log(prob) for prob in p.values() if prob > 0.0)


def q_interval(theta: float) -> tuple[float, float]:
    lo = -float("inf")
    hi = float("inf")
    for atom in atoms(4):
        s = sum(prod(atom, triple) for triple in TRIPLES_4)
        q_sign = prod(atom, (0, 1, 2, 3))
        if q_sign == 1:
            lo = max(lo, -1.0 - theta * s)
        else:
            hi = min(hi, 1.0 + theta * s)
    return lo, hi


def cycle_law(theta: float, q: float) -> dict[Atom, float]:
    p = {}
    for atom in atoms(4):
        s = sum(prod(atom, triple) for triple in TRIPLES_4)
        q_sign = prod(atom, (0, 1, 2, 3))
        p[atom] = 0.0625 * (1.0 + theta * s + q * q_sign)
    return p


def min_probability(p: dict[Atom, float]) -> float:
    return min(p.values())


def cycle_local_gap(theta: float, q: float) -> float:
    p = cycle_law(theta, q)
    target = triple_law_theta(theta)
    gaps = []
    for triple in TRIPLES_4:
        local = marginal(p, triple)
        gaps.append(max_gap(local, target))
    return max(gaps)


def expectation(p: dict[Atom, float], indices: tuple[int, ...]) -> float:
    return sum(prob * prod(atom, indices) for atom, prob in p.items())


def max_entropy_q(theta: float) -> tuple[float, float]:
    lo, hi = q_interval(theta)
    best_q = lo
    best_s = -float("inf")
    for k in range(1001):
        q = lo + (hi - lo) * k / 1000.0
        p = cycle_law(theta, q)
        s = entropy(p)
        if s > best_s:
            best_s = s
            best_q = q
    return best_q, best_s


def global_entropy_selector() -> tuple[float, float, float]:
    best_theta = 0.0
    best_q = 0.0
    best_s = -float("inf")
    for k in range(0, 501):
        theta = k / 1000.0
        lo, hi = q_interval(theta)
        if lo <= hi:
            q, _ = max_entropy_q(theta)
            s = entropy(cycle_law(theta, q))
            if s > best_s:
                best_s = s
                best_theta = theta
                best_q = q
    return best_theta, best_q, best_s


def admissible_theta_summary() -> tuple[int, float, float]:
    count = 0
    first = 0.0
    last = 0.0
    for k in range(1, 1000):
        theta = k / 1000.0
        lo, hi = q_interval(theta)
        if lo <= hi:
            count += 1
            if first == 0.0:
                first = theta
            last = theta
    return count, first, last


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    eta_left = 0.3316471087051321
    eta_right = 0.9504793805965235
    p_path = path_overlap_law(eta_left, eta_right)
    left_gap = max_gap(marginal(p_path, (0, 1, 2)), triple_law_eta(eta_left))
    right_gap = max_gap(marginal(p_path, (1, 2, 3)), triple_law_eta(eta_right))
    overlap_gap = max_gap(marginal(p_path, (1, 2)), marginal(triple_law_eta(eta_left), (1, 2)))

    eta_same_a = eta_left
    eta_same_b = eta_right
    same_pair_gap = max_gap(marginal(path_overlap_law(eta_same_a, eta_same_a), (1, 2)), marginal(path_overlap_law(eta_same_b, eta_same_b), (1, 2)))
    same_future_gap = abs(math.tanh(eta_same_a) - math.tanh(eta_same_b))

    theta = 0.18
    lo, hi = q_interval(theta)
    q_low = lo + 0.25 * (hi - lo)
    q_high = lo + 0.75 * (hi - lo)
    p_low = cycle_law(theta, q_low)
    p_high = cycle_law(theta, q_high)
    cycle_gap_low = cycle_local_gap(theta, q_low)
    cycle_gap_high = cycle_local_gap(theta, q_high)
    hidden_q_gap = abs(expectation(p_low, (0, 1, 2, 3)) - expectation(p_high, (0, 1, 2, 3)))
    min_prob = min(min_probability(p_low), min_probability(p_high))

    count, first_theta, last_theta = admissible_theta_summary()
    q_star, _ = max_entropy_q(theta)
    q_entropy_gap = abs(expectation(cycle_law(theta, q_star), (0, 1, 2, 3)) - q_star)
    global_theta, global_q, _ = global_entropy_selector()

    rows = [
        Row(
            "path-overlap sheaf gluing",
            "two triples ABC and BCD share BC",
            "a global whole-history law restricts to arbitrary local eta values",
            f"left={left_gap:.1e}, right={right_gap:.1e}, overlap={overlap_gap:.1e}",
            "CONSISTENT-FAMILY",
        ),
        Row(
            "isomorphic local diamonds",
            "force the same eta on each path diamond",
            "same-eta covariance still leaves a one-parameter family",
            f"overlap_gap={same_pair_gap:.1e}, future_gap={same_future_gap:.6f}",
            "COVARIANT-FAMILY",
        ),
        Row(
            "loop-cover existence",
            "four overlapping triples around a 4-history loop",
            "positivity restricts theta but leaves many nonzero choices",
            f"count={count}, theta_range=[{first_theta:.3f},{last_theta:.3f}]",
            "CONSTRAINS-NOT-SELECTS",
        ),
        Row(
            "same local sheaf, different global laws",
            "hold every triple restriction fixed and vary four-body q",
            "local diamonds agree exactly while hidden global holonomy changes",
            f"local_gap={max(cycle_gap_low, cycle_gap_high):.1e}, q_gap={hidden_q_gap:.6f}, minP={min_prob:.6f}",
            "REFUTES-LOCAL-SHEAF-COMPLETENESS",
        ),
        Row(
            "maximum-entropy extension",
            "choose q after local theta is supplied",
            "max entropy can pick hidden q but not the local coefficient theta",
            f"theta={theta:.3f}, q_star={q_star:.6f}, q_gap={q_entropy_gap:.1e}",
            "EXTENSION-NOT-LAW",
        ),
        Row(
            "global entropy over the sheaf family",
            "maximize entropy over theta and q",
            "global max entropy returns the divisible vacuum",
            f"theta={global_theta:.3f}, q={global_q:.3f}",
            "FAILS-NONDIV",
        ),
        Row(
            "overlap/sheaf verdict",
            "path covers + loop covers + positivity + extension",
            "overlap consistency is necessary, but it does not select h_G",
            "needs whole-process law",
            "FINITE-NO-GO",
        ),
    ]

    print_table(rows)
    print()
    values = {
        "eta_left": eta_left,
        "eta_right": eta_right,
        "path_left_gap": left_gap,
        "path_right_gap": right_gap,
        "path_overlap_gap": overlap_gap,
        "same_eta_future_gap": same_future_gap,
        "cycle_theta": theta,
        "cycle_q_lo": lo,
        "cycle_q_hi": hi,
        "cycle_q_low": q_low,
        "cycle_q_high": q_high,
        "cycle_local_gap_low": cycle_gap_low,
        "cycle_local_gap_high": cycle_gap_high,
        "hidden_q_gap": hidden_q_gap,
        "cycle_min_probability": min_prob,
        "admissible_theta_count": float(count),
        "admissible_theta_first": first_theta,
        "admissible_theta_last": last_theta,
        "max_entropy_q_fixed_theta": q_star,
        "max_entropy_global_theta": global_theta,
        "max_entropy_global_q": global_q,
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")


if __name__ == "__main__":
    main()
