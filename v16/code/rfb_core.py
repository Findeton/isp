#!/usr/bin/env python3
"""Generic exact core for RFB Paper 10.

This module is frozen before the RFB physical fixture and scorer.  It contains
only public finite algebra for cyclic writers, additive readers, history
interference, predictive partitions, and fixed-factor quantum channels.  It
contains no RFB verdict, expected fixture value, ISP graph, or law selection.

All numerical work is over ``fractions.Fraction``.  Roots of unity that occur
in cyclic writer/reader classifications are represented by integer exponents;
no floating-point approximation enters the public surface.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import tempfile
from collections import defaultdict, deque
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


Q = Fraction
Matrix = tuple[tuple[Q, ...], ...]


class GateFail(RuntimeError):
    """Raised before artifact promotion when a public calibration fails."""


def qtext(value: Q) -> str:
    item = Q(value)
    return str(item.numerator) if item.denominator == 1 else f"{item.numerator}/{item.denominator}"


def matrix(rows: Sequence[Sequence[Any]]) -> Matrix:
    result = tuple(tuple(Q(entry) for entry in row) for row in rows)
    if not result or not result[0]:
        raise ValueError("matrix must be nonempty")
    if len({len(row) for row in result}) != 1:
        raise ValueError("ragged matrix")
    return result


def shape(value: Matrix) -> tuple[int, int]:
    return len(value), len(value[0])


def zero(rows: int, columns: int) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(columns)) for _ in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Q(1) if row == column else Q(0) for column in range(size))
        for row in range(size)
    )


def matadd(left: Matrix, right: Matrix) -> Matrix:
    if shape(left) != shape(right):
        raise ValueError("matrix addition shape mismatch")
    rows, columns = shape(left)
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(columns))
        for row in range(rows)
    )


def matscale(coefficient: Any, value: Matrix) -> Matrix:
    scalar = Q(coefficient)
    return tuple(tuple(scalar * entry for entry in row) for row in value)


def matmul(left: Matrix, right: Matrix) -> Matrix:
    left_rows, inner = shape(left)
    right_rows, right_columns = shape(right)
    if inner != right_rows:
        raise ValueError("matrix multiplication shape mismatch")
    return tuple(
        tuple(
            sum((left[row][index] * right[index][column] for index in range(inner)), Q(0))
            for column in range(right_columns)
        )
        for row in range(left_rows)
    )


def transpose(value: Matrix) -> Matrix:
    rows, columns = shape(value)
    return tuple(tuple(value[row][column] for row in range(rows)) for column in range(columns))


def tensor(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    return tuple(
        tuple(
            left[row // right_rows][column // right_columns]
            * right[row % right_rows][column % right_columns]
            for column in range(left_columns * right_columns)
        )
        for row in range(left_rows * right_rows)
    )


def trace(value: Matrix) -> Q:
    rows, columns = shape(value)
    if rows != columns:
        raise ValueError("trace requires a square matrix")
    return sum((value[index][index] for index in range(rows)), Q(0))


def conjugate_by(operator: Matrix, state: Matrix) -> Matrix:
    return matmul(matmul(operator, state), transpose(operator))


def apply_channel(kraus: Sequence[Matrix], state: Matrix) -> Matrix:
    if not kraus:
        raise ValueError("channel needs at least one Kraus operator")
    result = zero(shape(kraus[0])[0], shape(kraus[0])[0])
    for operator in kraus:
        result = matadd(result, conjugate_by(operator, state))
    return result


def partial_trace_a(value: Matrix, dim_a: int, dim_b: int) -> Matrix:
    if shape(value) != (dim_a * dim_b, dim_a * dim_b):
        raise ValueError("partial-trace shape mismatch")
    return tuple(
        tuple(
            sum(
                (
                    value[a * dim_b + row][a * dim_b + column]
                    for a in range(dim_a)
                ),
                Q(0),
            )
            for column in range(dim_b)
        )
        for row in range(dim_b)
    )


def determinant_2(value: Matrix) -> Q:
    if shape(value) != (2, 2):
        raise ValueError("two-dimensional determinant required")
    return value[0][0] * value[1][1] - value[0][1] * value[1][0]


def psd_2(value: Matrix) -> bool:
    return (
        shape(value) == (2, 2)
        and value == transpose(value)
        and value[0][0] >= 0
        and value[1][1] >= 0
        and determinant_2(value) >= 0
    )


def permutation_cycles(images: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    size = len(images)
    if sorted(images) != list(range(size)):
        raise ValueError("images do not form a permutation")
    unseen = set(range(size))
    cycles: list[tuple[int, ...]] = []
    while unseen:
        start = min(unseen)
        orbit: list[int] = []
        item = start
        while item not in orbit:
            orbit.append(item)
            unseen.remove(item)
            item = images[item]
        cycles.append(tuple(orbit))
    return tuple(cycles)


def full_cycle_writers(order: int) -> tuple[tuple[int, ...], ...]:
    if order < 2:
        raise ValueError("record order must be at least two")
    return tuple(
        candidate
        for candidate in permutations(range(order))
        if len(permutation_cycles(candidate)) == 1
    )


def cycle_relabeling_to_shift(images: Sequence[int]) -> tuple[int, ...]:
    cycles = permutation_cycles(images)
    if len(cycles) != 1:
        raise ValueError("writer is not a full cycle")
    cycle = cycles[0]
    return tuple(cycle.index(label) for label in range(len(cycle)))


def relabeled_images(images: Sequence[int], relabeling: Sequence[int]) -> tuple[int, ...]:
    if sorted(relabeling) != list(range(len(images))):
        raise ValueError("invalid relabeling")
    inverse = [0] * len(images)
    for old, new in enumerate(relabeling):
        inverse[new] = old
    return tuple(relabeling[images[inverse[new]]] for new in range(len(images)))


def shift_images(order: int, step: int = 1) -> tuple[int, ...]:
    return tuple((index + step) % order for index in range(order))


def phase_gauge_transform(
    images: Sequence[int], edge_phases: Sequence[int], vertex_phases: Sequence[int], order: int
) -> tuple[int, ...]:
    if len(images) != len(edge_phases) or len(images) != len(vertex_phases):
        raise ValueError("phase-decoration shape mismatch")
    return tuple(
        (edge_phases[index] + vertex_phases[index] - vertex_phases[images[index]]) % order
        for index in range(len(images))
    )


def winding_phase(edge_phases: Sequence[int], order: int) -> int:
    return sum(edge_phases) % order


def phase_gauge_orbits(order: int, images: Sequence[int]) -> tuple[tuple[tuple[int, ...], ...], ...]:
    decorations = set(product(range(order), repeat=order))
    gauges = tuple((0,) + tail for tail in product(range(order), repeat=order - 1))
    orbits: list[tuple[tuple[int, ...], ...]] = []
    while decorations:
        seed = min(decorations)
        orbit = {
            phase_gauge_transform(images, seed, gauge, order)
            for gauge in gauges
        }
        decorations.difference_update(orbit)
        orbits.append(tuple(sorted(orbit)))
    return tuple(orbits)


def root_real(order: int, exponent: int) -> Q:
    index = exponent % order
    tables = {
        2: (Q(1), Q(-1)),
        3: (Q(1), Q(-1, 2), Q(-1, 2)),
        4: (Q(1), Q(0), Q(-1), Q(0)),
    }
    if order not in tables:
        raise ValueError("exact real-part table is registered only at orders two, three, and four")
    return tables[order][index]


def winding_interference_probability(order: int, theta: int) -> Q:
    return (Q(1) + root_real(order, theta)) / 2


def reader_functions(order: int) -> tuple[tuple[int, ...], ...]:
    return tuple((0,) + tail for tail in product(range(order), repeat=order - 1))


def reader_is_additive(values: Sequence[int], order: int) -> bool:
    return all(
        values[(left + right) % order] % order
        == (values[left] + values[right]) % order
        for left in range(order)
        for right in range(order)
    )


def reader_charge(values: Sequence[int], order: int) -> int | None:
    if not reader_is_additive(values, order):
        return None
    charge = values[1] % order
    return charge if all(values[index] % order == charge * index % order for index in range(order)) else None


def units(order: int) -> tuple[int, ...]:
    return tuple(value for value in range(1, order) if math.gcd(value, order) == 1)


def writer_reader_pair_orbits(order: int) -> tuple[tuple[tuple[int, int], ...], ...]:
    points = {(step, charge) for step in units(order) for charge in range(order)}
    result: list[tuple[tuple[int, int], ...]] = []
    while points:
        seed = min(points)
        orbit = {
            ((multiplier * seed[0]) % order, (pow(multiplier, -1, order) * seed[1]) % order)
            for multiplier in units(order)
        }
        points.difference_update(orbit)
        result.append(tuple(sorted(orbit)))
    return tuple(result)


def pair_invariant(step: int, charge: int, order: int) -> int:
    return step * charge % order


def two_history_ports(relative_sign: int) -> dict[str, Any]:
    if relative_sign not in (-1, 1):
        raise ValueError("relative sign must be plus or minus one")
    plus = (Q(1, 2), Q(relative_sign, 2))
    minus = (Q(1, 2), Q(-relative_sign, 2))
    plus_d = matrix([[plus[0] * plus[0], plus[0] * plus[1]], [plus[1] * plus[0], plus[1] * plus[1]]])
    minus_d = matrix([[minus[0] * minus[0], minus[0] * minus[1]], [minus[1] * minus[0], minus[1] * minus[1]]])
    coherent = {
        "plus": sum(plus, Q(0)) ** 2,
        "minus": sum(minus, Q(0)) ** 2,
    }
    exclusive = {
        "plus": plus_d[0][0] + plus_d[1][1],
        "minus": minus_d[0][0] + minus_d[1][1],
    }
    return {
        "functionals": {"plus": plus_d, "minus": minus_d},
        "coherent": coherent,
        "exclusive": exclusive,
        "sum_functional": matadd(plus_d, minus_d),
    }


def hybrid_tag(overlap: Q, complement: Q) -> dict[str, Any]:
    overlap = Q(overlap)
    complement = Q(complement)
    if overlap * overlap + complement * complement != 1:
        raise ValueError("tag coordinates are not normalized")
    gram = matrix([[1, overlap], [overlap, 1]])
    return {
        "overlap": overlap,
        "complement": complement,
        "gram": gram,
        "plus_probability": (Q(1) + overlap) / 2,
        "minus_probability": (Q(1) - overlap) / 2,
    }


def partition_from_key(items: Iterable[Any], key: Callable[[Any], Any]) -> tuple[tuple[Any, ...], ...]:
    blocks: dict[Any, list[Any]] = defaultdict(list)
    for item in items:
        blocks[key(item)].append(item)
    return tuple(tuple(blocks[label]) for label in sorted(blocks, key=repr))


def summary_sufficient(items: Sequence[Any], summary: Callable[[Any], Any], future: Callable[[Any], Any]) -> bool:
    return all(len({future(item) for item in block}) == 1 for block in partition_from_key(items, summary))


def predictive_refinement(
    states: Sequence[Any], observations: Callable[[Any], Any], transitions: Callable[[Any], Sequence[Any]]
) -> tuple[tuple[Any, ...], ...]:
    """Finite bisimulation-style predictive partition."""

    labels = {state: observations(state) for state in states}
    while True:
        signatures = {
            state: (labels[state], tuple(sorted((labels[target] for target in transitions(state)), key=repr)))
            for state in states
        }
        ordered = {signature: index for index, signature in enumerate(sorted(set(signatures.values()), key=repr))}
        refined = {state: ordered[signatures[state]] for state in states}
        if all(refined[state] == labels[state] for state in states) and all(isinstance(labels[state], int) for state in states):
            break
        normalized_old = partition_from_key(states, lambda state: labels[state])
        normalized_new = partition_from_key(states, lambda state: refined[state])
        labels = refined
        if normalized_old == normalized_new:
            break
    return partition_from_key(states, lambda state: labels[state])


def contains_float(value: Any) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, Mapping):
        return any(contains_float(key) or contains_float(item) for key, item in value.items())
    if isinstance(value, (tuple, list, set)):
        return any(contains_float(item) for item in value)
    return False


def serialize(value: Any) -> Any:
    if isinstance(value, Fraction):
        return qtext(value)
    if isinstance(value, Mapping):
        return {str(key): serialize(item) for key, item in sorted(value.items(), key=lambda row: str(row[0]))}
    if isinstance(value, (tuple, list)):
        return [serialize(item) for item in value]
    if isinstance(value, set):
        return [serialize(item) for item in sorted(value, key=repr)]
    return value


def canonical_json(value: Any) -> bytes:
    return (json.dumps(serialize(value), sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def gate(rows: list[dict[str, Any]], name: str, statement: str, ok: bool, evidence: Mapping[str, Any]) -> None:
    row = {
        "gate": name,
        "statement": statement,
        "passed": bool(ok),
        "evidence": serialize(dict(evidence)),
    }
    rows.append(row)
    if not ok:
        raise GateFail(f"{name}: {json.dumps(row['evidence'], sort_keys=True)}")


PUBLIC_MUTANTS = (
    "cycle-classifier",
    "phase-gauge",
    "reader-composition",
    "pair-orbit",
    "history-interference",
    "history-positivity",
    "hybrid-normalization",
    "predictive-partition",
    "locality",
    "exactness",
    "payload-seal",
)


PUBLIC_GATE_NAMES = (
    "RFB-PUBLIC-CYCLE",
    "RFB-PUBLIC-PHASE-GAUGE",
    "RFB-PUBLIC-READER",
    "RFB-PUBLIC-PAIR-ORBIT",
    "RFB-PUBLIC-HISTORY",
    "RFB-PUBLIC-HYBRID",
    "RFB-PUBLIC-PREDICTIVE",
    "RFB-PUBLIC-LOCALITY",
    "RFB-PUBLIC-EXACTNESS",
)


def public_calibration(mutant: str | None = None) -> dict[str, Any]:
    if mutant is not None and mutant not in PUBLIC_MUTANTS:
        raise ValueError(f"unknown public mutant {mutant!r}")
    gates: list[dict[str, Any]] = []

    order = 5
    writers = full_cycle_writers(order)
    canonical = all(
        relabeled_images(writer, cycle_relabeling_to_shift(writer)) == shift_images(order)
        for writer in writers
    )
    if mutant == "cycle-classifier":
        canonical = False
    gate(
        gates,
        "RFB-PUBLIC-CYCLE",
        "full-cycle reversible writers are relabeling-conjugate to one cyclic shift",
        len(writers) == math.factorial(order - 1) and canonical,
        {"order": order, "writers": len(writers), "canonical": canonical},
    )

    gauge_order = 3
    shift = shift_images(gauge_order)
    orbits = phase_gauge_orbits(gauge_order, shift)
    invariants = [{winding_phase(decoration, gauge_order) for decoration in orbit} for orbit in orbits]
    gauge_ok = len(orbits) == gauge_order and all(len(values) == 1 for values in invariants)
    if mutant == "phase-gauge":
        gauge_ok = False
    gate(
        gates,
        "RFB-PUBLIC-PHASE-GAUGE",
        "vertex phase gauge leaves exactly the cycle-product exponent on a decorated cyclic writer",
        gauge_ok,
        {"order": gauge_order, "orbits": len(orbits), "invariants": sorted(next(iter(values)) for values in invariants)},
    )

    readers = reader_functions(order)
    additive = tuple(values for values in readers if reader_is_additive(values, order))
    reader_ok = len(additive) == order and {reader_charge(values, order) for values in additive} == set(range(order))
    if mutant == "reader-composition":
        reader_ok = False
    gate(
        gates,
        "RFB-PUBLIC-READER",
        "translation composition reduces phase readers to the character charges of the cyclic record",
        reader_ok,
        {"order": order, "general": len(readers), "additive": len(additive)},
    )

    pair_orbits = writer_reader_pair_orbits(order)
    orbit_invariants = tuple({pair_invariant(step, charge, order) for step, charge in orbit} for orbit in pair_orbits)
    pair_ok = len(pair_orbits) == order and all(len(values) == 1 for values in orbit_invariants)
    if mutant == "pair-orbit":
        pair_ok = False
    gate(
        gates,
        "RFB-PUBLIC-PAIR-ORBIT",
        "simultaneous cyclic relabeling quotients writer-step and reader-charge pairs by their product",
        pair_ok,
        {"order": order, "orbits": len(pair_orbits), "products": sorted(next(iter(values)) for values in orbit_invariants)},
    )

    constructive = two_history_ports(1)
    destructive = two_history_ports(-1)
    if mutant == "history-interference":
        destructive["coherent"] = destructive["exclusive"]
    if mutant == "history-positivity":
        destructive["functionals"]["plus"] = matrix([[Q(1, 4), Q(1, 2)], [Q(1, 2), Q(1, 4)]])
    history_ok = (
        constructive["coherent"] == {"plus": Q(1), "minus": Q(0)}
        and destructive["coherent"] == {"plus": Q(0), "minus": Q(1)}
        and constructive["exclusive"] == destructive["exclusive"] == {"plus": Q(1, 2), "minus": Q(1, 2)}
        and all(psd_2(functional) for row in (constructive, destructive) for functional in row["functionals"].values())
        and constructive["sum_functional"] == destructive["sum_functional"] == matscale(Q(1, 2), identity(2))
    )
    gate(
        gates,
        "RFB-PUBLIC-HISTORY",
        "two strongly positive port functionals retain a relative phase that an exclusive rewrite kernel discards",
        history_ok,
        {
            "constructive": constructive["coherent"],
            "destructive": destructive["coherent"],
            "exclusive": constructive["exclusive"],
        },
    )

    try:
        tag = hybrid_tag(Q(3, 5), Q(4, 5) if mutant != "hybrid-normalization" else Q(3, 5))
        hybrid_ok = psd_2(tag["gram"]) and tag["plus_probability"] == Q(4, 5) and tag["minus_probability"] == Q(1, 5)
    except ValueError:
        tag = {"overlap": Q(3, 5)}
        hybrid_ok = False
    gate(
        gates,
        "RFB-PUBLIC-HYBRID",
        "a normalized partial tag gives an exact intermediate visibility between erased and orthogonal endpoints",
        hybrid_ok,
        tag,
    )

    histories = ((0, 0), (0, 1), (1, 0), (1, 1))
    last = lambda history: history[-1]
    parity = lambda history: sum(history) % 2
    coarse = (lambda history: 0) if mutant == "predictive-partition" else last
    predictive_ok = summary_sufficient(histories, coarse, last) and not summary_sufficient(histories, parity, last)
    gate(
        gates,
        "RFB-PUBLIC-PREDICTIVE",
        "predictive sufficiency is a partition property and can distinguish two equally small history summaries",
        predictive_ok,
        {
            "last_blocks": len(partition_from_key(histories, last)),
            "parity_blocks": len(partition_from_key(histories, parity)),
        },
    )

    bell = matrix(
        [
            [Q(1, 2), 0, 0, Q(1, 2)],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [Q(1, 2), 0, 0, Q(1, 2)],
        ]
    )
    identity2 = identity(2)
    z = matrix([[1, 0], [0, -1]])
    local_identity = tensor(identity2, identity2)
    local_z = tensor(z, identity2)
    dephased = matadd(
        matscale(Q(1, 2), conjugate_by(local_identity, bell)),
        matscale(Q(1, 2), conjugate_by(local_z, bell)),
    )
    bob_before = partial_trace_a(bell, 2, 2)
    bob_after = partial_trace_a(dephased, 2, 2)
    if mutant == "locality":
        bob_after = matrix([[1, 0], [0, 0]])
    gate(
        gates,
        "RFB-PUBLIC-LOCALITY",
        "a complete local channel on one fixed factor preserves the remote unconditioned marginal",
        bob_before == bob_after == matscale(Q(1, 2), identity2),
        {"bob_before": bob_before, "bob_after": bob_after},
    )

    exact_marker: Any = Q(1, 7)
    if mutant == "exactness":
        exact_marker = float(exact_marker)
    gate(
        gates,
        "RFB-PUBLIC-EXACTNESS",
        "the public result surface contains no floating-point value",
        not contains_float({"marker": exact_marker, "gates": gates}),
        {"marker": exact_marker},
    )

    if tuple(row["gate"] for row in gates) != PUBLIC_GATE_NAMES:
        raise GateFail("RFB-PUBLIC-GATE-TOTALITY")
    return {
        "schema": "rfb-public-v1",
        "arithmetic": "exact rational matrices plus symbolic cyclic phase exponents",
        "scope": "generic algebra only; no RFB physical fixture or verdict",
        "measurements": {
            "cycle_calibration_order": order,
            "cycle_writer_count": len(writers),
            "phase_gauge_order": gauge_order,
            "phase_gauge_orbits": len(orbits),
            "general_reader_count": len(readers),
            "additive_reader_count": len(additive),
            "pair_orbit_count": len(pair_orbits),
            "constructive_plus": constructive["coherent"]["plus"],
            "destructive_plus": destructive["coherent"]["plus"],
            "exclusive_plus": constructive["exclusive"]["plus"],
            "hybrid_plus": tag["plus_probability"] if hybrid_ok else None,
            "fixed_factor_bob_invariant": bob_before == bob_after,
        },
        "gates": gates,
        "mutants": list(PUBLIC_MUTANTS),
    }


def render_transcript(result: Mapping[str, Any]) -> str:
    lines = [
        "RFB GENERIC PUBLIC CORE",
        f"schema={result['schema']}",
        f"scope={result['scope']}",
    ]
    for row in result["gates"]:
        evidence = json.dumps(row["evidence"], sort_keys=True, separators=(",", ":"))
        lines.append(f"[PASS]\t{row['gate']}\t{row['statement']}\t{evidence}")
    lines.extend(
        (
            f"gates={len(result['gates'])}",
            f"mutants={len(result['mutants'])}",
        )
    )
    return "\n".join(lines) + "\n"


def transcript_gate_rows(text: str) -> tuple[tuple[str, str, str], ...]:
    rows: list[tuple[str, str, str]] = []
    for line in text.splitlines():
        if line.startswith("[PASS]\t"):
            marker, name, statement, evidence = line.split("\t", 3)
            if marker != "[PASS]":
                raise GateFail("RFB-PUBLIC-TRANSCRIPT-MARKER")
            json.loads(evidence)
            rows.append((name, statement, evidence))
    return tuple(rows)


def expected_transcript_gate_rows(result: Mapping[str, Any]) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (
            row["gate"],
            row["statement"],
            json.dumps(row["evidence"], sort_keys=True, separators=(",", ":")),
        )
        for row in result["gates"]
    )


def finalize_result(result: dict[str, Any], transcript: str, source: Path, mutant: str | None) -> bytes:
    if transcript_gate_rows(transcript) != expected_transcript_gate_rows(result):
        raise GateFail("RFB-PUBLIC-TRANSCRIPT-LEDGER")
    result["source_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    result["transcript_sha256"] = hashlib.sha256(transcript.encode()).hexdigest()
    result["content_sha256"] = digest(result)
    if mutant == "payload-seal":
        result["measurements"]["fixed_factor_bob_invariant"] = False
    expected = result["content_sha256"]
    observed = digest({key: value for key, value in result.items() if key != "content_sha256"})
    if expected != observed:
        raise GateFail("RFB-PUBLIC-PAYLOAD-SEAL")
    if contains_float(result):
        raise GateFail("RFB-PUBLIC-FINAL-EXACTNESS")
    return canonical_json(result)


def stage_and_promote(payloads: Sequence[tuple[Path, bytes]]) -> None:
    targets = [path.resolve() for path, _payload in payloads]
    if len(set(targets)) != len(targets):
        raise ValueError("artifact targets must differ")
    if any(path.exists() for path in targets):
        raise FileExistsError("refusing to overwrite an existing target")
    temporaries: list[tuple[Path, Path]] = []
    try:
        for target, payload in zip(targets, (row[1] for row in payloads), strict=True):
            target.parent.mkdir(parents=True, exist_ok=True)
            handle, raw_temporary = tempfile.mkstemp(prefix=f".{target.name}.", dir=str(target.parent))
            temporary = Path(raw_temporary)
            with os.fdopen(handle, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            if temporary.read_bytes() != payload:
                raise GateFail("RFB-PUBLIC-STAGE-READBACK")
            temporaries.append((temporary, target))
        for temporary, target in temporaries:
            os.replace(temporary, target)
        for target, payload in zip(targets, (row[1] for row in payloads), strict=True):
            if target.read_bytes() != payload:
                raise GateFail("RFB-PUBLIC-PROMOTION-READBACK")
    finally:
        for temporary, _target in temporaries:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def default_paths() -> tuple[Path, Path]:
    here = Path(__file__).resolve().parent
    return here / "rfb_public_output.txt", here / "rfb_public_receipt.json"


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--mutant", choices=PUBLIC_MUTANTS)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--list-gates", action="store_true")
    parser.add_argument("--list-mutants", action="store_true")
    return parser.parse_args(list(argv))


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(sys.argv[1:] if argv is None else argv)
    modes = sum((arguments.selftest, arguments.list_gates, arguments.list_mutants))
    if modes > 1:
        raise SystemExit("choose exactly one inspection mode")
    if modes and (arguments.output is not None or arguments.receipt is not None or arguments.mutant is not None):
        raise SystemExit("inspection modes cannot be combined with generation options")
    if arguments.list_gates:
        sys.stdout.write("\n".join(PUBLIC_GATE_NAMES) + "\n")
        return 0
    if arguments.list_mutants:
        sys.stdout.write("\n".join(PUBLIC_MUTANTS) + "\n")
        return 0
    if arguments.selftest:
        clean = public_calibration()
        if len(clean["gates"]) != len(PUBLIC_GATE_NAMES):
            return 1
        try:
            public_calibration("history-interference")
        except GateFail:
            return 0
        return 1

    default_output, default_receipt = default_paths()
    output = (arguments.output or default_output).resolve()
    receipt = (arguments.receipt or default_receipt).resolve()
    try:
        result = public_calibration(arguments.mutant)
        transcript = render_transcript(result)
        receipt_payload = finalize_result(result, transcript, Path(__file__).resolve(), arguments.mutant)
        stage_and_promote(((output, transcript.encode()), (receipt, receipt_payload)))
    except (GateFail, ValueError, TypeError, ArithmeticError, FileExistsError) as error:
        print(f"RFB PUBLIC REFUSAL: {error}", file=sys.stderr)
        return 1
    sys.stdout.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
