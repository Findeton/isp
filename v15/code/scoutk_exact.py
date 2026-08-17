#!/usr/bin/env python3
# ===========================================================================
# SCOUT-K  --  the record-dependent, locally covariant kernel census.
#
# Unit: v15/note-scoutk.md (report NOTE, scout class).
# Pin:  v15/note-scoutk-pin.md (FROZEN a1a6ccc61bd4), v15 ledger #60,
#       with the #64 binding addendum folded (trigger = candidate bridge;
#       the first-event boundary; the event-selection-only scope sentence).
#
# THE QUESTION (pin): does any LOCAL, RECORD-DEPENDENT kernel K(e|c,G,R),
# equivariant in the true sense K(ge|gc,gG,gR)=K(e|c,G,R) under
# SIMULTANEOUS relabelling of all four slots, preserve the delivered walk
# statistics at exact multi-step consistency -- or is the emptiness of
# #58's record-blind fixed-alpha family in fact general?
#
# PARENT APPARATUS: v15/code/scout_exact.py at its DELIVERED digest
# edb60bccd22e (ledger #58).  The live file is held by the scout repair
# worker mid-flight, so this unit binds to the delivered bytes through the
# byte-verified snapshot v15/code/scoutk_parent_delivered.py (the scout's
# own ECC-snapshot precedent).  Every reused constructor below carries an
# ANCHORED-REUSE comment naming its parent section; the reuse is bound by
# G-PIN-DIGESTS (snapshot digest) + G-ANCHORS (verbatim parent lines) +
# G-SUBFAM (the fixed-alpha subfamily re-derived inside THIS instrument's
# orbit family reproduces #58's refusal exactly).
#
# Exact arithmetic throughout: Python integers and fractions.Fraction.
# No floats, no builtin hash, no timestamps, no absolute paths in
# artifacts.  The delivery run is the only writer; every failure writes
# nothing.
#
# CLI: delivery (no args) | --no-write | --numbers | --kit | --selftest |
#      --mutant NAME | --verify-paper PATH | --list-gates | --list-mutants
# Exit codes: 0 pass, 2 usage, 3 gate failure / verification failure.
#
# MICRO-REPAIR (v15 ledger #81 orders M1-M5 + the #82 routed M6): the #68
# pin addendum is digest-pinned and CONSUMED by G-ADDENDUM-68; the D3
# verdict names its consistency mode; the G-fixed scope wall is a gated
# kit sentence; the #78 G-KERNEL-WALL is ported (subject-based, with the
# hyphen-fused replants as permanent dead plants); G-ENV-EXCLUSION and
# G-AST-DETERMINISM close the I8/I9 species in-run; the numeral sweep is
# per-occurrence total (BOUND / NON-CLAIM), the blanket whitelist
# retired; the no-caps sentence is receipt-backed by G-CAPS-REGISTER;
# the verifier's three strengthenings are re-derived by THIS instrument
# (108x8 arm covariance, the partition refinement order, the
# canonical-first clash).  No measured value moved.
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
NOTE_REL = "v15/note-scoutk.md"
OUT_REL = "v15/code/scoutk_output.txt"
REC_REL = "v15/code/scoutk_receipt.json"

# The parent scout is read ONLY through the disclosed byte-verified
# snapshot (the live file is mid-repair); LOG.md is anchor-only and never
# digest-recorded (append-only file; recording its digest would plant an
# environment/time-dependent value in the receipt -- the named hazard).
PINNED = {
    "v15/note-scoutk-pin.md": "a1a6ccc61bd4",
    "v15/note-scoutk-pin-addendum.md": "3a1e5a649537",
    "v15/code/scoutk_parent_delivered.py": "edb60bccd22e",
    "v14/paper-20-coupling.md": "4824d190af73",
    "v15/verify/scoutk-verifier-rebuild.py": "1188fe424d00",
    "v15/verify/scoutk-verifier-rebuild-output.txt": "084dd5e01336",
}

# The #68 pin addendum (v15 ledger #68, the eleventh external review's
# freezes), cited by digest and CONSUMED by gate G-ADDENDUM-68 below.
ADDENDUM_REL = "v15/note-scoutk-pin-addendum.md"
ADDENDUM_DIG = "3a1e5a649537"
# The hostile verifier's independent rebuild, archived at #82: the
# verification record this unit's addendum gate anchors by pinned digest.
VERIFY_REBUILD_REL = "v15/verify/scoutk-verifier-rebuild.py"
VERIFY_LEDGER_REL = "v15/verify/scoutk-verifier-rebuild-output.txt"

F = Fraction
ARMED = {"name": None}

# The caps register (M5, verifier finding F6): every constraint row this
# instrument constructs is typed at its construction site; the register
# proves the note's no-caps sentence at G-CAPS-REGISTER.
CAPS = {"counter": None}


def caps_note(kind, n=1):
    if CAPS["counter"] is not None:
        CAPS["counter"][kind] += n


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
# ANCHORED-REUSE: scout_exact.py (delivered edb60bccd22e) SECTION 1 -- the
# chart constructors, the ring Z[w], the committed walk.  Re-typed here,
# bound by G-ANCHORS + the G-SUBFAM reproduction.
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
# ANCHORED-REUSE: scout_exact.py SECTION 2 -- rref/nullspace and the
# two-phase simplex with phase-one dual extraction (Farkas on infeasible).
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


# ===========================================================================
# SECTION 3.  THE ANCHOR REGISTRY
# ===========================================================================
ANCHORS = (
    ("A-PIN-QUESTION", "v15/note-scoutk-pin.md",
     "Does any LOCAL, RECORD-DEPENDENT kernel K(e|c,G,R), equivariant in "
     "the true sense K(ge|gc,gG,gR)=K(e|c,G,R) under SIMULTANEOUS "
     "relabelling of all four slots, preserve the delivered walk statistics "
     "at exact multi-step consistency"),
    ("A-PIN-ORBITS", "v15/note-scoutk-pin.md",
     "Form the ORBITS of (G,R,c,e) under simultaneous relabelling; ONE "
     "FREE VARIABLE PER ORBIT."),
    ("A-LOG59-HONEST", "v15/LOG.md",
     "no record-blind, fixed-alpha, affine-equivariant kernel preserves "
     "the delivered three-step walk statistics."),
    ("A-LOG59-TRUE-EQ", "v15/LOG.md",
     "true equivariance K(ge|gc,gG,gR)=K(e|c,G,R) admits record-dependent "
     "kernels that distinguish candidate triples by their RELATION to the "
     "written record without privileging labels."),
    ("A-PARENT-KPOLY", "v15/code/scoutk_parent_delivered.py",
     "K_alpha: alpha on the line block, (1-alpha)/2 on each non-line"),
    ("A-PARENT-3STEP", "v15/code/scoutk_parent_delivered.py",
     "w = pmul(kpoly(e1), kpoly(e2))"),
    ("A-PARENT-GATE-729", "v15/code/scoutk_parent_delivered.py",
     "nrows == 729 and len(polys) == 25"),
    ("A-PARENT-GATE-288", "v15/code/scoutk_parent_delivered.py",
     "and len(combos_ok) == 8 and all_nonline and total_kernels == 288,"),
    ("A-P20-277", "v14/paper-20-coupling.md",
     "A division event on cell (x, l) increments n_l(x) by one."),
    ("A-P20-217", "v14/paper-20-coupling.md",
     "The menu at site x is the three link traversals and the weight "
     "q(l|x) is the post-coin Born weight |(Cψ)(x,l)|²."),
    ("A-P20-633", "v14/paper-20-coupling.md",
     "The record accumulates the law's own weights and the state is not "
     "collapsed onto the emitted cell, so the walk stays coherent between "
     "division events."),
    ("A-P19-289", "v14/paper-19-r3-weld.md",
     "at this generator a division event's footprint **is** its conflict "
     "group, so the geometry is a function of the groupings by "
     "construction"),
)


def measure_reads(LD, P):
    reads = {}
    for rel in sorted(PINNED):
        reads[rel] = sha12(read_rel(rel))
    P["read_set"] = reads
    bad = sorted(rel for rel, d in PINNED.items()
                 if pick("MUT-PINDIG", reads[rel], reads[rel] + "x") != d)
    P["pin_check"] = {"pinned": dict(PINNED), "bad": bad,
                      "parent_resolution": "SNAPSHOT-ONLY",
                      "log_resolution": "ANCHOR-ONLY-UNPINNED",
                      "ecc_reads": "NONE (this unit consumes no ECC LP "
                                   "values; the pin's ECC snapshots are "
                                   "therefore unread)"}
    LD.gate("G-PIN-DIGESTS", not bad,
            "the frozen pin, the #68 pin addendum, the delivered-parent "
            "snapshot, paper-20 and the archived verifier rebuild (with "
            "its check ledger) are read at their pinned digests; the "
            "parent is read ONLY through the byte-verified snapshot "
            "(the live scout file was mid-repair); LOG.md is "
            "anchor-only and its digest is never recorded (the receipt "
            "hazard, now machine-checked by G-ENV-EXCLUSION)",
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
            "(whitespace-collapsed) in its file, the parent-reuse anchors "
            "in the delivered snapshot included",
            {"count": len(anch),
             "missing": [a["id"] for a in anch if not a["found"]]})


# ===========================================================================
# SECTION 4.  ARENA + GAMMA + WALK GATES
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
    # ANCHORED-REUSE: scout_exact.py s2_kernel -- the relabelling group is
    # the affine stabilizer of the declared direction set, order 108.
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
    # first-event incident triangles and the blindness licence
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
                   "equation and the two-step window constrains nothing",
        "sample_space": "CELLS"}
    LD.gate("G-BLIND", blind and single_link and len(variants) == 11,
            "the depth-2 blindness licence re-measured: 11 record "
            "variants, one Born vector; mechanism single-link site "
            "support", {"variants": len(variants)})
    return psi1, q1, sup1, q2, sup2, BOC, E1S


# ===========================================================================
# SECTION 5.  THE PROXIMITY FORK (declared arms) + ORBIT MACHINERY
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
ARM_DECL = {
    "SA": "the kernel reads the record restricted to the cells sharing "
          "at least one actor with the trigger cell (11 cells)",
    "RD": "the kernel reads the recorded cluster reachable from the "
          "trigger through chains of actor-sharing recorded cells",
    "MC": "the kernel reads the record restricted to cells with an actor "
          "within declared-direction distance one of the trigger's actors",
    "CN": "the kernel reads the record restricted to cells whose actors "
          "or one-step shift images (either orientation) meet the "
          "trigger's actors",
    "GLOBAL": "the un-localized reference: the kernel reads the whole "
              "record (pure covariance, no locality leg)"}


