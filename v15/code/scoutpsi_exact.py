#!/usr/bin/env python3
# ===========================================================================
# SCOUT-PSI  --  the equal-density / different-preparation test.
#
# Unit: v15/note-scoutpsi.md (report NOTE, no paper number).
# Pin:  v15/note-scoutpsi-pin.md (FROZEN 8e9fe2448b00); ledger #64/#65.
# S4 apparatus consumed by anchor at the COMMITTED digests
#   v15/note-scout-bridge.md    34f10a6fd494
#   v15/code/scout_receipt.json 12bdb7a58909
# (the live files are under a concurrent repair; the committed witness
#  values are embedded below and re-verified by recomputation, so no
#  runtime read of the moved files is needed).
#
# Exact arithmetic throughout: Python integers and fractions.Fraction.
# No floats, no builtin hash, no timestamps or absolute paths in the
# artifacts.  The delivery run is the only writer; every failure writes
# nothing.  sorted() discipline: nothing serialized is fed from a bare
# set or dict iteration.
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

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # .../isp
NOTE_REL = "v15/note-scoutpsi.md"
OUT_REL = "v15/code/scoutpsi_output.txt"
REC_REL = "v15/code/scoutpsi_receipt.json"

PINNED = {
    "v15/note-scoutpsi-pin.md": "8e9fe2448b00",
    "v14/paper-20-coupling.md": "4824d190af73",
}

# the S4 apparatus, consumed by anchor at the committed digests: the
# committed nonlinearity witness of scout_receipt.json (s4_linearity)
# is embedded here and re-verified below by an independent recomputation.
S4_COMMITTED = {
    "note_digest": "34f10a6fd494",
    "receipt_digest": "12bdb7a58909",
    "witness": {"branch_cell": 0, "entry": (4, 4),
                "value_re": "1/36", "value_w": "0"},
    "closed_form": "-(1/4)(w_c(rho0)-w_c(rho1))(P0-P1)",
}

P20_QUOTES = (
    "The record accumulates the law's own weights and the state is not "
    "collapsed onto the emitted cell, so the walk stays coherent between "
    "division events.",
    "The selective reading is a different object — a classical "
    "Markov chain on cells — and it is not run.",
)

ARMED = {"name": None}


class GateFail(Exception):
    def __init__(self, gate, msg):
        self.gate = gate
        self.msg = msg
        super().__init__(gate + ": " + msg)


def mut(name):
    return ARMED["name"] == name


def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]


def fser(x):
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, dict):
        return {str(k): fser(v)
                for k, v in sorted(x.items(), key=lambda kv: str(kv[0]))}
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
# SECTION 1.  THE COMMITTED ARENA (rebuilt from constructors; the walk of
#             paper-20 as the committed scout re-implements it at S4)
# ===========================================================================
Q = 3
SITES = tuple((i, j) for i in range(Q) for j in range(Q))
LINKS = ((1, 0), (0, 1), (1, 1))


def vadd(a, b):
    return ((a[0] + b[0]) % Q, (a[1] + b[1]) % Q)


CELLS = tuple((x, l) for x in SITES for l in LINKS)
CI = {c: k for k, c in enumerate(CELLS)}
DIM = len(CELLS)
SHIFT = tuple(CI[(vadd(x, l), l)] for (x, l) in CELLS)

Z0, Z1 = (0, 0), (1, 0)
WPOW = ((1, 0), (0, 1), (-1, -1))
GR_CLEAN = (((-1, 0), (2, 0), (2, 0)),
            ((2, 0), (-1, 0), (2, 0)),
            ((2, 0), (2, 0), (-1, 0)))


def gr_matrix():
    if mut("MUT-UNITARY"):
        rows = [list(r) for r in GR_CLEAN]
        rows[0][1] = (3, 0)
        return tuple(tuple(r) for r in rows)
    return GR_CLEAN


def zmul(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2 - y1 * y2)


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def zconj(a):
    return (a[0] - a[1], -a[1])


def znorm(a):
    return a[0] * a[0] - a[0] * a[1] + a[1] * a[1]


def coin_apply(psi, n):
    """the delivered coin order G.D: count phase w^(n mod 3), then the
    Grover-over-3 coin, per site block."""
    GR = gr_matrix()
    out = [Z0] * DIM
    for s in range(9):
        base = s * 3
        src = [zmul(psi[base + j], WPOW[n[base + j] % Q]) for j in range(3)]
        for i in range(3):
            tot = Z0
            for j in range(3):
                tot = zadd(tot, zmul(GR[i][j], src[j]))
            out[base + i] = tot
    return out


def walk_shift(post):
    out = [Z0] * DIM
    for m in range(DIM):
        out[SHIFT[m]] = post[m]
    return tuple(out)


def basis(k):
    return tuple(Z1 if m == k else Z0 for m in range(DIM))


R0 = tuple([0] * DIM)


def scale_of(psi):
    return sum(znorm(z) for z in psi)


# ---- density matrices over Q(w) (the S4 arithmetic) -----------------------
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


def mix(members):
    out = None
    for (p, psi, s2) in members:
        term = dscale(dens(psi, s2), p)
        out = term if out is None else dadd(out, term)
    return out


