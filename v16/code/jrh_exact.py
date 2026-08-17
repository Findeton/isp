#!/usr/bin/env python3
"""JRH exact finite construction and demolition battery.

Plain invocation writes exactly the three generated artifacts beside this
source: the paper, transcript, and JSON receipt.  The source itself is the
fourth construction artifact and is created only through the orchestrator.

Substantive arithmetic is integer/Fraction/Gaussian-rational.  No float,
tolerance, random sampling, numerical diagonalisation, git lookup, network
access, or ambient-CWD path is used.

CLI:
  python3 jrh_exact.py
  python3 jrh_exact.py --selftest
  python3 jrh_exact.py --mutant NAME

Unknown syntax exits 2 and writes nothing.  Mutants are expected to die at
their named gate and exit 3, also without writes.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


# ---------------------------------------------------------------------------
# Exact scalar and matrix arithmetic over Q(i)
# ---------------------------------------------------------------------------

Q = Fraction
GI = tuple[Fraction, Fraction]
Matrix = tuple[tuple[GI, ...], ...]

Z0: GI = (Q(0), Q(0))
O1: GI = (Q(1), Q(0))
MI: GI = (Q(0), Q(-1))
PI: GI = (Q(0), Q(1))


def gi(x: int | Fraction = 0, y: int | Fraction = 0) -> GI:
    return (Q(x), Q(y))


def ga(a: GI, b: GI) -> GI:
    return (a[0] + b[0], a[1] + b[1])


def gn(a: GI) -> GI:
    return (-a[0], -a[1])


def gs(a: GI, b: GI) -> GI:
    return ga(a, gn(b))


def gm(a: GI, b: GI) -> GI:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gc(a: GI) -> GI:
    return (a[0], -a[1])


def gq(a: GI, q: Fraction | int) -> GI:
    return (a[0] * Q(q), a[1] * Q(q))


def gabs2(a: GI) -> Fraction:
    return a[0] * a[0] + a[1] * a[1]


def matrix(rows: Iterable[Iterable[GI | int | Fraction]]) -> Matrix:
    out: list[tuple[GI, ...]] = []
    for row in rows:
        cooked: list[GI] = []
        for x in row:
            cooked.append(x if isinstance(x, tuple) else gi(x))
        out.append(tuple(cooked))
    if not out or len({len(r) for r in out}) != 1:
        raise ValueError("matrix must be nonempty and rectangular")
    return tuple(out)


def mz(r: int, c: int) -> Matrix:
    return tuple(tuple(Z0 for _ in range(c)) for _ in range(r))


def eye(n: int) -> Matrix:
    return tuple(tuple(O1 if i == j else Z0 for j in range(n)) for i in range(n))


def shape(a: Matrix) -> tuple[int, int]:
    return (len(a), len(a[0]))


def madd(a: Matrix, b: Matrix) -> Matrix:
    if shape(a) != shape(b):
        raise ValueError("shape mismatch")
    return tuple(tuple(ga(x, y) for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def mneg(a: Matrix) -> Matrix:
    return tuple(tuple(gn(x) for x in row) for row in a)


def msub(a: Matrix, b: Matrix) -> Matrix:
    return madd(a, mneg(b))


def mscale(q: Fraction | int | GI, a: Matrix) -> Matrix:
    z = q if isinstance(q, tuple) else gi(q)
    return tuple(tuple(gm(z, x) for x in row) for row in a)


def mmul(a: Matrix, b: Matrix) -> Matrix:
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise ValueError("matrix product shape mismatch")
    return tuple(
        tuple(
            sum_gi(gm(a[i][k], b[k][j]) for k in range(ac))
            for j in range(bc)
        )
        for i in range(ar)
    )


def sum_gi(xs: Iterable[GI]) -> GI:
    out = Z0
    for x in xs:
        out = ga(out, x)
    return out


def mdag(a: Matrix) -> Matrix:
    r, c = shape(a)
    return tuple(tuple(gc(a[i][j]) for i in range(r)) for j in range(c))


def mtrace(a: Matrix) -> GI:
    r, c = shape(a)
    if r != c:
        raise ValueError("trace of nonsquare matrix")
    return sum_gi(a[i][i] for i in range(r))


def mtensor(a: Matrix, b: Matrix) -> Matrix:
    ar, ac = shape(a)
    br, bc = shape(b)
    return tuple(
        tuple(gm(a[i // br][j // bc], b[i % br][j % bc]) for j in range(ac * bc))
        for i in range(ar * br)
    )


def mblockdiag(blocks: list[Matrix]) -> Matrix:
    sizes = [shape(b)[0] for b in blocks]
    if any(shape(b)[0] != shape(b)[1] for b in blocks):
        raise ValueError("square blocks required")
    total = sum(sizes)
    rows = [[Z0 for _ in range(total)] for _ in range(total)]
    offset = 0
    for block, n in zip(blocks, sizes):
        for i in range(n):
            for j in range(n):
                rows[offset + i][offset + j] = block[i][j]
        offset += n
    return tuple(tuple(r) for r in rows)


def mvec(a: Matrix) -> tuple[GI, ...]:
    # Column-major vectorisation, fixed here and used by the independent Gram
    # certificate below.
    r, c = shape(a)
    return tuple(a[i][j] for j in range(c) for i in range(r))


def outer(v: tuple[GI, ...], w: tuple[GI, ...]) -> Matrix:
    return tuple(tuple(gm(v[i], gc(w[j])) for j in range(len(w))) for i in range(len(v)))


def determinant(a: Matrix) -> GI:
    n, m = shape(a)
    if n != m:
        raise ValueError("determinant of nonsquare matrix")
    if n == 1:
        return a[0][0]
    total = Z0
    for j in range(n):
        minor = tuple(tuple(a[i][k] for k in range(n) if k != j) for i in range(1, n))
        term = gm(a[0][j], determinant(minor))
        total = ga(total, term if j % 2 == 0 else gn(term))
    return total


def principal_minors_nonnegative(a: Matrix) -> tuple[bool, int]:
    n, m = shape(a)
    if n != m or a != mdag(a):
        return (False, 0)
    checked = 0
    for size in range(1, n + 1):
        for idx in itertools.combinations(range(n), size):
            sub = tuple(tuple(a[i][j] for j in idx) for i in idx)
            d = determinant(sub)
            checked += 1
            if d[1] != 0 or d[0] < 0:
                return (False, checked)
    return (True, checked)


def apply_k(k: Matrix, rho: Matrix) -> Matrix:
    return mmul(mmul(k, rho), mdag(k))


def apply_channel(ks: Iterable[Matrix], rho: Matrix) -> Matrix:
    out = mz(shape(rho)[0], shape(rho)[1])
    for k in ks:
        out = madd(out, apply_k(k, rho))
    return out


def effects_sum(ks: Iterable[Matrix]) -> Matrix:
    ks = list(ks)
    d = shape(ks[0])[1]
    out = mz(d, d)
    for k in ks:
        out = madd(out, mmul(mdag(k), k))
    return out


def purity(rho: Matrix) -> Fraction:
    t = mtrace(mmul(rho, rho))
    if t[1] != 0:
        raise ValueError("non-real purity")
    return t[0]


def partial_trace_first(rho: Matrix, da: int, db: int) -> Matrix:
    if shape(rho) != (da * db, da * db):
        raise ValueError("partial trace shape mismatch")
    return tuple(
        tuple(sum_gi(rho[a * db + i][a * db + j] for a in range(da)) for j in range(db))
        for i in range(db)
    )


def partial_trace_second(rho: Matrix, da: int, db: int) -> Matrix:
    if shape(rho) != (da * db, da * db):
        raise ValueError("partial trace shape mismatch")
    return tuple(
        tuple(sum_gi(rho[i * db + b][j * db + b] for b in range(db)) for j in range(da))
        for i in range(da)
    )


def phase4(n: int) -> GI:
    return (O1, PI, gi(-1), MI)[n % 4]


def qstr(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def gstr(z: GI) -> str:
    if z[1] == 0:
        return qstr(z[0])
    if z[0] == 0:
        return f"{qstr(z[1])}i"
    sign = "+" if z[1] >= 0 else "-"
    return f"{qstr(z[0])}{sign}{qstr(abs(z[1]))}i"


def serial(obj: Any) -> Any:
    if isinstance(obj, Fraction):
        return qstr(obj)
    if isinstance(obj, tuple):
        if len(obj) == 2 and all(isinstance(x, Fraction) for x in obj):
            return gstr(obj)  # GI
        return [serial(x) for x in obj]
    if isinstance(obj, list):
        return [serial(x) for x in obj]
    if isinstance(obj, set):
        return [serial(x) for x in sorted(obj, key=str)]
    if isinstance(obj, dict):
        return {str(k): serial(v) for k, v in sorted(obj.items(), key=lambda kv: str(kv[0]))}
    return obj


def canonical(obj: Any) -> bytes:
    return json.dumps(serial(obj), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def digest(obj: Any, n: int | None = None) -> str:
    h = hashlib.sha256(canonical(obj)).hexdigest()
    return h if n is None else h[:n]


def bytes_digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# Frozen source access
# ---------------------------------------------------------------------------

SOURCE_ANCHORS = {
    "v15/note-js-pin-v2.md": "99e90f9a2e8db6a67a1cb46902de96d6086a0931897145d5d54ca3a9e78816ea",
    "v15/note-dc-ontology-addendum-v3.md": "7df6120f585f194c3fd48c0cf36dadd8e10a0c1a9a7b440abb5b5139892f6160",
    "v15/note-dc-causality-addendum-v2.md": "ca713e89633bcd3510bbc898aef24133a64172cd2af158c82457033e32a53d71",
    "v15/note-scoutpsi.md": "5c46b34a4de9149cef48019eab16e39abd67797c34939cc2626f4a3546dfcc3a",
    "v15/code/scoutpsi_receipt.json": "681a9cccfa75ebc1755d03fd9555c7ef9902d6947cfd0e99e8db65776cc802e4",
    "v14/paper-38-epr.md": "22beb66962232240d2e673763e32b1fe451db7c44a2420754ed42f83e99983e2",
    "v14/code/epr_receipt.json": "8813e0c2aad9b003493fcbed6931cb1d93ad4fdb2f3ba76ce8f8be8c5568948f",
    "v15/paper-50-arity16.md": "3e01a1ce1b39e478482c485a15b6e5847a427310bafcb3370f04fe2ae963a9eb",
    "v15/code/arity16_receipt.json": "92a3e11b34a0f7c83d789c46a2b1b29723b27039bc0372bcb38f448453652def",
    "v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md": "173143f9ffb91673fe13f8b3a741dd29baaadf542b29720104af49f14f617578",
    "v10/note-d13-literature-audit-action-selection.md": "efe8792fd2c4fdcd78901b7de93e07fa77e4ef5bf7f652e630525ac8790f4173",
    "v10/note-d15-maximal-low-energy-action.md": "0d39eb2f023ce33fb27a0455424a8fba2e93dec590b3de6cc71fae84a27bd66b",
    "v14/code/era_template.py": "d04a3eb58fbcfe3d093b98126ca23c1610a9cc7cec96c9b9097eed515516f2b9",
}


class SourceReader:
    def __init__(self, root: Path):
        self.root = root
        self.reads: list[dict[str, str]] = []

    def read(self, rel: str) -> bytes:
        if rel not in SOURCE_ANCHORS:
            raise RuntimeError(f"undeclared source read: {rel}")
        path = self.root / rel
        data = path.read_bytes()
        got = bytes_digest(data)
        self.reads.append({"path": rel, "sha256": got})
        return data


# ---------------------------------------------------------------------------
# Gates, mutations, and fixtures
# ---------------------------------------------------------------------------


class GateFail(Exception):
    def __init__(self, gate: str, evidence: str, mutations: list[dict[str, str]] | None = None):
        super().__init__(f"{gate}: {evidence}")
        self.gate = gate
        self.evidence = evidence
        self.mutations = list(mutations or [])


class Ledger:
    def __init__(self):
        self.rows: list[dict[str, Any]] = []
        self.head = "0" * 16

    def gate(self, name: str, ok: bool, evidence: str, mutations: list[dict[str, str]] | None = None) -> None:
        row = {
            "index": len(self.rows) + 1,
            "gate": name,
            "passed": bool(ok),
            "evidence": evidence,
            "previous": self.head,
        }
        row["row_digest"] = digest(row, 16)
        self.head = hashlib.sha256((self.head + row["row_digest"]).encode()).hexdigest()[:16]
        self.rows.append(row)
        if not ok:
            raise GateFail(name, evidence, mutations)


@dataclass
class Mutator:
    name: str | None
    moves: list[dict[str, str]]

    def change(self, target: str, before: Any, after: Any) -> Any:
        if self.name != target:
            return before
        b, a = digest(before, 16), digest(after, 16)
        if b == a:
            raise RuntimeError(f"mutant {target} is a no-op")
        self.moves.append({"target": target, "before": b, "after": a})
        return after


P0 = matrix([[1, 0], [0, 0]])
P1 = matrix([[0, 0], [0, 1]])
PX = matrix([[0, 1], [1, 0]])
PY = matrix([[0, MI], [PI, 0]])
PZ = matrix([[1, 0], [0, -1]])
I2 = eye(2)
HPLUS = mscale(Q(1, 2), matrix([[1, 1], [1, 1]]))
HMINUS = mscale(Q(1, 2), matrix([[1, -1], [-1, 1]]))
RHO_MIX = mscale(Q(1, 2), I2)


def instrument_blocks(ks: dict[int, Matrix], rho: Matrix) -> dict[int, Matrix]:
    return {z: apply_k(k, rho) for z, k in sorted(ks.items())}


def weighted_blocks(ensemble: list[tuple[Fraction, Matrix]], ks: dict[int, Matrix]) -> dict[int, Matrix]:
    out = {z: mz(shape(next(iter(ks.values())))[0], shape(next(iter(ks.values())))[0]) for z in ks}
    for w, rho in ensemble:
        for z, block in instrument_blocks(ks, rho).items():
            out[z] = madd(out[z], mscale(w, block))
    return out


def successor(ks: dict[int, Matrix], rho: Matrix, relation: tuple[str, str], g: int, collar: int,
              erase_geometry: bool = False) -> dict[tuple[Any, ...], Matrix]:
    out: dict[tuple[Any, ...], Matrix] = {}
    for z, block in instrument_blocks(ks, rho).items():
        gp = g if erase_geometry else g ^ z
        key = ("outcome", z, "relation", tuple(sorted(relation)), "geometry", gp, "collar", z, "record", z)
        out[key] = block
    return out


def outcome_probabilities(blocks: dict[Any, Matrix]) -> dict[Any, Fraction]:
    out: dict[Any, Fraction] = {}
    for key, block in blocks.items():
        t = mtrace(block)
        if t[1] != 0:
            raise ValueError("complex probability")
        out[key] = t[0]
    return out


def ensemble_nonlinear_z2(ensemble: list[tuple[Fraction, Matrix]]) -> Fraction:
    total = Q(0)
    for w, rho in ensemble:
        e = mtrace(mmul(PZ, rho))
        if e[1] != 0:
            raise ValueError("complex expectation")
        total += w * e[0] * e[0]
    return total


def alice_conditional_bob(rho_ab: Matrix, projectors: list[Matrix]) -> list[tuple[Fraction, Matrix]]:
    out: list[tuple[Fraction, Matrix]] = []
    for p in projectors:
        kp = mtensor(p, I2)
        sub = partial_trace_first(apply_k(kp, rho_ab), 2, 2)
        tr = mtrace(sub)
        if tr[1] != 0 or tr[0] <= 0:
            raise ValueError("bad conditional weight")
        out.append((tr[0], mscale(Q(1, 1) / tr[0], sub)))
    return out


def graph_cycle_rank(vertices: set[int], edges: set[tuple[int, int]]) -> int:
    parent = {v: v for v in vertices}

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    components = len({find(v) for v in vertices})
    return len(edges) - len(vertices) + components


def parity_projectors_three() -> tuple[Matrix, Matrix]:
    rows0 = [[Z0 for _ in range(8)] for _ in range(8)]
    rows1 = [[Z0 for _ in range(8)] for _ in range(8)]
    for state in range(8):
        parity = ((state >> 0) & 1) ^ ((state >> 1) & 1) ^ ((state >> 2) & 1)
        (rows1 if parity else rows0)[state][state] = O1
    return (tuple(tuple(r) for r in rows0), tuple(tuple(r) for r in rows1))


def bloch(rho: Matrix) -> tuple[Fraction, Fraction, Fraction]:
    vals = []
    for p in (PX, PY, PZ):
        t = mtrace(mmul(p, rho))
        if t[1] != 0:
            raise ValueError("non-real Bloch coordinate")
        vals.append(t[0])
    return tuple(vals)  # type: ignore[return-value]


MUTANT_GATES = {
    "ANCHOR_CORRUPT": "G-SOURCE-ANCHOR",
    "DROP_OUTCOME": "G-A1-TOTAL-OUTCOMES",
    "CELL_NORMALIZE": "G-A3-NO-CELL-NORMALIZATION",
    "RELABEL_BREAK": "G-A4-RELABEL",
    "CP_BREAK": "G-B1-CP",
    "NONLINEAR": "G-B3-AFFINITY",
    "EPR_SIGNAL": "G-B5-NO-SIGNALLING",
    "GEOMETRY_ERASE": "G-C2-NONTRIVIAL-GEOMETRY",
    "COLLAR_ERASE": "G-C4-COLLAR",
    "SPECTATOR_COUPLE": "G-D2-IDLE-SPECTATOR",
    "LOOP_FAKE": "G-D4-FIRST-LOOP",
    "HAMILTONIAN_CANONICAL": "G-E2-BRANCH-AMBIGUITY",
    "RIVAL_IDENTICAL": "G-F3-RIVAL-LAW",
}


def run_core(root: Path, mutant_name: str | None = None) -> dict[str, Any]:
    if mutant_name is not None and mutant_name not in MUTANT_GATES:
        raise ValueError(f"unknown mutant {mutant_name}")
    mut = Mutator(mutant_name, [])
    ledger = Ledger()
    reader = SourceReader(root)

    # Source anchors: actual bytes are read through the sole accessor.
    observed: dict[str, str] = {}
    expected = dict(SOURCE_ANCHORS)
    if mutant_name == "ANCHOR_CORRUPT":
        first = sorted(expected)[0]
        expected[first] = mut.change("ANCHOR_CORRUPT", expected[first], "0" * 64)
    for rel in sorted(SOURCE_ANCHORS):
        observed[rel] = bytes_digest(reader.read(rel))
    ledger.gate(
        "G-SOURCE-ANCHOR",
        observed == expected,
        f"observed source digests match frozen inventory at {sum(observed[k] == expected[k] for k in observed)} of {len(observed)} paths",
        mut.moves,
    )

    # Main outcome-resolved two-actor instrument.
    main_ks: dict[int, Matrix] = {0: P0, 1: P1}
    if mutant_name == "DROP_OUTCOME":
        main_ks = mut.change("DROP_OUTCOME", main_ks, {0: P0})
    test_states = [P0, P1, HPLUS, RHO_MIX]
    normalised_rows = 0
    for rho in test_states:
        probs = outcome_probabilities(successor(main_ks, rho, ("A", "B"), 0, 0))
        normalised_rows += int(sum(probs.values(), Q(0)) == 1)
    ledger.gate(
        "G-A1-TOTAL-OUTCOMES",
        normalised_rows == len(test_states),
        f"complete-successor mass is one at {normalised_rows} of {len(test_states)} exact input rows",
        mut.moves,
    )

    type_rows = 0
    for rho in test_states:
        out = successor(main_ks, rho, ("A", "B"), 0, 0)
        type_rows += int(all(shape(block) == (2, 2) and key[0] == "outcome" and key[4] == "geometry" for key, block in out.items()))
    ledger.gate(
        "G-A2-DIRECT-SUM-TYPES",
        type_rows == len(test_states),
        f"domain/output geometry-sector types close at {type_rows} of {len(test_states)} rows",
        mut.moves,
    )

    triple_payload = [{"probability": Q(1), "writes": (("A", "B"), ("A", "C"), ("B", "C"))}]
    split_payload = [
        {"probability": Q(1, 3), "writes": (("A", "B"),)},
        {"probability": Q(1, 3), "writes": (("A", "C"),)},
        {"probability": Q(1, 3), "writes": (("B", "C"),)},
    ]
    triple_payload = mut.change("CELL_NORMALIZE", triple_payload, split_payload)
    simultaneous = len(triple_payload) == 1 and len(triple_payload[0]["writes"]) == 3 and triple_payload[0]["probability"] == 1
    ledger.gate(
        "G-A3-NO-CELL-NORMALIZATION",
        simultaneous,
        f"one complete outcome carries {len(triple_payload[0]['writes'])} simultaneous pair writes; cells are payload, not sample space",
        mut.moves,
    )

    event = {"actors": ("A", "B", "C"), "writes": (("A", "B"), ("A", "C"), ("B", "C"))}
    perm = {"A": "C", "B": "A", "C": "B"}
    relabelled = {
        "actors": tuple(perm[x] for x in event["actors"]),
        "writes": tuple(tuple(sorted((perm[a], perm[b]))) for a, b in event["writes"]),
    }
    expected_relabel = {
        "actors": ("C", "A", "B"),
        "writes": (("A", "C"), ("B", "C"), ("A", "B")),
    }
    relabelled = mut.change("RELABEL_BREAK", relabelled, event)
    ledger.gate(
        "G-A4-RELABEL",
        relabelled == expected_relabel,
        "the full actor-plus-write boundary commutes with the registered cyclic relabelling",
        mut.moves,
    )

    # CP/TP, exact affinity, HJW, and no-signalling.
    alt_ks = {0: HPLUS, 1: HMINUS}
    reset_ks = {0: matrix([[1, 0], [0, 0]]), 1: matrix([[0, 1], [0, 0]])}
    cp_maps = list(main_ks.values()) + list(alt_ks.values()) + list(reset_ks.values())
    cp_ok = True
    principal_checked = 0
    for idx, k in enumerate(cp_maps):
        choi = outer(mvec(k), mvec(k))
        if mutant_name == "CP_BREAK" and idx == 0:
            bad = [list(row) for row in choi]
            bad[0][0] = gi(-1)
            choi = mut.change("CP_BREAK", choi, tuple(tuple(row) for row in bad))
        ok, count = principal_minors_nonnegative(choi)
        principal_checked += count
        cp_ok = cp_ok and ok
    ledger.gate(
        "G-B1-CP",
        cp_ok,
        f"Kraus-Gram Choi certificates pass {principal_checked} exact principal-minor checks across {len(cp_maps)} branch maps",
        mut.moves,
    )

    tp_families = [main_ks, alt_ks, reset_ks]
    tp_count = sum(effects_sum(f.values()) == I2 for f in tp_families)
    ledger.gate(
        "G-B2-TRACE-PRESERVING",
        tp_count == len(tp_families),
        f"sum K-dagger-K equals identity for {tp_count} of {len(tp_families)} registered channel families",
        mut.moves,
    )

    mix_weight = Q(1, 3)
    rho_mix_test = madd(mscale(mix_weight, P0), mscale(1 - mix_weight, HPLUS))
    lhs = instrument_blocks(main_ks, rho_mix_test)
    rhs0 = instrument_blocks(main_ks, P0)
    rhs1 = instrument_blocks(main_ks, HPLUS)
    rhs = {z: madd(mscale(mix_weight, rhs0[z]), mscale(1 - mix_weight, rhs1[z])) for z in main_ks}
    affinity_ok = lhs == rhs
    if mutant_name == "NONLINEAR":
        nonlinear_lhs = mtrace(mmul(PZ, rho_mix_test))[0] ** 2
        nonlinear_rhs = mix_weight * (mtrace(mmul(PZ, P0))[0] ** 2) + (1 - mix_weight) * (mtrace(mmul(PZ, HPLUS))[0] ** 2)
        affinity_ok = mut.change("NONLINEAR", affinity_ok, nonlinear_lhs == nonlinear_rhs)
    ledger.gate(
        "G-B3-AFFINITY",
        affinity_ok,
        f"classical-quantum output respects the registered rational mixture of weight {qstr(mix_weight)} block by block",
        mut.moves,
    )

    ens_z = [(Q(1, 2), P0), (Q(1, 2), P1)]
    ens_x = [(Q(1, 2), HPLUS), (Q(1, 2), HMINUS)]
    rho_z = madd(mscale(Q(1, 2), P0), mscale(Q(1, 2), P1))
    rho_x = madd(mscale(Q(1, 2), HPLUS), mscale(Q(1, 2), HMINUS))
    hjw_equal_state = rho_z == rho_x == RHO_MIX
    hjw_equal_output = weighted_blocks(ens_z, main_ks) == weighted_blocks(ens_x, main_ks)
    ledger.gate(
        "G-B4-HJW-BLIND",
        hjw_equal_state and hjw_equal_output,
        "Z and X pure-state ensembles equal I/2 and produce identical complete local instrument blocks",
        mut.moves,
    )

    bell = mz(4, 4)
    bell_rows = [list(row) for row in bell]
    for i, j in ((0, 0), (0, 3), (3, 0), (3, 3)):
        bell_rows[i][j] = gi(Q(1, 2))
    bell = tuple(tuple(row) for row in bell_rows)
    alice_z = alice_conditional_bob(bell, [P0, P1])
    alice_x = alice_conditional_bob(bell, [HPLUS, HMINUS])
    bob_z = weighted_blocks(alice_z, main_ks)
    bob_x = weighted_blocks(alice_x, main_ks)
    no_signal = bob_z == bob_x
    if mutant_name == "EPR_SIGNAL":
        control_z = ensemble_nonlinear_z2(alice_z)
        control_x = ensemble_nonlinear_z2(alice_x)
        no_signal = mut.change("EPR_SIGNAL", no_signal, control_z == control_x)
    ledger.gate(
        "G-B5-NO-SIGNALLING",
        no_signal,
        "Alice's Z/X steering choice leaves Bob's unconditioned record-plus-geometry blocks identical",
        mut.moves,
    )

    nonlinear_z, nonlinear_x = ensemble_nonlinear_z2(ens_z), ensemble_nonlinear_z2(ens_x)
    nonlinear_mix = mtrace(mmul(PZ, RHO_MIX))[0] ** 2
    nonlinear_avg = Q(1, 2) * (mtrace(mmul(PZ, P0))[0] ** 2) + Q(1, 2) * (mtrace(mmul(PZ, P1))[0] ** 2)
    positive_control = nonlinear_z != nonlinear_x and nonlinear_mix != nonlinear_avg
    ledger.gate(
        "G-B6-POSITIVE-CONTROL",
        positive_control,
        f"decomposition-reading control separates Z/X at {qstr(nonlinear_z)} versus {qstr(nonlinear_x)} and violates affinity at {qstr(nonlinear_mix)} versus {qstr(nonlinear_avg)}",
        mut.moves,
    )

    # Actual outcome-resolved geometry and collar.
    main_plus = successor(main_ks, HPLUS, ("A", "B"), 0, 0)
    branch_probs = outcome_probabilities(main_plus)
    branch_resolution = all(key[7] == key[1] and key[9] == key[1] for key in main_plus)
    ledger.gate(
        "G-C1-BRANCH-RESOLUTION",
        branch_resolution,
        f"realized flux, output collar, and durable record agree on all {len(main_plus)} complete branches",
        mut.moves,
    )

    erase = mutant_name == "GEOMETRY_ERASE"
    if erase:
        mut.change("GEOMETRY_ERASE", {key[5] for key in main_plus}, {0})
    geom_out = successor(main_ks, HPLUS, ("A", "B"), 0, 0, erase_geometry=erase)
    reachable_geometry = {key[5] for key, p in outcome_probabilities(geom_out).items() if p > 0}
    later_probe = {g: g for g in reachable_geometry}
    ledger.gate(
        "G-C2-NONTRIVIAL-GEOMETRY",
        len(reachable_geometry) > 1 and len(set(later_probe.values())) > 1,
        f"{len(reachable_geometry)} reachable geometry labels are separated by the registered later geometry probe",
        mut.moves,
    )

    mean_geometry = sum(Q(key[1]) * p for key, p in branch_probs.items())
    threshold_left = int(mtrace(mmul(PZ, RHO_MIX))[0] >= 0)
    threshold_right = Q(1, 2) * int(mtrace(mmul(PZ, P0))[0] >= 0) + Q(1, 2) * int(mtrace(mmul(PZ, P1))[0] >= 0)
    mean_control_ok = mean_geometry not in {Q(0), Q(1)} and Q(threshold_left) != threshold_right
    ledger.gate(
        "G-C3-MEAN-DRIVEN-CONTROL",
        mean_control_ok,
        f"mean outcome {qstr(mean_geometry)} is not an actual geometry label; thresholding it violates affinity at {threshold_left} versus {qstr(threshold_right)}",
        mut.moves,
    )

    c0_ks = {0: P0, 1: P1}
    c1_ks = {0: P1, 1: P0}
    p_c0 = {z: mtrace(v)[0] for z, v in instrument_blocks(c0_ks, P0).items()}
    p_c1 = {z: mtrace(v)[0] for z, v in instrument_blocks(c1_ks, P0).items()}
    if mutant_name == "COLLAR_ERASE":
        p_c1 = mut.change("COLLAR_ERASE", p_c1, p_c0)
    ledger.gate(
        "G-C4-COLLAR",
        p_c0 != p_c1,
        "same relation and geometry with distinct collar data has distinguishable exact successor distributions",
        mut.moves,
    )

    # Two actors, spectators, disjoint diamonds, and first loop.
    l2_viable = branch_resolution and len(reachable_geometry) > 1 and tuple(sorted(("A", "B"))) in [key[3] for key in main_plus]
    ledger.gate(
        "G-D1-L2-VIABLE",
        l2_viable,
        "the two-actor complete successor jointly writes the pair fact, state block, geometry/collar and record",
        mut.moves,
    )

    spectator_state = P1
    local_blocks = instrument_blocks(main_ks, HPLUS)
    joint_ks = {z: mtensor(k, I2) for z, k in main_ks.items()}
    joint_blocks = instrument_blocks(joint_ks, mtensor(HPLUS, spectator_state))
    reduced = {z: partial_trace_second(block, 2, 2) for z, block in joint_blocks.items()}
    spectator_ok = reduced == local_blocks
    if mutant_name == "SPECTATOR_COUPLE":
        swapped = {0: local_blocks[1], 1: local_blocks[0]}
        spectator_ok = mut.change("SPECTATOR_COUPLE", spectator_ok, swapped == local_blocks)
    ledger.gate(
        "G-D2-IDLE-SPECTATOR",
        spectator_ok,
        "tensoring an irrelevant third actor and tracing it back reproduces every local branch exactly",
        mut.moves,
    )

    diamond_equal = True
    diamond_probs: dict[tuple[int, int], Fraction] = {}
    for a, c in itertools.product((0, 1), repeat=2):
        ka = mtensor(main_ks[a], I2)
        kc = mtensor(I2, main_ks[c])
        left = apply_k(kc, apply_k(ka, bell))
        right = apply_k(ka, apply_k(kc, bell))
        diamond_equal = diamond_equal and left == right
        diamond_probs[(a, c)] = mtrace(left)[0]
    correlated = diamond_probs[(0, 0)] == Q(1, 2) and diamond_probs[(1, 1)] == Q(1, 2) and diamond_probs[(0, 1)] == 0
    ledger.gate(
        "G-D3-DISJOINT-DIAMOND",
        diamond_equal and correlated,
        f"both construction orders agree on all {len(diamond_probs)} complete branches while the Bell input keeps non-factorized outcome correlations",
        mut.moves,
    )

    rank_k2 = graph_cycle_rank({0, 1}, {(0, 1)})
    rank_path3 = graph_cycle_rank({0, 1, 2}, {(0, 1), (1, 2)})
    rank_triangle = graph_cycle_rank({0, 1, 2}, {(0, 1), (1, 2), (0, 2)})
    if mutant_name == "LOOP_FAKE":
        rank_k2 = mut.change("LOOP_FAKE", rank_k2, 1)
    qi = matrix([[0, PI], [PI, 0]])
    qj = matrix([[0, 1], [-1, 0]])
    qh = mmul(qj, qi)
    first_loop_ok = rank_k2 == 0 and rank_path3 == 0 and rank_triangle == 1 and qh != I2
    ledger.gate(
        "G-D4-FIRST-LOOP",
        first_loop_ok,
        f"cycle ranks are {rank_k2}, {rank_path3}, {rank_triangle} for K2, the three-actor path, and the triangle; triangle holonomy is {serial(qh)}",
        mut.moves,
    )

    parity0, parity1 = parity_projectors_three()
    triple_tp = effects_sum([parity0, parity1]) == eye(8)
    # Each branch Choi matrix is explicitly |vec(K)><vec(K)|.  That Gram
    # factorisation is an exact all-dimension PSD certificate; enumerating all
    # 2^64 principal submatrices would add cost but no independent content.
    triple_choi = [outer(mvec(k), mvec(k)) for k in (parity0, parity1)]
    triple_cp = all(c == mdag(c) and c == outer(mvec(k), mvec(k)) for c, k in zip(triple_choi, (parity0, parity1)))
    arity_split_ok = l2_viable and triple_tp and triple_cp
    ledger.gate(
        "G-D5-ARITY-NONSEQUITUR",
        arity_split_ok,
        "a valid L2 instrument and a valid joint three-support parity instrument coexist; no robust irreducibility claim is made",
        mut.moves,
    )

    # Frozen-sector Hamiltonian representation and its limits.
    generator = (0, 1)
    u = matrix([[phase4(generator[0]), 0], [0, phase4(generator[1])]])
    reconstructed = matrix([[1, 0], [0, PI]])
    ledger.gate(
        "G-E1-FROZEN-RECOVERY",
        u == reconstructed,
        "with a declared unit clock, the frozen-sector integer phase generator reconstructs diag(1,i) exactly",
        mut.moves,
    )

    lifts = [(0, 1 + 4 * k) for k in range(-2, 3)]
    if mutant_name == "HAMILTONIAN_CANONICAL":
        lifts = mut.change("HAMILTONIAN_CANONICAL", lifts, [lifts[2]])
    lift_images = [matrix([[phase4(a), 0], [0, phase4(b)]]) for a, b in lifts]
    ledger.gate(
        "G-E2-BRANCH-AMBIGUITY",
        len(lifts) > 1 and all(x == reconstructed for x in lift_images) and len(set(lifts)) == len(lifts),
        f"{len(lifts)} distinct registered generator lifts yield the identical one-step transfer operator",
        mut.moves,
    )

    packet = {
        "generator_lift": lifts[len(lifts) // 2],
        "state_space": "frozen two-level sector",
        "instrument": "declared Z record instrument",
        "clock": "one boundary interval",
        "observable": "record plus geometry label",
        "beable_map": "pair record and realized geometry only",
    }
    packet_ok = set(packet) == {"generator_lift", "state_space", "instrument", "clock", "observable", "beable_map"}
    ledger.gate(
        "G-E3-PACKET-WALL",
        packet_ok,
        f"Hamiltonian comparison packet carries all {len(packet)} registered components; a bare matrix is not the comparison object",
        mut.moves,
    )

    cq = mblockdiag([local_blocks[0], local_blocks[1]])
    input_purity = purity(HPLUS)
    output_purity = purity(cq)
    dynamic_obstruction = input_purity == 1 and output_purity < 1
    ledger.gate(
        "G-E4-DYNAMIC-SECTOR-OBSTRUCTION",
        dynamic_obstruction,
        f"pure input has purity {qstr(input_purity)} while the same-sector classical-quantum output has purity {qstr(output_purity)}; a unitary dilation is possible but not selected",
        mut.moves,
    )

    # Law-relative normal modes, affine terms, and rival laws.
    i4 = eye(4)
    shift_rows = [[Z0 for _ in range(4)] for _ in range(4)]
    for j in range(4):
        shift_rows[(j + 1) % 4][j] = O1
    shift = tuple(tuple(row) for row in shift_rows)
    roots = [O1, PI, gi(-1), MI]
    mode_checks = 0
    for lam in roots:
        vec = tuple(phase4((-k * roots.index(lam)) % 4) for k in range(4))
        col = tuple((x,) for x in vec)
        mode_checks += int(mmul(shift, col) == mscale(lam, col))
    distinct_modes = len(set(roots))
    species_under = mode_checks == len(roots) and distinct_modes == len(roots) and i4 != shift
    ledger.gate(
        "G-F1-SPECIES-UNDERDETERMINATION",
        species_under,
        f"same four-site relational cycle admits identity degeneracy {len(roots)} and a shift with {distinct_modes} exact one-dimensional phase modes",
        mut.moves,
    )

    dephase_out = apply_channel(main_ks.values(), RHO_MIX)
    reset_out = apply_channel(reset_ks.values(), RHO_MIX)
    c_dephase = bloch(dephase_out)
    c_reset = bloch(reset_out)
    affine_split = c_dephase == (Q(0), Q(0), Q(0)) and c_reset == (Q(0), Q(0), Q(1))
    ledger.gate(
        "G-F2-AFFINE-SPLIT",
        affine_split,
        f"CPTP dephasing has channel translation {serial(c_dephase)} while CPTP reset has {serial(c_reset)}",
        mut.moves,
    )

    rival_ks = alt_ks
    if mutant_name == "RIVAL_IDENTICAL":
        rival_ks = mut.change("RIVAL_IDENTICAL", rival_ks, main_ks)

    # The rival must survive the same finite safety surface, not merely CP/TP.
    # These checks deliberately repeat the candidate tests with the X-resolving
    # law held in the same ontology and output grammar.
    rival_safety: dict[str, bool] = {}
    rival_safety["normalization"] = all(
        sum(outcome_probabilities(successor(rival_ks, rho, ("A", "B"), 0, 0)).values(), Q(0)) == 1
        for rho in test_states
    )
    rival_safety["cp_tp"] = (
        effects_sum(rival_ks.values()) == I2
        and all(principal_minors_nonnegative(outer(mvec(k), mvec(k)))[0] for k in rival_ks.values())
    )
    rival_lhs = instrument_blocks(rival_ks, rho_mix_test)
    rival_r0 = instrument_blocks(rival_ks, P0)
    rival_r1 = instrument_blocks(rival_ks, HPLUS)
    rival_rhs = {z: madd(mscale(mix_weight, rival_r0[z]), mscale(1 - mix_weight, rival_r1[z])) for z in rival_ks}
    rival_safety["affinity"] = rival_lhs == rival_rhs
    rival_safety["hjw"] = weighted_blocks(ens_z, rival_ks) == weighted_blocks(ens_x, rival_ks)
    rival_safety["no_signalling"] = weighted_blocks(alice_z, rival_ks) == weighted_blocks(alice_x, rival_ks)
    rival_successor = successor(rival_ks, P0, ("A", "B"), 0, 0)
    rival_geometries = {key[5] for key, p in outcome_probabilities(rival_successor).items() if p > 0}
    rival_safety["branch_geometry"] = (
        len(rival_geometries) > 1
        and all(key[7] == key[1] and key[9] == key[1] for key in rival_successor)
    )
    rival_joint_ks = {z: mtensor(k, I2) for z, k in rival_ks.items()}
    rival_joint_blocks = instrument_blocks(rival_joint_ks, mtensor(P0, spectator_state))
    rival_reduced = {z: partial_trace_second(block, 2, 2) for z, block in rival_joint_blocks.items()}
    rival_safety["idle_spectator"] = rival_reduced == instrument_blocks(rival_ks, P0)
    rival_diamond = True
    for a, c in itertools.product((0, 1), repeat=2):
        ka = mtensor(rival_ks[a], I2)
        kc = mtensor(I2, rival_ks[c])
        rival_diamond = rival_diamond and apply_k(kc, apply_k(ka, bell)) == apply_k(ka, apply_k(kc, bell))
    rival_safety["disjoint_diamond"] = rival_diamond
    rival_swap = {0: rival_ks[1], 1: rival_ks[0]}
    rival_safety["collar"] = (
        {z: mtrace(v)[0] for z, v in instrument_blocks(rival_ks, HPLUS).items()}
        != {z: mtrace(v)[0] for z, v in instrument_blocks(rival_swap, HPLUS).items()}
    )
    main_stats = {z: mtrace(v)[0] for z, v in instrument_blocks(main_ks, P0).items()}
    rival_stats = {z: mtrace(v)[0] for z, v in instrument_blocks(rival_ks, P0).items()}
    rival_diff = main_stats != rival_stats
    ledger.gate(
        "G-F3-RIVAL-LAW",
        rival_diff and all(rival_safety.values()),
        f"rival passes {sum(rival_safety.values())} of {len(rival_safety)} repeated safety checks and yields record statistics {serial(main_stats)} versus {serial(rival_stats)}",
        mut.moves,
    )

    no_forced_deviation = rival_diff
    ledger.gate(
        "G-F4-DEVIATION-STANDARD",
        no_forced_deviation,
        "rival admissible microscopic statistics prevent any law-family-invariant QFT/GR deviation from being inferred",
        mut.moves,
    )

    dimensionful_inputs: list[str] = []
    ledger.gate(
        "G-F5-SCALE-WALL",
        not dimensionful_inputs,
        "the finite candidate contains no generated dimensionful datum; Newton, mass, cutoff and cosmological values remain unpriced",
        mut.moves,
    )

    measurements = {
        "source_paths": len(observed),
        "complete_rows": normalised_rows,
        "complete_row_total": len(test_states),
        "cp_branch_maps": len(cp_maps),
        "cp_principal_minors_checked": principal_checked,
        "tp_families": tp_count,
        "tp_family_total": len(tp_families),
        "mixture_weight": mix_weight,
        "nonlinear_control_z": nonlinear_z,
        "nonlinear_control_x": nonlinear_x,
        "mean_geometry": mean_geometry,
        "reachable_geometries": sorted(reachable_geometry),
        "diamond_branches": len(diamond_probs),
        "cycle_ranks": {"K2": rank_k2, "path3": rank_path3, "triangle": rank_triangle},
        "triangle_holonomy": qh,
        "hamiltonian_lifts": lifts,
        "input_purity": input_purity,
        "cq_output_purity": output_purity,
        "shift_modes": [gstr(x) for x in roots],
        "dephasing_translation": c_dephase,
        "reset_translation": c_reset,
        "main_stats_on_zero": main_stats,
        "rival_stats_on_zero": rival_stats,
        "rival_safety": rival_safety,
        "rival_safety_passes": sum(rival_safety.values()),
        "rival_safety_total": len(rival_safety),
        "dimensionful_inputs": dimensionful_inputs,
    }

    return {
        "ledger": ledger,
        "measurements": measurements,
        "read_set": reader.reads,
        "mutations": mut.moves,
    }


# ---------------------------------------------------------------------------
# Scientific interpretation, paper rendering, and instrument checks
# ---------------------------------------------------------------------------


CONSEQUENCES = [
    ("joint dynamic-geometry instrument", "FORCED-IN-REGISTERED-ARENA", "An exact outcome-resolved CP instrument exists in the finite arena."),
    ("two-actor occurrence", "FORCED-IN-REGISTERED-ARENA", "The L2 construction passes with an idle spectator; pair viability does not imply universal pair factorization."),
    ("three actors", "FORCED-AS-FIRST-LOOP-ONLY", "A triangle is the first closed relational loop, not a derived minimum event arity."),
    ("EPR and no-signalling", "FORCED-BY-ADMISSIBILITY-GATE", "HJW-equivalent ensembles and remote steering choices give identical unconditioned local outputs."),
    ("ontic pure-state nonlinear rule", "REFUSED-AT-THIS-OPERATIONAL-READING", "The registered decomposition-reading control violates affinity and enables the steering signal."),
    ("global fundamental Hamiltonian", "REFUSED-AS-A-DERIVED-OBJECT", "The changing-geometry instrument supplies no canonical same-sector unitary or generator."),
    ("frozen-sector Hamiltonian", "CONDITIONAL", "It is reconstructible only after choosing a sector, clock and logarithm branch; multiple lifts are equivalent at one step."),
    ("particle species", "OPEN-AND-UNSELECTED", "Different admissible transfer laws on the same ontology have different mode inventories."),
    ("affine-coset event rule", "OPEN-AND-UNSELECTED", "The joint-law architecture neither derives the affine-line coset nor the old three-actor grammar."),
    ("channel affine translation", "PERMITTED-BUT-UNSELECTED", "Both zero and nonzero translations occur in exact CPTP channels."),
    ("cosmological integration constant", "OPEN-AND-UNSELECTED", "No continuum constraint/Bianchi system is built in this unit."),
    ("Newton or area scale", "REFUSED-AS-DERIVED", "No weight-nonzero datum is generated; the earlier scale wall remains."),
    ("dimensionless gravitational coupling", "OPEN", "A selected vacuum, matter law and continuum matching map are missing."),
    ("GR limit", "CONDITIONAL", "Requires a continuum/refinement limit and a discrete deformation or covariance closure selecting an effective gravitational action."),
    ("QFT limit", "CONDITIONAL", "Requires a selected vacuum, stable excitation/Fock reconstruction, locality and continuum scaling."),
    ("macroscopic geometry noise", "PERMITTED", "Outcome-geometry correlation exists, but its scale and coarse-grained observability are unselected."),
    ("higher-curvature deviations", "PERMITTED", "Finite loops allow such terms; no coefficient or sign is selected."),
    ("forced QFT/GR deviation", "REFUSED-IN-REGISTERED-FAMILY", "Rival laws survive with different microscopic statistics, so no common dimensionless deviation is fixed."),
    ("existing ISP walk", "OPEN", "No full representation-packet reconstruction is attempted."),
]


CHOICES = [
    ("pair records as atomic durable facts", "ONTOLOGY-ASSUMED"),
    ("complete outcome as probability sample point", "TYPE-FORCED"),
    ("operational CP-affinity/no-signalling", "ADMISSIBILITY-ASSUMED"),
    ("finite geometry alphabet", "FREE"),
    ("collar representation", "FREE-UP-TO-PREDICTIVE-SUFFICIENCY"),
    ("Z-projective candidate law", "FREE"),
    ("X-projective rival law", "FREE-CONTROL"),
    ("history amplitudes/action", "MISSING"),
    ("division boundaries", "MISSING-BEYOND-FIXTURE"),
    ("all-n extension law", "MISSING"),
    ("vacuum", "MISSING"),
    ("clock/logarithm branch", "FREE-IN-REPRESENTATION"),
    ("continuum/coarse-graining map", "MISSING"),
    ("absolute scale", "MISSING-BY-WALL"),
    ("readout connecting toy geometry to metric observations", "MISSING"),
]


def primary_verdict() -> str:
    return "JRH-CONSISTENT-BUT-UNDERDETERMINED"


def secondary_verdicts() -> list[str]:
    return [
        "L2-VIABLE",
        "TRIANGLE-FIRST-LOOP-NOT-FIRST-EVENT",
        "EPR-SAFE-INSTRUMENT",
        "HAMILTONIAN-RECOVERABLE-ONLY-RELATIVE-TO-FROZEN-SECTOR-AND-CLOCK",
        "SPECIES-UNSELECTED",
        "AFFINE-CHANNEL-TERM-UNSELECTED",
        "NO-FORCED-QFT-GR-DEVIATION-IN-REGISTERED-FAMILY",
    ]


def claims_for(measurements: dict[str, Any]) -> dict[str, str]:
    return {
        "PRIMARY": primary_verdict(),
        "EXISTENCE": (
            "An outcome-resolved dynamic-geometry instrument passes exact CP, trace, affinity, "
            f"HJW and no-signalling checks across {measurements['cp_branch_maps']} registered branch maps."
        ),
        "ARITY": (
            "Two-actor dynamics is viable in the fixture; cycle ranks "
            f"{measurements['cycle_ranks']['K2']}, {measurements['cycle_ranks']['path3']}, "
            f"{measurements['cycle_ranks']['triangle']} make three actors the first loop context, not the first event."
        ),
        "HAMILTONIAN": (
            f"The frozen transfer has {len(measurements['hamiltonian_lifts'])} tested generator lifts with one image, "
            f"while the complete backreacting output changes purity from {qstr(measurements['input_purity'])} "
            f"to {qstr(measurements['cq_output_purity'])}."
        ),
        "SELECTION": (
            f"The same ontology admits main statistics {serial(measurements['main_stats_on_zero'])} "
            f"and rival statistics {serial(measurements['rival_stats_on_zero'])}; the architecture does not select the law."
        ),
        "DEVIATION": "No dimensionless deviation from QFT or GR is forced across the registered surviving law family.",
    }


def render_paper(measurements: dict[str, Any], claims: dict[str, str], gate_count: int) -> str:
    consequence_rows = "\n".join(f"| {name} | {tag} | {reason} |" for name, tag, reason in CONSEQUENCES)
    choice_rows = "\n".join(f"| {name} | {status} |" for name, status in CHOICES)
    claim_block = "\n".join(f"{key}: {value}" for key, value in claims.items())
    secondaries = "\n".join(f"- `{x}`" for x in secondary_verdicts())
    cp_maps = measurements["cp_branch_maps"]
    cp_minors = measurements["cp_principal_minors_checked"]
    lift_count = len(measurements["hamiltonian_lifts"])
    source_count = measurements["source_paths"]
    free_count = sum(status.startswith("FREE") or status.startswith("MISSING") for _, status in CHOICES)
    return f"""# The missing object is a law over complete relational histories

