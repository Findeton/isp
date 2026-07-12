#!/usr/bin/env python3
"""Exact finite regional-amplitude/instrument-to-history core for FSDiam.

This uses the no-third-party-dependency Q(sqrt(2),i) arithmetic from reviewed D13
receipt.  It proves a finite circuit/category bridge, not a universal category
of all physical diamonds and not a selection of nature's kernels.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

from d13_finite_kernel_no_go_exact import (
    C2, Q2, ZERO, ONE, HALF, II, ROOT_HALF,
    matrix, eye, dagger, mul, add, scale, mv, inner, outer, trace, kron,
    basis, projector, iswap, reduced_second_qubit, memory_copy_unitary,
)


ROOT = Path(__file__).resolve().parents[2]
DEPENDENCY = Path(__file__).with_name("d13_finite_kernel_no_go_exact.py")
OUT = ROOT / "v10" / "data" / "d14-action-record-bridge-exact.json"
EXPECTED_DEPENDENCY_SHA256 = "1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45"
EXPECTED_CHECKS = 42
EXPECTED_SEMANTIC_SHA256 = "a8b22100a104b04069734bd563a8a3f1411e7772dafa1d0062baf019859658c7"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


def dim_product(ports):
    out = 1
    for port in ports:
        out *= port.dim
    return out


@dataclass(frozen=True)
class Port:
    kind: str
    dim: int
    sealed: bool = False
    owner: str | None = None
    record_id: str | None = None


@dataclass(frozen=True)
class Obj:
    ports: tuple[Port, ...] = ()

    @property
    def dim(self):
        return dim_product(self.ports)

    def tensor(self, other):
        return Obj(self.ports + other.ports)


@dataclass(frozen=True)
class Mor:
    name: str
    source: Obj
    target: Obj
    amp: tuple
    sealed_map: tuple[tuple[int, int], ...] | None = None
    derived: bool = False
    join_entitlement: tuple[str, ...] = ()

    def __post_init__(self):
        if len(self.amp) != self.target.dim:
            raise ValueError("target dimension mismatch")
        if any(len(row) != self.source.dim for row in self.amp):
            raise ValueError("source dimension mismatch")
        source_sealed = tuple(i for i, port in enumerate(self.source.ports) if port.sealed)
        target_sealed = tuple(i for i, port in enumerate(self.target.ports) if port.sealed)
        if len(target_sealed) < len(source_sealed):
            raise ValueError("a protected record cannot be consumed")
        if self.sealed_map is None:
            unused = list(target_sealed)
            inferred = []
            for source_pos in source_sealed:
                source_port = self.source.ports[source_pos]
                candidates = [target_pos for target_pos in unused
                              if self.target.ports[target_pos] == source_port]
                if not candidates:
                    raise ValueError("protected record identity/type mismatch")
                target_pos = candidates[0]
                unused.remove(target_pos)
                inferred.append((source_pos, target_pos))
            object.__setattr__(self, "sealed_map", tuple(inferred))
        if tuple(sorted(source for source, _ in self.sealed_map)) != source_sealed:
            raise ValueError("protected correspondence does not cover every source record")
        if len({target for _, target in self.sealed_map}) != len(self.sealed_map):
            raise ValueError("protected correspondence reuses a target record")
        for source_pos, target_pos in self.sealed_map:
            if target_pos not in target_sealed:
                raise ValueError("protected correspondence targets an unsealed port")
            source_port = self.source.ports[source_pos]
            target_port = self.target.ports[target_pos]
            if source_port != target_port:
                raise ValueError("protected record identity/type mismatch")
        if source_sealed:
            source_dims = tuple(port.dim for port in self.source.ports)
            target_dims = tuple(port.dim for port in self.target.ports)
            for row in range(self.target.dim):
                out_labels = unravel(row, target_dims)
                for col in range(self.source.dim):
                    if self.amp[row][col] == ZERO:
                        continue
                    in_labels = unravel(col, source_dims)
                    for source_pos, target_pos in self.sealed_map:
                        if in_labels[source_pos] != out_labels[target_pos]:
                            raise ValueError("protected record overwrite")
        if not self.derived:
            input_ports = self.source.ports
            declared_owners = tuple(port.owner for port in input_ports if port.owner is not None)
            if declared_owners and any(port.owner is None for port in input_ports):
                raise ValueError("primitive generator mixes owned and ownerless inputs")
            owners = tuple(sorted(set(declared_owners)))
            if len(owners) > 1 and tuple(sorted(self.join_entitlement)) != owners:
                raise ValueError("multi-component generator lacks a connected join entitlement")


class Signature:
    """Admission layer for primitive source generators, before matrix evaluation."""

    def __init__(self):
        self.generators = {}

    def declare(self, name, source, target, amp, join_entitlement=()):
        mor = Mor(name, source, target, amp, join_entitlement=tuple(join_entitlement))
        self.generators[name] = mor
        return mor


UNIT = Obj()


def ident(obj):
    protected = tuple((i, i) for i, port in enumerate(obj.ports) if port.sealed)
    return Mor(f"id[{obj.ports}]", obj, obj, eye(obj.dim),
               sealed_map=protected, derived=True)


def compose(g, f):
    if f.target != g.source:
        raise ValueError("ill-typed boundary gluing")
    g_map = dict(g.sealed_map)
    protected = tuple((source, g_map[mid]) for source, mid in f.sealed_map)
    return Mor(f"({g.name} o {f.name})", f.source, g.target, mul(g.amp, f.amp),
               sealed_map=protected, derived=True)


def tensor(f, g):
    source_offset = len(f.source.ports)
    target_offset = len(f.target.ports)
    protected = f.sealed_map + tuple(
        (source_offset + source, target_offset + target)
        for source, target in g.sealed_map
    )
    return Mor(f"({f.name} x {g.name})", f.source.tensor(g.source),
               f.target.tensor(g.target), kron(f.amp, g.amp),
               sealed_map=protected, derived=True)


def unravel(index, dims):
    values = [0] * len(dims)
    for k in range(len(dims) - 1, -1, -1):
        values[k] = index % dims[k]
        index //= dims[k]
    return tuple(values)


def ravel(values, dims):
    out = 0
    for value, dim in zip(values, dims):
        out = out * dim + value
    return out


def swap_mor(a, b):
    source, target = a.tensor(b), b.tensor(a)
    rows = [[0 for _ in range(source.dim)] for _ in range(target.dim)]
    ad, bd = tuple(p.dim for p in a.ports), tuple(p.dim for p in b.ports)
    dims = ad + bd
    for col in range(source.dim):
        labels = unravel(col, dims)
        swapped = labels[len(ad):] + labels[:len(ad)]
        row = ravel(swapped, bd + ad)
        rows[row][col] = 1
    protected = []
    for source_pos, port in enumerate(a.ports):
        if port.sealed:
            protected.append((source_pos, len(b.ports) + source_pos))
    for local_pos, port in enumerate(b.ports):
        if port.sealed:
            protected.append((len(a.ports) + local_pos, local_pos))
    return Mor("swap", source, target, matrix(rows),
               sealed_map=tuple(protected), derived=True)


def seal_birth_mor(system, record, collar):
    target = system.tensor(record).tensor(collar)
    rows = [[0 for _ in range(system.dim)] for _ in range(target.dim)]
    for j in range(system.dim):
        row = ravel((j, j, 1), (system.dim, record.dim, collar.dim))
        rows[row][j] = 1
    return Mor("seal_birth", system, target, matrix(rows))


def system_only_mor(system_map, system, record, collar):
    obj = system.tensor(record).tensor(collar)
    return Mor("future_system_only", obj, obj,
               kron(kron(system_map, eye(record.dim)), eye(collar.dim)))


def record_copy_mor(system, record, collar, reread):
    source = system.tensor(record).tensor(collar)
    target = source.tensor(reread)
    rows = [[0 for _ in range(source.dim)] for _ in range(target.dim)]
    dims = (system.dim, record.dim, collar.dim)
    for col in range(source.dim):
        s, r, c = unravel(col, dims)
        row = ravel((s, r, c, r), dims + (reread.dim,))
        rows[row][col] = 1
    return Mor("repeat_read", source, target, matrix(rows))


def append_history_record_mor(current, fresh_record):
    """Locally copy the leading binary system label into one fresh seal."""
    if not current.ports or current.ports[0].dim != 2 or fresh_record.dim != 2:
        raise ValueError("binary history seal requires a leading qubit")
    target = current.tensor(Obj((fresh_record,)))
    rows = [[0 for _ in range(current.dim)] for _ in range(target.dim)]
    source_dims = tuple(port.dim for port in current.ports)
    target_dims = source_dims + (2,)
    for col in range(current.dim):
        labels = unravel(col, source_dims)
        row = ravel(labels + (labels[0],), target_dims)
        rows[row][col] = 1
    return Mor("append_history_record", current, target, matrix(rows))


def append_selected_bit_mor(current, bit_position, fresh_record):
    """Copy one declared live binary carrier into a new protected record."""
    source_dims = tuple(port.dim for port in current.ports)
    if source_dims[bit_position] != 2 or fresh_record.dim != 2:
        raise ValueError("selected-bit seal requires binary carriers")
    target = current.tensor(Obj((fresh_record,)))
    rows = [[0 for _ in range(current.dim)] for _ in range(target.dim)]
    for col in range(current.dim):
        labels = unravel(col, source_dims)
        row = ravel(labels + (labels[bit_position],), source_dims + (2,))
        rows[row][col] = 1
    return Mor("append_selected_bit_record", current, target, matrix(rows))


def local_record_history_network(depth, qubit, u):
    network = ident(qubit)
    for step in range(depth):
        current = network.target
        record_dim = current.dim // 2
        evolve = Mor(f"history_evolve_{step}", current, current,
                     kron(u, eye(record_dim)))
        fresh = Port(f"history-record-{step}", 2, sealed=True)
        seal = append_history_record_mor(current, fresh)
        network = compose(seal, compose(evolve, network))
    return network


def branch_from_local_history(state, history):
    depth = len(history)
    dims = (2,) + (2,) * depth
    return tuple(
        amp if unravel(index, dims)[1:] == history else ZERO
        for index, amp in enumerate(state)
    )


def live_gate_mor(system, record, collar):
    """A continuation opportunity exists only on collar label live=1."""
    obj = system.tensor(record).tensor(collar)
    rows = [[0 for _ in range(obj.dim)] for _ in range(obj.dim)]
    dims = (system.dim, record.dim, collar.dim)
    for col in range(obj.dim):
        labels = unravel(col, dims)
        if labels[2] == 1:
            rows[col][col] = 1
    return Mor("live_gate", obj, obj, matrix(rows))


def preserves_record(mor, src_record_index, tgt_record_index):
    sd = tuple(p.dim for p in mor.source.ports)
    td = tuple(p.dim for p in mor.target.ports)
    for row in range(mor.target.dim):
        out_labels = unravel(row, td)
        for col in range(mor.source.dim):
            if mor.amp[row][col] != ZERO:
                in_labels = unravel(col, sd)
                if in_labels[src_record_index] != out_labels[tgt_record_index]:
                    return False
    return True


def class_operator(history, u):
    out = eye(2)
    for outcome in history:
        out = mul(projector(2, outcome), mul(u, out))
    return out


def history_probability(history, u, rho):
    c = class_operator(history, u)
    return trace(mul(c, mul(rho, dagger(c))))


def all_histories(depth):
    return tuple(product((0, 1), repeat=depth))


def recorded_branch(history, u, initial):
    """System branch tensored with an explicit orthogonal history record."""
    system_branch = mv(class_operator(history, u), initial)
    record_index = ravel(history, (2,) * len(history))
    record_branch = basis(2 ** len(history), record_index)
    return tuple(x * y for x in system_branch for y in record_branch)


def cnot_permutation(control, target):
    rows = [[0 for _ in range(16)] for _ in range(16)]
    for labels in product((0, 1), repeat=4):
        source = ravel(labels, (2, 2, 2, 2))
        out = list(labels)
        out[target] ^= out[control]
        rows[ravel(tuple(out), (2, 2, 2, 2))][source] = 1
    return matrix(rows)


def reset_memory_kraus():
    """CPTP reset M->0 on the ordered X,M,Y,Z carrier."""
    out = []
    for old_memory in (0, 1):
        rows = [[0 for _ in range(16)] for _ in range(16)]
        for x, y, zbit in product((0, 1), repeat=3):
            source = ravel((x, old_memory, y, zbit), (2, 2, 2, 2))
            target = ravel((x, 0, y, zbit), (2, 2, 2, 2))
            rows[target][source] = 1
        out.append(matrix(rows))
    return tuple(out)


def integrated_memory_history_tables(first_copy, final_copy):
    """One local protected network with projectivity and visible memory."""
    base = Obj(tuple(Port(kind, 2) for kind in ("X", "M", "Y", "Z")))
    first = Mor("store-X-in-M", base, base, first_copy)
    seal_x = append_selected_bit_mor(base, 0, Port("visible-X", 2, sealed=True))
    net1 = compose(seal_x, first)

    seal_y = append_selected_bit_mor(net1.target, 2, Port("visible-Y", 2, sealed=True))
    net2 = compose(seal_y, net1)

    reveal = Mor("reveal-M-in-Z", net2.target, net2.target, kron(final_copy, eye(4)))
    seal_z = append_selected_bit_mor(net2.target, 3, Port("visible-Z", 2, sealed=True))
    net3 = compose(seal_z, compose(reveal, net2))

    tables = {}
    for depth, network in ((1, net1), (2, net2), (3, net3)):
        table = {hist: Q2() for hist in all_histories(depth)}
        for initial_index in (0, 8):
            out = mv(network.amp, basis(16, initial_index))
            dims = (2, 2, 2, 2) + (2,) * depth
            for index, amp in enumerate(out):
                hist = unravel(index, dims)[4:]
                table[hist] += F(1, 2) * amp.norm2()
        tables[depth] = table
    return tables


def row_normalize(a):
    rows = []
    for row in a:
        total = sum(row, ZERO)
        rows.append(tuple(x / total for x in row))
    return tuple(rows)


def diagonal_inverse(a):
    rows = [[ZERO for _ in range(len(a))] for _ in range(len(a))]
    for j in range(len(a)):
        rows[j][j] = ONE / a[j][j]
    return tuple(tuple(row) for row in rows)


def main():
    dep_hash = sha256(DEPENDENCY.read_bytes()).hexdigest()
    check(dep_hash == EXPECTED_DEPENDENCY_SHA256, "reviewed exact arithmetic dependency hash")

    q = Obj((Port("q", 2),))
    s = Obj((Port("system2q", 4),))
    r = Obj((Port("record", 4, sealed=True),))
    c = Obj((Port("collar", 2),))
    rr = Obj((Port("reread", 4),))
    h = matrix(((ROOT_HALF, ROOT_HALF), (ROOT_HALF, -ROOT_HALF)))
    z = matrix(((1, 0), (0, -1)))
    phase = matrix(((1, 0), (0, II)))
    hmor, zmor, pmor = Mor("H", q, q, h), Mor("Z", q, q, z), Mor("P", q, q, phase)

    # B0/B1: typed category and exact coherence cells.
    check(compose(ident(q), hmor).amp == h and compose(hmor, ident(q)).amp == h,
          "left and right identity laws")
    lhs = compose(pmor, compose(zmor, hmor))
    rhs = compose(compose(pmor, zmor), hmor)
    check(lhs.amp == rhs.amp, "three-diamond composition associativity")
    check(tensor(tensor(hmor, zmor), pmor).amp == tensor(hmor, tensor(zmor, pmor)).amp,
          "tensor associativity on the strict carrier skeleton")
    interchange_l = compose(tensor(zmor, pmor), tensor(hmor, hmor))
    interchange_r = tensor(compose(zmor, hmor), compose(pmor, hmor))
    check(interchange_l.amp == interchange_r.amp, "interchange law for disjoint diamonds")
    swapqq = swap_mor(q, q)
    natural_l = compose(swapqq, tensor(hmor, zmor))
    natural_r = compose(tensor(zmor, hmor), swapqq)
    check(natural_l.amp == natural_r.amp, "symmetry naturality")
    check(compose(swapqq, swapqq).amp == eye(4), "symmetry involution")
    try:
        compose(hmor, tensor(hmor, hmor))
        ill_typed_rejected = False
    except ValueError:
        ill_typed_rejected = True
    check(ill_typed_rejected, "ill-typed boundary gluing is rejected")
    owned_a = Obj((Port("live", 2, owner="A"),))
    owned_b = Obj((Port("live", 2, owner="B"),))
    joined = Obj((Port("joined", 2, owner="AB"),))
    join_amp = matrix(((1, 0, 0, 0), (0, 0, 0, 1)))
    signature = Signature()
    try:
        signature.declare("unowned_join", owned_a.tensor(owned_b), joined, join_amp)
        unowned_join_rejected = False
    except ValueError:
        unowned_join_rejected = True
    try:
        Mor("raw_unowned_join", owned_a.tensor(owned_b), joined, join_amp)
        raw_unowned_join_rejected = False
    except ValueError:
        raw_unowned_join_rejected = True
    entitled_join = signature.declare("entitled_join", owned_a.tensor(owned_b), joined,
                                      join_amp, join_entitlement=("A", "B"))
    check(unowned_join_rejected and raw_unowned_join_rejected
          and entitled_join.source == owned_a.tensor(owned_b),
          "primitive admission rejects direct and signature unowned joins and admits entitlement")

    rec_a = Obj((Port("record-A", 2, sealed=True, owner="A", record_id="RA"),))
    rec_b = Obj((Port("record-B", 2, sealed=True, owner="B", record_id="RB"),))
    sealed_join_target = rec_a.tensor(rec_b).tensor(joined)
    sealed_join_rows = [[0 for _ in range(4)] for _ in range(8)]
    for a_label, b_label in product((0, 1), repeat=2):
        sealed_join_rows[ravel((a_label, b_label, 0), (2, 2, 2))][
            ravel((a_label, b_label), (2, 2))] = 1
    try:
        Mor("sealed_owner_join_bypass", rec_a.tensor(rec_b), sealed_join_target,
            matrix(sealed_join_rows))
        sealed_join_rejected = False
    except ValueError:
        sealed_join_rejected = True
    check(sealed_join_rejected,
          "primitive admission includes owned sealed inputs in join entitlement")
    protected_swap = swap_mor(rec_a, rec_b)
    fresh_left = append_history_record_mor(q,
        Port("fresh-left", 2, sealed=True, record_id="fresh-left"))
    protected_tensor = tensor(fresh_left, ident(rec_a))
    check(compose(swap_mor(rec_b, rec_a), protected_swap).amp == eye(4)
          and len(protected_tensor.sealed_map) == 1,
          "persistent record correspondences close protected symmetry and fresh-record tensor")
    try:
        Mor("owner_reassignment", rec_a,
            Obj((Port("record-A", 2, sealed=True, owner="B", record_id="RA"),)), eye(2))
        owner_reassignment_rejected = False
    except ValueError:
        owner_reassignment_rejected = True
    check(owner_reassignment_rejected, "protected record owner reassignment is rejected")

    # B2: construction order gauge for a nontrivial disjoint diagram.
    disjoint_a = compose(tensor(zmor, pmor), tensor(hmor, hmor))
    disjoint_b = compose(tensor(ident(q), pmor),
                         compose(tensor(zmor, ident(q)), tensor(hmor, hmor)))
    check(disjoint_a.amp == disjoint_b.amp,
          "two topological schedules of the same disjoint diagram agree")

    # B3: coherent gluing and classical-normalization controls.
    ket0 = basis(2, 0)
    coherent = mv(mul(h, h), ket0)[0].norm2()
    after_h = mv(h, ket0)
    inserted = sum((after_h[j].norm2() * h[0][j].norm2() for j in range(2)), Q2())
    check(coherent == Q2.make(1) and inserted == Q2(F(1, 2)),
          "intermediate record changes coherent interference")
    raw = matrix(((1, 1), (1, 0)))
    raw_composite = mul(raw, raw)
    local_norm_composite = mul(row_normalize(raw), row_normalize(raw))
    global_norm_composite = row_normalize(raw_composite)
    check(local_norm_composite != global_norm_composite,
          "local row normalization fails coherent/composite consistency")
    manual_00 = sum((raw[0][k] * raw[k][0] for k in range(2)), ZERO)
    check(raw_composite[0][0] == manual_00,
          "internal boundary contraction equals the finite path-amplitude sum")

    # B4: internal unitary frame cancellation.
    f, g = h, phase
    ga, gb, gc = z, h, phase
    fp = mul(gb, mul(f, dagger(ga)))
    gp = mul(gc, mul(g, dagger(gb)))
    check(mul(gp, fp) == mul(gc, mul(mul(g, f), dagger(ga))),
          "independent internal unitary frame cancels on a glued boundary")
    rho0 = outer(ket0, ket0)
    effect0 = projector(2, 0)
    original_p = trace(mul(effect0, mul(mul(mul(g, f), rho0), dagger(mul(g, f)))))
    rho_a = mul(ga, mul(rho0, dagger(ga)))
    effect_c = mul(gc, mul(effect0, dagger(gc)))
    transformed_p = trace(mul(effect_c, mul(mul(mul(gp, fp), rho_a), dagger(mul(gp, fp)))))
    check(original_p == transformed_p, "closed probability is unitary-frame invariant")

    # Dual SL(2,C) positive-cone pairing.  G=diag(2,1/2), det G=1.
    boost = matrix(((2, 0), (0, F(1, 2))))
    boost_inv = diagonal_inverse(boost)
    xstate = matrix(((1, 0), (0, 2)))
    effect = matrix(((3, 0), (0, 4)))
    xp = mul(boost, mul(xstate, dagger(boost)))
    ep = mul(dagger(boost_inv), mul(effect, boost_inv))
    check(boost[0][0] * boost[1][1] == ONE and trace(mul(ep, xp)) == trace(mul(effect, xstate)),
          "dual SL(2,C) state/effect pairing is invariant")
    check(xp[0][0].re.a > 0 and xp[1][1].re.a > 0,
          "rank-two positive cone is preserved in the exact boost cell")

    # B5: seal, live birth, protected future and repeat read.
    seal = seal_birth_mor(s, r, c)
    check(mul(dagger(seal.amp), seal.amp) == eye(4), "seal-and-live-collar map is isometric")
    future_system = kron(h, eye(2))
    future = system_only_mor(future_system, s, r, c)
    check(preserves_record(future, 1, 1), "licensed future system dynamics preserves sealed record label")
    reread = record_copy_mor(s, r, c, rr)
    check(preserves_record(reread, 1, 1), "fresh repeat-read map preserves the sealed source record")
    ket10 = basis(4, 2)
    uq = iswap(ROOT_HALF, ROOT_HALF)
    sealed_state = mv(seal.amp, mv(uq, ket10))
    later_state = mv(future.amp, sealed_state)
    reread_state = mv(reread.amp, later_state)
    mismatch_mass = Q2()
    for idx, amp in enumerate(reread_state):
        _, rec, _, read = unravel(idx, (4, 4, 2, 4))
        if rec != read:
            mismatch_mass += amp.norm2()
    check(mismatch_mass == Q2(), "repeat-read disagreement mass is exactly zero")
    collar_dead_mass = sum((amp.norm2() for idx, amp in enumerate(sealed_state)
                            if unravel(idx, (4, 4, 2))[2] == 0), Q2())
    check(collar_dead_mass == Q2(), "every seal branch emits the declared live collar")
    overwrite = kron(kron(eye(4), matrix(((0, 1, 0, 0), (1, 0, 0, 0),
                                          (0, 0, 1, 0), (0, 0, 0, 1)))), eye(2))
    try:
        Mor("overwrite", s.tensor(r).tensor(c), s.tensor(r).tensor(c), overwrite)
        overwrite_rejected = False
    except ValueError:
        overwrite_rejected = True
    check(overwrite_rejected, "sealed-record overwrite constructor is rejected")
    check(preserves_record(compose(future, ident(future.source)), 1, 1)
          and preserves_record(tensor(future, ident(q)), 1, 1),
          "protected morphisms are closed in executed composition and tensor cells")

    # A later opportunity in this frozen grammar requires the live collar.
    live_gate = live_gate_mor(s, r, c)
    check(compose(live_gate, seal).source == s,
          "declared live-collar continuation composes after the seal")
    no_collar_target = s.tensor(r)
    no_collar_rows = [[0 for _ in range(s.dim)] for _ in range(no_collar_target.dim)]
    for j in range(s.dim):
        no_collar_rows[ravel((j, j), (4, 4))][j] = 1
    no_collar_seal = Mor("no_collar_seal", s, no_collar_target, matrix(no_collar_rows))
    try:
        compose(live_gate, no_collar_seal)
        no_collar_rejected = False
    except ValueError:
        no_collar_rejected = True
    dead_input = basis(32, ravel((0, 0, 0), (4, 4, 2)))
    check(no_collar_rejected, "omitted collar cannot feed the declared continuation")
    check(all(x == ZERO for x in mv(live_gate.amp, dead_input)),
          "dead collar has zero licensed continuation amplitude")

    # B6/B7: history decoherence, normalization and projective cylinders.
    rho_plus = outer((ROOT_HALF, ROOT_HALF), (ROOT_HALF, ROOT_HALF))
    probs = {depth: {hist: history_probability(hist, h, rho_plus)
                     for hist in all_histories(depth)} for depth in (1, 2, 3)}
    local_states = {
        depth: mv(local_record_history_network(depth, q, h).amp,
                  (ROOT_HALF, ROOT_HALF))
        for depth in (1, 2, 3)
    }
    local_probs = {
        depth: {
            hist: inner(branch_from_local_history(local_states[depth], hist),
                        branch_from_local_history(local_states[depth], hist))
            for hist in all_histories(depth)
        }
        for depth in (1, 2, 3)
    }
    check(local_probs == probs,
          "sequential local protected instruments realize every depth-one-to-three cylinder")
    check(all(sum((p for p in probs[d].values()), ZERO) == ONE for d in (1, 2, 3)),
          "depth-one through depth-three recorded histories normalize")
    check(all(p.im == Q2() and p.re.b == 0 and p.re.a >= 0
              for table in probs.values() for p in table.values()),
          "recorded history diagonals are exact nonnegative reals")
    decoherent = True
    for depth in (1, 2, 3):
        for alpha in all_histories(depth):
            for beta in all_histories(depth):
                d_ab = inner(branch_from_local_history(local_states[depth], beta),
                             branch_from_local_history(local_states[depth], alpha))
                expected = probs[depth][alpha] if alpha == beta else ZERO
                if d_ab != expected:
                    decoherent = False
    check(decoherent,
          "explicit protected record strings give the exact diagonal decoherence functional")
    projective = True
    for depth in (1, 2):
        for hist in all_histories(depth):
            child_sum = probs[depth + 1][hist + (0,)] + probs[depth + 1][hist + (1,)]
            if child_sum != probs[depth][hist]:
                projective = False
    check(projective, "future complete instruments preserve past cylinders through depth three")
    # One selected conditional is computed once from cylinder ratios.
    parent = probs[1][(0,)]
    conditional = probs[2][(0, 1)] / parent
    check(parent != ZERO and conditional == HALF,
          "next-record conditional is exactly one-half by one disintegration")

    # B8: actual reversible memory circuit and visible non-Markov conditionals.
    umem = memory_copy_unitary()
    rho_mem_in = scale(HALF, add(outer(basis(16, 0), basis(16, 0)),
                                 outer(basis(16, 8), basis(16, 8))))
    rho_mem_out = mul(umem, mul(rho_mem_in, dagger(umem)))
    hist_mass = {}
    for x in range(2):
        for y in range(2):
            for zz in range(2):
                hist_mass[(x, y, zz)] = sum(
                    (rho_mem_out[ravel((x, m, y, zz), (2, 2, 2, 2))]
                                [ravel((x, m, y, zz), (2, 2, 2, 2))]
                     for m in range(2)), ZERO)
    p1 = hist_mass[(1, 0, 1)] / (hist_mass[(1, 0, 0)] + hist_mass[(1, 0, 1)])
    p0 = hist_mass[(0, 0, 1)] / (hist_mass[(0, 0, 0)] + hist_mass[(0, 0, 1)])
    check(mul(dagger(umem), umem) == eye(16) and p1 == ONE and p0 == ZERO,
          "unitary hidden memory produces exact visible non-Markov conditionals")
    first_copy = cnot_permutation(0, 1)
    final_copy = cnot_permutation(1, 3)
    integrated = integrated_memory_history_tables(first_copy, final_copy)
    integrated_projective = all(
        integrated[d][hist] == integrated[d + 1][hist + (0,)] + integrated[d + 1][hist + (1,)]
        for d in (1, 2) for hist in all_histories(d)
    )
    check(integrated_projective
          and integrated[3][(1, 0, 1)] == Q2.make(F(1, 2))
          and integrated[3][(0, 0, 0)] == Q2.make(F(1, 2)),
          "one sequential protected local-memory packet is projective and visibly non-Markov")
    reset_kraus = reset_memory_kraus()
    check(add(mul(dagger(reset_kraus[0]), reset_kraus[0]),
              mul(dagger(reset_kraus[1]), reset_kraus[1])) == eye(16),
          "hidden-memory reset is an exact complete CPTP instrument")
    rho_stored = mul(first_copy, mul(rho_mem_in, dagger(first_copy)))
    rho_reset = add(mul(reset_kraus[0], mul(rho_stored, dagger(reset_kraus[0]))),
                    mul(reset_kraus[1], mul(rho_stored, dagger(reset_kraus[1]))))
    rho_deleted = mul(final_copy, mul(rho_reset, dagger(final_copy)))
    deleted_mass = {}
    for x in range(2):
        for y in range(2):
            for zz in range(2):
                deleted_mass[(x, y, zz)] = sum(
                    (rho_deleted[ravel((x, m, y, zz), (2, 2, 2, 2))]
                                [ravel((x, m, y, zz), (2, 2, 2, 2))]
                     for m in range(2)), ZERO)
    deleted_p1 = deleted_mass[(1, 0, 1)] / (
        deleted_mass[(1, 0, 0)] + deleted_mass[(1, 0, 1)])
    deleted_p0 = deleted_mass[(0, 0, 1)] / (
        deleted_mass[(0, 0, 0)] + deleted_mass[(0, 0, 1)])
    check(deleted_p1 == deleted_p0 == ZERO and deleted_p1 != p1,
          "deleting hidden memory changes the visible process and removes past dependence")

    # B9: no-signalling marginal cell.
    bell = (ROOT_HALF, ZERO, ZERO, ROOT_HALF)
    bell_rho = outer(bell, bell)
    local_h = kron(h, eye(2))
    bell_after = mul(local_h, mul(bell_rho, dagger(local_h)))
    check(reduced_second_qubit(bell_rho) == reduced_second_qubit(bell_after),
          "one entangled disjoint-laboratory no-signalling marginal passes")

    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final exact check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    semantic = {
        "schema": "d14-regional-amplitude-record-history-core-exact-v2",
        "scope": "finite typed acyclic circuit diamonds FSDiam",
        "arithmetic": "Q(sqrt(2),i), local reviewed dependency",
        "checks_passed": CHECKS,
        "history_depths": [1, 2, 3],
        "nonmarkov": {"P(z=1|y=0,x=1)": "1", "P(z=1|y=0,x=0)": "0"},
        "verdict": "FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED",
    }
    semantic_bytes = json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    semantic_hash = sha256(semantic_bytes).hexdigest()
    if EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN" and semantic_hash != EXPECTED_SEMANTIC_SHA256:
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet.update({
        "semantic_sha256": semantic_hash,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256": dep_hash,
    })
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {packet['source_sha256']}")
    print(f"DEPENDENCY SHA256: {dep_hash}")
    print("EXECUTABLE VERDICT: FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED")


if __name__ == "__main__":
    main()