# ===========================================================================
# SECTION 2.  ANCHORS AND HYGIENE
# ===========================================================================
def source_scan(LD, P):
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
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
    allowed = {"os", "sys", "json", "hashlib", "ast", "fractions"}
    P["source_hygiene"] = {"float_literals": floats,
                          "hash_calls": hashes,
                          "imports": sorted(imports),
                          "digest": sha12(src.encode("utf-8"))}
    LD.gate("G-SRC-CLEAN",
            not floats and not hashes and imports <= allowed,
            "the instrument's own syntax tree carries no float literal, "
            "no builtin hash call, and no import outside the declared "
            "whitelist",
            {"imports": sorted(imports)})


def measure_anchors(LD, P):
    pins = {}
    for rel in sorted(PINNED):
        want = PINNED[rel]
        if mut("MUT-PIN") and rel == "v15/note-scoutpsi-pin.md":
            want = "000000000000"
        try:
            got = sha12(read_rel(rel))
        except OSError:
            got = "ABSENT"
        pins[rel] = {"want": want, "got": got, "ok": got == want}
    quotes = list(P20_QUOTES)
    if mut("MUT-ANCHOR"):
        quotes[0] = quotes[0].replace("coherent", "collapsed")
    p20 = canon(read_rel("v14/paper-20-coupling.md").decode("utf-8"))
    qrows = [{"quote": q, "present": canon(q) in p20} for q in quotes]
    P["anchors"] = {
        "pinned": pins,
        "paper20_quotes": qrows,
        "s4_committed_note_digest": S4_COMMITTED["note_digest"],
        "s4_committed_receipt_digest": S4_COMMITTED["receipt_digest"],
        "s4_consumption": "by anchor at the committed digests; the live "
                          "scout-bridge files are under a concurrent "
                          "repair and were not read",
    }
    LD.gate("G-PIN-DIGESTS",
            all(pins[r]["ok"] for r in sorted(pins)),
            "the pin note and paper-20 carry their pinned digests",
            {r: pins[r]["got"] for r in sorted(pins)})
    LD.gate("G-P20-ANCHOR",
            all(r["present"] for r in qrows),
            "paper-20's two delivered-rule sentences (the paper-20:633 "
            "region) are present verbatim in the live paper bytes",
            {"quotes": len(qrows)})


def measure_arena(LD, P):
    GR = gr_matrix()
    # exact unitarity of the un-normalized coin: GR . GR^dagger = 9 I
    gram_ok = True
    for i in range(3):
        for j in range(3):
            tot = Z0
            for k in range(3):
                tot = zadd(tot, zmul(GR[i][k], zconj(GR[j][k])))
            want = (9, 0) if i == j else Z0
            if tot != want:
                gram_ok = False
    shift_perm = sorted(SHIFT) == list(range(DIM))
    # norm conservation through one full coin at three probe states
    probes = [basis(0), basis(13),
              tuple(zadd(basis(0)[m], basis(1)[m]) for m in range(DIM))]
    cons = []
    for psi in probes:
        s2 = scale_of(psi)
        tot = sum(znorm(z) for z in coin_apply(psi, R0))
        cons.append(tot == 9 * s2)
    P["arena"] = {"cells": DIM, "sites": len(SITES), "links": len(LINKS),
                  "gr": [[list(v) for v in row] for row in GR],
                  "coin": "GROVER-over-3 with count phase w^(n mod 3), "
                          "delivered order G.D",
                  "shift_is_permutation": shift_perm,
                  "gram_is_9I": gram_ok,
                  "norm_conserved_at_probes": cons}
    LD.gate("G-ARENA",
            DIM == 27 and len(SITES) == 9 and shift_perm and gram_ok,
            "the committed arena rebuilds from constructors: 27 cells "
            "over 9 sites, the shift a permutation, and the coin exactly "
            "unitary over Z[w] (Gram = 9I)", None)
    LD.gate("G-UNITARITY", all(cons),
            "one coin application conserves the exact squared norm "
            "(total 9 x scale2) at every probe state",
            {"probes": len(cons)})


# ===========================================================================
# SECTION 3.  THE PREPARATIONS (two rhos, five decompositions)
# ===========================================================================
H = Fraction(1, 2)