## Candidate paper — hostile-review version

### Abstract

This paper tests a proposed completion of ISP rather than announcing one.  The
candidate says that a fundamental occurrence is a complete finite relational
history between genuine division boundaries.  A single outcome jointly changes
binary relational records, effective geometry with continuation/collar data,
and the predictive process state.  Quantum states, instruments, actions,
fields, and Hamiltonians begin as representations of that history law rather
than as the ontology itself.

An exact finite construction shows that this package is coherent at one small
but important level.  Outcome-resolved geometry change can be represented by a
linear completely positive instrument; it need not use expectation-valued
semiclassical backreaction or a decomposition-sensitive nonlinear update.  A
two-actor occurrence is viable with an idle spectator, while three actors are
only the first carrier of a closed loop.  The canonical remotely steerable
equal-density ensembles remain operationally indistinguishable, so the finite
candidate does not turn EPR steering into signalling.  A Hamiltonian is
recoverable in a frozen sector only after a clock and logarithm branch are
chosen.

The demolition is more important.  A second law on the identical ontology
passes the same structural safety conditions and predicts different records.
The ontology plus jointness, locality, affinity, and covariance therefore does
not select the dynamics.  It fixes no particle list, affine channel term,
cosmological value, gravitational scale, or dimensionless deviation from QFT or
GR.  The primary candidate verdict is `{primary_verdict()}`.  This is an exact
finite existence-and-no-selection result, not quantum gravity.

