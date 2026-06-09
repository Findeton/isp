#!/usr/bin/env python3
"""Paper 3 section 61 diagnostic.

This script audits candidate invariant laws for selecting a positive sealed
diamond record law P_D.  It is deliberately finite and conservative: the goal
is to separate principles that genuinely select a nontrivial law from
principles that only select a law after a moment, action, bridge, Hamiltonian,
or work target has already been supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Row:
    target: str
    principle: str
    selection: str
    obstruction: str
    value: str
    verdict: str


def binary_pair(theta: float) -> dict[tuple[int, int], float]:
    """Uniform-marginal two-screen law P(x,y)=(1+theta*x*y)/4."""
    return {
        (x, y): (1.0 + theta * x * y) / 4.0
        for x in (-1, 1)
        for y in (-1, 1)
    }


def kl(p: dict[tuple[int, ...], float], q: dict[tuple[int, ...], float]) -> float:
    return sum(px * math.log(px / q[x]) for x, px in p.items())


def pair_mi(theta: float) -> float:
    p = binary_pair(theta)
    prod = {xy: 0.25 for xy in p}
    return kl(p, prod)


def theta_for_work(work: float) -> float:
    if not (0.0 <= work < math.log(2.0)):
        raise ValueError("two-bit uniform-marginal work must be in [0, log 2)")
    lo = 0.0
    hi = 1.0 - 1e-13
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if pair_mi(mid) < work:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def l1_span(laws: list[dict[tuple[int, ...], float]]) -> float:
    keys = list(laws[0].keys())
    span = 0.0
    for i, p in enumerate(laws):
        for q in laws[i + 1 :]:
            span = max(span, sum(abs(p[k] - q[k]) for k in keys))
    return span


def schrodinger_product_bridge(mu: tuple[float, float], nu: tuple[float, float]) -> dict[tuple[int, int], float]:
    return {(i, j): mu[i] * nu[j] for i in range(2) for j in range(2)}


def markov_chain_law(alpha: float, flip: float) -> dict[tuple[int, int, int], float]:
    """A-B-C law with A and C conditionally independent over B."""
    law: dict[tuple[int, int, int], float] = {}
    for b in (0, 1):
        pb = alpha if b else 1.0 - alpha
        for a in (0, 1):
            pa = 1.0 - flip if a == b else flip
            for c in (0, 1):
                pc = 1.0 - flip if c == b else flip
                law[(a, b, c)] = pb * pa * pc
    return law


def cmi_abc(law: dict[tuple[int, int, int], float]) -> float:
    """Conditional mutual information I(A:C|B)."""
    p_b: dict[int, float] = {0: 0.0, 1: 0.0}
    p_ab: dict[tuple[int, int], float] = {}
    p_bc: dict[tuple[int, int], float] = {}
    p_abc = law
    for (a, b, c), p in law.items():
        p_b[b] += p
        p_ab[(a, b)] = p_ab.get((a, b), 0.0) + p
        p_bc[(b, c)] = p_bc.get((b, c), 0.0) + p
    total = 0.0
    for (a, b, c), p in p_abc.items():
        total += p * math.log((p * p_b[b]) / (p_ab[(a, b)] * p_bc[(b, c)]))
    return total


def main() -> None:
    rows: list[Row] = []

    theta_laws = [binary_pair(theta) for theta in (0.15, 0.45, 0.75)]
    rows.append(
        Row(
            "old structural axioms",
            "covariance + positivity + projectivity",
            "admits all theta",
            "defect amplitude remains free",
            f"span {l1_span(theta_laws):.3f}",
            "FAIL-UNIQUE",
        )
    )

    uniform = binary_pair(0.0)
    rows.append(
        Row(
            "maximum entropy",
            "maximize H(P) with no physical work constraint",
            "unique uniform law",
            "eventless",
            f"MI {pair_mi(0.0):.3f}",
            "FAIL-TRIVIAL",
        )
    )

    work_target = 0.125
    theta_star = theta_for_work(work_target)
    law_star = binary_pair(theta_star)
    rows.append(
        Row(
            "modular entropic equivalence",
            "max entropy subject to intrinsic W_D",
            "unique tilted law",
            "works only if W_D is intrinsic",
            f"W {work_target:.3f}, theta {theta_star:.4f}",
            "PASS-CONDITIONAL",
        )
    )

    work_targets = [0.03, 0.125, 0.30]
    target_thetas = [theta_for_work(w) for w in work_targets]
    rows.append(
        Row(
            "work-target drift",
            "same rule, different supplied W_D",
            "different laws",
            "W_D is the hidden selector",
            f"theta span {max(target_thetas)-min(target_thetas):.4f}",
            "FAIL-IF-W-SUPPLIED",
        )
    )

    mu = (0.65, 0.35)
    nu = (0.40, 0.60)
    bridge = schrodinger_product_bridge(mu, nu)
    prod_ref = {(i, j): mu[i] * nu[j] for i in range(2) for j in range(2)}
    rows.append(
        Row(
            "Schrodinger bridge, no coupling",
            "minimize KL to count/reference with only screen marginals",
            "unique product bridge",
            "no event-producing correlation",
            f"MI {kl(bridge, prod_ref):.3f}",
            "FAIL-EVENTLESS",
        )
    )

    tilted_bridge = law_star
    rows.append(
        Row(
            "Schrodinger/MaxCal with work",
            "minimize KL with boundary marginals plus work",
            "unique bridge",
            "work/action constraint is extra",
            f"KL-to-uniform {kl(tilted_bridge, uniform):.3f}",
            "COND-ACTION",
        )
    )

    markov_laws = [markov_chain_law(alpha, 0.2) for alpha in (0.25, 0.50, 0.75)]
    rows.append(
        Row(
            "Petz/Markov recovery",
            "exact recovery I(A:C|B)=0",
            "whole family",
            "recovery exactness is consistency, not dynamics",
            f"CMI {cmi_abc(markov_laws[1]):.1e}, span {l1_span(markov_laws):.3f}",
            "FAIL-UNIQUE",
        )
    )

    angles = [0.2, 0.5, 0.9]
    probs = [math.sin(a) ** 2 for a in angles]
    rows.append(
        Row(
            "Barandes/unistochastic form",
            "probabilities from an indivisible stochastic-quantum dilation",
            "family of unitary angles",
            "Hamiltonian/action still selects the law",
            f"p span {max(probs)-min(probs):.3f}",
            "FAIL-DYNAMICS-FREE",
        )
    )

    rows.append(
        Row(
            "causal-action analogue",
            "minimize positive spectral/RN defect action",
            "zero-defect law unless constrained",
            "nonzero event needs volume/trace/work constraint",
            "min at theta 0",
            "FAIL-TRIVIAL-OR-COND",
        )
    )

    rows.append(
        Row(
            "best candidate",
            "sealed modular entropic equivalence law",
            "P_D = max-ent law matching intrinsic screen-volume work profile",
            "not closed until that profile is derived from the diamond",
            f"finite theta {theta_star:.4f}",
            "CANDIDATE-LAW",
        )
    )

    print("| target | principle | selection | obstruction | value | verdict |")
    print("|---|---|---|---|---:|---|")
    for row in rows:
        print(
            f"| {row.target} | {row.principle} | {row.selection} | "
            f"{row.obstruction} | {row.value} | {row.verdict} |"
        )

    print()
    print("candidate_work_target", f"{work_target:.6f}")
    print("candidate_theta", f"{theta_star:.12f}")
    print("candidate_reconstruction_error", f"{abs(pair_mi(theta_star)-work_target):.3e}")
    print("old_family_span", f"{l1_span(theta_laws):.6f}")
    print("work_target_theta_span", f"{max(target_thetas)-min(target_thetas):.6f}")


if __name__ == "__main__":
    main()
