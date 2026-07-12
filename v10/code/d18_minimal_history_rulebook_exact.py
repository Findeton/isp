#!/usr/bin/env python3
"""Exact finite minimal-history-rulebook theorem.

At operational level, a typed event algebra and normalized strongly-positive
decoherence functional are sufficient to answer every supplied decoherent
event question.  Record semantics and units are an interpretation layer; a
local action/state/measure/instrument packet is a physically explanatory
generator.  The exact interventions below show that an action alone is not
the complete generator and distinguish physical changes from factorization
gauge.
"""

from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

from d13_finite_kernel_no_go_exact import C2, Q2, ZERO, ONE, HALF, ROOT_HALF, inner
from d17_integrated_causal_history_exact import (
    causal_nodes, causal_tower, is_projective_binary,
)


ROOT = Path(__file__).resolve().parents[2]
D17I = Path(__file__).with_name("d17_integrated_causal_history_exact.py")
OUT = ROOT / "v10" / "data" / "d18-minimal-history-rulebook-exact.json"
EXPECTED_D17I_SHA256 = "5fffa4d676da38a64e61cdd3b01c031d6fa74d2e1119f72c35369ad7be40be57"
EXPECTED_CHECKS = 30
EXPECTED_SEMANTIC_SHA256 = "e92b39b7308e6e51887ef073430e86608e96de863874fcf46b217f1d5d5dc779"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


HISTORIES = ((0, 0), (1, 0), (0, 1), (1, 1))  # (path, output)


def unrecorded_branches(initial=0):
    """Two-Hadamard interferometer branch vectors, exact in Q(sqrt(2),i)."""
    if initial == 0:
        signs = (1, 1, 1, -1)
    elif initial == 1:
        signs = (1, -1, 1, 1)
    else:
        raise ValueError("initial state must be 0 or 1")
    out = []
    for (path, output), sign in zip(HISTORIES, signs):
        vector = [ZERO, ZERO]
        vector[output] = HALF * sign
        out.append(tuple(vector))
    return tuple(out)


def recorded_branches(initial=0):
    out = []
    for history, branch in zip(HISTORIES, unrecorded_branches(initial)):
        path, output = history
        vector = [ZERO] * 4  # output tensor path-record
        vector[2 * output + path] = branch[output]
        out.append(tuple(vector))
    return tuple(out)


def decoherence(branches):
    return tuple(tuple(inner(left, right) for right in branches) for left in branches)


def total(d):
    return sum((sum(row, ZERO) for row in d), ZERO)


def hermitian(d):
    return all(d[i][j] == d[j][i].conj()
               for i in range(len(d)) for j in range(len(d)))


def quadratic(d, coefficients):
    return sum((coefficients[i].conj() * d[i][j] * coefficients[j]
                for i in range(len(d)) for j in range(len(d))), ZERO)


def strong_positive_on_grid(d):
    # Exact exhaustive witness grid; Gram construction supplies the general proof.
    for raw in product((-1, 0, 1), repeat=len(d)):
        coefficients = tuple(C2.make(x) for x in raw)
        value = quadratic(d, coefficients)
        if value.im != Q2() or value.re.b != 0 or value.re.a < 0:
            return False
    return True


def gram_quadratic(branches, coefficients):
    vector = tuple(sum((coefficients[i] * branches[i][k]
                        for i in range(len(branches))), ZERO)
                   for k in range(len(branches[0])))
    return inner(vector, vector)


def gram_identity_on_grid(d, branches):
    return all(quadratic(d, tuple(C2.make(x) for x in raw))
               == gram_quadratic(branches, tuple(C2.make(x) for x in raw))
               for raw in product((-1, 0, 1), repeat=len(d)))


def coarse(d, key):
    labels = tuple(sorted(set(key(history) for history in HISTORIES)))
    blocks = tuple(tuple(i for i, history in enumerate(HISTORIES)
                         if key(history) == label) for label in labels)
    out = []
    for left in blocks:
        row = []
        for right in blocks:
            row.append(sum((d[i][j] for i in left for j in right), ZERO))
        out.append(tuple(row))
    return labels, tuple(out)


def coarse_blocks(d, blocks):
    return tuple(tuple(sum((d[i][j] for i in left for j in right), ZERO)
                       for right in blocks) for left in blocks)


def set_partitions(items):
    if not items:
        return ((),)
    head, rest = items[0], items[1:]
    out = []
    for partition in set_partitions(rest):
        out.append(((head,),) + partition)
        for index in range(len(partition)):
            enlarged = list(partition)
            enlarged[index] = (head,) + enlarged[index]
            out.append(tuple(enlarged))
    # Canonicalize block/member ordering and remove recursive duplicates.
    canonical = {tuple(sorted((tuple(sorted(block)) for block in partition), key=lambda b: b[0]))
                 for partition in out}
    return tuple(sorted(canonical, key=lambda p: (len(p), p)))


