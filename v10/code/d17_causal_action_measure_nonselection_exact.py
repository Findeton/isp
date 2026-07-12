#!/usr/bin/env python3
"""Exact fixed-causal-action -> measure/record nonselection witness.

One interval action is held fixed on two unlabeled causal orders.  Distinct
boundary/orbit packets give distinct normalized record laws.  A D14 seal
realizes orthogonal durable records.  A supplied projective non-Markov tower
is compatible with the action but is not derived from it.
"""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

from d13_finite_kernel_no_go_exact import (
    Q2, ZERO, ONE, HALF, ROOT_HALF, matrix, eye, dagger, mul, add, scale, mv,
    inner, outer, basis,
)
from d14_action_record_bridge_exact import Port, Obj, Mor, compose, preserves_record
from d14_action_record_bridge_exact import (
    integrated_memory_history_tables, cnot_permutation, reset_memory_kraus,
)
from d16_covariant_causal_action_exact import CausalOrder, IntervalAction, relation


ROOT = Path(__file__).resolve().parents[2]
D14 = Path(__file__).with_name("d14_action_record_bridge_exact.py")
D16 = Path(__file__).with_name("d16_covariant_causal_action_exact.py")
OUT = ROOT / "v10" / "data" / "d17-causal-action-measure-nonselection-exact.json"
EXPECTED_D14_SHA256 = "e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425"
EXPECTED_D16_SHA256 = "861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37"
EXPECTED_CHECKS = 26
EXPECTED_SEMANTIC_SHA256 = "a5d2cb4dd4b7b065430bcb4aedc7c88daddf1df1ad84c970f1ae3b78cd7ee525"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


def record_seal():
    system = Obj((Port("causal-alternative", 2, owner="history-cell"),))
    record = Obj((Port("order-record", 2, sealed=True,
                       owner="history-cell", record_id="order-R"),))
    collar = Obj((Port("collar", 2, owner="history-cell"),))
    target = system.tensor(record).tensor(collar)
    rows = [[0 for _ in range(2)] for _ in range(8)]
    for alternative in range(2):
        rows[(alternative * 2 + alternative) * 2 + 1][alternative] = 1
    return Mor("commit-causal-order-record", system, target, matrix(rows)), system, record, collar


