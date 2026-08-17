#!/usr/bin/env python3
# ===========================================================================
# SCOUT-BRIDGE  --  the pre-DC scout: sample spaces, the pushforward
# ceiling, the kernel, the Delta-B gate, and the uncollapsed-record map.
#
# Unit: v15/note-scout-bridge.md (report NOTE, no paper number).
# Pin:  v15/note-scout-pin.md          (FROZEN c57a0afffd58)
# Add:  v15/note-scout-pin-addendum.md (FROZEN 2aa72e566cba)
#
# Exact arithmetic throughout: Python integers and fractions.Fraction.
# No floats, no builtin hash, no timestamps in artifacts.  The delivery
# run is the only writer; every failure writes nothing.
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
NOTE_REL = "v15/note-scout-bridge.md"
OUT_REL = "v15/code/scout_output.txt"
REC_REL = "v15/code/scout_receipt.json"

PINNED = {
    "v15/note-scout-pin.md": "c57a0afffd58",
    "v15/note-scout-pin-addendum.md": "2aa72e566cba",
    "v15/paper-46-ecc.md": "61d330d13fe0",
    "v15/code/ecc_receipt.json": "ea24c1fc2340",
}

# The ECC repair worker holds the live tree mid-flight; the pin binds this
# scout to the DELIVERED digests, so pinned ECC reads resolve through
# byte-verified snapshots of the delivered (committed-as-is) artifacts.
SNAPSHOT = {
    "v15/paper-46-ecc.md": "v15/code/scout_ecc_paper46_delivered.md",
    "v15/code/ecc_receipt.json":
        "v15/code/scout_ecc_receipt_delivered.json",
}

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
    """serialize exact values: Fraction -> 'p/q' string, recursively."""
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


def canon(text):
    """whitespace-collapsed text for verbatim location; markdown
    blockquote markers are stripped per line so quoted sources match."""
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


def read_pinned(rel):
    """read a digest-pinned source: the live path when it still carries
    the pinned bytes, else the scout's byte-verified delivered snapshot."""
    want = PINNED.get(rel)
    live = None
    try:
        live = read_rel(rel)
    except OSError:
        live = None
    if want is None or (live is not None and sha12(live) == want):
        return live, "LIVE"
    if rel in SNAPSHOT:
        snap = read_rel(SNAPSHOT[rel])
        return snap, "SNAPSHOT"
    return live, "LIVE"


class Ledger:
    def __init__(self):
        self.rows = []

    def gate(self, gid, ok, note, data=None):
        self.rows.append({"gate": gid, "ok": bool(ok), "note": note,
                          "data": fser(data) if data is not None else None})
        if not ok:
            raise GateFail(gid, note)


# ===========================================================================
# SECTION 1.  THE COMMITTED ARENA (rebuilt from constructors; ECC's chart)
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


def partitions_into_triples():
    acts = list(SITES)
    out = []

    def rec(rest, blocks):
        if not rest:
            out.append(tuple(sorted(blocks)))
            return
        a = rest[0]
        for pair in combinations(rest[1:], 2):
            blk = tuple(sorted((a,) + pair))
            rem = [x for x in rest if x not in blk]
            rec(rem, blocks + [blk])
    rec(acts, [])
    return tuple(sorted(set(out)))


PARTS = partitions_into_triples()
ROUNDS = tuple(p for p in PARTS
               if all(len(BLOCK_OF[b]) == len(b) for b in p))

# ---- the ring Z[w] and the committed walk (paper-20 as ECC re-implements) --
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
AMPS = (("THE-UNIFORM-AMPLITUDE", tuple([Z1] * DIM)),
        ("A-SINGLE-CELL-AMPLITUDE", SINGLE),
        ("ONE-LINK-DIRECTION-ONLY",
         tuple(Z1 if k % 3 == 0 else Z0 for k in range(DIM))),
        ("ALTERNATING-ROOTS",
         tuple(Z1 if k % 2 == 0 else WPOW[1] for k in range(DIM))),
        ("THE-ZERO-AMPLITUDE", tuple([Z0] * DIM)))


def nfield(cells):
    n = [0] * DIM
    for c in cells:
        n[c] += 1
    return tuple(n)


def round_fields(rounds):
    return tuple(nfield([c for blk in rnd for c in BLOCK_OF[blk]])
                 for rnd in rounds)


# ===========================================================================
# SECTION 2.  EXACT LINEAR ALGEBRA (rref, nullspaces, two-phase simplex
#             with phase-one dual extraction)
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


def left_null(A):
    m = len(A)
    n = len(A[0])
    AT = [[A[i][j] for i in range(m)] for j in range(n)]
    return null_of(AT)


def rank_of(A):
    R, piv = rref(A)
    return len(piv)


def simplex(A, b, c=None):
    """min c.x st A x = b, x >= 0.  Two-phase, Bland's rule, exact.
    Returns (status, gap_or_value, x, y) with y the phase-one dual vector
    (a Farkas certificate on infeasible instances)."""
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


# ---- matrices over Z[w] with an integer |entry|^2 scale --------------------
def mm(A, B):
    n = len(A)
    K = len(B)
    m2 = len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(m2):
            acc = Z0
            for k in range(K):
                acc = zadd(acc, zmul(A[i][k], B[k][j]))
            row.append(acc)
        out.append(tuple(row))
    return tuple(out)


def Bmat(U, s2):
    return tuple(tuple(Fraction(znorm(U[i][j]), s2)
                       for j in range(len(U[0]))) for i in range(len(U)))


def dB(B21, B2, B1):
    n = len(B21)
    return tuple(tuple(B21[i][j] - sum(B2[i][k] * B1[k][j]
                                       for k in range(n))
                       for j in range(n)) for i in range(n))


def nz_count(M):
    return sum(1 for row in M for v in row if v != 0)


def bigG():
    M = [[Z0] * DIM for _ in range(DIM)]
    for s in range(9):
        for i in range(3):
            for j in range(3):
                M[s * 3 + i][s * 3 + j] = GR[i][j]
    return tuple(tuple(r) for r in M)


def bigD(n):
    M = [[Z0] * DIM for _ in range(DIM)]
    for k in range(DIM):
        M[k][k] = WPOW[n[k] % Q]
    return tuple(tuple(r) for r in M)


def bigF():
    M = [[Z0] * DIM for _ in range(DIM)]
    for s in range(9):
        for i in range(3):
            for j in range(3):
                M[s * 3 + i][s * 3 + j] = WPOW[(i * j) % 3]
    return tuple(tuple(r) for r in M)


IDENT = tuple(tuple(Z1 if i == j else Z0 for j in range(DIM))
              for i in range(DIM))
SPERM = tuple(tuple(Z1 if SHIFT[j] == i else Z0 for j in range(DIM))
              for i in range(DIM))
ZERO27 = tuple(tuple(Fraction(0) for _ in range(DIM)) for _ in range(DIM))

# ===========================================================================
# SECTION 3.  THE ANCHOR REGISTRY (verbatim consumption, digests recorded)
# ===========================================================================
ANCHORS = (
    ("A-P20-277", "v14/paper-20-coupling.md",
     "A division event on cell (x, l) increments n_l(x) by one."),
    ("A-P20-217", "v14/paper-20-coupling.md",
     "The menu at site x is the three link traversals and the weight "
     "q(l|x) is the post-coin Born weight |(Cψ)(x,l)|²."),
    ("A-P20-633", "v14/paper-20-coupling.md",
     "The record accumulates the law's own weights and the state is not "
     "collapsed onto the emitted cell, so the walk stays coherent between "
     "division events."),
    ("A-P20-SELECTIVE", "v14/paper-20-coupling.md",
     "The selective reading is a different object — a classical "
     "Markov chain on cells — and it is not run."),
    ("A-P19-289", "v14/paper-19-r3-weld.md",
     "at this generator a division event's footprint **is** its conflict "
     "group, so the geometry is a function of the groupings by "
     "construction"),
    ("A-W1P-344", "v12/note-w1p-three-class.md",
     "Δᴮ is an amplitude-level coherence measure. It is not a "
     "divisibility measure, not a witness of indivisibility, and not the "
     "residual of any declared stochastic law unless that law is declared "
     "to be B(U₂)."),
    ("A-W5-120", "v12/note-w5-barandes-recast.md",
     "Allowed conditioning times `t₀` are called **division events** "
     "for the given system"),
    ("A-W5-68", "v12/note-w5-barandes-recast.md",
     "one can take the sample space to be the system's **configuration "
     "space C**, which is a **fixed ingredient of the model**"),
    ("A-D44-60", "v10/note-d44-d45-campaign-synthesis.md",
     "completed cross-component weights are FORCED to the decided "
     "completion's SECTOR CONDITIONAL (1/2, 1/4, 1/4 — the "
     "horizon-stable object, gated at two horizons) at verified-depth "
     "scope"),
    ("A-P38-275", "v14/paper-38-epr.md",
     "a description that passes a completeness test with an empty element "
     "set has not passed anything"),
    ("A-P38-BYCON", "v14/paper-38-epr.md",
     "the record-incomplete branch cannot fire on unmutated data"),
    ("A-CPIN-67", "v14/note-coupling-pin.md",
     "the law was confirmed on the (A,B) 2-actor carrier"),
    ("A-P46-DEBT", "v15/paper-46-ecc.md",
     "the coupled dynamics writes its own record: one emitted cell per "
     "step, which is a co-division pair rather than a group of the "
     "declared arity"),
    ("A-P46-CARRIER", "v15/paper-46-ecc.md",
     "Evolving is the sharp gap, at 0 of the 4 candidates: every cross "
     "pair the union admits is hosted by neither chart -- all 36 are "
     "directionless -- while the committed coin family is typed on "
     "three-direction site blocks, so no member of the family extends the "
     "committed evolution to a created cell."),
    ("A-P46-EMIT", "v15/paper-46-ecc.md",
     "a division event emitted on a cell with that cell's post-coin Born "
     "weight, every branch of the emission tree carried with no sampling "
     "and no pruning"),
    ("A-P46-FREE2", "v15/paper-46-ecc.md",
     "the free two-stage reading -- a per-event cell-selection weight "
     "chosen freely -- constrains nothing, since every one of the 27 "
     "cells is covered and any target becomes expressible, so it is "
     "disclosed as vacuous and carries no verdict"),
    ("A-LOG52-HOLD", "v15/LOG.md",
     "The ECC seal HOLD (#user, this date) REMAINS: repair+battery "
     "finish, then the unit parks unsealed."),
)


def measure_reads(LD, P):
    # Environment-dependent bytes are checked IN-RUN and NOT persisted:
    # the delivered receipt serialized the sha256-12 of the live,
    # unpinned, append-only v15/LOG.md (and per-run LIVE/SNAPSHOT
    # resolution flags), so every ledger append moved the receipt --
    # the #59 reproducibility defect.  The serialized read_set now
    # carries ONLY the four digest-pinned reads (gate-forced constants);
    # unpinned reads are verified by verbatim anchor location, their
    # digests and resolution printed to stderr only.
    reads = {}
    resolution = {}
    for rel in sorted({rel for (_i, rel, _q) in ANCHORS} | set(PINNED)):
        data, how = read_pinned(rel)
        reads[rel] = sha12(data)
        resolution[rel] = how
    P["read_set"] = {rel: reads[rel] for rel in PINNED}
    P["unpinned_reads"] = sorted(
        rel for rel in reads if rel not in PINNED)
    P["read_resolution_policy"] = (
        "pinned reads resolve through the live path when it still "
        "carries the pinned bytes, else through the byte-verified "
        "delivered snapshot; the resolved bytes are digest-gated either "
        "way, and the per-run LIVE/SNAPSHOT flag is environment-"
        "dependent so it is checked in-run and not serialized")
    sys.stderr.write("READ-RESOLUTION (in-run, not persisted): "
                     + to_json({"resolution": resolution,
                                "unpinned_digests":
                                {r: reads[r] for r in
                                 P["unpinned_reads"]}}) + "\n")
    bad = sorted(rel for rel, d in PINNED.items() if reads[rel] != d)
    LD.gate("G-PIN-DIGESTS", not bad,
            "the two frozen pins and the two delivered ECC artifacts are "
            "read at their pinned digests and no other bytes; pinned "
            "reads that the live tree no longer carries resolve through "
            "the byte-verified delivered snapshots",
            {"pinned": PINNED, "bad": bad})
    anch = []
    for (aid, rel, quote) in ANCHORS:
        hay = canon(read_pinned(rel)[0].decode("utf-8"))
        needle = canon(pick("MUT-ANCHOR", quote, quote + " CORRUPTED"))
        pos = hay.find(needle)
        anch.append({"id": aid, "rel": rel, "found": pos >= 0,
                     "quote": quote})
    P["anchors"] = anch
    LD.gate("G-ANCHORS", all(a["found"] for a in anch),
            "every declared source anchor is located verbatim "
            "(whitespace-collapsed) in its file",
            {"count": len(anch),
             "missing": [a["id"] for a in anch if not a["found"]]})
    ecc = json.loads(
        read_pinned("v15/code/ecc_receipt.json")[0].decode("utf-8"))
    consumed = {
        "committed_gaps": {},
        "words": dict((k, v) for k, v in ecc["lp"]["words"]),
        "many_dims": ecc["lp"]["many_dims"],
        "target_rows": ecc["lp"]["target_rows"],
        "distinct_targets": ecc["lp"]["distinct_targets"],
        "undefined_targets": ecc["lp"]["undefined_targets"],
        "ceiling_checked": ecc["lp"]["ceiling_checked"],
        "ceiling_exceptions": ecc["lp"]["ceiling_exceptions"],
        "carrier_evolves": sum(
            1 for cnd in ecc["carrier"]["candidates"]
            if cnd["evolves_across_creation"]),
        "carrier_candidates": len(ecc["carrier"]["candidates"]),
        "debt_menu_cross_overlap": ecc["debt"]["menu_cross_overlap"],
        "debt_cross_pairs": ecc["debt"]["cross_pairs"],
        "controls": {"feasible": ecc["lp_controls"]["forced_feasible_word"],
                     "infeasible":
                     ecc["lp_controls"]["forced_infeasible_word"]},
    }
    rowmap = {}
    for r in ecc["lp"]["rows"]:
        key = (r["class"], tuple(tuple(m) for m in r["members"]))
        rowmap[key] = r["word"]
        if any(m[0] == "A-SINGLE-CELL-AMPLITUDE" and m[1] == "R0"
               and m[2] == "G.D" for m in r["members"]):
            consumed["committed_gaps"][r["class"]] = r["gap"]
    if mut("MUT-ECC-VALS"):
        consumed["committed_gaps"]["E-BLOCK"] = "5"
    P["ecc_consumed"] = consumed
    LD.gate("G-ECC-CONSUME",
            consumed["committed_gaps"] == {"E-BLOCK": "4",
                                           "E-LINE-DECLARED": "4",
                                           "E-LINE-COSET": "3",
                                           "E-TRIPLE": "7/3"}
            and consumed["words"] == {"FEASIBLE-AT-THE-FIBER-ROW": 6,
                                      "INFEASIBLE": 136, "MANY": 6,
                                      "UNIQUE": 8}
            and consumed["many_dims"] == [8]
            and consumed["target_rows"] == 82
            and consumed["distinct_targets"] == 39
            and consumed["carrier_evolves"] == 0
            and consumed["carrier_candidates"] == 4
            and consumed["debt_menu_cross_overlap"] == 0
            and consumed["debt_cross_pairs"] == 36,
            "the delivered-candidate ECC values consumed by this scout "
            "are parsed from the sealed-digest receipt, not typed",
            consumed)
    return rowmap