def measure_arms(LD, P, GCELL, GTRI, E1S):
    # M6(a): FULL arm covariance, re-derived by this instrument -- all
    # 108 group elements x all 8 reached records (the unwritten start
    # record and the 7 written first-triple records; the delivered unit
    # sampled one written record, the verifier proved all, and this
    # gate now proves all in-run).
    Rsample = nfield(BLOCK_OF[E1S[0]])
    records = [("R0", R0)] + [("TRI-%d" % k, nfield(BLOCK_OF[e1]))
                              for k, e1 in enumerate(E1S)]
    rows = {}
    allok = True
    for an in ARM_ORDER:
        NF = ARM_FN[an]
        ok = True
        for (_rn, R) in records:
            NFC = {c: NF(c, R) for c in range(DIM)}
            for gi in range(len(GCELL)):
                gc = GCELL[gi]
                gR = [0] * DIM
                for c in range(DIM):
                    gR[gc[c]] = R[c]
                gR = tuple(gR)
                for c in range(DIM):
                    if frozenset(gc[x] for x in NFC[c]) != NF(gc[c], gR):
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        rows[an] = {"name": ARM_NAME[an], "declaration": ARM_DECL[an],
                    "covariant": ok,
                    "records_checked": len(records),
                    "group_elements": len(GCELL),
                    "size_at_cell0_r0": len(NF(0, R0)),
                    "size_at_cell0_sample": len(NF(0, Rsample))}
        allok = allok and ok
    P["arms"] = rows
    LD.gate("G-ARMS-COVARIANT",
            allok and len(records) == 8
            and all(rows[an]["records_checked"] == 8 for an in ARM_ORDER)
            and rows["SA"]["size_at_cell0_r0"] == 11
            and rows["RD"]["size_at_cell0_r0"] == 1
            and rows["RD"]["size_at_cell0_sample"] == 3
            and rows["MC"]["size_at_cell0_r0"] == 27
            and rows["CN"]["size_at_cell0_r0"] == 15
            and rows["GLOBAL"]["size_at_cell0_r0"] == 27,
            "all four declared proximity arms and the global reference "
            "are measured relabelling-covariant (N(gc,gR) = g N(c,R)) "
            "at ALL 108 group elements x ALL 8 reached records -- the "
            "M6 strengthening re-derived in-run; neighborhood sizes 11 "
            "/ record-cluster / 27 / 15 / 27",
            {an: rows[an]["size_at_cell0_r0"] for an in ARM_ORDER})


def loc_pattern(c, R, NF):
    return tuple(sorted((c2, R[c2]) for c2 in NF(c, R) if R[c2] > 0))


def make_canon(GCELL, GTRI):
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


# ===========================================================================
# SECTION 6.  THE REACH CENSUS (depths 2 and 3; step-1 separately, #64)
# ===========================================================================
def reach_census(LD, P, canon_tuple, canon_ctx, sup1, sup2, BOC, E1S):
    RAW = []
    for e1 in E1S:
        R1 = nfield(BLOCK_OF[e1])
        for c2 in sup2:
            for e2 in BOC[c2]:
                RAW.append((e1, R1, c2, e2))
    if mut("MUT-REACH"):
        RAW.append(RAW[0])
    raw_ctx = len(E1S) * len(sup2)
    depth3 = {}
    partitions = {}
    d2parts = {}
    for an in ARM_ORDER:
        NF = ARM_FN[an]
        vmap = {}
        for i, (e1, R1, c2, e2) in enumerate(RAW):
            vmap.setdefault(canon_tuple(R1, c2, e2, NF), []).append(i)
        cmap = {}
        desc = {}
        for e1 in E1S:
            R1 = nfield(BLOCK_OF[e1])
            for c2 in sup2:
                ck = canon_ctx(R1, c2, NF)
                cmap.setdefault(ck, []).append((e1, c2))
                patt = loc_pattern(c2, R1, NF)
                rec_shared = sum(1 for (cc, _v) in patt
                                 if CELL_PAIR[cc] & CELL_PAIR[c2]
                                 and cc != c2)
                desc.setdefault(ck, set()).add(
                    (len(patt), R1[c2] > 0, rec_shared, e1 in LINE_SET))
        d1keys = set()
        for c1 in sup1:
            for e1 in BOC[c1]:
                d1keys.add(canon_tuple(R0, c1, e1, NF))
        d3keys = set(vmap)
        emptyp = {k for k in vmap if k[0] == ()}
        partitions[an] = frozenset(frozenset(v) for v in vmap.values())
        d2parts[an] = len(d1keys)
        depth3[an] = {
            "context_classes": len(cmap),
            "tuple_orbit_variables": len(vmap),
            "depth1_orbit_variables": len(d1keys),
            "shared_with_depth1": len(d1keys & d3keys),
            "empty_pattern_orbits": len(emptyp),
            "class_descriptors": [
                {"class_index": ci,
                 "raw_members": len(cmap[ck]),
                 "descriptor": sorted([list(x) for x in desc[ck]])}
                for ci, ck in enumerate(sorted(cmap))]}
    # M6(b): the refinement order, re-derived by this instrument -- the
    # flat coincidence statement is replaced by the measured fact that
    # the three distinct partitions form a chain in the refinement
    # order: GLOBAL refines CN refines SA (= RD), both strictly.
    def refines(A, B):
        return all(any(blk <= b2 for b2 in B) for blk in A)

    coinc = {"SA_eq_RD": partitions["SA"] == partitions["RD"],
             "MC_eq_GLOBAL": partitions["MC"] == partitions["GLOBAL"],
             "SA_eq_CN": partitions["SA"] == partitions["CN"],
             "CN_eq_GLOBAL": partitions["CN"] == partitions["GLOBAL"],
             "SA_eq_GLOBAL": partitions["SA"] == partitions["GLOBAL"],
             "GLOBAL_refines_CN": refines(partitions["GLOBAL"],
                                          partitions["CN"]),
             "CN_refines_SA": refines(partitions["CN"],
                                      partitions["SA"]),
             "refinement_order": "GLOBAL refines CN refines SA (= RD), "
                                 "both refinements strict; MC = GLOBAL"}
    if mut("MUT-COINC"):
        coinc["SA_eq_RD"] = not coinc["SA_eq_RD"]
    P["reach"] = {
        "raw_tuples": len(RAW), "raw_contexts": raw_ctx,
        "distinct_first_events": len(E1S),
        "depth2": {"context_classes": 1, "tuple_orbits_per_arm":
                   {an: d2parts[an] for an in ARM_ORDER},
                   "note": "at the zero record every localized pattern is "
                           "empty, so all five arms coincide by "
                           "construction at depth 2"},
        "depth3": depth3,
        "sample_space": "TRIPLE-EVENTS"}
    P["coincidence"] = coinc
    LD.gate("G-REACH",
            len(RAW) == 189 and raw_ctx == 63 and len(E1S) == 7
            and {an: depth3[an]["context_classes"] for an in ARM_ORDER}
            == {"SA": 6, "RD": 6, "MC": 9, "CN": 7, "GLOBAL": 9}
            and {an: depth3[an]["tuple_orbit_variables"] for an in ARM_ORDER}
            == {"SA": 16, "RD": 16, "MC": 25, "CN": 19, "GLOBAL": 25}
            and {an: depth3[an]["shared_with_depth1"] for an in ARM_ORDER}
            == {"SA": 2, "RD": 2, "MC": 0, "CN": 2, "GLOBAL": 0}
            and all(d2parts[an] == 2 for an in ARM_ORDER),
            "the reach census: 63 raw contexts / 189 raw tuples over 7 "
            "distinct first events; per-arm depth-3 orbit variables "
            "16/16/25/19/25 against context classes 6/6/9/7/9; the "
            "shared-actor, record-distance and causal arms each carry 2 "
            "empty-pattern orbits identified with the depth-1 classes",
            {"raw": len(RAW)})
    LD.gate("G-COINCIDE",
            coinc["SA_eq_RD"] and coinc["MC_eq_GLOBAL"]
            and not coinc["SA_eq_CN"] and not coinc["CN_eq_GLOBAL"]
            and not coinc["SA_eq_GLOBAL"]
            and coinc["GLOBAL_refines_CN"] and coinc["CN_refines_SA"],
            "proximity coincidences measured, not assumed, and "
            "sharpened to the refinement-order fact (M6): SA and RD "
            "induce the same orbit partition; MC coincides with the "
            "global reading (its neighborhood is the whole chart at "
            "this arena); and the three distinct partitions form a "
            "chain -- GLOBAL refines CN refines SA, both refinements "
            "strict -- so CN sits strictly between and three distinct "
            "constraint systems remain", coinc)
    return RAW


def step1_census(LD, P, canon_tuple, sup1, BOC):
    # #64 FIRST-EVENT BOUNDARY: the step-1 orbit census published
    # separately.  At the symmetric start the record is unwritten, so the
    # orbit family collapses to the (c,e) orbits: line / non-line.
    NF = ARM_FN["GLOBAL"]
    keys = set()
    for c1 in sup1:
        for e1 in BOC[c1]:
            keys.add(canon_tuple(R0, c1, e1, NF))
    nvars = pick("MUT-STEP1", len(keys), len(keys) + 1)
    # normalization a + 2b = 1 -> family dim 1; deterministic covariant
    # selections: only a=1 (the line); a=0 splits 1/2-1/2 by the
    # stabilizer swap (G-GAMMA), so no covariant deterministic non-line
    # selection exists.
    trilemma = {
        "a_symmetric_stochastic_initial_kernel":
            "REALIZED-BY-THE-MEASURED-FAMILY (the dim-1 line-weight "
            "family a in [0,1]; the only deterministic covariant member "
            "is the line selection a=1 -- the stabilizer swap forbids a "
            "deterministic non-line pick)",
        "b_declared_initial_asymmetry":
            "NOT-REALIZABLE-WITHIN-THE-COVARIANT-FAMILY (privileging a "
            "label breaks K(ge|gc,gG,gR)=K(e|c,G,R); it would be a "
            "declared exit from equivariance, priced as a declaration)",
        "c_another_tie_breaking_state_variable":
            "NOT-REALIZABLE-WITHIN-K(e|c,G,R) (the declared kernel "
            "signature carries no further state slot; adding one is a "
            "new law, registered as a successor)"}
    P["step1"] = {
        "orbit_variables": nvars,
        "family_dim_after_normalization": 1,
        "collapse": "the depth-3 census grants 16/16/25/19/25 orbit "
                    "variables per arm; the unwritten record collapses "
                    "step 1 to 2 variables at every arm -- the collapse "
                    "size is 14/14/23/17/23 variables lost to symmetry",
        "tie_break_trilemma": trilemma,
        "sample_space": "TRIPLE-EVENTS"}
    LD.gate("G-STEP1", nvars == 2,
            "the step-1 orbit census is published separately (#64): the "
            "symmetric start collapses the kernel family to 2 orbit "
            "variables (line / non-line), dim 1 after normalization; the "
            "tie-break trilemma is recorded as measured constraints -- "
            "the family realizes arm (a) only",
            {"orbit_variables": nvars})