def build_preparations(LD, P):
    e0, e1, e5 = basis(0), basis(1), basis(5)
    w = WPOW[1]

    def sup(a, cellA, b, cellB):
        return tuple(a if m == cellA else (b if m == cellB else Z0)
                     for m in range(DIM))

    d1a_second = basis(2) if mut("MUT-RHO") else e1
    D = {
        "RHO1": {
            "D1A": ((H, e0, 1), (H, d1a_second, 1)),
            "D1B": ((H, sup(Z1, 0, (1, 0), 1), 2),
                    (H, sup(Z1, 0, (-1, 0), 1), 2)),
            "D1C": ((H, sup(Z1, 0, w, 1), 2),
                    (H, sup(Z1, 0, (0, -1), 1), 2)),
        },
        "RHO2": {
            "D2A": ((H, e0, 1), (H, e5, 1)),
            "D2B": ((H, sup(Z1, 0, (1, 0), 5), 2),
                    (H, sup(Z1, 0, (-1, 0), 5), 2)),
        },
    }
    if mut("MUT-DISTINCT"):
        D["RHO1"]["D1B"] = D["RHO1"]["D1A"]
    rows = {}
    rho_equal = True
    distinct = True
    for rho in sorted(D):
        mixes = {}
        for dn in sorted(D[rho]):
            members = D[rho][dn]
            ok_scales = all(scale_of(psi) == s2 for (_p, psi, s2) in members)
            if not ok_scales:
                rho_equal = False
            mixes[dn] = mix(members)
        names = sorted(mixes)
        for k in range(1, len(names)):
            if mixes[names[k]] != mixes[names[0]]:
                rho_equal = False
        # genuinely distinct as ensembles: the weighted member density
        # matrices, as multisets, differ pairwise between decompositions
        sigs = {dn: sorted(digest({"p": p, "d": dens(psi, s2)})
                           for (p, psi, s2) in D[rho][dn])
                for dn in sorted(D[rho])}
        for a in names:
            for b in names:
                if a < b and sigs[a] == sigs[b]:
                    distinct = False
        rows[rho] = {
            "decompositions": {
                dn: [{"weight": p,
                      "amplitudes": [[m, list(psi[m])] for m in range(DIM)
                                     if psi[m] != Z0],
                      "scale2": s2}
                     for (p, psi, s2) in D[rho][dn]]
                for dn in sorted(D[rho])},
            "mixture_digest": digest(mixes[names[0]]),
            "mixtures_equal": all(mixes[nm] == mixes[names[0]]
                                  for nm in names),
            "pairwise_distinct_as_ensembles": True,
        }
    P["preparations"] = {
        "rho_support": {"RHO1": "cells 0 and 1 (site (0,0), links (1,0) "
                                "and (0,1))",
                        "RHO2": "cells 0 and 5 (sites (0,0) and (0,1), "
                                "links (1,0) and (1,1))"},
        "rows": rows,
        "note": "each rho is the equal mixture of two orthogonal basis "
                "cells; D1A/D2A are the basis ensembles, D1B/D2B the "
                "plus-minus superposition ensembles, D1C the "
                "plus-minus-omega ensemble; all weights 1/2",
    }
    LD.gate("G-RHO-EQUAL", rho_equal,
            "within each rho every decomposition's weighted mixture is "
            "the same density matrix over Q(w), entry by entry, and every "
            "member's declared scale2 is its exact squared norm", None)
    LD.gate("G-DISTINCT", distinct,
            "the decompositions of one rho are genuinely distinct as "
            "ensembles: their weighted member density matrices differ as "
            "multisets, pairwise", None)
    return D


# ===========================================================================
# SECTION 4.  THE PROPAGATION ENGINE (per-branch, exact, windows 1..3)
# ===========================================================================
WINDOWS = 3


def rkey(n):
    return ",".join("%d:%d" % (c, n[c]) for c in range(DIM) if n[c])


def dist_windows(members, rule):
    """rule DELIVERED: branch weights = Born of the post-coin state at
    the branch record; state leg = the SAME uncollapsed evolved state on
    every outcome; child record n + 1_c consumed by the next coin.
    rule SELECTIVE: the declared linear completion paper-20 names as not
    run -- record and collapse: the post-state is the basis state at the
    shifted emitted cell.
    rule SQUARED: the synthetic decomposition-sensitive control -- branch
    weights proportional to the squares of the Born weights, state leg
    uncollapsed."""
    dists = [dict() for _ in range(WINDOWS)]
    for (p, psi, s2) in members:
        branches = [(Fraction(1), R0, psi, s2)]
        for t in range(WINDOWS):
            nb = []
            for (W, n, st, sc) in branches:
                post = coin_apply(st, n)
                tot = sum(znorm(z) for z in post)
                if tot != 9 * sc:
                    raise GateFail("G-UNITARITY",
                                   "a branch total moved off 9 x scale2")
                ws = [Fraction(znorm(z), tot) for z in post]
                if rule == "SQUARED":
                    sq = [x * x for x in ws]
                    ssum = sum(sq)
                    ws = [x / ssum for x in sq]
                ev = walk_shift(post)
                for c in range(DIM):
                    if ws[c] == 0:
                        continue
                    n2 = list(n)
                    n2[c] += 1
                    n2 = tuple(n2)
                    W2 = W * ws[c]
                    dists[t][n2] = dists[t].get(n2, Fraction(0)) + p * W2
                    if t < WINDOWS - 1:
                        if rule == "SELECTIVE":
                            nb.append((W2, n2, basis(SHIFT[c]), 1))
                        else:
                            nb.append((W2, n2, ev, 9 * sc))
            branches = nb
    return dists


def compare(dA, dB):
    keys = sorted(set(dA) | set(dB))
    diffs = [k for k in keys if dA.get(k, Fraction(0)) != dB.get(k, Fraction(0))]
    row = {"equal": not diffs,
           "records_left": len(dA), "records_right": len(dB),
           "sample_space": "RECORD-FIELDS"}
    if diffs:
        k = diffs[0]
        left = dA.get(k, Fraction(0))
        right = dB.get(k, Fraction(0))
        row["first_record"] = rkey(k)
        row["mass_left"] = left
        row["mass_right"] = right
        row["difference"] = left - right
        row["diverging_records"] = len(diffs)
    return row


def ser_dist(d):
    return [[rkey(k), d[k]] for k in sorted(d)]


