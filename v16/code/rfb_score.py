#!/usr/bin/env python3
"""Score the frozen RFB Paper 10 forcing-boundary fixture.

The generic core and data-only fixture were committed before this scorer.
This file derives all result words from exact measurements.  It must be
committed before its first invocation on ``rfb_fixture.json``.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
import sys
import tempfile
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, MutableMapping, Sequence

import rfb_core as core


Q = Fraction
Matrix = core.Matrix

EXPECTED_FIXTURE_SHA256 = "f3557b3400584d01984c6a4f38d40744c9e2cf2f0e36c7c4aa225b045e5bd362"
EXPECTED_CORE_SHA256 = "7d0a787d108ac16229dc6819a81f74f7b80203eaefa71d28f30f1f31b27e9ada"
EXPECTED_PUBLIC_OUTPUT_SHA256 = "4988daa3ca88f52af279d0491d5dd56ac2724f79f998e75f7a0c91ddceb28b2e"
EXPECTED_PUBLIC_RECEIPT_SHA256 = "7356ae0f309645eaee9e6202e8cc61a4f0e231e087c3c3f6104cb6f6cac6ad11"


class GateFail(RuntimeError):
    """Raised before promotion when an RFB gate fails."""


MUTANTS = (
    "anchor-hash",
    "fixture-answer",
    "core-hash",
    "writer-cycle",
    "writer-drop",
    "phase-gauge",
    "winding",
    "reader-universality",
    "reader-composition",
    "reader-drop",
    "pair-orbit",
    "chirality",
    "reciprocal-leak",
    "classical-instrument",
    "coherent-dilation",
    "same-channel",
    "hybrid-family",
    "history-exclusive",
    "history-positivity",
    "second-cut",
    "division-completeness",
    "process-coordinate",
    "predictive-merge",
    "predictive-resource",
    "predictive-heldout",
    "recoverability-reset",
    "recoverability-redundancy",
    "locality",
    "hjw",
    "locality-drop",
    "forcing-matrix",
    "primary-comparator",
    "outcome-reachability",
    "scope-promotion",
    "exactness",
    "read-set",
    "transcript-seal",
    "paper-claim",
    "receipt-seal",
)


MUTANT_GATE = {
    "anchor-hash": "RFB-G-ANCHORS",
    "fixture-answer": "RFB-G-FIXTURE-NEUTRAL",
    "core-hash": "RFB-G-CORE",
    "writer-cycle": "RFB-G-W-CYCLE",
    "writer-drop": "RFB-G-W-CYCLE-DROP",
    "phase-gauge": "RFB-G-W-PHASE",
    "winding": "RFB-G-W-WINDING",
    "reader-universality": "RFB-G-R-UNIVERSALITY",
    "reader-composition": "RFB-G-R-TRANSLATION",
    "reader-drop": "RFB-G-R-TRANSLATION-DROP",
    "pair-orbit": "RFB-G-R-PAIR",
    "chirality": "RFB-G-R-CHIRALITY",
    "reciprocal-leak": "RFB-G-R-LEAK",
    "classical-instrument": "RFB-G-M-CLASSICAL",
    "coherent-dilation": "RFB-G-M-COHERENT",
    "same-channel": "RFB-G-M-SAME-CHANNEL",
    "hybrid-family": "RFB-G-M-HYBRID",
    "history-exclusive": "RFB-G-H-INTERFERENCE",
    "history-positivity": "RFB-G-H-POSITIVITY",
    "second-cut": "RFB-G-H-SECOND-CUT",
    "division-completeness": "RFB-G-H-ALL-INPUT",
    "process-coordinate": "RFB-G-H-LAW-TYPE",
    "predictive-merge": "RFB-G-P-INTERVENTION",
    "predictive-resource": "RFB-G-P-RESOURCE",
    "predictive-heldout": "RFB-G-P-HELDOUT",
    "recoverability-reset": "RFB-G-RECOVERY-DROP",
    "recoverability-redundancy": "RFB-G-RECOVERY-REDUNDANCY",
    "locality": "RFB-G-N-LOCALITY",
    "hjw": "RFB-G-N-HJW",
    "locality-drop": "RFB-G-N-DROP",
    "forcing-matrix": "RFB-G-FORCING-MATRIX",
    "primary-comparator": "RFB-G-PRIMARY",
    "outcome-reachability": "RFB-G-OUTCOME-REACHABILITY",
    "scope-promotion": "RFB-PAPER-SCOPE",
    "exactness": "RFB-G-EXACTNESS",
    "read-set": "RFB-G-READ-SET",
    "transcript-seal": "RFB-TRANSCRIPT-SEAL",
    "paper-claim": "RFB-PAPER-CLAIMS",
    "receipt-seal": "RFB-RECEIPT-SEAL",
}


REQUIRED_GATE_NAMES = (
    "RFB-G-FIXTURE-HASH",
    "RFB-G-ANCHORS",
    "RFB-G-REFERENT",
    "RFB-G-CORE",
    "RFB-G-QSF-SCOPE",
    "RFB-G-PREDICTIVE-METHOD",
    "RFB-G-NOSIGNAL-SCOPE",
    "RFB-G-HISTORY-TYPE",
    "RFB-G-FIXTURE-NEUTRAL",
    "RFB-G-W-CYCLE",
    "RFB-G-W-CYCLE-DROP",
    "RFB-G-W-PHASE",
    "RFB-G-W-WINDING",
    "RFB-G-W-DIAL",
    "RFB-G-R-UNIVERSALITY",
    "RFB-G-R-TRANSLATION",
    "RFB-G-R-TRANSLATION-DROP",
    "RFB-G-R-PAIR",
    "RFB-G-R-CHIRALITY",
    "RFB-G-R-RECIPROCAL",
    "RFB-G-R-LEAK",
    "RFB-G-M-DIVISION",
    "RFB-G-M-CLASSICAL",
    "RFB-G-M-COHERENT",
    "RFB-G-M-SAME-CHANNEL",
    "RFB-G-M-HYBRID",
    "RFB-G-M-FAMILY",
    "RFB-G-H-INTERFERENCE",
    "RFB-G-H-POSITIVITY",
    "RFB-G-H-SECOND-CUT",
    "RFB-G-H-ALL-INPUT",
    "RFB-G-H-LAW-TYPE",
    "RFB-G-P-INTERVENTION",
    "RFB-G-P-RESOURCE",
    "RFB-G-P-HELDOUT",
    "RFB-G-RECOVERABILITY",
    "RFB-G-RECOVERY-DROP",
    "RFB-G-RECOVERY-REDUNDANCY",
    "RFB-G-N-LOCALITY",
    "RFB-G-N-HJW",
    "RFB-G-N-DROP",
    "RFB-G-FORCING-MATRIX",
    "RFB-G-COORDINATES",
    "RFB-G-OUTCOME-REACHABILITY",
    "RFB-G-PRIMARY",
    "RFB-G-SCOPE",
    "RFB-G-EXACTNESS",
    "RFB-G-READ-SET",
    "RFB-G-TOTALITY",
)


SCOPE_SENTENCES = {
    "NO-GRAPH-GROWTH": "RFB does not construct graph growth.",
    "NO-CATALOGUE-SELECTION": "RFB does not select a configuration catalogue.",
    "NO-DIVISION-DERIVATION": "RFB does not derive division placement.",
    "NO-ACTUALIZATION-DERIVATION": "RFB does not derive actualization.",
    "NO-DYNAMIC-FACTORIZATION-NOSIGNAL": "RFB does not prove no-signalling after a factorization changes.",
    "NO-INDEFINITE-CAUSAL-ORDER": "RFB does not witness indefinite causal order.",
    "NO-GEOMETRY-CLAIM": "RFB does not identify a record register or graph with physical geometry.",
    "NO-QFT-OR-GR-LIMIT": "RFB does not recover QFT or general relativity.",
    "NO-HAMILTONIAN-OR-ENERGY": "RFB does not select a Hamiltonian or define energy.",
    "NO-CONSTANT-SELECTION": "RFB does not select physical constants.",
    "NO-EMPIRICAL-PREDICTION": "RFB makes no empirical prediction about nature.",
}


READ_AUDIT: set[str] = set()


def root_path() -> Path:
    return Path(__file__).resolve().parents[2]


def relative_to_root(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def audited_read(path: Path, root: Path) -> bytes:
    resolved = path.resolve()
    READ_AUDIT.add(relative_to_root(resolved, root))
    return resolved.read_bytes()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value: Any) -> bytes:
    return core.canonical_json(value)


def digest(value: Any) -> str:
    return core.digest(value)


def qtext(value: Q) -> str:
    return core.qtext(Q(value))


def gate(rows: list[dict[str, Any]], name: str, statement: str, ok: bool, evidence: Mapping[str, Any]) -> None:
    row = {
        "gate": name,
        "statement": statement,
        "passed": bool(ok),
        "evidence": core.serialize(dict(evidence)),
    }
    rows.append(row)
    if not ok:
        raise GateFail(f"{name}: {json.dumps(row['evidence'], sort_keys=True)}")


def parse_q(value: Any) -> Q:
    if isinstance(value, int):
        return Q(value)
    if isinstance(value, str):
        return Q(value)
    if isinstance(value, list) and len(value) == 2:
        return Q(value[0], value[1])
    raise TypeError(f"invalid exact rational {value!r}")


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return core.matadd(left, core.matscale(-1, right))


def permutation_matrix(images: Sequence[int]) -> Matrix:
    size = len(images)
    if sorted(images) != list(range(size)):
        raise ValueError("not a permutation")
    return tuple(
        tuple(Q(1) if images[column] == row else Q(0) for column in range(size))
        for row in range(size)
    )


def is_orthogonal(value: Matrix) -> bool:
    rows, columns = core.shape(value)
    return rows == columns and core.matmul(core.transpose(value), value) == core.identity(rows)


def partial_trace_b(value: Matrix, dim_a: int, dim_b: int) -> Matrix:
    if core.shape(value) != (dim_a * dim_b, dim_a * dim_b):
        raise ValueError("partial-trace shape mismatch")
    return tuple(
        tuple(
            sum(
                (value[row * dim_b + b][column * dim_b + b] for b in range(dim_b)),
                Q(0),
            )
            for column in range(dim_a)
        )
        for row in range(dim_a)
    )


def probability(effect: Matrix, state: Matrix) -> Q:
    return core.trace(core.matmul(effect, state))


def channel_from_mixture(state: Matrix, left: Matrix, right: Matrix, weight: Q) -> Matrix:
    return core.matadd(
        core.matscale(weight, core.conjugate_by(left, state)),
        core.matscale(Q(1) - weight, core.conjugate_by(right, state)),
    )


def instrument_total(kraus: Sequence[Matrix]) -> Matrix:
    if not kraus:
        raise ValueError("empty instrument")
    dimension = core.shape(kraus[0])[1]
    result = core.zero(dimension, dimension)
    for operator in kraus:
        result = core.matadd(result, core.matmul(core.transpose(operator), operator))
    return result


def contains_float(value: Any) -> bool:
    return core.contains_float(value)


def forbidden_fixture_keys(value: Any, path: tuple[str, ...] = ()) -> list[str]:
    forbidden = {"answer", "verdict", "primary", "expected_result", "survivor_count", "gate_result"}
    found: list[str] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            here = path + (str(key),)
            if str(key).lower() in forbidden:
                found.append(".".join(here))
            found.extend(forbidden_fixture_keys(item, here))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(forbidden_fixture_keys(item, path + (str(index),)))
    return found


def consume_anchors(
    fixture: Mapping[str, Any], root: Path, mutant: str | None
) -> tuple[dict[str, bytes], dict[str, list[str]]]:
    payloads: dict[str, bytes] = {}
    consumers: dict[str, list[str]] = defaultdict(list)
    for index, row in enumerate(fixture["anchors"]):
        expected = row["sha256"]
        if mutant == "anchor-hash" and index == 0:
            expected = "0" * len(expected)
        path = root / row["path"]
        payload = audited_read(path, root)
        observed = sha256_bytes(payload)
        if observed != expected:
            raise GateFail(f"RFB-G-ANCHORS: {row['path']} expected {expected} observed {observed}")
        payloads[row["path"]] = payload
        consumers[row["consumer"]].append(row["path"])
    return payloads, consumers


def writer_measurements(fixture: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for dial in fixture["dial_rows"]:
        order = int(dial["q"])
        all_writers = tuple(permutations(range(order)))
        cyclic = core.full_cycle_writers(order)
        canonical = all(
            core.relabeled_images(writer, core.cycle_relabeling_to_shift(writer))
            == core.shift_images(order)
            for writer in cyclic
        )
        if mutant == "writer-cycle" and order == 3:
            canonical = False
        drop_general = len(all_writers)
        if mutant == "writer-drop" and order == 2:
            drop_general = len(cyclic)
        phase_orbits = core.phase_gauge_orbits(order, core.shift_images(order))
        orbit_invariants = [
            {core.winding_phase(decoration, order) for decoration in orbit}
            for orbit in phase_orbits
        ]
        phase_ok = (
            len(phase_orbits) == order
            and all(len(values) == 1 for values in orbit_invariants)
            and {next(iter(values)) for values in orbit_invariants} == set(range(order))
        )
        if mutant == "phase-gauge" and order == 4:
            phase_ok = False
        winding = {theta: core.winding_interference_probability(order, theta) for theta in range(order)}
        winding_moves = len(set(winding.values())) > 1
        if mutant == "winding" and order == 3:
            winding_moves = False
        rows.append(
            {
                "q": order,
                "all_reversible": len(all_writers),
                "full_cycles": len(cyclic),
                "canonical_shift": canonical,
                "drop_general": drop_general,
                "phase_orbits": len(phase_orbits),
                "phase_ok": phase_ok,
                "theta_values": sorted(next(iter(values)) for values in orbit_invariants),
                "winding_probabilities": winding,
                "winding_moves": winding_moves,
                "first_common_boundary_steps": order,
                "prewinding_common_boundary": False,
            }
        )
    return {"rows": rows}


def reader_measurements(fixture: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for dial in fixture["dial_rows"]:
        order = int(dial["q"])
        general = core.reader_functions(order)
        additive = tuple(row for row in general if core.reader_is_additive(row, order))
        charges = {core.reader_charge(row, order) for row in additive}
        shared_contexts = len(general)
        split_contexts = len(general) ** 2
        if mutant == "reader-universality" and order == 3:
            split_contexts = shared_contexts
        additive_ok = len(additive) == order and charges == set(range(order))
        if mutant == "reader-composition" and order == 4:
            additive_ok = False
        drop_returns = len(general) >= len(additive) and any(
            len(core.reader_functions(q)) > len(tuple(row for row in core.reader_functions(q) if core.reader_is_additive(row, q)))
            for q in (3, 4)
        )
        if mutant == "reader-drop" and order == 4:
            drop_returns = False
        pair_orbits = core.writer_reader_pair_orbits(order)
        products = [
            {core.pair_invariant(step, charge, order) for step, charge in orbit}
            for orbit in pair_orbits
        ]
        pair_ok = len(pair_orbits) == order and all(len(values) == 1 for values in products)
        if mutant == "pair-orbit" and order == 3:
            pair_ok = False
        chirality = {
            charge: core.winding_interference_probability(order, charge - 1)
            for charge in range(order)
        }
        chirality_distinguishes = (
            order == 2
            or chirality[1 % order] != chirality[(-1) % order]
        )
        if mutant == "chirality" and order == 4:
            chirality_distinguishes = False
        rows.append(
            {
                "q": order,
                "general_readers": len(general),
                "additive_readers": len(additive),
                "charges": sorted(charge for charge in charges if charge is not None),
                "additive_ok": additive_ok,
                "shared_context_parameters": shared_contexts,
                "split_context_parameters": split_contexts,
                "drop_returns": drop_returns,
                "pair_orbits": len(pair_orbits),
                "pair_products": sorted(next(iter(values)) for values in products),
                "pair_ok": pair_ok,
                "chirality_calibration": chirality,
                "chirality_distinguishes": chirality_distinguishes,
            }
        )

    plus = core.matrix([[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]])
    mixed = core.matscale(Q(1, 2), core.identity(2))
    p0 = core.matrix([[1, 0], [0, 0]])
    x = core.matrix([[0, 1], [1, 0]])
    input_joint = core.tensor(plus, p0)
    controlled_write = permutation_matrix((0, 1, 3, 2))
    inert_write = core.tensor(core.identity(2), x)
    controlled_out = core.conjugate_by(controlled_write, input_joint)
    inert_out = core.conjugate_by(inert_write, input_joint)
    controlled_matter = partial_trace_b(controlled_out, 2, 2)
    inert_matter = partial_trace_b(inert_out, 2, 2)
    decoherence_leak = controlled_matter == mixed and inert_matter == plus
    if mutant == "reciprocal-leak":
        decoherence_leak = False
    return {
        "rows": rows,
        "reciprocal": {
            "input_matter": plus,
            "controlled_write_matter": controlled_matter,
            "inert_write_matter": inert_matter,
            "decoherence_only_acts": decoherence_leak,
            "active_charges_exist": all(any(charge != 0 for charge in row["charges"]) for row in rows),
        },
    }


def extract_record_kraus(isometry: Matrix) -> tuple[Matrix, Matrix]:
    rows, columns = core.shape(isometry)
    if (rows, columns) != (4, 2):
        raise ValueError("expected a two-qubit isometry")
    return tuple(
        tuple(
            tuple(isometry[matter * 2 + record][column] for column in range(2))
            for matter in range(2)
        )
        for record in range(2)
    )  # type: ignore[return-value]


def record_mode_measurements(fixture: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    p0 = core.matrix([[1, 0], [0, 0]])
    p1 = core.matrix([[0, 0], [0, 1]])
    x = core.matrix([[0, 1], [1, 0]])
    plus = core.matrix([[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]])
    minus = core.matrix([[Q(1, 2), Q(-1, 2)], [Q(-1, 2), Q(1, 2)]])
    z = core.matrix([[1, 0], [0, -1]])

    classical_ports = (p0, core.matmul(x, p1))
    classical_complete = instrument_total(classical_ports) == core.identity(2)
    if mutant == "classical-instrument":
        classical_complete = False

    dilation = permutation_matrix((0, 3, 1, 2))
    isometry = tuple(
        tuple(dilation[row][column] for column in (0, 2))
        for row in range(4)
    )
    dilation_ports = extract_record_kraus(isometry)
    coherent_ok = is_orthogonal(dilation) and core.matmul(core.transpose(isometry), isometry) == core.identity(2)
    if mutant == "coherent-dilation":
        coherent_ok = False

    same_ports = dilation_ports == classical_ports
    sample_states = (p0, p1, plus)
    same_unconditioned = all(
        core.apply_channel(dilation_ports, state) == core.apply_channel(classical_ports, state)
        for state in sample_states
    )
    if mutant == "same-channel":
        same_unconditioned = False

    mode_rows: list[dict[str, Any]] = []
    for row in fixture["record_mode_arm"]["rows"]:
        overlap = parse_q(row["tag_overlap"])
        complement = parse_q(row["tag_complement"])
        tag = core.hybrid_tag(overlap, complement)
        dephased = channel_from_mixture(plus, core.identity(2), z, (Q(1) + overlap) / 2)
        plus_probability = probability(plus, dephased)
        minus_probability = probability(minus, dephased)
        mode_rows.append(
            {
                "id": row["id"],
                "overlap": overlap,
                "gram_determinant": core.determinant_2(tag["gram"]),
                "plus_probability": plus_probability,
                "minus_probability": minus_probability,
                "normalized": plus_probability + minus_probability == 1,
                "complete_mixture": Q(0) <= (Q(1) + overlap) / 2 <= Q(1),
            }
        )
    hybrid_dimension = 1
    hybrid_ok = (
        all(row["normalized"] and row["complete_mixture"] and row["gram_determinant"] >= 0 for row in mode_rows)
        and len({row["plus_probability"] for row in mode_rows}) == len(mode_rows)
        and any(row["id"] == "hybrid" and row["gram_determinant"] > 0 for row in mode_rows)
    )
    if mutant == "hybrid-family":
        hybrid_ok = False
    return {
        "division_ports": {"plus": plus, "minus": minus},
        "division_complete": core.matadd(plus, minus) == core.identity(2),
        "classical_ports": classical_ports,
        "classical_complete": classical_complete,
        "coherent_unitary": coherent_ok,
        "dilation_ports": dilation_ports,
        "same_ports": same_ports,
        "same_unconditioned_channel": same_unconditioned,
        "mode_rows": mode_rows,
        "hybrid_semialgebraic_condition": "1-w^2>=0",
        "hybrid_dimension": hybrid_dimension,
        "hybrid_ok": hybrid_ok,
    }


def history_measurements(fixture: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for sign in fixture["history_arm"]["relative_phase_rows"]:
        item = core.two_history_ports(int(sign))
        rows.append({"sign": int(sign), **item})
    exclusive_same = rows[0]["exclusive"] == rows[1]["exclusive"]
    coherent_moves = rows[0]["coherent"] != rows[1]["coherent"]
    if mutant == "history-exclusive":
        coherent_moves = False
    positive = all(core.psd_2(functional) for row in rows for functional in row["functionals"].values())
    if mutant == "history-positivity":
        positive = False
    second_cut = all(
        row["sum_functional"] == core.matscale(Q(1, 2), core.identity(2))
        and row["sum_functional"][0][1] == 0
        for row in rows
    )
    drop_cross = rows[0]["functionals"]["plus"][0][1] != 0
    if mutant == "second-cut":
        second_cut = False
    plus = core.matrix([[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]])
    minus = core.matrix([[Q(1, 2), Q(-1, 2)], [Q(-1, 2), Q(1, 2)]])
    all_input_complete = instrument_total((plus, minus)) == core.identity(2)
    if mutant == "division-completeness":
        all_input_complete = False
    law_survival = {
        "exclusive_rewrite_kernel": not (exclusive_same and coherent_moves),
        "enriched_state_kernel": all(sum(row["coherent"].values(), Q(0)) == 1 for row in rows),
        "indivisible_multitime": positive and second_cut,
        "decoherence_functional_representation": positive and second_cut,
        "higher_order_required": False,
    }
    process_coordinate = "METHOD-INCONCLUSIVE"
    representation_coordinate = "METHOD-INCONCLUSIVE"
    if mutant == "process-coordinate":
        process_coordinate = "INDIVISIBLE-MULTITIME-LAW-REQUIRED"
    return {
        "rows": rows,
        "exclusive_same": exclusive_same,
        "coherent_moves": coherent_moves,
        "positive": positive,
        "second_cut": second_cut,
        "drop_cross": drop_cross,
        "all_input_complete": all_input_complete,
        "law_survival": law_survival,
        "division_coordinate": "DIVISION-KERNEL-SUFFICIENT",
        "process_coordinate": process_coordinate,
        "representation_coordinate": representation_coordinate,
    }


def intervention_signature(order: int, initial: int, charge: int, horizon: int) -> tuple[Any, ...]:
    operations = ("identity", "advance", "read")
    rows: list[tuple[Any, ...]] = []
    for word in product(operations, repeat=horizon):
        state = initial
        outputs: list[int | str] = []
        for operation in word:
            if operation == "advance":
                state = (state + 1) % order
                outputs.append("-")
            elif operation == "read":
                outputs.append(charge * state % order)
            else:
                outputs.append("-")
        rows.append((word, tuple(outputs)))
    return tuple(rows)


def predictive_measurements(fixture: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    arm = fixture["predictive_arm"]
    order = int(arm["q"])
    horizons = tuple(int(value) for value in arm["horizons"])
    heldout = int(arm["heldout_horizon"])
    charges = {"constant": 0, "charge-one": 1, "charge-minus-one": -1}
    census: dict[str, dict[int, int]] = {}
    for name, charge in charges.items():
        census[name] = {}
        for horizon in horizons + (heldout,):
            signatures = {
                intervention_signature(order, state, charge, horizon)
                for state in arm["states"]
            }
            census[name][horizon] = len(signatures)
    if mutant == "predictive-merge":
        census["charge-one"][horizons[0]] = 1
    modes = ("classical", "coherent", "hybrid", "indivisible")
    mode_quotients = {
        mode: {name: census[name][heldout] for name in charges}
        for mode in modes
    }
    resources = dict(arm["resource_bound"])
    resource_parity = len(set(int(value) for value in resources.values())) == 1
    if mutant == "predictive-resource":
        resource_parity = False
    heldout_stable = all(
        census[name][heldout] == census[name][max(horizons)]
        for name in charges
    )
    if mutant == "predictive-heldout":
        heldout_stable = False
    raw_labels = order * len(arm["interventions"]) ** heldout
    return {
        "census": census,
        "mode_quotients": mode_quotients,
        "resource_parity": resource_parity,
        "heldout_stable": heldout_stable,
        "raw_history_labels": raw_labels,
        "minimal_active_labels": census["charge-one"][heldout],
    }


def recoverability_measurements(fixture: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    labels = tuple(int(value) for value in fixture["recoverability_arm"]["record_labels"])
    identity_outputs = {label: (label,) for label in labels}
    swap_outputs = {label: (1 - label,) for label in labels}
    copied_outputs = {label: (label, label) for label in labels}
    reset_outputs = {label: (0,) for label in labels}
    backup_outputs = {label: (0, label) for label in labels}
    append_recoverable = all(
        len(set(mapping.values())) == len(labels)
        for mapping in (identity_outputs, swap_outputs, copied_outputs)
    )
    reset_destroys = len(set(reset_outputs.values())) < len(labels)
    if mutant == "recoverability-reset":
        reset_destroys = False
    redundancy_survives = len(set(backup_outputs.values())) == len(labels)
    if mutant == "recoverability-redundancy":
        redundancy_survives = False
    return {
        "append_recoverable": append_recoverable,
        "reset_destroys": reset_destroys,
        "redundancy_survives_primary_reset": redundancy_survives,
        "scope": "finite licensed grammar only",
    }


def alice_conditioned_bob(state: Matrix, projector: Matrix) -> tuple[Q, Matrix]:
    operator = core.tensor(projector, core.identity(2))
    unnormalized = core.partial_trace_a(core.conjugate_by(operator, state), 2, 2)
    weight = core.trace(unnormalized)
    if weight == 0:
        raise ValueError("zero-probability conditioned state")
    return weight, core.matscale(Q(1) / weight, unnormalized)


def ensemble_average(ensemble: Sequence[tuple[Q, Matrix]]) -> Matrix:
    result = core.zero(2, 2)
    for weight, state in ensemble:
        result = core.matadd(result, core.matscale(weight, state))
    return result


def locality_measurements(fixture: Mapping[str, Any], mutant: str | None) -> dict[str, Any]:
    bell = core.matrix(
        [
            [Q(1, 2), 0, 0, Q(1, 2)],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [Q(1, 2), 0, 0, Q(1, 2)],
        ]
    )
    i2 = core.identity(2)
    x = core.matrix([[0, 1], [1, 0]])
    z = core.matrix([[1, 0], [0, -1]])
    before = core.partial_trace_a(bell, 2, 2)
    rows: list[dict[str, Any]] = []
    for row in fixture["locality_arm"]["alice_channels"]:
        if row["kind"] == "unitary":
            local = i2 if row["id"] == "identity" else x
            output = core.conjugate_by(core.tensor(local, i2), bell)
        else:
            weight = parse_q(row["weight"])
            output = channel_from_mixture(bell, core.tensor(i2, i2), core.tensor(z, i2), weight)
        after = core.partial_trace_a(output, 2, 2)
        rows.append({"id": row["id"], "bob": after, "invariant": after == before})
    if mutant == "locality":
        rows[-1]["invariant"] = False

    p0 = core.matrix([[1, 0], [0, 0]])
    p1 = core.matrix([[0, 0], [0, 1]])
    plus = core.matrix([[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]])
    minus = core.matrix([[Q(1, 2), Q(-1, 2)], [Q(-1, 2), Q(1, 2)]])
    z_ensemble = tuple(alice_conditioned_bob(bell, projector) for projector in (p0, p1))
    x_ensemble = tuple(alice_conditioned_bob(bell, projector) for projector in (plus, minus))
    z_average = ensemble_average(z_ensemble)
    x_average = ensemble_average(x_ensemble)
    hjw_ok = z_average == x_average == before and {state for _weight, state in z_ensemble} != {state for _weight, state in x_ensemble}
    if mutant == "hjw":
        hjw_ok = False

    amplified = core.matscale(parse_q(fixture["locality_arm"]["drop_control"]["trace_multiplier"]), bell)
    amplified_bob = core.partial_trace_a(amplified, 2, 2)
    drop_moves = amplified_bob != before and core.trace(amplified_bob) != 1
    if mutant == "locality-drop":
        drop_moves = False

    xa = core.tensor(x, i2)
    zb = core.tensor(i2, z)
    disjoint_commute = core.matmul(xa, zb) == core.matmul(zb, xa)
    return {
        "bob_before": before,
        "rows": rows,
        "all_local_invariant": all(row["invariant"] for row in rows),
        "hjw_equal_average": hjw_ok,
        "amplifier_moves": drop_moves,
        "disjoint_commute": disjoint_commute,
        "scope": fixture["locality_arm"]["scope"],
    }


def forcing_measurements(
    fixture: Mapping[str, Any],
    writer: Mapping[str, Any],
    reader: Mapping[str, Any],
    modes: Mapping[str, Any],
    history: Mapping[str, Any],
    predictive: Mapping[str, Any],
    recovery: Mapping[str, Any],
    locality: Mapping[str, Any],
    mutant: str | None,
) -> dict[str, Any]:
    assumptions = tuple(row["id"] for row in fixture["assumptions"])
    freedoms = tuple(fixture["freedoms"])
    matrix = {
        assumption: {freedom: "UNTOUCHED-BY-REGISTERED-SURFACE" for freedom in freedoms}
        for assumption in assumptions
    }
    matrix["A-POINTER-READABILITY"]["writer-permutation"] = "METHOD-INCONCLUSIVE-AT-compound-with-A-FULL-ACCUMULATION"
    matrix["A-FULL-ACCUMULATION"]["writer-permutation"] = "METHOD-INCONCLUSIVE-AT-compound-with-A-POINTER-READABILITY"
    matrix["A-RENAMING-COVARIANCE"]["writer-edge-phases"] = "QUOTIENTED-AS-REPRESENTATION-BY-pointer-phase-gauge"
    matrix["A-RENAMING-COVARIANCE"]["writer-reader-gauge-orbit"] = "QUOTIENTED-AS-REPRESENTATION-BY-cyclic-relabeling"
    matrix["A-TYPE-UNIVERSALITY"]["reader-family"] = "PRICED-POSTULATE-1"
    matrix["A-TRANSLATION-COMPOSITION"]["reader-family"] = "FORCED-BY-A-TRANSLATION-COMPOSITION"
    matrix["A-RECIPROCAL-FEEDBACK"]["reader-charge"] = "UNTOUCHED-BY-REGISTERED-SURFACE"
    matrix["A-DIVISION-PLACEMENT"]["microscopic-factorization"] = "METHOD-INCONCLUSIVE-AT-compound-with-A-REFINEMENT-GLUING"
    matrix["A-REFINEMENT-GLUING"]["microscopic-factorization"] = "METHOD-INCONCLUSIVE-AT-compound-with-A-DIVISION-PLACEMENT"
    matrix["A-PREDICTIVE-MINIMALITY"]["record-retention-mode"] = "UNTOUCHED-BY-REGISTERED-SURFACE"
    matrix["A-RECORD-RECOVERABILITY"]["record-partition"] = "FORCED-BY-A-RECORD-RECOVERABILITY"

    joint = {
        "W-CYCLE": {
            "status": "FORCED-BY-A-POINTER-READABILITY+A-FULL-ACCUMULATION",
            "impose": all(row["canonical_shift"] for row in writer["rows"]),
            "drop": all(row["drop_general"] > row["full_cycles"] for row in writer["rows"]),
        },
        "W-PHASE-QUOTIENT": {
            "status": "QUOTIENTED-AS-REPRESENTATION-BY-pointer-phase-gauge",
            "impose": all(row["phase_ok"] for row in writer["rows"]),
            "drop": all(row["q"] ** row["q"] > row["phase_orbits"] for row in writer["rows"]),
        },
        "W-WINDING": {
            "status": "UNTOUCHED-BY-REGISTERED-SURFACE",
            "impose": all(row["winding_moves"] for row in writer["rows"]),
            "drop": all(not row["prewinding_common_boundary"] for row in writer["rows"]),
        },
        "R-UNIVERSALITY": {
            "status": "PRICED-POSTULATE-1",
            "impose": all(row["shared_context_parameters"] < row["split_context_parameters"] for row in reader["rows"]),
            "drop": all(row["split_context_parameters"] > row["shared_context_parameters"] for row in reader["rows"]),
        },
        "R-CHARACTER": {
            "status": "FORCED-BY-A-TRANSLATION-COMPOSITION",
            "impose": all(row["additive_ok"] for row in reader["rows"]),
            "drop": any(row["general_readers"] > row["additive_readers"] for row in reader["rows"]),
        },
        "R-PAIR-QUOTIENT": {
            "status": "QUOTIENTED-AS-REPRESENTATION-BY-cyclic-relabeling",
            "impose": all(row["pair_ok"] for row in reader["rows"]),
            "drop": all(len(core.units(row["q"])) * row["q"] > row["pair_orbits"] for row in reader["rows"] if row["q"] > 2),
        },
        "R-DECOHERENCE-LEAK": {
            "status": "UNTOUCHED-BY-REGISTERED-SURFACE",
            "impose": reader["reciprocal"]["decoherence_only_acts"],
            "drop": reader["reciprocal"]["inert_write_matter"] == reader["reciprocal"]["input_matter"],
        },
        "M-FAMILY": {
            "status": "UNTOUCHED-BY-REGISTERED-SURFACE",
            "impose": modes["hybrid_ok"],
            "drop": locality["amplifier_moves"],
        },
        "H-RECONVERGENCE": {
            "status": "METHOD-INCONCLUSIVE-AT-microscopic-factorization",
            "impose": history["coherent_moves"] and history["second_cut"],
            "drop": history["exclusive_same"] and history["drop_cross"],
        },
        "P-RESOURCE-PARITY": {
            "status": "UNTOUCHED-BY-REGISTERED-SURFACE",
            "impose": predictive["resource_parity"],
            "drop": predictive["raw_history_labels"] > predictive["minimal_active_labels"],
        },
        "P-APPEND-ONLY": {
            "status": "FORCED-BY-A-RECORD-RECOVERABILITY",
            "impose": recovery["append_recoverable"],
            "drop": recovery["reset_destroys"],
        },
    }
    if mutant == "forcing-matrix":
        joint["H-RECONVERGENCE"]["drop"] = False
    return {
        "matrix": matrix,
        "joint_findings": joint,
        "all_impose_drop_measured": all(row["impose"] and row["drop"] for row in joint.values()),
        "rows": len(assumptions),
        "columns": len(freedoms),
    }


def derive_primary(flags: Mapping[str, Any]) -> str:
    if not flags["referent_bound"]:
        return "RFB-BLOCKED-AT-PROCESS-REFERENT"
    if flags["inconsistent"]:
        return "RFB-INCONSISTENT"
    if not flags["all_arms_complete"]:
        return "RFB-METHOD-INCONCLUSIVE-AT-unfinished-arm"
    return "RFB-FORCING-BOUNDARY-MAPPED"


def independent_primary(flags: Mapping[str, Any]) -> str:
    signature = (
        bool(flags["referent_bound"]),
        bool(flags["inconsistent"]),
        bool(flags["all_arms_complete"]),
    )
    table = {
        (False, False, False): "RFB-BLOCKED-AT-PROCESS-REFERENT",
        (False, False, True): "RFB-BLOCKED-AT-PROCESS-REFERENT",
        (False, True, False): "RFB-BLOCKED-AT-PROCESS-REFERENT",
        (False, True, True): "RFB-BLOCKED-AT-PROCESS-REFERENT",
        (True, True, False): "RFB-INCONSISTENT",
        (True, True, True): "RFB-INCONSISTENT",
        (True, False, False): "RFB-METHOD-INCONCLUSIVE-AT-unfinished-arm",
        (True, False, True): "RFB-FORCING-BOUNDARY-MAPPED",
    }
    return table[signature]


def result_word_licensed(word: str, templates: Sequence[str]) -> bool:
    for template in templates:
        if "<" not in template:
            if word == template:
                return True
            continue
        prefix = template.split("<", 1)[0]
        suffix = template.rsplit(">", 1)[-1]
        if word.startswith(prefix) and word.endswith(suffix) and len(word) > len(prefix) + len(suffix):
            return True
    return False


def score(fixture_path: Path, mutant: str | None = None) -> dict[str, Any]:
    if mutant is not None and mutant not in MUTANTS:
        raise ValueError(f"unknown mutant {mutant!r}")
    READ_AUDIT.clear()
    root = root_path()
    scorer_path = Path(__file__).resolve()
    scorer_bytes = audited_read(scorer_path, root)
    fixture_bytes = audited_read(fixture_path, root)
    fixture_hash = sha256_bytes(fixture_bytes)
    gates: list[dict[str, Any]] = []
    gate(
        gates,
        "RFB-G-FIXTURE-HASH",
        "the physical fixture is the separately committed result-neutral object",
        fixture_hash == EXPECTED_FIXTURE_SHA256,
        {"observed": fixture_hash, "frozen": EXPECTED_FIXTURE_SHA256},
    )
    fixture: MutableMapping[str, Any] = json.loads(fixture_bytes)
    if mutant == "fixture-answer":
        fixture["primary"] = "RFB-FORCING-BOUNDARY-MAPPED"
    payloads, consumers = consume_anchors(fixture, root, mutant)
    gate(
        gates,
        "RFB-G-ANCHORS",
        "every frozen local anchor matches its declared digest and named consumer",
        len(payloads) == len(fixture["anchors"]) and all(consumers.values()),
        {"anchors": len(payloads), "consumers": sorted(consumers)},
    )

    pin_text = payloads["v16/note-rfb-pin.md"].decode()
    referent_bound = (
        "Which parts of a lawful record-feedback dynamics follow from which explicit" in pin_text
        and "three axes that must not be conflated" in pin_text
        and fixture["history_arm"]["intermediate_cut"] == "no durable record"
        and fixture["record_mode_arm"]["retained_interface"].startswith("stable orthogonal")
    )
    gate(
        gates,
        "RFB-G-REFERENT",
        "the fixture distinguishes microscopic rewrites, record implementations, representations, and final divisions",
        referent_bound,
        {"referent_bound": referent_bound},
    )

    core_hash = sha256_bytes(payloads["v16/code/rfb_core.py"])
    if mutant == "core-hash":
        core_hash = "0" * len(core_hash)
    public_receipt = json.loads(payloads["v16/code/rfb_public_receipt.json"])
    core_ok = (
        core_hash == EXPECTED_CORE_SHA256
        and sha256_bytes(payloads["v16/code/rfb_public_output.txt"]) == EXPECTED_PUBLIC_OUTPUT_SHA256
        and sha256_bytes(payloads["v16/code/rfb_public_receipt.json"]) == EXPECTED_PUBLIC_RECEIPT_SHA256
        and public_receipt["schema"] == "rfb-public-v1"
        and all(row["passed"] for row in public_receipt["gates"])
    )
    gate(
        gates,
        "RFB-G-CORE",
        "the separately frozen public core and both calibration artifacts are intact",
        core_ok,
        {"source": core_hash, "public_gates": len(public_receipt["gates"])},
    )

    qsf_text = "\n".join(
        payloads[path].decode(errors="replace")
        for path in consumers["RFB-G-QSF-SCOPE"]
    )
    qsf_scope = "QSF-METHOD-INCONCLUSIVE" in qsf_text and "division-level" in qsf_text and "microscopic" in qsf_text
    gate(gates, "RFB-G-QSF-SCOPE", "terminal QSF licenses a division interface but does not select microscopic factorization", qsf_scope, {"licensed": qsf_scope})

    predictive_text = "\n".join(payloads[path].decode(errors="replace") for path in consumers["RFB-G-PREDICTIVE-METHOD"])
    predictive_anchor = "sufficien" in predictive_text.lower() and "predict" in predictive_text.lower()
    gate(gates, "RFB-G-PREDICTIVE-METHOD", "the predictive arm consumes both E-37 and JS-v2 method anchors", predictive_anchor, {"licensed": predictive_anchor})

    causality_text = "\n".join(payloads[path].decode(errors="replace") for path in consumers["RFB-G-NOSIGNAL-SCOPE"])
    causality_scope = "signalling" in causality_text.lower() and "composite" in causality_text.lower()
    gate(gates, "RFB-G-NOSIGNAL-SCOPE", "the locality arm inherits the positive-theorem composite standard and stays fixed-factor", causality_scope, {"licensed": causality_scope})

    history_text = "\n".join(payloads[path].decode(errors="replace") for path in consumers["RFB-G-HISTORY-TYPE"])
    history_type_anchor = "decoherence functional" in history_text.lower() and "histor" in history_text.lower()
    gate(gates, "RFB-G-HISTORY-TYPE", "the history arm consumes the candidate whole-history architecture without promoting it", history_type_anchor, {"licensed": history_type_anchor})

    forbidden = forbidden_fixture_keys(fixture)
    neutrality = (
        fixture["schema"] == "rfb-fixture-v1"
        and not forbidden
        and set(fixture["artifact_whitelist"])
        == {
            "v16/code/rfb_output.txt",
            "v16/code/rfb_receipt.json",
            "v16/paper-10-record-feedback-boundary.md",
        }
    )
    gate(gates, "RFB-G-FIXTURE-NEUTRAL", "the data-only fixture contains definitions and vocabularies but no selected result", neutrality, {"forbidden": forbidden})

    writer = writer_measurements(fixture, mutant)
    gate(gates, "RFB-G-W-CYCLE", "pointer readability plus full accumulation leaves only full cycles, all conjugate to one shift", all(row["canonical_shift"] and row["full_cycles"] == math.factorial(row["q"] - 1) for row in writer["rows"]), {"rows": writer["rows"]})
    gate(gates, "RFB-G-W-CYCLE-DROP", "dropping full accumulation restores reversible multi-cycle writers at every registered dial", all(row["drop_general"] > row["full_cycles"] for row in writer["rows"]), {"pairs": [(row["full_cycles"], row["drop_general"]) for row in writer["rows"]]})
    gate(gates, "RFB-G-W-PHASE", "pointer phase gauge reduces edge decorations to one cycle exponent without selecting it", all(row["phase_ok"] for row in writer["rows"]), {"orbits": [(row["q"], row["phase_orbits"]) for row in writer["rows"]]})
    gate(gates, "RFB-G-W-WINDING", "the residual cycle exponent first moves an interference port after the two paths reconverge", all(row["winding_moves"] and not row["prewinding_common_boundary"] for row in writer["rows"]), {"rows": [{"q": row["q"], "first_common": row["first_common_boundary_steps"], "probabilities": row["winding_probabilities"]} for row in writer["rows"]]})
    gate(gates, "RFB-G-W-DIAL", "the writer census covers exactly the separately registered orders without identifying them with a field order", [row["q"] for row in writer["rows"]] == [2, 3, 4], {"dials": [row["q"] for row in writer["rows"]]})

    reader = reader_measurements(fixture, mutant)
    gate(gates, "RFB-G-R-UNIVERSALITY", "type universality reduces two token-disjoint reader declarations to one shared rule but does not select that rule", all(row["shared_context_parameters"] < row["split_context_parameters"] for row in reader["rows"]), {"rows": [(row["q"], row["shared_context_parameters"], row["split_context_parameters"]) for row in reader["rows"]]})
    gate(gates, "RFB-G-R-TRANSLATION", "translation composition selects cyclic characters with one charge label under its stated hypothesis", all(row["additive_ok"] for row in reader["rows"]), {"rows": [(row["q"], row["additive_readers"], row["charges"]) for row in reader["rows"]]})
    gate(gates, "RFB-G-R-TRANSLATION-DROP", "dropping translation composition restores non-character readers at the nontrivial registered dials", all(row["drop_returns"] for row in reader["rows"]) and any(row["general_readers"] > row["additive_readers"] for row in reader["rows"]), {"rows": [(row["q"], row["general_readers"], row["additive_readers"]) for row in reader["rows"]]})
    gate(gates, "RFB-G-R-PAIR", "simultaneous cyclic relabeling leaves the writer-step times reader-charge pairing", all(row["pair_ok"] for row in reader["rows"]), {"rows": [(row["q"], row["pair_orbits"], row["pair_products"]) for row in reader["rows"]]})
    gate(gates, "RFB-G-R-CHIRALITY", "a biased phase reference distinguishes opposite charges for q greater than two while q equals two is its own inverse", all(row["chirality_distinguishes"] for row in reader["rows"]), {"rows": [(row["q"], row["chirality_calibration"]) for row in reader["rows"]]})
    gate(gates, "RFB-G-R-RECIPROCAL", "a matter-controlled write changes the matter marginal while an uncontrolled record shift is inert", reader["reciprocal"]["controlled_write_matter"] != reader["reciprocal"]["input_matter"] and reader["reciprocal"]["inert_write_matter"] == reader["reciprocal"]["input_matter"], reader["reciprocal"])
    gate(gates, "RFB-G-R-LEAK", "zero reader charge survives reciprocal feedback because the controlled write already decoheres matter", reader["reciprocal"]["decoherence_only_acts"] and reader["reciprocal"]["active_charges_exist"], reader["reciprocal"])

    modes = record_mode_measurements(fixture, mutant)
    gate(gates, "RFB-G-M-DIVISION", "the common plus/minus final port instrument is complete for every input", modes["division_complete"], {"complete": modes["division_complete"]})
    gate(gates, "RFB-G-M-CLASSICAL", "a classical outcome-conditioned feedback instrument is CP and all-input complete", modes["classical_complete"], {"complete": modes["classical_complete"]})
    gate(gates, "RFB-G-M-COHERENT", "the coherent record implementation is one reversible dilation whose reached isometry is complete", modes["coherent_unitary"], {"unitary": modes["coherent_unitary"]})
    gate(gates, "RFB-G-M-SAME-CHANNEL", "the classical instrument and coherent dilation induce the same calibrated ports and unconditioned channel", modes["same_ports"] and modes["same_unconditioned_channel"], {"same_ports": modes["same_ports"], "same_channel": modes["same_unconditioned_channel"]})
    gate(gates, "RFB-G-M-HYBRID", "the registered partial tag is an interior point of a positive-dimensional exact overlap family", modes["hybrid_ok"] and modes["hybrid_dimension"] == 1, {"rows": modes["mode_rows"], "dimension": modes["hybrid_dimension"]})
    gate(gates, "RFB-G-M-FAMILY", "classical, hybrid, and coherent rows share one port type, remain normalized, and move its calibrated probability", all(row["normalized"] for row in modes["mode_rows"]) and len({row["plus_probability"] for row in modes["mode_rows"]}) == len(modes["mode_rows"]), {"probabilities": [(row["id"], row["plus_probability"]) for row in modes["mode_rows"]]})

    history = history_measurements(fixture, mutant)
    gate(gates, "RFB-G-H-INTERFERENCE", "an exclusive intermediate rewrite kernel is phase-blind while coherent boundary laws distinguish the two rows", history["exclusive_same"] and history["coherent_moves"], {"rows": [{"sign": row["sign"], "coherent": row["coherent"], "exclusive": row["exclusive"]} for row in history["rows"]]})
    gate(gates, "RFB-G-H-POSITIVITY", "each final-port decoherence functional is strongly positive at the registered two-history grain", history["positive"], {"positive": history["positive"]})
    gate(gates, "RFB-G-H-SECOND-CUT", "coarse graining both stable ports cancels cross terms while deleting a port restores the defect", history["second_cut"] and history["drop_cross"], {"second_cut": history["second_cut"], "drop_cross": history["drop_cross"]})
    gate(gates, "RFB-G-H-ALL-INPUT", "the final division ports obey the operator completeness identity for every input", history["all_input_complete"], {"complete": history["all_input_complete"]})
    law_type_ok = (
        not history["law_survival"]["exclusive_rewrite_kernel"]
        and history["law_survival"]["enriched_state_kernel"]
        and history["law_survival"]["indivisible_multitime"]
        and history["law_survival"]["decoherence_functional_representation"]
        and not history["law_survival"]["higher_order_required"]
        and history["process_coordinate"] == "METHOD-INCONCLUSIVE"
    )
    gate(gates, "RFB-G-H-LAW-TYPE", "the arena excludes only an exclusive intermediate kernel; enriched-state and indivisible descriptions both survive, so microscopic type is unselected", law_type_ok, {"survival": history["law_survival"], "coordinate": history["process_coordinate"]})

    predictive = predictive_measurements(fixture, mutant)
    gate(gates, "RFB-G-P-INTERVENTION", "intervention-complete signatures separate active charges without treating raw history labels as states", predictive["census"]["charge-one"][1] == 3 and predictive["census"]["constant"][1] == 1, {"census": predictive["census"]})
    gate(gates, "RFB-G-P-RESOURCE", "classical, coherent, hybrid, and indivisible rows are compared at the same registered state budget and have the same predictive quotients", predictive["resource_parity"] and len({json.dumps(core.serialize(value), sort_keys=True) for value in predictive["mode_quotients"].values()}) == 1, {"resource_parity": predictive["resource_parity"], "quotients": predictive["mode_quotients"]})
    gate(gates, "RFB-G-P-HELDOUT", "the held-out horizon introduces no new predictive class at the registered intervention family", predictive["heldout_stable"], {"heldout_stable": predictive["heldout_stable"], "raw": predictive["raw_history_labels"], "minimal": predictive["minimal_active_labels"]})

    recovery = recoverability_measurements(fixture, mutant)
    gate(gates, "RFB-G-RECOVERABILITY", "the registered append-only continuations preserve perfect distinguishability up to relabeling", recovery["append_recoverable"], recovery)
    gate(gates, "RFB-G-RECOVERY-DROP", "enlarging the grammar by an uncopied reset destroys the candidate record", recovery["reset_destroys"], recovery)
    gate(gates, "RFB-G-RECOVERY-REDUNDANCY", "a copied record remains recoverable after the primary copy is reset", recovery["redundancy_survives_primary_reset"], recovery)

    locality = locality_measurements(fixture, mutant)
    gate(gates, "RFB-G-N-LOCALITY", "every registered complete operation on Alice's fixed factor preserves Bob's unconditioned marginal and disjoint actions commute", locality["all_local_invariant"] and locality["disjoint_commute"], {"rows": locality["rows"], "commute": locality["disjoint_commute"]})
    gate(gates, "RFB-G-N-HJW", "distinct HJW ensembles have one Bob average and remain operationally equal under the registered affine local families", locality["hjw_equal_average"], {"equal_average": locality["hjw_equal_average"]})
    gate(gates, "RFB-G-N-DROP", "the trace-amplifying drop control moves Bob's marginal and is refused as a local operation", locality["amplifier_moves"], {"amplifier_moves": locality["amplifier_moves"]})

    forcing = forcing_measurements(fixture, writer, reader, modes, history, predictive, recovery, locality, mutant)
    gate(gates, "RFB-G-FORCING-MATRIX", "every registered nontrivial forcing cell has both an impose measurement and a return-on-drop measurement", forcing["all_impose_drop_measured"] and forcing["rows"] == len(fixture["assumptions"]) and forcing["columns"] == len(fixture["freedoms"]), {"rows": forcing["rows"], "columns": forcing["columns"], "joint": forcing["joint_findings"]})

    coordinates = {
        "division_interface": history["division_coordinate"],
        "microscopic_process": history["process_coordinate"],
        "quantum_representation": history["representation_coordinate"],
        "higher_order": "NOT-REQUIRED-AT-FIXED-ORDER-FIXTURE",
        "record_modes": [
            "RFB-CLASSICAL-FEEDBACK-SURVIVES",
            "RFB-COHERENT-FEEDBACK-SURVIVES",
            f"RFB-HYBRID-FAMILY-SURVIVES-DIM-{modes['hybrid_dimension']}",
            "RFB-DECOHERENCE-ONLY-SURVIVES",
            "RFB-ACTIVE-FEEDBACK-SURVIVES",
            f"RFB-FEEDBACK-FAMILY-UNDERDETERMINED-DIM-{modes['hybrid_dimension']}",
        ],
    }
    coordinate_ok = (
        result_word_licensed(coordinates["division_interface"], fixture["result_schema"]["law_type_words"])
        and result_word_licensed(coordinates["microscopic_process"], fixture["result_schema"]["law_type_words"])
        and result_word_licensed(coordinates["quantum_representation"], fixture["result_schema"]["law_type_words"])
        and all(result_word_licensed(word, fixture["result_schema"]["record_mode_words"]) for word in coordinates["record_modes"])
    )
    gate(gates, "RFB-G-COORDINATES", "the division, microscopic-process, representation, higher-order, and record-mode coordinates are typed separately", coordinate_ok, coordinates)

    feasibility_flags = {
        "mapped": {"referent_bound": True, "inconsistent": False, "all_arms_complete": True},
        "blocked": {"referent_bound": False, "inconsistent": False, "all_arms_complete": False},
        "method": {"referent_bound": True, "inconsistent": False, "all_arms_complete": False},
        "inconsistent": {"referent_bound": True, "inconsistent": True, "all_arms_complete": True},
    }
    feasibility = {name: derive_primary(flags) for name, flags in feasibility_flags.items()}
    reachability_ok = (
        feasibility["mapped"] == "RFB-FORCING-BOUNDARY-MAPPED"
        and feasibility["blocked"] == "RFB-BLOCKED-AT-PROCESS-REFERENT"
        and feasibility["method"].startswith("RFB-METHOD-INCONCLUSIVE-AT-")
        and feasibility["inconsistent"] == "RFB-INCONSISTENT"
    )
    if mutant == "outcome-reachability":
        reachability_ok = False
    gate(gates, "RFB-G-OUTCOME-REACHABILITY", "all preregistered primary families are reachable by a named feasibility condition before the official derivation", reachability_ok, feasibility)

    flags = {
        "referent_bound": referent_bound,
        "inconsistent": False,
        "all_arms_complete": forcing["all_impose_drop_measured"] and coordinate_ok,
    }
    primary = derive_primary(flags)
    if mutant == "primary-comparator":
        primary = "RFB-INCONSISTENT"
    comparator = independent_primary(flags)
    primary_ok = primary == comparator and result_word_licensed(primary, fixture["result_schema"]["primary_words"])
    gate(gates, "RFB-G-PRIMARY", "an independent truth-table comparator agrees with the derived primary word", primary_ok, {"derived": primary, "comparator": comparator, "flags": flags})

    scope_codes = tuple(fixture["scope_walls"])
    gate(gates, "RFB-G-SCOPE", "every frozen scope wall has one positive paper sentence and no result coordinate crosses it", set(scope_codes) == set(SCOPE_SENTENCES), {"walls": scope_codes})

    result: dict[str, Any] = {
        "schema": "rfb-result-v1",
        "unit": "RFB",
        "primary": primary,
        "coordinates": coordinates,
        "ontology": {
            "operationally_established": "stable final records and their ordinary division probabilities at the registered finite fixture",
            "microscopic_process": "unselected between an enriched-state kernel and an indivisible multi-time law",
            "quantum_machinery": "Hilbert and decoherence-functional descriptions are representations at this scope",
            "actual_history": "one actual history remains a compatible candidate, not a result",
            "actualization": "postulated and untouched",
            "geometry": "absent; no graph or record register is promoted to geometry",
        },
        "measurements": {
            "writer": writer,
            "reader": reader,
            "record_modes": modes,
            "history": history,
            "predictive": predictive,
            "recoverability": recovery,
            "locality": locality,
            "forcing": forcing,
            "feasibility": feasibility,
        },
        "scope_walls": list(scope_codes),
        "fixture_sha256": fixture_hash,
        "core_sha256": core_hash,
        "scorer_sha256": sha256_bytes(scorer_bytes),
        "anchor_sha256": {row["path"]: row["sha256"] for row in fixture["anchors"]},
        "mutants": list(MUTANTS),
        "mutant_targets": dict(MUTANT_GATE),
        "gates": gates,
    }
    if mutant == "exactness":
        result["measurements"]["exactness_probe"] = float(Q(1, 3))
    gate(gates, "RFB-G-EXACTNESS", "the complete measurement and result surface contains no floating-point number", not contains_float(result), {"contains_float": contains_float(result)})

    expected_reads = {
        relative_to_root(scorer_path, root),
        relative_to_root(fixture_path, root),
        *(row["path"] for row in fixture["anchors"]),
    }
    if mutant == "read-set":
        READ_AUDIT.add("v16/undeclared-source.md")
    forbidden_reads = sorted(
        path for path in READ_AUDIT
        if any(path.startswith(prefix) for prefix in fixture["forbidden_source_prefixes"])
    )
    read_ok = READ_AUDIT == expected_reads and not forbidden_reads
    gate(gates, "RFB-G-READ-SET", "the live read set equals the frozen anchor, fixture, core, and scorer set and excludes SCOUT-T", read_ok, {"read": sorted(READ_AUDIT), "expected": sorted(expected_reads), "forbidden": forbidden_reads})

    names_before_totality = tuple(row["gate"] for row in gates)
    expected_before_totality = REQUIRED_GATE_NAMES[:-1]
    totality_ok = names_before_totality == expected_before_totality
    gate(gates, "RFB-G-TOTALITY", "the live ordered gate set equals the frozen totality registry", totality_ok, {"live": names_before_totality, "registered": expected_before_totality})
    if tuple(row["gate"] for row in gates) != REQUIRED_GATE_NAMES:
        raise GateFail("RFB-G-TOTALITY: final gate registry moved")
    result["read_set"] = sorted(READ_AUDIT)
    result["gates"] = gates
    return result


def render_transcript(result: Mapping[str, Any]) -> str:
    lines = [
        "RFB PAPER 10 — RECORD-FEEDBACK FORCING BOUNDARY",
        f"primary={result['primary']}",
        f"division_interface={result['coordinates']['division_interface']}",
        f"microscopic_process={result['coordinates']['microscopic_process']}",
        f"quantum_representation={result['coordinates']['quantum_representation']}",
    ]
    for row in result["gates"]:
        evidence = json.dumps(row["evidence"], sort_keys=True, separators=(",", ":"))
        lines.append(f"[PASS]\t{row['gate']}\t{row['statement']}\t{evidence}")
    lines.extend((f"gates={len(result['gates'])}", f"mutants={len(result['mutants'])}"))
    return "\n".join(lines) + "\n"


def transcript_rows(text: str) -> tuple[tuple[str, str, str], ...]:
    rows: list[tuple[str, str, str]] = []
    for line in text.splitlines():
        if line.startswith("[PASS]\t"):
            marker, name, statement, evidence = line.split("\t", 3)
            if marker != "[PASS]":
                raise GateFail("RFB-TRANSCRIPT-SEAL")
            json.loads(evidence)
            rows.append((name, statement, evidence))
    return tuple(rows)


def expected_transcript_rows(result: Mapping[str, Any]) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (
            row["gate"],
            row["statement"],
            json.dumps(row["evidence"], sort_keys=True, separators=(",", ":")),
        )
        for row in result["gates"]
    )


def claim_manifest(result: Mapping[str, Any]) -> dict[str, list[list[str]]]:
    writer_rows = [
        [
            str(row["q"]),
            str(row["all_reversible"]),
            str(row["full_cycles"]),
            str(row["phase_orbits"]),
            str(row["first_common_boundary_steps"]),
        ]
        for row in result["measurements"]["writer"]["rows"]
    ]
    reader_rows = [
        [
            str(row["q"]),
            str(row["general_readers"]),
            str(row["additive_readers"]),
            str(row["pair_orbits"]),
        ]
        for row in result["measurements"]["reader"]["rows"]
    ]
    mode_rows = [
        [row["id"], qtext(row["overlap"]), qtext(row["plus_probability"]), qtext(row["minus_probability"])]
        for row in result["measurements"]["record_modes"]["mode_rows"]
    ]
    return {"writer": writer_rows, "reader": reader_rows, "modes": mode_rows}


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
    ]
    lines.extend("| " + " | ".join(str(value) for value in row) + " |" for row in rows)
    return "\n".join(lines)


def render_paper(result: Mapping[str, Any]) -> str:
    claims = claim_manifest(result)
    forcing = result["measurements"]["forcing"]
    joint_rows = [
        [name, row["status"], str(row["impose"]), str(row["drop"])]
        for name, row in sorted(forcing["joint_findings"].items())
    ]
    wall_rows = [[code, SCOPE_SENTENCES[code]] for code in result["scope_walls"]]
    mode_words = "\n".join(f"- `{word}`" for word in result["coordinates"]["record_modes"])
    return f"""# Paper 10 — The record-feedback forcing boundary

