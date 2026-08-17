#!/usr/bin/env python3
# ===========================================================================
# SCOUT-PSI  --  the equal-density / different-preparation test.
# REPAIRED under ledger #76 orders Z1-Z8 and the #77 routing erratum,
# with the #80 (twelfth review) Z3 sharpening folded in.
#
# Unit: v15/note-scoutpsi.md (report NOTE, no paper number).
# Pin:  v15/note-scoutpsi-pin.md (FROZEN 8e9fe2448b00); ledger #64/#65.
# Pin addendum (FROZEN #68, consumed by gate): e717d3bbc1df.
# DC bipartite-causality addendum v2 (FROZEN #82, supersedes v1,
#   cited per the #80 routing order): ca713e89633b.
# Verifier review (FROZEN #76, expectations source): 7590f2c7abc1.
# S4 apparatus consumed by anchor at the COMMITTED digests
#   v15/note-scout-bridge.md    34f10a6fd494
#   v15/code/scout_receipt.json 12bdb7a58909
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
    "v15/note-scoutpsi-pin-addendum.md": "e717d3bbc1df",
    "v15/note-dc-causality-addendum-v2.md": "ca713e89633b",
    "v15/review-scoutpsi-verifier.md": "7590f2c7abc1",
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

# the #70 committed measured values (receipt d61a7f6e5ac0), embedded as
# the NO-VALUE-MOVED wall: the repair may only ADD rows, never move one.
COMMITTED_DELIVERED = {
    "witness_window2": {"first_record": "2:1,14:1", "mass_left": "16/729",
                        "mass_right": "32/729", "difference": "-16/729",
                        "diverging_records": 27},
    "first_windows": {"RHO1/D1A|D1B": 2, "RHO1/D1A|D1C": 2,
                      "RHO1/D1B|D1C": 2, "RHO2/D2A|D2B": 2},
    "positive_window1": {"first_record": "2:1", "mass_left": "16/33",
                         "mass_right": "64/129"},
    "window3_digests": {
        "RHO1": {"D1A": {"digest": "8af8ad6c18b0", "records": 477},
                 "D1B": {"digest": "574e1aa34870", "records": 477},
                 "D1C": {"digest": "f82e497d11fa", "records": 477}},
        "RHO2": {"D2A": {"digest": "1dcb18084d30", "records": 873},
                 "D2B": {"digest": "02d771567fe8", "records": 1527}}},
}

# the verifier's measured mitigation values (review 7590f2c7abc1, rows
# R16/R17), embedded as EXPECTATIONS: this instrument re-derives every
# one of them from its own walk and dies if any differs.
VERIFIER_EXPECT = {
    "secondary": {"window1": "equal", "window2_diverging_records": 378,
                  "first_record": "26:2", "mass_left": "0",
                  "mass_right": "1/729"},
    "witness_grains": {
        "ordered_raw_w2": 27, "ordered_raw_w3": 486,
        "count_raw_w2": 27, "count_raw_w3": 477,
        "count_T9_w2": 27, "count_T9_w3": 240,
        "count_S27_w2": "equal", "count_S27_w3": 2,
        "verifier_class_member": "23:1,26:1",
        "verifier_class_mass_left": "40/729",
        "verifier_class_mass_right": "8/729"},
}

# the #68 addendum's frozen objects, embedded for the consumption gate:
# what the addendum froze is checked field by field against what ran.
ADDENDUM_FROZEN = {
    "digest": "e717d3bbc1df",
    "primary_cells": (0, 1),
    "primary_weight_den": 2,
    "secondary": "maximally mixed on the S4 carrier; computational "
                 "basis uniform vs F3-character basis uniform",
    "rows": ("ordered-raw", "ordered-quotient-T9", "ordered-quotient-S27",
             "count-raw", "count-quotient-T9", "count-quotient-S27"),
    "null": "selective Born-collapse instrument: outcome c with the Born "
            "weight of the post-coin state; post-state the emitted cell "
            "component renormalized, then shifted; record += c",
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


def zdot(a, b):
    """<a|b> over Z[w], unnormalized."""
    tot = Z0
    for i in range(DIM):
        tot = zadd(tot, zmul(zconj(a[i]), b[i]))
    return tot


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
        "addendum_digest": ADDENDUM_FROZEN["digest"],
        "dc_addendum_digest": "ca713e89633b",
        "review_digest": "7590f2c7abc1",
    }
    LD.gate("G-PIN-DIGESTS",
            all(pins[r]["ok"] for r in sorted(pins)),
            "the pin note, the pin addendum, the DC causality addendum, "
            "the verifier review and paper-20 carry their pinned digests",
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
# SECTION 3.  THE PREPARATIONS (three rhos, seven decompositions:
#             the frozen primary + the frozen secondary of the #68
#             addendum, plus the two disclosed unfrozen extensions)
# ===========================================================================
H = Fraction(1, 2)
T27 = Fraction(1, 27)


def sup(a, cellA, b, cellB):
    return tuple(a if m == cellA else (b if m == cellB else Z0)
                 for m in range(DIM))


def chi_state(a, b, c):
    """the F3-character (Fourier) state w^(a i + b j + c m) over the
    cells ((i,j), link m); characters native to Q(w); scale2 = 27."""
    out = []
    for (x, l) in CELLS:
        i, j = x
        m = LINKS.index(l)
        out.append(WPOW[(a * i + b * j + c * m) % 3])
    return tuple(out)


def build_preparations(LD, P):
    e0, e1, e5 = basis(0), basis(1), basis(5)
    w = WPOW[1]
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
        "RHOSTAR": {
            "D1S": tuple((T27, basis(k), 1) for k in range(DIM)),
            "D2S": tuple((T27, chi_state(a, b, c), 27)
                         for a in range(3) for b in range(3)
                         for c in range(3)),
        },
    }
    if mut("MUT-DISTINCT"):
        D["RHO1"]["D1B"] = D["RHO1"]["D1A"]
    rows = {}
    rho_equal = True
    distinct = True
    star_mix = None
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
        if rho == "RHOSTAR":
            star_mix = mixes[names[0]]
        # genuinely distinct as ensembles: the weighted member density
        # matrices, as multisets, differ pairwise between decompositions
        sigs = {dn: sorted(digest({"p": p, "d": dens(psi, s2)})
                           for (p, psi, s2) in D[rho][dn])
                for dn in sorted(D[rho])}
        pd = True
        for a in names:
            for b in names:
                if a < b and sigs[a] == sigs[b]:
                    distinct = False
                    pd = False
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
            "pairwise_distinct_as_ensembles": pd,
        }
    P["preparations"] = {
        "rho_support": {"RHO1": "cells 0 and 1 (site (0,0), links (1,0) "
                                "and (0,1))",
                        "RHO2": "cells 0 and 5 (sites (0,0) and (0,1), "
                                "links (1,0) and (1,1))",
                        "RHOSTAR": "the maximally mixed state on all 27 "
                                   "cells (the frozen secondary of the "
                                   "#68 addendum)"},
        "rows": rows,
        "frozen_status": {"RHO1_D1A_D1B": "FROZEN (addendum item 1, "
                                          "primary)",
                          "RHOSTAR_D1S_D2S": "FROZEN (addendum item 1, "
                                             "secondary)",
                          "RHO1_D1C": "unfrozen extension, disclosed",
                          "RHO2": "unfrozen extension, disclosed"},
        "note": "each committed rho is the equal mixture of two "
                "orthogonal basis cells; D1A/D2A are the basis "
                "ensembles, D1B/D2B the plus-minus superposition "
                "ensembles, D1C the plus-minus-omega ensemble, all "
                "weights 1/2; the frozen secondary RHOSTAR is the "
                "maximally mixed state with D1S the computational basis "
                "uniform and D2S the F3-character basis uniform, all "
                "weights 1/27",
    }
    LD.gate("G-RHO-EQUAL", rho_equal,
            "within each rho every decomposition's weighted mixture is "
            "the same density matrix over Q(w), entry by entry, and every "
            "member's declared scale2 is its exact squared norm", None)
    # the frozen secondary's mixture must equal the exact maximally
    # mixed state I/27, entry by entry
    tden = 26 if mut("MUT-MAXMIX") else 27
    target_diag = (Fraction(1, tden), Fraction(0))
    mm_ok = star_mix is not None
    if mm_ok:
        for i in range(DIM):
            for j in range(DIM):
                want = target_diag if i == j else FZ
                if star_mix[i][j] != want:
                    mm_ok = False
    P["maxmix"] = {"target": "I/%d" % tden,
                   "equal_entry_by_entry": mm_ok,
                   "ensembles": ["D1S computational basis uniform",
                                 "D2S F3-character basis uniform"]}
    LD.gate("G-MAXMIX", mm_ok,
            "the frozen secondary rho** equals the exact maximally mixed "
            "state I/27 on the S4 carrier, entry by entry, from both "
            "frozen decompositions", None)
    LD.gate("G-DISTINCT", distinct,
            "the decompositions of one rho are genuinely distinct as "
            "ensembles: their weighted member density matrices differ as "
            "multisets, pairwise (the receipt field is the computed "
            "value)", None)
    # the HJW sharpening (#80): D1A|D1B is the canonical remotely
    # steerable pair -- the Z-basis / X-basis ensembles of the span:
    # within-ensemble orthogonality and cross mutual unbiasedness 1/2
    ub_target = Fraction(1, 3) if mut("MUT-HJW") else Fraction(1, 2)
    d1a = D["RHO1"]["D1A"]
    d1b = D["RHO1"]["D1B"]
    orth_a = znorm(zdot(d1a[0][1], d1a[1][1])) == 0
    orth_b = znorm(zdot(d1b[0][1], d1b[1][1])) == 0
    cross = []
    for (_pa, va, sa) in d1a:
        for (_pb, vb, sb) in d1b:
            cross.append(Fraction(znorm(zdot(va, vb)), sa * sb))
    hjw_ok = orth_a and orth_b and all(x == ub_target for x in cross)
    P["hjw_pair"] = {
        "within_ensemble_orthogonal": [orth_a, orth_b],
        "cross_overlap_ratios": cross,
        "mutual_unbiasedness_target": ub_target,
        "reading": "D1A and D1B are the Z-basis and X-basis ensembles "
                   "of the two-dimensional span: the "
                   "Hughston-Jozsa-Wootters remotely preparable pair",
        "dc_obligation": "v15/note-dc-causality-addendum-v2.md "
                         "ca713e89633b",
    }
    LD.gate("G-HJW-PAIR", hjw_ok,
            "the tested primary pair is the canonical remotely-steerable "
            "decomposition pair: both ensembles internally orthogonal "
            "and mutually unbiased at exact overlap ratio 1/2 "
            "(Z-basis vs X-basis of the span)", None)
    # deviation-4 truth (Z6): the four-member unequal-weight Z[w]
    # decomposition of RHO1 exists (verified), and the Bloch-balance
    # premise rho.rho = rho/2 holds for both committed rhos (verified)
    sixth = Fraction(1, 5) if mut("MUT-DEV4") else Fraction(1, 6)
    third = Fraction(1, 3)
    four_members = ((third, e0, 1), (third, e1, 1),
                    (sixth, sup(Z1, 0, (1, 0), 1), 2),
                    (sixth, sup(Z1, 0, (-1, 0), 1), 2))
    wsum = sum(p for (p, _v, _s) in four_members)
    m4 = mix(four_members)
    # renormalize nothing: weights must sum to 1 exactly for the witness
    rho1_mix = mix(D["RHO1"]["D1A"]) if not mut("MUT-RHO") else None
    four_ok = (wsum == 1 and rho1_mix is not None and m4 == rho1_mix)
    spectral = []
    for rho in ("RHO1", "RHO2"):
        M = mix(D[rho][sorted(D[rho])[0]])
        # M.M == M/2 entry by entry (equal eigenvalues 1/2 on rank 2)
        ok = True
        for i in range(DIM):
            for j in range(DIM):
                tot = FZ
                for k in range(DIM):
                    tot = fq_add(tot, fq_mul(M[i][k], M[k][j]))
                want = (M[i][j][0] / 2, M[i][j][1] / 2)
                if tot != want:
                    ok = False
        spectral.append(ok)
    P["deviation4_witness"] = {
        "four_member_weights": [str(p) for (p, _v, _s) in four_members],
        "mixes_to_rho1": four_ok,
        "spectral_balance_rho_rho_eq_rho_over_2": spectral,
        "bloch_balance": "with rho.rho = rho/2 verified, any two-member "
                         "pure decomposition is forced to weights 1/2 "
                         "and 1/2 over every field; unequal weights need "
                         "at least four members, and a four-member "
                         "unequal-weight witness exists inside Z[w]",
    }
    LD.gate("G-DEV4-WITNESS", four_ok and all(spectral),
            "the unequal-weight four-member Z[w] decomposition "
            "{1/3 e0; 1/3 e1; 1/6 (e0+e1); 1/6 (e0-e1)} mixes exactly "
            "to RHO1, and rho.rho = rho/2 verifies entry by entry for "
            "both committed rhos (the Bloch-balance premise)", None)
    return D


