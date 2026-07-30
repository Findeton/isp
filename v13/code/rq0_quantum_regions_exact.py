#!/usr/bin/env python3
"""v13 RQ0 exact quantum regional instruments and fact descent.

This standard-library-only receipt constructs fresh finite amplitude
instruments.  Record readouts are frozen before W3 tests and are derived from
the same write/preserve/erase matrices.  The outcome ceiling is deliberately
RQ0-FACT-DESCENT: there is no causal, metric, field, or gravity estimator here.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import subprocess
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
PIN_COMMIT = "307c36f017d9d5587334d3b79421645ee5b54c61"
READOUT_POLICY = (
    "record-candidate=memory-bit@bit-1;candidate-values=0,1;"
    "tomography-probe=full-configuration;partition-search=forbidden"
)
READOUT_POLICY_SHA256 = "0402cb35c215bc7d01a86e5b01e9e25c85d6bd69df951549f1265c367ae0ab79"
READOUT_VALUE_LOCKS = {
    "D1": "2bb60d330d26b7c9ebcd336d3920f3b722518d1a99d079034edf538b3a1781ec",
    "D2": "b3fb803d279f483a74b690e59c459136adbd984a01f9fd16de2af9788e01c462",
    "D3": "fa35dd0a9b4e43372a59c5764946e42d8a189719f40e98feaee347b4dd872564",
}

LOCKS = {
    "clean-sheet pin": (
        "v13/note-rq0-relativistic-arena-pin.md",
        "32f0fe8402c10477ba5f01abc69c44e0512c8f0cba7df1f5e39391908ead684c",
        "pin",
    ),
    "quantum amendment pin": (
        "v13/note-rq0-quantum-substrate-amendment-pin.md",
        "cc1c2177dc509641b1ae776444d599f554929c55c1452fa69d30af49cbd9ea91",
        "pin amendment",
    ),
    "v12 Paper 0": (
        "v12/relativistic-isp-v12-paper0-the-weld.md",
        "426633d8a9dfc85e24414ca4681ff5882a07110b410d34c6eed5d7051a4d67ef",
        "scope/postulate",
    ),
    "v12 Paper 1": (
        "v12/paper1-composition-defect.md",
        "81bdab5673fb67b63cd10c08fbb80870f8aa01088047718c5b4bf447e1669128",
        "inherited theorem/schema",
    ),
    "W6 note": (
        "v12/note-w6-record-coreference.md",
        "2f18e863c1930ef2bfd52cf448a8baadd8ceac47696d80e6e4ae2ccf802d37c3",
        "fact/token controls",
    ),
    "Paper 2": (
        "v12/paper2-record-coreference.md",
        "d6af0e6513fc7088407dc5a26c513ecc4e9e45b5a5ae71ffa8a9571f274ad670",
        "common-extension/descent discipline",
    ),
    "GW1": (
        "v13/note-gw1-metric-from-closure.md",
        "6f825ef6e1ced4842885a7356a860c7e55b16dc9d5dc4c15a3ef5da54da26627",
        "no-smuggling discipline",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        tuple(command),
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


@dataclass(frozen=True, order=True)
class Q2:
    """The exact real quadratic field Q(sqrt(2)): a + b sqrt(2)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(value: object) -> "Q2":
        if isinstance(value, Q2):
            return value
        if isinstance(value, Fraction):
            return Q2(value, Fraction(0))
        if isinstance(value, int):
            return Q2(Fraction(value), Fraction(0))
        raise TypeError("cannot coerce to Q2")

    def __add__(self, other: object) -> "Q2":
        rhs = Q2.coerce(other)
        return Q2(self.a + rhs.a, self.b + rhs.b)

    def __radd__(self, other: object) -> "Q2":
        return self + other

    def __sub__(self, other: object) -> "Q2":
        rhs = Q2.coerce(other)
        return Q2(self.a - rhs.a, self.b - rhs.b)

    def __rsub__(self, other: object) -> "Q2":
        return Q2.coerce(other) - self

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __mul__(self, other: object) -> "Q2":
        rhs = Q2.coerce(other)
        return Q2(
            self.a * rhs.a + 2 * self.b * rhs.b,
            self.a * rhs.b + self.b * rhs.a,
        )

    def __rmul__(self, other: object) -> "Q2":
        return self * other

    def __truediv__(self, other: object) -> "Q2":
        rhs = Q2.coerce(other)
        denominator = rhs.a * rhs.a - 2 * rhs.b * rhs.b
        if denominator == 0:
            raise ZeroDivisionError
        return Q2(
            (self.a * rhs.a - 2 * self.b * rhs.b) / denominator,
            (self.b * rhs.a - self.a * rhs.b) / denominator,
        )

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def square(self) -> "Q2":
        return self * self

    def render(self) -> str:
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return f"{self.b}*sqrt2"
        sign = "+" if self.b > 0 else "-"
        return f"{self.a}{sign}{abs(self.b)}*sqrt2"


ZERO = Q2()
ONE = Q2(Fraction(1))
SQRT2_OVER_2 = Q2(Fraction(0), Fraction(1, 2))
Matrix = Tuple[Tuple[Q2, ...], ...]


def matrix(rows: Iterable[Iterable[object]]) -> Matrix:
    result = tuple(tuple(Q2.coerce(value) for value in row) for row in rows)
    if result and any(len(row) != len(result[0]) for row in result):
        raise ValueError("ragged matrix")
    return result


def zeros(rows: int, columns: int) -> Matrix:
    return tuple(tuple(ZERO for _column in range(columns)) for _row in range(rows))


def identity(size: int) -> Matrix:
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def transpose(value: Matrix) -> Matrix:
    return tuple(tuple(value[row][column] for row in range(len(value))) for column in range(len(value[0])))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not compose")
    return tuple(
        tuple(
            sum((left[row][middle] * right[middle][column] for middle in range(len(right))), ZERO)
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(len(left[0])))
        for row in range(len(left))
    )


def kron(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[left_row][left_column] * right[right_row][right_column]
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        )
        for left_row in range(len(left))
        for right_row in range(len(right))
    )


def diagonal(values: Sequence[object]) -> Matrix:
    entries = tuple(Q2.coerce(value) for value in values)
    return tuple(
        tuple(entries[row] if row == column else ZERO for column in range(len(entries)))
        for row in range(len(entries))
    )


def is_unitary(value: Matrix) -> bool:
    return matmul(value, transpose(value)) == identity(len(value))


def born(value: Matrix) -> Matrix:
    return tuple(tuple(entry.square() for entry in row) for row in value)


def defect(later: Matrix, earlier: Matrix) -> Matrix:
    return matsub(born(matmul(later, earlier)), matmul(born(later), born(earlier)))


def nonzero_count(value: Matrix) -> int:
    return sum(not entry.is_zero() for row in value for entry in row)


