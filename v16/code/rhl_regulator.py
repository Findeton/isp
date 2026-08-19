#!/usr/bin/env python3
"""Result-neutral regulator and countercontrol family for RHL.

Every finite object in this file is explicitly a presentation receipt.  The
candidate ontology and law remain point-free and unsliced.  This file contains
no RHL verdict word and no claim that a finite presentation is fundamental.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Callable, Sequence

import rhl_core as core


Q = Fraction
QI = core.QI
Matrix = core.Matrix
Vector = core.Vector
ZERO = core.ZERO
ONE = core.ONE
I = core.I


def qpow(value: QI, power: int) -> QI:
    if power < 0:
        return qpow(ONE / value, -power)
    result = ONE
    factor = value
    exponent = power
    while exponent:
        if exponent & 1:
            result = result * factor
        factor = factor * factor
        exponent //= 2
    return result


def permutation_matrix(size: int, image: Callable[[int], int]) -> Matrix:
    rows = [[ZERO for _ in range(size)] for _ in range(size)]
    seen: set[int] = set()
    for source in range(size):
        target = image(source)
        if target < 0 or target >= size or target in seen:
            raise ValueError("image is not a permutation")
        seen.add(target)
        rows[target][source] = ONE
    return tuple(tuple(row) for row in rows)


def cnot(control: int, target: int, bits: int) -> Matrix:
    if control == target or not (0 <= control < bits and 0 <= target < bits):
        raise ValueError("invalid CNOT bits")

    def image(index: int) -> int:
        control_mask = 1 << (bits - 1 - control)
        target_mask = 1 << (bits - 1 - target)
        return index ^ target_mask if index & control_mask else index

    return permutation_matrix(1 << bits, image)


def support(value: Vector) -> list[int]:
    return [index for index, entry in enumerate(value) if entry != ZERO]


def density(value: Vector) -> Matrix:
    return tuple(tuple(left * right.conjugate() for right in value) for left in value)


def partial_trace_first_qubit(value: Matrix) -> Matrix:
    rows, columns = core.shape(value)
    if (rows, columns) != (4, 4):
        raise ValueError("registered partial trace expects two qubits")
    return tuple(
        tuple(value[bob_row][bob_column] + value[2 + bob_row][2 + bob_column] for bob_column in range(2))
        for bob_row in range(2)
    )


def conjugate_channel(unitary: Matrix, value: Matrix) -> Matrix:
    return core.mmul(unitary, core.mmul(value, core.adjoint(unitary)))


def local_dephase_first(value: Matrix) -> Matrix:
    p0 = core.matrix(((ONE, ZERO), (ZERO, ZERO)))
    p1 = core.matrix(((ZERO, ZERO), (ZERO, ONE)))
    identity2 = core.identity(2)
    k0 = core.kron(p0, identity2)
    k1 = core.kron(p1, identity2)
    return core.madd(conjugate_channel(k0, value), conjugate_channel(k1, value))


def trace(value: Matrix) -> QI:
    rows, columns = core.shape(value)
    if rows != columns:
        raise ValueError("trace requires square matrix")
    return sum((value[index][index] for index in range(rows)), ZERO)


def probability(state: Matrix, effect: Matrix) -> QI:
    return trace(core.mmul(effect, state))


def build_regulator_data() -> dict[str, object]:
    # Two nonisomorphic finite presentations of one two-dimensional boundary
    # interface.  Their cardinalities are descriptive coordinates only.
    left_embedding = core.matrix(
        (
            (Q(3, 5), Q(0)),
            (Q(4, 5), Q(0)),
            (Q(0), Q(1)),
        )
    )
    right_embedding = core.matrix(
        (
            (Q(1, 3), Q(0)),
            (Q(2, 3), Q(0)),
            (Q(2, 3), Q(0)),
            (Q(0), Q(1)),
        )
    )
    common_transport = core.matrix(((Q(3, 5), Q(4, 5)), (-Q(4, 5), Q(3, 5))))
    left_continuation = core.mmul(common_transport, core.adjoint(left_embedding))
    right_continuation = core.mmul(common_transport, core.adjoint(right_embedding))
    left_composite = core.mmul(left_continuation, left_embedding)
    right_composite = core.mmul(right_continuation, right_embedding)

    tampered_right = core.matrix(
        (
            (Q(1, 6), Q(0)),
            (Q(1, 3), Q(0)),
            (Q(1, 3), Q(0)),
            (Q(0), Q(1)),
        )
    )
    tampered_composite = core.mmul(right_continuation, tampered_right)

    # The committed interference anchor as a presentation-independent history
    # functional: the two entries are route amplitudes, not sampled routes.
    route_amplitudes = (QI(Q(9, 25)), QI(-Q(16, 25)))
    history_functional = core.gram(tuple((amplitude,) for amplitude in route_amplitudes))
    coherent_weight = core.coarse_grain(history_functional, ((0, 1),))[0][0]
    diagonal_weight = sum((history_functional[index][index] for index in (0, 1)), ZERO)
    route_defect = core.interference_defect(history_functional, (0, 1))

    # A writer that is its own eraser, and a redundant second flag that retains
    # the fact after the first copy is erased.
    seed_two = core.vector((Q(3, 5), Q(0), Q(4, 5), Q(0)))  # |s,0>
    writer_two = cnot(0, 1, 2)
    written_two = core.mv(writer_two, seed_two)
    erased_two = core.mv(writer_two, written_two)

    seed_three = core.vector((Q(3, 5), Q(0), Q(0), Q(0), Q(4, 5), Q(0), Q(0), Q(0)))
    write_first = cnot(0, 1, 3)
    write_second = cnot(0, 2, 3)
    copied = core.mv(write_second, core.mv(write_first, seed_three))
    first_erased = core.mv(write_first, copied)

    # Two structural-law counterfamilies.  The character family is
    # multiplicative under regional gluing; the blind family is k=0.  The
    # relational integer is deliberately not called geometry here.
    character_checks = []
    for charge in (0, 1, 2, 3):
        for left in range(-3, 4):
            for right in range(-3, 4):
                lhs = qpow(I, charge * (left + right))
                rhs = qpow(I, charge * left) * qpow(I, charge * right)
                character_checks.append(lhs == rhs)
    base_amplitudes = (QI(Q(1, 2)), QI(Q(1, 2)))
    relational_values = (0, 1)
    family_weights: dict[str, str] = {}
    for charge in (0, 1, 2, 3):
        total = sum(
            (
                amplitude * qpow(I, charge * relational_value)
                for amplitude, relational_value in zip(base_amplitudes, relational_values, strict=True)
            ),
            ZERO,
        )
        family_weights[str(charge)] = core.qtext(total.norm2() if isinstance(total.norm2(), QI) else QI(total.norm2()))

    # Fixed-factor locality control.  This is not the changing-subsystem
    # theorem: that separate missing referent is exposed below.
    # Normalize without square roots by using the corresponding rational mixed
    # Bell-correlated state with trace one.
    bell_like = core.matrix(
        (
            (Q(1, 2), Q(0), Q(0), Q(1, 2)),
            (Q(0), Q(0), Q(0), Q(0)),
            (Q(0), Q(0), Q(0), Q(0)),
            (Q(1, 2), Q(0), Q(0), Q(1, 2)),
        )
    )
    bob_before = partial_trace_first_qubit(bell_like)
    bob_after = partial_trace_first_qubit(local_dephase_first(bell_like))

    # Without a law-selected transport of Bob's boundary algebra, two
    # candidate identifications move the calibrated probability.
    bob_state = core.matrix(((Q(3, 4), Q(0)), (Q(0), Q(1, 4))))
    effect_zero = core.matrix(((ONE, ZERO), (ZERO, ZERO)))
    swap = core.matrix(((ZERO, ONE), (ONE, ZERO)))
    effect_swapped = conjugate_channel(swap, effect_zero)
    identity_reading = probability(bob_state, effect_zero)
    swapped_reading = probability(bob_state, effect_swapped)

    return {
        "schema": "rhl-regulator-family-v1",
        "scope": {
            "role": "finite regulator receipts and countercontrols only",
            "ontology": "no presentation cell, basis vector, or sequence index is ontic",
            "claim_scope": "general claims require analytical proofs over arbitrary directed refinements",
        },
        "presentations": {
            "left": {
                "description": "two-way split plus retained boundary channel",
                "embedding": core.mtext(left_embedding),
                "continuation": core.mtext(left_continuation),
                "composite": core.mtext(left_composite),
            },
            "right": {
                "description": "three-way split plus retained boundary channel",
                "embedding": core.mtext(right_embedding),
                "continuation": core.mtext(right_continuation),
                "composite": core.mtext(right_composite),
            },
            "common_boundary_transport": core.mtext(common_transport),
            "tampered_right_embedding": core.mtext(tampered_right),
            "tampered_right_composite": core.mtext(tampered_composite),
        },
        "history": {
            "route_amplitudes": [core.qtext(value) for value in route_amplitudes],
            "functional": core.mtext(history_functional),
            "coherent_weight": core.qtext(coherent_weight),
            "diagonal_weight": core.qtext(diagonal_weight),
            "interference_defect": core.qtext(route_defect),
        },
        "records": {
            "single_flag": {
                "seed_support": support(seed_two),
                "written_support": support(written_two),
                "erased_support": support(erased_two),
                "returns_to_seed": erased_two == seed_two,
            },
            "redundant_flag": {
                "seed_support": support(seed_three),
                "copied_support": support(copied),
                "first_copy_erased_support": support(first_erased),
            },
        },
        "structural_counterfamilies": {
            "character_gluing_checks": len(character_checks),
            "character_gluing_all_pass": all(character_checks),
            "two_filling_weights_by_charge": family_weights,
            "interpretation_guard": "charge character is permitted law data, not earned geometry",
        },
        "locality": {
            "fixed_factor": {
                "bob_before": core.mtext(bob_before),
                "bob_after_alice_dephase": core.mtext(bob_after),
            },
            "changing_boundary_identification": {
                "identity_calibration_probability": core.qtext(identity_reading),
                "swapped_calibration_probability": core.qtext(swapped_reading),
                "law_selected_transport_supplied": False,
            },
        },
    }


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def build_receipt(data: dict[str, object]) -> tuple[str, dict[str, object]]:
    presentations = data["presentations"]
    history = data["history"]
    records = data["records"]
    families = data["structural_counterfamilies"]
    locality = data["locality"]

    checks = [
        {
            "check": "REG-TWO-NONISOMORPHIC-PRESENTATIONS",
            "predicate": len(presentations["left"]["embedding"]) != len(presentations["right"]["embedding"]),
            "evidence": f"row_counts={len(presentations['left']['embedding'])},{len(presentations['right']['embedding'])}",
        },
        {
            "check": "REG-COMMON-BOUNDARY-COMPOSITE",
            "predicate": presentations["left"]["composite"] == presentations["right"]["composite"] == presentations["common_boundary_transport"],
            "evidence": f"composite={presentations['common_boundary_transport']}",
        },
        {
            "check": "REG-TAMPER-MOVES-BOUNDARY",
            "predicate": presentations["tampered_right_composite"] != presentations["common_boundary_transport"],
            "evidence": f"tampered={presentations['tampered_right_composite']}",
        },
        {
            "check": "REG-INTERFERENCE-VS-DIAGONAL",
            "predicate": history["coherent_weight"] != history["diagonal_weight"],
            "evidence": f"coherent={history['coherent_weight']} diagonal={history['diagonal_weight']}",
        },
        {
            "check": "REG-SINGLE-FLAG-ERASABLE",
            "predicate": records["single_flag"]["returns_to_seed"],
            "evidence": f"written={records['single_flag']['written_support']} erased={records['single_flag']['erased_support']}",
        },
        {
            "check": "REG-REDUNDANT-FLAG-RETAINS-CORRELATION",
            "predicate": records["redundant_flag"]["first_copy_erased_support"] == [0, 5],
            "evidence": f"support={records['redundant_flag']['first_copy_erased_support']}",
        },
        {
            "check": "REG-CHARACTER-FAMILY-GLUES",
            "predicate": families["character_gluing_all_pass"],
            "evidence": f"checks={families['character_gluing_checks']}",
        },
        {
            "check": "REG-STRUCTURAL-SURFACE-ALLOWS-MOVING-WEIGHTS",
            "predicate": len(set(families["two_filling_weights_by_charge"].values())) > 1,
            "evidence": f"weights={families['two_filling_weights_by_charge']}",
        },
        {
            "check": "REG-FIXED-FACTOR-LOCALITY-CONTROL",
            "predicate": locality["fixed_factor"]["bob_before"] == locality["fixed_factor"]["bob_after_alice_dephase"],
            "evidence": f"bob={locality['fixed_factor']['bob_before']}",
        },
        {
            "check": "REG-CHANGING-BOUNDARY-IDENTIFICATION-MATTERS",
            "predicate": locality["changing_boundary_identification"]["identity_calibration_probability"] != locality["changing_boundary_identification"]["swapped_calibration_probability"],
            "evidence": f"probabilities={locality['changing_boundary_identification']['identity_calibration_probability']},{locality['changing_boundary_identification']['swapped_calibration_probability']}",
        },
    ]
    if not all(item["predicate"] for item in checks):
        failures = [item["check"] for item in checks if not item["predicate"]]
        raise AssertionError(f"regulator control failed: {failures}")

    transcript_lines = [
        "RHL REGULATOR FAMILY — RESULT NEUTRAL",
        "scope: finite presentation receipts only; no point/tick ontology and no RHL verdict",
    ]
    for item in checks:
        transcript_lines.append(f"PASS {item['check']} :: {item['evidence']}")
    transcript_lines.append(f"SUMMARY {len(checks)}/{len(checks)} structural controls")
    transcript_lines.append(f"DATA-SHA256 {digest(data)}")
    transcript = "\n".join(transcript_lines) + "\n"

    receipt = {
        "schema": "rhl-regulator-receipt-v1",
        "scope": data["scope"],
        "checks": checks,
        "data": data,
        "data_sha256": digest(data),
        "transcript_sha256": hashlib.sha256(transcript.encode("utf-8")).hexdigest(),
    }
    receipt["seals"] = {
        "scope": digest(receipt["scope"]),
        "checks": digest(receipt["checks"]),
        "data": digest(receipt["data"]),
    }
    return transcript, receipt


def write_new(path: Path, text: str) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    path.write_text(text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = build_regulator_data()
    transcript, receipt = build_receipt(data)
    if args.selftest:
        mutated = json.loads(canonical_json(data))
        mutated["history"]["functional"][0][1] = "0"
        mutated["history"]["functional"][1][0] = "0"
        mutated["history"]["coherent_weight"] = mutated["history"]["diagonal_weight"]
        try:
            build_receipt(mutated)
        except AssertionError:
            print("SELFTEST PASS: removing the cross term kills the interference control")
            return 0
        raise AssertionError("selftest mutation escaped")

    write_new(args.output, transcript)
    write_new(args.receipt, canonical_json(receipt) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