# ===========================================================================
# SECTION 4.  THE PROPAGATION ENGINE (per-branch, exact, windows 1..3;
#             ordered emission histories tracked; integer fast path)
# ===========================================================================
WINDOWS = 3


def rkey(n):
    return ",".join("%d:%d" % (c, n[c]) for c in range(DIM) if n[c])


def hkey(h):
    return ">".join("%d" % c for c in h)


def hist_windows(members, rule):
    """ordered CELL-HIT emission-history distributions at windows 1..3.
    rule DELIVERED: branch weights = Born of the post-coin state at
    the branch record; state leg = the SAME uncollapsed evolved state on
    every outcome; child record n + 1_c consumed by the next coin.
    rule SELECTIVE: the declared linear completion paper-20 names as not
    run -- record and collapse: the post-state is the basis state at the
    shifted emitted cell.
    rule SQUARED: the synthetic decomposition-sensitive control -- branch
    weights proportional to the squares of the Born weights, state leg
    uncollapsed.
    Weights are exact: integer numerators over the level-uniform
    denominators (DELIVERED/SELECTIVE), or per-branch integer pairs
    (SQUARED); every mass is a Fraction at the end."""
    M = len(members)
    p0 = members[0][0]
    if any(p != p0 for (p, _v, _s) in members) or p0 * M != 1:
        raise GateFail("G-RHO-EQUAL",
                       "non-uniform member weights reached the engine")
    s0 = members[0][2]
    if any(s2 != s0 for (_p, _v, s2) in members):
        raise GateFail("G-RHO-EQUAL",
                       "non-uniform member scales reached the engine")
    dists = [dict() for _ in range(WINDOWS)]
    if rule in ("DELIVERED", "SELECTIVE"):
        dens_levels = []
        sc = s0
        acc = 1
        for t in range(WINDOWS):
            acc *= 9 * sc
            dens_levels.append(acc)
            sc = 1 if rule == "SELECTIVE" else 9 * sc
        for (_p, psi, s2) in members:
            branches = [(1, R0, (), psi, s2)]
            for t in range(WINDOWS):
                nb = []
                dt = dists[t]
                last = (t == WINDOWS - 1)
                for (num, n, h, st, sc2) in branches:
                    post = coin_apply(st, n)
                    tot = 0
                    for z in post:
                        tot += znorm(z)
                    if tot != 9 * sc2:
                        raise GateFail("G-UNITARITY",
                                       "a branch total moved off "
                                       "9 x scale2")
                    ev = None if last else walk_shift(post)
                    for c in range(DIM):
                        wn = znorm(post[c])
                        if wn == 0:
                            continue
                        h2 = h + (c,)
                        num2 = num * wn
                        dt[h2] = dt.get(h2, 0) + num2
                        if not last:
                            n2 = list(n)
                            n2[c] += 1
                            n2 = tuple(n2)
                            if rule == "SELECTIVE":
                                nb.append((num2, n2, h2,
                                           basis(SHIFT[c]), 1))
                            else:
                                nb.append((num2, n2, h2, ev, 9 * sc2))
                branches = nb
        for t in range(WINDOWS):
            den = M * dens_levels[t]
            dists[t] = {h: Fraction(v, den)
                        for h, v in sorted(dists[t].items())}
        return dists
    # SQUARED: per-branch integer numerator/denominator pairs
    for (_p, psi, s2) in members:
        branches = [(1, 1, R0, (), psi, s2)]
        for t in range(WINDOWS):
            nb = []
            dt = dists[t]
            last = (t == WINDOWS - 1)
            for (num, den, n, h, st, sc2) in branches:
                post = coin_apply(st, n)
                tot = 0
                sq = []
                for z in post:
                    zn = znorm(z)
                    tot += zn
                    sq.append(zn * zn)
                if tot != 9 * sc2:
                    raise GateFail("G-UNITARITY",
                                   "a branch total moved off 9 x scale2")
                ssum = sum(sq)
                ev = None if last else walk_shift(post)
                for c in range(DIM):
                    if sq[c] == 0:
                        continue
                    h2 = h + (c,)
                    num2 = num * sq[c]
                    den2 = den * ssum
                    dt[h2] = dt.get(h2, Fraction(0)) \
                        + Fraction(num2, den2)
                    if not last:
                        n2 = list(n)
                        n2[c] += 1
                        n2 = tuple(n2)
                        nb.append((num2, den2, n2, h2, ev, 9 * sc2))
            branches = nb
    for t in range(WINDOWS):
        dists[t] = {h: v * p0 for h, v in sorted(dists[t].items())}
    return dists


def count_of(h):
    n = [0] * DIM
    for c in h:
        n[c] += 1
    return tuple(n)


def to_count(dh):
    out = {}
    for h in sorted(dh):
        k = count_of(h)
        out[k] = out.get(k, Fraction(0)) + dh[h]
    return out


# ---- the relabelling groups (named, per the repair order Z2) --------------
# T9: the site-translation subgroup Z3 x Z3 -- cell (x,l) -> (x+t,l);
#     9 elements; a symmetry of the arena's constructors.
# S27: the full simultaneous-relabelling group Sym(27) on cell labels --
#     the COARSEST label quotient: a count field keeps only its
#     multiset of counts; an ordered history keeps only its equality
#     pattern.
TRANS = tuple(tuple(CI[(vadd(x, t), l)] for (x, l) in CELLS)
              for t in SITES)


def hist_T9(h):
    return min(tuple(g[c] for c in h) for g in TRANS)


def count_T9(n):
    best = None
    for g in TRANS:
        n2 = [0] * DIM
        for c in range(DIM):
            if n[c]:
                n2[g[c]] = n[c]
        n2 = tuple(n2)
        if best is None or n2 < best:
            best = n2
    return best


def hist_S27(h):
    seen = {}
    out = []
    for c in h:
        if c not in seen:
            seen[c] = len(seen)
        out.append(seen[c])
    return tuple(out)


def count_S27(n):
    if mut("MUT-GRAIN"):
        return ()
    return tuple(sorted(v for v in n if v))


def quot(d, rep):
    out = {}
    for k in sorted(d):
        r = rep(k)
        out[r] = out.get(r, Fraction(0)) + d[k]
    return out


def compare(dA, dB):
    keys = sorted(set(dA) | set(dB))
    diffs = [k for k in keys
             if dA.get(k, Fraction(0)) != dB.get(k, Fraction(0))]
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


def compare_grain(dA, dB, ss, keyser):
    keys = sorted(set(dA) | set(dB))
    diffs = [k for k in keys
             if dA.get(k, Fraction(0)) != dB.get(k, Fraction(0))]
    row = {"equal": not diffs,
           "classes_left": len(dA), "classes_right": len(dB),
           "sample_space": ss}
    if diffs:
        k = diffs[0]
        row["first_class"] = keyser(k)
        row["mass_left"] = dA.get(k, Fraction(0))
        row["mass_right"] = dB.get(k, Fraction(0))
        row["diverging_records"] = len(diffs)
    return row