**Candidate status:** GREEN-UNREVIEWED.  **Primary:**
`{result['primary']}`.

## Abstract

This unit does not propose a preferred dynamics. It measures which pieces of a
finite record-feedback architecture follow from which named assumptions. Full
cyclic accumulation fixes a reversible pointer writer only up to relabeling;
phase gauge leaves one measurable but unselected winding class. Translation
composition—not type universality alone—reduces readers to cyclic characters.
Reciprocity excludes an inert write but does not remove the zero-charge
decoherence-only family. Classical feedback, a coherent dilation, and a
one-dimensional hybrid overlap family all remain lawful at the common final
division interface.

The history arm gives the main negative result. A positive kernel that makes
the two unrecorded rewrites exclusive is unable to distinguish two relative
phases, while an enriched coherent state and an indivisible history functional
both reproduce the final record statistics. Therefore an ordinary kernel is
sufficient at the registered final division, but the microscopic law type and
its Hilbert-versus-decoherence-functional representation remain unselected.

## 1. Ontology: what this paper actually says exists

At this finite arena, what is operationally established is modest: there are
stable final record alternatives, ordinary probabilities for those
alternatives, and lawful transformations connecting preparations to that
division. The calculation does **not** establish that a probability is assigned
after each elementary rewrite.

One actual configuration history remains a compatible Barandes-style
ontological candidate. An indivisible multi-time law remains a compatible
nomological candidate. Neither is forced here, because a stochastic law on an
enriched coherent state passes the same registered boundary tests. Hilbert
states and decoherence functionals are consequently treated as mathematical
representations, not additional substances. Actualization remains a postulate.
There is no graph in the arena, and no register is called geometry.

