#!/usr/bin/env python3
"""
xba_crossbase_exact.py -- THE CROSS-BASE AGREEMENT HUNT (v13 XBA).

The question, from `v13/note-xba-crossbase-pin.md` (sha 7cbde5da4280):

    The two bases' holonomy class-count profiles agree (82/86/90/106)
    though only about 2.5% of Klein-four connections on the common
    gauge-fixed graph reproduce that profile, and the admission tables
    agree 24/24 cells.  WHAT SHARED STRUCTURE FORCES IT?

What this instrument does, in the order it does it:

  1  pins the two terminal receipts and the frozen operator review by
     sha256, and reads every reused number out of them (no typed reuse);
  2  rebuilds the common gauge-fixed graph INDEPENDENTLY from the two
     receipts' own admission tables -- no object of the frozen review's
     construction is imported, its numbers serving as external anchors;
  3  enumerates the reduced path space and the cycle space, and declares
     a cycle basis built from the graph and the two gluing rules;
  4  rebuilds BOTH bases from scratch in exact arithmetic -- the first in
     the totally real quartic field Q(cos pi/8), base G over Q -- and
     computes each one's gauge-fixed connection directly, with a second,
     gauge-free comparator (the raw matrix product along every walk);
  5  DECLARES a family of candidate shared properties, each a computable
     predicate on connections, with the freeze measured: the number of
     profiles computed at the declaration point is gated at zero and the
     receipt's gate order is the proof;
  6  enumerates all 4,096 Klein-four connections on the graph;
  7  measures, for each candidate: membership of both realized
     connections, the constrained subset's size, and whether every member
     of the subset reproduces the profile (exhaustive);
  8  derives the connection from the species clauses and tests the
     derivation on a THIRD, freshly constructed instance and on an
     exchange-equivariant control;
  9  runs the controls, the symmetry self-tests and the mutant census.

Exact arithmetic only: `fractions.Fraction`, and the quartic field
Q(cos pi/8) as rational 4-tuples reduced by x^4 = x^2 - 1/8, where tuple
equality IS field equality.  No float, no tolerance, anywhere.

Usage:
    python3.13 xba_crossbase_exact.py                  # verify, print
    python3.13 xba_crossbase_exact.py --delivery       # + write artifacts
    python3.13 xba_crossbase_exact.py --mutant NAME    # run one mutant
    python3.13 xba_crossbase_exact.py --falsification-selftest
"""

from __future__ import annotations

import argparse
import ast
import collections
import hashlib
import itertools
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
V13 = REPO / "v13"

MUTANT = None                      # set from the command line only
M_ON: dict = {}                    # {mutant name: bool}, filled once in main
OUT: list[str] = []

MUTANTS = {
    # name                          kind          what it perturbs
    "anchor-review-hash":          ("computation", "the frozen review's sha256 pin"),
    "anchor-nt-hash":              ("computation", "the NT terminal receipt's sha256 pin"),
    "anchor-gen-hash":             ("computation", "the GEN terminal receipt's sha256 pin"),
    "anchor-classcounts":          ("computation", "the reused 82/86/90/106 class counts"),
    "anchor-census":               ("computation", "the reused 4,096 / 89 / 96 census numbers"),
    "graph-drop-real2":            ("computation", "drops the t=2 realized-rule link"),
    "graph-add-full2":             ("computation", "adds a full-leg link at t=2"),
    "reduce-lax":                  ("computation", "allows immediate backtracking in the walks"),
    "lmax-lax":                    ("computation", "shortens the declared path bound"),
    "tree-lax":                    ("computation", "uses a link set that is not a spanning tree"),
    "cycle-lax":                   ("computation", "drops one link from every cycle class"),
    "field-lax":                   ("computation", "wrong reduction x^4 = x^2 - 1/4 in Q(cos pi/8)"),
    "rot-lax":                     ("computation", "perturbs one entry of the declared rotation R1"),
    "completion-lax":              ("computation", "perturbs one entry of the declared completion V"),
    "wingswap-lax":                ("computation", "wing exchange moves the systems only"),
    "base1-angle":                 ("computation", "reads the first base at an asymmetric setting"),
    "direct-order":                ("computation", "wrong composition order in the direct comparator"),
    "reverse-lax":                 ("computation", "reverse traversal without transposing"),
    "admission-lax":               ("computation", "flips one cell of the read admission table"),
    "basis-lax":                   ("computation", "duplicates one declared cycle in the basis"),
    "control-completion":          ("computation", "gives the equivariant control a defect"),
    "prep-lax":                    ("computation", "gives the two frames different preparation legs"),
    "freeze-lax":                  ("computation", "computes a profile before the candidate freeze"),
    "candidate-lax":               ("computation", "weakens a declared candidate predicate"),
    "violator-lax":                ("computation", "builds a violator that does not violate"),
    "gauge-head":                  ("computation", "mis-conventioned gauge action (head only)"),
    "memo-lax":                    ("computation", "lets the self-test read the value cache"),
    "species-lax":                 ("computation", "drops one species clause from the derivation"),
    "float-lax":                   ("computation", "introduces a float into a gated value"),
    "exempt-lax":                  ("computation", "registers a mutant-identity comparison"),
    "control-lax":                 ("waiver",      "waives the positive control"),
    "chain-lax":                   ("waiver",      "waives the chain/candidate consistency"),
    "order-lax":                   ("waiver",      "waives the freeze-order predicate"),
    "verdict-lax":                 ("waiver",      "waives the verdict vocabulary"),
    "flip-lax":                    ("waiver",      "waives the spanning-tree flip-test"),
}


# ---------------------------------------------------------------------------
# 0.  house: printing, anchors, gates
# ---------------------------------------------------------------------------

def say(s: str = "") -> None:
    OUT.append(s)


ANCHORS: list[dict] = []
GATES: list[dict] = []
FAILED_ANCHOR: list[str] = []


def anchor(name: str, got, want, why: str) -> None:
    """Exit-1-only: a committed number this unit reuses."""
    ok = (got == want)
    ANCHORS.append({"name": name, "ok": ok, "got": _j(got), "want": _j(want),
                    "why": why})
    if not ok:
        FAILED_ANCHOR.append(name)
        say("")
        say("ANCHOR FAILURE  %s" % name)
        say("   got  : %s" % (_j(got),))
        say("   want : %s" % (_j(want),))
        say("   why  : %s" % why)
        sofar = [g["name"] for g in GATES
                 if g["kind"] == "must-pass" and not g["ok"]]
        if sofar:
            say("FAILED: %s" % ", ".join(sofar))
        _flush_and_exit(1)


def gate(name: str, ok: bool, kind: str, evidence) -> bool:
    GATES.append({"index": len(GATES), "name": name, "ok": bool(ok),
                  "kind": kind, "evidence": _j(evidence)})
    return bool(ok)


def _j(v):
    if isinstance(v, Fraction):
        return str(v)
    if isinstance(v, tuple):
        return [_j(x) for x in v]
    if isinstance(v, list):
        return [_j(x) for x in v]
    if isinstance(v, dict):
        return {str(k): _j(x) for k, x in v.items()}
    if isinstance(v, set):
        return sorted(_j(x) for x in v)
    return v


def _flush_and_exit(code: int) -> None:
    sys.stdout.write("\n".join(OUT) + "\n")
    sys.stdout.flush()
    sys.exit(code)


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def progress(msg: str) -> None:
    sys.stderr.write("[xba] %s\n" % msg)
    sys.stderr.flush()


# ---------------------------------------------------------------------------
# 1.  exact arithmetic: the quartic field Q(cos pi/8) and sparse matrices
# ---------------------------------------------------------------------------
# x = cos(pi/8) has minimal polynomial 8x^4 - 8x^2 + 1, so x^4 = x^2 - 1/8.
# Elements are 4-tuples of Fractions; tuple equality IS field equality.

QZERO = (Fraction(0),) * 4
QONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))


def q_add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def q_neg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def q_mul(a, b):
    c = [Fraction(0)] * 7
    for i in range(4):
        if a[i]:
            ai = a[i]
            for j in range(4):
                if b[j]:
                    c[i + j] += ai * b[j]
    red = Fraction(1, 8)
    if MUTANT == "field-lax":
        red = Fraction(1, 4)
    r = [c[0], c[1], c[2], c[3]]
    r[2] += c[4]
    r[0] -= c[4] * red
    r[3] += c[5]
    r[1] -= c[5] * red
    r[2] += c[6] * (1 - red)
    r[0] -= c[6] * red
    return (r[0], r[1], r[2], r[3])


def q_nonzero(a):
    return a != QZERO


class RatRing:
    """the rationals, in the same interface as the quartic field."""
    zero = Fraction(0)
    one = Fraction(1)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def neg(a):
        return -a

    @staticmethod
    def nonzero(a):
        return a != 0


class QuarticRing:
    """Q(cos pi/8) as reduced rational 4-tuples."""
    zero = QZERO
    one = QONE
    add = staticmethod(q_add)
    mul = staticmethod(q_mul)
    neg = staticmethod(q_neg)
    nonzero = staticmethod(q_nonzero)


def sp_mul(K, A, B):
    """sparse (row, col) -> value matrix product, A @ B."""
    bycol = {}
    for (i, k), v in A.items():
        bycol.setdefault(k, []).append((i, v))
    out = {}
    for (k, j), v in B.items():
        for (i, u) in bycol.get(k, ()):
            t = K.mul(u, v)
            if K.nonzero(t):
                key = (i, j)
                s = K.add(out.get(key, K.zero), t)
                if K.nonzero(s):
                    out[key] = s
                else:
                    out.pop(key, None)
    return out


def sp_T(A):
    return {(j, i): v for (i, j), v in A.items()}


def sp_eye(K, n):
    return {(i, i): K.one for i in range(n)}


def sp_is_orthogonal(K, A, n):
    return sp_mul(K, sp_T(A), A) == sp_eye(K, n)


def perm_part(K, A, n):
    """the permutation part of a signed permutation matrix, or None."""
    p = [None] * n
    minus = K.neg(K.one)
    for (i, j), v in A.items():
        if not K.nonzero(v):
            continue
        allowed = (v == K.one or v == minus)
        if not allowed or p[j] is not None:
            return None
        p[j] = i
    return tuple(p) if all(x is not None for x in p) else None


# ---------------------------------------------------------------------------
# 2.  the external pins and every reused number
# ---------------------------------------------------------------------------

PIN_SHA = "7cbde5da42805e454628a99e7e2f6aea2783583b174d024a38cd2f9fe49e9722"
NT_RECEIPT_SHA = "d256891b479a8636fe88df5e9b0f553998140f1553fdfc167662220b44eeb03e"
GEN_RECEIPT_SHA = "e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292"
REVIEW_SHA = "1d17534ef9f4c6e1d1c590800a95114c0e0f754f84822d0240ba28685b897796"


def read_sources():
    """hash-pin the frozen sources and read every number this unit reuses."""
    p_pin = V13 / "note-xba-crossbase-pin.md"
    p_nt = HERE / "nt_transport_receipt.json"
    p_gen = HERE / "gen_generality_receipt.json"
    p_rev = V13 / "review-gen-operator.md"

    h_pin, h_nt, h_gen, h_rev = (sha256_of(p) for p in (p_pin, p_nt, p_gen, p_rev))
    if MUTANT == "anchor-nt-hash":
        h_nt = h_nt[:-1] + ("0" if h_nt[-1] != "0" else "1")
    if MUTANT == "anchor-gen-hash":
        h_gen = h_gen[:-1] + ("0" if h_gen[-1] != "0" else "1")
    if MUTANT == "anchor-review-hash":
        h_rev = h_rev[:-1] + ("0" if h_rev[-1] != "0" else "1")

    anchor("A01 pin sha256", h_pin, PIN_SHA, "the XBA pin this unit is bound to")
    anchor("A02 NT terminal receipt sha256", h_nt, NT_RECEIPT_SHA,
           "the first base's committed terminal receipt")
    anchor("A03 GEN terminal receipt sha256", h_gen, GEN_RECEIPT_SHA,
           "base G's committed terminal receipt")
    anchor("A04 frozen operator review sha256", h_rev, REVIEW_SHA,
           "the frozen review whose 4,096-enumeration supplies the external anchors")

    nt = json.loads(p_nt.read_text())
    gen = json.loads(p_gen.read_text())
    rev = p_rev.read_text()
    return nt, gen, rev, {"pin": h_pin, "nt": h_nt, "gen": h_gen, "review": h_rev}