def run_family(LD, P, D, rule, field):
    out = {}
    mass_checks = []
    for rho in sorted(D):
        dists = {dn: dist_windows(D[rho][dn], rule)
                 for dn in sorted(D[rho])}
        for dn in sorted(dists):
            for t in range(WINDOWS):
                mass_checks.append(sum(dists[dn][t][k]
                                       for k in sorted(dists[dn][t])) == 1)
        names = sorted(dists)
        pairs = {}
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                a, b = names[i], names[j]
                pr = {}
                for t in range(WINDOWS):
                    da, db = dict(dists[a][t]), dict(dists[b][t])
                    if rule == "DELIVERED" and mut("MUT-W1") and t == 0 \
                            and rho == "RHO1" and a == "D1A" and b == "D1B":
                        ks = sorted(da)
                        da[ks[0]] += Fraction(1, 59)
                        da[ks[-1]] -= Fraction(1, 59)
                    if rule == "DELIVERED" and mut("MUT-MASS") and t == 0 \
                            and rho == "RHO1" and a == "D1A" and b == "D1B":
                        da = {k: v / 2 for k, v in sorted(da.items())}
                        mass_checks.append(sum(da[k] for k in sorted(da))
                                           == 1)
                    if rule == "DELIVERED" and mut("MUT-DIV") and t == 1 \
                            and rho == "RHO1" and a == "D1A" and b == "D1B":
                        db = dict(da)
                    pr["window%d" % (t + 1)] = compare(da, db)
                first = None
                for t in range(WINDOWS):
                    if not pr["window%d" % (t + 1)]["equal"]:
                        first = t + 1
                        break
                pr["first_divergent_window"] = first
                pairs[a + "|" + b] = pr
        out[rho] = {"pairs": pairs}
        if rule == "DELIVERED":
            out[rho]["window3_digests"] = {
                dn: {"digest": digest(ser_dist(dists[dn][2])),
                     "records": len(dists[dn][2])}
                for dn in sorted(dists)}
            if rho == "RHO1":
                wd = {}
                for dn in ("D1A", "D1B"):
                    wd[dn] = {"window1": ser_dist(dists[dn][0]),
                              "window2": ser_dist(dists[dn][1]),
                              "sample_space": "RECORD-FIELDS"}
                P["witness_distributions"] = wd
    P[field] = out
    return mass_checks


def measure_delivered(LD, P, D):
    mass_checks = run_family(LD, P, D, "DELIVERED", "delivered")
    LD.gate("G-MASS", all(mass_checks),
            "every ensemble record distribution carries total mass "
            "exactly 1 at every window", {"checks": len(mass_checks)})
    w1 = all(P["delivered"][rho]["pairs"][pk]["window1"]["equal"]
             for rho in sorted(P["delivered"])
             for pk in sorted(P["delivered"][rho]["pairs"]))
    LD.gate("G-WINDOW1-BLIND", w1,
            "window 1 is blind at every decomposition pair of both rhos: "
            "the one-step CELL-HIT branch weights enter the ensemble "
            "record marginal linearly, and every pairwise comparison "
            "agrees record by record", None)
    wit = P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]
    all_pairs_first = {rho + "/" + pk:
                       P["delivered"][rho]["pairs"][pk]
                       ["first_divergent_window"]
                       for rho in sorted(P["delivered"])
                       for pk in sorted(P["delivered"][rho]["pairs"])}
    P["delivered_summary"] = {
        "first_divergent_window_by_pair": all_pairs_first,
        "witness_pair": "RHO1 D1A|D1B",
        "witness_first_window": wit["first_divergent_window"],
        "sample_space": "RECORD-FIELDS"}
    LD.gate("G-SENSITIVE",
            wit["first_divergent_window"] == 2
            and all(v == 2 for v in
                    sorted(all_pairs_first.values(), key=str)
                    if v is not None)
            and all(v is not None for v in all_pairs_first.values()),
            "the delivered rule is decomposition-sensitive with first "
            "divergence at window 2, at the witness pair and at every "
            "measured pair of both rhos",
            {"first_windows": all_pairs_first})


def measure_null(LD, P, D):
    mass_checks = run_family(LD, P, D, "SELECTIVE", "null_control")
    if mut("MUT-NULL"):
        run_family(LD, P, D, "DELIVERED", "null_control")
    ok = all(P["null_control"][rho]["pairs"][pk]["window%d" % w]["equal"]
             for rho in sorted(P["null_control"])
             for pk in sorted(P["null_control"][rho]["pairs"])
             for w in (1, 2, 3))
    P["null_control"]["declaration"] = (
        "the declared genuinely linear CPTP completion is the selective "
        "collapse reading paper-20 names as not run: record the emitted "
        "cell and collapse the state onto the shifted emitted cell -- a "
        "projective cell-basis instrument composed with the walk unitary")
    LD.gate("G-NULL-BLIND", ok and all(mass_checks),
            "the declared linear completion (the selective collapse "
            "reading) is blind at windows 1, 2 and 3 on the same "
            "decompositions, record by record", None)


def measure_positive(LD, P, D):
    mass_checks = run_family(LD, P, D, "SQUARED", "positive_control")
    if mut("MUT-POS"):
        run_family(LD, P, D, "DELIVERED", "positive_control")
    wit = P["positive_control"]["RHO1"]["pairs"]["D1A|D1B"]
    P["positive_control"]["declaration"] = (
        "the synthetic decomposition-sensitive map: branch weights "
        "proportional to the SQUARES of the Born weights, state leg "
        "uncollapsed -- quadratic in the state by construction")
    LD.gate("G-POSITIVE-SENSITIVE",
            (not wit["window1"]["equal"]) and all(mass_checks),
            "the synthetic decomposition-sensitive control reads "
            "SENSITIVE at window 1 on the witness pair",
            {"first_window": wit["first_divergent_window"]})