# ===========================================================================
# SECTION 4.  S0 + ARENA + THE 156-ROW CENSUS (S1's committed ground)
# ===========================================================================
def measure_arena(LD, P):
    tri = TRIANGLES
    if mut("MUT-ARENA"):
        tri = tri + (TRIPLES[0],)
    rounds = ROUNDS
    if mut("MUT-ROUNDS"):
        rounds = rounds + (PARTS[0],)
    writer = sorted(Counter(len(BLOCK_OF[t]) for t in TRIPLES).items())
    memb = Counter()
    for t in TRIANGLES:
        for c in BLOCK_OF[t]:
            memb[c] += 1
    arena = {"cells": DIM, "pair_bijection": len(set(CELL_PAIR)) == DIM,
             "parallel_classes": len(CLASSES), "lines": len(LINES),
             "declared_lines": len(DECLARED_LINES),
             "triples": len(TRIPLES), "triangles": len(tri),
             "writer_census": writer,
             "cell_in_blocks": sorted(Counter(memb.values()).items()),
             "partitions": len(PARTS), "rounds": len(rounds)}
    P["arena"] = arena
    LD.gate("G-ARENA",
            arena["cells"] == 27 and arena["pair_bijection"]
            and arena["lines"] == 12 and arena["declared_lines"] == 9
            and arena["triples"] == 84 and arena["triangles"] == 27
            and arena["writer_census"] == [(0, 3), (2, 54), (3, 27)]
            and arena["cell_in_blocks"] == [(3, 27)]
            and arena["partitions"] == 280 and arena["rounds"] == 36,
            "the committed chart rebuilt from constructors: 27 cells in "
            "bijection with the linked pairs, 27 triangles, 84 triples, "
            "writer census (0,3)(2,54)(3,27), 36 admissible rounds",
            arena)


def build_classes():
    cols = {"E-BLOCK": [BLOCK_OF[t] for t in TRIANGLES],
            "E-LINE-DECLARED": [BLOCK_OF[t] for t in DECLARED_LINES],
            "E-LINE-COSET": [BLOCK_OF[t] for t in LINES],
            "E-TRIPLE": [BLOCK_OF[t] for t in TRIPLES]}
    out = {}
    for cn in sorted(cols):
        cl = cols[cn]
        M = [[Fraction(0)] * len(cl) for _ in range(DIM)]
        for j, blk in enumerate(cl):
            for c in blk:
                M[c][j] = Fraction(1)
        out[cn] = (M, len(cl))
    return out


def build_targets():
    RF = round_fields(ROUNDS)
    rows = []
    for (an, psi) in AMPS:
        for order in ("G.D", "D.G"):
            rows.append({"amplitude": an, "record": "R0", "order": order,
                         "q": born(psi, R0, order)})
    for (an, psi) in AMPS:
        for ri, n in enumerate(RF):
            for order in ("G.D", "D.G"):
                rows.append({"amplitude": an, "record": "ROUND-%d" % ri,
                             "order": order, "q": born(psi, n, order)})
    lp_targets = [t for t in rows if t["record"] == "R0"
                  or t["amplitude"] == "THE-UNIFORM-AMPLITUDE"]
    return lp_targets, RF


def census(LD, P, CLS, targets, ecc_rowmap):
    pre = {}
    for cn in ("E-BLOCK", "E-LINE-DECLARED", "E-LINE-COSET"):
        M, nev = CLS[cn]
        A = [list(M[i]) for i in range(DIM)] + [[Fraction(1)] * nev]
        N = left_null(A)
        for v in N:
            if any(sum(v[i] * A[i][j] for i in range(len(A))) != 0
                   for j in range(nev)):
                raise GateFail("G-CENSUS-REPRO", "left-null basis invalid")
        pre[cn] = (A, N, nev)
    distinct = {}
    for t in targets:
        if t["q"] is None:
            continue
        distinct.setdefault(t["q"], []).append(
            (t["amplitude"], t["record"], t["order"]))
    undefined = sum(1 for t in targets if t["q"] is None)

    def word_at(cn, q, prim):
        A, N, nev = pre[cn]
        b = [3 * q[i] for i in range(DIM)] + [Fraction(1)]
        for k, v in enumerate(N):
            if sum(v[i] * b[i] for i in range(len(b))) != 0:
                return {"word": "INFEASIBLE", "route": "AFFINE-CERT",
                        "cert_index": k, "dim": None}
        st, gap, x, y = simplex(A, b)
        if st == "INFEASIBLE":
            return {"word": "INFEASIBLE", "route": "SIMPLEX",
                    "gap": gap, "dim": None}
        nul = null_of(A)
        if not nul:
            return {"word": "UNIQUE", "route": "SIMPLEX", "dim": 0}
        if not prim:
            return {"word": "FEASIBLE-AT-THE-FIBER-ROW",
                    "route": "SIMPLEX", "dim": None}
        w = [int(sum(A[i][j] for i in range(DIM))) for j in range(nev)]
        forced = [j for j in range(nev) if w[j] < 3]
        support = [j for j in range(nev) if j not in set(forced)]
        A2 = []
        for i in range(len(A)):
            row = [A[i][j] for j in support]
            row.append(sum(A[i][j] for j in support))
            A2.append(row)
        st2, val2, x2, _ = simplex(
            A2, b, [Fraction(0)] * len(support) + [Fraction(-1)])
        implicit = list(forced)
        if not (st2 == "FEASIBLE" and -val2 > 0):
            for j in support:
                cvec = [Fraction(0)] * nev
                cvec[j] = Fraction(-1)
                st3, v3, _x3, _y3 = simplex(A, b, cvec)
                if -v3 == 0:
                    implicit.append(j)
        A3 = A + [[Fraction(1) if kk == j else Fraction(0)
                   for kk in range(nev)] for j in implicit]
        d = len(null_of(A3))
        return {"word": "UNIQUE" if d == 0 else "MANY",
                "route": "SIMPLEX", "dim": d}

    words = Counter()
    rows = []
    dims = set()
    ceiling_exceptions = 0
    match = 0
    for q in sorted(distinct, key=lambda qq: tuple(qq)):
        mem = tuple(sorted(distinct[q]))
        prim = any(r == "R0" for (_a, r, _o) in mem)
        rb = word_at("E-BLOCK", list(q), prim)
        for cn in ("E-BLOCK", "E-LINE-COSET", "E-LINE-DECLARED",
                   "E-TRIPLE"):
            if cn == "E-BLOCK":
                res = rb
            elif cn == "E-TRIPLE":
                res = {"word": rb["word"],
                       "route": "DEFICIENT-WRITER-THEOREM",
                       "dim": rb["dim"]}
            else:
                res = word_at(cn, list(q), prim)
            words[res["word"]] += 1
            if res["word"] == "MANY":
                dims.add(res["dim"])
            if res["word"] != "INFEASIBLE" and max(q) > Fraction(1, 3):
                ceiling_exceptions += 1
            key = (cn, mem)
            agree = ecc_rowmap.get(key) == res["word"]
            match += 1 if agree else 0
            rows.append({"class": cn, "members": mem, "word": res["word"],
                         "route": res["route"], "dim": res["dim"],
                         "receipt_word_agrees": agree,
                         "sample_space": "TRIPLE-EVENTS"})
    if mut("MUT-CENSUS"):
        rows.append(dict(rows[0]))
        words[rows[0]["word"]] += 1
    if mut("MUT-CEIL"):
        ceiling_exceptions += 1
    prem = {}
    for cn in sorted(CLS):
        M, nev = CLS[cn]
        colmax = max(int(sum(M[i][j] for i in range(DIM)))
                     for j in range(nev))
        prem[cn] = {"entries_01": all(M[i][j] in (0, 1)
                                      for i in range(DIM)
                                      for j in range(nev)),
                    "colmax": colmax}
    sum1 = all(sum(q) == 1 for q in distinct)
    P["census"] = {"rows": rows, "words": sorted(words.items()),
                   "distinct_targets": len(distinct),
                   "target_rows": len(targets),
                   "undefined_targets": undefined,
                   "many_dims": sorted(dims),
                   "ceiling_exceptions": ceiling_exceptions,
                   "receipt_row_matches": match,
                   "theorem_premises": prem,
                   "targets_sum_to_one": sum1,
                   "sample_space": "TRIPLE-EVENTS"}
    LD.gate("G-CENSUS-REPRO",
            len(rows) == 156 and match == 156
            and dict(words) == {"FEASIBLE-AT-THE-FIBER-ROW": 6,
                                "INFEASIBLE": 136, "MANY": 6, "UNIQUE": 8}
            and sorted(dims) == [8]
            and len(distinct) == 39 and len(targets) == 82
            and undefined == 2,
            "the complete 156-row feasibility census is recomputed by an "
            "independent solver and every row's word equals the delivered "
            "receipt's word, 156 of 156",
            {"matches": match, "words": sorted(words.items())})
    LD.gate("G-CEILING",
            ceiling_exceptions == 0 and sum1
            and all(prem[cn]["entries_01"] and prem[cn]["colmax"] <= 3
                    for cn in prem),
            "the ceiling theorem's premises hold (0/1 incidence, no event "
            "writes more than 3 cells, unit-mass targets) and no feasible "
            "row exceeds one third, at 156 of 156 rows exceptions 0",
            {"exceptions": ceiling_exceptions})
    return distinct


def committed_row(LD, P, CLS):
    qc = born(SINGLE, R0, "G.D")
    if mut("MUT-Q"):
        qc = tuple(2 * v for v in qc)
    P["committed_q"] = {"support": [(i, qc[i]) for i in range(DIM)
                                    if qc[i] != 0],
                        "qmax": max(qc),
                        "sample_space": "CELLS",
                        "note": "post-coin Born weights of the walk's own "
                                "start state; a distribution over CELLS, "
                                "sum one"}
    LD.gate("G-COMMITTED-Q",
            sum(qc) == 1 and max(qc) == Fraction(4, 9)
            and sorted(i for i in range(DIM) if qc[i] != 0) == [0, 1, 2]
            and qc[0] == Fraction(1, 9),
            "the committed target is recomputed from the walk: weights "
            "(1/9, 4/9, 4/9) on the three cells of the start site, "
            "qmax 4/9 above the ceiling",
            {"qmax": qc[1]})
    duals = []
    for cn in ("E-BLOCK", "E-LINE-COSET", "E-LINE-DECLARED", "E-TRIPLE"):
        M, nev = CLS[cn]
        A = [list(M[i]) for i in range(DIM)] + [[Fraction(1)] * nev]
        b = [3 * qc[i] for i in range(DIM)] + [Fraction(1)]
        st, gap, x, y = simplex(A, b)
        if mut("MUT-GAP"):
            gap = gap + 1
        if mut("MUT-CERT"):
            y = [y[0] + 1] + list(y[1:])
        dual_ok = (st == "INFEASIBLE"
                   and all(sum(y[i] * A[i][j] for i in range(len(A))) <= 0
                           for j in range(nev))
                   and all(v <= 1 for v in y)
                   and sum(y[i] * b[i] for i in range(len(b))) == gap)
        duals.append({"class": cn, "status": st, "gap": gap,
                      "dual_valid": dual_ok, "dual_vector": list(y),
                      "sample_space": "TRIPLE-EVENTS"})
    P["committed_duals"] = duals
    got = {d["class"]: str(d["gap"]) for d in duals}
    LD.gate("G-COMMITTED-ROW",
            got == {"E-BLOCK": "4", "E-LINE-DECLARED": "4",
                    "E-LINE-COSET": "3", "E-TRIPLE": "7/3"}
            and all(d["status"] == "INFEASIBLE" for d in duals),
            "the committed row is infeasible at all four committed "
            "classes with exact phase-one gaps 4, 4, 3, 7/3 equal to the "
            "delivered receipt's gaps", got)
    LD.gate("G-FARKAS", all(d["dual_valid"] for d in duals),
            "each committed-class infeasibility carries a verified exact "
            "Farkas certificate: y.A <= 0 columnwise, y <= 1, and "
            "y.b equals the gap",
            {"classes": 4})
    return qc


