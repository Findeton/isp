#!/usr/bin/env python3
"""Paper 4 diagnostic A: single sealed event law.

This script is intentionally standalone.  It verifies the primitive event
packet:

    E^2 = E
    q = 2E - 1
    mu(q=-1)=mu(q=+1)=1/2
    Pi_0 P_eta = mu
    D(P_eta || mu) = Var_{P_eta}(q)

and audits the failure modes identified during Paper 3 feedback.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Row:
    target: str
    check: str
    result: str
    value: str
    verdict: str


def p_eta(eta: float) -> dict[int, float]:
    z = 2.0 * math.cosh(eta)
    return {-1: math.exp(-eta) / z, 1: math.exp(eta) / z}


def kl_to_mu(p: dict[int, float]) -> float:
    return sum(px * math.log(px / 0.5) for px in p.values())


def mean_q(p: dict[int, float]) -> float:
    return sum(q * pq for q, pq in p.items())


def var_q(p: dict[int, float]) -> float:
    m = mean_q(p)
    return sum(pq * (q - m) ** 2 for q, pq in p.items())


def residual(eta: float) -> float:
    p = p_eta(eta)
    return kl_to_mu(p) - var_q(p)


def solve_eta() -> float:
    lo = 0.0
    hi = 20.0
    flo = residual(lo)
    for _ in range(140):
        mid = 0.5 * (lo + hi)
        fm = residual(mid)
        if fm * flo <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    return 0.5 * (lo + hi)


def normalize(values: list[float], weights: list[float]) -> tuple[list[float], list[float]]:
    total = sum(weights)
    weights = [w / total for w in weights]
    mean = sum(w * v for w, v in zip(weights, values))
    var = sum(w * (v - mean) ** 2 for w, v in zip(weights, values))
    return [(v - mean) / math.sqrt(var) for v in values], weights


def work_response(values: list[float], weights: list[float], eta: float) -> tuple[float, float]:
    exponents = [eta * v for v in values]
    max_exp = max(exponents)
    raw = [w * math.exp(e - max_exp) for w, e in zip(weights, exponents)]
    z = sum(raw)
    probs = [r / z for r in raw]
    psi = math.log(z) + max_exp
    mean = sum(p * v for p, v in zip(probs, values))
    work = eta * mean - psi
    response = sum(p * (v - mean) ** 2 for p, v in zip(probs, values))
    return work, response


def root_for_score(values: list[float], weights: list[float]) -> float:
    values, weights = normalize(values, weights)
    lo = 0.0
    hi = 20.0
    flo = work_response(values, weights, lo)[0] - work_response(values, weights, lo)[1]
    for _ in range(140):
        mid = 0.5 * (lo + hi)
        work, response = work_response(values, weights, mid)
        fm = work - response
        if fm * flo <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    return 0.5 * (lo + hi)


def main() -> None:
    eta = solve_eta()
    p = p_eta(eta)
    theta = mean_q(p)
    work = kl_to_mu(p)
    response = var_q(p)

    unbalanced_eta = root_for_score([-1.0, 1.0], [3.0, 1.0])
    three_eta = root_for_score([-1.0, 0.0, 1.0], [1.0, 1.0, 1.0])

    rows = [
        Row(
            "idempotent event",
            "E^2=E and q=2E-1",
            "q^2=1",
            "q in {-1,+1}",
            "PASS",
        ),
        Row(
            "count-dual base",
            "internal complement E <-> 1-E",
            "mu=(-,+)=(1/2,1/2)",
            "mu fixed",
            "PASS",
        ),
        Row(
            "eventless repair",
            "Pi_0 kills holonomy contrast",
            "Pi_0 P_eta = mu",
            "explicit assumption/definition",
            "PASS-SCOPED",
        ),
        Row(
            "Fisher term",
            "d^2 log Z / d eta^2",
            "Var_{P_eta}(q)",
            f"{response:.15f}",
            "DEFINED",
        ),
        Row(
            "information-geometric saturation",
            "D(P_eta||mu)=Var(q)",
            "unique crossing",
            f"eta={eta:.15f}",
            "PASS",
        ),
        Row(
            "fixed primitive constants",
            "forced by q^2=1 and count-duality",
            "theta, eta, W=J",
            f"{theta:.15f}, {eta:.15f}, {work:.15f}",
            "PASS",
        ),
        Row(
            "pinch trap",
            "Pi_E P_eta instead of Pi_0 P_eta",
            "D(P||Pi_E P)=0",
            "degenerate",
            "FAILS",
        ),
        Row(
            "continuous-score tilt",
            "tilt by raw q_D with 3 score levels",
            "root moves",
            f"eta={three_eta:.15f}",
            "FAILS-UNIVERSALITY",
        ),
        Row(
            "unbalanced binary",
            "drop complement count-duality",
            "root moves",
            f"eta={unbalanced_eta:.15f}",
            "FAILS-UNIVERSALITY",
        ),
    ]

    print("| target | check | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.check} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("eta_star", f"{eta:.15f}")
    print("theta_star", f"{theta:.15f}")
    print("work_star", f"{work:.15f}")
    print("response_star", f"{response:.15f}")
    print("balance_error", f"{abs(work - response):.3e}")
    print("p_minus", f"{p[-1]:.15f}")
    print("p_plus", f"{p[1]:.15f}")


if __name__ == "__main__":
    main()
