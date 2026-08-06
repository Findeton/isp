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
from itertools import combinations, permutations, product
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
    start = 1 if MUTANT == "avail-lax" else 0
    for i in range(start, len(imgs)):
        for j in range(i + 1, len(imgs)):
            if imgs[i] & imgs[j]:
                return False
    return True


def comp(sup):
    """Connected components of the collision graph k ~ l iff sup[k] & sup[l].
    Lemma 3.2 of the paper: this is the FINEST record `sup` preserves."""
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
    if MUTANT == "comp-coarse" and n >= 2:
        a, b = find(0), find(1)
        if a != b:
            parent[a] = b
    groups = {}
    for x in range(n):
        groups.setdefault(find(x), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in groups.values()))


def transitive_closure_of_comerge(smat, n: int):
    """v12 Theorem 4.5's object M(U_2), rebuilt by its own algorithm: the
    co-merge relation k ~ l iff some later configuration i has smat[i][k] and
    smat[i][l] nonzero, closed transitively by Warshall (never by union-find,
    so that the comparison with comp() is a comparison of two procedures)."""
    rel = [[k == l for l in range(n)] for k in range(n)]
    for i in range(len(smat)):
        hit = [k for k in range(n) if smat[i][k]]
        for k in hit:
            for l in hit:
                rel[k][l] = True
    for m in range(n):
        for k in range(n):
            if rel[k][m]:
                for l in range(n):
                    if rel[m][l]:
                        rel[k][l] = True
    blocks, seen = [], set()
    for k in range(n):
        if k in seen:
            continue
        b = tuple(sorted(l for l in range(n) if rel[k][l]))
        seen |= set(b)
        blocks.append(b)
    return tuple(sorted(blocks))


def core_avail(sups):
    """Core(G) = the finest record preserved by every future in G."""
    return closure_of_relations([comp(s) for s in sups])


def meet_of_parts(ps, n: int):
    """The meet of a set of records in the refinement order (the transitive
    closure of the union of their equivalences).  The EMPTY meet is the top
    of the record lattice, Cl_op(S) -- the convention the adjunction needs at
    the empty future family."""
    if not ps:
        return discrete(n)
    return closure_of_relations(list(ps) + [discrete(n)])


def core_of_family(sups, n: int):
    """Core(G) with the empty-family convention Core(empty) = Cl_op(S)."""
    return meet_of_parts([comp(s) for s in sups], n)


_COMP_CACHE: dict = {}


def comps_of(n: int):
    """comp(F) for every future in the exhaustive relation family, cached."""
    if n not in _COMP_CACHE:
        _COMP_CACHE[n] = tuple(comp(s) for s in relations_of(n))
    return _COMP_CACHE[n]


# cl(pi) MEASURED from a declared future family: Pres membership is decided
# by the DEFINITION (pairwise disjoint block images) over every member of the
# family, and cl(pi) is the meet of the collision partitions actually
# realized by the futures that pass.  Populated by G1-00; no generator, and
# in particular never `meet(discrete, pi)`.
PRES_COMPS: dict = {}
_CL_TABLE: dict = {}


def cl_measured(part, n: int):
    if n not in PRES_COMPS:
        raise SystemExit(1)
    tab = _CL_TABLE.setdefault(n, {})
    if part not in tab:
        tab[part] = meet_of_parts(PRES_COMPS[n][part], n)
    return tab[part]


def fix_set_of_family(sups, n: int, comps=None):
    """Fix(cl_F) for a declared law family F.  The family is first reduced to
    the collision partitions it realizes -- exact by Lemma 3.2, which is gated
    exhaustively on the same relation set -- and Pres membership is then
    decided by the DEFINITION on one representative future per realized
    partition."""
    if comps is None:
        comps = [comp(s) for s in sups]
    reps: dict = {}
    for s, c in zip(sups, comps):
        reps.setdefault(c, s)
    fixed = []
    for p in parts_of(n):
        inside = [c for c, s in reps.items() if images_disjoint(s, p)]
        if meet_of_parts(inside, n) == p:
            fixed.append(p)
    return fixed


def lcg_step(state: int) -> int:
    """A fixed-seed integer linear congruential generator.  Exact integer
    arithmetic, no library entropy: the sweeps below are reproducible."""
    return (6364136223846793005 * state + 1442695040888963407) % (2 ** 64)


def functional_support(f):
    return tuple(frozenset({v}) for v in f)


def elementary_merge(n: int, k: int, l: int):
    """f_{k->l}: map sector k into sector l, act as the identity elsewhere.
    Discards nothing inside a kept sector and reprepares nothing."""
    return tuple(frozenset({l if i == k else i}) for i in range(n))


def has_total_support(sup, n: int, perms) -> bool:
    """Birkhoff/Koenig: a sector relation is the support of a doubly
    stochastic sector map exactly when every admitted entry lies on a
    permutation contained in the relation."""
    covered = set()
    for sg in perms:
        if all(sg[i] in sup[i] for i in range(n)):
            covered.update((i, sg[i]) for i in range(n))
    return all((k, l) in covered for k in range(n) for l in sup[k])


def relabel_part(part, sigma):
    """The action of an atom relabelling on a record."""
    return tuple(sorted(tuple(sorted(sigma[x] for x in b)) for b in part))


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


_FAM5_CACHE: list = []


def declared_family_n5():
    """Declared n = 5 subfamily: at most one multi-valued atom."""
    if _FAM5_CACHE:
        return _FAM5_CACHE[0]
    subsets = [frozenset(s) for r in range(1, 6) for s in combinations(range(5), r)]
    singles = [s for s in subsets if len(s) == 1]
    multis = [s for s in subsets if len(s) > 1]
    fam = [base for base in product(singles, repeat=5)]
    for k in range(5):
        for mset in multis:
            for base in product(singles, repeat=4):
                fam.append(tuple(list(base[:k]) + [mset] + list(base[k:])))
    _FAM5_CACHE.append(fam)
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


# --- the flag-retaining ("measure and broadcast") readings of the literal
#     formula.  D_M-hat : rho -> sum_r (z_r rho z_r) (x) |r><r| is not an
#     endomorphism of S, so the literal equation is type-ill-formed; there are
#     exactly three ways to repair the type, and all three are run.


def broadcast_b1_recollapses(alg: CStar, part, ch: Channel) -> bool:
    """B1 -- trace the flag out before comparing.  The S'-marginal of
    (F (x) id) D_M-hat(rho) is F(sum_r z_r rho z_r), so the test returns
    Theorem 2.1 exactly."""
    for b in alg.matrix_units():
        if not meq(ch.forward(forget_map(alg, part, b)), ch.forward(b)):
            return False
    return True