# ===========================================================================
# SECTION 7.  THE DEPTH-2 SYSTEM (window of two steps)
# ===========================================================================
def depth2_system(LD, P, psi1, q2, sup1, BOC):
    # kernel invoked once, at the zero record; consistency rows:
    # sum_e1 k1(e1) born(psi1, B(e1))[c2] = born(psi1, [c1])[c2].
    # By G-BLIND every Born factor is the same vector, so each row is
    # q2[c2] * (normalization) and the system is normalization alone.
    rows_vac = True
    for c1 in sup1:
        rhs = born(psi1, nfield([c1]), "G.D")
        for e1 in BOC[c1]:
            if born(psi1, nfield(BLOCK_OF[e1]), "G.D") != rhs:
                rows_vac = False
    nvars = 2
    norm = [[F(1), F(2)]]
    caps_note("D2-NORM")
    dim = pick("MUT-D2", len(null_of(norm)), 2)
    P["d2"] = {
        "kernel_variables": nvars,
        "normalization_rank": rank_of(norm),
        "consistency_rows_vacuous_given_blindness": rows_vac,
        "polytope_dim": dim,
        "verdict_per_arm": {an: "SCOUTK-NONVACUOUS-1-AT-2-" + an
                            for an in ("SA", "RD", "MC", "CN")},
        "arms_coincide": "all arms coincide at depth 2 (zero record, "
                         "empty localized patterns everywhere)",
        "sample_space": "TRIPLE-EVENTS"}
    LD.gate("G-D2", rows_vac and dim == 1,
            "the depth-2 window: consistency is vacuous under the "
            "measured blindness, the covariant family is the "
            "one-parameter line-weight segment a in [0,1] -- "
            "SCOUTK-NONVACUOUS-1-AT-2 at every arm, arms coinciding at "
            "the zero record", {"dim": dim})


# ===========================================================================
# SECTION 8.  THE DEPTH-3 SYSTEMS (the window with teeth)
# ===========================================================================
SAMPLES = (F(0), F(1, 6), F(1, 3), F(1, 2), F(2, 3), F(1))
SYSTEMS = (("SA-RD", "SA"), ("CN", "CN"), ("MC-GLOBAL", "GLOBAL"))


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
                raise GateFail("G-D3-SAMPLES", "undefined q3 branch")
            memo[key] = v
        return memo[key]
    return q3_of


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
    empties = sorted(vidx[k] for k in vidx if k[0] == ())
    empty_line = [j for j in empties if lineness[j]]
    empty_nonline = [j for j in empties if not lineness[j]]
    return {"nv": nv, "vidx": vidx, "TUP": TUP, "lineness": lineness,
            "line_ok": line_ok, "ctx_ok": ctx_ok, "normrows": normrows,
            "mixrows": mixrows, "empty_line": empty_line,
            "empty_nonline": empty_nonline}


def system_at(S, a, extra_pins=None):
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
        caps_note("MIX")
    for r in S["normrows"]:
        key = (r, F(1))
        if key not in seen:
            seen[key] = True
            A.append(list(r))
            b.append(F(1))
            meta.append(["NORM"])
            caps_note("NORM")
    if extra_pins:
        for (j, val) in extra_pins:
            row = [F(0)] * nv
            row[j] = F(1)
            A.append(row)
            b.append(val)
            meta.append(["PIN", j])
            caps_note("PIN")
    return A, b, meta


def depth3_systems(LD, P, canon_tuple, canon_ctx, q3_of, sup1, sup2, BOC,
                   E1S, RAW):
    out = {}
    welldef_ok = True
    for (label, an) in SYSTEMS:
        S = build_system(an, canon_tuple, canon_ctx, q3_of, sup1, sup2,
                         BOC, E1S, RAW)
        welldef_ok = welldef_ok and S["line_ok"] and S["ctx_ok"]
        srows = []
        for a in SAMPLES:
            A, b, meta = system_at(S, a)
            st, gap, x, y = simplex(A, b)
            if mut("MUT-SAMPLE") and a == F(1, 3):
                st = "FEASIBLE"
            if mut("MUT-CERT") and a == F(1, 3):
                y = [y[0] + 1] + list(y[1:])
            fk = farkas_ok(A, b, y, gap) if st == "INFEASIBLE" else None
            srows.append({"a": a, "rows": len(A), "status": st,
                          "gap": gap, "farkas_valid": fk,
                          "sample_space": "CELLS"})
        # branchwise lemma
        Abw, bbw = [], []
        seenbw = {}
        for c1 in sup1:
            for e1 in BOC[c1]:
                for c2 in sup2:
                    rhs = q3_of([c1], [c2])
                    rows = [[F(0)] * S["nv"] for _ in range(DIM)]
                    for e2 in BOC[c2]:
                        j = S["TUP"][(e1, c2, e2)]
                        v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                        for c3 in range(DIM):
                            if v[c3] != 0:
                                rows[c3][j] += v[c3]
                    for c3 in range(DIM):
                        row = tuple(rows[c3])
                        key = (row, rhs[c3])
                        if (any(v != 0 for v in row) or rhs[c3] != 0) \
                                and key not in seenbw:
                            seenbw[key] = True
                            Abw.append(list(row))
                            bbw.append(rhs[c3])
                            caps_note("BRANCHWISE-MIX")
        for r in S["normrows"]:
            if (r, F(1)) not in seenbw:
                Abw.append(list(r))
                bbw.append(F(1))
                caps_note("BRANCHWISE-NORM")
        stb, gapb, xb, yb = simplex(Abw, bbw)
        if mut("MUT-BW"):
            stb = "FEASIBLE"
        bwrow = {"rows": len(Abw), "status": stb, "gap": gapb,
                 "farkas_valid": farkas_ok(Abw, bbw, yb, gapb)
                 if stb == "INFEASIBLE" else None,
                 "sample_space": "CELLS"}
        # uniform-in-a Farkas certificate over the whole segment [0,1]
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
        ncols = 2 * m + 2 * S["nv"]
        rows, rhsv = [], []
        for j in range(S["nv"]):
            r = [F(0)] * ncols
            for i in range(m):
                r[i] = A0[i][j]
                r[m + i] = -A0[i][j]
            r[2 * m + j] = F(1)
            rows.append(r)
            rhsv.append(F(0))
        for j in range(S["nv"]):
            r = [F(0)] * ncols
            for i in range(m):
                v = A0[i][j] + A1[i][j]
                r[i] = v
                r[m + i] = -v
            r[2 * m + S["nv"] + j] = F(1)
            rows.append(r)
            rhsv.append(F(0))
        r = [F(0)] * ncols
        for i in range(m):
            r[i] = bb[i]
            r[m + i] = -bb[i]
        rows.append(r)
        rhsv.append(F(1))
        caps_note("UNIFORM-CERT-SEARCH", len(rows))
        stu, _gu, xu, _yu = simplex(rows, rhsv)
        uni = {"system_rows": m, "search_status": stu,
               "sample_space": "CELLS"}
        if stu == "FEASIBLE":
            yy = [xu[i] - xu[m + i] for i in range(m)]
            if mut("MUT-UNIF"):
                yy = [yy[0] + 1] + list(yy[1:])
            nz = [(i, yy[i]) for i in range(m) if yy[i] != 0]
            ok0 = all(sum(yy[i] * A0[i][j] for i in range(m)) <= 0
                      for j in range(S["nv"]))
            ok1 = all(sum(yy[i] * (A0[i][j] + A1[i][j])
                          for i in range(m)) <= 0 for j in range(S["nv"]))
            okb = sum(yy[i] * bb[i] for i in range(m)) == 1
            # the affinity spot-check licensing the two-endpoint argument
            mid_ok = True
            for (r0, r1, rhs, mm2) in S["mixrows"][:30]:
                lhs = tuple(x + F(1, 2) * y for x, y in zip(r0, r1))
                rr = tuple((x + (x + y)) / 2 for x, y in zip(r0, r1))
                if lhs != rr:
                    mid_ok = False
            uni.update({
                "certificate_support": len(nz),
                "support_rows": [{"row_meta": trip[order[i]],
                                  "y": yv} for (i, yv) in nz],
                "endpoint0_ok": ok0, "endpoint1_ok": ok1,
                "yb_equals_one": okb, "affine_midpoint_ok": mid_ok,
                "reading": "y.A(a) is affine in a per component, so the "
                           "two endpoint checks bound the whole segment; "
                           "with y.b = 1 the system is infeasible at "
                           "EVERY first-step line weight a in [0,1]"})
            uni_ok = ok0 and ok1 and okb and mid_ok
        else:
            uni_ok = False
        out[label] = {"arm_solved": an, "nv": S["nv"],
                      "samples": srows, "branchwise": bwrow,
                      "uniform_certificate": uni,
                      "empty_pattern_line_vars": S["empty_line"],
                      "empty_pattern_nonline_vars": S["empty_nonline"]}
        out[label]["_S"] = S
        if not uni_ok:
            out[label]["uniform_certificate"]["verified"] = False
        else:
            out[label]["uniform_certificate"]["verified"] = True
    P["d3_welldef"] = {"line_ok_and_ctx_ok_all_systems":
                       pick("MUT-CTX", welldef_ok, False)}
    LD.gate("G-WELLDEF", P["d3_welldef"]["line_ok_and_ctx_ok_all_systems"],
            "orbit bookkeeping is self-consistent: line-ness is constant "
            "on every orbit and relabelling-equivalent contexts carry "
            "identical candidate variable multisets, at all three "
            "distinct systems", None)
    # strip the private builder handle before the receipt
    samples_ok = all(
        r["status"] == "INFEASIBLE"
        for lbl in out for r in out[lbl]["samples"])
    P["d3"] = {lbl: {k: v for k, v in out[lbl].items() if k != "_S"}
               for lbl in out}
    LD.gate("G-D3-SAMPLES",
            samples_ok and all(len(out[lbl]["samples"]) == 6
                               for lbl in out),
            "the depth-3 covariant systems are INFEASIBLE at every "
            "declared sample of the first-step line weight (6 samples x "
            "3 distinct systems, 18 exact refusals)",
            {lbl: [str(r["gap"]) for r in out[lbl]["samples"]]
             for lbl in out})
    LD.gate("G-D3-FARKAS",
            all(r["farkas_valid"] for lbl in out
                for r in out[lbl]["samples"]),
            "every sampled emptiness carries a verified exact Farkas "
            "certificate: y.A <= 0 columnwise, y <= 1, y.b = gap",
            {"certificates": 18})
    LD.gate("G-D3-BW",
            all(out[lbl]["branchwise"]["status"] == "INFEASIBLE"
                and out[lbl]["branchwise"]["farkas_valid"] for lbl in out),
            "the branchwise (per-first-event) lemma: even conditioning "
            "on each written first triple separately, no covariant "
            "second-invocation kernel matches the delivered third-step "
            "profiles -- INFEASIBLE with verified certificates at all "
            "three systems",
            {lbl: str(out[lbl]["branchwise"]["gap"]) for lbl in out})
    LD.gate("G-D3-UNIFORM",
            all(out[lbl]["uniform_certificate"].get("verified")
                for lbl in out),
            "one uniform Farkas certificate per system closes the whole "
            "segment: emptiness holds at EVERY first-step line weight "
            "a in [0,1], not only at the samples; supports 6, 6 and 7 "
            "rows, all mixture rows",
            {lbl: out[lbl]["uniform_certificate"]["certificate_support"]
             for lbl in out})
    return out