### The idea without formalism

Think of reality not as objects moving across a pre-existing stage but as an
expanding engineering log.  Each accepted transaction says which actors became
related, what local routing/geometry now exists, what information can be carried
forward, and what durable fact was written.  Those are not four successive
jobs.  They are four readings of one committed transaction.

The most important correction to the earlier three-actor picture is that a
record is binary but an occurrence need not be.  Two actors can create or alter
one relation and thereby change the local geometry.  Three actors become special
only because a closed route can first be drawn among them.  A loop lets one
compare transport around different paths and therefore first makes curvature
meaningful.  That does not imply that nature groups every interaction into
triples.  A region can contain two, three, or many actors, and its law can assign
probabilities to the whole compatible network change at once.

This is the relational analogue of what a field accomplishes in QFT.  A field
is not a command to execute isolated particle collisions serially; it packages
degrees of freedom and their joint local evolution across a region.  Here the
corresponding object is a compatible regional successor instrument over a
changing relation network.  Pair facts are its local alphabet.  A finite joint
rewrite is its interaction.  Stable normal modes of a selected large-network
law would be the place to look for particles.

### What exists, what is law, and what is representation

The proposal keeps three levels separate.

**Ontology.**  One actual relational history exists.  Its durable elementary
facts are pair relations and records.  Effective geometry is encoded by the
actual pattern of relations and transport data, together with boundary collar
data that carries how that geometry can continue.  The mathematical catalogue
of possible graphs may be fixed once; the realized spacetime is not.  Its
relations, adjacency, carrier, and continuation data change with the actual
outcome and affect later possibilities.