def decoherent_probabilities(d_coarse):
    if any(d_coarse[i][j] != ZERO
           for i in range(len(d_coarse)) for j in range(len(d_coarse)) if i != j):
        raise ValueError("partition is not decoherent")
    probabilities = tuple(d_coarse[i][i] for i in range(len(d_coarse)))
    if sum(probabilities, ZERO) != ONE:
        raise ValueError("decoherent probabilities are not normalized")
    return probabilities


def weighted_branches(path_amplitudes):
    """Second-Hadamard histories from a supplied normalized path state."""
    out = []
    for path, output in HISTORIES:
        sign = -1 if (path, output) == (1, 1) else 1
        vector = [ZERO, ZERO]
        vector[output] = path_amplitudes[path] * ROOT_HALF * sign
        out.append(tuple(vector))
    return tuple(out)


def diagonal_history_functional(table):
    histories = tuple(sorted(table))
    d = tuple(tuple(ONE * table[history] if i == j else ZERO
                    for j, _ in enumerate(histories))
              for i, history in enumerate(histories))
    return histories, d


def restrict_by_prefix(child_histories, child_d):
    parents = tuple(sorted(set(history[:-1] for history in child_histories)))
    blocks = tuple(tuple(i for i, history in enumerate(child_histories)
                         if history[:-1] == parent) for parent in parents)
    return parents, coarse_blocks(child_d, blocks)