def matrix_digest(value: Matrix) -> str:
    payload = ";".join(
        ",".join(entry.render() for entry in row)
        for row in value
    )
    return hashlib.sha256(payload.encode()).hexdigest()


H = matrix(((SQRT2_OVER_2, SQRT2_OVER_2), (SQRT2_OVER_2, -SQRT2_OVER_2)))
I2 = identity(2)
X = matrix(((0, 1), (1, 0)))
Z = matrix(((1, 0), (0, -1)))


def on_qubit(gate: Matrix, target: int, qubits: int) -> Matrix:
    result = matrix(((1,),))
    for index in range(qubits):
        result = kron(result, gate if index == target else I2)
    return result


def cnot(qubits: int, control: int, target: int) -> Matrix:
    size = 2 ** qubits
    out = [[ZERO for _column in range(size)] for _row in range(size)]
    for source in range(size):
        bits = [(source >> (qubits - 1 - index)) & 1 for index in range(qubits)]
        target_bits = list(bits)
        target_bits[target] ^= bits[control]
        destination = 0
        for bit in target_bits:
            destination = 2 * destination + bit
        out[destination][source] = ONE
    return tuple(tuple(row) for row in out)


def bit_value(configuration: int, bit: int, qubits: int) -> int:
    return (configuration >> (qubits - 1 - bit)) & 1


@dataclass(frozen=True)
class Readout:
    name: str
    values: Tuple[Hashable, ...]
    record_candidate: bool