def record_probabilities(state):
    probs = [Q2(), Q2()]
    for index, amp in enumerate(state):
        record = (index // 2) % 2
        probs[record] += amp.norm2()
    return tuple(probs)


def branch(state, record_value):
    return tuple(amp if ((index // 2) % 2) == record_value else ZERO
                 for index, amp in enumerate(state))


def amplitudes(boundary_envelope, orbit_sqrt, phases):
    return tuple(boundary_envelope[j] * orbit_sqrt[j] * phases[j] for j in range(2))


def coherent_erasure_probability(state):
    return (state[0] + state[1]).norm2() / Q2.make(2)


def recorded_erasure_probability(state):
    return sum((branch(state, r)[(r * 2 + r) * 2 + 1].norm2() / Q2.make(2)
                for r in range(2)), Q2())


def is_one_element_extension(parent, child):
    if child.n != parent.n + 1:
        return False
    return all(child.relation[i][j] == parent.relation[i][j]
               for i in range(parent.n) for j in range(parent.n))


def projective_tower(weight0, weight1, max_depth=6):
    tower = {
        1: {(0,): weight0, (1,): weight1},
        2: {(0, 0): weight0, (1, 0): weight1},
        3: {(0, 0, 0): weight0, (1, 0, 1): weight1},
    }
    for depth in range(4, max_depth + 1):
        tower[depth] = {history + (0,): probability
                        for history, probability in tower[depth - 1].items()}
    return tower


def is_projective(tower):
    depths = tuple(sorted(tower))
    if depths != tuple(range(depths[0], depths[-1] + 1)):
        return False
    for depth, table in tower.items():
        if any(len(history) != depth or probability < 0
               for history, probability in table.items()):
            return False
        if sum(table.values()) != 1:
            return False
    for depth in depths[:-1]:
        for parent, probability in tower[depth].items():
            child_mass = sum(value for child, value in tower[depth + 1].items()
                             if child[:-1] == parent)
            if child_mass != probability:
                return False
    return True


def main():
    d14_hash = sha256(D14.read_bytes()).hexdigest()
    d16_hash = sha256(D16.read_bytes()).hexdigest()
    check(d14_hash == EXPECTED_D14_SHA256, "reviewed D14 record bridge hash")
    check(d16_hash == EXPECTED_D16_SHA256, "reviewed D16 causal-action hash")

    chain4 = CausalOrder(relation(4, ((0, 1), (1, 2), (2, 3),
                                             (0, 2), (1, 3), (0, 3))))
    diamond = CausalOrder(relation(4, ((0, 1), (0, 2), (1, 3), (2, 3), (0, 3))))
    fixed_action = IntervalAction(0, (1, 0, 0, 0))
    phases = (fixed_action.phase(chain4), fixed_action.phase(diamond))
    check(phases == (-1, 1), "one fixed interval action gives opposite exact phases")

    equal_envelope = (ROOT_HALF, ROOT_HALF)
    unit_orbit = (ONE, ONE)
    equal_boundary_state = amplitudes(equal_envelope, unit_orbit, phases)
    check(equal_boundary_state == (-ROOT_HALF, ROOT_HALF),
          "boundary envelope, orbit factor and action phase are separated exactly")
    check(inner(equal_boundary_state, equal_boundary_state) == ONE,
          "supplied equal boundary state is normalized")
    check(equal_boundary_state[0] + equal_boundary_state[1] == ZERO,
          "unrecorded alternatives cancel coherently")
    check(coherent_erasure_probability(equal_boundary_state) == Q2(),
          "fixed erasure effect has zero unrecorded probability")

    seal, system, record, collar = record_seal()
    recorded = mv(seal.amp, equal_boundary_state)
    check(mul(dagger(seal.amp), seal.amp) == eye(2),
          "actual D14 causal-order record seal is isometric")
    check(record_probabilities(recorded) == (Q2.make(F(1, 2)), Q2.make(F(1, 2))),
          "orthogonal causal-order records have exact half-half Born weights")
    check(inner(branch(recorded, 0), branch(recorded, 1)) == ZERO,
          "record-extended causal alternatives exactly decohere")
    check(recorded_erasure_probability(recorded) == Q2.make(F(1, 2)),
          "local record changes the same erasure interference observable")
    check(all(recorded[(s * 2 + r) * 2] == ZERO for s in range(2) for r in range(2)),
          "every causal-order commit emits the live collar")

    future = Mor("future-readonly", seal.target, seal.target, eye(8))
    check(preserves_record(future, 1, 1) and compose(future, seal).source == system,
          "D14 protected future preserves and composes after the causal record")

    second_envelope = (ONE * F(3, 5), ONE * F(4, 5))
    second_boundary_state = amplitudes(second_envelope, unit_orbit, phases)
    second_recorded = mv(seal.amp, second_boundary_state)
    check(inner(second_boundary_state, second_boundary_state) == ONE
          and record_probabilities(second_recorded) == (Q2.make(F(9, 25)), Q2.make(F(16, 25))),
          "positive-support second boundary state changes probabilities with action fixed")
    check(phases == (fixed_action.phase(chain4), fixed_action.phase(diamond)),
          "the causal action and history domain remain frozen across boundary states")

    uniform_orbit = (F(1, 2), F(1, 2))
    inverse_aut_raw = (F(1, len(chain4.automorphisms())),
                       F(1, len(diamond.automorphisms())))
    inverse_aut_total = sum(inverse_aut_raw)
    inverse_aut = tuple(weight / inverse_aut_total for weight in inverse_aut_raw)
    check(uniform_orbit == (F(1, 2), F(1, 2))
          and inverse_aut == (F(2, 3), F(1, 3)),
          "two explicit orbit conventions give different normalized weights")
    orbit_raw_state = amplitudes((ONE, ONE), (ONE, ROOT_HALF), phases)
    orbit_recorded = mv(seal.amp, orbit_raw_state)
    orbit_raw_probs = record_probabilities(orbit_recorded)
    orbit_total = orbit_raw_probs[0] + orbit_raw_probs[1]
    check((orbit_raw_probs[0] / orbit_total, orbit_raw_probs[1] / orbit_total)
          == (Q2.make(F(2, 3)), Q2.make(F(1, 3))),
          "inverse-automorphism orbit factors propagate end-to-end through D14 records")

    root1 = CausalOrder(relation(1, ()))
    chain2 = CausalOrder(relation(2, ((0, 1),)))
    anti2 = CausalOrder(relation(2, ()))
    chain3 = CausalOrder(relation(3, ((0, 1), (1, 2), (0, 2))))
    vee3 = CausalOrder(relation(3, ((0, 2), (1, 2))))
    check(all((is_one_element_extension(root1, child) for child in (chain2, anti2)))
          and is_one_element_extension(chain2, chain3)
          and is_one_element_extension(anti2, vee3),
          "projective branches are realized by actual one-element causal-order extensions")

    tower_equal = projective_tower(F(1, 2), F(1, 2))
    tower_second = projective_tower(F(9, 25), F(16, 25))
    check(is_projective(tower_equal) and is_projective(tower_second),
          "two inequivalent positive-support depth-one-to-six towers are exactly projective")
    check(tower_equal[6] != tower_second[6],
          "fixed action supports distinct complete recorded history laws")

    p_z1_x1 = tower_equal[3][(1, 0, 1)] / tower_equal[2][(1, 0)]
    p_z1_x0 = F(0) / tower_equal[2][(0, 0)]
    check(p_z1_x1 == 1 and p_z1_x0 == 0,
          "supplied projective tower has exact visible non-Markov conditionals one and zero")

    local_memory = integrated_memory_history_tables(cnot_permutation(0, 1),
                                                     cnot_permutation(1, 3))
    check(local_memory[3][(0, 0, 0)] == Q2.make(F(1, 2))
          and local_memory[3][(1, 0, 1)] == Q2.make(F(1, 2)),
          "same causal branches are realized by a local carried-memory D14 packet")
    first_copy = cnot_permutation(0, 1)
    final_copy = cnot_permutation(1, 3)
    rho_in = scale(HALF, add(outer(basis(16, 0), basis(16, 0)),
                             outer(basis(16, 8), basis(16, 8))))
    rho_stored = mul(first_copy, mul(rho_in, dagger(first_copy)))
    reset = reset_memory_kraus()
    rho_reset = add(mul(reset[0], mul(rho_stored, dagger(reset[0]))),
                    mul(reset[1], mul(rho_stored, dagger(reset[1]))))
    rho_deleted = mul(final_copy, mul(rho_reset, dagger(final_copy)))
    check(rho_deleted[0][0] == HALF and rho_deleted[8][8] == HALF
          and all(rho_deleted[index][index] == ZERO
                  for index in range(16) if index not in (0, 8)),
          "deleting local boundary memory changes the visible process to z=0 on both branches")

    inconsistent = {
        1: {(0,): F(1, 2), (1,): F(1, 2)},
        2: {(0, 0): F(1), (1, 0): F(0)},
    }
    check(not is_projective(inconsistent),
          "independent per-level normalization can violate cylinder projectivity")

    check(record_probabilities(recorded) != record_probabilities(second_recorded)
          and tower_equal != tower_second,
          "one fixed causal action does not select boundary state or projective measure")
    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final exact check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    semantic = {
        "schema": "d17-causal-action-measure-nonselection-exact-v1",
        "scope": "two finite unlabeled causal alternatives; supplied D14 record/towers",
        "checks_passed": CHECKS,
        "fixed_action_phases": [-1, 1],
        "projective_depths": [1, 2, 3, 4, 5, 6],
        "verdict": "CAUSAL-ACTION-TO-MEASURE-NONSELECTION",
        "ceiling": "record instrument and projective towers supplied, not action-derived",
    }
    semantic_bytes = json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    semantic_hash = sha256(semantic_bytes).hexdigest()
    if EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN" and semantic_hash != EXPECTED_SEMANTIC_SHA256:
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet.update({
        "semantic_sha256": semantic_hash,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "d14_dependency_sha256": d14_hash,
        "d16_dependency_sha256": d16_hash,
    })
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {packet['source_sha256']}")
    print("VERDICT: CAUSAL-ACTION-TO-MEASURE-NONSELECTION")


if __name__ == "__main__":
    main()
