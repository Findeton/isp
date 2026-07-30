#!/usr/bin/env python3
"""Exact RQ0 physical-overlap repair.

Constructs equal-dimensional quantum amplitude instruments, explicit
subinstrument morphisms, a physical overlap, and derived record descent.
No causal, geometric, field, or gravity object is constructed.
"""

from __future__ import annotations

import ast
import contextlib
import hashlib
import io
import itertools
import json
import subprocess
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, Hashable, Iterable, Mapping, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
PIN_COMMIT = "b05ab95d6721d104a561875bc39aa6daa03f875e"
PIN_SHA256 = "a3627bee84a9b222feedb4f41215477ada33088a38b500f6c77a32c110e56cf3"
MASTER_SPEC_SHA256 = "132116e2a5b5880443eb609ce52fa940d71211746ba5d7b728984d08c9dbd7d9"
CONSTRUCTION_SURFACE_SHA256 = "e5661e6566279997e3ebd7bbd6a18e99cc635e2d7cd6f6e0e16c1b1030f5bcc3"
PRIOR_ADJUDICATION_COMMIT = "150f191f6d67dbaa2de99594e6b401d0a3f6e71f"
HOSTILE_ADJUDICATION_COMMIT = "1d9af029d3c04006c6e42941d66a590b2d887831"
REVIEWED_COMMITS = (
    "307c36f017d9d5587334d3b79421645ee5b54c61",
    "1537b1475705a5def1d1d063459fa7d4fb534982",
)
PROVENANCE_COMMITS = REVIEWED_COMMITS + (
    PRIOR_ADJUDICATION_COMMIT,
    HOSTILE_ADJUDICATION_COMMIT,
)