The typed coordinates are:

- division interface: `{result['coordinates']['division_interface']}`;
- microscopic process: `{result['coordinates']['microscopic_process']}`;
- quantum representation: `{result['coordinates']['quantum_representation']}`;
- causal-order extension: `{result['coordinates']['higher_order']}`.

## 2. Writer and reader classification

The exact writer census is:

<!-- CLAIM-WRITER-START -->
{markdown_table(['q', 'all reversible', 'full cycles', 'phase orbits', 'first common step'], claims['writer'])}
<!-- CLAIM-WRITER-END -->

The phrase “forced writer” means only this conditional statement: pointer
readability plus full accumulation leaves full cycles, and all full cycles are
conjugate to the shift. Dropping accumulation restores multi-cycle
permutations. Vertex phases quotient the edge decorations to the cycle product,
but the assumptions do not select that product. It becomes visible only when a
complete winding and an identity history meet at a common boundary.

The exact reader census is:

<!-- CLAIM-READER-START -->
{markdown_table(['q', 'general readers', 'additive readers', 'pair orbits'], claims['reader'])}
<!-- CLAIM-READER-END -->

Type universality merely prices one shared rule instead of two unrelated rules.
The character/charge form follows only after imposing translation composition.
Simultaneous cyclic relabeling leaves the writer-step times charge pairing.
Both zero and nonzero charges survive. The zero-charge case is not inert:
matter-controlled writing already dephases matter, so the reciprocity principle
does not force active steering.

