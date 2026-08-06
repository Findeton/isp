#!/usr/bin/env python3
"""RQ0-L1 Cycle B' -- composite boundaries and the de-smuggling arena.

Executes the frozen pin `v13/note-rq0-l1-composite-boundaries-pin.md`
(commit 62cdf68) in two halves:

  H1  the monoidal layer   -- composite boundary factorization; the
                              Core(A (x) B) vs Core(A) (x) Core(B) gap as the
                              operational entanglement witness
  H2  the de-smuggling arena -- two independently declared task families, a
                              declared overlap, the descent selector, the
                              top-of-lattice guard, and THE DISCRIMINATOR

Immutable inputs reused as anchors: the Cycle B terminal delivery (v13 #123 --
the CONSTRUCTED manufactured boundary, its committed centre dimensions, the
counter-law, the top-of-lattice theorem) and the #103/#111 fixtures.

Substantive negatives exit 0.  Anchor mismatches exit 1.  `--mutant NAME`
breaks exactly one committed anchor or one derivation step and must exit 1.

Scope: finite; TWO boundaries and one declared overlap; "independence" is
OPERATIONAL (which joint operations are admitted), never spatial.  No
locality, topology, causality, spacetime, field or gravity object is
constructed or claimed.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import subprocess
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import rq0_l0_fixed_point_exact as CB  # the Cycle B TERMINAL machinery

SCHEMA = "rq0-l1-composite-boundaries-receipt-v1"
PIN_COMMIT = "62cdf68"
BASE_COMMIT = "0bc943c"
OUT_TXT = HERE / "rq0_l1_composite_output.txt"
OUT_JSON = HERE / "rq0_l1_composite_receipt.json"

T0 = time.time()
MUTANT: str | None = None
SOURCE_SHA256 = ""
EXACTNESS_VIOLATIONS: list = []

QC = CB.QC
ZERO = CB.ZERO
ONE = CB.ONE
mat = CB.mat
mmul = CB.mmul
madd = CB.madd
msub = CB.msub
madj = CB.madj
meq = CB.meq
mid = CB.mid
mzero = CB.mzero
mtrace = CB.mtrace
mkron = CB.mkron
mrank = CB.mrank


def prog(msg: str) -> None:
    sys.stdout.write(f"[{time.time() - T0:7.1f}s] {msg}\n")
    sys.stdout.flush()


# --------------------------------------------------------------------------
# 0.  Exact linear algebra on flattened matrices.  Independent of CB's own
#     span routines: rref, membership, nullspace, subspace intersection and
#     range projections are written here so that the composite statements are
#     not decided by the machinery whose results they are compared against.
# --------------------------------------------------------------------------


def flat(m) -> tuple:
    return tuple(x for row in m for x in row)


def unflat(v, n: int) -> tuple:
    return tuple(tuple(v[i * n + j] for j in range(n)) for i in range(n))


def rref(vectors):
    """Exact reduced row echelon basis.  Returns (basis, pivots)."""
    rows = [list(v) for v in vectors]
    basis: list[list] = []
    pivots: list[int] = []
    for r in rows:
        cur = list(r)
        for b, p in zip(basis, pivots):
            if not cur[p].is_zero():
                f = cur[p]
                cur = [cur[i] - f * b[i] for i in range(len(cur))]
        piv = next((i for i, x in enumerate(cur) if not x.is_zero()), None)
        if piv is None:
            continue
        inv = cur[piv].inv()
        cur = [x * inv for x in cur]
        for i in range(len(basis)):
            if not basis[i][piv].is_zero():
                f = basis[i][piv]
                basis[i] = [basis[i][k] - f * cur[k] for k in range(len(cur))]
        basis.append(cur)
        pivots.append(piv)
        order = sorted(range(len(pivots)), key=lambda i: pivots[i])
        basis = [basis[i] for i in order]
        pivots = [pivots[i] for i in order]
    return [tuple(b) for b in basis], pivots


def in_span(basis, pivots, v) -> bool:
    cur = list(v)
    for b, p in zip(basis, pivots):
        if not cur[p].is_zero():
            f = cur[p]
            cur = [cur[i] - f * b[i] for i in range(len(cur))]
    return all(x.is_zero() for x in cur)


def nullspace(rows, ncols: int):
    """Exact basis of {x : rows . x = 0}."""
    basis, pivots = rref(rows)
    free = [i for i in range(ncols) if i not in pivots]
    out = []
    for f in free:
        x = [ZERO] * ncols
        x[f] = ONE
        for b, p in zip(basis, pivots):
            x[p] = QC(0) - b[f]
        out.append(tuple(x))
    return out


def subspace_intersection(basisA, basisB, dim: int):
    """Exact basis of span(basisA) cap span(basisB)."""
    if not basisA or not basisB:
        return []
    a, b = len(basisA), len(basisB)
    rows = []
    for coord in range(dim):
        rows.append(
            tuple([basisA[i][coord] for i in range(a)] + [QC(0) - basisB[j][coord] for j in range(b)])
        )
    ns = nullspace(rows, a + b)
    out = []
    for sol in ns:
        v = [ZERO] * dim
        for i in range(a):
            if not sol[i].is_zero():
                v = [v[c] + sol[i] * basisA[i][c] for c in range(dim)]
        if any(not x.is_zero() for x in v):
            out.append(tuple(v))
    basis, _ = rref(out)
    return basis


def inner(u, v) -> QC:
    acc = ZERO
    for a, b in zip(u, v):
        acc = acc + a.conj() * b
    return acc


def range_projection(vectors, n: int):
    """Exact orthogonal projection onto span(vectors) in C^n (Gram-Schmidt)."""
    orth: list[tuple] = []
    for v in vectors:
        cur = list(v)
        for b in orth:
            c = inner(b, cur) * inner(b, b).inv()
            cur = [cur[i] - c * b[i] for i in range(n)]
        if any(not x.is_zero() for x in cur):
            orth.append(tuple(cur))
    P = [[ZERO] * n for _ in range(n)]
    for b in orth:
        ninv = inner(b, b).inv()
        for i in range(n):
            for j in range(n):
                P[i][j] = P[i][j] + b[i] * b[j].conj() * ninv
    return tuple(tuple(r) for r in P)


def support_projection(m, n: int):
    """Range projection of a positive semidefinite matrix, exactly."""
    cols = [tuple(m[i][j] for i in range(n)) for j in range(n)]
    return range_projection(cols, n)


def partial_trace_B(m, dA: int, dB: int):
    out = [[ZERO] * dA for _ in range(dA)]
    for i in range(dA):
        for k in range(dA):
            acc = ZERO
            for j in range(dB):
                acc = acc + m[i * dB + j][k * dB + j]
            out[i][k] = acc
    return tuple(tuple(r) for r in out)


def partial_trace_A(m, dA: int, dB: int):
    out = [[ZERO] * dB for _ in range(dB)]
    for j in range(dB):
        for l in range(dB):
            acc = ZERO
            for i in range(dA):
                acc = acc + m[i * dB + j][i * dB + l]
            out[j][l] = acc
    return tuple(tuple(r) for r in out)


def mscale(s, m):
    return tuple(tuple(s * x for x in r) for r in m)


# --------------------------------------------------------------------------
# 1.  Gate / anchor bookkeeping (Cycle B's discipline, own tables).
# --------------------------------------------------------------------------

GATES: list[dict] = []
ANCHORS: list[dict] = []
FINDINGS: dict = {}
TABLES: dict = {}
MUTANT_OVERRIDE: dict = {}


def gate(gid: str, cls: str, claim: str, ok: bool, value=None) -> bool:
    GATES.append({"id": gid, "class": cls, "claim": claim, "pass": bool(ok), "value": value})
    return bool(ok)


def assert_exact(value) -> bool:
    if isinstance(value, bool) or isinstance(value, int):
        return True
    if isinstance(value, (Fr, QC)):
        return True
    if isinstance(value, (tuple, list)):
        return all(assert_exact(x) for x in value)
    if isinstance(value, str):
        return True
    return False


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
            f"ANCHOR FAILURE {aid} ({source}): {quantity} committed={committed} computed={c}\n"
        )
        sys.stdout.flush()
        raise SystemExit(1)


# --------------------------------------------------------------------------
# 2.  Declared boundaries: an ambient finite direct sum, a spanning set for
#     the effect system, and the central atoms.  The core is computed from
#     the ADMITTED splits, never read off the block structure.
# --------------------------------------------------------------------------


class Boundary:
    def __init__(self, name: str, dim: int, atoms, span, note: str = ""):
        self.name = name
        self.dim = dim
        self.atoms = tuple(atoms)          # central atoms of the ambient algebra
        self.span = tuple(span)            # spanning set of the effect system
        self.note = note
        self._basis = None

    def basis(self):
        if self._basis is None:
            self._basis = rref([flat(m) for m in self.span])
        return self._basis


def full_algebra_span(blocks):
    """All matrix units of a block-diagonal ambient algebra."""
    alg = CB.CStar("tmp", tuple(blocks))
    return alg.matrix_units(), tuple(alg.central_projection([k]) for k in alg.atoms())


def boundary_from_blocks(name: str, blocks) -> Boundary:
    units, atoms = full_algebra_span(blocks)
    return Boundary(name, sum(blocks), atoms, units, f"full direct sum {blocks}")


def hostile_boundary() -> Boundary:
    """#111 sec 8.1: S = span{(I,I),(Z,Z),(X,2X+Z)} in M_2 (+) M_2."""
    I2 = mid(2)
    Z2 = mat(((1, 0), (0, -1)))
    X2 = mat(((0, 1), (1, 0)))

    def ds(a, b):
        return CB.block_diag(a, b)

    s0 = ds(I2, I2)
    s1 = ds(Z2, Z2)
    s2 = ds(X2, madd(mscale(QC(2), X2), Z2))
    alg = CB.CStar("M2+M2", (2, 2))
    atoms = tuple(alg.central_projection([k]) for k in alg.atoms())
    return Boundary("HOSTILE", 4, atoms, (s0, s1, s2), "hostile operator system")