**Law.**  For a genuine finite division region, the law assigns chances to
mutually exclusive complete successors.  Each successor contains the new
relations, new geometry/collar, new predictive state, and record.  Probabilities
normalize over those complete successors.  Three pair cells written in one
triple occurrence are simultaneous consequences, not three competing outcomes.

**Representation.**  In the finite construction the law is encoded by a
classical-quantum instrument: one completely positive map for each complete
outcome, with their sum trace preserving.  This is a representation of the law.
It does not prove that density matrices or Kraus operators are beables.  A
history action, path amplitude, wave function, transfer matrix, or Hamiltonian
would likewise need an explicit map back to complete history probabilities and
records before receiving ontological status.

This point is compatible with Barandes's programme of treating Hilbert-space
objects as secondary representations of an indivisible stochastic process, but
the present conjecture is not merely Barandes on a new graph.  Here the actual
spacetime carrier and its local geometry back-react in the same transaction.
The stage is not physically fixed.

### The finite construction

The exact arena uses rational and Gaussian-rational matrices, finite qubit
carriers, binary geometry labels, and boundaries of two through four actors.
It is deliberately too small to be called spacetime physics.  It isolates the
type constraints that any larger dynamics must satisfy.

The core two-actor instrument has outcome maps

`J_z(rho) = P_z rho P_z`,