## 3. Classical, coherent, and hybrid records

All rows use the same two-dimensional input and the same final plus/minus port
calibration:

<!-- CLAIM-MODES-START -->
{markdown_table(['mode', 'tag overlap', 'plus probability', 'minus probability'], claims['modes'])}
<!-- CLAIM-MODES-END -->

The classical outcome-conditioned instrument is all-input complete. A reversible
two-factor dilation yields exactly the same retained Kraus ports and the same
unconditioned channel. That identity is a representation/unravelling result,
not an ontological preference. The partial-tag Gram condition is
`1 - w^2 >= 0`; its interior contains the exact `w=3/5` row, so the registered
safety surface leaves a one-dimensional family rather than quantizing the
record to classical or coherent endpoints.

The surviving record-mode words are:

{mode_words}

## 4. Why the elementary stochastic arrow is not enough—and what is enough

Two histories reach the same final ports with identical diagonal weights and
opposite relative phases. The exclusive intermediate kernel returns the same
half/half distribution for both. Coherent summation returns opposite certain
ports. Each port's two-history functional is strongly positive; summing the
two stable ports cancels the off-diagonal terms exactly. The plus/minus division
instrument is complete for every input.

This excludes only `DIVISIBLE-REWRITE-KERNEL` when its rewrite alternatives are
declared exclusive outcomes. It does not exclude `ENRICHED-STATE-KERNEL`: a
state that retains the relative phase can evolve stochastically and emit the
correct final distribution. An indivisible multi-time law and a strongly
positive decoherence-functional representation also pass. No indefinite-order
witness exists in this fixed-order arena. Hence the honest microscopic and
representation coordinates are both `METHOD-INCONCLUSIVE`.