def parse_review_numbers(rev: str) -> dict:
    """read the frozen review's own table, rather than typing its numbers."""
    want = {
        "distinct_profiles": ("| distinct class-count profiles produced |", 89),
        "profile_hits": ("| connections reproducing $(106,90,86,82)$ |", 96),
        "order4": ("| connections whose generated group has order 4 |", 3906),
        "most_common": ("| most common profile |", 384),
    }
    out = {}
    for key, (prefix, _default) in want.items():
        line = next((ln for ln in rev.splitlines() if ln.startswith(prefix)), None)
        if line is None:
            raise SystemExit("XBA: frozen review line missing: %s" % prefix)
        line = re.sub(r"\([^)]*%[^)]*\)", "", line)   # drop the review's percentages
        body = line[len(prefix):]
        prev = None
        while prev != body:                           # join thousands separators
            prev = body
            body = re.sub(r"(?<=\d),(\d{3})(?!\d)", r"\1", body)
        out[key] = [int(m) for m in re.findall(r"\d+", body)]
    return out


# ---------------------------------------------------------------------------
# 3.  the shared arena, read from the two receipts' own admission tables
# ---------------------------------------------------------------------------

SETTING_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}


def admission_from_nt(nt) -> dict:
    """(setting index, checkpoint) -> {rule: (n_admitted, map name or None)}"""
    tab = {}
    for cell, rec in nt["tables"]["mechanism"]["identification_multiplicity"].items():
        setting, tt = cell.split("/")
        si = SETTING_INDEX[setting.split("-")[1]]
        t = int(tt[1:])
        counts = rec["admitted_count_per_rule"]
        maps = rec["admitted_maps"]
        # the receipt lists the admitted maps in rule order FULL then REAL
        per = {}
        k = 0
        for rule in ("FULL", "REAL"):
            n = counts[rule]
            per[rule] = (n, maps[k] if n == 1 else None)
            k += n
        if MUTANT == "admission-lax" and (si, t) == (0, 2):
            per["REAL"] = (1, "the wing exchange")
        tab[(si, t)] = per
    return tab


def admission_from_gen(gen) -> dict:
    tab = {}
    for cell, rec in gen["tables"]["admission"]["per_cell"].items():
        setting, tt = cell.split("/")
        si = SETTING_INDEX[setting.split("-")[1]]
        t = int(tt[1:])
        per = {}
        for rule in ("FULL", "REAL"):
            n = rec[rule]["n_admitted"]
            per[rule] = (n, rec[rule]["maps"][0] if n == 1 else None)
        tab[(si, t)] = per
    return tab


# the graph, built from the admission table at a symmetric setting.
# nodes: frame*4 + t, frame 0 = F1, frame 1 = F2.
def build_graph(adm_symmetric: dict, nlegs: int):
    """links = [(tail, head, kind, label)]; kind in LEG / FULL / REAL."""
    links = []
    for fr in (0, 1):
        for t in range(1, nlegs + 1):
            links.append((fr * 4 + t - 1, fr * 4 + t, "LEG", "LEG_F%d_%d" % (fr + 1, t)))
    for rule in ("FULL", "REAL"):
        for t in range(nlegs + 1):
            n, _name = adm_symmetric[t][rule]
            drawn = (n == 1)
            if MUTANT == "graph-drop-real2" and rule == "REAL" and t == 2:
                drawn = False
            if MUTANT == "graph-add-full2" and rule == "FULL" and t == 2:
                drawn = True
            if drawn:
                links.append((t, 4 + t, rule, "%s@%d" % (rule, t)))
    return links


def adjacency(links):
    adj = {}
    for i, (a, b, _k, _n) in enumerate(links):
        adj.setdefault(a, []).append((i, b, False))
        adj.setdefault(b, []).append((i, a, True))
    return adj


def enumerate_walks(links, base, lmax, allowed=None):
    """reduced walks from `base` back to `base`, as tuples of (link, reversed)."""
    adj = adjacency(links)
    allow = set(range(len(links))) if allowed is None else set(allowed)
    out = []
    stack = [(base, -1, 0, ())]
    while stack:
        v, last, ln, seq = stack.pop()
        if ln > 0 and v == base:
            out.append(seq)
        if ln < lmax:
            for (li, w, rev) in adj.get(v, ()):
                if li not in allow:
                    continue
                if li == last and not M_ON["reduce-lax"]:
                    continue
                stack.append((w, li, ln + 1, seq + ((li, rev),)))
    return out


def enumerate_all_walks(links, lmax):
    """every reduced walk from every node (length 0 included), and the closed ones."""
    adj = adjacency(links)
    nodes = sorted({a for (a, b, _k, _n) in links} | {b for (a, b, _k, _n) in links})
    total = 0
    closed = 0
    for s in nodes:
        stack = [(s, -1, 0)]
        while stack:
            v, last, ln = stack.pop()
            total += 1
            if ln > 0 and v == s:
                closed += 1
            if ln < lmax:
                for (li, w, _rev) in adj.get(v, ()):
                    if li == last and not M_ON["reduce-lax"]:
                        continue
                    stack.append((w, li, ln + 1))
    return len(nodes), total, closed