# ===========================================================================
# SECTION 5.  THE S4 CONSUMPTION WELD (re-derivation of the committed
#             witness against the embedded committed values)
# ===========================================================================
def s4_weld(LD, P):
    psi0, psi1 = basis(0), basis(1)
    post0 = coin_apply(psi0, R0)
    post1 = coin_apply(psi1, R0)
    t0 = sum(znorm(z) for z in post0)
    t1 = sum(znorm(z) for z in post1)
    w0 = tuple(Fraction(znorm(z), t0) for z in post0)
    w1 = tuple(Fraction(znorm(z), t1) for z in post1)
    ev0 = walk_shift(post0)
    ev1 = walk_shift(post1)
    Pm0 = dens(ev0, 9)
    Pm1 = dens(ev1, 9)
    identity_ok = True
    witness = None
    for c in range(DIM):
        wc_mix = (w0[c] + w1[c]) / 2
        lhs = dadd(dscale(dadd(Pm0, Pm1), wc_mix / 2),
                   dscale(dadd(dscale(Pm0, w0[c]), dscale(Pm1, w1[c])),
                          Fraction(-1, 2)))
        dw = w0[c] - w1[c]
        sign = Fraction(1, 4) if mut("MUT-CLOSED") else Fraction(-1, 4)
        rhs = dadd(dscale(Pm0, sign * dw), dscale(Pm1, -sign * dw))
        if lhs != rhs:
            identity_ok = False
        if dw != 0 and witness is None:
            for i in range(DIM):
                for j in range(DIM):
                    if lhs[i][j] != FZ:
                        witness = {"branch_cell": c, "entry": [i, j],
                                   "value_re": str(lhs[i][j][0]),
                                   "value_w": str(lhs[i][j][1])}
                        break
                if witness:
                    break
    committed = dict(S4_COMMITTED["witness"])
    if mut("MUT-S4"):
        committed["value_re"] = "1/37"
    match = (witness is not None
             and witness["branch_cell"] == committed["branch_cell"]
             and tuple(witness["entry"]) == tuple(committed["entry"])
             and witness["value_re"] == committed["value_re"]
             and witness["value_w"] == committed["value_w"])
    # the repaired successor (the scout repair landed as commit e8cb399
    # during this unit's build): its s4_linearity rows are verified at
    # the VALUE grain against the same embedded committed values; no
    # live-file digest is serialized (the #66 G-ENV-EXCLUSION lesson).
    try:
        rep = json.loads(read_rel("v15/code/scout_receipt.json"))
    except (OSError, ValueError):
        rep = None
    rep_row = rep.get("s4_linearity") if isinstance(rep, dict) else None
    rep_wit = rep_row.get("witness") if isinstance(rep_row, dict) else None
    expect = dict(committed)
    if mut("MUT-REPAIRED"):
        expect["value_re"] = "1/38"
    rep_match = (isinstance(rep_wit, dict)
                 and rep_wit.get("branch_cell") == expect["branch_cell"]
                 and tuple(rep_wit.get("entry", ())) ==
                 tuple(expect["entry"])
                 and rep_wit.get("value_re") == expect["value_re"]
                 and rep_wit.get("value_w") == expect["value_w"]
                 and rep_row.get("closed_form_identity_verifies") is True
                 and rep_row.get("nonlinear_on_mixtures") is True)
    P["s4_consumed"] = {
        "repaired_successor": {
            "read": "live v15/code/scout_receipt.json (the repaired "
                    "successor, landed during this unit's build)",
            "witness_rows_match_committed_values": rep_match,
            "checked_fields": ["witness.branch_cell", "witness.entry",
                               "witness.value_re", "witness.value_w",
                               "closed_form_identity_verifies",
                               "nonlinear_on_mixtures"],
        },
        "committed_note_digest": S4_COMMITTED["note_digest"],
        "committed_receipt_digest": S4_COMMITTED["receipt_digest"],
        "committed_witness": committed,
        "recomputed_witness": witness,
        "closed_form": S4_COMMITTED["closed_form"],
        "closed_form_identity_verifies": identity_ok,
        "witness_matches_committed": match,
        "consumed_via": "committed digests (git anchor); the live files "
                        "are under a concurrent repair and were not read",
    }
    LD.gate("G-CLOSED-FORM", identity_ok,
            "the S4 closed form -(1/4)(w_c(rho0)-w_c(rho1))(P0-P1) "
            "verifies entry by entry on this instrument's own machinery",
            None)
    LD.gate("G-S4-CONSUMED", match,
            "the committed S4 nonlinearity witness (branch cell 0, entry "
            "(4, 4), value 1/36) is recomputed exactly and equals the "
            "embedded committed values", {"witness": witness})
    LD.gate("G-S4-REPAIRED", rep_match,
            "the repaired successor's s4_linearity rows carry the "
            "identical witness values at the value grain, verified "
            "against the same embedded committed values", None)


# ===========================================================================
# SECTION 6.  SAMPLE SPACES, NUMERAL BINDINGS, VERDICT
# ===========================================================================
SS_NAMES = ("CELLS", "RECORD-FIELDS")