def depth3_identified(LD, P, out3):
    # the identified (non-relaxed) systems: where empty-pattern depth-3
    # orbits coincide with the depth-1 classes (SA-RD and CN), locality +
    # covariance force x_line-empty = a and x_nonline-empty = (1-a)/2.
    # The relaxed system omits these pins, so its solution set contains
    # the identified one; emptiness therefore transfers.  Run the pinned
    # systems at two declared samples as confirmation.
    runs = []
    for lbl in ("SA-RD", "CN"):
        S = out3[lbl]["_S"]
        for a in (F(1, 3), F(1, 2)):
            pins = [(j, a) for j in S["empty_line"]] + \
                   [(j, (1 - a) / 2) for j in S["empty_nonline"]]
            A, b, meta = system_at(S, a, extra_pins=pins)
            st, gap, x, y = simplex(A, b)
            if mut("MUT-IDENT") and lbl == "SA-RD" and a == F(1, 3):
                st = "FEASIBLE"
            runs.append({"system": lbl, "a": a, "pins": len(pins),
                         "status": st, "gap": gap,
                         "farkas_valid": farkas_ok(A, b, y, gap)
                         if st == "INFEASIBLE" else None,
                         "sample_space": "CELLS"})
    P["d3_identified"] = {
        "runs": runs,
        "relaxation_lemma": "the identified family adds pin rows to the "
                            "relaxed system on the same variables, so "
                            "every identified solution solves the relaxed "
                            "system; the relaxed emptiness (uniform in a) "
                            "already covers it, and the pinned runs "
                            "confirm"}
    LD.gate("G-D3-IDENT",
            all(r["status"] == "INFEASIBLE" and r["farkas_valid"]
                for r in runs) and len(runs) == 4,
            "the identified systems (empty-pattern orbits pinned to the "
            "step-1 kernel values) are INFEASIBLE at both confirmation "
            "samples for both affected systems, certificates verified",
            {"runs": len(runs)})


def clash_witness(LD, P, out3):
    # the minimal mechanism witness: at a = 0 two mixture rows of the
    # MC-GLOBAL system have IDENTICAL covariant coefficient vectors while
    # the delivered walk assigns them different values.
    # M6(c): the witness is gated as the FIRST clash in canonical
    # (c1,c2,c3) row order, re-derived by this instrument -- the row
    # metas are verified sorted, every clash is counted, and the
    # published pair is the first one, so the witness is canonical,
    # not curated.
    S = out3["MC-GLOBAL"]["_S"]
    metas = [m for (_r0, _r1, _rhs, m) in S["mixrows"]]
    canon_order_ok = all(metas[i] <= metas[i + 1]
                         for i in range(len(metas) - 1))
    seen = {}
    wit = None
    clashes = 0
    for (r0, r1, rhs, m) in S["mixrows"]:
        row = r0  # a = 0
        if all(v == 0 for v in row) and rhs == 0:
            continue
        if row in seen and seen[row][0] != rhs:
            clashes += 1
            if wit is None:
                wit = {"row_a": list(seen[row][1]), "rhs_a": seen[row][0],
                       "row_b": list(m), "rhs_b": rhs,
                       "delta": rhs - seen[row][0],
                       "sample_space": "CELLS"}
        if row not in seen:
            seen[row] = (rhs, m)
    if mut("MUT-CLASH"):
        wit = None
    P["clash"] = {
        "witness": wit,
        "clashes_at_a0": clashes,
        "canonical_row_order_verified": canon_order_ok,
        "witness_is_first_clash_in_canonical_order":
            wit is not None and canon_order_ok,
        "mechanism": "covariance identifies second-invocation tuples "
                     "across branches that the anchored start state "
                     "distinguishes: the two branches' kernel-weighted "
                     "predictions are the SAME covariant combination "
                     "while the delivered walk gives them different "
                     "values -- overdetermination, the same death mode "
                     "as #58, now at the full record-dependent family"}
    LD.gate("G-CLASH",
            wit is not None and wit["row_a"] == [0, 5, 14]
            and wit["row_b"] == [1, 11, 21]
            and str(wit["rhs_a"]) == "16/729"
            and str(wit["rhs_b"]) == "64/729"
            and canon_order_ok and clashes >= 1,
            "the minimal mechanism witness stands: at a = 0 the branch "
            "rows (c1,c2,c3) = (0,5,14) and (1,11,21) carry identical "
            "covariant coefficient vectors with delivered values 16/729 "
            "against 64/729; the witness is the FIRST clash in "
            "canonical row order (metas verified sorted; M6) -- "
            "canonical, not curated",
            wit)


# ===========================================================================
# SECTION 9.  THE FIXED-ALPHA SUBFAMILY (the binding consistency check)
# ===========================================================================
def kpoly(t):
    # ANCHORED-REUSE: scout_exact.py s2_record_consistency kpoly --
    # K_alpha: alpha on the line block, (1-alpha)/2 on each non-line.
    if t in LINE_SET:
        return (F(0), F(1))
    return (F(1, 2), F(-1, 2))


def pmul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return tuple(out)


def padd(p, q):
    n = max(len(p), len(q))
    out = [F(0)] * n
    for i, a in enumerate(p):
        out[i] += a
    for i, b in enumerate(q):
        out[i] += b
    return tuple(out)


def subfamily(LD, P, out3, q3_of, sup1, sup2, BOC):
    # direct route (the parent's own construction, re-typed)
    polys = set()
    nrows = 0
    compat = {}
    for c1 in sup1:
        for c2 in sup2:
            rhs = q3_of([c1], [c2])
            acc = [tuple() for _ in range(DIM)]
            for e1 in BOC[c1]:
                for e2 in BOC[c2]:
                    v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                    cflag = (v == rhs)
                    if mut("MUT-COMPAT") and (c1, e1, c2, e2) == \
                            (sup1[0], BOC[sup1[0]][0], sup2[0],
                             BOC[sup2[0]][0]):
                        cflag = not cflag
                    compat[(c1, e1, c2, e2)] = cflag
                    w = pmul(kpoly(e1), kpoly(e2))
                    for c3 in range(DIM):
                        if v[c3] != 0:
                            acc[c3] = padd(acc[c3],
                                           tuple(x * v[c3] for x in w))
            for c3 in range(DIM):
                pp = padd(acc[c3], (-rhs[c3],)) if rhs[c3] != 0 \
                    else acc[c3]
                pp = tuple(pp)
                while pp and pp[-1] == 0:
                    pp = pp[:-1]
                if pp:
                    polys.add(pp)
                nrows += 1
    if mut("MUT-POLY"):
        polys = {p for p in polys if len(p) != 2}
    lin_roots = sorted({-p[0] / p[1] for p in polys if len(p) == 2})
    alpha_tests = {}
    for a in (F(0), F(1, 3), F(1)):
        alpha_tests[str(a)] = all(
            sum(co * a ** i for i, co in enumerate(p)) == 0 for p in polys)
    # subfamily route: tie the orbit variables record-blind inside the
    # MC-GLOBAL system's own rows -- x_j = alpha on line orbits and
    # (1-alpha)/2 on non-line orbits -- and collect the row polynomials.
    S = out3["MC-GLOBAL"]["_S"]
    polys2 = set()
    for (r0, r1, rhs, m) in S["mixrows"]:
        p = (F(-rhs),) if rhs != 0 else (F(0),)
        for j in range(S["nv"]):
            if r0[j] == 0 and r1[j] == 0:
                continue
            xj = (F(0), F(1)) if S["lineness"][j] else (F(1, 2), F(-1, 2))
            p = padd(p, pmul((r0[j], r1[j]), xj))
        pp = tuple(p)
        while pp and pp[-1] == 0:
            pp = pp[:-1]
        if pp:
            polys2.add(pp)
    P["subfamily"] = {
        "rows": nrows, "distinct_nonzero_polys": len(polys),
        "linear_poly_roots": lin_roots,
        "alpha_probes_all_fail": {k: v for k, v in
                                  sorted(alpha_tests.items())},
        "via_orbit_rows_polys": len(polys2),
        "via_orbit_rows_equal_to_direct": polys2 == polys,
        "reading": "the record-blind fixed-alpha family is a "
                   "1-dimensional subfamily of this census's orbit "
                   "family (constant on orbits; line-ness is "
                   "orbit-invariant), and inside THIS instrument's rows "
                   "it reproduces #58's refusal exactly",
        "sample_space": "CELLS"}
    LD.gate("G-SUBFAM",
            nrows == 729 and len(polys) == 25
            and lin_roots == [F(-1), F(0), F(1)]
            and not any(alpha_tests.values())
            and polys2 == polys,
            "the binding consistency check: the fixed-alpha subfamily "
            "re-derived inside the orbit family gives 729 rows reducing "
            "to 25 distinct polynomials whose linear members force "
            "alpha = -1, 0 and +1 simultaneously (empty over the reals), "
            "byte-equal to the direct parent-style construction",
            {"rows": nrows, "polys": len(polys)})
    combos_ok = []
    total_kernels = 0
    for combo in product(*[BOC[c] for c in sup1]):
        prod_ct = 1
        ok = True
        for c2 in sup2:
            k = sum(1 for e2 in BOC[c2]
                    if all(compat[(c1, combo[i], c2, e2)]
                           for i, c1 in enumerate(sup1)))
            if k == 0:
                ok = False
                break
            prod_ct *= k
        if ok:
            combos_ok.append([t in LINE_SET for t in combo])
            total_kernels += prod_ct
    P["pure"] = {
        "surviving_first_step_combos": len(combos_ok),
        "all_nonline": all(not any(pat) for pat in combos_ok),
        "pure_kernels_total": total_kernels,
        "reading": "the 288 pure record-dependent kernels the parent "
                   "counted DO exist pointwise, and this census now "
                   "prices them: none is realizable by any covariant "
                   "assignment -- the whole covariant family is empty, "
                   "so every survivor breaks relabelling symmetry",
        "sample_space": "CELLS"}
    LD.gate("G-PURE",
            len(combos_ok) == 8 and P["pure"]["all_nonline"]
            and total_kernels == 288,
            "the parent's pure-kernel census reproduced: 8 all-non-line "
            "first-step selections extending to 288 pure kernels on the "
            "reached cells",
            {"combos": len(combos_ok), "total": total_kernels})