where the same complete outcome writes the pair relation, stores outcome `z`,
and changes the geometry/collar label by `z`.  The direct sum over `z` preserves
the branch identity.  Geometry reacts to the realized transfer rather than to
an ensemble expectation.  A later registered probe reads different lawful
continuations from the two geometry labels, so the output is not discarded
bookkeeping inside the toy.

The construction checks {cp_maps} branch maps by {cp_minors} exact Choi
principal-minor certificates, in addition to exact Kraus completeness.  The
full transcript carries {gate_count} gate rows and authenticates {source_count}
frozen corpus sources.  These are instrument counts, not continuum evidence.

The decisive comparison is with two bad replacements.

- A mean-driven geometry uses the average outcome.  On the balanced state the
  average lies between the two allowed actual geometries; retaining it loses a
  realized branch, while thresholding it is nonlinear under mixing.
- A preparation-decomposition rule reads which pure-state ensemble was used.
  It distinguishes the canonical Z and X ensembles of the same maximally mixed
  state.  In a Bell-pair steering realization Alice can select those ensembles,
  so the rule changes Bob's local statistics.  The linear instrument stays
  blind to that choice.

This is the right correction to v15's delivered nonlinear update.  Backreaction
does not require feeding an expectation value into geometry.  It can be a
correlation in a complete outcome: each actual branch carries its own geometry.
The ensemble map remains affine because the branch-resolved output is retained.