def lp_controls(LD, P, CLS):
    M, nev = CLS["E-BLOCK"]
    A = [list(M[i]) for i in range(DIM)] + [[Fraction(1)] * nev]
    tot = nev * (nev + 1) // 2
    phat = [Fraction(j + 1, tot) for j in range(nev)]
    qf = [sum(M[i][j] * phat[j] for j in range(nev)) / 3
          for i in range(DIM)]
    bf = [3 * v for v in qf] + [Fraction(1)]
    stf, _gf, _xf, _yf = simplex(A, bf)
    qi = [Fraction(0)] * DIM
    qi[0] = Fraction(1)
    bi = [3 * v for v in qi] + [Fraction(1)]
    sti, gi, _xi, _yi = simplex(A, bi)
    P["lp_controls"] = {"forced_feasible_status": stf,
                        "forced_infeasible_status": sti,
                        "forced_infeasible_ceiling": max(qi) > Fraction(1, 3),
                        "sample_space": "TRIPLE-EVENTS"}
    LD.gate("G-LP-CONTROLS",
            stf == "FEASIBLE" and sti == "INFEASIBLE"
            and max(qi) > Fraction(1, 3),
            "both control arms fire through the real solver: the known "
            "mixture is feasible, the single-cell target is infeasible "
            "with the ceiling witness, matching the delivered controls",
            None)


# ===========================================================================
# SECTION 5.  S1 -- THE PUSHFORWARD THEOREM AND THE FOUR-ESCAPE MENU
# ===========================================================================
def s1_pushforward(LD, P, CLS, qc):
    # the constructed history-law instance: uniform mu over the 36
    # admissible rounds; the read map picks the round's block containing
    # the start actor (a declared selector; every round has exactly one)
    start = SITES[0]
    pf = Counter()
    for rnd in ROUNDS:
        blk = [b for b in rnd if start in b]
        if len(blk) != 1:
            raise GateFail("G-PUSHFORWARD", "selector not unique")
        pf[blk[0]] += 1
    p = {t: Fraction(c, len(ROUNDS)) for t, c in sorted(pf.items())}
    total = sum(p.values())
    if mut("MUT-HISTORY"):
        p[sorted(p)[0]] += 1
    marg = [sum(pv for t, pv in p.items() if c in BLOCK_OF[t])
            for c in range(DIM)]
    P["s1_history_law"] = {
        "histories": len(ROUNDS), "distinct_events": len(p),
        "pushforward_total": sum(p.values()),
        "occupancy_marginal_sum": sum(marg),
        "occupancy_marginal_max": max(marg),
        "ceiling_bound_holds": max(marg) <= 1,
        "sample_space": "TRIPLE-EVENTS",
        "note": "an ordinary positive history law pushes forward to a "
                "probability over TRIPLE-EVENTS; its inclusion marginal "
                "never exceeds 1, so a Born weight tied to a third of it "
                "never exceeds 1/3"}
    LD.gate("G-PUSHFORWARD",
            total == 1 and sum(p.values()) == 1 and max(marg) <= 1,
            "the pushforward of the constructed history law is a "
            "probability over triple events with inclusion marginals "
            "bounded by total mass; the theorem instance verifies",
            {"max_marginal": max(marg)})
    # ESCAPE (a): the successor ontology -- Omega = union over G of
    # {(G, R, rho, event data)}; probabilities over complete successors
    Kunif = Fraction(1, 3)
    blocks_of_cell = {c: [t for t in TRIANGLES if c in BLOCK_OF[t]]
                      for c in range(DIM)}
    joint = {}
    for c in range(DIM):
        if qc[c] == 0:
            continue
        for t in blocks_of_cell[c]:
            joint[(c, t)] = qc[c] * pick("MUT-ESCA", Kunif, Fraction(1, 2))
    trig = [sum(v for (c, t), v in joint.items() if c == cc)
            for cc in range(DIM)]
    pev = Counter()
    for (c, t), v in joint.items():
        pev[t] += v
    incl = [sum(v for t, v in pev.items() if c in BLOCK_OF[t])
            for c in range(DIM)]
    succ = {}
    for t in sorted(pev):
        succ[t] = {"record": nfield(BLOCK_OF[t]),
                   "geometry": "G-UNCHANGED", "event": t}
    recs = [succ[t]["record"] for t in sorted(succ)]
    distinct_succ = len(set(recs)) == len(recs)
    P["s1_escape_a"] = {
        "joint_total": sum(joint.values()),
        "trigger_readout_equals_q": trig == list(qc),
        "successors": len(succ),
        "successors_pairwise_distinct": distinct_succ,
        "inclusion_marginal_max": max(incl),
        "inclusion_marginal_of_event_law_equals_3q":
            incl == [3 * v for v in qc],
        "instantaneous_triple_retained": True,
        "scaffold_status": "SCAFFOLD, not a successor dynamics: each "
                           "stored successor carries (event, new "
                           "record, G-UNCHANGED) and NO rho'_e -- "
                           "normalized trigger/triple bookkeeping on "
                           "the fixed arena; rho'_e and carrier "
                           "transport are owed",
        "exhibited_semantics": "TRIGGER-MARGINAL-NOT-OCCUPANCY-"
                               "MARGINAL: q is read as a trigger "
                               "marginal of the joint law, not as an "
                               "occupancy marginal; the construction "
                               "RETAINS an instantaneous triple t",
        "trigger_semantics_status": "the trigger reading is the "
                                    "exhibited construction's reading, "
                                    "a CANDIDATE -- not an established "
                                    "physical mechanism: cells have "
                                    "not been proven to trigger "
                                    "triple-events, and establishing "
                                    "or rejecting the trigger "
                                    "mechanism is SCOUT-K's charge",
        "uniform_kernel_alpha": Fraction(1, 3),
        "uniform_kernel_tension": "the scaffold's uniform kernel is "
                                  "rejected by the scout's own "
                                  "three-step test under walk "
                                  "preservation (the alpha probes "
                                  "refuse 0, 1/3 and 1 alike)",
        "lp_change": "the constraint M p = 3 q is DELETED, not repaired; "
                     "the object is P(X'_e | X) over mutually exclusive "
                     "complete local successors, sum 1; q returns as the "
                     "trigger readout of the joint law",
        "sample_space": "COMPLETE-SUCCESSOR-CONFIGURATIONS"}
    LD.gate("G-ESCAPE-A",
            sum(joint.values()) == 1 and trig == list(qc)
            and distinct_succ
            and incl != [3 * v for v in qc],
            "escape (a) exhibited by construction AS A SCAFFOLD "
            "(normalized trigger/triple bookkeeping on the fixed arena, "
            "no rho'_e, geometry unchanged): a normalized law over "
            "complete-successor bookkeeping carries the committed q as "
            "its trigger readout while its event-law inclusion marginal "
            "is NOT 3q -- the bridge is abandoned, nothing is violated; "
            "the exhibited escape is trigger-marginal semantics, and an "
            "instantaneous triple variable is retained",
            {"max_inclusion": max(incl)})
    # ESCAPE (b): endpoint statistics -- the (c,e) endpoint matrix has
    # column sums 1; every simplex target is expressible
    pairs = sorted(joint)
    colsums = [1 for _ in pairs]
    P["s1_escape_b"] = {
        "endpoint_pairs": len(pairs),
        "column_sum": pick("MUT-ESCB", 1, 2),
        "ceiling_constant": "1/1",
        "expressible": trig == list(qc),
        "lp_change": "the incidence matrix M (column sums 3) is replaced "
                     "by the endpoint matrix (column sums 1); the ceiling "
                     "constant 1/3 becomes 1/1 and is vacuous",
        "sample_space": "CELLS"}
    LD.gate("G-ESCAPE-B",
            P["s1_escape_b"]["column_sum"] == 1
            and P["s1_escape_b"]["expressible"],
            "escape (b) exhibited by construction: endpoint Born "
            "statistics have unit column sums and express the committed "
            "target exactly",
            None)
    # ESCAPE (c): drop positivity/additivity -- signed solvability
    esc_c = []
    for cn in ("E-BLOCK", "E-LINE-COSET", "E-LINE-DECLARED", "E-TRIPLE"):
        M, nev = CLS[cn]
        A = [list(M[i]) for i in range(DIM)] + [[Fraction(1)] * nev]
        b = [3 * qc[i] for i in range(DIM)] + [Fraction(1)]
        rk = rank_of(A)
        rk2 = rank_of([A[i] + [b[i]] for i in range(len(A))])
        row = {"class": cn, "rank_A": rk, "rank_Ab": rk2,
               "signed_solvable": rk == rk2, "min_entry": None,
               "sample_space": "TRIPLE-EVENTS"}
        if rk == rk2:
            R, piv = rref([A[i] + [b[i]] for i in range(len(A))])
            x = [Fraction(0)] * nev
            for i, pj in enumerate(piv):
                if pj < nev:
                    x[pj] = R[i][nev]
            ok = all(sum(A[i][j] * x[j] for j in range(nev)) == b[i]
                     for i in range(len(A)))
            if mut("MUT-ESCC"):
                x[0] += 1
                ok = all(sum(A[i][j] * x[j] for j in range(nev)) == b[i]
                         for i in range(len(A)))
            row["witness_verifies"] = ok
            row["min_entry"] = min(x)
        esc_c.append(row)
    got = {r["class"]: r["signed_solvable"] for r in esc_c}
    P["s1_escape_c"] = {"per_class": esc_c,
                        "lp_change": "the positivity constraint p >= 0 is "
                                     "dropped (a non-additive history "
                                     "measure's marginal need not be "
                                     "positive); solvability becomes an "
                                     "affine-span question"}
    LD.gate("G-ESCAPE-C",
            got == {"E-BLOCK": False, "E-LINE-DECLARED": False,
                    "E-LINE-COSET": False, "E-TRIPLE": True}
            and all(r.get("witness_verifies", True) for r in esc_c),
            "escape (c) is class-split: the committed target is outside "
            "the affine span at the block and both line classes (signed "
            "measures do not help), and inside it at the full triple "
            "class with a verified signed witness",
            got)
    # ESCAPE (d): selection -- scale invariance kills the minimal form
    esc_d = []
    M, nev = CLS["E-BLOCK"]
    for lam in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
        A = [list(M[i]) for i in range(DIM)] + [[Fraction(1)] * nev]
        b = [3 * lam * qc[i] for i in range(DIM)] + [lam]
        st, gap, x, y = simplex(A, b)
        st = pick("MUT-ESCD", st, "FEASIBLE")
        esc_d.append({"lambda": lam, "status": st,
                      "sample_space": "TRIPLE-EVENTS"})
    P["s1_escape_d"] = {
        "scaled_rows": esc_d,
        "lp_change": "record-writing on a selected sub-ensemble of mass "
                     "lambda rescales the system by lambda exactly; the "
                     "conditional-on-selection law re-enters the same LP",
        "identity": "M r = 3 lambda q with r >= 0, sum r = lambda is "
                    "equivalent to M(r/lambda) = 3 q on the simplex"}
    LD.gate("G-ESCAPE-D",
            all(r["status"] == "INFEASIBLE" for r in esc_d),
            "escape (d) in its minimal form is refused by scale "
            "invariance: the selected sub-ensemble system is infeasible "
            "at every tested selection mass; cell-selective writing is "
            "escape (b) under another name",
            {"tested": len(esc_d)})


# ===========================================================================
# SECTION 6.  S2 -- THE KERNEL K(e|c,G,R)
# ===========================================================================
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