def pkey(t):
    return "+".join("%d" % v for v in t)


GRAIN_ROWS = (
    ("ordered-raw", "hist", None, "EMISSION-HISTORIES"),
    ("ordered-quotient-T9", "hist", hist_T9, "EMISSION-HISTORIES"),
    ("ordered-quotient-S27", "hist", hist_S27, "EMISSION-HISTORIES"),
    ("count-raw", "count", None, "RECORD-FIELDS"),
    ("count-quotient-T9", "count", count_T9, "RECORD-FIELDS"),
    ("count-quotient-S27", "count", count_S27, "RECORD-FIELDS"),
)


def row_verdict(cmps):
    """the per-row verdict word, grain-indexed by construction."""
    eqs = [cmps[t]["equal"] for t in range(WINDOWS)]
    blind = [str(t + 1) for t in range(WINDOWS) if eqs[t]]
    first = None
    for t in range(WINDOWS):
        if not eqs[t]:
            first = t + 1
            break
    if first is None:
        return "BLIND-AT-" + "-".join(blind)
    pre = ("BLIND-AT-" + "-".join(str(t + 1) for t in range(first - 1))
           + "-") if first > 1 else ""
    return pre + "SENSITIVE-AT-%d" % first


def ser_dist(d):
    return [[rkey(k), d[k]] for k in sorted(d)]


def ser_hdist(d):
    return [[hkey(k), d[k]] for k in sorted(d)]


def run_family(LD, P, D, rule, field):
    out = {}
    grains = {}
    mass_checks = []
    for rho in sorted(D):
        hdists = {dn: hist_windows(D[rho][dn], rule)
                  for dn in sorted(D[rho])}
        cdists = {dn: [to_count(hdists[dn][t]) for t in range(WINDOWS)]
                  for dn in sorted(hdists)}
        for dn in sorted(cdists):
            for t in range(WINDOWS):
                mass_checks.append(sum(cdists[dn][t][k]
                                       for k in sorted(cdists[dn][t]))
                                   == 1)
        names = sorted(hdists)
        pairs = {}
        gpairs = {}
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                a, b = names[i], names[j]
                pr = {}
                gp = {}
                base = {}
                for t in range(WINDOWS):
                    da, db = dict(cdists[a][t]), dict(cdists[b][t])
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
                    if rule == "DELIVERED" and mut("MUT-SECDIV") \
                            and t in (1, 2) and rho == "RHOSTAR":
                        db = dict(da)
                    base[t] = (da, db)
                    pr["window%d" % (t + 1)] = compare(da, db)
                first = None
                for t in range(WINDOWS):
                    if not pr["window%d" % (t + 1)]["equal"]:
                        first = t + 1
                        break
                pr["first_divergent_window"] = first
                pairs[a + "|" + b] = pr
                # the four frozen comparison rows (addendum item 2),
                # quotients at both NAMED groups; the count-raw row's
                # comparisons reuse the (possibly mutant-perturbed)
                # legacy dicts so no mutant can split the two views
                for (rname, kind, rep, ss) in GRAIN_ROWS:
                    cmps = {}
                    for t in range(WINDOWS):
                        if kind == "count":
                            xa, xb = base[t]
                        else:
                            xa = hdists[a][t]
                            xb = hdists[b][t]
                        if rep is not None:
                            xa = quot(xa, rep)
                            xb = quot(xb, rep)
                            if rule == "DELIVERED" and mut("MUT-QCONS") \
                                    and t == 0 and rho == "RHO1" \
                                    and a == "D1A" and b == "D1B" \
                                    and rname == "count-quotient-T9":
                                ks = sorted(xa)
                                xa[ks[0]] += Fraction(1, 59)
                        if rname == "count-quotient-S27":
                            kser = pkey
                        elif kind == "count":
                            kser = rkey
                        elif rname == "ordered-quotient-S27":
                            kser = pkey
                        else:
                            kser = hkey
                        cmps["window%d" % (t + 1)] = compare_grain(
                            xa, xb, ss, kser)
                    cmps["verdict"] = row_verdict(
                        [cmps["window%d" % (t + 1)]
                         for t in range(WINDOWS)])
                    gp[rname] = cmps
                gpairs[a + "|" + b] = gp
        out[rho] = {"pairs": pairs}
        grains[rho] = gpairs
        if rule == "DELIVERED":
            out[rho]["window3_digests"] = {
                dn: {"digest": digest(ser_dist(cdists[dn][2])),
                     "records": len(cdists[dn][2])}
                for dn in sorted(cdists)}
            if rho == "RHO1":
                wd = {}
                for dn in ("D1A", "D1B"):
                    wd[dn] = {"window1": ser_dist(cdists[dn][0]),
                              "window2": ser_dist(cdists[dn][1]),
                              "sample_space": "RECORD-FIELDS"}
                P["witness_distributions"] = wd
            if rho == "RHOSTAR":
                sd = {}
                for dn in ("D1S", "D2S"):
                    sd[dn] = {"window1": ser_dist(cdists[dn][0]),
                              "window2": ser_dist(cdists[dn][1]),
                              "window3_digest":
                                  digest(ser_dist(cdists[dn][2])),
                              "sample_space": "RECORD-FIELDS"}
                P["secondary_distributions"] = sd
    P[field] = out
    P.setdefault("grain_rows", {})[field] = grains
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
            "window 1 is blind at every decomposition pair of all three "
            "rhos: the one-step CELL-HIT branch weights enter the "
            "ensemble record marginal linearly, and every pairwise "
            "comparison agrees record by record", None)
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
            "measured pair of all three rhos, the frozen secondary "
            "included",
            {"first_windows": all_pairs_first})
    # Z1: the frozen secondary re-derives the verifier's measured row
    ve = VERIFIER_EXPECT["secondary"]
    exp_div = ve["window2_diverging_records"]
    if mut("MUT-SECEXP"):
        exp_div = exp_div - 1
    sec = P["delivered"]["RHOSTAR"]["pairs"]["D1S|D2S"]
    sw2 = sec["window2"]
    sec_ok = (sec["window1"]["equal"]
              and not sw2["equal"]
              and sw2["diverging_records"] == exp_div
              and sw2["first_record"] == ve["first_record"]
              and str(sw2["mass_left"]) == ve["mass_left"]
              and str(sw2["mass_right"]) == ve["mass_right"])
    P["secondary_expect"] = {
        "expected_from": "review 7590f2c7abc1 row R16, re-derived by "
                         "this instrument's own walk",
        "expected": {"window1": ve["window1"],
                     "window2_diverging_records": exp_div,
                     "first_record": ve["first_record"],
                     "mass_left": ve["mass_left"],
                     "mass_right": ve["mass_right"]},
        "measured": {"window1_equal": sec["window1"]["equal"],
                     "window2": sw2},
        "match": sec_ok}
    LD.gate("G-SECONDARY-EXPECT", sec_ok,
            "the frozen secondary re-derives the verifier's mitigation "
            "row exactly: blind at window 1, sensitive at window 2 with "
            "378 diverging records, first diverging record {26:2} with "
            "masses 0 and 1/729", None)
    grain_gates(LD, P)


def grain_gates(LD, P):
    G = P["grain_rows"]["delivered"]
    # consistency first: a quotient row may only diverge where its raw
    # row diverges, at every pair and window (aggregation cannot create
    # a difference), and quotient masses stay total
    cons_ok = True
    cons_checks = 0
    for rho in sorted(G):
        for pk in sorted(G[rho]):
            gp = G[rho][pk]
            for (rname, kind, rep, _ss) in GRAIN_ROWS:
                if rep is None:
                    continue
                raw = gp["ordered-raw" if kind == "hist" else "count-raw"]
                for t in range(WINDOWS):
                    wk = "window%d" % (t + 1)
                    cons_checks += 1
                    if not gp[rname][wk]["equal"] and raw[wk]["equal"]:
                        cons_ok = False
    LD.gate("G-QUOT-CONSISTENT", cons_ok,
            "no quotient row diverges where its raw row is equal: "
            "label aggregation never manufactures a difference",
            {"checks": cons_checks})
    wg = VERIFIER_EXPECT["witness_grains"]
    wit = G["RHO1"]["D1A|D1B"]
    fine_ok = True
    for rho in sorted(G):
        for pk in sorted(G[rho]):
            for rname in ("ordered-raw", "count-raw",
                          "ordered-quotient-T9", "count-quotient-T9"):
                v = G[rho][pk][rname]["verdict"]
                if v != "BLIND-AT-1-SENSITIVE-AT-2":
                    fine_ok = False
    coarse_ok = (wit["count-quotient-S27"]["verdict"]
                 == "BLIND-AT-1-2-SENSITIVE-AT-3"
                 and wit["ordered-quotient-S27"]["verdict"]
                 == "BLIND-AT-1-2-SENSITIVE-AT-3"
                 and wit["count-quotient-S27"]["window3"]
                 ["diverging_records"] == wg["count_S27_w3"])
    counts_ok = (wit["ordered-raw"]["window2"]["diverging_records"]
                 == wg["ordered_raw_w2"]
                 and wit["ordered-raw"]["window3"]["diverging_records"]
                 == wg["ordered_raw_w3"]
                 and wit["count-raw"]["window2"]["diverging_records"]
                 == wg["count_raw_w2"]
                 and wit["count-raw"]["window3"]["diverging_records"]
                 == wg["count_raw_w3"]
                 and wit["count-quotient-T9"]["window2"]
                 ["diverging_records"] == wg["count_T9_w2"]
                 and wit["count-quotient-T9"]["window3"]
                 ["diverging_records"] == wg["count_T9_w3"])
    LD.gate("G-GRAIN-VERDICTS", fine_ok and coarse_ok and counts_ok,
            "the four frozen comparison rows carry their per-row "
            "verdicts: every pair diverges first at window 2 at the raw "
            "and translation grains; the witness pair under the "
            "coarsest simultaneous-relabelling quotient is blind at "
            "window 2 and first diverges at window 3; every verifier "
            "class count re-derives exactly",
            {"witness_verdicts": {r: wit[r]["verdict"]
                                  for (r, _k, _q, _s) in GRAIN_ROWS}})
    # the verifier's named diverging class, re-derived
    n0 = [0] * DIM
    n0[23] = 1
    n0[26] = 1
    rep = count_T9(tuple(n0))
    tq = wit["count-quotient-T9"]["window2"]
    exp_l = wg["verifier_class_mass_left"]
    if mut("MUT-VCLASS"):
        exp_l = "41/729"
    # recompute the class masses from the published witness w2 dists
    da = {}
    db = {}
    for dn, tgt in (("D1A", da), ("D1B", db)):
        for k, v in P["witness_distributions"][dn]["window2"]:
            n = [0] * DIM
            for part in k.split(","):
                c, m = part.split(":")
                n[int(c)] = int(m)
            r = count_T9(tuple(n))
            tgt[r] = tgt.get(r, Fraction(0)) + v
    vc_ok = (str(da.get(rep, Fraction(0))) == exp_l
             and str(db.get(rep, Fraction(0)))
             == wg["verifier_class_mass_right"])
    P["verifier_class"] = {
        "class_member": wg["verifier_class_member"],
        "class_representative": rkey(rep),
        "mass_left": da.get(rep, Fraction(0)),
        "mass_right": db.get(rep, Fraction(0)),
        "expected": {"mass_left": exp_l,
                     "mass_right": wg["verifier_class_mass_right"]},
        "window2_T9_diverging_classes": tq["diverging_records"],
        "sample_space": "RECORD-FIELDS", "equal": False}
    LD.gate("G-VERIFIER-CLASS", vc_ok,
            "the translation-quotient class of {23:1,26:1} re-derives "
            "the verifier's masses 40/729 and 8/729 at window 2 on the "
            "witness pair", None)