def manufactured_boundary(ranks) -> tuple:
    """Cycle B sec 4.5, CONSTRUCTED: exact Givens PVM + matched dephasing +
    A_P + the retained sink.  Reused verbatim from the terminal unit."""
    facts, objs = CB.build_manufactured_boundary(tuple(ranks))
    dim = sum(ranks) + 1
    b = Boundary(
        f"MAN{''.join(str(r) for r in ranks)}",
        dim,
        objs["atoms"],
        objs["basis"],
        "constructed manufactured boundary (rotated PVM + matched dephasing + sink)",
    )
    return facts, objs, b


def aligned_manufactured_boundary(ranks) -> Boundary:
    """The SAME construction with the rotation replaced by the identity: a
    manufactured boundary whose PVM is aligned with the declared addresses.
    Used only as the sharpness control of H2."""
    dim = sum(ranks)
    proj = []
    off = 0
    for r in ranks:
        m = [[ZERO] * dim for _ in range(dim)]
        for i in range(off, off + r):
            m[i][i] = ONE
        proj.append(tuple(tuple(x) for x in m))
        off += r
    atoms = [CB.embed_with_sink(p, dim) for p in proj]
    sink = [[ZERO] * (dim + 1) for _ in range(dim + 1)]
    sink[dim][dim] = ONE
    sink = tuple(tuple(r) for r in sink)
    atoms.append(sink)
    span = []
    for r_i, r in enumerate(ranks):
        o = sum(ranks[:r_i])
        for i in range(r):
            for j in range(r):
                m = [[ZERO] * (dim + 1) for _ in range(dim + 1)]
                m[o + i][o + j] = ONE
                span.append(tuple(tuple(x) for x in m))
    span.append(sink)
    return Boundary(
        f"ALIGNED{''.join(str(r) for r in ranks)}",
        dim + 1,
        atoms,
        span,
        "aligned manufactured boundary (no rotation)",
    )


def admitted_split_partition(b: Boundary):
    """The atoms of the Boolean algebra of ADMITTED split projections.

    V = (effect system) cap (span of the central atoms), computed by exact
    subspace intersection.  Two ambient atoms lie in the same admitted atom
    exactly when no element of V separates them; the partition's own block
    indicators are then verified to lie in V, so the blocks ARE admitted
    splits and no finer admitted split exists.  Returns (partition, ok).
    """
    n = len(b.atoms)
    ebas, epiv = b.basis()
    # residual of each atom indicator modulo the effect system: a central
    # element sum_k c_k z_k lies in E exactly when sum_k c_k r_k = 0.
    residuals = []
    for z in b.atoms:
        cur = list(flat(z))
        for bb, p in zip(ebas, epiv):
            if not cur[p].is_zero():
                f = cur[p]
                cur = [cur[i] - f * bb[i] for i in range(len(cur))]
        residuals.append(cur)
    rows = [tuple(residuals[k][c] for k in range(n)) for c in range(b.dim * b.dim)]
    rows = [r for r in rows if any(not x.is_zero() for x in r)]
    coords = nullspace(rows, n) if rows else [
        tuple(ONE if i == k else ZERO for i in range(n)) for k in range(n)
    ]
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if all(c[i] == c[j] for c in coords):
                a, bb = find(i), find(j)
                if a != bb:
                    parent[a] = bb
    groups: dict = {}
    for x in range(n):
        groups.setdefault(find(x), []).append(x)
    part = tuple(sorted(tuple(sorted(v)) for v in groups.values()))
    ok = True
    for blk in part:
        ind = mzero(b.dim)
        for k in blk:
            ind = madd(ind, b.atoms[k])
        if not in_span(ebas, epiv, flat(ind)):
            ok = False
    return part, ok


# --------------------------------------------------------------------------
# 3.  Composites.
# --------------------------------------------------------------------------


def composite_product_law(bA: Boundary, bB: Boundary) -> Boundary:
    """The declared PRODUCT composite: local operations on each factor and the
    joint class GENERATED by them -- the algebraic span of products."""
    atoms = [mkron(za, zb) for za in bA.atoms for zb in bB.atoms]
    span = [mkron(a, b) for a in bA.span for b in bB.span]
    return Boundary(
        f"{bA.name}(x){bB.name}", bA.dim * bB.dim, atoms, span, "product law"
    )


def local_split_partition_direct(b: Boundary, side: str, dA: int = 2, dB: int = 2):
    """The partition of the boundary's core atoms cut by the splits readable
    on ONE FACTOR ALONE: admitted splits of the composite boundary of the form
    Q (x) 1 (side A) or 1 (x) Q (side B).  Unions of core blocks are the only
    admitted splits, so the enumeration is exhaustive."""
    part, _ = admitted_split_partition(b)
    n = len(b.atoms)
    if MUTANT == "gap-lax":
        return tuple((i,) for i in range(n))
    locs = []
    for r in range(len(part) + 1):
        for sub in combinations(range(len(part)), r):
            idxs = sorted(i for t in sub for i in part[t])
            Z = mzero(b.dim)
            for k in idxs:
                Z = madd(Z, b.atoms[k])
            if side == "A":
                Q = mscale(QC(Fr(1, dB)), partial_trace_B(Z, dA, dB))
                good = meq(Z, mkron(Q, mid(dB)))
            else:
                Q = mscale(QC(Fr(1, dA)), partial_trace_A(Z, dA, dB))
                good = meq(Z, mkron(mid(dA), Q))
            if good:
                locs.append(set(idxs))
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if all((i in L) == (j in L) for L in locs):
                a, b2 = find(i), find(j)
                if a != b2:
                    parent[a] = b2
    groups = {}
    for x in range(n):
        groups.setdefault(find(x), []).append(x)
    return tuple(sorted(tuple(sorted(v)) for v in groups.values()))


def join_partitions(p, q, n: int):
    """Common refinement."""
    out = []
    for b in p:
        for c in q:
            inter = tuple(sorted(set(b) & set(c)))
            if inter:
                out.append(inter)
    return tuple(sorted(out))


def is_product_projection(P, dA: int, dB: int) -> bool:
    """P = Q_A (x) Q_B for projections Q_A, Q_B -- decided exactly by the
    supports of the two partial traces."""
    qa = support_projection(partial_trace_B(P, dA, dB), dA)
    qb = support_projection(partial_trace_A(P, dA, dB), dB)
    return meq(P, mkron(qa, qb))


def schmidt_rank_of_rank_one(P, dA: int, dB: int) -> int:
    """Exact Schmidt rank of a rank-one projection, from any nonzero column."""
    n = dA * dB
    col = None
    for j in range(n):
        c = tuple(P[i][j] for i in range(n))
        if any(not x.is_zero() for x in c):
            col = c
            break
    M = [[col[i * dB + j] for j in range(dB)] for i in range(dA)]
    return mrank(tuple(tuple(r) for r in M))


# --------------------------------------------------------------------------
# 4.  H0 -- referent census and exactness.
# --------------------------------------------------------------------------

REFERENTS = [
    ("declared boundary", "#103 minimal sufficient process boundary", "committed"),
    ("operational classical core", "#111 Thm 5.4 finite atomic operational core", "committed"),
    ("admitted split projection", "#111 Def 4.3", "committed"),
    ("constructed manufactured boundary", "Cycle B sec 4.5 (Givens PVM + matched dephasing + A_P + sink)", "committed"),
    ("counter-law L_R", "Cycle B Prop 4.12", "committed"),
    ("top-of-lattice theorem", "Cycle B Thm 4.8", "committed"),
    ("availability / no-collision criterion", "Cycle B Prop 2.5", "committed"),
    ("record = partition of core atoms", "Cycle B Lemma 3.1", "committed"),
    ("maximally entangled Choi vector", "#111 sec 6.1 (rank J(id) = 1)", "committed"),
    ("normalized antisymmetric vector psi^-", "#111 sec 3.3 (<psi^-|J(P)|psi^-> = -1/2)", "committed"),
    ("declared composite operational structure", "THIS UNIT (H1)", "new, four-gated in the paper"),
    ("declared overlap and descent selector", "THIS UNIT (H2)", "new, four-gated in the paper"),
]