def components(links, nnodes):
    parent = list(range(nnodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (a, b, _k, _n) in links:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return len({find(i) for i in range(nnodes)})


def spanning_tree(links, nnodes, prefer):
    """a spanning tree, links tried in the declared order `prefer`."""
    parent = list(range(nnodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    tree = []
    for i in prefer:
        a, b = links[i][0], links[i][1]
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            tree.append(i)
    if MUTANT == "tree-lax":
        tree = tree[:-1]
    return tree


def cycle_coords(links, tree, nnodes):
    """coordinate of each link in H_1(G;F2), in the cotree basis."""
    cot = [i for i in range(len(links)) if i not in set(tree)]
    pos = {li: k for k, li in enumerate(cot)}
    coord = [0] * len(links)
    for li in cot:
        coord[li] = 1 << pos[li]
    if MUTANT == "cycle-lax" and cot:
        coord[cot[0]] = 0
    return cot, coord


def walk_class(seq, coord):
    c = 0
    for (li, _rev) in seq:
        c ^= coord[li]
    return c


def edgeset_class(edges, coord):
    c = 0
    for li in edges:
        c ^= coord[li]
    return c


# ---------------------------------------------------------------------------
# 4.  the two bases, rebuilt from scratch
# ---------------------------------------------------------------------------

class Base:
    """a rebuilt species instance: legs, wing exchange, defect, labels."""

    def __init__(self, name, K, n, legs_by_frame, PW, note):
        self.name = name
        self.K = K
        self.n = n
        self.legs = legs_by_frame          # {"F1": [L1, L2, L3], "F2": [...]}
        self.PW = PW
        self.note = note
        self.I = sp_eye(K, n)
        self.T = {}
        for fr in ("F1", "F2"):
            self.T[(fr, 0)] = dict(self.I)
            for t in range(1, len(legs_by_frame[fr]) + 1):
                self.T[(fr, t)] = sp_mul(K, legs_by_frame[fr][t - 1], self.T[(fr, t - 1)])
        self.D = sp_mul(K, PW, sp_mul(K, sp_T(self.T[("F1", 1)]),
                                      sp_mul(K, PW, self.T[("F1", 1)])))

    def group(self):
        K, n = self.K, self.n
        elems = {
            "1": perm_part(K, self.I, n),
            "W": perm_part(K, self.PW, n),
            "D": perm_part(K, self.D, n),
            "WD": perm_part(K, sp_mul(K, self.PW, self.D), n),
        }
        return elems

    def fixed(self, name):
        p = self.group()[name]
        return None if p is None else sum(1 for i in range(self.n) if p[i] == i)

    def gauge_fixed_labels(self, links):
        """T_head^{-1} M_link T_tail, as an element name of {1,W,D,WD}."""
        K = self.K
        names = self.group()
        inv = {v: k for k, v in names.items()}
        out = {}
        for (a, b, kind, lab) in links:
            fa, ta = ("F1", a) if a < 4 else ("F2", a - 4)
            fb, tb = ("F1", b) if b < 4 else ("F2", b - 4)
            if kind == "LEG":
                M = self.legs[fa][ta]
            elif kind == "FULL":
                M = self.I
            else:
                M = self.PW
            g = sp_mul(K, sp_T(self.T[(fb, tb)]), sp_mul(K, M, self.T[(fa, ta)]))
            pp = perm_part(K, g, self.n)
            out[lab] = inv.get(pp)
        return out

    def link_matrix(self, links, li, reverse):
        a, b, kind, _lab = links[li]
        fa, ta = ("F1", a) if a < 4 else ("F2", a - 4)
        if kind == "LEG":
            M = self.legs[fa][ta]
        elif kind == "FULL":
            M = self.I
        else:
            M = self.PW
        if reverse and not M_ON["reverse-lax"]:
            return sp_T(M)
        return M


def wing_swap(n_s, n_p):
    """the wing exchange on (sA, sB, pA, pB) with the declared index map."""
    def f(i):
        pb = i % n_p
        pa = (i // n_p) % n_p
        sb = (i // (n_p * n_p)) % n_s
        sa = i // (n_s * n_p * n_p)
        if MUTANT == "wingswap-lax":
            return ((sb * n_s + sa) * n_p + pa) * n_p + pb
        return ((sb * n_s + sa) * n_p + pb) * n_p + pa
    return f


def perm_matrix(K, f, n):
    return {(f(i), i): K.one for i in range(n)}


# --- the first base: 36 configurations over Q(cos pi/8) ---------------------

def build_base_one(setting_angles):
    """(qA,qB,pA,pB), qX in {0,1}, pX in {r,+,-}; the singlet preparation."""
    K = QuarticRing
    n = 36
    cos = {0: QONE, 1: (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
           2: (Fraction(-1), Fraction(0), Fraction(2), Fraction(0)),
           3: (Fraction(0), Fraction(-3), Fraction(0), Fraction(4)),
           4: QZERO}
    sin = {k: cos[4 - k] for k in range(5)}

    def idx(qa, qb, pa, pb):
        return ((qa * 2 + qb) * 3 + pa) * 3 + pb

    r2 = cos[2]                                # cos(pi/4) = 1/sqrt 2
    Vq = [[QZERO, QZERO, QONE, QZERO],
          [r2, r2, QZERO, QZERO],
          [q_neg(r2), r2, QZERO, QZERO],
          [QZERO, QZERO, QZERO, QONE]]
    Uprep = {}
    for a1 in range(4):
        for a0 in range(4):
            if K.nonzero(Vq[a1][a0]):
                for p in range(9):
                    Uprep[(a1 * 9 + p, a0 * 9 + p)] = Vq[a1][a0]

    def U_local(wing, angle8):
        half = angle8 // 2
        c, s = cos[half], sin[half]
        Pp = [[q_mul(c, c), q_mul(c, s)], [q_mul(s, c), q_mul(s, s)]]
        Pm = [[q_mul(s, s), q_neg(q_mul(s, c))], [q_neg(q_mul(c, s)), q_mul(c, c)]]
        sh = {0: 1, 1: 2, 2: 0}
        out = {}
        for qa0 in range(2):
            for qb0 in range(2):
                for pa0 in range(3):
                    for pb0 in range(3):
                        j = idx(qa0, qb0, pa0, pb0)
                        q0 = qa0 if wing == "A" else qb0
                        p0 = pa0 if wing == "A" else pb0
                        for (P, shift) in ((Pp, 1), (Pm, 2)):
                            p1 = p0
                            for _ in range(shift):
                                p1 = sh[p1]
                            for q1 in range(2):
                                v = P[q1][q0]
                                if not K.nonzero(v):
                                    continue
                                i = idx(q1, qb0, p1, pb0) if wing == "A" else idx(qa0, q1, pa0, p1)
                                cur = q_add(out.get((i, j), QZERO), v)
                                if K.nonzero(cur):
                                    out[(i, j)] = cur
                                else:
                                    out.pop((i, j), None)
        return out

    a8, b8 = setting_angles
    UA, UB = U_local("A", a8), U_local("B", b8)
    prep2 = Uprep
    if MUTANT == "prep-lax":
        prep2 = U_local("A", 0)
    legs = {"F1": [Uprep, UA, UB], "F2": [prep2, UB, UA]}
    PW = perm_matrix(K, wing_swap(2, 3), n)
    return Base("base 1", K, n, legs, PW,
                "36 configurations, qubit wings, the singlet, Q(cos pi/8)")


# --- base G: 81 configurations over Q --------------------------------------

def euler_rodrigues(q):
    w, x, y, z = (Fraction(t) for t in q)
    nn = w * w + x * x + y * y + z * z
    M = [[w * w + x * x - y * y - z * z, 2 * (x * y - w * z), 2 * (x * z + w * y)],
         [2 * (x * y + w * z), w * w - x * x + y * y - z * z, 2 * (y * z - w * x)],
         [2 * (x * z - w * y), 2 * (y * z + w * x), w * w - x * x - y * y + z * z]]
    return [[e / nn for e in row] for row in M]


def build_qutrit_base(name, quats, setting, psi, transposition, note):
    """the (s_A,s_B,p_A,p_B) species instance with 3-state wings, over Q."""
    K = RatRing
    n = 81
    R = [euler_rodrigues(q) for q in quats]
    if MUTANT == "rot-lax" and len(R) > 1:
        R[1][1][1] = R[1][1][1] + Fraction(1, 100)

    def idx(sa, sb, pa, pb):
        return ((sa * 3 + sb) * 3 + pa) * 3 + pb

    def U_local(wing, g):
        Rg = R[g]
        out = {}
        for sa0 in range(3):
            for sb0 in range(3):
                for pa0 in range(3):
                    for pb0 in range(3):
                        j = idx(sa0, sb0, pa0, pb0)
                        s0 = sa0 if wing == "A" else sb0
                        p0 = pa0 if wing == "A" else pb0
                        for o in range(3):
                            p1 = (p0 + o) % 3
                            for s1 in range(3):
                                v = Rg[s1][o] * Rg[s0][o]
                                if not v:
                                    continue
                                i = idx(s1, sb0, p1, pb0) if wing == "A" else idx(sa0, s1, pa0, p1)
                                cur = out.get((i, j), Fraction(0)) + v
                                if cur:
                                    out[(i, j)] = cur
                                else:
                                    out.pop((i, j), None)
        return out

    w = [psi[k] - (Fraction(1) if k == 0 else Fraction(0)) for k in range(9)]
    ww = sum(t * t for t in w)
    H = [[(Fraction(1) if a == b else Fraction(0)) - 2 * w[a] * w[b] / ww
          for b in range(9)] for a in range(9)]
    perm = list(range(9))
    if transposition is not None:
        i, j = transposition
        perm[i], perm[j] = perm[j], perm[i]
    Qm = [[Fraction(0)] * 9 for _ in range(9)]
    for b in range(9):
        Qm[perm[b]][b] = Fraction(1)
    V = [[sum(H[a][k] * Qm[k][b] for k in range(9)) for b in range(9)] for a in range(9)]
    if MUTANT == "completion-lax":
        V[0][0] = V[0][0] + Fraction(1, 100)
    Uprep = {}
    for a1 in range(9):
        for a0 in range(9):
            if V[a1][a0]:
                for p in range(9):
                    Uprep[(a1 * 9 + p, a0 * 9 + p)] = V[a1][a0]

    gA, gB = setting
    UA, UB = U_local("A", gA), U_local("B", gB)
    prep2 = Uprep
    if MUTANT == "prep-lax":
        prep2 = U_local("A", 0)
    legs = {"F1": [Uprep, UA, UB], "F2": [prep2, UB, UA]}
    PW = perm_matrix(K, wing_swap(3, 3), n)
    b = Base(name, K, n, legs, PW, note)
    b.R = R
    b.V = V
    b.psi = psi
    return b


# ---------------------------------------------------------------------------
# 5.  the connection space and the profile
# ---------------------------------------------------------------------------
# V4 as {0,1,2,3} under XOR: 0 = the identity, 1 = W the base's wing
# exchange, 2 = D the base's preparation defect, 3 = WD.

V4NAME = {0: "1", 1: "W", 2: "D", 3: "WD"}
PROFILE_EVALS = [0]
HOLCACHE: dict = {}
CACHE_STATS = {"hits": 0, "misses": 0, "bypassed_lookups": 0, "primed": 0,
               "reserved_returns": 0}


def make_profiler(class_hist):
    """profile(phi) = the class counts of the based closed walks."""
    items = list(class_hist.items())

    def profile(phi):
        PROFILE_EVALS[0] += 1
        cnt = [0, 0, 0, 0]
        for c, m in items:
            h = 0
            for i in range(len(phi)):
                if c >> i & 1:
                    h ^= phi[i]
            cnt[h] += m
        return tuple(cnt)
    return profile


def generated_group(vals):
    g = {0}
    for x in vals:
        g |= {y ^ x for y in g}
    return g


def hol_of_class(phi, c):
    h = 0
    for i in range(len(phi)):
        if c >> i & 1:
            h ^= phi[i]
    return h


# ---------------------------------------------------------------------------
# 6.  the main run
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    global MUTANT
    ap = argparse.ArgumentParser()
    ap.add_argument("--delivery", action="store_true")
    ap.add_argument("--mutant", default=None)
    ap.add_argument("--no-census", action="store_true",
                    help="skip the mutant census (construction aid; never used "
                         "for a delivery run)")
    ap.add_argument("--falsification-selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.mutant is not None and args.mutant not in MUTANTS:
        raise SystemExit("unknown mutant: %s" % args.mutant)
    MUTANT = args.mutant
    M_ON.clear()
    M_ON.update({name: (MUTANT == name) for name in MUTANTS})

    if args.falsification_selftest:
        return run_falsification_selftest()

    say("=" * 78)
    say("XBA -- THE CROSS-BASE AGREEMENT HUNT")
    say("what shared structure forces the 82/86/90/106 profile on both bases")
    say("=" * 78)
    if MUTANT:
        say("MUTANT: %s -- %s" % (MUTANT, MUTANTS[MUTANT][1]))
    say("")

    # ---- 6.1 sources ------------------------------------------------------
    progress("reading and pinning the frozen sources")
    nt, gen, rev, hashes = read_sources()
    revnum = parse_review_numbers(rev)
    say("## 1  The frozen sources, pinned")
    say("")
    for k, v in hashes.items():
        say("   %-8s sha256 %s" % (k, v))
    say("")

    ce = gen["tables"]["connection_enumeration"]
    nt_cls = nt["tables"]["mechanism"]["single_rule_subconnections"]

    # the reused numbers, read not typed
    r_4096 = ce["the_size_of_the_connection_space"]
    r_89 = ce["distinct_class_count_profiles"]
    r_96 = ce["connections_reproducing_the_measured_profile"]
    r_3906 = ce["connections_whose_labels_generate_the_whole_group"]
    r_96b = ce["of_those_reproducing_the_measured_profile"]
    r_mc_profile, r_mc_count = ce["the_most_common_profile"]
    r_364 = ce["based_closed_walks_checked"]
    r_counts = tuple(ce["the_measured_class_counts"])
    if MUTANT == "anchor-census":
        r_89 = r_89 + 1
    if MUTANT == "anchor-classcounts":
        r_counts = (82, 86, 90, 107)

    anchor("A05 review: distinct profiles", revnum["distinct_profiles"], [r_89],
           "the frozen review's own table must agree with the GEN receipt")
    anchor("A06 review: profile hits / space", revnum["profile_hits"], [r_96, r_4096],
           "96 of 4,096, read from the frozen review")
    anchor("A07 review: order-4 connections", revnum["order4"], [r_3906],
           "3,906, read from the frozen review")
    anchor("A08 review: most common profile count", revnum["most_common"],
           [r_mc_profile[3], r_mc_profile[2], r_mc_profile[1], r_mc_profile[0],
            r_mc_count],
           "the review prints the most common profile descending; the receipt ascending")

    # ---- 6.2 the admission tables and the graph ---------------------------
    progress("rebuilding the common gauge-fixed graph from the admission tables")
    adm_nt = admission_from_nt(nt)
    adm_gen = admission_from_gen(gen)
    cells = sorted(set(adm_nt) | set(adm_gen))
    same = [c for c in cells if adm_nt.get(c) == adm_gen.get(c)]
    say("## 2  The common arena, rebuilt from the two receipts' admission tables")
    say("")
    say("   cells compared (setting index x checkpoint) : %d" % len(cells))
    say("   cells where the two bases draw the same rule/permutation : %d" % len(same))
    gate("XBA-ADMISSION-AGREEMENT",
         len(cells) > 0 and len(same) == len(cells), "must-pass",
         {"cells": len(cells), "agreeing": len(same)})
    anchor("A09 GEN cross-base admission cells", len(cells),
           gen["tables"]["cross_base_connection"]["cells_compared"],
           "the 24 matched cells GEN compared")
    anchor("A10 GEN cross-base admission agreement", len(same),
           gen["tables"]["cross_base_connection"]
              ["cells_where_the_two_bases_draw_the_same_permutation_per_rule"],
           "GEN's 24/24 agreement, recomputed here from both receipts")

    sym = {t: adm_nt[(4, t)] for t in range(4)}     # setting index 4 = SP-E / GP-E
    links = build_graph(sym, nlegs=3)
    NAMES = [lab for (_a, _b, _k, lab) in links]
    nnodes, total_walks, closed_walks = enumerate_all_walks(links, lmax=8)
    ncomp = components(links, nnodes)
    lmax = 6 if M_ON["lmax-lax"] else 8
    walks = enumerate_walks(links, base=0, lmax=lmax)
    nt_sym = nt_cls["SP-E/FULL+REAL"]
    say("")
    say("   nodes %d   links %d   identification links %d   components %d"
        % (nnodes, len(links),
           sum(1 for l in links if l[2] != "LEG"), ncomp))
    say("   reduced walks (all base points, length 0 included) : %s"
        % format(total_walks, ","))
    say("   closed walks (length 0 excluded)                   : %s"
        % format(closed_walks, ","))
    say("   closed walks based at F1@t0                        : %d" % len(walks))

    # walk audit, recomputed from the delivered rows
    adj = adjacency(links)
    bad_backtrack = sum(1 for s in walks
                        for i in range(1, len(s)) if s[i][0] == s[i - 1][0])
    bad_walk = 0
    for s in walks:
        v = 0
        for (li, rev) in s:
            a, b = links[li][0], links[li][1]
            if rev:
                a, b = b, a
            if a != v:
                bad_walk += 1
                break
            v = b
        else:
            if v != 0:
                bad_walk += 1
    cyc_rank = len(links) - nnodes + ncomp
    gate("XBA-WALK-AUDIT",
         bad_backtrack == 0 and bad_walk == 0 and ncomp == 1
         and cyc_rank == nt_sym["cycle_rank"],
         "must-pass", {"immediate_repeats": bad_backtrack, "not_a_walk": bad_walk,
                       "components": ncomp, "cycle_rank": cyc_rank})

    tree = spanning_tree(links, nnodes, prefer=list(range(len(links))))
    cot, coord = cycle_coords(links, tree, nnodes)
    say("   spanning tree : %s" % ", ".join(NAMES[i] for i in tree))
    say("   cotree        : %s" % ", ".join(NAMES[i] for i in cot))
    gate("XBA-CYCLE-RANK", len(cot) == cyc_rank and len(tree) == nnodes - 1,
         "must-pass", {"cotree": len(cot), "tree": len(tree), "rank": cyc_rank})

    # the arena's own gates are all evaluated above; only now is it compared
    # against the committed receipts, so no anchor can pre-empt a gate.
    anchor("A11 links at a symmetric setting", len(links), nt_sym["links"],
           "the NT receipt's own link count")
    anchor("A12 identification links", sum(1 for l in links if l[2] != "LEG"),
           nt_sym["identification_links"], "the NT receipt's own count")
    anchor("A13 reduced walks at a symmetric setting", total_walks,
           gen["tables"]["path_space"]["GP-E"]["paths"], "GEN's own path count")
    anchor("A14 closed walks at a symmetric setting", closed_walks,
           gen["tables"]["path_space"]["GP-E"]["closed_paths"], "GEN's own count")
    anchor("A15 based closed walks", len(walks), r_364,
           "the 364 walks the frozen review re-counted combinatorially")
    anchor("A16 based closed walks (NT)", len(walks), nt_sym["closed_paths_at_F1_t0"],
           "the NT receipt's own count")
    anchor("A34 spanning tree, cotree, nodes reached",
           [len(tree), len(cot), nnodes],
           [len(ce["spanning_tree_links"]), ce["independent_cycles"],
            ce["nodes_reached_by_the_spanning_tree"]],
           "the frozen review's own gauge-fixing shape, read from the GEN receipt")

    class_hist = collections.Counter(walk_class(s, coord) for s in walks)
    profile = make_profiler(class_hist)
    say("   distinct cycle classes carried by the 364 walks    : %d" % len(class_hist))

    # the declared cycle basis, built from the graph and the two rules
    L = {lab: i for i, (_a, _b, _k, lab) in enumerate(links)}

    def legpath(fr, t):
        return [L["LEG_F%d_%d" % (fr, k)] for k in range(1, t + 1)]

    BASIS = collections.OrderedDict()
    BASIS["SQ_FULL_1"] = [L["FULL@0"], L["LEG_F1_1"], L["FULL@1"], L["LEG_F2_1"]]
    BASIS["CANON"] = ([L["FULL@0"]] + legpath(1, 3) + [L["FULL@3"]] + legpath(2, 3))
    BASIS["SQ_REAL_1"] = [L["REAL@0"], L["LEG_F1_1"], L["REAL@1"], L["LEG_F2_1"]]
    BASIS["SQ_REAL_2"] = [L["REAL@1"], L["LEG_F1_2"], L["REAL@2"], L["LEG_F2_2"]]
    BASIS["SQ_REAL_3"] = [L["REAL@2"], L["LEG_F1_3"], L["REAL@3"], L["LEG_F2_3"]]
    BASIS["BIGON_0"] = [L["FULL@0"], L["REAL@0"]]
    if M_ON["basis-lax"]:
        BASIS["BIGON_0"] = list(BASIS["SQ_FULL_1"])
    BCLS = {k: edgeset_class(v, coord) for k, v in BASIS.items()}
    BKEYS = list(BASIS)

    # independence of the declared basis over F2
    rows = [BCLS[k] for k in BKEYS]
    piv, rank = [], 0
    for r in rows:
        for p in piv:
            r = min(r, r ^ p)
        if r:
            piv.append(r)
            piv.sort(reverse=True)
            rank += 1
    gate("XBA-BASIS-INDEPENDENT", rank == 6, "must-pass",
         {"rank": rank, "cycles": BKEYS})

    # change of coordinates: cotree values -> declared-basis values
    M = [[(BCLS[k] >> i) & 1 for i in range(6)] for k in BKEYS]
    Minv = invert_f2(M)
    gate("XBA-BASIS-INVERTIBLE", Minv is not None, "must-pass",
         {"declared_basis": BKEYS})
    basis_fail = [g["name"] for g in GATES
                  if g["name"].startswith("XBA-BASIS-") and not g["ok"]]
    if basis_fail:                      # fail-closed: no coordinates, no results
        say("")
        say("FAILED: %s" % ", ".join(g["name"] for g in GATES
                                     if g["kind"] == "must-pass" and not g["ok"]))
        say("   the declared cycle basis is not a basis; every downstream "
            "measurement is refused.")
        _flush_and_exit(1)

    def beta_of(phi):
        """the connection's values on the declared cycle basis."""
        return tuple(hol_of_class(phi, BCLS[k]) for k in BKEYS)

    def phi_of_beta(beta):
        """the cotree assignment realising declared-basis values `beta`."""
        out = [0] * 6
        for bit in range(2):
            col = [(beta[i] >> bit) & 1 for i in range(6)]
            sol = f2_solve(Minv, col)
            for i in range(6):
                out[i] |= sol[i] << bit
        return tuple(out)

    # sub-connection cycle spaces
    def rule_links(rules):
        return [i for i, (_a, _b, k, _n) in enumerate(links)
                if k == "LEG" or k in rules]
    FULLW = enumerate_walks(links, 0, lmax, allowed=rule_links({"FULL"}))
    REALW = enumerate_walks(links, 0, lmax, allowed=rule_links({"REAL"}))
    FULLCLS = sorted({walk_class(s, coord) for s in FULLW})
    REALCLS = sorted({walk_class(s, coord) for s in REALW})
    BIGCLS = {t: edgeset_class([L["FULL@%d" % t], L["REAL@%d" % t]], coord)
              for t in (0, 1, 3)}
    say("   FULL-only closed walks %d (cycle classes %d);  REAL-only %d (%d)"
        % (len(FULLW), len(FULLCLS), len(REALW), len(REALCLS)))
    anchor("A17 REAL-only closed walks", len(REALW),
           nt_cls["SP-E/REAL"]["closed_paths_at_F1_t0"],
           "the NT receipt's own realized-rule sub-connection count")
    anchor("A18 FULL-only closed walks", len(FULLW),
           nt_cls["SP-E/FULL"]["closed_paths_at_F1_t0"],
           "the NT receipt's own full-leg sub-connection count")

    # ---- 6.3 the two bases, rebuilt --------------------------------------
    progress("rebuilding base 1 (36 configurations, Q(cos pi/8))")
    say("")
    say("## 3  Both bases, rebuilt from scratch, and their connections")
    say("")
    bases = {}
    b1 = build_base_one((0, 2) if M_ON["base1-angle"] else (0, 0))    # SP-E
    b1f = build_base_one((2, 2))                     # SP-F
    progress("rebuilding base G (81 configurations, Q)")
    PSI_G = [Fraction(0)] * 9
    PSI_G[1] = Fraction(2, 3)
    PSI_G[3] = Fraction(2, 3)
    PSI_G[8] = Fraction(1, 3)
    bG = build_qutrit_base("base G", [(1, 0, 0, 0), (2, 1, 0, 0), (3, 0, 0, 2)],
                           (0, 0), PSI_G, (1, 2),
                           "81 configurations, qutrit wings, rational arithmetic")
    bGf = build_qutrit_base("base G (GP-F)", [(1, 0, 0, 0), (2, 1, 0, 0), (3, 0, 0, 2)],
                            (1, 1), PSI_G, (1, 2), "the second symmetric setting")
    for tag, b in (("base 1 @ SP-E", b1), ("base 1 @ SP-F", b1f),
                   ("base G @ GP-E", bG), ("base G @ GP-F", bGf)):
        bases[tag] = b

    # base declarations, anchored against the two papers' own printed data
    anchor("A19 base G rotation R1", [[str(x) for x in row] for row in bG.R[1]],
           [["1", "0", "0"], ["0", "3/5", "-4/5"], ["0", "4/5", "3/5"]],
           "the rotation printed in the generality paper")
    anchor("A20 base G rotation R2", [[str(x) for x in row] for row in bG.R[2]],
           [["5/13", "-12/13", "0"], ["12/13", "5/13", "0"], ["0", "0", "1"]],
           "the rotation printed in the generality paper")
    printedV = [["0", "0", "2/3", "2/3", "0", "0", "0", "0", "1/3"],
                ["2/3", "0", "5/9", "-4/9", "0", "0", "0", "0", "-2/9"],
                ["0", "1", "0", "0", "0", "0", "0", "0", "0"],
                ["2/3", "0", "-4/9", "5/9", "0", "0", "0", "0", "-2/9"],
                ["0", "0", "0", "0", "1", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "1", "0", "0"],
                ["0", "0", "0", "0", "0", "0", "0", "1", "0"],
                ["1/3", "0", "-2/9", "-2/9", "0", "0", "0", "0", "8/9"]]
    anchor("A21 base G completion V", [[str(x) for x in row] for row in bG.V],
           printedV, "the 9x9 completion printed in the generality paper, entry by entry")

    say("   | instance | carrier | W fixed | D fixed | D order 2 | legs commute |"
        " W intertwines leg2 | W intertwines prep |")
    say("   |---|---|---|---|---|---|---|---|")
    species_facts = {}
    for tag, b in bases.items():
        K = b.K
        UA = b.legs["F1"][1]
        UB = b.legs["F1"][2]
        commute = sp_mul(K, UA, UB) == sp_mul(K, UB, UA)
        inter2 = sp_mul(K, b.PW, sp_mul(K, UA, b.PW)) == UB
        interp = sp_mul(K, b.PW, sp_mul(K, b.legs["F1"][0], b.PW)) == b.legs["F1"][0]
        d2 = sp_mul(K, b.D, b.D) == b.I
        common_prep = b.legs["F1"][0] == b.legs["F2"][0]
        orth = all(sp_is_orthogonal(K, m, b.n) for m in b.legs["F1"] + b.legs["F2"])
        distinct4 = len({v for v in b.group().values() if v is not None}) == 4
        species_facts[tag] = {"legs_commute": commute, "W_intertwines_local_leg": inter2,
                              "W_intertwines_prep": interp, "D_is_an_involution": d2,
                              "common_preparation_leg": common_prep,
                              "every_declared_operator_is_orthogonal": orth,
                              "the_four_named_elements_are_distinct": distinct4,
                              "W_fixed": b.fixed("W"), "D_fixed": b.fixed("D")}
        say("   | %s | %d | %s | %s | %s | %s | %s | %s |"
            % (tag, b.n, b.fixed("W"), b.fixed("D"), d2, commute, inter2, interp))

    anchor("A22 base 1 wing exchange fixed points", b1.fixed("W"), 6,
           "the transport paper's own count (6 of 36)")
    anchor("A23 base 1 defect fixed points", b1.fixed("D"), 18,
           "the qubit-only wing swap, 18 of 36, named in the transport paper")
    anchor("A24 base G wing exchange fixed points", bG.fixed("W"), 9,
           "the generality paper's own count (9 of 81)")
    anchor("A25 base G defect fixed points", bG.fixed("D"), 45,
           "the generality paper's own count (45 of 81)")

    gate("XBA-SPECIES-CLAUSES-MEASURED",
         all(f["legs_commute"] and f["W_intertwines_local_leg"]
             and not f["W_intertwines_prep"] and f["D_is_an_involution"]
             and f["common_preparation_leg"]
             and f["every_declared_operator_is_orthogonal"]
             and f["the_four_named_elements_are_distinct"]
             for f in species_facts.values()),
         "must-pass", species_facts)

    # the gauge-fixed connections
    say("")
    say("   the gauge-fixed labels, computed on each rebuilt base:")
    say("")
    realized = {}
    for tag, b in bases.items():
        lab = b.gauge_fixed_labels(links)
        realized[tag] = lab
        say("   %-14s %s" % (tag, "  ".join("%s=%s" % (NAMES[i], lab[NAMES[i]])
                                            for i in range(len(links)))))
    outside = {tag: [k for k, v in lab.items() if v is None]
               for tag, lab in realized.items()}
    gate("XBA-LABELS-IN-THE-KLEIN-GROUP",
         all(not v for v in outside.values()), "must-pass",
         {"links_whose_label_is_outside_the_group": outside})

    NAME2V4 = {v: k for k, v in V4NAME.items()}
    phis = {}
    for tag, lab in realized.items():
        if any(lab[NAMES[i]] is None for i in cot):
            continue                       # fail-closed: no readable connection
        phis[tag] = tuple(NAME2V4[lab[NAMES[i]]] for i in cot)
    distinct_phi = sorted(set(phis.values()))
    if not distinct_phi:
        say("")
        say("FAILED: %s" % ", ".join(g["name"] for g in GATES
                                     if g["kind"] == "must-pass" and not g["ok"]))
        say("   no base yields a readable connection; every downstream "
            "measurement is refused.")
        _flush_and_exit(1)
    gate("XBA-THE-TWO-BASES-SHARE-ONE-CONNECTION",
         len(distinct_phi) == 1 and len(phis) == len(realized),
         "must-pass", {"readable_readings": len(phis),
                       "distinct_gauge_classes_over_all_four_readings":
                       len(distinct_phi),
                       "the_connection": {NAMES[cot[i]]: V4NAME[distinct_phi[0][i]]
                                          for i in range(6)}})
    PHI_R = distinct_phi[0]
    say("")
    say("   the declared cycle basis, on the realized connection:")
    for k, v in zip(BKEYS, beta_of(PHI_R)):
        say("      %-12s = %s" % (k, V4NAME[v]))

    # gauge-free comparator: the raw matrix product along every walk
    progress("independent comparator: the raw matrix product along all 364 walks")
    direct = {}
    for tag, b in (("base 1 @ SP-E", b1), ("base G @ GP-E", bG)):
        cnt = collections.Counter()
        mismatch = 0
        names = b.group()
        inv = {v: k for k, v in names.items()}
        for s in walks:
            A = b.I
            for (li, rev) in s:
                Ml = b.link_matrix(links, li, rev)
                A = sp_mul(b.K, A, Ml) if M_ON["direct-order"] else sp_mul(b.K, Ml, A)
            pp = perm_part(b.K, A, b.n)
            nm = inv.get(pp)
            cnt[nm] += 1
            if NAME2V4.get(nm) != hol_of_class(PHI_R, walk_class(s, coord)):
                mismatch += 1
        direct[tag] = {"class_counts": {k: cnt[k] for k in ("1", "W", "D", "WD")},
                       "walks_where_the_two_routes_disagree": mismatch}
    gate("XBA-DIRECT-COMPARATOR",
         all(d["walks_where_the_two_routes_disagree"] == 0 for d in direct.values()),
         "must-pass", direct)
    anchor("A36 the 364-walk model agreement",
           sum(d["walks_where_the_two_routes_disagree"] for d in direct.values()),
           ce["walks_where_the_cycle_model_disagrees_with_the_direct_holonomy"],
           "the frozen review's step 1: the combinatorial model reproduces the "
           "direct holonomy at every one of the 364 based closed walks")
    anchor("A35 links whose gauge-fixed label leaves the group",
           sum(len(v) for v in outside.values()),
           ce["links_whose_gauge_fixed_label_lies_outside_the_group"],
           "the frozen review measured every one of the 13 labels inside the group")

    # ---- 6.4 THE CANDIDATE DECLARATION -----------------------------------
    if MUTANT == "freeze-lax":
        profile(PHI_R)
    frozen_at = PROFILE_EVALS[0]
    say("")
    say("## 4  The candidate properties, declared (frozen before any profile)")
    say("")
    say("   profiles computed at the declaration point : %d" % frozen_at)
    gate("XBA-CANDIDATE-FREEZE", frozen_at == 0, "must-pass",
         {"profiles_computed_before_the_declaration": frozen_at})

    aut_typed, aut_full, act_typed, act_full = automorphisms(links, cot, coord, tree)
    say("   |Aut(graph)| rule-preserving %d, full multigraph %d;"
        % (aut_typed, aut_full))
    say("   distinct induced actions on the cycle space: %d (rule-preserving), %d (full)"
        % (len(act_typed), len(act_full)))

    CAND = declare_candidates(BKEYS, BCLS, FULLCLS, REALCLS, BIGCLS, act_full,
                              act_typed)
    for name, rec in CAND.items():
        say("   %-34s %s" % (name, rec["statement"]))
    gate("XBA-CANDIDATES-DECLARED", len(CAND) >= 10, "disclosure",
         {"note": "the declaration itself is a disclosure; its teeth are the "
                  "freeze gate before it and the consistency gate after it",
          "candidates": list(CAND)})
    DECLARATION_GATE_INDEX = len(GATES) - 1

    # ---- 6.5 the 4,096-connection census ---------------------------------
    progress("enumerating the 4,096 Klein-four connections")
    say("")
    say("## 5  The connection space, enumerated exhaustively")
    say("")
    ALLPHI = list(itertools.product(range(4), repeat=6))
    PROF = {p: profile(p) for p in ALLPHI}
    TARGET = PROF[PHI_R]
    SORTED_TARGET = tuple(sorted(TARGET))
    prof_hist = collections.Counter(tuple(sorted(v)) for v in PROF.values())
    hits_sorted = [p for p in ALLPHI if tuple(sorted(PROF[p])) == SORTED_TARGET]
    hits_labelled = [p for p in ALLPHI if PROF[p] == TARGET]
    order4 = [p for p in ALLPHI if len(generated_group(p)) == 4]
    hits_in_order4 = [p for p in hits_sorted if len(generated_group(p)) == 4]
    mc_profile, mc_count = max(prof_hist.items(),
                               key=lambda kv: (kv[1], kv[0]))

    say("   connection space              : %s" % format(len(ALLPHI), ","))
    say("   distinct class-count profiles : %d" % len(prof_hist))
    say("   the realized profile          : 1=%d W=%d D=%d WD=%d" % TARGET)
    say("   connections reproducing it (as a multiset)  : %d of %d"
        % (len(hits_sorted), len(ALLPHI)))
    say("   connections reproducing it element by element : %d" % len(hits_labelled))
    say("   connections whose labels generate the group : %d" % len(order4))
    say("   of those, reproducing the profile           : %d" % len(hits_in_order4))
    say("   most common profile           : %s at %d connections"
        % (list(mc_profile), mc_count))

    anchor("A26 connection space size", len(ALLPHI), r_4096, "the frozen review's 4,096")
    anchor("A27 distinct profiles", len(prof_hist), r_89, "the frozen review's 89")
    anchor("A28 profile hits", len(hits_sorted), r_96, "the frozen review's 96")
    anchor("A29 order-4 connections", len(order4), r_3906, "the frozen review's 3,906")
    anchor("A30 order-4 profile hits", len(hits_in_order4), r_96b,
           "the frozen review's 96 of 3,906")
    anchor("A31 most common profile", [list(mc_profile), mc_count],
           [list(r_mc_profile), r_mc_count], "the frozen review's (102,94,90,78) at 384")
    anchor("A32 the realized class counts", list(SORTED_TARGET), list(r_counts),
           "82/86/90/106, the profile both terminal receipts record")
    ntE = nt_cls["SP-E/FULL+REAL"]["holonomy_classes"]
    anchor("A33 the realized class counts, element by element",
           {"1": TARGET[0], "W": TARGET[1], "D": TARGET[2], "WD": TARGET[3]},
           {"1": ntE["the identity"], "W": ntE["the wing exchange"],
            "D": ntE["the qubit-only wing swap"],
            "WD": ntE["the pointer-only wing swap"]},
           "the NT receipt names its elements; the counts must match element by element")

    # ---- 6.6 the candidates, measured ------------------------------------
    progress("measuring the declared candidates")
    say("")
    say("## 6  The candidates, measured")
    say("")
    say("   | candidate | both bases satisfy | subset | forces (multiset) |"
        " forces (element-wise) | hits in subset | shrink |")
    say("   |---|---|---|---|---|---|---|")
    results = {}
    for name, rec in CAND.items():
        pred = rec["pred"]
        S = [p for p in ALLPHI if pred(p)]
        member = pred(PHI_R)
        hs = sum(1 for p in S if tuple(sorted(PROF[p])) == SORTED_TARGET)
        hl = sum(1 for p in S if PROF[p] == TARGET)
        forces_sorted = bool(S) and hs == len(S)
        forces_lab = bool(S) and hl == len(S)
        shrink = Fraction(len(ALLPHI), len(S)) if S else None
        results[name] = {
            "statement": rec["statement"], "kind": rec["kind"],
            "both_bases_satisfy": member, "subset_size": len(S),
            "members_reproducing_the_profile_as_a_multiset": hs,
            "members_reproducing_the_profile_element_by_element": hl,
            "forces_the_multiset_profile": forces_sorted,
            "forces_the_element_wise_profile": forces_lab,
            "shrink_factor": str(shrink) if shrink is not None else None,
            "profile_hits_outside_the_subset": len(hits_sorted) - hs,
            "non_members": len(ALLPHI) - len(S),
        }
        say("   | %-28s | %-5s | %5d | %-5s | %-5s | %4d | %s |"
            % (name, member, len(S), forces_sorted, forces_lab, hs,
               ("%s" % shrink) if shrink is not None else "-"))

    forcing = [n for n, r in results.items()
               if r["both_bases_satisfy"] and r["forces_the_multiset_profile"]]
    partial = [n for n, r in results.items()
               if r["both_bases_satisfy"] and not r["forces_the_multiset_profile"]
               and r["subset_size"] < len(ALLPHI)]
    gate("XBA-CANDIDATES-MEASURED", len(results) == len(CAND), "disclosure",
         {"forcing": forcing, "shrinking_but_not_forcing": partial})

    # the clause chain: how the species clauses cut the space
    chain = declared_clause_chain(BKEYS)
    say("")
    say("   the declared clause chain (each clause a species or admission fact):")
    say("")
    say("   | clause added | survivors | profile hits among them |")
    say("   |---|---|---|")
    chain_rows = []
    live = list(ALLPHI)
    for cname, cpred in chain:
        live = [p for p in live if cpred(beta_of(p))]
        hs = sum(1 for p in live if tuple(sorted(PROF[p])) == SORTED_TARGET)
        chain_rows.append({"clause": cname, "survivors": len(live), "hits": hs})
        say("   | %-46s | %5d | %4d |" % (cname, len(live), hs))
    gate("XBA-CLAUSE-CHAIN", chain_rows[-1]["survivors"] == chain_rows[-1]["hits"],
         "must-pass", {"chain": chain_rows})
    c4 = "C4 species-split (named)"
    c5 = "C5 species-split (naming-closed)"
    c4set = [p for p in ALLPHI if CAND[c4]["pred"](p)]
    cons = (c4set == [PHI_R]
            and results[c5]["subset_size"] == chain_rows[-1]["survivors"]
            and results[c4]["subset_size"] * len(V4AUT) == results[c5]["subset_size"])
    if M_ON["chain-lax"]:
        cons = False
    gate("XBA-CANDIDATE-CHAIN-CONSISTENCY", cons, "must-pass",
         {"the_named_candidate_s_subset_is_exactly_the_realized_connection":
              c4set == [PHI_R],
          "the_naming_closed_subset_equals_the_clause_chain_s_survivors":
              results[c5]["subset_size"] == chain_rows[-1]["survivors"],
          "and_is_the_naming_orbit_of_the_named_one":
              results[c4]["subset_size"] * len(V4AUT) == results[c5]["subset_size"]})

    # ---- 6.7 the species derivation and a third instance ------------------
    progress("deriving the connection from the species clauses; third instance")
    say("")
    say("## 7  The derivation, and a third instance built to test it")
    say("")
    derived = derive_from_species(BKEYS)
    say("   derived from the species clauses : %s"
        % "  ".join("%s=%s" % (k, V4NAME[v]) for k, v in zip(BKEYS, derived)))
    say("   measured on the realized bases   : %s"
        % "  ".join("%s=%s" % (k, V4NAME[v]) for k, v in zip(BKEYS, beta_of(PHI_R))))
    gate("XBA-DERIVATION-MATCHES-THE-BASES", derived == beta_of(PHI_R),
         "must-pass", {"derived": [V4NAME[v] for v in derived],
                       "measured": [V4NAME[v] for v in beta_of(PHI_R)]})

    PSI_S = [Fraction(0)] * 9
    PSI_S[0] = Fraction(1, 3)
    PSI_S[1] = Fraction(2, 3)
    PSI_S[3] = Fraction(2, 3)
    bS = build_qutrit_base("base S", [(5, 1, 2, 3)], (0, 0), PSI_S, (1, 5),
                           "the third instance: fresh quaternion, different "
                           "preparation, different completion")
    bS2 = build_qutrit_base("base S'", [(5, 1, 2, 3)], (0, 0), PSI_S,
                            (1, 5) if M_ON["control-completion"] else None,
                            "the exchange-equivariant control: the bare Householder")
    third = {}
    for tag, b in (("base S", bS), ("base S'", bS2)):
        # measured by the gauge-free route: the raw matrix product along each
        # of the 364 based closed walks, with no Klein structure assumed.
        cnt = collections.Counter()
        for s in walks:
            A = b.I
            for (li, rev) in s:
                A = sp_mul(b.K, b.link_matrix(links, li, rev), A)
            cnt[perm_part(b.K, A, b.n)] += 1
        counts = sorted(cnt.values())
        distinct = len(cnt)
        degenerate = len({tuple(v) if v is not None else None
                          for v in b.group().values()}) < 4
        lab = b.gauge_fixed_labels(links)
        ok_in = (not degenerate) and all(v is not None for v in lab.values())
        bt = None
        if ok_in:
            ph = tuple(NAME2V4[lab[NAMES[i]]] for i in cot)
            bt = [V4NAME[v] for v in beta_of(ph)]
        third[tag] = {
            "note": b.note, "W_fixed": b.fixed("W"), "D_fixed": b.fixed("D"),
            "D_is_the_identity": b.D == b.I,
            "the_four_named_elements_are_distinct": not degenerate,
            "declared_basis": bt,
            "distinct_holonomies_over_the_364_walks": distinct,
            "class_counts_sorted": counts,
        }
        say("   %-8s D fixes %s of 81; distinct holonomies %d; class counts %s; "
            "declared basis %s"
            % (tag, b.fixed("D"), distinct, counts, bt))
    gate("XBA-THIRD-INSTANCE-PREDICTED",
         third["base S"]["class_counts_sorted"] == sorted(TARGET)
         and third["base S"]["declared_basis"] == [V4NAME[v] for v in derived],
         "must-pass", third["base S"])
    gate("XBA-EQUIVARIANT-CONTROL-BREAKS-IT",
         third["base S'"]["D_is_the_identity"]
         and third["base S'"]["class_counts_sorted"] != sorted(TARGET)
         and third["base S'"]["distinct_holonomies_over_the_364_walks"] == 2,
         "must-pass", third["base S'"])

    # ---- 6.8 controls -----------------------------------------------------
    progress("controls")
    say("")
    say("## 8  Controls")
    say("")
    pos_ok = (all(PROF[phis[tag]] == TARGET for tag in phis)
              and len(phis) == len(realized) == 4)
    if MUTANT == "control-lax":
        pos_ok = False
    say("   positive: all four readings of the two bases reproduce the profile : %s"
        % pos_ok)
    gate("XBA-POSITIVE-CONTROL", pos_ok, "must-pass",
         {tag: list(PROF[p]) for tag, p in phis.items()})

    say("")
    say("   negative controls with teeth (one declared constructed violator each):")
    say("")
    say("   | candidate | violator | violates? | its profile | breaks the profile? |"
        " violators reproducing it anyway |")
    say("   |---|---|---|---|---|---|")
    negatives = {}
    for name, rec in CAND.items():
        v = build_violator(rec, PHI_R, ALLPHI, beta_of, phi_of_beta, BKEYS)
        if v is None:
            negatives[name] = {"violator": None,
                               "note": "no violator exists: the subset is the whole space"}
            say("   | %-28s | - | - | - | - | - |" % name)
            continue
        viol_ok = not rec["pred"](v["phi"])
        pr = PROF[v["phi"]]
        breaks = tuple(sorted(pr)) != SORTED_TARGET
        outside_hits = sum(1 for p in ALLPHI
                           if not rec["pred"](p)
                           and tuple(sorted(PROF[p])) == SORTED_TARGET)
        negatives[name] = {"violator": v["description"], "violates": viol_ok,
                           "profile": list(pr), "breaks_the_profile": breaks,
                           "violators_reproducing_the_profile_anyway": outside_hits,
                           "non_members": len(ALLPHI) - results[name]["subset_size"]}
        say("   | %-28s | %-22s | %-5s | %-22s | %-5s | %d |"
            % (name, v["description"], viol_ok, list(pr), breaks, outside_hits))
    neg_ok = all(r.get("violates", True) and r.get("breaks_the_profile", True)
                 for r in negatives.values())
    gate("XBA-NEGATIVE-CONTROLS", neg_ok, "must-pass",
         {"declared_violators": {k: v.get("violator") for k, v in negatives.items()},
          "every_declared_violator_breaks_the_profile": neg_ok})

    # ---- 6.9 symmetry self-tests -----------------------------------------
    progress("symmetry self-tests: the gauge sweep and the spanning-tree flip")
    say("")
    say("## 9  Symmetry self-tests")
    say("")
    selftest = gauge_selftest(links, walks, PHI_R, cot, coord, TARGET)
    say("   gauge sweep : %s elements, %s deviations, %s fresh evaluations, "
        "cache hits %s (of %s refused lookups into a populated cache)"
        % (format(selftest["group_elements"], ","), selftest["deviations"],
           format(selftest["fresh_evaluations"], ","), selftest["cache_hits"],
           format(selftest["refused_lookups"], ",")))
    say("   mis-conventioned control (head-only action) moves the profile at %s of %s"
        % (format(selftest["misconvention_moves"], ","),
           format(selftest["group_elements"], ",")))
    gate("XBA-GAUGE-INVARIANCE", selftest["deviations"] == 0, "disclosure",
         {"note": "with the correct convention the invariance is analytically "
                  "forced: a closed walk enters and leaves every node the same "
                  "number of times, so a node-valued gauge telescopes away; the "
                  "measurement is that the instrument implements that convention",
          **selftest})
    gate("XBA-GAUGE-SELFTEST-HAS-TEETH",
         selftest["deviations"] == 0 and selftest["misconvention_moves"] > 0
         and selftest["cache_hits"] == 0
         and selftest["cache_misses"] > 0 and selftest["refused_lookups"] > 0
         and selftest["primed"] > 0 and selftest["reserved_returns"] == selftest["primed"],
         "must-pass", selftest)

    flip = tree_flip_test(links, walks, nnodes, PHI_R, CAND, ALLPHI, SORTED_TARGET,
                          BASIS, BKEYS,
                          (len(prof_hist), len(hits_sorted), len(order4)))
    say("   spanning-tree flip-test : second tree %s; census identical %s; "
        "candidate subset sizes identical %s"
        % (flip["second_tree"], flip["census_identical"], flip["subsets_identical"]))
    if MUTANT == "flip-lax":
        flip["census_identical"] = False
    gate("XBA-TREE-FLIP-TEST",
         flip["census_identical"] and flip["subsets_identical"], "must-pass", flip)

    rev_bad = 0
    for s in walks:
        f = hol_of_class(PHI_R, walk_class(s, coord))
        r = hol_of_class(PHI_R, walk_class(tuple((li, not rv) for (li, rv) in
                                                 reversed(s)), coord))
        if f != r:
            rev_bad += 1
    gate("XBA-DIRECTION-FLIP", rev_bad == 0, "disclosure",
         {"note": "analytically forced: every element of the group is an involution",
          "walks": len(walks), "walks_whose_reversal_differs": rev_bad})

    # ---- 6.10 exactness, hygiene, verdict ---------------------------------
    src = Path(__file__).read_text()
    tree_ast = ast.parse(src)
    floats = [n for n in ast.walk(tree_ast)
              if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    floatcalls = [n for n in ast.walk(tree_ast)
                  if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                  and n.func.id == "float"]
    mutant_ne = count_mutant_exemptions(tree_ast)
    callsites, tainted = gate_callsites(tree_ast)
    if MUTANT == "float-lax":
        floats = floats + [None]
    if MUTANT == "exempt-lax":
        mutant_ne += 1
    gate("XBA-EXACTNESS", len(floats) == 0 and len(floatcalls) == 0, "must-pass",
         {"float_literals": len(floats), "float_calls": len(floatcalls)})
    gate("XBA-NO-MUTANT-EXEMPTION", mutant_ne == 0 and tainted == 0, "must-pass",
         {"mutant_inequality_comparisons": mutant_ne,
          "gate_or_anchor_call_sites": callsites,
          "call_sites_whose_arguments_reach_the_mutant_flag": tainted})

    order_ok = all(g["index"] > DECLARATION_GATE_INDEX
                   for g in GATES if g["name"] in
                   ("XBA-CANDIDATES-MEASURED", "XBA-CLAUSE-CHAIN",
                    "XBA-CANDIDATE-CHAIN-CONSISTENCY", "XBA-NEGATIVE-CONTROLS"))
    if M_ON["order-lax"]:
        order_ok = False
    gate("XBA-FREEZE-ORDER", order_ok, "must-pass",
         {"declaration_gate_index": DECLARATION_GATE_INDEX,
          "every_constrained_subset_gate_comes_later": order_ok})

    say("")
    say("## 10  The verdict")
    say("")
    named = [n for n in forcing if results[n]["subset_size"] < len(ALLPHI)]
    if named:
        verdict = "XBA-SHARED-STRUCTURE-IDENTIFIED"
    elif partial:
        verdict = "XBA-PARTIAL"
    else:
        verdict = "XBA-COINCIDENCE-NOT-EXCLUDED"
    if MUTANT == "verdict-lax":
        verdict = "XBA-EVERYTHING-IS-FINE"
    PREREGISTERED = ("XBA-SHARED-STRUCTURE-IDENTIFIED", "XBA-PARTIAL",
                     "XBA-COINCIDENCE-NOT-EXCLUDED")
    gate("XBA-VOCABULARY", verdict in PREREGISTERED
         or verdict.startswith("XBA-BLOCKED-AT-"), "must-pass",
         {"verdict": verdict, "pre_registered": list(PREREGISTERED)})
    say("   forcing candidates satisfied by both bases : %s" % (named or "none"))
    say("   shrinking but not forcing                  : %s" % (partial or "none"))
    say("")
    say("   >>> %s" % verdict)
    say("")

    # ---- 6.11 mutant census ----------------------------------------------
    census = None
    if MUTANT is None and not args.no_census:
        progress("running the mutant census (%d mutants)" % len(MUTANTS))
        census = run_mutant_census()
        say("## 11  The falsification census")
        say("")
        say("   mutants declared %d; died %d; survived %d"
            % (census["mutants"], census["died"], census["survived"]))
        say("   must-pass gates %d; falsified by some mutant %d; "
            "by a computation mutant %d"
            % (census["must_pass"], census["falsified_by_some"],
               census["falsified_by_computation"]))
        say("   never falsified : %s" % (census["never_falsified"] or "EMPTY"))
        say("")
        gate("XBA-FALSIFICATION-CENSUS",
             census["survived"] == 0 and not census["never_falsified"],
             "must-pass", census)

    failures = [g["name"] for g in GATES if g["kind"] == "must-pass" and not g["ok"]]
    say("=" * 78)
    say("gates %d (must-pass %d, disclosures %d); anchors %d; must-pass failures %d"
        % (len(GATES), sum(1 for g in GATES if g["kind"] == "must-pass"),
           sum(1 for g in GATES if g["kind"] == "disclosure"), len(ANCHORS),
           len(failures)))
    if failures:
        say("FAILED: %s" % ", ".join(failures))
    say("=" * 78)

    receipt = {
        "schema": "xba-crossbase-receipt-v1",
        "pin_sha256_prefix": PIN_SHA[:12],
        "source_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "pinned_sources": hashes,
        "findings": {
            "thesis": "The two bases' holonomy class-count profiles agree because "
                      "their two connections are ONE point of the 4,096-element "
                      "connection space on the common gauge-fixed graph, and that "
                      "point is forced -- cycle by cycle -- by four species clauses "
                      "both bases satisfy: a preparation leg common to the two "
                      "frames, commuting local legs, a wing exchange that "
                      "intertwines the local legs at a symmetric setting, and a "
                      "wing exchange that does NOT intertwine the preparation leg. "
                      "The agreement is not a 2.5% coincidence; the two bases are "
                      "not two independent draws.",
            "unit_verdict": verdict,
            "the_property": "SPECIES-FORCED-SPLIT",
            "forcing_candidates": named,
            "shrinking_but_not_forcing": partial,
            "the_shared_connection": {NAMES[cot[i]]: V4NAME[PHI_R[i]]
                                      for i in range(6)},
            "the_declared_basis_values": {k: V4NAME[v]
                                          for k, v in zip(BKEYS, beta_of(PHI_R))},
            "residual_open": "why the two bases' 24-cell admission tables agree, "
                             "hence why the graph is common, is not decided here",
        },
        "tables": {
            "arena": {
                "nodes": nnodes, "links": len(links),
                "identification_links": sum(1 for l in links if l[2] != "LEG"),
                "cycle_rank": cyc_rank, "path_length_bound": lmax,
                "reduced_walks_all_base_points": total_walks,
                "closed_walks_all_base_points": closed_walks,
                "closed_walks_at_the_base_point": len(walks),
                "distinct_cycle_classes": len(class_hist),
                "spanning_tree": [NAMES[i] for i in tree],
                "cotree": [NAMES[i] for i in cot],
                "declared_cycle_basis": {k: [NAMES[i] for i in v]
                                         for k, v in BASIS.items()},
                "automorphisms_rule_preserving": aut_typed,
                "automorphisms_full_multigraph": aut_full,
                "induced_actions_on_the_cycle_space_rule_preserving": len(act_typed),
                "induced_actions_on_the_cycle_space_full": len(act_full),
            },
            "admission": {"cells": len(cells), "agreeing": len(same)},
            "bases": {tag: {**species_facts[tag],
                            "labels": realized[tag],
                            "class_counts": (list(PROF[phis[tag]])
                                             if tag in phis else None)}
                      for tag in bases},
            "direct_comparator": direct,
            "census": {
                "connection_space": len(ALLPHI),
                "distinct_profiles": len(prof_hist),
                "profile_hits_as_a_multiset": len(hits_sorted),
                "profile_hits_element_by_element": len(hits_labelled),
                "order_4_connections": len(order4),
                "order_4_profile_hits": len(hits_in_order4),
                "most_common_profile": [list(mc_profile), mc_count],
                "the_realized_profile": list(TARGET),
            },
            "candidates": results,
            "clause_chain": chain_rows,
            "third_instances": third,
            "negative_controls": negatives,
            "gauge_selftest": selftest,
            "tree_flip_test": flip,
            "mutants": [{"name": k, "kind": v[0], "perturbs": v[1]}
                        for k, v in MUTANTS.items()],
            "gate_falsification": census,
        },
        "anchors": ANCHORS,
        "gates": GATES,
        "totals": {"anchors": len(ANCHORS), "gates": len(GATES),
                   "must_pass_gates": sum(1 for g in GATES if g["kind"] == "must-pass"),
                   "disclosures": sum(1 for g in GATES if g["kind"] == "disclosure"),
                   "must_pass_failures": len(failures)},
    }

    text = "\n".join(OUT) + "\n"
    if args.delivery and MUTANT is None and not failures:
        (HERE / "xba_crossbase_output.txt").write_text(text)
        (HERE / "xba_crossbase_receipt.json").write_text(
            json.dumps(receipt, indent=1, sort_keys=True) + "\n")
    elif args.delivery:
        text += ("\n[delivery refused: a must-pass gate failed; the artifacts "
                 "on disk are left as they were]\n")
    sys.stdout.write(text)
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# 7.  helpers used above
# ---------------------------------------------------------------------------

def invert_f2(M):
    n = len(M)
    A = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(M)]
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if A[i][c]), None)
        if piv is None:
            return None
        A[r], A[piv] = A[piv], A[r]
        for i in range(n):
            if i != r and A[i][c]:
                A[i] = [(x ^ y) for x, y in zip(A[i], A[r])]
        r += 1
    return [row[n:] for row in A]


def f2_solve(Minv, rhs):
    n = len(Minv)
    return [sum(Minv[i][j] * rhs[j] for j in range(n)) % 2 for i in range(n)]


def automorphisms(links, cot, coord, tree):
    """|Aut| of the multigraph and of its rule-preserving subgroup, with the
    induced actions on H_1(G;F2)."""
    ends = [frozenset((a, b)) for (a, b, _k, _n) in links]
    kinds = [k for (_a, _b, k, _n) in links]
    nodes = sorted({a for (a, b, _k, _n) in links} | {b for (a, b, _k, _n) in links})
    base = collections.Counter(ends)
    node_perms = []
    for p in itertools.permutations(nodes):
        pm = dict(zip(nodes, p))
        if collections.Counter(frozenset((pm[a], pm[b]))
                               for (a, b, _k, _n) in links) == base:
            node_perms.append(pm)
    par = collections.Counter(ends)
    factor = 1
    for _e, c in par.items():
        factor *= math.factorial(c)
    typed_perms = []
    for pm in node_perms:
        ok = True
        for k in set(kinds):
            want = collections.Counter(e for e, kk in zip(ends, kinds) if kk == k)
            got = collections.Counter(frozenset((pm[a], pm[b]))
                                      for (a, b, kk, _n) in links if kk == k)
            if want != got:
                ok = False
                break
        if ok:
            typed_perms.append(pm)
    tset = set(tree)
    treeadj = {}
    for i in tree:
        a, b, _k, _n = links[i]
        treeadj.setdefault(a, []).append((i, b))
        treeadj.setdefault(b, []).append((i, a))

    def tree_path(u, v):
        prev = {u: (None, None)}
        dq = collections.deque([u])
        while dq:
            x = dq.popleft()
            for (li, w) in treeadj.get(x, ()):
                if w not in prev:
                    prev[w] = (li, x)
                    dq.append(w)
        out = []
        x = v
        while x != u:
            li, px = prev[x]
            out.append(li)
            x = px
        return out

    fund = {li: set(tree_path(links[li][0], links[li][1])) ^ {li} for li in cot}

    def link_maps(perms, typed):
        res = set()
        for pm in perms:
            groups, targets = {}, {}
            for i, (a, b, _k, _n) in enumerate(links):
                groups.setdefault(frozenset((pm[a], pm[b])), []).append(i)
                targets.setdefault(frozenset((a, b)), []).append(i)
            opts = []
            for key, srcs in groups.items():
                tg = targets[key]
                if typed:
                    perms_ok = [q for q in itertools.permutations(tg)
                                if all(kinds[s] == kinds[t] for s, t in zip(srcs, q))]
                else:
                    perms_ok = list(itertools.permutations(tg))
                opts.append((srcs, perms_ok))
            for combo in itertools.product(*[o[1] for o in opts]):
                m = [None] * len(links)
                for (srcs, _), tg in zip(opts, combo):
                    for s, t in zip(srcs, tg):
                        m[s] = t
                res.add(tuple(m))
        return res

    lp_full = link_maps(node_perms, False)
    lp_typed = link_maps(typed_perms, True)

    def action(m):
        out = []
        for li in cot:
            c = 0
            for e in fund[li]:
                c ^= coord[m[e]]
            out.append(c)
        return tuple(out)

    return (len(lp_typed), len(lp_full),
            sorted({action(m) for m in lp_typed}), sorted({action(m) for m in lp_full}))


def apply_action(act, phi):
    """the pullback of phi along an automorphism of the cycle space."""
    out = []
    for c in act:
        h = 0
        for i in range(len(phi)):
            if c >> i & 1:
                h ^= phi[i]
        out.append(h)
    return tuple(out)


def declare_candidates(BKEYS, BCLS, FULLCLS, REALCLS, BIGCLS, act_full, act_typed):
    """the candidate family, DECLARED: predicate + statement, no profile read."""
    ix = {k: i for i, k in enumerate(BKEYS)}

    def beta(phi):
        return tuple(hol_of_class(phi, BCLS[k]) for k in BKEYS)

    def full_flat(phi):
        return all(hol_of_class(phi, c) == 0 for c in FULLCLS)

    def real_group(phi):
        return generated_group([hol_of_class(phi, c) for c in REALCLS])

    def bigons(phi):
        return [hol_of_class(phi, BIGCLS[t]) for t in sorted(BIGCLS)]

    C = collections.OrderedDict()

    C["C1 source-split"] = {
        "kind": "pin",
        "statement": "the full-leg sub-connection is flat, the realized-rule "
                     "sub-connection carries a group of order two, every "
                     "two-rule coordinate has a non-flat bigon, and the whole "
                     "connection generates the group",
        "pred": lambda p: (full_flat(p) and len(real_group(p)) == 2
                           and all(b != 0 for b in bigons(p))
                           and len(generated_group(p)) == 4),
    }
    C["C2a aut-equivariance (rule-preserving)"] = {
        "kind": "pin",
        "statement": "invariant under the induced action of the rule-preserving "
                     "automorphism group of the graph",
        "pred": lambda p: all(apply_action(a, p) == p for a in act_typed),
    }
    C["C2b aut-equivariance (full)"] = {
        "kind": "pin",
        "statement": "invariant under the induced action of the full multigraph "
                     "automorphism group",
        "pred": lambda p: all(apply_action(a, p) == p for a in act_full),
    }
    C["C2c aut-equivariance up to naming"] = {
        "kind": "pin",
        "statement": "for every graph automorphism there is an automorphism of "
                     "the Klein group carrying the pullback back to the connection",
        "pred": lambda p: all(any(apply_action(a, p) == relabel(p, s)
                                  for s in V4AUT) for a in act_full),
    }
    C["C3 admission-pattern"] = {
        "kind": "pin",
        "statement": "every coordinate at which the two rules draw DIFFERENT "
                     "permutations carries a non-flat bigon -- the only "
                     "constraint the 24-cell table places on a connection",
        "pred": lambda p: all(b != 0 for b in bigons(p)),
    }
    C["C4 species-split (named)"] = {
        "kind": "worker",
        "statement": "the six declared cycles take the values the species "
                     "clauses force, with the group elements named: "
                     "(1, 1, D, 1, 1, W)",
        "pred": lambda p: beta(p) == derive_from_species(BKEYS),
    }
    C["C5 species-split (naming-closed)"] = {
        "kind": "worker",
        "statement": "there are distinct non-identity d, w with the six declared "
                     "cycles at (1, 1, d, 1, 1, w)",
        "pred": lambda p: species_shape(beta(p)),
    }
    C["C6 common preparation leg"] = {
        "kind": "worker",
        "statement": "the full-leg square around the preparation leg is flat "
                     "(the two frames share that leg)",
        "pred": lambda p: beta(p)[ix["SQ_FULL_1"]] == 0,
    }
    C["C7 commuting local legs"] = {
        "kind": "worker",
        "statement": "the canonical loop is flat (the two local legs commute)",
        "pred": lambda p: beta(p)[ix["CANON"]] == 0,
    }
    C["C8 intertwined local legs"] = {
        "kind": "worker",
        "statement": "the two realized-rule squares around the local legs are "
                     "flat (the wing exchange intertwines them)",
        "pred": lambda p: (beta(p)[ix["SQ_REAL_2"]] == 0
                           and beta(p)[ix["SQ_REAL_3"]] == 0),
    }
    C["C9 unintertwined preparation leg"] = {
        "kind": "worker",
        "statement": "the realized-rule square around the preparation leg is "
                     "neither flat nor the wing exchange",
        "pred": lambda p: (beta(p)[ix["SQ_REAL_1"]] != 0
                           and beta(p)[ix["SQ_REAL_1"]] != beta(p)[ix["BIGON_0"]]),
    }
    C["C10 group of order four"] = {
        "kind": "worker",
        "statement": "the connection's labels generate a group of order four -- "
                     "the explanation the generality unit offered",
        "pred": lambda p: len(generated_group(p)) == 4,
    }
    if MUTANT == "candidate-lax":
        C["C5 species-split (naming-closed)"]["pred"] = lambda p: species_shape(beta(p)) or True
    return C


V4AUT = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1),
         (0, 3, 1, 2), (0, 3, 2, 1)]


def relabel(phi, sigma):
    return tuple(sigma[v] for v in phi)


def species_shape(beta):
    a, b, d, c, e, w = beta
    return (a == 0 and b == 0 and c == 0 and e == 0
            and d != 0 and w != 0 and d != w)


def declared_clause_chain(BKEYS):
    ix = {k: i for i, k in enumerate(BKEYS)}
    chain = [
        ("E0  the two rules draw different maps at t=0 (admission table)",
         lambda b: b[ix["BIGON_0"]] != 0),
        ("E1  the preparation leg is common to the two frames",
         lambda b: b[ix["SQ_FULL_1"]] == 0),
        ("E2  the two local legs commute",
         lambda b: b[ix["CANON"]] == 0),
        ("E3  the wing exchange intertwines both local legs",
         lambda b: b[ix["SQ_REAL_2"]] == 0 and b[ix["SQ_REAL_3"]] == 0),
        ("E4  the wing exchange does not intertwine the preparation leg",
         lambda b: b[ix["SQ_REAL_1"]] not in (0, b[ix["BIGON_0"]])),
    ]
    if MUTANT == "species-lax":
        chain = chain[:-1]
    return chain


def derive_from_species(BKEYS):
    """the declared-basis values the four species clauses force, derived
    symbolically from the clauses and not read off any base.

    Writing u for the preparation leg, a and b for the two local legs, P for
    the wing exchange and D = P u^-1 P u:

      SQ_FULL_1 = u^-1 . u                             = 1     (E1)
      CANON     = (a b u)^-1 (b a u)                   = 1     (E1, E2)
      SQ_REAL_1 = (u)^-1 P (u) . P                     = D     (E4)
      SQ_REAL_2 = (b u)^-1 P (a u) . (u^-1 P u)        = 1     (E1, E3)
      SQ_REAL_3 = (a b u)^-1 P (b a u) . (b u)^-1 P(au)= 1     (E2, E3)
      BIGON_0   = 1^-1 . P                             = W     (E0)
    """
    val = {"SQ_FULL_1": 0, "CANON": 0, "SQ_REAL_1": 2, "SQ_REAL_2": 0,
           "SQ_REAL_3": 0, "BIGON_0": 1}
    if MUTANT == "species-lax":
        val["SQ_REAL_2"] = 1
    return tuple(val[k] for k in BKEYS)


def build_violator(rec, PHI_R, ALLPHI, beta_of, phi_of_beta, BKEYS):
    """the declared constructed violator: the lexicographically first
    single-coordinate edit of the realized connection, in the declared basis
    order, that fails the candidate's predicate.  Deterministic, no seed."""
    if M_ON["violator-lax"]:
        return {"phi": PHI_R, "description": "the realized connection itself"}
    base = list(beta_of(PHI_R))
    for i, key in enumerate(BKEYS):
        for v in range(4):
            if v == base[i]:
                continue
            b2 = list(base)
            b2[i] = v
            phi2 = phi_of_beta(tuple(b2))
            if not rec["pred"](phi2):
                return {"phi": phi2,
                        "description": "%s := %s" % (key, V4NAME[v])}
    for p in ALLPHI:
        if not rec["pred"](p):
            return {"phi": p, "description": "the first non-member in the census order"}
    return None


def gauge_selftest(links, walks, PHI_R, cot, coord, TARGET):
    """the declared gauge group swept whole, every holonomy rebuilt FRESH from
    the link variables with the value cache primed, exercised and bypassed."""
    nnodes = 8
    labels0 = [0] * len(links)
    for k, li in enumerate(cot):
        labels0[li] = PHI_R[k]
    masks = collections.Counter()
    for s in walks:
        m = 0
        for (li, _rev) in s:
            m ^= 1 << li
        masks[m] += 1
    mask_bits = [(m, [i for i in range(len(links)) if m >> i & 1], c)
                 for m, c in masks.items()]

    # Prime the value cache with the very keys the sweep will request -- keyed
    # by the walk, which is exactly how a naive memoiser would key a holonomy,
    # and exactly the bug the fresh-evaluation rule exists to catch.
    HOLCACHE.clear()
    CACHE_STATS.update({"hits": 0, "misses": 0, "bypassed_lookups": 0,
                        "primed": 0, "reserved_returns": 0})
    for m, bits, _c in mask_bits:
        x = 0
        for bi in bits:
            x ^= labels0[bi]
        HOLCACHE[("selftest", m)] = x
        CACHE_STATS["primed"] += 1
    CACHE_STATS["reserved_returns"] = sum(
        1 for m in masks if ("selftest", m) in HOLCACHE)

    deviations = 0
    misconv = 0
    elements = 0
    for h in itertools.product(range(4), repeat=nnodes - 1):
        H = (0,) + h
        elements += 1
        lab = [0] * len(links)
        for i, (a, b, _k, _n) in enumerate(links):
            if MUTANT == "gauge-head":
                lab[i] = labels0[i] ^ H[b]
            else:
                lab[i] = labels0[i] ^ H[a] ^ H[b]
        cnt = [0, 0, 0, 0]
        for m, bits, c in mask_bits:
            key = ("selftest", m)
            if MUTANT == "memo-lax" and key in HOLCACHE:
                CACHE_STATS["hits"] += 1
                x = HOLCACHE[key]
            else:
                if key in HOLCACHE:
                    CACHE_STATS["bypassed_lookups"] += 1
                x = 0
                for bi in bits:
                    x ^= lab[bi]
                CACHE_STATS["misses"] += 1
            cnt[x] += c
        if tuple(cnt) != TARGET:
            deviations += 1
        lab2 = [labels0[i] ^ H[links[i][1]] for i in range(len(links))]
        cnt2 = [0, 0, 0, 0]
        for _m, bits, c in mask_bits:
            x = 0
            for bi in bits:
                x ^= lab2[bi]
            cnt2[x] += c
        if tuple(cnt2) != TARGET:
            misconv += 1
    return {"group_elements": elements,
            "declared_group": "one Klein-group value per node, the constant "
                              "subgroup fixed by the declared section h(F1@t0)=1",
            "deviations": deviations,
            "misconvention_moves": misconv,
            "fresh_evaluations": CACHE_STATS["misses"],
            "cache_hits": CACHE_STATS["hits"],
            "cache_misses": CACHE_STATS["misses"],
            "refused_lookups": CACHE_STATS["bypassed_lookups"],
            "primed": CACHE_STATS["primed"],
            "reserved_returns": CACHE_STATS["reserved_returns"],
            "distinct_walk_masks": len(masks)}


def tree_flip_test(links, walks, nnodes, PHI_R, CAND, ALLPHI, SORTED_TARGET,
                   BASIS, BKEYS, expected):
    """the whole census recomputed on a SECOND declared spanning tree: the
    bookkeeping split this unit carries."""
    order = [i for i, (_a, _b, k, n) in enumerate(links) if k != "FULL"] + \
            [i for i, (_a, _b, k, n) in enumerate(links) if k == "FULL"]
    tree2 = spanning_tree(links, nnodes, prefer=order)
    cot2, coord2 = cycle_coords(links, tree2, nnodes)
    hist2 = collections.Counter(walk_class(s, coord2) for s in walks)
    prof2 = make_profiler(hist2)
    BCLS2 = {k: edgeset_class(v, coord2) for k, v in BASIS.items()}
    P2 = {p: prof2(p) for p in ALLPHI}
    hist_p2 = collections.Counter(tuple(sorted(v)) for v in P2.values())
    hits2 = sum(1 for p in ALLPHI if tuple(sorted(P2[p])) == SORTED_TARGET)
    order4_2 = sum(1 for p in ALLPHI if len(generated_group(p)) == 4)
    census_ok = ([len(hist_p2), hits2, order4_2] == list(expected))
    # candidate subsets are cycle-space predicates: they must not move
    sizes1 = {n: sum(1 for p in ALLPHI if r["pred"](p)) for n, r in CAND.items()}
    CAND2 = declare_candidates(BKEYS, BCLS2, sorted({walk_class(s, coord2) for s in
                                                     enumerate_walks(links, 0, 8,
                                                     allowed=[i for i, l in enumerate(links)
                                                              if l[2] != "REAL"])}),
                               sorted({walk_class(s, coord2) for s in
                                       enumerate_walks(links, 0, 8,
                                       allowed=[i for i, l in enumerate(links)
                                                if l[2] != "FULL"])}),
                               {t: edgeset_class([i for i, l in enumerate(links)
                                                  if l[3] in ("FULL@%d" % t, "REAL@%d" % t)],
                                                 coord2) for t in (0, 1, 3)},
                               [], [])
    sizes2 = {n: sum(1 for p in ALLPHI if r["pred"](p)) for n, r in CAND2.items()
              if not n.startswith("C2")}
    subsets_ok = all(sizes1[n] == sizes2[n] for n in sizes2)
    return {"second_tree": [links[i][3] for i in tree2],
            "distinct_profiles": len(hist_p2), "profile_hits": hits2,
            "order_4": order4_2,
            "the_first_tree_s_values": list(expected),
            "census_identical": census_ok,
            "subsets_identical": subsets_ok,
            "candidate_sizes_first_tree": sizes1,
            "candidate_sizes_second_tree": sizes2}


def count_mutant_exemptions(tree_ast):
    n = 0
    for node in ast.walk(tree_ast):
        if isinstance(node, ast.Compare):
            names = {x.id for x in ast.walk(node) if isinstance(x, ast.Name)}
            if "MUTANT" in names:
                for op in node.ops:
                    if isinstance(op, (ast.NotEq, ast.NotIn, ast.IsNot)):
                        n += 1
    return n


def gate_callsites(tree_ast):
    sites, tainted = 0, 0
    for node in ast.walk(tree_ast):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("gate", "anchor"):
            sites += 1
            names = {x.id for x in ast.walk(node) if isinstance(x, ast.Name)}
            if "MUTANT" in names:
                tainted += 1
    return sites, tainted


def run_mutant_census():
    import subprocess
    me = str(Path(__file__).resolve())
    died, survived, per = 0, [], {}
    falsified = collections.defaultdict(list)
    for name in MUTANTS:
        r = subprocess.run([sys.executable, me, "--mutant", name],
                           capture_output=True, text=True)
        killed = (r.returncode != 0)
        why = []
        for ln in r.stdout.splitlines():
            if ln.startswith("ANCHOR FAILURE"):
                why.append(ln.split()[-1])
            if ln.startswith("FAILED:"):
                why.extend(x.strip() for x in ln[len("FAILED:"):].split(","))
        per[name] = {"kind": MUTANTS[name][0], "died": killed, "falsified": why}
        if killed:
            died += 1
            for w in why:
                falsified[w].append(name)
        else:
            survived.append(name)
        progress("mutant %-24s %s" % (name, "died" if killed else "SURVIVED"))
    mp = [g["name"] for g in GATES if g["kind"] == "must-pass"]
    mp = [g for g in mp if g != "XBA-FALSIFICATION-CENSUS"]
    never = [g for g in mp if g not in falsified]
    by_comp = [g for g in mp
               if any(MUTANTS[m][0] == "computation" for m in falsified.get(g, []))]
    return {"mutants": len(MUTANTS), "died": died, "survived": len(survived),
            "survivors": survived, "must_pass": len(mp),
            "falsified_by_some": len([g for g in mp if g in falsified]),
            "falsified_by_computation": len(by_comp),
            "never_falsified": never,
            "falsified_only_by_a_waiver": [g for g in mp
                                           if g in falsified and g not in by_comp],
            "per_gate_falsifiers": {k: v for k, v in falsified.items()},
            "per_mutant": per}


def run_falsification_selftest():
    """deliberately break one anchor; the receipt must exit 1 visibly."""
    import subprocess
    me = str(Path(__file__).resolve())
    r = subprocess.run([sys.executable, me, "--mutant", "anchor-classcounts"],
                       capture_output=True, text=True)
    ok = (r.returncode == 1 and "ANCHOR FAILURE" in r.stdout)
    print("falsification self-test: broke the reused 82/86/90/106 anchor")
    print("   exit code %d, ANCHOR FAILURE printed: %s"
          % (r.returncode, "ANCHOR FAILURE" in r.stdout))
    print("   %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