def measure_null(LD, P, D):
    mass_checks = run_family(LD, P, D, "SELECTIVE", "null_control")
    if mut("MUT-NULL"):
        run_family(LD, P, D, "DELIVERED", "null_control")
    ok = all(P["null_control"][rho]["pairs"][pk]["window%d" % w]["equal"]
             for rho in sorted(P["null_control"])
             for pk in sorted(P["null_control"][rho]["pairs"])
             for w in (1, 2, 3))
    G = P["grain_rows"]["null_control"]
    rows_ok = all(G[rho][pk][rname]["window%d" % w]["equal"]
                  for rho in sorted(G)
                  for pk in sorted(G[rho])
                  for (rname, _k, _q, _s) in GRAIN_ROWS
                  for w in (1, 2, 3))
    P["null_control"]["declaration"] = (
        "the declared genuinely linear CPTP completion is the selective "
        "collapse reading paper-20 names as not run -- the frozen null "
        "of addendum item 3: record the emitted cell and collapse the "
        "state onto the shifted emitted cell -- a projective cell-basis "
        "instrument composed with the walk unitary")
    LD.gate("G-NULL-BLIND", ok and rows_ok and all(mass_checks),
            "the declared linear completion (the selective collapse "
            "reading) is blind at windows 1, 2 and 3 on the same "
            "decompositions, record by record, at all four comparison "
            "rows and both quotient groups", None)
    # the frozen null is a genuine channel: Kraus completeness
    # K_c = (1/3)|e_SHIFT[c]><C_n row c| gives sum K'K = C_n' C_n / 9,
    # and the count phase is diagonal-unitary, so C_n' C_n = 9 I at
    # every record n.  Verified exactly at two records.
    want_diag = 8 if mut("MUT-KRAUS") else 9
    recs = [R0]
    n1 = [0] * DIM
    n1[0] = 1
    recs.append(tuple(n1))
    kraus_ok = True
    for n in recs:
        cols = [coin_apply(basis(j), n) for j in range(DIM)]
        for i in range(DIM):
            for j in range(DIM):
                tot = Z0
                for c in range(DIM):
                    tot = zadd(tot, zmul(zconj(cols[i][c]), cols[j][c]))
                want = (want_diag, 0) if i == j else Z0
                if tot != want:
                    kraus_ok = False
    P["null_kraus"] = {
        "kraus_form": "K_c = (1/3) |e_SHIFT[c]> <row c of C(n)|",
        "completeness": "sum_c K_c-dagger K_c = C(n)-dagger C(n) / 9 "
                        "= I, exactly, at both probe records",
        "records_checked": [rkey(n) for n in recs],
        "verified": kraus_ok}
    LD.gate("G-NULL-KRAUS", kraus_ok,
            "the frozen null instrument is a complete channel: "
            "sum K-dagger K = I verified exactly over Z[w] at the empty "
            "record and at a one-count record", None)


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
# SECTION 6.  THE NO-VALUE-MOVED WALL AND THE ADDENDUM CONSUMPTION GATE
# ===========================================================================
def no_value_moved(LD, P):
    cd = dict(COMMITTED_DELIVERED)
    wexp = dict(cd["witness_window2"])
    if mut("MUT-MOVED"):
        wexp["mass_left"] = "17/729"
    wit = P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]["window2"]
    checks = []
    for fld in ("first_record", "mass_left", "mass_right", "difference",
                "diverging_records"):
        checks.append(str(wit[fld]) == str(wexp[fld]))
    fw = P["delivered_summary"]["first_divergent_window_by_pair"]
    for pk in sorted(cd["first_windows"]):
        checks.append(fw.get(pk) == cd["first_windows"][pk])
    pos = P["positive_control"]["RHO1"]["pairs"]["D1A|D1B"]["window1"]
    for fld in ("first_record", "mass_left", "mass_right"):
        checks.append(str(pos[fld]) == str(cd["positive_window1"][fld]))
    for rho in sorted(cd["window3_digests"]):
        for dn in sorted(cd["window3_digests"][rho]):
            got = P["delivered"][rho]["window3_digests"][dn]
            wantd = cd["window3_digests"][rho][dn]
            checks.append(got["digest"] == wantd["digest"]
                          and got["records"] == wantd["records"])
    P["no_value_moved"] = {
        "committed_receipt": "d61a7f6e5ac0",
        "expected_witness_window2": wexp,
        "checks": len(checks), "all_equal": all(checks),
        "statement": "every #70 measured value is unchanged; the repair "
                     "only ADDS rows (the secondary, the grain rows, "
                     "the consumption and qualification gates)"}
    LD.gate("G-NO-VALUE-MOVED", all(checks),
            "no committed measured value moved: the witness window-2 "
            "row, all four committed first-divergence windows, the "
            "positive-control row and all five committed window-3 "
            "distribution digests re-derive byte-identically", None)


def addendum_consumed(LD, P, D):
    spec = dict(ADDENDUM_FROZEN)
    prim = spec["primary_cells"]
    if mut("MUT-ADDCON"):
        prim = (0, 2)
    checks = {}
    # primary as frozen: D1A = the two lex-first computational cells of
    # the S4 witness support, equal weights; D1B their plus/minus pair
    d1a = D["RHO1"]["D1A"]
    checks["primary_D1A"] = (
        len(d1a) == 2
        and d1a[0][1] == basis(prim[0]) and d1a[1][1] == basis(prim[1])
        and all(p == Fraction(1, spec["primary_weight_den"])
                for (p, _v, _s) in d1a))
    d1b = D["RHO1"]["D1B"]
    plus = sup(Z1, prim[0], (1, 0), prim[1])
    minus = sup(Z1, prim[0], (-1, 0), prim[1])
    checks["primary_D1B"] = (
        len(d1b) == 2 and d1b[0][1] == plus and d1b[1][1] == minus
        and all(p == Fraction(1, spec["primary_weight_den"])
                for (p, _v, _s) in d1b))
    # secondary as frozen: computational uniform and F3-character
    # uniform, both mixing to I/27 (G-MAXMIX), members unimodular
    d1s = D["RHOSTAR"]["D1S"]
    checks["secondary_D1S"] = (
        len(d1s) == DIM
        and all(d1s[k][1] == basis(k) for k in range(DIM))
        and all(p == T27 for (p, _v, _s) in d1s))
    d2s = D["RHOSTAR"]["D2S"]
    checks["secondary_D2S"] = (
        len(d2s) == DIM
        and all(p == T27 for (p, _v, _s) in d2s)
        and all(znorm(v[m]) == 1 for (_p, v, _s) in d2s
                for m in range(DIM))
        and len({v for (_p, v, _s) in d2s}) == DIM)
    checks["secondary_maxmix"] = P["maxmix"]["equal_entry_by_entry"]
    # the four comparison rows present with verdicts at every pair
    G = P["grain_rows"]["delivered"]
    rows_ok = True
    for rho in sorted(G):
        for pk in sorted(G[rho]):
            for rname in spec["rows"]:
                if rname not in G[rho][pk]:
                    rows_ok = False
                elif "verdict" not in G[rho][pk][rname]:
                    rows_ok = False
    checks["four_rows_all_pairs"] = rows_ok
    # the frozen null is the one that ran
    checks["null_is_frozen"] = ("selective collapse reading"
                                in P["null_control"]["declaration"]
                                and P["null_kraus"]["verified"])
    checks["addendum_pinned"] = (
        P["anchors"]["pinned"]
        ["v15/note-scoutpsi-pin-addendum.md"]["ok"])
    P["addendum_consumed"] = {
        "digest": spec["digest"],
        "frozen_primary_cells": list(prim),
        "checks": checks,
        "order_of_events": (
            "the addendum was frozen at ledger #68, mid-build, and was "
            "never routed to the original worker (ledger #77): the #70 "
            "delivery was built to the pin as launched and had already "
            "inspected the primary, D1C and RHO2 computations before "
            "any addendum text reached the unit; this repair received "
            "the addendum text and the verifier's measured expected "
            "values in its launch order, and re-derived every frozen "
            "leg with those expectations gated"),
    }
    LD.gate("G-ADDENDUM-CONSUMED",
            all(checks[k] for k in sorted(checks)),
            "the #68 addendum is consumed by gate at digest "
            "e717d3bbc1df: the frozen primary and secondary "
            "preparations, the four comparison rows, and the frozen "
            "null instrument are checked field by field against what "
            "ran", {k: checks[k] for k in sorted(checks)})