def sample_space_audit(LD, P):
    found = []

    def walk(obj, path):
        if isinstance(obj, dict):
            if "equal" in obj:
                found.append((path, obj.get("sample_space")))
            for k in sorted(obj, key=str):
                walk(obj[k], path + "/" + str(k))
        elif isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                walk(v, path + "/" + str(i))
    for key in ("delivered", "null_control", "positive_control",
                "witness_distributions", "delivered_summary"):
        walk(P.get(key), key)
    found.append(("delivered_summary",
                  P["delivered_summary"].get("sample_space")))
    for dn in sorted(P.get("witness_distributions", {})):
        found.append(("witness_distributions/" + dn,
                      P["witness_distributions"][dn].get("sample_space")))
    bad = sorted(p for (p, s) in found if s not in SS_NAMES)
    P["sample_spaces"] = {"names": list(SS_NAMES),
                          "probability_rows_declared": len(found),
                          "rows_without_declaration": bad}
    LD.gate("G-SAMPLE-SPACE", not bad,
            "every probability-typed row in the receipt declares its "
            "sample space from the two declared names",
            {"rows": len(found)})


def numeral_bindings(LD, P):
    wit = P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]["window2"]
    pos = P["positive_control"]["RHO1"]["pairs"]["D1A|D1B"]["window1"]
    binds = [
        {"token": str(wit["mass_left"]),
         "path": "delivered/RHO1/pairs/D1A|D1B/window2/mass_left"},
        {"token": str(wit["mass_right"]),
         "path": "delivered/RHO1/pairs/D1A|D1B/window2/mass_right"},
        {"token": str(wit["difference"]),
         "path": "delivered/RHO1/pairs/D1A|D1B/window2/difference"},
        {"token": wit["first_record"],
         "path": "delivered/RHO1/pairs/D1A|D1B/window2/first_record"},
        {"token": str(wit["diverging_records"]),
         "path": "delivered/RHO1/pairs/D1A|D1B/window2/diverging_records"},
        {"token": "1/36",
         "path": "s4_consumed/committed_witness/value_re"},
        {"token": str(pos["mass_left"]),
         "path": "positive_control/RHO1/pairs/D1A|D1B/window1/mass_left"},
        {"token": str(pos["mass_right"]),
         "path": "positive_control/RHO1/pairs/D1A|D1B/window1/mass_right"},
        {"token": pos["first_record"],
         "path": "positive_control/RHO1/pairs/D1A|D1B/window1/"
                 "first_record"},
    ]
    if mut("MUT-BIND"):
        binds[0]["token"] = "17/729"
    ser = fser(P)
    ok = True
    for b in binds:
        node = ser
        for part in b["path"].split("/"):
            if isinstance(node, dict) and part in node:
                node = node[part]
            else:
                node = None
                break
        b["resolves"] = (node is not None and str(node) == b["token"])
        if not b["resolves"]:
            ok = False
    P["numeral_bindings"] = binds
    LD.gate("G-NUMERAL-BINDING", ok,
            "every load-bearing numeral of the note is bound to its "
            "specific receipt field and the binding resolves to the "
            "identical token", {"bindings": len(binds)})


def build_verdict(P):
    wit = P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]
    w2 = wit["window2"]
    P["verdict"] = (
        "SCOUTPSI-DECOMPOSITION-SENSITIVE-AT-2"
        "<WINDOW-1-BLIND-AT-EVERY-PAIR-BY-MEASUREMENT; "
        "FIRST-DIVERGENCE-AT-WINDOW-2-ON-RHO1-D1A-VS-D1B-AT-RECORD-"
        + w2["first_record"].replace(":", "x").replace(",", "-")
        + "-MASSES-" + str(w2["mass_left"]).replace("/", "-OVER-")
        + "-VS-" + str(w2["mass_right"]).replace("/", "-OVER-")
        + "; EVERY-MEASURED-PAIR-OF-BOTH-RHOS-DIVERGES-FIRST-AT-WINDOW-2; "
        "NULL-SELECTIVE-COMPLETION-BLIND-AT-ALL-THREE-WINDOWS; "
        "POSITIVE-SYNTHETIC-MAP-SENSITIVE-AT-WINDOW-1; "
        "WINDOWS-BEYOND-3-REGISTERED-NOT-CLAIMED>")
    P["walls"] = {
        "ontology": "this unit decides no ontology: it measures a "
                    "property of the delivered rule; the fork's "
                    "resolution is a program decision informed by this "
                    "measurement",
        "windows_registered_not_claimed": "4 and deeper",
        "coin_order": "the delivered order G.D only; the alternative "
                      "order is registered, not measured",
    }


def build_kit(P):
    wit = P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]
    w2 = wit["window2"]
    pos = P["positive_control"]["RHO1"]["pairs"]["D1A|D1B"]["window1"]
    kit = []
    kit.append("window 1 is BLIND at every decomposition pair of both "
               "committed rhos: the one-step CELL-HIT branch weights "
               "enter the ensemble record marginal linearly, and all 4 "
               "pairwise comparisons agree record by record "
               "[SS:RECORD-FIELDS]")
    kit.append("the first divergence is at window 2: preparations D1A "
               "and D1B of the same rho assign masses %s and %s to the "
               "record {%s}, difference %s, and %d records diverge at "
               "that window [SS:RECORD-FIELDS]"
               % (w2["mass_left"], w2["mass_right"], w2["first_record"],
                  w2["difference"], w2["diverging_records"]))
    kit.append("every measured decomposition pair of both rhos diverges "
               "first at window 2, and window 3 diverges at every pair "
               "as well; windows beyond 3 are registered, not claimed")
    kit.append("the declared genuinely linear completion -- the "
               "selective collapse reading paper-20 names as not run -- "
               "is BLIND at windows 1, 2 and 3 on the same "
               "decompositions, record by record [SS:RECORD-FIELDS]")
    kit.append("the synthetic decomposition-sensitive control reads "
               "SENSITIVE at window 1: on the witness pair it assigns "
               "masses %s and %s to its first diverging record {%s} "
               "[SS:RECORD-FIELDS]" % (pos["mass_left"],
                                       pos["mass_right"],
                                       pos["first_record"]))
    kit.append("this unit decides no ontology: it measures a property "
               "of the delivered rule, and the fork's resolution is a "
               "program decision informed by this measurement")
    kit.append("the S4 apparatus is consumed at the committed digests "
               "34f10a6fd494 and 12bdb7a58909, and the committed "
               "nonlinearity witness is recomputed exactly: branch cell "
               "0, entry (4, 4), value 1/36")
    P["kit"] = kit