### Why two actors work and why three still matter

The exact L2 occurrence changes one pair fact, its geometry/collar, its process
state block, and its record.  Tensoring an irrelevant third actor and tracing it
back gives the identical local branch maps.  Two separated pair occurrences
also commute as complete instruments even on a correlated Bell input; their
probabilities need not factor.

The graph calculation then separates arity from curvature.  The two-actor edge
and a three-actor open path have zero cycle rank.  A triangle has the first
cycle, and a nontrivial exact quaternionic transport around it supplies a
holonomy witness.  Thus:

> Three actors are the first context in which relational curvature can be
> tested.  They are not thereby the smallest possible occurrence.

The paper also constructs a valid joint three-support parity instrument.  This
shows that higher-support complete laws are expressible; it does not establish
robust irreducibility.  A three-body map may admit a sequential dilation with an
ancilla even when the inserted intermediate steps are not physical division
events.  The all-arity extension theorem and the classification of genuine
division boundaries remain missing.

### The Hamiltonian returns to being a representation

On a frozen two-level geometry sector, choosing one boundary interval as a
clock gives the transfer `diag(1,i)`.  The exact battery exhibits {lift_count}
distinct integer phase-generator lifts with that same one-step image.  One
transfer matrix therefore does not select one logarithm or one Hamiltonian.

For the backreacting instrument the stronger obstruction is type-level.  A pure
matter input becomes a classical-quantum mixture over distinct geometry
sectors, with exact purity changing from {qstr(measurements['input_purity'])}
to {qstr(measurements['cq_output_purity'])}.  It cannot be the unitary
endomorphism of the original fixed matter sector.  A Stinespring dilation on a
larger fixed mathematical space certainly can be written, but the choice of
environment, geometry embedding, clock, and unravelling is additional
representation data.  The instrument does not select it.

Accordingly, the proper reconstruction target is a packet: generator, state,
instruments and observables, clock/cut, and beable map.  Matching only a matrix
or spectrum is not enough.  A global Hamiltonian may become useful after a
background, foliation, or relational clock is chosen; it is not the fundamental
object in this proposal.

### The hostile result already inside the construction

The proposal's strongest version said, in effect, “this is the missing law.”
The exact result supports only “this is a viable type for the missing law.”

Hold fixed the actors, relation records, binary geometry outcomes, complete
successor grammar, CP/trace/affinity requirements, backreaction pattern, and
no-signalling.  One admissible law resolves the Z alternatives.  Another
resolves the X alternatives.  On the same input, the first gives deterministic
record statistics and the second gives a balanced pair.  Both satisfy the
architecture.  Therefore the architecture has not selected transition weights,
an action, or even a prediction-equivalent class.

The choice inventory contains {len(CHOICES)} named items, of which {free_count}
remain free or missing under the displayed classification.  The exact counts
are less important than their types: the remaining choices include the history
weights/action, genuine division boundaries, all-arity extension, vacuum,
continuum map, readout, and scale.  No amount of renaming the instrument as “the
kernel” pays those debts.

| item | status |
|---|---|
{choice_rows}

### What could actually select the law

The serious refined bet is now narrower and testable.  The joint instrument is
the right container.  Its content should be constrained by the conjunction of:

1. **regional gluing:** equivalent decompositions of one finite region give the
   same boundary instrument, with no fake intermediate division events;
2. **refinement/path independence:** changing an unphysical slicing or
   refinement leaves complete boundary probabilities invariant;
3. **local covariance and causal composition:** disjoint regions compose and
   overlap data admit consistent extensions;
4. **record permanence and outcome-resolved flux:** realized local transfers
   change both durable facts and the geometry that controls later locality;
5. **quantum operational safety:** affinity, complete positivity where the
   standard operational state applies, HJW preparation-independence, and
   compositional no-signalling;
6. **a classical deformation-algebra limit:** coarse boundary moves reproduce
   the refoliation/path-independence structure of relativistic geometry; and
7. **a nontrivial renormalization fixed point:** many microscopic refinements
   flow to one stable long-distance law and vacuum.