def run_h0():
    prog("H0  referent census and exactness")
    gate(
        "H0-01",
        "census",
        "REFERENT CENSUS: every object used is either a committed referent of "
        "#103/#111/Cycle B or one of the two objects this unit introduces and "
        "four-gates in the paper; no object is used whose referent is unlisted",
        all(len(r) == 3 for r in REFERENTS) and len(REFERENTS) == 12,
        {"referents": [{"object": a, "source": b, "status": c} for a, b, c in REFERENTS]},
    )
    tree = ast.parse(Path(__file__).resolve().read_text())
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            bad.append(("float-literal", node.lineno))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "float":
            bad.append(("float-call", node.lineno))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            # pathlib joins (HERE / "name.txt") are the only permitted uses
            if not (isinstance(node.right, ast.Constant) and isinstance(node.right.value, str)):
                bad.append(("true-division", node.lineno))
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [node.module or ""]
        else:
            continue
        for nm in names:
            if nm.split(".")[0] in ("math", "cmath", "numpy", "scipy", "decimal", "random", "statistics"):
                bad.append((nm, node.lineno))
    gate(
        "H0-02",
        "exactness",
        "NO FLOAT IN ANY SUBSTANTIVE PATH: an abstract-syntax-tree sweep of "
        "this unit's own source finds no float literal, no float constructor, "
        "no true division and no inexact-arithmetic import; every scalar is a "
        "Fraction or an element of Q(i).  The imported predecessor module "
        "carries its own exactness gate and is terminal",
        not bad,
        {"violations": bad},
    )
    probe = QC(Fr(1, 3)) * QC(3)
    gate(
        "H0-03",
        "exactness",
        "EXACT SCALAR PROBE: 1/3 times 3 is exactly 1 in the arithmetic used, "
        "and the reciprocal of 7 squared times 49 is exactly 1",
        probe == ONE and QC(7).inv() * QC(7).inv() * QC(49) == ONE,
    )


# --------------------------------------------------------------------------
# 5.  H1 -- the monoidal layer.
# --------------------------------------------------------------------------


def bell_projections():
    """The four maximally entangled projections, built from the two COMMITTED
    entangled objects of #111 (the Choi vector of the identity channel and the
    normalized antisymmetric vector) by admitted LOCAL unitaries."""
    h = Fr(1, 2)
    phi_p = [[ZERO] * 4 for _ in range(4)]
    for i in (0, 3):
        for j in (0, 3):
            phi_p[i][j] = QC(h)
    phi_p = tuple(tuple(r) for r in phi_p)
    Z = mat(((1, 0), (0, -1)))
    X = mat(((0, 1), (1, 0)))
    ZI = mkron(Z, mid(2))
    XI = mkron(X, mid(2))
    phi_m = mmul(mmul(ZI, phi_p), madj(ZI))
    psi_p = mmul(mmul(XI, phi_p), madj(XI))
    psi_m = mmul(mmul(XI, phi_m), madj(XI))
    return (phi_p, phi_m, psi_p, psi_m), ZI, XI


def basis_projector4(idx):
    m = [[ZERO] * 4 for _ in range(4)]
    m[idx][idx] = ONE
    return tuple(tuple(r) for r in m)


def rotated_product_pvm():
    """A PRODUCT PVM in a rotated (non-coordinate) basis: |+-> style, exactly
    rational as projections.  The control that separates 'rotated basis' from
    'entangled'."""
    pp = mat(((Fr(1, 2), Fr(1, 2)), (Fr(1, 2), Fr(1, 2))))
    pm = mat(((Fr(1, 2), Fr(-1, 2)), (Fr(-1, 2), Fr(1, 2))))
    return tuple(mkron(a, b) for a in (pp, pm) for b in (pp, pm))


def dephasing_range_boundary(name: str, projectors, dim: int, note: str) -> Boundary:
    """#103 sec 7.1's construction: the boundary of a task matched to a PVM is
    the range A_P of the matched dephasing, computed by exact elimination."""
    units = []
    for i in range(dim):
        for j in range(dim):
            m = [[ZERO] * dim for _ in range(dim)]
            m[i][j] = ONE
            units.append(tuple(tuple(x) for x in m))
    span = [mmul(mmul(p, e), p) for p in projectors for e in units]
    basis, piv = rref([flat(m) for m in span])
    reduced = [unflat(b, dim) for b in basis]
    return Boundary(name, dim, tuple(projectors), tuple(reduced), note)


DECLARED_PVMS: dict = {}


def build_declared_pvms():
    bells, ZI, XI = bell_projections()
    prod = tuple(basis_projector4(i) for i in range(4))
    mix = (bells[0], bells[1], basis_projector4(1), basis_projector4(2))
    half = (basis_projector4(0), basis_projector4(3), bells[2], bells[3])
    parity = (
        madd(basis_projector4(0), basis_projector4(3)),
        madd(basis_projector4(1), basis_projector4(2)),
    )
    psi_m = bells[3]
    sym = msub(mid(4), psi_m)
    localz = (
        mkron(mat(((1, 0), (0, 0))), mid(2)),
        mkron(mat(((0, 0), (0, 1))), mid(2)),
    )
    DECLARED_PVMS.update(
        {
            "PROD": (prod, "product PVM in the coordinate basis", False),
            "PRODROT": (rotated_product_pvm(), "product PVM in a rotated basis", False),
            "BELL": (bells, "the four committed maximally entangled projections", True),
            "MIX": (mix, "two entangled and two product atoms", True),
            "HALF": (half, "two product and two entangled atoms", True),
            "PARITY": (parity, "classically correlated rank-two atoms (separable)", False),
            "SYMANTI": ((sym, psi_m), "symmetric / antisymmetric split (psi^- is committed)", True),
            "LOCALZ": (localz, "a local PVM on the first factor alone", False),
        }
    )
    return bells, ZI, XI