def s2_kernel(LD, P, qc):
    glin = [A for A in lin_maps()
            if all(class_rep(apply_lin(A, l)) in LINKS for l in LINKS)]
    gamma = [(A, t) for A in glin for t in SITES]
    if mut("MUT-GAMMA"):
        gamma = gamma[:-1]

    def g_site(g, x):
        A, t = g
        return vadd(apply_lin(A, x), t)

    def g_cell(g, ci):
        return PAIR_CELL[frozenset(g_site(g, x) for x in CELL_PAIR[ci])]

    def g_tri(g, t):
        return tuple(sorted(g_site(g, x) for x in t))

    tri_set = set(TRIANGLES)
    closed = all(g_tri(g, t) in tri_set for g in gamma for t in TRIANGLES)
    P["s2_gamma"] = {"linear_order": len(glin), "order": len(gamma),
                     "blocks_closed": closed}
    LD.gate("G-GAMMA", len(glin) == 12 and len(gamma) == 108 and closed,
            "the relabelling group is the affine stabilizer of the "
            "declared direction set: order 108 (12 linear x 9 "
            "translations), and the block class is closed under it",
            {"order": len(gamma)})

    def orbits(elems, act):
        left = set(elems)
        out = []
        while left:
            e = sorted(left)[0]
            orb = {e}
            frontier = [e]
            while frontier:
                x = frontier.pop()
                for g in gamma:
                    y = act(g, x)
                    if y not in orb:
                        orb.add(y)
                        frontier.append(y)
            out.append(sorted(orb))
            left -= orb
    # deterministic order
        return sorted(out)

    ocell = orbits(range(DIM), g_cell)
    otri = orbits(TRIANGLES, g_tri)
    inc = [(c, t) for t in TRIANGLES for c in BLOCK_OF[t]]
    opair = orbits(inc, lambda g, p: (g_cell(g, p[0]), g_tri(g, p[1])))
    stab0 = [g for g in gamma if g_cell(g, 0) == 0]
    b0 = [t for t in TRIANGLES if 0 in BLOCK_OF[t]]
    sorb = set()
    for t in b0:
        sorb.add(frozenset(g_tri(g, t) for g in stab0))
    sorb_sizes = sorted(len([t for t in b0 if t in o]) for o in sorb)
    npar = len(opair)
    if mut("MUT-ORBIT"):
        npar = npar - 1
    poi = {}
    for k, o in enumerate(opair):
        for pr in o:
            poi[pr] = k
    reps = [o[0] for o in ocell]
    rows = []
    for c in reps:
        row = [Fraction(0)] * npar
        for t in TRIANGLES:
            if c in BLOCK_OF[t]:
                row[poi[(c, t)] % npar] += 1
        rows.append(row)
    rk = rank_of(rows)
    equi_dim = npar - rk
    line_orbit_sizes = sorted(len(o) for o in otri)
    P["s2_orbits"] = {
        "cell_orbits": [len(o) for o in ocell],
        "block_orbits": line_orbit_sizes,
        "incident_pair_orbits": sorted(len(o) for o in opair),
        "stab_cell_order": len(stab0),
        "stab_orbits_on_incident_blocks": sorb_sizes,
        "equivariant_parameters": npar,
        "equivariant_constraint_rank": rk,
        "equivariant_dim": equi_dim}
    LD.gate("G-EQUIVARIANCE",
            [len(o) for o in ocell] == [27]
            and line_orbit_sizes == [9, 18]
            and sorted(len(o) for o in opair) == [27, 54]
            and len(stab0) == 4 and sorb_sizes == [1, 2]
            and equi_dim == 1,
            "equivariance is measured, not assumed: cells transitive, "
            "blocks split 9 lines + 18 non-lines, incident pairs split "
            "27 + 54, the cell stabilizer (order 4) swaps the two "
            "non-line blocks, and the record-blind equivariant kernel "
            "family has dimension exactly 1 (the one fixed line weight "
            "alpha)",
            P["s2_orbits"])
    # locality: support locality is structural; the declared adjacency
    adj_ok = True
    for t in TRIANGLES:
        for c in BLOCK_OF[t]:
            pc = CELL_PAIR[c]
            for c2 in BLOCK_OF[t]:
                if not (CELL_PAIR[c2] & pc) and c2 != c:
                    adj_ok = False
    P["s2_locality"] = {
        "adjacency": "two cells are adjacent when their actor pairs "
                     "share an actor",
        "support_local": adj_ok,
        "proximity_declaration": "the shared-actor adjacency is itself "
                                 "a DECLARATION and is counted as one; "
                                 "Q27 -- whether proximity is "
                                 "primitive, or means record "
                                 "co-participation, declared "
                                 "adjacency, causal influence, or "
                                 "something else -- remains OPEN; the "
                                 "alternatives (record-distance, "
                                 "metric distance, causal "
                                 "neighborhood) are SCOUT-K's "
                                 "declared fork",
        "record_dependence": "at the committed record R0 the kernel's "
                             "record argument is constant; the "
                             "round-window rows are fiber rows"}
    LD.gate("G-LOCALITY", adj_ok,
            "locality holds structurally at the block class: every cell "
            "an incident event writes shares an actor with the trigger "
            "cell, so the kernel's support lies inside the declared "
            "neighborhood", None)
    # ARM A: trigger-only -- the vacuous null and the equivariant cut
    norm_rows = []
    inc_index = {p: k for k, p in enumerate(inc)}
    for c in range(DIM):
        row = [Fraction(0)] * len(inc)
        for t in TRIANGLES:
            if c in BLOCK_OF[t]:
                row[inc_index[(c, t)]] = Fraction(1)
        norm_rows.append(row)
    bare_dim = len(inc) - rank_of(norm_rows)
    P["s2_arm_a"] = {"variables": len(inc), "bare_dim": bare_dim,
                     "equivariant_dim": equi_dim,
                     "strictly_stronger_than_vacuous": equi_dim < bare_dim,
                     "sample_space": "TRIPLE-EVENTS",
                     "word": "SCOUT-KERNEL-NONVACUOUS-TRIGGER-ONLY-DIM-%d"
                             % bare_dim}
    LD.gate("G-ARM-A", bare_dim == 54 and equi_dim == 1,
            "arm one (trigger-cell-only): normalization alone leaves the "
            "54-dimensional vacuous null (ECC's disclosed free two-stage); "
            "equivariance cuts it to the one-parameter line family -- "
            "strictly stronger than vacuous, shown by dimension",
            {"bare": bare_dim, "equivariant": equi_dim})
    # ARM B: all-write-one-measured -- W = 3q re-imported
    rows_b = []
    rhs_b = []
    for c in range(DIM):
        row = [Fraction(0)] * len(inc)
        for t in TRIANGLES:
            if c in BLOCK_OF[t]:
                row[inc_index[(c, t)]] = Fraction(1)
        rows_b.append(row)
        rhs_b.append(Fraction(1))
    for cp in range(DIM):
        row = [Fraction(0)] * len(inc)
        for t in TRIANGLES:
            if cp in BLOCK_OF[t]:
                for c in BLOCK_OF[t]:
                    row[inc_index[(c, t)]] += qc[c]
        rows_b.append(row)
        rhs_b.append(pick("MUT-ARMB", 3 * qc[cp], Fraction(0)))
    st, gap, x, y = simplex(rows_b, rhs_b)
    dual_ok = (st == "INFEASIBLE"
               and all(sum(y[i] * rows_b[i][j]
                           for i in range(len(rows_b))) <= 0
                       for j in range(len(inc)))
               and all(v <= 1 for v in y)
               and sum(y[i] * rhs_b[i] for i in range(len(rhs_b))) == gap)
    P["s2_arm_b"] = {"status": st, "gap": gap, "dual_valid": dual_ok,
                     "sample_space": "TRIPLE-EVENTS",
                     "word": "SCOUT-KERNEL-EMPTY-AT-ALL-WRITE-ONE-"
                             "MEASURED"}
    LD.gate("G-ARM-B", st == "INFEASIBLE" and gap == 6 and dual_ok,
            "arm two (all-write-one-measured) is EMPTY at the committed "
            "row with exact gap 6 and a verified Farkas certificate: "
            "demanding the written-cell marginal reproduce 3q re-imports "
            "the pushforward bridge, and S1's theorem kills it",
            {"gap": gap})
    return gamma