# ===========================================================================
# SECTION 7.  SAMPLE SPACES, NUMERAL BINDINGS, VERDICT, KIT
# ===========================================================================
SS_NAMES = ("CELLS", "RECORD-FIELDS", "EMISSION-HISTORIES")


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
                "witness_distributions", "secondary_distributions",
                "delivered_summary", "grain_rows", "verifier_class"):
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
            "sample space from the three declared names",
            {"rows": len(found)})


def numeral_bindings(LD, P):
    wit = P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]["window2"]
    pos = P["positive_control"]["RHO1"]["pairs"]["D1A|D1B"]["window1"]
    sec = P["delivered"]["RHOSTAR"]["pairs"]["D1S|D2S"]["window2"]
    witg = P["grain_rows"]["delivered"]["RHO1"]["D1A|D1B"]
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
        {"token": str(sec["diverging_records"]),
         "path": "delivered/RHOSTAR/pairs/D1S|D2S/window2/"
                 "diverging_records"},
        {"token": sec["first_record"],
         "path": "delivered/RHOSTAR/pairs/D1S|D2S/window2/first_record"},
        {"token": str(sec["mass_right"]),
         "path": "delivered/RHOSTAR/pairs/D1S|D2S/window2/mass_right"},
        {"token": str(P["verifier_class"]["mass_left"]),
         "path": "verifier_class/mass_left"},
        {"token": str(P["verifier_class"]["mass_right"]),
         "path": "verifier_class/mass_right"},
        {"token": str(witg["ordered-raw"]["window3"]
                      ["diverging_records"]),
         "path": "grain_rows/delivered/RHO1/D1A|D1B/ordered-raw/"
                 "window3/diverging_records"},
        {"token": str(witg["count-raw"]["window3"]["diverging_records"]),
         "path": "grain_rows/delivered/RHO1/D1A|D1B/count-raw/"
                 "window3/diverging_records"},
        {"token": str(witg["count-quotient-T9"]["window3"]
                      ["diverging_records"]),
         "path": "grain_rows/delivered/RHO1/D1A|D1B/count-quotient-T9/"
                 "window3/diverging_records"},
        {"token": str(witg["count-quotient-S27"]["window3"]
                      ["diverging_records"]),
         "path": "grain_rows/delivered/RHO1/D1A|D1B/count-quotient-S27/"
                 "window3/diverging_records"},
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
    P["windows"] = {"measured": [1, 2, 3],
                    "registered_not_claimed": "4 and deeper",
                    "mass_total": "1"}
    P["delivered_summary"]["committed_pairwise_comparisons"] = 4
    P["instrument_counts"] = {"gate_names": len(GATE_NAMES),
                              "falsifiers": len(FALSIFIERS)}
    wit = P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]
    w2 = wit["window2"]
    sec = P["delivered"]["RHOSTAR"]["pairs"]["D1S|D2S"]["window2"]
    P["verdict"] = (
        "SCOUTPSI-DECOMPOSITION-SENSITIVE-AT-2-AT-THE-FINE-GRAINS"
        "<WINDOW-1-BLIND-AT-EVERY-PAIR-BY-MEASUREMENT; "
        "FIRST-DIVERGENCE-AT-WINDOW-2-ON-RHO1-D1A-VS-D1B-AT-RECORD-"
        + w2["first_record"].replace(":", "x").replace(",", "-")
        + "-MASSES-" + str(w2["mass_left"]).replace("/", "-OVER-")
        + "-VS-" + str(w2["mass_right"]).replace("/", "-OVER-")
        + "; EVERY-MEASURED-PAIR-OF-ALL-THREE-RHOS-DIVERGES-FIRST-AT-"
        "WINDOW-2-AT-THE-RAW-AND-TRANSLATION-GRAINS; "
        "SECONDARY-MAXIMALLY-MIXED-BLIND-AT-1-SENSITIVE-AT-2-AT-"
        + str(sec["diverging_records"]) + "-DIVERGING-RECORDS; "
        "BLIND-AT-2-SENSITIVE-AT-3-AT-THE-COARSEST-QUOTIENT-ON-THE-"
        "WITNESS-PAIR; "
        "NULL-SELECTIVE-COMPLETION-BLIND-AT-ALL-THREE-WINDOWS-AT-ALL-"
        "FOUR-ROWS; "
        "POSITIVE-SYNTHETIC-MAP-SENSITIVE-AT-WINDOW-1; "
        "WINDOWS-BEYOND-3-REGISTERED-NOT-CLAIMED>")
    P["walls"] = {
        "ontology": "this unit decides no ontology: it measures a "
                    "property of the delivered rule; the fork's "
                    "resolution is a program decision informed by this "
                    "measurement",
        "ontology_wall_surface": "a literal pattern blacklist plus the "
                                 "verifier seat and the candidate-"
                                 "reading discipline; the general "
                                 "fresh-paraphrase condition is "
                                 "registered, not claimed",
        "windows_registered_not_claimed": "4 and deeper",
        "coin_order": "the delivered order G.D only; the alternative "
                      "order is registered, not measured",
        "steering_scope": "non-collapse is not a safety property "
                          "against steering; unphrasability is "
                          "incompleteness; paper-38's zero is scoped "
                          "as a reading, not a wall (ledger #80)",
    }


def build_kit(LD, P):
    wit = P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]
    w2 = wit["window2"]
    pos = P["positive_control"]["RHO1"]["pairs"]["D1A|D1B"]["window1"]
    sec = P["delivered"]["RHOSTAR"]["pairs"]["D1S|D2S"]["window2"]
    witg = P["grain_rows"]["delivered"]["RHO1"]["D1A|D1B"]
    vc = P["verifier_class"]
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
    kit.append("the frozen secondary rho** -- the maximally mixed state "
               "on the S4 carrier -- is BLIND at window 1 and SENSITIVE "
               "at window 2 on its frozen pair D1S|D2S (computational "
               "basis uniform vs F3-character basis uniform): %d "
               "records diverge at window 2, first diverging record "
               "{%s} with masses %s and %s [SS:RECORD-FIELDS]"
               % (sec["diverging_records"], sec["first_record"],
                  sec["mass_left"], sec["mass_right"]))
    kit.append("all four frozen comparison rows are measured with "
               "per-row verdicts at every pair: at the raw and "
               "translation-quotient grains every measured pair of all "
               "three rhos diverges first at window 2; at the coarsest "
               "simultaneous-relabelling quotient the witness pair is "
               "BLIND at window 2 and first diverges at window 3, in "
               "%d classes [SS:RECORD-FIELDS]"
               % witg["count-quotient-S27"]["window3"]
               ["diverging_records"])
    kit.append("under the site-translation quotient (the Z3xZ3 "
               "subgroup) the witness pair stays SENSITIVE at window 2 "
               "with %d diverging classes, and the class of "
               "{23:1,26:1} carries masses %s and %s [SS:RECORD-FIELDS]"
               % (vc["window2_T9_diverging_classes"], vc["mass_left"],
                  vc["mass_right"]))
    kit.append("the declared genuinely linear completion -- the "
               "selective collapse reading paper-20 names as not run -- "
               "is BLIND at windows 1, 2 and 3 on the same "
               "decompositions, record by record [SS:RECORD-FIELDS]")
    kit.append("the null is blind at all four comparison rows and both "
               "quotient groups, and its Kraus completeness "
               "sum K-dagger K = I verifies exactly [SS:RECORD-FIELDS]")
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
    # the operational-qualification wall sentences (addendum item 4,
    # sharpened by ledger #80), each gated
    kit.append("a SENSITIVE verdict proves rho is not a sufficient "
               "state descriptor FOR THE DELIVERED CELL-HIT RULE on "
               "pure-state ensembles")
    kit.append("it becomes an experimental distinction only if ISP can "
               "operationally prepare both decompositions -- "
               "preparation and intervention protocols are UNBUILT, "
               "and no experimental distinction is claimed")
    kit.append("a future triple-event law with a different state "
               "update may remove or change the sensitivity, and no "
               "sentence here reads the verdict as deciding the "
               "psi-ontology")
    kit.append("the tested primary pair is the canonical "
               "remotely-steerable decomposition pair: D1A and D1B are "
               "the Z-basis and X-basis ensembles of the "
               "two-dimensional span (Hughston-Jozsa-Wootters), "
               "exactly the two ensembles a remote party could prepare "
               "by measuring her half of a Bell pair in either basis, "
               "so the sensitivity is a hard compatibility gate on any "
               "future ISP composite dynamics (the DC "
               "bipartite-causality addendum v2, digest ca713e89633b, is "
               "the standing obligation)")
    kit.append("non-collapse is not presented as a safety property "
               "against steering, steering-unphrasability is "
               "incompleteness rather than safety, and paper-38's zero "
               "is scoped as a reading of an unchanged record, not a "
               "wall against a future steering test")
    kit.append("the pin addendum is consumed at its frozen digest "
               "e717d3bbc1df: the frozen preparations, the four "
               "comparison rows, the frozen null instrument and the "
               "qualification sentences are checked in-run against "
               "what ran")
    kit.append("the machine ontology wall is a literal pattern "
               "blacklist, not a semantic classifier: the enforcement "
               "is the blacklist plus the verifier seat and the "
               "candidate-reading discipline; the seat's passing "
               "paraphrases are embedded as permanent plants that die "
               "at the wall, and the general fresh-paraphrase "
               "condition stays registered, not claimed")
    if mut("MUT-QUAL"):
        kit = [s for s in kit
               if "sufficient state descriptor" not in s]
    P["kit"] = kit
    required = ("not a sufficient state descriptor FOR THE DELIVERED "
                "CELL-HIT RULE",
                "preparation and intervention protocols are UNBUILT",
                "future triple-event law",
                "deciding the psi-ontology",
                "canonical remotely-steerable decomposition pair",
                "Hughston-Jozsa-Wootters",
                "ca713e89633b",
                "not presented as a safety property against steering",
                "incompleteness rather than safety",
                "not a wall against a future steering test")
    missing = [r for r in required
               if not any(r in s for s in kit)]
    LD.gate("G-QUAL-GATED", not missing,
            "the operational-qualification wall sentences (addendum "
            "item 4, sharpened by ledger #80) are present in the "
            "rendered kit: rho-insufficiency scoped to the delivered "
            "rule, protocols unbuilt, the triple-law caveat, the "
            "psi-ontology wall, the HJW canonical-pair sentence and "
            "the steering-scope sentence",
            {"required": len(required), "missing": missing})


