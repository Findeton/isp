#!/usr/bin/env python3
"""Paper 4 diagnostic AA: whole-history law selection campaign.

This is the last structural selection test.  It asks whether the now-complete
packet of invariants selects a unique cofinal whole-history law P^{hist}.

Finite result:
  gluing, projectivity, RN identities, readout completeness, source/period
  origin, and non-divisibility do not select a unique law.  A one-parameter
  family of positive parity history laws survives all structural tests.  Thus
  the remaining primitive is the indivisible process law itself.
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


def parity(atom: Atom3) -> int:
    a, b, c = atom
    return a * b * c


def parity_law(theta: float) -> dict[Atom3, float]:
    return {atom: 0.125 * (1.0 + theta * parity(atom)) for atom in atoms3()}


def uniform_law() -> dict[Atom3, float]:
    return {atom: 0.125 for atom in atoms3()}


def tv(p: dict, q: dict) -> float:
    return 0.5 * sum(abs(p[k] - q[k]) for k in p)


def entropy(p: dict) -> float:
    return -sum(value * math.log(value) for value in p.values() if value > 0.0)


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


def rn_action(p: dict[Atom3, float]) -> dict[Atom3, float]:
    u = uniform_law()
    return {atom: math.log(p[atom] / u[atom]) for atom in p}


def parity_coefficient_from_action(action: dict[Atom3, float]) -> float:
    return sum(0.125 * action[atom] * parity(atom) for atom in action)


def reconstruct_from_parity_coeff(coeff: float) -> dict[Atom3, float]:
    weights = {atom: math.exp(coeff * parity(atom)) for atom in atoms3()}
    z = sum(weights.values())
    return {atom: value / z for atom, value in weights.items()}


def rn_identities(p: dict[Atom3, float]) -> tuple[float, float]:
    u = uniform_law()
    action = rn_action(p)
    e_u = sum(u[atom] * math.exp(action[atom]) for atom in p)
    e_p = sum(p[atom] * math.exp(-action[atom]) for atom in p)
    return e_u, e_p


def neutral_refine_push_gap(p: dict[Atom3, float]) -> float:
    fine: dict[tuple[int, int, int, int], float] = {}
    for atom, prob in p.items():
        for d in (-1, 1):
            fine[atom + (d,)] = 0.5 * prob
    pushed: dict[Atom3, float] = {atom: 0.0 for atom in p}
    for atom4, prob in fine.items():
        pushed[atom4[:3]] += prob
    return max(abs(p[atom] - pushed[atom]) for atom in p)


def product_gluing_gap(theta1: float, theta2: float) -> float:
    p1 = parity_law(theta1)
    p2 = parity_law(theta2)
    h1 = parity_coefficient_from_action(rn_action(p1))
    h2 = parity_coefficient_from_action(rn_action(p2))
    max_gap = 0.0
    z = 0.0
    weights: dict[tuple[Atom3, Atom3], float] = {}
    for a1, p_a1 in p1.items():
        for a2, p_a2 in p2.items():
            w = math.exp(h1 * parity(a1) + h2 * parity(a2))
            weights[(a1, a2)] = w
            z += w
    for key, w in weights.items():
        a1, a2 = key
        product_prob = p1[a1] * p2[a2]
        reconstructed = w / z
        max_gap = max(max_gap, abs(product_prob - reconstructed))
    return max_gap


def future_effect(p: dict[Atom3, float]) -> float:
    return sum(prob * parity(atom) for atom, prob in p.items())


def count_nondivisible_interval(threshold: float) -> int:
    count = 0
    for k in range(1, 100):
        theta = k / 100.0
        if cmi_a_c_given_b(parity_law(theta)) >= threshold:
            count += 1
    return count


def max_entropy_theta() -> float:
    best_theta = 0.0
    best_entropy = -1.0
    for k in range(-99, 100):
        theta = k / 100.0
        s = entropy(parity_law(theta))
        if s > best_entropy:
            best_entropy = s
            best_theta = theta
    return best_theta


def max_cmi_theta() -> float:
    best_theta = 0.0
    best_cmi = -1.0
    for k in range(1, 100):
        theta = k / 100.0
        value = cmi_a_c_given_b(parity_law(theta))
        if value > best_cmi:
            best_cmi = value
            best_theta = theta
    return best_theta


def main() -> None:
    theta_a = 0.32
    theta_b = 0.74
    p_a = parity_law(theta_a)
    p_b = parity_law(theta_b)

    pair_gap = max_pairwise_gap(p_a, p_b)
    full_tv = tv(p_a, p_b)
    cmi_a = cmi_a_c_given_b(p_a)
    cmi_b = cmi_a_c_given_b(p_b)
    h_a = parity_coefficient_from_action(rn_action(p_a))
    h_b = parity_coefficient_from_action(rn_action(p_b))
    recon_gap_a = tv(p_a, reconstruct_from_parity_coeff(h_a))
    recon_gap_b = tv(p_b, reconstruct_from_parity_coeff(h_b))
    e_u_a, e_p_a = rn_identities(p_a)
    e_u_b, e_p_b = rn_identities(p_b)
    rn_identity_gap = max(abs(e_u_a - 1.0), abs(e_p_a - 1.0), abs(e_u_b - 1.0), abs(e_p_b - 1.0))
    refine_gap = max(neutral_refine_push_gap(p_a), neutral_refine_push_gap(p_b))
    gluing_gap = product_gluing_gap(theta_a, theta_b)
    future_gap = abs(future_effect(p_a) - future_effect(p_b))

    neg = parity_law(-theta_a)
    sign_cmi_gap = abs(cmi_a_c_given_b(p_a) - cmi_a_c_given_b(neg))
    sign_entropy_gap = abs(entropy(p_a) - entropy(neg))
    sign_future_gap = abs(future_effect(p_a) - future_effect(neg))

    entropy_choice = max_entropy_theta()
    max_cmi_choice = max_cmi_theta()
    nondivisible_count = count_nondivisible_interval(threshold=0.02)

    rows = [
        Row(
            "same shadows, different laws",
            "compare two parity whole-history laws",
            "all one/two marginals agree but the full law differs",
            f"pair_gap={pair_gap:.1e}, TV={full_tv:.6f}",
            "REFUTES-SHADOW-SELECTION",
        ),
        Row(
            "RN/readout completeness",
            "recover each law from its complete parity RN coefficient",
            "complete readout reconstructs but does not select the coefficient",
            f"hA={h_a:.6f}, hB={h_b:.6f}, recon={max(recon_gap_a, recon_gap_b):.1e}",
            "PASS-READOUT-NOT-SELECTION",
        ),
        Row(
            "RN identities",
            "check integral fluctuation identities against count reference",
            "both laws satisfy exact RN consistency",
            f"gap={rn_identity_gap:.1e}",
            "PASS-CONSISTENCY-FAMILY",
        ),
        Row(
            "neutral refinement",
            "split every history atom into count twins",
            "both laws are projectively compatible under neutral refinement",
            f"gap={refine_gap:.1e}",
            "PASS-PROJECTIVE-FAMILY",
        ),
        Row(
            "sealed gluing",
            "independent product of two sealed histories",
            "closed-holonomy coefficients add exactly for arbitrary theta",
            f"gap={gluing_gap:.1e}",
            "PASS-GLUING-FAMILY",
        ),
        Row(
            "non-divisibility family",
            "require positive conditional memory",
            "non-divisibility removes theta=0 but leaves a continuum",
            f"CMI_A={cmi_a:.6f}, CMI_B={cmi_b:.6f}, count>0.02={nondivisible_count}",
            "REFUTES-NONDIV-UNIQUENESS",
        ),
        Row(
            "sign/orientation twin",
            "compare theta and -theta",
            "same entropy and CMI can have different future orientation",
            f"cmi_gap={sign_cmi_gap:.1e}, S_gap={sign_entropy_gap:.1e}, future_gap={sign_future_gap:.6f}",
            "REFUTES-SCALAR-SELECTORS",
        ),
        Row(
            "selector audit",
            "max entropy and max memory over the family",
            "max entropy selects divisible vacuum; max memory runs to boundary",
            f"theta_entropy={entropy_choice:.2f}, theta_maxCMI={max_cmi_choice:.2f}",
            "FAILS-AS-LAW",
        ),
        Row(
            "future-composition difference",
            "use parity moment as retained future coupling",
            "surviving laws predict different next composition",
            f"future_gap={future_gap:.6f}",
            "PHYSICAL-FAMILY",
        ),
        Row(
            "whole-history selection verdict",
            "gluing + projectivity + RN + readout completeness + nondivisibility",
            "the structural packet leaves a positive one-parameter family",
            "P_hist must be primitive/process law",
            "FINITE-NO-GO",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("theta_a", f"{theta_a:.15e}")
    print("theta_b", f"{theta_b:.15e}")
    print("pairwise_shadow_gap", f"{pair_gap:.15e}")
    print("full_total_variation", f"{full_tv:.15e}")
    print("h_a", f"{h_a:.15e}")
    print("h_b", f"{h_b:.15e}")
    print("reconstruction_gap_a", f"{recon_gap_a:.15e}")
    print("reconstruction_gap_b", f"{recon_gap_b:.15e}")
    print("rn_identity_gap", f"{rn_identity_gap:.15e}")
    print("neutral_refinement_gap", f"{refine_gap:.15e}")
    print("product_gluing_gap", f"{gluing_gap:.15e}")
    print("cmi_a", f"{cmi_a:.15e}")
    print("cmi_b", f"{cmi_b:.15e}")
    print("nondivisible_count_threshold_0p02", nondivisible_count)
    print("sign_cmi_gap", f"{sign_cmi_gap:.15e}")
    print("sign_entropy_gap", f"{sign_entropy_gap:.15e}")
    print("sign_future_gap", f"{sign_future_gap:.15e}")
    print("max_entropy_theta", f"{entropy_choice:.15e}")
    print("max_cmi_theta_grid", f"{max_cmi_choice:.15e}")
    print("future_gap", f"{future_gap:.15e}")


if __name__ == "__main__":
    main()