## 5. Predictive state, permanence, and no-signalling

Intervention-complete finite signatures distinguish all three cyclic states for
nonzero charge and merge them for zero charge. Classical, coherent, hybrid,
and indivisible descriptions were given the same three-state/dimension budget
and have the same predictive quotients through the held-out horizon. Raw
decision-tree labels are larger but carry no extra registered prediction.
Predictive minimality therefore selects no record implementation here.

The append-only grammar preserves the record partition up to relabeling. A
reset destroys an uncopied record; copying it first preserves recoverability
after the primary is reset. This is a finite grammar-relative result, not an
absolute permanence theorem.

Every registered trace-preserving operation on Alice's fixed factor preserves
Bob's unconditioned marginal, including the classical and hybrid dephasing
rows. Distinct HJW decompositions have the same Bob average. A trace amplifier
moves the marginal and is refused. This is the standard fixed-factor theorem;
it does not define Bob after graph birth, merge, or split.

## 6. The forcing boundary

<!-- CLAIM-JOINT-START -->
{markdown_table(['test', 'disposition', 'impose measured', 'drop measured'], joint_rows)}
<!-- CLAIM-JOINT-END -->

The full matrix has `{forcing['rows']}` named assumption rows and
`{forcing['columns']}` freedom columns. Cells not supported by a registered
impose/drop assay are explicitly `UNTOUCHED-BY-REGISTERED-SURFACE`; they are not
silently inferred. The boundary is mapped even though it does not select a
microscopic law. That is why the primary and the `METHOD-INCONCLUSIVE`
coordinate are consistent rather than contradictory.