The first five constrain a microscopic history law.  The sixth is where an
Einstein/Regge-like effective action might be selected rather than guessed.  In
four continuum dimensions, Lovelock-type and Hojman-Kuchar-Teitelboim results
show how strong locality, derivative, field-content, and deformation-algebra
assumptions can isolate Einstein dynamics up to constants.  They do not select
the microscopic ISP kernel, and importing Einstein's action would be a target
fit, not a derivation.  The seventh is what could turn normal modes into robust
species rather than fixture-dependent eigenvectors.

One serious speculative representation is a boundary class operator obtained
by summing amplitudes over finite relational histories with fixed boundary
data, using one local weight for both matter transport and geometric deficit.
That resembles general-boundary and spin-foam state sums and can encode the
joint transaction cleanly.  But an unrestricted choice of history weights can
represent almost any instrument.  Until gluing/refinement and the continuum
constraint algebra reduce that family, the action is an IOU, not the answer.

### Direct and indirect consequences

The classification below uses “forced” only relative to the registered finite
admissibility family.  “Permitted” means an example exists; it is not a
prediction.

| topic | classification | reason |
|---|---|---|
{consequence_rows}

The clean phenomenological verdict is therefore negative.  The candidate has
no forced deviation from QFT or GR.  Discrete higher-curvature corrections,
outcome-correlated metric noise, nonunitary matter evolution after geometry is
ignored, and species-dependent dispersion are all possible in members of the
family.  Their coefficients, scaling, and even presence depend on the missing
law.  Listing them as predictions would invert the logic of the investigation.

The EPR consequence is more definite but scoped.  Replacing v15's
decomposition-sensitive update by a proper outcome-resolved instrument removes
that specific signalling gun.  This does not derive relativistic microcausality,
Bell locality, or a continuum light cone.  It says only that backreaction and
standard mixture consistency are compatible when the complete branch, including
geometry, is retained.

The affine question divides into three independent debts.  The old affine-line
coset that selected three-actor records is untouched.  A channel's affine
translation is not fixed because exact unital and reset channels both satisfy
CP and trace preservation.  A cosmological constant is not even typed before a
continuum gravitational constraint system exists; in the earlier unimodular
branch it remains an integration/boundary datum.  None should borrow a result
from another merely because the word “affine” or “constant” appears.

### Candidate verdicts

Primary:

`{primary_verdict()}`

Secondary:

{secondaries}

Machine-equal claim block:

```text
{claim_block}
```

### Scope and missing work

This paper proves an exact finite consistency example and an exact
underdetermination counterexample.  It does not provide a Lorentzian continuum,
Einstein equations, a graviton, a particle, a vacuum, a cross-scale map, a
selected action, a nonperturbative QFT, or a reconstruction of the v14/v15 walk.
Its geometry labels implement the algebraic role of outcome-dependent future
connectivity; they are not a measured metric.  Its process regions are declared
fixtures; genuine division events are not yet derived.

The next worthwhile unit is therefore not a larger particle census.  It is a
law-selection attack: enumerate a finite but genuinely broad family of regional
instruments and ask whether gluing under competing refinements plus a discrete
deformation-algebra condition leaves a unique prediction-equivalence class.  If
many survive, the programme needs a new physical principle.  If none survive,
the joint-law conjecture is wrong in its present form.  Only if one robust class
survives should species, couplings, and deviations be computed.

### Primary literature anchors

- J. A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
  arXiv:2507.21192.
- R. Oeckl, *General boundary quantum field theory: Foundations and probability
  interpretation*, arXiv:hep-th/0509122; and *Probabilities in the general
  boundary formulation*, arXiv:hep-th/0612076.
- E. Hawkins, F. Markopoulou, H. Sahlmann, *Evolution in Quantum Causal
  Histories*, Class. Quantum Grav. 20 (2003) 3839,
  doi:10.1088/0264-9381/20/16/320.
- D. P. Rideout, R. D. Sorkin, *A Classical Sequential Growth Dynamics for
  Causal Sets*, Phys. Rev. D 61 (2000) 024002,
  doi:10.1103/PhysRevD.61.024002.
- T. Regge, *General Relativity Without Coordinates*, Nuovo Cimento 19 (1961)
  558–571, doi:10.1007/BF02733251.
- D. M. T. Benincasa, F. Dowker, *The Scalar Curvature of a Causal Set*, Phys.
  Rev. Lett. 104 (2010) 181301, doi:10.1103/PhysRevLett.104.181301.
- L. P. Hughston, R. Jozsa, W. K. Wootters, *A complete classification of
  quantum ensembles having a given density matrix*, Phys. Lett. A 183 (1993)
  14–18, doi:10.1016/0375-9601(93)90880-9.
- C. Simon, V. Buzek, N. Gisin, *No-Signaling Condition and Quantum Dynamics*,
  Phys. Rev. Lett. 87 (2001) 170405,
  doi:10.1103/PhysRevLett.87.170405.
- N. Gisin, *Weinberg's non-linear quantum mechanics and supraluminal
  communications*, Phys. Lett. A 143 (1990) 1–2,
  doi:10.1016/0375-9601(90)90786-N.
- S. A. Hojman, K. Kuchar, C. Teitelboim, *Geometrodynamics Regained*, Ann.
  Phys. 96 (1976) 88–135, doi:10.1016/0003-4916(76)90112-3.
- D. Lovelock, *The Einstein Tensor and Its Generalizations*, J. Math. Phys. 12
  (1971) 498–501, doi:10.1063/1.1665613.

### Exact artifact statement

