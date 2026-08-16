#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""THEORY-CONTRACT (paper-43) -- THE OBJECT CENSUS, THE STATE, THE GAUGE, THE
CIRCULARITY, Q58, AND THE PARAMETERS.

Pin: v15/note-contract-pin.md (sha256-12 438586c11db5, v15 ledger #1).
Questions: Q1-Q10, Q24, Q58 (+Q4-Q5, the actors-records circularity).

WHAT THIS UNIT IS.  A synthesis-with-measurements unit.  It states, once, what
objects the theory has; what the complete instantaneous state is; which
relabellings are redundancy and which are physical; whether the construction is
circular and if so whether the circle closes; whether the reconstruction of
actors from records survives a change of generating mechanism; and how many
declarations remain free after every law the sealed corpus has measured.
No new physics claim is made beyond the census's own measurements.

WHAT IS READ.  The sealed v14 corpus at pinned digests, and nothing else.
Every census row is either RECOMPUTED here from the corpus's own constructors,
re-implemented in this file, or CITED to a sealed unit at its pinned digest --
and the row says which.

S-1 BY CONSTRUCTION (the registered-unimplemented family, v14/TEMPLATE.md
Sec.11).  Four code regions, disjoint by machine check at G-S1-DISJOINT-CODE:
  b_*   THE BUILDER       -- the declared arena, the committed corpus, the
                             declared dynamics; the only region that may name a
                             declared-side constant;
  s_*   THE STRIPPER      -- the eraser that emits bare record bytes;
  r_*   THE RECONSTRUCTOR -- reads bare bytes and nothing else, ever;
  k_*   THE COMPARATOR    -- decides agreement and rebuilds the verdict; calls
                             no builder, no stripper and no reconstructor.
The comparator is shown to HAVE TEETH: it refuses four of eight declared
generating mechanisms, and it rebuilds the head from the serialized receipt
alone.

TEMPLATE.  The nine E-25...E-33 families are imported from
v14/code/era_template.py and USED, not copied: every family's check id is read
off the template's own table and matched to a live call in this module, and
that match is gated at G-TEMPLATE-EXERCISED.

EXACTNESS.  Python integers and fractions.Fraction only.  No float appears
anywhere; an AST scan of this module and a recursive type walk of the receipt
are gates.

CLI (#82).  --run | --no-write | --selftest | --list-gates | --list-mutants
            | --mutant NAME | --render
--render is the paper-free diagnostic: it fires every gate whose object is the
payload, skips exactly the four whose object is the paper, and writes nothing.
Anything else exits 2.
"""

from __future__ import annotations

import ast
import collections
import hashlib
import json
import os
import re
import sys
from fractions import Fraction
from itertools import combinations, permutations

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
_V14 = os.path.join(os.path.dirname(os.path.dirname(_HERE)), "v14", "code")
if _V14 not in sys.path:
    sys.path.insert(0, _V14)
import era_template as ET                                          # noqa: E402

REPO = os.path.dirname(os.path.dirname(_HERE))     # .../isp

PAPER_REL = "v15/paper-43-contract.md"
RECEIPT_REL = "v15/code/contract_receipt.json"
OUTPUT_REL = "v15/code/contract_output.txt"
SELF_REL = "v15/code/contract_exact.py"
TEMPLATE_REL = "v14/code/era_template.py"
PIN_REL = "v15/note-contract-pin.md"

# The sha256-12 of every pinned source, verified before use (#91: repository
# reads at pinned digests only, every product consumed by a gate).
SOURCES = {
    PIN_REL: "438586c11db5",
    "v15/PLAN.md": "6ba8621d4ec7",
    TEMPLATE_REL: "d04a3eb58fbc",
    "v14/TEMPLATE.md": "809ebe3514ad",
    "v14/paper-41-rec.md": "c5fbc9acbd76",
    "v14/paper-33-aid.md": "ecdd3fbf1d06",
    "v14/paper-35-fac.md": "281289a615ad",
    "v14/paper-31-occ.md": "0092caa4d9ad",
    "v14/paper-20-coupling.md": "4824d190af73",
    "v14/paper-21-r4dec.md": "ef4a8c35a0c4",
    "v14/paper-39-ndep.md": "e2293b8c3858",
    "v14/paper-40-sec2.md": "4fe88602280c",
    "v14/paper-32-sec.md": "f3f43d94cd75",
    "v14/paper-19-r3-weld.md": "50bb81e67942",
    "v14/paper-42-hor.md": "164aa0d755bc",
    "v14/paper-38-epr.md": "22beb6696223",
}

# ===========================================================================
# SECTION A.  b_*  --  THE BUILDER.
#   AG(2, 3); the four parallel classes and the three declared directions; the
#   27 cells; the groupings; paper-21's I7-STRICT triples, G-FLAT quadruples
#   and driven window; the three committed corpora; the coupled walk's coin,
#   shift and count-residue coupling.  Re-implemented here, never imported.
# ===========================================================================

B_Q = 3                       # the declared field order
B_DIMENSION = 2               # the declared spatial dimension
B_ARITY = 3                   # the declared division-event arity
B_ROUNDS = 3                  # the declared depth of the primary corpus
SITES = tuple((i, j) for i in range(B_Q) for j in range(B_Q))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
NACT = len(SITES)
DECLARED_LINKS = ((1, 0), (0, 1), (1, 1))
CLASS_NAMES = ("ROW", "COL", "DIA", "ANT")
CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": (1, 2)}
UNDECLARED_CLASS = "ANT"


def b_vadd(a, b):
    return ((a[0] + b[0]) % B_Q, (a[1] + b[1]) % B_Q)


def b_vmul(k, a):
    return ((k * a[0]) % B_Q, (k * a[1]) % B_Q)


def b_parallel_class(d):
    """the resolvable partition of AG(2, q) into the lines of slope d."""
    H = frozenset({(0, 0), d, b_vmul(2, d)})
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(b_vadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


CLASSES = {k: b_parallel_class(CLASS_DIR[k]) for k in CLASS_NAMES}
CELLS = tuple((x, l) for x in SITES for l in DECLARED_LINKS)
CELL_INDEX = {c: k for k, c in enumerate(CELLS)}
DIM = len(CELLS)


def b_codivision_pair(cell):
    """OCC's carrier typing: the cell IS the unordered co-division pair."""
    x, l = cell
    return frozenset((x, b_vadd(x, l)))


def b_all_groupings():
    """every partition of the sites into groups of the declared arity."""
    out = []

    def rec(rem, acc):
        if not rem:
            out.append(tuple(sorted(acc)))
            return
        a, rest = rem[0], rem[1:]
        for pair in combinations(rest, B_ARITY - 1):
            rec(tuple(x for x in rest if x not in pair),
                acc + [tuple(sorted((a,) + pair))])
    rec(tuple(SITES), [])
    return sorted(out)


def b_round_vec(P):
    return tuple(1 if any(x in g and b_vadd(x, l) in g for g in P) else 0
                 for (x, l) in CELLS)


_RAW: dict = {}


def b_raw_census():
    if _RAW:
        return _RAW
    parts = b_all_groupings()
    vecs = [b_round_vec(P) for P in parts]
    _RAW["parts"] = parts
    _RAW["vecs"] = vecs
    _RAW["sat"] = [i for i, v in enumerate(vecs) if sum(v) == NACT]
    return _RAW


def b_strict_triples():
    """paper-21's I7-STRICT class at the declared depth."""
    C = b_raw_census()
    V = [C["vecs"][i] for i in C["sat"]]
    out = []
    for ia, a in enumerate(V):
        for ib, b in enumerate(V):
            ab = [a[k] + b[k] for k in range(DIM)]
            for ic, c in enumerate(V):
                if all(ab[k] + c[k] >= 1 for k in range(DIM)):
                    out.append((C["sat"][ia], C["sat"][ib], C["sat"][ic]))
    return out


def b_flat_quadruples():
    """paper-21's saturating quadruples: the summed link field is G-FLAT."""
    C = b_raw_census()
    V = [C["vecs"][i] for i in C["sat"]]
    tgt = [1, 1, 2] * NACT
    out = []
    for ia, a in enumerate(V):
        for ib, b in enumerate(V):
            ab = [a[k] + b[k] for k in range(DIM)]
            if any(ab[k] > tgt[k] for k in range(DIM)):
                continue
            for ic, c in enumerate(V):
                abc = [ab[k] + c[k] for k in range(DIM)]
                if any(abc[k] > tgt[k] for k in range(DIM)):
                    continue
                for idd, d in enumerate(V):
                    if all(abc[k] + d[k] == tgt[k] for k in range(DIM)):
                        out.append((C["sat"][ia], C["sat"][ib],
                                    C["sat"][ic], C["sat"][idd]))
    return out


def b_canon_transversals(P):
    return [tuple(sorted(g)[k] for g in P) for k in range(B_ARITY)]


def b_history_of(rounds, seeds):
    """THE COMBINATORIAL HISTORY: division events as actor-subsets, in the
    driver's own order."""
    H = []
    for P, sd in zip(rounds, seeds):
        order = sorted(range(len(P)), key=lambda gi: SITE_INDEX[sd[gi]])
        for gi in order:
            H.append(frozenset(P[gi]))
    return tuple(H)


B_COLLINEAR_FLAT = ("ROW", "COL", "DIA", "DIA")
B_COMMITTED_R4 = ("ROW", "COL", "ROW", "COL")
B_SEEDS_PER_ROUND = 1


def b_window_schedules(flatq, parts):
    """paper-21's DRIVEN WINDOW, by its own constructor."""
    quads, tags = [], []
    for a in CLASS_NAMES:
        for b in CLASS_NAMES:
            for c in CLASS_NAMES:
                for d in CLASS_NAMES:
                    quads.append(tuple(CLASSES[k] for k in (a, b, c, d)))
                    tags.append("W4-CLASS")
    for q in flatq:
        quads.append(tuple(parts[i] for i in q))
        tags.append("W4-FLAT")
    quads.append(tuple(CLASSES[k] for k in B_COMMITTED_R4))
    tags.append("W4-CTRL")
    out, seen, meta = [], set(), []
    for T, tag in zip(quads, tags):
        menus = [b_canon_transversals(P)[:B_SEEDS_PER_ROUND] for P in T]
        for combo in _product(menus):
            sch = tuple(zip(T, combo))
            if sch in seen:
                continue
            seen.add(sch)
            out.append(sch)
            meta.append(tag)
    T = tuple(CLASSES[k] for k in B_COLLINEAR_FLAT)
    menus = [b_canon_transversals(P) for P in T]
    for combo in _product(menus):
        sch = tuple(zip(T, combo))
        if sch in seen:
            continue
        seen.add(sch)
        out.append(sch)
        meta.append("W4-SEEDFAN")
    return out, meta


def _product(lists):
    out = [()]
    for L in lists:
        out = [t + (x,) for t in out for x in L]
    return out


def b_build_corpus():
    C = b_raw_census()
    parts = C["parts"]
    strict = b_strict_triples()
    flatq = b_flat_quadruples()
    scheds, smeta = b_window_schedules(flatq, parts)
    corp = []
    for t in strict:
        Ps = [parts[i] for i in t]
        corp.append(("C1", b_history_of(
            Ps, [b_canon_transversals(P)[0] for P in Ps])))
    c1 = [h for (_t, h) in corp]
    for a in c1:
        for b in c1:
            corp.append(("C2", a + b))
    for sch in scheds:
        corp.append(("C3", b_history_of([p for p, _s in sch],
                                        [s for _p, s in sch])))
    return corp, parts, strict, flatq, scheds, smeta


def b_cell_footprint(F):
    """THE RECORD'S OWN BYTES for one division event: the cells whose two
    actors both take part in it.  An event both of whose ends lie in the
    undeclared parallel class writes nothing."""
    return frozenset(k for k, (x, l) in enumerate(CELLS)
                     if x in F and b_vadd(x, l) in F)


def b_record_field(H):
    """n_l(x): the count of division events containing both x and x + l."""
    r = [[0] * NACT for _ in range(NACT)]
    for F in H:
        idx = sorted(SITE_INDEX[x] for x in F)
        for a in idx:
            for b in idx:
                if a != b:
                    r[a][b] += 1
    return tuple(r[SITE_INDEX[x]][SITE_INDEX[b_vadd(x, l)]] for (x, l) in CELLS)


def b_declared_actors():
    """the declared cast, as the star of cells at each site."""
    st = collections.defaultdict(set)
    for k, (x, l) in enumerate(CELLS):
        st[x].add(k)
        st[b_vadd(x, l)].add(k)
    return {SITE_INDEX[x]: frozenset(v) for x, v in st.items()}


def b_declared_pairs():
    return {k: frozenset((SITE_INDEX[x], SITE_INDEX[b_vadd(x, l)]))
            for k, (x, l) in enumerate(CELLS)}


def b_translation_subgroups():
    """every subgroup of the translation group of the arena."""
    subs = {frozenset({(0, 0)})}
    for mask in range(1, 1 << NACT):
        E = [SITES[i] for i in range(NACT) if mask >> i & 1]
        if (0, 0) not in E:
            continue
        if all(b_vadd(u, v) in E for u in E for v in E):
            subs.add(frozenset(E))
    return subs


def b_declared_menu():
    """FAC's admissible actor-grain partitions: the coset partitions of the
    translation subgroups.  Built here from the subgroups, never typed."""
    out = set()
    for S in b_translation_subgroups():
        out.add(frozenset({frozenset(SITE_INDEX[b_vadd(x, h)] for h in S)
                           for x in SITES}))
    return out


def b_arena_automorphisms():
    """the affine maps of the arena permuting the DECLARED directions."""
    out = []
    for a in range(B_Q):
        for b in range(B_Q):
            for c in range(B_Q):
                for d in range(B_Q):
                    if (a * d - b * c) % B_Q == 0:
                        continue
                    M = ((a, b), (c, d))
                    img = [((M[0][0] * v[0] + M[0][1] * v[1]) % B_Q,
                            (M[1][0] * v[0] + M[1][1] * v[1]) % B_Q)
                           for v in DECLARED_LINKS]
                    pool = set(DECLARED_LINKS) | {b_vmul(2, l)
                                                  for l in DECLARED_LINKS}
                    if not all(v in pool for v in img):
                        continue
                    for t in SITES:
                        out.append(tuple(SITE_INDEX[b_vadd(
                            ((M[0][0] * x[0] + M[0][1] * x[1]) % B_Q,
                             (M[1][0] * x[0] + M[1][1] * x[1]) % B_Q), t)]
                            for x in SITES))
    return sorted(set(out))


# --- the declared dynamics: paper-20's coupled walk, re-implemented --------

B_Z0, B_Z1 = (0, 0), (1, 0)
B_WPOW = ((1, 0), (0, 1), (-1, -1))          # the cube roots of unity in Z[w]
B_GROVER = (((-1, 0), (2, 0), (2, 0)),
            ((2, 0), (-1, 0), (2, 0)),
            ((2, 0), (2, 0), (-1, 0)))       # three times the Grover coin


def b_zmul(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2 - y1 * y2)


def b_zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def b_zconj(a):
    return (a[0] - a[1], -a[1])


def b_znorm(a):
    return a[0] * a[0] - a[0] * a[1] + a[1] * a[1]


def b_ztrace(a):
    return 2 * a[0] - a[1]


B_SHIFT = tuple(CELL_INDEX[(b_vadd(x, l), l)] for (x, l) in CELLS)


def b_coin_apply(psi, n):
    """the coin C(x) = G . D(x) with D(x) = diag(w^{n_l(x)}): site-block
    diagonal, and reading the count field ONLY through its residue."""
    out = [B_Z0] * DIM
    for s in range(NACT):
        base = s * len(DECLARED_LINKS)
        src = [b_zmul(psi[base + j], B_WPOW[n[base + j] % B_Q])
               for j in range(len(DECLARED_LINKS))]
        for i in range(len(DECLARED_LINKS)):
            tot = B_Z0
            for j in range(len(DECLARED_LINKS)):
                tot = b_zadd(tot, b_zmul(B_GROVER[i][j], src[j]))
            out[base + i] = tot
    return out


def b_walk_step(psi, n):
    """one coupled step's quantum half: coin, then shift along the link."""
    post = b_coin_apply(psi, n)
    out = [B_Z0] * DIM
    for m in range(DIM):
        out[B_SHIFT[m]] = post[m]
    return tuple(out), tuple(post)


def b_born_menu(post):
    """reading A: the menu at a site is the three link traversals, weighted by
    the post-coin Born weight."""
    return tuple(b_zmul(z, b_zconj(z))[0] for z in post)


def b_record_menu(n):
    """reading B: the weight is the division count itself."""
    return tuple(tuple(n[s * len(DECLARED_LINKS) + i]
                       for i in range(len(DECLARED_LINKS)))
                 for s in range(NACT))


def b_coin_fiber(bound):
    """the S_3-covariant unitary coins over the arena's own ring: C = aI + bJ
    with |a| = 1 and a conj(b) + conj(a) b + q |b|^2 = 0, carried over the
    ring with the arena's own denominator."""
    unit = B_Q * B_Q
    A = [(x, y) for x in range(-bound, bound + 1)
         for y in range(-bound, bound + 1) if b_znorm((x, y)) == unit]
    sols, classes = [], collections.defaultdict(list)
    for a in A:
        for x in range(-bound, bound + 1):
            for y in range(-bound, bound + 1):
                b = (x, y)
                if b_ztrace(b_zmul(a, b_zconj(b))) + B_Q * b_znorm(b) == 0:
                    sols.append((a, b))
                    r = b_zmul(b, b_zconj(a))
                    classes[(Fraction(r[0], unit), Fraction(r[1], unit))].append((a, b))
    grover = [c for c in classes if c == (Fraction(-2, B_Q), Fraction(0))]
    return len(A), len(sols), len(classes), len(grover), sorted(
        (str(k[0]), str(k[1])) for k in classes)


def b_seam_rows():
    """SEC-2's seam: at a shared site the two sectors' declared directions live
    in a tangent space of twice the declared dimension, and each direction
    contributes one row of the symmetric square."""
    d = 2 * B_DIMENSION
    dirs = []
    for half in range(2):
        base = [0] * d
        e1, e2 = list(base), list(base)
        e1[2 * half] = 1
        e2[2 * half + 1] = 1
        s = [e1[i] + e2[i] for i in range(d)]
        dirs.extend([tuple(e1), tuple(e2), tuple(s)])
    return [[v[i] * v[j] for i in range(d) for j in range(i, d)] for v in dirs]


def b_rank(mat):
    m = [[Fraction(x) for x in row] for row in mat]
    r = 0
    for c in range(len(m[0])):
        piv = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c] / m[r][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
    return r


def b_direction_profile(declared):
    """the whole census, rebuilt for an arbitrary choice of declared classes.
    Used to price the direction declaration."""
    links = tuple(CLASS_DIR[k] for k in declared)
    cells = tuple((x, l) for x in SITES for l in links)
    dim = len(cells)
    parts = b_raw_census()["parts"]

    def rvec(P):
        return tuple(1 if any(x in g and b_vadd(x, l) in g for g in P) else 0
                     for (x, l) in cells)
    vecs = [rvec(P) for P in parts]
    sat = [i for i, v in enumerate(vecs) if sum(v) == NACT]
    V = [vecs[i] for i in sat]
    strict = sum(1 for a in V for b in V for c in V
                 if all(a[k] + b[k] + c[k] >= 1 for k in range(dim)))
    tgt = [1, 1, 2] * NACT
    flat = 0
    for a in V:
        for b in V:
            ab = [a[k] + b[k] for k in range(dim)]
            if any(ab[k] > tgt[k] for k in range(dim)):
                continue
            for c in V:
                abc = [ab[k] + c[k] for k in range(dim)]
                if any(abc[k] > tgt[k] for k in range(dim)):
                    continue
                for d in V:
                    if all(abc[k] + d[k] == tgt[k] for k in range(dim)):
                        flat += 1

    def fp(F):
        return frozenset(k for k, (x, l) in enumerate(cells)
                         if x in F and b_vadd(x, l) in F)
    groups = list(combinations(range(NACT), B_ARITY))
    sizes = collections.Counter(len(fp(frozenset(SITES[i] for i in t)))
                                for t in groups)
    blocks = {tuple(sorted(fp(frozenset(SITES[i] for i in t))))
              for t in groups if fp(frozenset(SITES[i] for i in t))}
    st = collections.defaultdict(set)
    for k, (x, l) in enumerate(cells):
        st[x].add(k)
        st[b_vadd(x, l)].add(k)
    return (dim, len(sat), strict, flat, tuple(sorted(sizes.items())),
            len(blocks), tuple(sorted(collections.Counter(
                len(v) for v in st.values()).items())))


def b_local_compat(fs, pos, ov, t, s, pt, ps, perms):
    for x in ov[t][s]:
        if fs[t][perms[pt][pos[t][x]]] != fs[s][perms[ps][pos[s][x]]]:
            return False
    return True


def b_groupoid_counts(H, widths):
    """the local-relabelling groupoid of a history: |Gamma_w| at each declared
    window width, and the global count."""
    perms = list(permutations(range(B_ARITY)))
    npg = len(perms)
    fs = [sorted(SITE_INDEX[x] for x in F) for F in H]
    T = len(H)
    pos = [{x: i for i, x in enumerate(f)} for f in fs]
    ov = [[sorted(set(fs[t]) & set(fs[s])) for s in range(T)] for t in range(T)]

    def win(w):
        if w == 0:
            return npg ** T
        ok = [[[[b_local_compat(fs, pos, ov, t, s, pt, ps, perms)
                 for ps in range(npg)] for pt in range(npg)]
               if 0 < t - s <= w else None for s in range(T)] for t in range(T)]
        states = {(): 1}
        for t in range(T):
            nxt: dict = {}
            for st, cnt in states.items():
                base = t - len(st)
                for pt in range(npg):
                    good = True
                    for j, ps in enumerate(st):
                        s = base + j
                        if 0 < t - s <= w and not ok[t][s][pt][ps]:
                            good = False
                            break
                    if good:
                        key = (st + (pt,))[-w:]
                        nxt[key] = nxt.get(key, 0) + cnt
            states = nxt
        return sum(states.values())

    total, cur = 0, [0] * T

    def bt(i):
        nonlocal total
        if i == T:
            total += 1
            return
        for pt in range(npg):
            if all(b_local_compat(fs, pos, ov, i, s, pt, cur[s], perms)
                   for s in range(i)):
                cur[i] = pt
                bt(i + 1)
    bt(0)
    counts = [win(w) for w in widths]
    thr = 0
    while win(thr) != total:
        thr += 1
    return counts, total, thr


# ===========================================================================
# SECTION B.  s_*  --  THE STRIPPING.
#   The eraser sees both sides; that is what an eraser is.  What it emits
#   carries no actor and no site: only token ids and the blocks they fall in.
# ===========================================================================

S_MULT, S_ADD = 5, 11


def s_coordinate(mult, add):
    return {k: (mult * k + add) % DIM for k in range(DIM)}


def s_bare_blocks(corpus, pi):
    """the DISTINCT record blocks of a corpus, in the emitted coordinate."""
    out = set()
    for _t, H in corpus:
        for F in H:
            f = b_cell_footprint(F)
            if f:
                out.add(tuple(sorted(pi[c] for c in f)))
    return sorted(out)


def s_bare_history(H, pi):
    return tuple(tuple(sorted(pi[c] for c in b_cell_footprint(F)))
                 for F in H if b_cell_footprint(F))


def s_type_walk(obj, depth=0):
    """the emitted object's shape: nesting depth and leaf types."""
    if isinstance(obj, int):
        return depth, {"int"}
    if isinstance(obj, (tuple, list, frozenset, set)):
        d, ts = depth, set()
        for o in obj:
            dd, tt = s_type_walk(o, depth + 1)
            d = max(d, dd)
            ts |= tt
        return d, ts
    return depth, {type(obj).__name__}


# ===========================================================================
# SECTION C.  r_*  --  THE RECONSTRUCTOR.
#   Reads record bytes and nothing else: set membership, set meets, maximal
#   cliques.  No arithmetic on token ids anywhere.
# ===========================================================================

def r_reconstruct(blocks):
    """paper-41's rule, re-implemented: two cells belong to a common actor when
    one event wrote them together, or when the cells written with each of them
    meet in the largest number any never-co-written pair attains.  Where the
    never-co-written pairs attain fewer than two distinct values the rule
    REFUSES rather than choosing one."""
    blocks = [frozenset(b) for b in blocks if b]
    if not blocks:
        return "NO-RECORD-BLOCKS", frozenset(), None
    toks = sorted({t for b in blocks for t in b})
    co = collections.defaultdict(set)
    with_ = collections.defaultdict(set)
    for b in blocks:
        for t in b:
            co[t] |= (set(b) - {t})
            with_[t] |= set(b)
    vals = set()
    for u, v in combinations(toks, 2):
        if v not in co[u]:
            vals.add(len(with_[u] & with_[v]))
    if len(vals) < 2:
        return "THRESHOLD-UNDETERMINED", frozenset(), None
    theta = max(vals)
    adj = {t: set() for t in toks}
    for u, v in combinations(toks, 2):
        if v in co[u] or len(with_[u] & with_[v]) == theta:
            adj[u].add(v)
            adj[v].add(u)
    cliques = r_maximal_cliques(toks, adj)
    top = max(len(c) for c in cliques)
    cast = frozenset(c for c in cliques if len(c) == top)
    memb = collections.Counter()
    for a in cast:
        for t in a:
            memb[t] += 1
    if any(memb[t] == 0 for t in toks):
        return "TOKEN-IN-NO-ACTOR", cast, theta
    if any(memb[t] != 2 for t in toks):
        return "TOKEN-NOT-IN-EXACTLY-TWO", cast, theta
    return "CERTIFIED", cast, theta


def r_maximal_cliques(verts, adj):
    out = []

    def bk(R, P, X):
        if not P and not X:
            out.append(frozenset(R))
            return
        piv = max(P | X, key=lambda u: len(adj[u] & P))
        for v in list(P - adj[piv]):
            bk(R | {v}, P & adj[v], X & adj[v])
            P = P - {v}
            X = X | {v}
    bk(set(), set(verts), set())
    return out


def r_pairs_of(cast):
    """each token's owner pair, read off the derived cast alone."""
    members = sorted(cast, key=sorted)
    out = {}
    for t in sorted({x for a in cast for x in a}):
        out[t] = frozenset(i for i, a in enumerate(members) if t in a)
    return out, members


def r_link_graph(cast):
    pairs, members = r_pairs_of(cast)
    adj = {i: set() for i in range(len(members))}
    for _t, p in pairs.items():
        a, b = sorted(p)
        adj[a].add(b)
        adj[b].add(a)
    return adj, pairs, members


def r_graph_automorphisms(adj):
    """every relabelling of the derived actors preserving the derived link
    structure.  Exhaustive: a backtracking search over the whole symmetric
    group, pruned at each partial assignment, so no permutation is skipped."""
    n = len(adj)
    out, img = [], [None] * n

    def bt(i, used):
        if i == n:
            out.append(tuple(img))
            return
        for v in range(n):
            if v in used:
                continue
            ok = True
            for j in range(i):
                if ((v in adj[img[j]]) != (i in adj[j])):
                    ok = False
                    break
            if ok:
                img[i] = v
                bt(i + 1, used | {v})
                img[i] = None
    bt(0, frozenset())
    return out


def group_set_stabilizer(n, arity, family):
    """every relabelling carrying a declared family of groups to itself.
    Exhaustive over the whole symmetric group by the same pruned search."""
    fam = frozenset(frozenset(g) for g in family)
    out, img = [], [None] * n

    def bt(i, used):
        if i == n:
            out.append(tuple(img))
            return
        for v in range(n):
            if v in used:
                continue
            img[i] = v
            good = True
            for g in combinations(range(i + 1), arity):
                if i not in g:
                    continue
                src = frozenset(g)
                dst = frozenset(img[j] for j in g)
                if (src in fam) != (dst in fam):
                    good = False
                    break
            if good:
                bt(i + 1, used | {v})
            img[i] = None
    bt(0, frozenset())
    return out


def r_direction_splittings(adj, pairs):
    """the ways the derived link structure splits into disjoint classes, each
    class a spanning union of triangles.  The record offers these and prefers
    none."""
    toks = sorted(pairs)
    n = len(adj)
    tok_of = {frozenset(p): t for t, p in pairs.items()}
    # a candidate class is a partition of the actors into cliques of the
    # declared arity; its tokens are the edges those cliques carry.
    tri = [c for c in combinations(range(n), B_ARITY)
           if all(b in adj[a] for a, b in combinations(c, 2))]
    parts, cur = [], []

    def bt(rem):
        if not rem:
            parts.append(list(cur))
            return
        a = min(rem)
        for c in tri:
            if a not in c or not set(c) <= rem:
                continue
            cur.append(c)
            bt(rem - set(c))
            cur.pop()
    bt(frozenset(range(n)))
    classes = []
    for P in parts:
        toks_here = frozenset(tok_of[frozenset(e)]
                              for c in P for e in combinations(c, 2))
        classes.append(toks_here)
    classes = sorted(set(classes), key=sorted)
    splits = set()
    for tri in combinations(classes, B_ARITY):
        if len(set().union(*tri)) == len(toks):
            splits.add(frozenset(tri))
    return len(classes), splits


def r_cast_solutions(blocks):
    """THE REPRESENTATION-CLASS SEARCH.  Every family of token-sets under which each
    record block is a triangle carrying no foreign token.  Actor names are not
    part of a solution: solutions are collected as families of token sets, so
    two that differ by a renaming are one."""
    blocks = [tuple(sorted(b)) for b in blocks]
    nt = len({t for b in blocks for t in b})
    toks = sorted({t for b in blocks for t in b})
    bof = collections.defaultdict(list)
    for bi, b in enumerate(blocks):
        for t in b:
            bof[t].append(bi)
    order, seen, frontier = [], set(), [blocks[0][0]]
    while len(order) < nt:
        if not frontier:
            frontier = [t for t in toks if t not in seen][:1]
        t = frontier.pop(0)
        if t in seen:
            continue
        seen.add(t)
        order.append(t)
        for bi in bof[t]:
            for u in blocks[bi]:
                if u not in seen:
                    frontier.append(u)
    assign, sols = {}, set()

    def block_ok(bi, final):
        ts = blocks[bi]
        ps = [assign.get(t) for t in ts]
        if any(p is None for p in ps):
            return True
        U = set().union(*ps)
        if len(U) != len(ts):
            return False
        for p, q in combinations(ps, 2):
            if len(p & q) != 1:
                return False
        if final:
            for t, p in assign.items():
                if t not in ts and p <= U:
                    return False
        return True

    def rec(i, maxid):
        if i == len(order):
            for bi in range(len(blocks)):
                if not block_ok(bi, True):
                    return
            fam = collections.defaultdict(set)
            for t, p in assign.items():
                for a in p:
                    fam[a].add(t)
            sols.add(frozenset(frozenset(v) for v in fam.values()))
            return
        t = order[i]
        if maxid < 0:
            cand = [frozenset((0, 1))]
        else:
            cand = [frozenset(p) for p in combinations(range(maxid + 1), 2)]
            cand += [frozenset((a, maxid + 1)) for a in range(maxid + 1)]
        for p in cand:
            assign[t] = p
            if all(block_ok(bi, False) for bi in bof[t]):
                rec(i + 1, max(maxid, max(p)))
            del assign[t]
    rec(0, -1)
    return sols


# ===========================================================================
# SECTION D.  k_*  --  THE COMPARATOR.
#   Decides agreement and rebuilds the verdict.  It calls no builder, no
#   stripper and no reconstructor, and it types no arena cardinality.
# ===========================================================================

def k_set_equal(derived, declared):
    return frozenset(derived) == frozenset(declared)


def k_census_word(rows):
    unbacked = [r for r in rows if r["backing"] == "NONE"]
    return "CENSUS-TOTAL" if not unbacked else "CENSUS-PARTIAL"


def k_circularity_word(has_cycle, solutions, matches, residue):
    """the word names UNIQUENESS INSIDE A DECLARED REPRESENTATION CLASS.  It
    is not a fixed point of the actor-record-emission dynamics, and the
    grammar carries no word that would say so."""
    if not has_cycle:
        return "ACYCLIC"
    if solutions != 1 or not matches:
        return "CIRCULAR-BLOCKED-AT-THE-CAST"
    if residue > 1:
        return ("CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS-"
                "UP-TO-THE-DIRECTION-DECLARATION")
    return "CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS"


def k_q58_word(recovering, refusing):
    if refusing == 0 and recovering > 1:
        return "Q58-EMERGENCE-GENERATOR-INDEPENDENT"
    if recovering == 0:
        return "Q58-UNDECIDED-NO-SECOND-MECHANISM"
    if recovering > 1 and refusing > 0:
        return "Q58-IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS"
    return "Q58-UNDECIDED-NO-SECOND-MECHANISM"


def k_parameter_word(free):
    return "ISP-IS-ONE-THEORY" if free == 0 else "ISP-IS-A-FAMILY"


def k_head(seg):
    return seg


def k_parse_head(segment):
    """the verdict's own numerals, parsed back out of the emitted string by a
    reader that shares no code and no literal with the builder."""
    out = {}
    for m in re.finditer(r"([A-Z0-9\-]+)=([0-9][0-9,]*)", segment):
        out[m.group(1)] = int(m.group(2).replace(",", ""))
    return out


# ===========================================================================
# PLUMBING
# ===========================================================================

def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def read_text(rel):
    with open(os.path.join(REPO, rel), "r", encoding="utf-8") as fh:
        return fh.read()


def com(n):
    return "{:,}".format(n)


def audit_no_floats(src):
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            bad.append(node.lineno)
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "float":
            bad.append(node.lineno)
    return bad


REGION_PREFIX = (("b_", "builder"), ("s_", "stripper"),
                 ("r_", "reconstructor"), ("k_", "comparator"))


def region_of(name):
    for pre, reg in REGION_PREFIX:
        if name.startswith(pre):
            return reg
    return "plumbing"


def module_call_graph(src):
    tree = ast.parse(src)
    out = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            calls = set()
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call):
                    f = getattr(sub.func, "id", None) or getattr(sub.func, "attr", None)
                    if f:
                        calls.add(f)
                if isinstance(sub, ast.Name):
                    calls.add(sub.id)
            out[node.name] = calls
    return out


def audit_regions(src):
    """no reconstructor and no comparator may REACH a builder or a stripper at
    any depth."""
    g = module_call_graph(src)
    offences = []
    for name in g:
        if region_of(name) not in ("reconstructor", "comparator"):
            continue
        seen, stack = set(), [name]
        while stack:
            cur = stack.pop()
            for callee in g.get(cur, ()):
                if callee in seen:
                    continue
                seen.add(callee)
                if region_of(callee) in ("builder", "stripper"):
                    offences.append("%s reaches %s" % (name, callee))
                if callee in g:
                    stack.append(callee)
    return offences


def region_census(src):
    g = module_call_graph(src)
    return collections.Counter(region_of(n) for n in g)


def receipt_type_walk(obj, bad, path="$"):
    if isinstance(obj, bool) or isinstance(obj, int) or obj is None:
        return
    if isinstance(obj, str):
        return
    if isinstance(obj, float):
        bad.append(path)
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            receipt_type_walk(v, bad, path + "." + str(k))
        return
    if isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            receipt_type_walk(v, bad, path + "[%d]" % i)
        return
    bad.append(path + ":" + type(obj).__name__)


MUT = {"none": None}


def mut(tag, state):
    return state.get("mutant") == tag


# ===========================================================================
# SECTION E.  THE MEASUREMENT.  Every published value is produced here, once,
# and every gate below is a predicate over this payload and nothing else.
# ===========================================================================

CLASS_ALPHABET = ("PRIMITIVE", "DECLARED", "GENERATED", "RECONSTRUCTED",
                  "LAW-SELECTED")
BACKING_ALPHABET = ("COMPUTED-HERE", "SEALED-CITATION")


def measure():
    R: dict = {}
    corp, parts, strict, flatq, scheds, smeta = b_build_corpus()
    pi = s_coordinate(S_MULT, S_ADD)
    DA = b_declared_actors()
    PAIRS = b_declared_pairs()

    # ---- the arena ------------------------------------------------------
    R["arena_sites"] = NACT
    R["arena_dimension"] = B_DIMENSION
    R["arena_field_order"] = B_Q
    R["arena_event_arity"] = B_ARITY
    R["arena_parallel_classes"] = len(CLASS_NAMES)
    R["arena_declared_directions"] = len(DECLARED_LINKS)
    R["arena_cells"] = DIM
    R["arena_groupings"] = len(parts)
    R["arena_saturating_groupings"] = len(b_raw_census()["sat"])
    R["arena_strict_triples"] = len(strict)
    R["arena_flat_quadruples"] = len(flatq)
    R["arena_window_schedules"] = len(scheds)
    R["arena_automorphisms"] = len(b_arena_automorphisms())
    R["arena_menu"] = len(b_declared_menu())
    R["arena_translation_subgroups"] = len(b_translation_subgroups())
    groups = list(combinations(range(NACT), B_ARITY))
    fsizes = collections.Counter(
        len(b_cell_footprint(frozenset(SITES[i] for i in t))) for t in groups)
    R["arena_actor_groups"] = len(groups)
    R["arena_groups_writing_three"] = fsizes[B_ARITY]
    R["arena_groups_writing_two"] = fsizes[2]
    R["arena_groups_writing_none"] = fsizes[0]

    # ---- the corpus -----------------------------------------------------
    bycorp = collections.Counter(t for t, _ in corp)
    R["corpus_slots"] = len(corp)
    R["corpus_c1"] = bycorp["C1"]
    R["corpus_c2"] = bycorp["C2"]
    R["corpus_c3"] = bycorp["C3"]
    hist = {h for _t, h in corp}
    R["corpus_distinct_histories"] = len(hist)
    events = collections.Counter()
    for _t, H in corp:
        for F in H:
            events[frozenset(sorted(SITE_INDEX[x] for x in F))] += 1
    R["corpus_distinct_events"] = len(events)
    R["corpus_events_writing_nothing"] = sum(
        1 for e in events if not b_cell_footprint(frozenset(SITES[i] for i in e)))

    # ---- the record -----------------------------------------------------
    blocks = s_bare_blocks(corp, pi)
    R["record_blocks"] = len(blocks)
    R["record_block_sizes"] = sorted({len(b) for b in blocks})
    unwritten = partly = nothing = 0
    for _t, H in corp:
        fps = [b_cell_footprint(F) for F in H]
        unwritten += sum(1 for f in fps if not f)
        if any(not f for f in fps):
            partly += 1
        if not any(fps):
            nothing += 1
    R["record_unwritten_events"] = unwritten
    R["record_partly_unwritten_histories"] = partly
    R["record_histories_writing_nothing"] = nothing
    fibers = collections.defaultdict(list)
    for H in hist:
        fibers[s_bare_history(H, pi)].append(H)
    R["record_distinct_bare_records"] = len(fibers)
    coll = {k: v for k, v in fibers.items() if len(v) > 1}
    R["record_collision_classes"] = len(coll)
    R["record_colliding_histories"] = sum(len(v) for v in coll.values())
    R["record_vanishing_histories"] = sum(len(v) - 1 for v in coll.values())
    fields = sorted({b_record_field(H) for H in hist})
    R["record_max_blocks_in_a_history"] = max(
        len({tuple(sorted(pi[c] for c in b_cell_footprint(F)))
             for F in H if b_cell_footprint(F)}) for H in hist)
    R["record_count_fields"] = len(fields)
    R["record_residue_fields"] = len({tuple(v % B_Q for v in n) for n in fields})
    byfield = collections.defaultdict(set)
    for H in hist:
        byfield[b_record_field(H)].add(H)
    R["record_field_classes_multi"] = sum(1 for v in byfield.values() if len(v) > 1)
    R["record_histories_in_multi_classes"] = sum(
        len(v) for v in byfield.values() if len(v) > 1)

    # ---- the state ------------------------------------------------------
    psi_uniform = [B_Z1] * DIM
    succ = {}
    for n in fields:
        nxt, post = b_walk_step(list(psi_uniform), list(n))
        succ[n] = (nxt, post)
    R["state_successors_distinct"] = len({succ[n] for n in fields})
    same = diff = agree = disagree = cross = 0
    for a, b in combinations(fields, 2):
        ra = tuple(v % B_Q for v in a)
        rb = tuple(v % B_Q for v in b)
        if ra == rb:
            same += 1
            if succ[a] == succ[b]:
                agree += 1
            else:
                disagree += 1
        else:
            diff += 1
            if succ[a] == succ[b]:
                cross += 1
    R["state_equal_residue_pairs"] = same
    R["state_equal_residue_agreements"] = agree
    R["state_equal_residue_disagreements"] = disagree
    R["state_distinct_residue_pairs"] = diff
    R["state_distinct_residue_collisions"] = cross
    R["state_reading_a_menus"] = len({succ[n][1] for n in fields})
    R["state_reading_b_menus"] = len({b_record_menu(n) for n in fields})
    R["state_reading_b_menus_on_residues"] = len(
        {b_record_menu(tuple(v % B_Q for v in n)) for n in fields})
    R["state_components"] = 3
    R["state_background_components"] = 6

    # ---- the reconstruction and the gauge -------------------------------
    cert, cast, theta = r_reconstruct(blocks)
    R["recon_certificate"] = cert
    R["recon_threshold"] = theta
    R["recon_cast_size"] = len(cast)
    R["recon_actor_size"] = max(len(a) for a in cast)
    declared_moved = frozenset(frozenset(pi[c] for c in v) for v in DA.values())
    R["recon_set_equality"] = k_set_equal(cast, declared_moved)
    adj, dpairs, members = r_link_graph(cast)
    R["recon_derived_pairs"] = len(dpairs)
    R["recon_degree"] = max(len(v) for v in adj.values())
    autos = r_graph_automorphisms(adj)
    # the same group in the DECLARED labelling, so that the quotient census
    # below acts on site-indexed objects and not on derived indices.
    adj_site = {i: set() for i in range(NACT)}
    for _k, pr in PAIRS.items():
        a, b = sorted(pr)
        adj_site[a].add(b)
        adj_site[b].add(a)
    autos_site = r_graph_automorphisms(adj_site)
    R["inv_symmetric_group"] = _factorial(NACT)
    R["inv_link_graph_automorphisms"] = len(autos)
    R["inv_link_graph_automorphisms_declared"] = len(autos_site)
    R["inv_two_labellings_agree"] = (len(autos) == len(autos_site))
    R["inv_arena_automorphisms"] = len(b_arena_automorphisms())
    R["inv_direction_index"] = len(autos) // len(b_arena_automorphisms())
    nclasses, splits = r_direction_splittings(adj, dpairs)
    R["inv_candidate_direction_classes"] = nclasses
    R["inv_direction_splittings"] = len(splits)
    declared_split = frozenset(
        frozenset(t for t in range(DIM) if _preimage(pi, t) % B_ARITY == d)
        for d in range(B_ARITY))
    R["inv_declared_splitting_offered"] = declared_split in splits

    # the law's own stabilizer in the symmetric group
    admissible_groups = {frozenset(SITE_INDEX[x] for x in g)
                         for i in b_raw_census()["sat"] for g in parts[i]}
    stab = group_set_stabilizer(NACT, B_ARITY, admissible_groups)
    R["inv_admissible_groups"] = len(admissible_groups)
    R["inv_law_stabilizer"] = len(stab)
    R["inv_law_blind_to_direction"] = (len(stab) == len(autos))

    # the direction declaration priced by rebuilding the whole census
    profs = {}
    for dec in combinations(CLASS_NAMES, B_ARITY):
        profs[dec] = b_direction_profile(dec)
    vals = list(profs.values())
    R["inv_direction_choices"] = len(profs)
    R["inv_direction_census_numbers"] = len(vals[0])
    R["inv_direction_profiles_agreeing"] = sum(1 for v in vals if v == vals[0])

    # the local relabelling group at the event grain
    c1hist = [h for t, h in corp if t == "C1"]
    widths = list(range(0, 6))
    counts, total, thr = b_groupoid_counts(c1hist[0], widths)
    R["inv_local_group_order"] = _factorial(B_ARITY)
    R["inv_local_widths"] = [[w, c] for w, c in zip(widths, counts)]
    R["inv_local_global_count"] = total
    R["inv_local_collapse_width"] = thr
    thrs = collections.Counter()
    for H in c1hist:
        _c, tt, th = b_groupoid_counts(H, [0])
        thrs[(th, tt)] += 1
    R["inv_local_c1_histories"] = len(c1hist)
    R["inv_local_c1_uniform"] = (len(thrs) == 1)
    R["inv_local_c1_threshold"] = sorted(thrs)[0][0]
    R["inv_local_c1_global"] = sorted(thrs)[0][1]

    # what survives the quotient
    AUTA = [tuple(p) for p in b_arena_automorphisms()]
    AUTL = [tuple(p) for p in autos_site]

    def himg(H, p):
        return tuple(sorted(tuple(sorted(p[SITE_INDEX[x]] for x in F)) for F in H))

    def fimg(n, p):
        d = {}
        for k in range(DIM):
            d[tuple(sorted(p[i] for i in PAIRS[k]))] = n[k]
        return tuple(v for _k, v in sorted(d.items()))
    R["quotient_histories"] = len(hist)
    R["quotient_histories_arena"] = len({min(himg(H, p) for p in AUTA) for H in hist})
    R["quotient_histories_link"] = len({min(himg(H, p) for p in AUTL) for H in hist})
    R["quotient_fields"] = len(fields)
    R["quotient_fields_arena"] = len({min(fimg(n, p) for p in AUTA) for n in fields})
    R["quotient_fields_link"] = len({min(fimg(n, p) for p in AUTL) for n in fields})

    # ---- the circularity and the fixed point ----------------------------
    R["dep_edges"] = len(DEPENDENCY_EDGES)
    R["dep_nodes"] = len({a for a, _b, _w in DEPENDENCY_EDGES} |
                         {b for _a, b, _w in DEPENDENCY_EDGES})
    cycles = _all_cycles(DEPENDENCY_EDGES)
    R["dep_cycles"] = len(cycles)
    R["dep_cycle_length"] = min(len(c) for c in cycles) if cycles else 0
    R["dep_longest_cycle_length"] = max(len(c) for c in cycles) if cycles else 0
    actor_record = [c for c in cycles if "ACTOR" in c and "RECORD-BLOCK" in c]
    R["dep_actor_record_cycles"] = len(actor_record)
    R["dep_actor_record_cycle"] = (sorted(actor_record, key=len)[0]
                                   if actor_record else [])
    R["dep_actor_record_cycle_length"] = (
        len(R["dep_actor_record_cycle"]) if actor_record else 0)
    sols = r_cast_solutions(blocks)
    R["class_cast_solutions"] = len(sols)
    R["class_cast_matches_declared"] = (sols == {declared_moved})
    R["class_cast_residue"] = len(splits)

    # ---- Q58: the mechanism arms ----------------------------------------
    arms = []
    bycorpus = collections.defaultdict(set)
    for t, H in corp:
        for F in H:
            f = b_cell_footprint(F)
            if f:
                bycorpus[t].add(tuple(sorted(pi[c] for c in f)))
    site_star = [tuple(sorted(pi[s * len(DECLARED_LINKS) + i]
                              for i in range(len(DECLARED_LINKS))))
                 for s in range(NACT)]
    unrestricted = [tuple(sorted(pi[c] for c in
                                 b_cell_footprint(frozenset(SITES[i] for i in t))))
                    for t in groups
                    if b_cell_footprint(frozenset(SITES[i] for i in t))]
    triangles = [b for b in unrestricted if len(b) == B_ARITY]
    pairs_only = [b for b in unrestricted if len(b) == 2]
    ARMS = [
        ("THE-COMMITTED-GRAMMAR", "GRAMMAR", B_ARITY,
         sorted(set().union(*bycorpus.values()))),
        ("THE-STRICT-COVER-DRIVER", "GRAMMAR", B_ARITY, sorted(bycorpus["C1"])),
        ("THE-CONCATENATION-DRIVER", "GRAMMAR", B_ARITY, sorted(bycorpus["C2"])),
        ("THE-DRIVEN-WINDOW", "GRAMMAR", B_ARITY, sorted(bycorpus["C3"])),
        ("THE-PAIRWISE-LINKED-GROUPS", "GRAMMAR-FREE", B_ARITY, sorted(set(triangles))),
        ("THE-UNRESTRICTED-GROUPS", "GRAMMAR-FREE", B_ARITY, sorted(set(unrestricted))),
        ("THE-NON-COLLINEAR-GROUPS", "GRAMMAR-FREE", 2, sorted(set(pairs_only))),
        ("THE-COUPLED-WALK-EMISSION", "DYNAMICS", 2,
         sorted({(pi[m],) for m in range(DIM)})),
        ("THE-COUPLED-WALK-SITE-MENU", "DYNAMICS", 2, sorted(set(site_star))),
    ]
    inv = {pi[k]: PAIRS[k] for k in range(DIM)}

    def is_triangle(block):
        if len(block) != B_ARITY:
            return False
        ps = [inv[t] for t in block]
        return (len(set().union(*ps)) == B_ARITY
                and all(len(p & q) == 1 for p, q in combinations(ps, 2)))
    for name, kind, arity, bl in ARMS:
        c, ca, th = r_reconstruct(bl)
        arms.append({"arm": name, "mechanism": kind, "event_arity": arity,
                     "blocks": len(bl),
                     "block_sizes": sorted(collections.Counter(
                         len(b) for b in bl).items()),
                     "certificate": c,
                     "threshold": th,
                     "all_blocks_triangular": all(is_triangle(b) for b in bl),
                     "tokens_covered": len({t for b in bl for t in b}),
                     "cast_recovered": bool(ca == declared_moved)})
    R["q58_arms"] = arms
    R["q58_arms_total"] = len(arms)
    R["q58_arms_recovering"] = sum(1 for a in arms if a["cast_recovered"])
    R["q58_arms_refusing"] = sum(1 for a in arms if not a["cast_recovered"])
    R["q58_arms_at_declared_arity"] = sum(
        1 for a in arms if a["event_arity"] == B_ARITY)
    R["q58_arms_all_blocks_at_arity"] = sum(
        1 for a in arms if all(s == B_ARITY for s, _n in a["block_sizes"]))
    # the split criterion, stated as a predicate and MEASURED, not asserted.
    # The block size alone is not it: one refusing arm writes blocks of the
    # declared arity.  What separates the arms is triangularity with every
    # token covered.
    R["q58_split_is_the_block_size"] = all(
        a["cast_recovered"] == all(s == B_ARITY for s, _n in a["block_sizes"])
        for a in arms)
    R["q58_split_is_triangularity"] = all(
        a["cast_recovered"] == (a["all_blocks_triangular"]
                                and a["tokens_covered"] == DIM)
        for a in arms)
    R["q58_triangular_arms"] = sum(1 for a in arms if a["all_blocks_triangular"])
    R["q58_mechanism_kinds"] = sorted({a["mechanism"] for a in arms})

    # ---- the parameters --------------------------------------------------
    nA, nsol, ncls, ngrov, ratios = b_coin_fiber(2 * len(DECLARED_LINKS) + 2)
    R["coin_norm_solutions"] = nA
    R["coin_ring_solutions"] = nsol
    R["coin_classes"] = ncls
    R["coin_grover_classes"] = ngrov
    R["coin_ratios"] = ratios
    seam = b_seam_rows()
    R["seam_rows"] = len(seam)
    R["seam_columns"] = len(seam[0])
    R["seam_rank"] = b_rank(seam)
    R["seam_kernel"] = len(seam[0]) - b_rank(seam)
    R["param_rows"] = PARAMETER_ROWS
    R["param_total"] = len(PARAMETER_ROWS)
    R["param_free"] = sum(1 for p in PARAMETER_ROWS if p[3] == "FREE")
    R["param_invariant"] = sum(
        1 for p in PARAMETER_ROWS if p[3] == "INVARIANT-IN-THE-SUBSTRATE-CENSUS")
    R["param_derived"] = sum(1 for p in PARAMETER_ROWS if p[3] == "DERIVED")
    R["param_reconstructed"] = sum(
        1 for p in PARAMETER_ROWS if p[3] == "RECONSTRUCTED-CONDITIONALLY")
    R["param_initial"] = sum(1 for p in PARAMETER_ROWS if p[3] == "INITIAL")
    R["param_selected_by_a_law"] = sum(1 for p in PARAMETER_ROWS if p[4] == "YES")
    R["param_free_selected_by_a_law"] = sum(
        1 for p in PARAMETER_ROWS if p[3] == "FREE" and p[4] == "YES")

    # ---- the object census ----------------------------------------------
    R["cited_gluings"] = 45010
    R["cited_chart_types"] = 16
    R["census_rows"] = census_rows(R)
    R["census_row_count"] = len(R["census_rows"])
    R["census_backed"] = sum(1 for r in R["census_rows"]
                             if r["backing"] in BACKING_ALPHABET)
    R["census_computed_here"] = sum(1 for r in R["census_rows"]
                                    if r["backing"] == "COMPUTED-HERE")
    R["census_cited"] = sum(1 for r in R["census_rows"]
                            if r["backing"] == "SEALED-CITATION")
    R["census_classes"] = sorted(collections.Counter(
        r["class"] for r in R["census_rows"]).items())
    return R


def _factorial(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def _preimage(pi, t):
    for k, v in pi.items():
        if v == t:
            return k
    raise KeyError(t)


def _all_cycles(edges):
    """every simple directed cycle of the dependency graph, as a vertex list."""
    g = collections.defaultdict(list)
    nodes = set()
    for a, b, _w in edges:
        g[a].append(b)
        nodes |= {a, b}
    out = []
    order = sorted(nodes)

    def dfs(start, u, path, onpath):
        for v in g[u]:
            if v == start:
                out.append(list(path))
            elif v not in onpath and order.index(v) > order.index(start):
                dfs(start, v, path + [v], onpath | {v})
    for s in order:
        dfs(s, s, [s], {s})
    return out


DEPENDENCY_EDGES = (
    ("ACTOR", "CELL", "a cell is an unordered pair of actors"),
    ("DIRECTION", "CELL", "a cell carries one declared direction"),
    ("ACTOR", "DIVISION-EVENT", "an event is a set of actors"),
    ("CELL", "ROUND-LAW", "saturation counts the cells a grouping covers"),
    ("ROUND-LAW", "HISTORY", "a history is a sequence of admissible rounds"),
    ("DIVISION-EVENT", "HISTORY", "a history is a sequence of events"),
    ("HISTORY", "RECORD-BLOCK", "an event writes the cells inside it"),
    ("RECORD-BLOCK", "COUNT-FIELD", "the count field tallies the blocks"),
    ("COUNT-FIELD", "QUANTUM-STATE", "the coin reads the count residue"),
    ("QUANTUM-STATE", "EMISSION", "the menu weights the next division event"),
    ("EMISSION", "COUNT-FIELD", "an emission increments the count field"),
    ("RECORD-BLOCK", "ACTOR", "the reconstruction derives the cast"),
)

PARAMETER_ROWS = (
    ("d", "the spatial dimension", "UNSWEPT", "FREE", "NO", "NDEP"),
    ("q", "the field order", "SWEPT-AT-THREE-POINTS", "FREE", "NO", "NDEP"),
    ("a", "the division-event arity", "UNSWEPT", "FREE", "NO", "ARITY-CHARTERED"),
    ("R", "the depth in rounds", "SWEPT-ALONG-THE-LADDER", "FREE", "NO", "PERR"),
    ("the window", "the driven schedule set", "DECLARED-WINDOW", "FREE", "NO", "R4DEC"),
    ("the coin", "the S_3-covariant unitary", "COMPUTED-HERE", "FREE", "NO", "COUPLING"),
    ("the coin order", "coin before or after the residue", "DECLARED-PAIR",
     "FREE", "NO", "COUPLING"),
    ("the orientation", "the sign of the shift", "DECLARED-PAIR", "FREE", "NO",
     "COUPLING"),
    ("the horizon", "the number of coupled steps", "DECLARED", "FREE", "NO",
     "COUPLING"),
    ("the reading", "the Born menu or the record menu", "DECLARED-PAIR", "FREE",
     "NO", "COUPLING"),
    ("the seam", "the completion at a shared site", "COMPUTED-HERE", "FREE", "NO",
     "SEC-2"),
    ("the ceiling", "the occupancy ceiling", "DECLARED", "FREE", "NO", "OCC"),
    ("the measure", "the measure over configurations", "A-SIMPLEX", "FREE", "NO",
     "R5M"),
    ("L", "which classes are declared links", "COMPUTED-HERE",
     "INVARIANT-IN-THE-SUBSTRATE-CENSUS", "NO", "AID"),
    ("the coordinate", "the naming of the record tokens", "ANY-BIJECTION",
     "INVARIANT-IN-THE-SUBSTRATE-CENSUS", "NO", "REC"),
    ("n", "the actor count", "COMPUTED-HERE", "RECONSTRUCTED-CONDITIONALLY",
     "NO", "THIS-UNIT"),
    ("the cell count", "the carrier size", "COMPUTED-HERE", "DERIVED", "YES",
     "THIS-UNIT"),
    ("the connection", "the group the walk's phases live in", "DECLARED",
     "DERIVED", "YES", "COUPLING"),
    ("the menu", "the admissible actor grains", "COMPUTED-HERE", "DERIVED",
     "YES", "FAC"),
    ("the state", "the initial amplitude", "AN-INITIAL-CONDITION", "INITIAL",
     "NO", "COUPLING"),
    ("the record", "the initial count field", "AN-INITIAL-CONDITION", "INITIAL",
     "NO", "COUPLING"),
)


def census_rows(R):
    """one row per object.  `class` is one of the pin's five words; `backing`
    says whether this unit computed the row or cites a sealed one."""
    C = "COMPUTED-HERE"
    S = "SEALED-CITATION"
    rows = [
        ("ACTOR", "DECLARED", C, R["arena_sites"],
         "declared as the points of the arena, and derived back from the record"),
        ("SITE", "DECLARED", C, R["arena_sites"],
         "the same objects as the actors under the weld's dictionary"),
        ("DIRECTION", "DECLARED", C, R["arena_declared_directions"],
         "three of the parallel classes of the arena are declared links"),
        ("PARALLEL-CLASS", "GENERATED", C, R["arena_parallel_classes"],
         "the resolutions of the arena, generated from the field"),
        ("CELL", "GENERATED", C, R["arena_cells"],
         "one per site and declared direction"),
        ("CO-DIVISION-PAIR", "GENERATED", C, R["arena_cells"],
         "the cell is the unordered pair, by the carrier typing"),
        ("DIVISION-EVENT", "GENERATED", C, R["arena_actor_groups"],
         "every group of the declared arity; the corpus realises some of them"),
        ("REALISED-EVENT", "GENERATED", C, R["corpus_distinct_events"],
         "the events the committed corpus actually runs"),
        ("GROUPING", "GENERATED", C, R["arena_groupings"],
         "the partitions of the actors into groups of the declared arity"),
        ("ADMISSIBLE-ROUND", "LAW-SELECTED", C, R["arena_saturating_groupings"],
         "the groupings the saturation law admits"),
        ("HISTORY", "GENERATED", C, R["corpus_distinct_histories"],
         "the distinct sequences of events the committed drivers produce"),
        ("RECORD-BLOCK", "GENERATED", C, R["record_blocks"],
         "the cells one event writes"),
        ("BARE-RECORD", "GENERATED", C, R["record_distinct_bare_records"],
         "the sequence of blocks, actor labels erased"),
        ("COUNT-FIELD", "GENERATED", C, R["record_count_fields"],
         "the division count on each cell"),
        ("QUANTUM-STATE", "DECLARED", C, R["arena_cells"],
         "one amplitude per cell, in the ring the field generates"),
        ("MENU", "LAW-SELECTED", C, R["arena_menu"],
         "the coset partitions of the translation subgroups"),
        ("NAMING", "RECONSTRUCTED", C, R["inv_link_graph_automorphisms"],
         "the relabellings the record admits of the derived cast"),
        ("DIRECTION-SPLITTING", "RECONSTRUCTED", C, R["inv_direction_splittings"],
         "the ways the derived link structure splits into classes"),
        ("COIN", "DECLARED", C, R["coin_classes"],
         "the covariant unitary family, up to a global phase"),
        ("SEAM", "DECLARED", C, R["seam_kernel"],
         "the undetermined entries the chart leaves at a shared site"),
        ("CHART", "DECLARED", S, R["cited_chart_types"],
         "the combinatorial types of a two-sector overlap"),
        ("TICK", "DECLARED", S, 1,
         "one scheduling convention; the emergent speed is one site a tick"),
        ("CARRIER-CANDIDATE", "DECLARED", S, R["arena_cells"],
         "the carrier the exclusion census selected; excitations are not "
         "declared until the excitation gate opens"),
    ]
    return [{"object": o, "class": c, "backing": bk, "cardinality": n,
             "reading": rd} for (o, c, bk, n, rd) in rows]


# ===========================================================================
# SECTION F.  THE ANCHORS, THE WALLS, THE UNIVERSES.
# ===========================================================================

ANCHORS = (
    ("REC-CARRIER", "v14/paper-41-rec.md", "G-OBJECT-CENSUS",
     "27 cells against 27 pairs, two actors in each cell at all of them, "
     "six cells per actor at all nine"),
    ("REC-NAMING", "v14/paper-41-rec.md", "G-INVARIANCE-GROUPS",
     "the record admits 1,296 namings of the derived cast and 108 of them "
     "carry the declared direction classes"),
    ("REC-DEPTH", "v14/paper-41-rec.md", "G-RECORD-REBUILT",
     "no committed history sees more than 18 of the 27 record blocks"),
    ("COUP-RESIDUE", "v14/paper-20-coupling.md", "G-STATE-READING-RELATIVE",
     "the walk consumes the count residue n mod 3, not the count."),
    ("COUP-COIN", "v14/paper-20-coupling.md", "G-COIN-FIBER",
     "falling into 6 classes up to a global phase, of which exactly 1 is "
     "+/- Grover"),
    ("OCC-CARRIER", "v14/paper-31-occ.md", "G-OBJECT-CENSUS",
     "CELLS-WITH-EXACTLY-TWO-ACTORS=27-OF-27; ACTORS-IN-EXACTLY-SIX-CELLS=9-OF-9"),
    ("SEC2-SEAM", "v14/paper-40-sec2.md", "G-SEAM-KERNEL",
     "The seam's own system is rank 6 on 10 by the chart alone, kernel 4; "
     "an unshared site's system is three equations on"),
    ("AID-GAUGE", "v14/paper-33-aid.md", "G-DIRECTION-INVARIANCE",
     "rebuilt with ANT in place of DIA the substrate returns 36 saturating, "
     "72 I7-STRICT triples and 276 G-FLAT quadruples"),
    ("NDEP-CARRIED", "v14/paper-39-ndep.md", "G-PARAMETERS",
     "NO TESTED NUMERAL IS REPRODUCED BY THE DECLARED n-ONLY READING"),
    ("EPR-MULTIPARTITE", "v14/paper-38-epr.md", "G-ARENA-REBUILT",
     "The graph is therefore complete multipartite with those three lines as "
     "its parts, and every site has degree six"),
    ("PLAN-WALLS", "v15/PLAN.md", "G-WALLS",
     "W1: reconstruction is never promoted to derivation. W2: invariance is "
     "never promoted to gauge or physical meaning before operational "
     "observables exist"),
    ("HOR-TICK", "v14/paper-42-hor.md", "G-OBJECT-CENSUS",
     "The Emergent Speed Is One Site a Tick and It Is Attained"),
    ("SEC-CHART", "v14/paper-32-sec.md", "G-OBJECT-CENSUS",
     "the family is 45010 gluings in 16 combinatorial types"),
)


def anchor_numerals(text):
    """the integers an anchor's located text carries, in order."""
    return [int(m.group(0).replace(",", ""))
            for m in re.finditer(r"(?<![\w.])\d[\d,]*(?![\w])", text)]


WALLS = (
    ("W-SCOPE",
     [r"\bat every arena\b", r"\bfor all arenas\b", r"\bin general\b",
      r"\bat any arena\b", r"\bfor any record\b", r"\bat all arenas\b",
      r"\bfor every possible\b", r"\bwithout restriction\b"],
     [r"one arena, the committed corpus", r"beyond the committed corpus"],
     (), ()),
    ("W-EMERGENCE",
     [r"\bthe actors emerge\b", r"\bactors emerge from\b",
      r"\bthe actors are emergent\b", r"\bthe cast is emergent\b",
      r"\bproves the emergence of\b",
      r"\b(?:reconstruction|result|cast|census)\s+is\s+(?:therefore\s+)?"
      r"generator[- ]independent\b",
      r"\bactors are not needed\b", r"\bactors need never be assumed\b",
      r"\bthe record alone creates\b"],
     [r"identifiability within a generative class",
      r"the reconstruction is not generator[- ]independent"],
     (), ()),
    ("W-RECONSTRUCTION-IS-NOT-DERIVATION",
     [r"\bthe actors are derived from the record\b",
      r"\bthe record derives the (?:cast|actors)\b",
      r"\bthe cast is derived\b",
      r"\bthe record selects the (?:cast|actors)\b",
      r"\bthe record selects among possible worlds\b",
      r"\bidentifiability (?:is|means) derivation\b",
      r"\breconstruction (?:therefore )?(?:shows|proves|establishes) "
      r"derivation\b",
      r"\bthe actor count is derived from the record\b"],
     [r"is identifiability and not derivation"],
     (), ()),
    ("W-INVARIANCE-IS-NOT-GAUGE",
     [r"\bis therefore gauge\b", r"\bis pure gauge\b",
      r"\bare therefore gauge\b", r"\bis a gauge redundancy\b",
      r"\bare gauge redundancies\b", r"\bis a redundancy\b",
      r"\bare redundancies\b", r"\bis physically meaningless\b",
      r"\bthe gauge quotient is\b",
      r"\bthe stabilizer is the gauge group\b"],
     [r"the gauge word is withheld here",
      r"every physical observable and every experiment"],
     (), ()),
    ("W-STATE-SCOPE",
     [r"\bthe complete state of the theory\b",
      r"\bthe universal state is\b", r"\bthis is the state of isp\b",
      r"\bthe state is complete for every dynamics\b",
      r"\bthe state list is universal\b"],
     [r"sufficient for the committed machine at fixed background",
      r"the universal state waits on the autonomous[- ]update unit"],
     (), ()),
    ("W-MEASURE",
     [r"\bmore likely\b", r"\bprobability that a history\b",
      r"\bthe typical history\b", r"\bon average the\b",
      r"\bmost histories are\b", r"\bwith high probability\b"],
     [r"counts are counting[- ]only"],
     (), ()),
    ("W-NEW-PHYSICS",
     [r"\bthis unit predicts\b", r"\bwe therefore predict\b",
      r"\bin the continuum limit\b", r"\bthis is spacetime\b",
      r"\bthe theory is confirmed\b", r"\ba new law\b",
      r"\bwe derive a new\b"],
     [r"no new physics claim"],
     (), ()),
)


# ===========================================================================
# SECTION G.  THE RUN.
# ===========================================================================

GATE_ORDER = (
    "G-SOURCES-PINNED", "G-NO-FLOAT", "G-S1-DISJOINT-CODE",
    "G-TEMPLATE-EXERCISED", "G-ARENA-REBUILT", "G-CORPUS-REBUILT",
    "G-RECORD-REBUILT", "G-OBJECT-CENSUS", "G-STATE-COMPONENTS",
    "G-STATE-SCREENS-THE-HISTORY", "G-STATE-READING-RELATIVE",
    "G-INVARIANCE-GROUPS", "G-DIRECTION-INVARIANCE",
    "G-LOCAL-ARITY-GROUP", "G-QUOTIENT-CENSUS",
    "G-DEPENDENCY-CYCLE", "G-CAST-UNIQUE-IN-THE-CLASS", "G-CAST-RESIDUE",
    "G-Q58-ARMS", "G-Q58-VERDICT", "G-COIN-FIBER", "G-MENU-LAW-SELECTED",
    "G-SEAM-KERNEL", "G-PARAMETERS", "G-OUTCOMES-REACHABLE",
    "G-CLAIMS-EQUAL", "G-REFERENTS-BOUND", "G-WALLS", "G-ANCHORS-CONSUMED",
    "G-NO-TYPED-COUNTS", "G-RECEIPT-TYPES", "G-HEAD-REBUILT",
    "G-TRANSCRIPT-BOUND", "G-READS-DECLARED",
)

SEAL_AT = {
    "inv_": "G-INVARIANCE-GROUPS",
    "arena": "G-ARENA-REBUILT", "corpus": "G-CORPUS-REBUILT",
    "record": "G-RECORD-REBUILT", "census": "G-OBJECT-CENSUS",
    "state": "G-STATE-COMPONENTS", "inv_": "G-INVARIANCE-GROUPS",
    "quotient": "G-QUOTIENT-CENSUS", "dep": "G-DEPENDENCY-CYCLE",
    "class_cast": "G-CAST-UNIQUE-IN-THE-CLASS", "q58": "G-Q58-ARMS",
    "coin": "G-COIN-FIBER", "seam": "G-SEAM-KERNEL",
    "param": "G-PARAMETERS", "recon": "G-RECORD-REBUILT",
}


KEY_GATE_EXACT = {
    "source_count": "G-SOURCES-PINNED",
    "source_mismatches": "G-SOURCES-PINNED",
    "source_mismatch_count": "G-SOURCES-PINNED",
    "float_offences": "G-NO-FLOAT", "float_offence_count": "G-NO-FLOAT",
    "region_offences": "G-S1-DISJOINT-CODE",
    "region_offence_count": "G-S1-DISJOINT-CODE",
    "region_census": "G-S1-DISJOINT-CODE", "region_count": "G-S1-DISJOINT-CODE",
    "template_families": "G-TEMPLATE-EXERCISED",
    "template_families_live": "G-TEMPLATE-EXERCISED",
    "cited_gluings": "G-OBJECT-CENSUS", "cited_chart_types": "G-OBJECT-CENSUS",
    "outcome_controls": "G-OUTCOMES-REACHABLE",
    "outcome_words": "G-OUTCOMES-REACHABLE",
    "outcome_reachable": "G-OUTCOMES-REACHABLE",
    "anchor_count": "G-ANCHORS-CONSUMED",
    "anchor_consumers": "G-ANCHORS-CONSUMED",
    "anchor_unconsumed": "G-ANCHORS-CONSUMED",
    "anchor_phantom_consumers": "G-ANCHORS-CONSUMED",
    "claim_rows": "G-CLAIMS-EQUAL", "claim_prose": "G-CLAIMS-EQUAL",
    "claim_fences": "G-CLAIMS-EQUAL", "render_tables": "G-CLAIMS-EQUAL",
    "paper_digest": "G-CLAIMS-EQUAL",
    "referent_universes": "G-REFERENTS-BOUND",
    "referent_occurrences": "G-REFERENTS-BOUND",
    "wall_count": "G-WALLS", "wall_patterns": "G-WALLS",
    "wall_positives": "G-WALLS",
    "typed_callers": "G-NO-TYPED-COUNTS",
    "typed_count_offences": "G-NO-TYPED-COUNTS",
    "typed_count_offence_count": "G-NO-TYPED-COUNTS",
    "exempt_tokens": "G-NO-TYPED-COUNTS",
    "exempt_tokens_unused": "G-NO-TYPED-COUNTS",
    "receipt_type_offences": "G-RECEIPT-TYPES",
    "receipt_type_offence_count": "G-RECEIPT-TYPES",
    "receipt_leaves": "G-RECEIPT-TYPES",
    "head_segments": "G-HEAD-REBUILT", "head_words": "G-HEAD-REBUILT",
    "head_segment_count": "G-HEAD-REBUILT",
    "head_fields_parsed": "G-HEAD-REBUILT",
    "head_mismatches": "G-HEAD-REBUILT",
    "transcript_rows": "G-TRANSCRIPT-BOUND",
    "ledger_rows": "G-TRANSCRIPT-BOUND",
    "transcript_stray": "G-TRANSCRIPT-BOUND",
    "transcript_missing": "G-TRANSCRIPT-BOUND",
    "reads_declared": "G-READS-DECLARED", "reads_stray": "G-READS-DECLARED",
    "reads_never": "G-READS-DECLARED", "reads_distinct": "G-READS-DECLARED",
    "reads_unpinnable": "G-READS-DECLARED",
}

UNSEALED_KEYS = {
    "gates": "counted after the last gate; the ledger's own rows carry it",
    "ledger_head": "the chain head, recomputable from the receipt's own rows",
    "mode": "a declared input, not a measurement",
    "mutant": "a declared input, not a measurement",
}


def gate_of_key(k):
    if k in KEY_GATE_EXACT:
        return KEY_GATE_EXACT[k]
    for pre, g in SEAL_AT.items():
        if k.startswith(pre):
            return g
    return None


class Run:
    """the delivery.  Gates are predicates over the payload and nothing else,
    which is what lets a falsifier move a measurement and be caught."""

    def __init__(self, mode="--run"):
        self.mode = mode
        self.led = ET.Ledger()
        self.tr = ET.Transcript()
        self.seal = ET.Seal()
        self.cr = ET.CountRegistry()
        self.claims = ET.Claims()
        self.ref = ET.ReferentRegistry()
        self.anchors = ET.AnchorSet(
            [ET.Anchor(n, needle, src, cons, floor=40)
             for (n, src, cons, needle) in ANCHORS])
        self.walls = [ET.SemanticWall(n, neg, pos, pol, lic)
                      for (n, neg, pos, pol, lic) in WALLS]
        self.reads = ET.ReadSet(REPO)
        self.sealed_keys = []
        self.render = {}

    # -- plumbing ---------------------------------------------------------
    def S(self, template, *names):
        return self.cr.stmt(template, **{n: None for n in names})

    def fire(self, gid, statement, ok, evidence, keys=()):
        for k in keys:
            self.seal.seal(k, self.P[k], gid)
            self.sealed_keys.append(k)
        self.led.gate(gid, statement, ok, evidence)
        self.tr.row(gid, ok, evidence)


def _measured_register(cr, P):
    for k, v in sorted(P.items()):
        if isinstance(v, bool):
            cr.measured(k, v, "computed by this run")
        elif isinstance(v, int):
            cr.measured(k, v, "computed by this run")
        elif isinstance(v, str):
            cr.measured(k, v, "decided by this run")
        else:
            cr.measured(k, len(v) if hasattr(v, "__len__") else v,
                        "the size of a computed structure")
    return cr


def head_segments(P):
    """the four verdict segments, every numeral interpolated from a measured
    name and every word chosen by a comparator function."""
    census = k_census_word(P["census_rows"])
    circ = k_circularity_word(P["dep_cycle_length"] > 0,
                              P["class_cast_solutions"],
                              P["class_cast_matches_declared"],
                              P["class_cast_residue"])
    q58 = k_q58_word(P["q58_arms_recovering"], P["q58_arms_refusing"])
    par = k_parameter_word(P["param_free"])
    s1 = ("CONTRACT-%s<OBJECTS=%d; COMPUTED-HERE=%d; CITED=%d; "
          "ACTORS=%d; CELLS=%d; EVENTS-REALISED=%d; HISTORIES=%d; "
          "BLOCKS=%d; COUNT-FIELDS=%d; MENU=%d; CHART-CLASSES=%d>") % (
        census, P["census_row_count"], P["census_computed_here"],
        P["census_cited"], P["arena_sites"], P["arena_cells"],
        P["corpus_distinct_events"], P["corpus_distinct_histories"],
        P["record_blocks"], P["record_count_fields"], P["arena_menu"],
        P["inv_link_graph_automorphisms"])
    s2 = ("CONTRACT-STATE-AT-FIXED-BACKGROUND-AND-INVARIANCE<"
          "STATE-COMPONENTS=%d; BACKGROUND=%d; "
          "COUNT-FIELDS=%d; RESIDUE-FIELDS=%d; SUCCESSORS=%d; "
          "EQUAL-RESIDUE-PAIRS-AGREEING=%d-OF-%d; "
          "DISTINCT-RESIDUE-COLLISIONS=%d-OF-%d; "
          "RELABELLINGS=%d; LAW-STABILIZER=%d; ARENA-STABILIZER=%d; "
          "DIRECTION-INDEX=%d; SPLITTINGS=%d; "
          "LOCAL-GROUP=%d; LOCAL-COLLAPSE-WIDTH=%d; "
          "HISTORIES-SURVIVING=%d-OF-%d; FIELDS-SURVIVING=%d-OF-%d; "
          "GAUGE-WORD=WITHHELD>") % (
        P["state_components"], P["state_background_components"],
        P["record_count_fields"], P["record_residue_fields"],
        P["state_successors_distinct"],
        P["state_equal_residue_agreements"], P["state_equal_residue_pairs"],
        P["state_distinct_residue_collisions"], P["state_distinct_residue_pairs"],
        P["inv_symmetric_group"], P["inv_law_stabilizer"],
        P["inv_arena_automorphisms"], P["inv_direction_index"],
        P["inv_direction_splittings"], P["inv_local_group_order"],
        P["inv_local_collapse_width"],
        P["quotient_histories_link"], P["quotient_histories"],
        P["quotient_fields_link"], P["quotient_fields"])
    s3 = ("CONTRACT-%s<CYCLE-LENGTH=%d; CAST-SOLUTIONS=%d; RESIDUE=%d; "
          "ARMS=%d; RECOVERING=%d; REFUSING=%d>") % (
        circ, P["dep_cycle_length"], P["class_cast_solutions"],
        P["class_cast_residue"], P["q58_arms_total"],
        P["q58_arms_recovering"], P["q58_arms_refusing"])
    s4 = ("CONTRACT-%s-%s<DECLARATIONS=%d; FREE=%d; "
          "INVARIANT-IN-THE-SUBSTRATE-CENSUS=%d; DERIVED=%d; "
          "RECONSTRUCTED-CONDITIONALLY=%d; INITIAL=%d; "
          "FREE-ROWS-A-LAW-SELECTS=%d; COIN-CLASSES=%d; SEAM-KERNEL=%d; "
          "DIRECTION-CHOICES=%d; "
          "UNRESOLVED=THE-GAUGE-QUOTIENT+THE-UNIVERSAL-STATE+"
          "THE-EXCITATION-CONTENT>") % (
        q58, par, P["param_total"], P["param_free"], P["param_invariant"],
        P["param_derived"], P["param_reconstructed"], P["param_initial"],
        P["param_free_selected_by_a_law"], P["coin_classes"], P["seam_kernel"],
        P["inv_direction_choices"])
    return [s1, s2, s3, s4], (census, circ, q58, par)


def outcome_controls():
    """#299: every pre-registered outcome word is shown REACHABLE by handing
    the comparator declared inputs it did not measure here."""
    rows = []
    rows.append(("CENSUS-TOTAL", k_census_word(
        [{"backing": "COMPUTED-HERE"}])))
    rows.append(("CENSUS-PARTIAL", k_census_word([{"backing": "NONE"}])))
    rows.append(("ACYCLIC", k_circularity_word(False, 1, True, 1)))
    rows.append(("CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS",
                 k_circularity_word(True, 1, True, 1)))
    rows.append(("CIRCULAR-CAST-UNIQUE-IN-THE-TRIANGULAR-CLASS-"
                 "UP-TO-THE-DIRECTION-DECLARATION",
                 k_circularity_word(True, 1, True, 2)))
    rows.append(("CIRCULAR-BLOCKED-AT-THE-CAST",
                 k_circularity_word(True, 2, False, 1)))
    rows.append(("Q58-EMERGENCE-GENERATOR-INDEPENDENT", k_q58_word(2, 0)))
    rows.append(("Q58-IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS",
                 k_q58_word(2, 1)))
    rows.append(("Q58-UNDECIDED-NO-SECOND-MECHANISM", k_q58_word(0, 1)))
    rows.append(("ISP-IS-ONE-THEORY", k_parameter_word(0)))
    rows.append(("ISP-IS-A-FAMILY", k_parameter_word(1)))
    return rows


# ===========================================================================
# SECTION H.  THE GATES, AS PREDICATES OVER THE PAYLOAD.
# ===========================================================================

CTX: dict = {}

SPELLED = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
           7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
           12: "twelve"}


def fmt(P, template, *names):
    cr = CTX["cr"]
    for n in names:
        v = P[n]
        cr.measured(n, v if isinstance(v, (int, str, bool)) else str(v),
                    "computed by this run")
    return cr.stmt(template, **{n: None for n in names})


def _paper_prose(text):
    """prose only: fenced blocks and rendered tables removed, since both are
    bound more tightly elsewhere."""
    t = ET.Claims.FENCE.sub(" ", text)
    return "\n".join(ln for ln in t.splitlines() if not ln.lstrip().startswith("|"))


def g_sources(P):
    ok = not P["source_mismatches"]
    return ok, fmt(P, "sources {source_count} mismatches {source_mismatch_count}",
                   "source_count", "source_mismatch_count")


def g_no_float(P):
    return not P["float_offences"], fmt(
        P, "float literals {float_offence_count} in the module",
        "float_offence_count")


def g_s1(P):
    return not P["region_offences"], fmt(
        P, "regions {region_count} offences {region_offence_count}",
        "region_count", "region_offence_count")


def g_template(P):
    return (P["template_families"] == P["template_families_live"]), fmt(
        P, "template families {template_families} exercised {template_families_live}",
        "template_families", "template_families_live")


def g_arena(P):
    a = CTX["anchors"].read("EPR-MULTIPARTITE", "G-ARENA-REBUILT")
    deg = "degree six" in a
    ok = (P["arena_sites"] == B_Q ** B_DIMENSION
          and P["arena_cells"] == P["arena_sites"] * P["arena_declared_directions"]
          and P["arena_parallel_classes"] == B_Q + 1
          and P["arena_groupings"] == len(b_raw_census()["parts"])
          and P["recon_degree"] * P["arena_sites"] == 2 * P["arena_cells"]
          and deg)
    return ok, fmt(P, "sites {arena_sites} cells {arena_cells} classes "
                      "{arena_parallel_classes} groupings {arena_groupings} "
                      "saturating {arena_saturating_groupings} degree {recon_degree}",
                   "arena_sites", "arena_cells", "arena_parallel_classes",
                   "arena_groupings", "arena_saturating_groupings", "recon_degree")


def g_corpus(P):
    ok = (P["corpus_slots"] == P["corpus_c1"] + P["corpus_c2"] + P["corpus_c3"]
          and P["corpus_c2"] == P["corpus_c1"] ** 2
          and P["corpus_distinct_histories"] <= P["corpus_slots"])
    return ok, fmt(P, "slots {corpus_slots} strict {corpus_c1} concatenations "
                      "{corpus_c2} window {corpus_c3} distinct "
                      "{corpus_distinct_histories} events {corpus_distinct_events}",
                   "corpus_slots", "corpus_c1", "corpus_c2", "corpus_c3",
                   "corpus_distinct_histories", "corpus_distinct_events")


def g_record(P):
    a = CTX["anchors"].read("REC-DEPTH", "G-RECORD-REBUILT")
    nums = anchor_numerals(a)
    ok = (nums == [P["record_max_blocks_in_a_history"], P["record_blocks"]]
          and P["record_block_sizes"] == [B_ARITY]
          and P["record_vanishing_histories"] ==
          P["record_colliding_histories"] - P["record_collision_classes"]
          and P["record_count_fields"] >= P["record_residue_fields"])
    return ok, fmt(P, "blocks {record_blocks} unwritten {record_unwritten_events} "
                      "partly {record_partly_unwritten_histories} silent "
                      "{record_histories_writing_nothing} bare "
                      "{record_distinct_bare_records} collisions "
                      "{record_collision_classes} colliding "
                      "{record_colliding_histories} fields {record_count_fields} "
                      "most blocks one history sees "
                      "{record_max_blocks_in_a_history}",
                   "record_blocks", "record_unwritten_events",
                   "record_partly_unwritten_histories",
                   "record_histories_writing_nothing",
                   "record_distinct_bare_records", "record_collision_classes",
                   "record_colliding_histories", "record_count_fields",
                   "record_max_blocks_in_a_history")


def g_census(P):
    A = CTX["anchors"]
    carrier_text = A.read("REC-CARRIER", "G-OBJECT-CENSUS")
    carrier = anchor_numerals(carrier_text)
    occ = anchor_numerals(A.read("OCC-CARRIER", "G-OBJECT-CENSUS"))
    chart = anchor_numerals(A.read("SEC-CHART", "G-OBJECT-CENSUS"))
    tick = A.read("HOR-TICK", "G-OBJECT-CENSUS")
    rows = P["census_rows"]
    classes_ok = all(r["class"] in CLASS_ALPHABET for r in rows)
    backing_ok = all(r["backing"] in BACKING_ALPHABET for r in rows)
    names_ok = len({r["object"] for r in rows}) == len(rows)
    chart_row = [r for r in rows if r["object"] == "CHART"]
    tick_row = [r for r in rows if r["object"] == "TICK"]
    ok = (classes_ok and backing_ok and names_ok
          and carrier[0] == P["arena_cells"] and carrier[1] == P["arena_cells"]
          and SPELLED[P["arena_sites"]] in carrier_text
          and occ[0] == P["arena_cells"] and occ[-1] == P["arena_sites"]
          and chart_row and chart_row[0]["cardinality"] == chart[-1]
          and tick_row and "One Site a Tick" in tick
          and P["census_backed"] == P["census_row_count"])
    return ok, fmt(P, "rows {census_row_count} computed {census_computed_here} "
                      "cited {census_cited} backed {census_backed}",
                   "census_row_count", "census_computed_here", "census_cited",
                   "census_backed")


def g_state_components(P):
    ok = (P["state_components"] == len(STATE_COMPONENTS)
          and P["state_background_components"] == len(STATE_BACKGROUND))
    return ok, fmt(P, "state components {state_components} background "
                      "{state_background_components}",
                   "state_components", "state_background_components")


def g_state_screens(P):
    ok = (P["state_equal_residue_agreements"] == P["state_equal_residue_pairs"]
          and P["state_equal_residue_disagreements"] == 0
          and P["state_distinct_residue_collisions"] == 0
          and P["state_successors_distinct"] == P["record_residue_fields"])
    return ok, fmt(P, "equal-residue pairs {state_equal_residue_pairs} agreeing "
                      "{state_equal_residue_agreements} distinct-residue pairs "
                      "{state_distinct_residue_pairs} colliding "
                      "{state_distinct_residue_collisions} successors "
                      "{state_successors_distinct}",
                   "state_equal_residue_pairs", "state_equal_residue_agreements",
                   "state_distinct_residue_pairs",
                   "state_distinct_residue_collisions",
                   "state_successors_distinct")


def g_state_reading(P):
    a = CTX["anchors"].read("COUP-RESIDUE", "G-STATE-READING-RELATIVE")
    ok = (anchor_numerals(a) == [B_Q]
          and P["state_reading_a_menus"] == P["record_residue_fields"]
          and P["state_reading_b_menus"] == P["record_count_fields"]
          and P["state_reading_b_menus"] > P["state_reading_a_menus"])
    return ok, fmt(P, "reading A menus {state_reading_a_menus} reading B menus "
                      "{state_reading_b_menus} residue fields "
                      "{record_residue_fields} count fields {record_count_fields}",
                   "state_reading_a_menus", "state_reading_b_menus",
                   "record_residue_fields", "record_count_fields")


def g_invariance_groups(P):
    a = CTX["anchors"].read("REC-NAMING", "G-INVARIANCE-GROUPS")
    nums = anchor_numerals(a)
    ok = (nums[0] == P["inv_link_graph_automorphisms"]
          and nums[1] == P["inv_arena_automorphisms"]
          and P["inv_two_labellings_agree"]
          and P["inv_law_stabilizer"] == P["inv_link_graph_automorphisms"]
          and P["inv_law_blind_to_direction"]
          and P["inv_direction_index"] * P["inv_arena_automorphisms"]
          == P["inv_link_graph_automorphisms"]
          and P["inv_direction_index"] == P["inv_direction_splittings"])
    return ok, fmt(P, "symmetric group {inv_symmetric_group} law stabilizer "
                      "{inv_law_stabilizer} link automorphisms "
                      "{inv_link_graph_automorphisms} arena automorphisms "
                      "{inv_arena_automorphisms} index {inv_direction_index} "
                      "splittings {inv_direction_splittings}",
                   "inv_symmetric_group", "inv_law_stabilizer",
                   "inv_link_graph_automorphisms", "inv_arena_automorphisms",
                   "inv_direction_index", "inv_direction_splittings")


def g_direction_invariance(P):
    a = CTX["anchors"].read("AID-GAUGE", "G-DIRECTION-INVARIANCE")
    nums = anchor_numerals(a)
    # the parent's own sentence names the three counts a rival declaration
    # returns; this run rebuilt every declaration's census and compares them.
    ok = (P["arena_saturating_groupings"] in nums
          and P["arena_strict_triples"] in nums
          and P["arena_flat_quadruples"] in nums
          and P["inv_direction_profiles_agreeing"] == P["inv_direction_choices"]
          and P["inv_direction_census_numbers"] > 0)
    return ok, fmt(P, "declarations {inv_direction_choices} agreeing "
                      "{inv_direction_profiles_agreeing} census numbers "
                      "{inv_direction_census_numbers}",
                   "inv_direction_choices", "inv_direction_profiles_agreeing",
                   "inv_direction_census_numbers")


B_ARITH_SEVEN = 7


def g_local_arity(P):
    w = dict((a, b) for a, b in P["inv_local_widths"])
    ok = (P["inv_local_global_count"] == 1
          and w[0] == P["inv_local_group_order"] ** len(CTX["c1_first"])
          and w[P["inv_local_collapse_width"]] == P["inv_local_global_count"]
          and w[P["inv_local_collapse_width"] - 1] > P["inv_local_global_count"]
          and P["inv_local_c1_uniform"]
          and P["inv_local_c1_threshold"] == P["inv_local_collapse_width"])
    return ok, fmt(P, "local group {inv_local_group_order} global "
                      "{inv_local_global_count} collapse width "
                      "{inv_local_collapse_width} histories "
                      "{inv_local_c1_histories}",
                   "inv_local_group_order", "inv_local_global_count",
                   "inv_local_collapse_width", "inv_local_c1_histories")


def g_quotient(P):
    ok = (P["quotient_histories_link"] <= P["quotient_histories_arena"]
          <= P["quotient_histories"]
          and P["quotient_fields_link"] <= P["quotient_fields_arena"]
          <= P["quotient_fields"]
          and P["quotient_fields_arena"] == P["quotient_fields_link"])
    return ok, fmt(P, "histories {quotient_histories} arena "
                      "{quotient_histories_arena} link {quotient_histories_link} "
                      "fields {quotient_fields} arena {quotient_fields_arena} "
                      "link {quotient_fields_link}",
                   "quotient_histories", "quotient_histories_arena",
                   "quotient_histories_link", "quotient_fields",
                   "quotient_fields_arena", "quotient_fields_link")


def g_dependency(P):
    ok = (P["dep_cycles"] > 0 and P["dep_actor_record_cycles"] > 0
          and P["dep_edges"] == len(DEPENDENCY_EDGES))
    return ok, fmt(P, "nodes {dep_nodes} edges {dep_edges} cycles {dep_cycles} "
                      "through the cast and the record {dep_actor_record_cycles} "
                      "shortest {dep_actor_record_cycle_length}",
                   "dep_nodes", "dep_edges", "dep_cycles",
                   "dep_actor_record_cycles", "dep_actor_record_cycle_length")


def g_cast_unique(P):
    ok = (P["class_cast_solutions"] == 1 and P["class_cast_matches_declared"]
          and P["recon_set_equality"] and P["recon_certificate"] == "CERTIFIED"
          and P["recon_cast_size"] == P["arena_sites"])
    return ok, fmt(P, "cast solutions {class_cast_solutions} certificate "
                      "{recon_certificate} derived cast {recon_cast_size} "
                      "threshold {recon_threshold}",
                   "class_cast_solutions", "recon_certificate",
                   "recon_cast_size", "recon_threshold")


def g_cast_residue(P):
    ok = (P["class_cast_residue"] == P["inv_direction_index"]
          and P["class_cast_residue"] > 1
          and P["inv_declared_splitting_offered"])
    return ok, fmt(P, "residue {class_cast_residue} index {inv_direction_index} "
                      "candidate classes {inv_candidate_direction_classes}",
                   "class_cast_residue", "inv_direction_index",
                   "inv_candidate_direction_classes")


def g_q58_arms(P):
    arms = P["q58_arms"]
    ok = (len(arms) == P["q58_arms_total"]
          and P["q58_arms_recovering"] + P["q58_arms_refusing"] == len(arms)
          and all(a["certificate"] in ("CERTIFIED", "THRESHOLD-UNDETERMINED",
                                       "TOKEN-IN-NO-ACTOR",
                                       "TOKEN-NOT-IN-EXACTLY-TWO",
                                       "NO-RECORD-BLOCKS") for a in arms)
          and len({a["arm"] for a in arms}) == len(arms))
    return ok, fmt(P, "arms {q58_arms_total} recovering {q58_arms_recovering} "
                      "refusing {q58_arms_refusing} triangular {q58_triangular_arms}",
                   "q58_arms_total", "q58_arms_recovering", "q58_arms_refusing",
                   "q58_triangular_arms")


def g_q58_verdict(P):
    ok = (P["q58_arms_recovering"] > 1 and P["q58_arms_refusing"] > 0
          and P["q58_split_is_triangularity"]
          and not P["q58_split_is_the_block_size"]
          and len(P["q58_mechanism_kinds"]) > 1)
    return ok, fmt(P, "recovering {q58_arms_recovering} refusing "
                      "{q58_arms_refusing} triangularity decides "
                      "{q58_split_is_triangularity} block size decides "
                      "{q58_split_is_the_block_size}",
                   "q58_arms_recovering", "q58_arms_refusing",
                   "q58_split_is_triangularity", "q58_split_is_the_block_size")


def g_coin(P):
    a = CTX["anchors"].read("COUP-COIN", "G-COIN-FIBER")
    nums = anchor_numerals(a)
    ok = (nums[0] == P["coin_classes"] and nums[1] == P["coin_grover_classes"]
          and P["coin_ring_solutions"] == P["coin_classes"] * P["coin_norm_solutions"]
          and P["coin_classes"] == len(P["coin_ratios"]))
    return ok, fmt(P, "ring solutions {coin_ring_solutions} classes "
                      "{coin_classes} phase units {coin_norm_solutions} "
                      "Grover classes {coin_grover_classes}",
                   "coin_ring_solutions", "coin_classes", "coin_norm_solutions",
                   "coin_grover_classes")


def g_menu(P):
    ok = (P["arena_menu"] == P["arena_translation_subgroups"]
          and P["arena_menu"] == B_Q + B_ARITY)
    return ok, fmt(P, "subgroups {arena_translation_subgroups} menu {arena_menu}",
                   "arena_translation_subgroups", "arena_menu")


def g_seam(P):
    a = CTX["anchors"].read("SEC2-SEAM", "G-SEAM-KERNEL")
    nums = anchor_numerals(a)
    ok = (nums[0] == P["seam_rank"] and nums[1] == P["seam_columns"]
          and nums[2] == P["seam_kernel"]
          and P["seam_rank"] + P["seam_kernel"] == P["seam_columns"])
    return ok, fmt(P, "rows {seam_rows} columns {seam_columns} rank {seam_rank} "
                      "kernel {seam_kernel}",
                   "seam_rows", "seam_columns", "seam_rank", "seam_kernel")


def g_parameters(P):
    a = CTX["anchors"].read("NDEP-CARRIED", "G-PARAMETERS")
    ok = ("NO TESTED NUMERAL IS REPRODUCED" in a
          and P["param_total"] == (P["param_free"] + P["param_invariant"]
                                   + P["param_derived"] + P["param_initial"]
                                   + P["param_reconstructed"])
          and P["param_free_selected_by_a_law"] == 0
          and P["param_free"] > 0)
    return ok, fmt(P, "declarations {param_total} free {param_free} invariant "
                      "{param_invariant} derived {param_derived} "
                      "reconstructed-conditionally {param_reconstructed} "
                      "initial {param_initial} free rows a law selects "
                      "{param_free_selected_by_a_law}",
                   "param_total", "param_free", "param_invariant",
                   "param_derived", "param_reconstructed", "param_initial",
                   "param_free_selected_by_a_law")


def g_outcomes(P):
    rows = P["outcome_controls"]
    ok = all(want == got for want, got in rows) and len(rows) == P["outcome_words"]
    return ok, fmt(P, "outcome words {outcome_words} reachable {outcome_reachable}",
                   "outcome_words", "outcome_reachable")


def g_anchors(P):
    A = CTX["anchors"]
    P["anchor_count"] = len(A.by_name)
    P["anchor_consumers"] = len({a.consumer for a in A.by_name.values()})
    P["anchor_unconsumed"] = sum(
        1 for a in A.by_name.values() if a.consumer not in a.read_by)
    _gates = set(CTX["ledger"].names())
    P["anchor_phantom_consumers"] = sum(
        1 for a in A.by_name.values() if a.consumer not in _gates)
    try:
        CTX["anchors"].verify_consumption(CTX["ledger"])
        bad = ""
    except ET.CheckFail as exc:
        bad = exc.detail
    ok = ((not bad) and P["anchor_unconsumed"] == 0
          and P["anchor_phantom_consumers"] == 0)
    return ok, fmt(P, "anchors {anchor_count} consumers {anchor_consumers} "
                      "unconsumed {anchor_unconsumed} phantom "
                      "{anchor_phantom_consumers}",
                   "anchor_count", "anchor_consumers", "anchor_unconsumed",
                   "anchor_phantom_consumers")


def g_claims(P):
    try:
        got = CTX["claims"].gate(CTX["paper"])
        bad = ""
    except ET.CheckFail as exc:
        got, bad = {}, exc.detail
    ok = not bad
    CTX["claims_counts"] = got
    return ok, fmt(P, "rows {claim_rows} prose {claim_prose} fences {claim_fences}",
                   "claim_rows", "claim_prose", "claim_fences")


def g_referents(P):
    try:
        got = CTX["ref"].gate(_paper_prose(CTX["paper"]))
        bad = ""
    except ET.CheckFail as exc:
        got, bad = {"occurrences_checked": 0}, exc.detail
    P["referent_occurrences"] = got["occurrences_checked"]
    CTX["referent_detail"] = bad
    ok = (not bad) and got["occurrences_checked"] > 0
    return ok, fmt(P, "universes {referent_universes} occurrences checked "
                      "{referent_occurrences}",
                   "referent_universes", "referent_occurrences")


def g_walls(P):
    order = CTX["anchors"].read("PLAN-WALLS", "G-WALLS")
    named = [w.name for w in CTX["walls"]]
    standing_present = ("W-RECONSTRUCTION-IS-NOT-DERIVATION" in named
                        and "W-INVARIANCE-IS-NOT-GAUGE" in named
                        and "derivation" in order and "gauge" in order)
    bad = [] if standing_present else ["the two standing walls are not built"]
    for w in CTX["walls"]:
        try:
            w.scan(CTX["paper"], CTX["claim_texts"])
        except ET.CheckFail as exc:
            bad.append(exc.detail)
    ok = not bad
    return ok, fmt(P, "walls {wall_count} patterns {wall_patterns} standing "
                      "sentences {wall_positives}",
                   "wall_count", "wall_patterns", "wall_positives")


def g_typed(P):
    ok = (not P["typed_count_offences"]
          and P["exempt_tokens_unused"] == 0)
    return ok, fmt(
        P, "statement builders audited {typed_callers} offences "
           "{typed_count_offence_count} exemptions {exempt_tokens} unused "
           "{exempt_tokens_unused}",
        "typed_callers", "typed_count_offence_count", "exempt_tokens",
        "exempt_tokens_unused")


def g_receipt_types(P):
    return not P["receipt_type_offences"], fmt(
        P, "receipt leaves {receipt_leaves} type offences "
           "{receipt_type_offence_count}",
        "receipt_leaves", "receipt_type_offence_count")


def g_head(P):
    """the head is not trusted to its renderer: every numeral position is
    parsed back out of the emitted string and compared, as an integer, against
    the receipt leaf it names."""
    bad = []
    for seg, want in zip(P["head_segments"], HEAD_FIELDS):
        got = k_parse_head(seg)
        for field, key in want:
            if field not in got:
                bad.append(field)
            elif got[field] != P[key]:
                bad.append(field)
    ok = not bad and len(P["head_segments"]) == len(HEAD_FIELDS)
    return ok, fmt(P, "segments {head_segment_count} fields parsed "
                      "{head_fields_parsed} mismatches {head_mismatches}",
                   "head_segment_count", "head_fields_parsed", "head_mismatches")


def g_transcript(P):
    ok = (P["transcript_rows"] == P["ledger_rows"] and P["transcript_stray"] == 0
          and P["transcript_missing"] == 0)
    return ok, fmt(P, "transcript rows {transcript_rows} ledger rows "
                      "{ledger_rows} stray {transcript_stray} missing "
                      "{transcript_missing}",
                   "transcript_rows", "ledger_rows", "transcript_stray",
                   "transcript_missing")


def g_reads(P):
    ok = (P["reads_stray"] == 0 and P["reads_never"] == 0
          and P["reads_declared"] == P["source_count"] + P["reads_unpinnable"])
    return ok, fmt(P, "declared {reads_declared} pinned {source_count} "
                      "unpinnable {reads_unpinnable} stray {reads_stray} "
                      "never read {reads_never} distinct {reads_distinct}",
                   "reads_declared", "source_count", "reads_unpinnable",
                   "reads_stray", "reads_never", "reads_distinct")


GATE_FN = {
    "G-SOURCES-PINNED": g_sources, "G-NO-FLOAT": g_no_float,
    "G-S1-DISJOINT-CODE": g_s1, "G-TEMPLATE-EXERCISED": g_template,
    "G-ARENA-REBUILT": g_arena, "G-CORPUS-REBUILT": g_corpus,
    "G-RECORD-REBUILT": g_record, "G-OBJECT-CENSUS": g_census,
    "G-STATE-COMPONENTS": g_state_components,
    "G-STATE-SCREENS-THE-HISTORY": g_state_screens,
    "G-STATE-READING-RELATIVE": g_state_reading,
    "G-INVARIANCE-GROUPS": g_invariance_groups,
    "G-DIRECTION-INVARIANCE": g_direction_invariance,
    "G-LOCAL-ARITY-GROUP": g_local_arity,
    "G-QUOTIENT-CENSUS": g_quotient,
    "G-DEPENDENCY-CYCLE": g_dependency,
    "G-CAST-UNIQUE-IN-THE-CLASS": g_cast_unique,
    "G-CAST-RESIDUE": g_cast_residue,
    "G-Q58-ARMS": g_q58_arms, "G-Q58-VERDICT": g_q58_verdict,
    "G-COIN-FIBER": g_coin, "G-MENU-LAW-SELECTED": g_menu,
    "G-SEAM-KERNEL": g_seam, "G-PARAMETERS": g_parameters,
    "G-OUTCOMES-REACHABLE": g_outcomes, "G-ANCHORS-CONSUMED": g_anchors,
    "G-CLAIMS-EQUAL": g_claims, "G-REFERENTS-BOUND": g_referents,
    "G-WALLS": g_walls, "G-NO-TYPED-COUNTS": g_typed,
    "G-RECEIPT-TYPES": g_receipt_types, "G-HEAD-REBUILT": g_head,
    "G-TRANSCRIPT-BOUND": g_transcript, "G-READS-DECLARED": g_reads,
}

GATE_STATEMENT = {
    "G-SOURCES-PINNED": "every repository read is at its pinned digest",
    "G-NO-FLOAT": "the module carries no float literal and no float call",
    "G-S1-DISJOINT-CODE": "no reconstructor and no comparator reaches a builder",
    "G-TEMPLATE-EXERCISED": "every template family's check is called live here",
    "G-ARENA-REBUILT": "the arena is rebuilt from the field and the declaration",
    "G-CORPUS-REBUILT": "the committed corpus is rebuilt from its own drivers",
    "G-RECORD-REBUILT": "the record layer is rebuilt from the corpus",
    "G-OBJECT-CENSUS": "every census row is classed and backed",
    "G-STATE-COMPONENTS": "the instantaneous state is listed once and totally",
    "G-STATE-SCREENS-THE-HISTORY": "the state screens the history off the update",
    "G-STATE-READING-RELATIVE": "what the state must carry is reading-relative",
    "G-INVARIANCE-GROUPS": "the relabelling groups are measured and nested",
    "G-DIRECTION-INVARIANCE": "the direction declaration moves no census number",
    "G-LOCAL-ARITY-GROUP": "the local relabelling group collapses at a width",
    "G-QUOTIENT-CENSUS": "what survives the quotient is counted",
    "G-DEPENDENCY-CYCLE": "the dependency graph is written and its cycles located",
    "G-CAST-UNIQUE-IN-THE-CLASS": "the record admits exactly one cast",
    "G-CAST-RESIDUE": "the fixed point carries the direction residue",
    "G-Q58-ARMS": "every declared mechanism is run through one reconstructor",
    "G-Q58-VERDICT": "the split between the mechanisms is measured, not asserted",
    "G-COIN-FIBER": "the covariant coin family is enumerated exactly",
    "G-MENU-LAW-SELECTED": "the admissible grains are the coset partitions",
    "G-SEAM-KERNEL": "the seam's undetermined entries are counted by rank",
    "G-PARAMETERS": "every declaration is classed and none free is law-selected",
    "G-OUTCOMES-REACHABLE": "every pre-registered outcome word is reachable",
    "G-ANCHORS-CONSUMED": "every anchor is consumed by the gate that names it",
    "G-CLAIMS-EQUAL": "the paper's tables, claims and fences match by equality",
    "G-REFERENTS-BOUND": "every prose numeral binds to its own universe",
    "G-WALLS": "the reading walls hold on the paper's own bytes",
    "G-NO-TYPED-COUNTS": "no published statement types a numeral",
    "G-RECEIPT-TYPES": "the receipt carries no float and no opaque leaf",
    "G-HEAD-REBUILT": "the head is parsed back and compared with the receipt",
    "G-TRANSCRIPT-BOUND": "the transcript is the ledger, row for row",
    "G-READS-DECLARED": "the read set is exactly the declared set",
}

STATE_COMPONENTS = (
    ("THE-COUNT-FIELD", "one non-negative integer per cell",
     "the geometry: the division count the weld identifies with the metric"),
    ("THE-AMPLITUDE", "one ring element per cell",
     "the quantum state the coin and the shift act on"),
    ("THE-BRANCH-WEIGHT", "one exact rational",
     "the bookkeeping weight the emission law multiplies"),
)

STATE_BACKGROUND = (
    ("THE-ACTOR-SET", "the cast the arena declares"),
    ("THE-DIRECTION-DECLARATION", "which classes are links"),
    ("THE-COIN", "the covariant unitary chosen from its family"),
    ("THE-ORDER", "coin before or after the residue"),
    ("THE-ORIENTATION", "the sign of the shift"),
    ("THE-READING", "the Born menu or the record menu"),
)

HEAD_FIELDS = (
    (("OBJECTS", "census_row_count"), ("COMPUTED-HERE", "census_computed_here"),
     ("CITED", "census_cited"), ("ACTORS", "arena_sites"),
     ("CELLS", "arena_cells"), ("EVENTS-REALISED", "corpus_distinct_events"),
     ("HISTORIES", "corpus_distinct_histories"), ("BLOCKS", "record_blocks"),
     ("COUNT-FIELDS", "record_count_fields"), ("MENU", "arena_menu"),
     ("CHART-CLASSES", "inv_link_graph_automorphisms")),
    (("STATE-COMPONENTS", "state_components"),
     ("BACKGROUND", "state_background_components"),
     ("COUNT-FIELDS", "record_count_fields"),
     ("RESIDUE-FIELDS", "record_residue_fields"),
     ("SUCCESSORS", "state_successors_distinct"),
     ("RELABELLINGS", "inv_symmetric_group"),
     ("LAW-STABILIZER", "inv_law_stabilizer"),
     ("ARENA-STABILIZER", "inv_arena_automorphisms"),
     ("DIRECTION-INDEX", "inv_direction_index"),
     ("SPLITTINGS", "inv_direction_splittings"),
     ("LOCAL-GROUP", "inv_local_group_order"),
     ("LOCAL-COLLAPSE-WIDTH", "inv_local_collapse_width")),
    (("CYCLE-LENGTH", "dep_cycle_length"),
     ("CAST-SOLUTIONS", "class_cast_solutions"),
     ("RESIDUE", "class_cast_residue"), ("ARMS", "q58_arms_total"),
     ("RECOVERING", "q58_arms_recovering"), ("REFUSING", "q58_arms_refusing")),
    (("DECLARATIONS", "param_total"), ("FREE", "param_free"),
     ("INVARIANT-IN-THE-SUBSTRATE-CENSUS", "param_invariant"),
     ("DERIVED", "param_derived"),
     ("RECONSTRUCTED-CONDITIONALLY", "param_reconstructed"),
     ("INITIAL", "param_initial"),
     ("FREE-ROWS-A-LAW-SELECTS", "param_free_selected_by_a_law"),
     ("COIN-CLASSES", "coin_classes"), ("SEAM-KERNEL", "seam_kernel"),
     ("DIRECTION-CHOICES", "inv_direction_choices")),
)


# ===========================================================================
# SECTION I.  THE RENDERING, THE RUN, THE FALSIFIERS, THE PROMOTION.
# ===========================================================================

def build_render(P, claims):
    """every table, claim and fenced block the paper carries is rendered HERE
    and matched against the paper's own bytes by two-way equality."""
    R = {}
    R["census"] = claims.table(
        "census", ("object", "class", "cardinality", "backing", "reading"),
        [(r["object"], r["class"], com(r["cardinality"]), r["backing"],
          r["reading"]) for r in P["census_rows"]])
    R["state"] = claims.table(
        "state", ("component", "shape", "what it carries"),
        [(a, b, c) for (a, b, c) in STATE_COMPONENTS])
    R["background"] = claims.table(
        "background", ("declaration", "what it fixes"),
        [(a, b) for (a, b) in STATE_BACKGROUND])
    R["screening"] = claims.table(
        "screening", ("quantity", "value"),
        [("count fields over the corpus", com(P["record_count_fields"])),
         ("residue fields", com(P["record_residue_fields"])),
         ("one-step successors", com(P["state_successors_distinct"])),
         ("equal-residue field pairs", com(P["state_equal_residue_pairs"])),
         ("of which the successor agrees", com(P["state_equal_residue_agreements"])),
         ("distinct-residue field pairs", com(P["state_distinct_residue_pairs"])),
         ("of which the successor agrees", com(P["state_distinct_residue_collisions"])),
         ("Born-menu values", com(P["state_reading_a_menus"])),
         ("record-menu values", com(P["state_reading_b_menus"]))])
    R["invariance"] = claims.table(
        "invariance", ("group", "order", "what it preserves",
                       "measured status"),
        [("all relabellings", com(P["inv_symmetric_group"]),
          "nothing of the arena", "MOVES-THE-SUBSTRATE-CENSUS"),
         ("the round law's stabilizer", com(P["inv_law_stabilizer"]),
          "which groups the law admits", "SUBSTRATE-CENSUS-INVARIANT"),
         ("the link structure's automorphisms",
          com(P["inv_link_graph_automorphisms"]),
          "which pairs are linked", "SUBSTRATE-CENSUS-INVARIANT"),
         ("the arena's automorphisms", com(P["inv_arena_automorphisms"]),
          "the link structure and the direction classes",
          "SUBSTRATE-CENSUS-INVARIANT"),
         ("the local relabellings at one event",
          com(P["inv_local_group_order"]),
          "nothing beyond the event's own order",
          "COUNT-INVARIANT-AT-AND-ABOVE-THE-WIDTH")])
    R["quotient"] = claims.table(
        "quotient", ("object", "before", "modulo the arena", "modulo the links"),
        [("histories", com(P["quotient_histories"]),
          com(P["quotient_histories_arena"]), com(P["quotient_histories_link"])),
         ("count fields", com(P["quotient_fields"]),
          com(P["quotient_fields_arena"]), com(P["quotient_fields_link"]))])
    R["local"] = claims.table(
        "local", ("window width", "locally coherent assignments"),
        [(com(w), com(c)) for w, c in P["inv_local_widths"]])
    R["dependency"] = claims.table(
        "dependency", ("from", "to", "the edge"),
        [(a, b, w) for (a, b, w) in DEPENDENCY_EDGES])
    R["arms"] = claims.table(
        "arms", ("mechanism", "kind", "actors per event", "blocks",
                 "block sizes", "certificate", "cast recovered"),
        [(a["arm"], a["mechanism"], com(a["event_arity"]), com(a["blocks"]),
          "+".join("%s x %s" % (com(n), com(s)) for s, n in a["block_sizes"]),
          a["certificate"], "yes" if a["cast_recovered"] else "no")
         for a in P["q58_arms"]])
    R["parameters"] = claims.table(
        "parameters", ("declaration", "what it fixes", "fiber", "class",
                       "a measured law selects it", "where it is measured"),
        [(a, b, c, d, e, f) for (a, b, c, d, e, f) in P["param_rows"]])
    R["outcomes"] = claims.table(
        "outcomes", ("pre-registered word", "the control that emits it"),
        [(w, "a declared input handed to the comparator")
         for w, _g in P["outcome_controls"]])
    R["sources"] = claims.table(
        "sources", ("path", "sha256-12"),
        [(k, v) for k, v in sorted(SOURCES.items())])
    return R


CLAIM_TEXTS = (
    "ISP is a parameterized family; actor cardinality is identifiable from "
    "records in a measured triangle-writing class; the full gauge quotient, "
    "universal state and physical excitation content remain unresolved.",
    "The construction is circular, and at the committed corpus the record "
    "admits exactly one cast inside the triangular representation class.",
    "That is uniqueness inside a declared representation class, and it is not "
    "a fixed point of the actor-record-emission dynamics.",
    "What the record does not fix is the direction declaration, and the "
    "residue is an index the record offers and does not choose.",
    "The reconstruction is not generator-independent: it holds across every "
    "mechanism that writes triangles and refuses on every mechanism that does "
    "not.",
    "So the answer to the emergence question is identifiability within a "
    "generative class.",
    "Recovering a datum from records that were generated with it is "
    "identifiability and not derivation, and this paper never promotes the one "
    "to the other.",
    "The count field enters the quantum update only through its residue, and "
    "enters the record menu whole, so what the state must carry is "
    "reading-relative.",
    "The state below is sufficient for the committed machine at fixed "
    "background, and the universal state waits on the autonomous-update unit.",
    "The round law is blind to which classes are declared, and the four "
    "declarations return the same substrate census.",
    "That blindness is measured on the substrate census alone; the coupled "
    "dynamics, the readings, the orientation and any interaction a later unit "
    "builds are outside the sweep.",
    "The gauge word is withheld here: an invariance becomes a gauge "
    "redundancy only when every physical observable and every experiment take "
    "identical values across the orbit, and this corpus has no operational "
    "observables to test that with.",
    "counts are counting-only, and no fraction in this paper is a "
    "probability.",
    "one arena, the committed corpus, and no claim beyond the committed "
    "corpus is made anywhere here.",
    "no new physics claim is made beyond the census's own measurements.",
)


def full_run(mode="--run", mutant=None, write=False):
    CTX.clear()
    reads = ET.ReadSet(REPO)
    reads.install()
    reads.active = True
    cr = ET.CountRegistry()
    for tok, why in EXEMPT_TOKENS:
        cr.exempt_token(tok, why)
    CTX["cr"] = cr

    src = read_text(SELF_REL)
    tpl_text = read_text(TEMPLATE_REL)
    mismatch = []
    for rel, want in sorted(SOURCES.items()):
        got = sha12(os.path.join(REPO, rel))
        if got != want:
            mismatch.append("%s %s != %s" % (rel, got, want))
    paper = ""
    if mode in ("--run", "--no-write", "--selftest"):
        pth = os.path.join(REPO, PAPER_REL)
        if os.path.exists(pth):
            paper = read_text(PAPER_REL)
        ET.require_object(mode, pth, paper)

    P = measure()
    P["source_count"] = len(SOURCES)
    P["source_mismatches"] = mismatch
    P["source_mismatch_count"] = len(mismatch)
    P["float_offences"] = audit_no_floats(src)
    P["float_offence_count"] = len(P["float_offences"])
    P["region_offences"] = audit_regions(src)
    P["region_offence_count"] = len(P["region_offences"])
    P["region_census"] = sorted(region_census(src).items())
    P["region_count"] = len(P["region_census"])
    live = [cid for (_l, _n, cid) in ET.FAMILIES if cid in TEMPLATE_CALLS
            and re.search(TEMPLATE_CALLS[cid], src)]
    P["template_families"] = len(ET.FAMILIES)
    P["template_families_live"] = len(live)
    P["outcome_controls"] = [[w, g] for w, g in outcome_controls()]
    P["outcome_words"] = len(P["outcome_controls"])
    P["outcome_reachable"] = sum(1 for w, g in P["outcome_controls"] if w == g)

    segs, words = head_segments(P)
    P["head_segments"] = segs
    P["head_words"] = list(words)
    P["head_segment_count"] = len(segs)
    P["head_fields_parsed"] = sum(len(f) for f in HEAD_FIELDS)
    P["head_mismatches"] = 0

    claims = ET.Claims()
    render = build_render(P, claims)
    for t in CLAIM_TEXTS:
        claims.claim(t)
    for s in segs:
        claims.fence(s)
    P["claim_rows"] = len(claims.rows)
    P["claim_prose"] = sum(claims.prose.values())
    P["claim_fences"] = sum(claims.fences.values())
    P["render_tables"] = len(render)

    ref = ET.ReferentRegistry()
    _universes(ref, P)
    P["referent_universes"] = len(ref.universes)
    P["referent_occurrences"] = 0

    anchors = ET.AnchorSet([ET.Anchor(n, needle, s, c, floor=40)
                            for (n, s, c, needle) in ANCHORS])
    sources_text = {s: read_text(s) for s in {a[1] for a in ANCHORS}}
    anchors.locate(sources_text, paper if paper else None)
    if mode == "--render":
        for _n, _s, _c, _needle in ANCHORS:
            anchors.read(_n, _c)
    P["anchor_count"] = len(ANCHORS)
    P["anchor_consumers"] = len({a[2] for a in ANCHORS})

    walls = [ET.SemanticWall(n, neg, pos, pol, lic)
             for (n, neg, pos, pol, lic) in WALLS]
    P["wall_count"] = len(walls)
    P["wall_patterns"] = sum(len(w.negative) for w in walls)
    P["wall_positives"] = sum(len(w.positive) for w in walls)

    P["typed_callers"] = len(TYPED_CALLERS)
    P["typed_count_offences"] = (cr.audit_module(src, TYPED_CALLERS)
                                 + audit_typed_deep(src, TYPED_CALLERS,
                                                    tuple(cr.exempt)))
    P["typed_count_offence_count"] = len(P["typed_count_offences"])
    P["exempt_tokens"] = len(EXEMPT_TOKENS)
    P["exempt_tokens_unused"] = sum(1 for t, _w in EXEMPT_TOKENS if t not in src)
    P["receipt_type_offences"] = []
    P["receipt_type_offence_count"] = 0
    P["receipt_leaves"] = 0
    P["transcript_rows"] = 0
    P["ledger_rows"] = 0
    P["transcript_stray"] = 0
    P["transcript_missing"] = 0
    P["reads_declared"] = len(SOURCES) + 1
    P["reads_unpinnable"] = 1
    P["reads_stray"] = 0
    P["reads_never"] = 0
    P["reads_distinct"] = 0
    P["anchor_unconsumed"] = 0
    P["paper_digest"] = ET.bytes_digest(paper.encode("utf-8"))
    P["mode"] = mode
    P["mutant"] = mutant or "none"

    led = ET.Ledger()
    tr = ET.Transcript()
    seal = ET.Seal()
    CTX.update({"paper": paper, "claims": claims, "claim_texts": list(CLAIM_TEXTS),
                "ref": ref, "anchors": anchors, "walls": walls, "ledger": led,
                "src": src, "template": tpl_text, "render": render,
                "c1_first": [h for t, h in b_build_corpus()[0] if t == "C1"][0]})

    if mutant:
        MUTANTS[mutant]["apply"](P)

    tr.say("CONTRACT -- THE THEORY CONTRACT -- the unit the pin names")
    tr.say("mode %s   mutant %s" % (mode, mutant or "none"))
    tr.say("")
    fired = []
    # --render is the paper-free diagnostic mode: it fires every gate whose
    # object is the payload and skips exactly the four whose object is the
    # paper, and it writes nothing.  It is strictly weaker than the delivery
    # path and says so.
    paperless = ("G-ANCHORS-CONSUMED", "G-CLAIMS-EQUAL", "G-REFERENTS-BOUND",
                 "G-WALLS")
    for gid in GATE_ORDER:
        if gid in ("G-TRANSCRIPT-BOUND", "G-READS-DECLARED"):
            continue
        if mode == "--render" and gid in paperless:
            continue
        ok, ev = GATE_FN[gid](P)
        for k in sorted(P):
            if gate_of_key(k) == gid and k not in seal.seals \
                    and k not in UNSEALED_KEYS:
                seal.seal(k, P[k], gid)
        led.gate(gid, GATE_STATEMENT[gid], ok, ev)
        tr.row(gid, ok, ev)
        fired.append(gid)

    # -- the closing gates -------------------------------------------------
    P["transcript_rows"] = len(tr.parse()) + 2
    P["ledger_rows"] = len(led.rows) + 2
    if mutant and MUTANTS[mutant]["gate"] == "G-TRANSCRIPT-BOUND":
        MUTANTS[mutant]["apply"](P)
    ok, ev = GATE_FN["G-TRANSCRIPT-BOUND"](P)
    for k in sorted(P):
        if gate_of_key(k) == "G-TRANSCRIPT-BOUND" and k not in seal.seals:
            seal.seal(k, P[k], "G-TRANSCRIPT-BOUND")
    led.gate("G-TRANSCRIPT-BOUND", GATE_STATEMENT["G-TRANSCRIPT-BOUND"], ok, ev)
    tr.row("G-TRANSCRIPT-BOUND", ok, ev)
    # the two objects that cannot be pinned against themselves: this module,
    # which its own AST gates audit, and the paper, which is the object under
    # test.  Both are declared, and the count is derived rather than typed.
    declared = sorted(SOURCES) + [SELF_REL]
    P["reads_unpinnable"] = 1
    if paper:
        declared = declared + [PAPER_REL]
        P["reads_unpinnable"] = 2
    P["reads_declared"] = len(declared)
    seen = collections.Counter(p for p in reads.log if not p.endswith(".tmp"))
    P["reads_stray"] = len(set(seen) - set(declared))
    P["reads_never"] = len(set(declared) - set(seen))
    P["reads_distinct"] = len(seen)
    if mutant and MUTANTS[mutant]["gate"] == "G-READS-DECLARED":
        MUTANTS[mutant]["apply"](P)
    ok, ev = GATE_FN["G-READS-DECLARED"](P)
    for k in sorted(P):
        if gate_of_key(k) == "G-READS-DECLARED" and k not in seal.seals:
            seal.seal(k, P[k], "G-READS-DECLARED")
    led.gate("G-READS-DECLARED", GATE_STATEMENT["G-READS-DECLARED"], ok, ev)
    tr.row("G-READS-DECLARED", ok, ev)

    P["gates"] = len(led.rows)
    P["ledger_head"] = led.recompute_chain()
    for k, why in sorted(UNSEALED_KEYS.items()):
        if k not in seal.seals:
            seal.declare_unsealed(k, why)
    uncovered = sorted(k for k in P
                       if k not in seal.seals and k not in seal.unsealed)
    if uncovered and mode != "--render":
        raise ET.CheckFail("T-SEAL-PROMOTION",
                           "payload keys neither sealed at a gate nor "
                           "declared: %s" % uncovered)

    tr.say("")
    tr.say("VERDICT")
    for s in segs:
        tr.say("  " + s)
    text = tr.text()
    bound = tr.bind(led, text)
    bad = []
    receipt_type_walk(P, bad)
    if bad:
        raise ET.CheckFail("G-RECEIPT-TYPES", "opaque leaves: %s" % bad[:4])

    if write:
        digests = ET.promote(seal, led, P, text,
                             os.path.join(REPO, RECEIPT_REL),
                             os.path.join(REPO, OUTPUT_REL))
    else:
        digests = {"receipt": bound, "side": bound}
    return P, led, tr, text, digests


TEMPLATE_CALLS = {
    "T-SEAL-PROMOTION": r"ET\.promote|ET\.Seal",
    "T-TRANSCRIPT-BOUND": r"tr\.bind|ET\.Transcript",
    "T-WALL-SEMANTIC": r"w\.scan|ET\.SemanticWall",
    "T-ANCHOR-CONSUMED": r"anchors\.verify_consumption|ET\.AnchorSet",
    "T-CLAIMS-EQUAL": r"claims\.gate|ET\.Claims",
    "T-REFERENT-BOUND": r"ref\.gate|ET\.ReferentRegistry",
    "T-NO-TYPED-COUNTS": r"cr\.audit_module|ET\.CountRegistry",
    "T-FALSIFIER-POISONS": r"ET\.FalsifierHarness",
    "T-READ-SET": r"reads\.install|ET\.ReadSet",
}

EXEMPT_TOKENS = (("sha256-12", "the name of the digest format, not a count"),)

TYPED_CALLERS = ("stmt", "fmt", "claim", "fence", "table", "gate", "row", "say")


def audit_typed_deep(src, callers, exempt):
    """the TPL-2 subspecies the template's own AST leg cannot see: a numeral
    reaching a statement builder through a %-format, a concatenation or an
    integer offset rather than as a direct string argument."""
    tree = ast.parse(src)
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fname = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
        if fname not in callers:
            continue
        for sub in ast.walk(node):
            if sub is node:
                continue
            if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                probe = sub.value
                for tok in exempt:
                    probe = probe.replace(tok, " ")
                if re.search(r"(?<![\w])\d+(?![\w])", probe):
                    out.append("line %d: a numeral inside a builder's string"
                               % sub.lineno)
            if isinstance(sub, ast.Constant) and isinstance(sub.value, int) \
                    and not isinstance(sub.value, bool):
                out.append("line %d: an integer offset inside a builder"
                           % sub.lineno)
    return out


def _universes(ref, P):
    """numerals bound to the universe their sentence is about."""
    def vals(prefixes):
        out = set()
        for k, v in P.items():
            if not any(k.startswith(p) for p in prefixes):
                continue
            if isinstance(v, bool):
                continue
            if isinstance(v, int):
                out.add(v)
        return out
    base = {B_Q, B_DIMENSION, B_ARITY, B_ROUNDS, DIM, NACT, 1, 2}
    ref.universe("THE-INVARIANCE", ["invariance", "naming", "relabelling",
                                    "automorphism", "splitting", "stabilizer",
                                    "quotient", "symmetric group", "orbit",
                                    "gauge"],
                 vals(["inv_", "quotient"]) | base,
                 {(P["inv_arena_automorphisms"],
                   P["inv_link_graph_automorphisms"]),
                  (P["quotient_histories_link"], P["quotient_histories"]),
                  (P["quotient_fields_link"], P["quotient_fields"])})
    ref.universe("THE-ARMS", ["arm", "mechanism", "reconstructor",
                              "generating", "generator"],
                 vals(["q58"]) | base,
                 {(P["q58_arms_recovering"], P["q58_arms_total"]),
                  (P["q58_arms_refusing"], P["q58_arms_total"])})
    ref.universe("THE-PARAMETERS", ["parameter", "declaration", "fiber",
                                    "free item", "coin", "seam"],
                 vals(["param", "coin", "seam"]) | base,
                 {(P["param_free"], P["param_total"]),
                  (P["coin_grover_classes"], P["coin_classes"])})
    ref.universe("THE-STATE", ["state", "amplitude", "residue", "successor",
                               "menu", "walk"],
                 vals(["state", "record_residue", "record_count"]) | base, set())
    ref.universe("THE-RECORD", ["record", "history", "corpus", "block",
                                "count field", "cast", "cast solution", "cycle",
                                "dependency"],
                 vals(["record", "corpus", "class_cast", "dep", "recon"]) | base,
                 {(P["record_collision_classes"], P["record_colliding_histories"]),
                  (P["record_max_blocks_in_a_history"], P["record_blocks"])})
    ref.universe("THE-ARENA", ["arena", "cell", "site", "actor", "grouping",
                               "direction", "class", "event", "census",
                               "object", "carrier"],
                 vals(["arena", "census", "recon", "cited"]) | base,
                 {(P["record_max_blocks_in_a_history"], P["record_blocks"])})


# ===========================================================================
# SECTION J.  THE FALSIFIERS.  Each names the measured key it must move; the
# harness digests that key before and after and refuses a recipe that leaves
# it identical, and the death must occur at the gate the recipe names.
# ===========================================================================

def _bump(key):
    def f(P):
        v = P[key]
        P[key] = v + 1 if isinstance(v, int) and not isinstance(v, bool) else (
            not v if isinstance(v, bool) else str(v) + "-MOVED")
        return P
    return f


def _flip(key):
    def f(P):
        P[key] = not P[key]
        return P
    return f


def _plant(key, value):
    def f(P):
        P[key] = value
        return P
    return f


def _corrupt_rows(P):
    P["census_rows"] = [dict(r) for r in P["census_rows"]]
    P["census_rows"][0]["class"] = "INVENTED"
    return P


def _corrupt_arms(P):
    P["q58_arms"] = [dict(a) for a in P["q58_arms"]]
    P["q58_arms"][0]["certificate"] = "INVENTED-CERTIFICATE"
    return P


def _corrupt_head(P):
    P["head_segments"] = list(P["head_segments"])
    P["head_segments"][0] = re.sub(r"OBJECTS=\d+", "OBJECTS=" + str(
        P["census_row_count"] + 1), P["head_segments"][0])
    return P


def _corrupt_outcomes(P):
    P["outcome_controls"] = [list(r) for r in P["outcome_controls"]]
    P["outcome_controls"][0][1] = "NOT-THE-WORD"
    return P


def _corrupt_widths(P):
    P["inv_local_widths"] = [[w, c] for w, c in P["inv_local_widths"]]
    P["inv_local_widths"][P["inv_local_collapse_width"]][1] += 1
    return P


def _corrupt_paper(marker, replacement):
    def f(P):
        CTX["paper"] = CTX["paper"].replace(marker, replacement, 1)
        P["paper_digest"] = ET.bytes_digest(CTX["paper"].encode("utf-8"))
        return P
    return f


MUTANTS = {}


def _mk(name, gate, description, target, apply):
    MUTANTS[name] = {"gate": gate, "description": description,
                     "target": target, "apply": apply}


_mk("MUT-SOURCE", "G-SOURCES-PINNED",
    "plants a digest mismatch in the pinned source list",
    "source_mismatches", _plant("source_mismatches", ["planted mismatch"]))
_mk("MUT-FLOAT", "G-NO-FLOAT", "plants a float offence in the module audit",
    "float_offences", _plant("float_offences", ["planted line"]))
_mk("MUT-REGION", "G-S1-DISJOINT-CODE",
    "plants a comparator reaching a builder", "region_offences",
    _plant("region_offences", ["k_planted reaches b_planted"]))
_mk("MUT-TEMPLATE", "G-TEMPLATE-EXERCISED",
    "drops one template family from the live set", "template_families_live",
    lambda P: P.update(template_families_live=P["template_families_live"] - 1) or P)
_mk("MUT-ARENA", "G-ARENA-REBUILT", "moves the cell count off the product",
    "arena_cells", _bump("arena_cells"))
_mk("MUT-CORPUS", "G-CORPUS-REBUILT", "moves the corpus slot count",
    "corpus_slots", _bump("corpus_slots"))
_mk("MUT-RECORD", "G-RECORD-REBUILT", "moves the record block count",
    "record_blocks", _bump("record_blocks"))
_mk("MUT-CENSUS-CLASS", "G-OBJECT-CENSUS",
    "types a census class outside the declared alphabet", "census_rows",
    _corrupt_rows)
_mk("MUT-STATE-COUNT", "G-STATE-COMPONENTS",
    "adds a state component the list does not carry", "state_components",
    _bump("state_components"))
_mk("MUT-SCREEN", "G-STATE-SCREENS-THE-HISTORY",
    "plants a disagreement between two equal-residue count fields",
    "state_equal_residue_disagreements", _bump("state_equal_residue_disagreements"))
_mk("MUT-READING", "G-STATE-READING-RELATIVE",
    "collapses the record menu onto the Born menu", "state_reading_b_menus",
    lambda P: P.update(state_reading_b_menus=P["state_reading_a_menus"]) or P)
_mk("MUT-INVARIANCE", "G-INVARIANCE-GROUPS", "moves the link automorphism order",
    "inv_link_graph_automorphisms", _bump("inv_link_graph_automorphisms"))
_mk("MUT-DIRECTION", "G-DIRECTION-INVARIANCE",
    "makes one direction declaration disagree with the others",
    "inv_direction_profiles_agreeing",
    lambda P: P.update(
        inv_direction_profiles_agreeing=P["inv_direction_choices"] - 1) or P)
_mk("MUT-LOCAL", "G-LOCAL-ARITY-GROUP",
    "moves the count at the collapse width off the global count",
    "inv_local_widths", _corrupt_widths)
_mk("MUT-QUOTIENT", "G-QUOTIENT-CENSUS",
    "makes the coarser quotient finer than the finer one",
    "quotient_histories_link",
    lambda P: P.update(
        quotient_histories_link=P["quotient_histories_arena"] + 1) or P)
_mk("MUT-CYCLE", "G-DEPENDENCY-CYCLE",
    "empties the cast-and-record cycle set", "dep_actor_record_cycles",
    _plant("dep_actor_record_cycles", 0))
_mk("MUT-CAST-UNIQUE", "G-CAST-UNIQUE-IN-THE-CLASS",
    "reports a second cast solution", "class_cast_solutions",
    _bump("class_cast_solutions"))
_mk("MUT-RESIDUE", "G-CAST-RESIDUE",
    "collapses the direction residue to one", "class_cast_residue",
    _plant("class_cast_residue", 1))
_mk("MUT-ARM", "G-Q58-ARMS", "invents a certificate word on one arm",
    "q58_arms", _corrupt_arms)
_mk("MUT-Q58", "G-Q58-VERDICT",
    "reports the measured split criterion as not deciding the arms",
    "q58_split_is_triangularity", _flip("q58_split_is_triangularity"))
_mk("MUT-COIN", "G-COIN-FIBER", "moves the coin class count", "coin_classes",
    _bump("coin_classes"))
_mk("MUT-MENU", "G-MENU-LAW-SELECTED", "moves the menu off the subgroup count",
    "arena_menu", _bump("arena_menu"))
_mk("MUT-SEAM", "G-SEAM-KERNEL", "moves the seam kernel off the corank",
    "seam_kernel", _bump("seam_kernel"))
_mk("MUT-PARAM", "G-PARAMETERS",
    "reports a free declaration as law-selected", "param_free_selected_by_a_law",
    _bump("param_free_selected_by_a_law"))
_mk("MUT-OUTCOME", "G-OUTCOMES-REACHABLE",
    "makes one pre-registered word unreachable", "outcome_controls",
    _corrupt_outcomes)
def _phantom_consumer(P):
    """the family (d) disease as a paper produces it: an anchor's declared
    consumer renamed to a gate that never ran."""
    A = CTX["anchors"]
    name = sorted(A.by_name)[0]
    A.by_name[name].consumer = "G-A-GATE-THAT-NEVER-RAN"
    P["anchor_phantom_consumers"] = 0
    return P


_mk("MUT-ANCHOR", "G-ANCHORS-CONSUMED",
    "renames an anchor's declared consumer to a gate that never ran",
    "anchor_phantom_consumers", _phantom_consumer)
_mk("MUT-CLAIM", "G-CLAIMS-EQUAL",
    "inverts a delivered result inside a rendered table row", "paper_digest",
    _corrupt_paper("| CERTIFIED | yes |", "| CERTIFIED | no |"))
_mk("MUT-REFERENT", "G-REFERENTS-BOUND",
    "plants a cross-universe numeral in the paper's prose", "paper_digest",
    _corrupt_paper("The corpus has been asked, unit by unit, what it can",
                   "The corpus has been asked, unit by unit, what its 999999 "
                   "objects can"))
_mk("MUT-WALL", "G-WALLS",
    "plants a generator-independence claim in the paper's own voice",
    "paper_digest",
    _corrupt_paper("## 1.", "The actors emerge from the record.\n\n## 1."))
_mk("MUT-TYPED", "G-NO-TYPED-COUNTS", "plants a typed numeral offence",
    "typed_count_offences", _plant("typed_count_offences", ["line 1: '27'"]))
_mk("MUT-RECEIPT", "G-RECEIPT-TYPES", "plants an opaque receipt leaf",
    "receipt_type_offences", _plant("receipt_type_offences", ["$.planted"]))
_mk("MUT-HEAD", "G-HEAD-REBUILT",
    "moves one numeral of the head away from its receipt leaf", "head_segments",
    _corrupt_head)
_mk("MUT-TRANSCRIPT", "G-TRANSCRIPT-BOUND", "inserts a transcript row",
    "transcript_rows", _bump("transcript_rows"))
_mk("MUT-READS", "G-READS-DECLARED", "plants a stray read", "reads_stray",
    _bump("reads_stray"))


def falsifier_rows():
    return [ET.Falsifier(n, m["gate"], m["description"], m["target"],
                         _hook(n)) for n, m in sorted(MUTANTS.items())]


def _hook(name):
    def apply(payload, ledger):
        MUTANTS[name]["apply"](payload)
        gid = MUTANTS[name]["gate"]
        ok, ev = GATE_FN[gid](payload)
        ledger.gate(gid, GATE_STATEMENT[gid], ok, ev)
    return apply


_BASE: dict = {}


def _fresh():
    if not _BASE:
        P, led, tr, text, _d = full_run(mode="--no-write")
        _BASE["P"] = P
        _BASE["ctx"] = dict(CTX)
        _BASE["paper"] = CTX["paper"]
        _BASE["sources_text"] = {s2: read_text(s2)
                                 for s2 in {a[1] for a in ANCHORS}}
    import copy
    CTX.clear()
    CTX.update(_BASE["ctx"])
    fresh_anchors = ET.AnchorSet([ET.Anchor(n, needle, src, cons, floor=40)
                                  for (n, src, cons, needle) in ANCHORS])
    fresh_anchors.locate(_BASE["sources_text"], _BASE["paper"] or None)
    for _n, _s, _c, _needle in ANCHORS:
        fresh_anchors.read(_n, _c)
    CTX["anchors"] = fresh_anchors
    CTX["cr"] = ET.CountRegistry()
    for tok, why in EXEMPT_TOKENS:
        CTX["cr"].exempt_token(tok, why)
    led = ET.Ledger()
    for gid in GATE_ORDER:
        led.gate(gid, GATE_STATEMENT[gid], True, "replayed for the harness")
    CTX["ledger"] = led
    return copy.deepcopy(_BASE["P"]), ET.Ledger()


COVERAGE_WAIVER = {
    "T-FALSIFIER-COVERAGE":
        "the coverage check cannot be falsified by a recipe that moves a "
        "measurement, because it reads the gate list rather than the payload; "
        "its forcing is machine-checked below",
}


def _coverage_forcing():
    """the waiver's forcing, checked by machine rather than described: hand
    coverage a gate list carrying a gate no recipe targets, and it must raise."""
    H = ET.FalsifierHarness(falsifier_rows())
    led = ET.Ledger()
    for gid in GATE_ORDER:
        led.gate(gid, GATE_STATEMENT[gid], True, "replayed for the forcing")
    led.gate("G-A-GATE-NO-RECIPE-TARGETS", "the forcing's own probe", True,
             "planted")
    try:
        H.coverage(led, COVERAGE_WAIVER, {"T-FALSIFIER-COVERAGE": True})
    except ET.CheckFail:
        return True
    return False


def run_falsifiers():
    H = ET.FalsifierHarness(falsifier_rows())
    rows = []
    for f in H.rows:
        rows.append(H.run_one(f, _fresh))
    offenders = H.audit_descriptions(read_text(SELF_REL))
    forced = _coverage_forcing()
    led = ET.Ledger()
    for gid in GATE_ORDER:
        led.gate(gid, GATE_STATEMENT[gid], True, "replayed for the coverage leg")
    cov = H.coverage(led, COVERAGE_WAIVER,
                     {"T-FALSIFIER-COVERAGE": forced})
    cov["waiver_forced"] = forced
    return rows, offenders, cov


# ===========================================================================
# SECTION K.  THE CLI (#82).
# ===========================================================================

USAGE = ("usage: contract_exact.py "
         "[--run|--no-write|--selftest|--list-gates|--list-mutants|"
         "--mutant NAME|--render]")


def main(argv):
    if len(argv) == 1:
        argv = argv + ["--run"]
    flag = argv[1]
    if flag == "--list-gates":
        for g in GATE_ORDER:
            print(g)
        return 0
    if flag == "--list-mutants":
        for n in sorted(MUTANTS):
            print("%-18s %-32s %s" % (n, MUTANTS[n]["gate"],
                                      MUTANTS[n]["description"]))
        return 0
    if flag == "--render":
        P, led, tr, text, _d = full_run(mode="--render")
        for k, v in CTX["render"].items():
            print("<<<TABLE %s>>>" % k)
            print(v)
            print()
        print("<<<FENCES>>>")
        for s in P["head_segments"]:
            print("```")
            print(s)
            print("```")
            print()
        print("<<<CLAIMS>>>")
        for c in CLAIM_TEXTS:
            print("- " + c)
        return 0
    if flag == "--selftest":
        rows, offenders, cov = run_falsifiers()
        for r in rows:
            print("%-18s died at %-32s target moved %s"
                  % (r["mutant"], r["died_at"], r["target_moved"]))
        print("description offenders %d" % len(offenders))
        print("coverage %s" % cov)
        if offenders:
            return 1
        print("SELFTEST PASS: %d recipes, each moving its named measurement and "
              "dying at its named gate; nothing written" % len(rows))
        return 0
    if flag == "--mutant":
        if len(argv) < 3 or argv[2] not in MUTANTS:
            print(USAGE)
            return 2
        name = argv[2]
        try:
            full_run(mode="--no-write", mutant=name)
        except ET.CheckFail as exc:
            print("%s died at %s :: %s" % (name, exc.check, exc.detail[:120]))
            return 1 if exc.check == MUTANTS[name]["gate"] else 3
        print("%s SURVIVED" % name)
        return 3
    if flag in ("--run", "--no-write"):
        P, led, tr, text, dig = full_run(mode=flag, write=(flag == "--run"))
        sys.stdout.write(text)
        print("")
        print("receipt %s  transcript %s" % (dig["receipt"], dig["side"]))
        return 0
    print(USAGE)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