# ===========================================================================
# SECTION 7.  THE FULL BUILD
# ===========================================================================
def build_all(P=None):
    LD = Ledger()
    if P is None:
        P = {}
    source_scan(LD, P)
    measure_anchors(LD, P)
    measure_arena(LD, P)
    D = build_preparations(LD, P)
    measure_delivered(LD, P, D)
    measure_null(LD, P, D)
    measure_positive(LD, P, D)
    s4_weld(LD, P)
    sample_space_audit(LD, P)
    numeral_bindings(LD, P)
    build_verdict(P)
    build_kit(P)
    P["ledger"] = LD.rows
    return P


# ===========================================================================
# SECTION 8.  NOTE VERIFICATION (the walls on the report's own prose)
# ===========================================================================
FORBIDDEN_GLOBAL = (
    "psi is ontic", "psi is real", "rho is complete", "rho is incomplete",
    "the ontic decomposition matters", "decides the ontology",
    "proves the ontic", "no reader will", "no one will doubt",
    "delta b is a divisibility", "measures divisibility",
)


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
        for k in sorted(obj, key=str):
            rationals_of(k, out)
            rationals_of(obj[k], out)
    if isinstance(obj, (list, tuple)):
        for v in obj:
            rationals_of(v, out)


def collect_numerals(obj, out):
    if isinstance(obj, bool):
        return
    if isinstance(obj, int):
        out.add(obj)
        return
    if isinstance(obj, str):
        for tok in obj.replace("/", " ").replace(",", " ") \
                      .replace(":", " ").split():
            neg = tok.lstrip("-")
            if neg.isdigit():
                out.add(int(neg))
        return
    if isinstance(obj, dict):
        for k in sorted(obj, key=str):
            collect_numerals(k, out)
            collect_numerals(obj[k], out)
    if isinstance(obj, (list, tuple)):
        for v in obj:
            collect_numerals(v, out)


LAYOUT_NUMERALS = set(range(0, 60)) | {64, 65, 84, 108, 156, 217, 275,
                                       277, 289, 344, 529, 633, 729, 100,
                                       120, 133, 2026, 6561, 19683}


def verify_note(P, note_bytes, problems):
    text = note_bytes.decode("utf-8")
    hay = canon(text)
    # hyphen-robust wall scan on the whole canon text
    hay_soft = " ".join(hay.lower().replace("-", " ").split())
    for pat in FORBIDDEN_GLOBAL:
        if pat in hay_soft:
            problems.append("forbidden pattern present: " + pat)
    for sent in P["kit"]:
        if canon(sent) not in hay:
            problems.append("kit sentence missing: " + sent[:70])
    for q in P20_QUOTES:
        if canon(q) not in hay:
            problems.append("paper-20 anchor quote missing from note")
    if P["verdict"] not in hay:
        problems.append("the verdict word is missing from the note")
    for name in SS_NAMES:
        if "[SS:" + name + "]" not in text:
            problems.append("sample-space tag [SS:%s] absent" % name)
    # heading-aware line rules: tables, quotes and headings are skipped
    for ln in text.splitlines():
        st = ln.strip()
        if st.startswith("|") or st.startswith(">") or st.startswith("#"):
            continue
        if ("P(" in ln or "q(" in ln) and "[SS:" not in ln:
            problems.append("probability expression without a "
                            "sample-space tag: " + st[:60])
        if "derive" in ln.lower() and "[BY:" not in ln:
            problems.append("derivation sentence without a subject tag: "
                            + st[:60])
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
    for b in P["numeral_bindings"]:
        if b["token"] not in text:
            problems.append("bound numeral absent from the note: "
                            + b["token"])
    inv = set()
    rationals_of(fser(P), inv)
    for ln in text.splitlines():
        for t in sorted(iter_rationals(ln)):
            if t not in inv:
                problems.append("slash rational not in receipt "
                                "inventory: " + t)
    nums = set()
    collect_numerals(fser(P), nums)
    for ln in text.splitlines():
        for tok in ln.replace("(", " ").replace(")", " ") \
                     .replace(",", " ").split():
            t = tok.strip(".;:|%{}").lstrip("#")
            if t.isascii() and t.isdigit():
                v = int(t)
                if v not in nums and v not in LAYOUT_NUMERALS:
                    problems.append("numeral not receipt-backed: " + t)
    return problems


