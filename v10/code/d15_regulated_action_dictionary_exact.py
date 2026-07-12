#!/usr/bin/env python3
"""Exact regulated action -> kernel -> environment-record dictionary.

This is a finite Z2/qubit regional-action witness.  It closes one concrete
dictionary cell required by D15.  It is not a generally covariant gravity
action, a continuum limit, or a selector of nature's action.
"""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

from d13_finite_kernel_no_go_exact import (
    C2, Q2, ZERO, ONE, HALF, ROOT_HALF,
    matrix, eye, dagger, mul, add, scale, mv, outer, trace, kron, basis,
    reduced_second_qubit,
)
from d14_action_record_bridge_exact import Port, Obj, Mor, compose, preserves_record


ROOT = Path(__file__).resolve().parents[2]
D13 = Path(__file__).with_name("d13_finite_kernel_no_go_exact.py")
D14 = Path(__file__).with_name("d14_action_record_bridge_exact.py")
OUT = ROOT / "v10" / "data" / "d15-regulated-action-dictionary-exact.json"
EXPECTED_D13_SHA256 = "1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45"
EXPECTED_D14_SHA256 = "e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425"
EXPECTED_CHECKS = 28
EXPECTED_SEMANTIC_SHA256 = "12f73918e7876a2f423d1d4596163e787f52ac50332f2d59bb941c0381f499fe"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


def h_action_kernel():
    """K(b,a)=2^-1/2 exp(i*pi*a*b)=2^-1/2 (-1)^(a*b)."""
    return matrix(tuple(
        tuple(ROOT_HALF * (-1 if a * b else 1) for a in range(2))
        for b in range(2)
    ))


def cnot_action_kernel():
    """Z2 multiplier path sum for b_c=a_c, b_t=a_t xor a_c."""
    return matrix(tuple(tuple(
        (HALF * sum(((-1) ** (lam * (bc ^ ac)) for lam in range(2)), ZERO))
        * (HALF * sum(((-1) ** (lam * (bt ^ at ^ ac)) for lam in range(2)), ZERO))
        for ac in range(2) for at in range(2)
    ) for bc in range(2) for bt in range(2)))


def seal_from_cnot_with_live():
    """Fix fresh record to 0, apply CNOT S->R, append live collar=1."""
    rows = [[0 for _ in range(2)] for _ in range(8)]
    for system in range(2):
        row = (system * 2 + system) * 2 + 1
        rows[row][system] = 1
    return matrix(rows)


def d14_seal_from_action(cnot):
    """Compose environment injection, action kernel, commit, and live collar in D14."""
    q = Obj((Port("system", 2, owner="cell-A"),))
    env = Obj((Port("environment", 2, owner="cell-A"),))
    record = Obj((Port("record", 2, sealed=True, owner="cell-A", record_id="R"),))
    collar = Obj((Port("collar", 2, owner="cell-A"),))

    inject_rows = [[0 for _ in range(2)] for _ in range(4)]
    for s in range(2):
        inject_rows[2 * s][s] = 1
    inject = Mor("fresh-environment-|0>", q, q.tensor(env), matrix(inject_rows))
    interaction = Mor("CNOT-action", q.tensor(env), q.tensor(env), cnot)
    commit = Mor("environment-to-protected-record", q.tensor(env), q.tensor(record), eye(4))

    live_rows = [[0 for _ in range(4)] for _ in range(8)]
    for source in range(4):
        live_rows[2 * source + 1][source] = 1
    emit_live = Mor("emit-live-collar", q.tensor(record),
                    q.tensor(record).tensor(collar), matrix(live_rows))
    return compose(emit_live, compose(commit, compose(interaction, inject))), q, record, collar


def cnot_four(two_bit_kernel, control, target):
    rows = [[0 for _ in range(16)] for _ in range(16)]
    for source in range(16):
        in_bits = [(source >> shift) & 1 for shift in (3, 2, 1, 0)]
        in_pair = 2 * in_bits[control] + in_bits[target]
        for out_pair in range(4):
            amp = two_bit_kernel[out_pair][in_pair]
            if amp == ZERO:
                continue
            out_bits = list(in_bits)
            out_bits[control], out_bits[target] = divmod(out_pair, 2)
            output = 8 * out_bits[0] + 4 * out_bits[1] + 2 * out_bits[2] + out_bits[3]
            rows[output][source] = amp
    return matrix(rows)


def reduced_first_qubit(rho):
    return tuple(tuple(
        sum((rho[2 * a + b][2 * ap + b] for b in range(2)), ZERO)
        for ap in range(2)
    ) for a in range(2))