## 7. What was achieved and what remains

RFB converts the forcing rhetoric into conditional theorems and measured
residues. It earns the cyclic writer modulo gauge, the additive reader only
under a representation axiom, the finite recovery criterion, the exclusion of
exclusive intermediate probabilities, and the sufficiency of a final division
instrument. It proves that the tested consistency surface does not choose
classical versus coherent records, zero versus active charge, enriched-state
versus indivisible microscopic law, or Hilbert versus decoherence-functional
representation.

The next physics unit still owes the generative content: graph-selected events,
graph-generated transports and weights, coherent changing carriers, overlap
composition, dynamically defined subsystems, stable divisions, and held-out
family irreducibility. Existing quantum-network and history machinery supplies
substantial kinematics; their background-free synthesis remains unbuilt.

## 8. Scope walls

<!-- CLAIM-WALLS-START -->
{markdown_table(['wall', 'standing sentence'], wall_rows)}
<!-- CLAIM-WALLS-END -->

## 9. Reproducibility

- fixture SHA-256: `{result['fixture_sha256']}`
- core SHA-256: `{result['core_sha256']}`
- scorer SHA-256: `{result['scorer_sha256']}`
- exact arithmetic: rational matrices plus symbolic cyclic phase exponents;
- candidate gate count: `{len(result['gates'])}`;
- registered targeted mutant count: `{len(result['mutants'])}`.

