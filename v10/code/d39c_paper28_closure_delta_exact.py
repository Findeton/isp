#!/usr/bin/env python3
"""D39c focused exact delta for Paper 28 hostile round one.

This receipt does not replace D39b.  It locks the closing-reviewed D39b source
and output, imports its exact finite objects, and gates the four theorem
stitches required by Paper 28's independent review:

* a declared generated-row constructor for D38b kernel outcomes;
* H1 invariance under projection to the touched-wire verification ledger;
* inclusion and dimension of the action-coboundary quotient; and
* the retained-through-R complete summable-tail identity.

All theorem arithmetic is integer/Fraction exact.
"""

from __future__ import annotations

import hashlib
import json
import runpy
from fractions import Fraction
from pathlib import Path
from typing import Dict, Hashable, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[1]
D39B_SOURCE = ROOT / "code" / "d39b_record_closed_law_selection_exact.py"
D39B_OUTPUT = ROOT / "data" / "d39b_record_closed_law_selection_exact.out"

D39B_SOURCE_SHA256 = "22fbda6a9189a2f46cf64c0f33b943b952e702fce30828a37b6d462f5a1458d3"
D39B_OUTPUT_SHA256 = "3e3ec1b1ab0459bddc5106e1ba4fe459741af264bfb0c725c8d9edd41ddf85ea"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable(value: object) -> str:
    def encode(item: object):
        if isinstance(item, Fraction):
            return {"fraction": [item.numerator, item.denominator]}
        if isinstance(item, Path):
            return str(item)
        if isinstance(item, (tuple, list)):
            return [encode(child) for child in item]
        if isinstance(item, (set, frozenset)):
            return sorted((encode(child) for child in item), key=repr)
        if isinstance(item, dict):
            return {
                str(key): encode(child)
                for key, child in sorted(item.items(), key=lambda pair: repr(pair[0]))
            }
        return item

    return json.dumps(encode(value), sort_keys=True, separators=(",", ":"))


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


B = runpy.run_path(str(D39B_SOURCE))
d38 = B["d38"]


# ---------------------------------------------------------------------------
# C1: D38b kernel outcomes inhabit a declared generated-row sum type.


GeneratedRow = Tuple[str, str]


def action_generated_row(action: Tuple[str, str]) -> GeneratedRow:
    tag, target = action
    if not tag or not target:
        raise AssertionError("empty action-generated row")
    return f"D38_ACTION:{tag}", target


def push_with_constructor(
    law: Mapping[Tuple[Tuple[str, str], ...], Fraction]
) -> Dict[Tuple[GeneratedRow, ...], Fraction]:
    answer: Dict[Tuple[GeneratedRow, ...], Fraction] = {}
    for path, probability in law.items():
        image = tuple(action_generated_row(action) for action in path)
        answer[image] = answer.get(image, Fraction()) + probability
    return answer


def generated_row_checks() -> Tuple[int, int, int, int]:
    laws = prefixes = atoms = typed = 0
    for star in d38.reachable_stars():
        pushed = {}
        for depth in (1, 2, 3):
            source = d38.cylinder_distribution(star, depth)
            image = push_with_constructor(source)
            if image != B["push_cylinder"](source):
                raise AssertionError("constructor push differs from D39b")
            if sum(image.values(), Fraction()) != 1 or any(value <= 0 for value in image.values()):
                raise AssertionError("improper generated-row law")
            typed += sum(
                int(all(len(row) == 2 and row[0].startswith("D38_ACTION:") for row in path))
                for path in image
            )
            atoms += len(image)
            laws += 1
            pushed[depth] = image
        for high, low in ((3, 2), (2, 1), (3, 1)):
            if B["prefix_law"](pushed[high], low) != pushed[low]:
                raise AssertionError("generated-row prefix")
            prefixes += 1
    return laws, prefixes, atoms, typed


# ---------------------------------------------------------------------------
# C2: H1 verification on the touched-wire projection.


def touched_ledger(store, event):
    derived = d38.derive(store.history)
    rows = derived.row_map()
    heads = derived.head_map()
    required = B["required_wires"](event)
    edges: Tuple[Tuple[str, str], ...] = ()
    payload = event.payload_map()
    if payload["event_kind"] == "INTERACTION":
        edges = (tuple(sorted((str(payload["initiator"]), str(payload["target"])))),)
    return B["LocalLedger"](
        tuple(sorted((wire, B["row_tuple"](rows[wire])) for wire in required)),
        tuple(sorted((wire, heads[wire]) for wire in required)),
        edges,
        tuple((edge, B["edge_source"](store.history, edge)) for edge in edges),
        (),
        (),
        frozenset(),
    )