# ===========================================================================
# SECTION 10.  CONTROLS (through the real builder and solver)
# ===========================================================================
def controls(LD, P, canon_tuple, canon_ctx, q3_of, sup1, sup2, BOC, E1S,
             RAW):
    def rhs_kernel(c1c2):
        c1, c2 = c1c2
        vout = [F(0)] * DIM
        for e1 in BOC[c1]:
            for e2 in BOC[c2]:
                v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                for c3 in range(DIM):
                    vout[c3] += F(1, 3) * F(1, 3) * v[c3]
        return tuple(vout)

    Sf = build_system("GLOBAL", canon_tuple, canon_ctx, q3_of, sup1, sup2,
                      BOC, E1S, RAW, rhs_override=rhs_kernel)
    A, b, meta = system_at(Sf, F(1, 3))
    stf, _g, xf, _y = simplex(A, b)
    # negative control: the uniform-certificate search must FAIL on the
    # feasible synthetic (no Farkas certificate exists for a feasible
    # system at the sampled member a = 1/3)
    wit_ok = None
    if stf == "FEASIBLE":
        wit_ok = all(v >= 0 for v in xf)

    def rhs_bad(c1c2):
        v = list(q3_of([c1c2[0]], [c1c2[1]]))
        v[0] += 1
        return tuple(v)

    Se = build_system("GLOBAL", canon_tuple, canon_ctx, q3_of, sup1, sup2,
                      BOC, E1S, RAW, rhs_override=rhs_bad)
    A2, b2, meta2 = system_at(Se, F(1, 3))
    ste, gape, _x2, ye = simplex(A2, b2)
    if mut("MUT-CTRL"):
        ste = "FEASIBLE"
    P["controls"] = {
        "forced_nonvacuous": {
            "construction": "target statistics generated by the declared "
                            "covariant record-dependent kernel (uniform "
                            "1/3 per candidate, a = 1/3) through the real "
                            "builder",
            "status": stf, "witness_nonnegative": wit_ok,
            "sample_space": "CELLS"},
        "forced_empty": {
            "construction": "one delivered branch value shifted by +1",
            "status": ste, "gap": gape,
            "farkas_valid": farkas_ok(A2, b2, ye, gape)
            if ste == "INFEASIBLE" else None,
            "sample_space": "CELLS"}}
    LD.gate("G-CONTROLS",
            stf == "FEASIBLE" and wit_ok
            and ste == "INFEASIBLE"
            and P["controls"]["forced_empty"]["farkas_valid"],
            "both synthetic controls fire through the real builder and "
            "solver: the kernel-generated target is FEASIBLE with a "
            "nonnegative witness, the shifted target is INFEASIBLE with "
            "a verified certificate", None)


def caps_register_gate(LD, P):
    # M5 (verifier finding F6): the note's no-caps sentence was an
    # unbound negative claim; this register binds it.  Every constraint
    # row constructed anywhere in the chain is typed at its
    # construction site; no CAP kind exists and no cap machinery is
    # present, so the register shows zero engaged caps.
    counts = {k: CAPS["counter"][k] for k in sorted(CAPS["counter"])}
    if mut("MUT-CAPS"):
        counts["CAP"] = 1
    engaged = counts.get("CAP", 0)
    allowed = {"MIX", "NORM", "PIN", "BRANCHWISE-MIX", "BRANCHWISE-NORM",
               "UNIFORM-CERT-SEARCH", "D2-NORM"}
    P["caps_register"] = {
        "row_kinds": counts,
        "engaged_caps": engaged,
        "policy": "every constraint row is typed at its construction "
                  "site (mixture / normalization / pin / branchwise / "
                  "uniform-certificate-search / depth-two "
                  "normalization); no CAP kind exists in this "
                  "instrument and no cap machinery is present, so zero "
                  "caps were engaged anywhere in the chain -- the "
                  "note's no-caps sentence is receipt-backed here"}
    LD.gate("G-CAPS-REGISTER",
            engaged == 0 and set(counts) <= allowed
            and sum(counts.values()) > 0,
            "the caps register: every constraint row this instrument "
            "constructed carries a declared kind, the kind set is the "
            "declared cap-free family, and zero engaged caps exist",
            {"engaged_caps": engaged, "kinds": sorted(counts)})


# ===========================================================================
# SECTION 11.  SAMPLE SPACES, NUMERAL BINDING, VERDICTS, KIT
# ===========================================================================
SS_NAMES = ("CELLS", "TRIPLE-EVENTS", "COMPLETE-SUCCESSOR-CONFIGURATIONS")


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
    LD.gate("G-SAMPLE-SPACE", len(found) == 38 and not bad,
            "every probability-typed measurement row in this receipt "
            "declares its sample space from the three declared names, 38 "
            "declarations; no claim changes sample space silently",
            {"declared": len(found)})


NUM_BINDINGS = (
    ("108", "gamma/order"),
    ("27", "arena/cells"),
    ("189", "reach/raw_tuples"),
    ("63", "reach/raw_contexts"),
    ("7", "reach/distinct_first_events"),
    ("16", "reach/depth3/SA/tuple_orbit_variables"),
    ("16", "reach/depth3/RD/tuple_orbit_variables"),
    ("25", "reach/depth3/GLOBAL/tuple_orbit_variables"),
    ("19", "reach/depth3/CN/tuple_orbit_variables"),
    ("6", "reach/depth3/SA/context_classes"),
    ("9", "reach/depth3/GLOBAL/context_classes"),
    ("2", "step1/orbit_variables"),
    ("1", "d2/polytope_dim"),
    ("11", "blindness/variants"),
    ("729", "subfamily/rows"),
    ("25", "subfamily/distinct_nonzero_polys"),
    ("8", "pure/surviving_first_step_combos"),
    ("288", "pure/pure_kernels_total"),
    ("38", "sample_spaces/declared"),
    ("6", "d3/SA-RD/uniform_certificate/certificate_support"),
    ("7", "d3/MC-GLOBAL/uniform_certificate/certificate_support"),
    ("16/729", "clash/witness/rhs_a"),
    ("64/729", "clash/witness/rhs_b"),
    ("30", "regime/gates_in_ledger"),
    ("29", "regime/falsifiers_registered"),
)


def resolve_path(P, path):
    cur = fser(P)
    for part in path.split("/"):
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
            "numeral-field binding from birth: every load-bearing prose "
            "numeral is bound to its SPECIFIC receipt field and each "
            "binding resolves to the claimed value",
            {"bindings": len(rows),
             "failed": [r["receipt_field"] for r in rows
                        if not r["bound"]]})


def build_verdicts(P):
    V = {}
    V["REACH"] = ("SCOUTK-REACH-CENSUS-PUBLISHED"
                  "<63-CONTEXTS-189-TUPLES-7-FIRST-EVENTS; "
                  "ORBIT-VARIABLES-16-16-25-19-25-PER-ARM; "
                  "STEP-1-COLLAPSES-TO-2-VARIABLES-DIM-1>")
    V["D2"] = ("SCOUTK-NONVACUOUS-1-AT-2-ALL-ARMS"
               "<BLINDNESS-11-VARIANTS; "
               "ARMS-COINCIDE-AT-THE-ZERO-RECORD>")
    d3ok = all(
        P["d3"][lbl]["uniform_certificate"].get("verified")
        and all(r["status"] == "INFEASIBLE"
                for r in P["d3"][lbl]["samples"])
        for lbl in P["d3"])
    if d3ok:
        # M1 (the #68 addendum, item 1): every verdict names its
        # consistency mode -- the frozen PRIMARY, CONDITIONAL.
        V["D3"] = ("SCOUTK-COVARIANT-EMPTY-AT-3-SA"
                   "-AT-CONDITIONAL-CONSISTENCY; "
                   "SCOUTK-COVARIANT-EMPTY-AT-3-RD"
                   "-AT-CONDITIONAL-CONSISTENCY; "
                   "SCOUTK-COVARIANT-EMPTY-AT-3-MC"
                   "-AT-CONDITIONAL-CONSISTENCY; "
                   "SCOUTK-COVARIANT-EMPTY-AT-3-CN"
                   "-AT-CONDITIONAL-CONSISTENCY"
                   "<GLOBAL-REFERENCE-ALSO-EMPTY-SO-LOCALITY-IS-NOT-THE-"
                   "OBSTRUCTION; UNIFORM-IN-THE-FIRST-STEP-LINE-WEIGHT; "
                   "BRANCHWISE-ALSO-EMPTY; "
                   "CERTIFICATES-PUBLISHED-AND-VERIFIED>")
    else:
        V["D3"] = "SCOUTK-UNDETERMINED"
    V["SUBFAMILY"] = ("SCOUTK-FIXED-ALPHA-SUBFAMILY-REPRODUCES-58"
                      "<729-ROWS-25-POLYS-LINEAR-ROOTS-MINUS1-0-PLUS1; "
                      "PURE-CENSUS-8-TO-288-REPRODUCED>")
    V["BRIDGE"] = ("SCOUTK-CANDIDATE-BRIDGE-REJECTED-IN-ITS-COVARIANT-"
                   "CLASS<THE-TRIGGER-SEMANTICS-REMAINS-A-CANDIDATE-"
                   "NEVER-A-THEOREM; EVENT-SELECTION-ONLY-TRANSPORT-"
                   "STILL-OPEN>")
    P["verdicts"] = V
    P["registered_successors"] = [
        "the depth-4 window (registered, not claimed)",
        "sub-normalized / leaky kernels outside the per-trigger "
        "normalization leg",
        "kernels with an additional tie-breaking state slot beyond "
        "(c,G,R) -- trilemma arm (c)",
        "declared-asymmetry (non-equivariant) kernels -- trilemma arm "
        "(b), a priced exit from covariance",
        "the ordered trigger trace and the marginal-history mode -- "
        "SCOUT-T (v15/note-scoutt-pin.md, FROZEN sha256-12 "
        "3f35573d88d8, pinned at v15 ledger #82), the named successor "
        "for the trace fork",
        "the quantum transport law rho'_e onto created cells (open "
        "regardless of any kernel outcome)"]


TERM_TABLE = (
    ("CELL-HIT", "paper-20's primitive: one Born-selected pair-cell "
     "increment per step (the mandatory rename)"),
    ("DIVISION-EVENT", "paper-19's three-actor conflict group whose "
     "footprint writes all three pair-relations; the only object this "
     "note calls a division event"),
    ("TRIPLE-EVENT", "a division event carried as one probabilistic "
     "alternative"),
    ("TRIGGER", "the cell the quantum menu selects; the conditional seat "
     "of q(c) under the ADOPTED CANDIDATE bridge "
     "P(c,e|X) = q(c|X) K(e|c,G,R) -- a candidate this census tests, "
     "never an established physical mechanism"),
    ("SUCCESSOR", "a COMPLETE-SUCCESSOR-CONFIGURATION X'_e = (G'_e, "
     "R'_e, rho'_e, event data): one outcome of the E-34.4 "
     "normalization rule"),
    ("RECORD", "the co-division relation with its multiplicities (ECC's "
     "sense, unchanged)"),
    ("KERNEL CONTEXT", "the localized pair (R restricted to the arm's "
     "neighborhood of the trigger, the trigger cell), up to simultaneous "
     "relabelling"),
    ("ORBIT VARIABLE", "one free kernel weight per relabelling orbit of "
     "localized (record, trigger, candidate event) tuples -- "
     "record-dependence through orbit structure only"),
)


# ---- the gated kit sentences added by the micro-repair (M1/M5/M6) ------
KIT_GFIXED = ("G is FIXED throughout — this unit tests RECORD "
              "backreaction only; transport across created cells and "
              "any G-to-G-prime remain independent missing laws")
KIT_MODE = ("the consistency mode is the #68 addendum's frozen PRIMARY "
            "-- CONDITIONAL transition agreement at every reached "
            "state: at fixed first-step weight each depth-3 constraint "
            "is linear in exactly one kernel factor (the "
            "second-invocation orbit variable), the first factor is "
            "swept exactly and closed by the uniform certificate, no "
            "bilinear system is solved, and the only relaxation used "
            "runs in the conservative emptiness direction with pinned "
            "confirmations -- and the D3 verdict names the mode in its "
            "words")