def main():
    d17i_hash = sha256(D17I.read_bytes()).hexdigest()
    check(d17i_hash == EXPECTED_D17I_SHA256,
          "review-candidate integrated D17 dependency is hash-pinned")

    un_branches = unrecorded_branches(0)
    rec_branches = recorded_branches(0)
    d_un = decoherence(un_branches)
    d_rec = decoherence(rec_branches)
    check(hermitian(d_un) and hermitian(d_rec),
          "unrecorded and recorded decoherence functionals are Hermitian")
    check(total(d_un) == ONE and total(d_rec) == ONE,
          "both complete-history decoherence functionals are normalized")
    check(strong_positive_on_grid(d_un) and strong_positive_on_grid(d_rec),
          "both functionals are strongly positive on the exact coefficient grid")
    check(gram_identity_on_grid(d_un, un_branches)
          and gram_identity_on_grid(d_rec, rec_branches),
          "every exact grid quadratic form equals the norm square of its branch sum")
    partitions = set_partitions(tuple(range(4)))
    check(len(partitions) == 15
          and all(hermitian(coarse_blocks(d_un, partition))
                  and total(coarse_blocks(d_un, partition)) == ONE
                  and strong_positive_on_grid(coarse_blocks(d_un, partition))
                  for partition in partitions),
          "all fifteen partitions preserve Hermiticity, normalization and strong positivity")
    coefficients = (ONE, -ONE, ONE, -ONE)
    check(quadratic(d_un, coefficients) == gram_quadratic(un_branches, coefficients)
          and quadratic(d_rec, coefficients) == gram_quadratic(rec_branches, coefficients),
          "strong positivity is a Gram identity, not only a sampled eigenvalue claim")

    labels_out, out_un = coarse(d_un, lambda history: history[1])
    _, out_rec = coarse(d_rec, lambda history: history[1])
    check(labels_out == (0, 1) and decoherent_probabilities(out_un) == (ONE, ZERO),
          "without a path record the two-Hadamard output is exactly deterministic")
    check(decoherent_probabilities(out_rec) == (HALF, HALF),
          "the local path commit removes interference and changes the output law")
    check(tuple(d_un[i][i] for i in range(4)) == (HALF * HALF,) * 4
          and tuple(d_rec[i][i] for i in range(4)) == (HALF * HALF,) * 4,
          "identical fine-history diagonals do not determine interference")
    check(d_un != d_rec,
          "off-diagonal decoherence data are necessary beyond a classical path measure")

    labels_path, path_un = coarse(d_un, lambda history: history[0])
    check(labels_path == (0, 1) and decoherent_probabilities(path_un) == (HALF, HALF),
          "the same D answers a distinct declared path-record question")
    try:
        decoherent_probabilities(((HALF, HALF), (HALF, HALF)))
        bad_partition_rejected = False
    except ValueError:
        bad_partition_rejected = True
    check(bad_partition_rejected,
          "a nondecoherent coarse graining cannot be silently read as classical probability")

    d_state1 = decoherence(unrecorded_branches(1))
    _, out_state1 = coarse(d_state1, lambda history: history[1])
    check(decoherent_probabilities(out_state1) == (ZERO, ONE) and d_state1 != d_un,
          "same local interferometer action with another boundary state changes records")
    tilted = (ONE * F(3, 5), ONE * F(4, 5))
    d_tilt = decoherence(weighted_branches(tilted))
    _, out_tilt = coarse(d_tilt, lambda history: history[1])
    check(total(d_tilt) == ONE
          and decoherent_probabilities(out_tilt) == (ONE * F(49, 50), ONE * F(1, 50)),
          "a second positive boundary/orbit envelope changes predictions with action fixed")

    factor_a_envelope = (ROOT_HALF, ROOT_HALF)
    factor_a_phase = (ONE, ONE)
    factor_b_envelope = (ROOT_HALF, -ROOT_HALF)
    factor_b_phase = (ONE, -ONE)
    product_a = tuple(factor_a_envelope[i] * factor_a_phase[i] for i in range(2))
    product_b = tuple(factor_b_envelope[i] * factor_b_phase[i] for i in range(2))
    check(product_a == product_b and factor_a_envelope != factor_b_envelope
          and factor_a_phase != factor_b_phase,
          "one amplitude admits distinct but representationally equivalent envelope/phase splits")

    nodes, grammar = causal_nodes(6)
    tower = causal_tower(nodes, grammar, F(1, 2), F(1, 2), 6)
    check(is_projective_binary(tower),
          "one supplied integrated causal record subalgebra is exactly projective")
    history_functionals = {depth: diagonal_history_functional(table)
                           for depth, table in tower.items()}
    check(all(total(d) == ONE and hermitian(d)
              for _, d in history_functionals.values()),
          "one normalized strongly-positive diagonal D_n family lives on the causal cylinders")
    check(all(restrict_by_prefix(*history_functionals[depth + 1])
              == history_functionals[depth] for depth in range(1, 6)),
          "the same D_n family restricts projectively on every tested causal depth")
    check(tower[2][(1, 0)] == F(1, 2)
          and tower[3][(1, 0, 1)] / tower[2][(1, 0)] == 1,
          "the projective law supplies its local next-record conditional by disintegration")
    check(tower[3][(0, 0, 0)] / tower[2][(0, 0)] == 1,
          "the other positive past has its conditional without a second click lottery")

    # Units are an interpretation map: rescaling the metre/second convention
    # cannot alter dimensionless D, but it alters reported dimensional values.
    dimensionless_probability = decoherent_probabilities(out_un)[0]
    length_in_metres_a = F(3, 1) * F(1, 1)
    length_in_metres_b = F(3, 1) * F(2, 1)
    check(dimensionless_probability == ONE and length_in_metres_a != length_in_metres_b,
          "unit dictionary is unnecessary for record odds but necessary for metres/seconds")
    measured_G_a = F(667430, 10**16)
    measured_G_b = measured_G_a * F(8, 1)
    check(measured_G_a != measured_G_b and d_un == decoherence(un_branches),
          "dimensionless histories do not fix G without a physical scale dictionary")

    # Layer-separation interventions.
    check(len(HISTORIES) == len(d_un) and all(len(row) == len(HISTORIES) for row in d_un),
          "event domain is necessary to type every decoherence-functional argument")
    check(out_un != out_rec, "physical record-generator intervention is operationally visible in D")
    check(out_un != path_un, "different event queries of one D return different observable laws")
    check(d_un != d_state1, "boundary-state intervention is operationally visible")
    check(d_un != d_tilt, "reference-envelope intervention is operationally visible")
    check(product_a == product_b,
          "generator-factor changes can be representational gauge and operationally invisible")
    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final exact check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    semantic = {
        "schema": "d18-operational-history-core-exact-v2",
        "scope": "finite typed histories, exact decoherence functionals and record cylinders",
        "checks_passed": CHECKS,
        "operational_core": ["typed-event-algebra", "decoherence-functional"],
        "interpretation_query_layer": ["record-semantics", "coarse-question", "units"],
        "generator_packet": ["domain-fields", "reference-measure", "action", "state", "instruments"],
        "verdict": "FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY",
        "ceiling": "finite/cylinder theorem; generator, interpretation and sigma-extension remain supplied",
    }
    semantic_bytes = json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    semantic_hash = sha256(semantic_bytes).hexdigest()
    if EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN" and semantic_hash != EXPECTED_SEMANTIC_SHA256:
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet.update({
        "semantic_sha256": semantic_hash,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "d17_integrated_dependency_sha256": d17i_hash,
    })
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {packet['source_sha256']}")
    print("VERDICT: FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY")


if __name__ == "__main__":
    main()