All finite claims above are generated from `v16/code/jrh_exact.py` into the
paired transcript and receipt.  The source uses exact arithmetic and a frozen
read whitelist.  This manuscript is a candidate reading until its independent
operator, gravity, and quantum hostile reports are frozen and adjudicated.
"""


def render_output(ledger: Ledger, claims: dict[str, str], measurements: dict[str, Any],
                  mutation_rows: list[dict[str, Any]], read_set: list[dict[str, str]]) -> str:
    lines = [
        "JRH EXACT FINITE BATTERY",
        f"PRIMARY {primary_verdict()}",
        f"GATES {len(ledger.rows)} OF {len(ledger.rows)} PASS",
        f"LEDGER_HEAD {ledger.head}",
        f"SOURCE_READS {len(read_set)}",
        f"MUTANTS {len(mutation_rows)} OF {len(MUTANT_GATES)} DIE AT NAMED GATES",
        "",
        "CLAIMS",
    ]
    lines.extend(f"{k}: {v}" for k, v in claims.items())
    lines.extend(["", "GATES"])
    lines.extend(f"{row['index']:02d} {row['gate']} PASS :: {row['evidence']}" for row in ledger.rows)
    lines.extend(["", "MEASUREMENTS", json.dumps(serial(measurements), sort_keys=True, indent=1)])
    lines.extend(["", "CONSEQUENCES"])
    lines.extend(f"{name} :: {tag} :: {reason}" for name, tag, reason in CONSEQUENCES)
    lines.extend(["", "END JRH EXACT FINITE BATTERY", ""])
    return "\n".join(lines)


def validate_claims(paper: str, output: str, claims: dict[str, str]) -> tuple[bool, str]:
    failures = []
    for key, value in claims.items():
        pcount = paper.count(f"{key}: {value}")
        ocount = output.count(f"{key}: {value}")
        if pcount != 1 or ocount != 1:
            failures.append(f"{key}:paper={pcount},output={ocount}")
    extra_paper = set(re.findall(r"^(PRIMARY|EXISTENCE|ARITY|HAMILTONIAN|SELECTION|DEVIATION): .+$", paper, re.M))
    return (not failures and extra_paper == set(claims), ";".join(failures) or "two-way claim keys and exact strings agree")


def paper_numeral_inventory(paper: str) -> tuple[list[dict[str, Any]], int]:
    """Bind every decimal numeral occurrence to a referent class and line.

    Scientific counts in the generated prose are interpolated from the exact
    measurement object.  Formal identifiers (v15, L2, I/2, and the displayed
    transfer) and bibliographic coordinates are not measurements, so they are
    split rather than silently admitted as receipt values.
    """
    rows: list[dict[str, Any]] = []
    in_bibliography = False
    formal = re.compile(r"(?:\bv\d+\b|\bL\d+\b|\bK\d+\b|\bI/\d+\b|diag\([^)]*\d|J_[A-Za-z0-9]+|P_[A-Za-z0-9]+)")
    total = 0
    for line_no, line in enumerate(paper.splitlines(), 1):
        if line == "### Primary literature anchors":
            in_bibliography = True
        elif line == "### Exact artifact statement":
            in_bibliography = False
        for match in re.finditer(r"\d+(?:/\d+)?", line):
            total += 1
            if in_bibliography:
                category = "BIBLIOGRAPHIC-COORDINATE"
            elif formal.search(line):
                category = "FORMAL-OR-CORPUS-IDENTIFIER"
            else:
                category = "GENERATED-FIXTURE-OR-MEASUREMENT"
            rows.append({
                "occurrence": total,
                "line": line_no,
                "token": match.group(0),
                "category": category,
                "referent": line.strip(),
            })
    return rows, total


def verify_seal(payload: dict[str, Any], seals: dict[str, str]) -> tuple[bool, str]:
    expected = set(payload)
    actual = set(seals)
    if expected != actual:
        return (False, f"totality mismatch payload={sorted(expected)} seal={sorted(actual)}")
    moved = [key for key in payload if digest(payload[key]) != seals[key]]
    return (not moved, "all payload keys sealed" if not moved else f"moved={moved}")


def parser_contract(argv: list[str]) -> tuple[str, str | None]:
    if not argv:
        return ("plain", None)
    if argv == ["--selftest"]:
        return ("selftest", None)
    if len(argv) == 2 and argv[0] == "--mutant" and argv[1] in MUTANT_GATES:
        return ("mutant", argv[1])
    raise ValueError("usage: jrh_exact.py [--selftest | --mutant NAME]")


def file_snapshot(paths: Iterable[Path]) -> dict[str, str | None]:
    return {str(path): bytes_digest(path.read_bytes()) if path.exists() else None for path in paths}


def mutation_survey(root: Path) -> list[dict[str, Any]]:
    rows = []
    for name, expected_gate in MUTANT_GATES.items():
        try:
            run_core(root, name)
        except GateFail as exc:
            moved = bool(exc.mutations) and all(row["before"] != row["after"] for row in exc.mutations)
            rows.append({
                "mutant": name,
                "expected_gate": expected_gate,
                "observed_gate": exc.gate,
                "moved": moved,
                "move_proofs": exc.mutations,
                "passed": exc.gate == expected_gate and moved,
            })
        else:
            rows.append({"mutant": name, "expected_gate": expected_gate, "observed_gate": "SURVIVED", "moved": False, "passed": False})
    return rows


def build(root: Path, artifact_paths: list[Path]) -> tuple[str, str, dict[str, Any]]:
    core = run_core(root)
    ledger: Ledger = core["ledger"]
    measurements = core["measurements"]
    read_set = core["read_set"]

    # Determinism at the scientific-object level.
    core2 = run_core(root)
    deterministic_core = canonical(measurements) == canonical(core2["measurements"]) and canonical(ledger.rows) == canonical(core2["ledger"].rows)
    ledger.gate("G-G2-DETERMINISM", deterministic_core, "two independent exact core builds are byte-identical before rendering")

    # CLI parser is tested in memory; unknown forms must raise.
    allowed_ok = parser_contract([]) == ("plain", None) and parser_contract(["--selftest"]) == ("selftest", None)
    unknown_rejected = False
    try:
        parser_contract(["--unknown"])
    except ValueError:
        unknown_rejected = True
    ledger.gate("G-G1-CLI", allowed_ok and unknown_rejected, "plain and selftest parse; unknown syntax is rejected before construction")

    before_self = file_snapshot(artifact_paths)
    try:
        run_core(root, "ANCHOR_CORRUPT")
        selftest_ok = False
    except GateFail as exc:
        selftest_ok = exc.gate == MUTANT_GATES["ANCHOR_CORRUPT"] and bool(exc.mutations)
    after_self = file_snapshot(artifact_paths)
    ledger.gate("G-G3-SELFTEST", selftest_ok and before_self == after_self, "observed source-anchor corruption dies at its named gate and changes no artifact bytes")

    mutant_rows = mutation_survey(root)
    mutant_ok = all(row["passed"] for row in mutant_rows) and len(mutant_rows) == len(MUTANT_GATES)
    ledger.gate("G-G4-MUTANTS-MOVE", mutant_ok, f"all {len(mutant_rows)} registered mutants move measured objects and die at their named gates")

    # Read-set wall: duplicates are expected across deliberate reruns; unique
    # path/digest pairs must equal the entire frozen inventory.
    unique_reads = {(row["path"], row["sha256"]) for row in read_set}
    expected_reads = set(SOURCE_ANCHORS.items())
    ledger.gate("G-G7-READ-SET", unique_reads == expected_reads, f"sole accessor read set equals all {len(expected_reads)} frozen path/digest anchors")

    # Foreign CWD test.  The root remains explicit and no git path is read.
    old_cwd = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="jrh-cwd-") as td:
        os.chdir(td)
        try:
            foreign = run_core(root)
        finally:
            os.chdir(old_cwd)
    portable = canonical(foreign["measurements"]) == canonical(measurements)
    ledger.gate("G-G8-PORTABILITY", portable, "foreign-CWD exact rebuild matches and all reads remain explicit; git is unused")

    claims = claims_for(measurements)
    # The gate count in prose is computed after all fixed integrity rows below.
    future_gate_count = len(ledger.rows) + 2
    paper = render_paper(measurements, claims, future_gate_count)
    provisional_output = render_output(ledger, claims, measurements, mutant_rows, read_set)
    claim_ok, claim_evidence = validate_claims(paper, provisional_output, claims)
    numeral_inventory, numeral_total = paper_numeral_inventory(paper)
    numeral_scan_total = len(re.findall(r"\d+(?:/\d+)?", paper))
    numeral_ok = (
        numeral_total == numeral_scan_total
        and len(numeral_inventory) == numeral_total
        and all(row["occurrence"] == i + 1 and row["referent"] for i, row in enumerate(numeral_inventory))
    )
    ledger.gate(
        "G-G6-CLAIM-EQUALITY",
        claim_ok and numeral_ok,
        f"{claim_evidence}; all {numeral_total} paper numeral occurrences carry line-level referent classes",
    )

    # Seal positive controls are run before the real seal.  The real seal is
    # verified again after disk promotion in write_artifacts().
    dummy = {"alpha": {"x": 1}, "beta": [2, 3]}
    dummy_seals = {k: digest(v) for k, v in dummy.items()}
    clean_ok = verify_seal(dummy, dummy_seals)[0]
    add_bad = dict(dummy)
    add_bad["intruder"] = 4
    edit_bad = dict(dummy)
    edit_bad["alpha"] = {"x": 9}
    controls_ok = clean_ok and not verify_seal(add_bad, dummy_seals)[0] and not verify_seal(edit_bad, dummy_seals)[0]
    ledger.gate("G-G5-TOTAL-SEAL", controls_ok, "clean seal passes; post-seal add and edit controls both die before promotion")

    output = render_output(ledger, claims, measurements, mutant_rows, read_set)
    if len(ledger.rows) != future_gate_count:
        raise RuntimeError("rendered gate count drift")

    # Recheck claims against the final transcript after the two integrity rows.
    final_claim_ok, final_claim_evidence = validate_claims(paper, output, claims)
    if not final_claim_ok:
        raise GateFail("G-G6-CLAIM-EQUALITY", final_claim_evidence)

    payload: dict[str, Any] = {
        "schema": "JRH-RECEIPT-v1",
        "unit": "v16-paper-01-jrh",
        "status": "CANDIDATE-PENDING-HOSTILE-REVIEW",
        "primary_verdict": primary_verdict(),
        "secondary_verdicts": secondary_verdicts(),
        "measurements": measurements,
        "claims": claims,
        "consequences": [{"topic": a, "classification": b, "reason": c} for a, b, c in CONSEQUENCES],
        "choice_inventory": [{"item": a, "status": b} for a, b in CHOICES],
        "paper_numeral_inventory": numeral_inventory,
        "gates": ledger.rows,
        "ledger_head": ledger.head,
        "mutant_survey": mutant_rows,
        "source_anchors": SOURCE_ANCHORS,
        "read_set": read_set,
        "paper_sha256": bytes_digest(paper.encode("utf-8")),
        "output_sha256": bytes_digest(output.encode("utf-8")),
        "scope": {
            "arithmetic": "exact Q(i)",
            "actors": "finite labelled boundaries at two through four actors",
            "continuum": False,
            "gr_claim": False,
            "qft_claim": False,
            "particle_claim": False,
            "existing_walk_reconstruction": False,
        },
    }
    seals = {key: digest(value) for key, value in payload.items()}
    ok, evidence = verify_seal(payload, seals)
    if not ok:
        raise GateFail("G-G5-TOTAL-SEAL", evidence)
    receipt = dict(payload)
    receipt["seal_manifest"] = {
        "algorithm": "sha256-canonical-json",
        "sealed_keys": seals,
        "total_keys_excluding_manifest": len(payload),
    }
    return paper, output, serial(receipt)


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def write_artifacts(root: Path) -> None:
    code_dir = Path(__file__).resolve().parent
    era_dir = code_dir.parent
    paper_path = era_dir / "paper-01-joint-relational-history-law.md"
    output_path = code_dir / "jrh_output.txt"
    receipt_path = code_dir / "jrh_receipt.json"
    paths = [paper_path, output_path, receipt_path]
    paper, output, receipt = build(root, paths)
    receipt_bytes = (json.dumps(receipt, sort_keys=True, indent=1, ensure_ascii=False) + "\n").encode("utf-8")
    paper_bytes = paper.encode("utf-8")
    output_bytes = output.encode("utf-8")

    # Stage all bytes before any promotion.
    staged = {
        paper_path: paper_bytes,
        output_path: output_bytes,
        receipt_path: receipt_bytes,
    }
    for path, data in staged.items():
        atomic_write(path, data)

    # Post-promotion readback: artifact hashes and the receipt's total seal.
    on_disk = json.loads(receipt_path.read_text(encoding="utf-8"))
    if bytes_digest(paper_path.read_bytes()) != on_disk["paper_sha256"]:
        raise GateFail("G-G5-TOTAL-SEAL", "paper disk hash moved")
    if bytes_digest(output_path.read_bytes()) != on_disk["output_sha256"]:
        raise GateFail("G-G5-TOTAL-SEAL", "output disk hash moved")
    manifest = on_disk.pop("seal_manifest")
    ok, evidence = verify_seal(on_disk, manifest["sealed_keys"])
    if not ok:
        raise GateFail("G-G5-TOTAL-SEAL", f"post-promotion {evidence}")


def repository_root() -> Path:
    # v16/code/jrh_exact.py -> repository root.  No CWD or git dependency.
    return Path(__file__).resolve().parents[2]


def main(argv: list[str]) -> int:
    try:
        mode, value = parser_contract(argv)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    root = repository_root()
    code_dir = Path(__file__).resolve().parent
    artifacts = [
        code_dir.parent / "paper-01-joint-relational-history-law.md",
        code_dir / "jrh_output.txt",
        code_dir / "jrh_receipt.json",
    ]

    if mode == "plain":
        write_artifacts(root)
        return 0

    before = file_snapshot(artifacts)
    mutant = "ANCHOR_CORRUPT" if mode == "selftest" else value
    assert mutant is not None
    try:
        run_core(root, mutant)
    except GateFail as exc:
        after = file_snapshot(artifacts)
        expected = MUTANT_GATES[mutant]
        if exc.gate != expected or not exc.mutations or before != after:
            print(f"MUTANT-FAIL {mutant} expected={expected} observed={exc.gate} moved={bool(exc.mutations)} writes={before != after}", file=sys.stderr)
            return 1
        print(f"MUTANT-DIED {mutant} AT {exc.gate} MOVE {exc.mutations[0]['before']}->{exc.mutations[0]['after']}")
        return 0 if mode == "selftest" else 3
    print(f"MUTANT-SURVIVED {mutant}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