def sealed_record_distribution(state):
    out = [Q2(), Q2()]
    for index, amp in enumerate(state):
        record = (index // 2) % 2
        out[record] += amp.norm2()
    return tuple(out)


def apply_system_to_sealed(u, state):
    out = [ZERO] * 8
    for so in range(2):
        for si in range(2):
            for record in range(2):
                for collar in range(2):
                    out[(so * 2 + record) * 2 + collar] += (
                        u[so][si] * state[(si * 2 + record) * 2 + collar]
                    )
    return tuple(out)


def system_zero_probability_sealed(state):
    return sum((state[(0 * 2 + r) * 2 + c].norm2()
                for r in range(2) for c in range(2)), Q2())


def diagonal_probabilities(rho):
    return tuple(rho[i][i] for i in range(len(rho)))


def main():
    d13_hash = sha256(D13.read_bytes()).hexdigest()
    d14_hash = sha256(D14.read_bytes()).hexdigest()
    check(d13_hash == EXPECTED_D13_SHA256, "reviewed exact arithmetic dependency hash")
    check(d14_hash == EXPECTED_D14_SHA256, "reviewed D14 bridge dependency hash")

    h = h_action_kernel()
    cnot = cnot_action_kernel()
    expected_h = matrix(((ROOT_HALF, ROOT_HALF), (ROOT_HALF, -ROOT_HALF)))
    check(h == expected_h, "local phase plus supplied vertex measure yields the Hadamard kernel")
    check(mul(dagger(h), h) == eye(2), "action-derived Hadamard kernel is unitary")
    check(mul(dagger(cnot), cnot) == eye(4), "constraint-action CNOT kernel is unitary")
    check(cnot == matrix(((1, 0, 0, 0), (0, 1, 0, 0),
                          (0, 0, 0, 1), (0, 0, 1, 0))),
          "Z2 multiplier sum exactly generates the CNOT support zeros")

    # Gluing is the internal path sum, with the vertex measure used once.
    glued = mul(h, h)
    manual_00 = sum((h[0][internal] * h[internal][0]
                     for internal in range(2)), ZERO)
    manual_10 = sum((h[1][internal] * h[internal][0]
                     for internal in range(2)), ZERO)
    check(glued == eye(2), "two regional action cells glue to the identity kernel")
    check(manual_00 == ONE and manual_10 == ZERO,
          "internal boundary sum gives constructive and destructive interference")

    # Disjoint action cells have no physical ordering.
    z = matrix(((1, 0), (0, -1)))
    check(mul(kron(h, eye(2)), kron(eye(2), z))
          == mul(kron(eye(2), z), kron(h, eye(2))),
          "disjoint action cells commute by tensor interchange")

    # The same local action generates Bell correlations.
    prepare_bell = mul(cnot, kron(h, eye(2)))
    bell = mv(prepare_bell, basis(4, 0))
    bell_rho = outer(bell, bell)
    check(bell == (ROOT_HALF, ZERO, ZERO, ROOT_HALF),
          "action-derived local gates prepare the exact Bell state")
    check(reduced_first_qubit(bell_rho) == scale(HALF, eye(2))
          and reduced_second_qubit(bell_rho) == scale(HALF, eye(2)),
          "Bell state has exact maximally mixed local marginals")
    zz_same = diagonal_probabilities(bell_rho)[0] + diagonal_probabilities(bell_rho)[3]
    check(zz_same == ONE, "Bell state has exact perfect same-basis correlation")
    local_h = kron(h, eye(2))
    check(reduced_second_qubit(mul(local_h, mul(bell_rho, dagger(local_h))))
          == reduced_second_qubit(bell_rho),
          "one action-derived entangled no-signalling marginal passes")

    # Derive the seal from the same CNOT action plus a supplied |0> environment.
    seal = seal_from_cnot_with_live()
    d14_seal, q_obj, record_obj, collar_obj = d14_seal_from_action(cnot)
    check(d14_seal.amp == seal,
          "D14 typed composition derives the seal from environment injection and CNOT action")
    check(d14_seal.target == q_obj.tensor(record_obj).tensor(collar_obj),
          "action dictionary lands in the actual D14 protected-record and collar types")
    check(all(port.owner == "cell-A" for port in d14_seal.source.ports + d14_seal.target.ports),
          "the finite action dictionary is confined to one explicit owned component")
    check(mul(dagger(seal), seal) == eye(2),
          "CNOT action plus fresh environment yields an isometric live seal")
    plus = mv(h, basis(2, 0))
    sealed = mv(seal, plus)
    check(sealed_record_distribution(sealed) == (Q2.make(F(1, 2)), Q2.make(F(1, 2))),
          "action-derived environment carries the Born record distribution")
    check(all(sealed[(s * 2 + r) * 2] == ZERO for s in range(2) for r in range(2)),
          "every action-derived seal branch carries live collar label one")

    # Tracing the environment derives Z-basis decoherence from the interaction.
    bell_sr = mv(cnot, kron(matrix((plus,)), matrix(((1, 0),)))[0])
    rho_sr = outer(bell_sr, bell_sr)
    reduced_s = reduced_first_qubit(rho_sr)
    check(reduced_s == scale(HALF, eye(2)),
          "tracing the locally coupled environment exactly decoheres the pointer basis")

    # A record changes the later interference, and later system dynamics does not rewrite it.
    coherent_p0 = mv(glued, basis(2, 0))[0].norm2()
    later = apply_system_to_sealed(h, sealed)
    recorded_p0 = system_zero_probability_sealed(later)
    check(coherent_p0 == Q2.make(1) and recorded_p0 == Q2.make(F(1, 2)),
          "action-derived intermediate record changes the interference observable")
    check(sealed_record_distribution(later) == sealed_record_distribution(sealed),
          "later local system action preserves the sealed record marginal")
    future_amp = kron(kron(h, eye(2)), eye(2))
    future = Mor("future-system-action", d14_seal.target, d14_seal.target, future_amp)
    check(preserves_record(future, 1, 1)
          and compose(future, d14_seal).source == q_obj,
          "actual D14 protected future composes and preserves the action-derived record")
    record_flip = kron(kron(eye(2), matrix(((0, 1), (1, 0)))), eye(2))
    try:
        Mor("forbidden-record-flip", d14_seal.target, d14_seal.target, record_flip)
        flip_rejected = False
    except ValueError:
        flip_rejected = True
    check(flip_rejected, "actual D14 constructor rejects a flip of the action-derived record")

    # The reversible memory action supplies a finite visible non-Markov cell.
    umem = mul(cnot_four(cnot, 1, 3), cnot_four(cnot, 0, 1))
    rho_in = scale(HALF, add(outer(basis(16, 0), basis(16, 0)),
                             outer(basis(16, 8), basis(16, 8))))
    rho_out = mul(umem, mul(rho_in, dagger(umem)))
    check(mul(dagger(umem), umem) == eye(16),
          "local CNOT action gives an exact reversible memory kernel")
    p_z1_given_x1_y0 = rho_out[13][13] / rho_out[13][13]
    p_z1_given_x0_y0 = rho_out[1][1] / (rho_out[0][0] + rho_out[1][1])
    check(rho_out[0][0] == HALF and rho_out[13][13] == HALF
          and p_z1_given_x1_y0 == ONE and p_z1_given_x0_y0 == ZERO,
          "action-built memory gives exact visible non-Markov conditionals one and zero")

    # The dictionary is a construction, not a selector: a local phase remains possible.
    phase = matrix(((1, 0), (0, C2(Q2(), Q2.make(1)))))
    alternative = mul(phase, h)
    base_closed_p = mv(mul(h, h), basis(2, 0))[0].norm2()
    alternative_closed_p = mv(mul(h, alternative), basis(2, 0))[0].norm2()
    check(mul(dagger(alternative), alternative) == eye(2)
          and base_closed_p == Q2.make(1)
          and alternative_closed_p == Q2.make(F(1, 2)),
          "fixed-frame closed experiment distinguishes the phase-modified local action")

    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final exact check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    semantic = {
        "schema": "d15-regulated-action-dictionary-exact-v1",
        "scope": "finite Z2/qubit regional action; nongravitational",
        "checks_passed": CHECKS,
        "dictionary": "local action weights -> kernels -> environment seal -> records",
        "verdict": "REGULATED-ACTION-DICTIONARY-WITNESS-PASSED",
        "ceiling": "does not select nature's action or establish generally covariant gravity",
    }
    semantic_bytes = json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    semantic_hash = sha256(semantic_bytes).hexdigest()
    if EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN" and semantic_hash != EXPECTED_SEMANTIC_SHA256:
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet.update({
        "semantic_sha256": semantic_hash,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "d13_dependency_sha256": d13_hash,
        "d14_dependency_sha256": d14_hash,
    })
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {packet['source_sha256']}")
    print("VERDICT: REGULATED-ACTION-DICTIONARY-WITNESS-PASSED")


if __name__ == "__main__":
    main()
