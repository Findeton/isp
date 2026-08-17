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


def relabel_successors(
    rows: dict[tuple[Any, ...], Matrix], perm: dict[str, str]
) -> dict[tuple[Any, ...], Matrix]:
    """Relabel every actor occurrence in the complete nominal successor."""
    out: dict[tuple[Any, ...], Matrix] = {}
    for key, block in rows.items():
        rel = tuple(sorted(perm[x] for x in key[3]))
        cooked = list(key)
        cooked[3] = rel
        out[tuple(cooked)] = block
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
    "FEEDFORWARD_BREAK": "G-C2-FEEDFORWARD-EQUIVALENCE",
    "COLLAR_SMUGGLE": "G-C4-COLLAR-UNINSTANTIATED",
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
    for rel in sorted(SOURCE_ANCHORS):
        observed[rel] = bytes_digest(reader.read(rel))
    if mutant_name == "ANCHOR_CORRUPT":
        first = sorted(observed)[0]
        observed[first] = mut.change("ANCHOR_CORRUPT", observed[first], "0" * 64)
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
        "G-A2-NOMINAL-BRANCH-TYPES",
        type_rows == len(test_states),
        f"matrix blocks and nominal branch-key positions close at {type_rows} of {len(test_states)} rows",
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

    perm = {"A": "C", "B": "A", "C": "B"}
    original_successors = successor(main_ks, HPLUS, ("A", "B"), 1, 0)
    relabelled_successors = relabel_successors(original_successors, perm)
    direct_successors = successor(main_ks, HPLUS, (perm["A"], perm["B"]), 1, 0)
    if mutant_name == "RELABEL_BREAK":
        relabelled_successors = mut.change("RELABEL_BREAK", relabelled_successors, original_successors)
    ledger.gate(
        "G-A4-RELABEL",
        relabelled_successors == direct_successors,
        "the complete nominal successor map commutes with the registered cyclic boundary relabelling",
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
        "Alice's Z/X steering choice leaves Bob's unconditioned complete nominal branch blocks identical",
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

    # The registered division instrument is entanglement breaking.  This is a
    # limitation of this particular instrument, not of every CP instrument.
    bell_after = mz(4, 4)
    for z in (0, 1):
        kz = mtensor(main_ks[z], I2)
        bell_after = madd(bell_after, apply_k(kz, bell))
    bell_classical = mz(4, 4)
    bell_classical_rows = [list(row) for row in bell_classical]
    bell_classical_rows[0][0] = gi(Q(1, 2))
    bell_classical_rows[3][3] = gi(Q(1, 2))
    bell_classical = tuple(tuple(row) for row in bell_classical_rows)
    entanglement_breaking = bell_after == bell_classical and purity(bell_after) == Q(1, 2)
    ledger.gate(
        "G-B7-ENTANGLEMENT-BREAKING",
        entanglement_breaking,
        "the unconditioned Z division map sends the Bell state to the exact separable 00/11 mixture of purity 1/2",
        mut.moves,
    )

    # A rational two-step rotation exposes why this projective instrument
    # cannot be inserted at every microscopic rewrite.  The two unresolved
    # intermediate histories interfere; declaring an intermediate record makes
    # their probabilities add instead.
    rot = matrix([[Q(3, 5), Q(4, 5)], [Q(-4, 5), Q(3, 5)]])
    rotation_unitary = mmul(mdag(rot), rot) == I2
    amp_via_0 = gm(rot[0][0], rot[0][0])
    amp_via_1 = gm(rot[0][1], rot[1][0])
    coherent_probability = gabs2(ga(amp_via_0, amp_via_1))
    divided_probability = gabs2(amp_via_0) + gabs2(amp_via_1)
    interference_survives = (
        rotation_unitary
        and coherent_probability == Q(49, 625)
        and divided_probability == Q(337, 625)
        and coherent_probability != divided_probability
    )
    ledger.gate(
        "G-B8-DIVISION-BOUNDARY",
        interference_survives,
        f"unresolved rational paths give {qstr(coherent_probability)} while an inserted intermediate record gives {qstr(divided_probability)}",
        mut.moves,
    )

    # The originally advertised geometry and collar are copied branch memory.
    # These gates now measure that negative exactly instead of promoting the
    # labels to spacetime.
    main_plus = successor(main_ks, HPLUS, ("A", "B"), 0, 0)
    branch_probs = outcome_probabilities(main_plus)
    branch_resolution = all(key[7] == key[1] and key[9] == key[1] for key in main_plus)
    ledger.gate(
        "G-C1-BRANCH-MEMORY",
        branch_resolution,
        f"the output collar label and durable record copy the outcome on all {len(main_plus)} nominal branches",
        mut.moves,
    )

    erase = mutant_name == "FEEDFORWARD_BREAK"
    geom_out = successor(main_ks, HPLUS, ("A", "B"), 0, 0)
    if erase:
        bad = dict(geom_out)
        first_key = sorted(bad, key=repr)[0]
        cooked = list(first_key)
        cooked[9] = 1 - int(cooked[9])
        moved_key = tuple(cooked)
        bad[moved_key] = bad.pop(first_key)
        geom_out = mut.change("FEEDFORWARD_BREAK", geom_out, bad)
    reconstructed: dict[tuple[Any, ...], Matrix] = {}
    for key, block in geom_out.items():
        cooked = list(key)
        record = cooked[9]
        cooked[5] = 0 ^ record
        cooked[7] = record
        reconstructed[tuple(cooked)] = block
    feedforward_equivalent = reconstructed == main_plus
    reachable_geometry = {key[5] for key, p in outcome_probabilities(main_plus).items() if p > 0}
    ledger.gate(
        "G-C2-FEEDFORWARD-EQUIVALENCE",
        feedforward_equivalent,
        "input bit plus retained record reconstruct every published geometry/collar label and its only later readout",
        mut.moves,
    )

    mean_geometry = sum(Q(key[1]) * p for key, p in branch_probs.items())
    threshold_left = int(mtrace(mmul(PZ, RHO_MIX))[0] >= 0)
    threshold_right = Q(1, 2) * int(mtrace(mmul(PZ, P0))[0] >= 0) + Q(1, 2) * int(mtrace(mmul(PZ, P1))[0] >= 0)
    mean_control_ok = mean_geometry not in {Q(0), Q(1)} and Q(threshold_left) != threshold_right
    ledger.gate(
        "G-C3-BINARY-MEAN-CONTROL",
        mean_control_ok,
        f"in this binary pointer alphabet the mean {qstr(mean_geometry)} is not a label, and the registered threshold rule violates affinity at {threshold_left} versus {qstr(threshold_right)}",
        mut.moves,
    )

    collar_zero = successor(main_ks, P0, ("A", "B"), 0, 0)
    collar_one = successor(main_ks, P0, ("A", "B"), 0, 1)
    if mutant_name == "COLLAR_SMUGGLE":
        changed = dict(collar_one)
        first_key = sorted(changed, key=repr)[0]
        cooked = list(first_key)
        cooked[7] = 1 - int(cooked[7])
        moved_key = tuple(cooked)
        changed[moved_key] = changed.pop(first_key)
        collar_one = mut.change("COLLAR_SMUGGLE", collar_one, changed)
    ledger.gate(
        "G-C4-COLLAR-UNINSTANTIATED",
        collar_zero == collar_one,
        "changing the input collar leaves the delivered successor exactly unchanged; no collar dynamics is instantiated",
        mut.moves,
    )

    # Two actors, spectators, disjoint diamonds, and first loop.
    l2_viable = branch_resolution and tuple(sorted(("A", "B"))) in [key[3] for key in main_plus]
    ledger.gate(
        "G-D1-L2-INSTRUMENT",
        l2_viable,
        "the two-actor projective instrument writes a pair-keyed nominal branch and durable outcome record",
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
    complete_left: dict[tuple[Any, ...], Matrix] = {}
    complete_right: dict[tuple[Any, ...], Matrix] = {}
    for a, c in itertools.product((0, 1), repeat=2):
        ka = mtensor(main_ks[a], I2)
        kc = mtensor(I2, main_ks[c])
        left = apply_k(kc, apply_k(ka, bell))
        right = apply_k(ka, apply_k(kc, bell))
        diamond_equal = diamond_equal and left == right
        diamond_probs[(a, c)] = mtrace(left)[0]
        payload = (
            "relations", (("A", "B"), ("C", "D")),
            "nominal_geometry", (("AB", a), ("CD", c)),
            "nominal_collar", (("AB", a), ("CD", c)),
            "records", (("AB", a), ("CD", c)),
        )
        complete_left[payload] = left
        complete_right[payload] = right
    correlated = diamond_probs[(0, 0)] == Q(1, 2) and diamond_probs[(1, 1)] == Q(1, 2) and diamond_probs[(0, 1)] == 0
    ledger.gate(
        "G-D3-DISJOINT-DIAMOND",
        diamond_equal and complete_left == complete_right and correlated,
        f"both orders agree on quantum blocks and every nominal payload field for all {len(diamond_probs)} disjoint branches",
        mut.moves,
    )

    rank_k2 = graph_cycle_rank({0, 1}, {(0, 1)})
    rank_path3 = graph_cycle_rank({0, 1, 2}, {(0, 1), (1, 2)})
    rank_triangle = graph_cycle_rank({0, 1, 2}, {(0, 1), (1, 2), (0, 2)})
    u01 = matrix([[0, PI], [PI, 0]])
    u12 = matrix([[0, 1], [-1, 0]])
    u20 = I2
    if mutant_name == "LOOP_FAKE":
        u20 = mut.change("LOOP_FAKE", u20, P0)
    qh = mmul(u20, mmul(u12, u01))
    reverse_h = mmul(mdag(u01), mmul(mdag(u12), mdag(u20)))
    g0, g1, g2 = PX, PZ, I2
    u01_g = mmul(g1, mmul(u01, mdag(g0)))
    u12_g = mmul(g2, mmul(u12, mdag(g1)))
    u20_g = mmul(g0, mmul(u20, mdag(g2)))
    qh_g = mmul(u20_g, mmul(u12_g, u01_g))
    loop_invariant = (
        effects_sum([u01]) == I2
        and effects_sum([u12]) == I2
        and effects_sum([u20]) == I2
        and reverse_h == mdag(qh)
        and qh_g == mmul(g0, mmul(qh, mdag(g0)))
        and mtrace(qh_g) == mtrace(qh)
        and determinant(qh_g) == determinant(qh)
        and qh != I2
    )
    first_loop_ok = rank_k2 == 0 and rank_path3 == 0 and rank_triangle == 1 and loop_invariant
    ledger.gate(
        "G-D4-FIRST-LOOP",
        first_loop_ok,
        f"cycle ranks are {rank_k2}, {rank_path3}, {rank_triangle}; a three-edge oriented loop has gauge-invariant trace {gstr(mtrace(qh))} and determinant {gstr(determinant(qh))}",
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

    cq = mblockdiag([local_blocks[0], local_blocks[1]])
    input_purity = purity(HPLUS)
    output_purity = purity(cq)
    dynamic_obstruction = input_purity == 1 and output_purity < 1
    ledger.gate(
        "G-E3-UNCONDITIONED-CHANNEL-NONUNITARY",
        dynamic_obstruction,
        f"pure matter input has purity {qstr(input_purity)} while the unconditioned enlarged classical-quantum output has purity {qstr(output_purity)}; a unitary dilation is possible but not selected",
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
        "G-F1-MODE-LAW-DEPENDENCE",
        species_under,
        f"one four-site carrier admits an identity degeneracy and a shift with {distinct_modes} exact one-dimensional phase modes; neither is a particle census",
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

    # The rival must survive the same honest finite boundary-instrument safety
    # surface, not the rejected geometry/collar interpretation.
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
    rival_safety["branch_record"] = all(key[9] == key[1] for key in rival_successor)
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
    rival_original = successor(rival_ks, HPLUS, ("A", "B"), 1, 0)
    rival_safety["relabel"] = (
        relabel_successors(rival_original, perm)
        == successor(rival_ks, HPLUS, (perm["A"], perm["B"]), 1, 0)
    )
    main_stats = {z: mtrace(v)[0] for z, v in instrument_blocks(main_ks, P0).items()}
    rival_stats = {z: mtrace(v)[0] for z, v in instrument_blocks(rival_ks, P0).items()}
    rival_diff = main_stats != rival_stats
    ledger.gate(
        "G-F3-RIVAL-LAW",
        rival_diff and all(rival_safety.values()),
        f"rival passes {sum(rival_safety.values())} of {len(rival_safety)} boundary-instrument checks and yields record statistics {serial(main_stats)} versus {serial(rival_stats)}",
        mut.moves,
    )

    allowed_consequence_tags = {"FORCED", "CONDITIONAL", "PERMITTED", "REFUSED", "OPEN"}
    consequence_tags = {tag for _, tag, _ in CONSEQUENCES}
    ledger.gate(
        "G-F4-CONSEQUENCE-VOCABULARY",
        consequence_tags <= allowed_consequence_tags,
        f"all {len(CONSEQUENCES)} consequence rows use exactly one of the five registered classification words",
        mut.moves,
    )

    dimensionful_inputs: list[str] = []

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
        "bell_after_division": bell_after,
        "entanglement_breaking": entanglement_breaking,
        "coherent_probability": coherent_probability,
        "divided_probability": divided_probability,
        "mean_geometry": mean_geometry,
        "reachable_geometries": sorted(reachable_geometry),
        "feedforward_equivalent": feedforward_equivalent,
        "diamond_branches": len(diamond_probs),
        "cycle_ranks": {"K2": rank_k2, "path3": rank_path3, "triangle": rank_triangle},
        "triangle_holonomy": qh,
        "triangle_holonomy_trace": mtrace(qh),
        "triangle_holonomy_determinant": determinant(qh),
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
    ("branch-resolved CP boundary instrument", "FORCED", "The exact Z instrument exists and is independently checkable from its Kraus maps."),
    ("joint dynamic-geometry instrument", "REFUSED", "The delivered geometry and collar are reconstructible copied memory and no relation carrier changes."),
    ("two-actor projective occurrence", "FORCED", "A typed pair-supported instrument exists and has an exact idle-spectator extension."),
    ("two-actor gravitational backreaction", "OPEN", "No calibrated source, relation rewrite, constraint, or geometric response is constructed."),
    ("three actors as first simple-graph cycle", "FORCED", "The exact connected simple-graph cycle ranks are 0, 0, and 1."),
    ("three actors as minimum event arity", "REFUSED", "The L2 instrument is a counterexample and no universal arity law is derived."),
    ("fixed-factor preparation blindness", "FORCED", "Blockwise linearity makes all decompositions of one density operator operationally equal."),
    ("growing-geometry no-signalling", "OPEN", "Relational subsystem algebras and their output-sector embeddings are not defined."),
    ("registered decomposition-reading control", "REFUSED", "It violates affinity and produces the registered steering signal."),
    ("every ontic pure-state dynamics", "OPEN", "One bad ensemble functional does not classify the full ontic branch."),
    ("coherent propagation through the displayed division map", "REFUSED", "The unconditioned projective map is entanglement breaking."),
    ("complex whole-history representation", "PERMITTED", "The exact interference witness requires coherent alternatives before a record boundary, but does not select their amplitudes."),
    ("one-step Hamiltonian uniqueness", "REFUSED", "Infinitely many logarithm lifts share the registered transfer once a clock is chosen."),
    ("global Hamiltonian representation", "OPEN", "No canonical one is supplied, while larger-space dilations remain possible."),
    ("particle species", "OPEN", "No selected law, vacuum, statistics, stability criterion, or scattering map exists."),
    ("affine-coset event rule", "OPEN", "The older affine-line grammar is untouched."),
    ("channel affine translation fixed by CP/TP", "REFUSED", "Exact unital and nonunital CPTP channels both exist."),
    ("cosmological integration constant", "OPEN", "No continuum metric constraint or Bianchi system exists here."),
    ("Newton or area scale derived here", "REFUSED", "No dimensionful or weight-nonzero datum is generated."),
    ("dimensionless matter-gravity coupling", "OPEN", "Matter load and geometric response have not been independently typed."),
    ("GR limit", "OPEN", "No geometric action, deformation closure, scale map, or continuum limit is constructed."),
    ("QFT limit", "OPEN", "No local algebra net, vacuum, statistics, excitation sectors, or continuum limit is constructed."),
    ("geometry-induced decoherence", "OPEN", "The measured dephasing is ordinary record-forgetting, not an independent geometry effect."),
    ("metric noise", "OPEN", "No metric or macroscopic coarse-graining is typed."),
    ("higher-curvature correction", "OPEN", "A loop transport exists, but no gravitational curvature action or coefficient is selected."),
    ("modified dispersion", "OPEN", "There is no momentum, energy, continuum clock, or dispersion observable."),
    ("forced QFT/GR deviation", "OPEN", "No comparison observable or exhaustive surviving law family is defined."),
    ("existing ISP walk reconstruction", "OPEN", "The qubit fixture is not a map from the committed walk."),
]


CHOICES = [
    ("pair records as atomic durable facts", "ONTOLOGY-ASSUMED"),
    ("complete outcome as probability sample point", "TYPE-FORCED"),
    ("operational CP-affinity/no-signalling", "ADMISSIBILITY-ASSUMED"),
    ("copied binary geometry alphabet", "REJECTED-AS-GEOMETRY"),
    ("delivered collar representation", "REJECTED-AS-UNUSED"),
    ("Z-projective division instrument", "FREE"),
    ("X-projective rival law", "FREE-CONTROL"),
    ("complex whole-history functional", "MISSING"),
    ("local matter-geometry amplitudes/action", "MISSING"),
    ("genuine division boundaries", "MISSING"),
    ("all-n extension law", "MISSING"),
    ("vacuum", "MISSING"),
    ("clock/logarithm branch", "FREE-IN-REPRESENTATION"),
    ("continuum/coarse-graining map", "MISSING"),
    ("absolute scale", "MISSING-BY-WALL"),
    ("relational geometry and metric readout", "MISSING"),
]


def primary_verdict() -> str:
    return "BOUNDARY-INSTRUMENT-CONSISTENT-BUT-FUNDAMENTAL-DYNAMICS-UNSELECTED"


def secondary_verdicts() -> list[str]:
    return [
        "DYNAMIC-GEOMETRY-NOT-INSTANTIATED",
        "FEEDFORWARD-EQUIVALENT",
        "CORE-DIVISION-MAP-ENTANGLEMENT-BREAKING",
        "L2-INSTRUMENT-VIABLE",
        "TRIANGLE-FIRST-CYCLE-NOT-FIRST-EVENT",
        "FIXED-FACTOR-PREPARATION-BLIND",
        "HAMILTONIAN-ONE-STEP-NONUNIQUE",
        "SPECIES-UNSELECTED",
        "AFFINE-CHANNEL-TERM-UNSELECTED",
        "QFT-GR-DEVIATIONS-OPEN-UNTYPED",
        "COMPLEX-RELATIONAL-HISTORY-LAW-CANDIDATE-UNPROVED",
    ]


def claims_for(measurements: dict[str, Any]) -> dict[str, str]:
    return {
        "PRIMARY": primary_verdict(),
        "EXISTENCE": (
            "A fixed-factor boundary instrument passes exact CP, trace, affinity, HJW and no-signalling checks "
            f"across {measurements['cp_branch_maps']} branch maps, but its geometry labels are feed-forward equivalent."
        ),
        "ARITY": (
            "A two-actor projective instrument is viable; cycle ranks "
            f"{measurements['cycle_ranks']['K2']}, {measurements['cycle_ranks']['path3']}, "
            f"{measurements['cycle_ranks']['triangle']} make three actors the first simple-graph cycle, not the first event."
        ),
        "HAMILTONIAN": (
            f"The frozen transfer has {len(measurements['hamiltonian_lifts'])} tested generator lifts with one image, "
            f"while the unconditioned boundary output changes purity from {qstr(measurements['input_purity'])} "
            f"to {qstr(measurements['cq_output_purity'])}."
        ),
        "SELECTION": (
            f"The same uncalibrated carrier and output grammar admit main statistics {serial(measurements['main_stats_on_zero'])} "
            f"and rival statistics {serial(measurements['rival_stats_on_zero'])}; the weak safety surface does not select a law."
        ),
        "DEVIATION": "No QFT or GR comparison observable is typed in this unit; deviations remain open rather than absent.",
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
    return f"""# The law one level above the Hamiltonian

## Complete relational histories, division boundaries, and the dynamics still missing

**Status:** final finite result plus a serious unproved candidate for the
fundamental law.

### Abstract

The proposed ontology is one actual relational history: relations, durable
records, effective causal/transport geometry, and physical contents change
together.  A wave function, density matrix, action, field, transfer matrix, or
Hamiltonian is a representation of the law over possible histories, not an
additional substance merely because it appears in the equations.

An exact finite test identifies where that proposal must live.  A
branch-resolved projective instrument is completely positive, trace preserving,
affine, preparation-independent, and non-signalling in a fixed one-region Bell
test.  But the labels originally attached to it as geometry and collar are
exactly reconstructible from an ordinary retained outcome bit.  No relation
carrier changes and the input collar is ignored.  The model is therefore
prediction-equivalent to a projective measurement followed by classical
feed-forward; it is not a model of back-reacting spacetime.

The same test reveals why a boundary instrument cannot be the microscopic law.
Its unconditioned map is entanglement breaking.  A separate exact rational
two-path example gives coherent probability
`{qstr(measurements['coherent_probability'])}` before an intermediate record
and `{qstr(measurements['divided_probability'])}` after one is inserted.  If
the projective map were applied at every relational rewrite, it would erase the
interference the theory is meant to explain.

The refined bet is consequently a strongly positive complex decoherence
functional over complete finite relational histories of matter and geometry.
Coherent alternatives are summed between genuine division boundaries.  A CP
instrument and one actual durable successor emerge only at a partition where
the functional decoheres.  Geometry back-reacts history by history because
each alternative contains its own relation and transport data; no expectation
value is fed nonlinearly into a classical metric.  This proposal has genuine
dynamical form, but its local complex weights, division criterion, refinement
fixed point, vacuum, scales, and continuum phase remain unselected.  The exact
primary verdict is `{primary_verdict()}`.

### The idea without technical language

Imagine that reality is an expanding transaction history, not objects moving
on a stage that exists independently of them.  A transaction may change who
can affect whom, what durable fact exists, and how later signals can travel.
Those are different readings of one physical occurrence.

There is an important quantum qualification.  Before a durable receipt exists,
several possible internal routes can combine and cancel or reinforce one
another.  Treating every internal route as an already completed transaction
destroys that effect.  The law must therefore speak about a whole stretch of
possible relational history at once.  Only when the alternatives have left
distinguishable, stable records may the law assign ordinary probabilities to
them and select one actual continuation.

This gives the Hamiltonian its classical philosophical status back.  It can be
an extremely useful compressed description of repeated evolution in a sector
where the geometry and clock have been held fixed.  It is not automatically
what exists.  What exists is the relational history; what is fundamental law
is the rule assigning coherent weights and eventual record probabilities to
such histories.

### Ontology, law, and representation

The proposal separates three levels.

**Ontology.**  Exactly one realized relational history exists.  Its elementary
durable facts are relations and records.  Effective geometry is not an extra
bit named `geometry`; it must be a rule-governed property of the realized
relation and transport structure that controls later reachability,
composition, or measured interval data.  A boundary collar is geometric only
if it carries typed continuation data constrained by that structure.

**Law.**  The law concerns the complete possible histories between genuine
division boundaries.  It need not factor into a sequence of physically real
micro-updates.  Mutually exclusive complete recorded successors are the sample
points of ordinary probability.  Several cells or relations written inside
one successor are simultaneous consequences, not competing outcomes.

**Representation.**  Hilbert spaces, class operators, amplitudes, density
operators, instruments, process tensors, actions, and Hamiltonians may encode
the law.  Their gauge-dependent parts are not promoted to ontology.  A
representation earns physical meaning by mapping its invariant content to
history probabilities, durable records, and relational observables.

One actual history does not imply a classical probability distribution over
every microscopic route.  Counterfactual histories may interfere in the law
that assigns the chance of the one realized recorded history, just as paths in
a path integral need not be individually actual.

The Barandes-inspired move here is the inversion of ontology and
representation: the process law and actual events are primary, while the
wave-function description is not automatically substance.  The present
candidate does not place that process on a fixed realized stage.  The
mathematical catalogue of possible relational histories may be fixed, but the
causal and transport structure of the realized history is itself part of the
outcome.  Each alternative carries its own geometry rather than evolving on
one externally supplied spacetime.

### Exact finite results

#### A safe boundary instrument

For projectors `P_z`, define the outcome maps

`J_z(rho) = P_z rho P_z`.

The exact battery checks {cp_maps} branch maps by {cp_minors} Choi
principal-minor certificates and exact Kraus completeness.  Its transcript has
{gate_count} passing gates and authenticates {source_count} frozen source
files.  The complete direct-sum output is linear in `rho`.  Therefore every
ensemble decomposition of one density operator gives the same output under
the fixed instrument, not only the displayed Z and X ensembles.

For a Bell pair, Alice's Z and X steering choices prepare different ensembles
of Bob's same reduced state.  Bob's unconditioned complete blocks remain equal
under the registered fixed-factor instrument.  The deliberately
decomposition-reading statistic instead changes from
`{qstr(measurements['nonlinear_control_z'])}` to
`{qstr(measurements['nonlinear_control_x'])}` and is non-affine.  This proves a
fixed-factor safety result.  It does not prove no-signalling when the outcome
changes which relational algebra counts as Bob's subsystem.

#### The geometry eliminability theorem

In every delivered branch the nominal outputs obey

`G' = g xor record` and `C' = record`.

The only later probe returns the reconstructed label, and changing the input
collar changes no successor.  Erasing `G'` and `C'` while retaining the input
bit and outcome record leaves every declared prediction recoverable exactly.
Thus the finite model is equivalent to ordinary measurement plus classical
feed-forward.  Its purity loss is ordinary loss from ignoring a record, not
evidence that gravity caused decoherence.

This is a constructive refusal, not a no-go against relational gravity.  A
valid successor must perform an actual relation or transport rewrite and use a
fixed geometric rule to change later availability or propagation.  Renaming a
controller bit is insufficient.

#### Division events cannot occur at every rewrite

On one half of a Bell pair, the unconditioned Z instrument produces exactly

`(1/2)|00><00| + (1/2)|11><11|`,

a separable state of purity `{qstr(measurements['cq_output_purity'])}`.  The
map is entanglement breaking.

The independent rational interference fixture uses the exact orthogonal
rotation

```text
R = [[3/5, 4/5], [-4/5, 3/5]].
```

For return to the first output after two rotations, the two intermediate path
amplitudes are `9/25` and `-16/25`.  Summing them before squaring gives
`{qstr(measurements['coherent_probability'])}`.  Inserting an intermediate
record makes the path probabilities add and gives
`{qstr(measurements['divided_probability'])}`.  The difference is exact.

Therefore the projective instrument is a possible shadow at a genuine record
boundary, not a universal microscopic successor.  A fundamental law must keep
coherent histories available between such boundaries.

#### Arity and loops

A pair-supported projective instrument exists and survives an idle spectator.
This establishes typed two-actor viability only; it does not establish
gravitational backreaction.  A higher-support parity instrument also exists,
so pair-record ontology does not imply pair-factorized dynamics.

The cycle ranks of a two-actor edge, a three-actor path, and a triangle are
respectively `{measurements['cycle_ranks']['K2']}`,
`{measurements['cycle_ranks']['path3']}`, and
`{measurements['cycle_ranks']['triangle']}`.  The repaired loop uses three
oriented edge transports, reverse edges as inverses, and a vertex-frame gauge
transformation.  Its trace `{gstr(measurements['triangle_holonomy_trace'])}`
and determinant `{gstr(measurements['triangle_holonomy_determinant'])}` are
unchanged.  This licenses a finite transport-loop statement, not Regge or
spacetime curvature.

Three actors are therefore the first cycle context in this simple-graph
family.  They are not the minimum interaction arity.  A regional law may
contain pair, triple, and arbitrary finite support in parallel, just as a field
theory packages simultaneous local degrees of freedom rather than enforcing
one universal collision size.

#### Underdetermination

The Z- and X-resolving instruments obey the same uncalibrated carrier and
output grammar and pass the same fixed boundary-instrument safety surface.
On the same input they predict record distributions
`{serial(measurements['main_stats_on_zero'])}` and
`{serial(measurements['rival_stats_on_zero'])}`.  Hence CP, normalization,
affinity, fixed-factor no-signalling, relabelling, idle-spectator extension,
and disjoint composition do not select the instrument.

This does not prove nonselection after an independently calibrated flux,
branchwise conservation, overlapping refinement, or continuum deformation
closure is imposed.  Z and X are different observables until such a common
calibration exists.  The exact result is nonselection by the present weak
surface.

### The refined dynamical candidate

Let `Hist(B_-,B_+)` be the finite complete relational histories between two
boundary records.  A history `h` contains at least:

- its changing relation and causal/transport structure `R_h`;
- boundary continuation data `C_h`;
- matter or process configurations `q_h`;
- every durable record actually formed; and
- typed maps identifying the same boundary fact across refinements.

For a coarse history question `A`, define a class operator by coherent
summation,

`K_A = sum_(h in A) a[h] V[h]`,

where `V[h]` transports the process state along the geometry of that same
history and `a[h]` is its complex scalar weight.  Define

`D(A,B) = Tr(K_A rho_boundary K_B^dagger)`.

The candidate law is the compatible family of these functionals, not one
instantaneous wave function.  It must be Hermitian, normalized, additive under
coarse graining, and strongly positive.  It must also satisfy:

1. **regional gluing:** shared unrecorded boundaries are summed/contracted and
   disjoint regions compose;
2. **refinement consistency:** two descriptions of one region push forward to
   the same boundary functional;
3. **relational locality:** a remote pre-contact intervention cannot alter a
   local unconditioned boundary law;
4. **branchwise constraints:** invalid relation, flux, gauge, or geometric
   histories have zero amplitude, and valid histories satisfy the discrete
   conservation/closure law on every branch;
5. **record permanence:** a durable record defines a stable orthogonal sector
   under every licensed future continuation; and
6. **nontrivial coherence:** at least one unrecorded refinement retains an
   off-diagonal term, so the theory is not a classical stochastic growth law
   in disguise.

A partition `{{A_alpha}}` is a genuine division boundary only when

`D(A_alpha,A_beta) = 0` for distinct recorded alternatives.

Then, and only then, ordinary probabilities are licensed:

`p(alpha) = D(A_alpha,A_alpha)`.

Conditioned on the actual recorded past `H`, the next complete recorded
successor has

`p(alpha | H) = D(H alpha,H alpha) / D(H,H)`

when the denominator is nonzero and the successor partition decoheres.  One
`alpha` becomes actual by an objective stochastic postulate.  The normalized
conditional state on that branch may be nonlinear because of conditioning;
the unconditioned complete law remains preparation-independent.

The finite result uses exact zero off-diagonal terms.  A macroscopic theory
would need a quantitative and refinement-stable error theorem for approximate
decoherence before an approximate division could count as physical; no
threshold is declared here.

#### A concrete local-weight ansatz

The least empty dynamical ansatz is

`a[h] = product_v exp(-I_v[h]/2 + i Theta_v[h])`,

with the product over local relational vertices/regions.  `I_v` is an
information or record-distinguishability cost and `Theta_v` is an oriented
phase/transport functional.  They are evaluated on the same local
matter-geometry history, so backreaction is not appended afterward.  They must
remain distinct: a positive probability shadow does not determine the phase
data responsible for interference.

This ansatz is concrete but not selected.  Its serious selector is a
universality problem rather than a slogan:

`R_coarse(D_*) = D_*`,

where `R_coarse` sums fine relational histories to a coarse boundary
functional.  The fixed point must simultaneously satisfy overlap gluing,
changing-factorization no-signalling, branchwise conservation, nontrivial
coherence, and a continuum deformation/refoliation closure.  A family of fixed
points or relevant directions is expected; boundary conditions and measured
couplings may remain physical data.  If only a trivial/topological or
entanglement-breaking fixed point survives, the proposal fails.

### How gravity would have to emerge

Geometry must do work through the relation/transport structure, not through a
label.  At minimum a local history must change `R` to `R'`; a predeclared graph
or transport rule must then change a later interaction's availability or
amplitude.  Matter flux must be defined independently of the outcome name, and
each history must satisfy a boundary balance law.  Neighboring loop transports
must obey a discrete closure/Bianchi relation, and two unphysical cuts of one
overlapping region must induce the same boundary functional.

The candidate differs from expectation-sourced semiclassical gravity.  It
does not calculate an average stress tensor and feed that average back into one
classical branch.  Matter and geometry are varied/summed jointly as parts of
each complete history.  The actual geometry is the geometry of the selected
recorded history.

There are then two empirical forks.

- If distinct geometry histories remain coherent until a genuine record forms,
  gravity need not cause universal microscopic decoherence.
- If geometry is classical and distinguishing at every microscopic step, it
  continually records the matter alternatives.  Decoherence and stochastic
  geometric noise then become unavoidable conditional consequences, with a
  quantitative tradeoff fixed only after the coupling and division rate are
  selected.

The present finite model realizes neither gravitational branch; it realizes
ordinary detector feed-forward.

### EPR and locality

The density-operator-complete boundary instrument removes the registered
decomposition-sensitive signalling mechanism at fixed factorization.  It is a
consistent replacement, not a derivation from an earlier nonlinear rule.

For growing geometry, no-signalling must be stated on relational local
algebras.  Summing over every outcome of a remote pre-contact intervention must
leave Bob's boundary functional invariant after the correct sector embedding,
even if Alice's outcome creates or deletes relations elsewhere.  This is a
constraint on the complete history functional and its gluing maps.  A partial
trace on one frozen tensor product is not enough.

An ontic pure-state variable is not ruled out in general.  It is viable only if
its complete composite law is preparation-independent wherever remote steering
is operationally phrasable, or if the extra structure cannot be remotely
selected.  The registered decomposition-reading functional fails this test.

### Hamiltonian reconstruction

In the frozen two-level fixture, one boundary transfer is `diag(1,i)`.  The
receipt displays {lift_count} exact witnesses, while the full integer family is
`(4m,1+4n)`.  After choosing a duration `Delta t`, units, and sign convention,
the energy branches differ by integer multiples of `2 pi hbar / Delta t`.
One discrete transfer therefore does not select a Hamiltonian.

A Hamiltonian can emerge when a selected phase contains:

- a stable background or relational clock;
- repeated thin boundaries on one identifiable state space;
- continuity or a semigroup/group law;
- locality and spectral conditions; and
- a chosen logarithm branch and units.

Then `H` is the generator of that effective transfer representation.  On a
changing carrier the more natural objects may be class operators, regional
amplitudes, combs, or process tensors.  A larger fixed-space unitary dilation
can always repackage many channels, but its environment, clock, and embedding
are additional representation choices.  None becomes ontology by notation.

### Particles, species, and interactions

A finite transfer matrix's eigenvectors are not particles.  In the serious
candidate, species would be sought only after a nontrivial refinement fixed
point and vacuum are selected.  Stable irreducible perturbations or localized
superselection sectors around that phase are species candidates.  Exchange
statistics require a permutation or braid action and the appropriate local
observable algebra; pair records alone neither force nor forbid bosons and
fermions.

Interactions are the multilinear/fusion terms among those stable sectors, or
equivalently the local vertices in the coarse history functional.  Pair,
triple, and higher effective vertices can coexist.  The number three has no
universal particle or interaction status merely because a triangle is the
first loop.

The exact identity-versus-shift example proves only that different unspecified
transfer laws on one finite carrier have different spectral partitions.  It
therefore establishes that the current ontology does not select a particle
list; it does not show that species can never be derived from a selected law.

### Constants, scales, and possible deviations

Three uses of “affine” or “constant” remain separate.

- The old affine-coset event grammar is untouched.
- Complete positivity and trace preservation do not select a channel's affine
  Bloch translation; exact unital and reset channels give zero and nonzero
  translations.
- A cosmological constant is not typed until an effective metric constraint
  system exists.  At a continuum fixed point it could be a relevant coupling
  or boundary/integration datum; the current law does not choose its value.

Dimensionless record data cannot create an absolute meter, second, mass, or
Newton constant without a scale-bearing input or dimensional transmutation
with a calibrated observable.  The proposal might derive ratios or critical
exponents before it derives a unit.

The consequence ledger is therefore deliberately conservative:

| topic | classification | reason |
|---|---|---|
{consequence_rows}

No QFT/GR deviation is presently typed, which is different from proving that
there is none.  Conditional possibilities include geometry-correlated
decoherence/noise in the always-classical branch, higher-derivative or nonlocal
operators away from a continuum fixed point, and multi-time memory not visible
in one-time channels.  Lorentz violation is not forced by discreteness.  No
coefficient, scale, or even presence of these effects is selected here.

### Choice inventory

| item | status |
|---|---|
{choice_rows}

The architecture has named the correct level of the missing object but has not
chosen its content.  In particular, writing an action for arbitrary weights is
not selection; any sufficiently regular law can be rewritten in action form.

### Candidate verdicts

Primary:

`{primary_verdict()}`

Secondary:

{secondaries}

Machine-equal claim block:

```text
{claim_block}
```

### Smallest decisive next test

The next exact arena should use three actors with overlapping supports `AB`
and `BC`, plus one external probe actor.  It must include:

1. two refinements/cuts of the same regional history;
2. an actual relation or transport rewrite, not a copied label;
3. a downstream interaction whose availability is computed from the output
   relation structure;
4. equality of the complete boundary decoherence functional under both cuts;
5. closure of overlapping deformations into independently defined boundary
   transport;
6. branchwise flux conservation and a geometry-validity constraint;
7. a fixed-factor and changing-factorization no-signalling census; and
8. an interference witness that an entanglement-breaking placeholder cannot
   pass.

A neighboring-loop four-actor closure test should follow.  Only after these
survive is it meaningful to search for an all-arity law, a vacuum, species, or
continuum deviations.

### Falsifiers of the refined bet

The proposal fails, rather than merely remaining incomplete, if any of the
following is proved at the intended scope:

- no strongly positive compatible functional exists when relations and local
  subsystem types change;
- overlap/refinement equality forces every allowed functional to be classical,
  topological, or entanglement breaking;
- no intrinsic record criterion separates coherent internal alternatives from
  actual division boundaries;
- branchwise conservation and changing geometry are incompatible with
  compositional no-signalling; or
- every nontrivial fixed point misses both the QFT benchmarks and a Lorentzian
  gravitational continuum.

Conversely, consistency alone is not confirmation.  The candidate becomes
physical only when a selected fixed point predicts a held-out dimensionless
observable or a controlled QFT/GR limit.

### Primary literature anchors

- J. A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
  arXiv:2507.21192.
- R. B. Griffiths, *Consistent Histories and the Interpretation of Quantum
  Mechanics*, J. Stat. Phys. 36 (1984) 219–272; M. Gell-Mann and J. B. Hartle,
  *Classical Equations for Quantum Systems*, Phys. Rev. D 47 (1993) 3345–3382.
- R. D. Sorkin, *Quantum Mechanics as Quantum Measure Theory*, Mod. Phys. Lett.
  A 9 (1994) 3119–3127, arXiv:gr-qc/9401003.
- R. Oeckl, *General Boundary Quantum Field Theory: Foundations and
  Probability Interpretation*, Adv. Theor. Math. Phys. 12 (2008) 319–352,
  arXiv:hep-th/0509122.
- E. Hawkins, F. Markopoulou, and H. Sahlmann, *Evolution in Quantum Causal
  Histories*, Class. Quantum Grav. 20 (2003) 3839–3854,
  arXiv:hep-th/0302111.
- L. P. Hughston, R. Jozsa, and W. K. Wootters, *A Complete Classification of
  Quantum Ensembles Having a Given Density Matrix*, Phys. Lett. A 183 (1993)
  14–18, doi:10.1016/0375-9601(93)90880-9.
- C. Simon, V. Buzek, and N. Gisin, *No-Signaling Condition and Quantum
  Dynamics*, Phys. Rev. Lett. 87 (2001) 170405,
  arXiv:quant-ph/0102125.
- M. Horodecki, P. W. Shor, and M. B. Ruskai, *Entanglement Breaking
  Channels*, Rev. Math. Phys. 15 (2003) 629–641,
  arXiv:quant-ph/0302031.
- G. Chiribella, G. M. D'Ariano, and P. Perinotti, *Theoretical Framework for
  Quantum Networks*, Phys. Rev. A 80 (2009) 022339, arXiv:0904.4483.
- F. M. Pollock et al., *Non-Markovian Quantum Processes: Complete Framework
  and Efficient Characterization*, Phys. Rev. A 97 (2018) 012127,
  arXiv:1512.00589.
- D. P. Rideout and R. D. Sorkin, *A Classical Sequential Growth Dynamics for
  Causal Sets*, Phys. Rev. D 61 (2000) 024002, arXiv:gr-qc/9904062.
- T. Regge, *General Relativity Without Coordinates*, Nuovo Cimento 19 (1961)
  558–571, doi:10.1007/BF02733251.
- D. M. T. Benincasa and F. Dowker, *The Scalar Curvature of a Causal Set*,
  Phys. Rev. Lett. 104 (2010) 181301, arXiv:1001.2725.
- S. A. Hojman, K. Kuchar, and C. Teitelboim, *Geometrodynamics Regained*,
  Ann. Phys. 96 (1976) 88–135, doi:10.1016/0003-4916(76)90112-3.
- D. Lovelock, *The Einstein Tensor and Its Generalizations*, J. Math. Phys.
  12 (1971) 498–501, doi:10.1063/1.1665613.
- J. Oppenheim, *A Postquantum Theory of Classical Gravity?*, Phys. Rev. X 13
  (2023) 041040, arXiv:1811.03116; A. Tilloy and L. Diosi, *Sourcing
  Semiclassical Gravity from Spontaneously Localized Quantum Matter*, Phys.
  Rev. D 93 (2016) 024026, arXiv:1509.08705.
- R. Haag and D. Kastler, *An Algebraic Approach to Quantum Field Theory*, J.
  Math. Phys. 5 (1964) 848–861; S. Doplicher, R. Haag, and J. E. Roberts,
  *Fields, Observables and Gauge Transformations I*, Commun. Math. Phys. 13
  (1969) 1–23.

### Exact artifact statement

Every finite numerical and matrix claim in this paper is regenerated from
`v16/code/jrh_exact.py` into the paired transcript and JSON receipt using exact
rational or Gaussian-rational arithmetic.  The dynamical functional and its
continuum fixed point are explicitly conjectural and have no generated
coefficient.  This paper proves a boundary-instrument result, an eliminability
no-go, an entanglement-breaking consequence, an interference placement
constraint, and weak-surface nonselection.  It does not prove quantum gravity.
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
        "status": "REPAIRED-PENDING-DELTA-VERIFICATION",
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
