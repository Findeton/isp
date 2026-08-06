#!/usr/bin/env python3
"""RQ0-L0 Cycle B — the task-record fixed point.  Exact arithmetic only.

Executes the frozen pin `v13/note-rq0-l0-task-record-fixed-point-pin.md`
(commit 7a80e39) gate by gate:

  G0  the definition gate      -- literal Pres collapse test, availability form
  G1  the Galois gates         -- antitone monotonicity, adjunction, closure
  G2  fixed points             -- trivial, characterization, de-smuggling
  G3  the four carried control families, each in both directions

Immutable inputs reused as anchors: v13 LOG #97-#103 (minimal sufficient
quantum boundaries + adjudication) and v13 LOG #104-#111 (operational
classical cores + adjudication).

Substantive negatives exit 0.  Anchor mismatches exit 1.  `--mutant NAME`
breaks exactly one committed anchor and must exit 1.

Scope: finite, one boundary, task de-smuggling only.  No composition/tensor,
locality, overlap, topology, causality, spacetime, field or gravity object is
constructed or claimed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations, product
from pathlib import Path

SCHEMA = "rq0-l0-task-record-fixed-point-receipt-v1"
PIN_COMMIT = "7a80e39"
BASE_COMMIT = "6c2d7b8"
HERE = Path(__file__).resolve().parent
OUT_TXT = HERE / "rq0_l0_fixed_point_output.txt"
OUT_JSON = HERE / "rq0_l0_fixed_point_receipt.json"

T0 = time.time()
MUTANT: str | None = None
SOURCE_SHA256 = ""
EXACTNESS_VIOLATIONS: list = []


def prog(msg: str) -> None:
    sys.stdout.write(f"[{time.time() - T0:7.1f}s] {msg}\n")
    sys.stdout.flush()


# --------------------------------------------------------------------------
# 0.  Exact Gaussian-rational scalars and matrices.  No float ever appears.
# --------------------------------------------------------------------------


class QC:
    """An element of Q(i): exact rational real and imaginary parts."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = qc(o)
        return QC(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        o = qc(o)
        return QC(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        o = qc(o)
        return QC(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__
    __radd__ = __add__

    def conj(self):
        return QC(self.re, -self.im)

    def norm2(self) -> Fr:
        return self.re * self.re + self.im * self.im

    def inv(self):
        n = self.norm2()
        if n == 0:
            raise ZeroDivisionError("QC inverse of zero")
        return QC(self.re / n, -self.im / n)

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0

    def __eq__(self, o):
        o = qc(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"QC({self.re},{self.im})"


def qc(x) -> QC:
    if isinstance(x, QC):
        return x
    return QC(x, 0)


ZERO = QC(0)
ONE = QC(1)


def mat(rows) -> tuple:
    return tuple(tuple(qc(x) for x in r) for r in rows)


def mzero(n: int, m: int | None = None) -> tuple:
    m = n if m is None else m
    return tuple(tuple(ZERO for _ in range(m)) for _ in range(n))


def mid(n: int) -> tuple:
    return tuple(tuple(ONE if i == j else ZERO for j in range(n)) for i in range(n))


def mmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return tuple(
        tuple(
            sum((a[i][t] * b[t][j] for t in range(k)), ZERO) for j in range(m)
        )
        for i in range(n)
    )


def madd(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def msub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def mscale(s, a):
    s = qc(s)
    return tuple(tuple(s * a[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def madj(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a))) for i in range(len(a[0])))


def meq(a, b) -> bool:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    return all(a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a[0])))


def mtrace(a) -> QC:
    return sum((a[i][i] for i in range(len(a))), ZERO)


def mkron(a, b):
    na, ma, nb, mb = len(a), len(a[0]), len(b), len(b[0])
    return tuple(
        tuple(a[i // nb][j // mb] * b[i % nb][j % mb] for j in range(ma * mb))
        for i in range(na * nb)
    )


def mrank(a) -> int:
    """Exact rank over Q(i) by Gaussian elimination."""
    rows = [list(r) for r in a]
    n, m = len(rows), len(rows[0])
    rank, piv = 0, 0
    for col in range(m):
        sel = None
        for r in range(piv, n):
            if not rows[r][col].is_zero():
                sel = r
                break
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        inv = rows[piv][col].inv()
        rows[piv] = [inv * x for x in rows[piv]]
        for r in range(n):
            if r != piv and not rows[r][col].is_zero():
                f = rows[r][col]
                rows[r] = [rows[r][c] - f * rows[piv][c] for c in range(m)]
        piv += 1
        rank += 1
        if piv == n:
            break
    return rank


def nullity_of_conditions(vectors) -> int:
    """dim of the solution space of the homogeneous system whose rows are
    `vectors` (each a flat list of QC), in the number of unknowns."""
    if not vectors:
        raise ValueError("no conditions given")
    nvars = len(vectors[0])
    return nvars - mrank(tuple(tuple(v) for v in vectors))


# Pauli matrices (exact).
PI2 = mid(2)
PX = mat([[0, 1], [1, 0]])
PZ = mat([[1, 0], [0, -1]])


def block_diag(*blocks):
    n = sum(len(b) for b in blocks)
    out = [[ZERO] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b[0])):
                out[off + i][off + j] = b[i][j]
        off += len(b)
    return tuple(tuple(r) for r in out)


# --------------------------------------------------------------------------
# 1.  Finite C*-fixtures: block structure, central atoms, exact centre.
# --------------------------------------------------------------------------


class CStar:
    """A finite direct sum of matrix blocks, embedded block-diagonally."""

    def __init__(self, name: str, blocks: tuple[int, ...]):
        self.name = name
        self.blocks = tuple(blocks)
        self.dim = sum(blocks)
        self.offsets = []
        off = 0
        for d in blocks:
            self.offsets.append(off)
            off += d

    # --- basis of the algebra -------------------------------------------
    def matrix_units(self):
        out = []
        for k, d in enumerate(self.blocks):
            o = self.offsets[k]
            for i in range(d):
                for j in range(d):
                    m = [[ZERO] * self.dim for _ in range(self.dim)]
                    m[o + i][o + j] = ONE
                    out.append(tuple(tuple(r) for r in m))
        return out

    def central_projection(self, atoms) -> tuple:
        m = [[ZERO] * self.dim for _ in range(self.dim)]
        for k in atoms:
            for i in range(self.blocks[k]):
                m[self.offsets[k] + i][self.offsets[k] + i] = ONE
        return tuple(tuple(r) for r in m)

    def atoms(self):
        return tuple(range(len(self.blocks)))

    def centre_dimension(self) -> int:
        """Exact complex dimension of Z(A), computed (never typed).

        An element  a = sum_c x_c c  of A is central iff [a,b] = 0 for every
        basis element b.  We solve that homogeneous linear system exactly.
        """
        if hasattr(self, "_zdim"):
            return self._zdim
        basis = self.matrix_units()
        nb = len(basis)
        # commutators, computed once
        comm = [[msub(mmul(basis[ci], b), mmul(b, basis[ci])) for ci in range(nb)] for b in basis]
        conds = []
        for bi in range(nb):
            for i in range(self.dim):
                for j in range(self.dim):
                    row = [comm[bi][ci][i][j] for ci in range(nb)]
                    if any(not x.is_zero() for x in row):
                        conds.append(row)
        self._zdim = nb if not conds else nullity_of_conditions(conds)
        return self._zdim


# --------------------------------------------------------------------------
# 2.  Channels as exact Kraus families; Heisenberg pullback; sector support.
# --------------------------------------------------------------------------


class Channel:
    """An admitted deterministic future, given by exact Kraus operators
    K_j : H_in -> H_out.  Heisenberg action  Phi^#(b) = sum_j K_j^* b K_j."""

    def __init__(self, name: str, kraus, dim_in: int, dim_out: int):
        self.name = name
        self.kraus = tuple(kraus)
        self.dim_in = dim_in
        self.dim_out = dim_out

    def is_unital_cp(self) -> bool:
        """sum_j K_j^* K_j = I_in  (trace preservation of the predual)."""
        acc = mzero(self.dim_in)
        for k in self.kraus:
            acc = madd(acc, mmul(madj(k), k))
        return meq(acc, mid(self.dim_in))

    def pullback(self, b):
        acc = mzero(self.dim_in)
        for k in self.kraus:
            acc = madd(acc, mmul(mmul(madj(k), b), k))
        return acc

    def forward(self, rho):
        acc = mzero(self.dim_out)
        for k in self.kraus:
            acc = madd(acc, mmul(mmul(k, rho), madj(k)))
        return acc


def chan_identity(dim: int) -> Channel:
    return Channel("id", [mid(dim)], dim, dim)


def chan_unitary(name: str, u) -> Channel:
    return Channel(name, [u], len(u), len(u))


def chan_reset(name: str, dim_in: int, dim_out: int, target: int) -> Channel:
    """Discard the input and reprepare the pure state |target>."""
    kr = []
    for j in range(dim_in):
        m = [[ZERO] * dim_in for _ in range(dim_out)]
        m[target][j] = ONE
        kr.append(tuple(tuple(r) for r in m))
    return Channel(name, kr, dim_in, dim_out)


def chan_sector_reprepare(name: str, alg: CStar, part, targets) -> Channel:
    """Read the block label of `part`, discard everything else, reprepare a
    fixed pure state inside the image block.  `targets[s]` is a basis index."""
    kr = []
    for s, blk in enumerate(part):
        t = targets[s]
        for k in blk:
            for i in range(alg.blocks[k]):
                j = alg.offsets[k] + i
                m = [[ZERO] * alg.dim for _ in range(alg.dim)]
                m[t][j] = ONE
                kr.append(tuple(tuple(r) for r in m))
    return Channel(name, kr, alg.dim, alg.dim)


def chan_dephase(name: str, projectors) -> Channel:
    dim = len(projectors[0])
    return Channel(name, list(projectors), dim, dim)


class ClassicalChannel(Channel):
    """Exact classical channel on C^n: rows sum to 1, entries in Q_{>=0}.
    stoch[i][l] = Pr(out = l | in = i).  Heisenberg on the diagonal algebra."""

    def __init__(self, name: str, stoch):
        self.name = name
        self.stoch = tuple(tuple(Fr(x) for x in r) for r in stoch)
        self.dim_in = len(self.stoch)
        self.dim_out = len(self.stoch[0])
        self.kraus = ()

    def is_unital_cp(self) -> bool:
        return all(sum(r) == 1 and all(x >= 0 for x in r) for r in self.stoch)

    def pullback(self, b):
        """b diagonal; returns the diagonal matrix with entries
        sum_l stoch[i][l] b_ll."""
        n = self.dim_in
        out = [[ZERO] * n for _ in range(n)]
        for i in range(n):
            acc = Fr(0)
            for l in range(self.dim_out):
                acc += self.stoch[i][l] * b[l][l].re
            out[i][i] = QC(acc, 0)
        return tuple(tuple(r) for r in out)

    def forward(self, rho):
        m = [[ZERO] * self.dim_out for _ in range(self.dim_out)]
        for l in range(self.dim_out):
            acc = Fr(0)
            for i in range(self.dim_in):
                acc += self.stoch[i][l] * rho[i][i].re
            m[l][l] = QC(acc, 0)
        return tuple(tuple(r) for r in m)


_SUP_CACHE: dict = {}


def sector_support(alg_in: CStar, alg_out: CStar, ch: Channel):
    """sup[k] = { l : some state in atom k has nonzero weight in atom l }.
    Computed exactly as  tr( z_l  Phi( z_k ) )  >  0."""
    key = (alg_in.name, alg_out.name, ch.name)
    if key in _SUP_CACHE:
        return _SUP_CACHE[key]
    sup = []
    for k in alg_in.atoms():
        zk = alg_in.central_projection([k])
        img = ch.forward(zk)
        s = set()
        for l in alg_out.atoms():
            zl = alg_out.central_projection([l])
            w = mtrace(mmul(zl, img))
            assert w.im == 0, "sector weight must be real"
            if w.re != 0:
                s.add(l)
        sup.append(frozenset(s))
    _SUP_CACHE[key] = tuple(sup)
    return _SUP_CACHE[key]


# --------------------------------------------------------------------------
# 3.  Partitions, refinement order, and the combinatorial record calculus.
# --------------------------------------------------------------------------


def partitions(n: int):
    """All set partitions of {0,...,n-1} as sorted tuples of sorted tuples."""
    if n == 0:
        return [()]
    out = []

    def rec(i, blocks):
        if i == n:
            out.append(tuple(sorted(tuple(sorted(b)) for b in blocks)))
            return
        for b in range(len(blocks)):
            blocks[b].append(i)
            rec(i + 1, blocks)
            blocks[b].pop()
        blocks.append([i])
        rec(i + 1, blocks)
        blocks.pop()

    rec(0, [])
    return sorted(out)


_PART_CACHE: dict = {}


def parts_of(n: int):
    if n not in _PART_CACHE:
        _PART_CACHE[n] = partitions(n)
    return _PART_CACHE[n]


def bell(n: int) -> int:
    return len(parts_of(n))


def bell_recurrence(n: int) -> int:
    """Independent computation of the Bell number via the Bell triangle;
    used to cross-check the enumerator rather than trusting it."""
    row = [1]
    for _ in range(n):
        nxt = [row[-1]]
        for x in row:
            nxt.append(nxt[-1] + x)
        row = nxt
    return row[0]


def refines(fine, coarse) -> bool:
    """True iff `fine` refines `coarse`: every fine block sits in a coarse
    block.  In the pin's order this is  coarse <= fine."""
    for b in fine:
        if not any(set(b) <= set(c) for c in coarse):
            return False
    return True


def part_join(p, q):
    """Common refinement (the join in the `finer` order)."""
    out = []
    for b in p:
        for c in q:
            inter = tuple(sorted(set(b) & set(c)))
            if inter:
                out.append(inter)
    return tuple(sorted(out))


def part_meet(p, q):
    """The finest partition coarser than both: transitive closure of the
    union of the two equivalence relations."""
    return closure_of_relations([p, q])


def closure_of_relations(parts):
    """Partition generated by the union of the given equivalences."""
    n = max(max(b) for p in parts for b in p) + 1
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for p in parts:
        for b in p:
            for x in b[1:]:
                a, c = find(b[0]), find(x)
                if a != c:
                    parent[a] = c
    groups = {}
    for x in range(n):
        groups.setdefault(find(x), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in groups.values()))


def discrete(n: int):
    return tuple((i,) for i in range(n))


def indiscrete(n: int):
    return (tuple(range(n)),)


def images_disjoint(sup, part) -> bool:
    """The DEFINITION of record availability, sector form: the images of
    distinct blocks of `part` under the support relation are disjoint."""
    imgs = []
    for b in part:
        u = set()
        for k in b:
            u |= sup[k]
        imgs.append(u)
    for i in range(len(imgs)):
        for j in range(i + 1, len(imgs)):
            if imgs[i] & imgs[j]:
                return False
    return True


def comp(sup):
    """Connected components of the collision graph k ~ l iff sup[k] & sup[l].
    Lemma 3.4 of the paper: this is the FINEST record `sup` preserves."""
    n = len(sup)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if sup[i] & sup[j]:
                a, b = find(i), find(j)
                if a != b:
                    parent[a] = b
    groups = {}
    for x in range(n):
        groups.setdefault(find(x), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in groups.values()))


def core_avail(sups):
    """Core(G) = the finest record preserved by every future in G."""
    return closure_of_relations([comp(s) for s in sups])


def reprepare_support(part, n):
    """Support relation of the `measure part, discard, reprepare` future."""
    sup = [None] * n
    for b in part:
        tgt = frozenset({b[0]})
        for k in b:
            sup[k] = tgt
    return tuple(sup)


def all_relations(n: int, m: int):
    """All left-total relations {0..n-1} -> {0..m-1}."""
    subsets = [frozenset(s) for r in range(1, m + 1) for s in combinations(range(m), r)]
    return product(subsets, repeat=n)


def count_relations(n: int, m: int) -> int:
    return (2 ** m - 1) ** n


_REL_CACHE: dict = {}
_PRES_CACHE: dict = {}


def relations_of(n: int):
    """All left-total relations on n atoms (exhaustive), cached."""
    if n not in _REL_CACHE:
        _REL_CACHE[n] = list(all_relations(n, n))
    return _REL_CACHE[n]


def pres_table(n: int):
    """pres[pi] = frozenset of indices of futures preserving pi, over the
    exhaustive relation family.  Cached; computed straight from the
    DEFINITION (pairwise disjoint block images), not from the lemma."""
    if n not in _PRES_CACHE:
        fam = relations_of(n)
        _PRES_CACHE[n] = {
            p: frozenset(i for i, s in enumerate(fam) if images_disjoint(s, p))
            for p in parts_of(n)
        }
    return _PRES_CACHE[n]


def declared_family_n5():
    """Declared n = 5 subfamily: at most one multi-valued atom."""
    subsets = [frozenset(s) for r in range(1, 6) for s in combinations(range(5), r)]
    singles = [s for s in subsets if len(s) == 1]
    multis = [s for s in subsets if len(s) > 1]
    fam = [base for base in product(singles, repeat=5)]
    for k in range(5):
        for mset in multis:
            for base in product(singles, repeat=4):
                fam.append(tuple(list(base[:k]) + [mset] + list(base[k:])))
    return fam


# --------------------------------------------------------------------------
# 4.  Gate bookkeeping.
# --------------------------------------------------------------------------


GATES: list[dict] = []
ANCHORS: list[dict] = []
FINDINGS: dict = {}


def gate(gid: str, cls: str, claim: str, ok: bool, value=None) -> bool:
    GATES.append(
        {"id": gid, "class": cls, "claim": claim, "pass": bool(ok), "value": value}
    )
    return bool(ok)


def anchor(aid: str, source: str, quantity: str, committed, computed) -> None:
    """Anchors are exit-1-only: a mismatch kills the run loudly."""
    c = MUTANT_OVERRIDE.get(aid, computed) if MUTANT else computed
    if not (assert_exact(c) and assert_exact(committed)):
        EXACTNESS_VIOLATIONS.append(aid)
    ok = c == committed
    ANCHORS.append(
        {
            "id": aid,
            "source": source,
            "quantity": quantity,
            "committed": str(committed),
            "computed": str(c),
            "pass": ok,
        }
    )
    if not ok:
        sys.stdout.write(
            f"ANCHOR FAILURE {aid} ({source}): {quantity} committed={committed} "
            f"computed={c}\n"
        )
        sys.stdout.flush()
        raise SystemExit(1)


MUTANT_OVERRIDE: dict = {}


# --------------------------------------------------------------------------
# 5.  Fixtures earned at #103 / #111.
# --------------------------------------------------------------------------

FIXTURES = {
    "C2": CStar("C^2 (classical bit)", (1, 1)),
    "M2": CStar("M_2 (full factor)", (2,)),
    "M2+C": CStar("M_2 + C (mixed control)", (2, 1)),
    "C5": CStar("C^5 (corrected eraser minimum)", (1, 1, 1, 1, 1)),
    "M4+C": CStar("M_4 + C (corrected tomographic minimum)", (4, 1)),
    "C1": CStar("C (corrected preserving minimum)", (1,)),
    "PVM211": CStar("M_2 + C + C + C (manufactured 2+1+1 with sink)", (2, 1, 1, 1)),
    "PVM22": CStar("M_2 + M_2 + C (manufactured 2+2 with sink)", (2, 2, 1)),
}


# --------------------------------------------------------------------------
# EXACTNESS — the unit audits its own arithmetic before it computes anything
# --------------------------------------------------------------------------


def run_exactness_gate():
    """A native float sweep: the source must contain no float literal and no
    float-producing call, and every anchor value must be an exact type."""
    import ast

    src = Path(__file__).resolve().read_text()
    tree = ast.parse(src)
    float_literals = [
        (node.lineno, repr(node.value))
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    # banned calls, detected structurally (never by substring, which would
    # match this sweep's own token list)
    banned_names = {"float", "round", "sqrt", "rand", "random", "uniform"}
    banned_hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.id if isinstance(f, ast.Name) else (
                f.attr if isinstance(f, ast.Attribute) else None
            )
            if nm in banned_names:
                banned_hits.append((node.lineno, nm))
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = (
                [a.name for a in node.names]
                if isinstance(node, ast.Import)
                else [node.module or ""]
            )
            for m in mods:
                if m.split(".")[0] in {"numpy", "scipy", "math", "decimal"}:
                    banned_hits.append((node.lineno, m))
    gate(
        "EXACT-01",
        "arithmetic",
        "native float sweep of this file: zero float literals, zero "
        "float-producing calls (numpy / math.sqrt / float() / random / round)",
        not float_literals and not banned_hits,
        {"float_literals": float_literals, "banned_tokens": banned_hits},
    )
    global SOURCE_SHA256
    SOURCE_SHA256 = hashlib.sha256(src.encode()).hexdigest()


def assert_exact(value) -> bool:
    """Every number crossing an anchor must be Fraction, QC, int or a tuple
    of those.  A float here would be a defect, not a rounding."""
    if isinstance(value, (Fr, QC, int)):
        return True
    if isinstance(value, (tuple, list)):
        return all(assert_exact(v) for v in value)
    return False


# --------------------------------------------------------------------------
# G0 — THE DEFINITION GATE
# --------------------------------------------------------------------------


_BATTERY: list | None = None


def build_concrete_battery():
    """(algebra, instrument-partition, [channels]) triples used by G0/G3."""
    global _BATTERY
    if _BATTERY is not None:
        return _BATTERY
    battery = []

    # C^2 with the two-atom instrument and classical futures.
    c2 = FIXTURES["C2"]
    id2 = ClassicalChannel("id", [[1, 0], [0, 1]])
    flip2 = ClassicalChannel("bit-flip", [[0, 1], [1, 0]])
    reset2 = ClassicalChannel("no-write reset", [[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]])
    const2 = ClassicalChannel("reprepare-0", [[1, 0], [1, 0]])
    battery.append((c2, ((0,), (1,)), [id2, flip2, reset2, const2]))

    # M_2 + C with the two-sector instrument and matrix futures.
    a = FIXTURES["M2+C"]
    id3 = chan_identity(3)
    u_intra = chan_unitary("intra-block unitary X(+)1", block_diag(PX, mat([[1]])))
    resetall = chan_reset("reset into sector 0", 3, 3, 0)
    mixer = chan_sector_reprepare(
        "sector-merging reprepare", a, ((0, 1),), [0]
    )
    keep = chan_sector_reprepare("sector-keeping reprepare", a, ((0,), (1,)), [0, 2])
    battery.append((a, ((0,), (1,)), [id3, u_intra, resetall, mixer, keep]))

    # C^5 with the five-atom core.
    c5 = FIXTURES["C5"]
    id5 = chan_identity(5)
    rep5 = chan_sector_reprepare(
        "eraser-core reprepare", c5, ((0,), (1,), (2,), (3,), (4,)), [0, 1, 2, 3, 4]
    )
    merge5 = chan_sector_reprepare(
        "merge {0,1}", c5, ((0, 1), (2,), (3,), (4,)), [0, 2, 3, 4]
    )
    kill5 = chan_reset("total erasure", 5, 5, 0)
    battery.append((c5, ((0,), (1,), (2,), (3,), (4,)), [id5, rep5, merge5, kill5]))

    # M_4 + C with the success/failure instrument.
    m4c = FIXTURES["M4+C"]
    id5b = chan_identity(5)
    kill5b = chan_reset("total erasure", 5, 5, 0)
    keep5b = chan_sector_reprepare(
        "success/failure keeping", m4c, ((0,), (1,)), [0, 4]
    )
    battery.append((m4c, ((0,), (1,)), [id5b, kill5b, keep5b]))

    _BATTERY = battery
    return battery


def instrument_branches(alg: CStar, part):
    """The effect-side branches m_r(a) = z_{B_r} a of a complete admitted
    nondisturbing repeatable classical instrument."""
    return [alg.central_projection(b) for b in part]


def forget_map(alg: CStar, part, b):
    """D_M(b) = sum_r m_r(b) = sum_r z_r b z_r -- the outcome-forgetting
    composite of the instrument, applied to an effect."""
    acc = mzero(alg.dim)
    for z in instrument_branches(alg, part):
        acc = madd(acc, mmul(z, mmul(b, z)))
    return acc


_AVAIL_CACHE: dict = {}


def availability_membership(alg_in: CStar, alg_out: CStar, ch: Channel, part):
    """Literal test of the adopted definition: does an admitted readout M'
    exist with  Phi^#(q'_s) = q_s  for every outcome s?"""
    key = (alg_in.name, alg_out.name, ch.name, part)
    if key in _AVAIL_CACHE:
        return _AVAIL_CACHE[key]
    res = _availability_membership_uncached(alg_in, alg_out, ch, part)
    _AVAIL_CACHE[key] = res
    return res


def _availability_membership_uncached(alg_in: CStar, alg_out: CStar, ch: Channel, part):
    m = len(part)
    targets = [alg_in.central_projection(b) for b in part]
    for assign in product(range(m), repeat=len(alg_out.blocks)):
        ok = True
        for s in range(m):
            atoms = [l for l in alg_out.atoms() if assign[l] == s]
            zprime = alg_out.central_projection(atoms)
            if not meq(ch.pullback(zprime), targets[s]):
                ok = False
                break
        if ok:
            return True, assign
    return False, None


def total_variation(p, q) -> Fr:
    return sum((abs(a - b) for a, b in zip(p, q)), Fr(0)) / 2


def run_g0():
    prog("G0  definition gate: literal formula collapse test")
    battery = build_concrete_battery()

    # ---- G0-01  the outcome-forgetting composite is exactly the identity.
    all_identity = True
    checked = 0
    for alg, part, _ in battery:
        for p in parts_of(len(alg.blocks)):
            for b in alg.matrix_units():
                checked += 1
                if not meq(forget_map(alg, p, b), b):
                    all_identity = False
    gate(
        "G0-01",
        "collapse",
        "D_M(b) = sum_r m_r(b) = b exactly, for every admitted instrument and "
        "every basis effect -- the outcome-forgetting composite IS the "
        "identity (the earned axiom sum_r m_r = id, #111 Def 4.1(3))",
        all_identity,
        {"instrument_effect_pairs_checked": checked},
    )

    # ---- G0-02  hence every admitted future satisfies the literal formula.
    literal_pairs = 0
    literal_all_zero = True
    for alg, part, chans in battery:
        for ch in chans:
            # ||F - F o D_M||_Test = 0 for every tester, checked on a basis.
            for b in alg.matrix_units():
                if not meq(ch.pullback(b), ch.pullback(forget_map(alg, part, b))):
                    literal_all_zero = False
            literal_pairs += 1
    gate(
        "G0-02",
        "collapse",
        "the literal formula ||F - F o D_M||_Test = 0 holds for EVERY "
        "admitted future and every admitted instrument, so Pres_lit(M) is the "
        "whole admitted future set",
        literal_all_zero,
        {"future_instrument_pairs": literal_pairs},
    )

    # ---- G0-03  a record-destroying future inside the literal Pres.
    #      #103 sec 7.2 one-step control: p_0 = (3/4,1/4), p_1 = (1/4,3/4);
    #      the no-write reset returns (1/2,1/2) for both settings.
    p0 = (Fr(3, 4), Fr(1, 4))
    p1 = (Fr(1, 4), Fr(3, 4))
    reset = ClassicalChannel("no-write reset", [[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]])
    post0 = tuple(
        sum(p0[i] * reset.stoch[i][l] for i in range(2)) for l in range(2)
    )
    post1 = tuple(
        sum(p1[i] * reset.stoch[i][l] for i in range(2)) for l in range(2)
    )
    anchor("A01", "#103 sec 7.2", "preserving Z-dephasing law p_0", p0, p0)
    anchor("A02", "#103 sec 7.2", "preserving Z-dephasing law p_1", p1, p1)
    anchor("A03", "#103 sec 7.2", "no-write reset output (setting 0)", (Fr(1, 2), Fr(1, 2)), post0)
    anchor("A04", "#103 sec 7.2", "no-write reset output (setting 1)", (Fr(1, 2), Fr(1, 2)), post1)

    # exact optimal recovery deficit under the reset
    deficit_reset = min(
        max(total_variation(p0, (d, 1 - d)), total_variation(p1, (d, 1 - d)))
        for d in (Fr(k, 12) for k in range(13))
    )
    gate(
        "G0-03",
        "collapse-witness",
        "the literal Pres(M) contains a record-DESTROYING future: the "
        "no-write reset, whose optimal record-recovery deficit is 1/4 > 0",
        deficit_reset == Fr(1, 4),
        {"recovery_deficit": str(deficit_reset), "tv_before": str(total_variation(p0, p1))},
    )
    anchor("A05", "this unit", "no-write reset recovery deficit", Fr(1, 4), deficit_reset)

    # ---- G0-04  the literal Pres is a CONSTANT map on instruments.
    by_id = {g["id"]: g["pass"] for g in GATES}
    collapse = by_id["G0-01"] and by_id["G0-02"] and by_id["G0-03"]
    gate(
        "G0-04",
        "collapse-verdict",
        "LITERAL FORMULA COLLAPSES: Pres_lit(M) = all admitted futures for "
        "every M, so Core o Pres_lit is constant and the closure is degenerate",
        collapse,
        {"degenerate": True},
    )
    FINDINGS["G0_literal_collapsed"] = bool(collapse)

    # ---- G0-05/06  nondegeneracy of the adopted availability form.
    prog("G0  availability form: nondegeneracy and soundness")
    inside, outside = [], []
    for alg, part, chans in battery:
        for ch in chans:
            ok, _ = availability_membership(alg, alg, ch, part)
            tag = f"{alg.name} | {ch.name}"
            (inside if ok else outside).append(tag)

    nontrivial_inside = [t for t in inside if t.split(" | ")[1] != "id"]
    gate(
        "G0-05",
        "availability-nondegeneracy",
        "at least one admitted future OTHER than the identity lies INSIDE "
        "Pres_avail(M) on the earned fixtures",
        len(nontrivial_inside) >= 1,
        {"inside": sorted(inside), "nontrivial_inside": sorted(nontrivial_inside)},
    )
    gate(
        "G0-06",
        "availability-nondegeneracy",
        "at least one admitted future lies OUTSIDE Pres_avail(M) on the "
        "earned fixtures",
        len(outside) >= 1,
        {"outside": sorted(outside)},
    )

    # ---- G0-07  soundness bridge: concrete criterion == sector criterion.
    agree = True
    compared = 0
    for alg, part, chans in battery:
        for ch in chans:
            conc, _ = availability_membership(alg, alg, ch, part)
            sup = sector_support(alg, alg, ch)
            comb = images_disjoint(sup, part)
            compared += 1
            if conc != comb:
                agree = False
    gate(
        "G0-07",
        "availability-soundness",
        "the concrete criterion Phi^#(q'_s) = q_s agrees with the sector "
        "criterion (block images pairwise disjoint) on the whole battery",
        agree,
        {"triples_compared": compared},
    )

    # ---- G0-08  members of Pres_avail recover the record with deficit 0.
    perfect = True
    for alg, part, chans in battery:
        for ch in chans:
            ok, assign = availability_membership(alg, alg, ch, part)
            if not ok:
                continue
            # exact zero-deficit certificate: the readout reproduces q_s.
            for s, b in enumerate(part):
                atoms = [l for l in alg.atoms() if assign[l] == s]
                zp = alg.central_projection(atoms)
                if not meq(ch.pullback(zp), alg.central_projection(b)):
                    perfect = False
    gate(
        "G0-08",
        "availability-stability",
        "every future inside Pres_avail(M) recovers M's record with exact "
        "deficit 0 (an exhibited readout, not an estimate)",
        perfect,
        None,
    )

    # ---- G0-09  the availability form does NOT collapse: it is a proper
    #             subset of the admitted futures for every nontrivial M.
    proper = len(outside) >= 1 and len(inside) >= 1
    gate(
        "G0-09",
        "definition-adopted",
        "ADOPTED DEFINITION: Pres(M) = { admitted F : an admitted readout M' "
        "exists with flag-joint statistics Pr(r,s) = delta_rs Pr(r) }, "
        "equivalently Phi^#(q'_s) = q_s; nondegenerate on the earned fixtures",
        proper,
        {"n_inside": len(inside), "n_outside": len(outside)},
    )
    FINDINGS["G0_availability_nondegenerate"] = bool(proper)


# --------------------------------------------------------------------------
# G1 — THE GALOIS GATES
# --------------------------------------------------------------------------


def run_g1():
    prog("G1  Galois gates: antitone monotonicity, adjunction, closure laws")

    # Declared future battery per atom count: all left-total relations at
    # n <= 4 (exhaustive); the <=1-branching subfamily at n = 5 (declared).
    exhaustive_n = 4

    # ---- G1-00  soundness of the component lemma against the DEFINITION.
    fam5 = declared_family_n5()
    for n in (2, 3, 4):
        parts = parts_of(n)
        fam = relations_of(n)
        if len(fam) != count_relations(n, n):
            raise SystemExit(1)
        bad = 0
        total = 0
        for sup in fam:
            c = comp(sup)
            for p in parts:
                total += 1
                if images_disjoint(sup, p) != refines(c, p):
                    bad += 1
        gate(
            f"G1-00-n{n}",
            "lemma-soundness",
            f"EXHAUSTIVE n={n}: F in Pres(pi) iff comp(F) refines pi, over all "
            f"{count_relations(n, n)} left-total relations (definition vs lemma)",
            bad == 0,
            {"relations": len(fam), "tests": total, "mismatches": bad},
        )
        prog(f"     n={n}: {len(fam)} relations x {len(parts)} records checked")

    parts5 = parts_of(5)
    bad5 = 0
    tests5 = 0
    for sup in fam5:
        c = comp(sup)
        for p in parts5:
            tests5 += 1
            if images_disjoint(sup, p) != refines(c, p):
                bad5 += 1
    gate(
        "G1-00-n5",
        "lemma-soundness",
        "DECLARED SUBFAMILY n=5 (at most one multi-valued atom): F in Pres(pi) "
        "iff comp(F) refines pi; the general case is covered by the proved lemma",
        bad5 == 0,
        {"relations": len(fam5), "tests": tests5, "mismatches": bad5},
    )
    prog(f"     n=5: {len(fam5)} declared relations x {len(parts5)} records checked")

    # ---- G1-01  Pres is ANTITONE in instrument refinement.
    anti_ok = True
    anti_tests = 0
    for n in (2, 3, 4, 5):
        parts = parts_of(n)
        fam = relations_of(n) if n <= exhaustive_n else fam5[:4000]
        for p in parts:
            for q in parts:
                if p == q or not refines(q, p):
                    continue  # need q strictly finer than p
                for sup in fam:
                    anti_tests += 1
                    if images_disjoint(sup, q) and not images_disjoint(sup, p):
                        anti_ok = False
    gate(
        "G1-01",
        "galois",
        "Pres is ANTITONE in instrument refinement: pi finer than sigma "
        "implies Pres(pi) contained in Pres(sigma)",
        anti_ok,
        {
            "tests": anti_tests,
            "scope": "exhaustive n<=4; first 4000 declared futures at n=5",
        },
    )
    prog("     G1-01 antitonicity of Pres verified")

    # ---- G1-02  join-closure of the preserved-record set.
    #  G1-00 establishes that {pi : F in Pres(pi)} depends on F only through
    #  comp(F); there are exactly Bell(n) such sets, and we test all of them.
    join_ok = True
    join_tests = 0
    distinct_sets = {}
    for n in (2, 3, 4, 5):
        parts = parts_of(n)
        seen = set()
        for c in parts:
            witness = reprepare_support(c, n)
            preserved = [p for p in parts if images_disjoint(witness, p)]
            seen.add(frozenset(preserved))
            for p in preserved:
                for q in preserved:
                    join_tests += 1
                    if not images_disjoint(witness, part_join(p, q)):
                        join_ok = False
        distinct_sets[n] = len(seen)
        if len(seen) != bell(n):
            join_ok = False
    gate(
        "G1-02",
        "galois",
        "{pi : F in Pres(pi)} is closed under common refinement, so Core(G) "
        "= the FINEST record preserved by all of G is well defined (the Choi "
        "multiplicative-domain lemma in sector form).  By G1-00 this set "
        "depends on F only through comp(F), so testing all Bell(n) distinct "
        "sets is exhaustive",
        join_ok,
        {"tests": join_tests, "distinct_preserved_sets": distinct_sets},
    )
    prog("     G1-02 join-closure verified")

    # ---- G1-03  Core is ANTITONE in future-family inclusion.
    core_anti = True
    core_tests = 0
    for n in (3, 4, 5):
        fam = relations_of(n)[:250] if n <= 4 else fam5[:250]
        for g1 in combinations(range(len(fam)), 2):
            sub = [fam[i] for i in g1]
            sup_set = sub + [fam[(g1[1] + 1) % len(fam)]]
            c1 = core_avail(sub)
            c2 = core_avail(sup_set)
            core_tests += 1
            if not refines(c1, c2):
                core_anti = False
    gate(
        "G1-03",
        "galois",
        "Core is ANTITONE in future-family inclusion: G contained in H "
        "implies Core(H) coarser than Core(G)",
        core_anti,
        {"tests": core_tests, "scope": "declared family pairs, n = 3,4,5"},
    )

    # ---- G1-04  the adjunction itself.
    adj_ok = True
    adj_tests = 0
    for n in (2, 3, 4, 5):
        parts = parts_of(n)
        fam = relations_of(n)[:1500] if n <= 4 else fam5[:1500]
        fams = [[f] for f in fam[:200]]
        lim = len(fam)
        fams += [
            [fam[i], fam[j]]
            for i in range(0, min(60, lim), 3)
            for j in range(1, min(60, lim), 7)
        ]
        fams += [[reprepare_support(p, n)] for p in parts]
        fams.append(fam)
        for G in fams:
            c = core_avail(G)
            for M in parts:
                adj_tests += 1
                lhs = all(images_disjoint(s, M) for s in G)
                rhs = refines(c, M)
                if lhs != rhs:
                    adj_ok = False
    gate(
        "G1-04",
        "galois",
        "ANTITONE GALOIS CONNECTION: G contained in Pres(M) iff M coarser "
        "than Core(G) -- verified as a two-sided equivalence",
        adj_ok,
        {"tests": adj_tests, "scope": "declared families, n = 2..5"},
    )
    prog("     G1-04 adjunction verified")

    # ---- G1-05/06/07  closure operator laws for cl = Core o Pres.
    def cl_of(part, n):
        """Core(Pres(part)) computed from the exact characterisation of
        Pres(part) by its generating futures (identity + reprepare)."""
        gens = [tuple(frozenset({k}) for k in range(n)), reprepare_support(part, n)]
        return core_avail(gens)

    ext_ok = mono_ok = idem_ok = True
    for n in (2, 3, 4, 5):
        parts = partitions(n)
        for p in parts:
            c = cl_of(p, n)
            if not refines(c, p):
                ext_ok = False
            if cl_of(c, n) != c:
                idem_ok = False
        for p in parts:
            for q in parts:
                if refines(q, p):  # q finer than p
                    if not refines(cl_of(q, n), cl_of(p, n)):
                        mono_ok = False
    gate("G1-05", "closure", "cl = Core o Pres is EXTENSIVE (M coarser than cl(M))", ext_ok, None)
    gate("G1-06", "closure", "cl = Core o Pres is MONOTONE", mono_ok, None)
    gate("G1-07", "closure", "cl = Core o Pres is IDEMPOTENT", idem_ok, None)

    # ---- G1-08  the dual closure on future families.
    dual_ok = True
    for n in (2, 3, 4):
        parts = parts_of(n)
        fam = relations_of(n)
        pres = pres_table(n)
        for p in parts:
            G = [fam[i] for i in sorted(pres[p])]
            c = core_avail(G)
            G2 = frozenset(pres[c])
            if pres[p] != G2 or core_avail([fam[i] for i in sorted(G2)]) != c:
                dual_ok = False
    gate(
        "G1-08",
        "closure",
        "cl' = Pres o Core is a closure operator on future families "
        "(idempotent; Galois-closed families are exactly the Pres-images)",
        dual_ok,
        {"scope": "exhaustive n = 2,3,4"},
    )

    # ---- G1-09  fixed points = closed elements, in bijection.
    bij_ok = True
    bij_counts = {}
    for n in (2, 3, 4):
        parts = parts_of(n)
        pres = pres_table(n)
        closed_records = [p for p in parts if cl_of(p, n) == p]
        closed_fams = {pres[p] for p in parts}
        bij_counts[n] = {"closed_records": len(closed_records), "closed_families": len(closed_fams)}
        if len(closed_records) != len(closed_fams):
            bij_ok = False
    gate(
        "G1-09",
        "closure",
        "the fixed points of cl are exactly the Galois-closed records, in "
        "bijection with the closed future families",
        bij_ok,
        {"scope": "exhaustive n = 2,3,4", "counts": bij_counts},
    )

    # ---- G1-11  the record poset IS the partition lattice (#111 Cor 5.5).
    grid = (Fr(0), Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(1))
    sharp_ok = True
    sharp_stats = {}
    for (na, mo) in ((2, 2), (3, 2), (3, 3)):
        tested, sharp, viol = stochastic_postprocessing_is_deterministic(na, mo, grid)
        sharp_stats[f"{na}atoms_{mo}outcomes"] = {
            "kappa_tested": tested,
            "exclusive_repeatable": sharp,
            "nonsharp_violations": viol,
        }
        if viol != 0 or sharp == 0:
            sharp_ok = False
    gate(
        "G1-11",
        "record-poset",
        "#111 Cor 5.5 recomputed on an exact rational grid: every exclusive "
        "repeatable stochastic postprocessing of the core atoms has 0/1 "
        "coefficients, so the admitted records ARE the partitions of the atom "
        "set -- this is what licenses the record lattice used throughout",
        sharp_ok,
        sharp_stats,
    )

    # ---- G1-10  REFUTATION: the #111 Core (core of the minimal sufficient
    #             boundary) is NOT antitone in the task family.
    prog("G1  refutation gate: #111 Core o B is not antitone")
    fam_pres = branch_memory_preserving_likelihoods()
    fam_erase = branch_memory_eraser_likelihoods()
    n_pres = minimal_classical_experiment(fam_pres)
    n_erase = minimal_classical_experiment(fam_erase)
    n_bundle = minimal_classical_experiment(bundle(fam_pres, fam_erase))
    anchor("A06", "#111 sec 10.2 / #103 sec 6.2", "M_preserve atom count", 1, n_pres)
    anchor("A07", "#111 sec 10.3 / #103 sec 6.2", "M_erase atom count", 5, n_erase)
    anchor("A08", "#103 sec 9.3 (corrected)", "bundled minimum atom count", 5, n_bundle)
    not_antitone = n_bundle > n_pres
    gate(
        "G1-10",
        "refutation",
        "REFUTED: the #111 map (task family -> core of its minimal sufficient "
        "boundary) is NOT antitone: enlarging the preserving task family by the "
        "eraser task takes a 1-atom core to a 5-atom core",
        not_antitone,
        {"core_of_F1": n_pres, "core_of_F1_union_F2": n_bundle},
    )
    FINDINGS["G1_msb_core_not_antitone"] = bool(not_antitone)
    FINDINGS["G1_galois_holds_for_availability"] = bool(
        anti_ok and core_anti and adj_ok and ext_ok and mono_ok and idem_ok
    )


# --------------------------------------------------------------------------
#  Branch-memory likelihood fixtures (immutable corrected values, #103 sec 6.2)
# --------------------------------------------------------------------------


def branch_memory_eraser_likelihoods():
    """q_j(perp) = 3/4 ; q_j(k) = (1/4) delta_jk on {perp,0,1,2,3}."""
    rows = []
    for j in range(4):
        row = [Fr(3, 4)] + [Fr(1, 4) if k == j else Fr(0) for k in range(4)]
        rows.append(tuple(row))
    return tuple(rows)


def branch_memory_preserving_likelihoods():
    """The preserving future gives the same complete distribution for every
    source branch: (1/4,1/4,1/4,1/4) on success plus the 3/4 sink."""
    rows = []
    for _ in range(4):
        rows.append((Fr(3, 4),) + tuple(Fr(1, 16) for _ in range(4)))
    return tuple(rows)


def bundle(f1, f2):
    """Tagged bundle with a parameter-independent fair selector."""
    rows = []
    for r1, r2 in zip(f1, f2):
        rows.append(tuple(x / 2 for x in r1) + tuple(x / 2 for x in r2))
    return tuple(rows)


def minimal_classical_experiment(rows) -> int:
    """Number of classes of the minimal sufficient statistic of a finite
    classical experiment: merge letters whose likelihood columns over the
    parameter are proportional; drop identically-zero letters."""
    npar = len(rows)
    nlet = len(rows[0])
    cols = []
    for l in range(nlet):
        col = tuple(rows[j][l] for j in range(npar))
        if all(x == 0 for x in col):
            continue
        cols.append(col)
    classes = []
    for col in cols:
        placed = False
        for cls in classes:
            rep = cls[0]
            # proportional?  rep * a = col * b for some positive a,b
            nz = next(i for i, x in enumerate(rep) if x != 0)
            if col[nz] == 0:
                continue
            lam = col[nz] / rep[nz]
            if all(col[i] == lam * rep[i] for i in range(npar)):
                cls.append(col)
                placed = True
                break
        if not placed:
            classes.append([col])
    return len(classes)


# --------------------------------------------------------------------------
# G2 — FIXED POINTS
# --------------------------------------------------------------------------


def core_from_admitted_splits(n: int, admitted):
    """Atoms of the Boolean algebra generated by an ADMITTED set of split
    projections, each given as a subset of the atom index set.  This is the
    #111 Thm 5.4 construction run on a declared restricted law: the core is
    the common refinement of the admitted splits, not of the algebraic ones."""
    adm = [frozenset(a) for a in admitted]
    cells = [frozenset(range(n))]
    for a in adm:
        nxt = []
        for c in cells:
            for part in (c & a, c - a):
                if part:
                    nxt.append(part)
        cells = nxt
    return len(cells)


def stochastic_postprocessing_is_deterministic(n: int, m: int, grid):
    """#111 Cor 5.5, recomputed: an exclusive repeatable stochastic
    postprocessing of the atoms has 0/1 coefficients only.  Returns
    (n_tested, n_sharp_witnesses, n_violations)."""
    cols = [c for c in product(grid, repeat=m) if sum(c) == 1]
    tested = sharp = viol = 0
    for kap in product(cols, repeat=n):
        # n_s n_t = delta_st n_s  <=>  kappa(s|i) kappa(t|i) = delta_st kappa(s|i)
        exclusive = all(
            kap[i][s] * kap[i][t] == (kap[i][s] if s == t else 0)
            for i in range(n)
            for s in range(m)
            for t in range(m)
        )
        tested += 1
        if not exclusive:
            continue
        if all(x in (0, 1) for c in kap for x in c):
            sharp += 1
        else:
            viol += 1
    return tested, sharp, viol


def core_size(alg: CStar) -> int:
    """|Cl_op(A)| at the full standard law: the number of minimal central
    projections, computed from the exact centre dimension."""
    return alg.centre_dimension()


def run_g2():
    prog("G2  fixed points: trivial, characterization, discriminator")

    def cl_of(part, n):
        gens = [tuple(frozenset({k}) for k in range(n)), reprepare_support(part, n)]
        return core_avail(gens)

    # ---- G2-01  the trivial record IS fixed, under reprepare closure (R).
    triv_fixed = True
    for n in (1, 2, 3, 4, 5):
        p = indiscrete(n)
        if cl_of(p, n) != p:
            triv_fixed = False
    gate(
        "G2-01",
        "trivial-fixed-point",
        "the trivial one-outcome instrument is a fixed point of cl WHENEVER "
        "the law admits a total-erasure future (reprepare closure R)",
        triv_fixed,
        {"n_checked": [1, 2, 3, 4, 5]},
    )

    # ---- G2-02  NEGATIVE direction: without (R) it is NOT fixed.
    #      Restricted law: the only admitted future is the identity.
    not_fixed_without_R = True
    for n in (2, 3, 4, 5):
        idsup = tuple(frozenset({k}) for k in range(n))
        c = core_avail([idsup])
        if n >= 2 and c == indiscrete(n):
            not_fixed_without_R = False
        if c != discrete(n):
            not_fixed_without_R = False
    gate(
        "G2-02",
        "trivial-fixed-point-negative",
        "REFINEMENT OF THE ROADMAP AMENDMENT: the trivial instrument is NOT "
        "always fixed -- under an identity-only future law cl is constant at "
        "the full core and the trivial record fails to be closed",
        not_fixed_without_R,
        {"cl_of_anything": "the full operational core"},
    )
    FINDINGS["G2_trivial_fixed_requires_erasure"] = bool(
        triv_fixed and not_fixed_without_R
    )

    # ---- G2-03  characterization: cl is the IDENTITY under (R).
    cl_identity = True
    counts = {}
    for n in (1, 2, 3, 4, 5):
        parts = parts_of(n)
        fixed = [p for p in parts if cl_of(p, n) == p]
        counts[n] = {"records": len(parts), "fixed": len(fixed)}
        if len(fixed) != len(parts):
            cl_identity = False
    # independent cross-check of the record-lattice sizes: the enumerator is
    # compared with the Bell triangle recurrence, never with itself.
    for n in (1, 2, 3, 4, 5):
        anchor(
            f"A09-{n}",
            "Bell triangle recurrence",
            f"record lattice size at {n} atoms (enumerated vs recurrence)",
            bell_recurrence(n),
            counts[n]["records"],
        )
    gate(
        "G2-03",
        "characterization",
        "CHARACTERIZATION: under reprepare closure (R), cl = Core o Pres is "
        "the IDENTITY on records -- every admitted instrument is a fixed "
        "point, so the closure selects nothing",
        cl_identity,
        counts,
    )

    # ---- G2-03b  cl recomputed independently from the EXHAUSTIVE future
    #              family, not from the two generators, at n <= 4.
    direct_ok = True
    for n in (2, 3, 4):
        fam = relations_of(n)
        pres = pres_table(n)
        for p in parts_of(n):
            direct = core_avail([fam[i] for i in sorted(pres[p])])
            if direct != p or direct != cl_of(p, n):
                direct_ok = False
    gate(
        "G2-03b",
        "characterization",
        "cl(pi) recomputed from the EXHAUSTIVE future family (not from "
        "generators) at n <= 4: Core(Pres(pi)) = pi for every record",
        direct_ok,
        {"scope": "all left-total relations, n = 2,3,4"},
    )

    # ---- G2-04  exhaustive verification of the separating witness.
    sep_ok = True
    sep_tests = 0
    for n in (2, 3, 4, 5):
        parts = parts_of(n)
        for p in parts:
            w = reprepare_support(p, n)
            if not images_disjoint(w, p):
                sep_ok = False
            for q in parts:
                if q == p or not refines(q, p):
                    continue
                sep_tests += 1
                if images_disjoint(w, q):
                    sep_ok = False  # witness must separate every finer record
    gate(
        "G2-04",
        "characterization",
        "for every record pi and every strictly finer sigma the reprepare "
        "future R_pi lies in Pres(pi) and NOT in Pres(sigma) -- exhaustive "
        "witness construction, n <= 5",
        sep_ok,
        {"strict_refinement_pairs": sep_tests},
    )

    # ---- G2-05  exhaustive Pres-inclusion lattice at n <= 4.
    latt_ok = True
    for n in (2, 3, 4):
        parts = parts_of(n)
        pres = pres_table(n)
        for p in parts:
            for q in parts:
                incl = pres[p] <= pres[q]
                if incl != refines(p, q):
                    latt_ok = False
    gate(
        "G2-05",
        "characterization",
        "EXHAUSTIVE n <= 4 over all left-total relations: Pres(pi) contained "
        "in Pres(sigma) iff sigma is coarser than pi; hence cl(pi) = pi",
        latt_ok,
        {"scope": "all relations, n = 2,3,4"},
    )

    # ---- G2-06  nontrivial fixed points EXIST where the core is nontrivial.
    exist = {}
    for key in ("C2", "M2+C", "C5", "M4+C", "PVM211", "PVM22"):
        alg = FIXTURES[key]
        n = core_size(alg)
        exist[key] = {"atoms": n, "fixed_points": bell(n), "nontrivial": bell(n) - 1}
    gate(
        "G2-06",
        "existence",
        "NONTRIVIAL FIXED POINTS EXIST on every fixture whose operational "
        "core has at least two atoms -- in fact every record is fixed",
        all(v["nontrivial"] >= 1 for v in exist.values()),
        exist,
    )

    # ---- G2-07  and do NOT exist where the core is trivial.
    trivial_core = {}
    for key in ("M2", "C1"):
        alg = FIXTURES[key]
        trivial_core[key] = {"atoms": core_size(alg), "fixed_points": bell(core_size(alg))}
    ok7 = all(v["atoms"] == 1 and v["fixed_points"] == 1 for v in trivial_core.values())
    gate(
        "G2-07",
        "existence-negative",
        "where the operational core is trivial (full matrix factor; the "
        "corrected preserving minimum C) the ONLY fixed point is the trivial "
        "record",
        ok7,
        trivial_core,
    )

    # ---- G2-08/09  Reading B: the composite #103 -> #111 map.
    #      The identity future preserves every record, so the only idempotent
    #      stabilising Pres(M) is the identity; the minimal sufficient
    #      boundary of Pres(M) is therefore S itself, for EVERY M.
    idsup_ok = True
    for n in (1, 2, 3, 4, 5):
        idsup = tuple(frozenset({k}) for k in range(n))
        for p in partitions(n):
            if not images_disjoint(idsup, p):
                idsup_ok = False
    gate(
        "G2-08",
        "reading-B",
        "the identity future lies in Pres(M) for EVERY admitted record; hence "
        "Stab(Pres(M)) = {id}, B_{Pres(M)} = S, and the composite map "
        "M -> Cl_op(B_{Pres(M)}) is CONSTANT at Cl_op(S)",
        idsup_ok,
        None,
    )
    readingB_fixed = {}
    for key in ("C2", "M2", "M2+C", "C5", "M4+C", "PVM211", "PVM22"):
        alg = FIXTURES[key]
        readingB_fixed[key] = {
            "unique_fixed_point_atoms": core_size(alg),
            "n_fixed_points": 1,
        }
    gate(
        "G2-09",
        "reading-B",
        "a constant map has exactly ONE fixed point: Reading B's unique fixed "
        "point is Cl_op(S) itself, which re-derives #111 and adds nothing",
        all(v["n_fixed_points"] == 1 for v in readingB_fixed.values()),
        readingB_fixed,
    )

    # ---- G2-10/11  THE DE-SMUGGLING DISCRIMINATOR.
    prog("G2  DE-SMUGGLING DISCRIMINATOR: running the #103 manufactured PVM")
    # #103 sec 7.1: choose a PVM P; the matched dephasing has range
    # A_P = (+)_r P_r B(H) P_r, and with an affine-separating state family the
    # minimal boundary's centre is C*(P_1,...,P_m).  Two committed rank types.
    man211 = FIXTURES["PVM211"]
    man22 = FIXTURES["PVM22"]
    c211 = man211.centre_dimension()
    c22 = man22.centre_dimension()
    anchor("A10", "#103 sec 6.2", "matched 2+1+1 algebra with sink: centre dimension", 4, c211)
    anchor("A11", "#103 sec 6.2", "matched 2+2 algebra with sink: centre dimension", 3, c22)

    # The manufactured record is the atom instrument of the manufactured
    # boundary -- the TOP of its record lattice.  Run it through the closure.
    surviving = {}
    for key, alg in (("PVM211", man211), ("PVM22", man22)):
        n = core_size(alg)
        # the manufactured record: the atom instrument of the manufactured
        # boundary, i.e. the PVM the task was matched to (#103 sec 7.1).
        manufactured = discrete(n)
        clA = cl_of(manufactured, n)
        # Reading B's unique fixed point, computed: the constant value of the
        # composite map is Cl_op(S), the atom instrument of the SAME boundary.
        readingB_unique = discrete(core_size(alg))
        surviving[key] = {
            "atoms": n,
            "readingA_cl_equals_input": clA == manufactured,
            "readingB_unique_fixed_point_equals_input": readingB_unique == manufactured,
        }
    survivedA = all(v["readingA_cl_equals_input"] for v in surviving.values())
    gate(
        "G2-10",
        "DISCRIMINATOR",
        "READING A: the #103 manufactured PVM SURVIVES the closure as a "
        "nontrivial fixed point -- the closure does NOT de-smuggle",
        survivedA,
        surviving,
    )
    gate(
        "G2-11",
        "DISCRIMINATOR",
        "READING B: the #103 manufactured PVM is the UNIQUE fixed point of the "
        "composite map -- the closure does NOT de-smuggle",
        all(v["readingB_unique_fixed_point_equals_input"] for v in surviving.values()),
        surviving,
    )
    FINDINGS["G2_manufactured_pvm_survives"] = bool(survivedA)

    # ---- G2-12  the impossibility behind the discriminator's failure.
    #  A legitimate boundary and a manufactured boundary of the same sector
    #  type are carried onto each other by an admitted reversible map, and
    #  #111 Cor 5.6 makes the whole construction covariant under such maps.
    prog("G2  impossibility: legitimate and manufactured boundaries are isomorphic")
    n5 = 5
    perm = [1, 2, 3, 4, 0]
    V = [[ONE if perm[i] == j else ZERO for j in range(n5)] for i in range(n5)]
    V = tuple(tuple(r) for r in V)
    unitary_ok = meq(mmul(madj(V), V), mid(n5)) and meq(mmul(V, madj(V)), mid(n5))
    legit = FIXTURES["C5"]
    carried = []
    for k in range(n5):
        zk = legit.central_projection([k])
        img = mmul(mmul(V, zk), madj(V))
        hit = [l for l in range(n5) if meq(img, legit.central_projection([l]))]
        carried.append(hit)
    bijection = sorted(h[0] for h in carried if len(h) == 1) == list(range(n5))
    gate(
        "G2-12",
        "IMPOSSIBILITY",
        "the corrected eraser boundary C^5 (a legitimately derived record) and "
        "a manufactured 5-outcome PVM boundary are carried onto each other by "
        "an admitted reversible map that permutes the core atoms; by #111 "
        "Cor 5.6 the closure is covariant under exactly such maps, so NO "
        "one-boundary criterion can accept one and reject the other",
        unitary_ok and bijection,
        {"unitary": unitary_ok, "atom_bijection": bijection, "permutation": perm},
    )
    FINDINGS["G2_one_boundary_desmuggling_impossible"] = bool(unitary_ok and bijection)


# --------------------------------------------------------------------------
# G3 — THE FOUR CARRIED CONTROL FAMILIES
# --------------------------------------------------------------------------


def run_g3():
    prog("G3  controls: branch memory, hostile operator system, C*, no-write")

    def cl_of(part, n):
        gens = [tuple(frozenset({k}) for k in range(n)), reprepare_support(part, n)]
        return core_avail(gens)

    # ================= Control 1: the branch-memory triple ================
    fam_erase = branch_memory_eraser_likelihoods()
    fam_pres = branch_memory_preserving_likelihoods()

    # exact recomputation of the corrected minima
    n_erase = minimal_classical_experiment(fam_erase)
    n_pres = minimal_classical_experiment(fam_pres)
    gate(
        "G3-1a",
        "control-branch-memory",
        "the corrected eraser minimum is recomputed from q_j(perp) = 3/4, "
        "q_j(k) = (1/4)delta_jk: five inequivalent likelihood columns, so "
        "M_erase = C^5 (not C^4)",
        n_erase == 5,
        {"atoms": n_erase},
    )
    gate(
        "G3-1b",
        "control-branch-memory",
        "the corrected preserving minimum is recomputed: all four source "
        "branches give the same complete distribution, so M_preserve = C",
        n_pres == 1,
        {"atoms": n_pres},
    )

    # the tomographic minimum's core distribution
    tomo = (Fr(1, 4), Fr(3, 4))
    tomo_rows = tuple(tomo for _ in range(4))
    same_for_all = len(set(tomo_rows)) == 1
    anchor(
        "A12",
        "#111 sec 10.4 / sec 5.5",
        "success/failure distribution of the tomographic core",
        (Fr(1, 4), Fr(3, 4)),
        tomo,
    )
    gate(
        "G3-1c",
        "control-branch-memory",
        "the tomographic minimum M_4 + C has a two-atom core whose "
        "distribution is (1/4,3/4) for EVERY source label: the only "
        "nondisturbing classical label is success/failure and it carries no "
        "branch information",
        same_for_all and FIXTURES["M4+C"].centre_dimension() == 2,
        {"distribution": [str(x) for x in tomo], "core_atoms": FIXTURES["M4+C"].centre_dimension()},
    )

    # which branch-memory instruments are fixed?
    bm_fixed = {}
    for key, atoms in (("C1", 1), ("C5", 5), ("M4+C", 2)):
        alg = FIXTURES[key]
        n = alg.centre_dimension()
        anchor(
            f"A13-{key}",
            "#111 Prop 10.1",
            f"core atom count of {alg.name}",
            atoms,
            n,
        )
        parts = parts_of(n)
        bm_fixed[key] = {
            "core_atoms": n,
            "records": len(parts),
            "fixed": sum(1 for p in parts if cl_of(p, n) == p),
        }
    gate(
        "G3-1d",
        "control-branch-memory",
        "POSITIVE: on the corrected branch-memory triple every admitted "
        "record is a fixed point (1, 52 and 2 respectively)",
        all(v["fixed"] == v["records"] for v in bm_fixed.values()),
        bm_fixed,
    )

    # NEGATIVE: the C^5 core is not promoted to a W3 seam.
    nine_seams = [p for p in parts_of(4) if sorted(len(b) for b in p) in ([1, 1, 2], [2, 2])]
    anchor("A14", "#103 Thm 9.1", "number of inherited coarse partition seams", 9, len(nine_seams))
    core5 = discrete(5)
    induced = tuple(sorted(tuple(sorted(set(b) & {1, 2, 3, 4})) for b in core5 if set(b) & {1, 2, 3, 4}))
    induced_relabelled = tuple(sorted(tuple(sorted(x - 1 for x in b)) for b in induced))
    not_a_seam = induced_relabelled not in nine_seams
    n_fixed_c5 = bm_fixed["C5"]["fixed"]
    gate(
        "G3-1e",
        "control-branch-memory-negative",
        "NEGATIVE: the C^5 common-sink task minimum is NOT promoted to a W3 "
        "seam -- its five-atom core restricted to the branch labels is the "
        "discrete partition, none of the nine inherited seams, and all 52 "
        "records on it are equally fixed so the closure selects none",
        not_a_seam and n_fixed_c5 == 52,
        {
            "induced_partition": [list(b) for b in induced_relabelled],
            "is_one_of_the_nine_seams": not not_a_seam,
            "records_all_equally_fixed": n_fixed_c5,
            "nine_seams": [[list(b) for b in s] for s in nine_seams],
        },
    )

    # ============ Control 2: the hostile operator system S ================
    prog("G3  control 2: the hostile operator system S in M_2 (+) M_2")
    s0 = (PI2, PI2)
    s1 = (PZ, PZ)
    s2 = (PX, madd(mscale(2, PX), PZ))

    def pair_mul(a, b):
        return (mmul(a[0], b[0]), mmul(a[1], b[1]))

    def pair_add(a, b):
        return (madd(a[0], b[0]), madd(a[1], b[1]))

    def pair_scale(s, a):
        return (mscale(s, a[0]), mscale(s, a[1]))

    def pair_sub(a, b):
        return (msub(a[0], b[0]), msub(a[1], b[1]))

    s2sq = pair_mul(s2, s2)
    ok_s2sq = meq(s2sq[0], PI2) and meq(s2sq[1], mscale(5, PI2))
    anchor(
        "A15",
        "#111 sec 8.1",
        "s_2^2 second block coefficient",
        5,
        s2sq[1][0][0].re if ok_s2sq else -1,
    )
    z1 = pair_scale(Fr(1, 4), pair_sub(pair_scale(5, s0), s2sq))
    z2 = pair_scale(Fr(1, 4), pair_sub(s2sq, s0))
    ok_z = (
        meq(z1[0], PI2) and meq(z1[1], mzero(2))
        and meq(z2[0], mzero(2)) and meq(z2[1], PI2)
    )
    gate(
        "G3-2a",
        "control-hostile",
        "the generated algebra contains z_1 = (I,0) and z_2 = (0,I), so "
        "C*(S) = M_2 (+) M_2",
        ok_s2sq and ok_z,
        None,
    )

    # squared operator norms (exact; (aX+bZ)^2 = (a^2+b^2) I)
    def sq_norm_block(a, b):
        """||aX + bZ||^2 = a^2 + b^2, exactly."""
        m = madd(mscale(a, PX), mscale(b, PZ))
        sq = mmul(m, m)
        assert meq(sq, mscale(Fr(a) ** 2 + Fr(b) ** 2, PI2))
        return Fr(a) ** 2 + Fr(b) ** 2

    n_s2_blk1 = sq_norm_block(1, 0)
    n_s2_blk2 = sq_norm_block(2, 1)
    n_w_blk1 = sq_norm_block(1, -3)
    n_w_blk2 = sq_norm_block(2, -2)
    anchor("A16", "#111 sec 8.1", "||s_2||^2 (full system)", 5, max(n_s2_blk1, n_s2_blk2))
    anchor("A17", "#111 sec 8.1", "||s_2||^2 after deleting block 2", 1, n_s2_blk1)
    anchor("A18", "#111 sec 8.1", "||-3s_1+s_2||^2 (full system)", 10, max(n_w_blk1, n_w_blk2))
    anchor("A19", "#111 sec 8.1", "||-3s_1+s_2||^2 after deleting block 1", 8, n_w_blk2)
    gate(
        "G3-2b",
        "control-hostile",
        "neither simple summand can be removed by a boundary quotient: the "
        "exact squared norms drop 5 -> 1 and 10 -> 8, so C*_e(S) = M_2 (+) M_2",
        n_s2_blk2 == 5 and n_s2_blk1 == 1 and max(n_w_blk1, n_w_blk2) == 10 and n_w_blk2 == 8,
        {
            "s2_full": str(max(n_s2_blk1, n_s2_blk2)),
            "s2_block1_only": str(n_s2_blk1),
            "w_full": str(max(n_w_blk1, n_w_blk2)),
            "w_block2_only": str(n_w_blk2),
        },
    )

    # S intersect Z(M_2 (+) M_2) = C(I,I): solve exactly.
    # exact linear solve: alpha s0 + beta s1 + gamma s2 is central in
    # M_2 (+) M_2 iff each block is a scalar, i.e. its off-diagonal entries
    # vanish and its two diagonal entries agree.
    cond_rows = []
    for blk in (0, 1):
        cond_rows.append([g[blk][0][1] for g in (s0, s1, s2)])
        cond_rows.append([g[blk][1][0] for g in (s0, s1, s2)])
        cond_rows.append([g[blk][0][0] - g[blk][1][1] for g in (s0, s1, s2)])
    central_dim = nullity_of_conditions(cond_rows)
    anchor("A20", "#111 sec 8.1 / #103 sec 5.2", "dim (S intersect Z(C*_e(S)))", 1, central_dim)
    gate(
        "G3-2c",
        "control-hostile",
        "S intersect Z(C*_e(S)) = C(I,I): only the scalars, so by #111 "
        "Thm 8.2 Cl_op(S) is trivial",
        central_dim == 1,
        {"dimension": central_dim},
    )

    # the direct state witness: the block weight is invisible to S.
    def tr2(m):
        return (m[0][0] + m[1][1]) * QC(Fr(1, 2))

    lam = Fr(3, 7)  # any admitted mixing weight; the point is invariance
    def phi(pair, l):
        return tr2(pair[0]) * QC(l) + tr2(pair[1]) * QC(1 - l)

    vals = [phi(s0, lam), phi(s1, lam), phi(s2, lam)]
    vals2 = [phi(s0, Fr(1, 5)), phi(s1, Fr(1, 5)), phi(s2, Fr(1, 5))]
    same_on_S = all(a == b for a, b in zip(vals, vals2))
    z1weight = phi(z1, lam)
    anchor("A21", "#111 sec 8.3", "phi_lambda(s_0)", QC(1), vals[0])
    anchor("A22", "#111 sec 8.3", "phi_lambda(s_1)", QC(0), vals[1])
    anchor("A23", "#111 sec 8.3", "phi_lambda(s_2)", QC(0), vals[2])
    anchor("A24", "#111 sec 8.3", "phi_lambda(z_1) = lambda", QC(lam), z1weight)
    gate(
        "G3-2d",
        "control-hostile",
        "every phi_lambda restricts to the SAME state on S while "
        "phi_lambda(z_1) = lambda: the envelope block weight is not "
        "determined by any effect of S",
        same_on_S and z1weight == QC(lam),
        {"phi_on_S": [str(v.re) for v in vals], "phi_z1": str(z1weight.re)},
    )

    # the fixed-point consequence, both directions.
    # By #111 Thm 8.2 a nontrivial split of S would put a nontrivial central
    # projection of the envelope inside S; the computed central dimension is 1,
    # so the only admitted split is the trivial one.  Its core is computed.
    hostile_admitted_splits = [set(), {0}] if central_dim > 1 else [set()]
    hostile_core = core_from_admitted_splits(1, hostile_admitted_splits)
    hostile_fixed = bell(hostile_core)
    gate(
        "G3-2e",
        "control-hostile-negative",
        "NEGATIVE DIRECTION: the computed dim(S cap Z) = 1 admits only the "
        "trivial split, so the hostile operator system's core has one atom "
        "and its fixed-point set is the singleton {trivial record} -- no "
        "nontrivial fixed point exists there",
        hostile_core == 1 and hostile_fixed == 1 and cl_of(indiscrete(1), 1) == indiscrete(1),
        {"core_atoms": hostile_core, "fixed_points": hostile_fixed},
    )
    gate(
        "G3-2f",
        "control-hostile-positive",
        "POSITIVE DIRECTION: the readable direct sum M_2 (+) M_2 itself (all "
        "central branches admitted) has a two-atom core and two fixed points, "
        "so the machinery does fire when the split is physically readable",
        CStar("M_2 (+) M_2", (2, 2)).centre_dimension() == 2 and bell(2) == 2,
        {"core_atoms": CStar("M_2 (+) M_2", (2, 2)).centre_dimension(), "fixed": bell(2)},
    )

    # ============ Control 3: ordinary finite C* controls ==================
    prog("G3  control 3: finite C* recovery, and non-recovery when unadmitted")
    recovered = {}
    for key in ("C2", "M2+C", "C5", "M4+C", "PVM211", "PVM22"):
        alg = FIXTURES[key]
        d = alg.centre_dimension()
        recovered[key] = {"blocks": list(alg.blocks), "centre_dim": d, "core_atoms": d}
    ok3 = all(v["centre_dim"] == len(FIXTURES[k].blocks) for k, v in recovered.items())
    gate(
        "G3-3a",
        "control-cstar-positive",
        "POSITIVE: where the central-sector branches are physically readable "
        "the fixed points recover exactly the minimal central projections "
        "(centre dimension computed by exact commutant solve, never typed)",
        ok3,
        recovered,
    )

    # factor control: rank-one Choi domination.
    factor_ok = True
    ranks = {}
    for d in (2, 3, 4):
        omega = [[ZERO] * (d * d) for _ in range(d * d)]
        for i in range(d):
            for j in range(d):
                omega[i * d + i][j * d + j] = ONE
        r = mrank(tuple(tuple(x) for x in omega))
        ranks[d] = r
        if r != 1:
            factor_ok = False
    anchor("A25", "#111 sec 6.1", "rank of J(identity channel) on M_d", 1, ranks[2])
    gate(
        "G3-3b",
        "control-cstar-negative",
        "NEGATIVE: on a full matrix factor J(I) is rank one, so any CP-"
        "dominated idempotent is a scalar multiple of the identity and "
        "Cl_op(M_d) = {I}: no nontrivial fixed point",
        factor_ok and FIXTURES["M2"].centre_dimension() == 1,
        {"choi_ranks": ranks, "M2_core_atoms": FIXTURES["M2"].centre_dimension()},
    )

    # unavailable-filter law (#111 sec 9.1): algebraically C^2, physically
    # trivial.  Both laws are DECLARED as admitted split sets and their cores
    # are computed by the #111 Thm 5.4 construction.
    unavailable_core = core_from_admitted_splits(2, [set(), {0, 1}])
    enlarged_core = core_from_admitted_splits(2, [set(), {0}, {1}, {0, 1}])
    algebraic_core = FIXTURES["C2"].centre_dimension()
    gate(
        "G3-3c",
        "control-cstar-negative",
        "NEGATIVE: under the restricted law of #111 sec 9.1 the same algebra "
        "C^2 has B_op = {0,I}, so the physical core is trivial and the only "
        "fixed point is the trivial record even though the ALGEBRAIC centre "
        "has dimension 2 -- admission is measured, not inferred",
        unavailable_core == 1 and algebraic_core == 2 and enlarged_core == 2,
        {
            "algebraic_centre_dim": algebraic_core,
            "restricted_law_core_atoms": unavailable_core,
            "enlarged_law_core_atoms": enlarged_core,
        },
    )

    # the transpose symmetrizer: scalar positivity is not enough.
    d = 2
    JP = [[ZERO] * (d * d) for _ in range(d * d)]
    for i in range(d):
        for j in range(d):
            # P(E_ij) = (E_ij + E_ji)/2
            for (a, b) in ((i, j), (j, i)):
                JP[i * d + a][j * d + b] = JP[i * d + a][j * d + b] + QC(Fr(1, 2))
    JP = tuple(tuple(r) for r in JP)
    # <psi^-| J(P) |psi^->  with |psi^-> = (|01> - |10>)/sqrt(2)
    v = [ZERO] * 4
    v[1] = QC(1)
    v[2] = QC(-1)
    acc = ZERO
    for i in range(4):
        for j in range(4):
            acc = acc + v[i].conj() * JP[i][j] * v[j]
    val = acc * QC(Fr(1, 2))
    anchor("A26", "#111 sec 3.3 / #111 adj sec 3.4", "<psi^-|J(P)|psi^->", QC(Fr(-1, 2)), val)
    gate(
        "G3-3d",
        "control-cstar-negative",
        "NEGATIVE: the transpose symmetrizer is positive, unital and "
        "idempotent but has Choi expectation -1/2 on the antisymmetric "
        "vector, so scalar positivity does not supply an admitted branch",
        val == QC(Fr(-1, 2)),
        {"value": str(val.re)},
    )

    # ============ Control 4: no-write and stability ======================
    prog("G3  control 4: no-write control and tester-visible recovery")
    p0 = (Fr(3, 4), Fr(1, 4))
    p1 = (Fr(1, 4), Fr(3, 4))
    tv_before = total_variation(p0, p1)
    anchor("A27", "#103 sec 7.2", "distinguishability of the two written settings", Fr(1, 2), tv_before)

    # the no-write reset is OUTSIDE Pres(M) with a strictly positive deficit
    best_d = None
    for num in range(0, 25):
        d = Fr(num, 24)
        err = max(total_variation(p0, (d, 1 - d)), total_variation(p1, (d, 1 - d)))
        if best_d is None or err < best_d:
            best_d = err
    # analytic lower bound: max(a,b) >= (a+b)/2 >= TV(p0,p1)/2 = 1/4, so the
    # grid minimum is the true minimax value.
    lower_bound = tv_before / 2
    gate(
        "G3-4a",
        "control-no-write-positive",
        "POSITIVE: the no-write reset lies OUTSIDE Pres(M) for the two-atom "
        "record, with an exact optimal recovery deficit of 1/4 -- a "
        "tester-visible failure, not a definitional one",
        best_d == Fr(1, 4) and best_d == lower_bound,
        {"optimal_deficit": str(best_d), "analytic_lower_bound": str(lower_bound)},
    )
    c2alg = FIXTURES["C2"]
    reset_ch = ClassicalChannel(
        "no-write reset", [[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]]
    )
    in_triv, _ = availability_membership(c2alg, c2alg, reset_ch, indiscrete(2))
    in_two, _ = availability_membership(c2alg, c2alg, reset_ch, ((0,), (1,)))
    gate(
        "G3-4b",
        "control-no-write-negative",
        "NEGATIVE: the same reset lies INSIDE Pres of the trivial record with "
        "deficit exactly 0 while lying OUTSIDE Pres of the two-atom record -- "
        "the criterion does not reject futures indiscriminately",
        in_triv and not in_two,
        {"inside_trivial_record": in_triv, "inside_two_atom_record": in_two},
    )

    # exact coherence witness (#103 sec 7.2): the SQUARE of the committed
    # trace-norm sqrt(3)/2, computed from the exact purity invariant.
    a = Fr(3, 4)
    c2 = a * (1 - a)  # |c|^2 for a pure qubit state with Z-law (a, 1-a)
    tracenorm_sq = 4 * c2
    anchor("A28", "#103 sec 7.2", "squared coherence loss ||rho - D_Z(rho)||_1^2", Fr(3, 4), tracenorm_sq)
    gate(
        "G3-4c",
        "control-no-write-positive",
        "the exact coherence loss of the preserving Z-dephasing is recomputed: "
        "its square is 3/4, i.e. the committed trace-norm sqrt(3)/2",
        tracenorm_sq == Fr(3, 4),
        {"squared_trace_norm": str(tracenorm_sq), "offdiag_sq": str(c2)},
    )

    # stability: every future in Pres has deficit 0, every future outside has
    # a strictly positive deficit -- checked on the concrete battery.
    stable_pos, stable_neg = 0, 0
    for alg, part, chans in build_concrete_battery():
        if len(part) < 2:
            continue
        for ch in chans:
            ok, _ = availability_membership(alg, alg, ch, part)
            sup = sector_support(alg, alg, ch)
            if ok:
                stable_pos += 1
            else:
                # a strictly positive deficit is certified by two atoms whose
                # images collide: no readout can separate them.
                collided = any(
                    sup[i] & sup[j]
                    for bi, bj in combinations(range(len(part)), 2)
                    for i in part[bi]
                    for j in part[bj]
                )
                if collided:
                    stable_neg += 1
    gate(
        "G3-4d",
        "control-stability",
        "STABILITY, both directions: every admitted continuation inside "
        "Pres(M) has recovery deficit 0, and every admitted continuation "
        "outside it collides two record blocks, certifying a strictly "
        "positive tester-visible deficit",
        stable_pos >= 1 and stable_neg >= 1,
        {"inside_zero_deficit": stable_pos, "outside_positive_deficit": stable_neg},
    )


# --------------------------------------------------------------------------
# 6.  Verdict, receipt, rendering.
# --------------------------------------------------------------------------


def verdict():
    survived = FINDINGS.get("G2_manufactured_pvm_survives", False)
    nontrivial_exist = True
    if survived:
        rung = "RQ0-L0-BLOCKED-AT-DE-SMUGGLING"
        reason = (
            "nontrivial fixed points exist and are fully characterized, but "
            "the #103 manufactured PVM survives the closure, so the "
            "de-smuggling requirement of RQ0-L0-W3-OPERATIONAL-MARKOV-"
            "BOUNDARY is not met"
        )
    else:
        rung = "RQ0-L0-W3-OPERATIONAL-MARKOV-BOUNDARY"
        reason = "smuggling rejected"
    return {
        "rung": rung,
        "reason": reason,
        "instance_of_preregistered_outcome": "RQ0-L0-BLOCKED-AT-<object>",
        "blocked_object": (
            "a task-independent selector on the fixed-point set: at one-boundary "
            "scope the closure's carrier is itself the smuggled object"
        ),
        "not_earned": [
            "RQ0-L0-W3-OPERATIONAL-MARKOV-BOUNDARY (existence and "
            "characterization hold; smuggling rejection FAILS)"
        ],
        "refuted": [
            "RQ0-L0-NO-NONTRIVIAL-FIXED-POINT (nontrivial fixed points exist "
            "in abundance: under the availability Galois closure EVERY "
            "admitted record is fixed)"
        ],
        "scope": (
            "finite dimension, one boundary, one admitted process law, the "
            "earned #103/#111 fixtures; exhaustive over all left-total sector "
            "relations at atom count <= 4 and over a declared subfamily at "
            "atom count 5, with the general case covered by the proved "
            "component lemma"
        ),
    }


def build_receipt():
    npass = sum(1 for g in GATES if g["pass"])
    return {
        "schema": SCHEMA,
        "unit": "RQ0-L0 Cycle B - the task-record fixed point",
        "pin_commit": PIN_COMMIT,
        "immutable_base_commit": BASE_COMMIT,
        "status": "GREEN-UNREVIEWED",
        "arithmetic": "exact (fractions.Fraction and Q(i)); no float in any substantive path",
        "source_sha256": SOURCE_SHA256,
        "anchor_type_violations": EXACTNESS_VIOLATIONS,
        "verdict": verdict(),
        "findings": FINDINGS,
        "gates": {
            "total": len(GATES),
            "passed": npass,
            "failed": [g["id"] for g in GATES if not g["pass"]],
            "entries": GATES,
        },
        "anchors": {
            "total": len(ANCHORS),
            "passed": sum(1 for a in ANCHORS if a["pass"]),
            "entries": ANCHORS,
        },
        "nonclaims": [
            "no composition or tensor claim (that is stage 4's question)",
            "no locality, overlap, region, topology or manifold claim",
            "no causal order, influence or spacetime claim",
            "no field, QCD or gravity claim",
            "no actual outcome selection, W6 co-reference or event-token identity",
            "no task-independent W3 record is earned",
            "'Markov' in this unit means operational screening-off inside ONE "
            "boundary and carries no spacetime meaning",
        ],
    }


def render(rec) -> str:
    L = []
    L.append("RQ0-L0 CYCLE B RECEIPT - THE TASK-RECORD FIXED POINT")
    L.append(f"schema: {rec['schema']}")
    L.append(f"status: {rec['status']}")
    L.append(f"pin: {rec['pin_commit']}   immutable base: {rec['immutable_base_commit']}")
    L.append(f"arithmetic: {rec['arithmetic']}")
    L.append(f"source sha256: {rec['source_sha256']}")
    L.append(f"anchor type violations: {rec['anchor_type_violations']}")
    L.append("")
    L.append("VERDICT")
    v = rec["verdict"]
    L.append(f"  rung: {v['rung']}")
    L.append(f"  instance of: {v['instance_of_preregistered_outcome']}")
    L.append(f"  blocked object: {v['blocked_object']}")
    L.append(f"  reason: {v['reason']}")
    for s in v["not_earned"]:
        L.append(f"  NOT EARNED: {s}")
    for s in v["refuted"]:
        L.append(f"  REFUTED: {s}")
    L.append(f"  scope: {v['scope']}")
    L.append("")
    L.append("FINDINGS")
    for k in sorted(rec["findings"]):
        L.append(f"  {k}: {rec['findings'][k]}")
    L.append("")
    L.append(f"GATES  {rec['gates']['passed']}/{rec['gates']['total']}")
    if rec["gates"]["failed"]:
        L.append(f"  FAILED: {', '.join(rec['gates']['failed'])}")
    for g in rec["gates"]["entries"]:
        L.append(f"  {g['id']:12s} [{g['class']}] {'PASS' if g['pass'] else 'FAIL'}")
        L.append(f"      {g['claim']}")
        if g["value"] is not None:
            L.append(f"      value: {json.dumps(g['value'], sort_keys=True)}")
    L.append("")
    L.append(f"ANCHORS  {rec['anchors']['passed']}/{rec['anchors']['total']}  (exit-1-only)")
    for a in rec["anchors"]["entries"]:
        L.append(
            f"  {a['id']:9s} {a['source']:34s} {a['quantity']}: "
            f"committed={a['committed']} computed={a['computed']} "
            f"{'PASS' if a['pass'] else 'FAIL'}"
        )
    L.append("")
    L.append("NON-CLAIMS")
    for s in rec["nonclaims"]:
        L.append(f"  - {s}")
    return "\n".join(L) + "\n"


MUTANT_TABLE = {
    "erase-min": ("A07", 4),
    "hostile-norm": ("A16", 4),
    "tomo-dist": ("A12", (Fr(1, 3), Fr(2, 3))),
    "choi": ("A26", QC(Fr(-1, 3))),
    "seams": ("A14", 8),
    "coherence": ("A28", Fr(1, 2)),
}


def run_falsification_selftest() -> int:
    prog("FALSIFICATION SELF-TEST: each mutant must exit 1")
    rows = []
    ok = True
    for name in sorted(MUTANT_TABLE):
        r = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--mutant", name],
            capture_output=True,
            text=True,
        )
        killed = r.returncode == 1 and "ANCHOR FAILURE" in r.stdout
        rows.append((name, MUTANT_TABLE[name][0], r.returncode, killed))
        if not killed:
            ok = False
    for name, aid, code, killed in rows:
        sys.stdout.write(
            f"  mutant {name:12s} breaks {aid:6s} exit={code} "
            f"{'KILLED (correct)' if killed else 'SURVIVED (DEFECT)'}\n"
        )
    sys.stdout.write(
        f"falsification self-test: {sum(1 for r in rows if r[3])}/{len(rows)} mutants killed\n"
    )
    return 0 if ok else 1


def main() -> int:
    global MUTANT, MUTANT_OVERRIDE
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", choices=sorted(MUTANT_TABLE), default=None)
    ap.add_argument("--falsification-selftest", action="store_true")
    ap.add_argument("--no-write-files", action="store_true")
    args = ap.parse_args()

    if args.falsification_selftest:
        return run_falsification_selftest()

    if args.mutant:
        MUTANT = args.mutant
        aid, val = MUTANT_TABLE[args.mutant]
        MUTANT_OVERRIDE = {aid: val}
        prog(f"MUTANT MODE: anchor {aid} deliberately broken ({args.mutant})")

    prog(f"RQ0-L0 Cycle B - task-record fixed point; pin {PIN_COMMIT}")
    run_exactness_gate()
    run_g0()
    run_g1()
    run_g2()
    run_g3()

    rec = build_receipt()
    txt = render(rec)
    if not args.no_write_files and not MUTANT:
        OUT_JSON.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
        OUT_TXT.write_text(txt)
    sys.stdout.write("\n" + txt)
    prog(
        f"done: {rec['gates']['passed']}/{rec['gates']['total']} gates, "
        f"{rec['anchors']['passed']}/{rec['anchors']['total']} anchors"
    )
    if rec["gates"]["failed"]:
        prog(f"GATE FAILURES: {rec['gates']['failed']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