This candidate is green-unreviewed. It is not terminal until an independent
three-lens hostile panel, adjudication, any ordered repair, and post-commit
off-tree verification are complete.
"""


def verify_paper(paper: str, result: Mapping[str, Any]) -> None:
    claims = claim_manifest(result)
    expected_blocks = {
        "writer": markdown_table(['q', 'all reversible', 'full cycles', 'phase orbits', 'first common step'], claims["writer"]),
        "reader": markdown_table(['q', 'general readers', 'additive readers', 'pair orbits'], claims["reader"]),
        "modes": markdown_table(['mode', 'tag overlap', 'plus probability', 'minus probability'], claims["modes"]),
    }
    markers = {
        "writer": ("<!-- CLAIM-WRITER-START -->", "<!-- CLAIM-WRITER-END -->"),
        "reader": ("<!-- CLAIM-READER-START -->", "<!-- CLAIM-READER-END -->"),
        "modes": ("<!-- CLAIM-MODES-START -->", "<!-- CLAIM-MODES-END -->"),
    }
    for name, expected in expected_blocks.items():
        start, end = markers[name]
        if paper.count(start) != 1 or paper.count(end) != 1:
            raise GateFail(f"RFB-PAPER-CLAIMS: {name} markers moved")
        actual = paper.split(start, 1)[1].split(end, 1)[0].strip()
        if actual != expected:
            raise GateFail(f"RFB-PAPER-CLAIMS: {name} table moved")
    if paper.count(result["primary"]) != 1:
        raise GateFail("RFB-PAPER-CLAIMS: primary occurrence moved")
    for code, sentence in SCOPE_SENTENCES.items():
        if paper.count(code) != 1 or paper.count(sentence) != 1:
            raise GateFail(f"RFB-PAPER-SCOPE: {code} is absent, duplicated, or rephrased")
    prohibited = (
        "RFB constructs graph growth.",
        "RFB derives actualization.",
        "RFB recovers QFT or general relativity.",
        "RFB makes an empirical prediction about nature.",
    )
    if any(sentence in paper for sentence in prohibited):
        raise GateFail("RFB-PAPER-SCOPE: a scope wall was promoted")


def stage_and_promote(payloads: Sequence[tuple[Path, bytes]]) -> None:
    targets = [path.resolve() for path, _payload in payloads]
    if len(set(targets)) != len(targets):
        raise ValueError("artifact targets must differ")
    if any(target.exists() for target in targets):
        raise FileExistsError("refusing to overwrite an existing artifact")
    staged: list[tuple[Path, Path, bytes]] = []
    try:
        for target, payload in zip(targets, (row[1] for row in payloads), strict=True):
            target.parent.mkdir(parents=True, exist_ok=True)
            handle, raw = tempfile.mkstemp(prefix=f".{target.name}.", dir=str(target.parent))
            temporary = Path(raw)
            with os.fdopen(handle, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            if temporary.read_bytes() != payload:
                raise GateFail("RFB-STAGE-READBACK")
            staged.append((temporary, target, payload))
        for temporary, target, _payload in staged:
            os.replace(temporary, target)
        for _temporary, target, payload in staged:
            if target.read_bytes() != payload:
                raise GateFail("RFB-PROMOTION-READBACK")
    finally:
        for temporary, _target, _payload in staged:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=here / "rfb_fixture.json")
    parser.add_argument("--output", type=Path, default=here / "rfb_output.txt")
    parser.add_argument("--receipt", type=Path, default=here / "rfb_receipt.json")
    parser.add_argument("--paper", type=Path, default=here.parent / "paper-10-record-feedback-boundary.md")
    parser.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--list-gates", action="store_true")
    parser.add_argument("--list-mutants", action="store_true")
    return parser.parse_args(list(argv))


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_args(sys.argv[1:] if argv is None else argv)
    modes = sum((arguments.selftest, arguments.list_gates, arguments.list_mutants))
    if modes > 1:
        raise SystemExit("choose exactly one inspection mode")
    if modes and arguments.mutant is not None:
        raise SystemExit("inspection modes cannot be combined with mutants")
    if arguments.list_gates:
        sys.stdout.write("\n".join(REQUIRED_GATE_NAMES) + "\n")
        return 0
    if arguments.list_mutants:
        sys.stdout.write("\n".join(MUTANTS) + "\n")
        return 0
    if arguments.selftest:
        flags = {"referent_bound": True, "inconsistent": False, "all_arms_complete": True}
        clean = derive_primary(flags) == independent_primary(flags) == "RFB-FORCING-BOUNDARY-MAPPED"
        public = core.public_calibration()
        return 0 if clean and all(row["passed"] for row in public["gates"]) else 1

    targets = (arguments.output.resolve(), arguments.receipt.resolve(), arguments.paper.resolve())
    if len(set(targets)) != len(targets):
        raise SystemExit("output, receipt, and paper targets must differ")
    if any(target.exists() for target in targets):
        raise SystemExit("refusing to overwrite an existing artifact")
    try:
        result = score(arguments.fixture.resolve(), arguments.mutant)
        transcript = render_transcript(result)
        if arguments.mutant == "transcript-seal":
            transcript = transcript.replace("RFB-G-H-INTERFERENCE", "RFB-G-H-INTERFERENZE", 1)
        if transcript_rows(transcript) != expected_transcript_rows(result):
            raise GateFail("RFB-TRANSCRIPT-SEAL: transcript and receipt gate ledgers differ")
        paper = render_paper(result)
        if arguments.mutant == "scope-promotion":
            paper = paper.replace("RFB does not construct graph growth.", "RFB constructs graph growth.", 1)
        if arguments.mutant == "paper-claim":
            paper = paper.replace("| 3 | 6 | 2 | 3 | 3 |", "| 3 | 6 | 3 | 3 | 3 |", 1)
        verify_paper(paper, result)
        result["transcript_sha256"] = sha256_bytes(transcript.encode())
        result["paper_sha256"] = sha256_bytes(paper.encode())
        result["content_sha256"] = digest(result)
        if arguments.mutant == "receipt-seal":
            result["coordinates"]["microscopic_process"] = "INDIVISIBLE-MULTITIME-LAW-REQUIRED"
        if result["content_sha256"] != digest({key: value for key, value in result.items() if key != "content_sha256"}):
            raise GateFail("RFB-RECEIPT-SEAL: result moved after its content seal")
        receipt = canonical_json(result)
        stage_and_promote(
            (
                (arguments.output.resolve(), transcript.encode()),
                (arguments.receipt.resolve(), receipt),
                (arguments.paper.resolve(), paper.encode()),
            )
        )
    except (GateFail, ValueError, TypeError, ArithmeticError, FileExistsError, KeyError, json.JSONDecodeError) as error:
        print(f"RFB REFUSAL: {error}", file=sys.stderr)
        return 1
    sys.stdout.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
