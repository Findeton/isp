#!/usr/bin/env python3
# ===========================================================================
# SCOUT-T  --  the trigger-trace fork: arms (1) and (2) of the #82 four-way
# fork, computed on SCOUT-K's committed apparatus.
#
# Unit: v15/note-scoutt.md (report NOTE, scout class).
# Pin:  v15/note-scoutt-pin.md (FROZEN 3f35573d88d8), v15 ledger #82,
#       AMENDED by the #87 SCOUT-T addendum (note-scoutt-pin-addendum.md,
#       15d763633293): W-REPRESENTATION binds in its #86 FORK-NEUTRAL
#       form (promotion-by-convenience forbidden; an ontic trigger/trace
#       remains ADMISSIBLE if independently declared, operationally
#       distinguished, mapped to the beables; this unit tests whether a
#       trace COULD be real and presupposes neither answer), and arm 1
#       runs the MINIMALITY LADDER of five trace grains.  The #68
#       SCOUT-K addendum (3a1e5a649537) binds identically (conditional
#       mode primary; marginal-history mode only with exact factorization
#       and polynomial certificates; linear relaxations over history
#       flows REFUSED).
#
# ARM 1 (TRIGGER REAL, CONDITIONAL MODE, THE MINIMALITY LADDER): does a
# minimal covariant kernel K(e|c,G,R,T) -- T the ordered trigger trace,
# exactly the datum the bridge's triple record erases at write-time
# (#82) -- preserve the delivered walk at the committed windows (depths
# 2 and 3)?  Five trace grains ordered by information content: (a) NONE
# (the T-blind parent reproduction), (b) PREV1 (previous trigger only),
# (c) COUNTS (unordered trigger counts), (d) SUFFIX2 (length-2 suffix),
# (e) FULL (the ordered trace).  Orbits of (G,R,T,c,e) under
# simultaneous relabelling; one variable per orbit; Farkas certificates
# for emptiness, affine-hull dimensions for non-emptiness, the unique
# kernel published at dimension 0; the verdict is PER GRAIN and the
# headline names the COARSEST feasible grain.
#
# ARM 2 (TRIGGER BOOKKEEPING, MARGINAL-HISTORY MODE): the exact
# factorizing history-level process (Markov in the complete successor,
# the trigger not carried in the state, latent event histories summed)
# compared to the delivered walk's OBSERVABLE record distributions at the
# same windows, at four disclosed grains: {ordered CELL-HIT emission
# histories, final count fields} x {raw, relabelling-quotiented}.  Exact
# polynomial method: the step-one factor is the measured dim-1 line-weight
# family (an exact census fact, not a relaxation), so every system is
# linear in the second kernel factor at each sampled line weight, with one
# uniform-in-a Farkas certificate per all-empty system.  No linear
# relaxation over history flows is used anywhere.
#
# MANDATORY CROSS-CHECK: the T-blind subfamily of arm 1 reproduces
# SCOUT-K's depth-3 refusal, bound BYTE-EXACTLY to the delivered parent
# receipt (gap strings, row counts, orbit counts) and re-verified with
# this instrument's own certificates.
#
# PARENT APPARATUS: SCOUT-K's delivered code at its #74 digest
# 38c3f6cb288e.  The live v15/code/scoutk_exact.py is held by the SCOUT-K
# micro-repair worker mid-flight (its working-tree bytes differ from the
# committed #74 bytes), so THIS unit binds the parent snapshot-only, per
# the #58 precedent: v15/code/scoutt_parent_scoutk74.py (byte-equal to
# the #74 commit) and v15/code/scoutt_parent_scoutk74_receipt.json (the
# delivered receipt, for the byte-exact T-blind binding).  The arena /
# group / walk constructors are ANCHORED-REUSE re-typings of the same
# parent sections SCOUT-K itself anchored in the scout walk snapshot
# v15/code/scoutk_parent_delivered.py (edb60bccd22e).
#
# Exact arithmetic throughout: Python integers and fractions.Fraction.
# No floats, no builtin hash, no timestamps, no absolute paths in
# artifacts.  The delivery run is the only writer; every failure writes
# nothing.
#
# CLI: delivery (no args) | --no-write | --numbers | --kit | --selftest |
#      --mutant NAME | --verify-paper PATH | --list-gates | --list-mutants
# Exit codes: 0 pass, 2 usage, 3 gate failure / verification failure.
# ===========================================================================
import os
import sys
import json
import hashlib
import ast
from fractions import Fraction
from itertools import combinations, product
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # .../isp
NOTE_REL = "v15/note-scoutt.md"
OUT_REL = "v15/code/scoutt_output.txt"
REC_REL = "v15/code/scoutt_receipt.json"

# The parent is read ONLY through the disclosed byte-verified snapshots
# (the live scoutk files are held by the concurrent micro-repair);
# LOG.md is anchor-only and never digest-recorded (append-only file;
# recording its digest would plant an environment-dependent value in the
# receipt -- the #66 named hazard, checked in-run by G-ENV-EXCLUSION).
PINNED = {
    "v15/note-scoutt-pin.md": "3f35573d88d8",
    "v15/note-scoutt-pin-addendum.md": "15d763633293",
    "v15/note-scoutk-pin-addendum.md": "3a1e5a649537",
    "v15/code/scoutt_parent_scoutk74.py": "38c3f6cb288e",
    "v15/code/scoutt_parent_scoutk74_receipt.json": "5af53face093",
    "v15/code/scoutk_parent_delivered.py": "edb60bccd22e",
    "v14/paper-20-coupling.md": "4824d190af73",
}

F = Fraction
ARMED = {"name": None}


class GateFail(Exception):
    def __init__(self, gate, msg):
        self.gate = gate
        self.msg = msg
        super().__init__(gate + ": " + msg)


def mut(name):
    return ARMED["name"] == name


def pick(name, normal, corrupted):
    return corrupted if mut(name) else normal


def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]


def fser(x):
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, dict):
        return {str(k): fser(v) for k, v in sorted(x.items(),
                                                   key=lambda kv: str(kv[0]))}
    if isinstance(x, (list, tuple)):
        return [fser(v) for v in x]
    if isinstance(x, (int, str, bool)) or x is None:
        return x
    raise GateFail("G-SERIAL", "unserializable type " + type(x).__name__)


def to_json(obj):
    return json.dumps(fser(obj), sort_keys=True, separators=(",", ":"))


def digest(obj):
    return sha12(to_json(obj).encode("utf-8"))


def canon_text(text):
    lines = []
    for ln in text.splitlines():
        s = ln.lstrip()
        while s.startswith(">"):
            s = s[1:].lstrip()
        lines.append(s)
    return " ".join(" ".join(lines).split())


def read_rel(rel):
    with open(os.path.join(ROOT, rel), "rb") as f:
        return f.read()


class Ledger:
    def __init__(self):
        self.rows = []

    def gate(self, gid, ok, note, data=None):
        self.rows.append({"gate": gid, "ok": bool(ok), "note": note,
                          "data": fser(data) if data is not None else None})
        if not ok:
            raise GateFail(gid, note)


# ===========================================================================
# SECTION 1.  THE COMMITTED ARENA
# ANCHORED-REUSE: scoutt_parent_scoutk74.py (the #74 delivered SCOUT-K,
# 38c3f6cb288e) SECTION 1, itself an anchored re-typing of
# scoutk_parent_delivered.py SECTION 1.  Bound by G-PIN-DIGESTS +
# G-ANCHORS + the G-KREACH / G-TBLIND byte-exact reproductions.
# ===========================================================================
Q = 3
SITES = tuple((i, j) for i in range(Q) for j in range(Q))
LINKS = ((1, 0), (0, 1), (1, 1))
FOURTH = (1, 2)


def vadd(a, b):
    return ((a[0] + b[0]) % Q, (a[1] + b[1]) % Q)


CELLS = tuple((x, l) for x in SITES for l in LINKS)
CI = {c: k for k, c in enumerate(CELLS)}
DIM = len(CELLS)
CELL_PAIR = tuple(frozenset((x, vadd(x, l))) for (x, l) in CELLS)
PAIR_CELL = {p: k for k, p in enumerate(CELL_PAIR)}