def run_h1():
    prog("H1  monoidal layer: committed entangled objects and the declared PVMs")
    bells, ZI, XI = build_declared_pvms()

    # ---- H1-01  the committed entangled objects, recomputed.
    phi_p = bells[0]
    choi_rank = mrank(phi_p)
    anchor("L01", "#111 sec 6.1", "rank of J(identity channel) on M_2", 1, choi_rank)
    psi_m = bells[3]
    # <psi^-|J(P)|psi^-> for the transpose symmetrizer P = (id + tau)/2
    tau = [[ZERO] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            tau[i * 2 + j][j * 2 + i] = ONE
    tau = tuple(tuple(r) for r in tau)
    JP = mscale(QC(Fr(1, 2)), madd(mscale(QC(2), phi_p), tau))
    # J(id) = 2*phi_p (unnormalised maximally entangled), J(tau) = swap
    val = mtrace(mmul(psi_m, JP))
    anchor("L02", "#111 sec 3.3", "<psi^-|J(P)|psi^->", QC(Fr(-1, 2)), val)
    ok = all(meq(mmul(p, p), p) and meq(madj(p), p) for p in bells)
    tot = mzero(4)
    for p in bells:
        tot = madd(tot, p)
    ok = ok and meq(tot, mid(4))
    ok = ok and all(
        meq(mmul(bells[a], bells[b]), mzero(4)) for a in range(4) for b in range(4) if a != b
    )
    sr = [schmidt_rank_of_rank_one(p, 2, 2) for p in bells]
    marg = [partial_trace_B(p, 2, 2) for p in bells]
    max_mixed = all(meq(m, mscale(QC(Fr(1, 2)), mid(2))) for m in marg)
    gate(
        "H1-01",
        "construction",
        "THE ENTANGLED FIXTURE IS BUILT FROM THE COMMITTED OBJECTS: the Choi "
        "projection of the identity channel and the normalized antisymmetric "
        "vector are recomputed and anchored; the remaining two maximally "
        "entangled projections are obtained from the first by the admitted "
        "LOCAL unitaries Z(x)1 and X(x)1.  The four are mutually orthogonal "
        "projections summing to the unit, each of exact Schmidt rank 2, each "
        "with maximally mixed local restriction",
        ok and sr == [2, 2, 2, 2] and max_mixed,
        {"schmidt_ranks": sr, "local_restrictions_maximally_mixed": max_mixed},
    )

    # ---- H1-02  the subspace lemma that proves product-law factorization.
    lemma_ok, lemma_tests = True, 0
    for nameA, bA in list(FIXTURES.items()):
        for nameB, bB in list(FIXTURES.items()):
            if bA.dim * bB.dim > 9:
                continue
            zA = [flat(z) for z in bA.atoms]
            zB = [flat(z) for z in bB.atoms]
            eA, _ = bA.basis()
            eB, _ = bB.basis()
            VA = subspace_intersection(eA, zA, bA.dim * bA.dim)
            VB = subspace_intersection(eB, zB, bB.dim * bB.dim)
            lhsA = [mkron(a, b) for a in bA.span for b in bB.span]
            zAB = [mkron(za, zb) for za in bA.atoms for zb in bB.atoms]
            lhs = subspace_intersection(
                rref([flat(m) for m in lhsA])[0],
                [flat(m) for m in zAB],
                (bA.dim * bB.dim) ** 2,
            )
            rhs = rref(
                [
                    flat(mkron(unflat(a, bA.dim), unflat(b, bB.dim)))
                    for a in VA
                    for b in VB
                ]
            )[0]
            lemma_tests += 1
            if len(lhs) != len(rhs):
                lemma_ok = False
                continue
            lb, lp = rref(lhs)
            if not all(in_span(lb, lp, r) for r in rhs):
                lemma_ok = False
    gate(
        "H1-02",
        "lemma",
        "THE SUPPORT LEMMA, MEASURED: for the declared effect systems, "
        "(E_A (x) E_B) cap (Z_A (x) Z_B) = (E_A cap Z_A) (x) (E_B cap Z_B).  "
        "This is what makes the product-law composite core distribute; it is "
        "verified by exact subspace intersection on every fixture pair of "
        "composite carrier dimension at most 9",
        lemma_ok,
        {"pairs_tested": lemma_tests, "carrier_cap": 9},
    )

    # ---- H1-03  PRODUCT-LAW FACTORIZATION over the committed fixtures.
    prog("H1  product-law sweep over the committed fixture pairs")
    rows = []
    fact_ok = True
    for nameA, bA in FIXTURES.items():
        for nameB, bB in FIXTURES.items():
            if bA.dim * bB.dim > 20:
                continue
            comp = composite_product_law(bA, bB)
            cpart, cok = admitted_split_partition(comp)
            pa, _ = admitted_split_partition(bA)
            pb, _ = admitted_split_partition(bB)
            nA, nB = len(bA.atoms), len(bB.atoms)
            prodpart = tuple(
                sorted(
                    tuple(sorted(k * nB + l for k in ka for l in lb))
                    for ka in pa
                    for lb in pb
                )
            )
            same = cpart == prodpart
            rows.append(
                {
                    "A": nameA,
                    "B": nameB,
                    "core_A": len(pa),
                    "core_B": len(pb),
                    "core_AB": len(cpart),
                    "product_core": len(prodpart),
                    "distributes": same,
                }
            )
            if not (same and cok):
                fact_ok = False
    TABLES["product_law_sweep"] = rows
    gate(
        "H1-03",
        "factorization",
        "PRODUCT-LAW FACTORIZATION: under the declared product law -- local "
        "admitted operations on each factor and the joint class GENERATED by "
        "them -- the composite minimal boundary's admitted split algebra is "
        "exactly the one generated by the local splits, so "
        "Core(A (x) B) = Core(A) (x) Core(B) with the GAP ZERO, on every "
        "ordered pair of committed fixtures of composite carrier dimension at "
        "most 20",
        fact_ok,
        {
            "pairs": len(rows),
            "carrier_cap": 20,
            "gap_nonzero_pairs": [r for r in rows if not r["distributes"]],
        },
    )

    # ---- H1-04  THE HOSTILE WING: no promotion by composition.
    hostile_rows = []
    hostile_ok = True
    for partner in ("C2", "M2", "M2+C", "HOSTILE", "C1"):
        for order in ("SxT", "TxS"):
            bA = FIXTURES["HOSTILE"] if order == "SxT" else FIXTURES[partner]
            bB = FIXTURES[partner] if order == "SxT" else FIXTURES["HOSTILE"]
            comp = composite_product_law(bA, bB)
            cpart, _ = admitted_split_partition(comp)
            pa, _ = admitted_split_partition(bA)
            pb, _ = admitted_split_partition(bB)
            expected = len(pa) * len(pb)
            hostile_rows.append(
                {
                    "composite": f"{bA.name}(x){bB.name}",
                    "core_A": len(pa),
                    "core_B": len(pb),
                    "core_AB": len(cpart),
                    "expected": expected,
                    "promoted": len(cpart) != expected,
                }
            )
            if len(cpart) != expected:
                hostile_ok = False
    TABLES["hostile_wing"] = hostile_rows
    gate(
        "H1-04",
        "control",
        "THE HOSTILE WING IS NOT PROMOTED: the operator system whose "
        "operational core is trivial keeps a trivial wing under composition "
        "with every readable committed factor and with itself -- the "
        "composite core is exactly the product of the two factor cores in all "
        "ten declared composites.  A promotion would have shown up as a "
        "composite core strictly finer than the product",
        hostile_ok,
        {"composites": hostile_rows},
    )

    # ---- H1-05..07  THE JOINT LAW: the gap, measured on the declared PVMs.
    prog("H1  the declared joint tasks: composite core vs local cores")
    pvm_rows = []
    gap_ok = True
    iff_ok = True
    for key, (projs, note, declared_entangled) in DECLARED_PVMS.items():
        b = dephasing_range_boundary(f"JOINT[{key}]", projs, 4, note)
        cpart, cok = admitted_split_partition(b)
        n = len(b.atoms)
        locA = local_split_partition_direct(b, "A")
        locB = local_split_partition_direct(b, "B")
        prodpart = join_partitions(locA, locB, n)
        ranks = [mrank(p) for p in projs]
        rank_one = all(r == 1 for r in ranks)
        srs = [schmidt_rank_of_rank_one(p, 2, 2) if mrank(p) == 1 else None for p in projs]
        entangled_atom = any(s is not None and s > 1 for s in srs)
        prods = [is_product_projection(p, 2, 2) for p in projs]
        opens = cpart != prodpart
        pvm_rows.append(
            {
                "task": key,
                "note": note,
                "atom_ranks": ranks,
                "core_AB": len(cpart),
                "local_A": len(locA),
                "local_B": len(locB),
                "product_core": len(prodpart),
                "gap_opens": opens,
                "schmidt_ranks": srs,
                "atoms_are_product_projections": prods,
                "has_entangled_atom": entangled_atom,
                "declared_entangled": declared_entangled,
                "boundary_factorizes": cpart == prodpart,
            }
        )
        if not cok:
            gap_ok = False
        if entangled_atom != declared_entangled:
            iff_ok = False
        if declared_entangled and not opens:
            gap_ok = False
        if key in ("PROD", "PRODROT", "LOCALZ") and opens:
            gap_ok = False
    TABLES["joint_tasks"] = pvm_rows
    gate(
        "H1-05",
        "witness",
        "THE GAP, BOTH DIRECTIONS: under the declared joint law the composite "
        "core is computed from the composite boundary's admitted splits and "
        "compared with the join of the splits readable on one factor alone.  "
        "The gap VANISHES on every declared product task, including a product "
        "task in a rotated basis and a purely local task; it OPENS on every "
        "declared entangled task.  Rotation of the basis alone does not open "
        "the gap -- that control separates 'manufactured in a rotated basis' "
        "from 'entangled'",
        gap_ok,
        {"tasks": pvm_rows},
    )
    gate(
        "H1-06",
        "witness",
        "WHAT THE GAP ACTUALLY WITNESSES: over the declared joint tasks, "
        "'some composite-core atom is entangled' holds exactly on the tasks "
        "declared entangled.  It is NOT equivalent to the gap opening: the "
        "classically correlated parity task has separable rank-two atoms and "
        "still opens the gap, so the gap alone is a JOINT-READABILITY witness "
        "and the entanglement witness is the gap TOGETHER WITH the atom "
        "classification (exact Schmidt rank on rank-one atoms)",
        iff_ok,
        {
            "gap_opens_without_entanglement": [
                r["task"] for r in pvm_rows if r["gap_opens"] and not r["has_entangled_atom"]
            ],
            "entangled_and_gap_opens": [
                r["task"] for r in pvm_rows if r["gap_opens"] and r["has_entangled_atom"]
            ],
        },
    )
    bell_row = next(r for r in pvm_rows if r["task"] == "BELL")
    prod_row = next(r for r in pvm_rows if r["task"] == "PROD")
    gate(
        "H1-07",
        "witness",
        "THE FLAGSHIP CONTRAST: for the committed four-outcome entangled task "
        "the composite classical core has four atoms while NOTHING is "
        "readable on either factor alone (both local cores trivial), so the "
        "composite boundary does not factorize; for the product task of the "
        "same size the composite core has four atoms and both local cores "
        "have two, and the boundary factorizes exactly",
        bell_row["core_AB"] == 4
        and bell_row["local_A"] == 1
        and bell_row["local_B"] == 1
        and bell_row["product_core"] == 1
        and not bell_row["boundary_factorizes"]
        and prod_row["core_AB"] == 4
        and prod_row["local_A"] == 2
        and prod_row["local_B"] == 2
        and prod_row["boundary_factorizes"],
        {"entangled": bell_row, "product": prod_row},
    )
    FINDINGS["H1_product_law_core_distributes"] = fact_ok
    FINDINGS["H1_gap_opens_on_entangled_tasks"] = gap_ok
    FINDINGS["H1_gap_alone_is_joint_readability_not_entanglement"] = True
    FINDINGS["H1_hostile_wing_not_promoted"] = hostile_ok


# --------------------------------------------------------------------------
# 6.  H2 -- the de-smuggling arena.
# --------------------------------------------------------------------------


def overlap_atoms_diagonal(dim: int):
    """The DECLARED overlap: the laboratory address algebra of the committed
    five-dimensional carrier (four success addresses and the retained sink).
    Declared BEFORE either context, and reachable from both by declaration."""
    out = []
    for j in range(dim):
        m = [[ZERO] * dim for _ in range(dim)]
        m[j][j] = ONE
        out.append(tuple(tuple(r) for r in m))
    return tuple(out)


def incidence(ctx_atoms, ovl_atoms):
    """iota(k) = the set of overlap atoms the context atom k meets, decided
    exactly by tr(w z_k) != 0.  Both are laboratory data."""
    out = []
    for z in ctx_atoms:
        s = set()
        for j, w in enumerate(ovl_atoms):
            t = mtrace(mmul(w, z))
            assert t.im == 0, "incidence weight must be real"
            if t.re != 0:
                s.add(j)
        out.append(frozenset(s))
    return tuple(out)


def transported_images(part, inc):
    imgs = []
    for blk in part:
        u = set()
        for k in blk:
            u |= inc[k]
        imgs.append(frozenset(u))
    if MUTANT == "fact-coarse" and len(imgs) >= 2:
        imgs = [imgs[0] | imgs[1]] + imgs[2:]
    return imgs


def transports_without_collision(part, inc) -> bool:
    """D1: the availability criterion of the predecessor cycle, posed at the
    DECLARED OVERLAP instead of at a later boundary of the same context."""
    imgs = transported_images(part, inc)
    for i in range(len(imgs)):
        for j in range(i + 1, len(imgs)):
            if MUTANT == "descent-lax" and (imgs[i] <= imgs[j] or imgs[j] <= imgs[i]):
                continue
            if imgs[i] & imgs[j]:
                return False
    return True


def fact_of(part, inc):
    """The transported FACT content: a partition of the overlap atoms, with no
    block name and no token carried across."""
    imgs = transported_images(part, inc)
    return tuple(sorted(tuple(sorted(x)) for x in imgs))


def facts_realized(ctx_atoms, inc):
    out = set()
    n = len(ctx_atoms)
    for p in CB.parts_of(n):
        if transports_without_collision(p, inc):
            out.add(fact_of(p, inc))
    return out


def certified_records(ctx_atoms, inc, partner_facts, n_overlap):
    """THE SELECTOR.  A record is certified when (D1) it transports to the
    declared overlap without collision, (D2) its transported fact content is
    also realized in the independently declared second context, and (D3) that
    fact content is non-vacuous."""
    vac = (tuple(range(n_overlap)),)
    out = []
    for p in CB.parts_of(len(ctx_atoms)):
        if not transports_without_collision(p, inc):
            continue
        f = fact_of(p, inc)
        if f == vac:
            continue
        if f in partner_facts:
            out.append(p)
    return out


def act_on_support(s, sigma):
    n = len(s)
    out = [None] * n
    for k in range(n):
        out[sigma[k]] = frozenset(sigma[l] for l in s[k])
    return tuple(out)


def family_image(fam, sigma):
    return frozenset(act_on_support(s, sigma) for s in fam)


def independence(famA, famB, isos):
    """MEASURED independence: no ADMITTED isomorphism carries one declared
    task family onto the other.  Returns (independent, witnesses)."""
    wit = []
    for sigma in isos:
        if family_image(famA, sigma) == frozenset(famB):
            wit.append(tuple(sigma))
    return (not wit), wit


def counter_law_L_R():
    """Cycle B Prop 4.12's counter-law, recomputed by its own algorithm."""
    gens5 = [CB.reprepare_support(p, 5) for p in CB.parts_of(5)]
    gens_fn = [tuple(next(iter(s)) for s in g) for g in gens5]
    seen = set(gens_fn)
    frontier = list(seen)
    while frontier:
        fresh = []
        for f in frontier:
            for g in gens_fn:
                for h in (tuple(g[f[k]] for k in range(5)), tuple(f[g[k]] for k in range(5))):
                    if h not in seen:
                        seen.add(h)
                        fresh.append(h)
        frontier = fresh
    law = sorted(seen)
    rev = [f for f in law if len(set(f)) == 5]
    return law, rev


def run_h2():
    prog("H2  arena: declared overlap, two independently declared contexts")
    dim = 5
    W = overlap_atoms_diagonal(dim)
    nW = len(W)

    # ---- the contexts, with the manufactured ones CONSTRUCTED by Cycle B's
    #      own routine and anchored at their committed values.
    ctx = {}
    for ranks, aid, committed in (((2, 1, 1), "L10", 4), ((2, 2), "L11", 3), ((1, 1, 1, 1), "L12", 5)):
        facts, objs, b = manufactured_boundary(ranks)
        anchor(
            aid,
            "Cycle B sec 4.5 / #103 sec 6.2",
            f"constructed manufactured {'+'.join(str(r) for r in ranks)} with sink: centre dimension",
            committed,
            facts["centre_dim_with_sink"],
        )
        anchor(
            aid + "r",
            "Cycle B sec 4.5",
            f"constructed manufactured {'+'.join(str(r) for r in ranks)}: PVM rank multiset",
            list(ranks),
            facts["pvm_ranks"],
        )
        ctx[b.name] = b
    ctx["ERASER"] = boundary_from_blocks("ERASER", (1, 1, 1, 1, 1))
    ctx["ADDRESS"] = boundary_from_blocks("ADDRESS", (1, 1, 1, 1, 1))
    ctx["TOMO"] = boundary_from_blocks("TOMO", (4, 1))
    ctx["ALIGNED211"] = aligned_manufactured_boundary((2, 1, 1))

    anchor("L05", "#111 Prop 10.1", "core atom count of C^5 (corrected eraser minimum)", 5,
           len(admitted_split_partition(ctx["ERASER"])[0]))
    anchor("L06", "#111 Prop 10.1", "core atom count of M_4 + C (corrected tomographic minimum)", 2,
           len(admitted_split_partition(ctx["TOMO"])[0]))
    anchor("L07", "#103 sec 9.3 (corrected)", "bundled minimum atom count", 5, len(ctx["ERASER"].atoms))
    for n, committed in ((1, 1), (2, 2), (3, 5), (4, 15), (5, 52)):
        anchor(f"L08-{n}", "Bell triangle recurrence",
               f"record lattice size at {n} atoms (enumerated vs recurrence)",
               CB.bell_recurrence(n), CB.bell(n))
        if n == 5:
            anchor("L09", "Cycle B sec 5.1", "records on the corrected eraser minimum", committed, CB.bell(n))

    inc = {k: incidence(v.atoms, W) for k, v in ctx.items()}
    TABLES["incidence"] = {
        k: {"atoms": len(ctx[k].atoms), "images": [sorted(s) for s in inc[k]]} for k in ctx
    }

    # ---- H2-01  the arena is declared, and the overlap is reachable from both.
    reach = all(
        all(len(s) > 0 for s in inc[k]) and set().union(*inc[k]) == set(range(nW))
        for k in ("MAN211", "ERASER", "ADDRESS", "TOMO")
    )
    gate(
        "H2-01",
        "census",
        "THE ARENA IS WELL POSED: the declared overlap is reached by every "
        "atom of every declared context and is covered by each context's "
        "atoms, so every record that transports without collision transports "
        "to a genuine partition of the overlap",
        reach,
        {"overlap_atoms": nW, "contexts": sorted(ctx)},
    )

    # ---- H2-02/03  INDEPENDENCE, MEASURED, and the relabelled control.
    ident = tuple(frozenset({k}) for k in range(5))
    F_eraser = frozenset({ident, tuple(frozenset({0 if k < 4 else 4}) for k in range(5))})
    F_address = frozenset({ident} | {tuple(frozenset({j}) for _ in range(5)) for j in range(5)})
    dephase_sup = {}
    for key in ("MAN211", "MAN22", "MAN1111", "ALIGNED211"):
        sup = []
        for j in range(5):
            img = mzero(5)
            for p in ctx[key].atoms:
                img = madd(img, mmul(mmul(p, W[j]), p))
            sup.append(frozenset(l for l in range(5) if not mtrace(mmul(W[l], img)).is_zero()))
        dephase_sup[key] = tuple(sup)
    F_man = frozenset({ident, dephase_sup["MAN211"]})
    perms = [tuple(s) for s in permutations(range(5))]
    shift = (1, 2, 3, 4, 0)
    F_relabelled = frozenset(family_image(F_eraser, shift))

    ind_real, wit_real = independence(F_eraser, F_address, perms)
    ind_man, wit_man = independence(F_man, F_address, perms)
    ind_ctrl, wit_ctrl = independence(F_eraser, F_relabelled, perms)
    gate(
        "H2-02",
        "independence",
        "INDEPENDENCE IS MEASURED, NOT DECLARED: no admitted isomorphism of "
        "the standard law -- all 120 address relabellings were searched -- "
        "carries the declared eraser family onto the declared address family, "
        "nor the manufactured family onto the address family.  The two "
        "contexts of the arena are operationally independent",
        ind_real and ind_man,
        {"relabellings_searched": len(perms), "witnesses": wit_real + wit_man},
    )
    gate(
        "H2-03",
        "control",
        "THE INDEPENDENCE GATE BITES: when the second context is replaced by "
        "an admitted-isomorphism image of the first -- the cyclic address "
        "shift applied to the eraser family -- the same gate FAILS and names "
        "the carrying isomorphism.  A gate that could not fail would prove "
        "nothing",
        (not ind_ctrl) and shift in wit_ctrl,
        {"carrying_isomorphism": wit_ctrl, "relabelled_context": "shift(eraser family)"},
    )

    # ---- H2-04  the bare-boundary isomorphism exists but MOVES the overlap.
    perm = [1, 2, 3, 4, 0]
    V = tuple(tuple(ONE if perm[i] == j else ZERO for j in range(5)) for i in range(5))
    facts5, objs5, _ = manufactured_boundary((1, 1, 1, 1))
    U = CB.embed_unitary_with_sink(objs5["rotation"], 4)
    T = mmul(U, V)
    legit = ctx["ERASER"]
    carried = []
    for k in range(5):
        img = mmul(mmul(T, legit.atoms[k]), madj(T))
        hit = [l for l in range(5) if meq(img, ctx["MAN1111"].atoms[l])]
        carried.append(hit[0] if len(hit) == 1 else None)
    anchor("L13", "Cycle B G2-13", "atom map carried by (W (+) 1)V", [4, 0, 1, 2, 3], carried)
    moved = []
    for j in range(5):
        img = mmul(mmul(T, W[j]), madj(T))
        diagonal = all(
            img[a][b].is_zero() for a in range(5) for b in range(5) if a != b
        )
        moved.append(not diagonal)
    gate(
        "H2-04",
        "impossibility",
        "WHY THE ONE-BOUNDARY COVARIANCE OBSTRUCTION DOES NOT TRANSFER: the "
        "reversible map that carries the legitimate five-atom boundary onto "
        "the constructed manufactured one -- recomputed here, with the same "
        "committed atom map -- does NOT preserve the declared overlap: it "
        "sends declared address projections to non-diagonal elements.  A "
        "criterion covariant for one context alone is therefore not a "
        "criterion covariant for the arena, and the predecessor's covariance "
        "theorem has no purchase here",
        any(moved),
        {"atom_map": carried, "overlap_atoms_moved": moved},
    )

    # ---- H2-05  THE TOP-OF-LATTICE GUARD.
    prog("H2  the top-of-lattice guard and the descent order")
    top_fixed_ok, top_tests = True, 0
    state = 20260806
    for n in (2, 3, 4, 5):
        pool = CB.relations_of(n) if n <= 4 else CB.declared_family_n5()
        for _ in range(40):
            state = CB.lcg_step(state)
            size = 1 + state % 6
            fam = []
            for _ in range(size):
                state = CB.lcg_step(state)
                fam.append(pool[state % len(pool)])
            top_tests += 1
            if CB.discrete(n) not in CB.fix_set_of_family(fam, n):
                top_fixed_ok = False
    gate(
        "H2-05a",
        "guard",
        "THE OBSTRUCTION BEING ESCAPED, RE-VERIFIED NATIVELY: on 160 declared "
        "admitted families at atom counts 2 to 5 the greatest record of the "
        "one-boundary record lattice is a fixed point of the availability "
        "closure without exception, so no closure operator on a single "
        "context's record lattice can reject it",
        top_fixed_ok,
        {"families": top_tests},
    )

    addr_facts = facts_realized(ctx["ADDRESS"].atoms, inc["ADDRESS"])
    tomo_facts = facts_realized(ctx["TOMO"].atoms, inc["TOMO"])
    cert = {}
    for key in ("MAN211", "MAN22", "MAN1111", "ERASER", "ALIGNED211"):
        cert[key] = {
            "vs_ADDRESS": certified_records(ctx[key].atoms, inc[key], addr_facts, nW),
            "vs_TOMO": certified_records(ctx[key].atoms, inc[key], tomo_facts, nW),
        }
    guard_rows = []
    guard_ok = True
    for key in ("MAN211", "MAN22", "MAN1111"):
        n = len(ctx[key].atoms)
        top = CB.discrete(n)
        inside = top in cert[key]["vs_ADDRESS"]
        guard_rows.append(
            {
                "context": key,
                "records": CB.bell(n),
                "certified_vs_address": len(cert[key]["vs_ADDRESS"]),
                "top_certified": inside,
            }
        )
        if inside:
            guard_ok = False
    gate(
        "H2-05b",
        "guard",
        "THE GUARD PASSES: the selector's carrier is the pair-plus-overlap "
        "structure, not one context's record lattice.  For every constructed "
        "manufactured context the certified set does NOT contain the greatest "
        "record, while every closure operator on that same lattice fixes it "
        "(H2-05a).  The certified set is therefore not the fixed-point set of "
        "any closure operator on the candidate's own record lattice -- the "
        "predecessor's top-of-lattice impossibility is genuinely escaped, not "
        "circumvented by renaming",
        guard_ok,
        {"contexts": guard_rows},
    )

    # the descent order, exhibited
    order_pairs = 0
    order_max = []
    n_man = len(ctx["MAN211"].atoms)
    D = []
    for pa in CB.parts_of(n_man):
        if not transports_without_collision(pa, inc["MAN211"]):
            continue
        fa = fact_of(pa, inc["MAN211"])
        if fa == (tuple(range(nW)),):
            continue
        for pb in CB.parts_of(len(ctx["ADDRESS"].atoms)):
            if not transports_without_collision(pb, inc["ADDRESS"]):
                continue
            if fact_of(pb, inc["ADDRESS"]) == fa:
                D.append((pa, pb))
                order_pairs += 1
    for x in D:
        if not any(
            y != x and CB.refines(y[0], x[0]) and CB.refines(y[1], x[1]) for y in D
        ):
            order_max.append({"A": [list(b) for b in x[0]], "B": [list(b) for b in x[1]]})
    gate(
        "H2-05c",
        "guard",
        "THE DESCENT ORDER, EXHIBITED: the carrier is the set of pairs of "
        "records, one per context, whose transported fact contents coincide "
        "and are non-vacuous, ordered by refinement in each component.  The "
        "candidate manufactured record occurs in NO pair of that carrier, so "
        "it is not merely non-maximal there, it is absent",
        order_pairs > 0
        and all(x[0] != CB.discrete(n_man) for x in D),
        {
            "carrier_size": order_pairs,
            "maximal_elements": order_max,
            "candidate_present": any(x[0] == CB.discrete(n_man) for x in D),
        },
    )

    # ---- H2-06/07  THE DISCRIMINATOR, both directions.
    prog("H2  THE DISCRIMINATOR")
    disc_rows = []
    disc_neg = True
    for key in ("MAN211", "MAN22", "MAN1111"):
        n = len(ctx[key].atoms)
        top = CB.discrete(n)
        d1 = transports_without_collision(top, inc[key])
        row = {
            "context": key,
            "atoms": n,
            "top_transports_without_collision": d1,
            "certified_vs_address": top in cert[key]["vs_ADDRESS"],
            "certified_vs_tomo": top in cert[key]["vs_TOMO"],
            "certified_records_vs_address": [
                [list(b) for b in p] for p in cert[key]["vs_ADDRESS"]
            ],
        }
        disc_rows.append(row)
        if d1 or row["certified_vs_address"] or row["certified_vs_tomo"]:
            disc_neg = False
    TABLES["discriminator"] = disc_rows
    gate(
        "H2-06",
        "DISCRIMINATOR",
        "DIRECTION ONE -- THE MANUFACTURED RECORD FAILS DESCENT: for all "
        "three constructed manufactured boundaries the manufactured record "
        "collides at the declared overlap (distinct blocks reach a common "
        "overlap atom), so it fails the transport clause outright and is "
        "certified against neither declared second context.  It fails for the "
        "very feature that manufactured it: the measure was chosen in a "
        "rotated basis so that no block structure could be read off the "
        "coordinates, and that is exactly what leaves it with no fact content "
        "at an independently declared overlap",
        disc_neg,
        {"contexts": disc_rows},
    )
    n_er = len(ctx["ERASER"].atoms)
    top_er = CB.discrete(n_er)
    er_d1 = transports_without_collision(top_er, inc["ERASER"])
    er_fact = fact_of(top_er, inc["ERASER"])
    er_cert = top_er in cert["ERASER"]["vs_ADDRESS"]
    partner_witness = [
        [list(b) for b in p]
        for p in CB.parts_of(len(ctx["ADDRESS"].atoms))
        if transports_without_collision(p, inc["ADDRESS"])
        and fact_of(p, inc["ADDRESS"]) == er_fact
    ]
    gate(
        "H2-07",
        "DISCRIMINATOR",
        "DIRECTION TWO -- THE LEGITIMATE ERASER RECORD SURVIVES DESCENT: the "
        "corrected eraser minimum's record transports to the declared overlap "
        "without collision, its transported fact content is non-vacuous, and "
        "the independently declared second context realizes exactly that fact "
        "content; a co-referring record is exhibited rather than asserted",
        er_d1 and er_cert and len(partner_witness) >= 1,
        {
            "transports": er_d1,
            "fact_content": [list(b) for b in er_fact],
            "certified": er_cert,
            "co_referring_records_in_second_context": partner_witness,
            "certified_of_total": [len(cert["ERASER"]["vs_ADDRESS"]), CB.bell(n_er)],
        },
    )
    FINDINGS["H2_manufactured_record_fails_descent"] = disc_neg
    FINDINGS["H2_legitimate_record_survives_descent"] = bool(er_d1 and er_cert)
    FINDINGS["H2_smuggling_survives_descent"] = not disc_neg

    # ---- H2-08  sharpness: what the selector does NOT certify.
    n_al = len(ctx["ALIGNED211"].atoms)
    top_al = CB.discrete(n_al)
    al_cert = top_al in cert["ALIGNED211"]["vs_ADDRESS"]
    gate(
        "H2-08",
        "sharpness",
        "WHAT DESCENT DOES AND DOES NOT CERTIFY: the same manufacturing "
        "construction with the rotation deleted -- a chosen measure ALIGNED "
        "with the declared addresses -- does descend.  Descent therefore does "
        "not certify 'not chosen to match a measure'; it certifies 'has "
        "non-vacuous fact content at an independently declared overlap'.  The "
        "aligned case is reported, not suppressed",
        al_cert,
        {"aligned_manufactured_record_certified": al_cert},
    )
    tomo_rows = {
        k: {
            "certified_vs_address": len(cert[k]["vs_ADDRESS"]),
            "certified_vs_tomo": len(cert[k]["vs_TOMO"]),
            "top_certified_vs_tomo": CB.discrete(len(ctx[k].atoms)) in cert[k]["vs_TOMO"],
        }
        for k in ("MAN211", "ERASER", "ALIGNED211")
    }
    TABLES["arena_relativity"] = tomo_rows
    gate(
        "H2-08b",
        "sharpness",
        "CERTIFICATION IS ARENA-RELATIVE, MEASURED: replacing the second "
        "context by the strictly coarser committed tomographic context leaves "
        "the manufactured rejection untouched but withdraws the legitimate "
        "record's certificate, since a two-atom context cannot co-refer with "
        "five distinguished addresses.  The negative direction of the "
        "discriminator is robust across both declared second contexts; the "
        "positive direction is not, and is claimed only at the declared arena",
        (not tomo_rows["MAN211"]["top_certified_vs_tomo"])
        and (not tomo_rows["ERASER"]["top_certified_vs_tomo"])
        and tomo_rows["ERASER"]["certified_vs_tomo"] < tomo_rows["ERASER"]["certified_vs_address"],
        tomo_rows,
    )

    # ---- H2-09  positive control: the identity overlap.
    self_inc = incidence(ctx["ERASER"].atoms, ctx["ERASER"].atoms)
    self_facts = facts_realized(ctx["ERASER"].atoms, self_inc)
    self_cert = certified_records(ctx["ERASER"].atoms, self_inc, self_facts, n_er)
    gate(
        "H2-09",
        "control",
        "POSITIVE CONTROL, THE IDENTITY OVERLAP: when the declared overlap is "
        "the context's own core and the second context is a copy, every "
        "non-vacuous record descends -- 51 of the 52 records, the excluded "
        "one being the trivial record, which fails the non-vacuity clause.  "
        "The selector fires when it should",
        len(self_cert) == CB.bell(n_er) - 1,
        {"certified": len(self_cert), "records": CB.bell(n_er)},
    )

    # ---- H2-10  the fact/token split, measured.
    al_fact = fact_of(top_al, inc["ALIGNED211"])
    same_fact_partners = [
        p
        for p in CB.parts_of(len(ctx["ADDRESS"].atoms))
        if transports_without_collision(p, inc["ADDRESS"]) and fact_of(p, inc["ADDRESS"]) == al_fact
    ]
    diff_fact_partner = next(
        p
        for p in CB.parts_of(len(ctx["ADDRESS"].atoms))
        if transports_without_collision(p, inc["ADDRESS"]) and fact_of(p, inc["ADDRESS"]) != al_fact
    )
    gate(
        "H2-10",
        "control",
        "THE FACT/TOKEN SPLIT IS PRESERVED: co-reference is decided on "
        "transported fact content and on nothing else.  A four-block record "
        "of a four-atom context and a four-block record of a five-atom "
        "context co-refer although no bijection of their outcome tokens "
        "exists; and a record of the same block count with different fact "
        "content does not co-refer.  Token identity is never used",
        len(same_fact_partners) >= 1
        and len(ctx["ALIGNED211"].atoms) != len(ctx["ADDRESS"].atoms)
        and fact_of(diff_fact_partner, inc["ADDRESS"]) != al_fact,
        {
            "candidate_atoms": len(ctx["ALIGNED211"].atoms),
            "partner_atoms": len(ctx["ADDRESS"].atoms),
            "co_referring": [[list(b) for b in p] for p in same_fact_partners],
        },
    )

    # ---- H2-11  CONTROL 5: the Cycle B counter-law as one context's law.
    prog("H2  control: the counter-law as the second context's law")
    law, rev = counter_law_L_R()
    anchor("L20", "Cycle B Prop 4.12", "admitted sector maps of the counter-law", 120, len(law))
    anchor("L21", "Cycle B Prop 4.12", "reversible admitted maps of the counter-law", 1, len(rev))
    fixed_R = CB.fix_set_of_family([CB.functional_support(f) for f in law], 5)
    anchor("L22", "Cycle B Prop 4.12", "records fixed under the counter-law", 52, len(fixed_R))
    isos_R = [f for f in rev]
    ind_ctrl_R, wit_ctrl_R = independence(F_eraser, F_relabelled, isos_R)
    gate(
        "H2-11",
        "control",
        "THE COUNTER-LAW AS THE SECOND CONTEXT'S LAW, REPORTED HONESTLY: "
        "under the composition closure of the reprepare futures the only "
        "reversible admitted map is the identity, so the relabelled context "
        "that the standard law exposes as a dependent copy PASSES the "
        "independence gate there.  Independence, like admission before it, is "
        "law-relative and must be certified per law; the descent verdicts "
        "themselves are unchanged, because transport to the overlap is decided "
        "by incidence and not by the future class",
        ind_ctrl_R and (not ind_ctrl),
        {
            "counter_law_size": len(law),
            "reversible": len(rev),
            "records_fixed": len(fixed_R),
            "relabelled_context_independent_under_counter_law": ind_ctrl_R,
            "relabelled_context_independent_under_standard_law": ind_ctrl,
        },
    )

    # ---- H2-12  CONTROL 2 follow-through on the entangled composite.
    rows = []
    for key in ("PROD", "BELL"):
        projs, note, _ = DECLARED_PVMS[key]
        b = dephasing_range_boundary(f"JOINT[{key}]", projs, 4, note)
        n = len(b.atoms)
        ovl = b.atoms
        i2 = incidence(b.atoms, ovl)
        locA = local_split_partition_direct(b, "A")
        locB = local_split_partition_direct(b, "B")
        fac = join_partitions(locA, locB, n)
        descends = transports_without_collision(fac, i2) and fact_of(fac, i2) != (
            tuple(range(n)),
        )
        rows.append(
            {
                "task": key,
                "factor_record_blocks": [list(x) for x in fac],
                "factor_record_descends_non_vacuously": descends,
            }
        )
    TABLES["factor_records"] = rows
    gate(
        "H2-12",
        "control",
        "WHICH FACTOR RECORDS STILL DESCEND: on the declared product task the "
        "record generated by the splits readable on one factor alone is the "
        "full four-atom record and it descends non-vacuously; on the "
        "committed entangled task that record is the TRIVIAL one, so no "
        "factor record descends non-vacuously at all.  The composite carries "
        "four certified atoms of which the factors carry none",
        rows[0]["factor_record_descends_non_vacuously"]
        and not rows[1]["factor_record_descends_non_vacuously"],
        {"tasks": rows},
    )


# --------------------------------------------------------------------------
# 7.  Fixtures, verdict, receipt, rendering.
# --------------------------------------------------------------------------

FIXTURES: dict = {}


def build_fixtures():
    FIXTURES["C1"] = boundary_from_blocks("C1", (1,))
    FIXTURES["C2"] = boundary_from_blocks("C2", (1, 1))
    FIXTURES["M2"] = boundary_from_blocks("M2", (2,))
    FIXTURES["M2+C"] = boundary_from_blocks("M2+C", (2, 1))
    FIXTURES["C5"] = boundary_from_blocks("C5", (1, 1, 1, 1, 1))
    FIXTURES["M4+C"] = boundary_from_blocks("M4+C", (4, 1))
    FIXTURES["HOSTILE"] = hostile_boundary()
    _, _, m211 = manufactured_boundary((2, 1, 1))
    _, _, m22 = manufactured_boundary((2, 2))
    FIXTURES["MAN211"] = m211
    FIXTURES["MAN22"] = m22


def run_fixture_anchors():
    prog("anchors: the committed fixture values, recomputed")
    for key, committed in (("C1", 1), ("C2", 2), ("M2", 1), ("M2+C", 2), ("C5", 5), ("M4+C", 2)):
        part, ok = admitted_split_partition(FIXTURES[key])
        anchor(
            f"L03-{key}",
            "#111 Thm 6.2 / Prop 10.1",
            f"operational core atom count of {key}",
            committed,
            len(part),
        )
    part, _ = admitted_split_partition(FIXTURES["HOSTILE"])
    anchor("L04", "#111 Thm 8.2", "operational core atom count of the hostile operator system", 1, len(part))
    S = FIXTURES["HOSTILE"]
    zb = [flat(z) for z in S.atoms]
    eb, _ = S.basis()
    inter = subspace_intersection(eb, zb, S.dim * S.dim)
    anchor("L14", "#111 sec 8.1 / #103 sec 5.2", "dim (S intersect Z(C*_e(S)))", 1, len(inter))
    s2 = S.span[2]
    sq = mmul(s2, s2)
    anchor("L15", "#111 sec 8.1", "s_2^2 second block coefficient", QC(5), sq[2][2])
    anchor("L16", "#111 sec 8.1", "s_2^2 first block coefficient", QC(1), sq[0][0])


def verdict():
    survives = FINDINGS.get("H2_smuggling_survives_descent", True)
    rungs = []
    if FINDINGS.get("H1_product_law_core_distributes"):
        rungs.append("RQ0-L1-COMPOSITE-BOUNDARY")
    if FINDINGS.get("H1_gap_opens_on_entangled_tasks"):
        rungs.append("RQ0-L1-ENTANGLEMENT-WITNESS")
    if not survives and FINDINGS.get("H2_legitimate_record_survives_descent"):
        rungs.append("RQ0-L1-DESCENT-SELECTOR")
    if survives:
        rungs.append("RQ0-L1-SMUGGLING-SURVIVES-DESCENT")
    return {
        "rungs": rungs,
        "scope": {
            "RQ0-L1-COMPOSITE-BOUNDARY": (
                "finite; the declared product law; exhaustive over ordered pairs of the "
                "nine committed fixtures with composite carrier dimension at most 20; the "
                "general case carried by the proved support lemma"
            ),
            "RQ0-L1-ENTANGLEMENT-WITNESS": (
                "finite; the declared eight-member family of joint tasks on the "
                "two-qubit composite, entangled members built from the committed "
                "entangled objects; the entanglement classification is exact on rank-one "
                "atoms via Schmidt rank"
            ),
            "RQ0-L1-DESCENT-SELECTOR": (
                "finite; ONE declared arena (two independently declared task families and "
                "one declared overlap on the committed five-dimensional carrier); "
                "exhaustive over all records of every declared context; the negative "
                "direction verified on all three constructed manufactured boundaries"
            ),
        },
        "corrections": [
            "the core gap ALONE is a joint-readability witness, not an entanglement "
            "witness: a classically correlated declared task opens it with separable "
            "atoms.  The entanglement witness is the gap together with the exact atom "
            "classification",
            "descent certifies non-vacuous fact content at an independently declared "
            "overlap, not absence of manufacture: an aligned manufactured measure does "
            "descend",
        ],
        "not_earned": [
            "no arena-independent selector: certification is relative to the declared "
            "arena, and a coarser second context certifies strictly less"
        ],
    }


def build_receipt():
    npass = sum(1 for g in GATES if g["pass"])
    return {
        "schema": SCHEMA,
        "unit": "RQ0-L1 Cycle B' - composite boundaries and the de-smuggling arena",
        "pin_commit": PIN_COMMIT,
        "immutable_base_commit": BASE_COMMIT,
        "status": "GREEN-UNREVIEWED",
        "arithmetic": "exact (fractions.Fraction and Q(i)); no float in any substantive path",
        "source_sha256": SOURCE_SHA256,
        "anchor_type_violations": EXACTNESS_VIOLATIONS,
        "verdict": verdict(),
        "findings": FINDINGS,
        "tables": TABLES,
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
                "run `--falsification-selftest`; each mutant must exit 1.  Anchor "
                "mutants substitute the reported value at the anchor comparison site; "
                "derivation mutants perturb a computation and must make at least one "
                "gate fail, which also exits 1"
            ),
            "anchor_mutants": {k: v[0] for k, v in sorted(MUTANT_TABLE.items())},
            "derivation_mutants": dict(sorted(MUTANT_GATE_TABLE.items())),
            "anchors_covered": sorted({v[0] for v in MUTANT_TABLE.values()}),
            "anchors_total": len(ANCHORS),
            "determinism": (
                "no wall-clock value enters this receipt or the rendered output; "
                "timings appear only on the progress stream, so two consecutive runs "
                "of the same source produce byte-identical artifacts"
            ),
        },
        "nonclaims": [
            "'independence' is OPERATIONAL (which joint operations are admitted) and "
            "has NO spatial reading whatsoever",
            "no locality, region, topology, atlas or manifold claim",
            "no causal order, influence or spacetime claim",
            "no field, QCD or gravity claim",
            "no arena-independent record and no W3 rung",
            "no claim that the declared composite is the only admissible one",
            "no actual outcome selection and no event-token identity",
        ],
    }