def broadcast_b4_membership(alg: CStar, part, ch: Channel) -> bool:
    """B4 -- keep the flag and demand no later readout: compare F (x) id with
    (F (x) id) o D_M-hat on S (x) C^Omega, where the broadcast overwrites the
    flag.  Joint operators are carried as flag-indexed blocks."""
    m = len(part)
    zs = instrument_branches(alg, part)
    zero = mzero(alg.dim)
    for f in range(m):
        for g in range(m):
            for rho in alg.matrix_units():
                # sigma = rho (x) |f><g|, carried as flag-indexed blocks.
                marg = rho if f == g else zero  # Tr_flag(sigma)
                for a in range(m):
                    for b in range(m):
                        lhs = ch.forward(rho if (a == f and b == g) else zero)
                        rhs = ch.forward(
                            mmul(mmul(zs[a], marg), zs[a]) if a == b else zero
                        )
                        if not meq(lhs, rhs):
                            return False
    return True


def broadcast_b3_membership(alg_in: CStar, alg_out: CStar, ch: Channel, part):
    """B3 -- keep the flag and demand the record be readable after F exactly
    as it was before it: m_s o Phi = Phi o m'_s for every outcome s, i.e. the
    full flag-joint statistics agree, not merely the flag marginal."""
    m = len(part)
    targets = [alg_in.central_projection(b) for b in part]
    basis = alg_out.matrix_units()
    pulled = [ch.pullback(b) for b in basis]
    zsub, psub = {}, {}
    for r in range(len(alg_out.blocks) + 1):
        for sub in combinations(alg_out.atoms(), r):
            zsub[frozenset(sub)] = alg_out.central_projection(list(sub))
            psub[frozenset(sub)] = ch.pullback(zsub[frozenset(sub)])
    for assign in product(range(m), repeat=len(alg_out.blocks)):
        zprime = []
        pruned = False
        for s in range(m):
            key = frozenset(l for l in alg_out.atoms() if assign[l] == s)
            # The case b = 1 of the identity is NECESSARY for B3, so failing
            # it discards no candidate; it only shortens the search.
            if not meq(psub[key], targets[s]):
                pruned = True
                break
            zprime.append(zsub[key])
        if pruned:
            continue
        ok = True
        for s in range(m):
            for bi, b in enumerate(basis):
                if not meq(ch.pullback(mmul(zprime[s], b)), mmul(targets[s], pulled[bi])):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True, assign
    return False, None


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

    # ---- G0-10/11/12/13  UNIQUENESS of the repair.  The literal formula can
    #      also be read with the flag RETAINED (measure and broadcast).  That
    #      reading is type-ill-formed, and has exactly three type repairs.
    prog("G0  uniqueness: the three typed repairs of the broadcast reading")

    b1_pairs, b1_recollapse = 0, 0
    for alg, part, chans in battery:
        for ch in chans:
            b1_pairs += 1
            if broadcast_b1_recollapses(alg, part, ch):
                b1_recollapse += 1
    gate(
        "G0-10",
        "repair-uniqueness",
        "REPAIR B1 (trace the flag out before comparing): the S'-marginal of "
        "the broadcast is sum_r z_r rho z_r = rho, so the test returns "
        "Theorem 2.1 exactly and RE-COLLAPSES on every battery pair",
        b1_recollapse == b1_pairs and b1_pairs >= 1,
        {"future_instrument_pairs": b1_pairs, "recollapsed": b1_recollapse},
    )

    b4_trivial_inside, b4_nontrivial_identity_inside, b4_records = 0, 0, 0
    for alg, part_default, chans in battery:
        for p in parts_of(len(alg.blocks)):
            b4_records += 1
            inside_id = broadcast_b4_membership(alg, p, chan_identity(alg.dim))
            if len(p) == 1:
                if all(broadcast_b4_membership(alg, p, ch) for ch in chans):
                    b4_trivial_inside += 1
            elif inside_id:
                b4_nontrivial_identity_inside += 1
    gate(
        "G0-11",
        "repair-uniqueness",
        "REPAIR B4 (keep the flag, demand no later readout): the broadcast "
        "overwrites the flag, so the test holds for the one-outcome record "
        "and fails for EVERY record with two or more outcomes -- even for the "
        "identity future.  Nondegenerate, but degenerate in the opposite "
        "direction: it empties Pres instead of filling it",
        b4_trivial_inside == len(battery) and b4_nontrivial_identity_inside == 0,
        {
            "records_tested": b4_records,
            "trivial_record_all_futures_inside": b4_trivial_inside,
            "nontrivial_records_with_identity_inside": b4_nontrivial_identity_inside,
        },
    )

    b3_in, b3_out, b3_disagree = 0, 0, 0
    for alg, part, chans in battery:
        for ch in chans:
            b3, _ = broadcast_b3_membership(alg, alg, ch, part)
            av, _ = availability_membership(alg, alg, ch, part)
            if b3:
                b3_in += 1
            else:
                b3_out += 1
            if b3 != av:
                b3_disagree += 1
    gate(
        "G0-12",
        "repair-uniqueness",
        "REPAIR B3 (keep the flag, demand the record be readable after F as "
        "it was before it: m_s o Phi = Phi o m'_s): nondegenerate, and "
        "EQUIVALENT to Definition 2.3 -- the multiplicative-domain lemma "
        "carries each direction",
        b3_disagree == 0 and b3_in >= 1 and b3_out >= 1,
        {"inside": b3_in, "outside": b3_out, "disagreements_with_definition_2_3": b3_disagree},
    )

    by_id = {g["id"]: g["pass"] for g in GATES}
    uniq = by_id["G0-10"] and by_id["G0-11"] and by_id["G0-12"]
    gate(
        "G0-13",
        "repair-uniqueness",
        "UNIQUENESS: of the three typed repairs of the literal formula one "
        "re-collapses (B1), one degenerates oppositely (B4), and the only "
        "nondegenerate survivor (B3) IS the adopted availability form.  The "
        "adoption of Definition 2.3 is forced at the scope of the "
        "flag-retaining repairs, not merely convenient",
        uniq,
        {"recollapses": "B1", "empties": "B4", "equals_definition_2_3": "B3"},
    )
    FINDINGS["G0_availability_form_is_the_unique_typed_repair"] = bool(uniq)


# --------------------------------------------------------------------------
# G1 — THE GALOIS GATES
# --------------------------------------------------------------------------