def projected_successor(store, event, preledger):
    after, accepted = d38.transact(store, event)
    if not accepted:
        raise AssertionError("registered oracle rejection")
    derived = d38.derive(after.history)
    actors = set(B["required_wires"](event))
    actors.update(str(actor) for actor, _row in event.payload_map()["post_rows"])
    edges = set(preledger.edges)
    sources = dict(preledger.edge_sources)
    if event.payload_map()["event_kind"] == "BIRTH":
        edge = tuple(event.payload_map()["created_edge"])
        edges.add(edge)
        sources[edge] = event.record_id
    return (
        tuple(sorted((actor, B["row_tuple"](derived.row_map()[actor])) for actor in actors)),
        tuple(sorted((actor, derived.head_map()[actor]) for actor in actors)),
        tuple(sorted(edges)),
        tuple(sorted(sources.items(), key=repr)),
    )


def touched_projection_checks() -> Tuple[int, int, int, int, int, int]:
    proposals = collected = certificate_equal = validated = successors = 0
    maximum_existing_wires = 0
    for store in B["registered_stores"](2):
        for event in B["valid_events"](store):
            proposals += 1
            projected = touched_ledger(store, event)
            maximum_existing_wires = max(maximum_existing_wires, len(projected.rows))
            locked, certificate, ok = B["collect_h1"](projected, event)
            collected += int(ok and certificate is not None)
            if not ok or certificate is None:
                raise AssertionError("projected collection")

            full = B["ledger_from_store"](store)
            _full_locked, full_certificate, full_ok = B["collect_h1"](full, event)
            certificate_equal += int(full_ok and certificate == full_certificate)

            after, admitted = B["commit_h1"](locked, certificate)
            if not admitted:
                raise AssertionError("projected admission")
            validated += int(B["protocol_history_valid"](after))
            actual = B["ledger_state"](after)
            successors += int(actual == projected_successor(store, event, projected))
    return proposals, collected, certificate_equal, validated, successors, maximum_existing_wires


# ---------------------------------------------------------------------------
# C3: exact coboundary inclusion and one-dimensional quotient.


def action_quotient_checks() -> Tuple[int, int, int, int, int, int, int, int]:
    variables, symbolic_rows, _squares, states, transitions = B["finite_action_complex"]()
    variable_index = {variable: index for index, variable in enumerate(variables)}
    state_index = {state: index for index, state in enumerate(states)}

    matrix = []
    for row in symbolic_rows:
        vector = [Fraction() for _ in variables]
        for variable, coefficient in row:
            vector[variable_index[variable]] = Fraction(coefficient)
        matrix.append(tuple(vector))

    coboundaries = []
    for state in states:
        vector = [Fraction() for _ in variables]
        for variable, source, target in transitions:
            vector[variable_index[variable]] += Fraction(int(target == state) - int(source == state))
        coboundaries.append(tuple(vector))

    inclusion = sum(
        int(all(sum((row[i] * vector[i] for i in range(len(variables))), Fraction()) == 0 for row in matrix))
        for vector in coboundaries
    )
    matrix_rank = B["rational_rank"](matrix)
    kernel_dimension = len(variables) - matrix_rank
    coboundary_rank = B["rational_rank"](coboundaries)
    components = len(states) - coboundary_rank
    quotient_dimension = kernel_dimension - coboundary_rank
    return (
        len(states),
        len(variables),
        matrix_rank,
        kernel_dimension,
        coboundary_rank,
        inclusion,
        components,
        quotient_dimension,
    )


# ---------------------------------------------------------------------------
# C4: retained-through-R exact complete-tail control.


def complete_tail_checks() -> Tuple[object, ...]:
    responses = tuple(B["responses"](state) for state in B["ACTIVE_PREPARATIONS"])
    max_distance = max(
        max(abs(responses[i][query] - responses[j][query]) for query in (0, 1))
        for i in range(len(responses))
        for j in range(i + 1, len(responses))
    )
    epsilon = Fraction(1, 64)

    # If shells through R are retained, the omitted summable family is
    # sum_{r>R} 2^r 4^-r = sum_{r>R} 2^-r = 2^-R.
    geometric_identities = 0
    for radius in range(13):
        for finite_terms in range(1, 13):
            partial = sum(
                (Fraction(2**r, 4**r) for r in range(radius + 1, radius + finite_terms + 1)),
                Fraction(),
            )
            remainder = Fraction(1, 2 ** (radius + finite_terms))
            geometric_identities += int(partial + remainder == Fraction(1, 2**radius))

    def summable_tail(radius: int) -> Fraction:
        return max_distance * Fraction(1, 2**radius)

    cutoff = next(radius for radius in range(20) if summable_tail(radius) <= epsilon)
    minimal = int(cutoff == 0 or summable_tail(cutoff - 1) > epsilon)
    nonsummable = sum(
        int(max_distance * Fraction(2**radius, 2**radius) > epsilon)
        for radius in range(1, 13)
    )
    return max_distance, epsilon, geometric_identities, cutoff, minimal, nonsummable