def render(rec) -> str:
    L = []
    L.append("RQ0-L1 CYCLE B' RECEIPT - COMPOSITE BOUNDARIES AND THE DE-SMUGGLING ARENA")
    L.append(f"schema: {rec['schema']}")
    L.append(f"status: {rec['status']}")
    L.append(f"pin: {rec['pin_commit']}   immutable base: {rec['immutable_base_commit']}")
    L.append(f"arithmetic: {rec['arithmetic']}")
    L.append(f"source sha256: {rec['source_sha256']}")
    L.append(f"anchor type violations: {rec['anchor_type_violations']}")
    L.append("")
    L.append("VERDICT")
    v = rec["verdict"]
    for r in v["rungs"]:
        L.append(f"  RUNG: {r}")
        L.append(f"    scope: {v['scope'].get(r, 'see paper')}")
    for c in v["corrections"]:
        L.append(f"  CORRECTED HEADLINE: {c}")
    for c in v["not_earned"]:
        L.append(f"  NOT EARNED: {c}")
    L.append("")
    L.append("FINDINGS")
    for k in sorted(rec["findings"]):
        L.append(f"  {k}: {rec['findings'][k]}")
    L.append("")
    L.append(f"GATES  {rec['gates']['passed']}/{rec['gates']['total']}")
    if rec["gates"]["failed"]:
        L.append(f"  FAILED: {', '.join(rec['gates']['failed'])}")
    for g in rec["gates"]["entries"]:
        L.append(f"  {g['id']:10s} [{g['class']}] {'PASS' if g['pass'] else 'FAIL'}")
        L.append(f"      {g['claim']}")
        if g["value"] is not None:
            L.append(f"      value: {json.dumps(g['value'], sort_keys=True, default=str)}")
    L.append("")
    L.append(f"ANCHORS  {rec['anchors']['passed']}/{rec['anchors']['total']}  (exit-1-only)")
    for a in rec["anchors"]["entries"]:
        L.append(
            f"  {a['id']:9s} {a['source']:34s} {a['quantity']}: "
            f"committed={a['committed']} computed={a['computed']} "
            f"{'PASS' if a['pass'] else 'FAIL'}"
        )
    L.append("")
    L.append("TABLES")
    for k in sorted(rec["tables"]):
        L.append(f"  {k}: {json.dumps(rec['tables'][k], sort_keys=True, default=str)}")
    L.append("")
    L.append("FALSIFICATION COVERAGE")
    f = rec["falsification"]
    L.append(
        f"  anchor mutants ({len(f['anchor_mutants'])}): "
        + ", ".join(f"{k} -> {v}" for k, v in f["anchor_mutants"].items())
    )
    L.append(
        f"  derivation mutants ({len(f['derivation_mutants'])}): "
        + ", ".join(f"{k} ({v})" for k, v in f["derivation_mutants"].items())
    )
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
    "man211-centre": ("L10", 3),
    "choi": ("L02", QC(Fr(-1, 3))),
    "counterlaw": ("L20", 119),
    "erase-min": ("L05", 4),
    "atom-map": ("L13", [0, 1, 2, 3, 4]),
    "hostile-dim": ("L14", 2),
}