# ===========================================================================
# SECTION 8.  THE FULL BUILD
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
    no_value_moved(LD, P)
    addendum_consumed(LD, P, D)
    sample_space_audit(LD, P)
    numeral_bindings(LD, P)
    build_verdict(P)
    build_kit(LD, P)
    P["ledger"] = LD.rows
    return P


# ===========================================================================
# SECTION 9.  NOTE VERIFICATION (the walls on the report's own prose)
# ===========================================================================
# the base blacklist (the #70 surface) plus the repair's extensions:
# the verifier's passing paraphrases (F6) and the #80 steering walls.
# The wall is a literal pattern blacklist and the note says so.
FORBIDDEN_BASE = (
    "psi is ontic", "psi is real", "rho is complete", "rho is incomplete",
    "the ontic decomposition matters", "decides the ontology",
    "proves the ontic", "no reader will", "no one will doubt",
    "delta b is a divisibility", "measures divisibility",
)
FORBIDDEN_EXTRA = (
    "is physically real", "the true state of affairs",
    "incomplete description of the actual state", "settling the fork",
    "steering lever is absent", "einstein locality is safe",
    "zero is a wall against", "unphrasability as safety",
    "unphrasable is safe",
)

# the permanent plants: the verifier's two passing paraphrases (review
# I5/I6) and the #80 steering family; each must die at the wall.
PLANTS = (
    ("PLANT-ONT-1", "the wavefunction is physically real and the "
                    "ensemble is the true state of affairs"),
    ("PLANT-ONT-2", "the density matrix is therefore an "
                    "incomplete-description of the actual state, "
                    "settling the fork"),
    ("PLANT-STEER-1", "the walk does not collapse, so the steering "
                      "lever is absent"),
    ("PLANT-STEER-2", "steering is unphrasable here, so Einstein "
                      "locality is safe"),
    ("PLANT-STEER-3", "paper-38's zero is a wall against any future "
                      "steering test"),
)


def forbidden_patterns():
    if mut("MUT-PLANT"):
        return FORBIDDEN_BASE
    return FORBIDDEN_BASE + FORBIDDEN_EXTRA


def wall_hits(text):
    soft = " ".join(canon(text).lower().replace("-", " ").split())
    return [pat for pat in forbidden_patterns() if pat in soft]


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


def verify_note(P, note_bytes, problems):
    text = note_bytes.decode("utf-8")
    hay = canon(text)
    for pat in wall_hits(text):
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
    gates.update(("G-NOTE-KIT", "G-WALL-PLANTS", "G-NUMERAL-TOTALITY",
                  "G-DETERMINISM", "G-SERIAL"))
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
    return problems


# ---- numeral totality (addendum item 5, repair order Z5) ------------------
# every numeral occurrence in the note -- every maximal digit run --
# is classified BOUND (a specific receipt field, containment-resolved)
# or NON-CLAIM (a reason class from the declared set).  The
# classification is an ordered rule table; the first matching rule
# wins; an occurrence no rule matches is UNCLASSIFIED and fails the
# gate.  This replaces the #70 integer whitelist entirely.
REASON_CLASSES = ("DATE", "LEDGER-INDEX", "FILE-OR-SECTION-NAME",
                  "GIT-COMMIT-CITATION", "LIST-MARKER", "FORMAT-NAME",
                  "GROUP-OR-FIELD-NAME", "REVIEW-CITATION",
                  "THEOREM-CONSTANT", "USAGE-CODE", "OBJECT-NAME",
                  "GATE-OR-TAG-NAME")

STRIP = ".,;:()[]{}|'\"`*<>!?"


def note_occurrences(text):
    occ = []
    for li, ln in enumerate(text.splitlines(), 1):
        for raw in ln.split():
            word = raw.strip(STRIP)
            runs = []
            cur = ""
            for ch in word:
                if ch.isascii() and ch.isdigit():
                    cur += ch
                else:
                    if cur:
                        runs.append(cur)
                    cur = ""
            if cur:
                runs.append(cur)
            for r in runs:
                occ.append({"line": li, "word": word, "digits": r})
    return occ