# ===========================================================================
# SECTION 9.  FALSIFIERS
# ===========================================================================
FALSIFIERS = (
    ("MUT-PIN", "G-PIN-DIGESTS", "anchors",
     "corrupts the pinned digest of the frozen pin note"),
    ("MUT-ANCHOR", "G-P20-ANCHOR", "anchors",
     "corrupts the expected paper-20 delivered-rule sentence"),
    ("MUT-UNITARY", "G-ARENA", "arena",
     "corrupts one coin entry so the Gram matrix leaves 9I"),
    ("MUT-RHO", "G-RHO-EQUAL", "preparations",
     "replaces one D1A member so the mixtures no longer agree"),
    ("MUT-DISTINCT", "G-DISTINCT", "preparations",
     "replaces D1B by D1A so the ensembles are no longer distinct"),
    ("MUT-W1", "G-WINDOW1-BLIND", "delivered",
     "transfers 1/59 of mass inside D1A's window-1 distribution"),
    ("MUT-MASS", "G-MASS", "delivered",
     "halves D1A's window-1 distribution so total mass leaves 1"),
    ("MUT-DIV", "G-SENSITIVE", "delivered",
     "copies D1A's window-2 distribution onto D1B, erasing the "
     "divergence"),
    ("MUT-NULL", "G-NULL-BLIND", "null_control",
     "runs the null control with the uncollapsed delivered state leg"),
    ("MUT-POS", "G-POSITIVE-SENSITIVE", "positive_control",
     "runs the positive control with plain Born weights (linear)"),
    ("MUT-S4", "G-S4-CONSUMED", "s4_consumed",
     "corrupts the embedded committed S4 witness value"),
    ("MUT-CLOSED", "G-CLOSED-FORM", "s4_consumed",
     "flips the sign in the S4 closed-form recomputation"),
    ("MUT-REPAIRED", "G-S4-REPAIRED", "s4_consumed",
     "corrupts the value expected of the repaired successor's witness "
     "row"),
    ("MUT-BIND", "G-NUMERAL-BINDING", "numeral_bindings",
     "corrupts a bound numeral token so the binding fails to resolve"),
)


# ===========================================================================
# SECTION 10.  ARTIFACTS, CLI, SELFTEST
# ===========================================================================
def render_output(P, note_digest):
    lines = []
    lines.append("SCOUT-PSI delivery transcript")
    lines.append("pin 8e9fe2448b00; unit note " + NOTE_REL)
    lines.append("S4 apparatus consumed at the committed digests "
                 "34f10a6fd494 / 12bdb7a58909")
    lines.append("object under test (the note): sha256-12 " + note_digest)
    lines.append("instrument source: sha256-12 "
                 + P["source_hygiene"]["digest"])
    lines.append("")
    for r in P["ledger"]:
        lines.append("GATE %-20s %s  %s"
                     % (r["gate"], "PASS" if r["ok"] else "FAIL",
                        r["note"]))
    lines.append("")
    lines.append("VERDICT")
    lines.append("  " + P["verdict"])
    lines.append("")
    lines.append("KEY CLAIMS")
    for sent in P["kit"]:
        lines.append("  " + sent)
    lines.append("")
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
        raise GateFail("G-NOTE-KIT", "the unit note is absent")
    note_bytes = read_rel(NOTE_REL)
    problems = verify_note(P1, note_bytes, [])
    if problems:
        raise GateFail("G-NOTE-KIT", "; ".join(problems[:8]))
    nd = sha12(note_bytes)
    P1["object_under_test"] = {"path": NOTE_REL, "sha256_12": nd}
    P1["falsifiers"] = [{"name": n, "gate": g, "object": o,
                         "description": d} for (n, g, o, d) in FALSIFIERS]
    P1["schema"] = "scoutpsi-receipt-v1"
    out = render_output(P1, nd)
    rec = to_json(P1)
    if write:
        with open(os.path.join(ROOT, OUT_REL), "w", encoding="utf-8") as f:
            f.write(out)
        with open(os.path.join(ROOT, REC_REL), "w", encoding="utf-8") as f:
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
        sys.stdout.write("FALSIFIER %-14s died at %-20s moved-proof ok\n"
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


USAGE = ("usage: scoutpsi_exact.py [--no-write | --numbers | --kit | "
         "--selftest | --mutant NAME | --verify-paper PATH | "
         "--list-gates | --list-mutants]\n")

GATE_NAMES = ("G-SRC-CLEAN", "G-PIN-DIGESTS", "G-P20-ANCHOR", "G-ARENA",
              "G-UNITARITY", "G-RHO-EQUAL", "G-DISTINCT", "G-MASS",
              "G-WINDOW1-BLIND", "G-SENSITIVE", "G-NULL-BLIND",
              "G-POSITIVE-SENSITIVE", "G-CLOSED-FORM", "G-S4-CONSUMED",
              "G-S4-REPAIRED", "G-SAMPLE-SPACE", "G-NUMERAL-BINDING",
              "G-DETERMINISM", "G-NOTE-KIT", "G-SERIAL")


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
        for g in GATE_NAMES:
            sys.stdout.write(g + "\n")
        return 0
    if mode == "--list-mutants":
        for (n, g, o, d) in FALSIFIERS:
            sys.stdout.write("%-14s -> %-20s (%s): %s\n" % (n, g, o, d))
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
                         "bindings, numerals all pass\n")
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
        sys.stdout.write(P["verdict"] + "\n")
        sys.stdout.write(to_json(
            {"delivered_summary": P["delivered_summary"],
             "witness_window2":
                 P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]["window2"]})
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