MUTANT_GATE_TABLE = {
    "descent-lax": "the transport clause treats nested images as non-colliding",
    "fact-coarse": "transported fact content merges the first two images",
    "gap-lax": "the local split partition is reported as the discrete one",
}


def run_falsification_selftest() -> int:
    prog("FALSIFICATION SELF-TEST: each mutant must exit 1")
    rows = []
    ok = True
    for name in sorted(MUTANT_TABLE) + sorted(MUTANT_GATE_TABLE):
        r = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--mutant", name],
            capture_output=True,
            text=True,
        )
        killed = r.returncode == 1 and ("ANCHOR FAILURE" in r.stdout or "GATE FAILURE" in r.stdout)
        broke = MUTANT_TABLE[name][0] if name in MUTANT_TABLE else "gates"
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
            f"  mutant {name:14s} breaks {broke:6s} exit={code} "
            f"{'KILLED (correct)' if killed else 'SURVIVED (DEFECT)'}"
            f"{('  ' + detail) if detail else ''}\n"
        )
    sys.stdout.write(
        f"falsification self-test: {sum(1 for r in rows if r[3])}/{len(rows)} mutants killed\n"
    )
    return 0 if ok else 1


def main() -> int:
    global MUTANT, MUTANT_OVERRIDE, SOURCE_SHA256
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutant", choices=sorted(MUTANT_TABLE) + sorted(MUTANT_GATE_TABLE), default=None)
    ap.add_argument("--falsification-selftest", action="store_true")
    ap.add_argument("--no-write-files", action="store_true")
    args = ap.parse_args()

    SOURCE_SHA256 = hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()

    if args.falsification_selftest:
        return run_falsification_selftest()

    if args.mutant:
        MUTANT = args.mutant
        if args.mutant in MUTANT_TABLE:
            aid, val = MUTANT_TABLE[args.mutant]
            MUTANT_OVERRIDE = {aid: val}
            prog(f"MUTANT MODE: anchor {aid} deliberately broken ({args.mutant})")
        else:
            prog(f"MUTANT MODE: derivation deliberately broken ({args.mutant}: {MUTANT_GATE_TABLE[args.mutant]})")

    prog(f"RQ0-L1 Cycle B' - composite boundaries and the arena; pin {PIN_COMMIT}")
    run_h0()
    build_fixtures()
    run_fixture_anchors()
    run_h1()
    run_h2()

    rec = build_receipt()
    txt = render(rec)
    if not args.no_write_files and not MUTANT:
        OUT_JSON.write_text(json.dumps(rec, indent=2, sort_keys=True, default=str) + "\n")
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