def numeral_rules():
    """the ordered classification table.  Fields: word (exact stripped
    word; None = any word), line_has (substring the line must carry;
    None = any line), cls BOUND/NON-CLAIM, ref (receipt path) or
    reason (a declared reason class)."""
    B, N = "BOUND", "NON-CLAIM"
    W2 = "delivered/RHO1/pairs/D1A|D1B/window2/"
    SEC = "delivered/RHOSTAR/pairs/D1S|D2S/window2/"
    GW = "grain_rows/delivered/RHO1/D1A|D1B/"
    rules = [
        # --- whole-line binds: the verdict block and digest words ---
        {"line_has": "SCOUTPSI-DECOMPOSITION-SENSITIVE", "word": None,
         "cls": B, "ref": "verdict"},
        {"word": "8e9fe2448b00", "cls": B,
         "ref": "anchors/pinned/v15~note-scoutpsi-pin.md/got"},
        {"word": "e717d3bbc1df", "cls": B,
         "ref": "anchors/addendum_digest"},
        {"word": "ca713e89633b", "cls": B,
         "ref": "anchors/dc_addendum_digest"},
        {"word": "7590f2c7abc1", "cls": B, "ref": "anchors/review_digest"},
        {"word": "4824d190af73", "cls": B,
         "ref": "anchors/pinned/v14~paper-20-coupling.md/got"},
        {"word": "34f10a6fd494", "cls": B,
         "ref": "anchors/s4_committed_note_digest"},
        {"word": "12bdb7a58909", "cls": B,
         "ref": "anchors/s4_committed_receipt_digest"},
        {"word": "d61a7f6e5ac0", "cls": B,
         "ref": "no_value_moved/committed_receipt"},
        {"word": "e8cb399", "cls": N, "reason": "GIT-COMMIT-CITATION"},
        # --- the measured masses and records ---
        {"word": "16/729", "cls": B, "ref": W2 + "mass_left"},
        {"word": "32/729", "cls": B, "ref": W2 + "mass_right"},
        {"word": "-16/729", "cls": B, "ref": W2 + "difference"},
        {"word": "2:1,14:1", "cls": B, "ref": W2 + "first_record"},
        {"word": "26:2", "cls": B, "ref": SEC + "first_record"},
        {"word": "1/729", "cls": B, "ref": SEC + "mass_right"},
        {"word": "40/729", "cls": B, "ref": "verifier_class/mass_left"},
        {"word": "8/729", "cls": B, "ref": "verifier_class/mass_right"},
        {"word": "23:1,26:1", "cls": B,
         "ref": "verifier_class/class_member"},
        {"word": "16/33", "cls": B,
         "ref": "positive_control/RHO1/pairs/D1A|D1B/window1/mass_left"},
        {"word": "64/129", "cls": B,
         "ref": "positive_control/RHO1/pairs/D1A|D1B/window1/mass_right"},
        {"word": "2:1", "cls": B,
         "ref": "positive_control/RHO1/pairs/D1A|D1B/window1/"
                "first_record"},
        {"word": "1/36", "cls": B,
         "ref": "s4_consumed/committed_witness/value_re"},
        {"word": "378", "cls": B, "ref": SEC + "diverging_records"},
        {"word": "486", "cls": B,
         "ref": GW + "ordered-raw/window3/diverging_records"},
        {"word": "477", "cls": B,
         "ref": GW + "count-raw/window3/diverging_records"},
        {"word": "240", "cls": B,
         "ref": GW + "count-quotient-T9/window3/diverging_records"},
        {"word": "1/3", "cls": B,
         "ref": "deviation4_witness/four_member_weights"},
        {"word": "1/6", "cls": B,
         "ref": "deviation4_witness/four_member_weights"},
        {"word": "1/27", "cls": B, "ref": "preparations/note"},
        {"word": "I/27", "cls": B, "ref": "maxmix/target"},
        {"word": "1/2", "cls": B, "ref": "preparations/note"},
        # --- the totality claim sentence's own totals, bound to the
        #     compact totals subtree (installed in pass 1, resolved in
        #     pass 2) ---
        {"word": None, "line_has": "numeral totality:", "cls": B,
         "ref": "numeral_totality/totals"},
        # --- the grain table: every numeral on a [GRAIN] table line is
        #     bound to the delivered grain-row subtree the table
        #     renders (the verdicts are separately gated at
        #     G-GRAIN-VERDICTS) ---
        {"word": None, "line_has": "| GRAIN |", "cls": B,
         "ref": "grain_rows/delivered"},
        # --- line-scoped binds for coordinates and readouts ---
        {"word": None, "line_has": "CELL-HIT on cell", "cls": B,
         "ref": "delivered/RHO1/pairs/D1A|D1B/window2/first_record"},
        {"word": None, "line_has": "site (", "cls": B,
         "ref": "preparations/rho_support"},
        {"word": None, "line_has": "sites (", "cls": B,
         "ref": "preparations/rho_support"},
        {"word": None, "line_has": "closed form", "cls": B,
         "ref": "s4_consumed/closed_form"},
        {"word": "33", "cls": B, "ref": "instrument_counts/gate_names"},
        {"word": "28", "cls": B, "ref": "instrument_counts/falsifiers"},
        # --- context-scoped small integers (before the generic
        #     fallbacks; first match wins) ---
        {"word": "4", "line_has": "entry (4", "cls": B,
         "ref": "s4_consumed/committed_witness/entry"},
        {"word": "4", "line_has": "pairwise comparisons", "cls": B,
         "ref": "delivered_summary/committed_pairwise_comparisons"},
        {"word": "1", "line_has": "windows", "cls": B,
         "ref": "windows/measured"},
        {"word": "2", "line_has": "windows", "cls": B,
         "ref": "windows/measured"},
        {"word": "3", "line_has": "windows", "cls": B,
         "ref": "windows/measured"},
        {"word": "4", "line_has": "windows", "cls": B,
         "ref": "windows/registered_not_claimed"},
        {"word": "1", "line_has": "window", "cls": B,
         "ref": "windows/measured"},
        {"word": "2", "line_has": "window", "cls": B,
         "ref": "windows/measured"},
        {"word": "3", "line_has": "window", "cls": B,
         "ref": "windows/measured"},
        {"word": "1", "line_has": "mass exactly 1", "cls": B,
         "ref": "windows/mass_total"},
        {"word": "window-1", "cls": B, "ref": "windows/measured"},
        {"word": "window-2", "cls": B, "ref": "windows/measured"},
        {"word": "window-3", "cls": B, "ref": "windows/measured"},
        {"word": "0", "line_has": "cells 0 and", "cls": B,
         "ref": "preparations/rho_support"},
        {"word": "1", "line_has": "cells 0 and 1", "cls": B,
         "ref": "preparations/rho_support"},
        {"word": "5", "line_has": "cells 0 and 5", "cls": B,
         "ref": "preparations/rho_support"},
        # --- structural counts bound to arena/instrument fields ---
        {"word": "27", "cls": B, "ref": "arena/cells"},
        {"word": "27-tuples", "cls": B, "ref": "arena/cells"},
        {"word": "27-member", "cls": B, "ref": "arena/cells"},
        {"word": "9", "cls": B, "ref": "arena/sites"},
        {"word": "9I", "cls": B, "ref": "arena/gram_is_9I"},
        {"word": "3", "cls": B, "ref": "arena/links"},
        {"word": "Grover-over-3", "cls": B, "ref": "arena/coin"},
        {"word": "2", "cls": B, "ref": "delivered_summary/"
                                       "witness_first_window"},
        {"word": "0", "cls": B, "ref": "s4_consumed/committed_witness/"
                                       "branch_cell"},
        # --- names, dates, files, markers ---
        {"word": None, "line_has": "2026-08-17", "cls": N,
         "reason": "DATE"},
        {"word": "2026-08-17", "cls": N, "reason": "DATE"},
        {"word": "#58", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#64", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#65", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#66", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#68", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#70", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#70's", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#76", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#77", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#80", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "paper-20", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "paper-20-coupling.md:633", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": "paper-20's", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": "paper-38's", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": "paper-38:429", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": "paper-19's", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": None, "line_has": "v15/", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": None, "line_has": "v14/", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": "S0", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "S1", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "S2", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "S3", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "S4", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "S4's", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "W4-TYPE-IDENTITY", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": "E-34", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z1-Z8", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z1", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z2", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z3", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z4", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z5", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z6", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z7", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "Z8", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "F1", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F2", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F3", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F4", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F7", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F1-F9", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F5", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F6", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F8", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F9", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "I5/I6", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "R16", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "R17", "cls": N, "reason": "REVIEW-CITATION"},
        {"word": "F3-character", "cls": N,
         "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "scale2", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "s4_linearity", "cls": N,
         "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "s4_map", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "rank-2", "cls": N, "reason": "THEOREM-CONSTANT"},
        {"word": "v2", "cls": N, "reason": "FILE-OR-SECTION-NAME"},
        {"word": "#82", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "#83", "cls": N, "reason": "LEDGER-INDEX"},
        {"word": "D1A", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D1A's", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D1B", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D1B's", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D1C", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D2A", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D2B", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D1S", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D2S", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D1A|D1B", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D1S|D2S", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "RHO1", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "RHO1's", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "RHO2", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "RHO2's", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "e0", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "e1", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "e5", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "e0+e1", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "e0-e1", "cls": N, "reason": "OBJECT-NAME"},
        {"word": None, "line_has": "addendum item", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": "4", "line_has": "item 4", "cls": N,
         "reason": "FILE-OR-SECTION-NAME"},
        {"word": "LIC:G-P20-ANCHOR", "cls": N,
         "reason": "GATE-OR-TAG-NAME"},
        {"word": "LIC:G-WINDOW1-BLIND", "cls": N,
         "reason": "GATE-OR-TAG-NAME"},
        {"word": "LIC:G-S4-CONSUMED", "cls": N,
         "reason": "GATE-OR-TAG-NAME"},
        {"word": "LIC:G-S4-REPAIRED", "cls": N,
         "reason": "GATE-OR-TAG-NAME"},
        {"word": "LIC:G-DEV4-WITNESS", "cls": N,
         "reason": "GATE-OR-TAG-NAME"},
        {"word": "G-S4-REPAIRED", "cls": N,
         "reason": "GATE-OR-TAG-NAME"},
        {"word": "G-S4-CONSUMED", "cls": N,
         "reason": "GATE-OR-TAG-NAME"},
        {"word": "G-DEV4-WITNESS", "cls": N,
         "reason": "GATE-OR-TAG-NAME"},
        {"word": "Z3xZ3", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "T9", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "S27", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "Sym(27)", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "Sym(27", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "D1-family", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "D2-family", "cls": N, "reason": "OBJECT-NAME"},
        {"word": "Z[w]", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "Q(w)", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "sha256-12", "cls": N, "reason": "FORMAT-NAME"},
        {"word": "rho**", "cls": N, "reason": "GROUP-OR-FIELD-NAME"},
        {"word": "-(1/4)(w_c(rho0)-w_c(rho1))(P0-P1)", "cls": N,
         "reason": "THEOREM-CONSTANT"},
        {"word": "rho/2", "cls": N, "reason": "THEOREM-CONSTANT"},
        {"word": None, "line_has": "usage code", "cls": N,
         "reason": "USAGE-CODE"},
        # numbered deviation/list markers, scoped to their item titles
        # (the strip pass removes the trailing dot, so the word is bare)
        {"word": "1", "line_has": "dual-anchored", "cls": N,
         "reason": "LIST-MARKER"},
        {"word": "2", "line_has": "coin order", "cls": N,
         "reason": "LIST-MARKER"},
        {"word": "3", "line_has": "**Windows.**", "cls": N,
         "reason": "LIST-MARKER"},
        {"word": "4", "line_has": "Decomposition scope", "cls": N,
         "reason": "LIST-MARKER"},
        {"word": "5", "line_has": "Unfrozen extensions", "cls": N,
         "reason": "LIST-MARKER"},
        {"word": "6", "line_has": "relabelling groups are", "cls": N,
         "reason": "LIST-MARKER"},
        {"word": "7", "line_has": "primary-support anchor", "cls": N,
         "reason": "LIST-MARKER"},
        {"word": "8", "line_has": "Chain time", "cls": N,
         "reason": "LIST-MARKER"},
        {"word": "9", "line_has": "Review shape", "cls": N,
         "reason": "LIST-MARKER"},
    ]
    if mut("MUT-NUMTOT"):
        rules = [r for r in rules if r["cls"] == "NON-CLAIM"]
    return rules


def resolve_ref(ser, ref, word, digits):
    node = ser
    for part in ref.split("/"):
        part = part.replace("~", "/")
        if isinstance(node, dict) and part in node:
            node = node[part]
        else:
            return False
    s = json.dumps(node) if isinstance(node, (dict, list)) else str(node)
    return word == s or word in s or digits in s


def numeral_totality(P, text):
    """two passes.  Pass 1 classifies every occurrence and installs the
    counts and the full per-occurrence table in P, so the totals of the
    claim sentence are themselves receipt fields.  Pass 2 re-serializes
    P (now carrying numeral_totality) and resolves every BOUND ref
    against it."""
    occ = note_occurrences(text)
    rules = numeral_rules()
    table = []
    counts = {"BOUND": 0, "NON-CLAIM": 0, "UNCLASSIFIED": 0}
    unresolved = []
    lines = text.splitlines()
    for o in occ:
        line_text = lines[o["line"] - 1]
        hit = None
        for r in rules:
            if r.get("word") is not None and r["word"] != o["word"]:
                continue
            if r.get("line_has") is not None \
                    and r["line_has"] not in line_text:
                continue
            hit = r
            break
        row = {"line": o["line"], "word": o["word"],
               "digits": o["digits"]}
        if hit is None:
            row["cls"] = "UNCLASSIFIED"
            counts["UNCLASSIFIED"] += 1
        elif hit["cls"] == "BOUND":
            row["cls"] = "BOUND"
            row["ref"] = hit["ref"]
            counts["BOUND"] += 1
        else:
            row["cls"] = "NON-CLAIM"
            row["reason"] = hit["reason"]
            counts["NON-CLAIM"] += 1
            if hit["reason"] not in REASON_CLASSES:
                unresolved.append("undeclared reason " + hit["reason"])
        table.append(row)
    total = len(occ)
    P["numeral_totality"] = {
        "total_occurrences": total,
        "bound": counts["BOUND"],
        "non_claim": counts["NON-CLAIM"],
        "unclassified": counts["UNCLASSIFIED"],
        "totals": {"total": total, "bound": counts["BOUND"],
                   "non_claim": counts["NON-CLAIM"]},
        "reason_classes": list(REASON_CLASSES),
        "rows": table,
        "rule_count": len(rules),
    }
    # pass 2: resolve BOUND refs against the receipt as it will be
    # serialized (numeral_totality included)
    ser = fser(P)
    for row in table:
        if row["cls"] == "BOUND" \
                and not resolve_ref(ser, row["ref"], row["word"],
                                    row["digits"]):
            unresolved.append(row["word"] + " -> " + row["ref"])
    P["numeral_totality"]["unresolved_bindings"] = sorted(set(unresolved))
    problems = []
    if counts["UNCLASSIFIED"]:
        samples = ["line %d word %s" % (r["line"], r["word"])
                   for r in table if r["cls"] == "UNCLASSIFIED"][:10]
        problems.append("%d numeral occurrences unclassified: %s"
                        % (counts["UNCLASSIFIED"], "; ".join(samples)))
    if unresolved:
        problems.append("unresolved bindings: "
                        + "; ".join(sorted(set(unresolved))[:5]))
    claim = ("numeral totality: %d numeral occurrences in this note; "
             "%d bound to receipt fields; %d non-claim with reason "
             "classes; every occurrence classified"
             % (total, counts["BOUND"], counts["NON-CLAIM"]))
    if canon(claim) not in canon(text):
        problems.append("the numeral-totality sentence with the "
                        "measured totals is absent: " + claim)
    P["numeral_totality"]["claim_sentence"] = claim
    return problems


def note_phase(P, note_bytes, collect=None):
    """the note-side gates: G-NOTE-KIT, G-WALL-PLANTS,
    G-NUMERAL-TOTALITY.  Appends ledger rows; raises on failure unless
    collect is a list (then problems are appended)."""
    text = note_bytes.decode("utf-8")
    problems = verify_note(P, note_bytes, [])
    P["ledger"].append({"gate": "G-NOTE-KIT", "ok": not problems,
                        "note": "the note carries every rendered kit "
                                "sentence, the verdict, the anchors, "
                                "the tags and no forbidden pattern",
                        "data": None})
    if problems:
        if collect is not None:
            collect.extend(problems)
        else:
            raise GateFail("G-NOTE-KIT", "; ".join(problems[:8]))
    prows = []
    all_die = True
    for (pname, ptext) in PLANTS:
        hits = wall_hits(ptext)
        prows.append({"plant": pname, "dies": bool(hits),
                      "killed_by": hits[0] if hits else None})
        if not hits:
            all_die = False
    P["wall_plants"] = {
        "plants": prows,
        "surface": "a literal pattern blacklist (%d patterns); the "
                   "general fresh-paraphrase condition is registered, "
                   "not claimed" % len(forbidden_patterns())}
    P["ledger"].append({"gate": "G-WALL-PLANTS", "ok": all_die,
                        "note": "every permanent plant (the verifier's "
                                "passing paraphrases and the #80 "
                                "steering family) dies at the wall",
                        "data": None})
    if not all_die:
        if collect is not None:
            collect.append("a permanent plant survives the wall")
        else:
            raise GateFail("G-WALL-PLANTS",
                           "a permanent plant survives the wall")
    tot_problems = numeral_totality(P, text)
    P["ledger"].append({"gate": "G-NUMERAL-TOTALITY",
                        "ok": not tot_problems,
                        "note": "every numeral occurrence in the note "
                                "is classified BOUND or NON-CLAIM, "
                                "per occurrence, and the totals "
                                "sentence matches the measurement",
                        "data": None})
    if tot_problems:
        if collect is not None:
            collect.extend(tot_problems)
        else:
            raise GateFail("G-NUMERAL-TOTALITY",
                           "; ".join(tot_problems[:6]))
    return P


# ===========================================================================
# SECTION 10.  FALSIFIERS
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
    ("MUT-MAXMIX", "G-MAXMIX", "maxmix",
     "corrupts the maximally-mixed target so the secondary's mixture "
     "check must fail"),
    ("MUT-DISTINCT", "G-DISTINCT", "preparations",
     "replaces D1B by D1A so the ensembles are no longer distinct"),
    ("MUT-HJW", "G-HJW-PAIR", "hjw_pair",
     "corrupts the mutual-unbiasedness target of the canonical pair"),
    ("MUT-DEV4", "G-DEV4-WITNESS", "deviation4_witness",
     "corrupts a weight of the four-member witness so it no longer "
     "mixes to RHO1"),
    ("MUT-W1", "G-WINDOW1-BLIND", "delivered",
     "transfers 1/59 of mass inside D1A's window-1 distribution"),
    ("MUT-MASS", "G-MASS", "delivered",
     "halves D1A's window-1 distribution so total mass leaves 1"),
    ("MUT-DIV", "G-SENSITIVE", "delivered",
     "copies D1A's window-2 distribution onto D1B, erasing the "
     "divergence"),
    ("MUT-SECDIV", "G-SENSITIVE", "delivered",
     "copies D1S's window-2 and window-3 distributions onto D2S, "
     "erasing the secondary's divergence"),
    ("MUT-SECEXP", "G-SECONDARY-EXPECT", "secondary_expect",
     "corrupts the verifier-expected diverging-record count of the "
     "frozen secondary"),
    ("MUT-QCONS", "G-QUOT-CONSISTENT", "grain_rows",
     "injects mass into a window-1 translation-quotient class so a "
     "quotient row diverges where its raw row is equal"),
    ("MUT-GRAIN", "G-GRAIN-VERDICTS", "grain_rows",
     "collapses the coarsest quotient map to a constant so the "
     "witness window-3 divergence disappears"),
    ("MUT-VCLASS", "G-VERIFIER-CLASS", "verifier_class",
     "corrupts the expected mass of the verifier's diverging class"),
    ("MUT-NULL", "G-NULL-BLIND", "null_control",
     "runs the null control with the uncollapsed delivered state leg"),
    ("MUT-KRAUS", "G-NULL-KRAUS", "null_kraus",
     "corrupts the expected Kraus completeness so sum K-dagger K "
     "leaves I"),
    ("MUT-POS", "G-POSITIVE-SENSITIVE", "positive_control",
     "runs the positive control with plain Born weights (linear)"),
    ("MUT-S4", "G-S4-CONSUMED", "s4_consumed",
     "corrupts the embedded committed S4 witness value"),
    ("MUT-CLOSED", "G-CLOSED-FORM", "s4_consumed",
     "flips the sign in the S4 closed-form recomputation"),
    ("MUT-REPAIRED", "G-S4-REPAIRED", "s4_consumed",
     "corrupts the value expected of the repaired successor's witness "
     "row"),
    ("MUT-MOVED", "G-NO-VALUE-MOVED", "no_value_moved",
     "corrupts an embedded committed value so the no-move wall must "
     "fire"),
    ("MUT-ADDCON", "G-ADDENDUM-CONSUMED", "addendum_consumed",
     "corrupts the embedded frozen primary cells so the addendum "
     "consumption check must fail"),
    ("MUT-QUAL", "G-QUAL-GATED", "kit",
     "drops the rho-insufficiency qualification sentence from the "
     "rendered kit"),
    ("MUT-BIND", "G-NUMERAL-BINDING", "numeral_bindings",
     "corrupts a bound numeral token so the binding fails to resolve"),
    ("MUT-PLANT", "G-WALL-PLANTS", "wall_plants",
     "removes the repair's wall patterns so the permanent plants "
     "survive"),
    ("MUT-NUMTOT", "G-NUMERAL-TOTALITY", "numeral_totality",
     "removes every BOUND classification rule so occurrences go "
     "unclassified"),
)

NOTE_PHASE_MUTANTS = {"MUT-PLANT", "MUT-NUMTOT"}


# ===========================================================================
# SECTION 11.  ARTIFACTS, CLI, SELFTEST
# ===========================================================================
def render_output(P, note_digest):
    lines = []
    lines.append("SCOUT-PSI delivery transcript (REPAIRED, orders Z1-Z8 "
                 "of ledger #76 + the #77 routing erratum + the #80 "
                 "sharpening)")
    lines.append("pin 8e9fe2448b00; addendum e717d3bbc1df; DC addendum "
                 "v2 ca713e89633b; review 7590f2c7abc1; unit note "
                 + NOTE_REL)
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
    lines.append("THE GRAIN TABLE (delivered rule, per-row verdicts)")
    G = P["grain_rows"]["delivered"]
    for rho in sorted(G):
        for pk in sorted(G[rho]):
            for (rname, _k, _q, _s) in GRAIN_ROWS:
                lines.append("  %-8s %-9s %-22s %s"
                             % (rho, pk, rname,
                                G[rho][pk][rname]["verdict"]))
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
    note_phase(P1, note_bytes)
    nd = sha12(note_bytes)
    P1["object_under_test"] = {"path": NOTE_REL, "sha256_12": nd}
    P1["falsifiers"] = [{"name": n, "gate": g, "object": o,
                         "description": d} for (n, g, o, d) in FALSIFIERS]
    P1["schema"] = "scoutpsi-receipt-v2"
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
    note_bytes = read_rel(NOTE_REL)
    clean = build_all()
    note_phase(clean, note_bytes)
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
            if name in NOTE_PHASE_MUTANTS:
                note_phase(partial, note_bytes)
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
              "G-UNITARITY", "G-RHO-EQUAL", "G-MAXMIX", "G-DISTINCT",
              "G-HJW-PAIR", "G-DEV4-WITNESS", "G-MASS",
              "G-WINDOW1-BLIND", "G-SENSITIVE", "G-SECONDARY-EXPECT",
              "G-QUOT-CONSISTENT", "G-GRAIN-VERDICTS",
              "G-VERIFIER-CLASS", "G-NULL-BLIND", "G-NULL-KRAUS",
              "G-POSITIVE-SENSITIVE", "G-CLOSED-FORM", "G-S4-CONSUMED",
              "G-S4-REPAIRED", "G-NO-VALUE-MOVED",
              "G-ADDENDUM-CONSUMED", "G-QUAL-GATED", "G-SAMPLE-SPACE",
              "G-NUMERAL-BINDING", "G-NOTE-KIT", "G-WALL-PLANTS",
              "G-NUMERAL-TOTALITY", "G-DETERMINISM", "G-SERIAL")


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
            P = build_all()
            if args[1] in NOTE_PHASE_MUTANTS:
                note_phase(P, read_rel(NOTE_REL))
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
        problems = []
        note_phase(P, nb, collect=problems)
        if problems:
            for pr in problems[:20]:
                sys.stdout.write("NOTE PROBLEM: " + pr + "\n")
            return 3
        sys.stdout.write("NOTE VERIFIED: kit, anchors, walls, plants, "
                         "tags, bindings, numeral totality all pass\n")
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
                 P["delivered"]["RHO1"]["pairs"]["D1A|D1B"]["window2"],
             "secondary_window2":
                 P["delivered"]["RHOSTAR"]["pairs"]["D1S|D2S"]
                 ["window2"]})
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
