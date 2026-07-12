#!/usr/bin/env python3
"""SUPERSEDED ROUND-1 D13 WITNESS (retained for review provenance).

Replacement: d13_finite_kernel_no_go_exact.py, which uses dependency-free
Q(sqrt(2),i) arithmetic and executes the narrowed 21-check theorem.

Original scope: universal diamond-amplitude gluing is not a selector.

All algebra is SymPy-exact.  No floating-point comparison is used.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.physics.quantum import TensorProduct


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "v10" / "data" / "d13-local-action-family-exact.json"
I = sp.I
SQRT2 = sp.sqrt(2)


def dagger(a: sp.Matrix) -> sp.Matrix:
    return a.conjugate().T


def tr(a: sp.Matrix):
    return sp.simplify(sp.trace(a))


def tp(*items: sp.Matrix) -> sp.Matrix:
    out = items[0]
    for item in items[1:]:
        out = TensorProduct(out, item)
    return sp.Matrix(out)


def zero(a: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in a)


def projector(index: int, dimension: int) -> sp.Matrix:
    v = sp.zeros(dimension, 1)
    v[index, 0] = 1
    return v * dagger(v)


def exchange_unitary(c, s) -> sp.Matrix:
    # exp(i theta X_ex) in |00>,|01>,|10>,|11> order.
    return sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, c, I * s, 0],
            [0, I * s, c, 0],
            [0, 0, 0, 1],
        ]
    )


def concurrence(psi: sp.Matrix):
    a, b, c, d = psi
    return sp.simplify(2 * sp.Abs(a * d - b * c))


def main() -> None:
    one = sp.eye(4)
    x_ex = sp.Matrix(
        [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
    )
    number = sp.diag(0, 1, 1, 2)
    swap = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])

    u_quarter = exchange_unitary(1 / SQRT2, 1 / SQRT2)
    u_half = exchange_unitary(0, 1)
    checks = {}

    checks["unitarity_both"] = zero(dagger(u_quarter) * u_quarter - one) and zero(
        dagger(u_half) * u_half - one
    )
    checks["same_local_generator"] = zero(x_ex * number - number * x_ex) and zero(
        x_ex * swap - swap * x_ex
    )
    checks["exchange_and_number_symmetry_both"] = all(
        zero(u * number - number * u) and zero(u * swap - swap * u)
        for u in (u_quarter, u_half)
    )

    # Exact gluing: two quarter-diamonds equal one half-diamond.
    checks["diamond_gluing"] = zero(u_quarter * u_quarter - u_half)

    # Disjoint construction order is gauge: local firings on (12) and (34) commute.
    u12 = tp(u_quarter, sp.eye(4))
    u34 = tp(sp.eye(4), u_half)
    checks["disjoint_schedule_commutes"] = zero(u12 * u34 - u34 * u12)

    # An overlapping firing is physically ordered rather than gauge.
    z = sp.diag(1, -1)
    z_first = tp(z, sp.eye(2))
    checks["overlap_order_is_physical"] = not zero(u_quarter * z_first - z_first * u_quarter)

    # Independent exact input/output frame changes preserve an instrument probability.
    h = sp.Matrix([[1, 1], [1, -1]]) / SQRT2
    phase = sp.diag(1, I)
    g_in = tp(h, phase)
    g_out = tp(phase, h)
    ket10 = sp.Matrix([0, 0, 1, 0])
    rho = ket10 * dagger(ket10)
    effect10 = projector(2, 4)
    k_prime = g_out * u_quarter * dagger(g_in)
    rho_prime = g_in * rho * dagger(g_in)
    effect_prime = g_out * effect10 * dagger(g_out)
    p = tr(effect10 * u_quarter * rho * dagger(u_quarter))
    p_prime = tr(effect_prime * k_prime * rho_prime * dagger(k_prime))
    checks["independent_frame_covariance"] = sp.simplify(p - p_prime) == 0

    # Exclusive durable records: orthogonal pointer branches have diagonal D.
    # W maps system |j> to system |j> tensor pointer |j>.
    w = sp.zeros(16, 4)
    for j in range(4):
        w[4 * j + j, j] = 1
    checks["record_isometry"] = zero(dagger(w) * w - sp.eye(4))
    branch = w * u_quarter * ket10
    pointer_projectors = []
    for j in range(4):
        pointer_projectors.append(tp(sp.eye(4), projector(j, 4)))
    decoherence = sp.Matrix(
        4,
        4,
        lambda a, b: sp.simplify(
            (dagger(branch) * pointer_projectors[b] * pointer_projectors[a] * branch)[0]
        ),
    )
    checks["durable_records_decohere_exactly"] = all(
        decoherence[a, b] == 0 for a in range(4) for b in range(4) if a != b
    )
    checks["record_probabilities_normalized"] = sp.simplify(tr(decoherence) - 1) == 0

    # Both gates can create a maximally entangled state, so entangling ability
    # does not select the angle.
    ket01 = sp.Matrix([0, 1, 0, 0])
    plus_plus = sp.Matrix([1, 1, 1, 1]) / 2
    c_quarter = concurrence(u_quarter * ket01)
    c_half = concurrence(u_half * plus_plus)
    checks["maximal_entanglement_witness_both"] = c_quarter == 1 and c_half == 1

    p_quarter = sp.simplify(tr(effect10 * u_quarter * rho * dagger(u_quarter)))
    p_half = sp.simplify(tr(effect10 * u_half * rho * dagger(u_half)))
    checks["inequivalent_durable_prediction"] = p_quarter == sp.Rational(1, 2) and p_half == 0

    if not all(checks.values()):
        failed = [name for name, ok in checks.items() if not ok]
        raise AssertionError(f"failed exact checks: {failed}")

    packet = {
        "schema": "d13-local-action-family-exact-v1",
        "arithmetic": "SymPy exact algebra; no floating-point predicates",
        "family": "U(theta)=exp(i theta X_ex)",
        "members": {"theta_pi_over_4": "sqrt-iSWAP", "theta_pi_over_2": "iSWAP"},
        "predictions": {
            "P_10_given_10_theta_pi_over_4": str(p_quarter),
            "P_10_given_10_theta_pi_over_2": str(p_half),
            "concurrence_witness_theta_pi_over_4": str(c_quarter),
            "concurrence_witness_theta_pi_over_2": str(c_half),
        },
        "checks": checks,
        "verdict": "LOCAL-COVARIANT-ACTION-UNIQUENESS-REFUTED",
    }
    payload = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(payload, encoding="utf-8")
    print(f"P(pi/4): {p_quarter}")
    print(f"P(pi/2): {p_half}")
    print(f"CHECKS PASSED: {sum(checks.values())}/{len(checks)}")
    print(f"SEMANTIC SHA256: {hashlib.sha256(payload.encode()).hexdigest()}")
    print("VERDICT: LOCAL-COVARIANT-ACTION-UNIQUENESS-REFUTED")


if __name__ == "__main__":
    main()