KIT_PRECISE = ("at this arena, no normalized covariant conditional "
               "kernel K(e|c,G,R) with fixed geometry, the trigger "
               "factorization P(c,e) = q(c) K(e|c,G,R), and exact "
               "preservation of the delivered cell-walk's conditional "
               "statistics, works through window 3 -- even with the "
               "entire record; it does NOT kill the triple ontology, "
               "covariance, locality generally, kernels with "
               "additional state or history, changing geometry, "
               "non-trigger-factorized bridges, history-level "
               "indivisible processes, or agreement at the "
               "observable-history level only")
KIT_ERASURE = ("the kernel construction builds the available record "
               "from the whole triple footprint while the target walk "
               "depends on the individual cell-trigger history -- the "
               "bridge lets one cell trigger a three-cell event, the "
               "triple record forgets which cell was the trigger, and "
               "the walk remembers and uses it; global access cannot "
               "recover information the bridge erased at write-time")
KIT_CAPS = ("the caps register records zero engaged caps anywhere in "
            "the chain: every constraint row is typed at its "
            "construction site and no capped row exists")


def build_kit(P):
    kit = []
    kit.append("SCOUT-K verdicts:")
    for k in ("REACH", "D2", "D3", "SUBFAMILY", "BRIDGE"):
        kit.append(P["verdicts"][k])
    kit.append("the honest parent scope is quoted and preserved: "
               "no record-blind, fixed-alpha, affine-equivariant kernel "
               "preserves the delivered three-step walk statistics.")
    kit.append("this census answers the general question the ninth "
               "review left open: the emptiness GENERALIZES -- no local, "
               "record-dependent, truly covariant kernel K(e|c,G,R) "
               "preserves the delivered walk statistics at the "
               "three-step window, at any declared proximity arm, at any "
               "first-step line weight, and not even at the global "
               "record reading")
    kit.append("the trigger semantics P(c,e|X) = q(c|X) K(e|c,G,R) is an "
               "ADOPTED CANDIDATE bridge, not a theorem; what is proven "
               "is that q(c) is the probability of paper-20's mutually "
               "exclusive CELL-HIT alternatives; this census REJECTS the "
               "candidate in its locally covariant record-dependent "
               "class at the committed windows")
    kit.append("even a SCOUTK-NONVACUOUS or SCOUTK-UNIQUE outcome would "
               "have closed EVENT SELECTION ONLY: quantum transport onto "
               "created cells remains an independent missing law")
    kit.append("the first-event boundary: the completely symmetric "
               "initial state cannot use an unwritten record to select "
               "the first event; step 1 collapses to 2 orbit variables "
               "(dim 1), and the measured family realizes only the "
               "symmetric stochastic tie-break -- a declared initial "
               "asymmetry or an extra tie-breaking state variable lies "
               "outside K(e|c,G,R) and is priced as a new declaration")
    kit.append("one uniform Farkas certificate per system closes the "
               "whole segment: y.A(a) is affine in the first-step line "
               "weight, both endpoint checks verify, and y.b = 1, so "
               "emptiness holds at EVERY a in [0,1]")
    kit.append("the mechanism witness: at a = 0 the branch rows (0,5,14) "
               "and (1,11,21) carry identical covariant coefficient "
               "vectors while the delivered walk assigns 16/729 against "
               "64/729 -- covariance identifies what the anchored start "
               "state distinguishes; the witness is the FIRST clash in "
               "canonical row order -- canonical, not curated")
    kit.append("the branchwise lemma is stronger than the mixture "
               "refusal: even conditioning on each written first triple "
               "separately, no covariant second-invocation kernel "
               "matches the delivered third-step profiles")
    kit.append("the 288 pure kernels the parent counted survive "
               "pointwise and are now priced: none is realizable by any "
               "covariant assignment, so every survivor breaks "
               "relabelling symmetry")
    kit.append("proximity was a declared fork, and the fork closed by "
               "measurement: shared-actor and record-distance induce the "
               "same orbit partition, metric-count coincides with the "
               "global reading at this arena, and the three distinct "
               "partitions stand in the measured refinement order -- "
               "the global partition refines the causal-neighborhood "
               "partition, which refines the shared-actor partition, "
               "both refinements strict -- so causal-neighborhood sits "
               "strictly between, and all three distinct systems are "
               "empty")
    kit.append("locality is not the obstruction: the global reference "
               "family (25 orbit variables, no locality leg) is empty by "
               "the same certificates")
    kit.append(KIT_GFIXED)
    kit.append(KIT_MODE)
    kit.append(KIT_PRECISE)
    kit.append(KIT_ERASURE)
    kit.append(KIT_CAPS)
    for (t, d) in TERM_TABLE:
        kit.append("| " + t + " | " + d + " |")
    P["kit"] = kit


# ===========================================================================
# SECTION 12.  FALSIFIER REGISTRY + SOURCE HYGIENE
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
    ("MUT-REACH", "G-REACH", "reach", "duplicates a raw tuple"),
    ("MUT-COINC", "G-COINCIDE", "coincidence",
     "flips a partition coincidence"),
    ("MUT-STEP1", "G-STEP1", "step1", "inflates the step-1 orbit count"),
    ("MUT-D2", "G-D2", "d2", "forges the depth-2 polytope dimension"),
    ("MUT-CTX", "G-WELLDEF", "d3_welldef",
     "poisons the orbit bookkeeping self-check"),
    ("MUT-SAMPLE", "G-D3-SAMPLES", "d3", "forges a sample status"),
    ("MUT-CERT", "G-D3-FARKAS", "d3", "corrupts a Farkas certificate"),
    ("MUT-BW", "G-D3-BW", "d3", "forges the branchwise status"),
    ("MUT-UNIF", "G-D3-UNIFORM", "d3",
     "corrupts the uniform certificate"),
    ("MUT-IDENT", "G-D3-IDENT", "d3_identified",
     "forges an identified-system status"),
    ("MUT-CLASH", "G-CLASH", "clash", "suppresses the clash witness"),
    ("MUT-POLY", "G-SUBFAM", "subfamily",
     "deletes the linear polynomial rows"),
    ("MUT-COMPAT", "G-PURE", "pure", "flips a compat entry"),
    ("MUT-CTRL", "G-CONTROLS", "controls",
     "forges the forced-empty status"),
    ("MUT-SS", "G-SAMPLE-SPACE", "sample_spaces",
     "strips a sample-space declaration"),
    ("MUT-NUMBIND", "G-NUM-BIND", "numeral_bindings",
     "corrupts a numeral binding resolution"),
    ("MUT-SETITER", "G-AST-DETERMINISM", "source_hygiene",
     "injects a bare set-iteration and a raw os.listdir into the "
     "scanned source (the registered iteration-order species, I9); "
     "must die deterministically at every hash seed, never vary "
     "silently"),
    ("MUT-CAPS", "G-CAPS-REGISTER", "caps_register",
     "injects an engaged CAP row kind into the caps register (the "
     "no-caps sentence's falsifier, F6)"),
    ("MUT-KWALL", "G-KERNEL-WALL", "kernel_wall",
     "blanks the kernel-scope wall's pattern family so the retired "
     "overclaim's permanent dead plants stop dying (the verifier's "
     "hyphen-fused replants, finding F2)"),
    ("MUT-NUMTOT", "G-NUM-TOTALITY", "numeral_totality_controls",
     "disables the NON-CLAIM reason classes so the alive control's "
     "classified numerals go unclassified (the per-occurrence "
     "totality's falsifier, F3)"),
    ("MUT-ADDENDUM", "G-ADDENDUM-68", "addendum_68",
     "corrupts the required consistency-mode suffix so the verdict "
     "words no longer name the #68 addendum's frozen mode (F1)"),
    ("MUT-ENV", "G-ENV-EXCLUSION", "env_exclusion",
     "injects an unpinned live-read digest into the receipt payload "
     "(the #59 disease species, I8)"),
)


# The MUT-SETITER falsifier's injection: appended to the SCANNED source
# only (never executed, never written) so the determinism leg below has
# a registered mutant that must die at G-AST-DETERMINISM at every hash
# seed rather than varying silently.
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
    # ---- the determinism leg (M3; the scout #78 / ARITY-16 Z10 port;
    # the I9 seed-variance species) ----------------------------------
    # Iteration order must never depend on the process hash seed: every
    # collection this instrument iterates can reach the sealed
    # artifacts through the double build, so bare iteration over a set
    # display, a set comprehension or a set()/frozenset() call, and any
    # os.listdir call not wrapped directly in sorted(), are refused at
    # the source.  The scan is syntactic (AST), so the refusal is
    # deterministic -- the same verdict at every PYTHONHASHSEED --
    # complementing the battery's cross-seed regeneration leg in-run.
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
            "the determinism leg: the instrument's own syntax tree "
            "carries no bare iteration over a set display, set "
            "comprehension or set()/frozenset() call and no os.listdir "
            "call outside a direct sorted() wrapper -- every collection "
            "iterated here feeds the sealed artifacts through the "
            "double build, so unsorted iteration is refused at the "
            "source, deterministically at every hash seed",
            {"set_iteration_lines": sorted(set_iter),
             "raw_listdir_lines": sorted(raw_listdir)})


# ===========================================================================
# SECTION 12b.  THE MICRO-REPAIR GATES (M1-M5)
# ===========================================================================
# ---- the kernel-scope wall (M2; the scout #78 port; verifier finding
# F2) --------------------------------------------------------------------
# The RETIRED overclaim -- the general "no equivariant record-consistent
# kernel" verdict, downgraded at #59 to the record-blind fixed-alpha
# scope -- survived replanting in hyphen-fused and fresh-worded forms
# (verifier plants P5 and P1).  This wall is SUBJECT-BASED: hyphens and
# spacing are normalized away, the note is split into segments, and any
# segment whose subject is the equivariant / record-consistent kernel
# family carrying a nonexistence or emptiness predicate is refused --
# UNLESS the segment carries the licensed record-blind scope qualifier,
# so the honest downgraded verdict (the twin) stays alive.  This unit's
# own covariant verdict names a DIFFERENT subject (the local,
# record-dependent, truly covariant kernel class) and stays alive
# untouched.
KERNEL_WALL_TOKENS = (
    "scout kernel empty at equivariant record consistent",
)
KERNEL_WALL_SUBJECTS = (
    "equivariant record consistent kernel",
    "record consistent kernel",
    "equivariant kernel",
)
KERNEL_WALL_NEG_EXISTENTIALS = tuple(
    "no " + s for s in KERNEL_WALL_SUBJECTS)