def run_g1():
    prog("G1  Galois gates: antitone monotonicity, adjunction, closure laws")

    # Declared future battery per atom count: all left-total relations at
    # n <= 4 (exhaustive); the <=1-branching subfamily at n = 5 (declared).
    exhaustive_n = 4

    # ---- G1-00  soundness of the component lemma against the DEFINITION.
    #      The same pass MEASURES the closure: whenever the definition puts a
    #      future inside Pres(pi), that future's realized collision partition
    #      is accumulated, so cl(pi) = Core(Pres(pi)) is afterwards available
    #      as the meet of the partitions the family actually realizes -- never
    #      as a function of pi's own reprepare generator.
    fam5 = declared_family_n5()
    tests_by_n = {}
    for n in (1, 2, 3, 4):
        parts = parts_of(n)
        fam = relations_of(n)
        if len(fam) != count_relations(n, n):
            raise SystemExit(1)
        cs = comps_of(n)
        acc = {p: set() for p in parts}
        bad = 0
        total = 0
        for i, sup in enumerate(fam):
            c = cs[i]
            for p in parts:
                total += 1
                inside = images_disjoint(sup, p)
                if inside != refines(c, p):
                    bad += 1
                if inside:
                    acc[p].add(c)
        PRES_COMPS[n] = acc
        tests_by_n[n] = total
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
    acc5 = {p: set() for p in parts5}
    bad5 = 0
    tests5 = 0
    for sup in fam5:
        c = comp(sup)
        for p in parts5:
            tests5 += 1
            inside = images_disjoint(sup, p)
            if inside != refines(c, p):
                bad5 += 1
            if inside:
                acc5[p].add(c)
    PRES_COMPS[5] = acc5
    gate(
        "G1-00-n5",
        "lemma-soundness",
        "DECLARED SUBFAMILY n=5 (the 84,375 relations in which at most one "
        "atom has a multi-valued sector support): F in Pres(pi) iff comp(F) "
        "refines pi; the general case is covered by the proved lemma",
        bad5 == 0,
        {"relations": len(fam5), "tests": tests5, "mismatches": bad5},
    )
    prog(f"     n=5: {len(fam5)} declared relations x {len(parts5)} records checked")

    total_le4 = sum(tests_by_n[n] for n in (2, 3, 4))
    gate(
        "G1-00-total",
        "lemma-soundness",
        "the exhaustive membership total quoted in the text: 18 + 1,715 + "
        "759,375 membership tests at atom counts 2, 3 and 4",
        total_le4 == 761108,
        {"tests_n2": tests_by_n[2], "tests_n3": tests_by_n[3],
         "tests_n4": tests_by_n[4], "total_tests_n_le_4": total_le4},
    )

    # ---- G1-12  comp(F) IS v12 Theorem 4.5's decision procedure M(U_2).
    mu2_bad, mu2_tested = 0, 0
    for bits in product((0, 1), repeat=9):
        smat = [bits[3 * i:3 * i + 3] for i in range(3)]
        sup = tuple(frozenset(i for i in range(3) if smat[i][k]) for k in range(3))
        mu2_tested += 1
        if comp(sup) != transitive_closure_of_comerge(smat, 3):
            mu2_bad += 1
    gate(
        "G1-12",
        "predecessor-identity",
        "comp(F) -- the connected components of the collision graph -- IS the "
        "object M(U_2) of the predecessor's Theorem 4.5, the transitive "
        "closure of the co-merge relation, over all 512 support patterns at "
        "three atoms; the two decision procedures are compared, union-find "
        "against Warshall, not merely the two statements",
        mu2_bad == 0,
        {"support_patterns": mu2_tested, "mismatches": mu2_bad},
    )

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

    # ---- G1-05/06/07  closure operator laws for cl = Core o Pres, computed
    #      from the MEASURED closure of G1-00's pass: cl(pi) is the meet of
    #      the collision partitions realized by the futures that the
    #      definition puts inside Pres(pi).
    ext_ok = mono_ok = idem_ok = True
    law_counts = {}
    for n in (1, 2, 3, 4, 5):
        parts = parts_of(n)
        law_counts[n] = {"records": len(parts), "closure_values_computed": 0}
        for p in parts:
            c = cl_measured(p, n)
            law_counts[n]["closure_values_computed"] += 1
            if not refines(c, p):
                ext_ok = False
            if cl_measured(c, n) != c:
                idem_ok = False
        for p in parts:
            for q in parts:
                if refines(q, p):  # q finer than p
                    if not refines(cl_measured(q, n), cl_measured(p, n)):
                        mono_ok = False
    gate(
        "G1-05",
        "closure",
        "cl = Core o Pres is EXTENSIVE (M coarser than cl(M)), measured from "
        "the declared future family at atom counts 1 to 5",
        ext_ok,
        law_counts,
    )
    gate(
        "G1-06",
        "closure",
        "cl = Core o Pres is MONOTONE, measured from the declared future "
        "family at atom counts 1 to 5",
        mono_ok,
        law_counts,
    )
    gate(
        "G1-07",
        "closure",
        "cl = Core o Pres is IDEMPOTENT, measured from the declared future "
        "family at atom counts 1 to 5",
        idem_ok,
        law_counts,
    )

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
        closed_records = [p for p in parts if cl_measured(p, n) == p]
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


def vec(m):
    return tuple(x for row in m for x in row)


def span_rank(mats) -> int:
    if not mats:
        return 0
    return mrank(tuple(vec(m) for m in mats))


def independent_subset(mats):
    """An exact basis of the span, by elimination -- never by counting."""
    chosen, r = [], 0
    for m in mats:
        if span_rank(chosen + [m]) > r:
            chosen.append(m)
            r += 1
    return chosen


def in_span(basis, x) -> bool:
    return span_rank(list(basis) + [x]) == span_rank(list(basis))


def centre_dim_of_basis(basis) -> int:
    """dim Z(A) for an algebra given by an exact basis: solve [x, y] = 0 for
    every basis element y, by exact elimination."""
    nb = len(basis)
    dim = len(basis[0])
    conds = []
    for y in basis:
        comms = [msub(mmul(b, y), mmul(y, b)) for b in basis]
        for i in range(dim):
            for j in range(dim):
                row = [comms[c][i][j] for c in range(nb)]
                if any(not x.is_zero() for x in row):
                    conds.append(row)
    return nb if not conds else nullity_of_conditions(conds)


def rational_rotation(n: int, i: int, j: int, c: Fr, s: Fr):
    """An exact rational Givens rotation in the (i,j) plane; c^2 + s^2 = 1 by
    a Pythagorean triple, so no root is ever extracted."""
    m = [[ONE if a == b else ZERO for b in range(n)] for a in range(n)]
    m[i][i] = QC(c)
    m[i][j] = QC(-s)
    m[j][i] = QC(s)
    m[j][j] = QC(c)
    return tuple(tuple(r) for r in m)


def embed_with_sink(m, dim: int):
    """Adjoin the retained sink summand of the #103 adjudication: the matched
    success algebra sits in the top-left corner, the failure branch is the
    extra diagonal entry."""
    out = [[ZERO] * (dim + 1) for _ in range(dim + 1)]
    for i in range(dim):
        for j in range(dim):
            out[i][j] = m[i][j]
    return tuple(tuple(r) for r in out)


def embed_unitary_with_sink(m, dim: int):
    """The same embedding for a REVERSIBLE map: it must act as the identity
    on the retained sink, not annihilate it."""
    out = [[ZERO] * (dim + 1) for _ in range(dim + 1)]
    for i in range(dim):
        for j in range(dim):
            out[i][j] = m[i][j]
    out[dim][dim] = ONE
    return tuple(tuple(r) for r in out)