def main() -> None:
    out = []
    gates: Dict[str, bool] = {}
    science: Dict[str, object] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D39c Paper 28 hostile-round closure delta]")
    emit("ARITHMETIC: integer/Fraction exact; no floating theorem")
    locks = (sha256(D39B_SOURCE), sha256(D39B_OUTPUT))
    gates["C0"] = locks == (D39B_SOURCE_SHA256, D39B_OUTPUT_SHA256)
    science["locks"] = locks
    emit(f"D39b_source_sha256={locks[0]}")
    emit(f"D39b_complete_output_sha256={locks[1]}")

    rows = generated_row_checks()
    gates["C1"] = rows == (12, 12, 1760, 1760)
    science["generated_rows"] = rows
    emit("[DECLARED D38b KERNEL-OUTCOME GENERATED ROWS]")
    emit(f"pushed_laws={rows[0]}/12; prefix_rows={rows[1]}/12; aggregate_positive_atoms={rows[2]}; typed_atoms={rows[3]}/{rows[2]}")
    emit("generated_row_sum_type=D38_RECORD|D38_ACTION; conditional_equivalence=NOT_INFERRED")

    projection = touched_projection_checks()
    gates["C2"] = projection == (410, 410, 410, 410, 410, 2)
    science["projection"] = projection
    emit("[H1 TOUCHED-WIRE PROJECTION INVARIANCE]")
    emit(f"proposals={projection[0]}; collections={projection[1]}/{projection[0]}; full_vs_projected_certificates={projection[2]}/{projection[0]}")
    emit(f"causal_validations={projection[3]}/{projection[0]}; projected_successor_matches={projection[4]}/{projection[0]}; maximum_existing_touched_wires={projection[5]}")
    emit("scope=EXHAUSTED_DEPTH_0_TO_2_REGISTRY; asynchronous_liveness_and_all_history_induction=OPEN")

    quotient = action_quotient_checks()
    gates["C3"] = quotient == (155, 401, 246, 155, 154, 155, 1, 1)
    science["quotient"] = quotient
    emit("[ACTION COBOUNDARY INCLUSION / ALGEBRAIC QUOTIENT]")
    emit(f"states={quotient[0]}; variables={quotient[1]}; cocycle_rank={quotient[2]}; kernel_dimension={quotient[3]}")
    emit(f"coboundary_rank={quotient[4]}; included_basis_columns={quotient[5]}/{quotient[0]}; transition_components={quotient[6]}; quotient_dimension={quotient[7]}")
    emit("endpoint_potential_observational_gauge=BRIDGE_DEPENDENT; physical_equivalence=NOT_INFERRED")

    tail = complete_tail_checks()
    gates["C4"] = tail == (Fraction(1), Fraction(1, 64), 156, 6, 1, 12)
    science["tail"] = tail
    emit("[RETAINED-THROUGH-R COMPLETE TAIL]")
    emit(f"maximum_response_distance={ftext(tail[0])}; epsilon={ftext(tail[1])}; exact_geometric_identities={tail[2]}/156")
    emit(f"sum_r_gt_R_of_2^r*4^-r=2^-R; least_cutoff={tail[3]}; minimal={tail[4]}/1; nonsummable_shells={tail[5]}/12")

    source_hash = sha256(Path(__file__))
    body_hash = hashlib.sha256(("\n".join(out) + "\n").encode()).hexdigest()
    science_hash = hashlib.sha256(stable(science).encode()).hexdigest()
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")
    emit("[GATES]")
    for name in sorted(gates):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    passed = sum(gates.values())
    emit("[VERDICT]")
    emit(f"{'PASS' if passed == len(gates) else 'FAIL'} {passed}/{len(gates)}")
    emit("FINITE TOUCHED-WIRE H1 PROJECTION THEOREM / ONE-DIMENSIONAL ALGEBRAIC ACTION-COCYCLE QUOTIENT")
    emit("conditional equivalence, all-history locality, physical endpoint gauge and infinite completion remain open")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