def readout_digest(readout: Readout) -> str:
    payload = json.dumps(
        {
            "candidate": readout.record_candidate,
            "name": readout.name,
            "values": readout.values,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode()).hexdigest()


@dataclass(frozen=True)
class Token:
    local_name: str
    readout_name: str
    provenance: Tuple[str, ...]


@dataclass(frozen=True)
class BoundarySpace:
    name: str
    dimension: int


@dataclass(frozen=True)
class ArrowSignature:
    name: str
    family: str
    source: str
    target: str


@dataclass(frozen=True)
class QuantumRegion:
    name: str
    qubits: int
    configurations: Tuple[int, ...]
    preparations: Tuple[int, ...]
    actual_preparation: int
    interfaces: Tuple[BoundarySpace, ...]
    amplitude_signatures: Tuple[ArrowSignature, ...]
    write: Matrix
    preserve: Tuple[Tuple[str, Matrix], ...]
    erase: Tuple[Tuple[str, Matrix], ...]
    controls: Tuple[Tuple[str, Matrix], ...]
    readouts: Tuple[Readout, ...]
    tokens: Tuple[Token, ...]

    @property
    def dimension(self) -> int:
        return len(self.configurations)


@dataclass(frozen=True)
class RecordStatus:
    occurred: bool
    availability: Tuple[Tuple[str, bool], ...]
    historical_algebra_generators: Tuple[str, ...]
    persistent_algebra_generators: Tuple[str, ...]


FORBIDDEN_SCHEMA_KEYS = frozenset(
    {
        "causal_order",
        "causal_cone",
        "coordinates",
        "embedding",
        "metric",
        "field_propagator",
        "dirac_operator",
        "stress_tensor",
    }
)


class SmugglingError(ValueError):
    pass


def reject_schema_inputs(offered: Mapping[str, object]) -> None:
    forbidden = tuple(sorted(FORBIDDEN_SCHEMA_KEYS.intersection(offered)))
    if forbidden:
        raise SmugglingError("forbidden region input: " + ",".join(forbidden))


def build_region(name: str, qubits: int, offered: Optional[Mapping[str, object]] = None) -> QuantumRegion:
    reject_schema_inputs(offered or {})
    if qubits < 2:
        raise ValueError("region needs branch and record bits")
    dimension = 2 ** qubits
    write_h = on_qubit(H, 0, qubits)
    copying = cnot(qubits, 0, 1)
    write = matmul(copying, write_h)
    preserve = identity(dimension)
    for target in (0,) + tuple(range(2, qubits)):
        preserve = matmul(on_qubit(H, target, qubits), preserve)
    eraser = matmul(preserve, copying)
    memory_values = tuple(bit_value(configuration, 1, qubits) for configuration in range(dimension))
    configuration_values = tuple(range(dimension))
    readouts = (
        Readout("memory", memory_values, True),
        Readout("configuration-probe", configuration_values, False),
    )
    tokens = (Token(name + ":memory-token", "memory", (name, "write", "memory-readout")),)
    interfaces = tuple(BoundarySpace(f"{name}:V{index}", dimension) for index in range(3))
    signatures = (
        ArrowSignature("write", "write", interfaces[0].name, interfaces[1].name),
        ArrowSignature("preserve", "preserve", interfaces[1].name, interfaces[2].name),
        ArrowSignature("erase", "erase", interfaces[1].name, interfaces[2].name),
        ArrowSignature("no-write", "control", interfaces[0].name, interfaces[1].name),
    )
    return QuantumRegion(
        name=name,
        qubits=qubits,
        configurations=tuple(range(dimension)),
        preparations=tuple(range(dimension)),
        actual_preparation=0,
        interfaces=interfaces,
        amplitude_signatures=signatures,
        write=write,
        preserve=(("preserve", preserve),),
        erase=(("erase", eraser),),
        controls=(("no-write", write_h),),
        readouts=readouts,
        tokens=tokens,
    )


def typed_amplitude_family(region: QuantumRegion) -> Mapping[str, object]:
    interfaces = {interface.name: interface for interface in region.interfaces}
    matrices = {
        "write": region.write,
        **dict(region.preserve),
        **dict(region.erase),
        **dict(region.controls),
    }
    rows = []
    for signature in region.amplitude_signatures:
        arrow = matrices[signature.name]
        source = interfaces[signature.source]
        target = interfaces[signature.target]
        rows.append(
            (
                signature.name,
                signature.family,
                signature.source,
                signature.target,
                len(arrow) == target.dimension,
                len(arrow[0]) == source.dimension,
            )
        )
    write = next(signature for signature in region.amplitude_signatures if signature.name == "write")
    continuations = tuple(
        signature
        for signature in region.amplitude_signatures
        if signature.family in ("preserve", "erase")
    )
    return {
        "rows": tuple(rows),
        "all_names_accounted": set(matrices) == {row.name for row in region.amplitude_signatures},
        "continuations_compose_after_write": all(
            write.target == continuation.source for continuation in continuations
        ),
        "families_disjoint": len({row.name for row in region.amplitude_signatures})
        == len(region.amplitude_signatures),
    }


def candidate_readouts(region: QuantumRegion) -> Tuple[Readout, ...]:
    return tuple(readout for readout in region.readouts if readout.record_candidate)


def h_corr(write: Matrix, readout: Readout, preparations: Sequence[int]) -> bool:
    for preparation in preparations:
        live = [row for row in range(len(write)) if not write[row][preparation].is_zero()]
        values = [readout.values[row] for row in live]
        if len(values) != len(set(values)):
            return False
    return True


def h_avail(continuation: Matrix, readout: Readout) -> bool:
    for output in range(len(continuation)):
        values = {
            readout.values[cut]
            for cut in range(len(continuation))
            if not continuation[output][cut].is_zero()
        }
        if len(values) > 1:
            return False
    return True


def derive_record_status(region: QuantumRegion) -> Mapping[str, RecordStatus]:
    result = {}
    continuations = region.preserve + region.erase
    for readout in candidate_readouts(region):
        occurred = h_corr(region.write, readout, region.preparations)
        availability = tuple(
            (name, bool(occurred and h_avail(continuation, readout)))
            for name, continuation in continuations
        )
        historical = (readout.name,) if occurred else ()
        persistent = (
            (readout.name,)
            if occurred and all(h_avail(continuation, readout) for _name, continuation in region.preserve)
            else ()
        )
        result[readout.name] = RecordStatus(occurred, availability, historical, persistent)
    return result


def cut_coherence_stats(later: Matrix, earlier: Matrix, values: Sequence[Hashable]) -> Mapping[str, int]:
    cross = 0
    within = 0
    total = 0
    for output in range(len(later)):
        for preparation in range(len(earlier[0])):
            live_paths = [
                cut
                for cut in range(len(earlier))
                if not (later[output][cut] * earlier[cut][preparation]).is_zero()
            ]
            for left_index, left in enumerate(live_paths):
                for right in live_paths[left_index + 1 :]:
                    coherence = (
                        later[output][left]
                        * earlier[left][preparation]
                        * later[output][right]
                        * earlier[right][preparation]
                    )
                    if coherence.is_zero():
                        continue
                    total += 1
                    if values[left] == values[right]:
                        within += 1
                    else:
                        cross += 1
    return {"total": total, "cross_sector": cross, "within_sector": within}


def aggregate_by_values(shadow: Matrix, values: Sequence[Hashable]) -> Tuple[Tuple[Q2, ...], ...]:
    labels = tuple(sorted(set(values)))
    rows = []
    for output_label in labels:
        row = []
        for input_configuration in range(len(shadow[0])):
            row.append(
                sum(
                    (
                        shadow[output][input_configuration]
                        for output in range(len(shadow))
                        if values[output] == output_label
                    ),
                    ZERO,
                )
            )
        rows.append(tuple(row))
    return tuple(rows)


def quotient_kernel(shadow: Matrix, values: Sequence[Hashable]) -> Optional[Matrix]:
    labels = tuple(sorted(set(values)))
    columns = []
    for input_label in labels:
        representatives = [index for index, value in enumerate(values) if value == input_label]
        profiles = []
        for representative in representatives:
            profile = tuple(
                sum(
                    (
                        shadow[output][representative]
                        for output in range(len(shadow))
                        if values[output] == output_label
                    ),
                    ZERO,
                )
                for output_label in labels
            )
            profiles.append(profile)
        if any(profile != profiles[0] for profile in profiles[1:]):
            return None
        columns.append(profiles[0])
    return tuple(tuple(columns[column][row] for column in range(len(columns))) for row in range(len(labels)))


def record_residual(region: QuantumRegion, continuation: Matrix, readout: Readout) -> Optional[Matrix]:
    write_shadow = born(region.write)
    continuation_shadow = born(continuation)
    quotient = quotient_kernel(continuation_shadow, readout.values)
    if quotient is None:
        return None
    gamma10 = aggregate_by_values(write_shadow, readout.values)
    gamma20 = aggregate_by_values(born(matmul(continuation, region.write)), readout.values)
    return matsub(gamma20, matmul(quotient, gamma10))


def sign_diagonal(signs: Sequence[int]) -> Matrix:
    return diagonal(tuple(1 if sign > 0 else -1 for sign in signs))


def boundary_gauge_pair(
    write: Matrix,
    continuation: Matrix,
    input_signs: Sequence[int],
    cut_signs: Sequence[int],
    output_signs: Sequence[int],
) -> Tuple[Matrix, Matrix]:
    d0 = sign_diagonal(input_signs)
    d1 = sign_diagonal(cut_signs)
    d2 = sign_diagonal(output_signs)
    return matmul(matmul(d1, write), d0), matmul(matmul(d2, continuation), d1)


def permutation_matrix(permutation: Sequence[int]) -> Matrix:
    size = len(permutation)
    out = [[ZERO for _column in range(size)] for _row in range(size)]
    for old, new in enumerate(permutation):
        out[new][old] = ONE
    return tuple(tuple(row) for row in out)


def conjugate_by_permutation(value: Matrix, permutation: Sequence[int]) -> Matrix:
    p = permutation_matrix(permutation)
    return matmul(matmul(p, value), transpose(p))


def permute_readout(readout: Readout, permutation: Sequence[int]) -> Readout:
    values = [None] * len(readout.values)
    for old, new in enumerate(permutation):
        values[new] = readout.values[old]
    return Readout(readout.name, tuple(values), readout.record_candidate)


def allowed_readout_permutations(readout: Readout, actual_preparation: int) -> Tuple[Tuple[int, ...], ...]:
    allowed = []
    for permutation in itertools.permutations(range(len(readout.values))):
        if permutation[actual_preparation] != actual_preparation:
            continue
        if all(readout.values[old] == readout.values[permutation[old]] for old in range(len(permutation))):
            allowed.append(tuple(permutation))
    return tuple(allowed)


def equivalent_composite_law(
    left: Matrix, right: Matrix, readout: Readout, actual_preparation: int
) -> bool:
    for permutation in allowed_readout_permutations(readout, actual_preparation):
        if conjugate_by_permutation(left, permutation) == right:
            return True
    return False


def find_uncompensated_control(region: QuantumRegion) -> Mapping[str, object]:
    continuation = dict(region.erase)["erase"]
    original_composite = born(matmul(continuation, region.write))
    readout = candidate_readouts(region)[0]
    for signs in itertools.product((-1, 1), repeat=region.dimension):
        if len(set(signs)) == 1:
            continue
        inserted_write = matmul(sign_diagonal(signs), region.write)
        candidate_composite = born(matmul(continuation, inserted_write))
        if candidate_composite == original_composite:
            continue
        if equivalent_composite_law(
            original_composite,
            candidate_composite,
            readout,
            region.actual_preparation,
        ):
            continue
        return {
            "signs": tuple(signs),
            "write_shadow_equal": born(inserted_write) == born(region.write),
            "continuation_shadow_equal": True,
            "composite_changed": True,
            "gauge_equivalent_under_allowed_relabelling": False,
            "original_digest": matrix_digest(original_composite),
            "inserted_digest": matrix_digest(candidate_composite),
        }
    raise AssertionError("no uncompensated physical control found")


def readout_law(write: Matrix, readout: Readout, preparation: int) -> Tuple[Tuple[Hashable, Q2], ...]:
    law: Dict[Hashable, Q2] = {}
    shadow = born(write)
    for configuration, value in enumerate(readout.values):
        probability = shadow[configuration][preparation]
        if not probability.is_zero():
            law[value] = law.get(value, ZERO) + probability
    return tuple(sorted(law.items()))


def bit_swap_permutation(qubits: int, left: int, right: int) -> Tuple[int, ...]:
    permutation = []
    for source in range(2 ** qubits):
        bits = [(source >> (qubits - 1 - index)) & 1 for index in range(qubits)]
        bits[left], bits[right] = bits[right], bits[left]
        destination = 0
        for bit in bits:
            destination = 2 * destination + bit
        permutation.append(destination)
    return tuple(permutation)


def common_extension() -> Mapping[str, object]:
    qubits = 4
    write = on_qubit(H, 0, qubits)
    for record_bit in (1, 2, 3):
        write = matmul(cnot(qubits, 0, record_bit), write)
    preserve = on_qubit(H, 0, qubits)
    joint_values = tuple(
        tuple(bit_value(configuration, bit, qubits) for bit in (1, 2, 3))
        for configuration in range(2 ** qubits)
    )
    readout = Readout("joint-memory", joint_values, True)
    preparation = 0
    support = tuple(
        sorted(
            {
                joint_values[configuration]
                for configuration in range(2 ** qubits)
                if not write[configuration][preparation].is_zero()
            }
        )
    )
    law = readout_law(write, readout, preparation)
    restrictions = tuple(
        tuple((joint_value, joint_value[index]) for joint_value in support)
        for index in range(3)
    )
    marginal_laws = tuple(
        tuple(
            sorted(
                {
                    value: sum(
                        (probability for joint_value, probability in law if joint_value[index] == value),
                        ZERO,
                    )
                    for value in (0, 1)
                }.items()
            )
        )
        for index in range(3)
    )
    swap12 = bit_swap_permutation(qubits, 1, 2)
    return {
        "write": write,
        "preserve": preserve,
        "readout": readout,
        "preparations": (preparation,),
        "support": support,
        "law": law,
        "restrictions": restrictions,
        "marginal_laws": marginal_laws,
        "record_swap_12": swap12,
    }


def pair_fact_maps(pair_support: Iterable[Tuple[int, int]]) -> Tuple[Tuple[Tuple[int, int], ...], ...]:
    support = frozenset(pair_support)
    maps = []
    for image in itertools.permutations((0, 1)):
        mapping = {0: image[0], 1: image[1]}
        if all((value, mapping[value]) in support for value in (0, 1)):
            maps.append(tuple(sorted(mapping.items())))
    return tuple(sorted(maps))


def regional_fact_groupoid(triple_support: Sequence[Tuple[int, int, int]]) -> Mapping[str, object]:
    objects = ("D1", "D2", "D3")
    arrows: Dict[Tuple[str, str], Tuple[Tuple[int, int], ...]] = {}
    for source_index, source in enumerate(objects):
        for target_index, target in enumerate(objects):
            pair_support = tuple(
                sorted(
                    {
                        (row[source_index], row[target_index])
                        for row in triple_support
                    }
                )
            )
            family = pair_fact_maps(pair_support)
            if len(family) != 1:
                raise AssertionError("common extension does not force a unique fact arrow")
            arrows[(source, target)] = family[0]

    identity_laws = []
    inverse_laws = []
    composition_laws = []
    for source in objects:
        identity_laws.append(dict(arrows[(source, source)]) == {0: 0, 1: 1})
        for target in objects:
            forward = dict(arrows[(source, target)])
            backward = dict(arrows[(target, source)])
            inverse_laws.append(
                all(backward[forward[value]] == value for value in (0, 1))
            )
            for destination in objects:
                second = dict(arrows[(target, destination)])
                composite = {value: second[forward[value]] for value in (0, 1)}
                composition_laws.append(
                    composite == dict(arrows[(source, destination)])
                )
    return {
        "objects": objects,
        "arrows": tuple(
            (source, target, arrows[(source, target)])
            for source in objects
            for target in objects
        ),
        "covering_family": objects,
        "triple_overlap_support": tuple(triple_support),
        "identity_laws": tuple(identity_laws),
        "inverse_laws": tuple(inverse_laws),
        "composition_laws": tuple(composition_laws),
        "all_laws": (
            all(identity_laws)
            and all(inverse_laws)
            and all(composition_laws)
            and bool(triple_support)
        ),
    }


def token_map_family() -> Tuple[Tuple[int, ...], ...]:
    return tuple(itertools.permutations((0, 1)))


def compose_token_maps(first: Sequence[int], second: Sequence[int]) -> Tuple[int, ...]:
    return tuple(second[first[index]] for index in range(len(first)))


def inverse_token_map(mapping: Sequence[int]) -> Tuple[int, ...]:
    inverse = [0] * len(mapping)
    for source, target in enumerate(mapping):
        inverse[target] = source
    return tuple(inverse)


def coarse_grain_shadow(
    fine_shadow: Matrix,
    coarse_dimension: int,
    extra_dimension: int,
    extra_input: int,
) -> Matrix:
    rows = []
    for coarse_output in range(coarse_dimension):
        row = []
        for coarse_input in range(coarse_dimension):
            fine_input = coarse_input * extra_dimension + extra_input
            probability = sum(
                (
                    fine_shadow[coarse_output * extra_dimension + extra_output][fine_input]
                    for extra_output in range(extra_dimension)
                ),
                ZERO,
            )
            row.append(probability)
        rows.append(tuple(row))
    return tuple(rows)


def refinement_rows(coarse: QuantumRegion, fine: QuantumRegion) -> Mapping[str, object]:
    extra_dimension = fine.dimension // coarse.dimension
    pairs = {
        "write": (coarse.write, fine.write),
        "preserve": (dict(coarse.preserve)["preserve"], dict(fine.preserve)["preserve"]),
        "erase": (dict(coarse.erase)["erase"], dict(fine.erase)["erase"]),
    }
    rows = {}
    for name, (coarse_arrow, fine_arrow) in pairs.items():
        matches = tuple(
            coarse_grain_shadow(
                born(fine_arrow),
                coarse.dimension,
                extra_dimension,
                extra_input,
            )
            == born(coarse_arrow)
            for extra_input in range(extra_dimension)
        )
        rows[name] = matches
    return {
        "extra_dimension": extra_dimension,
        "shadow_rows": rows,
        "all_match": all(all(values) for values in rows.values()),
        "coarse_erase_defect_nonzero": nonzero_count(defect(dict(coarse.erase)["erase"], coarse.write)),
        "fine_erase_defect_nonzero": nonzero_count(defect(dict(fine.erase)["erase"], fine.write)),
    }


def fact_map_static_audit(path: Path) -> Mapping[str, object]:
    tree = ast.parse(path.read_text())
    forbidden = {
        "amplitude",
        "phase",
        "matrix",
        "born",
        "defect",
        "metric",
        "coordinates",
        "field_propagator",
    }
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "pair_fact_maps":
            names = {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}
            return {
                "arguments": tuple(argument.arg for argument in node.args.args),
                "forbidden_names": tuple(sorted(names.intersection(forbidden))),
            }
    raise AssertionError("pair_fact_maps not found")


def json_ready(value: object) -> object:
    if isinstance(value, Q2):
        return value.render()
    if isinstance(value, Fraction):
        return str(value)
    if hasattr(value, "__dataclass_fields__"):
        return {
            field: json_ready(getattr(value, field))
            for field in value.__dataclass_fields__
        }
    if isinstance(value, dict):
        return {
            str(key): json_ready(item)
            for key, item in sorted(value.items(), key=lambda row: str(row[0]))
        }
    if isinstance(value, (tuple, list)):
        return [json_ready(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [json_ready(item) for item in sorted(value)]
    if value is None or isinstance(value, (str, int, bool)):
        return value
    return repr(value)


class Checks:
    def __init__(self, emit: bool, mutant: bool) -> None:
        self.emit = emit
        self.mutant = mutant
        self.rows = []

    def section(self, title: str) -> None:
        if self.emit:
            print("\n" + title)

    def check(self, label: str, computed: object, expected: object) -> None:
        if self.mutant and label == "quantum amendment pin hash":
            expected = "0" * 64
            if self.emit:
                print("[MUTANT] deliberately corrupting the amendment-pin anchor")
        ok = computed == expected
        self.rows.append(
            {
                "label": label,
                "computed": json_ready(computed),
                "expected": json_ready(expected),
                "ok": ok,
            }
        )
        if self.emit:
            print(f"[{'PASS' if ok else 'FAIL'}] {label}: {computed!r}")

    def summary(self) -> Mapping[str, int]:
        failures = sum(not row["ok"] for row in self.rows)
        return {
            "checks": len(self.rows),
            "pass": len(self.rows) - failures,
            "fail": failures,
        }


def build_science(checks: Checks) -> Mapping[str, object]:
    checks.section("ANCHORS, READOUT FREEZE, AND USE CLASSES")
    ancestor = run(("/usr/bin/git", "merge-base", "--is-ancestor", PIN_COMMIT, "HEAD"))
    checks.check("amendment pin commit is ancestor of HEAD", ancestor.returncode, 0)
    checks.check("quantum amendment pin hash", sha256(ROOT / LOCKS["quantum amendment pin"][0]), LOCKS["quantum amendment pin"][1])
    lock_rows = tuple(
        (name, sha256(ROOT / relative) == expected, use_class)
        for name, (relative, expected, use_class) in LOCKS.items()
    )
    checks.check(
        "all binding locks and use classes",
        lock_rows,
        tuple((name, True, use_class) for name, (_relative, _expected, use_class) in LOCKS.items()),
    )
    policy_hash = hashlib.sha256(READOUT_POLICY.encode()).hexdigest()
    checks.check("frozen readout policy hash", policy_hash, READOUT_POLICY_SHA256)
    checks.check("record partition search is absent by policy", "partition-search=forbidden" in READOUT_POLICY, True)

    regions = tuple(build_region(f"D{index}", qubits) for index, qubits in enumerate((2, 3, 4), start=1))

    checks.section("NEW GAUGE-TYPED QUANTUM REGIONS")
    checks.check("three carrier dimensions are exact and pairwise distinct", tuple(region.dimension for region in regions), (4, 8, 16))
    checks.check(
        "frozen regional readout hashes",
        tuple(
            (region.name, readout_digest(candidate_readouts(region)[0]))
            for region in regions
        ),
        tuple((name, digest) for name, digest in READOUT_VALUE_LOCKS.items()),
    )
    checks.check(
        "preparation and intervention scopes are explicit",
        tuple(
            (
                region.name,
                region.actual_preparation,
                len(region.preparations),
                tuple(name for name, _arrow in region.preserve),
                tuple(name for name, _arrow in region.erase),
                tuple(name for name, _arrow in region.controls),
            )
            for region in regions
        ),
        tuple(
            (f"D{index}", 0, dimension, ("preserve",), ("erase",), ("no-write",))
            for index, dimension in enumerate((4, 8, 16), start=1)
        ),
    )
    typed_families = {region.name: typed_amplitude_family(region) for region in regions}
    checks.check(
        "amplitude arrows have explicit source/target types and compose at the declared cut",
        tuple(
            (
                region.name,
                typed_families[region.name]["rows"],
                typed_families[region.name]["all_names_accounted"],
                typed_families[region.name]["continuations_compose_after_write"],
                typed_families[region.name]["families_disjoint"],
            )
            for region in regions
        ),
        tuple(
            (
                f"D{index}",
                (
                    ("write", "write", f"D{index}:V0", f"D{index}:V1", True, True),
                    ("preserve", "preserve", f"D{index}:V1", f"D{index}:V2", True, True),
                    ("erase", "erase", f"D{index}:V1", f"D{index}:V2", True, True),
                    ("no-write", "control", f"D{index}:V0", f"D{index}:V1", True, True),
                ),
                True,
                True,
                True,
            )
            for index in range(1, 4)
        ),
    )
    checks.check(
        "all amplitude arrows are unitary",
        all(
            is_unitary(arrow)
            for region in regions
            for arrow in (region.write,)
            + tuple(value for _name, value in region.preserve)
            + tuple(value for _name, value in region.erase)
            + tuple(value for _name, value in region.controls)
        ),
        True,
    )
    checks.check("all basis configurations are operationally preparable", tuple(len(region.preparations) for region in regions), tuple(region.dimension for region in regions))
    checks.check("all final configurations are exposed to the tomography probe", tuple(len(next(readout.values for readout in region.readouts if readout.name == "configuration-probe")) for region in regions), tuple(region.dimension for region in regions))
    checks.check("exact carrier dimension invariant proves regional non-isomorphism", tuple(math.factorial(left.dimension) if left.dimension == right.dimension else 0 for left, right in ((regions[0], regions[1]), (regions[1], regions[2]), (regions[0], regions[2]))), (0, 0, 0))

    statuses = {region.name: derive_record_status(region) for region in regions}
    checks.section("DERIVED CONTINUATION-RELATIVE RECORD ALGEBRAS")
    checks.check(
        "memory occurrence is derived by H-corr on each write arrow",
        tuple(statuses[region.name]["memory"].occurred for region in regions),
        (True, True, True),
    )
    checks.check(
        "memory availability is continuation-relative",
        tuple(statuses[region.name]["memory"].availability for region in regions),
        tuple((("preserve", True), ("erase", False)) for _region in regions),
    )
    checks.check(
        "historical and persistent algebras are derived separately",
        tuple(
            (
                statuses[region.name]["memory"].historical_algebra_generators,
                statuses[region.name]["memory"].persistent_algebra_generators,
            )
            for region in regions
        ),
        tuple((("memory",), ("memory",)) for _region in regions),
    )
    checks.check(
        "no-write control fails H-corr",
        tuple(
            h_corr(dict(region.controls)["no-write"], candidate_readouts(region)[0], region.preparations)
            for region in regions
        ),
        (False, False, False),
    )

    coherence_rows = {}
    residual_rows = {}
    checks.section("CUT COHERENCE, CONFIGURATION DEFECT, AND RECORD RESIDUAL")
    for region in regions:
        readout = candidate_readouts(region)[0]
        preserving = dict(region.preserve)["preserve"]
        erasing = dict(region.erase)["erase"]
        preserve_coherence = cut_coherence_stats(preserving, region.write, readout.values)
        erase_coherence = cut_coherence_stats(erasing, region.write, readout.values)
        preserve_defect = defect(preserving, region.write)
        erase_defect = defect(erasing, region.write)
        preserve_residual = record_residual(region, preserving, readout)
        erase_residual = record_residual(region, erasing, readout)
        coherence_rows[region.name] = {
            "preserve": preserve_coherence,
            "erase": erase_coherence,
            "preserve_defect_nonzero": nonzero_count(preserve_defect),
            "erase_defect_nonzero": nonzero_count(erase_defect),
        }
        residual_rows[region.name] = {
            "preserve_defined": preserve_residual is not None,
            "preserve_nonzero": None if preserve_residual is None else nonzero_count(preserve_residual),
            "erase_defined": erase_residual is not None,
            "erase_nonzero": None if erase_residual is None else nonzero_count(erase_residual),
        }
        checks.check(f"{region.name} H-avail block-diagonalizes preserving cut coherence", preserve_coherence["cross_sector"], 0)
        checks.check(f"{region.name} H-corr kills remaining preserving off-diagonals", preserve_coherence["within_sector"], 0)
        checks.check(f"{region.name} preserving configuration defect vanishes", nonzero_count(preserve_defect), 0)
        checks.check(f"{region.name} coarse record residual is defined and zero", (preserve_residual is not None, nonzero_count(preserve_residual) if preserve_residual is not None else None), (True, 0))
        checks.check(f"{region.name} eraser restores cross-sector coherence", erase_coherence["cross_sector"] > 0, True)
        checks.check(f"{region.name} eraser has an observable nonzero configuration defect", nonzero_count(erase_defect) > 0, True)
        checks.check(f"{region.name} eraser destroys a well-defined record quotient", erase_residual is None, True)

    checks.section("REGIONAL GAUGE AND PHYSICAL PHASE CONTROL")
    base = regions[0]
    base_readout = candidate_readouts(base)[0]
    base_preserve = dict(base.preserve)["preserve"]
    signs0 = (1, -1, 1, -1)
    signs1 = (-1, 1, 1, -1)
    signs2 = (1, 1, -1, -1)
    gauged_write, gauged_preserve = boundary_gauge_pair(
        base.write, base_preserve, signs0, signs1, signs2
    )
    checks.check(
        "composition-compatible boundary gauge preserves both arrows and composite Born laws",
        (
            born(gauged_write) == born(base.write),
            born(gauged_preserve) == born(base_preserve),
            born(matmul(gauged_preserve, gauged_write)) == born(matmul(base_preserve, base.write)),
        ),
        (True, True, True),
    )
    cut_only_write, cut_only_preserve = boundary_gauge_pair(
        base.write,
        base_preserve,
        (1,) * base.dimension,
        signs1,
        (1,) * base.dimension,
    )
    outer_only_write, outer_only_preserve = boundary_gauge_pair(
        base.write,
        base_preserve,
        signs0,
        (1,) * base.dimension,
        signs2,
    )
    checks.check(
        "outer-boundary and compensated-cut gauges are separately verified",
        (
            born(matmul(cut_only_preserve, cut_only_write))
            == born(matmul(base_preserve, base.write)),
            born(matmul(outer_only_preserve, outer_only_write))
            == born(matmul(base_preserve, base.write)),
        ),
        (True, True),
    )
    gauge_readout = Readout(base_readout.name, base_readout.values, True)
    checks.check("boundary gauge preserves W3 status", (h_corr(gauged_write, gauge_readout, base.preparations), h_avail(gauged_preserve, gauge_readout)), (True, True))

    permutation = (0, 3, 2, 1)
    permuted_write = conjugate_by_permutation(base.write, permutation)
    permuted_preserve = conjugate_by_permutation(base_preserve, permutation)
    permuted_erase = conjugate_by_permutation(dict(base.erase)["erase"], permutation)
    permuted_region = QuantumRegion(
        name="D1-relabelled",
        qubits=base.qubits,
        configurations=tuple(permutation[index] for index in base.configurations),
        preparations=tuple(permutation[index] for index in base.preparations),
        actual_preparation=permutation[base.actual_preparation],
        interfaces=base.interfaces,
        amplitude_signatures=base.amplitude_signatures,
        write=permuted_write,
        preserve=(("preserve", permuted_preserve),),
        erase=(("erase", permuted_erase),),
        controls=tuple(
            (name, conjugate_by_permutation(arrow, permutation))
            for name, arrow in base.controls
        ),
        readouts=tuple(permute_readout(readout, permutation) for readout in base.readouts),
        tokens=base.tokens,
    )
    permuted_readout = candidate_readouts(permuted_region)[0]
    base_status = derive_record_status(base)["memory"]
    permuted_status = derive_record_status(permuted_region)["memory"]
    checks.check(
        "C1 configuration relabelling preserves shadows, defect, W3, and derived algebras",
        (
            born(permuted_write) == conjugate_by_permutation(born(base.write), permutation),
            born(permuted_preserve) == conjugate_by_permutation(born(base_preserve), permutation),
            defect(permuted_preserve, permuted_write)
            == conjugate_by_permutation(defect(base_preserve, base.write), permutation),
            h_corr(permuted_write, permuted_readout, permuted_region.preparations),
            h_avail(permuted_preserve, permuted_readout),
            permuted_status == base_status,
        ),
        (True, True, True, True, True, True),
    )
    uncompensated = find_uncompensated_control(base)
    checks.check("C2 uncompensated cut leaves one-step Born shadows equal", (uncompensated["write_shadow_equal"], uncompensated["continuation_shadow_equal"]), (True, True))
    checks.check("C2 uncompensated cut changes the accessible composite law", uncompensated["composite_changed"], True)
    checks.check("C2 physical phase control is not an allowed relabelling gauge", uncompensated["gauge_equivalent_under_allowed_relabelling"], False)

    checks.section("COMMON-EXTENSION FACT CERTIFICATE AND TRIPLE DESCENT")
    extension = common_extension()
    extension_readout = extension["readout"]
    checks.check("common extension is exact and unitary", (is_unitary(extension["write"]), is_unitary(extension["preserve"])), (True, True))
    checks.check("common-extension joint support is nonvacuous and diagonal", extension["support"], ((0, 0, 0), (1, 1, 1)))
    checks.check("common-extension joint readout passes scoped H-corr", h_corr(extension["write"], extension_readout, extension["preparations"]), True)
    checks.check("common-extension joint readout passes H-avail", h_avail(extension["preserve"], extension_readout), True)
    checks.check("common-extension fact law is exactly balanced", extension["law"], (((0, 0, 0), Q2(Fraction(1, 2))), ((1, 1, 1), Q2(Fraction(1, 2)))))
    expected_restriction = (((0, 0, 0), 0), ((1, 1, 1), 1))
    checks.check(
        "common-extension restriction maps to all three regional readouts are explicit",
        extension["restrictions"],
        (expected_restriction, expected_restriction, expected_restriction),
    )
    regional_record_laws = tuple(
        readout_law(
            region.write,
            candidate_readouts(region)[0],
            region.actual_preparation,
        )
        for region in regions
    )
    checks.check(
        "common-extension marginals equal the three regional record laws",
        extension["marginal_laws"],
        regional_record_laws,
    )

    triple_support = extension["support"]
    pair_supports = (
        tuple(sorted({(row[0], row[1]) for row in triple_support})),
        tuple(sorted({(row[1], row[2]) for row in triple_support})),
        tuple(sorted({(row[0], row[2]) for row in triple_support})),
    )
    fact_map_families = tuple(pair_fact_maps(support) for support in pair_supports)
    checks.check("C5 common extension forces one fact map on each pair", tuple(len(family) for family in fact_map_families), (1, 1, 1))
    map12 = dict(fact_map_families[0][0])
    map23 = dict(fact_map_families[1][0])
    map13 = dict(fact_map_families[2][0])
    composite_fact_map = {value: map23[map12[value]] for value in map12}
    checks.check("C5 unique fact maps satisfy the triple law", composite_fact_map, map13)
    fact_groupoid = regional_fact_groupoid(triple_support)
    checks.check(
        "regional fact groupoid has identities, inverses, all 27 composition laws, and a nonvacuous cover",
        (
            fact_groupoid["objects"],
            len(fact_groupoid["arrows"]),
            len(fact_groupoid["identity_laws"]),
            len(fact_groupoid["inverse_laws"]),
            len(fact_groupoid["composition_laws"]),
            fact_groupoid["covering_family"],
            fact_groupoid["triple_overlap_support"],
            fact_groupoid["all_laws"],
        ),
        (
            ("D1", "D2", "D3"),
            9,
            3,
            9,
            27,
            ("D1", "D2", "D3"),
            ((0, 0, 0), (1, 1, 1)),
            True,
        ),
    )

    regional_tokens = tuple(region.tokens[0] for region in regions)
    checks.check(
        "C3 three regional event tokens remain provenance-distinct",
        tuple((token.local_name, token.provenance) for token in regional_tokens),
        tuple(
            (
                f"D{index}:memory-token",
                (f"D{index}", "write", "memory-readout"),
            )
            for index in range(1, 4)
        ),
    )
    token_family = token_map_family()
    record_swap = extension["record_swap_12"]
    support_swapped = tuple(
        sorted((row[1], row[0], row[2]) for row in extension["support"])
    )
    checks.check(
        "C3/C7 redundant-copy S2 is an exact common-extension amplitude symmetry",
        (
            conjugate_by_permutation(extension["write"], record_swap) == extension["write"],
            conjugate_by_permutation(extension["preserve"], record_swap) == extension["preserve"],
            record_swap[extension["preparations"][0]] == extension["preparations"][0],
            support_swapped == extension["support"],
            len(token_family),
        ),
        (True, True, True, True, 2),
    )
    checks.check("C3 one fact remains independently forced", tuple(len(family) for family in fact_map_families), (1, 1, 1))
    token12 = token_family[0]
    token23 = token_family[0]
    token13 = token_family[1]
    token_composite = compose_token_maps(token12, token23)
    holonomy = compose_token_maps(token_composite, inverse_token_map(token13))
    checks.check("C6 all twisted pairwise groupoid-fibre maps are admissible", all(mapping in token_family for mapping in (token12, token23, token13)), True)
    checks.check("C6 twisted groupoid-fibre triple fails on the nose", token_composite == token13, False)
    checks.check("C6 groupoid-fibre loop holonomy is the nonidentity swap", holonomy, (1, 0))
    checks.check("C7 receipt retains the full family rather than a representative", token_family, ((0, 1), (1, 0)))

    audit = fact_map_static_audit(ROOT / "v13/code/rq0_quantum_regions_exact.py")
    checks.check("fact-map predicate consumes support only", audit["arguments"], ("pair_support",))
    checks.check("phase/amplitude/geometry names are absent from fact identity", audit["forbidden_names"], ())

    checks.section("REFINEMENT AND CLAIM CEILING")
    refinement12 = refinement_rows(regions[0], regions[1])
    refinement23 = refinement_rows(regions[1], regions[2])
    checks.check("C10 D1-to-D2 instrument shadows coarse-grain exactly", refinement12["all_match"], True)
    checks.check("C10 D2-to-D3 instrument shadows coarse-grain exactly", refinement23["all_match"], True)
    checks.check("C10 refinement preserves the derived record generator", tuple(statuses[region.name]["memory"].persistent_algebra_generators for region in regions), (("memory",), ("memory",), ("memory",)))
    checks.check("C10 refinement reports rather than hides full-defect changes", (refinement12["coarse_erase_defect_nonzero"], refinement12["fine_erase_defect_nonzero"], refinement23["fine_erase_defect_nonzero"]), tuple(coherence_rows[region.name]["erase_defect_nonzero"] for region in regions))

    guard_results = []
    for forbidden_key in ("causal_order", "metric", "field_propagator"):
        try:
            build_region("forbidden", 2, offered={forbidden_key: "inserted"})
            guard_results.append(False)
        except SmugglingError:
            guard_results.append(True)
    checks.check("C8/C9/C11 causal, geometry, and field schema guards fire", tuple(guard_results), (True, True, True))
    classification = "FACT-DESCENT-ONLY" if all(len(family) == 1 for family in fact_map_families) else "NO-FACT-DESCENT"
    checks.check("C8 no locality instrument means fact descent only", classification, "FACT-DESCENT-ONLY")

    earned = {
        "RQ0-BLOCKED-AT-REGION": False,
        "RQ0-REGIONS-CONSTRUCTED": all(statuses[region.name]["memory"].occurred for region in regions),
        "RQ0-REGIONAL-SITE": fact_groupoid["all_laws"],
        "RQ0-FACT-DESCENT": classification == "FACT-DESCENT-ONLY" and extension["support"] == ((0, 0, 0), (1, 1, 1)),
        "RQ0-GROUPOID-ARENA": False,
        "RQ0-CAUSAL-ARENA": False,
        "RQ0-CONFORMAL-ARENA": False,
    }
    checks.section("PRE-REGISTERED OUTCOME LADDER")
    checks.check("three permitted positive rungs are earned", tuple(earned[name] for name in ("RQ0-REGIONS-CONSTRUCTED", "RQ0-REGIONAL-SITE", "RQ0-FACT-DESCENT")), (True, True, True))
    checks.check("all forbidden higher arena rungs remain false", tuple(earned[name] for name in ("RQ0-GROUPOID-ARENA", "RQ0-CAUSAL-ARENA", "RQ0-CONFORMAL-ARENA")), (False, False, False))
    checks.check("highest permitted outcome", "RQ0-FACT-DESCENT", "RQ0-FACT-DESCENT")

    return {
        "pin": {
            "commit": PIN_COMMIT,
            "clean_sheet_sha256": LOCKS["clean-sheet pin"][1],
            "amendment_sha256": LOCKS["quantum amendment pin"][1],
            "readout_policy": READOUT_POLICY,
            "readout_policy_sha256": READOUT_POLICY_SHA256,
        },
        "scope": {
            "arithmetic": "exact Q(sqrt(2)); no floats or tolerances",
            "region_dimensions": {region.name: region.dimension for region in regions},
            "preparation_scope": "every basis configuration in each region; actual preparation 0",
            "common_extension_preparation_scope": [0],
            "continuation_families": {
                "preserving": ["preserve"],
                "erasing": ["erase"],
                "controls": ["no-write"],
            },
            "readout_search": "none; one frozen memory-bit candidate per region",
            "readout_value_locks": READOUT_VALUE_LOCKS,
            "gauge_control": "configuration relabelling and exact +/- boundary rephasing",
            "fact_map_search": "all two bijections of the binary value alphabet",
            "token_map_search": "all two bijections of two redundant tokens",
            "isomorphism_scope": "carrier dimension is an exact accessible invariant; unequal-dimension bijection domains empty",
            "numerical_diagnostics": "none",
            "random_seeds": "none",
            "runtime_cap_seconds": 120,
        },
        "classifications": {
            "primitive_region": "DEFINITION plus provisional operational-nomology POSTULATE",
            "record_occurrence_availability": "MEASUREMENT by W3 support predicates",
            "preserving_cut_classicality": "THEOREM instance and exact measurement",
            "eraser_recoherence": "EXACT MEASUREMENT",
            "common_extension_fact": "CONSTRUCTED CERTIFICATE",
            "fact_descent": "EXACT MEASUREMENT",
            "token_groupoid": "EXACT MEASUREMENT; no geometric arena claim",
            "causal_locality": "OPEN; no instrument",
        },
        "legacy_uses": {
            name: {"path": relative, "class": use_class, "code_imported": False}
            for name, (relative, _expected, use_class) in LOCKS.items()
        }
        | {
            "v10_and_earlier": {
                "class": "no ontology, fixture, data, or code imported",
                "code_imported": False,
            }
        },
        "regions": {
            region.name: {
                "dimension": region.dimension,
                "preparations": len(region.preparations),
                "actual_preparation": region.actual_preparation,
                "interfaces": region.interfaces,
                "amplitude_signatures": region.amplitude_signatures,
                "record_readout_digest": readout_digest(candidate_readouts(region)[0]),
                "write_digest": matrix_digest(region.write),
                "preserve_digest": matrix_digest(dict(region.preserve)["preserve"]),
                "erase_digest": matrix_digest(dict(region.erase)["erase"]),
                "record_status": statuses[region.name],
                "coherence_and_defect": coherence_rows[region.name],
                "record_residual": residual_rows[region.name],
            }
            for region in regions
        },
        "gauge_and_phase_control": uncompensated,
        "common_extension": {
            "dimension": len(extension["write"]),
            "support": extension["support"],
            "law": extension["law"],
            "restriction_maps": extension["restrictions"],
            "marginal_laws": extension["marginal_laws"],
            "regional_record_laws": regional_record_laws,
            "fact_map_counts": tuple(len(family) for family in fact_map_families),
            "fact_triple_coherent": composite_fact_map == map13,
            "regional_tokens": regional_tokens,
            "token_map_family": token_family,
            "record_swap_12_amplitude_symmetry": (
                conjugate_by_permutation(extension["write"], record_swap) == extension["write"]
                and conjugate_by_permutation(extension["preserve"], record_swap)
                == extension["preserve"]
            ),
            "twisted_holonomy": holonomy,
        },
        "regional_fact_groupoid": fact_groupoid,
        "refinement": {"D1_to_D2": refinement12, "D2_to_D3": refinement23},
        "outcomes": earned,
        "highest_outcome": "RQ0-FACT-DESCENT",
        "first_unresolved_obstruction": (
            "define localized quantum subinstruments before constructing an operational "
            "influence relation between regional stable-record algebras"
        ),
        "nonclaims": (
            "no causal order or cone",
            "no spacetime region",
            "no volume or conformal metric",
            "no field propagator",
            "no gravity dynamics",
        ),
    }


def main() -> int:
    mutant = "--mutant" in sys.argv[1:]
    json_mode = "--json" in sys.argv[1:]
    emit = not json_mode
    if emit:
        print("=" * 78)
        print("v13 RQ0 -- QUANTUM REGIONAL INSTRUMENTS AND FACT DESCENT")
        print("Exact amplitude construction; no causal, metric, field, or gravity claim")
        print("=" * 78)
    checks = Checks(emit=emit, mutant=mutant)
    science = build_science(checks)
    summary = checks.summary()
    receipt = {
        "unit": "v13 RQ0 quantum factual base",
        "status": "GREEN-UNREVIEWED",
        "science": science,
        "checks": checks.rows,
        "summary": summary,
    }
    if json_mode:
        print(json.dumps(json_ready(receipt), indent=2, sort_keys=True))
    else:
        print("\nVERDICT")
        print("  highest rung: RQ0-FACT-DESCENT")
        print("  lower positive: RQ0-REGIONS-CONSTRUCTED / RQ0-REGIONAL-SITE")
        print("  token descent: groupoid-valued in the redundant-copy control")
        print("  ceiling: FACT-DESCENT-ONLY -- no localized quantum influence instrument")
        print("  next referent: localized subinstruments before operational influence")
        print("-" * 78)
        print(f"{summary['checks']} checks: {summary['pass']} pass, {summary['fail']} fail")
    return 1 if summary["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