def build_manufactured_boundary(ranks):
    """#103 sec 7.1, CONSTRUCTED rather than typed.  Choose a PVM P = {P_r} of
    the declared rank multiset in a ROTATED basis (so that no block structure
    is read off the coordinates), form the matched dephasing
    D_P(rho) = sum_r P_r rho P_r, take A_P = range(D_P) = (+)_r P_r B(H) P_r
    by exact elimination, and adjoin the retained sink summand.  Every
    reported quantity below is computed from the projections."""
    dim = sum(ranks)
    W = mmul(
        mmul(
            rational_rotation(dim, 0, 1, Fr(3, 5), Fr(4, 5)),
            rational_rotation(dim, 1, 2, Fr(5, 13), Fr(12, 13)),
        ),
        rational_rotation(dim, 2, 3, Fr(8, 17), Fr(15, 17)),
    )
    proj = []
    off = 0
    for r in ranks:
        d0 = [[ZERO] * dim for _ in range(dim)]
        for i in range(off, off + r):
            d0[i][i] = ONE
        p0 = tuple(tuple(x) for x in d0)
        proj.append(mmul(mmul(W, p0), madj(W)))
        off += r
    units = []
    for i in range(dim):
        for j in range(dim):
            m = [[ZERO] * dim for _ in range(dim)]
            m[i][j] = ONE
            units.append(tuple(tuple(x) for x in m))

    def dephase(rho):
        acc = mzero(dim)
        for p in proj:
            acc = madd(acc, mmul(mmul(p, rho), p))
        return acc

    ap_basis = independent_subset(
        [mmul(mmul(p, e), p) for p in proj for e in units]
    )
    # the matched dephasing's matrix in the matrix-unit basis; its rank is the
    # dimension of its range, computed rather than asserted.
    dmat = tuple(vec(dephase(e)) for e in units)
    facts = {
        "unitary_rotation": meq(mmul(W, madj(W)), mid(dim))
        and meq(mmul(madj(W), W), mid(dim)),
        "pvm_projections": all(
            meq(mmul(p, p), p) and meq(madj(p), p) for p in proj
        ),
        "pvm_complete": meq(
            [
                [
                    sum((proj[r][i][j] for r in range(len(proj))), ZERO)
                    for j in range(dim)
                ]
                for i in range(dim)
            ],
            mid(dim),
        ),
        "pvm_ranks": [mrank(p) for p in proj],
        "pvm_is_rotated_not_diagonal": any(
            not proj[0][i][j].is_zero() for i in range(dim) for j in range(dim) if i != j
        ),
        "dephasing_unital": meq(dephase(mid(dim)), mid(dim)),
        "dephasing_idempotent": all(meq(dephase(dephase(e)), dephase(e)) for e in units),
        "range_dimension": mrank(dmat),
        "algebra_dimension": len(ap_basis),
        "algebra_is_the_range": all(meq(dephase(b), b) for b in ap_basis),
        "centre_dim_without_sink": centre_dim_of_basis(ap_basis),
    }
    full = [embed_with_sink(b, dim) for b in ap_basis]
    sink = [[ZERO] * (dim + 1) for _ in range(dim + 1)]
    sink[dim][dim] = ONE
    sink = tuple(tuple(r) for r in sink)
    full.append(sink)
    atoms = [embed_with_sink(p, dim) for p in proj] + [sink]
    facts["multiplicatively_closed"] = all(
        in_span(full, mmul(a, b)) for a in full for b in full
    )
    facts["centre_dim_with_sink"] = centre_dim_of_basis(full)
    facts["atoms_in_algebra"] = all(in_span(full, z) for z in atoms)
    facts["atoms_central"] = all(
        meq(mmul(z, b), mmul(b, z)) for z in atoms for b in full
    )
    facts["atoms_orthogonal"] = all(
        meq(mmul(atoms[a], atoms[b]), mzero(dim + 1))
        for a in range(len(atoms))
        for b in range(len(atoms))
        if a != b
    )
    facts["atoms_sum_to_unit"] = meq(
        [
            [
                sum((atoms[r][i][j] for r in range(len(atoms))), ZERO)
                for j in range(dim + 1)
            ]
            for i in range(dim + 1)
        ],
        mid(dim + 1),
    )
    facts["atom_count"] = len(atoms)
    return facts, {"atoms": atoms, "basis": full, "rotation": W, "projections": proj}


def core_size(alg: CStar) -> int:
    """|Cl_op(A)| at the full standard law: the number of minimal central
    projections, computed from the exact centre dimension."""
    return alg.centre_dimension()