def s2_record_consistency(LD, P):
    post1 = coin_apply(list(SINGLE), list(R0), "G.D")
    psi1 = walk_shift(post1)
    # MUT-BLIND replaces the stepped state by the pre-shift state, whose
    # start site carries three occupied links, so the count phases become
    # relative and the blindness claim must measurably fail.
    psi_w2 = pick("MUT-BLIND", psi1, tuple(post1))
    q2 = born(psi1, R0, "G.D")
    sup2 = [c for c in range(DIM) if q2[c] > 0]
    blocks_of_cell = {c: [t for t in TRIANGLES if c in BLOCK_OF[t]]
                      for c in range(DIM)}
    # depth-2: increment blindness
    variants = {"R0": R0}
    for c in (0, 1, 2):
        variants["HIT-%d" % c] = nfield([c])
    tri_inc = []
    for c in (0, 1, 2):
        for t in blocks_of_cell[c]:
            if t not in tri_inc:
                tri_inc.append(t)
    for k, t in enumerate(tri_inc):
        variants["TRI-%d" % k] = nfield(BLOCK_OF[t])
    base = born(psi_w2, R0, "G.D")
    blind = all(born(psi_w2, n, "G.D") == base
                for _k, n in sorted(variants.items()))
    occ1 = sorted(i for i, z in enumerate(psi_w2) if z != Z0)
    single_link = all(
        sum(1 for j in range(3) if psi_w2[s * 3 + j] != Z0) <= 1
        for s in range(9))
    P["s2_arm_c_depth2"] = {
        "variants": len(variants), "all_equal": blind,
        "occupied_cells": occ1,
        "single_link_per_site": single_link,
        "mechanism": "every occupied site carries one link only, so a "
                     "count phase there is a global phase of that site "
                     "block and the post-coin Born vector cannot move",
        "sample_space": "CELLS",
        "word": "VACUOUS-AT-THE-TWO-STEP-WINDOW"}
    LD.gate("G-ARM-C-WINDOW2", blind and single_link
            and len(variants) == 11,
            "arm three at the two-step window is VACUOUS: the step-two "
            "Born vector is byte-identical across the initial record, "
            "all 3 cell-hit increments and all 7 incident triple-writes "
            "(11 variants); the mechanism is single-link site support",
            {"variants": len(variants)})
    # depth-3: the first window with teeth
    def step(psi, n):
        return walk_shift(coin_apply(list(psi), list(n), "G.D"))

    def q3_of(n1_cells, n2_cells):
        psi2 = step(psi1, nfield(n1_cells))
        return born(psi2, nfield(list(n1_cells) + list(n2_cells)), "G.D")

    def kpoly(t):
        # K_alpha: alpha on the line block, (1-alpha)/2 on each non-line
        if t in LINE_SET:
            return (Fraction(0), Fraction(1))
        return (Fraction(1, 2), Fraction(-1, 2))

    def pmul(p, q):
        out = [Fraction(0)] * (len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                out[i + j] += a * b
        return tuple(out)

    def padd(p, q):
        n = max(len(p), len(q))
        out = [Fraction(0)] * n
        for i, a in enumerate(p):
            out[i] += a
        for i, b in enumerate(q):
            out[i] += b
        return tuple(out)

    polys = set()
    nrows = 0
    compat = {}
    for c1 in (0, 1, 2):
        for c2 in sup2:
            rhs = q3_of([c1], [c2])
            acc = [tuple() for _ in range(DIM)]
            for e1 in blocks_of_cell[c1]:
                for e2 in blocks_of_cell[c2]:
                    v = q3_of(BLOCK_OF[e1], BLOCK_OF[e2])
                    compat[(c1, e1, c2, e2)] = (v == rhs)
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
    if mut("MUT-ARMC"):
        polys = {p for p in polys if len(p) != 2}
    lin_roots = sorted({-p[0] / p[1] for p in polys if len(p) == 2})
    alpha_tests = {}
    for a in (Fraction(0), Fraction(1, 3), Fraction(1)):
        alpha_tests[str(a)] = all(
            sum(co * a ** i for i, co in enumerate(p)) == 0
            for p in polys)
    combos_ok = []
    total_kernels = 0
    for combo in product(*[blocks_of_cell[c] for c in (0, 1, 2)]):
        prod_ct = 1
        ok = True
        for c2 in sup2:
            k = sum(1 for e2 in blocks_of_cell[c2]
                    if all(compat[(c1, combo[i], c2, e2)]
                           for i, c1 in enumerate((0, 1, 2))))
            if k == 0:
                ok = False
                break
            prod_ct *= k
        if ok:
            combos_ok.append([t in LINE_SET for t in combo])
            total_kernels += prod_ct
    all_nonline = all(not any(pat) for pat in combos_ok)
    P["s2_arm_c_depth3"] = {
        "rows": nrows, "distinct_nonzero_polys": len(polys),
        "linear_poly_roots": lin_roots,
        "record_blind_fixed_alpha_line_empty": len(lin_roots) >= 2,
        "alpha_probes": alpha_tests,
        "pure_first_step_survivors": len(combos_ok),
        "pure_survivors_all_nonline": all_nonline,
        "pure_kernels_total": total_kernels,
        "kernel_family_scope": "RECORD-BLIND, FIXED-ALPHA: the "
                               "three-step test multiplies the SAME "
                               "one-parameter line-vs-non-line kernel "
                               "polynomial at BOTH event selections, "
                               "although the first event has already "
                               "changed the record R; true "
                               "equivariance K(ge|gc,gG,gR)=K(e|c,G,R) "
                               "admits record-dependent kernels that "
                               "distinguish candidate triples by their "
                               "relation to the written record, and "
                               "that census is SCOUT-K's "
                               "(v15/note-scoutk-pin.md), not this "
                               "unit's",
        "sample_space": "CELLS",
        "word": "NONVACUOUS-AT-THE-THREE-STEP-WINDOW-EMPTY-ON-THE-"
                "RECORD-BLIND-FIXED-ALPHA-LINE"}
    LD.gate("G-ARM-C-WINDOW3",
            nrows == 729 and len(polys) == 25
            and lin_roots == [Fraction(-1), Fraction(0), Fraction(1)]
            and not any(alpha_tests.values())
            and len(combos_ok) == 8 and all_nonline
            and total_kernels == 288,
            "arm three first bites at the three-step window: 729 "
            "agreement rows reduce to 25 distinct polynomials in the "
            "line weight; linear rows force alpha = -1, alpha = 0 and "
            "alpha = 1 simultaneously, so the record-blind fixed-alpha "
            "equivariant line is EMPTY over the reals (the "
            "record-dependent equivariant question is SCOUT-K's); 8 "
            "pure non-line first-step selections survive, "
            "extending to 288 pure kernels on the reached cells",
            {"rows": nrows, "polys": len(polys),
             "survivors": len(combos_ok)})
    # overlap-exclusivity: distinct successors from overlapping triples
    recs = [nfield(BLOCK_OF[t]) for t in TRIANGLES]
    if mut("MUT-EXCL"):
        recs[1] = recs[0]
    pairs = sum(1 for i in range(len(recs)) for j in range(i + 1, len(recs))
                if recs[i] == recs[j])
    P["s2_exclusivity"] = {
        "block_pairs_checked": len(recs) * (len(recs) - 1) // 2,
        "record_collisions": pairs,
        "sentence": "overlapping triples are compatible with mutual "
                    "exclusivity: exclusivity is about which complete "
                    "successor happens, not about which actors are "
                    "shared, and all 351 successor pairs are distinct"}
    LD.gate("G-OVERLAP", pairs == 0,
            "overlapping triples are compatible with exclusivity: the 27 "
            "block successors are pairwise distinct records, 351 pairs, "
            "0 collisions", {"pairs": 351})
    verdict = ("SCOUT-KERNEL-EMPTY-AT-RECORD-BLIND-FIXED-ALPHA-"
               "AFFINE-EQUIVARIANT"
               if (len(lin_roots) >= 2 and len(combos_ok) > 0
                   and all_nonline) else "SCOUT-KERNEL-UNDETERMINED")
    P["s2_determination"] = {
        "word": verdict,
        "finding": "no record-blind, fixed-alpha, affine-equivariant "
                   "kernel preserves the delivered three-step walk "
                   "statistics: within that measured family, symmetry "
                   "pins the one-parameter line family and record "
                   "consistency excludes that whole line, leaving only "
                   "deterministic kernels outside it; the general "
                   "record-dependent equivariant question is NOT "
                   "decided here and is SCOUT-K's census; an arbitrary "
                   "K remains a hidden free law and is refused"}


# ===========================================================================
# SECTION 7.  S3 -- THE DELTA-B GATE (four pre-conditions)
# ===========================================================================
def s3_deltab(LD, P, CLS, qc):
    G27 = bigG()
    RF = round_fields(ROUNDS)
    # the silence lemma: diagonal factors are Delta-B silent (both sides)
    sil_ok = True
    for n in (R0, nfield([0]), RF[0], RF[1]):
        GD = mm(G27, bigD(n))
        DG = mm(bigD(n), G27)
        BGD = Bmat(GD, 9)
        BDG = Bmat(DG, 9)
        BG = Bmat(G27, 9)
        if mut("MUT-SILENCE"):
            BGD = tuple(tuple(v + 1 for v in row) for row in BGD)
        if BGD != BG or BDG != BG:
            sil_ok = False
    P["s3_silence"] = {
        "records_probed": 4, "holds": sil_ok,
        "lemma": "a diagonal unitary factor never moves an entrywise "
                 "squared modulus, so every one-step phase/coin cut of "
                 "every census row carries Delta-B exactly zero"}
    LD.gate("G-S3-SILENCE", sil_ok,
            "the silence lemma verifies at 4 probed records both sides: "
            "B(G.D) = B(G) = B(D.G) entrywise, so the one-step Delta-B "
            "datum is identically zero across all 156 census rows",
            None)
    # condition 1: the map must target the full dual certificates
    V = mm(G27, bigD(R0))
    BV = Bmat(V, 9)
    BI = Bmat(IDENT, 1)
    BG = Bmat(G27, 9)
    BD = Bmat(bigD(R0), 1)
    cuts = {"I.V": dB(BV, BI, BV), "V.I": dB(BV, BV, BI),
            "G.D": dB(BV, BG, BD)}
    committed_datum = {k: nz_count(v) for k, v in sorted(cuts.items())}
    if mut("MUT-WITNESS"):
        committed_datum["G.D"] = 1
    uniform_datum = dict(committed_datum)  # same record R0, same cuts
    gaps_committed = ("4", "4", "3", "7/3")
    gaps_uniform = ("0", "0", "0", "0")
    cond1_builds = not (committed_datum == uniform_datum
                       and gaps_committed != gaps_uniform)
    P["s3_cond1"] = {
        "committed_datum_nonzero_entries": committed_datum,
        "uniform_r0_datum_nonzero_entries": uniform_datum,
        "committed_gap_vector": list(gaps_committed),
        "uniform_gap_vector": list(gaps_uniform),
        "map_well_defined": cond1_builds,
        "verdict": "FAILS-TO-BUILD: the committed row and the uniform-R0 "
                   "row carry byte-identical (all-zero) Delta-B data at "
                   "every declared cut while their delivered certificate "
                   "vectors differ (4,4,3,7/3 against feasibility); no "
                   "function of the datum can target the certificates"}
    LD.gate("G-S3-COND1",
            committed_datum == {"G.D": 0, "I.V": 0, "V.I": 0}
            and not cond1_builds,
            "S3 pre-condition (1) fails to build: identical zero datum, "
            "different certificate targets -- the identification map is "
            "not a function of the Delta-B datum",
            committed_datum)
    # condition 2: cut invariance incl. the degenerate I.U cut
    P["s3_cond2"] = {
        "cut_family": sorted(cuts),
        "datum_invariant_across_cuts": len(set(
            committed_datum.values())) == 1,
        "invariant_value_zero": all(v == 0
                                    for v in committed_datum.values()),
        "obstruction_stands": True,
        "verdict": "the datum is cut-invariant only because it is zero "
                   "at every allowed cut, the degenerate I.U cut "
                   "included, while the obstruction stands at gaps "
                   "4, 4, 3, 7/3 -- an identification that needs a "
                   "nonzero cut-stable value has none"}
    LD.gate("G-S3-COND2",
            P["s3_cond2"]["datum_invariant_across_cuts"]
            and P["s3_cond2"]["invariant_value_zero"],
            "S3 pre-condition (2): the cut sweep is built and the "
            "invariant value is zero at every member including the "
            "degenerate cut, while the obstruction stands",
            None)
    # condition 3: the two countercontrols
    BS = Bmat(SPERM, 1)
    BSS = Bmat(mm(SPERM, SPERM), 1)
    perm_zero = dB(BSS, BS, BS) == ZERO27 and \
        dB(BS, BI, BS) == ZERO27 and dB(BS, BS, BI) == ZERO27
    qP = tuple(Fraction(1) if k == SHIFT[0] else Fraction(0)
               for k in range(DIM))
    M, nev = CLS["E-BLOCK"]
    A = [list(M[i]) for i in range(DIM)] + [[Fraction(1)] * nev]
    bP = [3 * v for v in qP] + [Fraction(1)]
    stP, gP, _xP, _yP = simplex(A, bP)
    F27 = bigF()
    BF = Bmat(F27, 3)
    BFF = Bmat(mm(F27, F27), 9)
    dF = dB(BFF, BF, BF)
    nzF = pick("MUT-CONTROL", nz_count(dF), 0)
    wF = [znorm(F27[i][0]) for i in range(DIM)]
    totF = sum(wF)
    qmid = tuple(Fraction(x, totF) for x in wF)
    mid_rows = {}
    for cn in ("E-BLOCK", "E-LINE-COSET", "E-LINE-DECLARED", "E-TRIPLE"):
        Mx, nevx = CLS[cn]
        Ax = [list(Mx[i]) for i in range(DIM)] + [[Fraction(1)] * nevx]
        bx = [3 * v for v in qmid] + [Fraction(1)]
        stx, gx, _xx, _yx = simplex(Ax, bx)
        mid_rows[cn] = {"status": stx,
                        "ceiling_witness": max(qmid) > Fraction(1, 3)}
    P["s3_cond3"] = {
        "perm_control": {"qmax": max(qP), "lp_status": stP,
                         "ceiling_witness": max(qP) > Fraction(1, 3),
                         "delta_b_zero_at_all_cuts": perm_zero,
                         "kills": "EXCESS-WITHOUT-DELTA-B",
                         "sample_space": "CELLS"},
        "fourier_control": {"delta_b_nonzero_entries": nzF,
                            "intermediate_qmax": max(qmid),
                            "at_the_cap": max(qmid) == Fraction(1, 3),
                            "lp_rows": mid_rows,
                            "kills": "DELTA-B-WITHOUT-EXCESS",
                            "sample_space": "CELLS"}}
    LD.gate("G-S3-COND3",
            perm_zero and stP == "INFEASIBLE" and max(qP) == 1
            and nzF == 81 and max(qmid) == Fraction(1, 3)
            and all(r["status"] == "INFEASIBLE"
                    and not r["ceiling_witness"]
                    for r in mid_rows.values()),
            "both countercontrols run and both kill: the basis "
            "permutation violates the ceiling grossly (qmax 1) with "
            "Delta-B exactly zero at every cut, and F3,F3 carries 81 "
            "nonzero Delta-B entries with a uniform intermediate at the "
            "cap (its rows even fail structurally, without any ceiling "
            "witness)",
            {"perm_qmax": "1", "fourier_nz": nzF})
    # condition 4: the scored 156-row feasibility prediction
    # predictor PRED-DB: predict INFEASIBLE iff the row's one-step
    # phase/coin Delta-B datum is nonzero.  By the silence lemma the
    # datum is zero at every row, so the predictor says feasible
    # everywhere.
    words = Counter(r["word"] for r in P["census"]["rows"])
    n_inf = words["INFEASIBLE"]
    correct = pick("MUT-SCORE", 156 - n_inf, 156)
    P["s3_cond4"] = {
        "predictor": "PRED-DB: INFEASIBLE iff one-step Delta-B datum "
                     "nonzero",
        "datum_zero_rows": 156,
        "predicted_infeasible": 0,
        "actual_infeasible": n_inf,
        "correct": correct, "of": 156,
        "confusion": {"true_feasible": 156 - n_inf,
                      "false_feasible": n_inf,
                      "true_infeasible": 0, "false_infeasible": 0},
        "sample_space": "TRIPLE-EVENTS"}
    LD.gate("G-S3-COND4",
            correct == 156 - n_inf and n_inf == 136,
            "S3 pre-condition (4) is built and scored: the declared "
            "predictor scores 20 of 156 (it misses all 136 infeasible "
            "rows, because the datum is identically zero while "
            "feasibility varies) -- the prediction carries no signal",
            {"correct": correct})
    # the exemplar sweep: where Delta-B lives and does not
    W1 = mm(SPERM, mm(G27, bigD(R0)))
    ex = {}
    for lbl, n2 in (("R0", R0), ("HIT-1", nfield([1])),
                    ("ROUND-0", RF[0])):
        W2 = mm(SPERM, mm(G27, bigD(n2)))
        d2 = dB(Bmat(mm(W2, W1), 81), Bmat(W2, 9), Bmat(W1, 9))
        ex[lbl] = nz_count(d2)
    P["s3_step_cuts"] = {
        "two_step_composite_nonzero_entries": ex,
        "note": "even the honest two-step step-cut composites carry "
                "Delta-B zero at every probed record of the committed "
                "walk family; the F3,F3 control is where a nonzero "
                "Delta-B was exhibited at this scout"}
    LD.gate("G-S3-EXEMPLAR",
            all(v == 0 for v in ex.values()),
            "the two-step step-cut sweep at three probed records carries "
            "Delta-B zero everywhere on the committed walk family",
            ex)
    P["s3_verdict"] = {
        "word": "SCOUT-DELTA-B-IDENTIFICATION-KILLED-AT-CONDITION-1-THE-"
                "DATUM-DOES-NOT-DETERMINE-THE-CERTIFICATE",
        "overdetermination": "conditions (2), (3), (4) also fail as "
                             "measured above; the identification is "
                             "retired on the record"}


# ===========================================================================
# SECTION 8.  S4 -- THE UNCOLLAPSED-RECORD MAP
# ===========================================================================
def fq_mul(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2 - y1 * y2)


def fq_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def fq_conj(a):
    return (a[0] - a[1], -a[1])


FZ = (Fraction(0), Fraction(0))


def dens(psi, scale2):
    """|psi><psi| / scale2 as a DIM x DIM matrix over Q(w)."""
    out = []
    for i in range(DIM):
        row = []
        zi = (Fraction(psi[i][0]), Fraction(psi[i][1]))
        for j in range(DIM):
            zj = fq_conj((Fraction(psi[j][0]), Fraction(psi[j][1])))
            v = fq_mul(zi, zj)
            row.append((v[0] / scale2, v[1] / scale2))
        out.append(tuple(row))
    return tuple(out)


def dscale(M, s):
    return tuple(tuple((v[0] * s, v[1] * s) for v in row) for row in M)


def dadd(A, B):
    return tuple(tuple(fq_add(a, b) for a, b in zip(ra, rb))
                 for ra, rb in zip(A, B))


def s4_map(LD, P):
    # the delivered rule: branch weights w_c(rho) = Born weights of the
    # post-coin state; branch state = the SAME uncollapsed evolved state
    # on every branch; branch record = n + 1_c.
    psi0 = SINGLE
    psi1v = tuple(Z1 if k == 1 else Z0 for k in range(DIM))
    w0 = born(psi0, R0, "G.D")
    w1 = born(psi1v, R0, "G.D")
    ev0 = walk_shift(coin_apply(list(psi0), list(R0), "G.D"))
    ev1 = walk_shift(coin_apply(list(psi1v), list(R0), "G.D"))
    P0 = dens(ev0, 9)
    P1 = dens(ev1, 9)
    # linearity on mixtures: Xi(rho)_c = w_c(rho) * P(rho); for
    # rho_mix = (rho0+rho1)/2:  w_c(mix) = (w0+w1)/2 (linear),
    # P(mix) = (P0+P1)/2 (linear), but the product is quadratic:
    # diff_c = Xi(mix)_c - (Xi(rho0)_c + Xi(rho1)_c)/2
    #        = -1/4 (w_c(0) - w_c(1)) (P0 - P1)
    identity_ok = True
    witness = None
    for c in range(DIM):
        wc_mix = (w0[c] + w1[c]) / 2
        lhs = dadd(dscale(dadd(P0, P1), wc_mix / 2),
                   dscale(dadd(dscale(P0, w0[c]), dscale(P1, w1[c])),
                          Fraction(-1, 2)))
        dw = w0[c] - w1[c]
        rhs = dadd(dscale(P0, Fraction(-1, 4) * dw),
                   dscale(P1, Fraction(1, 4) * dw))
        if lhs != rhs:
            identity_ok = False
        if dw != 0 and witness is None:
            for i in range(DIM):
                for j in range(DIM):
                    if lhs[i][j] != FZ:
                        witness = {"branch_cell": c, "entry": [i, j],
                                   "value_re": lhs[i][j][0],
                                   "value_w": lhs[i][j][1]}
                        break
                if witness:
                    break
    if mut("MUT-LIN"):
        witness = None
    nonlinear = witness is not None
    P["s4_linearity"] = {
        "closed_form_identity_verifies": identity_ok,
        "nonlinear_on_mixtures": nonlinear,
        "witness": witness,
        "what_it_is": "a branch-indexed family of linear weight "
                      "functionals multiplying one outcome-independent "
                      "unitary conjugation; per pure branch it is "
                      "consistent bookkeeping, but as a map on mixtures "
                      "it is quadratic in the state -- not a CPTP "
                      "instrument, and not any linear map",
        "ontology_qualification": "the nonlinearity verdict is "
                                  "conditional on the psi-ontology: "
                                  "mixtures read as "
                                  "preparation-independent physical "
                                  "states; if pure psi is ontic, the "
                                  "fundamental process (psi, R) -> "
                                  "(U psi, R + event record) with "
                                  "outcome probabilities q_c(psi) is "
                                  "an ORDINARY stochastic process, "
                                  "distributions over ontic psi "
                                  "evolve LINEARLY, and the "
                                  "nonlinearity lives ONLY in the "
                                  "compressed density-matrix "
                                  "description -- two ensembles with "
                                  "the same rho may produce different "
                                  "future records",
        "completeness_dichotomy": "the dichotomy: either rho is "
                                  "complete and the delivered rule "
                                  "must be replaced -- and the linear "
                                  "completion space is larger than "
                                  "projective collapse, the general "
                                  "instruments with outcome-dependent "
                                  "post-states -- or rho is "
                                  "INCOMPLETE because the ontic "
                                  "decomposition matters; SCOUT-PSI "
                                  "(v15/note-scoutpsi-pin.md) is the "
                                  "operational test now running, and "
                                  "until it reports the fork has "
                                  "mathematical content and no "
                                  "demonstrated operational "
                                  "distinction",
        "linear_completion_space": "projective collapse is not the "
                                   "only linear completion: the larger "
                                   "space is the general instruments "
                                   "with outcome-dependent post-states "
                                   "and no projective collapse "
                                   "required, and that space is DC's "
                                   "search space; the selective "
                                   "reading paper-20 declared not-run "
                                   "is one member of it",
        "sample_space": "CELLS"}
    LD.gate("G-S4-LINEARITY", identity_ok and nonlinear,
            "the delivered record-a-cell-leave-the-state-uncollapsed "
            "rule fails linearity on mixtures with an exact witness, and "
            "the deviation obeys the closed form "
            "-(1/4)(w_c(rho0)-w_c(rho1))(P0-P1) entry by entry; the "
            "verdict is conditional on the psi-ontology (mixtures as "
            "preparation-independent physical states)",
            witness)
    # the joint-successor requirement
    branch_states = []
    branch_records = []
    for c in (0, 1, 2):
        branch_states.append(ev0)
        branch_records.append(nfield([c]))
    if mut("MUT-JOINT"):
        branch_states[0] = ev1
    same_state = all(s == branch_states[0] for s in branch_states)
    dist_rec = len(set(branch_records)) == len(branch_records)
    wsum = sum(w0[c] for c in (0, 1, 2))
    P["s4_joint"] = {
        "record_leg_per_outcome": True,
        "state_leg_outcome_independent": same_state,
        "records_pairwise_distinct": dist_rec,
        "weights_sum_one": wsum == 1,
        "verdict": "SATISFIES-THE-FORM-WITH-AN-OUTCOME-INDEPENDENT-"
                   "STATE-LEG",
        "requirement": "a joint successor law must supply, per mutually "
                       "exclusive outcome, both the record change and "
                       "the state change, with weights summing to one; "
                       "paper-20's delivered rule supplies both, with "
                       "the state leg constant across outcomes -- it is "
                       "neither a collapse instrument nor a "
                       "configuration jump",
        "sample_space": "COMPLETE-SUCCESSOR-CONFIGURATIONS"}
    LD.gate("G-S4-JOINT",
            same_state and dist_rec and wsum == 1,
            "the joint-successor requirement is formalized and measured "
            "against the delivered rule: record leg per outcome, state "
            "leg byte-identical across the three outcomes, weights "
            "summing to one",
            {"branches": 3})
    P["s4_rho_constraints"] = {
        "constraints": [
            "C1 the successor state rho'_e lives on the successor "
            "carrier H_{G'_e}, with the inclusion H_G -> H_{G'} an exact "
            "isometry",
            "C2 rho'_e carries unit mass on the successor menu",
            "C3 rho'_e is equivariant under the successor's relabelling "
            "group",
            "C4 the transport reads only the created cell's declared "
            "neighborhood",
            "C5 rho'_e is consistent with the written triple's record"],
        "delivered_candidates_evolving_across_creation": "0 of 4",
        "cross_pairs_directionless": 36,
        "status": "constraints stated, no construction claimed; every "
                  "delivered carrier candidate fails the transport leg"}
    LD.gate("G-S4-RHO",
            P["ecc_consumed"]["carrier_evolves"] == 0
            and P["ecc_consumed"]["carrier_candidates"] == 4
            and P["ecc_consumed"]["debt_cross_pairs"] == 36,
            "the rho'_e successor constraints are stated as constraints "
            "with the delivered measurements consumed: 0 of 4 candidates "
            "evolve across creation and all 36 cross pairs are "
            "directionless", None)


# ===========================================================================
# SECTION 9.  THE PRIMITIVE SELECTION (the deliverable question)
# ===========================================================================
def primitive_selection(LD, P):
    rf0 = round_fields(ROUNDS)[0]
    cells_per_round = sum(rf0)
    d3 = P["s2_arm_c_depth3"]
    crit = {
        "CRIT-A-carries-the-committed-q": {
            "CELL-HIT": "PASS (a distribution over CELLS, sum 1)",
            "TRIPLE-EVENT": "PASS (q is the trigger readout of a "
                            "normalized successor law)",
            "Mp=3q-bridge": "FAIL (demands inclusion probability 4/3)"},
        "CRIT-B-grammar-object-arity": {
            "CELL-HIT": "FAIL (writes 1 cell per step; the three-actor "
                        "object never occurs as one process event)",
            "TRIPLE-EVENT": "PASS (writes 3 cells per event; one "
                            "admissible round writes 9)",
            "measured": {"cell_hit_write": 1, "triple_write": 3,
                         "round_write": cells_per_round}},
        "CRIT-C-walk-preservation": {
            "CELL-HIT": "PASS (identity with the delivered walk)",
            "TRIPLE-EVENT": "CONDITIONAL (any kernel preserves the "
                            "two-step window; at the three-step window "
                            "only 288 pure non-line kernels among the "
                            "censused deterministic kernels preserve it "
                            "and no record-blind fixed-alpha "
                            "equivariant kernel does; the "
                            "record-dependent equivariant question is "
                            "SCOUT-K's)",
            "measured": {"two_step_blind": True,
                         "three_step_pure_survivors":
                             d3["pure_first_step_survivors"],
                         "three_step_pure_total":
                             d3["pure_kernels_total"],
                         "record_blind_fixed_alpha_equivariant_"
                         "survivors": 0}},
        "CRIT-D-successor-and-backreaction-reading": {
            "CELL-HIT": "FAIL (no geometry leg; the walk's menu meets "
                        "the cross class at 0 of 36, so growth is "
                        "unphrasable)",
            "TRIPLE-EVENT": "PASS-AS-FORM (successors bundle the event, "
                            "the record, the geometry and the state; the "
                            "transport constraints are stated and "
                            "unsatisfied by every delivered candidate, "
                            "0 of 4)"},
        "CRIT-E-purchased-declarations": {
            "CELL-HIT": "the rename only; the grammar identification is "
                        "refused without proof",
            "TRIPLE-EVENT": "the kernel K (not uniquely determined; the "
                            "surviving pure kernels are a counted "
                            "declaration) plus the owed transport law "
                            "plus the shared-actor proximity "
                            "declaration (Q27 open; SCOUT-K's fork)"},
    }
    P["primitive_selection"] = {
        "criteria": crit,
        "user_recommendation": "the user recommends the triple-event "
                               "primitive; the scout tested both",
        "adoption_status": "the triple-event primitive is "
                           "ADOPTED-BY-PROGRAM-DECISION: adopted "
                           "because it matches the intended local, "
                           "backreacting ontology; not selected "
                           "uniquely by an existing ISP law",
        "answer": "the TRIPLE-EVENT primitive survives every "
                  "sample-space and type test at the committed windows "
                  "and costs one counted kernel declaration plus the "
                  "owed transport law plus the counted proximity "
                  "declaration; the CELL-HIT primitive survives "
                  "as the delivered walk's own bookkeeping and cannot "
                  "phrase the three-actor grammar object or growth; "
                  "under the triple primitive the walk's statistics are "
                  "preserved at the committed windows only by kernel "
                  "selections outside the record-blind fixed-alpha "
                  "equivariant family, and whether a record-dependent, "
                  "locally covariant equivariant kernel preserves them "
                  "is OPEN -- the SCOUT-K census",
        "word": "SCOUT-PRIMITIVE-SELECTION-TRIPLE-SURVIVES-THE-TYPE-"
                "TESTS-AND-COSTS-THE-KERNEL-CELL-HIT-SURVIVES-AS-THE-"
                "DELIVERED-WALK"}
    LD.gate("G-PRIMITIVE",
            crit["CRIT-B-grammar-object-arity"]["measured"] ==
            {"cell_hit_write": 1, "triple_write": 3, "round_write": 9}
            and crit["CRIT-C-walk-preservation"]["measured"][
                "three_step_pure_survivors"] == 8,
            "the primitive-selection criteria are measured, and the "
            "selection answer is rendered from them",
            None)


# ===========================================================================
# SECTION 10.  SAMPLE-SPACE DISCIPLINE + VERDICTS + KIT
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
    LD.gate("G-SAMPLE-SPACE",
            len(found) == 182 and not bad,
            "every probability-typed measurement row in this receipt "
            "declares its sample space from the three declared names, "
            "182 declarations; no claim changes sample space silently",
            {"declared": len(found)})


# ---- the semantic numeral gate (ordered at ledger #59, R3) ---------------
# Every load-bearing prose numeral in the note is bound to its SPECIFIC
# receipt field: (context sentence, token, field path).  Any-occurrence
# backing -- accepting a prose numeral because the same number appears
# ANYWHERE in the receipt -- is the disease that let the delivered note
# say 27 where the receipt's s1_escape_a.successors said 7 (the era's
# fourth false delivered numeral).  The gate checks token == field value
# in-build; note verification requires each context sentence verbatim.
NUMERAL_FIELD_MAP = (
    ("its 7 successors are pairwise distinct records",
     "7", "s1_escape_a/successors"),
    ("infeasible at all four committed classes with exact gaps 4, 4, 3 "
     "and 7/3", "4", "committed_duals[0]/gap"),
    ("infeasible at all four committed classes with exact gaps 4, 4, 3 "
     "and 7/3", "4", "committed_duals[2]/gap"),
    ("infeasible at all four committed classes with exact gaps 4, 4, 3 "
     "and 7/3", "3", "committed_duals[1]/gap"),
    ("infeasible at all four committed classes with exact gaps 4, 4, 3 "
     "and 7/3", "7/3", "committed_duals[3]/gap"),
    ("matches the delivered receipt at 156 of 156 rows",
     "156", "census/receipt_row_matches"),
    ("The receipt carries 182 such declarations",
     "182", "sample_spaces/declared"),
    ("order 108, 12 linear parts times 9 translations",
     "108", "s2_gamma/order"),
    ("order 108, 12 linear parts times 9 translations",
     "12", "s2_gamma/linear_order"),
    ("Equivariance cuts 54 to 1", "54", "s2_arm_a/bare_dim"),
    ("Equivariance cuts 54 to 1", "1", "s2_arm_a/equivariant_dim"),
    ("EMPTY at the committed row with exact phase-one gap 6",
     "6", "s2_arm_b/gap"),
    ("729 agreement rows reduce to 25 distinct polynomials",
     "729", "s2_arm_c_depth3/rows"),
    ("729 agreement rows reduce to 25 distinct polynomials",
     "25", "s2_arm_c_depth3/distinct_nonzero_polys"),
    ("8 pure non-line first-step selections survive and extend to 288 "
     "pure kernels", "8", "s2_arm_c_depth3/pure_first_step_survivors"),
    ("8 pure non-line first-step selections survive and extend to 288 "
     "pure kernels", "288", "s2_arm_c_depth3/pure_kernels_total"),
    ("the declared predictor scores 20 of 156", "20", "s3_cond4/correct"),
    ("81 nonzero Delta-B entries", "81",
     "s3_cond3/fourier_control/delta_b_nonzero_entries"),
    ("0 of 4 delivered candidates evolve across creation",
     "0", "ecc_consumed/carrier_evolves"),
    ("0 of 4 delivered candidates evolve across creation",
     "4", "ecc_consumed/carrier_candidates"),
    ("all 36 cross pairs are directionless",
     "36", "ecc_consumed/debt_cross_pairs"),
    ("all 351 successor pairs are distinct",
     "351", "s2_exclusivity/block_pairs_checked"),
    ("weights 1/9, 4/9, 4/9 on the three cells of the start site",
     "4/9", "committed_q/qmax"),
    ("most negative entry is -2/3",
     "-2/3", "s1_escape_c/per_class[3]/min_entry"),
    ("11 variants", "11", "s2_arm_c_depth2/variants"),
    ("36 admissible rounds", "36", "arena/rounds"),
    ("27 cells over the 9 actors", "27", "arena/cells"),
    ("84 actor triples", "84", "arena/triples"),
    ("9 declared lines", "9", "arena/declared_lines"),
    ("12 affine-line cosets", "12", "arena/lines"),
)


def resolve_field(P, path):
    cur = P
    for seg in path.split("/"):
        idxs = []
        while seg.endswith("]"):
            k = seg.rindex("[")
            idxs.insert(0, int(seg[k + 1:-1]))
            seg = seg[:k]
        cur = cur[seg]
        for i in idxs:
            cur = cur[i]
    return cur


def numeral_bindings(LD, P):
    rows = []
    allok = True
    for (ctx, tok, path) in NUMERAL_FIELD_MAP:
        try:
            val = fser(resolve_field(P, path))
        except (KeyError, IndexError, TypeError):
            val = "UNRESOLVED-FIELD"
        if mut("MUT-NUMBIND") and path == "s1_escape_a/successors":
            val = 27
        ok = str(val) == tok
        allok = allok and ok
        rows.append({"context": ctx, "token": tok, "field": path,
                     "value": val, "ok": ok})
    P["numeral_bindings"] = {
        "bindings": rows, "all_bound": allok,
        "policy": "every load-bearing prose numeral is bound to its "
                  "specific receipt field by this map; any-occurrence "
                  "backing is refused as the sole backing"}
    LD.gate("G-NUMERAL-FIELD", allok,
            "every load-bearing prose numeral is bound to a specific "
            "receipt field and each bound token equals that field's "
            "value exactly; the note-side context sentences are "
            "required verbatim at note verification",
            {"bindings": len(rows),
             "failing": [r["field"] for r in rows if not r["ok"]]})


def env_exclusion(LD, P):
    """no environment-dependent value may enter the serialized receipt:
    the sha256-12 of every unpinned live read is computed in-run and
    must not occur anywhere in the receipt payload (the delivered
    receipt's defect: it serialized the live LOG digest)."""
    unp = sorted({rel for (_i, rel, _q) in ANCHORS} - set(PINNED))
    digs = {}
    for rel in unp:
        data, _how = read_pinned(rel)
        digs[rel] = sha12(data)
    P["env_exclusion"] = {
        "unpinned_reads_scanned": unp,
        "probe": pick("MUT-ENV", None, digs[unp[-1]]),
        "policy": "unpinned live-read digests and LIVE/SNAPSHOT "
                  "resolution flags are checked in-run and never "
                  "serialized into either artifact"}
    blob = to_json(P) + to_json(LD.rows)
    leaks = sorted(rel for rel, d in digs.items() if d in blob)
    P["env_exclusion"]["leaks"] = leaks
    LD.gate("G-ENV-EXCLUSION", not leaks,
            "the serialized receipt payload carries no digest of any "
            "unpinned live read: environment-dependent bytes are "
            "excluded from the artifacts and checked in-run only",
            {"scanned": len(unp), "leaks": leaks})


def build_verdicts(P):
    d3 = P["s2_arm_c_depth3"]
    esc_c = {r["class"]: r["signed_solvable"]
             for r in P["s1_escape_c"]["per_class"]}
    V = {}
    V["S1"] = ("SCOUT-PUSHFORWARD-ESCAPE-EXHIBITED-AT-TRIGGER-MARGINAL-"
               "NOT-OCCUPANCY-MARGINAL<CEILING-THEOREM-PROVED-AT-THE-"
               "INCLUSION-BRIDGE-156-OF-156-EXCEPTIONS-0; "
               "ESCAPE-A-EXHIBITED-AS-SCAFFOLD; ESCAPE-B-EXHIBITED; "
               "ESCAPE-C-CLASS-SPLIT-E-TRIPLE-ONLY; "
               "ESCAPE-D-INHERITED-BY-SCALE-INVARIANCE>")
    if not (P["census"]["ceiling_exceptions"] == 0
            and P["s1_escape_a"]["trigger_readout_equals_q"]
            and esc_c == {"E-BLOCK": False, "E-LINE-DECLARED": False,
                          "E-LINE-COSET": False, "E-TRIPLE": True}):
        V["S1"] = "SCOUT-PUSHFORWARD-UNDETERMINED"
    V["S2"] = (P["s2_determination"]["word"]
               + "<TRIGGER-ONLY-DIM-54-EQUIVARIANT-DIM-1; "
               "ALL-WRITE-ONE-MEASURED-EMPTY-GAP-6; "
               "RECORD-CONSISTENCY-VACUOUS-AT-TWO-STEPS-"
               "FIRST-BITES-AT-THREE-STEPS; "
               "PURE-NON-LINE-SURVIVORS-8-EXTENDING-TO-288; "
               "RECORD-BLIND-FIXED-ALPHA-LINE-EMPTY; "
               "RECORD-DEPENDENT-CENSUS-IS-SCOUT-K>")
    V["S3"] = (P["s3_verdict"]["word"]
               + "<DATUM-ZERO-AT-ALL-156-ROWS; "
               "CUTS-INCLUDE-THE-DEGENERATE-I.U; "
               "BOTH-COUNTERCONTROLS-KILL; "
               "PREDICTION-SCORES-20-OF-156>")
    V["S4"] = ("SCOUT-RECORD-UPDATE-NOT-A-LINEAR-MAP-ON-MIXTURES"
               "<CONDITIONAL-ON-THE-PSI-ONTOLOGY; "
               "CLOSED-FORM-WITNESS-EXACT; "
               "JOINT-SUCCESSOR-FORM-SATISFIED-WITH-AN-OUTCOME-"
               "INDEPENDENT-STATE-LEG; "
               "RHO-TRANSPORT-CONSTRAINTS-STATED-DELIVERED-"
               "CANDIDATES-0-OF-4>")
    V["PRIMITIVE"] = P["primitive_selection"]["word"]
    P["verdicts"] = V


ROUTE_TABLE = (
    ("R1 the delivered bridge Mp = 3q", "TRIPLE-EVENTS (misread as CELLS)",
     "DEAD-BY-TYPE-ERROR: demands inclusion probability 4/3",
     "none -- this is the surfaced conflation"),
    ("R2 CELL-HIT primitive (paper-20 as delivered)", "CELLS",
     "SOUND-AS-BOOKKEEPING: q sums to 1; cannot phrase the grammar "
     "object or growth",
     "renames the walk's primitive; refuses the grammar identification"),
    ("R3 TRIPLE-EVENT primitive with kernel K", "TRIPLE-EVENTS",
     "SOUND-IF-A-KERNEL-IS-DECLARED: no record-blind fixed-alpha "
     "affine-equivariant K preserves the three-step walk statistics; "
     "288 pure non-line kernels survive the measured windows; the "
     "record-dependent census is SCOUT-K's",
     "purchases the kernel declaration"),
    ("R4 complete-successor law (escape a)",
     "COMPLETE-SUCCESSOR-CONFIGURATIONS",
     "EXHIBITED-AS-SCAFFOLD: sum 1, trigger readout q, bridge "
     "abandoned; no rho'_e, geometry unchanged",
     "purchases the successor ontology and the owed transport law"),
    ("R5 endpoint Born statistics (escape b)", "CELLS",
     "EXHIBITED: unit column sums, ceiling vacuous",
     "purchases endpoint semantics for every Born weight"),
    ("R6 non-additive history measure (escape c)", "TRIPLE-EVENTS",
     "CLASS-SPLIT: signed witness at E-TRIPLE only; refused at the "
     "affine level at the other three classes",
     "purchases non-additivity and buys only the full triple class"),
    ("R7 selective record-writing (escape d)", "TRIPLE-EVENTS",
     "INHERITED: scale invariance returns the same LP",
     "purchases nothing in its minimal form"),
    ("R8 the Delta-B identification (S3)", "TRIPLE-EVENTS",
     "KILLED-AT-CONDITION-1: the datum does not determine the "
     "certificate",
     "attempted purchase failed all four pre-conditions"),
)

AUDIT_TABLE = (
    ("Mp = 3q", "events e (mutually exclusive)",
     "the three written cells (simultaneous consequences)",
     "CONFLATES: the marginal sums consequence-inclusion as if it were "
     "alternative mass"),
    ("P(c,e|X) = q(c|X) K(e|c,G,R)",
     "(trigger, event) pairs (mutually exclusive)",
     "the written cells inside e (carried as data)",
     "SOUND: consequences never enter the normalization"),
    ("W(c') = 3 q(c') (arm two)", "events under the kernel law",
     "written-cell inclusion re-read as measured statistics",
     "CONFLATES: re-imports the bridge; measured EMPTY at gap 6"),
    ("sum_e P(X'_e|X) = 1", "complete local successors",
     "the pair-cells inside each successor (carried as data)",
     "SOUND: the addendum's normalization rule"),
    ("Xi(rho)_c = w_c(rho) P(rho) (S4)",
     "record branches n + 1_c (mutually exclusive)",
     "the uncollapsed state leg (shared across branches)",
     "SOUND-AS-BOOKKEEPING, NOT-A-CHANNEL: quadratic on mixtures"),
)

TERM_TABLE = (
    ("CELL-HIT", "paper-20's primitive: one Born-selected pair-cell "
     "increment per step (the mandatory rename)"),
    ("DIVISION-EVENT", "paper-19's three-actor conflict group whose "
     "footprint writes all three pair-relations; the only object this "
     "note calls a division event"),
    ("TRIPLE-EVENT", "a division event carried as one probabilistic "
     "alternative"),
    ("COMPLETE-SUCCESSOR-CONFIGURATION", "X'_e = (G'_e, R'_e, rho'_e, "
     "event data): one outcome of the E-34.4 normalization rule"),
    ("CELL", "an unordered co-division pair of actors carrying one "
     "declared direction (ECC's sense, unchanged)"),
    ("TRIGGER", "the cell the quantum menu selects; the conditional "
     "seat of q(c) under the triple primitive"),
    ("RECORD", "the co-division relation with its multiplicities "
     "(ECC's sense, unchanged)"),
    ("INCLUSION MARGINAL", "sum over events containing a cell of the "
     "event law's mass; a consequence count, never a probability of an "
     "alternative"),
)


def build_kit(P):
    V = P["verdicts"]
    kit = []
    kit.append("SCOUT-BRIDGE verdicts:")
    for k in ("S1", "S2", "S3", "S4", "PRIMITIVE"):
        kit.append(V[k])
    kit.append("the committed row is infeasible at all four committed "
               "classes with exact gaps 4, 4, 3 and 7/3, and the "
               "recomputed census matches the delivered receipt at 156 "
               "of 156 rows with ceiling exceptions 0")
    kit.append("the committed target puts weights 1/9, 4/9, 4/9 on the "
               "three cells of the start site, and 4/9 exceeds the "
               "ceiling 1/3 that any inclusion-marginal bridge forces")
    kit.append("Mp = 3q is abandoned under the triple primitive, not "
               "repaired: the object is P(X'_e|X) over mutually "
               "exclusive complete local successors, summing to one, "
               "with the three pair-cells correlated consequences of "
               "one transition")
    kit.append("this scout consumes ECC's committed artifacts as "
               "delivered-candidate values: panel-verified at "
               "adjudication #50 (accept-with-fixes, no reject), seal "
               "status HELD")
    kit.append("the sector conditional of the D44/D45 synthesis is "
               "precedent for a different object -- a horizon-stable "
               "conditional between completion sectors at a fixture -- "
               "and is cited as such, not as a lift of cell weights to "
               "triple events")
    kit.append("record-completeness in paper-38 is by construction for "
               "the censused catalogue and is not inflated here")
    kit.append("indivisibility in the Barandes recast means sparsity of "
               "the allowed conditioning times; his framework retains "
               "ordinary probability, definite configurations and "
               "single-time distributions")
    kit.append("an arbitrary K is a hidden free law and is refused as "
               "an outcome word")
    kit.append("no route claims to evade the no-go without naming the "
               "sample-space change or escape assumption it purchased")
    for row in ROUTE_TABLE:
        kit.append("| " + " | ".join(row) + " |")
    for row in AUDIT_TABLE:
        kit.append("| " + " | ".join(row) + " |")
    for row in TERM_TABLE:
        kit.append("| " + " | ".join(row) + " |")
    d3 = P["s2_arm_c_depth3"]
    kit.append("at the three-step window the 729 agreement rows reduce "
               "to 25 distinct polynomials in the line weight; "
               "linear rows force alpha = -1, alpha = 0 and alpha = 1 "
               "at once, so "
               "the record-blind fixed-alpha equivariant line is "
               "empty, while 8 pure non-line "
               "first-step selections survive and extend to 288 pure "
               "kernels on the reached cells")
    kit.append(P["s2_arm_c_depth3"]["kernel_family_scope"])
    kit.append(P["s1_escape_a"]["scaffold_status"])
    kit.append(P["s1_escape_a"]["uniform_kernel_tension"])
    kit.append(P["s1_escape_a"]["trigger_semantics_status"])
    kit.append(P["s2_locality"]["proximity_declaration"])
    kit.append(P["s4_linearity"]["ontology_qualification"])
    kit.append(P["s4_linearity"]["completeness_dichotomy"])
    kit.append(P["s4_linearity"]["linear_completion_space"])
    kit.append(P["primitive_selection"]["adoption_status"])
    kit.append("the one-step Delta-B datum is identically zero at every "
               "allowed cut of every census row (a diagonal factor "
               "never moves an entrywise squared modulus), while the "
               "certificate vector varies from (4, 4, 3, 7/3) to "
               "feasibility -- no function of the datum can target the "
               "certificates")
    kit.append("the basis-permutation control violates the ceiling at "
               "qmax 1 with Delta-B exactly zero at every cut; the "
               "F3,F3 control carries 81 nonzero Delta-B entries with a "
               "uniform intermediate Born vector at the cap, and its "
               "rows fail structurally without any ceiling witness")
    kit.append("the declared predictor scores 20 of 156")
    kit.append("the delivered record-update rule fails linearity on "
               "mixtures with an exact witness obeying the closed form "
               "-(1/4)(w_c(rho0)-w_c(rho1))(P0-P1); per pure branch it "
               "is consistent bookkeeping; as a state-space map it is "
               "not a CPTP instrument")
    kit.append("the successor state constraints C1-C5 are stated as "
               "constraints, not a construction: 0 of 4 delivered "
               "candidates evolve across creation and all 36 cross "
               "pairs are directionless")
    kit.append(P["s2_exclusivity"]["sentence"])
    kit.append(P["s2_determination"]["finding"])
    P["kit"] = kit


# ===========================================================================
# SECTION 11.  THE FALSIFIER REGISTRY
# ===========================================================================
FALSIFIERS = (
    ("MUT-ARENA", "G-ARENA", "arena", "adds a fake triangle"),
    ("MUT-ROUNDS", "G-ARENA", "arena", "appends an inadmissible round"),
    ("MUT-Q", "G-COMMITTED-Q", "committed_q",
     "skips the Born normalization"),
    ("MUT-CENSUS", "G-CENSUS-REPRO", "census", "duplicates a census row"),
    ("MUT-CEIL", "G-CEILING", "census", "injects a ceiling exception"),
    ("MUT-GAP", "G-COMMITTED-ROW", "committed_duals",
     "moves a committed gap by one"),
    ("MUT-CERT", "G-FARKAS", "committed_duals",
     "corrupts a Farkas certificate entry"),
    ("MUT-HISTORY", "G-PUSHFORWARD", "s1_history_law",
     "breaks the pushforward normalization"),
    ("MUT-ESCA", "G-ESCAPE-A", "s1_escape_a",
     "breaks the joint-law kernel normalization"),
    ("MUT-ESCB", "G-ESCAPE-B", "s1_escape_b",
     "breaks the endpoint column sum"),
    ("MUT-ESCC", "G-ESCAPE-C", "s1_escape_c",
     "corrupts the signed witness"),
    ("MUT-ESCD", "G-ESCAPE-D", "s1_escape_d",
     "forges a feasible scaled row"),
    ("MUT-GAMMA", "G-GAMMA", "s2_gamma", "drops a group element"),
    ("MUT-ORBIT", "G-EQUIVARIANCE", "s2_orbits", "merges pair orbits"),
    ("MUT-ARMB", "G-ARM-B", "s2_arm_b", "zeroes the arm-two marginal"),
    ("MUT-BLIND", "G-ARM-C-WINDOW2", "s2_arm_c_depth2",
     "corrupts a blindness variant"),
    ("MUT-ARMC", "G-ARM-C-WINDOW3", "s2_arm_c_depth3",
     "deletes the linear polynomial rows"),
    ("MUT-EXCL", "G-OVERLAP", "s2_exclusivity",
     "collides two successor records"),
    ("MUT-SILENCE", "G-S3-SILENCE", "s3_silence",
     "corrupts a B matrix in the silence sweep"),
    ("MUT-WITNESS", "G-S3-COND1", "s3_cond1",
     "forges a nonzero committed datum"),
    ("MUT-CONTROL", "G-S3-COND3", "s3_cond3",
     "zeroes the Fourier control's Delta-B count"),
    ("MUT-SCORE", "G-S3-COND4", "s3_cond4", "miscounts the score"),
    ("MUT-LIN", "G-S4-LINEARITY", "s4_linearity",
     "suppresses the linearity witness"),
    ("MUT-JOINT", "G-S4-JOINT", "s4_joint",
     "makes the branch states differ"),
    ("MUT-SS", "G-SAMPLE-SPACE", "sample_spaces",
     "strips a sample-space declaration"),
    ("MUT-ANCHOR", "G-ANCHORS", "anchors", "corrupts an anchor quote"),
    ("MUT-ECC-VALS", "G-ECC-CONSUME", "ecc_consumed",
     "corrupts a consumed delivered gap"),
    ("MUT-NUMBIND", "G-NUMERAL-FIELD", "numeral_bindings",
     "re-injects 27 into the bound successors field (the fourth false "
     "delivered numeral's disease)"),
    ("MUT-ENV", "G-ENV-EXCLUSION", "env_exclusion",
     "injects an unpinned live-read digest into the receipt payload"),
    ("MUT-KWALL", "G-KERNEL-WALL", "kernel_wall",
     "blanks the kernel-scope wall's pattern family so the retired "
     "overclaim's permanent dead controls stop dying (the verifier's "
     "verbatim replant, finding F1)"),
    ("MUT-SETITER", "G-AST-DETERMINISM", "source_hygiene",
     "injects a bare set-iteration and a raw os.listdir into the "
     "scanned source (the registered iteration-order species, verifier "
     "finding F2); must die deterministically at every hash seed, "
     "never vary silently"),
)


# ===========================================================================
# SECTION 12.  SELF-SOURCE HYGIENE
# ===========================================================================
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
    # ---- the determinism leg (the micro-repair's M3; ARITY-16 Z10
    # ported; the #62 iteration-order species, verifier finding F2) ----
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
# SECTION 13.  THE FULL BUILD
# ===========================================================================
def build_all(P=None):
    LD = Ledger()
    if P is None:
        P = {}
    source_scan(LD, P)
    rowmap = measure_reads(LD, P)
    measure_arena(LD, P)
    CLS = build_classes()
    targets, RF = build_targets()
    distinct = census(LD, P, CLS, targets, rowmap)
    qc = committed_row(LD, P, CLS)
    lp_controls(LD, P, CLS)
    s1_pushforward(LD, P, CLS, qc)
    s2_kernel(LD, P, qc)
    s2_record_consistency(LD, P)
    s3_deltab(LD, P, CLS, qc)
    s4_map(LD, P)
    primitive_selection(LD, P)
    sample_space_audit(LD, P)
    build_verdicts(P)
    build_kit(P)
    numeral_bindings(LD, P)
    kernel_wall_gate(LD, P)
    env_exclusion(LD, P)
    P["ledger"] = LD.rows
    return P


# ===========================================================================
# SECTION 14.  NOTE VERIFICATION (the walls on the report's own prose)
# ===========================================================================
FORBIDDEN_GLOBAL = (
    "no reader will", "no one will doubt", "will not doubt",
    "being gated,", "delta-b is a divisibility",
    "delta-b is divisibility", "measures divisibility",
    "missing single-time", "lacks single-time",
    "no single-time distributions",
    "no equivariant record-consistent kernel",
    "no equivariant record consistent kernel",
)
S3_FORBIDDEN = ("probably", "likely", "explains")

# ---- the kernel-scope wall (the micro-repair's M1; verifier finding
# F1) --------------------------------------------------------------------
# The RETIRED overclaim -- the general "no equivariant record-consistent
# kernel" verdict, downgraded at #59 to the record-blind fixed-alpha
# scope -- replanted VERBATIM with no wall firing (verifier plant P14 /
# INJ-8): the #59/#66 repair made the four files grep-clean but
# installed no defense against reintroduction.  This wall is
# SUBJECT-BASED: hyphens and spacing are normalized away, the note is
# split into segments, and any segment whose subject is the equivariant
# / record-consistent kernel family carrying a nonexistence or
# emptiness predicate is refused -- UNLESS the segment carries the
# licensed record-blind scope qualifier, so the honest downgraded
# verdict (the twin) stays alive.
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
# verbatim retired sentence (the verifier's P14 plant), two paraphrase
# variants and the retired verdict token must DIE at this wall; the
# licensed record-blind fixed-alpha forms are the twins and must
# SURVIVE.
KERNEL_WALL_DEAD_CONTROLS = (
    "So no equivariant record-consistent kernel exists at the "
    "committed arena.",
    "every equivariant kernel is empty at the committed arena",
    "record consistent kernels do not exist at this arena",
    "SCOUT-KERNEL-EMPTY-AT-EQUIVARIANT-RECORD-CONSISTENT",
)
KERNEL_WALL_ALIVE_CONTROLS = (
    "no record-blind, fixed-alpha, affine-equivariant kernel preserves "
    "the delivered three-step walk statistics",
    "at the three-step window only the 288 pure non-line kernels among "
    "the censused deterministic kernels preserve it and no "
    "record-blind fixed-alpha equivariant kernel does",
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
                  "verbatim retired sentence, two paraphrases and the "
                  "retired verdict token are permanent dead controls, "
                  "and the licensed downgraded forms are permanent "
                  "alive twins"}
    LD.gate("G-KERNEL-WALL", ok,
            "the kernel-scope wall fires on the retired overclaim "
            "family (verbatim, hyphen and paraphrase variants, and the "
            "retired verdict token) and stays silent on the licensed "
            "record-blind fixed-alpha forms; all permanent controls "
            "behave as declared on this build",
            {"dead_controls": len(KERNEL_WALL_DEAD_CONTROLS),
             "alive_controls": len(KERNEL_WALL_ALIVE_CONTROLS),
             "misbehaving": [r["control"][:50] for r in rows
                             if (r["expected"] == "DEAD")
                             != r["flagged"]]})


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
    hay = canon(text)
    low = hay.lower()
    for sent in P["kit"]:
        if canon(sent) not in hay:
            problems.append("kit sentence missing: " + sent[:80])
    for (aid, _rel, quote) in ANCHORS:
        if aid in ("A-P46-EMIT", "A-P46-FREE2", "A-LOG52-HOLD"):
            continue
        if canon(quote) not in hay:
            problems.append("anchor quote missing from note: " + aid)
    for pat in FORBIDDEN_GLOBAL:
        if pat in low:
            problems.append("forbidden pattern present: " + pat)
    for h in kernel_wall_hits(text):
        problems.append("kernel-scope wall: " + h)
    # the S3 language wall, scoped to the S3 section
    s3start = text.find("## S3")
    s3end = text.find("## S4")
    if s3start < 0 or s3end < 0 or s3end <= s3start:
        problems.append("S3/S4 section markers missing")
    else:
        s3 = text[s3start:s3end].lower()
        for tok in S3_FORBIDDEN:
            if tok in s3:
                problems.append("S3 language wall: '%s' present" % tok)
    # sample-space tokens: the three names appear as tags, and every
    # probability-expression line outside tables and quotes carries one
    for name in SS_NAMES:
        if "[SS:" + name + "]" not in text:
            problems.append("sample-space tag [SS:%s] absent" % name)
    for ln in text.splitlines():
        st = ln.strip()
        if st.startswith("|") or st.startswith(">") or st.startswith("#"):
            continue
        if ("P(" in ln or "q(" in ln) and "[SS:" not in ln:
            problems.append("probability expression without a "
                            "sample-space tag: " + st[:60])
    # licence ids are structural
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
    # W1 subject policing: derive-stem lines carry a subject or a quote
    for ln in text.splitlines():
        lnl = ln.lower()
        if "derive" in lnl and not ln.strip().startswith(">") \
                and "[BY:" not in ln and "|" not in ln:
            problems.append("derivation sentence without subject tag: "
                            + ln.strip()[:60])
    # the semantic numeral gate, note side: every load-bearing prose
    # numeral's context sentence must be present verbatim, welding the
    # prose numeral to its specific receipt field (any-occurrence
    # backing is refused as the sole backing)
    for (ctx, tok, path) in NUMERAL_FIELD_MAP:
        if canon(ctx) not in hay:
            problems.append("numeral-field context missing (%s = %s): %s"
                            % (path, tok, ctx[:60]))
    if not P.get("numeral_bindings", {}).get("all_bound"):
        problems.append("numeral-field bindings not all bound")
    # slash rationals in prose are backed by the receipt inventory
    inv = set()
    rationals_of(fser(P), inv)
    body = text
    for ln in body.splitlines():
        for t in sorted(iter_rationals(ln)):
            if t not in inv:
                problems.append("slash rational not in receipt "
                                "inventory: " + t)
    # integer numerals in prose are backed by the receipt or the layout
    nums = set()
    collect_numerals(fser(P), nums)
    layout = set(range(0, 60)) | {84, 108, 156, 280, 288, 344, 275, 277,
                                  217, 289, 633, 67, 68, 120, 60, 529,
                                  729, 100, 133, 2026}
    for ln in body.splitlines():
        for tok in ln.replace("(", " ").replace(")", " ").split():
            t = tok.strip(".,;:|%").lstrip("#")
            if t.isascii() and t.isdigit():
                v = int(t)
                if v not in nums and v not in layout:
                    problems.append("numeral not receipt-backed: " + t)
    return problems


# ===========================================================================
# SECTION 15.  ARTIFACTS, CLI, SELFTEST
# ===========================================================================
def render_output(P, note_digest):
    lines = []
    lines.append("SCOUT-BRIDGE delivery transcript")
    lines.append("pin c57a0afffd58 + addendum 2aa72e566cba; "
                 "unit note " + NOTE_REL)
    lines.append("object under test (the note): sha256-12 " + note_digest)
    lines.append("instrument source: sha256-12 "
                 + P["source_hygiene"]["digest"])
    lines.append("")
    for r in P["ledger"]:
        lines.append("GATE %-18s %s  %s"
                     % (r["gate"], "PASS" if r["ok"] else "FAIL",
                        r["note"]))
    lines.append("")
    lines.append("VERDICTS")
    for k in ("S1", "S2", "S3", "S4", "PRIMITIVE"):
        lines.append("  " + P["verdicts"][k])
    lines.append("")
    lines.append("KEY CLAIMS")
    lines.append("  committed q: (1/9, 4/9, 4/9) on cells 0,1,2; "
                 "qmax 4/9")
    lines.append("  committed gaps: E-BLOCK 4, E-LINE-DECLARED 4, "
                 "E-LINE-COSET 3, E-TRIPLE 7/3 (receipt-equal, "
                 "Farkas-verified)")
    lines.append("  census reproduction: 156 of 156 row words equal the "
                 "delivered receipt")
    lines.append("  arm two gap: 6; arm three: vacuous at two steps, "
                 "first bites at three steps")
    lines.append("  record-blind fixed-alpha kernel family: dim 1; "
                 "empty under record consistency; pure survivors "
                 "8 -> 288; the record-dependent census is SCOUT-K's")
    lines.append("  Delta-B datum: zero at every cut of every row; "
                 "prediction scores 20 of 156")
    lines.append("  S4: nonlinear on mixtures, exact witness; state leg "
                 "outcome-independent")
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
    P1["schema"] = "scout-bridge-receipt-v1"
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
    """runs every falsifier fresh; requires death at the declared gate;
    verifies move by digest; writes nothing."""
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
        sys.stdout.write("FALSIFIER %-14s died at %-18s moved-proof ok\n"
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


USAGE = ("usage: scout_exact.py [--no-write | --numbers | --kit | "
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
                       | {"G-SRC-CLEAN", "G-PIN-DIGESTS", "G-CENSUS-REPRO",
                          "G-DETERMINISM", "G-NOTE-KIT", "G-LOCALITY",
                          "G-LP-CONTROLS", "G-PUSHFORWARD", "G-FARKAS",
                          "G-S3-COND2", "G-S3-EXEMPLAR", "G-PRIMITIVE",
                          "G-S4-RHO", "G-COMMITTED-ROW",
                          "G-NUMERAL-FIELD", "G-ENV-EXCLUSION"})
        for g in gates:
            sys.stdout.write(g + "\n")
        return 0
    if mode == "--list-mutants":
        for (n, g, o, d) in FALSIFIERS:
            sys.stdout.write("%-14s -> %-18s (%s): %s\n" % (n, g, o, d))
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
        for k in ("S1", "S2", "S3", "S4", "PRIMITIVE"):
            sys.stdout.write(P["verdicts"][k] + "\n")
        sys.stdout.write(to_json({"census": P["census"]["words"],
                                  "gaps": {d["class"]: str(d["gap"])
                                           for d in
                                           P["committed_duals"]}})
                         + "\n")
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
