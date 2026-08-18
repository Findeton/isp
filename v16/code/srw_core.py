#!/usr/bin/env python3
"""Generic exact machinery for SRW Paper 4.

This module contains no SRW physical fixture, expected outcome, or verdict.
Its CLI runs public calibration examples only.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import sys
import tempfile
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


Q = Fraction


@dataclass(frozen=True, order=True)
class GQ:
    """A Gaussian rational a + b i."""

    re: Q = Q(0)
    im: Q = Q(0)

    @staticmethod
    def coerce(value: Any) -> "GQ":
        if isinstance(value, GQ):
            return value
        if isinstance(value, Fraction):
            return GQ(value, Q(0))
        if isinstance(value, int):
            return GQ(Q(value), Q(0))
        raise TypeError(f"cannot coerce {type(value)!r} to GQ")

    def __add__(self, other: Any) -> "GQ":
        rhs = GQ.coerce(other)
        return GQ(self.re + rhs.re, self.im + rhs.im)

    __radd__ = __add__

    def __neg__(self) -> "GQ":
        return GQ(-self.re, -self.im)

    def __sub__(self, other: Any) -> "GQ":
        return self + (-GQ.coerce(other))

    def __rsub__(self, other: Any) -> "GQ":
        return GQ.coerce(other) - self

    def __mul__(self, other: Any) -> "GQ":
        rhs = GQ.coerce(other)
        return GQ(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "GQ":
        return GQ(self.re, -self.im)

    def norm2(self) -> Q:
        return self.re * self.re + self.im * self.im

    def inverse(self) -> "GQ":
        n2 = self.norm2()
        if n2 == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        c = self.conjugate()
        return GQ(c.re / n2, c.im / n2)

    def __truediv__(self, other: Any) -> "GQ":
        return self * GQ.coerce(other).inverse()


ZERO = GQ(0)
ONE = GQ(1)
I = GQ(0, 1)
Matrix = tuple[tuple[GQ, ...], ...]
Vector = tuple[GQ, ...]


def qtext(value: Q) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def gtext(value: GQ) -> str:
    if value.im == 0:
        return qtext(value.re)
    if value.re == 0:
        if value.im == 1:
            return "i"
        if value.im == -1:
            return "-i"
        return f"{qtext(value.im)}i"
    sign = "+" if value.im > 0 else "-"
    mag = abs(value.im)
    imag = "i" if mag == 1 else f"{qtext(mag)}i"
    return f"{qtext(value.re)}{sign}{imag}"


def scalar(value: Any) -> GQ:
    if isinstance(value, str):
        return GQ(Q(value))
    return GQ.coerce(value)


def matrix(rows: Sequence[Sequence[Any]]) -> Matrix:
    out = tuple(tuple(scalar(x) for x in row) for row in rows)
    if not out or not out[0]:
        raise ValueError("matrix must be nonempty")
    width = len(out[0])
    if any(len(row) != width for row in out):
        raise ValueError("ragged matrix")
    return out


def shape(a: Matrix) -> tuple[int, int]:
    return len(a), len(a[0])


def transpose(a: Matrix) -> Matrix:
    rows, cols = shape(a)
    return tuple(tuple(a[r][c] for r in range(rows)) for c in range(cols))


def adjoint(a: Matrix) -> Matrix:
    return tuple(tuple(x.conjugate() for x in row) for row in transpose(a))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise ValueError(f"shape mismatch {shape(a)} x {shape(b)}")
    return tuple(
        tuple(sum((a[r][k] * b[k][c] for k in range(ac)), ZERO) for c in range(bc))
        for r in range(ar)
    )


def matadd(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise ValueError("shape mismatch")
    return tuple(
        tuple(a[r][c] + b[r][c] for c in range(shape(a)[1]))
        for r in range(shape(a)[0])
    )


def matscale(s: Any, a: Matrix) -> Matrix:
    z = scalar(s)
    return tuple(tuple(z * x for x in row) for row in a)


def matvec(a: Matrix, v: Vector) -> Vector:
    rows, cols = shape(a)
    if cols != len(v):
        raise ValueError("shape mismatch")
    return tuple(sum((a[r][c] * v[c] for c in range(cols)), ZERO) for r in range(rows))


def identity(n: int) -> Matrix:
    return tuple(tuple(ONE if r == c else ZERO for c in range(n)) for r in range(n))


def zero(rows: int, cols: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(cols)) for _ in range(rows))


def direct_sum(a: Matrix, b: Matrix) -> Matrix:
    ar, ac = shape(a)
    br, bc = shape(b)
    return tuple(
        tuple(
            a[r][c]
            if r < ar and c < ac
            else b[r - ar][c - ac]
            if r >= ar and c >= ac
            else ZERO
            for c in range(ac + bc)
        )
        for r in range(ar + br)
    )


def kron(a: Matrix, b: Matrix) -> Matrix:
    ar, ac = shape(a)
    br, bc = shape(b)
    return tuple(
        tuple(a[r // br][c // bc] * b[r % br][c % bc] for c in range(ac * bc))
        for r in range(ar * br)
    )


def support(a: Matrix) -> frozenset[tuple[int, int]]:
    return frozenset(
        (r, c)
        for r, row in enumerate(a)
        for c, value in enumerate(row)
        if value != ZERO
    )


def is_isometry(a: Matrix) -> bool:
    return matmul(adjoint(a), a) == identity(shape(a)[1])


def probability(effect_row: Vector, state: Vector) -> Q:
    if len(effect_row) != len(state):
        raise ValueError("dimension mismatch")
    amp = sum((effect_row[k].conjugate() * state[k] for k in range(len(state))), ZERO)
    return amp.norm2()


def permutation_matrix(order: Sequence[int]) -> Matrix:
    n = len(order)
    if sorted(order) != list(range(n)):
        raise ValueError("not a permutation")
    return tuple(tuple(ONE if c == order[r] else ZERO for c in range(n)) for r in range(n))


def conjugate_map(a: Matrix, source_order: Sequence[int], target_order: Sequence[int]) -> Matrix:
    ps = permutation_matrix(source_order)
    pt = permutation_matrix(target_order)
    return matmul(pt, matmul(a, adjoint(ps)))


def circle(t: Q) -> tuple[Q, Q]:
    den = 1 + t * t
    return (1 - t * t) / den, (2 * t) / den


def growth(x: Q, z: Q) -> Matrix:
    return matrix([[x, 0], [0, 1], [z, 0]])


def rotation(u: Q, v: Q) -> Matrix:
    return matrix([[u, v], [-v, u]])


def reflection(u: Q, v: Q) -> Matrix:
    return matrix([[u, v], [v, -u]])


def readout_pair(u: Q, v: Q) -> Matrix:
    return rotation(u, v)


def coherent_screen(x: Q, z: Q, u: Q, v: Q) -> tuple[Q, Q]:
    state = (GQ(x), GQ(z))
    readout = readout_pair(u, v)
    out = matvec(readout, state)
    return out[0].norm2(), out[1].norm2()


@dataclass(frozen=True)
class RelGraph:
    internal: tuple[str, ...]
    ports: tuple[str, ...]
    edges: frozenset[frozenset[str]]

    def all_vertices(self) -> frozenset[str]:
        return frozenset(self.internal + self.ports)

    def neighbors(self, vertex: str) -> frozenset[str]:
        if vertex not in self.all_vertices():
            raise KeyError(vertex)
        return frozenset(next(iter(edge - {vertex})) for edge in self.edges if vertex in edge)

    def relabel(self, rename: Mapping[str, str]) -> "RelGraph":
        if set(rename) != set(self.all_vertices()) or len(set(rename.values())) != len(rename):
            raise ValueError("rename must be a bijection on all vertices")
        return RelGraph(
            tuple(rename[v] for v in self.internal),
            tuple(rename[v] for v in self.ports),
            frozenset(frozenset(rename[v] for v in edge) for edge in self.edges),
        )


@dataclass(frozen=True)
class RewriteSpan:
    source: RelGraph
    target: RelGraph
    persists: tuple[tuple[str, str], ...]
    created: frozenset[str]
    allowed_entries: frozenset[tuple[str, str]]

    def validate(self) -> None:
        src = set(self.source.internal)
        dst = set(self.target.internal)
        if {a for a, _ in self.persists} - src:
            raise ValueError("persistence source outside graph")
        if {b for _, b in self.persists} - dst:
            raise ValueError("persistence target outside graph")
        if len({a for a, _ in self.persists}) != len(self.persists):
            raise ValueError("persistence source not injective")
        if len({b for _, b in self.persists}) != len(self.persists):
            raise ValueError("persistence target not injective")
        if self.created - dst:
            raise ValueError("created target outside graph")
        if self.created & {b for _, b in self.persists}:
            raise ValueError("created and persistent overlap")
        if any(a not in src or b not in dst for a, b in self.allowed_entries):
            raise ValueError("allowed entry outside internal vertices")


@dataclass(frozen=True)
class FiberSpec:
    sector: str
    internal_multiplicity: int = 1
    include_ports: bool = False

    def dimension(self, graph: RelGraph) -> int:
        if self.internal_multiplicity <= 0:
            raise ValueError("multiplicity must be positive")
        if self.sector == "vertex-one-excitation":
            base = len(graph.internal)
        elif self.sector == "edge-one-excitation":
            base = len(graph.edges)
        else:
            raise ValueError(f"unknown sector {self.sector}")
        if self.include_ports:
            base += len(graph.ports)
        return base * self.internal_multiplicity


@dataclass(frozen=True)
class DictionaryCandidate:
    source_by_col: tuple[str, ...]
    target_by_row: tuple[str, ...]

    def labelled_support(self, a: Matrix) -> frozenset[tuple[str, str]]:
        return frozenset(
            (self.source_by_col[c], self.target_by_row[r]) for r, c in support(a)
        )


def dictionary_candidates(source_labels: Sequence[str], target_labels: Sequence[str]) -> tuple[DictionaryCandidate, ...]:
    return tuple(
        DictionaryCandidate(tuple(src), tuple(dst))
        for src in itertools.permutations(source_labels)
        for dst in itertools.permutations(target_labels)
    )


def support_compatible(
    candidate: DictionaryCandidate,
    a: Matrix,
    allowed: frozenset[tuple[str, str]],
    required_sources: frozenset[str],
) -> bool:
    labelled = candidate.labelled_support(a)
    return labelled <= allowed and {src for src, _ in labelled} == required_sources


def row_for_label(candidate: DictionaryCandidate, label: str) -> int:
    return candidate.target_by_row.index(label)


def graph_port_neighbor(graph: RelGraph, port: str) -> str:
    neighbors = graph.neighbors(port) & frozenset(graph.internal)
    if len(neighbors) != 1:
        raise ValueError("probe port must have one internal neighbor")
    return next(iter(neighbors))


def graph_probe_probability(
    graph: RelGraph,
    port: str,
    candidate: DictionaryCandidate,
    state: Vector,
) -> Q:
    label = graph_port_neighbor(graph, port)
    row = row_for_label(candidate, label)
    effect = tuple(ONE if k == row else ZERO for k in range(len(state)))
    return probability(effect, state)


def commutes(a: Matrix, b: Matrix) -> bool:
    return shape(a)[0] == shape(a)[1] == shape(b)[0] == shape(b)[1] and matmul(a, b) == matmul(b, a)


def common_commutant_contains(transform: Matrix, generators: Sequence[Matrix]) -> bool:
    return all(commutes(transform, generator) for generator in generators)


PHASES = (ONE, I, -ONE, -I)


def phase_index(value: GQ) -> int:
    return PHASES.index(value)


def cycle_holonomy(connection: tuple[GQ, GQ, GQ]) -> GQ:
    return connection[2] * connection[1] * connection[0]


def gauge_cycle(
    connection: tuple[GQ, GQ, GQ], frames: tuple[GQ, GQ, GQ]
) -> tuple[GQ, GQ, GQ]:
    u01, u12, u20 = connection
    g0, g1, g2 = frames
    return (
        g1 * u01 * g0.inverse(),
        g2 * u12 * g1.inverse(),
        g0 * u20 * g2.inverse(),
    )


def cycle_orbits() -> tuple[frozenset[tuple[GQ, GQ, GQ]], ...]:
    connections = tuple(itertools.product(PHASES, repeat=3))
    frames = tuple(itertools.product(PHASES, repeat=3))
    unseen = set(connections)
    orbits: list[frozenset[tuple[GQ, GQ, GQ]]] = []
    while unseen:
        seed = min(unseen, key=lambda c: tuple(phase_index(x) for x in c))
        orbit = frozenset(gauge_cycle(seed, frame) for frame in frames)
        if not orbit <= set(connections):
            raise AssertionError("gauge orbit left phase group")
        unseen -= orbit
        orbits.append(orbit)
    return tuple(orbits)


def two_route_probability(holonomy: GQ) -> Q:
    amp = (ONE + holonomy) / GQ(2)
    return amp.norm2()


def canonical_json(obj: Any) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


@dataclass
class GateLedger:
    rows: list[dict[str, Any]]

    def __init__(self) -> None:
        self.rows = []

    def check(self, name: str, condition: bool, evidence: str) -> None:
        self.rows.append({"gate": name, "passed": bool(condition), "evidence": evidence})
        if not condition:
            raise AssertionError(f"{name}: {evidence}")


def public_calibrations(mutant: str | None = None) -> tuple[dict[str, Any], GateLedger]:
    ledger = GateLedger()
    t = Q(2, 3)
    x, z = circle(t)
    if mutant == "public-circle":
        z += Q(1, 13)
    ledger.check("PUB-CIRCLE", x * x + z * z == 1, f"x={qtext(x)} z={qtext(z)}")

    vg = growth(x, z)
    ledger.check("PUB-ISOMETRY", is_isometry(vg), f"shape={shape(vg)}")
    allowed = frozenset({("s0", "t0"), ("s0", "new"), ("s1", "t1")})
    generic_support = frozenset({("s0", "t0"), ("s0", "new"), ("s1", "t1")})
    endpoint = growth(Q(1), Q(0))
    endpoint_support = frozenset({("s0", "t0"), ("s1", "t1")})
    if mutant == "public-support-equality":
        endpoint_support = generic_support
    ledger.check(
        "PUB-SUPPORT-SUBSET",
        generic_support <= allowed and endpoint_support < allowed,
        f"generic={len(generic_support)} endpoint={len(endpoint_support)} allowed={len(allowed)}",
    )

    candidates = dictionary_candidates(("s0", "s1"), ("t0", "t1", "new"))
    survivors = tuple(
        c for c in candidates if support_compatible(c, vg, allowed, frozenset({"s0", "s1"}))
    )
    if mutant == "public-dictionary-drop":
        survivors = survivors[:-1]
    expected_candidates = math.factorial(len(vg[0])) * math.factorial(len(vg))
    ambiguous_targets = frozenset(dst for src, dst in allowed if src == "s0")
    expected_survivors = math.factorial(len(ambiguous_targets))
    ledger.check(
        "PUB-DICTIONARY-CENSUS",
        len(candidates) == expected_candidates and len(survivors) == expected_survivors,
        f"candidates={len(candidates)} survivors={len(survivors)}",
    )

    graph = RelGraph(
        internal=("t0", "t1", "new"),
        ports=("probe",),
        edges=frozenset({frozenset({"t0", "new"}), frozenset({"new", "probe"})}),
    )
    state = matvec(vg, (ONE, ZERO))
    probe_values = tuple(graph_probe_probability(graph, "probe", c, state) for c in survivors)
    ledger.check(
        "PUB-FUTURE-SEPARATES",
        len(set(probe_values)) == len(survivors),
        f"probabilities={[qtext(v) for v in probe_values]}",
    )

    span = RewriteSpan(
        source=RelGraph(("s0", "s1"), ("probe",), frozenset()),
        target=graph,
        persists=(("s0", "t0"), ("s1", "t1")),
        created=frozenset({"new"}),
        allowed_entries=allowed,
    )
    span.validate()
    fiber_rows = []
    for spec in (
        FiberSpec("vertex-one-excitation"),
        FiberSpec("vertex-one-excitation", 2),
        FiberSpec("vertex-one-excitation", 1, True),
        FiberSpec("edge-one-excitation"),
    ):
        fiber_rows.append((spec.sector, spec.internal_multiplicity, spec.include_ports, spec.dimension(span.source), spec.dimension(span.target)))
    ledger.check(
        "PUB-FIBER-DIMENSIONS",
        fiber_rows[0][-2:] == (len(span.source.internal), len(span.target.internal))
        and fiber_rows[1][-2:] == (len(span.source.internal) * 2, len(span.target.internal) * 2)
        and fiber_rows[2][-2:] == (len(span.source.all_vertices()), len(span.target.all_vertices()))
        and fiber_rows[3][-2:] == (len(span.source.edges), len(span.target.edges)),
        f"rows={fiber_rows}",
    )

    vg2 = kron(vg, identity(2))
    ledger.check("PUB-INTERNAL-LIFT", is_isometry(vg2) and shape(vg2) == (6, 4), f"shape={shape(vg2)}")
    internal_swap = permutation_matrix((1, 0))
    blind_generator = kron(identity(3), identity(2))
    active_generator = kron(identity(3), matrix([[1, 0], [0, -1]]))
    lifted_swap = kron(identity(3), internal_swap)
    ledger.check(
        "PUB-INTERNAL-REACTIVATION",
        common_commutant_contains(lifted_swap, (blind_generator,))
        and not common_commutant_contains(lifted_swap, (blind_generator, active_generator)),
        "blind=true active=false",
    )

    u, v = circle(Q(1, 4))
    screens = coherent_screen(x, z, u, v)
    ledger.check("PUB-INDEPENDENT-ANGLES", sum(screens, Q(0)) == 1, f"screens={[qtext(p) for p in screens]}")
    reciprocal = coherent_screen(x, z, x, z)
    ledger.check("PUB-RECIPROCITY", reciprocal == (Q(1), Q(0)), f"screens={[qtext(p) for p in reciprocal]}")

    orbits = cycle_orbits()
    orbit_holonomies = tuple(frozenset(cycle_holonomy(c) for c in orbit) for orbit in orbits)
    orbit_sizes = tuple(sorted(len(orbit) for orbit in orbits))
    connection_count = len(tuple(itertools.product(PHASES, repeat=len(next(iter(orbits[0]))))))
    effective_gauge_size = len(PHASES) ** (len(next(iter(orbits[0]))) - 1)
    ledger.check(
        "PUB-PHASE-ORBITS",
        len(orbits) == len(PHASES)
        and all(len(hs) == 1 for hs in orbit_holonomies)
        and orbit_sizes == tuple([effective_gauge_size] * len(PHASES)),
        f"connections={connection_count} orbits={len(orbits)} sizes={orbit_sizes}",
    )
    screen_by_holonomy = {gtext(h): qtext(two_route_probability(h)) for h in PHASES}
    ledger.check(
        "PUB-HOLONOMY-SCREEN",
        len(set(screen_by_holonomy.values())) > 1
        and screen_by_holonomy[gtext(ONE)] == qtext(Q(1))
        and screen_by_holonomy[gtext(-ONE)] == qtext(Q(0)),
        f"screens={screen_by_holonomy}",
    )

    measurements: dict[str, Any] = {
        "circle": {"t": qtext(t), "x": qtext(x), "z": qtext(z)},
        "dictionary": {
            "candidate_count": len(candidates),
            "survivor_count": len(survivors),
            "future_probabilities": [qtext(p) for p in probe_values],
        },
        "support": {
            "allowed_count": len(allowed),
            "generic_actual_count": len(generic_support),
            "endpoint_actual_count": len(endpoint_support),
        },
        "fibers": [
            {
                "sector": sector,
                "multiplicity": multiplicity,
                "include_ports": include_ports,
                "source_dimension": source_dim,
                "target_dimension": target_dim,
            }
            for sector, multiplicity, include_ports, source_dim, target_dim in fiber_rows
        ],
        "angle_screen": [qtext(p) for p in screens],
        "reciprocal_screen": [qtext(p) for p in reciprocal],
        "phase": {
            "connection_count": connection_count,
            "orbit_count": len(orbits),
            "orbit_sizes": list(orbit_sizes),
            "screens": screen_by_holonomy,
        },
    }
    return measurements, ledger


def render_public(receipt: Mapping[str, Any]) -> bytes:
    m = receipt["measurements"]
    lines = [
        "SRW GENERIC PUBLIC CALIBRATIONS",
        f"GATES {len(receipt['gates'])}/{len(receipt['gates'])} PASS",
        f"CIRCLE t={m['circle']['t']} x={m['circle']['x']} z={m['circle']['z']}",
        f"DICTIONARIES candidates={m['dictionary']['candidate_count']} survivors={m['dictionary']['survivor_count']} future={m['dictionary']['future_probabilities']}",
        f"SUPPORT allowed={m['support']['allowed_count']} generic={m['support']['generic_actual_count']} endpoint={m['support']['endpoint_actual_count']}",
        f"FIBERS {m['fibers']}",
        f"ANGLES screen={m['angle_screen']} reciprocal={m['reciprocal_screen']}",
        f"PHASE connections={m['phase']['connection_count']} orbits={m['phase']['orbit_count']} sizes={m['phase']['orbit_sizes']} screens={m['phase']['screens']}",
    ]
    lines.extend(f"[PASS] {row['gate']} :: {row['evidence']}" for row in receipt["gates"])
    return ("\n".join(lines) + "\n").encode("utf-8")


def build_public_receipt(mutant: str | None = None) -> tuple[dict[str, Any], bytes]:
    measurements, ledger = public_calibrations(mutant)
    payload: dict[str, Any] = {
        "schema": "srw-public-v1",
        "scope": {
            "arithmetic": "Q and Q(i)",
            "role": "generic calibrations only; no SRW physical fixture or outcome",
        },
        "measurements": measurements,
        "gates": ledger.rows,
    }
    seals = {key: sha256_bytes(canonical_json(payload[key])) for key in tuple(payload)}
    payload["seals"] = seals
    transcript = render_public(payload)
    payload["transcript_sha256"] = sha256_bytes(transcript)
    return payload, transcript


def atomic_write_pair(output_path: Path, receipt_path: Path, output: bytes, receipt: bytes) -> None:
    if output_path.exists() or receipt_path.exists():
        raise FileExistsError("refusing to overwrite an existing public artifact")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    staged: list[tuple[Path, Path]] = []
    try:
        for target, data in ((output_path, output), (receipt_path, receipt)):
            fd, name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
            stage = Path(name)
            with os.fdopen(fd, "wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            if stage.read_bytes() != data:
                raise IOError("staged bytes differ")
            staged.append((stage, target))
        for stage, target in staged:
            os.replace(stage, target)
        if output_path.read_bytes() != output or receipt_path.read_bytes() != receipt:
            raise IOError("promoted bytes differ")
    finally:
        for stage, _ in staged:
            if stage.exists():
                stage.unlink()


PUBLIC_MUTANTS = (
    "public-circle",
    "public-support-equality",
    "public-dictionary-drop",
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SRW generic exact public calibrations")
    parser.add_argument("--public-output", type=Path)
    parser.add_argument("--public-receipt", type=Path)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--mutant", choices=PUBLIC_MUTANTS)
    args = parser.parse_args(argv)

    if args.selftest:
        if args.public_output or args.public_receipt or args.mutant:
            parser.error("--selftest is exclusive")
        try:
            build_public_receipt("public-circle")
        except AssertionError as exc:
            print(f"SELFTEST PASS :: {exc}")
            return 0
        print("SELFTEST FAIL :: corrupted circle survived", file=sys.stderr)
        return 1

    if bool(args.public_output) != bool(args.public_receipt):
        parser.error("--public-output and --public-receipt are required together")
    if not args.public_output:
        parser.error("public artifact paths are required")

    try:
        payload, transcript = build_public_receipt(args.mutant)
    except (AssertionError, ValueError, TypeError) as exc:
        print(f"REFUSED {exc}", file=sys.stderr)
        return 1

    receipt = canonical_json(payload)
    try:
        atomic_write_pair(args.public_output, args.public_receipt, transcript, receipt)
    except (FileExistsError, IOError) as exc:
        print(f"REFUSED {exc}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