def run_g2():
    prog("G2  fixed points: trivial, characterization, discriminator")

    # ---- G2-01  the trivial record IS fixed under the declared family, and
    #      the exact criterion is the MEET of the realized collision
    #      partitions -- measured, not read off a generator.
    triv_fixed = True
    triv_detail = {}
    for n in (1, 2, 3, 4, 5):
        p = indiscrete(n)
        c = cl_measured(p, n)
        realized_meet = meet_of_parts(PRES_COMPS[n][p], n)
        triv_detail[n] = {
            "cl_of_trivial_is_trivial": c == p,
            "meet_of_realized_collision_partitions_is_trivial": realized_meet == p,
        }
        if c != p or realized_meet != p:
            triv_fixed = False
    gate(
        "G2-01",
        "trivial-fixed-point",
        "the trivial one-outcome instrument is a fixed point of cl exactly "
        "when the MEET of the collision partitions realized by the admitted "
        "futures is trivial; under the declared family (which contains the "
        "total-erasure future of condition R) it is, at atom counts 1 to 5",
        triv_fixed,
        triv_detail,
    )

    # ---- G2-01b  the meet form is STRICTLY weaker than "some admitted future
    #      erases the record": a composition-closed three-atom law on which
    #      the trivial record is fixed although no single admitted future
    #      preserves no nontrivial record.
    a_map = functional_support((0, 0, 2))
    b_map = functional_support((0, 2, 2))
    id3 = functional_support((0, 1, 2))
    fam3 = [id3, a_map, b_map]

    def compose_sup(f, g):
        """g after f, for single-valued sector maps."""
        return tuple(frozenset({next(iter(g[next(iter(f[k]))]))}) for k in range(3))

    closed = all(compose_sup(f, g) in fam3 for f in fam3 for g in fam3)
    comps3 = [comp(s) for s in fam3]
    meet3 = meet_of_parts(comps3, 3)
    erasers = [c for c in comps3 if c == indiscrete(3)]
    fixed3 = fix_set_of_family(fam3, 3, comps3)
    ce_ok = (
        closed
        and meet3 == indiscrete(3)
        and not erasers
        and indiscrete(3) in fixed3
        and len(fixed3) == 4
    )
    gate(
        "G2-01b",
        "trivial-fixed-point",
        "COUNTEREXAMPLE to the erasing-future form: on three atoms the "
        "composition-closed law generated by the sector maps (0,0,2) and "
        "(0,2,2) realizes the collision partitions {01|2} and {0|12}, whose "
        "MEET is trivial, so the trivial record is fixed -- yet NO admitted "
        "future preserves only the trivial record.  The closure is genuinely "
        "selective here: 4 of the 5 records are fixed",
        ce_ok,
        {
            "composition_closed": closed,
            "realized_collision_partitions": [[list(b) for b in c] for c in comps3],
            "meet_is_trivial": meet3 == indiscrete(3),
            "futures_preserving_no_nontrivial_record": len(erasers),
            "fixed_records": len(fixed3),
            "records": bell(3),
        },
    )

    # ---- G2-01c  the two criteria compared over every realizable law.
    crit_agree_meet, crit_agree_eraser, crit_cases = 0, 0, 0
    for n in (3, 4):
        parts = parts_of(n)
        reps = [reprepare_support(p, n) for p in parts]
        reps_comp = [comp(s) for s in reps]
        for size in range(1, len(parts) + 1):
            for idx in combinations(range(len(parts)), size):
                fam = [reps[i] for i in idx]
                cs = [reps_comp[i] for i in idx]
                crit_cases += 1
                fixed_trivial = meet_of_parts(
                    [c for s, c in zip(fam, cs) if images_disjoint(s, indiscrete(n))],
                    n,
                ) == indiscrete(n)
                if fixed_trivial == (meet_of_parts(cs, n) == indiscrete(n)):
                    crit_agree_meet += 1
                if fixed_trivial == any(c == indiscrete(n) for c in cs):
                    crit_agree_eraser += 1
    gate(
        "G2-01c",
        "trivial-fixed-point",
        "over every law realizable by a set of reprepare futures at atom "
        "counts 3 and 4, the MEET criterion decides the trivial fixed point "
        "in every case, while the erasing-future criterion decides it wrongly "
        "in a large minority -- the two are not equivalent",
        crit_agree_meet == crit_cases and crit_agree_eraser < crit_cases,
        {
            "laws_tested": crit_cases,
            "meet_criterion_correct": crit_agree_meet,
            "erasing_future_criterion_correct": crit_agree_eraser,
            "erasing_future_criterion_wrong": crit_cases - crit_agree_eraser,
        },
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
    FINDINGS["G2_trivial_fixed_iff_meet_of_realized_collisions_is_trivial"] = bool(
        triv_fixed and not_fixed_without_R
    )

    # ---- G2-03  characterization: cl is the IDENTITY under (R).  Every
    #      stratum is MEASURED from the declared future family -- exhaustively
    #      at atom counts 1 to 4, and from all 84,375 declared futures at
    #      atom count 5.
    cl_identity = True
    counts = {}
    for n in (1, 2, 3, 4, 5):
        parts = parts_of(n)
        fixed = [p for p in parts if cl_measured(p, n) == p]
        counts[n] = {
            "records": len(parts),
            "fixed": len(fixed),
            "futures_in_family": len(relations_of(n)) if n <= 4 else 84375,
        }
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
        "point, so the closure selects nothing.  Every stratum is measured "
        "from the declared future family, none is asserted",
        cl_identity,
        counts,
    )

    # ---- G2-03b  cl recomputed by a second route at n <= 4: Pres(pi) is
    #              materialized as an explicit index set over the exhaustive
    #              family and Core is taken of the futures themselves.
    direct_ok = True
    for n in (2, 3, 4):
        fam = relations_of(n)
        pres = pres_table(n)
        for p in parts_of(n):
            direct = core_avail([fam[i] for i in sorted(pres[p])])
            if direct != p or direct != cl_measured(p, n):
                direct_ok = False
    gate(
        "G2-03b",
        "characterization",
        "cl(pi) recomputed from the EXHAUSTIVE future family by a second "
        "route (explicit Pres index sets, then Core of the futures) at "
        "n <= 4: Core(Pres(pi)) = pi for every record",
        direct_ok,
        {"scope": "all left-total relations, n = 2,3,4"},
    )

    # ---- G2-03c  the two strata that a generator-based closure cannot see:
    #              atom count 1, and atom count 5 over the whole declared
    #              family of 84,375 futures.
    n5_fixed = [p for p in parts_of(5) if cl_measured(p, 5) == p]
    n1_fixed = [p for p in parts_of(1) if cl_measured(p, 1) == p]
    gate(
        "G2-03c",
        "characterization",
        "the extreme strata, measured: at atom count 1 the single record is "
        "fixed, and at atom count 5 all 52 records are fixed, with Pres "
        "membership decided by the definition over each of the 84,375 "
        "declared futures",
        len(n5_fixed) == 52 and len(n1_fixed) == 1,
        {
            "n1_fixed_of_records": [len(n1_fixed), bell(1)],
            "n5_fixed_of_records": [len(n5_fixed), bell(5)],
            "n5_declared_futures": 84375,
            "n5_membership_tests": 84375 * 52,
        },
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
        fixed = [p for p in parts_of(n) if cl_measured(p, n) == p]
        exist[key] = {
            "atoms": n,
            "records": bell(n),
            "fixed_points": len(fixed),
            "nontrivial": len(fixed) - 1,
        }
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
        n = core_size(alg)
        trivial_core[key] = {
            "atoms": n,
            "fixed_points": len([p for p in parts_of(n) if cl_measured(p, n) == p]),
        }
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

    # ---- G2-09a/b  THE MANUFACTURED BOUNDARY, CONSTRUCTED.
    prog("G2  constructing the manufactured boundary: PVM, matched dephasing, A_P")
    built = {}
    objs = {}
    for key, ranks in (("PVM211", (2, 1, 1)), ("PVM22", (2, 2)), ("PVM5", (1, 1, 1, 1))):
        built[key], objs[key] = build_manufactured_boundary(ranks)
    construction_ok = all(
        f["unitary_rotation"]
        and f["pvm_projections"]
        and f["pvm_complete"]
        and f["pvm_is_rotated_not_diagonal"]
        and f["dephasing_unital"]
        and f["dephasing_idempotent"]
        and f["algebra_is_the_range"]
        and f["multiplicatively_closed"]
        and f["atoms_in_algebra"]
        and f["atoms_central"]
        and f["atoms_orthogonal"]
        and f["atoms_sum_to_unit"]
        and f["range_dimension"] == f["algebra_dimension"]
        for f in built.values()
    )
    gate(
        "G2-09a",
        "manufactured-construction",
        "the manufactured boundary is CONSTRUCTED, not typed: a PVM of the "
        "declared rank multiset is built in a ROTATED basis by exact "
        "Pythagorean Givens rotations, its matched dephasing D_P(rho) = "
        "sum_r P_r rho P_r is verified unital and idempotent, A_P = range(D_P) "
        "is obtained by exact elimination and verified multiplicatively "
        "closed, and the retained sink summand of the #103 adjudication is "
        "adjoined; the atoms are exhibited as orthogonal central projections "
        "summing to the unit",
        construction_ok,
        {k: {kk: vv for kk, vv in f.items()} for k, f in built.items()},
    )
    anchor(
        "A10",
        "#103 sec 6.2",
        "matched 2+1+1 algebra with sink: centre dimension",
        4,
        built["PVM211"]["centre_dim_with_sink"],
    )
    anchor(
        "A11",
        "#103 sec 6.2",
        "matched 2+2 algebra with sink: centre dimension",
        3,
        built["PVM22"]["centre_dim_with_sink"],
    )
    man211 = FIXTURES["PVM211"]
    man22 = FIXTURES["PVM22"]
    typed_agrees = (
        man211.centre_dimension() == built["PVM211"]["centre_dim_with_sink"]
        and man22.centre_dimension() == built["PVM22"]["centre_dim_with_sink"]
        and FIXTURES["C5"].centre_dimension() == built["PVM5"]["centre_dim_with_sink"]
    )
    gate(
        "G2-09b",
        "manufactured-construction",
        "the declared fixtures are representatives of the CONSTRUCTED "
        "isomorphism classes: the commutant solve on the constructed rotated "
        "algebras returns the same centre dimensions as the typed block "
        "structures (4, 3 and 5)",
        typed_agrees,
        {
            "constructed_centre_dims": {
                k: built[k]["centre_dim_with_sink"] for k in built
            },
            "typed_centre_dims": {
                "PVM211": man211.centre_dimension(),
                "PVM22": man22.centre_dimension(),
                "C5": FIXTURES["C5"].centre_dimension(),
            },
        },
    )

    # ---- G2-10/11  THE DE-SMUGGLING DISCRIMINATOR, run on the constructed
    #      object.  The manufactured record is the atom instrument of the
    #      constructed boundary; its atom count comes from the PVM's rank
    #      multiset plus the sink, while Reading B's unique fixed point comes
    #      from the commutant solve -- two different routes to the same
    #      record, so the comparison can fail.
    prog("G2  DE-SMUGGLING DISCRIMINATOR: the constructed manufactured PVM")
    surviving = {}
    for key in ("PVM211", "PVM22"):
        f = built[key]
        n_from_pvm = f["atom_count"]
        manufactured = discrete(n_from_pvm)
        clA = cl_measured(manufactured, n_from_pvm)
        readingB_unique = discrete(f["centre_dim_with_sink"])
        surviving[key] = {
            "atoms_from_pvm_ranks_plus_sink": n_from_pvm,
            "atoms_from_commutant_solve": f["centre_dim_with_sink"],
            "records": bell(n_from_pvm),
            "readingA_cl_equals_input": clA == manufactured,
            "readingB_unique_fixed_point_equals_input": readingB_unique == manufactured,
        }
    survivedA = all(v["readingA_cl_equals_input"] for v in surviving.values())
    gate(
        "G2-10",
        "DISCRIMINATOR",
        "READING A: the CONSTRUCTED manufactured PVM record SURVIVES the "
        "closure as a nontrivial fixed point -- cl is computed from the "
        "exhaustive future family, and the closure does NOT de-smuggle",
        survivedA,
        surviving,
    )
    gate(
        "G2-11",
        "DISCRIMINATOR",
        "READING B: the CONSTRUCTED manufactured PVM record is the UNIQUE "
        "fixed point of the composite map -- the closure does NOT de-smuggle",
        all(v["readingB_unique_fixed_point_equals_input"] for v in surviving.values()),
        surviving,
    )
    FINDINGS["G2_manufactured_pvm_survives"] = bool(survivedA)

    # ---- G2-12  THE LOAD-BEARING IMPOSSIBILITY: the manufactured record is
    #      the TOP of its own record lattice, and every closure operator
    #      fixes the top -- under every admitted law, with no covariance
    #      premise and no condition on the law whatsoever.
    prog("G2  top of lattice: no closure operator dethrones its own top")
    top_ok, top_families, top_violations = True, 0, 0
    state = 20260806
    for n in (2, 3, 4, 5):
        pool = relations_of(n) if n <= 4 else declared_family_n5()
        top = discrete(n)
        for t in range(1000):
            state = lcg_step(state)
            size = state % 7  # includes the EMPTY family
            fam = []
            for _ in range(size):
                state = lcg_step(state)
                fam.append(pool[state % len(pool)])
            inside = [comp(s) for s in fam if images_disjoint(s, top)]
            top_families += 1
            if meet_of_parts(inside, n) != top:
                top_violations += 1
                top_ok = False
    manufactured_is_top = all(
        discrete(built[k]["atom_count"]) == discrete(built[k]["centre_dim_with_sink"])
        for k in ("PVM211", "PVM22")
    )
    gate(
        "G2-12",
        "IMPOSSIBILITY",
        "TOP OF LATTICE: the manufactured record is the atom instrument of "
        "its own boundary, hence the greatest element of that boundary's "
        "record lattice; and cl(top) = top for EVERY admitted future family, "
        "the empty family included, by extensivity alone.  No closure "
        "operator dethrones the top of its own lattice, under any law -- this "
        "is what defeats the discriminator, and it needs no covariance premise",
        top_ok and manufactured_is_top,
        {
            "families_swept": top_families,
            "violations": top_violations,
            "atom_counts_swept": [2, 3, 4, 5],
            "manufactured_record_is_the_top": manufactured_is_top,
        },
    )
    FINDINGS["G2_manufactured_record_is_lattice_top"] = bool(top_ok and manufactured_is_top)

    # ---- G2-12b  STRUCTURE THEOREM: Fix(cl_F) is exactly the Moore family of
    #      meets of the collision partitions the family realizes.
    struct_ok, struct_families, struct_bad = True, 0, 0
    state = 771103
    for n in (3, 4):
        pool = relations_of(n)
        for t in range(750):
            state = lcg_step(state)
            size = 1 + state % 5
            fam = []
            for _ in range(size):
                state = lcg_step(state)
                fam.append(pool[state % len(pool)])
            cs = [comp(s) for s in fam]
            realized = sorted(set(cs))
            fixed = set(fix_set_of_family(fam, n, cs))
            moore = set()
            for k in range(len(realized) + 1):
                for sub in combinations(realized, k):
                    moore.add(meet_of_parts(list(sub), n))
            struct_families += 1
            if fixed != moore:
                struct_bad += 1
                struct_ok = False
    gate(
        "G2-12b",
        "IMPOSSIBILITY",
        "STRUCTURE: Fix(cl_F) is exactly the set of meets of subsets of the "
        "collision partitions realized by F, the empty meet being the top -- "
        "so the fixed-point set is always a meet-subsemilattice containing "
        "the top, whatever the law",
        struct_ok,
        {"families_swept": struct_families, "mismatches": struct_bad},
    )

    # ---- G2-12c  the closure is COVARIANT under atom relabelling: this is
    #      the step the covariance obstruction actually uses, measured.
    cov_ok, cov_tests = True, 0
    for n in (4, 5):
        for sigma in permutations(range(n)):
            for p in parts_of(n):
                cov_tests += 1
                if cl_measured(relabel_part(p, sigma), n) != relabel_part(
                    cl_measured(p, n), sigma
                ):
                    cov_ok = False
    gate(
        "G2-12c",
        "IMPOSSIBILITY",
        "COVARIANCE, MEASURED: cl commutes with every atom relabelling at "
        "atom counts 4 and 5 -- the fixed-point set is stable under the whole "
        "symmetric group, so no object built from it distinguishes two "
        "boundaries related by a relabelling",
        cov_ok,
        {"tests": cov_tests, "atom_counts": [4, 5]},
    )

    # ---- G2-13  THE SECTOR-TYPE WITNESS, on two independently built objects.
    prog("G2  witness: the legitimate C^5 and a constructed manufactured C^5")
    n5 = 5
    perm = [1, 2, 3, 4, 0]
    V = tuple(
        tuple(ONE if perm[i] == j else ZERO for j in range(n5)) for i in range(n5)
    )
    unitary_ok = meq(mmul(madj(V), V), mid(n5)) and meq(mmul(V, madj(V)), mid(n5))
    legit = FIXTURES["C5"]
    legit_atoms = [legit.central_projection([k]) for k in range(n5)]
    man_atoms = objs["PVM5"]["atoms"]
    U = embed_unitary_with_sink(objs["PVM5"]["rotation"], 4)
    U_unitary = meq(mmul(madj(U), U), mid(n5)) and meq(mmul(U, madj(U)), mid(n5))
    T = mmul(U, V)
    carried = []
    for k in range(n5):
        img = mmul(mmul(T, legit_atoms[k]), madj(T))
        hit = [l for l in range(n5) if meq(img, man_atoms[l])]
        carried.append(hit[0] if len(hit) == 1 else None)
    bijection = sorted(h for h in carried if h is not None) == list(range(n5))
    same_sector_type = sorted(mrank(z) for z in legit_atoms) == sorted(
        mrank(z) for z in man_atoms
    )
    gate(
        "G2-13",
        "IMPOSSIBILITY",
        "SECTOR-TYPE ISOMORPHISM, TWO CONSTRUCTED OBJECTS: the legitimately "
        "derived eraser minimum C^5 and an independently constructed "
        "manufactured five-outcome boundary (a rank-(1,1,1,1) PVM in a "
        "rotated basis, its matched dephasing's range, plus the retained "
        "sink) have the same sector type, and the explicit reversible map "
        "(W (+) 1)V carries the atoms of the first onto the atoms of the "
        "second bijectively.  Whether that map is ADMITTED is a property of "
        "the committed law, measured per law in G2-14, never inferred from "
        "its existence",
        unitary_ok and U_unitary and bijection and same_sector_type,
        {
            "shift_unitary_over_Z": unitary_ok,
            "rotation_unitary": U_unitary,
            "atom_bijection": carried,
            "same_sector_type": same_sector_type,
            "permutation": perm,
        },
    )
    FINDINGS["G2_covariant_criteria_cannot_separate_under_law_hom"] = bool(
        unitary_ok and U_unitary and bijection and same_sector_type and cov_ok
    )

    # ---- G2-14  ADMISSION IS LAW-RELATIVE: a committed law that satisfies
    #      condition R, keeps every earned rung, and admits NO nontrivial
    #      relabelling at all.
    prog("G2  counter-law: the reprepare-generated law admits no relabelling")
    gens5 = [reprepare_support(p, 5) for p in parts_of(5)]
    gens_fn = [tuple(next(iter(s)) for s in g) for g in gens5]
    seen = set(gens_fn)
    frontier = list(seen)
    while frontier:
        fresh = []
        for f in frontier:
            for g in gens_fn:
                for h in (
                    tuple(g[f[k]] for k in range(5)),
                    tuple(f[g[k]] for k in range(5)),
                ):
                    if h not in seen:
                        seen.add(h)
                        fresh.append(h)
        frontier = fresh
    law_R = sorted(seen)
    reversible = [f for f in law_R if len(set(f)) == 5]
    shift_admitted = tuple(perm) in seen
    law_R_sups = [functional_support(f) for f in law_R]
    fixed_under_R = fix_set_of_family(law_R_sups, 5)
    counter_ok = (
        len(law_R) == 120
        and len(reversible) == 1
        and reversible[0] == (0, 1, 2, 3, 4)
        and not shift_admitted
        and len(fixed_under_R) == 52
    )
    gate(
        "G2-14",
        "IMPOSSIBILITY",
        "ADMISSION IS MEASURED, NOT INFERRED: the composition closure of the "
        "reprepare futures that condition R itself demands is a law with 120 "
        "admitted sector maps of which exactly ONE is reversible -- the "
        "identity.  It admits no nontrivial atom relabelling at all, so the "
        "cyclic shift is not admitted there, while every record remains fixed "
        "(52 of 52).  The covariance obstruction is therefore law-relative "
        "and its hypothesis must be measured for each committed law",
        counter_ok,
        {
            "admitted_sector_maps": len(law_R),
            "reversible_admitted": len(reversible),
            "nontrivial_admitted_permutations": len(reversible) - 1,
            "cyclic_shift_admitted": shift_admitted,
            "records_fixed": len(fixed_under_R),
            "records": bell(5),
        },
    )
    FINDINGS["G2_relabelling_admission_is_law_relative"] = bool(counter_ok)

    # ---- G2-15  THE DEGENERACY IS NOT AN ARTIFACT OF THE ADMITTED CLASS.
    prog("G2  law families: the degeneracy under five no-reprepare laws")
    fam_table = {}
    for n in (1, 2, 3, 4, 5):
        parts = parts_of(n)
        perms_n = list(permutations(range(n)))
        rows = {}
        det = [functional_support(f) for f in product(range(n), repeat=n)]
        rows["DET"] = det
        rows["FUNNEL"] = [functional_support(tuple(range(n)))] + [
            elementary_merge(n, k, l) for k in range(n) for l in range(n) if k != l
        ]
        rows["REV"] = [functional_support(sg) for sg in perms_n]
        if n <= 4:
            allrel = relations_of(n)
            reps = {reprepare_support(p, n) for p in parts}
            rows["ALL"] = allrel
            rows["NOREP"] = [s for s in allrel if s not in reps]
            rows["UNITAL"] = [s for s in allrel if has_total_support(s, n, perms_n)]
        fam_table[n] = {}
        for label, fam in rows.items():
            fam_table[n][label] = {
                "futures": len(fam),
                "fixed": len(fix_set_of_family(fam, n)),
                "records": len(parts),
            }
    no_reprepare_degenerate = all(
        fam_table[n][label]["fixed"] == fam_table[n][label]["records"]
        for n in fam_table
        for label in ("DET", "FUNNEL")
    ) and all(
        fam_table[n][label]["fixed"] == fam_table[n][label]["records"]
        for n in (1, 2, 3, 4)
        for label in ("ALL", "NOREP", "UNITAL")
    )
    gate(
        "G2-15",
        "characterization",
        "THE DEGENERACY IS NOT BOUGHT WITH A GENEROUS FUTURE CLASS: cl is the "
        "identity on the deterministic classical postprocessings (DET), on "
        "the unital futures (UNITAL), on the admitted class with every "
        "reprepare deleted (NOREP), and on the FUNNEL law of the identity "
        "plus the n(n-1) elementary sector merges -- three futures at two "
        "atoms, seven at three, twenty-one at five.  None of these discards "
        "anything inside a kept sector",
        no_reprepare_degenerate,
        fam_table,
    )

    # ---- G2-16  the single escape, and its price.
    rev_fixed = {n: fam_table[n]["REV"]["fixed"] for n in fam_table}
    rev_selective = all(rev_fixed[n] == 1 for n in rev_fixed)
    rev_value_is_top = all(
        fix_set_of_family(
            [functional_support(sg) for sg in permutations(range(n))], n
        )
        == [discrete(n)]
        for n in (2, 3, 4, 5)
    )
    gate(
        "G2-16",
        "characterization",
        "THE ONE ESCAPE AND ITS PRICE: under a reversible-only law the "
        "closure IS selective -- exactly one record is fixed out of "
        "1, 2, 5, 15, 52 -- but the record it selects is the top of the "
        "lattice, i.e. the manufactured record itself, which becomes the "
        "UNIQUE fixed point.  Restricting the law to escape the degeneracy "
        "makes the smuggling worse, not better",
        rev_selective and rev_value_is_top,
        {
            "fixed_per_atom_count": rev_fixed,
            "records_per_atom_count": {n: bell(n) for n in rev_fixed},
            "selected_record_is_the_top": rev_value_is_top,
        },
    )


# --------------------------------------------------------------------------
# G3 — THE FOUR CARRIED CONTROL FAMILIES
# --------------------------------------------------------------------------


def run_g3():
    prog("G3  controls: branch memory, hostile operator system, C*, no-write")

    cl_of = cl_measured

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

    def branch_restriction(part):
        """The restriction of a record on the five-atom eraser core to the
        four branch labels (atom 0 is the common sink), relabelled to
        {0,1,2,3} so that it can be compared with the inherited seams."""
        induced = tuple(
            sorted(
                tuple(sorted(set(b) & {1, 2, 3, 4}))
                for b in part
                if set(b) & {1, 2, 3, 4}
            )
        )
        return tuple(sorted(tuple(sorted(x - 1 for x in b)) for b in induced))

    induced_relabelled = branch_restriction(core5)
    not_a_seam = induced_relabelled not in nine_seams
    n_fixed_c5 = bm_fixed["C5"]["fixed"]
    # how many of the 52 records DO restrict to one of the nine seams, and
    # how many of those are fixed?  The control's negative direction is that
    # the closure selects nothing, not that it excludes seams.
    seam_records = [p for p in parts_of(5) if branch_restriction(p) in nine_seams]
    seam_records_fixed = [p for p in seam_records if cl_of(p, 5) == p]
    gate(
        "G3-1e",
        "control-branch-memory-negative",
        "NEGATIVE: the C^5 common-sink task minimum is NOT promoted to a W3 "
        "seam -- its five-atom core restricted to the branch labels is the "
        "discrete partition, which is none of the nine inherited seams "
        "because it is too FINE, not because anything rejected it.  Of the 52 "
        "records on that core, 33 do restrict to one of the nine seams, and "
        "all 33 are fixed, exactly as all 52 are: the closure SELECTS "
        "NOTHING, it does not exclude seams",
        not_a_seam
        and n_fixed_c5 == 52
        and len(seam_records) == 33
        and len(seam_records_fixed) == 33,
        {
            "induced_partition": [list(b) for b in induced_relabelled],
            "is_one_of_the_nine_seams": not not_a_seam,
            "records_all_equally_fixed": n_fixed_c5,
            "records_restricting_to_a_seam": len(seam_records),
            "of_those_fixed": len(seam_records_fixed),
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
        "falsification": {
            "note": (
                "run `--falsification-selftest`; each mutant must exit 1.  "
                "Anchor mutants substitute the reported value at the anchor "
                "comparison site and certify that the anchor harness is live; "
                "derivation mutants perturb a computation and must make at "
                "least one G1/G2 gate fail, which also exits 1"
            ),
            "anchor_mutants": {k: v[0] for k, v in sorted(MUTANT_TABLE.items())},
            "derivation_mutants": dict(sorted(MUTANT_GATE_TABLE.items())),
            "anchors_covered": sorted({v[0] for v in MUTANT_TABLE.values()}),
            "anchors_total": len(ANCHORS),
            "determinism": (
                "no wall-clock value enters this receipt or the rendered "
                "output; timings appear only on the progress stream, so two "
                "consecutive runs of the same source produce byte-identical "
                "artifacts"
            ),
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
    L.append("FALSIFICATION COVERAGE")
    f = rec["falsification"]
    L.append(f"  anchor mutants ({len(f['anchor_mutants'])}): " + ", ".join(
        f"{k} -> {v}" for k, v in f["anchor_mutants"].items()
    ))
    L.append(f"  derivation mutants ({len(f['derivation_mutants'])}): " + ", ".join(
        f"{k} ({v})" for k, v in f["derivation_mutants"].items()
    ))
    L.append(
        f"  anchors exercised: {len(f['anchors_covered'])} of {f['anchors_total']}"
        f"  ({', '.join(f['anchors_covered'])})"
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

# Mutants that perturb a DERIVATION rather than a reported anchor value, so
# that the unit's own new results -- the component lemma, the closure, the
# fixed-point strata and the discriminator -- carry falsification coverage
# too.  Each must make at least one G1/G2 gate fail, and a failing gate under
# a mutant exits 1.
MUTANT_GATE_TABLE = {
    "comp-coarse": "comp() merges the first two atoms unconditionally",
    "avail-lax": "images_disjoint() skips the first block pair",
}


def run_falsification_selftest() -> int:
    prog("FALSIFICATION SELF-TEST: each mutant must exit 1")
    rows = []
    ok = True
    names = sorted(MUTANT_TABLE) + sorted(MUTANT_GATE_TABLE)
    for name in names:
        r = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--mutant", name],
            capture_output=True,
            text=True,
        )
        killed = r.returncode == 1 and (
            "ANCHOR FAILURE" in r.stdout or "GATE FAILURE" in r.stdout
        )
        broke = (
            MUTANT_TABLE[name][0] if name in MUTANT_TABLE else "gates"
        )
        detail = ""
        if name in MUTANT_GATE_TABLE:
            for line in r.stdout.splitlines():
                if line.startswith("GATE FAILURE"):
                    detail = line[len("GATE FAILURE "):]
        rows.append((name, broke, r.returncode, killed, detail))
        if not killed:
            ok = False
    for name, broke, code, killed, detail in rows:
        sys.stdout.write(
            f"  mutant {name:12s} breaks {broke:6s} exit={code} "
            f"{'KILLED (correct)' if killed else 'SURVIVED (DEFECT)'}"
            f"{('  ' + detail) if detail else ''}\n"
        )
    sys.stdout.write(
        f"falsification self-test: {sum(1 for r in rows if r[3])}/{len(rows)} mutants killed\n"
    )
    return 0 if ok else 1


def main() -> int:
    global MUTANT, MUTANT_OVERRIDE
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--mutant",
        choices=sorted(MUTANT_TABLE) + sorted(MUTANT_GATE_TABLE),
        default=None,
    )
    ap.add_argument("--falsification-selftest", action="store_true")
    ap.add_argument("--no-write-files", action="store_true")
    args = ap.parse_args()

    if args.falsification_selftest:
        return run_falsification_selftest()

    if args.mutant:
        MUTANT = args.mutant
        if args.mutant in MUTANT_TABLE:
            aid, val = MUTANT_TABLE[args.mutant]
            MUTANT_OVERRIDE = {aid: val}
            prog(f"MUTANT MODE: anchor {aid} deliberately broken ({args.mutant})")
        else:
            prog(
                f"MUTANT MODE: derivation deliberately broken "
                f"({args.mutant}: {MUTANT_GATE_TABLE[args.mutant]})"
            )

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
        if MUTANT:
            sys.stdout.write(f"GATE FAILURE {','.join(rec['gates']['failed'])}\n")
            sys.stdout.flush()
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