KERNEL_WALL_PREDICATES = (
    "does not exist", "do not exist", "cannot exist", "never exists",
    "none exists", "none exist", "is empty", "are empty",
    "is impossible", "are impossible", "is ruled out", "are ruled out",
)
KERNEL_WALL_LICENCE = "record blind"
# Permanent controls, exercised on every build by G-KERNEL-WALL: the
# verbatim retired sentence, two paraphrase variants, the retired
# verdict token, the verifier's surviving hyphen-fused replant (P5) and
# the fresh-worded family nonexistence (P1) must DIE at this wall; the
# licensed record-blind forms and this unit's own covariant verdict
# sentence are the twins and must SURVIVE.
KERNEL_WALL_DEAD_CONTROLS = (
    "So no equivariant record-consistent kernel exists at the "
    "committed arena.",
    "every equivariant kernel is empty at the committed arena",
    "record consistent kernels do not exist at this arena",
    "SCOUT-KERNEL-EMPTY-AT-EQUIVARIANT-RECORD-CONSISTENT",
    "no-equivariant-record-consistent-kernel-exists",
    "no equivariant kernel of any kind survives",
)
KERNEL_WALL_ALIVE_CONTROLS = (
    "no record-blind, fixed-alpha, affine-equivariant kernel preserves "
    "the delivered three-step walk statistics",
    "at the three-step window only the 288 pure non-line kernels among "
    "the censused deterministic kernels preserve it and no "
    "record-blind fixed-alpha equivariant kernel does",
    "no local, record-dependent, truly covariant kernel K(e|c,G,R) "
    "preserves the delivered walk statistics at the three-step window",
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
            if KERNEL_WALL_LICENCE in s:
                continue
            if any(p in s for p in negs) \
                    or (any(p in s for p in subjects)
                        and any(p in s for p in KERNEL_WALL_PREDICATES)):
                hits.append("retired kernel-scope claim: "
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
        "policy": "the retired kernel-scope overclaim family is "
                  "refused subject-based (normalized against hyphen "
                  "and spacing evasion) wherever the licensed "
                  "record-blind scope qualifier is absent; the "
                  "verbatim retired sentence, the paraphrases, the "
                  "retired verdict token and the hyphen-fused replant "
                  "are permanent dead plants, and the licensed "
                  "downgraded forms plus this unit's own covariant "
                  "verdict are permanent alive twins"}
    LD.gate("G-KERNEL-WALL", ok,
            "the kernel-scope wall fires on the retired overclaim "
            "family (verbatim, hyphen-fused, paraphrase variants, and "
            "the retired verdict token) and stays silent on the "
            "licensed record-blind forms and on this unit's own "
            "covariant verdict; all permanent controls behave as "
            "declared on this build",
            {"dead_controls": len(KERNEL_WALL_DEAD_CONTROLS),
             "alive_controls": len(KERNEL_WALL_ALIVE_CONTROLS),
             "misbehaving": [r["control"][:50] for r in rows
                             if (r["expected"] == "DEAD")
                             != r["flagged"]]})


# ---- the per-occurrence numeral totality (M4; the #68 addendum item 5;
# verifier finding F3) ---------------------------------------------------
# Every integer numeral occurrence in the note is classified BOUND (a
# specific receipt field) or NON-CLAIM (a declared reason class); the
# blanket whitelist (range 0..sixty plus hard-coded constants) is
# RETIRED.  Totality is enforced at note verification (any unclassified
# occurrence refuses delivery) and the full per-occurrence table is
# serialized in the receipt; the in-run controls below keep a registry
# falsifier on the mechanism itself.
NONCLAIM_SEEDS = (0, 1, 424242)


def numeral_paths(P):
    paths = {}

    def note_tok(s, path):
        for tok in s.replace("/", " ").replace(",", " ").split():
            neg = tok.lstrip("-")
            if neg.isascii() and neg.isdigit():
                paths.setdefault(int(neg), path)

    def walk(obj, path):
        if isinstance(obj, bool):
            return
        if isinstance(obj, int):
            paths.setdefault(obj, path)
            return
        if isinstance(obj, str):
            note_tok(obj, path)
            return
        if isinstance(obj, dict):
            for k in sorted(obj):
                np = (path + "/" + str(k)) if path else str(k)
                note_tok(str(k), np)
                walk(obj[k], np)
            return
        if isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                walk(v, path + "[%d]" % i)
    walk(fser(P), "")
    return paths


def classify_numeral(line, raw, v, nums, table_map, num_paths,
                     nonclaim_on):
    if raw.startswith("#"):
        if nonclaim_on:
            return ("NON-CLAIM", "LEDGER-REFERENCE")
        return (None, None)
    if str(v) in table_map:
        return ("BOUND", table_map[str(v)])
    if v in nums:
        return ("BOUND", num_paths.get(v, "receipt-inventory"))
    if nonclaim_on and "PYTHONHASHSEED" in line and v in NONCLAIM_SEEDS:
        return ("NON-CLAIM", "DECLARED-BATTERY-SEED")
    return (None, None)


def numeral_sweep(text, nums, table_map, num_paths, nonclaim_on):
    rows = []
    for lni, ln in enumerate(text.splitlines(), 1):
        for tok in ln.replace("(", " ").replace(")", " ").split():
            raw = tok.strip(".,;:|%")
            t = raw.lstrip("#")
            if not (t.isascii() and t.isdigit()):
                continue
            cls, detail = classify_numeral(ln, raw, int(t), nums,
                                           table_map, num_paths,
                                           nonclaim_on)
            rows.append({"line": lni, "token": t,
                         "class": cls if cls else "UNCLASSIFIED",
                         "binding": detail if detail else "NONE"})
    return rows


NUMTOT_DEAD_CONTROL = ("the census would have found 4242424271 kernels "
                       "had the arena been larger")
NUMTOT_ALIVE_CONTROL = ("unit pinned at v15 ledger #60, regenerated "
                        "under PYTHONHASHSEED 424242")


def table_map_of(P):
    tm = {}
    for r in P["numeral_bindings"]:
        tm.setdefault(r["numeral"], r["receipt_field"])
    return tm


def numeral_totality_controls(LD, P):
    nonclaim_on = pick("MUT-NUMTOT", True, False)
    nums, num_paths = totality_inventory(P)
    tm = table_map_of(P)
    dead = numeral_sweep(NUMTOT_DEAD_CONTROL, nums, tm, num_paths,
                         nonclaim_on)
    alive = numeral_sweep(NUMTOT_ALIVE_CONTROL, nums, tm, num_paths,
                          nonclaim_on)
    dead_flagged = any(r["class"] == "UNCLASSIFIED" for r in dead)
    alive_clean = bool(alive) and all(r["class"] != "UNCLASSIFIED"
                                      for r in alive)
    P["numeral_totality_controls"] = {
        "dead_control": dead, "alive_control": alive,
        "policy": "every numeral occurrence in the note is classified "
                  "BOUND (a specific receipt field) or NON-CLAIM (a "
                  "declared reason class: LEDGER-REFERENCE, "
                  "DECLARED-BATTERY-SEED); the blanket whitelist is "
                  "retired; totality is enforced at note verification "
                  "and the full per-occurrence table is serialized in "
                  "the receipt; the mechanism's own control subtrees "
                  "are excluded from the inventory, so the dead "
                  "control's invented numeral cannot self-whitelist"}
    LD.gate("G-NUM-TOTALITY", dead_flagged and alive_clean,
            "the numeral-totality mechanism behaves as declared on its "
            "permanent controls: an unbacked invented numeral goes "
            "UNCLASSIFIED (and would refuse delivery at note "
            "verification), while ledger references and the declared "
            "battery seed classify NON-CLAIM with their reason classes",
            {"dead_flagged": dead_flagged, "alive_clean": alive_clean})


# ---- the #68 addendum consumption gate (M1; verifier finding F1) -------
def addendum_gate(LD, P):
    gates_so_far = [r["gate"] for r in LD.rows]
    dig_ok = (P["read_set"].get(ADDENDUM_REL) == ADDENDUM_DIG
              and PINNED[ADDENDUM_REL] == ADDENDUM_DIG)
    suffix = pick("MUT-ADDENDUM", "-AT-CONDITIONAL-CONSISTENCY",
                  "-AT-CONDITIONAL-CONSISTENCY-CORRUPTED")
    head = P["verdicts"]["D3"].split("<")[0]
    toks = [t.strip() for t in head.split(";")]
    mode_named = (len(toks) == 4
                  and all(t.endswith(suffix) for t in toks))
    affine_ok = all(P["d3"][lbl]["uniform_certificate"]
                    .get("affine_midpoint_ok") for lbl in P["d3"])
    relax_ok = "adds pin rows" in P["d3_identified"]["relaxation_lemma"]
    item1 = mode_named and affine_ok and relax_ok
    arms = P["arms"]
    d3_idx = [i for i, g in enumerate(gates_so_far)
              if g.startswith("G-D3")]
    item2 = (all(arms[an]["covariant"] and arms[an]["declaration"]
                 for an in ARM_ORDER)
             and "G-ARMS-COVARIANT" in gates_so_far and bool(d3_idx)
             and gates_so_far.index("G-ARMS-COVARIANT") < min(d3_idx))
    tri = P["step1"]["tie_break_trilemma"]
    item3 = (P["step1"]["orbit_variables"] == 2
             and "G-STEP1" in gates_so_far
             and set(tri) == {"a_symmetric_stochastic_initial_kernel",
                              "b_declared_initial_asymmetry",
                              "c_another_tie_breaking_state_variable"}
             and "depth3" in P["reach"])
    item4 = (KIT_GFIXED in P["kit"]
             and any("EVENT SELECTION ONLY" in s for s in P["kit"]))
    item5 = "G-NUM-TOTALITY" in gates_so_far
    P["addendum_68"] = {
        "addendum": ADDENDUM_REL,
        "digest": ADDENDUM_DIG,
        "consistency_mode":
            "CONDITIONAL (the frozen PRIMARY): transition agreement at "
            "every reached state; each constraint linear in exactly "
            "one kernel factor; LP/Farkas valid; no bilinear system "
            "solved; no outcome-bearing history-flow relaxation (the "
            "one relaxation used runs in the conservative emptiness "
            "direction with pinned confirmations); the SECONDARY "
            "(marginal-history agreement) was not attempted here -- it "
            "is SCOUT-T's fork arm",
        "verification_record": {
            "rebuild": VERIFY_REBUILD_REL,
            "check_ledger": VERIFY_LEDGER_REL,
            "binding": "the hostile verifier's independent rebuild, "
                       "archived at v15 ledger #82 and read at its "
                       "pinned digests (G-PIN-DIGESTS)"},
        "checks": {
            "digest_pinned": dig_ok,
            "item1_mode_named_in_verdict_words": mode_named,
            "item1_linear_in_one_factor_evidence": affine_ok,
            "item1_relaxation_conservative_direction": relax_ok,
            "item2_predicates_preregistered_and_covariant": item2,
            "item3_first_event_requirements": item3,
            "item4_scope_wall_gated_kit_sentence": item4,
            "item5_numeral_totality_gated": item5}}
    LD.gate("G-ADDENDUM-68",
            dig_ok and item1 and item2 and item3 and item4 and item5,
            "the #68 pin addendum is cited by digest and CONSUMED: the "
            "frozen CONDITIONAL mode is what ran (each constraint "
            "linear in one kernel factor, the relaxation "
            "emptiness-direction only) and the D3 verdict names it in "
            "its words; the proximity predicates are pre-registered, "
            "declared in committed objects, and gated covariant BEFORE "
            "any feasibility gate; the step-1 census is published "
            "separately with the tie-break trilemma; the G-fixed scope "
            "wall is a gated kit sentence; the numeral totality is "
            "gated",
            P["addendum_68"]["checks"])


# ---- the environment-exclusion gate (M3; the I8 species) ---------------
def env_exclusion(LD, P):
    """no environment-dependent value may enter the serialized receipt:
    the sha256-12 of every unpinned live read is computed in-run and
    must not occur anywhere in the receipt payload (the parent's
    delivered receipt's defect: it serialized the live LOG digest, so a
    one-line LOG append moved the receipt)."""
    unp = sorted({rel for (_i, rel, _q) in ANCHORS} - set(PINNED))
    digs = {}
    for rel in unp:
        digs[rel] = sha12(read_rel(rel))
    P["env_exclusion"] = {
        "unpinned_reads_scanned": unp,
        "probe": pick("MUT-ENV", None, digs[unp[-1]]),
        "policy": "unpinned live-read digests (the append-only LOG and "
                  "the anchor-only paper sources) are computed in-run "
                  "for this exclusion check only and are never "
                  "serialized into either artifact; the receipt is "
                  "therefore LOG-append-independent by construction"}
    blob = to_json(P) + to_json(LD.rows)
    leaks = sorted(rel for rel, d in digs.items() if d in blob)
    P["env_exclusion"]["leaks"] = leaks
    LD.gate("G-ENV-EXCLUSION", not leaks,
            "the serialized receipt payload carries no digest of any "
            "unpinned live read: environment-dependent bytes are "
            "excluded from the artifacts and checked in-run only, so "
            "the LOG-append regeneration probe is provably closed at "
            "the receipt",
            {"scanned": len(unp), "leaks": leaks})


# ===========================================================================
# SECTION 13.  THE FULL BUILD
# ===========================================================================
def build_all(P=None):
    LD = Ledger()
    if P is None:
        P = {}
    CAPS["counter"] = Counter()
    source_scan(LD, P)
    P["regime"] = {
        "gates_in_ledger": 30,
        "falsifiers_registered": len(FALSIFIERS),
        "policy": "declared up front; note verification refuses "
                  "delivery if these counts drift from the live ledger "
                  "and registry"}
    measure_reads(LD, P)
    measure_arena(LD, P)
    GCELL, GTRI = build_gamma(LD, P)
    psi1, q1, sup1, q2, sup2, BOC, E1S = build_walk(LD, P)
    measure_arms(LD, P, GCELL, GTRI, E1S)
    canon_tuple, canon_ctx = make_canon(GCELL, GTRI)
    RAW = reach_census(LD, P, canon_tuple, canon_ctx, sup1, sup2, BOC, E1S)
    step1_census(LD, P, canon_tuple, sup1, BOC)
    depth2_system(LD, P, psi1, q2, sup1, BOC)
    q3_of = make_q3(psi1)
    out3 = depth3_systems(LD, P, canon_tuple, canon_ctx, q3_of, sup1,
                          sup2, BOC, E1S, RAW)
    depth3_identified(LD, P, out3)
    clash_witness(LD, P, out3)
    subfamily(LD, P, out3, q3_of, sup1, sup2, BOC)
    controls(LD, P, canon_tuple, canon_ctx, q3_of, sup1, sup2, BOC, E1S,
             RAW)
    caps_register_gate(LD, P)
    build_verdicts(P)
    sample_space_audit(LD, P)
    numeral_bindings(LD, P)
    build_kit(P)
    kernel_wall_gate(LD, P)
    numeral_totality_controls(LD, P)
    addendum_gate(LD, P)
    env_exclusion(LD, P)
    P["ledger"] = LD.rows
    return P


# ===========================================================================
# SECTION 14.  NOTE VERIFICATION (the walls on the report's own prose)
# ===========================================================================
FORBIDDEN_GLOBAL = (
    "no equivariant record-consistent kernel exists",
    "scout-kernel-empty-at-equivariant-record-consistent",
    "no reader will", "no one will doubt", "will not doubt",
    "probably", "likely", "explains why",
    "the trigger mechanism is established",
    "establishes the trigger", "proves the trigger",
    "trigger is a theorem",
)
REQUIRED_SENTENCES = (
    "no record-blind, fixed-alpha, affine-equivariant kernel preserves "
    "the delivered three-step walk statistics.",
)


def totality_inventory(P):
    """The numeral inventory the note sweep classifies against.  The
    totality mechanism's OWN subtrees are excluded: the permanent dead
    control's invented numeral is serialized inside
    numeral_totality_controls, and leaving it in the inventory would
    self-whitelist exactly the numeral the control exists to refuse
    (found by this unit's own battery; the F3 residual class)."""
    Pv = {k: v for k, v in P.items()
          if k not in ("numeral_totality_controls", "numeral_totality")}
    nums = set()
    collect_numerals(fser(Pv), nums)
    return nums, numeral_paths(Pv)


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
        if aid in ("A-PARENT-GATE-729", "A-PARENT-GATE-288",
                   "A-PARENT-3STEP"):
            continue
        if canon_text(quote) not in hay:
            problems.append("anchor quote missing from note: " + aid)
    for pat in FORBIDDEN_GLOBAL:
        if pat in low:
            problems.append("forbidden pattern present: " + pat)
    for h in kernel_wall_hits(text):
        problems.append("kernel-scope wall: " + h)
    if P.get("regime", {}).get("gates_in_ledger") != len(P["ledger"]) \
            or P.get("regime", {}).get("falsifiers_registered") \
            != len(FALSIFIERS):
        problems.append("regime counts stale against the live ledger "
                        "and falsifier registry")
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
    # the numeral-binding table must appear in the note with rows equal
    # to the receipt's binding registry
    for r in P["numeral_bindings"]:
        want = "| %s | %s |" % (r["numeral"], r["receipt_field"])
        if want not in text:
            problems.append("numeral-binding row missing: " + want)
    inv = set()
    rationals_of(fser(P), inv)
    for ln in text.splitlines():
        for t in sorted(iter_rationals(ln)):
            if t not in inv:
                problems.append("slash rational not in receipt "
                                "inventory: " + t)
    # M4: the per-occurrence numeral totality (the #68 addendum item 5).
    # The former blanket whitelist is RETIRED: every integer numeral
    # occurrence is classified BOUND (a specific receipt field) or
    # NON-CLAIM (a declared reason class), any unclassified occurrence
    # refuses delivery, and the full table is serialized in the receipt.
    nums, num_paths = totality_inventory(P)
    tm = table_map_of(P)
    tot_rows = numeral_sweep(text, nums, tm, num_paths, True)
    for r in tot_rows:
        if r["class"] == "UNCLASSIFIED":
            problems.append("numeral unclassified (neither BOUND to a "
                            "receipt field nor NON-CLAIM): " + r["token"]
                            + " at note line %d" % r["line"])
    P["numeral_totality"] = {
        "occurrences": len(tot_rows),
        "bound": sum(1 for r in tot_rows if r["class"] == "BOUND"),
        "non_claim": sum(1 for r in tot_rows
                         if r["class"] == "NON-CLAIM"),
        "unclassified": sum(1 for r in tot_rows
                            if r["class"] == "UNCLASSIFIED"),
        "reason_classes": sorted({r["binding"] for r in tot_rows
                                  if r["class"] == "NON-CLAIM"}),
        "rows": tot_rows,
        "policy": "per-occurrence total classification; the binding "
                  "table is the BOUND core; the blanket whitelist is "
                  "retired"}
    return problems


# ===========================================================================
# SECTION 15.  ARTIFACTS, CLI, SELFTEST
# ===========================================================================
def render_output(P, note_digest):
    lines = []
    lines.append("SCOUT-K delivery transcript")
    lines.append("pin a1a6ccc61bd4 (v15 ledger #60) + the #64 addendum "
                 "+ the #68 addendum 3a1e5a649537 (consumed at "
                 "G-ADDENDUM-68); unit note " + NOTE_REL)
    lines.append("object under test (the note): sha256-12 " + note_digest)
    lines.append("instrument source: sha256-12 "
                 + P["source_hygiene"]["digest"])
    lines.append("parent apparatus: delivered scout_exact.py edb60bccd22e "
                 "via byte-verified snapshot (live file mid-repair)")
    lines.append("")
    for r in P["ledger"]:
        lines.append("GATE %-18s %s  %s"
                     % (r["gate"], "PASS" if r["ok"] else "FAIL",
                        r["note"]))
    lines.append("")
    lines.append("VERDICTS")
    for k in ("REACH", "D2", "D3", "SUBFAMILY", "BRIDGE"):
        lines.append("  " + P["verdicts"][k])
    lines.append("")
    lines.append("KEY CLAIMS")
    lines.append("  reach census: 63 contexts / 189 tuples / 7 first "
                 "events; orbit variables SA 16, RD 16, MC 25, CN 19, "
                 "GLOBAL 25 (vs the fixed-alpha family's 1)")
    lines.append("  step-1 census (the first-event boundary): 2 orbit "
                 "variables, dim 1; only the symmetric stochastic "
                 "tie-break is realizable")
    lines.append("  depth 2: nonvacuous, dim 1, all arms coincide at the "
                 "zero record")
    lines.append("  depth 3: EMPTY at all arms and at the global "
                 "reference, at all 6 sampled line weights, branchwise, "
                 "and uniformly in a by one small Farkas certificate per "
                 "system (supports 6, 6, 7)")
    lines.append("  mechanism: branch rows (0,5,14) and (1,11,21) are "
                 "the same covariant combination; the walk gives 16/729 "
                 "vs 64/729")
    lines.append("  fixed-alpha subfamily: 729 rows, 25 polys, linear "
                 "roots -1, 0, +1 (reproduces #58); pure census 8 -> 288 "
                 "reproduced and priced")
    lines.append("  consistency mode: CONDITIONAL (the #68 addendum's "
                 "frozen PRIMARY), named in the D3 verdict words")
    lines.append("  M6 strengthenings re-derived in-run: arm covariance "
                 "at 108 x 8, refinement order GLOBAL -> CN -> SA(=RD), "
                 "canonical-first clash")
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
    note_path = os.path.join(ROOT, NOTE_REL)
    if not os.path.exists(note_path):
        raise GateFail("G-NOTE-PRESENT", "the unit note is absent")
    note_bytes = read_rel(NOTE_REL)
    problems = verify_note(P1, note_bytes, [])
    if problems:
        raise GateFail("G-NOTE-KIT", "; ".join(problems[:8]))
    nd = sha12(note_bytes)
    P1["object_under_test"] = {"path": NOTE_REL, "sha256_12": nd}
    P1["falsifiers"] = [{"name": n, "gate": g, "object": o,
                         "description": d} for (n, g, o, d) in FALSIFIERS]
    P1["schema"] = "scoutk-receipt-v1"
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


USAGE = ("usage: scoutk_exact.py [--no-write | --numbers | --kit | "
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
                          "G-D2", "G-STEP1", "G-D3-UNIFORM", "G-D3-BW",
                          "G-D3-IDENT", "G-WELLDEF", "G-LP-SOLVE"})
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
        for k in ("REACH", "D2", "D3", "SUBFAMILY", "BRIDGE"):
            sys.stdout.write(P["verdicts"][k] + "\n")
        sys.stdout.write(to_json(
            {"orbit_vars": {an: P["reach"]["depth3"][an]
                            ["tuple_orbit_variables"]
                            for an in ARM_ORDER},
             "d3_gaps": {lbl: [str(r["gap"]) for r in
                               P["d3"][lbl]["samples"]]
                         for lbl in P["d3"]}}) + "\n")
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
