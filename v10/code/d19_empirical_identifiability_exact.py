#!/usr/bin/env python3
"""Exact finite empirical non-identifiability theorem for complete histories."""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "v10" / "data" / "d19-empirical-identifiability-exact.json"
EXPECTED_CHECKS = 20
EXPECTED_SEMANTIC_SHA256 = "d188a40340eca1148a8c957d8139e411748aacc355531a87f20ef6fbd9866856"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


OMEGA = tuple(product((-1, 1), repeat=3))
CHARACTERS = (
    lambda x, y, z: 1,
    lambda x, y, z: x,
    lambda x, y, z: y,
    lambda x, y, z: z,
    lambda x, y, z: x * y,
    lambda x, y, z: x * z,
    lambda x, y, z: y * z,
)


def observation_matrix():
    return tuple(tuple(F(character(*omega)) for omega in OMEGA)
                 for character in CHARACTERS)


def matvec(matrix, vector):
    return tuple(sum((row[j] * vector[j] for j in range(len(vector))), F(0))
                 for row in matrix)


def rank(matrix):
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    pivot_row = 0
    for col in range(n):
        pivot = next((row for row in range(pivot_row, m) if rows[row][col] != 0), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][col]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for row in range(m):
            if row == pivot_row or rows[row][col] == 0:
                continue
            factor = rows[row][col]
            rows[row] = [rows[row][j] - factor * rows[pivot_row][j] for j in range(n)]
        pivot_row += 1
        if pivot_row == m:
            break
    return pivot_row


def law(r):
    r = F(r)
    return tuple((F(1) + r * x * y * z) / 8 for x, y, z in OMEGA)


def triple_direction():
    return tuple(F(x * y * z, 8) for x, y, z in OMEGA)


def marginal(probabilities, indices):
    out = {}
    for omega, probability in zip(OMEGA, probabilities):
        key = tuple(omega[index] for index in indices)
        out[key] = out.get(key, F(0)) + probability
    return out


def expectation(probabilities, function):
    return sum((probability * function(*omega)
                for omega, probability in zip(OMEGA, probabilities)), F(0))


def conditional_z_one(probabilities, x, y):
    table = dict(zip(OMEGA, probabilities))
    return table[(x, y, 1)] / (table[(x, y, -1)] + table[(x, y, 1)])


def main():
    observations = observation_matrix()
    direction = triple_direction()
    check(len(OMEGA) == 8 and len(observations) == 7,
          "frozen carrier has eight histories and seven training characters")
    check(rank(observations) == 7,
          "training observation map has exact rank seven")
    check(matvec(observations, direction) == (F(0),) * 7,
          "triple-correlation direction is exactly invisible to all training data")
    check(any(value != 0 for value in direction),
          "the invisible direction is nonzero")

    half = law(F(1, 2))
    third = law(F(1, 3))
    check(sum(half, F(0)) == 1 and min(half) > 0,
          "first whole-history law is strictly positive and normalized")
    check(sum(third, F(0)) == 1 and min(third) > 0,
          "second whole-history law is strictly positive and normalized")
    check(half != third, "the two complete history laws are inequivalent")
    check(matvec(observations, half) == matvec(observations, third),
          "all frozen normalization, one-record and two-record training moments agree")
    check(matvec(observations, half) == (F(1), F(0), F(0), F(0), F(0), F(0), F(0)),
          "shared training vector is exact")
    check(all(marginal(half, pair) == marginal(third, pair)
              for pair in ((0, 1), (0, 2), (1, 2))),
          "every complete one/two-record marginal agrees")
    check(all(set(marginal(half, pair).values()) == {F(1, 4)}
              for pair in ((0, 1), (0, 2), (1, 2))),
          "all shared pair marginals are uniform")

    check(expectation(half, lambda x, y, z: x * y * z) == F(1, 2)
          and expectation(third, lambda x, y, z: x * y * z) == F(1, 3),
          "designed triple-correlation discriminator separates the survivors")
    check(conditional_z_one(half, 1, 1) == F(3, 4)
          and conditional_z_one(third, 1, 1) == F(2, 3),
          "equivalent future conditional exposes the same invisible coordinate")
    check(conditional_z_one(half, 1, 1) != conditional_z_one(half, -1, 1),
          "first survivor is visibly non-Markov in the current record")
    check(conditional_z_one(third, 1, 1) != conditional_z_one(third, -1, 1),
          "second survivor is visibly non-Markov in the current record")

    for r in (F(-9, 10), F(0), F(9, 10)):
        probabilities = law(r)
        check(sum(probabilities, F(0)) == 1 and min(probabilities) > 0,
              f"positive invisible perturbation survives at r={r}")

    check(tuple(half[i] - third[i] for i in range(8))
          == tuple(F(1, 6) * value for value in direction),
          "survivor difference lies exactly in the empirical null direction")
    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final exact check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    semantic = {
        "schema": "d19-empirical-identifiability-exact-v1",
        "scope": "eight classical complete histories; one/two-record training evidence",
        "checks_passed": CHECKS,
        "training_rank": 7,
        "carrier_dimension": 8,
        "verdict": "FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY",
        "ceiling": "finite exact identifiability counterexample, not a census of physical UV theories",
    }
    semantic_bytes = json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    semantic_hash = sha256(semantic_bytes).hexdigest()
    if EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN" and semantic_hash != EXPECTED_SEMANTIC_SHA256:
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet.update({
        "semantic_sha256": semantic_hash,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    })
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {packet['source_sha256']}")
    print("VERDICT: FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY")


if __name__ == "__main__":
    main()