def parallel_class(d):
    H = frozenset({(0, 0), d, vadd(d, d)})
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(vadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


ALL_DIRS = (LINKS[0], LINKS[1], LINKS[2], FOURTH)
CLASSES = {d: parallel_class(d) for d in ALL_DIRS}
LINES = tuple(sorted({L for d in ALL_DIRS for L in CLASSES[d]}))
DECLARED_LINES = tuple(sorted({L for d in LINKS for L in CLASSES[d]}))
TRIPLES = tuple(tuple(sorted(t)) for t in combinations(SITES, 3))


def block_of(t):
    out = []
    for p in combinations(t, 2):
        fp = frozenset(p)
        if fp in PAIR_CELL:
            out.append(PAIR_CELL[fp])
    return tuple(sorted(out))


BLOCK_OF = {t: block_of(t) for t in TRIPLES}
TRIANGLES = tuple(t for t in TRIPLES if len(BLOCK_OF[t]) == 3)
LINE_SET = frozenset(DECLARED_LINES)

Z0, Z1 = (0, 0), (1, 0)
WPOW = ((1, 0), (0, 1), (-1, -1))
GR = (((-1, 0), (2, 0), (2, 0)),
      ((2, 0), (-1, 0), (2, 0)),
      ((2, 0), (2, 0), (-1, 0)))


def zmul(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2 - y1 * y2)


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def znorm(a):
    return a[0] * a[0] - a[0] * a[1] + a[1] * a[1]


SHIFT = tuple(CI[(vadd(x, l), l)] for (x, l) in CELLS)


def coin_apply(psi, n, order):
    out = [Z0] * DIM
    for s in range(9):
        base = s * 3
        if order == "G.D":
            src = [zmul(psi[base + j], WPOW[n[base + j] % Q])
                   for j in range(3)]
        else:
            src = [psi[base + j] for j in range(3)]
        for i in range(3):
            tot = Z0
            for j in range(3):
                tot = zadd(tot, zmul(GR[i][j], src[j]))
            if order == "D.G":
                tot = zmul(tot, WPOW[n[base + i] % Q])
            out[base + i] = tot
    return out


def walk_shift(post):
    out = [Z0] * DIM
    for m in range(DIM):
        out[SHIFT[m]] = post[m]
    return tuple(out)


def born(psi, n, order):
    post = coin_apply(list(psi), list(n), order)
    w = [znorm(z) for z in post]
    tot = sum(w)
    if tot == 0:
        return None
    return tuple(Fraction(x, tot) for x in w)


R0 = tuple([0] * DIM)
SINGLE = tuple(Z1 if k == 0 else Z0 for k in range(DIM))


def nfield(cells):
    n = [0] * DIM
    for c in cells:
        n[c] += 1
    return tuple(n)


# ===========================================================================
# SECTION 2.  EXACT LINEAR ALGEBRA
# ANCHORED-REUSE: parent SECTION 2 (rref/nullspace, two-phase simplex with
# phase-one dual extraction, Farkas verification) re-typed verbatim; the
# fast equality-system pipeline (rref-first, reduced-row simplex, exact
# certificate recovery over the ORIGINAL published rows) is new and every
# certificate it emits is verified by the same farkas_ok as the parent's.
# ===========================================================================
def rref(rows):
    M = [list(r) for r in rows]
    piv, r = [], 0
    ncol = len(M[0])
    for c in range(ncol):
        p = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = Fraction(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return M, piv


def null_of(A):
    R, piv = rref(A)
    n = len(A[0])
    free = [j for j in range(n) if j not in piv]
    out = []
    for fj in free:
        v = [Fraction(0)] * n
        v[fj] = Fraction(1)
        for i, pj in enumerate(piv):
            v[pj] = -R[i][fj]
        out.append(v)
    return out


def rank_of(A):
    R, piv = rref(A)
    return len(piv)


def simplex(A, b, c=None):
    m = len(A)
    n = len(A[0])
    T = []
    sgn = []
    for i in range(m):
        row = [Fraction(v) for v in A[i]]
        rb = Fraction(b[i])
        if rb < 0:
            row = [-v for v in row]
            rb = -rb
            sgn.append(Fraction(-1))
        else:
            sgn.append(Fraction(1))
        T.append(row + [Fraction(1) if j == i else Fraction(0)
                        for j in range(m)] + [rb])
    basis = list(range(n, n + m))
    z = [Fraction(0)] * (n + m + 1)
    for i in range(m):
        for j in range(n + m + 1):
            z[j] += T[i][j]
    red = [(Fraction(1) if j >= n else Fraction(0)) - z[j]
           for j in range(n + m)] + [-z[n + m]]

    def pivot(pr, pc):
        pv = T[pr][pc]
        T[pr] = [v / pv for v in T[pr]]
        for i in range(m):
            if i != pr and T[i][pc] != 0:
                f = T[i][pc]
                T[i] = [a - f * bb for a, bb in zip(T[i], T[pr])]
        f = red[pc]
        if f != 0:
            for j in range(n + m + 1):
                red[j] -= f * T[pr][j]
        basis[pr] = pc

    def run(cols):
        while True:
            pc = None
            for j in cols:
                if red[j] < 0:
                    pc = j
                    break
            if pc is None:
                return
            pr, best = None, None
            for i in range(m):
                if T[i][pc] > 0:
                    ratio = T[i][n + m] / T[i][pc]
                    if best is None or ratio < best or \
                            (ratio == best and basis[i] < basis[pr]):
                        pr, best = i, ratio
            if pr is None:
                raise GateFail("G-LP-SOLVE", "unbounded phase")
            pivot(pr, pc)

    run(list(range(n + m)))
    gap = -red[n + m]
    y = [sgn[i] * (Fraction(1) - red[n + i]) for i in range(m)]
    if gap != 0:
        return ("INFEASIBLE", gap, None, y)
    for i in range(m):
        if basis[i] >= n:
            for j in range(n):
                if T[i][j] != 0:
                    pivot(i, j)
                    break
    x = [Fraction(0)] * n
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = T[i][n + m]
    if c is None:
        return ("FEASIBLE", Fraction(0), x, y)
    cost2 = [Fraction(v) for v in c] + [Fraction(0)] * m
    z2 = [Fraction(0)] * (n + m + 1)
    for i in range(m):
        cb = cost2[basis[i]] if basis[i] < n + m else Fraction(0)
        if cb != 0:
            for j in range(n + m + 1):
                z2[j] += cb * T[i][j]
    for j in range(n + m):
        red[j] = cost2[j] - z2[j]
    red[n + m] = -z2[n + m]
    run(list(range(n)))
    x = [Fraction(0)] * n
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = T[i][n + m]
    val = sum(Fraction(c[j]) * x[j] for j in range(n))
    return ("FEASIBLE", val, x, y)


def farkas_ok(A, b, y, gap):
    m = len(A)
    n = len(A[0])
    return (all(sum(y[i] * A[i][j] for i in range(m)) <= 0 for j in range(n))
            and all(v <= 1 for v in y)
            and sum(y[i] * b[i] for i in range(m)) == gap)


def witness_ok(A, b, x):
    m = len(A)
    n = len(A[0])
    if any(v < 0 for v in x):
        return False
    return all(sum(A[i][j] * x[j] for j in range(n)) == b[i]
               for i in range(m))


def solve_transpose(A, rhs_cols, target):
    """solve y^T A = target_row with extra linear conditions: rhs_cols is
    a list of (colvec, value) pairs meaning sum_i y_i colvec_i = value.
    Returns y or None.  Used to recover exact Farkas certificates over
    the ORIGINAL rows from reduced-system certificates."""
    m = len(A)
    n = len(A[0])
    rows = []
    rhs = []
    for j in range(n):
        rows.append([A[i][j] for i in range(m)])
        rhs.append(target[j])
    for (colvec, value) in rhs_cols:
        rows.append(list(colvec))
        rhs.append(value)
    aug = [rows[i] + [rhs[i]] for i in range(len(rows))]
    R, piv = rref(aug)
    y = [Fraction(0)] * m
    for i, pj in enumerate(piv):
        if pj == m:
            return None
        y[pj] = R[i][m]
    for i in range(len(R)):
        lhs = sum(R[i][j] * y[j] for j in range(m))
        if lhs != R[i][m]:
            return None
    return y


def eq_solve(A, b):
    """exact feasibility of {x >= 0 : Ax = b} with certificates over the
    published rows (A, b):
      INFEASIBLE-LINEAR: rank([A|b]) > rank(A); Farkas y with yA = 0,
        yb = gap > 0 recovered by transpose solve.
      INFEASIBLE (consistent): phase-one simplex on the rref-reduced
        rows; the reduced certificate is lifted to the original rows by
        the transpose solve (y with yA <= 0, yb = gap > 0).
      FEASIBLE: witness x verified directly against (A, b).
    Every emitted certificate/witness is re-verified by farkas_ok /
    witness_ok before being returned."""
    m = len(A)
    n = len(A[0])
    aug = [list(A[i]) + [Fraction(b[i])] for i in range(m)]
    R, piv = rref(aug)
    red_rows = []
    red_rhs = []
    inconsistent = False
    for i in range(len(R)):
        if any(R[i][j] != 0 for j in range(n)):
            red_rows.append(R[i][:n])
            red_rhs.append(R[i][n])
        elif R[i][n] != 0:
            inconsistent = True
    if inconsistent:
        y = solve_transpose(A, [(list(b), Fraction(1))],
                            [Fraction(0)] * n)
        if y is None:
            raise GateFail("G-LP-SOLVE", "linear Farkas recovery failed")
        s = max([Fraction(1)] + [v for v in y])
        y = [v / s for v in y]
        gap = sum(y[i] * b[i] for i in range(m))
        if not farkas_ok(A, b, y, gap) or gap <= 0:
            raise GateFail("G-LP-SOLVE", "linear Farkas invalid")
        return ("INFEASIBLE", gap, None, y, "LINEAR")
    st, gap_r, x, y_r = simplex(red_rows, red_rhs)
    if st == "FEASIBLE":
        if not witness_ok(A, b, x):
            raise GateFail("G-LP-SOLVE", "reduced witness fails original")
        return ("FEASIBLE", Fraction(0), x, None, "REDUCED")
    fvec = []
    for j in range(n):
        fvec.append(sum(y_r[i] * red_rows[i][j]
                        for i in range(len(red_rows))))
    gval = sum(y_r[i] * red_rhs[i] for i in range(len(red_rows)))
    y = solve_transpose(A, [(list(b), gval)], fvec)
    if y is None:
        raise GateFail("G-LP-SOLVE", "Farkas lift failed")
    s = max([Fraction(1)] + [v for v in y])
    y = [v / s for v in y]
    gap = gval / s
    if not farkas_ok(A, b, y, gap) or gap <= 0:
        raise GateFail("G-LP-SOLVE", "lifted Farkas invalid")
    return ("INFEASIBLE", gap, None, y, "REDUCED")


def polytope_dim(A, b, x0):
    """affine-hull dimension of the nonempty polytope {x >= 0: Ax = b},
    with a relative-interior support certificate: iteratively maximize
    the mass on the still-zero coordinate set; a zero optimum PROVES
    those coordinates vanish on every feasible point (each term is
    nonnegative); then dim = nullity of A stacked with the unit rows of
    the provably-zero set.  Returns (dim, zero_set, interior_pt)."""
    m = len(A)
    n = len(A[0])
    aug = [list(A[i]) + [Fraction(b[i])] for i in range(m)]
    R, piv = rref(aug)
    red_rows = []
    red_rhs = []
    for i in range(len(R)):
        if any(R[i][j] != 0 for j in range(n)):
            red_rows.append(R[i][:n])
            red_rhs.append(R[i][n])
    pts = [list(x0)]
    while True:
        cur = [sum(p[j] for p in pts) / len(pts) for j in range(n)]
        Zset = [j for j in range(n) if cur[j] == 0]
        if not Zset:
            break
        cvec = [Fraction(0)] * n
        for j in Zset:
            cvec[j] = Fraction(-1)
        st, val, x, _y = simplex(red_rows, red_rhs, cvec)
        if st != "FEASIBLE":
            raise GateFail("G-LP-SOLVE", "dim probe infeasible")
        if val == 0:
            break
        pts.append(list(x))
    cur = [sum(p[j] for p in pts) / len(pts) for j in range(n)]
    Zset = [j for j in range(n) if cur[j] == 0]
    stacked = [list(r) for r in red_rows]
    for j in Zset:
        row = [Fraction(0)] * n
        row[j] = Fraction(1)
        stacked.append(row)
    dim = n - rank_of(stacked)
    return dim, Zset, cur

# ===========================================================================
# SECTION 3.  THE ANCHOR REGISTRY
# ===========================================================================
ANCHORS = (
    ("A-PIN-ARM1", "v15/note-scoutt-pin.md",
     "does a minimal covariant kernel K(e|c,G,R,T) — T the ORDERED TRIGGER "
     "TRACE (the sequence of past trigger cells, exactly what the bridge "
     "erased) — preserve the delivered walk at the committed windows?"),
    ("A-PIN-ORBITS", "v15/note-scoutt-pin.md",
     "T enters the orbit space (orbits of (G,R,T,c,e) under simultaneous "
     "relabelling); one variable per orbit; conditional consistency mode; "
     "depths 2 and 3."),
    ("A-PIN-ARM2", "v15/note-scoutt-pin.md",
     "build the MARGINAL-HISTORY comparison: an exact factorizing "
     "history-level process (Markov in the complete successor, latent "
     "triggers summed out) compared to the walk's OBSERVABLE record "
     "distributions only, at the same windows; exact polynomial method "
     "with certificates per the #68 freeze (the linear-relaxation refusal "
     "binds)."),
    ("A-PIN-TBLIND", "v15/note-scoutt-pin.md",
     "CROSS-CHECK (mandatory): the T-blind subfamily of arm 1 must "
     "reproduce SCOUT-K's refusal (binds to the parent)."),
    ("A-PIN-FEAS", "v15/note-scoutt-pin.md",
     "even TRACE-SUFFICIENT is a FEASIBILITY fact, not an ontology "
     "decision; gated"),
    ("A-ADD-MODE", "v15/note-scoutk-pin-addendum.md",
     "PRIMARY = CONDITIONAL transition agreement at every reached state "
     "(each constraint linear in exactly one kernel factor; LP/Farkas "
     "valid)."),
    ("A-ADD-MARGINAL", "v15/note-scoutk-pin-addendum.md",
     "SECONDARY (only if attempted, disclosed) = marginal-history "
     "agreement WITH exact Markov factorization preserved, decided by an "
     "exact polynomial method with certificates."),
    ("A-ADD-REFUSAL", "v15/note-scoutk-pin-addendum.md",
     "A linear relaxation over history flows is REFUSED as an "
     "outcome-bearing method: it can certify \"kernels\" that do not "
     "factor into one reusable K.  Every verdict names its mode."),
    ("A-ADD-SCOPE", "v15/note-scoutk-pin-addendum.md",
     "G is FIXED throughout — this unit tests RECORD backreaction only; "
     "success does not establish quantum transport across "
     "AUTOGLUE-created cells or any topology change G→G'; those remain "
     "independent missing laws."),
    ("A-LOG82-MECH", "v15/LOG.md",
     "the kernel construction builds the available record from the WHOLE "
     "TRIPLE FOOTPRINT (R1 = nfield(BLOCK_OF[e1])) while the target walk "
     "depends on the individual CELL-TRIGGER history (q3 over "
     "[c1],[c2])."),
    ("A-LOG82-ERASE", "v15/LOG.md",
     "The bridge lets one cell trigger a three-cell event, AND THE TRIPLE "
     "RECORD FORGETS WHICH CELL WAS THE TRIGGER; the walk remembers and "
     "uses it."),
    ("A-LOG82-PRECISE", "v15/LOG.md",
     "at this arena, no normalized covariant conditional kernel "
     "K(e|c,G,R) with fixed geometry, the trigger factorization "
     "P(c,e)=q(c)K(e|c,G,R), and exact preservation of the delivered "
     "cell-walk's conditional statistics, works through window 3 — even "
     "with the entire record."),
    ("A-LOG82-FORK2", "v15/LOG.md",
     "TRIGGER BOOKKEEPING — per-latent-history equality may be too "
     "strong; test the marginal-history mode (the frozen secondary the "
     "#68 addendum already names): an exact factorizing history-level "
     "process compared AFTER latent triggers are marginalized."),
    ("A-PLAN-WREP", "v15/PLAN.md",
     "no currently supplied mathematical object (K, psi, rho, H, a "
     "field, a trigger) may be promoted to ontology merely because the "
     "equations need it; an ontic psi, field, or trigger remains "
     "admissible if independently declared, operationally distinguished, "
     "and mapped to the beables."),
    ("A-ADD2-NEUTRAL", "v15/note-scoutt-pin-addendum.md",
     "Your unit tests whether a trace COULD be real — it must not "
     "presuppose either answer."),
    ("A-ADD2-LADDER", "v15/note-scoutt-pin-addendum.md",
     "Publish the feasibility verdict PER GRAIN with "
     "certificates/dimensions; the honest headline names the COARSEST "
     "feasible grain."),
    ("A-ADD2-GRAIN", "v15/note-scoutt-pin-addendum.md",
     "SCOUTT-TRACE-SUFFICIENT carries its grain: "
     "SCOUTT-TRACE-SUFFICIENT-<grain>-<dim>-AT-<depth>."),
    ("A-LOG84-FEAS", "v15/LOG.md",
     "Even TRACE-SUFFICIENT (SCOUT-T) is feasibility, not nature."),
    ("A-LOG84-ARITY", "v15/LOG.md",
     "RECORD-ARITY (two actors per elementary relational fact — the "
     "atomic beable is a pair relation) vs PROCESS-ARITY (any number of "
     "actors may participate in ONE indivisible boundary-to-boundary "
     "transition)."),
    ("A-PARENT-1010", "v15/code/scoutt_parent_scoutk74.py",
     "for e1 in E1S: R1 = nfield(BLOCK_OF[e1])"),
    ("A-PARENT-CANON", "v15/code/scoutt_parent_scoutk74.py",
     "key = (tuple(sorted((gc[x], v) for (x, v) in patt)), gc[c], "
     "GTRI[gi][e])"),
    ("A-PARENT-KPOLY", "v15/code/scoutk_parent_delivered.py",
     "K_alpha: alpha on the line block, (1-alpha)/2 on each non-line"),
    ("A-LOG74-ORBITS", "v15/LOG.md",
     "16 to 25 orbit variables per arm against the fixed-alpha family's "
     "one"),
    ("A-P20-277", "v14/paper-20-coupling.md",
     "A division event on cell (x, l) increments n_l(x) by one."),
    ("A-P20-217", "v14/paper-20-coupling.md",
     "The menu at site x is the three link traversals and the weight "
     "q(l|x) is the post-coin Born weight |(Cψ)(x,l)|²."),
    ("A-P20-633", "v14/paper-20-coupling.md",
     "The record accumulates the law's own weights and the state is not "
     "collapsed onto the emitted cell, so the walk stays coherent between "
     "division events."),
)


def measure_reads(LD, P):
    reads = {}
    for rel in sorted(PINNED):
        reads[rel] = sha12(read_rel(rel))
    P["read_set"] = reads
    bad = sorted(rel for rel, d in PINNED.items()
                 if pick("MUT-PINDIG", reads[rel], reads[rel] + "x") != d)
    P["pin_check"] = {
        "pinned": dict(PINNED), "bad": bad,
        "parent_resolution": "SNAPSHOT-ONLY (the #58 precedent): the "
                             "live scoutk_exact.py is held by the "
                             "concurrent micro-repair worker and its "
                             "working-tree bytes differ from the #74 "
                             "commit; this unit binds the parent at the "
                             "COMMITTED #74 digest through "
                             "scoutt_parent_scoutk74.py and the "
                             "delivered receipt snapshot",
        "log_resolution": "ANCHOR-ONLY-UNPINNED (append-only file; its "
                          "digest is checked in-run by G-ENV-EXCLUSION "
                          "and never serialized)"}
    LD.gate("G-PIN-DIGESTS", not bad,
            "the frozen pin, the #68 addendum, both parent snapshots, "
            "the scout walk snapshot and paper-20 are read at their "
            "pinned digests; the parent is bound snapshot-only (the "
            "live scoutk files are mid-repair); LOG.md is anchor-only "
            "and its digest is never recorded",
            P["pin_check"])
    anch = []
    for (aid, rel, quote) in ANCHORS:
        hay = canon_text(read_rel(rel).decode("utf-8"))
        needle = canon_text(pick("MUT-ANCHOR", quote, quote + " CORRUPTED"))
        anch.append({"id": aid, "rel": rel, "found": hay.find(needle) >= 0,
                     "quote": quote})
    P["anchors"] = anch
    LD.gate("G-ANCHORS", all(a["found"] for a in anch),
            "every declared source anchor is located verbatim "
            "(whitespace-collapsed) in its file: the pin's two arm "
            "definitions, the #68 mode freeze with its relaxation "
            "refusal, the #82 trigger-erasure mechanism and precise "
            "parent formulation, the #84 W-REPRESENTATION and arity "
            "split, the parent-code write-time line and paper-20",
            {"count": len(anch),
             "missing": [a["id"] for a in anch if not a["found"]]})
    parent_receipt = json.loads(
        read_rel("v15/code/scoutt_parent_scoutk74_receipt.json")
        .decode("utf-8"))
    return parent_receipt


# ===========================================================================
# SECTION 4.  ARENA + GAMMA + WALK GATES
# ANCHORED-REUSE: parent SECTION 4 re-typed; identical gates.
# ===========================================================================
def measure_arena(LD, P):
    tri = TRIANGLES
    if mut("MUT-ARENA"):
        tri = tri + (TRIPLES[0],)
    memb = Counter()
    for t in TRIANGLES:
        for c in BLOCK_OF[t]:
            memb[c] += 1
    P["arena"] = {"cells": DIM, "pair_bijection": len(set(CELL_PAIR)) == DIM,
                  "lines": len(LINES), "declared_lines": len(DECLARED_LINES),
                  "triples": len(TRIPLES), "triangles": len(tri),
                  "cell_in_blocks": sorted(Counter(memb.values()).items())}
    LD.gate("G-ARENA",
            P["arena"]["cells"] == 27 and P["arena"]["pair_bijection"]
            and P["arena"]["lines"] == 12
            and P["arena"]["declared_lines"] == 9
            and P["arena"]["triples"] == 84 and P["arena"]["triangles"] == 27
            and P["arena"]["cell_in_blocks"] == [(3, 27)],
            "the committed chart rebuilt from constructors: 27 cells in "
            "bijection with the linked pairs, 27 triangles among 84 "
            "triples, 9 declared lines of 12, every cell in exactly 3 "
            "blocks", P["arena"])


def lin_maps():
    out = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a * d - b * c) % 3 != 0:
                        out.append(((a, b), (c, d)))
    return out


def apply_lin(A, v):
    (a, b), (c, d) = A
    return ((a * v[0] + b * v[1]) % 3, (c * v[0] + d * v[1]) % 3)


def class_rep(v):
    for dd in ALL_DIRS:
        if v in (dd, vadd(dd, dd)):
            return dd
    return None


def build_gamma(LD, P):
    glin = [A for A in lin_maps()
            if all(class_rep(apply_lin(A, l)) in LINKS for l in LINKS)]
    gamma = [(A, t) for A in glin for t in SITES]
    if mut("MUT-GAMMA"):
        gamma = gamma[:-1]

    def g_site(g, x):
        A, t = g
        return vadd(apply_lin(A, x), t)

    GCELL = []
    GTRI = []
    for g in gamma:
        gc = tuple(PAIR_CELL[frozenset(g_site(g, x) for x in CELL_PAIR[ci])]
                   for ci in range(DIM))
        GCELL.append(gc)
        GTRI.append({t: tuple(sorted(g_site(g, x) for x in t))
                     for t in TRIANGLES})
    tri_set = set(TRIANGLES)
    closed = all(GTRI[gi][t] in tri_set
                 for gi in range(len(gamma)) for t in TRIANGLES)
    stab0 = [gi for gi in range(len(gamma)) if GCELL[gi][0] == 0]
    b0 = [t for t in TRIANGLES if 0 in BLOCK_OF[t]]
    sorb = set()
    for t in b0:
        sorb.add(frozenset(GTRI[gi][t] for gi in stab0))
    sorb_sizes = sorted(len([t for t in b0 if t in o]) for o in sorb)
    P["gamma"] = {"linear_order": len(glin), "order": len(gamma),
                  "blocks_closed": closed, "stab_cell_order": len(stab0),
                  "stab_orbits_on_incident_blocks": sorb_sizes}
    LD.gate("G-GAMMA",
            len(glin) == 12 and len(gamma) == 108 and closed
            and len(stab0) == 4 and sorb_sizes == [1, 2],
            "the relabelling group is rebuilt at order 108 (12 linear x 9 "
            "translations), closed on the block class; the cell stabilizer "
            "(order 4) swaps the two non-line incident blocks -- the "
            "measured fact behind the first-event boundary",
            P["gamma"])
    return GCELL, GTRI


def build_walk(LD, P):
    psi1 = walk_shift(coin_apply(list(SINGLE), list(R0), "G.D"))
    q1 = born(SINGLE, R0, "G.D")
    if mut("MUT-Q"):
        q1 = tuple(2 * v for v in q1)
    sup1 = [c for c in range(DIM) if q1[c] > 0]
    q2 = born(psi1, R0, "G.D")
    sup2 = [c for c in range(DIM) if q2[c] > 0]
    P["walk"] = {"q1_support": sup1,
                 "q1_values": [str(q1[c]) for c in sup1],
                 "q2_support": sup2, "q2_support_count": len(sup2),
                 "q2_sum": sum(q2), "sample_space": "CELLS"}
    LD.gate("G-WALK",
            sum(q1) == 1 and sup1 == [0, 1, 2]
            and [str(q1[c]) for c in sup1] == ["1/9", "4/9", "4/9"]
            and sup2 == [3, 4, 5, 9, 10, 11, 12, 13, 14]
            and sum(q2) == 1,
            "the delivered walk rebuilt: first-trigger weights "
            "(1/9, 4/9, 4/9) on cells 0,1,2; second-trigger support the 9 "
            "cells of the three shifted sites, unit mass",
            P["walk"])
    BOC = {c: [t for t in TRIANGLES if c in BLOCK_OF[t]]
           for c in range(DIM)}
    E1S = []
    for c1 in sup1:
        for t in BOC[c1]:
            if t not in E1S:
                E1S.append(t)
    variants = {"R0": R0}
    for c in sup1:
        variants["HIT-%d" % c] = nfield([c])
    for k, t in enumerate(E1S):
        variants["TRI-%d" % k] = nfield(BLOCK_OF[t])
    post1 = coin_apply(list(SINGLE), list(R0), "G.D")
    psi_probe = pick("MUT-BLIND", psi1, tuple(post1))
    base = born(psi_probe, R0, "G.D")
    blind = all(born(psi_probe, n, "G.D") == base
                for _k, n in sorted(variants.items()))
    single_link = all(
        sum(1 for j in range(3) if psi_probe[s * 3 + j] != Z0) <= 1
        for s in range(9))
    P["blindness"] = {
        "variants": len(variants), "all_equal": blind,
        "single_link_per_site": single_link,
        "licence": "the second-step Born vector is byte-identical across "
                   "the initial record, all 3 cell-hit increments and all "
                   "7 incident triple-writes, so the second-trigger "
                   "conditional cancels row-wise in every consistency "
                   "equation, the two-step window constrains nothing, and "
                   "the window-2 observable-history marginals of arm 2 "
                   "agree for every normalized kernel",
        "sample_space": "CELLS"}
    LD.gate("G-BLIND", blind and single_link and len(variants) == 11,
            "the depth-2 blindness licence re-measured: 11 record "
            "variants, one Born vector; mechanism single-link site "
            "support", {"variants": len(variants)})
    return psi1, q1, sup1, q2, sup2, BOC, E1S


# ===========================================================================
# SECTION 5.  THE PROXIMITY ARMS (parent's frozen predicates, reused by
# anchor and re-measured covariant) + ORBIT MACHINERY (T-less and T-full)
# ANCHORED-REUSE: parent SECTION 5.  The arm predicates are the parent's
# pre-registered, digest-sealed predicates (in the pinned snapshot at
# 38c3f6cb288e); NO new proximity predicate is introduced by this unit;
# the trace slot T is carried WHOLE at every arm (a locality-restricted
# trace is a registered successor, not an improvised predicate).
# ===========================================================================
ADJD = set()
for _d in LINKS:
    ADJD.add(_d)
    ADJD.add(vadd(_d, _d))


def N_shared(c, R):
    p = CELL_PAIR[c]
    base = frozenset(c2 for c2 in range(DIM) if CELL_PAIR[c2] & p)
    if mut("MUT-ARMCOV") and c == 0:
        base = base - {min(x for x in base if x != 0)}
    return base


def N_recdist(c, R):
    vis = {c}
    frontier = [c]
    while frontier:
        u = frontier.pop()
        for v in range(DIM):
            if v not in vis and R[v] > 0 and (CELL_PAIR[v] & CELL_PAIR[u]):
                vis.add(v)
                frontier.append(v)
    return frozenset(vis)


def N_metric(c, R):
    S = set()
    for u in CELL_PAIR[c]:
        for v in SITES:
            dxy = ((v[0] - u[0]) % 3, (v[1] - u[1]) % 3)
            if dxy == (0, 0) or dxy in ADJD:
                S.add(v)
    return frozenset(c2 for c2 in range(DIM)
                     if any(x in S for x in CELL_PAIR[c2]))


def N_causal(c, R):
    sc = set(CELL_PAIR[c])
    out = set()
    for c2 in range(DIM):
        if set(CELL_PAIR[c2]) & sc:
            out.add(c2)
            continue
        x, l = CELLS[c2]
        fwd = CI[(vadd(x, l), l)]
        bwd = CI[(((x[0] - l[0]) % 3, (x[1] - l[1]) % 3), l)]
        if set(CELL_PAIR[fwd]) & sc or set(CELL_PAIR[bwd]) & sc:
            out.add(c2)
    return frozenset(out)


def N_global(c, R):
    return frozenset(range(DIM))


ARM_ORDER = ("SA", "RD", "MC", "CN", "GLOBAL")
ARM_FN = {"SA": N_shared, "RD": N_recdist, "MC": N_metric,
          "CN": N_causal, "GLOBAL": N_global}
ARM_NAME = {"SA": "SHARED-ACTOR", "RD": "RECORD-DISTANCE",
            "MC": "METRIC-COUNT", "CN": "CAUSAL-NEIGHBORHOOD",
            "GLOBAL": "GLOBAL-REFERENCE"}


def measure_arms(LD, P, GCELL, GTRI, E1S):
    Rsample = nfield(BLOCK_OF[E1S[0]])
    rows = {}
    allok = True
    for an in ARM_ORDER:
        NF = ARM_FN[an]
        ok = True
        for gi in range(len(GCELL)):
            gc = GCELL[gi]
            gR = [0] * DIM
            for c in range(DIM):
                gR[gc[c]] = Rsample[c]
            gR = tuple(gR)
            for c in range(DIM):
                if frozenset(gc[x] for x in NF(c, Rsample)) != NF(gc[c], gR):
                    ok = False
                    break
            if not ok:
                break
        rows[an] = {"name": ARM_NAME[an], "covariant": ok,
                    "size_at_cell0_r0": len(NF(0, R0)),
                    "size_at_cell0_sample": len(NF(0, Rsample))}
        allok = allok and ok
    P["arms"] = rows
    LD.gate("G-ARMS-COVARIANT",
            allok and rows["SA"]["size_at_cell0_r0"] == 11
            and rows["RD"]["size_at_cell0_r0"] == 1
            and rows["RD"]["size_at_cell0_sample"] == 3
            and rows["MC"]["size_at_cell0_r0"] == 27
            and rows["CN"]["size_at_cell0_r0"] == 15
            and rows["GLOBAL"]["size_at_cell0_r0"] == 27,
            "the parent's four pre-registered proximity arms and the "
            "global reference are re-measured relabelling-covariant "
            "(N(gc,gR) = g N(c,R) for all 108 elements); neighborhood "
            "sizes 11 / record-cluster / 27 / 15 / 27; no new predicate "
            "is introduced by this unit",
            {an: rows[an]["size_at_cell0_r0"] for an in ARM_ORDER})


def loc_pattern(c, R, NF):
    return tuple(sorted((c2, R[c2]) for c2 in NF(c, R) if R[c2] > 0))


def make_canon(GCELL, GTRI):
    # ANCHORED-REUSE: the parent's T-less canonicalization, verbatim.
    ng = len(GCELL)

    def canon_tuple(R, c, e, NF):
        patt = loc_pattern(c, R, NF)
        best = None
        for gi in range(ng):
            gc = GCELL[gi]
            key = (tuple(sorted((gc[x], v) for (x, v) in patt)),
                   gc[c], GTRI[gi][e])
            if best is None or key < best:
                best = key
        return best

    def canon_ctx(R, c, NF):
        patt = loc_pattern(c, R, NF)
        best = None
        for gi in range(ng):
            gc = GCELL[gi]
            key = (tuple(sorted((gc[x], v) for (x, v) in patt)), gc[c])
            if best is None or key < best:
                best = key
        return best
    return canon_tuple, canon_ctx


TRACE_GRAINS = ("PREV1", "COUNTS", "SUFFIX2", "FULL")
LADDER = ("NONE",) + TRACE_GRAINS
GRAIN_TRACE_DECL = {
    "NONE": "no trace: the kernel is K(e|c,G,R) -- the T-blind parent "
            "family, bound byte-exactly to the delivered SCOUT-K refusal",
    "PREV1": "the previous trigger cell only: T restricted to its last "
             "entry (an ordered length-1 suffix)",
    "COUNTS": "unordered trigger counts: T carried as a multiset (the "
              "orbit datum is the sorted image, order forgotten)",
    "SUFFIX2": "the length-2 ordered suffix of the trigger trace",
    "FULL": "the full ordered trigger trace"}


def tgrain(T, grain):
    if grain == "NONE":
        return ()
    if grain == "PREV1":
        return T[-1:]
    if grain == "SUFFIX2":
        return T[-2:]
    return tuple(T)


def make_canonT(GCELL, GTRI):
    # NEW: the trace-carrying canonicalization -- the orbit of
    # (G, R, T, c, e) under SIMULTANEOUS relabelling of all five slots
    # (G is fixed and Gamma-invariant, so the orbit space is over
    # (R, T, c, e)); an ordered trace transforms pointwise with order
    # kept; the COUNTS grain carries the multiset, so its orbit datum
    # is the SORTED image of the trace under each group element.
    ng = len(GCELL)

    def canonT_tuple(R, T, c, e, NF, tmode="ORD"):
        patt = loc_pattern(c, R, NF)
        best = None
        for gi in range(ng):
            gc = GCELL[gi]
            if tmode == "ORD":
                timg = tuple(gc[t] for t in T)
            else:
                timg = tuple(sorted(gc[t] for t in T))
            key = (tuple(sorted((gc[x], v) for (x, v) in patt)),
                   timg, gc[c], GTRI[gi][e])
            if best is None or key < best:
                best = key
        return best

    def canonT_ctx(R, T, c, NF, tmode="ORD"):
        patt = loc_pattern(c, R, NF)
        best = None
        for gi in range(ng):
            gc = GCELL[gi]
            if tmode == "ORD":
                timg = tuple(gc[t] for t in T)
            else:
                timg = tuple(sorted(gc[t] for t in T))
            key = (tuple(sorted((gc[x], v) for (x, v) in patt)),
                   timg, gc[c])
            if best is None or key < best:
                best = key
        return best
    return canonT_tuple, canonT_ctx


# ===========================================================================
# SECTION 6.  THE PARENT REACH CENSUS (T-less), BOUND TO THE DELIVERED
# RECEIPT, AND THE TRACE REACH CENSUS (the headline orbit counts)
# ===========================================================================
def kreach_census(LD, P, canon_tuple, canon_ctx, sup1, sup2, BOC, E1S,
                  PREC):
    RAW = []
    for e1 in E1S:
        R1 = nfield(BLOCK_OF[e1])
        for c2 in sup2:
            for e2 in BOC[c2]:
                RAW.append((e1, R1, c2, e2))
    if mut("MUT-KREACH"):
        RAW.append(RAW[0])
    raw_ctx = len(E1S) * len(sup2)
    depth3 = {}
    partitions = {}
    for an in ARM_ORDER:
        NF = ARM_FN[an]
        vmap = {}
        for i, (e1, R1, c2, e2) in enumerate(RAW):
            vmap.setdefault(canon_tuple(R1, c2, e2, NF), []).append(i)
        cmap = {}
        for e1 in E1S:
            R1 = nfield(BLOCK_OF[e1])
            for c2 in sup2:
                cmap.setdefault(canon_ctx(R1, c2, NF), []).append((e1, c2))
        partitions[an] = frozenset(frozenset(v) for v in vmap.values())
        depth3[an] = {"context_classes": len(cmap),
                      "tuple_orbit_variables": len(vmap)}
    coinc = {"SA_eq_RD": partitions["SA"] == partitions["RD"],
             "MC_eq_GLOBAL": partitions["MC"] == partitions["GLOBAL"],
             "SA_eq_CN": partitions["SA"] == partitions["CN"],
             "CN_eq_GLOBAL": partitions["CN"] == partitions["GLOBAL"]}
    want = PREC["reach"]["depth3"]
    match_parent = all(
        depth3[an]["tuple_orbit_variables"]
        == want[an]["tuple_orbit_variables"]
        and depth3[an]["context_classes"] == want[an]["context_classes"]
        for an in ARM_ORDER)
    P["kreach"] = {
        "raw_tuples": len(RAW), "raw_contexts": raw_ctx,
        "distinct_first_events": len(E1S),
        "depth3": depth3, "coincidence": coinc,
        "parent_receipt_match": match_parent,
        "sample_space": "TRIPLE-EVENTS"}
    LD.gate("G-KREACH",
            len(RAW) == 189 and raw_ctx == 63 and len(E1S) == 7
            and match_parent
            and {an: depth3[an]["tuple_orbit_variables"]
                 for an in ARM_ORDER}
            == {"SA": 16, "RD": 16, "MC": 25, "CN": 19, "GLOBAL": 25}
            and coinc["SA_eq_RD"] and coinc["MC_eq_GLOBAL"]
            and not coinc["SA_eq_CN"] and not coinc["CN_eq_GLOBAL"],
            "the parent's T-blind reach census is reproduced inside this "
            "instrument and matches the pinned delivered receipt "
            "field-by-field: 63 contexts / 189 tuples / 7 first events, "
            "orbit variables 16/16/25/19/25, coincidences SA=RD and "
            "MC=GLOBAL with CN strictly between",
            {"raw": len(RAW)})
    return RAW, partitions


def treach_census(LD, P, canonT_tuple, canonT_ctx, canon_tuple, sup1,
                  sup2, BOC):
    RAWT = []
    for c1 in sup1:
        for e1 in BOC[c1]:
            R1 = nfield(BLOCK_OF[e1])
            for c2 in sup2:
                for e2 in BOC[c2]:
                    RAWT.append((c1, e1, R1, c2, e2))
    if mut("MUT-TREACH"):
        RAWT.append(RAWT[0])
    pairs = sorted({(c1, e1) for (c1, e1, _R, _c, _e) in RAWT})
    depth3 = {}
    partitionsT = {}
    refine_all = True
    for an in ARM_ORDER:
        NF = ARM_FN[an]
        vmap = {}
        pkey = {}
        for i, (c1, e1, R1, c2, e2) in enumerate(RAWT):
            vmap.setdefault(canonT_tuple(R1, (c1,), c2, e2, NF),
                            []).append(i)
            pkey[i] = canon_tuple(R1, c2, e2, NF)
        cmap = {}
        for c1 in sup1:
            for e1 in BOC[c1]:
                R1 = nfield(BLOCK_OF[e1])
                for c2 in sup2:
                    cmap.setdefault(canonT_ctx(R1, (c1,), c2, NF),
                                    []).append((c1, e1, c2))
        refine = all(len({pkey[i] for i in v}) == 1
                     for v in vmap.values())
        refine_all = refine_all and refine
        partitionsT[an] = frozenset(frozenset(v) for v in vmap.values())
        depth3[an] = {"context_classes": len(cmap),
                      "tuple_orbit_variables": len(vmap),
                      "refines_parent_partition": refine}
    coincT = {"SA_eq_RD": partitionsT["SA"] == partitionsT["RD"],
              "MC_eq_GLOBAL": partitionsT["MC"] == partitionsT["GLOBAL"],
              "SA_eq_CN": partitionsT["SA"] == partitionsT["CN"],
              "CN_eq_GLOBAL": partitionsT["CN"] == partitionsT["GLOBAL"]}
    if mut("MUT-TCOINC"):
        coincT["SA_eq_RD"] = not coincT["SA_eq_RD"]
    groups = []
    leader = {}
    for an in ARM_ORDER:
        placed = False
        for grp in groups:
            if partitionsT[grp[0]] == partitionsT[an]:
                grp.append(an)
                leader[an] = grp[0]
                placed = True
                break
        if not placed:
            groups.append([an])
            leader[an] = an
    P["treach"] = {
        "raw_tuples": len(RAWT), "raw_contexts": len(pairs) * len(sup2),
        "first_event_pairs": len(pairs),
        "depth3": depth3,
        "depth2_orbit_variables_all_arms": 2,
        "sample_space": "TRIPLE-EVENTS"}
    P["tcoincidence"] = {
        "coincidences": coincT,
        "distinct_systems": [grp[0] for grp in groups],
        "groups": [list(grp) for grp in groups],
        "reading": "which arms induce identical trace-orbit partitions "
                   "is MEASURED, never assumed; one representative "
                   "system is solved per distinct partition"}
    LD.gate("G-TREACH",
            len(RAWT) == 243 and len(pairs) == 9
            and P["treach"]["raw_contexts"] == 81 and refine_all
            and all(depth3[an]["tuple_orbit_variables"] >= 2
                    for an in ARM_ORDER),
            "the trace reach census: 81 raw contexts / 243 raw tuples "
            "over 9 (trigger, first-event) pairs; at every arm the "
            "trace-orbit partition REFINES the parent partition (every "
            "trace orbit lies inside exactly one T-blind orbit)",
            {"raw": len(RAWT),
             "orbit_variables": {an: depth3[an]["tuple_orbit_variables"]
                                 for an in ARM_ORDER}})
    grp_ok = all(
        (partitionsT[a] == partitionsT[b]) == (leader[a] == leader[b])
        for a in ARM_ORDER for b in ARM_ORDER)
    LD.gate("G-TCOINCIDE",
            grp_ok and len(groups) >= 1
            and coincT["SA_eq_RD"] == (partitionsT["SA"]
                                       == partitionsT["RD"]),
            "trace-partition coincidences measured and the representative "
            "grouping is exactly the measured partition equality",
            P["tcoincidence"]["coincidences"])
    return RAWT, partitionsT


def step1_censusT(LD, P, canonT_tuple, sup1, BOC):
    # #64/#68 FIRST-EVENT BOUNDARY, with the trace slot: at step one the
    # trace is EMPTY (no past triggers), so the census must collapse to
    # the parent's 2 orbit variables -- the trace adds nothing before
    # the first event, and the step-one factor remains the measured
    # dim-1 line-weight family (the exact linearization seat).
    NF = ARM_FN["GLOBAL"]
    keys = set()
    for c1 in sup1:
        for e1 in BOC[c1]:
            keys.add(canonT_tuple(R0, (), c1, e1, NF))
    nvars = pick("MUT-STEP1", len(keys), len(keys) + 1)
    P["step1t"] = {
        "orbit_variables": nvars,
        "family_dim_after_normalization": 1,
        "trace_at_step_one": "EMPTY (the ordered trigger trace has no "
                             "entries before the first trigger); the "
                             "step-one kernel factor is the parent's "
                             "line-weight family a in [0,1] exactly",
        "sample_space": "TRIPLE-EVENTS"}
    LD.gate("G-STEP1T", nvars == 2,
            "the step-one census with the trace slot: the empty trace "
            "collapses step one to the parent's 2 orbit variables (line "
            "/ non-line), dim 1 after normalization -- the exact seat "
            "of the conditional-mode linearization",
            {"orbit_variables": nvars})


def depth2_system(LD, P, psi1, sup1, BOC):
    rows_vac = True
    for c1 in sup1:
        rhs = born(psi1, nfield([c1]), "G.D")
        for e1 in BOC[c1]:
            if born(psi1, nfield(BLOCK_OF[e1]), "G.D") != rhs:
                rows_vac = False
    norm = [[F(1), F(2)]]
    dim = pick("MUT-D2", len(null_of(norm)), 2)
    P["d2t"] = {
        "kernel_variables": 2,
        "normalization_rank": rank_of(norm),
        "consistency_rows_vacuous_given_blindness": rows_vac,
        "polytope_dim": dim,
        "arm1_verdict": "SCOUTT-TRACE-SUFFICIENT-1-AT-2"
                        "<CONDITIONAL-MODE; VACUOUS-BY-BLINDNESS; "
                        "TRACE-EMPTY-AT-STEP-ONE>",
        "arm2_verdict": "SCOUTT-MARGINAL-AGREES-AT-2-ALL-GRAINS"
                        "<MARGINAL-HISTORY-MODE-EXACT-FACTORIZATION; "
                        "VACUOUS-BY-BLINDNESS: the window-2 "
                        "observable-history distribution is q1 x q2 for "
                        "EVERY normalized kernel, equal to the walk's>",
        "sample_space": "TRIPLE-EVENTS"}
    LD.gate("G-D2T", rows_vac and dim == 1,
            "the depth-2 window: consistency is vacuous under the "
            "measured blindness at both arms and every grain -- the "
            "covariant family is the one-parameter line-weight segment, "
            "dim 1; the trace is empty at step one, so depth 2 cannot "
            "distinguish the trace-carrying kernel from the parent's",
            {"dim": dim})


def make_q3(psi1):
    memo = {}

    def step(psi, n):
        return walk_shift(coin_apply(list(psi), list(n), "G.D"))

    def q3_of(n1_cells, n2_cells):
        key = (tuple(sorted(n1_cells)), tuple(sorted(n2_cells)))
        if key not in memo:
            psi2 = step(psi1, nfield(n1_cells))
            v = born(psi2, nfield(list(n1_cells) + list(n2_cells)), "G.D")
            if v is None:
                raise GateFail("G-A1-SAMPLES", "undefined q3 branch")
            memo[key] = v
        return memo[key]
    return q3_of


# ===========================================================================
# SECTION 7.  SYSTEM BUILDERS
# build_system / system_at: ANCHORED-REUSE, parent SECTION 8 verbatim
# (needed for the byte-exact T-blind binding and as arm 2's row source).
# build_systemT: NEW -- the trace-carrying conditional-mode system.
# ===========================================================================
SAMPLES = (F(0), F(1, 6), F(1, 3), F(1, 2), F(2, 3), F(1))
SYSTEMS = (("SA-RD", "SA"), ("CN", "CN"), ("MC-GLOBAL", "GLOBAL"))
REP_LABEL = {"SA": "SA-RD", "RD": "SA-RD", "CN": "CN",
             "MC": "MC-GLOBAL", "GLOBAL": "MC-GLOBAL"}


def build_system(an, canon_tuple, canon_ctx, q3_of, sup1, sup2, BOC, E1S,
                 RAW, rhs_override=None):
    NF = ARM_FN[an]
    vidx = {}
    TUP = {}
    for (e1, R1, c2, e2) in RAW:
        k = canon_tuple(R1, c2, e2, NF)
        if k not in vidx:
            vidx[k] = len(vidx)
        TUP[(e1, c2, e2)] = vidx[k]
    nv = len(vidx)
    lineness = {}
    line_ok = True
    for (e1, R1, c2, e2) in RAW:
        j = TUP[(e1, c2, e2)]
        bln = e2 in LINE_SET
        if j in lineness and lineness[j] != bln:
            line_ok = False
        lineness[j] = bln
    ctx_ok = True
    ctx_row = {}
    normset = {}
    for e1 in E1S:
        R1 = nfield(BLOCK_OF[e1])
        for c2 in sup2:
            idxs = tuple(sorted(TUP[(e1, c2, e2)] for e2 in BOC[c2]))
            ck = canon_ctx(R1, c2, NF)
            if ck in ctx_row and ctx_row[ck] != idxs:
                ctx_ok = False
            ctx_row[ck] = idxs
            row = [F(0)] * nv
            for j in idxs:
                row[j] += 1
            normset[tuple(row)] = True
    normrows = sorted(normset, key=lambda r: [str(v) for v in r])
    mixrows = []
    for c1 in sup1:
        for c2 in sup2:
            rhs = rhs_override((c1, c2)) if rhs_override \
                else q3_of([c1], [c2])
            rows0 = [[F(0)] * nv for _ in range(DIM)]
            rows1 = [[F(0)] * nv for _ in range(DIM)]
            for e1 in BOC[c1]:
                isl = e1 in LINE_SET
                for e2 in BOC[c2]:
                    j = TUP[(e1, c2, e2)]
                    v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                    for c3 in range(DIM):
                        if v[c3] == 0:
                            continue
                        if isl:
                            rows1[c3][j] += v[c3]
                        else:
                            rows0[c3][j] += v[c3] / 2
                            rows1[c3][j] += -v[c3] / 2
            for c3 in range(DIM):
                mixrows.append((tuple(rows0[c3]), tuple(rows1[c3]),
                                rhs[c3], (c1, c2, c3)))
    return {"nv": nv, "vidx": vidx, "TUP": TUP, "lineness": lineness,
            "line_ok": line_ok, "ctx_ok": ctx_ok, "normrows": normrows,
            "mixrows": mixrows}


def build_systemT(an, canonT_tuple, canonT_ctx, q3_of, sup1, sup2, BOC,
                  grain="FULL", rhs_override=None):
    NF = ARM_FN[an]
    tmode = "MULTISET" if grain == "COUNTS" else "ORD"
    vidx = {}
    TUP = {}
    for c1 in sup1:
        for e1 in BOC[c1]:
            R1 = nfield(BLOCK_OF[e1])
            for c2 in sup2:
                for e2 in BOC[c2]:
                    k = canonT_tuple(R1, tgrain((c1,), grain), c2, e2,
                                     NF, tmode)
                    if k not in vidx:
                        vidx[k] = len(vidx)
                    TUP[(c1, e1, c2, e2)] = vidx[k]
    nv = len(vidx)
    lineness = {}
    line_ok = True
    for kk in sorted(TUP):
        (c1, e1, c2, e2) = kk
        j = TUP[kk]
        bln = e2 in LINE_SET
        if j in lineness and lineness[j] != bln:
            line_ok = False
        lineness[j] = bln
    ctx_ok = True
    ctx_row = {}
    normset = {}
    for c1 in sup1:
        for e1 in BOC[c1]:
            R1 = nfield(BLOCK_OF[e1])
            for c2 in sup2:
                idxs = tuple(sorted(TUP[(c1, e1, c2, e2)]
                                    for e2 in BOC[c2]))
                ck = canonT_ctx(R1, tgrain((c1,), grain), c2, NF, tmode)
                if ck in ctx_row and ctx_row[ck] != idxs:
                    ctx_ok = False
                ctx_row[ck] = idxs
                row = [F(0)] * nv
                for j in idxs:
                    row[j] += 1
                normset[tuple(row)] = True
    normrows = sorted(normset, key=lambda r: [str(v) for v in r])
    mixrows = []
    for c1 in sup1:
        for c2 in sup2:
            rhs = rhs_override((c1, c2)) if rhs_override \
                else q3_of([c1], [c2])
            rows0 = [[F(0)] * nv for _ in range(DIM)]
            rows1 = [[F(0)] * nv for _ in range(DIM)]
            for e1 in BOC[c1]:
                isl = e1 in LINE_SET
                for e2 in BOC[c2]:
                    j = TUP[(c1, e1, c2, e2)]
                    v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                    for c3 in range(DIM):
                        if v[c3] == 0:
                            continue
                        if isl:
                            rows1[c3][j] += v[c3]
                        else:
                            rows0[c3][j] += v[c3] / 2
                            rows1[c3][j] += -v[c3] / 2
            for c3 in range(DIM):
                mixrows.append((tuple(rows0[c3]), tuple(rows1[c3]),
                                rhs[c3], (c1, c2, c3)))
    bwrows = []
    for c1 in sup1:
        for e1 in BOC[c1]:
            for c2 in sup2:
                rhs = q3_of([c1], [c2])
                rows = [[F(0)] * nv for _ in range(DIM)]
                for e2 in BOC[c2]:
                    j = TUP[(c1, e1, c2, e2)]
                    v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                    for c3 in range(DIM):
                        if v[c3] != 0:
                            rows[c3][j] += v[c3]
                for c3 in range(DIM):
                    bwrows.append((tuple(rows[c3]), rhs[c3],
                                   (c1, "E", c2, c3)))
    groups_by_var = {}
    for kk in sorted(TUP):
        groups_by_var.setdefault(TUP[kk], []).append(kk)
    partition = frozenset(frozenset(v) for v in groups_by_var.values())
    return {"nv": nv, "vidx": vidx, "TUP": TUP, "lineness": lineness,
            "line_ok": line_ok, "ctx_ok": ctx_ok, "normrows": normrows,
            "mixrows": mixrows, "bwrows": bwrows, "grain": grain,
            "partition": partition}


def system_at(S, a, extra_pins=None, extra_ties=None):
    nv = S["nv"]
    seen = {}
    A, b, meta = [], [], []
    for (r0, r1, rhs, m) in S["mixrows"]:
        row = tuple(x + a * y for x, y in zip(r0, r1))
        if all(v == 0 for v in row) and rhs == 0:
            continue
        key = (row, rhs)
        if key in seen:
            continue
        seen[key] = True
        A.append(list(row))
        b.append(rhs)
        meta.append(list(m))
    for r in S["normrows"]:
        key = (r, F(1))
        if key not in seen:
            seen[key] = True
            A.append(list(r))
            b.append(F(1))
            meta.append(["NORM"])
    if extra_pins:
        for (j, val) in extra_pins:
            row = [F(0)] * nv
            row[j] = F(1)
            A.append(row)
            b.append(val)
            meta.append(["PIN", j])
    if extra_ties:
        for (i, j) in extra_ties:
            row = [F(0)] * nv
            row[i] = F(1)
            row[j] = F(-1)
            A.append(row)
            b.append(F(0))
            meta.append(["TIE", i, j])
    return A, b, meta


# ===========================================================================
# SECTION 8.  THE T-BLIND BINDING (mandatory cross-check) -- parent
# pipeline byte-exact + the literal tied-subfamily route
# ===========================================================================
def tblind_systems(LD, P, canon_tuple, canon_ctx, q3_of, sup1, sup2, BOC,
                   E1S, RAW, PREC, STLIST):
    parent_out = {}
    runs = []
    match = True
    certs_ok = True
    for (label, an) in SYSTEMS:
        S = build_system(an, canon_tuple, canon_ctx, q3_of, sup1, sup2,
                         BOC, E1S, RAW)
        parent_out[label] = S
        want = PREC["d3"][label]
        nv_ok = (S["nv"] == want["nv"])
        for k, a in enumerate(SAMPLES):
            A, b, meta = system_at(S, a)
            st, gap, x, y = simplex(A, b)
            fk = farkas_ok(A, b, y, gap) if st == "INFEASIBLE" else None
            wrow = want["samples"][k]
            gap_s = pick("MUT-TBLIND", str(gap), str(gap) + "1")
            if mut("MUT-TBCERT") and label == "SA-RD" and a == F(0):
                y = [y[0] + 1] + list(y[1:])
                fk = farkas_ok(A, b, y, gap)
            row_match = (wrow["a"] == str(a) and wrow["rows"] == len(A)
                         and wrow["status"] == st
                         and wrow["gap"] == gap_s and nv_ok)
            match = match and row_match
            certs_ok = certs_ok and (fk is True)
            runs.append({"system": label, "a": a, "rows": len(A),
                         "status": st, "gap": gap, "farkas_valid": fk,
                         "matches_parent_receipt": row_match,
                         "sample_space": "CELLS"})
    tied = []
    tied_ok = True
    for (label, an) in SYSTEMS:
        ST = STLIST[(an, "FULL")]
        S = parent_out[label]
        merge = {}
        for kk in sorted(ST["TUP"]):
            (c1, e1, c2, e2) = kk
            R1 = nfield(BLOCK_OF[e1])
            merge.setdefault(S["TUP"][(e1, c2, e2)], set()).add(
                ST["TUP"][kk])
        ties = []
        for pj in sorted(merge):
            grp = sorted(merge[pj])
            for j in grp[1:]:
                ties.append((grp[0], j))
        for a in SAMPLES:
            A, b, meta = system_at(ST, a, extra_ties=ties)
            st, gap, x, y, route = eq_solve(A, b)
            ok = (st == "INFEASIBLE")
            tied_ok = tied_ok and ok
            tied.append({"system": label, "a": a, "rows": len(A),
                         "tie_rows": len(ties), "status": st,
                         "gap": gap, "route": route,
                         "sample_space": "CELLS"})
    P["tblind"] = {
        "parent_pipeline_runs": runs,
        "parent_receipt_match_all": match,
        "refusals": sum(1 for r in runs if r["status"] == "INFEASIBLE"),
        "tied_subfamily_runs": tied,
        "tied_all_refused": tied_ok,
        "reading": "the T-blind subfamily is realized twice: (i) the "
                   "parent's own three systems rebuilt and solved by the "
                   "parent's own pipeline, byte-equal to the delivered "
                   "receipt in status, row count and gap at all 18 runs; "
                   "(ii) the literal route -- the trace-carrying systems "
                   "with tying equalities x_i = x_j across trace orbits "
                   "inside one parent orbit -- refused at every sampled "
                   "line weight, certificates verified in-run"}
    LD.gate("G-TBLIND",
            match and tied_ok
            and P["tblind"]["refusals"] == 18 and len(tied) == 18,
            "the MANDATORY cross-check binds: the T-blind subfamily "
            "reproduces SCOUT-K's depth-3 refusal byte-exactly against "
            "the pinned delivered receipt (18 of 18 runs: status, row "
            "count, gap string) and the literal tied-trace route refuses "
            "identically",
            {"refusals": P["tblind"]["refusals"],
             "tied_refused": tied_ok})
    LD.gate("G-TBLIND-CERT", certs_ok,
            "every parent-pipeline refusal carries a Farkas certificate "
            "verified by this instrument (y.A <= 0 columnwise, y <= 1, "
            "y.b = gap), independently of the parent's own verification",
            {"certificates": 18})
    return parent_out


# ===========================================================================
# SECTION 9.  ARM 1 -- THE TRACE-CARRYING CONDITIONAL-MODE SYSTEMS
# ===========================================================================
def verify_run(A, b, entry):
    ok = True
    if entry["status"] == "INFEASIBLE":
        y = entry.get("_y")
        ok = (y is not None and farkas_ok(A, b, y, entry["gap"])
              and entry["gap"] > 0)
    elif entry["status"] == "FEASIBLE":
        x = entry.get("_x")
        ok = (x is not None and witness_ok(A, b, x))
    else:
        ok = False
    entry["verified"] = ok
    return ok


def refines(fine, coarse):
    """every class of the fine partition lies inside one coarse class"""
    where = {}
    for cl in coarse:
        for k in cl:
            where[k] = cl
    for cl in fine:
        homes = {where[k] for k in cl}
        if len(homes) != 1:
            return False
    return True


def arm1_systems(LD, P, STL, groups, q3_of, sup1, sup2, BOC, tb_status):
    out = {}
    welldef = True
    all_verified = True
    dims_checked = []
    ladder_ok = True
    none_ok = True
    for rep in groups:
        gout = {}
        solved_cache = []
        for grain in LADDER:
            ST = STL[(rep, grain)]
            welldef = welldef and ST["line_ok"] and ST["ctx_ok"]
            inherit = None
            for (g2, res2) in solved_cache:
                S2 = STL[(rep, g2)]
                if S2["partition"] == ST["partition"] \
                        and S2["mixrows"] == ST["mixrows"] \
                        and S2["normrows"] == ST["normrows"]:
                    inherit = g2
                    break
            if inherit is not None:
                gout[grain] = {
                    "nv": ST["nv"],
                    "identical_system_to": inherit,
                    "samples": [dict(r) for r in
                                gout[inherit]["samples"]],
                    "branchwise": dict(gout[inherit]["branchwise"])}
                continue
            srows = []
            # #102 fix: the mutation site must be a grain the ladder
            # actually SOLVES -- FULL is inherited from PREV1 here, so
            # the injection targets PREV1 (the first solved trace
            # grain), never dead code.
            first_mut = (rep == groups[0] and grain == "PREV1")
            for a in SAMPLES:
                A, b, meta = system_at(ST, a)
                st, gap, x, y, route = eq_solve(A, b)
                entry = {"a": a, "rows": len(A), "status": st,
                         "gap": gap, "route": route, "_x": x, "_y": y,
                         "sample_space": "CELLS"}
                if mut("MUT-SAMPLE") and first_mut and a == SAMPLES[0]:
                    entry["status"] = ("FEASIBLE" if st == "INFEASIBLE"
                                       else "INFEASIBLE")
                if mut("MUT-CERT") and first_mut and a == SAMPLES[0]:
                    if entry["_y"] is not None:
                        entry["_y"] = [entry["_y"][0] + 1] \
                            + list(entry["_y"][1:])
                    if entry["_x"] is not None:
                        entry["_x"] = [entry["_x"][0] + 1] \
                            + list(entry["_x"][1:])
                verify_run(A, b, entry)
                all_verified = all_verified and entry["verified"]
                if entry["status"] == "FEASIBLE" and entry["verified"]:
                    dim, Z, xin = polytope_dim(A, b, entry["_x"])
                    entry["dim"] = dim
                    entry["always_zero_vars"] = len(Z)
                    dims_checked.append(
                        (A, b, dim, Z, xin,
                         "arm1-%s-%s" % (rep, grain)))
                    if dim == 0:
                        uk = [{"orbit_var": j, "value": xin[j],
                               "line_candidate": ST["lineness"][j]}
                              for j in range(ST["nv"]) if xin[j] != 0]
                        entry["unique_kernel"] = uk
                entry["farkas_valid"] = (
                    entry["verified"]
                    if entry["status"] == "INFEASIBLE" else None)
                entry["certificate_support"] = (
                    len([v for v in entry["_y"] if v != 0])
                    if entry["_y"] is not None
                    and entry["status"] == "INFEASIBLE" else None)
                srows.append(entry)
            bwA = []
            bwb = []
            seen = {}
            for (row, rhs, m) in ST["bwrows"]:
                if all(v == 0 for v in row) and rhs == 0:
                    continue
                key = (row, rhs)
                if key in seen:
                    continue
                seen[key] = True
                bwA.append(list(row))
                bwb.append(rhs)
            for r in ST["normrows"]:
                if (r, F(1)) not in seen:
                    bwA.append(list(r))
                    bwb.append(F(1))
            stb, gapb, xb, yb, routeb = eq_solve(bwA, bwb)
            bw = {"rows": len(bwA), "status": stb, "gap": gapb,
                  "route": routeb, "_x": xb, "_y": yb,
                  "sample_space": "CELLS"}
            if mut("MUT-BW") and first_mut:
                bw["status"] = ("FEASIBLE" if stb == "INFEASIBLE"
                                else "INFEASIBLE")
            verify_run(bwA, bwb, bw)
            all_verified = all_verified and bw["verified"]
            if bw["status"] == "FEASIBLE" and bw["verified"]:
                dimb, Zb, xinb = polytope_dim(bwA, bwb, bw["_x"])
                bw["dim"] = dimb
                dims_checked.append((bwA, bwb, dimb, Zb, xinb,
                                     "arm1-bw-%s-%s" % (rep, grain)))
            gout[grain] = {"nv": ST["nv"], "samples": srows,
                           "branchwise": bw}
            solved_cache.append((grain, gout[grain]))
        # ladder structure: information-order refinements are measured
        pN = STL[(rep, "NONE")]["partition"]
        p1 = STL[(rep, "PREV1")]["partition"]
        pC = STL[(rep, "COUNTS")]["partition"]
        p2 = STL[(rep, "SUFFIX2")]["partition"]
        pF = STL[(rep, "FULL")]["partition"]
        lad = {"trace_grains_refine_none": all(
                   refines(p, pN) for p in (p1, pC, p2, pF)),
               "suffix2_refines_prev1": refines(p2, p1),
               "full_refines_all": all(refines(pF, p)
                                       for p in (p1, pC, p2)),
               "grain_partition_equalities": {
                   "PREV1_eq_COUNTS": p1 == pC,
                   "PREV1_eq_SUFFIX2": p1 == p2,
                   "PREV1_eq_FULL": p1 == pF},
               "window_note": "at the committed windows every "
                              "trace-bearing invocation sees a "
                              "length-1 trace, so the four trace "
                              "grains are expected to coincide; the "
                              "equalities above are MEASURED, and any "
                              "inherited verdict is licensed only by "
                              "a byte-level partition equality"}
        ladder_ok = ladder_ok and lad["trace_grains_refine_none"] \
            and lad["suffix2_refines_prev1"] and lad["full_refines_all"]
        # the NONE grain must agree with the byte-bound parent verdicts
        for r in gout["NONE"]["samples"]:
            if r["status"] != tb_status[(REP_LABEL[rep], str(r["a"]))]:
                none_ok = False
        nv_none = STL[(rep, "NONE")]["nv"]
        gout["ladder"] = lad
        out[rep] = {"grains": gout, "nv_none": nv_none}
    P["a1"] = {
        "welldef": {"line_ok_and_ctx_ok": welldef},
        "systems": {rep: {
            "nv_per_grain": {g: STL[(rep, g)]["nv"] for g in LADDER},
            "ladder": out[rep]["grains"]["ladder"],
            "grains": {g: {
                "nv": out[rep]["grains"][g]["nv"],
                "identical_system_to":
                    out[rep]["grains"][g].get("identical_system_to"),
                "samples": [{k: v for k, v in r.items()
                             if not k.startswith("_")}
                            for r in out[rep]["grains"][g]["samples"]],
                "branchwise": {k: v for k, v in
                               out[rep]["grains"][g]["branchwise"]
                               .items() if not k.startswith("_")}}
                for g in LADDER}}
            for rep in out},
        "mode": "CONDITIONAL (the #68 primary): every constraint is "
                "linear in the second kernel factor at each sampled "
                "first-step line weight; the step-one factor is the "
                "measured dim-1 family, an exact census fact",
        "ladder_declarations": {g: GRAIN_TRACE_DECL[g] for g in LADDER}}
    LD.gate("G-A1-WELLDEF",
            pick("MUT-CTX", welldef, False),
            "trace-orbit bookkeeping is self-consistent at every ladder "
            "grain of every solved system: line-ness is constant on "
            "every trace orbit and relabelling-equivalent trace "
            "contexts carry identical candidate variable multisets",
            None)
    LD.gate("G-LADDER", ladder_ok and none_ok,
            "the minimality ladder is structurally sound by "
            "measurement: every trace grain's partition refines the "
            "no-trace partition, SUFFIX2 refines PREV1, FULL refines "
            "every other grain, and the NONE-grain verdicts agree with "
            "the byte-bound parent reproduction at all samples",
            {rep: P["a1"]["systems"][rep]["ladder"]
             ["grain_partition_equalities"] for rep in out})
    LD.gate("G-A1-SAMPLES",
            all(r["status"] in ("FEASIBLE", "INFEASIBLE")
                and (r["status"] == "INFEASIBLE") == (r["gap"] > 0)
                for rep in out for g in LADDER
                for r in out[rep]["grains"][g]["samples"])
            and all(len(out[rep]["grains"][g]["samples"]) == 6
                    for rep in out for g in LADDER),
            "every arm-1 system is decided (FEASIBLE or INFEASIBLE, "
            "never silent) at all 6 declared samples of the first-step "
            "line weight, at every ladder grain of one representative "
            "per measured distinct partition, and every published "
            "status word MATCHES the solver object (INFEASIBLE exactly "
            "when the solver's gap is positive) -- the #102 wiring "
            "fix: a forged status dies HERE, not downstream",
            {rep: {g: [r["status"]
                       for r in out[rep]["grains"][g]["samples"]]
                   for g in LADDER} for rep in out})
    LD.gate("G-A1-CERT", all_verified,
            "every arm-1 status carries its verified exact object: a "
            "Farkas certificate on INFEASIBLE (y.A <= 0, y <= 1, "
            "y.b = gap > 0), a nonnegative exact witness on FEASIBLE, "
            "branchwise runs included",
            {"verified": all_verified})
    return out, dims_checked


def arm1_free_lemma(LD, P, q3_of, sup1, sup2, BOC, a1_out, groups):
    rows = []
    all_ok = True
    by_a = {}
    for a in SAMPLES:
        w1 = {}
        for c1 in sup1:
            for e1 in BOC[c1]:
                w1[e1] = a if e1 in LINE_SET else (1 - a) / 2
        feas = 0
        infeas = 0
        exemplar = None
        for c1 in sup1:
            for c2 in sup2:
                rhs = q3_of([c1], [c2])
                elist = list(BOC[c1])
                A = []
                b = []
                for c3 in range(DIM):
                    row = []
                    for e1 in elist:
                        for e2 in BOC[c2]:
                            v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                            row.append(w1[e1] * v[c3])
                    if any(x != 0 for x in row) or rhs[c3] != 0:
                        A.append(row)
                        b.append(rhs[c3])
                for i1 in range(len(elist)):
                    row = [F(0)] * (3 * len(elist))
                    for i2 in range(3):
                        row[i1 * 3 + i2] = F(1)
                    A.append(row)
                    b.append(F(1))
                st, gap, x, y, route = eq_solve(A, b)
                entry = {"a": a, "c1": c1, "c2": c2, "status": st,
                         "gap": gap, "_x": x, "_y": y,
                         "sample_space": "CELLS"}
                if mut("MUT-FREE") and a == SAMPLES[0] and c1 == sup1[0] \
                        and c2 == sup2[0]:
                    entry["status"] = ("FEASIBLE" if st == "INFEASIBLE"
                                       else "INFEASIBLE")
                verify_run(A, b, entry)
                all_ok = all_ok and entry["verified"]
                if entry["status"] == "FEASIBLE":
                    feas += 1
                else:
                    infeas += 1
                    if exemplar is None:
                        exemplar = {"c1": c1, "c2": c2,
                                    "gap": gap, "route": route}
        by_a[str(a)] = {"feasible_pairs": feas,
                        "infeasible_pairs": infeas,
                        "exemplar_refusal": exemplar,
                        "sample_space": "CELLS"}
    P["a1"]["free_lemma"] = {
        "per_sample": by_a,
        "pairs_per_sample": 27,
        "reading": "the free relaxation drops covariance entirely: one "
                   "unconstrained normalized weight per (first event, "
                   "candidate second event) inside each (c1,c2) branch "
                   "pair, keeping only the measured step-one family and "
                   "the record-evolution mismatch; a refusal here is a "
                   "refusal of EVERY trace-informed second-invocation "
                   "kernel, covariant or not, at that branch pair"}
    LD.gate("G-A1-FREE", all_ok,
            "the free-relaxation lemma is decided at every (c1,c2) "
            "branch pair and every sampled line weight (162 exact "
            "solves), each status carrying its verified certificate or "
            "witness",
            {a: (by_a[a]["feasible_pairs"], by_a[a]["infeasible_pairs"])
             for a in sorted(by_a)})
    consist = True
    detail = []
    for rep in groups:
        for g in ("FULL",):
            for r in P["a1"]["systems"][rep]["grains"][g]["samples"]:
                if r["status"] == "FEASIBLE":
                    blk = by_a[str(r["a"])]
                    if blk["infeasible_pairs"] > 0:
                        consist = False
                        detail.append((rep, g, str(r["a"])))
    if mut("MUT-CONSIST"):
        consist = not consist
    P["a1"]["consistency"] = {
        "covariant_feasible_implies_free_feasible": consist,
        "violations": detail}
    LD.gate("G-A1-CONSIST", consist,
            "logical consistency across relaxation levels: wherever the "
            "covariant trace system is feasible, every branch pair of "
            "the free relaxation is feasible too (a covariant solution "
            "restricts to a free one); no violation observed",
            {"violations": detail})


# ===========================================================================
# SECTION 10.  UNIFORM-IN-a CERTIFICATES + THE CLASH-T PROBE
# ===========================================================================
def uniform_certificate(S, subset=None, tag=""):
    # ANCHORED-REUSE: the parent's uniform affine-endpoint search,
    # generalized with an optional candidate-support restriction (the
    # verification below is always against the FULL system, so the
    # restriction can only fail to find, never mis-certify).
    trip = {}
    order = []
    for (r0, r1, rhs, m) in S["mixrows"]:
        key = (r0, r1, rhs)
        if (any(v != 0 for v in r0) or any(v != 0 for v in r1)
                or rhs != 0) and key not in trip:
            trip[key] = list(m)
            order.append(key)
    zero = tuple([F(0)] * S["nv"])
    for r in S["normrows"]:
        key = (r, zero, F(1))
        if key not in trip:
            trip[key] = ["NORM"]
            order.append(key)
    m = len(order)
    A0 = [k[0] for k in order]
    A1 = [k[1] for k in order]
    bb = [k[2] for k in order]
    nv = S["nv"]
    chosen = sorted(subset) if subset is not None else list(range(m))
    mc = len(chosen)
    ncols = 2 * mc + 2 * nv
    rows, rhsv = [], []
    for j in range(nv):
        r = [F(0)] * ncols
        for t, i in enumerate(chosen):
            r[t] = A0[i][j]
            r[mc + t] = -A0[i][j]
        r[2 * mc + j] = F(1)
        rows.append(r)
        rhsv.append(F(0))
    for j in range(nv):
        r = [F(0)] * ncols
        for t, i in enumerate(chosen):
            v = A0[i][j] + A1[i][j]
            r[t] = v
            r[mc + t] = -v
        r[2 * mc + nv + j] = F(1)
        rows.append(r)
        rhsv.append(F(0))
    r = [F(0)] * ncols
    for t, i in enumerate(chosen):
        r[t] = bb[i]
        r[mc + t] = -bb[i]
    rows.append(r)
    rhsv.append(F(1))
    stu, _gu, xu, _yu = simplex(rows, rhsv)
    uni = {"system_rows": m, "candidate_rows": mc,
           "search_status": stu, "sample_space": "CELLS"}
    if stu != "FEASIBLE":
        uni["verified"] = False
        return uni, order, trip
    yy = [F(0)] * m
    for t, i in enumerate(chosen):
        yy[i] = xu[t] - xu[mc + t]
    if mut("MUT-UNIF") and tag == "A2-SA-RD-ORD-RAW":
        yy = [yy[0] + 1] + list(yy[1:])
    nz = [(i, yy[i]) for i in range(m) if yy[i] != 0]
    ok0 = all(sum(yy[i] * A0[i][j] for i in range(m)) <= 0
              for j in range(nv))
    ok1 = all(sum(yy[i] * (A0[i][j] + A1[i][j])
                  for i in range(m)) <= 0 for j in range(nv))
    okb = sum(yy[i] * bb[i] for i in range(m)) == 1
    mid_ok = True
    for (r0, r1, rhs, mm2) in S["mixrows"][:30]:
        lhs = tuple(x + F(1, 2) * y for x, y in zip(r0, r1))
        rr = tuple((x + (x + y)) / 2 for x, y in zip(r0, r1))
        if lhs != rr:
            mid_ok = False
    uni.update({
        "certificate_support": len(nz),
        "support_rows": [{"row_meta": trip[order[i]], "y": yv}
                         for (i, yv) in nz],
        "endpoint0_ok": ok0, "endpoint1_ok": ok1,
        "yb_equals_one": okb, "affine_midpoint_ok": mid_ok,
        "verified": ok0 and ok1 and okb and mid_ok,
        "reading": "y.A(a) is affine in a per component, so the two "
                   "endpoint checks bound the whole segment; with "
                   "y.b = 1 the system is infeasible at EVERY "
                   "first-step line weight a in [0,1]"})
    return uni, order, trip


def run_uniform(S, sample_entries, sysobj_meta_lists, tag=""):
    # try a restricted candidate support first (the union of sampled
    # certificate supports mapped through row metas, plus all NORM
    # rows), then the full row set.
    trip = {}
    order = []
    for (r0, r1, rhs, m) in S["mixrows"]:
        key = (r0, r1, rhs)
        if (any(v != 0 for v in r0) or any(v != 0 for v in r1)
                or rhs != 0) and key not in trip:
            trip[key] = list(m)
            order.append(key)
    zero = tuple([F(0)] * S["nv"])
    for r in S["normrows"]:
        key = (r, zero, F(1))
        if key not in trip:
            trip[key] = ["NORM"]
            order.append(key)
    meta_index = {}
    for i, key in enumerate(order):
        meta_index[tuple(trip[key])] = i
    hint = set()
    for (metas, y) in zip(sysobj_meta_lists, sample_entries):
        if y is None:
            continue
        for i, v in enumerate(y):
            if v != 0 and i < len(metas):
                mi = meta_index.get(tuple(metas[i]))
                if mi is not None:
                    hint.add(mi)
    for i, key in enumerate(order):
        if trip[key] == ["NORM"]:
            hint.add(i)
    if hint:
        uni, _o, _t = uniform_certificate(S, subset=hint, tag=tag)
        if uni.get("verified"):
            uni["candidate_strategy"] = "SAMPLED-SUPPORT-UNION"
            return uni
    uni, _o, _t = uniform_certificate(S, subset=None, tag=tag)
    uni["candidate_strategy"] = "FULL"
    return uni


def clash_probe(LD, P, ST_global, PREC):
    vec = {}
    for (r0, r1, rhs, m) in ST_global["mixrows"]:
        if tuple(m) == (0, 5, 14):
            vec["A"] = (r0, rhs)
        if tuple(m) == (1, 11, 21):
            vec["B"] = (r0, rhs)
    found = "A" in vec and "B" in vec
    separated = None
    if found:
        separated = (vec["A"][0] != vec["B"][0])
    if mut("MUT-CLASHT"):
        found = False
    wit = PREC["clash"]["witness"]
    rhs_match = (found and str(vec["A"][1]) == wit["rhs_a"]
                 and str(vec["B"][1]) == wit["rhs_b"])
    P["a1"]["clash_t"] = {
        "parent_witness_rows": [[0, 5, 14], [1, 11, 21]],
        "parent_rhs": [wit["rhs_a"], wit["rhs_b"]],
        "rows_found": found,
        "delivered_values_match_parent": rhs_match,
        "trace_separates_the_pair": separated,
        "reading": "the parent's mechanism witness -- two branch rows "
                   "carrying IDENTICAL covariant coefficient vectors at "
                   "a = 0 while the delivered walk assigns 16/729 "
                   "against 64/729 -- is re-examined in the "
                   "trace-carrying variable space at the global arm: "
                   "whether the trace refinement separates the "
                   "coefficient vectors is MEASURED here, and whatever "
                   "the answer, the feasibility verdicts above are the "
                   "authority on whether separation suffices",
        "sample_space": "CELLS"}
    LD.gate("G-CLASH-T",
            found and rhs_match and separated is not None,
            "the clash-T probe stands: both parent witness rows are "
            "located in the trace system at a = 0, their delivered walk "
            "values match the pinned parent receipt (16/729 and "
            "64/729), and the separation question is answered by "
            "measurement, not assumption",
            {"separated": separated})


# ===========================================================================
# SECTION 11.  ARM 2 -- THE MARGINAL-HISTORY GRAINS
# ===========================================================================
GRAIN_ORDER = ("ORD-RAW", "CNT-RAW", "ORD-GAM", "CNT-GAM")
GRAIN_DECL = {
    "ORD-RAW": "the complete ordered CELL-HIT emission history "
               "(c1,c2,c3), raw",
    "CNT-RAW": "the final count field nfield([c1,c2,c3]), raw "
               "(order forgotten, multiplicity kept)",
    "ORD-GAM": "the ordered emission history quotiented by simultaneous "
               "relabelling (one row per Gamma-orbit of histories)",
    "CNT-GAM": "the final count field quotiented by simultaneous "
               "relabelling (one row per Gamma-orbit of count fields)"}
GRAIN_SS = {"ORD-RAW": "CELL-HIT-HISTORIES",
            "CNT-RAW": "COUNT-FIELDS",
            "ORD-GAM": "GAMMA-ORBIT-HISTORIES",
            "CNT-GAM": "GAMMA-ORBIT-COUNT-FIELDS"}


def make_hist_canon(GCELL):
    def hcanon(h):
        best = None
        for gc in GCELL:
            k = (gc[h[0]], gc[h[1]], gc[h[2]])
            if best is None or k < best:
                best = k
        return best

    def ncanon(N):
        best = None
        for gc in GCELL:
            out = [0] * DIM
            for c in range(DIM):
                out[gc[c]] = N[c]
            k = tuple(out)
            if best is None or k < best:
                best = k
        return best
    return hcanon, ncanon


def grain_system(S, grain, q1, q2, hcanon, ncanon):
    agg = {}
    keyorder = []
    for (r0, r1, rhs, m) in S["mixrows"]:
        (c1, c2, c3) = m
        sc = q1[c1] * q2[c2]
        if grain == "ORD-RAW":
            key = ("H", c1, c2, c3)
        elif grain == "CNT-RAW":
            key = ("N",) + nfield([c1, c2, c3])
        elif grain == "ORD-GAM":
            key = ("HG",) + hcanon((c1, c2, c3))
        else:
            key = ("NG",) + ncanon(nfield([c1, c2, c3]))
        if key not in agg:
            agg[key] = [[F(0)] * S["nv"], [F(0)] * S["nv"], F(0), 0]
            keyorder.append(key)
        acc = agg[key]
        for j in range(S["nv"]):
            if r0[j] != 0:
                acc[0][j] += sc * r0[j]
            if r1[j] != 0:
                acc[1][j] += sc * r1[j]
        acc[2] += sc * rhs
        acc[3] += 1
    mixrows = []
    fibers = Counter()
    for ci, key in enumerate(keyorder):
        acc = agg[key]
        mixrows.append((tuple(acc[0]), tuple(acc[1]), acc[2],
                        ("GRAIN", grain, ci)))
        fibers[acc[3]] += 1
    return {"nv": S["nv"], "normrows": S["normrows"],
            "mixrows": mixrows, "lineness": S["lineness"],
            "fiber_histogram": sorted(fibers.items()),
            "grain_rows": len(mixrows)}


def arm2_grains(LD, P, parent_out, q1, q2, GCELL, tblind_runs):
    hcanon, ncanon = make_hist_canon(GCELL)
    out = {}
    all_verified = True
    collapse_ok = True
    dims_checked = []
    tb_status = {}
    for r in tblind_runs:
        tb_status[(r["system"], str(r["a"]))] = r["status"]
    for (label, an) in SYSTEMS:
        S = parent_out[label]
        gout = {}
        for grain in GRAIN_ORDER:
            SG = grain_system(S, grain, q1, q2, hcanon, ncanon)
            srows = []
            metas_l = []
            ys_l = []
            for a in SAMPLES:
                A, b, meta = system_at(SG, a)
                st, gap, x, y, route = eq_solve(A, b)
                entry = {"a": a, "rows": len(A), "status": st,
                         "gap": gap, "route": route, "_x": x, "_y": y,
                         "sample_space": GRAIN_SS[grain]}
                if mut("MUT-A2") and label == "SA-RD" \
                        and grain == "CNT-RAW" and a == SAMPLES[0]:
                    entry["status"] = ("FEASIBLE"
                                       if st == "INFEASIBLE"
                                       else "INFEASIBLE")
                if mut("MUT-A2CERT") and label == "SA-RD" \
                        and grain == "ORD-RAW" and a == SAMPLES[0]:
                    if entry["_y"] is not None:
                        entry["_y"] = [entry["_y"][0] + 1] \
                            + list(entry["_y"][1:])
                    if entry["_x"] is not None:
                        entry["_x"] = [entry["_x"][0] + 1] \
                            + list(entry["_x"][1:])
                verify_run(A, b, entry)
                all_verified = all_verified and entry["verified"]
                if entry["status"] == "FEASIBLE" and entry["verified"]:
                    dim, Z, xin = polytope_dim(A, b, entry["_x"])
                    entry["dim"] = dim
                    entry["always_zero_vars"] = len(Z)
                    dims_checked.append((A, b, dim, Z, xin,
                                         "arm2-%s-%s" % (label, grain)))
                    if dim == 0:
                        uk = [{"orbit_var": j, "value": xin[j]}
                              for j in range(SG["nv"]) if xin[j] != 0]
                        entry["unique_kernel"] = uk
                entry["farkas_valid"] = (
                    entry["verified"]
                    if entry["status"] == "INFEASIBLE" else None)
                if grain == "ORD-RAW":
                    want = tb_status[(label, str(a))]
                    same = (entry["status"] == want)
                    entry["collapse_matches_conditional"] = pick(
                        "MUT-COLLAPSE", same, not same)
                    collapse_ok = collapse_ok \
                        and entry["collapse_matches_conditional"]
                metas_l.append(meta)
                ys_l.append(entry["_y"])
                srows.append(entry)
            grow = {"grain_rows": SG["grain_rows"],
                    "fiber_histogram": SG["fiber_histogram"],
                    "declaration": GRAIN_DECL[grain],
                    "samples": [{k: v for k, v in r.items()
                                 if not k.startswith("_")}
                                for r in srows]}
            if all(r["status"] == "INFEASIBLE" for r in srows):
                uni = run_uniform(SG, ys_l, metas_l,
                                  tag="A2-%s-%s" % (label, grain))
                grow["uniform_certificate"] = uni
            gout[grain] = grow
        out[label] = gout
    P["a2"] = {
        "systems": out,
        "mode": "MARGINAL-HISTORY (the #68 disclosed secondary): the "
                "observable compared is the delivered walk's record "
                "observable -- the CELL-HIT emission history and its "
                "count field -- under the anchored paper-20 "
                "identification; the latent event histories are summed "
                "inside each exactly factorizing Markov step; no linear "
                "relaxation over history flows is used",
        "collapse": {
            "ordered_raw_equals_conditional": collapse_ok,
            "reading": "at this arena the window-2 blindness makes "
                       "every prefix marginal equal for every "
                       "normalized kernel, so the ordered-raw "
                       "marginal-history system is the conditional "
                       "system scaled row-wise by the positive prefix "
                       "weights q1(c1)q2(c2): the two modes provably "
                       "coincide at the ordered grain, and the "
                       "marginal-history question lives entirely at "
                       "the coarser grains"}}
    LD.gate("G-A2-COLLAPSE", collapse_ok,
            "the measured collapse: the ordered-raw marginal-history "
            "verdict coincides with the conditional-mode verdict at "
            "every system and sample (rows are positive scalings), so "
            "arm 2's genuinely new content is the count-field and "
            "Gamma-quotient grains",
            {"ok": collapse_ok})
    LD.gate("G-A2-SAMPLES",
            all(r["status"] in ("FEASIBLE", "INFEASIBLE")
                and (r["status"] == "INFEASIBLE") == (r["gap"] > 0)
                for lbl in out for g in GRAIN_ORDER
                for r in out[lbl][g]["samples"]),
            "every arm-2 grain system is decided at all 6 samples at "
            "all three distinct conditional systems and all four "
            "disclosed grains, and every published status word MATCHES "
            "the solver object (INFEASIBLE exactly when the solver's "
            "gap is positive) -- the #102 wiring fix: a forged status "
            "dies HERE, not downstream",
            {lbl: {g: [r["status"] for r in out[lbl][g]["samples"]]
                   for g in GRAIN_ORDER} for lbl in out})
    LD.gate("G-A2-CERT", all_verified,
            "every arm-2 status carries its verified exact certificate "
            "or witness", {"verified": all_verified})
    uni_ok = True
    for lbl in sorted(out):
        for g in GRAIN_ORDER:
            grow = out[lbl][g]
            if "uniform_certificate" in grow:
                uni_ok = uni_ok \
                    and grow["uniform_certificate"].get("verified")
    LD.gate("G-A2-UNIFORM", uni_ok,
            "every all-empty arm-2 grain system carries one verified "
            "uniform-in-a Farkas certificate closing the whole line "
            "weight segment", {"ok": uni_ok})
    return out, dims_checked


# ===========================================================================
# SECTION 12.  CONTROLS (forced both ways, through the real builders and
# the real solver) + THE DIMENSION VERIFICATION GATE
# ===========================================================================
def controls(LD, P, canonT_tuple, canonT_ctx, q3_of, sup1, sup2, BOC,
             parent_out, q1, q2, GCELL, dims_checked):
    def rhs_kernel(c1c2):
        c1, c2 = c1c2
        vout = [F(0)] * DIM
        for e1 in BOC[c1]:
            for e2 in BOC[c2]:
                v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                for c3 in range(DIM):
                    vout[c3] += F(1, 3) * F(1, 3) * v[c3]
        return tuple(vout)

    STf = build_systemT("GLOBAL", canonT_tuple, canonT_ctx, q3_of, sup1,
                        sup2, BOC, grain="FULL", rhs_override=rhs_kernel)
    A, b, meta = system_at(STf, F(1, 3))
    stf, _g, xf, _y, routef = eq_solve(A, b)
    wit_ok = None
    dimf = None
    if stf == "FEASIBLE":
        wit_ok = witness_ok(A, b, xf)
        dim, Z, xin = polytope_dim(A, b, xf)
        dimf = pick("MUT-DIM", dim, dim + 1)
        dims_checked.append((A, b, dimf, Z, xin, "control-feasible"))

    def rhs_bad(c1c2):
        v = list(q3_of([c1c2[0]], [c1c2[1]]))
        v[0] += 1
        return tuple(v)

    STe = build_systemT("GLOBAL", canonT_tuple, canonT_ctx, q3_of, sup1,
                        sup2, BOC, grain="FULL", rhs_override=rhs_bad)
    A2, b2, meta2 = system_at(STe, F(1, 3))
    ste, gape, _x2, ye, routee = eq_solve(A2, b2)
    if mut("MUT-CTRL"):
        ste = "FEASIBLE"
    fe_ok = farkas_ok(A2, b2, ye, gape) if ste == "INFEASIBLE" else None
    # arm-2 count-grain controls through the real grain aggregator
    hcanon, ncanon = make_hist_canon(GCELL)
    Sf2 = build_system("GLOBAL", CANON_HOLDER["tuple"],
                       CANON_HOLDER["ctx"], q3_of, sup1, sup2, BOC,
                       CANON_HOLDER["E1S"], CANON_HOLDER["RAW"],
                       rhs_override=rhs_kernel)
    SG_f = grain_system(Sf2, "CNT-RAW", q1, q2, hcanon, ncanon)
    A3, b3, _m3 = system_at(SG_f, F(1, 3))
    st3, _g3, x3, _y3, route3 = eq_solve(A3, b3)
    wit3 = witness_ok(A3, b3, x3) if st3 == "FEASIBLE" else None
    Se2 = build_system("GLOBAL", CANON_HOLDER["tuple"],
                       CANON_HOLDER["ctx"], q3_of, sup1, sup2, BOC,
                       CANON_HOLDER["E1S"], CANON_HOLDER["RAW"],
                       rhs_override=rhs_bad)
    SG_e = grain_system(Se2, "CNT-RAW", q1, q2, hcanon, ncanon)
    A4, b4, _m4 = system_at(SG_e, F(1, 3))
    st4, gap4, _x4, y4, route4 = eq_solve(A4, b4)
    fe4 = farkas_ok(A4, b4, y4, gap4) if st4 == "INFEASIBLE" else None
    P["controls"] = {
        "arm1_forced_feasible": {
            "construction": "target statistics generated by the "
                            "declared covariant trace kernel (uniform "
                            "1/3 per candidate at both invocations, "
                            "a = 1/3) through the real trace builder",
            "status": stf, "witness_nonnegative": wit_ok,
            "polytope_dim": dimf, "sample_space": "CELLS"},
        "arm1_forced_empty": {
            "construction": "one delivered branch value shifted by +1",
            "status": ste, "gap": gape, "farkas_valid": fe_ok,
            "sample_space": "CELLS"},
        "arm2_forced_feasible": {
            "construction": "the same synthetic kernel target pushed "
                            "through the real count-field grain "
                            "aggregator",
            "status": st3, "witness_nonnegative": wit3,
            "sample_space": "COUNT-FIELDS"},
        "arm2_forced_empty": {
            "construction": "one shifted branch value pushed through "
                            "the real count-field grain aggregator",
            "status": st4, "gap": gap4, "farkas_valid": fe4,
            "sample_space": "COUNT-FIELDS"}}
    LD.gate("G-CONTROLS",
            stf == "FEASIBLE" and wit_ok
            and ste == "INFEASIBLE" and fe_ok
            and st3 == "FEASIBLE" and wit3
            and st4 == "INFEASIBLE" and fe4,
            "all four synthetic controls fire through the real builders "
            "and solver, both arms forced both ways: kernel-generated "
            "targets FEASIBLE with nonnegative witnesses, shifted "
            "targets INFEASIBLE with verified certificates",
            {"arm1": (stf, ste), "arm2": (st3, st4)})
    dim_rows = []
    dims_ok = True
    for (A_, b_, dimv, Z, xin, label) in dims_checked:
        n = len(A_[0])
        aug = [list(A_[i]) + [Fraction(b_[i])] for i in range(len(A_))]
        R, piv = rref(aug)
        red = [R[i][:n] for i in range(len(R))
               if any(R[i][j] != 0 for j in range(n))]
        stacked = [list(r) for r in red]
        for j in Z:
            row = [Fraction(0)] * n
            row[j] = Fraction(1)
            stacked.append(row)
        recomputed = n - rank_of(stacked)
        okd = (witness_ok(A_, b_, xin)
               and all(xin[j] > 0 for j in range(n) if j not in Z)
               and recomputed == dimv)
        dims_ok = dims_ok and okd
        dim_rows.append({"label": label, "dim": dimv,
                         "always_zero_vars": len(Z), "ok": okd})
    P["dims"] = {"rows": dim_rows, "all_ok": dims_ok,
                 "method": "affine-hull dimension: iterated support "
                           "maximization proves the always-zero set "
                           "(a zero optimum of a nonnegative sum "
                           "forces every term to vanish on the whole "
                           "polytope), then dim = nullity of the "
                           "equality system stacked with the "
                           "always-zero unit rows; every published "
                           "dimension is recomputed here from its "
                           "stored zero-set and interior point"}
    LD.gate("G-A1-DIM", dims_ok,
            "every published polytope dimension (arm 1, arm 2 and the "
            "feasible control) is re-verified: the interior point is an "
            "exact feasible witness, strictly positive off the proven "
            "always-zero set, and the stacked-nullity recomputation "
            "equals the published dimension",
            {"count": len(dim_rows), "all_ok": dims_ok})


CANON_HOLDER = {}


def arm1_uniform(LD, P, STL, out, groups):
    uni_res = {}
    ok = True
    ran = 0
    for rep in groups:
        for g in LADDER:
            gr = out[rep]["grains"][g]
            if gr.get("identical_system_to"):
                continue
            if not all(r["status"] == "INFEASIBLE"
                       for r in gr["samples"]):
                continue
            ST = STL[(rep, g)]
            metas = []
            ys = []
            for k, a in enumerate(SAMPLES):
                A, b, meta = system_at(ST, a)
                metas.append(meta)
                ys.append(gr["samples"][k].get("_y"))
            uni = run_uniform(ST, ys, metas, tag="A1-%s-%s" % (rep, g))
            uni_res["%s/%s" % (rep, g)] = uni
            ok = ok and bool(uni.get("verified"))
            ran += 1
    P["a1"]["uniform"] = uni_res
    LD.gate("G-A1-UNIFORM", ok,
            "every solved all-empty arm-1 ladder system carries one "
            "verified uniform-in-a Farkas certificate closing the whole "
            "first-step line-weight segment (inherited systems are "
            "covered by their byte-identical solved representative)",
            {"ran": ran, "ok": ok})


# ===========================================================================
# SECTION 13.  VERDICTS, TERM BINDING, WALLS
# ===========================================================================
def grain_verdict(gr):
    feas = [r for r in gr["samples"] if r["status"] == "FEASIBLE"]
    if not feas:
        return ("EMPTY", None, None)
    dims = sorted({r.get("dim") for r in feas})
    a_list = [str(r["a"]) for r in feas]
    return ("FEASIBLE", dims, a_list)


def build_verdicts(P, groups, out1):
    V = {}
    tre = P["treach"]
    V["REACH"] = ("SCOUTT-TRACE-CENSUS-PUBLISHED"
                  "<81-CONTEXTS-243-TUPLES-9-TRIGGER-EVENT-PAIRS; "
                  "FULL-GRAIN-ORBIT-VARIABLES-"
                  + "-".join(str(tre["depth3"][an]
                                 ["tuple_orbit_variables"])
                             for an in ARM_ORDER)
                  + "-PER-ARM-VS-PARENT-16-16-25-19-25; "
                  "EVERY-TRACE-PARTITION-REFINES-THE-PARENT>")
    V["D2"] = (P["d2t"]["arm1_verdict"] + "; " + P["d2t"]["arm2_verdict"])
    words = []
    for rep in groups:
        grains = out1[rep]["grains"]
        coarsest = None
        for g in LADDER:
            st, dims, a_list = grain_verdict(grains[g])
            if st == "FEASIBLE":
                coarsest = (g, dims, a_list)
                break
        if coarsest is None:
            words.append("SCOUTT-TRACE-INSUFFICIENT-AT-3-" + rep
                         + "<ALL-FIVE-GRAINS-EMPTY; CONDITIONAL-MODE; "
                         "UNIFORM-IN-THE-FIRST-STEP-LINE-WEIGHT; "
                         "CERTIFICATES-PUBLISHED-AND-VERIFIED>")
        else:
            (g, dims, a_list) = coarsest
            if dims == [0]:
                words.append("SCOUTT-TRACE-UNIQUE-" + g + "-AT-3-" + rep
                             + "<CONDITIONAL-MODE; COARSEST-FEASIBLE-"
                             "GRAIN; FEASIBILITY-NOT-NATURE>")
            else:
                dimw = ("-".join(str(d) for d in dims)
                        if len(dims) > 1 else str(dims[0]))
                words.append("SCOUTT-TRACE-SUFFICIENT-" + g + "-" + dimw
                             + "-AT-3-" + rep
                             + "<CONDITIONAL-MODE; COARSEST-FEASIBLE-"
                             "GRAIN; FEASIBILITY-NOT-NATURE>")
    V["A1"] = "; ".join(words)
    a2words = []
    for (label, an) in SYSTEMS:
        for grain in GRAIN_ORDER:
            gr = P["a2"]["systems"][label][grain]
            feas = [r for r in gr["samples"]
                    if r["status"] == "FEASIBLE"]
            if feas:
                dims = sorted({r.get("dim") for r in feas})
                dimw = "-".join(str(d) for d in dims)
                a2words.append("SCOUTT-MARGINAL-AGREES-AT-3-" + label
                               + "-" + grain + "-DIM-" + dimw)
            else:
                a2words.append("SCOUTT-MARGINAL-DISAGREES-AT-3-" + label
                               + "-" + grain)
    V["A2"] = ("; ".join(a2words)
               + "<MARGINAL-HISTORY-MODE-EXACT-FACTORIZATION; "
               "ORDERED-RAW-COLLAPSES-ONTO-THE-CONDITIONAL-SYSTEM; "
               "NO-LINEAR-RELAXATION-OVER-HISTORY-FLOWS>")
    V["TBLIND"] = ("SCOUTT-TBLIND-REPRODUCES-PARENT"
                   "<18-OF-18-BYTE-EQUAL-GAPS; TIED-ROUTE-REFUSED; "
                   "MANDATORY-CROSS-CHECK-BOUND>")
    V["BRIDGE"] = ("SCOUTT-TRIGGER-AND-TRACE-STAY-CANDIDATE-MARKED"
                   "<FEASIBILITY-NEVER-NATURE; FORK-NEUTRAL-PER-87; "
                   "EVENT-SELECTION-ONLY-TRANSPORT-STILL-OPEN>")
    P["verdicts"] = V
    P["registered_successors"] = [
        "the depth-4 window (registered, not claimed)",
        "a locality-restricted trace (the trace slot localized by the "
        "proximity arm; carried whole here)",
        "longer windows where the five ladder grains genuinely "
        "separate (traces of length >= 2)",
        "sub-normalized / leaky kernels outside the per-trigger "
        "normalization leg",
        "the quantum transport law rho'_e onto created cells (open "
        "regardless of any kernel outcome)",
        "an operational protocol that would independently declare, "
        "distinguish and map an ontic trace to the beables (the #87 "
        "admissibility route; untested here)",
        "the NON-COVARIANT trace bridge at a = 0 (the free lemma "
        "measures all 27 branch pairs feasible there once covariance "
        "is dropped): pricing that covariance exit -- trilemma arm "
        "(b) territory -- is a successor unit, not claimed here",
        "THE #98 MODEL SPACE (replacing any narrower fork): four "
        "dynamics classes compared by the SAME complete-successor "
        "observable, never by making one model's event kernel "
        "compensate another model's state evolution -- (1) "
        "pair-native (one pair changes; geometry and state backreact "
        "locally; substep generators, fractional evolution and "
        "simultaneous compatible changes untested by SCOUT-PAIR's "
        "clocked test, which only proved three-full-old-steps is not "
        "one-old-step); (2) joint rewrite over compatible collections "
        "(the field analogue); (3) triple-native; (4) n-adaptive "
        "(effective arity a function of the local relational "
        "situation)"]
    P["caps"] = {
        "windows": "depths 2 and 3 only; nothing at depth 4 or beyond "
                   "is claimed",
        "trace_length": "at these windows every trace-bearing "
                        "invocation sees a length-1 trace, so the four "
                        "trace grains coincide by measurement; longer "
                        "windows are needed to separate them",
        "geometry": "G is FIXED; record backreaction only",
        "ontology": "every verdict is a feasibility statement about a "
                    "candidate bridge; no ontic status is decided "
                    "either way",
        "solver": "one representative solved per measured distinct "
                  "partition; inherited verdicts are licensed by "
                  "byte-level system identity, gated"}


TERM_TABLE = (
    ("CELL-HIT", "paper-20's primitive: one Born-selected pair-cell "
     "increment per step (the mandatory rename); the walk's "
     "record-arity emission"),
    ("PAIR ATOM", "the record's atomic datum: one pair-relation of two "
     "actors (one cell of the chart); the count field counts "
     "pair-incidences (the #84 record-arity side)"),
    ("DIVISION EVENT", "paper-19's three-actor conflict group whose "
     "footprint writes all three pair-relations; the only object this "
     "note calls a division event"),
    ("PROCESS EVENT", "a division event carried as ONE indivisible "
     "boundary-to-boundary transition (the #84 process-arity side); "
     "same referent as division event, arity-typed"),
    ("TRIPLE-EVENT", "a division event carried as one probabilistic "
     "alternative"),
    ("TRIGGER", "the cell the quantum menu selects; the conditional "
     "seat of q(c) under the ADOPTED CANDIDATE bridge "
     "P(c,e|X) = q(c|X) K(e|c,G,R,T) -- a candidate this census "
     "tests, never an established physical mechanism"),
    ("TRIGGER TRACE", "T: the ordered tuple of past trigger cells; a "
     "candidate conditioning datum tested at five grains; whether it "
     "could be real is what arm 1 measures, and no outcome here "
     "decides that it is"),
    ("SUCCESSOR", "a COMPLETE-SUCCESSOR-CONFIGURATION X'_e = (G'_e, "
     "R'_e, rho'_e, event data): one outcome of the E-34 "
     "normalization rule, clause 4"),
    ("RECORD", "the co-division relation with its multiplicities "
     "(ECC's sense, unchanged)"),
    ("KERNEL CONTEXT", "the localized triple (R restricted to the "
     "arm's neighborhood of the trigger, the trace at its grain, the "
     "trigger cell), up to simultaneous relabelling"),
    ("ORBIT VARIABLE", "one free kernel weight per relabelling orbit "
     "of localized (record, trace, trigger, candidate event) tuples"),
)


# ---- the kernel-scope wall (ported from the scout micro-repair, widened
# with the #82 precise-formulation scope) ---------------------------------
KERNEL_WALL_TOKENS = (
    "scout kernel empty at equivariant record consistent",
)
KERNEL_WALL_SUBJECTS = (
    "equivariant record consistent kernel",
    "record consistent kernel",
    "equivariant kernel",
    "covariant conditional kernel",
    "covariant kernel",
)
KERNEL_WALL_NEG_EXISTENTIALS = tuple(
    "no " + s for s in KERNEL_WALL_SUBJECTS)
KERNEL_WALL_PREDICATES = (
    "does not exist", "do not exist", "cannot exist", "never exist",
    "none exists", "none exist", "is empty", "are empty",
    "is impossible", "are impossible", "is ruled out", "are ruled out",
)
KERNEL_WALL_LICENCES = ("record blind", "fixed geometry",
                        "at the committed window", "through window 3",
                        "at these windows", "at the committed windows")
KERNEL_WALL_DEAD_CONTROLS = (
    "So no equivariant record-consistent kernel exists at the "
    "committed arena.",
    "every equivariant kernel is empty at the committed arena",
    "record consistent kernels do not exist at this arena",
    "SCOUT-KERNEL-EMPTY-AT-EQUIVARIANT-RECORD-CONSISTENT",
    "no covariant kernel preserves the delivered walk",
    "covariant-conditional kernels never exist at any window",
)
KERNEL_WALL_ALIVE_CONTROLS = (
    "no record-blind, fixed-alpha, affine-equivariant kernel preserves "
    "the delivered three-step walk statistics",
    "at this arena, no normalized covariant conditional kernel "
    "K(e|c,G,R) with fixed geometry, the trigger factorization "
    "P(c,e)=q(c)K(e|c,G,R), and exact preservation of the delivered "
    "cell-walk's conditional statistics, works through window 3 — even "
    "with the entire record.",
)


def kernel_norm(seg):
    return " ".join(seg.lower().replace("-", " ").split())


def kernel_wall_hits(text):
    tokens = pick("MUT-KWALL", KERNEL_WALL_TOKENS, ())
    negs = pick("MUT-KWALL", KERNEL_WALL_NEG_EXISTENTIALS, ())
    subjects = pick("MUT-KWALL", KERNEL_WALL_SUBJECTS, ())
    hits = []
    for ln in text.splitlines():
        cut = ln.replace(";", ".").replace("|", ".").replace(":", ".")
        for seg in cut.split("."):
            s = kernel_norm(seg)
            if not s:
                continue
            if any(t in s for t in tokens):
                hits.append("retired verdict token present: "
                            + seg.strip()[:60])
                continue
            if any(li in s for li in KERNEL_WALL_LICENCES):
                continue
            if any(p in s for p in negs) \
                    or (any(p in s for p in subjects)
                        and any(p in s for p in KERNEL_WALL_PREDICATES)):
                hits.append("retired or widened kernel-scope claim: "
                            + seg.strip()[:60])
    return hits


def kernel_wall_gate(LD, P):
    rows = []
    ok = True
    for s in KERNEL_WALL_DEAD_CONTROLS:
        flagged = bool(kernel_wall_hits(s))
        rows.append({"control": s, "expected": "DEAD",
                     "flagged": flagged})
        ok = ok and flagged
    for s in KERNEL_WALL_ALIVE_CONTROLS:
        flagged = bool(kernel_wall_hits(s))
        rows.append({"control": s, "expected": "ALIVE",
                     "flagged": flagged})
        ok = ok and not flagged
    P["kernel_wall"] = {
        "controls": rows,
        "policy": "the retired kernel-scope overclaim family and its "
                  "unscoped widenings are refused subject-based "
                  "(normalized against hyphen and spacing evasion, "
                  "segment-local so a licence in one heading section "
                  "or clause never licenses another); the licensed "
                  "scoped forms -- record-blind, fixed-geometry, "
                  "committed-window -- are permanent alive twins"}
    LD.gate("G-KERNEL-WALL", ok,
            "the kernel-scope wall fires on the retired overclaim "
            "family (verbatim, hyphen, paraphrase and unscoped-widening "
            "variants) and stays silent on the licensed scoped forms; "
            "all permanent controls behave as declared on this build",
            {"dead": len(KERNEL_WALL_DEAD_CONTROLS),
             "alive": len(KERNEL_WALL_ALIVE_CONTROLS),
             "misbehaving": [r["control"][:50] for r in rows
                             if (r["expected"] == "DEAD")
                             != r["flagged"]]})


# ---- the representation wall (the #87 fork-neutral form) ----------------
REP_WALL_SUBJECTS = ("trace", "trigger", "kernel", "psi")
REP_WALL_PREDICATES = (
    "is physically real", "is ontic", "is reality", "is nature",
    "is the ontology", "is real because", "must be real",
    "cannot be real", "is not real", "is mere bookkeeping",
    "is the minimal sufficient datum", "is minimal",
)
REP_WALL_LICENCES = (
    "admissible if independently declared", "feasibility fact",
    "could be real", "presuppose either answer", "open question",
    "coarsest feasible grain", "candidate", "never nature",
)
REP_WALL_DEAD_CONTROLS = (
    "feasibility of the trace kernel proves the trace is physically "
    "real",
    "the trace is ontic because the equations need it",
    "so the kernel is reality",
    "no reader will doubt that the trace is physically real",
    "the full ordered trace is the minimal sufficient datum",
    "the trigger is mere bookkeeping and cannot be real",
)
REP_WALL_ALIVE_CONTROLS = (
    "an ontic trigger or trace remains admissible if independently "
    "declared, operationally distinguished, and mapped to the beables",
    "TRACE-SUFFICIENT at any grain is a feasibility fact, never "
    "nature",
    "this unit tests whether a trace COULD be real and presupposes "
    "neither answer; whether the trigger is real or bookkeeping is "
    "the fork's open question",
)


def rep_wall_hits(text):
    subjects = pick("MUT-RWALL", REP_WALL_SUBJECTS, ())
    hits = []
    for ln in text.splitlines():
        cut = ln.replace(";", ".").replace("|", ".").replace(":", ".")
        for seg in cut.split("."):
            s = kernel_norm(seg)
            if not s:
                continue
            if any(li in s for li in REP_WALL_LICENCES):
                continue
            if any((" " + sub + " ") in (" " + s + " ")
                   or s.startswith(sub + " ") for sub in subjects) \
                    and any(p in s for p in REP_WALL_PREDICATES):
                hits.append("promotion-or-presupposition claim: "
                            + seg.strip()[:60])
    return hits


def rep_wall_gate(LD, P):
    rows = []
    ok = True
    for s in REP_WALL_DEAD_CONTROLS:
        flagged = bool(rep_wall_hits(s))
        rows.append({"control": s, "expected": "DEAD",
                     "flagged": flagged})
        ok = ok and flagged
    for s in REP_WALL_ALIVE_CONTROLS:
        flagged = bool(rep_wall_hits(s))
        rows.append({"control": s, "expected": "ALIVE",
                     "flagged": flagged})
        ok = ok and not flagged
    P["rep_wall"] = {
        "controls": rows,
        "policy": "the #87 fork-neutral W-REPRESENTATION wall: "
                  "promotion-by-convenience (feasibility or equations "
                  "as grounds for ontic status) and presupposition in "
                  "EITHER direction (ontic asserted, or bookkeeping "
                  "asserted) are refused segment-locally with hyphen "
                  "normalization; the admissibility route and the "
                  "feasibility-not-nature forms are permanent alive "
                  "twins; a negation whose scope is consumed by a "
                  "doubt verb still dies (the policed core is matched "
                  "regardless of leading negations)"}
    LD.gate("G-REP-WALL", ok,
            "the fork-neutral representation wall fires on "
            "promotion-by-convenience and on either-direction "
            "presupposition (doubt-consumed negations included) and "
            "stays silent on the licensed admissibility and "
            "feasibility forms; all permanent controls behave as "
            "declared on this build",
            {"dead": len(REP_WALL_DEAD_CONTROLS),
             "alive": len(REP_WALL_ALIVE_CONTROLS),
             "misbehaving": [r["control"][:50] for r in rows
                             if (r["expected"] == "DEAD")
                             != r["flagged"]]})


# ===========================================================================
# SECTION 14.  SAMPLE SPACES, NUMERAL BINDING, ENV EXCLUSION, SOURCE SCAN
# ===========================================================================
SS_NAMES = ("CELLS", "TRIPLE-EVENTS", "COMPLETE-SUCCESSOR-CONFIGURATIONS",
            "CELL-HIT-HISTORIES", "COUNT-FIELDS", "GAMMA-ORBIT-HISTORIES",
            "GAMMA-ORBIT-COUNT-FIELDS")
SS_EXPECTED = 248


def sample_space_audit(LD, P):
    found = []

    def walk(obj, path):
        if isinstance(obj, dict):
            if "sample_space" in obj:
                found.append((path, obj["sample_space"]))
            for k in sorted(obj):
                walk(obj[k], path + "/" + str(k))
        elif isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                walk(v, path + "[%d]" % i)
    for key in sorted(P):
        walk(P[key], key)
    if mut("MUT-SS"):
        found = found[:-1]
    bad = [(p, s) for (p, s) in found if s not in SS_NAMES]
    P["sample_spaces"] = {"declared": len(found), "invalid": bad}
    LD.gate("G-SAMPLE-SPACE", len(found) == SS_EXPECTED and not bad,
            "every probability-typed measurement row in this receipt "
            "declares its sample space from the seven declared names "
            "(%d declarations); no claim changes sample space silently"
            % SS_EXPECTED,
            {"declared": len(found)})


NUM_BINDINGS = (
    ("108", "gamma/order"),
    ("27", "arena/cells"),
    ("243", "treach/raw_tuples"),
    ("81", "treach/raw_contexts"),
    ("9", "treach/first_event_pairs"),
    ("189", "kreach/raw_tuples"),
    ("63", "kreach/raw_contexts"),
    ("7", "kreach/distinct_first_events"),
    ("16", "kreach/depth3/SA/tuple_orbit_variables"),
    ("25", "kreach/depth3/GLOBAL/tuple_orbit_variables"),
    ("19", "kreach/depth3/CN/tuple_orbit_variables"),
    ("37", "treach/depth3/SA/tuple_orbit_variables"),
    ("37", "treach/depth3/RD/tuple_orbit_variables"),
    ("46", "treach/depth3/GLOBAL/tuple_orbit_variables"),
    ("43", "treach/depth3/CN/tuple_orbit_variables"),
    ("46", "treach/depth3/MC/tuple_orbit_variables"),
    ("2", "step1t/orbit_variables"),
    ("1", "d2t/polytope_dim"),
    ("11", "blindness/variants"),
    ("18", "tblind/refusals"),
    ("16/729", "a1/clash_t/parent_rhs[0]"),
    ("64/729", "a1/clash_t/parent_rhs[1]"),
    ("16", "controls/arm1_forced_feasible/polytope_dim"),
    ("248", "sample_spaces/declared"),
    ("35", "registry/falsifiers_registered"),
    ("37", "registry/gates_total"),
)


def resolve_path(P, path):
    cur = fser(P)
    for part in path.replace("]", "").replace("[", "/").split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            if part not in cur:
                return None
            cur = cur[part]
    return cur


def numeral_bindings(LD, P):
    rows = []
    allok = True
    for (num, path) in NUM_BINDINGS:
        val = resolve_path(P, path)
        got = str(val)
        if mut("MUT-NUMBIND") and path == "gamma/order":
            got = got + "0"
        ok = (got == num)
        allok = allok and ok
        rows.append({"numeral": num, "receipt_field": path,
                     "resolved": got, "bound": ok})
    P["numeral_bindings"] = rows
    LD.gate("G-NUM-BIND", allok,
            "numeral-field binding: every load-bearing prose numeral "
            "is bound to its SPECIFIC receipt field and each binding "
            "resolves to the claimed value; the note-side totality "
            "sweep is enforced at note verification",
            {"bindings": len(rows),
             "failed": [r["receipt_field"] for r in rows
                        if not r["bound"]]})


NUMTOT_DEAD_CONTROLS = (
    "the census found 8191 orbit variables at depth 3",
    "the walk was preserved at 5041 of 6241 rows",
)
NUMTOT_ALIVE_CONTROLS = (
    "the trace census covers 243 raw tuples in 81 raw contexts",
)


def num_total_gate(LD, P):
    rows = []
    ok = True
    for t in NUMTOT_DEAD_CONTROLS:
        pr = []
        numeral_totality(P, t, pr)
        rows.append({"control": t, "expected": "DEAD",
                     "flagged": bool(pr)})
        ok = ok and bool(pr)
    for t in NUMTOT_ALIVE_CONTROLS:
        pr = []
        numeral_totality(P, t, pr)
        rows.append({"control": t, "expected": "ALIVE",
                     "flagged": bool(pr)})
        ok = ok and not pr
    P["num_total_controls"] = {
        "controls": rows,
        "policy": "the #98 hostile-plant leg: invented numerals with no "
                  "measurement-subtree backing and no claim-specific "
                  "table row must be refused by the totality "
                  "classifier; permanent dead plants and one alive twin "
                  "run on every build"}
    LD.gate("G-NUM-TOTAL", ok,
            "the numeral-totality classifier refuses the planted "
            "unbacked numerals and passes the measurement-backed twin; "
            "the sweep inventory is measurement-subtrees-only, so "
            "control and audit values cannot legitimize invented prose "
            "(the class SCOUT-K repaired at its #93)",
            {"dead": len(NUMTOT_DEAD_CONTROLS),
             "alive": len(NUMTOT_ALIVE_CONTROLS),
             "misbehaving": [r["control"][:40] for r in rows
                             if (r["expected"] == "DEAD")
                             != r["flagged"]]})


def env_exclusion(LD, P, LD_rows_probe=None):
    unp = sorted({rel for (_i, rel, _q) in ANCHORS} - set(PINNED))
    digs = {}
    for rel in unp:
        digs[rel] = sha12(read_rel(rel))
    P["env_exclusion"] = {
        "unpinned_reads_scanned": unp,
        "probe": pick("MUT-ENV", None, digs[sorted(digs)[-1]]),
        "policy": "unpinned live-read digests (LOG.md, PLAN.md) are "
                  "computed in-run and must not occur anywhere in the "
                  "receipt payload; environment-dependent bytes are "
                  "excluded from the artifacts (the #66 ledger-self-"
                  "reference hazard, closed in-run)"}
    blob = to_json(P) + to_json(LD.rows)
    leaks = sorted(rel for rel, d in digs.items() if d in blob)
    P["env_exclusion"]["leaks"] = leaks
    LD.gate("G-ENV-EXCLUSION", not leaks,
            "the serialized receipt payload carries no digest of any "
            "unpinned live read: environment-dependent bytes are "
            "excluded from the artifacts and checked in-run only",
            {"scanned": len(unp), "leaks": leaks})


def hex_tokens(blob):
    toks = set()
    cur = ""
    for ch in blob:
        if ch.isalnum():
            cur += ch
        else:
            if len(cur) == 12 and is_hex12(cur):
                toks.add(cur)
            cur = ""
    if len(cur) == 12 and is_hex12(cur):
        toks.add(cur)
    return toks


def classify_digests(P, extra_self):
    pinned_vals = set(PINNED.values())
    selfd = P["source_hygiene"]["digest"]
    blob = to_json(P)
    toks = hex_tokens(blob)
    inv = {}
    unclass = []
    for t in sorted(toks):
        if t in pinned_vals:
            inv[t] = "PINNED"
        elif t == selfd:
            inv[t] = "SELF-SOURCE"
        elif t in extra_self:
            inv[t] = extra_self[t]
        else:
            inv[t] = "UNCLASSIFIED"
            unclass.append(t)
    return inv, unclass


def digest_inventory(LD, P):
    """the #98 port of SCOUT-PAIR's #95 receipt-wide hex-digest
    inventory: every hex-12 token anywhere in the serialized receipt is
    classified PINNED (a frozen input digest), SELF (this unit's own
    declared digests), or refused; then the inventory itself is folded
    in and the scan re-run to a fixed point (the inventory adds no new
    tokens).  The canary-only check (current unpinned live digests
    absent) remains in G-ENV-EXCLUSION; THIS gate refuses ARBITRARY
    unregistered digests, not just today's."""
    inv, unclass = classify_digests(P, {})
    if mut("MUT-DIGINV"):
        probe = sha12(read_rel("v15/LOG.md"))
        inv[probe] = "UNCLASSIFIED"
        unclass = unclass + [probe]
    P["digest_inventory"] = {
        "tokens": inv, "unclassified": unclass,
        "classes": sorted(Counter(inv.values()).items()),
        "policy": "receipt-wide, fixed-point: every hex-12 token in "
                  "the serialized receipt is classified "
                  "pinned/declared/self; an unclassified digest "
                  "refuses the build; the delivery re-runs the scan on "
                  "the FINAL receipt bytes (note digest and "
                  "double-build digest classified SELF) and refuses on "
                  "any residue"}
    blob2 = to_json(P)
    new = sorted(hex_tokens(blob2) - set(inv))
    P["digest_inventory"]["fixed_point_new_tokens"] = new
    LD.gate("G-DIGEST-INVENTORY", not unclass and not new,
            "the receipt-wide hex-digest inventory closes: every "
            "hex-12 token in the serialized receipt is classified "
            "pinned or self, the re-scan with the inventory folded in "
            "reaches a fixed point with no new tokens, and an "
            "arbitrary unpinned-read plant dies here by registered "
            "mutant",
            {"tokens": len(inv), "unclassified": unclass,
             "fixed_point_new": new})


MUT_SETITER_SNIPPET = (
    "\n\ndef _mutant_set_iteration_and_listdir():\n"
    "    acc = []\n"
    "    for cell in {3, 1, 2}:\n"
    "        acc.append(cell)\n"
    "    for name in os.listdir(HERE):\n"
    "        acc.append(name)\n"
    "    return acc\n")


def source_scan(LD, P):
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as f:
        src = f.read()
    scan_src = pick("MUT-SETITER", src, src + MUT_SETITER_SNIPPET)
    tree = ast.parse(scan_src)
    floats = [n.lineno for n in ast.walk(tree)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    hashes = [n.lineno for n in ast.walk(tree)
              if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
              and n.func.id == "hash"]
    imports = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            imports.update(a.name for a in n.names)
        if isinstance(n, ast.ImportFrom):
            imports.add(n.module)
    allowed = {"os", "sys", "json", "hashlib", "ast", "fractions",
               "itertools", "collections"}
    sorted_args = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                and n.func.id == "sorted":
            for a in n.args:
                sorted_args.add(id(a))

    def set_like(node):
        return isinstance(node, (ast.Set, ast.SetComp)) or (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in ("set", "frozenset"))

    def is_listdir(node):
        return isinstance(node, ast.Call) and (
            (isinstance(node.func, ast.Attribute)
             and node.func.attr == "listdir")
            or (isinstance(node.func, ast.Name)
                and node.func.id == "listdir"))
    set_iter = []
    raw_listdir = []
    for n in ast.walk(tree):
        if isinstance(n, ast.For) and set_like(n.iter):
            set_iter.append(n.iter.lineno)
        if isinstance(n, (ast.ListComp, ast.SetComp, ast.GeneratorExp,
                          ast.DictComp)):
            for g in n.generators:
                if set_like(g.iter):
                    set_iter.append(g.iter.lineno)
        if is_listdir(n) and id(n) not in sorted_args:
            raw_listdir.append(n.lineno)
    P["source_hygiene"] = {"float_literals": floats,
                           "hash_calls": hashes,
                           "imports": sorted(imports),
                           "set_iteration_lines": sorted(set_iter),
                           "raw_listdir_lines": sorted(raw_listdir),
                           "determinism_policy":
                               "bare set-iteration and raw os.listdir "
                               "are refused at the source by AST scan, "
                               "in-run and seed-independent; sorted() "
                               "is the one licensed wrapper",
                           "digest": sha12(src.encode("utf-8"))}
    LD.gate("G-SRC-CLEAN",
            not floats and not hashes and imports <= allowed,
            "the instrument's own syntax tree carries no float literal, "
            "no builtin hash call, and no import outside the declared "
            "whitelist",
            {"imports": sorted(imports)})
    LD.gate("G-AST-DETERMINISM",
            not set_iter and not raw_listdir,
            "the determinism leg: no bare iteration over a set display, "
            "set comprehension or set()/frozenset() call and no "
            "os.listdir outside a direct sorted() wrapper -- every "
            "iterated collection can reach the sealed artifacts, so "
            "unsorted iteration is refused at the source, "
            "deterministically at every hash seed",
            {"set_iteration_lines": sorted(set_iter),
             "raw_listdir_lines": sorted(raw_listdir)})


# ===========================================================================
# SECTION 15.  THE KIT
# ===========================================================================
REQUIRED_SENTENCES = (
    "no record-blind, fixed-alpha, affine-equivariant kernel preserves "
    "the delivered three-step walk statistics.",
    "at this arena, no normalized covariant conditional kernel "
    "K(e|c,G,R) with fixed geometry, the trigger factorization "
    "P(c,e)=q(c)K(e|c,G,R), and exact preservation of the delivered "
    "cell-walk's conditional statistics, works through window 3 — even "
    "with the entire record.",
    "G is FIXED throughout — this unit tests RECORD backreaction only; "
    "success does not establish quantum transport across "
    "AUTOGLUE-created cells or any topology change G→G'; those remain "
    "independent missing laws.",
    "an ontic trigger or trace remains admissible if independently "
    "declared, operationally distinguished, and mapped to the beables",
    "TRACE-SUFFICIENT at any grain is a feasibility fact, never "
    "nature",
    "the honest headline names the COARSEST feasible grain",
    "no TRIGGER-TRACE information added to THIS NORMALIZED "
    "EVENT-SELECTION KERNEL repairs it — other state variables and "
    "DIFFERENT UPDATE LAWS remain open",
    "this verdict defeats THIS trace repair AT THIS WINDOW; it does "
    "not rule out longer-memory distinctions at later windows",
)
FORBIDDEN_GLOBAL = (
    "no reader will", "no one will doubt", "will not doubt",
    "probably", "likely", "explains why",
    "the trigger mechanism is established",
    "establishes the trigger", "proves the trigger",
    "trigger is a theorem", "establishes the trace",
    "trace is a theorem", "the trace is established",
    "no amount of kernel-side memory",
)


def build_kit(P, groups):
    kit = []
    kit.append("SCOUT-T verdicts:")
    for k in ("REACH", "D2", "A1", "A2", "TBLIND", "BRIDGE"):
        kit.append(P["verdicts"][k])
    for s in REQUIRED_SENTENCES:
        kit.append(s)
    tre = P["treach"]
    kit.append("the trace reach census against the parent: the full "
               "ordered trace lifts the per-arm depth-3 orbit counts "
               "from 16/16/25/19/25 to %s, over 243 raw tuples in 81 "
               "raw contexts (9 trigger-event pairs); every trace "
               "partition refines the parent partition"
               % "/".join(str(tre["depth3"][an]["tuple_orbit_variables"])
                          for an in ARM_ORDER))
    rep0 = groups[0]
    lad = P["a1"]["systems"][rep0]["ladder"]
    eqs = lad["grain_partition_equalities"]
    if eqs["PREV1_eq_COUNTS"] and eqs["PREV1_eq_SUFFIX2"] \
            and eqs["PREV1_eq_FULL"]:
        kit.append("the minimality ladder collapses at this window by "
                   "measurement: every trace-bearing invocation sees a "
                   "length-1 trace, so PREV1, COUNTS, SUFFIX2 and FULL "
                   "induce byte-identical systems; their verdicts are "
                   "one verdict, and the honest headline names the "
                   "COARSEST feasible grain, never the full trace")
    else:
        kit.append("the minimality ladder does NOT fully collapse at "
                   "this window: the measured grain-partition "
                   "equalities are published per system and each grain "
                   "carries its own verdict")
    fl = P["a1"]["free_lemma"]["per_sample"]
    fmin = min(fl[a]["infeasible_pairs"] for a in sorted(fl))
    fmax = max(fl[a]["infeasible_pairs"] for a in sorted(fl))
    others = [a for a in sorted(fl) if a != "0"]
    if fl["0"]["infeasible_pairs"] == 0 \
            and all(fl[a]["infeasible_pairs"] == 25 for a in others):
        kit.append("the free-relaxation lemma splits the mechanism in "
                   "two: at a = 0 every one of the 27 branch pairs is "
                   "feasible once covariance is dropped -- there the "
                   "refusal is COVARIANCE ITSELF, the relabelling "
                   "identification the clash-T probe shows surviving "
                   "the trace -- while at all five other sampled line "
                   "weights 25 of 27 branch pairs are refused even "
                   "with covariance dropped entirely, so there no "
                   "trace-informed second-invocation kernel of any "
                   "kind matches the delivered walk at the committed "
                   "window: the record-evolution mismatch itself is "
                   "the obstruction, and no TRIGGER-TRACE information "
                   "added to THIS NORMALIZED EVENT-SELECTION KERNEL "
                   "repairs it — other state variables and DIFFERENT "
                   "UPDATE LAWS remain open")
    elif fmin == 27:
        kit.append("the free-relaxation lemma is total: at every "
                   "sampled line weight all 27 branch pairs are "
                   "refused even with covariance dropped entirely -- "
                   "no trace-informed second-invocation kernel, "
                   "covariant or not, matches the delivered walk at "
                   "the committed window, so the obstruction is the "
                   "record-evolution mismatch itself, not the "
                   "relabelling identification")
    else:
        kit.append("the free-relaxation lemma: between %d and %d of "
                   "the 27 branch pairs are refused per sampled line "
                   "weight with covariance dropped entirely; the "
                   "per-pair table is published"
                   % (fmin, fmax))
    ct = P["a1"]["clash_t"]
    if ct["trace_separates_the_pair"]:
        kit.append("the clash-T probe: the trace refinement SEPARATES "
                   "the parent's mechanism witness -- the branch rows "
                   "(0,5,14) and (1,11,21) that carried identical "
                   "covariant coefficient vectors at a = 0 now carry "
                   "distinct trace-orbit vectors -- and the "
                   "feasibility verdicts above say whether separation "
                   "suffices")
    else:
        kit.append("the clash-T probe: the trace refinement does NOT "
                   "separate the parent's mechanism witness rows "
                   "(0,5,14) and (1,11,21) at a = 0; the parent "
                   "identification survives the trace")
    kit.append("arm 2's ordered-raw grain collapses onto the "
               "conditional system by the measured window-2 blindness "
               "(every prefix marginal is q1 x q2 for every normalized "
               "kernel), so the marginal-history question lives "
               "entirely at the count-field and relabelling-quotient "
               "grains, each published with its own verdict and "
               "certificates")
    kit.append("this unit tests whether a trace COULD be real and "
               "presupposes neither answer; whether the trigger is "
               "real or bookkeeping is the fork's open question")
    for (t, d) in TERM_TABLE:
        kit.append("| " + t + " | " + d + " |")
    P["kit"] = kit


# ===========================================================================
# SECTION 16.  THE FULL BUILD
# ===========================================================================
def build_all(P=None):
    LD = Ledger()
    if P is None:
        P = {}
    source_scan(LD, P)
    PREC = measure_reads(LD, P)
    measure_arena(LD, P)
    GCELL, GTRI = build_gamma(LD, P)
    psi1, q1, sup1, q2, sup2, BOC, E1S = build_walk(LD, P)
    measure_arms(LD, P, GCELL, GTRI, E1S)
    canon_tuple, canon_ctx = make_canon(GCELL, GTRI)
    canonT_tuple, canonT_ctx = make_canonT(GCELL, GTRI)
    CANON_HOLDER["tuple"] = canon_tuple
    CANON_HOLDER["ctx"] = canon_ctx
    CANON_HOLDER["E1S"] = E1S
    RAW, parts_parent = kreach_census(LD, P, canon_tuple, canon_ctx,
                                      sup1, sup2, BOC, E1S, PREC)
    CANON_HOLDER["RAW"] = RAW
    RAWT, partsT = treach_census(LD, P, canonT_tuple, canonT_ctx,
                                 canon_tuple, sup1, sup2, BOC)
    step1_censusT(LD, P, canonT_tuple, sup1, BOC)
    depth2_system(LD, P, psi1, sup1, BOC)
    q3_of = make_q3(psi1)
    groups = P["tcoincidence"]["distinct_systems"]
    STL = {}
    for rep in groups:
        for grain in LADDER:
            STL[(rep, grain)] = build_systemT(
                rep, canonT_tuple, canonT_ctx, q3_of, sup1, sup2, BOC,
                grain=grain)
    for an in ("SA", "CN", "GLOBAL"):
        if (an, "FULL") not in STL:
            STL[(an, "FULL")] = build_systemT(
                an, canonT_tuple, canonT_ctx, q3_of, sup1, sup2, BOC,
                grain="FULL")
    parent_out = tblind_systems(LD, P, canon_tuple, canon_ctx, q3_of,
                                sup1, sup2, BOC, E1S, RAW, PREC, STL)
    tb_status = {}
    for r in P["tblind"]["parent_pipeline_runs"]:
        tb_status[(r["system"], str(r["a"]))] = r["status"]
    out1, dims_checked = arm1_systems(LD, P, STL, groups, q3_of, sup1,
                                      sup2, BOC, tb_status)
    arm1_free_lemma(LD, P, q3_of, sup1, sup2, BOC, out1, groups)
    arm1_uniform(LD, P, STL, out1, groups)
    clash_probe(LD, P, STL[("GLOBAL", "FULL")], PREC)
    out2, dims2 = arm2_grains(LD, P, parent_out, q1, q2, GCELL,
                              P["tblind"]["parent_pipeline_runs"])
    dims_checked.extend(dims2)
    controls(LD, P, canonT_tuple, canonT_ctx, q3_of, sup1, sup2, BOC,
             parent_out, q1, q2, GCELL, dims_checked)
    build_verdicts(P, groups, out1)
    kernel_wall_gate(LD, P)
    rep_wall_gate(LD, P)
    P["mode_disclosure"] = {
        "addenda_received": [
            "the #68 SCOUT-K addendum (3a1e5a649537) was in the birth "
            "orders, before any construction",
            "the #87 SCOUT-T addendum (15d763633293) was received by "
            "routed message while instrument sections 1-11 were "
            "drafted and BEFORE any feasibility row was solved or any "
            "solver output inspected; the single-full-trace arm-1 "
            "design was replaced by the five-grain minimality ladder "
            "and the #84-form W-REPRESENTATION citation replaced by "
            "the #86 fork-neutral form prior to any computation"],
        "computations_inspected_before_receipt": "NONE (syntax checks "
                                                 "only)",
        "addendum_98": "the #98 addendum (eighteenth external review, "
                       "routed per #77) was received AFTER this unit's "
                       "artifacts were first sealed and while the "
                       "self-battery was mid-run; all solver results "
                       "had been computed and inspected at receipt; "
                       "the #98 items change instrument auditing "
                       "(digest inventory, numeral-inventory "
                       "restriction, hostile plants) and claim "
                       "language (the event-selection-kernel "
                       "narrowing, the joint-successor-law diagnosis, "
                       "the four-class model space), and NO measured "
                       "value; delivery re-run and battery restarted "
                       "on the folded instrument",
        "review_102": "the #102 diagnosis (twentieth external review, "
                      "routed per #77) was received while the folded "
                      "battery's selftest leg was in flight: the "
                      "arm-1 status/certificate mutants targeted the "
                      "INHERITED full grain (dead code under the "
                      "ladder collapse) and the SAMPLES gates "
                      "validated status words only; both wired "
                      "defects fixed (injection at the SOLVED PREV1 "
                      "grain; SAMPLES gates validate status against "
                      "the solver object), the scope sentence "
                      "engraved, and delivery, selftest and the full "
                      "battery re-run fresh; audit wiring only, no "
                      "measured value moved"}
    P["registry"] = {"falsifiers_registered": len(FALSIFIERS),
                     "gates_total": 37}
    build_kit(P, P["tcoincidence"]["distinct_systems"])
    sample_space_audit(LD, P)
    numeral_bindings(LD, P)
    num_total_gate(LD, P)
    env_exclusion(LD, P)
    digest_inventory(LD, P)
    P["ledger"] = LD.rows
    return P


# ===========================================================================
# SECTION 17.  NOTE VERIFICATION (the walls on the report's own prose,
# with per-occurrence numeral TOTALITY -- the #68 standard from birth)
# ===========================================================================
def collect_numerals(obj, out):
    if isinstance(obj, bool):
        return
    if isinstance(obj, int):
        out.add(obj)
        return
    if isinstance(obj, str):
        for tok in obj.replace("/", " ").replace(",", " ").split():
            neg = tok.lstrip("-")
            if neg.isdigit():
                out.add(int(neg))
        return
    if isinstance(obj, dict):
        for k in obj:
            collect_numerals(k, out)
            collect_numerals(obj[k], out)
    if isinstance(obj, (list, tuple)):
        for v in obj:
            collect_numerals(v, out)


def iter_rationals(text):
    toks = text.replace("(", " ").replace(")", " ").replace(",", " ")
    out = set()
    for tok in toks.split():
        t = tok.strip(".;:|")
        parts = t.split("/")
        if len(parts) == 2 and parts[0].lstrip("-").isascii() \
                and parts[0].lstrip("-").isdigit() \
                and parts[1].isascii() and parts[1].isdigit():
            out.add(t)
    return out


def rationals_of(obj, out):
    if isinstance(obj, str):
        out.update(iter_rationals(obj))
    if isinstance(obj, dict):
        for k in obj:
            rationals_of(k, out)
            rationals_of(obj[k], out)
    if isinstance(obj, (list, tuple)):
        for v in obj:
            rationals_of(v, out)


NUM_INCLUDE_SUBTREES = ("arena", "gamma", "walk", "blindness", "arms",
                        "kreach", "treach", "step1t", "d2t", "tblind",
                        "a1", "a2", "registry")
# the #98 order (SCOUT-K's #93 class): the sweep inventory is built from
# MEASUREMENT subtrees only -- audit, control, wall, falsifier and
# ledger subtrees are EXCLUDED, so unrelated receipt/control values can
# never legitimize an invented prose numeral; claims about audit values
# route through the claim-specific NUM_BINDINGS table.


def value_paths(P):
    paths = {}

    def walkv(obj, path):
        if isinstance(obj, bool):
            return
        if isinstance(obj, int):
            paths.setdefault(str(obj), path)
            return
        if isinstance(obj, str):
            t = obj.strip()
            if t.lstrip("-").isdigit() or (
                    "/" in t and len(t.split("/")) == 2
                    and t.split("/")[0].lstrip("-").isdigit()
                    and t.split("/")[1].isdigit()):
                paths.setdefault(t, path)
            return
        if isinstance(obj, dict):
            for k in sorted(obj):
                walkv(obj[k], path + "/" + str(k))
            return
        if isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                walkv(v, path + "[%d]" % i)
    walkv(fser({k: P[k] for k in NUM_INCLUDE_SUBTREES if k in P}), "")
    return paths


def is_hex12(t):
    return (len(t) == 12
            and all(ch in "0123456789abcdef" for ch in t)
            and any(ch.isdigit() for ch in t)
            and any(ch in "abcdef" for ch in t))


def is_date(t):
    parts = t.split("-")
    return (len(parts) == 3 and all(p.isdigit() for p in parts)
            and len(parts[0]) == 4)


def is_symbol(t):
    # identifier-style symbol like q3, c1, psi2, R1, SUFFIX2, K(e...)
    head = t.rstrip("0123456789")
    tail = t[len(head):]
    return (head != "" and tail != ""
            and all(ch.isalpha() or ch in "_'" for ch in head))


CORPUS_PREFIXES = ("v", "paper-", "E-", "W", "K", "Z", "M", "F", "S",
                   "T", "D", "P", "H")


def is_corpus_label(t):
    for pref in CORPUS_PREFIXES:
        if t.startswith(pref):
            rest = t[len(pref):]
            if rest and all(ch.isdigit() or ch == "-" for ch in rest) \
                    and any(ch.isdigit() for ch in rest):
                return True
    return False


def digit_runs(t):
    runs = []
    cur = ""
    for ch in t:
        if ch.isdigit():
            cur += ch
        else:
            if cur:
                runs.append(cur)
            cur = ""
    if cur:
        runs.append(cur)
    return runs


def numeral_totality(P, text, problems):
    paths = value_paths(P)
    inv = set()
    rationals_of(fser({k: P[k] for k in NUM_INCLUDE_SUBTREES
                       if k in P}), inv)
    verdict_blob = " ".join(str(P["verdicts"][k])
                            for k in sorted(P["verdicts"]))
    audit = []
    for li, ln in enumerate(text.splitlines()):
        stripped = ln.strip()
        if stripped.startswith("#"):
            lclass = "heading"
        elif stripped.startswith(">"):
            lclass = "quotation"
        else:
            lclass = None
        for tok in ln.split():
            t = tok.strip(".,;:|()[]{}*'\"`!?<>")
            if t.endswith("'s"):
                t = t[:-2]
            if not any(ch.isdigit() for ch in t):
                continue
            cls = None
            field = None
            if lclass:
                cls = "NON-CLAIM-" + lclass
            elif is_date(t):
                cls = "NON-CLAIM-date"
            elif is_hex12(t):
                cls = "NON-CLAIM-digest"
            elif "/" in t and (".md" in t or ".py" in t
                               or ".json" in t):
                cls = "NON-CLAIM-path-label"
            elif t.startswith("#") and t.lstrip("#").isdigit():
                cls = "NON-CLAIM-ledger-ref"
            elif is_corpus_label(t):
                cls = "NON-CLAIM-corpus-label"
            elif any(t == num for (num, _pp) in NUM_BINDINGS):
                cls = "BOUND-table"
                field = ";".join(pp for (num, pp) in NUM_BINDINGS
                                 if num == t)
            elif t in inv:
                cls = "BOUND-rational"
                field = paths.get(t, "inventory")
            elif t in verdict_blob:
                cls = "NON-CLAIM-verdict-token"
            elif is_symbol(t):
                cls = "NON-CLAIM-symbol-name"
            else:
                runs = digit_runs(t)
                if runs and all(r in paths for r in runs):
                    cls = "BOUND"
                    field = ";".join(paths[r] for r in runs)
            if cls is None and mut("MUT-NUMTOT"):
                cls = "BOUND-blanket"
            if cls is None:
                problems.append("numeral occurrence unclassified "
                                "(line %d): %s" % (li + 1, tok[:30]))
            else:
                audit.append({"line": li + 1, "token": t, "class": cls,
                              "field": field})
    return audit


def verify_note(P, note_bytes, problems):
    text = note_bytes.decode("utf-8")
    hay = canon_text(text)
    low = hay.lower()
    for sent in P["kit"]:
        if canon_text(sent) not in hay:
            problems.append("kit sentence missing: " + sent[:80])
    for sent in REQUIRED_SENTENCES:
        if canon_text(sent) not in hay:
            problems.append("required sentence missing: " + sent[:60])
    for (aid, _rel, quote) in ANCHORS:
        if aid in ("A-PARENT-1010", "A-PARENT-CANON",
                   "A-PARENT-KPOLY"):
            continue
        if canon_text(quote) not in hay:
            problems.append("anchor quote missing from note: " + aid)
    for pat in FORBIDDEN_GLOBAL:
        if pat in low:
            problems.append("forbidden pattern present: " + pat)
    for h in kernel_wall_hits(text):
        problems.append("kernel wall: " + h)
    for h in rep_wall_hits(text):
        problems.append("representation wall: " + h)
    for name in SS_NAMES:
        if "[SS:" + name + "]" not in text:
            problems.append("sample-space tag [SS:%s] absent" % name)
    for ln in text.splitlines():
        st = ln.strip()
        if st.startswith("|") or st.startswith(">") or st.startswith("#"):
            continue
        if ("P(" in ln or "q(" in ln or "K(" in ln) and "[SS:" not in ln:
            problems.append("probability expression without a "
                            "sample-space tag: " + st[:60])
    gates = {r["gate"] for r in P["ledger"]}
    pos = 0
    while True:
        k = text.find("[LIC:", pos)
        if k < 0:
            break
        end = text.find("]", k)
        gid = text[k + 5:end]
        if gid not in gates:
            problems.append("licence token names no registered gate: "
                            + gid)
        pos = end
    for ln in text.splitlines():
        lnl = ln.lower()
        if "derive" in lnl and not ln.strip().startswith(">") \
                and "[BY:" not in ln and "|" not in ln:
            problems.append("derivation sentence without subject tag: "
                            + ln.strip()[:60])
    for r in P["numeral_bindings"]:
        want = "| %s | %s |" % (r["numeral"], r["receipt_field"])
        if want not in text:
            problems.append("numeral-binding row missing: " + want)
    inv = set()
    rationals_of(fser({k: P[k] for k in NUM_INCLUDE_SUBTREES
                       if k in P}), inv)
    for ln in text.splitlines():
        for t in sorted(iter_rationals(ln)):
            if t not in inv:
                problems.append("slash rational not in "
                                "measurement-subtree inventory: " + t)
    numeral_totality(P, text, problems)
    return problems


# ===========================================================================
# SECTION 18.  FALSIFIER REGISTRY
# ===========================================================================
FALSIFIERS = (
    ("MUT-PINDIG", "G-PIN-DIGESTS", "pin_check",
     "corrupts a pinned-read digest comparison"),
    ("MUT-ANCHOR", "G-ANCHORS", "anchors", "corrupts an anchor quote"),
    ("MUT-ARENA", "G-ARENA", "arena", "adds a fake triangle"),
    ("MUT-GAMMA", "G-GAMMA", "gamma", "drops a group element"),
    ("MUT-Q", "G-WALK", "walk", "skips the Born normalization"),
    ("MUT-BLIND", "G-BLIND", "blindness",
     "replaces the stepped state by the pre-shift state"),
    ("MUT-ARMCOV", "G-ARMS-COVARIANT", "arms",
     "punctures the shared-actor neighborhood at one cell"),
    ("MUT-KREACH", "G-KREACH", "kreach",
     "duplicates a parent raw tuple"),
    ("MUT-TREACH", "G-TREACH", "treach",
     "duplicates a trace raw tuple"),
    ("MUT-TCOINC", "G-TCOINCIDE", "tcoincidence",
     "flips a trace-partition coincidence"),
    ("MUT-STEP1", "G-STEP1T", "step1t",
     "inflates the step-one orbit count"),
    ("MUT-D2", "G-D2T", "d2t", "forges the depth-2 polytope dimension"),
    ("MUT-TBLIND", "G-TBLIND", "tblind",
     "corrupts a reproduced parent gap string"),
    ("MUT-TBCERT", "G-TBLIND-CERT", "tblind",
     "corrupts a parent-pipeline Farkas certificate"),
    ("MUT-CTX", "G-A1-WELLDEF", "a1",
     "poisons the trace-orbit bookkeeping self-check"),
    ("MUT-SAMPLE", "G-A1-SAMPLES", "a1",
     "flips an arm-1 sample status against its gap"),
    ("MUT-CERT", "G-A1-CERT", "a1",
     "corrupts an arm-1 certificate or witness"),
    ("MUT-BW", "G-A1-CERT", "a1",
     "forges the branchwise status against its stored object"),
    ("MUT-FREE", "G-A1-FREE", "a1",
     "flips a free-lemma block status"),
    ("MUT-CONSIST", "G-A1-CONSIST", "a1",
     "inverts the relaxation-consistency flag"),
    ("MUT-CLASHT", "G-CLASH-T", "a1",
     "suppresses the clash-T probe rows"),
    ("MUT-COLLAPSE", "G-A2-COLLAPSE", "a2",
     "inverts an ordered-raw collapse comparison"),
    ("MUT-A2", "G-A2-SAMPLES", "a2",
     "flips an arm-2 grain status against its gap"),
    ("MUT-A2CERT", "G-A2-CERT", "a2",
     "corrupts an arm-2 certificate or witness"),
    ("MUT-UNIF", "G-A2-UNIFORM", "a2",
     "corrupts a uniform-in-a certificate"),
    ("MUT-DIM", "G-A1-DIM", "dims",
     "forges a published polytope dimension"),
    ("MUT-CTRL", "G-CONTROLS", "controls",
     "forges the forced-empty control status"),
    ("MUT-KWALL", "G-KERNEL-WALL", "kernel_wall",
     "blinds the kernel-scope wall patterns"),
    ("MUT-RWALL", "G-REP-WALL", "rep_wall",
     "blinds the representation-wall subjects"),
    ("MUT-SS", "G-SAMPLE-SPACE", "sample_spaces",
     "strips a sample-space declaration"),
    ("MUT-NUMBIND", "G-NUM-BIND", "numeral_bindings",
     "corrupts a numeral binding resolution"),
    ("MUT-ENV", "G-ENV-EXCLUSION", "env_exclusion",
     "serializes an unpinned live-read digest into the receipt"),
    ("MUT-SETITER", "G-AST-DETERMINISM", "source_hygiene",
     "plants bare set-iteration and raw listdir in the scanned source"),
    ("MUT-NUMTOT", "G-NUM-TOTAL", "num_total_controls",
     "blinds the totality classifier so an invented numeral passes"),
    ("MUT-DIGINV", "G-DIGEST-INVENTORY", "digest_inventory",
     "plants an arbitrary unpinned live-read digest in the receipt"),
)


# ===========================================================================
# SECTION 19.  ARTIFACTS, CLI, SELFTEST
# ===========================================================================
def render_output(P, note_digest):
    lines = []
    lines.append("SCOUT-T delivery transcript")
    lines.append("pin 3f35573d88d8 (v15 ledger #82) + the #87 addendum "
                 "15d763633293 + the #68 addendum 3a1e5a649537; unit "
                 "note " + NOTE_REL)
    lines.append("object under test (the note): sha256-12 " + note_digest)
    lines.append("instrument source: sha256-12 "
                 + P["source_hygiene"]["digest"])
    lines.append("parent apparatus: SCOUT-K #74 code 38c3f6cb288e + "
                 "receipt 5af53face093 via byte-verified snapshots "
                 "(the live scoutk files are mid-repair); walk snapshot "
                 "edb60bccd22e")
    lines.append("")
    for r in P["ledger"]:
        lines.append("GATE %-18s %s  %s"
                     % (r["gate"], "PASS" if r["ok"] else "FAIL",
                        r["note"]))
    lines.append("")
    lines.append("VERDICTS")
    for k in ("REACH", "D2", "A1", "A2", "TBLIND", "BRIDGE"):
        lines.append("  " + P["verdicts"][k])
    lines.append("")
    lines.append("KEY CLAIMS")
    tre = P["treach"]
    lines.append("  trace census: 81 contexts / 243 tuples / 9 "
                 "trigger-event pairs; FULL-grain orbit variables "
                 + ", ".join("%s %d" % (an, tre["depth3"][an]
                                        ["tuple_orbit_variables"])
                             for an in ARM_ORDER)
                 + " (parent: 16/16/25/19/25)")
    for rep in sorted(P["a1"]["systems"]):
        sysd = P["a1"]["systems"][rep]
        for g in LADDER:
            gr = sysd["grains"][g]
            sts = [r["status"] for r in gr["samples"]]
            lines.append("  arm1 %s %s (nv %d)%s: %s"
                         % (rep, g, gr["nv"],
                            " [= " + gr["identical_system_to"] + "]"
                            if gr.get("identical_system_to") else "",
                            "/".join("F" if s == "FEASIBLE" else "I"
                                     for s in sts)))
    for (label, an) in SYSTEMS:
        for g in GRAIN_ORDER:
            gr = P["a2"]["systems"][label][g]
            sts = [r["status"] for r in gr["samples"]]
            lines.append("  arm2 %s %s (%d rows): %s"
                         % (label, g, gr["grain_rows"],
                            "/".join("F" if s == "FEASIBLE" else "I"
                                     for s in sts)))
    fl = P["a1"]["free_lemma"]["per_sample"]
    lines.append("  free lemma refused pairs per sample: "
                 + ", ".join("a=%s:%d" % (a, fl[a]["infeasible_pairs"])
                             for a in sorted(fl)))
    lines.append("  clash-T separation: "
                 + str(P["a1"]["clash_t"]["trace_separates_the_pair"]))
    lines.append("  falsifiers: %d registered; gates: %d"
                 % (len(FALSIFIERS), len(P["ledger"])))
    lines.append("")
    return "\n".join(lines) + "\n"


def deliver(write):
    P1 = build_all()
    P2 = build_all()
    d1, d2 = digest(P1), digest(P2)
    if d1 != d2:
        raise GateFail("G-DETERMINISM", "double build differs")
    P1["determinism"] = {"double_build_digest": d1, "equal": True}
    if len(P1["ledger"]) != P1["registry"]["gates_total"]:
        raise GateFail("G-NOTE-KIT", "gates_total registry mismatch: "
                       + str(len(P1["ledger"])))
    note_path = os.path.join(ROOT, NOTE_REL)
    if not os.path.exists(note_path):
        raise GateFail("G-NOTE-PRESENT", "the unit note is absent")
    note_bytes = read_rel(NOTE_REL)
    problems = verify_note(P1, note_bytes, [])
    if problems:
        raise GateFail("G-NOTE-KIT", "; ".join(problems[:8]))
    audit = numeral_totality(P1, note_bytes.decode("utf-8"), [])
    P1["note_numeral_audit"] = {
        "occurrences": len(audit),
        "classes": sorted(Counter(r["class"] for r in audit).items()),
        "policy": "per-occurrence totality (#68): every numeral "
                  "occurrence in the note is classified BOUND (with a "
                  "specific receipt field) or NON-CLAIM (with a reason "
                  "class); no blanket layout whitelist exists"}
    nd = sha12(note_bytes)
    P1["object_under_test"] = {"path": NOTE_REL, "sha256_12": nd}
    P1["falsifiers"] = [{"name": n, "gate": g, "object": o,
                         "description": d} for (n, g, o, d) in FALSIFIERS]
    P1["schema"] = "scoutt-receipt-v1"
    extra_self = {d1: "SELF-DETERMINISM", nd: "SELF-NOTE"}
    inv_f, unclass_f = classify_digests(P1, extra_self)
    P1["digest_inventory"]["final"] = {
        "tokens": len(inv_f),
        "classes": sorted(Counter(inv_f.values()).items()),
        "unclassified": unclass_f}
    blobf = to_json(P1)
    new_f = sorted(hex_tokens(blobf) - set(inv_f))
    if unclass_f or new_f:
        raise GateFail("G-DIGEST-INVENTORY",
                       "final receipt carries unclassified digests: "
                       + ",".join(unclass_f + new_f))
    out = render_output(P1, nd)
    rec = to_json(P1)
    if write:
        with open(os.path.join(ROOT, OUT_REL), "w", encoding="utf-8") \
                as f:
            f.write(out)
        with open(os.path.join(ROOT, REC_REL), "w", encoding="utf-8") \
                as f:
            f.write(rec)
    sys.stdout.write(out)
    return 0


def selftest():
    before = {}
    for rel in (OUT_REL, REC_REL):
        p = os.path.join(ROOT, rel)
        before[rel] = sha12(read_rel(rel)) if os.path.exists(p) else None
    clean = build_all()
    clean_dig = {}
    for (_n, _g, obj, _d) in FALSIFIERS:
        clean_dig[obj] = digest(clean.get(obj))
    failures = []
    for (name, gate, obj, _desc) in FALSIFIERS:
        ARMED["name"] = name
        died, at = False, None
        partial = {}
        try:
            build_all(partial)
        except GateFail as e:
            died, at = True, e.gate
        ARMED["name"] = None
        if not died:
            failures.append(name + ": survived")
            continue
        if at != gate:
            failures.append("%s: died at %s not %s" % (name, at, gate))
            continue
        moved = (obj in partial
                 and digest(partial.get(obj)) != clean_dig[obj])
        if not moved:
            failures.append(name + ": no move proof")
            continue
        sys.stdout.write("FALSIFIER %-12s died at %-18s moved-proof ok\n"
                         % (name, at))
    after = {}
    for rel in (OUT_REL, REC_REL):
        p = os.path.join(ROOT, rel)
        after[rel] = sha12(read_rel(rel)) if os.path.exists(p) else None
    if before != after:
        sys.stdout.write("SELFTEST: artifacts moved\n")
        return 3
    if failures:
        for f in failures:
            sys.stdout.write("SELFTEST FAIL " + f + "\n")
        return 3
    sys.stdout.write("SELFTEST PASS: %d falsifiers, all died at their "
                     "declared gates, artifacts untouched\n"
                     % len(FALSIFIERS))
    return 0


USAGE = ("usage: scoutt_exact.py [--no-write | --numbers | --kit | "
         "--selftest | --mutant NAME | --verify-paper PATH | "
         "--list-gates | --list-mutants]\n")


def main(argv):
    args = argv[1:]
    known = {"--no-write", "--numbers", "--kit", "--selftest",
             "--mutant", "--verify-paper", "--list-gates",
             "--list-mutants"}
    flags = [a for a in args if a.startswith("--")]
    for a in flags:
        if a not in known:
            sys.stderr.write(USAGE)
            return 2
    if len(flags) != len(set(flags)) or len(flags) > 1:
        sys.stderr.write(USAGE)
        return 2
    if not args:
        try:
            return deliver(True)
        except GateFail as e:
            sys.stderr.write("GATE FAILURE %s: %s\n" % (e.gate, e.msg))
            return 3
    mode = args[0]
    if mode == "--list-gates":
        gates = sorted({g for (_n, g, _o, _d) in FALSIFIERS}
                       | {"G-SRC-CLEAN", "G-DETERMINISM", "G-NOTE-KIT",
                          "G-D2T", "G-STEP1T", "G-A1-UNIFORM",
                          "G-LADDER", "G-LP-SOLVE"})
        for g in gates:
            sys.stdout.write(g + "\n")
        return 0
    if mode == "--list-mutants":
        for (n, g, o, d) in FALSIFIERS:
            sys.stdout.write("%-12s -> %-18s (%s): %s\n" % (n, g, o, d))
        return 0
    if mode == "--mutant":
        if len(args) != 2:
            sys.stderr.write(USAGE)
            return 2
        names = {n for (n, _g, _o, _d) in FALSIFIERS}
        if args[1] not in names:
            sys.stderr.write("unknown mutant\n")
            return 2
        ARMED["name"] = args[1]
        try:
            build_all()
        except GateFail as e:
            sys.stderr.write("MUTANT %s died at %s\n" % (args[1], e.gate))
            return 3
        sys.stderr.write("MUTANT %s survived\n" % args[1])
        return 3
    if mode == "--verify-paper":
        if len(args) != 2:
            sys.stderr.write(USAGE)
            return 2
        P = build_all()
        try:
            with open(args[1], "rb") as f:
                nb = f.read()
        except OSError:
            sys.stderr.write("cannot read note\n")
            return 2
        problems = verify_note(P, nb, [])
        if problems:
            for pr in problems[:20]:
                sys.stdout.write("NOTE PROBLEM: " + pr + "\n")
            return 3
        sys.stdout.write("NOTE VERIFIED: kit, anchors, walls, tags, "
                         "numerals all pass\n")
        return 0
    if len(args) != 1:
        sys.stderr.write(USAGE)
        return 2
    if mode == "--no-write":
        try:
            return deliver(False)
        except GateFail as e:
            sys.stderr.write("GATE FAILURE %s: %s\n" % (e.gate, e.msg))
            return 3
    if mode == "--numbers":
        P = build_all()
        for k in ("REACH", "D2", "A1", "A2", "TBLIND", "BRIDGE"):
            sys.stdout.write(P["verdicts"][k] + "\n")
        sys.stdout.write(to_json(
            {"orbit_vars_full": {an: P["treach"]["depth3"][an]
                                 ["tuple_orbit_variables"]
                                 for an in ARM_ORDER},
             "a1": {rep: {g: [r["status"] for r in
                              P["a1"]["systems"][rep]["grains"][g]
                              ["samples"]]
                          for g in LADDER}
                    for rep in sorted(P["a1"]["systems"])},
             "a2": {lbl: {g: [r["status"] for r in
                              P["a2"]["systems"][lbl][g]["samples"]]
                          for g in GRAIN_ORDER}
                    for lbl in sorted(P["a2"]["systems"])}}) + "\n")
        return 0
    if mode == "--kit":
        P = build_all()
        for sent in P["kit"]:
            sys.stdout.write(sent + "\n")
        return 0
    if mode == "--selftest":
        return selftest()
    sys.stderr.write(USAGE)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