LOCKS = {
    "clean-sheet pin": (
        "v13/note-rq0-relativistic-arena-pin.md",
        "32f0fe8402c10477ba5f01abc69c44e0512c8f0cba7df1f5e39391908ead684c",
        "antecedent pin",
    ),
    "quantum amendment pin": (
        "v13/note-rq0-quantum-substrate-amendment-pin.md",
        "cc1c2177dc509641b1ae776444d599f554929c55c1452fa69d30af49cbd9ea91",
        "antecedent pin",
    ),
    "physical-overlap repair pin": (
        "v13/note-rq0-physical-overlap-repair-pin.md",
        PIN_SHA256,
        "active pin",
    ),
    "Paper 1": (
        "v12/paper1-composition-defect.md",
        "81bdab5673fb67b63cd10c08fbb80870f8aa01088047718c5b4bf447e1669128",
        "W3 and boundary-gauge antecedent",
    ),
    "Paper 2": (
        "v12/paper2-record-coreference.md",
        "d6af0e6513fc7088407dc5a26c513ecc4e9e45b5a5ae71ffa8a9571f274ad670",
        "fact-versus-law antecedent",
    ),
    "hostile review": (
        "v13/review-rq0-quantum-factual-base-hostile.md",
        "e8b5dab245f138402469aaf97eaf04ca2cf657c12c1396538005d69ca87b9eb3",
        "antecedent repair obligations",
    ),
    "physical-overlap hostile review": (
        "v13/review-rq0-physical-overlap-repair-hostile.md",
        "4aab5520f881a20033b3a0e67597feb330f7c3bd7592d8ad32479d3b5e0d0a10",
        "current bounded-repair obligations",
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
    """Exact a + b sqrt(2)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(value: object) -> "Q2":
        if isinstance(value, Q2):
            return value
        if isinstance(value, Fraction):
            return Q2(value)
        if isinstance(value, int):
            return Q2(Fraction(value))
        raise TypeError(f"cannot coerce {type(value).__name__} to Q2")

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


def identity(size: int) -> Matrix:
    return tuple(
        tuple(ONE if row == column else ZERO for column in range(size))
        for row in range(size)
    )


def rectangular_basis_map(rows: int, columns: int) -> Matrix:
    """Canonical basis truncation/inclusion used only for a failed bridge control."""

    return tuple(
        tuple(ONE if row == column else ZERO for column in range(columns))
        for row in range(rows)
    )


def transpose(value: Matrix) -> Matrix:
    return tuple(
        tuple(value[row][column] for row in range(len(value)))
        for column in range(len(value[0]))
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not compose")
    return tuple(
        tuple(
            sum(
                (
                    left[row][middle] * right[middle][column]
                    for middle in range(len(right))
                ),
                ZERO,
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][column] - right[row][column]
            for column in range(len(left[0]))
        )
        for row in range(len(left))
    )


def kron(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[lr][lc] * right[rr][rc]
            for lc in range(len(left[0]))
            for rc in range(len(right[0]))
        )
        for lr in range(len(left))
        for rr in range(len(right))
    )


def diagonal(values: Sequence[object]) -> Matrix:
    entries = tuple(Q2.coerce(value) for value in values)
    return tuple(
        tuple(entries[row] if row == column else ZERO for column in range(len(entries)))
        for row in range(len(entries))
    )


def is_unitary(value: Matrix) -> bool:
    return matmul(value, transpose(value)) == identity(len(value))


def is_signed_permutation(value: Matrix) -> bool:
    if not value or len(value) != len(value[0]):
        return False
    allowed = {ONE, -ONE}
    return (
        all(sum(entry in allowed for entry in row) == 1 for row in value)
        and all(
            sum(value[row][column] in allowed for row in range(len(value))) == 1
            for column in range(len(value[0]))
        )
        and all(
            entry.is_zero() or entry in allowed
            for row in value
            for entry in row
        )
    )


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


def born_multiset(value: Matrix) -> Tuple[str, ...]:
    return tuple(sorted(entry.render() for row in born(value) for entry in row))


H = matrix(((SQRT2_OVER_2, SQRT2_OVER_2), (SQRT2_OVER_2, -SQRT2_OVER_2)))
I2 = identity(2)
X = matrix(((0, 1), (1, 0)))


def on_qubit(gate: Matrix, target: int, qubits: int) -> Matrix:
    result = matrix(((1,),))
    for index in range(qubits):
        result = kron(result, gate if index == target else I2)
    return result


def controlled_x(qubits: int, control: int, target: int) -> Matrix:
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


def controlled_z(qubits: int, left: int, right: int) -> Matrix:
    signs = []
    for configuration in range(2 ** qubits):
        left_bit = (configuration >> (qubits - 1 - left)) & 1
        right_bit = (configuration >> (qubits - 1 - right)) & 1
        signs.append(-1 if left_bit and right_bit else 1)
    return diagonal(signs)


def compose_chronological(*gates: Matrix) -> Matrix:
    result = identity(len(gates[0]))
    for gate in gates:
        result = matmul(gate, result)
    return result


def bit_value(configuration: int, bit: int, qubits: int = 3) -> int:
    return (configuration >> (qubits - 1 - bit)) & 1


@dataclass(frozen=True)
class Boundary:
    name: str
    dimension: int


@dataclass(frozen=True)
class Arrow:
    name: str
    family: str
    source: str
    target: str
    amplitude: Matrix


@dataclass(frozen=True)
class Readout:
    name: str
    boundary: str
    values: Tuple[Hashable, ...]
    record_candidate: bool


@dataclass(frozen=True)
class Instrument:
    name: str
    boundaries: Tuple[Boundary, ...]
    arrows: Tuple[Arrow, ...]
    preparations: Tuple[int, ...]
    actual_preparation: int
    readouts: Tuple[Readout, ...]
    access_class: str
    gauge_class: str


@dataclass(frozen=True)
class BoundaryMap:
    source_boundary: str
    target_boundary: str
    amplitude: Matrix


@dataclass(frozen=True)
class InstrumentMorphism:
    name: str
    source: str
    target: str
    boundary_maps: Tuple[BoundaryMap, ...]
    arrow_map: Tuple[Tuple[str, str], ...]
    readout_map: Tuple[Tuple[str, str], ...]


@dataclass(frozen=True)
class RegCategory:
    """Finite category of amplitude instruments and typed morphisms."""

    objects: Tuple[str, ...]
    morphisms: Tuple[InstrumentMorphism, ...]
    cover: Tuple[str, ...]
    overlap: str


@dataclass(frozen=True)
class FactAlgebra:
    """Derived two-atom Boolean record algebra at the preserving scope."""

    name: str
    region: str
    generator: Optional[str]
    values: Tuple[Hashable, ...]


@dataclass(frozen=True)
class FactMorphism:
    """Contravariant record restriction induced by one Reg morphism."""

    name: str
    reg_morphism: str
    source: str
    target: str
    value_map: Tuple[Tuple[Hashable, Hashable], ...]


@dataclass(frozen=True)
class FactIfaceCategory:
    objects: Tuple[FactAlgebra, ...]
    morphisms: Tuple[FactMorphism, ...]


@dataclass(frozen=True)
class RecordFunctor:
    variance: str
    object_map: Tuple[Tuple[str, str], ...]
    arrow_map: Tuple[Tuple[str, str], ...]


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
        "complex_u1_gauge",
        "u1_boundary_gauge",
    }
)


class SmugglingError(ValueError):
    pass


def reject_schema_inputs(offered: Mapping[str, object]) -> None:
    forbidden = tuple(sorted(FORBIDDEN_SCHEMA_KEYS.intersection(offered)))
    if forbidden:
        raise SmugglingError("forbidden construction input: " + ",".join(forbidden))


def arrow_dict(instrument: Instrument) -> Dict[str, Arrow]:
    return {arrow.name: arrow for arrow in instrument.arrows}


def boundary_dict(instrument: Instrument) -> Dict[str, Boundary]:
    return {boundary.name: boundary for boundary in instrument.boundaries}


def readout_dict(instrument: Instrument) -> Dict[str, Readout]:
    return {readout.name: readout for readout in instrument.readouts}


def renamed_boundaries(name: str, dimension: int = 8) -> Tuple[Boundary, ...]:
    return tuple(Boundary(f"{name}:V{index}", dimension) for index in range(3))


def make_arrow(
    name: str,
    family: str,
    boundaries: Sequence[Boundary],
    source: int,
    target: int,
    amplitude: Matrix,
) -> Arrow:
    return Arrow(name, family, boundaries[source].name, boundaries[target].name, amplitude)


def build_amplitude_family() -> Mapping[str, object]:
    """Build the master first; regional subfamilies are restrictions of it."""

    qubits = 3
    hb = on_qubit(H, 0, qubits)
    ha = on_qubit(H, 2, qubits)
    cx_br = controlled_x(qubits, 0, 1)
    cx_ra = controlled_x(qubits, 1, 2)
    cx_ba = controlled_x(qubits, 0, 2)
    cx_ab = controlled_x(qubits, 2, 0)

    write = compose_chronological(hb, cx_br, cx_ra)
    no_write = hb
    uncopy = compose_chronological(cx_ra, cx_br)

    # Every preserving arrow leaves the record bit fixed.  The branch and
    # auxiliary are nevertheless coupled, and the shared write also couples
    # record to auxiliary.
    core_preserve = cx_ab
    regional_preserves = (
        cx_ba,
        compose_chronological(hb, cx_ba),
        compose_chronological(hb, ha, cx_ba),
    )
    eraser_posts = (
        regional_preserves[1],
        regional_preserves[2],
        compose_chronological(hb, cx_ba, ha, cx_ab),
    )
    erasers = tuple(
        compose_chronological(cx_ra, cx_br, post)
        for post in eraser_posts
    )

    master_boundaries = renamed_boundaries("E")
    master_arrows = [
        make_arrow("core.write", "write", master_boundaries, 0, 1, write),
        make_arrow("core.preserve", "preserve", master_boundaries, 1, 2, core_preserve),
        make_arrow("core.no-write", "control", master_boundaries, 0, 1, no_write),
    ]
    for index, (preserve, erase) in enumerate(zip(regional_preserves, erasers), start=1):
        master_arrows.extend(
            (
                make_arrow(
                    f"D{index}.preserve",
                    "preserve",
                    master_boundaries,
                    1,
                    2,
                    preserve,
                ),
                make_arrow(
                    f"D{index}.erase",
                    "erase",
                    master_boundaries,
                    1,
                    2,
                    erase,
                ),
            )
        )

    memory_values = tuple(bit_value(configuration, 1) for configuration in range(8))
    configuration_values = tuple(range(8))
    master = Instrument(
        name="E",
        boundaries=master_boundaries,
        arrows=tuple(master_arrows),
        preparations=tuple(range(8)),
        actual_preparation=0,
        readouts=(
            Readout("memory", master_boundaries[1].name, memory_values, True),
            Readout(
                "configuration-probe",
                master_boundaries[2].name,
                configuration_values,
                False,
            ),
        ),
        access_class="POSTULATE: all basis preparations and configuration probe",
        gauge_class="REAL-SIGN-GAUGE: common configuration relabelling x +/- boundary phases",
    )

    regions = []
    region_embeddings = []
    core_embeddings = []
    for index in range(1, 4):
        name = f"D{index}"
        boundaries = renamed_boundaries(name)
        arrows = (
            make_arrow("write", "write", boundaries, 0, 1, write),
            make_arrow("core-preserve", "preserve", boundaries, 1, 2, core_preserve),
            make_arrow(
                "regional-preserve",
                "preserve",
                boundaries,
                1,
                2,
                regional_preserves[index - 1],
            ),
            make_arrow("erase", "erase", boundaries, 1, 2, erasers[index - 1]),
            make_arrow("no-write", "control", boundaries, 0, 1, no_write),
        )
        region = Instrument(
            name=name,
            boundaries=boundaries,
            arrows=arrows,
            preparations=tuple(range(8)),
            actual_preparation=0,
            readouts=(
                Readout("memory", boundaries[1].name, memory_values, True),
                Readout(
                    "configuration-probe",
                    boundaries[2].name,
                    configuration_values,
                    False,
                ),
            ),
            access_class="POSTULATE: all basis preparations and configuration probe",
            gauge_class="REAL-SIGN-GAUGE: common configuration relabelling x +/- boundary phases",
        )
        regions.append(region)
        region_embeddings.append(
            InstrumentMorphism(
                name=f"j{index}:{name}->E",
                source=name,
                target="E",
                boundary_maps=tuple(
                    BoundaryMap(boundaries[slot].name, master_boundaries[slot].name, identity(8))
                    for slot in range(3)
                ),
                arrow_map=(
                    ("write", "core.write"),
                    ("core-preserve", "core.preserve"),
                    ("regional-preserve", f"D{index}.preserve"),
                    ("erase", f"D{index}.erase"),
                    ("no-write", "core.no-write"),
                ),
                readout_map=(("memory", "memory"), ("configuration-probe", "configuration-probe")),
            )
        )

    core_boundaries = renamed_boundaries("O")
    core = Instrument(
        name="O",
        boundaries=core_boundaries,
        arrows=(
            make_arrow("write", "write", core_boundaries, 0, 1, write),
            make_arrow("core-preserve", "preserve", core_boundaries, 1, 2, core_preserve),
            make_arrow("no-write", "control", core_boundaries, 0, 1, no_write),
        ),
        preparations=tuple(range(8)),
        actual_preparation=0,
        readouts=(
            Readout("memory", core_boundaries[1].name, memory_values, True),
            Readout(
                "configuration-probe",
                core_boundaries[2].name,
                configuration_values,
                False,
            ),
        ),
        access_class="POSTULATE: inherited core basis access",
        gauge_class="REAL-SIGN-GAUGE: inherited from regional embeddings",
    )
    for index, region in enumerate(regions, start=1):
        core_embeddings.append(
            InstrumentMorphism(
                name=f"i{index}:O->{region.name}",
                source="O",
                target=region.name,
                boundary_maps=tuple(
                    BoundaryMap(
                        core_boundaries[slot].name,
                        region.boundaries[slot].name,
                        identity(8),
                    )
                    for slot in range(3)
                ),
                arrow_map=(
                    ("write", "write"),
                    ("core-preserve", "core-preserve"),
                    ("no-write", "no-write"),
                ),
                readout_map=(("memory", "memory"), ("configuration-probe", "configuration-probe")),
            )
        )

    return {
        "master": master,
        "regions": tuple(regions),
        "core": core,
        "region_embeddings": tuple(region_embeddings),
        "core_embeddings": tuple(core_embeddings),
        "write": write,
        "core_preserve": core_preserve,
        "regional_preserves": regional_preserves,
        "erasers": erasers,
        "no_write": no_write,
    }


def candidate_record(instrument: Instrument) -> Readout:
    candidates = tuple(readout for readout in instrument.readouts if readout.record_candidate)
    if len(candidates) != 1:
        raise AssertionError("expected one frozen record candidate")
    return candidates[0]


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


def cut_coherence_stats(
    later: Matrix,
    earlier: Matrix,
    values: Sequence[Hashable],
) -> Mapping[str, int]:
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


def aggregate_by_values(
    shadow: Matrix,
    output_values: Sequence[Hashable],
) -> Matrix:
    labels = tuple(sorted(set(output_values)))
    return tuple(
        tuple(
            sum(
                (
                    shadow[output][input_configuration]
                    for output in range(len(shadow))
                    if output_values[output] == label
                ),
                ZERO,
            )
            for input_configuration in range(len(shadow[0]))
        )
        for label in labels
    )


def quotient_kernel(shadow: Matrix, values: Sequence[Hashable]) -> Optional[Matrix]:
    labels = tuple(sorted(set(values)))
    columns = []
    for input_label in labels:
        representatives = [index for index, value in enumerate(values) if value == input_label]
        profiles = []
        for representative in representatives:
            profiles.append(
                tuple(
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
            )
        if any(profile != profiles[0] for profile in profiles[1:]):
            return None
        columns.append(profiles[0])
    return tuple(
        tuple(columns[column][row] for column in range(len(columns)))
        for row in range(len(labels))
    )


def record_residual(write: Matrix, continuation: Matrix, readout: Readout) -> Optional[Matrix]:
    quotient = quotient_kernel(born(continuation), readout.values)
    if quotient is None:
        return None
    gamma10 = aggregate_by_values(born(write), readout.values)
    gamma20 = aggregate_by_values(born(matmul(continuation, write)), readout.values)
    return matsub(gamma20, matmul(quotient, gamma10))


def readout_law(write: Matrix, readout: Readout, preparation: int) -> Tuple[Tuple[Hashable, Q2], ...]:
    law: Dict[Hashable, Q2] = {}
    shadow = born(write)
    for configuration, value in enumerate(readout.values):
        probability = shadow[configuration][preparation]
        if not probability.is_zero():
            law[value] = law.get(value, ZERO) + probability
    return tuple(sorted(law.items()))


def readout_projector(readout: Readout, value: Hashable) -> Matrix:
    return diagonal(tuple(1 if item == value else 0 for item in readout.values))


def validate_morphism(
    morphism: InstrumentMorphism,
    source: Instrument,
    target: Instrument,
) -> Mapping[str, object]:
    if morphism.source != source.name or morphism.target != target.name:
        return {"ok": False, "reason": "object names"}
    source_boundaries = boundary_dict(source)
    target_boundaries = boundary_dict(target)
    source_arrows = arrow_dict(source)
    target_arrows = arrow_dict(target)
    source_readouts = readout_dict(source)
    target_readouts = readout_dict(target)
    boundary_maps = {
        row.source_boundary: row
        for row in morphism.boundary_maps
    }
    boundary_map_is_total = (
        len(morphism.boundary_maps) == len(source.boundaries)
        and len(boundary_maps) == len(source.boundaries)
        and set(boundary_maps) == set(source_boundaries)
        and len({row.target_boundary for row in morphism.boundary_maps})
        == len(morphism.boundary_maps)
    )
    boundary_rows = []
    for row in morphism.boundary_maps:
        source_boundary = source_boundaries.get(row.source_boundary)
        target_boundary = target_boundaries.get(row.target_boundary)
        boundary_rows.append(
            (
                row.source_boundary,
                row.target_boundary,
                source_boundary is not None,
                target_boundary is not None,
                source_boundary is not None
                and target_boundary is not None
                and len(row.amplitude) == target_boundary.dimension
                and len(row.amplitude[0]) == source_boundary.dimension,
                is_unitary(row.amplitude),
                is_signed_permutation(row.amplitude),
            )
        )

    arrow_rows = []
    for source_name, target_name in morphism.arrow_map:
        source_arrow = source_arrows.get(source_name)
        target_arrow = target_arrows.get(target_name)
        if source_arrow is None or target_arrow is None:
            arrow_rows.append((source_name, target_name, False, False, False))
            continue
        source_map = boundary_maps.get(source_arrow.source)
        target_map = boundary_maps.get(source_arrow.target)
        typed = (
            source_map is not None
            and target_map is not None
            and source_map.target_boundary == target_arrow.source
            and target_map.target_boundary == target_arrow.target
            and source_arrow.family == target_arrow.family
        )
        intertwines = bool(
            typed
            and matmul(target_map.amplitude, source_arrow.amplitude)
            == matmul(target_arrow.amplitude, source_map.amplitude)
        )
        arrow_rows.append((source_name, target_name, True, typed, intertwines))
    arrow_map_is_total = (
        len(morphism.arrow_map) == len(source.arrows)
        and len(dict(morphism.arrow_map)) == len(source.arrows)
        and set(dict(morphism.arrow_map)) == set(source_arrows)
        and len({target_name for _source_name, target_name in morphism.arrow_map})
        == len(morphism.arrow_map)
    )

    readout_rows = []
    for source_name, target_name in morphism.readout_map:
        source_readout = source_readouts.get(source_name)
        target_readout = target_readouts.get(target_name)
        if source_readout is None or target_readout is None:
            readout_rows.append((source_name, target_name, False, False))
            continue
        boundary_map = boundary_maps.get(source_readout.boundary)
        labels = tuple(sorted(set(source_readout.values)))
        pullback = bool(
            boundary_map is not None
            and boundary_map.target_boundary == target_readout.boundary
            and set(source_readout.values) == set(target_readout.values)
            and all(
                matmul(
                    transpose(boundary_map.amplitude),
                    matmul(
                        readout_projector(target_readout, value),
                        boundary_map.amplitude,
                    ),
                )
                == readout_projector(source_readout, value)
                for value in labels
            )
        )
        readout_rows.append((source_name, target_name, True, pullback))
    readout_map_is_total = (
        len(morphism.readout_map) == len(source.readouts)
        and len(dict(morphism.readout_map)) == len(source.readouts)
        and set(dict(morphism.readout_map)) == set(source_readouts)
        and len({target_name for _source_name, target_name in morphism.readout_map})
        == len(morphism.readout_map)
    )

    input_boundary = source.boundaries[0].name
    input_map = boundary_maps.get(input_boundary)
    preparation_rows = []
    if input_map is not None:
        for preparation in source.preparations:
            live = tuple(
                row
                for row in range(len(input_map.amplitude))
                if not input_map.amplitude[row][preparation].is_zero()
            )
            preparation_rows.append(
                (
                    preparation,
                    live,
                    len(live) == 1 and live[0] in target.preparations,
                )
            )
    actual_ok = bool(
        input_map is not None
        and tuple(
            row
            for row in range(len(input_map.amplitude))
            if not input_map.amplitude[row][source.actual_preparation].is_zero()
        )
        == (target.actual_preparation,)
    )
    gauge_compatible = (
        source.gauge_class.startswith("REAL-SIGN-GAUGE")
        and target.gauge_class.startswith("REAL-SIGN-GAUGE")
    )
    all_ok = (
        boundary_map_is_total
        and all(
            row[2] and row[3] and row[4] and row[5] and row[6]
            for row in boundary_rows
        )
        and arrow_map_is_total
        and all(row[2] and row[3] and row[4] for row in arrow_rows)
        and readout_map_is_total
        and all(row[2] and row[3] for row in readout_rows)
        and len(preparation_rows) == len(source.preparations)
        and all(row[2] for row in preparation_rows)
        and actual_ok
        and gauge_compatible
    )
    return {
        "boundary_rows": tuple(boundary_rows),
        "boundary_map_is_total": boundary_map_is_total,
        "arrow_rows": tuple(arrow_rows),
        "arrow_map_is_total": arrow_map_is_total,
        "readout_rows": tuple(readout_rows),
        "readout_map_is_total": readout_map_is_total,
        "preparation_rows": tuple(preparation_rows),
        "actual_preparation": actual_ok,
        "gauge_compatible": gauge_compatible,
        "ok": all_ok,
    }


def identity_morphism(instrument: Instrument) -> InstrumentMorphism:
    return InstrumentMorphism(
        name=f"id:{instrument.name}",
        source=instrument.name,
        target=instrument.name,
        boundary_maps=tuple(
            BoundaryMap(boundary.name, boundary.name, identity(boundary.dimension))
            for boundary in instrument.boundaries
        ),
        arrow_map=tuple((arrow.name, arrow.name) for arrow in instrument.arrows),
        readout_map=tuple((readout.name, readout.name) for readout in instrument.readouts),
    )


def sign_gauge_instrument(
    instrument: Instrument,
    signs: Mapping[str, Matrix],
) -> Instrument:
    """Apply the exact real boundary gauge U -> D_t U D_s^{-1}."""

    return Instrument(
        name=instrument.name,
        boundaries=instrument.boundaries,
        arrows=tuple(
            Arrow(
                arrow.name,
                arrow.family,
                arrow.source,
                arrow.target,
                matmul(signs[arrow.target], matmul(arrow.amplitude, signs[arrow.source])),
            )
            for arrow in instrument.arrows
        ),
        preparations=instrument.preparations,
        actual_preparation=instrument.actual_preparation,
        readouts=instrument.readouts,
        access_class=instrument.access_class,
        gauge_class=instrument.gauge_class,
    )


def sign_gauge_morphism(
    morphism: InstrumentMorphism,
    source_signs: Mapping[str, Matrix],
    target_signs: Mapping[str, Matrix],
) -> InstrumentMorphism:
    """Transform a boundary map f -> D_target f D_source^{-1}."""

    return InstrumentMorphism(
        name=morphism.name,
        source=morphism.source,
        target=morphism.target,
        boundary_maps=tuple(
            BoundaryMap(
                row.source_boundary,
                row.target_boundary,
                matmul(
                    target_signs[row.target_boundary],
                    matmul(row.amplitude, source_signs[row.source_boundary]),
                ),
            )
            for row in morphism.boundary_maps
        ),
        arrow_map=morphism.arrow_map,
        readout_map=morphism.readout_map,
    )


def relabel_instrument(instrument: Instrument, permutation: Sequence[int]) -> Instrument:
    """Apply one common carrier relabelling on every boundary."""

    inverse = {new: old for old, new in enumerate(permutation)}
    return Instrument(
        name=instrument.name,
        boundaries=instrument.boundaries,
        arrows=tuple(
            Arrow(
                arrow.name,
                arrow.family,
                arrow.source,
                arrow.target,
                conjugate_by_permutation(arrow.amplitude, permutation),
            )
            for arrow in instrument.arrows
        ),
        preparations=tuple(sorted(permutation[item] for item in instrument.preparations)),
        actual_preparation=permutation[instrument.actual_preparation],
        readouts=tuple(
            Readout(
                readout.name,
                readout.boundary,
                tuple(readout.values[inverse[index]] for index in range(len(permutation))),
                readout.record_candidate,
            )
            for readout in instrument.readouts
        ),
        access_class=instrument.access_class,
        gauge_class=instrument.gauge_class,
    )


def compose_morphisms(
    first: InstrumentMorphism,
    second: InstrumentMorphism,
    name: str,
) -> InstrumentMorphism:
    if first.target != second.source:
        raise ValueError("morphisms do not compose")
    second_boundaries = {
        row.source_boundary: row
        for row in second.boundary_maps
    }
    second_arrows = dict(second.arrow_map)
    second_readouts = dict(second.readout_map)
    return InstrumentMorphism(
        name=name,
        source=first.source,
        target=second.target,
        boundary_maps=tuple(
            BoundaryMap(
                row.source_boundary,
                second_boundaries[row.target_boundary].target_boundary,
                matmul(second_boundaries[row.target_boundary].amplitude, row.amplitude),
            )
            for row in first.boundary_maps
        ),
        arrow_map=tuple((source_name, second_arrows[target_name]) for source_name, target_name in first.arrow_map),
        readout_map=tuple(
            (source_name, second_readouts[target_name])
            for source_name, target_name in first.readout_map
        ),
    )


def morphism_signature(morphism: InstrumentMorphism) -> Tuple[object, ...]:
    return (
        morphism.source,
        morphism.target,
        tuple(
            (
                row.source_boundary,
                row.target_boundary,
                matrix_digest(row.amplitude),
            )
            for row in morphism.boundary_maps
        ),
        morphism.arrow_map,
        morphism.readout_map,
    )


def mapped_master_arrow_set(morphism: InstrumentMorphism) -> frozenset[str]:
    return frozenset(target for _source, target in morphism.arrow_map)


def regional_category(family: Mapping[str, object]) -> Mapping[str, object]:
    master = family["master"]
    regions = family["regions"]
    core = family["core"]
    region_embeddings = family["region_embeddings"]
    core_embeddings = family["core_embeddings"]
    core_to_master = tuple(
        compose_morphisms(core_embeddings[index], region_embeddings[index], f"k{index + 1}:O->E")
        for index in range(3)
    )
    core_signatures = tuple(morphism_signature(row) for row in core_to_master)

    object_sets = {
        "O": mapped_master_arrow_set(core_to_master[0]),
        **{
            region.name: mapped_master_arrow_set(region_embeddings[index])
            for index, region in enumerate(regions)
        },
        "E": frozenset(arrow.name for arrow in master.arrows),
    }
    objects = ("O", "D1", "D2", "D3", "E")
    instruments = {
        "O": core,
        **{region.name: region for region in regions},
        "E": master,
    }
    morphisms: Dict[Tuple[str, str], InstrumentMorphism] = {
        (name, name): identity_morphism(instrument)
        for name, instrument in instruments.items()
    }
    for index, region in enumerate(regions):
        morphisms[("O", region.name)] = core_embeddings[index]
        morphisms[(region.name, "E")] = region_embeddings[index]
    morphisms[("O", "E")] = core_to_master[0]
    order = tuple(
        (source, target)
        for source in objects
        for target in objects
        if object_sets[source].issubset(object_sets[target])
    )
    identities = tuple((name, name) in order for name in objects)
    antisymmetry = tuple(
        not ((left, right) in order and (right, left) in order) or left == right
        for left in objects
        for right in objects
    )
    transitivity = tuple(
        (left, right) not in order
        or (right, destination) not in order
        or (left, destination) in order
        for left in objects
        for right in objects
        for destination in objects
    )
    composition_laws = tuple(
        morphism_signature(
            compose_morphisms(first, second, "composition-check")
        )
        == morphism_signature(morphisms[(first.source, second.target)])
        for first in morphisms.values()
        for second in morphisms.values()
        if first.target == second.source
    )
    pair_overlaps = tuple(
        object_sets[regions[left].name].intersection(object_sets[regions[right].name])
        for left, right in ((0, 1), (1, 2), (0, 2))
    )
    triple_overlap = set.intersection(
        *(set(object_sets[region.name]) for region in regions)
    )
    cover_union = set.union(
        *(set(object_sets[region.name]) for region in regions)
    )
    pullback_universal = tuple(
        all(
            not (
                object_sets[candidate].issubset(object_sets[left])
                and object_sets[candidate].issubset(object_sets[right])
            )
            or object_sets[candidate].issubset(object_sets["O"])
            for candidate in objects
        )
        for left, right in (("D1", "D2"), ("D2", "D3"), ("D1", "D3"))
    )
    reg = RegCategory(
        objects=objects,
        morphisms=tuple(morphisms[key] for key in order),
        cover=("D1->E", "D2->E", "D3->E"),
        overlap="O",
    )
    return {
        "Reg": reg,
        "objects": objects,
        "object_arrow_sets": object_sets,
        "order_arrows": order,
        "morphisms": morphisms,
        "morphism_keys_match_order": set(morphisms) == set(order),
        "all_morphisms_valid": all(
            validate_morphism(morphism, instruments[source], instruments[target])["ok"]
            for (source, target), morphism in morphisms.items()
        ),
        "identities": identities,
        "antisymmetry": antisymmetry,
        "transitivity": transitivity,
        "composition_laws": composition_laws,
        "core_to_master": core_to_master,
        "core_composites_equal": len(set(core_signatures)) == 1,
        "pair_overlaps": pair_overlaps,
        "triple_overlap": frozenset(triple_overlap),
        "pullback_universal": pullback_universal,
        "cover_union": frozenset(cover_union),
        "cover_is_master": cover_union == set(object_sets["E"]),
        "all_category_laws": (
            all(identities)
            and all(antisymmetry)
            and all(transitivity)
            and all(composition_laws)
            and set(morphisms) == set(order)
        ),
    }


def induced_record_pullback(
    morphism: InstrumentMorphism,
    source: Instrument,
    target: Instrument,
) -> Optional[Tuple[Tuple[int, int], ...]]:
    readout_pair = dict(morphism.readout_map)
    if "memory" not in readout_pair:
        return None
    source_readout = readout_dict(source)["memory"]
    target_readout = readout_dict(target)[readout_pair["memory"]]
    boundary_map = {
        row.source_boundary: row
        for row in morphism.boundary_maps
    }[source_readout.boundary]
    mapping = []
    for target_value in sorted(set(target_readout.values)):
        pulled = matmul(
            transpose(boundary_map.amplitude),
            matmul(
                readout_projector(target_readout, target_value),
                boundary_map.amplitude,
            ),
        )
        matches = tuple(
            source_value
            for source_value in sorted(set(source_readout.values))
            if readout_projector(source_readout, source_value) == pulled
        )
        if len(matches) != 1:
            return None
        mapping.append((target_value, matches[0]))
    return tuple(mapping)


def record_functor(
    family: Mapping[str, object],
    category: Mapping[str, object],
) -> Mapping[str, object]:
    instruments = {
        "O": family["core"],
        **{region.name: region for region in family["regions"]},
        "E": family["master"],
    }
    algebras = {}
    fact_algebras = []
    for name, instrument in instruments.items():
        record = candidate_record(instrument)
        write_name = "core.write" if name == "E" else "write"
        write = arrow_dict(instrument)[write_name].amplitude
        preserve_names = tuple(
            arrow.name
            for arrow in instrument.arrows
            if arrow.family == "preserve"
        )
        occurred = h_corr(write, record, instrument.preparations)
        available = tuple(
            (arrow_name, h_avail(arrow_dict(instrument)[arrow_name].amplitude, record))
            for arrow_name in preserve_names
        )
        generator = "memory" if occurred and all(row[1] for row in available) else None
        values = tuple(sorted(set(record.values)))
        algebras[name] = {
            "generator": generator,
            "occurred": occurred,
            "availability": available,
            "values": values,
        }
        fact_algebras.append(FactAlgebra(f"R({name})", name, generator, values))
    induced_arrows = tuple(
        (
            source,
            target,
            induced_record_pullback(
                category["morphisms"][(source, target)],
                instruments[source],
                instruments[target],
            ),
        )
        for source, target in category["order_arrows"]
    )
    functor_identity = tuple(
        row[2] == ((0, 0), (1, 1))
        for row in induced_arrows
        if row[0] == row[1]
    )
    arrow_map = {
        (source, target): dict(mapping)
        for source, target, mapping in induced_arrows
        if mapping is not None
    }
    functor_composition = tuple(
        (left, middle) not in arrow_map
        or (middle, right) not in arrow_map
        or {
            value: arrow_map[(left, middle)][arrow_map[(middle, right)][value]]
            for value in (0, 1)
        }
        == arrow_map[(left, right)]
        for left in category["objects"]
        for middle in category["objects"]
        for right in category["objects"]
    )
    core_maps = tuple(arrow_map[("O", f"D{index}")] for index in range(1, 4))
    fact_morphisms = tuple(
        FactMorphism(
            name=f"Rec({category['morphisms'][(source, target)].name})",
            reg_morphism=category["morphisms"][(source, target)].name,
            source=f"R({target})",
            target=f"R({source})",
            value_map=tuple(mapping or ()),
        )
        for source, target, mapping in induced_arrows
    )
    fact_iface = FactIfaceCategory(tuple(fact_algebras), fact_morphisms)
    rec = RecordFunctor(
        variance="CONTRAVARIANT",
        object_map=tuple((name, f"R({name})") for name in category["objects"]),
        arrow_map=tuple(
            (
                category["morphisms"][(source, target)].name,
                f"Rec({category['morphisms'][(source, target)].name})",
            )
            for source, target in category["order_arrows"]
        ),
    )
    direct_core_master = arrow_map[("O", "E")]
    path_core_master = tuple(
        {
            value: arrow_map[("O", f"D{index}")][arrow_map[(f"D{index}", "E")][value]]
            for value in (0, 1)
        }
        for index in range(1, 4)
    )
    return {
        "FactIface": fact_iface,
        "Rec": rec,
        "algebras": algebras,
        "induced_arrows": induced_arrows,
        "all_induced_from_morphisms": all(row[2] is not None for row in induced_arrows),
        "identity_laws": functor_identity,
        "composition_laws": functor_composition,
        "core_maps": core_maps,
        "triple_descends": len({tuple(sorted(row.items())) for row in core_maps}) == 1,
        "direct_core_master": direct_core_master,
        "path_core_master": path_core_master,
        "triple_path_law": all(row == direct_core_master for row in path_core_master),
        "all_functor_laws": all(functor_identity) and all(functor_composition),
    }


def permutation_matrix(permutation: Sequence[int]) -> Matrix:
    size = len(permutation)
    out = [[ZERO for _column in range(size)] for _row in range(size)]
    for old, new in enumerate(permutation):
        out[new][old] = ONE
    return tuple(tuple(row) for row in out)


def conjugate_by_permutation(value: Matrix, permutation: Sequence[int]) -> Matrix:
    size = len(permutation)
    out = [[ZERO for _column in range(size)] for _row in range(size)]
    for old_row, new_row in enumerate(permutation):
        for old_column, new_column in enumerate(permutation):
            out[new_row][new_column] = value[old_row][old_column]
    return tuple(tuple(row) for row in out)


def kronecker_rank_one_2x4(value: Matrix) -> bool:
    rearranged = tuple(
        tuple(
            value[2 * left_output + right_output][2 * left_input + right_input]
            for right_output in range(2)
            for right_input in range(2)
        )
        for left_output in range(4)
        for left_input in range(4)
    )
    pivot = next(
        (
            (row, column)
            for row in range(len(rearranged))
            for column in range(len(rearranged[0]))
            if not rearranged[row][column].is_zero()
        ),
        None,
    )
    if pivot is None:
        return True
    pivot_row, pivot_column = pivot
    pivot_value = rearranged[pivot_row][pivot_column]
    return all(
        rearranged[row][column] * pivot_value
        == rearranged[row][pivot_column] * rearranged[pivot_row][column]
        for row in range(len(rearranged))
        for column in range(len(rearranged[0]))
    )


def simultaneous_product_search(arrows: Sequence[Matrix]) -> Mapping[str, object]:
    tested = 0
    for permutation in itertools.permutations(range(8)):
        tested += 1
        if all(
            kronecker_rank_one_2x4(conjugate_by_permutation(arrow, permutation))
            for arrow in arrows
        ):
            return {
                "factor_found": True,
                "permutations_tested": tested,
                "witness": tuple(permutation),
            }
    return {
        "factor_found": False,
        "permutations_tested": tested,
        "witness": None,
    }


def old_padded_negative() -> Tuple[Matrix, ...]:
    """Exact q=3 member of commit #12's tensor-padded family."""

    old_write = compose_chronological(on_qubit(H, 0, 2), controlled_x(2, 0, 1))
    old_preserve = on_qubit(H, 0, 2)
    old_erase = compose_chronological(controlled_x(2, 0, 1), old_preserve)
    old_no_write = on_qubit(H, 0, 2)
    return (
        kron(old_write, I2),
        kron(old_preserve, H),
        kron(old_erase, H),
        kron(old_no_write, I2),
    )


def region_dynamic_signature(region: Instrument) -> Tuple[object, ...]:
    arrows = arrow_dict(region)
    write = arrows["write"].amplitude
    preserves = tuple(
        arrow.amplitude
        for arrow in region.arrows
        if arrow.family == "preserve"
    )
    erase = arrows["erase"].amplitude
    return (
        len(write),
        tuple(sorted(nonzero_count(preserve) for preserve in preserves)),
        tuple(
            sorted(nonzero_count(matmul(preserve, write)) for preserve in preserves)
        ),
        nonzero_count(erase),
        nonzero_count(defect(erase, write)),
        tuple(
            sorted(
                hashlib.sha256(
                    ";".join(born_multiset(matmul(preserve, write))).encode()
                ).hexdigest()
                for preserve in preserves
            )
        ),
    )


def build_equal_law_control(name: str, flip_record: Optional[int]) -> Instrument:
    """Build a typed 16-dimensional equal-law control instrument."""

    qubits = 4
    write = on_qubit(H, 0, qubits)
    for record_bit in (1, 2, 3):
        write = matmul(controlled_x(qubits, 0, record_bit), write)
    if flip_record is not None:
        write = matmul(on_qubit(X, flip_record, qubits), write)
    preserve = on_qubit(H, 0, qubits)
    boundaries = renamed_boundaries(name, dimension=16)
    joint_values = tuple(
        tuple(bit_value(configuration, bit, qubits) for bit in (1, 2, 3))
        for configuration in range(2 ** qubits)
    )
    return Instrument(
        name=name,
        boundaries=boundaries,
        arrows=(
            make_arrow("write", "write", boundaries, 0, 1, write),
            make_arrow("preserve", "preserve", boundaries, 1, 2, preserve),
        ),
        preparations=(0,),
        actual_preparation=0,
        readouts=(
            Readout("joint-memory", boundaries[1].name, joint_values, True),
            Readout("configuration-probe", boundaries[2].name, tuple(range(16)), False),
        ),
        access_class="CONTROL: actual preparation 0 and exact joint-record readout",
        gauge_class="REAL-SIGN-GAUGE: candidate signed-permutation identification",
    )


def equal_law_control_measurements(control: Instrument) -> Mapping[str, object]:
    arrows = arrow_dict(control)
    write = arrows["write"].amplitude
    preserve = arrows["preserve"].amplitude
    readout = candidate_record(control)
    support = tuple(
        sorted(
            {
                readout.values[configuration]
                for configuration in range(len(write))
                if not write[configuration][control.actual_preparation].is_zero()
            }
        )
    )
    joint_law = readout_law(write, readout, control.actual_preparation)
    component_count = len(readout.values[0])
    marginals = tuple(
        tuple(
            (
                value,
                sum(
                    (
                        probability
                        for joint_value, probability in joint_law
                        if joint_value[index] == value
                    ),
                    ZERO,
                ),
            )
            for value in (0, 1)
        )
        for index in range(component_count)
    )
    return {
        "instrument": control,
        "dimension": control.boundaries[0].dimension,
        "support": support,
        "joint_law": joint_law,
        "marginals": marginals,
        "h_corr": h_corr(write, readout, control.preparations),
        "h_avail": h_avail(preserve, readout),
    }


def equal_law_bridge_candidate(
    control: Instrument,
    master: Instrument,
) -> InstrumentMorphism:
    """An explicit attempted control-to-master bridge in the admitted schema."""

    return InstrumentMorphism(
        name=f"candidate:{control.name}->{master.name}",
        source=control.name,
        target=master.name,
        boundary_maps=tuple(
            BoundaryMap(
                source_boundary.name,
                target_boundary.name,
                rectangular_basis_map(
                    target_boundary.dimension,
                    source_boundary.dimension,
                ),
            )
            for source_boundary, target_boundary in zip(
                control.boundaries,
                master.boundaries,
            )
        ),
        arrow_map=(("write", "core.write"), ("preserve", "core.preserve")),
        readout_map=(("joint-memory", "memory"), ("configuration-probe", "configuration-probe")),
    )


def validate_candidate_bridge(
    morphism: InstrumentMorphism,
    source: Instrument,
    target: Instrument,
) -> Mapping[str, object]:
    """Fail at the first structural obstruction in the frozen morphism class."""

    dimension_rows = tuple(
        (
            source_boundary.name,
            source_boundary.dimension,
            target_boundary.name,
            target_boundary.dimension,
            source_boundary.dimension == target_boundary.dimension,
        )
        for source_boundary, target_boundary in zip(source.boundaries, target.boundaries)
    )
    dimensions_match = (
        len(source.boundaries) == len(target.boundaries)
        and all(row[4] for row in dimension_rows)
    )
    if not dimensions_match:
        return {
            "candidate_is_instrument_morphism": isinstance(morphism, InstrumentMorphism),
            "dimension_rows": dimension_rows,
            "dimensions_match": False,
            "full_validator_called": False,
            "accepted": False,
            "reason": "boundary_dimension_mismatch",
        }
    diagnostics = validate_morphism(morphism, source, target)
    return {
        "candidate_is_instrument_morphism": isinstance(morphism, InstrumentMorphism),
        "dimension_rows": dimension_rows,
        "dimensions_match": True,
        "full_validator_called": True,
        "accepted": diagnostics["ok"],
        "reason": "accepted" if diagnostics["ok"] else "morphism_diagram_failure",
        "diagnostics": diagnostics,
    }


def forced_binary_maps(triple_support: Sequence[Tuple[int, int, int]]) -> Mapping[str, object]:
    pairs = ((0, 1), (1, 2), (0, 2))
    rows = []
    for source, target in pairs:
        pair_support = frozenset((row[source], row[target]) for row in triple_support)
        maps = []
        for image in itertools.permutations((0, 1)):
            mapping = {0: image[0], 1: image[1]}
            if all((value, mapping[value]) in pair_support for value in (0, 1)):
                maps.append(tuple(sorted(mapping.items())))
        rows.append(tuple(maps))
    return {
        "families": tuple(rows),
        "unique": all(len(row) == 1 for row in rows),
        "maps": tuple(row[0] if len(row) == 1 else None for row in rows),
    }


def build_equal_law_rogue(reference: Instrument) -> Instrument:
    boundaries = renamed_boundaries("N")
    source_arrows = arrow_dict(reference)
    rotation = matrix(
        (
            (Fraction(3, 5), Fraction(4, 5)),
            (Fraction(4, 5), Fraction(-3, 5)),
        )
    )
    rotation_b = on_qubit(rotation, 0, 3)
    cx_ba = controlled_x(3, 0, 2)
    cx_ra = controlled_x(3, 1, 2)
    cx_br = controlled_x(3, 0, 1)
    rogue_preserve = compose_chronological(rotation_b, cx_ba)
    rogue_erase = compose_chronological(cx_ra, cx_br, rogue_preserve)
    memory_values = tuple(bit_value(configuration, 1) for configuration in range(8))
    configuration_values = tuple(range(8))
    return Instrument(
        name="N",
        boundaries=boundaries,
        arrows=(
            make_arrow("write", "write", boundaries, 0, 1, source_arrows["write"].amplitude),
            make_arrow(
                "core-preserve",
                "preserve",
                boundaries,
                1,
                2,
                source_arrows["core-preserve"].amplitude,
            ),
            make_arrow(
                "regional-preserve",
                "preserve",
                boundaries,
                1,
                2,
                rogue_preserve,
            ),
            make_arrow("erase", "erase", boundaries, 1, 2, rogue_erase),
            make_arrow(
                "no-write",
                "control",
                boundaries,
                0,
                1,
                source_arrows["no-write"].amplitude,
            ),
        ),
        preparations=tuple(range(8)),
        actual_preparation=0,
        readouts=(
            Readout("memory", boundaries[1].name, memory_values, True),
            Readout("configuration-probe", boundaries[2].name, configuration_values, False),
        ),
        access_class="POSTULATE: same access scope as positive regions",
        gauge_class="REAL-SIGN-GAUGE: candidate for exhaustive-invariant rejection",
    )


def rogue_bridge_invariant(
    rogue: Instrument,
    master: Instrument,
) -> Mapping[str, object]:
    rogue_arrow = arrow_dict(rogue)["regional-preserve"]
    candidates = tuple(
        arrow
        for arrow in master.arrows
        if arrow.family == rogue_arrow.family
    )
    rogue_multiset = born_multiset(rogue_arrow.amplitude)
    rows = tuple(
        (
            arrow.name,
            born_multiset(arrow.amplitude) == rogue_multiset,
            nonzero_count(arrow.amplitude),
        )
        for arrow in candidates
    )
    return {
        "same_law": readout_law(
            arrow_dict(rogue)["write"].amplitude,
            candidate_record(rogue),
            rogue.actual_preparation,
        ),
        "candidate_rows": rows,
        "invariant_match": any(row[1] for row in rows),
        "bridge_exists": any(row[1] for row in rows),
        "reason": "Born-entry multiset is invariant under signed row/column relabelling",
    }


def canonical_master_spec(family: Mapping[str, object]) -> Mapping[str, object]:
    def instrument_spec(instrument: Instrument) -> Mapping[str, object]:
        return {
            "name": instrument.name,
            "boundaries": tuple((row.name, row.dimension) for row in instrument.boundaries),
            "arrows": tuple(
                (
                    arrow.name,
                    arrow.family,
                    arrow.source,
                    arrow.target,
                    matrix_digest(arrow.amplitude),
                )
                for arrow in instrument.arrows
            ),
            "preparations": instrument.preparations,
            "actual_preparation": instrument.actual_preparation,
            "readouts": tuple(
                (
                    readout.name,
                    readout.boundary,
                    readout.values,
                    readout.record_candidate,
                )
                for readout in instrument.readouts
            ),
            "access_class": instrument.access_class,
            "gauge_class": instrument.gauge_class,
        }

    def morphism_spec(morphism: InstrumentMorphism) -> Mapping[str, object]:
        return {
            "name": morphism.name,
            "source": morphism.source,
            "target": morphism.target,
            "boundary_maps": tuple(
                (
                    row.source_boundary,
                    row.target_boundary,
                    matrix_digest(row.amplitude),
                )
                for row in morphism.boundary_maps
            ),
            "arrow_map": morphism.arrow_map,
            "readout_map": morphism.readout_map,
        }

    return {
        "admissible_extension_class": (
            "fixed-carrier amplitude-subinstrument inclusions",
            "typed boundary maps",
            "signed-permutation boundary maps",
            "family-preserving injective arrow maps",
            "exact intertwiners",
            "preparation compatibility",
            "projector pullbacks",
            "real-sign gauge compatibility",
        ),
        "master": instrument_spec(family["master"]),
        "core": instrument_spec(family["core"]),
        "regions": tuple(instrument_spec(region) for region in family["regions"]),
        "region_embeddings": tuple(
            morphism_spec(morphism) for morphism in family["region_embeddings"]
        ),
        "core_embeddings": tuple(
            morphism_spec(morphism) for morphism in family["core_embeddings"]
        ),
    }


def master_spec_digest(family: Mapping[str, object]) -> str:
    payload = json.dumps(json_ready(canonical_master_spec(family)), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def constructor_static_audit(path: Path) -> Mapping[str, object]:
    tree = ast.parse(path.read_text())
    forbidden = {
        "target_law",
        "marginal_law",
        "fact_map",
        "requested_identity",
        "metric",
        "coordinates",
        "field_propagator",
    }
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "build_amplitude_family":
            names = {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}
            return {
                "arguments": tuple(argument.arg for argument in node.args.args),
                "forbidden_names": tuple(sorted(names.intersection(forbidden))),
            }
    raise AssertionError("master constructor not found")


def construction_surface_digest(path: Path) -> str:
    source = path.read_text()
    tree = ast.parse(source)
    frozen_names = {
        "Boundary",
        "Arrow",
        "Readout",
        "Instrument",
        "BoundaryMap",
        "InstrumentMorphism",
        "build_amplitude_family",
        "validate_morphism",
        "canonical_master_spec",
        "matches_canonical_spec",
        "validate_structural_bridge",
        "build_equal_law_control",
        "rectangular_basis_map",
        "equal_law_bridge_candidate",
        "validate_candidate_bridge",
    }
    rows = []
    for node in tree.body:
        if isinstance(node, (ast.ClassDef, ast.FunctionDef)) and node.name in frozen_names:
            segment = ast.get_source_segment(source, node)
            if segment is None:
                raise AssertionError(f"cannot recover source for {node.name}")
            rows.append((node.name, segment))
    if {name for name, _segment in rows} != frozen_names:
        raise AssertionError("construction surface is incomplete")
    payload = "\n\n".join(name + "\n" + segment for name, segment in rows)
    return hashlib.sha256(payload.encode()).hexdigest()


def record_functor_static_audit(path: Path) -> Mapping[str, object]:
    tree = ast.parse(path.read_text())
    forbidden = {
        "readout_law",
        "build_equal_law_control",
        "equal_law_control_measurements",
        "forced_binary_maps",
        "marginal_law",
        "joint_law",
        "law_only_accepts",
    }
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "record_functor":
            names = {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}
            return {
                "forbidden_names": tuple(sorted(names.intersection(forbidden))),
                "uses_induced_record_pullback": "induced_record_pullback" in names,
                "uses_h_corr": "h_corr" in names,
                "uses_h_avail": "h_avail" in names,
            }
    raise AssertionError("record_functor not found")


def exactness_static_audit(path: Path) -> Mapping[str, object]:
    tree = ast.parse(path.read_text())
    float_literals = tuple(
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    )
    imported = tuple(
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    )
    return {
        "float_literals": float_literals,
        "random_imports": tuple(name for name in imported if "random" in name),
        "numpy_imports": tuple(name for name in imported if "numpy" in name),
    }


def law_only_accepts(
    regional_laws: Sequence[Tuple[Tuple[Hashable, Q2], ...]],
    control: Instrument,
) -> bool:
    """Deliberately inadequate control: marginals alone decide."""

    return tuple(regional_laws) == tuple(
        equal_law_control_measurements(control)["marginals"]
    )


def matches_canonical_spec(
    family: Mapping[str, object],
    canonical_digest: str,
) -> bool:
    """Same-file canonical authentication, not historical preregistration."""

    required = {"master", "regions", "core", "region_embeddings", "core_embeddings"}
    if not isinstance(family, Mapping) or not required.issubset(family):
        return False
    return master_spec_digest(family) == canonical_digest


def validate_structural_bridge(family: Mapping[str, object]) -> Mapping[str, object]:
    """Validate the family structurally without consulting its canonical digest."""

    required = {"master", "regions", "core", "region_embeddings", "core_embeddings"}
    if not isinstance(family, Mapping) or not required.issubset(family):
        return {
            "schema_complete": False,
            "region_rows": (),
            "core_rows": (),
            "ok": False,
            "reason": "family_schema_incomplete",
        }
    master = family["master"]
    region_rows = tuple(
        validate_morphism(morphism, region, master)
        for region, morphism in zip(family["regions"], family["region_embeddings"])
    )
    core_rows = tuple(
        validate_morphism(morphism, family["core"], region)
        for region, morphism in zip(family["regions"], family["core_embeddings"])
    )
    cardinalities_ok = (
        len(family["regions"]) == 3
        and len(region_rows) == len(family["regions"])
        and len(core_rows) == len(family["regions"])
    )
    ok = cardinalities_ok and all(row["ok"] for row in region_rows + core_rows)
    return {
        "schema_complete": True,
        "cardinalities_ok": cardinalities_ok,
        "region_rows": region_rows,
        "core_rows": core_rows,
        "ok": ok,
        "reason": "accepted" if ok else "morphism_diagram_failure",
    }


def mutate_mapped_arrow(morphism: InstrumentMorphism) -> InstrumentMorphism:
    """One-arrow falsification control for the morphism gate."""

    mutated = []
    changed = False
    for source_name, target_name in morphism.arrow_map:
        if source_name == "regional-preserve":
            mutated.append((source_name, "core.preserve"))
            changed = True
        else:
            mutated.append((source_name, target_name))
    if not changed:
        raise AssertionError("regional-preserve arrow not found")
    return InstrumentMorphism(
        name=morphism.name + ":MUTATED",
        source=morphism.source,
        target=morphism.target,
        boundary_maps=morphism.boundary_maps,
        arrow_map=tuple(mutated),
        readout_map=morphism.readout_map,
    )


def is_reg_category(candidate: object) -> bool:
    return bool(
        isinstance(candidate, RegCategory)
        and all(isinstance(row, InstrumentMorphism) for row in candidate.morphisms)
    )


def is_fact_iface_category(candidate: object) -> bool:
    return bool(
        isinstance(candidate, FactIfaceCategory)
        and all(isinstance(row, FactAlgebra) for row in candidate.objects)
        and all(isinstance(row, FactMorphism) for row in candidate.morphisms)
    )


def value_only_fact_groupoid() -> FactIfaceCategory:
    """Commit #12's value-level shape, retained only as a type control."""

    objects = tuple(
        FactAlgebra(f"R(D{index})", f"D{index}", "memory", (0, 1))
        for index in range(1, 4)
    )
    arrows = tuple(
        FactMorphism(
            name=f"value:D{source}->D{target}",
            reg_morphism="ABSENT:VALUE-ONLY",
            source=f"R(D{target})",
            target=f"R(D{source})",
            value_map=((0, 0), (1, 1)),
        )
        for source in range(1, 4)
        for target in range(1, 4)
    )
    return FactIfaceCategory(objects, arrows)


def value_only_groupoid_laws(candidate: FactIfaceCategory) -> Mapping[str, object]:
    names = tuple(row.name for row in candidate.objects)
    lookup = {(row.source, row.target): dict(row.value_map) for row in candidate.morphisms}
    identities = tuple(
        lookup[(name, name)] == {0: 0, 1: 1}
        for name in names
    )
    inverses = tuple(
        {
            value: lookup[(target, source)][lookup[(source, target)][value]]
            for value in (0, 1)
        }
        == {0: 0, 1: 1}
        for source in names
        for target in names
    )
    compositions = tuple(
        {
            value: lookup[(middle, target)][lookup[(source, middle)][value]]
            for value in (0, 1)
        }
        == lookup[(source, target)]
        for source in names
        for middle in names
        for target in names
    )
    return {
        "identity_count": len(identities),
        "inverse_count": len(inverses),
        "composition_count": len(compositions),
        "all_laws": all(identities) and all(inverses) and all(compositions),
    }


def is_instrument_refinement(
    candidate: object,
    instruments: Mapping[str, Instrument],
) -> bool:
    return bool(
        isinstance(candidate, InstrumentMorphism)
        and candidate.source in instruments
        and candidate.target in instruments
        and validate_morphism(
            candidate,
            instruments[candidate.source],
            instruments[candidate.target],
        )["ok"]
    )


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


CHECK_CATEGORIES = (
    "anchor",
    "authentication",
    "static",
    "type",
    "schema",
    "measurement",
    "control",
    "semantic",
)


class Checks:
    def __init__(self, emit: bool, mutant: bool) -> None:
        self.emit = emit
        self.mutant = mutant
        self.rows = []
        self.results: Dict[str, bool] = {}

    def section(self, title: str) -> None:
        if self.emit:
            print("\n" + title)

    def observed_anchor(self, label: str, observed: str) -> str:
        if self.mutant and label == "physical-overlap repair pin hash":
            if self.emit:
                print("[MUTANT] deliberately corrupting observed active-pin state")
            return "0" * len(observed)
        return observed

    def check(
        self,
        label: str,
        computed: object,
        expected: object,
        *,
        category: str = "measurement",
        key: Optional[str] = None,
    ) -> bool:
        if category not in CHECK_CATEGORIES:
            raise ValueError(f"unknown check category: {category}")
        result_key = key or label
        if result_key in self.results:
            raise ValueError(f"duplicate check key: {result_key}")
        ok = computed == expected
        self.results[result_key] = ok
        self.rows.append(
            {
                "key": result_key,
                "category": category,
                "label": label,
                "computed": json_ready(computed),
                "expected": json_ready(expected),
                "ok": ok,
            }
        )
        if self.emit:
            print(f"[{'PASS' if ok else 'FAIL'}] {label}: {json_ready(computed)!r}")
        return ok

    def summary(self) -> Mapping[str, object]:
        failures = sum(not row["ok"] for row in self.rows)
        category_rows = {
            category: tuple(row for row in self.rows if row["category"] == category)
            for category in CHECK_CATEGORIES
        }
        return {
            "checks": len(self.rows),
            "pass": len(self.rows) - failures,
            "fail": failures,
            "by_category": {
                category: {
                    "checks": len(rows),
                    "pass": sum(row["ok"] for row in rows),
                    "fail": sum(not row["ok"] for row in rows),
                }
                for category, rows in category_rows.items()
            },
        }


def build_science(checks: Checks) -> Mapping[str, object]:
    code_path = ROOT / "v13/code/rq0_physical_overlap_exact.py"

    checks.section("ANCHORS, CANONICAL AUTHENTICATION, AND EXACTNESS")
    pin_ancestor = run(("/usr/bin/git", "merge-base", "--is-ancestor", PIN_COMMIT, "HEAD"))
    checks.check(
        "repair pin commit is an ancestor of HEAD",
        pin_ancestor.returncode,
        0,
        category="anchor",
        key="anchor.pin_commit",
    )
    commit_rows = tuple(
        (
            commit,
            run(("/usr/bin/git", "cat-file", "-e", commit + "^{commit}")).returncode,
            run(("/usr/bin/git", "merge-base", "--is-ancestor", commit, "HEAD")).returncode,
        )
        for commit in PROVENANCE_COMMITS
    )
    checks.check(
        "reviewed and adjudication commits are immutable ancestors",
        commit_rows,
        tuple((commit, 0, 0) for commit in PROVENANCE_COMMITS),
        category="anchor",
        key="anchor.provenance_commits",
    )
    observed_pin_hash = checks.observed_anchor(
        "physical-overlap repair pin hash",
        sha256(ROOT / LOCKS["physical-overlap repair pin"][0]),
    )
    checks.check(
        "physical-overlap repair pin hash",
        observed_pin_hash,
        PIN_SHA256,
        category="anchor",
        key="anchor.active_pin_hash",
    )
    lock_rows = tuple(
        (name, sha256(ROOT / relative) == expected, use_class)
        for name, (relative, expected, use_class) in LOCKS.items()
        if name != "physical-overlap repair pin"
    )
    checks.check(
        "all other binding files are hash-locked with declared use classes",
        lock_rows,
        tuple(
            (name, True, use_class)
            for name, (_relative, _expected, use_class) in LOCKS.items()
            if name != "physical-overlap repair pin"
        ),
        category="anchor",
        key="anchor.binding_files",
    )
    constructor_audit = constructor_static_audit(code_path)
    checks.check(
        "master constructor consumes no comparison target",
        constructor_audit,
        {"arguments": (), "forbidden_names": ()},
        category="static",
        key="static.constructor_law_blind",
    )
    observed_surface_digest = construction_surface_digest(code_path)
    checks.check(
        "constructor, typed controls, and bridge validators are canonically authenticated",
        observed_surface_digest,
        CONSTRUCTION_SURFACE_SHA256,
        category="authentication",
        key="authentication.construction_surface",
    )
    exactness_audit = exactness_static_audit(code_path)
    checks.check(
        "substantive code has no float, random, or numpy path",
        exactness_audit,
        {"float_literals": (), "random_imports": (), "numpy_imports": ()},
        category="static",
        key="static.exactness",
    )

    # The family is built before any record law or equal-law control is
    # evaluated.  Its digest is a same-file canonical authenticator, not
    # evidence of historical independent preregistration.
    family = build_amplitude_family()
    frozen_digest = master_spec_digest(family)
    checks.check(
        "fixed canonical master/morphism specification matches",
        (frozen_digest, matches_canonical_spec(family, MASTER_SPEC_SHA256)),
        (MASTER_SPEC_SHA256, True),
        category="authentication",
        key="authentication.master_spec",
    )
    structural_family = validate_structural_bridge(family)
    checks.check(
        "structural bridge validator accepts the fixed family independently of its digest",
        structural_family["ok"],
        True,
        category="control",
        key="control.positive_structural_family",
    )
    rec_audit = record_functor_static_audit(code_path)
    checks.check(
        "Rec is law-blind and derives restrictions from morphisms",
        rec_audit,
        {
            "forbidden_names": (),
            "uses_induced_record_pullback": True,
            "uses_h_corr": True,
            "uses_h_avail": True,
        },
        category="static",
        key="static.record_functor_law_blind",
    )

    master = family["master"]
    regions = family["regions"]
    core = family["core"]
    instruments = {
        "O": core,
        **{region.name: region for region in regions},
        "E": master,
    }

    checks.section("EQUAL-DIMENSIONAL QUANTUM REGIONS")
    checks.check(
        "three regions and the core/master use equal eight-dimensional boundaries",
        tuple(
            tuple(boundary.dimension for boundary in instrument.boundaries)
            for instrument in (core,) + regions + (master,)
        ),
        ((8, 8, 8),) * 5,
    )
    typed_rows = tuple(
        (
            instrument.name,
            all(
                arrow.source in boundary_dict(instrument)
                and arrow.target in boundary_dict(instrument)
                and len(arrow.amplitude)
                == boundary_dict(instrument)[arrow.target].dimension
                and len(arrow.amplitude[0])
                == boundary_dict(instrument)[arrow.source].dimension
                for arrow in instrument.arrows
            ),
            len({arrow.name for arrow in instrument.arrows}) == len(instrument.arrows),
            len({readout.name for readout in instrument.readouts})
            == len(instrument.readouts),
        )
        for instrument in (core,) + regions + (master,)
    )
    checks.check(
        "all arrows and readouts are explicitly and uniquely typed",
        typed_rows,
        tuple((name, True, True, True) for name in ("O", "D1", "D2", "D3", "E")),
        category="type",
    )
    checks.check(
        "all constructed amplitude arrows are exactly unitary",
        all(
            is_unitary(arrow.amplitude)
            for instrument in (core,) + regions + (master,)
            for arrow in instrument.arrows
        ),
        True,
    )
    checks.check(
        "basis preparation and configuration tomography are explicit access postulates",
        tuple(
            (
                instrument.name,
                len(instrument.preparations),
                len(readout_dict(instrument)["configuration-probe"].values),
                instrument.access_class.startswith("POSTULATE"),
            )
            for instrument in (core,) + regions + (master,)
        ),
        tuple((name, 8, 8, True) for name in ("O", "D1", "D2", "D3", "E")),
        category="schema",
    )
    checks.check(
        "implemented gauge is the exact real sign/permutation gauge only",
        tuple(instrument.gauge_class.startswith("REAL-SIGN-GAUGE") for instrument in regions),
        (True, True, True),
        category="schema",
    )

    quantum_rows = {}
    for region in regions:
        arrows = arrow_dict(region)
        readout = candidate_record(region)
        preserve_rows = {}
        for name in ("core-preserve", "regional-preserve"):
            continuation = arrows[name].amplitude
            residual = record_residual(arrows["write"].amplitude, continuation, readout)
            preserve_rows[name] = {
                "available": h_avail(continuation, readout),
                "coherence": cut_coherence_stats(
                    continuation,
                    arrows["write"].amplitude,
                    readout.values,
                ),
                "defect_nonzero": nonzero_count(
                    defect(continuation, arrows["write"].amplitude)
                ),
                "residual_defined": residual is not None,
                "residual_nonzero": None if residual is None else nonzero_count(residual),
            }
        erase = arrows["erase"].amplitude
        erase_residual = record_residual(arrows["write"].amplitude, erase, readout)
        quantum_rows[region.name] = {
            "occurrence": h_corr(arrows["write"].amplitude, readout, region.preparations),
            "no_write_h_corr": h_corr(
                arrows["no-write"].amplitude,
                readout,
                region.preparations,
            ),
            "preserve": preserve_rows,
            "erase": {
                "available": h_avail(erase, readout),
                "coherence": cut_coherence_stats(
                    erase,
                    arrows["write"].amplitude,
                    readout.values,
                ),
                "defect_nonzero": nonzero_count(defect(erase, arrows["write"].amplitude)),
                "residual_defined": erase_residual is not None,
            },
        }
        checks.check(f"{region.name} record occurrence is derived by H-corr", quantum_rows[region.name]["occurrence"], True)
        checks.check(f"{region.name} no-write control fails H-corr", quantum_rows[region.name]["no_write_h_corr"], False)
        checks.check(
            f"{region.name} both preserving continuations retain availability",
            tuple(preserve_rows[name]["available"] for name in preserve_rows),
            (True, True),
        )
        checks.check(
            f"{region.name} preserving seams have zero coherence, defect, and residual",
            tuple(
                (
                    row["coherence"],
                    row["defect_nonzero"],
                    row["residual_defined"],
                    row["residual_nonzero"],
                )
                for row in preserve_rows.values()
            ),
            (
                ({"total": 0, "cross_sector": 0, "within_sector": 0}, 0, True, 0),
                ({"total": 0, "cross_sector": 0, "within_sector": 0}, 0, True, 0),
            ),
        )
        checks.check(f"{region.name} eraser destroys availability", quantum_rows[region.name]["erase"]["available"], False)
        checks.check(
            f"{region.name} eraser restores cross-sector coherence and nonzero defect",
            (
                quantum_rows[region.name]["erase"]["coherence"]["cross_sector"] > 0,
                quantum_rows[region.name]["erase"]["defect_nonzero"] > 0,
                quantum_rows[region.name]["erase"]["residual_defined"],
            ),
            (True, True, False),
        )

    checks.section("REAL GAUGE AND PRESENTATION CONTROLS")
    base = regions[0]
    source_patterns = (
        (1, -1, 1, -1, -1, 1, -1, 1),
        (-1, 1, 1, -1, 1, -1, -1, 1),
        (1, 1, -1, -1, -1, -1, 1, 1),
    )
    target_patterns = tuple(tuple(reversed(row)) for row in source_patterns)
    source_signs = {
        boundary.name: diagonal(source_patterns[index])
        for index, boundary in enumerate(base.boundaries)
    }
    target_signs = {
        boundary.name: diagonal(target_patterns[index])
        for index, boundary in enumerate(master.boundaries)
    }
    gauged_base = sign_gauge_instrument(base, source_signs)
    gauged_master = sign_gauge_instrument(master, target_signs)
    gauged_embedding = sign_gauge_morphism(
        family["region_embeddings"][0],
        source_signs,
        target_signs,
    )
    base_arrows = arrow_dict(base)
    gauged_arrows = arrow_dict(gauged_base)
    checks.check(
        "composition-compatible sign gauge preserves accessible composite Born laws",
        tuple(
            born(matmul(gauged_arrows[name].amplitude, gauged_arrows["write"].amplitude))
            == born(matmul(base_arrows[name].amplitude, base_arrows["write"].amplitude))
            for name in ("core-preserve", "regional-preserve", "erase")
        ),
        (True, True, True),
    )
    checks.check(
        "real-gauged region/master morphism still satisfies every diagram",
        validate_morphism(gauged_embedding, gauged_base, gauged_master)["ok"],
        True,
    )
    relabelling = (7, 0, 5, 2, 6, 1, 4, 3)
    relabelled = relabel_instrument(base, relabelling)
    relabelled_arrows = arrow_dict(relabelled)
    checks.check(
        "common configuration relabelling preserves W3 and accessible invariants",
        (
            h_corr(
                relabelled_arrows["write"].amplitude,
                candidate_record(relabelled),
                relabelled.preparations,
            ),
            h_avail(
                relabelled_arrows["regional-preserve"].amplitude,
                candidate_record(relabelled),
            ),
            region_dynamic_signature(relabelled) == region_dynamic_signature(base),
        ),
        (True, True, True),
    )
    guard_rows = []
    for forbidden in ("causal_order", "metric", "field_propagator", "complex_u1_gauge"):
        try:
            reject_schema_inputs({forbidden: "inserted"})
            guard_rows.append(False)
        except SmugglingError:
            guard_rows.append(True)
    checks.check(
        "causal, geometric, field, and full-U(1) insertion guards fire",
        tuple(guard_rows),
        (True, True, True, True),
        category="schema",
    )

    checks.section("ANTI-PADDING AND SAME-DIMENSIONAL DIVERSITY")
    old_product = simultaneous_product_search(old_padded_negative())
    checks.check(
        "old q=3 spectator-padded family is detected",
        old_product,
        {
            "factor_found": True,
            "permutations_tested": 1,
            "witness": (0, 1, 2, 3, 4, 5, 6, 7),
        },
    )
    anti_padding_rows = {}
    for region in regions:
        substantive = tuple(arrow.amplitude for arrow in region.arrows)
        anti_padding_rows[region.name] = simultaneous_product_search(substantive)
        checks.check(
            f"{region.name} exhausts all 8! common relabellings with no 4x2 product family",
            anti_padding_rows[region.name],
            {
                "factor_found": False,
                "permutations_tested": 40320,
                "witness": None,
            },
        )
    signatures = tuple(region_dynamic_signature(region) for region in regions)
    checks.check(
        "preserve-family support multisets separate all equal-dimensional regions even if labels permute",
        tuple((region.name, region_dynamic_signature(region)[1]) for region in regions),
        (("D1", (8, 8)), ("D2", (8, 16)), ("D3", (8, 32))),
    )
    checks.check(
        "all three full accessible dynamic signatures are distinct",
        len(set(signatures)),
        3,
    )

    checks.section("TYPED MASTER MORPHISMS, OVERLAPS, AND REFINEMENT")
    region_morphism_rows = tuple(
        validate_morphism(morphism, region, master)
        for region, morphism in zip(regions, family["region_embeddings"])
    )
    core_morphism_rows = tuple(
        validate_morphism(morphism, core, region)
        for region, morphism in zip(regions, family["core_embeddings"])
    )
    checks.check(
        "all region-to-master embeddings pass typing, intertwiners, preparations, and readout pullback",
        tuple(row["ok"] for row in region_morphism_rows),
        (True, True, True),
        category="type",
    )
    checks.check(
        "all core-to-region embeddings pass typing, intertwiners, preparations, and readout pullback",
        tuple(row["ok"] for row in core_morphism_rows),
        (True, True, True),
        category="type",
    )
    checks.check(
        "changing one mapped regional arrow breaks every embedding",
        tuple(
            validate_morphism(mutate_mapped_arrow(morphism), region, master)["ok"]
            for region, morphism in zip(regions, family["region_embeddings"])
        ),
        (False, False, False),
    )
    nonmonomial_boundary = InstrumentMorphism(
        name="j1:NONMONOMIAL-BOUNDARY-CONTROL",
        source=family["region_embeddings"][0].source,
        target=family["region_embeddings"][0].target,
        boundary_maps=(
            BoundaryMap(
                family["region_embeddings"][0].boundary_maps[0].source_boundary,
                family["region_embeddings"][0].boundary_maps[0].target_boundary,
                on_qubit(H, 0, 3),
            ),
        )
        + family["region_embeddings"][0].boundary_maps[1:],
        arrow_map=family["region_embeddings"][0].arrow_map,
        readout_map=family["region_embeddings"][0].readout_map,
    )
    nonmonomial_diagnostics = validate_morphism(nonmonomial_boundary, regions[0], master)
    checks.check(
        "unitary but non-signed-permutation boundary maps are outside the declared Reg scope",
        (
            nonmonomial_diagnostics["boundary_rows"][0][5],
            nonmonomial_diagnostics["boundary_rows"][0][6],
            nonmonomial_diagnostics["ok"],
        ),
        (True, False, False),
        category="control",
    )
    category = regional_category(family)
    checks.check(
        "Reg has amplitude instruments and typed instrument morphisms",
        (is_reg_category(category["Reg"]), len(category["Reg"].objects), len(category["Reg"].morphisms)),
        (True, 5, 12),
        category="type",
        key="type.reg_category",
    )
    checks.check(
        "Reg morphisms, identities, and all 22 declared compositions validate",
        (
            category["all_category_laws"],
            category["all_morphisms_valid"],
            category["morphism_keys_match_order"],
            category["core_composites_equal"],
            len(category["composition_laws"]),
            all(category["composition_laws"]),
        ),
        (True, True, True, True, 22, True),
        category="measurement",
        key="measurement.reg_category_laws",
    )
    expected_core = frozenset(("core.write", "core.preserve", "core.no-write"))
    checks.check(
        "all pair and triple intersections are the nonvacuous amplitude core",
        (category["pair_overlaps"], category["triple_overlap"]),
        ((expected_core, expected_core, expected_core), expected_core),
    )
    checks.check(
        "O satisfies the finite pair-pullback universal tests",
        category["pullback_universal"],
        (True, True, True),
    )
    checks.check(
        "the three regional subfamilies cover the fixed master arrow family",
        category["cover_is_master"],
        True,
    )
    positive_refinement = family["region_embeddings"][0]
    old_shadow_object = {"kind": "Born-shadow product coarse-graining", "squares_first": True}
    positive_refinement_ok = is_instrument_refinement(positive_refinement, instruments)
    old_shadow_is_refinement = is_instrument_refinement(old_shadow_object, instruments)

    checks.section("NO-CIRCULARITY AND SAME-LAW NEGATIVE CONTROLS")
    corrupted_family = dict(family)
    corrupted_family["region_embeddings"] = (
        mutate_mapped_arrow(family["region_embeddings"][0]),
    ) + tuple(family["region_embeddings"][1:])
    corrupted_structural = validate_structural_bridge(corrupted_family)
    checks.check(
        "altering one bridge breaks canonical matching and independent structural validation",
        (
            matches_canonical_spec(corrupted_family, MASTER_SPEC_SHA256),
            corrupted_structural["ok"],
            corrupted_structural["reason"],
        ),
        (False, False, "morphism_diagram_failure"),
        category="control",
        key="control.mapped_arrow_mutant",
    )
    regional_laws = tuple(
        readout_law(
            arrow_dict(region)["write"].amplitude,
            candidate_record(region),
            region.actual_preparation,
        )
        for region in regions
    )
    fair_law = ((0, Q2(Fraction(1, 2))), (1, Q2(Fraction(1, 2))))
    checks.check("regional fair laws are consequence-only measurements", regional_laws, (fair_law,) * 3)
    diagonal_control = build_equal_law_control("G-diagonal", None)
    anti_control = build_equal_law_control("G-anti-diagonal", 2)
    diagonal_extension = equal_law_control_measurements(diagonal_control)
    anti_extension = equal_law_control_measurements(anti_control)
    diagonal_candidate = equal_law_bridge_candidate(diagonal_control, master)
    anti_candidate = equal_law_bridge_candidate(anti_control, master)
    diagonal_obstruction = validate_candidate_bridge(
        diagonal_candidate,
        diagonal_control,
        master,
    )
    anti_obstruction = validate_candidate_bridge(
        anti_candidate,
        anti_control,
        master,
    )
    checks.check(
        "diagonal and anti-diagonal controls are typed exact W3-compatible instruments",
        tuple(
            (
                isinstance(control, Instrument),
                extension["dimension"],
                all(is_unitary(arrow.amplitude) for arrow in control.arrows),
                extension["h_corr"],
                extension["h_avail"],
            )
            for control, extension in (
                (diagonal_control, diagonal_extension),
                (anti_control, anti_extension),
            )
        ),
        ((True, 16, True, True, True), (True, 16, True, True, True)),
        category="type",
        key="type.equal_law_controls",
    )
    checks.check(
        "diagonal and anti-diagonal supports differ",
        (diagonal_extension["support"], anti_extension["support"]),
        (((0, 0, 0), (1, 1, 1)), ((0, 1, 0), (1, 0, 1))),
    )
    checks.check(
        "law-only predicate accepts both incompatible extensions",
        (
            law_only_accepts(regional_laws, diagonal_control),
            law_only_accepts(regional_laws, anti_control),
        ),
        (True, True),
        category="control",
        key="control.law_only_ambiguity",
    )
    diagonal_maps = forced_binary_maps(diagonal_extension["support"])
    anti_maps = forced_binary_maps(anti_extension["support"])
    checks.check(
        "equal marginals force incompatible pair-map families",
        (diagonal_maps["maps"], anti_maps["maps"]),
        (
            (((0, 0), (1, 1)), ((0, 0), (1, 1)), ((0, 0), (1, 1))),
            (((0, 1), (1, 0)), ((0, 1), (1, 0)), ((0, 0), (1, 1))),
        ),
    )
    checks.check(
        "typed equal-law bridge candidates fail at the exact 16-versus-8 boundary obstruction",
        tuple(
            (
                row["candidate_is_instrument_morphism"],
                row["dimensions_match"],
                row["full_validator_called"],
                row["accepted"],
                row["reason"],
                tuple((dimension[1], dimension[3]) for dimension in row["dimension_rows"]),
            )
            for row in (diagonal_obstruction, anti_obstruction)
        ),
        (
            (True, False, False, False, "boundary_dimension_mismatch", ((16, 8),) * 3),
            (True, False, False, False, "boundary_dimension_mismatch", ((16, 8),) * 3),
        ),
        category="control",
        key="control.typed_equal_law_bridge_obstruction",
    )
    rogue = build_equal_law_rogue(regions[0])
    rogue_invariant = rogue_bridge_invariant(rogue, master)
    checks.check(
        "rogue region has the same stable fair record law",
        (
            rogue_invariant["same_law"],
            h_corr(
                arrow_dict(rogue)["write"].amplitude,
                candidate_record(rogue),
                rogue.preparations,
            ),
            h_avail(
                arrow_dict(rogue)["regional-preserve"].amplitude,
                candidate_record(rogue),
            ),
        ),
        (fair_law, True, True),
    )
    checks.check(
        "rogue preserve has no admissible signed-permutation bridge into the fixed master",
        (
            len(rogue_invariant["candidate_rows"]),
            rogue_invariant["invariant_match"],
            rogue_invariant["bridge_exists"],
        ),
        (4, False, False),
    )

    checks.section("FACTIFACE, REC, AND PHYSICAL TRIPLE DESCENT")
    rec_data = record_functor(family, category)
    checks.check(
        "all five record algebras are derived at the preserving scope",
        tuple(
            (
                name,
                row["generator"],
                row["occurred"],
                all(value for _arrow, value in row["availability"]),
            )
            for name, row in rec_data["algebras"].items()
        ),
        tuple((name, "memory", True, True) for name in ("O", "D1", "D2", "D3", "E")),
    )
    checks.check(
        "FactIface and Rec are distinct typed executable objects",
        (
            is_fact_iface_category(rec_data["FactIface"]),
            isinstance(rec_data["Rec"], RecordFunctor),
            rec_data["Rec"].variance,
            len(rec_data["FactIface"].objects),
            len(rec_data["FactIface"].morphisms),
        ),
        (True, True, "CONTRAVARIANT", 5, 12),
        category="type",
    )
    checks.check(
        "every fact restriction is induced from a validated Reg morphism",
        rec_data["all_induced_from_morphisms"],
        True,
    )
    checks.check(
        "Rec satisfies identities and contravariant composition",
        (rec_data["all_functor_laws"], all(rec_data["identity_laws"]), all(rec_data["composition_laws"])),
        (True, True, True),
    )
    checks.check(
        "the common record descends across the genuine triple and all three master paths",
        (
            rec_data["core_maps"],
            rec_data["triple_descends"],
            rec_data["triple_path_law"],
        ),
        (
            ({0: 0, 1: 1}, {0: 0, 1: 1}, {0: 0, 1: 1}),
            True,
            True,
        ),
    )
    checks.check(
        "regional record projectors are literal morphism pullbacks",
        tuple(
            tuple(row[3] for row in diagnostics["readout_rows"])
            for diagnostics in region_morphism_rows + core_morphism_rows
        ),
        ((True, True),) * 6,
    )
    value_groupoid = value_only_fact_groupoid()
    value_groupoid_laws = value_only_groupoid_laws(value_groupoid)
    checks.check(
        "value-only groupoid is FactIface-shaped but cannot satisfy Reg typing",
        (
            is_fact_iface_category(value_groupoid),
            is_reg_category(value_groupoid),
            len(value_groupoid.objects),
            len(value_groupoid.morphisms),
        ),
        (True, False, 3, 9),
        category="type",
    )
    checks.check(
        "value-only control obeys FactIface groupoid laws without becoming Reg",
        value_groupoid_laws,
        {
            "identity_count": 3,
            "inverse_count": 9,
            "composition_count": 27,
            "all_laws": True,
        },
    )

    checks.section("PREREQUISITE-DERIVED OUTCOME (NOT COUNTED AS NEW CHECKS)")
    anchor_keys = (
        "anchor.pin_commit",
        "anchor.provenance_commits",
        "anchor.active_pin_hash",
        "anchor.binding_files",
        "static.constructor_law_blind",
        "authentication.construction_surface",
        "static.exactness",
        "authentication.master_spec",
        "control.positive_structural_family",
        "static.record_functor_law_blind",
    )
    region_keys = (
        "three regions and the core/master use equal eight-dimensional boundaries",
        "all arrows and readouts are explicitly and uniquely typed",
        "all constructed amplitude arrows are exactly unitary",
        "basis preparation and configuration tomography are explicit access postulates",
        "implemented gauge is the exact real sign/permutation gauge only",
        "composition-compatible sign gauge preserves accessible composite Born laws",
        "real-gauged region/master morphism still satisfies every diagram",
        "common configuration relabelling preserves W3 and accessible invariants",
        "causal, geometric, field, and full-U(1) insertion guards fire",
        "old q=3 spectator-padded family is detected",
        "D1 exhausts all 8! common relabellings with no 4x2 product family",
        "D2 exhausts all 8! common relabellings with no 4x2 product family",
        "D3 exhausts all 8! common relabellings with no 4x2 product family",
        "preserve-family support multisets separate all equal-dimensional regions even if labels permute",
        "all three full accessible dynamic signatures are distinct",
    ) + tuple(
        f"{region.name} {suffix}"
        for region in regions
        for suffix in (
            "record occurrence is derived by H-corr",
            "no-write control fails H-corr",
            "both preserving continuations retain availability",
            "preserving seams have zero coherence, defect, and residual",
            "eraser destroys availability",
            "eraser restores cross-sector coherence and nonzero defect",
        )
    )
    morphism_keys = (
        "all region-to-master embeddings pass typing, intertwiners, preparations, and readout pullback",
        "all core-to-region embeddings pass typing, intertwiners, preparations, and readout pullback",
        "changing one mapped regional arrow breaks every embedding",
        "unitary but non-signed-permutation boundary maps are outside the declared Reg scope",
        "type.reg_category",
        "measurement.reg_category_laws",
    )
    site_keys = (
        "all pair and triple intersections are the nonvacuous amplitude core",
        "O satisfies the finite pair-pullback universal tests",
        "the three regional subfamilies cover the fixed master arrow family",
    )
    fact_keys = (
        "control.mapped_arrow_mutant",
        "regional fair laws are consequence-only measurements",
        "type.equal_law_controls",
        "diagonal and anti-diagonal supports differ",
        "control.law_only_ambiguity",
        "equal marginals force incompatible pair-map families",
        "control.typed_equal_law_bridge_obstruction",
        "rogue region has the same stable fair record law",
        "rogue preserve has no admissible signed-permutation bridge into the fixed master",
        "all five record algebras are derived at the preserving scope",
        "FactIface and Rec are distinct typed executable objects",
        "every fact restriction is induced from a validated Reg morphism",
        "Rec satisfies identities and contravariant composition",
        "the common record descends across the genuine triple and all three master paths",
        "regional record projectors are literal morphism pullbacks",
        "value-only groupoid is FactIface-shaped but cannot satisfy Reg typing",
        "value-only control obeys FactIface groupoid laws without becoming Reg",
    )

    def prerequisite_rows(keys: Sequence[str]) -> Mapping[str, bool]:
        return {key: checks.results[key] for key in keys}

    prerequisites = {
        "anchors_and_authentication": prerequisite_rows(anchor_keys),
        "regions_and_diversity": prerequisite_rows(region_keys),
        "morphisms": prerequisite_rows(morphism_keys),
        "cover_and_overlap": prerequisite_rows(site_keys)
        | {
            "Ref reuses the validated j1 instrument morphism": positive_refinement_ok,
        },
        "fact_descent": prerequisite_rows(fact_keys),
    }
    assigned_check_keys = set(anchor_keys + region_keys + morphism_keys + site_keys + fact_keys)
    unassigned_check_keys = tuple(sorted(set(checks.results) - assigned_check_keys))
    prerequisite_classification_complete = not unassigned_check_keys
    anchor_stage = (
        prerequisite_classification_complete
        and all(prerequisites["anchors_and_authentication"].values())
    )
    regions_stage = anchor_stage and all(prerequisites["regions_and_diversity"].values())
    morphism_stage = regions_stage and all(prerequisites["morphisms"].values())
    site_stage = morphism_stage and all(prerequisites["cover_and_overlap"].values())
    fact_stage = site_stage and all(prerequisites["fact_descent"].values())
    earned = {
        "RQ0-REPAIR-BLOCKED-AT-DIVERSITY": anchor_stage and not regions_stage,
        "RQ0-REPAIR-BLOCKED-AT-MORPHISM": regions_stage and not morphism_stage,
        "RQ0-REPAIR-BLOCKED-AT-OVERLAP": morphism_stage and not site_stage,
        "RQ0-REGIONS-CONSTRUCTED": regions_stage,
        "RQ0-REGIONAL-SITE": site_stage,
        "RQ0-FACT-DESCENT": fact_stage,
    }
    if fact_stage:
        highest_outcome: Optional[str] = "RQ0-FACT-DESCENT"
        first_failed_stage = "NONE"
    elif site_stage:
        highest_outcome = "RQ0-REGIONAL-SITE"
        first_failed_stage = "FACT-DESCENT"
    elif morphism_stage:
        highest_outcome = "RQ0-REGIONS-CONSTRUCTED"
        first_failed_stage = "OVERLAP"
    elif regions_stage:
        highest_outcome = "RQ0-REGIONS-CONSTRUCTED"
        first_failed_stage = "MORPHISM"
    elif anchor_stage:
        highest_outcome = None
        first_failed_stage = "DIVERSITY"
    else:
        highest_outcome = None
        first_failed_stage = (
            "UNCLASSIFIED-CHECK" if unassigned_check_keys else "ANCHOR-OR-AUTHENTICATION"
        )
    receipt_valid = prerequisite_classification_complete and all(checks.results.values())
    nonclaims = (
        "no localized influence or RQ0-C1",
        "no causal order or cone",
        "no spacetime region, volume, or conformal metric",
        "no field propagator or stress object",
        "no gravity dynamics",
        "no full complex U(1) gauge",
    )

    return {
        "provenance_and_authentication": {
            "pin_commit": PIN_COMMIT,
            "pin_sha256": PIN_SHA256,
            "prior_adjudication_commit": PRIOR_ADJUDICATION_COMMIT,
            "hostile_adjudication_commit": HOSTILE_ADJUDICATION_COMMIT,
            "reviewed_commits": REVIEWED_COMMITS,
            "immutable_git_provenance": commit_rows,
            "canonical_master_spec": {
                "expected_sha256": MASTER_SPEC_SHA256,
                "observed_sha256": frozen_digest,
                "matches": matches_canonical_spec(family, MASTER_SPEC_SHA256),
                "scope": "same-file canonical authentication; not historical independent preregistration",
            },
            "canonical_construction_surface": {
                "expected_sha256": CONSTRUCTION_SURFACE_SHA256,
                "observed_sha256": observed_surface_digest,
                "matches": observed_surface_digest == CONSTRUCTION_SURFACE_SHA256,
                "scope": "same-file canonical source authentication",
            },
            "structural_validation": {
                "separate_from_authentication": "BY IMPLEMENTATION: validate_structural_bridge takes no digest",
                "positive_family_ok": structural_family["ok"],
            },
            "constructor_arguments": constructor_audit["arguments"],
            "constructor_forbidden_names": constructor_audit["forbidden_names"],
        },
        "scope": {
            "arithmetic": "exact Q(sqrt(2)) plus exact rational subfield; no floats or tolerances",
            "carrier": "three named operational bits; every boundary has dimension 8",
            "preparations": "all eight basis configurations POSTULATED accessible; actual preparation 0",
            "tomography": "full configuration probe POSTULATED accessible",
            "record_candidate_search": "none; memory-bit readout frozen in the locked master specification",
            "gauge": "REAL-SIGN-GAUGE: common configuration relabelling x independent +/- boundary phases",
            "morphism_boundary_scope": "exact signed-permutation identifications on the fixed eight-configuration carrier",
            "anti_padding_search": "exhaustive all 8! common carrier relabellings for the declared nontrivial 4x2 split; exact rearrangement-rank test; no arbitrary-unitary irreducibility claim",
            "rogue_morphism_scope": "all four preserve-family master arrows; exact Born-entry multiset excludes every signed row/column relabelling",
            "random_seeds": "none",
            "caps": {"runtime_seconds": 120, "anti_padding_permutations_per_positive": 40320},
            "numerical_geometry": "none",
        },
        "postulates": (
            "operational individuation by the declared accessible amplitude-instrument family",
            "all basis preparations are accessible",
            "the complete final-configuration probe is accessible",
            "the frozen fixed-carrier subinstrument class is the admissible extension class",
            "the implemented regional gauge is real signs and common carrier relabelling",
        ),
        "inherited_results": {
            "Paper_1": "W3 H-corr/H-avail seam and composition-compatible boundary-gauge discipline",
            "Paper_2": "same law is not same fact; fact co-reference precedes token identity",
            "hostile_review": "anti-spectator and anti-diagonal obstructions; repair specification",
        },
        "legacy_uses": {
            name: {"path": relative, "class": use_class, "code_imported": False}
            for name, (relative, _expected, use_class) in LOCKS.items()
        }
        | {
            "commit_12_family": {
                "class": "negative control only: exact q=3 spectator-padded family reconstructed from specification",
                "code_imported": False,
            },
            "commit_12_refinement": {
                "class": "negative/type control only: Born-shadow product coarse-graining",
                "code_imported": False,
            },
            "v10_and_earlier": {
                "class": "no ontology, fixture, algorithm, or code imported",
                "code_imported": False,
            },
        },
        "regions": {
            region.name: {
                "dimension": region.boundaries[0].dimension,
                "write_digest": matrix_digest(arrow_dict(region)["write"].amplitude),
                "core_preserve_digest": matrix_digest(arrow_dict(region)["core-preserve"].amplitude),
                "regional_preserve_digest": matrix_digest(arrow_dict(region)["regional-preserve"].amplitude),
                "erase_digest": matrix_digest(arrow_dict(region)["erase"].amplitude),
                "dynamic_signature": signatures[index],
                "quantum_record_measurements": quantum_rows[region.name],
                "anti_padding": anti_padding_rows[region.name],
            }
            for index, region in enumerate(regions)
        },
        "anti_padding_negative": old_product,
        "master": {
            "name": master.name,
            "dimension": master.boundaries[0].dimension,
            "arrow_names": tuple(arrow.name for arrow in master.arrows),
            "region_embedding_names": tuple(row.name for row in family["region_embeddings"]),
            "core_embedding_names": tuple(row.name for row in family["core_embeddings"]),
            "all_region_morphisms_valid": tuple(row["ok"] for row in region_morphism_rows),
            "all_core_morphisms_valid": tuple(row["ok"] for row in core_morphism_rows),
            "scope_classification": "DECLARED SCOPE: one finite local witness instrument; no global-universe claim",
        },
        "Reg": {
            "standard_name": "finite amplitude-subinstrument cover category/atlas",
            "topology_scope": "no Grothendieck topology declared; RQ0-REGIONAL-SITE is the pin's internal rung name",
            "object_type": "Instrument",
            "morphism_type": "InstrumentMorphism",
            "objects": category["objects"],
            "arrow_count": len(category["order_arrows"]),
            "pair_overlaps": category["pair_overlaps"],
            "triple_overlap": category["triple_overlap"],
            "pullback_universal": category["pullback_universal"],
            "cover_is_master": category["cover_is_master"],
            "all_category_laws": category["all_category_laws"],
            "composition_law_count": len(category["composition_laws"]),
        },
        "Ref": {
            "kind": "fixed-carrier intervention-family inclusion",
            "positive": positive_refinement.name,
            "positive_is_instrument_morphism": positive_refinement_ok,
            "positive_gate_source": "deduplicated: the already validated j1 region-to-master morphism",
            "old_result_name": "Born-shadow product coarse-graining",
            "old_result_is_instrument_morphism": old_shadow_is_refinement,
            "old_result_classification": "TYPE CONTROL ONLY; not counted as an independent scientific gate",
            "scope": "no spacetime-resolution claim",
        },
        "no_circularity_controls": {
            "regional_laws": regional_laws,
            "diagonal_instrument": diagonal_control,
            "anti_diagonal_instrument": anti_control,
            "diagonal_support": diagonal_extension["support"],
            "anti_diagonal_support": anti_extension["support"],
            "law_only_accepts_diagonal_and_anti": (
                law_only_accepts(regional_laws, diagonal_control),
                law_only_accepts(regional_laws, anti_control),
            ),
            "diagonal_forced_maps": diagonal_maps["maps"],
            "anti_diagonal_forced_maps": anti_maps["maps"],
            "candidate_morphisms": (diagonal_candidate, anti_candidate),
            "structural_bridge_diagnostics": (
                diagonal_obstruction,
                anti_obstruction,
            ),
            "rogue_same_law": rogue_invariant["same_law"],
            "rogue_candidate_rows": rogue_invariant["candidate_rows"],
            "rogue_classification": "SAME-LAW-NOT-SAME-FACT",
        },
        "FactIface": {
            "object_type": "FactAlgebra",
            "morphism_type": "FactMorphism",
            "object_count": len(rec_data["FactIface"].objects),
            "arrow_count": len(rec_data["FactIface"].morphisms),
            "value_only_control_laws": value_groupoid_laws,
            "value_only_control_is_Reg": is_reg_category(value_groupoid),
        },
        "Rec": {
            "variance": rec_data["Rec"].variance,
            "object_map": rec_data["Rec"].object_map,
            "arrow_map": rec_data["Rec"].arrow_map,
            "algebras": rec_data["algebras"],
            "all_maps_induced_from_Reg": rec_data["all_induced_from_morphisms"],
            "all_functor_laws": rec_data["all_functor_laws"],
            "triple_descends": rec_data["triple_descends"],
            "three_paths_equal_direct_pullback": rec_data["triple_path_law"],
            "static_law_inputs_detected": rec_audit["forbidden_names"],
        },
        "classifications": {
            "region": "DEFINITION plus provisional operational-nomology POSTULATES",
            "record_occurrence_and_availability": "EXACT MEASUREMENTS",
            "preserving_classical_seam": "PAPER-1 THEOREM INSTANCE plus EXACT MEASUREMENTS",
            "eraser_recoherence": "EXACT MEASUREMENT",
            "same_dimensional_diversity": "EXACT ACCESSIBLE INVARIANT",
            "anti_padding": "EXHAUSTIVE EXACT FINITE SEARCH over common relabellings for the 4 x 2 split; arbitrary-unitary tensor irreducibility open",
            "master_and_morphisms": "CONSTRUCTED OBJECTS plus SAME-FILE CANONICAL AUTHENTICATION",
            "overlap": "EXACT PULLBACK/INTERSECTION IN THE DECLARED FINITE AMPLITUDE-SUBINSTRUMENT COVER CATEGORY",
            "fact_descent": "EXACT FUNCTORIAL MEASUREMENT",
            "causal_locality": "OPEN; NOT CONSTRUCTED",
        },
        "outcome_derivation": {
            "prerequisites": prerequisites,
            "all_check_rows_assigned": prerequisite_classification_complete,
            "unassigned_check_keys": unassigned_check_keys,
            "receipt_valid": receipt_valid,
            "first_failed_stage": first_failed_stage,
            "semantic_declaration_check_count": sum(
                row["category"] == "semantic" for row in checks.rows
            ),
        },
        "outcomes": earned,
        "highest_outcome": highest_outcome,
        "first_unresolved_obstruction": (
            "a typed, gauge-invariant localized quantum subinstrument; only after a new pin "
            "could it support an operational-influence study"
        ),
        "nonclaims": nonclaims,
    }


def make_receipt(emit: bool, mutant: bool) -> Mapping[str, object]:
    checks = Checks(emit=emit, mutant=mutant)
    science = build_science(checks)
    return {
        "unit": "v13 RQ0 physical-overlap repair",
        "status": (
            "GREEN-UNREVIEWED-REPAIRED"
            if science["outcome_derivation"]["receipt_valid"]
            else "INVALID-RECEIPT-POSITIVE-RUNG-SUPPRESSED"
        ),
        "science": science,
        "checks": checks.rows,
        "summary": checks.summary(),
    }


def render_text(mutant: bool) -> Tuple[str, Mapping[str, object]]:
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        print("=" * 78)
        print("v13 RQ0 -- PHYSICAL OVERLAP OF QUANTUM REGIONAL INSTRUMENTS")
        print("Exact amplitude/morphism construction; no causal, metric, field, or gravity claim")
        print("=" * 78)
        receipt = make_receipt(emit=True, mutant=mutant)
        summary = receipt["summary"]
        derivation = receipt["science"]["outcome_derivation"]
        outcomes = receipt["science"]["outcomes"]
        print("\nVERDICT")
        if derivation["receipt_valid"]:
            print(f"  highest restored rung: {receipt['science']['highest_outcome']}")
            print(
                "  earned outcomes: "
                + " / ".join(name for name, earned in outcomes.items() if earned)
            )
            print("  overlap: exact common amplitude subinstrument with projector pullbacks")
            print("  no-circularity: typed equal-law bridges fail at 16-versus-8; fixed structural family passes")
        else:
            print("  INVALID RECEIPT: EVERY POSITIVE VERDICT IS SUPPRESSED")
            print(f"  first failed stage: {derivation['first_failed_stage']}")
            print("  highest restored rung: NONE")
        print("  ceiling: no localized influence, causal, spacetime, field, or gravity claim")
        print("  next obstruction: localized quantum subinstrument (not started)")
        print("-" * 78)
        print(f"{summary['checks']} checks: {summary['pass']} pass, {summary['fail']} fail")
        print(
            "categories: "
            + ", ".join(
                f"{name}={row['checks']}"
                for name, row in summary["by_category"].items()
            )
        )
    return stream.getvalue(), receipt


def main() -> int:
    mutant = "--mutant" in sys.argv[1:]
    json_mode = "--json" in sys.argv[1:]
    write_receipts = "--write-receipts" in sys.argv[1:]
    verify_receipts = "--verify-receipts" in sys.argv[1:]
    modes = sum((mutant, json_mode, write_receipts, verify_receipts))
    if modes > 1:
        raise SystemExit("choose at most one of --mutant, --json, --write-receipts, --verify-receipts")

    if verify_receipts:
        first_text, first_receipt = render_text(mutant=False)
        second_text, second_receipt = render_text(mutant=False)
        first_json = json.dumps(json_ready(first_receipt), indent=2, sort_keys=True) + "\n"
        second_json = json.dumps(json_ready(second_receipt), indent=2, sort_keys=True) + "\n"
        stored_text = (ROOT / "v13/code/rq0_physical_overlap_output.txt").read_text()
        stored_json = (ROOT / "v13/code/rq0_physical_overlap_receipt.json").read_text()
        rows = (
            ("two complete text runs byte-identical", first_text == second_text),
            ("two complete JSON runs byte-identical", first_json == second_json),
            ("stored text receipt exactly regenerated", first_text == stored_text),
            ("stored JSON receipt exactly regenerated", first_json == stored_json),
        )
        for label, ok in rows:
            print(f"[{'PASS' if ok else 'FAIL'}] {label}")
        return 0 if all(ok for _label, ok in rows) else 1

    if write_receipts:
        text_output, receipt = render_text(mutant=False)
        output_path = ROOT / "v13/code/rq0_physical_overlap_output.txt"
        receipt_path = ROOT / "v13/code/rq0_physical_overlap_receipt.json"
        output_path.write_text(text_output)
        receipt_path.write_text(
            json.dumps(json_ready(receipt), indent=2, sort_keys=True) + "\n"
        )
        print(f"wrote {output_path.relative_to(ROOT)}")
        print(f"wrote {receipt_path.relative_to(ROOT)}")
        return 1 if receipt["summary"]["fail"] or not receipt["science"]["outcome_derivation"]["receipt_valid"] else 0

    if json_mode:
        receipt = make_receipt(emit=False, mutant=mutant)
        print(json.dumps(json_ready(receipt), indent=2, sort_keys=True))
        return 1 if receipt["summary"]["fail"] or not receipt["science"]["outcome_derivation"]["receipt_valid"] else 0

    text_output, receipt = render_text(mutant=mutant)
    print(text_output, end="")
    return 1 if receipt["summary"]["fail"] or not receipt["science"]["outcome_derivation"]["receipt_valid"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
